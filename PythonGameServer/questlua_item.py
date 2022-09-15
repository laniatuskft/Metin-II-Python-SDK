class quest: #this class replaces the original namespace 'quest'
    @staticmethod
    def item_get_cell(L):
        q = quest.CQuestManager.instance()

        if q.GetCurrentItem():
            lua_pushnumber(L, q.GetCurrentItem().GetCell())
        else:
            lua_pushnumber(L, 0)
        return 1

    @staticmethod
    def item_select_cell(L):
        lua_pushboolean(L, 0)
        if not lua_isnumber(L, 1):
            return 1
        cell = lua_tonumber(L, 1)

        ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()
        item = ch.GetInventoryItem(ushort(cell)) if ch is not None else None

        if item is None:
            return 1

        quest.CQuestManager.instance().SetCurrentItem(item)
        lua_pushboolean(L, 1)

        return 1

    @staticmethod
    def item_select(L):
        lua_pushboolean(L, 0)
        if not lua_isnumber(L, 1):
            return 1
        id = lua_tonumber(L, 1)
        item = ITEM_MANAGER.instance().Find(id)

        if item is None:
            return 1

        quest.CQuestManager.instance().SetCurrentItem(item)
        lua_pushboolean(L, 1)

        return 1

    @staticmethod
    def item_get_id(L):
        q = quest.CQuestManager.instance()

        if q.GetCurrentItem():
            lua_pushnumber(L, q.GetCurrentItem().GetID())
        else:
            lua_pushnumber(L, 0)
        return 1

    @staticmethod
    def item_remove(L):
        q = quest.CQuestManager.instance()
        item = q.GetCurrentItem()
        if item is not None:
            if q.GetCurrentCharacterPtr() is item.GetOwner():
                ITEM_MANAGER.instance().RemoveItem(item, NULL)
            else:
                #lani_err("Tried to remove invalid item %p", Globals.get_pointer(item))
            q.ClearCurrentItem()

        return 0

    @staticmethod
    def item_rem(L):
        item = quest.CQuestManager.instance().GetCurrentItem()

        if item is None or quest.CQuestManager.instance().GetCurrentCharacterPtr() is not item.GetOwner():
            lua_pushboolean(L, 0)
            return 0

        count = int(lua_tonumber(L, 1))

        item.SetCount(item.GetCount() - count)
        lua_pushboolean(L, 1)

        return 1

    @staticmethod
    def item_get_socket(L):
        q = quest.CQuestManager.instance()
        if q.GetCurrentItem() is not None and lua_isnumber(L, 1):
            idx = int(lua_tonumber(L, 1))
            if idx < 0 or idx >= EItemMisc.LG_ITEM_SOCKET_MAX_NUM:
                lua_pushnumber(L,0)
            else:
                lua_pushnumber(L, q.GetCurrentItem().GetSocket(idx))
        else:
            lua_pushnumber(L,0)
        return 1

    @staticmethod
    def item_set_socket(L):
        q = quest.CQuestManager.instance()
        if q.GetCurrentItem() is not None and lua_isnumber(L,1) and lua_isnumber(L,2):
            idx = int(lua_tonumber(L, 1))
            value = int(lua_tonumber(L, 2))
            if idx >=0 and idx < EItemMisc.LG_ITEM_SOCKET_MAX_NUM:
                q.GetCurrentItem().SetSocket(idx, value, ((not DefineConstants.false)))
        return 0

    @staticmethod
    def item_get_vnum(L):
        q = quest.CQuestManager.instance()
        item = q.GetCurrentItem()

        if item:
            lua_pushnumber(L, item.GetVnum())
        else:
            lua_pushnumber(L, 0)

        return 1

    @staticmethod
    def item_has_flag(L):
        q = quest.CQuestManager.instance()
        item = q.GetCurrentItem()

        if not lua_isnumber(L, 1):
            #lani_err("flag is not a number.")
            lua_pushboolean(L, 0)
            return 1

        if item is None:
            lua_pushboolean(L, 0)
            return 1

        lCheckFlag = int(lua_tonumber(L, 1))
        ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'IS_SET' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
        lua_pushboolean(L, IS_SET(item.GetFlag(), lCheckFlag))

        return 1

    @staticmethod
    def item_get_value(L):
        q = quest.CQuestManager.instance()
        item = q.GetCurrentItem()

        if item is None:
            lua_pushnumber(L, 0)
            return 1

        if not lua_isnumber(L, 1):
            #lani_err("index is not a number")
            lua_pushnumber(L, 0)
            return 1

        index = int(lua_tonumber(L, 1))

        if index < 0 or index >= EItemMisc.ITEM_VALUES_MAX_NUM:
            #lani_err("index(%d) is out of range (0..%d)", index, EItemMisc.ITEM_VALUES_MAX_NUM)
            lua_pushnumber(L, 0)
        else:
            lua_pushnumber(L, item.GetValue(uint(index)))

        return 1

    @staticmethod
    def item_set_value(L):
        q = quest.CQuestManager.instance()
        item = q.GetCurrentItem()

        if item is None:
            lua_pushnumber(L, 0)
            return 1

        if LGEMiscellaneous.DEFINECONSTANTS.false == (lua_isnumber(L, 1) and lua_isnumber(L, 2) and lua_isnumber(L, 3)):
            #lani_err("index is not a number")
            lua_pushnumber(L, 0)
            return 1

        item.SetForceAttribute(lua_tonumber(L, 1), lua_tonumber(L, 2), lua_tonumber(L, 3))

        return 0

    @staticmethod
    def item_get_name(L):
        q = quest.CQuestManager.instance()
        item = q.GetCurrentItem()

        if item:
            lua_pushstring(L, item.GetName(LOCALE_LANIATUS))
        else:
            lua_pushstring(L, "")

        return 1

    @staticmethod
    def item_get_size(L):
        q = quest.CQuestManager.instance()
        item = q.GetCurrentItem()

        if item:
            lua_pushnumber(L, item.GetSize())
        else:
            lua_pushnumber(L, 0)

        return 1

    @staticmethod
    def item_get_count(L):
        q = quest.CQuestManager.instance()
        item = q.GetCurrentItem()

        if item:
            lua_pushnumber(L, item.GetCount())
        else:
            lua_pushnumber(L, 0)

        return 1

    @staticmethod
    def item_get_type(L):
        q = quest.CQuestManager.instance()
        item = q.GetCurrentItem()

        if item:
            lua_pushnumber(L, item.GetType())
        else:
            lua_pushnumber(L, 0)

        return 1

    @staticmethod
    def item_get_sub_type(L):
        q = quest.CQuestManager.instance()
        item = q.GetCurrentItem()

        if item:
            lua_pushnumber(L, item.GetSubType())
        else:
            lua_pushnumber(L, 0)

        return 1

    @staticmethod
    def item_get_refine_vnum(L):
        q = quest.CQuestManager.instance()
        item = q.GetCurrentItem()

        if item:
            lua_pushnumber(L, item.GetRefinedVnum())
        else:
            lua_pushnumber(L, 0)

        return 1

    @staticmethod
    def item_next_refine_vnum(L):
        vnum = 0
        if lua_isnumber(L, 1):
            vnum = lua_tonumber(L, 1)

        pTable = ITEM_MANAGER.instance().GetTable(vnum)
        if pTable:
            lua_pushnumber(L, pTable.dwRefinedVnum)
        else:
            #lani_err("Cannot find item table of vnum %u", vnum)
            lua_pushnumber(L, 0)
        return 1

    @staticmethod
    def item_get_level(L):
        q = quest.CQuestManager.instance()
        item = q.GetCurrentItem()

        if item:
            lua_pushnumber(L, item.GetRefineLevel())
        else:
            lua_pushnumber(L, 0)

        return 1

    @staticmethod
    def item_get_level_limit(L):
        q = quest.CQuestManager.instance()

        if q.GetCurrentItem():
            if q.GetCurrentItem().GetType() != EItemTypes.ITEM_WEAPON and q.GetCurrentItem().GetType() != EItemTypes.ITEM_ARMOR:
                return 0
            lua_pushnumber(L, q.GetCurrentItem().GetLevelLimit())
            return 1
        return 0

    @staticmethod
    def item_start_realtime_expire(L):
        q = quest.CQuestManager.instance()
        pItem = q.GetCurrentItem()

        if pItem:
            pItem.StartRealTimeExpireEvent()
            return 1

        return 0

    @staticmethod
    def get_attr(L):
        item = quest.CQuestManager.instance().GetCurrentItem()
        if (not lua_isnumber(L,1)) or item is None:
            return 0
        attr_index = lua_tonumber(L,1)
        if attr_index <0 or attr_index > 6:
            return 0
        attr = item.GetAttribute(attr_index)
        lua_pushnumber(L,attr.bType)
        lua_pushnumber(L,attr.sValue)
        return 2
    @staticmethod
    def set_attr(L):
        item = quest.CQuestManager.instance().GetCurrentItem()
        if (not lua_isnumber(L,1)) or (not lua_isnumber(L,2)) or (not lua_isnumber(L,3)) or item is None:
            lua_pushboolean(L,0)
            return 1
        attr_index = lua_tonumber(L,1)
        if attr_index <0 or attr_index > 6:
            lua_pushboolean(L,0)
            return 1
        item.SetForceAttribute(attr_index, lua_tonumber(L,2), lua_tonumber(L,3))
        lua_pushboolean(L,1)
        return 1

    @staticmethod
    def item_get_attr_value(L):
        q = quest.CQuestManager.instance()
        item = q.GetCurrentItem()

        if item is None:
            #lani_err("cannot get current item")
            lua_pushnumber(L, 0)
            return 1

        if LGEMiscellaneous.DEFINECONSTANTS.false == lua_isnumber(L, 1):
            #lani_err("index is not a number")
            lua_pushnumber(L, 0)
            return 1

        index = lua_tonumber(L, 1)
        attrItem = item.GetAttribute(index)

        lua_pushnumber(L, attrItem.sValue)

        return 1

    @staticmethod
    def item_get_attr_type(L):
        q = quest.CQuestManager.instance()
        item = q.GetCurrentItem()

        if item is None:
            #lani_err("cannot get current item")
            lua_pushnumber(L, 0)
            return 1

        if LGEMiscellaneous.DEFINECONSTANTS.false == lua_isnumber(L, 1):
            #lani_err("index is not a number")
            lua_pushnumber(L, 0)
            return 1

        index = lua_tonumber(L, 1)
        attrItem = item.GetAttribute(index)

        lua_pushnumber(L, attrItem.bType)

        return 1

    @staticmethod
    def item_copy_and_give_before_remove(L):
        lua_pushboolean(L, 0)
        if not lua_isnumber(L, 1):
            return 1

        vnum = lua_tonumber(L, 1)

        q = quest.CQuestManager.instance()
        pItem = q.GetCurrentItem()
        pChar = q.GetCurrentCharacterPtr()

        pkNewItem = ITEM_MANAGER.instance().CreateItem(vnum, 1, 0, LGEMiscellaneous.DEFINECONSTANTS.false, -1, DefineConstants.false)

        if pkNewItem:
            ITEM_MANAGER.CopyAllAttrTo(pItem, pkNewItem)
            wCell = pItem.GetCell()

            ITEM_MANAGER.instance().RemoveItem(pItem, "REMOVE (COPY SUCCESS)")

            pkNewItem.AddToCharacter(pChar, TItemPos(EWindows.INVENTORY, wCell))
            ITEM_MANAGER.instance().FlushDelayedSave(pkNewItem)
            lua_pushboolean(L, 1)

        return 1

    @staticmethod
    def RegisterITEMFunctionTable():

        item_functions = [luaL_reg("get_id", item_get_id), luaL_reg("get_cell", item_get_cell), luaL_reg("select", item_select), luaL_reg("select_cell", item_select_cell), luaL_reg("remove", item_remove), luaL_reg("rem", item_rem), luaL_reg("get_socket", item_get_socket), luaL_reg("set_socket", item_set_socket), luaL_reg("get_vnum", item_get_vnum), luaL_reg("has_flag", item_has_flag), luaL_reg("get_value", item_get_value), luaL_reg("set_value", item_set_value), luaL_reg("get_name", item_get_name), luaL_reg("get_size", item_get_size), luaL_reg("attr_value", item_get_attr_value), luaL_reg("attr_type", item_get_attr_type), luaL_reg("set_attr", set_attr), luaL_reg("get_attr", get_attr), luaL_reg("get_count", item_get_count), luaL_reg("get_type", item_get_type), luaL_reg("get_sub_type", item_get_sub_type), luaL_reg("get_refine_vnum", item_get_refine_vnum), luaL_reg("get_level", item_get_level), luaL_reg("next_refine_vnum", item_next_refine_vnum), luaL_reg("get_level_limit", item_get_level_limit), luaL_reg("start_realtime_expire", item_start_realtime_expire), luaL_reg("copy_and_give_before_remove", item_copy_and_give_before_remove), luaL_reg(None, None)]
        quest.CQuestManager.instance().AddLuaFunctionTable("item", item_functions)
