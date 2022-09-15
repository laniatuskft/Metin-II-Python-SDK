import math

class quest: #this class replaces the original namespace 'quest'
    @staticmethod
    def game_set_event_flag(L):
        q = quest.CQuestManager.instance()

        if lua_isstring(L,1) and lua_isnumber(L, 2):
            q.RequestSetEventFlag(lua_tostring(L,1), int(lua_tonumber(L,2)))

        return 0

    @staticmethod
    def game_get_event_flag(L):
        q = quest.CQuestManager.instance()

        if lua_isstring(L,1):
            lua_pushnumber(L, q.GetEventFlag(lua_tostring(L,1)))
        else:
            lua_pushnumber(L, 0)

        return 1

    @staticmethod
    def game_request_make_guild(L):
        q = quest.CQuestManager.instance()
        d = q.GetCurrentCharacterPtr().GetDesc()
        if d:
            header = byte(Globals.LG_HEADER_GC_REQUEST_MAKE_GUILD)
            d.Packet(header, 1)
        return 0

    @staticmethod
    def game_get_safebox_level(L):
        q = quest.CQuestManager.instance()
        lua_pushnumber(L, math.trunc(q.GetCurrentCharacterPtr().GetSafeboxSize() / float(Globals.SAFEBOX_PAGE_SIZE)))
        return 1

    @staticmethod
    def game_set_safebox_level(L):
        q = quest.CQuestManager.instance()
        p = SSafeboxChangeSizePacket()
        p.dwID = q.GetCurrentCharacterPtr().GetDesc().GetAccountTable().id
        p.bSize = byte(int(lua_tonumber(L,-1)))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        db_clientdesc.DBPacket(Globals.LG_HEADER_GD_SAFEBOX_CHANGE_SIZE, q.GetCurrentCharacterPtr().GetDesc().GetHandle(), p, sizeof(p))

        q.GetCurrentCharacterPtr().SetSafeboxSize(Globals.SAFEBOX_PAGE_SIZE * int(lua_tonumber(L,-1)))
        return 0

    @staticmethod
    def game_open_safebox(UnnamedParameter):
        q = quest.CQuestManager.instance()
        ch = q.GetCurrentCharacterPtr()
        ch.SetSafeboxOpenPosition()
        ch.ChatPacket(EChatType.CHAT_TYPE_COMMAND, "ShowMeSafeboxPassword")
        return 0

    @staticmethod
    def game_open_mall(UnnamedParameter):
        q = quest.CQuestManager.instance()
        ch = q.GetCurrentCharacterPtr()
        ch.SetSafeboxOpenPosition()
        ch.ChatPacket(EChatType.CHAT_TYPE_COMMAND, "ShowMeMallPassword")
        return 0

    @staticmethod
    def game_drop_item(L):
        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()

        item_vnum = lua_tonumber(L, 1)
        count = int(lua_tonumber(L, 2))
        x = ch.GetX()
        y = ch.GetY()

        item = ITEM_MANAGER.instance().CreateItem(item_vnum, uint(count), 0, DefineConstants.false, -1, DefineConstants.false)

        if item is None:
            #lani_err("cannot create item vnum %d count %d", item_vnum, count)
            return 0

        pos = pixel_position_s()
        pos.x = x + number(-200, 200)
        pos.y = y + number(-200, 200)

        item.AddToGround(ch.GetMapIndex(), pos, DefineConstants.false)
        item.StartDestroyEvent(300)

        return 0

    @staticmethod
    def game_drop_item_with_ownership(L):
        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()

        item = None
        if lua_gettop(L) == 1:
            item = ITEM_MANAGER.instance().CreateItem(lua_tonumber(L, 1), 1, 0, DefineConstants.false, -1, DefineConstants.false)
        elif (lua_gettop(L) == 2) or (lua_gettop(L) == 3):
            item = ITEM_MANAGER.instance().CreateItem(lua_tonumber(L, 1), uint(int(lua_tonumber(L, 2))), 0, DefineConstants.false, -1, DefineConstants.false)
        else:
            return 0

        if item is None:
            return 0

        if lua_isnumber(L, 3):
            sec = int(lua_tonumber(L, 3))
            if sec <= 0:
                item.SetOwnership(ch, 10)
            else:
                item.SetOwnership(ch, sec)
        else:
            item.SetOwnership(ch, 10)

        pos = pixel_position_s()
        pos.x = ch.GetX() + number(-200, 200)
        pos.y = ch.GetY() + number(-200, 200)

        item.AddToGround(ch.GetMapIndex(), pos, DefineConstants.false)
        item.StartDestroyEvent(300)

        return 0

    @staticmethod
    def game_web_mall(L):
        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()

        if ch is not None:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no equivalent to 'const_cast' in Python:
            do_in_game_mall(ch, const_cast<char>(""), 0, 0)
        return 0

    @staticmethod
    def RegisterGameFunctionTable():
        game_functions = [luaL_reg("get_safebox_level", game_get_safebox_level), luaL_reg("request_make_guild", game_request_make_guild), luaL_reg("set_safebox_level", game_set_safebox_level), luaL_reg("open_safebox", game_open_safebox), luaL_reg("open_mall", game_open_mall), luaL_reg("get_event_flag", game_get_event_flag), luaL_reg("set_event_flag", game_set_event_flag), luaL_reg("drop_item", game_drop_item), luaL_reg("drop_item_with_ownership", game_drop_item_with_ownership), luaL_reg("open_web_mall", game_web_mall), luaL_reg(None, None)]

        quest.CQuestManager.instance().AddLuaFunctionTable("game", game_functions)

