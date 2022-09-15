## Laniatus Games Studio Inc. | NOTE: Python has no need of forward class declarations:
#class CParty

class CDungeon:


    def close(self):
        if self._m_pParty is not None:
            self._m_pParty.SetDungeon_for_Only_party(None)
        self.ClearRegen()
        event_cancel(self._deadEvent)
        event_cancel(self._exit_all_event_)
        event_cancel(self._jump_to_event_)

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: uint32_t GetId() const
    def GetId(self):
        return uint32_t(self._m_id)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if __MULTI_LANGUAGE_SYSTEM__
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if __MULTI_LANGUAGE_SYSTEM__
    def Notice(self, msg, *LegacyParamArray):
##else
    def Notice(self, msg):
##endif
        #sys_log(0, "XXX Dungeon Notice %p %s", self, msg)
        pMap = SECTREE_MANAGER.instance().GetMap(int(self._m_lMapIndex))

        if pMap is None:
            #lani_err("cannot find map by index %d", self._m_lMapIndex)
            return

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if __MULTI_LANGUAGE_SYSTEM__
        c_ref_set = DESC_MANAGER.instance().GetClientSet()

        if (not msg) != '\0':
            return

        it = c_ref_set.begin()

        while it is not c_ref_set.end():
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: DESC* d = *(it++);
            d = *(it)
            it += 1

            if d.GetCharacter():
                pSecMap = SECTREE_MANAGER.instance().GetMap(d.GetCharacter().GetMapIndex())
                if pSecMap is not pMap:
                    continue

                strMsg = msg
                c_pszBuf = None

                if (not len(strMsg)) == 0 and std::all_of(strMsg.begin(), strMsg.end(), isdigit):
                    dwKey = uint(int(msg))
                    bLanguage = (d.GetLanguage() if d is not None else LaniatusLocalization.LOCALE_LANIATUS)

                    c_pszBuf = LC_LOCALE_QUEST_TEXT(dwKey, bLanguage)
                else:
                    c_pszBuf = msg

                strBuffFilter = c_pszBuf
                strReplace = "%d"

                pos = 0
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: while ((pos = strBuffFilter.find(strReplace)) != -1)
                while (pos = strBuffFilter.find(strReplace)) != -1:
                    strBuffFilter = (strBuffFilter[0:pos] + "%s" + strBuffFilter[pos + len(strReplace):])

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to pointers to value types:
#ORIGINAL METINII C CODE: const char* c_pszConvBuf = strBuffFilter.c_str();
                c_pszConvBuf = strBuffFilter
                szNoticeBuf = str(['\0' for _ in range((int)LGEMiscellaneous.CHAT_MAX_LEN + 1)])

                args = None
                va_start(args, msg)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                len = vsnprintf(szNoticeBuf, sizeof(szNoticeBuf), c_pszConvBuf, args)
                va_end(args)

                c_pszToken = None
                c_pszLast = szNoticeBuf

                strBuff = szNoticeBuf
                strDelim = "[ENTER]"
                strToken = ""

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: while ((pos = strBuff.find(strDelim)) != -1)
                while (pos = strBuff.find(strDelim)) != -1:
                    strToken = strBuff[0:pos]
                    c_pszToken = strToken
                    d.GetCharacter().ChatPacket(EChatType.CHAT_TYPE_NOTICE, "%s", c_pszToken)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no equivalent to the standard string 'erase' method in Python if it's used as an rvalue:
                    c_pszLast = strBuff.erase(0, pos + len(strDelim)).c_str()
                d.GetCharacter().ChatPacket(EChatType.CHAT_TYPE_NOTICE, "%s", c_pszLast)
##else
        f = FNotice(msg)
        pMap.for_each(f.functor_method)
##endif

##else
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    Notice(msg)
##endif
    def JoinParty(self, pParty):
        pParty.SetDungeon(self)
        self._m_map_pkParty.insert((pParty,0))

        if SECTREE_MANAGER.instance().GetMap(int(self._m_lMapIndex)) is None:
            #lani_err("CDungeon: SECTREE_MAP not found for #%ld", self._m_lMapIndex)
            return
        f = FWarpToDungeon(int(self._m_lMapIndex), self)
        pParty.ForEachOnlineMember(f.functor_method)

    def QuitParty(self, pParty):
        pParty.SetDungeon(None)
        it = self._m_map_pkParty.find(pParty)

        if it != self._m_map_pkParty.end():
            self._m_map_pkParty.erase(it)

    def Join(self, ch):
        if SECTREE_MANAGER.instance().GetMap(int(self._m_lMapIndex)) is None:
            #lani_err("CDungeon: SECTREE_MAP not found for #%ld", self._m_lMapIndex)
            return
        FWarpToDungeon(self._m_lMapIndex, self)(ch)

    def IncMember(self, ch):
        if self._m_set_pkCharacter.find(ch) == self._m_set_pkCharacter.end():
            self._m_set_pkCharacter.insert(ch)

        event_cancel(self._deadEvent)

    def DecMember(self, ch):
        it = self._m_set_pkCharacter.find(ch)

        if it == self._m_set_pkCharacter.end():
            return

        self._m_set_pkCharacter.erase(it)

        if self._m_set_pkCharacter.empty():
            info = Globals.AllocEventInfo()
            info.dungeon_id = self._m_id

            event_cancel(self._deadEvent)
            self._deadEvent = event_create_ex(dungeon_dead_event, info, ((10) * passes_per_sec))

    def Purge(self):
        pkMap = SECTREE_MANAGER.instance().GetMap(int(self._m_lMapIndex))
        if pkMap is None:
            #lani_err("CDungeon: SECTREE_MAP not found for #%ld", self._m_lMapIndex)
            return
        f = FPurgeSectree()
        pkMap.for_each(f.functor_method)

    def KillAll(self):
        pkMap = SECTREE_MANAGER.instance().GetMap(int(self._m_lMapIndex))
        if pkMap is None:
            #lani_err("CDungeon: SECTREE_MAP not found for #%ld", self._m_lMapIndex)
            return
        f = FKillSectree()
        pkMap.for_each(f.functor_method)

    def IncMonster(self):
        self._m_iMonsterCount += 1
        #sys_log(0, "MonsterCount %d", self._m_iMonsterCount)
    def DecMonster(self):
        self._m_iMonsterCount -= 1
        self.CheckEliminated()
    def CountMonster(self):
        return self._m_iMonsterCount
    def CountRealMonster(self):
        pMap = SECTREE_MANAGER.instance().GetMap(int(self._m_lOrigMapIndex))

        if pMap is None:
            #lani_err("cannot find map by index %d", self._m_lOrigMapIndex)
            return 0

        f = FCountMonster()
        pMap.for_each(f.functor_method)
        return f.n

    def IncPartyMember(self, pParty, ch):
        it = self._m_map_pkParty.find(pParty)

        if it != self._m_map_pkParty.end():
            it.second += 1
        else:
            self._m_map_pkParty.insert((pParty,1))

        self.IncMember(ch)

    def DecPartyMember(self, pParty, ch):
        it = self._m_map_pkParty.find(pParty)

        if it == self._m_map_pkParty.end():
            #lani_err("cannot find party")
        else:
            it.second -= 1

            if it.second == 0:
                self.QuitParty(pParty)

        self.DecMember(ch)

    def IncKillCount(self, pkKiller, pkVictim):
        if pkVictim.IsStone():
            self._m_iStoneKill += 1
        else:
            self._m_iMobKill += 1

    def GetKillMobCount(self):
        return self._m_iMobKill

    def GetKillStoneCount(self):
        return self._m_iStoneKill

    def IsUsePotion(self):
        return self._m_bUsePotion

    def IsUseRevive(self):
        return self._m_bUseRevive

    def UsePotion(self, ch):
        self._m_bUsePotion = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def UseRevive(self, ch):
        self._m_bUseRevive = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def GetMapIndex(self):
        return int(self._m_lMapIndex)
    def Spawn(self, vnum, pos):
        it = self._m_map_Area.find(pos)

        if it is self._m_map_Area.end():
            #lani_err("Wrong position string : %s", pos)
            return

        ai = it.second
        dir = ai.dir
        if dir == -1:
            dir = number(0,359)

        pkSectreeMap = SECTREE_MANAGER.instance().GetMap(int(self._m_lMapIndex))
        if pkSectreeMap is None:
            #lani_err("cannot find map by index %d", self._m_lMapIndex)
            return
        dx = number(ai.sx, ai.ex)
        dy = number(ai.sy, ai.ey)

        ch = CHARACTER_MANAGER.instance().SpawnMob(vnum, int(self._m_lMapIndex), pkSectreeMap.m_setting.iBaseX+dx, pkSectreeMap.m_setting.iBaseY+dy, 0, LGEMiscellaneous.DEFINECONSTANTS.false, dir, ((not DefineConstants.false)))
        if ch:
            ch.SetDungeon(self)

    def SpawnMob(self, vnum, x, y, dir = 0):
        pkSectreeMap = SECTREE_MANAGER.instance().GetMap(int(self._m_lMapIndex))
        if pkSectreeMap is None:
            #lani_err("CDungeon: SECTREE_MAP not found for #%ld", self._m_lMapIndex)
            return None
        #sys_log(0, "CDungeon::SpawnMob %u %d %d", vnum, x, y)

        ch = CHARACTER_MANAGER.instance().SpawnMob(vnum, int(self._m_lMapIndex), pkSectreeMap.m_setting.iBaseX+x *100, pkSectreeMap.m_setting.iBaseY+y *100, 0, LGEMiscellaneous.DEFINECONSTANTS.false,-1 if dir == 0 else (dir - 1) * 45, ((not DefineConstants.false)))

        if ch:
            ch.SetDungeon(self)
            #sys_log(0, "CDungeon::SpawnMob name %s", ch.GetName(LOCALE_LANIATUS))

        return ch

    def SpawnMob_ac_dir(self, vnum, x, y, dir = 0):
        pkSectreeMap = SECTREE_MANAGER.instance().GetMap(int(self._m_lMapIndex))
        if pkSectreeMap is None:
            #lani_err("CDungeon: SECTREE_MAP not found for #%ld", self._m_lMapIndex)
            return None
        #sys_log(0, "CDungeon::SpawnMob %u %d %d", vnum, x, y)

        ch = CHARACTER_MANAGER.instance().SpawnMob(vnum, int(self._m_lMapIndex), pkSectreeMap.m_setting.iBaseX+x *100, pkSectreeMap.m_setting.iBaseY+y *100, 0, LGEMiscellaneous.DEFINECONSTANTS.false, dir, ((not DefineConstants.false)))

        if ch:
            ch.SetDungeon(self)
            #sys_log(0, "CDungeon::SpawnMob name %s", ch.GetName(LOCALE_LANIATUS))

        return ch

    def SpawnGroup(self, vnum, x, y, radius, bAggressive = LGEMiscellaneous.DefineConstants.false, count = 1):
        pkSectreeMap = SECTREE_MANAGER.instance().GetMap(int(self._m_lMapIndex))
        if pkSectreeMap is None:
            #lani_err("CDungeon: SECTREE_MAP not found for #%ld", self._m_lMapIndex)
            return None

        iRadius = int(radius)

        sx = pkSectreeMap.m_setting.iBaseX + x - iRadius
        sy = pkSectreeMap.m_setting.iBaseY + y - iRadius
        ex = sx + iRadius
        ey = sy + iRadius

        ch = None

## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: while (count--)
        while (count) != 0:
            count -= 1
            chLeader = CHARACTER_MANAGER.instance().SpawnGroup(vnum, int(self._m_lMapIndex), sx, sy, ex, ey, None, bAggressive, self)
            if chLeader is not None and ch is None:
                ch = chLeader
        count -= 1

        return ch

    def SpawnNameMob(self, vnum, x, y, name):
        pkSectreeMap = SECTREE_MANAGER.instance().GetMap(int(self._m_lMapIndex))
        if pkSectreeMap is None:
            #lani_err("CDungeon: SECTREE_MAP not found for #%ld", self._m_lMapIndex)
            return

        ch = CHARACTER_MANAGER.instance().SpawnMob(vnum, int(self._m_lMapIndex), pkSectreeMap.m_setting.iBaseX+x, pkSectreeMap.m_setting.iBaseY+y, 0, LGEMiscellaneous.DEFINECONSTANTS.false, -1, ((not DefineConstants.false)))
        if ch:
            ch.SetName(name)
            ch.SetDungeon(self)

    def SpawnGotoMob(self, lFromX, lFromY, lToX, lToY):
        MOB_GOTO_VNUM = 20039

        pkSectreeMap = SECTREE_MANAGER.instance().GetMap(int(self._m_lMapIndex))
        if pkSectreeMap is None:
            #lani_err("CDungeon: SECTREE_MAP not found for #%ld", self._m_lMapIndex)
            return

        #sys_log(0, "SpawnGotoMob %d %d to %d %d", lFromX, lFromY, lToX, lToY)

        lFromX = pkSectreeMap.m_setting.iBaseX+lFromX *100
        lFromY = pkSectreeMap.m_setting.iBaseY+lFromY *100

        ch = CHARACTER_MANAGER.instance().SpawnMob(uint(MOB_GOTO_VNUM), int(self._m_lMapIndex), lFromX, lFromY, 0, LGEMiscellaneous.DEFINECONSTANTS.false, -1, ((not DefineConstants.false)))

        if ch:
            buf = str(['\0' for _ in range(30+1)])
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            snprintf(buf, sizeof(buf), ". %ld %ld", lToX, lToY)

            ch.SetName(buf)
            ch.SetDungeon(self)

    def SpawnRegen(self, filename, bOnce = (!LGEMiscellaneous.DefineConstants.false)):
        if (not filename) != '\0':
            #lani_err("CDungeon::SpawnRegen(filename=NULL, bOnce=%d) - m_lMapIndex[%d]", bOnce, self._m_lMapIndex)
            return

        pkSectreeMap = SECTREE_MANAGER.instance().GetMap(int(self._m_lMapIndex))
        if pkSectreeMap is None:
            #lani_err("CDungeon::SpawnRegen(filename=%s, bOnce=%d) - m_lMapIndex[%d]", filename, bOnce, self._m_lMapIndex)
            return
        regen_do(filename, self._m_lMapIndex, pkSectreeMap.m_setting.iBaseX, pkSectreeMap.m_setting.iBaseY, self, bOnce)

    def AddRegen(self, regen):
## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: regen->id = regen_id_++;
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
        regen.id.copy_from(self._regen_id_)
        self._regen_id_ += 1
        self._m_regen.append(regen)

    def ClearRegen(self):
        for it in self._m_regen:
            regen = *it

            event_cancel(regen.event)
            LG_DEL_MEM(regen)
        self._m_regen.clear()

# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    IsValidRegen(regen, regen_id)
    def SetUnique(self, key, vid):
        ch = CHARACTER_MANAGER.instance().Find(vid)
        if ch:
            self._m_map_UniqueMob.update({str(key): ch})
            ch.AddAffect(LaniatusEAffectTypes.LANIA_AFFECT_DUNGEON_UNIQUE, EPointTypes.LG_POINT_NONE, 0, EAffectBits.AFF_DUNGEON_UNIQUE, 65535, 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), DefineConstants.false)

    def SpawnMoveUnique(self, key, vnum, pos_from, pos_to):
        it_to = self._m_map_Area.find(pos_to)
        if it_to is self._m_map_Area.end():
            #lani_err("Wrong position string : %s", pos_to)
            return

        it_from = self._m_map_Area.find(pos_from)
        if it_from is self._m_map_Area.end():
            #lani_err("Wrong position string : %s", pos_from)
            return

        ai = it_from.second
        ai_to = it_to.second
        dir = ai.dir
        if dir == -1:
            dir = number(0,359)

        pkSectreeMap = SECTREE_MANAGER.instance().GetMap(int(self._m_lMapIndex))
        if pkSectreeMap is None:
            #lani_err("CDungeon: SECTREE_MAP not found for #%ld", self._m_lMapIndex)
            return
        for i in range(0, 100):
            dx = number(ai.sx, ai.ex)
            dy = number(ai.sy, ai.ey)
            tx = number(ai_to.sx, ai_to.ex)
            ty = number(ai_to.sy, ai_to.ey)

            ch = CHARACTER_MANAGER.instance().SpawnMob(vnum, int(self._m_lMapIndex), pkSectreeMap.m_setting.iBaseX+dx, pkSectreeMap.m_setting.iBaseY+dy, 0, LGEMiscellaneous.DEFINECONSTANTS.false, dir, ((not DefineConstants.false)))

            if ch:
                self._m_map_UniqueMob.update({str(key): ch})
                ch.AddAffect(LaniatusEAffectTypes.LANIA_AFFECT_DUNGEON_UNIQUE, EPointTypes.LG_POINT_NONE, 0, EAffectBits.AFF_DUNGEON_UNIQUE, 65535, 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), DefineConstants.false)
                ch.SetDungeon(self)

                if ch.Goto(pkSectreeMap.m_setting.iBaseX+tx, pkSectreeMap.m_setting.iBaseY+ty):
                    ch.SendMovePacket(EMoveFuncType.FUNC_WAIT, 0, 0, 0, 0, 0, -1)
            else:
                #lani_err("Cannot spawn at %d %d", pkSectreeMap.m_setting.iBaseX+((ai.sx+ai.ex)>>1), pkSectreeMap.m_setting.iBaseY+((ai.sy+ai.ey)>>1))


    def SpawnMoveGroup(self, vnum, pos_from, pos_to, count = 1):
        it_to = self._m_map_Area.find(pos_to)

        if it_to is self._m_map_Area.end():
            #lani_err("Wrong position string : %s", pos_to)
            return

        it_from = self._m_map_Area.find(pos_from)

        if it_from is self._m_map_Area.end():
            #lani_err("Wrong position string : %s", pos_from)
            return

        ai = it_from.second
        ai_to = it_to.second
        dir = ai.dir

        if dir == -1:
            dir = number(0,359)

        pkSectreeMap = SECTREE_MANAGER.instance().GetMap(int(self._m_lMapIndex))
        if pkSectreeMap is None:
            #lani_err("CDungeon: SECTREE_MAP not found for #%ld", self._m_lMapIndex)
            return

## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: while (count--)
        while (count) != 0:
            count -= 1
            tx = number(ai_to.sx, ai_to.ex)+pkSectreeMap.m_setting.iBaseX
            ty = number(ai_to.sy, ai_to.ey)+pkSectreeMap.m_setting.iBaseY
            CHARACTER_MANAGER.instance().SpawnMoveGroup(vnum, int(self._m_lMapIndex), pkSectreeMap.m_setting.iBaseX+ai.sx, pkSectreeMap.m_setting.iBaseY+ai.sy, pkSectreeMap.m_setting.iBaseX+ai.ex, pkSectreeMap.m_setting.iBaseY+ai.ey, tx, ty, None, ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
        count -= 1

    def SpawnUnique(self, key, vnum, pos):
        it = self._m_map_Area.find(pos)
        if it is self._m_map_Area.end():
            #lani_err("Wrong position string : %s", pos)
            return

        ai = it.second
        dir = ai.dir
        if dir == -1:
            dir = number(0,359)

        pkSectreeMap = SECTREE_MANAGER.instance().GetMap(int(self._m_lMapIndex))
        if pkSectreeMap is None:
            #lani_err("CDungeon: SECTREE_MAP not found for #%ld", self._m_lMapIndex)
            return
        for i in range(0, 100):
            dx = number(ai.sx, ai.ex)
            dy = number(ai.sy, ai.ey)

            ch = CHARACTER_MANAGER.instance().SpawnMob(vnum, int(self._m_lMapIndex), pkSectreeMap.m_setting.iBaseX+dx, pkSectreeMap.m_setting.iBaseY+dy, 0, LGEMiscellaneous.DEFINECONSTANTS.false, dir, ((not DefineConstants.false)))

            if ch:
                self._m_map_UniqueMob.update({str(key): ch})
                ch.SetDungeon(self)
                ch.AddAffect(LaniatusEAffectTypes.LANIA_AFFECT_DUNGEON_UNIQUE, EPointTypes.LG_POINT_NONE, 0, EAffectBits.AFF_DUNGEON_UNIQUE, 65535, 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), DefineConstants.false)
                break
            else:
                #lani_err("Cannot spawn at %d %d", pkSectreeMap.m_setting.iBaseX+((ai.sx+ai.ex)>>1), pkSectreeMap.m_setting.iBaseY+((ai.sy+ai.ey)>>1))

    def SpawnStoneDoor(self, key, pos):
        self.SpawnUnique(key, 13001, pos)

    def SpawnWoodenDoor(self, key, pos):
        self.SpawnUnique(key, 13000, pos)
        self.UniqueSetMaxHP(key, 10000)
        self.UniqueSetHP(key, 10000)
        self.UniqueSetDefGrade(key, 300)

    def KillUnique(self, key):
        it = self._m_map_UniqueMob.find(key)
        if it is self._m_map_UniqueMob.end():
            return
        ch = it.second
        self._m_map_UniqueMob.pop(it)
        ch.Dead(NULL, DefineConstants.false)

    def PurgeUnique(self, key):
        it = self._m_map_UniqueMob.find(key)
        if it is self._m_map_UniqueMob.end():
            #lani_err("Unknown Key or Dead: %s", key)
            return
        ch = it.second
        self._m_map_UniqueMob.pop(it)
        CHARACTER_MANAGER.instance().DestroyCharacter(ch)

    def IsUniqueDead(self, key):
        it = self._m_map_UniqueMob.find(key)

        if it is self._m_map_UniqueMob.end():
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        return it.second.IsDead()

    def GetUniqueHpPerc(self, key):
        it = self._m_map_UniqueMob.find(key)
        if it is self._m_map_UniqueMob.end():
            return 0.0
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        return (100.0 *it.second.GetHP())/it.second.GetMaxHP()

    def GetUniqueVid(self, key):
        it = self._m_map_UniqueMob.find(key)
        if it is self._m_map_UniqueMob.end():
            return 0
        ch = it.second
        return ch.GetVID()

    def DeadCharacter(self, ch):
        if not ch.IsPC():
            it = self._m_map_UniqueMob.begin()
            while it is not self._m_map_UniqueMob.end():
                if it.second is ch:
                    self._m_map_UniqueMob.pop(it)
                    break
                it += 1

    def UniqueSetMaxHP(self, key, iMaxHP):
        it = self._m_map_UniqueMob.find(key)
        if it is self._m_map_UniqueMob.end():
            #lani_err("Unknown Key : %s", key)
            return
        it.second.SetMaxHP(iMaxHP)

    def UniqueSetHP(self, key, iHP):
        it = self._m_map_UniqueMob.find(key)
        if it is self._m_map_UniqueMob.end():
            #lani_err("Unknown Key : %s", key)
            return
        it.second.SetHP(iHP)

    def UniqueSetDefGrade(self, key, iGrade):
        it = self._m_map_UniqueMob.find(key)
        if it is self._m_map_UniqueMob.end():
            #lani_err("Unknown Key : %s", key)
            return
        it.second.PointChange(EPointTypes.LG_POINT_DEF_GRADE,iGrade - it.second.GetPoint(EPointTypes.LG_POINT_DEF_GRADE))

    def SendDestPositionToParty(self, pParty, x, y):
        if self._m_map_pkParty.find(pParty) == self._m_map_pkParty.end():
            #lani_err("PARTY %u not in DUNGEON %d", pParty.GetLeaderPID(), self._m_lMapIndex)
            return

        f = FSendDestPosition(x, y)
        pParty.ForEachNearMember(f.functor_method)

    def CheckEliminated(self):
        if self._m_iMonsterCount > 0:
            return

        if self._m_bExitAllAtEliminate:
            #sys_log(0, "CheckEliminated: exit")
            self._m_bExitAllAtEliminate = LGEMiscellaneous.DEFINECONSTANTS.false

            if self._m_iWarpDelay != 0:
                info = Globals.AllocEventInfo()
                info.dungeon_id = self._m_id

                event_cancel(self._exit_all_event_)
                self._exit_all_event_ = event_create_ex(dungeon_exit_all_event, info, ((self._m_iWarpDelay) * passes_per_sec))
            else:
                self.ExitAll()
        elif self._m_bWarpAtEliminate:
            #sys_log(0, "CheckEliminated: warp")
            self._m_bWarpAtEliminate = LGEMiscellaneous.DEFINECONSTANTS.false

            if self._m_iWarpDelay != 0:
                info = Globals.AllocEventInfo()
                info.dungeon_id = self._m_id

                event_cancel(self._jump_to_event_)
                self._jump_to_event_ = event_create_ex(dungeon_jump_to_event, info, ((self._m_iWarpDelay) * passes_per_sec))
            else:
                self.JumpToEliminateLocation()
        else:
            #sys_log(0, "CheckEliminated: none")

    def JumpAll(self, lFromMapIndex, x, y):
        x *= 100
        y *= 100

        pMap = SECTREE_MANAGER.instance().GetMap(lFromMapIndex)

        if pMap is None:
            #lani_err("cannot find map by index %d", lFromMapIndex)
            return

        f = FWarpToPosition(int(self._m_lMapIndex), x, y)
        pMap.for_each(f.functor_method)

    def WarpAll(self, lFromMapIndex, x, y):
        x *= 100
        y *= 100

        pMap = SECTREE_MANAGER.instance().GetMap(lFromMapIndex)

        if pMap is None:
            #lani_err("cannot find map by index %d", lFromMapIndex)
            return

        f = FWarpToPositionForce(int(self._m_lMapIndex), x, y)
        pMap.for_each(f.functor_method)

    def JumpParty(self, pParty, lFromMapIndex, x, y):
        x *= 100
        y *= 100

        pMap = SECTREE_MANAGER.instance().GetMap(lFromMapIndex)

        if pMap is None:
            #lani_err("cannot find map by index %d", lFromMapIndex)
            return

        if pParty.GetDungeon_for_Only_party() is None:
            if self._m_pParty is None:
                self._m_pParty = pParty
            elif self._m_pParty is not pParty:
                #lani_err("Dungeon already has party. Another party cannot jump in dungeon : index %d", self.GetMapIndex())
                return
            pParty.SetDungeon_for_Only_party(self)

        f = FWarpToPosition(int(self._m_lMapIndex), x, y)

        pParty.ForEachOnMapMember(f.functor_method, lFromMapIndex)

    def ExitAll(self):
        pMap = SECTREE_MANAGER.instance().GetMap(int(self._m_lMapIndex))

        if pMap is None:
            #lani_err("cannot find map by index %d", self._m_lMapIndex)
            return

        f = FExitDungeon()
        pMap.for_each(f.functor_method)

    def ExitAllToStartPosition(self):
        pMap = SECTREE_MANAGER.instance().GetMap(int(self._m_lMapIndex))

        if pMap is None:
            #lani_err("cannot find map by index %d", self._m_lMapIndex)
            return

        f = FExitDungeonToStartPosition()
        pMap.for_each(f.functor_method)

    def JumpToEliminateLocation(self):
        pDungeon = CDungeonManager.instance().FindByMapIndex(self._m_lWarpMapIndex)

        if pDungeon:
            pDungeon.JumpAll(int(self._m_lMapIndex), self._m_lWarpX, self._m_lWarpY)

            if (not len(self._m_stRegenFile)) == 0:
                pDungeon.SpawnRegen(self._m_stRegenFile, ((not DefineConstants.false)))
                self._m_stRegenFile = ""
        else:
            pMap = SECTREE_MANAGER.instance().GetMap(int(self._m_lMapIndex))

            if pMap is None:
                #lani_err("no map by index %d", self._m_lMapIndex)
                return

            f = FWarpToPosition(self._m_lWarpMapIndex, self._m_lWarpX * 100, self._m_lWarpY * 100)
            pMap.for_each(f.functor_method)

    def SetExitAllAtEliminate(self, time):
        #sys_log(0, "SetExitAllAtEliminate: time %d", time)
        self._m_bExitAllAtEliminate = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
        self._m_iWarpDelay = time

    def SetWarpAtEliminate(self, time, lMapIndex, x, y, regen_file):
        self._m_bWarpAtEliminate = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
        self._m_iWarpDelay = time
        self._m_lWarpMapIndex = lMapIndex
        self._m_lWarpX = x
        self._m_lWarpY = y

        if (not regen_file) != '\0' or (not regen_file[0]) != '\0':
            self._m_stRegenFile = ""
        else:
            self._m_stRegenFile = regen_file

        #sys_log(0, "SetWarpAtEliminate: time %d map %d %dx%d regenfile %s", time, lMapIndex, x, y, self._m_stRegenFile)

    def GetFlag(self, name):
        it = self._m_map_Flag.find(name)
        if it is not self._m_map_Flag.end():
            return it.second
        else:
            return 0

    def SetFlag(self, name, value):
        it = self._m_map_Flag.find(name)
        if it is not self._m_map_Flag.end():
            it.second = value
        else:
            self._m_map_Flag.update({name: value})

# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    CreateItemGroup(group_name, item_group)
    def GetItemGroup(self, group_name):
        it = self._m_map_ItemGroup.find(group_name)
        if it is not self._m_map_ItemGroup.end():
            return (it.second)
        else:
            return None

# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    ForEachMember(f)
    def IsAllPCNearTo(self, x, y, dist):
        pMap = SECTREE_MANAGER.instance().GetMap(int(self._m_lMapIndex))

        if pMap is None:
            #lani_err("cannot find map by index %d", self._m_lMapIndex)
            return LGEMiscellaneous.DEFINECONSTANTS.false

        f = FNearPosition(x, y, dist)
        pMap.for_each(f.functor_method)
        return f.ret

# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    CDungeon(id, lOriginalMapIndex, lMapIndex)
    def Initialize(self):
        self._deadEvent = None
        self._exit_all_event_ = None
        self._jump_to_event_ = None
        self._regen_id_ = 0

        self._m_iMobKill = 0
        self._m_iStoneKill = 0
        self._m_bUsePotion = LGEMiscellaneous.DEFINECONSTANTS.false
        self._m_bUseRevive = LGEMiscellaneous.DEFINECONSTANTS.false

        self._m_iMonsterCount = 0

        self._m_bExitAllAtEliminate = LGEMiscellaneous.DEFINECONSTANTS.false
        self._m_bWarpAtEliminate = LGEMiscellaneous.DEFINECONSTANTS.false

        self._m_iWarpDelay = 0
        self._m_lWarpMapIndex = 0
        self._m_lWarpX = 0
        self._m_lWarpY = 0

        self._m_stRegenFile = ""

        self._m_pParty = None






## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python has no concept of a 'friend' class:
#    friend class CDungeonManager
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python has no concept of a 'friend' function:
#ORIGINAL METINII C CODE: friend int(dungeon_dead_event)(_boost_func_of_void::intrusive_ptr<struct event> event, int processing_time);
    int(dungeon_dead_event)(_boost_func_of_void.intrusive_ptr<struct event> event, int processing_time)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python has no concept of a 'friend' function:
#ORIGINAL METINII C CODE: friend int(dungeon_exit_all_event)(_boost_func_of_void::intrusive_ptr<struct event> event, int processing_time);
    int(dungeon_exit_all_event)(_boost_func_of_void.intrusive_ptr<struct event> event, int processing_time)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python has no concept of a 'friend' function:
#ORIGINAL METINII C CODE: friend int(dungeon_jump_to_event)(_boost_func_of_void::intrusive_ptr<struct event> event, int processing_time);
    int(dungeon_jump_to_event)(_boost_func_of_void.intrusive_ptr<struct event> event, int processing_time)
    def SetPartyNull(self):
        self._m_pParty = None

class CDungeonManager(singleton):

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self._m_map_pkDungeon = {}
        self._m_map_pkMapDungeon = {}
        self._next_id_ = uint32_t()

        self._next_id_ = 0

    def close(self):
        pass

    def Create(self, lOriginalMapIndex):
        lMapIndex = uint(SECTREE_MANAGER.instance().CreatePrivateMap(lOriginalMapIndex))

        if lMapIndex == 0:
            #sys_log(0, "Fail to Create Dungeon : OrginalMapindex %d NewMapindex %d", lOriginalMapIndex, lMapIndex)
            return None

## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: uint id = next_id_++;
        id = self._next_id_
        self._next_id_ += 1
        while self.Find(id) is not None:
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: id = next_id_++;
            id = self._next_id_
            self._next_id_ += 1

        pDungeon = LG_NEW_M2 CDungeon(id, lOriginalMapIndex, int(lMapIndex))
        if pDungeon is None:
            #lani_err("LG_NEW_M2 CDungeon failed")
            return None
        self._m_map_pkDungeon.update({id: pDungeon})
        self._m_map_pkMapDungeon.update({lMapIndex: pDungeon})

        return pDungeon

# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    Destroy(dungeon_id)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    Find(dungeon_id)
    def FindByMapIndex(self, lMapIndex):
        it = self._m_map_pkMapDungeon.find(lMapIndex)
        if it is not self._m_map_pkMapDungeon.end():
            return it.second
        return None


## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if __MULTI_LANGUAGE_SYSTEM__
##endif

def __init__(id, lOriginalMapIndex, lMapIndex):
    self.m_id = id
    self.m_lOrigMapIndex = lOriginalMapIndex
    self.m_lMapIndex = lMapIndex
    self.m_map_Area = SECTREE_MANAGER.instance().GetDungeonArea(lOriginalMapIndex)
    Initialize()

class FSendDestPosition:
    def __init__(self, x, y):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.p1 = packet_dungeon()
        self.p2 = packet_dungeon_dest_position()

        self.p1.bHeader = byte(Globals.LG_HEADER_GC_DUNGEON)
        self.p1.subheader = byte(Globals.DUNGEON_SUBLG_HEADER_GC_DESTINATION_POSITION)
        self.p2.x = x
        self.p2.y = y
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.p1.size = sizeof(self.p1)+sizeof(self.p2)

    def functor_method(self, ch):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        ch.GetDesc().BufferedPacket(self.p1, sizeof(packet_dungeon))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        ch.GetDesc().Packet(self.p2, sizeof(packet_dungeon_dest_position))


class FWarpToDungeon:
    def __init__(self, lMapIndex, d):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.m_lMapIndex = 0
        self.m_x = 0
        self.m_y = 0
        self.m_pkDungeon = None

        self.m_lMapIndex = lMapIndex
        self.m_pkDungeon = d
        pkSectreeMap = SECTREE_MANAGER.instance().GetMap(lMapIndex)
        self.m_x = pkSectreeMap.m_setting.posSpawn.x
        self.m_y = pkSectreeMap.m_setting.posSpawn.y

    def functor_method(self, ch):
        ch.SaveExitLocation()
        ch.WarpSet(self.m_x, self.m_y, self.m_lMapIndex)


class dungeon_id_info(event_info_data):

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.dungeon_id = 0

        self.dungeon_id = 0

class FWarpToPosition:
    def __init__(self, lMapIndex, x, y):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.lMapIndex = 0
        self.x = 0
        self.y = 0

        self.lMapIndex = lMapIndex
        self.x = x
        self.y = y

    def functor_method(self, ent):
        if not ent.IsType(EEntityTypes.ENTITY_CHARACTER):
            return
        ch = ent
        if not ch.IsPC():
            return
        if ch.GetMapIndex() == self.lMapIndex:
            ch.Show(self.lMapIndex, self.x, self.y, 0, DefineConstants.false)
            ch.Stop()
        else:
            ch.WarpSet(self.x, self.y, self.lMapIndex)

class FWarpToPositionForce:
    def __init__(self, lMapIndex, x, y):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.lMapIndex = 0
        self.x = 0
        self.y = 0

        self.lMapIndex = lMapIndex
        self.x = x
        self.y = y

    def functor_method(self, ent):
        if not ent.IsType(EEntityTypes.ENTITY_CHARACTER):
            return
        ch = ent
        if not ch.IsPC():
            return
        ch.WarpSet(self.x, self.y, self.lMapIndex)


def Destroy(dungeon_id):
    #sys_log(0, "DUNGEON destroy : map index %u", dungeon_id)
    pDungeon = Find(dungeon_id)
    if pDungeon is None:
        return
    m_map_pkDungeon.erase(dungeon_id)

    lMapIndex = int(pDungeon.m_lMapIndex)
    m_map_pkMapDungeon.erase(lMapIndex)

    server_timer_arg = uint(lMapIndex)
    quest.CQuestManager.instance().CancelServerTimers(server_timer_arg)

    SECTREE_MANAGER.instance().DestroyPrivateMap(lMapIndex)
    LG_DEL_MEM(pDungeon)

def Find(dungeon_id):
    it = m_map_pkDungeon.find(dungeon_id)
    if it != m_map_pkDungeon.end():
        return it.second
    return None

def IsValidRegen(regen, regen_id):
    it = std::find(m_regen.begin(), m_regen.end(), regen)
    if it is m_regen.end():
        return LGEMiscellaneous.DEFINECONSTANTS.false
    found = *it
    return (found.id == regen_id)

## Laniatus Games Studio Inc. | NOTE: Anonymous namespaces are not defined:
#namespace
class FKillSectree:
    def functor_method(self, ent):
        if ent.IsType(EEntityTypes.ENTITY_CHARACTER):
            ch = ent

            if ch.IsMonster() or ch.IsStone():
                ch.Dead(NULL, DefineConstants.false)

class FPurgeSectree:
    def functor_method(self, ent):
        if ent.IsType(EEntityTypes.ENTITY_CHARACTER):
            ch = ent

            if ch.IsMonster() or ch.IsStone():
                CHARACTER_MANAGER.instance().DestroyCharacter(ch)
        elif ent.IsType(EEntityTypes.ENTITY_ITEM):
            item = ent
            ITEM_MANAGER.instance().DestroyItem(item)
        else:
            #lani_err("unknown entity type %d is in dungeon", ent.GetType())

class FCountMonster:
    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.n = 0

        self.n = 0
    def functor_method(self, ent):
        if ent.IsType(EEntityTypes.ENTITY_CHARACTER):
            ch = ent
            if (not ch.IsPC()) or (not ch.IsNPC()) and not ch.IsDead():
                self.n += 1

class FExitDungeon:
    def functor_method(self, ent):
        if ent.IsType(EEntityTypes.ENTITY_CHARACTER):
            ch = ent

            if ch.IsPC():
                ch.ExitToSavedLocation()

## Laniatus Games Studio Inc. | NOTE: Anonymous namespaces are not defined:
#namespace
class FNotice:
    def __init__(self, psz):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.m_psz = '\0'

        self.m_psz = psz

    def functor_method(self, ent):
        if ent.IsType(EEntityTypes.ENTITY_CHARACTER):
            ch = ent
            if ch.IsPC():
                ch.ChatPacket(EChatType.CHAT_TYPE_NOTICE, "%s", self.m_psz)



class FExitDungeonToStartPosition:
    def functor_method(self, ent):
        if ent.IsType(EEntityTypes.ENTITY_CHARACTER):
            ch = ent

            if ch.IsPC():
                posWarp = pixel_position_s()

                if SECTREE_MANAGER.instance().GetRecallPositionByEmpire(g_start_map[ch.GetEmpire()], ch.GetEmpire(), posWarp):
                    ch.WarpSet(posWarp.x, posWarp.y, 0)
                else:
                    ch.ExitToSavedLocation()

class FNearPosition:

    def __init__(self, x, y, d):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.x = 0
        self.y = 0
        self.dist = 0
        self.ret = False

        self.x = x
        self.y = y
        self.dist = d
        self.ret = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def functor_method(self, ent):
        if self.ret == LGEMiscellaneous.DEFINECONSTANTS.false:
            return

        if ent.IsType(EEntityTypes.ENTITY_CHARACTER):
            ch = ent

            if ch.IsPC():
                if Globals.DISTANCE_APPROX(ch.GetX() - self.x * 100, ch.GetY() - self.y * 100) > self.dist * 100:
                    self.ret = LGEMiscellaneous.DEFINECONSTANTS.false

def CreateItemGroup(group_name, item_group):
    m_map_ItemGroup.insert(ItemGroupMap.value_type(group_name, item_group))
