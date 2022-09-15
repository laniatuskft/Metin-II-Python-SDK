class quest: #this class replaces the original namespace 'quest'
    @staticmethod
    def target_pos(L):
        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()
        iQuestIndex = quest.CQuestManager.instance().GetCurrentPC().GetCurrentQuestIndex()

        if (not lua_isstring(L, 1)) or (not lua_isnumber(L, 2)) or not lua_isnumber(L, 3):
            #lani_err("invalid argument, name: %s, quest_index %d", ch.GetName(LOCALE_LANIATUS), iQuestIndex)
            return 0

        pos = pixel_position_s()

        if not SECTREE_MANAGER.instance().GetMapBasePositionByMapIndex(ch.GetMapIndex(), pos):
            #lani_err("cannot find base position in this map %d", ch.GetMapIndex())
            return 0

        x = pos.x + int(lua_tonumber(L, 2)) * 100
        y = pos.y + int(lua_tonumber(L, 3)) * 100

        CTargetManager.instance().CreateTarget(ch.GetPlayerID(), uint(iQuestIndex), lua_tostring(L, 1), ETargetTypes.TARGET_TYPE_POS, x, y, int(lua_tonumber(L, 4)),lua_tostring(L, 5) if lua_isstring(L, 5) else None,int(lua_tonumber(L, 6)) if lua_isnumber(L, 6) ) else 1)

        return 0

    @staticmethod
    def target_vid(L):
        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()
        iQuestIndex = quest.CQuestManager.instance().GetCurrentPC().GetCurrentQuestIndex()

        if (not lua_isstring(L, 1)) or not lua_isnumber(L, 2):
            #lani_err("invalid argument, name: %s, quest_index %d", ch.GetName(LOCALE_LANIATUS), iQuestIndex)
            return 0


        CTargetManager.instance().CreateTarget(ch.GetPlayerID(), uint(iQuestIndex), lua_tostring(L, 1), ETargetTypes.TARGET_TYPE_VID, int(lua_tonumber(L, 2)), 0, ch.GetMapIndex(),lua_tostring(L, 3) if lua_isstring(L, 3) else None,int(lua_tonumber(L, 4)) if lua_isnumber(L, 4) ) else 1)

        return 0

    @staticmethod
    def target_delete(L):
        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()
        iQuestIndex = quest.CQuestManager.instance().GetCurrentPC().GetCurrentQuestIndex()

        if not lua_isstring(L, 1):
            #lani_err("invalid argument, name: %s, quest_index %d", ch.GetName(LOCALE_LANIATUS), iQuestIndex)
            return 0

        CTargetManager.instance().DeleteTarget(ch.GetPlayerID(), uint(iQuestIndex), lua_tostring(L, 1))

        return 0

    @staticmethod
    def target_clear(L):
        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()
        iQuestIndex = quest.CQuestManager.instance().GetCurrentPC().GetCurrentQuestIndex()

        CTargetManager.instance().DeleteTarget(ch.GetPlayerID(), uint(iQuestIndex), None)

        return 0

    @staticmethod
    def target_id(L):
        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()
        dwQuestIndex = uint(quest.CQuestManager.instance().GetCurrentPC().GetCurrentQuestIndex())

        if not lua_isstring(L, 1):
            #lani_err("invalid argument, name: %s, quest_index %u", ch.GetName(LOCALE_LANIATUS), dwQuestIndex)
            lua_pushnumber(L, 0)
            return 1

        pkEvent = CTargetManager.instance().GetTargetEvent(ch.GetPlayerID(), dwQuestIndex, str(lua_tostring(L, 1)))

        if pkEvent:
            pInfo = if isinstance(pkEvent.info, TargetInfo) else None

            if pInfo is None:
                #lani_err("target_id> <Factor> Null pointer")
                lua_pushnumber(L, 0)
                return 1

            if pInfo.iType == ETargetTypes.TARGET_TYPE_VID:
                lua_pushnumber(L, pInfo.iArg1)
                return 1

        lua_pushnumber(L, 0)
        return 1

    @staticmethod
    def RegisterTargetFunctionTable():
        target_functions = [luaL_reg("pos", target_pos), luaL_reg("vid", target_vid), luaL_reg("npc", target_vid), luaL_reg("pc", target_vid), luaL_reg("delete", target_delete), luaL_reg("clear", target_clear), luaL_reg("id", target_id), luaL_reg(None, None)]

        quest.CQuestManager.instance().AddLuaFunctionTable("target", target_functions)

