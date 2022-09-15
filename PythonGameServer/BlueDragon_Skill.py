import math

class FSkillBreath:

    def __init__(self, p):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.Set1 = EJobs()
        self.Set2 = EJobs()
        self.gender = ESex()
        self.pAttacker = LPCHARACTER()

## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: pAttacker = p;
        self.pAttacker.copy_from(p)

        self.Set1 = number(0,3)
        self.Set2 = number(0,3)
        self.gender = number(0,2)

    def functor_method(self, ent):
        if None is not ent:
            if True == ent.IsType(ENTITY_CHARACTER):
                ch = ent

                if True == ch.IsPC() and False == ch.IsDead():
                    if None != ch.FindAffect(LANIA_AFFECT_REVIVE_INVISIBLE, APPLY_NONE):
                        return

                    if int(BlueDragon_GetSkillFactor(2, "Skill0", "damage_area")) < DISTANCE_APPROX(self.pAttacker.GetX()-ch.GetX(), self.pAttacker.GetY()-ch.GetY()):
                        #sys_log(0, "BlueDragon: Breath too far (%d)", DISTANCE_APPROX(self.pAttacker.GetX()-ch.GetX(), self.pAttacker.GetY()-ch.GetY()))
                        return

                    overlapDamageCount = 0

                    pct = 0
                    if ch.GetJob() is self.Set1:
                        ptr = None

                        if self.Set1 is JOB_LG_PAWN_WARRIOR:
                            ptr = "musa"
                        elif self.Set1 is JOB_LG_PAWN_ASSASSIN:
                            ptr = "assa"
                        elif self.Set1 is JOB_LG_PAWN_SHURA:
                            ptr = "LG_PAWN_SHURA"
                        elif self.Set1 is JOB_LG_PAWN_MAGE:
                            ptr = "muda"
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if ENABLE_WOLFMAN
                        # elif self.Set1 is JOB_WOLFMAN:
                            # ptr = "wolf" 
##endif

                        else:
                            return


                        firstDamagePercent = number(BlueDragon_GetSkillFactor(4, "Skill0", "damage", ptr, "min"), BlueDragon_GetSkillFactor(4, "Skill0", "damage", ptr, "max"))
                        pct += firstDamagePercent

                        if firstDamagePercent > 0:
                            overlapDamageCount += 1

                    if ch.GetJob() is self.Set2:
                        ptr = None

                        if self.Set2 is JOB_LG_PAWN_WARRIOR:
                            ptr = "musa"
                        elif self.Set2 is JOB_LG_PAWN_ASSASSIN:
                            ptr = "assa"
                        elif self.Set2 is JOB_LG_PAWN_SHURA:
                            ptr = "LG_PAWN_SHURA"
                        elif self.Set2 is JOB_LG_PAWN_MAGE:
                            ptr = "muda"
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if ENABLE_WOLFMAN
                        elif self.Set2 is JOB_WOLFMAN:
                            ptr = "wolf"
##endif

                        else:
                            return

                        secondDamagePercent = number(BlueDragon_GetSkillFactor(4, "Skill0", "damage", ptr, "min"), BlueDragon_GetSkillFactor(4, "Skill0", "damage", ptr, "max"))
                        pct += secondDamagePercent

                        if secondDamagePercent > 0:
                            overlapDamageCount += 1

                    if GET_SEX(ch) is self.gender:
                        ptr = None

                        if self.gender is LG_SEX_MALE:
                            ptr = "male"
                        elif self.gender is LG_SEX_FEMALE:
                            ptr = "female"
                        else:
                            return

                        thirdDamagePercent = number(BlueDragon_GetSkillFactor(4, "Skill0", "gender", ptr, "min"), BlueDragon_GetSkillFactor(4, "Skill0", "gender", ptr, "max"))
                        pct += thirdDamagePercent

                        if thirdDamagePercent > 0:
                            overlapDamageCount += 1

                    if overlapDamageCount == 1:
                        ch.EffectPacket(SE_PERCENT_DAMAGE1)
                    elif overlapDamageCount == 2:
                        ch.EffectPacket(SE_PERCENT_DAMAGE2)
                    elif overlapDamageCount == 3:
                        ch.EffectPacket(SE_PERCENT_DAMAGE3)

                    addPct = BlueDragon_GetRangeFactor("hp_damage", self.pAttacker.GetHPPct())

                    pct += addPct

                    dam = number(BlueDragon_GetSkillFactor(3, "Skill0", "default_damage", "min"), BlueDragon_GetSkillFactor(3, "Skill0", "default_damage", "max"))

                    dam += math.trunc((dam * addPct) / float(100))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
                    dam += (ch.GetMaxHP() * pct) / 100

                    ch.Damage(self.pAttacker, dam, DAMAGE_TYPE_ICE)

                    #sys_log(0, "BlueDragon: Breath to %s pct(%d) dam(%d) overlap(%d)", ch.GetName(), pct, dam, overlapDamageCount)

class FSkillWeakBreath:

    def __init__(self, p):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.pAttacker = LPCHARACTER()

## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: pAttacker = p;
        self.pAttacker.copy_from(p)

    def functor_method(self, ent):
        if None is not ent:
            if True == ent.IsType(ENTITY_CHARACTER):
                ch = ent

                if True == ch.IsPC() and False == ch.IsDead():
                    if None != ch.FindAffect(LANIA_AFFECT_REVIVE_INVISIBLE, APPLY_NONE):
                        return

                    if int(BlueDragon_GetSkillFactor(2, "Skill1", "damage_area")) < DISTANCE_APPROX(self.pAttacker.GetX()-ch.GetX(), self.pAttacker.GetY()-ch.GetY()):
                        #sys_log(0, "BlueDragon: Breath too far (%d)", DISTANCE_APPROX(self.pAttacker.GetX()-ch.GetX(), self.pAttacker.GetY()-ch.GetY()))
                        return

                    addPct = BlueDragon_GetRangeFactor("hp_damage", self.pAttacker.GetHPPct())

                    dam = number(BlueDragon_GetSkillFactor(3, "Skill1", "default_damage", "min"), BlueDragon_GetSkillFactor(3, "Skill1", "default_damage", "max"))
                    dam += math.trunc((dam * addPct) / float(100))

                    ch.Damage(self.pAttacker, dam, DAMAGE_TYPE_ICE)

                    #sys_log(0, "BlueDragon: WeakBreath to %s addPct(%d) dam(%d)", ch.GetName(), addPct, dam)

class FSkillEarthQuake:

    def __init__(self, p):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.Set1 = EJobs()
        self.Set2 = EJobs()
        self.gender = ESex()
        self.MaxDistance = 0
        self.pAttacker = LPCHARACTER()
        self.pFarthestChar = LPCHARACTER()

## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: pAttacker = p;
        self.pAttacker.copy_from(p)

        self.MaxDistance = 0
        self.pFarthestChar = None

        self.Set1 = number(0,3)
        self.Set2 = number(0,3)
        self.gender = number(0,2)

    def functor_method(self, ent):
        if None is not ent:
            if True == ent.IsType(ENTITY_CHARACTER):
                ch = ent

                if True == ch.IsPC() and False == ch.IsDead():
                    if None != ch.FindAffect(LANIA_AFFECT_REVIVE_INVISIBLE, APPLY_NONE):
                        return

                    if int(BlueDragon_GetSkillFactor(2, "Skill2", "damage_area")) < DISTANCE_APPROX(self.pAttacker.GetX()-ch.GetX(), self.pAttacker.GetY()-ch.GetY()):
                        #sys_log(0, "BlueDragon: Breath too far (%d)", DISTANCE_APPROX(self.pAttacker.GetX()-ch.GetX(), self.pAttacker.GetY()-ch.GetY()))
                        return

                    sec = number(BlueDragon_GetSkillFactor(4, "Skill2", "stun_time", "default", "min"), BlueDragon_GetSkillFactor(4, "Skill2", "stun_time", "default", "max"))

                    if ch.GetJob() is self.Set1:
                        ptr = None

                        if self.Set1 is JOB_LG_PAWN_WARRIOR:
                            ptr = "musa"
                        elif self.Set1 is JOB_LG_PAWN_ASSASSIN:
                            ptr = "assa"
                        elif self.Set1 is JOB_LG_PAWN_SHURA:
                            ptr = "LG_PAWN_SHURA"
                        elif self.Set1 is JOB_LG_PAWN_MAGE:
                            ptr = "muda"
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if ENABLE_WOLFMAN
                        elif self.Set1 is JOB_WOLFMAN:
                            ptr = "wolf"
##endif

                        else:
                            return

                        sec += number(BlueDragon_GetSkillFactor(4, "Skill2", "stun_time", ptr, "min"), BlueDragon_GetSkillFactor(4, "Skill2", "stun_time", ptr, "max"))

                    if ch.GetJob() is self.Set2:
                        ptr = None

                        if self.Set2 is JOB_LG_PAWN_WARRIOR:
                            ptr = "musa"
                        elif self.Set2 is JOB_LG_PAWN_ASSASSIN:
                            ptr = "assa"
                        elif self.Set2 is JOB_LG_PAWN_SHURA:
                            ptr = "LG_PAWN_SHURA"
                        elif self.Set2 is JOB_LG_PAWN_MAGE:
                            ptr = "muda"
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if ENABLE_WOLFMAN
                        elif self.Set2 is JOB_WOLFMAN:
                            ptr = "wolf"
##endif

                        else:
                            return

                        sec += number(BlueDragon_GetSkillFactor(4, "Skill2", "stun_time", ptr, "min"), BlueDragon_GetSkillFactor(4, "Skill2", "stun_time", ptr, "max"))

                    if GET_SEX(ch) is self.gender:
                        ptr = None

                        if self.gender is LG_SEX_MALE:
                            ptr = "male"
                        elif self.gender is LG_SEX_FEMALE:
                            ptr = "female"
                        else:
                            return

                        sec += number(BlueDragon_GetSkillFactor(4, "Skill2", "gender", ptr, "min"), BlueDragon_GetSkillFactor(4, "Skill2", "gender", ptr, "max"))

                    addPct = BlueDragon_GetRangeFactor("hp_damage", self.pAttacker.GetHPPct())

                    dam = number(BlueDragon_GetSkillFactor(3, "Skill2", "default_damage", "min"), BlueDragon_GetSkillFactor(3, "Skill2", "default_damage", "max"))
                    dam += math.trunc((dam * addPct) / float(100))

                    ch.Damage(self.pAttacker, dam, DAMAGE_TYPE_ICE)

                    SkillAttackAffect(ch, 1000, IMMUNE_STUN, LANIA_AFFECT_STUN, LG_POINT_NONE, 0, AFF_STUN, sec, "BDRAGON_STUN")

                    #sys_log(0, "BlueDragon: EarthQuake to %s addPct(%d) dam(%d) sec(%d)", ch.GetName(), addPct, dam, sec)


                    vec = VECTOR()
                    vec.x = float((self.pAttacker.GetX() - ch.GetX()))
                    vec.y = float((self.pAttacker.GetY() - ch.GetY()))
                    vec.z = 0.0

                    Normalize(vec, vec)

                    NFLYDISTANCE = 1000

                    tx = ch.GetX() + vec.x * NFLYDISTANCE
                    ty = ch.GetY() + vec.y * NFLYDISTANCE

                    for i in range(0, 5):
                        if True == SECTREE_MANAGER.instance().IsMovablePosition(ch.GetMapIndex(), tx, ty):
                            break

                        if i == 0:
                            tx = ch.GetX() + vec.x * NFLYDISTANCE * -1
                            ty = ch.GetY() + vec.y * NFLYDISTANCE * -1
                        elif i == 1:
                            tx = ch.GetX() + vec.x * NFLYDISTANCE * -1
                            ty = ch.GetY() + vec.y * NFLYDISTANCE
                        elif i == 2:
                            tx = ch.GetX() + vec.x * NFLYDISTANCE
                            ty = ch.GetY() + vec.y * NFLYDISTANCE * -1
                        elif i == 3:
                            tx = ch.GetX() + vec.x * number(1,100)
                            ty = ch.GetY() + vec.y * number(1,100)
                        elif i == 4:
                            tx = ch.GetX() + vec.x * number(1,10)
                            ty = ch.GetY() + vec.y * number(1,10)

                    ch.Sync(tx, ty)
                    ch.Goto(tx, ty)
                    ch.CalculateMoveDuration()

                    ch.SyncPacket()

                    dist = DISTANCE_APPROX(self.pAttacker.GetX() - ch.GetX(), self.pAttacker.GetY() - ch.GetY())

                    if dist > self.MaxDistance:
                        self.MaxDistance = dist
## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: pFarthestChar = ch;
                        self.pFarthestChar.copy_from(ch)
