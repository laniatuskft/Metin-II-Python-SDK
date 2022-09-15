from building import *

class quest: #this class replaces the original namespace 'quest'
    @staticmethod
    def building_get_land_id(L):

        if (not lua_isnumber(L, 1)) or (not lua_isnumber(L, 2)) or not lua_isnumber(L, 3):
            #lani_err("invalid argument")
            lua_pushnumber(L, 0)
            return 1

        pkLand = building.CManager.instance().FindLand(int(lua_tonumber(L, 1)), int(lua_tonumber(L, 2)), int(lua_tonumber(L, 3)))
        lua_pushnumber(L,pkLand.GetID() if pkLand is not None else 0)
        return 1

    @staticmethod
    def building_get_land_info(L):
        price = 1000000000
        owner = 1000000000
        level_limit = 1000000000

        if lua_isnumber(L, 1):

            pkLand = building.CManager.instance().FindLand(lua_tonumber(L, 1))

            if pkLand:
                t = pkLand.GetData()

                price = t.lldPrice
                owner = t.dwGuildID
                level_limit = t.bGuildLevelLimit
        else:
            #lani_err("invalid argument")

        lua_pushnumber(L, price)
        lua_pushnumber(L, owner)
        lua_pushnumber(L, level_limit)
        return 3

    @staticmethod
    def building_set_land_owner(L):
        if (not lua_isnumber(L, 1)) or not lua_isnumber(L, 2):
            #lani_err("invalid argument")
            return 0


        pkLand = building.CManager.instance().FindLand(lua_tonumber(L, 1))

        if pkLand:
            if pkLand.GetData().dwGuildID == 0:
                pkLand.SetOwner(lua_tonumber(L, 2))

        return 0

    @staticmethod
    def building_has_land(L):

        if not lua_isnumber(L, 1):
            #lani_err("invalid argument")
            lua_pushboolean(L, ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
            return 1

        pmsg = std::unique_ptr(DBManager.instance().DirectQuery("SELECT COUNT(*) FROM land%s WHERE guild_id = %d", get_table_postfix(), lua_tonumber(L,1)))

        if pmsg.Get().uiNumRows > 0:
            row = mysql_fetch_row(pmsg.Get().pSQLResult)

            count = 0
            temp_ref_count = RefObject(count);
            Globals.str_to_number(temp_ref_count, row[0])
            count = temp_ref_count.arg_value

            if count == 0:
                lua_pushboolean(L, LGEMiscellaneous.DEFINECONSTANTS.false)
            else:
                lua_pushboolean(L, ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
        else:
            lua_pushboolean(L, ((not LGEMiscellaneous.DEFINECONSTANTS.false)))

        return 1

    @staticmethod
    def building_reconstruct(L):

        dwNewBuilding = lua_tonumber(L, 1)

        q = quest.CQuestManager.instance()

        npc = q.GetCurrentNPCCharacterPtr()
        if npc is None:
            return 0

        pGuild = npc.GetGuild()
        if pGuild is None:
            return 0

        pLand = building.CManager.instance().FindLandByGuild(pGuild.GetID())
        if pLand is None:
            return 0

        pObject = pLand.FindObjectByNPC(npc)
        if pObject is None:
            return 0

        pObject.Reconstruct(dwNewBuilding)

        return 0

    @staticmethod
    def RegisterBuildingFunctionTable():
        functions = [luaL_reg("get_land_id", building_get_land_id), luaL_reg("get_land_info", building_get_land_info), luaL_reg("set_land_owner", building_set_land_owner), luaL_reg("has_land", building_has_land), luaL_reg("reconstruct", building_reconstruct), luaL_reg(None, None)]

        quest.CQuestManager.instance().AddLuaFunctionTable("building", functions)
