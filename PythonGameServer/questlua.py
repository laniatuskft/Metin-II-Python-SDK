import math

class quest: #this class replaces the original namespace 'quest'
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    RegisterPCFunctionTable()
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    RegisterNPCFunctionTable()
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    RegisterTargetFunctionTable()
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    RegisterAffectFunctionTable()
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    RegisterBuildingFunctionTable()
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    RegisterMarriageFunctionTable()
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    RegisterITEMFunctionTable()
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    RegisterDungeonFunctionTable()
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    RegisterQuestFunctionTable()
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    RegisterPartyFunctionTable()
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    RegisterHorseFunctionTable()
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    RegisterPetFunctionTable()
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    RegisterGuildFunctionTable()
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    RegisterGameFunctionTable()
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    RegisterGlobalFunctionTable(L)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    RegisterOXEventFunctionTable()
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    RegisterDanceEventFunctionTable()
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    RegisterDragonLairFunctionTable()
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    RegisterDragonSoulFunctionTable()

    @staticmethod
    def combine_lua_string(L, s):
        buf = str(['\0' for _ in range(32)])

        n = lua_gettop(L)
        i = None

        for i in range(1, n + 1):
            if lua_isstring(L,i):
                s << lua_tostring(L, i)
            elif lua_isnumber(L, i):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                snprintf(buf, sizeof(buf), "%.14g\n", lua_tonumber(L,i))
                s << buf

    class FSetWarpLocation:

        def __init__(self, _map_index, _x, _y):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.map_index = 0
            self.x = 0
            self.y = 0

            self.map_index = _map_index
            self.x = _x
            self.y = _y
        def functor_method(self, ch):
            if ch.IsPC():
                ch.SetWarpLocation(self.map_index, self.x, self.y)

    class FSetQuestFlag:

        def __init__(self):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.flagname = ""
            self.value = 0


        def functor_method(self, ch):
            if not ch.IsPC():
                return

            pPC = CQuestManager.instance().GetPCForce(ch.GetPlayerID())

            if pPC:
                pPC.SetFlag(self.flagname, self.value, DefineConstants.false)

    class FPartyCheckFlagLt:

        def __init__(self):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.flagname = ""
            self.value = 0


        def functor_method(self, ch):
            if not ch.IsPC():
                return LGEMiscellaneous.DEFINECONSTANTS.false

            pPC = CQuestManager.instance().GetPCForce(ch.GetPlayerID())
            returnBool = None
            if pPC:
                flagValue = pPC.GetFlag(self.flagname)
                if self.value > flagValue:
                    returnBool = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
                else:
                    returnBool = LGEMiscellaneous.DEFINECONSTANTS.false

            return returnBool

    class FPartyChat:

        def __init__(self, ChatType, str):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.iChatType = 0
            self.str = '\0'

            self.iChatType = ChatType
            self.str = str

        def functor_method(self, ch):
            ch.ChatPacket(byte(self.iChatType), "%s", self.str)

    class FPartyClearReady:
        def functor_method(self, ch):
            ch.RemoveAffect(LaniatusEAffectTypes.LANIA_AFFECT_DUNGEON_READY)

    class FSendPacket:

        def __init__(self):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.buf = TEMP_BUFFER(8192, DefineConstants.false)


        def functor_method(self, ent):
            if ent.IsType(EEntityTypes.ENTITY_CHARACTER):
                ch = ent

                if ch.GetDesc():
                    ch.GetDesc().Packet(self.buf.read_peek(), self.buf.size())

    class FSendPacketToEmpire:

        def __init__(self):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.buf = TEMP_BUFFER(8192, DefineConstants.false)
            self.bEmpire = 0


        def functor_method(self, ent):
            if ent.IsType(EEntityTypes.ENTITY_CHARACTER):
                ch = ent

                if ch.GetDesc():
                    if ch.GetEmpire() == self.bEmpire:
                        ch.GetDesc().Packet(self.buf.read_peek(), self.buf.size())

    class FWarpEmpire:

        def __init__(self):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.m_bEmpire = 0
            self.m_lMapIndexTo = 0
            self.m_x = 0
            self.m_y = 0


        def functor_method(self, ent):
            if ent.IsType(EEntityTypes.ENTITY_CHARACTER):
                ch = ent

                if ch.IsPC() and ch.GetEmpire() == self.m_bEmpire:
                    ch.WarpSet(self.m_x, self.m_y, self.m_lMapIndexTo)

    class warp_all_to_map_my_empire_event_info(event_info_data):

        def __init__(self):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.m_bEmpire = 0
            self.m_lMapIndexFrom = 0
            self.m_lMapIndexTo = 0
            self.m_x = 0
            self.m_y = 0

            self.m_bEmpire = 0
            self.m_lMapIndexFrom = 0
            self.m_lMapIndexTo = 0
            self.m_x = 0
            self.m_y = 0

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following statement was not recognized, possibly due to an unrecognized macro:
    int(warp_all_to_map_my_empire_event)(_boost_func_of_void.intrusive_ptr<struct event> event, int processing_time)

    class FBuildLuaGuildWarList:

        def __init__(self, lua_state):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.L = None
            self.m_count = 0

            self.L = lua_state
            self.m_count = 1
            lua_newtable(lua_state)

        def functor_method(self, g1, g2):
            g = CGuildManager.instance().FindGuild(g1)

            if g is None:
                return

            if g.GetGuildWarType(g2) == EGuildWarType.GUILD_WAR_TYPE_FIELD:
                return

            if g.GetGuildWarState(g2) != EGuildWarState.GUILD_WAR_ON_WAR:
                return

            lua_newtable(self.L)
            lua_pushnumber(self.L, g1)
            lua_rawseti(self.L, -2, 1)
            lua_pushnumber(self.L, g2)
            lua_rawseti(self.L, -2, 2)
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: lua_rawseti(L, -2, m_count++);
            lua_rawseti(self.L, -2, self.m_count)
            self.m_count += 1


class quest: #this class replaces the original namespace 'quest'

    @staticmethod
    def ScriptToString(str):
        L = quest.CQuestManager.instance().GetLuaState()
        x = lua_gettop(L)

        errcode = lua_dobuffer(L, ("return "+str).c_str(), len(str)+7, "ScriptToString")
        retstr = ""
        if errcode == 0:
            if lua_isstring(L,-1):
                retstr = lua_tostring(L, -1)
        else:
            #lani_err("LUA ScriptRunError (code:%d src:[%s])", errcode, str)
        lua_settop(L,x)
        return retstr

    @staticmethod
    def IsScriptTrue(code, size):
        if size == 0:
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        L = quest.CQuestManager.instance().GetLuaState()
        x = lua_gettop(L)
        errcode = lua_dobuffer(L, code, size, "IsScriptTrue")
        bStart = lua_toboolean(L, -1)
        if errcode != 0:
            buf = str(['\0' for _ in range(100)])
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            snprintf(buf, sizeof(buf), "LUA ScriptRunError (code:%%d src:[%%%ds])", size)
            #lani_err(buf, errcode, code)
        lua_settop(L,x)
        return bStart != 0

    @staticmethod
    def highscore_show(L):
        q = quest.CQuestManager.instance()
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to pointers to value types:
#ORIGINAL METINII C CODE: const char * pszBoardName = lua_tostring(L, 1);
        pszBoardName = lua_tostring(L, 1)
        mypid = q.GetCurrentCharacterPtr().GetPlayerID()
        bOrder = ((not LGEMiscellaneous.DEFINECONSTANTS.false)) if int(lua_tonumber(L, 2)) != 0 else LGEMiscellaneous.DEFINECONSTANTS.false

        DBManager.instance().ReturnQuery(Globals.QID_HIGHSCORE_SHOW, mypid, None, "SELECT h.pid, p.name, h.value FROM highscore%s as h, player%s as p WHERE h.board = '%s' AND h.pid = p.id ORDER BY h.value %s LIMIT 10", get_table_postfix(), get_table_postfix(), pszBoardName,"DESC" if bOrder else "")
        return 0

    @staticmethod
    def highscore_register(L):
        q = quest.CQuestManager.instance()

        qi = LG_NEW_M2 SHighscoreRegisterQueryInfo

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        strncpy_s(qi.szBoard, sizeof(qi.szBoard), lua_tostring(L, 1), _TRUNCATE)
        qi.dwPID = q.GetCurrentCharacterPtr().GetPlayerID()
        qi.iValue = int(lua_tonumber(L, 2))
        qi.bOrder = int(lua_tonumber(L, 3)) != 0

        DBManager.instance().ReturnQuery(Globals.QID_HIGHSCORE_REGISTER, qi.dwPID, qi, "SELECT value FROM highscore%s WHERE board='%s' AND pid=%u", get_table_postfix(), qi.szBoard, qi.dwPID)
        return 1

    @staticmethod
    def member_chat(L):
        s = ostringstream()
        quest.combine_lua_string(L, s)
        quest.CQuestManager.Instance().GetCurrentPartyMember().ChatPacket(EChatType.CHAT_TYPE_TALKING, "%s", s.str().c_str())
        return 0

    @staticmethod
    def member_clear_ready(L):
        ch = quest.CQuestManager.instance().GetCurrentPartyMember()
        ch.RemoveAffect(LaniatusEAffectTypes.LANIA_AFFECT_DUNGEON_READY)
        return 0

    @staticmethod
    def member_set_ready(L):
        ch = quest.CQuestManager.instance().GetCurrentPartyMember()
        ch.AddAffect(LaniatusEAffectTypes.LANIA_AFFECT_DUNGEON_READY, EPointTypes.LG_POINT_NONE, 0, EAffectBits.AFF_DUNGEON_READY, 65535, 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), DefineConstants.false)
        return 0

    @staticmethod
    def mob_spawn(L):
        if (not lua_isnumber(L, 1)) or (not lua_isnumber(L, 2)) or (not lua_isnumber(L, 3)) or not lua_isnumber(L, 4):
            #lani_err("invalid argument")
            return 0

        mob_vnum = lua_tonumber(L, 1)
        local_x = int(lua_tonumber(L, 2))*100
        local_y = int(lua_tonumber(L, 3))*100
        radius = float(lua_tonumber(L, 4))*100
        bAggressive = lua_toboolean(L, 5)
        count = uint(lua_tonumber(L, 6) if (lua_isnumber(L, 6)) ) else 1)

        if count == 0:
            count = 1
        elif count > 10:
            #lani_err("count bigger than 10")
            count = 10

        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()
        pMap = SECTREE_MANAGER.instance().GetMap(ch.GetMapIndex())
        if pMap is None:
            return 0
        dwQuestIdx = uint(quest.CQuestManager.instance().GetCurrentPC().GetCurrentQuestIndex())

        ret = LGEMiscellaneous.DEFINECONSTANTS.false
        mob = None

## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: while (count--)
        while (count) != 0:
            count -= 1
            for loop in range(0, 8):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
                angle = number(0, 999) * LGEMiscellaneous.DEFINECONSTANTS.M_PI * 2 / 1000
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
                r = number(0, 999) * radius / 1000

                x = local_x + pMap.m_setting.iBaseX + int((r * math.cos(angle)))
                y = local_y + pMap.m_setting.iBaseY + int((r * math.sin(angle)))

                mob = CHARACTER_MANAGER.instance().SpawnMob(mob_vnum, ch.GetMapIndex(), x, y, 0, DefineConstants.false, -1, ((not DefineConstants.false)))

                if mob:
                    break

            if mob:
                if bAggressive:
                    mob.SetAggressive()

                mob.SetQuestBy(dwQuestIdx)

                if not ret:
                    ret = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
                    lua_pushnumber(L, mob.GetVID())
        count -= 1

        if not ret:
            lua_pushnumber(L, 0)

        return 1

    @staticmethod
    def mob_spawn_group(L):
        if (not lua_isnumber(L, 1)) or (not lua_isnumber(L, 2)) or (not lua_isnumber(L, 3)) or (not lua_isnumber(L, 4)) or not lua_isnumber(L, 6):
            #lani_err("invalid argument")
            lua_pushnumber(L, 0)
            return 1

        group_vnum = lua_tonumber(L, 1)
        local_x = int(lua_tonumber(L, 2)) * 100
        local_y = int(lua_tonumber(L, 3)) * 100
        radius = float(lua_tonumber(L, 4)) * 100
        bAggressive = lua_toboolean(L, 5)
        count = lua_tonumber(L, 6)

        if count == 0:
            count = 1
        elif count > 10:
            #lani_err("count bigger than 10")
            count = 10

        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()
        pMap = SECTREE_MANAGER.instance().GetMap(ch.GetMapIndex())
        if pMap is None:
            lua_pushnumber(L, 0)
            return 1
        dwQuestIdx = uint(quest.CQuestManager.instance().GetCurrentPC().GetCurrentQuestIndex())

        ret = LGEMiscellaneous.DEFINECONSTANTS.false
        mob = None

## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: while (count--)
        while (count) != 0:
            count -= 1
            for loop in range(0, 8):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
                angle = number(0, 999) * LGEMiscellaneous.DEFINECONSTANTS.M_PI * 2 / 1000
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
                r = number(0, 999)*radius/1000

                x = local_x + pMap.m_setting.iBaseX + int((r * math.cos(angle)))
                y = local_y + pMap.m_setting.iBaseY + int((r * math.sin(angle)))

                mob = CHARACTER_MANAGER.instance().SpawnGroup(group_vnum, ch.GetMapIndex(), x, y, x, y, None, bAggressive, NULL)

                if mob:
                    break

            if mob:
                mob.SetQuestBy(dwQuestIdx)

                if not ret:
                    ret = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
                    lua_pushnumber(L, mob.GetVID())
        count -= 1

        if not ret:
            lua_pushnumber(L, 0)

        return 1

    @staticmethod
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Pointer arithmetic is detected on the parameter 'preg':
#ORIGINAL METINII C CODE: void CQuestManager::AddLuaFunctionTable(const char * c_pszName, luaL_reg * preg)
    def AddLuaFunctionTable(c_pszName, preg):
        lua_newtable(L)

        while (preg.name):
            lua_pushstring(L, preg.name)
            lua_pushcfunction(L, preg.func)
            lua_rawset(L, -3)
            preg += 1

        lua_setglobal(L, c_pszName)

    @staticmethod
    def BuildStateIndexToName(questName):
        x = lua_gettop(L)
        lua_getglobal(L, questName)

        if lua_isnil(L,-1):
            #lani_err("QUEST wrong quest state file for quest %s",questName)
            lua_settop(L,x)
            return

        lua_pushnil(L)
        while lua_next(L, -2):
            if lua_isstring(L, -2) and lua_isnumber(L, -1):
                lua_pushvalue(L, -2)
                lua_rawset(L, -4)
            else:
                lua_pop(L, 1)

        lua_settop(L, x)

    @staticmethod
    def InitializeLua():
        L = lua_open()

        luaopen_base(L)
        luaopen_table(L)
        luaopen_string(L)
        luaopen_math(L)
        luaopen_io(L)
        luaopen_debug(L)

        quest.RegisterAffectFunctionTable()
        quest.RegisterBuildingFunctionTable()
        quest.RegisterDungeonFunctionTable()
        quest.RegisterGameFunctionTable()
        quest.RegisterGuildFunctionTable()
        quest.RegisterHorseFunctionTable()
        quest.RegisterPetFunctionTable()
        quest.RegisterITEMFunctionTable()
        quest.RegisterMarriageFunctionTable()
        quest.RegisterNPCFunctionTable()
        quest.RegisterPartyFunctionTable()
        quest.RegisterPCFunctionTable()
        quest.RegisterQuestFunctionTable()
        quest.RegisterTargetFunctionTable()
        quest.RegisterOXEventFunctionTable()
        quest.RegisterDanceEventFunctionTable()
        quest.RegisterDragonLairFunctionTable()
        quest.RegisterDragonSoulFunctionTable()

            member_functions = [luaL_reg("chat", member_chat), luaL_reg("set_ready", member_set_ready), luaL_reg("clear_ready", member_clear_ready), luaL_reg(None, None)]

            AddLuaFunctionTable("member", member_functions)

            highscore_functions = [luaL_reg("register", highscore_register), luaL_reg("show", highscore_show), luaL_reg(None, None)]

            AddLuaFunctionTable("highscore", highscore_functions)

            mob_functions = [luaL_reg("spawn", mob_spawn), luaL_reg("spawn_group", mob_spawn_group), luaL_reg(None, None)]

            AddLuaFunctionTable("mob", mob_functions)

        quest.RegisterGlobalFunctionTable(L)

            settingsFileName = str(['\0' for _ in range(256)])
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            snprintf(settingsFileName, sizeof(settingsFileName), "%s/settings.lua", LocaleService_GetBasePath().c_str())

            settingsLoadingResult = lua_dofile(L, settingsFileName)
            #sys_log(0, "LoadSettings(%s), returns %d", settingsFileName, settingsLoadingResult)
            if settingsLoadingResult != 0:
                #lani_err("LOAD_SETTINGS_FAILURE(%s)", settingsFileName)
                return LGEMiscellaneous.DEFINECONSTANTS.false

            questlibFileName = str(['\0' for _ in range(256)])
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            snprintf(questlibFileName, sizeof(questlibFileName), "%s/questlib.lua", LocaleService_GetQuestPath().c_str())

            questlibLoadingResult = lua_dofile(L, questlibFileName)
            #sys_log(0, "LoadQuestlib(%s), returns %d", questlibFileName, questlibLoadingResult)
            if questlibLoadingResult != 0:
                #lani_err("LOAD_QUESTLIB_FAILURE(%s)", questlibFileName)
                return LGEMiscellaneous.DEFINECONSTANTS.false

        translateFileName = str(['\0' for _ in range(256)])
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        snprintf(translateFileName, sizeof(translateFileName), "%s/translate.lua", LocaleService_GetBasePath().c_str())

        translateLoadingResult = lua_dofile(L, translateFileName)
        #sys_log(0, "LoadTranslate(%s), returns %d", translateFileName, translateLoadingResult)
        if translateLoadingResult != 0:
            #lani_err("LOAD_TRANSLATE_ERROR(%s)", translateFileName)
            return LGEMiscellaneous.DEFINECONSTANTS.false

            questLocaleFileName = str(['\0' for _ in range(256)])
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            snprintf(questLocaleFileName, sizeof(questLocaleFileName), "%s/locale.lua", g_stQuestDir.c_str())

            questLocaleLoadingResult = lua_dofile(L, questLocaleFileName)
            #sys_log(0, "LoadQuestLocale(%s), returns %d", questLocaleFileName, questLocaleLoadingResult)
            if questLocaleLoadingResult != 0:
                #lani_err("LoadQuestLocale(%s) FAILURE", questLocaleFileName)
                return LGEMiscellaneous.DEFINECONSTANTS.false

        it = g_setQuestObjectDir.begin()
        while it is not g_setQuestObjectDir.end():
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to references to variables:
#ORIGINAL METINII C CODE: const str& stQuestObjectDir = *it;
            stQuestObjectDir = *it
            buf = str(['\0' for _ in range(_MAX_PATH)])
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            snprintf(buf, sizeof(buf), "%s/state/", stQuestObjectDir)
            pdir = opendir(buf)
            iQuestIdx = 0

            if pdir:
                pde = None

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: while ((pde = readdir(pdir)))
                while (pde = readdir(pdir)):
                    if pde.d_name[0] == '.':
                        continue

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                    snprintf(buf[11:], sizeof(buf) - 11, "%s", pde.d_name)

                    iQuestIdx += 1
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: RegisterQuest(pde->d_name, ++iQuestIdx);
                    RegisterQuest(pde.d_name, iQuestIdx)
                    ret = lua_dofile(L, (stQuestObjectDir + "/state/" + pde.d_name).c_str())
                    #sys_log(0, "QUEST: loading %s, returns %d", (stQuestObjectDir + "/state/" + pde.d_name).c_str(), ret)

                    BuildStateIndexToName(pde.d_name)

                closedir(pdir)
            it += 1

        lua_setgcthreshold(L, 0)

        lua_newtable(L)
        lua_setglobal(L, "__codecache")
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    @staticmethod
    def GotoSelectState(qs):
        lua_checkstack(qs.co, 1)
        n = luaL_getn(qs.co, -1)
        qs.args = short(n)

        os = ostringstream()
        os << "[QUESTION "

        for i in range(1, n + 1):
            lua_rawgeti(qs.co,-1,i)
            if lua_isstring(qs.co,-1):
                if i != 1:
                    os << "|"
                os << i << ";" << lua_tostring(qs.co,-1)
            else:
                #lani_err("SELECT wrong data %s", lua_typename(qs.co, -1))
                #lani_err("here")
            lua_pop(qs.co,1)
        os << "]"


        AddScript(os.str())
        qs.suspend_state = byte(quest.SUSPEND_STATE_SELECT)
        if test_server:
            #sys_log(0, "%s", m_strScript.c_str())
        SendScript()

    class confirm_timeout_event_info(event_info_data):

        def __init__(self):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.dwWaitPID = 0
            self.dwReplyPID = 0

            self.dwWaitPID = 0
            self.dwReplyPID = 0

    @staticmethod
    def (UnnamedParameter):
        info = if isinstance(event.info, confirm_timeout_event_info) else None

        if info is None:
            #lani_err("confirm_timeout_event> <Factor> Null pointer")
            return 0

        chWait = CHARACTER_MANAGER.instance().FindByPID(info.dwWaitPID)
        chReply = None

        if chReply:
            pass

        if chWait:
            quest.CQuestManager.instance().Confirm(info.dwWaitPID, quest.EQuestConfirmType.CONFIRM_TIMEOUT, 0)

        return 0

    @staticmethod
    def GotoConfirmState(qs):
        qs.suspend_state = byte(quest.SUSPEND_STATE_CONFIRM)
        dwVID = lua_tonumber(qs.co, -3)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to pointers to value types:
#ORIGINAL METINII C CODE: const char* szMsg = lua_tostring(qs.co, -2);
        szMsg = lua_tostring(qs.co, -2)
        iTimeout = int(lua_tonumber(qs.co, -1))

        #sys_log(0, "GotoConfirmState vid %u msg '%s', timeout %d", dwVID, szMsg, iTimeout)

        ch = CHARACTER_MANAGER.instance().Find(dwVID)
        if ch is not None and ch.IsPC():
            ch.ConfirmWithMsg(szMsg, iTimeout, GetCurrentCharacterPtr().GetPlayerID())

        GetCurrentPC().SetConfirmWait(ch.GetPlayerID() if (ch is not None and ch.IsPC()) ) else 0)
        os = ostringstream()
        os << "[CONFIRM_WAIT timeout;" << iTimeout << "]"
        AddScript(os.str())
        SendScript()

        info = Globals.AllocEventInfo()

        info.dwWaitPID = GetCurrentCharacterPtr().GetPlayerID()
        info.dwReplyPID = ch.GetPlayerID() if (ch is not None and ch.IsPC()) else 0

        event_create_ex(confirm_timeout_event, info, ((iTimeout) * passes_per_sec))

    @staticmethod
    def GotoSelectItemState(qs):
        qs.suspend_state = byte(quest.SUSPEND_STATE_SELECT_ITEM)
        AddScript("[SELECT_ITEM]")
        SendScript()

    @staticmethod
    def GotoInputState(qs):
        qs.suspend_state = byte(quest.SUSPEND_STATE_INPUT)
        AddScript("[INPUT]")
        SendScript()

    @staticmethod
    def GotoPauseState(qs):
        qs.suspend_state = byte(quest.SUSPEND_STATE_PAUSE)
        AddScript("[NEXT]")
        SendScript()

    @staticmethod
    def GotoEndState(qs):
        AddScript("[DONE]")
        SendScript()

    @staticmethod
    def OpenState(quest_name, state_index):
        qs = QuestState()
        qs.args = 0
        qs.st = state_index
        qs.co = lua_newthread(L)
        qs.ico = lua_ref(L, 1)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
#ORIGINAL METINII C CODE: return qs;
        return quest.QuestState(qs)

    @staticmethod
    def RunState(qs):
        ClearError()

        m_CurrentRunningState = qs
        ret = lua_resume(qs.co, qs.args)

        if ret == 0:
            if lua_gettop(qs.co) == 0:
                GotoEndState(qs)
                return LGEMiscellaneous.DEFINECONSTANTS.false

            if not strcmp(lua_tostring(qs.co, 1), "select"):
                GotoSelectState(qs)
                return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

            if not strcmp(lua_tostring(qs.co, 1), "wait"):
                GotoPauseState(qs)
                return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

            if not strcmp(lua_tostring(qs.co, 1), "input"):
                GotoInputState(qs)
                return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

            if not strcmp(lua_tostring(qs.co, 1), "confirm"):
                GotoConfirmState(qs)
                return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

            if not strcmp(lua_tostring(qs.co, 1), "select_item"):
                GotoSelectItemState(qs)
                return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
        else:
            #lani_err("LUA_ERROR: %s", lua_tostring(qs.co, 1))

        WriteRunningStateToSyserr()
        SetError()

        GotoEndState(qs)
        return LGEMiscellaneous.DEFINECONSTANTS.false

    @staticmethod
    def CloseState(qs):
        if qs.co:
            lua_unref(L, qs.ico)
            qs.co = None
