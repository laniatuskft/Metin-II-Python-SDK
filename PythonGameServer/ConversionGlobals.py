class Globals:
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
    #SendAffectAddPacket(d, pkAff)

    @staticmethod
    def CalcAttBonus(pkAttacker, pkVictim, iAtk):
        if not pkVictim.IsPC():
            iAtk += pkAttacker.GetMarriageBonus(uint(Globals.UNIQUE_ITEM_MARRIAGE_ATTACK_BONUS), ((not DefineConstants.false)))

        if not pkAttacker.IsPC():
            iReduceDamagePct = pkVictim.GetMarriageBonus(uint(Globals.UNIQUE_ITEM_MARRIAGE_TRANSFER_DAMAGE), ((not DefineConstants.false)))
            iAtk = math.trunc(iAtk * (100 + iReduceDamagePct) / float(100))

        if pkAttacker.IsNPC() and pkVictim.IsPC():
            iAtk = math.trunc((iAtk * CHARACTER_MANAGER.instance().GetMobDamageRate(pkAttacker)) / float(100))

        if pkVictim.IsNPC():
            if pkVictim.IsRaceFlag(ERaceFlags.RACE_FLAG_ANIMAL):
                iAtk += math.trunc((iAtk * pkAttacker.GetPoint(EPointTypes.LG_POINT_ATTBONUS_ANIMAL)) / float(100))
            elif pkVictim.IsRaceFlag(ERaceFlags.RACE_FLAG_UNDEAD):
                iAtk += math.trunc((iAtk * pkAttacker.GetPoint(EPointTypes.LG_POINT_ATTBONUS_UNDEAD)) / float(100))
            elif pkVictim.IsRaceFlag(ERaceFlags.RACE_FLAG_DEVIL):
                iAtk += math.trunc((iAtk * pkAttacker.GetPoint(EPointTypes.LG_POINT_ATTBONUS_DEVIL)) / float(100))
            elif pkVictim.IsRaceFlag(ERaceFlags.RACE_FLAG_HUMAN):
                iAtk += math.trunc((iAtk * pkAttacker.GetPoint(EPointTypes.LG_POINT_ATTBONUS_HUMAN)) / float(100))
            elif pkVictim.IsRaceFlag(ERaceFlags.RACE_FLAG_ORC):
                iAtk += math.trunc((iAtk * pkAttacker.GetPoint(EPointTypes.LG_POINT_ATTBONUS_ORC)) / float(100))
            elif pkVictim.IsRaceFlag(ERaceFlags.RACE_FLAG_MILGYO):
                iAtk += math.trunc((iAtk * pkAttacker.GetPoint(EPointTypes.LG_POINT_ATTBONUS_MILGYO)) / float(100))
            elif pkVictim.IsRaceFlag(ERaceFlags.RACE_FLAG_INSECT):
                iAtk += math.trunc((iAtk * pkAttacker.GetPoint(EPointTypes.LG_POINT_ATTBONUS_INSECT)) / float(100))
            elif pkVictim.IsRaceFlag(ERaceFlags.RACE_FLAG_DESERT):
                iAtk += math.trunc((iAtk * pkAttacker.GetPoint(EPointTypes.LG_POINT_ATTBONUS_DESERT)) / float(100))
            elif pkVictim.IsRaceFlag(ERaceFlags.RACE_FLAG_TREE):
                iAtk += math.trunc((iAtk * pkAttacker.GetPoint(EPointTypes.LG_POINT_ATTBONUS_TREE)) / float(100))

            if pkVictim.IsRaceFlag(ERaceFlags.RACE_FLAG_ATT_ELEC):
                iAtk += math.trunc((iAtk * pkAttacker.GetPoint(EPointTypes.LG_POINT_ENCHANT_ELEC)) / float(100))
            elif pkVictim.IsRaceFlag(ERaceFlags.RACE_FLAG_ATT_FIRE):
                iAtk += math.trunc((iAtk * pkAttacker.GetPoint(EPointTypes.LG_POINT_ENCHANT_FIRE)) / float(100))
            elif pkVictim.IsRaceFlag(ERaceFlags.RACE_FLAG_ATT_ICE):
                iAtk += math.trunc((iAtk * pkAttacker.GetPoint(EPointTypes.LG_POINT_ENCHANT_ICE)) / float(100))
            elif pkVictim.IsRaceFlag(ERaceFlags.RACE_FLAG_ATT_WIND):
                iAtk += math.trunc((iAtk * pkAttacker.GetPoint(EPointTypes.LG_POINT_ENCHANT_WIND)) / float(100))
            elif pkVictim.IsRaceFlag(ERaceFlags.RACE_FLAG_ATT_EARTH):
                iAtk += math.trunc((iAtk * pkAttacker.GetPoint(EPointTypes.LG_POINT_ENCHANT_EARTH)) / float(100))
            elif pkVictim.IsRaceFlag(ERaceFlags.RACE_FLAG_ATT_DARK):
                iAtk += math.trunc((iAtk * pkAttacker.GetPoint(EPointTypes.LG_POINT_ENCHANT_DARK)) / float(100))

            iAtk += math.trunc((iAtk * pkAttacker.GetPoint(EPointTypes.LG_POINT_ATTBONUS_MONSTER)) / float(100))
        elif pkVictim.IsPC():
            iAtk += math.trunc((iAtk * pkAttacker.GetPoint(EPointTypes.LG_POINT_ATTBONUS_HUMAN)) / float(100))

            if pkVictim.GetJob() == EJobs.JOB_LG_PAWN_WARRIOR:
                iAtk += math.trunc((iAtk * pkAttacker.GetPoint(EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_WARRIOR)) / float(100))

            elif pkVictim.GetJob() == EJobs.JOB_LG_PAWN_ASSASSIN:
                iAtk += math.trunc((iAtk * pkAttacker.GetPoint(EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_ASSASSIN)) / float(100))

            elif pkVictim.GetJob() == EJobs.JOB_LG_PAWN_SHURA:
                iAtk += math.trunc((iAtk * pkAttacker.GetPoint(EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_SHURA)) / float(100))

            elif pkVictim.GetJob() == EJobs.JOB_LG_PAWN_MAGE:
                iAtk += math.trunc((iAtk * pkAttacker.GetPoint(EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_MAGE)) / float(100))
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##if ENABLE_WOLFMAN
            elif pkVictim.GetJob() == EJobs.JOB_WOLFMAN:
                iAtk += math.trunc((iAtk * pkAttacker.GetPoint(EPointTypes.LG_POINT_ATTBONUS_WOLFMAN)) / float(100))
    ##endif

        if pkAttacker.IsPC() == ((not LGEMiscellaneous.DEFINECONSTANTS.false)):
            iAtk -= math.trunc((iAtk * pkVictim.GetPoint(EPointTypes.LG_POINT_RESIST_HUMAN)) / float(100))

            if pkAttacker.GetJob() == EJobs.JOB_LG_PAWN_WARRIOR:
                iAtk -= math.trunc((iAtk * pkVictim.GetPoint(EPointTypes.LG_POINT_RESIST_LG_PAWN_WARRIOR)) / float(100))

            elif pkAttacker.GetJob() == EJobs.JOB_LG_PAWN_ASSASSIN:
                iAtk -= math.trunc((iAtk * pkVictim.GetPoint(EPointTypes.LG_POINT_RESIST_LG_PAWN_ASSASSIN)) / float(100))

            elif pkAttacker.GetJob() == EJobs.JOB_LG_PAWN_SHURA:
                iAtk -= math.trunc((iAtk * pkVictim.GetPoint(EPointTypes.LG_POINT_RESIST_LG_PAWN_SHURA)) / float(100))

            elif pkAttacker.GetJob() == EJobs.JOB_LG_PAWN_MAGE:
                iAtk -= math.trunc((iAtk * pkVictim.GetPoint(EPointTypes.LG_POINT_RESIST_LG_PAWN_MAGE)) / float(100))

    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##if ENABLE_WOLFMAN
            elif pkAttacker.GetJob() == EJobs.JOB_WOLFMAN:
                iAtk -= math.trunc((iAtk * pkVictim.GetPoint(EPointTypes.LG_POINT_RESIST_WOLFMAN)) / float(100))
    ##endif

        if pkAttacker.IsNPC() and pkVictim.IsPC():
            if pkAttacker.IsRaceFlag(ERaceFlags.RACE_FLAG_ATT_ELEC):
                iAtk -= math.trunc((iAtk * 30 * pkVictim.GetPoint(EPointTypes.LG_POINT_RESIST_ELEC)) / float(10000))
            elif pkAttacker.IsRaceFlag(ERaceFlags.RACE_FLAG_ATT_FIRE):
                iAtk -= math.trunc((iAtk * 30 * pkVictim.GetPoint(EPointTypes.LG_POINT_RESIST_FIRE)) / float(10000))
            elif pkAttacker.IsRaceFlag(ERaceFlags.RACE_FLAG_ATT_ICE):
                iAtk -= math.trunc((iAtk * 30 * pkVictim.GetPoint(EPointTypes.LG_POINT_RESIST_ICE)) / float(10000))
            elif pkAttacker.IsRaceFlag(ERaceFlags.RACE_FLAG_ATT_WIND):
                iAtk -= math.trunc((iAtk * 30 * pkVictim.GetPoint(EPointTypes.LG_POINT_RESIST_WIND)) / float(10000))
            elif pkAttacker.IsRaceFlag(ERaceFlags.RACE_FLAG_ATT_EARTH):
                iAtk -= math.trunc((iAtk * 30 * pkVictim.GetPoint(EPointTypes.LG_POINT_RESIST_EARTH)) / float(10000))
            elif pkAttacker.IsRaceFlag(ERaceFlags.RACE_FLAG_ATT_DARK):
                iAtk -= math.trunc((iAtk * 30 * pkVictim.GetPoint(EPointTypes.LG_POINT_RESIST_DARK)) / float(10000))


        return iAtk

    @staticmethod
    def CalcBattleDamage(iDam, iAttackerLev, iVictimLev):
        if iDam < 3:
            iDam = number(1, 5)

        return iDam

    @staticmethod
    def CalcMeleeDamage(pkAttacker, pkVictim, bIgnoreDefense = LGEMiscellaneous.DefineConstants.false, bIgnoreTargetRating = LGEMiscellaneous.DefineConstants.false):
        pWeapon = pkAttacker.GetWear(EWearPositions.WEAR_WEAPON)
        pAcce = pkAttacker.GetWear(EWearPositions.WEAR_COSTUME_ACCE)
        bPolymorphed = pkAttacker.IsPolymorphed()

        if pWeapon is not None and not(bPolymorphed and (not pkAttacker.IsPolyMaintainStat())):
            if pWeapon.GetType() != EItemTypes.ITEM_WEAPON:
                return 0

            if (pWeapon.GetSubType() == EWeaponSubTypes.WEAPON_SWORD) or (pWeapon.GetSubType() == EWeaponSubTypes.WEAPON_DAGGER) or (pWeapon.GetSubType() == EWeaponSubTypes.WEAPON_TWO_HANDED) or (pWeapon.GetSubType() == EWeaponSubTypes.WEAPON_BELL) or (pWeapon.GetSubType() == EWeaponSubTypes.WEAPON_FAN) or (pWeapon.GetSubType() == EWeaponSubTypes.WEAPON_MOUNT_SPEAR):
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##if ENABLE_WOLFMAN
            if (pWeapon.GetSubType() == EWeaponSubTypes.WEAPON_SWORD) or (pWeapon.GetSubType() == EWeaponSubTypes.WEAPON_DAGGER) or (pWeapon.GetSubType() == EWeaponSubTypes.WEAPON_TWO_HANDED) or (pWeapon.GetSubType() == EWeaponSubTypes.WEAPON_BELL) or (pWeapon.GetSubType() == EWeaponSubTypes.WEAPON_FAN) or (pWeapon.GetSubType() == EWeaponSubTypes.WEAPON_MOUNT_SPEAR) or (pWeapon.GetSubType() == EWeaponSubTypes.WEAPON_CLAW):
    ##endif

            elif pWeapon.GetSubType() == EWeaponSubTypes.WEAPON_BOW:
                #lani_err("CalcMeleeDamage should not handle bows (name: %s)", pkAttacker.GetName(LOCALE_LANIATUS))
                return 0


            if pWeapon.GetSubType() != WEAPON_SWORD and pWeapon.GetSubType() != WEAPON_DAGGER and pWeapon.GetSubType() != WEAPON_TWO_HANDED and pWeapon.GetSubType() != WEAPON_BELL and pWeapon.GetSubType() != WEAPON_FAN and pWeapon.GetSubType() != WEAPON_MOUNT_SPEAR and pWeapon.GetSubType() != WEAPON_CLAW:
                return 0

        iDam = 0
        fAR = Globals.CalcAttackRating(pkAttacker, pkVictim, bIgnoreTargetRating)
        iDamMin = 0
        iDamMax = 0

        DEBUG_iDamCur = 0
        DEBUG_iDamBonus = 0

        if bPolymorphed and not pkAttacker.IsPolyMaintainStat():
            temp_ref_iDamMin = RefObject(iDamMin);
            temp_ref_iDamMax = RefObject(iDamMax);
            Globals.Item_GetDamage(pWeapon, temp_ref_iDamMin, temp_ref_iDamMax)
            iDamMax = temp_ref_iDamMax.arg_value
            iDamMin = temp_ref_iDamMin.arg_value

            dwMobVnum = pkAttacker.GetPolymorphVnum()
            pMob = CMobManager.instance().Get(dwMobVnum)

            if pMob:
                iPower = pkAttacker.GetPolymorphPower()
                iDamMin += math.trunc(pMob.m_table.dwDamageRange[0] * iPower / float(100))
                iDamMax += math.trunc(pMob.m_table.dwDamageRange[1] * iPower / float(100))
        elif pWeapon:
            temp_ref_iDamMin2 = RefObject(iDamMin);
            temp_ref_iDamMax2 = RefObject(iDamMax);
            Globals.Item_GetDamage(pWeapon, temp_ref_iDamMin2, temp_ref_iDamMax2)
            iDamMax = temp_ref_iDamMax2.arg_value
            iDamMin = temp_ref_iDamMin2.arg_value
        elif pkAttacker.IsNPC():
            iDamMin = int(pkAttacker.GetMobDamageMin())
            iDamMax = int(pkAttacker.GetMobDamageMax())
        if pAcce is not None and pAcce.GetType() == EItemTypes.ITEM_COSTUME and pAcce.GetSubType() == ECostumeSubTypes.COSTUME_ACCE and pAcce.GetSocket(1) > 0:
            p = ITEM_MANAGER.instance().GetTable(uint(pAcce.GetSocket(1)))
            if p is not None and p.bType == EItemTypes.ITEM_WEAPON:
                iDamMin += int(float(p.alValues[3]) / 100.0 * pAcce.GetSocket(0))
                iDamMax += int(float(p.alValues[4]) / 100.0 * pAcce.GetSocket(0))

        iDam = number(iDamMin, iDamMax) * 2
        DEBUG_iDamCur = iDam
        iAtk = 0

        iAtk = int(pkAttacker.GetPoint(EPointTypes.LG_POINT_ATT_GRADE) + iDam - (pkAttacker.GetLevel() * 2))
        iAtk = int((iAtk * fAR))
        iAtk += pkAttacker.GetLevel() * 2

        if pWeapon:
            iAtk += pWeapon.GetValue(5) * 2
            DEBUG_iDamBonus = pWeapon.GetValue(5) * 2

        if pAcce is not None and pAcce.GetType() == EItemTypes.ITEM_COSTUME and pAcce.GetSubType() == ECostumeSubTypes.COSTUME_ACCE and pAcce.GetSocket(1) > 0:
            p = ITEM_MANAGER.instance().GetTable(uint(pAcce.GetSocket(1)))
            if p is not None and p.bType == EItemTypes.ITEM_WEAPON:
                iAtk += int((float(p.alValues[5]) / 100.0 * float(pAcce.GetSocket(0))) * 2)

        iAtk += int(pkAttacker.GetPoint(EPointTypes.LG_POINT_PARTY_ATTACKER_BONUS))
        iAtk = int((math.trunc(iAtk * (100 + (pkAttacker.GetPoint(EPointTypes.LG_POINT_ATT_BONUS) + pkAttacker.GetPoint(EPointTypes.LG_POINT_MELEE_MAGIC_ATT_BONUS_PER))) / float(100))))

        iAtk = Globals.CalcAttBonus(pkAttacker, pkVictim, iAtk)

        iDef = 0

        if not bIgnoreDefense:
            iDef = (math.trunc(pkVictim.GetPoint(EPointTypes.LG_POINT_DEF_GRADE) * (100 + pkVictim.GetPoint(EPointTypes.LG_POINT_DEF_BONUS)) / float(100)))

            if not pkAttacker.IsPC():
                iDef += pkVictim.GetMarriageBonus(uint(Globals.UNIQUE_ITEM_MARRIAGE_DEFENSE_BONUS), ((not DefineConstants.false)))

        if pkAttacker.IsNPC():
            iAtk = int((iAtk * pkAttacker.GetMobDamageMultiply()))

        iDam = MAX(0, iAtk - iDef)

        if test_server:
            DEBUG_iLV = pkAttacker.GetLevel()*2
            DEBUG_iST = int((pkAttacker.GetPoint(EPointTypes.LG_POINT_ATT_GRADE) - DEBUG_iLV) * fAR)
            DEBUG_iPT = int(pkAttacker.GetPoint(EPointTypes.LG_POINT_PARTY_ATTACKER_BONUS))
            DEBUG_iWP = 0
            DEBUG_iPureAtk = 0
            DEBUG_iPureDam = 0
            szRB = ""
            szGradeAtkBonus = ""

            DEBUG_iWP = int((DEBUG_iDamCur * fAR))
            DEBUG_iPureAtk = DEBUG_iLV + DEBUG_iST + DEBUG_iWP+DEBUG_iDamBonus
            DEBUG_iPureDam = iAtk - iDef

            if pkAttacker.IsNPC():
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                snprintf(szGradeAtkBonus, sizeof(szGradeAtkBonus), "=%d*%.1f", DEBUG_iPureAtk, pkAttacker.GetMobDamageMultiply())
                DEBUG_iPureAtk = int((DEBUG_iPureAtk * pkAttacker.GetMobDamageMultiply()))

            if DEBUG_iDamBonus != 0:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                snprintf(szRB, sizeof(szRB), "+RB(%d)", DEBUG_iDamBonus)

            szPT = ""

            if DEBUG_iPT != 0:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                snprintf(szPT, sizeof(szPT), ", PT=%d", DEBUG_iPT)

            szUnknownAtk = ""

            if iAtk != DEBUG_iPureAtk:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                snprintf(szUnknownAtk, sizeof(szUnknownAtk), "+?(%d)", iAtk-DEBUG_iPureAtk)

            szUnknownDam = ""

            if iDam != DEBUG_iPureDam:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                snprintf(szUnknownDam, sizeof(szUnknownDam), "+?(%d)", iDam-DEBUG_iPureDam)

            szMeleeAttack = str(['\0' for _ in range(128)])

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            snprintf(szMeleeAttack, sizeof(szMeleeAttack), "%s(%d)-%s(%d)=%d%s, ATK=LV(%d)+ST(%d)+WP(%d)%s%s%s, AR=%.3g%s", pkAttacker.GetName(LOCALE_LANIATUS), iAtk, pkVictim.GetName(LOCALE_LANIATUS), iDef, iDam, szUnknownDam, DEBUG_iLV, DEBUG_iST, DEBUG_iWP, szRB, szUnknownAtk, szGradeAtkBonus, fAR, szPT)

            pkAttacker.ChatPacket(EChatType.CHAT_TYPE_TALKING, "%s", szMeleeAttack)
            pkVictim.ChatPacket(EChatType.CHAT_TYPE_TALKING, "%s", szMeleeAttack)

        return Globals.CalcBattleDamage(iDam, pkAttacker.GetLevel(), pkVictim.GetLevel())

    @staticmethod
    def CalcMagicDamage(pkAttacker, pkVictim):
        iDam = 0

        if pkAttacker.IsNPC():
            iDam = Globals.CalcMeleeDamage(pkAttacker, pkVictim, LGEMiscellaneous.DEFINECONSTANTS.false, LGEMiscellaneous.DEFINECONSTANTS.false)

        iDam += int(pkAttacker.GetPoint(EPointTypes.LG_POINT_PARTY_ATTACKER_BONUS))

        return Globals.CalcMagicDamageWithValue(iDam, pkAttacker, pkVictim)

    @staticmethod
    def CalcArrowDamage(pkAttacker, pkVictim, pkBow, pkArrow, bIgnoreDefense = LGEMiscellaneous.DefineConstants.false):
        if pkBow is None or pkBow.GetType() != EItemTypes.ITEM_WEAPON or pkBow.GetSubType() != EWeaponSubTypes.WEAPON_BOW:
            return 0

        if pkArrow is None:
            return 0

        iDist = int(Globals.DISTANCE_SQRT(pkAttacker.GetX() - pkVictim.GetX(), pkAttacker.GetY() - pkVictim.GetY()))
        iGap = (math.trunc(iDist / float(100))) - 5 - pkAttacker.GetPoint(EPointTypes.LG_POINT_BOW_DISTANCE)
        iPercent = 100 - (iGap * 5)

        if pkArrow.GetSubType() == EWeaponSubTypes.WEAPON_QUIVER:
            iPercent = 100


        if iPercent <= 0:
            return 0
        elif iPercent > 100:
            iPercent = 100

        iDam = 0

        fAR = Globals.CalcAttackRating(pkAttacker, pkVictim, LGEMiscellaneous.DEFINECONSTANTS.false)
        iDam = number(pkBow.GetValue(3), pkBow.GetValue(4)) * 2 + pkArrow.GetValue(3)
        iAtk = None

        iAtk = int(pkAttacker.GetPoint(EPointTypes.LG_POINT_ATT_GRADE) + iDam - (pkAttacker.GetLevel() * 2))
        iAtk = int((iAtk * fAR))
        iAtk += pkAttacker.GetLevel() * 2

        iAtk += pkBow.GetValue(5) * 2

        iAtk += int(pkAttacker.GetPoint(EPointTypes.LG_POINT_PARTY_ATTACKER_BONUS))
        iAtk = int((math.trunc(iAtk * (100 + (pkAttacker.GetPoint(EPointTypes.LG_POINT_ATT_BONUS) + pkAttacker.GetPoint(EPointTypes.LG_POINT_MELEE_MAGIC_ATT_BONUS_PER))) / float(100))))

        iAtk = Globals.CalcAttBonus(pkAttacker, pkVictim, iAtk)

        iDef = 0

        if not bIgnoreDefense:
            iDef = (math.trunc(pkVictim.GetPoint(EPointTypes.LG_POINT_DEF_GRADE) * (100 + pkAttacker.GetPoint(EPointTypes.LG_POINT_DEF_BONUS)) / float(100)))

        if pkAttacker.IsNPC():
            iAtk = int((iAtk * pkAttacker.GetMobDamageMultiply()))

        iDam = MAX(0, iAtk - iDef)

        iPureDam = iDam

        iPureDam = math.trunc((iPureDam * iPercent) / float(100))

        if test_server:
            pkAttacker.ChatPacket(EChatType.CHAT_TYPE_INFO, "ARROW %s -> %s, DAM %d DIST %d GAP %d %% %d", pkAttacker.GetName(LOCALE_LANIATUS), pkVictim.GetName(LOCALE_LANIATUS), iPureDam, iDist, iGap, iPercent)

        return iPureDam

    @staticmethod
    def CalcAttackRating(pkAttacker, pkVictim, bIgnoreTargetRating = LGEMiscellaneous.DefineConstants.false):
        iARSrc = None
        iERSrc = None

        attacker_dx = pkAttacker.GetPolymorphPoint(EPointTypes.LG_POINT_DX)
        attacker_lv = pkAttacker.GetLevel()

        victim_dx = pkVictim.GetPolymorphPoint(EPointTypes.LG_POINT_DX)
        victim_lv = pkAttacker.GetLevel()

        iARSrc = MIN(90, math.trunc((attacker_dx * 4 + attacker_lv * 2) / float(6)))
        iERSrc = MIN(90, math.trunc((victim_dx * 4 + victim_lv * 2) / float(6)))

        fAR = (float(iARSrc) + 210.0) / 300.0

        if bIgnoreTargetRating:
            return fAR

        fER = (float((iERSrc * 2 + 5)) / (iERSrc + 95)) * 3.0 / 10.0

        return fAR - fER

    @staticmethod
    def battle_is_attackable(ch, victim):
        if victim.IsDead():
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if victim.IsObserverMode():
            return LGEMiscellaneous.DEFINECONSTANTS.false

            sectree = None

            sectree = ch.GetSectree()
            if sectree is not None and sectree.IsAttr(ch.GetX(), ch.GetY(), uint(Globals.ATTR_BANPK)):
                return LGEMiscellaneous.DEFINECONSTANTS.false

            sectree = victim.GetSectree()
            if sectree is not None and sectree.IsAttr(victim.GetX(), victim.GetY(), uint(Globals.ATTR_BANPK)):
                return LGEMiscellaneous.DEFINECONSTANTS.false

        if ch.IsStun() or ch.IsDead():
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if ch.IsPC() and victim.IsPC():
            g1 = ch.GetGuild()
            g2 = victim.GetGuild()

            if g1 is not None and g2 is not None:
                if g1.UnderWar(g2.GetID()):
                    return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        return CPVPManager.instance().CanAttack(ch, victim)

    @staticmethod
    def battle_melee_attack(ch, victim):
        if test_server and ch.IsPC():
            #sys_log(0, "battle_melee_attack : [%s] attack to [%s]", ch.GetName(LOCALE_LANIATUS), victim.GetName(LOCALE_LANIATUS))

        if victim is None or ch is victim:
            return EBattleTypes.BATTLE_NONE

        if test_server and ch.IsPC():
            #sys_log(0, "battle_melee_attack : [%s] attack to [%s]", ch.GetName(LOCALE_LANIATUS), victim.GetName(LOCALE_LANIATUS))

        if not Globals.battle_is_attackable(ch, victim):
            return EBattleTypes.BATTLE_NONE

        if test_server and ch.IsPC():
            #sys_log(0, "battle_melee_attack : [%s] attack to [%s]", ch.GetName(LOCALE_LANIATUS), victim.GetName(LOCALE_LANIATUS))

        distance = Globals.DISTANCE_APPROX(ch.GetX() - victim.GetX(), ch.GetY() - victim.GetY())

        if not victim.IsBuilding():
            max = 325

            if LGEMiscellaneous.DEFINECONSTANTS.false == ch.IsPC():
                max = int((ch.GetMobAttackRange() * 1.15))
            else:
                if LGEMiscellaneous.DEFINECONSTANTS.false == victim.IsPC() and EBattleType.BATTLE_TYPE_MELEE == victim.GetMobBattleType():
                    max = MAX(300, int((victim.GetMobAttackRange() * 1.15)))

            if distance > max:
                if test_server:
                    #sys_log(0, "VICTIM_FAR: %s distance: %d max: %d", ch.GetName(LOCALE_LANIATUS), distance, max)

                return EBattleTypes.BATTLE_NONE

        if Globals.timed_event_cancel(ch):
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Cancelled. The Battle did not begin."))

        if Globals.timed_event_cancel(victim):
            victim.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Cancelled. The Battle did not begin."))

        ch.SetPosition(EPositions.POS_FIGHTING)
        ch.SetVictim(victim)

        vpos = victim.GetXYZ()
        ch.SetRotationToXY(vpos.x, vpos.y)

        dam = None
        ret = Globals.battle_hit(ch, victim, dam)
        return (ret)

    @staticmethod
    def battle_end(ch):
        Globals.battle_end_ex(ch)

    @staticmethod
    def battle_distance_valid_by_xy(x, y, tx, ty):
        distance = Globals.DISTANCE_APPROX(x - tx, y - ty)

        if distance > 170:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    @staticmethod
    def battle_distance_valid(ch, victim):
        return Globals.battle_distance_valid_by_xy(ch.GetX(), ch.GetY(), victim.GetX(), victim.GetY())

    @staticmethod
    def NormalAttackAffect(pkAttacker, pkVictim):
        if pkAttacker.GetPoint(EPointTypes.LG_POINT_POISON_PCT) != 0 and not pkVictim.IsAffectFlag(EAffectBits.AFF_POISON):
            if number(1, 100) <= pkAttacker.GetPoint(EPointTypes.LG_POINT_POISON_PCT):
                pkVictim.AttackedByPoison(pkAttacker)

    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##if ENABLE_WOLFMAN
        if pkAttacker.GetPoint(EPointTypes.LG_POINT_BLEEDING_PCT) != 0 and not pkVictim.IsAffectFlag(EAffectBits.AFF_BLEEDING):
            if number(1, 100) <= pkAttacker.GetPoint(EPointTypes.LG_POINT_BLEEDING_PCT):
                pkVictim.AttackedByBleeding(pkAttacker)
    ##endif

        iStunDuration = 2
        if pkAttacker.IsPC() and not pkVictim.IsPC():
            iStunDuration = 4

        Globals.AttackAffect(pkAttacker, pkVictim, EPointTypes.LG_POINT_STUN_PCT, EImmuneFlags.IMMUNE_STUN, LaniatusEAffectTypes.LANIA_AFFECT_STUN, EPointTypes.LG_POINT_NONE, 0, EAffectBits.AFF_STUN, iStunDuration, "STUN")
        Globals.AttackAffect(pkAttacker, pkVictim, EPointTypes.LG_POINT_SLOW_PCT, EImmuneFlags.IMMUNE_SLOW, LaniatusEAffectTypes.LANIA_AFFECT_SLOW, EPointTypes.LG_POINT_MOV_SPEED, -30, EAffectBits.AFF_SLOW, 20, "SLOW")

    @staticmethod
    def AttackAffect(pkAttacker, pkVictim, att_point, immune_flag, affect_idx, affect_point, affect_amount, affect_flag, time, name):
        if pkAttacker.GetPoint(att_point) != 0 and not pkVictim.IsAffectFlag(affect_flag):
            if number(1, 100) <= pkAttacker.GetPoint(att_point) and not pkVictim.IsImmune(immune_flag):
                pkVictim.AddAffect(affect_idx, affect_point, affect_amount, affect_flag, time, 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), DefineConstants.false)

                if test_server:
                    pkVictim.ChatPacket(EChatType.CHAT_TYPE_PARTY, "%s %s(%ld%%) SUCCESS", pkAttacker.GetName(LOCALE_LANIATUS), name, pkAttacker.GetPoint(att_point))
            elif test_server:
                pkVictim.ChatPacket(EChatType.CHAT_TYPE_PARTY, "%s %s(%ld%%) FAIL", pkAttacker.GetName(LOCALE_LANIATUS), name, pkAttacker.GetPoint(att_point))

    @staticmethod
    def SkillAttackAffect(pkVictim, success_pct, immune_flag, affect_idx, affect_point, affect_amount, affect_flag, time, name):
        if success_pct != 0 and not pkVictim.IsAffectFlag(affect_flag):
            if number(1, 1000) <= success_pct and not pkVictim.IsImmune(immune_flag):
                pkVictim.AddAffect(affect_idx, affect_point, affect_amount, affect_flag, time, 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), DefineConstants.false)

                if test_server:
                    pkVictim.ChatPacket(EChatType.CHAT_TYPE_PARTY, "%s(%d%%) -> %s SUCCESS", name, success_pct, name)
            elif test_server:
                pkVictim.ChatPacket(EChatType.CHAT_TYPE_PARTY, "%s(%d%%) -> %s FAIL", name, success_pct, name)

    ## Laniatus Games Studio Inc. | NOTE: The following #define macro was replaced in-line:
    #ORIGINAL METINII C CODE: #define GET_SPEED_HACK_COUNT(ch) ((ch)->m_speed_hack_count)
    ## Laniatus Games Studio Inc. | NOTE: The following #define macro was replaced in-line:
    #ORIGINAL METINII C CODE: #define INCREASE_SPEED_HACK_COUNT(ch) (++GET_SPEED_HACK_COUNT(ch))
    @staticmethod
    def GET_ATTACK_SPEED(ch):
        if None is ch:
            return 1000

        item = ch.GetWear(EWearPositions.WEAR_WEAPON)
        default_bonus = SPEEDHACK_LIMIT_BONUS
        riding_bonus = 0

        if ch.IsRiding():
            riding_bonus = 50

        ani_speed = Globals.ani_attack_speed(ch)
        real_speed = math.trunc((ani_speed * 100) / float(default_bonus + ch.GetPoint(EPointTypes.LG_POINT_ATT_SPEED) + riding_bonus))

        if item is not None and item.GetSubType() == EWeaponSubTypes.WEAPON_DAGGER:
            real_speed = math.trunc(real_speed / float(2))

    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##if ENABLE_WOLFMAN
        if item is not None and item.GetSubType() == EWeaponSubTypes.WEAPON_CLAW:
            real_speed = math.trunc(real_speed / float(2))
    ##endif

        return real_speed


    @staticmethod
    def SET_ATTACK_TIME(ch, victim, current_time):
        if None is ch or None is victim:
            return

        if not ch.IsPC():
            return

        ch.m_kAttackLog.dwVID = victim.GetVID()
        ch.m_kAttackLog.dwTime = current_time

    @staticmethod
    def SET_ATTACKED_TIME(ch, victim, current_time):
        if None is ch or None is victim:
            return

        if not ch.IsPC():
            return

        victim.m_AttackedLog.dwPID = ch.GetPlayerID()
        victim.m_AttackedLog.dwAttackedTime = current_time

    @staticmethod
    def IS_SPEED_HACK(ch, victim, current_time):
        if ch.m_kAttackLog.dwVID == victim.GetVID():
            if current_time - ch.m_kAttackLog.dwTime < Globals.GET_ATTACK_SPEED(ch):
                (++((ch).m_speed_hack_count))

                if test_server:
                    #sys_log(0, "%s attack hack! time (delta, limit)=(%u, %u) hack_count %d", ch.GetName(LOCALE_LANIATUS), current_time - ch.m_kAttackLog.dwTime, Globals.GET_ATTACK_SPEED(ch), ch.m_speed_hack_count)

                    ch.ChatPacket(EChatType.CHAT_TYPE_INFO, "%s attack hack! time (delta, limit)=(%u, %u) hack_count %d", ch.GetName(LOCALE_LANIATUS), current_time - ch.m_kAttackLog.dwTime, Globals.GET_ATTACK_SPEED(ch), ch.m_speed_hack_count)

                Globals.SET_ATTACK_TIME(ch, victim, current_time)
                Globals.SET_ATTACKED_TIME(ch, victim, current_time)
                return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        Globals.SET_ATTACK_TIME(ch, victim, current_time)

        if victim.m_AttackedLog.dwPID == ch.GetPlayerID():
            if current_time - victim.m_AttackedLog.dwAttackedTime < Globals.GET_ATTACK_SPEED(ch):
                (++((ch).m_speed_hack_count))

                if test_server:
                    #sys_log(0, "%s Attack Speed HACK! time (delta, limit)=(%u, %u), hack_count = %d", ch.GetName(LOCALE_LANIATUS), current_time - victim.m_AttackedLog.dwAttackedTime, Globals.GET_ATTACK_SPEED(ch), ch.m_speed_hack_count)

                    ch.ChatPacket(EChatType.CHAT_TYPE_INFO, "Attack Speed Hack(%s), (delta, limit)=(%u, %u)", ch.GetName(LOCALE_LANIATUS), current_time - victim.m_AttackedLog.dwAttackedTime, Globals.GET_ATTACK_SPEED(ch))

                Globals.SET_ATTACKED_TIME(ch, victim, current_time)
                return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        Globals.SET_ATTACKED_TIME(ch, victim, current_time)
        return LGEMiscellaneous.DEFINECONSTANTS.false


    @staticmethod
    def battle_hit(pkAttacker, pkVictim, iRetDam):
        if test_server:
            #sys_log(0, "battle_hit : [%s] attack to [%s] : dam :%d type :%d", pkAttacker.GetName(LOCALE_LANIATUS), pkVictim.GetName(LOCALE_LANIATUS), iRetDam.arg_value)

        iDam = Globals.CalcMeleeDamage(pkAttacker, pkVictim, DefineConstants.false, DefineConstants.false)

        if iDam <= 0:
            return (EBattleTypes.BATTLE_DAMAGE)

        Globals.NormalAttackAffect(pkAttacker, pkVictim)

        pkWeapon = pkAttacker.GetWear(EWearPositions.WEAR_WEAPON)

        if pkWeapon:
            if pkWeapon.GetSubType() == EWeaponSubTypes.WEAPON_SWORD:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
                iDam = int(iDam * (100 - pkVictim.GetPoint(EPointTypes.LG_POINT_RESIST_SWORD)) / 100)

            elif pkWeapon.GetSubType() == EWeaponSubTypes.WEAPON_TWO_HANDED:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
                iDam = int(iDam * (100 - pkVictim.GetPoint(EPointTypes.LG_POINT_RESIST_TWOHAND)) / 100)

            elif pkWeapon.GetSubType() == EWeaponSubTypes.WEAPON_DAGGER:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
                iDam = int(iDam * (100 - pkVictim.GetPoint(EPointTypes.LG_POINT_RESIST_DAGGER)) / 100)

            elif pkWeapon.GetSubType() == EWeaponSubTypes.WEAPON_BELL:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
                iDam = int(iDam * (100 - pkVictim.GetPoint(EPointTypes.LG_POINT_RESIST_BELL)) / 100)

            elif pkWeapon.GetSubType() == EWeaponSubTypes.WEAPON_FAN:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
                iDam = int(iDam * (100 - pkVictim.GetPoint(EPointTypes.LG_POINT_RESIST_FAN)) / 100)

            elif pkWeapon.GetSubType() == EWeaponSubTypes.WEAPON_BOW:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
                iDam = int(iDam * (100 - pkVictim.GetPoint(EPointTypes.LG_POINT_RESIST_BOW)) / 100)

    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##if ENABLE_WOLFMAN
            elif pkWeapon.GetSubType() == EWeaponSubTypes.WEAPON_CLAW:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
                iDam = int(iDam * (100 - pkVictim.GetPoint(EPointTypes.LG_POINT_RESIST_CLAW)) / 100)
    ##endif

        attMul = pkAttacker.GetAttMul()
        tempIDam = iDam
        iDam = int(attMul * tempIDam + 0.5)

        iRetDam.arg_value = iDam

        if pkVictim.Damage(pkAttacker, iDam, EDamageType.DAMAGE_TYPE_NORMAL):
            return (EBattleTypes.BATTLE_DEAD)

        return (EBattleTypes.BATTLE_DAMAGE)


    @staticmethod
    def timed_event_cancel(ch):
        if ch.m_pkTimedEvent:
            Globals.event_cancel(ch.m_pkTimedEvent)
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        return LGEMiscellaneous.DEFINECONSTANTS.false

    @staticmethod
    def battle_end_ex(ch):
        if ch.IsPosition(EPositions.POS_FIGHTING):
            ch.SetPosition(EPositions.POS_STANDING)

    @staticmethod
    def CalcMagicDamageWithValue(iDam, pkAttacker, pkVictim):
        return Globals.CalcBattleDamage(iDam, pkAttacker.GetLevel(), pkVictim.GetLevel())

    @staticmethod
    def Item_GetDamage(pkItem, pdamMin, pdamMax):
        pdamMin.arg_value = None
        pdamMax.arg_value = 1

        if pkItem is None:
            return

        if (pkItem.GetType() == EItemTypes.ITEM_ROD) or (pkItem.GetType() == EItemTypes.ITEM_PICK):
            return

        if pkItem.GetType() != EItemTypes.ITEM_WEAPON:
            #lani_err("Item_GetDamage - !ITEM_WEAPON vnum=%d, type=%d", pkItem.GetOriginalVnum(), pkItem.GetType())

        pdamMin.arg_value = pkItem.GetValue(3)
        pdamMax.arg_value = pkItem.GetValue(4)



    ##define _blend_item_cpp_


    @staticmethod
    def Blend_Item_init():
        blend_item_info = None
        iter = None
        file_name = str(['\0' for _ in range(256)])
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        snprintf(file_name, sizeof(file_name), "%s/blend.txt", Globals.LocaleService_GetBasePath())

        Globals.#sys_log(0, "Blend_Item_init %s ", file_name)

        iter = s_blend_info.begin()
        while iter is not Globals.s_blend_info.end():
            blend_item_info = *iter
            LG_DEL_MEM(blend_item_info)
            iter += 1
        Globals.s_blend_info.clear()

        temp_ref_file_name = RefObject(file_name);
        if LGEMiscellaneous.DEFINECONSTANTS.false==Globals.Blend_Item_load(temp_ref_file_name):
            file_name = temp_ref_file_name.arg_value
            #lani_err("<Blend_Item_init> fail")
            return LGEMiscellaneous.DEFINECONSTANTS.false
        else:
            file_name = temp_ref_file_name.arg_value
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    @staticmethod
    def Blend_Item_load(file):
        fp = None
        one_line = str(['\0' for _ in range(256)])
        delim = " \t\r\n"
        v = None

        blend_item_info = LG_NEW_M2 BLEND_ITEM_INFO

        if None==file.arg_value or None==file.arg_value[0]:
            return LGEMiscellaneous.DEFINECONSTANTS.false

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((fp = fopen(file, "r"))==0)
        if (fp = fopen(file.arg_value, "r")) is None:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        while fgets(one_line, 256, fp):
            if one_line[0]=='#':
                continue

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to pointers to value types:
#ORIGINAL METINII C CODE: const char* token_string = strtok(one_line, delim);
            token_string = strtok(one_line, delim)

            if None==token_string:
                continue

            TOKEN("section")
                blend_item_info = LG_NEW_M2 BLEND_ITEM_INFO
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                memset(blend_item_info, 0x00, sizeof(BLEND_ITEM_INFO))
            else:
                TOKEN("item_vnum")
                v = strtok(None, delim)

                if None==v:
                    fclose(fp)
                    return LGEMiscellaneous.DEFINECONSTANTS.false

                temp_ref_item_vnum = RefObject(blend_item_info.item_vnum);
                Globals.str_to_number(temp_ref_item_vnum, v)
                blend_item_info.item_vnum = temp_ref_item_vnum.arg_value
            else:
                TOKEN("apply_type")
                v = strtok(None, delim)

                if None==v:
                    fclose(fp)
                    return LGEMiscellaneous.DEFINECONSTANTS.false

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if (0 == (blend_item_info->apply_type = FN_get_apply_type(v)))
                if 0 == (blend_item_info.apply_type = Globals.FN_get_apply_type(v)):
                    #lani_err("Invalid apply_type(%s)", v)
                    return LGEMiscellaneous.DEFINECONSTANTS.false
            else:
                TOKEN("apply_value")
                for i in range(0, LGEMiscellaneous.DEFINECONSTANTS.MAX_BLEND_ITEM_VALUE):
                    v = strtok(None, delim)

                    if None==v:
                        fclose(fp)
                        return LGEMiscellaneous.DEFINECONSTANTS.false

                    Globals.str_to_number(ushort(short(1 if blend_item_info.apply_value[i] != 0 else 0)), v)
            else:
                TOKEN("apply_duration")
                for i in range(0, LGEMiscellaneous.DEFINECONSTANTS.MAX_BLEND_ITEM_VALUE):
                    v = strtok(None, delim)

                    if None==v:
                        fclose(fp)
                        return LGEMiscellaneous.DEFINECONSTANTS.false

                    Globals.str_to_number(ushort(short(1 if blend_item_info.apply_duration[i] != 0 else 0)), v)
            else:
                TOKEN("end")
                Globals.s_blend_info.append(blend_item_info)

        fclose(fp)

        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    @staticmethod
    def Blend_Item_set_value(item):
        blend_info = None
        iter = None

        iter = s_blend_info.begin()
        while iter is not Globals.s_blend_info.end():
            blend_info = *iter
            if blend_info.item_vnum == item.GetVnum():
                apply_type = None
                apply_value = None
                apply_duration = None

                if item.GetVnum() == 51002:
                    apply_type = blend_info.apply_type
                    apply_value = blend_info.apply_value [Globals.FN_ECS_random_index()]
                    apply_duration = blend_info.apply_duration [Globals.FN_ECS_random_index()]
                else:
                    apply_type = blend_info.apply_type
                    apply_value = blend_info.apply_value [Globals.FN_random_index()]
                    apply_duration = blend_info.apply_duration [Globals.FN_random_index()]
                #sys_log(0, "blend_item : type : %d, value : %d, du : %d", apply_type, apply_value, apply_duration)
                item.SetSocket(0, apply_type, ((not DefineConstants.false)))
                item.SetSocket(1, apply_value, ((not DefineConstants.false)))
                item.SetSocket(2, apply_duration, ((not DefineConstants.false)))
                return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

            iter += 1
        return LGEMiscellaneous.DEFINECONSTANTS.false

    @staticmethod
    def Blend_Item_find(item_vnum):
        blend_info = None
        iter = None

        iter = s_blend_info.begin()
        while iter is not Globals.s_blend_info.end():
            blend_info = *iter
            if blend_info.item_vnum == item_vnum:
                return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
            iter += 1
        return LGEMiscellaneous.DEFINECONSTANTS.false


    s_blend_info = []

    @staticmethod
    def FN_random_index():
        percent = number(1,100)

        if percent<=10:
            return 0
        elif percent<=30:
            return 1
        elif percent<=70:
            return 2
        elif percent<=90:
            return 3
        else:
            return 4

        return 0

    @staticmethod
    def FN_ECS_random_index():
        percent = number(1,100)

        if percent<=5:
            return 0
        elif percent<=15:
            return 1
        elif percent<=60:
            return 2
        elif percent<=85:
            return 3
        else:
            return 4

        return 0


    ## Laniatus Games Studio Inc. | NOTE: This was formerly a static local variable declaration (not allowed in Python):
    BlueDragon_StateBattle_timeSkillCanUseTime = [time_t() for _ in range(SkillCount)]

    @staticmethod
    def BlueDragon_StateBattle(pChar):
        if pChar.GetHPPct() > 98:
            return ((1) * passes_per_sec)

        SKILLCOUNT = 3
        SkillPriority = [0 for _ in range(SKILLCOUNT)]
        ## Laniatus Games Studio Inc. | NOTE: This static local variable declaration (not allowed in Python) has been moved just prior to the method:
        #    static time_t timeSkillCanUseTime[SkillCount]

        if pChar.GetHPPct() > 76:
            SkillPriority[0] = 1
            SkillPriority[1] = 0
            SkillPriority[2] = 2
        elif pChar.GetHPPct() > 31:
            SkillPriority[0] = 0
            SkillPriority[1] = 1
            SkillPriority[2] = 2
        else:
            SkillPriority[0] = 0
            SkillPriority[1] = 2
            SkillPriority[2] = 1

        timeNow = get_dword_time()

        for i in range(0, SKILLCOUNT):
            SkillIndex = SkillPriority[i]

            if BlueDragon_StateBattle_timeSkillCanUseTime[SkillIndex] < timeNow:
                SkillUsingDuration = int(CMotionManager.instance().GetMotionDuration(pChar.GetRaceNum(), uint((((EMotionMode.MOTION_MODE_GENERAL) << 24) | ((EPublicMotion.MOTION_SPECIAL_1 + SkillIndex) << 8) | (0)))))

                BlueDragon_StateBattle_timeSkillCanUseTime[SkillIndex] = timeNow + (Globals.UseBlueDragonSkill(pChar, uint(SkillIndex)) * 1000) + SkillUsingDuration + 3000

                pChar.SendMovePacket(EMoveFuncType.FUNC_MOB_SKILL, byte(SkillIndex), uint(pChar.GetX()), uint(pChar.GetY()), 0, time_t(timeNow), -1)

                return ((1) * passes_per_sec) if 0 == SkillUsingDuration else ((SkillUsingDuration) * passes_per_sec)

        return ((1) * passes_per_sec)

    @staticmethod
    def UseBlueDragonSkill(pChar, idx):
        pSecMap = SECTREE_MANAGER.instance().GetMap(pChar.GetMapIndex())

        if None is pSecMap:
            return 0

        nextUsingTime = 0

        if idx == 0:
                #sys_log(0, "BlueDragon: Using Skill Breath")

                f = FSkillBreath(pChar)

                pSecMap.for_each(f.functor_method)

                nextUsingTime = number(BlueDragon_GetSkillFactor(3, "Skill0", "period", "min"), BlueDragon_GetSkillFactor(3, "Skill0", "period", "max"))

        elif idx == 1:
                #sys_log(0, "BlueDragon: Using Skill Weak Breath")

                f = FSkillWeakBreath(pChar)

                pSecMap.for_each(f.functor_method)

                nextUsingTime = number(BlueDragon_GetSkillFactor(3, "Skill1", "period", "min"), BlueDragon_GetSkillFactor(3, "Skill1", "period", "max"))

        elif idx == 2:
                #sys_log(0, "BlueDragon: Using Skill EarthQuake")

                f = FSkillEarthQuake(pChar)

                pSecMap.for_each(f.functor_method)

                nextUsingTime = number(BlueDragon_GetSkillFactor(3, "Skill2", "period", "min"), BlueDragon_GetSkillFactor(3, "Skill2", "period", "max"))

                if None is not f.pFarthestChar:
                    pChar.BeginFight(f.pFarthestChar)

        else:
            #lani_err("BlueDragon: Wrong Skill Index: %d", idx)
            return 0

        addPct = int(Globals.BlueDragon_GetRangeFactor("hp_period", pChar.GetHPPct()))

        nextUsingTime += math.trunc((nextUsingTime * addPct) / float(100))

        return nextUsingTime

    @staticmethod
    def BlueDragon_Damage(me, pAttacker, dam):
        if None is me or None is pAttacker:
            return dam

        if ((not LGEMiscellaneous.DEFINECONSTANTS.false)) == pAttacker.IsMonster() and 2493 == pAttacker.GetMobTable().dwVnum:
            for i in range(1, 5):
                if BLUEDRAGON_STONE_EFFECT.ATK_BONUS == Globals.BlueDragon_GetIndexFactor("DragonStone", i, "effect_type"):
                    dwDragonStoneID = Globals.BlueDragon_GetIndexFactor("DragonStone", i, "vnum")
                    val = Globals.BlueDragon_GetIndexFactor("DragonStone", i, "val")
                    cnt = SECTREE_MANAGER.instance().GetMonsterCountInMap(pAttacker.GetMapIndex(), dwDragonStoneID)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
                    dam += (dam * (val *cnt))/100

                    break

        if ((not LGEMiscellaneous.DEFINECONSTANTS.false)) == me.IsMonster() and 2493 == me.GetMobTable().dwVnum:
            for i in range(1, 5):
                if BLUEDRAGON_STONE_EFFECT.DEF_BONUS == Globals.BlueDragon_GetIndexFactor("DragonStone", i, "effect_type"):
                    dwDragonStoneID = Globals.BlueDragon_GetIndexFactor("DragonStone", i, "vnum")
                    val = Globals.BlueDragon_GetIndexFactor("DragonStone", i, "val")
                    cnt = SECTREE_MANAGER.instance().GetMonsterCountInMap(me.GetMapIndex(), dwDragonStoneID)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
                    dam -= (dam * (val *cnt))/100

                    if dam <= 0:
                        dam = 1

                    break

        if ((not LGEMiscellaneous.DEFINECONSTANTS.false)) == me.IsStone() and 0 != pAttacker.GetMountVnum():
            for i in range(1, 5):
                if me.GetMobTable().dwVnum == Globals.BlueDragon_GetIndexFactor("DragonStone", i, "vnum"):
                    if pAttacker.GetMountVnum() == Globals.BlueDragon_GetIndexFactor("DragonStone", i, "enemy"):
                        val = Globals.BlueDragon_GetIndexFactor("DragonStone", i, "enemy_val")

                        dam *= val

                        break

        return dam


## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern int test_server
## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern int passes_per_sec


    @staticmethod
    def BlueDragon_GetRangeFactor(key, val):
        L = quest.CQuestManager.instance().GetLuaState()

        stack_top = lua_gettop(L)

        lua_getglobal(L, "BlueDragonSetting")

        if DefineConstants.false == lua_istable(L, -1):
            lua_settop(L, stack_top)

            return 0

        lua_pushstring(L, key)
        lua_gettable(L, -2)

        if DefineConstants.false == lua_istable(L, -1):
            lua_settop(L, stack_top)

            #lani_err("BlueDragon: no required table %s", key)
            return 0

        cnt = int(luaL_getn(L, -1))

        for i in range(1, cnt + 1):
            lua_rawgeti(L, -1, i)

            if DefineConstants.false == lua_istable(L, -1):
                lua_settop(L, stack_top)

                #lani_err("BlueDragon: wrong table index %s %d", key, i)
                return 0

            lua_pushstring(L, "min")
            lua_gettable(L, -2)

            if DefineConstants.false == lua_isnumber(L, -1):
                lua_settop(L, stack_top)

                #lani_err("BlueDragon: no min value set %s", key)
                return 0

            min = int(lua_tonumber(L, -1))

            lua_pop(L, 1)

            lua_pushstring(L, "max")
            lua_gettable(L, -2)

            if DefineConstants.false == lua_isnumber(L, -1):
                lua_settop(L, stack_top)

                #lani_err("BlueDragon: no max value set %s", key)
                return 0

            max = int(lua_tonumber(L, -1))

            lua_pop(L, 1)

            if min <= val and val <= max:
                lua_pushstring(L, "pct")
                lua_gettable(L, -2)

                if DefineConstants.false == lua_isnumber(L, -1):
                    lua_settop(L, stack_top)

                    #lani_err("BlueDragon: no pct value set %s", key)
                    return 0

                pct = int(lua_tonumber(L, -1))

                lua_settop(L, stack_top)

                return uint(pct)

            lua_pop(L, 1)

        lua_settop(L, stack_top)

        return 0

# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
    #BlueDragon_GetSkillFactor(cnt, *LegacyParamArray)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
    #BlueDragon_GetIndexFactor(container, idx, key)


    @staticmethod
    def BlueDragon_GetSkillFactor(cnt, *LegacyParamArray):
        L = quest.CQuestManager.instance().GetLuaState()

        stack_top = lua_gettop(L)

        lua_getglobal(L, "BlueDragonSetting")

        if DefineConstants.false == lua_istable(L, -1):
            lua_settop(L, stack_top)

            return 0

        vl = None

    ParamCount = -1
    #    va_start(vl, cnt)

        for i in range(0, cnt):
        ParamCount += 1
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to pointers to value types:
#ORIGINAL METINII C CODE: const char* key = va_arg(vl, const char*);
            key = LegacyParamArray[ParamCount]

            if None == key:
    #            va_end(vl)
                lua_settop(L, stack_top)
                #lani_err("BlueDragon: wrong key list")
                return 0

            lua_pushstring(L, key)
            lua_gettable(L, -2)

            if DefineConstants.false == lua_istable(L, -1) and i != cnt-1:
    #            va_end(vl)
                lua_settop(L, stack_top)
                #lani_err("BlueDragon: wrong key table %s", key)
                return 0

    #    va_end(vl)

        if DefineConstants.false == lua_isnumber(L, -1):
            lua_settop(L, stack_top)
            #lani_err("BlueDragon: Last key is not a number")
            return 0

        val = int(lua_tonumber(L, -1))

        lua_settop(L, stack_top)

        return uint(val)

    @staticmethod
    def BlueDragon_GetIndexFactor(container, idx, key):
        L = quest.CQuestManager.instance().GetLuaState()

        stack_top = lua_gettop(L)

        lua_getglobal(L, "BlueDragonSetting")

        if DefineConstants.false == lua_istable(L, -1):
            lua_settop(L, stack_top)

            return 0

        lua_pushstring(L, container)
        lua_gettable(L, -2)

        if DefineConstants.false == lua_istable(L, -1):
            lua_settop(L, stack_top)

            #lani_err("BlueDragon: no required table %s", key)
            return 0

        lua_rawgeti(L, -1, idx)

        if DefineConstants.false == lua_istable(L, -1):
            lua_settop(L, stack_top)

            #lani_err("BlueDragon: wrong table index %s %d", key, idx)
            return 0

        lua_pushstring(L, key)
        lua_gettable(L, -2)

        if DefineConstants.false == lua_isnumber(L, -1):
            lua_settop(L, stack_top)

            #lani_err("BlueDragon: no min value set %s", key)
            return 0

        ret = lua_tonumber(L, -1)

        lua_settop(L, stack_top)

        return ret



    BUILDING_INCREASE_GUILD_MEMBER_COUNT_SMALL = 14061
    BUILDING_INCREASE_GUILD_MEMBER_COUNT_MEDIUM = 14062
    BUILDING_INCREASE_GUILD_MEMBER_COUNT_LARGE = 14063
    FLAG_VNUM = 14200
    WALL_DOOR_VNUM = 14201
    WALL_BACK_VNUM = 14202
    WALL_LEFT_VNUM = 14203
    WALL_RIGHT_VNUM = 14204
    ## Laniatus Games Studio Inc. | NOTE: The following #define macro was replaced in-line:
    #ORIGINAL METINII C CODE: #define IS_NO_SAVE_AFFECT(type) ((type) == LANIA_AFFECT_WAR_FLAG || (type) == LANIA_AFFECT_REVIVE_INVISIBLE || ((type) >= LANIA_AFFECT_PREMIUM_START && (type) <= LANIA_AFFECT_PREMIUM_END))
    ## Laniatus Games Studio Inc. | NOTE: The following #define macro was replaced in-line:
    #ORIGINAL METINII C CODE: #define IS_NO_CLEAR_ON_DEATH_AFFECT(type) ((type) == LANIA_AFFECT_BLOCK_CHAT || ((type) >= 500 && (type) < 600))

    @staticmethod
    def SendAffectRemovePacket(d, pid, type, point):
        ptoc = TPacketGLaniaCAffectsRemove()
        ptoc.bHeader = byte(Globals.LG_HEADER_GC_LANIA_AFFECT_REMOVE)
        ptoc.dwType = type
        ptoc.bApplyOn = point
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        d.Packet(ptoc, sizeof(TPacketGLaniaCAffectsRemove))

        ptod = SPacketGDRemoveAffect()
        ptod.dwPID = pid
        ptod.dwType = type
        ptod.bApplyOn = point
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        db_clientdesc.DBPacket(Globals.LG_HEADER_GD_REMOVE_AFFECT, 0, ptod, sizeof(ptod))

    @staticmethod
    def SendAffectAddPacket(d, pkAff):
        ptoc = TPacketGLaniaCAffectsAdd()
        ptoc.bHeader = byte(Globals.LG_HEADER_GC_LANIA_AFFECT_ADD)
        ptoc.elem.dwType = pkAff.dwType
        ptoc.elem.bApplyOn = pkAff.bApplyOn
        ptoc.elem.lApplyValue = pkAff.lApplyValue
        ptoc.elem.dwFlag = pkAff.dwFlag
        ptoc.elem.lDuration = pkAff.lDuration
        ptoc.elem.lSPCost = pkAff.lSPCost
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        d.Packet(ptoc, sizeof(TPacketGLaniaCAffectsAdd))

    @staticmethod
    def (UnnamedParameter):
        info = if isinstance(event.info, char_event_info) else None

        if info is None:
            #lani_err("affect_event> <Factor> Null pointer")
            return 0

        ch = info.ch

        if ch is None:
            return 0

        if not ch.UpdateAffect():
            return 0
        else:
            return passes_per_sec

    @staticmethod
    def (UnnamedParameter):
        info = if isinstance(event.info, load_affect_login_event_info) else None

        if info is None:
            #lani_err("load_affect_login_event_info> <Factor> Null pointer")
            return 0

        dwPID = info.pid
        ch = CHARACTER_MANAGER.instance().FindByPID(dwPID)

        if ch is None:
            LG_DEL_MEM_ARRAY(info.data)
            return 0

        d = ch.GetDesc()

        if d is None:
            LG_DEL_MEM_ARRAY(info.data)
            return 0

        if d.IsPhase(EPhase.PHASE_HANDSHAKE) or d.IsPhase(EPhase.PHASE_LOGIN) or d.IsPhase(EPhase.PHASE_SELECT) or d.IsPhase(EPhase.PHASE_DEAD) or d.IsPhase(EPhase.PHASE_LOADING):
            return ((1) * passes_per_sec)
        elif d.IsPhase(EPhase.PHASE_CLOSE):
            LG_DEL_MEM_ARRAY(info.data)
            return 0
        elif d.IsPhase(EPhase.PHASE_GAME):
            #sys_log(1, "Affect Load by Event")
            ch.LoadAffect(info.count, info.data)
            LG_DEL_MEM_ARRAY(info.data)
            return 0
        else:
            #lani_err("input_db.cpp:quest_login_event INVALID PHASE pid %d", ch.GetPlayerID())
            LG_DEL_MEM_ARRAY(info.data)
            return 0
    @staticmethod
    def AdjustExpByLevel(ch, exp):
        if LGEMiscellaneous.PLAYER_EXP_TABLE_MAX < ch.GetLevel():
            ret = 0.95
            factor = 0.1

            i = 0
            while i < ch.GetLevel()-100:
                if (math.fmod(i, 10)) == 0:
                    factor /= 2.0

                ret *= 1.0 - factor
                i += 1

            ret = ret * float(exp)

            if ret < 1.0:
                return 1

            return uint(ret)

        return exp

    @staticmethod
    def (UnnamedParameter):
        info = if isinstance(event.info, char_event_info) else None

        if info is None:
            #lani_err("StunEvent> <Factor> Null pointer")
            return 0

        ch = info.ch

        if ch is None:
            return 0
        ch.m_pkStunEvent = None
        ch.Dead(NULL, DefineConstants.false)
        return 0

    @staticmethod
    def (UnnamedParameter):
        info = if isinstance(event.info, SCharDeadEventInfo) else None

        if info is None:
            #lani_err("dead_event> <Factor> Null pointer")
            return 0

        ch = None

        if ((not LGEMiscellaneous.DEFINECONSTANTS.false)) == info.isPC:
            ch = CHARACTER_MANAGER.instance().FindByPID(info.dwID)
        else:
            ch = CHARACTER_MANAGER.instance().Find(info.dwID)

        if None is ch:
            #lani_err("DEAD_EVENT: cannot find char pointer with %s id(%d)","PC" if info.isPC else "MOB", info.dwID)
            return 0

        ch.m_pkDeadEvent = None

        if ch.GetDesc():
            ch.GetDesc().SetPhase(EPhase.PHASE_GAME)

            ch.SetPosition(EPositions.POS_STANDING)

            pos = pixel_position_s()

            if SECTREE_MANAGER.instance().GetRecallPositionByEmpire(ch.GetMapIndex(), ch.GetEmpire(), pos):
                ch.WarpSet(pos.x, pos.y, 0)
            else:
                #lani_err("cannot find spawn position (name %s)", ch.GetName(LOCALE_LANIATUS))
                ch.WarpSet(int(Globals.EMPIRE_START_X(ch.GetEmpire())), int(Globals.EMPIRE_START_Y(ch.GetEmpire())), 0)

            ch.PointChange(EPointTypes.LG_POINT_HP, (math.trunc(ch.GetMaxHP() / float(2))) - ch.GetHP(), ((not LGEMiscellaneous.DEFINECONSTANTS.false)), DefineConstants.false)

            ch.DeathPenalty(0)

            ch.StartRecoveryEvent()

            ch.ChatPacket(EChatType.CHAT_TYPE_COMMAND, "CloseRestartWindow")
        else:
            if ch.IsMonster() == ((not LGEMiscellaneous.DEFINECONSTANTS.false)):
                if ch.IsRevive() == LGEMiscellaneous.DEFINECONSTANTS.false and ch.HasReviverInParty() == ((not LGEMiscellaneous.DEFINECONSTANTS.false)):
                    ch.SetPosition(EPositions.POS_STANDING)
                    ch.SetHP(ch.GetMaxHP())

                    ch.ViewReencode()

                    ch.SetAggressive()
                    ch.SetRevive(((not LGEMiscellaneous.DEFINECONSTANTS.false)))

                    return 0

            CHARACTER_MANAGER.instance().DestroyCharacter(ch)

        return 0

    ## Laniatus Games Studio Inc. | NOTE: This was formerly a static local variable declaration (not allowed in Python):
    Reward_s_vec_item = []

    aItemDropPenalty_kor = [TItemDropPenalty(0, 0, 0, 0), TItemDropPenalty(0, 0, 0, 0), TItemDropPenalty(0, 0, 0, 0), TItemDropPenalty(0, 0, 0, 0), TItemDropPenalty(0, 0, 0, 0), TItemDropPenalty(25, 1, 5, 1), TItemDropPenalty(50, 2, 10, 1), TItemDropPenalty(75, 4, 15, 1), TItemDropPenalty(100, 8, 20, 1)]

    @staticmethod
    def GiveExp(from_, to, iExp):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        iExp = ((iExp * aiPercentByDeltaLev[MINMAX(0, (from_.GetLevel() + 15) - to.GetLevel(), LGEMiscellaneous.DEFINECONSTANTS.MAX_EXP_DELTA_OF_LEV - 1)]) / 100)

        iBaseExp = iExp
        iExp = math.trunc(iExp * (100 + CPrivManager.instance().GetPriv(to, EPrivType.PRIV_EXP_PCT)) / float(100))

            if to.IsEquipUniqueItem(uint(Globals.UNIQUE_ITEM_LARBOR_MEDAL)):
                iExp += math.trunc(iExp * 20 / float(100))

            if to.GetMapIndex() >= 660000 and to.GetMapIndex() < 670000:
                iExp += math.trunc(iExp * 20 / float(100))

            if to.GetPoint(EPointTypes.LG_POINT_EXP_DOUBLE_BONUS) != 0:
                if number(1, 100) <= to.GetPoint(EPointTypes.LG_POINT_EXP_DOUBLE_BONUS):
                    iExp += math.trunc(iExp * 30 / float(100))

            if to.IsEquipUniqueItem(uint(Globals.UNIQUE_ITEM_DOUBLE_EXP)):
                iExp += math.trunc(iExp * 50 / float(100))

            if (to.GetMountVnum() == 20110) or (to.GetMountVnum() == 20111) or (to.GetMountVnum() == 20112) or (to.GetMountVnum() == 20113):
                if to.IsEquipUniqueItem(71115) or to.IsEquipUniqueItem(71117) or to.IsEquipUniqueItem(71119) or to.IsEquipUniqueItem(71121):
                    iExp += math.trunc(iExp * 10 / float(100))

            elif (to.GetMountVnum() == 20114) or (to.GetMountVnum() == 20120) or (to.GetMountVnum() == 20121) or (to.GetMountVnum() == 20122) or (to.GetMountVnum() == 20123) or (to.GetMountVnum() == 20124) or (to.GetMountVnum() == 20125):
                iExp += math.trunc(iExp * 30 / float(100))

        if to.GetPremiumRemainSeconds(EPremiumTypes.PREMIUM_EXP) > 0:
            iExp += (math.trunc(iExp * 50 / float(100)))

        if to.IsEquipUniqueGroup(uint(Globals.UNIQUE_GROUP_RING_OF_EXP)) == ((not LGEMiscellaneous.DEFINECONSTANTS.false)):
            iExp += (math.trunc(iExp * 50 / float(100)))

        iExp += math.trunc(iExp * to.GetMarriageBonus(uint(Globals.UNIQUE_ITEM_MARRIAGE_EXP_BONUS), ((not DefineConstants.false))) / float(100))

        iExp += (math.trunc(iExp * to.GetPoint(EPointTypes.LG_POINT_RAMADAN_CANDY_BONUS_EXP) / float(100)))
        iExp += (math.trunc(iExp * to.GetPoint(EPointTypes.LG_POINT_MALL_EXPBONUS) / float(100)))
        iExp += (math.trunc(iExp * to.GetPoint(EPointTypes.LG_POINT_EXP) / float(100)))

        if test_server:
            #sys_log(0, "Bonus Exp : Ramadan Candy: %d MallExp: %d PointExp: %d", to.GetPoint(EPointTypes.LG_POINT_RAMADAN_CANDY_BONUS_EXP), to.GetPoint(EPointTypes.LG_POINT_MALL_EXPBONUS), to.GetPoint(EPointTypes.LG_POINT_EXP))

        iExp = math.trunc(iExp * CHARACTER_MANAGER.instance().GetMobExpRate(to) / float(100))
        iExp = MINMAX(0, iExp, math.trunc(to.GetNextExp() / float(10)))

        if test_server:
            if (quest.CQuestManager.instance().GetEventFlag("exp_bonus_log")) != 0 and iBaseExp>0:
                to.ChatPacket(EChatType.CHAT_TYPE_INFO, "exp bonus %d%%", math.trunc((iExp-iBaseExp)*100 / float(iBaseExp)))

        iExp = int(Globals.AdjustExpByLevel(to, uint(iExp)))

        to.PointChange(EPointTypes.LG_POINT_EXP, iExp, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), DefineConstants.false)
        from_.CreateFly(byte(Globals.FLY_EXP), to)

            you = to.GetMarryPartner()
            if you:
                dwUpdatePoint = math.trunc(2000 *iExp / float(math.trunc(to.GetLevel() / float(math.trunc(to.GetLevel() / float(3))))))

                if to.GetPremiumRemainSeconds(EPremiumTypes.PREMIUM_MARRIAGE_FAST) > 0 or you.GetPremiumRemainSeconds(EPremiumTypes.PREMIUM_MARRIAGE_FAST) > 0:
                    dwUpdatePoint = (dwUpdatePoint * 3)

                pMarriage = marriage.CManager.instance().Get(to.GetPlayerID())

                if pMarriage is not None and pMarriage.IsNear():
                    pMarriage.Update(dwUpdatePoint)

    @staticmethod
    def (UnnamedParameter):
        info = if isinstance(event.info, char_event_info) else None

        if info is None:
            #lani_err("horse_dead_event> <Factor> Null pointer")
            return 0

        ch = info.ch
        if ch is None:
            return 0
        ch.HorseSummon(LGEMiscellaneous.DEFINECONSTANTS.false, DefineConstants.false, 0, 0)
        return 0
    ITEM_BROKEN_METIN_VNUM = 28960
    g_aBuffOnAttrPoints = [(int)EPointTypes.LG_POINT_ENERGY, (int)EPointTypes.LG_POINT_COSTUME_ATTR_BONUS]

    @staticmethod
    def IS_SUMMON_ITEM(vnum):
        if (vnum == 22000) or (vnum == 22010) or (vnum == 22011) or (vnum == 22020) or (vnum == Globals.ITEM_MARRIAGE_RING):
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        return LGEMiscellaneous.DEFINECONSTANTS.false

    @staticmethod
    def IS_MONKEY_DUNGEON(map_index):
        if (map_index == 5) or (map_index == 25) or (map_index == 45) or (map_index == 108) or (map_index == 109):
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        return LGEMiscellaneous.DEFINECONSTANTS.false

    @staticmethod
    def IS_SUMMONABLE_ZONE(map_index):
        if Globals.IS_MONKEY_DUNGEON(map_index):
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if (map_index == 66) or (map_index == 71) or (map_index == 72) or (map_index == 73) or (map_index == 193):
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##if false
            #		case 184 :
            #		case 185 :
            #		case 186 :
            #		case 187 :
            #		case 188 :
            #		case 189 :
    ##endif
        if (map_index == 66) or (map_index == 71) or (map_index == 72) or (map_index == 73) or (map_index == 193) or (map_index == 216) or (map_index == 217) or (map_index == 208):
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if map_index > 10000:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    @staticmethod
    def FN_check_LG_ITEM_SOCKET(item):
        i = 0
        while i < EItemMisc.LG_ITEM_SOCKET_MAX_NUM:
            if item.GetSocket(i) != item.GetProto().alSockets[i]:
                return LGEMiscellaneous.DEFINECONSTANTS.false
            i += 1

        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    @staticmethod
    def FN_copy_LG_ITEM_SOCKET(dest, src):
        i = 0
        while i < EItemMisc.LG_ITEM_SOCKET_MAX_NUM:
            dest.SetSocket(i, src.GetSocket(i), ((not DefineConstants.false)))
            i += 1
    @staticmethod
    def FN_check_item_sex(ch, item):
        ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'IS_SET' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
        if IS_SET(item.GetAntiFlag(), LaniatusEITMAntiFlagDcs.ITEM_ANTIFLAG_MALE):
            if ESex.LG_SEX_MALE == Globals.GET_SEX(ch):
                return LGEMiscellaneous.DEFINECONSTANTS.false

        ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'IS_SET' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
        if IS_SET(item.GetAntiFlag(), LaniatusEITMAntiFlagDcs.ITEM_ANTIFLAG_FEMALE):
            if ESex.LG_SEX_FEMALE == Globals.GET_SEX(ch):
                return LGEMiscellaneous.DEFINECONSTANTS.false

        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    @staticmethod
    def TransformRefineItem(pkOldItem, pkNewItem):
        if pkOldItem.IsAccessoryForSocket():
            i = 0
            while i < EItemMisc.LG_ITEM_SOCKET_MAX_NUM:
                pkNewItem.SetSocket(i, pkOldItem.GetSocket(i), ((not DefineConstants.false)))
                i += 1
        else:
            i = 0
            while i < EItemMisc.LG_ITEM_SOCKET_MAX_NUM:
                if pkOldItem.GetSocket(i) == 0:
                    break
                else:
                    pkNewItem.SetSocket(i, 1, ((not DefineConstants.false)))
                i += 1

            slot = 0

            i = 0
            while i < EItemMisc.LG_ITEM_SOCKET_MAX_NUM:
                socket = pkOldItem.GetSocket(i)

                if socket > 2 and socket != Globals.ITEM_BROKEN_METIN_VNUM:
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: pkNewItem->SetSocket(slot++, socket);
                    pkNewItem.SetSocket(slot, socket, ((not DefineConstants.false)))
                    slot += 1
                i += 1

        pkOldItem.CopyAttributeTo(pkNewItem)

    @staticmethod
    def NotifyRefineSuccess(ch, item, way):
        if None is not ch and item is not None:
            ch.ChatPacket(EChatType.CHAT_TYPE_COMMAND, "RefineSuceeded")

    @staticmethod
    def NotifyRefineFail(ch, item, way, success = 0):
        if None is not ch and None is not item:
            ch.ChatPacket(EChatType.CHAT_TYPE_COMMAND, "RefineFailed")

    @staticmethod
    def (UnnamedParameter):
        info = if isinstance(event.info, char_event_info) else None

        if info is None:
            #lani_err("kill_campfire_event> <Factor> Null pointer")
            return 0

        ch = info.ch

        if ch is None:
            return 0
        ch.m_pkMiningEvent = None
        CHARACTER_MANAGER.instance().DestroyCharacter(ch)
        return 0

    @staticmethod
    def CalculateConsume(ch):
        WARP_NEED_LIFE_PERCENT = 30
        WARP_MIN_LIFE_PERCENT = 10

        consumeLife = 0
            curLife = ch.GetHP()
            NEEDPERCENT = WARP_NEED_LIFE_PERCENT
            needLife = math.trunc(ch.GetMaxHP() * NEEDPERCENT / float(100))
            if curLife < needLife:
                ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You don't have enough HP."))
                return -1

            consumeLife = needLife
            MINPERCENT = WARP_MIN_LIFE_PERCENT
            minLife = math.trunc(ch.GetMaxHP() * MINPERCENT / float(100))
            if curLife - needLife < minLife:
                consumeLife = curLife - minLife

            if consumeLife < 0:
                consumeLife = 0
        return consumeLife

    @staticmethod
    def CalculateConsumeSP(lpChar):
        NEED_WARP_SP_PERCENT = 30

        curSP = lpChar.GetSP()
        needSP = math.trunc(lpChar.GetMaxSP() * NEED_WARP_SP_PERCENT / float(100))

        if curSP < needSP:
            lpChar.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You don't have enough Spell Points to use this."))
            return -1

        return needSP

    g_nPortalLimitTime = 10

    ## Laniatus Games Studio Inc. | NOTE: This was formerly a static local variable declaration (not allowed in Python):
    BuffOnAttr_ValueChange_abSlot = [(int)EWearPositions.WEAR_BODY, EWearPositions.WEAR_HEAD, EWearPositions.WEAR_FOOTS, EWearPositions.WEAR_WRIST, EWearPositions.WEAR_WEAPON, EWearPositions.WEAR_NECK, EWearPositions.WEAR_EAR, (int)EWearPositions.WEAR_SHIELD]
    ## Laniatus Games Studio Inc. | NOTE: This was formerly a static local variable declaration (not allowed in Python):
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
    #BuffOnAttr_ValueChange_vec_slots(UnnamedParameter, )
    ## Laniatus Games Studio Inc. | NOTE: This was formerly a static local variable declaration (not allowed in Python):
    BuffOnAttr_ValueChange_abSlot = [(int)EWearPositions.WEAR_COSTUME_BODY, EWearPositions.WEAR_COSTUME_HAIR, (int)EWearPositions.WEAR_COSTUME_WEAPON]
    ## Laniatus Games Studio Inc. | NOTE: This was formerly a static local variable declaration (not allowed in Python):
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
    #BuffOnAttr_ValueChange_vec_slots(UnnamedParameter, )

    @staticmethod
    def GetAcceRefineGrade(vnum):
        if vnum >= 85001 and vnum <= 85004:
            return int(vnum - 85000)
        elif vnum >= 85005 and vnum <= 85008:
            return int(vnum - 85004)
        elif vnum >= 85011 and vnum <= 85014:
            return int(vnum - 85010)
        elif vnum >= 85015 and vnum <= 85018:
            return int(vnum - 85014)
        elif vnum >= 85021 and vnum <= 85024:
            return int(vnum - 85020)
        elif vnum >= 86001 and vnum <= 86004:
            return int(vnum - 86000)
        elif vnum >= 86005 and vnum <= 86008:
            return int(vnum - 86004)
        elif vnum >= 86011 and vnum <= 86014:
            return int(vnum - 86010)
        elif vnum >= 86015 and vnum <= 86018:
            return int(vnum - 86014)
        elif vnum >= 86021 and vnum <= 86024:
            return int(vnum - 86020)
        elif vnum >= 86025 and vnum <= 86028:
            return int(vnum - 86024)
        elif vnum >= 86031 and vnum <= 86034:
            return int(vnum - 86030)
        elif vnum >= 86035 and vnum <= 86038:
            return int(vnum - 86034)
        elif vnum >= 86041 and vnum <= 86044:
            return int(vnum - 86040)
        elif vnum >= 86045 and vnum <= 86048:
            return int(vnum - 86044)
        elif vnum >= 86051 and vnum <= 86054:
            return int(vnum - 86050)
        elif vnum >= 86055 and vnum <= 86058:
            return int(vnum - 86054)
        elif vnum >= 86061 and vnum <= 86064:
            return int(vnum - 86060)
        else:
            return 0

    ## Laniatus Games Studio Inc. | NOTE: The following #define macro was replaced in-line:
    #ORIGINAL METINII C CODE: #define M2_DESTROY_CHARACTER(ptr) CHARACTER_MANAGER::instance().DestroyCharacter(ptr)

    @staticmethod
    def __IsSpawnableInSafeZone(raceType):
        if (raceType == ECharType.CHAR_TYPE_NPC) or (raceType == ECharType.CHAR_TYPE_WARP) or (raceType == ECharType.CHAR_TYPE_GOTO) or (raceType == ECharType.CHAR_TYPE_HORSE) or (raceType == ECharType.CHAR_TYPE_PET) or (raceType == ECharType.CHAR_TYPE_MOUNT):
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        if True:
            return LGEMiscellaneous.DEFINECONSTANTS.false
    poison_damage_rate = [80, 50, 40, 30, 25, 1] + [0 for _ in range(EMobRank.MOB_RANK_MAX_NUM - 6)]

    @staticmethod
    def GetPoisonDamageRate(ch):
        iRate = None

        if ch.IsPC():
            iRate = 50
        else:
            iRate = Globals.poison_damage_rate[ch.GetMobRank()]

        iRate = MAX(0, iRate - ch.GetPoint(EPointTypes.LG_POINT_POISON_REDUCE))
        return iRate

    @staticmethod
    def (UnnamedParameter):
        info = if isinstance(event.info, TPoisonEventInfo) else None

        if info is None:
            #lani_err("poison_event> <Factor> Null pointer")
            return 0

        ch = info.ch

        if ch is None:
            return 0
        pkAttacker = CHARACTER_MANAGER.instance().FindByPID(info.attacker_pid)

        dam = math.trunc(ch.GetMaxHP() * Globals.GetPoisonDamageRate(ch) / float(1000))
        if test_server:
            ch.ChatPacket(EChatType.CHAT_TYPE_NOTICE, "Poison Damage %d", dam)

        if ch.Damage(pkAttacker, dam, EDamageType.DAMAGE_TYPE_POISON):
            ch.m_pkPoisonEvent = None
            return 0

        info.count -= 1

        if info.count != 0:
            return ((3) * passes_per_sec)
        else:
            ch.m_pkPoisonEvent = None
            return 0

    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##if ENABLE_WOLFMAN
    bleeding_damage_rate = [80, 50, 40, 30, 25, 1] + [0 for _ in range(EMobRank.MOB_RANK_MAX_NUM - 6)]

    @staticmethod
    def GetBleedingDamageRate(ch):
        iRate = None

        if ch.IsPC():
            iRate = 50
        else:
            iRate = Globals.bleeding_damage_rate[ch.GetMobRank()]

        iRate = MAX(0, iRate - ch.GetPoint(EPointTypes.LG_POINT_BLEEDING_REDUCE))

        return iRate

    @staticmethod
    def (UnnamedParameter):
        info = if isinstance(event.info, TBleedingEventInfo) else None

        if info is None:
            #lani_err("bleeding_event> <Factor> Null pointer")
            return 0

        ch = info.ch

        if ch is None:
            return 0
        pkAttacker = CHARACTER_MANAGER.instance().FindByPID(info.attacker_pid)

        dam = math.trunc(ch.GetMaxHP() * Globals.GetBleedingDamageRate(ch) / float(1000))
        if test_server:
            ch.ChatPacket(EChatType.CHAT_TYPE_NOTICE, "Bleeding Damage %d", dam)

        if ch.Damage(pkAttacker, dam, EDamageType.DAMAGE_TYPE_BLEEDING):
            ch.m_pkBleedingEvent = None
            return 0

        info.count -= 1

        if info.count != 0:
            return ((3) * passes_per_sec)
        else:
            ch.m_pkBleedingEvent = None
            return 0

    @staticmethod
    def (UnnamedParameter):
        info = if isinstance(event.info, TFireEventInfo) else None

        if info is None:
            #lani_err("fire_event> <Factor> Null pointer")
            return 0

        ch = info.ch
        if ch is None:
            return 0
        pkAttacker = CHARACTER_MANAGER.instance().FindByPID(info.attacker_pid)

        dam = info.amount
        if test_server:
            ch.ChatPacket(EChatType.CHAT_TYPE_NOTICE, "Fire Damage %d", dam)

        if ch.Damage(pkAttacker, dam, EDamageType.DAMAGE_TYPE_FIRE):
            ch.m_pkFireEvent = None
            return 0

        info.count -= 1

        if info.count != 0:
            return ((3) * passes_per_sec)
        else:
            ch.m_pkFireEvent = None
            return 0

    poison_level_adjust = [100, 90, 80, 70, 50, 30, 10, 5, 0]

    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##if ENABLE_WOLFMAN
    bleeding_level_adjust = [100, 90, 80, 70, 50, 30, 10, 5, 0]

    g_test_server = False
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
    #FindVictim(pkChr, iMaxDistance)

    @staticmethod
    def __CHARACTER_GotoNearTarget(self, victim):
        ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'IS_SET' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
        if IS_SET(self.GetAIFlag(), EAIFlags.AIFLAG_NOMOVE):
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if (self.GetMobBattleType() == EBattleType.BATTLE_TYPE_RANGE) or (self.GetMobBattleType() == EBattleType.BATTLE_TYPE_MAGIC):
            if self.Follow(victim, math.trunc(self.GetMobAttackRange() * 8 / float(10))):
                return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        else:
            if self.Follow(victim, math.trunc(self.GetMobAttackRange() * 9 / float(10))):
                return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        return LGEMiscellaneous.DEFINECONSTANTS.false
    emotion_types = [emotion_type_s("french_kiss", "french_kiss", (1 << 1) | (SELF_DISARM | (1 << 5)), 2.0), emotion_type_s("kiss", "kiss", (1 << 1) | (SELF_DISARM | (1 << 5)), 1.5), emotion_type_s("slap", "slap", (1 << 1) | (1 << 4), 1.5), emotion_type_s("clap", "clap", 0, 1.0), emotion_type_s("cheer1", "cheer1", 0, 1.0), emotion_type_s("cheer2", "cheer2", 0, 1.0), emotion_type_s("dance1", "dance1", 0, 1.0), emotion_type_s("dance2", "dance2", 0, 1.0), emotion_type_s("dance3", "dance3", 0, 1.0), emotion_type_s("dance4", "dance4", 0, 1.0), emotion_type_s("dance5", "dance5", 0, 1.0), emotion_type_s("dance6", "dance6", 0, 1.0), emotion_type_s("congratulation", "congratulation", 0, 1.0), emotion_type_s("forgive", "forgive", 0, 1.0), emotion_type_s("angry", "angry", 0, 1.0), emotion_type_s("attractive", "attractive", 0, 1.0), emotion_type_s("sad", "sad", 0, 1.0), emotion_type_s("shy", "shy", 0, 1.0), emotion_type_s("cheerup", "cheerup", 0, 1.0), emotion_type_s("banter", "banter", 0, 1.0), emotion_type_s("joy", "joy", 0, 1.0), emotion_type_s("\n", "\n", 0, 0.0)]


    s_emotion_set = std::set()

    @staticmethod
    def (UnnamedParameter):
        arg1 = str(['\0' for _ in range(256)])
        temp_ref_arg1 = RefObject(arg1);
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        Globals.one_argument(argument, temp_ref_arg1, sizeof(arg1))
        arg1 = temp_ref_arg1.arg_value

        if (not arg1[0]) != '\0':
            return

        val = 0
        temp_ref_val = RefObject(val);
        Globals.str_to_number(temp_ref_val, arg1)
        val = temp_ref_val.arg_value
        Globals.s_emotion_set.insert((ch.GetVID(), val))

    @staticmethod
    def (UnnamedParameter):
        i = None
            if ch.IsRiding():
                ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("you cannot exchange emotions on a horse."))
                return

        i = 0
        while Globals.emotion_types[i].command[0] != '\n':
            if not strcmp(cmd_info[cmd].command, Globals.emotion_types[i].command):
                break

            if not strcmp(cmd_info[cmd].command, Globals.emotion_types[i].command_to_client):
                break
            i += 1

        if Globals.emotion_types[i].command[0] == '\n':
            #lani_err("cannot find emotion")
            return

        ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'IS_SET' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
        if IS_SET(Globals.emotion_types[i].flag, (1 << 2)) and ESex.LG_SEX_MALE == Globals.GET_SEX(ch):
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Only women can do this."))
            return

        arg1 = str(['\0' for _ in range(256)])
        temp_ref_arg1 = RefObject(arg1);
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        Globals.one_argument(argument, temp_ref_arg1, sizeof(arg1))
        arg1 = temp_ref_arg1.arg_value

        victim = None

        if arg1[0] != '\0':
            ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'IS_SET' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
            victim = ch.FindCharacterInView(arg1, IS_SET(Globals.emotion_types[i].flag, (1 << 1)))

        ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'IS_SET' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
        if IS_SET(Globals.emotion_types[i].flag, (1 << 0) | (1 << 1)):
            if victim is None:
                ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("This person doesn't exist."))
                return

        if victim:
            if (not victim.IsPC()) or victim is ch:
                return

            if victim.IsRiding():
                ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You cannot exchange emotions with someone on a horse."))
                return

            distance = Globals.DISTANCE_APPROX(ch.GetX() - victim.GetX(), ch.GetY() - victim.GetY())

            if distance < 10:
                ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You are too near."))
                return

            if distance > 500:
                ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You are too far away."))
                return

            ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'IS_SET' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
            if IS_SET(Globals.emotion_types[i].flag, (1 << 3)):
                if Globals.GET_SEX(ch) == Globals.GET_SEX(victim):
                    ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("This can only be done with another gender."))
                    return

            ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'IS_SET' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
            if IS_SET(Globals.emotion_types[i].flag, (1 << 1)):
                if Globals.s_emotion_set.find((victim.GetVID(), ch.GetVID())) == Globals.s_emotion_set.end():
                    if ((not LGEMiscellaneous.DEFINECONSTANTS.false)) == marriage.CManager.instance().IsMarried(ch.GetPlayerID()):
                        marriageInfo = marriage.CManager.instance().Get(ch.GetPlayerID())

                        other = marriageInfo.GetOther(ch.GetPlayerID())

                        if 0 == other or other != victim.GetPlayerID():
                            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You must have the acknowledgement of your partner."))
                            return
                    else:
                        ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You must have the acknowledgement of your partner."))
                        return

                Globals.s_emotion_set.insert((ch.GetVID(), victim.GetVID()))

        chatbuf = str(['\0' for _ in range(256+1)])
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        len = snprintf(chatbuf, sizeof(chatbuf), "%s %u %u", Globals.emotion_types[i].command_to_client, ch.GetVID(),victim.GetVID() if victim is not None else 0)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        if len < 0 or len >= int(sizeof(chatbuf)):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            len = sizeof(chatbuf) - 1

        len += 1

        pack_chat = packet_chat()
        pack_chat.header = byte(Globals.LG_HEADER_GC_CHAT)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        pack_chat.size = sizeof(packet_chat) + len
        pack_chat.type = EChatType.CHAT_TYPE_COMMAND
        pack_chat.id = 0
        buf = TEMP_BUFFER(8192, DefineConstants.false)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        buf.write(pack_chat, sizeof(packet_chat))
        buf.write(chatbuf, len)

        ch.PacketAround(buf.read_peek(), buf.size())

        if victim:
            #sys_log(1, "ACTION: %s TO %s", Globals.emotion_types[i].command, victim.GetName(LOCALE_LANIATUS))
        else:
            Globals.#sys_log(1, "ACTION: %s", Globals.emotion_types[i].command)


    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##if ! _WIN32
    ## Laniatus Games Studio Inc. | WARNING: The following #include directive was ignored:
    ##include <md5.h>
    ##else
    ##endif

## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern int g_server_id

## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern int g_nPortalLimitTime

    @staticmethod
    def (UnnamedParameter):
        if ch.IsObserverMode():
            return

        if ch.IsDead() or ch.IsStun():
            return

        if ch.IsHorseRiding() == LGEMiscellaneous.DEFINECONSTANTS.false:
            if ch.GetMountVnum():
                ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You are already riding a mount."))
                return

            if ch.GetHorse() is None:
                ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Please call your Horse first."))
                return

            ch.StartRiding()
        else:
            ch.StopRiding()

    @staticmethod
    def (UnnamedParameter):
        if ch.GetHorse() is not None:
            ch.HorseSummon(LGEMiscellaneous.DEFINECONSTANTS.false)
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You sent back your Horse."))
        elif ch.IsHorseRiding() == ((not LGEMiscellaneous.DEFINECONSTANTS.false)):
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You have to get off your Horse."))
        else:
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Please call your Horse first."))

    @staticmethod
    def (UnnamedParameter):
        if ch.GetMyShop():
            return

        if ch.GetHorse() is None:
            if ch.IsHorseRiding() == LGEMiscellaneous.DEFINECONSTANTS.false:
                ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Please call your Horse first."))
            else:
                ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You cannot feed your Horse while sitting on it."))
            return

        dwFood = ch.GetHorseGrade() + 50054 - 1

        if ch.CountSpecifyItem(dwFood) > 0:
            ch.RemoveSpecifyItem(dwFood, 1)
            ch.FeedHorse()
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You gave %s%s to a Horse."), ITEM_MANAGER.instance().GetTable(dwFood).szLocaleName, "")
        else:
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You need %s."), ITEM_MANAGER.instance().GetTable(dwFood).szLocaleName)

    @staticmethod
    def (UnnamedParameter):
        info = if isinstance(event.info, shutdown_event_data) else None

        if info is None:
            #lani_err("shutdown_event> <Factor> Null pointer")
            return 0

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to pointers to value types:
#ORIGINAL METINII C CODE: int *pSec = & (info->seconds);
        pSec = & (info.seconds)

        if *pSec < None:
            Globals.#sys_log(0, "shutdown_event sec %d", pSec)

            pSec -= 1
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: if (--*pSec == -10)
            if  pSec == -10:
                c_set_desc = DESC_MANAGER.instance().GetClientSet()
                std::for_each(c_set_desc.begin(), c_set_desc.end(), DisconnectFunc())
                return passes_per_sec
            elif *pSec < -10:
                return 0

            return passes_per_sec
        elif *pSec is None:
            c_set_desc = DESC_MANAGER.instance().GetClientSet()
            std::for_each(c_set_desc.begin(), c_set_desc.end(), SendDisconnectFunc())
            g_bNoMoreClient = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
            pSec -= 1
            return passes_per_sec
        else:
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##if __MULTI_LANGUAGE_SYSTEM__
            Globals.SendNotice(LC_TEXT("%d seconds until shutting off."), pSec)
    ##else
            buf = str(['\0' for _ in range(64)])
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            snprintf(buf, sizeof(buf), LC_TEXT("%d seconds until shutting off."), pSec)
            Globals.SendNotice(buf)
    ##endif

            pSec -= 1
            return passes_per_sec

    @staticmethod
    def Shutdown(iSec):
        if g_bNoMoreClient:
            Globals.thecore_shutdown()
            return

        CWarMapManager.instance().OnShutdown()

    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##if __MULTI_LANGUAGE_SYSTEM__
        Globals.SendNotice(LC_TEXT("The Game will be closed after %d Seconds."), iSec)
    ##else
        buf = str(['\0' for _ in range(64)])
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        snprintf(buf, sizeof(buf), LC_TEXT("The Game will be closed after %d Seconds."), iSec)
        Globals.SendNotice(buf)
    ##endif

        info = Globals.AllocEventInfo()
        info.seconds = iSec

        Globals.event_create_ex(shutdown_event, info, 1)

    @staticmethod
    def (UnnamedParameter):
        if None == ch:
            return
        p = SPacketGGShutdown()
        p.bHeader = byte(Globals.LG_HEADER_GG_SHUTDOWN)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        P2P_MANAGER.instance().Send(p, sizeof(SPacketGGShutdown), NULL)

    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##if ! _IMPROVED_PACKET_ENCRYPTION_
        client_packet = SPacketShutdown()
        client_packet.state = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        db_clientdesc.DBPacket(Globals.LG_HEADER_GD_SHUTDOWN, 0, client_packet, sizeof(client_packet))
    ##endif

        Globals.Shutdown(10)

    @staticmethod
    def (UnnamedParameter):
        info = if isinstance(event.info, TimedEventInfo) else None

        if info is None:
            #lani_err("timed_event> <Factor> Null pointer")
            return 0

        ch = info.ch
        if ch is None:
            return 0
        d = ch.GetDesc()

        if info.left_second <= 0:
            ch.m_pkTimedEvent = None

            if (info.subcmd == SCMD_CMD.SCMD_LOGOUT) or (info.subcmd == SCMD_CMD.SCMD_QUIT) or (info.subcmd == SCMD_CMD.SCMD_PHASE_SELECT):
                    acc_info = tNeedLoginLogInfo()
                    acc_info.dwPlayerID = ch.GetDesc().GetAccountTable().id
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##if __MULTI_LANGUAGE_SYSTEM__
                    acc_info.bLanguage = ch.GetDesc().GetAccountTable().bLanguage
    ##endif

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                    db_clientdesc.DBPacket(Globals.LG_HEADER_GD_VALID_LOGOUT, 0, acc_info, sizeof(acc_info))

            if info.subcmd == SCMD_CMD.SCMD_LOGOUT:
                if d:
                    d.SetPhase(EPhase.PHASE_CLOSE)

            elif info.subcmd == SCMD_CMD.SCMD_QUIT:
                ch.ChatPacket(EChatType.CHAT_TYPE_COMMAND, "quit")

            elif info.subcmd == SCMD_CMD.SCMD_PHASE_SELECT:
                    ch.Disconnect("timed_event - SCMD_PHASE_SELECT")

                    if d:
                        d.SetPhase(EPhase.PHASE_SELECT)

            return 0
        else:
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("%d seconds until shutting off."), info.left_second)
            info.left_second -= 1

        return ((1) * passes_per_sec)

    @staticmethod
    def (UnnamedParameter):
        if ch.m_pkTimedEvent:
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Your Logout was cancelled."))
            Globals.event_cancel(ch.m_pkTimedEvent)
            return

        if subcmd == SCMD_CMD.SCMD_LOGOUT:
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Back to Login Window. Please wait."))

        elif subcmd == SCMD_CMD.SCMD_QUIT:
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You will be disconnected from the server. Please wait."))

        elif subcmd == SCMD_CMD.SCMD_PHASE_SELECT:
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Changing character. Please wait."))

        nExitLimitTime = 10

        if ch.IsHack(LGEMiscellaneous.DEFINECONSTANTS.false, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), nExitLimitTime) and ((not ch.GetWarMap()) or ch.GetWarMap().GetType() == EGuildWarType.GUILD_WAR_TYPE_FLAG):
            return

        if (subcmd == SCMD_CMD.SCMD_LOGOUT) or (subcmd == SCMD_CMD.SCMD_QUIT) or (subcmd == SCMD_CMD.SCMD_PHASE_SELECT):
                info = Globals.AllocEventInfo()

                    if ch.IsPosition(EPositions.POS_FIGHTING):
                        info.left_second = 10
                    else:
                        info.left_second = 3

                info.ch = ch
                info.subcmd = subcmd
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                strncpy_s(info.szReason, sizeof(info.szReason), argument, _TRUNCATE)

                ch.m_pkTimedEvent = Globals.event_create_ex(timed_event, info, 1)

    @staticmethod
    def (UnnamedParameter):
        pass

    @staticmethod
    def (UnnamedParameter):
        arg1 = str(['\0' for _ in range(256)])
        temp_ref_arg1 = RefObject(arg1);
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        Globals.one_argument(argument, temp_ref_arg1, sizeof(arg1))
        arg1 = temp_ref_arg1.arg_value

        if (not arg1[0]) != '\0':
            return

        ch.SetRotation(float(arg1))
        ch.fishing()

    @staticmethod
    def (UnnamedParameter):
        ch.ChatPacket(EChatType.CHAT_TYPE_COMMAND, "ConsoleEnable")

    @staticmethod
    def (UnnamedParameter):
        if LGEMiscellaneous.DEFINECONSTANTS.false == ch.IsDead():
            ch.ChatPacket(EChatType.CHAT_TYPE_COMMAND, "CloseRestartWindow")
            ch.StartRecoveryEvent()
            return

        if None == ch.m_pkDeadEvent:
            return

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        iTimeToDead = (Globals.event_time(ch.m_pkDeadEvent) / passes_per_sec)

        if subcmd != SCMD_RESTART.SCMD_RESTART_TOWN and ((not ch.GetWarMap()) or ch.GetWarMap().GetType() == EGuildWarType.GUILD_WAR_TYPE_FLAG):
            if not test_server:
                if ch.IsHack():
                    ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("No new start possible.(%d seconds left) "), iTimeToDead - (180 - g_nPortalLimitTime))
                    return

                if iTimeToDead > 170:
                    ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("No new start possible.(%d seconds left) "), iTimeToDead - 170)
                    return

        if subcmd == SCMD_RESTART.SCMD_RESTART_TOWN:
            if ch.IsHack():
                if ((not ch.GetWarMap()) or ch.GetWarMap().GetType() == EGuildWarType.GUILD_WAR_TYPE_FLAG):
                    ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("No new start possible.(%d seconds left) "), iTimeToDead - (180 - g_nPortalLimitTime))
                    return

            if iTimeToDead > 173:
                ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Still no new start possible in the city. (%d seconds left)"), iTimeToDead - 173)
                return

        ch.ChatPacket(EChatType.CHAT_TYPE_COMMAND, "CloseRestartWindow")

        ch.GetDesc().SetPhase(EPhase.PHASE_GAME)
        ch.SetPosition(EPositions.POS_STANDING)
        ch.StartRecoveryEvent()

        if ch.GetDungeon():
            ch.GetDungeon().UseRevive(ch)

        if ch.GetWarMap() and not ch.IsObserverMode():
            pMap = ch.GetWarMap()
            dwGuildOpponent = pMap.GetGuildOpponent(ch) if pMap is not None else 0

            if dwGuildOpponent != 0:
                if subcmd == SCMD_RESTART.SCMD_RESTART_TOWN:
                    #sys_log(0, "do_restart: restart town")
                    pos = pixel_position_s()

                    if CWarMapManager.instance().GetStartPosition(ch.GetMapIndex(), byte(0 if ch.GetGuild().GetID() < dwGuildOpponent else 1), pos):
                        ch.Show(ch.GetMapIndex(), pos.x, pos.y)
                    else:
                        ch.ExitToSavedLocation()

                    ch.PointChange(EPointTypes.LG_POINT_HP, ch.GetMaxHP() - ch.GetHP())
                    ch.PointChange(EPointTypes.LG_POINT_SP, ch.GetMaxSP() - ch.GetSP())
                    ch.ReviveInvisible(5)

                elif subcmd == SCMD_RESTART.SCMD_RESTART_HERE:
                    #sys_log(0, "do_restart: restart here")
                    ch.RestartAtSamePos()
                    ch.PointChange(EPointTypes.LG_POINT_HP, ch.GetMaxHP() - ch.GetHP())
                    ch.PointChange(EPointTypes.LG_POINT_SP, ch.GetMaxSP() - ch.GetSP())
                    ch.ReviveInvisible(5)

                return

        if subcmd == SCMD_RESTART.SCMD_RESTART_TOWN:
            #sys_log(0, "do_restart: restart town")
            pos = pixel_position_s()

            if SECTREE_MANAGER.instance().GetRecallPositionByEmpire(ch.GetMapIndex(), ch.GetEmpire(), pos):
                ch.WarpSet(pos.x, pos.y)
            else:
                ch.WarpSet(Globals.EMPIRE_START_X(ch.GetEmpire()), Globals.EMPIRE_START_Y(ch.GetEmpire()))

            ch.PointChange(EPointTypes.LG_POINT_HP, 50 - ch.GetHP())
            ch.DeathPenalty(1)

        elif subcmd == SCMD_RESTART.SCMD_RESTART_HERE:
            #sys_log(0, "do_restart: restart here")
            ch.RestartAtSamePos()
            ch.PointChange(EPointTypes.LG_POINT_HP, 50 - ch.GetHP())
            ch.DeathPenalty(0)
            ch.ReviveInvisible(5)


    @staticmethod
    def (UnnamedParameter):
        ch.PointChange(EPointTypes.LG_POINT_STAT_RESET_COUNT, 12 - ch.GetPoint(EPointTypes.LG_POINT_STAT_RESET_COUNT))

    @staticmethod
    def (UnnamedParameter):
        arg1 = str(['\0' for _ in range(256)])
        temp_ref_arg1 = RefObject(arg1);
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        Globals.one_argument(argument, temp_ref_arg1, sizeof(arg1))
        arg1 = temp_ref_arg1.arg_value

        if (not arg1[0]) != '\0':
            return

        if ch.IsPolymorphed():
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You cannot change your state as long as you are transformed."))
            return

        if ch.GetPoint(EPointTypes.LG_POINT_STAT_RESET_COUNT) <= 0:
            return

        if not strcmp(arg1, "st"):
            if ch.GetRealPoint(EPointTypes.LG_POINT_ST) <= JobInitialPoints[ch.GetJob()].st:
                return

            ch.SetRealPoint(EPointTypes.LG_POINT_ST, ch.GetRealPoint(EPointTypes.LG_POINT_ST) - 1)
            ch.SetPoint(EPointTypes.LG_POINT_ST, ch.GetPoint(EPointTypes.LG_POINT_ST) - 1)
            ch.ComputePoints()
            ch.PointChange(EPointTypes.LG_POINT_ST, 0)
        elif not strcmp(arg1, "dx"):
            if ch.GetRealPoint(EPointTypes.LG_POINT_DX) <= JobInitialPoints[ch.GetJob()].dx:
                return

            ch.SetRealPoint(EPointTypes.LG_POINT_DX, ch.GetRealPoint(EPointTypes.LG_POINT_DX) - 1)
            ch.SetPoint(EPointTypes.LG_POINT_DX, ch.GetPoint(EPointTypes.LG_POINT_DX) - 1)
            ch.ComputePoints()
            ch.PointChange(EPointTypes.LG_POINT_DX, 0)
        elif not strcmp(arg1, "ht"):
            if ch.GetRealPoint(EPointTypes.LG_POINT_HT) <= JobInitialPoints[ch.GetJob()].ht:
                return

            ch.SetRealPoint(EPointTypes.LG_POINT_HT, ch.GetRealPoint(EPointTypes.LG_POINT_HT) - 1)
            ch.SetPoint(EPointTypes.LG_POINT_HT, ch.GetPoint(EPointTypes.LG_POINT_HT) - 1)
            ch.ComputePoints()
            ch.PointChange(EPointTypes.LG_POINT_HT, 0)
            ch.PointChange(EPointTypes.LG_POINT_MAX_HP, 0)
        elif not strcmp(arg1, "iq"):
            if ch.GetRealPoint(EPointTypes.LG_POINT_IQ) <= JobInitialPoints[ch.GetJob()].iq:
                return

            ch.SetRealPoint(EPointTypes.LG_POINT_IQ, ch.GetRealPoint(EPointTypes.LG_POINT_IQ) - 1)
            ch.SetPoint(EPointTypes.LG_POINT_IQ, ch.GetPoint(EPointTypes.LG_POINT_IQ) - 1)
            ch.ComputePoints()
            ch.PointChange(EPointTypes.LG_POINT_IQ, 0)
            ch.PointChange(EPointTypes.LG_POINT_MAX_SP, 0)
        else:
            return

        ch.PointChange(EPointTypes.LG_POINT_STAT, +1)
        ch.PointChange(EPointTypes.LG_POINT_STAT_RESET_COUNT, -1)
        ch.ComputePoints()

    @staticmethod
    def (UnnamedParameter):
        arg1 = str(['\0' for _ in range(256)])
        temp_ref_arg1 = RefObject(arg1);
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        Globals.one_argument(argument, temp_ref_arg1, sizeof(arg1))
        arg1 = temp_ref_arg1.arg_value

        if (not arg1[0]) != '\0':
            return

        if ch.IsPolymorphed():
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You cannot change your state as long as you are transformed."))
            return

        if ch.GetPoint(EPointTypes.LG_POINT_STAT) <= 0:
            return

        idx = 0

        if not strcmp(arg1, "st"):
            idx = EPointTypes.LG_POINT_ST
        elif not strcmp(arg1, "dx"):
            idx = EPointTypes.LG_POINT_DX
        elif not strcmp(arg1, "ht"):
            idx = EPointTypes.LG_POINT_HT
        elif not strcmp(arg1, "iq"):
            idx = EPointTypes.LG_POINT_IQ
        else:
            return

        if ch.GetRealPoint(idx) >= LGEMiscellaneous.DEFINECONSTANTS.MAX_STAT:
            return

        ch.SetRealPoint(idx, ch.GetRealPoint(idx) + 1)
        ch.SetPoint(idx, ch.GetPoint(idx) + 1)
        ch.ComputePoints()
        ch.PointChange(idx, 0)

        if idx == EPointTypes.LG_POINT_IQ:
            ch.PointChange(EPointTypes.LG_POINT_MAX_HP, 0)
        elif idx == EPointTypes.LG_POINT_HT:
            ch.PointChange(EPointTypes.LG_POINT_MAX_SP, 0)

        ch.PointChange(EPointTypes.LG_POINT_STAT, -1)
        ch.ComputePoints()

    @staticmethod
    def (UnnamedParameter):
        arg1 = str(['\0' for _ in range(256)])
        temp_ref_arg1 = RefObject(arg1);
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        Globals.one_argument(argument, temp_ref_arg1, sizeof(arg1))
        arg1 = temp_ref_arg1.arg_value

        vid = 0
        temp_ref_vid = RefObject(vid);
        Globals.str_to_number(temp_ref_vid, arg1)
        vid = temp_ref_vid.arg_value
        pkVictim = CHARACTER_MANAGER.instance().Find(vid)

        if pkVictim is None:
            return

        if pkVictim.IsNPC():
            return

        CPVPManager.instance().Insert(ch, pkVictim)

    @staticmethod
    def (UnnamedParameter):
        arg1 = str(['\0' for _ in range(256)])
        temp_ref_arg1 = RefObject(arg1);
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        Globals.one_argument(argument, temp_ref_arg1, sizeof(arg1))
        arg1 = temp_ref_arg1.arg_value

        if (not arg1[0]) != '\0':
            return

        if not ch.GetGuild():
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> It does not belong to the Guild."))
            return

        g = ch.GetGuild()
        gm = g.GetMember(ch.GetPlayerID())
        if gm.grade == Globals.GUILD_LEADER_GRADE:
            vnum = 0
            temp_ref_vnum = RefObject(vnum);
            Globals.str_to_number(temp_ref_vnum, arg1)
            vnum = temp_ref_vnum.arg_value
            g.SkillLevelUp(vnum)
        else:
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> You cannot change the Level of the Guild Skills."))

    @staticmethod
    def (UnnamedParameter):
        arg1 = str(['\0' for _ in range(256)])
        temp_ref_arg1 = RefObject(arg1);
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        Globals.one_argument(argument, temp_ref_arg1, sizeof(arg1))
        arg1 = temp_ref_arg1.arg_value

        if (not arg1[0]) != '\0':
            return

        vnum = 0
        temp_ref_vnum = RefObject(vnum);
        Globals.str_to_number(temp_ref_vnum, arg1)
        vnum = temp_ref_vnum.arg_value

        if ((not LGEMiscellaneous.DEFINECONSTANTS.false)) == ch.CanUseSkill(vnum):
            ch.SkillLevelUp(vnum)
        else:



            if (vnum == LaniatusETalentXes.LG_SKILL_HORSE_WILDATTACK) or (vnum == LaniatusETalentXes.LG_SKILL_HORSE_CHARGE) or (vnum == LaniatusETalentXes.LG_SKILL_HORSE_ESCAPE) or (vnum == LaniatusETalentXes.LG_SKILL_HORSE_WILDATTACK_RANGE) or (vnum == LaniatusETalentXes.LG_SKILL_7_A_ANTI_TANHWAN) or (vnum == LaniatusETalentXes.LG_SKILL_7_B_ANTI_AMSEOP) or (vnum == LaniatusETalentXes.LG_SKILL_7_C_ANTI_SWAERYUNG) or (vnum == LaniatusETalentXes.LG_SKILL_7_D_ANTI_YONGBI) or (vnum == LaniatusETalentXes.LG_SKILL_8_A_ANTI_GIGONGCHAM) or (vnum == LaniatusETalentXes.LG_SKILL_8_B_ANTI_YEONSA) or (vnum == LaniatusETalentXes.LG_SKILL_8_C_ANTI_MAHWAN) or (vnum == LaniatusETalentXes.LG_SKILL_8_D_ANTI_BYEURAK) or (vnum == LaniatusETalentXes.LG_SKILL_ADD_HP) or (vnum == LaniatusETalentXes.LG_SKILL_RESIST_PENETRATE):
                ch.SkillLevelUp(vnum)

    @staticmethod
    def (UnnamedParameter):
        ch.CloseSafebox()

    @staticmethod
    def (UnnamedParameter):
        arg1 = str(['\0' for _ in range(256)])
        temp_ref_arg1 = RefObject(arg1);
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        Globals.one_argument(argument, temp_ref_arg1, sizeof(arg1))
        arg1 = temp_ref_arg1.arg_value
        ch.ReqSafeboxLoad(arg1)

    @staticmethod
    def (UnnamedParameter):
        arg1 = str(['\0' for _ in range(256)])
        arg2 = str(['\0' for _ in range(256)])

        temp_ref_arg1 = RefObject(arg1);
        temp_ref_arg2 = RefObject(arg2);
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        Globals.two_arguments(argument, temp_ref_arg1, sizeof(arg1), temp_ref_arg2, sizeof(arg2))
        arg2 = temp_ref_arg2.arg_value
        arg1 = temp_ref_arg1.arg_value

        if (not arg1[0]) != '\0' or len(arg1)>6:
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Storages> You entered a wrong password."))
            return

        if (not arg2[0]) != '\0' or len(arg2)>6:
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Storages> You entered a wrong password."))
            return

        p = SSafeboxChangePasswordPacket()

        p.dwID = ch.GetDesc().GetAccountTable().id
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        strncpy_s(p.szOldPassword, sizeof(p.szOldPassword), arg1, _TRUNCATE)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        strncpy_s(p.szNewPassword, sizeof(p.szNewPassword), arg2, _TRUNCATE)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        db_clientdesc.DBPacket(Globals.LG_HEADER_GD_SAFEBOX_CHANGE_PASSWORD, ch.GetDesc().GetHandle(), p, sizeof(p))

    @staticmethod
    def (UnnamedParameter):
        arg1 = str(['\0' for _ in range(256)])
        temp_ref_arg1 = RefObject(arg1);
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        Globals.one_argument(argument, temp_ref_arg1, sizeof(arg1))
        arg1 = temp_ref_arg1.arg_value

        if (not arg1[0]) != '\0' or len(arg1) > 6:
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Storages> You entered a wrong password."))
            return

        iPulse = Globals.thecore_pulse()

        if ch.GetMall():
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Storages> The storage is already open."))
            return

        if iPulse - ch.GetMallLoadTime() < passes_per_sec * 10:
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Storages> You have to wait 10 seconds to open the storage again."))
            return

        ch.SetMallLoadTime(iPulse)

        p = SSafeboxLoadPacket()
        p.dwID = ch.GetDesc().GetAccountTable().id
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        strncpy_s(p.szLogin, sizeof(p.szLogin), ch.GetDesc().GetAccountTable().login, _TRUNCATE)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        strncpy_s(p.szPassword, sizeof(p.szPassword), arg1, _TRUNCATE)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        db_clientdesc.DBPacket(Globals.LG_HEADER_GD_MALL_LOAD, ch.GetDesc().GetHandle(), p, sizeof(p))

    @staticmethod
    def (UnnamedParameter):
        if ch.GetMall():
            ch.SetMallLoadTime(Globals.thecore_pulse())
            ch.CloseMall()
            ch.Save()

    @staticmethod
    def (UnnamedParameter):
        if not ch.GetParty():
            return

        if not CPartyManager.instance().IsEnablePCParty():
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Group> The server cannot execute the Group request."))
            return

        if ch.GetDungeon():
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Group> You cannot leave a Group while you are in a dungeon."))
            return

        pParty = ch.GetParty()

        if pParty.GetMemberCount() == 2:
            CPartyManager.instance().DeleteParty(pParty)
        else:
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Group> You left the Group."))
            pParty.Quit(ch.GetPlayerID())

    @staticmethod
    def (UnnamedParameter):
        if ch.GetMyShop():
            ch.CloseMyShop()
            return

    @staticmethod
    def (UnnamedParameter):
        ch.SetNowWalking(((not LGEMiscellaneous.DEFINECONSTANTS.false)))
        ch.SetWalking(((not LGEMiscellaneous.DEFINECONSTANTS.false)))

    @staticmethod
    def (UnnamedParameter):
        ch.SetNowWalking(LGEMiscellaneous.DEFINECONSTANTS.false)
        ch.SetWalking(LGEMiscellaneous.DEFINECONSTANTS.false)

    @staticmethod
    def (UnnamedParameter):
        g = ch.GetGuild()

        if g is None:
            return

        if g.UnderAnyWar(GUILD_WAR_TYPE_MAX_NUM) != 0:
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> Your Guild is already participating in another war."))
            return

        arg1 = str(['\0' for _ in range(256)])
        arg2 = str(['\0' for _ in range(256)])
        type = EGuildWarType.GUILD_WAR_TYPE_FIELD
        temp_ref_arg1 = RefObject(arg1);
        temp_ref_arg2 = RefObject(arg2);
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        Globals.two_arguments(argument, temp_ref_arg1, sizeof(arg1), temp_ref_arg2, sizeof(arg2))
        arg2 = temp_ref_arg2.arg_value
        arg1 = temp_ref_arg1.arg_value

        if (not arg1[0]) != '\0':
            return

        if arg2[0] != '\0':
            temp_ref_type = RefObject(type);
            Globals.str_to_number(temp_ref_type, arg2)
            type = temp_ref_type.arg_value

            if type >= EGuildWarType.GUILD_WAR_TYPE_MAX_NUM:
                type = EGuildWarType.GUILD_WAR_TYPE_FIELD

            if type < 0:
                return

        gm_pid = g.GetMasterPID()

        if gm_pid != ch.GetPlayerID():
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> You are not entitled to declare a Guild war."))
            return

        opp_g = CGuildManager.instance().FindGuildByName(arg1)

        if opp_g is None:
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> This Guild does not exist."))
            return

        if g.GetGuildWarState(opp_g.GetID()) == EGuildWarState.GUILD_WAR_NONE:
                if opp_g.UnderAnyWar(GUILD_WAR_TYPE_MAX_NUM) != 0:
                    ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> This Guild is already participating in a war."))
                    return

                iWarPrice = KOR_aGuildWarInfo[type].iWarPrice

                if g.GetGuildMoney() < iWarPrice:
                    ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> There is not enough Yang to participate in a Guild war."))
                    return

                if opp_g.GetGuildMoney() < iWarPrice:
                    ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> The Guild does not have enough Yang to participate in a Guild war."))
                    return

        elif g.GetGuildWarState(opp_g.GetID()) == EGuildWarState.GUILD_WAR_SEND_DECLARE:
                ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You already declared war on this Guild."))
                return

        elif g.GetGuildWarState(opp_g.GetID()) == EGuildWarState.GUILD_WAR_RECV_DECLARE:
                if opp_g.UnderAnyWar(GUILD_WAR_TYPE_MAX_NUM) != 0:
                    ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> This Guild is already participating in a war."))
                    g.RequestRefuseWar(opp_g.GetID())
                    return

        elif g.GetGuildWarState(opp_g.GetID()) == EGuildWarState.GUILD_WAR_RESERVE:
                ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> This Guild is already noted for another Guild war."))
                return

        elif g.GetGuildWarState(opp_g.GetID()) == EGuildWarState.GUILD_WAR_END:
            return


        if g.GetGuildWarState(opp_g.GetID()) != GUILD_WAR_NONE and g.GetGuildWarState(opp_g.GetID()) != GUILD_WAR_SEND_DECLARE and g.GetGuildWarState(opp_g.GetID()) != GUILD_WAR_RECV_DECLARE and g.GetGuildWarState(opp_g.GetID()) != GUILD_WAR_RESERVE:
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> This Guild is already participating in another war."))
            g.RequestRefuseWar(opp_g.GetID())
            return

        if not g.CanStartWar(byte(type)):
            if g.GetLadderPoint() == 0:
                ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> Rank is too low to participate in a Guild war."))
                #sys_log(0, "GuildWar.StartError.NEED_LADDER_POINT")
            elif g.GetMemberCount() < Globals.GUILD_WAR_MIN_MEMBER_COUNT:
                ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> At least %d players have to participate in a Guild war."), Globals.GUILD_WAR_MIN_MEMBER_COUNT)
                Globals.#sys_log(0, "GuildWar.StartError.NEED_MINIMUM_MEMBER[%d]", Globals.GUILD_WAR_MIN_MEMBER_COUNT)
            else:
                #sys_log(0, "GuildWar.StartError.UNKNOWN_ERROR")
            return

        if not opp_g.CanStartWar(EGuildWarType.GUILD_WAR_TYPE_FIELD):
            if opp_g.GetLadderPoint() == 0:
                ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> The Guild does not have enough Rank Points to participate in a Guild war."))
            elif opp_g.GetMemberCount() < Globals.GUILD_WAR_MIN_MEMBER_COUNT:
                ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> The Guild does not have enough members to participate in a Guild war."))
            return

        condition = True
        while condition:
            if g.GetMasterCharacter() is not None:
                break

            pCCI = P2P_MANAGER.instance().FindByPID(g.GetMasterPID())

            if pCCI is not None:
                break

            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> The Guild master is not online."))
            g.RequestRefuseWar(opp_g.GetID())
            return

            condition = LGEMiscellaneous.DEFINECONSTANTS.false

        condition = True
        while condition:
            if opp_g.GetMasterCharacter() is not None:
                break

            pCCI = P2P_MANAGER.instance().FindByPID(opp_g.GetMasterPID())

            if pCCI is not None:
                break

            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> The Guild master is not online."))
            g.RequestRefuseWar(opp_g.GetID())
            return

            condition = LGEMiscellaneous.DEFINECONSTANTS.false

        g.RequestDeclareWar(opp_g.GetID(), byte(type))

    @staticmethod
    def (UnnamedParameter):
        g = ch.GetGuild()
        if g is None:
            return

        arg1 = str(['\0' for _ in range(256)])
        temp_ref_arg1 = RefObject(arg1);
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        Globals.one_argument(argument, temp_ref_arg1, sizeof(arg1))
        arg1 = temp_ref_arg1.arg_value

        if (not arg1[0]) != '\0':
            return

        gm_pid = g.GetMasterPID()

        if gm_pid != ch.GetPlayerID():
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> You are not entitled to declare a Guild war."))
            return

        opp_g = CGuildManager.instance().FindGuildByName(arg1)

        if opp_g is None:
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> This Guild does not exist."))
            return

        g.RequestRefuseWar(opp_g.GetID())

    @staticmethod
    def (UnnamedParameter):
        arg1 = str(['\0' for _ in range(256)])
        temp_ref_arg1 = RefObject(arg1);
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        Globals.one_argument(argument, temp_ref_arg1, sizeof(arg1))
        arg1 = temp_ref_arg1.arg_value

        if (not arg1[0]) != '\0':
            return

        mode = 0
        temp_ref_mode = RefObject(mode);
        Globals.str_to_number(temp_ref_mode, arg1)
        mode = temp_ref_mode.arg_value

        if mode == EPKModes.PK_MODE_PROTECT:
            return

        if ch.GetLevel() < PK_PROTECT_LEVEL and mode != 0:
            return

        ch.SetPKMode(mode)

    @staticmethod
    def (UnnamedParameter):
        arg1 = str(['\0' for _ in range(256)])
        arg2 = str(['\0' for _ in range(256)])
        temp_ref_arg1 = RefObject(arg1);
        temp_ref_arg2 = RefObject(arg2);
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        Globals.two_arguments(argument, temp_ref_arg1, sizeof(arg1), temp_ref_arg2, sizeof(arg2))
        arg2 = temp_ref_arg2.arg_value
        arg1 = temp_ref_arg1.arg_value

        if (not arg1[0]) != '\0' or (not arg2[0]) != '\0':
            return

        answer = LOWERarg1

        if not MessengerManager.instance().AuthToAdd(ch.GetName(), arg2,LGEMiscellaneous.DEFINECONSTANTS.false if answer == 'y' else ((not LGEMiscellaneous.DEFINECONSTANTS.false))):
            return

        if answer != 'y':
            tch = CHARACTER_MANAGER.instance().FindPC(arg2)

            if tch:
                tch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Messenger> %s rejected your request."), ch.GetName())

    @staticmethod
    def (UnnamedParameter):
        arg1 = str(['\0' for _ in range(256)])
        temp_ref_arg1 = RefObject(arg1);
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        Globals.one_argument(argument, temp_ref_arg1, sizeof(arg1))
        arg1 = temp_ref_arg1.arg_value

        if arg1[0] != '\0':
            flag = 0
            temp_ref_flag = RefObject(flag);
            Globals.str_to_number(temp_ref_flag, arg1)
            flag = temp_ref_flag.arg_value
            ch.SetBlockMode(flag)

    @staticmethod
    def (UnnamedParameter):
        arg1 = str(['\0' for _ in range(256)])
        arg2 = str(['\0' for _ in range(256)])

        temp_ref_arg1 = RefObject(arg1);
        temp_ref_arg2 = RefObject(arg2);
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        Globals.two_arguments(argument, temp_ref_arg1, sizeof(arg1), temp_ref_arg2, sizeof(arg2))
        arg2 = temp_ref_arg2.arg_value
        arg1 = temp_ref_arg1.arg_value

        if arg1[0] != '\0' and arg2[0] != '\0' and arg1.isdigit() and arg2.isdigit():
            mode = None
            flag = None

            temp_ref_mode = RefObject(mode);
            Globals.str_to_number(temp_ref_mode, arg1)
            mode = temp_ref_mode.arg_value
            temp_ref_flag = RefObject(flag);
            Globals.str_to_number(temp_ref_flag, arg2)
            flag = temp_ref_flag.arg_value

            ch.SetPickupMode(mode)
            ch.SetPickupBlockFlag(flag)

    @staticmethod
    def (UnnamedParameter):
        if ((not LGEMiscellaneous.DEFINECONSTANTS.false)) == ch.UnEquipSpecialRideUniqueItem():
            ch.RemoveAffect(LaniatusEAffectTypes.LANIA_AFFECT_MOUNT)
            ch.RemoveAffect(LaniatusEAffectTypes.LANIA_AFFECT_MOUNT_BONUS)

            if ch.IsHorseRiding():
                ch.StopRiding()
        else:
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Your inventory is full."))


    @staticmethod
    def (UnnamedParameter):
        if ch.GetGMLevel() <= EGMLevels.GM_PLAYER:
            return

        arg1 = str(['\0' for _ in range(256)])
        temp_ref_arg1 = RefObject(arg1);
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        Globals.one_argument(argument, temp_ref_arg1, sizeof(arg1))
        arg1 = temp_ref_arg1.arg_value

        if arg1[0] != '\0':
            vid = 0
            temp_ref_vid = RefObject(vid);
            Globals.str_to_number(temp_ref_vid, arg1)
            vid = temp_ref_vid.arg_value
            tch = CHARACTER_MANAGER.instance().Find(vid)

            if tch is None:
                return

            if not tch.IsPC():
                return

            tch.SendEquipment(ch)

    @staticmethod
    def (UnnamedParameter):
        if ch.GetParty():
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You cannot accept the invitation because you are already in the Group."))
            return

        arg1 = str(['\0' for _ in range(256)])
        temp_ref_arg1 = RefObject(arg1);
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        Globals.one_argument(argument, temp_ref_arg1, sizeof(arg1))
        arg1 = temp_ref_arg1.arg_value

        if (not arg1[0]) != '\0':
            return

        vid = 0
        temp_ref_vid = RefObject(vid);
        Globals.str_to_number(temp_ref_vid, arg1)
        vid = temp_ref_vid.arg_value
        tch = CHARACTER_MANAGER.instance().Find(vid)

        if tch:
            if not ch.RequestToParty(tch):
                ch.ChatPacket(EChatType.CHAT_TYPE_COMMAND, "PartyRequestDenied")

    @staticmethod
    def (UnnamedParameter):
        arg1 = str(['\0' for _ in range(256)])
        temp_ref_arg1 = RefObject(arg1);
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        Globals.one_argument(argument, temp_ref_arg1, sizeof(arg1))
        arg1 = temp_ref_arg1.arg_value

        if (not arg1[0]) != '\0':
            return

        vid = 0
        temp_ref_vid = RefObject(vid);
        Globals.str_to_number(temp_ref_vid, arg1)
        vid = temp_ref_vid.arg_value
        tch = CHARACTER_MANAGER.instance().Find(vid)

        if tch:
            ch.AcceptToParty(tch)

    @staticmethod
    def (UnnamedParameter):
        arg1 = str(['\0' for _ in range(256)])
        temp_ref_arg1 = RefObject(arg1);
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        Globals.one_argument(argument, temp_ref_arg1, sizeof(arg1))
        arg1 = temp_ref_arg1.arg_value

        if (not arg1[0]) != '\0':
            return

        vid = 0
        temp_ref_vid = RefObject(vid);
        Globals.str_to_number(temp_ref_vid, arg1)
        vid = temp_ref_vid.arg_value
        tch = CHARACTER_MANAGER.instance().Find(vid)

        if tch:
            ch.DenyToParty(tch)

    @staticmethod
    def FN_LG_POINT_string(apply_number):
        if apply_number == EPointTypes.LG_POINT_MAX_HP:
            return LC_TEXT("Energy Points +%d")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP):
            return LC_TEXT("Mana Points +%d")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT):
            return LC_TEXT("Endurance +%d")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ):
            return LC_TEXT("Intelligence +%d")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST):
            return LC_TEXT("Strength +%d")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX):
            return LC_TEXT("Agility +%d")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED):
            return LC_TEXT("Attack Speed +%d")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED):
            return LC_TEXT("Moving Speed %d")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED):
            return LC_TEXT("Cooldown Time -%d")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN):
            return LC_TEXT("Energy Recovery +%d")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN):
            return LC_TEXT("Spell Point Recovery +%d")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT):
            return LC_TEXT("Poison Attack %d")
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##if ENABLE_WOLFMAN
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT):
            return LC_TEXT("Poison Attack %d")
    ##endif
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT):
            return LC_TEXT("Stun +%d")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT):
            return LC_TEXT("Speed Reducing +%d")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT):
            return LC_TEXT("Critical Attack with a chance of %d%%")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_CRITICAL):
            return LC_TEXT("Critical damage reduction %d%%")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_CRITICAL) or (apply_number == EPointTypes.LG_POINT_PENETRATE_PCT):
            return LC_TEXT("%d%% chance to thrusting attack")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_CRITICAL) or (apply_number == EPointTypes.LG_POINT_PENETRATE_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_PENETRATE):
            return LC_TEXT("thrust damage reduction %d%%")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_CRITICAL) or (apply_number == EPointTypes.LG_POINT_PENETRATE_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_PENETRATE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_HUMAN):
            return LC_TEXT("Player Attack Power against Monster +%d%%")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_CRITICAL) or (apply_number == EPointTypes.LG_POINT_PENETRATE_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_PENETRATE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_HUMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ANIMAL):
            return LC_TEXT("Horse Attack Power against Monster +%d%%")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_CRITICAL) or (apply_number == EPointTypes.LG_POINT_PENETRATE_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_PENETRATE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_HUMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ANIMAL) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ORC):
            return LC_TEXT("Attack Boost against Orc + %d%%")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_CRITICAL) or (apply_number == EPointTypes.LG_POINT_PENETRATE_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_PENETRATE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_HUMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ANIMAL) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ORC) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MILGYO):
            return LC_TEXT("Attack Boost against Esoteric + %d%%")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_CRITICAL) or (apply_number == EPointTypes.LG_POINT_PENETRATE_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_PENETRATE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_HUMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ANIMAL) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ORC) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MILGYO) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_UNDEAD):
            return LC_TEXT("Attack Boost against Undead + %d%%")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_CRITICAL) or (apply_number == EPointTypes.LG_POINT_PENETRATE_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_PENETRATE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_HUMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ANIMAL) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ORC) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MILGYO) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_UNDEAD) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_DEVIL):
            return LC_TEXT("Attack Boost against Devil + %d%%")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_CRITICAL) or (apply_number == EPointTypes.LG_POINT_PENETRATE_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_PENETRATE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_HUMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ANIMAL) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ORC) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MILGYO) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_UNDEAD) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_DEVIL) or (apply_number == EPointTypes.LG_POINT_STEAL_HP):
            return LC_TEXT("Absorbing of HP %d%% while attacking.")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_CRITICAL) or (apply_number == EPointTypes.LG_POINT_PENETRATE_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_PENETRATE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_HUMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ANIMAL) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ORC) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MILGYO) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_UNDEAD) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_DEVIL) or (apply_number == EPointTypes.LG_POINT_STEAL_HP) or (apply_number == EPointTypes.LG_POINT_STEAL_SP):
            return LC_TEXT("Absorbing of Mana %d%% while attacking.")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_CRITICAL) or (apply_number == EPointTypes.LG_POINT_PENETRATE_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_PENETRATE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_HUMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ANIMAL) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ORC) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MILGYO) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_UNDEAD) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_DEVIL) or (apply_number == EPointTypes.LG_POINT_STEAL_HP) or (apply_number == EPointTypes.LG_POINT_STEAL_SP) or (apply_number == EPointTypes.LG_POINT_MANA_BURN_PCT):
            return LC_TEXT("With a chance of %d%% Mana will be taken from the enemy.")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_CRITICAL) or (apply_number == EPointTypes.LG_POINT_PENETRATE_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_PENETRATE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_HUMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ANIMAL) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ORC) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MILGYO) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_UNDEAD) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_DEVIL) or (apply_number == EPointTypes.LG_POINT_STEAL_HP) or (apply_number == EPointTypes.LG_POINT_STEAL_SP) or (apply_number == EPointTypes.LG_POINT_MANA_BURN_PCT) or (apply_number == EPointTypes.LG_POINT_DAMAGE_SP_RECOVER):
            return LC_TEXT("Absorbing of Spell Points with a chance of %d%% .")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_CRITICAL) or (apply_number == EPointTypes.LG_POINT_PENETRATE_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_PENETRATE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_HUMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ANIMAL) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ORC) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MILGYO) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_UNDEAD) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_DEVIL) or (apply_number == EPointTypes.LG_POINT_STEAL_HP) or (apply_number == EPointTypes.LG_POINT_STEAL_SP) or (apply_number == EPointTypes.LG_POINT_MANA_BURN_PCT) or (apply_number == EPointTypes.LG_POINT_DAMAGE_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_BLOCK):
            return LC_TEXT("%d%% Chance to block a Close Combat Attack.")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_CRITICAL) or (apply_number == EPointTypes.LG_POINT_PENETRATE_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_PENETRATE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_HUMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ANIMAL) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ORC) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MILGYO) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_UNDEAD) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_DEVIL) or (apply_number == EPointTypes.LG_POINT_STEAL_HP) or (apply_number == EPointTypes.LG_POINT_STEAL_SP) or (apply_number == EPointTypes.LG_POINT_MANA_BURN_PCT) or (apply_number == EPointTypes.LG_POINT_DAMAGE_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_BLOCK) or (apply_number == EPointTypes.LG_POINT_DODGE):
            return LC_TEXT("To block a Distance Attack there is a chance of %d%%")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_CRITICAL) or (apply_number == EPointTypes.LG_POINT_PENETRATE_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_PENETRATE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_HUMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ANIMAL) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ORC) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MILGYO) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_UNDEAD) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_DEVIL) or (apply_number == EPointTypes.LG_POINT_STEAL_HP) or (apply_number == EPointTypes.LG_POINT_STEAL_SP) or (apply_number == EPointTypes.LG_POINT_MANA_BURN_PCT) or (apply_number == EPointTypes.LG_POINT_DAMAGE_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_BLOCK) or (apply_number == EPointTypes.LG_POINT_DODGE) or (apply_number == EPointTypes.LG_POINT_RESIST_SWORD):
            return LC_TEXT("Sword Defence %d%%")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_CRITICAL) or (apply_number == EPointTypes.LG_POINT_PENETRATE_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_PENETRATE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_HUMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ANIMAL) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ORC) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MILGYO) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_UNDEAD) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_DEVIL) or (apply_number == EPointTypes.LG_POINT_STEAL_HP) or (apply_number == EPointTypes.LG_POINT_STEAL_SP) or (apply_number == EPointTypes.LG_POINT_MANA_BURN_PCT) or (apply_number == EPointTypes.LG_POINT_DAMAGE_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_BLOCK) or (apply_number == EPointTypes.LG_POINT_DODGE) or (apply_number == EPointTypes.LG_POINT_RESIST_SWORD) or (apply_number == EPointTypes.LG_POINT_RESIST_TWOHAND):
            return LC_TEXT("Two-Handed Sword Defence %d%%")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_CRITICAL) or (apply_number == EPointTypes.LG_POINT_PENETRATE_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_PENETRATE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_HUMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ANIMAL) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ORC) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MILGYO) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_UNDEAD) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_DEVIL) or (apply_number == EPointTypes.LG_POINT_STEAL_HP) or (apply_number == EPointTypes.LG_POINT_STEAL_SP) or (apply_number == EPointTypes.LG_POINT_MANA_BURN_PCT) or (apply_number == EPointTypes.LG_POINT_DAMAGE_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_BLOCK) or (apply_number == EPointTypes.LG_POINT_DODGE) or (apply_number == EPointTypes.LG_POINT_RESIST_SWORD) or (apply_number == EPointTypes.LG_POINT_RESIST_TWOHAND) or (apply_number == EPointTypes.LG_POINT_RESIST_DAGGER):
            return LC_TEXT("Two-Handed Sword Defence %d%%")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_CRITICAL) or (apply_number == EPointTypes.LG_POINT_PENETRATE_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_PENETRATE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_HUMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ANIMAL) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ORC) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MILGYO) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_UNDEAD) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_DEVIL) or (apply_number == EPointTypes.LG_POINT_STEAL_HP) or (apply_number == EPointTypes.LG_POINT_STEAL_SP) or (apply_number == EPointTypes.LG_POINT_MANA_BURN_PCT) or (apply_number == EPointTypes.LG_POINT_DAMAGE_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_BLOCK) or (apply_number == EPointTypes.LG_POINT_DODGE) or (apply_number == EPointTypes.LG_POINT_RESIST_SWORD) or (apply_number == EPointTypes.LG_POINT_RESIST_TWOHAND) or (apply_number == EPointTypes.LG_POINT_RESIST_DAGGER) or (apply_number == EPointTypes.LG_POINT_RESIST_BELL):
            return LC_TEXT("Bell Defence %d%%")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_CRITICAL) or (apply_number == EPointTypes.LG_POINT_PENETRATE_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_PENETRATE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_HUMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ANIMAL) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ORC) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MILGYO) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_UNDEAD) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_DEVIL) or (apply_number == EPointTypes.LG_POINT_STEAL_HP) or (apply_number == EPointTypes.LG_POINT_STEAL_SP) or (apply_number == EPointTypes.LG_POINT_MANA_BURN_PCT) or (apply_number == EPointTypes.LG_POINT_DAMAGE_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_BLOCK) or (apply_number == EPointTypes.LG_POINT_DODGE) or (apply_number == EPointTypes.LG_POINT_RESIST_SWORD) or (apply_number == EPointTypes.LG_POINT_RESIST_TWOHAND) or (apply_number == EPointTypes.LG_POINT_RESIST_DAGGER) or (apply_number == EPointTypes.LG_POINT_RESIST_BELL) or (apply_number == EPointTypes.LG_POINT_RESIST_FAN):
            return LC_TEXT("Fan Defence %d%%")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_CRITICAL) or (apply_number == EPointTypes.LG_POINT_PENETRATE_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_PENETRATE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_HUMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ANIMAL) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ORC) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MILGYO) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_UNDEAD) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_DEVIL) or (apply_number == EPointTypes.LG_POINT_STEAL_HP) or (apply_number == EPointTypes.LG_POINT_STEAL_SP) or (apply_number == EPointTypes.LG_POINT_MANA_BURN_PCT) or (apply_number == EPointTypes.LG_POINT_DAMAGE_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_BLOCK) or (apply_number == EPointTypes.LG_POINT_DODGE) or (apply_number == EPointTypes.LG_POINT_RESIST_SWORD) or (apply_number == EPointTypes.LG_POINT_RESIST_TWOHAND) or (apply_number == EPointTypes.LG_POINT_RESIST_DAGGER) or (apply_number == EPointTypes.LG_POINT_RESIST_BELL) or (apply_number == EPointTypes.LG_POINT_RESIST_FAN) or (apply_number == EPointTypes.LG_POINT_RESIST_BOW):
            return LC_TEXT("Distant Attack Resistance %d%%")
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##if ENABLE_WOLFMAN
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_CRITICAL) or (apply_number == EPointTypes.LG_POINT_PENETRATE_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_PENETRATE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_HUMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ANIMAL) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ORC) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MILGYO) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_UNDEAD) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_DEVIL) or (apply_number == EPointTypes.LG_POINT_STEAL_HP) or (apply_number == EPointTypes.LG_POINT_STEAL_SP) or (apply_number == EPointTypes.LG_POINT_MANA_BURN_PCT) or (apply_number == EPointTypes.LG_POINT_DAMAGE_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_BLOCK) or (apply_number == EPointTypes.LG_POINT_DODGE) or (apply_number == EPointTypes.LG_POINT_RESIST_SWORD) or (apply_number == EPointTypes.LG_POINT_RESIST_TWOHAND) or (apply_number == EPointTypes.LG_POINT_RESIST_DAGGER) or (apply_number == EPointTypes.LG_POINT_RESIST_BELL) or (apply_number == EPointTypes.LG_POINT_RESIST_FAN) or (apply_number == EPointTypes.LG_POINT_RESIST_BOW) or (apply_number == EPointTypes.LG_POINT_RESIST_CLAW):
            return LC_TEXT("Two-Handed Sword Defence %d%%")
    ##endif
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_CRITICAL) or (apply_number == EPointTypes.LG_POINT_PENETRATE_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_PENETRATE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_HUMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ANIMAL) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ORC) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MILGYO) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_UNDEAD) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_DEVIL) or (apply_number == EPointTypes.LG_POINT_STEAL_HP) or (apply_number == EPointTypes.LG_POINT_STEAL_SP) or (apply_number == EPointTypes.LG_POINT_MANA_BURN_PCT) or (apply_number == EPointTypes.LG_POINT_DAMAGE_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_BLOCK) or (apply_number == EPointTypes.LG_POINT_DODGE) or (apply_number == EPointTypes.LG_POINT_RESIST_SWORD) or (apply_number == EPointTypes.LG_POINT_RESIST_TWOHAND) or (apply_number == EPointTypes.LG_POINT_RESIST_DAGGER) or (apply_number == EPointTypes.LG_POINT_RESIST_BELL) or (apply_number == EPointTypes.LG_POINT_RESIST_FAN) or (apply_number == EPointTypes.LG_POINT_RESIST_BOW) or (apply_number == EPointTypes.LG_POINT_RESIST_CLAW) or (apply_number == EPointTypes.LG_POINT_RESIST_FIRE):
            return LC_TEXT("Fire Resistance %d%%")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_CRITICAL) or (apply_number == EPointTypes.LG_POINT_PENETRATE_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_PENETRATE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_HUMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ANIMAL) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ORC) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MILGYO) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_UNDEAD) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_DEVIL) or (apply_number == EPointTypes.LG_POINT_STEAL_HP) or (apply_number == EPointTypes.LG_POINT_STEAL_SP) or (apply_number == EPointTypes.LG_POINT_MANA_BURN_PCT) or (apply_number == EPointTypes.LG_POINT_DAMAGE_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_BLOCK) or (apply_number == EPointTypes.LG_POINT_DODGE) or (apply_number == EPointTypes.LG_POINT_RESIST_SWORD) or (apply_number == EPointTypes.LG_POINT_RESIST_TWOHAND) or (apply_number == EPointTypes.LG_POINT_RESIST_DAGGER) or (apply_number == EPointTypes.LG_POINT_RESIST_BELL) or (apply_number == EPointTypes.LG_POINT_RESIST_FAN) or (apply_number == EPointTypes.LG_POINT_RESIST_BOW) or (apply_number == EPointTypes.LG_POINT_RESIST_CLAW) or (apply_number == EPointTypes.LG_POINT_RESIST_FIRE) or (apply_number == EPointTypes.LG_POINT_RESIST_ELEC):
            return LC_TEXT("Lightning Resistance %d%%")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_CRITICAL) or (apply_number == EPointTypes.LG_POINT_PENETRATE_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_PENETRATE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_HUMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ANIMAL) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ORC) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MILGYO) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_UNDEAD) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_DEVIL) or (apply_number == EPointTypes.LG_POINT_STEAL_HP) or (apply_number == EPointTypes.LG_POINT_STEAL_SP) or (apply_number == EPointTypes.LG_POINT_MANA_BURN_PCT) or (apply_number == EPointTypes.LG_POINT_DAMAGE_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_BLOCK) or (apply_number == EPointTypes.LG_POINT_DODGE) or (apply_number == EPointTypes.LG_POINT_RESIST_SWORD) or (apply_number == EPointTypes.LG_POINT_RESIST_TWOHAND) or (apply_number == EPointTypes.LG_POINT_RESIST_DAGGER) or (apply_number == EPointTypes.LG_POINT_RESIST_BELL) or (apply_number == EPointTypes.LG_POINT_RESIST_FAN) or (apply_number == EPointTypes.LG_POINT_RESIST_BOW) or (apply_number == EPointTypes.LG_POINT_RESIST_CLAW) or (apply_number == EPointTypes.LG_POINT_RESIST_FIRE) or (apply_number == EPointTypes.LG_POINT_RESIST_ELEC) or (apply_number == EPointTypes.LG_POINT_RESIST_MAGIC):
            return LC_TEXT("Magic Resistance %d%%")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_CRITICAL) or (apply_number == EPointTypes.LG_POINT_PENETRATE_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_PENETRATE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_HUMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ANIMAL) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ORC) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MILGYO) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_UNDEAD) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_DEVIL) or (apply_number == EPointTypes.LG_POINT_STEAL_HP) or (apply_number == EPointTypes.LG_POINT_STEAL_SP) or (apply_number == EPointTypes.LG_POINT_MANA_BURN_PCT) or (apply_number == EPointTypes.LG_POINT_DAMAGE_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_BLOCK) or (apply_number == EPointTypes.LG_POINT_DODGE) or (apply_number == EPointTypes.LG_POINT_RESIST_SWORD) or (apply_number == EPointTypes.LG_POINT_RESIST_TWOHAND) or (apply_number == EPointTypes.LG_POINT_RESIST_DAGGER) or (apply_number == EPointTypes.LG_POINT_RESIST_BELL) or (apply_number == EPointTypes.LG_POINT_RESIST_FAN) or (apply_number == EPointTypes.LG_POINT_RESIST_BOW) or (apply_number == EPointTypes.LG_POINT_RESIST_CLAW) or (apply_number == EPointTypes.LG_POINT_RESIST_FIRE) or (apply_number == EPointTypes.LG_POINT_RESIST_ELEC) or (apply_number == EPointTypes.LG_POINT_RESIST_MAGIC) or (apply_number == EPointTypes.LG_POINT_RESIST_WIND):
            return LC_TEXT("Wind Resistance %d%%")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_CRITICAL) or (apply_number == EPointTypes.LG_POINT_PENETRATE_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_PENETRATE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_HUMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ANIMAL) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ORC) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MILGYO) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_UNDEAD) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_DEVIL) or (apply_number == EPointTypes.LG_POINT_STEAL_HP) or (apply_number == EPointTypes.LG_POINT_STEAL_SP) or (apply_number == EPointTypes.LG_POINT_MANA_BURN_PCT) or (apply_number == EPointTypes.LG_POINT_DAMAGE_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_BLOCK) or (apply_number == EPointTypes.LG_POINT_DODGE) or (apply_number == EPointTypes.LG_POINT_RESIST_SWORD) or (apply_number == EPointTypes.LG_POINT_RESIST_TWOHAND) or (apply_number == EPointTypes.LG_POINT_RESIST_DAGGER) or (apply_number == EPointTypes.LG_POINT_RESIST_BELL) or (apply_number == EPointTypes.LG_POINT_RESIST_FAN) or (apply_number == EPointTypes.LG_POINT_RESIST_BOW) or (apply_number == EPointTypes.LG_POINT_RESIST_CLAW) or (apply_number == EPointTypes.LG_POINT_RESIST_FIRE) or (apply_number == EPointTypes.LG_POINT_RESIST_ELEC) or (apply_number == EPointTypes.LG_POINT_RESIST_MAGIC) or (apply_number == EPointTypes.LG_POINT_RESIST_WIND) or (apply_number == EPointTypes.LG_POINT_RESIST_ICE):
            return LC_TEXT("�ñ� ���� %d%%")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_CRITICAL) or (apply_number == EPointTypes.LG_POINT_PENETRATE_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_PENETRATE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_HUMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ANIMAL) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ORC) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MILGYO) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_UNDEAD) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_DEVIL) or (apply_number == EPointTypes.LG_POINT_STEAL_HP) or (apply_number == EPointTypes.LG_POINT_STEAL_SP) or (apply_number == EPointTypes.LG_POINT_MANA_BURN_PCT) or (apply_number == EPointTypes.LG_POINT_DAMAGE_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_BLOCK) or (apply_number == EPointTypes.LG_POINT_DODGE) or (apply_number == EPointTypes.LG_POINT_RESIST_SWORD) or (apply_number == EPointTypes.LG_POINT_RESIST_TWOHAND) or (apply_number == EPointTypes.LG_POINT_RESIST_DAGGER) or (apply_number == EPointTypes.LG_POINT_RESIST_BELL) or (apply_number == EPointTypes.LG_POINT_RESIST_FAN) or (apply_number == EPointTypes.LG_POINT_RESIST_BOW) or (apply_number == EPointTypes.LG_POINT_RESIST_CLAW) or (apply_number == EPointTypes.LG_POINT_RESIST_FIRE) or (apply_number == EPointTypes.LG_POINT_RESIST_ELEC) or (apply_number == EPointTypes.LG_POINT_RESIST_MAGIC) or (apply_number == EPointTypes.LG_POINT_RESIST_WIND) or (apply_number == EPointTypes.LG_POINT_RESIST_ICE) or (apply_number == EPointTypes.LG_POINT_RESIST_EARTH):
            return LC_TEXT("���� ���� %d%%")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_CRITICAL) or (apply_number == EPointTypes.LG_POINT_PENETRATE_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_PENETRATE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_HUMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ANIMAL) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ORC) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MILGYO) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_UNDEAD) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_DEVIL) or (apply_number == EPointTypes.LG_POINT_STEAL_HP) or (apply_number == EPointTypes.LG_POINT_STEAL_SP) or (apply_number == EPointTypes.LG_POINT_MANA_BURN_PCT) or (apply_number == EPointTypes.LG_POINT_DAMAGE_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_BLOCK) or (apply_number == EPointTypes.LG_POINT_DODGE) or (apply_number == EPointTypes.LG_POINT_RESIST_SWORD) or (apply_number == EPointTypes.LG_POINT_RESIST_TWOHAND) or (apply_number == EPointTypes.LG_POINT_RESIST_DAGGER) or (apply_number == EPointTypes.LG_POINT_RESIST_BELL) or (apply_number == EPointTypes.LG_POINT_RESIST_FAN) or (apply_number == EPointTypes.LG_POINT_RESIST_BOW) or (apply_number == EPointTypes.LG_POINT_RESIST_CLAW) or (apply_number == EPointTypes.LG_POINT_RESIST_FIRE) or (apply_number == EPointTypes.LG_POINT_RESIST_ELEC) or (apply_number == EPointTypes.LG_POINT_RESIST_MAGIC) or (apply_number == EPointTypes.LG_POINT_RESIST_WIND) or (apply_number == EPointTypes.LG_POINT_RESIST_ICE) or (apply_number == EPointTypes.LG_POINT_RESIST_EARTH) or (apply_number == EPointTypes.LG_POINT_RESIST_DARK):
            return LC_TEXT("��� ���� %d%%")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_CRITICAL) or (apply_number == EPointTypes.LG_POINT_PENETRATE_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_PENETRATE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_HUMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ANIMAL) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ORC) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MILGYO) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_UNDEAD) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_DEVIL) or (apply_number == EPointTypes.LG_POINT_STEAL_HP) or (apply_number == EPointTypes.LG_POINT_STEAL_SP) or (apply_number == EPointTypes.LG_POINT_MANA_BURN_PCT) or (apply_number == EPointTypes.LG_POINT_DAMAGE_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_BLOCK) or (apply_number == EPointTypes.LG_POINT_DODGE) or (apply_number == EPointTypes.LG_POINT_RESIST_SWORD) or (apply_number == EPointTypes.LG_POINT_RESIST_TWOHAND) or (apply_number == EPointTypes.LG_POINT_RESIST_DAGGER) or (apply_number == EPointTypes.LG_POINT_RESIST_BELL) or (apply_number == EPointTypes.LG_POINT_RESIST_FAN) or (apply_number == EPointTypes.LG_POINT_RESIST_BOW) or (apply_number == EPointTypes.LG_POINT_RESIST_CLAW) or (apply_number == EPointTypes.LG_POINT_RESIST_FIRE) or (apply_number == EPointTypes.LG_POINT_RESIST_ELEC) or (apply_number == EPointTypes.LG_POINT_RESIST_MAGIC) or (apply_number == EPointTypes.LG_POINT_RESIST_WIND) or (apply_number == EPointTypes.LG_POINT_RESIST_ICE) or (apply_number == EPointTypes.LG_POINT_RESIST_EARTH) or (apply_number == EPointTypes.LG_POINT_RESIST_DARK) or (apply_number == EPointTypes.LG_POINT_REFLECT_MELEE):
            return LC_TEXT("Reflect Direct Hit: %d%%")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_CRITICAL) or (apply_number == EPointTypes.LG_POINT_PENETRATE_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_PENETRATE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_HUMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ANIMAL) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ORC) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MILGYO) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_UNDEAD) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_DEVIL) or (apply_number == EPointTypes.LG_POINT_STEAL_HP) or (apply_number == EPointTypes.LG_POINT_STEAL_SP) or (apply_number == EPointTypes.LG_POINT_MANA_BURN_PCT) or (apply_number == EPointTypes.LG_POINT_DAMAGE_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_BLOCK) or (apply_number == EPointTypes.LG_POINT_DODGE) or (apply_number == EPointTypes.LG_POINT_RESIST_SWORD) or (apply_number == EPointTypes.LG_POINT_RESIST_TWOHAND) or (apply_number == EPointTypes.LG_POINT_RESIST_DAGGER) or (apply_number == EPointTypes.LG_POINT_RESIST_BELL) or (apply_number == EPointTypes.LG_POINT_RESIST_FAN) or (apply_number == EPointTypes.LG_POINT_RESIST_BOW) or (apply_number == EPointTypes.LG_POINT_RESIST_CLAW) or (apply_number == EPointTypes.LG_POINT_RESIST_FIRE) or (apply_number == EPointTypes.LG_POINT_RESIST_ELEC) or (apply_number == EPointTypes.LG_POINT_RESIST_MAGIC) or (apply_number == EPointTypes.LG_POINT_RESIST_WIND) or (apply_number == EPointTypes.LG_POINT_RESIST_ICE) or (apply_number == EPointTypes.LG_POINT_RESIST_EARTH) or (apply_number == EPointTypes.LG_POINT_RESIST_DARK) or (apply_number == EPointTypes.LG_POINT_REFLECT_MELEE) or (apply_number == EPointTypes.LG_POINT_REFLECT_CURSE):
            return LC_TEXT("Reflect Curse: %d%%")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_CRITICAL) or (apply_number == EPointTypes.LG_POINT_PENETRATE_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_PENETRATE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_HUMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ANIMAL) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ORC) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MILGYO) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_UNDEAD) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_DEVIL) or (apply_number == EPointTypes.LG_POINT_STEAL_HP) or (apply_number == EPointTypes.LG_POINT_STEAL_SP) or (apply_number == EPointTypes.LG_POINT_MANA_BURN_PCT) or (apply_number == EPointTypes.LG_POINT_DAMAGE_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_BLOCK) or (apply_number == EPointTypes.LG_POINT_DODGE) or (apply_number == EPointTypes.LG_POINT_RESIST_SWORD) or (apply_number == EPointTypes.LG_POINT_RESIST_TWOHAND) or (apply_number == EPointTypes.LG_POINT_RESIST_DAGGER) or (apply_number == EPointTypes.LG_POINT_RESIST_BELL) or (apply_number == EPointTypes.LG_POINT_RESIST_FAN) or (apply_number == EPointTypes.LG_POINT_RESIST_BOW) or (apply_number == EPointTypes.LG_POINT_RESIST_CLAW) or (apply_number == EPointTypes.LG_POINT_RESIST_FIRE) or (apply_number == EPointTypes.LG_POINT_RESIST_ELEC) or (apply_number == EPointTypes.LG_POINT_RESIST_MAGIC) or (apply_number == EPointTypes.LG_POINT_RESIST_WIND) or (apply_number == EPointTypes.LG_POINT_RESIST_ICE) or (apply_number == EPointTypes.LG_POINT_RESIST_EARTH) or (apply_number == EPointTypes.LG_POINT_RESIST_DARK) or (apply_number == EPointTypes.LG_POINT_REFLECT_MELEE) or (apply_number == EPointTypes.LG_POINT_REFLECT_CURSE) or (apply_number == EPointTypes.LG_POINT_POISON_REDUCE):
            return LC_TEXT("Poison Resistance %d%%")
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##if ENABLE_WOLFMAN
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_CRITICAL) or (apply_number == EPointTypes.LG_POINT_PENETRATE_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_PENETRATE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_HUMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ANIMAL) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ORC) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MILGYO) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_UNDEAD) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_DEVIL) or (apply_number == EPointTypes.LG_POINT_STEAL_HP) or (apply_number == EPointTypes.LG_POINT_STEAL_SP) or (apply_number == EPointTypes.LG_POINT_MANA_BURN_PCT) or (apply_number == EPointTypes.LG_POINT_DAMAGE_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_BLOCK) or (apply_number == EPointTypes.LG_POINT_DODGE) or (apply_number == EPointTypes.LG_POINT_RESIST_SWORD) or (apply_number == EPointTypes.LG_POINT_RESIST_TWOHAND) or (apply_number == EPointTypes.LG_POINT_RESIST_DAGGER) or (apply_number == EPointTypes.LG_POINT_RESIST_BELL) or (apply_number == EPointTypes.LG_POINT_RESIST_FAN) or (apply_number == EPointTypes.LG_POINT_RESIST_BOW) or (apply_number == EPointTypes.LG_POINT_RESIST_CLAW) or (apply_number == EPointTypes.LG_POINT_RESIST_FIRE) or (apply_number == EPointTypes.LG_POINT_RESIST_ELEC) or (apply_number == EPointTypes.LG_POINT_RESIST_MAGIC) or (apply_number == EPointTypes.LG_POINT_RESIST_WIND) or (apply_number == EPointTypes.LG_POINT_RESIST_ICE) or (apply_number == EPointTypes.LG_POINT_RESIST_EARTH) or (apply_number == EPointTypes.LG_POINT_RESIST_DARK) or (apply_number == EPointTypes.LG_POINT_REFLECT_MELEE) or (apply_number == EPointTypes.LG_POINT_REFLECT_CURSE) or (apply_number == EPointTypes.LG_POINT_POISON_REDUCE) or (apply_number == EPointTypes.LG_POINT_BLEEDING_REDUCE):
            return LC_TEXT("Poison Resistance %d%%")
    ##endif
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_CRITICAL) or (apply_number == EPointTypes.LG_POINT_PENETRATE_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_PENETRATE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_HUMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ANIMAL) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ORC) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MILGYO) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_UNDEAD) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_DEVIL) or (apply_number == EPointTypes.LG_POINT_STEAL_HP) or (apply_number == EPointTypes.LG_POINT_STEAL_SP) or (apply_number == EPointTypes.LG_POINT_MANA_BURN_PCT) or (apply_number == EPointTypes.LG_POINT_DAMAGE_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_BLOCK) or (apply_number == EPointTypes.LG_POINT_DODGE) or (apply_number == EPointTypes.LG_POINT_RESIST_SWORD) or (apply_number == EPointTypes.LG_POINT_RESIST_TWOHAND) or (apply_number == EPointTypes.LG_POINT_RESIST_DAGGER) or (apply_number == EPointTypes.LG_POINT_RESIST_BELL) or (apply_number == EPointTypes.LG_POINT_RESIST_FAN) or (apply_number == EPointTypes.LG_POINT_RESIST_BOW) or (apply_number == EPointTypes.LG_POINT_RESIST_CLAW) or (apply_number == EPointTypes.LG_POINT_RESIST_FIRE) or (apply_number == EPointTypes.LG_POINT_RESIST_ELEC) or (apply_number == EPointTypes.LG_POINT_RESIST_MAGIC) or (apply_number == EPointTypes.LG_POINT_RESIST_WIND) or (apply_number == EPointTypes.LG_POINT_RESIST_ICE) or (apply_number == EPointTypes.LG_POINT_RESIST_EARTH) or (apply_number == EPointTypes.LG_POINT_RESIST_DARK) or (apply_number == EPointTypes.LG_POINT_REFLECT_MELEE) or (apply_number == EPointTypes.LG_POINT_REFLECT_CURSE) or (apply_number == EPointTypes.LG_POINT_POISON_REDUCE) or (apply_number == EPointTypes.LG_POINT_BLEEDING_REDUCE) or (apply_number == EPointTypes.LG_POINT_KILL_SP_RECOVER):
            return LC_TEXT("Spell Points will be increased up to %d%% if you win.")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_CRITICAL) or (apply_number == EPointTypes.LG_POINT_PENETRATE_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_PENETRATE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_HUMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ANIMAL) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ORC) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MILGYO) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_UNDEAD) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_DEVIL) or (apply_number == EPointTypes.LG_POINT_STEAL_HP) or (apply_number == EPointTypes.LG_POINT_STEAL_SP) or (apply_number == EPointTypes.LG_POINT_MANA_BURN_PCT) or (apply_number == EPointTypes.LG_POINT_DAMAGE_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_BLOCK) or (apply_number == EPointTypes.LG_POINT_DODGE) or (apply_number == EPointTypes.LG_POINT_RESIST_SWORD) or (apply_number == EPointTypes.LG_POINT_RESIST_TWOHAND) or (apply_number == EPointTypes.LG_POINT_RESIST_DAGGER) or (apply_number == EPointTypes.LG_POINT_RESIST_BELL) or (apply_number == EPointTypes.LG_POINT_RESIST_FAN) or (apply_number == EPointTypes.LG_POINT_RESIST_BOW) or (apply_number == EPointTypes.LG_POINT_RESIST_CLAW) or (apply_number == EPointTypes.LG_POINT_RESIST_FIRE) or (apply_number == EPointTypes.LG_POINT_RESIST_ELEC) or (apply_number == EPointTypes.LG_POINT_RESIST_MAGIC) or (apply_number == EPointTypes.LG_POINT_RESIST_WIND) or (apply_number == EPointTypes.LG_POINT_RESIST_ICE) or (apply_number == EPointTypes.LG_POINT_RESIST_EARTH) or (apply_number == EPointTypes.LG_POINT_RESIST_DARK) or (apply_number == EPointTypes.LG_POINT_REFLECT_MELEE) or (apply_number == EPointTypes.LG_POINT_REFLECT_CURSE) or (apply_number == EPointTypes.LG_POINT_POISON_REDUCE) or (apply_number == EPointTypes.LG_POINT_BLEEDING_REDUCE) or (apply_number == EPointTypes.LG_POINT_KILL_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_EXP_DOUBLE_BONUS):
            return LC_TEXT("Experience increases up to %d%% if you win.")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_CRITICAL) or (apply_number == EPointTypes.LG_POINT_PENETRATE_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_PENETRATE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_HUMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ANIMAL) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ORC) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MILGYO) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_UNDEAD) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_DEVIL) or (apply_number == EPointTypes.LG_POINT_STEAL_HP) or (apply_number == EPointTypes.LG_POINT_STEAL_SP) or (apply_number == EPointTypes.LG_POINT_MANA_BURN_PCT) or (apply_number == EPointTypes.LG_POINT_DAMAGE_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_BLOCK) or (apply_number == EPointTypes.LG_POINT_DODGE) or (apply_number == EPointTypes.LG_POINT_RESIST_SWORD) or (apply_number == EPointTypes.LG_POINT_RESIST_TWOHAND) or (apply_number == EPointTypes.LG_POINT_RESIST_DAGGER) or (apply_number == EPointTypes.LG_POINT_RESIST_BELL) or (apply_number == EPointTypes.LG_POINT_RESIST_FAN) or (apply_number == EPointTypes.LG_POINT_RESIST_BOW) or (apply_number == EPointTypes.LG_POINT_RESIST_CLAW) or (apply_number == EPointTypes.LG_POINT_RESIST_FIRE) or (apply_number == EPointTypes.LG_POINT_RESIST_ELEC) or (apply_number == EPointTypes.LG_POINT_RESIST_MAGIC) or (apply_number == EPointTypes.LG_POINT_RESIST_WIND) or (apply_number == EPointTypes.LG_POINT_RESIST_ICE) or (apply_number == EPointTypes.LG_POINT_RESIST_EARTH) or (apply_number == EPointTypes.LG_POINT_RESIST_DARK) or (apply_number == EPointTypes.LG_POINT_REFLECT_MELEE) or (apply_number == EPointTypes.LG_POINT_REFLECT_CURSE) or (apply_number == EPointTypes.LG_POINT_POISON_REDUCE) or (apply_number == EPointTypes.LG_POINT_BLEEDING_REDUCE) or (apply_number == EPointTypes.LG_POINT_KILL_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_EXP_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_GOLD_DOUBLE_BONUS):
            return LC_TEXT("Increase of Yang up to %d%% if you win")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_CRITICAL) or (apply_number == EPointTypes.LG_POINT_PENETRATE_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_PENETRATE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_HUMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ANIMAL) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ORC) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MILGYO) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_UNDEAD) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_DEVIL) or (apply_number == EPointTypes.LG_POINT_STEAL_HP) or (apply_number == EPointTypes.LG_POINT_STEAL_SP) or (apply_number == EPointTypes.LG_POINT_MANA_BURN_PCT) or (apply_number == EPointTypes.LG_POINT_DAMAGE_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_BLOCK) or (apply_number == EPointTypes.LG_POINT_DODGE) or (apply_number == EPointTypes.LG_POINT_RESIST_SWORD) or (apply_number == EPointTypes.LG_POINT_RESIST_TWOHAND) or (apply_number == EPointTypes.LG_POINT_RESIST_DAGGER) or (apply_number == EPointTypes.LG_POINT_RESIST_BELL) or (apply_number == EPointTypes.LG_POINT_RESIST_FAN) or (apply_number == EPointTypes.LG_POINT_RESIST_BOW) or (apply_number == EPointTypes.LG_POINT_RESIST_CLAW) or (apply_number == EPointTypes.LG_POINT_RESIST_FIRE) or (apply_number == EPointTypes.LG_POINT_RESIST_ELEC) or (apply_number == EPointTypes.LG_POINT_RESIST_MAGIC) or (apply_number == EPointTypes.LG_POINT_RESIST_WIND) or (apply_number == EPointTypes.LG_POINT_RESIST_ICE) or (apply_number == EPointTypes.LG_POINT_RESIST_EARTH) or (apply_number == EPointTypes.LG_POINT_RESIST_DARK) or (apply_number == EPointTypes.LG_POINT_REFLECT_MELEE) or (apply_number == EPointTypes.LG_POINT_REFLECT_CURSE) or (apply_number == EPointTypes.LG_POINT_POISON_REDUCE) or (apply_number == EPointTypes.LG_POINT_BLEEDING_REDUCE) or (apply_number == EPointTypes.LG_POINT_KILL_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_EXP_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_GOLD_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_ITEM_DROP_BONUS):
            return LC_TEXT("Increase of captured Items up to %d%% if you win.")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_CRITICAL) or (apply_number == EPointTypes.LG_POINT_PENETRATE_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_PENETRATE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_HUMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ANIMAL) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ORC) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MILGYO) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_UNDEAD) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_DEVIL) or (apply_number == EPointTypes.LG_POINT_STEAL_HP) or (apply_number == EPointTypes.LG_POINT_STEAL_SP) or (apply_number == EPointTypes.LG_POINT_MANA_BURN_PCT) or (apply_number == EPointTypes.LG_POINT_DAMAGE_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_BLOCK) or (apply_number == EPointTypes.LG_POINT_DODGE) or (apply_number == EPointTypes.LG_POINT_RESIST_SWORD) or (apply_number == EPointTypes.LG_POINT_RESIST_TWOHAND) or (apply_number == EPointTypes.LG_POINT_RESIST_DAGGER) or (apply_number == EPointTypes.LG_POINT_RESIST_BELL) or (apply_number == EPointTypes.LG_POINT_RESIST_FAN) or (apply_number == EPointTypes.LG_POINT_RESIST_BOW) or (apply_number == EPointTypes.LG_POINT_RESIST_CLAW) or (apply_number == EPointTypes.LG_POINT_RESIST_FIRE) or (apply_number == EPointTypes.LG_POINT_RESIST_ELEC) or (apply_number == EPointTypes.LG_POINT_RESIST_MAGIC) or (apply_number == EPointTypes.LG_POINT_RESIST_WIND) or (apply_number == EPointTypes.LG_POINT_RESIST_ICE) or (apply_number == EPointTypes.LG_POINT_RESIST_EARTH) or (apply_number == EPointTypes.LG_POINT_RESIST_DARK) or (apply_number == EPointTypes.LG_POINT_REFLECT_MELEE) or (apply_number == EPointTypes.LG_POINT_REFLECT_CURSE) or (apply_number == EPointTypes.LG_POINT_POISON_REDUCE) or (apply_number == EPointTypes.LG_POINT_BLEEDING_REDUCE) or (apply_number == EPointTypes.LG_POINT_KILL_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_EXP_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_GOLD_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_ITEM_DROP_BONUS) or (apply_number == EPointTypes.LG_POINT_POTION_BONUS):
            return LC_TEXT("Increase of Power up to %d%% when taking the Potion.")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_CRITICAL) or (apply_number == EPointTypes.LG_POINT_PENETRATE_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_PENETRATE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_HUMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ANIMAL) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ORC) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MILGYO) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_UNDEAD) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_DEVIL) or (apply_number == EPointTypes.LG_POINT_STEAL_HP) or (apply_number == EPointTypes.LG_POINT_STEAL_SP) or (apply_number == EPointTypes.LG_POINT_MANA_BURN_PCT) or (apply_number == EPointTypes.LG_POINT_DAMAGE_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_BLOCK) or (apply_number == EPointTypes.LG_POINT_DODGE) or (apply_number == EPointTypes.LG_POINT_RESIST_SWORD) or (apply_number == EPointTypes.LG_POINT_RESIST_TWOHAND) or (apply_number == EPointTypes.LG_POINT_RESIST_DAGGER) or (apply_number == EPointTypes.LG_POINT_RESIST_BELL) or (apply_number == EPointTypes.LG_POINT_RESIST_FAN) or (apply_number == EPointTypes.LG_POINT_RESIST_BOW) or (apply_number == EPointTypes.LG_POINT_RESIST_CLAW) or (apply_number == EPointTypes.LG_POINT_RESIST_FIRE) or (apply_number == EPointTypes.LG_POINT_RESIST_ELEC) or (apply_number == EPointTypes.LG_POINT_RESIST_MAGIC) or (apply_number == EPointTypes.LG_POINT_RESIST_WIND) or (apply_number == EPointTypes.LG_POINT_RESIST_ICE) or (apply_number == EPointTypes.LG_POINT_RESIST_EARTH) or (apply_number == EPointTypes.LG_POINT_RESIST_DARK) or (apply_number == EPointTypes.LG_POINT_REFLECT_MELEE) or (apply_number == EPointTypes.LG_POINT_REFLECT_CURSE) or (apply_number == EPointTypes.LG_POINT_POISON_REDUCE) or (apply_number == EPointTypes.LG_POINT_BLEEDING_REDUCE) or (apply_number == EPointTypes.LG_POINT_KILL_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_EXP_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_GOLD_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_ITEM_DROP_BONUS) or (apply_number == EPointTypes.LG_POINT_POTION_BONUS) or (apply_number == EPointTypes.LG_POINT_KILL_HP_RECOVERY):
            return LC_TEXT("%d%% Chance to fill up Energy Points after you won.")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_CRITICAL) or (apply_number == EPointTypes.LG_POINT_PENETRATE_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_PENETRATE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_HUMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ANIMAL) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ORC) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MILGYO) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_UNDEAD) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_DEVIL) or (apply_number == EPointTypes.LG_POINT_STEAL_HP) or (apply_number == EPointTypes.LG_POINT_STEAL_SP) or (apply_number == EPointTypes.LG_POINT_MANA_BURN_PCT) or (apply_number == EPointTypes.LG_POINT_DAMAGE_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_BLOCK) or (apply_number == EPointTypes.LG_POINT_DODGE) or (apply_number == EPointTypes.LG_POINT_RESIST_SWORD) or (apply_number == EPointTypes.LG_POINT_RESIST_TWOHAND) or (apply_number == EPointTypes.LG_POINT_RESIST_DAGGER) or (apply_number == EPointTypes.LG_POINT_RESIST_BELL) or (apply_number == EPointTypes.LG_POINT_RESIST_FAN) or (apply_number == EPointTypes.LG_POINT_RESIST_BOW) or (apply_number == EPointTypes.LG_POINT_RESIST_CLAW) or (apply_number == EPointTypes.LG_POINT_RESIST_FIRE) or (apply_number == EPointTypes.LG_POINT_RESIST_ELEC) or (apply_number == EPointTypes.LG_POINT_RESIST_MAGIC) or (apply_number == EPointTypes.LG_POINT_RESIST_WIND) or (apply_number == EPointTypes.LG_POINT_RESIST_ICE) or (apply_number == EPointTypes.LG_POINT_RESIST_EARTH) or (apply_number == EPointTypes.LG_POINT_RESIST_DARK) or (apply_number == EPointTypes.LG_POINT_REFLECT_MELEE) or (apply_number == EPointTypes.LG_POINT_REFLECT_CURSE) or (apply_number == EPointTypes.LG_POINT_POISON_REDUCE) or (apply_number == EPointTypes.LG_POINT_BLEEDING_REDUCE) or (apply_number == EPointTypes.LG_POINT_KILL_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_EXP_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_GOLD_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_ITEM_DROP_BONUS) or (apply_number == EPointTypes.LG_POINT_POTION_BONUS) or (apply_number == EPointTypes.LG_POINT_KILL_HP_RECOVERY) or (apply_number == EPointTypes.LG_POINT_ATT_GRADE_BONUS):
            return LC_TEXT("Attack Power + %d")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_CRITICAL) or (apply_number == EPointTypes.LG_POINT_PENETRATE_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_PENETRATE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_HUMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ANIMAL) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ORC) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MILGYO) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_UNDEAD) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_DEVIL) or (apply_number == EPointTypes.LG_POINT_STEAL_HP) or (apply_number == EPointTypes.LG_POINT_STEAL_SP) or (apply_number == EPointTypes.LG_POINT_MANA_BURN_PCT) or (apply_number == EPointTypes.LG_POINT_DAMAGE_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_BLOCK) or (apply_number == EPointTypes.LG_POINT_DODGE) or (apply_number == EPointTypes.LG_POINT_RESIST_SWORD) or (apply_number == EPointTypes.LG_POINT_RESIST_TWOHAND) or (apply_number == EPointTypes.LG_POINT_RESIST_DAGGER) or (apply_number == EPointTypes.LG_POINT_RESIST_BELL) or (apply_number == EPointTypes.LG_POINT_RESIST_FAN) or (apply_number == EPointTypes.LG_POINT_RESIST_BOW) or (apply_number == EPointTypes.LG_POINT_RESIST_CLAW) or (apply_number == EPointTypes.LG_POINT_RESIST_FIRE) or (apply_number == EPointTypes.LG_POINT_RESIST_ELEC) or (apply_number == EPointTypes.LG_POINT_RESIST_MAGIC) or (apply_number == EPointTypes.LG_POINT_RESIST_WIND) or (apply_number == EPointTypes.LG_POINT_RESIST_ICE) or (apply_number == EPointTypes.LG_POINT_RESIST_EARTH) or (apply_number == EPointTypes.LG_POINT_RESIST_DARK) or (apply_number == EPointTypes.LG_POINT_REFLECT_MELEE) or (apply_number == EPointTypes.LG_POINT_REFLECT_CURSE) or (apply_number == EPointTypes.LG_POINT_POISON_REDUCE) or (apply_number == EPointTypes.LG_POINT_BLEEDING_REDUCE) or (apply_number == EPointTypes.LG_POINT_KILL_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_EXP_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_GOLD_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_ITEM_DROP_BONUS) or (apply_number == EPointTypes.LG_POINT_POTION_BONUS) or (apply_number == EPointTypes.LG_POINT_KILL_HP_RECOVERY) or (apply_number == EPointTypes.LG_POINT_ATT_GRADE_BONUS) or (apply_number == EPointTypes.LG_POINT_DEF_GRADE_BONUS):
            return LC_TEXT("Armour + %d")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_CRITICAL) or (apply_number == EPointTypes.LG_POINT_PENETRATE_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_PENETRATE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_HUMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ANIMAL) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ORC) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MILGYO) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_UNDEAD) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_DEVIL) or (apply_number == EPointTypes.LG_POINT_STEAL_HP) or (apply_number == EPointTypes.LG_POINT_STEAL_SP) or (apply_number == EPointTypes.LG_POINT_MANA_BURN_PCT) or (apply_number == EPointTypes.LG_POINT_DAMAGE_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_BLOCK) or (apply_number == EPointTypes.LG_POINT_DODGE) or (apply_number == EPointTypes.LG_POINT_RESIST_SWORD) or (apply_number == EPointTypes.LG_POINT_RESIST_TWOHAND) or (apply_number == EPointTypes.LG_POINT_RESIST_DAGGER) or (apply_number == EPointTypes.LG_POINT_RESIST_BELL) or (apply_number == EPointTypes.LG_POINT_RESIST_FAN) or (apply_number == EPointTypes.LG_POINT_RESIST_BOW) or (apply_number == EPointTypes.LG_POINT_RESIST_CLAW) or (apply_number == EPointTypes.LG_POINT_RESIST_FIRE) or (apply_number == EPointTypes.LG_POINT_RESIST_ELEC) or (apply_number == EPointTypes.LG_POINT_RESIST_MAGIC) or (apply_number == EPointTypes.LG_POINT_RESIST_WIND) or (apply_number == EPointTypes.LG_POINT_RESIST_ICE) or (apply_number == EPointTypes.LG_POINT_RESIST_EARTH) or (apply_number == EPointTypes.LG_POINT_RESIST_DARK) or (apply_number == EPointTypes.LG_POINT_REFLECT_MELEE) or (apply_number == EPointTypes.LG_POINT_REFLECT_CURSE) or (apply_number == EPointTypes.LG_POINT_POISON_REDUCE) or (apply_number == EPointTypes.LG_POINT_BLEEDING_REDUCE) or (apply_number == EPointTypes.LG_POINT_KILL_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_EXP_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_GOLD_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_ITEM_DROP_BONUS) or (apply_number == EPointTypes.LG_POINT_POTION_BONUS) or (apply_number == EPointTypes.LG_POINT_KILL_HP_RECOVERY) or (apply_number == EPointTypes.LG_POINT_ATT_GRADE_BONUS) or (apply_number == EPointTypes.LG_POINT_DEF_GRADE_BONUS) or (apply_number == EPointTypes.LG_POINT_MAGIC_ATT_GRADE):
            return LC_TEXT("Magical Attack + %d")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_CRITICAL) or (apply_number == EPointTypes.LG_POINT_PENETRATE_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_PENETRATE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_HUMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ANIMAL) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ORC) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MILGYO) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_UNDEAD) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_DEVIL) or (apply_number == EPointTypes.LG_POINT_STEAL_HP) or (apply_number == EPointTypes.LG_POINT_STEAL_SP) or (apply_number == EPointTypes.LG_POINT_MANA_BURN_PCT) or (apply_number == EPointTypes.LG_POINT_DAMAGE_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_BLOCK) or (apply_number == EPointTypes.LG_POINT_DODGE) or (apply_number == EPointTypes.LG_POINT_RESIST_SWORD) or (apply_number == EPointTypes.LG_POINT_RESIST_TWOHAND) or (apply_number == EPointTypes.LG_POINT_RESIST_DAGGER) or (apply_number == EPointTypes.LG_POINT_RESIST_BELL) or (apply_number == EPointTypes.LG_POINT_RESIST_FAN) or (apply_number == EPointTypes.LG_POINT_RESIST_BOW) or (apply_number == EPointTypes.LG_POINT_RESIST_CLAW) or (apply_number == EPointTypes.LG_POINT_RESIST_FIRE) or (apply_number == EPointTypes.LG_POINT_RESIST_ELEC) or (apply_number == EPointTypes.LG_POINT_RESIST_MAGIC) or (apply_number == EPointTypes.LG_POINT_RESIST_WIND) or (apply_number == EPointTypes.LG_POINT_RESIST_ICE) or (apply_number == EPointTypes.LG_POINT_RESIST_EARTH) or (apply_number == EPointTypes.LG_POINT_RESIST_DARK) or (apply_number == EPointTypes.LG_POINT_REFLECT_MELEE) or (apply_number == EPointTypes.LG_POINT_REFLECT_CURSE) or (apply_number == EPointTypes.LG_POINT_POISON_REDUCE) or (apply_number == EPointTypes.LG_POINT_BLEEDING_REDUCE) or (apply_number == EPointTypes.LG_POINT_KILL_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_EXP_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_GOLD_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_ITEM_DROP_BONUS) or (apply_number == EPointTypes.LG_POINT_POTION_BONUS) or (apply_number == EPointTypes.LG_POINT_KILL_HP_RECOVERY) or (apply_number == EPointTypes.LG_POINT_ATT_GRADE_BONUS) or (apply_number == EPointTypes.LG_POINT_DEF_GRADE_BONUS) or (apply_number == EPointTypes.LG_POINT_MAGIC_ATT_GRADE) or (apply_number == EPointTypes.LG_POINT_MAGIC_DEF_GRADE):
            return LC_TEXT("Magical Defence + %d")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_CRITICAL) or (apply_number == EPointTypes.LG_POINT_PENETRATE_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_PENETRATE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_HUMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ANIMAL) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ORC) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MILGYO) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_UNDEAD) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_DEVIL) or (apply_number == EPointTypes.LG_POINT_STEAL_HP) or (apply_number == EPointTypes.LG_POINT_STEAL_SP) or (apply_number == EPointTypes.LG_POINT_MANA_BURN_PCT) or (apply_number == EPointTypes.LG_POINT_DAMAGE_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_BLOCK) or (apply_number == EPointTypes.LG_POINT_DODGE) or (apply_number == EPointTypes.LG_POINT_RESIST_SWORD) or (apply_number == EPointTypes.LG_POINT_RESIST_TWOHAND) or (apply_number == EPointTypes.LG_POINT_RESIST_DAGGER) or (apply_number == EPointTypes.LG_POINT_RESIST_BELL) or (apply_number == EPointTypes.LG_POINT_RESIST_FAN) or (apply_number == EPointTypes.LG_POINT_RESIST_BOW) or (apply_number == EPointTypes.LG_POINT_RESIST_CLAW) or (apply_number == EPointTypes.LG_POINT_RESIST_FIRE) or (apply_number == EPointTypes.LG_POINT_RESIST_ELEC) or (apply_number == EPointTypes.LG_POINT_RESIST_MAGIC) or (apply_number == EPointTypes.LG_POINT_RESIST_WIND) or (apply_number == EPointTypes.LG_POINT_RESIST_ICE) or (apply_number == EPointTypes.LG_POINT_RESIST_EARTH) or (apply_number == EPointTypes.LG_POINT_RESIST_DARK) or (apply_number == EPointTypes.LG_POINT_REFLECT_MELEE) or (apply_number == EPointTypes.LG_POINT_REFLECT_CURSE) or (apply_number == EPointTypes.LG_POINT_POISON_REDUCE) or (apply_number == EPointTypes.LG_POINT_BLEEDING_REDUCE) or (apply_number == EPointTypes.LG_POINT_KILL_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_EXP_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_GOLD_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_ITEM_DROP_BONUS) or (apply_number == EPointTypes.LG_POINT_POTION_BONUS) or (apply_number == EPointTypes.LG_POINT_KILL_HP_RECOVERY) or (apply_number == EPointTypes.LG_POINT_ATT_GRADE_BONUS) or (apply_number == EPointTypes.LG_POINT_DEF_GRADE_BONUS) or (apply_number == EPointTypes.LG_POINT_MAGIC_ATT_GRADE) or (apply_number == EPointTypes.LG_POINT_MAGIC_DEF_GRADE) or (apply_number == EPointTypes.LG_POINT_MAX_STAMINA):
            return LC_TEXT("Maximum Endurance + %d")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_CRITICAL) or (apply_number == EPointTypes.LG_POINT_PENETRATE_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_PENETRATE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_HUMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ANIMAL) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ORC) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MILGYO) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_UNDEAD) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_DEVIL) or (apply_number == EPointTypes.LG_POINT_STEAL_HP) or (apply_number == EPointTypes.LG_POINT_STEAL_SP) or (apply_number == EPointTypes.LG_POINT_MANA_BURN_PCT) or (apply_number == EPointTypes.LG_POINT_DAMAGE_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_BLOCK) or (apply_number == EPointTypes.LG_POINT_DODGE) or (apply_number == EPointTypes.LG_POINT_RESIST_SWORD) or (apply_number == EPointTypes.LG_POINT_RESIST_TWOHAND) or (apply_number == EPointTypes.LG_POINT_RESIST_DAGGER) or (apply_number == EPointTypes.LG_POINT_RESIST_BELL) or (apply_number == EPointTypes.LG_POINT_RESIST_FAN) or (apply_number == EPointTypes.LG_POINT_RESIST_BOW) or (apply_number == EPointTypes.LG_POINT_RESIST_CLAW) or (apply_number == EPointTypes.LG_POINT_RESIST_FIRE) or (apply_number == EPointTypes.LG_POINT_RESIST_ELEC) or (apply_number == EPointTypes.LG_POINT_RESIST_MAGIC) or (apply_number == EPointTypes.LG_POINT_RESIST_WIND) or (apply_number == EPointTypes.LG_POINT_RESIST_ICE) or (apply_number == EPointTypes.LG_POINT_RESIST_EARTH) or (apply_number == EPointTypes.LG_POINT_RESIST_DARK) or (apply_number == EPointTypes.LG_POINT_REFLECT_MELEE) or (apply_number == EPointTypes.LG_POINT_REFLECT_CURSE) or (apply_number == EPointTypes.LG_POINT_POISON_REDUCE) or (apply_number == EPointTypes.LG_POINT_BLEEDING_REDUCE) or (apply_number == EPointTypes.LG_POINT_KILL_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_EXP_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_GOLD_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_ITEM_DROP_BONUS) or (apply_number == EPointTypes.LG_POINT_POTION_BONUS) or (apply_number == EPointTypes.LG_POINT_KILL_HP_RECOVERY) or (apply_number == EPointTypes.LG_POINT_ATT_GRADE_BONUS) or (apply_number == EPointTypes.LG_POINT_DEF_GRADE_BONUS) or (apply_number == EPointTypes.LG_POINT_MAGIC_ATT_GRADE) or (apply_number == EPointTypes.LG_POINT_MAGIC_DEF_GRADE) or (apply_number == EPointTypes.LG_POINT_MAX_STAMINA) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_WARRIOR):
            return LC_TEXT("Strong against LG_PAWN_WARRIORs + %d%%")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_CRITICAL) or (apply_number == EPointTypes.LG_POINT_PENETRATE_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_PENETRATE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_HUMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ANIMAL) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ORC) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MILGYO) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_UNDEAD) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_DEVIL) or (apply_number == EPointTypes.LG_POINT_STEAL_HP) or (apply_number == EPointTypes.LG_POINT_STEAL_SP) or (apply_number == EPointTypes.LG_POINT_MANA_BURN_PCT) or (apply_number == EPointTypes.LG_POINT_DAMAGE_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_BLOCK) or (apply_number == EPointTypes.LG_POINT_DODGE) or (apply_number == EPointTypes.LG_POINT_RESIST_SWORD) or (apply_number == EPointTypes.LG_POINT_RESIST_TWOHAND) or (apply_number == EPointTypes.LG_POINT_RESIST_DAGGER) or (apply_number == EPointTypes.LG_POINT_RESIST_BELL) or (apply_number == EPointTypes.LG_POINT_RESIST_FAN) or (apply_number == EPointTypes.LG_POINT_RESIST_BOW) or (apply_number == EPointTypes.LG_POINT_RESIST_CLAW) or (apply_number == EPointTypes.LG_POINT_RESIST_FIRE) or (apply_number == EPointTypes.LG_POINT_RESIST_ELEC) or (apply_number == EPointTypes.LG_POINT_RESIST_MAGIC) or (apply_number == EPointTypes.LG_POINT_RESIST_WIND) or (apply_number == EPointTypes.LG_POINT_RESIST_ICE) or (apply_number == EPointTypes.LG_POINT_RESIST_EARTH) or (apply_number == EPointTypes.LG_POINT_RESIST_DARK) or (apply_number == EPointTypes.LG_POINT_REFLECT_MELEE) or (apply_number == EPointTypes.LG_POINT_REFLECT_CURSE) or (apply_number == EPointTypes.LG_POINT_POISON_REDUCE) or (apply_number == EPointTypes.LG_POINT_BLEEDING_REDUCE) or (apply_number == EPointTypes.LG_POINT_KILL_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_EXP_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_GOLD_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_ITEM_DROP_BONUS) or (apply_number == EPointTypes.LG_POINT_POTION_BONUS) or (apply_number == EPointTypes.LG_POINT_KILL_HP_RECOVERY) or (apply_number == EPointTypes.LG_POINT_ATT_GRADE_BONUS) or (apply_number == EPointTypes.LG_POINT_DEF_GRADE_BONUS) or (apply_number == EPointTypes.LG_POINT_MAGIC_ATT_GRADE) or (apply_number == EPointTypes.LG_POINT_MAGIC_DEF_GRADE) or (apply_number == EPointTypes.LG_POINT_MAX_STAMINA) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_WARRIOR) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_ASSASSIN):
            return LC_TEXT("Strong against Ninja + %d%%")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_CRITICAL) or (apply_number == EPointTypes.LG_POINT_PENETRATE_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_PENETRATE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_HUMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ANIMAL) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ORC) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MILGYO) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_UNDEAD) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_DEVIL) or (apply_number == EPointTypes.LG_POINT_STEAL_HP) or (apply_number == EPointTypes.LG_POINT_STEAL_SP) or (apply_number == EPointTypes.LG_POINT_MANA_BURN_PCT) or (apply_number == EPointTypes.LG_POINT_DAMAGE_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_BLOCK) or (apply_number == EPointTypes.LG_POINT_DODGE) or (apply_number == EPointTypes.LG_POINT_RESIST_SWORD) or (apply_number == EPointTypes.LG_POINT_RESIST_TWOHAND) or (apply_number == EPointTypes.LG_POINT_RESIST_DAGGER) or (apply_number == EPointTypes.LG_POINT_RESIST_BELL) or (apply_number == EPointTypes.LG_POINT_RESIST_FAN) or (apply_number == EPointTypes.LG_POINT_RESIST_BOW) or (apply_number == EPointTypes.LG_POINT_RESIST_CLAW) or (apply_number == EPointTypes.LG_POINT_RESIST_FIRE) or (apply_number == EPointTypes.LG_POINT_RESIST_ELEC) or (apply_number == EPointTypes.LG_POINT_RESIST_MAGIC) or (apply_number == EPointTypes.LG_POINT_RESIST_WIND) or (apply_number == EPointTypes.LG_POINT_RESIST_ICE) or (apply_number == EPointTypes.LG_POINT_RESIST_EARTH) or (apply_number == EPointTypes.LG_POINT_RESIST_DARK) or (apply_number == EPointTypes.LG_POINT_REFLECT_MELEE) or (apply_number == EPointTypes.LG_POINT_REFLECT_CURSE) or (apply_number == EPointTypes.LG_POINT_POISON_REDUCE) or (apply_number == EPointTypes.LG_POINT_BLEEDING_REDUCE) or (apply_number == EPointTypes.LG_POINT_KILL_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_EXP_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_GOLD_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_ITEM_DROP_BONUS) or (apply_number == EPointTypes.LG_POINT_POTION_BONUS) or (apply_number == EPointTypes.LG_POINT_KILL_HP_RECOVERY) or (apply_number == EPointTypes.LG_POINT_ATT_GRADE_BONUS) or (apply_number == EPointTypes.LG_POINT_DEF_GRADE_BONUS) or (apply_number == EPointTypes.LG_POINT_MAGIC_ATT_GRADE) or (apply_number == EPointTypes.LG_POINT_MAGIC_DEF_GRADE) or (apply_number == EPointTypes.LG_POINT_MAX_STAMINA) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_WARRIOR) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_ASSASSIN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_SHURA):
            return LC_TEXT("Strong against LG_PAWN_SHURA + %d%%")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_CRITICAL) or (apply_number == EPointTypes.LG_POINT_PENETRATE_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_PENETRATE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_HUMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ANIMAL) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ORC) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MILGYO) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_UNDEAD) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_DEVIL) or (apply_number == EPointTypes.LG_POINT_STEAL_HP) or (apply_number == EPointTypes.LG_POINT_STEAL_SP) or (apply_number == EPointTypes.LG_POINT_MANA_BURN_PCT) or (apply_number == EPointTypes.LG_POINT_DAMAGE_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_BLOCK) or (apply_number == EPointTypes.LG_POINT_DODGE) or (apply_number == EPointTypes.LG_POINT_RESIST_SWORD) or (apply_number == EPointTypes.LG_POINT_RESIST_TWOHAND) or (apply_number == EPointTypes.LG_POINT_RESIST_DAGGER) or (apply_number == EPointTypes.LG_POINT_RESIST_BELL) or (apply_number == EPointTypes.LG_POINT_RESIST_FAN) or (apply_number == EPointTypes.LG_POINT_RESIST_BOW) or (apply_number == EPointTypes.LG_POINT_RESIST_CLAW) or (apply_number == EPointTypes.LG_POINT_RESIST_FIRE) or (apply_number == EPointTypes.LG_POINT_RESIST_ELEC) or (apply_number == EPointTypes.LG_POINT_RESIST_MAGIC) or (apply_number == EPointTypes.LG_POINT_RESIST_WIND) or (apply_number == EPointTypes.LG_POINT_RESIST_ICE) or (apply_number == EPointTypes.LG_POINT_RESIST_EARTH) or (apply_number == EPointTypes.LG_POINT_RESIST_DARK) or (apply_number == EPointTypes.LG_POINT_REFLECT_MELEE) or (apply_number == EPointTypes.LG_POINT_REFLECT_CURSE) or (apply_number == EPointTypes.LG_POINT_POISON_REDUCE) or (apply_number == EPointTypes.LG_POINT_BLEEDING_REDUCE) or (apply_number == EPointTypes.LG_POINT_KILL_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_EXP_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_GOLD_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_ITEM_DROP_BONUS) or (apply_number == EPointTypes.LG_POINT_POTION_BONUS) or (apply_number == EPointTypes.LG_POINT_KILL_HP_RECOVERY) or (apply_number == EPointTypes.LG_POINT_ATT_GRADE_BONUS) or (apply_number == EPointTypes.LG_POINT_DEF_GRADE_BONUS) or (apply_number == EPointTypes.LG_POINT_MAGIC_ATT_GRADE) or (apply_number == EPointTypes.LG_POINT_MAGIC_DEF_GRADE) or (apply_number == EPointTypes.LG_POINT_MAX_STAMINA) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_WARRIOR) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_ASSASSIN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_SHURA) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_MAGE):
            return LC_TEXT("Strong against Mages + %d%%")
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##if ENABLE_WOLFMAN
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_CRITICAL) or (apply_number == EPointTypes.LG_POINT_PENETRATE_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_PENETRATE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_HUMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ANIMAL) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ORC) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MILGYO) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_UNDEAD) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_DEVIL) or (apply_number == EPointTypes.LG_POINT_STEAL_HP) or (apply_number == EPointTypes.LG_POINT_STEAL_SP) or (apply_number == EPointTypes.LG_POINT_MANA_BURN_PCT) or (apply_number == EPointTypes.LG_POINT_DAMAGE_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_BLOCK) or (apply_number == EPointTypes.LG_POINT_DODGE) or (apply_number == EPointTypes.LG_POINT_RESIST_SWORD) or (apply_number == EPointTypes.LG_POINT_RESIST_TWOHAND) or (apply_number == EPointTypes.LG_POINT_RESIST_DAGGER) or (apply_number == EPointTypes.LG_POINT_RESIST_BELL) or (apply_number == EPointTypes.LG_POINT_RESIST_FAN) or (apply_number == EPointTypes.LG_POINT_RESIST_BOW) or (apply_number == EPointTypes.LG_POINT_RESIST_CLAW) or (apply_number == EPointTypes.LG_POINT_RESIST_FIRE) or (apply_number == EPointTypes.LG_POINT_RESIST_ELEC) or (apply_number == EPointTypes.LG_POINT_RESIST_MAGIC) or (apply_number == EPointTypes.LG_POINT_RESIST_WIND) or (apply_number == EPointTypes.LG_POINT_RESIST_ICE) or (apply_number == EPointTypes.LG_POINT_RESIST_EARTH) or (apply_number == EPointTypes.LG_POINT_RESIST_DARK) or (apply_number == EPointTypes.LG_POINT_REFLECT_MELEE) or (apply_number == EPointTypes.LG_POINT_REFLECT_CURSE) or (apply_number == EPointTypes.LG_POINT_POISON_REDUCE) or (apply_number == EPointTypes.LG_POINT_BLEEDING_REDUCE) or (apply_number == EPointTypes.LG_POINT_KILL_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_EXP_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_GOLD_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_ITEM_DROP_BONUS) or (apply_number == EPointTypes.LG_POINT_POTION_BONUS) or (apply_number == EPointTypes.LG_POINT_KILL_HP_RECOVERY) or (apply_number == EPointTypes.LG_POINT_ATT_GRADE_BONUS) or (apply_number == EPointTypes.LG_POINT_DEF_GRADE_BONUS) or (apply_number == EPointTypes.LG_POINT_MAGIC_ATT_GRADE) or (apply_number == EPointTypes.LG_POINT_MAGIC_DEF_GRADE) or (apply_number == EPointTypes.LG_POINT_MAX_STAMINA) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_WARRIOR) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_ASSASSIN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_SHURA) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_MAGE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_WOLFMAN):
            return LC_TEXT("Strong against Mages + %d%%")
    ##endif
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_CRITICAL) or (apply_number == EPointTypes.LG_POINT_PENETRATE_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_PENETRATE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_HUMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ANIMAL) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ORC) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MILGYO) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_UNDEAD) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_DEVIL) or (apply_number == EPointTypes.LG_POINT_STEAL_HP) or (apply_number == EPointTypes.LG_POINT_STEAL_SP) or (apply_number == EPointTypes.LG_POINT_MANA_BURN_PCT) or (apply_number == EPointTypes.LG_POINT_DAMAGE_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_BLOCK) or (apply_number == EPointTypes.LG_POINT_DODGE) or (apply_number == EPointTypes.LG_POINT_RESIST_SWORD) or (apply_number == EPointTypes.LG_POINT_RESIST_TWOHAND) or (apply_number == EPointTypes.LG_POINT_RESIST_DAGGER) or (apply_number == EPointTypes.LG_POINT_RESIST_BELL) or (apply_number == EPointTypes.LG_POINT_RESIST_FAN) or (apply_number == EPointTypes.LG_POINT_RESIST_BOW) or (apply_number == EPointTypes.LG_POINT_RESIST_CLAW) or (apply_number == EPointTypes.LG_POINT_RESIST_FIRE) or (apply_number == EPointTypes.LG_POINT_RESIST_ELEC) or (apply_number == EPointTypes.LG_POINT_RESIST_MAGIC) or (apply_number == EPointTypes.LG_POINT_RESIST_WIND) or (apply_number == EPointTypes.LG_POINT_RESIST_ICE) or (apply_number == EPointTypes.LG_POINT_RESIST_EARTH) or (apply_number == EPointTypes.LG_POINT_RESIST_DARK) or (apply_number == EPointTypes.LG_POINT_REFLECT_MELEE) or (apply_number == EPointTypes.LG_POINT_REFLECT_CURSE) or (apply_number == EPointTypes.LG_POINT_POISON_REDUCE) or (apply_number == EPointTypes.LG_POINT_BLEEDING_REDUCE) or (apply_number == EPointTypes.LG_POINT_KILL_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_EXP_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_GOLD_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_ITEM_DROP_BONUS) or (apply_number == EPointTypes.LG_POINT_POTION_BONUS) or (apply_number == EPointTypes.LG_POINT_KILL_HP_RECOVERY) or (apply_number == EPointTypes.LG_POINT_ATT_GRADE_BONUS) or (apply_number == EPointTypes.LG_POINT_DEF_GRADE_BONUS) or (apply_number == EPointTypes.LG_POINT_MAGIC_ATT_GRADE) or (apply_number == EPointTypes.LG_POINT_MAGIC_DEF_GRADE) or (apply_number == EPointTypes.LG_POINT_MAX_STAMINA) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_WARRIOR) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_ASSASSIN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_SHURA) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_MAGE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_WOLFMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MONSTER):
            return LC_TEXT("Strong against Monster + %d%%")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_CRITICAL) or (apply_number == EPointTypes.LG_POINT_PENETRATE_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_PENETRATE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_HUMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ANIMAL) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ORC) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MILGYO) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_UNDEAD) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_DEVIL) or (apply_number == EPointTypes.LG_POINT_STEAL_HP) or (apply_number == EPointTypes.LG_POINT_STEAL_SP) or (apply_number == EPointTypes.LG_POINT_MANA_BURN_PCT) or (apply_number == EPointTypes.LG_POINT_DAMAGE_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_BLOCK) or (apply_number == EPointTypes.LG_POINT_DODGE) or (apply_number == EPointTypes.LG_POINT_RESIST_SWORD) or (apply_number == EPointTypes.LG_POINT_RESIST_TWOHAND) or (apply_number == EPointTypes.LG_POINT_RESIST_DAGGER) or (apply_number == EPointTypes.LG_POINT_RESIST_BELL) or (apply_number == EPointTypes.LG_POINT_RESIST_FAN) or (apply_number == EPointTypes.LG_POINT_RESIST_BOW) or (apply_number == EPointTypes.LG_POINT_RESIST_CLAW) or (apply_number == EPointTypes.LG_POINT_RESIST_FIRE) or (apply_number == EPointTypes.LG_POINT_RESIST_ELEC) or (apply_number == EPointTypes.LG_POINT_RESIST_MAGIC) or (apply_number == EPointTypes.LG_POINT_RESIST_WIND) or (apply_number == EPointTypes.LG_POINT_RESIST_ICE) or (apply_number == EPointTypes.LG_POINT_RESIST_EARTH) or (apply_number == EPointTypes.LG_POINT_RESIST_DARK) or (apply_number == EPointTypes.LG_POINT_REFLECT_MELEE) or (apply_number == EPointTypes.LG_POINT_REFLECT_CURSE) or (apply_number == EPointTypes.LG_POINT_POISON_REDUCE) or (apply_number == EPointTypes.LG_POINT_BLEEDING_REDUCE) or (apply_number == EPointTypes.LG_POINT_KILL_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_EXP_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_GOLD_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_ITEM_DROP_BONUS) or (apply_number == EPointTypes.LG_POINT_POTION_BONUS) or (apply_number == EPointTypes.LG_POINT_KILL_HP_RECOVERY) or (apply_number == EPointTypes.LG_POINT_ATT_GRADE_BONUS) or (apply_number == EPointTypes.LG_POINT_DEF_GRADE_BONUS) or (apply_number == EPointTypes.LG_POINT_MAGIC_ATT_GRADE) or (apply_number == EPointTypes.LG_POINT_MAGIC_DEF_GRADE) or (apply_number == EPointTypes.LG_POINT_MAX_STAMINA) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_WARRIOR) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_ASSASSIN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_SHURA) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_MAGE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_WOLFMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MONSTER) or (apply_number == EPointTypes.LG_POINT_MALL_ATTBONUS):
            return LC_TEXT("Attack + %d%%")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_CRITICAL) or (apply_number == EPointTypes.LG_POINT_PENETRATE_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_PENETRATE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_HUMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ANIMAL) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ORC) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MILGYO) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_UNDEAD) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_DEVIL) or (apply_number == EPointTypes.LG_POINT_STEAL_HP) or (apply_number == EPointTypes.LG_POINT_STEAL_SP) or (apply_number == EPointTypes.LG_POINT_MANA_BURN_PCT) or (apply_number == EPointTypes.LG_POINT_DAMAGE_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_BLOCK) or (apply_number == EPointTypes.LG_POINT_DODGE) or (apply_number == EPointTypes.LG_POINT_RESIST_SWORD) or (apply_number == EPointTypes.LG_POINT_RESIST_TWOHAND) or (apply_number == EPointTypes.LG_POINT_RESIST_DAGGER) or (apply_number == EPointTypes.LG_POINT_RESIST_BELL) or (apply_number == EPointTypes.LG_POINT_RESIST_FAN) or (apply_number == EPointTypes.LG_POINT_RESIST_BOW) or (apply_number == EPointTypes.LG_POINT_RESIST_CLAW) or (apply_number == EPointTypes.LG_POINT_RESIST_FIRE) or (apply_number == EPointTypes.LG_POINT_RESIST_ELEC) or (apply_number == EPointTypes.LG_POINT_RESIST_MAGIC) or (apply_number == EPointTypes.LG_POINT_RESIST_WIND) or (apply_number == EPointTypes.LG_POINT_RESIST_ICE) or (apply_number == EPointTypes.LG_POINT_RESIST_EARTH) or (apply_number == EPointTypes.LG_POINT_RESIST_DARK) or (apply_number == EPointTypes.LG_POINT_REFLECT_MELEE) or (apply_number == EPointTypes.LG_POINT_REFLECT_CURSE) or (apply_number == EPointTypes.LG_POINT_POISON_REDUCE) or (apply_number == EPointTypes.LG_POINT_BLEEDING_REDUCE) or (apply_number == EPointTypes.LG_POINT_KILL_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_EXP_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_GOLD_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_ITEM_DROP_BONUS) or (apply_number == EPointTypes.LG_POINT_POTION_BONUS) or (apply_number == EPointTypes.LG_POINT_KILL_HP_RECOVERY) or (apply_number == EPointTypes.LG_POINT_ATT_GRADE_BONUS) or (apply_number == EPointTypes.LG_POINT_DEF_GRADE_BONUS) or (apply_number == EPointTypes.LG_POINT_MAGIC_ATT_GRADE) or (apply_number == EPointTypes.LG_POINT_MAGIC_DEF_GRADE) or (apply_number == EPointTypes.LG_POINT_MAX_STAMINA) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_WARRIOR) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_ASSASSIN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_SHURA) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_MAGE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_WOLFMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MONSTER) or (apply_number == EPointTypes.LG_POINT_MALL_ATTBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_DEFBONUS):
            return LC_TEXT("Defence + %d%%")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_CRITICAL) or (apply_number == EPointTypes.LG_POINT_PENETRATE_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_PENETRATE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_HUMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ANIMAL) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ORC) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MILGYO) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_UNDEAD) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_DEVIL) or (apply_number == EPointTypes.LG_POINT_STEAL_HP) or (apply_number == EPointTypes.LG_POINT_STEAL_SP) or (apply_number == EPointTypes.LG_POINT_MANA_BURN_PCT) or (apply_number == EPointTypes.LG_POINT_DAMAGE_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_BLOCK) or (apply_number == EPointTypes.LG_POINT_DODGE) or (apply_number == EPointTypes.LG_POINT_RESIST_SWORD) or (apply_number == EPointTypes.LG_POINT_RESIST_TWOHAND) or (apply_number == EPointTypes.LG_POINT_RESIST_DAGGER) or (apply_number == EPointTypes.LG_POINT_RESIST_BELL) or (apply_number == EPointTypes.LG_POINT_RESIST_FAN) or (apply_number == EPointTypes.LG_POINT_RESIST_BOW) or (apply_number == EPointTypes.LG_POINT_RESIST_CLAW) or (apply_number == EPointTypes.LG_POINT_RESIST_FIRE) or (apply_number == EPointTypes.LG_POINT_RESIST_ELEC) or (apply_number == EPointTypes.LG_POINT_RESIST_MAGIC) or (apply_number == EPointTypes.LG_POINT_RESIST_WIND) or (apply_number == EPointTypes.LG_POINT_RESIST_ICE) or (apply_number == EPointTypes.LG_POINT_RESIST_EARTH) or (apply_number == EPointTypes.LG_POINT_RESIST_DARK) or (apply_number == EPointTypes.LG_POINT_REFLECT_MELEE) or (apply_number == EPointTypes.LG_POINT_REFLECT_CURSE) or (apply_number == EPointTypes.LG_POINT_POISON_REDUCE) or (apply_number == EPointTypes.LG_POINT_BLEEDING_REDUCE) or (apply_number == EPointTypes.LG_POINT_KILL_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_EXP_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_GOLD_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_ITEM_DROP_BONUS) or (apply_number == EPointTypes.LG_POINT_POTION_BONUS) or (apply_number == EPointTypes.LG_POINT_KILL_HP_RECOVERY) or (apply_number == EPointTypes.LG_POINT_ATT_GRADE_BONUS) or (apply_number == EPointTypes.LG_POINT_DEF_GRADE_BONUS) or (apply_number == EPointTypes.LG_POINT_MAGIC_ATT_GRADE) or (apply_number == EPointTypes.LG_POINT_MAGIC_DEF_GRADE) or (apply_number == EPointTypes.LG_POINT_MAX_STAMINA) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_WARRIOR) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_ASSASSIN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_SHURA) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_MAGE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_WOLFMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MONSTER) or (apply_number == EPointTypes.LG_POINT_MALL_ATTBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_DEFBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_EXPBONUS):
            return LC_TEXT("Experience %d%%")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_CRITICAL) or (apply_number == EPointTypes.LG_POINT_PENETRATE_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_PENETRATE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_HUMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ANIMAL) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ORC) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MILGYO) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_UNDEAD) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_DEVIL) or (apply_number == EPointTypes.LG_POINT_STEAL_HP) or (apply_number == EPointTypes.LG_POINT_STEAL_SP) or (apply_number == EPointTypes.LG_POINT_MANA_BURN_PCT) or (apply_number == EPointTypes.LG_POINT_DAMAGE_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_BLOCK) or (apply_number == EPointTypes.LG_POINT_DODGE) or (apply_number == EPointTypes.LG_POINT_RESIST_SWORD) or (apply_number == EPointTypes.LG_POINT_RESIST_TWOHAND) or (apply_number == EPointTypes.LG_POINT_RESIST_DAGGER) or (apply_number == EPointTypes.LG_POINT_RESIST_BELL) or (apply_number == EPointTypes.LG_POINT_RESIST_FAN) or (apply_number == EPointTypes.LG_POINT_RESIST_BOW) or (apply_number == EPointTypes.LG_POINT_RESIST_CLAW) or (apply_number == EPointTypes.LG_POINT_RESIST_FIRE) or (apply_number == EPointTypes.LG_POINT_RESIST_ELEC) or (apply_number == EPointTypes.LG_POINT_RESIST_MAGIC) or (apply_number == EPointTypes.LG_POINT_RESIST_WIND) or (apply_number == EPointTypes.LG_POINT_RESIST_ICE) or (apply_number == EPointTypes.LG_POINT_RESIST_EARTH) or (apply_number == EPointTypes.LG_POINT_RESIST_DARK) or (apply_number == EPointTypes.LG_POINT_REFLECT_MELEE) or (apply_number == EPointTypes.LG_POINT_REFLECT_CURSE) or (apply_number == EPointTypes.LG_POINT_POISON_REDUCE) or (apply_number == EPointTypes.LG_POINT_BLEEDING_REDUCE) or (apply_number == EPointTypes.LG_POINT_KILL_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_EXP_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_GOLD_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_ITEM_DROP_BONUS) or (apply_number == EPointTypes.LG_POINT_POTION_BONUS) or (apply_number == EPointTypes.LG_POINT_KILL_HP_RECOVERY) or (apply_number == EPointTypes.LG_POINT_ATT_GRADE_BONUS) or (apply_number == EPointTypes.LG_POINT_DEF_GRADE_BONUS) or (apply_number == EPointTypes.LG_POINT_MAGIC_ATT_GRADE) or (apply_number == EPointTypes.LG_POINT_MAGIC_DEF_GRADE) or (apply_number == EPointTypes.LG_POINT_MAX_STAMINA) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_WARRIOR) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_ASSASSIN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_SHURA) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_MAGE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_WOLFMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MONSTER) or (apply_number == EPointTypes.LG_POINT_MALL_ATTBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_DEFBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_EXPBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_ITEMBONUS):
            return LC_TEXT("Chance to find an Item %. 1f")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_CRITICAL) or (apply_number == EPointTypes.LG_POINT_PENETRATE_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_PENETRATE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_HUMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ANIMAL) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ORC) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MILGYO) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_UNDEAD) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_DEVIL) or (apply_number == EPointTypes.LG_POINT_STEAL_HP) or (apply_number == EPointTypes.LG_POINT_STEAL_SP) or (apply_number == EPointTypes.LG_POINT_MANA_BURN_PCT) or (apply_number == EPointTypes.LG_POINT_DAMAGE_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_BLOCK) or (apply_number == EPointTypes.LG_POINT_DODGE) or (apply_number == EPointTypes.LG_POINT_RESIST_SWORD) or (apply_number == EPointTypes.LG_POINT_RESIST_TWOHAND) or (apply_number == EPointTypes.LG_POINT_RESIST_DAGGER) or (apply_number == EPointTypes.LG_POINT_RESIST_BELL) or (apply_number == EPointTypes.LG_POINT_RESIST_FAN) or (apply_number == EPointTypes.LG_POINT_RESIST_BOW) or (apply_number == EPointTypes.LG_POINT_RESIST_CLAW) or (apply_number == EPointTypes.LG_POINT_RESIST_FIRE) or (apply_number == EPointTypes.LG_POINT_RESIST_ELEC) or (apply_number == EPointTypes.LG_POINT_RESIST_MAGIC) or (apply_number == EPointTypes.LG_POINT_RESIST_WIND) or (apply_number == EPointTypes.LG_POINT_RESIST_ICE) or (apply_number == EPointTypes.LG_POINT_RESIST_EARTH) or (apply_number == EPointTypes.LG_POINT_RESIST_DARK) or (apply_number == EPointTypes.LG_POINT_REFLECT_MELEE) or (apply_number == EPointTypes.LG_POINT_REFLECT_CURSE) or (apply_number == EPointTypes.LG_POINT_POISON_REDUCE) or (apply_number == EPointTypes.LG_POINT_BLEEDING_REDUCE) or (apply_number == EPointTypes.LG_POINT_KILL_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_EXP_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_GOLD_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_ITEM_DROP_BONUS) or (apply_number == EPointTypes.LG_POINT_POTION_BONUS) or (apply_number == EPointTypes.LG_POINT_KILL_HP_RECOVERY) or (apply_number == EPointTypes.LG_POINT_ATT_GRADE_BONUS) or (apply_number == EPointTypes.LG_POINT_DEF_GRADE_BONUS) or (apply_number == EPointTypes.LG_POINT_MAGIC_ATT_GRADE) or (apply_number == EPointTypes.LG_POINT_MAGIC_DEF_GRADE) or (apply_number == EPointTypes.LG_POINT_MAX_STAMINA) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_WARRIOR) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_ASSASSIN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_SHURA) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_MAGE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_WOLFMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MONSTER) or (apply_number == EPointTypes.LG_POINT_MALL_ATTBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_DEFBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_EXPBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_ITEMBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_GOLDBONUS):
            return LC_TEXT("Chance to find Yang %. 1f")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_CRITICAL) or (apply_number == EPointTypes.LG_POINT_PENETRATE_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_PENETRATE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_HUMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ANIMAL) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ORC) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MILGYO) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_UNDEAD) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_DEVIL) or (apply_number == EPointTypes.LG_POINT_STEAL_HP) or (apply_number == EPointTypes.LG_POINT_STEAL_SP) or (apply_number == EPointTypes.LG_POINT_MANA_BURN_PCT) or (apply_number == EPointTypes.LG_POINT_DAMAGE_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_BLOCK) or (apply_number == EPointTypes.LG_POINT_DODGE) or (apply_number == EPointTypes.LG_POINT_RESIST_SWORD) or (apply_number == EPointTypes.LG_POINT_RESIST_TWOHAND) or (apply_number == EPointTypes.LG_POINT_RESIST_DAGGER) or (apply_number == EPointTypes.LG_POINT_RESIST_BELL) or (apply_number == EPointTypes.LG_POINT_RESIST_FAN) or (apply_number == EPointTypes.LG_POINT_RESIST_BOW) or (apply_number == EPointTypes.LG_POINT_RESIST_CLAW) or (apply_number == EPointTypes.LG_POINT_RESIST_FIRE) or (apply_number == EPointTypes.LG_POINT_RESIST_ELEC) or (apply_number == EPointTypes.LG_POINT_RESIST_MAGIC) or (apply_number == EPointTypes.LG_POINT_RESIST_WIND) or (apply_number == EPointTypes.LG_POINT_RESIST_ICE) or (apply_number == EPointTypes.LG_POINT_RESIST_EARTH) or (apply_number == EPointTypes.LG_POINT_RESIST_DARK) or (apply_number == EPointTypes.LG_POINT_REFLECT_MELEE) or (apply_number == EPointTypes.LG_POINT_REFLECT_CURSE) or (apply_number == EPointTypes.LG_POINT_POISON_REDUCE) or (apply_number == EPointTypes.LG_POINT_BLEEDING_REDUCE) or (apply_number == EPointTypes.LG_POINT_KILL_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_EXP_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_GOLD_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_ITEM_DROP_BONUS) or (apply_number == EPointTypes.LG_POINT_POTION_BONUS) or (apply_number == EPointTypes.LG_POINT_KILL_HP_RECOVERY) or (apply_number == EPointTypes.LG_POINT_ATT_GRADE_BONUS) or (apply_number == EPointTypes.LG_POINT_DEF_GRADE_BONUS) or (apply_number == EPointTypes.LG_POINT_MAGIC_ATT_GRADE) or (apply_number == EPointTypes.LG_POINT_MAGIC_DEF_GRADE) or (apply_number == EPointTypes.LG_POINT_MAX_STAMINA) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_WARRIOR) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_ASSASSIN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_SHURA) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_MAGE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_WOLFMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MONSTER) or (apply_number == EPointTypes.LG_POINT_MALL_ATTBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_DEFBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_EXPBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_ITEMBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_GOLDBONUS) or (apply_number == EPointTypes.LG_POINT_MAX_HP_PCT):
            return LC_TEXT("Energy Upper Limit +%d%%")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_CRITICAL) or (apply_number == EPointTypes.LG_POINT_PENETRATE_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_PENETRATE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_HUMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ANIMAL) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ORC) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MILGYO) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_UNDEAD) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_DEVIL) or (apply_number == EPointTypes.LG_POINT_STEAL_HP) or (apply_number == EPointTypes.LG_POINT_STEAL_SP) or (apply_number == EPointTypes.LG_POINT_MANA_BURN_PCT) or (apply_number == EPointTypes.LG_POINT_DAMAGE_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_BLOCK) or (apply_number == EPointTypes.LG_POINT_DODGE) or (apply_number == EPointTypes.LG_POINT_RESIST_SWORD) or (apply_number == EPointTypes.LG_POINT_RESIST_TWOHAND) or (apply_number == EPointTypes.LG_POINT_RESIST_DAGGER) or (apply_number == EPointTypes.LG_POINT_RESIST_BELL) or (apply_number == EPointTypes.LG_POINT_RESIST_FAN) or (apply_number == EPointTypes.LG_POINT_RESIST_BOW) or (apply_number == EPointTypes.LG_POINT_RESIST_CLAW) or (apply_number == EPointTypes.LG_POINT_RESIST_FIRE) or (apply_number == EPointTypes.LG_POINT_RESIST_ELEC) or (apply_number == EPointTypes.LG_POINT_RESIST_MAGIC) or (apply_number == EPointTypes.LG_POINT_RESIST_WIND) or (apply_number == EPointTypes.LG_POINT_RESIST_ICE) or (apply_number == EPointTypes.LG_POINT_RESIST_EARTH) or (apply_number == EPointTypes.LG_POINT_RESIST_DARK) or (apply_number == EPointTypes.LG_POINT_REFLECT_MELEE) or (apply_number == EPointTypes.LG_POINT_REFLECT_CURSE) or (apply_number == EPointTypes.LG_POINT_POISON_REDUCE) or (apply_number == EPointTypes.LG_POINT_BLEEDING_REDUCE) or (apply_number == EPointTypes.LG_POINT_KILL_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_EXP_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_GOLD_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_ITEM_DROP_BONUS) or (apply_number == EPointTypes.LG_POINT_POTION_BONUS) or (apply_number == EPointTypes.LG_POINT_KILL_HP_RECOVERY) or (apply_number == EPointTypes.LG_POINT_ATT_GRADE_BONUS) or (apply_number == EPointTypes.LG_POINT_DEF_GRADE_BONUS) or (apply_number == EPointTypes.LG_POINT_MAGIC_ATT_GRADE) or (apply_number == EPointTypes.LG_POINT_MAGIC_DEF_GRADE) or (apply_number == EPointTypes.LG_POINT_MAX_STAMINA) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_WARRIOR) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_ASSASSIN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_SHURA) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_MAGE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_WOLFMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MONSTER) or (apply_number == EPointTypes.LG_POINT_MALL_ATTBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_DEFBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_EXPBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_ITEMBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_GOLDBONUS) or (apply_number == EPointTypes.LG_POINT_MAX_HP_PCT) or (apply_number == EPointTypes.LG_POINT_MAX_SP_PCT):
            return LC_TEXT("Energy Upper Limit +%d%%")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_CRITICAL) or (apply_number == EPointTypes.LG_POINT_PENETRATE_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_PENETRATE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_HUMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ANIMAL) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ORC) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MILGYO) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_UNDEAD) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_DEVIL) or (apply_number == EPointTypes.LG_POINT_STEAL_HP) or (apply_number == EPointTypes.LG_POINT_STEAL_SP) or (apply_number == EPointTypes.LG_POINT_MANA_BURN_PCT) or (apply_number == EPointTypes.LG_POINT_DAMAGE_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_BLOCK) or (apply_number == EPointTypes.LG_POINT_DODGE) or (apply_number == EPointTypes.LG_POINT_RESIST_SWORD) or (apply_number == EPointTypes.LG_POINT_RESIST_TWOHAND) or (apply_number == EPointTypes.LG_POINT_RESIST_DAGGER) or (apply_number == EPointTypes.LG_POINT_RESIST_BELL) or (apply_number == EPointTypes.LG_POINT_RESIST_FAN) or (apply_number == EPointTypes.LG_POINT_RESIST_BOW) or (apply_number == EPointTypes.LG_POINT_RESIST_CLAW) or (apply_number == EPointTypes.LG_POINT_RESIST_FIRE) or (apply_number == EPointTypes.LG_POINT_RESIST_ELEC) or (apply_number == EPointTypes.LG_POINT_RESIST_MAGIC) or (apply_number == EPointTypes.LG_POINT_RESIST_WIND) or (apply_number == EPointTypes.LG_POINT_RESIST_ICE) or (apply_number == EPointTypes.LG_POINT_RESIST_EARTH) or (apply_number == EPointTypes.LG_POINT_RESIST_DARK) or (apply_number == EPointTypes.LG_POINT_REFLECT_MELEE) or (apply_number == EPointTypes.LG_POINT_REFLECT_CURSE) or (apply_number == EPointTypes.LG_POINT_POISON_REDUCE) or (apply_number == EPointTypes.LG_POINT_BLEEDING_REDUCE) or (apply_number == EPointTypes.LG_POINT_KILL_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_EXP_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_GOLD_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_ITEM_DROP_BONUS) or (apply_number == EPointTypes.LG_POINT_POTION_BONUS) or (apply_number == EPointTypes.LG_POINT_KILL_HP_RECOVERY) or (apply_number == EPointTypes.LG_POINT_ATT_GRADE_BONUS) or (apply_number == EPointTypes.LG_POINT_DEF_GRADE_BONUS) or (apply_number == EPointTypes.LG_POINT_MAGIC_ATT_GRADE) or (apply_number == EPointTypes.LG_POINT_MAGIC_DEF_GRADE) or (apply_number == EPointTypes.LG_POINT_MAX_STAMINA) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_WARRIOR) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_ASSASSIN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_SHURA) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_MAGE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_WOLFMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MONSTER) or (apply_number == EPointTypes.LG_POINT_MALL_ATTBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_DEFBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_EXPBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_ITEMBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_GOLDBONUS) or (apply_number == EPointTypes.LG_POINT_MAX_HP_PCT) or (apply_number == EPointTypes.LG_POINT_MAX_SP_PCT) or (apply_number == EPointTypes.LG_POINT_LG_SKILL_DAMAGE_BONUS):
            return LC_TEXT("Skill Damage %d%%")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_CRITICAL) or (apply_number == EPointTypes.LG_POINT_PENETRATE_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_PENETRATE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_HUMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ANIMAL) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ORC) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MILGYO) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_UNDEAD) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_DEVIL) or (apply_number == EPointTypes.LG_POINT_STEAL_HP) or (apply_number == EPointTypes.LG_POINT_STEAL_SP) or (apply_number == EPointTypes.LG_POINT_MANA_BURN_PCT) or (apply_number == EPointTypes.LG_POINT_DAMAGE_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_BLOCK) or (apply_number == EPointTypes.LG_POINT_DODGE) or (apply_number == EPointTypes.LG_POINT_RESIST_SWORD) or (apply_number == EPointTypes.LG_POINT_RESIST_TWOHAND) or (apply_number == EPointTypes.LG_POINT_RESIST_DAGGER) or (apply_number == EPointTypes.LG_POINT_RESIST_BELL) or (apply_number == EPointTypes.LG_POINT_RESIST_FAN) or (apply_number == EPointTypes.LG_POINT_RESIST_BOW) or (apply_number == EPointTypes.LG_POINT_RESIST_CLAW) or (apply_number == EPointTypes.LG_POINT_RESIST_FIRE) or (apply_number == EPointTypes.LG_POINT_RESIST_ELEC) or (apply_number == EPointTypes.LG_POINT_RESIST_MAGIC) or (apply_number == EPointTypes.LG_POINT_RESIST_WIND) or (apply_number == EPointTypes.LG_POINT_RESIST_ICE) or (apply_number == EPointTypes.LG_POINT_RESIST_EARTH) or (apply_number == EPointTypes.LG_POINT_RESIST_DARK) or (apply_number == EPointTypes.LG_POINT_REFLECT_MELEE) or (apply_number == EPointTypes.LG_POINT_REFLECT_CURSE) or (apply_number == EPointTypes.LG_POINT_POISON_REDUCE) or (apply_number == EPointTypes.LG_POINT_BLEEDING_REDUCE) or (apply_number == EPointTypes.LG_POINT_KILL_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_EXP_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_GOLD_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_ITEM_DROP_BONUS) or (apply_number == EPointTypes.LG_POINT_POTION_BONUS) or (apply_number == EPointTypes.LG_POINT_KILL_HP_RECOVERY) or (apply_number == EPointTypes.LG_POINT_ATT_GRADE_BONUS) or (apply_number == EPointTypes.LG_POINT_DEF_GRADE_BONUS) or (apply_number == EPointTypes.LG_POINT_MAGIC_ATT_GRADE) or (apply_number == EPointTypes.LG_POINT_MAGIC_DEF_GRADE) or (apply_number == EPointTypes.LG_POINT_MAX_STAMINA) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_WARRIOR) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_ASSASSIN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_SHURA) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_MAGE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_WOLFMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MONSTER) or (apply_number == EPointTypes.LG_POINT_MALL_ATTBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_DEFBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_EXPBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_ITEMBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_GOLDBONUS) or (apply_number == EPointTypes.LG_POINT_MAX_HP_PCT) or (apply_number == EPointTypes.LG_POINT_MAX_SP_PCT) or (apply_number == EPointTypes.LG_POINT_LG_SKILL_DAMAGE_BONUS) or (apply_number == EPointTypes.LG_POINT_NORMAL_HIT_DAMAGE_BONUS):
            return LC_TEXT("Hit Damage %d%%")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_CRITICAL) or (apply_number == EPointTypes.LG_POINT_PENETRATE_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_PENETRATE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_HUMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ANIMAL) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ORC) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MILGYO) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_UNDEAD) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_DEVIL) or (apply_number == EPointTypes.LG_POINT_STEAL_HP) or (apply_number == EPointTypes.LG_POINT_STEAL_SP) or (apply_number == EPointTypes.LG_POINT_MANA_BURN_PCT) or (apply_number == EPointTypes.LG_POINT_DAMAGE_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_BLOCK) or (apply_number == EPointTypes.LG_POINT_DODGE) or (apply_number == EPointTypes.LG_POINT_RESIST_SWORD) or (apply_number == EPointTypes.LG_POINT_RESIST_TWOHAND) or (apply_number == EPointTypes.LG_POINT_RESIST_DAGGER) or (apply_number == EPointTypes.LG_POINT_RESIST_BELL) or (apply_number == EPointTypes.LG_POINT_RESIST_FAN) or (apply_number == EPointTypes.LG_POINT_RESIST_BOW) or (apply_number == EPointTypes.LG_POINT_RESIST_CLAW) or (apply_number == EPointTypes.LG_POINT_RESIST_FIRE) or (apply_number == EPointTypes.LG_POINT_RESIST_ELEC) or (apply_number == EPointTypes.LG_POINT_RESIST_MAGIC) or (apply_number == EPointTypes.LG_POINT_RESIST_WIND) or (apply_number == EPointTypes.LG_POINT_RESIST_ICE) or (apply_number == EPointTypes.LG_POINT_RESIST_EARTH) or (apply_number == EPointTypes.LG_POINT_RESIST_DARK) or (apply_number == EPointTypes.LG_POINT_REFLECT_MELEE) or (apply_number == EPointTypes.LG_POINT_REFLECT_CURSE) or (apply_number == EPointTypes.LG_POINT_POISON_REDUCE) or (apply_number == EPointTypes.LG_POINT_BLEEDING_REDUCE) or (apply_number == EPointTypes.LG_POINT_KILL_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_EXP_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_GOLD_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_ITEM_DROP_BONUS) or (apply_number == EPointTypes.LG_POINT_POTION_BONUS) or (apply_number == EPointTypes.LG_POINT_KILL_HP_RECOVERY) or (apply_number == EPointTypes.LG_POINT_ATT_GRADE_BONUS) or (apply_number == EPointTypes.LG_POINT_DEF_GRADE_BONUS) or (apply_number == EPointTypes.LG_POINT_MAGIC_ATT_GRADE) or (apply_number == EPointTypes.LG_POINT_MAGIC_DEF_GRADE) or (apply_number == EPointTypes.LG_POINT_MAX_STAMINA) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_WARRIOR) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_ASSASSIN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_SHURA) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_MAGE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_WOLFMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MONSTER) or (apply_number == EPointTypes.LG_POINT_MALL_ATTBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_DEFBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_EXPBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_ITEMBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_GOLDBONUS) or (apply_number == EPointTypes.LG_POINT_MAX_HP_PCT) or (apply_number == EPointTypes.LG_POINT_MAX_SP_PCT) or (apply_number == EPointTypes.LG_POINT_LG_SKILL_DAMAGE_BONUS) or (apply_number == EPointTypes.LG_POINT_NORMAL_HIT_DAMAGE_BONUS) or (apply_number == EPointTypes.LG_POINT_LG_SKILL_DEFEND_BONUS):
            return LC_TEXT("Resistance against Skill Damage %d%%")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_CRITICAL) or (apply_number == EPointTypes.LG_POINT_PENETRATE_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_PENETRATE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_HUMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ANIMAL) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ORC) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MILGYO) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_UNDEAD) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_DEVIL) or (apply_number == EPointTypes.LG_POINT_STEAL_HP) or (apply_number == EPointTypes.LG_POINT_STEAL_SP) or (apply_number == EPointTypes.LG_POINT_MANA_BURN_PCT) or (apply_number == EPointTypes.LG_POINT_DAMAGE_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_BLOCK) or (apply_number == EPointTypes.LG_POINT_DODGE) or (apply_number == EPointTypes.LG_POINT_RESIST_SWORD) or (apply_number == EPointTypes.LG_POINT_RESIST_TWOHAND) or (apply_number == EPointTypes.LG_POINT_RESIST_DAGGER) or (apply_number == EPointTypes.LG_POINT_RESIST_BELL) or (apply_number == EPointTypes.LG_POINT_RESIST_FAN) or (apply_number == EPointTypes.LG_POINT_RESIST_BOW) or (apply_number == EPointTypes.LG_POINT_RESIST_CLAW) or (apply_number == EPointTypes.LG_POINT_RESIST_FIRE) or (apply_number == EPointTypes.LG_POINT_RESIST_ELEC) or (apply_number == EPointTypes.LG_POINT_RESIST_MAGIC) or (apply_number == EPointTypes.LG_POINT_RESIST_WIND) or (apply_number == EPointTypes.LG_POINT_RESIST_ICE) or (apply_number == EPointTypes.LG_POINT_RESIST_EARTH) or (apply_number == EPointTypes.LG_POINT_RESIST_DARK) or (apply_number == EPointTypes.LG_POINT_REFLECT_MELEE) or (apply_number == EPointTypes.LG_POINT_REFLECT_CURSE) or (apply_number == EPointTypes.LG_POINT_POISON_REDUCE) or (apply_number == EPointTypes.LG_POINT_BLEEDING_REDUCE) or (apply_number == EPointTypes.LG_POINT_KILL_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_EXP_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_GOLD_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_ITEM_DROP_BONUS) or (apply_number == EPointTypes.LG_POINT_POTION_BONUS) or (apply_number == EPointTypes.LG_POINT_KILL_HP_RECOVERY) or (apply_number == EPointTypes.LG_POINT_ATT_GRADE_BONUS) or (apply_number == EPointTypes.LG_POINT_DEF_GRADE_BONUS) or (apply_number == EPointTypes.LG_POINT_MAGIC_ATT_GRADE) or (apply_number == EPointTypes.LG_POINT_MAGIC_DEF_GRADE) or (apply_number == EPointTypes.LG_POINT_MAX_STAMINA) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_WARRIOR) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_ASSASSIN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_SHURA) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_MAGE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_WOLFMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MONSTER) or (apply_number == EPointTypes.LG_POINT_MALL_ATTBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_DEFBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_EXPBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_ITEMBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_GOLDBONUS) or (apply_number == EPointTypes.LG_POINT_MAX_HP_PCT) or (apply_number == EPointTypes.LG_POINT_MAX_SP_PCT) or (apply_number == EPointTypes.LG_POINT_LG_SKILL_DAMAGE_BONUS) or (apply_number == EPointTypes.LG_POINT_NORMAL_HIT_DAMAGE_BONUS) or (apply_number == EPointTypes.LG_POINT_LG_SKILL_DEFEND_BONUS) or (apply_number == EPointTypes.LG_POINT_NORMAL_HIT_DEFEND_BONUS):
            return LC_TEXT("Resistance against Hits %d%%")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_CRITICAL) or (apply_number == EPointTypes.LG_POINT_PENETRATE_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_PENETRATE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_HUMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ANIMAL) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ORC) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MILGYO) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_UNDEAD) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_DEVIL) or (apply_number == EPointTypes.LG_POINT_STEAL_HP) or (apply_number == EPointTypes.LG_POINT_STEAL_SP) or (apply_number == EPointTypes.LG_POINT_MANA_BURN_PCT) or (apply_number == EPointTypes.LG_POINT_DAMAGE_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_BLOCK) or (apply_number == EPointTypes.LG_POINT_DODGE) or (apply_number == EPointTypes.LG_POINT_RESIST_SWORD) or (apply_number == EPointTypes.LG_POINT_RESIST_TWOHAND) or (apply_number == EPointTypes.LG_POINT_RESIST_DAGGER) or (apply_number == EPointTypes.LG_POINT_RESIST_BELL) or (apply_number == EPointTypes.LG_POINT_RESIST_FAN) or (apply_number == EPointTypes.LG_POINT_RESIST_BOW) or (apply_number == EPointTypes.LG_POINT_RESIST_CLAW) or (apply_number == EPointTypes.LG_POINT_RESIST_FIRE) or (apply_number == EPointTypes.LG_POINT_RESIST_ELEC) or (apply_number == EPointTypes.LG_POINT_RESIST_MAGIC) or (apply_number == EPointTypes.LG_POINT_RESIST_WIND) or (apply_number == EPointTypes.LG_POINT_RESIST_ICE) or (apply_number == EPointTypes.LG_POINT_RESIST_EARTH) or (apply_number == EPointTypes.LG_POINT_RESIST_DARK) or (apply_number == EPointTypes.LG_POINT_REFLECT_MELEE) or (apply_number == EPointTypes.LG_POINT_REFLECT_CURSE) or (apply_number == EPointTypes.LG_POINT_POISON_REDUCE) or (apply_number == EPointTypes.LG_POINT_BLEEDING_REDUCE) or (apply_number == EPointTypes.LG_POINT_KILL_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_EXP_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_GOLD_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_ITEM_DROP_BONUS) or (apply_number == EPointTypes.LG_POINT_POTION_BONUS) or (apply_number == EPointTypes.LG_POINT_KILL_HP_RECOVERY) or (apply_number == EPointTypes.LG_POINT_ATT_GRADE_BONUS) or (apply_number == EPointTypes.LG_POINT_DEF_GRADE_BONUS) or (apply_number == EPointTypes.LG_POINT_MAGIC_ATT_GRADE) or (apply_number == EPointTypes.LG_POINT_MAGIC_DEF_GRADE) or (apply_number == EPointTypes.LG_POINT_MAX_STAMINA) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_WARRIOR) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_ASSASSIN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_SHURA) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_MAGE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_WOLFMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MONSTER) or (apply_number == EPointTypes.LG_POINT_MALL_ATTBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_DEFBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_EXPBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_ITEMBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_GOLDBONUS) or (apply_number == EPointTypes.LG_POINT_MAX_HP_PCT) or (apply_number == EPointTypes.LG_POINT_MAX_SP_PCT) or (apply_number == EPointTypes.LG_POINT_LG_SKILL_DAMAGE_BONUS) or (apply_number == EPointTypes.LG_POINT_NORMAL_HIT_DAMAGE_BONUS) or (apply_number == EPointTypes.LG_POINT_LG_SKILL_DEFEND_BONUS) or (apply_number == EPointTypes.LG_POINT_NORMAL_HIT_DEFEND_BONUS) or (apply_number == EPointTypes.LG_POINT_RESIST_LG_PAWN_WARRIOR):
            return LC_TEXT("%d%% Resistance against LG_PAWN_WARRIOR Attacks")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_CRITICAL) or (apply_number == EPointTypes.LG_POINT_PENETRATE_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_PENETRATE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_HUMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ANIMAL) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ORC) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MILGYO) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_UNDEAD) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_DEVIL) or (apply_number == EPointTypes.LG_POINT_STEAL_HP) or (apply_number == EPointTypes.LG_POINT_STEAL_SP) or (apply_number == EPointTypes.LG_POINT_MANA_BURN_PCT) or (apply_number == EPointTypes.LG_POINT_DAMAGE_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_BLOCK) or (apply_number == EPointTypes.LG_POINT_DODGE) or (apply_number == EPointTypes.LG_POINT_RESIST_SWORD) or (apply_number == EPointTypes.LG_POINT_RESIST_TWOHAND) or (apply_number == EPointTypes.LG_POINT_RESIST_DAGGER) or (apply_number == EPointTypes.LG_POINT_RESIST_BELL) or (apply_number == EPointTypes.LG_POINT_RESIST_FAN) or (apply_number == EPointTypes.LG_POINT_RESIST_BOW) or (apply_number == EPointTypes.LG_POINT_RESIST_CLAW) or (apply_number == EPointTypes.LG_POINT_RESIST_FIRE) or (apply_number == EPointTypes.LG_POINT_RESIST_ELEC) or (apply_number == EPointTypes.LG_POINT_RESIST_MAGIC) or (apply_number == EPointTypes.LG_POINT_RESIST_WIND) or (apply_number == EPointTypes.LG_POINT_RESIST_ICE) or (apply_number == EPointTypes.LG_POINT_RESIST_EARTH) or (apply_number == EPointTypes.LG_POINT_RESIST_DARK) or (apply_number == EPointTypes.LG_POINT_REFLECT_MELEE) or (apply_number == EPointTypes.LG_POINT_REFLECT_CURSE) or (apply_number == EPointTypes.LG_POINT_POISON_REDUCE) or (apply_number == EPointTypes.LG_POINT_BLEEDING_REDUCE) or (apply_number == EPointTypes.LG_POINT_KILL_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_EXP_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_GOLD_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_ITEM_DROP_BONUS) or (apply_number == EPointTypes.LG_POINT_POTION_BONUS) or (apply_number == EPointTypes.LG_POINT_KILL_HP_RECOVERY) or (apply_number == EPointTypes.LG_POINT_ATT_GRADE_BONUS) or (apply_number == EPointTypes.LG_POINT_DEF_GRADE_BONUS) or (apply_number == EPointTypes.LG_POINT_MAGIC_ATT_GRADE) or (apply_number == EPointTypes.LG_POINT_MAGIC_DEF_GRADE) or (apply_number == EPointTypes.LG_POINT_MAX_STAMINA) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_WARRIOR) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_ASSASSIN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_SHURA) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_MAGE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_WOLFMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MONSTER) or (apply_number == EPointTypes.LG_POINT_MALL_ATTBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_DEFBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_EXPBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_ITEMBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_GOLDBONUS) or (apply_number == EPointTypes.LG_POINT_MAX_HP_PCT) or (apply_number == EPointTypes.LG_POINT_MAX_SP_PCT) or (apply_number == EPointTypes.LG_POINT_LG_SKILL_DAMAGE_BONUS) or (apply_number == EPointTypes.LG_POINT_NORMAL_HIT_DAMAGE_BONUS) or (apply_number == EPointTypes.LG_POINT_LG_SKILL_DEFEND_BONUS) or (apply_number == EPointTypes.LG_POINT_NORMAL_HIT_DEFEND_BONUS) or (apply_number == EPointTypes.LG_POINT_RESIST_LG_PAWN_WARRIOR) or (apply_number == EPointTypes.LG_POINT_RESIST_LG_PAWN_ASSASSIN):
            return LC_TEXT("%d%% Resistance against Ninja Attacks")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_CRITICAL) or (apply_number == EPointTypes.LG_POINT_PENETRATE_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_PENETRATE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_HUMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ANIMAL) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ORC) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MILGYO) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_UNDEAD) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_DEVIL) or (apply_number == EPointTypes.LG_POINT_STEAL_HP) or (apply_number == EPointTypes.LG_POINT_STEAL_SP) or (apply_number == EPointTypes.LG_POINT_MANA_BURN_PCT) or (apply_number == EPointTypes.LG_POINT_DAMAGE_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_BLOCK) or (apply_number == EPointTypes.LG_POINT_DODGE) or (apply_number == EPointTypes.LG_POINT_RESIST_SWORD) or (apply_number == EPointTypes.LG_POINT_RESIST_TWOHAND) or (apply_number == EPointTypes.LG_POINT_RESIST_DAGGER) or (apply_number == EPointTypes.LG_POINT_RESIST_BELL) or (apply_number == EPointTypes.LG_POINT_RESIST_FAN) or (apply_number == EPointTypes.LG_POINT_RESIST_BOW) or (apply_number == EPointTypes.LG_POINT_RESIST_CLAW) or (apply_number == EPointTypes.LG_POINT_RESIST_FIRE) or (apply_number == EPointTypes.LG_POINT_RESIST_ELEC) or (apply_number == EPointTypes.LG_POINT_RESIST_MAGIC) or (apply_number == EPointTypes.LG_POINT_RESIST_WIND) or (apply_number == EPointTypes.LG_POINT_RESIST_ICE) or (apply_number == EPointTypes.LG_POINT_RESIST_EARTH) or (apply_number == EPointTypes.LG_POINT_RESIST_DARK) or (apply_number == EPointTypes.LG_POINT_REFLECT_MELEE) or (apply_number == EPointTypes.LG_POINT_REFLECT_CURSE) or (apply_number == EPointTypes.LG_POINT_POISON_REDUCE) or (apply_number == EPointTypes.LG_POINT_BLEEDING_REDUCE) or (apply_number == EPointTypes.LG_POINT_KILL_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_EXP_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_GOLD_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_ITEM_DROP_BONUS) or (apply_number == EPointTypes.LG_POINT_POTION_BONUS) or (apply_number == EPointTypes.LG_POINT_KILL_HP_RECOVERY) or (apply_number == EPointTypes.LG_POINT_ATT_GRADE_BONUS) or (apply_number == EPointTypes.LG_POINT_DEF_GRADE_BONUS) or (apply_number == EPointTypes.LG_POINT_MAGIC_ATT_GRADE) or (apply_number == EPointTypes.LG_POINT_MAGIC_DEF_GRADE) or (apply_number == EPointTypes.LG_POINT_MAX_STAMINA) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_WARRIOR) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_ASSASSIN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_SHURA) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_MAGE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_WOLFMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MONSTER) or (apply_number == EPointTypes.LG_POINT_MALL_ATTBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_DEFBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_EXPBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_ITEMBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_GOLDBONUS) or (apply_number == EPointTypes.LG_POINT_MAX_HP_PCT) or (apply_number == EPointTypes.LG_POINT_MAX_SP_PCT) or (apply_number == EPointTypes.LG_POINT_LG_SKILL_DAMAGE_BONUS) or (apply_number == EPointTypes.LG_POINT_NORMAL_HIT_DAMAGE_BONUS) or (apply_number == EPointTypes.LG_POINT_LG_SKILL_DEFEND_BONUS) or (apply_number == EPointTypes.LG_POINT_NORMAL_HIT_DEFEND_BONUS) or (apply_number == EPointTypes.LG_POINT_RESIST_LG_PAWN_WARRIOR) or (apply_number == EPointTypes.LG_POINT_RESIST_LG_PAWN_ASSASSIN) or (apply_number == EPointTypes.LG_POINT_RESIST_LG_PAWN_SHURA):
            return LC_TEXT("%d%% Resistance against LG_PAWN_SHURA Attacks")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_CRITICAL) or (apply_number == EPointTypes.LG_POINT_PENETRATE_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_PENETRATE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_HUMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ANIMAL) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ORC) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MILGYO) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_UNDEAD) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_DEVIL) or (apply_number == EPointTypes.LG_POINT_STEAL_HP) or (apply_number == EPointTypes.LG_POINT_STEAL_SP) or (apply_number == EPointTypes.LG_POINT_MANA_BURN_PCT) or (apply_number == EPointTypes.LG_POINT_DAMAGE_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_BLOCK) or (apply_number == EPointTypes.LG_POINT_DODGE) or (apply_number == EPointTypes.LG_POINT_RESIST_SWORD) or (apply_number == EPointTypes.LG_POINT_RESIST_TWOHAND) or (apply_number == EPointTypes.LG_POINT_RESIST_DAGGER) or (apply_number == EPointTypes.LG_POINT_RESIST_BELL) or (apply_number == EPointTypes.LG_POINT_RESIST_FAN) or (apply_number == EPointTypes.LG_POINT_RESIST_BOW) or (apply_number == EPointTypes.LG_POINT_RESIST_CLAW) or (apply_number == EPointTypes.LG_POINT_RESIST_FIRE) or (apply_number == EPointTypes.LG_POINT_RESIST_ELEC) or (apply_number == EPointTypes.LG_POINT_RESIST_MAGIC) or (apply_number == EPointTypes.LG_POINT_RESIST_WIND) or (apply_number == EPointTypes.LG_POINT_RESIST_ICE) or (apply_number == EPointTypes.LG_POINT_RESIST_EARTH) or (apply_number == EPointTypes.LG_POINT_RESIST_DARK) or (apply_number == EPointTypes.LG_POINT_REFLECT_MELEE) or (apply_number == EPointTypes.LG_POINT_REFLECT_CURSE) or (apply_number == EPointTypes.LG_POINT_POISON_REDUCE) or (apply_number == EPointTypes.LG_POINT_BLEEDING_REDUCE) or (apply_number == EPointTypes.LG_POINT_KILL_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_EXP_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_GOLD_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_ITEM_DROP_BONUS) or (apply_number == EPointTypes.LG_POINT_POTION_BONUS) or (apply_number == EPointTypes.LG_POINT_KILL_HP_RECOVERY) or (apply_number == EPointTypes.LG_POINT_ATT_GRADE_BONUS) or (apply_number == EPointTypes.LG_POINT_DEF_GRADE_BONUS) or (apply_number == EPointTypes.LG_POINT_MAGIC_ATT_GRADE) or (apply_number == EPointTypes.LG_POINT_MAGIC_DEF_GRADE) or (apply_number == EPointTypes.LG_POINT_MAX_STAMINA) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_WARRIOR) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_ASSASSIN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_SHURA) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_MAGE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_WOLFMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MONSTER) or (apply_number == EPointTypes.LG_POINT_MALL_ATTBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_DEFBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_EXPBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_ITEMBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_GOLDBONUS) or (apply_number == EPointTypes.LG_POINT_MAX_HP_PCT) or (apply_number == EPointTypes.LG_POINT_MAX_SP_PCT) or (apply_number == EPointTypes.LG_POINT_LG_SKILL_DAMAGE_BONUS) or (apply_number == EPointTypes.LG_POINT_NORMAL_HIT_DAMAGE_BONUS) or (apply_number == EPointTypes.LG_POINT_LG_SKILL_DEFEND_BONUS) or (apply_number == EPointTypes.LG_POINT_NORMAL_HIT_DEFEND_BONUS) or (apply_number == EPointTypes.LG_POINT_RESIST_LG_PAWN_WARRIOR) or (apply_number == EPointTypes.LG_POINT_RESIST_LG_PAWN_ASSASSIN) or (apply_number == EPointTypes.LG_POINT_RESIST_LG_PAWN_SHURA) or (apply_number == EPointTypes.LG_POINT_RESIST_LG_PAWN_MAGE):
            return LC_TEXT("%d%% Resistance against Mage Attacks")
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##if ENABLE_WOLFMAN
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_CRITICAL) or (apply_number == EPointTypes.LG_POINT_PENETRATE_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_PENETRATE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_HUMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ANIMAL) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ORC) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MILGYO) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_UNDEAD) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_DEVIL) or (apply_number == EPointTypes.LG_POINT_STEAL_HP) or (apply_number == EPointTypes.LG_POINT_STEAL_SP) or (apply_number == EPointTypes.LG_POINT_MANA_BURN_PCT) or (apply_number == EPointTypes.LG_POINT_DAMAGE_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_BLOCK) or (apply_number == EPointTypes.LG_POINT_DODGE) or (apply_number == EPointTypes.LG_POINT_RESIST_SWORD) or (apply_number == EPointTypes.LG_POINT_RESIST_TWOHAND) or (apply_number == EPointTypes.LG_POINT_RESIST_DAGGER) or (apply_number == EPointTypes.LG_POINT_RESIST_BELL) or (apply_number == EPointTypes.LG_POINT_RESIST_FAN) or (apply_number == EPointTypes.LG_POINT_RESIST_BOW) or (apply_number == EPointTypes.LG_POINT_RESIST_CLAW) or (apply_number == EPointTypes.LG_POINT_RESIST_FIRE) or (apply_number == EPointTypes.LG_POINT_RESIST_ELEC) or (apply_number == EPointTypes.LG_POINT_RESIST_MAGIC) or (apply_number == EPointTypes.LG_POINT_RESIST_WIND) or (apply_number == EPointTypes.LG_POINT_RESIST_ICE) or (apply_number == EPointTypes.LG_POINT_RESIST_EARTH) or (apply_number == EPointTypes.LG_POINT_RESIST_DARK) or (apply_number == EPointTypes.LG_POINT_REFLECT_MELEE) or (apply_number == EPointTypes.LG_POINT_REFLECT_CURSE) or (apply_number == EPointTypes.LG_POINT_POISON_REDUCE) or (apply_number == EPointTypes.LG_POINT_BLEEDING_REDUCE) or (apply_number == EPointTypes.LG_POINT_KILL_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_EXP_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_GOLD_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_ITEM_DROP_BONUS) or (apply_number == EPointTypes.LG_POINT_POTION_BONUS) or (apply_number == EPointTypes.LG_POINT_KILL_HP_RECOVERY) or (apply_number == EPointTypes.LG_POINT_ATT_GRADE_BONUS) or (apply_number == EPointTypes.LG_POINT_DEF_GRADE_BONUS) or (apply_number == EPointTypes.LG_POINT_MAGIC_ATT_GRADE) or (apply_number == EPointTypes.LG_POINT_MAGIC_DEF_GRADE) or (apply_number == EPointTypes.LG_POINT_MAX_STAMINA) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_WARRIOR) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_ASSASSIN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_SHURA) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_MAGE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_WOLFMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MONSTER) or (apply_number == EPointTypes.LG_POINT_MALL_ATTBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_DEFBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_EXPBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_ITEMBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_GOLDBONUS) or (apply_number == EPointTypes.LG_POINT_MAX_HP_PCT) or (apply_number == EPointTypes.LG_POINT_MAX_SP_PCT) or (apply_number == EPointTypes.LG_POINT_LG_SKILL_DAMAGE_BONUS) or (apply_number == EPointTypes.LG_POINT_NORMAL_HIT_DAMAGE_BONUS) or (apply_number == EPointTypes.LG_POINT_LG_SKILL_DEFEND_BONUS) or (apply_number == EPointTypes.LG_POINT_NORMAL_HIT_DEFEND_BONUS) or (apply_number == EPointTypes.LG_POINT_RESIST_LG_PAWN_WARRIOR) or (apply_number == EPointTypes.LG_POINT_RESIST_LG_PAWN_ASSASSIN) or (apply_number == EPointTypes.LG_POINT_RESIST_LG_PAWN_SHURA) or (apply_number == EPointTypes.LG_POINT_RESIST_LG_PAWN_MAGE) or (apply_number == EPointTypes.LG_POINT_RESIST_WOLFMAN):
            return LC_TEXT("%d%% Resistance against Mage Attacks")
    ##endif
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_CRITICAL) or (apply_number == EPointTypes.LG_POINT_PENETRATE_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_PENETRATE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_HUMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ANIMAL) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ORC) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MILGYO) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_UNDEAD) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_DEVIL) or (apply_number == EPointTypes.LG_POINT_STEAL_HP) or (apply_number == EPointTypes.LG_POINT_STEAL_SP) or (apply_number == EPointTypes.LG_POINT_MANA_BURN_PCT) or (apply_number == EPointTypes.LG_POINT_DAMAGE_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_BLOCK) or (apply_number == EPointTypes.LG_POINT_DODGE) or (apply_number == EPointTypes.LG_POINT_RESIST_SWORD) or (apply_number == EPointTypes.LG_POINT_RESIST_TWOHAND) or (apply_number == EPointTypes.LG_POINT_RESIST_DAGGER) or (apply_number == EPointTypes.LG_POINT_RESIST_BELL) or (apply_number == EPointTypes.LG_POINT_RESIST_FAN) or (apply_number == EPointTypes.LG_POINT_RESIST_BOW) or (apply_number == EPointTypes.LG_POINT_RESIST_CLAW) or (apply_number == EPointTypes.LG_POINT_RESIST_FIRE) or (apply_number == EPointTypes.LG_POINT_RESIST_ELEC) or (apply_number == EPointTypes.LG_POINT_RESIST_MAGIC) or (apply_number == EPointTypes.LG_POINT_RESIST_WIND) or (apply_number == EPointTypes.LG_POINT_RESIST_ICE) or (apply_number == EPointTypes.LG_POINT_RESIST_EARTH) or (apply_number == EPointTypes.LG_POINT_RESIST_DARK) or (apply_number == EPointTypes.LG_POINT_REFLECT_MELEE) or (apply_number == EPointTypes.LG_POINT_REFLECT_CURSE) or (apply_number == EPointTypes.LG_POINT_POISON_REDUCE) or (apply_number == EPointTypes.LG_POINT_BLEEDING_REDUCE) or (apply_number == EPointTypes.LG_POINT_KILL_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_EXP_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_GOLD_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_ITEM_DROP_BONUS) or (apply_number == EPointTypes.LG_POINT_POTION_BONUS) or (apply_number == EPointTypes.LG_POINT_KILL_HP_RECOVERY) or (apply_number == EPointTypes.LG_POINT_ATT_GRADE_BONUS) or (apply_number == EPointTypes.LG_POINT_DEF_GRADE_BONUS) or (apply_number == EPointTypes.LG_POINT_MAGIC_ATT_GRADE) or (apply_number == EPointTypes.LG_POINT_MAGIC_DEF_GRADE) or (apply_number == EPointTypes.LG_POINT_MAX_STAMINA) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_WARRIOR) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_ASSASSIN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_SHURA) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_MAGE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_WOLFMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MONSTER) or (apply_number == EPointTypes.LG_POINT_MALL_ATTBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_DEFBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_EXPBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_ITEMBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_GOLDBONUS) or (apply_number == EPointTypes.LG_POINT_MAX_HP_PCT) or (apply_number == EPointTypes.LG_POINT_MAX_SP_PCT) or (apply_number == EPointTypes.LG_POINT_LG_SKILL_DAMAGE_BONUS) or (apply_number == EPointTypes.LG_POINT_NORMAL_HIT_DAMAGE_BONUS) or (apply_number == EPointTypes.LG_POINT_LG_SKILL_DEFEND_BONUS) or (apply_number == EPointTypes.LG_POINT_NORMAL_HIT_DEFEND_BONUS) or (apply_number == EPointTypes.LG_POINT_RESIST_LG_PAWN_WARRIOR) or (apply_number == EPointTypes.LG_POINT_RESIST_LG_PAWN_ASSASSIN) or (apply_number == EPointTypes.LG_POINT_RESIST_LG_PAWN_SHURA) or (apply_number == EPointTypes.LG_POINT_RESIST_LG_PAWN_MAGE) or (apply_number == EPointTypes.LG_POINT_RESIST_WOLFMAN) or (apply_number == EPointTypes.LG_POINT_RESIST_MAGIC_REDUCTION):
            return LC_TEXT("Anti Magic Resistance: %d%%")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_CRITICAL) or (apply_number == EPointTypes.LG_POINT_PENETRATE_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_PENETRATE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_HUMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ANIMAL) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ORC) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MILGYO) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_UNDEAD) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_DEVIL) or (apply_number == EPointTypes.LG_POINT_STEAL_HP) or (apply_number == EPointTypes.LG_POINT_STEAL_SP) or (apply_number == EPointTypes.LG_POINT_MANA_BURN_PCT) or (apply_number == EPointTypes.LG_POINT_DAMAGE_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_BLOCK) or (apply_number == EPointTypes.LG_POINT_DODGE) or (apply_number == EPointTypes.LG_POINT_RESIST_SWORD) or (apply_number == EPointTypes.LG_POINT_RESIST_TWOHAND) or (apply_number == EPointTypes.LG_POINT_RESIST_DAGGER) or (apply_number == EPointTypes.LG_POINT_RESIST_BELL) or (apply_number == EPointTypes.LG_POINT_RESIST_FAN) or (apply_number == EPointTypes.LG_POINT_RESIST_BOW) or (apply_number == EPointTypes.LG_POINT_RESIST_CLAW) or (apply_number == EPointTypes.LG_POINT_RESIST_FIRE) or (apply_number == EPointTypes.LG_POINT_RESIST_ELEC) or (apply_number == EPointTypes.LG_POINT_RESIST_MAGIC) or (apply_number == EPointTypes.LG_POINT_RESIST_WIND) or (apply_number == EPointTypes.LG_POINT_RESIST_ICE) or (apply_number == EPointTypes.LG_POINT_RESIST_EARTH) or (apply_number == EPointTypes.LG_POINT_RESIST_DARK) or (apply_number == EPointTypes.LG_POINT_REFLECT_MELEE) or (apply_number == EPointTypes.LG_POINT_REFLECT_CURSE) or (apply_number == EPointTypes.LG_POINT_POISON_REDUCE) or (apply_number == EPointTypes.LG_POINT_BLEEDING_REDUCE) or (apply_number == EPointTypes.LG_POINT_KILL_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_EXP_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_GOLD_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_ITEM_DROP_BONUS) or (apply_number == EPointTypes.LG_POINT_POTION_BONUS) or (apply_number == EPointTypes.LG_POINT_KILL_HP_RECOVERY) or (apply_number == EPointTypes.LG_POINT_ATT_GRADE_BONUS) or (apply_number == EPointTypes.LG_POINT_DEF_GRADE_BONUS) or (apply_number == EPointTypes.LG_POINT_MAGIC_ATT_GRADE) or (apply_number == EPointTypes.LG_POINT_MAGIC_DEF_GRADE) or (apply_number == EPointTypes.LG_POINT_MAX_STAMINA) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_WARRIOR) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_ASSASSIN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_SHURA) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_MAGE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_WOLFMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MONSTER) or (apply_number == EPointTypes.LG_POINT_MALL_ATTBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_DEFBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_EXPBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_ITEMBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_GOLDBONUS) or (apply_number == EPointTypes.LG_POINT_MAX_HP_PCT) or (apply_number == EPointTypes.LG_POINT_MAX_SP_PCT) or (apply_number == EPointTypes.LG_POINT_LG_SKILL_DAMAGE_BONUS) or (apply_number == EPointTypes.LG_POINT_NORMAL_HIT_DAMAGE_BONUS) or (apply_number == EPointTypes.LG_POINT_LG_SKILL_DEFEND_BONUS) or (apply_number == EPointTypes.LG_POINT_NORMAL_HIT_DEFEND_BONUS) or (apply_number == EPointTypes.LG_POINT_RESIST_LG_PAWN_WARRIOR) or (apply_number == EPointTypes.LG_POINT_RESIST_LG_PAWN_ASSASSIN) or (apply_number == EPointTypes.LG_POINT_RESIST_LG_PAWN_SHURA) or (apply_number == EPointTypes.LG_POINT_RESIST_LG_PAWN_MAGE) or (apply_number == EPointTypes.LG_POINT_RESIST_WOLFMAN) or (apply_number == EPointTypes.LG_POINT_RESIST_MAGIC_REDUCTION) or (apply_number == EPointTypes.LG_POINT_RESIST_HUMAN):
            return LC_TEXT("Resist Half Human %d%%")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_CRITICAL) or (apply_number == EPointTypes.LG_POINT_PENETRATE_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_PENETRATE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_HUMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ANIMAL) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ORC) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MILGYO) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_UNDEAD) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_DEVIL) or (apply_number == EPointTypes.LG_POINT_STEAL_HP) or (apply_number == EPointTypes.LG_POINT_STEAL_SP) or (apply_number == EPointTypes.LG_POINT_MANA_BURN_PCT) or (apply_number == EPointTypes.LG_POINT_DAMAGE_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_BLOCK) or (apply_number == EPointTypes.LG_POINT_DODGE) or (apply_number == EPointTypes.LG_POINT_RESIST_SWORD) or (apply_number == EPointTypes.LG_POINT_RESIST_TWOHAND) or (apply_number == EPointTypes.LG_POINT_RESIST_DAGGER) or (apply_number == EPointTypes.LG_POINT_RESIST_BELL) or (apply_number == EPointTypes.LG_POINT_RESIST_FAN) or (apply_number == EPointTypes.LG_POINT_RESIST_BOW) or (apply_number == EPointTypes.LG_POINT_RESIST_CLAW) or (apply_number == EPointTypes.LG_POINT_RESIST_FIRE) or (apply_number == EPointTypes.LG_POINT_RESIST_ELEC) or (apply_number == EPointTypes.LG_POINT_RESIST_MAGIC) or (apply_number == EPointTypes.LG_POINT_RESIST_WIND) or (apply_number == EPointTypes.LG_POINT_RESIST_ICE) or (apply_number == EPointTypes.LG_POINT_RESIST_EARTH) or (apply_number == EPointTypes.LG_POINT_RESIST_DARK) or (apply_number == EPointTypes.LG_POINT_REFLECT_MELEE) or (apply_number == EPointTypes.LG_POINT_REFLECT_CURSE) or (apply_number == EPointTypes.LG_POINT_POISON_REDUCE) or (apply_number == EPointTypes.LG_POINT_BLEEDING_REDUCE) or (apply_number == EPointTypes.LG_POINT_KILL_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_EXP_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_GOLD_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_ITEM_DROP_BONUS) or (apply_number == EPointTypes.LG_POINT_POTION_BONUS) or (apply_number == EPointTypes.LG_POINT_KILL_HP_RECOVERY) or (apply_number == EPointTypes.LG_POINT_ATT_GRADE_BONUS) or (apply_number == EPointTypes.LG_POINT_DEF_GRADE_BONUS) or (apply_number == EPointTypes.LG_POINT_MAGIC_ATT_GRADE) or (apply_number == EPointTypes.LG_POINT_MAGIC_DEF_GRADE) or (apply_number == EPointTypes.LG_POINT_MAX_STAMINA) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_WARRIOR) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_ASSASSIN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_SHURA) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_MAGE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_WOLFMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MONSTER) or (apply_number == EPointTypes.LG_POINT_MALL_ATTBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_DEFBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_EXPBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_ITEMBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_GOLDBONUS) or (apply_number == EPointTypes.LG_POINT_MAX_HP_PCT) or (apply_number == EPointTypes.LG_POINT_MAX_SP_PCT) or (apply_number == EPointTypes.LG_POINT_LG_SKILL_DAMAGE_BONUS) or (apply_number == EPointTypes.LG_POINT_NORMAL_HIT_DAMAGE_BONUS) or (apply_number == EPointTypes.LG_POINT_LG_SKILL_DEFEND_BONUS) or (apply_number == EPointTypes.LG_POINT_NORMAL_HIT_DEFEND_BONUS) or (apply_number == EPointTypes.LG_POINT_RESIST_LG_PAWN_WARRIOR) or (apply_number == EPointTypes.LG_POINT_RESIST_LG_PAWN_ASSASSIN) or (apply_number == EPointTypes.LG_POINT_RESIST_LG_PAWN_SHURA) or (apply_number == EPointTypes.LG_POINT_RESIST_LG_PAWN_MAGE) or (apply_number == EPointTypes.LG_POINT_RESIST_WOLFMAN) or (apply_number == EPointTypes.LG_POINT_RESIST_MAGIC_REDUCTION) or (apply_number == EPointTypes.LG_POINT_RESIST_HUMAN) or (apply_number == EPointTypes.LG_POINT_ENCHANT_ELEC):
            return LC_TEXT("ELEC POWER: %d%%")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_CRITICAL) or (apply_number == EPointTypes.LG_POINT_PENETRATE_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_PENETRATE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_HUMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ANIMAL) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ORC) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MILGYO) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_UNDEAD) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_DEVIL) or (apply_number == EPointTypes.LG_POINT_STEAL_HP) or (apply_number == EPointTypes.LG_POINT_STEAL_SP) or (apply_number == EPointTypes.LG_POINT_MANA_BURN_PCT) or (apply_number == EPointTypes.LG_POINT_DAMAGE_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_BLOCK) or (apply_number == EPointTypes.LG_POINT_DODGE) or (apply_number == EPointTypes.LG_POINT_RESIST_SWORD) or (apply_number == EPointTypes.LG_POINT_RESIST_TWOHAND) or (apply_number == EPointTypes.LG_POINT_RESIST_DAGGER) or (apply_number == EPointTypes.LG_POINT_RESIST_BELL) or (apply_number == EPointTypes.LG_POINT_RESIST_FAN) or (apply_number == EPointTypes.LG_POINT_RESIST_BOW) or (apply_number == EPointTypes.LG_POINT_RESIST_CLAW) or (apply_number == EPointTypes.LG_POINT_RESIST_FIRE) or (apply_number == EPointTypes.LG_POINT_RESIST_ELEC) or (apply_number == EPointTypes.LG_POINT_RESIST_MAGIC) or (apply_number == EPointTypes.LG_POINT_RESIST_WIND) or (apply_number == EPointTypes.LG_POINT_RESIST_ICE) or (apply_number == EPointTypes.LG_POINT_RESIST_EARTH) or (apply_number == EPointTypes.LG_POINT_RESIST_DARK) or (apply_number == EPointTypes.LG_POINT_REFLECT_MELEE) or (apply_number == EPointTypes.LG_POINT_REFLECT_CURSE) or (apply_number == EPointTypes.LG_POINT_POISON_REDUCE) or (apply_number == EPointTypes.LG_POINT_BLEEDING_REDUCE) or (apply_number == EPointTypes.LG_POINT_KILL_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_EXP_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_GOLD_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_ITEM_DROP_BONUS) or (apply_number == EPointTypes.LG_POINT_POTION_BONUS) or (apply_number == EPointTypes.LG_POINT_KILL_HP_RECOVERY) or (apply_number == EPointTypes.LG_POINT_ATT_GRADE_BONUS) or (apply_number == EPointTypes.LG_POINT_DEF_GRADE_BONUS) or (apply_number == EPointTypes.LG_POINT_MAGIC_ATT_GRADE) or (apply_number == EPointTypes.LG_POINT_MAGIC_DEF_GRADE) or (apply_number == EPointTypes.LG_POINT_MAX_STAMINA) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_WARRIOR) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_ASSASSIN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_SHURA) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_MAGE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_WOLFMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MONSTER) or (apply_number == EPointTypes.LG_POINT_MALL_ATTBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_DEFBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_EXPBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_ITEMBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_GOLDBONUS) or (apply_number == EPointTypes.LG_POINT_MAX_HP_PCT) or (apply_number == EPointTypes.LG_POINT_MAX_SP_PCT) or (apply_number == EPointTypes.LG_POINT_LG_SKILL_DAMAGE_BONUS) or (apply_number == EPointTypes.LG_POINT_NORMAL_HIT_DAMAGE_BONUS) or (apply_number == EPointTypes.LG_POINT_LG_SKILL_DEFEND_BONUS) or (apply_number == EPointTypes.LG_POINT_NORMAL_HIT_DEFEND_BONUS) or (apply_number == EPointTypes.LG_POINT_RESIST_LG_PAWN_WARRIOR) or (apply_number == EPointTypes.LG_POINT_RESIST_LG_PAWN_ASSASSIN) or (apply_number == EPointTypes.LG_POINT_RESIST_LG_PAWN_SHURA) or (apply_number == EPointTypes.LG_POINT_RESIST_LG_PAWN_MAGE) or (apply_number == EPointTypes.LG_POINT_RESIST_WOLFMAN) or (apply_number == EPointTypes.LG_POINT_RESIST_MAGIC_REDUCTION) or (apply_number == EPointTypes.LG_POINT_RESIST_HUMAN) or (apply_number == EPointTypes.LG_POINT_ENCHANT_ELEC) or (apply_number == EPointTypes.LG_POINT_ENCHANT_FIRE):
            return LC_TEXT("FIRE POWER: %d%%")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_CRITICAL) or (apply_number == EPointTypes.LG_POINT_PENETRATE_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_PENETRATE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_HUMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ANIMAL) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ORC) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MILGYO) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_UNDEAD) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_DEVIL) or (apply_number == EPointTypes.LG_POINT_STEAL_HP) or (apply_number == EPointTypes.LG_POINT_STEAL_SP) or (apply_number == EPointTypes.LG_POINT_MANA_BURN_PCT) or (apply_number == EPointTypes.LG_POINT_DAMAGE_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_BLOCK) or (apply_number == EPointTypes.LG_POINT_DODGE) or (apply_number == EPointTypes.LG_POINT_RESIST_SWORD) or (apply_number == EPointTypes.LG_POINT_RESIST_TWOHAND) or (apply_number == EPointTypes.LG_POINT_RESIST_DAGGER) or (apply_number == EPointTypes.LG_POINT_RESIST_BELL) or (apply_number == EPointTypes.LG_POINT_RESIST_FAN) or (apply_number == EPointTypes.LG_POINT_RESIST_BOW) or (apply_number == EPointTypes.LG_POINT_RESIST_CLAW) or (apply_number == EPointTypes.LG_POINT_RESIST_FIRE) or (apply_number == EPointTypes.LG_POINT_RESIST_ELEC) or (apply_number == EPointTypes.LG_POINT_RESIST_MAGIC) or (apply_number == EPointTypes.LG_POINT_RESIST_WIND) or (apply_number == EPointTypes.LG_POINT_RESIST_ICE) or (apply_number == EPointTypes.LG_POINT_RESIST_EARTH) or (apply_number == EPointTypes.LG_POINT_RESIST_DARK) or (apply_number == EPointTypes.LG_POINT_REFLECT_MELEE) or (apply_number == EPointTypes.LG_POINT_REFLECT_CURSE) or (apply_number == EPointTypes.LG_POINT_POISON_REDUCE) or (apply_number == EPointTypes.LG_POINT_BLEEDING_REDUCE) or (apply_number == EPointTypes.LG_POINT_KILL_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_EXP_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_GOLD_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_ITEM_DROP_BONUS) or (apply_number == EPointTypes.LG_POINT_POTION_BONUS) or (apply_number == EPointTypes.LG_POINT_KILL_HP_RECOVERY) or (apply_number == EPointTypes.LG_POINT_ATT_GRADE_BONUS) or (apply_number == EPointTypes.LG_POINT_DEF_GRADE_BONUS) or (apply_number == EPointTypes.LG_POINT_MAGIC_ATT_GRADE) or (apply_number == EPointTypes.LG_POINT_MAGIC_DEF_GRADE) or (apply_number == EPointTypes.LG_POINT_MAX_STAMINA) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_WARRIOR) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_ASSASSIN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_SHURA) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_MAGE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_WOLFMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MONSTER) or (apply_number == EPointTypes.LG_POINT_MALL_ATTBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_DEFBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_EXPBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_ITEMBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_GOLDBONUS) or (apply_number == EPointTypes.LG_POINT_MAX_HP_PCT) or (apply_number == EPointTypes.LG_POINT_MAX_SP_PCT) or (apply_number == EPointTypes.LG_POINT_LG_SKILL_DAMAGE_BONUS) or (apply_number == EPointTypes.LG_POINT_NORMAL_HIT_DAMAGE_BONUS) or (apply_number == EPointTypes.LG_POINT_LG_SKILL_DEFEND_BONUS) or (apply_number == EPointTypes.LG_POINT_NORMAL_HIT_DEFEND_BONUS) or (apply_number == EPointTypes.LG_POINT_RESIST_LG_PAWN_WARRIOR) or (apply_number == EPointTypes.LG_POINT_RESIST_LG_PAWN_ASSASSIN) or (apply_number == EPointTypes.LG_POINT_RESIST_LG_PAWN_SHURA) or (apply_number == EPointTypes.LG_POINT_RESIST_LG_PAWN_MAGE) or (apply_number == EPointTypes.LG_POINT_RESIST_WOLFMAN) or (apply_number == EPointTypes.LG_POINT_RESIST_MAGIC_REDUCTION) or (apply_number == EPointTypes.LG_POINT_RESIST_HUMAN) or (apply_number == EPointTypes.LG_POINT_ENCHANT_ELEC) or (apply_number == EPointTypes.LG_POINT_ENCHANT_FIRE) or (apply_number == EPointTypes.LG_POINT_ENCHANT_ICE):
            return LC_TEXT("ICE POWER: %d%%")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_CRITICAL) or (apply_number == EPointTypes.LG_POINT_PENETRATE_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_PENETRATE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_HUMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ANIMAL) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ORC) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MILGYO) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_UNDEAD) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_DEVIL) or (apply_number == EPointTypes.LG_POINT_STEAL_HP) or (apply_number == EPointTypes.LG_POINT_STEAL_SP) or (apply_number == EPointTypes.LG_POINT_MANA_BURN_PCT) or (apply_number == EPointTypes.LG_POINT_DAMAGE_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_BLOCK) or (apply_number == EPointTypes.LG_POINT_DODGE) or (apply_number == EPointTypes.LG_POINT_RESIST_SWORD) or (apply_number == EPointTypes.LG_POINT_RESIST_TWOHAND) or (apply_number == EPointTypes.LG_POINT_RESIST_DAGGER) or (apply_number == EPointTypes.LG_POINT_RESIST_BELL) or (apply_number == EPointTypes.LG_POINT_RESIST_FAN) or (apply_number == EPointTypes.LG_POINT_RESIST_BOW) or (apply_number == EPointTypes.LG_POINT_RESIST_CLAW) or (apply_number == EPointTypes.LG_POINT_RESIST_FIRE) or (apply_number == EPointTypes.LG_POINT_RESIST_ELEC) or (apply_number == EPointTypes.LG_POINT_RESIST_MAGIC) or (apply_number == EPointTypes.LG_POINT_RESIST_WIND) or (apply_number == EPointTypes.LG_POINT_RESIST_ICE) or (apply_number == EPointTypes.LG_POINT_RESIST_EARTH) or (apply_number == EPointTypes.LG_POINT_RESIST_DARK) or (apply_number == EPointTypes.LG_POINT_REFLECT_MELEE) or (apply_number == EPointTypes.LG_POINT_REFLECT_CURSE) or (apply_number == EPointTypes.LG_POINT_POISON_REDUCE) or (apply_number == EPointTypes.LG_POINT_BLEEDING_REDUCE) or (apply_number == EPointTypes.LG_POINT_KILL_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_EXP_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_GOLD_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_ITEM_DROP_BONUS) or (apply_number == EPointTypes.LG_POINT_POTION_BONUS) or (apply_number == EPointTypes.LG_POINT_KILL_HP_RECOVERY) or (apply_number == EPointTypes.LG_POINT_ATT_GRADE_BONUS) or (apply_number == EPointTypes.LG_POINT_DEF_GRADE_BONUS) or (apply_number == EPointTypes.LG_POINT_MAGIC_ATT_GRADE) or (apply_number == EPointTypes.LG_POINT_MAGIC_DEF_GRADE) or (apply_number == EPointTypes.LG_POINT_MAX_STAMINA) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_WARRIOR) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_ASSASSIN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_SHURA) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_MAGE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_WOLFMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MONSTER) or (apply_number == EPointTypes.LG_POINT_MALL_ATTBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_DEFBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_EXPBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_ITEMBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_GOLDBONUS) or (apply_number == EPointTypes.LG_POINT_MAX_HP_PCT) or (apply_number == EPointTypes.LG_POINT_MAX_SP_PCT) or (apply_number == EPointTypes.LG_POINT_LG_SKILL_DAMAGE_BONUS) or (apply_number == EPointTypes.LG_POINT_NORMAL_HIT_DAMAGE_BONUS) or (apply_number == EPointTypes.LG_POINT_LG_SKILL_DEFEND_BONUS) or (apply_number == EPointTypes.LG_POINT_NORMAL_HIT_DEFEND_BONUS) or (apply_number == EPointTypes.LG_POINT_RESIST_LG_PAWN_WARRIOR) or (apply_number == EPointTypes.LG_POINT_RESIST_LG_PAWN_ASSASSIN) or (apply_number == EPointTypes.LG_POINT_RESIST_LG_PAWN_SHURA) or (apply_number == EPointTypes.LG_POINT_RESIST_LG_PAWN_MAGE) or (apply_number == EPointTypes.LG_POINT_RESIST_WOLFMAN) or (apply_number == EPointTypes.LG_POINT_RESIST_MAGIC_REDUCTION) or (apply_number == EPointTypes.LG_POINT_RESIST_HUMAN) or (apply_number == EPointTypes.LG_POINT_ENCHANT_ELEC) or (apply_number == EPointTypes.LG_POINT_ENCHANT_FIRE) or (apply_number == EPointTypes.LG_POINT_ENCHANT_ICE) or (apply_number == EPointTypes.LG_POINT_ENCHANT_WIND):
            return LC_TEXT("WIND POWER: %d%%")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_CRITICAL) or (apply_number == EPointTypes.LG_POINT_PENETRATE_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_PENETRATE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_HUMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ANIMAL) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ORC) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MILGYO) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_UNDEAD) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_DEVIL) or (apply_number == EPointTypes.LG_POINT_STEAL_HP) or (apply_number == EPointTypes.LG_POINT_STEAL_SP) or (apply_number == EPointTypes.LG_POINT_MANA_BURN_PCT) or (apply_number == EPointTypes.LG_POINT_DAMAGE_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_BLOCK) or (apply_number == EPointTypes.LG_POINT_DODGE) or (apply_number == EPointTypes.LG_POINT_RESIST_SWORD) or (apply_number == EPointTypes.LG_POINT_RESIST_TWOHAND) or (apply_number == EPointTypes.LG_POINT_RESIST_DAGGER) or (apply_number == EPointTypes.LG_POINT_RESIST_BELL) or (apply_number == EPointTypes.LG_POINT_RESIST_FAN) or (apply_number == EPointTypes.LG_POINT_RESIST_BOW) or (apply_number == EPointTypes.LG_POINT_RESIST_CLAW) or (apply_number == EPointTypes.LG_POINT_RESIST_FIRE) or (apply_number == EPointTypes.LG_POINT_RESIST_ELEC) or (apply_number == EPointTypes.LG_POINT_RESIST_MAGIC) or (apply_number == EPointTypes.LG_POINT_RESIST_WIND) or (apply_number == EPointTypes.LG_POINT_RESIST_ICE) or (apply_number == EPointTypes.LG_POINT_RESIST_EARTH) or (apply_number == EPointTypes.LG_POINT_RESIST_DARK) or (apply_number == EPointTypes.LG_POINT_REFLECT_MELEE) or (apply_number == EPointTypes.LG_POINT_REFLECT_CURSE) or (apply_number == EPointTypes.LG_POINT_POISON_REDUCE) or (apply_number == EPointTypes.LG_POINT_BLEEDING_REDUCE) or (apply_number == EPointTypes.LG_POINT_KILL_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_EXP_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_GOLD_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_ITEM_DROP_BONUS) or (apply_number == EPointTypes.LG_POINT_POTION_BONUS) or (apply_number == EPointTypes.LG_POINT_KILL_HP_RECOVERY) or (apply_number == EPointTypes.LG_POINT_ATT_GRADE_BONUS) or (apply_number == EPointTypes.LG_POINT_DEF_GRADE_BONUS) or (apply_number == EPointTypes.LG_POINT_MAGIC_ATT_GRADE) or (apply_number == EPointTypes.LG_POINT_MAGIC_DEF_GRADE) or (apply_number == EPointTypes.LG_POINT_MAX_STAMINA) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_WARRIOR) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_ASSASSIN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_SHURA) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_MAGE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_WOLFMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MONSTER) or (apply_number == EPointTypes.LG_POINT_MALL_ATTBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_DEFBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_EXPBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_ITEMBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_GOLDBONUS) or (apply_number == EPointTypes.LG_POINT_MAX_HP_PCT) or (apply_number == EPointTypes.LG_POINT_MAX_SP_PCT) or (apply_number == EPointTypes.LG_POINT_LG_SKILL_DAMAGE_BONUS) or (apply_number == EPointTypes.LG_POINT_NORMAL_HIT_DAMAGE_BONUS) or (apply_number == EPointTypes.LG_POINT_LG_SKILL_DEFEND_BONUS) or (apply_number == EPointTypes.LG_POINT_NORMAL_HIT_DEFEND_BONUS) or (apply_number == EPointTypes.LG_POINT_RESIST_LG_PAWN_WARRIOR) or (apply_number == EPointTypes.LG_POINT_RESIST_LG_PAWN_ASSASSIN) or (apply_number == EPointTypes.LG_POINT_RESIST_LG_PAWN_SHURA) or (apply_number == EPointTypes.LG_POINT_RESIST_LG_PAWN_MAGE) or (apply_number == EPointTypes.LG_POINT_RESIST_WOLFMAN) or (apply_number == EPointTypes.LG_POINT_RESIST_MAGIC_REDUCTION) or (apply_number == EPointTypes.LG_POINT_RESIST_HUMAN) or (apply_number == EPointTypes.LG_POINT_ENCHANT_ELEC) or (apply_number == EPointTypes.LG_POINT_ENCHANT_FIRE) or (apply_number == EPointTypes.LG_POINT_ENCHANT_ICE) or (apply_number == EPointTypes.LG_POINT_ENCHANT_WIND) or (apply_number == EPointTypes.LG_POINT_ENCHANT_EARTH):
            return LC_TEXT("EARTH POWER: %d%%")
        if (apply_number == EPointTypes.LG_POINT_MAX_HP) or (apply_number == EPointTypes.LG_POINT_MAX_SP) or (apply_number == EPointTypes.LG_POINT_HT) or (apply_number == EPointTypes.LG_POINT_IQ) or (apply_number == EPointTypes.LG_POINT_ST) or (apply_number == EPointTypes.LG_POINT_DX) or (apply_number == EPointTypes.LG_POINT_ATT_SPEED) or (apply_number == EPointTypes.LG_POINT_MOV_SPEED) or (apply_number == EPointTypes.LG_POINT_CASTING_SPEED) or (apply_number == EPointTypes.LG_POINT_HP_REGEN) or (apply_number == EPointTypes.LG_POINT_SP_REGEN) or (apply_number == EPointTypes.LG_POINT_POISON_PCT) or (apply_number == EPointTypes.LG_POINT_BLEEDING_PCT) or (apply_number == EPointTypes.LG_POINT_STUN_PCT) or (apply_number == EPointTypes.LG_POINT_SLOW_PCT) or (apply_number == EPointTypes.LG_POINT_CRITICAL_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_CRITICAL) or (apply_number == EPointTypes.LG_POINT_PENETRATE_PCT) or (apply_number == EPointTypes.LG_POINT_RESIST_PENETRATE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_HUMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ANIMAL) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_ORC) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MILGYO) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_UNDEAD) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_DEVIL) or (apply_number == EPointTypes.LG_POINT_STEAL_HP) or (apply_number == EPointTypes.LG_POINT_STEAL_SP) or (apply_number == EPointTypes.LG_POINT_MANA_BURN_PCT) or (apply_number == EPointTypes.LG_POINT_DAMAGE_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_BLOCK) or (apply_number == EPointTypes.LG_POINT_DODGE) or (apply_number == EPointTypes.LG_POINT_RESIST_SWORD) or (apply_number == EPointTypes.LG_POINT_RESIST_TWOHAND) or (apply_number == EPointTypes.LG_POINT_RESIST_DAGGER) or (apply_number == EPointTypes.LG_POINT_RESIST_BELL) or (apply_number == EPointTypes.LG_POINT_RESIST_FAN) or (apply_number == EPointTypes.LG_POINT_RESIST_BOW) or (apply_number == EPointTypes.LG_POINT_RESIST_CLAW) or (apply_number == EPointTypes.LG_POINT_RESIST_FIRE) or (apply_number == EPointTypes.LG_POINT_RESIST_ELEC) or (apply_number == EPointTypes.LG_POINT_RESIST_MAGIC) or (apply_number == EPointTypes.LG_POINT_RESIST_WIND) or (apply_number == EPointTypes.LG_POINT_RESIST_ICE) or (apply_number == EPointTypes.LG_POINT_RESIST_EARTH) or (apply_number == EPointTypes.LG_POINT_RESIST_DARK) or (apply_number == EPointTypes.LG_POINT_REFLECT_MELEE) or (apply_number == EPointTypes.LG_POINT_REFLECT_CURSE) or (apply_number == EPointTypes.LG_POINT_POISON_REDUCE) or (apply_number == EPointTypes.LG_POINT_BLEEDING_REDUCE) or (apply_number == EPointTypes.LG_POINT_KILL_SP_RECOVER) or (apply_number == EPointTypes.LG_POINT_EXP_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_GOLD_DOUBLE_BONUS) or (apply_number == EPointTypes.LG_POINT_ITEM_DROP_BONUS) or (apply_number == EPointTypes.LG_POINT_POTION_BONUS) or (apply_number == EPointTypes.LG_POINT_KILL_HP_RECOVERY) or (apply_number == EPointTypes.LG_POINT_ATT_GRADE_BONUS) or (apply_number == EPointTypes.LG_POINT_DEF_GRADE_BONUS) or (apply_number == EPointTypes.LG_POINT_MAGIC_ATT_GRADE) or (apply_number == EPointTypes.LG_POINT_MAGIC_DEF_GRADE) or (apply_number == EPointTypes.LG_POINT_MAX_STAMINA) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_WARRIOR) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_ASSASSIN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_SHURA) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_LG_PAWN_MAGE) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_WOLFMAN) or (apply_number == EPointTypes.LG_POINT_ATTBONUS_MONSTER) or (apply_number == EPointTypes.LG_POINT_MALL_ATTBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_DEFBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_EXPBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_ITEMBONUS) or (apply_number == EPointTypes.LG_POINT_MALL_GOLDBONUS) or (apply_number == EPointTypes.LG_POINT_MAX_HP_PCT) or (apply_number == EPointTypes.LG_POINT_MAX_SP_PCT) or (apply_number == EPointTypes.LG_POINT_LG_SKILL_DAMAGE_BONUS) or (apply_number == EPointTypes.LG_POINT_NORMAL_HIT_DAMAGE_BONUS) or (apply_number == EPointTypes.LG_POINT_LG_SKILL_DEFEND_BONUS) or (apply_number == EPointTypes.LG_POINT_NORMAL_HIT_DEFEND_BONUS) or (apply_number == EPointTypes.LG_POINT_RESIST_LG_PAWN_WARRIOR) or (apply_number == EPointTypes.LG_POINT_RESIST_LG_PAWN_ASSASSIN) or (apply_number == EPointTypes.LG_POINT_RESIST_LG_PAWN_SHURA) or (apply_number == EPointTypes.LG_POINT_RESIST_LG_PAWN_MAGE) or (apply_number == EPointTypes.LG_POINT_RESIST_WOLFMAN) or (apply_number == EPointTypes.LG_POINT_RESIST_MAGIC_REDUCTION) or (apply_number == EPointTypes.LG_POINT_RESIST_HUMAN) or (apply_number == EPointTypes.LG_POINT_ENCHANT_ELEC) or (apply_number == EPointTypes.LG_POINT_ENCHANT_FIRE) or (apply_number == EPointTypes.LG_POINT_ENCHANT_ICE) or (apply_number == EPointTypes.LG_POINT_ENCHANT_WIND) or (apply_number == EPointTypes.LG_POINT_ENCHANT_EARTH) or (apply_number == EPointTypes.LG_POINT_ENCHANT_DARK):
            return LC_TEXT("DARK POWER: %d%%")

        if True:
            return None

    @staticmethod
    def FN_hair_affect_string(ch, buf, bufsiz):
        if None is ch or None == buf.arg_value:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        aff = None
        expire = 0
        ltm = tm()
        year = None
        mon = None
        day = None
        offset = 0

        aff = ch.FindAffect(LaniatusEAffectTypes.LANIA_AFFECT_HAIR, APPLY_NONE)

        if None is aff:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        expire = ch.GetQuestFlag("hair.limit_time")

        if expire < Globals.get_global_time():
            return LGEMiscellaneous.DEFINECONSTANTS.false

        offset = snprintf(buf.arg_value, bufsiz, Globals.FN_LG_POINT_string(aff.bApplyOn), aff.lApplyValue)

        if offset < 0 or offset >= int(bufsiz):
            offset = bufsiz - 1

        localtime_s(ltm, expire)

        year = ltm.tm_year + 1900
        mon = ltm.tm_mon + 1
        day = ltm.tm_mday

        snprintf(buf.arg_value[offset:], bufsiz - offset, LC_TEXT("(Procedure: %d y- %d m - %d d)"), year, mon, day)

        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    @staticmethod
    def (UnnamedParameter):
        index = 0
        count = 1

        arg1 = str(['\0' for _ in range(256)])
        arg2 = str(['\0' for _ in range(256)])

        item = None

        temp_ref_arg1 = RefObject(arg1);
        temp_ref_arg2 = RefObject(arg2);
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        Globals.two_arguments(argument, temp_ref_arg1, sizeof(arg1), temp_ref_arg2, sizeof(arg2))
        arg2 = temp_ref_arg2.arg_value
        arg1 = temp_ref_arg1.arg_value

        if (not arg1[0]) != '\0':
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, "Usage: inventory <start_index> <count>")
            return

        if (not arg2[0]) != '\0':
            index = 0
            temp_ref_count = RefObject(count);
            Globals.str_to_number(temp_ref_count, arg1)
            count = temp_ref_count.arg_value
        else:
            temp_ref_index = RefObject(index);
            Globals.str_to_number(temp_ref_index, arg1)
            index = temp_ref_index.arg_value
            index = MIN(index, LGEMiscellaneous.INVENTORY_MAX_NUM)
            temp_ref_count2 = RefObject(count);
            Globals.str_to_number(temp_ref_count2, arg2)
            count = temp_ref_count2.arg_value
            count = MIN(count, LGEMiscellaneous.INVENTORY_MAX_NUM)

        for i in range(0, count):
            if index >= LGEMiscellaneous.INVENTORY_MAX_NUM:
                break

            item = ch.GetInventoryItem(index)

            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, "inventory [%d] = %s", index,item.GetName(LOCALE_LANIATUS) if item is not None else "<NONE>")
            index += 1

    @staticmethod
    def (UnnamedParameter):
        ch.ChatPacket(EChatType.CHAT_TYPE_COMMAND, "gift")

    @staticmethod
    def (UnnamedParameter):
        if not ch.CanDoCube():
            return

        cube_index = 0
        inven_index = 0
        line = None

        arg1 = str(['\0' for _ in range(256)])
        arg2 = str(['\0' for _ in range(256)])
        arg3 = str(['\0' for _ in range(256)])

        temp_ref_arg1 = RefObject(arg1);
        temp_ref_arg2 = RefObject(arg2);
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        line = Globals.two_arguments(argument, temp_ref_arg1, sizeof(arg1), temp_ref_arg2, sizeof(arg2))
        arg2 = temp_ref_arg2.arg_value
        arg1 = temp_ref_arg1.arg_value
        temp_ref_arg3 = RefObject(arg3);
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        Globals.one_argument(line, temp_ref_arg3, sizeof(arg3))
        arg3 = temp_ref_arg3.arg_value

        if 0 == arg1[0]:
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, "Usage: cube open")
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, "       cube close")
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, "       cube add <inveltory_index>")
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, "       cube delete <cube_index>")
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, "       cube list")
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, "       cube cancel")
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, "       cube make [all]")
            return

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to references to variables:
#ORIGINAL METINII C CODE: const str& strArg1 = str(arg1);
        strArg1 = arg1

        if strArg1 == "r_info":
            if 0 == arg2[0]:
                Globals.Cube_request_result_list(ch)
            else:
                if arg2.isdigit():
                    listIndex = 0
                    requestCount = 1
                    temp_ref_listIndex = RefObject(listIndex);
                    Globals.str_to_number(temp_ref_listIndex, arg2)
                    listIndex = temp_ref_listIndex.arg_value

                    if 0 != arg3[0] and arg3.isdigit():
                        temp_ref_requestCount = RefObject(requestCount);
                        Globals.str_to_number(temp_ref_requestCount, arg3)
                        requestCount = temp_ref_requestCount.arg_value

                    Globals.Cube_request_material_info(ch, listIndex, requestCount)

            return

        if LOWER(arg1[0]) == 'o':
            Globals.Cube_open(ch)

        elif LOWER(arg1[0]) == 'c':
            Globals.Cube_close(ch)

        elif LOWER(arg1[0]) == 'l':
            Globals.Cube_show_list(ch)

        elif LOWER(arg1[0]) == 'a':
                if 0 == arg2[0] or (not arg2.isdigit()) or 0 == arg3[0] or not arg3.isdigit():
                    return

                temp_ref_cube_index = RefObject(cube_index);
                Globals.str_to_number(temp_ref_cube_index, arg2)
                cube_index = temp_ref_cube_index.arg_value
                temp_ref_inven_index = RefObject(inven_index);
                Globals.str_to_number(temp_ref_inven_index, arg3)
                inven_index = temp_ref_inven_index.arg_value
                Globals.Cube_add_item(ch, cube_index, inven_index)

        elif LOWER(arg1[0]) == 'd':
                if 0 == arg2[0] or not arg2.isdigit():
                    return

                temp_ref_cube_index2 = RefObject(cube_index);
                Globals.str_to_number(temp_ref_cube_index2, arg2)
                cube_index = temp_ref_cube_index2.arg_value
                Globals.Cube_delete_item(ch, cube_index)

        elif LOWER(arg1[0]) == 'm':
            Globals.Cube_make(ch)

        else:
            return

    @staticmethod
    def (UnnamedParameter):
        country_code = str(['\0' for _ in range(3)])
        country_code[0] = 'd'
        country_code[1] = 'e'
        country_code[2] = '\0'

        buf = str(['\0' for _ in range(512 + 1)])
        sas = str(['\0' for _ in range(33)])
        ctx = MD5Context()
        SAS_KEY = "GF9001"

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        snprintf(buf, sizeof(buf), "%u%u%s", ch.GetPlayerID(), ch.GetAID(), SAS_KEY)

        Globals.MD5Init(ctx)
        Globals.MD5Update(ctx, ord(buf), uint(len(buf)))
        temp_ref_sas = RefObject(sas);
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##if __FreeBSD__
        Globals.MD5End(ctx, temp_ref_sas)
        sas = temp_ref_sas.arg_value
    ##else
        HEX = "0123456789abcdef"
        digest = [0 for _ in range(16)]
        Globals.MD5Final(digest, ctx)
        i = None
        for i in range(0, 16):
            sas[i + i] = HEX[digest[i] >> 4]
            sas[i + i + 1] = HEX[digest[i] & 0x0f]
        sas[i + i] = '\0'
    ##endif

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        snprintf(buf, sizeof(buf), "mall http:#%s/ishop?pid=%u&c=%s&sid=%d&sas=%s", g_strWebMallURL.c_str(), ch.GetPlayerID(), country_code, g_server_id, sas)

        ch.ChatPacket(EChatType.CHAT_TYPE_COMMAND, buf)

    @staticmethod
    def (UnnamedParameter):
        ch.ChatPacket(EChatType.CHAT_TYPE_COMMAND, "ShowMeMallPassword")

    @staticmethod
    def (UnnamedParameter):
        if ch.IsDead() or ch.IsStun():
            return

            if ch.IsHorseRiding():
                ch.StopRiding()
                return

            if ch.GetMountVnum():
                do_unmount(ch, None, 0, 0)
                return

        if ch.GetHorse() is not None:
            ch.StartRiding()
            return

        if ch.GetWear(EWearPositions.WEAR_COSTUME_MOUNT):
            ch.HorseSummon(((not LGEMiscellaneous.DEFINECONSTANTS.false)))
            ch.StartRiding()
            return
        else:
            i = 0
            while i < LGEMiscellaneous.INVENTORY_MAX_NUM:
                item = ch.GetInventoryItem(i)
                if None is item:
                    continue

                if item.IsCostumeMountItem():
                    ch.EquipItem(item)
                    ch.HorseSummon(((not LGEMiscellaneous.DEFINECONSTANTS.false)))
                    ch.StartRiding()
                    return
                i += 1

        ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Please call your Horse first."))

    @staticmethod
    def (UnnamedParameter):
        arg1 = str(['\0' for _ in range(256)])
        arg2 = str(['\0' for _ in range(256)])
        temp_ref_arg1 = RefObject(arg1);
        temp_ref_arg2 = RefObject(arg2);
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        Globals.two_arguments(argument, temp_ref_arg1, sizeof(arg1), temp_ref_arg2, sizeof(arg2))
        arg2 = temp_ref_arg2.arg_value
        arg1 = temp_ref_arg1.arg_value
        val = 0
        temp_ref_val = RefObject(val);
        Globals.str_to_number(temp_ref_val, arg2)
        val = temp_ref_val.arg_value

        if (not arg1[0]) != '\0' or val <= 0:
            return

        if ch.IsPolymorphed():
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You cannot change your state as long as you are transformed."))
            return

        if ch.GetPoint(EPointTypes.LG_POINT_STAT) <= 0:
            return

        idx = 0

        if not strcmp(arg1, "st"):
            idx = EPointTypes.LG_POINT_ST
        elif not strcmp(arg1, "dx"):
            idx = EPointTypes.LG_POINT_DX
        elif not strcmp(arg1, "ht"):
            idx = EPointTypes.LG_POINT_HT
        elif not strcmp(arg1, "iq"):
            idx = EPointTypes.LG_POINT_IQ
        else:
            return

        if ch.GetRealPoint(idx) >= LGEMiscellaneous.DEFINECONSTANTS.MAX_STAT:
            return

        if val > ch.GetPoint(EPointTypes.LG_POINT_STAT):
            val = ch.GetPoint(EPointTypes.LG_POINT_STAT)

        if ch.GetRealPoint(idx) + val > LGEMiscellaneous.DEFINECONSTANTS.MAX_STAT:
            val = LGEMiscellaneous.DEFINECONSTANTS.MAX_STAT - ch.GetRealPoint(idx)

        ch.SetRealPoint(idx, ch.GetRealPoint(idx) + val)
        ch.SetPoint(idx, ch.GetPoint(idx) + val)
        ch.ComputePoints()
        ch.PointChange(idx, 0)

        if idx == EPointTypes.LG_POINT_IQ:
            ch.PointChange(EPointTypes.LG_POINT_MAX_HP, 0)
        elif idx == EPointTypes.LG_POINT_HT:
            ch.PointChange(EPointTypes.LG_POINT_MAX_SP, 0)

        ch.PointChange(EPointTypes.LG_POINT_STAT, -val)
        ch.ComputePoints()

    @staticmethod
    def (UnnamedParameter):
        ch.ChatPacket(EChatType.CHAT_TYPE_INFO, "===== OX QUIZ LIST =====")
        COXEventManager.instance().ShowQuizList(ch)
        ch.ChatPacket(EChatType.CHAT_TYPE_INFO, "===== OX QUIZ LIST END =====")

    @staticmethod
    def (UnnamedParameter):
        if COXEventManager.instance().LogWinner() == LGEMiscellaneous.DEFINECONSTANTS.false:
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("OX The other participants in the Event are listed."))
        else:
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("OX The other participants in the Event are not listed."))

    @staticmethod
    def (UnnamedParameter):
        ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Number of the other participants : %d "), COXEventManager.instance().GetAttenderCount())


    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##if ! _WIN32
    ## Laniatus Games Studio Inc. | WARNING: The following #include directive was ignored:
    ##include <ifaddrs.h>
    ##endif

    ADDRESS_MAX_LEN = 15

# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
    #config_init(st_localeServiceName)
## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern char sql_addr[256]
## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern ushort mother_port
## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern ushort p2p_port
## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern char db_addr[ADDRESS_MAX_LEN + 1]
## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern ushort db_port
## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern int passes_per_sec
## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern int save_event_second_cycle
## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern int ping_event_second_cycle
## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern int test_server
## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern bool guild_mark_server
## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern byte guild_mark_min_level
## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern bool g_bNoMoreClient
## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern bool g_bNoRegen
## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern bool g_bEmpireShopPriceTrippleDisable
## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern bool g_bShoutAddonEnable
## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern bool g_bGlobalShoutEnable
## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern bool g_bAllMountAttack
## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern byte g_bChannel
    @staticmethod
    def map_allow_find(index):
        if Globals.g_bAuthServer != 0:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if Globals.s_set_map_allows.find(index) == Globals.s_set_map_allows.end():
            return LGEMiscellaneous.DEFINECONSTANTS.false

        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    @staticmethod
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Pointer arithmetic is detected on the parameter 'pl':
#ORIGINAL METINII C CODE: void map_allow_copy(int * pl, int size)
    def map_allow_copy(pl, size):
        iCount = 0
        it = Globals.s_set_map_allows.begin()

        while it is not Globals.s_set_map_allows.end():
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: int i = *(it++);
            i = *(it)
            it += 1
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: *(pl++) = i;
            *(pl) = i
            pl += 1

            iCount += 1
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: if (++iCount > size)
            if iCount > size:
                break

## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern bool no_wander
## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern int g_iUserLimit
## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern time_t g_global_time
    @staticmethod
    def get_table_postfix():
        return Globals.g_table_postfix.c_str()

## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern str g_stHostname
## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern str g_stLocale
## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern str g_stLocaleFilename
## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern char g_szPublicIP[16]
## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern char g_szInternalIP[16]
class is_twobyteDelegate:
    def invoke(self, str):
        pass

    is_twobyte = is_twobyteDelegate()
    extern int(check_name)(const char * str)
## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern bool g_bSkillDisable
## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern int g_iFullUserCount
## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern int g_iBusyUserCount
    @staticmethod
    def LoadStateUserCount():
        fp = fopen("state_user_count", "r")

        if fp is None:
            return

        fscanf(fp, " %d %d ", Globals.g_iFullUserCount, Globals.g_iBusyUserCount)
        fclose(fp)

## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern bool g_bEmpireWhisper
## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern byte g_bAuthServer
## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern byte PK_PROTECT_LEVEL
    @staticmethod
    def LoadValidCRCList():
        Globals.s_set_dwProcessCRC.clear()
        Globals.s_set_dwFileCRC.clear()

        fp = None
        buf = str(['\0' for _ in range(256)])

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((fp = fopen("CRC", "r")))
        if (fp = fopen("CRC", "r")):
            while fgets(buf, 256, fp):
                if (not buf[0]) != '\0':
                    continue

                dwValidClientProcessCRC = None
                dwValidClientFileCRC = None

                sscanf(buf, " %u %u ", dwValidClientProcessCRC, dwValidClientFileCRC)

                Globals.s_set_dwProcessCRC.insert(dwValidClientProcessCRC)
                Globals.s_set_dwFileCRC.insert(dwValidClientFileCRC)

                fprintf(stderr, "CLIENT_CRC: %u %u\n", dwValidClientProcessCRC, dwValidClientFileCRC)

            fclose(fp)

    @staticmethod
    def IsValidProcessCRC(dwCRC):
        return Globals.s_set_dwProcessCRC.find(dwCRC) != Globals.s_set_dwProcessCRC.end()

    @staticmethod
    def IsValidFileCRC(dwCRC):
        return Globals.s_set_dwFileCRC.find(dwCRC) != Globals.s_set_dwFileCRC.end()

## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern str g_stAuthMasterIP
## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern ushort g_wAuthMasterPort
## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern str g_stClientVersion
## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern bool g_bCheckClientVersion
    @staticmethod
    def CheckClientVersion():
        Globals.g_bCheckClientVersion = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        set = DESC_MANAGER.instance().GetClientSet()
        it = set.begin()

        while it is not set.end():
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: DESC* d = *(it++);
            d = *(it)
            it += 1

            if d.GetCharacter() is None:
                continue


            version = atoi(Globals.g_stClientVersion.c_str())
            date = atoi(d.GetClientVersion())

            if version > date:
                d.GetCharacter().ChatPacket(EChatType.CHAT_TYPE_NOTICE, LC_TEXT("Your client version is not correct. Please install the normal patch."))
                d.DelayedDisconnect(10)

## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern str g_stQuestDir
## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern std::set<str> g_setQuestObjectDir
## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern int SPEEDHACK_LIMIT_COUNT
## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern int SPEEDHACK_LIMIT_BONUS
## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern int g_iSyncHackLimitCount
## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern int g_server_id
## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern str g_strWebMallURL
## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern int VIEW_RANGE
## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern int VIEW_BONUS_RANGE
## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern bool g_bCheckMultiHack
## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern bool g_protectNormalPlayer
## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern bool g_noticeBattleZone
## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern uint g_GoldDropTimeLimitValue
## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern int gPlayerMaxLevel
## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern int gShutdownAge
## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern int gShutdownEnable
## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern bool g_BlockCharCreation
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##if ! _IMPROVED_PACKET_ENCRYPTION_
## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern bool g_isShutdowned

    g_bChannel = 0
    mother_port = 50080
    passes_per_sec = 25
    db_port = 0
    p2p_port = 50900
    db_addr = str(['\0' for _ in range(ADDRESS_MAX_LEN + 1)])
    save_event_second_cycle = passes_per_sec * 120
    ping_event_second_cycle = passes_per_sec * 60
    g_bNoMoreClient = LGEMiscellaneous.DEFINECONSTANTS.false
    g_bNoRegen = LGEMiscellaneous.DEFINECONSTANTS.false
    g_bEmpireShopPriceTrippleDisable = LGEMiscellaneous.DEFINECONSTANTS.false
    g_bShoutAddonEnable = LGEMiscellaneous.DEFINECONSTANTS.false
    g_bGlobalShoutEnable = LGEMiscellaneous.DEFINECONSTANTS.false
    g_bAllMountAttack = LGEMiscellaneous.DEFINECONSTANTS.false
    test_server = 0
    guild_mark_server = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
    guild_mark_min_level = 3
    no_wander = LGEMiscellaneous.DEFINECONSTANTS.false
    g_iUserLimit = 32768
    g_szPublicIP = "0"
    g_szInternalIP = "0"
    g_bSkillDisable = LGEMiscellaneous.DEFINECONSTANTS.false
    g_iFullUserCount = 1200
    g_iBusyUserCount = 150
    g_bEmpireWhisper = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
    g_bAuthServer = LGEMiscellaneous.DEFINECONSTANTS.false
    g_bCheckClientVersion = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
    g_stClientVersion = LGEMiscellaneous.DEFINECONSTANTS.CLIENT_VERSION
    g_stAuthMasterIP = string()
    g_wAuthMasterPort = 0

    s_set_dwFileCRC = std::set()
    s_set_dwProcessCRC = std::set()

    g_stHostname = ""
    g_table_postfix = ""
    g_stQuestDir = "./share/quest"
    g_stDefaultQuestObjectDir = "./share/quest/object"
    g_setQuestObjectDir = std::set()
    g_stBlockDate = "30000705"

## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern string g_stLocale
## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern str g_stLocaleFilename

    SPEEDHACK_LIMIT_COUNT = 50
    SPEEDHACK_LIMIT_BONUS = 80
    g_iSyncHackLimitCount = 10
    VIEW_RANGE = 5000
    VIEW_BONUS_RANGE = 500
    g_server_id = 0
    g_strWebMallURL = "localhost/ishop/"

    g_uiSpamBlockDuration = uint(60 * 15)
    g_uiSpamBlockScore = 100
    g_uiSpamReloadCycle = uint(60 * 10)
    g_bCheckMultiHack = LGEMiscellaneous.DEFINECONSTANTS.false
    g_iSpamBlockMaxLevel = 10
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
    #LoadStateUserCount()
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
    #LoadValidCRCList()
    @staticmethod
    def LoadClientVersion():
        fp = fopen("VERSION", "r")

        if fp is None:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        buf = str(['\0' for _ in range(256)])
        fgets(buf, 256, fp)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to pointers to value types:
#ORIGINAL METINII C CODE: char * p = strchr(buf, '\n');
        p = strchr(buf, '\n')
        if p != '\0':
            p = '\0'

        fprintf(stderr, "VERSION: \"%s\"\n", buf)

        Globals.g_stClientVersion = buf
        fclose(fp)
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    g_protectNormalPlayer = LGEMiscellaneous.DEFINECONSTANTS.false
    g_noticeBattleZone = LGEMiscellaneous.DEFINECONSTANTS.false

    gPlayerMaxLevel = 99
    gShutdownAge = 0
    gShutdownEnable = 0
    g_BlockCharCreation = LGEMiscellaneous.DEFINECONSTANTS.false
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##if ! _IMPROVED_PACKET_ENCRYPTION_
    g_isShutdowned = LGEMiscellaneous.DEFINECONSTANTS.false
    ##endif

    @staticmethod
    def is_string_true(string):
        result = False
        if (not((string & 0xE0) > 0x90) and isdigitstring):
            temp_ref_result = RefObject(result);
            Globals.str_to_number(temp_ref_result, string)
            result = temp_ref_result.arg_value
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false)) if result > False else LGEMiscellaneous.DEFINECONSTANTS.false
        elif LOWERstring == 't':
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
        else:
            return LGEMiscellaneous.DEFINECONSTANTS.false

    s_set_map_allows = std::set()

    @staticmethod
    def map_allow_log():
        i = s_set_map_allows.begin()
        while i is not Globals.s_set_map_allows.end():
            Globals.#sys_log(0, "MAP_ALLOW: %d", i)
            i += 1

    @staticmethod
    def map_allow_add(index):
        if Globals.map_allow_find(index) == ((not LGEMiscellaneous.DEFINECONSTANTS.false)):
            fprintf(stdout, "!!! FATAL ERROR !!! multiple MAP_ALLOW setting!!\n")
            exit(1)

        fprintf(stdout, "MAP ALLOW %d\n", index)
        Globals.s_set_map_allows.insert(index)

    @staticmethod
    def GetIPInfo():
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##if ! _WIN32
        ifaddrp = None

        if 0 != getifaddrs(ifaddrp):
            return LGEMiscellaneous.DEFINECONSTANTS.false

        ifap = ifaddrp
        while None is not ifap:
            sai = ifap.ifa_addr

            if (not ifap.ifa_netmask) or sai.sin_addr.s_addr == 0 or sai.sin_addr.s_addr == 16777343:
                continue
    ##else
        wsa_data = WSADATA()
        host_name = str(['\0' for _ in range(100)])
        host_ent = None
        n = 0

        if WSAStartup(0x0101, wsa_data):
            return LGEMiscellaneous.DEFINECONSTANTS.false

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        gethostname(host_name, sizeof(host_name))
        host_ent = gethostbyname(host_name)
        if host_ent is None:
            return LGEMiscellaneous.DEFINECONSTANTS.false
        while host_ent.h_addr_list[n] is not None:
            addr = sockaddr_in()
            sai = addr
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memcpy' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
            memcpy(sai.sin_addr.s_addr, host_ent.h_addr_list[n], host_ent.h_length)
    ##endif

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to pointers to value types:
#ORIGINAL METINII C CODE: char* netip = inet_ntoa(sai->sin_addr);
            netip = inet_ntoa(sai.sin_addr)

            if not strncmp(netip, "10.", 3):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                strncpy_s(Globals.g_szInternalIP, sizeof(Globals.g_szInternalIP), netip, _TRUNCATE)
            elif Globals.g_szPublicIP[0] == '0':
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                strncpy_s(Globals.g_szPublicIP, sizeof(Globals.g_szPublicIP), netip, _TRUNCATE)
            n += 1

    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##if ! _WIN32
        freeifaddrs(ifaddrp)
    ##else
        WSACleanup()
    ##endif

        if Globals.g_szPublicIP[0] != '0':
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
        else:
            return LGEMiscellaneous.DEFINECONSTANTS.false

    @staticmethod
    def config_init(st_localeServiceName):
        fp = None

        buf = str(['\0' for _ in range(256)])
        token_string = str(['\0' for _ in range(256)])
        value_string = str(['\0' for _ in range(256)])

        st_configFileName = string()

        st_configFileName.reserve(32)
        st_configFileName = "CONFIG"

        if not st_localeServiceName.empty():
            st_configFileName += "."
            st_configFileName += st_localeServiceName

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if (!(fp = fopen(st_configFileName.c_str(), "r")))
        if not(fp = fopen(st_configFileName.c_str(), "r")):
            fprintf(stderr, "Can not open [%s]\n", st_configFileName.c_str())
            exit(1)

        if not Globals.GetIPInfo():
            fprintf(stderr, "Can not get public ip address\n")
            exit(1)

        db_host = [[] for _ in range(2)]
        db_user = [[] for _ in range(2)]
        db_pwd = [[] for _ in range(2)]
        db_db = [[] for _ in range(2)]
        mysql_db_port = [0 for _ in range(2)]

        for n in range(0, 2):
            db_host[n] = '\0'
            db_user[n] = '\0'
            db_pwd[n] = '\0'
            db_db[n] = '\0'
            mysql_db_port[n] = 0

        log_host = str(['\0' for _ in range(64)])
        log_user = str(['\0' for _ in range(64)])
        log_pwd = str(['\0' for _ in range(64)])
        log_db = str(['\0' for _ in range(64)])
        log_port = 0

        log_host[0] = '\0'
        log_user[0] = '\0'
        log_pwd[0] = '\0'
        log_db[0] = '\0'


        isCommonSQL = LGEMiscellaneous.DEFINECONSTANTS.false
        isPlayerSQL = LGEMiscellaneous.DEFINECONSTANTS.false

        fpOnlyForDB = None

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if (!(fpOnlyForDB = fopen(st_configFileName.c_str(), "r")))
        if not(fpOnlyForDB = fopen(st_configFileName.c_str(), "r")):
            fprintf(stderr, "Can not open [%s]\n", st_configFileName.c_str())
            exit(1)

        while fgets(buf, 256, fpOnlyForDB):
            parse_token(buf, token_string, value_string)

            TOKEN("BLOCK_LOGIN")
                Globals.g_stBlockDate = value_string

            TOKEN("hostname")
                Globals.g_stHostname = value_string
                continue

            TOKEN("channel")
                temp_ref_g_bChannel = RefObject(Globals.g_bChannel);
                Globals.str_to_number(temp_ref_g_bChannel, value_string)
                Globals.g_bChannel = temp_ref_g_bChannel.arg_value
                continue

            TOKEN("sql_player")
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                line = Globals.two_arguments(value_string, db_host[0], sizeof(db_host[0]), db_user[0], sizeof(db_user[0]))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                line = Globals.two_arguments(line, db_pwd[0], sizeof(db_pwd[0]), db_db[0], sizeof(db_db[0]))

                if '\0' != line[0]:
                    buf = str(['\0' for _ in range(256)])
                    temp_ref_buf = RefObject(buf);
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                    Globals.one_argument(line, temp_ref_buf, sizeof(buf))
                    buf = temp_ref_buf.arg_value
                    Globals.str_to_number(ushort(short(1 if mysql_db_port[0] != 0 else 0)), buf)

                if (not db_host[0]) != '\0' or (not db_user[0]) != '\0' or (not db_pwd[0]) != '\0' or (not db_db[0]) != '\0':
                    fprintf(stderr, "PLAYER_SQL syntax: logsql <host user password db>\n")
                    exit(1)

                buf = str(['\0' for _ in range(1024)])
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                snprintf(buf, sizeof(buf), "PLAYER_SQL: %s %s %s %s %d", db_host[0], db_user[0], db_pwd[0], db_db[0], mysql_db_port[0])
                isPlayerSQL = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
                continue

            TOKEN("sql_common")
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                line = Globals.two_arguments(value_string, db_host[1], sizeof(db_host[1]), db_user[1], sizeof(db_user[1]))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                line = Globals.two_arguments(line, db_pwd[1], sizeof(db_pwd[1]), db_db[1], sizeof(db_db[1]))

                if '\0' != line[0]:
                    buf = str(['\0' for _ in range(256)])
                    temp_ref_buf2 = RefObject(buf);
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                    Globals.one_argument(line, temp_ref_buf2, sizeof(buf))
                    buf = temp_ref_buf2.arg_value
                    Globals.str_to_number(ushort(short(1 if mysql_db_port[1] != 0 else 0)), buf)

                if (not db_host[1]) != '\0' or (not db_user[1]) != '\0' or (not db_pwd[1]) != '\0' or (not db_db[1]) != '\0':
                    fprintf(stderr, "COMMON_SQL syntax: logsql <host user password db>\n")
                    exit(1)

                buf = str(['\0' for _ in range(1024)])
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                snprintf(buf, sizeof(buf), "COMMON_SQL: %s %s %s %s %d", db_host[1], db_user[1], db_pwd[1], db_db[1], mysql_db_port[1])
                isCommonSQL = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
                continue

            TOKEN("sql_log")
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                line = Globals.two_arguments(value_string, log_host, sizeof(log_host), log_user, sizeof(log_user))
                temp_ref_log_pwd = RefObject(log_pwd);
                temp_ref_log_db = RefObject(log_db);
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                line = Globals.two_arguments(line, temp_ref_log_pwd, sizeof(log_pwd), temp_ref_log_db, sizeof(log_db))
                log_db = temp_ref_log_db.arg_value
                log_pwd = temp_ref_log_pwd.arg_value

                if '\0' != line[0]:
                    buf = str(['\0' for _ in range(256)])
                    temp_ref_buf3 = RefObject(buf);
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                    Globals.one_argument(line, temp_ref_buf3, sizeof(buf))
                    buf = temp_ref_buf3.arg_value
                    temp_ref_log_port = RefObject(log_port);
                    Globals.str_to_number(temp_ref_log_port, buf)
                    log_port = temp_ref_log_port.arg_value

                if (not log_host[0]) != '\0' or (not log_user[0]) != '\0' or (not log_pwd[0]) != '\0' or (not log_db[0]) != '\0':
                    fprintf(stderr, "LOG_SQL syntax: logsql <host user password db>\n")
                    exit(1)

                buf = str(['\0' for _ in range(1024)])
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                snprintf(buf, sizeof(buf), "LOG_SQL: %s %s %s %s %d", log_host, log_user, log_pwd, log_db, log_port)
                continue
        fclose(fpOnlyForDB)

        if not isCommonSQL:
            puts("LOAD_COMMON_SQL_INFO_FAILURE:")
            puts("")
            puts("CONFIG:")
            puts("------------------------------------------------")
            puts("COMMON_SQL: HOST USER PASSWORD DATABASE")
            puts("")
            exit(1)

        if not isPlayerSQL:
            puts("LOAD_PLAYER_SQL_INFO_FAILURE:")
            puts("")
            puts("CONFIG:")
            puts("------------------------------------------------")
            puts("PLAYER_SQL: HOST USER PASSWORD DATABASE")
            puts("")
            exit(1)

        AccountDB.instance().Connect(db_host[1], mysql_db_port[1], db_user[1], db_pwd[1], db_db[1])

        if LGEMiscellaneous.DEFINECONSTANTS.false == AccountDB.instance().IsConnected():
            fprintf(stderr, "cannot start server while no common sql connected\n")
            exit(1)

        printf("-----------------------------------------------\n")
        fprintf(stdout, "CommonSQL connected\n")

            szQuery = str(['\0' for _ in range(512)])
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            snprintf(szQuery, sizeof(szQuery), "SELECT mKey, mValue FROM locale")

            pMsg = std::unique_ptr(AccountDB.instance().DirectQuery(szQuery))

            if pMsg.Get().uiNumRows == 0:
                fprintf(stderr, "COMMON_SQL: DirectQuery failed : %s\n", szQuery)
                exit(1)

        AccountDB.instance().SetLocale(g_stLocale)
        AccountDB.instance().ConnectAsync(db_host[1], mysql_db_port[1], db_user[1], db_pwd[1], db_db[1], g_stLocale.c_str())

        DBManager.instance().Connect(db_host[0], mysql_db_port[0], db_user[0], db_pwd[0], db_db[0])

        if not DBManager.instance().IsConnected():
            fprintf(stderr, "PlayerSQL.ConnectError\n")
            exit(1)

        fprintf(stdout, "PlayerSQL connected\n")

        if LGEMiscellaneous.DEFINECONSTANTS.false == Globals.g_bAuthServer:
            LogManager.instance().Connect(log_host, log_port, log_user, log_pwd, log_db)

            if not LogManager.instance().IsConnected():
                fprintf(stderr, "LogSQL.ConnectError\n")
                exit(1)

            fprintf(stdout, "LogSQL connected\n")
            printf("-----------------------------------------------\n")

            LogManager.instance().BootLog(Globals.g_stHostname.c_str(), Globals.g_bChannel)

            szQuery = str(['\0' for _ in range(256)])
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            snprintf(szQuery, sizeof(szQuery), "SELECT mValue FROM locale WHERE mKey='LG_SKILL_POWER_BY_LEVEL'")
            pMsg = std::unique_ptr(AccountDB.instance().DirectQuery(szQuery))

            if pMsg.Get().uiNumRows == 0:
                fprintf(stderr, "[LG_SKILL_PERCENT] Query failed: %s", szQuery)
                exit(1)

            row = MYSQL_ROW()

            row = Globals.mysql_fetch_row(pMsg.Get().pSQLResult)

            p = row[0]
            cnt = 0
            num = str(['\0' for _ in range(128)])
            aiBaseSkillPowerByLevelTable = [0 for _ in range((int)LGEMiscellaneous.LG_SKILL_MAX_LEVEL + 1)]

            while p[0] != '\0' and cnt < (LGEMiscellaneous.LG_SKILL_MAX_LEVEL + 1):
                temp_ref_num = RefObject(num);
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                p = Globals.one_argument(p, temp_ref_num, sizeof(num))
                num = temp_ref_num.arg_value
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: aiBaseSkillPowerByLevelTable[cnt++] = atoi(num);
                aiBaseSkillPowerByLevelTable[cnt] = atoi(num)
                cnt += 1

                if p[0] == '\0':
                    if cnt != (LGEMiscellaneous.LG_SKILL_MAX_LEVEL + 1):
                        fprintf(stderr, "[LG_SKILL_PERCENT] locale table has not enough skill information! (count: %d query: %s)", cnt, szQuery)
                        exit(1)
                    break

            job = 0
            while job < EJobs.JOB_MAX_NUM * 2:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                snprintf(szQuery, sizeof(szQuery), "SELECT mValue from locale where mKey='LG_SKILL_POWER_BY_LEVEL_TYPE%d' ORDER BY CAST(mValue AS unsigned)", job)
                pMsg = std::unique_ptr(AccountDB.instance().DirectQuery(szQuery))

                if pMsg.Get().uiNumRows == 0:
                    CTableBySkill.instance().SetSkillPowerByLevelFromType(job, aiBaseSkillPowerByLevelTable)
                    continue

                row = Globals.mysql_fetch_row(pMsg.Get().pSQLResult)
                cnt = 0
                p = row[0]
                aiSkillTable = [0 for _ in range((int)LGEMiscellaneous.LG_SKILL_MAX_LEVEL + 1)]

                while p[0] != '\0' and cnt < (LGEMiscellaneous.LG_SKILL_MAX_LEVEL + 1):
                    temp_ref_num2 = RefObject(num);
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                    p = Globals.one_argument(p, temp_ref_num2, sizeof(num))
                    num = temp_ref_num2.arg_value
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: aiSkillTable[cnt++] = atoi(num);
                    aiSkillTable[cnt] = atoi(num)
                    cnt += 1

                    if p[0] == '\0':
                        if cnt != (LGEMiscellaneous.LG_SKILL_MAX_LEVEL + 1):
                            fprintf(stderr, "[LG_SKILL_PERCENT] locale table has not enough skill information! (count: %d query: %s)", cnt, szQuery)
                            exit(1)
                        break

                CTableBySkill.instance().SetSkillPowerByLevelFromType(job, aiSkillTable)
                job += 1

        Globals.log_set_expiration_days(2)
        while fgets(buf, 256, fp):
            parse_token(buf, token_string, value_string)

            TOKEN("empire_whisper")
                b_value = False
                temp_ref_b_value = RefObject(b_value);
                Globals.str_to_number(temp_ref_b_value, value_string)
                b_value = temp_ref_b_value.arg_value
                Globals.g_bEmpireWhisper = b_value
                continue

            TOKEN("mark_server")
                Globals.guild_mark_server = Globals.is_string_true(value_string)
                continue

            TOKEN("mark_min_level")
                temp_ref_guild_mark_min_level = RefObject(Globals.guild_mark_min_level);
                Globals.str_to_number(temp_ref_guild_mark_min_level, value_string)
                Globals.guild_mark_min_level = temp_ref_guild_mark_min_level.arg_value
                Globals.guild_mark_min_level = MINMAX(0, Globals.guild_mark_min_level, LGEMiscellaneous.GUILD_MAX_LEVEL)
                continue

            TOKEN("port")
                temp_ref_mother_port = RefObject(Globals.mother_port);
                Globals.str_to_number(temp_ref_mother_port, value_string)
                Globals.mother_port = temp_ref_mother_port.arg_value
                continue

            TOKEN("log_keep_days")
                i = 0
                temp_ref_i = RefObject(i);
                Globals.str_to_number(temp_ref_i, value_string)
                i = temp_ref_i.arg_value
                Globals.log_set_expiration_days(MINMAX(1, i, 90))
                continue

            TOKEN("passes_per_sec")
                temp_ref_passes_per_sec = RefObject(Globals.passes_per_sec);
                Globals.str_to_number(temp_ref_passes_per_sec, value_string)
                Globals.passes_per_sec = temp_ref_passes_per_sec.arg_value
                continue

            TOKEN("p2p_port")
                temp_ref_p2p_port = RefObject(Globals.p2p_port);
                Globals.str_to_number(temp_ref_p2p_port, value_string)
                Globals.p2p_port = temp_ref_p2p_port.arg_value
                continue

            TOKEN("db_port")
                temp_ref_db_port = RefObject(Globals.db_port);
                Globals.str_to_number(temp_ref_db_port, value_string)
                Globals.db_port = temp_ref_db_port.arg_value
                continue

            TOKEN("db_addr")
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                strncpy_s(Globals.db_addr, sizeof(Globals.db_addr), value_string, _TRUNCATE)

                for n in range(0, Globals.ADDRESS_MAX_LEN):
                    if Globals.db_addr[n] == ' ':
                        Globals.db_addr[n] = '\0'
                continue

            TOKEN("save_event_second_cycle")
                cycle = 0
                temp_ref_cycle = RefObject(cycle);
                Globals.str_to_number(temp_ref_cycle, value_string)
                cycle = temp_ref_cycle.arg_value
                Globals.save_event_second_cycle = cycle * Globals.passes_per_sec
                continue

            TOKEN("ping_event_second_cycle")
                cycle = 0
                temp_ref_cycle2 = RefObject(cycle);
                Globals.str_to_number(temp_ref_cycle2, value_string)
                cycle = temp_ref_cycle2.arg_value
                Globals.ping_event_second_cycle = cycle * Globals.passes_per_sec
                continue

            TOKEN("table_postfix")
                Globals.g_table_postfix = value_string
                continue

            TOKEN("test_server")
                printf("-----------------------------------------------\n")
                printf("TEST_SERVER\n")
                printf("-----------------------------------------------\n")
                temp_ref_test_server = RefObject(Globals.test_server);
                Globals.str_to_number(temp_ref_test_server, value_string)
                Globals.test_server = temp_ref_test_server.arg_value
                continue

            TOKEN("shutdowned")
                Globals.g_bNoMoreClient = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
                continue

            TOKEN("no_regen")
                Globals.g_bNoRegen = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
                continue


            TOKEN("map_allow")
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Pointer arithmetic is detected on this variable:
#ORIGINAL METINII C CODE: char* p = value_string;
                p = value_string
                stNum = string()

                while *p != '\0':
                    if (not(((*p) & 0xE0) > 0x90) and isspace(*p)):
                        if stNum.length():
                            index = 0
                            temp_ref_index = RefObject(index);
                            Globals.str_to_number(temp_ref_index, stNum.c_str())
                            index = temp_ref_index.arg_value
                            Globals.map_allow_add(index)
                            stNum.clear()
                    else:
                        stNum += *p
                    p += 1

                if stNum.length():
                    index = 0
                    temp_ref_index2 = RefObject(index);
                    Globals.str_to_number(temp_ref_index2, stNum.c_str())
                    index = temp_ref_index2.arg_value
                    Globals.map_allow_add(index)

                continue

            TOKEN("no_wander")
                Globals.no_wander = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
                continue

            TOKEN("user_limit")
                temp_ref_g_iUserLimit = RefObject(Globals.g_iUserLimit);
                Globals.str_to_number(temp_ref_g_iUserLimit, value_string)
                Globals.g_iUserLimit = temp_ref_g_iUserLimit.arg_value
                continue

            TOKEN("LG_SKILL_disable")
                temp_ref_g_bSkillDisable = RefObject(Globals.g_bSkillDisable);
                Globals.str_to_number(temp_ref_g_bSkillDisable, value_string)
                Globals.g_bSkillDisable = temp_ref_g_bSkillDisable.arg_value
                continue

            TOKEN("auth_server")
                szIP = str(['\0' for _ in range(32)])
                szPort = str(['\0' for _ in range(32)])

                temp_ref_szIP = RefObject(szIP);
                temp_ref_szPort = RefObject(szPort);
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                Globals.two_arguments(value_string, temp_ref_szIP, sizeof(szIP), temp_ref_szPort, sizeof(szPort))
                szPort = temp_ref_szPort.arg_value
                szIP = temp_ref_szIP.arg_value

                if (not szIP[0]) != '\0' or ((not szPort[0]) != '\0' and _stricmp(szIP, "master")):
                    fprintf(stderr, "AUTH_SERVER: syntax error: <ip|master> <port>\n")
                    exit(1)

                Globals.g_bAuthServer = 1 if ((not LGEMiscellaneous.DEFINECONSTANTS.false)) else 0
                if not _stricmp(szIP, "master"):
                    printf("-----------------------------------------------\n")
                    fprintf(stdout, "Login server was started.\n")
                    printf("-----------------------------------------------\n")
                else:
                    Globals.g_stAuthMasterIP = szIP
                    temp_ref_g_wAuthMasterPort = RefObject(Globals.g_wAuthMasterPort);
                    Globals.str_to_number(temp_ref_g_wAuthMasterPort, szPort)
                    Globals.g_wAuthMasterPort = temp_ref_g_wAuthMasterPort.arg_value
                    fprintf(stdout, "AUTH_SERVER: master %s %u\n", Globals.g_stAuthMasterIP.c_str(), Globals.g_wAuthMasterPort)
                continue

            TOKEN("quest_dir")
                Globals.#sys_log(0, "QUEST_DIR SETTING : %s", value_string)
                Globals.g_stQuestDir = value_string

            TOKEN("quest_object_dir")
                is_ = std::istringstream(value_string)
                Globals.#sys_log(0, "QUEST_OBJECT_DIR SETTING : %s", value_string)
                dir = string()
                while not is_.eof():
                    is_ >> dir
                    if is_.fail():
                        break
                    Globals.g_setQuestObjectDir.insert(dir)
                    Globals.#sys_log(0, "QUEST_OBJECT_DIR INSERT : %s", dir.c_str())

            TOKEN("server_id")
                temp_ref_g_server_id = RefObject(Globals.g_server_id);
                Globals.str_to_number(temp_ref_g_server_id, value_string)
                Globals.g_server_id = temp_ref_g_server_id.arg_value

            TOKEN("mall_url")
                Globals.g_strWebMallURL = value_string

            TOKEN("bind_ip")
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                strncpy_s(Globals.g_szPublicIP, sizeof(Globals.g_szPublicIP), value_string, _TRUNCATE)

            TOKEN("view_range")
                temp_ref_VIEW_RANGE = RefObject(Globals.VIEW_RANGE);
                Globals.str_to_number(temp_ref_VIEW_RANGE, value_string)
                Globals.VIEW_RANGE = temp_ref_VIEW_RANGE.arg_value

            TOKEN("protect_normal_player")
                temp_ref_g_protectNormalPlayer = RefObject(Globals.g_protectNormalPlayer);
                Globals.str_to_number(temp_ref_g_protectNormalPlayer, value_string)
                Globals.g_protectNormalPlayer = temp_ref_g_protectNormalPlayer.arg_value

            TOKEN("pk_protect_level")
                temp_ref_PK_PROTECT_LEVEL = RefObject(PK_PROTECT_LEVEL);
                Globals.str_to_number(temp_ref_PK_PROTECT_LEVEL, value_string)
                PK_PROTECT_LEVEL = temp_ref_PK_PROTECT_LEVEL.arg_value

            TOKEN("max_level")
                temp_ref_gPlayerMaxLevel = RefObject(Globals.gPlayerMaxLevel);
                Globals.str_to_number(temp_ref_gPlayerMaxLevel, value_string)
                Globals.gPlayerMaxLevel = temp_ref_gPlayerMaxLevel.arg_value
                Globals.gPlayerMaxLevel = MINMAX(1, Globals.gPlayerMaxLevel, LGEMiscellaneous.PLAYER_MAX_LEVEL_CONST)

            TOKEN("block_char_creation")
                tmp = 0

                temp_ref_tmp = RefObject(tmp);
                Globals.str_to_number(temp_ref_tmp, value_string)
                tmp = temp_ref_tmp.arg_value

                if 0 == tmp:
                    Globals.g_BlockCharCreation = LGEMiscellaneous.DEFINECONSTANTS.false
                else:
                    Globals.g_BlockCharCreation = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

                continue

        if Globals.g_setQuestObjectDir.empty():
            Globals.g_setQuestObjectDir.insert(Globals.g_stDefaultQuestObjectDir)

        if 0 == Globals.db_port:
            fprintf(stderr, "DB_PORT not configured\n")
            exit(1)

        if 0 == Globals.g_bChannel:
            fprintf(stderr, "CHANNEL not configured\n")
            exit(1)

        if Globals.g_stHostname.empty():
            fprintf(stderr, "HOSTNAME must be configured.\n")
            exit(1)

        if Globals.g_bAuthServer == 0:
            Globals.LocaleService_LoadLocaleStringFile()
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##if __MULTI_LANGUAGE_SYSTEM__
            Globals.LocaleService_LoadQuestTranslateFile()
            Globals.LocaleService_LoadItemNameFile()
            Globals.LocaleService_LoadMobNameFile()
            Globals.LocaleService_LoadSkillNameFile()
    ##endif

            printf("-----------------------------------------------\n")
            fprintf(stdout, "%s was started.\n", Globals.g_stHostname.c_str())
            printf("-----------------------------------------------\n")

        fclose(fp)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((fp = fopen("CMD", "r")))
        if (fp = fopen("CMD", "r")):
            while fgets(buf, 256, fp):
                cmd = str(['\0' for _ in range(32)])
                levelname = str(['\0' for _ in range(32)])
                level = None

                temp_ref_cmd = RefObject(cmd);
                temp_ref_levelname = RefObject(levelname);
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                Globals.two_arguments(buf, temp_ref_cmd, sizeof(cmd), temp_ref_levelname, sizeof(levelname))
                levelname = temp_ref_levelname.arg_value
                cmd = temp_ref_cmd.arg_value

                if (not cmd[0]) != '\0' or (not levelname[0]) != '\0':
                    fprintf(stderr, "CMD syntax error: <cmd> <DISABLE | PLAYER | PLAYER | LOW_WIZARD | WIZARD | HIGH_WIZARD | GOD>\n")
                    exit(1)

                if not _stricmp(levelname, "LOW_WIZARD"):
                    level = EGMLevels.GM_LOW_WIZARD
                elif not _stricmp(levelname, "WIZARD"):
                    level = EGMLevels.GM_WIZARD
                elif not _stricmp(levelname, "HIGH_WIZARD"):
                    level = EGMLevels.GM_HIGH_WIZARD
                elif not _stricmp(levelname, "GOD"):
                    level = EGMLevels.GM_GOD
                elif not _stricmp(levelname, "IMPLEMENTOR"):
                    level = EGMLevels.GM_IMPLEMENTOR
                elif not _stricmp(levelname, "PLAYER"):
                    level = EGMLevels.GM_PLAYER
                elif not _stricmp(levelname, "DISABLE"):
                    level = EGMLevels.GM_IMPLEMENTOR + 1
                else:
                    fprintf(stderr, "CMD syntax error: <cmd> <DISABLE  | PLAYER | LOW_WIZARD | WIZARD | HIGH_WIZARD | GOD>\n")
                    exit(1)

                Globals.interpreter_set_privilege(cmd, level)

            fclose(fp)

        Globals.LoadStateUserCount()
        CWarMapManager.instance().LoadWarMapInfo(None)
        if Globals.g_szPublicIP[0] == '0':
            fprintf(stderr, "Can not get public ip address\n")
            exit(1)




    @staticmethod
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Pointer arithmetic is detected on the parameter 'buf':
#ORIGINAL METINII C CODE: uint GetCRC32(const char * buf, size_t len)
    def GetCRC32(buf, len):
        crc = 0xffffffff

        if 16 <= len:
            condition = True
            while condition:
                crc = Globals.CRCTable[(crc ^ buf[0]) & 0xff] ^ (crc >> 8)
                crc = Globals.CRCTable[(crc ^ buf[0 + 1]) & 0xff] ^ (crc >> 8)
                pass
                crc = Globals.CRCTable[(crc ^ buf[0 + 2]) & 0xff] ^ (crc >> 8)
                crc = Globals.CRCTable[(crc ^ buf[0 + 2 + 1]) & 0xff] ^ (crc >> 8)
                pass
                pass
                crc = Globals.CRCTable[(crc ^ buf[0 + 4]) & 0xff] ^ (crc >> 8)
                crc = Globals.CRCTable[(crc ^ buf[0 + 4 + 1]) & 0xff] ^ (crc >> 8)
                pass
                crc = Globals.CRCTable[(crc ^ buf[0 + 4 + 2]) & 0xff] ^ (crc >> 8)
                crc = Globals.CRCTable[(crc ^ buf[0 + 4 + 2 + 1]) & 0xff] ^ (crc >> 8)
                pass
                pass
                pass
                crc = Globals.CRCTable[(crc ^ buf[0 + 8]) & 0xff] ^ (crc >> 8)
                crc = Globals.CRCTable[(crc ^ buf[0 + 8 + 1]) & 0xff] ^ (crc >> 8)
                pass
                crc = Globals.CRCTable[(crc ^ buf[0 + 8 + 2]) & 0xff] ^ (crc >> 8)
                crc = Globals.CRCTable[(crc ^ buf[0 + 8 + 2 + 1]) & 0xff] ^ (crc >> 8)
                pass
                pass
                crc = Globals.CRCTable[(crc ^ buf[0 + 8 + 4]) & 0xff] ^ (crc >> 8)
                crc = Globals.CRCTable[(crc ^ buf[0 + 8 + 4 + 1]) & 0xff] ^ (crc >> 8)
                pass
                crc = Globals.CRCTable[(crc ^ buf[0 + 8 + 4 + 2]) & 0xff] ^ (crc >> 8)
                crc = Globals.CRCTable[(crc ^ buf[0 + 8 + 4 + 2 + 1]) & 0xff] ^ (crc >> 8)

                buf += 16
                len -= 16
                condition = len >= 16

        if 0 != len:
            condition = True
            while condition:
                crc = Globals.CRCTable[(crc ^ buf[0]) & 0xff] ^ (crc >> 8)

                buf += 1
                len -= 1
                condition = len > 0

        crc ^= 0xffffffff
        return crc

    @staticmethod
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Pointer arithmetic is detected on the parameter 'buf':
#ORIGINAL METINII C CODE: uint GetCaseCRC32(const char * buf, size_t len)
    def GetCaseCRC32(buf, len):
        crc = 0xffffffff

        if 16 <= len:
            condition = True
            while condition:
                crc = Globals.CRCTable[(crc ^ UPPER(buf[0])) & 0xff] ^ (crc >> 8)
                crc = Globals.CRCTable[(crc ^ UPPER(buf[0 + 1])) & 0xff] ^ (crc >> 8)
                pass
                crc = Globals.CRCTable[(crc ^ UPPER(buf[0 + 2])) & 0xff] ^ (crc >> 8)
                crc = Globals.CRCTable[(crc ^ UPPER(buf[0 + 2 + 1])) & 0xff] ^ (crc >> 8)
                pass
                pass
                crc = Globals.CRCTable[(crc ^ UPPER(buf[0 + 4])) & 0xff] ^ (crc >> 8)
                crc = Globals.CRCTable[(crc ^ UPPER(buf[0 + 4 + 1])) & 0xff] ^ (crc >> 8)
                pass
                crc = Globals.CRCTable[(crc ^ UPPER(buf[0 + 4 + 2])) & 0xff] ^ (crc >> 8)
                crc = Globals.CRCTable[(crc ^ UPPER(buf[0 + 4 + 2 + 1])) & 0xff] ^ (crc >> 8)
                pass
                pass
                pass
                crc = Globals.CRCTable[(crc ^ UPPER(buf[0 + 8])) & 0xff] ^ (crc >> 8)
                crc = Globals.CRCTable[(crc ^ UPPER(buf[0 + 8 + 1])) & 0xff] ^ (crc >> 8)
                pass
                crc = Globals.CRCTable[(crc ^ UPPER(buf[0 + 8 + 2])) & 0xff] ^ (crc >> 8)
                crc = Globals.CRCTable[(crc ^ UPPER(buf[0 + 8 + 2 + 1])) & 0xff] ^ (crc >> 8)
                pass
                pass
                crc = Globals.CRCTable[(crc ^ UPPER(buf[0 + 8 + 4])) & 0xff] ^ (crc >> 8)
                crc = Globals.CRCTable[(crc ^ UPPER(buf[0 + 8 + 4 + 1])) & 0xff] ^ (crc >> 8)
                pass
                crc = Globals.CRCTable[(crc ^ UPPER(buf[0 + 8 + 4 + 2])) & 0xff] ^ (crc >> 8)
                crc = Globals.CRCTable[(crc ^ UPPER(buf[0 + 8 + 4 + 2 + 1])) & 0xff] ^ (crc >> 8)

                buf += 16
                len -= 16
                condition = len >= 16

        if 0 != len:
            condition = True
            while condition:
                crc = Globals.CRCTable[(crc ^ UPPER(buf[0])) & 0xff] ^ (crc >> 8)

                buf += 1
                len -= 1
                condition = len > 0

        crc ^= 0xffffffff
        return crc

    @staticmethod
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Pointer arithmetic is detected on the parameter 'key':
#ORIGINAL METINII C CODE: uint GetFastHash(const char * key, size_t len)
    def GetFastHash(key, len):
        end = key + len
        h = 0

        while key < end:
            h *= 16777619
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: h ^= *(key++);
            h ^= *(key)
            key += 1

        return (h)


    CRCTable = [0x00000000, 0x77073096, 0xEE0E612C, 0x990951BA, 0x076DC419, 0x706AF48F, 0xE963A535, 0x9E6495A3, 0x0EDB8832, 0x79DCB8A4, 0xE0D5E91E, 0x97D2D988, 0x09B64C2B, 0x7EB17CBD, 0xE7B82D07, 0x90BF1D91, 0x1DB71064, 0x6AB020F2, 0xF3B97148, 0x84BE41DE, 0x1ADAD47D, 0x6DDDE4EB, 0xF4D4B551, 0x83D385C7, 0x136C9856, 0x646BA8C0, 0xFD62F97A, 0x8A65C9EC, 0x14015C4F, 0x63066CD9, 0xFA0F3D63, 0x8D080DF5, 0x3B6E20C8, 0x4C69105E, 0xD56041E4, 0xA2677172, 0x3C03E4D1, 0x4B04D447, 0xD20D85FD, 0xA50AB56B, 0x35B5A8FA, 0x42B2986C, 0xDBBBC9D6, 0xACBCF940, 0x32D86CE3, 0x45DF5C75, 0xDCD60DCF, 0xABD13D59, 0x26D930AC, 0x51DE003A, 0xC8D75180, 0xBFD06116, 0x21B4F4B5, 0x56B3C423, 0xCFBA9599, 0xB8BDA50F, 0x2802B89E, 0x5F058808, 0xC60CD9B2, 0xB10BE924, 0x2F6F7C87, 0x58684C11, 0xC1611DAB, 0xB6662D3D, 0x76DC4190, 0x01DB7106, 0x98D220BC, 0xEFD5102A, 0x71B18589, 0x06B6B51F, 0x9FBFE4A5, 0xE8B8D433, 0x7807C9A2, 0x0F00F934, 0x9609A88E, 0xE10E9818, 0x7F6A0DBB, 0x086D3D2D, 0x91646C97, 0xE6635C01, 0x6B6B51F4, 0x1C6C6162, 0x856530D8, 0xF262004E, 0x6C0695ED, 0x1B01A57B, 0x8208F4C1, 0xF50FC457, 0x65B0D9C6, 0x12B7E950, 0x8BBEB8EA, 0xFCB9887C, 0x62DD1DDF, 0x15DA2D49, 0x8CD37CF3, 0xFBD44C65, 0x4DB26158, 0x3AB551CE, 0xA3BC0074, 0xD4BB30E2, 0x4ADFA541, 0x3DD895D7, 0xA4D1C46D, 0xD3D6F4FB, 0x4369E96A, 0x346ED9FC, 0xAD678846, 0xDA60B8D0, 0x44042D73, 0x33031DE5, 0xAA0A4C5F, 0xDD0D7CC9, 0x5005713C, 0x270241AA, 0xBE0B1010, 0xC90C2086, 0x5768B525, 0x206F85B3, 0xB966D409, 0xCE61E49F, 0x5EDEF90E, 0x29D9C998, 0xB0D09822, 0xC7D7A8B4, 0x59B33D17, 0x2EB40D81, 0xB7BD5C3B, 0xC0BA6CAD, 0xEDB88320, 0x9ABFB3B6, 0x03B6E20C, 0x74B1D29A, 0xEAD54739, 0x9DD277AF, 0x04DB2615, 0x73DC1683, 0xE3630B12, 0x94643B84, 0x0D6D6A3E, 0x7A6A5AA8, 0xE40ECF0B, 0x9309FF9D, 0x0A00AE27, 0x7D079EB1, 0xF00F9344, 0x8708A3D2, 0x1E01F268, 0x6906C2FE, 0xF762575D, 0x806567CB, 0x196C3671, 0x6E6B06E7, 0xFED41B76, 0x89D32BE0, 0x10DA7A5A, 0x67DD4ACC, 0xF9B9DF6F, 0x8EBEEFF9, 0x17B7BE43, 0x60B08ED5, 0xD6D6A3E8, 0xA1D1937E, 0x38D8C2C4, 0x4FDFF252, 0xD1BB67F1, 0xA6BC5767, 0x3FB506DD, 0x48B2364B, 0xD80D2BDA, 0xAF0A1B4C, 0x36034AF6, 0x41047A60, 0xDF60EFC3, 0xA867DF55, 0x316E8EEF, 0x4669BE79, 0xCB61B38C, 0xBC66831A, 0x256FD2A0, 0x5268E236, 0xCC0C7795, 0xBB0B4703, 0x220216B9, 0x5505262F, 0xC5BA3BBE, 0xB2BD0B28, 0x2BB45A92, 0x5CB36A04, 0xC2D7FFA7, 0xB5D0CF31, 0x2CD99E8B, 0x5BDEAE1D, 0x9B64C2B0, 0xEC63F226, 0x756AA39C, 0x026D930A, 0x9C0906A9, 0xEB0E363F, 0x72076785, 0x05005713, 0x95BF4A82, 0xE2B87A14, 0x7BB12BAE, 0x0CB61B38, 0x92D28E9B, 0xE5D5BE0D, 0x7CDCEFB7, 0x0BDBDF21, 0x86D3D2D4, 0xF1D4E242, 0x68DDB3F8, 0x1FDA836E, 0x81BE16CD, 0xF6B9265B, 0x6FB077E1, 0x18B74777, 0x88085AE6, 0xFF0F6A70, 0x66063BCA, 0x11010B5C, 0x8F659EFF, 0xF862AE69, 0x616BFFD3, 0x166CCF45, 0xA00AE278, 0xD70DD2EE, 0x4E048354, 0x3903B3C2, 0xA7672661, 0xD06016F7, 0x4969474D, 0x3E6E77DB, 0xAED16A4A, 0xD9D65ADC, 0x40DF0B66, 0x37D83BF0, 0xA9BCAE53, 0xDEBB9EC5, 0x47B2CF7F, 0x30B5FFE9, 0xBDBDF21C, 0xCABAC28A, 0x53B39330, 0x24B4A3A6, 0xBAD03605, 0xCDD70693, 0x54DE5729, 0x23D967BF, 0xB3667A2E, 0xC4614AB8, 0x5D681B02, 0x2A6F2B94, 0xB40BBE37, 0xC30C8EA1, 0x5A05DF1B, 0x2D02EF8D]

    ## Laniatus Games Studio Inc. | NOTE: The following #define macro was replaced in-line:
    #ORIGINAL METINII C CODE: #define DO1(buf, i) crc = CRCTable[(crc ^ buf[i]) & 0xff] ^ (crc >> 8)
    ## Laniatus Games Studio Inc. | NOTE: The following #define macro was replaced in-line:
    #ORIGINAL METINII C CODE: #define DO2(buf, i) DO1(buf, i); DO1(buf, i + 1);
    ## Laniatus Games Studio Inc. | NOTE: The following #define macro was replaced in-line:
    #ORIGINAL METINII C CODE: #define DO4(buf, i) DO2(buf, i); DO2(buf, i + 2);
    ## Laniatus Games Studio Inc. | NOTE: The following #define macro was replaced in-line:
    #ORIGINAL METINII C CODE: #define DO8(buf, i) DO4(buf, i); DO4(buf, i + 4);
    ## Laniatus Games Studio Inc. | NOTE: The following #define macro was replaced in-line:
    #ORIGINAL METINII C CODE: #define DO16(buf, i) DO8(buf, i); DO8(buf, i + 8);

    ## Laniatus Games Studio Inc. | NOTE: The following #define macro was replaced in-line:
    #ORIGINAL METINII C CODE: #define DO1CI(buf, i) crc = CRCTable[(crc ^ UPPER(buf[i])) & 0xff] ^ (crc >> 8)
    ## Laniatus Games Studio Inc. | NOTE: The following #define macro was replaced in-line:
    #ORIGINAL METINII C CODE: #define DO2CI(buf, i) DO1CI(buf, i); DO1CI(buf, i + 1);
    ## Laniatus Games Studio Inc. | NOTE: The following #define macro was replaced in-line:
    #ORIGINAL METINII C CODE: #define DO4CI(buf, i) DO2CI(buf, i); DO2CI(buf, i + 2);
    ## Laniatus Games Studio Inc. | NOTE: The following #define macro was replaced in-line:
    #ORIGINAL METINII C CODE: #define DO8CI(buf, i) DO4CI(buf, i); DO4CI(buf, i + 4);
    ## Laniatus Games Studio Inc. | NOTE: The following #define macro was replaced in-line:
    #ORIGINAL METINII C CODE: #define DO16CI(buf, i) DO8CI(buf, i); DO8CI(buf, i + 8);



    @staticmethod
    def Trim(str):
        str = str[0:str.find_last_not_of(" \t\r\n") + 1]
        str = str[0:0] + str[0 + str.find_first_not_of(" \t\r\n"):]
        return str

    @staticmethod
    def Lower(original):
        original = original.casefold()
        return original


    @staticmethod
    def Cube_init():
        p_cube = None

        file_name = str(['\0' for _ in range(256+1)])
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        snprintf(file_name, sizeof(file_name), "%s/cube.txt", Globals.LocaleService_GetBasePath())

        Globals.#sys_log(0, "Cube_Init %s", file_name)

        for iter in Globals.s_cube_proto:
            p_cube = *iter
            LG_DEL_MEM(p_cube)

        Globals.s_cube_proto.clear()

        if LGEMiscellaneous.DEFINECONSTANTS.false == Globals.Cube_load(file_name):
            #lani_err("Cube_Init failed")

    @staticmethod
    def Cube_load(file):
        fp = None
        one_line = str(['\0' for _ in range(256)])
        value1 = None
        value2 = None
        delim = " \t\r\n"
        v = None
        token_string = None
        cube_data = None
        cube_value = CUBE_VALUE(0, 0)

        if None == file or None == file[0]:
            return LGEMiscellaneous.DEFINECONSTANTS.false

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((fp = fopen(file, "r")) == 0)
        if (fp = fopen(file, "r")) is None:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        while fgets(one_line, 256, fp):
            value1 = value2 = 0

            if one_line[0] == '#':
                continue

            token_string = strtok(one_line, delim)

            if None == token_string:
                continue

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((v = strtok(NULL, delim)))
            if (v = strtok(None, delim)):
                temp_ref_value1 = RefObject(value1);
                Globals.str_to_number(temp_ref_value1, v)
                value1 = temp_ref_value1.arg_value

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((v = strtok(NULL, delim)))
            if (v = strtok(None, delim)):
                temp_ref_value2 = RefObject(value2);
                Globals.str_to_number(temp_ref_value2, v)
                value2 = temp_ref_value2.arg_value

            TOKEN("section")
                cube_data = LG_NEW_M2 CUBE_DATA
            else:
                TOKEN("npc")
                cube_data.npc_vnum.append(ushort(value1))
            else:
                TOKEN("item")
                cube_value.vnum = uint(value1)
                cube_value.count = int(value2)

                cube_data.item.append(cube_value)
            else:
                TOKEN("reward")
                cube_value.vnum = uint(value1)
                cube_value.count = int(value2)

                cube_data.reward.append(cube_value)
            else:
                TOKEN("percent")
                cube_data.percent = int(value1)
            else:
                TOKEN("gold")
                cube_data.gold = value1
            else:
                TOKEN("end")
                if LGEMiscellaneous.DEFINECONSTANTS.false == Globals.FN_check_cube_data(cube_data):
                    LG_DEL_MEM(cube_data)
                    continue
                Globals.s_cube_proto.append(cube_data)

        fclose(fp)
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    @staticmethod
    def Cube_make(ch):
        npc = None
        percent_number = 0
        cube_proto = None
        items = []
        new_item = None

        if not(ch).IsCubeOpen():
            (ch).ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("The creation screen is not open."))
            return LGEMiscellaneous.DEFINECONSTANTS.false

        npc = ch.GetQuestNPC()
        if None is npc:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        items = ch.GetCubeItem()
        cube_proto = Globals.FN_find_cube(items, npc.GetRaceNum())

        if None is cube_proto:
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Not enough ingredient."))
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if ch.GetGold() < cube_proto.gold:
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Not enough Yang or no space in the inventory."))
            return LGEMiscellaneous.DEFINECONSTANTS.false

        reward_value = cube_proto.reward_value()
        cube_proto.remove_material(ch)

        if 0 < cube_proto.gold:
            ch.PointChange(EPointTypes.LG_POINT_GOLD, -int(cube_proto.gold), LGEMiscellaneous.DEFINECONSTANTS.false, DefineConstants.false)

        percent_number = number(1,100)
        if percent_number<=cube_proto.percent:
            ch.ChatPacket(EChatType.CHAT_TYPE_COMMAND, "cube success %d %d", reward_value.vnum, reward_value.count)
            new_item = ch.AutoGiveItem(reward_value.vnum, reward_value.count)

            LogManager.instance().CubeLog(ch.GetPlayerID(), ch.GetName(LOCALE_LANIATUS), reward_value.vnum, new_item.GetID(), reward_value.count, True)
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
        else:
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("cube failed"))
            ch.ChatPacket(EChatType.CHAT_TYPE_COMMAND, "cube fail")
            LogManager.instance().CubeLog(ch.GetPlayerID(), ch.GetName(LOCALE_LANIATUS), reward_value.vnum, 0, 0, False)
            return LGEMiscellaneous.DEFINECONSTANTS.false

        return LGEMiscellaneous.DEFINECONSTANTS.false

    @staticmethod
    def Cube_clean_item(ch):
        cube_item = []

        cube_item = ch.GetCubeItem()

        for i in range(0, LGEMiscellaneous.DEFINECONSTANTS.CUBE_MAX_NUM):
            if None is cube_item[i]:
                continue

            cube_item[i] = None

    @staticmethod
    def Cube_open(ch):
        if LGEMiscellaneous.DEFINECONSTANTS.false == Globals.s_isInitializedCubeMaterialInformation:
            Globals.Cube_InformationInitialize()

        if None is ch:
            return

        npc = None
        npc = ch.GetQuestNPC()
        if None is npc:
            return

        if Globals.FN_check_valid_npc(npc.GetRaceNum()) == LGEMiscellaneous.DEFINECONSTANTS.false:
            return

        if ch.IsCubeOpen():
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("The creation screen is already open."))
            return
        if ch.GetExchange() is not None or ch.GetMyShop() is not None or ch.GetShopOwner() is not None or ch.IsOpenSafebox() or ch.IsCubeOpen():
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You can't use now."))
            return

        distance = Globals.DISTANCE_APPROX(ch.GetX() - npc.GetX(), ch.GetY() - npc.GetY())

        if distance >= LGEMiscellaneous.DEFINECONSTANTS.CUBE_MAX_DISTANCE:
            #sys_log(1, "CUBE: TOO_FAR: %s distance %d", ch.GetName(LOCALE_LANIATUS), distance)
            return


        Globals.Cube_clean_item(ch)
        ch.SetCubeNpc(npc)
        ch.ChatPacket(EChatType.CHAT_TYPE_COMMAND, "cube open %d", npc.GetRaceNum())

    @staticmethod
    def Cube_close(ch):
        if not(ch).IsCubeOpen():
            return
        Globals.Cube_clean_item(ch)
        ch.SetCubeNpc(None)
        ch.ChatPacket(EChatType.CHAT_TYPE_COMMAND, "cube close")

    @staticmethod
    def Cube_show_list(ch):
        cube_item = []
        item = None

        if not(ch).IsCubeOpen():
            return

        cube_item = ch.GetCubeItem()

        for i in range(0, LGEMiscellaneous.DEFINECONSTANTS.CUBE_MAX_NUM):
            item = cube_item[i]
            if None is item:
                continue

            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, "cube[%d]: inventory[%d]: %s", i, item.GetCell(), item.GetName(LOCALE_LANIATUS))

    @staticmethod
    def Cube_add_item(ch, cube_index, inven_index):
        item = None
        cube_item = []

        if not(ch).IsCubeOpen():
            return

        if inven_index<0 or LGEMiscellaneous.INVENTORY_MAX_NUM<=inven_index:
            return
        if cube_index<0 or LGEMiscellaneous.DEFINECONSTANTS.CUBE_MAX_NUM<=cube_index:
            return

        item = ch.GetInventoryItem(ushort(inven_index))

        if None is item:
            return

        cube_item = ch.GetCubeItem()

        for i in range(0, LGEMiscellaneous.DEFINECONSTANTS.CUBE_MAX_NUM):
            if item is cube_item[i]:
                cube_item[i] = None
                break

## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: cube_item[cube_index] = item;
        cube_item[cube_index].copy_from(item)

        if test_server:
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, "cube[%d]: inventory[%d]: %s added", cube_index, inven_index, item.GetName(LOCALE_LANIATUS))

        Globals.FN_update_cube_status(ch)

        return

    @staticmethod
    def Cube_delete_item(ch, cube_index):
        item = None
        cube_item = []

        if not(ch).IsCubeOpen():
            return

        if cube_index<0 or LGEMiscellaneous.DEFINECONSTANTS.CUBE_MAX_NUM<=cube_index:
            return

        cube_item = ch.GetCubeItem()

        if None is cube_item[cube_index]:
            return

        item = cube_item[cube_index]
        cube_item[cube_index] = None

        if test_server:
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, "cube[%d]: cube[%d]: %s deleted", cube_index, item.GetCell(), item.GetName(LOCALE_LANIATUS))

        Globals.FN_update_cube_status(ch)

        return

    @staticmethod
    def Cube_request_result_list(ch):
        if not(ch).IsCubeOpen():
            return

        npc = ch.GetQuestNPC()
        if None is npc:
            return

        npcVNUM = npc.GetRaceNum()
        resultCount = 0

        resultText = Globals.cube_result_info_map_by_npc[npcVNUM]

        if len(resultText) == 0:
            resultText = ""

            resultList = Globals.cube_info_map[npcVNUM]
            for iter in resultList:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to references to variables:
#ORIGINAL METINII C CODE: const SCubeMaterialInfo& materialInfo = *iter;
                materialInfo = *iter
                temp = str(['\0' for _ in range(128)])
                sprintf(temp, "%d,%d", materialInfo.reward.vnum, materialInfo.reward.count)

                resultText += str(temp) + "/"

            resultCount = len(resultList)
            if resultCount == 0:
                return

            if len(resultText) != 0:
                resultText = resultText[0:len(resultText) - 1]

            resultTextSize = 20 - len(resultText) if len(resultText) < 20 else len(resultText) - 20

            if resultTextSize >= LGEMiscellaneous.CHAT_MAX_LEN:
                #lani_err("[CubeInfo] Too long cube result list text. (NPC: %d, length: %d)", npcVNUM, len(resultText))
                resultText = ""
                resultCount = 0

        ch.ChatPacket(EChatType.CHAT_TYPE_COMMAND, "cube r_list %d %d %s", npcVNUM, resultCount, resultText)

    @staticmethod
    def Cube_request_material_info(ch, requestStartIndex, requestCount = 1):
        if not(ch).IsCubeOpen():
            return

        npc = ch.GetQuestNPC()
        if None is npc:
            return

        npcVNUM = npc.GetRaceNum()
        materialInfoText = ""

        index = 0
        bCatchInfo = LGEMiscellaneous.DEFINECONSTANTS.false

        resultList = Globals.cube_info_map[npcVNUM]
        for iter in resultList:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to references to variables:
#ORIGINAL METINII C CODE: const SCubeMaterialInfo& materialInfo = *iter;
            materialInfo = *iter

## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: if (index++ == requestStartIndex)
            if index == requestStartIndex:
                index += 1
                bCatchInfo = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
            else:
                index += 1

            if bCatchInfo:
                materialInfoText += materialInfo.infoText + "@"

            if index >= requestStartIndex + requestCount:
                break

        if (not bCatchInfo) or len(materialInfoText) == 0:
            #lani_err("[CubeInfo] Can't find matched material info (NPC: %d, index: %d, request count: %d)", npcVNUM, requestStartIndex, requestCount)
            return

        if len(materialInfoText) != 0:
            materialInfoText = materialInfoText[0:len(materialInfoText) - 1]

        materialInfoTextSize = 20 - len(materialInfoText) if len(materialInfoText) < 20 else len(materialInfoText) - 20

        if materialInfoTextSize >= LGEMiscellaneous.CHAT_MAX_LEN:
            #lani_err("[CubeInfo] Too long material info. (NPC: %d, requestStart: %d, requestCount: %d, length: %d)", npcVNUM, requestStartIndex, requestCount, len(materialInfoText))

        ch.ChatPacket(EChatType.CHAT_TYPE_COMMAND, "cube m_info %d %d %s", requestStartIndex, requestCount, materialInfoText)

    @staticmethod
    def Cube_InformationInitialize():
        i = 0
        while i < len(Globals.s_cube_proto):
            cubeData = Globals.s_cube_proto[i]

            rewards = cubeData.reward

            if 1 != len(rewards):
                #lani_err("[CubeInfo] WARNING! Does not support multiple rewards (count: %d)", len(rewards))
                continue

            reward = rewards[0]
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to references to value types:
#ORIGINAL METINII C CODE: const ushort& npcVNUM = cubeData->npc_vnum.at(0);
            npcVNUM = cubeData.npc_vnum[0]
            bComplicate = LGEMiscellaneous.DEFINECONSTANTS.false

            cubeMap = Globals.cube_info_map
            resultList = cubeMap[npcVNUM]
            materialInfo = SCubeMaterialInfo()

## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: materialInfo.reward = reward;
            materialInfo.reward.copy_from(reward)
            materialInfo.gold = cubeData.gold
            materialInfo.material = list(cubeData.item)

            for iter in resultList:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to references to variables:
#ORIGINAL METINII C CODE: SCubeMaterialInfo& existInfo = *iter;
                existInfo = *iter

                if reward.vnum == existInfo.reward.vnum:
                    for existMaterialIter in existInfo.material:
                        existMaterialProto = ITEM_MANAGER.Instance().GetTable(existMaterialIter.vnum)
                        if None is existMaterialProto:
                            #lani_err("There is no item(%u)", existMaterialIter.vnum)
                            return LGEMiscellaneous.DEFINECONSTANTS.false
                        existItemInfo = Globals.SplitItemNameAndLevelFromName(existMaterialProto.szName)

                        if 0 < existItemInfo.level:
                            for currentMaterialIter in materialInfo.material:
                                currentMaterialProto = ITEM_MANAGER.Instance().GetTable(currentMaterialIter.vnum)
                                currentItemInfo = Globals.SplitItemNameAndLevelFromName(currentMaterialProto.szName)

                                if currentItemInfo.name == existItemInfo.name:
                                    bComplicate = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
                                    existInfo.complicateMaterial.append(currentMaterialIter)

                                    if std::find(existInfo.complicateMaterial.begin(), existInfo.complicateMaterial.end(), *existMaterialIter) == existInfo.complicateMaterial.end():
                                        existInfo.complicateMaterial.append(existMaterialIter)

                                    break

            if LGEMiscellaneous.DEFINECONSTANTS.false == bComplicate:
                resultList.append(materialInfo)
            i += 1

        Globals.Cube_MakeCubeInformationText()

        Globals.s_isInitializedCubeMaterialInformation = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))


## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern int test_server

    ## Laniatus Games Studio Inc. | NOTE: The following #define macro was replaced in-line:
    #ORIGINAL METINII C CODE: #define RETURN_IF_CUBE_IS_NOT_OPENED(ch) if (!(ch)->IsCubeOpen()) return

    s_cube_proto = []
    s_isInitializedCubeMaterialInformation = LGEMiscellaneous.DEFINECONSTANTS.false


    cube_info_map = _boost_func_of_void.unordered_map()
    cube_result_info_map_by_npc = _boost_func_of_void.unordered_map()

    @staticmethod
    def FN_check_item_count(items, item_vnum, need_count):
        count = 0

        for i in range(0, LGEMiscellaneous.DEFINECONSTANTS.CUBE_MAX_NUM):
            if None is items[i]:
                continue

            if item_vnum == items[i].GetVnum():
                count += int(items[i].GetCount())

        return (count>=need_count)

    @staticmethod
    def FN_remove_material(items, item_vnum, need_count):
        count = 0
        item = None

        for i in range(0, LGEMiscellaneous.DEFINECONSTANTS.CUBE_MAX_NUM):
            if None is items[i]:
                continue

            item = items[i]
            if item_vnum == item.GetVnum():
                count += int(item.GetCount())

                if count> need_count:
                    item.SetCount(uint(count-need_count))
                    return
                else:
                    item.SetCount(0)
                    items[i] = None

    @staticmethod
    def FN_find_cube(items, npc_vnum):
        i = None
        end_index = None

        if 0==npc_vnum:
            return None

        end_index = len(Globals.s_cube_proto)
        for i in range(0, end_index):
            if Globals.s_cube_proto[i].can_make_item(items, npc_vnum):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
#ORIGINAL METINII C CODE: return s_cube_proto[i];
                return CUBE_DATA(Globals.s_cube_proto[i])

        return None

    @staticmethod
    def FN_check_valid_npc(vnum):
        for iter in Globals.s_cube_proto:
            if std::find(iter.npc_vnum.begin(), iter.npc_vnum.end(), vnum) != iter.npc_vnum.end():
                return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        return LGEMiscellaneous.DEFINECONSTANTS.false

    @staticmethod
    def FN_check_cube_data(cube_data):
        i = 0
        end_index = 0

        end_index = uint(len(cube_data.npc_vnum))
        for i in range(0, end_index):
            if cube_data.npc_vnum[i] == 0:
                return LGEMiscellaneous.DEFINECONSTANTS.false

        end_index = uint(len(cube_data.item))
        for i in range(0, end_index):
            if cube_data.item[i].vnum == 0:
                return LGEMiscellaneous.DEFINECONSTANTS.false
            if cube_data.item[i].count == 0:
                return LGEMiscellaneous.DEFINECONSTANTS.false

        end_index = uint(len(cube_data.reward))
        for i in range(0, end_index):
            if cube_data.reward[i].vnum == 0:
                return LGEMiscellaneous.DEFINECONSTANTS.false
            if cube_data.reward[i].count == 0:
                return LGEMiscellaneous.DEFINECONSTANTS.false
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    @staticmethod
    def FN_update_cube_status(ch):
        if None is ch:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if not ch.IsCubeOpen():
            return LGEMiscellaneous.DEFINECONSTANTS.false

        npc = ch.GetQuestNPC()
        if None is npc:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        cube = Globals.FN_find_cube(ch.GetCubeItem(), npc.GetRaceNum())

        if None is cube:
            ch.ChatPacket(EChatType.CHAT_TYPE_COMMAND, "cube info 0 0 0")
            return LGEMiscellaneous.DEFINECONSTANTS.false

        ch.ChatPacket(EChatType.CHAT_TYPE_COMMAND, "cube info %lld %d %d", cube.gold, 0, 0)
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    @staticmethod
    def SplitItemNameAndLevelFromName(name):
        level = 0
        info = SItemNameAndLevel()
        info.name = name

        pos = name.find("+")

        if -1 != pos:
            levelStr = name[pos + 1:pos + 1 + len(name) - pos - 1]
            temp_ref_level = RefObject(level);
            Globals.str_to_number(temp_ref_level, levelStr)
            level = temp_ref_level.arg_value

            info.name = name[0:pos]

        info.level = level

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
#ORIGINAL METINII C CODE: return info;
        return SItemNameAndLevel(info)

    @staticmethod
    def FIsEqualCubeValue(a, b):
        return (a.vnum == b.vnum) and (a.count == b.count)

    @staticmethod
    def FIsLessCubeValue(a, b):
        return a.vnum < b.vnum

    @staticmethod
    def Cube_MakeCubeInformationText():
        iter = cube_info_map.begin()
        while Globals.cube_info_map.end() is not iter:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to references to value types:
#ORIGINAL METINII C CODE: const uint& npcVNUM = iter->first;
            npcVNUM = iter.first
            resultList = iter.second

            for resultIter in resultList:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to references to variables:
#ORIGINAL METINII C CODE: SCubeMaterialInfo& materialInfo = *resultIter;
                materialInfo = *resultIter
                infoText = materialInfo.infoText

                if 0 < len(materialInfo.complicateMaterial):
                    std::sort(materialInfo.complicateMaterial.begin(), materialInfo.complicateMaterial.end(), FIsLessCubeValue)
                    std::sort(materialInfo.material.begin(), materialInfo.material.end(), FIsLessCubeValue)

                    for iter in materialInfo.complicateMaterial:
                        for targetIter in materialInfo.material:
                            if *targetIter == *iter:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no direct equivalent to the STL vector 'erase' method in Python:
                                targetIter = materialInfo.material.erase(targetIter)

                    for iter in materialInfo.complicateMaterial:
                        tempBuffer = str(['\0' for _ in range(128)])
                        sprintf(tempBuffer, "%d,%d|", iter.vnum, iter.count)

                        infoText += str(tempBuffer)

                    infoText = infoText[0:len(infoText) - 1]

                    if 0 < len(materialInfo.material):
                        infoText.push_back('&')

                for iter in materialInfo.material:
                    tempBuffer = str(['\0' for _ in range(128)])
                    sprintf(tempBuffer, "%d,%d&", iter.vnum, iter.count)
                    infoText += str(tempBuffer)

                infoText = infoText[0:len(infoText) - 1]

                if 0 < materialInfo.gold:
                    temp = str(['\0' for _ in range(128)])
                    sprintf(temp, "%lld", materialInfo.gold)
                    infoText += str("/") + temp
            iter += 1

    QUERY_TYPE_RETURN = 1
    QUERY_TYPE_FUNCTION = 2
    QUERY_TYPE_AFTER_FUNCTION = 3

    QID_SAFEBOX_SIZE = 0
    QID_AUTH_LOGIN = 1
    QID_HIGHSCORE_REGISTER = 3
    QID_HIGHSCORE_SHOW = 4
    QID_BLOCK_CHAT_LIST = 5
    QID_PROTECT_CHILD = 6

    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##if ! _IMPROVED_PACKET_ENCRYPTION_
    ##endif
## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern str g_stBlockDate

## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern uint g_uiSpamReloadCycle

    s_pkReloadSpamEvent = None

    @staticmethod
    def (UnnamedParameter):
        AccountDB.instance().ReturnQuery(EAccountQID.QID_SPAM_DB, 0, None, "SELECT word, score FROM spam_db WHERE type='SPAM'")
        return ((g_uiSpamReloadCycle) * passes_per_sec)

    @staticmethod
    def LoadSpamDB():
        AccountDB.instance().ReturnQuery(EAccountQID.QID_SPAM_DB, 0, None, "SELECT word, score FROM spam_db WHERE type='SPAM'")

        if None is Globals.s_pkReloadSpamEvent:
            info = Globals.AllocEventInfo()
## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: s_pkReloadSpamEvent = event_create_ex(reload_spam_event, info, ((g_uiSpamReloadCycle) * passes_per_sec));
            Globals.s_pkReloadSpamEvent.copy_from(Globals.event_create_ex(reload_spam_event, info, ((g_uiSpamReloadCycle) * passes_per_sec)))

    @staticmethod
    def CancelReloadSpamEvent():
        Globals.s_pkReloadSpamEvent = None



## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern int max_bytes_written
## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern int current_bytes_written
## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern int total_bytes_written

    @staticmethod
    def (UnnamedParameter):
        info = if isinstance(event.info, DESC.desc_event_info) else None

        if info is None:
            #lani_err("ping_event> <Factor> Null pointer")
            return 0

        desc = info.desc

        if not desc.IsPong():
            Globals.#sys_log(0, "PING_EVENT: no pong %s", desc.GetHostName())

            desc.SetPhase(EPhase.PHASE_CLOSE)

            return (ping_event_second_cycle)
        else:
            p = packet_ping()
            p.header = byte(Globals.LG_HEADER_GC_PING)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            desc.Packet(p, sizeof(packet_ping))
            desc.SetPong(LGEMiscellaneous.DEFINECONSTANTS.false)

        desc.SendHandshake(get_dword_time(), 0)

        return (ping_event_second_cycle)

##endif

    @staticmethod
    def (UnnamedParameter):
        info = if isinstance(event.info, DESC.desc_event_info) else None

        if info is None:
            #lani_err("disconnect_event> <Factor> Null pointer")
            return 0

        d = info.desc

        d.m_pkDisconnectEvent = None
        d.SetPhase(EPhase.PHASE_CLOSE)
        return 0

    ## Laniatus Games Studio Inc. | NOTE: This was formerly a static local variable declaration (not allowed in Python):
    GetKey_20050304Myevan_bGenerated = LGEMiscellaneous.DEFINECONSTANTS.false
    ## Laniatus Games Studio Inc. | NOTE: This was formerly a static local variable declaration (not allowed in Python):
    GetKey_20050304Myevan_s_adwKey = [0 for _ in range(1938)]

    @staticmethod
## Laniatus Games Studio Inc. | WARNING: Python has no equivalent to methods returning pointers to value types:
#ORIGINAL METINII C CODE: const byte* GetKey_20050304Myevan()
    def GetKey_20050304Myevan():
        ## Laniatus Games Studio Inc. | NOTE: This static local variable declaration (not allowed in Python) has been moved just prior to the method:
        #    static bool bGenerated = DefineConstants.false
        ## Laniatus Games Studio Inc. | NOTE: This static local variable declaration (not allowed in Python) has been moved just prior to the method:
        #    static uint s_adwKey[1938]

        if not GetKey_20050304Myevan_bGenerated:
            GetKey_20050304Myevan_bGenerated = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
            seed = 1491971513

            i = 0
            while i < int(seed):
                seed ^= 2148941891
                seed += 3592385981

                GetKey_20050304Myevan_s_adwKey[i] = seed
                i += 1

        return byte(int(GetKey_20050304Myevan_s_adwKey))





## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern CLIENT_DESC* db_clientdesc
## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern CLIENT_DESC* g_pkAuthMasterDesc
## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern CLIENT_DESC* g_NetmarbleDBDesc



## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern LPFDWATCH main_fdw

    db_clientdesc = None
    g_pkAuthMasterDesc = None
    g_NetmarbleDBDesc = None

    @staticmethod
    def GetKnownClientDescName(desc):
        if desc is Globals.db_clientdesc:
            return "db_clientdesc"
        elif desc is Globals.g_pkAuthMasterDesc:
            return "g_pkAuthMasterDesc"
        elif desc is Globals.g_NetmarbleDBDesc:
            return "g_NetmarbleDBDesc"
        return "unknown"


    admin_ip = [valid_ip("210.123.10", 128, 128), valid_ip("\n", 0, 0)]

    @staticmethod
    def IsValidIP(ip_table, host):
        i = None
        j = None
        ip_addr = str(['\0' for _ in range(256)])

        i = 0
        while ip_table[i].ip != '\n':
            j = 255 - (ip_table + i).mask

            condition = True
            while condition:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                snprintf(ip_addr, sizeof(ip_addr), "%s.%d", (ip_table + i).ip, (ip_table + i).network + j)

                if not strcmp(ip_addr, host):
                    return 1 if ((not LGEMiscellaneous.DEFINECONSTANTS.false)) else 0

                if j == 0:
                    break
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: } while (j--);
                condition = j
            j -= 1
            i += 1

        return LGEMiscellaneous.DEFINECONSTANTS.false
    DRAGON_SOUL_ADDITIONAL_ATTR_START_IDX = 3

## Laniatus Games Studio Inc. | NOTE: Python has no need of forward class declarations:
    #class CGroupNode
## Laniatus Games Studio Inc. | NOTE: Python has no need of forward class declarations:
    #class CGroupTextParseTreeLoader

    ## Laniatus Games Studio Inc. | WARNING: The following #include directive was ignored:
    ##include <_boost_func_of_void/lexical_cast.hpp>
    g_astGradeName = ["grade_normal", "grade_brilliant", "grade_rare", "grade_ancient", "grade_legendary", "grade_myth"]

    g_astStepName = ["step_lowest", "step_low", "step_mid", "step_high", "step_highest"]

    g_astMaterialName = ["material_leather", "material_blood", "material_root", "material_needle", "material_jewel", "material_ds_refine_normal", "material_ds_refine_blessed", "material_ds_refine_holly"]




## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern int passes_per_sec

    @staticmethod
    def (UnnamedParameter):
        pInfo = if isinstance(event.info, tag_DragonLair_Collapse_EventInfo) else None

        if pInfo is None:
            #lani_err("DragonLair_Collapse_Event> <Factor> Null pointer")
            return 0

        if 0 == pInfo.step:
            buf = str(['\0' for _ in range(512)])
            snprintf(buf, 512, LC_TEXT("You managed to defeat the dragon in %d seconds!"), pInfo.pLair.GetEstimatedTime())
            Globals.SendNoticeMap(buf, pInfo.InstanceMapIndex, ((not LGEMiscellaneous.DEFINECONSTANTS.false)))

            pInfo.step += 1

            return ((30) * passes_per_sec)
        elif 1 == pInfo.step:
            pMap = SECTREE_MANAGER.instance().GetMap(pInfo.InstanceMapIndex)

            if None is not pMap:
                f = FWarpToVillage()
                pMap.for_each(f.functor_method)

            pInfo.step += 1

            return ((30) * passes_per_sec)
        else:
            SECTREE_MANAGER.instance().DestroyPrivateMap(pInfo.InstanceMapIndex)
            LG_DEL_MEM(pInfo.pLair)

        return 0



    ## Laniatus Games Studio Inc. | WARNING: The following #include directive was ignored:
    ##include <_boost_func_of_void/lexical_cast.hpp>


    @staticmethod
    def Gamble(vec_probs):
        range = 0.0
        i = 0
        while i < len(vec_probs):
            range += vec_probs[i]
            i += 1
        fProb = fnumber(0.0, range)
        sum = 0.0
        idx = 0
        while idx < len(vec_probs):
            sum += vec_probs[idx]
            if sum >= fProb:
                return idx
            idx += 1
        return -1

    @staticmethod
    def MakeDistinctRandomNumberSet(prob_lst, random_set):
        size = prob_lst.size()
        n = len(random_set)
        if size < n:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        select_bit = [0 for _ in range(size)]
        for i in range(0, n):
            range = 0.0
            it = prob_lst.begin()
            while it is not prob_lst.end():
                range += *it
                it += 1
            r = fnumber(0.0, range)
            sum = 0.0
            idx = 0
            it = prob_lst.begin()
            while it is not prob_lst.end():
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: while (select_bit[idx++]);
                while (select_bit[idx]) != 0:
                    idx += 1
                    pass
                idx += 1

                sum += *it
                if sum >= r:
                    select_bit[idx - 1] = 1
                    random_set[i] = idx - 1
                    prob_lst.erase(it)
                    break
                it += 1
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    @staticmethod
    def GetType(dwVnum):
        return (math.trunc(dwVnum / float(10000)))

    @staticmethod
    def GetGradeIdx(dwVnum):
        return math.fmod((math.trunc(dwVnum / float(1000))), 10)

    @staticmethod
    def GetStepIdx(dwVnum):
        return math.fmod((math.trunc(dwVnum / float(100))), 10)

    @staticmethod
    def GetStrengthIdx(dwVnum):
        return math.fmod((math.trunc(dwVnum / float(10))), 10)

    @staticmethod
    def IsDragonSoulRefineMaterial(pItem):
        if pItem.GetType() != EItemTypes.ITEM_MATERIAL:
            return LGEMiscellaneous.DEFINECONSTANTS.false
        return (pItem.GetSubType() == EMaterialSubTypes.MATERIAL_DS_REFINE_NORMAL or pItem.GetSubType() == EMaterialSubTypes.MATERIAL_DS_REFINE_BLESSED or pItem.GetSubType() == EMaterialSubTypes.MATERIAL_DS_REFINE_HOLLY)


    @staticmethod
    def (UnnamedParameter):
        info = if isinstance(event.info, dungeon_id_info) else None

        if info is None:
            #lani_err("dungeon_dead_event> <Factor> Null pointer")
            return 0

        pDungeon = CDungeonManager.instance().Find(info.dungeon_id)
        if pDungeon is None:
            return 0

        pDungeon.deadEvent = None

        CDungeonManager.instance().Destroy(info.dungeon_id)
        return 0

    @staticmethod
    def (UnnamedParameter):
        info = if isinstance(event.info, dungeon_id_info) else None

        if info is None:
            #lani_err("dungeon_jump_to_event> <Factor> Null pointer")
            return 0

        pDungeon = CDungeonManager.instance().Find(info.dungeon_id)
        pDungeon.jump_to_event_ = None

        if pDungeon:
            pDungeon.JumpToEliminateLocation()
        else:
            #lani_err("cannot find dungeon with map index %u", info.dungeon_id)

        return 0

    @staticmethod
    def (UnnamedParameter):
        info = if isinstance(event.info, dungeon_id_info) else None

        if info is None:
            #lani_err("dungeon_exit_all_event> <Factor> Null pointer")
            return 0

        pDungeon = CDungeonManager.instance().Find(info.dungeon_id)
        pDungeon.exit_all_event_ = None

        if pDungeon:
            pDungeon.ExitAll()

        return 0
    @staticmethod
    def LoadEmpireTextConvertTable(dwEmpireID, c_szFileName):
        if dwEmpireID < 1 or dwEmpireID > 3:
            return DefineConstants.false

        fp = fopen(c_szFileName, "rb")

        if fp is None:
            return DefineConstants.false

        dwEngCount = 26
        dwHanCount = uint((0xC8 - 0xB0+1) * (0xFE - 0xA1+1))
        dwHanSize = dwHanCount * 2

        rkTextConvTable = Globals.g_aTextConvTable[dwEmpireID-1]

        fread(rkTextConvTable.acUpper, 1, dwEngCount, fp)
        fread(rkTextConvTable.acLower, 1, dwEngCount, fp)
        fread(rkTextConvTable.aacHan, 1, dwHanSize, fp)

        fread(rkTextConvTable.aacJaum, 1, 60, fp)
        fread(rkTextConvTable.aacMoum, 1, 42, fp)

        fclose(fp)

        return ((not DefineConstants.false))

    @staticmethod
    def ConvertEmpireText(dwEmpireID, szText, len, iPct):
        if dwEmpireID < 1 or dwEmpireID > 3 or len == 0:
            return

        rkTextConvTable = Globals.g_aTextConvTable[dwEmpireID - 1]

        pbText = reinterpret_cast<byte*>(szText)
        while len > 0 and *pbText != '\0':
            if number(1,100) > iPct:
                if (*pbText & 0x80) != 0:
                        if pbText[0] >= 0xB0 and pbText[0] <= 0xC8 and pbText[1] >= 0xA1 and pbText[1] <= 0xFE:
                            uHanPos = (pbText[0] - 0xB0) * (0xFE - 0xA1 + 1) + (pbText[1] - 0xA1)
                            pbText[0] = rkTextConvTable.aacHan[uHanPos][0]
                            pbText[1] = rkTextConvTable.aacHan[uHanPos][1]
                        elif pbText[0] == 0xA4:
                            if pbText[1] >= 0xA1 and pbText[1] <= 0xBE:
                                pbText[0] = rkTextConvTable.aacJaum[pbText[1] - 0xA1][0]
                                pbText[1] = rkTextConvTable.aacJaum[pbText[1] - 0xA1][1]
                            elif pbText[1] >= 0xBF and pbText[1] <= 0xD3:
                                pbText[0] = rkTextConvTable.aacMoum[pbText[1] - 0xBF][0]
                                pbText[1] = rkTextConvTable.aacMoum[pbText[1] - 0xBF][1]
                    pbText += 1
                    len -= 1
                else:
                    if *pbText >= 'a' and *pbText <= 'z':
                        *pbText = rkTextConvTable.acLower[*pbText - 'a']
                    elif *pbText >= 'A' and *pbText <= 'Z':
                        *pbText = rkTextConvTable.acUpper[*pbText - 'A']
            else:
                if (*pbText & 0x80) != 0:
                    pbText += 1
                    len -= 1
            len -= 1
            pbText += 1
    g_aTextConvTable = [STextConvertTable() for _ in range(3)]



    @staticmethod
    def intrusive_ptr_add_ref(p):
        ++(p.ref_count)

    @staticmethod
    def intrusive_ptr_release(p):
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: if (--(p->ref_count) == 0)
        if (p.ref_count) == 0:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if -= 1;
            if -= 1
            LG_DEL_MEM(p)
        else:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if -= 1;
            if -= 1

    @staticmethod
    def AllocEventInfo():
        return LG_NEW_M2 T

    @staticmethod
    def event_destroy():
        pElem = None

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: while ((pElem = cxx_q.Dequeue()))
        while (pElem = Globals.cxx_q.Dequeue()):
            the_event = pElem.pvData

            if not pElem.bCancel:
                pass

            Globals.cxx_q.Delete(pElem)

    @staticmethod
    def event_process(pulse):
        new_time = None
        num_events = 0

        while pulse >= Globals.cxx_q.GetTopKey():
            pElem = Globals.cxx_q.Dequeue()

            if pElem.bCancel:
                Globals.cxx_q.Delete(pElem)
                continue

            new_time = pElem.iKey

            the_event = pElem.pvData
            processing_time = Globals.event_processing_time(_boost_func_of_void.intrusive_ptr(the_event))
            Globals.cxx_q.Delete(pElem)

            the_event.is_processing = ((not DefineConstants.false))

            if not the_event.info:
                the_event.q_el = None
                Globals.ContinueOnFatalError()
            else:
                new_time = (Globals.get_pointer(_boost_func_of_void.intrusive_ptr(the_event)), processing_time)

                if new_time <= 0 or the_event.is_force_to_end:
                    the_event.q_el = None
                else:
                    the_event.q_el = Globals.cxx_q.Enqueue(_boost_func_of_void.intrusive_ptr(the_event), new_time, pulse)
                    the_event.is_processing = DefineConstants.false

            num_events += 1

        return num_events

    @staticmethod
    def event_count():
        return Globals.cxx_q.Size()

    ## Laniatus Games Studio Inc. | NOTE: The following #define macro was replaced in-line:
    #ORIGINAL METINII C CODE: #define event_create(func, info, when) event_create_ex(func, info, when)
    @staticmethod
    def event_create_ex(func, info, when):
        new_event = None

        if when < 1:
            when = 1

        new_event = LG_NEW_M2 event
        assert None is not new_event

        new_event.func = func
        new_event.info = info
        new_event.q_el = Globals.cxx_q.Enqueue(_boost_func_of_void.intrusive_ptr(new_event), when, thecore_heart.pulse)
        new_event.is_processing = DefineConstants.false
        new_event.is_force_to_end = DefineConstants.false

        return (new_event)

    @staticmethod
    def event_cancel(ppevent):
        event = _boost_func_of_void.intrusive_ptr()

        if ppevent is None:
            #lani_err("null pointer")
            return

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if (!(event = *ppevent))
        if not(event = ppevent):
            return

        if event.is_processing:
            event.is_force_to_end = ((not DefineConstants.false))

            if event.q_el:
                event.q_el.bCancel = ((not DefineConstants.false))

            ppevent = None
            return

        if not event.q_el:
            ppevent = None
            return

        if event.q_el.bCancel:
            ppevent = None
            return

        event.q_el.bCancel = ((not DefineConstants.false))

        ppevent = None

    @staticmethod
    def event_processing_time(event):
        start_time = None

        if not event.q_el:
            return 0

        start_time = event.q_el.iStartTime
        return (thecore_heart.pulse - start_time)

    @staticmethod
    def event_time(event):
        when = None

        if not event.q_el:
            return 0

        when = event.q_el.iKey
        return (when - thecore_heart.pulse)

    @staticmethod
    def event_reset_time(event, when):
        if not event.is_processing:
            if event.q_el:
                event.q_el.bCancel = ((not DefineConstants.false))

            event.q_el = Globals.cxx_q.Enqueue(_boost_func_of_void.intrusive_ptr(event), when, thecore_heart.pulse)

# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
    #ContinueOnFatalError()
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
    #ShutdownOnFatalError()
    cxx_q = CEventQueue()



    @staticmethod
    def exchange_packet(ch, sub_header, is_me, arg1, arg2, arg3, pvData = None):
        if ch.GetDesc() is None:
            return

        pack_exchg = packet_exchange()

        pack_exchg.header = byte(Globals.LG_HEADER_GC_EXCHANGE)
        pack_exchg.sub_header = sub_header
        pack_exchg.is_me = 1 if is_me else 0
        pack_exchg.arg1 = arg1
        pack_exchg.arg2 = arg2
        pack_exchg.arg3 = arg3

        if sub_header == EPacketTradeSubHeaders.EXCHANGE_SUBLG_HEADER_GC_ITEM_ADD and pvData:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memcpy' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            memcpy(pack_exchg.alSockets, (pvData).GetSockets(), sizeof(pack_exchg.alSockets))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memcpy' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            memcpy(pack_exchg.aAttr, (pvData).GetAttributes(), sizeof(pack_exchg.aAttr))
        else:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            memset(pack_exchg.alSockets, 0, sizeof(pack_exchg.alSockets))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            memset(pack_exchg.aAttr, 0, sizeof(pack_exchg.aAttr))

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        ch.GetDesc().Packet(pack_exchg, sizeof(pack_exchg))
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
    #gm_insert(name, level)
    @staticmethod
    def gm_get_level(name, host = None, account = None):
        return Globals.gm_new_get_level(name, host, account)

# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
    #gm_host_insert(host)
    @staticmethod
    def gm_new_clear():
        Globals.g_set_Host.clear()
        Globals.g_map_GM.clear()

    @staticmethod
    def gm_new_insert(rAdminInfo):
        #sys_log(0, "InsertGMList(account:%s, player:%s, contact_ip:%s, server_ip:%s, auth:%d)", rAdminInfo.m_szAccount, rAdminInfo.m_szName, rAdminInfo.m_szContactIP, rAdminInfo.m_szServerIP, rAdminInfo.m_Authority)

        t = tGM()

        if strlen(rAdminInfo.m_szContactIP) == 0:
            t.pset_Host = Globals.g_set_Host
            #sys_log(0, "GM Use ContactIP")
        else:
            t.pset_Host = None
            #sys_log(0, "GM Use Default Host List")

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memcpy' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memcpy(t.Info, rAdminInfo, sizeof(rAdminInfo))

        Globals.g_map_GM[rAdminInfo.m_szName] = t


    @staticmethod
    def gm_new_host_inert(host):
        Globals.g_set_Host.insert(host)
        Globals.#sys_log(0, "InsertGMHost(ip:%s)", host)


## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern int test_server

    g_set_Host = std::set()
    g_map_GM = {}

    @staticmethod
    def gm_new_get_level(name, host, account):
        if test_server:
            return EGMLevels.GM_IMPLEMENTOR

        it = Globals.g_map_GM.find(name)

        if Globals.g_map_GM.end() is it:
            return EGMLevels.GM_PLAYER
            if account != '\0':
                if strcmp(it.second.Info.m_szAccount, account) != 0:
                    #sys_log(0, "GM_NEW_GET_LEVEL : BAD ACCOUNT [ACCOUNT:%s/%s", it.second.Info.m_szAccount, account)
                    return EGMLevels.GM_PLAYER
            #sys_log(0, "GM_NEW_GET_LEVEL : FIND ACCOUNT")
            return it.second.Info.m_Authority

        return EGMLevels.GM_PLAYER


    @staticmethod
    def from_string(t, s):
        iss = std::istringstream(s)
        return not(iss >> t).fail()

    @staticmethod
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: C++ template specialization was removed by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: inline bool from_string <byte>(byte& t, const str& s)
    def from_string(t, s):
        iss = std::istringstream(s)
        temp = None
        b = not(iss >> temp).fail()
        t.arg_value = byte(int(temp))
        return b



    GUILD_GRADE_NAME_MAX_LEN = 8
    GUILD_GRADE_COUNT = 15
    GUILD_COMMENT_MAX_COUNT = 12
    GUILD_COMMENT_MAX_LEN = 50
    GUILD_LEADER_GRADE = 1
    GUILD_BASE_POWER = 400
    GUILD_POWER_PER_LG_SKILL_LEVEL = 200
    GUILD_POWER_PER_LEVEL = 100
    GUILD_MINIMUM_LEADERSHIP = 40
    GUILD_WAR_MIN_MEMBER_COUNT = 8
    GUILD_LADDER_LG_POINT_PER_LEVEL = 1000
    GUILD_CREATE_ITEM_VNUM = 70101
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##pragma pack()

    GUILD_AUTH_ADD_MEMBER = (1 << 0)
    GUILD_AUTH_REMOVE_MEMBER = (1 << 1)
    GUILD_AUTH_NOTICE = (1 << 2)
    GUILD_AUTH_USE_SKILL = (1 << 3)

    @staticmethod
    def __guild_levelup_exp(level):
        return guild_exp_table[level]

    @staticmethod
    def (UnnamedParameter):
        pInfo = if isinstance(event.info, TInviteGuildEventInfo) else None

        if pInfo is None:
            #lani_err("GuildInviteEvent> <Factor> Null pointer")
            return 0

        pGuild = CGuildManager.instance().FindGuild(pInfo.dwGuildID)

        if pGuild:
            Globals.#sys_log(0, "GuildInviteEvent %s", pGuild.GetName())
            pGuild.InviteDeny(pInfo.dwInviteePID)

        return 0



    @staticmethod
    def SendGuildWarScore(dwGuild, dwGuildOpp, iDelta, iBetScoreDelta = 0):
        p = SPacketGuildWarScore()

        p.dwGuildGainPoint = dwGuild
        p.dwGuildOpponent = dwGuildOpp
        p.lScore = iDelta
        p.lBetScore = iBetScoreDelta

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        db_clientdesc.DBPacket(Globals.LG_HEADER_GD_GUILD_WAR_SCORE, 0, p, sizeof(SPacketGuildWarScore))
        #sys_log(0, "SendGuildWarScore %u %u %d", dwGuild, dwGuildOpp, iDelta)

    @staticmethod
    def SendGuildWarOverNotice(g1, g2, bDraw):
        if g1 is not None and g2 is not None:
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##if __MULTI_LANGUAGE_SYSTEM__
            if bDraw:
                SendNotice(LC_TEXT("The war between the %s Guild and the %s Guild is a draw."), g1.GetName(), g2.GetName())
            else:
                if g1.GetWarScoreAgainstTo(g2.GetID()) > g2.GetWarScoreAgainstTo(g1.GetID()):
                    SendNotice(LC_TEXT("The %s Guild has won the war against the %s Guild."), g1.GetName(), g2.GetName())
                else:
                    SendNotice(LC_TEXT("The %s Guild has won the war against the %s Guild."), g2.GetName(), g1.GetName())
    ##else
            buf = str(['\0' for _ in range(256)])

            if bDraw:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                snprintf(buf, sizeof(buf), LC_TEXT("The war between the %s Guild and the %s Guild is a draw."), g1.GetName(), g2.GetName())
            else:
                if g1.GetWarScoreAgainstTo(g2.GetID()) > g2.GetWarScoreAgainstTo(g1.GetID()):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                    snprintf(buf, sizeof(buf), LC_TEXT("The %s Guild has won the war against the %s Guild."), g1.GetName(), g2.GetName())
                else:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                    snprintf(buf, sizeof(buf), LC_TEXT("The %s Guild has won the war against the %s Guild."), g2.GetName(), g1.GetName())

            Globals.SendNotice(buf)
    ##endif


    GUILD_WAR_WAIT_START_DURATION = 10 *60

    @staticmethod
    def GuildWar_GetTypeInfo(type):
        return KOR_aGuildWarInfo[type]

    @staticmethod
    def GuildWar_GetTypeMapIndex(type):
        return uint(Globals.GuildWar_GetTypeInfo(type).lMapIndex)

    @staticmethod
    def GuildWar_IsWarMap(type):
        if type == EGuildWarType.GUILD_WAR_TYPE_FIELD:
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        mapIndex = Globals.GuildWar_GetTypeMapIndex(type)

        if SECTREE_MANAGER.instance().GetMapRegion(int(mapIndex)):
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        return LGEMiscellaneous.DEFINECONSTANTS.false

# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
    #map_allow_log()
    HORSE_MAX_LEVEL = 30

## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern THorseStat c_aHorseStat[HORSE_MAX_LEVEL+1]


    HORSE_HEALTH_DROP_INTERVAL = 3 * 24 * 60 * 60
    HORSE_STAMINA_CONSUME_INTERVAL = 6 * 60
    HORSE_STAMINA_REGEN_INTERVAL = 12 * 60

    c_aHorseStat = [THorseStat(0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0), THorseStat(25, 20101, 3, 4, 26, 35, 18, 9, 54, 43, 64, 32), THorseStat(25, 20101, 4, 4, 27, 36, 18, 9, 55, 44, 66, 33), THorseStat(25, 20101, 5, 5, 28, 38, 19, 9, 56, 44, 67, 33), THorseStat(25, 20101, 7, 5, 29, 39, 19, 10, 57, 45, 68, 34), THorseStat(25, 20101, 8, 6, 30, 40, 20, 10, 58, 46, 69, 34), THorseStat(25, 20101, 9, 6, 31, 41, 21, 10, 59, 47, 70, 35), THorseStat(25, 20101, 11, 7, 32, 42, 21, 11, 60, 48, 72, 36), THorseStat(25, 20101, 12, 7, 33, 44, 22, 11, 61, 48, 73, 36), THorseStat(25, 20101, 13, 8, 34, 45, 22, 11, 62, 49, 74, 37), THorseStat(25, 20101, 15, 10, 35, 46, 23, 12, 63, 50, 75, 37), THorseStat(35, 20104, 18, 30, 40, 53, 27, 13, 69, 55, 82, 41), THorseStat(35, 20104, 19, 35, 41, 54, 27, 14, 70, 56, 84, 42), THorseStat(35, 20104, 21, 40, 42, 56, 28, 14, 71, 56, 85, 42), THorseStat(35, 20104, 22, 50, 43, 57, 28, 14, 72, 57, 86, 43), THorseStat(35, 20104, 24, 55, 44, 58, 29, 15, 73, 58, 87, 43), THorseStat(35, 20104, 25, 60, 44, 59, 30, 15, 74, 59, 88, 44), THorseStat(35, 20104, 27, 65, 45, 60, 30, 15, 75, 60, 90, 45), THorseStat(35, 20104, 28, 70, 46, 62, 31, 15, 76, 60, 91, 45), THorseStat(35, 20104, 30, 80, 47, 63, 31, 16, 77, 61, 92, 46), THorseStat(35, 20104, 32, 100, 48, 64, 32, 16, 78, 62, 93, 46), THorseStat(50, 20107, 35, 120, 53, 71, 36, 18, 84, 67, 100, 50), THorseStat(50, 20107, 36, 125, 55, 74, 37, 18, 86, 68, 103, 51), THorseStat(50, 20107, 37, 130, 57, 76, 38, 19, 88, 70, 105, 52), THorseStat(50, 20107, 38, 135, 59, 78, 39, 20, 90, 72, 108, 54), THorseStat(50, 20107, 40, 140, 60, 80, 40, 20, 91, 72, 109, 54), THorseStat(50, 20107, 42, 145, 61, 81, 40, 20, 92, 73, 110, 55), THorseStat(50, 20107, 44, 150, 62, 83, 42, 21, 94, 75, 112, 56), THorseStat(50, 20107, 46, 160, 63, 84, 42, 21, 95, 76, 114, 57), THorseStat(50, 20107, 48, 170, 65, 87, 43, 22, 97, 77, 116, 58), THorseStat(50, 20107, 50, 200, 67, 89, 45, 22, 99, 79, 118, 59)]

    @staticmethod
    def (UnnamedParameter):
        info = if isinstance(event.info, horserider_info) else None

        if info is None:
            #lani_err("horse_stamina_consume_event> <Factor> Null pointer")
            return 0

        hr = info.hr

        if hr.GetHorseHealth() <= 0:
            hr.m_eventStaminaConsume = None
            return 0

        hr.UpdateHorseStamina(-1)
        hr.UpdateRideTime(Globals.HORSE_STAMINA_CONSUME_INTERVAL)

        delta = ((Globals.HORSE_STAMINA_CONSUME_INTERVAL) * passes_per_sec)

        if hr.GetHorseStamina() == 0:
            hr.m_eventStaminaConsume = None
            delta = 0

        hr.CheckHorseHealthDropTime()
        Globals.#sys_log(0, "HORSE STAMINA - %p", Globals.get_pointer(event))
        return delta

    @staticmethod
    def (UnnamedParameter):
        info = if isinstance(event.info, horserider_info) else None

        if info is None:
            #lani_err("horse_stamina_regen_event> <Factor> Null pointer")
            return 0

        hr = info.hr

        if hr.GetHorseHealth()<=0:
            hr.m_eventStaminaRegen = None
            return 0

        hr.UpdateHorseStamina(+1)
        delta = ((Globals.HORSE_STAMINA_REGEN_INTERVAL) * passes_per_sec)
        if hr.GetHorseStamina() == hr.GetHorseMaxStamina():
            delta = 0
            hr.m_eventStaminaRegen = None

        hr.CheckHorseHealthDropTime()
        Globals.#sys_log(0, "HORSE STAMINA + %p", Globals.get_pointer(event))


        return delta


    INPROC_CLOSE = 0
    INPROC_HANDSHAKE = 1
    INPROC_LOGIN = 2
    INPROC_MAIN = 3
    INPROC_DEAD = 4
    INPROC_DB = 5
    INPROC_UDP = 6
    INPROC_P2P = 7
    INPROC_AUTH = 8

    @staticmethod
    def LoginFailure(d, c_pszStatus):
        if d is None:
            return

        failurePacket = packet_login_failure()

        failurePacket.header = byte(Globals.LG_HEADER_GC_LOGIN_FAILURE)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        strncpy_s(failurePacket.szStatus, sizeof(failurePacket.szStatus), c_pszStatus, _TRUNCATE)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        d.Packet(failurePacket, sizeof(failurePacket))


# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
    #get_global_time()


    g_sim = {}
    g_simByPID = {}
    g_vec_save = []

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following statement was not recognized, possibly due to an unrecognized macro:
    void(do_block_chat)(CHARACTER* ch, const char *argument, int cmd, int subcmd)



## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern byte g_bAuthServer
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
    #gm_insert(name, level)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
    #gm_get_level(name, host, account)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
    #gm_host_insert(host)


    @staticmethod
    def GetServerLocation(rTab, bEmpire):
        bFound = LGEMiscellaneous.DEFINECONSTANTS.false

        i = 0
        while i < LGEMiscellaneous.PLAYER_PER_ACCOUNT:
            if 0 == rTab.players[i].dwID:
                continue

            bFound = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
            lIndex = 0

            temp_ref_lIndex = RefObject(lIndex);
            if not CMapLocation.instance().Get(rTab.players[i].x, rTab.players[i].y, temp_ref_lIndex, rTab.players[i].lAddr, rTab.players[i].wPort):
                lIndex = temp_ref_lIndex.arg_value
                #lani_err("location error name %s mapindex %d %d x %d empire %d", rTab.players[i].szName, lIndex, rTab.players[i].x, rTab.players[i].y, rTab.bEmpire)

                rTab.players[i].x = int(Globals.EMPIRE_START_X(rTab.bEmpire))
                rTab.players[i].y = int(Globals.EMPIRE_START_Y(rTab.bEmpire))

                lIndex = 0

                temp_ref_lIndex2 = RefObject(lIndex);
                if not CMapLocation.instance().Get(rTab.players[i].x, rTab.players[i].y, temp_ref_lIndex2, rTab.players[i].lAddr, rTab.players[i].wPort):
                    lIndex = temp_ref_lIndex2.arg_value
                    #lani_err("cannot find server for mapindex %d %d x %d (name %s)", lIndex, rTab.players[i].x, rTab.players[i].y, rTab.players[i].szName)

                    continue
                else:
                    lIndex = temp_ref_lIndex2.arg_value
            else:
                lIndex = temp_ref_lIndex.arg_value

            in_ = in_addr()
            in_.s_addr = rTab.players[i].lAddr
            #sys_log(0, "success to %s:%d", inet_ntoa(in_), rTab.players[i].wPort)
            i += 1

        return bFound

## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern dict<uint, CLoginSim *> g_sim
## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern dict<uint, CLoginSim *> g_simByPID

    @staticmethod
    def (UnnamedParameter):
        info = if isinstance(event.info, quest_login_event_info) else None

        if info is None:
            #lani_err("quest_login_event> <Factor> Null pointer")
            return 0

        dwPID = info.dwPID

        ch = CHARACTER_MANAGER.instance().FindByPID(dwPID)

        if ch is None:
            return 0

        d = ch.GetDesc()

        if d is None:
            return 0

        if d.IsPhase(EPhase.PHASE_HANDSHAKE) or d.IsPhase(EPhase.PHASE_LOGIN) or d.IsPhase(EPhase.PHASE_SELECT) or d.IsPhase(EPhase.PHASE_DEAD) or d.IsPhase(EPhase.PHASE_LOADING):
            return ((1) * passes_per_sec)
        elif d.IsPhase(EPhase.PHASE_CLOSE):
            return 0
        elif d.IsPhase(EPhase.PHASE_GAME):
            Globals.#sys_log(0, "QUEST_LOAD: Login pc %d by event", ch.GetPlayerID())
            quest.CQuestManager.instance().Login(ch.GetPlayerID(), NULL)
            return 0
        else:
            #lani_err(0, "input_db.cpp:quest_login_event INVALID PHASE pid %d", ch.GetPlayerID())
            return 0
    @staticmethod
    def _send_bonus_info(ch):
        item_drop_bonus = 0
        gold_drop_bonus = 0
        gold10_drop_bonus = 0
        exp_bonus = 0

        item_drop_bonus = CPrivManager.instance().GetPriv(ch, EPrivType.PRIV_ITEM_DROP)
        gold_drop_bonus = CPrivManager.instance().GetPriv(ch, EPrivType.PRIV_GOLD_DROP)
        gold10_drop_bonus = CPrivManager.instance().GetPriv(ch, EPrivType.PRIV_GOLD10_DROP)
        exp_bonus = CPrivManager.instance().GetPriv(ch, EPrivType.PRIV_EXP_PCT)

        if item_drop_bonus != 0:
            ch.ChatPacket(EChatType.CHAT_TYPE_NOTICE, LC_TEXT("The Item drop ratio is increased by %d%% because of your luck."), item_drop_bonus)
        if gold_drop_bonus != 0:
            ch.ChatPacket(EChatType.CHAT_TYPE_NOTICE, LC_TEXT("The Yang drop ratio is increased by %d%% because of your luck."), gold_drop_bonus)
        if gold10_drop_bonus != 0:
            ch.ChatPacket(EChatType.CHAT_TYPE_NOTICE, LC_TEXT("The Yang drop ratio is increased by %d%% because of your luck "), gold10_drop_bonus)
        if exp_bonus != 0:
            ch.ChatPacket(EChatType.CHAT_TYPE_NOTICE, LC_TEXT("The Experience point ratio is increased by %d%% because of your luck."), exp_bonus)

    @staticmethod
    def FN_is_battle_zone(ch):
        if (ch.GetMapIndex() == 1) or (ch.GetMapIndex() == 2) or (ch.GetMapIndex() == 21) or (ch.GetMapIndex() == 23) or (ch.GetMapIndex() == 41) or (ch.GetMapIndex() == 43) or (ch.GetMapIndex() == 113):
            return LGEMiscellaneous.DEFINECONSTANTS.false

        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    @staticmethod
    def NewPlayerTable(table, name, job, shape, bEmpire, bCon, bInt, bStr, bDex):
        if job >= EJobs.JOB_MAX_NUM:
            return LGEMiscellaneous.DEFINECONSTANTS.false

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memset(table, 0, sizeof(SPlayerTable))

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        strncpy_s(table.name, sizeof(table.name), name, _TRUNCATE)

        table.level = 1
        table.job = job
        table.voice = 0
        table.part_base = shape

        table.st = JobInitialPoints[job].st
        table.dx = JobInitialPoints[job].dx
        table.ht = JobInitialPoints[job].ht
        table.iq = JobInitialPoints[job].iq

        table.hp = JobInitialPoints[job].max_hp + table.ht * JobInitialPoints[job].hp_per_ht
        table.sp = JobInitialPoints[job].max_sp + table.iq * JobInitialPoints[job].sp_per_iq
        table.stamina = JobInitialPoints[job].max_stamina

        table.x = Globals.CREATE_START_X(bEmpire) + number(-300, 300)
        table.y = Globals.CREATE_START_Y(bEmpire) + number(-300, 300)
        table.z = 0
        table.dir = 0
        table.playtime = 0
        table.gold = 0

        table.LG_SKILL_group = 0

        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    @staticmethod
    def RaceToJob(race, ret_job):
        ret_job.arg_value = None

        if race >= Globals.MAIN_RACE_MAX_NUM:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if race == Globals.MAIN_RACE_LG_PAWN_WARRIOR_M:
            ret_job.arg_value = EJobs.JOB_LG_PAWN_WARRIOR

        elif race == Globals.MAIN_RACE_LG_PAWN_WARRIOR_W:
            ret_job.arg_value = EJobs.JOB_LG_PAWN_WARRIOR

        elif race == Globals.MAIN_RACE_LG_PAWN_ASSASSIN_M:
            ret_job.arg_value = EJobs.JOB_LG_PAWN_ASSASSIN

        elif race == Globals.MAIN_RACE_LG_PAWN_ASSASSIN_W:
            ret_job.arg_value = EJobs.JOB_LG_PAWN_ASSASSIN

        elif race == Globals.MAIN_RACE_LG_PAWN_SHURA_M:
            ret_job.arg_value = EJobs.JOB_LG_PAWN_SHURA

        elif race == Globals.MAIN_RACE_LG_PAWN_SHURA_W:
            ret_job.arg_value = EJobs.JOB_LG_PAWN_SHURA

        elif race == Globals.MAIN_RACE_LG_PAWN_MAGE_M:
            ret_job.arg_value = EJobs.JOB_LG_PAWN_MAGE

        elif race == Globals.MAIN_RACE_LG_PAWN_MAGE_W:
            ret_job.arg_value = EJobs.JOB_LG_PAWN_MAGE

    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##if ENABLE_WOLFMAN
        elif race == Globals.MAIN_RACE_WOLFMAN_M:
            ret_job.arg_value = EJobs.JOB_WOLFMAN
    ##endif

        else:
            return LGEMiscellaneous.DEFINECONSTANTS.false
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    @staticmethod
    def NewPlayerTable2(table, name, race, shape, bEmpire):
        if race >= Globals.MAIN_RACE_MAX_NUM:
            #lani_err("NewPlayerTable2.OUT_OF_RACE_RANGE(%d >= max(%d))\n", race, Globals.MAIN_RACE_MAX_NUM)
            return LGEMiscellaneous.DEFINECONSTANTS.false

        job = None

        temp_ref_job = RefObject(job);
        if not Globals.RaceToJob(race, temp_ref_job):
            job = temp_ref_job.arg_value
            #lani_err("NewPlayerTable2.RACE_TO_JOB_ERROR(%d)\n", race)
            return LGEMiscellaneous.DEFINECONSTANTS.false
        else:
            job = temp_ref_job.arg_value

        #sys_log(0, "NewPlayerTable2(name=%s, race=%d, job=%d)", name, race, job)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memset(table, 0, sizeof(SPlayerTable))

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        strncpy_s(table.name, sizeof(table.name), name, _TRUNCATE)

        table.level = 1
        table.job = race
        table.voice = 0
        table.part_base = shape

        table.st = JobInitialPoints[job].st
        table.dx = JobInitialPoints[job].dx
        table.ht = JobInitialPoints[job].ht
        table.iq = JobInitialPoints[job].iq

        table.hp = JobInitialPoints[job].max_hp + table.ht * JobInitialPoints[job].hp_per_ht
        table.sp = JobInitialPoints[job].max_sp + table.iq * JobInitialPoints[job].sp_per_iq
        table.stamina = JobInitialPoints[job].max_stamina

        table.x = Globals.CREATE_START_X(bEmpire) + number(-300, 300)
        table.y = Globals.CREATE_START_Y(bEmpire) + number(-300, 300)
        table.z = 0
        table.dir = 0
        table.playtime = 0
        table.gold = 0

        table.LG_SKILL_group = 0

        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
    #SendShout(szText, bEmpire)
## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern int g_nPortalLimitTime

    @staticmethod
    def __deposit_limit():
        return (1000 *10000)

    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##if ENABLE_TARGET_INFO
    ## Laniatus Games Studio Inc. | NOTE: This was formerly a static local variable declaration (not allowed in Python):
    TargetInfoLoad_s_vec_item = []
    ##endif

    @staticmethod
    def SendBlockChatInfo(ch, sec):
        if sec <= 0:
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Your Chat is blocked."))
            return

        hour = math.trunc(sec / float(3600))
        sec -= hour * 3600

        min = (math.trunc(sec / float(60)))
        sec -= min * 60

        buf = str(['\0' for _ in range(128+1)])

    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##if __MULTI_LANGUAGE_SYSTEM__
        if hour > 0 and min > 0:
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Your chat is blocked for %d hours %d min and %d sec."), hour, min, sec)
        elif hour > 0 and min == 0:
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Your chat is blocked for %d hours and %d sec."), hour, sec)
        elif hour == 0 and min > 0:
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Your chat is blocked for %d min and %d sec."), min, sec)
        else:
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Your chat is blocked for %d sec."), sec)
    ##else
        if hour > 0 and min > 0:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            snprintf(buf, sizeof(buf), LC_TEXT("Your chat is blocked for %d hours %d min and %d sec."), hour, min, sec)
        elif hour > 0 and min == 0:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            snprintf(buf, sizeof(buf), LC_TEXT("Your chat is blocked for %d hours and %d sec."), hour, sec)
        elif hour == 0 and min > 0:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            snprintf(buf, sizeof(buf), LC_TEXT("Your chat is blocked for %d min and %d sec."), min, sec)
        else:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            snprintf(buf, sizeof(buf), LC_TEXT("Your chat is blocked for %d sec."), sec)

        ch.ChatPacket(EChatType.CHAT_TYPE_INFO, buf)
    ##endif

    spam_score_of_ip = _boost_func_of_void.unordered_map()

    @staticmethod
    def (UnnamedParameter):
        info = if isinstance(event.info, spam_event_info) else None

        if info is None:
            #lani_err("block_chat_by_ip_event> <Factor> Null pointer")
            return 0

        host = info.host

        it = Globals.spam_score_of_ip.find(host)

        if it != Globals.spam_score_of_ip.end():
            it.second.first = 0
            it.second.second = None

        return 0

    @staticmethod
    def SpamBlockCheck(ch, buf, buflen):
## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #    extern int g_iSpamBlockMaxLevel

        if ch.GetLevel() < g_iSpamBlockMaxLevel:
            it = Globals.spam_score_of_ip.find(ch.GetDesc().GetHostName())

            if it == Globals.spam_score_of_ip.end():
                Globals.spam_score_of_ip.insert((ch.GetDesc().GetHostName(), (0, None)))
                it = Globals.spam_score_of_ip.find(ch.GetDesc().GetHostName())

            if it.second.second:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
                Globals.SendBlockChatInfo(ch, Globals.event_time(it.second.second) / passes_per_sec)
                return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

            score = None
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to pointers to value types:
#ORIGINAL METINII C CODE: const char * word = SpamManager::instance().GetSpamScore(buf, buflen, score);
            word = SpamManager.instance().GetSpamScore(buf, buflen, score)

            it.second.first += score

            if word != '\0':
                #sys_log(0, "SPAM_SCORE: %s text: %s score: %u total: %u word: %s", ch.GetName(LOCALE_LANIATUS), buf, score, it.second.first, word)

## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #        extern uint g_uiSpamBlockScore
## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #        extern uint g_uiSpamBlockDuration

            if it.second.first >= g_uiSpamBlockScore:
                info = Globals.AllocEventInfo()
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                strncpy_s(info.host, sizeof(info.host), ch.GetDesc().GetHostName(), _TRUNCATE)

                it.second.second = Globals.event_create_ex(block_chat_by_ip_event, info, ((g_uiSpamBlockDuration) * passes_per_sec))
                #sys_log(0, "SPAM_IP: %s for %u seconds", info.host, g_uiSpamBlockDuration)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
                Globals.SendBlockChatInfo(ch, Globals.event_time(it.second.second) / passes_per_sec)

                return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        return LGEMiscellaneous.DEFINECONSTANTS.false

    TEXT_TAG_PLAIN = 0
    TEXT_TAG_TAG = 1
    TEXT_TAG_COLOR = 2
    TEXT_TAG_HYPERLINK_START = 3
    TEXT_TAG_HYPERLINK_END = 4
    TEXT_TAG_RESTORE_COLOR = 5

    @staticmethod
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Pointer arithmetic is detected on the parameter 'src':
#ORIGINAL METINII C CODE: int GetTextTag(const char * src, int maxLen, int & tagLen, str & extraInfo)
    def GetTextTag(src, maxLen, tagLen, extraInfo):
        tagLen.arg_value = 1

        if maxLen < 2 or *src != '|':
            return Globals.TEXT_TAG_PLAIN

        src += 1
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: const char * cur = ++src;
        cur = src

        if cur[0] == '|':
            tagLen.arg_value = 2
            return Globals.TEXT_TAG_TAG
        elif cur[0] == 'c':
            tagLen.arg_value = 2
            return Globals.TEXT_TAG_COLOR
        elif cur[0] == 'H':
            tagLen.arg_value = 2
            return Globals.TEXT_TAG_HYPERLINK_START
        elif cur[0] == 'h':
            tagLen.arg_value = 2
            return Globals.TEXT_TAG_HYPERLINK_END

        return Globals.TEXT_TAG_PLAIN

    @staticmethod
    def GetTextTagInfo(src, src_len, hyperlinks, colored):
        colored.arg_value = LGEMiscellaneous.DEFINECONSTANTS.false
        hyperlinks.arg_value = 0

        len = None
        extraInfo = ""

        i = 0
        while i < src_len:
            tag = Globals.GetTextTag(src[i], src_len - i, len, extraInfo)

            if tag == Globals.TEXT_TAG_HYPERLINK_START:
                hyperlinks.arg_value += 1

            if tag == Globals.TEXT_TAG_COLOR:
                colored.arg_value = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

            i += len

    @staticmethod
    def ProcessTextTag(ch, c_pszText, len):
        return 0
        hyperlinks = None
        colored = None

        temp_ref_hyperlinks = RefObject(hyperlinks);
        temp_ref_colored = RefObject(colored);
        Globals.GetTextTagInfo(c_pszText, len, temp_ref_hyperlinks, temp_ref_colored)
        colored = temp_ref_colored.arg_value
        hyperlinks = temp_ref_hyperlinks.arg_value

        if colored == ((not LGEMiscellaneous.DEFINECONSTANTS.false)) and hyperlinks == 0:
            return 4

        if ch.GetExchange():
            if hyperlinks == 0:
                return 0
            else:
                return 3

        nPrismCount = ch.CountSpecifyItem(uint(Globals.ITEM_PRISM), -1)

        if nPrismCount < hyperlinks:
            return 1


        if ch.GetMyShop() is None:
            ch.RemoveSpecifyItem(uint(Globals.ITEM_PRISM), uint(hyperlinks), -1)
            return 0
        else:
            sellingNumber = ch.GetMyShop().GetNumberByVnum(uint(Globals.ITEM_PRISM))
            if nPrismCount - sellingNumber < hyperlinks:
                return 2
            else:
                ch.RemoveSpecifyItem(uint(Globals.ITEM_PRISM), uint(hyperlinks), -1)
                return 0

        return 4

    @staticmethod
    def SendShout(szText, bEmpire):
        c_ref_set = DESC_MANAGER.instance().GetClientSet()
        std::for_each(c_ref_set.begin(), c_ref_set.end(), FuncShout(szText, bEmpire))

    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##if __MULTI_LANGUAGE_SYSTEM__
    @staticmethod
    def SendLCNotice(szNotice, bBigFont, *LegacyParamArray):
        c_ref_set = DESC_MANAGER.instance().GetClientSet()
        it = c_ref_set.begin()

        while it is not c_ref_set.end():
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: DESC* d = *(it++);
            d = *(it)
            it += 1
            if d.GetCharacter():
                strMsg = szNotice
                c_pszBuf = None

                if (not len(strMsg)) == 0 and std::all_of(strMsg.begin(), strMsg.end(), isdigit):
                    dwKey = uint(int(szNotice))
                    bLanguage = (d.GetLanguage() if d is not None else LaniatusLocalization.LOCALE_LANIATUS)

                    c_pszBuf = LC_LOCALE_QUEST_TEXT(dwKey, bLanguage)
                else:
                    c_pszBuf = szNotice

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
            ParamCount = -1
    #            va_start(args, bBigFont)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                len = vsnprintf(szNoticeBuf, sizeof(szNoticeBuf), c_pszConvBuf, args)
    #            va_end(args)

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
                    d.GetCharacter().ChatPacket(EChatType.CHAT_TYPE_BIG_NOTICE if bBigFont else EChatType.CHAT_TYPE_NOTICE, "%s", c_pszToken)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no equivalent to the standard string 'erase' method in Python if it's used as an rvalue:
                    c_pszLast = strBuff.erase(0, pos + len(strDelim)).c_str()
                d.GetCharacter().ChatPacket(EChatType.CHAT_TYPE_BIG_NOTICE if bBigFont else EChatType.CHAT_TYPE_NOTICE, "%s", c_pszLast)
## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern socket_t udp_socket

    @staticmethod
    def (UnnamedParameter):
        info = if isinstance(event.info, item_event_info) else None

        if info is None:
            #lani_err("item_destroy_event> <Factor> Null pointer")
            return 0

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
#ORIGINAL METINII C CODE: CItem* pkItem = info->item;
        pkItem = CItem(info.item)

        if pkItem.GetOwner():
            #lani_err("item_destroy_event: Owner exist. (item %s owner %s)", pkItem.GetName(), pkItem.GetOwner().GetName(LOCALE_LANIATUS))

        pkItem.SetDestroyEvent(None)
        ITEM_MANAGER.instance().DestroyItem(pkItem)
        return 0

    @staticmethod
    def __IsWearableWithoutWearFlags(item_type):
        if (item_type == EItemTypes.ITEM_COSTUME) or (item_type == EItemTypes.ITEM_DS) or (item_type == EItemTypes.ITEM_SPECIAL_DS) or (item_type == EItemTypes.ITEM_RING) or (item_type == EItemTypes.ITEM_BELT):
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        if True:
            return LGEMiscellaneous.DEFINECONSTANTS.false

    @staticmethod
    def (UnnamedParameter):
        info = if isinstance(event.info, item_event_info) else None

        if info is None:
            #lani_err("ownership_event> <Factor> Null pointer")
            return 0

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
#ORIGINAL METINII C CODE: CItem* pkItem = info->item;
        pkItem = CItem(info.item)

        pkItem.SetOwnershipEvent(None)

        p = packet_item_ownership()

        p.bHeader = byte(Globals.LG_HEADER_GC_ITEM_OWNERSHIP)
        p.dwVID = pkItem.GetVID()
        p.szName[0] = '\0'

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        pkItem.PacketAround(p, sizeof(p))
        return 0

    @staticmethod
    def (UnnamedParameter):
        info = if isinstance(event.info, item_event_info) else None

        if info is None:
            #lani_err("unique_expire_event> <Factor> Null pointer")
            return 0

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
#ORIGINAL METINII C CODE: CItem* pkItem = info->item;
        pkItem = CItem(info.item)

        if pkItem.GetValue(2) == 0:
            if pkItem.GetSocket(EItemUniqueSockets.LG_ITEM_SOCKET_UNIQUE_REMAIN_TIME) <= 1:
                #sys_log(0, "UNIQUE_ITEM: expire %s %u", pkItem.GetName(), pkItem.GetID())
                pkItem.SetUniqueExpireEvent(None)
                ITEM_MANAGER.instance().RemoveItem(pkItem, "UNIQUE_EXPIRE")
                return 0
            else:
                pkItem.SetSocket(EItemUniqueSockets.LG_ITEM_SOCKET_UNIQUE_REMAIN_TIME, pkItem.GetSocket(EItemUniqueSockets.LG_ITEM_SOCKET_UNIQUE_REMAIN_TIME) - 1)
                return ((60) * passes_per_sec)
        else:
            cur = Globals.get_global_time()

            if pkItem.GetSocket(EItemUniqueSockets.LG_ITEM_SOCKET_UNIQUE_REMAIN_TIME) <= cur:
                pkItem.SetUniqueExpireEvent(None)
                ITEM_MANAGER.instance().RemoveItem(pkItem, "UNIQUE_EXPIRE")
                return 0
            else:
                if pkItem.GetSocket(EItemUniqueSockets.LG_ITEM_SOCKET_UNIQUE_REMAIN_TIME) - cur < 600:
                    return ((pkItem.GetSocket(EItemUniqueSockets.LG_ITEM_SOCKET_UNIQUE_REMAIN_TIME) - cur) * passes_per_sec)
                else:
                    return ((600) * passes_per_sec)

    @staticmethod
    def (UnnamedParameter):
        info = if isinstance(event.info, item_event_info) else None

        if info is None:
            #lani_err("expire_event <Factor> Null pointer")
            return 0

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
#ORIGINAL METINII C CODE: CItem* pkItem = info->item;
        pkItem = CItem(info.item)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        remain_time = pkItem.GetSocket(Globals.LG_ITEM_SOCKET_REMAIN_SEC) - processing_time/passes_per_sec
        if remain_time <= 0:
            #sys_log(0, "ITEM EXPIRED : expired %s %u", pkItem.GetName(), pkItem.GetID())
            pkItem.SetTimerBasedOnWearExpireEvent(None)
            pkItem.SetSocket(Globals.LG_ITEM_SOCKET_REMAIN_SEC, 0)

            if pkItem.IsDragonSoul():
                DSManager.instance().DeactivateDragonSoul(pkItem, DefineConstants.false)
            else:
                ITEM_MANAGER.instance().RemoveItem(pkItem, "TIMER_BASED_ON_WEAR_EXPIRE")
            return 0
        pkItem.SetSocket(Globals.LG_ITEM_SOCKET_REMAIN_SEC, remain_time)
        return ((MIN(60, remain_time)) * passes_per_sec)

    @staticmethod
    def (UnnamedParameter):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no equivalent to 'reinterpret_cast' in Python:
        info = reinterpret_cast<const item_vid_event_info>(event.info)

        if None is info:
            return 0

        item = ITEM_MANAGER.instance().FindByVID(info.item_vid)

        if None is item:
            return 0

        current = Globals.get_global_time()

        if current > item.GetSocket(0):
            if item.IsNewMountItem():
                if item.GetSocket(2) != 0:
                    item.ClearMountAttributeAndAffect()

            ITEM_MANAGER.instance().RemoveItem(item, "REAL_TIME_EXPIRE")

            return 0

        return ((1) * passes_per_sec)

    @staticmethod
    def (UnnamedParameter):
        info = if isinstance(event.info, item_vid_event_info) else None

        if info is None:
            #lani_err("accessory_socket_expire_event> <Factor> Null pointer")
            return 0

        item = ITEM_MANAGER.instance().FindByVID(info.item_vid)

        if item.GetAccessorySocketDownGradeTime() <= 1:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There are no gotos or labels in Python:
            degrade:
            item.SetAccessorySocketExpireEvent(None)
            item.AccessorySocketDegrade()
            return 0
        else:
            iTime = item.GetAccessorySocketDownGradeTime() - 60

            if iTime <= 1:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There are no gotos or labels in Python:
                goto degrade

            item.SetAccessorySocketDownGradeTime(uint(iTime))

            if iTime > 60:
                return ((60) * passes_per_sec)
            else:
                return ((iTime) * passes_per_sec)

    @staticmethod
    def CanPutIntoRing(ring, item):
        vnum = item.GetVnum()
        return LGEMiscellaneous.DEFINECONSTANTS.false


    MAX_NORM_ATTR_NUM = ITEM_MANAGER.MAX_NORM_ATTR_NUM
    MAX_RARE_ATTR_NUM = ITEM_MANAGER.MAX_RARE_ATTR_NUM

## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern list<CItemDropInfo> g_vec_pkCommonDropItem[MOB_RANK_MAX_NUM]


    @staticmethod
    def GetDropPerKillPct(iMinimum, iDefault, iDeltaPercent, c_pszFlag):
        iVal = 0

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((iVal = quest::CQuestManager::instance().GetEventFlag(c_pszFlag)))
        if (iVal = quest.CQuestManager.instance().GetEventFlag(c_pszFlag)):
            if iVal < iMinimum:
                iVal = iDefault

            if iVal < 0:
                iVal = iDefault

        if iVal == 0:
            return 0

        return (math.trunc(40000 * iDeltaPercent / float(iVal)))


    @staticmethod
    def GetThreeSkillLevelAdjust(level):
        if level < 40:
            return 32
        if level < 45:
            return 16
        if level < 50:
            return 8
        if level < 55:
            return 4
        if level < 60:
            return 2
        return 1

    @staticmethod
    def touch(path):
        fp = None

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if (!(fp = fopen(path, "a")))
        if not(fp = fopen(path, "a")):
            #lani_err("touch failed")
            return (-1)

        fclose(fp)
        return 0
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##if __MULTI_LANGUAGE_SYSTEM__
    ##endif

    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##if __MULTI_LANGUAGE_SYSTEM__
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Typedefs defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
    #typedef dict<uint, str> LocaleQuestTranslateMapType;
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Typedefs defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
    #typedef dict<uint, str> LocaleItemMapType;
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Typedefs defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
    #typedef dict<uint, str> LocaleMobMapType;
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Typedefs defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
    #typedef dict<uint, str> LocaleSkillMapType;
    ##endif

    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##if __MULTI_LANGUAGE_SYSTEM__
    localeQuestTranslate = [{} for _ in range((int)LaniatusLocalization.LOCALE_MAX_NUM)]
    localeString = [{} for _ in range((int)LaniatusLocalization.LOCALE_MAX_NUM)]
    localeItem = [{} for _ in range((int)LaniatusLocalization.LOCALE_MAX_NUM)]
    localeMob = [{} for _ in range((int)LaniatusLocalization.LOCALE_MAX_NUM)]
    localeSkill = [{} for _ in range((int)LaniatusLocalization.LOCALE_MAX_NUM)]
    ##else
    localeString = {}
    ##endif

    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##if __MULTI_LANGUAGE_SYSTEM__
    @staticmethod
    def get_locale(locale):
        if locale == LaniatusLocalization.LOCALE_EN:
            return "en"
        if (locale == LaniatusLocalization.LOCALE_EN) or (locale == LaniatusLocalization.LOCALE_DE):
            return "de"
            #	case LOCALE_PT:
            #		return "pt"
            #	case LOCALE_ES:
            #		return "es"
            #	case LOCALE_FR:
            #		return "fr"
            #	case LOCALE_RO:
            #		return "ro"
            #	case LOCALE_PL:
            #		return "pl"
            #	case LOCALE_IT:
            #		return "it"
            #	case LOCALE_CZ:
            #		return "cz"
            #	case LOCALE_HU:
            #		return "hu"
            #	case LOCALE_TR:
            #		return "tr"; 

        if True:
            return "en"

    @staticmethod
    def locale_add(strings, locale):
        iter = Globals.localeString[locale].find(strings[0])

        if iter is Globals.localeString[locale].end():
            Globals.localeString[locale].update({strings[0]: strings[1]})

    @staticmethod
    def locale_find(string, locale):
        if (not string[0]) != '\0' or locale == LaniatusLocalization.LOCALE_LANIATUS:
            return string

        if locale > LaniatusLocalization.LOCALE_MAX_NUM:
            locale = LaniatusLocalization.LOCALE_EN

        iter = Globals.localeString[locale].find(string)

        if iter is Globals.localeString[locale].end():
            # #lani_err("LOCALE_ERROR: \"%s\";", string)
            return string

        return iter.second.c_str()

    @staticmethod
    def locale_quest_translate_find(vnum, locale):
        if locale > LaniatusLocalization.LOCALE_MAX_NUM:
            locale = LaniatusLocalization.LOCALE_EN

        iter = Globals.localeQuestTranslate[locale].find(vnum)

        if iter is Globals.localeQuestTranslate[locale].end():
            return "NoName"

        return iter.second.c_str()

    @staticmethod
    def locale_item_find(vnum, locale):
        if locale > LaniatusLocalization.LOCALE_MAX_NUM:
            locale = LaniatusLocalization.LOCALE_EN

        iter = Globals.localeItem[locale].find(vnum)

        if iter is Globals.localeItem[locale].end():
            return "NoName"

        return iter.second.c_str()

    @staticmethod
    def locale_mob_find(vnum, locale):
        if locale > LaniatusLocalization.LOCALE_MAX_NUM:
            locale = LaniatusLocalization.LOCALE_EN

        iter = Globals.localeMob[locale].find(vnum)

        if iter is Globals.localeMob[locale].end():
            return "NoName"

        return iter.second.c_str()

    @staticmethod
    def locale_LG_SKILL_find(vnum, locale):
        if locale > LaniatusLocalization.LOCALE_MAX_NUM:
            locale = LaniatusLocalization.LOCALE_EN

        iter = Globals.localeSkill[locale].find(vnum)

        if iter is Globals.localeSkill[locale].end():
            return "NoName"

        return iter.second.c_str()

    @staticmethod
    def locale_quest_translate_init(filename, locale):
        nameData = cCsvTable()

        if not nameData.Load(filename, '\t', '"'):
            fprintf(stderr, "%s couldn't be loaded or its format is incorrect.\n", filename)
            return

        nameData.Next()

        while nameData.Next():
            if nameData.ColCount() > 1:
                Globals.localeQuestTranslate[locale].update({atoi(nameData.AsStringByIndex(0)): nameData.AsStringByIndex(1)})

        nameData.Destroy()

    @staticmethod
    def locale_item_init(filename, locale):
        nameData = cCsvTable()

        if not nameData.Load(filename, '\t', '"'):
            fprintf(stderr, "%s couldn't be loaded or its format is incorrect.\n", filename)
            return

        nameData.Next()

        while nameData.Next():
            if nameData.ColCount() > 1:
                Globals.localeItem[locale].update({atoi(nameData.AsStringByIndex(0)): nameData.AsStringByIndex(1)})

        nameData.Destroy()

    @staticmethod
    def locale_mob_init(filename, locale):
        nameData = cCsvTable()

        if not nameData.Load(filename, '\t', '"'):
            fprintf(stderr, "%s couldn't be loaded or its format is incorrect.\n", filename)
            return

        nameData.Next()

        while nameData.Next():
            if nameData.ColCount() > 1:
                Globals.localeMob[locale].update({atoi(nameData.AsStringByIndex(0)): nameData.AsStringByIndex(1)})

        nameData.Destroy()

    @staticmethod
    def locale_LG_SKILL_init(filename, locale):
        nameData = cCsvTable()

        if not nameData.Load(filename, '\t', '"'):
            fprintf(stderr, "%s couldn't be loaded or its format is incorrect.\n", filename)
            return

        nameData.Next()

        while nameData.Next():
            if nameData.ColCount() > 1:
                Globals.localeSkill[locale].update({atoi(nameData.AsStringByIndex(0)): nameData.AsStringByIndex(1)})

        nameData.Destroy()
    ##else
    @staticmethod
    def locale_add(strings):
        iter = Globals.localeString.find(strings[0])

        if iter == Globals.localeString.end():
            Globals.localeString.update({strings[0]: strings[1]})

    ## Laniatus Games Studio Inc. | NOTE: This was formerly a static local variable declaration (not allowed in Python):
    locale_find_s_line = "@0949"

    @staticmethod
    def locale_find(string):
        iter = Globals.localeString.find(string)

        if iter == Globals.localeString.end():
            ## Laniatus Games Studio Inc. | NOTE: This static local variable declaration (not allowed in Python) has been moved just prior to the method:
            #        static char s_line[1024] = "@0949"
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            strncpy_s(locale_find_s_line + 5, sizeof(locale_find_s_line) - 5, string, _TRUNCATE)

            #lani_err("LOCALE_ERROR: \"%s\";", string)
            return locale_find_s_line

        return iter.second.c_str()
    ##endif

    @staticmethod
    def quote_find_end(string):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Pointer arithmetic is detected on this variable:
#ORIGINAL METINII C CODE: const char *tmp = string;
        tmp = string
        quote = 0

        while *tmp != '\0':
            if quote != 0 and *tmp == '\\' and (*(tmp + 1)) != 0:
                if *(tmp + 1) == '"':
                    tmp += 2
                    continue
            elif *tmp == '"':
                quote = 1 if quote == 0 else 0
            elif quote == 0 and *tmp == ';':
                return (tmp)

            tmp += 1

        return (None)

    @staticmethod
    def locale_convert(src, len):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Pointer arithmetic is detected on this variable:
#ORIGINAL METINII C CODE: const char *tmp;
        tmp = None
        i = None
        j = None
        buf = None
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Pointer arithmetic is detected on this variable:
#ORIGINAL METINII C CODE: char *dest;
        dest = None
        start = 0
        last_char = 0

        if len == 0:
            return None

        buf = LG_NEW_M2 char[len + 1]

        j = i = 0
        tmp = src
        dest = buf
        while i < len:
            if *tmp == '"':
                if last_char != '\\':
                    start = 1 if start == 0 else 0
                else:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There are no gotos or labels in Python:
                    goto ENCODE
            elif *tmp == ';':
                if last_char != '\\' and start == 0:
                    break
                else:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There are no gotos or labels in Python:
                    goto ENCODE
            elif start != 0:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There are no gotos or labels in Python:
                ENCODE:
                if *tmp == '\\' and *(tmp + 1) == 'n':
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: *(dest++) = '\n';
                    *(dest) = '\n'
                    dest += 1
                    tmp += 1
                    last_char = '\n'
                else:
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: *(dest++) = *tmp;
                    *(dest) = *tmp
                    dest += 1
                    last_char = *tmp

                j += 1
            i += 1
            tmp += 1

        if j == 0:
            LG_DEL_MEM_ARRAY(buf)
            return None

        *dest = '\0'
        return (buf)


    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##if __MULTI_LANGUAGE_SYSTEM__
    @staticmethod
    def locale_init(filename, locale):
    ##else
    @staticmethod
    def locale_init(filename):
    ##endif
        fp = fopen(filename, "rb")
        buf = None

        if fp is None:
            return

        fseek(fp, 0, SEEK_END)
        i = ftell(fp)
        fseek(fp, 0, SEEK_SET)

        i += 1

        buf = LG_NEW_M2 char[i]

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
        memset(buf, 0, i)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        fread(buf, i - 1, sizeof(char), fp)

        fclose(fp)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Pointer arithmetic is detected on this variable:
#ORIGINAL METINII C CODE: const char * tmp;
        tmp = None
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Pointer arithmetic is detected on this variable:
#ORIGINAL METINII C CODE: const char * end;
        end = None

        strings = ["" for _ in range((int)LGEMiscellaneous.DEFINECONSTANTS.NUM_LOCALES)]

        if (not buf) != '\0':
            #lani_err("locale_read: no file %s", filename)
            exit(1)

        tmp = buf

        condition = True
        while condition:
            for i in range(0, LGEMiscellaneous.DEFINECONSTANTS.NUM_LOCALES):
                strings[i] = None

            if *tmp == '"':
                for i in range(0, LGEMiscellaneous.DEFINECONSTANTS.NUM_LOCALES):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if (!(end = quote_find_end(tmp)))
                    if not(end = Globals.quote_find_end(tmp)):
                        break

                    strings[i] = Globals.locale_convert(tmp, end - tmp)
                    end += 1
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: tmp = ++end;
                    tmp = end

                    while *tmp == '\n' or *tmp == '\r' or *tmp == ' ':
                        tmp += 1

                    if i + 1 == LGEMiscellaneous.DEFINECONSTANTS.NUM_LOCALES:
                        break

                    if *tmp != '"':
                        #lani_err("locale_init: invalid format filename %s", filename)
                        break

                if strings[0] is None or strings[1] is None:
                    break

    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##if __MULTI_LANGUAGE_SYSTEM__
                Globals.locale_add(str(strings), locale)
    ##else
                Globals.locale_add(str(strings))
    ##endif

                for i in range(0, LGEMiscellaneous.DEFINECONSTANTS.NUM_LOCALES):
                    if strings[i] != '\0':
                        LG_DEL_MEM_ARRAY(strings[i])
            else:
                tmp = strchr(tmp, '\n')

                if tmp != '\0':
                    tmp += 1
            condition = tmp and *tmp

        LG_DEL_MEM_ARRAY(buf)


    @staticmethod
    def LocaleService_LoadLocaleStringFile():
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##if ! __MULTI_LANGUAGE_SYSTEM__
        if (not len(Globals.g_stLocaleFilename)) == 0:
            locale_init(Globals.g_stLocaleFilename)
            fprintf(stderr, "LocaleService %s\n", Globals.g_stLocaleFilename)
        locale = 0
    ##else
        while locale < LaniatusLocalization.LOCALE_MAX_NUM:
            if locale == LaniatusLocalization.LOCALE_LANIATUS:
                Globals.g_stLocaleFilename = Globals.g_stServiceBasePath + "/country/" + get_locale(LaniatusLocalization.LOCALE_DEFAULT) + "/" + "locale_string.txt"
            else:
                Globals.g_stLocaleFilename = Globals.g_stServiceBasePath + "/country/" + get_locale(locale) + "/" + "locale_string.txt"

            if len(Globals.g_stLocaleFilename) == 0:
                continue

            if (not locale) == LaniatusLocalization.LOCALE_LANIATUS:
                fprintf(stderr, "LocaleService %s\n", get_locale(locale))

            locale_init(Globals.g_stLocaleFilename, locale)
            locale += 1
    ##endif

    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##if __MULTI_LANGUAGE_SYSTEM__
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##if __MULTI_LANGUAGE_SYSTEM__
    @staticmethod
    def LocaleService_LoadQuestTranslateFile():
        if len(Globals.g_stLocaleFilename) == 0:
            return

        if g_bAuthServer:
            return

        locale = 0
        while locale < LaniatusLocalization.LOCALE_MAX_NUM:
            if locale == LaniatusLocalization.LOCALE_LANIATUS:
                Globals.g_stLocaleFilename = Globals.g_stServiceBasePath + "/country/" + get_locale(LaniatusLocalization.LOCALE_DEFAULT) + "/" + "locale_quest.txt"
            else:
                Globals.g_stLocaleFilename = Globals.g_stServiceBasePath + "/country/" + get_locale(locale) + "/" + "locale_quest.txt"

            if len(Globals.g_stLocaleFilename) == 0:
                continue

            locale_quest_translate_init(Globals.g_stLocaleFilename, locale)
            locale += 1

    @staticmethod
    def LocaleService_LoadItemNameFile():
        if len(Globals.g_stLocaleFilename) == 0:
            return

        if g_bAuthServer:
            return

        locale = 0
        while locale < LaniatusLocalization.LOCALE_MAX_NUM:
            if locale == LaniatusLocalization.LOCALE_LANIATUS:
                Globals.g_stLocaleFilename = Globals.g_stServiceBasePath + "/country/" + get_locale(LaniatusLocalization.LOCALE_DEFAULT) + "/" + "item_names.txt"
            else:
                Globals.g_stLocaleFilename = Globals.g_stServiceBasePath + "/country/" + get_locale(locale) + "/" + "item_names.txt"

            if len(Globals.g_stLocaleFilename) == 0:
                continue

            locale_item_init(Globals.g_stLocaleFilename, locale)
            locale += 1

    @staticmethod
    def LocaleService_LoadMobNameFile():
        if len(Globals.g_stLocaleFilename) == 0:
            return

        if g_bAuthServer:
            return

        locale = 0
        while locale < LaniatusLocalization.LOCALE_MAX_NUM:
            if locale == LaniatusLocalization.LOCALE_LANIATUS:
                Globals.g_stLocaleFilename = Globals.g_stServiceBasePath + "/country/" + get_locale(LaniatusLocalization.LOCALE_DEFAULT) + "/" + "mob_names.txt"
            else:
                Globals.g_stLocaleFilename = Globals.g_stServiceBasePath + "/country/" + get_locale(locale) + "/" + "mob_names.txt"

            if len(Globals.g_stLocaleFilename) == 0:
                continue

            locale_mob_init(Globals.g_stLocaleFilename, locale)
            locale += 1

    @staticmethod
    def LocaleService_LoadSkillNameFile():
        if len(Globals.g_stLocaleFilename) == 0:
            return

        if g_bAuthServer:
            return

        locale = 0
        while locale < LaniatusLocalization.LOCALE_MAX_NUM:
            if locale == LaniatusLocalization.LOCALE_LANIATUS:
                Globals.g_stLocaleFilename = Globals.g_stServiceBasePath + "/country/" + get_locale(LaniatusLocalization.LOCALE_DEFAULT) + "/" + "LG_SKILL_names.txt"
            else:
                Globals.g_stLocaleFilename = Globals.g_stServiceBasePath + "/country/" + get_locale(locale) + "/" + "LG_SKILL_names.txt"

            if len(Globals.g_stLocaleFilename) == 0:
                continue

            locale_LG_SKILL_init(Globals.g_stLocaleFilename, locale)
            locale += 1

    ##endif
    @staticmethod
    def LocaleService_GetBasePath():
        return Globals.g_stServiceBasePath

    @staticmethod
    def LocaleService_GetMapPath():
        return Globals.g_stServiceMapPath

    @staticmethod
    def LocaleService_GetQuestPath():
        return g_stQuestDir



    g_stLocale = "latin1"
    g_stServiceName = ""
    g_stServiceBasePath = "share"
    g_stServiceMapPath = g_stServiceBasePath + "/map"
    g_stLocaleFilename = g_stServiceBasePath + "/locale_string.txt"
    PK_PROTECT_LEVEL = 15
    g_stLocal = ""

    @staticmethod
    def check_name(str):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Pointer arithmetic is detected on this variable:
#ORIGINAL METINII C CODE: const char* tmp;
        tmp = None

        if (not str) != '\0' or (not str[0]) != '\0':
            return 0

        if len(str) < 2:
            return 0

        tmp = str
        while *tmp != '\0':
            if tmp.isdigit() or tmp.isalpha():
                continue
            else:
                return 0
            tmp += 1

        szTmp = str(['\0' for _ in range(256)])
        temp_ref_szTmp = RefObject(szTmp);
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        Globals.str_lower(str, temp_ref_szTmp, sizeof(szTmp))
        szTmp = temp_ref_szTmp.arg_value

        if CMobManager.instance().Get(szTmp, LGEMiscellaneous.DEFINECONSTANTS.false):
            return 0

        return 1

    ##endif

    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##if __cplusplus
    ##endif
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
    #log_init()
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
    #log_destroy()
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
    #log_rotate()

# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
    #log_set_level(level)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
    #log_unset_level(level)

# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
    #log_set_expiration_days(days)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
    #log_get_expiration_days()

    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##if ! _WIN32
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
    #_#lani_err(func, line, format, *LegacyParamArray)
    ##else
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
    #_#lani_err(func, line, format, *LegacyParamArray)
    ##endif
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
    ##sys_log_header(header)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
    ##sys_log(lv, format, *LegacyParamArray)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
    #pt_log(format, *LegacyParamArray)

    #Copyright © 2021 - 2022 Laniatus Games Studio Inc. Software System and Partition T.F

    ##define isdigit iswdigit
    ##define isspace iswspace
    ## Laniatus Games Studio Inc. | NOTE: The following #define macro was replaced in-line:
    #ORIGINAL METINII C CODE: #define PASSES_PER_SEC(sec) ((sec) * passes_per_sec)

    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##if _WIN32
    ##endif

    ##define IN
    ##define OUT

    #Copyright © 2021 - 2022 Laniatus Games Studio Inc. Software System and Partition T.F


    __escape_hint = str(['\0' for _ in range(1024)])



## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern str g_stBlockDate


    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##if __cplusplus
    ##endif

    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##if __LIBTHECORE__
## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern volatile int tics
## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern volatile int shutdowned
    ##endif

## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern struct heart * thecore_heart

## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern uint thecore_profiler[NUM_PF]

# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
    #thecore_init(fps, heartbeat_func)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
    #thecore_idle()
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
    #thecore_shutdown()
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
    #thecore_destroy()
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
    #thecore_pulse()
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
    #thecore_time()
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
    #thecore_pulse_per_second()
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
    #thecore_is_shutdowned()

# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
    #thecore_tick()

    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##if __cplusplus
    ##endif

    ## Laniatus Games Studio Inc. | WARNING: The following #include directive was ignored:
    ##include <_boost_func_of_void/bind.hpp>
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##if USE_STACKTRACE
    ## Laniatus Games Studio Inc. | WARNING: The following #include directive was ignored:
    ##include <execinfo.h>
    ##endif

# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
    #WriteVersion()
class _malloc_messageDelegate:
    def invoke(self, p1, p2, p3, p4):
        pass

    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##if __FreeBSD__ && DEBUG_ALLOC
    _malloc_message = _malloc_messageDelegate()
    @staticmethod
    def WriteMallocMessage(p1, p2, p3, p4):
        fp = fopen(LGEMiscellaneous.DEFINECONSTANTS.DBGALLOC_LOG_FILENAME, "a")
        if fp is None:
            return
        fprintf(fp, "%s %s %s %s\n", p1, p2, p3, p4)
        fclose(fp)
    ##endif

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There are no equivalents to volatile variables in Python:
#ORIGINAL METINII C CODE: volatile int num_events_called = 0;
    num_events_called = 0
    max_bytes_written = 0
    current_bytes_written = 0
    total_bytes_written = 0
    g_bLogLevel = 0

    tcp_socket = 0
    udp_socket = 0
    p2p_socket = 0

    main_fdw = None

    @staticmethod
    def io_loop(fdw):
        d = None
        num_events = None
        event_idx = None

        DESC_MANAGER.instance().DestroyClosed()
        DESC_MANAGER.instance().TryConnect()

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((num_events = fdwatch(fdw, 0)) < 0)
        if (num_events = fdwatch(fdw, 0)) < 0:
            return 0

        for event_idx in range(0, num_events):
            d = Globals.fdwatch_get_client_data(LPFDWATCH(fdw), uint(event_idx))

            if d is None:
                if EFdwatch.FDW_READ == Globals.fdwatch_check_event(LPFDWATCH(fdw), socket_t(Globals.tcp_socket), uint(event_idx)):
                    DESC_MANAGER.instance().AcceptDesc(LPFDWATCH(fdw), socket_t(Globals.tcp_socket))
                    Globals.fdwatch_clear_event(LPFDWATCH(fdw), socket_t(Globals.tcp_socket), uint(event_idx))
                elif EFdwatch.FDW_READ == Globals.fdwatch_check_event(LPFDWATCH(fdw), socket_t(Globals.p2p_socket), uint(event_idx)):
                    DESC_MANAGER.instance().AcceptP2PDesc(LPFDWATCH(fdw), socket_t(Globals.p2p_socket))
                    Globals.fdwatch_clear_event(LPFDWATCH(fdw), socket_t(Globals.p2p_socket), uint(event_idx))
                continue

            iRet = Globals.fdwatch_check_event(LPFDWATCH(fdw), d.GetSocket(), uint(event_idx))

            if iRet == EFdwatch.FDW_READ:
                if db_clientdesc is d:
                    size = d.ProcessInput()

                    if size != 0:
                        Globals.#sys_log(1, "DB_BYTES_READ: %d", size)

                    if size < 0:
                        d.SetPhase(EPhase.PHASE_CLOSE)
                elif d.ProcessInput() < 0:
                    d.SetPhase(EPhase.PHASE_CLOSE)

            elif iRet == EFdwatch.FDW_WRITE:
                if db_clientdesc is d:
                    buf_size = int(Globals.buffer_size(d.GetOutputBuffer()))
                    sock_buf_size = Globals.fdwatch_get_buffer_size(LPFDWATCH(fdw), d.GetSocket())

                    ret = d.ProcessOutput()

                    if ret < 0:
                        d.SetPhase(EPhase.PHASE_CLOSE)

                    if buf_size != 0:
                        #sys_log(1, "DB_BYTES_WRITE: size %d sock_buf %d ret %d", buf_size, sock_buf_size, ret)
                elif d.ProcessOutput() < 0:
                    d.SetPhase(EPhase.PHASE_CLOSE)

            elif iRet == EFdwatch.FDW_EOF:
                    d.SetPhase(EPhase.PHASE_CLOSE)

            else:
                #lani_err("fdwatch_check_event returned unknown %d", iRet)
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##if _WIN32
                if d is None:
                    return 1
    ##endif
                d.SetPhase(EPhase.PHASE_CLOSE)

        return 1

    @staticmethod
    def start(argc, argv):
        st_localeServiceName = ""

        bVerbose = LGEMiscellaneous.DEFINECONSTANTS.false
        ch = None

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: while((ch = getopt(argc, argv, "npverltI")) != -1)
        while (ch = Globals.getopt(argc, argv, "npverltI")) != -1:
            ep = None

            if ch == 'I':
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                strncpy_s(g_szPublicIP, sizeof(g_szPublicIP), argv[optind], _TRUNCATE)

                print("IP {0}\n".format(g_szPublicIP), end = '')

                optind += 1
                optreset = 1

            elif ch == 'p':
                mother_port = strtol(argv[optind], ep, 10)

                if mother_port <= 1024:
                    Globals.usage()
                    return 0

                print("port {0:d}\n".format(mother_port), end = '')

                optind += 1
                optreset = 1

            elif ch == 'l':
                    l = strtol(argv[optind], ep, 10)

                    Globals.log_set_level(uint(l))

                    optind += 1
                    optreset = 1

            elif ch == 'n':
                    if optind < argc:
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: st_localeServiceName = argv[optind++];
                        st_localeServiceName = argv[optind]
                        optind += 1
                        optreset = 1

            elif ch == 'v':
                bVerbose = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

            elif ch == 'r':
                g_bNoRegen = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        Globals.config_init(st_localeServiceName)

        if not bVerbose:
            freopen("stdout", "a", stdout)

        is_thecore_initialized = Globals.thecore_init(25, heartbeat) != 0

        if not is_thecore_initialized:
            fprintf(stderr, "Could not initialize thecore, check owner of pid, syslog\n")
            sys.exit(0)

        signal_timer_disable()

## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: main_fdw = fdwatch_new(4096);
        Globals.main_fdw.copy_from(Globals.fdwatch_new(4096))

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if((tcp_socket = socket_tcp_bind(g_szPublicIP, mother_port)) == DefineConstants.INVALID_SOCKET)
        if (Globals.tcp_socket = Globals.socket_tcp_bind(g_szPublicIP, mother_port)) is LGEMiscellaneous.DEFINECONSTANTS.INVALID_SOCKET:
            perror("socket_tcp_bind: tcp_socket")
            return 0


    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##if ! ENABLE_UDP_BLOCK
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if((udp_socket = socket_udp_bind(g_szPublicIP, mother_port)) == DefineConstants.INVALID_SOCKET)
        if (Globals.udp_socket = Globals.socket_udp_bind(g_szPublicIP, mother_port)) is LGEMiscellaneous.DEFINECONSTANTS.INVALID_SOCKET:
            perror("socket_udp_bind: udp_socket")
            return 0
    ##endif

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((p2p_socket = socket_tcp_bind(*g_szInternalIP ? g_szInternalIP : g_szPublicIP, p2p_port)) == DefineConstants.INVALID_SOCKET)
        if (Globals.p2p_socket = Globals.socket_tcp_bind(g_szInternalIP if *g_szInternalIP else g_szPublicIP, p2p_port)) is LGEMiscellaneous.DEFINECONSTANTS.INVALID_SOCKET:
            perror("socket_tcp_bind: p2p_socket")
            return 0

        Globals.fdwatch_add_fd(LPFDWATCH(Globals.main_fdw), socket_t(Globals.tcp_socket), None, EFdwatch.FDW_READ, LGEMiscellaneous.DEFINECONSTANTS.false)
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##if ! ENABLE_UDP_BLOCK
        Globals.fdwatch_add_fd(LPFDWATCH(Globals.main_fdw), socket_t(Globals.udp_socket), None, EFdwatch.FDW_READ, LGEMiscellaneous.DEFINECONSTANTS.false)
    ##endif
        Globals.fdwatch_add_fd(LPFDWATCH(Globals.main_fdw), socket_t(Globals.p2p_socket), None, EFdwatch.FDW_READ, LGEMiscellaneous.DEFINECONSTANTS.false)

        db_clientdesc = DESC_MANAGER.instance().CreateConnectionDesc(LPFDWATCH(Globals.main_fdw), db_addr, db_port, EPhase.PHASE_DBCLIENT, ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
        if not g_bAuthServer:
            db_clientdesc.UpdateChannelStatus(0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)))

        if g_bAuthServer:
            if g_stAuthMasterIP.length() != 0:
                fprintf(stderr, "SlaveAuth! \n")
                g_pkAuthMasterDesc = DESC_MANAGER.instance().CreateConnectionDesc(LPFDWATCH(Globals.main_fdw), g_stAuthMasterIP.c_str(), g_wAuthMasterPort, EPhase.PHASE_P2P, ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
                P2P_MANAGER.instance().RegisterConnector(g_pkAuthMasterDesc)
                g_pkAuthMasterDesc.SetP2P(g_stAuthMasterIP.c_str(), g_wAuthMasterPort, g_bChannel)
            else:
                szIP = g_szInternalIP if len(g_szInternalIP) > 1 else g_szPublicIP

                fprintf(stderr, "Master Auth! \n")
                g_pkAuthMasterDesc = DESC_MANAGER.instance().CreateConnectionDesc(LPFDWATCH(Globals.main_fdw), szIP, p2p_port, EPhase.PHASE_P2P, ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
                P2P_MANAGER.instance().RegisterConnector(g_pkAuthMasterDesc)
                g_pkAuthMasterDesc.SetP2P(szIP, p2p_port, g_bChannel)

        signal_timer_enable(30)
        return 1

    ## Laniatus Games Studio Inc. | NOTE: This was formerly a static local variable declaration (not allowed in Python):
    pta = { 0, 0 }
    ## Laniatus Games Studio Inc. | NOTE: This was formerly a static local variable declaration (not allowed in Python):
    idle_process_time_count = 0

    @staticmethod
    def idle():
        ## Laniatus Games Studio Inc. | NOTE: This static local variable declaration (not allowed in Python) has been moved just prior to the method:
        #    static struct timeval pta = { 0, 0 }
        ## Laniatus Games Studio Inc. | NOTE: This static local variable declaration (not allowed in Python) has been moved just prior to the method:
        #    static int process_time_count = 0
        now = idle_timeval()

        if pta.tv_sec == 0:
            gettimeofday(pta, 0)

        passed_pulses = None

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if (!(passed_pulses = thecore_idle()))
        if not(passed_pulses = Globals.thecore_idle()):
            return 0

        assert passed_pulses > 0

        t = None

## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: while (passed_pulses--)
        while (passed_pulses) != 0:
            passed_pulses -= 1
            thecore_heart.pulse += 1
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: heartbeat(thecore_heart, ++thecore_heart->pulse);
            Globals.heartbeat(thecore_heart, thecore_heart.pulse)
            Globals.thecore_tick()
        passed_pulses -= 1

        t = get_dword_time()
        CHARACTER_MANAGER.instance().Update(thecore_heart.pulse)
        db_clientdesc.Update(t)
        Globals.s_dwProfiler[(int)EProfile.PROF_CHR_UPDATE] += (get_dword_time() - t)

        t = get_dword_time()
        if Globals.io_loop(LPFDWATCH(Globals.main_fdw)) == 0:
            return 0
        Globals.s_dwProfiler[(int)EProfile.PROF_IO] += (get_dword_time() - t)

        Globals.log_rotate()

        gettimeofday(now, 0)
        idle_process_time_count += 1

        if now.tv_sec - pta.tv_sec > 0:
            pt_log("[%3d] event %5d/%-5d idle %-4ld event %-4ld heartbeat %-4ld I/O %-4ld chrUpate %-4ld | WRITE: %-7d | PULSE: %d", idle_process_time_count, Globals.num_events_called, Globals.event_count(), thecore_profiler[(int)ENUM_PROFILER.PF_IDLE], Globals.s_dwProfiler[(int)EProfile.PROF_EVENT], Globals.s_dwProfiler[(int)EProfile.PROF_HEARTBEAT], Globals.s_dwProfiler[(int)EProfile.PROF_IO], Globals.s_dwProfiler[(int)EProfile.PROF_CHR_UPDATE], Globals.current_bytes_written, Globals.thecore_pulse())

            Globals.num_events_called = 0
            Globals.current_bytes_written = 0

            idle_process_time_count = 0
            gettimeofday(pta, 0)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            memset(thecore_profiler[0], 0, sizeof(thecore_profiler))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            memset(Globals.s_dwProfiler[0], 0, sizeof(Globals.s_dwProfiler))
        return 1

    @staticmethod
    def destroy():
        #sys_log(0, "<shutdown> Canceling ReloadSpamEvent...")
        Globals.CancelReloadSpamEvent()

        #sys_log(0, "<shutdown> regen_free()...")
        Globals.regen_free()

        #sys_log(0, "<shutdown> Closing sockets...")
        Globals.socket_close(socket_t(Globals.tcp_socket))
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##if ! ENABLE_UDP_BLOCK
        Globals.socket_close(socket_t(Globals.udp_socket))
    ##endif
        Globals.socket_close(socket_t(Globals.p2p_socket))

        #sys_log(0, "<shutdown> fdwatch_delete()...")
        Globals.fdwatch_delete(LPFDWATCH(Globals.main_fdw))

        #sys_log(0, "<shutdown> event_destroy()...")
        Globals.event_destroy()

        #sys_log(0, "<shutdown> CTextFileLoader::DestroySystem()...")
        CTextFileLoader.DestroySystem()

        #sys_log(0, "<shutdown> thecore_destroy()...")
        Globals.thecore_destroy()

# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
    #test()

    s_dwProfiler = [0 for _ in range((int)EProfile.PROF_MAX_NUM)]

    g_shutdown_disconnect_pulse = 0
    g_shutdown_disconnect_force_pulse = 0
    g_shutdown_core_pulse = 0
    g_bShutdown = LGEMiscellaneous.DEFINECONSTANTS.false

# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
    #CancelReloadSpamEvent()

    @staticmethod
    def ContinueOnFatalError():
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##if USE_STACKTRACE
        array = [None for _ in range(200)]
        size = None
        symbols = []

        size = backtrace(array, 200)
        symbols = backtrace_symbols(array, size)

        oss = std::ostringstream()
        oss << std::endl
        for i in range(0, size):
            oss << "  Stack> " << symbols[i] << std::endl

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'free' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
        free(symbols)

        #lani_err("FatalError on %s", oss.str().c_str())
    ##else
        #lani_err("FatalError")
    ##endif

    @staticmethod
    def ShutdownOnFatalError():
        if not Globals.g_bShutdown:
            #lani_err("ShutdownOnFatalError!!!!!!!!!!")
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##if __MULTI_LANGUAGE_SYSTEM__
                Globals.SendNotice(LC_TEXT("Critical server error. The server will be restarted automatically."))
                Globals.SendNotice(LC_TEXT("You will be disconnected in 10 seconds."))
                Globals.SendNotice(LC_TEXT("You can connect after 5 minutes."))
    ##else
                buf = str(['\0' for _ in range(256)])
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                strncpy_s(buf, sizeof(buf), LC_TEXT("Critical server error. The server will be restarted automatically."), _TRUNCATE)
                Globals.SendNotice(buf)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                strncpy_s(buf, sizeof(buf), LC_TEXT("You will be disconnected in 10 seconds."), _TRUNCATE)
                Globals.SendNotice(buf)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                strncpy_s(buf, sizeof(buf), LC_TEXT("You can connect after 5 minutes."), _TRUNCATE)
                Globals.SendNotice(buf)
    ##endif

            Globals.g_bShutdown = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
            g_bNoMoreClient = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

            Globals.g_shutdown_disconnect_pulse = Globals.thecore_pulse() + ((10) * passes_per_sec)
            Globals.g_shutdown_disconnect_force_pulse = Globals.thecore_pulse() + ((20) * passes_per_sec)
            Globals.g_shutdown_core_pulse = Globals.thecore_pulse() + ((30) * passes_per_sec)

## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern dict<uint, CLoginSim *> g_sim
## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern dict<uint, CLoginSim *> g_simByPID
## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern list<SPlayerTable> g_vec_save
    save_idx = 0

    @staticmethod
    def heartbeat(ht, pulse):
        t = None

        t = get_dword_time()
        Globals.num_events_called += Globals.event_process(pulse)
        Globals.s_dwProfiler[(int)EProfile.PROF_EVENT] += (get_dword_time() - t)

        t = get_dword_time()

        if (math.fmod(pulse, ht.passes_per_sec)) == 0:
            if not g_bAuthServer:
                pack = SPlayerCountPacket()
                pack.dwCount = DESC_MANAGER.instance().GetLocalUserCount()
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                db_clientdesc.DBPacket(Globals.LG_HEADER_GD_PLAYER_COUNT, 0, pack, sizeof(SPlayerCountPacket))
            else:
                DESC_MANAGER.instance().ProcessExpiredLoginKey()

                count = 0
                it = g_sim.begin()

                while it is not g_sim.end():
                    if not it.second.IsCheck():
                        it.second.SendLogin()

                        count += 1
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: if (++count > 50)
                        if count > 50:
                            #sys_log(0, "FLUSH_SENT")
                            break

                    it += 1

                if Globals.save_idx < g_vec_save.size():
                    count = MIN(100, g_vec_save.size() - Globals.save_idx)

                    i = 0
                    while i < count:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                        db_clientdesc.DBPacket(Globals.LG_HEADER_GD_PLAYER_SAVE, 0, g_vec_save[Globals.save_idx], sizeof(SPlayerTable))
                        i += 1
                        save_idx += 1

                    Globals.#sys_log(0, "SAVE_FLUSH %d", count)

        if not(math.fmod(pulse, (passes_per_sec + 4))):
            CHARACTER_MANAGER.instance().ProcessDelayedSave()

    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##if __FreeBSD__ && __FILEMONITOR__
        if not(math.fmod(pulse, (passes_per_sec * 5))):
            FileMonitorFreeBSD.Instance().Update(pulse)
    ##endif

        if not(math.fmod(pulse, (passes_per_sec * 5 + 2))):
            ITEM_MANAGER.instance().Update()
            DESC_MANAGER.instance().UpdateLocalUserCount()

        Globals.s_dwProfiler[(int)EProfile.PROF_HEARTBEAT] += (get_dword_time() - t)

        DBManager.instance().Process()
        AccountDB.instance().Process()
        CPVPManager.instance().Process()

        if Globals.g_bShutdown:
            if Globals.thecore_pulse() > Globals.g_shutdown_disconnect_pulse:
                c_set_desc = DESC_MANAGER.instance().GetClientSet()
                std::for_each(c_set_desc.begin(), c_set_desc.end(), SendDisconnectFunc())
                Globals.g_shutdown_disconnect_pulse = numeric_limits.max()
            elif Globals.thecore_pulse() > Globals.g_shutdown_disconnect_force_pulse:
                c_set_desc = DESC_MANAGER.instance().GetClientSet()
                std::for_each(c_set_desc.begin(), c_set_desc.end(), DisconnectFunc())
            elif Globals.thecore_pulse() > Globals.g_shutdown_disconnect_force_pulse + ((5) * passes_per_sec):
                Globals.thecore_shutdown()

    @staticmethod
    def CleanUpForEarlyExit():
        Globals.CancelReloadSpamEvent()

    @staticmethod
    def usage():
        print("Option list\n" + "-p <port>    : bind port number (port must be over 1024)\n" + "-l <level>   : sets log level\n" + "-v           : log to stdout\n" + "-r           : do not load regen tables\n" + "-t           : traffic proflie on\n", end = '')






    g_mapLocations = CMapLocation()



    @staticmethod
## Laniatus Games Studio Inc. | WARNING: Python has no equivalent to methods returning pointers to value types:
#ORIGINAL METINII C CODE: static uint * LoadOldGuildMarkImageFile()
    def LoadOldGuildMarkImageFile():
        fp = fopen(DefineConstants.OLD_MARK_DATA_FILENAME, "rb")

        if fp is None:
            #lani_err("cannot open %s", DefineConstants.OLD_MARK_INDEX_FILENAME)
            return None

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        dataSize = 512 * 512 * sizeof(uint)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to pointers to value types:
#ORIGINAL METINII C CODE: uint * dataPtr = (uint *) malloc(dataSize);
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'malloc' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
        dataPtr = malloc(dataSize)

        fread(dataPtr, dataSize, 1, fp)

        fclose(fp)

        return dataPtr

    @staticmethod
    def GuildMarkConvert(vecGuildID):
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##if _WIN32
        _mkdir("mark")
        if 0 != _access(DefineConstants.OLD_MARK_INDEX_FILENAME, 0):
    ##else
        mkdir("mark", S_IRWXU)
        if 0 != access(DefineConstants.OLD_MARK_INDEX_FILENAME, F_OK):
    ##endif
            return ((not DefineConstants.false))

    fp = fopen(DefineConstants.OLD_MARK_INDEX_FILENAME, "r")

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following statement was not recognized, possibly due to an unrecognized macro:
    if (NULL == fp)
    DefineConstants.false = return()

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to pointers to value types:
#ORIGINAL METINII C CODE: uint * oldImagePtr = LoadOldGuildMarkImageFile();
    oldImagePtr = LoadOldGuildMarkImageFile()

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following method format was not recognized, possibly due to an unrecognized macro:
    if (NULL == oldImagePtr)
        fclose(fp)
        return DefineConstants.false

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following statement was not recognized, possibly due to an unrecognized macro:
    #sys_log(0, "Guild Mark Converting Start.")

    line = str(['\0' for _ in range(256)])
    guild_id = 0
    mark_id = 0
    mark = [0 for _ in range(SGuildMark.SIZE)]

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following method format was not recognized, possibly due to an unrecognized macro:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    while (fgets(line, sizeof(line)-1, fp))
        sscanf(line, "%u %u", guild_id, mark_id)

        if find(vecGuildID.begin(), vecGuildID.end(), guild_id) == vecGuildID.end():
            Globals.#sys_log(0, "  skipping guild ID %u", guild_id)
            continue

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        row = mark_id / 32
        col = math.fmod(mark_id, 32)

        if row >= 42:
            #lani_err("invalid mark_id %u", mark_id)
            continue

        sx = col * 16
        sy = row * 12

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Pointer arithmetic is detected on this variable:
#ORIGINAL METINII C CODE: uint * src = oldImagePtr + sy * 512 + sx;
        src = oldImagePtr + sy * 512 + sx
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Pointer arithmetic is detected on this variable:
#ORIGINAL METINII C CODE: uint * dst = mark;
        dst = mark

        y = 0
        while y != SGuildMark.HEIGHT:
            x = 0
            while x != SGuildMark.WIDTH:
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: *(dst++) = *(src+x);
                *(dst) = *(src+x)
                dst += 1
                x += 1

            src += 512
            y += 1
        CGuildMarkManager.instance().SaveMark(guild_id, byte(int(mark)))
        line[0] = '\0'

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following statement was not recognized, possibly due to an unrecognized macro:
    free(oldImagePtr)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following statement was not recognized, possibly due to an unrecognized macro:
    fclose(fp)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following statement was not recognized, possibly due to an unrecognized macro:
    system("mv -f guild_mark.idx guild_mark.idx.removable")
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following statement was not recognized, possibly due to an unrecognized macro:
    system("mv -f guild_mark.tga guild_mark.tga.removable")

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following statement was not recognized, possibly due to an unrecognized macro:
    #sys_log(0, "Guild Mark Converting Complete.")

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following statement was not recognized, possibly due to an unrecognized macro:
    return (!DefineConstants.false)




    ## Laniatus Games Studio Inc. | NOTE: The following #define macro was replaced in-line:
    #ORIGINAL METINII C CODE: #define CLZO LZOManager

    @staticmethod
    def NewMarkImage():
        return LG_NEW_M2 CGuildMarkImage

    @staticmethod
    def DeleteMarkImage(pkImage):
        LG_DEL_MEM(pkImage)


    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##if __UNITTEST__

    @staticmethod
    def heartbeat(ht, pulse):
        return

    @staticmethod
    def SaveMark(guildID, filename):
        m_uImg = ILuint()

        ilGenImages(1, m_uImg)
        ilBindImage(m_uImg)
        ilEnable(IL_ORIGIN_SET)
        ilOriginFunc(IL_ORIGIN_UPPER_LEFT)

        if ilLoad(IL_TYPE_UNKNOWN, filename):
            width = ilGetInteger(IL_IMAGE_WIDTH)
            height = ilGetInteger(IL_IMAGE_HEIGHT)

            ilConvertImage(IL_BGRA, IL_UNSIGNED_BYTE)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to pointers to value types:
#ORIGINAL METINII C CODE: byte * data = (byte *) malloc(sizeof(uint) * width * height);
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'malloc' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            data = byte(int(malloc(sizeof(uint) * width * height)))
            ilCopyPixels(0, 0, 0, width, height, 1, IL_BGRA, IL_UNSIGNED_BYTE, data)
            ilDeleteImages(1, m_uImg)

            printf("%s w%u h%u ", filename, width, height)
            temp_ref_data = RefObject(data);
            CGuildMarkManager.instance().SaveMark(guildID, temp_ref_data)
            data = temp_ref_data.arg_value
        else:
            printf("%s cannot open file.\n", filename)


## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern bool g_bShutdown

    ## Laniatus Games Studio Inc. | NOTE: This was formerly a static local variable declaration (not allowed in Python):
    _flag = 0

    @staticmethod
    def (UnnamedParameter):
        ## Laniatus Games Studio Inc. | NOTE: This static local variable declaration (not allowed in Python) has been moved just prior to the method:
        #    static byte flag = 0
        info = if isinstance(event.info, OXEventInfoData) else None

        if info is None:
            #lani_err("oxevent_timer> <Factor> Null pointer")
            return 0

        if flag == 0:
            Globals.SendNoticeMap(LC_TEXT("The answer follows in 10 sec."), LGEMiscellaneous.DEFINECONSTANTS.OXEVENT_MAP_INDEX, ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
            flag += 1
            return ((10) * passes_per_sec)

        if (flag == 0) or (flag == 1):
            Globals.SendNoticeMap(LC_TEXT("The correct answer is"), LGEMiscellaneous.DEFINECONSTANTS.OXEVENT_MAP_INDEX, ((not LGEMiscellaneous.DEFINECONSTANTS.false)))

            if info.answer == ((not LGEMiscellaneous.DEFINECONSTANTS.false)):
                COXEventManager.instance().CheckAnswer(((not LGEMiscellaneous.DEFINECONSTANTS.false)))
                Globals.SendNoticeMap(LC_TEXT("Yes"), LGEMiscellaneous.DEFINECONSTANTS.OXEVENT_MAP_INDEX, ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
            else:
                COXEventManager.instance().CheckAnswer(LGEMiscellaneous.DEFINECONSTANTS.false)
                Globals.SendNoticeMap(LC_TEXT("No"), LGEMiscellaneous.DEFINECONSTANTS.OXEVENT_MAP_INDEX, ((not LGEMiscellaneous.DEFINECONSTANTS.false)))

            Globals.SendNoticeMap(LC_TEXT("After 5 seconds, the participants who gave a wrong answer have to leave."), LGEMiscellaneous.DEFINECONSTANTS.OXEVENT_MAP_INDEX, ((not LGEMiscellaneous.DEFINECONSTANTS.false)))

            flag += 1
            return ((5) * passes_per_sec)

        if (flag == 0) or (flag == 1) or (flag == 2):
            COXEventManager.instance().WarpToAudience()
            COXEventManager.instance().SetStatus(OXEventStatus.OXEVENT_CLOSE)
            Globals.SendNoticeMap(LC_TEXT("Ready for the next question."), LGEMiscellaneous.DEFINECONSTANTS.OXEVENT_MAP_INDEX, ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
            flag = 0
        return 0


    PARTY_ENOUGH_MINUTE_FOR_EXP_BONUS = 60
    PARTY_HEAL_COOLTIME_LONG = 60
    PARTY_HEAL_COOLTIME_SHORT = 30
    PARTY_MAX_MEMBER = 8
    PARTY_DEFAULT_RANGE = 5000

    @staticmethod
    def (UnnamedParameter):
        info = if isinstance(event.info, party_update_event_info) else None

        if info is None:
            #lani_err("party_update_event> <Factor> Null pointer")
            return 0

        pid = info.pid
        leader = CHARACTER_MANAGER.instance().FindByPID(pid)

        if leader is not None and leader.GetDesc() is not None:
            pParty = leader.GetParty()

            if pParty:
                pParty.Update()

        return ((3) * passes_per_sec)



## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern int passes_per_sec

    @staticmethod
    def (UnnamedParameter):
        info = if isinstance(event.info, petsystem_event_info) else None
        if info is None:
            #lani_err("check_speedhack_event> <Factor> Null pointer")
            return 0

        pPetSystem = info.pPetSystem

        if None is pPetSystem:
            return 0

        pPetSystem.Update(0)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        return ((1) * passes_per_sec) / 4

    PET_COUNT_LIMIT = 3



    @staticmethod
    def GetEmpireName(priv):
        return LC_TEXT(c_apszEmpireNames[priv])

    @staticmethod
    def GetPrivName(priv):
        return LC_TEXT(c_apszPrivNames[priv])




## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern int test_server
    extern void(do_in_game_mall)(CHARACTER* ch, const char *argument, int cmd, int subcmd)
    extern int(check_name)(const char * str)
## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern int g_nPortalLimitTime
    extern int(check_name)(const char * str)

    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##if __QUEST_RENEWAL__
    ## Laniatus Games Studio Inc. | WARNING: The following #include directive was ignored:
    ##include <_boost_func_of_void/tokenizer.hpp>
    ##endif

    g_GoldDropTimeLimitValue = 0

## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern int test_server


## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern int test_server

    BLACKSMITH_MOB = 20016
    ALCHEMIST_MOB = 20001
    GOLDEN_BLACKSMITH_MOB = 21900
    BLACKSMITH_WEAPON_MOB = 20044
    BLACKSMITH_ARMOR_MOB = 20045
    BLACKSMITH_ACCESSORY_MOB = 20046
    DEVILTOWER_BLACKSMITH_WEAPON_MOB = 20074
    DEVILTOWER_BLACKSMITH_ARMOR_MOB = 20075
    DEVILTOWER_BLACKSMITH_ACCESSORY_MOB = 20076
    BLACKSMITH2_MOB = 20091
    REGEN_TYPE_MOB = 0
    REGEN_TYPE_GROUP = 1
    REGEN_TYPE_EXCEPTION = 2
    REGEN_TYPE_GROUP_GROUP = 3
    REGEN_TYPE_ANYWHERE = 4
    REGEN_TYPE_MAX_NUM = 5

    @staticmethod
    def regen_load(filename, lMapIndex, base_x, base_y):
        if g_bNoRegen:
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        regen = None
        fp = fopen(filename, "rt")

        if None is fp:
            Globals.#sys_log(0, "SYSTEM: regen_load: %s: file not found", filename)
            return LGEMiscellaneous.DEFINECONSTANTS.false

        while ((not LGEMiscellaneous.DEFINECONSTANTS.false)):
            tmp = regen()

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            memset(tmp, 0, sizeof(tmp))

            if not Globals.read_line(fp, tmp):
                break

            if tmp.type == Globals.REGEN_TYPE_MOB or tmp.type == Globals.REGEN_TYPE_GROUP or tmp.type == Globals.REGEN_TYPE_GROUP_GROUP or tmp.type == Globals.REGEN_TYPE_ANYWHERE:
                if test_server:
                    CMobManager.instance().IncRegenCount(byte(tmp.type), uint(tmp.vnum), tmp.max_count, int(tmp.time))

                regen = LG_NEW_M2 regen
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memcpy' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                memcpy(regen, tmp, sizeof(regen))
                INSERT_TO_TW_LIST(regen, Globals.regen_list, prev, next)

                regen.lMapIndex = lMapIndex
                regen.count = 0

                regen.sx += base_x
                regen.ex += base_x

                regen.sy += base_y
                regen.ey += base_y

                if regen.sx > regen.ex:
                    regen.sx ^= regen.ex
                    regen.ex ^= regen.sx
                    regen.sx ^= regen.ex

                if regen.sy > regen.ey:
                    regen.sy ^= regen.ey
                    regen.ey ^= regen.sy
                    regen.sy ^= regen.ey

                if regen.type == Globals.REGEN_TYPE_MOB:
                    p = CMobManager.instance().Get(uint(regen.vnum))

                    if p is None:
                        #lani_err("No mob data by vnum %u", regen.vnum)
                    elif p.m_table.bType == ECharType.CHAR_TYPE_NPC or p.m_table.bType == ECharType.CHAR_TYPE_WARP or p.m_table.bType == ECharType.CHAR_TYPE_GOTO:
                        SECTREE_MANAGER.instance().InsertNPCPosition(lMapIndex, p.m_table.bType, p.m_table.szLocaleName, math.trunc((regen.sx+regen.ex) / float(2)) - base_x, math.trunc((regen.sy+regen.ey) / float(2)) - base_y)

                if regen.time != 0:
                    Globals.regen_spawn(regen, LGEMiscellaneous.DEFINECONSTANTS.false)

                    info = Globals.AllocEventInfo()

                    info.regen = regen

## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: regen->event = event_create_ex(regen_event, info, ((number(0, 16)) * passes_per_sec) + ((regen->time) * passes_per_sec));
                    regen.event.copy_from(Globals.event_create_ex(regen_event, info, ((number(0, 16)) * passes_per_sec) + ((regen.time) * passes_per_sec)))
            elif tmp.type == Globals.REGEN_TYPE_EXCEPTION:
                exc = None

                exc = LG_NEW_M2 regen_exception

                exc.sx = tmp.sx
                exc.sy = tmp.sy
                exc.ex = tmp.ex
                exc.ey = tmp.ey
                exc.z_section = tmp.z_section

                INSERT_TO_TW_LIST(exc, Globals.regen_exception_list, prev, next)

        fclose(fp)
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    @staticmethod
    def regen_do(filename, lMapIndex, base_x, base_y, pDungeon, bOnce = (!LGEMiscellaneous.DefineConstants.false)):
        if g_bNoRegen:
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        if lMapIndex >= 114 and lMapIndex <= 117:
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        regen = None
        fp = fopen(filename, "rt")

        if None is fp:
            #lani_err("SYSTEM: regen_do: %s: file not found", filename)
            return LGEMiscellaneous.DEFINECONSTANTS.false

        while ((not LGEMiscellaneous.DEFINECONSTANTS.false)):
            tmp = regen()

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            memset(tmp, 0, sizeof(tmp))

            if not Globals.read_line(fp, tmp):
                break

            if tmp.type == Globals.REGEN_TYPE_MOB or tmp.type == Globals.REGEN_TYPE_GROUP or tmp.type == Globals.REGEN_TYPE_GROUP_GROUP or tmp.type == Globals.REGEN_TYPE_ANYWHERE:
                if not bOnce:
                    regen = LG_NEW_M2 regen
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memcpy' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                    memcpy(regen, tmp, sizeof(regen))
                else:
                    regen = tmp

                if pDungeon:
                    regen.is_aggressive = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

                regen.lMapIndex = lMapIndex
                regen.count = 0

                regen.sx += base_x
                regen.ex += base_x

                regen.sy += base_y
                regen.ey += base_y

                if regen.sx > regen.ex:
                    regen.sx ^= regen.ex
                    regen.ex ^= regen.sx
                    regen.sx ^= regen.ex

                if regen.sy > regen.ey:
                    regen.sy ^= regen.ey
                    regen.ey ^= regen.sy
                    regen.sy ^= regen.ey

                if regen.type == Globals.REGEN_TYPE_MOB:
                    p = CMobManager.instance().Get(uint(regen.vnum))

                    if p is None:
                        #lani_err("No mob data by vnum %u", regen.vnum)
                        if not bOnce:
                            LG_DEL_MEM(regen)
                        continue

                if (not bOnce) and pDungeon is not None:
                    info = Globals.AllocEventInfo()

                    info.regen = regen
## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: info->dungeon_id = pDungeon->GetId();
                    info.dungeon_id.copy_from(pDungeon.GetId())

## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: regen->event = event_create_ex(dungeon_regen_event, info, ((number(0, 16)) * passes_per_sec) + ((regen->time) * passes_per_sec));
                    regen.event.copy_from(Globals.event_create_ex(dungeon_regen_event, info, ((number(0, 16)) * passes_per_sec) + ((regen.time) * passes_per_sec)))

                    pDungeon.AddRegen(regen)

                Globals.regen_spawn_dungeon(regen, pDungeon, bOnce)

        fclose(fp)
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    @staticmethod
    def regen_load_in_file(filename, lMapIndex, base_x, base_y):
        if g_bNoRegen:
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        regen = None
        fp = fopen(filename, "rt")

        if None is fp:
            #lani_err("SYSTEM: regen_do: %s: file not found", filename)
            return LGEMiscellaneous.DEFINECONSTANTS.false

        while ((not LGEMiscellaneous.DEFINECONSTANTS.false)):
            tmp = regen()

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            memset(tmp, 0, sizeof(tmp))

            if not Globals.read_line(fp, tmp):
                break

            if tmp.type == Globals.REGEN_TYPE_MOB or tmp.type == Globals.REGEN_TYPE_GROUP or tmp.type == Globals.REGEN_TYPE_GROUP_GROUP or tmp.type == Globals.REGEN_TYPE_ANYWHERE:
                regen = tmp

                regen.is_aggressive = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

                regen.lMapIndex = lMapIndex
                regen.count = 0

                regen.sx += base_x
                regen.ex += base_x

                regen.sy += base_y
                regen.ey += base_y

                if regen.sx > regen.ex:
                    regen.sx ^= regen.ex
                    regen.ex ^= regen.sx
                    regen.sx ^= regen.ex

                if regen.sy > regen.ey:
                    regen.sy ^= regen.ey
                    regen.ey ^= regen.sy
                    regen.sy ^= regen.ey

                if regen.type == Globals.REGEN_TYPE_MOB:
                    p = CMobManager.instance().Get(uint(regen.vnum))

                    if p is None:
                        #lani_err("No mob data by vnum %u", regen.vnum)
                        continue

                Globals.regen_spawn(regen, ((not LGEMiscellaneous.DEFINECONSTANTS.false)))

        fclose(fp)
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    @staticmethod
    def regen_free():
        regen = None
        next_regen = None
        exc = None
        next_exc = None

        regen = regen_list
        while regen:
            next_regen = regen.next

            Globals.event_cancel(regen.event)
            LG_DEL_MEM(regen)
            regen = next_regen

        Globals.regen_list = None

        exc = regen_exception_list
        while exc:
            next_exc = exc.next

            LG_DEL_MEM(exc)
            exc = next_exc

        Globals.regen_exception_list = None

    @staticmethod
    def is_regen_exception(x, y):
        exc = None

        exc = regen_exception_list
        while exc:
            if exc.sx <= x and exc.sy <= y:
                if exc.ex >= x and exc.ey >= y:
                    return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
            exc = exc.next

        return LGEMiscellaneous.DEFINECONSTANTS.false

    @staticmethod
    def regen_reset(x, y):
        regen = None

        regen = regen_list
        while regen:
            if regen.event is None:
                continue

            if x != 0 or y != 0:
                if x >= regen.sx and x <= regen.ex:
                    if y >= regen.sy and y <= regen.ey:
                        Globals.event_reset_time(_boost_func_of_void.intrusive_ptr(regen.event), 1)
            else:
                Globals.event_reset_time(_boost_func_of_void.intrusive_ptr(regen.event), 1)
            regen = regen.next


    regen_list = None
    regen_exception_list = None

    @staticmethod
    def get_word(fp, buf):
        i = 0
        c = None

        semicolon_mode = 0

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: while ((c = fgetc(fp)) != EOF)
        while (c = fgetc(fp)) != EOF:
            if i == 0:
                if c == '"':
                    semicolon_mode = 1
                    continue

                if c == ' ' or c == '\t' or c == '\n' or c == '\r':
                    continue

            if semicolon_mode != 0:
                if c == '"':
                    buf.arg_value[i] = '\0'
                    return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: buf[i++] = c;
                buf.arg_value[i] = c
                i += 1
            else:
                if (c == ' ' or c == '\t' or c == '\n' or c == '\r'):
                    buf.arg_value[i] = '\0'
                    return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: buf[i++] = c;
                buf.arg_value[i] = c
                i += 1

            if i == 2 and buf.arg_value[0] == '/' and buf.arg_value[1] == '/':
                buf.arg_value[i] = '\0'
                return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        buf.arg_value[i] = '\0'
        return (i != 0)

    @staticmethod
    def next_line(fp):
        c = None

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: while ((c = fgetc(fp)) != EOF)
        while (c = fgetc(fp)) != EOF:
            if c == '\n':
                return

    @staticmethod
    def read_line(fp, regen):
        szTmp = str(['\0' for _ in range(256)])

        mode = ERegenModes.MODE_TYPE
        tmpTime = None
        i = None

        temp_ref_szTmp = RefObject(szTmp);
        while Globals.get_word(fp, temp_ref_szTmp):
            szTmp = temp_ref_szTmp.arg_value
            if not strncmp(szTmp, "#", 2):
                Globals.next_line(fp)
                continue

            if mode == ERegenModes.MODE_TYPE:
                if szTmp[0] == 'm':
                    regen.type = Globals.REGEN_TYPE_MOB
                elif szTmp[0] == 'g':
                    regen.type = Globals.REGEN_TYPE_GROUP

                    if szTmp[1] == 'a':
                        regen.is_aggressive = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
                elif szTmp[0] == 'e':
                    regen.type = Globals.REGEN_TYPE_EXCEPTION
                elif szTmp[0] == 'r':
                    regen.type = Globals.REGEN_TYPE_GROUP_GROUP
                elif szTmp[0] == 's':
                    regen.type = Globals.REGEN_TYPE_ANYWHERE
                else:
                    #lani_err("read_line: unknown regen type %c", szTmp[0])
                    exit(1)

                mode += 1

            elif mode == ERegenModes.MODE_SX:
                temp_ref_sx = RefObject(regen.sx);
                Globals.str_to_number(temp_ref_sx, szTmp)
                regen.sx = temp_ref_sx.arg_value
                mode += 1

            elif mode == ERegenModes.MODE_SY:
                temp_ref_sy = RefObject(regen.sy);
                Globals.str_to_number(temp_ref_sy, szTmp)
                regen.sy = temp_ref_sy.arg_value
                mode += 1

            elif mode == ERegenModes.MODE_EX:
                    iX = 0
                    temp_ref_iX = RefObject(iX);
                    Globals.str_to_number(temp_ref_iX, szTmp)
                    iX = temp_ref_iX.arg_value

                    regen.sx -= iX
                    regen.ex = regen.sx + iX * 2

                    regen.sx *= 100
                    regen.ex *= 100

                    mode += 1

            elif mode == ERegenModes.MODE_EY:
                    iY = 0
                    temp_ref_iY = RefObject(iY);
                    Globals.str_to_number(temp_ref_iY, szTmp)
                    iY = temp_ref_iY.arg_value

                    regen.sy -= iY
                    regen.ey = regen.sy + iY * 2

                    regen.sy *= 100
                    regen.ey *= 100

                    mode += 1

            elif mode == ERegenModes.MODE_Z_SECTION:
                temp_ref_z_section = RefObject(regen.z_section);
                Globals.str_to_number(temp_ref_z_section, szTmp)
                regen.z_section = temp_ref_z_section.arg_value

                if regen.type == Globals.REGEN_TYPE_EXCEPTION:
                    return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

                mode += 1

            elif mode == ERegenModes.MODE_DIRECTION:
                temp_ref_direction = RefObject(regen.direction);
                Globals.str_to_number(temp_ref_direction, szTmp)
                regen.direction = temp_ref_direction.arg_value
                mode += 1

            elif mode == ERegenModes.MODE_REGEN_TIME:
                regen.time = 0
                tmpTime = 0

                i = 0
                while i < strlen(szTmp):
                    if szTmp[i] == 'h':
                        regen.time += uint(tmpTime * 3600)
                        tmpTime = 0

                    elif szTmp[i] == 'm':
                        regen.time += uint(tmpTime * 60)
                        tmpTime = 0

                    elif szTmp[i] == 's':
                        regen.time += uint(tmpTime)
                        tmpTime = 0

                    else:
                        if szTmp[i] >= '0' and szTmp[i] <= '9':
                            tmpTime *= 10
                            tmpTime += (szTmp[i] - '0')
                    i += 1

                mode += 1

            elif (mode == ERegenModes.MODE_REGEN_TIME) or (mode == ERegenModes.MODE_REGEN_PERCENT):
                mode += 1

            elif mode == ERegenModes.MODE_MAX_COUNT:
                regen.count = 0
                temp_ref_max_count = RefObject(regen.max_count);
                Globals.str_to_number(temp_ref_max_count, szTmp)
                regen.max_count = temp_ref_max_count.arg_value
                mode += 1

            elif mode == ERegenModes.MODE_VNUM:
                temp_ref_vnum = RefObject(regen.vnum);
                Globals.str_to_number(temp_ref_vnum, szTmp)
                regen.vnum = temp_ref_vnum.arg_value
                mode += 1
                return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
        szTmp = temp_ref_szTmp.arg_value

        return LGEMiscellaneous.DEFINECONSTANTS.false

    @staticmethod
    def regen_spawn_dungeon(regen, pDungeon, bOnce):
        num = None
        i = None

        num = uint((regen.max_count - regen.count))

        if num == 0:
            return

        for i in range(0, num):
            ch = None

            if regen.type == Globals.REGEN_TYPE_ANYWHERE:
                ch = CHARACTER_MANAGER.instance().SpawnMobRandomPosition(uint(regen.vnum), regen.lMapIndex)

                if ch:
                    regen.count += 1
                    ch.SetDungeon(pDungeon)
            elif regen.sx == regen.ex and regen.sy == regen.ey:
                ch = CHARACTER_MANAGER.instance().SpawnMob(uint(regen.vnum), regen.lMapIndex, regen.sx, regen.sy, regen.z_section, LGEMiscellaneous.DEFINECONSTANTS.false,number(0, 7) * 45 if regen.direction == 0 else (regen.direction - 1) * 45, ((not DefineConstants.false)))

                if ch:
                    regen.count += 1
                    ch.SetDungeon(pDungeon)
            else:
                if regen.type == Globals.REGEN_TYPE_MOB:
                    ch = CHARACTER_MANAGER.Instance().SpawnMobRange(uint(regen.vnum), regen.lMapIndex, regen.sx, regen.sy, regen.ex, regen.ey, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), DefineConstants.false, DefineConstants.false)

                    if ch:
                        regen.count += 1
                        ch.SetDungeon(pDungeon)
                elif regen.type == Globals.REGEN_TYPE_GROUP:
                    if CHARACTER_MANAGER.Instance().SpawnGroup(uint(regen.vnum), regen.lMapIndex, regen.sx, regen.sy, regen.ex, regen.ey,None if bOnce else regen, regen.is_aggressive, pDungeon):
                        regen.count += 1
                elif regen.type == Globals.REGEN_TYPE_GROUP_GROUP:
                    if CHARACTER_MANAGER.Instance().SpawnGroupGroup(uint(regen.vnum), regen.lMapIndex, regen.sx, regen.sy, regen.ex, regen.ey,None if bOnce else regen, regen.is_aggressive, pDungeon):
                        regen.count += 1

            if ch is not None and not bOnce:
                ch.SetRegen(regen)

    @staticmethod
    def regen_spawn(regen, bOnce):
        num = None
        i = None

        num = uint((regen.max_count - regen.count))

        if num == 0:
            return

        for i in range(0, num):
            ch = None

            if regen.type == Globals.REGEN_TYPE_ANYWHERE:
                ch = CHARACTER_MANAGER.instance().SpawnMobRandomPosition(uint(regen.vnum), regen.lMapIndex)

                if ch:
                    regen.count += 1
            elif regen.sx == regen.ex and regen.sy == regen.ey:
                ch = CHARACTER_MANAGER.instance().SpawnMob(uint(regen.vnum), regen.lMapIndex, regen.sx, regen.sy, regen.z_section, LGEMiscellaneous.DEFINECONSTANTS.false,number(0, 7) * 45 if regen.direction == 0 else (regen.direction - 1) * 45, ((not DefineConstants.false)))

                if ch:
                    regen.count += 1
            else:
                if regen.type == Globals.REGEN_TYPE_MOB:
                    ch = CHARACTER_MANAGER.Instance().SpawnMobRange(uint(regen.vnum), regen.lMapIndex, regen.sx, regen.sy, regen.ex, regen.ey, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), regen.is_aggressive, regen.is_aggressive)

                    if ch:
                        regen.count += 1
                elif regen.type == Globals.REGEN_TYPE_GROUP:
                    if CHARACTER_MANAGER.Instance().SpawnGroup(uint(regen.vnum), regen.lMapIndex, regen.sx, regen.sy, regen.ex, regen.ey,None if bOnce else regen, regen.is_aggressive, NULL):
                        regen.count += 1
                elif regen.type == Globals.REGEN_TYPE_GROUP_GROUP:
                    if CHARACTER_MANAGER.Instance().SpawnGroupGroup(uint(regen.vnum), regen.lMapIndex, regen.sx, regen.sy, regen.ex, regen.ey,None if bOnce else regen, regen.is_aggressive, NULL):
                        regen.count += 1

            if ch is not None and not bOnce:
                ch.SetRegen(regen)

    @staticmethod
    def (UnnamedParameter):
        info = if isinstance(event.info, dungeon_regen_event_info) else None

        if info is None:
            #lani_err("dungeon_regen_event> <Factor> Null pointer")
            return 0

        pDungeon = CDungeonManager.instance().Find(uint32_t(info.dungeon_id))
        if pDungeon is None:
            return 0

        regen = info.regen
        if regen.time == 0:
            regen.event = None

        Globals.regen_spawn_dungeon(regen, pDungeon, LGEMiscellaneous.DEFINECONSTANTS.false)
        return ((regen.time) * passes_per_sec)

    @staticmethod
    def (UnnamedParameter):
        info = if isinstance(event.info, regen_event_info) else None

        if info is None:
            #lani_err("regen_event> <Factor> Null pointer")
            return 0

        regen = info.regen

        if regen.time == 0:
            regen.event = None

        Globals.regen_spawn(regen, LGEMiscellaneous.DEFINECONSTANTS.false)
        return ((regen.time) * passes_per_sec)

    #{
    #    uint package;
    #    sectree_coord coord;
    #};

    ATTR_BLOCK = (1 << 0)
    ATTR_WATER = (1 << 1)
    ATTR_BANPK = (1 << 2)
    ATTR_OBJECT = (1 << 7)
## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern const byte gc_abSequence[DefineConstants.SEQUENCE_MAX_NUM]


    gc_abSequence = [0xaf,0xca,0x8a,0xcf,0x48,0xa7,0x54,0xc7,0xd7,0xdf,0x1,0x25,0x72,0xf7,0x6f,0x84, 0xbc,0x37,0x46,0xe3,0x24,0xda,0xa1,0xc8,0xee,0x36,0x7c,0x33,0x2f,0x98,0x76,0x5e, 0xe2,0x1,0x2e,0xab,0x29,0x3,0xf2,0x1,0xe2,0xf3,0xa5,0x56,0x6b,0x15,0x5a,0xa7, 0xcc,0x21,0x8b,0x70,0xfb,0xac,0x3a,0x6b,0xe3,0x36,0x9e,0x92,0x4e,0x16,0xf1,0x31, 0x96,0x9f,0x5c,0x3f,0xa2,0x50,0xbf,0x6,0xc3,0x66,0xdb,0x30,0xfa,0xb5,0xd7,0x47, 0xd6,0xe3,0xb8,0x53,0x90,0x72,0xbe,0xf3,0xa8,0xdc,0x7,0x76,0x72,0x78,0xa7,0xa, 0x18,0x84,0xc8,0x3b,0xd4,0x89,0x41,0x18,0xef,0x9c,0x48,0x6a,0x52,0xa0,0xb2,0xa9, 0x4,0xea,0x7c,0x94,0xdc,0x3b,0x9,0x85,0x97,0x10,0x7b,0xb,0x88,0x23,0x94,0x20, 0x27,0x5d,0xda,0xfb,0xe6,0x1c,0x15,0x56,0x38,0xdc,0xc1,0xb,0xfc,0xf3,0xb4,0x1, 0xde,0x31,0x16,0xbb,0xeb,0x9e,0xc0,0x83,0x2e,0x3c,0xe,0x36,0xde,0xa2,0x56,0x86, 0x80,0x32,0x82,0xe6,0xcd,0x17,0x3e,0x86,0x74,0x7f,0x91,0xf0,0x73,0x46,0xf2,0xd1, 0xf6,0x88,0xd,0x62,0x27,0x4d,0x65,0x55,0x9,0x74,0xb,0x67,0x96,0x61,0xed,0x17, 0x13,0xf0,0xfe,0xe1,0x87,0xbc,0xe7,0xfb,0x3c,0x79,0x6d,0xaf,0x3f,0x60,0x1,0x36, 0x68,0xe,0x18,0xf,0x5b,0x7d,0xe3,0x64,0x71,0xee,0xcb,0x9,0xcf,0x3a,0x9f,0xe3, 0x2b,0x1e,0x45,0xb2,0xda,0x2d,0x2f,0x96,0xa6,0x9c,0x46,0xe5,0x7c,0xc6,0x9b,0xe4, 0xd4,0xb3,0x73,0xaf,0xb0,0x57,0x93,0x23,0x46,0xdf,0xab,0x16,0x1a,0x4b,0x79,0x45, 0x6a,0xbe,0xf7,0xc4,0xeb,0xa6,0x5c,0x12,0x43,0x22,0x77,0xbf,0xe9,0x92,0x24,0x3e, 0x46,0x97,0xee,0x77,0xee,0x82,0x9a,0xb4,0x62,0xc5,0x4b,0xfb,0x11,0xc4,0x41,0xfa, 0x84,0xb9,0x40,0xef,0x60,0x9c,0x82,0xa4,0x3e,0xf9,0x64,0xa7,0x8d,0x89,0xe6,0x53, 0xa0,0x55,0x4a,0x90,0x57,0x64,0x45,0x3a,0x2a,0x90,0x36,0x3c,0xd5,0x78,0xb6,0xd9, 0x32,0xf6,0x49,0x12,0x13,0xcb,0xb6,0xd1,0x46,0x9b,0x79,0x53,0xa4,0xdf,0x26,0x45, 0xb4,0x71,0x55,0xd,0xd5,0x9b,0x47,0x80,0xab,0x7d,0x3c,0x81,0x75,0xf2,0xda,0x27, 0x6a,0x25,0x3a,0x7d,0xf0,0xf0,0xce,0xb6,0xc,0x49,0xa,0xb0,0xa8,0xb0,0x76,0x5e, 0x22,0xcb,0x6b,0x77,0xe6,0x32,0x77,0x13,0x2f,0xb3,0x94,0xa5,0xa7,0xef,0x4c,0x12, 0x15,0x86,0xf,0x85,0xf7,0xde,0x3d,0x83,0xa7,0x47,0x35,0x50,0x77,0x2b,0xae,0x99, 0xf6,0x99,0x91,0xde,0xcb,0x9,0xf1,0x7b,0xbd,0x6,0x21,0xe4,0xf5,0x6d,0xf6,0x8a, 0x74,0x85,0x11,0xeb,0x64,0x4e,0x6f,0xc,0x15,0xa4,0xdc,0x8d,0x4f,0xb,0xa6,0x47, 0xa5,0xb7,0xa5,0xf0,0x41,0x17,0x6c,0xfe,0x9c,0xd,0x63,0x93,0x7b,0xd9,0x9d,0x6f, 0x5f,0xae,0x5b,0x44,0xfc,0xca,0xcf,0x13,0xef,0xac,0x20,0x3f,0xb8,0xc6,0x6,0xdd, 0xfe,0xab,0xce,0x40,0x42,0x3c,0x3f,0xdf,0x49,0x22,0xf2,0x44,0xfb,0x90,0xb3,0xda, 0x40,0x8e,0x1f,0x3d,0xd9,0xef,0xcf,0xc9,0x1c,0xef,0x88,0xd4,0x37,0x8f,0xb2,0x36, 0xba,0x82,0xf5,0xfd,0x3e,0xb4,0xdd,0x7,0xd6,0xd0,0x4c,0xd2,0x61,0x7f,0xad,0xa1, 0xf,0x4d,0x5f,0xe8,0x3d,0x2f,0x32,0x59,0x9f,0xba,0xae,0x56,0xc9,0x61,0xc,0x85, 0x63,0x2,0x3,0x21,0xb6,0xe0,0x29,0xd,0xb1,0xf4,0xdf,0x92,0x74,0xd,0xb4,0x3, 0x5a,0x14,0x6b,0x17,0xc2,0x1d,0xf0,0xe1,0x58,0x9f,0x38,0x22,0x80,0xc3,0xa7,0x64, 0x45,0xaa,0x85,0xfb,0xb,0x2e,0x88,0x3c,0x23,0x68,0xcf,0x18,0xf5,0x84,0x1b,0xcf, 0x18,0x7,0xe7,0xda,0x24,0xd8,0xbd,0x7c,0xf7,0xf5,0x1f,0xf7,0x3a,0x46,0x5c,0x7f, 0x71,0x62,0xfb,0x7c,0x90,0x84,0xb9,0x34,0x6d,0x9,0x4c,0x63,0xd,0xe6,0xb2,0x25, 0x6d,0x1a,0x0,0x12,0x72,0x3d,0xe,0x6a,0xb3,0x2d,0x63,0xed,0x74,0x3f,0x6d,0xe5, 0xa1,0x69,0xe1,0xb2,0x6e,0x1b,0xe6,0xdb,0x24,0x33,0xbe,0xb0,0x99,0x71,0xd5,0x8, 0x8c,0x56,0x1a,0xfe,0x93,0x28,0xe9,0x47,0x56,0xcc,0xb4,0x4a,0xc,0x23,0xaf,0xae, 0xc,0x91,0xe0,0x7a,0xad,0xc7,0xd5,0x51,0x7a,0x94,0x82,0x14,0x86,0x58,0x9b,0x13, 0x2e,0xb5,0x91,0x42,0x5e,0xfa,0x9,0x34,0xc7,0xbe,0x7e,0xd4,0xe1,0x2e,0x3,0x6d, 0x3f,0xe3,0x68,0x6c,0x2b,0x3e,0xbe,0xa5,0xd3,0x41,0x39,0x5a,0x19,0xd5,0xec,0xc7, 0xb,0xfd,0xa,0x69,0xf9,0x92,0x9d,0xc1,0x51,0x9b,0x16,0xb2,0x49,0x98,0x21,0x9, 0x7c,0x89,0x75,0xa7,0xc7,0x34,0xcc,0x1b,0xf4,0x7,0xf4,0x8e,0xdc,0xe1,0x56,0xe7, 0x60,0xdf,0xd1,0x5a,0x72,0xee,0x9b,0x44,0xb,0x32,0xf6,0x54,0xca,0x18,0x5d,0xc7, 0x21,0x53,0xee,0x69,0x7,0xbc,0x4,0xfc,0x43,0xf9,0xb,0x9f,0x5b,0xe0,0x7,0xbb, 0x40,0xd8,0x16,0xb2,0x48,0x32,0xf6,0x53,0x64,0x6e,0x27,0xae,0x6,0x5,0x76,0x28, 0x58,0xe5,0x11,0x5f,0x22,0x15,0xdb,0x65,0x8e,0xe6,0x5,0xea,0xc7,0x8b,0xa6,0x8, 0x65,0x3d,0x3b,0xad,0x6f,0xb1,0x80,0x53,0x20,0xa7,0x2,0x27,0xac,0xf8,0xce,0x5, 0xde,0x5f,0xe4,0x80,0xf3,0xc0,0xe5,0x83,0xa8,0x6a,0x6e,0xef,0xf5,0x94,0x78,0xda, 0xd1,0x33,0x8,0xc0,0xe4,0x88,0x14,0x85,0xb0,0x96,0x2c,0x5d,0x8f,0xfa,0xe2,0xed, 0xd9,0xc7,0x6e,0xcd,0x8,0x54,0x51,0x30,0x3e,0x3f,0x21,0xb3,0xd4,0x19,0x8f,0x26, 0x4c,0x17,0x67,0xb0,0xa0,0x7b,0x36,0xd0,0x12,0x62,0x2e,0x21,0xdc,0x90,0xf,0xb6, 0x58,0x7d,0x85,0xe0,0x51,0x56,0x11,0x8f,0x96,0x32,0xc3,0xea,0xca,0xd2,0x90,0x96, 0xe9,0xf7,0x48,0xa,0xf3,0xfd,0xda,0x6,0x61,0x89,0xa7,0xbd,0x1a,0xb6,0xf4,0xf2, 0x35,0x7a,0xd3,0x6,0x50,0xe4,0x16,0xe6,0x97,0xd9,0x51,0xe1,0xac,0xe2,0x79,0x16, 0xda,0xc1,0x21,0xce,0xbf,0x7b,0x55,0xa0,0x5,0xfc,0xde,0x9f,0x33,0xd3,0x92,0xe7, 0xcd,0xe5,0xee,0x1e,0x4a,0x5,0x6,0x61,0x5e,0xd6,0x44,0xb,0xb9,0xbd,0xa0,0x15, 0xfe,0xc1,0x63,0xbe,0xbd,0xb8,0xdf,0x42,0x35,0xbe,0xe1,0xe8,0x92,0xf3,0xd0,0x60, 0x59,0x3f,0x7e,0xa4,0x44,0x4,0x6,0x22,0xdb,0x4a,0x2d,0x15,0x87,0xce,0x2a,0x86, 0x10,0x8e,0xc5,0x4d,0xc6,0xa5,0x90,0x7c,0x64,0xf1,0x65,0x76,0xe6,0xb5,0x56,0x40, 0xf5,0x54,0xe4,0xb9,0xd8,0x6b,0xdc,0x34,0x35,0x89,0x49,0xbd,0xd7,0xf3,0xc3,0x68, 0x2,0x89,0xb5,0xc8,0x2f,0x46,0xc4,0x13,0xb8,0xa9,0x9,0x9f,0x60,0x5f,0x5f,0xd5, 0x34,0x45,0xf,0xd,0x30,0xeb,0x41,0x65,0x76,0x8a,0xa2,0xcd,0xfd,0x67,0x36,0x0, 0xf0,0x6c,0x49,0xa0,0x32,0xe,0x33,0xea,0x38,0x3d,0x8a,0x18,0x1c,0xea,0xed,0x50, 0xaf,0xfc,0x5d,0xdf,0x69,0x9e,0xc4,0x5f,0xa9,0xe7,0x2d,0xa7,0x4f,0x64,0xa8,0xbf, 0x50,0xf1,0xdf,0x82,0x7f,0x14,0x6e,0xb7,0xd0,0xf8,0xcf,0xec,0x63,0x3d,0xbd,0x13, 0xba,0x1b,0x72,0x24,0x3a,0xb7,0x83,0xe3,0x9f,0x30,0xb,0x6e,0x94,0x33,0xad,0x64, 0xa4,0x8e,0xe7,0x25,0x22,0x56,0x5c,0x72,0x4f,0xac,0xde,0xb3,0x69,0x9c,0x46,0x24, 0xb8,0x39,0x48,0x72,0xf0,0x4b,0xd5,0x10,0x7c,0xe0,0x7e,0x90,0x15,0x2c,0xf5,0xb9, 0x3a,0xdd,0x5e,0xdb,0x34,0x3b,0x4e,0x3,0xe7,0x2e,0x36,0x51,0xca,0x7d,0x76,0x3, 0x36,0x3e,0xf4,0x27,0x8a,0xca,0x37,0x7,0x2c,0x35,0x17,0xc0,0xe0,0xd,0x7a,0x1c, 0xea,0x59,0xf7,0x9e,0x94,0xc6,0xa2,0x7c,0x74,0xd8,0x4d,0x3f,0xd5,0x43,0xc2,0xc, 0x82,0x37,0xb2,0x8c,0x3,0x69,0x13,0x2f,0x9e,0x2a,0xef,0x80,0xb7,0xe9,0x1c,0x22, 0xc2,0x93,0xc1,0x57,0x5a,0x64,0x53,0xce,0xbc,0xa1,0x8e,0x13,0x64,0xd0,0x9e,0x66, 0x8,0x52,0x72,0xb,0xbb,0x85,0xb9,0xda,0x30,0x29,0x5b,0xe7,0x93,0xf6,0xa,0x56, 0x8a,0x4b,0x2e,0x65,0x2f,0x81,0x34,0xec,0xa2,0x42,0x0,0x8,0x13,0x1e,0xed,0x9b, 0x70,0x61,0x26,0xac,0xe6,0x60,0x87,0x96,0x89,0x62,0xfd,0x9c,0xd8,0x88,0xf3,0x63, 0xd3,0xa1,0xc8,0x4,0x23,0x7d,0x70,0x46,0x3f,0xef,0xcd,0xd2,0xe,0xbb,0x6e,0x7f, 0x1d,0x94,0xab,0x84,0xf4,0xb2,0x1b,0xfe,0x94,0x99,0x9b,0x6d,0x22,0xf,0xd0,0xf5, 0xb0,0x1a,0x79,0x54,0x17,0x69,0x9a,0x56,0x59,0x68,0x29,0x68,0x24,0x97,0x67,0xc1, 0xac,0x92,0x46,0xa1,0x45,0x61,0xa0,0xd9,0xfa,0xbc,0x47,0x9c,0xcb,0x97,0x13,0xfc, 0x31,0xc,0x51,0x48,0x76,0x6b,0x1f,0xcf,0xd3,0xc7,0x38,0x77,0xdf,0x1f,0x39,0x8c, 0xb1,0xfe,0xad,0xf6,0x61,0xce,0x50,0xdb,0x8b,0x17,0xf8,0xd6,0x2f,0xc,0xd3,0x60, 0x18,0xa4,0x29,0x8e,0x10,0xc7,0xde,0x63,0x8f,0x96,0xdb,0x6f,0xb6,0x94,0x7b,0xe7, 0x94,0x2a,0x5f,0x75,0xf8,0xaf,0xd0,0x4,0xc7,0xc9,0xda,0x76,0x55,0xaf,0xd6,0xed, 0x54,0x7f,0x7c,0x65,0x47,0x5b,0xc8,0xd7,0xf2,0x24,0xc6,0x29,0xb9,0xc2,0x11,0xcd, 0xec,0x70,0x43,0x65,0xa0,0x93,0x69,0xe7,0xdd,0xc3,0x5e,0x33,0x73,0xb4,0x21,0x48, 0x35,0x1e,0xad,0x7c,0xf8,0xf5,0xd3,0x6b,0x9a,0x9b,0x94,0xd3,0x5e,0x26,0xa1,0xca, 0x96,0x64,0xaf,0xb6,0xf7,0x98,0x9e,0xd5,0x5c,0x7c,0x89,0x50,0x32,0xaa,0x98,0x67, 0x48,0x46,0xe3,0x42,0xbb,0xb8,0xad,0x56,0xd3,0x43,0x2a,0xb1,0xe8,0x4b,0xfb,0x7f, 0xaf,0xab,0xb6,0x28,0xc3,0xd4,0x7d,0x9f,0x52,0x7,0xef,0x4,0x32,0x88,0xea,0x7a, 0x4e,0xce,0xbc,0xb,0x7,0xea,0xe0,0x5a,0xad,0x8b,0xc,0x96,0x56,0x87,0x95,0x7, 0xb2,0x4c,0xae,0x76,0xa1,0x2c,0x17,0x73,0xb3,0x7,0x77,0xe5,0x10,0x62,0xdf,0x5e, 0xb0,0x1d,0xe8,0x38,0x8,0x4a,0x92,0xb5,0xd5,0x1f,0xcb,0x2c,0xa6,0x61,0xb2,0x5a, 0x2e,0x61,0x50,0xcf,0xe,0x67,0x43,0xc1,0xee,0xba,0x27,0xfe,0x9c,0x7,0x5d,0x4d, 0x24,0xc6,0x5,0x2c,0x11,0x98,0x61,0xe6,0x37,0x2d,0x92,0xdd,0xf,0xc5,0x38,0x3d, 0xa6,0x89,0xd,0xb4,0x70,0xcf,0xf5,0x5f,0x8a,0x1d,0xdd,0xa6,0x25,0x3c,0x73,0xc8, 0x3,0x79,0x75,0x14,0x91,0x56,0x7a,0xc8,0x84,0x8c,0xa6,0x13,0x52,0x5f,0x50,0xf9, 0x68,0xdc,0x2e,0x58,0xac,0x25,0x38,0xb6,0xc1,0x16,0x5d,0x66,0x52,0x50,0x30,0xd4, 0xc9,0xa5,0x68,0x5b,0xfb,0x62,0xa3,0x0,0xef,0x4b,0x13,0x42,0x2a,0xe2,0xbb,0x12, 0xbf,0xea,0x6a,0x6c,0x10,0xa2,0xa2,0xd1,0xb9,0x0,0x39,0x8b,0x51,0xe8,0xe0,0x9a, 0xe,0x49,0x76,0xa,0xac,0x1a,0x8a,0x1c,0x65,0x1d,0x5e,0xf,0x1,0x1b,0x21,0x40, 0x85,0xc,0x2d,0x95,0xae,0xcf,0xe6,0xe7,0x50,0x9f,0x74,0xa1,0x88,0x55,0xbb,0x96, 0x1e,0x32,0x21,0x4a,0x4d,0x2b,0x66,0x32,0x48,0xc5,0x42,0xc8,0x60,0xe2,0x89,0xe5, 0xee,0xb6,0xfa,0x1e,0x6,0x61,0x6,0x56,0x2,0xf9,0x77,0xa,0xce,0x34,0xa1,0xed, 0x66,0x42,0x38,0xb3,0x6d,0x9f,0xe6,0xb5,0xe4,0xa8,0xfe,0xc4,0x8b,0x88,0x2a,0xfa, 0xbe,0x25,0x19,0xc4,0x6,0x9e,0x9b,0x8,0x99,0x13,0x13,0xe7,0x47,0x34,0xd5,0xae, 0x76,0x8e,0x62,0xe3,0xad,0xc8,0x19,0x92,0x71,0x97,0x57,0xfd,0x9f,0x81,0xf8,0x5e, 0x26,0x91,0xa3,0x2c,0x30,0x3f,0xb4,0x49,0xd1,0x47,0x32,0x1a,0x7b,0x87,0x48,0x71, 0x16,0x2a,0x55,0xc3,0xf3,0xed,0xd5,0x65,0x6,0xac,0xe2,0xa5,0xad,0x5b,0x84,0xd3, 0x6c,0x28,0x80,0x1d,0xe6,0x35,0x66,0xb8,0x7c,0x18,0xd2,0x77,0xa0,0x9a,0xe8,0x36, 0xc5,0xbd,0x7a,0xb9,0x2b,0x50,0x9e,0x31,0x7d,0x2,0xd7,0x2b,0xdc,0x5c,0x7f,0x4a, 0x4,0x0,0x67,0xea,0xb4,0x4d,0x23,0xb0,0x66,0x76,0x28,0x7,0x11,0x90,0xbc,0xd6, 0x4e,0x37,0x10,0x79,0x8,0xaf,0x2b,0x85,0x31,0x3,0xb0,0xe,0xde,0x30,0xd7,0x62, 0xaf,0xbe,0xcc,0xe3,0xd,0xef,0x14,0x73,0x66,0xbb,0xf9,0xf7,0x4c,0xb6,0xce,0x1a, 0xee,0xdf,0x94,0x76,0xf,0xbf,0xfb,0xbf,0x42,0xac,0xcd,0xa0,0x5d,0x26,0x3,0x8c, 0xe4,0xcf,0xf0,0xf1,0xbf,0x5,0xe4,0xa6,0xc1,0x5e,0x9e,0xe,0x16,0xec,0xa8,0x84, 0xcc,0x3d,0xfa,0x5b,0x7c,0x76,0x1b,0x3e,0x23,0x69,0xde,0x0,0x8f,0xe1,0xd,0xf3, 0xb1,0xfd,0x66,0xf0,0x82,0x4b,0x97,0x44,0x2a,0xb5,0xd2,0x40,0xa3,0x7b,0x44,0x70, 0x38,0xbe,0x4c,0x34,0x35,0xe6,0x72,0xd7,0x50,0xd0,0xd8,0x5f,0xb2,0x65,0xd3,0xe3, 0xe2,0x3a,0xd4,0x65,0x5,0xec,0x2a,0x2f,0xa2,0xfc,0xee,0x46,0xf7,0x33,0x37,0xaf, 0x71,0x3,0xe3,0xa6,0xe9,0xd5,0x7f,0x3b,0xa6,0xd7,0x1a,0x59,0xbc,0xed,0x3d,0x9f, 0xa7,0x91,0x5,0xad,0x7e,0x2f,0x5c,0xa1,0xab,0x4c,0x67,0xa3,0xfe,0x9e,0x53,0x71, 0xa1,0xb6,0x97,0x8c,0x8c,0x17,0x47,0x33,0x6e,0xe0,0xc,0x2b,0x4f,0x49,0xca,0xf6, 0x5b,0x50,0x24,0x59,0x7f,0x81,0xfa,0xab,0x4d,0xe2,0xce,0xcb,0x81,0xa2,0xbc,0xa3, 0x59,0x55,0xaf,0xe6,0xeb,0xf6,0x99,0xda,0xd7,0xa6,0x6,0xa6,0x6f,0x51,0x9e,0xca, 0xa1,0xc2,0xa4,0xa0,0xc3,0x1f,0xcb,0x11,0x2,0x9b,0xdd,0x84,0x3e,0x9a,0xa7,0x17, 0x6f,0x57,0xfd,0x5c,0x4e,0x18,0x37,0xa5,0xbe,0xbc,0x4d,0x2e,0x8d,0x6b,0x79,0xae, 0x2e,0x1e,0x50,0xf2,0x3d,0x9b,0x83,0xbf,0x37,0xe0,0x44,0xf4,0xfb,0x6b,0xd,0x6b, 0xc2,0x8a,0x47,0x90,0xa2,0xfd,0x36,0x61,0xbb,0x3,0x90,0x49,0x6e,0xa,0x78,0x1d, 0xa7,0xc8,0x8f,0x64,0xe3,0x13,0x24,0x1c,0x74,0xe7,0x90,0x70,0x53,0x9d,0x5b,0x16, 0x29,0xa3,0xa6,0xcb,0xa1,0x5d,0xad,0xdc,0xdf,0xbd,0xa6,0x4f,0x47,0x1f,0xeb,0xee, 0x67,0xfa,0x53,0x4b,0xe,0xf7,0xe6,0x2,0xdf,0x78,0x72,0x34,0x95,0x4e,0x4a,0xbe, 0xf1,0x71,0xb,0x13,0xce,0xb8,0x70,0xae,0xf5,0x96,0x7d,0x3d,0xb5,0xe8,0x2c,0x9c, 0xe3,0xfe,0x67,0x72,0xf6,0xce,0x74,0xd7,0x47,0x67,0x8b,0x5c,0xb5,0x55,0x1c,0x27, 0xc6,0xa6,0x3a,0x15,0xde,0x2a,0x44,0xd4,0xc0,0x41,0x12,0xf5,0x2b,0xbd,0x92,0x8e, 0xbc,0x7a,0x1,0x34,0x49,0xf5,0x8b,0x10,0xdc,0x17,0x6c,0x92,0xeb,0x88,0xb9,0xb3, 0x2f,0x73,0x48,0x8d,0x9e,0x8c,0x62,0xde,0x4e,0x74,0xd5,0x79,0xb1,0x68,0x8,0x6f, 0xe2,0x89,0x23,0x2c,0xfe,0x2e,0x3c,0xdb,0xc4,0x29,0xed,0xb0,0xb1,0xa7,0xe3,0x61, 0x9a,0x2d,0xee,0xb8,0x39,0xd1,0x98,0x87,0x46,0xed,0x80,0xf8,0x56,0x9,0xe7,0xb9, 0x12,0x8a,0x65,0x11,0xb8,0x22,0xec,0x7d,0x4b,0xda,0xad,0x7c,0x2,0x92,0x5d,0x1c, 0x3f,0x4d,0xd5,0xf7,0x1f,0xed,0x80,0xe4,0xdb,0x80,0x5d,0xb1,0x89,0xc4,0xea,0x9b, 0x4f,0x51,0x2c,0x87,0xf2,0x19,0x84,0xbd,0x73,0x33,0x3a,0x75,0x45,0x98,0x12,0x84, 0x65,0x67,0x7c,0x4,0xd4,0x7c,0xe8,0xb0,0xfd,0xc6,0xe1,0x87,0x8b,0x4d,0xa3,0x5b, 0x1e,0xcf,0x62,0x11,0x69,0xe7,0xce,0x5c,0x1b,0x88,0x52,0x60,0x21,0x64,0x64,0x86, 0xcb,0xe0,0xa,0xa0,0x5e,0xf3,0xd0,0xdb,0x3a,0x32,0xe2,0x45,0x7f,0x86,0xa0,0x9d, 0xd6,0x4,0x2e,0xbf,0x6b,0xfc,0x1c,0x86,0x86,0x6e,0x66,0x27,0xd2,0xca,0x2e,0x1e, 0x2b,0x38,0x3e,0x89,0xab,0xf,0xe4,0x65,0xc1,0xc8,0xab,0x41,0x4f,0x4c,0x5f,0xa5, 0xcf,0x8d,0xe4,0x3b,0xb,0x2,0x41,0x11,0x70,0xa7,0x38,0xc3,0xf1,0xe5,0x61,0x1e, 0x1f,0xa0,0x27,0x4a,0x2f,0xd,0xb0,0xf0,0xd5,0x5c,0xb2,0xa4,0x28,0x12,0xca,0xf8, 0x1f,0xaf,0xb3,0x2a,0xb1,0xf5,0x3b,0xa2,0x1d,0xf3,0xe5,0x8f,0xd9,0x47,0xad,0x78, 0x67,0x54,0xc3,0x97,0xe0,0xf3,0x8,0x36,0x50,0x3a,0x5b,0xf7,0xcb,0xa5,0x70,0xeb, 0x55,0x25,0x16,0x87,0x9a,0xd1,0xa9,0xb7,0xc5,0xf,0x47,0x9f,0xd5,0x74,0x98,0x3e, 0x49,0xdb,0x55,0xa9,0xcf,0xdc,0x60,0x9f,0x18,0xbb,0x97,0xe3,0x61,0x9,0x4f,0x36, 0xad,0xe5,0x3d,0x48,0xb7,0xe6,0x7f,0xfc,0xf5,0x47,0x1c,0x4c,0x3b,0xb4,0x8a,0x84, 0x90,0x5f,0xae,0x60,0x3c,0xf,0x0,0xd3,0xca,0x18,0x38,0xab,0x21,0x87,0xe1,0x4e, 0x6d,0x20,0x96,0x25,0x86,0x95,0xa1,0xfc,0xdc,0xbe,0x49,0x19,0x73,0x53,0x1d,0x5, 0xb2,0xcb,0xe4,0x6e,0xda,0x65,0x43,0x25,0x7d,0x7b,0x50,0x1e,0x3,0x33,0x6c,0xf0, 0xd2,0x82,0x95,0xd8,0x18,0x38,0xd5,0xf5,0xf6,0x1f,0x8e,0x6a,0xf1,0x2b,0xee,0xa4, 0xf7,0xd4,0x14,0x52,0x3a,0xd6,0xf7,0xb7,0x52,0x48,0xd5,0xd4,0xfa,0xc1,0xc5,0xcd, 0x44,0x5c,0x27,0x5c,0x94,0xfc,0xd1,0x8b,0x9c,0xdf,0x75,0x8e,0xc,0x65,0xb3,0x83, 0x3a,0xc7,0x55,0xf3,0x1e,0x4d,0x2b,0x70,0x16,0x80,0x45,0x11,0x42,0x8b,0x5f,0x6, 0xe7,0x86,0x62,0xfb,0x83,0xb4,0x7,0x9f,0x94,0x7c,0x2f,0x20,0xe1,0xe2,0xa3,0x9b, 0x2a,0xf9,0xf,0x48,0xc6,0x3a,0x38,0xdc,0x3a,0xfc,0xee,0x7c,0x88,0x4e,0x82,0xef, 0x54,0x65,0xeb,0xd7,0x99,0x72,0xf7,0x2e,0xef,0x27,0x4f,0x51,0x89,0x72,0x6d,0xb3, 0xeb,0x7c,0x7b,0xb3,0x37,0xb3,0x90,0x71,0xb0,0xfe,0xee,0xb9,0xcc,0xf0,0xa9,0x21, 0xd5,0x16,0x79,0x6f,0x88,0x71,0x1e,0xf7,0x18,0xec,0x4a,0xa1,0x5f,0xb7,0xd4,0x4c, 0xb3,0xcf,0x7f,0xea,0x83,0x8f,0x5d,0xb3,0x8f,0xcb,0xec,0x5c,0x3c,0x97,0xfd,0x13, 0x2d,0x77,0x82,0xb5,0x68,0xa0,0x2e,0x80,0xd,0x78,0xa1,0x6d,0xaf,0xf5,0x39,0x63, 0xc5,0xb8,0x4f,0xc8,0xc7,0x2c,0xfb,0x57,0xf7,0xe9,0x34,0x34,0x1,0x32,0xc6,0x2e, 0x29,0x4a,0x63,0x91,0x6a,0x91,0x91,0x78,0xa,0x33,0x65,0xb9,0xa8,0x1e,0x9d,0x6e, 0x56,0x6c,0xb6,0x1e,0x98,0xb2,0x76,0x10,0x9c,0x2a,0xc3,0x9d,0xdb,0x8b,0x4b,0x5, 0x55,0xaf,0x16,0x3f,0x41,0xa7,0x37,0xcb,0x5a,0x9c,0x5,0x3,0x3a,0xa2,0x71,0x90, 0xf,0xa7,0xaf,0x27,0x5a,0x26,0x37,0x77,0xcf,0xfb,0x94,0xab,0x87,0xe0,0xb0,0x5c, 0x10,0xc6,0x9b,0x51,0xed,0xd3,0x1d,0x48,0xef,0x23,0x4b,0x2b,0xc5,0x3c,0xbb,0x55, 0xe3,0x6b,0x7c,0xbd,0x11,0x34,0x35,0xe0,0x30,0x4a,0x8c,0x37,0xaa,0xbc,0x93,0xba, 0x3,0xae,0xc,0xf0,0x82,0xa9,0x39,0xf2,0xcc,0x84,0x1e,0x12,0x40,0x59,0xe6,0x24, 0x45,0x64,0x62,0x56,0x18,0x97,0xb7,0x48,0x61,0xc3,0xfe,0xc,0x81,0x12,0xc6,0x84, 0xc0,0xd3,0x76,0xc3,0x7d,0x2f,0xb6,0xc9,0x34,0x54,0xdb,0x74,0x2d,0xc3,0x19,0x72, 0xa7,0x7b,0x49,0xbf,0x92,0x80,0x87,0xf4,0x44,0x6,0x1,0x45,0x18,0xc8,0xca,0xd8, 0x1c,0xc0,0x1c,0x19,0x6f,0x52,0xe2,0xa3,0x26,0x3e,0x98,0x54,0x81,0x31,0x46,0xa8, 0xac,0x8f,0xe7,0xbe,0x10,0xee,0xb3,0xd4,0xf4,0x35,0x1a,0xd,0x7d,0x64,0x66,0x19, 0xa4,0x82,0x32,0x15,0xd5,0x94,0x38,0x7b,0x52,0xd0,0xcf,0x54,0x2,0x17,0x7c,0x2e, 0x26,0x65,0xed,0xb6,0x54,0x21,0x8b,0xc9,0xd5,0xa5,0xd6,0x53,0xb,0xbc,0xeb,0xaf, 0xbf,0x1e,0x44,0x15,0x32,0x7d,0x90,0x5,0xcd,0x61,0x59,0x50,0xf7,0xd5,0x7e,0x9d, 0xba,0xeb,0x54,0x8f,0x8d,0xdf,0x59,0x63,0x6,0xaf,0x37,0x11,0xec,0x23,0x40,0xac, 0xc1,0x85,0x41,0x73,0x82,0xd1,0x78,0x50,0xb2,0x51,0xa0,0x2a,0xa7,0x9f,0xc8,0x62, 0xb,0x1d,0x71,0x18,0x7d,0x4a,0xfb,0x83,0x7a,0x33,0x14,0x67,0xd5,0x54,0x93,0x97, 0x59,0xd4,0xc,0xdb,0x26,0x4,0xac,0xd9,0x56,0xcc,0x4,0xfd,0x6c,0xcc,0xdf,0xf7, 0x6a,0x52,0x10,0xe7,0x1c,0x8b,0xea,0x96,0xbe,0xfe,0x7d,0x95,0x53,0x90,0xac,0x2d, 0x65,0x38,0x88,0xc,0x3d,0x35,0xe5,0x13,0x3,0x69,0x90,0xee,0x37,0x70,0x66,0x21, 0x42,0xf6,0x9,0xde,0x82,0xf3,0x75,0xc1,0x72,0x73,0xd6,0xc5,0x4,0x83,0x72,0xe9, 0x3c,0xfb,0xf5,0xf8,0xb0,0x5b,0xc,0xb3,0xc4,0x1c,0x23,0x7b,0x8c,0x89,0x9c,0x4f, 0x0,0x25,0x2e,0x83,0x98,0x23,0x45,0xb,0x16,0x1c,0x51,0x9a,0x1f,0xc3,0x84,0x5b, 0x3f,0xf9,0xd3,0xf0,0x55,0x5f,0x24,0x99,0x7b,0x47,0x16,0x9,0x51,0x32,0xd7,0x51, 0x58,0x85,0x54,0x70,0x28,0x19,0x7c,0x3f,0x35,0x4d,0xd9,0xd4,0x90,0xdd,0xaf,0xd0, 0xd7,0x84,0x41,0xac,0xe3,0x65,0x46,0x60,0x2d,0x5c,0xe8,0x7e,0x8f,0x40,0x4f,0x67, 0xc5,0x24,0xd7,0xed,0x3d,0xd3,0x2d,0xf2,0x21,0x86,0x47,0x32,0x64,0xf6,0x82,0x3c, 0xfa,0xc3,0x68,0xdf,0x29,0xaf,0xbf,0xd5,0x8b,0x28,0xd3,0x9a,0x68,0xa3,0x81,0xad, 0xc7,0x5a,0x9b,0x84,0xad,0x49,0x77,0x4f,0x4f,0xbe,0x81,0xb4,0x36,0x4,0x70,0x31, 0xc7,0xd9,0x90,0x70,0x9,0x50,0x47,0x14,0x78,0x1b,0xaf,0x60,0x3e,0x31,0xe,0x6, 0xb,0x2a,0x8b,0x39,0xf2,0x82,0x88,0x42,0xc1,0xa,0xf6,0xf7,0x8d,0xe7,0xa8,0x55, 0xc1,0x3a,0x45,0x4a,0x8a,0xc,0x5e,0x83,0xa7,0xe,0xe3,0xe5,0xbf,0x72,0xec,0x4a, 0x9c,0xf7,0x83,0xf,0x7a,0x8b,0x51,0x3c,0x95,0xc8,0xb3,0x23,0x30,0x5d,0xf7,0xf1, 0x97,0xbd,0x3c,0xa1,0xc9,0x1a,0xa4,0x71,0x29,0x9,0xd7,0x68,0x7b,0x44,0x32,0x97, 0x3c,0x36,0xa6,0x36,0xc1,0x77,0xf2,0xd7,0xbf,0xa6,0x7a,0xef,0x83,0xf2,0x61,0x9a, 0xb0,0x1d,0xbc,0x7a,0x38,0x61,0x6c,0xe0,0x6a,0xc3,0xc8,0x65,0x8,0xfa,0x7c,0x44, 0x31,0xa2,0xf9,0x73,0x1b,0xec,0x4b,0x5a,0x14,0x45,0x4b,0x97,0x38,0x2c,0xb2,0xe8, 0x4a,0x6f,0xe3,0x82,0xd0,0xcf,0xe2,0xbb,0x93,0xab,0xa0,0x1b,0xa6,0x1e,0xde,0x58, 0xc0,0xd8,0xcb,0x5b,0xc6,0x96,0xb6,0xda,0xdb,0x81,0xf1,0x94,0xad,0x24,0x7d,0xf7, 0x93,0xe0,0xf9,0xe4,0xb0,0xdc,0xa0,0xc3,0x88,0x41,0xde,0xaf,0xde,0xbd,0x8,0xa0, 0x97,0x53,0xfb,0xdd,0xe9,0x32,0x38,0x45,0xb3,0x2a,0xd9,0x62,0x4f,0xd7,0xd9,0x62, 0xb8,0xd4,0x47,0x6a,0xb1,0x67,0xad,0xba,0x29,0x8d,0x6a,0x8,0x4b,0x72,0x28,0xe2, 0x45,0x25,0xc0,0x2f,0x57,0xf8,0xf3,0xc,0xa3,0x4e,0xed,0x72,0x26,0xc7,0xd4,0xde, 0x1c,0x9c,0xc8,0x4e,0x4,0x77,0x9,0xac,0x5,0x73,0xb5,0xcf,0x65,0x5d,0x33,0xaa, 0x82,0x73,0x59,0x5a,0xec,0xcc,0xe5,0x90,0x1b,0xd3,0x82,0xc0,0x1b,0xd6,0x20,0x38, 0x73,0xe8,0x86,0xf7,0xdf,0xf,0xa4,0x64,0x2,0xd9,0xb4,0xe6,0x38,0xe7,0x91,0x3a, 0x5b,0x6a,0x14,0x48,0xb6,0xf9,0x58,0xd2,0x4d,0xda,0x93,0xe8,0x32,0xb3,0x21,0xa5, 0x1d,0x27,0x1d,0x7c,0xb5,0x42,0x61,0xb7,0x1c,0x16,0x9e,0xd3,0xfd,0xaf,0x8e,0x59, 0x1a,0xa2,0x22,0xd0,0x1d,0x7a,0x23,0x6a,0xd5,0x37,0x53,0x8,0x6a,0xf3,0xad,0x7, 0x9a,0x4b,0x84,0x50,0x8d,0xe5,0x8,0x29,0xfb,0x26,0x7d,0xf9,0xd5,0xc,0xd2,0x6f, 0x2e,0xf4,0xc0,0x4b,0xef,0x63,0xb6,0xc5,0x9a,0x89,0xcd,0x6,0xfd,0xfa,0x8c,0x98, 0xc5,0x11,0x69,0x53,0x76,0xf0,0x7d,0x72,0x18,0xfa,0xeb,0x6d,0x86,0x3f,0xdd,0xb4, 0xb3,0x1e,0x1,0xa3,0x81,0x37,0xe8,0x1d,0x40,0x36,0xa2,0x3e,0xb1,0xae,0x57,0x77, 0xc0,0x40,0xcb,0x37,0x31,0xc8,0x2a,0xc8,0x43,0x95,0x37,0xc9,0xd4,0x94,0xfd,0x89, 0xb2,0x7e,0xac,0x34,0x35,0x96,0xd0,0x76,0xcc,0xf2,0x34,0x7e,0xa2,0xb,0xf6,0xe2, 0x4b,0x42,0x99,0xfc,0xb,0xc3,0xc5,0xcd,0xd9,0xfc,0x97,0xae,0x91,0x15,0xb7,0x44, 0x94,0xe4,0xf8,0x49,0x7b,0x49,0xbf,0xc7,0x3d,0x74,0x47,0x5f,0xfe,0xbd,0xc1,0x4b, 0x0,0x5b,0x48,0x8a,0x9f,0xe,0x58,0x79,0x8b,0x6f,0xa7,0x1d,0x4,0xdf,0xe1,0x18, 0xc4,0x5a,0x62,0xbf,0xa3,0xa1,0x87,0x60,0x16,0x4e,0x3f,0x16,0xc,0x1,0xe0,0x8b, 0x5d,0xa8,0x16,0xfc,0xb6,0xed,0xf5,0xc1,0xdc,0x1d,0xdf,0xe1,0xfc,0x41,0xf9,0x41, 0x9b,0x5c,0x1,0x3f,0xfe,0x89,0x20,0x94,0xd7,0x5f,0x2a,0x64,0x61,0x8a,0xef,0xbe, 0x33,0x86,0x3b,0x6a,0xf3,0xb0,0x2c,0xd1,0xcd,0x8b,0xb3,0x4b,0xcc,0x2d,0x8c,0xe7, 0x8a,0x8e,0x28,0x9,0x97,0x48,0x1d,0xee,0x27,0xc7,0x53,0x88,0x52,0xc3,0xc6,0x6, 0xc9,0x2,0x70,0xbd,0x32,0x1c,0x8f,0x1,0xa8,0xc2,0x4c,0xf4,0xf0,0x58,0xdd,0xfa, 0x66,0x85,0x83,0xfd,0x4d,0xa0,0x6d,0x74,0xe7,0x40,0xfd,0xba,0x4,0xc4,0xc0,0xcd, 0x47,0xb0,0xc,0x79,0x4c,0x9b,0xf9,0xf4,0xde,0xc5,0x6a,0xcf,0x1f,0x48,0xca,0x5, 0xcd,0x4e,0x83,0x1b,0x6e,0xf0,0xf,0x57,0x31,0xd,0x12,0xb5,0x52,0x52,0x83,0x19, 0x82,0xf,0x12,0xce,0xab,0xd,0x44,0x8a,0x52,0xae,0xd9,0xf0,0xf6,0x24,0xf6,0x44, 0x72,0x7a,0xde,0x60,0x6b,0xed,0x37,0x1c,0x7b,0xc8,0xd1,0x4d,0x1b,0xd5,0xe5,0x1d, 0xe4,0xf7,0xec,0x10,0x84,0x31,0x1a,0xd7,0x5f,0xf3,0xc8,0xd5,0x97,0x3f,0x1a,0xa, 0xb9,0x78,0xea,0x25,0xe5,0x22,0xc1,0x61,0xeb,0x93,0x2e,0x86,0x69,0x14,0xa4,0xce, 0xd,0x91,0xde,0x11,0x42,0xf9,0xe8,0x21,0x6d,0x32,0xf6,0x6,0x71,0x90,0x8f,0xab, 0x9,0x7a,0x50,0xee,0x1d,0x12,0xd0,0x9,0xa6,0x7e,0x8f,0x8f,0x93,0xb3,0x5e,0x20, 0x45,0x3e,0x31,0x7,0xb7,0x9a,0x28,0xa4,0x4c,0x1f,0xaa,0x3d,0x2f,0xba,0xe8,0x38, 0xb4,0x3a,0xa7,0xd1,0x4c,0xf7,0x5a,0xf2,0xf5,0x6a,0x3,0x89,0x1e,0x61,0x29,0xe3, 0x1f,0x5b,0xea,0x56,0x75,0x93,0xfb,0xc1,0x32,0x26,0xfe,0x62,0xe0,0xe8,0x1a,0x16, 0xa2,0x41,0xe7,0xee,0xb8,0xc2,0x62,0xaf,0x2d,0x65,0x39,0xca,0x46,0xe2,0xae,0xe5, 0xbd,0x1a,0x3c,0x33,0xad,0x38,0x74,0x5f,0x5f,0xf2,0xc1,0xbf,0x5b,0xdc,0xd5,0xfd, 0x9d,0x3e,0xed,0x57,0x1,0xcf,0x7,0xad,0xb4,0xbf,0x78,0x7a,0xa2,0xa7,0x60,0x60, 0xc1,0x9d,0x93,0xee,0xd5,0x87,0x4e,0xb4,0x7b,0x90,0xf4,0xd6,0x6d,0xca,0xd5,0x8a, 0x88,0x43,0xe1,0x9,0x92,0xe8,0xb6,0x47,0x29,0xaf,0xc1,0xcb,0x57,0x23,0x2d,0x19, 0x40,0x40,0x87,0x95,0x48,0xd5,0x4b,0xc3,0x66,0xbf,0x9a,0x53,0xa,0xef,0xde,0x93, 0xb2,0x40,0x9c,0x45,0xa9,0xd3,0xc,0xd2,0x83,0x4e,0x9e,0xda,0x71,0x4b,0xf3,0x31, 0xc,0xfa,0xc6,0x54,0xd0,0x91,0x97,0xb7,0x51,0x32,0x8a,0x5c,0xa2,0x69,0x6f,0x55, 0x2a,0x8b,0x9b,0xd3,0x5f,0xa7,0xa6,0xe2,0xf5,0xc4,0xbd,0xe6,0x90,0x31,0x18,0x1c, 0x2c,0x5f,0xef,0x7d,0xf0,0x87,0x35,0xc2,0xb9,0xbf,0x9e,0xdb,0xa9,0xe,0x32,0xd3, 0x99,0xcd,0xa7,0xf9,0xf4,0xcd,0xdc,0x6b,0x12,0x1b,0xd1,0x22,0x4c,0x6a,0x3e,0xf8, 0xc9,0x2e,0x76,0x3a,0xb5,0x2b,0xfc,0xef,0xea,0x9b,0xcb,0x14,0x29,0x7d,0xe7,0xc3, 0xca,0xf,0x3d,0xc0,0x5c,0x99,0xab,0xee,0xb4,0x7d,0x11,0x81,0x67,0x50,0x7a,0xb0, 0xfd,0x70,0xeb,0x34,0x9b,0x68,0xa3,0x6,0x5,0xee,0x1b,0x2e,0x6d,0x82,0x71,0x38, 0x92,0x2e,0x78,0x6e,0xc8,0x24,0x5d,0xfc,0x22,0x6f,0xfd,0x89,0x3f,0xf7,0xba,0xbc, 0xe7,0xa6,0xf0,0x83,0xf,0x94,0x8a,0x93,0x84,0x25,0x42,0x71,0xa7,0x33,0xa9,0xb9, 0x62,0x23,0x29,0xaa,0x47,0x86,0x27,0xe8,0x75,0xa5,0xf2,0x34,0x9d,0xad,0xf1,0x86, 0x54,0xe2,0x89,0xe2,0xf7,0x93,0xf6,0xfb,0xb8,0x39,0x6d,0x61,0x6c,0x17,0x9a,0x4e, 0x3a,0xc3,0xf8,0x2,0xca,0xa0,0xea,0xbf,0x46,0xdd,0xf4,0xe3,0xb,0xe6,0xe9,0xde, 0x49,0xf3,0xc2,0x41,0x87,0x39,0x3d,0x41,0xf1,0x2a,0x22,0x5e,0x42,0x3c,0x2d,0xfb, 0x1,0xa5,0xfd,0x4b,0x46,0x69,0x8a,0xc,0xc6,0x7f,0x70,0xd2,0xe5,0x5a,0xb1,0xaf, 0xcd,0xf3,0x70,0x56,0xac,0x2e,0x17,0x9e,0x58,0xb8,0x7d,0x9a,0xf4,0xaa,0x97,0x75, 0xcf,0x15,0x40,0x17,0xfd,0xcb,0x23,0xc5,0xca,0x13,0x18,0x31,0xed,0x49,0xe0,0xbb, 0xbd,0x51,0x12,0x6a,0x7f,0x29,0xa,0xd8,0x61,0x87,0xf2,0x57,0xb1,0xa,0x4c,0x81, 0x9f,0x8d,0x18,0x9d,0xd8,0xbb,0x63,0xa3,0xce,0xfa,0xd4,0xbc,0x45,0x35,0x79,0x82, 0x87,0x8b,0xec,0x86,0x35,0xf6,0xde,0x96,0xfd,0xd2,0x6d,0xaf,0x5c,0xba,0x32,0xfb, 0xc7,0x4a,0x9a,0xa0,0x6,0x7d,0xc3,0xd5,0xf8,0x19,0x92,0x3e,0xcd,0x8b,0xc0,0xd4, 0x18,0x2d,0x5c,0xcc,0x25,0xba,0x63,0xa2,0x8d,0x51,0x53,0x6a,0x8b,0x5,0x66,0x53, 0x4f,0x80,0x73,0xd5,0xfe,0xb6,0x2b,0xf7,0x4f,0x3d,0xb5,0x1e,0xc9,0xf5,0xf2,0x61, 0x23,0xce,0x2e,0xc7,0x8a,0x11,0xea,0x97,0x62,0x3e,0x2,0x6d,0xc2,0xe8,0x40,0x91, 0x69,0x33,0x67,0xe7,0xea,0x92,0x5f,0xb9,0x50,0x15,0xd7,0x1a,0x8a,0x4b,0x7b,0x2e, 0x1a,0xa9,0x75,0x24,0x3a,0x60,0xbc,0x1d,0x1e,0x3e,0x8a,0xe0,0x27,0xcb,0x73,0x91, 0xfe,0x5a,0xf8,0x69,0xed,0x59,0x24,0xbd,0x6e,0x7b,0xd7,0x79,0x46,0xd2,0xa7,0x61, 0xfb,0x1d,0x5,0x36,0x7e,0x41,0x53,0x1c,0x80,0xde,0xfd,0xa7,0x2a,0xf0,0xb8,0xa8, 0x4b,0xb2,0x13,0xb8,0xc,0xb6,0x76,0xf9,0x32,0x4e,0x73,0xf8,0x21,0x9a,0x5a,0x1d, 0x38,0xde,0xd3,0x36,0x21,0x27,0x52,0xa1,0x85,0x50,0xc8,0x2f,0x41,0x2,0xd8,0xd, 0x34,0xeb,0xc5,0xbf,0x22,0x3d,0x39,0xd3,0xb,0x2d,0xcc,0xac,0xc7,0xa6,0xc9,0x0, 0x86,0x1d,0xb5,0x27,0xc4,0x9,0xc8,0x4a,0xd8,0x11,0x7a,0x9a,0x92,0xd2,0xa7,0x46, 0x3e,0x6d,0x6,0x60,0xaa,0x40,0x34,0x36,0xec,0x81,0xe2,0x34,0x28,0x2c,0xb4,0xae, 0x4a,0x6a,0x55,0xf,0x73,0x1e,0xd8,0x4d,0xaf,0xd2,0xe7,0xc1,0xa5,0xf,0x9,0xe3, 0x7c,0xf,0x44,0xa7,0xce,0xf8,0xdd,0x3b,0x7a,0xc0,0x70,0xa2,0x6c,0x25,0xd1,0xb6, 0x8f,0x27,0x45,0x4,0xc5,0x1f,0xd0,0xf4,0xf1,0x38,0xb6,0x18,0x47,0x3f,0xfb,0xc3, 0x4f,0xc0,0xea,0x9d,0x39,0x48,0xd9,0xb3,0x9,0xc9,0xd5,0xf5,0xee,0x27,0xac,0xfd, 0xce,0xf2,0x81,0x14,0x91,0x52,0x88,0x3,0xa,0x3f,0x1b,0x51,0x7f,0x97,0x95,0x4e, 0xd7,0x80,0x6b,0x11,0xc9,0xc4,0x44,0x52,0x8e,0x99,0x48,0xfc,0x41,0x75,0xfb,0x10, 0xe7,0x7d,0xa3,0x79,0x50,0x2c,0xfb,0x5a,0xea,0x97,0x2c,0xe9,0xae,0xc1,0xb7,0x86, 0xc1,0x24,0x17,0xb,0x68,0xda,0xdd,0xf7,0x74,0xa5,0x74,0xb5,0x1b,0x70,0x45,0x82, 0x6e,0xe8,0x7b,0xbe,0x15,0x78,0x19,0x80,0x8f,0xc4,0x6a,0x3e,0x86,0xa2,0xc4,0xc8, 0xc6,0x5b,0xd3,0xae,0x36,0x31,0x26,0xaa,0xd7,0x9b,0xe0,0x72,0xc,0x26,0x75,0x7a, 0x10,0xf0,0xb8,0xa4,0xe8,0x52,0x25,0x78,0x17,0x10,0xb6,0x1e,0xb2,0xfa,0xe6,0xf8, 0x56,0x3a,0x27,0x8c,0x6c,0x4e,0xb7,0xc3,0xe9,0x98,0xb5,0x75,0xbe,0x2b,0x70,0x4e, 0x1d,0x29,0xf3,0x6,0x7b,0x98,0x7f,0x13,0x28,0x36,0x31,0x5a,0x32,0x97,0xd2,0x8, 0xd1,0xfa,0x95,0xbd,0xc8,0xcc,0x81,0xb2,0x65,0x38,0x28,0x24,0x63,0x18,0xf2,0x0, 0x42,0x66,0x7,0x3d,0x7e,0x6,0xcf,0xa7,0xbb,0x1,0x81,0x6d,0x98,0xd4,0x76,0xea, 0x4f,0x8b,0xa8,0x18,0x58,0x2b,0xca,0xbd,0xe2,0x72,0x61,0xc5,0x8b,0x54,0xc6,0x4d, 0x3a,0xcd,0x8a,0xb9,0x53,0x5b,0xe0,0xf,0xdb,0xe1,0x7d,0xf4,0xb6,0x73,0xdf,0x6, 0xfe,0x88,0x1e,0x57,0xb3,0x68,0x94,0x16,0xdb,0xf5,0xdc,0x67,0xca,0xa3,0x34,0x5, 0xf0,0xbe,0x3e,0x44,0x99,0x1f,0xd2,0xf5,0x2,0x50,0xea,0x38,0xc3,0xca,0x3f,0xc2, 0xd2,0x5d,0x99,0x87,0xc6,0x2e,0x9d,0x22,0xa4,0xf9,0x9,0x6f,0x9d,0x3d,0xf3,0x8e, 0x7b,0x33,0x52,0x95,0xd1,0x26,0x8b,0xd3,0x76,0xf5,0x8c,0xba,0xc0,0xcb,0xfc,0x93, 0xa8,0x97,0x9a,0xee,0x45,0xb8,0x11,0xe9,0xb2,0x99,0xd8,0xd0,0xd6,0xcd,0x5f,0x53, 0x80,0x32,0x68,0x52,0x58,0xf3,0xa6,0x4e,0xe9,0x33,0x9,0x2a,0x7e,0x86,0x3d,0x27, 0x9d,0x58,0x96,0xe2,0x90,0x27,0x4d,0xc2,0xc1,0xa5,0x93,0x98,0xf2,0x73,0x6b,0x73, 0xa5,0xd3,0x46,0xfd,0x47,0x6c,0x4c,0xb0,0x1f,0xd5,0x5a,0x9d,0xdb,0x18,0x44,0x79, 0x70,0xda,0xdb,0x80,0x82,0x29,0x43,0x44,0xcf,0xd7,0x5c,0xc2,0x4b,0xc8,0xb6,0xf0, 0x1c,0x7c,0x6e,0xe3,0xe8,0x3a,0x94,0x8,0x8f,0x6f,0x25,0x6b,0x87,0xe8,0xe4,0x77, 0x44,0x41,0xf7,0xc6,0x6a,0x3b,0xb,0xb9,0x92,0x67,0xfc,0x5d,0xaf,0x33,0xcd,0x4c, 0xaf,0x3c,0x30,0x18,0x77,0x44,0x9f,0x7,0xb3,0xc4,0xf2,0xba,0x2d,0xd7,0x32,0x71, 0x19,0xa9,0x38,0x4,0x65,0x43,0x3d,0xf7,0x2b,0xb9,0xd5,0xda,0xec,0xa3,0x27,0x1c, 0xe0,0xd6,0x34,0xd7,0x1c,0x53,0x5e,0x4f,0x97,0x51,0xb,0xc5,0xa9,0xbc,0x37,0x42, 0xe6,0xef,0xc5,0x4c,0x33,0x4,0xc3,0xdd,0x3d,0x99,0x39,0xaa,0x3e,0xdf,0xc6,0x9e, 0xb7,0x7b,0x76,0x53,0xce,0x54,0xa2,0x67,0xa6,0x2d,0x2d,0xcf,0x6a,0xe3,0x12,0x51, 0xd3,0xd8,0x1d,0x87,0x5c,0x60,0x65,0x99,0x7a,0x1e,0x44,0xb8,0xfe,0x8b,0xd6,0xb6, 0x7,0xcc,0xa,0x55,0x21,0x2c,0xbc,0x47,0xd9,0x69,0x17,0x44,0xcd,0xa9,0x15,0xa1, 0x2,0x32,0x29,0xdd,0x92,0xf,0x77,0xd,0x2d,0x3c,0x45,0x2c,0x47,0x9b,0x62,0x4e, 0x68,0xeb,0x23,0xa,0x98,0xe0,0x51,0x72,0xc9,0xe8,0xb6,0x97,0x12,0xcb,0xb9,0x14, 0x7d,0x62,0xf1,0x8f,0xf0,0xe8,0x1d,0x9e,0xa4,0x62,0x4a,0xeb,0x7e,0xad,0xb9,0xe6, 0x19,0xdd,0xf0,0xb1,0xbe,0xc2,0xa3,0x8,0x2b,0x5a,0x20,0x3d,0xa5,0x59,0xd0,0xa2, 0xbb,0x42,0x33,0xad,0x2b,0x50,0x4c,0xd0,0x32,0x96,0x3c,0xb0,0xc3,0xf6,0x18,0xdd, 0xd4,0x88,0xf,0x13,0x4b,0xb3,0x1b,0xf5,0x8d,0xba,0xb2,0xb3,0x14,0x83,0x56,0xd0, 0xc5,0x9,0xfd,0x71,0xd8,0xc9,0xc1,0x8b,0x60,0xfd,0x3c,0xa4,0xf4,0xd3,0x2,0xc9, 0x5d,0x11,0xdc,0x28,0x44,0x78,0x1f,0xd2,0x33,0xd1,0x6,0x48,0xd5,0x5c,0x98,0x9b, 0xe5,0x16,0x8c,0x3e,0xdf,0x4e,0xc9,0xbf,0x4d,0x86,0x64,0x42,0x5a,0x66,0xd,0xb7, 0xf7,0x69,0x60,0x3c,0xe1,0x7f,0xf,0x16,0xd0,0x15,0xdd,0xa6,0xf1,0x76,0xc2,0x57, 0x8c,0x4f,0x95,0xeb,0x9e,0xdf,0xab,0xeb,0x66,0x11,0xad,0xc0,0xf6,0xba,0xf8,0xee, 0xa4,0x59,0x2c,0x86,0x58,0xba,0x9c,0x29,0x50,0xf9,0x50,0xc1,0xef,0x13,0x19,0xfb, 0xe1,0x2e,0xe7,0x80,0xe,0x94,0xeb,0x74,0x25,0x1a,0xb5,0x1c,0x54,0x2e,0x8b,0xf8, 0x7,0xb7,0x80,0x5f,0xf1,0x9c,0x8,0x42,0x97,0x58,0x83,0x7,0xea,0x9c,0x4,0xcd, 0x4b,0xeb,0xcd,0x59,0x0,0x3a,0x4e,0xa4,0x54,0x83,0x41,0xa8,0xb1,0xcc,0x22,0xb8, 0x4,0xa2,0x18,0xf5,0x3f,0x9f,0xb8,0x56,0xf8,0x3c,0x5e,0xe3,0x59,0xe1,0x31,0xa4, 0x4d,0x7f,0x7d,0x4e,0xb9,0xcb,0x72,0x8d,0x4f,0xb3,0xb5,0x80,0x80,0xd7,0x39,0x84, 0x7a,0xd0,0xfa,0x3a,0x71,0x33,0x10,0xe9,0x6f,0xed,0x4d,0x48,0xcf,0x7f,0x6c,0x1e, 0x7e,0xea,0xeb,0x38,0x36,0x5e,0x45,0x6,0x13,0xfa,0x86,0x13,0xd3,0x40,0x18,0xcd, 0x90,0x13,0x8,0x81,0x46,0x19,0x6b,0x35,0x7,0x39,0xfd,0x57,0x38,0x6a,0x75,0xb6, 0xd4,0x61,0xee,0xc,0x3f,0x34,0x12,0xd1,0xae,0x18,0xe5,0x82,0x58,0xfd,0x51,0xe9, 0x90,0xd8,0xea,0x56,0x71,0xd6,0xb,0xf8,0x10,0x88,0x50,0x48,0xf3,0x45,0xfe,0xc8, 0xa6,0x6d,0x54,0x65,0x21,0xe5,0x38,0xcf,0xfe,0x9d,0xd2,0x57,0x1b,0x24,0xc0,0xab, 0x7c,0x2c,0x81,0xee,0x3,0xc,0xe7,0x13,0x95,0xb7,0x5b,0x89,0xfc,0xd9,0xd1,0x23, 0xc6,0xa6,0x88,0xe7,0x8c,0xc0,0x37,0xb,0xdd,0xa,0x63,0xf8,0xad,0xa3,0x24,0x2b, 0xcf,0xa5,0x1a,0xd2,0x32,0x81,0x65,0xc7,0x39,0x40,0xd0,0x36,0x1a,0x22,0x59,0xe0, 0xc8,0xe1,0x48,0xd5,0x23,0x80,0xe0,0x80,0x8a,0xc3,0x7a,0xb8,0xe7,0x9e,0xe3,0x37, 0xc4,0xfd,0x8a,0xf6,0x7f,0xef,0x3e,0x38,0x31,0xf,0x6e,0xca,0x31,0xc7,0x2c,0x7a, 0x29,0x74,0x50,0xcb,0xf4,0xb0,0x4d,0x0,0x75,0x47,0x38,0x5d,0x65,0x1c,0x14,0x2a, 0x99,0x9e,0xa0,0x19,0x8f,0xde,0xd0,0x40,0x6d,0x3f,0xb,0x9f,0x86,0x37,0x99,0x2f, 0x2c,0xe9,0x7b,0xa0,0x1a,0xc8,0x20,0x8f,0x8f,0x58,0x6c,0xf4,0x74,0x1,0x9f,0xe, 0x9f,0xbf,0xa6,0xae,0x9f,0x77,0xee,0xd,0xb6,0x7a,0x2c,0xbc,0x31,0xc5,0xec,0x5d, 0x2f,0x68,0xfe,0x4a,0xb0,0x1f,0x59,0x40,0x78,0x46,0xb4,0xec,0x47,0x54,0x7b,0x66, 0x94,0x22,0x16,0x34,0x9a,0x5,0xc0,0xd0,0xfe,0x6d,0xe,0x31,0x33,0xfa,0x8e,0xe2, 0xe2,0x8d,0xac,0x93,0x2d,0x85,0x53,0xa5,0x4b,0x8,0x12,0x12,0xdc,0x8d,0x79,0xf0, 0xb0,0x8f,0xa4,0xca,0x14,0x65,0x1b,0x14,0x52,0x29,0xc4,0x86,0xa3,0x53,0xe8,0x86, 0x61,0x95,0x99,0x8e,0x9a,0xec,0xb3,0xe6,0x75,0xc5,0xf8,0xd1,0x54,0xf1,0xc2,0x84, 0x1,0x67,0xce,0x16,0x4c,0x69,0xa9,0x9f,0x93,0x6e,0xa5,0xb6,0x41,0x8e,0x3e,0x22, 0xa3,0xd7,0xb0,0xbd,0x45,0xe3,0xa4,0xba,0xaa,0x1e,0xc,0x7e,0x8f,0xce,0x3,0x91, 0xb5,0x51,0xa7,0x2,0xba,0xd0,0x21,0xcd,0xbe,0xc6,0x5,0x0,0xd4,0x43,0x23,0x78, 0x9a,0x53,0x37,0x5f,0x38,0x5b,0x99,0x62,0xf8,0xa5,0xe0,0x89,0xf3,0x63,0x1b,0xa9, 0xb4,0x42,0x2c,0xee,0x13,0x4d,0x3d,0xd1,0x15,0x42,0x51,0xe9,0x5,0x74,0xe2,0x9f, 0x48,0x99,0x7f,0x0,0x74,0x19,0x62,0x6e,0xbf,0x43,0x77,0x33,0x26,0x92,0x5d,0xda, 0x54,0x89,0x49,0x67,0x56,0x86,0xb8,0xea,0x48,0xa,0x55,0x4d,0xfe,0x38,0x6d,0xc6, 0x51,0xec,0xc6,0xc5,0x6,0x29,0xb3,0x45,0xeb,0x2b,0x79,0x12,0x3d,0xd6,0x6c,0x91, 0x60,0xb5,0x78,0x36,0xbc,0x31,0x22,0x5,0xbb,0x77,0x53,0x3a,0x2f,0x40,0x1,0x0, 0x2d,0xc7,0xc5,0x33,0x70,0xf9,0x79,0x5c,0xa4,0xf2,0x6e,0x62,0x49,0x5a,0x73,0x29, 0x10,0xec,0x5f,0x4c,0x9d,0x1,0xd1,0xd8,0x78,0x25,0x13,0x27,0xe4,0x93,0x27,0x12, 0x5b,0x6d,0xc4,0x4b,0x67,0x3e,0xa7,0x8b,0xb0,0x95,0xed,0x79,0xef,0x62,0xa2,0x80, 0xce,0x3,0x4c,0xeb,0x4,0x1e,0x45,0xfc,0xc2,0xd7,0x24,0xa7,0x6c,0xcb,0xb9,0x47, 0x39,0x7f,0x93,0x20,0x3d,0xba,0xab,0x6e,0x51,0x1a,0xe7,0xc0,0xfb,0xb,0xc0,0xca, 0xe,0xe,0x36,0x91,0x2c,0xfa,0xe,0x6f,0xd3,0xb2,0x17,0xbf,0x7e,0x51,0x7,0x37, 0x50,0x9a,0x57,0x8d,0x56,0x3,0x7b,0x27,0x1d,0x64,0xe7,0x19,0x6f,0x29,0x63,0xfc, 0xb6,0x1a,0xe,0xe2,0x94,0x9c,0xd1,0x68,0x4f,0xe9,0x28,0x4d,0x3b,0x30,0x84,0xb, 0x4a,0xdb,0x98,0x20,0x5e,0x94,0x47,0xfb,0xf8,0xaf,0x94,0xe7,0xd8,0x78,0x64,0x8f, 0x12,0xf1,0xf1,0xa6,0x8e,0xc4,0x8f,0xdd,0x2e,0xb7,0x2b,0xe8,0x67,0x2f,0xf3,0x32, 0x8a,0xc,0x52,0xe9,0xa0,0x9a,0x65,0x99,0x4a,0xf9,0x1,0xa2,0xf1,0xe4,0xb1,0x4, 0xd7,0xa3,0x2b,0x66,0xe7,0xba,0xc4,0x16,0xf1,0x6f,0x7e,0xd9,0x9f,0x72,0xc,0x2a, 0x7f,0x5e,0x93,0x20,0x78,0xf8,0x3a,0x42,0x73,0xba,0xe4,0xe4,0xa0,0x96,0x69,0xf7, 0xba,0x94,0xdd,0xa2,0x4f,0xa2,0x39,0x41,0x92,0xb7,0x1b,0x32,0x2b,0xa6,0xdb,0x2a, 0x6,0xef,0xc9,0xfd,0x68,0x4,0x41,0x5b,0x3f,0xa5,0x41,0x5f,0x3d,0xaa,0x57,0x77, 0xbe,0x35,0x1a,0xe,0x58,0xd2,0xce,0xea,0x8b,0x6a,0x9c,0x36,0x11,0xf7,0xdf,0x96, 0xe7,0xa9,0x95,0x51,0x2e,0xd6,0xac,0x6d,0xfb,0x6d,0xcc,0xb8,0x97,0x24,0x30,0x56, 0xd8,0xca,0xe3,0x31,0x9d,0xb3,0x9b,0xa8,0x1e,0x38,0x5e,0xae,0xb0,0x3e,0x46,0x98, 0xe8,0xdb,0x69,0x17,0x32,0x96,0x4,0x2e,0x4,0xd0,0x67,0x1c,0x74,0x97,0x72,0xcc, 0x62,0x57,0x7e,0x80,0x8a,0x1a,0x29,0x28,0xd2,0x88,0xd6,0x83,0xc6,0x1d,0x9b,0x2f, 0x78,0x6,0xc5,0x2a,0x9c,0xc9,0xd8,0x20,0x1a,0x40,0x3c,0xe,0xd7,0x2f,0xdb,0xba, 0x6,0x5a,0x3b,0x10,0x74,0x64,0x38,0xc6,0x6c,0x8e,0xc9,0xb3,0xac,0x66,0x62,0xa4, 0xeb,0x29,0x4f,0x88,0x72,0x28,0x28,0xd,0xe7,0xe4,0x1b,0xbf,0x14,0x76,0xf9,0x99, 0xd0,0x35,0xa9,0xc5,0x1a,0x61,0x8c,0x6,0xef,0xd6,0xb9,0x1c,0x3d,0x9c,0xc1,0x29, 0xc5,0x11,0x31,0xb7,0xb8,0xd8,0x44,0xa0,0xbd,0xdf,0xdf,0x51,0x56,0xda,0xea,0x28, 0x8f,0x14,0xed,0xa9,0xf4,0xf9,0x30,0xe5,0x50,0xe9,0x2,0x8d,0x6,0x43,0x36,0xcb, 0x54,0xe6,0x4,0x8c,0xc0,0xc7,0x2d,0xfd,0xa7,0xe,0x50,0xfe,0xe8,0xba,0xa6,0xf7, 0x4f,0x14,0x22,0x44,0x8d,0x52,0x2a,0xde,0xbb,0xac,0xeb,0xc2,0xef,0x23,0xe,0x45, 0x89,0x91,0x51,0x4a,0x5a,0x7f,0x49,0x81,0x8d,0x19,0x0,0xf5,0x53,0xa6,0x6d,0xa2, 0x3a,0x8f,0xe7,0xc8,0xe1,0x91,0x27,0x9e,0x3e,0x13,0xe0,0x2f,0xb5,0xee,0xf3,0x40, 0x81,0x45,0xa,0x5b,0xc4,0xd2,0xdc,0xd1,0xeb,0x5d,0x47,0x40,0x83,0xb5,0x62,0xbe, 0x45,0xc9,0x7,0xa7,0x5c,0x2e,0xc5,0x9a,0xc0,0xa6,0x49,0x77,0x15,0x3d,0xb7,0x96, 0x3,0xc1,0x71,0x47,0x15,0xce,0x1a,0x1,0x2c,0xe0,0xc0,0xaf,0x96,0xa3,0xed,0x5c, 0x6d,0x74,0x83,0xc9,0xa2,0x49,0xe4,0x64,0xef,0xad,0x5b,0x5,0xeb,0x13,0x1c,0x6e, 0x54,0xd,0xb5,0x69,0xdb,0x4f,0xea,0x87,0x31,0x2b,0xb7,0x47,0xce,0x25,0x23,0xbc, 0x9a,0xa6,0x6,0x3d,0xef,0xea,0x21,0x5f,0x99,0x7c,0xe4,0x5,0xf,0x80,0x73,0x64, 0x8d,0x29,0x4d,0xe9,0x79,0xb7,0xf0,0x2a,0xe3,0x28,0x71,0x32,0x4e,0x95,0xee,0xe8, 0xbb,0x75,0xa5,0xac,0x60,0x47,0x8b,0x79,0xc3,0x70,0x7e,0x53,0xf0,0x71,0x37,0xfe, 0x1b,0x84,0x68,0x14,0xbc,0x59,0x3e,0x20,0x82,0xaf,0x52,0x50,0xc4,0xc1,0x39,0x81, 0x37,0xde,0xad,0x17,0x26,0x39,0x11,0x6a,0x2a,0xf,0x3d,0x9a,0x81,0x74,0x19,0x1c, 0x78,0x81,0x30,0x35,0x5b,0x6e,0x55,0x5d,0x9d,0x28,0xad,0xe2,0x69,0x66,0xe3,0x20, 0xc4,0x91,0xb6,0x6b,0x4a,0xc7,0xd5,0xf3,0xd7,0x13,0xf,0xd8,0x7,0x28,0xf4,0x7f, 0xaa,0x25,0x35,0x85,0x93,0x8a,0x62,0xb0,0x32,0x8f,0x93,0x1b,0xf5,0x77,0x3b,0xba, 0x88,0xf2,0x26,0x53,0x3a,0x7b,0xc6,0x12,0xe,0xd5,0xea,0x15,0xfe,0xdf,0x15,0x29, 0x5,0x4a,0x2e,0x18,0x54,0x90,0xc9,0x87,0x20,0xdc,0xa2,0x16,0xd4,0x5e,0x50,0x5d, 0xd0,0xf6,0x30,0xb,0x72,0xf7,0x1e,0x1,0xcd,0x88,0x16,0x4c,0x69,0xaa,0x75,0xed, 0xf4,0xa3,0x86,0x4a,0xb3,0xcf,0xd1,0xd3,0xac,0xf3,0x69,0x81,0xd1,0x3a,0x5f,0xa2, 0x31,0xf,0xae,0x23,0x7,0x4c,0x24,0x55,0xd4,0xba,0xa1,0xbd,0x65,0x97,0x2c,0x5b, 0xba,0xb2,0x25,0x6f,0x2,0xf6,0x43,0xae,0x6a,0x2d,0xb0,0xbc,0x67,0x8f,0x5f,0x98, 0x9e,0x8d,0x3b,0x26,0x59,0x60,0xfa,0xae,0x9a,0x1c,0x6c,0x7f,0xb3,0x18,0xda,0x6f, 0x4a,0x0,0x5e,0x4c,0x76,0x21,0x7b,0x61,0x4e,0x2c,0x1e,0x35,0xbb,0xfc,0x4d,0xd9, 0x8b,0x89,0x0,0xe4,0x69,0xfa,0x93,0x4,0x18,0x80,0x83,0x4b,0x18,0xde,0x3a,0x63, 0x5e,0x98,0xaf,0x55,0xba,0x2b,0xb6,0x88,0xd6,0xd4,0xbe,0x12,0x51,0xc,0xec,0xdc, 0x95,0x6c,0x42,0x7e,0xe7,0x55,0x82,0x0,0xd5,0x86,0xca,0x6e,0xe4,0x6,0xd1,0x43, 0x1e,0x1,0x98,0xd8,0xac,0xce,0xe1,0x3,0x23,0xa0,0x16,0x75,0x2c,0x82,0x52,0xc2, 0xee,0x94,0x41,0xd6,0x6a,0x44,0x56,0xbf,0x4a,0x22,0x2e,0x2f,0xa7,0x0,0x72,0xc5, 0x81,0x8b,0x1f,0x2e,0x5a,0x1,0x31,0x7e,0xa1,0xc6,0xf3,0xcd,0x49,0xc5,0x10,0xb8, 0xda,0xd1,0x8f,0x45,0x16,0x66,0x5,0xdf,0x8,0x34,0xf,0xaf,0xb3,0x1,0x75,0x35, 0x8c,0x94,0xe2,0x67,0x95,0x15,0x65,0xb6,0xdb,0x59,0x5,0xa5,0x9e,0x15,0x5e,0x79, 0x66,0x6d,0x3e,0x7c,0xd3,0x44,0xdb,0xdb,0xf7,0xea,0x8b,0x2b,0x6c,0x81,0x61,0xf8, 0x16,0xc3,0xdf,0x2c,0xd8,0x45,0xe2,0x35,0x1e,0xe7,0x5a,0xbd,0x7d,0xb8,0x37,0xe3, 0x26,0xf5,0xe0,0x7a,0x3a,0xbc,0x56,0xb1,0xa8,0x62,0xdc,0x15,0xe3,0xbd,0x8d,0x79, 0x82,0xed,0xa5,0xda,0x33,0x89,0x8f,0x52,0xf0,0xe9,0x10,0x6e,0xa2,0xc6,0x53,0x49, 0xbc,0x34,0xc3,0x76,0xf0,0x99,0xa7,0x19,0x7b,0x85,0xad,0xde,0xc2,0xbb,0x59,0xc4, 0xa9,0xfe,0xa0,0x5c,0x8,0xaf,0xae,0xf9,0x9a,0x3e,0x68,0xbc,0x6,0x3b,0x6,0x42, 0x6f,0x49,0x39,0xe0,0x63,0xe0,0x79,0xde,0xe5,0x28,0xbe,0x29,0x63,0x97,0xed,0xd, 0x16,0xe,0x69,0x1f,0xbe,0x98,0x98,0xd8,0xd6,0x80,0x95,0x5c,0xbc,0x1c,0x1f,0xab, 0xe4,0x58,0x8c,0x48,0xb8,0x7,0x28,0x1f,0xae,0x66,0x48,0x12,0xfd,0x36,0x9e,0x14, 0xc4,0x87,0xb2,0x83,0x20,0x4b,0x5c,0x77,0xcc,0x71,0x53,0x9,0x8d,0x72,0xb4,0x73, 0x4a,0xc1,0x3b,0x83,0x48,0x63,0xa2,0xf6,0x49,0x6a,0x88,0xc6,0x20,0xa6,0x5b,0xe4, 0x2e,0xe,0x68,0xce,0xd9,0x44,0x46,0x26,0xb6,0x19,0x2f,0x44,0xc,0x63,0x37,0x56, 0xa4,0x73,0x59,0xec,0x56,0x7b,0x63,0x20,0xe5,0x6b,0xe6,0x7,0x12,0x42,0xeb,0x41, 0xd0,0xd4,0x8f,0x2a,0x98,0xd5,0x50,0x4f,0x6e,0xfe,0x14,0x7a,0xe1,0xca,0x51,0x87, 0x3e,0xaa,0xf3,0x15,0x27,0xd7,0x35,0x8c,0xc2,0x9b,0x93,0xd5,0x5e,0x0,0x96,0x2f, 0x54,0x26,0x59,0xec,0x7b,0x29,0xbc,0xe9,0x28,0x50,0x65,0x89,0x1b,0x36,0x90,0xd9, 0xe0,0x85,0xee,0x87,0xdc,0x24,0x15,0x9f,0x3f,0x28,0xf4,0x9d,0xa7,0x8b,0xcc,0xfb, 0x31,0xa5,0x69,0xac,0xce,0x26,0x17,0x76,0xf5,0xfb,0x1,0x11,0x32,0x91,0xea,0x13, 0x96,0xd9,0x1b,0xf2,0x7d,0xaf,0x93,0xbd,0xd7,0x8,0x5b,0x0,0x14,0xa8,0x7b,0x45, 0xcd,0xe4,0x72,0x1d,0x8a,0x9,0x93,0x80,0x5,0x14,0x92,0x37,0x26,0xfc,0xc9,0x3c, 0x57,0x64,0x30,0xd4,0x14,0x43,0x12,0x6c,0x4b,0xed,0x6c,0x5f,0x16,0xe7,0x25,0xe3, 0x4d,0x17,0x80,0xd7,0x20,0x15,0xd8,0x25,0xa8,0xea,0xdb,0x4e,0xe7,0xa5,0x8b,0x3f, 0xb,0xbb,0x94,0x9e,0x7e,0x26,0xb,0xc9,0x93,0x77,0xa9,0xa9,0xdf,0x4e,0xe,0x2d, 0x65,0x8e,0x84,0x85,0x23,0x5d,0x2a,0x4c,0x48,0x6,0x9a,0x31,0x2b,0x26,0xef,0xb5, 0x61,0x84,0x55,0xdf,0x2b,0x60,0x2a,0xbe,0x58,0x53,0xe8,0x38,0xa1,0x76,0xe4,0x86, 0x84,0x69,0xc,0x28,0xc7,0xb5,0x74,0x10,0xbb,0xf,0xc0,0xe6,0xb5,0xb1,0x9d,0x96, 0xb5,0xf2,0x77,0x60,0xd2,0x21,0x20,0xaa,0x74,0x88,0x62,0x16,0xfe,0x47,0x9c,0x3, 0xb1,0x28,0x2b,0xf8,0xdd,0x9f,0x88,0x19,0x2f,0xc9,0x7f,0x64,0xfa,0x9c,0xfa,0x30, 0xf,0x72,0x91,0xe2,0x93,0xb1,0x8d,0x87,0xb9,0x70,0x1d,0xb8,0xb7,0x39,0xbb,0xe8, 0x61,0x67,0x61,0xbe,0x7,0xea,0x57,0xb5,0x34,0xd7,0x1a,0x2f,0x74,0x16,0x5f,0x84, 0x8,0xf0,0xe6,0x1c,0x22,0xf3,0xa3,0xdb,0x64,0xc1,0x14,0x1d,0x7a,0xd0,0x85,0xdc, 0x38,0xe7,0x1b,0xbe,0x52,0x73,0x75,0x86,0xca,0xf,0xb5,0x3f,0xa4,0x15,0xc3,0xad, 0x86,0x2a,0x49,0xa8,0x1f,0xec,0x85,0x83,0x2e,0x99,0xa0,0xa9,0xe9,0xa6,0x6,0xa1, 0x8e,0xa0,0x61,0xe0,0x14,0x56,0xe6,0xde,0xe4,0x9c,0x9e,0x8a,0x31,0xe1,0xb7,0xb7, 0xd,0x1,0xe0,0x2c,0x6d,0x66,0xaf,0x1c,0x7f,0xd0,0x45,0x6a,0xf6,0x4b,0xc,0x85, 0x6b,0xec,0xe5,0x0,0xc2,0x4c,0x5e,0x28,0xe8,0xfc,0xb2,0x99,0xdf,0x6a,0xd1,0x6c, 0xea,0xb2,0x18,0x58,0x98,0x47,0x74,0x18,0x97,0xb9,0x2,0x8e,0x84,0x8e,0x14,0xf0, 0xfa,0x79,0xf0,0xbe,0xc5,0x4f,0xe6,0x2e,0xcc,0x19,0x48,0x2c,0x3,0x1a,0x98,0xed, 0x4c,0x30,0x46,0x64,0x77,0x3b,0x7c,0x10,0xf4,0xfe,0x9e,0xf9,0x8d,0x33,0x6a,0x88, 0x2c,0x5b,0xc6,0x72,0x2a,0x2d,0xa0,0xf6,0xc5,0x68,0xa2,0xc8,0x82,0x3b,0xb6,0x4e, 0xea,0xfd,0xb2,0x63,0x39,0xaf,0x73,0xad,0xae,0x91,0x27,0xbb,0x44,0x91,0xc3,0x71, 0x6c,0xb,0xe3,0x17,0x38,0x4,0xe,0xfe,0x6d,0x31,0xc7,0x6f,0xeb,0xfe,0xbe,0xd7, 0x7c,0xf0,0x3b,0x35,0x20,0x2e,0xe2,0xce,0xbf,0x8a,0xa,0x5,0x1c,0xce,0xf5,0x9, 0xd9,0x59,0x20,0x91,0x5d,0xad,0x10,0xca,0xde,0x58,0xba,0xcb,0x57,0xf8,0xa3,0xd3, 0xe9,0xde,0x9,0xb,0x8c,0x6b,0x59,0xcb,0xf5,0xe3,0x50,0x92,0xb2,0x46,0x9b,0xc, 0x9f,0xbb,0x9d,0x7d,0xe8,0x2e,0x48,0xc8,0x86,0x82,0x94,0xdd,0x7b,0xb7,0x31,0xe5, 0x16,0xb9,0x70,0xa2,0x25,0x49,0x6e,0x9b,0x2d,0xbf,0xad,0x5f,0x85,0xc8,0x6b,0x26, 0x4,0x89,0xa3,0xec,0xb7,0x6b,0xb5,0xbd,0xee,0xc9,0x1b,0xe9,0x81,0x4c,0xcf,0x97, 0x6,0x40,0xb9,0xaa,0x8a,0x29,0xc5,0x37,0x68,0x73,0x97,0xed,0x3c,0x3,0x93,0x40, 0xc,0xb6,0xad,0x43,0xa2,0x63,0x1,0x11,0x2e,0x1c,0xfa,0x2f,0xe7,0x4b,0x47,0xed, 0x8b,0x1,0x19,0x95,0xa9,0xde,0xcd,0x91,0xd2,0xe4,0x80,0x8e,0xe7,0x93,0x4f,0x74, 0x4b,0xfc,0xb7,0x6d,0xdf,0x39,0x7e,0x8d,0xd4,0xf8,0xbd,0xbd,0x44,0x84,0x2b,0x50, 0x85,0xc3,0xe5,0xaf,0xa3,0x33,0x41,0xf5,0x18,0x41,0x84,0x80,0xd5,0x53,0x74,0xa0, 0x50,0xab,0xe,0x31,0x64,0x8c,0xbe,0x3a,0x85,0xfb,0x77,0x4a,0x80,0x22,0x9a,0x86, 0xe6,0x0,0x36,0xa,0xb3,0x77,0x0,0xcb,0xb9,0x4,0xcb,0xf,0x58,0xbf,0xaf,0xa8, 0x6c,0xbd,0x59,0xd0,0xc9,0x98,0xb,0xce,0x94,0x2,0x19,0x95,0x25,0x33,0x1c,0xc, 0x34,0x52,0x95,0xe7,0x49,0x95,0x33,0x82,0x19,0x7f,0x91,0x71,0x3f,0x41,0x9a,0xab, 0x7e,0x73,0xfc,0xc7,0xc,0x87,0x17,0x21,0x8a,0x30,0xb6,0x2f,0xe3,0x52,0x3b,0x18, 0xa4,0xd0,0x7f,0x6d,0xe5,0x32,0xf0,0x7e,0xb1,0x2,0xf0,0xf1,0xc3,0xb,0x1d,0xc1, 0x7e,0x99,0x8a,0xb,0x22,0xa1,0x2c,0x2c,0x51,0x62,0x5b,0x35,0xb4,0x96,0xcc,0xd8, 0xe6,0x4c,0x46,0x4c,0x7f,0xb6,0xca,0xb0,0x39,0x3b,0x22,0xfc,0xc5,0xbf,0x3e,0xc4, 0x59,0x48,0xcf,0x7b,0xe9,0x7b,0xa7,0xbb,0xdd,0x82,0x70,0x92,0x19,0x3e,0xea,0x7f, 0xa,0xb0,0x4b,0x9,0x68,0x17,0x3a,0x21,0xd1,0x5c,0x9d,0x98,0x1c,0xdb,0x5d,0xf5, 0x25,0xac,0xf0,0x8e,0x28,0x19,0x4a,0x85,0x9b,0xbb,0x18,0x35,0x79,0x82,0xb4,0x3, 0x33,0x80,0xd,0x1b,0x17,0x47,0x3c,0xe8,0x23,0xd9,0x1,0xbf,0xb6,0xdd,0xb5,0x5b, 0x8a,0xa6,0xe9,0xb2,0x3f,0xb4,0x38,0xdb,0xef,0xcf,0x11,0x69,0x52,0x45,0x6c,0x6, 0xc5,0xf8,0x21,0xdc,0x40,0x5e,0x46,0x64,0xb7,0x47,0x24,0xed,0x26,0x59,0x49,0xb0, 0x7f,0x34,0xe3,0xbf,0xe8,0x9b,0x9b,0xd8,0xeb,0x2c,0xc1,0x3e,0x71,0xad,0xc3,0xb7, 0xa7,0xe5,0x94,0xe7,0xc3,0xda,0xcb,0x7b,0xa2,0x6f,0x6a,0xc8,0x48,0xb3,0xf8,0xc8, 0x67,0x5c,0x88,0xcf,0xf8,0x24,0x28,0xe4,0xcf,0xe9,0xa2,0x41,0x98,0x67,0xf8,0x40, 0xcc,0xe,0xa7,0x90,0x68,0xf3,0xc,0xb,0xe2,0x76,0x53,0xab,0xaa,0x4d,0x74,0x12, 0xa9,0x7c,0xe2,0x22,0xa0,0xb,0x7,0xef,0x75,0x2a,0x31,0xe,0x91,0xaa,0xcd,0x5e, 0xb8,0xf4,0xee,0x21,0x68,0x7a,0x2d,0x4c,0xf1,0x80,0xf7,0x9c,0x4d,0xeb,0x2e,0x77, 0x68,0x11,0x99,0x88,0x9c,0x21,0x78,0x12,0x4b,0xa9,0x9f,0x5c,0x54,0x6d,0xba,0x8c, 0xe1,0x29,0xae,0x4b,0xa3,0xdb,0x17,0x15,0xdb,0x8e,0x31,0x2a,0x7a,0x60,0x21,0xe2, 0x71,0xba,0xea,0x8d,0xdb,0x63,0x9f,0xa6,0x8c,0x3f,0x3,0x61,0x2c,0x3d,0xed,0x8e, 0x66,0x9c,0xd9,0x8a,0xf7,0xf0,0x9f,0xd4,0x7f,0xd1,0x7e,0x79,0x32,0x9f,0x5c,0x23, 0xd9,0x47,0xb1,0x36,0x2a,0xd0,0xdc,0xb6,0x90,0xe0,0x18,0x3c,0x1e,0x86,0xca,0x5, 0x23,0xa4,0x8f,0x9b,0x15,0xae,0xef,0x14,0x0,0x6e,0x8d,0x32,0x8d,0x69,0xd5,0xe6, 0x30,0x87,0x1d,0x5a,0x58,0x7a,0x91,0x68,0xda,0x29,0xa5,0x78,0xaf,0x70,0xfc,0x53, 0x95,0x8c,0xee,0x2a,0xbb,0xde,0x3f,0xbb,0xcc,0x4c,0x6e,0xd9,0xb6,0x44,0x40,0x66, 0x4b,0x5e,0x41,0x23,0x58,0x52,0x8c,0xb2,0x7b,0x32,0x2b,0xab,0xa2,0x29,0x7e,0xb7, 0x35,0xec,0xe2,0xf0,0x4b,0x22,0x2d,0x18,0xed,0x9b,0x71,0x24,0xdf,0xb1,0x8b,0x2b, 0x8f,0xcc,0xcd,0x67,0x1f,0x5a,0x1a,0x1a,0x8c,0x46,0x45,0xaf,0xee,0xc3,0x67,0x24, 0xb0,0xc9,0x95,0xfb,0x6b,0xc2,0x93,0x5a,0x5e,0x84,0x7e,0xbd,0x37,0xa,0x68,0x46, 0x56,0x36,0xae,0xf4,0x91,0xc8,0x8f,0x9d,0x8e,0xd4,0xcc,0xfc,0x19,0xb4,0x22,0xc9, 0x7e,0x37,0x46,0xea,0x79,0x59,0xc4,0x57,0xde,0x43,0x15,0x95,0xcd,0xfc,0x5b,0x24, 0x33,0xa,0x1a,0x44,0x53,0x29,0x62,0x61,0xfd,0xae,0x5f,0x17,0x63,0x1,0x61,0x62, 0xb7,0x27,0xcc,0x31,0x80,0x91,0x88,0xde,0xd4,0x1d,0x74,0xa2,0x1a,0xd0,0x47,0xcc, 0x5a,0xe0,0x91,0x2d,0xa,0x73,0x8f,0x8,0x22,0x6e,0x9f,0x86,0x6f,0x1,0x68,0x27, 0x28,0x35,0xd7,0x28,0xc6,0xdf,0x8,0x1b,0xfc,0xfb,0x3e,0x96,0xcc,0x85,0xe2,0xa7, 0xe5,0x74,0xd4,0xef,0xe7,0x64,0x77,0x8a,0xd2,0x17,0x90,0xc1,0x97,0xf8,0xe8,0x3f, 0xad,0x40,0x68,0xf3,0x20,0xef,0xf,0x1d,0xeb,0xcc,0x33,0x39,0xd1,0x17,0xe0,0xb7, 0xb,0xb5,0xa7,0x73,0x1b,0x9f,0xfd,0x6d,0x36,0x8e,0x30,0xce,0x87,0x98,0x8d,0x35, 0xd9,0xf5,0x29,0xf9,0x65,0xb7,0x97,0x52,0x85,0x4a,0x8b,0xd6,0x61,0x6c,0x8f,0xec, 0xa1,0xb6,0x60,0xbc,0x56,0x5e,0xaa,0x8d,0xec,0xda,0xdb,0xf3,0xf2,0x69,0xa8,0xcc, 0xdf,0x51,0x47,0x45,0x9,0x5e,0x97,0xe,0xa8,0xa2,0xe5,0x8a,0x8e,0xf4,0x77,0x31, 0xab,0xd7,0x6d,0x82,0x36,0x18,0x8f,0xa2,0x72,0x6b,0x96,0x66,0xd4,0x3f,0xb2,0x34, 0x90,0x79,0x7a,0x19,0xd7,0x91,0xa7,0x1,0x35,0x8d,0x8b,0x43,0x2,0x3,0x74,0xad, 0xda,0x62,0x30,0x90,0xf9,0xbf,0x33,0xec,0xaa,0xc9,0xd2,0x0,0x88,0x85,0x34,0x98, 0x7f,0x2e,0x31,0x57,0xc0,0xd8,0xd7,0x75,0xe5,0x63,0xb8,0xe7,0x66,0xad,0x16,0xc0, 0x8f,0x46,0x51,0x89,0x86,0x84,0x76,0x31,0xcd,0x49,0x31,0x56,0x4f,0xe5,0x6e,0xce, 0x14,0xa0,0xa5,0x54,0xf8,0x7e,0xc9,0xdf,0xe1,0x3,0xc7,0xc8,0x30,0xdd,0x89,0xbf, 0xa4,0xdb,0x49,0xaa,0xdf,0x40,0xdb,0xae,0x89,0x8d,0x84,0x58,0x73,0x73,0x27,0x7, 0x14,0xcd,0x5c,0xd,0xcb,0x26,0x6c,0xad,0xa8,0x35,0xf5,0xd8,0x92,0x80,0x98,0xb6, 0xdb,0x62,0x61,0xbb,0xa2,0xbd,0xe9,0xab,0x4b,0x6f,0x5,0x3e,0xe2,0x2c,0x45,0x76, 0x79,0x21,0x83,0xc4,0xc7,0xf0,0xf2,0x70,0xa5,0xe8,0x4a,0xb7,0x69,0x62,0xee,0x45, 0xc4,0x50,0x81,0xe6,0x8d,0x6b,0x93,0xd8,0x5a,0x18,0x96,0x3d,0xc3,0x5c,0x33,0x3e, 0x7d,0x37,0x3,0x45,0xa7,0xf5,0xb6,0x4d,0x5f,0x80,0x84,0xc8,0xe2,0xf2,0x8e,0x28, 0x44,0x8f,0x8e,0xd1,0xfa,0x22,0x2b,0x56,0xb9,0xc1,0x13,0x7e,0x1e,0xc6,0xbc,0x1c, 0xfd,0x3f,0x61,0xa5,0xb5,0x18,0x72,0x15,0x18,0x76,0x5d,0xfb,0x6a,0x6b,0xa3,0xae, 0xfa,0x32,0x0,0x76,0xd4,0xaa,0x4c,0x8e,0xec,0xde,0xd,0x8a,0xa5,0x49,0xa6,0xa3, 0x9,0x9,0x49,0xbe,0xa0,0x3b,0x53,0xb9,0xb2,0x30,0x35,0x1d,0x9c,0xd8,0x4b,0x17, 0x8a,0xca,0xd,0x5f,0x76,0x59,0x6e,0xe2,0x39,0x7b,0x6d,0x5e,0xc5,0x15,0x82,0xce, 0x9d,0xcb,0xd,0x3e,0x87,0xdf,0x77,0x3a,0x10,0xac,0xd6,0x2c,0x5,0x22,0x44,0x90, 0xec,0x51,0x6f,0xe2,0x2b,0xdd,0x45,0xe3,0xd9,0xb3,0x42,0x1f,0x48,0xc4,0xed,0xe5, 0x11,0x7a,0xa3,0x18,0x5a,0x1c,0x52,0x6a,0x48,0x29,0x17,0xcd,0xca,0x5b,0xdd,0x37, 0x2c,0x4d,0x9a,0xd6,0xab,0xdf,0xba,0x85,0x93,0x7d,0xa4,0xdb,0xc1,0x12,0x41,0x52, 0x8c,0xe5,0x6a,0x66,0x81,0xbc,0x50,0xc9,0x65,0x67,0x17,0xaf,0x42,0xf4,0xe7,0xee, 0x43,0x2,0xc5,0x6e,0xe1,0x1,0xf3,0xf5,0x7e,0x18,0x51,0xbf,0x2a,0x93,0x13,0x36, 0xf8,0x7d,0x1c,0x7a,0xba,0x6c,0xc3,0x9f,0xd4,0xdb,0x50,0x96,0xd0,0xb7,0x85,0x93, 0xb9,0x4c,0x2,0x9b,0xcc,0x75,0x91,0x4b,0xd,0xe3,0x8a,0x37,0xf6,0x9d,0xec,0xef, 0x1c,0x9,0x6a,0xd6,0xf5,0xad,0x76,0x4a,0x89,0x46,0xe0,0xda,0xfd,0xe6,0xed,0xb7, 0xb2,0x70,0xd3,0x7f,0xe5,0x65,0x4a,0x73,0xc8,0xd4,0xaa,0x3f,0x73,0x18,0x2f,0xf, 0xa0,0x19,0xe5,0x96,0xc7,0xdb,0xe0,0xd0,0x23,0x42,0x2b,0xa0,0x29,0x1a,0x59,0xdb, 0x8a,0x2d,0xda,0xef,0x12,0x25,0x63,0x5b,0xf9,0x8e,0x9a,0xec,0x26,0x4a,0xfb,0xc6, 0xe2,0x61,0xdd,0x2a,0xbd,0x3e,0x7b,0xe0,0x0,0xa6,0x1,0xa8,0x40,0x5a,0x84,0x4a, 0x7,0xde,0xba,0x99,0x4,0x9d,0xf4,0x7e,0xab,0xf,0xea,0xd1,0xd8,0xe7,0x19,0xbc, 0xc8,0x76,0xe6,0x86,0xb4,0x62,0xe6,0xb5,0x89,0xe8,0x5e,0xc9,0x43,0x63,0x94,0xca, 0xc1,0x4f,0x64,0xc6,0xec,0xd8,0xc4,0x99,0xe7,0xaf,0xea,0xc1,0x17,0x4,0xfd,0x60, 0xf9,0xe4,0xe6,0xaf,0xc7,0xce,0xe4,0x51,0x37,0xc2,0x9a,0xf9,0xa5,0x2f,0xc4,0x68, 0x7e,0x29,0xae,0xeb,0x2,0xf2,0x5,0x6a,0x22,0xef,0xab,0xb9,0x74,0xa9,0x1a,0x6e, 0xe,0x1,0x9d,0xd5,0x4f,0x2,0xa6,0x86,0x45,0x42,0x81,0xea,0xf0,0x46,0xd2,0xef, 0xef,0x1,0x5b,0x71,0xf3,0x60,0x5b,0x17,0xcf,0x7,0xd0,0x44,0x30,0xea,0x33,0x3f, 0x6b,0x50,0x94,0xbb,0x53,0x3c,0x42,0x98,0xfd,0x43,0x3,0x6e,0xa,0xd6,0x5e,0xf9, 0xd7,0xb9,0xea,0x4c,0x99,0x47,0xe2,0x6a,0xcd,0x33,0x2e,0xfe,0x9d,0x61,0xbd,0x9, 0x32,0x52,0x44,0x85,0xe,0x87,0x1e,0x8b,0x4a,0xa0,0xfa,0x54,0x77,0xd8,0xcd,0xcf, 0x13,0xb9,0x9b,0xac,0x80,0x7e,0x96,0xcd,0x31,0xc5,0x4c,0xce,0xa6,0xa,0x57,0xd8, 0x5d,0x9c,0xdd,0xea,0xa3,0x7b,0x77,0xed,0x1d,0xf1,0x43,0x14,0xca,0x11,0xe3,0x5d, 0x4a,0xfe,0xb,0x4a,0xfc,0x21,0x19,0x2e,0x66,0x65,0xfc,0xe,0x70,0x55,0x66,0x4d, 0xf1,0xc4,0x38,0x95,0x40,0x2f,0x3,0x5d,0x21,0x46,0x72,0x6c,0xd7,0xd5,0xc9,0x22, 0xd5,0x54,0x6d,0xd2,0x76,0x6,0x81,0xdc,0x6b,0xfd,0x6a,0x5b,0x53,0x51,0x28,0xc4, 0x16,0xe0,0xd9,0x56,0x10,0xdd,0x34,0xb1,0xa3,0xa6,0x1e,0x7b,0xfb,0xe7,0x9e,0x51, 0x3d,0x8b,0xa4,0x33,0x11,0x26,0x10,0x7c,0x24,0xfa,0x58,0xf7,0x4c,0x80,0x3c,0xe1, 0x61,0x96,0x38,0xf1,0x74,0x6c,0xa3,0x97,0x92,0xc1,0x14,0xf,0x29,0x32,0x60,0xe5, 0x3d,0x84,0x98,0x4e,0xaa,0x29,0x4a,0x4f,0x24,0xa2,0xc6,0xef,0xa3,0x3,0xd1,0x5, 0x99,0xa,0x76,0x8d,0xf6,0x1a,0x26,0x9,0x5b,0x3a,0x97,0x5,0xeb,0xf8,0xea,0x29, 0x7d,0x4,0x77,0xa8,0x2d,0x41,0x77,0x51,0xe4,0x3e,0x41,0x88,0x41,0x92,0xd,0xdb, 0x1c,0x84,0xe8,0x13,0x1e,0xf,0x9c,0x7a,0xc8,0x34,0xfe,0xb4,0xac,0x69,0x5d,0xaa, 0x6d,0x54,0xd2,0x9a,0x96,0x4a,0xeb,0x7b,0x88,0xac,0x83,0x49,0x3f,0x10,0x25,0x5c, 0x14,0x8e,0xee,0x33,0x9d,0xb,0x2d,0xe6,0x40,0x2c,0x1b,0x6c,0x95,0x79,0x17,0x4, 0x4d,0xe9,0x9e,0xe3,0x34,0xb,0xde,0x3c,0x37,0xe1,0x86,0xf6,0xf2,0x2b,0xd2,0x7, 0xb9,0xc1,0x3a,0xd7,0xcd,0xe6,0xbe,0x8d,0x13,0x59,0xf9,0x29,0xd2,0x91,0xac,0xa0, 0x7b,0x4b,0x84,0x30,0xd5,0xe3,0xeb,0xe,0xc5,0x72,0x84,0xb8,0x9e,0x57,0x40,0xd7, 0x98,0xf9,0xaf,0xe5,0xe1,0xed,0x73,0x74,0xc7,0xed,0x9d,0x9a,0x7f,0x4a,0xba,0x7a, 0x16,0x40,0x2a,0xeb,0x24,0x17,0x79,0x69,0x9,0x7d,0x23,0x27,0xd4,0x63,0x0,0x6e, 0xdc,0x2f,0x54,0xbe,0x9d,0x48,0x34,0x65,0x36,0x51,0x7f,0x35,0x9c,0x3b,0x2f,0x32, 0xfa,0xd9,0x9d,0x9e,0x70,0x18,0x8,0x79,0x15,0xaa,0xa1,0xea,0x8d,0xa1,0x59,0x6b, 0x50,0x2d,0x2a,0xed,0x75,0xdd,0x53,0x2b,0x30,0x53,0xdf,0xcc,0x8e,0x10,0xfe,0x89, 0x69,0x9c,0x28,0xd9,0x34,0xaf,0x53,0x4a,0x5b,0x74,0xb4,0xe8,0x95,0x8d,0x54,0xe6, 0xba,0x7f,0x54,0xb0,0xdc,0xa8,0xdb,0xd,0x7b,0xbc,0xd9,0xa,0x4c,0x58,0x13,0x35, 0x75,0xba,0xf,0x29,0x6a,0xe1,0xf2,0xc5,0x57,0xa7,0xaf,0xec,0x35,0x4,0xd3,0x70, 0x3,0x29,0x21,0x60,0x51,0x7c,0x6d,0xcc,0xb8,0xc7,0x56,0x84,0x20,0x69,0xb9,0x15, 0x24,0x48,0x3f,0x8e,0x2b,0xb1,0xd4,0x82,0x5a,0x84,0xee,0xf,0x8,0xc3,0xfe,0x8b, 0x6c,0x9f,0xeb,0x3d,0x1d,0x59,0x89,0x55,0x21,0xdf,0x5a,0xc1,0x49,0x14,0x56,0xec, 0xdc,0x15,0xfa,0x8,0xc7,0xcf,0xa,0x22,0x54,0x78,0xb0,0xdc,0xbb,0xb0,0x68,0x28, 0xcf,0xd3,0xe4,0x6c,0x2d,0x6e,0xc2,0xce,0x4e,0x1d,0x10,0x17,0xb0,0xe5,0x4,0xd, 0xfb,0x0,0x15,0xc3,0x4f,0x9e,0x65,0xa4,0x18,0x95,0x1,0xd3,0xc5,0x69,0x7c,0x96, 0x3d,0x61,0x3,0xe9,0xd0,0x45,0x38,0x9e,0xe1,0xc7,0xb6,0x13,0xae,0xba,0x20,0x2a, 0x3a,0x36,0xed,0x8a,0x54,0xd2,0xae,0xeb,0x68,0xaf,0xc0,0xae,0x98,0xbc,0x45,0x55, 0x1e,0xc7,0xbe,0x6e,0xe,0x77,0xe,0xef,0x3f,0xc4,0x3,0x6d,0xfe,0x24,0x97,0xb9, 0xd9,0x5,0xc3,0xad,0x57,0x72,0x9a,0xc0,0xa1,0xda,0xee,0x3a,0x97,0x34,0xf,0x35, 0xfb,0xcd,0xa4,0x89,0x45,0x32,0xf9,0x5,0xf6,0x7c,0x72,0x75,0x20,0x8a,0x2f,0x79, 0x8f,0xf2,0x28,0xe7,0xe4,0xc2,0x28,0x86,0x1d,0x17,0x40,0xb4,0xca,0x4f,0x69,0x46, 0x1e,0xe,0x50,0x63,0x40,0x4a,0x68,0xb6,0xc6,0x5b,0x2d,0xe7,0xe5,0xdb,0x61,0xf4, 0xcf,0x9,0xdc,0xb4,0x4b,0x84,0xbb,0x68,0x1b,0xfb,0x9c,0x65,0x4c,0x7,0xac,0x6a, 0x15,0xfc,0x4d,0xd5,0xc6,0xb6,0xc,0x8d,0x91,0xb8,0xf4,0x77,0x95,0xd6,0x6c,0xe4, 0xdf,0xc9,0x19,0xab,0xcd,0xd4,0x14,0xe9,0xd1,0xb1,0x4f,0x1e,0xb8,0x7b,0x8,0x4d, 0x78,0x55,0xa2,0x3f,0x8b,0xaf,0x4d,0x1d,0xe7,0xc1,0x14,0x7d,0x98,0x81,0x62,0xf8, 0xca,0x7c,0x24,0x98,0x51,0x38,0x2,0xa2,0x69,0x52,0x40,0x22,0x4d,0x48,0xef,0xc6, 0x9e,0x92,0x85,0xa9,0xc1,0xd2,0xc7,0xaa,0x15,0xdb,0xa7,0xad,0xdc,0xb,0x26,0xa7, 0x7,0x4a,0xc0,0xd7,0x3,0xc2,0x7b,0x6c,0x94,0xbb,0xf,0xe2,0x84,0xfe,0x29,0x23, 0x11,0xae,0xcc,0x53,0x2,0x14,0x7d,0x17,0x70,0x25,0x44,0x4d,0xaf,0xea,0x75,0x36, 0xb4,0xb5,0xf,0xb7,0x78,0xa,0xa4,0x8d,0x45,0xb3,0x70,0xc9,0xb2,0x99,0x6c,0x43, 0xc7,0xb9,0x96,0xc9,0x4d,0x14,0x60,0xbd,0xb9,0x25,0x8b,0x69,0x10,0x80,0x20,0x44, 0x36,0x2f,0xfc,0x2e,0xb8,0xa1,0xbb,0xfd,0xd4,0xab,0x48,0x7,0x45,0x34,0x4a,0x8d, 0xed,0x61,0xd6,0xbb,0xf4,0x38,0x79,0xae,0xdc,0x84,0x98,0xec,0x5,0xb8,0x31,0x3b, 0x67,0xad,0xe9,0x20,0xce,0xa5,0x9d,0xa3,0x52,0x65,0xaa,0x17,0x9a,0xf5,0xa4,0x8, 0xd6,0xfb,0x43,0xcb,0x34,0xbd,0x7b,0x11,0xc1,0x93,0x7d,0xc7,0x4c,0x2e,0x82,0x33, 0x5c,0x6c,0x53,0x2b,0x13,0x70,0x4f,0xe4,0x56,0xf9,0xfb,0x70,0x6f,0x21,0xf7,0x46, 0x1d,0x3c,0x13,0xd0,0x79,0xe,0x61,0x3b,0xa1,0x5e,0x3,0x6d,0x8c,0x86,0xa0,0xe8, 0x72,0xf3,0x94,0x5,0xe3,0xe3,0xe9,0x3a,0x5d,0x66,0x2a,0xcd,0x7,0x23,0x93,0xa3, 0x5f,0xa6,0x74,0xd8,0x34,0x55,0x14,0xd5,0xb3,0x18,0x43,0xbf,0x1e,0xe3,0x29,0x90, 0x57,0xbd,0x96,0xbb,0x21,0x0,0x75,0x7e,0x66,0xa0,0x4c,0xec,0xc3,0xe0,0x90,0x23, 0x7,0x84,0x7b,0xbb,0xd9,0x8f,0x11,0x8d,0x27,0x55,0xcd,0xc4,0xb8,0xf6,0x56,0x90, 0xb4,0x6c,0x4c,0x55,0xeb,0x41,0xd3,0xd2,0xe1,0x21,0xbf,0xa5,0x81,0x51,0x48,0x8, 0xd5,0xc3,0x43,0xb0,0xd3,0x55,0xbd,0xfa,0xaa,0x8b,0xc0,0xe2,0x2,0x96,0xf2,0x36, 0x82,0xbe,0x8b,0x6e,0x1,0x60,0x41,0x62,0x1,0x2,0x9,0x2,0xd2,0xd0,0x89,0xa8, 0x15,0xcd,0xd8,0xe8,0x23,0x17,0x63,0x4d,0x22,0xa3,0xaf,0x25,0xb9,0xa3,0x5b,0xbb, 0x62,0xe7,0x2b,0xe2,0x48,0xeb,0x46,0xc8,0x6d,0xce,0xca,0x40,0x9f,0x54,0x69,0x34, 0xa1,0xc1,0x9c,0xc4,0xd8,0x80,0x12,0xfb,0x24,0xc2,0xa0,0x5e,0xe5,0xfb,0x1a,0x48, 0xe3,0xc4,0x2c,0xab,0x31,0xf1,0xf3,0x9e,0xc0,0x3e,0x5f,0xdf,0x93,0xc8,0x15,0xb4, 0xa,0xb1,0x7a,0xe3,0x32,0x8c,0x5f,0xd6,0xce,0x0,0xb4,0xb4,0x7b,0x4e,0x7d,0xdf, 0x14,0x29,0xb,0x45,0x1b,0x0,0x63,0xdb,0x3e,0xc2,0xbb,0x51,0x8b,0x50,0x7,0x16, 0x82,0x81,0x79,0xb4,0x8d,0xd8,0xb,0xdc,0x58,0x3f,0x11,0x53,0x8e,0x8e,0x33,0xa2, 0xb7,0xbe,0x67,0x52,0xbe,0xca,0xad,0x7c,0x8e,0xe9,0x4e,0x99,0x3a,0x55,0xaf,0xbc, 0x56,0x29,0xf1,0x63,0x81,0x7c,0xbf,0x59,0xbc,0xd1,0x2d,0x4b,0xdf,0x60,0x6d,0x98, 0x9e,0xd4,0x6a,0x5d,0x1f,0x19,0x5a,0x2d,0x3,0xa8,0xc7,0x3d,0xfd,0xf6,0x7a,0xd3, 0xa0,0x6c,0xb6,0xa1,0xe8,0x77,0x7b,0xa5,0xc8,0xa8,0x70,0xa8,0x88,0xdd,0xc0,0x28, 0xb2,0x2c,0x5,0x52,0x45,0x5f,0x7f,0x48,0x87,0xc6,0x5,0x85,0x3e,0x7f,0xd8,0xde, 0x6b,0x90,0x0,0xd4,0x87,0xfa,0x7a,0x50,0x23,0xeb,0xf8,0xac,0xc9,0x3a,0x54,0xfc, 0x66,0xd8,0x4f,0x2b,0x39,0xce,0xf2,0xc0,0x96,0xf7,0xc6,0x54,0xf7,0x1f,0x33,0x63, 0x2f,0xb2,0x38,0x36,0xae,0x33,0x86,0xd1,0x9e,0x0,0xfd,0xe7,0x3a,0xd1,0xe4,0x20, 0xab,0xb3,0x4b,0x64,0x3,0x3e,0x25,0x19,0xb5,0x6b,0x6d,0xad,0xb,0x20,0x91,0x3a, 0xd2,0xc9,0x71,0x1,0x7c,0x77,0xd3,0x1b,0xf6,0x51,0x4,0xb0,0x24,0x68,0xd0,0xcf, 0x1d,0x9b,0x34,0x20,0xd9,0xd8,0xb8,0x10,0xc4,0x26,0xbd,0xcf,0x46,0x4f,0x89,0x19, 0x99,0x7a,0x9a,0x16,0x72,0xed,0x32,0x69,0x3f,0xb5,0x1b,0x63,0x1e,0x6b,0xb2,0xba, 0x8,0xe6,0xda,0x61,0x40,0x93,0x71,0x5,0x39,0xaf,0x54,0x7f,0x7e,0x5d,0x19,0x18, 0xd8,0xb3,0xae,0x4b,0xa1,0x60,0x34,0xe0,0x16,0x4f,0xc4,0x34,0x3b,0x77,0xef,0x43, 0xde,0x4a,0x24,0x1f,0x5e,0x16,0xa3,0x97,0xc5,0x77,0x97,0x44,0xd4,0xb0,0xdc,0xad, 0xe3,0x8b,0x78,0x85,0xeb,0xad,0xe5,0x2,0x7c,0x2a,0xb5,0xb7,0x22,0x25,0x7a,0x1, 0xef,0x9f,0x9f,0x4e,0xb5,0xc2,0x65,0x7b,0x3a,0x7c,0x3f,0xf,0xac,0x1c,0x3d,0x90, 0x27,0x35,0x95,0x92,0xe2,0xfb,0x94,0x60,0x26,0xca,0x97,0xc7,0x6f,0x13,0x48,0x5f, 0x32,0x67,0x2d,0xe7,0x2a,0x13,0xe2,0xe3,0x8f,0xa1,0xf3,0x3d,0x3e,0xb0,0xcd,0x65, 0xe5,0xe3,0xf8,0x49,0xdf,0xd,0x29,0x85,0x57,0xc0,0x4e,0xc7,0x53,0x96,0x27,0x85, 0x7e,0xd4,0x6d,0xa8,0xe7,0xcf,0x8d,0xf6,0x72,0x1,0x34,0xb0,0xb1,0x82,0x95,0x17, 0xe5,0xe,0x60,0xc5,0x1c,0x89,0xca,0x73,0xca,0x98,0xba,0x1e,0xaf,0xe2,0xa4,0x2e, 0x37,0x91,0xd6,0x1f,0x62,0xe3,0x95,0x54,0xe4,0xca,0x84,0x16,0xcc,0x1a,0xad,0xb2, 0x29,0xe,0xf7,0xc4,0x18,0xc2,0xb7,0xe2,0x5c,0x73,0x1,0x8b,0xd5,0x25,0xb9,0xd, 0xb7,0x90,0xab,0x99,0xf4,0x41,0xed,0xd9,0x8b,0x72,0x70,0xd7,0xc,0x1e,0x8a,0xb4, 0xab,0x2,0x79,0x43,0x45,0x32,0x26,0xa1,0xa5,0xa7,0x2d,0xfa,0x4c,0x66,0x8,0x4, 0xf6,0x33,0x1d,0xeb,0xf3,0xb,0x46,0x80,0xfc,0x36,0x58,0x89,0x54,0x63,0x3e,0x7f, 0xe4,0xb8,0xc3,0x2a,0x6a,0x69,0xcb,0x8f,0x90,0x78,0x8a,0xdd,0xde,0x12,0x61,0x56, 0x45,0x7f,0xc1,0x39,0xa,0x87,0x39,0x87,0xbd,0x12,0x11,0x91,0xf4,0x4f,0x12,0xd9, 0x87,0x55,0x5,0x71,0x3e,0x50,0x1,0xcf,0x49,0xb,0x2d,0xa7,0x1d,0x8e,0x7d,0xe1, 0x8d,0x40,0x9b,0x18,0xc7,0xd4,0x9f,0x6,0x66,0x30,0x97,0x5b,0xfe,0x29,0xb5,0x87, 0xfd,0xba,0x78,0x3d,0x8a,0x7a,0x8c,0xd3,0x85,0xb9,0xfb,0x23,0xc7,0x79,0x5,0xd5, 0xb9,0xa0,0xed,0x2,0xf5,0xd,0x8,0xdb,0x3d,0x1f,0xb7,0x3c,0x49,0x6d,0x43,0x47, 0xa7,0xbc,0x84,0x32,0xb6,0x90,0x86,0xbb,0x4a,0x82,0xde,0x92,0xfb,0xe4,0x68,0x36, 0x5,0xd5,0xb7,0x7a,0xe2,0xbf,0x57,0x9f,0xde,0xf,0xdb,0xa7,0xfb,0x9f,0xef,0xa3, 0xdb,0xf3,0x55,0x92,0x85,0xdb,0x4e,0x4f,0xdd,0xad,0x61,0x5a,0x12,0xc9,0x90,0x17, 0x9f,0x48,0x92,0x82,0x87,0x69,0x22,0xe5,0x78,0x7e,0x8e,0x74,0x9d,0xfd,0x97,0xf8, 0x71,0xec,0xb,0xf6,0x49,0xd8,0xc6,0xa6,0x86,0x28,0x1,0x98,0x72,0x11,0xb0,0x91, 0xd8,0xc2,0x15,0x60,0x2c,0xb6,0xc6,0x24,0xb4,0xd4,0x18,0xd1,0xd2,0xaf,0xca,0x44, 0x1c,0xd5,0xbb,0x65,0xaf,0x2,0xd,0xb5,0x2a,0xe,0x4f,0x1c,0x9f,0x7f,0xae,0x78, 0xc1,0x43,0x59,0xed,0x79,0x20,0x91,0x2f,0xf4,0xa9,0x80,0x47,0x59,0x4c,0x8b,0x75, 0xa1,0x47,0x5b,0xd0,0x49,0x68,0x87,0xf3,0xf5,0xd6,0x10,0x15,0x56,0x3e,0x8e,0x18, 0x81,0xe7,0x85,0xfb,0x87,0x96,0xaa,0xfb,0x40,0x2b,0x43,0x19,0x77,0x4e,0xe,0x99, 0x16,0x69,0x6a,0x5f,0x51,0xf1,0xd2,0xc7,0x48,0x63,0xdc,0x1e,0xa1,0xea,0xb5,0x24, 0x52,0x3b,0x9f,0x59,0x51,0x4a,0x55,0x91,0x75,0x18,0xaa,0x6d,0x67,0x39,0x7,0xfc, 0x22,0x71,0xdb,0x74,0xe3,0xaf,0xbb,0x2c,0x92,0x18,0x4b,0x34,0x4,0x80,0xd7,0x56, 0x3c,0x77,0xb0,0x8d,0xc1,0x85,0x20,0xb7,0x1e,0x4a,0x25,0x5,0x83,0xab,0x2,0xa6, 0x9c,0xdd,0x9a,0x80,0x8d,0x56,0x2d,0x20,0xed,0xf7,0xd4,0xf1,0x78,0x2c,0xc8,0xb4, 0xa4,0xf8,0x43,0xe5,0xfd,0x63,0x9d,0x1c,0x2d,0x42,0x21,0xb1,0xed,0xa2,0xd7,0x8b, 0x81,0xf1,0x8b,0x8e,0xc7,0xb8,0x2f,0xb5,0xb0,0x83,0xa8,0x2a,0xaf,0xf0,0x5e,0x54, 0x69,0xa1,0x3b,0x67,0x84,0x58,0x4,0xb2,0x9b,0xa4,0xe3,0x89,0x48,0xbb,0x94,0xc9, 0x2d,0x21,0xd7,0xf4,0xd9,0x7,0xaa,0xb,0x8a,0xd2,0xb4,0x3b,0xc3,0x13,0xf,0x2d, 0x35,0xc9,0x95,0xb9,0x23,0x19,0xeb,0x3e,0xbd,0xcf,0xc7,0x6,0xb,0x5d,0x4f,0x38, 0xfd,0x28,0x2d,0xd7,0x2f,0xd8,0x62,0x3a,0xab,0x17,0xf4,0xef,0xaa,0x4,0x1d,0xdf, 0xce,0x32,0x19,0x71,0x4b,0x6,0xaf,0xa,0x55,0xf6,0x8f,0x61,0xd3,0xdf,0x19,0xd1, 0x8,0xc6,0x2a,0xb6,0x9f,0xc,0x70,0xca,0x24,0x65,0xba,0x4e,0xe9,0x58,0xad,0x38, 0xa,0x46,0xa9,0xd5,0xcb,0xd8,0x5f,0x22,0xcf,0xee,0x3,0x24,0xce,0x1c,0xf5,0x56, 0xe2,0x9f,0xe,0x2,0xac,0x7e,0x4d,0x50,0x64,0x8,0x9e,0x4e,0xdf,0xcb,0x86,0x6a, 0x12,0xaf,0x40,0xde,0x88,0x1f,0x1,0x58,0x8d,0x83,0x7c,0xdc,0x9f,0xf2,0x33,0x3, 0x92,0xc0,0x84,0x3f,0xbf,0xd1,0x8f,0x24,0x5a,0xad,0xf1,0x3a,0x79,0x78,0x24,0xc, 0xa7,0xe3,0xea,0x30,0x3,0x6b,0x8,0x11,0xee,0x5,0xed,0xe,0xf7,0x21,0x90,0xa, 0x62,0x16,0xc9,0x22,0x67,0xd8,0xc5,0xc1,0x7,0xb7,0x7c,0x0,0xaf,0xa0,0xc,0x57, 0x5,0x76,0x7,0x8,0x61,0xf,0x19,0xcf,0x14,0x86,0x5e,0x8b,0xa8,0xee,0x16,0xb, 0x84,0x5f,0xac,0xec,0x38,0x72,0x2e,0x3f,0xa9,0xaa,0x40,0x59,0xcb,0xcb,0x30,0xd0, 0x43,0x37,0x58,0x24,0xc5,0x72,0xf4,0xda,0xf8,0x53,0xe5,0x21,0xc1,0x7b,0xab,0xc6, 0xda,0x58,0x33,0x14,0x4a,0x61,0xd2,0xf3,0xd,0x92,0xcc,0x58,0x5f,0x7c,0x29,0x22, 0xb3,0x81,0xc5,0xf9,0x73,0xba,0xd4,0xec,0x8d,0x3a,0x8d,0x50,0xb6,0x3a,0x96,0x91, 0x12,0xc9,0x25,0x5d,0x2b,0xf8,0xd0,0xb7,0x8b,0x1e,0x8f,0x6a,0x9a,0xb8,0xc,0xce, 0xba,0xd2,0xc8,0x2e,0xd,0x1d,0x9a,0x9b,0x57,0x29,0x6b,0x8d,0x63,0x2,0x20,0xf4, 0x4b,0x45,0x52,0x76,0xbd,0xa3,0xae,0xc9,0xc1,0x3e,0xb3,0x5c,0x77,0xc0,0x2b,0x32, 0x13,0x73,0xdf,0x20,0x90,0x7b,0xbb,0x68,0xa4,0xa6,0xf5,0x87,0x28,0x95,0x7c,0x73, 0xdb,0x4f,0x6a,0x19,0xf2,0x98,0xe2,0x34,0x56,0x97,0x90,0xcd,0xd7,0x3c,0x7f,0xea, 0xaf,0x60,0x8a,0xc0,0xdb,0xc6,0x29,0x0,0x6d,0x1f,0x7,0x96,0xb5,0x83,0x89,0x11, 0x52,0xf3,0xa9,0xc4,0x8c,0xd,0xf8,0xe3,0x24,0xa,0xb1,0xfb,0x46,0xb1,0x66,0x75, 0x12,0xf0,0xb5,0x6d,0xb7,0xde,0x6d,0xa5,0x7e,0x74,0xbb,0xb3,0x77,0x45,0x44,0xca, 0x3a,0xed,0xf,0xc6,0xfa,0x9,0x2a,0x1f,0x92,0x5c,0x9a,0xd8,0xe,0x1,0xcd,0x20, 0x72,0x4,0xd,0xa9,0xe2,0x7a,0x4f,0xe0,0x6e,0xb,0x14,0x65,0xd0,0x58,0xaf,0xb, 0xc6,0xbf,0x51,0xc1,0x48,0x7c,0x61,0xda,0x58,0x7b,0x33,0x66,0xfc,0x1,0x6,0x6f, 0x84,0x13,0x19,0x68,0xd,0xe8,0xc8,0xfa,0x73,0xdd,0x60,0x44,0x36,0x11,0xce,0x7c, 0x50,0x21,0xbe,0x98,0x1d,0x20,0x73,0xf4,0x1b,0xa6,0x5b,0x18,0x27,0xe0,0x87,0xac, 0x73,0x21,0x94,0x0,0x89,0x5d,0xfa,0xfc,0xba,0xda,0xc1,0x71,0x6b,0x90,0xed,0xbb, 0x31,0xac,0x54,0xcd,0x4c,0x47,0xc2,0x68,0xed,0x1e,0x80,0x95,0x7e,0x88,0x42,0xf1, 0x29,0x56,0x71,0xb2,0x33,0xeb,0x2f,0xee,0xc7,0xf0,0x60,0x33,0x82,0xcd,0x6f,0xb3, 0x7b,0x43,0x82,0xc7,0x8b,0x45,0xaf,0xf8,0xe3,0xb0,0x8e,0xe1,0xb8,0x50,0x54,0xe1, 0xa6,0xc5,0x14,0x5a,0xb2,0x43,0x49,0xf9,0x35,0x29,0xac,0xb7,0xf6,0x1c,0xea,0x72, 0x60,0xec,0xba,0x6b,0xb2,0xe9,0x64,0x16,0x9a,0xf3,0xf7,0xd2,0xc3,0x4c,0xb4,0x6b, 0x92,0xc8,0xc5,0xc4,0x8c,0x8e,0xbe,0xc1,0xb7,0xea,0xf8,0x2e,0x8,0xe3,0x21,0xe7, 0x51,0x5b,0x53,0x4,0x45,0xb7,0x99,0x60,0x2b,0x91,0x33,0xef,0x5e,0x68,0xda,0x70, 0xb0,0x20,0x35,0x3d,0x2e,0xf3,0x7e,0xe5,0xde,0x77,0x93,0x66,0xdb,0xb4,0xcd,0x2d, 0x10,0xa0,0xb0,0xd5,0xd8,0x4a,0x36,0x4,0x5b,0xe8,0x73,0x39,0xd0,0x4e,0xa9,0x82, 0xed,0xde,0x3f,0x1c,0x52,0xbe,0x81,0xb1,0xb5,0x16,0x18,0x91,0xca,0x66,0x3e,0xdb, 0x7,0xee,0x31,0xdf,0xb8,0x67,0x64,0x94,0xcf,0xd7,0xcd,0xa1,0xa6,0x78,0xa3,0x14, 0x57,0x62,0x31,0xaa,0x21,0xb2,0x5c,0x57,0x48,0xf3,0xe8,0x14,0xd9,0x28,0x6f,0xe1, 0x96,0xa0,0x41,0xcf,0x87,0xa5,0x64,0x57,0xfd,0x32,0x78,0xa4,0xaa,0x1c,0xb8,0x3, 0x7f,0x69,0x2d,0x20,0x9c,0x89,0x77,0xe4,0xfc,0x61,0xf8,0xd7,0x9,0xe7,0x39,0x1f, 0x88,0x7a,0xee,0x8f,0xa0,0x53,0xe7,0x1e,0x6,0x60,0x42,0xb0,0xfc,0x7a,0x33,0x7c, 0xe4,0x60,0x9c,0x81,0x69,0x94,0xe5,0x67,0xf5,0xdf,0xbe,0x7e,0x47,0x77,0x9d,0x50, 0xf1,0xd,0xdf,0x12,0xdf,0x47,0x30,0xe5,0xa8,0x72,0x97,0x25,0xed,0xca,0xa1,0x52, 0x2c,0xbd,0x53,0x15,0x52,0x39,0xfb,0xc7,0x19,0xba,0xc5,0xe0,0x32,0xe3,0x31,0xa4, 0xf0,0x90,0x36,0xd0,0xd8,0x67,0xb7,0x1,0x59,0x4f,0x26,0xc6,0x99,0x47,0x19,0x45, 0x5,0x6c,0x5b,0xd7,0xa6,0x57,0x1f,0x3f,0x92,0xe5,0x20,0xc4,0xc9,0xd0,0xe8,0xba, 0x62,0x20,0xb,0x3b,0x7,0xc2,0x3c,0x60,0x91,0xe1,0x28,0x2c,0x29,0xc0,0xf0,0xad, 0x2e,0x4c,0x85,0x54,0x24,0xa5,0x93,0xb6,0xb,0x34,0x7b,0xd4,0x84,0xe4,0xf,0xe6, 0x5,0x1a,0xa1,0xc,0x5d,0x5d,0xeb,0xee,0x3f,0x14,0x9a,0x68,0x55,0x8c,0x96,0x3, 0x58,0x1c,0x57,0x7c,0x41,0x6a,0x33,0xcb,0x1e,0x2f,0x20,0xa3,0x14,0x2f,0x8a,0x19, 0xc9,0x2d,0xa4,0xa6,0x8a,0x90,0x15,0x4a,0x25,0xb0,0x32,0x7a,0xbc,0xc8,0x7d,0x15, 0x65,0x54,0x12,0xa6,0xbe,0x45,0x73,0xdd,0x74,0x13,0x1,0x8,0x43,0x8b,0xa0,0x8c, 0x38,0x45,0xb2,0x43,0xd6,0xc7,0x8d,0xfb,0xf7,0xbf,0xf5,0xb4,0x9,0xf2,0x4a,0x6e, 0x47,0x5c,0x94,0x6,0x21,0x87,0x63,0x16,0x9b,0x64,0x1e,0x5e,0x70,0xbf,0x6a,0xa8, 0x84,0x1d,0x6b,0x5b,0xe4,0xf8,0xd6,0x5d,0x39,0x4c,0x91,0x42,0x3f,0xdb,0x30,0x86, 0xb7,0xc4,0xd,0x59,0x4d,0xef,0x6f,0xe8,0xd4,0xd,0xc6,0x45,0x4c,0x31,0x6d,0xd1, 0x4e,0xd9,0xac,0xb2,0x52,0x4,0x8f,0x8b,0x50,0x22,0x4d,0x10,0x7d,0x7d,0x16,0x36, 0xc2,0x23,0xf,0x8f,0x93,0x7e,0x78,0x68,0xb,0xbe,0xad,0x58,0xef,0x9a,0x2a,0xbd, 0x74,0x56,0xef,0xc7,0x5a,0x80,0xd2,0x2b,0xa2,0xa0,0x3b,0x20,0x9d,0x51,0xd5,0xdf, 0xf4,0xe4,0x6f,0x88,0xe2,0x67,0x70,0xee,0x26,0x1e,0xc6,0x16,0x38,0xf0,0x53,0xad, 0xc6,0x44,0xf4,0xa1,0xc4,0x47,0xcc,0xe6,0x67,0x87,0x86,0x6,0x58,0x5d,0xe5,0xcc, 0xc1,0x56,0xd4,0x25,0xbd,0x45,0x93,0x64,0x63,0x5a,0x7a,0x1c,0xca,0x4e,0xc9,0x91, 0x92,0x3e,0x33,0xd6,0x5,0x7f,0xbd,0x6d,0x7,0x44,0xf2,0xdf,0x21,0x58,0xac,0xe3, 0x2e,0x82,0x88,0x6c,0xc7,0x1c,0xd0,0xab,0xf5,0xca,0xc7,0xc0,0x19,0x11,0xd1,0xab, 0x4f,0x6,0x2,0xd3,0x5,0xbf,0x41,0x8c,0x5,0x34,0x6c,0x26,0xd,0x19,0x89,0x3b, 0x1b,0x91,0xa7,0x63,0xad,0xf7,0xf,0x23,0xc3,0x56,0xe3,0x5c,0x67,0xb6,0x88,0x36, 0x3c,0x8a,0xa,0x41,0x4b,0xcb,0xcd,0xcf,0x7f,0xb9,0xf5,0x8c,0x53,0x0,0xc8,0x6e, 0x91,0xef,0xd1,0xbf,0xe8,0x60,0xe2,0x2c,0xb6,0xc7,0x88,0x9d,0xfd,0x11,0x53,0xb9, 0x9c,0xdd,0x7a,0xe7,0xa9,0xc8,0xb7,0x29,0x82,0x2d,0x36,0xd5,0xac,0xfe,0xc4,0x3f, 0x6e,0x16,0xfe,0xd6,0x77,0x61,0x3,0xad,0xa8,0x8c,0xcb,0x26,0x1d,0x1f,0xdf,0xb9, 0xfc,0x5b,0x21,0xa6,0xa3,0x58,0x50,0x26,0x6,0x86,0x7c,0xb2,0x5,0x41,0xf1,0xf2, 0xd6,0x70,0xca,0x4e,0xd2,0x4d,0x7c,0xfa,0x59,0x48,0x22,0x77,0xe6,0x2,0x31,0xe4, 0xdc,0xd2,0xb,0x80,0x2b,0x5b,0x27,0x31,0x61,0xa3,0xe4,0x66,0x64,0x56,0x5a,0x3b, 0x47,0xa4,0xa,0x1a,0xf1,0x86,0x94,0x4c,0x4e,0xb6,0xc3,0x35,0x39,0x74,0x1a,0x16, 0xc6,0xa5,0x17,0x72,0x80,0x3e,0x23,0xe2,0x61,0x87,0xc8,0x45,0xde,0xa2,0x80,0x26, 0x47,0xa,0xbf,0x3a,0x10,0x54,0x6,0x5e,0xc,0x49,0x94,0x45,0x3d,0x2e,0xda,0x5, 0x53,0x71,0x77,0xd4,0x2f,0x9a,0xb7,0x90,0x23,0x80,0x55,0x81,0x24,0x56,0xa7,0xea, 0x60,0xe6,0xa4,0x71,0xba,0xaa,0x4f,0x46,0xf3,0x63,0x8b,0x32,0x12,0xe6,0xb6,0x65, 0x58,0x2e,0x3a,0x8,0x48,0xf1,0x98,0x6b,0xf2,0x6e,0x6c,0x96,0xc4,0x93,0x81,0x25, 0x7a,0x27,0x16,0x36,0x51,0x66,0x7c,0x46,0xc9,0x88,0xf7,0xdb,0xee,0xae,0xc1,0xc6, 0x5c,0xfb,0xce,0xa4,0x6e,0xe7,0x90,0x61,0x56,0xfc,0x77,0x1b,0x91,0x78,0xbf,0x8b, 0x9f,0x56,0x41,0x71,0xbc,0x3e,0x37,0x6,0xc6,0x2f,0x62,0x35,0x5d,0x24,0xfb,0x39, 0x9f,0xcb,0xdd,0xe,0x33,0xed,0xee,0x89,0x6b,0x66,0x24,0xfc,0xdf,0x63,0x8,0xfe, 0xb9,0x4a,0x70,0xf5,0x88,0xa7,0xfc,0xce,0x56,0xde,0x4,0x33,0x3,0x7f,0x6c,0xa2, 0x4b,0xca,0x31,0xfd,0xb8,0x20,0x87,0x24,0x7,0x2b,0xa0,0x66,0x8f,0xa9,0xe4,0xc8, 0x73,0x56,0xbf,0xfb,0x7d,0xbc,0x4a,0x54,0x1b,0x4e,0x87,0x9d,0xcd,0x74,0xbf,0x99, 0x3f,0xf0,0x97,0xf7,0x91,0x9f,0x9c,0x98,0x4a,0x3d,0xfe,0x59,0x66,0x63,0x23,0xd9, 0x39,0xe2,0x55,0xb7,0x1f,0x9f,0x8b,0x3a,0x6d,0x92,0xd7,0x3c,0x7,0x97,0x55,0xc5, 0x89,0x6c,0x3e,0x1b,0x8b,0xda,0x33,0xd6,0x97,0xb1,0x30,0xfe,0x15,0x53,0x58,0x4f, 0x36,0xae,0x86,0xd4,0xcd,0x91,0xf,0x3c,0x24,0x66,0xf7,0xab,0xfe,0x4d,0x71,0x8, 0x39,0xaf,0xa2,0xc5,0xa,0x55,0x9c,0xa2,0x7,0x4c,0x21,0x9b,0x20,0xf8,0xea,0x56, 0xa7,0xf0,0x2c,0x76,0x82,0xba,0x32,0x27,0x22,0x2a,0xd2,0xa0,0xf6,0x44,0x28,0x30, 0x74,0xca,0xf5,0xfd,0x20,0x12,0xa0,0xa6,0xde,0x41,0x42,0xfe,0x3b,0xad,0xd4,0x62, 0x1e,0x80,0x58,0xa1,0x3c,0x8a,0x48,0xdd,0xb4,0x1b,0x7e,0xab,0xde,0xa6,0x5c,0x53, 0xf0,0xd1,0x52,0x90,0xe4,0x72,0x37,0x43,0x34,0xf8,0x42,0xee,0x26,0x17,0x51,0x45, 0x98,0xaa,0x66,0x54,0x35,0xae,0x32,0x6a,0x49,0x30,0x95,0x28,0xd6,0xf1,0xfb,0x47, 0xc4,0xcd,0xd7,0x29,0xbf,0x8e,0x6c,0xf3,0x7,0x2e,0x62,0xad,0x45,0xb4,0xf2,0xdd, 0xde,0xd8,0x32,0x93,0x7,0xe3,0xfd,0xcf,0x14,0x14,0xf7,0x6a,0x6,0x73,0xb1,0x4a, 0x41,0x9,0xf2,0x81,0x97,0xde,0xf4,0x1f,0xd,0x58,0xcc,0x53,0xd,0x3f,0xb0,0x6b, 0x97,0x63,0xfe,0x1e,0x47,0x7d,0xed,0x5c,0x91,0x65,0xc6,0x17,0xd9,0xf8,0xe1,0x9a, 0x2,0xd4,0x9b,0x1a,0xb4,0x91,0x39,0xc1,0xe9,0x85,0x94,0x76,0x44,0x46,0xe1,0xdb, 0x29,0x60,0xf9,0x70,0xdd,0x67,0x4c,0xee,0xcc,0x14,0x7,0x26,0xd,0xe8,0x41,0x8e, 0x3d,0xdc,0xa8,0x71,0xed,0x61,0xb3,0xd7,0xe6,0x48,0xcd,0x2b,0xe,0x2f,0x86,0x37, 0x90,0x0,0xa8,0x6e,0x67,0x74,0x5e,0xb4,0x88,0xe4,0x5a,0x15,0x4d,0x9b,0xa4,0x8a, 0xf8,0xcc,0x7c,0xe6,0x2f,0x30,0x3f,0x95,0x78,0xd,0xc1,0x7,0x3d,0xc7,0x3e,0x4d, 0xc8,0x66,0xbb,0xaf,0xdb,0x99,0x64,0xe3,0xfd,0xbf,0x79,0x4b,0xda,0x1e,0x56,0x53, 0xea,0xd2,0x3b,0x99,0x3,0xf9,0x30,0xfa,0x86,0x71,0x2,0xc3,0x39,0xc0,0x90,0x81, 0xa6,0xcc,0x32,0x2,0x66,0x16,0x66,0x65,0x55,0xdf,0x30,0x31,0x7d,0x86,0x4,0xe7, 0x59,0xbe,0x82,0xdb,0xb8,0x32,0xd7,0x40,0xa3,0x59,0x83,0x5c,0x99,0x15,0xde,0xc0, 0xe1,0x90,0x42,0xc7,0xa6,0x28,0xac,0xfc,0x8,0xdd,0xad,0x5,0xe3,0xb1,0xed,0xbd, 0x71,0xef,0x99,0xa9,0xa1,0xf0,0x69,0x45,0xca,0xed,0x21,0xe3,0x82,0x0,0x24,0x64, 0x90,0xe6,0xab,0x38,0xf,0x59,0xb4,0x97,0xb6,0x62,0x9c,0x9a,0x14,0xa,0xd7,0x5, 0xf9,0x72,0xaf,0x9b,0xe2,0x19,0x60,0xad,0x86,0x82,0x12,0x9,0x2,0x36,0xec,0x13, 0x1d,0x19,0xca,0x2d,0xf1,0x7f,0x44,0xa8,0xe1,0xe0,0xc2,0x75,0xeb,0x9b,0xfa,0x65, 0x8d,0xaa,0x81,0x70,0x43,0xe1,0x9e,0x4a,0xe3,0xb0,0xd2,0x66,0x66,0x40,0x79,0x84, 0x59,0x44,0x31,0x4b,0x43,0x75,0x73,0x25,0xd5,0x36,0x1a,0xc1,0x51,0x15,0xa7,0xde, 0x3f,0x29,0x50,0x3,0x8a,0xee,0x4d,0x6f,0x1f,0x9f,0x55,0x85,0xdf,0xce,0x89,0xb8, 0x92,0x3a,0x83,0xd5,0x2f,0xf6,0x7a,0x6,0xad,0x94,0x47,0xfe,0xaa,0xee,0xde,0xe9, 0x18,0xae,0x6c,0x23,0x1d,0x39,0x12,0x3c,0xd9,0x67,0xc1,0x39,0x36,0x4c,0x72,0xc8, 0x6,0xf5,0x1e,0x36,0x6d,0x98,0x3c,0x9a,0x2d,0x83,0x99,0x57,0xf2,0xf7,0xc1,0x8a, 0x26,0x2e,0xad,0x43,0x68,0xbf,0x7f,0xc1,0x27,0xc1,0x7a,0xdc,0x8d,0xec,0x25,0x93, 0x63,0x43,0xc9,0x50,0x5b,0x85,0xea,0x89,0xa,0x84,0xe0,0x7c,0xfc,0x22,0x7,0x23, 0x51,0xb5,0xe6,0x39,0xf4,0x66,0xfa,0x9c,0xa7,0xf4,0xf8,0x35,0x62,0x1f,0xc9,0xc5, 0xe1,0x93,0x16,0x3e,0x1a,0x1,0x47,0xa3,0x5,0xa7,0x9f,0x81,0xca,0xa6,0x25,0x1c, 0xdb,0xc,0xd4,0x51,0xf1,0x4f,0xed,0x9a,0x44,0xe6,0x4f,0xa6,0x85,0x19,0x6c,0xe7, 0x2d,0x2,0x26,0xc6,0x82,0x6d,0xe9,0x8,0x15,0x89,0x89,0x5f,0xaf,0xae,0x7b,0x8c, 0x3a,0x50,0xdd,0x2d,0x1f,0x4b,0x47,0x64,0xb1,0x96,0xb,0x38,0x30,0xf7,0x9f,0x5d, 0x79,0xc5,0xa3,0x7c,0xb2,0x8d,0x84,0x47,0x96,0xe,0xa7,0x46,0x3d,0xa2,0xd2,0xf6, 0x73,0x30,0x24,0x92,0x7b,0xea,0x76,0xad,0x82,0x82,0x65,0x32,0xf9,0x5,0x8f,0xf2, 0x4a,0xb2,0x6f,0xfc,0xbf,0xf3,0xc3,0x56,0x82,0xea,0x9c,0x3f,0x8e,0xef,0x36,0x81, 0x9f,0xda,0x14,0x9b,0xc5,0x8b,0x49,0xc7,0x8d,0xae,0xf9,0x7,0xb3,0x9,0x79,0x7d, 0xbb,0xe9,0x7a,0x7b,0x5d,0xbd,0x51,0xdf,0xa9,0x6e,0x9e,0xb7,0x5e,0xd5,0xb8,0x7d, 0xb0,0x4c,0x19,0xf5,0xd7,0x62,0xbe,0xe4,0x90,0x38,0x6b,0xc3,0x42,0xe5,0x41,0x7d, 0x4f,0x3b,0x79,0xac,0xf9,0xca,0xd,0x23,0x39,0x2b,0x5a,0x17,0x1,0x13,0x95,0x31, 0x5f,0xae,0x28,0xb7,0x91,0x66,0x1c,0x22,0x9e,0x88,0x66,0x60,0xed,0xa7,0xde,0xbc, 0x63,0x58,0xe8,0xdc,0xa2,0xf5,0x0,0xdc,0x22,0xd9,0xf3,0xa2,0xec,0x89,0x54,0xcb, 0xb8,0x7c,0x83,0x4a,0x62,0xa0,0xeb,0x80,0xa8,0x52,0xe1,0x16,0x7a,0x40,0xd2,0x5d, 0x18,0xbb,0x3a,0x3a,0x32,0xb9,0x17,0xd3,0x93,0x8b,0x76,0x0,0x94,0xca,0xcb,0x4d, 0xc6,0x50,0x17,0xa8,0x70,0x4,0x2a,0x98,0xd5,0x8b,0xae,0xcf,0x4b,0x1,0xac,0x63, 0xbc,0xe6,0x9d,0x6e,0xa0,0x35,0x42,0xb3,0x40,0x39,0xb3,0xd4,0x83,0x80,0x23,0x4b, 0x50,0xb9,0x73,0x40,0x3d,0x9d,0xd8,0x93,0x29,0x7,0x63,0x74,0x8,0x90,0x57,0x44, 0x77,0x75,0xb3,0x98,0x2a,0xf5,0x4c,0x6a,0x2f,0x1,0x3f,0x33,0x1,0xe1,0xfd,0x51, 0x1c,0x71,0x11,0x59,0x10,0xe9,0xec,0xb8,0xf0,0xd0,0xad,0xf8,0x61,0x84,0x3d,0x58, 0xf9,0xf0,0xf0,0xa3,0x67,0x3e,0xe,0x16,0xbe,0xcd,0x49,0x3f,0x2f,0x47,0x90,0x4b, 0x39,0xa1,0x25,0x49,0xb,0x12,0x81,0xfb,0x62,0x2f,0x74,0x43,0xb4,0x31,0x9c,0x2e, 0xa2,0x8d,0xd2,0x89,0x4b,0x60,0x9f,0x89,0x2e,0x69,0xc8,0xdd,0xb0,0xd8,0xa8,0x69, 0xf9,0xcd,0xb2,0x5,0x60,0x35,0x80,0xc2,0xe3,0x74,0x86,0x18,0xa6,0x23,0x47,0xc8, 0x30,0x1a,0x52,0xfb,0x7a,0x71,0x85,0x29,0xda,0x4f,0x86,0xc,0xa7,0x2f,0x75,0xa2, 0xfd,0xa8,0x27,0x5e,0x5d,0xa8,0xa0,0x41,0x9c,0x27,0x5a,0xc2,0x4a,0xa1,0x8b,0xfa, 0x3b,0x5d,0xf6,0x35,0xcf,0x7c,0xdd,0xaa,0x4b,0x64,0xb6,0xf3,0x94,0xac,0x16,0x12, 0x55,0x3d,0x70,0xb2,0xe5,0x90,0xf3,0x3,0xb8,0xcd,0xc5,0x82,0xee,0x52,0xfc,0x2a, 0xaf,0xf3,0xdf,0xfe,0xf0,0xbd,0xaa,0x3c,0xa2,0xe0,0xaf,0xb6,0x8d,0xc5,0xc8,0xe2, 0x4,0xb8,0x15,0x69,0x49,0x89,0x6c,0x81,0x57,0x33,0x84,0x47,0x5,0x81,0xf0,0x34, 0x76,0x50,0x34,0x67,0x8e,0x5e,0x23,0x31,0x3f,0xd3,0xe7,0x4d,0x99,0xb0,0x30,0x9d, 0x69,0xc5,0x87,0x32,0x4f,0xf3,0xb4,0xa6,0xa6,0x39,0x6d,0x2b,0xba,0xde,0x60,0xb0, 0x2f,0x14,0x18,0xbd,0x72,0x3c,0x6e,0xb1,0x8f,0x56,0x7e,0x29,0x86,0x2f,0x47,0x6f, 0xf4,0xce,0xa2,0x44,0x42,0xd6,0xea,0x69,0x8f,0xd8,0x94,0x4a,0xb7,0x74,0x7b,0x66, 0x88,0x13,0x25,0xfa,0xce,0x93,0x2d,0x5e,0x6a,0xab,0x8,0x70,0xda,0x4f,0x60,0x4f, 0x9d,0x82,0x93,0x5f,0x59,0xfe,0xc8,0xe8,0xd7,0xdd,0xb2,0xf,0x52,0xad,0x75,0xdb, 0xc1,0x9a,0x56,0x90,0xae,0x83,0xef,0x98,0xaf,0xf7,0x88,0xa,0xc6,0xe8,0x5a,0x64, 0x6b,0x6d,0x43,0x44,0x6c,0xd,0x2d,0x44,0x6a,0x60,0x53,0xbc,0xe,0x49,0x18,0xcf, 0xe3,0x6f,0xe0,0x12,0x72,0xd0,0x2a,0xa1,0x48,0xb3,0xac,0xf,0x1c,0x86,0xf2,0x88, 0xf3,0x36,0xcc,0xe0,0xc2,0x7a,0x25,0x2d,0xda,0xf8,0x6a,0x68,0xc1,0x82,0xb8,0xa5, 0x71,0x99,0x38,0xe4,0xe9,0xe1,0x6,0x32,0x95,0xb2,0xc0,0xb2,0xb8,0xb3,0xba,0x2d, 0x69,0x87,0xe,0x2d,0x2,0xb2,0xd9,0x5c,0x2b,0xc3,0x45,0xec,0x47,0x7d,0x13,0xb8, 0x17,0xca,0x1d,0x80,0xac,0x24,0xb2,0xc2,0x56,0x73,0xf4,0x8f,0xa6,0xaf,0xbc,0x10, 0xb6,0x4a,0xbc,0x39,0xfc,0x17,0x95,0x29,0xda,0x5a,0x95,0x22,0xd7,0xa8,0x5b,0x6e, 0x73,0xf7,0xee,0xa0,0x9b,0x21,0x63,0xf2,0x14,0x58,0x2,0xba,0x87,0xbe,0x4b,0x3e, 0x9,0x87,0x77,0x85,0x9e,0x8d,0x2e,0x7a,0xe7,0xc4,0x1c,0x40,0xec,0xf6,0xae,0xe0, 0x6f,0x9e,0x81,0xb,0xbf,0x64,0x7d,0x54,0xbc,0x7f,0xf,0xc3,0x3e,0xd9,0x2,0xc6, 0x62,0x7a,0x4d,0x1,0x8,0x7b,0xfa,0x6f,0xbf,0x97,0xaf,0xad,0xe,0x5f,0x8e,0x7d, 0x7d,0x10,0x89,0xbc,0xf3,0x7,0x11,0x30,0x87,0xa0,0xf3,0x45,0x7a,0xf5,0x8c,0x5c, 0xef,0xd9,0xdd,0x77,0xd4,0xd8,0xe7,0x95,0xef,0x97,0x43,0xfe,0x76,0x51,0x7c,0xf3, 0x61,0x6,0x31,0xd4,0x8d,0x42,0x5,0x94,0xe2,0xf8,0xd9,0xdd,0xee,0x66,0x3a,0x5f, 0xbf,0x18,0xd6,0x95,0x71,0xbe,0xaa,0x61,0xd6,0x6d,0x60,0x4d,0xbe,0x5d,0xc1,0x9f, 0xe2,0x72,0x74,0x70,0xb4,0x79,0x5,0x18,0x72,0x5f,0x75,0xe0,0x45,0xaf,0x40,0x6, 0x48,0x18,0x1b,0xb9,0xd6,0x45,0x9a,0x2d,0xb2,0x7b,0xfa,0x71,0xd8,0xbc,0x11,0xbb, 0xae,0x85,0xac,0x63,0xfe,0xb1,0xfa,0xf0,0x90,0x70,0xd1,0xd6,0xa0,0x13,0x5c,0x68, 0xaa,0xf6,0x22,0x1,0x3c,0x3c,0x2f,0xee,0xb7,0x2a,0xdf,0x90,0x66,0xf0,0xcc,0x15, 0x76,0x79,0xf7,0xf4,0xaa,0x73,0xe5,0x3c,0x63,0x37,0x92,0x4,0x4a,0x6e,0x6c,0x74, 0xe4,0xe,0x76,0x21,0xca,0xa5,0x8f,0x82,0x4f,0x6f,0x93,0xb5,0xdf,0x60,0x4a,0xd5, 0xd9,0x42,0xca,0x84,0xb5,0x30,0x40,0x1a,0x67,0xd2,0x9d,0x32,0xc0,0x8a,0xa6,0xa5, 0x18,0x1d,0x46,0xe2,0x42,0x55,0xe5,0x91,0xc4,0x79,0xc6,0x24,0xd9,0x11,0xf9,0xb3, 0xd3,0xc4,0xb7,0x89,0xf4,0xf8,0x23,0x5d,0x4b,0xc1,0xf,0x8c,0xcb,0xb5,0xb1,0xe3, 0xd3,0xf8,0xc7,0x95,0x4e,0xad,0x28,0x93,0xa6,0x6e,0xb7,0x80,0x80,0x32,0xb3,0x54, 0xf6,0xea,0x5d,0x6c,0xe3,0x81,0x49,0xaf,0xc2,0x58,0xbb,0x8e,0xe,0x6d,0xf1,0x61, 0x66,0xb9,0xf7,0x35,0xe6,0x9f,0x48,0x8d,0x8d,0x0,0x8d,0xe,0xb1,0xc0,0xe1,0xa9, 0xac,0xbf,0x95,0x10,0xc0,0x5e,0xbf,0x3,0xb6,0xfa,0x91,0x44,0x69,0x83,0x26,0xcf, 0xbd,0x9d,0x84,0x24,0x3d,0xcc,0x32,0x4a,0x4d,0x3f,0xd8,0xfe,0x1,0xba,0x28,0xad, 0xf9,0xbd,0xbd,0xba,0x1c,0xfd,0x3d,0x52,0xf8,0xce,0x17,0x62,0xd2,0x3d,0xb2,0x10, 0xda,0x37,0xb3,0x97,0x5,0x65,0xe1,0x52,0xa5,0xba,0x51,0x26,0xf5,0x7a,0xd3,0x6f, 0xb7,0x11,0x2b,0x54,0x8e,0x68,0xa6,0x8,0xb7,0xbd,0xe9,0xa,0x7a,0x1c,0x99,0x55, 0x54,0x4d,0xec,0xd8,0x33,0x4f,0xaa,0xd8,0x89,0x7b,0xfe,0x7f,0x75,0x52,0xef,0x2e, 0xe2,0x9a,0x82,0xf1,0x82,0xa8,0xf9,0xb9,0xe6,0x63,0x43,0x61,0x80,0xdc,0x37,0xd4, 0xaa,0xa3,0x2d,0xdd,0xf2,0xd7,0xb6,0x7d,0x53,0x35,0x7c,0xc9,0x7,0x6c,0x77,0x69, 0x86,0x79,0x5b,0xa,0xa1,0xd4,0x43,0x88,0x39,0x87,0x6a,0xb9,0x64,0x21,0xe,0xf, 0xc4,0x3b,0x6c,0xb8,0x92,0x23,0xb5,0x65,0xd7,0x32,0xae,0x5e,0x1f,0x26,0xc8,0x25, 0x1f,0xa3,0x2f,0xc1,0x79,0xf2,0xc9,0xb2,0x7a,0xb3,0xeb,0x5e,0xd4,0xf9,0xed,0x9a, 0xb4,0x5a,0xd2,0xc6,0xfd,0x88,0x2c,0x55,0x3a,0xdb,0xb4,0xd8,0x81,0xfc,0xfe,0xa1, 0xa0,0xad,0x63,0x1a,0xa0,0xac,0x4c,0x9a,0x61,0x38,0xf9,0x36,0xb1,0x67,0xd0,0xe5, 0xc1,0xa3,0xac,0xbf,0xab,0x59,0x16,0x66,0x35,0xca,0x3f,0xb6,0x47,0xbd,0x58,0xe7, 0x6c,0x3b,0x3,0x8c,0xe8,0xce,0x28,0x4a,0x8,0xa1,0x0,0x39,0x9,0x51,0x9f,0x4a, 0x74,0x4c,0xb,0x21,0xa5,0xa0,0x7,0x5a,0xea,0xc5,0x91,0x32,0x84,0x69,0x1a,0x70, 0xa5,0x9c,0xfc,0xe,0x6c,0xa4,0xd7,0x74,0xc5,0xd7,0x2d,0x4e,0x29,0xcc,0x99,0x9e, 0x99,0xa4,0x3f,0xbe,0xc4,0xc5,0x1a,0xaf,0x8b,0xab,0xe1,0x10,0x15,0xfb,0x0,0x3a, 0x99,0x7d,0xc7,0x6,0x22,0x9f,0xf9,0xe8,0xf7,0xa6,0xb6,0xa0,0x74,0x50,0x3f,0xe, 0x74,0xfd,0xcc,0x39,0xc3,0x66,0xe8,0x50,0x91,0xca,0xdf,0x27,0x47,0x60,0x61,0xe0, 0xdd,0x2a,0x66,0x0,0x49,0xdf,0x68,0x41,0x86,0x20,0xe2,0xfa,0x70,0xa1,0x88,0x65, 0xa0,0xd5,0x9e,0xe3,0x3c,0x88,0xb3,0xce,0x53,0x94,0xf5,0x1a,0xf4,0xd6,0xfa,0x52, 0x80,0xe0,0x52,0xca,0xc0,0x3b,0x8b,0x48,0xda,0x6e,0xc2,0xca,0x90,0x4c,0x30,0xb0, 0xa1,0xcf,0x94,0xdd,0x58,0x49,0x2c,0x2b,0x5d,0x22,0x46,0xd1,0x79,0xc0,0x24,0xf9, 0xa2,0xf5,0xc4,0xe2,0x31,0xd0,0xaa,0xc,0xbe,0x6e,0x57,0x4f,0x3a,0x87,0x0,0x5b, 0x57,0x15,0x39,0x2f,0x5e,0x66,0x5b,0x3b,0x8,0xa1,0x8c,0x81,0x62,0xb0,0x7c,0x84, 0xa6,0xc0,0xe7,0x58,0x11,0x92,0xe3,0xd0,0x80,0x3b,0x20,0x3a,0x43,0xa0,0x95,0x9a, 0x35,0x4f,0xca,0x13,0xb5,0x26,0x4e,0xbd,0x47,0xda,0xbf,0x29,0xb,0xbb,0x2e,0x31, 0xfb,0x16,0x89,0xe,0xa8,0xed,0xde,0xa9,0xa8,0x7e,0xe3,0xeb,0x9e,0xf9,0x87,0xd3, 0x49,0xd1,0xe6,0xfe,0x77,0xb4,0x3c,0x3e,0x8f,0x7b,0x67,0x1a,0x37,0x15,0x4c,0x34, 0x2b,0x55,0x42,0x54,0x43,0xa0,0x7d,0xec,0x1f,0xe0,0x58,0xbe,0xda,0x5f,0x12,0x24, 0x31,0xf9,0xa2,0x28,0x2e,0x5f,0x66,0x3e,0x5a,0x4e,0x58,0x92,0x63,0xa4,0x46,0xf, 0x7a,0x8,0xe2,0xbd,0xa8,0x60,0x2a,0x47,0x41,0x83,0x85,0x1d,0x62,0x98,0xc0,0x14, 0x12,0xe3,0x3c,0x40,0xc2,0x23,0xfd,0x1d,0x71,0x57,0x2f,0x54,0x7b,0x75,0xe2,0xf5, 0x7d,0xc5,0x34,0xa5,0x26,0x5e,0xed,0xe7,0x61,0x73,0x84,0xc4,0x8b,0xc4,0xd8,0x1d, 0xa8,0x94,0x5e,0x6b,0xb7,0x5c,0x9,0xa8,0x33,0x38,0xfd,0xaf,0xae,0xe0,0x25,0xab, 0x27,0x59,0xd1,0xcc,0x38,0xbf,0xb4,0x99,0xb2,0xb8,0xdd,0xbe,0x7e,0x36,0xdb,0xa6, 0xcb,0xb9,0x92,0x3,0x96,0x9b,0xac,0xc9,0xd3,0x2a,0xf8,0x2,0x8a,0x1f,0xae,0xb1, 0xf7,0x0,0xfe,0x30,0xbf,0x33,0xca,0xf1,0xec,0x28,0x30,0xea,0xde,0xd,0x91,0x2a, 0x46,0x24,0x2d,0xdc,0xbf,0x59,0x27,0x14,0x83,0x9f,0x16,0x8e,0x3e,0x44,0xbf,0x37, 0x44,0xbe,0x67,0x83,0xf2,0xb1,0x76,0x5f,0x5a,0xa6,0x4a,0x39,0x33,0xdb,0x63,0x7a, 0x1,0x90,0xd6,0x40,0x6a,0xfd,0x54,0xed,0x9e,0x6b,0x7c,0x5c,0xaf,0x3d,0x93,0x74, 0x7b,0x7b,0xf7,0x6e,0xac,0xed,0x4d,0x7,0x95,0x97,0xbf,0x48,0x74,0x23,0xc2,0xf4, 0x34,0x9a,0xb4,0x9e,0x18,0xa,0xc,0x36,0xf4,0x9,0x93,0xa4,0xc5,0xa6,0x98,0x41, 0xa1,0x91,0x30,0x4f,0x7f,0x7d,0xd5,0x94,0x95,0x96,0xdd,0x89,0xb9,0x20,0x7e,0x6d, 0x3a,0x33,0xc,0x53,0xbc,0x98,0x9,0xb1,0xa1,0x1c,0xd6,0x67,0xc3,0x6f,0x28,0x65, 0x1,0xd7,0x34,0x1,0x56,0xb,0x95,0x6b,0xa1,0xf2,0xf4,0xda,0x93,0xf2,0x49,0xcd, 0x26,0xd4,0xa0,0x63,0xec,0xaa,0x15,0x8e,0xc6,0xeb,0x75,0xa,0xdb,0x1e,0xef,0xdc, 0xf5,0x24,0x5d,0xcb,0xae,0x73,0x37,0xcf,0x66,0x2c,0xab,0xf9,0x1f,0x74,0x48,0xc5, 0xc8,0xe8,0xa8,0xb6,0x93,0xbd,0xc4,0xda,0x2a,0xba,0xe4,0x6,0xd8,0xd4,0x62,0x4e, 0xf9,0x40,0x1b,0x28,0xb3,0xd1,0xf8,0x99,0x7e,0x24,0x94,0x9d,0x18,0x5c,0xe2,0xe0, 0x45,0xb,0x17,0x59,0xc9,0x5c,0x34,0x73,0x17,0x19,0xf8,0x6f,0xee,0x5b,0xbd,0x68, 0x1b,0xd8,0x90,0xce,0xab,0x9,0x69,0xa9,0x2d,0x7d,0xc6,0x45,0xd9,0xaa,0xa6,0x1f, 0xb5,0x3d,0x78,0xfe,0x99,0xac,0xf1,0x30,0x46,0xea,0x9f,0xb4,0xc6,0x5e,0x1d,0xe1, 0xb6,0x2d,0xb1,0xe1,0xb6,0x9a,0x8b,0xe3,0x18,0x53,0xa9,0xf1,0x7d,0xcf,0x90,0xb2, 0xd,0xa,0xb2,0x27,0x36,0x24,0x57,0x7c,0x10,0xf7,0xb0,0xd6,0xd5,0xcd,0x38,0x8c, 0x7b,0x69,0x6f,0x32,0x4,0xfa,0x95,0x1c,0xcd,0xbe,0x8d,0x4b,0x8e,0x1f,0xfe,0x1c, 0xa8,0xb1,0x43,0x5e,0x55,0x1a,0x5b,0x65,0x91,0xc,0xbb,0x67,0x5a,0x74,0xf4,0xd5, 0xdd,0xe3,0x87,0xe2,0x5e,0x9c,0x7e,0x2d,0x5c,0x8c,0x78,0x6a,0xab,0x77,0x6,0xd3, 0xa8,0x49,0x32,0xfe,0xe3,0x8d,0xe3,0x75,0x9a,0xa0,0x5d,0xf4,0x15,0xd1,0x4a,0x72, 0xb5,0x51,0xd4,0x93,0xed,0x54,0xc0,0xc9,0xe0,0xb9,0xb4,0xc,0xb0,0xba,0x5f,0x5a, 0x84,0x91,0xd8,0x68,0x9f,0xbc,0x5d,0x3a,0xdc,0xba,0xae,0x71,0x8c,0xf8,0x64,0xc1, 0xc9,0x39,0x56,0x37,0x8d,0x96,0x81,0xed,0x50,0x36,0x79,0x2,0x70,0xd8,0xdb,0xf4, 0x6b,0x34,0xdc,0xb,0xf0,0xba,0xc4,0x4e,0x75,0x73,0x3f,0x82,0xeb,0xa3,0xc3,0xb5, 0xdd,0x99,0xec,0xea,0x31,0x6e,0xd9,0x1,0x24,0x53,0x82,0x95,0xac,0xdd,0xa,0x18, 0x12,0xe7,0xa2,0x83,0xa2,0x67,0x51,0x97,0x5a,0x90,0x99,0x46,0xb4,0xdd,0xfb,0x92, 0x77,0x68,0x7d,0x28,0xd7,0xd6,0xa9,0xfb,0xaa,0xab,0x11,0x57,0x8a,0x1c,0xee,0x1c, 0x83,0x11,0x9f,0x26,0x78,0xf0,0x3d,0x52,0x2,0x57,0x98,0xb6,0x35,0x14,0xc8,0xac, 0xfb,0xc5,0x55,0xd3,0x9d,0xfe,0x50,0xc7,0xaa,0x61,0x9e,0xb4,0xfc,0xd,0xd1,0x80, 0x1e,0xf0,0x26,0x16,0xe2,0xe3,0x68,0x64,0x3b,0x80,0x1b,0xef,0x14,0x63,0x9c,0x10, 0x29,0x71,0x64,0x46,0xef,0x34,0x8d,0x1b,0x15,0x2c,0xcf,0x13,0xb8,0x21,0x93,0xd6, 0x13,0x3a,0x6c,0x75,0x1e,0xd4,0xd9,0x59,0xd4,0x74,0x49,0x68,0xd7,0x65,0xf8,0x1, 0x57,0x5d,0xc7,0x47,0x11,0x55,0x62,0x26,0x82,0x33,0xb8,0x3b,0x54,0xcc,0x92,0xe6, 0x7,0xfe,0x5c,0x25,0x54,0x36,0xfd,0xa8,0x2a,0xc6,0x12,0x2,0xab,0xb,0x83,0x3, 0xe7,0x4b,0x4b,0xf8,0xa0,0xad,0x9e,0xa2,0x60,0x58,0x5e,0x35,0xa4,0xf0,0x1c,0xab, 0x6f,0x79,0x50,0xc3,0x2f,0xcd,0x6d,0x5a,0x94,0xfe,0xdb,0x40,0xa,0x5f,0x44,0x71, 0x2a,0xf,0x6a,0xcb,0x3c,0x88,0x6e,0x9d,0x60,0xcc,0x52,0x5,0x3d,0x6e,0x30,0xad, 0x67,0x80,0xf0,0x17,0xcd,0x5e,0xf0,0x62,0x5d,0xcc,0x23,0xe6,0xac,0xe6,0x58,0xd6, 0xf5,0x42,0xa2,0x32,0x4b,0x91,0x4f,0xab,0xdd,0xa1,0x31,0x9b,0x90,0x61,0x49,0x77, 0x62,0x3a,0x8e,0x30,0x19,0xfe,0x13,0xf5,0xcc,0x36,0x5d,0x79,0x1d,0xb5,0x50,0x13, 0x78,0x73,0xc4,0xc3,0x84,0x94,0xee,0x62,0x36,0x20,0xfd,0x46,0x2,0xc6,0xbe,0x64, 0x2,0xcc,0x14,0x9a,0x4c,0x27,0x90,0x19,0x5d,0xed,0x12,0xf9,0x24,0xe1,0x8c,0x1c, 0xd4,0x52,0x5f,0x59,0xe6,0x4e,0xbc,0x9c,0xee,0x3a,0xe3,0xf0,0x2,0x22,0xd4,0x83, 0x6e,0xe8,0x9d,0xba,0x90,0x2e,0x53,0x6d,0x9c,0xe4,0x68,0x40,0xc7,0xf4,0x5c,0x9c, 0xc6,0xbb,0xf6,0xad,0x89,0x33,0xca,0x78,0x6d,0x2e,0x69,0xee,0xcf,0x3e,0xf1,0x3e, 0xa7,0x8f,0x79,0x38,0x3e,0x4c,0xa5,0xda,0x32,0xe,0x1b,0xf9,0x83,0xf6,0x16,0x4a, 0xb2,0xd,0x78,0xbb,0xbf,0x43,0x35,0xad,0x71,0x9e,0x1c,0x41,0x5d,0xf,0xfe,0x84, 0x9e,0xf7,0x3c,0x5c,0x45,0xe1,0x37,0x77,0x70,0xd1,0xf0,0x73,0x48,0x7,0xbd,0x7a, 0x94,0x36,0x37,0xd3,0xf8,0x6c,0x81,0x6a,0x8a,0x9e,0xab,0x67,0xad,0x2b,0xeb,0xcb, 0x23,0x28,0x29,0x68,0x8a,0xdf,0x5f,0x7a,0x32,0x50,0xed,0x7a,0xd7,0x2b,0xf5,0xeb, 0xe1,0x2d,0xbf,0xda,0x19,0x42,0x46,0xa3,0x60,0x71,0xc,0x8d,0x9c,0x77,0x59,0x40, 0x20,0x2,0xa8,0x2a,0x62,0x88,0x24,0x94,0xd8,0x91,0x8e,0x30,0xbc,0x4,0x1c,0x1e, 0x31,0xdc,0xf9,0xc9,0x9e,0xbf,0x6e,0xfe,0xb0,0xf9,0x8c,0xcd,0xf0,0x65,0xe,0x90, 0xe7,0x36,0xba,0x4a,0xbe,0xde,0x5e,0x18,0xef,0xec,0x48,0x2d,0x71,0xe4,0x4b,0x22, 0xc1,0xc4,0xec,0xdf,0x84,0x5b,0xde,0xb5,0xd4,0x6b,0x83,0xc5,0x50,0x91,0x57,0x38, 0xc7,0x91,0x2,0x87,0xf0,0x60,0x9f,0xe0,0xcd,0x67,0xe,0x3f,0x4c,0xd9,0x61,0x8d, 0x9e,0x4e,0x6d,0xa3,0x29,0x4c,0x59,0x7d,0x37,0xdc,0xc3,0x88,0xed,0x1b,0xc0,0x35, 0x2c,0x43,0x3c,0x1d,0xa3,0xdb,0x7e,0xf0,0xc3,0xc,0xaf,0x10,0xe5,0x12,0x9e,0x5, 0xdf,0xc,0xa8,0x89,0x59,0x81,0x7,0x10,0xdd,0xca,0x98,0xcb,0x65,0xd9,0x80,0x12, 0x1d,0xbd,0xae,0x40,0x99,0x2d,0x32,0xdc,0xb9,0xe1,0xed,0x1f,0x73,0x8c,0x24,0xd3, 0x18,0x4c,0xdc,0xf0,0xcd,0xe3,0x2,0xab,0x2f,0x9a,0xf6,0x14,0xf3,0x78,0x26,0x90, 0x36,0x55,0xd1,0x4f,0x2,0x83,0x2d,0xbb,0xe4,0x1b,0xdb,0xd8,0x27,0x7f,0x2c,0x3f, 0xcc,0x9,0x31,0x9a,0x6c,0xb2,0xc6,0x9b,0xcc,0xbd,0x30,0xc1,0x36,0xd5,0x52,0x6c, 0x2b,0xa3,0xbc,0x2e,0xa6,0x69,0x69,0x8c,0x84,0xc4,0xe4,0xab,0x45,0x11,0x6a,0x91, 0x1a,0x1b,0x2c,0x86,0xcd,0xf2,0xa2,0x9b,0x31,0x52,0xdc,0x67,0x28,0xae,0x54,0xd3, 0xd2,0x90,0x81,0x79,0xf9,0xea,0x85,0x7e,0xb0,0x6a,0xa9,0x75,0xfa,0x93,0x7,0x15, 0xaf,0xb2,0x1c,0xfc,0x26,0x3e,0x18,0x57,0x90,0xf4,0x3e,0x38,0x24,0x92,0x8b,0xf6, 0xa2,0xd,0x70,0x9c,0x78,0xf6,0x9a,0xa8,0xe0,0xc3,0x1e,0xdc,0xd7,0xa4,0x71,0x7, 0x57,0x8d,0x4,0x7d,0x4b,0x1d,0x54,0x5b,0x91,0x93,0x94,0xb5,0xa5,0x20,0x2c,0xc8, 0xad,0x9d,0x65,0x26,0x14,0x80,0xce,0x74,0xc3,0xec,0x51,0x9b,0x11,0xc3,0xa2,0x68, 0xd0,0x27,0x66,0x9c,0xc3,0xba,0xf7,0x55,0xcd,0xc,0x8b,0xf3,0x2d,0xb7,0xbc,0x5a, 0xd4,0xa1,0x80,0x68,0x22,0x4f,0xdd,0x66,0xbb,0x2f,0x2,0xcc,0x72,0x25,0xb4,0xc3, 0x4c,0x1b,0x60,0x8f,0xd6,0x58,0x64,0x24,0x65,0xef,0x18,0x12,0x28,0xd4,0x6c,0xfc, 0x77,0x6c,0x66,0x19,0x3b,0xc3,0x7f,0xf6,0xf2,0x2,0x43,0xe5,0xa6,0xf7,0x29,0xf2, 0x14,0x89,0x2,0x6a,0x61,0x66,0xe,0x46,0xd6,0x27,0xd7,0xfe,0xfb,0xc3,0x7b,0xf2, 0x30,0x61,0x8c,0x6b,0x25,0x8b,0xe1,0x98,0x8d,0x25,0xfd,0x34,0x9d,0x27,0xa6,0xb1, 0x30,0xa8,0x9b,0x91,0x8f,0xa9,0x58,0x66,0x50,0x30,0x65,0xcc,0xf4,0x60,0xbf,0x25, 0xc2,0xcb,0x11,0xe7,0x58,0xf2,0x0,0xe5,0x98,0xfd,0x9a,0x36,0x25,0xc0,0x67,0x55, 0xe9,0x3,0x67,0x79,0x2c,0xbf,0xdf,0xfc,0xef,0xc4,0xc9,0xe4,0x25,0x9,0x8a,0xe7, 0xd5,0x1b,0x50,0x2e,0xe,0xcf,0x93,0xa6,0xce,0xad,0x5c,0x73,0x6f,0xc3,0xc9,0xd8, 0x46,0xb0,0x52,0x73,0x70,0xb1,0x70,0xdf,0xf5,0xb9,0xc5,0x1b,0xc2,0xcf,0x83,0x98, 0x6a,0x53,0x46,0x78,0x23,0xda,0x9f,0x71,0x8,0xfb,0xe5,0x77,0xc0,0x2f,0xcf,0x7, 0xdf,0xa1,0xf9,0xcf,0x53,0xe9,0xaf,0x49,0xa3,0xf4,0xe4,0x67,0xc4,0x68,0x7f,0xae, 0x3b,0xc6,0x28,0xdd,0x21,0x47,0x50,0x29,0xc2,0x36,0x21,0x3,0xe4,0xf0,0xb,0xc4, 0x93,0x84,0x14,0x66,0xee,0xc3,0x30,0x92,0xb9,0x15,0x79,0xfd,0xfc,0xf9,0xad,0xb7, 0x40,0x55,0x95,0x61,0x9c,0xe5,0xa,0xde,0x9b,0x2b,0xe2,0x80,0x9c,0x6d,0xc4,0xaf, 0xf1,0xd8,0x95,0xe0,0x9d,0xc5,0xf3,0xd6,0x5a,0x6d,0xd4,0x57,0xe6,0x2,0x8e,0x27, 0x57,0x25,0x8,0x73,0xb,0x13,0x53,0x27,0xbd,0x36,0xa7,0xd9,0x23,0xec,0x89,0x15, 0xc5,0x9f,0x76,0xe2,0x65,0xe9,0x39,0xc0,0xd6,0x8e,0x97,0xbe,0x90,0x27,0x65,0xe8, 0xcb,0x6e,0xdb,0x56,0x1,0xae,0x7d,0xbe,0x64,0xa5,0x19,0x87,0x92,0xa2,0x1d,0xd7, 0x42,0x13,0x3b,0x28,0xfc,0x74,0x68,0xd3,0x3,0x0,0x92,0x14,0xa6,0xf8,0x7c,0x72, 0xe6,0x58,0x49,0xe7,0x8,0xc6,0x26,0x6c,0xeb,0x3f,0xf4,0x7e,0x62,0x91,0xd6,0xa4, 0xa4,0x91,0x4c,0xa1,0x6,0xb4,0xf4,0x89,0x35,0x88,0x9d,0x5b,0x1,0x1a,0xce,0x67, 0xf1,0x18,0x4f,0x79,0x5e,0x75,0x66,0x4b,0xb5,0xda,0x49,0x18,0x6c,0x9f,0x3c,0x11, 0x31,0x89,0xb2,0xb7,0xbd,0x27,0xc0,0xf2,0xaf,0x5e,0xce,0x30,0xf7,0x9d,0x97,0x69, 0x35,0x66,0xe3,0x13,0xdc,0x4a,0xdd,0x12,0x25,0x28,0x2a,0x91,0xc7,0xe5,0x22,0xf9, 0xee,0x54,0x31,0xad,0x7b,0xf1,0x20,0xab,0xcf,0xee,0x5b,0xc7,0xc,0xf3,0xb0,0xc0, 0x5a,0x14,0x54,0xb6,0x5e,0x32,0xc8,0x3,0xd9,0x72,0x14,0xa2,0x59,0x36,0x1c,0x48, 0xa,0xcc,0x75,0x86,0xbe,0x16,0x32,0x8e,0x84,0x8d,0xd5,0x91,0x1,0x86,0xd1,0xdb, 0x9b,0x26,0x12,0x79,0xd8,0xdb,0xfc,0xb2,0xcd,0x11,0xd4,0xa6,0xc7,0xf0,0xef,0x51, 0xbd,0xe4,0xd7,0xfb,0xfa,0x89,0x8a,0x0,0x97,0x60,0x11,0x98,0x67,0xe2,0xf3,0x82, 0x89,0x7,0xfb,0x62,0x62,0x78,0x94,0xaf,0x8a,0x6a,0x57,0xd1,0xda,0xc6,0x23,0x19, 0xab,0x7b,0x15,0x27,0x5,0x20,0x27,0x1c,0x0,0x38,0xb5,0x67,0x9a,0x29,0xe9,0xa3, 0xaf,0x66,0x6,0x91,0xde,0x9b,0x42,0xe8,0x85,0x99,0x3a,0x60,0x60,0x5e,0x79,0x8b, 0x59,0xf,0x32,0xdd,0x2f,0xd8,0xfa,0x2f,0x90,0x30,0x97,0x2c,0x59,0x1,0xcf,0xa, 0xe6,0x56,0x1b,0x46,0x71,0x5d,0x2f,0xf6,0xf6,0x6a,0xd6,0xd6,0x48,0xd0,0xe2,0x21, 0xdf,0x15,0xfe,0xf,0xee,0xf9,0x3e,0xfe,0x2a,0x55,0x2b,0x84,0xd6,0x7b,0xe,0xbd, 0x51,0x29,0x4,0x42,0x7,0xb3,0xb8,0x7d,0x9d,0x8f,0x55,0x65,0x60,0xb7,0x86,0x40, 0xcc,0x85,0xce,0x3b,0x80,0x8d,0x3b,0xaa,0xe2,0xe5,0xae,0x39,0xe0,0x3c,0xf7,0x32, 0xe5,0x7b,0x74,0xec,0x2f,0x2d,0x6a,0x4c,0x3d,0x3f,0xb1,0x9d,0xf6,0x38,0x5e,0x44, 0xbe,0x2d,0x7f,0xbe,0xba,0x3a,0xe8,0x1e,0x21,0x98,0x57,0x2,0x54,0xce,0xb4,0x3a, 0xca,0xa8,0x27,0xf9,0xd6,0x12,0xc6,0x14,0x51,0x78,0x31,0x49,0xb1,0xf,0xd,0xef, 0xbc,0x8c,0x2e,0x77,0xc7,0x17,0x15,0x68,0x2f,0xec,0xe9,0x84,0xbb,0x9e,0x3e,0x86, 0x48,0xe5,0x1,0x9e,0x77,0x47,0x32,0xc8,0xbf,0xe2,0x91,0xf0,0xf2,0x9e,0x60,0xaf, 0xab,0x8e,0xa6,0xf2,0x26,0xbc,0x5b,0x55,0x29,0xc4,0x59,0x64,0xe3,0x18,0x6b,0x2c, 0xfd,0x6c,0x4a,0x75,0xb3,0xfb,0xbd,0xf2,0xde,0x50,0xe4,0xd1,0x6e,0xc4,0x1,0x1a, 0x54,0xa8,0x8c,0x7a,0xe4,0xe7,0x4f,0x8d,0x2d,0xa9,0xf1,0x11,0x41,0x5d,0xbc,0x3f, 0x49,0x7,0x34,0x7c,0x3,0x71,0x70,0x61,0x41,0xd4,0xb3,0xb0,0x99,0xb4,0x4a,0x6d, 0xdc,0xd7,0x67,0x41,0x3f,0xb7,0xce,0x6c,0xe0,0xc1,0x7d,0xa1,0x1f,0xb9,0xe0,0x69, 0xc0,0x94,0xe5,0x43,0x6,0x56,0x25,0x48,0xaa,0xd8,0x78,0xc4,0x8d,0xc2,0x32,0xea, 0x1a,0x1a,0x2c,0x5a,0xd1,0xfb,0xc6,0x32,0xbd,0xc4,0xd3,0xdc,0x7e,0x34,0xc5,0xbf, 0x48,0xac,0x82,0xcd,0x82,0xa7,0x95,0x2e,0x80,0xe,0xf2,0x8e,0x51,0xa4,0xf8,0x6b, 0xbe,0x25,0xc5,0x10,0x21,0xd,0xc1,0x5e,0xd1,0x15,0xbb,0xcf,0xc8,0x81,0x8f,0x11, 0xad,0x92,0xdf,0x31,0x3a,0xf4,0xde,0x3b,0x4,0x51,0x49,0x55,0x75,0x42,0xc0,0x35, 0x67,0x7,0xc4,0x9,0x14,0x87,0xe6,0x65,0x1c,0xa2,0x35,0xe5,0xa4,0x45,0x76,0x52, 0xd7,0xd5,0x3,0x12,0xcb,0x61,0xcc,0xcf,0xb2,0x16,0xa4,0x29,0x58,0xe4,0xdd,0x40, 0xeb,0x22,0xc8,0x0,0xa9,0xaf,0x65,0x46,0xd2,0x1b,0x2c,0xf6,0x60,0xa2,0x49,0x38, 0x79,0xcc,0x4a,0x45,0x2e,0x18,0x94,0x61,0xad,0x39,0xa,0x7,0x1e,0xe7,0xc6,0x8a, 0xa,0xf,0x8a,0x34,0x3e,0x70,0x7a,0x11,0x8b,0x26,0x87,0x6b,0x48,0xd1,0xa3,0xc1, 0x1e,0xed,0x86,0x4c,0x85,0x9a,0x2d,0x34,0xd3,0x37,0xba,0x72,0x1f,0x1,0xfc,0xa9, 0x10,0x7,0x5d,0x4e,0xf6,0x57,0xdf,0x2,0x7d,0x67,0x6d,0x45,0xb8,0x11,0x8,0xd6, 0x7f,0xe,0xa3,0x84,0xa9,0xd0,0x38,0xfc,0x9,0xf2,0xee,0xa7,0xf3,0x6b,0xd0,0x83, 0xf2,0x2e,0xd2,0xe9,0x85,0x32,0x6c,0x82,0x99,0xd9,0xc8,0xd2,0x6b,0x50,0xa9,0x6a, 0xdd,0xcc,0xee,0x7,0x9e,0x28,0x5,0x27,0x9a,0x73,0x4e,0xf,0xdf,0x20,0x92,0xd2, 0x4e,0xe4,0x3c,0x54,0x17,0xa8,0x56,0x31,0x3,0x9e,0x4,0xed,0x6e,0x2d,0x58,0x4d, 0x7a,0xc6,0x54,0x98,0x6e,0xd8,0xbf,0xa,0x4d,0xe,0x98,0x2d,0xad,0xaa,0x7f,0xfc, 0x90,0xbb,0xd0,0x27,0xe4,0x27,0x58,0x67,0x46,0xdb,0x55,0xb4,0x89,0x2d,0x81,0x4, 0xf3,0xd6,0x9c,0xe2,0x2f,0xdb,0xec,0x7c,0x69,0x5,0x29,0x18,0xaf,0xa8,0x94,0xbf, 0xe4,0x65,0xe7,0xc9,0xc,0xbf,0x31,0xd1,0x1c,0x6,0x87,0xa5,0x33,0x9,0x29,0xa6, 0x5f,0x45,0x89,0x8f,0x21,0xf5,0xc,0xa,0xfa,0xb5,0x22,0x2b,0x5e,0x36,0xea,0xc2, 0x9b,0x52,0x8c,0x28,0x13,0x3d,0xf9,0xae,0x43,0x1,0xd3,0xf5,0xb,0xfc,0x9d,0xe9, 0x42,0x27,0x79,0xe2,0x1e,0x6,0x6c,0x98,0xbb,0xf,0xc3,0x99,0x45,0xaf,0x5d,0x61, 0x81,0x69,0x9,0x94,0x27,0x3,0xc2,0x6a,0x5,0x96,0xe0,0x8f,0x93,0x7e,0xf8,0x55, 0xa5,0x73,0xb7,0x43,0xf8,0x25,0xdc,0x34,0xb3,0x20,0x4d,0xf8,0xcf,0x2a,0x5a,0x52, 0x94,0x63,0x66,0xbb,0xe6,0xa9,0xa5,0x6b,0x40,0x86,0x7a,0x54,0x84,0x73,0xa9,0xaa, 0x66,0xe1,0xed,0xde,0x86,0x4a,0x13,0x3a,0x6b,0x61,0x33,0xba,0xb,0xe,0x8c,0x9f, 0xf0,0x73,0xda,0x57,0x1d,0x1,0xc2,0x5d,0x7,0xbc,0xb1,0x8c,0x31,0xdb,0x37,0x17, 0x3d,0xa4,0xf6,0xc3,0x6f,0x89,0x7d,0x5a,0x6a,0x30,0x15,0x76,0x3e,0x22,0x16,0xaf, 0x95,0x71,0x86,0xb2,0x72,0xc9,0x8f,0x79,0x86,0xc1,0x85,0x37,0x1d,0x3c,0x4f,0x5a, 0xe1,0xc5,0x9d,0xd0,0x4f,0x1b,0x2b,0xba,0x4b,0xbf,0x31,0xa,0xe1,0xc6,0x39,0xf6, 0xb7,0xbf,0x29,0x2a,0x89,0xb9,0x24,0x90,0xfa,0xa9,0xc7,0x18,0xe6,0x96,0xf1,0x48, 0xdb,0xf,0x98,0x2c,0xa9,0xc3,0x66,0xf4,0x83,0x17,0x7e,0xe5,0x5d,0xb7,0xdc,0x16, 0xf7,0x7,0x40,0x1,0x40,0xe3,0x91,0x3b,0x8e,0xd9,0xd2,0xf4,0xef,0x44,0x3d,0xcc, 0x53,0xd5,0x78,0x7c,0x19,0x5e,0x71,0x1c,0x75,0x70,0x2,0xd2,0xa7,0x5f,0xe8,0x9f, 0x66,0xa9,0x21,0xa6,0x8d,0x32,0x61,0x9b,0xc,0x34,0x90,0x7c,0xf7,0x4d,0xc8,0xca, 0xa2,0x41,0x47,0xbb,0x9f,0x38,0x58,0x15,0xa8,0x5a,0x67,0x51,0x39,0xd0,0x70,0x9f, 0x7a,0x91,0xc5,0x87,0xc4,0x27,0x24,0x50,0xda,0xb4,0xcc,0xd2,0x82,0x95,0x9d,0x25, 0x56,0xe4,0x61,0xf5,0x1e,0xb9,0x8a,0x46,0x93,0x72,0x97,0xcd,0x43,0x88,0xec,0xbd, 0x1a,0xb3,0xc4,0x5e,0xda,0xe8,0x2f,0xb6,0x1e,0x7b,0x9,0x20,0x91,0xa7,0x45,0xe7, 0xc,0x26,0x5e,0xa9,0x5f,0x68,0xf0,0x73,0xda,0x8,0xc0,0x9d,0x90,0xad,0x5b,0x2b, 0xe0,0xa0,0x9,0x3c,0x89,0x38,0x72,0x27,0xb4,0x7b,0x47,0x46,0xa2,0xd,0xad,0xaf, 0x33,0xc,0xd8,0x13,0xf4,0xc9,0x86,0xcf,0xd2,0x47,0x6e,0xe2,0x74,0x49,0xe,0xd5, 0xe9,0x97,0x12,0xf3,0xcf,0x84,0x1b,0x4,0x0,0xe2,0xc9,0xa3,0xef,0x78,0xd2,0x23, 0x4,0xab,0x36,0xf8,0xf5,0x3c,0x49,0x48,0x3,0x37,0x2b,0x78,0x0,0xb9,0xcd,0x6a, 0x51,0xdf,0x5e,0xa0,0x64,0xf8,0xa5,0xe3,0xdb,0x6f,0x7,0xcb,0x67,0xd9,0x6f,0x6c, 0x6,0xa5,0xe4,0xfb,0x62,0x2e,0x44,0x65,0xe4,0xee,0x5d,0xe5,0xa8,0x2b,0x50,0xf9, 0xb,0x2e,0x1b,0xee,0x27,0xc0,0x53,0x4,0xaf,0x5a,0x4f,0x18,0xb4,0xbe,0x4,0xba, 0xe4,0xe8,0x36,0x47,0x97,0x7a,0xac,0xfb,0xe8,0x8a,0xe1,0x92,0xb5,0xb1,0xc,0x41, 0xdf,0x27,0x30,0x8,0xe7,0x83,0x8b,0x18,0x5e,0xda,0x30,0x13,0x9a,0xb3,0x4d,0x7f, 0x1c,0x83,0x46,0xb3,0x7d,0x72,0x30,0x66,0xfc,0x12,0x78,0xb3,0x44,0x85,0xf4,0x24, 0xac,0xa4,0x2c,0x15,0xa8,0xb7,0x2d,0x7,0x13,0xdc,0x1a,0xad,0x90,0xe6,0xac,0x2c, 0x6a,0xf2,0xe0,0x67,0x65,0x90,0xcd,0x63,0x22,0x47,0x96,0x66,0x4c,0xb,0x8b,0x78, 0x2f,0x37,0x8d,0xd7,0xef,0x3a,0x5e,0x82,0x96,0xf7,0x30,0xa6,0xde,0xdc,0xd3,0x49, 0x4f,0x34,0x30,0x34,0xc4,0xfe,0x97,0xe6,0xc5,0xad,0x4e,0x91,0xb8,0x59,0xa,0xe8, 0x90,0x18,0x40,0x0,0x52,0x9f,0x82,0x69,0x97,0xb2,0x10,0x77,0xf,0xe3,0x40,0xdd, 0x97,0x71,0x13,0x5c,0xef,0x2a,0xc3,0x35,0xd8,0x91,0xc6,0x11,0xea,0xd0,0xf9,0x7b, 0xe8,0x3b,0xfb,0xbb,0x5a,0x7e,0x25,0xf1,0xb1,0xb4,0x69,0xc0,0x99,0x2a,0x1f,0xb0, 0x9b,0x32,0xe,0x8b,0x5c,0x51,0x40,0xb4,0xe2,0x7,0xc6,0xcd,0xd7,0xc0,0xc8,0x41, 0x7b,0xc4,0xfc,0xd5,0xc3,0xa1,0x48,0x75,0x56,0x31,0xb5,0xef,0x5b,0xd4,0x21,0xf6, 0x86,0x2f,0x2,0xe3,0x0,0x42,0x98,0xe2,0xc8,0x5f,0x30,0xa1,0xa0,0x78,0x62,0x9b, 0xbd,0x5f,0xf1,0x81,0x1,0x3a,0xf6,0x57,0xea,0xac,0xc7,0x47,0x2,0xe8,0xbd,0x88, 0x97,0x40,0xeb,0x17,0x2,0x85,0xf9,0xcb,0x64,0xa9,0xec,0x84,0xa1,0x4f,0x21,0x5f, 0x2e,0x13,0xe0,0x2f,0xcc,0x57,0x6,0xb7,0x84,0x4d,0x7e,0x86,0x36,0x3d,0x8e,0x4d, 0xfc,0x7b,0x64,0xfe,0x1,0xdd,0xca,0xe4,0x7,0x37,0x6a,0xa9,0x86,0x8b,0x9,0xb4, 0x1e,0x6a,0x63,0x6a,0x41,0xe9,0xa1,0xc5,0x37,0x21,0xcb,0xed,0xdd,0x5b,0x3b,0xda, 0xd6,0x20,0x59,0xd7,0x7d,0xa4,0x3c,0x85,0xdb,0xa6,0x2f,0xe2,0xb1,0xb7,0x97,0x4f, 0x22,0x7b,0xb9,0x64,0x65,0x5c,0xa9,0x1c,0xfc,0x76,0xa,0x5a,0xd1,0x46,0x35,0xa8, 0xe5,0x8e,0x0,0x63,0x33,0x3c,0xe8,0x8f,0x63,0x97,0x72,0x15,0x50,0x89,0x65,0xf1, 0x5,0x9e,0xd5,0xe9,0xfa,0x80,0x7,0x77,0xf6,0x11,0xd1,0x48,0xd6,0x86,0x70,0x3c, 0x95,0x70,0xa0,0xc8,0x2c,0x9,0xd7,0x8f,0x21,0x4a,0x25,0x71,0xd4,0x8a,0xe2,0x59, 0x29,0xb9,0x44,0xa4,0x3a,0xca,0x9b,0xb0,0x5b,0x6e,0x78,0xb2,0x74,0xe8,0xee,0xa, 0x59,0xf,0x53,0x5,0x98,0x2b,0x95,0xb9,0x76,0xba,0x2b,0x4b,0xc4,0xe,0x24,0x6d, 0x47,0x68,0x91,0x81,0xb2,0x2e,0xb1,0xf,0x1c,0x2a,0xc1,0x90,0x13,0x30,0x9b,0xeb, 0x40,0x6e,0xf1,0xd8,0x99,0x7,0x12,0x10,0x41,0xbc,0xda,0x6,0x4a,0x0,0x73,0x92, 0xe7,0x6,0x93,0x1b,0xb3,0xc5,0x2a,0xcf,0xef,0x6b,0xdf,0x83,0x1b,0x7b,0xee,0x5b, 0xe9,0xe0,0xb3,0x4,0x67,0x45,0x93,0xa8,0x2,0xee,0x2e,0x4d,0x6e,0xa2,0x5f,0xd5, 0x28,0xf2,0xf0,0x5b,0xb8,0x9a,0x2b,0x29,0x85,0xb,0x2c,0xa1,0x7,0x1b,0xfc,0x70, 0xfc,0x31,0xf3,0x64,0x76,0x88,0x8d,0xf8,0x77,0xbb,0x46,0x65,0xdd,0xa5,0x3b,0x85, 0x18,0x2d,0xe0,0x51,0x47,0x8b,0x7a,0xcd,0x17,0xa6,0x6f,0x1e,0xc1,0x6c,0xe,0x3e, 0x1d,0x3,0x23,0x14,0xb,0xb0,0xd,0x2,0xeb,0x53,0x67,0xca,0x78,0xa2,0x50,0x10, 0x4f,0xb1,0x61,0x97,0x3d,0xdb,0x65,0x54,0x2,0xd4,0xf1,0x44,0xc0,0x80,0x82,0x5e, 0x83,0x25,0x72,0xe,0xd5,0x7f,0x10,0xc2,0x52,0xf6,0xd,0xca,0x99,0x5d,0xda,0x69, 0xf,0xbc,0x80,0xcc,0x98,0xe5,0x21,0x1b,0x3a,0x93,0x5f,0x7a,0x14,0xe1,0xd8,0x17, 0x8,0x4b,0x25,0x5d,0x4a,0xb4,0x9f,0x9c,0xab,0xac,0xe6,0xc4,0x8a,0x42,0x2e,0x19, 0xfe,0xae,0xe5,0x17,0x14,0x87,0x32,0xcd,0x1b,0x91,0x49,0x2f,0xf3,0x22,0x46,0x7b, 0xed,0xea,0x58,0xb7,0x9f,0xf8,0xd4,0xca,0x25,0xbb,0x8f,0xaf,0x7d,0x3e,0xc9,0xfb, 0xec,0x2f,0x14,0x81,0xb6,0xc5,0x4f,0xd1,0xd7,0x98,0x80,0x4b,0x3b,0x46,0x46,0xa8, 0xb0,0x9e,0x60,0x50,0x97,0xb4,0x9a,0xbd,0xf0,0x2b,0xec,0x6e,0x69,0x36,0xea,0xd5, 0x66,0x7e,0xd6,0x1d,0xc3,0x27,0x6f,0x9b,0x3f,0x6f,0x66,0x7a,0x36,0xac,0xa2,0xe6, 0x4c,0x83,0xb7,0xe3,0x38,0x52,0x21,0x29,0xfc,0xf,0x18,0xe5,0x45,0x3,0xbc,0x2b, 0x1,0x13,0xc8,0xc4,0x3a,0x38,0x61,0x7a,0x27,0x47,0x74,0x5d,0xf4,0x97,0x45,0x41, 0x1b,0xfc,0xa4,0xd2,0xce,0x46,0xfc,0xcc,0xd4,0x94,0xb2,0x1a,0x17,0xee,0x46,0x18, 0x3,0xf,0xdc,0x3d,0xc6,0xbd,0x37,0x6d,0x6,0x2c,0xcb,0x7a,0xc3,0x90,0x3b,0xde, 0xd,0x5f,0xb1,0xdb,0xa5,0x2e,0xa8,0x7a,0x42,0xdb,0x15,0x59,0xca,0x5b,0xf0,0xcd, 0xe9,0x4e,0x8b,0x30,0xc,0x42,0x9d,0x91,0x6e,0xe8,0x8b,0x32,0xf8,0xc6,0x90,0x6, 0x27,0xc2,0x62,0x4c,0xf0,0x8a,0xc7,0xb3,0x66,0xdc,0xd,0xb1,0xb7,0x7e,0x7f,0x21, 0xcc,0x8a,0xd0,0x58,0xcd,0xed,0x6a,0x3c,0xd7,0xf5,0xee,0x50,0x3d,0x7f,0x57,0xe3, 0x42,0x39,0x30,0xb3,0xc3,0xf7,0x67,0xaa,0x54,0xf3,0x5c,0x8b,0x72,0x5b,0xac,0xbe, 0xe6,0x7d,0x18,0x34,0x6c,0x82,0xef,0xc3,0xf7,0xde,0x14,0x35,0x5f,0xea,0x19,0xa1, 0x24,0xc9,0xd4,0x68,0xc1,0x3c,0x13,0x96,0x31,0x6f,0x22,0x23,0x4a,0x4f,0xe2,0xb0, 0xcc,0x7a,0xe4,0xb8,0x7c,0xd5,0xfb,0x74,0xb4,0x11,0x2a,0x14,0x7b,0xc2,0x36,0x20, 0x8c,0xb,0x88,0xce,0xc7,0x9b,0x65,0x78,0x8a,0x7,0x9b,0xd4,0x56,0xfd,0x86,0x24, 0x78,0xea,0x5c,0x74,0xc0,0x59,0x69,0xf5,0xe9,0x13,0x89,0xe4,0xd5,0xbf,0x5,0xe2, 0x4b,0x8d,0xb1,0x13,0x29,0x96,0x8b,0x33,0x9d,0xa6,0x9,0xf4,0xa5,0xf,0x98,0x9d, 0xf9,0xf4,0x92,0x3b,0xcd,0xfb,0x31,0x37,0xf,0xba,0x1d,0x64,0xfa,0x22,0x47,0xc5, 0xb0,0x78,0xd8,0x59,0x8e,0xe3,0xd,0xac,0xa,0x16,0xa1,0x2f,0xa4,0xb9,0x4d,0x1e, 0x2e,0xdf,0x59,0xfc,0xdb,0xa,0xb3,0x6a,0xc5,0xd0,0xce,0x40,0xf3,0x96,0x6,0x24, 0x8e,0x5e,0xfc,0x1e,0xc1,0xa,0xca,0xcb,0x9f,0xeb,0xfb,0xc3,0xa5,0x49,0xe2,0x53, 0x29,0xbb,0xcf,0x84,0xc6,0x84,0xee,0xc,0x55,0x3d,0x4c,0xc8,0x53,0x52,0x6c,0xe2, 0x30,0x6a,0x80,0xf1,0xf3,0xca,0xbd,0x94,0x36,0xb9,0x58,0x5b,0x82,0xba,0xae,0x2b, 0x77,0x7f,0xaf,0x3e,0x4,0x1e,0x4a,0xd8,0x5c,0x16,0xa2,0x2f,0x68,0x8e,0x91,0x98, 0xf8,0x12,0xa,0x6d,0x5c,0xc7,0x2,0x92,0x2,0xd9,0xed,0x84,0x95,0x1d,0xb0,0x8c, 0x9c,0xdf,0xca,0x20,0xfe,0x94,0xf8,0xda,0xaa,0x1b,0x89,0x92,0xaa,0x1c,0xaa,0x23, 0x2e,0xb4,0x90,0xb,0xfb,0x12,0x9d,0xfd,0xec,0xc,0x3,0x2,0xa8,0x33,0xe,0x45, 0x13,0xd8,0xe4,0x91,0xec,0xdd,0xeb,0x97,0x79,0x76,0xa9,0x24,0x92,0x54,0x47,0xc0, 0x88,0xd8,0x4b,0x84,0xea,0x69,0x83,0x57,0x75,0x86,0xd8,0x9d,0xb9,0xe6,0x62,0x4c, 0x3f,0x47,0xde,0xab,0xa4,0xca,0xc2,0x1e,0x41,0x6c,0x42,0x53,0xc0,0xa,0x94,0x49, 0x62,0xdf,0xce,0x4d,0x49,0xd1,0x25,0x3e,0xd7,0x7d,0xdb,0x11,0xe4,0x3e,0x5d,0xa3, 0x85,0xbb,0x50,0xaa,0x7,0x13,0xc8,0xc7,0x80,0x8b,0x1c,0xc0,0x95,0xb0,0x8a,0xf7, 0x90,0xd8,0xc4,0xda,0x2a,0x69,0x19,0x2,0x67,0x75,0x13,0x4c,0xb3,0xef,0x6f,0xb9, 0x2c,0xbf,0x64,0x33,0x53,0x2d,0xfa,0x53,0x38,0x17,0x93,0xcd,0x47,0x1e,0x45,0xd8, 0x76,0x8a,0x33,0xa0,0xf3,0xcb,0xa2,0x5b,0x41,0x35,0x27,0xf5,0xa5,0x97,0xaf,0xd1, 0xd6,0x93,0x5,0x2a,0xc0,0x7f,0xfc,0x79,0x17,0x91,0x47,0x5e,0xaf,0xd,0x37,0x27, 0x97,0xe9,0x47,0xb,0xb6,0xea,0x67,0xf7,0x9f,0xe,0x6d,0x45,0x25,0x9c,0x17,0xfc, 0x30,0x9b,0xa6,0x71,0x1c,0xa4,0xea,0x33,0xb5,0xb1,0x11,0x65,0xbe,0xc8,0xc,0x56, 0xb2,0xd3,0x62,0x69,0x3e,0x49,0xe1,0xdd,0xd6,0x4f,0xa3,0xfc,0x6c,0xba,0xf9,0x9c, 0xd6,0x20,0x8d,0xf2,0x44,0x78,0xa5,0xf9,0x2b,0xb6,0x60,0x69,0x7f,0xeb,0x40,0x33, 0x3f,0x22,0x1c,0x7d,0x6b,0x7d,0x5c,0xc1,0x4d,0x0,0xbe,0xb9,0x3a,0x38,0xd5,0x11, 0x59,0x64,0x83,0x9d,0xdc,0x29,0x98,0x87,0x60,0x78,0x71,0xdf,0xe3,0xb1,0x92,0x24, 0xd3,0x2f,0xa1,0xbe,0x2c,0xfd,0x80,0x79,0x7d,0x40,0xb2,0xb8,0x78,0x89,0x49,0x51, 0xed,0xcd,0xef,0x4a,0x76,0x88,0x52,0xd6,0x80,0xc3,0x37,0x64,0x75,0xc9,0x88,0xc8, 0x78,0x2b,0x87,0xa5,0xa8,0x87,0x9e,0xa6,0x47,0x52,0x5f,0x40,0x5b,0x28,0x91,0x49, 0xf5,0x1,0x13,0x6d,0x9,0xe4,0x44,0x89,0xa8,0xfa,0xee,0x9d,0xc5,0xf6,0x66,0xbd, 0xa1,0x6d,0x63,0xca,0x75,0x82,0x71,0xbc,0xd4,0x50,0xfc,0x30,0x78,0xf,0xf8,0xee, 0x10,0x8b,0x5c,0x1a,0x71,0x20,0x23,0x99,0x1c,0x12,0xb7,0x61,0x89,0x1e,0x9e,0xaa, 0xc,0x82,0x75,0x81,0x5,0x66,0xbd,0xd9,0xb6,0x3b,0xa,0xaf,0x4a,0x82,0x9e,0xd9, 0xe,0x7a,0x73,0xfe,0x1a,0x97,0x99,0xb5,0x29,0x51,0x17,0xb2,0xee,0x36,0xdd,0x7a, 0xb8,0x53,0x7b,0xbd,0xba,0x3a,0x97,0xf0,0x75,0x21,0xa0,0x3f,0xa3,0x3f,0x98,0x31, 0xb9,0xd,0x31,0x54,0xa4,0x4a,0xa,0xcd,0x9b,0xa1,0x1,0xa,0xd7,0xde,0x85,0x90, 0xb1,0x1,0x4e,0x6c,0xba,0x65,0x5e,0x30,0x86,0x7e,0xee,0xa9,0xbe,0x88,0x5a,0xf7, 0x95,0x8b,0x4c,0xb9,0x55,0xd6,0x7,0xf0,0x78,0x8,0xfb,0x50,0x66,0x1,0xe0,0x19, 0x2,0xae,0x5,0x3d,0x14,0xe2,0xec,0x1a,0x62,0xdc,0x43,0xa0,0xe4,0x1d,0x18,0xf9, 0x29,0xe4,0xb3,0x7e,0xbb,0xba,0x70,0x34,0x43,0xeb,0x84,0xa9,0x6c,0xe4,0x42,0xed, 0x13,0xc7,0x2b,0xa6,0xaa,0x19,0x40,0x8c,0xf5,0x3,0xac,0x5a,0x20,0xc5,0x54,0x49, 0xaa,0x8,0xc8,0xe5,0xc2,0xb8,0x1a,0x6,0x24,0x1e,0x30,0x90,0x82,0x72,0x7e,0x95, 0x3a,0xaa,0xbb,0x65,0xc3,0xfb,0x71,0x39,0xfe,0x1f,0x93,0x1f,0xe4,0xe7,0xe8,0xf, 0xef,0xb1,0xf4,0x32,0x6a,0x8e,0xb8,0xe,0xac,0x68,0x9e,0xae,0xda,0x1d,0x44,0x95, 0xc7,0x7f,0x7a,0xb,0x7b,0xeb,0x44,0x7a,0xb,0x57,0x19,0x6f,0x3f,0x2,0xfd,0xae, 0x33,0x72,0xe1,0x1d,0x1,0x1a,0x2b,0x2d,0x82,0xc9,0xdb,0xdc,0xe7,0x9f,0xf1,0x2f, 0x1f,0x6c,0x3b,0x9a,0xd8,0xfe,0x94,0x63,0x57,0x2e,0xd3,0x16,0x30,0x51,0xc5,0x64, 0xc4,0x27,0x81,0xc5,0x41,0x2d,0xf3,0x43,0xf6,0x4f,0x20,0x5e,0xef,0x92,0x8e,0xf, 0x7e,0x49,0x2a,0x57,0xc7,0xbe,0x3b,0x1f,0x6c,0x8e,0xb5,0x9d,0xdf,0x7b,0x81,0xa4, 0x22,0x82,0x6b,0xe2,0xaf,0xde,0x26,0xa7,0x2e,0xc5,0x85,0x9d,0x58,0x14,0xad,0xd7, 0xdc,0x57,0xae,0xa5,0x95,0xe9,0x44,0x3,0x78,0xf9,0xa0,0x59,0xf4,0xa1,0x7d,0x17, 0xa3,0x68,0xf9,0x54,0x47,0x9f,0x7b,0xf5,0x66,0x1,0x93,0x3e,0x95,0xc0,0x95,0xf1, 0x97,0x45,0x17,0x2e,0xae,0x5c,0x31,0x28,0xd5,0x51,0x1,0x4b,0x72,0x7e,0xe1,0x16, 0xe7,0xdc,0x6a,0xae,0xfb,0x65,0x24,0xe1,0xe6,0x38,0x21,0x7c,0xf8,0xb6,0x6e,0x11, 0xfb,0x86,0x3f,0xab,0x62,0xef,0x53,0xb7,0xc0,0x54,0x3,0x33,0x52,0xe5,0x49,0xb9, 0x42,0x34,0x69,0xbd,0x19,0x8d,0xa0,0x0,0xc5,0xc1,0x7c,0x3f,0x78,0x6b,0x50,0xf4, 0x71,0xf,0x20,0x53,0xfe,0x73,0xb,0xbf,0x47,0x8e,0xf2,0x99,0xf3,0xbb,0x54,0xb5, 0x6f,0x3d,0x73,0x89,0xca,0x14,0x89,0x11,0x55,0x86,0x50,0xce,0x71,0x20,0x43,0x62, 0x2f,0x63,0xb5,0x2e,0x56,0x40,0x6d,0x9d,0xce,0x60,0xb6,0x42,0x9b,0xb,0xf7,0xc, 0xc7,0xeb,0x15,0x93,0x0,0x9e,0x24,0xd5,0xa4,0xf3,0xa4,0x95,0x14,0x67,0xf7,0xc2, 0xca,0xad,0x70,0xa0,0x6e,0xdd,0x3e,0x3d,0xbd,0xf4,0x0,0x59,0x80,0xf7,0xe4,0x48, 0x63,0xf9,0x5b,0x64,0x19,0x7f,0xb9,0x3d,0xf2,0xdd,0xd3,0x7,0x45,0xcb,0x49,0x8f, 0xf9,0xb9,0x30,0x68,0x97,0xed,0x25,0x55,0xe2,0xa4,0x2f,0xe2,0x9d,0x14,0xab,0x1, 0x8e,0x7,0xe4,0x27,0x7,0x9e,0x64,0xf9,0x7c,0xb7,0x81,0x41,0x4,0xca,0xd0,0xfd, 0x85,0x80,0xe5,0x9c,0x6e,0x8a,0xf2,0xd1,0x30,0x22,0xb4,0x4d,0xb5,0x60,0xcd,0xc3, 0xe7,0x33,0xea,0x6e,0x51,0x50,0x68,0x4e,0x8,0x69,0x8f,0xc,0xb4,0xe0,0x89,0x3a, 0x61,0xee,0xd6,0xd0,0xf9,0x49,0xa2,0xa9,0xea,0xd6,0xf6,0x21,0x38,0x44,0xe4,0x9f, 0x77,0xd0,0xe,0x49,0x21,0xf5,0x97,0xa8,0x60,0xa6,0x35,0x94,0x7,0x3e,0xce,0x69, 0xad,0x25,0xb9,0xa7,0xee,0x5c,0x51,0xd9,0x33,0xc7,0xfa,0xea,0xc,0xe0,0xa,0x4, 0x31,0x18,0xcc,0xd1,0x8e,0xe3,0x7a,0x6e,0x8a,0x2f,0x3,0x12,0xed,0x51,0x7b,0x9b, 0xf5,0x35,0x43,0xe4,0x11,0x14,0x3f,0x44,0xdb,0xb9,0xaf,0x67,0x1a,0xb9,0xea,0x4b, 0x52,0xb7,0x1d,0xe0,0x9b,0x18,0xce,0xa6,0x47,0xd1,0xb8,0xb4,0xa2,0xb3,0x50,0x98, 0x68,0x13,0x7e,0x79,0x27,0xbd,0x3d,0x82,0xf6,0x6c,0xea,0x12,0x27,0x55,0x5d,0xf8, 0xe,0x7b,0x59,0x29,0x13,0x28,0x4f,0x5a,0x79,0x87,0x10,0x1c,0xba,0xdf,0xb4,0x23, 0xf3,0xb2,0x9c,0x1b,0xef,0x5a,0x1e,0xe7,0xc6,0x88,0xf9,0x6d,0xdd,0x57,0x66,0x6b, 0x52,0xbf,0x95,0x65,0x67,0x64,0x40,0xe0,0x6c,0xcf,0x7c,0x27,0xaf,0xb1,0x4b,0x23, 0x64,0x67,0xbe,0xd4,0xc1,0xdc,0xbc,0x89,0x65,0x36,0xf6,0x43,0xd,0xdd,0xaf,0x60, 0x1d,0xc4,0x45,0x85,0xa8,0x5,0xe5,0x15,0xd4,0x63,0x3d,0x5,0x94,0x88,0x28,0x78, 0xef,0xe6,0x4d,0x32,0x43,0x89,0x3b,0xa8,0xbf,0xb1,0x6c,0xcd,0x8f,0x1c,0xad,0xad, 0x60,0xf2,0xb2,0x9,0xf8,0x98,0x9e,0x4d,0x7b,0xdb,0x52,0x8f,0xe3,0xfa,0x9,0x53, 0x61,0x56,0x85,0xa5,0xe0,0x40,0x4e,0xa0,0xf2,0xba,0xed,0x2,0x56,0x9b,0x2f,0x36, 0xf,0xe1,0xbf,0x87,0xfa,0x5e,0x54,0xf5,0x3a,0x27,0x86,0x9d,0xa1,0x8f,0xf0,0x3, 0xe5,0xf6,0xa8,0x46,0xb6,0x77,0x67,0xa9,0x32,0x55,0x2c,0x9,0x71,0x5b,0x3f,0x0, 0xbd,0xfe,0x7,0xb8,0xdc,0xda,0xae,0x96,0x2,0xb4,0x34,0xa3,0x44,0xa5,0xa7,0xaa, 0x9c,0xcf,0x70,0x53,0x47,0xd7,0x7d,0xf9,0xad,0xa9,0x82,0x9e,0x84,0xc1,0x9e,0x42, 0x41,0x25,0xfa,0x1e,0x0,0x2a,0xb5,0x82,0xde,0x69,0x26,0x24,0xf,0x4d,0x4e,0x2b, 0x9d,0xbe,0xfe,0x64,0x97,0xfb,0xdd,0xc4,0xa5,0x60,0x63,0xa9,0xa2,0x81,0xec,0xe3, 0xa6,0xe7,0x81,0x26,0x91,0xb6,0xa8,0x71,0x21,0x4f,0x15,0x30,0x1c,0x63,0xdb,0xb9, 0xa1,0xda,0x9e,0xb8,0xd6,0x7c,0x7d,0xfb,0xdd,0x60,0xa5,0x80,0xe1,0x92,0xe3,0x8, 0xfa,0xe4,0xae,0x8c,0x9c,0x57,0x7d,0x3d,0x26,0x92,0xec,0xc2,0x75,0xc8,0xfb,0x18, 0x23,0x9a,0x50,0x79,0x18,0x4e,0xf4,0xf5,0xae,0x1b,0xf5,0x91,0x2d,0x59,0x19,0x28, 0x3e,0xc7,0x35,0x5a,0x9f,0xb2,0x97,0x45,0xc5,0x85,0x8,0x3b,0xcd,0x5,0xd2,0xf1, 0x9f,0x24,0xea,0xb7,0xf1,0xe0,0x2d,0xa0,0xfb,0xa2,0xb1,0x29,0xfb,0xcb,0xd1,0xba, 0x13,0x86,0x15,0xb2,0x39,0xad,0x78,0x7e,0xb2,0x80,0xba,0x80,0x5,0xd,0xf1,0xa5, 0xb0,0xdd,0xdc,0xa2,0x3e,0x8a,0x44,0xb9,0x2d,0x75,0xe2,0x2a,0x41,0x34,0xe4,0xd4, 0xba,0x79,0x7,0x74,0xa6,0x7f,0xf2,0x59,0x80,0x2d,0x5a,0x85,0xba,0xcb,0xaa,0xea, 0x29,0x8,0x8e,0x67,0x92,0x52,0xa0,0xbf,0xc7,0x4,0x69,0x89,0x38,0xcd,0x5e,0x73, 0x48,0xe4,0x67,0xee,0x65,0x5a,0xc8,0x65,0x8,0xa2,0xea,0x42,0x6e,0x16,0x2d,0x18, 0x1e,0x3b,0xfe,0xb0,0x8d,0xa0,0xef,0xd5,0xa4,0x5a,0xde,0x5c,0x28,0xbc,0xcf,0xef, 0xa1,0x37,0x5f,0x86,0x12,0x28,0xeb,0x99,0xca,0xd7,0xdb,0xb8,0xed,0x88,0xd0,0x8b, 0xc4,0x50,0x3c,0x52,0xf0,0x2c,0xa7,0x15,0x6,0x86,0x71,0x2f,0x43,0xc1,0x9e,0x65, 0xf8,0xfd,0xeb,0x8a,0x26,0xd8,0x24,0x70,0x30,0x7f,0xa9,0x9d,0x88,0xf9,0x29,0x4d, 0x4a,0xe4,0x1f,0xba,0x90,0xc7,0xcf,0x97,0xcd,0x42,0x46,0x91,0x4,0xe4,0xf6,0x7c, 0xe3,0x62,0x8,0x89,0xba,0xab,0x7a,0x6a,0xab,0x24,0x87,0x34,0x1e,0x30,0x1,0xe8, 0x15,0x20,0xa3,0xa6,0x67,0x74,0xbd,0x36,0x36,0x4,0x47,0xb9,0x68,0x3e,0x36,0x4c, 0x20,0xbd,0x56,0xdb,0xe9,0xd0,0xc5,0x15,0xf4,0x4e,0xc8,0x92,0x7e,0xc9,0x7b,0x94, 0xe9,0x9f,0xba,0x52,0x14,0x78,0x8,0xc9,0xfb,0x4f,0x83,0x64,0xd,0x39,0x31,0x2d, 0x77,0x7,0x88,0xe0,0xd7,0x4f,0xf5,0x4c,0x9d,0x3e,0x5e,0x9b,0x8,0xda,0x30,0xf1, 0xf9,0x6a,0xc3,0xe,0x62,0xcb,0x57,0xdd,0x9a,0x5a,0x43,0xa7,0x93,0xf3,0x55,0x8a, 0xfa,0x5d,0xea,0x52,0x2c,0xe0,0x9e,0xc9,0x1f,0xfc,0xe5,0xa6,0x57,0x16,0x19,0x51, 0x1,0xdc,0xde,0x63,0x29,0x36,0x42,0xc3,0x10,0x5,0xeb,0x24,0x78,0x41,0xae,0x73, 0x1e,0x9a,0xc5,0x4b,0xfa,0xe3,0x94,0x9a,0xe0,0x7a,0x41,0xb8,0x11,0x5a,0xa,0x12, 0xb7,0x69,0xf4,0xe0,0x1f,0xb6,0x24,0x30,0x3b,0x10,0x54,0xb3,0xd0,0x82,0x27,0x6f, 0x9c,0x6c,0xba,0x98,0x50,0x4f,0xb2,0xb1,0x4a,0x73,0x6a,0x5b,0x4e,0xf3,0xec,0x6, 0x5d,0xe1,0x66,0x7d,0x19,0xa,0x2d,0x54,0x9a,0x1,0x9,0x6b,0x83,0xaf,0xda,0x21, 0x9c,0x15,0x39,0xec,0xe4,0x6b,0x1e,0x2f,0x5e,0x88,0x8a,0xac,0x7d,0x77,0x32,0x5a, 0xd8,0x18,0x57,0xf1,0x23,0x84,0x47,0xbd,0x5,0xcf,0xa8,0x89,0x7f,0x4,0x2a,0x1c, 0x19,0xe2,0x89,0xfd,0x4e,0xa7,0x2d,0x2c,0xb0,0x37,0xd9,0xad,0xae,0x8b,0x8,0x88, 0xa4,0xdf,0x7a,0x47,0xe3,0x41,0x5,0xe9,0x11,0x2d,0xf2,0x11,0xb0,0x1d,0xac,0xca, 0x7f,0x36,0x48,0x4d,0x5e,0xf5,0x79,0xf,0xac,0x53,0xbc,0xdb,0x5f,0x44,0xe3,0x4, 0x24,0xdd,0xca,0x88,0x20,0x4f,0x72,0x31,0x7c,0x65,0xc1,0x2e,0x2,0x6f,0x78,0x81, 0xa5,0x40,0xce,0x83,0xb5,0xc7,0x92,0x63,0x9b,0xce,0x3f,0xfa,0x14,0x23,0x7e,0xb7, 0x1,0x49,0xbf,0xa0,0x98,0x32,0xd2,0x15,0x17,0x14,0xc2,0x98,0x83,0xba,0x99,0xa9, 0xfb,0xe7,0x2d,0xb1,0xb0,0xc0,0x94,0x4c,0x8f,0x53,0x47,0x23,0x76,0x45,0x5b,0xf7, 0x8e,0x1b,0x98,0x27,0xcd,0xea,0xbb,0x64,0x0,0x7f,0xfd,0x83,0x3a,0x17,0x2d,0xb5, 0x0,0x5b,0xe7,0xb0,0x9b,0x7c,0x7c,0xaa,0xd0,0x43,0x4e,0xc6,0x88,0xa9,0x3e,0x17, 0x44,0xd7,0xbd,0x91,0xc2,0x79,0xf6,0x42,0xf8,0x74,0x46,0xb3,0xb,0x73,0x69,0xb, 0x4e,0xd0,0x3b,0x69,0xcd,0x37,0x15,0x1e,0x7a,0x63,0xe4,0x82,0x8c,0x24,0x19,0x50, 0x7b,0xd6,0xe2,0xbd,0x51,0x59,0x1,0x4a,0x4d,0x47,0x7d,0x58,0x3a,0x67,0xe3,0x9, 0x38,0x1f,0x72,0x6,0x57,0x87,0x24,0x51,0x6a,0x89,0x54,0x76,0x2d,0x6d,0x47,0xa8, 0x45,0xa9,0x66,0x96,0x3,0x67,0x60,0xcf,0x2e,0xde,0xa7,0x69,0x46,0x8b,0xf1,0xfd, 0x2b,0x64,0x84,0x2,0x6c,0xa8,0x53,0x56,0xb1,0xa7,0xcd,0xde,0x16,0x15,0x87,0xda, 0xbe,0x6e,0x71,0x41,0xd5,0xd1,0x90,0x84,0x30,0x38,0xed,0x76,0xc4,0xdf,0xf4,0x6f, 0xc3,0x79,0x71,0x30,0xa1,0x44,0x87,0x54,0xec,0xd4,0x33,0x82,0x69,0x3b,0x5d,0xa7, 0xa9,0x4e,0x68,0xfe,0x20,0xf8,0x83,0x51,0xb0,0xf0,0x47,0xf4,0x50,0x3c,0x64,0x15, 0x35,0xd5,0xc4,0xd7,0x1b,0xcb,0x2c,0x87,0xa0,0xde,0x89,0x89,0x1a,0xe6,0x31,0x43, 0xb4,0x99,0x43,0xd4,0x12,0xc6,0xa5,0xc3,0x38,0x6d,0xb8,0x88,0x29,0x1e,0x9d,0x5f, 0x73,0xe2,0x37,0x8e,0xae,0xe2,0x95,0x50,0xc1,0x1f,0xd9,0x5c,0x85,0x8b,0x9f,0x3a, 0xa4,0xe2,0x10,0xb7,0x2a,0x35,0x7b,0x62,0xa2,0xb3,0x6a,0xcc,0xd1,0x88,0x2c,0xc5, 0x6b,0xe2,0x54,0x1a,0xc5,0xea,0xe9,0x87,0xa,0x44,0xe3,0x10,0xcf,0x84,0x4a,0x74, 0xe6,0xd9,0xab,0x11,0x10,0x27,0xf2,0x32,0x5b,0x5e,0xfe,0xac,0xe6,0xaa,0x72,0x52, 0xd,0xc7,0xeb,0xd2,0x32,0xd6,0xda,0xbb,0x1b,0xbe,0xcb,0x6a,0xc2,0x96,0x5e,0x2a, 0x70,0xb,0xba,0x0,0xb1,0xae,0x33,0xd,0x8c,0xb1,0xba,0xf2,0x5d,0xac,0xc4,0x6a, 0xf3,0xb0,0xbd,0x26,0x7,0x98,0x62,0x22,0xd6,0xad,0xc,0x1a,0x44,0x6b,0x44,0x35, 0xf5,0x7e,0x35,0xa7,0xac,0x68,0x35,0x39,0x1b,0x6f,0x2c,0xf7,0x1c,0x70,0xe1,0x11, 0x22,0x9f,0xb6,0x29,0xb7,0x98,0xcb,0x8f,0x47,0xd7,0x29,0xb,0xc2,0x6d,0x40,0xb8, 0x6b,0x76,0xe0,0x19,0x5e,0x16,0x52,0xf8,0x85,0xfe,0xf0,0x21,0x6f,0x53,0x32,0x11, 0x72,0x69,0x3b,0x2b,0x2,0x7,0x3a,0x49,0x5e,0x63,0x55,0xa1,0x50,0x15,0x5a,0xbb, 0x8b,0x3b,0xd4,0x6a,0xd0,0xa7,0x63,0xd5,0x26,0xd4,0xf7,0x15,0x28,0x2a,0x27,0x9a, 0x93,0xe1,0x45,0x16,0x68,0xfe,0x5f,0x46,0x62,0x34,0xe7,0x32,0x4a,0xc2,0xee,0x55, 0xfd,0x43,0xbf,0x4f,0x6a,0x24,0x25,0x10,0xf8,0x1d,0x26,0xa0,0xc7,0xcc,0xba,0xda, 0x2e,0x1,0xf0,0x96,0x0,0x51,0x5c,0xe2,0x5,0x45,0x15,0x4f,0x8,0x83,0xa5,0x85, 0x47,0xe4,0xd4,0xb1,0x9,0xfa,0xc2,0x81,0x97,0x68,0x22,0x5f,0xb4,0x5d,0x3b,0xe2, 0xdd,0x2c,0xf8,0x5d,0xfc,0x55,0x40,0x3,0x9a,0xd5,0xd1,0x22,0xd8,0xf6,0xa8,0x20, 0xdc,0xfc,0x52,0x65,0x77,0x15,0xe7,0x10,0xfc,0x89,0x6f,0xb1,0xe6,0xaa,0x94,0xc4, 0x57,0x8d,0x23,0xd3,0x62,0xe2,0x56,0xfd,0xb8,0x29,0x9f,0x12,0x9f,0xc7,0x32,0x7c, 0xc5,0x84,0xe2,0x3d,0x19,0x4a,0x4d,0x16,0xd3,0xbd,0x47,0xbb,0xe7,0xdb,0x0,0xbe, 0xe8,0xa2,0x93,0xcb,0x86,0x69,0x49,0xbe,0x92,0xe8,0xd0,0x33,0xb1,0x83,0x2f,0x77, 0x87,0x91,0x34,0xa1,0xdb,0x82,0x37,0xb0,0xbf,0xfe,0xeb,0x27,0x5a,0x6b,0xe6,0x44, 0xf,0xf9,0x10,0x15,0x63,0x59,0xd3,0x76,0xc1,0x25,0x29,0x73,0xa8,0xd7,0x6a,0x30, 0x6a,0x9f,0x51,0x46,0xa1,0x9,0x76,0x61,0x8,0xe1,0x88,0x62,0x4e,0xee,0x26,0xdc, 0x68,0xb5,0xf1,0xcc,0x8e,0x45,0xc2,0x51,0xe9,0xeb,0xc4,0x92,0xc3,0xaf,0x43,0xad, 0x4f,0x14,0xf4,0xf0,0x9c,0xea,0xd1,0xa4,0x4d,0xd9,0x87,0x1b,0xc9,0xad,0xf7,0x32, 0x64,0x69,0x7e,0xf2,0x2e,0x41,0xc3,0x19,0x2d,0x9,0x2b,0x71,0xb8,0xed,0x1f,0x87, 0x3,0x93,0xf7,0x9f,0xfe,0xc9,0xc4,0x4c,0xa3,0x4c,0x67,0x6d,0xf9,0xde,0x20,0xdd, 0x48,0x9e,0x51,0xf5,0xe0,0x15,0xf,0x8d,0x1e,0x3b,0x7e,0x56,0x29,0x1e,0xdd,0xab, 0xb1,0xd5,0x4c,0xb0,0x1f,0x90,0x7c,0xc3,0xdc,0xe3,0xb0,0x56,0x42,0x50,0xb4,0xa, 0xef,0x6,0x1,0x50,0x9a,0x10,0x5d,0xb9,0xca,0xdc,0x10,0xf4,0xfa,0x6e,0xa0,0x2c, 0xc3,0x6c,0x5d,0xe3,0x7c,0xd9,0xa7,0x59,0x3e,0xd7,0x30,0x80,0x29,0x64,0x8b,0x98, 0x6a,0xc,0x68,0x84,0x1c,0xc5,0xbd,0x67,0x22,0x4e,0x5c,0x9c,0xbc,0x7c,0xc9,0x80, 0x69,0xa6,0x64,0xe5,0x80,0x8b,0xbf,0x3e,0xe3,0x6f,0xbf,0x8c,0xd3,0xca,0x25,0xbd, 0xd6,0xd,0x42,0x72,0xd2,0x80,0xd9,0x75,0xce,0xb5,0x12,0xb,0xb2,0x5b,0x8b,0x9b, 0x2,0x70,0x81,0x3,0x7b,0xc0,0x41,0x5f,0xaf,0x80,0x6b,0x83,0xca,0x90,0xc0,0x21, 0x1d,0x83,0x14,0xf0,0x4,0x6d,0xe5,0x52,0x24,0xf7,0x5d,0x56,0x54,0x68,0xf1,0xd5, 0xd8,0xf2,0xd8,0xd4,0x34,0x9a,0x34,0xe3,0x9a,0xa0,0xe7,0x66,0xb0,0xa8,0x7,0x4e, 0xab,0x1b,0x3f,0xaf,0x89,0x25,0x2,0x2d,0x9c,0xde,0x83,0x70,0x48,0xf4,0x47,0x21, 0xe7,0x9f,0xf5,0x1c,0xb9,0xaa,0x1,0x55,0xca,0x68,0x3b,0xfa,0x11,0x42,0x49,0xbd, 0x5e,0x8,0xec,0xe7,0xac,0x6f,0x15,0x4a,0x4e,0x18,0xba,0x96,0xd,0x81,0x38,0xf4, 0xa1,0xad,0x91,0x5b,0x58,0x12,0xb0,0xa2,0x7a,0xeb,0x9e,0x8b,0xae,0x67,0xc8,0xd, 0x70,0x36,0x74,0x1d,0xa5,0x89,0xe6,0x73,0xa1,0xa2,0xb,0x2e,0xa3,0xc2,0x23,0x45, 0x70,0x34,0xa1,0xc9,0x46,0xd1,0xeb,0xc0,0x3e,0x8a,0xcc,0xec,0x72,0x15,0x79,0xe2, 0x4b,0xed,0x7f,0x70,0x77,0x67,0xe4,0x98,0x89,0x6f,0x46,0x2d,0x32,0x69,0xf2,0xa2, 0x9e,0x14,0xeb,0xe4,0xe5,0xd8,0x26,0x24,0xe2,0xf2,0x90,0x55,0x8,0xa,0x38,0xd3, 0xf7,0x38,0x44,0xee,0x9f,0x29,0x7,0xa8,0x18,0x4d,0x55,0x4a,0x37,0x48,0xed,0x55, 0x5c,0xd9,0xb9,0xc2,0x32,0xdf,0xe6,0x16,0x52,0xf7,0x6b,0xda,0x2,0x24,0xae,0x7a, 0xdb,0xf2,0xe8,0x7b,0x9c,0xf0,0xa3,0xb4,0xbd,0xf8,0x7f,0xf4,0x42,0x6d,0xc9,0x1e, 0xc6,0x84,0xe0,0xf9,0xe3,0x48,0x8f,0x37,0x40,0x7a,0x12,0xc1,0x1e,0x40,0xbb,0xf9, 0xb2,0xa5,0xf4,0x4f,0x16,0x98,0x84,0xd3,0x12,0x4,0x49,0xd3,0xf0,0x13,0xf1,0x37, 0x97,0x53,0xb0,0x7c,0x1b,0x40,0x33,0xda,0x3b,0x45,0x9c,0x59,0x5,0xd8,0xd3,0xb7, 0x7e,0x48,0x87,0x94,0xe1,0xc,0xe7,0x73,0x8f,0x31,0x47,0x0,0xc4,0xb8,0xb6,0x5c, 0x8b,0x68,0x58,0xa6,0x28,0xb,0x81,0x63,0x50,0x9e,0x3d,0x55,0x77,0x11,0x8d,0x75, 0x59,0x15,0x89,0xba,0xa0,0x71,0xad,0xaf,0x23,0xf4,0xaf,0xe7,0x2e,0x66,0xc3,0xb9, 0x4e,0x9c,0x61,0x77,0xa7,0x62,0xda,0x78,0x1,0x97,0x4d,0xf7,0xa8,0xda,0x6d,0x82, 0xef,0xf6,0xbc,0x90,0xe8,0x6b,0x40,0x8b,0x60,0x6f,0x73,0xe,0x56,0xb6,0xc8,0xa4, 0x53,0xa9,0x9b,0xfb,0xc,0xf6,0x74,0x8d,0x8e,0xc1,0x85,0x38,0x1d,0x73,0x3a,0xd, 0xe9,0xf6,0x1e,0xd2,0x62,0x5e,0x5e,0x43,0x4e,0x51,0x51,0xa4,0x9,0x99,0xc8,0x5c, 0x43,0x65,0xd7,0xcf,0x5c,0xcb,0xdc,0xea,0xe,0x62,0xa2,0x2b,0xd5,0xdc,0x38,0xc0, 0x54,0xd5,0x13,0xb6,0x35,0xf1,0xf9,0x3,0x43,0xcb,0xa7,0xcb,0x65,0xef,0xa8,0x29, 0xd4,0x80,0x78,0x31,0xcc,0x55,0x9c,0xda,0xb7,0xbe,0x6,0xe,0x1c,0xbd,0x4e,0x70, 0x94,0xe0,0xa6,0x49,0xd2,0x21,0x4c,0x96,0xec,0x73,0x62,0x52,0x63,0x8a,0xfa,0xb8, 0xc,0x73,0xe9,0xd8,0xc8,0x6,0x33,0x1,0xc5,0x39,0x8e,0x61,0x76,0x5c,0xd1,0x8a, 0x3d,0x78,0xd3,0x90,0x99,0x9f,0xa6,0x6,0x13,0x9,0xd8,0xf6,0x14,0xd3,0xaf,0x9f, 0x48,0x19,0xf7,0x90,0x9f,0x2b,0x11,0xe4,0xe3,0x9f,0x46,0x5a,0xfb,0x97,0x65,0xb9, 0x10,0x39,0xc9,0x2a,0xd9,0x70,0x30,0x6c,0xf8,0x88,0xe2,0xd,0x5d,0x92,0xac,0x25, 0x2c,0xa4,0x35,0xcb,0xcf,0x47,0xb0,0xb3,0x66,0xf6,0x8e,0x63,0x8e,0xf3,0x9c,0x1e, 0xac,0x66,0xc7,0x6,0xd6,0x78,0x73,0xcf,0x1,0x56,0x5d,0xdd,0x69,0xa,0x3,0x95, 0xaf,0xb8,0xe0,0xfe,0x0,0x91,0x33,0x66,0x8,0xc1,0x49,0x16,0x35,0x65,0x34,0x61, 0x4b,0x7c,0x68,0x22,0xf4,0x5b,0x72,0x75,0x31,0x4f,0x54,0x1a,0x59,0xd6,0xaf,0x88, 0x8f,0x10,0x88,0xf,0xa1,0xbb,0xf5,0x29,0xfc,0xbe,0x3f,0xb1,0xa4,0xf3,0x13,0xef, 0x70,0x7b,0x92,0xe4,0x56,0x5,0xd9,0x88,0x54,0xad,0xa2,0x2d,0x85,0xd2,0xb6,0x94, 0xe2,0x3f,0x24,0x5,0x7a,0x99,0xad,0x77,0x58,0xed,0x29,0xfc,0x61,0x3c,0xed,0x51, 0x38,0x80,0xb5,0x8e,0x5,0x8f,0x96,0xd8,0x3e,0xb9,0x6,0x43,0x8c,0x3c,0xd7,0xee, 0x7b,0x7b,0x73,0x75,0x15,0x22,0xec,0x6e,0x8f,0x95,0xea,0xf0,0x52,0x58,0x42,0x8a, 0x58,0xf7,0x98,0x5d,0x87,0x30,0xb5,0x45,0x69,0x3c,0x88,0xf5,0x78,0xe0,0x64,0x74, 0x5c,0xd8,0xe9,0x72,0x7a,0x57,0x60,0xa,0xec,0xca,0xfa,0x3f,0x24,0xbc,0xc9,0xfb, 0xb4,0xe2,0x5a,0xbb,0x92,0x8f,0x81,0xfb,0xcb,0xa,0x71,0x45,0xea,0xd5,0x39,0x48, 0x2e,0x23,0x3a,0x28,0x7a,0x1a,0x32,0x68,0xe4,0xac,0x27,0x88,0x69,0xf1,0x85,0x9d, 0x54,0x5f,0xd9,0xe6,0xee,0x5b,0xe2,0x3b,0x65,0xd3,0x80,0xd0,0xa9,0x39,0x98,0x58, 0x5c,0xd2,0x80,0x57,0x6c,0x33,0xbf,0x51,0x5f,0xe6,0x5a,0x49,0x58,0xdf,0xe6,0xac, 0x3f,0x40,0x13,0xad,0x1b,0x75,0xe8,0x1,0x49,0xe8,0xd1,0xf3,0x22,0x6a,0xcb,0xfe, 0xbc,0xcb,0x56,0xa8,0x7e,0x16,0xf9,0xde,0x7c,0xd3,0x28,0x55,0xb3,0x8e,0x81,0x72, 0xcf,0x95,0x21,0x6a,0xb,0x89,0x6b,0x55,0xf2,0x3d,0xc8,0x15,0x27,0x94,0x14,0x63, 0xdf,0xe9,0xc,0x5f,0x7f,0x86,0x3e,0xfc,0x5a,0xe5,0xd1,0xf,0x74,0x53,0x1,0xc3, 0x68,0xa1,0x2f,0x74,0x2c,0x9a,0x49,0x1f,0x58,0x12,0xb3,0x7f,0x26,0x48,0x63,0x85, 0x32,0x6f,0xe4,0xb2,0xf5,0xa2,0x2f,0xd0,0x88,0x1,0xdf,0x7d,0xd3,0x60,0x41,0x3d, 0x3,0xef,0xb1,0x2f,0x8b,0x7a,0xcd,0x63,0x8c,0x1,0xe2,0x32,0x49,0x46,0xb7,0x7c, 0x36,0x9d,0xae,0x2c,0xbf,0x5d,0x7c,0x49,0x5e,0xdb,0xc6,0xb1,0x3d,0x87,0xee,0x40, 0x78,0x20,0xee,0x83,0x9a,0x3c,0xe6,0xa6,0x3d,0xc9,0xd8,0x87,0x90,0x11,0x83,0xc6, 0x2e,0xb1,0x72,0xed,0xf,0xef,0x37,0xec,0xcb,0x7d,0x9e,0x88,0x6,0x8e,0xc8,0x7e, 0xae,0x37,0x2,0xc9,0x73,0xe8,0x70,0x31,0x32,0xc9,0xb8,0x42,0xda,0xbb,0x88,0x9, 0x6d,0x7b,0xf6,0x7c,0xea,0xae,0x69,0x36,0x2c,0x8,0xbf,0x32,0x16,0x8,0xb0,0x45, 0x40,0x32,0xf,0x33,0x9a,0xfe,0x64,0xcd,0x48,0x9c,0x8f,0x23,0x58,0x19,0xab,0x45, 0x14,0x23,0xc1,0xfe,0xd1,0xaa,0x35,0x7d,0x33,0x74,0xb0,0xc8,0x7d,0xe0,0xe,0x3d, 0x93,0x9c,0x70,0x2e,0x1c,0x55,0x7b,0x64,0xf1,0xc,0x8,0xca,0xa4,0xb3,0x10,0xb8, 0x56,0x52,0x37,0xa7,0xfc,0xeb,0x26,0xaf,0x61,0x56,0x79,0x5e,0xb6,0x7,0x9b,0x4a, 0xa4,0x8b,0x79,0xc0,0xe0,0xf4,0xa4,0x53,0x80,0xac,0x1e,0x25,0xe0,0x2e,0x5d,0x37, 0x0,0x14,0xdf,0x7d,0x1,0x85,0x2d,0xe1,0xdb,0x26,0x40,0x92,0x2e,0x5b,0x5d,0xd2, 0xe6,0xd6,0x13,0x48,0x4b,0xb7,0x1b,0xcc,0x65,0x39,0x71,0x46,0xe6,0x4f,0xfc,0xe7, 0x63,0xdc,0x65,0xe3,0x62,0x92,0xc5,0xbd,0x39,0x85,0x51,0x67,0xe0,0xae,0xb9,0x48, 0x5,0xcc,0x10,0xcf,0x4,0x2b,0x9c,0x69,0x64,0x8e,0x2f,0xca,0x5d,0x2d,0xb2,0x40, 0x89,0x18,0x25,0x6c,0x2b,0x6a,0x2a,0x64,0xf0,0xfa,0x4b,0x51,0x29,0x5,0x19,0xad, 0xd1,0x29,0x7e,0xd5,0xd3,0x9a,0xbf,0xb7,0x29,0x6e,0x83,0x6,0x1b,0x36,0x47,0x25, 0xce,0xeb,0x91,0x79,0x56,0xbb,0x5d,0xc6,0x37,0xa8,0x98,0x60,0xad,0xb1,0xf,0xfe, 0x5b,0x8d,0x54,0x2f,0xa7,0x93,0xe7,0xd1,0x3,0x6b,0xd7,0x9d,0x21,0x9e,0xc2,0x6f, 0x8a,0x54,0x68,0xe1,0x90,0xc5,0x28,0x47,0xed,0xc0,0x27,0x1b,0x73,0xb5,0x1a,0x4e, 0xc2,0xee,0x7d,0x6b,0x82,0xe4,0x3d,0x5,0xcf,0x94,0xa3,0x71,0x34,0xe5,0xe0,0x3e, 0x3b,0xc9,0x20,0x4b,0xf,0xc8,0x12,0xfd,0x89,0x39,0x19,0x7c,0xef,0xb3,0x4a,0xb2, 0xa2,0xc8,0x1e,0x25,0x2d,0xda,0x2b,0xfd,0x70,0x4e,0x6f,0x24,0x34,0xcf,0x62,0xee, 0x99,0x3,0xb9,0x29,0xcb,0xcb,0x27,0xd4,0x6,0xbf,0xd1,0xf5,0x73,0x1c,0x28,0x95, 0x64,0x47,0x3b,0x92,0x22,0x66,0x90,0x92,0x34,0x7f,0x36,0x68,0x4f,0x99,0xd7,0x69, 0x1c,0x91,0x92,0x67,0x5e,0x39,0xbb,0xe3,0xf8,0x8d,0x59,0xec,0x2a,0x81,0x82,0x8e, 0xc8,0xbd,0x21,0xeb,0xa3,0x31,0xfd,0xd7,0xb0,0xb4,0xc0,0x1,0xcd,0x98,0xe9,0xe9, 0xa9,0xfb,0x51,0x8,0x35,0x8c,0xeb,0x2e,0x1b,0xc4,0x9a,0x45,0x47,0x9d,0xd3,0x10, 0x5b,0x75,0x7b,0x7f,0xa6,0x7a,0xd6,0x58,0xae,0x17,0xd8,0x7c,0xaf,0x42,0x66,0x5a, 0x3e,0x37,0xe1,0x73,0xc3,0x4e,0x21,0x5e,0x13,0xbc,0xa3,0x5a,0x5a,0xf7,0xea,0x35, 0x6d,0x66,0x34,0x93,0x60,0xc,0xeb,0xf,0x23,0x44,0x8b,0x53,0x86,0x71,0x2d,0xc4, 0xa8,0xf,0xb7,0xec,0xdc,0xd9,0x4b,0xf0,0x16,0xef,0xca,0xef,0x67,0xb5,0xa4,0xd4, 0x9c,0xd9,0x68,0xfc,0x65,0xd4,0xd,0x8,0x19,0x18,0x5b,0x20,0x8a,0x88,0xe4,0xb2, 0x18,0x9d,0x9f,0x74,0xf6,0xeb,0xe4,0xd,0x5b,0xb0,0x7c,0xc2,0xe5,0x21,0x17,0x82, 0xfa,0xfe,0x0,0x60,0xd3,0x8c,0x69,0x6d,0xa4,0x44,0x8d,0x2f,0x4d,0xf1,0xe2,0xe4, 0xf,0x2,0x59,0x6,0xed,0x3f,0x92,0x49,0x6f,0xf,0x8b,0x55,0x31,0xa2,0x58,0xab, 0x22,0x58,0xd,0xf5,0xe4,0xf5,0xe2,0x89,0x3a,0xef,0x39,0x7,0xe2,0x9b,0xeb,0x71, 0x9d,0x46,0x78,0xc,0x5,0x8a,0xd4,0x74,0x9a,0x61,0xc9,0xcb,0x83,0x22,0x77,0xa5, 0x7a,0x4,0x1c,0x5f,0x79,0xfe,0x69,0x34,0x6f,0x22,0x3b,0x52,0xbd,0x28,0x43,0xda, 0xed,0xbb,0xe6,0xf2,0x47,0xbc,0x67,0x61,0x9d,0xb0,0x2d,0x21,0xd3,0x24,0xc7,0xcd, 0xa8,0x63,0xad,0x22,0x62,0x17,0x56,0x51,0xb8,0x12,0x23,0x76,0xb9,0x67,0x51,0xa7, 0x23,0xb8,0x1a,0xe9,0xf4,0x1,0x4b,0x92,0xb1,0xf7,0x33,0x5,0x9c,0x7a,0x53,0x45, 0xdd,0x1,0xe6,0xc0,0x97,0x3e,0x12,0x50,0xcf,0x36,0x46,0x89,0x9d,0x17,0xb0,0x40, 0xcf,0xca,0xaa,0x44,0x4b,0xf5,0xd6,0xfc,0x6e,0x8a,0x82,0xb,0x5,0xd5,0x50,0x63, 0xd6,0x37,0x24,0xed,0xf4,0xb5,0x3e,0x44,0x6b,0x84,0xcd,0x9,0x9b,0xfd,0xc9,0xeb, 0x48,0x74,0x30,0x93,0xe9,0x87,0x91,0x58,0x12,0x93,0xe2,0x96,0x69,0xb2,0xf9,0xbf, 0x6a,0x9d,0xad,0xde,0x54,0xeb,0x24,0x3f,0xef,0xf1,0x49,0xb,0xf0,0x92,0xf6,0x39, 0x7,0x28,0x4d,0x70,0x2f,0x5e,0x49,0xc0,0xf1,0x2c,0x57,0x5b,0xdf,0xd1,0x1b,0x4a, 0xee,0xc8,0x29,0xc2,0x34,0xcc,0x3,0xa3,0xbf,0x4c,0xae,0x30,0x5e,0xa6,0xe8,0xe4, 0x4e,0x36,0x55,0xfc,0x94,0x9e,0xbd,0x86,0xcb,0x15,0x61,0x2b,0x66,0x7c,0xf4,0x56, 0xc4,0x9d,0x19,0x78,0x6b,0x1c,0x1c,0xaa,0xe7,0xcb,0xda,0x46,0xf1,0x43,0x2b,0x40, 0xf9,0x1,0x3d,0x8e,0x1f,0x7a,0x95,0x6a,0x8f,0xf6,0x95,0x76,0xf3,0xa,0xcc,0x38, 0xa8,0x65,0xb1,0x14,0x82,0xcd,0x3e,0xe9,0x19,0x19,0xb0,0xb,0xdb,0x5b,0xca,0xd5, 0x5c,0x87,0xe4,0x7c,0x2,0x7a,0x66,0x12,0xf0,0xfc,0x88,0xe4,0x7,0xd4,0x1e,0x2f, 0x3a,0x4f,0xc2,0x3c,0x9c,0x1,0xa6,0xb6,0x99,0x57,0xc1,0x76,0x32,0xd,0xcb,0xf, 0x94,0xb0,0xb,0x17,0x2b,0x71,0xa8,0x1d,0x6e,0x31,0x81,0xf5,0x85,0x1f,0xa4,0x3f, 0x6e,0x68,0xfb,0xc,0x69,0xa2,0xc2,0x83,0x79,0x4,0xf9,0xab,0x90,0x45,0xba,0xa5, 0xf6,0x45,0xbc,0x22,0xb7,0x65,0xbe,0x26,0x16,0xc0,0x9b,0x1b,0xdf,0x41,0x5a,0x4f, 0x29,0x56,0xda,0x92,0x78,0x9d,0x95,0x71,0x21,0x8f,0x9d,0xb2,0x55,0xd7,0xd7,0x4c, 0x1e,0x14,0xed,0xd5,0x79,0x2d,0x7b,0xf,0xed,0x18,0x2a,0xcd,0xd8,0x4,0x1d,0x2, 0xda,0xf7,0x14,0x53,0x15,0xaa,0x45,0xb6,0xb9,0xe2,0xe8,0xf,0x3a,0xc0,0x5b,0x58, 0xd4,0xc9,0x2e,0xcd,0xf6,0xaa,0x5c,0xe4,0x42,0x6,0xb2,0x9a,0xa,0x50,0x9c,0xe4, 0xc7,0xb0,0xb8,0x5d,0x5b,0x7d,0x14,0x95,0x60,0xfc,0xa4,0x9a,0x3d,0x80,0x73,0x91, 0x4a,0xa1,0xde,0x41,0xcb,0x3b,0x26,0x8d,0xc0,0xd8,0x28,0xca,0xa8,0x44,0x30,0x71, 0xf5,0x68,0xce,0xd0,0xe5,0x62,0x66,0xc5,0xde,0x8b,0xdf,0x1c,0xc,0x53,0x2d,0x56, 0x75,0xc,0x97,0xc0,0xc6,0x3d,0x4f,0x87,0x16,0xf6,0xd1,0x3f,0x3c,0x2,0xb0,0x32, 0x6a,0xfe,0x82,0xcf,0x61,0x69,0x95,0x40,0xf4,0x76,0xdb,0x1,0x49,0x9,0x57,0xbe, 0x94,0x6e,0x80,0x5b,0xab,0xcf,0x62,0x41,0x46,0x34,0x80,0x82,0xb6,0xb0,0xb4,0xa0, 0xaf,0xb7,0x71,0x90,0x21,0x86,0x50,0x16,0xfc,0x2c,0x96,0x47,0x35,0x6d,0x85,0x49, 0xdb,0x6,0xa4,0x7,0x55,0x86,0x48,0x9c,0xbb,0x49,0x1f,0x72,0xf9,0x54,0x13,0x2a, 0xc,0x4,0xba,0xac,0x8b,0x8b,0x42,0x8,0xb7,0xd8,0xce,0x6d,0x46,0x55,0xb6,0xa1, 0xda,0xdb,0xa8,0x31,0x62,0x70,0x4d,0x9d,0xb9,0xeb,0x10,0x34,0x40,0xa3,0x5e,0xcb, 0x27,0x98,0xf7,0xb2,0x24,0x3a,0xbb,0x5c,0x92,0x8a,0xc9,0x58,0x5f,0x0,0xf9,0x3b, 0xdb,0x22,0x6c,0xbe,0x93,0x39,0x5c,0xcc,0x25,0xec,0x1,0xe5,0x90,0xde,0x31,0x37, 0xf7,0x2a,0xea,0x9b,0xe3,0x26,0xf7,0xf6,0xb0,0x41,0x4f,0x11,0xc1,0x4a,0xcb,0x9d, 0xeb,0x38,0xdb,0xfe,0xf0,0x39,0x4c,0x16,0x26,0x4d,0x7b,0x36,0xac,0x2d,0x6d,0x24, 0xd6,0xd7,0x3f,0xba,0xfd,0xb7,0xb1,0x2f,0xf8,0x81,0xbf,0xba,0x4b,0x8b,0xd8,0x37, 0x43,0xb4,0x37,0x34,0x6d,0x83,0xc9,0x93,0x50,0x46,0x49,0x7c,0x73,0xb7,0x20,0x4a, 0x8f,0x60,0x84,0xe,0x18,0xb6,0x3d,0x11,0x38,0xfc,0x4c,0x83,0x8,0xa4,0x3a,0x4b, 0xd8,0xf0,0x7f,0x47,0xf3,0xc8,0xda,0x45,0x8e,0x25,0x41,0x81,0x5c,0x62,0x4b,0x6b, 0xc2,0xd0,0x79,0xda,0x7,0x36,0x6b,0x3f,0xb2,0x37,0x42,0xba,0x5b,0x7c,0x85,0x35, 0x6e,0x84,0x7c,0x62,0x4e,0xd6,0x27,0xdc,0x7b,0x69,0x5f,0xd7,0x4b,0xaa,0xc3,0x8d, 0xfa,0xbc,0xe7,0x2,0xf3,0xd2,0xc0,0x26,0xb,0x3,0x61,0x66,0x80,0xe6,0x1b,0xee, 0x6c,0x97,0xd0,0xba,0x6f,0xf8,0x17,0x6a,0xe1,0xf5,0x43,0x2d,0xa1,0x7,0x3a,0x1c, 0x43,0x22,0x1f,0x37,0xf4,0x5f,0xdd,0x7f,0x63,0x3f,0x66,0xe3,0x26,0x81,0x52,0x92, 0x99,0x23,0xcc,0x88,0x9b,0xe4,0xf2,0x7d,0xda,0xb5,0x2a,0xfb,0xbc,0x64,0x19,0x80, 0x6,0xb7,0xb7,0xfb,0x17,0x15,0xfa,0x7a,0x54,0xe0,0xdd,0x7b,0x63,0xaf,0x8d,0x7c, 0x53,0x5b,0x5,0xee,0x40,0xf7,0xec,0x9a,0xae,0x17,0x17,0xea,0xfb,0x30,0x6b,0x2, 0x67,0xa3,0x7d,0x7e,0x38,0x79,0x79,0x8d,0x5a,0xd6,0x9,0x3d,0x7,0x96,0xb9,0xd9, 0x71,0x3e,0x48,0x31,0xb6,0x35,0x4c,0x65,0xcc,0x63,0xcf,0xc8,0x93,0xbb,0x4a,0xfa, 0xde,0xc8,0xf8,0x17,0xc1,0xf1,0x24,0x9b,0x49,0x2d,0x59,0x50,0x44,0x92,0x2a,0x35, 0xd1,0x72,0x67,0x88,0x28,0xb3,0x6d,0x74,0x17,0xbc,0xbc,0x2a,0xf7,0x7,0xa4,0x56, 0x4f,0x1d,0x6e,0x90,0x10,0x12,0xac,0x59,0xbf,0x6,0xa9,0x83,0x98,0x53,0xb8,0xe9, 0x45,0x9f,0x72,0x6d,0x53,0x5f,0xe1,0xe9,0x9c,0x1e,0x93,0x94,0x26,0x38,0xeb,0xf4, 0x56,0xd9,0x86,0xe5,0xeb,0x33,0x3f,0xab,0xb8,0x68,0x2f,0xd0,0xbb,0xe8,0xbb,0x80, 0x88,0xad,0x6e,0x5c,0xe,0x50,0xc5,0x2a,0xee,0x5a,0xbe,0x15,0x12,0xaa,0xa,0xe7, 0x4,0x10,0xcd,0xf0,0xc2,0xd,0x1c,0x7b,0x75,0x4c,0x4d,0xb0,0xb4,0x88,0x32,0xbc, 0x36,0xa0,0x19,0xc3,0x70,0x5f,0xed,0x5f,0x39,0x2d,0xf3,0x4b,0xd7,0x7e,0x34,0x5c, 0xe,0x2,0x4d,0xd1,0x10,0x69,0xcc,0x5,0x35,0x99,0x36,0xe9,0xa1,0xe7,0xa7,0xd8, 0x8,0x40,0x1c,0x78,0x9f,0xb,0x58,0xd8,0x38,0xcb,0xa4,0x8f,0x4a,0xd8,0x6b,0xd8, 0xda,0xb8,0xaa,0x6a,0xa2,0xf6,0xef,0x57,0x11,0xa5,0x42,0xb2,0x8d,0x69,0x8b,0x95, 0xa9,0x28,0x8d,0xc9,0xb2,0x65,0x22,0x6a,0x32,0xc6,0x79,0xfb,0x1f,0xe5,0xd4,0x7a, 0x1e,0xfe,0xe4,0xc0,0x76,0x54,0x19,0x87,0xf9,0xda,0x3a,0x87,0x44,0x46,0x9c,0x6d, 0xed,0x2b,0x37,0xa0,0x90,0xd9,0xb,0x42,0x20,0x84,0x3f,0x40,0x6a,0x93,0xba,0x89, 0x93,0x1f,0xc9,0xa,0x74,0x62,0x11,0xed,0xbc,0xca,0xf5,0x1,0x90,0x92,0xee,0x7e, 0x3d,0xa5,0x1f,0xce,0x7f,0x2a,0x11,0xa0,0x2f,0xcf,0xe0,0x19,0x64,0x1b,0xa2,0xf7, 0x3a,0xec,0x81,0xae,0xce,0x92,0x1d,0x8c,0xdc,0x13,0xd,0x6e,0x25,0xfb,0xec,0x63, 0xa2,0xd,0xb1,0xa1,0xb6,0xc2,0x42,0x65,0x93,0xa2,0x7f,0x77,0xbd,0xa1,0x6f,0x78, 0xe,0x70,0xa6,0xdd,0x82,0xc3,0x6a,0x5f,0x56,0x77,0xcd,0x7c,0xf3,0x3b,0xdf,0x96, 0xc7,0x91,0x38,0x7e,0xd3,0xfa,0x64,0xe6,0x1d,0xe3,0x5e,0x5b,0x85,0x4d,0xd3,0x94, 0x3d,0x7a,0xf1,0xbf,0xbe,0x5c,0x9f,0x15,0x53,0xec,0x11,0x47,0x28,0xf0,0x5d,0x6f, 0x2,0x96,0xee,0x56,0x11,0xd2,0xbc,0xad,0xb6,0x9b,0x88,0xbb,0xe8,0x5c,0xcf,0xa6, 0x57,0xc1,0xe5,0x95,0x9d,0x85,0xaa,0xf1,0xf2,0xbc,0xb8,0x9a,0x2d,0x17,0xb,0xaf, 0x2d,0x79,0x85,0xbd,0x4c,0x42,0x6b,0x82,0xdd,0xf4,0x3e,0x47,0xd0,0x8e,0xed,0xa7, 0x50,0xd3,0x3d,0x6e,0xd9,0xe8,0xdf,0xcc,0x25,0x98,0xe6,0xd1,0xaf,0xf1,0x1,0x5c, 0x6b,0x6,0x1a,0x37,0x49,0x86,0xb9,0xa6,0xfa,0xf8,0x6d,0xcb,0x87,0x5b,0x74,0x57, 0xaf,0xb1,0xc5,0x9,0x1a,0xa5,0xd5,0xbe,0xbe,0xbc,0x11,0x6e,0x2f,0x91,0x4b,0x9a, 0x98,0x65,0xd2,0x61,0x6b,0x8c,0x8,0x66,0x5,0x76,0xb2,0xc,0x51,0xa6,0x64,0x80, 0x58,0xa9,0x89,0xf2,0xcf,0xde,0x31,0x8e,0x9c,0xc1,0x7c,0x4b,0x54,0xc7,0x65,0x6c, 0x2e,0xb7,0xcd,0x19,0x45,0x55,0x80,0xc9,0xcb,0xb2,0xd6,0x9d,0x59,0xba,0x1e,0x31, 0x64,0xa8,0xa3,0x34,0x87,0xd5,0x42,0xa3,0x17,0xbf,0xee,0x6b,0x7,0x55,0x57,0xb4, 0xd,0x25,0xce,0xd1,0x7b,0x4f,0x1c,0xc6,0x81,0xf2,0x64,0xda,0x2d,0x3,0xc,0x91, 0xab,0xb0,0x46,0x33,0x6,0x8,0x57,0x1d,0x47,0x46,0x9,0x4f,0x1b,0x60,0x4,0xa8, 0x86,0xd2,0xf9,0x81,0xa1,0x16,0xc7,0x23,0x9,0xac,0xfd,0xb5,0xaf,0x8a,0xc7,0x5b, 0x3b,0x8d,0xe,0x41,0x95,0xe4,0xdd,0xdd,0x2c,0xe6,0x2d,0xc6,0x48,0xb0,0xee,0x4e, 0x4,0xe9,0x4f,0xa5,0x0,0x17,0x49,0x89,0xc3,0xc6,0x3f,0xf2,0x51,0x7,0xcd,0xc, 0x94,0xdc,0xcc,0xaa,0x41,0xab,0x88,0xec,0x92,0x35,0xb4,0xda,0x65,0xa3,0xa8,0x69, 0x8d,0xf7,0x8f,0xe,0x10,0xd8,0x97,0x53,0x1f,0xd6,0x47,0x71,0x5e,0x15,0xfc,0x72, 0x71,0x4a,0x1d,0x33,0xf5,0xa5,0x20,0x8,0x5a,0xd4,0x63,0xc0,0xf8,0xc,0xa9,0x6, 0x5,0x39,0x14,0x94,0x12,0xab,0x67,0x32,0x3,0xae,0x23,0x61,0x44,0x9f,0xd3,0x35, 0xe9,0x71,0x68,0x5f,0x17,0x89,0xe7,0xf1,0xdd,0x4b,0x32,0x56,0xd6,0xdb,0x5d,0xdb, 0x16,0x71,0xef,0xa7,0x9d,0x58,0x59,0xa0,0x86,0xfb,0x81,0x4a,0x9c,0x55,0x0,0x6, 0x46,0xe7,0xe5,0x5e,0xf0,0xcd,0xcf,0xcf,0x19,0x81,0x26,0xef,0x5d,0x83,0x4c,0xf2, 0x75,0xbb,0x9b,0x13,0x14,0x74,0xb3,0x1b,0x71,0xb4,0x65,0x8d,0x89,0xe4,0x13,0xd0, 0xcd,0xf8,0xae,0xbe,0xc6,0x7e,0x8e,0x5f,0x0,0x35,0xcf,0xdc,0x38,0x9b,0xd0,0x2d, 0x57,0xeb,0x40,0xeb,0x60,0x73,0x7,0xd1,0x28,0xeb,0xde,0xb2,0xd1,0xf2,0x83,0x9f, 0xeb,0xb1,0xdd,0x33,0x30,0xec,0x92,0xaf,0x22,0xe1,0x8c,0xd9,0x7d,0xdc,0x8,0xd5, 0xc8,0xc7,0xc1,0xa9,0xbb,0x48,0x7b,0xe3,0x34,0xda,0x16,0x85,0xcd,0x19,0xa4,0x39, 0xca,0x83,0x6c,0x7a,0x70,0x7f,0x2a,0x12,0x61,0x37,0xeb,0xdf,0x14,0x73,0x35,0x5d, 0x3c,0xf6,0x7,0xf7,0xbe,0x2,0x5b,0x72,0xdc,0xf1,0xf8,0x2a,0xb,0x1d,0x64,0xd6, 0xa0,0xd0,0xd0,0x11,0x50,0xfb,0x23,0x32,0xb2,0x8f,0x12,0x46,0x3,0x47,0xa3,0xbe, 0xbd,0x2a,0x36,0x7c,0x2d,0x12,0x6e,0x89,0x4,0xe6,0xb4,0xf,0x5,0x98,0x65,0xa5, 0x69,0x37,0x37,0x3a,0xb2,0xd9,0x6c,0x65,0xe8,0xfd,0xab,0xec,0xc4,0xcf,0x2b,0x82, 0xf9,0xe1,0x7e,0xa6,0xf3,0x6c,0xb0,0xf7,0x54,0xe4,0x7,0x59,0x7d,0xec,0x7e,0x66, 0x24,0x35,0xa0,0x56,0x10,0x8c,0x3b,0xf8,0xa,0x66,0x65,0xce,0x36,0x11,0xd0,0xb0, 0xf2,0xce,0xd6,0xe6,0x3c,0x87,0xde,0x10,0x6c,0x65,0x69,0x69,0x52,0x67,0xd0,0xf5, 0x9d,0xf0,0xcb,0xad,0x7e,0x7,0x26,0x8,0x6e,0x8c,0x57,0xa4,0x9d,0xa7,0xd4,0x10, 0x77,0x2c,0xf6,0x33,0xb3,0x55,0x43,0xa0,0xba,0x2c,0x89,0x8d,0x93,0x5a,0x83,0x31, 0x4c,0xcf,0x5e,0x4a,0xd6,0x85,0x52,0x45,0x91,0x29,0x6a,0xae,0xd1,0x3f,0xbe,0x49, 0xea,0xb5,0xfb,0x9f,0xb,0x3f,0xbf,0x45,0x6b,0x49,0xd2,0x7e,0x24,0xd6,0x30,0x70, 0xa6,0x8e,0x3a,0x7d,0x93,0x8c,0x43,0xa4,0xb6,0xad,0x53,0x88,0x6c,0x12,0x51,0x58, 0x47,0x4d,0x77,0xd1,0xc,0xb6,0x18,0xf6,0x7f,0xea,0x75,0xa3,0x41,0xa5,0x93,0xe7, 0xb4,0xcd,0xe5,0x48,0xda,0x29,0xed,0x91,0x56,0xc0,0x99,0x42,0xd3,0x6a,0x9a,0x9a, 0xb7,0x91,0x6d,0x43,0x48,0x85,0x3a,0xc8,0xef,0x2f,0xeb,0xb1,0xd5,0x80,0x19,0xa, 0x4e,0x7e,0xd1,0x29,0x27,0x3f,0x3a,0x7d,0x1,0x53,0xc0,0x54,0xbd,0xda,0xee,0xf4, 0x6d,0xdb,0x38,0x35,0xe0,0xf1,0x7d,0x51,0x22,0x6a,0x3,0x77,0x6a,0x1c,0x1,0x38, 0x9b,0xd2,0x62,0xc2,0x13,0x1c,0xc0,0x93,0x70,0x1,0xe7,0xad,0xdb,0x56,0xa3,0xc8, 0x33,0x5b,0x7e,0x14,0xcd,0xfb,0xe4,0xef,0xe5,0xe7,0xe6,0x50,0x84,0xe7,0x89,0x9f, 0xba,0x6b,0xe1,0x4d,0x87,0xa2,0xe0,0x77,0xa3,0x48,0x26,0x0,0x9f,0x49,0x48,0x52, 0x24,0xc6,0x66,0xf1,0xc3,0xcb,0x61,0xa9,0xb3,0x48,0x7a,0xb7,0xaf,0x4,0x57,0x6b, 0x6f,0x3a,0x38,0x76,0x5c,0x1a,0xee,0x80,0x62,0x94,0x80,0x81,0xdd,0xc8,0xd3,0x81, 0x10,0xba,0x74,0x53,0x86,0xd5,0xfc,0x3a,0x9e,0xf6,0x72,0x4e,0xfa,0xc9,0x39,0xe9, 0x83,0xf1,0x61,0xe0,0x8b,0xcf,0x61,0xed,0x64,0xe1,0xef,0xc1,0x2a,0xc3,0x43,0xb9, 0xfd,0x37,0xd,0x84,0x8d,0xb,0x3f,0x2c,0x2,0xb1,0xf9,0x7d,0x7b,0xb3,0x67,0x7f, 0xa5,0x48,0x60,0x31,0x18,0xc1,0x9e,0xfb,0x23,0x8e,0xbd,0xcc,0xd2,0x81,0x87,0xd0, 0xb8,0x94,0x56,0x46,0x1f,0x95,0x72,0xa1,0xc6,0xec,0x1f,0xc1,0xa0,0x6,0x41,0x46, 0x4f,0xa1,0x77,0xe6,0xe2,0x16,0xe3,0x6,0x25,0xa1,0xd3,0xf7,0x23,0xda,0x48,0xdc, 0x6f,0x9e,0xa2,0xf,0xb3,0x16,0xb0,0xf9,0x82,0x4f,0xbc,0x23,0x55,0xfd,0x69,0x24, 0x20,0x60,0xc,0x3,0xf5,0x6f,0x89,0x1b,0x11,0xdc,0x92,0xb4,0xb7,0xdb,0x11,0xa6, 0xf9,0xb3,0xb5,0xae,0x49,0x66,0xa8,0xcb,0xb5,0xe4,0xee,0x8b,0xe3,0xd7,0xaf,0x83, 0x38,0x3b,0x86,0xae,0xaa,0x8f,0xc9,0x3c,0x6c,0xdc,0x70,0x24,0xb8,0x81,0xcb,0xb2, 0xb4,0x1,0xe0,0xfe,0x68,0x8a,0x4a,0x9d,0xee,0xb9,0xa8,0xd2,0x91,0xd8,0xd5,0x4a, 0x14,0xdc,0xf8,0x3f,0x6c,0x42,0x7b,0xd9,0x1f,0x6b,0x7d,0xd7,0xec,0xc8,0xb,0x21, 0xca,0xeb,0x20,0xb2,0xf5,0xea,0xcf,0xe5,0xa4,0x79,0x38,0xb5,0x52,0xf,0x7f,0xe5, 0x6b,0xf7,0x25,0xd7,0x3b,0x20,0x31,0xd9,0x8b,0xaf,0x32,0xf7,0xf7,0x3d,0x1a,0x42, 0xa8,0xb9,0xf4,0x9f,0xa4,0x45,0x5,0xc8,0xbe,0x3d,0xfe,0x90,0xcb,0x7e,0x76,0x37, 0xf6,0x1c,0x8f,0xb1,0x3c,0xc0,0x8b,0x48,0x70,0xbd,0xbf,0xe8,0x7a,0xd9,0x2b,0x24, 0x94,0xa0,0x43,0xb8,0xe5,0x48,0x2,0xa4,0x5,0x1,0xb4,0x51,0xfe,0x2b,0x8,0xf5, 0x47,0x97,0xa7,0x4,0x59,0xb3,0xcb,0x49,0xf0,0x8b,0x32,0x6c,0x66,0xdd,0x10,0x7a, 0x7e,0xd2,0xb2,0x64,0x9a,0xb4,0x88,0x9f,0x35,0x3d,0x70,0xb4,0xe7,0x79,0xaa,0x30, 0x90,0xd2,0xb3,0xe9,0x6,0xfe,0xb3,0xf6,0x8a,0x65,0xe2,0x70,0x43,0xf2,0x6a,0xc1, 0xc5,0x1e,0xa5,0x60,0x52,0x2e,0x80,0x8,0xea,0x70,0xbc,0xd3,0x69,0xe6,0x83,0xfa, 0x39,0xb6,0x64,0x3f,0xb5,0x18,0x37,0x40,0x7e,0x1a,0x31,0x41,0x8d,0x9b,0x4,0x53, 0x39,0x29,0x34,0x8c,0xd7,0x34,0x14,0xc2,0x24,0xd0,0x96,0x8e,0xb7,0x99,0x89,0x71, 0x50,0xed,0xb0,0x6,0x86,0xe7,0xc6,0x84,0x82,0xf7,0xc5,0x10,0x13,0x49,0xe2,0x4d, 0x73,0x17,0x59,0x4b,0xca,0x6d,0xe,0xef,0xbd,0x25,0x7e,0xf4,0x3e,0x87,0x66,0x8f, 0xf4,0x18,0x15,0x7b,0x7f,0x5b,0x0,0x2,0xd2,0xc6,0x12,0xe6,0x8f,0x75,0xb3,0x3, 0xc,0xd,0x4e,0xd7,0xf9,0xdc,0x47,0xb7,0x81,0x45,0xac,0xbf,0xcc,0x93,0xce,0x41, 0xab,0x64,0xbd,0x2b,0x3f,0x3d,0xad,0x13,0x83,0x3f,0x79,0x14,0xb4,0x2d,0x17,0xc1, 0x3a,0xe5,0x19,0xb3,0x42,0x60,0xea,0x43,0xa5,0x17,0x82,0xf1,0xaa,0xd1,0x33,0xd5, 0x36,0x70,0x2,0x75,0x2e,0x2f,0x8,0xb1,0x6e,0x81,0x45,0xa3,0xae,0xdc,0x65,0x68, 0xc2,0x7e,0x9b,0x84,0x5e,0x86,0xc7,0x4,0x9e,0x4a,0x75,0x49,0x1c,0xa8,0x20,0xd1, 0x99,0xa1,0xc7,0xc7,0xd0,0xcf,0xf8,0xbe,0xd1,0x3f,0x62,0x0,0x1c,0x47,0x69,0x5e, 0xc5,0x5,0x62,0x24,0x8c,0x2a,0xa7,0xaa,0xf3,0x9c,0xf3,0x90,0xc5,0x93,0x62,0x5f, 0xb4,0x2a,0xa6,0x5,0x7a,0x9f,0xc4,0xcb,0xde,0xa6,0xcb,0x7a,0xee,0x35,0x58,0x34, 0xba,0xba,0xd8,0xc6,0xe4,0x0,0x71,0x59,0x9d,0xe4,0xe9,0x63,0xf8,0x4c,0xc2,0xad, 0xf6,0x69,0x33,0xf0,0x88,0x77,0xbc,0x68,0x1e,0x88,0x62,0x8c,0x3e,0xbb,0xc1,0xf8, 0x76,0x1a,0xbf,0xdb,0x1a,0xb0,0x35,0xb7,0x15,0x1f,0x1b,0xe,0xea,0x5d,0x3c,0x61, 0xc6,0x6f,0x52,0x50,0xe6,0xf,0x38,0x5,0x18,0x9a,0x12,0x56,0x56,0xd3,0x4f,0x4d, 0xed,0x8e,0x29,0x87,0x3f,0xdd,0x40,0xd3,0x7c,0x5b,0xe2,0x67,0xb9,0x9e,0x49,0x0, 0xe,0x9b,0xcf,0xf4,0x2b,0x8,0x79,0x43,0x23,0x8b,0x99,0xf8,0xde,0xe8,0xc5,0x4c, 0xf6,0xee,0xd4,0xb5,0x4c,0x94,0x89,0xc8,0xef,0xeb,0xb0,0x29,0x8a,0xf9,0xa9,0x98, 0x15,0x79,0xd,0x40,0x2,0x87,0x3,0xa4,0x92,0x9c,0x9d,0xf1,0x5,0x64,0x3e,0xfb, 0xd2,0x92,0xb1,0x20,0x27,0xbb,0x68,0x97,0xa7,0x98,0xc0,0x33,0x92,0xe9,0x4b,0x28, 0x64,0x59,0x68,0xe5,0x60,0xeb,0x8a,0xf2,0x88,0xa7,0xe4,0x8e,0xc,0xa3,0xa,0x5f, 0xb5,0x3c,0xfe,0xdd,0xf7,0xe6,0x75,0x1f,0x80,0xb5,0xd1,0x13,0xa0,0x1e,0xba,0x84, 0x77,0xa3,0x6a,0xd7,0x8f,0xf4,0x4a,0x18,0x9c,0x30,0x26,0x29,0x53,0xb0,0x8,0x9, 0xec,0x86,0x66,0x64,0x6d,0xdb,0x3,0xed,0x12,0xd5,0x81,0x32,0xf3,0x3c,0xb6,0xea, 0xdf,0xa0,0xc2,0x6f,0x95,0x8c,0x8,0xb1,0x3c,0x2e,0x5a,0x8f,0x5e,0xe1,0x99,0xca, 0x68,0x7f,0x2f,0xd6,0xdb,0x33,0xc4,0xed,0x9,0x46,0x9f,0x7c,0x83,0x56,0x67,0x63, 0x76,0xa9,0x53,0xc,0x36,0x5b,0x3d,0x73,0x9,0x18,0x3,0x68,0xf9,0x1c,0x33,0xe2, 0x9c,0xe2,0xb9,0x78,0x95,0x7e,0xe5,0x1e,0x45,0x85,0x9a,0x48,0x5b,0x2,0xab,0xd1, 0xab,0x7e,0x5d,0x61,0xd9,0x1a,0xd4,0xe3,0x32,0x58,0xcb,0xac,0x74,0xfe,0x8f,0x90, 0xe1,0x49,0x88,0xf6,0x47,0x6e,0x15,0x8c,0x73,0xaf,0xd4,0xce,0x31,0x1,0xa0,0x5c, 0x7f,0x7d,0xbe,0xd9,0x98,0x93,0x3d,0x4a,0xeb,0x9,0xf6,0xe0,0x87,0x86,0xf0,0xe9, 0x4f,0x7a,0xe0,0x17,0x68,0xf6,0x23,0xdc,0xa6,0xf8,0xab,0x58,0x79,0xcc,0xb4,0x78, 0xc9,0x73,0xd1,0x62,0x87,0xf,0xad,0xf2,0x97,0x24,0x53,0x20,0xab,0x45,0xa,0x7a, 0xbf,0xea,0x91,0xa7,0x61,0xb5,0x84,0x88,0x2e,0xb0,0xe0,0x27,0x7d,0x95,0x1f,0x47, 0x89,0xf1,0x2a,0x90,0x1,0x57,0x83,0x99,0x7b,0x57,0x39,0xa6,0x9c,0x43,0x22,0xdb, 0xad,0x33,0x83,0x10,0xe8,0x88,0x98,0x96,0x39,0xf8,0x3d,0x36,0x8e,0x5d,0x7d,0x97, 0x4f,0x27,0x28,0xcf,0x7e,0x2c,0xe8,0xfa,0x83,0x22,0xa1,0x9f,0x65,0x43,0xfa,0x93, 0x77,0xfd,0x23,0xdf,0x86,0x3b,0xf6,0xbf,0x34,0x34,0xf5,0xc2,0x91,0xf3,0x5b,0x60, 0x9a,0x3,0x31,0x1a,0x2f,0x1a,0x94,0x32,0x3d,0x36,0x51,0x22,0xf9,0x4c,0x35,0x71, 0xca,0x58,0xd0,0x51,0x93,0xc7,0x91,0xc7,0xfc,0x7,0xb,0xe,0x7a,0xe5,0x6f,0x16, 0x68,0xa0,0x30,0x18,0x3a,0xc4,0x4a,0xf6,0x7a,0x1c,0x1a,0x74,0xe7,0xce,0x65,0xb2, 0x28,0x37,0x84,0x3b,0x7e,0x95,0x83,0xfa,0x9c,0x8e,0xa,0x18,0xf3,0x79,0xad,0x5c, 0x99,0x5d,0x74,0xd3,0x22,0x3f,0xcb,0x1c,0x5b,0x65,0x11,0x43,0x34,0xf5,0x76,0x5c, 0xac,0xfa,0x18,0x2c,0x90,0x9b,0x27,0xac,0xa9,0xb0,0x44,0x1d,0x2a,0xf1,0xf8,0xc3, 0x4f,0x6e,0x98,0xf0,0x2d,0xe3,0x8d,0x8,0x49,0x9e,0x4b,0x7d,0x94,0x41,0x5a,0xc1, 0x3c,0x72,0xed,0x4c,0xe,0x94,0xf9,0x37,0x46,0x3e,0x54,0x70,0xb0,0x4d,0xb4,0x7f, 0x3b,0xcc,0x71,0xe7,0xb0,0xfe,0xef,0xf9,0x1d,0xbb,0x77,0x31,0xfc,0xd1,0xf2,0xb9, 0xc3,0x60,0x6,0x51,0xf5,0x7f,0x88,0xbb,0x3e,0x5c,0xab,0xee,0x2a,0x60,0x6e,0xe4, 0xac,0x5f,0xcd,0x5d,0xdd,0x3d,0x57,0x7a,0x78,0x4f,0xac,0x76,0xa0,0x1f,0x30,0x65, 0x0,0xb5,0xb6,0x75,0x36,0xbf,0x31,0x74,0x1c,0xdc,0x63,0xc5,0xbd,0x51,0xab,0x6a, 0xb1,0xf8,0x48,0xf,0xb5,0x9f,0x8a,0x2f,0x6e,0xb6,0xa5,0x10,0x55,0x55,0x75,0x55, 0xb,0xab,0xca,0xc0,0x6b,0x7b,0x35,0x8,0xd8,0x18,0x4d,0x96,0x6a,0xf8,0x80,0x9b, 0x71,0xc8,0xaa,0x28,0xe8,0xb4,0xd6,0x57,0xea,0xfb,0xe6,0x41,0x51,0xdb,0x16,0xdb, 0x88,0x61,0x9d,0x73,0xdc,0x52,0x7b,0x35,0x6b,0xc9,0x4b,0xd5,0x42,0xcc,0xf0,0x34, 0x15,0x1b,0xdb,0xfd,0xd0,0xb2,0xd5,0x3b,0xae,0xbc,0x7c,0x0,0x19,0x13,0x5b,0xa1, 0x74,0x78,0x15,0xd0,0xcb,0x11,0x7,0x37,0x5a,0x52,0x8c,0x1c,0x9e,0x7d,0x50,0xb4, 0x98,0x2c,0x32,0xe8,0xde,0x87,0x25,0x8d,0xc4,0x21,0xd,0xdd,0xb3,0xe8,0x7f,0x28, 0x61,0x14,0x79,0xac,0xa4,0x80,0x63,0x7e,0x52,0xef,0x9b,0xf1,0xec,0xeb,0x26,0x86, 0x98,0x58,0xee,0xf6,0xe0,0x93,0x5,0x25,0xb5,0x12,0x3,0x69,0x7a,0x2,0x12,0x5c, 0x16,0x8b,0x9,0x3b,0x8b,0x6d,0xb9,0xdd,0xdc,0x55,0x4f,0xca,0xc1,0x75,0x51,0x5a, 0x4e,0xbf,0xd0,0xae,0x54,0xd5,0xd3,0x89,0x68,0xd6,0xf2,0xe2,0xd8,0x84,0x3f,0x6e, 0x8f,0x49,0xa9,0x1b,0x36,0x64,0x79,0x13,0x39,0x48,0xdd,0xfa,0xbe,0xae,0xd4,0x8c, 0x6f,0xa6,0x3b,0xc3,0x7c,0xf,0x4d,0xe4,0x65,0xbf,0x48,0xbd,0xc4,0x87,0x2c,0x54, 0x50,0x56,0xef,0x86,0xba,0xe8,0x9a,0xf3,0x31,0xf7,0x6f,0x6f,0xa7,0x44,0xfb,0x17, 0x6a,0xb6,0xda,0x67,0xc5,0xa7,0xcb,0xaa,0x67,0x14,0x68,0xab,0x9c,0x95,0x1,0x6c, 0xeb,0xf0,0xf3,0x26,0x59,0xe,0x99,0x8a,0x6,0x9,0x7a,0xad,0xcd,0x76,0xc4,0xb7, 0x2e,0x1f,0x9e,0x73,0x46,0x6b,0x1f,0x2e,0xfe,0x7,0xd9,0x1b,0x1c,0xda,0x88,0x87, 0x4b,0x7c,0xad,0x24,0x8a,0xc7,0xaf,0x90,0x50,0x2a,0xbe,0x1e,0x20,0x3,0x56,0xcd, 0x23,0xf4,0x42,0xe8,0xdf,0xe0,0x17,0xdf,0x67,0x71,0x7a,0x84,0xcb,0x3,0xc,0x18, 0xfe,0x3a,0x3c,0x89,0x2,0x6b,0x9a,0x52,0x15,0x59,0xf0,0x36,0xdb,0xc6,0x4,0xfe, 0xbb,0xc5,0x68,0x1c,0x26,0xfe,0x7b,0x8e,0x70,0xf5,0x13,0x3d,0xf9,0x1f,0xd4,0xf8, 0xd8,0x90,0x3,0xda,0xfc,0x1d,0xad,0x12,0xf5,0x9e,0xc7,0xd1,0x65,0xcc,0x51,0xa0, 0x12,0xb9,0xbc,0x39,0xb8,0xb7,0xc7,0x2a,0xae,0xda,0xe6,0x28,0x79,0xbb,0xa0,0x53, 0x4c,0xa3,0xad,0x49,0x40,0x5b,0xdb,0x36,0x79,0xa3,0x88,0xde,0xef,0xd9,0x0,0x3, 0x13,0x3c,0xbb,0xcb,0xf4,0x83,0x75,0x23,0xdd,0x5c,0x4b,0x57,0x18,0xeb,0x2a,0xe4, 0x10,0x58,0x2e,0x50,0xb3,0x89,0x7,0x2e,0xad,0x8f,0x8c,0x1d,0xe8,0xc,0x9f,0xfb, 0x49,0x5b,0x47,0xbd,0xde,0xbd,0xe0,0xbc,0x99,0x2c,0x94,0x32,0x97,0x3e,0x17,0xa7, 0x96,0xc4,0x78,0xca,0x4f,0xfe,0x78,0x7c,0xe,0x84,0x99,0xf6,0x91,0x3a,0xf2,0x5a, 0x95,0xb9,0x18,0xf4,0x77,0xf8,0xb1,0x91,0xa4,0xc5,0xc3,0x3c,0x84,0x5a,0x64,0x1b, 0x1f,0x5c,0x65,0xed,0xda,0xdd,0xe9,0xe8,0x63,0x84,0x5f,0x74,0xbe,0xd1,0xce,0xd3, 0x8b,0xe6,0xc8,0x4,0x5f,0xfa,0x15,0x4,0x40,0x58,0xbf,0xc4,0xb2,0xa3,0xe0,0x51, 0x0,0xc5,0xbf,0xda,0xa4,0xa9,0x43,0x87,0x2e,0xa2,0xfb,0x6c,0x74,0xca,0xc0,0x1, 0x31,0x89,0x84,0x90,0x4,0x99,0x14,0x45,0xf1,0x53,0x89,0x24,0xf7,0xe9,0x75,0xf7, 0xb0,0x35,0x53,0x55,0xdf,0x96,0x5c,0x8d,0x3a,0x58,0xfa,0x2e,0xa2,0xbb,0x2f,0x53, 0xc4,0xb3,0x63,0x49,0xcc,0x77,0xe,0x3e,0xca,0x97,0x62,0xc2,0x82,0xd8,0x3b,0x33, 0xe,0xe,0x8,0x6d,0xa4,0x64,0xfb,0x5e,0x3c,0x76,0xd,0x5e,0xb1,0x3c,0xb1,0xf5, 0x70,0x15,0x3f,0x3d,0xc,0x4d,0xfb,0x56,0xe5,0x5e,0x99,0x68,0x37,0xd4,0x1b,0xc5, 0xe2,0xa2,0xb2,0x7,0x7,0x2e,0xe5,0xc2,0xa4,0xf2,0x21,0xd5,0xae,0xd2,0xcc,0x1f, 0x67,0x8b,0xdc,0x73,0xd9,0xd8,0xc9,0x3f,0x37,0x63,0xa7,0xee,0xb7,0x42,0x34,0x1a, 0xe4,0xe6,0xa1,0x6b,0x16,0x87,0x2e,0x3a,0xf9,0x4f,0x90,0xa8,0xa1,0xdc,0xc8,0x9, 0x68,0x25,0xfb,0x42,0xfd,0xc5,0x81,0xb4,0xa9,0xa8,0x23,0xe0,0x6a,0x57,0xfb,0xce, 0xbe,0x1d,0x3a,0x54,0xa4,0xe7,0xe,0x9e,0x37,0x9e,0x47,0x58,0x7b,0x8f,0xe0,0xe4, 0xb4,0xdc,0xa6,0x32,0x23,0xa8,0x67,0xcc,0xd0,0x8a,0x2d,0x3c,0x62,0xa8,0xb,0x21, 0xc5,0xc5,0x75,0xe9,0xad,0x83,0x88,0x65,0x23,0x50,0xbd,0x1e,0x5f,0x9f,0x82,0x15, 0x7c,0xa9,0xc6,0x1f,0x52,0x2e,0x6b,0x23,0x39,0x99,0xde,0x9b,0x42,0xea,0x3c,0x88, 0xb0,0xb1,0x72,0x5e,0xb4,0x7b,0x43,0x57,0xcb,0x2,0x76,0x2b,0x21,0x78,0xbf,0x1d, 0x22,0x7,0x3d,0x74,0xb4,0xa8,0x18,0xed,0x42,0xf6,0x9,0x5,0xe1,0x45,0x8d,0x12, 0xf6,0x0,0xf0,0xac,0x7b,0x34,0x4,0xc6,0xb5,0xf9,0x72,0xd6,0x73,0xb1,0xf4,0x95, 0xb8,0x32,0x8a,0x6e,0x5a,0xa2,0xdb,0x1d,0x19,0xe5,0xa1,0x7b,0x2b,0x2f,0x8d,0xa2, 0xae,0x7e,0x4f,0xaa,0x33,0xd2,0xf0,0xe8,0x4d,0x63,0xc0,0xc0,0x95,0x35,0xd5,0x4e, 0xe6,0xdf,0x3c,0x41,0x2,0x19,0xdd,0x1c,0xfe,0x7f,0x97,0xa9,0xae,0x25,0x4c,0xdd, 0x24,0x1b,0x8,0xd6,0xee,0xf8,0xbf,0xbb,0xdc,0x0,0xfb,0x72,0x35,0x51,0x40,0x9b, 0x32,0x7d,0xdd,0x34,0x16,0xbb,0x50,0x94,0xbb,0x67,0x3e,0xe9,0xd,0x8b,0xc7,0x31, 0xa6,0x4f,0x87,0x15,0xc8,0x47,0x50,0x25,0xc7,0x4c,0x17,0x7c,0x9e,0x57,0x19,0xd0, 0x54,0x76,0x84,0xe9,0xb1,0x55,0x7e,0x6d,0xbc,0xbd,0x58,0xc9,0xc8,0x9f,0x7a,0x6f, 0xef,0x2,0x5,0xb8,0xc9,0x55,0xdd,0x91,0xa2,0xf4,0xe,0xc0,0xcb,0xa6,0x11,0xa0, 0x1d,0x95,0x8a,0xcf,0xea,0xa,0x3d,0x28,0xc7,0x15,0xf1,0x10,0xb5,0x6d,0xfe,0xa5, 0xee,0x4,0xdd,0xb8,0xd9,0x3b,0xc9,0xfb,0x30,0x58,0xbc,0x7b,0xfe,0xcd,0x1c,0x9c, 0xe2,0xa7,0x6c,0xce,0xb1,0x29,0xf6,0xf8,0x3f,0x68,0x9,0x74,0x55,0x87,0x1a,0x45, 0x8c,0x77,0x7d,0xe5,0xb2,0xc7,0xe1,0x62,0x9f,0x1e,0xdd,0x9e,0xeb,0xfa,0xba,0x4e, 0x22,0x27,0x1d,0x53,0xd0,0x93,0xcb,0x10,0x7c,0x54,0x4,0xd1,0xdb,0x1e,0x96,0x68, 0x15,0x15,0xcd,0xc7,0x5c,0xaf,0xa9,0xfb,0x4d,0x87,0x1a,0xb8,0x2,0xd5,0x8,0xa3, 0x7c,0x25,0xf6,0x4d,0x39,0xc2,0xdc,0xb5,0x17,0xe0,0x7,0xf3,0x7e,0x9e,0xdb,0x93, 0x33,0xaa,0xda,0x8f,0xd9,0x84,0xb,0x28,0x8c,0x25,0xe0,0x8e,0xfa,0xe8,0xb2,0x78, 0x8e,0xa9,0x45,0x47,0xec,0x23,0xfc,0x4,0x83,0x83,0x77,0x3,0x22,0x54,0x96,0x55, 0x7e,0xf1,0x64,0x58,0x76,0x6f,0x0,0x3,0x95,0xe1,0x12,0x10,0x4a,0xc4,0x8,0xd8, 0x6e,0x4e,0x20,0x5b,0x71,0x9c,0xdf,0x74,0x21,0x57,0x77,0xc2,0x2b,0x8e,0x19,0xa9, 0x80,0xfc,0x82,0xf6,0x6d,0x82,0xfa,0x82,0xe3,0xd,0x92,0x2f,0x51,0x9b,0x87,0xbf, 0x69,0xa8,0x9b,0x5a,0xc4,0x7b,0xce,0x65,0x52,0x47,0x29,0x7e,0xd5,0xc1,0xa7,0x56, 0xbe,0xa9,0xcc,0xab,0x2d,0x47,0x2e,0x90,0xd3,0x41,0xbf,0x25,0x5c,0x48,0x65,0xc5, 0x70,0x1,0x20,0xb4,0xfb,0xee,0x1b,0xcd,0x36,0xc3,0x4c,0x8b,0x85,0x74,0x61,0xc3, 0x1e,0x2f,0x70,0xca,0xf5,0x1e,0x5c,0xca,0x5f,0x9b,0x6f,0xbb,0x63,0xd4,0x81,0xd3, 0x55,0xa1,0x9,0x51,0x11,0x24,0x20,0x47,0xe7,0xeb,0x53,0xec,0xdf,0xb4,0x30,0xfe, 0x63,0xa0,0x49,0x5a,0x3f,0xa5,0x25,0x9e,0xc1,0x94,0xda,0x25,0xe9,0xdb,0x79,0x3f, 0xfd,0x82,0x11,0xf,0xa6,0xb0,0xd5,0xe,0x9c,0x29,0x7a,0xfc,0xde,0xaa,0xfb,0xc1, 0xcb,0xc4,0x1c,0xb,0x6b,0xc0,0xa9,0xac,0xd5,0x4,0xd1,0xbf,0xe0,0x4b,0x7e,0xde, 0x4d,0x8f,0x6d,0xf3,0x40,0x43,0x81,0x5d,0xec,0x7b,0x5a,0xcb,0x27,0xd5,0xd,0xf2, 0x9a,0x2a,0x7d,0x85,0x6a,0xa6,0x32,0xbf,0xab,0x84,0xfe,0xc,0x4f,0x7e,0x6a,0x9d, 0x8d,0xd7,0x11,0xce,0x9a,0x13,0xab,0x87,0x8e,0x6,0xd2,0x35,0x5b,0xe0,0x28,0xf5, 0x8a,0x25,0xfb,0xf4,0xcc,0x2e,0xb5,0x78,0x32,0xb4,0x84,0x82,0xb2,0x6e,0x20,0x41, 0x46,0x31,0x8f,0xe0,0xc3,0x3b,0x69,0x53,0xc0,0x3c,0x88,0x1c,0x1d,0x31,0x91,0xa7, 0x56,0x8d,0x1d,0x23,0x3c,0x52,0x1b,0x6e,0x7,0x1f,0x70,0x3a,0x8d,0x10,0x7b,0x53, 0x42,0xb,0x35,0x6,0xc5,0x1e,0xd8,0x86,0xd9,0x62,0x22,0xf7,0x13,0x33,0x1f,0x69, 0x41,0xbb,0xd,0x7d,0xe,0x28,0x6b,0x95,0xc7,0x5c,0xcf,0x55,0x6c,0x4b,0xa9,0x2e, 0xd5,0x5e,0xb4,0x9b,0x7c,0x8d,0xa1,0x56,0x6f,0xc3,0xcd,0x82,0x76,0x6d,0xec,0xb7, 0xa8,0x79,0xb4,0xb7,0x21,0xa0,0x4d,0xe8,0xfc,0x9c,0xbe,0x69,0x67,0xe7,0x98,0x3d, 0x46,0x4d,0x58,0x42,0xda,0xf9,0x18,0xca,0x3d,0x66,0x4d,0x33,0x53,0xb9,0xeb,0xfb, 0x33,0xa0,0xb3,0x55,0xc0,0x80,0xbd,0xbd,0x1d,0x7c,0x28,0x4,0xe3,0x40,0x41,0x2a, 0xd,0x19,0xeb,0x67,0x92,0x84,0x32,0xcf,0xea,0x80,0x4,0x3e,0xb9,0x6f,0x3a,0xed, 0x8f,0x6e,0xc2,0x51,0x6e,0x0,0x8e,0x8c,0x7d,0x36,0x10,0xe0,0x76,0xd1,0xc,0x83, 0xea,0x77,0xeb,0x7e,0xfb,0x1e,0xcd,0x66,0x1e,0x51,0x24,0xd8,0xc0,0xde,0x46,0x51, 0x4d,0x88,0x22,0xbb,0x88,0xb0,0xc7,0x85,0xe7,0xd8,0x67,0x5e,0x2a,0xf2,0x62,0x15, 0x6a,0xcd,0x13,0xe6,0x6b,0xe1,0xcc,0x8a,0x33,0xf1,0xe2,0x74,0xd0,0xa8,0xc5,0x9d, 0x31,0x67,0x59,0x39,0x18,0xa1,0xbf,0x0,0xf9,0xa6,0xde,0x24,0x99,0x41,0xb8,0x83, 0x8e,0xcc,0xe9,0xf9,0xae,0xb7,0x84,0x61,0x29,0xe6,0xd5,0xf9,0x8f,0x1b,0x97,0x40, 0x82,0x70,0x7a,0x1b,0x91,0xb9,0x1b,0x8b,0x60,0x79,0xaf,0xf9,0xba,0x69,0xfc,0x49, 0xb5,0xe7,0xc3,0x64,0x1f,0xc7,0x45,0x48,0xaf,0x9b,0x42,0xbe,0xb6,0x59,0x0,0xb9, 0x49,0xf9,0xd4,0xdb,0xb3,0x6f,0x67,0x14,0xe9,0x97,0x8d,0x24,0x80,0x8a,0xed,0x36, 0xf1,0xb1,0x1a,0x11,0x79,0x5f,0x59,0xa8,0xfa,0x1b,0x68,0x32,0x74,0xe7,0x6b,0xbe, 0x61,0x40,0x9a,0x15,0x2f,0x81,0xa8,0x19,0x19,0x36,0xbd,0x99,0xc0,0xab,0xcf,0x33, 0xdc,0xe9,0x44,0x56,0xc9,0x9e,0x7f,0x44,0xb9,0x67,0x76,0xae,0xce,0x61,0x6d,0x30, 0x21,0x87,0x45,0x51,0x88,0xed,0xe9,0xa2,0xa3,0xa7,0xbb,0xe3,0xd2,0xc,0x17,0xaf, 0x75,0x5c,0x86,0x3f,0xfa,0x85,0x4,0x34,0xec,0xf9,0xe2,0xbb,0x5c,0xcf,0x6b,0x7d, 0xd6,0xb0,0x4e,0x60,0x1e,0x39,0x82,0x41,0x60,0xbd,0x25,0x34,0xc9,0x3d,0x63,0x40, 0x99,0xe9,0xfe,0x14,0xee,0x3,0xc7,0xdb,0x7d,0x2b,0x17,0xd9,0xfa,0x82,0xd6,0x52, 0xb2,0x26,0x32,0x50,0xde,0x34,0x91,0x3f,0xf1,0xb7,0xf2,0x3c,0xf4,0x57,0xfb,0xe, 0xc0,0xfa,0x22,0xb0,0x7e,0x69,0xc,0xfb,0x94,0x24,0x55,0x10,0x26,0x2c,0x62,0xd9, 0x52,0x14,0xa9,0x31,0x48,0x3c,0xf0,0xb9,0xf3,0xe3,0xf5,0x68,0xba,0xf1,0x76,0xfb, 0x6d,0x18,0xac,0x6b,0x81,0x38,0xe6,0x96,0xdb,0x3c,0xa6,0x3,0x68,0x88,0x5c,0x3b, 0x9c,0x6,0xeb,0x64,0x42,0xdc,0x9d,0xb5,0x41,0x94,0x1e,0xfb,0x6,0x14,0xf7,0xf2, 0xab,0x24,0x5e,0xad,0x5d,0xc4,0x44,0x39,0x1,0x6a,0xbb,0xe9,0xf2,0x18,0xa4,0xf, 0x1f,0x90,0xf2,0xe0,0xed,0x90,0x97,0x2f,0xa4,0x35,0x2b,0x2b,0xc9,0xa3,0x1e,0x75, 0x47,0xfc,0xa2,0x24,0x41,0x66,0x5e,0xc2,0xd0,0x99,0xac,0xc3,0xb2,0xd0,0x52,0x51, 0x61,0x45,0x32,0xce,0x56,0x49,0xfd,0x7a,0x7f,0xa9,0xa5,0xc8,0x4d,0x44,0xbd,0x14, 0xc0,0x61,0x39,0x81,0xc7,0x17,0x44,0x99,0xb0,0x70,0xdc,0xe2,0x41,0xaf,0x34,0x23, 0xf4,0xe6,0xf1,0xca,0x30,0x70,0x46,0x2f,0x1a,0x6b,0xf7,0xe6,0x2f,0xb6,0xfa,0x6f, 0x18,0x34,0xf1,0x5f,0x4b,0x36,0x78,0xfc,0xa7,0xd5,0xdf,0x68,0x85,0x94,0x8b,0xf9, 0x7b,0xfd,0xc5,0x2b,0x6e,0x8b,0x5b,0x8,0x76,0xd2,0xee,0x26,0x89,0x69,0x95,0x21, 0x9e,0x7,0x1,0x69,0xbd,0x79,0xe5,0x65,0x4f,0x46,0x4d,0x54,0xda,0x59,0x4f,0xd5, 0x57,0x94,0x1,0x45,0x9f,0xdb,0x4d,0x16,0xaf,0xbb,0x3c,0xb8,0x25,0x52,0xda,0xc3, 0xd8,0x5b,0x2e,0x96,0x54,0x14,0x7b,0xa4,0x5a,0xc9,0x78,0xb4,0x23,0xc7,0x8a,0xf9, 0xdb,0xc,0x3f,0x7b,0xe7,0xc,0x12,0x97,0xc7,0xcd,0xd0,0xec,0x20,0x2b,0x31,0xf9, 0x86,0x5f,0x90,0xda,0xf2,0x8c,0xfe,0xcd,0x56,0x78,0x82,0xf8,0xbf,0x8d,0xf2,0x9c, 0x99,0xb1,0x97,0x81,0xbd,0xa9,0x99,0x5,0x78,0x6a,0xf1,0x18,0x95,0x23,0x12,0x9b, 0x2,0x23,0x76,0xf5,0xaf,0x76,0x43,0x85,0x6e,0xc5,0x7e,0x2e,0x53,0xf0,0x4a,0xec, 0xa2,0xe2,0xee,0xdf,0xc,0x8,0xe4,0x84,0x72,0x56,0x9d,0x87,0xf9,0x2f,0x23,0xfb, 0xd1,0x99,0x71,0x1,0x8f,0xb4,0x86,0xfd,0xfa,0x84,0xac,0x4e,0x75,0x76,0xbb,0x97, 0x59,0x2a,0x77,0xe5,0x32,0xdb,0x6a,0xa4,0xb2,0x87,0xab,0xac,0x37,0xce,0xa8,0x88, 0xe7,0x9a,0x8a,0x78,0x4f,0x90,0xf5,0x4a,0x16,0xa2,0x19,0xb,0x1a,0x54,0xa3,0xf2, 0x7e,0x9a,0xd8,0xb0,0xf6,0xc3,0x55,0xa9,0x4b,0x1,0x56,0x2,0x4f,0x7e,0x8b,0x37, 0x19,0x16,0xaf,0xe8,0x26,0x26,0xb2,0xbb,0xc8,0xcb,0xc7,0x62,0x20,0xea,0x56,0x1e, 0x5,0xae,0xce,0xfb,0x72,0x24,0x25,0x3e,0xa4,0xfa,0x40,0x73,0x7a,0x4b,0xab,0x13, 0xe0,0xda,0x7b,0x8,0x1,0x2f,0xc3,0x4a,0x7a,0x8b,0xac,0x1b,0xf5,0x3,0x39,0xfb, 0x32,0x9,0xf7,0xa4,0xac,0x1e,0x62,0xd1,0x98,0x23,0x45,0x13,0x6e,0x70,0xa6,0x50, 0x4c,0x22,0xd7,0x4d,0xd0,0x9b,0x97,0x4c,0xa7,0xc4,0xe6,0x9d,0x47,0x20,0x19,0x79, 0xa8,0x12,0x1f,0xd5,0xaf,0x1,0xa7,0x48,0x24,0x6c,0xdb,0x93,0xdd,0x2,0x63,0x2a, 0x24,0x3b,0xf6,0xf5,0x56,0xf,0xc1,0xfd,0xd3,0xa8,0x1c,0x1b,0x48,0x35,0x15,0x71, 0xc6,0x34,0x47,0xf5,0xb4,0x6e,0xbe,0xd9,0xda,0x9a,0xec,0x38,0x9c,0xcf,0xe1,0x40, 0xb,0xd9,0xb5,0xe0,0x68,0xf6,0xdf,0xbb,0x9f,0x7b,0x56,0x68,0xb0,0x6b,0xd9,0xf7, 0x1f,0xa0,0xed,0xd4,0xf,0xac,0x2e,0xe9,0xc6,0x1b,0xa2,0xe2,0xea,0x84,0x24,0x75, 0xdd,0x59,0x56,0x46,0x51,0xb5,0x81,0x70,0x31,0x58,0xd8,0x62,0xc3,0x32,0xd9,0x63, 0xd2,0xc7,0x38,0xe1,0xf4,0xe5,0x4c,0x3b,0x1,0xee,0x1f,0x6b,0x73,0xc2,0x60,0xd1, 0x1c,0xb6,0x97,0x6d,0xec,0x1a,0x5e,0x1e,0x72,0x37,0x0,0xb5,0xe9,0xd9,0x19,0xbc, 0x22,0xd0,0x1f,0x96,0x36,0xea,0xd1,0x37,0xd9,0xf0,0x22,0xcc,0x33,0x82,0x9e,0x50, 0xb9,0xb6,0x3d,0xa6,0xd0,0x9b,0x44,0xc2,0x53,0x45,0xf7,0x3d,0x9e,0x91,0x79,0x40, 0xe1,0x98,0xd6,0x19,0x83,0x29,0x50,0xdc,0x99,0xf2,0x2a,0xcd,0x75,0x48,0x9d,0x2f, 0xfe,0xda,0xd5,0x4f,0xf6,0x9a,0x91,0xc9,0x5f,0x8a,0x86,0xfd,0x1c,0x0,0xbe,0xfd, 0x19,0x15,0x17,0x9c,0x3e,0xe7,0xf9,0xd8,0x5a,0x24,0xa6,0x4f,0xeb,0x44,0x7f,0xeb, 0x9e,0xd4,0x3b,0x15,0x6f,0xcd,0xde,0xce,0xd7,0x65,0x4d,0xf3,0xe5,0x8b,0x71,0xfe, 0x20,0x9,0x1b,0x5f,0x70,0x94,0xb7,0xca,0xb8,0xdd,0x99,0xa5,0xa1,0x19,0x11,0xbf, 0x6e,0xcb,0xd5,0x5d,0x99,0x34,0xac,0xf0,0x1a,0x79,0x64,0x0,0x84,0xd6,0x7e,0xa4, 0x5f,0x99,0x4,0x4f,0x2f,0x3b,0x99,0x67,0x98,0x33,0x8c,0x3a,0xcc,0x9d,0xfa,0x3b, 0xe9,0x50,0x18,0x83,0x84,0x44,0xf4,0x9e,0xbd,0x59,0x1e,0x42,0x30,0x9c,0xe7,0xf, 0x37,0x6b,0x5e,0xe5,0x27,0xf7,0xcc,0xbf,0xab,0x5a,0xfa,0x78,0x77,0x75,0x33,0x61, 0xc5,0x4b,0x65,0xc9,0x90,0x5a,0xe8,0xcd,0xb3,0x7,0x90,0x64,0xa4,0xf7,0xf2,0x5b, 0xe2,0x52,0xc0,0xa,0xc9,0x8d,0xca,0x75,0x67,0x45,0xed,0x5f,0x3a,0x21,0x40,0x7f, 0xec,0x25,0x49,0xfc,0xfe,0xb1,0xca,0x33,0xb9,0x5b,0x97,0xdd,0xd2,0xa,0x39,0xb6, 0xdb,0xf9,0xc0,0xa6,0x7,0xb,0x9b,0x6f,0xcf,0xa,0x4e,0x89,0xaa,0x8e,0x9,0x97, 0xb4,0xd2,0x14,0xb3,0x84,0xdf,0x66,0x3e,0xba,0xfd,0x9b,0x8e,0x88,0xd4,0x45,0x64, 0x4e,0x85,0xb,0x56,0x11,0x27,0x45,0x60,0x31,0x13,0xea,0xdb,0xa1,0xf3,0xf3,0xd5, 0x46,0x8,0xa,0xcb,0x67,0x70,0x89,0xa2,0xee,0x26,0x31,0x77,0x7a,0xf5,0xdb,0xc9, 0xfa,0x67,0x9f,0x8b,0x8e,0x64,0xec,0x3f,0x77,0xd7,0x9a,0x19,0x4b,0xe,0x6f,0x92, 0x96,0x79,0xdd,0xfd,0x69,0xe6,0x20,0x58,0x8c,0x51,0x4f,0x8,0xc6,0x2c,0x51,0x42, 0x13,0x70,0xcd,0xa1,0xd4,0xba,0x60,0xcb,0x12,0xfa,0x64,0x5e,0xa,0xd3,0x70,0xa0, 0xcc,0xcd,0x1e,0x37,0xb4,0x3f,0xf,0xc1,0x10,0x5f,0x49,0x57,0xb,0x1a,0x99,0x1e, 0x8a,0xe6,0x3f,0xde,0x22,0x9f,0xaa,0x34,0x9a,0xf,0x12,0x24,0x63,0x82,0xc4,0x30, 0xcf,0x63,0xe6,0x5,0xa2,0x76,0xc6,0xb2,0xd5,0x10,0xa,0x60,0x2a,0x23,0xfd,0x34, 0xb,0x3d,0x13,0x2d,0x5c,0xbd,0x61,0x76,0x4c,0xf3,0x9b,0xaf,0xf5,0xdf,0x60,0xc6, 0x43,0x47,0xcb,0xe5,0x3d,0x92,0x99,0x13,0x22,0x23,0xf2,0x4c,0x47,0xf0,0x80,0xd1, 0xad,0x13,0xfe,0xa,0xd0,0xdf,0x81,0x9c,0xd3,0x1d,0x4d,0xca,0xfc,0xad,0x11,0xc0, 0x74,0xdc,0xa6,0xb2,0xee,0xbf,0x45,0x11,0xe3,0xb8,0xdc,0xaa,0xa9,0xdc,0x7c,0x58, 0xef,0xfa,0xe1,0x40,0xda,0x63,0xdc,0x2f,0x0,0xa9,0x79,0x7d,0xd6,0x8a,0x3e,0xcb, 0xe6,0xe4,0x7e,0xd5,0x25,0x43,0x66,0x88,0xfb,0x43,0x33,0x26,0x20,0x2f,0xfd,0x8f, 0xa9,0xdf,0xcf,0x4,0x44,0x2c,0x33,0x44,0xd6,0x2c,0xc1,0x2d,0x36,0x7f,0xf8,0x1d, 0xe4,0xf6,0x72,0xa,0x3b,0xd8,0x92,0xb6,0x9b,0x45,0xdc,0x3b,0xf3,0xda,0xca,0x9d, 0xbb,0x1a,0xa1,0x7f,0xc6,0x55,0x43,0x9d,0x1,0x85,0x4a,0x38,0x5,0x44,0xd4,0xe9, 0x3b,0x48,0x73,0xf5,0xa0,0x6,0xad,0x3d,0xca,0x8a,0xf7,0xbe,0xe5,0xc3,0xdb,0x21, 0x5d,0xfd,0xa0,0x24,0xd2,0xe3,0x41,0xd3,0x69,0x8c,0x8b,0xee,0x50,0x61,0xd8,0x8b, 0x29,0x4d,0x82,0xc9,0xd2,0x30,0x86,0x9e,0x3a,0x7f,0xdc,0x9f,0xc2,0x39,0xc0,0x9f, 0x37,0xe0,0x44,0xa,0xc5,0x85,0x5d,0xae,0x91,0xe9,0x9d,0xe1,0x4b,0xf6,0x6e,0xf3, 0xc3,0x70,0xbd,0x96,0x20,0xc4,0xb4,0x5a,0xc3,0x12,0x7a,0x6,0x4b,0x3b,0xa5,0x2, 0x1d,0xe9,0x8b,0x62,0xef,0xe8,0x11,0x81,0xd2,0x2f,0xe3,0x9d,0x26,0xd1,0x91,0xe9, 0x42,0xcf,0x0,0x62,0x94,0xb5,0x3c,0xd7,0x47,0xb6,0xdd,0x92,0x72,0x3,0x14,0x8f, 0xed,0x9f,0x71,0x5d,0x88,0x2,0x5e,0xdb,0x31,0x42,0x79,0xd6,0x14,0xc,0x40,0xd5, 0xdb,0x41,0xb7,0xef,0x76,0xf4,0xc7,0xbd,0x2b,0x25,0xcf,0x9d,0x28,0xe3,0xac,0x95, 0x3,0x1e,0xf2,0x8b,0x21,0x52,0x67,0xd1,0x94,0x61,0x29,0x29,0x6d,0x69,0xfe,0xc8, 0x2a,0xb7,0x38,0x20,0x2c,0x7f,0x5d,0x57,0xa4,0xac,0xf5,0xcc,0x90,0x22,0x63,0x93, 0x41,0x56,0x9f,0x62,0x28,0x86,0xb3,0xbd,0xe7,0xdc,0x66,0xd4,0x47,0xe4,0x9d,0xf0, 0x1c,0xd5,0x12,0x48,0x55,0xee,0x20,0x79,0x9c,0x16,0x47,0xac,0xb7,0x2a,0xc0,0xf8, 0x0,0x60,0xda,0x29,0x66,0x8f,0x66,0x4f,0x6c,0x4c,0x24,0x33,0x31,0xc2,0xa4,0x4e, 0x18,0x36,0x96,0xed,0x25,0xb6,0xe6,0xc1,0x4c,0xad,0x6f,0x5,0xd7,0x30,0x7d,0x58, 0x10,0x59,0x1,0x76,0x68,0xe6,0xc5,0x54,0x33,0x6a,0x8,0x64,0xac,0xac,0x32,0x44, 0xe2,0x49,0x32,0x87,0x7f,0x99,0x4a,0x4c,0x47,0x39,0xd0,0x9f,0xe8,0x4e,0xf7,0xf8, 0x27,0xf8,0xee,0x8f,0x5f,0x35,0x64,0x92,0x9f,0x6c,0x76,0x4c,0x98,0x29,0x10,0xfa, 0x72,0xc2,0x82,0xf1,0x5c,0xcc,0x3e,0xa3,0x85,0x8e,0x43,0x6e,0xdd,0xba,0xe6,0x84, 0xb3,0xd6,0x15,0x92,0x8b,0xf8,0xa4,0x2b,0x65,0x1c,0xf6,0x7d,0x45,0x7,0x78,0x37, 0x49,0xfa,0x29,0xa5,0x48,0xe7,0x4a,0xcd,0x76,0xd,0xbc,0xd3,0xc8,0xa3,0x59,0xfb, 0xf9,0xed,0x8f,0x85,0xe6,0x34,0x30,0xcb,0xcf,0xa6,0x49,0x94,0x2e,0x41,0xcb,0x77, 0x3c,0x75,0x9d,0x4,0x5d,0xe7,0x52,0x53,0x74,0xf,0x28,0x3d,0x32,0x1,0x3a,0xac, 0xee,0x49,0xb1,0xd5,0xfc,0xe2,0x21,0xcd,0x9,0x6a,0x62,0xb6,0x2b,0x2f,0xae,0xe6, 0x24,0x4c,0xeb,0x81,0xb3,0x3e,0x54,0x28,0xcc,0xfb,0xe5,0xfe,0xfc,0x9f,0xab,0xeb, 0xe8,0xdd,0x41,0xe5,0xc0,0x62,0xb3,0x49,0x4c,0x96,0x80,0x77,0x45,0x2f,0x5f,0x69, 0x7b,0xca,0x6a,0xae,0x9,0xbe,0xd6,0x55,0xbb,0xbc,0xd3,0x38,0xdb,0x0,0x25,0xc4, 0xdd,0x66,0x2b,0x1e,0x49,0x5e,0x67,0x95,0xf4,0xe7,0x8d,0xb9,0x17,0xec,0x23,0x12, 0xb7,0x8d,0xc0,0x40,0xcc,0x18,0x95,0x8,0x54,0x69,0x40,0x31,0x69,0x65,0x75,0x47, 0x4c,0xa0,0x65,0x95,0x0,0x4d,0xaa,0x74,0xb4,0x38,0x2f,0x4c,0xa4,0x52,0x5e,0x5c, 0x60,0x9f,0x1c,0xac,0x37,0x31,0xb4,0x8b,0x9b,0xf4,0x3c,0x84,0xda,0xb2,0x4c,0xa6, 0x53,0x31,0xbb,0x53,0x7e,0x66,0x48,0xb3,0x1f,0x77,0x0,0xc3,0x49,0xdd,0xa0,0xa9, 0xfc,0xbc,0x56,0x34,0xee,0x8a,0x40,0xa,0x0,0x7c,0xe,0xda,0x2f,0x5a,0x1,0x83, 0x8c,0xbc,0x56,0x8a,0xa2,0x9e,0x3e,0xc1,0x95,0xbd,0x86,0xdf,0x9c,0xa6,0x9,0x19, 0xe2,0xdf,0x4e,0x51,0x6a,0x8e,0x5b,0x6a,0xb,0xe9,0xc4,0x3b,0x44,0xc5,0x3e,0x50, 0x82,0x94,0x5b,0x26,0xb3,0x99,0x67,0x49,0xd7,0x6d,0xa8,0x74,0x14,0xb2,0xd,0x77, 0x92,0x5b,0xc8,0xfc,0x69,0xa4,0xe7,0x75,0x8e,0xac,0x30,0xd2,0x73,0x6e,0xa3,0x75, 0x82,0xfe,0x1b,0x36,0x98,0x83,0x0,0xef,0x70,0xa8,0xe3,0x85,0x5b,0xf1,0xfc,0x6d, 0x4d,0x45,0xea,0xb7,0xe9,0xd2,0xac,0x78,0x7f,0xdc,0xcb,0x72,0xca,0x6f,0x68,0xcc, 0x6e,0x83,0x4,0x86,0x86,0x83,0x77,0xf7,0x2c,0x5b,0xfc,0x8,0x4d,0x79,0x75,0x9b, 0xbe,0x60,0xd2,0x29,0xb2,0x7f,0xa1,0xb2,0xdb,0x6d,0x25,0xa6,0xdc,0x8d,0x73,0xca, 0x91,0xf6,0x52,0x97,0xf9,0xc9,0xf,0xa6,0x25,0x8b,0x2e,0x73,0x5,0x23,0x8e,0x44, 0x4,0x61,0xec,0xb6,0x60,0x8e,0x69,0xbb,0x7c,0xf,0x62,0xd8,0x9c,0x55,0xa4,0xad, 0xcc,0xf6,0xc5,0x46,0xc0,0xd4,0xec,0xe5,0x61,0x1b,0xd8,0xe5,0x3f,0x67,0x2a,0x43, 0x48,0x17,0x79,0xa8,0x26,0xe3,0x64,0x22,0xf2,0x46,0xfa,0xf,0x1c,0x1f,0x3d,0x68, 0x16,0x3,0xae,0xd6,0xd7,0x1c,0x3d,0x39,0xb6,0x16,0x20,0xf5,0xfd,0xc9,0xb8,0x46, 0x61,0x33,0x6f,0x7,0x17,0x53,0x29,0x89,0x1a,0xa3,0x98,0x36,0xc3,0xd5,0x1e,0xd9, 0xd8,0x4c,0x31,0x31,0x68,0xed,0x6a,0x20,0x83,0xa,0x95,0x81,0x54,0x4f,0x48,0x35, 0x2,0xb7,0x3c,0x19,0x8a,0xe4,0x22,0xa4,0x88,0xba,0x5a,0xcb,0x11,0x78,0xa6,0x69, 0xc5,0x57,0x9a,0xad,0xc4,0x85,0xcd,0x48,0xf,0xe3,0x4a,0x63,0x33,0x92,0x18,0x35, 0xc9,0x54,0xcd,0x54,0xb8,0xef,0x79,0x42,0x2a,0xd3,0xe,0x3b,0x4d,0x34,0x25,0x13, 0xb,0xbf,0x40,0xcf,0xc4,0xf,0x19,0xd4,0xf2,0x63,0xb7,0xa5,0x75,0xd0,0x5a,0xbe, 0xa4,0x28,0x13,0x5e,0x97,0x8c,0xa0,0xc1,0x61,0x2e,0x7d,0x2e,0xe2,0xa2,0xc0,0xed, 0x62,0x1,0x3e,0xa7,0x8f,0xd6,0x7c,0x82,0x3a,0xb3,0xa7,0x2f,0x84,0x2,0xed,0x2a, 0x2a,0x80,0x88,0x41,0x8d,0xa8,0x4,0x6e,0x56,0x81,0x9c,0xb8,0x24,0xdc,0x27,0x6, 0xdd,0x65,0xad,0x6e,0x3c,0xa9,0x70,0xf5,0x5e,0x19,0xa4,0xe2,0x9a,0x92,0x8c,0x45, 0x92,0x94,0x86,0x20,0x3d,0x8a,0xe,0x14,0xc,0xaa,0xcc,0xaf,0x87,0xf3,0xb6,0xe5, 0x59,0xe3,0xd3,0x15,0x8e,0x44,0xb,0x6c,0xdc,0x2f,0xce,0x78,0xc1,0x5c,0xbd,0x55, 0xf0,0x44,0xf4,0xae,0x4f,0x4,0xc2,0xda,0x2e,0x8f,0x8b,0x36,0x4,0xc1,0x1c,0xdc, 0xa5,0xef,0xf2,0xb3,0xb3,0x7d,0x20,0x91,0xad,0xef,0x89,0xee,0xcb,0x47,0xc3,0xbc, 0xb,0xb9,0x6b,0xd9,0x3d,0xad,0xb5,0x6b,0x3e,0xc0,0xa1,0xc1,0x82,0x3d,0x9e,0xa7, 0xac,0x91,0xdb,0xe0,0x8f,0x7b,0x72,0x3d,0xea,0x7b,0xab,0xb6,0x42,0x70,0xf3,0x4d, 0x2a,0x5f,0x28,0x67,0x8d,0x5d,0x52,0x4b,0x1e,0x74,0xd,0xa0,0xb1,0xab,0xc7,0xde, 0xbd,0xa3,0xbf,0x4d,0x20,0xb1,0xa,0xb,0xac,0xb5,0x42,0xee,0x26,0x36,0xbb,0x50, 0x15,0xe3,0x37,0xa2,0xc0,0x8a,0xed,0xde,0xfe,0xfa,0x7f,0x30,0xa7,0xc7,0x8e,0x65, 0x6b,0xcd,0x32,0xb,0xfe,0x3c,0x96,0xab,0xf1,0xd8,0x9a,0x19,0xf,0x57,0xe8,0x24, 0xba,0x21,0x47,0x7c,0x2b,0x35,0x5b,0xa9,0xb0,0x5b,0xd9,0xd7,0x23,0xe8,0x3d,0xe, 0xb6,0xee,0x1a,0xb6,0x2b,0xb0,0x62,0x1d,0x9,0x7d,0xb5,0x18,0xd4,0x1f,0xbb,0xf, 0xbf,0x82,0xb,0xea,0xb8,0x67,0x94,0xe8,0x42,0xed,0xc0,0xe4,0xd6,0x7d,0xf2,0x8e, 0x6c,0x8c,0xc4,0x97,0xbc,0xa6,0x34,0xc5,0x24,0x6a,0x5d,0x78,0x89,0x99,0x88,0x49, 0x1c,0x93,0xb3,0x54,0x7a,0x48,0x3d,0x3c,0xb5,0xfd,0x21,0xd,0x7b,0x94,0x1b,0x67, 0x21,0xdf,0x7e,0x5e,0x86,0xb3,0x24,0xab,0x9d,0x82,0xa3,0x27,0x9b,0x2c,0xef,0xb7, 0x40,0xa3,0xd,0x3a,0xeb,0xc9,0xf6,0x21,0xc8,0x18,0x2e,0xc3,0x2c,0x49,0xab,0xcd, 0x29,0x2a,0x2c,0x30,0x5d,0x50,0xdb,0xfa,0x52,0xfe,0x22,0xed,0x2c,0x12,0x26,0xeb, 0xb5,0x33,0xa5,0x21,0xfc,0x9c,0xc2,0x45,0x35,0xf0,0x89,0x61,0x3b,0x35,0x2f,0xe3, 0xde,0x5b,0x14,0x3d,0x2c,0x6f,0x38,0xfd,0x6f,0xda,0xec,0x1b,0x6c,0x13,0x86,0xa2, 0xc5,0xab,0x43,0x42,0xc8,0x6,0x8,0xfd,0x77,0x91,0xde,0x32,0x46,0x8e,0x16,0x25, 0xe9,0xaa,0xe1,0x95,0x99,0x1b,0x94,0x88,0x75,0x81,0x23,0xe1,0x14,0x29,0x4,0x59, 0xd5,0x48,0x9b,0x9e,0x4e,0x23,0x1c,0xc5,0xb4,0xfa,0xf7,0x7a,0x89,0x8e,0x20,0xf3, 0xb8,0x2,0x89,0x52,0x9c,0x9d,0x5b,0x12,0x9e,0x7e,0x74,0xb2,0x28,0x78,0x8b,0xfd, 0x40,0x28,0x1c,0x8f,0x4b,0xb7,0xd4,0x80,0xb2,0x4d,0x7a,0xbc,0x5b,0x9a,0x30,0x14, 0x1d,0xb9,0xe5,0xb9,0xd7,0x41,0x4c,0x76,0x40,0x40,0x2a,0x68,0x38,0xb5,0xe5,0x79, 0x5d,0x81,0x88,0x29,0x39,0xdc,0x29,0x6b,0x2a,0xa3,0x28,0x5,0xbe,0x58,0x98,0xdb, 0x92,0x7f,0x15,0x6a,0x40,0xe0,0xe0,0x80,0x21,0x8a,0x68,0xd9,0xc0,0xcd,0x53,0x9d, 0x4f,0xdb,0xc6,0x88,0xb8,0xef,0xf4,0x63,0x14,0x9c,0x68,0xd2,0xf5,0x2,0x2e,0x8, 0x1,0xc2,0xf1,0x41,0xa4,0xd2,0x42,0x45,0xdd,0x2a,0x1f,0x9e,0xf8,0xf1,0x3c,0x48, 0xcd,0x83,0x51,0x7,0xf2,0x46,0xe9,0x86,0xe2,0x52,0x59,0x58,0xd3,0x7,0x60,0x54, 0xca,0x52,0x16,0xee,0xa5,0x58,0xb3,0x83,0x2,0x53,0xa1,0xfa,0x45,0x5d,0xc3,0x93, 0x60,0x15,0x9a,0x54,0x5b,0x4,0xda,0xbd,0x56,0xb4,0x17,0xaa,0x3b,0x77,0x7e,0x6, 0x4a,0x94,0x74,0x6f,0x6c,0xa8,0xf2,0x6f,0xfb,0x14,0x6a,0xc0,0xf0,0xad,0x54,0x52, 0xc2,0x6e,0x26,0x1e,0x72,0x80,0xdc,0x49,0x35,0x73,0x73,0xf0,0x6a,0xf1,0xf6,0xb4, 0x87,0xeb,0x24,0x73,0x94,0x96,0xe2,0x10,0x2a,0xcd,0xd0,0x1c,0x7b,0x26,0xed,0x3f, 0x14,0x14,0xdc,0x87,0x94,0x39,0xd0,0x4a,0xac,0xc3,0x3b,0x97,0xb5,0xb1,0x4c,0xbc, 0x1d,0xf0,0x31,0xb1,0x87,0x93,0xc1,0x32,0x61,0x13,0x4e,0x5d,0x39,0x3c,0x1c,0x4d, 0xcf,0xf8,0x54,0x64,0xb2,0xa4,0x2e,0xde,0x68,0x69,0x76,0x9e,0x9b,0xc3,0x5b,0xb8, 0x34,0xc,0xea,0x3b,0xa0,0x2c,0x6d,0x81,0x3f,0x3b,0xde,0xf7,0x77,0x7a,0xc5,0x47, 0x74,0x1a,0x2c,0x27,0xbf,0xd9,0x85,0xa7,0x44,0xfc,0x46,0x5f,0x40,0x22,0x97,0x74, 0xad,0x82,0xaf,0xcd,0x2f,0x9d,0x50,0xed,0xd8,0xae,0xe6,0x51,0x2a,0xac,0x18,0x1e, 0xc6,0xc3,0xc4,0x6,0x9e,0x4a,0x2e,0x62,0x47,0x74,0xc1,0x87,0x16,0xd8,0x7b,0xc4, 0xdb,0x2c,0x12,0xb,0x49,0x62,0xf8,0x22,0x91,0x5f,0xf2,0x3b,0xc,0xc,0xd8,0x53, 0x4f,0x9d,0xd8,0xed,0x67,0x7,0xcf,0xaf,0xfb,0x11,0xb6,0x12,0xea,0x33,0x56,0xc6, 0xde,0x69,0x51,0x28,0x4b,0xc9,0xc9,0x5c,0x2a,0xbd,0x17,0xb5,0x49,0xef,0x9,0x98, 0x8d,0x62,0x7,0xf5,0x69,0x56,0x25,0xe4,0x68,0x5b,0x77,0xd2,0xe,0xcd,0x99,0xec, 0xb6,0x6a,0x94,0x82,0x34,0xde,0x5e,0xdd,0x9c,0x76,0x94,0xe5,0x66,0x1d,0xfd,0xf4, 0x7f,0x84,0x6a,0xe9,0xdb,0xf,0xce,0x44,0x6a,0x46,0x17,0x79,0x94,0x30,0xe5,0xca, 0x1a,0xfa,0x4d,0xcd,0xd9,0xac,0xac,0x76,0xa2,0x41,0xdb,0x9,0x5e,0x59,0x7d,0xde, 0xde,0x67,0x48,0xba,0x76,0x96,0x7e,0xe1,0xdd,0x15,0x5b,0xf1,0x45,0xc0,0xbc,0xde, 0xbb,0x8a,0xac,0x15,0xb6,0x59,0xb,0x59,0x1a,0xe6,0x62,0x79,0x41,0x60,0xd7,0x9f, 0xc7,0x20,0xd9,0x3f,0xb6,0x58,0xa0,0x14,0x6d,0x7b,0x6,0x32,0x3c,0x43,0x11,0x78, 0xcd,0x3d,0x8d,0x4,0x97,0x99,0x5d,0xb1,0x0,0x3f,0xaa,0x41,0x9f,0x82,0x60,0x68, 0x22,0x3a,0x27,0x59,0x92,0xc7,0x6d,0x7f,0x43,0xf3,0x31,0xfe,0xb6,0xc1,0x77,0x4, 0x0,0x6,0x8,0x97,0x9f,0xe4,0xc8,0x9f,0x24,0xf3,0x61,0x44,0xf5,0x41,0x2c,0x19, 0x7c,0xd2,0xf1,0x8e,0x9a,0xde,0x8e,0x5d,0xd2,0xbf,0x5c,0x9,0x82,0xd4,0xd,0x82, 0x5a,0x94,0x99,0x79,0x79,0xe1,0x19,0x1e,0xd5,0xf9,0xe1,0xcc,0x3c,0xe,0x65,0xb8, 0xe0,0x57,0xc6,0xfa,0x36,0x55,0xd7,0x89,0x16,0x34,0x12,0x18,0x88,0x20,0x1a,0x62, 0x34,0xb3,0xdb,0x2e,0x15,0xf5,0x4c,0x6b,0x6f,0xad,0x38,0xab,0xbb,0x1d,0xe3,0x1c, 0xf3,0xab,0x96,0xa9,0x1,0x6e,0x33,0x96,0x22,0xc5,0xae,0x2b,0x65,0xc8,0x8d,0x99, 0xfb,0x6a,0xc7,0x12,0xdf,0x93,0xfc,0x4f,0x41,0x35,0xfb,0x7c,0xd1,0x5f,0x18,0xc5, 0xb,0xae,0x6f,0x8c,0x9c,0x23,0xa2,0xbf,0xe8,0x52,0x6a,0x4e,0x9a,0xf7,0x67,0x97, 0xe1,0x30,0x29,0xc1,0x43,0x26,0x12,0x85,0xda,0x8d,0x2,0xac,0xec,0x1b,0xf1,0x78, 0x49,0xe0,0x84,0xe6,0x4,0x27,0x26,0x6c,0x79,0x90,0x3a,0x15,0x8,0xa2,0x2c,0xea, 0x52,0x55,0xac,0x95,0xfa,0x3e,0x9a,0xd5,0xcb,0x9d,0x2,0x39,0x38,0x73,0x31,0x1, 0x54,0xb5,0xe7,0xd8,0xdc,0x8d,0xc4,0xd6,0x9d,0x0,0x6b,0x26,0x22,0x97,0x11,0x74, 0x6c,0x3d,0xa,0x67,0xfb,0xa5,0xbc,0x47,0xc2,0xbe,0x80,0x7a,0xb1,0xb1,0x7b,0x6, 0x67,0xe3,0xde,0xc4,0x71,0xa4,0x9b,0x8f,0x24,0x7,0xb5,0x46,0x1e,0x46,0xba,0x8a, 0x83,0x44,0x71,0x7f,0x69,0x2e,0xc7,0xab,0x6c,0xc7,0x26,0x1e,0xf9,0x22,0x24,0xe0, 0x6,0x83,0xa5,0x77,0xa7,0xc0,0x7,0xcb,0xc7,0x3c,0x91,0xe5,0x82,0xcb,0xef,0x7, 0x10,0x61,0x6,0xf9,0x8f,0x4d,0xa5,0xfb,0x95,0x4c,0x99,0x8f,0x6e,0xbe,0x70,0x74, 0xc1,0x17,0x6b,0x69,0xd7,0xf2,0xb4,0x20,0x2f,0xc5,0x85,0xb2,0x91,0x76,0x39,0xa1, 0xd7,0xbe,0x1b,0xe7,0x8c,0x41,0x63,0x22,0x8d,0xfd,0xb1,0x7b,0x3c,0x22,0xef,0xfd, 0xb8,0xda,0xe6,0x11,0xcd,0x1b,0x31,0xfd,0xe0,0xb6,0x30,0x72,0xac,0xe8,0x93,0x5, 0xa7,0x2f,0xec,0x34,0x70,0xcf,0x56,0xfd,0xcd,0x87,0x79,0x89,0x2a,0xe8,0x7,0xe2, 0xc3,0xed,0xf3,0x12,0x88,0xa4,0x10,0x69,0xdb,0xbf,0x5b,0x88,0xa8,0x6f,0x8d,0xcf, 0x9e,0xf9,0x5,0xf,0xca,0xda,0x8c,0x18,0xe2,0x85,0xa2,0xd,0x6e,0xa9,0xef,0xb1, 0x18,0x64,0xc3,0xa0,0x88,0x53,0x8a,0x64,0x13,0x65,0xed,0x3b,0xd4,0xfa,0xc,0x73, 0xf5,0x90,0x2,0x40,0xea,0x8e,0x58,0xcd,0x14,0x7a,0xda,0x2,0xa4,0x4b,0xb4,0xbc, 0x2f,0x78,0xdc,0xb7,0xcc,0x67,0x1d,0x5f,0x4d,0x8a,0x9b,0x22,0x5,0x27,0x16,0x7a, 0xb7,0x18,0xba,0x22,0xa7,0x93,0xf0,0x3b,0x8d,0x4b,0x3e,0x32,0x96,0xf2,0xee,0x45, 0x6b,0xcc,0xfd,0xb7,0xb3,0x9a,0x18,0x1,0x25,0x33,0xa3,0x2a,0x5a,0xb9,0xa5,0x91, 0xd1,0xdf,0xb3,0xf8,0xf2,0x24,0x35,0x81,0x70,0xf2,0xb3,0x86,0xe5,0xa3,0xcc,0xd0, 0xef,0xca,0x89,0x23,0x65,0x21,0xa4,0xa,0xd3,0x48,0xb3,0xad,0x2,0xd8,0xbe,0x53, 0xb9,0x72,0xcc,0xac,0x17,0x2,0xad,0x87,0xf4,0x62,0xe,0x5a,0x85,0xda,0x2b,0xf4, 0x25,0x34,0x18,0xa,0xd4,0xbc,0x14,0xa8,0x84,0xc8,0xd5,0x86,0xa1,0x94,0x5a,0xda, 0x87,0x27,0x8,0x9e,0xa8,0xb5,0xa5,0x1d,0x18,0xb3,0xf6,0x1d,0xf,0x22,0x12,0x34, 0xd6,0xaa,0x3f,0xab,0xe6,0xd2,0xd4,0x6c,0x1b,0x2a,0x72,0xbd,0xbf,0xcc,0x18,0xc6, 0x73,0x20,0xe4,0x9b,0xd6,0x8a,0xb8,0x6e,0xbd,0xaf,0xc,0xcc,0x52,0x1e,0x81,0xa8, 0xc8,0x40,0x54,0xb0,0x13,0xa8,0x9c,0xae,0x53,0xf,0x6c,0x92,0x5c,0x84,0x59,0xcf, 0x25,0x3e,0x6c,0x7b,0xc8,0xa4,0xe9,0x86,0xd4,0xf5,0xd3,0x27,0x94,0xd4,0xcf,0xdc, 0x15,0xa3,0xd,0xa7,0xcc,0xa9,0x56,0x20,0xb9,0x42,0x32,0x16,0x47,0x8b,0x65,0x6c, 0xc9,0xd1,0xe7,0x12,0xf6,0x51,0x18,0xcb,0xc7,0x6b,0x72,0xdb,0x40,0xc1,0xb8,0xd4, 0xe4,0xc6,0xfc,0xb1,0x70,0x53,0x51,0xa9,0x16,0x83,0x3f,0xdc,0x8e,0xa5,0x49,0xd7, 0xf6,0xb0,0xe9,0xed,0x81,0x82,0x39,0xc8,0xed,0xab,0xa4,0xae,0xec,0x5e,0x83,0xd2, 0xa4,0x80,0x4,0x15,0x54,0xd5,0x3f,0x6a,0xd8,0x7e,0xc6,0x68,0xa3,0x10,0xbf,0x9b, 0x40,0x2a,0x9,0x41,0xac,0x43,0xb,0x1a,0x6e,0xaf,0xc8,0x5c,0x8d,0x4d,0xae,0x32, 0x4d,0xb2,0xc7,0xa1,0x8,0x7,0x8b,0xe1,0x5,0x52,0xc9,0xa9,0xe1,0x89,0x45,0xa1, 0xb3,0xcd,0xe3,0xdf,0x11,0x6e,0xfa,0x0,0x9d,0xc3,0x5c,0x2c,0x90,0xb,0x5e,0xde, 0x3d,0xa5,0x0,0x46,0xac,0x8c,0xa7,0x32,0x5e,0x71,0xdb,0xc0,0xfa,0xa0,0x62,0x2f, 0xed,0xc5,0xf,0x0,0x34,0xa,0x0,0xd2,0x4e,0xdb,0x7e,0x5e,0x66,0xdc,0x3d,0xa3, 0x3,0xbd,0x69,0x2f,0x4a,0x11,0x61,0x28,0x82,0xbc,0xe8,0xfd,0xdc,0xcb,0x2d,0xcb, 0x91,0xbb,0x4b,0x46,0xc6,0x4b,0x98,0x94,0xa6,0x17,0xf2,0xd,0x73,0x31,0x30,0x76, 0xee,0x1a,0xa6,0xb8,0x2b,0x8,0x60,0x2e,0x45,0x4a,0xab,0x22,0x95,0x58,0xed,0x27, 0x14,0x39,0x6d,0x5a,0x4,0x85,0xee,0xaa,0x9c,0xe2,0x37,0x11,0x93,0xe7,0x87,0x2, 0x2,0x2e,0x3a,0xac,0xb6,0x9a,0x5a,0xfb,0x64,0x85,0x9d,0xf9,0xdd,0x8c,0xa1,0xf2, 0x45,0x8e,0xcc,0xc9,0x15,0xbc,0xf3,0xb1,0x1f,0x2c,0x42,0xb2,0x93,0xca,0x34,0x95, 0x78,0x6e,0xc1,0xae,0x88,0x1d,0x2a,0x6d,0x22,0xc8,0xe6,0x1,0xd4,0x88,0x73,0x99, 0x97,0x40,0x63,0x2c,0x7c,0x58,0x5d,0x9b,0x4,0xa0,0x4e,0x97,0xea,0x82,0xac,0xe2, 0x70,0x6e,0x92,0x79,0xb,0xbc,0xe6,0x2e,0x85,0xcd,0xae,0xd9,0xd6,0x22,0x74,0xed, 0xe1,0xd7,0x1a,0x5f,0xaf,0x77,0xfa,0xb3,0x97,0xc9,0xca,0x2,0xcb,0x77,0xe5,0xbc, 0x66,0x78,0x36,0x71,0xb4,0x1d,0x1f,0xba,0xea,0x4d,0x94,0x41,0xee,0x88,0x2f,0xd1, 0x61,0xc8,0xb0,0x90,0xc0,0x2b,0x45,0x58,0xf4,0x8f,0x5b,0x41,0x8,0xc0,0xfd,0x6e, 0x39,0x34,0x5f,0x6d,0x51,0xfe,0x28,0xbb,0x4c,0x3d,0x7d,0x3c,0xc5,0xac,0xe,0xa6, 0xf5,0xbe,0x38,0xb6,0x69,0xfc,0x8e,0x5f,0x8c,0xe9,0xa0,0x14,0x2a,0x1e,0x82,0x63, 0x52,0x62,0x51,0x23,0x61,0x79,0x5e,0xad,0x36,0x5b,0xe9,0xfc,0x9,0x77,0x23,0x7e, 0xb5,0x5b,0x35,0x20,0xd7,0xc3,0x7f,0x65,0x2e,0x9f,0x79,0x58,0x3d,0x7c,0x3c,0xf, 0xde,0x8d,0x32,0x40,0x86,0x10,0x6d,0xbd,0x6c,0x58,0x3a,0xf4,0xcf,0x5d,0x73,0x6, 0xb9,0x28,0x26,0x91,0xeb,0x25,0x76,0x1a,0x44,0x70,0x73,0x81,0xec,0xaf,0x90,0x4b, 0xbc,0x42,0xb,0x43,0xd1,0x78,0x1,0xbd,0xd0,0x3b,0x32,0x21,0x19,0xa5,0x27,0xd2, 0xcd,0xcc,0xe3,0x3a,0xf1,0xda,0x54,0x36,0x4b,0x47,0x37,0xb7,0x76,0xc7,0x3,0x33, 0x89,0x8d,0xf6,0x5b,0x6,0x77,0x99,0x57,0x33,0xcb,0xf7,0x4c,0x72,0x1f,0x9e,0xbf, 0x6b,0x2,0x79,0x5d,0xdc,0x4e,0x13,0xa7,0x95,0x4a,0x5f,0x8c,0x91,0xe1,0x3f,0x9a, 0x6f,0x36,0xf5,0xf5,0xae,0xf,0x4d,0xe1,0xdb,0x45,0x2e,0xcd,0xe3,0x4c,0x8d,0x4f, 0x4e,0x87,0x2c,0x2c,0xd5,0x3f,0xd3,0xea,0x9,0xb3,0x77,0x9a,0x15,0xb7,0x35,0x5, 0x6d,0xaa,0xfa,0x9b,0xba,0x48,0x7d,0x96,0x8d,0x2b,0xe3,0xf0,0x77,0x71,0x40,0xc6, 0x78,0x6c,0x72,0x4e,0x2b,0xc5,0x3a,0x34,0xf8,0x31,0xce,0xf,0x68,0x83,0x14,0xd6, 0xad,0x8e,0x72,0xe7,0xd6,0x70,0xfd,0xe3,0x9b,0xe1,0xd4,0x93,0xd3,0x94,0xd9,0x4c, 0x1,0x4c,0x9b,0xab,0x91,0x55,0xdf,0x8b,0x6,0x2e,0x9a,0x6f,0xb1,0x2e,0x46,0xde, 0xbc,0x38,0xc7,0x13,0x28,0xc5,0x76,0x44,0x28,0x4b,0xd7,0xfb,0x5f,0x31,0x48,0xdf, 0x7d,0x63,0x8b,0xf,0x38,0x6b,0x1a,0x3f,0x99,0x34,0xae,0xca,0x62,0x74,0xa9,0x9e, 0x2c,0xf0,0x31,0x55,0xb7,0xa7,0x99,0xdf,0xf2,0xf0,0x5b,0xd1,0x22,0x23,0xb1,0x9f, 0x87,0x3d,0x2e,0x3f,0xa8,0x49,0x7e,0x42,0xfc,0xac,0x8c,0x60,0xa0,0x37,0x7e,0xcd, 0x28,0xb0,0x23,0x5f,0x58,0x3c,0xbe,0xcb,0x2d,0x1a,0x9d,0x4f,0x3e,0x50,0x6e,0x45, 0x8d,0x9c,0x84,0xb6,0x65,0x83,0x78,0x63,0x30,0x6,0x43,0x51,0x3d,0x41,0x1f,0xe4, 0xf1,0xc1,0x45,0xca,0xfd,0x83,0x96,0x2b,0x9e,0xb3,0x7a,0x5c,0x83,0xe8,0x21,0x91, 0x5,0xa5,0x48,0xea,0xa8,0x40,0x4e,0x59,0x46,0x11,0xaa,0x3,0x52,0x49,0xe8,0xc4, 0xb,0xad,0x8f,0x9,0x31,0xa5,0x34,0x4f,0xd8,0x2e,0xab,0x5d,0x96,0xcc,0x6e,0x9b, 0xf2,0xb6,0x86,0x1b,0x76,0x54,0x74,0xbd,0xe4,0x9e,0xc0,0xb7,0xe7,0x29,0x7c,0xf2, 0xd6,0x8b,0xfb,0x9,0x31,0xaf,0xd7,0x89,0xdd,0x84,0xe6,0xf3,0xd0,0xd4,0x90,0x43, 0xb,0x96,0x5f,0x82,0x6b,0xd3,0x40,0x50,0xf2,0x80,0x8,0xda,0x2a,0x84,0xce,0x1, 0x8f,0x4a,0x89,0xc0,0x7a,0x62,0xca,0xd7,0x66,0x31,0xcc,0x37,0x7,0x5d,0xfa,0x12, 0x73,0x5a,0x94,0xde,0xad,0x54,0x30,0xa0,0x55,0xb7,0x7c,0x7f,0x3d,0xca,0x0,0xcc, 0x94,0x8a,0xe,0xf,0x6c,0xd8,0xe7,0x52,0x89,0xb4,0x9,0x90,0x91,0x4,0xa3,0x5, 0x5e,0xb7,0xe4,0xd,0xd,0x94,0x2d,0xe1,0x4c,0xa9,0x61,0x9,0xf3,0x61,0x56,0x89, 0x6b,0xe3,0x18,0xd7,0x3c,0x0,0xa9,0xc5,0x34,0xb3,0x57,0xc5,0xb7,0x7a,0x4b,0x96, 0x32,0xaf,0xa3,0xbe,0xc3,0xd0,0xa0,0x10,0xfa,0x81,0x99,0x6e,0xe3,0xef,0x77,0xce, 0xd3,0x90,0x27,0x10,0x90,0xd0,0x55,0xc5,0x84,0x2c,0xb,0xbc,0xa6,0xd5,0x53,0x59, 0x85,0xf6,0x97,0x49,0x47,0xb8,0xd9,0xc1,0x3a,0x73,0xb0,0x9d,0x63,0x28,0x6d,0xb6, 0xb8,0x94,0x46,0xc9,0x65,0x9b,0x8f,0x6a,0xc8,0x1a,0x27,0xee,0xf0,0x7a,0xc7,0xf5, 0xf0,0x60,0xbf,0x38,0x19,0x99,0x7a,0xd2,0xd,0xaa,0x71,0xef,0xd2,0x5e,0x26,0x8c, 0xf2,0x6c,0x56,0xd7,0x87,0x65,0x42,0xcf,0xfe,0x69,0xbf,0x6f,0xe3,0x87,0x66,0xd4, 0x67,0x26,0x8d,0x0,0x3f,0x87,0xd3,0x4c,0x32,0xc4,0xbb,0x5,0x23,0xe1,0x11,0x16, 0x4e,0xe6,0x6d,0x55,0xcb,0xb0,0x26,0xcb,0x1a,0x65,0x3b,0x7e,0x6c,0x21,0xd2,0xd4, 0xc6,0x60,0xd4,0x6,0x67,0x28,0xd1,0x99,0xec,0x8d,0x1f,0x10,0x6f,0xaf,0xa5,0x3d, 0x97,0x14,0x93,0x63,0xc4,0x39,0xae,0x5e,0x9e,0x6a,0xdc,0x8a,0x8b,0xb0,0xde,0xd2, 0x90,0xb4,0xd8,0xf8,0xdc,0xab,0x12,0xca,0x39,0xb0,0xda,0x29,0x61,0x81,0x66,0xf8, 0x15,0x79,0x5c,0xd9,0x32,0x8b,0xb7,0x50,0xf5,0x15,0xdb,0x81,0x45,0xba,0x54,0xd5, 0xee,0xad,0x4e,0xcc,0x59,0xe0,0x17,0x12,0x91,0x71,0xba,0xf2,0x72,0xa1,0xeb,0x87, 0x1b,0xc8,0xe0,0xcd,0x54,0x99,0x1e,0x4a,0xae,0xf9,0x4b,0xf3,0x35,0x20,0x49,0x24, 0xcd,0x98,0x70,0xa6,0xf8,0x87,0x38,0x8a,0x79,0xf3,0x7e,0xeb,0x95,0xe9,0xf3,0x30, 0x32,0xd4,0xfd,0x6,0xed,0x9c,0x50,0x9c,0x96,0x1c,0x10,0xcb,0xbb,0x5a,0xf0,0x9, 0x72,0xe0,0xaf,0xea,0x69,0xe7,0x75,0xe2,0x5b,0x73,0x4e,0x70,0x5e,0x42,0xa1,0x90, 0x97,0x1f,0x97,0x85,0xbb,0x67,0xa2,0xd2,0x3,0xb2,0x1e,0xbe,0x8c,0x8e,0x47,0x7e, 0x70,0xf6,0x69,0xd9,0x5f,0x5f,0x3c,0x3a,0xd2,0x8a,0xab,0xb0,0x4d,0xcc,0x42,0xe4, 0xeb,0x59,0x6a,0x28,0x40,0xd,0xfa,0xc3,0x40,0x19,0x2,0xcc,0x28,0x4a,0xcb,0x98, 0xc0,0x35,0x72,0x20,0x94,0x2e,0xda,0xe7,0xb8,0x86,0x98,0x85,0x53,0x5a,0x6a,0xbe, 0xb3,0xd5,0x66,0x74,0x62,0xe0,0xb7,0xa2,0x7a,0xb9,0xef,0xa2,0x83,0xbb,0x3b,0x45, 0x70,0x2d,0xe4,0x85,0x5b,0xbf,0x6d,0x93,0xc5,0x6,0x1a,0x19,0x61,0x84,0x58,0x94, 0xd9,0xbe,0x88,0xbc,0xa0,0x40,0x5f,0x1b,0x7a,0xce,0xbd,0xfd,0xa,0x78,0x43,0xfa, 0xa5,0xa8,0x80,0x80,0x68,0x6d,0x14,0x2f,0xf2,0xad,0xc7,0xd3,0x33,0x9f,0xe8,0x8c, 0x5f,0x71,0x49,0x7f,0x32,0x29,0x1a,0x2c,0xf7,0x57,0x2a,0x82,0xcf,0xed,0x7d,0xf4, 0x96,0x7d,0x75,0x7e,0xea,0x9,0x2d,0x5d,0xb7,0x75,0x32,0x6a,0x15,0x1b,0xf6,0xf3, 0xc,0xc0,0xf2,0xbd,0xe9,0x8c,0xe9,0x61,0xe3,0x15,0x63,0x33,0x82,0xe0,0xa7,0x98, 0x5e,0x1d,0x96,0xc8,0x27,0xc4,0x27,0x5e,0xb9,0x59,0xc8,0x4e,0xf3,0x3f,0x43,0x7f, 0x0,0xb5,0x3e,0x69,0x43,0x28,0xcb,0xa6,0xbc,0xae,0xda,0x3f,0x90,0x82,0xd7,0x6e, 0x20,0xee,0x38,0xc6,0xb3,0xde,0x25,0xec,0xb7,0xed,0x3b,0xab,0x2d,0xfd,0x2b,0xad, 0xb4,0x69,0x17,0x77,0x12,0x62,0x1e,0xce,0x12,0x78,0x8e,0x22,0xfb,0xe5,0x90,0x9b, 0xd4,0x48,0x62,0x88,0x27,0x87,0xf4,0xde,0xf4,0x31,0xa,0xa1,0x2f,0x36,0x4f,0x63, 0x1f,0x67,0xda,0x31,0x49,0xf9,0x80,0xda,0x72,0xf,0xfc,0xed,0xf4,0x8e,0x89,0xca, 0xd6,0xeb,0xd2,0xfe,0xf2,0xc8,0x5d,0xe7,0x79,0x68,0x8a,0xa8,0x9e,0xd9,0xd,0x3d, 0xc0,0xe7,0xee,0x8a,0x61,0x6f,0x65,0xd4,0xfd,0x63,0x42,0xf2,0xf1,0xcc,0x3d,0x48, 0x38,0x90,0xc6,0x2c,0xd8,0x25,0x14,0x52,0x8d,0x1e,0x7a,0xab,0x78,0x7,0xe8,0x39, 0x6f,0x57,0xc3,0xd0,0x46,0xa9,0x25,0x44,0xd,0x68,0xb7,0x7e,0xb4,0xf4,0xc6,0xec, 0x5,0x8e,0x19,0xdd,0x33,0xad,0xaf,0xc0,0xcb,0x2b,0x6c,0x44,0x32,0xd4,0xfd,0xa1, 0x2d,0x41,0xf2,0x73,0xea,0x18,0x38,0xf7,0x0,0xef,0x76,0xb4,0x64,0xbd,0xa2,0x6a, 0xcb,0xbb,0xc7,0xfe,0xe8,0x78,0xbf,0xb5,0xa3,0xab,0x79,0x55,0x0,0x77,0x77,0x2d, 0xb9,0x6a,0x21,0xa4,0x2,0xd8,0x1d,0x3,0xc8,0x13,0xb7,0x2d,0x50,0x5a,0x17,0x1c, 0x96,0xdf,0x1b,0x7f,0xd7,0x5a,0xb4,0xfa,0x85,0x2f,0x50,0x86,0x26,0xc7,0x33,0xdf, 0xb1,0x54,0x5,0xb4,0x2d,0xa1,0xb7,0x75,0xb4,0xee,0x23,0x6,0xc9,0xb9,0xa1,0x60, 0x19,0x3d,0x5f,0xf0,0x97,0x94,0xeb,0x1e,0x43,0xbc,0xa4,0x69,0x4,0xd7,0xc9,0xb6, 0xac,0xce,0xea,0x59,0xef,0xa2,0x4f,0x24,0x91,0x72,0x2a,0xda,0x2c,0x4c,0xba,0x46, 0x89,0x1b,0xb6,0xa0,0x2f,0xa3,0xbe,0x72,0xdf,0xe2,0xdb,0xe3,0x3b,0x25,0x1a,0x67, 0x73,0x5,0xc0,0x63,0x27,0x10,0x88,0x39,0x2,0x32,0x14,0x2f,0x7e,0xcf,0xf4,0x87, 0x6a,0xab,0x29,0x99,0xce,0x67,0x8b,0x2e,0x4b,0xe6,0x92,0x6,0xd,0xac,0x6d,0x80, 0x32,0x2e,0xe4,0xd8,0xbe,0xec,0x12,0x40,0x1f,0x27,0x6f,0x1e,0x76,0xe3,0xa5,0xe0, 0x10,0x4e,0xf9,0x5e,0xb6,0x85,0x8d,0x2,0x6c,0x20,0x87,0x79,0x4c,0xf4,0x7a,0xfd, 0xa2,0xde,0xd7,0x61,0xcb,0xe9,0xa2,0x6a,0x90,0x91,0x8,0x7,0xf5,0x2e,0x67,0x6, 0x7c,0xe0,0x64,0x33,0x66,0x71,0xb4,0x53,0x91,0x3c,0x4c,0x5e,0x31,0xc6,0x5c,0xd4, 0xa5,0x34,0xb5,0xf0,0x1f,0xd7,0x5c,0x2f,0xe9,0x64,0xb6,0xdf,0x92,0x1e,0x65,0x10, 0x0,0x49,0xc2,0xe5,0xbb,0x78,0x39,0xcc,0x34,0x86,0x2b,0xe5,0xcc,0x88,0x3a,0x73, 0xbc,0x6f,0x64,0x5b,0x48,0x40,0x8b,0xb1,0xa5,0x42,0x11,0xb7,0xdf,0xf5,0x47,0x5f, 0x3f,0xb,0xc5,0x7a,0x3,0xfe,0x48,0xb6,0x5,0xf2,0x9c,0x52,0x7b,0xd6,0xc5,0xb8, 0x47,0xa9,0x14,0xf,0x6a,0x1f,0x40,0x8f,0xe0,0x51,0x47,0xc1,0x47,0xf,0xa0,0x6, 0x99,0x66,0x81,0x9c,0xe5,0xc9,0xd2,0x6a,0xbc,0x70,0xbc,0xb8,0xc6,0x2,0x71,0x8d, 0x2c,0x5,0x1c,0x96,0x25,0x5c,0x26,0x6,0xad,0xec,0x47,0x74,0xfb,0xe8,0x7b,0x95, 0xce,0xfc,0xb1,0x34,0x46,0x5,0x9f,0x82,0x75,0xdb,0xba,0xbb,0xde,0x2c,0xc9,0x8a, 0xb1,0xe5,0x21,0xd6,0xc2,0xc6,0x5c,0xef,0x33,0xa4,0x65,0xaf,0xd,0x60,0xc4,0x5b, 0x5d,0xf6,0x90,0x23,0xfb,0x30,0x25,0xf0,0xc,0xe0,0xac,0x6a,0x8c,0xf5,0xf4,0x3e, 0x5c,0x16,0x94,0x1f,0x5c,0xf1,0xf,0x90,0x16,0xf3,0xbf,0xa2,0x54,0x84,0xfd,0x31, 0x7b,0x8e,0xd3,0x77,0x3e,0xf9,0x68,0x4b,0x5a,0x95,0xb5,0x66,0x8b,0x2b,0x25,0x67, 0xc0,0xb9,0x86,0x1e,0x2b,0x16,0x2e,0xc0,0xa,0xed,0x63,0xde,0x72,0xe1,0x8f,0x6e, 0x70,0x64,0xe5,0xaf,0xdd,0xce,0x7a,0x38,0xe3,0xaf,0x1e,0xee,0xda,0x43,0x57,0x9c, 0x7d,0xdd,0x3a,0xa8,0x73,0xe7,0xe9,0xfd,0xd5,0x4d,0x5c,0xc7,0xae,0xeb,0x36,0x20, 0x50,0x9c,0x4f,0x2e,0xea,0x49,0xe5,0xce,0xf8,0x5,0xbd,0x54,0xc7,0x15,0x70,0x45, 0x73,0x2a,0x6e,0x66,0x12,0x58,0x64,0xe7,0x25,0xc0,0x2f,0xd4,0x2d,0xe5,0xf4,0x7d, 0x2,0xc3,0x2c,0xec,0xd,0x91,0x3b,0x85,0x16,0xf8,0x59,0xde,0x8e,0x49,0x24,0x81] + [0 for _ in range(DefineConstants.SEQUENCE_MAX_NUM - 32768)]


    SHOP_MAX_DISTANCE = 1000

## Laniatus Games Studio Inc. | NOTE: Python has no need of forward class declarations:
    #class CGrid

    @staticmethod
    def CompareShopItemName(lhs, rhs):
        lItem = ITEM_MANAGER.instance().GetTable(lhs.vnum)
        rItem = ITEM_MANAGER.instance().GetTable(rhs.vnum)
        if lItem is not None and rItem is not None:
            return strcmp(lItem.szLocaleName, rItem.szLocaleName) < 0
        else:
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    @staticmethod
    def ConvertToShopItemTable(pNode, shopTable):
        if not pNode.GetValue("vnum", 0, shopTable.dwVnum):
            #lani_err("Group %s does not have vnum.", pNode.GetNodeName())
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if not pNode.GetValue("name", 0, shopTable.name):
            #lani_err("Group %s does not have name.", pNode.GetNodeName())
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if len(shopTable.name) >= LGEMiscellaneous.SHOP_TAB_NAME_MAX:
            #lani_err("Shop name length must be less than %d. Error in Group %s, name %s", LGEMiscellaneous.SHOP_TAB_NAME_MAX, pNode.GetNodeName(), shopTable.name)
            return LGEMiscellaneous.DEFINECONSTANTS.false

        stCoinType = ""
        if not pNode.GetValue("cointype", 0, stCoinType):
            stCoinType = "Gold"

        if _boost_func_of_void.iequals(stCoinType, "Gold"):
            shopTable.coinType = EShopCoinType.SHOP_COIN_TYPE_GOLD
        elif _boost_func_of_void.iequals(stCoinType, "SecondaryCoin"):
            shopTable.coinType = EShopCoinType.SHOP_COIN_TYPE_SECONDARY_COIN
        else:
            #lani_err("Group %s has undefine cointype(%s).", pNode.GetNodeName(), stCoinType)
            return LGEMiscellaneous.DEFINECONSTANTS.false

        pItemGroup = pNode.GetChildNode("items")
        if pItemGroup is None:
            #lani_err("Group %s does not have 'group items'.", pNode.GetNodeName())
            return LGEMiscellaneous.DEFINECONSTANTS.false

        itemGroupSize = pItemGroup.GetRowCount()
        shopItems = [None for _ in range(itemGroupSize)]
        if itemGroupSize >= LGEMiscellaneous.SHOP_HOST_ITEM_MAX_NUM:
            #lani_err("count(%d) of rows of group items of group %s must be smaller than %d", itemGroupSize, pNode.GetNodeName(), LGEMiscellaneous.SHOP_HOST_ITEM_MAX_NUM)
            return LGEMiscellaneous.DEFINECONSTANTS.false

        for i in range(0, itemGroupSize):
            if not pItemGroup.GetValue(i, "vnum", shopItems[i].vnum):
                #lani_err("row(%d) of group items of group %s does not have vnum column", i, pNode.GetNodeName())
                return LGEMiscellaneous.DEFINECONSTANTS.false

            if not pItemGroup.GetValue(i, "count", shopItems[i].count):
                #lani_err("row(%d) of group items of group %s does not have count column", i, pNode.GetNodeName())
                return LGEMiscellaneous.DEFINECONSTANTS.false
            if not pItemGroup.GetValue(i, "price", shopItems[i].price):
                #lani_err("row(%d) of group items of group %s does not have price column", i, pNode.GetNodeName())
                return LGEMiscellaneous.DEFINECONSTANTS.false
            if shopItems[i].price_type >= EX_MAX or shopItems[i].price_type < EX_GOLD:
                #lani_err("row(%d) of group items of group %s price_type is wrong!", i, pNode.GetNodeName())
                return LGEMiscellaneous.DEFINECONSTANTS.false
            getval = str(['\0' for _ in range(20)])
            j = 0
            while j < EItemMisc.LG_ITEM_SOCKET_MAX_NUM:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                snprintf(getval, sizeof(getval), "socket%d", j)
                if not pItemGroup.GetValue(i, getval, shopItems[i].alSockets[j]):
                    #lani_err("row(%d) stage %d of group items of group %s does not have socket column", i, j, pNode.GetNodeName())
                    return LGEMiscellaneous.DEFINECONSTANTS.false
                j += 1
            j = 0
            while j < EItemMisc.ITEM_ATTRIBUTE_MAX_NUM:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                snprintf(getval, sizeof(getval), "attr_type%d", j)
                if not pItemGroup.GetValue(i, getval, shopItems[i].aAttr[j].bType):
                    #lani_err("row(%d) stage %d of group items of group %s does not have attr_type column", i, j, pNode.GetNodeName())
                    return LGEMiscellaneous.DEFINECONSTANTS.false
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                snprintf(getval, sizeof(getval), "attr_value%d", j)
                if not pItemGroup.GetValue(i, getval, shopItems[i].aAttr[j].sValue):
                    #lani_err("row(%d) stage %d of group items of group %s does not have attr_value column", i, j, pNode.GetNodeName())
                    return LGEMiscellaneous.DEFINECONSTANTS.false
                j += 1
            if pItemGroup.GetValue(i, "price_type", shopItems[i].price_type) and pItemGroup.GetValue(i, "price_vnum", shopItems[i].price_vnum) and shopItems[i].price_type == 3:
                if ITEM_MANAGER.instance().GetTable(shopItems[i].price_vnum) is None:
                    #lani_err("NOT GET ITEM PROTO %d", shopItems[i].price_vnum)
                    return LGEMiscellaneous.DEFINECONSTANTS.false
        stSort = ""
        if not pNode.GetValue("sort", 0, stSort):
            stSort = "None"

        if _boost_func_of_void.iequals(stSort, "Asc"):
            std::sort(shopItems.begin(), shopItems.end(), CompareShopItemName)
        elif _boost_func_of_void.iequals(stSort, "Desc"):
            std::sort(shopItems.rbegin(), shopItems.rend(), CompareShopItemName)
        else:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Only expression lambdas are converted by # Laniatus Games Studio Inc. |:
    # std::sort(shopItems.begin(), shopItems.end(), [stSort](const SShopItemTable& i1, const SShopItemTable& i2)
            #        {
            #            const auto lItem = ITEM_MANAGER::instance().GetTable(i1.vnum)
            #            const auto rItem = ITEM_MANAGER::instance().GetTable(i2.vnum)
            #            if (!stSort.compare("Vnum"))
            #                return i1.vnum > i2.vnum
            #            else if (!stSort.compare("Price"))
            #                return i1.price > i2.price
            #            else if (!stSort.compare("Name") && lItem && rItem)
            #                return strcmp(lItem->szLocaleName, rItem->szLocaleName) < 0
            #            else if (!stSort.compare("Type") && lItem && rItem)
            #                return lItem->bType > rItem->bType
            #            return i1.vnum > i2.vnum
            #        }
            #        )

        grid = CGrid(5, 9)
        iPos = None

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memset(shopTable.items[0], 0, sizeof(shopTable.items))

        i = 0
        while i < len(shopItems):
            item_table = ITEM_MANAGER.instance().GetTable(shopItems[i].vnum)
            if item_table is None:
                #lani_err("vnum(%d) of group items of group %s does not exist", shopItems[i].vnum, pNode.GetNodeName())
                return LGEMiscellaneous.DEFINECONSTANTS.false

            iPos = grid.FindBlank(1, item_table.bSize)

            grid.Put(iPos, 1, item_table.bSize)
## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: shopTable.items[iPos] = shopItems[i];
            shopTable.items[iPos].copy_from(shopItems[i])
            i += 1

        shopTable.byItemCount = len(shopItems)
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern char g_nation_name[4][32]
## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern uint g_start_position[4][2]
## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern int g_start_map[4]
## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern uint g_create_position[4][2]
## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern uint g_create_position_canada[4][2]


    @staticmethod
    def EMPIRE_NAME(e):
        return LC_TEXT(Globals.g_nation_name[e])

    @staticmethod
    def EMPIRE_START_MAP(e):
        return uint(Globals.g_start_map[e])

    @staticmethod
    def EMPIRE_START_X(e):
        if 1 <= e and e <= 3:
            return Globals.g_start_position[e][0]

        return 0

    @staticmethod
    def EMPIRE_START_Y(e):
        if 1 <= e and e <= 3:
            return Globals.g_start_position[e][1]

        return 0

    @staticmethod
    def CREATE_START_X(e):
        if 1 <= e and e <= 3:
            return Globals.g_create_position[e][0]

        return 0

    @staticmethod
    def CREATE_START_Y(e):
        if 1 <= e and e <= 3:
            return Globals.g_create_position[e][1]

        return 0



    g_nation_name = ["", "Pandemonia Kingdom", "Asmodia Kingdom", "Elgoria Kingdom"]

    g_start_map = [0, 1, 21, 41]

    g_start_position = [[ 0, 0 ], [ 469300, 964200 ], [ 55700, 157900 ], [ 969600, 278400 ]]

    g_create_position = [[ 0, 0 ], [ 459800, 953900 ], [ 52070, 166600 ], [ 957300, 255200 ]]

    g_create_position_canada = [[ 0, 0 ], [ 457100, 946900 ], [ 45700, 166500 ], [ 966300, 288300 ]]




    @staticmethod
    def SendTargetCreatePacket(d, info):
        if not info.bSendToClient:
            return

        pck = TPacketGCTargetCreate()

        pck.bHeader = byte(Globals.LG_HEADER_GC_TARGET_CREATE)
        pck.lID = info.iID
        pck.bType = byte(info.iType)
        pck.dwVID = uint(info.iArg1)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        strncpy_s(pck.szName, sizeof(pck.szName), info.szTargetDesc, _TRUNCATE)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        d.Packet(pck, sizeof(TPacketGCTargetCreate))

    @staticmethod
    def SendTargetUpdatePacket(d, iID, x, y):
        pck = TPacketGCTargetUpdate()
        pck.bHeader = byte(Globals.LG_HEADER_GC_TARGET_UPDATE)
        pck.lID = iID
        pck.lX = x
        pck.lY = y
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        d.Packet(pck, sizeof(TPacketGCTargetUpdate))
        #sys_log(0, "SendTargetUpdatePacket %d %dx%d", iID, x, y)

    @staticmethod
    def SendTargetDeletePacket(d, iID):
        pck = TPacketGCTargetDelete()
        pck.bHeader = byte(Globals.LG_HEADER_GC_TARGET_DELETE)
        pck.lID = iID
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        d.Packet(pck, sizeof(TPacketGCTargetDelete))

    @staticmethod
    def (UnnamedParameter):
        info = if isinstance(event.info, TargetInfo) else None

        if info is None:
            #lani_err("target_event> <Factor> Null pointer")
            return 0


        pkChr = CHARACTER_MANAGER.instance().FindByPID(info.dwPID)
        if pkChr is None:
            return 0
        tch = None
        x = 0
        y = 0
        iDist = 5000

        if info.iMapIndex != pkChr.GetMapIndex():
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
            return MINMAX(passes_per_sec / 2, iDist / (1500 / passes_per_sec), passes_per_sec * 5)

        if info.iType == ETargetTypes.TARGET_TYPE_POS:
            x = info.iArg1
            y = info.iArg2
            iDist = Globals.DISTANCE_APPROX(pkChr.GetX() - x, pkChr.GetY() - y)

        elif info.iType == ETargetTypes.TARGET_TYPE_VID:
                tch = CHARACTER_MANAGER.instance().Find(info.iArg1)

                if tch is not None and tch.GetMapIndex() == pkChr.GetMapIndex():
                    x = tch.GetX()
                    y = tch.GetY()
                    iDist = Globals.DISTANCE_APPROX(pkChr.GetX() - x, pkChr.GetY() - y)

        bRet = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        if iDist <= 500:
            bRet = quest.CQuestManager.instance().Target(pkChr.GetPlayerID(), info.dwQuestIndex, info.szTargetName, "arrive")

        if tch is None and info.iType == ETargetTypes.TARGET_TYPE_VID:
            quest.CQuestManager.instance().Target(pkChr.GetPlayerID(), info.dwQuestIndex, info.szTargetName, "die")
            CTargetManager.instance().DeleteTarget(pkChr.GetPlayerID(), info.dwQuestIndex, info.szTargetName)

        if event.is_force_to_end:
            #sys_log(0, "target_event: event canceled")
            return 0

        if x != info.iOldX or y != info.iOldY:
            if info.bSendToClient:
                Globals.SendTargetUpdatePacket(pkChr.GetDesc(), info.iID, x, y)

            info.iOldX = x
            info.iOldY = y

        if not bRet:
            return passes_per_sec
        else:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
            return MINMAX(passes_per_sec / 2, iDist / (1500 / passes_per_sec), passes_per_sec * 5)




    ms_groupNodePool = CDynamicPool()
    @staticmethod
    def OnClickShop(ch, causer):
        CShopManager.instance().StartShopping(causer, ch, 0)
        return 1

# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
    #OnClickTalk(ch, causer)

    @staticmethod
    def OnIdleDefault(ch, causer):
        if ch.OnIdle():
            return ((1) * passes_per_sec)

        return ((1) * passes_per_sec)

# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
    #OnAttackDefault(ch, causer)

    OnClickTriggers = [STriggerFunction(None), STriggerFunction(OnClickShop)]

    @staticmethod
    def FindVictim(pkChr, iMaxDistance):
        f = FuncFindMobVictim(pkChr, iMaxDistance)
        if pkChr.GetSectree() is not None:
            pkChr.GetSectree().ForEachAround(f.functor_method)
        return f.GetVictim()


    ## Laniatus Games Studio Inc. | NOTE: The following #define macro was replaced in-line:
    #ORIGINAL METINII C CODE: #define IS_SET(flag, bit) ((flag) & (bit))
    ## Laniatus Games Studio Inc. | NOTE: The following #define macro was replaced in-line:
    #ORIGINAL METINII C CODE: #define SET_BIT(var, bit) ((var) |= (bit))
    ## Laniatus Games Studio Inc. | NOTE: The following #define macro was replaced in-line:
    #ORIGINAL METINII C CODE: #define REMOVE_BIT(var, bit) ((var) &= ~(bit))
    ## Laniatus Games Studio Inc. | NOTE: The following #define macro was replaced in-line:
    #ORIGINAL METINII C CODE: #define TOGGLE_BIT(var, bit) ((var) = (var) ^ (bit))

    @staticmethod
    def DISTANCE_SQRT(dx, dy):
        return sqrt(float(dx) * dx + float(dy) * dy)

    @staticmethod
    def DISTANCE_APPROX(dx, dy):
        min = None
        max = None

        if dx < 0:
            dx = -dx

        if dy < 0:
            dy = -dy

        if dx < dy:
            min = dx
            max = dy
        else:
            min = dy
            max = dx

        return (((max << 8) + (max << 3) - (max << 4) - (max << 1) + (min << 7) - (min << 5) + (min << 3) - (min << 1)) >> 8)

    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##if ! _WIN32
    @staticmethod
    def MAKEWORD(a, b):
        return ushort(a | (b << 8))
    ##endif

    @staticmethod
    def set_global_time(t):
        Globals.global_time_gap = t - time(0)

        time_str_buf = str(['\0' for _ in range(32)])
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        snprintf(time_str_buf, sizeof(time_str_buf), "%s", time_str(Globals.get_global_time()))

        #sys_log(0, "GLOBAL_TIME: %s time_gap %d", time_str_buf, Globals.global_time_gap)

    @staticmethod
    def get_global_time():
        return time(0) + Globals.global_time_gap

    @staticmethod
    def dice(number, size):
        sum = 0
        val = None

        if size <= 0 or number <= 0:
            return (0)

        while number != 0:
            val = ((math.fmod(thecore_random(), size)) + 1)
            sum += val
            number -= 1

        return (sum)

    @staticmethod
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Pointer arithmetic is detected on the parameter 'src':
#ORIGINAL METINII C CODE: size_t str_lower(const char* src, char* dest, size_t dest_size)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Pointer arithmetic is detected on the parameter 'dest':
    def str_lower(src, dest, dest_size):
        len = 0

        if (not dest) != '\0' or dest_size == 0:
            return size_t(len)

        if (not src) != '\0':
            *dest = '\0'
            return size_t(len)

        dest_size -= 1

        while *src != '\0' and len < dest_size:
            *dest = LOWER(*src)

            src += 1
            dest += 1
            len += 1

        *dest = '\0'
        return size_t(len)

    @staticmethod
    def skip_spaces(string):
        while *string[0] != '\0' and (not(((string[0]) & 0xE0) > 0x90) and isspace(string[0])):
            pass
            (*string) += 1

    @staticmethod
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Pointer arithmetic is detected on the parameter 'argument':
#ORIGINAL METINII C CODE: const char* one_argument(const char* argument, char* first_arg, size_t first_size)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Pointer arithmetic is detected on the parameter 'first_arg':
    def one_argument(argument, first_arg, first_size):
        mark = DefineConstants.false
        first_len = 0

        if (not argument) != '\0' or 0 == first_size:
            #lani_err("one_argument received a NULL pointer!")
            *first_arg = '\0'
            return None

        first_size -= 1

        Globals.skip_spaces(argument)

        while *argument != '\0' and first_len < first_size:
            if *argument == '\"':
                mark = not mark
                argument += 1
                continue

            if (not mark) != '\0' and (not(((*argument) & 0xE0) > 0x90) and isspace(*argument)):
                break

## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: * (first_arg++) = *argument;
            * (first_arg) = *argument
            first_arg += 1
            argument += 1
            first_len += 1

        *first_arg = '\0'

        Globals.skip_spaces(argument)
        return (argument)

    @staticmethod
    def two_arguments(argument, first_arg, first_size, second_arg, second_size):
        return (Globals.one_argument(Globals.one_argument(argument, first_arg.arg_value, size_t(first_size)), second_arg.arg_value, size_t(second_size)))

    @staticmethod
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Pointer arithmetic is detected on the parameter 'argument':
#ORIGINAL METINII C CODE: const char* first_cmd(const char* argument, char* first_arg, size_t first_arg_size, size_t* first_arg_len_result)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Pointer arithmetic is detected on the parameter 'first_arg':
    def first_cmd(argument, first_arg, first_arg_size, first_arg_len_result):
        cur_len = 0
        Globals.skip_spaces(argument)

        first_arg_size -= 1

        while *argument != '\0' and not(not(((*argument) & 0xE0) > 0x90) and isspace(*argument)) and cur_len < first_arg_size:
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: * (first_arg++) = LOWER(*argument);
            * (first_arg) = LOWER(*argument)
            first_arg += 1
            argument += 1
            cur_len += 1

## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: *first_arg_len_result = cur_len;
        first_arg_len_result.copy_from(cur_len)
        *first_arg = '\0'
        return (argument)

    @staticmethod
    def CalculateDuration(iSpd, iDur):
        i = 100 - iSpd

        if i > 0:
            i = 100 + i
        elif i < 0:
            i = math.trunc(10000 / float(100 - i))
        else:
            i = 100

        return math.trunc(iDur * i / float(100))

    ## Laniatus Games Studio Inc. | NOTE: This was formerly a static local variable declaration (not allowed in Python):
    gauss_random_haveNextGaussian = DefineConstants.false
    ## Laniatus Games Studio Inc. | NOTE: This was formerly a static local variable declaration (not allowed in Python):
    gauss_random_nextGaussian = 0.0

    @staticmethod
    def gauss_random(avg = 0, sigma = 1):
        ## Laniatus Games Studio Inc. | NOTE: This static local variable declaration (not allowed in Python) has been moved just prior to the method:
        #    static bool haveNextGaussian = DefineConstants.false
        ## Laniatus Games Studio Inc. | NOTE: This static local variable declaration (not allowed in Python) has been moved just prior to the method:
        #    static float nextGaussian = 0.0f

        if gauss_random_haveNextGaussian:
            gauss_random_haveNextGaussian = DefineConstants.false
            return gauss_random_nextGaussian * sigma + avg
        else:
            v1 = None
            v2 = None
            s = None
            condition = True
            while condition:
                v1 = Globals.uniform_random(-1.0, 1.0)
                v2 = Globals.uniform_random(-1.0, 1.0)
                s = v1 * v1 + v2 * v2
                condition = s >= 1.0 or abs(s) < FLT_EPSILON
            multiplier = sqrtf(-2 * logf(s) / s)
            gauss_random_nextGaussian = v2 * multiplier
            gauss_random_haveNextGaussian = ((not DefineConstants.false))
            return v1 * multiplier * sigma + avg

    @staticmethod
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Pointer arithmetic is detected on the parameter 'str':
#ORIGINAL METINII C CODE: int parse_time_str(const char* str)
    def parse_time_str(str):
        tmp = 0
        secs = 0

        while *str != 0:
            if (*str == 'm') or (*str == 'M'):
                secs += tmp * 60
                tmp = 0

            elif (*str == 'h') or (*str == 'H'):
                secs += tmp * 3600
                tmp = 0

            elif (*str == 'd') or (*str == 'D'):
                secs += tmp * 86400
                tmp = 0

            elif (*str == '0') or (*str == '1') or (*str == '2') or (*str == '3') or (*str == '4') or (*str == '5') or (*str == '6') or (*str == '7') or (*str == '8') or (*str == '9'):
                tmp *= 10
                tmp += (*str) - '0'

            elif (*str == 's') or (*str == 'S'):
                secs += tmp
                tmp = 0
            else:
                return -1
            str += 1

        return secs + tmp

    @staticmethod
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Pointer arithmetic is detected on the parameter 'w':
#ORIGINAL METINII C CODE: bool WildCaseCmp(const char* w, const char* s)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Pointer arithmetic is detected on the parameter 's':
    def WildCaseCmp(w, s):
        while True:
            if *w == '*':
                if '\0' == w[1]:
                    return ((not DefineConstants.false))
                    i = 0
                    while i <= strlen(s):
                        if ((not DefineConstants.false)) == Globals.WildCaseCmp(w + 1, s + i):
                            return ((not DefineConstants.false))
                        i += 1
                return DefineConstants.false

            if (*w == '*') or (*w == '?'):
                if '\0' == *s:
                    return DefineConstants.false

                w += 1
                s += 1

            else:
                if *w != *s:
                    if tolower(*w) != tolower(*s):
                        return DefineConstants.false

                if '\0' == *w:
                    return ((not DefineConstants.false))

                w += 1
                s += 1
        return DefineConstants.false



    @staticmethod
    def str_to_number(out, in_):
        if None==in_ or None==in_[0]:
            return DefineConstants.false

        out.arg_value = (strtol(in_, None, 10) != 0)
        return ((not DefineConstants.false))

    @staticmethod
    def str_to_number(out, in_):
        if None==in_ or None==in_[0]:
            return DefineConstants.false

        out.arg_value = (char) strtol(in_, None, 10)
        return ((not DefineConstants.false))

    @staticmethod
    def str_to_number(out, in_):
        if None==in_ or None==in_[0]:
            return DefineConstants.false

        out.arg_value = byte(int(strtoul(in_, None, 10)))
        return ((not DefineConstants.false))

    @staticmethod
    def str_to_number(out, in_):
        if None==in_ or None==in_[0]:
            return DefineConstants.false

        out.arg_value = short(int(strtol(in_, None, 10)))
        return ((not DefineConstants.false))

    @staticmethod
    def str_to_number(out, in_):
        if None==in_ or None==in_[0]:
            return DefineConstants.false

        out.arg_value = strtoul(in_, None, 10)
        return ((not DefineConstants.false))

    @staticmethod
    def str_to_number(out, in_):
        if None==in_ or None==in_[0]:
            return DefineConstants.false

        out.arg_value = int(strtol(in_, None, 10))
        return ((not DefineConstants.false))

    @staticmethod
    def str_to_number(out, in_):
        if None==in_ or None==in_[0]:
            return DefineConstants.false

        out.arg_value = strtoul(in_, None, 10)
        return ((not DefineConstants.false))

    @staticmethod
    def str_to_number(out, in_):
        if None==in_ or None==in_[0]:
            return DefineConstants.false

        out.arg_value = int(strtol(in_, None, 10))
        return ((not DefineConstants.false))

    @staticmethod
    def str_to_number(out, in_):
        if None==in_ or None==in_[0]:
            return DefineConstants.false

        out.arg_value = strtoul(in_, None, 10)
        return ((not DefineConstants.false))

    @staticmethod
    def str_to_number(out, in_):
        if None==in_ or None==in_[0]:
            return DefineConstants.false

        out.arg_value = int(strtoull(in_, None, 10))
        return ((not DefineConstants.false))

    @staticmethod
    def str_to_number(out, in_):
        if None==in_ or None==in_[0]:
            return DefineConstants.false

        out.arg_value = float(strtof(in_, None))
        return ((not DefineConstants.false))

    @staticmethod
    def str_to_number(out, in_):
        if None==in_ or None==in_[0]:
            return DefineConstants.false

        out.arg_value = float(strtod(in_, None))
        return ((not DefineConstants.false))

    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##if __FreeBSD__
    @staticmethod
    def str_to_number(out, in_):
        if None==in_ or None==in_[0]:
            return DefineConstants.false

        out.arg_value = float(strtold(in_, None))
        return ((not DefineConstants.false))
    ##endif


    global_time_gap = 0

    @staticmethod
    def three_arguments(argument, first_arg, first_size, second_arg, second_size, third_arg, third_size):
        return (Globals.one_argument(Globals.one_argument(Globals.one_argument(argument, first_arg.arg_value, size_t(first_size)), second_arg.arg_value, size_t(second_size)), third_arg.arg_value, size_t(third_size)))
    @staticmethod
    def uniform_random(a, b):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        return thecore_random() / (RAND_MAX + 1.0) * (b - a) + a

    ## Laniatus Games Studio Inc. | NOTE: The following #define macro was replaced in-line:
    #ORIGINAL METINII C CODE: #define _PI ((float) 3.141592654f)
    ## Laniatus Games Studio Inc. | NOTE: The following #define macro was replaced in-line:
    #ORIGINAL METINII C CODE: #define _1BYPI ((float) 0.318309886f)

    ## Laniatus Games Studio Inc. | NOTE: The following #define macro was replaced in-line:
    #ORIGINAL METINII C CODE: #define DegreeToRadian( degree ) ((degree) * (_PI / 180.0f))
    ## Laniatus Games Studio Inc. | NOTE: The following #define macro was replaced in-line:
    #ORIGINAL METINII C CODE: #define RadianToDegree( radian ) ((radian) * (180.0f / _PI))

    @staticmethod
    def Normalize(pV1, pV2):
        l = sqrtf(pV1.x * pV1.x + pV1.y * pV1.y + pV1.z * pV1.z + 1.0e-12)

        pV2.x = pV1.x / l
        pV2.y = pV1.y / l
        pV2.z = pV1.z / l

    @staticmethod
    def DotProduct(pV1, pV2):
        return pV1.x * pV2.x + pV1.y * pV2.y + pV1.z * pV2.z

    @staticmethod
    def GetDegreeFromPosition(x, y):
        vtDir = VECTOR()
        vtStan = VECTOR()
        ret = None

        vtDir.x = x
        vtDir.y = y
        vtDir.z = 0.0

        Globals.Normalize(vtDir, vtDir)

        vtStan.x = 0.0
        vtStan.y = 1.0
        vtStan.z = 0.0

        ret = ((acosf(Globals.DotProduct(vtDir, vtStan))) * (180.0 / (float(3.141592654))))

        if vtDir.x < 0.0:
            ret = 360.0 - ret

        return (ret)

    @staticmethod
    def GetDegreeFromPositionXY(sx, sy, ex, ey):
        return Globals.GetDegreeFromPosition(ex - sx, ey - sy)

    @staticmethod
    def GetDeltaByDegree(fDegree, fDistance, x, y):
        fRadian = ((fDegree) * ((float(3.141592654)) / 180.0))

        x.arg_value = fDistance * math.sin(fRadian)
        y.arg_value = fDistance * math.cos(fRadian)

    @staticmethod
    def GetDegreeDelta(iDegree, iDegree2):
        if iDegree > 180.0:
            iDegree = iDegree - 360.0

        if iDegree2 > 180.0:
            iDegree2 = iDegree2 - 360.0

        return abs(iDegree - iDegree2)


    @staticmethod
    def WriteVersion():
        fp = fopen("VERSION.txt", "w")

        if fp:
            fprintf(fp, "Game Version: %s\n", DefineConstants.VERSION)
            fclose(fp)



##include <_boost_func_of_void/functional/hash.hpp>


    @staticmethod
    def hash_value(v):
        hasher = _boost_func_of_void.hash()
        return hasher(v.getID())



    @staticmethod
    def (UnnamedParameter):
        info = if isinstance(event.info, war_map_info) else None

        if info is None:
            #lani_err("war_begin_event> <Factor> Null pointer")
            return 0

        pMap = info.pWarMap
        pMap.CheckWarEnd()
        return ((10) * passes_per_sec)

    @staticmethod
    def (UnnamedParameter):
        info = if isinstance(event.info, war_map_info) else None

        if info is None:
            #lani_err("war_end_event> <Factor> Null pointer")
            return 0

        pMap = info.pWarMap

        if info.iStep == 0:
            info.iStep += 1
            pMap.ExitAll()
            return ((5) * passes_per_sec)
        else:
            pMap.SetEndEvent(None)
            CWarMapManager.instance().DestroyWarMap(pMap)
            return 0

    @staticmethod
    def (UnnamedParameter):
        info = if isinstance(event.info, war_map_info) else None

        if info is None:
            #lani_err("war_timeout_event> <Factor> Null pointer")
            return 0

        pMap = info.pWarMap
        pMap.Timeout()
        return 0

    @staticmethod
    def (UnnamedParameter):
        info = if isinstance(event.info, war_map_info) else None

        if info is None:
            #lani_err("war_reset_flag_event> <Factor> Null pointer")
            return 0

        pMap = info.pWarMap

        pMap.AddFlag(0, 0, 0)
        pMap.AddFlag(1, 0, 0)

        pMap.SetResetFlagEvent(None)
        return 0

    def equals_to(self, lhs, rhs):
        return lhs.bits[0] == rhs.bits[0] and lhs.bits[1] == rhs.bits[1]

    def not_equals_to(self, lhs, rhs):
        return not(lhs is rhs)

    @staticmethod
    def void_bind(f, arg):
        return void_binder(f, arg_type(arg))

    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##if DEBUG_ALLOC
    ##define USE_DEBUG_PTR
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
    ##define ALLOCATOR_DETAIL FifoAllocator
    ## Laniatus Games Studio Inc. | WARNING: The following #include directive was ignored:
    ##include "fifo_allocator.h"

    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Typedefs defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
    #typedef DebugAllocatorAdapter<FifoAllocator> DebugAllocator;


## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following operator cannot be converted to Python:
    #inline object* operator new(size_t size, const char* file, size_t line)
    #{
    ##if ! USE_DEBUG_PTR
    #    object* p = DebugAllocatorAdapter<FifoAllocator>::Alloc(size);
    ##else
    #    object* p = DebugAllocatorAdapter<FifoAllocator>::Alloc(size + sizeof(size_t));
    #    p = reinterpret_cast<size_t*>(p) + 1;
    ##endif
    #    if (p != NULL)
    #    {
    #        size_t age = DebugAllocatorAdapter<FifoAllocator>::MarkAcquired(p, file, line, "new");
    ##if USE_DEBUG_PTR
    #        *(reinterpret_cast<size_t*>(p) - 1) = age;
    ##endif
    #    }
    #    return p;
    #}
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following operator cannot be converted to Python:
    #inline object* operator new[](size_t size, const char* file, size_t line)
    #{
    ##if ! USE_DEBUG_PTR
    #    object* p = DebugAllocatorAdapter<FifoAllocator>::Alloc(size);
    ##else
    #    object* p = DebugAllocatorAdapter<FifoAllocator>::Alloc(size + sizeof(size_t));
    #    p = reinterpret_cast<size_t*>(p) + 1;
    ##endif
    #    if (p != NULL)
    #    {
    #        size_t age = DebugAllocatorAdapter<FifoAllocator>::MarkAcquired(p, file, line, "new[]");
    ##if USE_DEBUG_PTR
    #        *(reinterpret_cast<size_t*>(p) - 1) = age;
    ##endif
    #    }
    #    return p;
    #}
    @staticmethod
    def debug_delete(p, file, line):
        if p is not None:
            DebugAllocatorAdapter.VerifyDeletion(p, file, size_t(line), False, 0)
            p.~None
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##if ! USE_DEBUG_PTR
            DebugAllocatorAdapter.Free(p)
    ##else
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no equivalent to 'reinterpret_cast' in Python:
            px = reinterpret_cast<size_t>(p) - 1
## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: *px = AllocTag::IncreaseAge(*px);
            px.copy_from(AllocTag.IncreaseAge(px))
            DebugAllocatorAdapter.Free(px)
    ##endif
            DebugAllocatorAdapter.MarkReleased(p, file, line, "delete")
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##if USE_DEBUG_PTR
    @staticmethod
    def debug_delete(ptr, file, line):
        p = ptr.Get()
        if p is not None:
            DebugAllocatorAdapter.VerifyDeletion(ptr.Get(), file, size_t(line), True, ptr.GetAge())
            p.~None
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no equivalent to 'reinterpret_cast' in Python:
            px = reinterpret_cast<size_t>(p) - 1
## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: *px = AllocTag::IncreaseAge(*px);
            px.copy_from(AllocTag.IncreaseAge(px))
            DebugAllocatorAdapter.Free(px)
            DebugAllocatorAdapter.MarkReleased(ptr, file, line, "delete")
    ##endif
    @staticmethod
    def debug_delete_array(p, file, line):
        if p is not None:
            DebugAllocatorAdapter.VerifyDeletion(p, file, size_t(line), False, 0)

    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##if ! USE_DEBUG_PTR
            DebugAllocatorAdapter.Free(p)
    ##else
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no equivalent to 'reinterpret_cast' in Python:
            px = reinterpret_cast<size_t>(p) - 1
## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: *px = AllocTag::IncreaseAge(*px);
            px.copy_from(AllocTag.IncreaseAge(px))
            DebugAllocatorAdapter.Free(px)
    ##endif
            DebugAllocatorAdapter.MarkReleased(p, file, line, "delete[]")
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##if USE_DEBUG_PTR
    @staticmethod
    def debug_delete_array(ptr, file, line):
        p = ptr.Get()
        if p is not None:
            DebugAllocatorAdapter.VerifyDeletion(ptr.Get(), file, size_t(line), True, ptr.GetAge())

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no equivalent to 'reinterpret_cast' in Python:
            px = reinterpret_cast<size_t>(p) - 1
## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: *px = AllocTag::IncreaseAge(*px);
            px.copy_from(AllocTag.IncreaseAge(px))
            DebugAllocatorAdapter.Free(px)
            DebugAllocatorAdapter.MarkReleased(ptr, file, line, "delete[]")
    ##endif
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
    ##define LG_NEW_M2 new(__FILE__, __LINE__)
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
    ##define LG_DEL_MEM(p) debug_delete(p, __FILE__, __LINE__)
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
    ##define LG_DEL_MEM_EX(p, f, l) debug_delete(p, f, l)
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
    ##define LG_DEL_MEM_ARRAY(p) debug_delete_array(p, __FILE__, __LINE__)
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
    ##define M2_PTR_REF(ptr) (DebugAllocator::Verify(ptr.Get(), ptr.GetAge(), __FILE__, __LINE__))
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
    ##define M2_PTR_DEREF(ptr) (*(DebugAllocator::Verify(ptr.Get(), ptr.GetAge(), __FILE__, __LINE__)))

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following operator cannot be converted to Python:
    #inline void operator delete(object* p, const char* file, size_t line)
    #{
    #    if (p != NULL)
    #    {
    #        DebugAllocatorAdapter<FifoAllocator>::VerifyDeletion(p, file, line, false);
    ##if ! USE_DEBUG_PTR
    #        DebugAllocatorAdapter<FifoAllocator>::Free(p);
    ##else
    #        size_t* px = reinterpret_cast<size_t*>(p) - 1;
    #        *px = AllocTag::IncreaseAge(*px);
    #        DebugAllocatorAdapter<FifoAllocator>::Free(px);
    ##endif
    #        DebugAllocatorAdapter<FifoAllocator>::MarkReleased(p, file, line, "delete");
    #    }
    #}

    ##else

    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
    ##define LG_NEW_M2 new
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
    ##define LG_DEL_MEM(p) delete (p)
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
    ##define LG_DEL_MEM_ARRAY(p) delete[] (p)
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
    ##define M2_PTR_REF(p) (p)
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
    ##define M2_PTR_DEREF(p) (*(p))

    ##endif

    @staticmethod
    def get_pointer(p):
        return p


    def left_shift(self, os, tag):
        return os << "<" << tag.file << " line:" << tag.line << " age:" << tag.age << ">"
    def equals_to(self, a, b):
        return a.Get() is b.Get()
    def not_equals_to(self, a, b):
        return a.Get() is not b.Get()

    def equals_to(self, a, b):
        return a.Get() is b
    def not_equals_to(self, a, b):
        return a.Get() is not b

    def equals_to(self, a, b):
        return a is b.Get()
    def not_equals_to(self, a, b):
        return a is not b.Get()

    @staticmethod
    def static_pointer_cast(o):
        return DebugPtr(o.Get(), o.GetAge())
    @staticmethod
    def const_pointer_cast(o):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no equivalent to 'const_cast' in Python:
        return DebugPtr(const_cast<T>(o.Get()), o.GetAge())
    @staticmethod
    def dynamic_pointer_cast(o):
        return DebugPtr(if isinstance(o.Get(), T) else None, o.GetAge())

    @staticmethod
    def get_pointer(ptr):
        return ptr.Get()

## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
    #extern list<CItemDropInfo> g_vec_pkCommonDropItem[MOB_RANK_MAX_NUM]
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##if __MULTI_LANGUAGE_SYSTEM__
    ##endif

    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##if __MULTI_LANGUAGE_SYSTEM__
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
    #locale_init(filename, locale)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
    #locale_find(string, locale = LOCALE_LANIATUS)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
    #get_locale(locale)

# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
    #locale_quest_translate_init(filename, locale)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
    #locale_quest_translate_find(vnum, locale = LOCALE_LANIATUS)

# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
    #locale_item_init(filename, locale)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
    #locale_item_find(vnum, locale = LOCALE_LANIATUS)

# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
    #locale_mob_init(filename, locale)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
    #locale_mob_find(vnum, locale = LOCALE_LANIATUS)

# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
    #locale_LG_SKILL_init(filename, locale)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
    #locale_LG_SKILL_find(vnum, locale = LOCALE_LANIATUS)
    ##else
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
    #locale_init(filename)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
    #locale_find(string)
    ##endif

    ## Laniatus Games Studio Inc. | NOTE: The following #define macro was replaced in-line:
    #ORIGINAL METINII C CODE: #define LC_TEXT(str) locale_find(str)

    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##if __MULTI_LANGUAGE_SYSTEM__
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
    ##define LC_LOCALE_TEXT(str, locale) locale_find(str, locale)
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
    ##define LC_LOCALE(locale) get_locale(locale)
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
    ##define LC_LOCALE_QUEST_TEXT(vnum, locale) locale_quest_translate_find(vnum, locale)
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
    ##define LC_LOCALE_ITEM_TEXT(vnum, locale) locale_item_find(vnum, locale)
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
    ##define LC_LOCALE_MOB_TEXT(vnum, locale) locale_mob_find(vnum, locale)
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
    ##define LC_LOCALE_LG_SKILL_TEXT(vnum, locale) locale_LG_SKILL_find(vnum, locale)
    ##endif


    DEFAULT_FREE_TRIGGER_COUNT = 32


    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: C++ 'constraints' are not converted by # Laniatus Games Studio Inc. |:
    #ORIGINAL METINII C CODE: template <typename OBJ, size_t FREE_TRIGGER>
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no equivalent in Python to templates on variables:
    LateAllocator = 0

    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: C++ 'constraints' are not converted by # Laniatus Games Studio Inc. |:
    #ORIGINAL METINII C CODE: template <typename OBJ, size_t FREE_TRIGGER>
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no equivalent in Python to templates on variables:
    LateAllocator = std::deque()

    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: C++ 'constraints' are not converted by # Laniatus Games Studio Inc. |:
    #ORIGINAL METINII C CODE: template <typename OBJ, size_t FREE_TRIGGER=DEFAULT_FREE_TRIGGER_COUNT>
    LG_HEADER_CG_HANDSHAKE = 0xff
    LG_HEADER_CG_PONG = 0xfe
    LG_HEADER_CG_TIME_SYNC = 0xfc
    int #if _IMPROVED_PACKET_ENCRYPTION_ = 253
    LG_HEADER_CG_KEY_AGREEMENT = 0xfb
    int #endif = 252
    LG_HEADER_CG_LOGIN = 1
    LG_HEADER_CG_ATTACK = 2
    LG_HEADER_CG_CHAT = 3
    LG_HEADER_CG_CHARACTER_CREATE = 4
    LG_HEADER_CG_CHARACTER_DELETE = 5
    LG_HEADER_CG_CHARACTER_SELECT = 6
    LG_HEADER_CG_MOVE = 7
    LG_HEADER_CG_SYNC_POSITION = 8
    LG_HEADER_CG_ENTERGAME = 10
    LG_HEADER_CG_ITEM_USE = 11
    LG_HEADER_CG_ITEM_DROP = 12
    LG_HEADER_CG_ITEM_MOVE = 13
    LG_HEADER_CG_ITEM_PICKUP = 15
    LG_HEADER_CG_LG_QUICKSLOT_ADD = 16
    LG_HEADER_CG_LG_QUICKSLOT_DEL = 17
    LG_HEADER_CG_LG_QUICKSLOT_SWAP = 18
    LG_HEADER_CG_WHISPER = 19
    LG_HEADER_CG_ITEM_DROP2 = 20
    LG_HEADER_CG_ITEM_DESTROY = 21
    LG_HEADER_CG_ON_CLICK = 26
    LG_HEADER_CG_EXCHANGE = 27
    LG_HEADER_CG_CHARACTER_POSITION = 28
    LG_HEADER_CG_SCRIPT_ANSWER = 29
    LG_HEADER_CG_QUEST_INPUT_STRING = 30
    LG_HEADER_CG_QUEST_CONFIRM = 31
    LG_HEADER_CG_SHOP = 50
    LG_HEADER_CG_FLY_TARGETING = 51
    LG_HEADER_CG_USE_SKILL = 52
    LG_HEADER_CG_ADD_FLY_TARGETING = 53
    LG_HEADER_CG_SHOOT = 54
    LG_HEADER_CG_MYSHOP = 55
    int #if ENABLE_TARGET_INFO = 56
    LG_HEADER_CG_TARGET_INFO_LOAD = 59
    int #endif = 60
    LG_HEADER_CG_ITEM_USE_TO_ITEM = 60
    LG_HEADER_CG_TARGET = 61
    LG_HEADER_CG_TEXT = 64
    LG_HEADER_CG_WARP = 65
    LG_HEADER_CG_SCRIPT_BUTTON = 66
    LG_HEADER_CG_MESSENGER = 67
    LG_HEADER_CG_MALL_CHECKOUT = 69
    LG_HEADER_CG_SAFEBOX_CHECKIN = 70
    LG_HEADER_CG_SAFEBOX_CHECKOUT = 71
    LG_HEADER_CG_PARTY_INVITE = 72
    LG_HEADER_CG_PARTY_INVITE_ANSWER = 73
    LG_HEADER_CG_PARTY_REMOVE = 74
    LG_HEADER_CG_PARTY_SET_STATE = 75
    LG_HEADER_CG_PARTY_USE_SKILL = 76
    LG_HEADER_CG_SAFEBOX_ITEM_MOVE = 77
    LG_HEADER_CG_PARTY_PARAMETER = 78
    LG_HEADER_CG_GUILD = 80
    LG_HEADER_CG_ANSWER_MAKE_GUILD = 81
    LG_HEADER_CG_FISHING = 82
    LG_HEADER_CG_ITEM_GIVE = 83
    LG_HEADER_CG_EMPIRE = 90
    LG_HEADER_CG_REFINE = 96
    LG_HEADER_CG_MARK_LOGIN = 100
    LG_HEADER_CG_MARK_CRCLIST = 101
    LG_HEADER_CG_MARK_UPLOAD = 102
    LG_HEADER_CG_MARK_IDXLIST = 104
    LG_HEADER_CG_HACK = 105
    LG_HEADER_CG_CHANGE_NAME = 106
    LG_HEADER_CG_LOGIN2 = 109
    LG_HEADER_CG_DUNGEON = 110
    LG_HEADER_CG_LOGIN3 = 111
    LG_HEADER_CG_GUILD_SYMBOL_UPLOAD = 112
    LG_HEADER_CG_SYMBOL_CRC = 113
    LG_HEADER_CG_SCRIPT_SELECT_ITEM = 114
    int #if __EXTENDED_WHISPER_DETAILS__ = 115
    LG_HEADER_CG_WHISPER_DETAILS = 120
    int #endif = 121
    LG_HEADER_CG_DRAGON_SOUL_REFINE = 205
    LG_HEADER_CG_STATE_CHECKER = 206
    LG_HEADER_CG_ACCE = 207
    int #if __MULTI_LANGUAGE_SYSTEM__ = 208
    LG_HEADER_CG_CHANGE_LANGUAGE = 230
    int #endif = 231
    LG_HEADER_CG_CLIENT_VERSION = 0xfd
    LG_HEADER_CG_CLIENT_VERSION2 = 0xf1
    int #if _IMPROVED_PACKET_ENCRYPTION_ = 242
    LG_HEADER_GC_KEY_AGREEMENT_COMPLETED = 0xfa
    LG_HEADER_GC_KEY_AGREEMENT = 0xfb
    int #endif = 252
    LG_HEADER_GC_TIME_SYNC = 0xfc
    LG_HEADER_GC_PHASE = 0xfd
    LG_HEADER_GC_BINDUDP = 0xfe
    LG_HEADER_GC_HANDSHAKE = 0xff
    LG_HEADER_GC_CHARACTER_ADD = 1
    LG_HEADER_GC_CHARACTER_DEL = 2
    LG_HEADER_GC_MOVE = 3
    LG_HEADER_GC_CHAT = 4
    LG_HEADER_GC_SYNC_POSITION = 5
    LG_HEADER_GC_LOGIN_SUCCESS = 6
    LG_HEADER_GC_LOGIN_SUCCESS_NEWSLOT = 32
    LG_HEADER_GC_LOGIN_FAILURE = 7
    LG_HEADER_GC_CHARACTER_CREATE_SUCCESS = 8
    LG_HEADER_GC_CHARACTER_CREATE_FAILURE = 9
    LG_HEADER_GC_CHARACTER_DELETE_SUCCESS = 10
    LG_HEADER_GC_CHARACTER_DELETE_WRONG_SOCIAL_ID = 11
    LG_HEADER_GC_ATTACK = 12
    LG_HEADER_GC_STUN = 13
    LG_HEADER_GC_DEAD = 14
    LG_HEADER_GC_MAIN_CHARACTER_OLD = 15
    LG_HEADER_GC_CHARACTER_POINTS = 16
    LG_HEADER_GC_CHARACTER_LG_POINT_CHANGE = 17
    LG_HEADER_GC_CHANGE_SPEED = 18
    LG_HEADER_GC_CHARACTER_UPDATE = 19
    LG_HEADER_GC_ITEM_DEL = 20
    LG_HEADER_GC_ITEM_SET = 21
    LG_HEADER_GC_ITEM_USE = 22
    LG_HEADER_GC_ITEM_DROP = 23
    LG_HEADER_GC_ITEM_UPDATE = 25
    LG_HEADER_GC_ITEM_GROUND_ADD = 26
    LG_HEADER_GC_ITEM_GROUND_DEL = 27
    LG_HEADER_GC_LG_QUICKSLOT_ADD = 28
    LG_HEADER_GC_LG_QUICKSLOT_DEL = 29
    LG_HEADER_GC_LG_QUICKSLOT_SWAP = 30
    LG_HEADER_GC_ITEM_OWNERSHIP = 31
    LG_HEADER_GC_WHISPER = 34
    LG_HEADER_GC_MOTION = 36
    LG_HEADER_GC_PARTS = 37
    LG_HEADER_GC_SHOP = 38
    LG_HEADER_GC_SHOP_SIGN = 39
    LG_HEADER_GC_PVP = 41
    LG_HEADER_GC_EXCHANGE = 42
    LG_HEADER_GC_CHARACTER_POSITION = 43
    LG_HEADER_GC_PING = 44
    LG_HEADER_GC_SCRIPT = 45
    LG_HEADER_GC_QUEST_CONFIRM = 46
    int #if ENABLE_TARGET_INFO = 47
    LG_HEADER_GC_TARGET_INFO = 58
    int #endif = 59
    LG_HEADER_GC_MOUNT = 61
    LG_HEADER_GC_OWNERSHIP = 62
    LG_HEADER_GC_TARGET = 63
    LG_HEADER_GC_WARP = 65
    LG_HEADER_GC_ADD_FLY_TARGETING = 69
    LG_HEADER_GC_CREATE_FLY = 70
    LG_HEADER_GC_FLY_TARGETING = 71
    LG_HEADER_GC_LG_SKILL_LEVEL_OLD = 72
    LG_HEADER_GC_LG_SKILL_LEVEL = 76
    LG_HEADER_GC_MESSENGER = 74
    LG_HEADER_GC_GUILD = 75
    LG_HEADER_GC_PARTY_INVITE = 77
    LG_HEADER_GC_PARTY_ADD = 78
    LG_HEADER_GC_PARTY_UPDATE = 79
    LG_HEADER_GC_PARTY_REMOVE = 80
    LG_HEADER_GC_QUEST_INFO = 81
    LG_HEADER_GC_REQUEST_MAKE_GUILD = 82
    LG_HEADER_GC_PARTY_PARAMETER = 83
    LG_HEADER_GC_SAFEBOX_SET = 85
    LG_HEADER_GC_SAFEBOX_DEL = 86
    LG_HEADER_GC_SAFEBOX_WRONG_PASSWORD = 87
    LG_HEADER_GC_SAFEBOX_SIZE = 88
    LG_HEADER_GC_FISHING = 89
    LG_HEADER_GC_EMPIRE = 90
    LG_HEADER_GC_PARTY_LINK = 91
    LG_HEADER_GC_PARTY_UNLINK = 92
    LG_HEADER_GC_REFINE_INFORMATION_OLD = 95
    LG_HEADER_GC_VIEW_EQUIP = 99
    LG_HEADER_GC_MARK_BLOCK = 100
    LG_HEADER_GC_MARK_IDXLIST = 102
    LG_HEADER_GC_TIME = 106
    LG_HEADER_GC_CHANGE_NAME = 107
    LG_HEADER_GC_DUNGEON = 110
    LG_HEADER_GC_WALK_MODE = 111
    LG_HEADER_GC_LG_SKILL_GROUP = 112
    LG_HEADER_GC_MAIN_CHARACTER = 113
    LG_HEADER_GC_SEPCIAL_EFFECT = 114
    LG_HEADER_GC_NPC_POSITION = 115
    LG_HEADER_GC_LOGIN_KEY = 118
    LG_HEADER_GC_REFINE_INFORMATION = 119
    LG_HEADER_GC_CHANNEL = 121
    LG_HEADER_GC_TARGET_UPDATE = 123
    LG_HEADER_GC_TARGET_DELETE = 124
    LG_HEADER_GC_TARGET_CREATE = 125
    LG_HEADER_GC_LANIA_AFFECT_ADD = 126
    LG_HEADER_GC_LANIA_AFFECT_REMOVE = 127
    LG_HEADER_GC_MALL_OPEN = 122
    LG_HEADER_GC_MALL_SET = 128
    LG_HEADER_GC_MALL_DEL = 129
    LG_HEADER_GC_LAND_LIST = 130
    LG_HEADER_GC_LOVER_INFO = 131
    LG_HEADER_GC_LOVE_LG_POINT_UPDATE = 132
    LG_HEADER_GC_SYMBOL_DATA = 133
    LG_HEADER_GC_DIG_MOTION = 134
    LG_HEADER_GC_DAMAGE_INFO = 135
    LG_HEADER_GC_CHAR_ADDITIONAL_INFO = 136
    LG_HEADER_GC_MAIN_CHARACTER3_BGM = 137
    LG_HEADER_GC_MAIN_CHARACTER4_BGM_VOL = 138
    LG_HEADER_GC_AUTH_SUCCESS = 150
    int #if __EXTENDED_WHISPER_DETAILS__ = 151
    LG_HEADER_GC_WHISPER_DETAILS = 160
    int #endif = 161
    LG_HEADER_GC_SPECIFIC_EFFECT = 208
    LG_HEADER_GC_DRAGON_SOUL_REFINE = 209
    LG_HEADER_GC_RESPOND_CHANNELSTATUS = 210
    LG_HEADER_GC_ACCE = 211
    int #if __MULTI_LANGUAGE_SYSTEM__ = 212
    LG_HEADER_GC_REQUEST_CHANGE_LANGUAGE = 216
    int #endif = 217
    LG_HEADER_GG_LOGIN = 1
    LG_HEADER_GG_LOGOUT = 2
    LG_HEADER_GG_RELAY = 3
    LG_HEADER_GG_NOTICE = 4
    LG_HEADER_GG_SHUTDOWN = 5
    LG_HEADER_GG_GUILD = 6
    LG_HEADER_GG_DISCONNECT = 7
    LG_HEADER_GG_SHOUT = 8
    LG_HEADER_GG_SETUP = 9
    LG_HEADER_GG_MESSENGER_ADD = 10
    LG_HEADER_GG_MESSENGER_REMOVE = 11
    LG_HEADER_GG_FIND_POSITION = 12
    LG_HEADER_GG_WARP_CHARACTER = 13
    LG_HEADER_GG_GUILD_WAR_ZONE_MAP_INDEX = 15
    LG_HEADER_GG_TRANSFER = 16
    LG_HEADER_GG_XMAS_WARP_SANTA = 17
    LG_HEADER_GG_XMAS_WARP_SANTA_REPLY = 18
    LG_HEADER_GG_RELOAD_CRC_LIST = 19
    LG_HEADER_GG_LOGIN_PING = 20
    LG_HEADER_GG_CHECK_CLIENT_VERSION = 21
    LG_HEADER_GG_BLOCK_CHAT = 22
    LG_HEADER_GG_CHECK_AWAKENESS = 29
    int #if __MULTI_LANGUAGE_SYSTEM__ = 30
    LG_HEADER_GG_LOCALE_NOTICE = 30
    int #endif = 31

    GUILD_SUBLG_HEADER_GG_CHAT = 0
    GUILD_SUBLG_HEADER_GG_SET_MEMBER_COUNT_BONUS = 1

    PARTY_SUBLG_HEADER_GG_CREATE = 0
    PARTY_SUBLG_HEADER_GG_DESTROY = 1
    PARTY_SUBLG_HEADER_GG_JOIN = 2
    PARTY_SUBLG_HEADER_GG_QUIT = 3

    SHOP_SUBLG_HEADER_CG_END = 0
    SHOP_SUBLG_HEADER_CG_BUY = 1
    SHOP_SUBLG_HEADER_CG_SELL = 2
    SHOP_SUBLG_HEADER_CG_SELL2 = 3

    EXCHANGE_SUBLG_HEADER_CG_START = 0
    EXCHANGE_SUBLG_HEADER_CG_ITEM_ADD = 1
    EXCHANGE_SUBLG_HEADER_CG_ITEM_DEL = 2
    EXCHANGE_SUBLG_HEADER_CG_ELK_ADD = 3
    EXCHANGE_SUBLG_HEADER_CG_ACCEPT = 4
    EXCHANGE_SUBLG_HEADER_CG_CANCEL = 5

    LOGIN_FAILURE_ALREADY = 1
    LOGIN_FAILURE_ID_NOT_EXIST = 2
    LOGIN_FAILURE_WRONG_PASS = 3
    LOGIN_FAILURE_FALSE = 4
    LOGIN_FAILURE_NOT_TESTOR = 5
    LOGIN_FAILURE_NOT_TEST_TIME = 6
    LOGIN_FAILURE_FULL = 7

    ADD_CHARACTER_STATE_DEAD = (1 << 0)
    ADD_CHARACTER_STATE_SPAWN = (1 << 1)
    ADD_CHARACTER_STATE_GUNGON = (1 << 2)
    ADD_CHARACTER_STATE_KILLER = (1 << 3)
    ADD_CHARACTER_STATE_PARTY = (1 << 4)

    MESSENGER_SUBLG_HEADER_GC_LIST = 0
    MESSENGER_SUBLG_HEADER_GC_LOGIN = 1
    MESSENGER_SUBLG_HEADER_GC_LOGOUT = 2
    MESSENGER_SUBLG_HEADER_GC_INVITE = 3
    MESSENGER_SUBLG_HEADER_GC_REMOVE_FRIEND = 4

    MESSENGER_SUBLG_HEADER_CG_ADD_BY_VID = 0
    MESSENGER_SUBLG_HEADER_CG_ADD_BY_NAME = 1
    MESSENGER_SUBLG_HEADER_CG_REMOVE = 2
    MESSENGER_SUBLG_HEADER_CG_INVITE_ANSWER = 3

    PARTY_LG_SKILL_HEAL = 1
    PARTY_LG_SKILL_WARP = 2

    SAFEBOX_MONEY_STATE_SAVE = 0
    SAFEBOX_MONEY_STATE_WITHDRAW = 1

    GUILD_SUBLG_HEADER_GC_LOGIN = 0
    GUILD_SUBLG_HEADER_GC_LOGOUT = 1
    GUILD_SUBLG_HEADER_GC_LIST = 2
    GUILD_SUBLG_HEADER_GC_GRADE = 3
    GUILD_SUBLG_HEADER_GC_ADD = 4
    GUILD_SUBLG_HEADER_GC_REMOVE = 5
    GUILD_SUBLG_HEADER_GC_GRADE_NAME = 6
    GUILD_SUBLG_HEADER_GC_GRADE_AUTH = 7
    GUILD_SUBLG_HEADER_GC_INFO = 8
    GUILD_SUBLG_HEADER_GC_COMMENTS = 9
    GUILD_SUBLG_HEADER_GC_CHANGE_EXP = 10
    GUILD_SUBLG_HEADER_GC_CHANGE_MEMBER_GRADE = 11
    GUILD_SUBLG_HEADER_GC_LG_SKILL_INFO = 12
    GUILD_SUBLG_HEADER_GC_CHANGE_MEMBER_GENERAL = 13
    GUILD_SUBLG_HEADER_GC_GUILD_INVITE = 14
    GUILD_SUBLG_HEADER_GC_WAR = 15
    GUILD_SUBLG_HEADER_GC_GUILD_NAME = 16
    GUILD_SUBLG_HEADER_GC_GUILD_WAR_LIST = 17
    GUILD_SUBLG_HEADER_GC_GUILD_WAR_END_LIST = 18
    GUILD_SUBLG_HEADER_GC_WAR_SCORE = 19
    GUILD_SUBLG_HEADER_GC_MONEY_CHANGE = 20

    FISHING_SUBLG_HEADER_GC_START = 0
    FISHING_SUBLG_HEADER_GC_STOP = 1
    FISHING_SUBLG_HEADER_GC_REACT = 2
    FISHING_SUBLG_HEADER_GC_SUCCESS = 3
    FISHING_SUBLG_HEADER_GC_FAIL = 4
    FISHING_SUBLG_HEADER_GC_FISH = 5

    DUNGEON_SUBLG_HEADER_GC_TIME_ATTACK_START = 0
    DUNGEON_SUBLG_HEADER_GC_DESTINATION_POSITION = 1

    WALKMODE_RUN = 0
    WALKMODE_WALK = 1
    ## Laniatus Games Studio Inc. | NOTE: This was formerly a static local variable declaration (not allowed in Python):
    encode_byte_a = str(['\0' for _ in range(8)])

    @staticmethod
    def encode_byte(ind):
        ## Laniatus Games Studio Inc. | NOTE: This static local variable declaration (not allowed in Python) has been moved just prior to the method:
        #    static char a[8]
        str(encode_byte_a) = ind
        return (encode_byte_a)

    ## Laniatus Games Studio Inc. | NOTE: This was formerly a static local variable declaration (not allowed in Python):
    encode_2bytes_a = str(['\0' for _ in range(8)])

    @staticmethod
    def encode_2bytes(ind):
        ## Laniatus Games Studio Inc. | NOTE: This static local variable declaration (not allowed in Python) has been moved just prior to the method:
        #    static char a[8]
        encode_2bytes_a = ind
        return (encode_2bytes_a)

    ## Laniatus Games Studio Inc. | NOTE: This was formerly a static local variable declaration (not allowed in Python):
    encode_4bytes_a = str(['\0' for _ in range(8)])

    @staticmethod
    def encode_4bytes(ind):
        ## Laniatus Games Studio Inc. | NOTE: This static local variable declaration (not allowed in Python) has been moved just prior to the method:
        #    static char a[8]
        int(encode_4bytes_a) = ind
        return (encode_4bytes_a)

    @staticmethod
    def decode_byte(a):
        return byte((int(a)))

    @staticmethod
    def decode_2bytes(a):
        return (a)

    @staticmethod
    def decode_4bytes(a):
        return (int(a))

    ## Laniatus Games Studio Inc. | NOTE: The following #define macro was replaced in-line:
    #ORIGINAL METINII C CODE: #define packet_encode(buf, data, len) __packet_encode(buf, data, len, __FILE__, __LINE__)


    @staticmethod
    def __packet_encode(pbuf, data, length, file, line):
        assert None is not pbuf
        assert None != data

        if buffer_has_space(pbuf) < length:
            return False

        buffer_write(pbuf, data, length)
        return True

    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##if _WIN32
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
    ##define INLINE inline
    ##else
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
    ##define INLINE __inline__
    ##endif

    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##if ! _WIN32
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
    ##define true (!false)
    ##endif

    ## Laniatus Games Studio Inc. | NOTE: The following #define macro was replaced in-line:
    #ORIGINAL METINII C CODE: #define FALSE false
    ## Laniatus Games Studio Inc. | NOTE: The following #define macro was replaced in-line:
    #ORIGINAL METINII C CODE: #define TRUE (!FALSE)

    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##if _WIN32
    ##define WIN32_LEAN_AND_MEAN

    ## Laniatus Games Studio Inc. | WARNING: The following #include directive was ignored:
    ##include <winsock2.h>
    ## Laniatus Games Studio Inc. | WARNING: The following #include directive was ignored:
    ##include <sys/types.h>
    ## Laniatus Games Studio Inc. | WARNING: The following #include directive was ignored:
    ##include <sys/stat.h>
    ## Laniatus Games Studio Inc. | WARNING: The following #include directive was ignored:
    ##include <process.h>
    ## Laniatus Games Studio Inc. | WARNING: The following #include directive was ignored:
    ##include <direct.h>
    ## Laniatus Games Studio Inc. | WARNING: The following #include directive was ignored:
    ##include <fcntl.h>


    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
    ##define S_ISDIR(m) (m & _S_IFDIR)

    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
    ##define strlcat(dst, src, size) strcat_s(dst, size, src)
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
    ##define strlcpy(dst, src, size) strncpy_s(dst, size, src, _TRUNCATE)
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
    ##define strcasecmp(s1, s2) _stricmp(s1, s2)
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
    ##define strncasecmp(s1, s2, n) _strnicmp(s1, s2, n)
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
    ##define strtok_r(s, delim, ptrptr) strtok_s(s, delim, ptrptr)
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
    ##define localtime_r(timet, result) localtime_s(result, timet)


    @staticmethod
    def usleep(usec):
        Sleep(math.trunc(usec / float(1000)))

    @staticmethod
    def sleep(sec):
        Sleep(sec * 1000)
        return 0

    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
    ##define PATH_MAX _MAX_PATH
    ##else
    ## Laniatus Games Studio Inc. | WARNING: The following #include directive was ignored:
    ##include <unistd.h>
    ## Laniatus Games Studio Inc. | WARNING: The following #include directive was ignored:
    ##include <fcntl.h>
    ## Laniatus Games Studio Inc. | WARNING: The following #include directive was ignored:
    ##include <dirent.h>

    ## Laniatus Games Studio Inc. | WARNING: The following #include directive was ignored:
    ##include <sys/stat.h>
    ## Laniatus Games Studio Inc. | WARNING: The following #include directive was ignored:
    ##include <sys/types.h>

    ## Laniatus Games Studio Inc. | WARNING: The following #include directive was ignored:
    ##include <netinet/in.h>
    ## Laniatus Games Studio Inc. | WARNING: The following #include directive was ignored:
    ##include <arpa/inet.h>
    ## Laniatus Games Studio Inc. | WARNING: The following #include directive was ignored:
    ##include <netdb.h>
    ## Laniatus Games Studio Inc. | WARNING: The following #include directive was ignored:
    ##include <sys/socket.h>

    ## Laniatus Games Studio Inc. | WARNING: The following #include directive was ignored:
    ##include <sys/wait.h>

    ## Laniatus Games Studio Inc. | WARNING: The following #include directive was ignored:
    ##include <pthread.h>
    ## Laniatus Games Studio Inc. | WARNING: The following #include directive was ignored:
    ##include <sys/event.h>
    ##endif


    ##define isdigit iswdigit
    ##define isspace iswspace
    ## Laniatus Games Studio Inc. | NOTE: The following #define macro was replaced in-line:
    #ORIGINAL METINII C CODE: #define PASSES_PER_SEC(sec) ((sec) * passes_per_sec)

    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##if _WIN32
    ##endif

    ##define IN
    ##define OUT

    UNIQUE_GROUP_LUCKY_GOLD = 10024
    UNIQUE_GROUP_AUTOLOOT = 10011
    UNIQUE_GROUP_RING_OF_EXP = 10000
    UNIQUE_GROUP_FISH_MIND = 10009
    UNIQUE_GROUP_LARGE_SAFEBOX = 10021
    UNIQUE_GROUP_DOUBLE_ITEM = 10002
    UNIQUE_GROUP_RING_OF_LANGUAGE = 10025
    UNIQUE_GROUP_SPECIAL_RIDE = 10030
    UNIQUE_GROUP_DRAGON_HEART = 10053
    UNIQUE_ITEM_TEARDROP_OF_GODNESS = 70012
    UNIQUE_ITEM_RING_OF_LANGUAGE = 70006
    UNIQUE_ITEM_RING_OF_LANGUAGE_SAMPLE = 70047
    UNIQUE_ITEM_WHITE_FLAG = 70008
    UNIQUE_ITEM_TREASURE_BOX = 70009
    UNIQUE_ITEM_CAPE_OF_COURAGE = 70038
    UNIQUE_ITEM_HALF_STAMINA = 70040
    UNIQUE_ITEM_HIDE_ALIGNMENT_TITLE = 70048
    UNIQUE_ITEM_SKIP_ITEM_DROP_PENALTY = 70049
    UNIQUE_ITEM_FASTER_ALIGNMENT_UP_BY_TIME = 70050
    UNIQUE_ITEM_FASTER_ALIGNMENT_UP_BY_KILL = 70051
    UNIQUE_ITEM_NO_BAD_LUCK_EFFECT = 70052
    UNIQUE_ITEM_LARBOR_MEDAL = 70004
    UNIQUE_ITEM_DOUBLE_EXP = 70005
    UNIQUE_ITEM_DOUBLE_ITEM = 70043
    UNIQUE_ITEM_PARTY_BONUS_EXP = 70003
    UNIQUE_ITEM_PARTY_BONUS_EXP_MALL = 71012
    UNIQUE_ITEM_PARTY_BONUS_EXP_GIFT = 76011
    ITEM_GIVE_STAT_RESET_COUNT_VNUM = 70014
    ITEM_SKILLFORGET_VNUM = 70037
    ITEM_SKILLFORGET2_VNUM = 70055
    UNIQUE_ITEM_FISH_MIND = 71008
    UNIQUE_ITEM_SAFEBOX_EXPAND = 71009
    UNIQUE_ITEM_AUTOLOOT_GOLD = 71010
    UNIQUE_ITEM_EMOTION_MASK = 71011
    UNIQUE_ITEM_EMOTION_MASK2 = 71033
    ITEM_NEW_YEAR_GREETING_VNUM = 50023
    ITEM_WONSO_BEAN_VNUM = 50020
    ITEM_WONSO_SUGAR_VNUM = 50021
    ITEM_WONSO_FRUIT_VNUM = 50022
    ITEM_VALENTINE_ROSE = 50024
    ITEM_VALENTINE_CHOCOLATE = 50025
    ITEM_WHITEDAY_CANDY = 50032
    ITEM_WHITEDAY_ROSE = 50031
    ITEM_HORSE_FOOD_1 = 50054
    ITEM_HORSE_FOOD_2 = 50055
    ITEM_HORSE_FOOD_3 = 50056
    ITEM_REVIVE_HORSE_1 = 50057
    ITEM_REVIVE_HORSE_2 = 50058
    ITEM_REVIVE_HORSE_3 = 50059
    ITEM_HORSE_LG_SKILL_TRAIN_BOOK = 50060
    UNIQUE_ITEM_MARRIAGE_PENETRATE_BONUS = 71069
    UNIQUE_ITEM_MARRIAGE_EXP_BONUS = 71070
    UNIQUE_ITEM_MARRIAGE_CRITICAL_BONUS = 71071
    UNIQUE_ITEM_MARRIAGE_TRANSFER_DAMAGE = 71072
    UNIQUE_ITEM_MARRIAGE_ATTACK_BONUS = 71073
    UNIQUE_ITEM_MARRIAGE_DEFENSE_BONUS = 71074
    ITEM_MARRIAGE_RING = 70302
    ITEM_MINING_LG_SKILL_TRAIN_BOOK = 50600
    ITEM_PRISM = 71113
    ITEM_AUTO_HP_RECOVERY_S = 72723
    ITEM_AUTO_HP_RECOVERY_M = 72724
    ITEM_AUTO_HP_RECOVERY_L = 72725
    ITEM_AUTO_HP_RECOVERY_X = 72726
    ITEM_AUTO_SP_RECOVERY_S = 72727
    ITEM_AUTO_SP_RECOVERY_M = 72728
    ITEM_AUTO_SP_RECOVERY_L = 72729
    ITEM_AUTO_SP_RECOVERY_X = 72730
    ITEM_RAMADAN_CANDY = 50183
    ITEM_NOG_POCKET = 50216
    REWARD_BOX_ITEM_AUTO_SP_RECOVERY_XS = 76004
    REWARD_BOX_ITEM_AUTO_SP_RECOVERY_S = 76005
    REWARD_BOX_ITEM_AUTO_HP_RECOVERY_S = 76021
    REWARD_BOX_ITEM_AUTO_HP_RECOVERY_XS = 76022
    FUCKING_BRAZIL_ITEM_AUTO_SP_RECOVERY_S = 79013
    FUCKING_BRAZIL_ITEM_AUTO_HP_RECOVERY_S = 79012
    REWARD_BOX_UNIQUE_ITEM_CAPE_OF_COURAGE = 76007
    DRAGON_SOUL_EXTRACTOR_GROUP = 10600
    DRAGON_HEART_EXTRACTOR_GROUP = 10601
    DRAGON_HEART_VNUM = 100000


# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
    #Normalize(pV1, pV2)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
    #GetDegreeFromPosition(x, y)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
    #GetDegreeFromPositionXY(sx, sy, ex, ey)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
    #GetDeltaByDegree(fDegree, fDistance, x, y)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
    #GetDegreeDelta(iDegree, iDegree2)
