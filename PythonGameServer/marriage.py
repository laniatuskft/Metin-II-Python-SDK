import math

class marriage: #this class replaces the original namespace 'marriage'
    class TWeddingInfo:

        def __init__(self):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.dwMapIndex = 0


## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
#    extern const int MARRIAGE_LG_POINT_PER_DAY
    class TMarriage:


        def __init__(self, pid1, pid2, _love_point, _marry_time, name1, name2):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.m_pid1 = 0
            self.m_pid2 = 0
            self.love_point = 0
            self.marry_time = time_t()
            self.ch1 = None
            self.ch2 = None
            self.bSave = False
            self.is_married = False
            self.name1 = ""
            self.name2 = ""
            self.pWeddingInfo = None
            self.isLastNear = False
            self.byLastLovePoint = 0
            self.eventNearCheck = _boost_func_of_void.intrusive_ptr()

            self.m_pid1 = pid1
            self.m_pid2 = pid2
            self.love_point = _love_point
## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: this.marry_time = _marry_time;
            self.marry_time.copy_from(_marry_time)
            self.is_married = LGEMiscellaneous.DEFINECONSTANTS.false
            self.name1 = name1
            self.name2 = name2
            self.pWeddingInfo = None
            self.eventNearCheck = None
            self.ch1 = self.ch2 = None
            self.bSave = LGEMiscellaneous.DEFINECONSTANTS.false
            self.isLastNear = LGEMiscellaneous.DEFINECONSTANTS.false
            self.byLastLovePoint = 0

        def close(self):
            self.StopNearCheckEvent()
            if self.IsOnline():
                self.ch1.ChatPacket(EChatType.CHAT_TYPE_COMMAND, "lover_divorce")
                self.ch2.ChatPacket(EChatType.CHAT_TYPE_COMMAND, "lover_divorce")
            LG_DEL_MEM(self.pWeddingInfo)
            self.pWeddingInfo = None

        def Login(self, ch):
            if ch.GetPlayerID() == self.m_pid1:
                self.ch1 = ch
                if self.is_married:
                    SendLoverInfo(self.ch1, self.name2, self.GetMarriagePoint())
            elif ch.GetPlayerID() == self.m_pid2:
                self.ch2 = ch
                if self.is_married:
                    SendLoverInfo(self.ch2, self.name1, self.GetMarriagePoint())

            if self.IsOnline():
                self.ch1.SetMarryPartner(self.ch2)
                self.ch2.SetMarryPartner(self.ch1)

                self.StartNearCheckEvent()

            if self.is_married:
                d1 = None
                d2 = None
                pkCCI = None

                d1 = self.ch1.GetDesc() if self.ch1 is not None else None

                if d1 is None:
                    pkCCI = P2P_MANAGER.instance().FindByPID(self.m_pid1)

                    if pkCCI:
                        d1 = pkCCI.pkDesc
                        d1.SetRelay(pkCCI.szName)

                d2 = self.ch2.GetDesc() if self.ch2 is not None else None

                if d2 is None:
                    pkCCI = P2P_MANAGER.instance().FindByPID(self.m_pid2)

                    if pkCCI:
                        d2 = pkCCI.pkDesc
                        d2.SetRelay(pkCCI.szName)

                if d1 is not None and d2 is not None:
                    d1.ChatPacket(EChatType.CHAT_TYPE_COMMAND, "lover_login")
                    d2.ChatPacket(EChatType.CHAT_TYPE_COMMAND, "lover_login")
                    #sys_log(0, "lover_login %u %u", self.m_pid1, self.m_pid2)

        def Logout(self, pid):
            if pid == self.m_pid1:
                self.ch1 = None
            elif pid == self.m_pid2:
                self.ch2 = None

            if self.ch1 is not None or self.ch2 is not None:
                self.Save()

                if self.ch1:
                    self.ch1.SetMarryPartner(None)

                if self.ch2:
                    self.ch2.SetMarryPartner(None)

                self.StopNearCheckEvent()

            if self.is_married:
                d1 = None
                d2 = None
                pkCCI = None

                d1 = self.ch1.GetDesc() if self.ch1 is not None else None

                if d1 is None:
                    pkCCI = P2P_MANAGER.instance().FindByPID(self.m_pid1)

                    if pkCCI:
                        d1 = pkCCI.pkDesc
                        d1.SetRelay(pkCCI.szName)

                if d1 is not None and not g_bShutdown:
                    d1.ChatPacket(EChatType.CHAT_TYPE_COMMAND, "lover_logout")

                d2 = self.ch2.GetDesc() if self.ch2 is not None else None

                if d2 is None:
                    pkCCI = P2P_MANAGER.instance().FindByPID(self.m_pid2)

                    if pkCCI:
                        d2 = pkCCI.pkDesc
                        d2.SetRelay(pkCCI.szName)

                if d2 is not None and not g_bShutdown:
                    d2.ChatPacket(EChatType.CHAT_TYPE_COMMAND, "lover_logout")

        def IsOnline(self):
            return self.ch1 is not None and ch2 is not None

        def IsNear(self):
            if not self.is_married:
                return LGEMiscellaneous.DEFINECONSTANTS.false
            if not self.IsOnline():
                return LGEMiscellaneous.DEFINECONSTANTS.false

            return self.ch1.GetMapIndex() == self.ch2.GetMapIndex()

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: uint GetOther(uint PID) const
        def GetOther(self, PID):
            if self.m_pid1 == PID:
                return self.m_pid2

            if self.m_pid2 == PID:
                return self.m_pid1

            return 0

        def GetMarriagePoint(self):
            if test_server:
                value = quest.CQuestManager.instance().GetEventFlag("lovepoint")
                if value != 0:
                    return MINMAX(0, value, 100)

            LG_POINT_per_day = MARRIAGE_LG_POINT_PER_DAY
            max_limit = 30
            if self.IsOnline():
                if self.ch1.GetPremiumRemainSeconds(EPremiumTypes.PREMIUM_MARRIAGE_FAST) > 0 or self.ch2.GetPremiumRemainSeconds(EPremiumTypes.PREMIUM_MARRIAGE_FAST) > 0:
                    LG_POINT_per_day = MARRIAGE_LG_POINT_PER_DAY_FAST
                    max_limit = 40

            days = (get_global_time() - self.marry_time)
            if test_server:
                days = math.trunc(days / float(60))
            else:
                days = math.trunc(days / float(86400))

            return MIN(50 + MIN(days * LG_POINT_per_day, max_limit) + MIN(math.trunc(self.love_point / float(1000000)), max_limit), 100)

        def GetMarriageGrade(self):
            point = MINMAX(50, self.GetMarriagePoint(), 100)
            if point < 65:
                return 0
            elif point < 80:
                return 1
            elif point < 100:
                return 2
            return 3

        def GetBonus(self, dwItemVnum, bShare = (!LGEMiscellaneous.DefineConstants.false), me = None):
            if not self.is_married:
                return 0

            iFindedBonusIndex = 0
                iFindedBonusIndex = 0
                while iFindedBonusIndex < MAX_MARRIAGE_UNIQUE_ITEM:
                    if g_ItemBonus[iFindedBonusIndex].dwVnum == dwItemVnum:
                        break
                    iFindedBonusIndex += 1

                if iFindedBonusIndex == MAX_MARRIAGE_UNIQUE_ITEM:
                    return 0

            if bShare:
                count = 0
                if None is not self.ch1 and self.ch1.IsEquipUniqueItem(dwItemVnum):
                    count += 1
                if None is not self.ch2 and self.ch2.IsEquipUniqueItem(dwItemVnum):
                    count += 1

                rkBonus = g_ItemBonus[iFindedBonusIndex]

                if count>=1:
                    return rkBonus.value[self.GetMarriageGrade()]
                return 0
            else:
                count = 0
                if me is not self.ch1 and None is not self.ch1 and self.ch1.IsEquipUniqueItem(dwItemVnum):
                    count += 1
                if me is not self.ch2 and None is not self.ch2 and self.ch2.IsEquipUniqueItem(dwItemVnum):
                    count += 1

                rkBonus = g_ItemBonus[iFindedBonusIndex]

                if count>=1:
                    return rkBonus.value[self.GetMarriageGrade()]
                return 0

        def WarpToWeddingMap(self, dwPID):
            if self.pWeddingInfo is None:
                return

            ch = CHARACTER_MANAGER.instance().FindByPID(dwPID)
            if ch:
                pos = pixel_position_s()
                if not SECTREE_MANAGER.instance().GetRecallPositionByEmpire(math.trunc(self.pWeddingInfo.dwMapIndex / float(10000)), 0, pos):
                    #lani_err("cannot get warp position")
                    return
                ch.SaveExitLocation()
                ch.WarpSet(pos.x, pos.y, int(self.pWeddingInfo.dwMapIndex))

        def Save(self):
            #sys_log(0, "TMarriage::Save() - RequestUpdate.bSave=%d", self.bSave)
            if self.bSave:
                CManager.instance().RequestUpdate(self.m_pid1, self.m_pid2, self.love_point,1 if self.is_married else 0)
                self.bSave = LGEMiscellaneous.DEFINECONSTANTS.false

        def SetMarried(self):
            self.is_married = True
            self.bSave = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
            self.Save()

            if self.IsOnline():
                SendLoverInfo(self.ch1, self.name2, self.GetMarriagePoint())
                SendLoverInfo(self.ch2, self.name1, self.GetMarriagePoint())

                self.ch1.ChatPacket(EChatType.CHAT_TYPE_COMMAND, "lover_login")
                self.ch2.ChatPacket(EChatType.CHAT_TYPE_COMMAND, "lover_login")

        def Update(self, point):
            if not self.IsOnline():
                return

            if point > 0 and self.is_married:
                self.bSave = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
                self.love_point += int(point)

                self.love_point = MIN(self.love_point, 2000000000)

                if test_server:
                    ch = None
                    ch = CHARACTER_MANAGER.instance().FindByPID(self.m_pid1)
                    if ch:
                        ch.ChatPacket(EChatType.CHAT_TYPE_PARTY, "lovepoint bykill %.3g total %d", self.love_point / 1000000.0, self.GetMarriagePoint())
                    ch = CHARACTER_MANAGER.instance().FindByPID(self.m_pid2)
                    if ch:
                        ch.ChatPacket(EChatType.CHAT_TYPE_PARTY, "lovepoint bykill %.3g total %d", self.love_point / 1000000.0, self.GetMarriagePoint())

        def RequestEndWedding(self):
            if self.pWeddingInfo is None:
                return
            CManager.instance().RequestEndWedding(self.m_pid1, self.m_pid2)

        def StartNearCheckEvent(self):
            self.StopNearCheckEvent()

            info = Globals.AllocEventInfo()
            info.pMarriage = self
            self.eventNearCheck = event_create_ex(near_check_event, info, 1)

        def StopNearCheckEvent(self):
            self.byLastLovePoint = 0
            self.isLastNear = LGEMiscellaneous.DEFINECONSTANTS.false
            event_cancel(self.eventNearCheck)

        def NearCheck(self):
            if not self.is_married:
                return

            if not self.IsOnline():
                self.StopNearCheckEvent()
                return
            #sys_log(0, "NearCheck %u %u %d %d %d", self.m_pid1, self.m_pid2, self.IsNear(), self.isLastNear, self.byLastLovePoint, self.GetMarriagePoint())

            if self.IsNear() and not self.isLastNear:
                self.isLastNear = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
                self.ch1.ChatPacket(EChatType.CHAT_TYPE_COMMAND, "lover_near")
                self.ch2.ChatPacket(EChatType.CHAT_TYPE_COMMAND, "lover_near")
            elif (not self.IsNear()) and self.isLastNear:
                self.isLastNear = LGEMiscellaneous.DEFINECONSTANTS.false
                self.ch1.ChatPacket(EChatType.CHAT_TYPE_COMMAND, "lover_far")
                self.ch2.ChatPacket(EChatType.CHAT_TYPE_COMMAND, "lover_far")

            if self.byLastLovePoint != self.GetMarriagePoint():
                self.byLastLovePoint = byte(self.GetMarriagePoint())
                p = packet_love_LG_POINT_update()
                p.header = byte(Globals.LG_HEADER_GC_LOVE_LG_POINT_UPDATE)
                p.love_point = self.byLastLovePoint

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                self.ch1.GetDesc().Packet(p, sizeof(p))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                self.ch2.GetDesc().Packet(p, sizeof(p))


    class CManager(singleton):
        def __init__(self):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self._m_Marriages = _boost_func_of_void.unordered_set()
            self._m_MarriageByPID = {}
            self._m_setWedding = std::set()


        def close(self):
            pass

        def Initialize(self):
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        def Destroy(self):
            pass

        def Get(self, dwPlayerID):
            it = self._m_MarriageByPID.find(dwPlayerID)

            if it is not self._m_MarriageByPID.end():
                return it.second

            return None

        def IsMarriageUniqueItem(self, dwItemVnum):
            LaniatusDefVariables = 0
            while LaniatusDefVariables < MAX_MARRIAGE_UNIQUE_ITEM:
                if g_ItemBonus[LaniatusDefVariables].dwVnum == dwItemVnum:
                    return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
                LaniatusDefVariables += 1
            return LGEMiscellaneous.DEFINECONSTANTS.false

        def IsMarried(self, dwPlayerID):
            pkMarriageFinded = self.Get(dwPlayerID)
            if pkMarriageFinded is not None and pkMarriageFinded.is_married:
                return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

            return LGEMiscellaneous.DEFINECONSTANTS.false

        def IsEngaged(self, dwPlayerID):
            pkMarriageFinded = self.Get(dwPlayerID)
            if pkMarriageFinded is not None and not pkMarriageFinded.is_married:
                return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

            return LGEMiscellaneous.DEFINECONSTANTS.false

        def IsEngagedOrMarried(self, dwPlayerID):
            return self.Get(dwPlayerID) is not None

        def RequestAdd(self, dwPID1, dwPID2, szName1, szName2):
            if dwPID1 > dwPID2:
                std::swap(dwPID1, dwPID2)
                std::swap(szName1, szName2)

            p = TPacketMarriageAdd()

            p.dwPID1 = dwPID1
            p.dwPID2 = dwPID2
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            strncpy_s(p.szName1, sizeof(p.szName1), szName1, _TRUNCATE)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            strncpy_s(p.szName2, sizeof(p.szName2), szName2, _TRUNCATE)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            db_clientdesc.DBPacket(Globals.LG_HEADER_GD_MARRIAGE_ADD, 0, p, sizeof(p))

        def Add(self, dwPID1, dwPID2, tMarryTime, szName1, szName2):
            if self.IsEngagedOrMarried(dwPID1) or self.IsEngagedOrMarried(dwPID2):
                #lani_err("cannot marry already married character. %d - %d", dwPID1, dwPID2)
                return

            if dwPID1 > dwPID2:
                std::swap(dwPID1, dwPID2)
                std::swap(szName1, szName2)

            pMarriage = LG_NEW_M2 TMarriage(dwPID1, dwPID2, 0, tMarryTime, szName1, szName2)
            self._m_Marriages.insert(pMarriage)
            self._m_MarriageByPID.update({dwPID1: pMarriage})
            self._m_MarriageByPID.update({dwPID2: pMarriage})
                A = CHARACTER_MANAGER.instance().FindByPID(dwPID1)
                B = CHARACTER_MANAGER.instance().FindByPID(dwPID2)

                if A is not None and B is not None:
                    p = TPacketWeddingRequest()
                    p.dwPID1 = dwPID1
                    p.dwPID2 = dwPID2
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                    db_clientdesc.DBPacket(Globals.LG_HEADER_GD_WEDDING_REQUEST, 0, p, sizeof(p))

        def RequestUpdate(self, dwPID1, dwPID2, iUpdatePoint, byMarried):
            Align(dwPID1, dwPID2)

            p = TPacketMarriageUpdate()
            p.dwPID1 = dwPID1
            p.dwPID2 = dwPID2
            p.iLovePoint = iUpdatePoint
            p.byMarried = byMarried
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            db_clientdesc.DBPacket(Globals.LG_HEADER_GD_MARRIAGE_UPDATE, 0, p, sizeof(p))

        def Update(self, dwPID1, dwPID2, lTotalPoint, byMarried):
            pMarriage = self.Get(dwPID1)

            if pMarriage is None or pMarriage.GetOther(dwPID1) != dwPID2:
                #lani_err("not under marriage : %u %u", dwPID1, dwPID2)
                return

            pMarriage.love_point = lTotalPoint
            pMarriage.is_married = byMarried != 0

        def RequestRemove(self, dwPID1, dwPID2):
            Align(dwPID1, dwPID2)

            p = TPacketMarriageRemove()
            p.dwPID1 = dwPID1
            p.dwPID2 = dwPID2
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            db_clientdesc.DBPacket(Globals.LG_HEADER_GD_MARRIAGE_REMOVE, 0, p, sizeof(p))

        def Remove(self, dwPID1, dwPID2):
            pMarriage = self.Get(dwPID1)
            if pMarriage is None or pMarriage.GetOther(dwPID1) != dwPID2:
                #lani_err("not under marriage : %u %u", dwPID1, dwPID2)
                return

            self._m_Marriages.erase(pMarriage)
            self._m_MarriageByPID.pop(dwPID1)
            self._m_MarriageByPID.pop(dwPID2)

            LG_DEL_MEM(pMarriage)

        def Login(self, ch):
            pid = ch.GetPlayerID()

            pMarriage = self.Get(pid)
            if pMarriage is None:
                return

            pMarriage.Login(ch)

        def Logout(self, pid):
            pMarriage = self.Get(pid)

            if pMarriage is None:
                return

            pMarriage.Logout(pid)

        def Logout(self, ch):
            self.Logout(ch.GetPlayerID())

        def WeddingReady(self, dwPID1, dwPID2, dwMapIndex):
            pMarriage = self.Get(dwPID1)
            if pMarriage is None or pMarriage.GetOther(dwPID1) != dwPID2:
                #lani_err("wrong marriage %u, %u", dwPID1, dwPID2)
                return

            pwi = None
            if pMarriage.pWeddingInfo:
                pwi = pMarriage.pWeddingInfo
            else:
                pwi = LG_NEW_M2 TWeddingInfo
                pMarriage.pWeddingInfo = pwi

            pwi.dwMapIndex = dwMapIndex

        def WeddingStart(self, dwPID1, dwPID2):
            pMarriage = self.Get(dwPID1)
            if pMarriage is None or pMarriage.GetOther(dwPID1) != dwPID2:
                #lani_err("wrong marriage %u, %u", dwPID1, dwPID2)
                return

            pwi = pMarriage.pWeddingInfo

            if pwi is None:
                return

            pMarriage.WarpToWeddingMap(dwPID1)
            pMarriage.WarpToWeddingMap(dwPID2)
            self._m_setWedding.insert((dwPID1, dwPID2))

        def WeddingEnd(self, dwPID1, dwPID2):
            pMarriage = self.Get(dwPID1)
            if pMarriage is None or pMarriage.GetOther(dwPID1) != dwPID2:
                #lani_err("wrong marriage %u, %u", dwPID1, dwPID2)
                return

            if pMarriage.pWeddingInfo is None:
                #lani_err("not under wedding %u, %u", dwPID1, dwPID2)
                return

            if map_allow_find(WEDDING_MAP_INDEX):
                if not WeddingManager.instance().End(pMarriage.pWeddingInfo.dwMapIndex):
                    #lani_err("wedding map error: map_index=%d", pMarriage.pWeddingInfo.dwMapIndex)
                    return

            LG_DEL_MEM(pMarriage.pWeddingInfo)
            pMarriage.pWeddingInfo = None

            self._m_setWedding.erase((dwPID1, dwPID2))

        def RequestEndWedding(self, dwPID1, dwPID2):
            p = TPacketWeddingEnd()
            p.dwPID1 = dwPID1
            p.dwPID2 = dwPID2

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            db_clientdesc.DBPacket(Globals.LG_HEADER_GD_WEDDING_END, 0, p, sizeof(p))

        def for_each_wedding(self, f):
            it = m_setWedding.begin()
            while it is not self._m_setWedding.end():
                pMarriage = self.Get(it.first)
                if pMarriage:
                    f(pMarriage)
                it += 1
            return f



class marriage: #this class replaces the original namespace 'marriage'
    MAX_LOVE_GRADE = 4
    MAX_MARRIAGE_UNIQUE_ITEM = 6

    class TMarriageItemBonusByGrade:

        def __init__(self):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.dwVnum = 0
            self.value = [0 for _ in range(MAX_LOVE_GRADE)]

    g_ItemBonus = [TMarriageItemBonusByGrade(71069, [ 4, 5, 6, 8]), TMarriageItemBonusByGrade(71070, [ 10, 12, 15, 20]), TMarriageItemBonusByGrade(71071, [ 4, 5, 6, 8]), TMarriageItemBonusByGrade(71072, [ -4, -5, -6, -8]), TMarriageItemBonusByGrade(71073, [ 20, 25, 30, 40]), TMarriageItemBonusByGrade(71074, [ 12, 16, 20, 30])]

    MARRIAGE_LG_POINT_PER_DAY = 1
    MARRIAGE_LG_POINT_PER_DAY_FAST = 2

    @staticmethod
    def SendLoverInfo(ch, lover_name, love_point):
        p = packet_lover_info()

        p.header = byte(Globals.LG_HEADER_GC_LOVER_INFO)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        strncpy_s(p.name, sizeof(p.name), lover_name, _TRUNCATE)
        p.love_point = byte(love_point)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        ch.GetDesc().Packet(p, sizeof(p))

    class near_check_event_info(event_info_data):

        def __init__(self):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.pMarriage = None

            self.pMarriage = None

    @staticmethod
    def (UnnamedParameter):
        info = if isinstance(event.info, near_check_event_info) else None

        if info is None:
            #lani_err("near_check_event> <Factor> Null pointer")
            return 0

        pMarriage = info.pMarriage
        pMarriage.NearCheck()
        return ((5) * passes_per_sec)

    @staticmethod
    def Align(dwPID1, dwPID2):
        if dwPID1.arg_value > dwPID2.arg_value:
            std::swap(dwPID1.arg_value, dwPID2.arg_value)
