class quest: #this class replaces the original namespace 'quest'
    @staticmethod
    def pet_summon(L):
        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()
        petSystem = ch.GetPetSystem()
        pItem = quest.CQuestManager.instance().GetCurrentItem()
        if ch is None or petSystem is None or pItem is None:
            lua_pushnumber(L, 0)
            return 1

        if None is petSystem:
            lua_pushnumber(L, 0)
            return 1

        mobVnum = uint(lua_tonumber(L, 1) if lua_isnumber(L, 1) else 0)

        petName = lua_tostring(L, 2) if lua_isstring(L, 2) else None

        bFromFar = lua_toboolean(L, 3) if lua_isboolean(L, 3) else LGEMiscellaneous.DEFINECONSTANTS.false

        pet = petSystem.Summon(mobVnum, pItem, petName, bFromFar, CPetActor.EPetOption_Followable | CPetActor.EPetOption_Summonable)

        if pet is not None:
            lua_pushnumber(L, pet.GetVID())
        else:
            lua_pushnumber(L, 0)

        return 1

    @staticmethod
    def pet_unsummon(L):
        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()
        petSystem = ch.GetPetSystem()

        if None is petSystem:
            return 0

        mobVnum = uint(lua_tonumber(L, 1) if lua_isnumber(L, 1) else 0)

        petSystem.Unsummon(mobVnum, DefineConstants.false)
        return 1

    @staticmethod
    def pet_count_summoned(L):
        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()
        petSystem = ch.GetPetSystem()

        count = 0

        if None is not petSystem:
            count = petSystem.CountSummoned()

        lua_pushnumber(L, count)

        return 1

    @staticmethod
    def pet_is_summon(L):
        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()
        petSystem = ch.GetPetSystem()

        if None is petSystem:
            return 0

        mobVnum = uint(lua_tonumber(L, 1) if lua_isnumber(L, 1) else 0)

        petActor = petSystem.GetByVnum(mobVnum)

        if None is petActor:
            lua_pushboolean(L, LGEMiscellaneous.DEFINECONSTANTS.false)
        else:
            lua_pushboolean(L, petActor.IsSummoned())

        return 1

    @staticmethod
    def pet_spawn_effect(L):
        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()
        petSystem = ch.GetPetSystem()

        if None is petSystem:
            return 0

        mobVnum = uint(lua_tonumber(L, 1) if lua_isnumber(L, 1) else 0)

        petActor = petSystem.GetByVnum(mobVnum)
        if None is petActor:
            return 0
        pet_ch = petActor.GetCharacter()
        if None is pet_ch:
            return 0

        if lua_isstring(L, 2):
            pet_ch.SpecificEffectPacket(lua_tostring(L, 2))
        return 0

    @staticmethod
    def RegisterPetFunctionTable():
        pet_functions = [luaL_reg("summon", pet_summon), luaL_reg("unsummon", pet_unsummon), luaL_reg("is_summon", pet_is_summon), luaL_reg("count_summoned", pet_count_summoned), luaL_reg("spawn_effect", pet_spawn_effect), luaL_reg(None, None)]

        quest.CQuestManager.instance().AddLuaFunctionTable("pet", pet_functions)
