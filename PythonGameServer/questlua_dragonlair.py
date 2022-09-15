class quest: #this class replaces the original namespace 'quest'
    @staticmethod
    def dl_startRaid(L):
        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()
        baseMapIndex = lua_tonumber(L, -1)

        CDragonLairManager.instance().Start(ch.GetMapIndex(), baseMapIndex, ch.GetGuild().GetID())

        return 0

    @staticmethod
    def RegisterDragonLairFunctionTable():
        dl_functions = [luaL_reg("startRaid", dl_startRaid), luaL_reg(None, None)]

        quest.CQuestManager.instance().AddLuaFunctionTable("DragonLair", dl_functions)

