## Laniatus Games Studio Inc. | NOTE: Python has no need of forward class declarations:
#class CGuild
## Laniatus Games Studio Inc. | NOTE: Python has no need of forward class declarations:
#struct TGuildCreateParameter


class CGuildWarReserveForGame:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.data = SGuildReserve()
        self.mapBet = {}


class CGuildManager(singleton):
    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self._m_mapGuild = {}
        self._m_GuildWar = std::set()
        self._m_GuildWarEndTime = {}
        self._m_map_pkGuildByPID = {}
        self._m_map_kReserveWar = {}
        self._m_vec_kReserveWar = []


    def close(self):
        iter = m_mapGuild.begin()
        while iter is not self._m_mapGuild.end():
            LG_DEL_MEM(iter.second)
            iter += 1

        self._m_mapGuild.clear()

    def CreateGuild(self, gcp):
        if gcp.master is None:
            return 0

        if not check_name(gcp.name):
            gcp.master.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> The Guildname is invalid."))
            return 0

        pmsg = std::unique_ptr(DBManager.instance().DirectQuery("SELECT COUNT(*) FROM guild%s WHERE name = '%s'", get_table_postfix(), gcp.name))

        if pmsg.Get().uiNumRows > 0:
            row = mysql_fetch_row(pmsg.Get().pSQLResult)

            if not(row[0] and row[0][0] == '0'):
                gcp.master.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> This Guild name is already taken."))
                return 0
        else:
            gcp.master.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> You cannot create a Guild."))
            return 0

        pg = LG_NEW_M2 CGuild(gcp)
        self._m_mapGuild.update({pg.GetID(): pg})
        return pg.GetID()

    def FindGuild(self, guild_id):
        it = self._m_mapGuild.find(guild_id)
        if it is self._m_mapGuild.end():
            return None
        return it.second

    def FindGuildByName(self, guild_name):
        it = m_mapGuild.begin()
        while it is not self._m_mapGuild.end():
            if it.second.GetName()==guild_name:
                return it.second
            it += 1
        return None

    def LoadGuild(self, guild_id):
        it = self._m_mapGuild.find(guild_id)

        if it is self._m_mapGuild.end():
            self._m_mapGuild.update({guild_id: LG_NEW_M2 CGuild(guild_id)})
        else:
            pass

    def TouchGuild(self, guild_id):
        it = self._m_mapGuild.find(guild_id)

        if it is self._m_mapGuild.end():
            self._m_mapGuild.update({guild_id: LG_NEW_M2 CGuild(guild_id)})
## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: it = m_mapGuild.find(guild_id);
            it.copy_from(self._m_mapGuild.find(guild_id))

            CHARACTER_MANAGER.instance().for_each_pc.functor_method(FGuildNameSender(guild_id, it.second.GetName()))

        return it.second

    def DisbandGuild(self, guild_id):
        it = self._m_mapGuild.find(guild_id)

        if it is self._m_mapGuild.end():
            return

        it.second.Disband()

        LG_DEL_MEM(it.second)
        self._m_mapGuild.pop(it)

        CGuildMarkManager.instance().DeleteMark(guild_id)

    def Initialize(self):
        #sys_log(0, "Initializing Guild")

        if g_bAuthServer:
            return

        pmsg = std::unique_ptr(DBManager.instance().DirectQuery("SELECT id FROM guild%s", get_table_postfix()))

        vecGuildID = []
        vecGuildID.reserve(pmsg.Get().uiNumRows)

        LaniatusDefVariables = 0
        while LaniatusDefVariables < pmsg.Get().uiNumRows:
            row = mysql_fetch_row(pmsg.Get().pSQLResult)
            guild_id = strtoul(row[0], str(None), 10)
            self.LoadGuild(guild_id)

            vecGuildID.append(guild_id)
            LaniatusDefVariables += 1

        rkMarkMgr = CGuildMarkManager.instance()

        rkMarkMgr.SetMarkPathPrefix("mark")

## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
#        extern bool GuildMarkConvert(const list<uint> & vecGuildID)
        GuildMarkConvert(vecGuildID)

        rkMarkMgr.LoadMarkIndex()
        rkMarkMgr.LoadMarkImages()
        rkMarkMgr.LoadSymbol(LGEMiscellaneous.DEFINECONSTANTS.GUILD_SYMBOL_FILENAME)

    def Link(self, pid, guild):
        if pid not in self._m_map_pkGuildByPID.keys():
            self._m_map_pkGuildByPID.update({pid: guild})

    def Unlink(self, pid):
        self._m_map_pkGuildByPID.pop(pid)

    def GetLinkedGuild(self, pid):
        it = self._m_map_pkGuildByPID.find(pid)

        if it is self._m_map_pkGuildByPID.end():
            return None

        return it.second

    def LoginMember(self, ch):
        it = self._m_map_pkGuildByPID.find(ch.GetPlayerID())

        if it is not self._m_map_pkGuildByPID.end():
            it.second.LoginMember(ch)

    def P2PLoginMember(self, pid):
        it = self._m_map_pkGuildByPID.find(pid)

        if it is not self._m_map_pkGuildByPID.end():
            it.second.P2PLoginMember(pid)

    def P2PLogoutMember(self, pid):
        it = self._m_map_pkGuildByPID.find(pid)

        if it is not self._m_map_pkGuildByPID.end():
            it.second.P2PLogoutMember(pid)

    def SkillRecharge(self):
        it = m_mapGuild.begin()
        while it is not self._m_mapGuild.end():
            it.second.SkillRecharge()
            it += 1

    def ShowGuildWarList(self, ch):
        it = m_GuildWar.begin()
        while it is not self._m_GuildWar.end():
            A = self.TouchGuild(it.first)
            B = self.TouchGuild(it.second)

            if A is not None and B is not None:
                ch.ChatPacket(EChatType.CHAT_TYPE_NOTICE, "%s[%d] vs %s[%d] time %u sec.", A.GetName(), A.GetID(), B.GetName(), B.GetID(), get_global_time() - A.GetWarStartTime(B.GetID()))
            it += 1

    def SendGuildWar(self, ch):
        if ch.GetDesc() is None:
            return

        buf = TEMP_BUFFER(8192, DefineConstants.false)
        p = packet_guild()
        p.header = byte(Globals.LG_HEADER_GC_GUILD)
        p.subheader = byte(Globals.GUILD_SUBLG_HEADER_GC_GUILD_WAR_LIST)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        p.size = sizeof(p) + (sizeof(uint) * 2) * self._m_GuildWar.size()
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        buf.write(p, sizeof(p))

        it = m_GuildWar.begin()
        while it is not self._m_GuildWar.end():
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            buf.write(it.first, sizeof(uint))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            buf.write(it.second, sizeof(uint))
            it += 1

        ch.GetDesc().Packet(buf.read_peek(), buf.size())

    def RequestEndWar(self, guild_id1, guild_id2):
        #sys_log(0, "RequestEndWar %d %d", guild_id1, guild_id2)

        p = SPacketGuildWar()
        p.bWar = EGuildWarState.GUILD_WAR_END
        p.dwGuildFrom = guild_id1
        p.dwGuildTo = guild_id2
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        db_clientdesc.DBPacket(Globals.LG_HEADER_GD_GUILD_WAR, 0, p, sizeof(p))

    def RequestCancelWar(self, guild_id1, guild_id2):
        #sys_log(0, "RequestCancelWar %d %d", guild_id1, guild_id2)

        p = SPacketGuildWar()
        p.bWar = EGuildWarState.GUILD_WAR_CANCEL
        p.dwGuildFrom = guild_id1
        p.dwGuildTo = guild_id2
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        db_clientdesc.DBPacket(Globals.LG_HEADER_GD_GUILD_WAR, 0, p, sizeof(p))

    def RequestWarOver(self, dwGuild1, dwGuild2, dwGuildWinner, lReward):
        g1 = self.TouchGuild(dwGuild1)
        g2 = self.TouchGuild(dwGuild2)

        if g1.GetGuildWarState(g2.GetID()) != EGuildWarState.GUILD_WAR_ON_WAR:
            #sys_log(0, "RequestWarOver : both guild was not in war %u %u", dwGuild1, dwGuild2)
            self.RequestEndWar(dwGuild1, dwGuild2)
            return

        p = SPacketGuildWar()

        p.bWar = EGuildWarState.GUILD_WAR_OVER
        p.lWarPrice = 0
        p.bType = byte(1 if dwGuildWinner == 0 else 0)

        if dwGuildWinner == 0:
            p.dwGuildFrom = dwGuild1
            p.dwGuildTo = dwGuild2
        else:
            p.dwGuildFrom = dwGuildWinner
            p.dwGuildTo = dwGuild2 if dwGuildWinner == dwGuild1 else dwGuild1

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        db_clientdesc.DBPacket(Globals.LG_HEADER_GD_GUILD_WAR, 0, p, sizeof(p))
        #sys_log(0, "RequestWarOver : winner %u loser %u draw %u betprice %lld", p.dwGuildFrom, p.dwGuildTo, p.bType, p.lWarPrice)

    def DeclareWar(self, guild_id1, guild_id2, bType):
        if guild_id1 == guild_id2:
            return

        g1 = self.FindGuild(guild_id1)
        g2 = self.FindGuild(guild_id2)

        if g1 is None or g2 is None:
            return

        if g1.DeclareWar(guild_id2, bType, EGuildWarState.GUILD_WAR_SEND_DECLARE) and g2.DeclareWar(guild_id1, bType, EGuildWarState.GUILD_WAR_RECV_DECLARE):

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if __MULTI_LANGUAGE_SYSTEM__
            SendNotice(LC_TEXT("The %s Guild declared war on the %s Guild!"), self.TouchGuild(guild_id1).GetName(), self.TouchGuild(guild_id2).GetName())
##else
            buf = str(['\0' for _ in range(256)])
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            snprintf(buf, sizeof(buf), LC_TEXT("The %s Guild declared war on the %s Guild!"), self.TouchGuild(guild_id1).GetName(), self.TouchGuild(guild_id2).GetName())
            SendNotice(buf)
##endif

    def RefuseWar(self, guild_id1, guild_id2):
        g1 = self.FindGuild(guild_id1)
        g2 = self.FindGuild(guild_id2)

        if g1 is not None and g2 is not None:
            if g2.GetMasterCharacter():
                g2.GetMasterCharacter().ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> %s declined the Guild war."), g1.GetName())

        if g1 is not None:
            g1.RefuseWar(guild_id2)

        if g2 is not None and g1 is not None:
            g2.RefuseWar(g1.GetID())

    def StartWar(self, guild_id1, guild_id2):
        g1 = self.FindGuild(guild_id1)
        g2 = self.FindGuild(guild_id2)

        if g1 is None or g2 is None:
            return

        if (not g1.CheckStartWar(guild_id2)) or not g2.CheckStartWar(guild_id1):
            return

        g1.StartWar(guild_id2)
        g2.StartWar(guild_id1)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if __MULTI_LANGUAGE_SYSTEM__
        SendNotice(LC_TEXT("The War between the %s Guild and the %s Guild has begun."), g1.GetName(), g2.GetName())
##else
        buf = str(['\0' for _ in range(256)])
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        snprintf(buf, sizeof(buf), LC_TEXT("The War between the %s Guild and the %s Guild has begun."), g1.GetName(), g2.GetName())
        SendNotice(buf)
##endif

        if guild_id1 > guild_id2:
            std::swap(guild_id1, guild_id2)

        CHARACTER_MANAGER.instance().for_each_pc.functor_method(FSendWarList(byte(Globals.GUILD_SUBLG_HEADER_GC_GUILD_WAR_LIST), guild_id1, guild_id2))
        self._m_GuildWar.insert((guild_id1, guild_id2))

    def WaitStartWar(self, guild_id1, guild_id2):
        g1 = self.FindGuild(guild_id1)
        g2 = self.FindGuild(guild_id2)

        if g1 is None or g2 is None:
            #sys_log(0, "GuildWar: CGuildManager::WaitStartWar(%d,%d) - something wrong in arg. there is no guild like that.", guild_id1, guild_id2)
            return

        if g1.WaitStartWar(guild_id2) or g2.WaitStartWar(guild_id1):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if __MULTI_LANGUAGE_SYSTEM__
            SendNotice(LC_TEXT("The War between the %s Guild and the %s Guild begins in a few minutes!"), g1.GetName(), g2.GetName())
##else
            buf = str(['\0' for _ in range(256)])
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            snprintf(buf, sizeof(buf), LC_TEXT("The War between the %s Guild and the %s Guild begins in a few minutes!"), g1.GetName(), g2.GetName())
            SendNotice(buf)
##endif

    def WarOver(self, guild_id1, guild_id2, bDraw):
        g1 = self.FindGuild(guild_id1)
        g2 = self.FindGuild(guild_id2)

        if guild_id1 > guild_id2:
            std::swap(guild_id1, guild_id2)

        k = (guild_id1, guild_id2)

        it = self._m_GuildWar.find(k)

        if self._m_GuildWar.end() == it:
            return

        Globals.SendGuildWarOverNotice(g1, g2, bDraw)

        self.EndWar(guild_id1, guild_id2)

    def CancelWar(self, guild_id1, guild_id2):
        if not self.EndWar(guild_id1, guild_id2):
            return

        g1 = self.FindGuild(guild_id1)
        g2 = self.FindGuild(guild_id2)

        if g1:
            master1 = g1.GetMasterCharacter()

            if master1:
                master1.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> The Guild war is cancelled."))

        if g2:
            master2 = g2.GetMasterCharacter()

            if master2:
                master2.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> The Guild war is cancelled."))

        if g1 is not None and g2 is not None:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if __MULTI_LANGUAGE_SYSTEM__
            SendNotice(LC_TEXT("The War between the %s Guild and the %s Guild was cancelled."), g1.GetName(), g2.GetName())
##else
            buf = str(['\0' for _ in range(256+1)])
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            snprintf(buf, sizeof(buf), LC_TEXT("The War between the %s Guild and the %s Guild was cancelled."), g1.GetName(), g2.GetName())
            SendNotice(buf)
##endif

    def EndWar(self, guild_id1, guild_id2):
        if guild_id1 > guild_id2:
            std::swap(guild_id1, guild_id2)

        g1 = self.FindGuild(guild_id1)
        g2 = self.FindGuild(guild_id2)

        k = (guild_id1, guild_id2)

        it = self._m_GuildWar.find(k)

        if self._m_GuildWar.end() == it:
            #sys_log(0, "EndWar(%d,%d) - EndWar request but guild is not in list", guild_id1, guild_id2)
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if g1 is not None and g2 is not None:
            if g1.GetGuildWarType(guild_id2) == EGuildWarType.GUILD_WAR_TYPE_FIELD:
                Globals.SendGuildWarOverNotice(g1, g2, g1.GetWarScoreAgainstTo(guild_id2) == g2.GetWarScoreAgainstTo(guild_id1))
        else:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if g1:
            g1.EndWar(guild_id2)

        if g2:
            g2.EndWar(guild_id1)

        self._m_GuildWarEndTime[k] = get_global_time()
        CHARACTER_MANAGER.instance().for_each_pc.functor_method(FSendWarList(byte(Globals.GUILD_SUBLG_HEADER_GC_GUILD_WAR_END_LIST), guild_id1, guild_id2))
        self._m_GuildWar.erase(it)

        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def ReserveWar(self, dwGuild1, dwGuild2, bType):
        #sys_log(0, "GuildManager::ReserveWar %u %u", dwGuild1, dwGuild2)

        g1 = self.FindGuild(dwGuild1)
        g2 = self.FindGuild(dwGuild2)

        if g1 is None or g2 is None:
            return

        g1.ReserveWar(dwGuild2, bType)
        g2.ReserveWar(dwGuild1, bType)

    def ReserveWarAdd(self, p):
        it = self._m_map_kReserveWar.find(p.dwID)

        pkReserve = None

        if it is not self._m_map_kReserveWar.end():
            pkReserve = it.second
        else:
            pkReserve = LG_NEW_M2 CGuildWarReserveForGame

            self._m_map_kReserveWar.update({p.dwID: pkReserve})
            self._m_vec_kReserveWar.append(pkReserve)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memcpy' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memcpy(pkReserve.data, p, sizeof(SGuildReserve))

        #sys_log(0, "ReserveWarAdd %u gid1 %u power %d gid2 %u power %d handicap %d", pkReserve.data.dwID, p.dwGuildFrom, p.lPowerFrom, p.dwGuildTo, p.lPowerTo, p.lHandicap)

    def ReserveWarDelete(self, dwID):
        #sys_log(0, "ReserveWarDelete %u", dwID)
        it = self._m_map_kReserveWar.find(dwID)

        if it is self._m_map_kReserveWar.end():
            return

        it_vec = self._m_vec_kReserveWar.begin()

        while it_vec is not self._m_vec_kReserveWar.end():
            if *it_vec == it.second:
## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: it_vec = m_vec_kReserveWar.erase(it_vec);
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no direct equivalent to the STL vector 'erase' method in Python:
                it_vec.copy_from(self._m_vec_kReserveWar.erase(it_vec))
                break
            else:
                it_vec += 1

        LG_DEL_MEM(it.second)
        self._m_map_kReserveWar.pop(it)

    def GetReserveWarRef(self):
        return list(self._m_vec_kReserveWar)

    def ReserveWarBet(self, p):
        it = self._m_map_kReserveWar.find(p.dwWarID)

        if it is self._m_map_kReserveWar.end():
            return

        it.second.mapBet.insert((p.szLogin, (p.dwGuild, p.lldGold)))

    def IsBet(self, dwID, c_pszLogin):
        it = self._m_map_kReserveWar.find(dwID)

        if it is self._m_map_kReserveWar.end():
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        return it.second.mapBet.end() != it.second.mapBet.find(c_pszLogin)

    def StopAllGuildWar(self):
        it = m_GuildWar.begin()
        while it is not self._m_GuildWar.end():
            g = CGuildManager.instance().TouchGuild(it.first)
            pg = CGuildManager.instance().TouchGuild(it.second)
            g.EndWar(it.second)
            pg.EndWar(it.first)
            it += 1

        self._m_GuildWar.clear()

    def Kill(self, killer, victim):
        if not killer.IsPC():
            return

        if not victim.IsPC():
            return

        if killer.GetWarMap():
            killer.GetWarMap().OnKill(killer, victim)
            return

        gAttack = killer.GetGuild()
        gDefend = victim.GetGuild()

        if gAttack is None or gDefend is None:
            return

        if gAttack.GetGuildWarType(gDefend.GetID()) != EGuildWarType.GUILD_WAR_TYPE_FIELD:
            return

        if not gAttack.UnderWar(gDefend.GetID()):
            return

        Globals.SendGuildWarScore(gAttack.GetID(), gDefend.GetID(), victim.GetLevel(), 0)

    def GetRank(self, g):
        point = g.GetLadderPoint()
        rank = 1

        it = m_mapGuild.begin()
        while it is not self._m_mapGuild.end():
            pg = it.second

            if pg.GetLadderPoint() > point:
                rank += 1
            it += 1

        return rank

    def GetHighRankString(self, dwMyGuild, buffer, buflen):
        v = []

        it = m_mapGuild.begin()
        while it is not self._m_mapGuild.end():
            if it.second:
                v.append(it.second)
            it += 1

        std::sort(v.begin(), v.end(), FGuildCompare())
        n = len(v)
        len = 0
        len2 = None
        buffer.arg_value[0] = '\0'

        for LaniatusDefVariables in range(0, 8):
            if n - LaniatusDefVariables - 1 < 0:
                break

            g = v[n - LaniatusDefVariables - 1]

            if g is None:
                continue

            if g.GetLadderPoint() <= 0:
                break

            if dwMyGuild == g.GetID():
                len2 = snprintf(buffer.arg_value[len:], buflen - len, "[COLOR r;255|g;255|b;0]")

                if len2 < 0 or len2 >= int(buflen) - len:
                    len += (buflen - len) - 1
                else:
                    len += len2

            if i:
                len2 = snprintf(buffer.arg_value[len:], buflen - len, "[ENTER]")

                if len2 < 0 or len2 >= int(buflen) - len:
                    len += (buflen - len) - 1
                else:
                    len += len2

            len2 = snprintf(buffer.arg_value[len:], buflen - len, "%3d | %-12s | %-8d | %4d | %4d | %4d", self.GetRank(g), g.GetName(), g.GetLadderPoint(), g.GetGuildWarWinCount(), g.GetGuildWarDrawCount(), g.GetGuildWarLossCount())

            if len2 < 0 or len2 >= int(buflen) - len:
                len += (buflen - len) - 1
            else:
                len += len2

            if g.GetID() == dwMyGuild:
                len2 = snprintf(buffer.arg_value[len:], buflen - len, "[/COLOR]")

                if len2 < 0 or len2 >= int(buflen) - len:
                    len += (buflen - len) - 1
                else:
                    len += len2

    def GetAroundRankString(self, dwMyGuild, buffer, buflen):
        v = []

        it = m_mapGuild.begin()
        while it is not self._m_mapGuild.end():
            if it.second:
                v.append(it.second)
            it += 1

        std::sort(v.begin(), v.end(), FGuildCompare())
        n = len(v)
        idx = None

        idx = 0
        while idx < int(len(v)):
            if v[idx].GetID() == dwMyGuild:
                break
            idx += 1

        len = 0
        len2 = None
        count = 0
        buffer.arg_value[0] = '\0'

        for LaniatusDefVariables in range(-3, 4):
            if idx - LaniatusDefVariables < 0:
                continue

            if idx - LaniatusDefVariables >= n:
                continue

            g = v[idx - i]

            if g is None:
                continue

            if dwMyGuild == g.GetID():
                len2 = snprintf(buffer.arg_value[len:], buflen - len, "[COLOR r;255|g;255|b;0]")

                if len2 < 0 or len2 >= int(buflen) - len:
                    len += (buflen - len) - 1
                else:
                    len += len2

            if count != 0:
                len2 = snprintf(buffer.arg_value[len:], buflen - len, "[ENTER]")

                if len2 < 0 or len2 >= int(buflen) - len:
                    len += (buflen - len) - 1
                else:
                    len += len2

            len2 = snprintf(buffer.arg_value[len:], buflen - len, "%3d | %-12s | %-8d | %4d | %4d | %4d", self.GetRank(g), g.GetName(), g.GetLadderPoint(), g.GetGuildWarWinCount(), g.GetGuildWarDrawCount(), g.GetGuildWarLossCount())

            if len2 < 0 or len2 >= int(buflen) - len:
                len += (buflen - len) - 1
            else:
                len += len2

            count += 1

            if g.GetID() == dwMyGuild:
                len2 = snprintf(buffer.arg_value[len:], buflen - len, "[/COLOR]")

                if len2 < 0 or len2 >= int(buflen) - len:
                    len += (buflen - len) - 1
                else:
                    len += len2

    def for_each_war(self, f):
        it = m_GuildWar.begin()
        while it is not self._m_GuildWar.end():
            f(it.first, it.second)
            it += 1

    def GetDisbandDelay(self):
        return quest.CQuestManager.instance().GetEventFlag("guild_disband_delay") * (60 if test_server else 86400)

    def GetWithdrawDelay(self):
        return quest.CQuestManager.instance().GetEventFlag("guild_withdraw_delay") * (60 if test_server else 86400)

    def ChangeMaster(self, dwGID):
        iter = self._m_mapGuild.find(dwGID)

        if iter is not self._m_mapGuild.end():
            iter.second.Load(dwGID)

        DBManager.instance().FuncQuery(std::bind(CGuild.SendGuildDataUpdateToAllMember, iter.second, std::placeholders._1), "SELECT 1")






## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python has no concept of a 'friend' class:
#    friend class CGuild


## Laniatus Games Studio Inc. | NOTE: Anonymous namespaces are not defined:
#namespace

class FGuildNameSender:
    def __init__(self, id, guild_name):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.id = 0
        self.name = '\0'
        self.p = packet_guild()

        self.id = id
        self.name = guild_name
        self.p.header = byte(Globals.LG_HEADER_GC_GUILD)
        self.p.subheader = byte(Globals.GUILD_SUBLG_HEADER_GC_GUILD_NAME)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.p.size = sizeof(self.p) + LGEMiscellaneous.GUILD_NAME_MAX_LEN + sizeof(uint)

    def functor_method(self, ch):
        d = ch.GetDesc()

        if d:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            d.BufferedPacket(self.p, sizeof(self.p))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            d.BufferedPacket(self.id, sizeof(self.id))
            d.Packet(self.name, LGEMiscellaneous.GUILD_NAME_MAX_LEN)


class FGuildCompare:

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: bool operator ()(CGuild* g1, CGuild* g2) const
    def functor_method(self, g1, g2):
        if g1.GetLadderPoint() < g2.GetLadderPoint():
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
        if g1.GetLadderPoint() > g2.GetLadderPoint():
            return LGEMiscellaneous.DEFINECONSTANTS.false
        if g1.GetGuildWarWinCount() < g2.GetGuildWarWinCount():
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
        if g1.GetGuildWarWinCount() > g2.GetGuildWarWinCount():
            return LGEMiscellaneous.DEFINECONSTANTS.false
        if g1.GetGuildWarLossCount() < g2.GetGuildWarLossCount():
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
        if g1.GetGuildWarLossCount() > g2.GetGuildWarLossCount():
            return LGEMiscellaneous.DEFINECONSTANTS.false
        c = strcmp(g1.GetName(), g2.GetName())
        if c > 0:
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
        return LGEMiscellaneous.DEFINECONSTANTS.false

class FSendWarList:
    def __init__(self, subheader, guild_id1, guild_id2):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.gid1 = 0
        self.gid2 = 0
        self.p = packet_guild()

        self.gid1 = guild_id1
        self.gid2 = guild_id2

        self.p.header = byte(Globals.LG_HEADER_GC_GUILD)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.p.size = sizeof(self.p) + sizeof(uint) * 2
        self.p.subheader = subheader

    def functor_method(self, ch):
        d = ch.GetDesc()

        if d:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            d.BufferedPacket(self.p, sizeof(self.p))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            d.BufferedPacket(self.gid1, sizeof(uint))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            d.Packet(self.gid2, sizeof(uint))
