#Laniatus Games Studio Inc. | Python Metin II Server Warnings Statement interrupted by a preprocessor statement:
#The original statement from the file sal.h starts with:
#    __inner_fallthrough_dec
#Preprocessor-interrupted statements cannot be handled by this converter.
#The remainder of the header file sal.h is ignored.

class marriage: #this class replaces the original namespace 'marriage'
    class TWeddingInfo:
        def __init__(self, time, pid1, pid2):
            self.dwTime = time
            self.dwPID1 = pid1
            self.dwPID2 = pid2

    class TWedding:

        def __init__(self, time, dwMapIndex, pid1, pid2):
            self.dwTime = time
            self.dwMapIndex = dwMapIndex
            self.dwPID1 = pid1
            self.dwPID2 = pid2

    def less_than(self, lhs, rhs):
        return lhs.dwTime < rhs.dwTime

    def greater_than(self, lhs, rhs):
        return lhs.dwTime > rhs.dwTime

    def greater_than(self, lhs, rhs):
        return lhs.dwTime > rhs.dwTime

    class TMarriage:

        def __init__(self, _pid1, _pid2, _love_point, _time, _is_married, name1, name2):
            self.pid1 = _pid1
            self.pid2 = _pid2
            self.love_point = _love_point
            self.time = _time
            self.is_married = _is_married
            self.name1 = name1
            self.name2 = name2

        def GetOther(self, PID):
            if pid1 == PID:
                return pid2

            if pid2 == PID:
                return pid1

            return 0

    class CManager(singleton):
        def __init__(self):
            pass

        def close(self):
            pass

        def Initialize(self):
            szQuery = str(['\0' for _ in range(1024)])

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
            snprintf(szQuery, sizeof(szQuery), "SELECT pid1, pid2, love_point, time, is_married, p1.name, p2.name FROM marriage, player%s as p1, player%s as p2 WHERE p1.id = pid1 AND p2.id = pid2", GetTablePostfix(), GetTablePostfix())

            pmsg_delete = unique_ptr(CDBManager.instance().DirectQuery("DELETE FROM marriage WHERE is_married = 0"))
            pmsg = unique_ptr(CDBManager.instance().DirectQuery(szQuery))

            pRes = pmsg.Get()
            sys_log(0, "MarriageList(size=%lu)", pRes.uiNumRows)

            if pRes.uiNumRows > 0:
                uiRow = 0
                while uiRow != pRes.uiNumRows:
                    row = mysql_fetch_row(pRes.pSQLResult)

                    pid1 = 0
                    str_to_number(pid1, row[0])
                    pid2 = 0
                    str_to_number(pid2, row[1])
                    love_point = 0
                    str_to_number(love_point, row[2])
                    time = 0
                    str_to_number(time, row[3])
                    is_married = 0
                    str_to_number(is_married, row[4])
                    name1 = row[5]
                    name2 = row[6]

                    pMarriage = TMarriage(pid1, pid2, love_point, time, is_married, name1, name2)
                    m_Marriages.insert(pMarriage)
                    m_MarriageByPID.insert((pid1, pMarriage))
                    m_MarriageByPID.insert((pid2, pMarriage))

                    sys_log(0, "Marriage %lu: LP:%d TM:%u ST:%d %10lu:%16s %10lu:%16s ", uiRow, love_point, time, is_married, pid1, name1, pid2, name2)
                    uiRow += 1
            return ((not DefineConstants.false))

        def Get(self, dwPlayerID):
            it = m_MarriageByPID.find(dwPlayerID)

            if it != m_MarriageByPID.end():
                return it.second

            return None

        def IsMarried(self, dwPlayerID):
            return Get(dwPlayerID) is not None

        def Add(self, dwPID1, dwPID2, szName1, szName2):
            now = CClientManager.instance().GetCurrentTime()
            if IsMarried(dwPID1) or IsMarried(dwPID2):
                sys_err("cannot marry already married character. %d - %d", dwPID1, dwPID2)
                return

            Align(dwPID1, dwPID2)

            szQuery = str(['\0' for _ in range(512)])
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
            snprintf(szQuery, sizeof(szQuery), "INSERT INTO marriage(pid1, pid2, love_point, time) VALUES (%u, %u, 0, %u)", dwPID1, dwPID2, now)

            pmsg = unique_ptr(CDBManager.instance().DirectQuery(szQuery))

            res = pmsg.Get()
            if res.uiAffectedRows == 0 or res.uiAffectedRows == -1:
                sys_err("cannot insert marriage")
                return

            sys_log(0, "MARRIAGE ADD %u %u", dwPID1, dwPID2)

            pMarriage = TMarriage(dwPID1, dwPID2, 0, now, 0, szName1, szName2)
            m_Marriages.insert(pMarriage)
            m_MarriageByPID.insert((dwPID1, pMarriage))
            m_MarriageByPID.insert((dwPID2, pMarriage))

            p = TPacketMarriageAdd()
            p.dwPID1 = dwPID1
            p.dwPID2 = dwPID2
            p.tMarryTime = now
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
            strlcpy(p.szName1, szName1, sizeof(p.szName1))
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
            strlcpy(p.szName2, szName2, sizeof(p.szName2))
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
            CClientManager.instance().ForwardPacket(LG_HEADER_DG_MARRIAGE_ADD, p, sizeof(p))

        def Remove(self, dwPID1, dwPID2):
            pMarriage = Get(dwPID1)

            if pMarriage:
                sys_log(0, "Break Marriage pid1 %d pid2 %d Other %d", dwPID1, dwPID2, pMarriage.GetOther(dwPID1))
            if pMarriage is None or pMarriage.GetOther(dwPID1) != dwPID2:
                it = m_MarriageByPID.begin()

                while it is not m_MarriageByPID.end():
                    sys_log(0, "Marriage List pid1 %d pid2 %d", it.second.pid1, it.second.pid2)
                    it += 1
                sys_err("not under marriage : PID:%u %u", dwPID1, dwPID2)
                return

            Align(dwPID1, dwPID2)

            szQuery = str(['\0' for _ in range(512)])
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
            snprintf(szQuery, sizeof(szQuery), "DELETE FROM marriage WHERE pid1 = %u AND pid2 = %u", dwPID1, dwPID2)

            pmsg = unique_ptr(CDBManager.instance().DirectQuery(szQuery))

            res = pmsg.Get()
            if res.uiAffectedRows == 0 or res.uiAffectedRows == -1:
                sys_err("cannot delete marriage : PID:%u %u", dwPID1, dwPID2)
                return

            sys_log(0, "MARRIAGE REMOVE PID:%u %u", dwPID1, dwPID2)

            m_Marriages.erase(pMarriage)
            m_MarriageByPID.erase(dwPID1)
            m_MarriageByPID.erase(dwPID2)

            p = TPacketMarriageRemove()
            p.dwPID1 = dwPID1
            p.dwPID2 = dwPID2
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
            CClientManager.instance().ForwardPacket(LG_HEADER_DG_MARRIAGE_REMOVE, p, sizeof(p))

            pMarriage = None

        def Update(self, dwPID1, dwPID2, iLovePoint, byMarried):
            pMarriage = Get(dwPID1)
            if pMarriage is None or pMarriage.GetOther(dwPID1) != dwPID2:
                sys_err("not under marriage : %u %u", dwPID1, dwPID2)
                return

            Align(dwPID1, dwPID2)

            szQuery = str(['\0' for _ in range(512)])
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
            snprintf(szQuery, sizeof(szQuery), "UPDATE marriage SET love_point = %d, is_married = %d WHERE pid1 = %u AND pid2 = %u", iLovePoint, byMarried, pMarriage.pid1, pMarriage.pid2)

            pmsg = unique_ptr(CDBManager.instance().DirectQuery(szQuery))

            res = pmsg.Get()
            if res.uiAffectedRows == 0 or res.uiAffectedRows == -1:
                sys_err("cannot update marriage : PID:%u %u", dwPID1, dwPID2)
                return

            sys_log(0, "MARRIAGE UPDATE PID:%u %u LP:%u ST:%d", dwPID1, dwPID2, iLovePoint, byMarried)
            pMarriage.love_point = iLovePoint
            pMarriage.is_married = byMarried

            p = TPacketMarriageUpdate()
            p.dwPID1 = dwPID1
            p.dwPID2 = dwPID2
            p.iLovePoint = pMarriage.love_point
            p.byMarried = pMarriage.is_married
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
            CClientManager.instance().ForwardPacket(LG_HEADER_DG_MARRIAGE_UPDATE, p, sizeof(p))

        def EngageToMarriage(self, dwPID1, dwPID2):
            pMarriage = Get(dwPID1)
            if pMarriage is None or pMarriage.GetOther(dwPID1) != dwPID2:
                sys_err("not under marriage : PID:%u %u", dwPID1, dwPID2)
                return

            if pMarriage.is_married:
                sys_err("already married, cannot change engage to marry : PID:%u %u", dwPID1, dwPID2)
                return

            Align(dwPID1, dwPID2)

            szQuery = str(['\0' for _ in range(512)])
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
            snprintf(szQuery, sizeof(szQuery), "UPDATE marriage SET is_married = 1 WHERE pid1 = %u AND pid2 = %u", pMarriage.pid1, pMarriage.pid2)

            pmsg = unique_ptr(CDBManager.instance().DirectQuery(szQuery))

            res = pmsg.Get()
            if res.uiAffectedRows == 0 or res.uiAffectedRows == -1:
                sys_err("cannot change engage to marriage : PID:%u %u", dwPID1, dwPID2)
                return

            sys_log(0, "MARRIAGE ENGAGE->MARRIAGE PID:%u %u", dwPID1, dwPID2)
            pMarriage.is_married = 1

            p = TPacketMarriageUpdate()
            p.dwPID1 = dwPID1
            p.dwPID2 = dwPID2
            p.iLovePoint = pMarriage.love_point
            p.byMarried = pMarriage.is_married
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
            CClientManager.instance().ForwardPacket(LG_HEADER_DG_MARRIAGE_UPDATE, p, sizeof(p))

        def ReadyWedding(self, dwMapIndex, dwPID1, dwPID2):
            dwStartTime = CClientManager.instance().GetCurrentTime()
            m_pqWeddingStart.push(TWedding(dwStartTime + 5, dwMapIndex, dwPID1, dwPID2))

        def EndWedding(self, dwPID1, dwPID2):
            it = m_mapRunningWedding.find((dwPID1, dwPID2))
            if it == m_mapRunningWedding.end():
                sys_err("try to end wedding %u %u", dwPID1, dwPID2)
                return

            w = it.second

            p = TPacketWeddingEnd()
            p.dwPID1 = w.dwPID1
            p.dwPID2 = w.dwPID2
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
            CClientManager.instance().ForwardPacket(LG_HEADER_DG_WEDDING_END, p, sizeof(p))
            m_mapRunningWedding.erase(it)

        def OnSetup(self, peer):
            it = m_Marriages.begin()
            while it is not m_Marriages.end():
                pMarriage = *it

                    p = TPacketMarriageAdd()
                    p.dwPID1 = pMarriage.pid1
                    p.dwPID2 = pMarriage.pid2
                    p.tMarryTime = pMarriage.time
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
                    strlcpy(p.szName1, pMarriage.name1.c_str(), sizeof(p.szName1))
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
                    strlcpy(p.szName2, pMarriage.name2.c_str(), sizeof(p.szName2))
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
                    peer.EncodeHeader(LG_HEADER_DG_MARRIAGE_ADD, 0, sizeof(p))
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
                    peer.Encode(p, sizeof(p))

                    p = TPacketMarriageUpdate()
                    p.dwPID1 = pMarriage.pid1
                    p.dwPID2 = pMarriage.pid2
                    p.iLovePoint = pMarriage.love_point
                    p.byMarried = pMarriage.is_married
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
                    peer.EncodeHeader(LG_HEADER_DG_MARRIAGE_UPDATE, 0, sizeof(p))
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
                    peer.Encode(p, sizeof(p))
                it += 1

            it = m_mapRunningWedding.begin()
            while it is not m_mapRunningWedding.end():
                t = it.second

                p = TPacketWeddingReady()
                p.dwPID1 = t.dwPID1
                p.dwPID2 = t.dwPID2
                p.dwMapIndex = t.dwMapIndex

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
                peer.EncodeHeader(LG_HEADER_DG_WEDDING_READY, 0, sizeof(p))
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
                peer.Encode(p, sizeof(p))

                p2 = TPacketWeddingStart()
                p2.dwPID1 = t.dwPID1
                p2.dwPID2 = t.dwPID2

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
                peer.EncodeHeader(LG_HEADER_DG_WEDDING_START, 0, sizeof(p2))
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
                peer.Encode(p2, sizeof(p2))
                it += 1

        def Update(self):
            now = CClientManager.instance().GetCurrentTime()

            if not m_pqWeddingEnd.empty():
                while (not m_pqWeddingEnd.empty()) and m_pqWeddingEnd.top().dwTime <= now:
                    wi = m_pqWeddingEnd.top()
                    m_pqWeddingEnd.pop()

                    it = m_mapRunningWedding.find((wi.dwPID1, wi.dwPID2))
                    if it == m_mapRunningWedding.end():
                        continue

                    w = it.second

                    p = TPacketWeddingEnd()
                    p.dwPID1 = w.dwPID1
                    p.dwPID2 = w.dwPID2
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
                    CClientManager.instance().ForwardPacket(LG_HEADER_DG_WEDDING_END, p, sizeof(p))
                    m_mapRunningWedding.erase(it)

                    it_marriage = m_MarriageByPID.find(w.dwPID1)

                    if it_marriage != m_MarriageByPID.end():
                        pMarriage = it_marriage.second
                        if not pMarriage.is_married:
                            Remove(pMarriage.pid1, pMarriage.pid2)
            if not m_pqWeddingStart.empty():
                while (not m_pqWeddingStart.empty()) and m_pqWeddingStart.top().dwTime <= now:
                    w = m_pqWeddingStart.top()
                    m_pqWeddingStart.pop()

                    p = TPacketWeddingStart()
                    p.dwPID1 = w.dwPID1
                    p.dwPID2 = w.dwPID2
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
                    CClientManager.instance().ForwardPacket(LG_HEADER_DG_WEDDING_START, p, sizeof(p))

                    w.dwTime += WEDDING_LENGTH
                    m_pqWeddingEnd.push(TWeddingInfo(w.dwTime, w.dwPID1, w.dwPID2))
                    m_mapRunningWedding.insert(((w.dwPID1, w.dwPID2), w))



class marriage: #this class replaces the original namespace 'marriage'
    WEDDING_LENGTH = 60 * 60


    @staticmethod
    def Align(rPID1, rPID2):
        if rPID1.arg_value > rPID2.arg_value:
            std::swap(rPID1.arg_value, rPID2.arg_value)
