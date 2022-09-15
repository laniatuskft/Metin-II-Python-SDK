class quest: #this class replaces the original namespace 'quest'
    @staticmethod
    def affect_add(L):
        if (not lua_isnumber(L, 1)) or (not lua_isnumber(L, 2)) or not lua_isnumber(L, 3):
            #lani_err("invalid argument")
            return 0

        q = quest.CQuestManager.instance()

        applyOn = byte(int(lua_tonumber(L, 1)))

        ch = q.GetCurrentCharacterPtr()

        if applyOn >= EApplyTypes.MAX_APPLY_NUM or applyOn < 1:
            #lani_err("apply is out of range : %d", applyOn)
            return 0

        if ch.FindAffect(LaniatusEAffectTypes.LANIA_AFFECT_QUEST_START_IDX, applyOn):
            return 0

        value = int(lua_tonumber(L, 2))
        duration = int(lua_tonumber(L, 3))

        ch.AddAffect(LaniatusEAffectTypes.LANIA_AFFECT_QUEST_START_IDX, aApplyInfo[applyOn].bPointType, value, 0, duration, 0, LGEMiscellaneous.DEFINECONSTANTS.false, DefineConstants.false)

        return 0

    @staticmethod
    def affect_remove(L):
        q = quest.CQuestManager.instance()
        iType = None

        if lua_isnumber(L, 1):
            iType = int(lua_tonumber(L, 1))

            if iType == 0:
                iType = q.GetCurrentPC().GetCurrentQuestIndex() + int(LaniatusEAffectTypes.LANIA_AFFECT_QUEST_START_IDX)
        else:
            iType = q.GetCurrentPC().GetCurrentQuestIndex() + int(LaniatusEAffectTypes.LANIA_AFFECT_QUEST_START_IDX)

        q.GetCurrentCharacterPtr().RemoveAffect(iType)

        return 0

    @staticmethod
    def affect_remove_bad(L):
        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()
        ch.RemoveBadAffect()
        return 0

    @staticmethod
    def affect_remove_good(L):
        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()
        ch.RemoveGoodAffect()
        return 0

    @staticmethod
    def affect_add_hair(L):
        if (not lua_isnumber(L, 1)) or (not lua_isnumber(L, 2)) or not lua_isnumber(L, 3):
            #lani_err("invalid argument")
            return 0

        q = quest.CQuestManager.instance()

        applyOn = byte(int(lua_tonumber(L, 1)))

        ch = q.GetCurrentCharacterPtr()

        if applyOn >= EApplyTypes.MAX_APPLY_NUM or applyOn < 1:
            #lani_err("apply is out of range : %d", applyOn)
            return 0

        value = int(lua_tonumber(L, 2))
        duration = int(lua_tonumber(L, 3))

        ch.AddAffect(LaniatusEAffectTypes.LANIA_AFFECT_HAIR, aApplyInfo[applyOn].bPointType, value, 0, duration, 0, LGEMiscellaneous.DEFINECONSTANTS.false, DefineConstants.false)

        return 0

    @staticmethod
    def affect_remove_hair(L):
        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()

        pkAff = ch.FindAffect(LaniatusEAffectTypes.LANIA_AFFECT_HAIR, APPLY_NONE)

        if pkAff is not None:
            lua_pushnumber(L, pkAff.lDuration)
            ch.RemoveAffect(pkAff)
        else:
            lua_pushnumber(L, 0)

        return 1

    @staticmethod
    def affect_get_apply_on(L):
        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()

        if not lua_isnumber(L, 1):
            #lani_err("invalid argument")
            return 0

        affectType = lua_tonumber(L, 1)

        pkAff = ch.FindAffect(affectType, APPLY_NONE)

        if pkAff is not None:
            lua_pushnumber(L, pkAff.bApplyOn)
        else:
            lua_pushnil(L)

        return 1


    @staticmethod
    def affect_add_collect(L):
        if (not lua_isnumber(L, 1)) or (not lua_isnumber(L, 2)) or not lua_isnumber(L, 3):
            #lani_err("invalid argument")
            return 0

        q = quest.CQuestManager.instance()

        applyOn = byte(int(lua_tonumber(L, 1)))

        ch = q.GetCurrentCharacterPtr()

        if applyOn >= EApplyTypes.MAX_APPLY_NUM or applyOn < 1:
            #lani_err("apply is out of range : %d", applyOn)
            return 0

        value = int(lua_tonumber(L, 2))
        duration = int(lua_tonumber(L, 3))

        ch.AddAffect(LaniatusEAffectTypes.LANIA_AFFECT_COLLECT, aApplyInfo[applyOn].bPointType, value, 0, duration, 0, LGEMiscellaneous.DEFINECONSTANTS.false, DefineConstants.false)

        return 0

    @staticmethod
    def affect_add_collect_point(L):
        if (not lua_isnumber(L, 1)) or (not lua_isnumber(L, 2)) or not lua_isnumber(L, 3):
            #lani_err("invalid argument")
            return 0

        q = quest.CQuestManager.instance()

        LG_POINT_type = byte(int(lua_tonumber(L, 1)))

        ch = q.GetCurrentCharacterPtr()

        if LG_POINT_type >= LGEMiscellaneous.LG_POINT_MAX_NUM or LG_POINT_type < 1:
            #lani_err("point is out of range : %d", LG_POINT_type)
            return 0

        value = int(lua_tonumber(L, 2))
        duration = int(lua_tonumber(L, 3))

        ch.AddAffect(LaniatusEAffectTypes.LANIA_AFFECT_COLLECT, LG_POINT_type, value, 0, duration, 0, LGEMiscellaneous.DEFINECONSTANTS.false, DefineConstants.false)

        return 0

    @staticmethod
    def affect_remove_collect(L):
        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()

        if ch is not None:
            bApply = byte(int(lua_tonumber(L, 1)))

            if bApply >= EApplyTypes.MAX_APPLY_NUM:
                return 0

            bApply = aApplyInfo[bApply].bPointType
            value = int(lua_tonumber(L, 2))

            rList = ch.GetAffectContainer()
            pAffect = None

            iter = rList.begin()
            while iter is not rList.end():
                pAffect = *iter

                if pAffect.dwType == LaniatusEAffectTypes.LANIA_AFFECT_COLLECT:
                    if pAffect.bApplyOn == bApply and pAffect.lApplyValue == value:
                        break

                pAffect = None
                iter += 1

            if pAffect is not None:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no equivalent to 'const_cast' in Python:
                ch.RemoveAffect(const_cast<LaniaCAffects>(pAffect))

        return 0

    @staticmethod
    def affect_remove_all_collect(L):
        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()

        if ch is not None:
            ch.RemoveAffect(LaniatusEAffectTypes.LANIA_AFFECT_COLLECT)

        return 0

    @staticmethod
    def RegisterAffectFunctionTable():
        affect_functions = [luaL_reg("add", affect_add), luaL_reg("remove", affect_remove), luaL_reg("remove_bad", affect_remove_bad), luaL_reg("remove_good", affect_remove_good), luaL_reg("add_hair", affect_add_hair), luaL_reg("remove_hair", affect_remove_hair), luaL_reg("add_collect", affect_add_collect), luaL_reg("add_collect_point", affect_add_collect_point), luaL_reg("remove_collect", affect_remove_collect), luaL_reg("remove_all_collect", affect_remove_all_collect), luaL_reg("get_apply_on", affect_get_apply_on), luaL_reg(None, None)]

        quest.CQuestManager.instance().AddLuaFunctionTable("affect", affect_functions)
