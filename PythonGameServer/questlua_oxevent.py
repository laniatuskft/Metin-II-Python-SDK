class quest: #this class replaces the original namespace 'quest'
    @staticmethod
    def oxevent_get_status(L):
        ret = COXEventManager.instance().GetStatus()

        lua_pushnumber(L, int(ret))

        return 1

    @staticmethod
    def oxevent_open(L):
        COXEventManager.instance().ClearQuiz()

        script = str(['\0' for _ in range(256)])
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        snprintf(script, sizeof(script), "%s/oxquiz.lua", LocaleService_GetBasePath().c_str())
        result = lua_dofile(quest.CQuestManager.instance().GetLuaState(), script)

        if result != 0:
            lua_pushnumber(L, 0)
            return 1
        else:
            lua_pushnumber(L, 1)

        COXEventManager.instance().SetStatus(OXEventStatus.OXEVENT_OPEN)

        return 1

    @staticmethod
    def oxevent_close(L):
        COXEventManager.instance().SetStatus(OXEventStatus.OXEVENT_CLOSE)

        return 0

    @staticmethod
    def oxevent_quiz(L):
        if lua_isnumber(L, 1) and lua_isnumber(L, 2):
            ret = COXEventManager.instance().Quiz(byte(int(lua_tonumber(L, 1))), int(lua_tonumber(L, 2)))

            if ret == LGEMiscellaneous.DEFINECONSTANTS.false:
                lua_pushnumber(L, 0)
            else:
                lua_pushnumber(L, 1)

        return 1

    @staticmethod
    def oxevent_get_attender(L):
        lua_pushnumber(L, int(COXEventManager.instance().GetAttenderCount()))
        return 1

    class end_oxevent_info(event_info_data):

        def __init__(self):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.empty = 0

            self.empty = 0

    @staticmethod
    def (UnnamedParameter):
        COXEventManager.instance().CloseEvent()
        return 0

    @staticmethod
    def oxevent_end_event(L):
        COXEventManager.instance().SetStatus(OXEventStatus.OXEVENT_FINISH)

        info = Globals.AllocEventInfo()
        event_create_ex(end_oxevent, info, ((5) * passes_per_sec))

        return 0

    @staticmethod
    def oxevent_end_event_force(L):
        COXEventManager.instance().CloseEvent()
        COXEventManager.instance().SetStatus(OXEventStatus.OXEVENT_FINISH)

        return 0

    @staticmethod
    def oxevent_give_item(L):
        if lua_isnumber(L, 1) and lua_isnumber(L, 2):
            COXEventManager.instance().GiveItemToAttender(uint(int(lua_tonumber(L, 1))), ushort(int(lua_tonumber(L, 2))))

        return 0

    @staticmethod
    def RegisterOXEventFunctionTable():
        oxevent_functions = [luaL_reg("get_status", oxevent_get_status), luaL_reg("open", oxevent_open), luaL_reg("close", oxevent_close), luaL_reg("quiz", oxevent_quiz), luaL_reg("get_attender", oxevent_get_attender), luaL_reg("end_event", oxevent_end_event), luaL_reg("end_event_force", oxevent_end_event_force), luaL_reg("give_item", oxevent_give_item), luaL_reg(None, None)]

        quest.CQuestManager.instance().AddLuaFunctionTable("oxevent", oxevent_functions)

