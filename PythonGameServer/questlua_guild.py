class quest: #this class replaces the original namespace 'quest'
    @staticmethod
    def guild_around_ranking_string(L):
        q = quest.CQuestManager.instance()
        ch = q.GetCurrentCharacterPtr()
        if ch.GetGuild() is None:
            lua_pushstring(L,"")
        else:
            szBuf = str(['\0' for _ in range(4096+1)])
            temp_ref_szBuf = RefObject(szBuf);
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            CGuildManager.instance().GetAroundRankString(ch.GetGuild().GetID(), temp_ref_szBuf, sizeof(szBuf))
            szBuf = temp_ref_szBuf.arg_value
            lua_pushstring(L, szBuf)
        return 1

    @staticmethod
    def guild_high_ranking_string(L):
        q = quest.CQuestManager.instance()
        ch = q.GetCurrentCharacterPtr()
        dwMyGuild = 0
        if ch.GetGuild():
            dwMyGuild = ch.GetGuild().GetID()

        szBuf = str(['\0' for _ in range(4096+1)])
        temp_ref_szBuf = RefObject(szBuf);
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        CGuildManager.instance().GetHighRankString(dwMyGuild, temp_ref_szBuf, sizeof(szBuf))
        szBuf = temp_ref_szBuf.arg_value
        lua_pushstring(L, szBuf)
        return 1

    @staticmethod
    def guild_get_ladder_point(L):
        q = quest.CQuestManager.instance()
        ch = q.GetCurrentCharacterPtr()
        if ch.GetGuild() is None:
            lua_pushnumber(L, -1)
        else:
            lua_pushnumber(L, ch.GetGuild().GetLadderPoint())
        return 1

    @staticmethod
    def guild_get_rank(L):
        q = quest.CQuestManager.instance()
        ch = q.GetCurrentCharacterPtr()

        if ch.GetGuild() is None:
            lua_pushnumber(L, -1)
        else:
            lua_pushnumber(L, CGuildManager.instance().GetRank(ch.GetGuild()))
        return 1

    @staticmethod
    def guild_is_war(L):
        if not lua_isnumber(L, 1):
            #lani_err("invalid argument")
            return 0

        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()

        if ch.GetGuild() is not None and ch.GetGuild().UnderWar(lua_tonumber(L, 1)):
            lua_pushboolean(L, ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
        else:
            lua_pushboolean(L, LGEMiscellaneous.DEFINECONSTANTS.false)

        return 1

    @staticmethod
    def guild_name(L):
        if not lua_isnumber(L, 1):
            #lani_err("invalid argument")
            return 0

        pkGuild = CGuildManager.instance().FindGuild(lua_tonumber(L, 1))

        if pkGuild:
            lua_pushstring(L, pkGuild.GetName())
        else:
            lua_pushstring(L, "")

        return 1

    @staticmethod
    def guild_level(L):
        luaL_checknumber(L, 1)

        pkGuild = CGuildManager.instance().FindGuild(lua_tonumber(L, 1))

        if pkGuild:
            lua_pushnumber(L, pkGuild.GetLevel())
        else:
            lua_pushnumber(L, 0)

        return 1

    @staticmethod
    def guild_war_enter(L):
        if not lua_isnumber(L, 1):
            #lani_err("invalid argument")
            return 0

        q = quest.CQuestManager.instance()
        ch = q.GetCurrentCharacterPtr()

        if ch.GetGuild():
            ch.GetGuild().GuildWarEntryAccept(lua_tonumber(L, 1), ch)

        return 0

    @staticmethod
    def guild_get_any_war(L):
        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()

        if ch.GetGuild():
            lua_pushnumber(L, ch.GetGuild().UnderAnyWar(GUILD_WAR_TYPE_MAX_NUM))
        else:
            lua_pushnumber(L, 0)

        return 1

    @staticmethod
    def guild_get_name(L):
        if not lua_isnumber(L, 1):
            lua_pushstring(L, "")
            return 1

        pkGuild = CGuildManager.instance().FindGuild(lua_tonumber(L, 1))

        if pkGuild:
            lua_pushstring(L, pkGuild.GetName())
        else:
            lua_pushstring(L, "")

        return 1

    @staticmethod
    def guild_war_bet(L):
        if (not lua_isnumber(L, 1)) or (not lua_isnumber(L, 2)) or not lua_isnumber(L, 3):
            #lani_err("invalid argument")
            return 0

        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()

        p = TPacketGDGuildWarBet()

        p.dwWarID = lua_tonumber(L, 1)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        strncpy_s(p.szLogin, sizeof(p.szLogin), ch.GetDesc().GetAccountTable().login, _TRUNCATE)
        p.dwGuild = lua_tonumber(L, 2)
        p.lldGold = int(lua_tonumber(L, 3))

        #sys_log(0, "GUILD_WAR_BET: %s login %s war_id %u guild %u gold %lld", ch.GetName(LOCALE_LANIATUS), p.szLogin, p.dwWarID, p.dwGuild, p.lldGold)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        db_clientdesc.DBPacket(Globals.LG_HEADER_GD_GUILD_WAR_BET, 0, p, sizeof(p))
        return 0

    @staticmethod
    def guild_is_bet(L):
        if not lua_isnumber(L, 1):
            #lani_err("invalid argument")
            lua_pushboolean(L, ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
            return 1

        bBet = CGuildManager.instance().IsBet(lua_tonumber(L, 1), quest.CQuestManager.instance().GetCurrentCharacterPtr().GetDesc().GetAccountTable().login)

        lua_pushboolean(L, bBet)
        return 1

    @staticmethod
    def guild_get_warp_war_list(L):
        f = FBuildLuaGuildWarList(L)
        CGuildManager.instance().for_each_war(f.functor_method)
        return 1

    @staticmethod
    def guild_get_reserve_war_table(L):
        con = CGuildManager.instance().GetReserveWarRef()

        LaniatusDefVariables = 0
        it = con.begin()

        #sys_log(0, "con.size(): %d", len(con))
        lua_newtable(L)

        while it is not con.end():
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: SGuildReserve * p = &(*(it++))->data;
            p = &(*(it)).data
            it += 1

            if p.bType != EGuildWarType.GUILD_WAR_TYPE_BATTLE:
                continue

            lua_newtable(L)

            #sys_log(0, "con.size(): %u %u %u handi %d", p.dwID, p.dwGuildFrom, p.dwGuildTo, p.lHandicap)
            lua_pushnumber(L, p.dwID)
            lua_rawseti(L, -2, 1)

            if p.lPowerFrom > p.lPowerTo:
                lua_pushnumber(L, p.dwGuildFrom)
            else:
                lua_pushnumber(L, p.dwGuildTo)

            lua_rawseti(L, -2, 2)

            if p.lPowerFrom > p.lPowerTo:
                lua_pushnumber(L, p.dwGuildTo)
            else:
                lua_pushnumber(L, p.dwGuildFrom)

            lua_rawseti(L, -2, 3)

            lua_pushnumber(L, p.lHandicap)
            lua_rawseti(L, -2, 4)
            LaniatusDefVariables += 1
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: lua_rawseti(L, -2, ++i);
            lua_rawseti(L, -2, i)

        return 1

    @staticmethod
    def guild_get_member_count(L):
        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()

        if ch is None:
            lua_pushnumber(L, 0)
            return 1

        pGuild = ch.GetGuild()

        if pGuild is None:
            lua_pushnumber(L, 0)
            return 1

        lua_pushnumber(L, pGuild.GetMemberCount())

        return 1

    @staticmethod
    def guild_change_master(L):
        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()

        pGuild = ch.GetGuild()

        if pGuild is not None:
            if pGuild.GetMasterPID() == ch.GetPlayerID():
                if lua_isstring(L, 1) == LGEMiscellaneous.DEFINECONSTANTS.false:
                    lua_pushnumber(L, 0)
                else:
                    ret = pGuild.ChangeMasterTo(pGuild.GetMemberPID(lua_tostring(L, 1)))

                    lua_pushnumber(L,2 if ret == LGEMiscellaneous.DEFINECONSTANTS.false else 3)
            else:
                lua_pushnumber(L, 1)
        else:
            lua_pushnumber(L, 4)

        return 1

    @staticmethod
    def guild_change_master_with_limit(L):
        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()

        pGuild = ch.GetGuild()

        if pGuild is not None:
            if pGuild.GetMasterPID() == ch.GetPlayerID():
                if lua_isstring(L, 1) == LGEMiscellaneous.DEFINECONSTANTS.false:
                    lua_pushnumber(L, 0)
                else:
                    pNewMaster = CHARACTER_MANAGER.instance().FindPC(lua_tostring(L,1))

                    if pNewMaster is not None:
                        if pNewMaster.GetLevel() < lua_tonumber(L, 2):
                            lua_pushnumber(L, 6)
                        else:
                            nBeOtherLeader = pNewMaster.GetQuestFlag("change_guild_master.be_other_leader")
                            quest.CQuestManager.instance().GetPC(ch.GetPlayerID())

                            if lua_toboolean(L, 6) == ((not LGEMiscellaneous.DEFINECONSTANTS.false)):
                                nBeOtherLeader = 0

                            if nBeOtherLeader > get_global_time():
                                lua_pushnumber(L, 7)
                            else:
                                ret = pGuild.ChangeMasterTo(pGuild.GetMemberPID(lua_tostring(L, 1)))

                                if ret == LGEMiscellaneous.DEFINECONSTANTS.false:
                                    lua_pushnumber(L, 2)
                                else:
                                    lua_pushnumber(L, 3)

                                    pNewMaster.SetQuestFlag("change_guild_master.be_other_leader", 0)
                                    pNewMaster.SetQuestFlag("change_guild_master.be_other_member", 0)
                                    pNewMaster.SetQuestFlag("change_guild_master.resign_limit", int(lua_tonumber(L, 3)))

                                    ch.SetQuestFlag("change_guild_master.be_other_leader", int(lua_tonumber(L, 4)))
                                    ch.SetQuestFlag("change_guild_master.be_other_member", int(lua_tonumber(L, 5)))
                                    ch.SetQuestFlag("change_guild_master.resign_limit", 0)
                    else:
                        lua_pushnumber(L, 5)
            else:
                lua_pushnumber(L, 1)
        else:
            lua_pushnumber(L, 4)

        return 1

    @staticmethod
    def RegisterGuildFunctionTable():
        guild_functions = [luaL_reg("get_rank", guild_get_rank), luaL_reg("get_ladder_point", guild_get_ladder_point), luaL_reg("high_ranking_string", guild_high_ranking_string), luaL_reg("around_ranking_string", guild_around_ranking_string), luaL_reg("name", guild_name), luaL_reg("level", guild_level), luaL_reg("is_war", guild_is_war), luaL_reg("war_enter", guild_war_enter), luaL_reg("get_any_war", guild_get_any_war), luaL_reg("get_reserve_war_table", guild_get_reserve_war_table), luaL_reg("get_name", guild_get_name), luaL_reg("war_bet", guild_war_bet), luaL_reg("is_bet", guild_is_bet), luaL_reg("get_warp_war_list", guild_get_warp_war_list), luaL_reg("get_member_count", guild_get_member_count), luaL_reg("change_master", guild_change_master), luaL_reg("change_master_with_limit", guild_change_master_with_limit), luaL_reg(None, None)]

        quest.CQuestManager.instance().AddLuaFunctionTable("guild", guild_functions)

