import math

class TPoisonEventInfo(event_info_data):

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.ch = DynamicCharacterPtr()
        self.count = 0
        self.attacker_pid = 0

        self.ch = DynamicCharacterPtr()
        self.count = 0
        self.attacker_pid = 0

class TBleedingEventInfo(event_info_data):
    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.ch = DynamicCharacterPtr()
        self.count = 0
        self.attacker_pid = 0

        self.ch = DynamicCharacterPtr()
        self.count = 0
        self.attacker_pid = 0

##endif

class TFireEventInfo(event_info_data):

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.ch = DynamicCharacterPtr()
        self.count = 0
        self.amount = 0
        self.attacker_pid = 0

        self.ch = DynamicCharacterPtr()
        self.count = 0
        self.amount = 0
        self.attacker_pid = 0
##endif

def AttackedByFire(pkAttacker, amount, count):
    if m_pkFireEvent:
        return

    AddAffect(LaniatusEAffectTypes.LANIA_AFFECT_FIRE, EPointTypes.LG_POINT_NONE, 0, EAffectBits.AFF_FIRE, count *3+1, 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)))

    info = AllocEventInfo()

    info.ch = self
    info.count = count
    info.amount = amount
    info.attacker_pid = pkAttacker.GetPlayerID()

    m_pkFireEvent = event_create_ex(fire_event, info, 1)

def AttackedByPoison(pkAttacker):
    if m_pkPoisonEvent:
        return

    if m_bHasPoisoned and not IsPC():
        return

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if ENABLE_WOLFMAN
    if m_pkBleedingEvent:
        return

    if m_bHasBled and not IsPC():
        return
##endif

    if pkAttacker is not None and pkAttacker.GetLevel() < GetLevel():
        delta = GetLevel() - pkAttacker.GetLevel()

        if delta > 8:
            delta = 8

        if number(1, 100) > poison_level_adjust[delta]:
            return

    m_bHasPoisoned = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    AddAffect(LaniatusEAffectTypes.LANIA_AFFECT_POISON, EPointTypes.LG_POINT_NONE, 0, EAffectBits.AFF_POISON, POISON_LENGTH + 1, 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)))

    info = AllocEventInfo()

    info.ch = self
    info.count = 10
    info.attacker_pid = pkAttacker.GetPlayerID() if pkAttacker is not None ) else 0

    m_pkPoisonEvent = event_create_ex(poison_event, info, 1)

    if test_server and pkAttacker:
        buf = str(['\0' for _ in range(256)])
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        snprintf(buf, sizeof(buf), "POISON %s -> %s", pkAttacker.GetName(LOCALE_LANIATUS), GetName())
        pkAttacker.ChatPacket(EChatType.CHAT_TYPE_INFO, "%s", buf)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if ENABLE_WOLFMAN
def AttackedByBleeding(pkAttacker):
    if m_pkBleedingEvent:
        return

    if m_bHasBled and not IsPC():
        return

    if m_pkPoisonEvent:
        return

    if m_bHasPoisoned and not IsPC():
        return

    if pkAttacker is not None and pkAttacker.GetLevel() < GetLevel():
        delta = GetLevel() - pkAttacker.GetLevel()

        if delta > 8:
            delta = 8

        if number(1, 100) > bleeding_level_adjust[delta]:
            return

    m_bHasBled = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
    AddAffect(LaniatusEAffectTypes.LANIA_AFFECT_BLEEDING, EPointTypes.LG_POINT_NONE, 0, EAffectBits.AFF_BLEEDING, BLEEDING_LENGTH + 1, 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)))

    info = AllocEventInfo()

    info.ch = self
    info.count = 10
    info.attacker_pid = pkAttacker.GetPlayerID() if pkAttacker is not None else 0

    m_pkBleedingEvent = event_create_ex(bleeding_event, info, 1)

    if test_server and pkAttacker:
        buf = str(['\0' for _ in range(256)])
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        snprintf(buf, sizeof(buf), "BLEEDING %s -> %s", pkAttacker.GetName(LOCALE_LANIATUS), GetName())
        pkAttacker.ChatPacket(EChatType.CHAT_TYPE_INFO, "%s", buf)
##endif

def RemoveFire():
    RemoveAffect(LaniatusEAffectTypes.LANIA_AFFECT_FIRE)
    event_cancel(m_pkFireEvent)

def RemovePoison():
    RemoveAffect(LaniatusEAffectTypes.LANIA_AFFECT_POISON)
    event_cancel(m_pkPoisonEvent)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if ENABLE_WOLFMAN
def RemoveBleeding():
    RemoveAffect(LaniatusEAffectTypes.LANIA_AFFECT_BLEEDING)
    event_cancel(m_pkBleedingEvent)
##endif

def ApplyMobAttribute(table):
    i = 0
    while i < EMobEnchants.MOB_ENCHANTS_MAX_NUM:
        if table.cEnchants[i] != 0:
            ApplyPoint(aiMobEnchantApplyIdx[i], table.cEnchants[i])
        i += 1

    i = 0
    while i < EMobResists.MOB_RESISTS_MAX_NUM:
        if table.cResists[i] != 0:
            ApplyPoint(aiMobResistsApplyIdx[i], table.cResists[i])
        i += 1

def UpdateImmuneFlags():
    m_pointsInstant.dwImmuneFlag = 0

    i = 0
    while i < EWearPositions.WEAR_MAX_NUM:
        if GetWear(i):
            i2 = 0
            while i2 < EItemMisc.ITEM_APPLY_MAX_NUM:
                if GetWear(i).GetProto().aApplies[i2].bType == EApplyTypes.APPLY_NONE:
                    continue

                if GetWear(i).GetProto().aApplies[i2].bType == EApplyTypes.APPLY_IMMUNE_STUN:
                    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'SET_BIT' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
                    SET_BIT(m_pointsInstant.dwImmuneFlag, EImmuneFlags.IMMUNE_STUN)

                if GetWear(i).GetProto().aApplies[i2].bType == EApplyTypes.APPLY_IMMUNE_SLOW:
                    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'SET_BIT' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
                    SET_BIT(m_pointsInstant.dwImmuneFlag, EImmuneFlags.IMMUNE_SLOW)

                if GetWear(i).GetProto().aApplies[i2].bType == EApplyTypes.APPLY_IMMUNE_FALL:
                    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'SET_BIT' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
                    SET_BIT(m_pointsInstant.dwImmuneFlag, EImmuneFlags.IMMUNE_FALL)
                i2 += 1

            i3 = 0
            while i3 < EItemMisc.ITEM_ATTRIBUTE_MAX_NUM:
                if GetWear(i).GetAttributeType(i3):
                    ia = GetWear(i).GetAttribute(i3)

                    if ia.bType == EApplyTypes.APPLY_IMMUNE_STUN:
                        ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'SET_BIT' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
                        SET_BIT(m_pointsInstant.dwImmuneFlag, EImmuneFlags.IMMUNE_STUN)

                    if ia.bType == EApplyTypes.APPLY_IMMUNE_SLOW:
                        ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'SET_BIT' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
                        SET_BIT(m_pointsInstant.dwImmuneFlag, EImmuneFlags.IMMUNE_SLOW)

                    if ia.bType == EApplyTypes.APPLY_IMMUNE_FALL:
                        ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'SET_BIT' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
                        SET_BIT(m_pointsInstant.dwImmuneFlag, EImmuneFlags.IMMUNE_FALL)
                i3 += 1
        i += 1

def IsImmune(dwImmuneFlag):
    UpdateImmuneFlags()
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'IS_SET' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
    if IS_SET(m_pointsInstant.dwImmuneFlag, dwImmuneFlag):
        immune_pct = 100
        percent = number(1, 100)

        if percent <= immune_pct:
            if test_server and IsPC():
                ChatPacket(EChatType.CHAT_TYPE_PARTY, "<IMMUNE_SUCCESS> (%s)", GetName())

            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
        else:
            if test_server and IsPC():
                ChatPacket(EChatType.CHAT_TYPE_PARTY, "<IMMUNE_FAIL> (%s)", GetName())

            return LGEMiscellaneous.DEFINECONSTANTS.false

    if test_server and IsPC():
        ChatPacket(EChatType.CHAT_TYPE_PARTY, "<IMMUNE_FAIL> (%s) NO_IMMUNE_FLAG", GetName())

    return LGEMiscellaneous.DEFINECONSTANTS.false
