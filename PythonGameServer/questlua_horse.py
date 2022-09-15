class quest: #this class replaces the original namespace 'quest'
    @staticmethod
    def horse_is_riding(L):
        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()

        if ch.IsHorseRiding():
            lua_pushnumber(L, 1)
        else:
            lua_pushnumber(L, 0)

        return 1

    @staticmethod
    def horse_is_summon(L):
        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()

        if None is not ch:
            lua_pushboolean(L,((not LGEMiscellaneous.DEFINECONSTANTS.false)) if (ch.GetHorse() is not None) else LGEMiscellaneous.DEFINECONSTANTS.false)
        else:
            lua_pushboolean(L, LGEMiscellaneous.DEFINECONSTANTS.false)

        return 1

    @staticmethod
    def horse_ride(L):
        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()
        ch.StartRiding()
        return 0

    @staticmethod
    def horse_unride(L):
        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()
        ch.StopRiding()
        return 0

    @staticmethod
    def horse_summon(L):
        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()
        bFromFar = lua_toboolean(L, 1) if lua_isboolean(L, 1) else LGEMiscellaneous.DEFINECONSTANTS.false
        horseVnum = uint(lua_tonumber(L, 2) if lua_isnumber(L, 2) else 0)

        name = lua_tostring(L, 3) if lua_isstring(L, 3) else None
        ch.HorseSummon(((not LGEMiscellaneous.DEFINECONSTANTS.false)), bFromFar, horseVnum, name)
        return 0

    @staticmethod
    def horse_unsummon(L):
        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()
        ch.HorseSummon(LGEMiscellaneous.DEFINECONSTANTS.false, DefineConstants.false, 0, 0)
        return 0

    @staticmethod
    def horse_is_mine(L):
        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()
        horse = quest.CQuestManager.instance().GetCurrentNPCCharacterPtr()

        lua_pushboolean(L, horse and horse.GetRider() is ch)
        return 1

    @staticmethod
    def horse_set_level(L):
        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()

        if not lua_isnumber(L, 1):
            return 0

        newlevel = MINMAX(0, int(lua_tonumber(L, 1)), Globals.HORSE_MAX_LEVEL)
        ch.SetHorseLevel(newlevel)
        ch.ComputePoints()
        ch.SkillLevelPacket()
        return 0

    @staticmethod
    def horse_get_level(L):
        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()
        lua_pushnumber(L, ch.GetHorseLevel())
        return 1

    @staticmethod
    def horse_advance(L):
        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()

        if ch.GetHorseLevel() >= Globals.HORSE_MAX_LEVEL:
            return 0

        ch.SetHorseLevel(ch.GetHorseLevel() + 1)
        ch.ComputePoints()
        ch.SkillLevelPacket()
        return 0

    @staticmethod
    def horse_get_health(L):
        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()

        if ch.GetHorseLevel() != 0:
            lua_pushnumber(L, ch.GetHorseHealth())
        else:
            lua_pushnumber(L, 0)

        return 1

    @staticmethod
    def horse_get_health_pct(L):
        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        pct = MINMAX(0, ch.GetHorseHealth() * 100 / ch.GetHorseMaxHealth(), 100)
        #sys_log(1, "horse.get_health_pct %d", pct)

        if ch.GetHorseLevel() != 0:
            lua_pushnumber(L, pct)
        else:
            lua_pushnumber(L, 0)

        return 1

    @staticmethod
    def horse_get_stamina(L):
        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()

        if ch.GetHorseLevel() != 0:
            lua_pushnumber(L, ch.GetHorseStamina())
        else:
            lua_pushnumber(L, 0)

        return 1

    @staticmethod
    def horse_get_stamina_pct(L):
        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        pct = MINMAX(0, ch.GetHorseStamina() * 100 / ch.GetHorseMaxStamina(), 100)
        #sys_log(1, "horse.get_stamina_pct %d", pct)

        if ch.GetHorseLevel() != 0:
            lua_pushnumber(L, pct)
        else:
            lua_pushnumber(L, 0)

        return 1

    @staticmethod
    def horse_get_grade(L):
        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()
        lua_pushnumber(L, ch.GetHorseGrade())
        return 1

    @staticmethod
    def horse_is_dead(L):
        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()
        lua_pushboolean(L, ch.GetHorseHealth()<=0)
        return 1

    @staticmethod
    def horse_revive(L):
        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()
        if ch.GetHorseLevel() > 0 and ch.GetHorseHealth() <= 0:
            ch.ReviveHorse()
        return 0

    @staticmethod
    def horse_feed(L):
        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()
        if ch.GetHorseLevel() > 0 and ch.GetHorseHealth() > 0:
            ch.FeedHorse()
        return 0

    @staticmethod
    def horse_set_name(L):
        if lua_isstring(L, -1) != ((not LGEMiscellaneous.DEFINECONSTANTS.false)):
            return 0

        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()

        if ch.GetHorseLevel() > 0:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to pointers to value types:
#ORIGINAL METINII C CODE: const char* pHorseName = lua_tostring(L, -1);
            pHorseName = lua_tostring(L, -1)

            if pHorseName is None or check_name(pHorseName) == 0:
                lua_pushnumber(L, 1)
            else:
                nHorseNameDuration = 60 *5 if test_server == ((not LGEMiscellaneous.DEFINECONSTANTS.false)) else 60 *60 *24 *30

                ch.SetQuestFlag("horse_name.valid_till", get_global_time() + nHorseNameDuration)
                ch.AddAffect(LaniatusEAffectTypes.LANIA_AFFECT_HORSE_NAME, 0, 0, 0, ((nHorseNameDuration) * passes_per_sec), 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), DefineConstants.false)

                CHorseNameManager.instance().UpdateHorseName(ch.GetPlayerID(), lua_tostring(L, -1), ((not LGEMiscellaneous.DEFINECONSTANTS.false)))

                ch.HorseSummon(LGEMiscellaneous.DEFINECONSTANTS.false, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), 0, 0)
                ch.HorseSummon(((not LGEMiscellaneous.DEFINECONSTANTS.false)), ((not LGEMiscellaneous.DEFINECONSTANTS.false)), 0, 0)

                lua_pushnumber(L, 2)
        else:
            lua_pushnumber(L, 0)

        return 1

    @staticmethod
    def horse_get_name(L):
        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()

        if ch is not None:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to pointers to value types:
#ORIGINAL METINII C CODE: const char* pHorseName = CHorseNameManager::instance().GetHorseName(ch->GetPlayerID());
            pHorseName = CHorseNameManager.instance().GetHorseName(ch.GetPlayerID())

            if pHorseName is not None:
                lua_pushstring(L, pHorseName)
                return 1

        lua_pushstring(L, "")

        return 1

    @staticmethod
    def RegisterHorseFunctionTable():
        horse_functions = [luaL_reg("is_mine", horse_is_mine), luaL_reg("is_riding", horse_is_riding), luaL_reg("is_summon", horse_is_summon), luaL_reg("ride", horse_ride), luaL_reg("unride", horse_unride), luaL_reg("summon", horse_summon), luaL_reg("unsummon", horse_unsummon), luaL_reg("advance", horse_advance), luaL_reg("get_level", horse_get_level), luaL_reg("set_level", horse_set_level), luaL_reg("get_health", horse_get_health), luaL_reg("get_health_pct", horse_get_health_pct), luaL_reg("get_stamina", horse_get_stamina), luaL_reg("get_stamina_pct",horse_get_stamina_pct), luaL_reg("get_grade", horse_get_grade), luaL_reg("is_dead", horse_is_dead), luaL_reg("revive", horse_revive), luaL_reg("feed", horse_feed), luaL_reg("set_name", horse_set_name), luaL_reg("get_name", horse_get_name), luaL_reg(None, None)]

        quest.CQuestManager.instance().AddLuaFunctionTable("horse", horse_functions)




