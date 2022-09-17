import math

## Laniatus Games Studio Inc. | NOTE: Python has no need of forward class declarations:
#class CDungeon
## Laniatus Games Studio Inc. | NOTE: Python has no need of forward class declarations:
#class CHARACTER
## Laniatus Games Studio Inc. | NOTE: Python has no need of forward class declarations:
#class CharacterVectorInteractor

class CHARACTER_MANAGER(singleton):


    ##include <_boost_func_of_void/bind.hpp>

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self._m_iMobItemRate = 0
        self._m_iMobDamageRate = 0
        self._m_iMobGoldAmountRate = 0
        self._m_iMobGoldDropRate = 0
        self._m_iMobExpRate = 0
        self._m_iMobItemRatePremium = 0
        self._m_iMobGoldAmountRatePremium = 0
        self._m_iMobGoldDropRatePremium = 0
        self._m_iMobExpRatePremium = 0
        self._m_iUserDamageRate = 0
        self._m_iUserDamageRatePremium = 0
        self._m_iVIDCount = 0
        self._m_map_pkChrByVID = _boost_func_of_void.unordered_map()
        self._m_map_pkChrByPID = _boost_func_of_void.unordered_map()
        self._m_map_pkPCChr = _boost_func_of_void.unordered_map()
        self._dummy1 = str(['\0' for _ in range(1024)])
        self._m_set_pkChrState = boost.unordered_set()
        self._m_set_pkChrForDelayedSave = boost.unordered_set()
        self._m_pkChrSelectedStone = None
        self._m_map_dwMobKillCount = {}
        self._m_set_dwRegisteredRaceNum = std::set()
        self._m_map_pkChrByRaceNum = {}
        self._m_bUsePendingDestroy = False
        self._m_set_pkChrPendingDestroy = boost.unordered_set()

        self._m_iVIDCount = 0
        self._m_pkChrSelectedStone = None
        self._m_bUsePendingDestroy = LGEMiscellaneous.DEFINECONSTANTS.false
        self.RegisterRaceNum(uint(xmas.MOB_XMAS_FIRWORK_SELLER_VNUM))
        self.RegisterRaceNum(uint(xmas.MOB_SANTA_VNUM))
        self.RegisterRaceNum(uint(xmas.MOB_XMAS_TREE_VNUM))

        self._m_iMobItemRate = 100
        self._m_iMobDamageRate = 100
        self._m_iMobGoldAmountRate = 100
        self._m_iMobGoldDropRate = 100
        self._m_iMobExpRate = 100

        self._m_iMobItemRatePremium = 100
        self._m_iMobGoldAmountRatePremium = 100
        self._m_iMobGoldDropRatePremium = 100
        self._m_iMobExpRatePremium = 100

        self._m_iUserDamageRate = 100
        self._m_iUserDamageRatePremium = 100

    def close(self):
        self.Destroy()

    def Destroy(self):
        it = self._m_map_pkChrByVID.begin()
        while it is not self._m_map_pkChrByVID.end():
            ch = it.second
            CHARACTER_MANAGER.instance().DestroyCharacter(ch)
            it = self._m_map_pkChrByVID.begin()

    def GracefulShutdown(self):
        it = self._m_map_pkPCChr.begin()

        while it is not self._m_map_pkPCChr.end():
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: (it++)->second->Disconnect("GracefulShutdown");
            (it).second.Disconnect("GracefulShutdown")
            it += 1

    def AllocVID(self):
        self._m_iVIDCount += 1
        return uint(self._m_iVIDCount)

    def CreateCharacter(self, name, dwPID = 0):
        dwVID = self.AllocVID()
        ch = LG_NEW_M2 CHARACTER
        ch.Create(name, dwVID,((not LGEMiscellaneous.DEFINECONSTANTS.false)) if dwPID != 0 else LGEMiscellaneous.DEFINECONSTANTS.false)
        self._m_map_pkChrByVID.insert((dwVID, ch))

        if dwPID != 0:
            szName = str(['\0' for _ in range((int)LGEMiscellaneous.CHARACTER_NAME_MAX_LEN + 1)])
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            str_lower(name, szName, sizeof(szName))

            self._m_map_pkPCChr.insert(NAME_MAP.value_type(szName, ch))
            self._m_map_pkChrByPID.insert((dwPID, ch))

        return (ch)

    def DestroyCharacter(self, ch):
        if ch is None:
            return

        it = self._m_map_pkChrByVID.find(ch.GetVID())
        if it == self._m_map_pkChrByVID.end():
            #lani_err("[CHARACTER_MANAGER::DestroyCharacter] <Factor> %d not found", int(ch.GetVID()))
            return

        if ch.IsNPC() and (not ch.IsPet()) and ch.GetRider() is None:
            if ch.GetDungeon():
                ch.GetDungeon().DeadCharacter(ch)

        if self._m_bUsePendingDestroy:
            self._m_set_pkChrPendingDestroy.insert(ch)
            return

        self._m_map_pkChrByVID.erase(it)

        if ((not LGEMiscellaneous.DEFINECONSTANTS.false)) == ch.IsPC():
            szName = str(['\0' for _ in range((int)LGEMiscellaneous.CHARACTER_NAME_MAX_LEN + 1)])

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            str_lower(ch.GetName(LOCALE_LANIATUS), szName, sizeof(szName))

            it = self._m_map_pkPCChr.find(szName)

            if self._m_map_pkPCChr.end() != it:
                self._m_map_pkPCChr.erase(it)

        if 0 != ch.GetPlayerID():
            it = self._m_map_pkChrByPID.find(ch.GetPlayerID())

            if self._m_map_pkChrByPID.end() != it:
                self._m_map_pkChrByPID.erase(it)

        self.UnregisterRaceNumMap(ch)
        self.RemoveFromStateList(ch)
        LG_DEL_MEM(ch)

    def Update(self, iPulse):
        self.BeginPendingDestroy()

            if not self._m_map_pkPCChr.empty():
                v = []
                v.reserve(len(self._m_map_pkPCChr))
                transform(self._m_map_pkPCChr.begin(), self._m_map_pkPCChr.end(), back_inserter(v), _boost_func_of_void.bind(NAME_MAP.value_type.second, _1))

                if 0 == (math.fmod(iPulse, ((5) * passes_per_sec))):
                    f = FuncUpdateAndResetChatCounter()
                    for_each(v.begin(), v.end(), f.functor_method)
                else:
                    for_each(v.begin(), v.end(), std::bind(CHARACTER.UpdateCharacter, std::placeholders._1, iPulse))

            if not self._m_set_pkChrState.empty():
                v = []
                v.reserve(len(self._m_set_pkChrState))
                v.extend(self._m_set_pkChrState)
                for_each(v.begin(), v.end(), std::bind(CHARACTER.UpdateStateMachine, std::placeholders._1, iPulse))

            LaniatusDefVariables = CharacterVectorInteractor()

            temp_ref_i = RefObject(i);
            if CHARACTER_MANAGER.instance().GetCharactersByRaceNum(uint(xmas.MOB_SANTA_VNUM), temp_ref_i):
                LaniatusDefVariables = temp_ref_i.arg_value
                for_each(i.begin(), i.end(), std::bind(CHARACTER.UpdateStateMachine, std::placeholders._1, iPulse))
            else:
                LaniatusDefVariables = temp_ref_i.arg_value

        if 0 == (math.fmod(iPulse, ((3600) * passes_per_sec))):
            self._m_map_dwMobKillCount.clear()

        if test_server and 0 == (math.fmod(iPulse, ((60) * passes_per_sec))):
            #sys_log(0, "CHARACTER COUNT vid %zu pid %zu", self._m_map_pkChrByVID.size(), self._m_map_pkChrByPID.size())

        self.FlushPendingDestroy()

    ## Laniatus Games Studio Inc. | NOTE: This was formerly a static local variable declaration (not allowed in Python):
    ## Laniatus Games Studio Inc. | NOTE: This was formerly a static local variable declaration (not allowed in Python):

    def SpawnMob(self, dwVnum, lMapIndex, x, y, z, bSpawnMotion = LGEMiscellaneous.DefineConstants.false, iRot = -1, bShow = (!LGEMiscellaneous.DefineConstants.false)):
        pkMob = CMobManager.instance().Get(dwVnum)
        if pkMob is None:
            #lani_err("SpawnMob: no mob data for vnum %u", dwVnum)
            return None

        if (not Globals.__IsSpawnableInSafeZone(pkMob.m_table.bType)) or mining.IsVeinOfOre(dwVnum):
            tree = SECTREE_MANAGER.instance().Get(uint(lMapIndex), uint(x), uint(y))

            if tree is None:
                #sys_log(0, "no sectree for spawn at %d %d mobvnum %d mapindex %d", x, y, dwVnum, lMapIndex)
                return None

            dwAttr = tree.GetAttribute(x, y)

            is_set = LGEMiscellaneous.DEFINECONSTANTS.false

            ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'IS_SET' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
            if mining.IsVeinOfOre(dwVnum):
                ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'IS_SET' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
                is_set = IS_SET(dwAttr, Globals.ATTR_BLOCK)
            ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'IS_SET' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
            else:
                ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'IS_SET' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
                is_set = IS_SET(dwAttr, Globals.ATTR_BLOCK | Globals.ATTR_OBJECT)

            if is_set:
                ## Laniatus Games Studio Inc. | NOTE: This static local variable declaration (not allowed in Python) has been moved just prior to the method:
                #                static bool s_isLog=quest::CQuestManager::instance().GetEventFlag("spawn_block_log")
                ## Laniatus Games Studio Inc. | NOTE: This static local variable declaration (not allowed in Python) has been moved just prior to the method:
                #                static uint s_nextTime=get_global_time()+10000

                curTime = get_global_time()

                if curTime> SpawnMob_s_nextTime:
                    SpawnMob_s_nextTime=curTime
                    SpawnMob_s_isLog=quest.CQuestManager.instance().GetEventFlag("spawn_block_log")


                if SpawnMob_s_isLog:
                    #sys_log(0, "SpawnMob: BLOCKED position for spawn %s %u at %d %d (attr %u)", pkMob.m_table.szName, dwVnum, x, y, dwAttr)
                return None

            ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'IS_SET' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
            if IS_SET(dwAttr, Globals.ATTR_BANPK):
                #sys_log(0, "SpawnMob: BAN_PK position for mob spawn %s %u at %d %d", pkMob.m_table.szName, dwVnum, x, y)
                return None

        sectree = SECTREE_MANAGER.instance().Get(uint(lMapIndex), uint(x), uint(y))

        if sectree is None:
            #sys_log(0, "SpawnMob: cannot create monster at non-exist sectree %d x %d (map %d)", x, y, lMapIndex)
            return None

        ch = CHARACTER_MANAGER.instance().CreateCharacter(pkMob.m_table.szLocaleName, 0)

        if ch is None:
            #sys_log(0, "SpawnMob: cannot create new character")
            return None

        if iRot == -1:
            iRot = number(0, 360)

        ch.SetProto(pkMob)

        if pkMob.m_table.bType == ECharType.CHAR_TYPE_NPC:
            if ch.GetEmpire() == 0:
                ch.SetEmpire(SECTREE_MANAGER.instance().GetEmpireFromMapIndex(lMapIndex))

        ch.SetRotation(iRot)

        if bShow and not ch.Show(lMapIndex, x, y, z, bSpawnMotion):
            CHARACTER_MANAGER.instance().DestroyCharacter(ch)
            #sys_log(0, "SpawnMob: cannot show monster")
            return None

        return (ch)

    def SpawnMobRange(self, dwVnum, lMapIndex, sx, sy, ex, ey, bIsException = LGEMiscellaneous.DefineConstants.false, bSpawnMotion = LGEMiscellaneous.DefineConstants.false, bAggressive = LGEMiscellaneous.DefineConstants.false):
        pkMob = CMobManager.instance().Get(dwVnum)

        if pkMob is None:
            return None

        if pkMob.m_table.bType == ECharType.CHAR_TYPE_STONE:
            bSpawnMotion = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        LaniatusDefVariables = 16

## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: while (LaniatusDefVariables--)
        while (i) != 0:
            LaniatusDefVariables -= 1
            x = number(sx, ex)
            y = number(sy, ey)

            ch = self.SpawnMob(dwVnum, lMapIndex, x, y, 0, bSpawnMotion, -1, ((not DefineConstants.false)))

            if ch:
                #sys_log(1, "MOB_SPAWN: %s(%d) %dx%d", ch.GetName(LOCALE_LANIATUS), ch.GetVID(), ch.GetX(), ch.GetY())
                if bAggressive:
                    ch.SetAggressive()
                return (ch)
        LaniatusDefVariables -= 1

        return None

    def SpawnGroup(self, dwVnum, lMapIndex, sx, sy, ex, ey, pkRegen = None, bAggressive_ = LGEMiscellaneous.DefineConstants.false, pDungeon = None):
        pkGroup = CMobManager.Instance().GetGroup(dwVnum)

        if pkGroup is None:
            #lani_err("NOT_EXIST_GROUP_VNUM(%u) Map(%u) ", dwVnum, lMapIndex)
            return None

        pkChrMaster = None
        pkParty = None

        c_rdwMembers = pkGroup.GetMemberVector()

        bSpawnedByStone = LGEMiscellaneous.DEFINECONSTANTS.false
        bAggressive = bAggressive_

        if self._m_pkChrSelectedStone:
            bSpawnedByStone = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

            if self._m_pkChrSelectedStone.GetDungeon():
                bAggressive = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        chLeader = None

        LaniatusDefVariables = 0
        while LaniatusDefVariables < len(c_rdwMembers):
            tch = self.SpawnMobRange(list(c_rdwMembers[LaniatusDefVariables]), lMapIndex, sx, sy, ex, ey, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), bSpawnedByStone, DefineConstants.false)

            if tch is None:
                if LaniatusDefVariables == 0:
                    return None

                continue

            if LaniatusDefVariables == 0:
                chLeader = tch

            tch.SetDungeon(pDungeon)

            sx = tch.GetX() - number(300, 500)
            sy = tch.GetY() - number(300, 500)
            ex = tch.GetX() + number(300, 500)
            ey = tch.GetY() + number(300, 500)

            if self._m_pkChrSelectedStone:
                tch.SetStone(self._m_pkChrSelectedStone)
            elif pkParty:
                pkParty.Join(tch.GetVID())
                pkParty.Link(tch)
            elif pkChrMaster is None:
                pkChrMaster = tch
                pkChrMaster.SetRegen(pkRegen)

                pkParty = CPartyManager.instance().CreateParty(pkChrMaster)

            if bAggressive:
                tch.SetAggressive()
            LaniatusDefVariables += 1

        return chLeader

    def SpawnGroupGroup(self, dwVnum, lMapIndex, sx, sy, ex, ey, pkRegen = None, bAggressive_ = LGEMiscellaneous.DefineConstants.false, pDungeon = None):
        dwGroupID = CMobManager.Instance().GetGroupFromGroupGroup(dwVnum)

        if dwGroupID != 0:
            return self.SpawnGroup(dwGroupID, lMapIndex, sx, sy, ex, ey, pkRegen, bAggressive_, pDungeon) is not None
        else:
            #lani_err("NOT_EXIST_GROUP_GROUP_VNUM(%u) MAP(%ld)", dwVnum, lMapIndex)
            return LGEMiscellaneous.DEFINECONSTANTS.false

    def SpawnMoveGroup(self, dwVnum, lMapIndex, sx, sy, ex, ey, tx, ty, pkRegen = None, bAggressive_ = LGEMiscellaneous.DefineConstants.false):
        pkGroup = CMobManager.Instance().GetGroup(dwVnum)

        if pkGroup is None:
            #lani_err("NOT_EXIST_GROUP_VNUM(%u) Map(%u) ", dwVnum, lMapIndex)
            return LGEMiscellaneous.DEFINECONSTANTS.false

        pkChrMaster = None
        pkParty = None

        c_rdwMembers = pkGroup.GetMemberVector()

        bSpawnedByStone = LGEMiscellaneous.DEFINECONSTANTS.false
        bAggressive = bAggressive_

        if self._m_pkChrSelectedStone:
            bSpawnedByStone = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
            if self._m_pkChrSelectedStone.GetDungeon():
                bAggressive = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        LaniatusDefVariables = 0
        while LaniatusDefVariables < len(c_rdwMembers):
            tch = self.SpawnMobRange(list(c_rdwMembers[LaniatusDefVariables]), lMapIndex, sx, sy, ex, ey, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), bSpawnedByStone, DefineConstants.false)

            if tch is None:
                if LaniatusDefVariables == 0:
                    return LGEMiscellaneous.DEFINECONSTANTS.false

                continue

            sx = tch.GetX() - number(300, 500)
            sy = tch.GetY() - number(300, 500)
            ex = tch.GetX() + number(300, 500)
            ey = tch.GetY() + number(300, 500)

            if self._m_pkChrSelectedStone:
                tch.SetStone(self._m_pkChrSelectedStone)
            elif pkParty:
                pkParty.Join(tch.GetVID())
                pkParty.Link(tch)
            elif pkChrMaster is None:
                pkChrMaster = tch
                pkChrMaster.SetRegen(pkRegen)

                pkParty = CPartyManager.instance().CreateParty(pkChrMaster)
            if bAggressive:
                tch.SetAggressive()

            if tch.Goto(tx, ty):
                tch.SendMovePacket(EMoveFuncType.FUNC_WAIT, 0, 0, 0, 0, 0, -1)
            LaniatusDefVariables += 1

        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def SpawnMobRandomPosition(self, dwVnum, lMapIndex):
            if dwVnum == 5001 and (quest.CQuestManager.instance().GetEventFlag("japan_regen")) == 0:
                #sys_log(1, "WAEGU[5001] regen disabled.")
                return None

            if dwVnum == 5002 and (quest.CQuestManager.instance().GetEventFlag("newyear_mob")) == 0:
                #sys_log(1, "HAETAE (new-year-mob) [5002] regen disabled.")
                return None

            if dwVnum == 5004 and (quest.CQuestManager.instance().GetEventFlag("independence_day")) == 0:
                #sys_log(1, "INDEPENDECE DAY [5004] regen disabled.")
                return None

        pkMob = CMobManager.instance().Get(dwVnum)

        if pkMob is None:
            #lani_err("no mob data for vnum %u", dwVnum)
            return None

        if not map_allow_find(lMapIndex):
            #lani_err("not allowed map %u", lMapIndex)
            return None

        pkSectreeMap = SECTREE_MANAGER.instance().GetMap(lMapIndex)
        if pkSectreeMap is None:
            return None

        LaniatusDefVariables = None
        x = None
        y = None
        for LaniatusDefVariables in range(0, 2000):
            x = number(1, (math.trunc(pkSectreeMap.m_setting.iWidth / float(100))) - 1) * 100 + pkSectreeMap.m_setting.iBaseX
            y = number(1, (math.trunc(pkSectreeMap.m_setting.iHeight / float(100))) - 1) * 100 + pkSectreeMap.m_setting.iBaseY

            tree = pkSectreeMap.Find(uint(x), uint(y))

            if tree is None:
                continue

            dwAttr = tree.GetAttribute(x, y)

            ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'IS_SET' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
            if IS_SET(dwAttr, Globals.ATTR_BLOCK | Globals.ATTR_OBJECT):
                continue

            ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'IS_SET' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
            if IS_SET(dwAttr, Globals.ATTR_BANPK):
                continue

            break

        if LaniatusDefVariables == 2000:
            #lani_err("cannot find valid location")
            return None

        sectree = SECTREE_MANAGER.instance().Get(uint(lMapIndex), uint(x), uint(y))

        if sectree is None:
            #sys_log(0, "SpawnMobRandomPosition: cannot create monster at non-exist sectree %d x %d (map %d)", x, y, lMapIndex)
            return None

        ch = CHARACTER_MANAGER.instance().CreateCharacter(pkMob.m_table.szLocaleName, 0)

        if ch is None:
            #sys_log(0, "SpawnMobRandomPosition: cannot create new character")
            return None

        ch.SetProto(pkMob)

        if pkMob.m_table.bType == ECharType.CHAR_TYPE_NPC:
            if ch.GetEmpire() == 0:
                ch.SetEmpire(SECTREE_MANAGER.instance().GetEmpireFromMapIndex(lMapIndex))

        ch.SetRotation(number(0, 360))

        if not ch.Show(lMapIndex, x, y, 0, LGEMiscellaneous.DEFINECONSTANTS.false):
            CHARACTER_MANAGER.instance().DestroyCharacter(ch)
            #lani_err(0, "SpawnMobRandomPosition: cannot show monster")
            return None

        buf = str(['\0' for _ in range(512+1)])
        local_x = x - pkSectreeMap.m_setting.iBaseX
        local_y = y - pkSectreeMap.m_setting.iBaseY
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        snprintf(buf, sizeof(buf), "spawn %s[%d] random position at %ld %ld %ld %ld (time: %d)", ch.GetName(LOCALE_LANIATUS), dwVnum, x, y, local_x, local_y, get_global_time())

        if test_server:
            SendNotice(buf)

        #sys_log(0, buf)
        return (ch)

    def SelectStone(self, pkChr):
        self._m_pkChrSelectedStone = pkChr

    def GetPCMap(self):
        return _boost_func_of_void.unordered_map(self._m_map_pkPCChr)

    def Find(self, dwVID):
        it = self._m_map_pkChrByVID.find(dwVID)

        if self._m_map_pkChrByVID.end() == it:
            return None

        found = it.second
        if found is not None and dwVID != found.GetVID():
            #lani_err("[CHARACTER_MANAGER::Find] <Factor> %u != %u", dwVID, found.GetVID())
            return None
        return found

    def Find(self, vid):
        tch = self.Find(vid)

        if tch is None or tch.GetVID() is not vid:
            return None

        return tch

    def FindPC(self, name):
        szName = str(['\0' for _ in range((int)LGEMiscellaneous.CHARACTER_NAME_MAX_LEN + 1)])
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        str_lower(name, szName, sizeof(szName))
        it = self._m_map_pkPCChr.find(szName)

        if it == self._m_map_pkPCChr.end():
            return None

        found = it.second
        if found is not None and _strnicmp(szName, found.GetName(LOCALE_LANIATUS), LGEMiscellaneous.CHARACTER_NAME_MAX_LEN) != 0:
            #lani_err("[CHARACTER_MANAGER::FindPC] <Factor> %s != %s", name, found.GetName(LOCALE_LANIATUS))
            return None
        return found

    def FindByPID(self, dwPID):
        it = self._m_map_pkChrByPID.find(dwPID)

        if self._m_map_pkChrByPID.end() == it:
            return None

        found = it.second
        if found is not None and dwPID != found.GetPlayerID():
            #lani_err("[CHARACTER_MANAGER::FindByPID] <Factor> %u != %u", dwPID, found.GetPlayerID())
            return None
        return found

    def AddToStateList(self, ch):
        assert ch is not None

        it = self._m_set_pkChrState.find(ch)

        if it == self._m_set_pkChrState.end():
            self._m_set_pkChrState.insert(ch)
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        return LGEMiscellaneous.DEFINECONSTANTS.false

    def RemoveFromStateList(self, ch):
        it = self._m_set_pkChrState.find(ch)

        if it != self._m_set_pkChrState.end():
            self._m_set_pkChrState.erase(it)

    def DelayedSave(self, ch):
        self._m_set_pkChrForDelayedSave.insert(ch)

    def FlushDelayedSave(self, ch):
        it = self._m_set_pkChrForDelayedSave.find(ch)

        if it == self._m_set_pkChrForDelayedSave.end():
            return LGEMiscellaneous.DEFINECONSTANTS.false

        self._m_set_pkChrForDelayedSave.erase(it)
        ch.SaveReal()
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def ProcessDelayedSave(self):
        it = self._m_set_pkChrForDelayedSave.begin()

        while it is not self._m_set_pkChrForDelayedSave.end():
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: CHARACTER* pkChr = *it++;
            pkChr = *it
            it += 1
            pkChr.SaveReal()

        self._m_set_pkChrForDelayedSave.clear()

    def for_each_pc(self, f):
        it = m_map_pkChrByPID.begin()
        while it is not self._m_map_pkChrByPID.end():
            f(it.second)
            it += 1

        return f

    def KillLog(self, dwVnum):
        SEND_LIMIT = 10000

        it = self._m_map_dwMobKillCount.find(dwVnum)

        if it is self._m_map_dwMobKillCount.end():
            self._m_map_dwMobKillCount.update({dwVnum: 1})
        else:
            it.second += 1

            if it.second > SEND_LIMIT:
                self._m_map_dwMobKillCount.pop(it)

    def RegisterRaceNum(self, dwVnum):
        self._m_set_dwRegisteredRaceNum.insert(dwVnum)

    def RegisterRaceNumMap(self, ch):
        dwVnum = ch.GetRaceNum()

        if self._m_set_dwRegisteredRaceNum.find(dwVnum) != self._m_set_dwRegisteredRaceNum.end():
            #sys_log(0, "RegisterRaceNumMap %s %u", ch.GetName(LOCALE_LANIATUS), dwVnum)
            self._m_map_pkChrByRaceNum[dwVnum].insert(ch)

    def UnregisterRaceNumMap(self, ch):
        dwVnum = ch.GetRaceNum()

        it = self._m_map_pkChrByRaceNum.find(dwVnum)

        if it is not self._m_map_pkChrByRaceNum.end():
            it.second.erase(ch)

    def GetCharactersByRaceNum(self, dwRaceNum, i):
        it = self._m_map_pkChrByRaceNum.find(dwRaceNum)

        if it is self._m_map_pkChrByRaceNum.end():
            return LGEMiscellaneous.DEFINECONSTANTS.false

        i.arg_value = it.second
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if ENABLE_WOLFMAN
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
##define FIND_JOB_WOLFMAN_0 = (1 << 15)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
##define FIND_JOB_WOLFMAN_1 = (1 << 16)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
##define FIND_JOB_WOLFMAN_2 = (1 << 17)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
##define FIND_JOB_WOLFMAN = (FIND_JOB_WOLFMAN_0 | FIND_JOB_WOLFMAN_1 | FIND_JOB_WOLFMAN_2)
##endif
    def FindSpecifyPC(self, uiJobFlag, lMapIndex, except_ = None, iMinLevel = 1, iMaxLevel = LGEMiscellaneous.PLAYER_MAX_LEVEL_CONST):
        chFind = None
        n = 0

        it = m_map_pkChrByPID.begin()
        while it is not self._m_map_pkChrByPID.end():
            ch = it.second

            if ch is except_:
                continue

            if ch.GetLevel() < iMinLevel:
                continue

            if ch.GetLevel() > iMaxLevel:
                continue

            if ch.GetMapIndex() != lMapIndex:
                continue

            if uiJobFlag != 0:
                uiChrJob = uint((1 << ((ch.GetJob() + 1) * 3 + ch.GetSkillGroup())))

                ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'IS_SET' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
                if not IS_SET(uiJobFlag, uiChrJob):
                    continue

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if (!chFind || number(1, ++n) == 1)
            if chFind is None or number(1, ++n) == 1:
                chFind = ch
            it += 1

        return chFind

    def SetMobItemRate(self, value):
        self._m_iMobItemRate = value
    def SetMobDamageRate(self, value):
        self._m_iMobDamageRate = value
    def SetMobGoldAmountRate(self, value):
        self._m_iMobGoldAmountRate = value
    def SetMobGoldDropRate(self, value):
        self._m_iMobGoldDropRate = value
    def SetMobExpRate(self, value):
        self._m_iMobExpRate = value

    def SetMobItemRatePremium(self, value):
        self._m_iMobItemRatePremium = value
    def SetMobGoldAmountRatePremium(self, value):
        self._m_iMobGoldAmountRatePremium = value
    def SetMobGoldDropRatePremium(self, value):
        self._m_iMobGoldDropRatePremium = value
    def SetMobExpRatePremium(self, value):
        self._m_iMobExpRatePremium = value

    def SetUserDamageRatePremium(self, value):
        self._m_iUserDamageRatePremium = value
    def SetUserDamageRate(self, value):
        self._m_iUserDamageRate = value
    def GetMobItemRate(self, ch):
        if ch is not None and ch.GetPremiumRemainSeconds(EPremiumTypes.PREMIUM_ITEM) > 0:
            return self._m_iMobItemRatePremium
        return self._m_iMobItemRate

    def GetMobDamageRate(self, ch):
        return self._m_iMobDamageRate

    def GetMobGoldAmountRate(self, ch):
        if ch is None:
            return self._m_iMobGoldAmountRate

        if ch is not None and ch.GetPremiumRemainSeconds(EPremiumTypes.PREMIUM_GOLD) > 0:
            return self._m_iMobGoldAmountRatePremium
        return self._m_iMobGoldAmountRate

    def GetMobGoldDropRate(self, ch):
        if ch is None:
            return self._m_iMobGoldDropRate

        if ch is not None and ch.GetPremiumRemainSeconds(EPremiumTypes.PREMIUM_GOLD) > 0:
            return self._m_iMobGoldDropRatePremium
        return self._m_iMobGoldDropRate

    def GetMobExpRate(self, ch):
        if ch is None:
            return self._m_iMobExpRate

        if ch is not None and ch.GetPremiumRemainSeconds(EPremiumTypes.PREMIUM_EXP) > 0:
            return self._m_iMobExpRatePremium
        return self._m_iMobExpRate

    def GetUserDamageRate(self, ch):
        if ch is None:
            return self._m_iUserDamageRate

        if ch is not None and ch.GetPremiumRemainSeconds(EPremiumTypes.PREMIUM_EXP) > 0:
            return self._m_iUserDamageRatePremium

        return self._m_iUserDamageRate

    def SendScriptToMap(self, lMapIndex, s):
        pSecMap = SECTREE_MANAGER.instance().GetMap(lMapIndex)

        if None is pSecMap:
            return

        p = packet_script()

        p.header = byte(Globals.LG_HEADER_GC_SCRIPT)
        p.skin = 1
        p.src_size = len(s)

        f = quest.FSendPacket()
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        p.size = p.src_size + sizeof(packet_script)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        f.buf.write(p, sizeof(packet_script))
        f.buf.write(s[0], len(s))

        pSecMap.for_each(f.functor_method)

    def BeginPendingDestroy(self):
        if self._m_bUsePendingDestroy:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        self._m_bUsePendingDestroy = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def FlushPendingDestroy(self):

        self._m_bUsePendingDestroy = LGEMiscellaneous.DEFINECONSTANTS.false

        if not self._m_set_pkChrPendingDestroy.empty():
            #sys_log(0, "FlushPendingDestroy size %d", self._m_set_pkChrPendingDestroy.size())

            it = self._m_set_pkChrPendingDestroy.begin()
            end = self._m_set_pkChrPendingDestroy.end()
            while it is not end:
                CHARACTER_MANAGER.instance().DestroyCharacter(auto(it))
                it += 1

            self._m_set_pkChrPendingDestroy.clear()










class CharacterVectorInteractor(list):

    def _initialize_instance_fields(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self._m_bMyBegin = False

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to multiple constructors:
#ORIGINAL METINII C CODE: CharacterVectorInteractor() : m_bMyBegin(DefineConstants.false)
    def __init__(self):
        self._initialize_instance_fields()

        self._m_bMyBegin = LGEMiscellaneous.DEFINECONSTANTS.false

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to multiple constructors:
#ORIGINAL METINII C CODE: CharacterVectorInteractor(const boost::unordered_set<CHARACTER*> & r)
    def __init__(self, r):
        self._initialize_instance_fields()


        reserve(r.size())
        insert(end(), r.begin(), r.end())

        if CHARACTER_MANAGER.instance().BeginPendingDestroy():
            self._m_bMyBegin = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def close(self):
        if self._m_bMyBegin:
            CHARACTER_MANAGER.instance().FlushPendingDestroy()


class FuncUpdateAndResetChatCounter:
    def functor_method(self, ch):
        ch.ResetChatCounter()
        ch.CFSM.Update()

## Laniatus Games Studio Inc. | NOTE: The following #define macro was replaced in-line:
#ORIGINAL METINII C CODE: #define FIND_JOB_LG_PAWN_WARRIOR_0 (1 << 3)
## Laniatus Games Studio Inc. | NOTE: The following #define macro was replaced in-line:
#ORIGINAL METINII C CODE: #define FIND_JOB_LG_PAWN_WARRIOR_1 (1 << 4)
## Laniatus Games Studio Inc. | NOTE: The following #define macro was replaced in-line:
#ORIGINAL METINII C CODE: #define FIND_JOB_LG_PAWN_WARRIOR_2 (1 << 5)
## Laniatus Games Studio Inc. | NOTE: The following #define macro was replaced in-line:
#ORIGINAL METINII C CODE: #define FIND_JOB_LG_PAWN_WARRIOR (FIND_JOB_LG_PAWN_WARRIOR_0 | FIND_JOB_LG_PAWN_WARRIOR_1 | FIND_JOB_LG_PAWN_WARRIOR_2)
## Laniatus Games Studio Inc. | NOTE: The following #define macro was replaced in-line:
#ORIGINAL METINII C CODE: #define FIND_JOB_LG_PAWN_ASSASSIN_0 (1 << 6)
## Laniatus Games Studio Inc. | NOTE: The following #define macro was replaced in-line:
#ORIGINAL METINII C CODE: #define FIND_JOB_LG_PAWN_ASSASSIN_1 (1 << 7)
## Laniatus Games Studio Inc. | NOTE: The following #define macro was replaced in-line:
#ORIGINAL METINII C CODE: #define FIND_JOB_LG_PAWN_ASSASSIN_2 (1 << 8)
## Laniatus Games Studio Inc. | NOTE: The following #define macro was replaced in-line:
#ORIGINAL METINII C CODE: #define FIND_JOB_LG_PAWN_ASSASSIN (FIND_JOB_LG_PAWN_ASSASSIN_0 | FIND_JOB_LG_PAWN_ASSASSIN_1 | FIND_JOB_LG_PAWN_ASSASSIN_2)
## Laniatus Games Studio Inc. | NOTE: The following #define macro was replaced in-line:
#ORIGINAL METINII C CODE: #define FIND_JOB_LG_PAWN_SHURA_0 (1 << 9)
## Laniatus Games Studio Inc. | NOTE: The following #define macro was replaced in-line:
#ORIGINAL METINII C CODE: #define FIND_JOB_LG_PAWN_SHURA_1 (1 << 10)
## Laniatus Games Studio Inc. | NOTE: The following #define macro was replaced in-line:
#ORIGINAL METINII C CODE: #define FIND_JOB_LG_PAWN_SHURA_2 (1 << 11)
## Laniatus Games Studio Inc. | NOTE: The following #define macro was replaced in-line:
#ORIGINAL METINII C CODE: #define FIND_JOB_LG_PAWN_SHURA (FIND_JOB_LG_PAWN_SHURA_0 | FIND_JOB_LG_PAWN_SHURA_1 | FIND_JOB_LG_PAWN_SHURA_2)
## Laniatus Games Studio Inc. | NOTE: The following #define macro was replaced in-line:
#ORIGINAL METINII C CODE: #define FIND_JOB_LG_PAWN_MAGE_0 (1 << 12)
## Laniatus Games Studio Inc. | NOTE: The following #define macro was replaced in-line:
#ORIGINAL METINII C CODE: #define FIND_JOB_LG_PAWN_MAGE_1 (1 << 13)
## Laniatus Games Studio Inc. | NOTE: The following #define macro was replaced in-line:
#ORIGINAL METINII C CODE: #define FIND_JOB_LG_PAWN_MAGE_2 (1 << 14)
## Laniatus Games Studio Inc. | NOTE: The following #define macro was replaced in-line:
#ORIGINAL METINII C CODE: #define FIND_JOB_LG_PAWN_MAGE (FIND_JOB_LG_PAWN_MAGE_0 | FIND_JOB_LG_PAWN_MAGE_1 | FIND_JOB_LG_PAWN_MAGE_2)

