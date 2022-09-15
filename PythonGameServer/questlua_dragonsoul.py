class quest: #this class replaces the original namespace 'quest'
    @staticmethod
    def ds_open_refine_window(L):
        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()
        if None is ch:
            #lani_err("NULL POINT ERROR")
            return 0
        if ch.DragonSoul_IsQualified():
            ch.DragonSoul_RefineWindow_Open(quest.CQuestManager.instance().GetCurrentNPCCharacterPtr())

        return 0

    @staticmethod
    def ds_give_qualification(L):
        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()
        if None is ch:
            #lani_err("NULL POINT ERROR")
            return 0
        ch.DragonSoul_GiveQualification()

        return 0

    @staticmethod
    def ds_is_qualified(L):
        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()
        if None is ch:
            #lani_err("NULL POINT ERROR")
            lua_pushnumber(L, 0)
            return 1

        lua_pushnumber(L, ch.DragonSoul_IsQualified())
        return 1

    @staticmethod
    def RegisterDragonSoulFunctionTable():
        ds_functions = [luaL_reg("open_refine_window", ds_open_refine_window), luaL_reg("give_qualification", ds_give_qualification), luaL_reg("is_qualified", ds_is_qualified), luaL_reg(None, None)]

        quest.CQuestManager.instance().AddLuaFunctionTable("ds", ds_functions)
