from enum import Enum
import math

class EWarMapTypes(Enum):
    WAR_MAP_TYPE_NORMAL = 0
    WAR_MAP_TYPE_FLAG = 1

class SWarMapInfo:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.bType = 0
        self.lMapIndex = 0
        self.posStart = [pixel_position_s() for _ in range(3)]


class warmap: #this class replaces the original namespace 'warmap'
    WAR_FLAG_VNUM_START = 20035
    WAR_FLAG_VNUM_END = 20037
    WAR_FLAG_VNUM0 = 20035
    WAR_FLAG_VNUM1 = 20036
    WAR_FLAG_VNUM2 = 20037
    WAR_FLAG_BASE_VNUM = 20038

    @staticmethod
    def IsWarFlag(dwVnum):
        if dwVnum >= warmap.WAR_FLAG_VNUM_START and dwVnum <= warmap.WAR_FLAG_VNUM_END:
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        return LGEMiscellaneous.DEFINECONSTANTS.false

    @staticmethod
    def IsWarFlagBase(dwVnum):
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false)) if dwVnum == warmap.WAR_FLAG_BASE_VNUM else LGEMiscellaneous.DEFINECONSTANTS.false

class CWarMap:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python has no concept of a 'friend' class:
#    friend class CGuild

    def __init__(self, lMapIndex, r_info, pkWarMapInfo, dwGuildID1, dwGuildID2):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self._m_kMapInfo = SWarMapInfo()
        self._m_bEnded = False
        self._m_pkBeginEvent = _boost_func_of_void.intrusive_ptr()
        self._m_pkTimeoutEvent = _boost_func_of_void.intrusive_ptr()
        self._m_pkEndEvent = _boost_func_of_void.intrusive_ptr()
        self._m_pkResetFlagEvent = _boost_func_of_void.intrusive_ptr()
        self._m_TeamData = [STeamData() for _ in range(2)]
        self._m_iObserverCount = 0
        self._m_dwStartTime = 0
        self._m_bTimeout = 0
        self._m_WarInfo = TGuildWarInfo()
        self._m_set_pkChr = boost.unordered_set()

## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: m_kMapInfo = *pkWarMapInfo;
        self._m_kMapInfo.copy_from(pkWarMapInfo)
        self._m_kMapInfo.lMapIndex = lMapIndex

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memcpy' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memcpy(self._m_WarInfo, r_info, sizeof(TGuildWarInfo))

        self._m_TeamData[0].Initialize()
        self._m_TeamData[0].dwID = dwGuildID1
        self._m_TeamData[0].pkGuild = CGuildManager.instance().TouchGuild(dwGuildID1)

        self._m_TeamData[1].Initialize()
        self._m_TeamData[1].dwID = dwGuildID2
        self._m_TeamData[1].pkGuild = CGuildManager.instance().TouchGuild(dwGuildID2)
        self._m_iObserverCount = 0

        info = Globals.AllocEventInfo()
        info.pWarMap = self

        self.SetBeginEvent(event_create_ex(war_begin_event, info, ((60) * passes_per_sec)))
        self._m_pkEndEvent = None
        self._m_pkTimeoutEvent = None
        self._m_pkResetFlagEvent = None
        self._m_bTimeout = LGEMiscellaneous.DEFINECONSTANTS.false
        self._m_dwStartTime = get_dword_time()
        self._m_bEnded = LGEMiscellaneous.DEFINECONSTANTS.false

        if self.GetType() == EWarMapTypes.WAR_MAP_TYPE_FLAG:
            self.AddFlagBase(0, 0, 0)
            self.AddFlagBase(1, 0, 0)
            self.AddFlag(0, 0, 0)
            self.AddFlag(1, 0, 0)

    def close(self):
        event_cancel(self._m_pkBeginEvent)
        event_cancel(self._m_pkEndEvent)
        event_cancel(self._m_pkTimeoutEvent)
        event_cancel(self._m_pkResetFlagEvent)

        #sys_log(0, "WarMap::~WarMap : map index %d", self.GetMapIndex())

        it = self._m_set_pkChr.begin()

        while it is not self._m_set_pkChr.end():
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: CHARACTER* ch = *(it++);
            ch = *(it)
            it += 1

            if ch.GetDesc():
                #sys_log(0, "WarMap::~WarMap : disconnecting %s", ch.GetName(LOCALE_LANIATUS))
                DESC_MANAGER.instance().DestroyDesc(ch.GetDesc(), ((not DefineConstants.false)))

        self._m_set_pkChr.clear()

    def GetTeamIndex(self, dwGuildID, bIdx):
        if self._m_TeamData[0].dwID == dwGuildID:
            bIdx.arg_value = 0
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
        elif self._m_TeamData[1].dwID == dwGuildID:
            bIdx.arg_value = 1
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        return LGEMiscellaneous.DEFINECONSTANTS.false

    def IncMember(self, ch):
        if not ch.IsPC():
            return

        #sys_log(0, "WarMap::IncMember")
        gid = 0

        if ch.GetGuild():
            gid = ch.GetGuild().GetID()

        isWarMember = ((not LGEMiscellaneous.DEFINECONSTANTS.false)) if ch.GetQuestFlag("war.is_war_member") > 0 else LGEMiscellaneous.DEFINECONSTANTS.false

        if isWarMember and gid != self._m_TeamData[0].dwID and gid != self._m_TeamData[1].dwID:
            ch.SetQuestFlag("war.is_war_member", 0)
            isWarMember = LGEMiscellaneous.DEFINECONSTANTS.false

        if isWarMember:
            if gid == self._m_TeamData[0].dwID:
                self._m_TeamData[0].AppendMember(ch)

            elif gid == self._m_TeamData[1].dwID:
                self._m_TeamData[1].AppendMember(ch)


            event_cancel(self._m_pkTimeoutEvent)

            #sys_log(0, "WarMap +m %u(cur:%d, acc:%d) vs %u(cur:%d, acc:%d)", self._m_TeamData[0].dwID, self._m_TeamData[0].GetCurJointerCount(), self._m_TeamData[0].GetAccumulatedJoinerCount(), self._m_TeamData[1].dwID, self._m_TeamData[1].GetCurJointerCount(), self._m_TeamData[1].GetAccumulatedJoinerCount())
        else:
            self._m_iObserverCount += 1
            #sys_log(0, "WarMap +o %d", self._m_iObserverCount)
            ch.SetObserverMode(((not LGEMiscellaneous.DEFINECONSTANTS.false)))
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You can participate in the Guild Battle in Viewer Mode"))
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Click the <End observer mode> icon to leave this war."))

        self._UpdateUserCount()

        self._m_set_pkChr.insert(ch)

        d = ch.GetDesc()

        self.SendWarPacket(d)
        self.SendScorePacket(0, d)
        self.SendScorePacket(1, d)

    def DecMember(self, ch):
        if not ch.IsPC():
            return

        #sys_log(0, "WarMap::DecMember")
        gid = 0

        if ch.GetGuild():
            gid = ch.GetGuild().GetID()

        if not ch.IsObserverMode():
            if gid == self._m_TeamData[0].dwID:
                self._m_TeamData[0].RemoveMember(ch)
            elif gid == self._m_TeamData[1].dwID:
                self._m_TeamData[1].RemoveMember(ch)

            if self._m_kMapInfo.bType == EWarMapTypes.WAR_MAP_TYPE_FLAG:
                pkAff = ch.FindAffect(LaniatusEAffectTypes.LANIA_AFFECT_WAR_FLAG, APPLY_NONE)

                if pkAff:
                    idx = None

                    temp_ref_idx = RefObject(idx);
                    if self.GetTeamIndex(uint(pkAff.lApplyValue), temp_ref_idx):
                        idx = temp_ref_idx.arg_value
                        self.AddFlag(idx, uint(ch.GetX()), uint(ch.GetY()))
                    else:
                        idx = temp_ref_idx.arg_value

                    ch.RemoveAffect(LaniatusEAffectTypes.LANIA_AFFECT_WAR_FLAG)

            #sys_log(0, "WarMap -m %u(cur:%d, acc:%d) vs %u(cur:%d, acc:%d)", self._m_TeamData[0].dwID, self._m_TeamData[0].GetCurJointerCount(), self._m_TeamData[0].GetAccumulatedJoinerCount(), self._m_TeamData[1].dwID, self._m_TeamData[1].GetCurJointerCount(), self._m_TeamData[1].GetAccumulatedJoinerCount())

            self.CheckWarEnd()
            ch.SetQuestFlag("war.is_war_member", 0)
        else:
            self._m_iObserverCount -= 1

            #sys_log(0, "WarMap -o %d", self._m_iObserverCount)
            ch.SetObserverMode(LGEMiscellaneous.DEFINECONSTANTS.false)

        self._UpdateUserCount()

        self._m_set_pkChr.erase(ch)

    def GetGuild(self, bIdx):
        return self._m_TeamData[bIdx].pkGuild

    def GetGuildID(self, bIdx):
        assert bIdx < 2
        return self._m_TeamData[bIdx].dwID

    def GetType(self):
        return self._m_kMapInfo.bType

    def GetMapIndex(self):
        return self._m_kMapInfo.lMapIndex

    def GetGuildOpponent(self, ch):
        if ch.GetGuild():
            gid = ch.GetGuild().GetID()
            idx = None

            temp_ref_idx = RefObject(idx);
            if self.GetTeamIndex(gid, temp_ref_idx):
                idx = temp_ref_idx.arg_value
                return self._m_TeamData[(not idx)].dwID
            else:
                idx = temp_ref_idx.arg_value
        return 0

    def GetWinnerGuild(self):
        win_gid = 0

        if self._m_TeamData[1].iScore > self._m_TeamData[0].iScore:
            win_gid = self._m_TeamData[1].dwID
        elif self._m_TeamData[0].iScore > self._m_TeamData[1].iScore:
            win_gid = self._m_TeamData[0].dwID

        return (win_gid)

    def UsePotion(self, ch, item):
        if self._m_pkEndEvent:
            return

        if ch.IsObserverMode():
            return

        if ch.GetGuild() is None:
            return

        if item.GetProto() is None:
            return

        iPrice = item.GetProto().lldGold

        gid = ch.GetGuild().GetID()

        if gid == self._m_TeamData[0].dwID:
            self._m_TeamData[0].iUsePotionPrice += int(iPrice)
        elif gid == self._m_TeamData[1].dwID:
            self._m_TeamData[1].iUsePotionPrice += int(iPrice)

    def Draw(self):
        CGuildManager.instance().RequestWarOver(self._m_TeamData[0].dwID, self._m_TeamData[1].dwID, 0, 0)

    def Timeout(self):
        self.SetTimeoutEvent(None)

        if self._m_bTimeout != 0:
            return

        if self._m_bEnded:
            return

        dwWinner = 0
        dwLoser = 0
        iRewardGold = 0

        if get_dword_time() - self._m_dwStartTime < 60000 * 5:
            self.Notice(LC_TEXT("As the Guild War was finished before time, it will be judged as a draw."))
            dwWinner = 0
            dwLoser = 0
        else:
            iWinnerIdx = -1

            if self._m_TeamData[0].iMemberCount == 0:
                iWinnerIdx = 1
            elif self._m_TeamData[1].iMemberCount == 0:
                iWinnerIdx = 0

            if iWinnerIdx == -1:
                dwWinner = self.GetWinnerGuild()

                if dwWinner == self._m_TeamData[0].dwID:
                    iRewardGold = self.GetRewardGold(0)
                    dwLoser = self._m_TeamData[1].dwID
                elif dwWinner == self._m_TeamData[1].dwID:
                    iRewardGold = self.GetRewardGold(1)
                    dwLoser = self._m_TeamData[0].dwID

                #lani_err("WarMap: member count is not zero, guild1 %u %d guild2 %u %d, winner %u", self._m_TeamData[0].dwID, self._m_TeamData[0].iMemberCount, self._m_TeamData[1].dwID, self._m_TeamData[1].iMemberCount, dwWinner)
            else:
                dwWinner = self._m_TeamData[iWinnerIdx].dwID
                dwLoser = self._m_TeamData[1 if iWinnerIdx == 0 else 0].dwID

                iRewardGold = self.GetRewardGold(byte(iWinnerIdx))

        #sys_log(0, "WarMap: Timeout %u %u winner %u loser %u reward %d map %d", self._m_TeamData[0].dwID, self._m_TeamData[1].dwID, dwWinner, dwLoser, iRewardGold, self._m_kMapInfo.lMapIndex)

        if dwWinner != 0:
            CGuildManager.instance().RequestWarOver(dwWinner, dwLoser, dwWinner, int(iRewardGold))
        else:
            CGuildManager.instance().RequestWarOver(self._m_TeamData[0].dwID, self._m_TeamData[1].dwID, dwWinner, int(iRewardGold))

        self._m_bTimeout = 1 if ((not LGEMiscellaneous.DEFINECONSTANTS.false)) else 0

    def CheckWarEnd(self):
        if self._m_bEnded:
            return

        if self._m_TeamData[0].iMemberCount == 0 or self._m_TeamData[1].iMemberCount == 0:
            if self._m_bTimeout != 0:
                return

            if self._m_pkTimeoutEvent:
                return

            self.Notice(LC_TEXT("There are no Enemies."))
            self.Notice(LC_TEXT("If no Enemy can be found the Guild War will be ended automatically."))

            #sys_log(0, "CheckWarEnd: Timeout begin %u vs %u", self._m_TeamData[0].dwID, self._m_TeamData[1].dwID)

            info = Globals.AllocEventInfo()
            info.pWarMap = self

            self.SetTimeoutEvent(event_create_ex(war_timeout_event, info, ((60) * passes_per_sec)))
        else:
            self.CheckScore()

    def SetEnded(self):
        #sys_log(0, "WarMap::SetEnded %d", self._m_kMapInfo.lMapIndex)

        if self._m_pkEndEvent:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if self._m_TeamData[0].pkChrFlag:
            CHARACTER_MANAGER.instance().DestroyCharacter(self._m_TeamData[0].pkChrFlag)
            self._m_TeamData[0].pkChrFlag = None

        if self._m_TeamData[0].pkChrFlagBase:
            CHARACTER_MANAGER.instance().DestroyCharacter(self._m_TeamData[0].pkChrFlagBase)
            self._m_TeamData[0].pkChrFlagBase = None

        if self._m_TeamData[1].pkChrFlag:
            CHARACTER_MANAGER.instance().DestroyCharacter(self._m_TeamData[1].pkChrFlag)
            self._m_TeamData[1].pkChrFlag = None

        if self._m_TeamData[1].pkChrFlagBase:
            CHARACTER_MANAGER.instance().DestroyCharacter(self._m_TeamData[1].pkChrFlagBase)
            self._m_TeamData[1].pkChrFlagBase = None

        event_cancel(self._m_pkResetFlagEvent)
        self._m_bEnded = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        info = Globals.AllocEventInfo()

        info.pWarMap = self
        info.iStep = 0
        self.SetEndEvent(event_create_ex(war_end_event, info, ((10) * passes_per_sec)))
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def ExitAll(self):
        f = FExitGuildWar()
        std::for_each(self._m_set_pkChr.begin(), self._m_set_pkChr.end(), f.functor_method)

    def SetBeginEvent(self, pkEv):
        if self._m_pkBeginEvent is not None:
            event_cancel(self._m_pkBeginEvent)
        if pkEv is not None:
## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: m_pkBeginEvent = pkEv;
            self._m_pkBeginEvent.copy_from(pkEv)

    def SetTimeoutEvent(self, pkEv):
        if self._m_pkTimeoutEvent is not None:
            event_cancel(self._m_pkTimeoutEvent)
        if pkEv is not None:
## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: m_pkTimeoutEvent = pkEv;
            self._m_pkTimeoutEvent.copy_from(pkEv)

    def SetEndEvent(self, pkEv):
        if self._m_pkEndEvent is not None:
            event_cancel(self._m_pkEndEvent)
        if pkEv is not None:
## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: m_pkEndEvent = pkEv;
            self._m_pkEndEvent.copy_from(pkEv)

    def SetResetFlagEvent(self, pkEv):
        if self._m_pkResetFlagEvent is not None:
            event_cancel(self._m_pkResetFlagEvent)
        if pkEv is not None:
## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: m_pkResetFlagEvent = pkEv;
            self._m_pkResetFlagEvent.copy_from(pkEv)

    def UpdateScore(self, g1, score1, g2, score2):
        idx = None

        temp_ref_idx = RefObject(idx);
        if self.GetTeamIndex(g1, temp_ref_idx):
            idx = temp_ref_idx.arg_value
            if self._m_TeamData[idx].iScore != score1:
                self._m_TeamData[idx].iScore = score1
                self.SendScorePacket(idx, NULL)
        else:
            idx = temp_ref_idx.arg_value

        temp_ref_idx2 = RefObject(idx);
        if self.GetTeamIndex(g2, temp_ref_idx2):
            idx = temp_ref_idx2.arg_value
            if self._m_TeamData[idx].iScore != score2:
                self._m_TeamData[idx].iScore = score2
                self.SendScorePacket(idx, NULL)
        else:
            idx = temp_ref_idx2.arg_value

        self.CheckScore()

    def CheckScore(self):
        if self._m_bEnded:
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        if get_dword_time() - self._m_dwStartTime < 30000:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if self._m_TeamData[0].iScore == self._m_TeamData[1].iScore:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        iEndScore = self._m_WarInfo.iEndScore

        if test_server:
            iEndScore = math.trunc(iEndScore / float(10))

        dwWinner = None
        dwLoser = None

        if self._m_TeamData[0].iScore >= iEndScore:
            dwWinner = self._m_TeamData[0].dwID
            dwLoser = self._m_TeamData[1].dwID
        elif self._m_TeamData[1].iScore >= iEndScore:
            dwWinner = self._m_TeamData[1].dwID
            dwLoser = self._m_TeamData[0].dwID
        else:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        iRewardGold = 0

        if dwWinner == self._m_TeamData[0].dwID:
            iRewardGold = self.GetRewardGold(0)
        elif dwWinner == self._m_TeamData[1].dwID:
            iRewardGold = self.GetRewardGold(1)

        #sys_log(0, "WarMap::CheckScore end score %d guild1 %u score guild2 %d %u score %d winner %u reward %d", iEndScore, self._m_TeamData[0].dwID, self._m_TeamData[0].iScore, self._m_TeamData[1].dwID, self._m_TeamData[1].iScore, dwWinner, iRewardGold)

        CGuildManager.instance().RequestWarOver(dwWinner, dwLoser, dwWinner, int(iRewardGold))
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def GetRewardGold(self, bWinnerIdx):
        iRewardGold = self._m_WarInfo.iWarPrice
        iRewardGold += math.trunc((self._m_TeamData[bWinnerIdx].iUsePotionPrice * self._m_WarInfo.iWinnerPotionRewardPctToWinner) / float(100))
        iRewardGold += math.trunc((self._m_TeamData[0 if bWinnerIdx != 0 else 1].iUsePotionPrice * self._m_WarInfo.iLoserPotionRewardPctToWinner) / float(100))
        return iRewardGold

# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    GetGuildIndex(dwGuild, iIndex)
    def Packet(self, p, size):
        f = FPacket(p, size)
        std::for_each(self._m_set_pkChr.begin(), self._m_set_pkChr.end(), f.functor_method)

    def Notice(self, psz):
        f = FNotice(psz)
        std::for_each(self._m_set_pkChr.begin(), self._m_set_pkChr.end(), f.functor_method)

    def SendWarPacket(self, d):
        pack = packet_guild()
        pack2 = packet_guild_war()

        pack.header = byte(Globals.LG_HEADER_GC_GUILD)
        pack.subheader = byte(Globals.GUILD_SUBLG_HEADER_GC_WAR)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        pack.size = sizeof(pack) + sizeof(pack2)

        pack2.dwGuildSelf = self._m_TeamData[0].dwID
        pack2.dwGuildOpp = self._m_TeamData[1].dwID
        pack2.bType = byte(CGuildManager.instance().TouchGuild(self._m_TeamData[0].dwID).GetGuildWarType(self._m_TeamData[1].dwID))
        pack2.bWarState = byte(CGuildManager.instance().TouchGuild(self._m_TeamData[0].dwID).GetGuildWarState(self._m_TeamData[1].dwID))

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        d.BufferedPacket(pack, sizeof(pack))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        d.Packet(pack2, sizeof(pack2))

    def SendScorePacket(self, bIdx, d = None):
        p = packet_guild()

        p.header = byte(Globals.LG_HEADER_GC_GUILD)
        p.subheader = byte(Globals.GUILD_SUBLG_HEADER_GC_WAR_SCORE)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        p.size = sizeof(p) + sizeof(uint) + sizeof(uint) + sizeof(int)

        buf = TEMP_BUFFER(8192, DefineConstants.false)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        buf.write(p, sizeof(p))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        buf.write(self._m_TeamData[bIdx].dwID, sizeof(uint))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        buf.write(self._m_TeamData[0 if bIdx != 0 else 1].dwID, sizeof(uint))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        buf.write(self._m_TeamData[bIdx].iScore, sizeof(int))

        if d:
            d.Packet(buf.read_peek(), buf.size())
        else:
            self.Packet(buf.read_peek(), buf.size())

    def OnKill(self, killer, ch):
        if self._m_bEnded:
            return

        dwKillerGuild = 0
        dwDeadGuild = 0

        if killer.GetGuild():
            dwKillerGuild = killer.GetGuild().GetID()

        if ch.GetGuild():
            dwDeadGuild = ch.GetGuild().GetID()

        idx = None

        #sys_log(0, "WarMap::OnKill %u %u", dwKillerGuild, dwDeadGuild)

        temp_ref_idx = RefObject(idx);
        if not self.GetTeamIndex(dwKillerGuild, temp_ref_idx):
            idx = temp_ref_idx.arg_value
            return
        else:
            idx = temp_ref_idx.arg_value

        temp_ref_idx2 = RefObject(idx);
        if not self.GetTeamIndex(dwDeadGuild, temp_ref_idx2):
            idx = temp_ref_idx2.arg_value
            return
        else:
            idx = temp_ref_idx2.arg_value

        if self._m_kMapInfo.bType == EWarMapTypes.WAR_MAP_TYPE_NORMAL:
            SendGuildWarScore(dwKillerGuild, dwDeadGuild, 1, ch.GetLevel())

        elif self._m_kMapInfo.bType == EWarMapTypes.WAR_MAP_TYPE_FLAG:
                pkAff = ch.FindAffect(LaniatusEAffectTypes.LANIA_AFFECT_WAR_FLAG, APPLY_NONE)

                if pkAff:
                    temp_ref_idx3 = RefObject(idx);
                    if self.GetTeamIndex(uint(pkAff.lApplyValue), temp_ref_idx3):
                        idx = temp_ref_idx3.arg_value
                        self.AddFlag(idx, uint(ch.GetX()), uint(ch.GetY()))
                    else:
                        idx = temp_ref_idx3.arg_value

                    ch.RemoveAffect(LaniatusEAffectTypes.LANIA_AFFECT_WAR_FLAG)

        else:
            #lani_err("unknown war map type %u index %d", self._m_kMapInfo.bType, self._m_kMapInfo.lMapIndex)

    def AddFlag(self, bIdx, x = 0, y = 0):
        if self._m_bEnded:
            return

        assert bIdx < 2

        r = self._m_TeamData[bIdx]

        if r.pkChrFlag:
            return

        if x == 0:
            x = uint(self._m_kMapInfo.posStart[bIdx].x)
            y = uint(self._m_kMapInfo.posStart[bIdx].y)

        r.pkChrFlag = CHARACTER_MANAGER.instance().SpawnMob(uint(warmap.WAR_FLAG_VNUM0) if bIdx == 0 else uint(warmap.WAR_FLAG_VNUM1), self._m_kMapInfo.lMapIndex, int(x), int(y), 0, DefineConstants.false, -1, ((not DefineConstants.false)))
        #sys_log(0, "WarMap::AddFlag %u %p id %u", bIdx, Globals.get_pointer(r.pkChrFlag), r.dwID)

        r.pkChrFlag.SetPoint(EPointTypes.LG_POINT_STAT, r.dwID)
        r.pkChrFlag.SetWarMap(self)

    def AddFlagBase(self, bIdx, x = 0, y = 0):
        if self._m_bEnded:
            return

        assert bIdx < 2

        r = self._m_TeamData[bIdx]

        if r.pkChrFlagBase:
            return

        if x == 0:
            x = uint(self._m_kMapInfo.posStart[bIdx].x)
            y = uint(self._m_kMapInfo.posStart[bIdx].y)

        r.pkChrFlagBase = CHARACTER_MANAGER.instance().SpawnMob(uint(warmap.WAR_FLAG_BASE_VNUM), self._m_kMapInfo.lMapIndex, int(x), int(y), 0, DefineConstants.false, -1, ((not DefineConstants.false)))
        #sys_log(0, "WarMap::AddFlagBase %u %p id %u", bIdx, Globals.get_pointer(r.pkChrFlagBase), r.dwID)

        r.pkChrFlagBase.SetPoint(EPointTypes.LG_POINT_STAT, r.dwID)
        r.pkChrFlagBase.SetWarMap(self)

    def RemoveFlag(self, bIdx):
        assert bIdx < 2

        r = self._m_TeamData[bIdx]

        if not r.pkChrFlag:
            return

        #sys_log(0, "WarMap::RemoveFlag %u %p", bIdx, Globals.get_pointer(r.pkChrFlag))

        r.pkChrFlag.Dead(None, ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
        r.pkChrFlag = None

    def IsFlagOnBase(self, bIdx):
        assert bIdx < 2

        r = self._m_TeamData[bIdx]

        if not r.pkChrFlag:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        pos = r.pkChrFlag.GetXYZ()

        if pos.x == self._m_kMapInfo.posStart[bIdx].x and pos.y == self._m_kMapInfo.posStart[bIdx].y:
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        return LGEMiscellaneous.DEFINECONSTANTS.false

    def ResetFlag(self):
        if self._m_kMapInfo.bType != EWarMapTypes.WAR_MAP_TYPE_FLAG:
            return

        if self._m_pkResetFlagEvent:
            return

        if self._m_bEnded:
            return

        f = FRemoveFlagAffect()
        std::for_each(self._m_set_pkChr.begin(), self._m_set_pkChr.end(), f.functor_method)

        self.RemoveFlag(0)
        self.RemoveFlag(1)

        info = Globals.AllocEventInfo()

        info.pWarMap = self
        info.iStep = 0
        self.SetResetFlagEvent(event_create_ex(war_reset_flag_event, info, ((10) * passes_per_sec)))

    def _UpdateUserCount(self):
        f = FSendUserCount(self._m_TeamData[0].dwID, self._m_TeamData[0].GetAccumulatedJoinerCount(), self._m_TeamData[1].dwID, self._m_TeamData[1].GetAccumulatedJoinerCount(), self._m_iObserverCount)

        std::for_each(self._m_set_pkChr.begin(), self._m_set_pkChr.end(), f.functor_method)



    class STeamData:

        def __init__(self):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.dwID = 0
            self.pkGuild = None
            self.iMemberCount = 0
            self.iUsePotionPrice = 0
            self.iScore = 0
            self.pkChrFlag = None
            self.pkChrFlagBase = None
            self.set_pidJoiner = std::set()



        def Initialize(self):
            self.dwID = 0
            self.pkGuild = None
            self.iMemberCount = 0
            self.iUsePotionPrice = 0
            self.iScore = 0
            self.pkChrFlag = None
            self.pkChrFlagBase = None

            self.set_pidJoiner.clear()

        def GetAccumulatedJoinerCount(self):
            return self.set_pidJoiner.size()

        def GetCurJointerCount(self):
            return self.iMemberCount

        def AppendMember(self, ch):
            self.set_pidJoiner.insert(ch.GetPlayerID())
            self.iMemberCount += 1

        def RemoveMember(self, ch):
            self.iMemberCount -= 1


class CWarMapManager(singleton):
    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self._m_map_kWarMapInfo = {}
        self._m_mapWarMap = {}


    def close(self):
        iter = m_map_kWarMapInfo.begin()
        while iter is not self._m_map_kWarMapInfo.end():
            LG_DEL_MEM(iter.second)
            iter += 1

        self._m_map_kWarMapInfo.clear()

    def LoadWarMapInfo(self, c_pszFileName):
        k = None

        k = LG_NEW_M2 SWarMapInfo
        k.bType = EWarMapTypes.WAR_MAP_TYPE_NORMAL

        k.lMapIndex = 110
        k.posStart[0].x = 48 * 100 + 32000
        k.posStart[0].y = 52 * 100 + 0
        k.posStart[1].x = 183 * 100 + 32000
        k.posStart[1].y = 206 * 100 + 0
        k.posStart[2].x = 141 * 100 + 32000
        k.posStart[2].y = 117 * 100 + 0

        self._m_map_kWarMapInfo.update({k.lMapIndex: k})

        k = LG_NEW_M2 SWarMapInfo
        k.bType = EWarMapTypes.WAR_MAP_TYPE_FLAG

        k.lMapIndex = 111
        k.posStart[0].x = 68 * 100 + 57600
        k.posStart[0].y = 69 * 100 + 0
        k.posStart[1].x = 171 * 100 + 57600
        k.posStart[1].y = 182 * 100 + 0
        k.posStart[2].x = 122 * 100 + 57600
        k.posStart[2].y = 131 * 100 + 0

        self._m_map_kWarMapInfo.update({k.lMapIndex: k})
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def IsWarMap(self, lMapIndex):
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false)) if self.GetWarMapInfo(lMapIndex) is not None else LGEMiscellaneous.DEFINECONSTANTS.false

    def GetWarMapInfo(self, lMapIndex):
        if lMapIndex >= 10000:
            lMapIndex = math.trunc(lMapIndex / float(10000))

        it = self._m_map_kWarMapInfo.find(lMapIndex)

        if self._m_map_kWarMapInfo.end() is it:
            return None

        return it.second

    def GetStartPosition(self, lMapIndex, bIdx, pos):
        assert bIdx < 3

        pi = self.GetWarMapInfo(lMapIndex)

        if pi is None:
            #sys_log(0, "GetStartPosition FAILED [%d] WarMapInfoSize(%d)", lMapIndex, len(self._m_map_kWarMapInfo))

            it = m_map_kWarMapInfo.begin()
            while it is not self._m_map_kWarMapInfo.end():
                cur = it.second.posStart[bIdx]
                #sys_log(0, "WarMap[%d]=Pos(%d, %d)", it.first, cur.x, cur.y)
                it += 1
            return LGEMiscellaneous.DEFINECONSTANTS.false

        pos.arg_value = pi.posStart[bIdx]
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def for_each(self, f):
        it = m_mapWarMap.begin()
        while it is not self._m_mapWarMap.end():
            f(it.second)
            it += 1

        return f

    def CreateWarMap(self, guildWarInfo, dwGuildID1, dwGuildID2):
        pkInfo = self.GetWarMapInfo(guildWarInfo.lMapIndex)
        if pkInfo is None:
            #lani_err("GuildWar.CreateWarMap.NOT_FOUND_MAPINFO[%d]", guildWarInfo.lMapIndex)
            return 0

        lMapIndex = uint(SECTREE_MANAGER.instance().CreatePrivateMap(guildWarInfo.lMapIndex))

        if lMapIndex != 0:
            self._m_mapWarMap.update({lMapIndex: LG_NEW_M2 CWarMap(int(lMapIndex), guildWarInfo, pkInfo, dwGuildID1, dwGuildID2)})

        return int(lMapIndex)

    def DestroyWarMap(self, pMap):
        mapIdx = pMap.GetMapIndex()

        #sys_log(0, "WarMap::DestroyWarMap : %d", mapIdx)

        self._m_mapWarMap.pop(pMap.GetMapIndex())
        LG_DEL_MEM(pMap)

        SECTREE_MANAGER.instance().DestroyPrivateMap(mapIdx)

    def Find(self, lMapIndex):
        it = self._m_mapWarMap.find(lMapIndex)

        if it is self._m_mapWarMap.end():
            return None

        return it.second

    def CountWarMap(self):
        return len(self._m_mapWarMap)
    def OnShutdown(self):
        it = self._m_mapWarMap.begin()

        while it is not self._m_mapWarMap.end():
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: (it++)->second->Draw();
            (it).second.Draw()
            it += 1




class war_map_info(event_info_data):

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.iStep = 0
        self.pWarMap = None

        self.iStep = 0
        self.pWarMap = None


class FSendUserCount:

    def __init__(self, g1, g1_count, g2, g2_count, observer):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.buf1 = str(['\0' for _ in range(30)])
        self.buf2 = str(['\0' for _ in range(128)])

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        snprintf(self.buf1, sizeof(self.buf1), "ObserverCount %d", observer)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        snprintf(self.buf2, sizeof(self.buf2), "WarUC %u %d %u %d %d", g1, g1_count, g2, g2_count, observer)

    def functor_method(self, ch):
        ch.ChatPacket(EChatType.CHAT_TYPE_COMMAND, self.buf1)
        ch.ChatPacket(EChatType.CHAT_TYPE_COMMAND, self.buf2)

class FExitGuildWar:
    def functor_method(self, ch):
        if ch.IsPC():
            ch.ExitToSavedLocation()

## Laniatus Games Studio Inc. | NOTE: Anonymous namespaces are not defined:
#namespace
class FPacket:
    def __init__(self, p, size):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.m_pvData = None
        self.m_iSize = 0

        self.m_pvData = p
        self.m_iSize = size

    def functor_method(self, ch):
        ch.GetDesc().Packet(self.m_pvData, self.m_iSize)


class FNotice:
    def __init__(self, psz):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.m_psz = '\0'

        self.m_psz = psz

    def functor_method(self, ch):
        ch.ChatPacket(EChatType.CHAT_TYPE_NOTICE, "%s", self.m_psz)


class FRemoveFlagAffect:
    def functor_method(self, ch):
        if ch.FindAffect(LaniatusEAffectTypes.LANIA_AFFECT_WAR_FLAG, APPLY_NONE):
            ch.RemoveAffect(LaniatusEAffectTypes.LANIA_AFFECT_WAR_FLAG)

