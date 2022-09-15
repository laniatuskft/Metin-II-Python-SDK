import math

## Laniatus Games Studio Inc. | NOTE: Anonymous namespaces are not defined:
#namespace
class FuncFindChrForFlag:
    def __init__(self, pkChr):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.m_pkChr = None
        self.m_pkChrFind = None
        self.m_iMinDistance = 0

        self.m_pkChr = pkChr
        self.m_pkChrFind = None
        self.m_iMinDistance = numeric_limits.max()

    def functor_method(self, ent):
        if not ent.IsType(EEntityTypes.ENTITY_CHARACTER):
            return

        if ent.IsObserverMode():
            return

        pkChr = ent

        if not pkChr.IsPC():
            return

        if pkChr.GetGuild() is None:
            return

        if pkChr.IsDead():
            return

        iDist = Globals.DISTANCE_APPROX(pkChr.GetX()-self.m_pkChr.GetX(), pkChr.GetY()-self.m_pkChr.GetY())

        if iDist <= 500 and self.m_iMinDistance > iDist and (not pkChr.IsAffectFlag(EAffectBits.AFF_WAR_FLAG1)) and (not pkChr.IsAffectFlag(EAffectBits.AFF_WAR_FLAG2)) and not pkChr.IsAffectFlag(EAffectBits.AFF_WAR_FLAG3):
            if self.m_pkChr.GetPoint(EPointTypes.LG_POINT_STAT) == pkChr.GetGuild().GetID():
                pMap = pkChr.GetWarMap()
                idx = None

                temp_ref_idx = RefObject(idx);
                if pMap is None or not pMap.GetTeamIndex(pkChr.GetGuild().GetID(), temp_ref_idx):
                    idx = temp_ref_idx.arg_value
                    return
                else:
                    idx = temp_ref_idx.arg_value

                if not pMap.IsFlagOnBase(idx):
                    self.m_pkChrFind = pkChr
                    self.m_iMinDistance = iDist
            else:
                self.m_pkChrFind = pkChr
                self.m_iMinDistance = iDist


class FuncFindChrForFlagBase:
    def __init__(self, pkChr):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.m_pkChr = None

        self.m_pkChr = pkChr

    def functor_method(self, ent):
        if not ent.IsType(EEntityTypes.ENTITY_CHARACTER):
            return

        if ent.IsObserverMode():
            return

        pkChr = ent

        if not pkChr.IsPC():
            return

        pkGuild = pkChr.GetGuild()

        if pkGuild is None:
            return

        iDist = Globals.DISTANCE_APPROX(pkChr.GetX()-self.m_pkChr.GetX(), pkChr.GetY()-self.m_pkChr.GetY())

        if iDist <= 500 and (pkChr.IsAffectFlag(EAffectBits.AFF_WAR_FLAG1) or pkChr.IsAffectFlag(EAffectBits.AFF_WAR_FLAG2) or pkChr.IsAffectFlag(EAffectBits.AFF_WAR_FLAG3)):
            pkAff = pkChr.FindAffect(LaniatusEAffectTypes.LANIA_AFFECT_WAR_FLAG, APPLY_NONE)

            #sys_log(0, "FlagBase %s dist %d aff %p flag gid %d chr gid %u", pkChr.GetName(LOCALE_LANIATUS), iDist, pkAff, self.m_pkChr.GetPoint(EPointTypes.LG_POINT_STAT), pkChr.GetGuild().GetID())

            if pkAff:
                if self.m_pkChr.GetPoint(EPointTypes.LG_POINT_STAT) == pkGuild.GetID() and self.m_pkChr.GetPoint(EPointTypes.LG_POINT_STAT) != pkAff.lApplyValue:
                    pMap = pkChr.GetWarMap()
                    idx = None

                    temp_ref_idx = RefObject(idx);
                    if pMap is None or not pMap.GetTeamIndex(pkGuild.GetID(), temp_ref_idx):
                        idx = temp_ref_idx.arg_value
                        return
                    else:
                        idx = temp_ref_idx.arg_value

                        idx_opp = byte(1 if idx == 0 else 0)
                        SendGuildWarScore(self.m_pkChr.GetPoint(EPointTypes.LG_POINT_STAT), pkAff.lApplyValue, 1)
                        pMap.ResetFlag()
                        buf = str(['\0' for _ in range(256)])
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                        snprintf(buf, sizeof(buf), LC_TEXT("%s Guild captured the Flag of the %s Guild!"), pMap.GetGuild(idx).GetName(), pMap.GetGuild(idx_opp).GetName())
                        pMap.Notice(buf)


class FuncFindGuardVictim:
    def __init__(self, pkChr, iMaxDistance):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self._m_pkChr = None
        self._m_iMinDistance = 0
        self._m_iMaxDistance = 0
        self._m_lx = 0
        self._m_ly = 0
        self._m_pkChrVictim = None

        self._m_pkChr = pkChr
        self._m_iMinDistance = numeric_limits.max()
        self._m_iMaxDistance = iMaxDistance
        self._m_lx = pkChr.GetX()
        self._m_ly = pkChr.GetY()
        self._m_pkChrVictim = None

    def functor_method(self, ent):
        if not ent.IsType(EEntityTypes.ENTITY_CHARACTER):
            return

        pkChr = ent

        if pkChr.IsPC():
            return


        if pkChr.IsNPC() and not pkChr.IsMonster():
            return

        if pkChr.IsDead():
            return

        if pkChr.IsAffectFlag(EAffectBits.AFF_EUNHYUNG) or pkChr.IsAffectFlag(EAffectBits.AFF_INVISIBILITY) or pkChr.IsAffectFlag(EAffectBits.AFF_REVIVE_INVISIBLE):
            return

        if pkChr.GetRaceNum() == 5001:
            return

        iDistance = Globals.DISTANCE_APPROX(self._m_lx - pkChr.GetX(), self._m_ly - pkChr.GetY())

        if iDistance < self._m_iMinDistance and iDistance <= self._m_iMaxDistance:
            self._m_pkChrVictim = pkChr
            self._m_iMinDistance = iDistance

    def GetVictim(self):
        return (self._m_pkChrVictim)





## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: bool CHARACTER::IsAggressive() const
def IsAggressive():
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'IS_SET' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
    return IS_SET(m_pointsInstant.dwAIFlag, EAIFlags.AIFLAG_AGGRESSIVE)

def SetAggressive():
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'SET_BIT' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
    SET_BIT(m_pointsInstant.dwAIFlag, EAIFlags.AIFLAG_AGGRESSIVE)

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: bool CHARACTER::IsCoward() const
def IsCoward():
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'IS_SET' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
    return IS_SET(m_pointsInstant.dwAIFlag, EAIFlags.AIFLAG_COWARD)

def SetCoward():
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'SET_BIT' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
    SET_BIT(m_pointsInstant.dwAIFlag, EAIFlags.AIFLAG_COWARD)

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: bool CHARACTER::IsBerserker() const
def IsBerserker():
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'IS_SET' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
    return IS_SET(m_pointsInstant.dwAIFlag, EAIFlags.AIFLAG_BERSERK)

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: bool CHARACTER::IsStoneSkinner() const
def IsStoneSkinner():
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'IS_SET' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
    return IS_SET(m_pointsInstant.dwAIFlag, EAIFlags.AIFLAG_STONESKIN)

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: bool CHARACTER::IsGodSpeeder() const
def IsGodSpeeder():
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'IS_SET' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
    return IS_SET(m_pointsInstant.dwAIFlag, EAIFlags.AIFLAG_GODSPEED)

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: bool CHARACTER::IsDeathBlower() const
def IsDeathBlower():
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'IS_SET' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
    return IS_SET(m_pointsInstant.dwAIFlag, EAIFlags.AIFLAG_DEATHBLOW)

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: bool CHARACTER::IsReviver() const
def IsReviver():
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'IS_SET' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
    return IS_SET(m_pointsInstant.dwAIFlag, EAIFlags.AIFLAG_REVIVE)

def CowardEscape():
    iDist = [500, 1000, 3000, 5000]

    for iDistIdx in range(2, -1, -1):
        for iTryCount in range(0, 8):
            SetRotation(number(0, 359))

            fx = None
            fy = None
            fDist = number(iDist[iDistIdx], iDist[iDistIdx+1])

            GetDeltaByDegree(GetRotation(), fDist, fx, fy)

            bIsWayBlocked = LGEMiscellaneous.DEFINECONSTANTS.false
            for j in range(1, 101):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
                if not SECTREE_MANAGER.instance().IsMovablePosition(GetMapIndex(), GetX() + int(fx) *j/100, GetY() + int(fy) *j/100):
                    bIsWayBlocked = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
                    break

            if bIsWayBlocked:
                continue

            m_dwStateDuration = ((1) * passes_per_sec)

            iDestX = GetX() + int(fx)
            iDestY = GetY() + int(fy)

            if Goto(iDestX, iDestY):
                SendMovePacket(EMoveFuncType.FUNC_WAIT, 0, 0, 0, 0)

            #sys_log(0, "WAEGU move to %d %d (far)", iDestX, iDestY)
            return

def SetNoAttackShinsu():
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'SET_BIT' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
    SET_BIT(m_pointsInstant.dwAIFlag, EAIFlags.AIFLAG_NOATTACKSHINSU)
## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: bool CHARACTER::IsNoAttackShinsu() const
def IsNoAttackShinsu():
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'IS_SET' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
    return IS_SET(m_pointsInstant.dwAIFlag, EAIFlags.AIFLAG_NOATTACKSHINSU)

def SetNoAttackChunjo():
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'SET_BIT' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
    SET_BIT(m_pointsInstant.dwAIFlag, EAIFlags.AIFLAG_NOATTACKCHUNJO)

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: bool CHARACTER::IsNoAttackChunjo() const
def IsNoAttackChunjo():
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'IS_SET' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
    return IS_SET(m_pointsInstant.dwAIFlag, EAIFlags.AIFLAG_NOATTACKCHUNJO)

def SetNoAttackJinno():
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'SET_BIT' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
    SET_BIT(m_pointsInstant.dwAIFlag, EAIFlags.AIFLAG_NOATTACKJINNO)

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: bool CHARACTER::IsNoAttackJinno() const
def IsNoAttackJinno():
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'IS_SET' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
    return IS_SET(m_pointsInstant.dwAIFlag, EAIFlags.AIFLAG_NOATTACKJINNO)

def SetAttackMob():
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'SET_BIT' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
    SET_BIT(m_pointsInstant.dwAIFlag, EAIFlags.AIFLAG_ATTACKMOB)

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: bool CHARACTER::IsAttackMob() const
def IsAttackMob():
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'IS_SET' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
    return IS_SET(m_pointsInstant.dwAIFlag, EAIFlags.AIFLAG_ATTACKMOB)

def StateIdle():
    if IsStone():
        __StateIdle_Stone()
        return
    elif IsWarp() or IsGoto():
        m_dwStateDuration = 60 * passes_per_sec
        return

    if IsPC():
        return

    if not IsMonster():
        __StateIdle_NPC()
        return

    __StateIdle_Monster()

def __StateIdle_Stone():
    m_dwStateDuration = ((1) * passes_per_sec)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
    iPercent = (GetHP() * 100) / GetMaxHP()
    dwVnum = number(MIN(GetMobTable().sAttackSpeed, GetMobTable().sMovingSpeed), MAX(GetMobTable().sAttackSpeed, GetMobTable().sMovingSpeed))

    if iPercent <= 10 and GetMaxSP() < 10:
        SetMaxSP(10)
        SendMovePacket(EMoveFuncType.FUNC_ATTACK, 0, GetX(), GetY(), 0)

        CHARACTER_MANAGER.instance().SelectStone(self)
        CHARACTER_MANAGER.instance().SpawnGroup(dwVnum, GetMapIndex(), GetX() - 500, GetY() - 500, GetX() + 500, GetY() + 500, NULL, DefineConstants.false, NULL)
        CHARACTER_MANAGER.instance().SpawnGroup(dwVnum, GetMapIndex(), GetX() - 1000, GetY() - 1000, GetX() + 1000, GetY() + 1000, NULL, DefineConstants.false, NULL)
        CHARACTER_MANAGER.instance().SpawnGroup(dwVnum, GetMapIndex(), GetX() - 1500, GetY() - 1500, GetX() + 1500, GetY() + 1500, NULL, DefineConstants.false, NULL)
        CHARACTER_MANAGER.instance().SelectStone(None)
    elif iPercent <= 20 and GetMaxSP() < 9:
        SetMaxSP(9)
        SendMovePacket(EMoveFuncType.FUNC_ATTACK, 0, GetX(), GetY(), 0)

        CHARACTER_MANAGER.instance().SelectStone(self)
        CHARACTER_MANAGER.instance().SpawnGroup(dwVnum, GetMapIndex(), GetX() - 500, GetY() - 500, GetX() + 500, GetY() + 500, NULL, DefineConstants.false, NULL)
        CHARACTER_MANAGER.instance().SpawnGroup(dwVnum, GetMapIndex(), GetX() - 1000, GetY() - 1000, GetX() + 1000, GetY() + 1000, NULL, DefineConstants.false, NULL)
        CHARACTER_MANAGER.instance().SpawnGroup(dwVnum, GetMapIndex(), GetX() - 1500, GetY() - 1500, GetX() + 1500, GetY() + 1500, NULL, DefineConstants.false, NULL)
        CHARACTER_MANAGER.instance().SelectStone(None)
    elif iPercent <= 30 and GetMaxSP() < 8:
        SetMaxSP(8)
        SendMovePacket(EMoveFuncType.FUNC_ATTACK, 0, GetX(), GetY(), 0)

        CHARACTER_MANAGER.instance().SelectStone(self)
        CHARACTER_MANAGER.instance().SpawnGroup(dwVnum, GetMapIndex(), GetX() - 500, GetY() - 500, GetX() + 500, GetY() + 500, NULL, DefineConstants.false, NULL)
        CHARACTER_MANAGER.instance().SpawnGroup(dwVnum, GetMapIndex(), GetX() - 1000, GetY() - 1000, GetX() + 1000, GetY() + 1000, NULL, DefineConstants.false, NULL)
        CHARACTER_MANAGER.instance().SpawnGroup(dwVnum, GetMapIndex(), GetX() - 1000, GetY() - 1000, GetX() + 1000, GetY() + 1000, NULL, DefineConstants.false, NULL)
        CHARACTER_MANAGER.instance().SelectStone(None)
    elif iPercent <= 40 and GetMaxSP() < 7:
        SetMaxSP(7)
        SendMovePacket(EMoveFuncType.FUNC_ATTACK, 0, GetX(), GetY(), 0)

        CHARACTER_MANAGER.instance().SelectStone(self)
        CHARACTER_MANAGER.instance().SpawnGroup(dwVnum, GetMapIndex(), GetX() - 1000, GetY() - 1000, GetX() + 1000, GetY() + 1000, NULL, DefineConstants.false, NULL)
        CHARACTER_MANAGER.instance().SpawnGroup(dwVnum, GetMapIndex(), GetX() - 1000, GetY() - 1000, GetX() + 1000, GetY() + 1000, NULL, DefineConstants.false, NULL)
        CHARACTER_MANAGER.instance().SpawnGroup(dwVnum, GetMapIndex(), GetX() - 1000, GetY() - 1000, GetX() + 1000, GetY() + 1000, NULL, DefineConstants.false, NULL)
        CHARACTER_MANAGER.instance().SelectStone(None)
    elif iPercent <= 50 and GetMaxSP() < 6:
        SetMaxSP(6)
        SendMovePacket(EMoveFuncType.FUNC_ATTACK, 0, GetX(), GetY(), 0)

        CHARACTER_MANAGER.instance().SelectStone(self)
        CHARACTER_MANAGER.instance().SpawnGroup(dwVnum, GetMapIndex(), GetX() - 1000, GetY() - 1000, GetX() + 1000, GetY() + 1000, NULL, DefineConstants.false, NULL)
        CHARACTER_MANAGER.instance().SpawnGroup(dwVnum, GetMapIndex(), GetX() - 1000, GetY() - 1000, GetX() + 1000, GetY() + 1000, NULL, DefineConstants.false, NULL)
        CHARACTER_MANAGER.instance().SelectStone(None)
    elif iPercent <= 60 and GetMaxSP() < 5:
        SetMaxSP(5)
        SendMovePacket(EMoveFuncType.FUNC_ATTACK, 0, GetX(), GetY(), 0)

        CHARACTER_MANAGER.instance().SelectStone(self)
        CHARACTER_MANAGER.instance().SpawnGroup(dwVnum, GetMapIndex(), GetX() - 1000, GetY() - 1000, GetX() + 1000, GetY() + 1000, NULL, DefineConstants.false, NULL)
        CHARACTER_MANAGER.instance().SpawnGroup(dwVnum, GetMapIndex(), GetX() - 500, GetY() - 500, GetX() + 500, GetY() + 500, NULL, DefineConstants.false, NULL)
        CHARACTER_MANAGER.instance().SelectStone(None)
    elif iPercent <= 70 and GetMaxSP() < 4:
        SetMaxSP(4)
        SendMovePacket(EMoveFuncType.FUNC_ATTACK, 0, GetX(), GetY(), 0)

        CHARACTER_MANAGER.instance().SelectStone(self)
        CHARACTER_MANAGER.instance().SpawnGroup(dwVnum, GetMapIndex(), GetX() - 500, GetY() - 500, GetX() + 500, GetY() + 500, NULL, DefineConstants.false, NULL)
        CHARACTER_MANAGER.instance().SpawnGroup(dwVnum, GetMapIndex(), GetX() - 1000, GetY() - 1000, GetX() + 1000, GetY() + 1000, NULL, DefineConstants.false, NULL)
        CHARACTER_MANAGER.instance().SelectStone(None)
    elif iPercent <= 80 and GetMaxSP() < 3:
        SetMaxSP(3)
        SendMovePacket(EMoveFuncType.FUNC_ATTACK, 0, GetX(), GetY(), 0)

        CHARACTER_MANAGER.instance().SelectStone(self)
        CHARACTER_MANAGER.instance().SpawnGroup(dwVnum, GetMapIndex(), GetX() - 1000, GetY() - 1000, GetX() + 1000, GetY() + 1000, NULL, DefineConstants.false, NULL)
        CHARACTER_MANAGER.instance().SpawnGroup(dwVnum, GetMapIndex(), GetX() - 1000, GetY() - 1000, GetX() + 1000, GetY() + 1000, NULL, DefineConstants.false, NULL)
        CHARACTER_MANAGER.instance().SelectStone(None)
    elif iPercent <= 90 and GetMaxSP() < 2:
        SetMaxSP(2)
        SendMovePacket(EMoveFuncType.FUNC_ATTACK, 0, GetX(), GetY(), 0)

        CHARACTER_MANAGER.instance().SelectStone(self)
        CHARACTER_MANAGER.instance().SpawnGroup(dwVnum, GetMapIndex(), GetX() - 500, GetY() - 500, GetX() + 500, GetY() + 500, NULL, DefineConstants.false, NULL)
        CHARACTER_MANAGER.instance().SelectStone(None)
    elif iPercent <= 99 and GetMaxSP() < 1:
        SetMaxSP(1)
        SendMovePacket(EMoveFuncType.FUNC_ATTACK, 0, GetX(), GetY(), 0)

        CHARACTER_MANAGER.instance().SelectStone(self)
        CHARACTER_MANAGER.instance().SpawnGroup(dwVnum, GetMapIndex(), GetX() - 1000, GetY() - 1000, GetX() + 1000, GetY() + 1000, NULL, DefineConstants.false, NULL)
        CHARACTER_MANAGER.instance().SelectStone(None)
    else:
        return

    UpdatePacket()
    return

def __StateIdle_NPC():
    m_dwStateDuration = ((5) * passes_per_sec)

    if IsPet():
        return
    elif IsGuardNPC():
        if (quest.CQuestManager.instance().GetEventFlag("noguard")) == 0:
            f = FuncFindGuardVictim(self, 50000)

            if GetSectree():
                GetSectree().ForEachAround(f.functor_method)

            victim = f.GetVictim()

            if victim:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
                m_dwStateDuration = passes_per_sec/2

                if CanBeginFight():
                    BeginFight(victim)
    else:
        if GetRaceNum() == xmas.MOB_SANTA_VNUM:
            if get_dword_time() > m_dwPlayStartTime:
                next_warp_time = 2 * 1000

                m_dwPlayStartTime = get_dword_time() + next_warp_time

                WARP_MAP_INDEX_NUM = 7
                c_lWarpMapIndexs = [61, 62, 63, 64, 3, 23, 43] + [0 for _ in range(WARP_MAP_INDEX_NUM - 7)]
                lNextMapIndex = None
                lNextMapIndex = c_lWarpMapIndexs[number(1, WARP_MAP_INDEX_NUM) - 1]

                if map_allow_find(lNextMapIndex):
                    CHARACTER_MANAGER.instance().DestroyCharacter(self)
                    iNextSpawnDelay = 50 * 60

                    xmas.SpawnSanta(lNextMapIndex, iNextSpawnDelay)
                else:
                    p = SPacketGGXmasWarpSanta()
                    p.bHeader = byte(LG_HEADER_GG_XMAS_WARP_SANTA)
                    p.bChannel = g_bChannel
                    p.lMapIndex = lNextMapIndex
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                    P2P_MANAGER.instance().Send(p, sizeof(SPacketGGXmasWarpSanta), NULL)
                return

        ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'IS_SET' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
        if not IS_SET(m_pointsInstant.dwAIFlag, EAIFlags.AIFLAG_NOMOVE):
            pkChrProtege = GetProtege()

            if pkChrProtege:
                if DISTANCE_APPROX(GetX() - pkChrProtege.GetX(), GetY() - pkChrProtege.GetY()) > 500:
                    if Follow(pkChrProtege, number(100, 300)):
                        return

            if not number(0, 6):
                SetRotation(number(0, 359))

                fx = None
                fy = None
                fDist = number(200, 400)

                GetDeltaByDegree(GetRotation(), fDist, fx, fy)

                if not(SECTREE_MANAGER.instance().IsMovablePosition(GetMapIndex(), GetX() + int(fx), GetY() + int(fy)) and SECTREE_MANAGER.instance().IsMovablePosition(GetMapIndex(), GetX() + math.trunc(int(fx) / float(2)), GetY() + math.trunc(int(fy) / float(2)))):
                    return

                SetNowWalking(((not LGEMiscellaneous.DEFINECONSTANTS.false)))

                if Goto(GetX() + int(fx), GetY() + int(fy)):
                    SendMovePacket(EMoveFuncType.FUNC_WAIT, 0, 0, 0, 0)

                return

def __StateIdle_Monster():
    if IsStun():
        return

    if not CanMove():
        return

    if IsCoward():
        if not IsDead():
            CowardEscape()

        return

    if IsBerserker():
        if IsBerserk():
            SetBerserk(LGEMiscellaneous.DEFINECONSTANTS.false)

    if IsGodSpeeder():
        if IsGodSpeed():
            SetGodSpeed(LGEMiscellaneous.DEFINECONSTANTS.false)

    victim = GetVictim()

    if victim is None or victim.IsDead():
        SetVictim(None)
        victim = None
        m_dwStateDuration = ((1) * passes_per_sec)

    if victim is None or victim.IsBuilding():
        if m_pkChrStone:
            victim = m_pkChrStone.GetNearestVictim(m_pkChrStone)
        elif (not no_wander) and IsAggressive():
            if GetMapIndex() == 61 and (quest.CQuestManager.instance().GetEventFlag("xmas_tree")) != 0:
                pass

            else:
                victim = FindVictim(self, m_pkMobData.m_table.wAggressiveSight)

    if victim is not None and not victim.IsDead():
        if CanBeginFight():
            BeginFight(victim)

        return

    if IsAggressive() and victim is None:
        m_dwStateDuration = ((number(1, 3)) * passes_per_sec)
    else:
        m_dwStateDuration = ((number(3, 5)) * passes_per_sec)

    pkChrProtege = GetProtege()

    if pkChrProtege:
        if DISTANCE_APPROX(GetX() - pkChrProtege.GetX(), GetY() - pkChrProtege.GetY()) > 1000:
            if Follow(pkChrProtege, number(150, 400)):
                return

    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'IS_SET' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
    if (not no_wander) and not IS_SET(m_pointsInstant.dwAIFlag, EAIFlags.AIFLAG_NOMOVE):
        if not number(0, 6):
            SetRotation(number(0, 359))

            fx = None
            fy = None
            fDist = number(300, 700)

            GetDeltaByDegree(GetRotation(), fDist, fx, fy)

            if not(SECTREE_MANAGER.instance().IsMovablePosition(GetMapIndex(), GetX() + int(fx), GetY() + int(fy)) and SECTREE_MANAGER.instance().IsMovablePosition(GetMapIndex(), GetX() + math.trunc(int(fx) / float(2)), GetY() + math.trunc(int(fy) / float(2)))):
                return

            if g_test_server:
                if number(0, 100) < 60:
                    SetNowWalking(LGEMiscellaneous.DEFINECONSTANTS.false)
                else:
                    SetNowWalking(((not LGEMiscellaneous.DEFINECONSTANTS.false)))

            if Goto(GetX() + int(fx), GetY() + int(fy)):
                SendMovePacket(EMoveFuncType.FUNC_WAIT, 0, 0, 0, 0)

            return

def StateMove():
    dwElapsedTime = get_dword_time() - m_dwMoveStartTime
    fRate = float(dwElapsedTime) / float(m_dwMoveDuration)

    if fRate > 1.0:
        fRate = 1.0

    x = int((float((m_posDest.x - m_posStart.x)) * fRate + m_posStart.x))
    y = int((float((m_posDest.y - m_posStart.y)) * fRate + m_posStart.y))

    Move(x, y)

    if IsPC() and (thecore_pulse() & 15) == 0:
        UpdateSectree()

        if GetExchange():
            victim = GetExchange().GetCompany().GetOwner()
            iDist = DISTANCE_APPROX(GetX() - victim.GetX(), GetY() - victim.GetY())

            if iDist >= EExchangeValues.EXCHANGE_MAX_DISTANCE:
                GetExchange().Cancel()

    if IsPC():
        if IsWalking() and GetStamina() < GetMaxStamina():
            if get_dword_time() - GetWalkStartTime() > 5000:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
                PointChange(EPointTypes.LG_POINT_STAMINA, GetMaxStamina() / 1)

        if (not IsWalking()) and not IsRiding():
            if (get_dword_time() - GetLastAttackTime()) < 20000:
                StartAffectEvent()

                if IsStaminaHalfConsume():
                    if (thecore_pulse()&1) != 0:
                        PointChange(EPointTypes.LG_POINT_STAMINA, -STAMINA_PER_STEP)
                else:
                    PointChange(EPointTypes.LG_POINT_STAMINA, -STAMINA_PER_STEP)

                StartStaminaConsume()

                if GetStamina() <= 0:
                    SetStamina(0)
                    SetNowWalking(((not LGEMiscellaneous.DEFINECONSTANTS.false)))
                    StopStaminaConsume()
            elif IsStaminaConsume():
                StopStaminaConsume()
    else:
        if IsMonster() and GetVictim():
            victim = GetVictim()
            UpdateAggrPoint(victim, EDamageType.DAMAGE_TYPE_NORMAL, -(math.trunc(victim.GetLevel() / float(3)) + 1))

            if g_test_server:
                SetNowWalking(LGEMiscellaneous.DEFINECONSTANTS.false)

        if IsMonster() and GetMobRank() >= EMobRank.MOB_RANK_BOSS and GetVictim():
            victim = GetVictim()

            if GetRaceNum() == 2191 and number(1, 20) == 1 and get_dword_time() - m_pkMobInst.m_dwLastWarpTime > 1000:
                fx = None
                fy = None
                GetDeltaByDegree(victim.GetRotation(), 400, fx, fy)
                new_x = victim.GetX() + int(fx)
                new_y = victim.GetY() + int(fy)
                SetRotation(GetDegreeFromPositionXY(new_x, new_y, victim.GetX(), victim.GetY()))
                Show(victim.GetMapIndex(), new_x, new_y, 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
                GotoState(m_stateBattle)
                m_dwStateDuration = 1
                ResetMobSkillCooltime()
                m_pkMobInst.m_dwLastWarpTime = get_dword_time()
                return

            if number(0, 3) == 0:
                if __CHARACTER_GotoNearTarget(self, victim):
                    return

    if 1.0 == fRate:
        if IsPC():
            #sys_log(1, "���� %s %d %d", GetName(), x, y)
            GotoState(m_stateIdle)
            StopStaminaConsume()
        else:
            if GetVictim() and not IsCoward():
                GotoState(m_stateBattle)
                m_dwStateDuration = 1
            else:
                GotoState(m_stateIdle)

                rider = GetRider()

                if rider:
                    m_dwStateDuration = 1
                else:
                    m_dwStateDuration = ((number(1, 3)) * passes_per_sec)

def StateBattle():
    if IsStone():
        #lani_err("Stone must not use battle state (name %s)", GetName())
        return

    if IsPC():
        return

    if not CanMove():
        return

    if IsStun():
        return

    victim = GetVictim()

    if IsCoward():
        if IsDead():
            return

        SetVictim(None)

        if number(1, 50) != 1:
            GotoState(m_stateIdle)
            m_dwStateDuration = 1
        else:
            CowardEscape()

        return

    if victim is None or (victim.IsStun() and IsGuardNPC()) or victim.IsDead():
        if victim is not None and victim.IsDead() and (not no_wander) and IsAggressive() and ((not GetParty()) or GetParty().GetLeader() is self):
            new_victim = FindVictim(self, m_pkMobData.m_table.wAggressiveSight)

            SetVictim(new_victim)
            m_dwStateDuration = ((1) * passes_per_sec)

            if new_victim is None:
                if (GetMobBattleType() == EBattleType.BATTLE_TYPE_MELEE) or (GetMobBattleType() == EBattleType.BATTLE_TYPE_SUPER_POWER) or (GetMobBattleType() == EBattleType.BATTLE_TYPE_SUPER_TANKER) or (GetMobBattleType() == EBattleType.BATTLE_TYPE_POWER) or (GetMobBattleType() == EBattleType.BATTLE_TYPE_TANKER):
                        fx = None
                        fy = None
                        fDist = number(400, 1500)

                        GetDeltaByDegree(number(0, 359), fDist, fx, fy)

                        if SECTREE_MANAGER.instance().IsMovablePosition(victim.GetMapIndex(), victim.GetX() + int(fx), victim.GetY() + int(fy)) and SECTREE_MANAGER.instance().IsMovablePosition(victim.GetMapIndex(), victim.GetX() + math.trunc(int(fx) / float(2)), victim.GetY() + math.trunc(int(fy) / float(2))):
                            dx = victim.GetX() + fx
                            dy = victim.GetY() + fy

                            SetRotation(GetDegreeFromPosition(dx, dy))

                            if Goto(int(dx), int(dy)):
                                #sys_log(0, "KILL_AND_GO: %s distance %.1f", GetName(), fDist)
                                SendMovePacket(EMoveFuncType.FUNC_WAIT, 0, 0, 0, 0)
            return

        SetVictim(None)

        if IsGuardNPC():
            Return()

        m_dwStateDuration = ((1) * passes_per_sec)
        return

    if IsSummonMonster() and (not IsDead()) and not IsStun():
        if not GetParty():
            CPartyManager.instance().CreateParty(self)

        pParty = GetParty()
        bPct = not number(0, 3)

        if bPct and pParty.CountMemberByVnum(GetSummonVnum()) < SUMMON_MONSTER_COUNT:
            sx = GetX() - 300
            sy = GetY() - 300
            ex = GetX() + 300
            ey = GetY() + 300

            tch = CHARACTER_MANAGER.instance().SpawnMobRange(GetSummonVnum(), GetMapIndex(), sx, sy, ex, ey, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), ((not LGEMiscellaneous.DEFINECONSTANTS.false)), DefineConstants.false)

            if tch:
                pParty.Join(tch.GetVID())
                pParty.Link(tch)

    pkChrProtege = GetProtege()

    fDist = DISTANCE_APPROX(GetX() - victim.GetX(), GetY() - victim.GetY())

    if fDist >= 5000.0:
        SetVictim(None)

        if pkChrProtege:
            if DISTANCE_APPROX(GetX() - pkChrProtege.GetX(), GetY() - pkChrProtege.GetY()) > 1000:
                Follow(pkChrProtege, number(150, 400))

        return

    if fDist >= GetMobAttackRange() * 1.15:
        __CHARACTER_GotoNearTarget(self, victim)
        return

    if m_pkParty:
        m_pkParty.SendMessage(self, EPartyMessages.PM_ATTACKED_BY, 0, 0)

    if 2493 == m_pkMobData.m_table.dwVnum:
        m_dwStateDuration = BlueDragon_StateBattle(self)
        return

    dwCurTime = get_dword_time()
    dwDuration = uint(CalculateDuration(GetLimitPoint(EPointTypes.LG_POINT_ATT_SPEED), 2000))

    if (dwCurTime - m_dwLastAttackTime) < dwDuration:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        m_dwStateDuration = MAX(1, (passes_per_sec * (dwDuration - (dwCurTime - m_dwLastAttackTime)) / 1000))
        return

    if IsBerserker() == ((not LGEMiscellaneous.DEFINECONSTANTS.false)):
        if GetHPPct() < m_pkMobData.m_table.bBerserkPoint:
            if IsBerserk() != ((not LGEMiscellaneous.DEFINECONSTANTS.false)):
                SetBerserk(((not LGEMiscellaneous.DEFINECONSTANTS.false)))

    if IsGodSpeeder() == ((not LGEMiscellaneous.DEFINECONSTANTS.false)):
        if GetHPPct() < m_pkMobData.m_table.bGodSpeedPoint:
            if IsGodSpeed() != ((not LGEMiscellaneous.DEFINECONSTANTS.false)):
                SetGodSpeed(((not LGEMiscellaneous.DEFINECONSTANTS.false)))

    if HasMobSkill():
        iSkillIdx = 0
        while iSkillIdx < LGEMiscellaneous.MOB_LG_SKILL_MAX_NUM:
            if CanUseMobSkill(iSkillIdx):
                SetRotationToXY(victim.GetX(), victim.GetY())

                if UseMobSkill(iSkillIdx):
                    SendMovePacket(EMoveFuncType.FUNC_MOB_SKILL, iSkillIdx, GetX(), GetY(), 0, dwCurTime)

                    fDuration = CMotionManager.instance().GetMotionDuration(GetRaceNum(), uint((((EMotionMode.MOTION_MODE_GENERAL) << 24) | ((EPublicMotion.MOTION_SPECIAL_1 + iSkillIdx) << 8) | (0))))
                    m_dwStateDuration = (((2) * passes_per_sec) if fDuration == 0.0 else ((fDuration) * passes_per_sec))

                    if test_server:
                        #sys_log(0, "USE_MOB_SKILL: %s idx %u motion %u duration %.0f", GetName(), iSkillIdx, EPublicMotion.MOTION_SPECIAL_1 + iSkillIdx, fDuration)

                    return
            iSkillIdx += 1

    if not Attack(victim):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        m_dwStateDuration = passes_per_sec / 2
    else:
        SetRotationToXY(victim.GetX(), victim.GetY())
        SendMovePacket(EMoveFuncType.FUNC_ATTACK, 0, GetX(), GetY(), 0, dwCurTime)
        fDuration = CMotionManager.instance().GetMotionDuration(GetRaceNum(), uint((((EMotionMode.MOTION_MODE_GENERAL) << 24) | ((EPublicMotion.MOTION_NORMAL_ATTACK) << 8) | (0))))
        m_dwStateDuration = (((2) * passes_per_sec) if fDuration == 0.0 else ((fDuration) * passes_per_sec))

def StateFlag():
    m_dwStateDuration = ((0.5) * passes_per_sec)

    pMap = GetWarMap()

    if pMap is None:
        return

    f = FuncFindChrForFlag(self)
    GetSectree().ForEachAround(f.functor_method)

    if f.m_pkChrFind is None:
        return

    if None is f.m_pkChrFind.GetGuild():
        return

    buf = str(['\0' for _ in range(256)])
    idx = None

    temp_ref_idx = RefObject(idx);
    if not pMap.GetTeamIndex(uint(GetPoint(EPointTypes.LG_POINT_STAT)), temp_ref_idx):
        idx = temp_ref_idx.arg_value
        return
    else:
        idx = temp_ref_idx.arg_value

    f.m_pkChrFind.AddAffect(LaniatusEAffectTypes.LANIA_AFFECT_WAR_FLAG, EPointTypes.LG_POINT_NONE, GetPoint(EPointTypes.LG_POINT_STAT),EAffectBits.AFF_WAR_FLAG1 if idx == 0 else EAffectBits.AFF_WAR_FLAG2, AffectVariable.INFINITE_LANIA_AFFECT_DURATION, 0, LGEMiscellaneous.DEFINECONSTANTS.false, DefineConstants.false)
    f.m_pkChrFind.AddAffect(LaniatusEAffectTypes.LANIA_AFFECT_WAR_FLAG, EPointTypes.LG_POINT_MOV_SPEED, int(50 - f.m_pkChrFind.GetPoint(EPointTypes.LG_POINT_MOV_SPEED)), 0, AffectVariable.INFINITE_LANIA_AFFECT_DURATION, 0, LGEMiscellaneous.DEFINECONSTANTS.false, DefineConstants.false)

    pMap.RemoveFlag(idx)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    snprintf(buf, sizeof(buf), LC_TEXT("%s of the Guild was captured by %s."), pMap.GetGuild(idx).GetName(), f.m_pkChrFind.GetName(LOCALE_LANIATUS))
    pMap.Notice(buf)

def StateFlagBase():
    m_dwStateDuration = ((0.5) * passes_per_sec)

    f = FuncFindChrForFlagBase(self)
    GetSectree().ForEachAround(f.functor_method)

def StateHorse():
    START_FOLLOW_DISTANCE = 400.0
    START_RUN_DISTANCE = 400.0
    APPROACH = 300

    STATE_DURATION = uint(((0.25) * passes_per_sec))

    bDoMoveAlone = LGEMiscellaneous.DEFINECONSTANTS.false
    bRun = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    if IsDead():
        return

    m_dwStateDuration = STATE_DURATION
    victim = GetRider()

    if victim is None:
        CHARACTER_MANAGER.instance().DestroyCharacter(self)
        return

    m_pkMobInst.m_posLastAttacked = GetXYZ()

    fDist = DISTANCE_APPROX(GetX() - victim.GetX(), GetY() - victim.GetY())

    if fDist >= START_FOLLOW_DISTANCE:
        if fDist > START_RUN_DISTANCE:
            SetNowWalking((not bRun))

        Follow(victim, APPROACH)

        m_dwStateDuration = STATE_DURATION
    elif bDoMoveAlone and (get_dword_time() > m_dwLastAttackTime):
        m_dwLastAttackTime = get_dword_time() + number(5000, 12000)
        SetRotation(number(0, 359))
        fx = None
        fy = None
        fDist = number(200, 400)
        GetDeltaByDegree(GetRotation(), fDist, fx, fy)

        if not(SECTREE_MANAGER.instance().IsMovablePosition(GetMapIndex(), GetX() + int(fx), GetY() + int(fy)) and SECTREE_MANAGER.instance().IsMovablePosition(GetMapIndex(), GetX() + math.trunc(int(fx) / float(2)), GetY() + math.trunc(int(fy) / float(2)))):
            return

        SetNowWalking(((not LGEMiscellaneous.DEFINECONSTANTS.false)))

        if Goto(GetX() + int(fx), GetY() + int(fy)):
            SendMovePacket(EMoveFuncType.FUNC_WAIT, 0, 0, 0, 0)

