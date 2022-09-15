class quest: #this class replaces the original namespace 'quest'
    @staticmethod
    def npc_open_shop(L):
        iShopVnum = 0

        if lua_gettop(L) == 1:
            if lua_isnumber(L, 1):
                iShopVnum = int(lua_tonumber(L, 1))

        if quest.CQuestManager.instance().GetCurrentNPCCharacterPtr():
            CShopManager.instance().StartShopping(quest.CQuestManager.instance().GetCurrentCharacterPtr(), quest.CQuestManager.instance().GetCurrentNPCCharacterPtr(), iShopVnum)
        return 0

    @staticmethod
    def npc_is_pc(L):
        q = quest.CQuestManager.instance()
        npc = q.GetCurrentNPCCharacterPtr()
        if npc is not None and npc.IsPC():
            lua_pushboolean(L, 1)
        else:
            lua_pushboolean(L, 0)
        return 1

    @staticmethod
    def npc_get_empire(L):
        q = quest.CQuestManager.instance()
        npc = q.GetCurrentNPCCharacterPtr()
        if npc:
            lua_pushnumber(L, npc.GetEmpire())
        else:
            lua_pushnumber(L, 0)
        return 1

    @staticmethod
    def npc_get_race(L):
        lua_pushnumber(L, quest.CQuestManager.instance().GetCurrentNPCRace())
        return 1

    @staticmethod
    def npc_get_guild(L):
        q = quest.CQuestManager.instance()
        npc = q.GetCurrentNPCCharacterPtr()
        pGuild = None
        if npc:
            pGuild = npc.GetGuild()

        lua_pushnumber(L,pGuild.GetID() if pGuild is not None else 0)
        return 1

    @staticmethod
    def npc_get_remain_LG_SKILL_book_count(L):
        npc = quest.CQuestManager.instance().GetCurrentNPCCharacterPtr()
        if npc is None or npc.IsPC() or npc.GetRaceNum() != xmas.MOB_SANTA_VNUM:
            lua_pushnumber(L, 0)
            return 1
        lua_pushnumber(L, MAX(0, npc.GetPoint(EPointTypes.LG_POINT_ATT_GRADE_BONUS)))
        return 1

    @staticmethod
    def npc_dec_remain_LG_SKILL_book_count(L):
        npc = quest.CQuestManager.instance().GetCurrentNPCCharacterPtr()
        if npc is None or npc.IsPC() or npc.GetRaceNum() != xmas.MOB_SANTA_VNUM:
            return 0
        npc.SetPoint(EPointTypes.LG_POINT_ATT_GRADE_BONUS, MAX(0, npc.GetPoint(EPointTypes.LG_POINT_ATT_GRADE_BONUS)-1))
        return 0

    @staticmethod
    def npc_get_remain_hairdye_count(L):
        npc = quest.CQuestManager.instance().GetCurrentNPCCharacterPtr()
        if npc is None or npc.IsPC() or npc.GetRaceNum() != xmas.MOB_SANTA_VNUM:
            lua_pushnumber(L, 0)
            return 1
        lua_pushnumber(L, MAX(0, npc.GetPoint(EPointTypes.LG_POINT_DEF_GRADE_BONUS)))
        return 1

    @staticmethod
    def npc_dec_remain_hairdye_count(L):
        npc = quest.CQuestManager.instance().GetCurrentNPCCharacterPtr()
        if npc is None or npc.IsPC() or npc.GetRaceNum() != xmas.MOB_SANTA_VNUM:
            return 0
        npc.SetPoint(EPointTypes.LG_POINT_DEF_GRADE_BONUS, MAX(0, npc.GetPoint(EPointTypes.LG_POINT_DEF_GRADE_BONUS)-1))
        return 0

    @staticmethod
    def npc_is_quest(L):
        q = quest.CQuestManager.instance()
        npc = q.GetCurrentNPCCharacterPtr()

        if npc:
            r_st = q.GetCurrentQuestName()

            if q.GetQuestIndexByName(r_st) == npc.GetQuestBy():
                lua_pushboolean(L, 1)
                return 1

        lua_pushboolean(L, 0)
        return 1

    @staticmethod
    def npc_kill(L):
        q = quest.CQuestManager.instance()
        ch = q.GetCurrentCharacterPtr()
        npc = q.GetCurrentNPCCharacterPtr()

        ch.SetQuestNPCID(0)
        if npc:
            npc.Dead(NULL, DefineConstants.false)
        return 0

    @staticmethod
    def npc_purge(L):
        q = quest.CQuestManager.instance()
        ch = q.GetCurrentCharacterPtr()
        npc = q.GetCurrentNPCCharacterPtr()

        ch.SetQuestNPCID(0)
        if npc:
            CHARACTER_MANAGER.instance().DestroyCharacter(npc)
        return 0

    @staticmethod
    def npc_is_near(L):
        q = quest.CQuestManager.instance()
        ch = q.GetCurrentCharacterPtr()
        npc = q.GetCurrentNPCCharacterPtr()

        dist = 10

        if lua_isnumber(L, 1):
            dist = lua_tonumber(L, 1)

        if ch is None or npc is None:
            lua_pushboolean(L, LGEMiscellaneous.DEFINECONSTANTS.false)
        else:
            lua_pushboolean(L, Globals.DISTANCE_APPROX(ch.GetX() - npc.GetX(), ch.GetY() - npc.GetY()) < dist *100)

        return 1

    @staticmethod
    def npc_is_near_vid(L):
        if not lua_isnumber(L, 1):
            #lani_err("invalid vid")
            lua_pushboolean(L, 0)
            return 1

        q = quest.CQuestManager.instance()
        ch = CHARACTER_MANAGER.instance().Find(lua_tonumber(L, 1))
        npc = q.GetCurrentNPCCharacterPtr()

        dist = 10

        if lua_isnumber(L, 2):
            dist = lua_tonumber(L, 2)

        if ch is None or npc is None:
            lua_pushboolean(L, LGEMiscellaneous.DEFINECONSTANTS.false)
        else:
            lua_pushboolean(L, Globals.DISTANCE_APPROX(ch.GetX() - npc.GetX(), ch.GetY() - npc.GetY()) < dist *100)

        return 1

    @staticmethod
    def npc_unlock(L):
        q = quest.CQuestManager.instance()
        ch = q.GetCurrentCharacterPtr()
        npc = q.GetCurrentNPCCharacterPtr()

        if npc is not None:
            if npc.IsPC():
                return 0

            if npc.GetQuestNPCID() == ch.GetPlayerID():
                npc.SetQuestNPCID(0)
        return 0

    @staticmethod
    def npc_lock(L):
        q = quest.CQuestManager.instance()
        ch = q.GetCurrentCharacterPtr()
        npc = q.GetCurrentNPCCharacterPtr()

        if npc is None or npc.IsPC():
            lua_pushboolean(L, ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
            return 1

        if npc.GetQuestNPCID() == 0 or npc.GetQuestNPCID() == ch.GetPlayerID():
            npc.SetQuestNPCID(ch.GetPlayerID())
            lua_pushboolean(L, ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
        else:
            lua_pushboolean(L, LGEMiscellaneous.DEFINECONSTANTS.false)

        return 1

    @staticmethod
    def npc_get_leader_vid(L):
        q = quest.CQuestManager.instance()
        npc = q.GetCurrentNPCCharacterPtr()

        party = npc.GetParty()

        if party is None:
            #lani_err("npc_get_leader_vid: Function triggered without party")
            return 1

        leader = party.GetLeader()

        if leader:
            lua_pushnumber(L, leader.GetVID())
        else:
            lua_pushnumber(L, 0)


        return 1

    @staticmethod
    def npc_get_vid(L):
        q = quest.CQuestManager.instance()
        npc = q.GetCurrentNPCCharacterPtr()

        lua_pushnumber(L, npc.GetVID())


        return 1

    @staticmethod
    def npc_get_vid_attack_mul(L):
        q = quest.CQuestManager.instance()

        vid = lua_tonumber(L, 1)
        targetChar = CHARACTER_MANAGER.instance().Find(vid)

        if targetChar:
            lua_pushnumber(L, targetChar.GetAttMul())
        else:
            lua_pushnumber(L, 0)


        return 1

    @staticmethod
    def npc_set_vid_attack_mul(L):
        q = quest.CQuestManager.instance()

        vid = lua_tonumber(L, 1)
        attack_mul = lua_tonumber(L, 2)

        targetChar = CHARACTER_MANAGER.instance().Find(vid)

        if targetChar:
            targetChar.SetAttMul(lua_Number(attack_mul))

        return 0

    @staticmethod
    def npc_get_vid_damage_mul(L):
        q = quest.CQuestManager.instance()

        vid = lua_tonumber(L, 1)
        targetChar = CHARACTER_MANAGER.instance().Find(vid)

        if targetChar:
            lua_pushnumber(L, targetChar.GetDamMul())
        else:
            lua_pushnumber(L, 0)


        return 1

    @staticmethod
    def npc_set_vid_damage_mul(L):
        q = quest.CQuestManager.instance()

        vid = lua_tonumber(L, 1)
        damage_mul = lua_tonumber(L, 2)

        targetChar = CHARACTER_MANAGER.instance().Find(vid)

        if targetChar:
            targetChar.SetDamMul(lua_Number(damage_mul))

        return 0

    @staticmethod
    def RegisterNPCFunctionTable():
        npc_functions = [luaL_reg("getrace", npc_get_race), luaL_reg("get_race", npc_get_race), luaL_reg("open_shop", npc_open_shop), luaL_reg("get_empire", npc_get_empire), luaL_reg("is_pc", npc_is_pc), luaL_reg("is_quest", npc_is_quest), luaL_reg("kill", npc_kill), luaL_reg("purge", npc_purge), luaL_reg("is_near", npc_is_near), luaL_reg("is_near_vid", npc_is_near_vid), luaL_reg("lock", npc_lock), luaL_reg("unlock", npc_unlock), luaL_reg("get_guild", npc_get_guild), luaL_reg("get_leader_vid", npc_get_leader_vid), luaL_reg("get_vid", npc_get_vid), luaL_reg("get_vid_attack_mul", npc_get_vid_attack_mul), luaL_reg("set_vid_attack_mul", npc_set_vid_attack_mul), luaL_reg("get_vid_damage_mul", npc_get_vid_damage_mul), luaL_reg("set_vid_damage_mul", npc_set_vid_damage_mul), luaL_reg("get_remain_LG_SKILL_book_count", npc_get_remain_LG_SKILL_book_count), luaL_reg("dec_remain_LG_SKILL_book_count", npc_dec_remain_LG_SKILL_book_count), luaL_reg("get_remain_hairdye_count", npc_get_remain_hairdye_count), luaL_reg("dec_remain_hairdye_count", npc_dec_remain_hairdye_count), luaL_reg(None, None)]

        quest.CQuestManager.instance().AddLuaFunctionTable("npc", npc_functions)
