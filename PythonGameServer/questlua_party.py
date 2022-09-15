class quest: #this class replaces the original namespace 'quest'

    @staticmethod
    def party_clear_ready(L):
        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()

        if ch.GetParty():
            f = FPartyClearReady()
            ch.GetParty().ForEachNearMember(f.functor_method)
        return 0

    @staticmethod
    def party_get_max_level(L):
        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()

        if ch.GetParty():
            lua_pushnumber(L,ch.GetParty().GetMemberMaxLevel())
        else:
            lua_pushnumber(L, 1)

        return 1

    class FRunCinematicSender:

        def __init__(self, str):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.data = ""
            self.pack = packet_script()

            self.data = "[RUN_CINEMA value;"
            self.data += str
            self.data += "]"

            self.pack.header = byte(Globals.LG_HEADER_GC_SCRIPT)
            self.pack.skin = byte(CQuestManager.QUEST_SKIN_CINEMATIC)
            self.pack.src_size = len(self.data)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            self.pack.size = self.pack.src_size + sizeof(packet_script)

        def functor_method(self, ch):
            #sys_log(0, "CINEMASEND_TRY %s", ch.GetName(LOCALE_LANIATUS))

            if ch.GetDesc():
                #sys_log(0, "CINEMASEND %s", ch.GetName(LOCALE_LANIATUS))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                ch.GetDesc().BufferedPacket(self.pack, sizeof(packet_script))
                ch.GetDesc().Packet(self.data, len(self.data))

    @staticmethod
    def party_run_cinematic(L):
        if not lua_isstring(L, 1):
            return 0

        #sys_log(0, "RUN_CINEMA %s", lua_tostring(L, 1))
        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()

        if ch.GetParty():
            f = FRunCinematicSender(lua_tostring(L, 1))

            ch.GetParty().Update()
            ch.GetParty().ForEachNearMember(f.functor_method)

        return 0

    class FCinematicSender:

        def __init__(self, str):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.str = '\0'
            self.packet_script = struct.packet_script()
            self.len = 0

            self.str = str
            self.len = len(str)

            self.packet_script.header = Globals.LG_HEADER_GC_SCRIPT
            self.packet_script.skin = CQuestManager.QUEST_SKIN_CINEMATIC
            self.packet_script.src_size = self.len
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            self.packet_script.size = self.packet_script.src_size + sizeof(self.packet_script)

        def functor_method(self, ch):
            #sys_log(0, "CINEMASEND_TRY %s", ch.GetName(LOCALE_LANIATUS))

            if ch.GetDesc():
                #sys_log(0, "CINEMASEND %s", ch.GetName(LOCALE_LANIATUS))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                ch.GetDesc().BufferedPacket(self.packet_script, sizeof(self.packet_script))
                ch.GetDesc().Packet(self.str, self.len)

    @staticmethod
    def party_show_cinematic(L):
        if not lua_isstring(L, 1):
            return 0

        #sys_log(0, "CINEMA %s", lua_tostring(L, 1))
        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()

        if ch.GetParty():
            f = FCinematicSender(lua_tostring(L, 1))

            ch.GetParty().Update()
            ch.GetParty().ForEachNearMember(f.functor_method)
        return 0

    @staticmethod
    def party_get_near_count(L):
        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()

        if ch.GetParty():
            lua_pushnumber(L, ch.GetParty().GetNearMemberCount())
        else:
            lua_pushnumber(L, 0)

        return 1

    @staticmethod
    def party_syschat(L):
        pParty = quest.CQuestManager.Instance().GetCurrentCharacterPtr().GetParty()

        if pParty:
            s = ostringstream()
            quest.combine_lua_string(L, s)

            f = FPartyChat(EChatType.CHAT_TYPE_INFO, s.str().c_str())

            pParty.ForEachOnlineMember(f.functor_method)

        return 0

    @staticmethod
    def party_is_leader(L):
        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()

        if ch.GetParty() is not None and ch.GetParty().GetLeaderPID() == ch.GetPlayerID():
            lua_pushboolean(L, 1)
        else:
            lua_pushboolean(L, 0)

        return 1

    @staticmethod
    def party_is_party(L):
        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()
        lua_pushboolean(L,1 if ch.GetParty() is not None else 0)
        return 1

    @staticmethod
    def party_get_leader_pid(L):
        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()
        if ch.GetParty():
            lua_pushnumber(L, ch.GetParty().GetLeaderPID())
        else:
            lua_pushnumber(L, -1)
        return 1


    @staticmethod
    def party_chat(L):
        pParty = quest.CQuestManager.Instance().GetCurrentCharacterPtr().GetParty()

        if pParty:
            s = ostringstream()
            quest.combine_lua_string(L, s)

            f = FPartyChat(EChatType.CHAT_TYPE_TALKING, s.str().c_str())

            pParty.ForEachOnlineMember(f.functor_method)

        return 0


    @staticmethod
    def party_is_map_member_flag_lt(L):

        if (not lua_isstring(L, 1)) or not lua_isnumber(L, 2):
            lua_pushnumber(L, 0)
            return 1

        q = quest.CQuestManager.Instance()
        pParty = q.GetCurrentCharacterPtr().GetParty()
        ch = q.GetCurrentCharacterPtr()
        pPC = q.GetCurrentPC()

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to pointers to value types:
#ORIGINAL METINII C CODE: const char* sz = lua_tostring(L,1);
        sz = lua_tostring(L,1)

        if pParty:
            f = FPartyCheckFlagLt()
            f.flagname = pPC.GetCurrentQuestName() + "."+sz
            f.value = int(rint(lua_tonumber(L, 2)))

            returnBool = pParty.ForEachOnMapMemberBool(f.functor_method, ch.GetMapIndex())
            lua_pushboolean(L, returnBool)

        return 1

    @staticmethod
    def party_set_flag(L):
        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()

        if ch.GetParty() is not None and lua_isstring(L, 1) and lua_isnumber(L, 2):
            ch.GetParty().SetFlag(lua_tostring(L, 1), int(lua_tonumber(L, 2)))

        return 0

    @staticmethod
    def party_get_flag(L):
        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()

        if ch.GetParty() is None or not lua_isstring(L, 1):
            lua_pushnumber(L, 0)
        else:
            lua_pushnumber(L, ch.GetParty().GetFlag(lua_tostring(L, 1)))

        return 1

    @staticmethod
    def party_set_quest_flag(L):
        q = quest.CQuestManager.instance()

        f = FSetQuestFlag()

        f.flagname = q.GetCurrentPC().GetCurrentQuestName() + "." + lua_tostring(L, 1)
        f.value = int(rint(lua_tonumber(L, 2)))

        ch = q.GetCurrentCharacterPtr()

        if ch.GetParty():
            ch.GetParty().ForEachOnlineMember(f.functor_method)
        else:
            f.functor_method(ch)

        return 0

    @staticmethod
    def party_is_in_dungeon(L):
        q = quest.CQuestManager.instance()
        ch = q.GetCurrentCharacterPtr()
        pParty = ch.GetParty()
        if pParty is not None:
            lua_pushboolean(L,((not LGEMiscellaneous.DEFINECONSTANTS.false)) if pParty.GetDungeon() is not None else LGEMiscellaneous.DEFINECONSTANTS.false)
            return 1
        lua_pushboolean(L, LGEMiscellaneous.DEFINECONSTANTS.false)
        return 1

    class FGiveBuff:

        def __init__(self, _dwType, _bApplyOn, _lApplyValue, _dwFlag, _lDuration, _lSPCost, _bOverride, _IsCube = LGEMiscellaneous.DefineConstants.false):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.dwType = 0
            self.bApplyOn = 0
            self.lApplyValue = 0
            self.dwFlag = 0
            self.lDuration = 0
            self.lSPCost = 0
            self.bOverride = False
            self.IsCube = False

            self.dwType = _dwType
            self.bApplyOn = _bApplyOn
            self.lApplyValue = _lApplyValue
            self.dwFlag = _dwFlag
            self.lDuration = _lDuration
            self.lSPCost = _lSPCost
            self.bOverride = _bOverride
            self.IsCube = _IsCube
        def functor_method(self, ch):
            ch.AddAffect(self.dwType, self.bApplyOn, self.lApplyValue, self.dwFlag, self.lDuration, self.lSPCost, self.bOverride, self.IsCube)

    @staticmethod
    def party_give_buff(L):
        q = quest.CQuestManager.instance()
        ch = q.GetCurrentCharacterPtr()

        if (not lua_isnumber(L, 1)) or (not lua_isnumber(L, 2)) or (not lua_isnumber(L, 3)) or (not lua_isnumber(L, 4)) or (not lua_isnumber(L, 5)) or (not lua_isnumber(L, 6)) or (not lua_isboolean(L, 7)) or not lua_isboolean(L, 8):
            lua_pushboolean(L, LGEMiscellaneous.DEFINECONSTANTS.false)
            return 1
        dwType = lua_tonumber(L, 1)
        bApplyOn = lua_tonumber(L, 2)
        lApplyValue = lua_tonumber(L, 3)
        dwFlag = lua_tonumber(L, 4)
        lDuration = lua_tonumber(L, 5)
        lSPCost = lua_tonumber(L, 6)
        bOverride = lua_toboolean(L, 7)
        IsCube = lua_toboolean(L, 8)

        f = FGiveBuff(dwType, bApplyOn, lApplyValue, dwFlag, lDuration, lSPCost, bOverride, IsCube)
        if ch.GetParty():
            ch.GetParty().ForEachOnMapMember(f.functor_method, ch.GetMapIndex())
        else:
            f.functor_method(ch)

        lua_pushboolean(L, ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
        return 1

    class FPartyPIDCollector:
        def __init__(self):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.vecPIDs = []

        def functor_method(self, ch):
            self.vecPIDs.append(ch.GetPlayerID())
    @staticmethod
    def party_get_member_pids(L):
        q = quest.CQuestManager.instance()
        ch = q.GetCurrentCharacterPtr()
        pParty = ch.GetParty()
        if None is pParty:
            return 0
        f = FPartyPIDCollector()
        pParty.ForEachOnMapMember(f.functor_method, ch.GetMapIndex())

        for it in f.vecPIDs:
            lua_pushnumber(L, *it)
        return len(f.vecPIDs)

    @staticmethod
    def RegisterPartyFunctionTable():
        party_functions = [luaL_reg("is_leader", party_is_leader), luaL_reg("is_party", party_is_party), luaL_reg("get_leader_pid", party_get_leader_pid), luaL_reg("setf", party_set_flag), luaL_reg("getf", party_get_flag), luaL_reg("setqf", party_set_quest_flag), luaL_reg("chat", party_chat), luaL_reg("syschat", party_syschat), luaL_reg("get_near_count", party_get_near_count), luaL_reg("show_cinematic", party_show_cinematic), luaL_reg("run_cinematic", party_run_cinematic), luaL_reg("get_max_level", party_get_max_level), luaL_reg("clear_ready", party_clear_ready), luaL_reg("is_in_dungeon", party_is_in_dungeon), luaL_reg("give_buff", party_give_buff), luaL_reg("is_map_member_flag_lt", party_is_map_member_flag_lt), luaL_reg("get_member_pids", party_get_member_pids), luaL_reg(None, None)]

        quest.CQuestManager.instance().AddLuaFunctionTable("party", party_functions)




