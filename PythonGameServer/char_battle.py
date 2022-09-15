from enum import Enum
import math

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: bool CHARACTER::CanBeginFight() const
def CanBeginFight():
    if not CanMove():
        return LGEMiscellaneous.DEFINECONSTANTS.false

    return m_pointsInstant.position == EPositions.POS_STANDING and (not IsDead()) and not IsStun()

def BeginFight(pkVictim):
    SetVictim(pkVictim)
    SetPosition(EPositions.POS_FIGHTING)
    SetNextStatePulse(1)

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: bool CHARACTER::CanFight() const
def CanFight():
    return ((not LGEMiscellaneous.DEFINECONSTANTS.false)) if m_pointsInstant.position >= EPositions.POS_FIGHTING else LGEMiscellaneous.DEFINECONSTANTS.false

def CreateFly(bType, pkVictim):
    packFly = packet_fly()

    packFly.bHeader = byte(LG_HEADER_GC_CREATE_FLY)
    packFly.bType = bType
    packFly.dwStartVID = GetVID()
    packFly.dwEndVID = pkVictim.GetVID()

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    PacketAround(packFly, sizeof(packet_fly))

def DistributeSP(pkKiller, iMethod):
    if pkKiller.GetSP() >= pkKiller.GetMaxSP():
        return

    bAttacking = (get_dword_time() - GetLastAttackTime()) < 3000
    bMoving = (get_dword_time() - GetLastMoveTime()) < 3000

    if iMethod == 1:
        num = number(0, 3)

        if num == 0:
            iLvDelta = GetLevel() - pkKiller.GetLevel()
            iAmount = 0

            if iLvDelta >= 5:
                iAmount = 10
            elif iLvDelta >= 0:
                iAmount = 6
            elif iLvDelta >= -3:
                iAmount = 2

            if iAmount != 0:
                iAmount += math.trunc((iAmount * pkKiller.GetPoint(EPointTypes.LG_POINT_SP_REGEN)) / float(100))

                if iAmount >= 11:
                    CreateFly(FLY_SP_BIG, pkKiller)
                elif iAmount >= 7:
                    CreateFly(FLY_SP_MEDIUM, pkKiller)
                else:
                    CreateFly(FLY_SP_SMALL, pkKiller)

                pkKiller.PointChange(EPointTypes.LG_POINT_SP, iAmount, DefineConstants.false, DefineConstants.false)
    else:
        if pkKiller.GetJob() == EJobs.JOB_LG_PAWN_MAGE or (pkKiller.GetJob() == EJobs.JOB_LG_PAWN_SHURA and pkKiller.GetSkillGroup() == 2):
            iAmount = None

            if bAttacking:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
                iAmount = 2 + GetMaxSP() / 100
            elif bMoving:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
                iAmount = 3 + GetMaxSP() * 2 / 100
            else:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
                iAmount = 10 + GetMaxSP() * 3 / 100

            iAmount += math.trunc((iAmount * pkKiller.GetPoint(EPointTypes.LG_POINT_SP_REGEN)) / float(100))
            pkKiller.PointChange(EPointTypes.LG_POINT_SP, iAmount, DefineConstants.false, DefineConstants.false)
        else:
            iAmount = None

            if bAttacking:
                iAmount = 2 + math.trunc(pkKiller.GetMaxSP() / float(200))
            elif bMoving:
                iAmount = 2 + math.trunc(pkKiller.GetMaxSP() / float(100))
            else:
                if pkKiller.GetHP() < pkKiller.GetMaxHP():
                    iAmount = 2 + (math.trunc(pkKiller.GetMaxSP() / float(100)))
                else:
                    iAmount = 9 + (math.trunc(pkKiller.GetMaxSP() / float(100)))

            iAmount += math.trunc((iAmount * pkKiller.GetPoint(EPointTypes.LG_POINT_SP_REGEN)) / float(100))
            pkKiller.PointChange(EPointTypes.LG_POINT_SP, iAmount, DefineConstants.false, DefineConstants.false)


def Attack(pkVictim, bType):
    if test_server:
        #sys_log(0, "[TEST_SERVER] Attack : %s type %d, MobBattleType %d", GetName(), bType,0 if (not GetMobBattleType()) else GetMobAttackRange())

    if not CanMove():
        return LGEMiscellaneous.DEFINECONSTANTS.false

    if not battle_is_attackable(self, pkVictim):
        return LGEMiscellaneous.DEFINECONSTANTS.false

    dwCurrentTime = get_dword_time()

    if IsPC():
        if IS_SPEED_HACK(self, pkVictim, dwCurrentTime):
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if bType == 0 and dwCurrentTime < GetSkipComboAttackByTime():
            return LGEMiscellaneous.DEFINECONSTANTS.false

    pkVictim.SetSyncOwner(self, ((not DefineConstants.false)))

    if pkVictim.CanBeginFight():
        pkVictim.BeginFight(self)

    iRet = None

    if bType == 0:
        if (GetMobBattleType() == EBattleType.BATTLE_TYPE_MELEE) or (GetMobBattleType() == EBattleType.BATTLE_TYPE_POWER) or (GetMobBattleType() == EBattleType.BATTLE_TYPE_TANKER) or (GetMobBattleType() == EBattleType.BATTLE_TYPE_SUPER_POWER) or (GetMobBattleType() == EBattleType.BATTLE_TYPE_SUPER_TANKER):
            iRet = battle_melee_attack(self, pkVictim)

        elif GetMobBattleType() == EBattleType.BATTLE_TYPE_RANGE:
            FlyTarget(pkVictim.GetVID(), pkVictim.GetX(), pkVictim.GetY(), LG_HEADER_CG_FLY_TARGETING)
            iRet = EBattleTypes.BATTLE_DAMAGE if Shoot(0) else EBattleTypes.BATTLE_NONE

        elif GetMobBattleType() == EBattleType.BATTLE_TYPE_MAGIC:
            FlyTarget(pkVictim.GetVID(), pkVictim.GetX(), pkVictim.GetY(), LG_HEADER_CG_FLY_TARGETING)
            iRet = EBattleTypes.BATTLE_DAMAGE if Shoot(1) else EBattleTypes.BATTLE_NONE

        else:
            #lani_err("Unhandled battle type %d", GetMobBattleType())
            iRet = EBattleTypes.BATTLE_NONE
    else:
        if IsPC() == ((not LGEMiscellaneous.DEFINECONSTANTS.false)):
            if dwCurrentTime - m_dwLastSkillTime > 1500:
                #sys_log(1, "HACK: Too long skill using term. Name(%s) PID(%u) delta(%u)", GetName(), GetPlayerID(), (dwCurrentTime - m_dwLastSkillTime))
                return LGEMiscellaneous.DEFINECONSTANTS.false

        #sys_log(1, "Attack call ComputeSkill %d %s", bType,pkVictim.GetName(LOCALE_LANIATUS) if pkVictim is not None ) else "")
        iRet = ComputeSkill(bType, pkVictim)

    if iRet == EBattleTypes.BATTLE_DAMAGE or iRet == EBattleTypes.BATTLE_DEAD:
        OnMove(((not LGEMiscellaneous.DEFINECONSTANTS.false)))
        pkVictim.OnMove(DefineConstants.false)

        if EBattleTypes.BATTLE_DEAD == iRet and IsPC():
            SetVictim(None)

        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    return LGEMiscellaneous.DEFINECONSTANTS.false

def DeathPenalty(bTown):
    #sys_log(1, "DEATH_PERNALY_CHECK(%s) town(%d)", GetName(), bTown)

    Cube_close(self)
    AcceClose()

    if GetLevel() < 10:
        #sys_log(0, "NO_DEATH_PENALTY_LESS_LV10(%s)", GetName())
        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You did not lose any Experience because of the Blessing of the Dragon God."))
        return

    if number(0, 2):
        #sys_log(0, "NO_DEATH_PENALTY_LUCK(%s)", GetName())
        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You did not lose any Experience because of the Blessing of the Dragon God."))
        return

    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'IS_SET' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
    if IS_SET(m_pointsInstant.instant_flag, (1 << 0)):
        ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'REMOVE_BIT' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
        REMOVE_BIT(m_pointsInstant.instant_flag, (1 << 0))

        if bTown == 0:
            if FindAffect(LaniatusEAffectTypes.LANIA_AFFECT_NO_DEATH_PENALTY):
                #sys_log(0, "NO_DEATH_PENALTY_AFFECT(%s)", GetName())
                ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You did not lose any Experience because of the Blessing of the Dragon God."))
                RemoveAffect(LaniatusEAffectTypes.LANIA_AFFECT_NO_DEATH_PENALTY)
                return

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        iLoss = ((GetNextExp() * aiExpLossPercents[MINMAX(1, GetLevel(), LGEMiscellaneous.PLAYER_EXP_TABLE_MAX)]) / 100)
        iLoss = MIN(800000, iLoss)

        if bTown != 0:
            iLoss = 0

        if IsEquipUniqueItem(UNIQUE_ITEM_TEARDROP_OF_GODNESS):
            iLoss = math.trunc(iLoss / float(2))

        #sys_log(0, "DEATH_PENALTY(%s) EXP_LOSS: %d percent %d%%", GetName(), iLoss, aiExpLossPercents[MIN(gPlayerMaxLevel, GetLevel())])

        PointChange(EPointTypes.LG_POINT_EXP, -iLoss, ((not LGEMiscellaneous.DEFINECONSTANTS.false)))

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: bool CHARACTER::IsStun() const
def IsStun():
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'IS_SET' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
    if IS_SET(m_pointsInstant.instant_flag, (1 << 3)):
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    return LGEMiscellaneous.DEFINECONSTANTS.false

def Stun():
    if IsStun():
        return

    if IsDead():
        return

    if (not IsPC()) and m_pkParty:
        m_pkParty.SendMessage(self, EPartyMessages.PM_ATTACKED_BY, 0, 0)

    #sys_log(1, "%s: Stun %p", GetName(), self)

    PointChange(EPointTypes.LG_POINT_HP_RECOVERY, -GetPoint(EPointTypes.LG_POINT_HP_RECOVERY))
    PointChange(EPointTypes.LG_POINT_SP_RECOVERY, -GetPoint(EPointTypes.LG_POINT_SP_RECOVERY))

    CloseMyShop()

    event_cancel(m_pkRecoveryEvent)

    pack = packet_stun()
    pack.header = byte(LG_HEADER_GC_STUN)
    pack.vid = m_vid
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    PacketAround(pack, sizeof(pack))

    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'SET_BIT' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
    SET_BIT(m_pointsInstant.instant_flag, (1 << 3))

    if m_pkStunEvent:
        return

    info = AllocEventInfo()

    info.ch = self

    m_pkStunEvent = event_create_ex(StunEvent, info, ((3) * passes_per_sec))

class SCharDeadEventInfo(event_info_data):

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.isPC = False
        self.dwID = 0

        self.isPC = False
        self.dwID = 0

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: bool CHARACTER::IsDead() const
def IsDead():
    if m_pointsInstant.position == EPositions.POS_DEAD:
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    return LGEMiscellaneous.DEFINECONSTANTS.false

## Laniatus Games Studio Inc. | NOTE: The following #define macro was replaced in-line:
#ORIGINAL METINII C CODE: #define GetGoldMultipler() 1

def RewardGold(pkAttacker):
    isAutoLoot = ((not LGEMiscellaneous.DEFINECONSTANTS.false)) if (pkAttacker.GetPremiumRemainSeconds(EPremiumTypes.PREMIUM_AUTOLOOT) > 0 or pkAttacker.IsEquipUniqueGroup(uint(UNIQUE_GROUP_AUTOLOOT))) else LGEMiscellaneous.DEFINECONSTANTS.false

    pos = pixel_position_s()

    if not isAutoLoot:
        if not SECTREE_MANAGER.instance().GetMovablePosition(GetMapIndex(), GetX(), GetY(), pos):
            return

    iTotalGold = 0

    iGoldPercent = MobRankStats[GetMobRank()].iGoldPercent

    if pkAttacker.IsPC():
        iGoldPercent = math.trunc(iGoldPercent * (100 + CPrivManager.instance().GetPriv(pkAttacker, EPrivType.PRIV_GOLD_DROP)) / float(100))

    if pkAttacker.GetPoint(EPointTypes.LG_POINT_MALL_GOLDBONUS) != 0:
        iGoldPercent += (math.trunc(iGoldPercent * pkAttacker.GetPoint(EPointTypes.LG_POINT_MALL_GOLDBONUS) / float(100)))

    iGoldPercent = math.trunc(iGoldPercent * CHARACTER_MANAGER.instance().GetMobGoldDropRate(pkAttacker) / float(100))

    if pkAttacker.GetPremiumRemainSeconds(EPremiumTypes.PREMIUM_GOLD) > 0 or pkAttacker.IsEquipUniqueGroup(uint(UNIQUE_GROUP_LUCKY_GOLD)):
        iGoldPercent += iGoldPercent

    if iGoldPercent > 100:
        iGoldPercent = 100

    iPercent = None

    if GetMobRank() >= EMobRank.MOB_RANK_BOSS:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        iPercent = ((iGoldPercent * aiPercentByDeltaLevForBoss[MINMAX(0, (GetLevel() + 15) - pkAttacker.GetLevel(), LGEMiscellaneous.DEFINECONSTANTS.MAX_EXP_DELTA_OF_LEV - 1)]) / 100)
    else:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        iPercent = ((iGoldPercent * aiPercentByDeltaLev[MINMAX(0, (GetLevel() + 15) - pkAttacker.GetLevel(), LGEMiscellaneous.DEFINECONSTANTS.MAX_EXP_DELTA_OF_LEV - 1)]) / 100)

    if number(1, 100) > iPercent:
        return

    iGoldMultipler = 1

    if 1 == number(1, 50000):
        iGoldMultipler *= 10
    elif 1 == number(1, 10000):
        iGoldMultipler *= 5

    if pkAttacker.GetPoint(EPointTypes.LG_POINT_GOLD_DOUBLE_BONUS) != 0:
        if number(1, 100) <= pkAttacker.GetPoint(EPointTypes.LG_POINT_GOLD_DOUBLE_BONUS):
            iGoldMultipler *= 2

    if test_server:
        pkAttacker.ChatPacket(EChatType.CHAT_TYPE_PARTY, "gold_mul %d rate %d", iGoldMultipler, CHARACTER_MANAGER.instance().GetMobGoldAmountRate(pkAttacker))

    item = None

    iGold10DropPct = 100
    iGold10DropPct = math.trunc((iGold10DropPct * 100) / float(100 + CPrivManager.instance().GetPriv(pkAttacker, EPrivType.PRIV_GOLD10_DROP)))

    if GetMobRank() >= EMobRank.MOB_RANK_BOSS and (not IsStone()) and GetMobTable().dwGoldMax != 0:
        if 1 == number(1, iGold10DropPct):
            iGoldMultipler *= 10

        iSplitCount = number(25, 35)

        for i in range(0, iSplitCount):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
            iGold = number(GetMobTable().dwGoldMin, GetMobTable().dwGoldMax) / iSplitCount
            if test_server:
                #sys_log(0, "iGold %d", iGold)
            iGold = math.trunc(iGold * CHARACTER_MANAGER.instance().GetMobGoldAmountRate(pkAttacker) / float(100))
            iGold *= iGoldMultipler

            if iGold == 0:
                continue

            if test_server:
                #sys_log(0, "Drop Moeny MobGoldAmountRate %d %d", CHARACTER_MANAGER.instance().GetMobGoldAmountRate(pkAttacker), iGoldMultipler)
                #sys_log(0, "Drop Money gold %d GoldMin %d GoldMax %d", iGold, GetMobTable().dwGoldMax, GetMobTable().dwGoldMax)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((item = ITEM_MANAGER::instance().CreateItem(1, iGold)))
            if (item = ITEM_MANAGER.instance().CreateItem(1, uint(iGold), 0, DefineConstants.false, -1, DefineConstants.false)):
                pos.x = GetX() + ((number(-14, 14) + number(-14, 14)) * 23)
                pos.y = GetY() + ((number(-14, 14) + number(-14, 14)) * 23)

                item.AddToGround(GetMapIndex(), pos, DefineConstants.false)
                item.StartDestroyEvent(300)

                iTotalGold += iGold
    elif 1 == number(1, iGold10DropPct):
        for i in range(0, 10):
            iGold = number(GetMobTable().dwGoldMin, GetMobTable().dwGoldMax)
            iGold = math.trunc(iGold * CHARACTER_MANAGER.instance().GetMobGoldAmountRate(pkAttacker) / float(100))
            iGold *= iGoldMultipler

            if iGold == 0:
                continue

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((item = ITEM_MANAGER::instance().CreateItem(1, iGold)))
            if (item = ITEM_MANAGER.instance().CreateItem(1, uint(iGold), 0, DefineConstants.false, -1, DefineConstants.false)):
                pos.x = GetX() + (number(-7, 7) * 20)
                pos.y = GetY() + (number(-7, 7) * 20)

                item.AddToGround(GetMapIndex(), pos, DefineConstants.false)
                item.StartDestroyEvent(300)

                iTotalGold += iGold
    else:
        iGold = number(GetMobTable().dwGoldMin, GetMobTable().dwGoldMax)
        iGold = math.trunc(iGold * CHARACTER_MANAGER.instance().GetMobGoldAmountRate(pkAttacker) / float(100))
        iGold *= iGoldMultipler

        iSplitCount = None

        if iGold >= 3:
            iSplitCount = number(1, 3)
        elif GetMobRank() >= EMobRank.MOB_RANK_BOSS:
            iSplitCount = number(3, 10)

            if (math.trunc(iGold / float(iSplitCount))) == 0:
                iSplitCount = 1
        else:
            iSplitCount = 1

        if iGold != 0:
            iTotalGold += iGold

            for i in range(0, iSplitCount):
                if isAutoLoot:
                    pkAttacker.GiveGold(math.trunc(iGold / float(iSplitCount)))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: else if ((item = ITEM_MANAGER::instance().CreateItem(1, iGold / iSplitCount)))
                elif (item = ITEM_MANAGER.instance().CreateItem(1, math.trunc(iGold / float(iSplitCount)), 0, DefineConstants.false, -1, DefineConstants.false)):
                    pos.x = GetX() + (number(-7, 7) * 20)
                    pos.y = GetY() + (number(-7, 7) * 20)

                    item.AddToGround(GetMapIndex(), pos, DefineConstants.false)
                    item.StartDestroyEvent(300)

def Reward(bItemDrop):
    if GetRaceNum() == 5001:
        pos = pixel_position_s()

        if not SECTREE_MANAGER.instance().GetMovablePosition(GetMapIndex(), GetX(), GetY(), pos):
            return

        item = None
        iGold = number(GetMobTable().dwGoldMin, GetMobTable().dwGoldMax)
        iGold = math.trunc(iGold * CHARACTER_MANAGER.instance().GetMobGoldAmountRate(None) / float(100))
        iGold *= 1
        iSplitCount = number(25, 35)

        #sys_log(0, "WAEGU Dead gold %d split %d", iGold, iSplitCount)

        for i in range(1, iSplitCount + 1):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((item = ITEM_MANAGER::instance().CreateItem(1, iGold / iSplitCount)))
            if (item = ITEM_MANAGER.instance().CreateItem(1, math.trunc(iGold / float(iSplitCount)), 0, DefineConstants.false, -1, DefineConstants.false)):
                if i != 0:
                    pos.x = number(-7, 7) * 20
                    pos.y = number(-7, 7) * 20

                    pos.x += GetX()
                    pos.y += GetY()

                item.AddToGround(GetMapIndex(), pos, DefineConstants.false)
                item.StartDestroyEvent(300)
        return

    pkAttacker = DistributeExp()

    if pkAttacker is None:
        return

    if pkAttacker.IsPC():
        if GetLevel() - pkAttacker.GetLevel() >= -10:
            if pkAttacker.GetRealAlignment() < 0:
                if pkAttacker.IsEquipUniqueItem(uint(UNIQUE_ITEM_FASTER_ALIGNMENT_UP_BY_KILL)):
                    pkAttacker.UpdateAlignment(14)
                else:
                    pkAttacker.UpdateAlignment(7)
            else:
                pkAttacker.UpdateAlignment(2)

        pkAttacker.SetQuestNPCID(GetVID())
        quest.CQuestManager.instance().Kill(pkAttacker.GetPlayerID(), GetRaceNum())
        CHARACTER_MANAGER.instance().KillLog(GetRaceNum())

        if not number(0, 9):
            if pkAttacker.GetPoint(EPointTypes.LG_POINT_KILL_HP_RECOVERY) != 0:
                iHP = math.trunc(pkAttacker.GetMaxHP() * pkAttacker.GetPoint(EPointTypes.LG_POINT_KILL_HP_RECOVERY) / float(100))
                pkAttacker.PointChange(EPointTypes.LG_POINT_HP, iHP, DefineConstants.false, DefineConstants.false)
                CreateFly(FLY_HP_SMALL, pkAttacker)

            if pkAttacker.GetPoint(EPointTypes.LG_POINT_KILL_SP_RECOVER) != 0:
                iSP = math.trunc(pkAttacker.GetMaxSP() * pkAttacker.GetPoint(EPointTypes.LG_POINT_KILL_SP_RECOVER) / float(100))
                pkAttacker.PointChange(EPointTypes.LG_POINT_SP, iSP, DefineConstants.false, DefineConstants.false)
                CreateFly(FLY_SP_SMALL, pkAttacker)

    if not bItemDrop:
        return

    pos = GetXYZ()

    if not SECTREE_MANAGER.instance().GetMovablePosition(GetMapIndex(), pos.x, pos.y, pos):
        return

    if test_server:
        #sys_log(0, "Drop money : Attacker %s", pkAttacker.GetName(LOCALE_LANIATUS))
    RewardGold(pkAttacker)
    item = None

    ## Laniatus Games Studio Inc. | NOTE: This static local variable declaration (not allowed in Python) has been moved just prior to the method:
    #    static list<CItem*> s_vec_item
    Reward_s_vec_item.clear()

    if ITEM_MANAGER.instance().CreateDropItem(self, pkAttacker, Reward_s_vec_item):
        if Reward_s_vec_item.size() == 0:
            pass
        elif Reward_s_vec_item.size() == 1:
            item = Reward_s_vec_item[0]
            item.AddToGround(GetMapIndex(), pos, DefineConstants.false)
            item.SetOwnership(pkAttacker, 10)
            item.StartDestroyEvent(300)

            pos.x = number(-7, 7) * 20
            pos.y = number(-7, 7) * 20
            pos.x += GetX()
            pos.y += GetY()

            #sys_log(0, "DROP_ITEM: %s %d %d from %s", item.GetName(LOCALE_LANIATUS), pos.x, pos.y, GetName())
        else:
            iItemIdx = Reward_s_vec_item.size() - 1

            pq = std::priority_queue()

            total_dam = 0

            it = m_map_kDamage.begin()
            while it is not m_map_kDamage.end():
                iDamage = it.second.iTotalDamage
                if iDamage > 0:
                    ch = CHARACTER_MANAGER.instance().Find(it.first)

                    if ch:
                        pq.push((iDamage, ch))
                        total_dam += iDamage
                it += 1

            v = []

            while (not pq.empty()) and pq.top().first * 10 >= total_dam:
                v.append(pq.top().second)
                pq.pop()

            if not v:
                while iItemIdx >= 0:
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: item = s_vec_item[iItemIdx--];
                    item = Reward_s_vec_item[iItemIdx]
                    iItemIdx -= 1

                    if item is None:
                        #lani_err("item null in vector idx %d", iItemIdx + 1)
                        continue

                    item.AddToGround(GetMapIndex(), pos, DefineConstants.false)
                    item.StartDestroyEvent(300)

                    pos.x = number(-7, 7) * 20
                    pos.y = number(-7, 7) * 20
                    pos.x += GetX()
                    pos.y += GetY()

                    #sys_log(0, "DROP_ITEM: %s %d %d by %s", item.GetName(LOCALE_LANIATUS), pos.x, pos.y, GetName())
            else:
                it = v.begin()

                while iItemIdx >= 0:
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: item = s_vec_item[iItemIdx--];
                    item = Reward_s_vec_item[iItemIdx]
                    iItemIdx -= 1

                    if item is None:
                        #lani_err("item null in vector idx %d", iItemIdx + 1)
                        continue

                    item.AddToGround(GetMapIndex(), pos, DefineConstants.false)

                    ch = *it

                    it += 1

                    if it is v.end():
## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: it = v.begin();
                        it.copy_from(v.begin())

                    item.SetOwnership(ch, 10)
                    item.StartDestroyEvent(300)

                    pos.x = number(-7, 7) * 20
                    pos.y = number(-7, 7) * 20
                    pos.x += GetX()
                    pos.y += GetY()

                    #sys_log(0, "DROP_ITEM: %s %d %d by %s", item.GetName(LOCALE_LANIATUS), pos.x, pos.y, GetName())

    m_map_kDamage.clear()

class TItemDropPenalty:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.iInventoryPct = 0
        self.iInventoryQty = 0
        self.iEquipmentPct = 0
        self.iEquipmentQty = 0


def ItemDropPenalty(pkKiller):
    if GetMyShop():
        return

    if GetLevel() < 50:
        return

    table = aItemDropPenalty_kor[0]

    if GetLevel() < 10:
        return

    iAlignIndex = None

    if GetRealAlignment() >= 120000:
        iAlignIndex = 0
    elif GetRealAlignment() >= 80000:
        iAlignIndex = 1
    elif GetRealAlignment() >= 40000:
        iAlignIndex = 2
    elif GetRealAlignment() >= 10000:
        iAlignIndex = 3
    elif GetRealAlignment() >= 0:
        iAlignIndex = 4
    elif GetRealAlignment() > -40000:
        iAlignIndex = 5
    elif GetRealAlignment() > -80000:
        iAlignIndex = 6
    elif GetRealAlignment() > -120000:
        iAlignIndex = 7
    else:
        iAlignIndex = 8

    vec_item = []
    pkItem = None
    i = None
    isDropAllEquipments = LGEMiscellaneous.DEFINECONSTANTS.false

    r = table[iAlignIndex]
    #sys_log(0, "%s align %d inven_pct %d equip_pct %d", GetName(), iAlignIndex, r.iInventoryPct, r.iEquipmentPct)

    bDropInventory = r.iInventoryPct >= number(1, 1000)
    bDropEquipment = r.iEquipmentPct >= number(1, 100)
    bDropAntiDropUniqueItem = LGEMiscellaneous.DEFINECONSTANTS.false

    if (bDropInventory or bDropEquipment) and IsEquipUniqueItem(UNIQUE_ITEM_SKIP_ITEM_DROP_PENALTY):
        bDropInventory = LGEMiscellaneous.DEFINECONSTANTS.false
        bDropEquipment = LGEMiscellaneous.DEFINECONSTANTS.false
        bDropAntiDropUniqueItem = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    if bDropInventory:
        vec_bSlots = []

        i = 0
        while i < LGEMiscellaneous.INVENTORY_MAX_NUM:
            if GetInventoryItem(i):
                vec_bSlots.append(byte(i))
            i += 1

        if vec_bSlots:
            rd = std::random_device()
            g = std::mt19937(rd())
            std::shuffle(vec_bSlots.begin(), vec_bSlots.end(), g)

            iQty = MIN(len(vec_bSlots), r.iInventoryQty)

            if iQty != 0:
                iQty = number(1, iQty)

            for i in range(0, iQty):
                pkItem = GetInventoryItem(vec_bSlots[i])

                ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'IS_SET' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
                if IS_SET(pkItem.GetAntiFlag(), LaniatusEITMAntiFlagDcs.ITEM_ANTIFLAG_GIVE | LaniatusEITMAntiFlagDcs.ITEM_ANTIFLAG_PKDROP):
                    continue

                SyncQuickslot(LG_QUICKSLOT_TYPE_ITEM, vec_bSlots[i], 255)
                vec_item.append((pkItem.RemoveFromCharacter(), EWindows.INVENTORY))
        elif iAlignIndex == 8:
            isDropAllEquipments = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    if bDropEquipment:
        vec_bSlots = []

        i = 0
        while i < EWearPositions.WEAR_MAX_NUM:
            if GetWear(i):
                vec_bSlots.append(byte(i))
            i += 1

        if vec_bSlots:
            rd = std::random_device()
            g = std::mt19937(rd())
            std::shuffle(vec_bSlots.begin(), vec_bSlots.end(), g)
            iQty = None

            if isDropAllEquipments:
                iQty = len(vec_bSlots)
            else:
                iQty = MIN(len(vec_bSlots), number(1, r.iEquipmentQty))

            if iQty != 0:
                iQty = number(1, iQty)

            for i in range(0, iQty):
                pkItem = GetWear(vec_bSlots[i])

                ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'IS_SET' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
                if IS_SET(pkItem.GetAntiFlag(), LaniatusEITMAntiFlagDcs.ITEM_ANTIFLAG_GIVE | LaniatusEITMAntiFlagDcs.ITEM_ANTIFLAG_PKDROP):
                    continue

                SyncQuickslot(LG_QUICKSLOT_TYPE_ITEM, vec_bSlots[i], 255)
                vec_item.append((pkItem.RemoveFromCharacter(), EWindows.EQUIPMENT))

    if bDropAntiDropUniqueItem:
        pkItem = None

        pkItem = GetWear(EWearPositions.WEAR_UNIQUE1)

        if pkItem is not None and pkItem.GetVnum() == UNIQUE_ITEM_SKIP_ITEM_DROP_PENALTY:
            SyncQuickslot(LG_QUICKSLOT_TYPE_ITEM, EWearPositions.WEAR_UNIQUE1, 255)
            vec_item.append((pkItem.RemoveFromCharacter(), EWindows.EQUIPMENT))

        pkItem = GetWear(EWearPositions.WEAR_UNIQUE2)

        if pkItem is not None and pkItem.GetVnum() == UNIQUE_ITEM_SKIP_ITEM_DROP_PENALTY:
            SyncQuickslot(LG_QUICKSLOT_TYPE_ITEM, EWearPositions.WEAR_UNIQUE2, 255)
            vec_item.append((pkItem.RemoveFromCharacter(), EWindows.EQUIPMENT))

        pos = pixel_position_s()
        pos.x = GetX()
        pos.y = GetY()

        i = None

        i = 0
        while i < len(vec_item):
            item = vec_item[i][0]
            window = vec_item[i][1]

            item.AddToGround(GetMapIndex(), pos, DefineConstants.false)
            item.StartDestroyEvent(300)

            #sys_log(0, "DROP_ITEM_PK: %s %d %d from %s", item.GetName(LOCALE_LANIATUS), pos.x, pos.y, GetName())

            pos.x = GetX() + number(-7, 7) * 20
            pos.y = GetY() + number(-7, 7) * 20
            i += 1

class FPartyAlignmentCompute:
    def __init__(self, iAmount, x, y):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.m_iAmount = 0
        self.m_iCount = 0
        self.m_iStep = 0
        self.m_iKillerX = 0
        self.m_iKillerY = 0

        self.m_iAmount = iAmount
        self.m_iCount = 0
        self.m_iStep = 0
        self.m_iKillerX = x
        self.m_iKillerY = y

    def functor_method(self, pkChr):
        if Globals.DISTANCE_APPROX(pkChr.GetX() - self.m_iKillerX, pkChr.GetY() - self.m_iKillerY) < Globals.PARTY_DEFAULT_RANGE:
            if self.m_iStep == 0:
                self.m_iCount += 1
            else:
                pkChr.UpdateAlignment(math.trunc(self.m_iAmount / float(self.m_iCount)))





def Dead(pkKiller, bImmediateDead):
    if IsDead():
        return

        if IsHorseRiding():
            StopRiding()
        elif GetMountVnum():
            RemoveAffect(LaniatusEAffectTypes.LANIA_AFFECT_MOUNT_BONUS)
            m_dwMountVnum = 0
            UnEquipSpecialRideUniqueItem()

            UpdatePacket()

    isAgreedPVP = LGEMiscellaneous.DEFINECONSTANTS.false
    isUnderGuildWar = LGEMiscellaneous.DEFINECONSTANTS.false

    if pkKiller is not None and pkKiller.IsPC():
        if pkKiller.m_pkChrTarget is self:
            pkKiller.SetTarget(None)

        if (not IsPC()) and pkKiller.GetDungeon():
            pkKiller.GetDungeon().IncKillCount(pkKiller, self)

        isAgreedPVP = CPVPManager.instance().Dead(self, pkKiller.GetPlayerID())

        if IsPC():
            g1 = GetGuild()
            g2 = pkKiller.GetGuild()

            if g1 is not None and g2 is not None:
                if g1.UnderWar(g2.GetID()):
                    isUnderGuildWar = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

            pkKiller.SetQuestNPCID(GetVID())
            quest.CQuestManager.instance().Kill(pkKiller.GetPlayerID(), uint(quest.QUEST_NO_NPC))
            CGuildManager.instance().Kill(pkKiller, self)

    if pkKiller is not None and (not isAgreedPVP) and (not isUnderGuildWar) and IsPC():
        if GetGMLevel() == EGMLevels.GM_PLAYER or test_server:
            ItemDropPenalty(pkKiller)

    SetPosition(EPositions.POS_DEAD)
    ClearAffect(((not LGEMiscellaneous.DEFINECONSTANTS.false)))

    if pkKiller is not None and IsPC():
        if not pkKiller.IsPC():
            #sys_log(1, "DEAD: %s %p WITH PENALTY", GetName(), self)
            ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'SET_BIT' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
            SET_BIT(m_pointsInstant.instant_flag, (1 << 0))
        else:
            #sys_log(1, "DEAD_BY_PC: %s %p KILLER %s %p", GetName(), self, pkKiller.GetName(LOCALE_LANIATUS), get_pointer(pkKiller))
            ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'REMOVE_BIT' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
            REMOVE_BIT(m_pointsInstant.instant_flag, (1 << 0))

            if GetEmpire() != pkKiller.GetEmpire():
                iEP = MIN(GetPoint(EPointTypes.LG_POINT_EMPIRE_POINT), pkKiller.GetPoint(EPointTypes.LG_POINT_EMPIRE_POINT))

                PointChange(EPointTypes.LG_POINT_EMPIRE_POINT, -(math.trunc(iEP / float(10))))
                pkKiller.PointChange(EPointTypes.LG_POINT_EMPIRE_POINT, math.trunc(iEP / float(5)), DefineConstants.false, DefineConstants.false)

                if GetPoint(EPointTypes.LG_POINT_EMPIRE_POINT) < 10:
                    pass
            else:
                if (not isAgreedPVP) and (not isUnderGuildWar) and (not IsKillerMode()) and GetAlignment() >= 0:
                    iNoPenaltyProb = 0

                    if pkKiller.GetAlignment() >= 0:
                        iNoPenaltyProb = 33
                    else:
                        iNoPenaltyProb = 20

                    if number(1, 100) < iNoPenaltyProb:
                        pkKiller.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You did not drop any Item as you are protected by the Dragon God."))
                    else:
                        if pkKiller.GetParty():
                            f = FPartyAlignmentCompute(-20000, pkKiller.GetX(), pkKiller.GetY())
                            pkKiller.GetParty().ForEachOnlineMember(f.functor_method)

                            if f.m_iCount == 0:
                                pkKiller.UpdateAlignment(-20000)
                            else:
                                #sys_log(0, "ALIGNMENT PARTY count %d amount %d", f.m_iCount, f.m_iAmount)

                                f.m_iStep = 1
                                pkKiller.GetParty().ForEachOnlineMember(f.functor_method)
                        else:
                            pkKiller.UpdateAlignment(-20000)
    else:
        #sys_log(1, "DEAD: %s %p", GetName(), self)
        ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'REMOVE_BIT' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
        REMOVE_BIT(m_pointsInstant.instant_flag, (1 << 0))

    ClearSync()

    event_cancel(m_pkStunEvent)

    if IsPC():
        m_dwLastDeadTime = get_dword_time()
        SetKillerMode(LGEMiscellaneous.DEFINECONSTANTS.false)
        GetDesc().SetPhase(EPhase.PHASE_DEAD)
    else:
        ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'IS_SET' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
        if not IS_SET(m_pointsInstant.instant_flag, (1 << 4)):
            if not(pkKiller is not None and pkKiller.IsPC() and pkKiller.GetGuild() is not None and (pkKiller.GetGuild().UnderAnyWar(EGuildWarType.GUILD_WAR_TYPE_FIELD)) != 0):
                if GetMobTable().dwResurrectionVnum:
                    chResurrect = CHARACTER_MANAGER.instance().SpawnMob(GetMobTable().dwResurrectionVnum, GetMapIndex(), GetX(), GetY(), GetZ(), ((not LGEMiscellaneous.DEFINECONSTANTS.false)), int(GetRotation()), ((not DefineConstants.false)))
                    if GetDungeon() and chResurrect:
                        chResurrect.SetDungeon(GetDungeon())

                    Reward(LGEMiscellaneous.DEFINECONSTANTS.false)
                elif IsRevive() == ((not LGEMiscellaneous.DEFINECONSTANTS.false)):
                    Reward(LGEMiscellaneous.DEFINECONSTANTS.false)
                else:
                    Reward(((not LGEMiscellaneous.DEFINECONSTANTS.false)))
            else:
                if pkKiller.m_dwUnderGuildWarInfoMessageTime < get_dword_time():
                    pkKiller.m_dwUnderGuildWarInfoMessageTime = get_dword_time() + 60000
                    pkKiller.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> Guild Skills only affect players in war."))

    pack = packet_dead()
    pack.header = byte(LG_HEADER_GC_DEAD)
    pack.vid = m_vid
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    PacketAround(pack, sizeof(pack))

    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'REMOVE_BIT' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
    REMOVE_BIT(m_pointsInstant.instant_flag, (1 << 3))

    if GetDesc() is not None:
        it = m_list_pkAffect.begin()

        while it is not m_list_pkAffect.end():
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: SendAffectAddPacket(GetDesc(), *it++);
            SendAffectAddPacket(GetDesc(), it)
            it += 1

    if m_pkDeadEvent:
        #sys_log(1, "DEAD_EVENT_CANCEL: %s %p %p", GetName(), self, get_pointer(m_pkDeadEvent))
        event_cancel(m_pkDeadEvent)

    if IsStone():
        ClearStone()

    if GetDungeon():
        GetDungeon().DeadCharacter(self)

    pEventInfo = AllocEventInfo()

    if IsPC():
        pEventInfo.isPC = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
        pEventInfo.dwID = self.GetPlayerID()

        m_pkDeadEvent = event_create_ex(dead_event, pEventInfo, ((180) * passes_per_sec))
    else:
        pEventInfo.isPC = LGEMiscellaneous.DEFINECONSTANTS.false
        pEventInfo.dwID = self.GetVID()

        if IsRevive() == LGEMiscellaneous.DEFINECONSTANTS.false and HasReviverInParty() == ((not LGEMiscellaneous.DEFINECONSTANTS.false)):
            m_pkDeadEvent = event_create_ex(dead_event, pEventInfo,1 if bImmediateDead else ((3) * passes_per_sec))
        else:
            m_pkDeadEvent = event_create_ex(dead_event, pEventInfo,1 if bImmediateDead else ((1) * passes_per_sec))

    #sys_log(1, "DEAD_EVENT_CREATE: %s %p %p", GetName(), self, get_pointer(m_pkDeadEvent))

    if m_pkExchange is not None:
        m_pkExchange.Cancel()

    if IsCubeOpen() == ((not LGEMiscellaneous.DEFINECONSTANTS.false)):
        Cube_close(self)

    if IsAcceWindowOpen():
        AcceClose()

    CShopManager.instance().StopShopping(self)
    CloseMyShop()
    CloseSafebox()

    if ((not LGEMiscellaneous.DEFINECONSTANTS.false)) == IsMonster() and 2493 == GetMobTable().dwVnum:
        if None is not pkKiller and None is not pkKiller.GetGuild():
            CDragonLairManager.instance().OnDragonDead(self, pkKiller.GetGuild().GetID())
        else:
            #lani_err("DragonLair: Dragon killed by nobody")

class FuncSetLastAttacked:
    def __init__(self, dwTime):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.m_dwTime = 0

        self.m_dwTime = dwTime

    def functor_method(self, ch):
        ch.SetLastAttacked(self.m_dwTime)


def SetLastAttacked(dwTime):
    assert m_pkMobInst is not None

    m_pkMobInst.m_dwLastAttackedTime = dwTime
    m_pkMobInst.m_posLastAttacked = GetXYZ()

def SendDamagePacket(pAttacker, Damage, DamageFlag):
    if IsPC() == ((not LGEMiscellaneous.DEFINECONSTANTS.false)) or (pAttacker.IsPC() == ((not LGEMiscellaneous.DEFINECONSTANTS.false)) and pAttacker.GetTarget() is self):
        damageInfo = packet_damage_info()
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memset(damageInfo, 0, sizeof(packet_damage_info))

        damageInfo.header = byte(LG_HEADER_GC_DAMAGE_INFO)
        damageInfo.dwVID = GetVID()
        damageInfo.flag = DamageFlag
        damageInfo.damage = Damage

        if GetDesc() is not None:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            GetDesc().Packet(damageInfo, sizeof(packet_damage_info))

        if pAttacker.GetDesc() is not None:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            pAttacker.GetDesc().Packet(damageInfo, sizeof(packet_damage_info))

class DamageFlag(Enum):
    DAMAGE_NORMAL = (1 << 0)
    DAMAGE_POISON = (1 << 1)
    DAMAGE_DODGE = (1 << 2)
    DAMAGE_BLOCK = (1 << 3)
    DAMAGE_PENETRATE = (1 << 4)
    DAMAGE_CRITICAL = (1 << 5)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if ENABLE_WOLFMAN
    DAMAGE_BLEEDING = (1 << 6)
##endif
def Damage(pAttacker, dam, type):
    if EDamageType.DAMAGE_TYPE_MAGIC == type:
        dam = int((float(dam * (100 + (pAttacker.GetPoint(EPointTypes.LG_POINT_MAGIC_ATT_BONUS_PER) + pAttacker.GetPoint(EPointTypes.LG_POINT_MELEE_MAGIC_ATT_BONUS_PER)))) / 100.0 + 0.5))
    if GetRaceNum() == 5001:
        bDropMoney = LGEMiscellaneous.DEFINECONSTANTS.false
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        iPercent = (GetHP() * 100) / GetMaxHP()

        if iPercent <= 10 and GetMaxSP() < 5:
            SetMaxSP(5)
            bDropMoney = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
        elif iPercent <= 20 and GetMaxSP() < 4:
            SetMaxSP(4)
            bDropMoney = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
        elif iPercent <= 40 and GetMaxSP() < 3:
            SetMaxSP(3)
            bDropMoney = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
        elif iPercent <= 60 and GetMaxSP() < 2:
            SetMaxSP(2)
            bDropMoney = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
        elif iPercent <= 80 and GetMaxSP() < 1:
            SetMaxSP(1)
            bDropMoney = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        if bDropMoney:
            lldGold = 1000
            iSplitCount = number(10, 13)

            #sys_log(0, "WAEGU DropGoldOnHit %d times", GetMaxSP())

            for i in range(1, iSplitCount + 1):
                pos = pixel_position_s()
                item = None

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((item = ITEM_MANAGER::instance().CreateItem(1, lldGold / iSplitCount)))
                if (item = ITEM_MANAGER.instance().CreateItem(1, math.trunc(lldGold / float(iSplitCount)), 0, DefineConstants.false, -1, DefineConstants.false)):
                    if i != 0:
                        pos.x = (number(-14, 14) + number(-14, 14)) * 20
                        pos.y = (number(-14, 14) + number(-14, 14)) * 20

                        pos.x += GetX()
                        pos.y += GetY()

                    item.AddToGround(GetMapIndex(), pos, DefineConstants.false)
                    item.StartDestroyEvent(300)

    if type != EDamageType.DAMAGE_TYPE_NORMAL and type != EDamageType.DAMAGE_TYPE_NORMAL_RANGE:
        if IsAffectFlag(EAffectBits.AFF_TERROR):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
            pct = GetSkillPower(LaniatusETalentXes.LG_SKILL_TERROR) / 400

            if number(1, 100) <= pct:
                return LGEMiscellaneous.DEFINECONSTANTS.false

    iCurHP = GetHP()
    iCurSP = GetSP()

    IsCritical = LGEMiscellaneous.DEFINECONSTANTS.false
    IsPenetrate = LGEMiscellaneous.DEFINECONSTANTS.false
    IsDeathBlow = LGEMiscellaneous.DEFINECONSTANTS.false


    if type == EDamageType.DAMAGE_TYPE_MELEE or type == EDamageType.DAMAGE_TYPE_RANGE or type == EDamageType.DAMAGE_TYPE_MAGIC:
        if pAttacker:
            iCriticalPct = int(pAttacker.GetPoint(EPointTypes.LG_POINT_CRITICAL_PCT))

            if not IsPC():
                iCriticalPct += pAttacker.GetMarriageBonus(uint(UNIQUE_ITEM_MARRIAGE_CRITICAL_BONUS), ((not DefineConstants.false)))

            if iCriticalPct != 0:
                if iCriticalPct >= 10:
                    iCriticalPct = 5 + math.trunc((iCriticalPct - 10) / float(4))
                else:
                    iCriticalPct = math.trunc(iCriticalPct / float(2))

                iCriticalPct -= GetPoint(EPointTypes.LG_POINT_RESIST_CRITICAL)

                if number(1, 100) <= iCriticalPct:
                    IsCritical = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
                    dam *= 2
                    EffectPacket(SPECIAL_EFFECT.SE_CRITICAL)

                    if IsAffectFlag(EAffectBits.AFF_MANASHIELD):
                        RemoveAffect(EAffectBits.AFF_MANASHIELD)

            iPenetratePct = int(pAttacker.GetPoint(EPointTypes.LG_POINT_PENETRATE_PCT))

            if not IsPC():
                iPenetratePct += pAttacker.GetMarriageBonus(uint(UNIQUE_ITEM_MARRIAGE_PENETRATE_BONUS), ((not DefineConstants.false)))


            if iPenetratePct != 0:
                    pkSk = CSkillManager.instance().Get(LaniatusETalentXes.LG_SKILL_RESIST_PENETRATE)

                    if None is not pkSk:
                        pkSk.SetPointVar("k", 1.0 * GetSkillPower(LaniatusETalentXes.LG_SKILL_RESIST_PENETRATE) / 100.0)

                        iPenetratePct -= int(pkSk.kPointPoly.Eval())

                if iPenetratePct >= 10:
                    iPenetratePct = 5 + math.trunc((iPenetratePct - 10) / float(4))
                else:
                    iPenetratePct = math.trunc(iPenetratePct / float(2))

                iPenetratePct -= GetPoint(EPointTypes.LG_POINT_RESIST_PENETRATE)

                if number(1, 100) <= iPenetratePct:
                    IsPenetrate = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

                    if test_server:
                        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Additional Thrusting Damage %d"), math.trunc(GetPoint(EPointTypes.LG_POINT_DEF_GRADE) * (100 + GetPoint(EPointTypes.LG_POINT_DEF_BONUS)) / float(100)))

                    dam += math.trunc(GetPoint(EPointTypes.LG_POINT_DEF_GRADE) * (100 + GetPoint(EPointTypes.LG_POINT_DEF_BONUS)) / float(100))
                    EffectPacket(SPECIAL_EFFECT.SE_PENETRATE)

                    if IsAffectFlag(EAffectBits.AFF_MANASHIELD):
                        RemoveAffect(EAffectBits.AFF_MANASHIELD)

    elif type == EDamageType.DAMAGE_TYPE_NORMAL or type == EDamageType.DAMAGE_TYPE_NORMAL_RANGE:
        if type == EDamageType.DAMAGE_TYPE_NORMAL:
            if GetPoint(EPointTypes.LG_POINT_BLOCK) != 0 and number(1, 100) <= GetPoint(EPointTypes.LG_POINT_BLOCK):
                if test_server:
                    pAttacker.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("%s block! (%d%%)"), GetName(), GetPoint(EPointTypes.LG_POINT_BLOCK))
                    ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("%s block! (%d%%)"), GetName(), GetPoint(EPointTypes.LG_POINT_BLOCK))

                SendDamagePacket(pAttacker, 0, DAMAGE_BLOCK)
                return LGEMiscellaneous.DEFINECONSTANTS.false
        elif type == EDamageType.DAMAGE_TYPE_NORMAL_RANGE:
            if GetPoint(EPointTypes.LG_POINT_DODGE) != 0 and number(1, 100) <= GetPoint(EPointTypes.LG_POINT_DODGE):
                if test_server:
                    pAttacker.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("%s avoid! (%d%%)"), GetName(), GetPoint(EPointTypes.LG_POINT_DODGE))
                    ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("%s avoid! (%d%%)"), GetName(), GetPoint(EPointTypes.LG_POINT_DODGE))

                SendDamagePacket(pAttacker, 0, DAMAGE_DODGE)
                return LGEMiscellaneous.DEFINECONSTANTS.false

        if IsAffectFlag(EAffectBits.AFF_JEONGWIHON):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
            dam = int((dam * (100 + GetSkillPower(LaniatusETalentXes.LG_SKILL_JEONGWI) * 25 / 100) / 100))

        if IsAffectFlag(EAffectBits.AFF_TERROR):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
            dam = int((dam * (95 - GetSkillPower(LaniatusETalentXes.LG_SKILL_TERROR) / 5) / 100))

        if IsAffectFlag(EAffectBits.AFF_HOSIN):
            dam = math.trunc(dam * (100 - GetPoint(EPointTypes.LG_POINT_RESIST_NORMAL_DAMAGE)) / float(100))

        if pAttacker:
            if type == EDamageType.DAMAGE_TYPE_NORMAL:
                if GetPoint(EPointTypes.LG_POINT_REFLECT_MELEE) != 0:
                    reflectDamage = math.trunc(dam * GetPoint(EPointTypes.LG_POINT_REFLECT_MELEE) / float(100))

                    if pAttacker.IsImmune(EImmuneFlags.IMMUNE_REFLECT):
                        reflectDamage = int((reflectDamage / 3.0 + 0.5))

                    pAttacker.Damage(self, reflectDamage, EDamageType.DAMAGE_TYPE_SPECIAL)

            iCriticalPct = int(pAttacker.GetPoint(EPointTypes.LG_POINT_CRITICAL_PCT))

            if not IsPC():
                iCriticalPct += pAttacker.GetMarriageBonus(uint(UNIQUE_ITEM_MARRIAGE_CRITICAL_BONUS), ((not DefineConstants.false)))

            if iCriticalPct != 0:
                iCriticalPct -= GetPoint(EPointTypes.LG_POINT_RESIST_CRITICAL)

                if number(1, 100) <= iCriticalPct:
                    IsCritical = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
                    dam *= 2
                    EffectPacket(SPECIAL_EFFECT.SE_CRITICAL)

            iPenetratePct = int(pAttacker.GetPoint(EPointTypes.LG_POINT_PENETRATE_PCT))

            if not IsPC():
                iPenetratePct += pAttacker.GetMarriageBonus(uint(UNIQUE_ITEM_MARRIAGE_PENETRATE_BONUS), ((not DefineConstants.false)))

                pkSk = CSkillManager.instance().Get(LaniatusETalentXes.LG_SKILL_RESIST_PENETRATE)

                if None is not pkSk:
                    pkSk.SetPointVar("k", 1.0 * GetSkillPower(LaniatusETalentXes.LG_SKILL_RESIST_PENETRATE) / 100.0)

                    iPenetratePct -= int(pkSk.kPointPoly.Eval())

            if iPenetratePct != 0:

                iPenetratePct -= GetPoint(EPointTypes.LG_POINT_RESIST_PENETRATE)

                if number(1, 100) <= iPenetratePct:
                    IsPenetrate = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

                    if test_server:
                        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Additional Thrusting Damage %d"), math.trunc(GetPoint(EPointTypes.LG_POINT_DEF_GRADE) * (100 + GetPoint(EPointTypes.LG_POINT_DEF_BONUS)) / float(100)))
                    dam += math.trunc(GetPoint(EPointTypes.LG_POINT_DEF_GRADE) * (100 + GetPoint(EPointTypes.LG_POINT_DEF_BONUS)) / float(100))
                    EffectPacket(SPECIAL_EFFECT.SE_PENETRATE)

            if pAttacker.GetPoint(EPointTypes.LG_POINT_STEAL_HP) != 0:
                pct = 1

                if number(1, 10) <= pct:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
                    iHP = MIN(dam, MAX(0, iCurHP)) * pAttacker.GetPoint(EPointTypes.LG_POINT_STEAL_HP) / 100

                    if iHP > 0 and GetHP() >= iHP:
                        CreateFly(FLY_HP_SMALL, pAttacker)
                        pAttacker.PointChange(EPointTypes.LG_POINT_HP, iHP, DefineConstants.false, DefineConstants.false)
                        PointChange(EPointTypes.LG_POINT_HP, -iHP)

            if pAttacker.GetPoint(EPointTypes.LG_POINT_STEAL_SP) != 0:
                pct = 1

                if number(1, 10) <= pct:
                    iCur = None

                    if IsPC():
                        iCur = iCurSP
                    else:
                        iCur = iCurHP

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
                    iSP = MIN(dam, MAX(0, iCur)) * pAttacker.GetPoint(EPointTypes.LG_POINT_STEAL_SP) / 100

                    if iSP > 0 and iCur >= iSP:
                        CreateFly(FLY_SP_SMALL, pAttacker)
                        pAttacker.PointChange(EPointTypes.LG_POINT_SP, iSP, DefineConstants.false, DefineConstants.false)

                        if IsPC():
                            PointChange(EPointTypes.LG_POINT_SP, -iSP)

            if pAttacker.GetPoint(EPointTypes.LG_POINT_STEAL_GOLD) != 0:
                if number(1, 100) <= pAttacker.GetPoint(EPointTypes.LG_POINT_STEAL_GOLD):
                    iAmount = number(1, GetLevel())
                    pAttacker.PointChange(EPointTypes.LG_POINT_GOLD, iAmount, DefineConstants.false, DefineConstants.false)

            if pAttacker.GetPoint(EPointTypes.LG_POINT_HIT_HP_RECOVERY) != 0 and number(0, 4) > 0:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
                i = MIN(dam, iCurHP) * pAttacker.GetPoint(EPointTypes.LG_POINT_HIT_HP_RECOVERY) / 100

                i != 0 i:
                    CreateFly(FLY_HP_SMALL, pAttacker)
                    pAttacker.PointChange(EPointTypes.LG_POINT_HP, abs(i), DefineConstants.false, DefineConstants.false)

            if pAttacker.GetPoint(EPointTypes.LG_POINT_HIT_SP_RECOVERY) != 0 and number(0, 4) > 0:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
                i = MIN(dam, iCurHP) * pAttacker.GetPoint(EPointTypes.LG_POINT_HIT_SP_RECOVERY) / 100

                i != 0 i:
                    CreateFly(FLY_SP_SMALL, pAttacker)
                    pAttacker.PointChange(EPointTypes.LG_POINT_SP, i, DefineConstants.false, DefineConstants.false)

            if pAttacker.GetPoint(EPointTypes.LG_POINT_MANA_BURN_PCT) != 0:
                if number(1, 100) <= pAttacker.GetPoint(EPointTypes.LG_POINT_MANA_BURN_PCT):
                    PointChange(EPointTypes.LG_POINT_SP, -50)

    if (type == EDamageType.DAMAGE_TYPE_NORMAL) or (type == EDamageType.DAMAGE_TYPE_NORMAL_RANGE):
        if pAttacker:
            if pAttacker.GetPoint(EPointTypes.LG_POINT_NORMAL_HIT_DAMAGE_BONUS) != 0:
                dam = math.trunc(dam * (100 + pAttacker.GetPoint(EPointTypes.LG_POINT_NORMAL_HIT_DAMAGE_BONUS)) / float(100))

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        dam = dam * (100 - MIN(99, GetPoint(EPointTypes.LG_POINT_NORMAL_HIT_DEFEND_BONUS))) / 100

    elif (type == EDamageType.DAMAGE_TYPE_MELEE) or (type == EDamageType.DAMAGE_TYPE_RANGE) or (type == EDamageType.DAMAGE_TYPE_FIRE) or (type == EDamageType.DAMAGE_TYPE_ICE) or (type == EDamageType.DAMAGE_TYPE_ELEC) or (type == EDamageType.DAMAGE_TYPE_MAGIC):
        if pAttacker:
            if pAttacker.GetPoint(EPointTypes.LG_POINT_LG_SKILL_DAMAGE_BONUS) != 0:
                dam = math.trunc(dam * (100 + pAttacker.GetPoint(EPointTypes.LG_POINT_LG_SKILL_DAMAGE_BONUS)) / float(100))

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        dam = dam * (100 - MIN(99, GetPoint(EPointTypes.LG_POINT_LG_SKILL_DEFEND_BONUS))) / 100


    if IsAffectFlag(EAffectBits.AFF_MANASHIELD):

        iDamageSPPart = math.trunc(dam / float(3))
        iDamageToSP = math.trunc(iDamageSPPart * GetPoint(EPointTypes.LG_POINT_MANASHIELD) / float(100))
        iSP = GetSP()

        if iDamageToSP <= iSP:
            PointChange(EPointTypes.LG_POINT_SP, -iDamageToSP)
            dam -= iDamageSPPart
        else:
            PointChange(EPointTypes.LG_POINT_SP, -GetSP())
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
            dam -= iSP * 100 / MAX(GetPoint(EPointTypes.LG_POINT_MANASHIELD), 1)

    if GetPoint(EPointTypes.LG_POINT_MALL_DEFBONUS) > 0:
        dec_dam = MIN(200, math.trunc(dam * GetPoint(EPointTypes.LG_POINT_MALL_DEFBONUS) / float(100)))
        dam -= dec_dam

    if pAttacker:
        if pAttacker.GetPoint(EPointTypes.LG_POINT_MALL_ATTBONUS) > 0:
            add_dam = MIN(300, math.trunc(dam * pAttacker.GetLimitPoint(EPointTypes.LG_POINT_MALL_ATTBONUS) / float(100)))
            dam += add_dam

        if pAttacker.IsPC():
            if (not IsPC()) and GetMonsterDrainSPPoint() != 0:
                iDrain = GetMonsterDrainSPPoint()

                if iDrain <= pAttacker.GetSP():
                    pAttacker.PointChange(EPointTypes.LG_POINT_SP, -iDrain, DefineConstants.false, DefineConstants.false)
                else:
                    iSP = pAttacker.GetSP()
                    pAttacker.PointChange(EPointTypes.LG_POINT_SP, -iSP, DefineConstants.false, DefineConstants.false)

        elif pAttacker.IsGuardNPC():
            ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'SET_BIT' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
            SET_BIT(m_pointsInstant.instant_flag, (1 << 4))
            Stun()
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    if (not GetSectree()) or GetSectree().IsAttr(GetX(), GetY(), ATTR_BANPK):
        return LGEMiscellaneous.DEFINECONSTANTS.false

    if not IsPC():
        if m_pkParty and m_pkParty.GetLeader():
            m_pkParty.GetLeader().SetLastAttacked(get_dword_time())
        else:
            SetLastAttacked(get_dword_time())

    if IsStun():
        Dead(pAttacker)
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    if IsDead():
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    if type == EDamageType.DAMAGE_TYPE_POISON:
        if GetHP() - dam <= 0:
            dam = GetHP() - 1
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if ENABLE_WOLFMAN
    elif type == EDamageType.DAMAGE_TYPE_BLEEDING:
        if GetHP() - dam <= 0:
            dam = GetHP()
##endif
    if pAttacker is not None and pAttacker.IsPC():
        iDmgPct = CHARACTER_MANAGER.instance().GetUserDamageRate(pAttacker)
        dam = math.trunc(dam * iDmgPct / float(100))

    if IsMonster() and IsStoneSkinner():
        if GetHPPct() < GetMobTable().bStoneSkinPoint:
            dam = math.trunc(dam / float(2))

    if pAttacker:
        if pAttacker.IsMonster() and pAttacker.IsDeathBlower():
            if pAttacker.IsDeathBlow():
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if ENABLE_WOLFMAN
                if number(EJobs.JOB_LG_PAWN_WARRIOR, EJobs.JOB_WOLFMAN) == GetJob():
##else
                if number(EJobs.JOB_LG_PAWN_WARRIOR, EJobs.JOB_LG_PAWN_MAGE) == GetJob():
##endif
                    IsDeathBlow = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
                    dam = dam * 4

        dam = BlueDragon_Damage(self, pAttacker, dam)

        damageFlag = 0

        if type == EDamageType.DAMAGE_TYPE_POISON:
            damageFlag = DAMAGE_POISON
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if ENABLE_WOLFMAN
        elif type == EDamageType.DAMAGE_TYPE_BLEEDING:
            damageFlag = DAMAGE_BLEEDING
##endif
        else:
            damageFlag = DAMAGE_NORMAL

        if IsCritical == ((not LGEMiscellaneous.DEFINECONSTANTS.false)):
            damageFlag |= DAMAGE_CRITICAL

        if IsPenetrate == ((not LGEMiscellaneous.DEFINECONSTANTS.false)):
            damageFlag |= DAMAGE_PENETRATE

        damMul = self.GetDamMul()
        tempDam = dam
        dam = int(tempDam * damMul + 0.5)


        if pAttacker:
            SendDamagePacket(pAttacker, dam, damageFlag)

        if test_server:
            if pAttacker:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
                pAttacker.ChatPacket(EChatType.CHAT_TYPE_INFO, "-> %s, DAM %d HP %d(%d%%) %s%s", GetName(), dam, GetHP(), (GetHP() * 100) / GetMaxHP(),"crit " if IsCritical else "","pene " if IsPenetrate else "","deathblow " if IsDeathBlow else "")

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
            ChatPacket(EChatType.CHAT_TYPE_PARTY, "<- %s, DAM %d HP %d(%d%%) %s%s",pAttacker.GetName(LOCALE_LANIATUS) if pAttacker is not None else 0, dam, GetHP(), (GetHP() * 100) / GetMaxHP(),"crit " if IsCritical else "","pene " if IsPenetrate else "","deathblow " if IsDeathBlow else "")

    if not cannot_dead:
        PointChange(EPointTypes.LG_POINT_HP, -dam, LGEMiscellaneous.DEFINECONSTANTS.false)

    if pAttacker is not None and dam > 0 and IsNPC():
        it = m_map_kDamage.find(pAttacker.GetVID())

        if it == m_map_kDamage.end():
            m_map_kDamage.insert(TDamageMap.value_type(pAttacker.GetVID(), TBattleInfo(dam, 0)))
            it = m_map_kDamage.find(pAttacker.GetVID())
        else:
            it.second.iTotalDamage += dam

        StartRecoveryEvent()
        UpdateAggrPointEx(pAttacker, type, dam, it.second)

    if GetHP() <= 0:
        Dead(pAttacker)

    return LGEMiscellaneous.DEFINECONSTANTS.false

def DistributeHP(pkKiller):
    if pkKiller.GetDungeon():
        return

class NPartyExpDistribute: #this class replaces the original namespace 'NPartyExpDistribute'
    class FPartyTotaler:

        def __init__(self, center):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.total = 0
            self.member_count = 0
            self.x = 0
            self.y = 0

            self.total = 0
            self.member_count = 0
            self.x = center.GetX()
            self.y = center.GetY()

        def functor_method(self, ch):
            if Globals.DISTANCE_APPROX(ch.GetX() - self.x, ch.GetY() - self.y) <= Globals.PARTY_DEFAULT_RANGE:
                self.total += party_exp_distribute_table[ch.GetLevel()]

                self.member_count += 1

    class FPartyDistributor:

        def __init__(self, center, member_count, total, iExp, iMode):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.total = 0
            self.c = []
            self.x = 0
            self.y = 0
            self._iExp = 0
            self.m_iMode = 0
            self.m_iMemberCount = 0

            self.total = total
            self.c = CHARACTER(center)
            self.x = center.GetX()
            self.y = center.GetY()
            self._iExp = iExp
            self.m_iMode = iMode
            self.m_iMemberCount = member_count
            if self.m_iMemberCount == 0:
                self.m_iMemberCount = 1

        def functor_method(self, ch):
            if Globals.DISTANCE_APPROX(ch.GetX() - self.x, ch.GetY() - self.y) <= Globals.PARTY_DEFAULT_RANGE:
                iExp2 = 0

                if self.m_iMode == EPartyExpDistributionModes.PARTY_EXP_DISTRIBUTION_NON_PARITY:
                    iExp2 = uint((self._iExp * float(party_exp_distribute_table[ch.GetLevel()]) / self.total))

                elif self.m_iMode == EPartyExpDistributionModes.PARTY_EXP_DISTRIBUTION_PARITY:
                    iExp2 = math.trunc(self._iExp / float(self.m_iMemberCount))

                else:
                    #lani_err("Unknown party exp distribution mode %d", self.m_iMode)
                    return

                Globals.GiveExp(self.c, ch, int(iExp2))

class SDamageInfo:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.iDam = 0
        self.pAttacker = None
        self.pParty = None


    def Clear(self):
        self.pAttacker = None
        self.pParty = None

    def Distribute(self, ch, iExp):
        if self.pAttacker:
            Globals.GiveExp(ch, self.pAttacker, iExp)
        elif self.pParty:
            f = NPartyExpDistribute.FPartyTotaler(ch)
            self.pParty.ForEachOnlineMember(f.functor_method)

            if self.pParty.IsPositionNearLeader(ch):
                iExp = math.trunc(iExp * (100 + self.pParty.GetExpBonusPercent()) / float(100))

            if test_server:
                if (quest.CQuestManager.instance().GetEventFlag("exp_bonus_log")) != 0 and self.pParty.GetExpBonusPercent() != 0:
                    self.pParty.ChatPacketToAllMember(EChatType.CHAT_TYPE_INFO, "exp party bonus %d%%", self.pParty.GetExpBonusPercent())

            if self.pParty.GetExpCentralizeCharacter():
                tch = self.pParty.GetExpCentralizeCharacter()

                if Globals.DISTANCE_APPROX(ch.GetX() - tch.GetX(), ch.GetY() - tch.GetY()) <= Globals.PARTY_DEFAULT_RANGE:
                    iExpCenteralize = int((iExp * 0.05))
                    iExp -= iExpCenteralize

                    Globals.GiveExp(ch, self.pParty.GetExpCentralizeCharacter(), iExpCenteralize)

            fDist = NPartyExpDistribute.FPartyDistributor(ch, f.member_count, f.total, uint(iExp), self.pParty.GetExpDistributionMode())
            self.pParty.ForEachOnlineMember(fDist.functor_method)

def DistributeExp():
    iExpToDistribute = GetExp()

    if iExpToDistribute <= 0:
        return None

    iTotalDam = 0
    pkChrMostAttacked = None
    iMostDam = 0

    damage_info_table = []
    map_party_damage = {}

    damage_info_table.reserve(len(m_map_kDamage))

    it = m_map_kDamage.begin()

    while it is not m_map_kDamage.end():
        c_VID = it.first
        iDam = it.second.iTotalDamage

        it += 1

        pAttacker = CHARACTER_MANAGER.instance().Find(c_VID)

        if pAttacker is None or pAttacker.IsNPC() or DISTANCE_APPROX(GetX()-pAttacker.GetX(), GetY()-pAttacker.GetY())>5000:
            continue

        iTotalDam += iDam
        if pkChrMostAttacked is None or iDam > iMostDam:
            pkChrMostAttacked = pAttacker
            iMostDam = iDam

        if pAttacker.GetParty():
            it = map_party_damage.find(pAttacker.GetParty())
            if it is map_party_damage.end():
                di = SDamageInfo()
                di.iDam = iDam
                di.pAttacker = None
                di.pParty = pAttacker.GetParty()
                map_party_damage.update({di.pParty: di})
            else:
                it.second.iDam += iDam
        else:
            di = SDamageInfo()

            di.iDam = iDam
            di.pAttacker = pAttacker
            di.pParty = None

            damage_info_table.append(di)

    it = map_party_damage.begin()
    while it is not map_party_damage.end():
        damage_info_table.append(it.second)
        it += 1

    SetExp(0)

    if iTotalDam == 0:
        return None

    if m_pkChrStone:
        iExp = iExpToDistribute >> 1
        m_pkChrStone.SetExp(m_pkChrStone.GetExp() + iExp)
        iExpToDistribute -= iExp

    #sys_log(1, "%s total exp: %d, damage_info_table.size() == %d, TotalDam %d", GetName(), iExpToDistribute, len(damage_info_table), iTotalDam)

    if not damage_info_table:
        return None

    DistributeHP(pkChrMostAttacked)

        di = damage_info_table.begin()
            for it in damage_info_table:
                if it.iDam > di.iDam:
                    di = it

        iExp = math.trunc(iExpToDistribute / float(5))
        iExpToDistribute -= iExp

        fPercent = float(di.iDam) / iTotalDam

        if fPercent > 1.0:
            #lani_err("DistributeExp percent over 1.0 (fPercent %f name %s)", fPercent, di.pAttacker.GetName())
            fPercent = 1.0

        iExp += int((iExpToDistribute * fPercent))

        di.Distribute(self, iExp)

        if fPercent == 1.0:
            return pkChrMostAttacked

        di.Clear()

        for it in damage_info_table:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to references to variables:
#ORIGINAL METINII C CODE: SDamageInfo & di = *it;
            di = *it

            fPercent = float(di.iDam) / iTotalDam

            if fPercent > 1.0:
                #lani_err("DistributeExp percent over 1.0 (fPercent %f name %s)", fPercent, di.pAttacker.GetName(LOCALE_LANIATUS))
                fPercent = 1.0

            di.Distribute(self, int((iExpToDistribute * fPercent)))

    return pkChrMostAttacked

def GetArrowAndBow(ppkBow, ppkArrow, iArrowCount):
    pkBow = None

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if (!(pkBow = GetWear(WEAR_WEAPON)) || pkBow->GetProto()->bSubType != WEAPON_BOW)
    if not(pkBow = GetWear(EWearPositions.WEAR_WEAPON)) or pkBow.GetProto().bSubType != EWeaponSubTypes.WEAPON_BOW:
        return 0

    pkArrow = None

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if (!(pkArrow = GetWear(WEAR_ARROW)) || pkArrow->GetType() != ITEM_WEAPON || (pkArrow->GetSubType() != WEAPON_ARROW && pkArrow->GetSubType() != WEAPON_QUIVER))
    if not(pkArrow = GetWear(EWearPositions.WEAR_ARROW)) or pkArrow.GetType() != EItemTypes.ITEM_WEAPON or (pkArrow.GetSubType() != EWeaponSubTypes.WEAPON_ARROW and pkArrow.GetSubType() != EWeaponSubTypes.WEAPON_QUIVER):
        return 0

    if pkArrow.GetSubType() == EWeaponSubTypes.WEAPON_QUIVER:
        iArrowCount = MIN(iArrowCount, pkArrow.GetSocket(0) - time(0))
    else:
        iArrowCount = MIN(iArrowCount, pkArrow.GetCount())

## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: *ppkBow = pkBow;
    ppkBow[0].copy_from(pkBow)
## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: *ppkArrow = pkArrow;
    ppkArrow[0].copy_from(pkArrow)

    return iArrowCount

def UseArrow(pkArrow, dwArrowCount):
    iCount = int(pkArrow.GetCount())

    if pkArrow.GetSubType() == EWeaponSubTypes.WEAPON_QUIVER:
        return

    dwVnum = pkArrow.GetVnum()
    iCount = iCount - MIN(iCount, dwArrowCount)
    pkArrow.SetCount(uint(iCount))

    if iCount == 0:
        pkNewArrow = FindSpecifyItem(dwVnum)

        #sys_log(0, "UseArrow : FindSpecifyItem %u %p", dwVnum, get_pointer(pkNewArrow))

        if pkNewArrow:
            EquipItem(pkNewArrow)

class CFuncShoot:

    def __init__(self, ch, bType):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.m_me = None
        self.m_bType = 0
        self.m_bSucceed = False

        self.m_me = ch
        self.m_bType = bType
        self.m_bSucceed = LGEMiscellaneous.DEFINECONSTANTS.false

    def functor_method(self, dwTargetVID):
        if self.m_bType > 1:
            if g_bSkillDisable:
                return

            self.m_me.m_SkillUseInfo[self.m_bType].SetMainTargetVID(dwTargetVID)

        pkVictim = CHARACTER_MANAGER.instance().Find(dwTargetVID)

        if pkVictim is None:
            return

        if not battle_is_attackable(self.m_me, pkVictim):
            return

        if self.m_me.IsNPC():
            if Globals.DISTANCE_APPROX(self.m_me.GetX() - pkVictim.GetX(), self.m_me.GetY() - pkVictim.GetY()) > 5000:
                return

        pkBow = None
        pkArrow = None
        reduce_resist_magic = 0

        if self.m_bType == 0:
                iDam = 0

                if self.m_me.IsPC():
                    if self.m_me.GetJob() != EJobs.JOB_LG_PAWN_ASSASSIN:
                        return

                    if 0 == self.m_me.GetArrowAndBow(pkBow, pkArrow, 1):
                        return

                    if self.m_me.GetSkillGroup() != 0:
                        if (not self.m_me.IsNPC()) and self.m_me.GetSkillGroup() != 2:
                            if self.m_me.GetSP() < 5:
                                return

                            self.m_me.PointChange(EPointTypes.LG_POINT_SP, -5, DefineConstants.false, DefineConstants.false)

                    iDam = CalcArrowDamage(self.m_me, pkVictim, pkBow, pkArrow)
                    self.m_me.UseArrow(pkArrow, 1)

                    dwCurrentTime = get_dword_time()
                    if IS_SPEED_HACK(self.m_me, pkVictim, dwCurrentTime):
                        iDam = 0
                else:
                    iDam = CalcMeleeDamage(self.m_me, pkVictim)

                NormalAttackAffect(self.m_me, pkVictim)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
                iDam = int(iDam * (100 - pkVictim.GetPoint(EPointTypes.LG_POINT_RESIST_BOW)) / 100)
                self.m_me.OnMove(((not LGEMiscellaneous.DEFINECONSTANTS.false)))
                pkVictim.OnMove(DefineConstants.false)

                if pkVictim.CanBeginFight():
                    pkVictim.BeginFight(self.m_me)

                pkVictim.Damage(self.m_me, iDam, EDamageType.DAMAGE_TYPE_NORMAL_RANGE)

        elif self.m_bType == 1:
                iDam = None

                if self.m_me.IsPC():
                    return

                iDam = CalcMagicDamage(self.m_me, pkVictim)

                NormalAttackAffect(self.m_me, pkVictim)
                reduce_resist_magic = int(pkVictim.GetPoint(EPointTypes.LG_POINT_RESIST_MAGIC))
                if self.m_me.GetPoint(EPointTypes.LG_POINT_RESIST_MAGIC_REDUCTION) > 0:
                    fix_magic_resistance = int((100)) if (pkVictim.GetPoint(EPointTypes.LG_POINT_RESIST_MAGIC) > 100) else int(pkVictim.GetPoint(EPointTypes.LG_POINT_RESIST_MAGIC))

                    reduce_resist_magic = int(fix_magic_resistance - self.m_me.GetPoint(EPointTypes.LG_POINT_RESIST_MAGIC_REDUCTION))
                    if reduce_resist_magic < 1:
                        reduce_resist_magic = 0

                iDam = math.trunc(iDam * (100 - reduce_resist_magic) / float(100))
                self.m_me.OnMove(((not LGEMiscellaneous.DEFINECONSTANTS.false)))
                pkVictim.OnMove(DefineConstants.false)

                if pkVictim.CanBeginFight():
                    pkVictim.BeginFight(self.m_me)

                pkVictim.Damage(self.m_me, iDam, EDamageType.DAMAGE_TYPE_MAGIC)

        elif self.m_bType == LaniatusETalentXes.LG_SKILL_YEONSA:
                iUseArrow = 1
                    if iUseArrow == self.m_me.GetArrowAndBow(pkBow, pkArrow, iUseArrow):
                        self.m_me.OnMove(((not LGEMiscellaneous.DEFINECONSTANTS.false)))
                        pkVictim.OnMove(DefineConstants.false)

                        if pkVictim.CanBeginFight():
                            pkVictim.BeginFight(self.m_me)

                        self.m_me.ComputeSkill(self.m_bType, pkVictim, 0)
                        self.m_me.UseArrow(pkArrow, uint(iUseArrow))

                        if pkVictim.IsDead():
                            break

                    else:
                        break


        elif self.m_bType == LaniatusETalentXes.LG_SKILL_KWANKYEOK:
                iUseArrow = 1

                if iUseArrow == self.m_me.GetArrowAndBow(pkBow, pkArrow, iUseArrow):
                    self.m_me.OnMove(((not LGEMiscellaneous.DEFINECONSTANTS.false)))
                    pkVictim.OnMove(DefineConstants.false)

                    if pkVictim.CanBeginFight():
                        pkVictim.BeginFight(self.m_me)

                    #sys_log(0, "%s kwankeyok %s", self.m_me.GetName(LOCALE_LANIATUS), pkVictim.GetName(LOCALE_LANIATUS))
                    self.m_me.ComputeSkill(self.m_bType, pkVictim, 0)
                    self.m_me.UseArrow(pkArrow, uint(iUseArrow))

        elif self.m_bType == LaniatusETalentXes.LG_SKILL_GIGUNG:
                iUseArrow = 1
                if iUseArrow == self.m_me.GetArrowAndBow(pkBow, pkArrow, iUseArrow):
                    self.m_me.OnMove(((not LGEMiscellaneous.DEFINECONSTANTS.false)))
                    pkVictim.OnMove(DefineConstants.false)

                    if pkVictim.CanBeginFight():
                        pkVictim.BeginFight(self.m_me)

                    #sys_log(0, "%s gigung %s", self.m_me.GetName(LOCALE_LANIATUS), pkVictim.GetName(LOCALE_LANIATUS))
                    self.m_me.ComputeSkill(self.m_bType, pkVictim, 0)
                    self.m_me.UseArrow(pkArrow, uint(iUseArrow))

        elif self.m_bType == LaniatusETalentXes.LG_SKILL_HWAJO:
                iUseArrow = 1
                if iUseArrow == self.m_me.GetArrowAndBow(pkBow, pkArrow, iUseArrow):
                    self.m_me.OnMove(((not LGEMiscellaneous.DEFINECONSTANTS.false)))
                    pkVictim.OnMove(DefineConstants.false)

                    if pkVictim.CanBeginFight():
                        pkVictim.BeginFight(self.m_me)

                    #sys_log(0, "%s hwajo %s", self.m_me.GetName(LOCALE_LANIATUS), pkVictim.GetName(LOCALE_LANIATUS))
                    self.m_me.ComputeSkill(self.m_bType, pkVictim, 0)
                    self.m_me.UseArrow(pkArrow, uint(iUseArrow))


        elif self.m_bType == LaniatusETalentXes.LG_SKILL_HORSE_WILDATTACK_RANGE:
                iUseArrow = 1
                if iUseArrow == self.m_me.GetArrowAndBow(pkBow, pkArrow, iUseArrow):
                    self.m_me.OnMove(((not LGEMiscellaneous.DEFINECONSTANTS.false)))
                    pkVictim.OnMove(DefineConstants.false)

                    if pkVictim.CanBeginFight():
                        pkVictim.BeginFight(self.m_me)

                    #sys_log(0, "%s horse_wildattack %s", self.m_me.GetName(LOCALE_LANIATUS), pkVictim.GetName(LOCALE_LANIATUS))
                    self.m_me.ComputeSkill(self.m_bType, pkVictim, 0)
                    self.m_me.UseArrow(pkArrow, uint(iUseArrow))


        elif (self.m_bType == LaniatusETalentXes.LG_SKILL_MARYUNG) or (self.m_bType == LaniatusETalentXes.LG_SKILL_TUSOK) or (self.m_bType == LaniatusETalentXes.LG_SKILL_BIPABU) or (self.m_bType == LaniatusETalentXes.LG_SKILL_NOEJEON) or (self.m_bType == LaniatusETalentXes.LG_SKILL_GEOMPUNG) or (self.m_bType == LaniatusETalentXes.LG_SKILL_SANGONG) or (self.m_bType == LaniatusETalentXes.LG_SKILL_MAHWAN) or (self.m_bType == LaniatusETalentXes.LG_SKILL_PABEOB):
                self.m_me.OnMove(((not LGEMiscellaneous.DEFINECONSTANTS.false)))
                pkVictim.OnMove(DefineConstants.false)

                if pkVictim.CanBeginFight():
                    pkVictim.BeginFight(self.m_me)

                #sys_log(0, "%s - Skill %d -> %s", self.m_me.GetName(LOCALE_LANIATUS), self.m_bType, pkVictim.GetName(LOCALE_LANIATUS))
                self.m_me.ComputeSkill(self.m_bType, pkVictim, 0)

        elif self.m_bType == LaniatusETalentXes.LG_SKILL_CHAIN:
                self.m_me.OnMove(((not LGEMiscellaneous.DEFINECONSTANTS.false)))
                pkVictim.OnMove(DefineConstants.false)

                if pkVictim.CanBeginFight():
                    pkVictim.BeginFight(self.m_me)

                #sys_log(0, "%s - Skill %d -> %s", self.m_me.GetName(LOCALE_LANIATUS), self.m_bType, pkVictim.GetName(LOCALE_LANIATUS))
                self.m_me.ComputeSkill(self.m_bType, pkVictim, 0)

        elif self.m_bType == LaniatusETalentXes.LG_SKILL_YONGBI:
                self.m_me.OnMove(((not LGEMiscellaneous.DEFINECONSTANTS.false)))

        else:
            #lani_err("CFuncShoot: I don't know this type [%d] of range attack.", int(self.m_bType))

        self.m_bSucceed = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

def Shoot(bType):
    #sys_log(1, "Shoot %s type %u flyTargets.size %zu", GetName(), bType, m_vec_dwFlyTargets.size())

    if not CanMove():
        return LGEMiscellaneous.DEFINECONSTANTS.false

    f = CFuncShoot(self, bType)

    if m_dwFlyTargetID != 0:
        f.functor_method(m_dwFlyTargetID)
        m_dwFlyTargetID = 0

    f = std::for_each(m_vec_dwFlyTargets.begin(), m_vec_dwFlyTargets.end(), f.functor_method)
    m_vec_dwFlyTargets.clear()

    return f.m_bSucceed

def FlyTarget(dwTargetVID, x, y, bHeader):
    pkVictim = CHARACTER_MANAGER.instance().Find(dwTargetVID)
    pack = packet_fly_targeting()

    pack.bHeader = byte(LG_HEADER_GC_FLY_TARGETING) if (bHeader == LG_HEADER_CG_FLY_TARGETING) else byte(LG_HEADER_GC_ADD_FLY_TARGETING)
    pack.dwShooterVID = GetVID()

    if pkVictim:
        pack.dwTargetVID = pkVictim.GetVID()
        pack.x = pkVictim.GetX()
        pack.y = pkVictim.GetY()

        if bHeader == LG_HEADER_CG_FLY_TARGETING:
            m_dwFlyTargetID = dwTargetVID
        else:
            m_vec_dwFlyTargets.push_back(dwTargetVID)
    else:
        pack.dwTargetVID = 0
        pack.x = x
        pack.y = y

    #sys_log(1, "FlyTarget %s vid %d x %d y %d", GetName(), pack.dwTargetVID, pack.x, pack.y)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    PacketAround(pack, sizeof(pack), self)

def GetNearestVictim(pkChr):
    if None is pkChr:
        pkChr = self

    fMinDist = 99999.0
    pkVictim = None

    it = m_map_kDamage.begin()

    while it is not m_map_kDamage.end():
        c_VID = it.first
        it += 1

        pAttacker = CHARACTER_MANAGER.instance().Find(c_VID)

        if pAttacker is None:
            continue

        if pAttacker.IsAffectFlag(EAffectBits.AFF_EUNHYUNG) or pAttacker.IsAffectFlag(EAffectBits.AFF_INVISIBILITY) or pAttacker.IsAffectFlag(EAffectBits.AFF_REVIVE_INVISIBLE):
            continue

        fDist = DISTANCE_APPROX(pAttacker.GetX() - pkChr.GetX(), pAttacker.GetY() - pkChr.GetY())

        if fDist < fMinDist:
            pkVictim = pAttacker
            fMinDist = fDist

    return pkVictim

def SetVictim(pkVictim):
    if pkVictim is None:
        m_kVIDVictim.Reset()
        battle_end(self)
    else:
        m_kVIDVictim = pkVictim.GetVID()
        m_dwLastVictimSetTime = get_dword_time()

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: CHARACTER* CHARACTER::GetVictim() const
def GetVictim():
    return CHARACTER_MANAGER.instance().Find(m_kVIDVictim)

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: CHARACTER* CHARACTER::GetProtege() const
def GetProtege():
    if m_pkChrStone:
        return m_pkChrStone

    if m_pkParty:
        return m_pkParty.GetLeader()

    return None

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: int CHARACTER::GetAlignment() const
def GetAlignment():
    return m_iAlignment

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: int CHARACTER::GetRealAlignment() const
def GetRealAlignment():
    return m_iRealAlignment

def ShowAlignment(bShow):
    if bShow:
        if m_iAlignment != m_iRealAlignment:
            m_iAlignment = m_iRealAlignment
            UpdatePacket()
    else:
        if m_iAlignment != 0:
            m_iAlignment = 0
            UpdatePacket()

def UpdateAlignment(iAmount):
    bShow = LGEMiscellaneous.DEFINECONSTANTS.false

    if m_iAlignment == m_iRealAlignment:
        bShow = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
    i = m_iAlignment / 10

    m_iRealAlignment = MINMAX(-200000, m_iRealAlignment + iAmount, 200000)

    if bShow:
        m_iAlignment = m_iRealAlignment

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        if i != m_iAlignment / 10:
            UpdatePacket()

def SetKillerMode(isOn):
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'IS_SET' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
    if (ADD_CHARACTER_STATE_KILLER if isOn else 0) == IS_SET(m_bAddChrState, ADD_CHARACTER_STATE_KILLER):
        return

    if isOn:
        ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'SET_BIT' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
        SET_BIT(m_bAddChrState, ADD_CHARACTER_STATE_KILLER)
    else:
        ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'REMOVE_BIT' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
        REMOVE_BIT(m_bAddChrState, ADD_CHARACTER_STATE_KILLER)

    m_iKillerModePulse = thecore_pulse()
    UpdatePacket()
    #sys_log(0, "SetKillerMode Update %s[%d]", GetName(), GetPlayerID())

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: bool CHARACTER::IsKillerMode() const
def IsKillerMode():
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'IS_SET' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
    return IS_SET(m_bAddChrState, ADD_CHARACTER_STATE_KILLER)

def UpdateKillerMode():
    if not IsKillerMode():
        return

    if thecore_pulse() - m_iKillerModePulse >= ((30) * passes_per_sec):
        SetKillerMode(LGEMiscellaneous.DEFINECONSTANTS.false)

def SetPKMode(bPKMode):
    if bPKMode >= EPKModes.PK_MODE_MAX_NUM:
        return

    if m_bPKMode == bPKMode:
        return

    if bPKMode == EPKModes.PK_MODE_GUILD and not GetGuild():
        bPKMode = EPKModes.PK_MODE_FREE

    m_bPKMode = bPKMode
    UpdatePacket()

    #sys_log(0, "PK_MODE: %s %d", GetName(), m_bPKMode)

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: byte CHARACTER::GetPKMode() const
def GetPKMode():
    return m_bPKMode

class FuncForgetMyAttacker:
    def __init__(self, ch):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.m_ch = None

        self.m_ch = ch
    def functor_method(self, ent):
        if ent.IsType(EEntityTypes.ENTITY_CHARACTER):
            ch = ent
            if ch.IsPC():
                return
            if ch.m_kVIDVictim.equals_to(self.m_ch.GetVID()):
                ch.SetVictim(None)

class FuncAggregateMonster:
    def __init__(self, ch):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.m_ch = None

        self.m_ch = ch
    def functor_method(self, ent):
        if ent.IsType(EEntityTypes.ENTITY_CHARACTER):
            ch = ent
            if ch.IsPC():
                return
            if not ch.IsMonster():
                return
            if ch.GetVictim():
                return

            if Globals.DISTANCE_APPROX(ch.GetX() - self.m_ch.GetX(), ch.GetY() - self.m_ch.GetY()) < 5000:
                if ch.CanBeginFight():
                    ch.BeginFight(self.m_ch)

class FuncAttractRanger:
    def __init__(self, ch):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.m_ch = None

        self.m_ch = ch

    def functor_method(self, ent):
        if ent.IsType(EEntityTypes.ENTITY_CHARACTER):
            ch = ent
            if ch.IsPC():
                return
            if not ch.IsMonster():
                return
            if ch.GetVictim() is not None and ch.GetVictim() is not self.m_ch:
                return
            if ch.GetMobAttackRange() > 150:
                iNewRange = 150
                if iNewRange < 150:
                    iNewRange = 150

                ch.AddAffect(LaniatusEAffectTypes.LANIA_AFFECT_BOW_DISTANCE, EPointTypes.LG_POINT_BOW_DISTANCE, iNewRange - ch.GetMobAttackRange(), EAffectBits.AFF_NONE, 3 *60, 0, LGEMiscellaneous.DEFINECONSTANTS.false, DefineConstants.false)

class FuncPullMonster:
    def __init__(self, ch, iLength = 300):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.m_ch = None
        self.m_iLength = 0

        self.m_ch = ch
        self.m_iLength = iLength

    def functor_method(self, ent):
        if ent.IsType(EEntityTypes.ENTITY_CHARACTER):
            ch = ent
            if ch.IsPC():
                return
            if not ch.IsMonster():
                return

            fDist = Globals.DISTANCE_APPROX(self.m_ch.GetX() - ch.GetX(), self.m_ch.GetY() - ch.GetY())
            if fDist > 3000 or fDist < 100:
                return

            fNewDist = fDist - self.m_iLength
            if fNewDist < 100:
                fNewDist = 100

            degree = GetDegreeFromPositionXY(ch.GetX(), ch.GetY(), self.m_ch.GetX(), self.m_ch.GetY())
            fx = None
            fy = None

            GetDeltaByDegree(degree, fDist - fNewDist, fx, fy)
            tx = int((ch.GetX() + fx))
            ty = int((ch.GetY() + fy))

            ch.Sync(tx, ty)
            ch.Goto(tx, ty)
            ch.CalculateMoveDuration()

            ch.SyncPacket()

def ForgetMyAttacker():
    pSec = GetSectree()
    if pSec:
        f = FuncForgetMyAttacker(self)
        pSec.ForEachAround(f.functor_method)
    ReviveInvisible(5)

def AggregateMonster():
    pSec = GetSectree()
    if pSec:
        f = FuncAggregateMonster(self)
        pSec.ForEachAround(f.functor_method)

def AttractRanger():
    pSec = GetSectree()
    if pSec:
        f = FuncAttractRanger(self)
        pSec.ForEachAround(f.functor_method)

def PullMonster():
    pSec = GetSectree()
    if pSec:
        f = FuncPullMonster(self, 300)
        pSec.ForEachAround(f.functor_method)

def UpdateAggrPointEx(pAttacker, type, dam, info):
    if type == EDamageType.DAMAGE_TYPE_NORMAL_RANGE:
        dam = int((dam *1.2))

    elif type == EDamageType.DAMAGE_TYPE_RANGE:
        dam = int((dam *1.5))

    elif type == EDamageType.DAMAGE_TYPE_MAGIC:
        dam = int((dam *1.2))


    if pAttacker is GetVictim():
        dam = int((dam * 1.2))

    info.iAggro += dam

    if info.iAggro < 0:
        info.iAggro = 0

    if GetParty() and dam > 0 and type != EDamageType.DAMAGE_TYPE_SPECIAL:
        pParty = GetParty()
        iPartyAggroDist = dam

        if pParty.GetLeaderPID() == GetVID():
            iPartyAggroDist = math.trunc(iPartyAggroDist / float(2))
        else:
            iPartyAggroDist = math.trunc(iPartyAggroDist / float(3))

        pParty.SendMessage(self, EPartyMessages.PM_AGGRO_INCREASE, uint(iPartyAggroDist), pAttacker.GetVID())

    if type != EDamageType.DAMAGE_TYPE_POISON:
        ChangeVictimByAggro(info.iAggro, pAttacker)

def UpdateAggrPoint(pAttacker, type, dam):
    if IsDead() or IsStun():
        return

    it = m_map_kDamage.find(pAttacker.GetVID())

    if it == m_map_kDamage.end():
        m_map_kDamage.insert(TDamageMap.value_type(pAttacker.GetVID(), TBattleInfo(0, dam)))
        it = m_map_kDamage.find(pAttacker.GetVID())

    UpdateAggrPointEx(pAttacker, type, dam, it.second)

def ChangeVictimByAggro(iNewAggro, pNewVictim):
    if get_dword_time() - m_dwLastVictimSetTime < 3000:
        return

    if pNewVictim is GetVictim():
        if m_iMaxAggro < iNewAggro:
            m_iMaxAggro = iNewAggro
            return

        itFind = m_map_kDamage.end()

        it = m_map_kDamage.begin()
        while it is not m_map_kDamage.end():
            if it.second.iAggro > iNewAggro:
                ch = CHARACTER_MANAGER.instance().Find(it.first)

                if ch is not None and (not ch.IsDead()) and DISTANCE_APPROX(ch.GetX() - GetX(), ch.GetY() - GetY()) < 5000:
## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: itFind = it;
                    itFind.copy_from(it)
                    iNewAggro = it.second.iAggro
            it += 1

        if itFind is not m_map_kDamage.end():
            m_iMaxAggro = iNewAggro
            SetVictim(CHARACTER_MANAGER.instance().Find(itFind.first))
            m_dwStateDuration = 1
    else:
        if m_iMaxAggro < iNewAggro:
            m_iMaxAggro = iNewAggro
            SetVictim(pNewVictim)
            m_dwStateDuration = 1

