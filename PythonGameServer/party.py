from enum import Enum

class EPartyRole(Enum):
    PARTY_ROLE_NORMAL = 0
    PARTY_ROLE_LEADER = 1
    PARTY_ROLE_ATTACKER = 2
    PARTY_ROLE_TANKER = 3
    PARTY_ROLE_BUFFER = 4
    PARTY_ROLE_LG_SKILL_MASTER = 5
    PARTY_ROLE_HASTE = 6
    PARTY_ROLE_DEFENDER = 7
    PARTY_ROLE_MAX_NUM = 8

class EPartyExpDistributionModes(Enum):
    PARTY_EXP_DISTRIBUTION_NON_PARITY = 0
    PARTY_EXP_DISTRIBUTION_PARITY = 1
    PARTY_EXP_DISTRIBUTION_MAX_NUM = 2

## Laniatus Games Studio Inc. | NOTE: Python has no need of forward class declarations:
#class CParty
## Laniatus Games Studio Inc. | NOTE: Python has no need of forward class declarations:
#class CDungeon

class CPartyManager(singleton):

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self._m_map_pkParty = {}
        self._m_map_pkMobParty = {}
        self._m_set_pkPCParty = std::set()
        self._m_bEnablePCParty = False

        self.Initialize()

    def close(self):
        pass

    def Initialize(self):
        self._m_bEnablePCParty = LGEMiscellaneous.DEFINECONSTANTS.false

    def EnablePCParty(self):
        self._m_bEnablePCParty = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
        #sys_log(0,"PARTY Enable")
    def DisablePCParty(self):
        self._m_bEnablePCParty = LGEMiscellaneous.DEFINECONSTANTS.false
        #sys_log(0,"PARTY Disable")
    def IsEnablePCParty(self):
        return self._m_bEnablePCParty

    def CreateParty(self, pLeader):
        if pLeader.GetParty():
            return pLeader.GetParty()

        pParty = LG_NEW_M2 CParty

        if pLeader.IsPC():
            p = SPacketPartyCreate()
            p.dwLeaderPID = pLeader.GetPlayerID()

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            db_clientdesc.DBPacket(Globals.LG_HEADER_GD_PARTY_CREATE, 0, p, sizeof(SPacketPartyCreate))

            #sys_log(0, "PARTY: Create %s pid %u", pLeader.GetName(LOCALE_LANIATUS), pLeader.GetPlayerID())
            pParty.SetPCParty(((not LGEMiscellaneous.DEFINECONSTANTS.false)))
            pParty.Join(pLeader.GetPlayerID())

            self._m_set_pkPCParty.insert(pParty)
        else:
            pParty.SetPCParty(LGEMiscellaneous.DEFINECONSTANTS.false)
            pParty.Join(pLeader.GetVID())

        pParty.Link(pLeader)
        return (pParty)

    def DeleteParty(self, pParty):
        p = SPacketPartyDelete()
        p.dwLeaderPID = pParty.GetLeaderPID()

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        db_clientdesc.DBPacket(Globals.LG_HEADER_GD_PARTY_DELETE, 0, p, sizeof(SPacketPartyDelete))

        self._m_set_pkPCParty.erase(pParty)
        LG_DEL_MEM(pParty)

    def DeleteAllParty(self):
        it = self._m_set_pkPCParty.begin()

        while it is not self._m_set_pkPCParty.end():
            self.DeleteParty(it)
            it = self._m_set_pkPCParty.begin()

    def SetParty(self, ch):
        it = self._m_map_pkParty.find(ch.GetPlayerID())

        if it is self._m_map_pkParty.end():
            return LGEMiscellaneous.DEFINECONSTANTS.false

        pParty = it.second
        pParty.Link(ch)
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def SetPartyMember(self, dwPID, pParty):
        it = self._m_map_pkParty.find(dwPID)

        if pParty is None:
            if it is not self._m_map_pkParty.end():
                self._m_map_pkParty.pop(it)
        else:
            if it is not self._m_map_pkParty.end():
                if it.second is not pParty:
                    it.second.Quit(dwPID)
                    it.second = pParty
            else:
                self._m_map_pkParty.insert(TPartyMap.value_type(dwPID, pParty))

    def P2PLogin(self, pid, name):
        it = self._m_map_pkParty.find(pid)

        if it is self._m_map_pkParty.end():
            return

        it.second.UpdateOnlineState(pid, name)

    def P2PLogout(self, pid):
        it = self._m_map_pkParty.find(pid)

        if it is self._m_map_pkParty.end():
            return

        it.second.UpdateOfflineState(pid)

    def P2PCreateParty(self, pid):
        it = self._m_map_pkParty.find(pid)
        if it is not self._m_map_pkParty.end():
            return it.second

        pParty = LG_NEW_M2 CParty

        self._m_set_pkPCParty.insert(pParty)

        self.SetPartyMember(pid, pParty)
        pParty.SetPCParty(((not LGEMiscellaneous.DEFINECONSTANTS.false)))
        pParty.P2PJoin(pid)

        return pParty

    def P2PDeleteParty(self, pid):
        it = self._m_map_pkParty.find(pid)

        if it is not self._m_map_pkParty.end():
            self._m_set_pkPCParty.erase(it.second)
            LG_DEL_MEM(it.second)
        else:
            #lani_err("PARTY P2PDeleteParty Cannot find party [%u]", pid)

    def P2PJoinParty(self, leader, pid, role = 0):
        it = self._m_map_pkParty.find(leader)

        if it is not self._m_map_pkParty.end():
            it.second.P2PJoin(pid)

            if role >= EPartyRole.PARTY_ROLE_MAX_NUM:
                role = EPartyRole.PARTY_ROLE_NORMAL

            it.second.SetRole(pid, role, ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
        else:
            #lani_err("No such party with leader [%d]", leader)

    def P2PQuitParty(self, pid):
        it = self._m_map_pkParty.find(pid)

        if it is not self._m_map_pkParty.end():
            it.second.P2PQuit(pid)
        else:
            #lani_err("No such party with member [%d]", pid)




class EPartyMessages(Enum):
    PM_ATTACK = 0
    PM_RETURN = 1
    PM_ATTACKED_BY = 2
    PM_AGGRO_INCREASE = 3

class CParty:
    class SMember:

        def __init__(self):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.pCharacter = None
            self.bNear = False
            self.bRole = 0
            self.bLevel = 0
            self.strName = ""




    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.m_memberMap = {}
        self.m_dwLeaderPID = 0
        self.m_pkChrLeader = None
        self.m_eventUpdate = _boost_func_of_void.intrusive_ptr()
        self.m_itNextOwner = None
        self._m_iExpDistributionMode = 0
        self._m_pkChrExpCentralize = None
        self._m_dwPartyStartTime = 0
        self._m_dwPartyHealTime = 0
        self._m_bPartyHealReady = False
        self._m_bCanUsePartyHeal = False
        self._m_anRoleCount = [0 for _ in range((int)EPartyRole.PARTY_ROLE_MAX_NUM)]
        self._m_anMaxRole = [0 for _ in range((int)EPartyRole.PARTY_ROLE_MAX_NUM)]
        self._m_iLongTimeExpBonus = 0
        self._m_iLeadership = 0
        self._m_iExpBonus = 0
        self._m_iAttBonus = 0
        self._m_iDefBonus = 0
        self._m_iCountNearPartyMember = 0
        self._m_bPCParty = False
        self._m_map_iFlag = {}
        self._m_pkDungeon = None
        self._m_pkDungeon_for_Only_party = None

        self.Initialize()

    def close(self):
        self.Destroy()

    def P2PJoin(self, dwPID):
        it = self.m_memberMap.find(dwPID)

        if it is self.m_memberMap.end():
            Member = TMember()

            Member.pCharacter = None
            Member.bNear = LGEMiscellaneous.DEFINECONSTANTS.false

            if not self.m_memberMap:
                Member.bRole = EPartyRole.PARTY_ROLE_LEADER
                self.m_dwLeaderPID = dwPID
            else:
                Member.bRole = EPartyRole.PARTY_ROLE_NORMAL

            if self._m_bPCParty:
                ch = CHARACTER_MANAGER.instance().FindByPID(dwPID)

                if ch:
                    #sys_log(0, "PARTY: Join %s pid %u leader %u", ch.GetName(LOCALE_LANIATUS), dwPID, self.m_dwLeaderPID)
                    Member.strName = ch.GetName(LOCALE_LANIATUS)

                    if Member.bRole == EPartyRole.PARTY_ROLE_LEADER:
                        self._m_iLeadership = ch.GetLeadershipSkillLevel()
                else:
                    pcci = P2P_MANAGER.instance().FindByPID(dwPID)

                    if pcci is None:
                        pass
                    elif pcci.bChannel == g_bChannel:
                        Member.strName = pcci.szName
                    else:
                        #lani_err("member is not in same channel PID: %u channel %d, this channel %d", dwPID, pcci.bChannel, g_bChannel)

            #sys_log(2, "PARTY[%d] MemberCountChange %d -> %d", self.GetLeaderPID(), self.GetMemberCount(), self.GetMemberCount()+1)

            self.m_memberMap.insert(TMemberMap.value_type(dwPID, Member))

            if len(self.m_memberMap) == 1:
                self.m_itNextOwner = self.m_memberMap.begin()

            if self._m_bPCParty:
                CPartyManager.instance().SetPartyMember(dwPID, self)
                self.SendPartyJoinOneToAll(dwPID)

                ch = CHARACTER_MANAGER.instance().FindByPID(dwPID)

                if ch:
                    self.SendParameter(ch)

        if self._m_pkDungeon:
            self._m_pkDungeon.QuitParty(self)

    def P2PQuit(self, dwPID):
        it = self.m_memberMap.find(dwPID)

        if it is self.m_memberMap.end():
            return

        if self._m_bPCParty:
            self.SendPartyRemoveOneToAll(dwPID)

        if it is self.m_itNextOwner:
            self.IncreaseOwnership()

        if self._m_bPCParty:
            self.RemoveBonusForOne(dwPID)

        ch = it.second.pCharacter
        bRole = it.second.bRole

        self.m_memberMap.pop(it)

        #sys_log(2, "PARTY[%d] MemberCountChange %d -> %d", self.GetLeaderPID(), self.GetMemberCount(), self.GetMemberCount() - 1)

        if bRole < EPartyRole.PARTY_ROLE_MAX_NUM:
            self._m_anRoleCount[bRole] -= 1
        else:
            #lani_err("ROLE_COUNT_QUIT_ERROR: INDEX(%d) > MAX(%d)", bRole, EPartyRole.PARTY_ROLE_MAX_NUM)

        if ch:
            ch.SetParty(None)
            self.ComputeRolePoint(ch, bRole, LGEMiscellaneous.DEFINECONSTANTS.false)

        if self._m_bPCParty:
            CPartyManager.instance().SetPartyMember(dwPID, None)

        if bRole == EPartyRole.PARTY_ROLE_LEADER:
            CPartyManager.instance().DeleteParty(self)

    def Join(self, dwPID):
        self.P2PJoin(dwPID)

        if self._m_bPCParty:
            p = SPacketPartyAdd()
            p.dwLeaderPID = self.GetLeaderPID()
            p.dwPID = dwPID
            p.bState = EPartyRole.PARTY_ROLE_NORMAL
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            db_clientdesc.DBPacket(Globals.LG_HEADER_GD_PARTY_ADD, 0, p, sizeof(p))

    def Quit(self, dwPID):
        self.P2PQuit(dwPID)

        if self._m_bPCParty and dwPID != self.GetLeaderPID():
            p = SPacketPartyRemove()
            p.dwPID = dwPID
            p.dwLeaderPID = self.GetLeaderPID()
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            db_clientdesc.DBPacket(Globals.LG_HEADER_GD_PARTY_REMOVE, 0, p, sizeof(p))

    def Link(self, pkChr):
        it = TMemberMap.iterator()

        if pkChr.IsPC():
            it = self.m_memberMap.find(pkChr.GetPlayerID())
        else:
            it = self.m_memberMap.find(pkChr.GetVID())

        if it is self.m_memberMap.end():
            #lani_err("%s is not member of this party", pkChr.GetName(LOCALE_LANIATUS))
            return

        if self._m_bPCParty and self.m_eventUpdate is None:
            info = Globals.AllocEventInfo()
            info.pid = self.m_dwLeaderPID
            self.m_eventUpdate = event_create_ex(party_update_event, info, ((3) * passes_per_sec))

        if it.second.bRole == EPartyRole.PARTY_ROLE_LEADER:
            self.m_pkChrLeader = pkChr

        #sys_log(2, "PARTY[%d] %s linked to party", self.GetLeaderPID(), pkChr.GetName(LOCALE_LANIATUS))

        it.second.pCharacter = pkChr
        pkChr.SetParty(self)

        if pkChr.IsPC():
            if it.second.strName.empty():
                it.second.strName = pkChr.GetName(LOCALE_LANIATUS)

            self.SendPartyJoinOneToAll(pkChr.GetPlayerID())

            self.SendPartyJoinAllToOne(pkChr)
            self.SendPartyLinkOneToAll(pkChr)
            self.SendPartyLinkAllToOne(pkChr)
            self.SendPartyInfoAllToOne(pkChr)
            self.SendPartyInfoOneToAll(pkChr)
            self.SendParameter(pkChr)

            if self.GetDungeon() is not None and self.GetDungeon().GetMapIndex() == pkChr.GetMapIndex():
                pkChr.SetDungeon(self.GetDungeon())

            self.RequestSetMemberLevel(pkChr.GetPlayerID(), byte(pkChr.GetLevel()))


    def Unlink(self, pkChr):
        it = TMemberMap.iterator()

        if pkChr.IsPC():
            it = self.m_memberMap.find(pkChr.GetPlayerID())
        else:
            it = self.m_memberMap.find(pkChr.GetVID())

        if it is self.m_memberMap.end():
            #lani_err("%s is not member of this party", pkChr.GetName(LOCALE_LANIATUS))
            return

        if pkChr.IsPC():
            self.SendPartyUnlinkOneToAll(pkChr)

            if it.second.bRole == EPartyRole.PARTY_ROLE_LEADER:
                self.RemoveBonus()

                if it.second.pCharacter.GetDungeon():
                    f = FExitDungeon()
                    self.ForEachNearMember(f.functor_method)

        if it.second.bRole == EPartyRole.PARTY_ROLE_LEADER:
            self.m_pkChrLeader = None

        it.second.pCharacter = None
        pkChr.SetParty(None)

    def ChatPacketToAllMember(self, type, format, *LegacyParamArray):
        chatbuf = str(['\0' for _ in range((int)LGEMiscellaneous.CHAT_MAX_LEN + 1)])
        args = None

        ParamCount = -1
#        va_start(args, format)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        vsnprintf(chatbuf, sizeof(chatbuf), format, args)
#        va_end(args)

        it = m_memberMap.begin()
        while it is not self.m_memberMap.end():
            rMember = it.second

            if rMember.pCharacter:
                if rMember.pCharacter.GetDesc():
                    rMember.pCharacter.ChatPacket(type, "%s", chatbuf)
            it += 1

    def UpdateOnlineState(self, dwPID, name):
        r = self.m_memberMap[dwPID]

        p = packet_party_add()

        p.header = byte(Globals.LG_HEADER_GC_PARTY_ADD)
        p.pid = dwPID
        r.strName = name
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        strncpy_s(p.name, sizeof(p.name), name, _TRUNCATE)

        it = m_memberMap.begin()
        while it is not self.m_memberMap.end():
            if it.second.pCharacter and it.second.pCharacter.GetDesc():
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                it.second.pCharacter.GetDesc().Packet(p, sizeof(p))
            it += 1

    def UpdateOfflineState(self, dwPID):
        p = packet_party_add()
        p.header = byte(Globals.LG_HEADER_GC_PARTY_ADD)
        p.pid = dwPID
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
        memset(p.name, 0, LGEMiscellaneous.CHARACTER_NAME_MAX_LEN+1)

        it = m_memberMap.begin()
        while it is not self.m_memberMap.end():
            if it.second.pCharacter and it.second.pCharacter.GetDesc():
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                it.second.pCharacter.GetDesc().Packet(p, sizeof(p))
            it += 1

    def GetLeaderPID(self):
        return self.m_dwLeaderPID

    def GetLeaderCharacter(self):
        return self.m_memberMap[self.GetLeaderPID()].pCharacter

    def GetLeader(self):
        return self.m_pkChrLeader

    def GetMemberCount(self):
        return len(self.m_memberMap)

    def GetNearMemberCount(self):
        return uint(self._m_iCountNearPartyMember)

    def IsMember(self, pid):
        return pid in self.m_memberMap.keys()

    def IsNearLeader(self, pid):
        it = self.m_memberMap.find(pid)

        if it is self.m_memberMap.end():
            return LGEMiscellaneous.DEFINECONSTANTS.false

        return it.second.bNear

    def IsPositionNearLeader(self, ch):
        if self.m_pkChrLeader is None:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if Globals.DISTANCE_APPROX(ch.GetX() - self.m_pkChrLeader.GetX(), ch.GetY() - self.m_pkChrLeader.GetY()) >= Globals.PARTY_DEFAULT_RANGE:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def SendMessage(self, ch, bMsg, dwArg1, dwArg2):
        if ch.GetParty() is not self:
            #lani_err("%s is not member of this party %p", ch.GetName(LOCALE_LANIATUS), self)
            return

        if bMsg == EPartyMessages.PM_ATTACK:
            pass

        elif bMsg == EPartyMessages.PM_RETURN:
                it = self.m_memberMap.begin()

                while it is not self.m_memberMap.end():
                    rMember = it.second
                    it += 1

                    pkChr = None

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((pkChr = rMember.pCharacter) && ch != pkChr)
                    if (pkChr = rMember.pCharacter) and ch is not pkChr:
                        x = dwArg1 + number(-500, 500)
                        y = dwArg2 + number(-500, 500)

                        pkChr.SetVictim(None)
                        pkChr.SetRotationToXY(int(x), int(y))

                        if pkChr.Goto(int(x), int(y)):
                            victim = pkChr.GetVictim()
                            #sys_log(0, "%s %p RETURN victim %p", pkChr.GetName(LOCALE_LANIATUS), Globals.get_pointer(pkChr), Globals.get_pointer(victim))
                            pkChr.SendMovePacket(EMoveFuncType.FUNC_WAIT, 0, 0, 0, 0, 0, -1)

        elif bMsg == EPartyMessages.PM_ATTACKED_BY:
                pkChrVictim = ch.GetVictim()

                if pkChrVictim is None:
                    return

                it = self.m_memberMap.begin()

                while it is not self.m_memberMap.end():
                    rMember = it.second
                    it += 1

                    pkChr = None

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((pkChr = rMember.pCharacter) && ch != pkChr)
                    if (pkChr = rMember.pCharacter) and ch is not pkChr:
                        if pkChr.CanBeginFight():
                            pkChr.BeginFight(pkChrVictim)

        elif bMsg == EPartyMessages.PM_AGGRO_INCREASE:
                victim = CHARACTER_MANAGER.instance().Find(dwArg2)

                if victim is None:
                    return

                it = self.m_memberMap.begin()

                while it is not self.m_memberMap.end():
                    rMember = it.second
                    it += 1

                    pkChr = None

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((pkChr = rMember.pCharacter) && ch != pkChr)
                    if (pkChr = rMember.pCharacter) and ch is not pkChr:
                        pkChr.UpdateAggrPoint(victim, EDamageType.DAMAGE_TYPE_SPECIAL, int(dwArg1))

    def SendPartyJoinOneToAll(self, pid):
        r = self.m_memberMap[pid]

        p = packet_party_add()

        p.header = byte(Globals.LG_HEADER_GC_PARTY_ADD)
        p.pid = pid
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        strncpy_s(p.name, sizeof(p.name), r.strName.c_str(), _TRUNCATE)

        it = m_memberMap.begin()
        while it is not self.m_memberMap.end():
            if it.second.pCharacter and it.second.pCharacter.GetDesc():
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                it.second.pCharacter.GetDesc().Packet(p, sizeof(p))
            it += 1

    def SendPartyJoinAllToOne(self, ch):
        if ch.GetDesc() is None:
            return

        p = packet_party_add()

        p.header = byte(Globals.LG_HEADER_GC_PARTY_ADD)
        p.name[(int)LGEMiscellaneous.CHARACTER_NAME_MAX_LEN] = '\0'

        it = m_memberMap.begin()
        while it is not self.m_memberMap.end():
            p.pid = it.first
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            strncpy_s(p.name, sizeof(p.name), it.second.strName.c_str(), _TRUNCATE)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            ch.GetDesc().Packet(p, sizeof(p))
            it += 1

    def SendPartyRemoveOneToAll(self, pid):
        p = packet_party_remove()
        p.header = byte(Globals.LG_HEADER_GC_PARTY_REMOVE)
        p.pid = pid

        it = m_memberMap.begin()
        while it is not self.m_memberMap.end():
            if it.second.pCharacter and it.second.pCharacter.GetDesc():
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                it.second.pCharacter.GetDesc().Packet(p, sizeof(p))
            it += 1

    def SendPartyInfoOneToAll(self, pid):
        it = self.m_memberMap.find(pid)

        if it is self.m_memberMap.end():
            return

        if it.second.pCharacter:
            SendPartyInfoOneToAll(it.second.pCharacter)
            return

        p = TPacketGCPartyUpdate()
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memset(p, 0, sizeof(p))
        p.header = Globals.LG_HEADER_GC_PARTY_UPDATE
        p.pid = pid
        p.percent_hp = 255
        p.role = it.second.bRole

        it = m_memberMap.begin()
        while it is not self.m_memberMap.end():
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following line could not be converted:
            if ((it.second.pCharacter) && (it.second.pCharacter.GetDesc()))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                it.second.pCharacter.GetDesc().Packet(p, sizeof(p))
            it += 1

    def SendPartyInfoOneToAll(self, ch):
        if ch.GetDesc() is None:
            return

        p = TPacketGCPartyUpdate()
        ch.BuildUpdatePartyPacket(p)

        it = m_memberMap.begin()
        while it is not self.m_memberMap.end():
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following line could not be converted:
            if ((it.second.pCharacter) && (it.second.pCharacter.GetDesc()))
                #sys_log(2, "PARTY send info %s[%d] to %s[%d]", ch.GetName(LOCALE_LANIATUS), ch.GetVID(), it.second.pCharacter.GetName(), it.second.pCharacter.GetVID())
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                it.second.pCharacter.GetDesc().Packet(p, sizeof(p))
            it += 1

    def SendPartyInfoAllToOne(self, ch):
        p = TPacketGCPartyUpdate()

        it = m_memberMap.begin()
        while it is not self.m_memberMap.end():
            if not it.second.pCharacter:
                pid = it.first
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                memset(p, 0, sizeof(p))
                p.header = Globals.LG_HEADER_GC_PARTY_UPDATE
                p.pid = pid
                p.percent_hp = 255
                p.role = it.second.bRole
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                ch.GetDesc().Packet(p, sizeof(p))
                continue

            it.second.pCharacter.BuildUpdatePartyPacket(p)
            #sys_log(2, "PARTY send info %s[%d] to %s[%d]", it.second.pCharacter.GetName(), it.second.pCharacter.GetVID(), ch.GetName(LOCALE_LANIATUS), ch.GetVID())
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            ch.GetDesc().Packet(p, sizeof(p))
            it += 1

    def SendPartyLinkOneToAll(self, ch):
        if ch.GetDesc() is None:
            return

        p = packet_party_link()
        p.header = byte(Globals.LG_HEADER_GC_PARTY_LINK)
        p.vid = ch.GetVID()
        p.pid = ch.GetPlayerID()

        it = m_memberMap.begin()
        while it is not self.m_memberMap.end():
            if it.second.pCharacter and it.second.pCharacter.GetDesc():
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                it.second.pCharacter.GetDesc().Packet(p, sizeof(p))
            it += 1

    def SendPartyLinkAllToOne(self, ch):
        if ch.GetDesc() is None:
            return

        p = packet_party_link()
        p.header = byte(Globals.LG_HEADER_GC_PARTY_LINK)

        it = m_memberMap.begin()
        while it is not self.m_memberMap.end():
            if it.second.pCharacter:
                p.vid = it.second.pCharacter.GetVID()
                p.pid = it.second.pCharacter.GetPlayerID()
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                ch.GetDesc().Packet(p, sizeof(p))
            it += 1

    def SendPartyUnlinkOneToAll(self, ch):
        if ch.GetDesc() is None:
            return

        p = packet_party_link()
        p.header = byte(Globals.LG_HEADER_GC_PARTY_UNLINK)
        p.pid = ch.GetPlayerID()
        p.vid = ch.GetVID()

        it = m_memberMap.begin()
        while it is not self.m_memberMap.end():
            if it.second.pCharacter and it.second.pCharacter.GetDesc():
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                it.second.pCharacter.GetDesc().Packet(p, sizeof(p))
            it += 1

    def GetPartyBonusExpPercent(self):
        return self._m_iExpBonus
    def GetPartyBonusAttackGrade(self):
        return self._m_iAttBonus
    def GetPartyBonusDefenseGrade(self):
        return self._m_iDefBonus

    def ComputePartyBonusExpPercent(self):
        if self.GetNearMemberCount() <= 1:
            return 0

        leader = self.GetLeaderCharacter()

        iBonusPartyExpFromItem = 0
        iMemberCount = MIN(8, self.GetNearMemberCount())

        if leader is not None and (leader.IsEquipUniqueItem(uint(Globals.UNIQUE_ITEM_PARTY_BONUS_EXP)) or leader.IsEquipUniqueItem(uint(Globals.UNIQUE_ITEM_PARTY_BONUS_EXP_MALL)) or leader.IsEquipUniqueItem(uint(Globals.UNIQUE_ITEM_PARTY_BONUS_EXP_GIFT)) or leader.IsEquipUniqueGroup(10010)):
            iBonusPartyExpFromItem = 30

        return iBonusPartyExpFromItem + CHN_aiPartyBonusExpPercentByMemberCount[iMemberCount]

    def ComputePartyBonusAttackGrade(self):
        return 0

    def ComputePartyBonusDefenseGrade(self):
        return 0

    def ForEachMember(self, f):
        it = m_memberMap.begin()
        while it is not self.m_memberMap.end():
            f(it.first)
            it += 1

    def ForEachMemberPtr(self, f):
        it = m_memberMap.begin()
        while it is not self.m_memberMap.end():
            f(it.second.pCharacter)
            it += 1

    def ForEachOnlineMember(self, f):
        it = m_memberMap.begin()
        while it is not self.m_memberMap.end():
            if it.second.pCharacter:
                f(it.second.pCharacter)
            it += 1

    def ForEachNearMember(self, f):
        it = m_memberMap.begin()
        while it is not self.m_memberMap.end():
            if it.second.pCharacter and it.second.bNear:
                f(it.second.pCharacter)
            it += 1

    def ForEachOnMapMember(self, f, lMapIndex):
        it = m_memberMap.begin()
        while it is not self.m_memberMap.end():
            ch = it.second.pCharacter
            if ch:
                if ch.GetMapIndex() == lMapIndex:
                    f(ch)
            it += 1

    def ForEachOnMapMemberBool(self, f, lMapIndex):
        it = m_memberMap.begin()
        while it is not self.m_memberMap.end():
            ch = it.second.pCharacter
            if ch:
                if ch.GetMapIndex() == lMapIndex:
                    if f(ch) == LGEMiscellaneous.DEFINECONSTANTS.false:
                        return LGEMiscellaneous.DEFINECONSTANTS.false

            it += 1
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def Update(self):
        #sys_log(1, "PARTY::Update")

        l = self.GetLeaderCharacter()

        if l is None:
            return

        iNearMember = 0
        bResendAll = LGEMiscellaneous.DEFINECONSTANTS.false

        it = m_memberMap.begin()
        while it is not self.m_memberMap.end():
            ch = it.second.pCharacter

            it.second.bNear = LGEMiscellaneous.DEFINECONSTANTS.false

            if ch is None:
                continue

            if l.GetDungeon():
                it.second.bNear = l.GetDungeon() is ch.GetDungeon()
            else:
                it.second.bNear = (Globals.DISTANCE_APPROX(l.GetX()-ch.GetX(), l.GetY()-ch.GetY()) < Globals.PARTY_DEFAULT_RANGE)

            if it.second.bNear:
                iNearMember += 1
            it += 1

        if iNearMember <= 1 and l.GetDungeon() is None:
            it = m_memberMap.begin()
            while it is not self.m_memberMap.end():
                it.second.bNear = LGEMiscellaneous.DEFINECONSTANTS.false
                it += 1

            iNearMember = 0

        if iNearMember != self._m_iCountNearPartyMember:
            self._m_iCountNearPartyMember = iNearMember
            bResendAll = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        self._m_iLeadership = l.GetLeadershipSkillLevel()
        iNewExpBonus = self.ComputePartyBonusExpPercent()
        self._m_iAttBonus = self.ComputePartyBonusAttackGrade()
        self._m_iDefBonus = self.ComputePartyBonusDefenseGrade()

        if self._m_iExpBonus != iNewExpBonus:
            bResendAll = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
            self._m_iExpBonus = iNewExpBonus

        bLongTimeExpBonusChanged = LGEMiscellaneous.DEFINECONSTANTS.false


        if self._m_iLongTimeExpBonus == 0 and (get_dword_time() - self._m_dwPartyStartTime > Globals.PARTY_ENOUGH_MINUTE_FOR_EXP_BONUS * 30 * 1000):
            bLongTimeExpBonusChanged = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
            self._m_iLongTimeExpBonus = 5
            bResendAll = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        it = m_memberMap.begin()
        while it is not self.m_memberMap.end():
            ch = it.second.pCharacter

            if ch is None:
                continue

            if bLongTimeExpBonusChanged and ch.GetDesc():
                ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Your Group cooperates and received an Experience Bonus."))

            bNear = it.second.bNear

            self.ComputeRolePoint(ch, it.second.bRole, bNear)

            if bNear:
                if not bResendAll:
                    self.SendPartyInfoOneToAll(ch)
            it += 1

        self._m_anMaxRole[(int)EPartyRole.PARTY_ROLE_ATTACKER] = 1 if self._m_iLeadership >= 10 else 0
        self._m_anMaxRole[(int)EPartyRole.PARTY_ROLE_HASTE] = 1 if self._m_iLeadership >= 20 else 0
        self._m_anMaxRole[(int)EPartyRole.PARTY_ROLE_TANKER] = 1 if self._m_iLeadership >= 20 else 0
        self._m_anMaxRole[(int)EPartyRole.PARTY_ROLE_BUFFER] = 1 if self._m_iLeadership >= 25 else 0
        self._m_anMaxRole[(int)EPartyRole.PARTY_ROLE_LG_SKILL_MASTER] = 1 if self._m_iLeadership >= 35 else 0
        self._m_anMaxRole[(int)EPartyRole.PARTY_ROLE_DEFENDER] = 1 if self._m_iLeadership >= 40 else 0
        self._m_anMaxRole[(int)EPartyRole.PARTY_ROLE_ATTACKER] += 1 if self._m_iLeadership >= 40 else 0

        if not self._m_bPartyHealReady:
            if (not self._m_bCanUsePartyHeal) and self._m_iLeadership >= 18:
                self._m_dwPartyHealTime = get_dword_time()

            self._m_bCanUsePartyHeal = self._m_iLeadership >= 18

            PartyHealCoolTime = Globals.PARTY_HEAL_COOLTIME_SHORT * 60 * 1000 if (self._m_iLeadership >= 40) else Globals.PARTY_HEAL_COOLTIME_LONG * 60 * 1000

            if self._m_bCanUsePartyHeal:
                if get_dword_time() > self._m_dwPartyHealTime + PartyHealCoolTime:
                    self._m_bPartyHealReady = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

                    if False:
                        if self.GetLeaderCharacter():
                            self.GetLeaderCharacter().ChatPacket(EChatType.CHAT_TYPE_COMMAND, "PartyHealReady")

        if bResendAll:
            it = m_memberMap.begin()
            while it is not self.m_memberMap.end():
                if it.second.pCharacter:
                    SendPartyInfoOneToAll(it.second.pCharacter)
                it += 1

    def GetExpBonusPercent(self):
        if self.GetNearMemberCount() <= 1:
            return 0

        return self._m_iExpBonus + self._m_iLongTimeExpBonus

    def SetRole(self, dwPID, bRole, bSet):
        it = self.m_memberMap.find(dwPID)

        if it is self.m_memberMap.end():
            return LGEMiscellaneous.DEFINECONSTANTS.false

        ch = it.second.pCharacter

        if bSet:
            if self._m_anRoleCount[bRole] >= self._m_anMaxRole[bRole]:
                return LGEMiscellaneous.DEFINECONSTANTS.false

            if it.second.bRole != EPartyRole.PARTY_ROLE_NORMAL:
                return LGEMiscellaneous.DEFINECONSTANTS.false

            it.second.bRole = bRole

            if ch is not None and self.GetLeader() is not None:
                self.ComputeRolePoint(ch, bRole, ((not LGEMiscellaneous.DEFINECONSTANTS.false)))

            if bRole < EPartyRole.PARTY_ROLE_MAX_NUM:
                self._m_anRoleCount[bRole] += 1
            else:
                #lani_err("ROLE_COUNT_INC_ERROR: INDEX(%d) > MAX(%d)", bRole, EPartyRole.PARTY_ROLE_MAX_NUM)
        else:
            if it.second.bRole == EPartyRole.PARTY_ROLE_LEADER:
                return LGEMiscellaneous.DEFINECONSTANTS.false

            if it.second.bRole == EPartyRole.PARTY_ROLE_NORMAL:
                return LGEMiscellaneous.DEFINECONSTANTS.false

            it.second.bRole = EPartyRole.PARTY_ROLE_NORMAL

            if ch is not None and self.GetLeader() is not None:
                self.ComputeRolePoint(ch, EPartyRole.PARTY_ROLE_NORMAL, LGEMiscellaneous.DEFINECONSTANTS.false)

            if bRole < EPartyRole.PARTY_ROLE_MAX_NUM:
                self._m_anRoleCount[bRole] -= 1
            else:
                #lani_err("ROLE_COUNT_DEC_ERROR: INDEX(%d) > MAX(%d)", bRole, EPartyRole.PARTY_ROLE_MAX_NUM)

        self.SendPartyInfoOneToAll(dwPID)
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def GetRole(self, pid):
        it = self.m_memberMap.find(pid)

        if it is self.m_memberMap.end():
            return EPartyRole.PARTY_ROLE_NORMAL
        else:
            return it.second.bRole

    def IsRole(self, pid, bRole):
        it = self.m_memberMap.find(pid)

        if it is self.m_memberMap.end():
            return LGEMiscellaneous.DEFINECONSTANTS.false

        return it.second.bRole == bRole

    def GetMemberMaxLevel(self):
        bMax = 0

        it = self.m_memberMap.begin()
        while it is not self.m_memberMap.end():
            if not it.second.bLevel:
                it += 1
                continue

            if bMax == 0:
                bMax = it.second.bLevel
            elif it.second.bLevel:
                bMax = MAX(bMax, it.second.bLevel)
            it += 1
        return bMax

    def GetMemberMinLevel(self):
        bMin = LGEMiscellaneous.PLAYER_MAX_LEVEL_CONST

        it = self.m_memberMap.begin()
        while it is not self.m_memberMap.end():
            if not it.second.bLevel:
                it += 1
                continue

            if bMin == 0:
                bMin = it.second.bLevel
            elif it.second.bLevel:
                bMin = MIN(bMin, it.second.bLevel)
            it += 1
        return bMin

    def ComputeRolePoint(self, ch, bRole, bAdd):
        if not bAdd:
            ch.PointChange(EPointTypes.LG_POINT_PARTY_ATTACKER_BONUS, -ch.GetPoint(EPointTypes.LG_POINT_PARTY_ATTACKER_BONUS), DefineConstants.false, DefineConstants.false)
            ch.PointChange(EPointTypes.LG_POINT_PARTY_TANKER_BONUS, -ch.GetPoint(EPointTypes.LG_POINT_PARTY_TANKER_BONUS), DefineConstants.false, DefineConstants.false)
            ch.PointChange(EPointTypes.LG_POINT_PARTY_BUFFER_BONUS, -ch.GetPoint(EPointTypes.LG_POINT_PARTY_BUFFER_BONUS), DefineConstants.false, DefineConstants.false)
            ch.PointChange(EPointTypes.LG_POINT_PARTY_LG_SKILL_MASTER_BONUS, -ch.GetPoint(EPointTypes.LG_POINT_PARTY_LG_SKILL_MASTER_BONUS), DefineConstants.false, DefineConstants.false)
            ch.PointChange(EPointTypes.LG_POINT_PARTY_DEFENDER_BONUS, -ch.GetPoint(EPointTypes.LG_POINT_PARTY_DEFENDER_BONUS), DefineConstants.false, DefineConstants.false)
            ch.PointChange(EPointTypes.LG_POINT_PARTY_HASTE_BONUS, -ch.GetPoint(EPointTypes.LG_POINT_PARTY_HASTE_BONUS), DefineConstants.false, DefineConstants.false)
            ch.ComputeBattlePoints()
            return

        k = float(ch.GetSkillPowerByLevel(MIN(LGEMiscellaneous.LG_SKILL_MAX_LEVEL, self._m_iLeadership), DefineConstants.false))/ 100.0

        if bRole == EPartyRole.PARTY_ROLE_ATTACKER:
                iBonus = int((10 + 60 * k))

                if ch.GetPoint(EPointTypes.LG_POINT_PARTY_ATTACKER_BONUS) != iBonus:
                    ch.PointChange(EPointTypes.LG_POINT_PARTY_ATTACKER_BONUS, iBonus - ch.GetPoint(EPointTypes.LG_POINT_PARTY_ATTACKER_BONUS), DefineConstants.false, DefineConstants.false)
                    ch.ComputePoints()

        elif bRole == EPartyRole.PARTY_ROLE_TANKER:
                iBonus = int((50 + 1450 * k))

                if ch.GetPoint(EPointTypes.LG_POINT_PARTY_TANKER_BONUS) != iBonus:
                    ch.PointChange(EPointTypes.LG_POINT_PARTY_TANKER_BONUS, iBonus - ch.GetPoint(EPointTypes.LG_POINT_PARTY_TANKER_BONUS), DefineConstants.false, DefineConstants.false)
                    ch.ComputePoints()

        elif bRole == EPartyRole.PARTY_ROLE_BUFFER:
                iBonus = int((5 + 45 * k))

                if ch.GetPoint(EPointTypes.LG_POINT_PARTY_BUFFER_BONUS) != iBonus:
                    ch.PointChange(EPointTypes.LG_POINT_PARTY_BUFFER_BONUS, iBonus - ch.GetPoint(EPointTypes.LG_POINT_PARTY_BUFFER_BONUS), DefineConstants.false, DefineConstants.false)

        elif bRole == EPartyRole.PARTY_ROLE_LG_SKILL_MASTER:
                iBonus = int((25 + 600 * k))

                if ch.GetPoint(EPointTypes.LG_POINT_PARTY_LG_SKILL_MASTER_BONUS) != iBonus:
                    ch.PointChange(EPointTypes.LG_POINT_PARTY_LG_SKILL_MASTER_BONUS, iBonus - ch.GetPoint(EPointTypes.LG_POINT_PARTY_LG_SKILL_MASTER_BONUS), DefineConstants.false, DefineConstants.false)
                    ch.ComputePoints()
        elif bRole == EPartyRole.PARTY_ROLE_HASTE:
                iBonus = int((1+5 *k))
                if ch.GetPoint(EPointTypes.LG_POINT_PARTY_HASTE_BONUS) != iBonus:
                    ch.PointChange(EPointTypes.LG_POINT_PARTY_HASTE_BONUS, iBonus - ch.GetPoint(EPointTypes.LG_POINT_PARTY_HASTE_BONUS), DefineConstants.false, DefineConstants.false)
                    ch.ComputePoints()
        elif bRole == EPartyRole.PARTY_ROLE_DEFENDER:
                iBonus = int((5+30 *k))
                if ch.GetPoint(EPointTypes.LG_POINT_PARTY_DEFENDER_BONUS) != iBonus:
                    ch.PointChange(EPointTypes.LG_POINT_PARTY_DEFENDER_BONUS, iBonus - ch.GetPoint(EPointTypes.LG_POINT_PARTY_DEFENDER_BONUS), DefineConstants.false, DefineConstants.false)
                    ch.ComputePoints()

    def HealParty(self):
            return
        if not self._m_bPartyHealReady:
            return

        l = self.GetLeaderCharacter()

        it = m_memberMap.begin()
        while it is not self.m_memberMap.end():
            if not it.second.pCharacter:
                continue

            ch = it.second.pCharacter

            if Globals.DISTANCE_APPROX(l.GetX()-ch.GetX(), l.GetY()-ch.GetY()) < Globals.PARTY_DEFAULT_RANGE:
                ch.PointChange(EPointTypes.LG_POINT_HP, ch.GetMaxHP()-ch.GetHP(), DefineConstants.false, DefineConstants.false)
                ch.PointChange(EPointTypes.LG_POINT_SP, ch.GetMaxSP()-ch.GetSP(), DefineConstants.false, DefineConstants.false)
            it += 1

        self._m_bPartyHealReady = LGEMiscellaneous.DEFINECONSTANTS.false
        self._m_dwPartyHealTime = get_dword_time()

    def SummonToLeader(self, pid):
        xy = [[ 250, 0 ], [ 216, 125 ], [ 125, 216 ], [ 0, 250 ], [ -125, 216 ], [ -216, 125 ], [ -250, 0 ], [ -216, -125 ], [ -125, -216 ], [ 0, -250 ], [ 125, -216 ], [ 216, -125 ]]

        n = 0
        x = [0 for _ in range(12)]
        y = [0 for _ in range(12)]

        s = SECTREE_MANAGER.instance()
        l = self.GetLeaderCharacter()

        if pid not in self.m_memberMap.keys():
            l.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Group> The target was not found."))
            return

        ch = self.m_memberMap[pid].pCharacter

        if ch is None:
            l.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Group> The target was not found."))
            return

        if not ch.CanSummon(self._m_iLeadership):
            l.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Group> You cannot call the target."))
            return

        for i in range(0, 12):
            p = pixel_position_s()

            if s.GetMovablePosition(l.GetMapIndex(), l.GetX() + xy [i][0], l.GetY() + xy[i][1], p):
                x[n] = p.x
                y[n] = p.y
                n += 1

        if n == 0:
            l.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Group> You cannot call Group members to your current position."))
        else:
            i = number(0, n - 1)
            ch.Show(l.GetMapIndex(), x[i], y[i], LONG_MAX, DefineConstants.false)
            ch.Stop()

    def SetPCParty(self, b):
        self._m_bPCParty = b

    def GetNextOwnership(self, ch, x, y):
        if self.m_itNextOwner is self.m_memberMap.end():
            return ch

        size = len(self.m_memberMap)

## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: while (size-- > 0)
        while size > 0:
            size -= 1
            pkMember = self.m_itNextOwner.second.pCharacter

            if pkMember is not None and Globals.DISTANCE_APPROX(pkMember.GetX() - x, pkMember.GetY() - y) < 3000:
                self.IncreaseOwnership()
                return pkMember

            self.IncreaseOwnership()
        size -= 1

        return ch

    def SetFlag(self, name, value):
        it = self._m_map_iFlag.find(name)

        if it is self._m_map_iFlag.end():
            self._m_map_iFlag.update({name: value})
        elif it.second != value:
            it.second = value

    def GetFlag(self, name):
        it = self._m_map_iFlag.find(name)

        if it is not self._m_map_iFlag.end():
            return it.second
        return 0

    def SetDungeon(self, pDungeon):
        self._m_pkDungeon = pDungeon
        self._m_map_iFlag.clear()

    def GetDungeon(self):
        return self._m_pkDungeon

    def CountMemberByVnum(self, dwVnum):
        if self._m_bPCParty:
            return 0

        tch = None
        bCount = 0

        it = m_memberMap.begin()
        while it is not self.m_memberMap.end():
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if (!(tch = it->second.pCharacter))
            if not(tch = it.second.pCharacter):
                continue

            if tch.IsPC():
                continue

            if tch.GetMobTable().dwVnum == dwVnum:
                bCount += 1
            it += 1

        return bCount

    def SetParameter(self, iMode):
        if iMode >= EPartyExpDistributionModes.PARTY_EXP_DISTRIBUTION_MAX_NUM:
            #lani_err("Invalid exp distribution mode %d", iMode)
            return

        self._m_iExpDistributionMode = iMode
        self.SendParameterToAll()

    def GetExpDistributionMode(self):
        return self._m_iExpDistributionMode

    def SetExpCentralizeCharacter(self, dwPID):
        it = self.m_memberMap.find(dwPID)

        if it is self.m_memberMap.end():
            return

        self._m_pkChrExpCentralize = it.second.pCharacter

    def GetExpCentralizeCharacter(self):
        return self._m_pkChrExpCentralize

    def RequestSetMemberLevel(self, pid, level):
        p = SPacketPartySetMemberLevel()
        p.dwLeaderPID = self.GetLeaderPID()
        p.dwPID = pid
        p.bLevel = level
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        db_clientdesc.DBPacket(Globals.LG_HEADER_GD_PARTY_SET_MEMBER_LEVEL, 0, p, sizeof(SPacketPartySetMemberLevel))

    def P2PSetMemberLevel(self, pid, level):
        if not self._m_bPCParty:
            return

        it = TMemberMap.iterator()

        #sys_log(0, "PARTY P2PSetMemberLevel leader %d pid %d level %d", self.GetLeaderPID(), pid, level)

        it = self.m_memberMap.find(pid)
        if it is not self.m_memberMap.end():
            it.second.bLevel = level

    def IncreaseOwnership(self):
        if not self.m_memberMap:
            self.m_itNextOwner = self.m_memberMap.begin()
            return

        if self.m_itNextOwner is self.m_memberMap.end():
            self.m_itNextOwner = self.m_memberMap.begin()
        else:
            self.m_itNextOwner += 1

            if self.m_itNextOwner is self.m_memberMap.end():
                self.m_itNextOwner = self.m_memberMap.begin()

    def Initialize(self):
        #sys_log(2, "Party::Initialize")

        self._m_iExpDistributionMode = EPartyExpDistributionModes.PARTY_EXP_DISTRIBUTION_NON_PARITY
        self._m_pkChrExpCentralize = None

        self.m_dwLeaderPID = 0

        self.m_eventUpdate = None

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memset(self._m_anRoleCount, 0, sizeof(self._m_anRoleCount))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memset(self._m_anMaxRole, 0, sizeof(self._m_anMaxRole))
        self._m_anMaxRole[(int)EPartyRole.PARTY_ROLE_LEADER] = 1
        self._m_anMaxRole[(int)EPartyRole.PARTY_ROLE_NORMAL] = 32

        self._m_dwPartyStartTime = get_dword_time()
        self._m_iLongTimeExpBonus = 0

        self._m_dwPartyHealTime = get_dword_time()
        self._m_bPartyHealReady = LGEMiscellaneous.DEFINECONSTANTS.false
        self._m_bCanUsePartyHeal = LGEMiscellaneous.DEFINECONSTANTS.false

        self._m_iLeadership = 0
        self._m_iExpBonus = 0
        self._m_iAttBonus = 0
        self._m_iDefBonus = 0

        self.m_itNextOwner = self.m_memberMap.begin()

        self._m_iCountNearPartyMember = 0

        self.m_pkChrLeader = None
        self._m_bPCParty = LGEMiscellaneous.DEFINECONSTANTS.false
        self._m_pkDungeon = None
        self._m_pkDungeon_for_Only_party = None

    def Destroy(self):
        #sys_log(2, "Party::Destroy")

        if self._m_bPCParty:
            it = m_memberMap.begin()
            while it is not self.m_memberMap.end():
                CPartyManager.instance().SetPartyMember(it.first, None)
                it += 1

        event_cancel(self.m_eventUpdate)

        self.RemoveBonus()

        it = self.m_memberMap.begin()

        dwTime = get_dword_time()

        while it is not self.m_memberMap.end():
            rMember = it.second
            it += 1

            if rMember.pCharacter:
                if rMember.pCharacter.GetDesc():
                    p = packet_party_remove()
                    p.header = byte(Globals.LG_HEADER_GC_PARTY_REMOVE)
                    p.pid = rMember.pCharacter.GetPlayerID()
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                    rMember.pCharacter.GetDesc().Packet(p, sizeof(p))
                    rMember.pCharacter.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Group> The Group is deleted."))
                else:
                    rMember.pCharacter.SetLastAttacked(dwTime)
                    rMember.pCharacter.StartDestroyWhenIdleEvent()

                rMember.pCharacter.SetParty(None)

        self.m_memberMap.clear()
        self.m_itNextOwner = self.m_memberMap.begin()

        if self._m_pkDungeon_for_Only_party is not None:
            self._m_pkDungeon_for_Only_party.SetPartyNull()
            self._m_pkDungeon_for_Only_party = None

# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    RemovePartyBonus()

    def RemoveBonus(self):
        it = m_memberMap.begin()
        while it is not self.m_memberMap.end():
            ch = None

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((ch = it->second.pCharacter))
            if (ch = it.second.pCharacter):
                self.ComputeRolePoint(ch, it.second.bRole, LGEMiscellaneous.DEFINECONSTANTS.false)

            it.second.bNear = LGEMiscellaneous.DEFINECONSTANTS.false
            it += 1

    def RemoveBonusForOne(self, pid):
        it = self.m_memberMap.find(pid)

        if it is self.m_memberMap.end():
            return

        ch = None

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((ch = it->second.pCharacter))
        if (ch = it.second.pCharacter):
            self.ComputeRolePoint(ch, it.second.bRole, LGEMiscellaneous.DEFINECONSTANTS.false)

    def SendParameter(self, ch):
        p = paryt_parameter()

        p.bHeader = byte(Globals.LG_HEADER_GC_PARTY_PARAMETER)
        p.bDistributeMode = byte(self._m_iExpDistributionMode)

        d = ch.GetDesc()

        if d:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            d.Packet(p, sizeof(paryt_parameter))

    def SendParameterToAll(self):
        if not self._m_bPCParty:
            return

        it = m_memberMap.begin()
        while it is not self.m_memberMap.end():
            if it.second.pCharacter:
                self.SendParameter(it.second.pCharacter)
            it += 1













    def SetDungeon_for_Only_party(self, pDungeon):
        self._m_pkDungeon_for_Only_party = pDungeon

    def GetDungeon_for_Only_party(self):
        return self._m_pkDungeon_for_Only_party

class party_update_event_info(event_info_data):

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.pid = 0

        self.pid = 0

## Laniatus Games Studio Inc. | NOTE: Anonymous namespaces are not defined:
#namespace
class FExitDungeon:
    def functor_method(self, ch):
        ch.ExitToSavedLocation()
