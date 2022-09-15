class quest: #this class replaces the original namespace 'quest'
    @staticmethod
    def marriage_engage_to(L):
        vid = lua_tonumber(L, 1)
        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()
        ch_you = CHARACTER_MANAGER.instance().Find(vid)
        if ch_you:
            marriage.CManager.instance().RequestAdd(ch.GetPlayerID(), ch_you.GetPlayerID(), ch.GetName(LOCALE_LANIATUS), ch_you.GetName(LOCALE_LANIATUS))
        return 0

    @staticmethod
    def marriage_remove(L):
        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()
        pMarriage = marriage.CManager.instance().Get(ch.GetPlayerID())
        if pMarriage is None:
            #lani_err("pid[%d:%s] is not exist couple", ch.GetPlayerID(), ch.GetName(LOCALE_LANIATUS))
            return 0
        marriage.CManager.instance().RequestRemove(ch.GetPlayerID(), pMarriage.GetOther(ch.GetPlayerID()))
        return 0

    @staticmethod
    def marriage_set_to_marriage(L):
        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()
        pMarriage = marriage.CManager.instance().Get(ch.GetPlayerID())
        if pMarriage is None:
            #lani_err("pid[%d:%s] is not exist couple", ch.GetPlayerID(), ch.GetName(LOCALE_LANIATUS))
            return 0
        pMarriage.SetMarried()
        return 0

    @staticmethod
    def marriage_find_married_vid(L):
        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()
        pMarriage = marriage.CManager.instance().Get(ch.GetPlayerID())
        vid = 0
        if pMarriage:
            you = CHARACTER_MANAGER.instance().FindByPID(pMarriage.GetOther(ch.GetPlayerID()))
            if you:
                vid = you.GetVID()

        lua_pushnumber(L, vid)

        return 1

    class FBuildLuaWeddingMapList:
        def __init__(self, L):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.L = None
            self.m_count = 0

            self.L = L
            self.m_count = 1
            lua_newtable(L)

        def functor_method(self, pMarriage):
            if pMarriage.pWeddingInfo is None:
                return

            lua_newtable(self.L)
            lua_pushnumber(self.L, pMarriage.m_pid1)
            lua_rawseti(self.L, -2, 1)
            lua_pushnumber(self.L, pMarriage.m_pid2)
            lua_rawseti(self.L, -2, 2)
            lua_pushstring(self.L, pMarriage.name1)
            lua_rawseti(self.L, -2, 3)
            lua_pushstring(self.L, pMarriage.name2)
            lua_rawseti(self.L, -2, 4)
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: lua_rawseti(L, -2, m_count++);
            lua_rawseti(self.L, -2, self.m_count)
            self.m_count += 1

    @staticmethod
    def marriage_get_wedding_list(L):
        marriage.CManager.instance().for_each_wedding.functor_method(FBuildLuaWeddingMapList(L))
        return 1

    @staticmethod
    def marriage_join_wedding(L):
        if (not lua_isnumber(L, 1)) or not lua_isnumber(L, 2):
            #lani_err("invalid player id for wedding map")
            return 0

        pid1 = lua_tonumber(L, 1)
        pid2 = lua_tonumber(L, 2)

        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()

        pMarriage = marriage.CManager.instance().Get(pid1)
        if pMarriage is None:
            #lani_err("pid[%d:%s] is not exist couple", ch.GetPlayerID(), ch.GetName(LOCALE_LANIATUS))
            return 0
        if pMarriage.GetOther(pid1) != pid2:
            #lani_err("not married %u %u", pid1, pid2)
            return 0

        if ch.IsHack(((not DefineConstants.false)), ((not DefineConstants.false)), g_nPortalLimitTime):
            return 0

        pMarriage.WarpToWeddingMap(ch.GetPlayerID())
        return 0

    @staticmethod
    def marriage_warp_to_my_marriage_map(L):
        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()
        pMarriage = marriage.CManager.instance().Get(ch.GetPlayerID())
        if pMarriage is None:
            #lani_err("pid[%d:%s] is not exist couple", ch.GetPlayerID(), ch.GetName(LOCALE_LANIATUS))
            return 0

        if ch.IsHack(((not DefineConstants.false)), ((not DefineConstants.false)), g_nPortalLimitTime):
            return 0

        pMarriage.WarpToWeddingMap(ch.GetPlayerID())
        return 0

    @staticmethod
    def marriage_end_wedding(L):
        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()
        pMarriage = marriage.CManager.instance().Get(ch.GetPlayerID())
        if pMarriage is None:
            #lani_err("pid[%d:%s] is not exist couple", ch.GetPlayerID(), ch.GetName(LOCALE_LANIATUS))
            return 0
        if pMarriage.pWeddingInfo:
            pMarriage.RequestEndWedding()
        return 0

    @staticmethod
    def marriage_wedding_dark(L):
        if not lua_isboolean(L, 1):
            #lani_err("invalid argument 1 : must be boolean")
            return 0
        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()
        pMarriage = marriage.CManager.instance().Get(ch.GetPlayerID())

        if pMarriage is None:
            #lani_err("pid[%d:%s] is not exist couple", ch.GetPlayerID(), ch.GetName(LOCALE_LANIATUS))
            return 0
        if pMarriage.pWeddingInfo:
            pWedding = marriage.WeddingManager.instance().Find(pMarriage.pWeddingInfo.dwMapIndex)
            pWedding.SetDark(lua_toboolean(L, 1))

        return 0

    @staticmethod
    def marriage_wedding_client_command(L):
        if not lua_isstring(L, 1):
            #lani_err("invalid argument 1 : must be string")
            return 0

        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()
        pMarriage = marriage.CManager.instance().Get(ch.GetPlayerID())
        if pMarriage is None:
            #lani_err("pid[%d:%s] is not exist couple", ch.GetPlayerID(), ch.GetName(LOCALE_LANIATUS))
            return 0
        if pMarriage.pWeddingInfo:
            pWedding = marriage.WeddingManager.instance().Find(pMarriage.pWeddingInfo.dwMapIndex)
            pWedding.ShoutInMap(EChatType.CHAT_TYPE_COMMAND, lua_tostring(L, 1))
        return 0


    @staticmethod
    def marriage_wedding_is_playing_music(L):
        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()
        pMarriage = marriage.CManager.instance().Get(ch.GetPlayerID())
        if pMarriage is None:
            #lani_err("pid[%d:%s] is not exist couple", ch.GetPlayerID(), ch.GetName(LOCALE_LANIATUS))
            return 0
        if pMarriage.pWeddingInfo:
            pWedding = marriage.WeddingManager.instance().Find(pMarriage.pWeddingInfo.dwMapIndex)
            if pWedding:
                lua_pushboolean(L, pWedding.IsPlayingMusic())
            else:
                lua_pushboolean(L, LGEMiscellaneous.DEFINECONSTANTS.false)

        lua_pushboolean(L, LGEMiscellaneous.DEFINECONSTANTS.false)
        return 1
    @staticmethod
    def marriage_wedding_music(L):
        if not lua_isboolean(L, 1):
            #lani_err("invalid argument 1 : must be boolean")
            return 0
        if not lua_isstring(L, 2):
            #lani_err("invalid argument 2 : must be string")
            return 0

        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()
        pMarriage = marriage.CManager.instance().Get(ch.GetPlayerID())
        if pMarriage is None:
            #lani_err("pid[%d:%s] is not exist couple", ch.GetPlayerID(), ch.GetName(LOCALE_LANIATUS))
            return 0
        if pMarriage.pWeddingInfo:
            pWedding = marriage.WeddingManager.instance().Find(pMarriage.pWeddingInfo.dwMapIndex)
            pWedding.SetMusic(lua_toboolean(L, 1), lua_tostring(L, 2))
        return 0
    @staticmethod
    def marriage_wedding_snow(L):
        if not lua_isboolean(L, 1):
            #lani_err("invalid argument 1 : must be boolean")
            return 0
        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()
        pMarriage = marriage.CManager.instance().Get(ch.GetPlayerID())
        if pMarriage is None:
            #lani_err("pid[%d:%s] is not exist couple", ch.GetPlayerID(), ch.GetName(LOCALE_LANIATUS))
            return 0
        if pMarriage.pWeddingInfo:
            pWedding = marriage.WeddingManager.instance().Find(pMarriage.pWeddingInfo.dwMapIndex)
            pWedding.SetSnow(lua_toboolean(L, 1))
        return 0

    @staticmethod
    def marriage_in_my_wedding(L):
        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()
        pMarriage = marriage.CManager.instance().Get(ch.GetPlayerID())
        if pMarriage.pWeddingInfo:
            lua_pushboolean(L, ch.GetMapIndex() == pMarriage.pWeddingInfo.dwMapIndex)
        else:
            lua_pushboolean(L, 0)
        return 1

    @staticmethod
    def marriage_get_married_time(L):
        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()
        pMarriage = marriage.CManager.instance().Get(ch.GetPlayerID())

        if pMarriage is None:
            #lani_err("trying to get time for not married character")
            lua_pushnumber(L, 0)
            return 1

        lua_pushnumber(L, get_global_time() - pMarriage.marry_time)
        return 1

    @staticmethod
    def RegisterMarriageFunctionTable():
        marriage_functions = [luaL_reg("engage_to", marriage_engage_to), luaL_reg("remove", marriage_remove), luaL_reg("find_married_vid", marriage_find_married_vid), luaL_reg("get_wedding_list", marriage_get_wedding_list), luaL_reg("join_wedding", marriage_join_wedding), luaL_reg("set_to_marriage", marriage_set_to_marriage), luaL_reg("end_wedding", marriage_end_wedding), luaL_reg("wedding_dark", marriage_wedding_dark), luaL_reg("wedding_snow", marriage_wedding_snow), luaL_reg("wedding_music", marriage_wedding_music), luaL_reg("wedding_is_playing_music", marriage_wedding_is_playing_music), luaL_reg("wedding_client_command", marriage_wedding_client_command), luaL_reg("in_my_wedding", marriage_in_my_wedding), luaL_reg("warp_to_my_marriage_map",marriage_warp_to_my_marriage_map), luaL_reg("get_married_time", marriage_get_married_time), luaL_reg(None, None)]
        quest.CQuestManager.instance().AddLuaFunctionTable("marriage", marriage_functions)
