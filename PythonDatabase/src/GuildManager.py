import math

class TGuildDeclareInfo:

    def __init__(self, _bType, _dwGuildID1, _dwGuildID2):
        self.bType = _bType
        dwGuildID[0] = _dwGuildID1
        dwGuildID[1] = _dwGuildID2

#Laniatus Games Studio Inc. | Python Metin II Server Warnings 'const' methods are not available in Python:
#ORIGINAL LINE: bool operator < (const TGuildDeclareInfo& r) const
    def less_than(self, r):
        return dwGuildID[0] < r.dwGuildID[0] or dwGuildID[0] == r.dwGuildID[0] and dwGuildID[1] < r.dwGuildID[1]

#Laniatus Games Studio Inc. | Python Metin II Server Note This 'copy_from' method was converted from the original copy assignment operator:
#ORIGINAL LINE: TGuildDeclareInfo& operator = (const TGuildDeclareInfo& r)
    def copy_from(self, r):
        bType = r.bType
        dwGuildID[0] = r.dwGuildID[0]
        dwGuildID[1] = r.dwGuildID[1]
        return self

class TGuildWaitStartInfo:

    def __init__(self, _bType, _g1, _g2, _lWarPrice, _lInitialScore, _pkReserve):
        self.bType = _bType
        self.lWarPrice = _lWarPrice
        self.lInitialScore = _lInitialScore
        self.pkReserve = _pkReserve
        GID[0] = _g1
        GID[1] = _g2

#Laniatus Games Studio Inc. | Python Metin II Server Warnings 'const' methods are not available in Python:
#ORIGINAL LINE: bool operator < (const TGuildWaitStartInfo& r) const
    def less_than(self, r):
        return GID[0] < r.GID[0] or GID[0] == r.GID[0] and GID[1] < r.GID[1]

class TGuildWarPQElement:

    def __init__(self, _bType, GID1, GID2):
        self.bEnd = DefineConstants.false
        self.bType = _bType
        bType = _bType
        GID[0] = GID1
        GID[1] = GID2
        iScore[0] = iScore[1] = 0
        iBetScore[0] = iBetScore[1] = 0

class TGuildSkillUsed:

    def __init__(self, _GID, _dwSkillVnum):
        self.GID = _GID
        self.dwSkillVnum = _dwSkillVnum

class SGuild:
    def __init__(self):
        self.ladder_point = 0
        self.win = 0
        self.draw = 0
        self.loss = 0
        self.gold = 0
        self.level = 0
# Laniatus Games Studio Inc. |  TODO TASK: The memory management function 'memset' has no equivalent in Python:
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        memset(szName, 0, sizeof(szName))


class SGuildWarInfo:

    def __init__(self):
        self.pElement = None

class CGuildWarReserve:
    def __init__(self, rTable):
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        thecore_memcpy(m_data, rTable, sizeof(TGuildWarReserve))
        m_iLastNoticeMin = -1

        Initialize()

    def Initialize(self):
        szQuery = str(['\0' for _ in range(256)])
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        snprintf(szQuery, sizeof(szQuery), "SELECT login, guild, gold FROM guild_war_bet WHERE war_id=%u", m_data.dwID)

        msgbet = std::unique_ptr(CDBManager.instance().DirectQuery(szQuery))

        if msgbet.Get().uiNumRows:
            res = msgbet.Get().pSQLResult
            row = MYSQL_ROW()

            szLogin = str(['\0' for _ in range(LOGIN_MAX_LEN+1)])
            dwGuild = None
            lldGold = None

# Laniatus Games Studio Inc. |  TODO TASK: The following assignments within expression was not converted by Laniatus Games Studio Inc. T.F |:
#ORIGINAL LINE: while ((row = mysql_fetch_row(res)))
            while (row = mysql_fetch_row(res)):
                dwGuild = uint(lldGold) = 0
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
                strlcpy(szLogin, row[0], sizeof(szLogin))
                str_to_number(dwGuild, row[1])
                str_to_number(lldGold, row[2])

                mapBet.insert((szLogin, (dwGuild, lldGold)))

    def GetDataRef(self):
        return m_data

    def OnSetup(self, peer):
        if m_data.bStarted:
            return

        FSendPeerWar(m_data.bType, GUILD_WAR_RESERVE, m_data.dwGuildFrom, m_data.dwGuildTo)(peer)

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        peer.EncodeHeader(LG_HEADER_DG_GUILD_WAR_RESERVE_ADD, 0, sizeof(TGuildWarReserve))
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        peer.Encode(m_data, sizeof(TGuildWarReserve))

        pckBet = TPacketGDGuildWarBet()
        pckBet.dwWarID = m_data.dwID

        it = mapBet.begin()

        while it is not mapBet.end():
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
            strlcpy(pckBet.szLogin, it.first.c_str(), sizeof(pckBet.szLogin))
            pckBet.dwGuild = it.second.first
            pckBet.lldGold = it.second.second

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
            peer.EncodeHeader(LG_HEADER_DG_GUILD_WAR_BET, 0, sizeof(TPacketGDGuildWarBet))
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
            peer.Encode(pckBet, sizeof(TPacketGDGuildWarBet))

            it += 1

    def Bet(self, pszLogin, lldGold, dwGuild):
        szQuery = str(['\0' for _ in range(1024)])

        if m_data.dwGuildFrom != dwGuild and m_data.dwGuildTo != dwGuild:
            sys_log(0, "GuildWarReserve::Bet: invalid guild id")
            return DefineConstants.false

        if m_data.bStarted:
            sys_log(0, "GuildWarReserve::Bet: war is already started")
            return DefineConstants.false

        if mapBet.find(pszLogin) != mapBet.end():
            sys_log(0, "GuildWarReserve::Bet: failed. already bet")
            return DefineConstants.false

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        snprintf(szQuery, sizeof(szQuery), "INSERT INTO guild_war_bet (war_id, login, gold, guild) VALUES(%u, '%s', %lld, %u)", m_data.dwID, pszLogin, lldGold, dwGuild)

        pmsg = std::unique_ptr(CDBManager.instance().DirectQuery(szQuery))

        if pmsg.Get().uiAffectedRows == 0 or pmsg.Get().uiAffectedRows == -1:
            sys_log(0, "GuildWarReserve::Bet: failed. cannot insert row to guild_war_bet table")
            return DefineConstants.false

        if m_data.dwGuildFrom == dwGuild:
            m_data.dwBetFrom += lldGold
        else:
            m_data.dwBetTo += lldGold

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        CClientManager.instance().ForwardPacket(LG_HEADER_DG_GUILD_WAR_RESERVE_ADD, m_data, sizeof(TGuildWarReserve))

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        snprintf(szQuery, sizeof(szQuery), "UPDATE guild_war_reservation SET bet_from=%lld,bet_to=%lld WHERE id=%u", m_data.dwBetFrom, m_data.dwBetTo, m_data.dwID)

        CDBManager.instance().AsyncQuery(szQuery)

        sys_log(0, "GuildWarReserve::Bet: success. %s %u war_id %u bet %lld : %lld", pszLogin, dwGuild, m_data.dwID, m_data.dwBetFrom, m_data.dwBetTo)
        mapBet.insert((pszLogin, (dwGuild, lldGold)))

        pckBet = TPacketGDGuildWarBet()
        pckBet.dwWarID = m_data.dwID
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        strlcpy(pckBet.szLogin, pszLogin, sizeof(pckBet.szLogin))
        pckBet.dwGuild = dwGuild
        pckBet.lldGold = lldGold

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        CClientManager.instance().ForwardPacket(LG_HEADER_DG_GUILD_WAR_BET, pckBet, sizeof(TPacketGDGuildWarBet))
        return ((not DefineConstants.false))

    def Draw(self):
        szQuery = str(['\0' for _ in range(1024)])

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        snprintf(szQuery, sizeof(szQuery), "UPDATE guild_war_reservation SET started=1,winner=0 WHERE id=%u", m_data.dwID)
        CDBManager.instance().AsyncQuery(szQuery)

        if mapBet.empty():
            return

        sys_log(0, "WAR_REWARD: Draw. war_id %u", m_data.dwID)

        it = mapBet.begin()

        while True:
            iLen = 0
            iRow = 0

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
            iLen += snprintf(szQuery, sizeof(szQuery) - iLen, "INSERT INTO item_award (login, vnum, socket0, given_time) VALUES")

            while it is not mapBet.end():
                if iRow == 0:
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
                    iLen += snprintf(szQuery[iLen:], sizeof(szQuery) - iLen, "('%s', %d, %u, NOW())", it.first.c_str(), ITEM_ELK_VNUM, it.second.second)
                else:
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
                    iLen += snprintf(szQuery[iLen:], sizeof(szQuery) - iLen, ",('%s', %d, %u, NOW())", it.first.c_str(), ITEM_ELK_VNUM, it.second.second)

                it += 1

                if iLen > 384:
                    break

                iRow += 1

            if iRow > 0:
                sys_log(0, "WAR_REWARD: QUERY: %s", szQuery)
                CDBManager.instance().AsyncQuery(szQuery)

            if it is mapBet.end():
                break

    def End(self, iScoreFrom, iScoreTo):
        dwWinner = None

        sys_log(0, "WAR_REWARD: End: From %u %d To %u %d", m_data.dwGuildFrom, iScoreFrom, m_data.dwGuildTo, iScoreTo)

        if m_data.lPowerFrom > m_data.lPowerTo:
            if m_data.lHandicap > iScoreFrom - iScoreTo:
                sys_log(0, "WAR_REWARD: End: failed to overcome handicap, From is strong but To won")
                dwWinner = m_data.dwGuildTo
            else:
                sys_log(0, "WAR_REWARD: End: success to overcome handicap, From win!")
                dwWinner = m_data.dwGuildFrom
        else:
            if m_data.lHandicap > iScoreTo - iScoreFrom:
                sys_log(0, "WAR_REWARD: End: failed to overcome handicap, To is strong but From won")
                dwWinner = m_data.dwGuildFrom
            else:
                sys_log(0, "WAR_REWARD: End: success to overcome handicap, To win!")
                dwWinner = m_data.dwGuildTo

        szQuery = str(['\0' for _ in range(1024)])
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        snprintf(szQuery, sizeof(szQuery), "UPDATE guild_war_reservation SET started=1,winner=%u,result1=%d,result2=%d WHERE id=%u", dwWinner, iScoreFrom, iScoreTo, m_data.dwID)
        CDBManager.instance().AsyncQuery(szQuery)

        if mapBet.empty():
            return

        dwTotalBet = m_data.dwBetFrom + m_data.dwBetTo
        dwWinnerBet = 0

        if dwWinner == m_data.dwGuildFrom:
            dwWinnerBet = m_data.dwBetFrom
        elif dwWinner == m_data.dwGuildTo:
            dwWinnerBet = m_data.dwBetTo
        else:
            sys_err("WAR_REWARD: fatal error, winner does not exist!")
            return

        if dwWinnerBet == 0:
            sys_err("WAR_REWARD: total bet money on winner is zero")
            return

        sys_log(0, "WAR_REWARD: End: Total bet: %u, Winner bet: %u", dwTotalBet, dwWinnerBet)

        it = mapBet.begin()

        while True:
            iLen = 0
            iRow = 0

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
            iLen += snprintf(szQuery, sizeof(szQuery) - iLen, "INSERT INTO item_award (login, vnum, socket0, given_time) VALUES")

            while it is not mapBet.end():
                if it.second.first != dwWinner:
                    it += 1
                    continue

                ratio = float(it.second.second) / dwWinnerBet

                sys_log(0, "WAR_REWARD: %s %u ratio %f", it.first.c_str(), it.second.second, ratio)

                lldGold = int((dwTotalBet * ratio * 0.9))

                if iRow == 0:
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
                    iLen += snprintf(szQuery[iLen:], sizeof(szQuery) - iLen, "('%s', %d, %lld, NOW())", it.first.c_str(), ITEM_ELK_VNUM, lldGold)
                else:
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
                    iLen += snprintf(szQuery[iLen:], sizeof(szQuery) - iLen, ",('%s', %d, %lld, NOW())", it.first.c_str(), ITEM_ELK_VNUM, lldGold)

                it += 1

                if iLen > 384:
                    break

                iRow += 1

            if iRow > 0:
                sys_log(0, "WAR_REWARD: query: %s", szQuery)
                CDBManager.instance().AsyncQuery(szQuery)

            if it is mapBet.end():
                break

    def GetLastNoticeMin(self):
        return m_iLastNoticeMin
    def SetLastNoticeMin(self, iMin):
        m_iLastNoticeMin = iMin

//Laniatus Games Studio Inc. T.F | TODO TASK: The implementation of the following method could not be found:
//    CGuildWarReserve()


class CGuildManager(singleton):
    def __init__(self):
        pass

    def close(self):
        while not m_pqOnWar.empty():
            if not m_pqOnWar.top().second.bEnd:
                if m_pqOnWar.top().second is not None:
                    m_pqOnWar.top().second.close()

            m_pqOnWar.pop()

    def Initialize(self):
        szQuery = str(['\0' for _ in range(1024)])
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        snprintf(szQuery, sizeof(szQuery), "SELECT id, name, ladder_point, win, draw, loss, gold, level FROM guild%s", GetTablePostfix())
        pmsg = std::unique_ptr(CDBManager.instance().DirectQuery(szQuery))

        if pmsg.Get().uiNumRows:
            ParseResult(pmsg.Get())

        str = str(['\0' for _ in range(128 + 1)])

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        if not CConfig.instance().GetValue("POLY_POWER", str, sizeof(str)):
            str[0] = '\0'

        if not polyPower.Analyze(str):
            sys_err("cannot set power poly: %s", str)
        else:
            sys_log(0, "POWER_POLY: %s", str)

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        if not CConfig.instance().GetValue("POLY_HANDICAP", str, sizeof(str)):
            str[0] = '\0'

        if not polyHandicap.Analyze(str):
            sys_err("cannot set handicap poly: %s", str)
        else:
            sys_log(0, "HANDICAP_POLY: %s", str)

        QueryRanking()

    def Load(self, dwGuildID):
        szQuery = str(['\0' for _ in range(1024)])

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        snprintf(szQuery, sizeof(szQuery), "SELECT id, name, ladder_point, win, draw, loss, gold, level FROM guild%s WHERE id=%u", GetTablePostfix(), dwGuildID)
        pmsg = std::unique_ptr(CDBManager.instance().DirectQuery(szQuery))

        if pmsg.Get().uiNumRows:
            ParseResult(pmsg.Get())

    def TouchGuild(self, GID):
        it = m_map_kGuild.find(GID)

        if it != m_map_kGuild.end():
            return it.second

        info = SGuild()
        m_map_kGuild.insert(dict.value_type(GID, info))
        return m_map_kGuild[GID]

    def Update(self):
        ProcessReserveWar()

        now = CClientManager.instance().GetCurrentTime()

        if not m_pqOnWar.empty():
            while (not m_pqOnWar.empty()) and (m_pqOnWar.top().first <= now or (m_pqOnWar.top().second and m_pqOnWar.top().second.bEnd)):
                e = m_pqOnWar.top().second

                m_pqOnWar.pop()

                if e:
                    if not e.bEnd:
                        WarEnd(e.GID[0], e.GID[1], DefineConstants.false)

                    e = None

        while (not m_pqSkill.empty()) and m_pqSkill.top().first <= now:
            s = m_pqSkill.top().second
            CClientManager.instance().SendGuildSkillUsable(s.GID, s.dwSkillVnum, ((not DefineConstants.false)))
            m_pqSkill.pop()

        while (not m_pqWaitStart.empty()) and m_pqWaitStart.top().first <= now:
            ws = m_pqWaitStart.top().second
            m_pqWaitStart.pop()

            StartWar(ws.bType, ws.GID[0], ws.GID[1], ws.pkReserve)

            if ws.lInitialScore:
                UpdateScore(ws.GID[0], ws.GID[1], ws.lInitialScore, 0)
                UpdateScore(ws.GID[1], ws.GID[0], ws.lInitialScore, 0)

            p = TPacketGuildWar()

            p.bType = ws.bType
            p.bWar = GUILD_WAR_ON_WAR
            p.dwGuildFrom = ws.GID[0]
            p.dwGuildTo = ws.GID[1]

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
            CClientManager.instance().ForwardPacket(LG_HEADER_DG_GUILD_WAR, p, sizeof(p))
            sys_log(0, "GuildWar: GUILD sending start of wait start war %d %d", ws.GID[0], ws.GID[1])

    def OnSetup(self, peer):
        it_cont = (m_WarMap).begin()
        while it_cont is not (m_WarMap).end():
            it = (it_cont.second).begin()
            while it is not (it_cont.second).end():
                g1 = it_cont.first
                g2 = it.first
                p = it.second.pElement

                if p is None or p.bEnd:
                    continue

                FSendPeerWar(p.bType, GUILD_WAR_ON_WAR, g1, g2)(peer)
                FSendGuildWarScore(p.GID[0], p.GID[1], p.iScore[0], p.iBetScore[0])
                FSendGuildWarScore(p.GID[1], p.GID[0], p.iScore[1], p.iBetScore[1])
                it += 1
            it_cont += 1

        it = (m_DeclareMap).begin()
        while it is not (m_DeclareMap).end():
            FSendPeerWar(it.bType, GUILD_WAR_SEND_DECLARE, it.dwGuildID[0], it.dwGuildID[1])(peer)
            it += 1

        it = (m_map_kWarReserve).begin()
        while it is not (m_map_kWarReserve).end():
            it.second.OnSetup(peer)
            it += 1

    def StartWar(self, bType, GID1, GID2, pkReserve = None):
        sys_log(0, "GuildWar: StartWar(%d,%d,%d)", bType, GID1, GID2)

        if GID1 > GID2:
            std::swap(GID1, GID2)

        gw = m_WarMap[GID1][GID2]

        if bType == GUILD_WAR_TYPE_FIELD:
            gw.tEndTime = CClientManager.instance().GetCurrentTime() + GUILD_WAR_DURATION
        else:
            gw.tEndTime = CClientManager.instance().GetCurrentTime() + 172800

        gw.pElement = TGuildWarPQElement(bType, GID1, GID2)
        gw.pkReserve = pkReserve

        m_pqOnWar.push((gw.tEndTime, gw.pElement))

    def UpdateScore(self, dwGainGID, dwOppGID, iScoreDelta, iBetScoreDelta):
        GID1 = dwGainGID
        GID2 = dwOppGID

        if GID1 > GID2:
            std::swap(GID1, GID2)

        it = m_WarMap[GID1].find(GID2)

        if it != m_WarMap[GID1].end():
            p = it.second.pElement

            if p is None or p.bEnd:
                sys_err("GuildWar: war not exist or already ended.")
                return

            iNewScore = 0
            iNewBetScore = 0

            if p.GID[0] == dwGainGID:
                p.iScore[0] += iScoreDelta
                p.iBetScore[0] += iBetScoreDelta

                iNewScore = p.iScore[0]
                iNewBetScore = p.iBetScore[0]
            else:
                p.iScore[1] += iScoreDelta
                p.iBetScore[1] += iBetScoreDelta

                iNewScore = p.iScore[1]
                iNewBetScore = p.iBetScore[1]

            sys_log(0, "GuildWar: SendGuildWarScore guild %u wartype %u score_delta %d betscore_delta %d result %u, %u", dwGainGID, p.bType, iScoreDelta, iBetScoreDelta, iNewScore, iNewBetScore)

            CClientManager.instance().for_each_peer(FSendGuildWarScore(dwGainGID, dwOppGID, iNewScore, iNewBetScore))

    def AddDeclare(self, bType, guild_from, guild_to):
        di = TGuildDeclareInfo(bType, guild_from, guild_to)

        if m_DeclareMap.find(di) == m_DeclareMap.end():
            m_DeclareMap.insert(di)

        sys_log(0, "GuildWar: AddDeclare(Type:%d,from:%d,to:%d)", bType, guild_from, guild_to)

    def RemoveDeclare(self, guild_from, guild_to):
        it = m_DeclareMap.find(TGuildDeclareInfo(0, guild_from, guild_to))

        if it != m_DeclareMap.end():
            m_DeclareMap.erase(it)

        it = m_DeclareMap.find(TGuildDeclareInfo(0,guild_to, guild_from))

        if it != m_DeclareMap.end():
            m_DeclareMap.erase(it)

        sys_log(0, "GuildWar: RemoveDeclare(from:%d,to:%d)", guild_from, guild_to)

    def TakeBetPrice(self, dwGuildTo, dwGuildFrom, lWarPrice):
        it_from = m_map_kGuild.find(dwGuildFrom)
        it_to = m_map_kGuild.find(dwGuildTo)

        if it_from == m_map_kGuild.end() or it_to == m_map_kGuild.end():
            sys_log(0, "TakeBetPrice: guild not exist %u %u", dwGuildFrom, dwGuildTo)
            return DefineConstants.false

        if it_from.second.gold < lWarPrice or it_to.second.gold < lWarPrice:
            sys_log(0, "TakeBetPrice: not enough gold %u %lld to %u %lld", dwGuildFrom, it_from.second.gold, dwGuildTo, it_to.second.gold)
            return DefineConstants.false

        it_from.second.gold -= lWarPrice
        it_to.second.gold -= lWarPrice

        MoneyChange(dwGuildFrom, it_from.second.gold)
        MoneyChange(dwGuildTo, it_to.second.gold)
        return ((not DefineConstants.false))

    def WaitStart(self, p):
        if p.lWarPrice > 0:
            if not TakeBetPrice(p.dwGuildFrom, p.dwGuildTo, p.lWarPrice):
                return DefineConstants.false

        dwCurTime = CClientManager.instance().GetCurrentTime()

        info = TGuildWaitStartInfo(p.bType, p.dwGuildFrom, p.dwGuildTo, p.lWarPrice, p.lInitialScore, None)
        m_pqWaitStart.push((dwCurTime + GetGuildWarWaitStartDuration(), info))

        sys_log(0, "GuildWar: WaitStart g1 %d g2 %d price %lld start at %u", p.dwGuildFrom, p.dwGuildTo, p.lWarPrice, dwCurTime + GetGuildWarWaitStartDuration())

        return ((not DefineConstants.false))

    def RecvWarEnd(self, GID1, GID2):
        sys_log(0, "GuildWar: RecvWarEnded : %u vs %u", GID1, GID2)
        WarEnd(GID1, GID2, ((not DefineConstants.false)))

    def RecvWarOver(self, dwGuildWinner, dwGuildLoser, bDraw, lWarPrice):
        sys_log(0, "GuildWar: RecvWarOver : winner %u vs %u draw? %d war_price %lld", dwGuildWinner, dwGuildLoser,1 if bDraw else 0, lWarPrice)

        GID1 = dwGuildWinner
        GID2 = dwGuildLoser

        if GID1 > GID2:
            std::swap(GID1, GID2)

        it = m_WarMap[GID1].find(GID2)

        if it == m_WarMap[GID1].end():
            return

        gw = it.second

        if bDraw:
            DepositMoney(dwGuildWinner, math.trunc(lWarPrice / float(2)))
            DepositMoney(dwGuildLoser, math.trunc(lWarPrice / float(2)))
            ProcessDraw(dwGuildWinner, dwGuildLoser)
        else:
            DepositMoney(dwGuildWinner, lWarPrice)
            ProcessWinLose(dwGuildWinner, dwGuildLoser)

        if gw.pkReserve:
            if bDraw or not gw.pElement:
                gw.pkReserve.Draw()
            elif gw.pElement.bType == GUILD_WAR_TYPE_BATTLE:
                gw.pkReserve.End(gw.pElement.iBetScore[0], gw.pElement.iBetScore[1])

        RemoveWar(GID1, GID2)

    def ChangeLadderPoint(self, GID, change):
        it = m_map_kGuild.find(GID)

        if it == m_map_kGuild.end():
            return

        r = it.second

        r.ladder_point += change

        if r.ladder_point < 0:
            r.ladder_point = 0

        buf = str(['\0' for _ in range(1024)])
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        snprintf(buf, sizeof(buf), "UPDATE guild%s SET ladder_point=%d WHERE id=%u", GetTablePostfix(), r.ladder_point, GID)
        CDBManager.instance().AsyncQuery(buf)

        sys_log(0, "GuildManager::ChangeLadderPoint %u %d", GID, r.ladder_point)
        sys_log(0, "%s", buf)

        p = TPacketGuildLadder()

        p.dwGuild = GID
        p.lLadderPoint = r.ladder_point
        p.lWin = r.win
        p.lDraw = r.draw
        p.lLoss = r.loss

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        CClientManager.instance().ForwardPacket(LG_HEADER_DG_GUILD_LADDER, p, sizeof(TPacketGuildLadder))

    def UseSkill(self, GID, dwSkillVnum, dwCooltime):
        sys_log(0, "UseSkill(gid=%d, skill=%d) CoolTime(%d:%d)", GID, dwSkillVnum, dwCooltime, CClientManager.instance().GetCurrentTime() + dwCooltime)
        m_pqSkill.push((CClientManager.instance().GetCurrentTime() + dwCooltime, TGuildSkillUsed(GID, dwSkillVnum)))

    def DepositMoney(self, dwGuild, iGold):
        if iGold <= 0:
            return

        it = m_map_kGuild.find(dwGuild)

        if it == m_map_kGuild.end():
            sys_err("No guild by id %u", dwGuild)
            return

        it.second.gold += iGold
        sys_log(0, "GUILD: %u Deposit %lld Total %lld", dwGuild, iGold, it.second.gold)

        MoneyChange(dwGuild, it.second.gold)

    def WithdrawMoney(self, peer, dwGuild, iGold):
        it = m_map_kGuild.find(dwGuild)

        if it == m_map_kGuild.end():
            sys_err("No guild by id %u", dwGuild)
            return

        if it.second.gold >= iGold:
            it.second.gold -= iGold
            sys_log(0, "GUILD: %u Withdraw %lld Total %lld", dwGuild, iGold, it.second.gold)

            p = TPacketDGGuildMoneyWithdraw()
            p.dwGuild = dwGuild
            p.iChangeGold = iGold

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
            peer.EncodeHeader(LG_HEADER_DG_GUILD_WITHDRAW_MONEY_GIVE, 0, sizeof(TPacketDGGuildMoneyWithdraw))
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
            peer.Encode(p, sizeof(TPacketDGGuildMoneyWithdraw))

    def WithdrawMoneyReply(self, dwGuild, bGiveSuccess, iGold):
        it = m_map_kGuild.find(dwGuild)

        if it == m_map_kGuild.end():
            return

        sys_log(0, "GuildManager::WithdrawMoneyReply : guild %u success %d gold %lld", dwGuild, bGiveSuccess, iGold)

        if bGiveSuccess == 0:
            it.second.gold += iGold
        else:
            MoneyChange(dwGuild, it.second.gold)

    def MoneyChange(self, dwGuild, lldGold):
        sys_log(0, "GuildManager::MoneyChange %d %lld", dwGuild, lldGold)

        p = TPacketDGGuildMoneyChange()
        p.dwGuild = dwGuild
        p.iTotalGold = lldGold
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        CClientManager.instance().ForwardPacket(LG_HEADER_DG_GUILD_MONEY_CHANGE, p, sizeof(p))

        buf = str(['\0' for _ in range(1024)])
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        snprintf(buf, sizeof(buf), "UPDATE guild%s SET gold=%lld WHERE id = %u", GetTablePostfix(), lldGold, dwGuild)
        CDBManager.instance().AsyncQuery(buf)

    def QueryRanking(self):
        szQuery = str(['\0' for _ in range(256)])
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        snprintf(szQuery, sizeof(szQuery), "SELECT id,name,ladder_point FROM guild%s ORDER BY ladder_point DESC LIMIT 20", GetTablePostfix())

        CDBManager.instance().ReturnQuery(szQuery, QID_GUILD_RANKING, 0, 0)

    def ResultRanking(self, pRes):
        if pRes is None:
            return

        iLastLadderPoint = -1
        iRank = 0

        map_kLadderPointRankingByGID.clear()

        row = MYSQL_ROW()

# Laniatus Games Studio Inc. |  TODO TASK: The following assignments within expression was not converted by Laniatus Games Studio Inc. T.F |:
#ORIGINAL LINE: while ((row = mysql_fetch_row(pRes)))
        while (row = mysql_fetch_row(pRes)):
            dwGID = 0
            str_to_number(dwGID, row[0])
            iLadderPoint = 0
            str_to_number(iLadderPoint, row[2])

            if iLadderPoint != iLastLadderPoint:
                iRank += 1

            sys_log(0, "GUILD_RANK: %-24s %2d %d", row[1], iRank, iLadderPoint)

            map_kLadderPointRankingByGID.insert((dwGID, iRank))

    def GetRanking(self, dwGID):
        it = map_kLadderPointRankingByGID.find(dwGID)

        if it == map_kLadderPointRankingByGID.end():
            return GUILD_RANK_MAX_NUM

        return MINMAX(0, it.second, GUILD_RANK_MAX_NUM)

    def BootReserveWar(self):
        c_apszQuery = ["SELECT id, guild1, guild2, UNIX_TIMESTAMP(time), type, warprice, initscore, bet_from, bet_to, power1, power2, handicap FROM guild_war_reservation WHERE started=1 AND winner=-1", "SELECT id, guild1, guild2, UNIX_TIMESTAMP(time), type, warprice, initscore, bet_from, bet_to, power1, power2, handicap FROM guild_war_reservation WHERE started=0"]

        for i in range(0, 2):
            pmsg = std::unique_ptr(CDBManager.instance().DirectQuery(c_apszQuery[i]))

            if pmsg.Get().uiNumRows == 0:
                continue

            row = MYSQL_ROW()

# Laniatus Games Studio Inc. |  TODO TASK: The following assignments within expression was not converted by Laniatus Games Studio Inc. T.F |:
#ORIGINAL LINE: while ((row = mysql_fetch_row(pmsg->Get()->pSQLResult)))
            while (row = mysql_fetch_row(pmsg.Get().pSQLResult)):
                col = 0

                t = TGuildWarReserve()

#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(t.dwID, row[col++]);
                str_to_number(t.dwID, row[col])
                col += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(t.dwGuildFrom, row[col++]);
                str_to_number(t.dwGuildFrom, row[col])
                col += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(t.dwGuildTo, row[col++]);
                str_to_number(t.dwGuildTo, row[col])
                col += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(t.dwTime, row[col++]);
                str_to_number(t.dwTime, row[col])
                col += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(t.bType, row[col++]);
                str_to_number(t.bType, row[col])
                col += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(t.lWarPrice, row[col++]);
                str_to_number(t.lWarPrice, row[col])
                col += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(t.lInitialScore, row[col++]);
                str_to_number(t.lInitialScore, row[col])
                col += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(t.dwBetFrom, row[col++]);
                str_to_number(t.dwBetFrom, row[col])
                col += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(t.dwBetTo, row[col++]);
                str_to_number(t.dwBetTo, row[col])
                col += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(t.lPowerFrom, row[col++]);
                str_to_number(t.lPowerFrom, row[col])
                col += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(t.lPowerTo, row[col++]);
                str_to_number(t.lPowerTo, row[col])
                col += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(t.lHandicap, row[col++]);
                str_to_number(t.lHandicap, row[col])
                col += 1
                t.bStarted = 0

                pkReserve = CGuildWarReserve(t)

                buf = str(['\0' for _ in range(512)])
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
                snprintf(buf, sizeof(buf), "GuildWar: BootReserveWar : step %d id %u GID1 %u GID2 %u", i, t.dwID, t.dwGuildFrom, t.dwGuildTo)

                if i == 0 or int(t.dwTime) - CClientManager.instance().GetCurrentTime() < 0:
                    if i == 0:
                        sys_log(0, "%s : DB was shutdowned while war is being.", buf)
                    else:
                        sys_log(0, "%s : left time lower than 5 minutes, will be canceled", buf)

                    pkReserve.Draw()
                    pkReserve = None
                else:
                    sys_log(0, "%s : OK", buf)
                    m_map_kWarReserve.insert((t.dwID, pkReserve))

    def ReserveWar(self, p):
        GID1 = p.dwGuildFrom
        GID2 = p.dwGuildTo

        if GID1 > GID2:
            std::swap(GID1, GID2)

        if p.lWarPrice > 0:
            if not TakeBetPrice(GID1, GID2, p.lWarPrice):
                return DefineConstants.false

        t = TGuildWarReserve()
# Laniatus Games Studio Inc. |  TODO TASK: The memory management function 'memset' has no equivalent in Python:
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        memset(t, 0, sizeof(TGuildWarReserve))

        t.dwGuildFrom = GID1
        t.dwGuildTo = GID2
        t.dwTime = CClientManager.instance().GetCurrentTime() + GetGuildWarReserveSeconds()
        t.bType = p.bType
        t.lWarPrice = p.lWarPrice
        t.lInitialScore = p.lInitialScore

        lvp = None
        rkp = None
        alv = None
        mc = None

        k1 = TouchGuild(GID1)

        lvp = c_aiScoreByLevel[MIN(GUILD_MAX_LEVEL, k1.level)]
        rkp = c_aiScoreByRanking[GetRanking(GID1)]
        alv = GetAverageGuildMemberLevel(GID1)
        mc = GetGuildMemberCount(GID1)

        polyPower.SetVar("lvp", lvp)
        polyPower.SetVar("rkp", rkp)
        polyPower.SetVar("alv", alv)
        polyPower.SetVar("mc", mc)

        t.lPowerFrom = int(polyPower.Eval())
        sys_log(0, "GuildWar: %u lvp %d rkp %d alv %d mc %d power %d", GID1, lvp, rkp, alv, mc, t.lPowerFrom)

        k2 = TouchGuild(GID2)

        lvp = c_aiScoreByLevel[MIN(GUILD_MAX_LEVEL, k2.level)]
        rkp = c_aiScoreByRanking[GetRanking(GID2)]
        alv = GetAverageGuildMemberLevel(GID2)
        mc = GetGuildMemberCount(GID2)

        polyPower.SetVar("lvp", lvp)
        polyPower.SetVar("rkp", rkp)
        polyPower.SetVar("alv", alv)
        polyPower.SetVar("mc", mc)

        t.lPowerTo = int(polyPower.Eval())
        sys_log(0, "GuildWar: %u lvp %d rkp %d alv %d mc %d power %d", GID2, lvp, rkp, alv, mc, t.lPowerTo)

        if t.lPowerTo > t.lPowerFrom:
            polyHandicap.SetVar("pA", t.lPowerTo)
            polyHandicap.SetVar("pB", t.lPowerFrom)
        else:
            polyHandicap.SetVar("pA", t.lPowerFrom)
            polyHandicap.SetVar("pB", t.lPowerTo)

        t.lHandicap = int(polyHandicap.Eval())
        sys_log(0, "GuildWar: handicap %d", t.lHandicap)

        szQuery = str(['\0' for _ in range(512)])

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        snprintf(szQuery, sizeof(szQuery), "INSERT INTO guild_war_reservation (guild1, guild2, time, type, warprice, initscore, power1, power2, handicap) " + "VALUES(%u, %u, DATE_ADD(NOW(), INTERVAL 180 SECOND), %u, %lld, %ld, %ld, %ld, %ld)", GID1, GID2, p.bType, p.lWarPrice, p.lInitialScore, t.lPowerFrom, t.lPowerTo, t.lHandicap)

        pmsg = std::unique_ptr(CDBManager.instance().DirectQuery(szQuery))

        if pmsg.Get().uiAffectedRows == 0 or pmsg.Get().uiInsertID == 0 or pmsg.Get().uiAffectedRows == -1:
            sys_err("GuildWar: Cannot insert row")
            return DefineConstants.false

        t.dwID = pmsg.Get().uiInsertID

        m_map_kWarReserve.insert((t.dwID, CGuildWarReserve(t)))

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        CClientManager.instance().ForwardPacket(LG_HEADER_DG_GUILD_WAR_RESERVE_ADD, t, sizeof(TGuildWarReserve))
        return ((not DefineConstants.false))

    def ProcessReserveWar(self):
        dwCurTime = CClientManager.instance().GetCurrentTime()

        it = m_map_kWarReserve.begin()

        while it is not m_map_kWarReserve.end():
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: auto it2 = it++;
            it2 = it
            it += 1

            pk = it2.second
            r = pk.GetDataRef()

            if (not r.bStarted) and r.dwTime - 1800 <= dwCurTime:
                iMin = int(math.ceil(int((r.dwTime - dwCurTime)) / 60.0))

                r_1 = m_map_kGuild[r.dwGuildFrom]
                r_2 = m_map_kGuild[r.dwGuildTo]

                sys_log(0, "GuildWar: started GID1 %u GID2 %u %d time %d min %d", r.dwGuildFrom, r.dwGuildTo, r.bStarted, dwCurTime - r.dwTime, iMin)

                if iMin <= 0:
                    szQuery = str(['\0' for _ in range(128)])
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
                    snprintf(szQuery, sizeof(szQuery), "UPDATE guild_war_reservation SET started=1 WHERE id=%u", r.dwID)
                    CDBManager.instance().AsyncQuery(szQuery)

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
                    CClientManager.instance().ForwardPacket(LG_HEADER_DG_GUILD_WAR_RESERVE_DEL, r.dwID, sizeof(uint))

                    r.bStarted = ((not DefineConstants.false))

                    info = TGuildWaitStartInfo(r.bType, r.dwGuildFrom, r.dwGuildTo, r.lWarPrice, r.lInitialScore, pk)
                    m_pqWaitStart.push((dwCurTime + GetGuildWarWaitStartDuration(), info))

                    pck = TPacketGuildWar()

                    pck.bType = r.bType
                    pck.bWar = GUILD_WAR_WAIT_START
                    pck.dwGuildFrom = r.dwGuildFrom
                    pck.dwGuildTo = r.dwGuildTo
                    pck.lWarPrice = r.lWarPrice
                    pck.lInitialScore = r.lInitialScore

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
                    CClientManager.instance().ForwardPacket(LG_HEADER_DG_GUILD_WAR, pck, sizeof(TPacketGuildWar))
                else:
                    if iMin != pk.GetLastNoticeMin():
                        pk.SetLastNoticeMin(iMin)

                        CClientManager.instance().SendNotice("The war between %s and %s will start after %d minutes!", r_1.szName, r_2.szName, iMin)

    def Bet(self, dwID, c_pszLogin, lldGold, dwGuild):
        it = m_map_kWarReserve.find(dwID)

        szQuery = str(['\0' for _ in range(1024)])

        if it == m_map_kWarReserve.end():
            sys_log(0, "WAR_RESERVE: Bet: cannot find reserve war by id %u", dwID)
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
            snprintf(szQuery, sizeof(szQuery), "INSERT INTO item_award (login, vnum, socket0, given_time) VALUES('%s', %d, %lld, NOW())", c_pszLogin, ITEM_ELK_VNUM, lldGold)
            CDBManager.instance().AsyncQuery(szQuery)
            return DefineConstants.false

        if not it.second.Bet(c_pszLogin, lldGold, dwGuild):
            sys_log(0, "WAR_RESERVE: Bet: cannot bet id %u, login %s, gold %lld, guild %u", dwID, c_pszLogin, lldGold, dwGuild)
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
            snprintf(szQuery, sizeof(szQuery), "INSERT INTO item_award (login, vnum, socket0, given_time) VALUES('%s', %d, %lld, NOW())", c_pszLogin, ITEM_ELK_VNUM, lldGold)
            CDBManager.instance().AsyncQuery(szQuery)
            return DefineConstants.false

        return ((not DefineConstants.false))

    def CancelWar(self, GID1, GID2):
        RemoveDeclare(GID1, GID2)
        RemoveWar(GID1, GID2)

    def ChangeMaster(self, dwGID, dwFrom, dwTo):
        iter = m_map_kGuild.find(dwGID)

        if iter == m_map_kGuild.end():
            return DefineConstants.false

        szQuery = str(['\0' for _ in range(1024)])

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        snprintf(szQuery, sizeof(szQuery), "UPDATE guild%s SET master=%u WHERE id=%u", GetTablePostfix(), dwTo, dwGID)
        CDBManager.instance().DirectQuery(szQuery) = None

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        snprintf(szQuery, sizeof(szQuery), "UPDATE guild_member%s SET grade=1 WHERE pid=%u", GetTablePostfix(), dwTo)
        CDBManager.instance().DirectQuery(szQuery) = None

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        snprintf(szQuery, sizeof(szQuery), "UPDATE guild_member%s SET grade=15 WHERE pid=%u", GetTablePostfix(), dwFrom)
        CDBManager.instance().DirectQuery(szQuery) = None

        return ((not DefineConstants.false))

//Laniatus Games Studio Inc. T.F | TODO TASK: The implementation of the following method could not be found:
//    ParseResult(pRes)
    def RemoveWar(self, GID1, GID2):
        sys_log(0, "GuildWar: RemoveWar(%d, %d)", GID1, GID2)

        if GID1 > GID2:
            std::swap(GID2, GID1)

        it = m_WarMap[GID1].find(GID2)

        if it == m_WarMap[GID1].end():
            if m_WarMap[GID1].empty():
                m_WarMap.erase(GID1)

            return

        if it.second.pElement:
            it.second.pElement.bEnd = ((not DefineConstants.false))

        m_mapGuildWarEndTime[GID1][GID2] = CClientManager.instance().GetCurrentTime()

        m_WarMap[GID1].erase(it)

        if m_WarMap[GID1].empty():
            m_WarMap.erase(GID1)

    def WarEnd(self, GID1, GID2, bForceDraw = DefineConstants.false):
        if GID1 > GID2:
            std::swap(GID2, GID1)

        sys_log(0, "GuildWar: WarEnd %d %d", GID1, GID2)

        itWarMap = m_WarMap[GID1].find(GID2)

        if itWarMap == m_WarMap[GID1].end():
            sys_err("GuildWar: war not exist or already ended. [1]")
            return

        gwi = itWarMap.second
        pData = gwi.pElement

        if pData is None or pData.bEnd:
            sys_err("GuildWar: war not exist or already ended. [2]")
            return

        win_guild = pData.GID[0]
        lose_guild = pData.GID[1]

        bDraw = DefineConstants.false

        if not bForceDraw:
            if pData.iScore[0] > pData.iScore[1]:
                win_guild = pData.GID[0]
                lose_guild = pData.GID[1]
            elif pData.iScore[1] > pData.iScore[0]:
                win_guild = pData.GID[1]
                lose_guild = pData.GID[0]
            else:
                bDraw = ((not DefineConstants.false))
        else:
            bDraw = ((not DefineConstants.false))

        if bDraw:
            ProcessDraw(win_guild, lose_guild)
        else:
            ProcessWinLose(win_guild, lose_guild)

        CClientManager.instance().for_each_peer(FSendPeerWar(0, GUILD_WAR_END, GID1, GID2))

        RemoveWar(GID1, GID2)

    def GetLadderPoint(self, GID):
        it = m_map_kGuild.find(GID)

        if it == m_map_kGuild.end():
            return 0

        return it.second.ladder_point

    def GuildWarWin(self, GID):
        it = m_map_kGuild.find(GID)

        if it == m_map_kGuild.end():
            return

        it.second.win += 1

        buf = str(['\0' for _ in range(1024)])
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        snprintf(buf, sizeof(buf), "UPDATE guild%s SET win=%d WHERE id=%u", GetTablePostfix(), it.second.win, GID)
        CDBManager.instance().AsyncQuery(buf)

    def GuildWarDraw(self, GID):
        it = m_map_kGuild.find(GID)

        if it == m_map_kGuild.end():
            return

        it.second.draw += 1

        buf = str(['\0' for _ in range(1024)])
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        snprintf(buf, sizeof(buf), "UPDATE guild%s SET draw=%d WHERE id=%u", GetTablePostfix(), it.second.draw, GID)
        CDBManager.instance().AsyncQuery(buf)

    def GuildWarLose(self, GID):
        it = m_map_kGuild.find(GID)

        if it == m_map_kGuild.end():
            return

        it.second.loss += 1

        buf = str(['\0' for _ in range(1024)])
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        snprintf(buf, sizeof(buf), "UPDATE guild%s SET loss=%d WHERE id=%u", GetTablePostfix(), it.second.loss, GID)
        CDBManager.instance().AsyncQuery(buf)

    def ProcessDraw(self, dwGuildID1, dwGuildID2):
        sys_log(0, "GuildWar: \tThe war between %d and %d is ended in draw", dwGuildID1, dwGuildID2)

        GuildWarDraw(dwGuildID1)
        GuildWarDraw(dwGuildID2)
        ChangeLadderPoint(dwGuildID1, 0)
        ChangeLadderPoint(dwGuildID2, 0)

        QueryRanking()

    def ProcessWinLose(self, dwGuildWinner, dwGuildLoser):
        GuildWarWin(dwGuildWinner)
        GuildWarLose(dwGuildLoser)
        sys_log(0, "GuildWar: \tWinner : %d Loser : %d", dwGuildWinner, dwGuildLoser)

        iPoint = GetLadderPoint(dwGuildLoser)
        gain = int((iPoint * 0.05))
        loss = int((iPoint * 0.07))

        if IsHalfWinLadderPoint(dwGuildWinner, dwGuildLoser) != 0:
            gain = math.trunc(gain / float(2))

        sys_log(0, "GuildWar: \tgain : %d loss : %d", gain, loss)

        ChangeLadderPoint(dwGuildWinner, gain)
        ChangeLadderPoint(dwGuildLoser, -loss)

        QueryRanking()

    def IsHalfWinLadderPoint(self, dwGuildWinner, dwGuildLoser):
        GID1 = dwGuildWinner
        GID2 = dwGuildLoser

        if GID1 > GID2:
            std::swap(GID1, GID2)

        it = m_mapGuildWarEndTime[GID1].find(GID2)

        if it != m_mapGuildWarEndTime[GID1].end() and it.second + GUILD_WAR_LADDER_HALF_PENALTY_TIME > CClientManager.instance().GetCurrentTime():
            return ((not DefineConstants.false))

        return DefineConstants.false







#Laniatus Games Studio Inc. | Python Metin II Server Note Anonymous namespaces are not converted:
#namespace
class FSendPeerWar:
    def __init__(self, bType, bWar, GID1, GID2):
        if number(0, 1):
            std::swap(GID1, GID2)

# Laniatus Games Studio Inc. |  TODO TASK: The memory management function 'memset' has no equivalent in Python:
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        memset(p, 0, sizeof(TPacketGuildWar))

        p.bWar = bWar
        p.bType = bType
        p.dwGuildFrom = GID1
        p.dwGuildTo = GID2

    def functor_method(self, peer):
        if peer.GetChannel() == 0:
            return

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        peer.EncodeHeader(LG_HEADER_DG_GUILD_WAR, 0, sizeof(TPacketGuildWar))
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        peer.Encode(p, sizeof(TPacketGuildWar))


class FSendGuildWarScore:
    def __init__(self, guild_gain, dwOppGID, iScore, iBetScore):
        pck.dwGuildGainPoint = guild_gain
        pck.dwGuildOpponent = dwOppGID
        pck.lScore = iScore
        pck.lBetScore = iBetScore

    def functor_method(self, peer):
        if peer.GetChannel() == 0:
            return

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        peer.EncodeHeader(LG_HEADER_DG_GUILD_WAR_SCORE, 0, sizeof(pck))
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        peer.Encode(pck, sizeof(pck))


def ParseResult(pRes):
    row = MYSQL_ROW()

# Laniatus Games Studio Inc. |  TODO TASK: The following assignments within expression was not converted by Laniatus Games Studio Inc. T.F |:
#ORIGINAL LINE: while ((row = mysql_fetch_row(pRes->pSQLResult)))
    while (row = mysql_fetch_row(pRes.pSQLResult)):
        GID = strtoul(row[0], None, 10)

        r_info = TouchGuild(GID)

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        strlcpy(r_info.szName, row[1], sizeof(r_info.szName))
        str_to_number(r_info.ladder_point, row[2])
        str_to_number(r_info.win, row[3])
        str_to_number(r_info.draw, row[4])
        str_to_number(r_info.loss, row[5])
        str_to_number(r_info.gold, row[6])
        str_to_number(r_info.level, row[7])

        sys_log(0, "GuildWar: %-24s ladder %-5d win %-3d draw %-3d loss %-3d", r_info.szName, r_info.ladder_point, r_info.win, r_info.draw, r_info.loss)