import math

def ForEachMember(f):
    it = m_set_pkCharacter.begin()
    while it is not m_set_pkCharacter.end():
        #sys_log(0, "Dungeon ForEachMember %s", it.GetName())
        f(*it)
        it += 1
    return f

class quest: #this class replaces the original namespace 'quest'
    @staticmethod
    def dungeon_notice(L):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if ! __MULTI_LANGUAGE_SYSTEM__
        if not lua_isstring(L, 1):
            return 0
##endif

        q = quest.CQuestManager.instance()
        pDungeon = q.GetCurrentDungeon()

        if pDungeon:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if __MULTI_LANGUAGE_SYSTEM__
            pDungeon.Notice(lua_tostring(L, 1), lua_tostring(L, 2), lua_tostring(L, 3), lua_tostring(L, 4), lua_tostring(L, 5), lua_tostring(L, 6), lua_tostring(L, 7), lua_tostring(L, 8), lua_tostring(L, 9), lua_tostring(L, 10))
##else
            pDungeon.Notice(lua_tostring(L, 1))
##endif
            return 0

        int quest.dungeon_set_quest_flag(lua_State* L)
            q = quest.CQuestManager.instance()

            f = FSetQuestFlag()

            f.flagname = q.GetCurrentPC().GetCurrentQuestName() + "." + lua_tostring(L, 1)
            f.value = int(rint(lua_tonumber(L, 2)))

            pDungeon = q.GetCurrentDungeon()

            if pDungeon:
                pDungeon.ForEachMember(f.functor_method)

            return 0

        int quest.dungeon_set_flag(lua_State* L)
            if (not lua_isstring(L,1)) or not lua_isnumber(L,2):
                #lani_err("wrong set flag")
            else:
                q = quest.CQuestManager.instance()
                pDungeon = q.GetCurrentDungeon()

                if pDungeon:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to pointers to value types:
#ORIGINAL METINII C CODE: const char* sz = lua_tostring(L,1);
                    sz = lua_tostring(L,1)
                    value = lua_tonumber(L, 2)
                    pDungeon.SetFlag(sz, value)
                else:
                    #lani_err("no dungeon !!!")
            return 0

        int quest.dungeon_get_flag(lua_State* L)
            if not lua_isstring(L,1):
                #lani_err("wrong get flag")

            q = quest.CQuestManager.instance()
            pDungeon = q.GetCurrentDungeon()

            if pDungeon:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to pointers to value types:
#ORIGINAL METINII C CODE: const char* sz = lua_tostring(L,1);
                sz = lua_tostring(L,1)
                lua_pushnumber(L, pDungeon.GetFlag(sz))
            else:
                #lani_err("no dungeon !!!")
                lua_pushnumber(L, 0)

            return 1

        int quest.dungeon_get_flag_from_map_index(lua_State* L)
            if (not lua_isstring(L,1)) or not lua_isnumber(L,2):
                #lani_err("wrong get flag")

            dwMapIndex = lua_tonumber(L, 2)
            if dwMapIndex != 0:
                pDungeon = CDungeonManager.instance().FindByMapIndex(int(dwMapIndex))
                if pDungeon:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to pointers to value types:
#ORIGINAL METINII C CODE: const char* sz = lua_tostring(L,1);
                    sz = lua_tostring(L,1)
                    lua_pushnumber(L, pDungeon.GetFlag(sz))
                else:
                    #lani_err("no dungeon !!!")
                    lua_pushnumber(L, 0)
            else:
                lua_pushboolean(L, 0)
            return 1

        int quest.dungeon_get_map_index(lua_State* L)
            q = quest.CQuestManager.instance()
            pDungeon = q.GetCurrentDungeon()

            if pDungeon:
                #sys_log(0, "Dungeon GetMapIndex %d",pDungeon.GetMapIndex())
                lua_pushnumber(L, pDungeon.GetMapIndex())
            else:
                #lani_err("no dungeon !!!")
                lua_pushnumber(L, 0)

            return 1

        int quest.dungeon_regen_file(lua_State* L)
            if not lua_isstring(L,1):
                #lani_err("wrong filename")
                return 0

            q = quest.CQuestManager.instance()
            pDungeon = q.GetCurrentDungeon()

            if pDungeon:
                pDungeon.SpawnRegen(lua_tostring(L,1), ((not DefineConstants.false)))

            return 0

        int quest.dungeon_set_regen_file(lua_State* L)
            if not lua_isstring(L,1):
                #lani_err("wrong filename")
                return 0
            q = quest.CQuestManager.instance()
            pDungeon = q.GetCurrentDungeon()

            if pDungeon:
                pDungeon.SpawnRegen(lua_tostring(L,1), LGEMiscellaneous.DEFINECONSTANTS.false)
            return 0

        int quest.dungeon_clear_regen(lua_State* L)
            q = quest.CQuestManager.instance()
            pDungeon = q.GetCurrentDungeon()
            if pDungeon:
                pDungeon.ClearRegen()
            return 0

        int quest.dungeon_check_eliminated(lua_State* L)
            q = quest.CQuestManager.instance()
            pDungeon = q.GetCurrentDungeon()
            if pDungeon:
                pDungeon.CheckEliminated()
            return 0

        int quest.dungeon_set_exit_all_at_eliminate(lua_State* L)
            if not lua_isnumber(L,1):
                #lani_err("wrong time")
                return 0

            q = quest.CQuestManager.instance()
            pDungeon = q.GetCurrentDungeon()

            if pDungeon:
                pDungeon.SetExitAllAtEliminate(int(lua_tonumber(L, 1)))

            return 0

        int quest.dungeon_set_warp_at_eliminate(lua_State* L)
            if not lua_isnumber(L, 1):
                #lani_err("wrong time")
                return 0

            if not lua_isnumber(L, 2):
                #lani_err("wrong map index")
                return 0

            if not lua_isnumber(L, 3):
                #lani_err("wrong X")
                return 0

            if not lua_isnumber(L, 4):
                #lani_err("wrong Y")
                return 0

            c_pszRegenFile = None

            if lua_gettop(L) >= 5:
                c_pszRegenFile = lua_tostring(L,5)

            q = quest.CQuestManager.instance()
            pDungeon = q.GetCurrentDungeon()

            if pDungeon:
                pDungeon.SetWarpAtEliminate(int(lua_tonumber(L,1)), int(lua_tonumber(L,2)), int(lua_tonumber(L,3)), int(lua_tonumber(L,4)), c_pszRegenFile)
            else:
                #lani_err("cannot find dungeon")

            return 0

        int quest.dungeon_new_jump(lua_State* L)
            if lua_gettop(L) < 3:
                #lani_err("not enough argument")
                return 0

            if (not lua_isnumber(L, 1)) or (not lua_isnumber(L, 2)) or not lua_isnumber(L, 3):
                #lani_err("wrong argument")
                return 0

            lMapIndex = int(lua_tonumber(L,1))

            pDungeon = CDungeonManager.instance().Create(lMapIndex)

            if pDungeon is None:
                #lani_err("cannot create dungeon %d", lMapIndex)
                return 0

            ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()
            ch.WarpSet(int(lua_tonumber(L, 2)), int(lua_tonumber(L, 3)), pDungeon.GetMapIndex())
            return 0

        int quest.dungeon_new_jump_all(lua_State* L)
            if lua_gettop(L)<3 or (not lua_isnumber(L,1)) or (not lua_isnumber(L, 2)) or not lua_isnumber(L,3):
                #lani_err("not enough argument")
                return 0

            lMapIndex = int(lua_tonumber(L,1))

            pDungeon = CDungeonManager.instance().Create(lMapIndex)

            if pDungeon is None:
                #lani_err("cannot create dungeon %d", lMapIndex)
                return 0

            ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()

            pDungeon.JumpAll(ch.GetMapIndex(), int(lua_tonumber(L, 2)), int(lua_tonumber(L, 3)))

            return 0

        int quest.dungeon_new_jump_party(lua_State* L)
            if lua_gettop(L)<3 or (not lua_isnumber(L,1)) or (not lua_isnumber(L, 2)) or not lua_isnumber(L,3):
                #lani_err("not enough argument")
                return 0

            lMapIndex = int(lua_tonumber(L,1))

            pDungeon = CDungeonManager.instance().Create(lMapIndex)

            if pDungeon is None:
                #lani_err("cannot create dungeon %d", lMapIndex)
                return 0

            ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()

            if ch.GetParty() is None:
                #lani_err("cannot go to dungeon alone.")
                return 0
            pDungeon.JumpParty(ch.GetParty(), ch.GetMapIndex(), int(lua_tonumber(L, 2)), int(lua_tonumber(L, 3)))

            return 0

        int quest.dungeon_jump_all(lua_State* L)
            if lua_gettop(L)<2 or (not lua_isnumber(L, 1)) or not lua_isnumber(L,2):
                return 0

            pDungeon = quest.CQuestManager.instance().GetCurrentDungeon()

            if pDungeon is None:
                return 0

            pDungeon.JumpAll(pDungeon.GetMapIndex(), int(lua_tonumber(L, 1)), int(lua_tonumber(L, 2)))
            return 0

        int quest.dungeon_warp_all(lua_State* L)
            if lua_gettop(L)<2 or (not lua_isnumber(L, 1)) or not lua_isnumber(L,2):
                return 0

            pDungeon = quest.CQuestManager.instance().GetCurrentDungeon()

            if pDungeon is None:
                return 0

            pDungeon.WarpAll(pDungeon.GetMapIndex(), int(lua_tonumber(L, 1)), int(lua_tonumber(L, 2)))
            return 0

        int quest.dungeon_get_kill_stone_count(lua_State* L)
            if (not lua_isnumber(L,1)) or not lua_isnumber(L,2):
                lua_pushnumber(L, 0)
                return 1


            q = quest.CQuestManager.instance()
            pDungeon = q.GetCurrentDungeon()

            if pDungeon:
                lua_pushnumber(L, pDungeon.GetKillStoneCount())
                return 1

            lua_pushnumber(L, 0)
            return 1

        int quest.dungeon_get_kill_mob_count(lua_State * L)
            if (not lua_isnumber(L,1)) or not lua_isnumber(L,2):
                lua_pushnumber(L, 0)
                return 1

            q = quest.CQuestManager.instance()
            pDungeon = q.GetCurrentDungeon()

            if pDungeon:
                lua_pushnumber(L, pDungeon.GetKillMobCount())
                return 1

            lua_pushnumber(L, 0)
            return 1

        int quest.dungeon_is_use_potion(lua_State* L)
            if (not lua_isnumber(L, 1)) or not lua_isnumber(L, 2):
                lua_pushboolean(L, 1)
                return 1

            q = quest.CQuestManager.instance()
            pDungeon = q.GetCurrentDungeon()

            if pDungeon:
                lua_pushboolean(L, pDungeon.IsUsePotion())
                return 1

            lua_pushboolean(L, 1)
            return 1

        int quest.dungeon_revived(lua_State* L)
            if (not lua_isnumber(L,1)) or not lua_isnumber(L,2):
                lua_pushboolean(L, 1)
                return 1

            q = quest.CQuestManager.instance()
            pDungeon = q.GetCurrentDungeon()

            if pDungeon:
                lua_pushboolean(L, pDungeon.IsUseRevive())
                return 1

            lua_pushboolean(L, 1)
            return 1

        int quest.dungeon_set_dest(lua_State* L)
            if (not lua_isnumber(L,1)) or not lua_isnumber(L,2):
                return 0

            ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()

            pParty = ch.GetParty()
            q = quest.CQuestManager.instance()
            pDungeon = q.GetCurrentDungeon()

            if pDungeon is not None and pParty is not None:
                pDungeon.SendDestPositionToParty(pParty, int(lua_tonumber(L,1)), int(lua_tonumber(L,2)))

            return 0

        int quest.dungeon_unique_set_maxhp(lua_State* L)
            if (not lua_isstring(L,1)) or not lua_isnumber(L,2):
                return 0

            q = quest.CQuestManager.instance()
            pDungeon = q.GetCurrentDungeon()

            if pDungeon:
                pDungeon.UniqueSetMaxHP(lua_tostring(L,1), int(lua_tonumber(L,2)))

            return 0

        int quest.dungeon_unique_set_hp(lua_State* L)
            if (not lua_isstring(L,1)) or not lua_isnumber(L,2):
                return 0

            q = quest.CQuestManager.instance()
            pDungeon = q.GetCurrentDungeon()

            if pDungeon:
                pDungeon.UniqueSetHP(lua_tostring(L,1), int(lua_tonumber(L,2)))

            return 0

        int quest.dungeon_unique_set_def_grade(lua_State* L)
            if (not lua_isstring(L,1)) or not lua_isnumber(L,2):
                return 0

            q = quest.CQuestManager.instance()
            pDungeon = q.GetCurrentDungeon()

            if pDungeon:
                pDungeon.UniqueSetDefGrade(lua_tostring(L,1), int(lua_tonumber(L,2)))

            return 0

        int quest.dungeon_unique_get_hp_perc(lua_State* L)
            if not lua_isstring(L,1):
                lua_pushnumber(L,0)
                return 1

            q = quest.CQuestManager.instance()
            pDungeon = q.GetCurrentDungeon()

            if pDungeon:
                lua_pushnumber(L, pDungeon.GetUniqueHpPerc(lua_tostring(L,1)))
                return 1

            lua_pushnumber(L,0)
            return 1

        int quest.dungeon_is_unique_dead(lua_State* L)
            if not lua_isstring(L,1):
                lua_pushboolean(L, 0)
                return 1

            q = quest.CQuestManager.instance()
            pDungeon = q.GetCurrentDungeon()

            if pDungeon:
                lua_pushboolean(L,1 if pDungeon.IsUniqueDead(lua_tostring(L,1)) 1 else 0)
                return 1

            lua_pushboolean(L, 0)
            return 1

        int quest.dungeon_purge_unique(lua_State* L)
            if not lua_isstring(L,1):
                return 0
            #sys_log(0,"QUEST_DUNGEON_PURGE_UNIQUE %s", lua_tostring(L,1))

            q = quest.CQuestManager.instance()
            pDungeon = q.GetCurrentDungeon()

            if pDungeon:
                pDungeon.PurgeUnique(lua_tostring(L,1))

            return 0

        struct FPurgeArea
            x1 = None
            y1 = None
            x2 = None
            y2 = None
            ExceptChar = None

            FPurgeArea(int a, int b, int c, int d, CHARACTER* p) : x1(a), y1(b), x2(c), y2(d), ExceptChar(p)

            void operator ()(CEntity* ent)
                if ((not LGEMiscellaneous.DEFINECONSTANTS.false)) == ent.IsType(EEntityTypes.ENTITY_CHARACTER):
                    pChar = ent

                    if pChar is ExceptChar:
                        return

                    if (not pChar.IsPet()) and (((not LGEMiscellaneous.DEFINECONSTANTS.false)) == pChar.IsMonster() or ((not LGEMiscellaneous.DEFINECONSTANTS.false)) == pChar.IsStone()):
                        if x1 <= pChar.GetX() and pChar.GetX() <= x2 and y1 <= pChar.GetY() and pChar.GetY() <= y2:
                            pChar.Dead(NULL, DefineConstants.false)

        int quest.dungeon_purge_area(lua_State* L)
            if (not lua_isnumber(L,1)) or (not lua_isnumber(L,2)) or (not lua_isnumber(L,3)) or not lua_isnumber(L,4):
                return 0
            #sys_log(0,"QUEST_DUNGEON_PURGE_AREA")

            x1 = lua_tonumber(L, 1)
            y1 = lua_tonumber(L, 2)
            x2 = lua_tonumber(L, 3)
            y2 = lua_tonumber(L, 4)

            q = quest.CQuestManager.instance()
            pDungeon = q.GetCurrentDungeon()

            mapIndex = pDungeon.GetMapIndex()

            if 0 == mapIndex:
                #lani_err("_purge_area: cannot get a map index with (%u, %u)", x1, y1)
                return 0

            pSectree = SECTREE_MANAGER.instance().GetMap(mapIndex)

            if None is not pSectree:
                func = FPurgeArea(x1, y1, x2, y2, quest.CQuestManager.instance().GetCurrentNPCCharacterPtr())

                pSectree.for_each(func.functor_method)

            return 0

        int quest.dungeon_kill_unique(lua_State* L)
            if not lua_isstring(L,1):
                return 0
            #sys_log(0,"QUEST_DUNGEON_KILL_UNIQUE %s", lua_tostring(L,1))

            q = quest.CQuestManager.instance()
            pDungeon = q.GetCurrentDungeon()

            if pDungeon:
                pDungeon.KillUnique(lua_tostring(L,1))

            return 0

        int quest.dungeon_spawn_stone_door(lua_State* L)
            if (not lua_isstring(L,1)) or not lua_isstring(L,2):
                return 0
            #sys_log(0,"QUEST_DUNGEON_SPAWN_STONE_DOOR %s %s", lua_tostring(L,1), lua_tostring(L,2))

            q = quest.CQuestManager.instance()
            pDungeon = q.GetCurrentDungeon()

            if pDungeon:
                pDungeon.SpawnStoneDoor(lua_tostring(L,1), lua_tostring(L,2))

            return 0

        int quest.dungeon_spawn_wooden_door(lua_State* L)
            if (not lua_isstring(L,1)) or not lua_isstring(L,2):
                return 0
            #sys_log(0,"QUEST_DUNGEON_SPAWN_WOODEN_DOOR %s %s", lua_tostring(L,1), lua_tostring(L,2))

            q = quest.CQuestManager.instance()
            pDungeon = q.GetCurrentDungeon()

            if pDungeon:
                pDungeon.SpawnWoodenDoor(lua_tostring(L,1), lua_tostring(L,2))

            return 0

        int quest.dungeon_spawn_move_group(lua_State* L)
            if (not lua_isnumber(L,1)) or (not lua_isstring(L,2)) or not lua_isstring(L,3):
                return 0
            #sys_log(0,"QUEST_DUNGEON_SPAWN_MOVE_GROUP %d %s %s", int(lua_tonumber(L,1)), lua_tostring(L,2), lua_tostring(L,3))

            q = quest.CQuestManager.instance()
            pDungeon = q.GetCurrentDungeon()

            if pDungeon:
                pDungeon.SpawnMoveGroup(lua_tonumber(L,1), lua_tostring(L,2), lua_tostring(L,3), 1)

            return 0

        int quest.dungeon_spawn_move_unique(lua_State* L)
            if (not lua_isstring(L,1)) or (not lua_isnumber(L,2)) or (not lua_isstring(L,3)) or not lua_isstring(L,4):
                return 0
            #sys_log(0,"QUEST_DUNGEON_SPAWN_MOVE_UNIQUE %s %d %s %s", lua_tostring(L,1), int(lua_tonumber(L,2)), lua_tostring(L,3), lua_tostring(L,4))

            q = quest.CQuestManager.instance()
            pDungeon = q.GetCurrentDungeon()

            if pDungeon:
                pDungeon.SpawnMoveUnique(lua_tostring(L,1), lua_tonumber(L,2), lua_tostring(L,3), lua_tostring(L,4))

            return 0

        int quest.dungeon_spawn_unique(lua_State* L)
            if (not lua_isstring(L,1)) or (not lua_isnumber(L,2)) or not lua_isstring(L,3):
                return 0
            #sys_log(0,"QUEST_DUNGEON_SPAWN_UNIQUE %s %d %s", lua_tostring(L,1), int(lua_tonumber(L,2)), lua_tostring(L,3))

            q = quest.CQuestManager.instance()
            pDungeon = q.GetCurrentDungeon()

            if pDungeon:
                pDungeon.SpawnUnique(lua_tostring(L,1), lua_tonumber(L,2), lua_tostring(L,3))

            return 0

        int quest.dungeon_spawn(lua_State* L)
            if (not lua_isnumber(L,1)) or not lua_isstring(L,2):
                return 0
            #sys_log(0,"QUEST_DUNGEON_SPAWN %d %s", int(lua_tonumber(L,1)), lua_tostring(L,2))

            q = quest.CQuestManager.instance()
            pDungeon = q.GetCurrentDungeon()

            if pDungeon:
                pDungeon.Spawn(lua_tonumber(L,1), lua_tostring(L,2))

            return 0

        int quest.dungeon_set_unique(lua_State* L)
            if (not lua_isstring(L, 1)) or not lua_isnumber(L, 2):
                return 0

            q = quest.CQuestManager.instance()
            pDungeon = q.GetCurrentDungeon()

            vid = lua_tonumber(L, 2)

            if pDungeon:
                pDungeon.SetUnique(lua_tostring(L, 1), vid)
            return 0

        int quest.dungeon_get_unique_vid(lua_State* L)
            if not lua_isstring(L,1):
                lua_pushnumber(L,0)
                return 1

            q = quest.CQuestManager.instance()
            pDungeon = q.GetCurrentDungeon()

            if pDungeon:
                lua_pushnumber(L, pDungeon.GetUniqueVid(lua_tostring(L,1)))
                return 1

            lua_pushnumber(L,0)
            return 1

        int quest.dungeon_spawn_mob(lua_State* L)
            if (not lua_isnumber(L, 1)) or (not lua_isnumber(L, 2)) or not lua_isnumber(L, 3):
                #lani_err("invalid argument")
                return 0

            q = quest.CQuestManager.instance()
            pDungeon = q.GetCurrentDungeon()

            vid = 0

            if pDungeon:
                dwVnum = lua_tonumber(L, 1)
                x = int(lua_tonumber(L, 2))
                y = int(lua_tonumber(L, 3))
                radius = float(lua_tonumber(L, 4)) if lua_isnumber(L, 4) else 0
                count = uint(lua_tonumber(L, 5) if (lua_isnumber(L, 5)) else 1)

                #sys_log(0, "dungeon_spawn_mob %u %d %d", dwVnum, x, y)

                if count == 0:
                    count = 1

## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: while (count --)
                while (count ) != 0:
                    count -= 1
                    if radius<1:
                        ch = pDungeon.SpawnMob(dwVnum, x, y, 0)
                        if ch is not None and vid == 0:
                            vid = ch.GetVID()
                    else:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
                        angle = number(0, 999) * LGEMiscellaneous.DEFINECONSTANTS.M_PI * 2 / 1000
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
                        r = number(0, 999) * radius / 1000

                        nx = x + int((r * math.cos(angle)))
                        ny = y + int((r * math.sin(angle)))

                        ch = pDungeon.SpawnMob(dwVnum, nx, ny, 0)
                        if ch is not None and vid == 0:
                            vid = ch.GetVID()
                count -= 1

            lua_pushnumber(L, vid)
            return 1

        int quest.dungeon_spawn_mob_dir(lua_State* L)
            if (not lua_isnumber(L, 1)) or (not lua_isnumber(L, 2)) or (not lua_isnumber(L, 3)) or not lua_isnumber(L, 4):
                #lani_err("invalid argument")
                return 0

            q = quest.CQuestManager.instance()
            pDungeon = q.GetCurrentDungeon()

            vid = 0

            if pDungeon:
                dwVnum = lua_tonumber(L, 1)
                x = int(lua_tonumber(L, 2))
                y = int(lua_tonumber(L, 3))
                dir = byte(int(lua_tonumber(L, 4)))

                ch = pDungeon.SpawnMob(dwVnum, x, y, dir)
                if ch is not None and vid == 0:
                    vid = ch.GetVID()
            lua_pushnumber(L, vid)
            return 1

        int quest.dungeon_spawn_mob_ac_dir(lua_State* L)
            if (not lua_isnumber(L, 1)) or (not lua_isnumber(L, 2)) or (not lua_isnumber(L, 3)) or not lua_isnumber(L, 4):
                #lani_err("invalid argument")
                return 0

            q = quest.CQuestManager.instance()
            pDungeon = q.GetCurrentDungeon()

            vid = 0

            if pDungeon:
                dwVnum = lua_tonumber(L, 1)
                x = int(lua_tonumber(L, 2))
                y = int(lua_tonumber(L, 3))
                dir = byte(int(lua_tonumber(L, 4)))

                ch = pDungeon.SpawnMob_ac_dir(dwVnum, x, y, dir)
                if ch is not None and vid == 0:
                    vid = ch.GetVID()
            lua_pushnumber(L, vid)
            return 1

        int quest.dungeon_spawn_goto_mob(lua_State* L)
            if (not lua_isnumber(L, 1)) or (not lua_isnumber(L, 2)) or (not lua_isnumber(L, 3)) or not lua_isnumber(L, 4):
                return 0

            lFromX = int(lua_tonumber(L, 1))
            lFromY = int(lua_tonumber(L, 2))
            lToX = int(lua_tonumber(L, 3))
            lToY = int(lua_tonumber(L, 4))

            q = quest.CQuestManager.instance()
            pDungeon = q.GetCurrentDungeon()

            if pDungeon:
                pDungeon.SpawnGotoMob(lFromX, lFromY, lToX, lToY)

            return 0

        int quest.dungeon_spawn_name_mob(lua_State* L)
            if (not lua_isnumber(L, 1)) or (not lua_isnumber(L, 2)) or (not lua_isnumber(L, 3)) or not lua_isstring(L, 4):
                return 0

            q = quest.CQuestManager.instance()
            pDungeon = q.GetCurrentDungeon()

            if pDungeon:
                dwVnum = lua_tonumber(L, 1)
                x = int(lua_tonumber(L, 2))
                y = int(lua_tonumber(L, 3))
                pDungeon.SpawnNameMob(dwVnum, x, y, lua_tostring(L, 4))
            return 0

        int quest.dungeon_spawn_group(lua_State* L)
            if (not lua_isnumber(L, 1)) or (not lua_isnumber(L, 2)) or (not lua_isnumber(L, 3)) or (not lua_isnumber(L, 4)) or not lua_isnumber(L, 6):
                #lani_err("invalid argument")
                return 0

            vid = 0

            q = quest.CQuestManager.instance()
            pDungeon = q.GetCurrentDungeon()

            if pDungeon:
                group_vnum = lua_tonumber(L, 1)
                local_x = int(lua_tonumber(L, 2)) * 100
                local_y = int(lua_tonumber(L, 3)) * 100
                radius = float(lua_tonumber(L, 4)) * 100
                bAggressive = lua_toboolean(L, 5)
                count = lua_tonumber(L, 6)

                chRet = pDungeon.SpawnGroup(group_vnum, local_x, local_y, radius, bAggressive, int(count))
                if chRet:
                    vid = chRet.GetVID()

            lua_pushnumber(L, vid)
            return 1

        int quest.dungeon_join(lua_State* L)
            if lua_gettop(L) < 1 or not lua_isnumber(L, 1):
                return 0

            lMapIndex = int(lua_tonumber(L, 1))
            pDungeon = CDungeonManager.instance().Create(lMapIndex)

            if pDungeon is None:
                return 0

            ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()

            if ch.GetParty() is not None and ch.GetParty().GetLeaderPID() == ch.GetPlayerID():
                pDungeon.JoinParty(ch.GetParty())
            elif ch.GetParty() is None:
                pDungeon.Join(ch)

            return 0

        int quest.dungeon_exit(lua_State* L)
            ch = quest.CQuestManager.instance().GetCurrentCharacterPtr()

            ch.ExitToSavedLocation()
            return 0

        int quest.dungeon_exit_all(lua_State* L)
            q = quest.CQuestManager.instance()
            pDungeon = q.GetCurrentDungeon()

            if pDungeon:
                pDungeon.ExitAll()

            return 0

        struct FSayDungeonByItemGroup
            item_group = None
            can_enter_ment = ""
            cant_enter_ment = ""
            void operator ()(CEntity* ent)
                if ent.IsType(EEntityTypes.ENTITY_CHARACTER):
                    ch = ent

                    if ch.IsPC():
                        packet_script = struct.packet_script()
                        buf = TEMP_BUFFER(8192, DefineConstants.false)

                        it = item_group.begin()
                        while it is not item_group.end():
                            if ch.CountSpecifyItem(it.first, -1) >= it.second:
                                packet_script.header = Globals.LG_HEADER_GC_SCRIPT
                                packet_script.skin = quest.CQuestManager.QUEST_SKIN_NORMAL
                                packet_script.src_size = len(can_enter_ment)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                                packet_script.size = packet_script.src_size + sizeof(packet_script)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                                buf.write(packet_script, sizeof(packet_script))
                                buf.write(can_enter_ment[0], len(can_enter_ment))
                                ch.GetDesc().Packet(buf.read_peek(), buf.size())
                                return
                            it += 1

                        packet_script.header = Globals.LG_HEADER_GC_SCRIPT
                        packet_script.skin = quest.CQuestManager.QUEST_SKIN_NORMAL
                        packet_script.src_size = len(cant_enter_ment)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                        packet_script.size = packet_script.src_size + sizeof(packet_script)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                        buf.write(packet_script, sizeof(packet_script))
                        buf.write(cant_enter_ment[0], len(cant_enter_ment))
                        ch.GetDesc().Packet(buf.read_peek(), buf.size())


        int quest.dungeon_say_diff_by_item_group(lua_State* L)
            if (not lua_isstring(L, 1)) or (not lua_isstring(L, 2)) or not lua_isstring(L, 3):
                #sys_log(0, "QUEST wrong set flag")
                return 0

            q = quest.CQuestManager.instance()
            pDungeon = q.GetCurrentDungeon()

            if pDungeon is None:
                #lani_err("QUEST : no dungeon")
                return 0

            pMap = SECTREE_MANAGER.instance().GetMap(pDungeon.GetMapIndex())

            if pMap is None:
                #lani_err("cannot find map by index %d", pDungeon.GetMapIndex())
                return 0
            f = FSayDungeonByItemGroup()
            #sys_log(0,"diff_by_item")

            group_name = lua_tostring(L, 1)
            f.item_group = pDungeon.GetItemGroup(group_name)

            if f.item_group is None:
                #lani_err("invalid item group")
                return 0

            f.can_enter_ment = lua_tostring(L, 2)
            f.can_enter_ment+= "[ENTER][ENTER][ENTER][ENTER][DONE]"
            f.cant_enter_ment = lua_tostring(L, 3)
            f.cant_enter_ment+= "[ENTER][ENTER][ENTER][ENTER][DONE]"

            pMap.for_each(f.functor_method)

            return 0

        struct FExitDungeonByItemGroup
            item_group = None

            void operator ()(CEntity* ent)
                if ent.IsType(EEntityTypes.ENTITY_CHARACTER):
                    ch = ent

                    if ch.IsPC():
                        it = item_group.begin()
                        while it is not item_group.end():
                            if ch.CountSpecifyItem(it.first, -1) >= it.second:
                                return
                            it += 1
                        ch.ExitToSavedLocation()

        int quest.dungeon_exit_all_by_item_group(lua_State* L)
            if not lua_isstring(L, 1):
                #sys_log(0, "QUEST wrong set flag")
                return 0

            q = quest.CQuestManager.instance()
            pDungeon = q.GetCurrentDungeon()

            if pDungeon is None:
                #lani_err("QUEST : no dungeon")
                return 0

            pMap = SECTREE_MANAGER.instance().GetMap(pDungeon.GetMapIndex())

            if pMap is None:
                #lani_err("cannot find map by index %d", pDungeon.GetMapIndex())
                return 0
            f = FExitDungeonByItemGroup()

            group_name = lua_tostring(L, 1)
            f.item_group = pDungeon.GetItemGroup(group_name)

            if f.item_group is None:
                #lani_err("invalid item group")
                return 0

            pMap.for_each(f.functor_method)

            return 0

        struct FDeleteItemInItemGroup
            item_group = None

            void operator ()(CEntity* ent)
                if ent.IsType(EEntityTypes.ENTITY_CHARACTER):
                    ch = ent

                    if ch.IsPC():
                        it = item_group.begin()
                        while it is not item_group.end():
                            if ch.CountSpecifyItem(it.first, -1) >= it.second:
                                ch.RemoveSpecifyItem(it.first, it.second, -1)
                                return
                            it += 1

        int quest.dungeon_delete_item_in_item_group_from_all(lua_State* L)
            if not lua_isstring(L, 1):
                #sys_log(0, "QUEST wrong set flag")
                return 0

            q = quest.CQuestManager.instance()
            pDungeon = q.GetCurrentDungeon()

            if pDungeon is None:
                #lani_err("QUEST : no dungeon")
                return 0

            pMap = SECTREE_MANAGER.instance().GetMap(pDungeon.GetMapIndex())

            if pMap is None:
                #lani_err("cannot find map by index %d", pDungeon.GetMapIndex())
                return 0
            f = FDeleteItemInItemGroup()

            group_name = lua_tostring(L, 1)
            f.item_group = pDungeon.GetItemGroup(group_name)

            if f.item_group is None:
                #lani_err("invalid item group")
                return 0

            pMap.for_each(f.functor_method)

            return 0


        int quest.dungeon_kill_all(lua_State* L)
            q = quest.CQuestManager.instance()
            pDungeon = q.GetCurrentDungeon()

            if pDungeon:
                pDungeon.KillAll()

            return 0

        int quest.dungeon_purge(lua_State* L)
            q = quest.CQuestManager.instance()
            pDungeon = q.GetCurrentDungeon()

            if pDungeon:
                pDungeon.Purge()

            return 0

        int quest.dungeon_exit_all_to_start_position(lua_State * L)
            q = quest.CQuestManager.instance()
            pDungeon = q.GetCurrentDungeon()

            if pDungeon:
                pDungeon.ExitAllToStartPosition()

            return 0

        int quest.dungeon_count_monster(lua_State * L)
            q = quest.CQuestManager.instance()
            pDungeon = q.GetCurrentDungeon()

            if pDungeon:
                lua_pushnumber(L, pDungeon.CountMonster())
            else:
                #lani_err("not in a dungeon")
                lua_pushnumber(L, numeric_limits.max())

            return 1

        int quest.dungeon_select(lua_State* L)
            dwMapIndex = lua_tonumber(L, 1)
            if dwMapIndex != 0:
                pDungeon = CDungeonManager.instance().FindByMapIndex(int(dwMapIndex))
                if pDungeon:
                    quest.CQuestManager.instance().SelectDungeon(pDungeon)
                    lua_pushboolean(L, 1)
                else:
                    quest.CQuestManager.instance().SelectDungeon(None)
                    lua_pushboolean(L, 0)
            else:
                quest.CQuestManager.instance().SelectDungeon(None)
                lua_pushboolean(L, 0)
            return 1

        int quest.dungeon_find(lua_State* L)
            dwMapIndex = lua_tonumber(L, 1)
            if dwMapIndex != 0:
                pDungeon = CDungeonManager.instance().FindByMapIndex(int(dwMapIndex))
                if pDungeon:
                    lua_pushboolean(L, 1)
                else:
                    lua_pushboolean(L, 0)
            else:
                lua_pushboolean(L, 0)
            return 1

        int quest.dungeon_all_near_to(lua_State* L)
            pDungeon = quest.CQuestManager.instance().GetCurrentDungeon()

            if pDungeon is not None:
                lua_pushboolean(L, pDungeon.IsAllPCNearTo(int(lua_tonumber(L, 1)), int(lua_tonumber(L, 2)), 30))
            else:
                lua_pushboolean(L, LGEMiscellaneous.DEFINECONSTANTS.false)

            return 1

        int quest.dungeon_set_warp_location(lua_State* L)
            pDungeon = quest.CQuestManager.instance().GetCurrentDungeon()

            if pDungeon is None:
                return 0

            if lua_gettop(L)<3 or (not lua_isnumber(L, 1)) or (not lua_isnumber(L,2)) or not lua_isnumber(L, 3):
                return 0

            f = FSetWarpLocation(int(lua_tonumber(L, 1)), int(lua_tonumber(L, 2)), int(lua_tonumber(L, 3)))
            pDungeon.ForEachMember(f.functor_method)

            return 0

        int quest.dungeon_set_item_group(lua_State* L)
            if (not lua_isstring(L, 1)) or not lua_isnumber(L, 2):
                return 0
            group_name = lua_tostring(L, 1)
            size = lua_tonumber(L, 2)

            item_group = []

            for LaniatusDefVariables in range(0, size):
                if (not lua_isnumber(L, LaniatusDefVariables * 2 + 3)) or not lua_isnumber(L, LaniatusDefVariables * 2 + 4):
                    return 0
                item_group.append(std::pair  (lua_tonumber(L, LaniatusDefVariables * 2 + 3), lua_tonumber(L, LaniatusDefVariables * 2 + 4)))
            pDungeon = quest.CQuestManager.instance().GetCurrentDungeon()

            if pDungeon is None:
                return 0

            pDungeon.CreateItemGroup(group_name, item_group)
            return 0

        int quest.dungeon_set_quest_flag2(lua_State* L)
            q = quest.CQuestManager.instance()

            f = FSetQuestFlag()

            if (not lua_isstring(L, 1)) or (not lua_isstring(L, 2)) or not lua_isnumber(L, 3):
                #lani_err("Invalid Argument")

            f.flagname = str(lua_tostring(L, 1)) + "." + lua_tostring(L, 2)
            f.value = int(rint(lua_tonumber(L, 3)))

            pDungeon = q.GetCurrentDungeon()

            if pDungeon:
                pDungeon.ForEachMember(f.functor_method)

            return 0

        void RegisterDungeonFunctionTable()
            dungeon_functions = [luaL_reg("join", dungeon_join), luaL_reg("exit", dungeon_exit), luaL_reg("exit_all", dungeon_exit_all), luaL_reg("set_item_group", dungeon_set_item_group), luaL_reg("exit_all_by_item_group", dungeon_exit_all_by_item_group), luaL_reg("say_diff_by_item_group", dungeon_say_diff_by_item_group), luaL_reg("delete_item_in_item_group_from_all", dungeon_delete_item_in_item_group_from_all), luaL_reg("purge", dungeon_purge), luaL_reg("kill_all", dungeon_kill_all), luaL_reg("spawn", dungeon_spawn), luaL_reg("spawn_mob", dungeon_spawn_mob), luaL_reg("spawn_mob_dir", dungeon_spawn_mob_dir), luaL_reg("spawn_mob_ac_dir", dungeon_spawn_mob_ac_dir), luaL_reg("spawn_name_mob", dungeon_spawn_name_mob), luaL_reg("spawn_goto_mob", dungeon_spawn_goto_mob), luaL_reg("spawn_group", dungeon_spawn_group), luaL_reg("spawn_unique", dungeon_spawn_unique), luaL_reg("spawn_move_unique", dungeon_spawn_move_unique), luaL_reg("spawn_move_group", dungeon_spawn_move_group), luaL_reg("spawn_stone_door", dungeon_spawn_stone_door), luaL_reg("spawn_wooden_door", dungeon_spawn_wooden_door), luaL_reg("purge_unique", dungeon_purge_unique), luaL_reg("purge_area", dungeon_purge_area), luaL_reg("kill_unique", dungeon_kill_unique), luaL_reg("is_unique_dead", dungeon_is_unique_dead), luaL_reg("unique_get_hp_perc", dungeon_unique_get_hp_perc), luaL_reg("unique_set_def_grade", dungeon_unique_set_def_grade), luaL_reg("unique_set_hp", dungeon_unique_set_hp), luaL_reg("unique_set_maxhp", dungeon_unique_set_maxhp), luaL_reg("get_unique_vid", dungeon_get_unique_vid), luaL_reg("get_kill_stone_count", dungeon_get_kill_stone_count), luaL_reg("get_kill_mob_count", dungeon_get_kill_mob_count), luaL_reg("is_use_potion", dungeon_is_use_potion), luaL_reg("revived", dungeon_revived), luaL_reg("set_dest", dungeon_set_dest), luaL_reg("jump_all", dungeon_jump_all), luaL_reg("warp_all", dungeon_warp_all), luaL_reg("new_jump_all", dungeon_new_jump_all), luaL_reg("new_jump_party", dungeon_new_jump_party), luaL_reg("new_jump", dungeon_new_jump), luaL_reg("regen_file", dungeon_regen_file), luaL_reg("set_regen_file", dungeon_set_regen_file), luaL_reg("clear_regen", dungeon_clear_regen), luaL_reg("set_exit_all_at_eliminate", dungeon_set_exit_all_at_eliminate), luaL_reg("set_warp_at_eliminate", dungeon_set_warp_at_eliminate), luaL_reg("get_map_index", dungeon_get_map_index), luaL_reg("check_eliminated", dungeon_check_eliminated), luaL_reg("exit_all_to_start_position", dungeon_exit_all_to_start_position), luaL_reg("count_monster", dungeon_count_monster), luaL_reg("setf", dungeon_set_flag), luaL_reg("getf", dungeon_get_flag), luaL_reg("getf_from_map_index", dungeon_get_flag_from_map_index), luaL_reg("set_unique", dungeon_set_unique), luaL_reg("select", dungeon_select), luaL_reg("find", dungeon_find), luaL_reg("notice", dungeon_notice), luaL_reg("setqf", dungeon_set_quest_flag), luaL_reg("all_near_to", dungeon_all_near_to), luaL_reg("set_warp_location", dungeon_set_warp_location), luaL_reg("setqf2", dungeon_set_quest_flag2), luaL_reg(None, None)]

            quest.CQuestManager.instance().AddLuaFunctionTable("d", dungeon_functions)
