## Laniatus Games Studio Inc. | NOTE: Python has no need of forward class declarations:
#class CHARACTER

class CPVP:

    def _initialize_instance_fields(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.m_players = [_player() for _ in range(2)]
        self.m_dwCRC = 0
        self.m_bRevenge = False
        self.m_dwLastFightTime = 0

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python has no concept of a 'friend' class:
#    friend class CPVPManager

    class _player:

        def __init__(self):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.dwPID = 0
            self.dwVID = 0
            self.bAgree = False
            self.bCanRevenge = False

            self.dwPID = 0
            self.dwVID = 0
            self.bAgree = LGEMiscellaneous.DEFINECONSTANTS.false
            self.bCanRevenge = LGEMiscellaneous.DEFINECONSTANTS.false

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to multiple constructors:
#ORIGINAL METINII C CODE: CPVP(uint dwPID1, uint dwPID2)
    def __init__(self, dwPID1, dwPID2):
        self._initialize_instance_fields()

        if dwPID1 > dwPID2:
            self.m_players[0].dwPID = dwPID1
            self.m_players[1].dwPID = dwPID2
            self.m_players[0].bAgree = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
        else:
            self.m_players[0].dwPID = dwPID2
            self.m_players[1].dwPID = dwPID1
            self.m_players[1].bAgree = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        adwID = [0 for _ in range(2)]
        adwID[0] = self.m_players[0].dwPID
        adwID[1] = self.m_players[1].dwPID
        self.m_dwCRC = GetFastHash(str(adwID), 8)
        self.m_bRevenge = LGEMiscellaneous.DEFINECONSTANTS.false

        self.SetLastFightTime()

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to multiple constructors:
#ORIGINAL METINII C CODE: CPVP(CPVP & k)
    def __init__(self, k):
        self._initialize_instance_fields()

## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: m_players[0] = k.m_players[0];
        self.m_players[0].copy_from(k.m_players[0])
## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: m_players[1] = k.m_players[1];
        self.m_players[1].copy_from(k.m_players[1])

        self.m_dwCRC = k.m_dwCRC
        self.m_bRevenge = k.m_bRevenge

        self.SetLastFightTime()

    def close(self):
        pass

    def Win(self, dwPID):
        iSlot = 1 if self.m_players[0].dwPID != dwPID else 0

        self.m_bRevenge = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        self.m_players[iSlot].bAgree = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
        self.m_players[(not iSlot)].bCanRevenge = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
        self.m_players[(not iSlot)].bAgree = LGEMiscellaneous.DEFINECONSTANTS.false

        self.Packet(DefineConstants.false)

    def CanRevenge(self, dwPID):
        return self.m_players[1 if self.m_players[0].dwPID != dwPID else 0].bCanRevenge

    def IsFight(self):
        return (self.m_players[0].bAgree == self.m_players[1].bAgree) and self.m_players[0].bAgree

    def Agree(self, dwPID):
        self.m_players[1 if self.m_players[0].dwPID != dwPID else 0].bAgree = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        if self.IsFight():
            self.Packet(DefineConstants.false)
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        return LGEMiscellaneous.DEFINECONSTANTS.false

    def SetVID(self, dwPID, dwVID):
        if self.m_players[0].dwPID == dwPID:
            self.m_players[0].dwVID = dwVID
        else:
            self.m_players[1].dwVID = dwVID

    def Packet(self, bDelete = LGEMiscellaneous.DefineConstants.false):
        if (self.m_players[0].dwVID) == 0 or (self.m_players[1].dwVID) == 0:
            if bDelete:
                #lani_err("null vid when removing %u %u", self.m_players[0].dwVID, self.m_players[0].dwVID)

            return

        pack = packet_pvp()

        pack.bHeader = byte(Globals.LG_HEADER_GC_PVP)

        if bDelete:
            pack.bMode = EPVPModes.PVP_MODE_NONE
            pack.dwVIDSrc = self.m_players[0].dwVID
            pack.dwVIDDst = self.m_players[1].dwVID
        elif self.IsFight():
            pack.bMode = EPVPModes.PVP_MODE_FIGHT
            pack.dwVIDSrc = self.m_players[0].dwVID
            pack.dwVIDDst = self.m_players[1].dwVID
        else:
            pack.bMode = EPVPModes.PVP_MODE_REVENGE if self.m_bRevenge else EPVPModes.PVP_MODE_AGREE

            if self.m_players[0].bAgree:
                pack.dwVIDSrc = self.m_players[0].dwVID
                pack.dwVIDDst = self.m_players[1].dwVID
            else:
                pack.dwVIDSrc = self.m_players[1].dwVID
                pack.dwVIDDst = self.m_players[0].dwVID

        c_rSet = DESC_MANAGER.instance().GetClientSet()
        it = c_rSet.begin()

        while it is not c_rSet.end():
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: DESC* d = *it++;
            d = *it
            it += 1

            if d.IsPhase(EPhase.PHASE_GAME) or d.IsPhase(EPhase.PHASE_DEAD):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                d.Packet(pack, sizeof(pack))

    def SetLastFightTime(self):
        self.m_dwLastFightTime = get_dword_time()

    def GetLastFightTime(self):
        return self.m_dwLastFightTime

    def GetCRC(self):
        return self.m_dwCRC


class CPVPManager(singleton):

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.m_map_pkPVP = {}
        self.m_map_pkPVPSetByID = {}


    def close(self):
        pass

    def Insert(self, pkChr, pkVictim):
        if pkChr.IsDead() or pkVictim.IsDead():
            return

        kPVP = CPVP(pkChr.GetPlayerID(), pkVictim.GetPlayerID())

        pkPVP = None

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((pkPVP = Find(kPVP.m_dwCRC)))
        if (pkPVP = self.Find(kPVP.m_dwCRC)):
            if pkPVP.Agree(pkChr.GetPlayerID()):
                pkVictim.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("The duel with %s has begin!"), pkChr.GetName(LOCALE_LANIATUS))
                pkChr.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("The duel with %s has begin!"), pkVictim.GetName(LOCALE_LANIATUS))
            return

        pkPVP = LG_NEW_M2 CPVP(kPVP)

        pkPVP.SetVID(pkChr.GetPlayerID(), pkChr.GetVID())
        pkPVP.SetVID(pkVictim.GetPlayerID(), pkVictim.GetVID())

        self.m_map_pkPVP.insert(dict.value_type(pkPVP.m_dwCRC, pkPVP))

        self.m_map_pkPVPSetByID[pkChr.GetPlayerID()].insert(pkPVP)
        self.m_map_pkPVPSetByID[pkVictim.GetPlayerID()].insert(pkPVP)

        pkPVP.Packet(DefineConstants.false)

        msg = str(['\0' for _ in range((int)LGEMiscellaneous.CHAT_MAX_LEN + 1)])
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if __MULTI_LANGUAGE_SYSTEM__
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        snprintf(msg, sizeof(msg), LC_LOCALE_TEXT("%s challenged you for a duel!", pkVictim.GetDesc().GetLanguage()), pkChr.GetName(LOCALE_LANIATUS))
##else
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        snprintf(msg, sizeof(msg), LC_TEXT("%s challenged you for a duel!"), pkChr.GetName(LOCALE_LANIATUS))
##endif

        pkVictim.ChatPacket(EChatType.CHAT_TYPE_INFO, msg)
        pkChr.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You challenged %s for a duel."), pkVictim.GetName(LOCALE_LANIATUS))

        pkVictimDesc = pkVictim.GetDesc()
        if pkVictimDesc:
            pack = packet_whisper()

            len = MIN(LGEMiscellaneous.CHAT_MAX_LEN, len(msg) + 1)

            pack.bHeader = byte(Globals.LG_HEADER_GC_WHISPER)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            pack.wSize = sizeof(packet_whisper) + len
            pack.bType = EWhisperType.WHISPER_TYPE_SYSTEM
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            strncpy_s(pack.szNameFrom, sizeof(pack.szNameFrom), pkChr.GetName(LOCALE_LANIATUS), _TRUNCATE)

            buf = TEMP_BUFFER(8192, DefineConstants.false)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            buf.write(pack, sizeof(packet_whisper))
            buf.write(msg, len)

            pkVictimDesc.Packet(buf.read_peek(), buf.size())

    def CanAttack(self, pkChr, pkVictim):
        if (pkVictim.GetCharType() == ECharType.CHAR_TYPE_NPC) or (pkVictim.GetCharType() == ECharType.CHAR_TYPE_WARP) or (pkVictim.GetCharType() == ECharType.CHAR_TYPE_GOTO) or (pkVictim.GetCharType() == ECharType.CHAR_TYPE_MOUNT) or (pkVictim.GetCharType() == ECharType.CHAR_TYPE_PET):
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if pkChr is pkVictim:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if pkVictim.IsNPC() and pkChr.IsNPC() and not pkChr.IsGuardNPC():
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if ((not LGEMiscellaneous.DEFINECONSTANTS.false)) == pkChr.IsHorseRiding():
            if pkChr.GetHorseLevel() > 0 and 1 == pkChr.GetHorseGrade() and pkChr.GetMountVnum() >= 20101 and pkChr.GetMountVnum() <= 20103:
                return LGEMiscellaneous.DEFINECONSTANTS.false
        else:
            if (pkChr.GetMountVnum() == 0) or (pkChr.GetMountVnum() == 20030) or (pkChr.GetMountVnum() == 20110) or (pkChr.GetMountVnum() == 20111) or (pkChr.GetMountVnum() == 20112) or (pkChr.GetMountVnum() == 20113) or (pkChr.GetMountVnum() == 20114) or (pkChr.GetMountVnum() == 20115) or (pkChr.GetMountVnum() == 20116) or (pkChr.GetMountVnum() == 20117) or (pkChr.GetMountVnum() == 20118) or (pkChr.GetMountVnum() == 20205) or (pkChr.GetMountVnum() == 20206) or (pkChr.GetMountVnum() == 20207) or (pkChr.GetMountVnum() == 20208) or (pkChr.GetMountVnum() == 20209) or (pkChr.GetMountVnum() == 20210) or (pkChr.GetMountVnum() == 20211) or (pkChr.GetMountVnum() == 20212) or (pkChr.GetMountVnum() == 20119) or (pkChr.GetMountVnum() == 20219) or (pkChr.GetMountVnum() == 20220) or (pkChr.GetMountVnum() == 20221) or (pkChr.GetMountVnum() == 20222) or (pkChr.GetMountVnum() == 20120) or (pkChr.GetMountVnum() == 20121) or (pkChr.GetMountVnum() == 20122) or (pkChr.GetMountVnum() == 20123) or (pkChr.GetMountVnum() == 20124) or (pkChr.GetMountVnum() == 20125) or (pkChr.GetMountVnum() == 20214) or (pkChr.GetMountVnum() == 20215) or (pkChr.GetMountVnum() == 20217) or (pkChr.GetMountVnum() == 20218) or (pkChr.GetMountVnum() == 20223) or (pkChr.GetMountVnum() == 20224) or (pkChr.GetMountVnum() == 20225) or (pkChr.GetMountVnum() == 20226) or (pkChr.GetMountVnum() == 20227) or (pkChr.GetMountVnum() == 20228) or (pkChr.GetMountVnum() == 20229) or (pkChr.GetMountVnum() == 20230) or (pkChr.GetMountVnum() == 20231) or (pkChr.GetMountVnum() == 20232) or (pkChr.GetMountVnum() == 20233) or (pkChr.GetMountVnum() == 20234) or (pkChr.GetMountVnum() == 20235) or (pkChr.GetMountVnum() == 20236) or (pkChr.GetMountVnum() == 20237) or (pkChr.GetMountVnum() == 20238) or (pkChr.GetMountVnum() == 20239) or (pkChr.GetMountVnum() == 20240) or (pkChr.GetMountVnum() == 20241) or (pkChr.GetMountVnum() == 20242) or (pkChr.GetMountVnum() == 20243) or (pkChr.GetMountVnum() == 20244) or (pkChr.GetMountVnum() == 20245) or (pkChr.GetMountVnum() == 20246) or (pkChr.GetMountVnum() == 20247) or (pkChr.GetMountVnum() == 20248) or (pkChr.GetMountVnum() == 20249) or (pkChr.GetMountVnum() == 20250) or (pkChr.GetMountVnum() == 20251) or (pkChr.GetMountVnum() == 20252) or (pkChr.GetMountVnum() == 20253) or (pkChr.GetMountVnum() == 20254) or (pkChr.GetMountVnum() == 20255) or (pkChr.GetMountVnum() == 20256) or (pkChr.GetMountVnum() == 20257) or (pkChr.GetMountVnum() == 20258) or (pkChr.GetMountVnum() == 20259) or (pkChr.GetMountVnum() == 20260) or (pkChr.GetMountVnum() == 20261) or (pkChr.GetMountVnum() == 20262):
                pass

            else:
                return LGEMiscellaneous.DEFINECONSTANTS.false

        if pkVictim.IsNPC() or pkChr.IsNPC():
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        if pkVictim.IsObserverMode() or pkChr.IsObserverMode():
            return LGEMiscellaneous.DEFINECONSTANTS.false

            bMapEmpire = SECTREE_MANAGER.instance().GetEmpireFromMapIndex(pkChr.GetMapIndex())

            if pkChr.GetPKMode() == EPKModes.PK_MODE_PROTECT and pkChr.GetEmpire() == bMapEmpire or pkVictim.GetPKMode() == EPKModes.PK_MODE_PROTECT and pkVictim.GetEmpire() == bMapEmpire:
                return LGEMiscellaneous.DEFINECONSTANTS.false

        if pkChr.GetEmpire() != pkVictim.GetEmpire():
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        beKillerMode = LGEMiscellaneous.DEFINECONSTANTS.false

        if pkVictim.GetParty() is not None and pkVictim.GetParty() is pkChr.GetParty():
            return LGEMiscellaneous.DEFINECONSTANTS.false
        else:
            if pkVictim.IsKillerMode():
                return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

            if pkChr.GetAlignment() < 0 and pkVictim.GetAlignment() >= 0:
                if g_protectNormalPlayer:
                    if EPKModes.PK_MODE_PEACE == pkVictim.GetPKMode():
                        return LGEMiscellaneous.DEFINECONSTANTS.false


            if (pkChr.GetPKMode() == EPKModes.PK_MODE_PEACE) or (pkChr.GetPKMode() == EPKModes.PK_MODE_REVENGE):
                if pkVictim.GetGuild() is not None and pkVictim.GetGuild() is pkChr.GetGuild():
                    break

                if pkChr.GetPKMode() == EPKModes.PK_MODE_REVENGE:
                    if pkChr.GetAlignment() < 0 and pkVictim.GetAlignment() >= 0:
                        pkChr.SetKillerMode(((not LGEMiscellaneous.DEFINECONSTANTS.false)))
                        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
                    elif pkChr.GetAlignment() >= 0 and pkVictim.GetAlignment() < 0:
                        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

            elif pkChr.GetPKMode() == EPKModes.PK_MODE_GUILD:
                if pkChr.GetGuild() is None or (pkVictim.GetGuild() is not pkChr.GetGuild()):
                    if pkVictim.GetAlignment() >= 0:
                        pkChr.SetKillerMode(((not LGEMiscellaneous.DEFINECONSTANTS.false)))
                    elif pkChr.GetAlignment() < 0 and pkVictim.GetAlignment() < 0:
                        pkChr.SetKillerMode(((not LGEMiscellaneous.DEFINECONSTANTS.false)))

                    return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

            elif pkChr.GetPKMode() == EPKModes.PK_MODE_FREE:
                if pkVictim.GetAlignment() >= 0:
                    pkChr.SetKillerMode(((not LGEMiscellaneous.DEFINECONSTANTS.false)))
                elif pkChr.GetAlignment() < 0 and pkVictim.GetAlignment() < 0:
                    pkChr.SetKillerMode(((not LGEMiscellaneous.DEFINECONSTANTS.false)))
                return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        kPVP = CPVP(pkChr.GetPlayerID(), pkVictim.GetPlayerID())
        pkPVP = self.Find(kPVP.m_dwCRC)

        if pkPVP is None or not pkPVP.IsFight():
            if beKillerMode:
                pkChr.SetKillerMode(((not LGEMiscellaneous.DEFINECONSTANTS.false)))

            return (beKillerMode)

        pkPVP.SetLastFightTime()
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def Dead(self, pkChr, dwKillerPID):
        it = self.m_map_pkPVPSetByID.find(pkChr.GetPlayerID())

        if it is self.m_map_pkPVPSetByID.end():
            return LGEMiscellaneous.DEFINECONSTANTS.false

        found = LGEMiscellaneous.DEFINECONSTANTS.false

        #sys_log(1, "PVPManager::Dead %d", pkChr.GetPlayerID())
        it2 = it.second.begin()

        while it2 is not it.second.end():
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: CPVP * pkPVP = *it2++;
            pkPVP = *it2
            it2 += 1

            dwCompanionPID = None

            if pkPVP.m_players[0].dwPID == pkChr.GetPlayerID():
                dwCompanionPID = pkPVP.m_players[1].dwPID
            else:
                dwCompanionPID = pkPVP.m_players[0].dwPID

            if dwCompanionPID == dwKillerPID:
                if pkPVP.IsFight():
                    pkPVP.SetLastFightTime()
                    pkPVP.Win(dwKillerPID)
                    found = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
                    break
                elif get_dword_time() - pkPVP.GetLastFightTime() <= 15000:
                    found = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
                    break

        return found

    def GiveUp(self, pkChr, dwKillerPID):
        it = self.m_map_pkPVPSetByID.find(pkChr.GetPlayerID())

        if it is self.m_map_pkPVPSetByID.end():
            return

        #sys_log(1, "PVPManager::Dead %d", pkChr.GetPlayerID())
        it2 = it.second.begin()

        while it2 is not it.second.end():
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: CPVP * pkPVP = *it2++;
            pkPVP = *it2
            it2 += 1

            dwCompanionPID = None

            if pkPVP.m_players[0].dwPID == pkChr.GetPlayerID():
                dwCompanionPID = pkPVP.m_players[1].dwPID
            else:
                dwCompanionPID = pkPVP.m_players[0].dwPID

            if dwCompanionPID != dwKillerPID:
                continue

            pkPVP.SetVID(pkChr.GetPlayerID(), 0)

            self.m_map_pkPVPSetByID.pop(dwCompanionPID)

            it.second.erase(pkPVP)

            if it.second.empty():
                self.m_map_pkPVPSetByID.pop(it)

            self.m_map_pkPVP.pop(pkPVP.m_dwCRC)

            pkPVP.Packet(((not LGEMiscellaneous.DEFINECONSTANTS.false)))
            LG_DEL_MEM(pkPVP)
            break

    def Connect(self, pkChr):
        self.ConnectEx(pkChr, LGEMiscellaneous.DEFINECONSTANTS.false)

    def Disconnect(self, pkChr):
        pass

    def SendList(self, d):
        it = self.m_map_pkPVP.begin()

        dwVID = d.GetCharacter().GetVID()

        pack = packet_pvp()

        pack.bHeader = byte(Globals.LG_HEADER_GC_PVP)

        while it is not self.m_map_pkPVP.end():
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: CPVP * pkPVP = (it++)->second;
            pkPVP = (it).second
            it += 1

            if (pkPVP.m_players[0].dwVID) == 0 or (pkPVP.m_players[1].dwVID) == 0:
                continue

            if pkPVP.IsFight():
                pack.bMode = EPVPModes.PVP_MODE_FIGHT
                pack.dwVIDSrc = pkPVP.m_players[0].dwVID
                pack.dwVIDDst = pkPVP.m_players[1].dwVID
            else:
                pack.bMode = EPVPModes.PVP_MODE_REVENGE if pkPVP.m_bRevenge else EPVPModes.PVP_MODE_AGREE

                if pkPVP.m_players[0].bAgree:
                    pack.dwVIDSrc = pkPVP.m_players[0].dwVID
                    pack.dwVIDDst = pkPVP.m_players[1].dwVID
                else:
                    pack.dwVIDSrc = pkPVP.m_players[1].dwVID
                    pack.dwVIDDst = pkPVP.m_players[0].dwVID

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            d.Packet(pack, sizeof(pack))
            #sys_log(1, "PVPManager::SendList %d %d", pack.dwVIDSrc, pack.dwVIDDst)

            if pkPVP.m_players[0].dwVID == dwVID:
                ch = CHARACTER_MANAGER.instance().Find(pkPVP.m_players[1].dwVID)
                if ch is not None and ch.GetDesc() is not None:
                    d = ch.GetDesc()
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                    d.Packet(pack, sizeof(pack))
            elif pkPVP.m_players[1].dwVID == dwVID:
                ch = CHARACTER_MANAGER.instance().Find(pkPVP.m_players[0].dwVID)
                if ch is not None and ch.GetDesc() is not None:
                    d = ch.GetDesc()
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                    d.Packet(pack, sizeof(pack))

    def Delete(self, pkPVP):
        it = self.m_map_pkPVP.find(pkPVP.m_dwCRC)

        if it is self.m_map_pkPVP.end():
            return

        self.m_map_pkPVP.pop(it)
        self.m_map_pkPVPSetByID[pkPVP.m_players[0].dwPID].erase(pkPVP)
        self.m_map_pkPVPSetByID[pkPVP.m_players[1].dwPID].erase(pkPVP)

        LG_DEL_MEM(pkPVP)

    def Process(self):
        it = self.m_map_pkPVP.begin()

        while it is not self.m_map_pkPVP.end():
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: CPVP * pvp = (it++)->second;
            pvp = (it).second
            it += 1

            if get_dword_time() - pvp.GetLastFightTime() > 600000:
                pvp.Packet(((not LGEMiscellaneous.DEFINECONSTANTS.false)))
                self.Delete(pvp)

    def Find(self, dwCRC):
        it = self.m_map_pkPVP.find(dwCRC)

        if it is self.m_map_pkPVP.end():
            return None

        return it.second

    def ConnectEx(self, pkChr, bDisconnect):
        it = self.m_map_pkPVPSetByID.find(pkChr.GetPlayerID())

        if it is self.m_map_pkPVPSetByID.end():
            return

        dwVID = uint(0 if bDisconnect else pkChr.GetVID())

        it2 = it.second.begin()

        while it2 is not it.second.end():
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: CPVP * pkPVP = *it2++;
            pkPVP = *it2
            it2 += 1
            pkPVP.SetVID(pkChr.GetPlayerID(), dwVID)




