class quest: #this class replaces the original namespace 'quest'
    @staticmethod
    def quest_start(L):
        q = quest.CQuestManager.instance()
        q.GetCurrentPC().SetCurrentQuestStartFlag()
        return 0

    @staticmethod
    def quest_done(L):
        q = quest.CQuestManager.instance()
        q.GetCurrentPC().SetCurrentQuestDoneFlag()
        return 0

    @staticmethod
    def quest_set_title(L):
        q = quest.CQuestManager.instance()

        if lua_isstring(L,-1):
            q.GetCurrentPC().SetCurrentQuestTitle(lua_tostring(L,-1))

        return 0

    @staticmethod
    def quest_set_another_title(L):
        q = quest.CQuestManager.instance()

        if lua_isstring(L,1) and lua_isstring(L,2):
            q.GetCurrentPC().SetQuestTitle(lua_tostring(L,1), lua_tostring(L,2))

        return 0

    @staticmethod
    def quest_set_clock_name(L):
        q = quest.CQuestManager.instance()

        if lua_isstring(L,-1):
            q.GetCurrentPC().SetCurrentQuestClockName(lua_tostring(L,-1))

        return 0

    @staticmethod
    def quest_set_clock_value(L):
        q = quest.CQuestManager.instance()

        if lua_isnumber(L,-1):
            q.GetCurrentPC().SetCurrentQuestClockValue(int(rint(lua_tonumber(L,-1))))

        return 0

    @staticmethod
    def quest_set_counter_name(L):
        q = quest.CQuestManager.instance()

        if lua_isstring(L,-1):
            q.GetCurrentPC().SetCurrentQuestCounterName(lua_tostring(L,-1))

        return 0

    @staticmethod
    def quest_set_counter_value(L):
        q = quest.CQuestManager.instance()

        if lua_isnumber(L,-1):
            q.GetCurrentPC().SetCurrentQuestCounterValue(int(rint(lua_tonumber(L,-1))))

        return 0

    @staticmethod
    def quest_set_icon_file(L):
        q = quest.CQuestManager.instance()

        if lua_isstring(L,-1):
            q.GetCurrentPC().SetCurrentQuestIconFile(lua_tostring(L,-1))

        return 0

    @staticmethod
    def quest_setstate(L):
        if lua_tostring(L, -1)==None:
            #lani_err("state name is empty")
            return 0

        q = quest.CQuestManager.instance()
        pqs = q.GetCurrentState()
        pPC = q.GetCurrentPC()

        if L is not pqs.co:
            luaL_error(L, "running thread != current thread???")
            if test_server:
                #sys_log(0,"running thread != current thread???")
            return 0

        if pPC:
            stCurrentState = lua_tostring(L,-1)
            if test_server:
                #sys_log(0,"questlua->setstate( %s, %s )", pPC.GetCurrentQuestName(), stCurrentState)
            pqs.st = q.GetQuestStateIndex(pPC.GetCurrentQuestName(), stCurrentState)
            pPC.SetCurrentQuestStateName(stCurrentState)
        return 0

    @staticmethod
    def quest_coroutine_yield(L):
        q = quest.CQuestManager.instance()

        if q.IsInOtherPCBlock():
            #lani_err("FATAL ERROR! Yield occur in other_pc_block.")
            pPC = q.GetOtherPCBlockRootPC()
            if None is pPC:
                #lani_err("	... FFFAAATTTAAALLL Error. RootPC is NULL")
                return 0
            pQS = pPC.GetRunningQuestState()
            if None is pQS or None == q.GetQuestStateName(pPC.GetCurrentQuestName(), pQS.st):
                #lani_err("	... WHO AM I? WHERE AM I? I only know QuestName(%s)...", pPC.GetCurrentQuestName())
            else:
                #lani_err("	Current Quest(%s). State(%s)", pPC.GetCurrentQuestName(), q.GetQuestStateName(pPC.GetCurrentQuestName(), pQS.st))
            return 0
        return lua_yield(L, lua_gettop(L))

    @staticmethod
    def quest_no_send(L):
        q = quest.CQuestManager.instance()
        q.SetNoSend()
        return 0

    @staticmethod
    def quest_get_current_quest_index(L):
        q = quest.CQuestManager.instance()
        pPC = q.GetCurrentPC()

        idx = int(q.GetQuestIndexByName(pPC.GetCurrentQuestName()))
        lua_pushnumber(L, idx)
        return 1

    @staticmethod
    def quest_begin_other_pc_block(L):
        q = quest.CQuestManager.instance()
        pid = lua_tonumber(L, -1)
        q.BeginOtherPCBlock(pid)
        return 0

    @staticmethod
    def quest_end_other_pc_block(L):
        q = quest.CQuestManager.instance()
        q.EndOtherPCBlock()
        return 0

    @staticmethod
    def RegisterQuestFunctionTable():
        quest_functions = [luaL_reg("setstate", quest_setstate), luaL_reg("set_state", quest_setstate), luaL_reg("yield", quest_coroutine_yield), luaL_reg("set_title", quest_set_title), luaL_reg("set_title2", quest_set_another_title), luaL_reg("set_clock_name", quest_set_clock_name), luaL_reg("set_clock_value", quest_set_clock_value), luaL_reg("set_counter_name", quest_set_counter_name), luaL_reg("set_counter_value", quest_set_counter_value), luaL_reg("set_icon", quest_set_icon_file), luaL_reg("start", quest_start), luaL_reg("done", quest_done), luaL_reg("getcurrentquestindex", quest_get_current_quest_index), luaL_reg("no_send", quest_no_send), luaL_reg("begin_other_pc_block", quest_begin_other_pc_block), luaL_reg("end_other_pc_block", quest_end_other_pc_block), luaL_reg(None, None)]

        quest.CQuestManager.instance().AddLuaFunctionTable("q", quest_functions)
