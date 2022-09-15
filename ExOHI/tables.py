from enum import Enum

# Laniatus Games Studio Inc. |  TODO TASK: There is no preprocessor in Python:
##pragma pack(1)
class ERequestChargeType(Enum):
    EREQUESTCHARGE_CASH = 0
    EREQUESTCHARGE_MILEAGE = 1

class SRequestChargeCash:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.dwAID = 0
        self.dwAmount = 0
        self.eChargeType = 0



class SSimplePlayer:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.dwID = 0
        self.szName = str(['\0' for _ in range((int)LGEMiscellaneous.CHARACTER_NAME_MAX_LEN + 1)])
        self.byJob = 0
        self.byLevel = 0
        self.dwPlayMinutes = 0
        self.byST = 0
        self.byHT = 0
        self.byDX = 0
        self.byIQ = 0
        self.wMainPart = 0
        self.bChangeName = 0
        self.wHairPart = 0
        self.dwAccePart = 0
        self.bDummy = [0 for _ in range(4)]
        self.x = 0
        self.y = 0
        self.lAddr = 0
        self.wPort = 0
        self.LG_SKILL_group = 0


class SAccountTable:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.id = 0
        self.login = str(['\0' for _ in range((int)LGEMiscellaneous.LOGIN_MAX_LEN + 1)])
        self.passwd = str(['\0' for _ in range((int)LGEMiscellaneous.PASSWD_MAX_LEN + 1)])
        self.social_id = str(['\0' for _ in range((int)LGEMiscellaneous.SOCIAL_ID_MAX_LEN + 1)])
        self.status = str(['\0' for _ in range((int)LGEMiscellaneous.ACCOUNT_STATUS_MAX_LEN + 1)])
        self.bEmpire = 0
        self.bLanguage = 0
        self.players = [SSimplePlayer() for _ in range((int)LGEMiscellaneous.PLAYER_PER_ACCOUNT)]

# Laniatus Games Studio Inc. |  TODO TASK: There is no preprocessor in Python:
##if __MULTI_LANGUAGE_SYSTEM__
##endif

class SPacketDGCreateSuccess:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.bAccountCharacterIndex = 0
        self.player = SSimplePlayer()


class TPlayerItemAttribute:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.bType = 0
        self.sValue = 0


class SPlayerItem:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.id = 0
        self.window = 0
        self.pos = 0
        self.count = 0
        self.vnum = 0
        self.alSockets = [0 for _ in range((int)EItemMisc.LG_ITEM_SOCKET_MAX_NUM)]
        self.aAttr = [TPlayerItemAttribute() for _ in range((int)EItemMisc.ITEM_ATTRIBUTE_MAX_NUM)]
        self.owner = 0


class SQuickslot:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.type = 0
        self.pos = 0


class SPlayerSkill:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.bMasterType = 0
        self.bLevel = 0
        self.tNextRead = time_t()


class THorseInfo:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.bLevel = 0
        self.bRiding = 0
        self.sStamina = 0
        self.sHealth = 0
        self.dwHorseHealthDropTime = 0


class SPlayerTable:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.id = 0
        self.name = str(['\0' for _ in range((int)LGEMiscellaneous.CHARACTER_NAME_MAX_LEN + 1)])
        self.ip = str(['\0' for _ in range((int)LGEMiscellaneous.LG_IP_ADDRESS_LENGTH + 1)])
        self.job = 0
        self.voice = 0
        self.level = 0
        self.level_step = 0
        self.st = 0
        self.ht = 0
        self.dx = 0
        self.iq = 0
        self.exp = 0
        self.gold = 0
        self.dir = 0
        self.x = 0
        self.y = 0
        self.z = 0
        self.lMapIndex = 0
        self.lExitX = 0
        self.lExitY = 0
        self.lExitMapIndex = 0
        self.hp = 0
        self.sp = 0
        self.sRandomHP = 0
        self.sRandomSP = 0
        self.playtime = 0
        self.stat_point = 0
        self.LG_SKILL_point = 0
        self.sub_LG_SKILL_point = 0
        self.horse_LG_SKILL_point = 0
        self.skills = [SPlayerSkill() for _ in range((int)LGEMiscellaneous.LG_SKILL_MAX_NUM)]
        self.quickslot = [SQuickslot() for _ in range((int)LGEMiscellaneous.LG_QUICKSLOT_MAX_NUM)]
        self.part_base = 0
        self.parts = [0 for _ in range((int)EParts.PART_MAX_NUM)]
        self.stamina = 0
        self.LG_SKILL_group = 0
        self.lAlignment = 0
        self.stat_reset_count = 0
        self.horse = THorseInfo()
        self.logoff_interval = 0
        self.aiPremiumTimes = [0 for _ in range((int)EPremiumTypes.PREMIUM_MAX_NUM)]


class SMobSkillLevel:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.dwVnum = 0
        self.bLevel = 0


class SEntityTable:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.dwVnum = 0


class SMobTable(SEntityTable):

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.szName = str(['\0' for _ in range((int)LGEMiscellaneous.CHARACTER_NAME_MAX_LEN + 1)])
        self.szLocaleName = str(['\0' for _ in range((int)LGEMiscellaneous.CHARACTER_NAME_MAX_LEN + 1)])
        self.bType = 0
        self.bRank = 0
        self.bBattleType = 0
        self.bLevel = 0
        self.bSize = 0
        self.dwGoldMin = 0
        self.dwGoldMax = 0
        self.dwExp = 0
        self.dwMaxHP = 0
        self.bRegenCycle = 0
        self.bRegenPercent = 0
        self.wDef = 0
        self.dwAIFlag = 0
        self.dwRaceFlag = 0
        self.dwImmuneFlag = 0
        self.bStr = 0
        self.bDex = 0
        self.bCon = 0
        self.bInt = 0
        self.dwDamageRange = [0 for _ in range(2)]
        self.sAttackSpeed = 0
        self.sMovingSpeed = 0
        self.bAggresiveHPPct = 0
        self.wAggressiveSight = 0
        self.wAttackRange = 0
        self.cEnchants = str(['\0' for _ in range((int)EMobEnchants.MOB_ENCHANTS_MAX_NUM)])
        self.cResists = str(['\0' for _ in range((int)EMobResists.MOB_RESISTS_MAX_NUM)])
        self.dwResurrectionVnum = 0
        self.dwDropItemVnum = 0
        self.bMountCapacity = 0
        self.bOnClickType = 0
        self.bEmpire = 0
        self.szFolder = str(['\0' for _ in range(64 + 1)])
        self.fDamMultiply = 0
        self.dwSummonVnum = 0
        self.dwDrainSP = 0
        self.dwMobColor = 0
        self.dwPolymorphItemVnum = 0
        self.Skills = [SMobSkillLevel() for _ in range((int)LGEMiscellaneous.MOB_LG_SKILL_MAX_NUM)]
        self.bBerserkPoint = 0
        self.bStoneSkinPoint = 0
        self.bGodSpeedPoint = 0
        self.bDeathBlowPoint = 0
        self.bRevivePoint = 0


class SSkillTable:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.dwVnum = 0
        self.szName = str(['\0' for _ in range(32 + 1)])
        self.bType = 0
        self.bMaxLevel = 0
        self.dwSplashRange = 0
        self.szPointOn = str(['\0' for _ in range(64)])
        self.szPointPoly = str(['\0' for _ in range(100 + 1)])
        self.szSPCostPoly = str(['\0' for _ in range(100 + 1)])
        self.szDurationPoly = str(['\0' for _ in range(100 + 1)])
        self.szDurationSPCostPoly = str(['\0' for _ in range(100 + 1)])
        self.szCooldownPoly = str(['\0' for _ in range(100 + 1)])
        self.szMasterBonusPoly = str(['\0' for _ in range(100 + 1)])
        self.szGrandMasterAddSPCostPoly = str(['\0' for _ in range(100 + 1)])
        self.dwFlag = 0
        self.dwAffectFlag = 0
        self.szPointOn2 = str(['\0' for _ in range(64)])
        self.szPointPoly2 = str(['\0' for _ in range(100 + 1)])
        self.szDurationPoly2 = str(['\0' for _ in range(100 + 1)])
        self.dwAffectFlag2 = 0
        self.szPointOn3 = str(['\0' for _ in range(64)])
        self.szPointPoly3 = str(['\0' for _ in range(100 + 1)])
        self.szDurationPoly3 = str(['\0' for _ in range(100 + 1)])
        self.bLevelStep = 0
        self.bLevelLimit = 0
        self.preSkillVnum = 0
        self.preSkillLevel = 0
        self.lMaxHit = 0
        self.szSplashAroundDamageAdjustPoly = str(['\0' for _ in range(100 + 1)])
        self.bSkillAttrType = 0
        self.dwTargetRange = 0


class SShopItemTable:
    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.vnum = 0
        self.count = 0
        self.pos = SItemPos()
        self.price = 0
        self.display_pos = 0
        self.alSockets = [0 for _ in range((int)EItemMisc.LG_ITEM_SOCKET_MAX_NUM)]
        self.aAttr = [TPlayerItemAttribute() for _ in range((int)EItemMisc.ITEM_ATTRIBUTE_MAX_NUM)]
        self.price_type = 1
        self.price_vnum = 0

# Laniatus Games Studio Inc. |  TODO TASK: The memory management function 'memset' has no equivalent in Python:
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        memset(self.alSockets, 0, sizeof(self.alSockets))
# Laniatus Games Studio Inc. |  TODO TASK: The memory management function 'memset' has no equivalent in Python:
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        memset(self.aAttr, 0, sizeof(self.aAttr))

# Laniatus Games Studio Inc. |  TODO TASK: The following method format was not recognized, possibly due to an unrecognized macro:
enum STableExTypes : decltype(SShopItemTable.price_type)
    EX_GOLD = 1, EX_SECONDARY, EX_ITEM, EX_EXP, EX_MAX,

class SShopTable:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.dwVnum = 0
        self.dwNPCVnum = 0
        self.byItemCount = 0
        self.items = [SShopItemTable() for _ in range((int)LGEMiscellaneous.SHOP_HOST_ITEM_MAX_NUM)]



class SQuestTable:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.dwPID = 0
        self.szName = str(['\0' for _ in range(DefineConstants.QUEST_NAME_MAX_LEN + 1)])
        self.szState = str(['\0' for _ in range(DefineConstants.QUEST_STATE_MAX_LEN + 1)])
        self.lValue = 0


class SItemLimit:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.bType = 0
        self.lValue = 0


class SItemApply:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.bType = 0
        self.lValue = 0


class SItemTable(SEntityTable):

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.dwVnumRange = 0
        self.szName = str(['\0' for _ in range((int)EItemMisc.ITEM_NAME_MAX_LEN + 1)])
        self.szLocaleName = str(['\0' for _ in range((int)EItemMisc.ITEM_NAME_MAX_LEN + 1)])
        self.bType = 0
        self.bSubType = 0
        self.bWeight = 0
        self.bSize = 0
        self.dwAntiFlags = 0
        self.dwFlags = 0
        self.dwWearFlags = 0
        self.dwImmuneFlag = 0
        self.lldGold = 0
        self.lldShopBuyPrice = 0
        self.aLimits = [SItemLimit() for _ in range((int)EItemMisc.ITEM_LIMIT_MAX_NUM)]
        self.aApplies = [SItemApply() for _ in range((int)EItemMisc.ITEM_APPLY_MAX_NUM)]
        self.alValues = [0 for _ in range((int)EItemMisc.ITEM_VALUES_MAX_NUM)]
        self.alSockets = [0 for _ in range((int)EItemMisc.LG_ITEM_SOCKET_MAX_NUM)]
        self.dwRefinedVnum = 0
        self.wRefineSet = 0
        self.bAlterToMagicItemPct = 0
        self.bSpecular = 0
        self.bGainSocketPct = 0
        self.sAddonType = 0
        self.cLimitRealTimeFirstUseIndex = '\0'
        self.cLimitTimerBasedOnWearIndex = '\0'


class TItemAttrTable:
    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.szApply = str(['\0' for _ in range((int)LGEMiscellaneous.APPLY_NAME_MAX_LEN + 1)])
        self.dwApplyIndex = 0
        self.dwProb = 0
        self.lValues = [0 for _ in range(5)]
        self.bMaxLevelBySet = [0 for _ in range((int)EAttributeSet.ATTRIBUTE_SET_MAX_NUM)]

        self.dwApplyIndex = 0
        self.dwProb = 0
        self.szApply = None
# Laniatus Games Studio Inc. |  TODO TASK: The memory management function 'memset' has no equivalent in Python:
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        memset(self.lValues, 0, sizeof(self.lValues))
# Laniatus Games Studio Inc. |  TODO TASK: The memory management function 'memset' has no equivalent in Python:
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        memset(self.bMaxLevelBySet, 0, sizeof(self.bMaxLevelBySet))


class SConnectTable:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.login = str(['\0' for _ in range((int)LGEMiscellaneous.LOGIN_MAX_LEN + 1)])
        self.ident = 0


class SLoginPacket:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.login = str(['\0' for _ in range((int)LGEMiscellaneous.LOGIN_MAX_LEN + 1)])
        self.passwd = str(['\0' for _ in range((int)LGEMiscellaneous.PASSWD_MAX_LEN + 1)])


class SPlayerLoadPacket:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.account_id = 0
        self.player_id = 0
        self.account_index = 0


class SPlayerCreatePacket:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.login = str(['\0' for _ in range((int)LGEMiscellaneous.LOGIN_MAX_LEN + 1)])
        self.passwd = str(['\0' for _ in range((int)LGEMiscellaneous.PASSWD_MAX_LEN + 1)])
        self.account_id = 0
        self.account_index = 0
        self.player_table = SPlayerTable()


class SPlayerDeletePacket:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.login = str(['\0' for _ in range((int)LGEMiscellaneous.LOGIN_MAX_LEN + 1)])
        self.player_id = 0
        self.account_index = 0
        self.private_code = str(['\0' for _ in range(8)])


class SLogoutPacket:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.login = str(['\0' for _ in range((int)LGEMiscellaneous.LOGIN_MAX_LEN + 1)])
        self.passwd = str(['\0' for _ in range((int)LGEMiscellaneous.PASSWD_MAX_LEN + 1)])


class SPlayerCountPacket:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.dwCount = 0



class SSafeboxTable:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.dwID = 0
        self.bSize = 0
        self.lldGold = 0
        self.wItemCount = 0


class SSafeboxChangeSizePacket:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.dwID = 0
        self.bSize = 0


class SSafeboxLoadPacket:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.dwID = 0
        self.szLogin = str(['\0' for _ in range((int)LGEMiscellaneous.LOGIN_MAX_LEN + 1)])
        self.szPassword = str(['\0' for _ in range(DefineConstants.SAFEBOX_PASSWORD_MAX_LEN + 1)])


class SSafeboxChangePasswordPacket:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.dwID = 0
        self.szOldPassword = str(['\0' for _ in range(DefineConstants.SAFEBOX_PASSWORD_MAX_LEN + 1)])
        self.szNewPassword = str(['\0' for _ in range(DefineConstants.SAFEBOX_PASSWORD_MAX_LEN + 1)])


class SSafeboxChangePasswordPacketAnswer:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.flag = 0


class SEmpireSelectPacket:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.dwAccountID = 0
        self.bEmpire = 0


class SPacketGDSetup:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.szPublicIP = str(['\0' for _ in range(16)])
        self.bChannel = 0
        self.wListenPort = 0
        self.wP2PPort = 0
        self.alMaps = [0 for _ in range(32)]
        self.dwLoginCount = 0
        self.bAuthServer = 0


class SPacketDGMapLocations:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.bCount = 0


class SMapLocation:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.alMaps = [0 for _ in range(32)]
        self.szHost = str(['\0' for _ in range((int)LGEMiscellaneous.LG_MAX_HOST_LENGTH + 1)])
        self.wPort = 0


class SPacketDGP2P:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.szHost = str(['\0' for _ in range((int)LGEMiscellaneous.LG_MAX_HOST_LENGTH + 1)])
        self.wPort = 0
        self.bChannel = 0


class SPacketGDDirectEnter:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.login = str(['\0' for _ in range((int)LGEMiscellaneous.LOGIN_MAX_LEN + 1)])
        self.passwd = str(['\0' for _ in range((int)LGEMiscellaneous.PASSWD_MAX_LEN + 1)])
        self.index = 0


class SPacketDGDirectEnter:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.accountTable = SAccountTable()
        self.playerTable = SPlayerTable()


# Laniatus Games Studio Inc. |  TODO TASK: There is no preprocessor in Python:
##if ! _IMPROVED_PACKET_ENCRYPTION_
class SPacketShutdown:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.state = False

# Laniatus Games Studio Inc. |  TODO TASK: Typedefs defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
#typedef SPacketShutdown TPacketShutdown;
##endif

class SPacketGuildSkillUpdate:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.guild_id = 0
        self.amount = 0
        self.LG_SKILL_levels = [0 for _ in range(12)]
        self.LG_SKILL_point = 0
        self.save = 0


class SPacketGuildExpUpdate:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.guild_id = 0
        self.amount = 0


class SPacketGuildChangeMemberData:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.guild_id = 0
        self.pid = 0
        self.offer = 0
        self.level = 0
        self.grade = 0


class SPacketDGLoginAlready:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.szLogin = str(['\0' for _ in range((int)LGEMiscellaneous.LOGIN_MAX_LEN + 1)])


class TPacketAffectElement:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.dwType = 0
        self.bApplyOn = 0
        self.lApplyValue = 0
        self.dwFlag = 0
        self.lDuration = 0
        self.lSPCost = 0


class SPacketGDAddAffect:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.dwPID = 0
        self.elem = TPacketAffectElement()


class SPacketGDRemoveAffect:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.dwPID = 0
        self.dwType = 0
        self.bApplyOn = 0


class SPacketGDHighscore:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.dwPID = 0
        self.lValue = 0
        self.cDir = '\0'
        self.szBoard = str(['\0' for _ in range(21)])


class SPacketPartyCreate:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.dwLeaderPID = 0


class SPacketPartyDelete:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.dwLeaderPID = 0


class SPacketPartyAdd:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.dwLeaderPID = 0
        self.dwPID = 0
        self.bState = 0


class SPacketPartyRemove:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.dwLeaderPID = 0
        self.dwPID = 0


class SPacketPartyStateChange:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.dwLeaderPID = 0
        self.dwPID = 0
        self.bRole = 0
        self.bFlag = 0


class SPacketPartySetMemberLevel:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.dwLeaderPID = 0
        self.dwPID = 0
        self.bLevel = 0


class SPacketGDBoot:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.dwItemIDRange = [0 for _ in range(2)]
        self.szIP = str(['\0' for _ in range(16)])


class SPacketGuild:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.dwGuild = 0
        self.dwInfo = 0


class SPacketGDGuildAddMember:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.dwPID = 0
        self.dwGuild = 0
        self.bGrade = 0


class SPacketDGGuildMember:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.dwPID = 0
        self.dwGuild = 0
        self.bGrade = 0
        self.isGeneral = 0
        self.bJob = 0
        self.bLevel = 0
        self.dwOffer = 0
        self.szName = str(['\0' for _ in range((int)LGEMiscellaneous.CHARACTER_NAME_MAX_LEN + 1)])


class SPacketGuildWar:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.bType = 0
        self.bWar = 0
        self.dwGuildFrom = 0
        self.dwGuildTo = 0
        self.lWarPrice = 0
        self.lInitialScore = 0


class SPacketGuildWarScore:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.dwGuildGainPoint = 0
        self.dwGuildOpponent = 0
        self.lScore = 0
        self.lBetScore = 0


class SRefineMaterial:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.vnum = 0
        self.count = 0


class SRefineTable:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.id = 0
        self.material_count = 0
        self.cost = 0
        self.prob = 0
        self.materials = [SRefineMaterial() for _ in range((int)EItemMisc.REFINE_MATERIAL_MAX_NUM)]


class SPacketGDChangeName:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.pid = 0
        self.name = str(['\0' for _ in range((int)LGEMiscellaneous.CHARACTER_NAME_MAX_LEN + 1)])


class SPacketDGChangeName:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.pid = 0
        self.name = str(['\0' for _ in range((int)LGEMiscellaneous.CHARACTER_NAME_MAX_LEN + 1)])


class SPacketGuildLadder:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.dwGuild = 0
        self.lLadderPoint = 0
        self.lWin = 0
        self.lDraw = 0
        self.lLoss = 0


class SPacketGuildLadderPoint:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.dwGuild = 0
        self.lChange = 0


class SPacketGuildUseSkill:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.dwGuild = 0
        self.dwSkillVnum = 0
        self.dwCooltime = 0


class SPacketGuildSkillUsableChange:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.dwGuild = 0
        self.dwSkillVnum = 0
        self.bUsable = 0


class SPacketGDLoginKey:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.dwAccountID = 0
        self.dwLoginKey = 0


class SPacketGDAuthLogin:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.dwID = 0
        self.dwLoginKey = 0
        self.szLogin = str(['\0' for _ in range((int)LGEMiscellaneous.LOGIN_MAX_LEN + 1)])
        self.szSocialID = str(['\0' for _ in range((int)LGEMiscellaneous.SOCIAL_ID_MAX_LEN + 1)])
        self.adwClientKey = [0 for _ in range(4)]
        self.iPremiumTimes = [0 for _ in range((int)EPremiumTypes.PREMIUM_MAX_NUM)]
        self.bLanguage = 0

# Laniatus Games Studio Inc. |  TODO TASK: There is no preprocessor in Python:
##if __MULTI_LANGUAGE_SYSTEM__
##endif

class SPacketGDLoginByKey:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.szLogin = str(['\0' for _ in range((int)LGEMiscellaneous.LOGIN_MAX_LEN + 1)])
        self.dwLoginKey = 0
        self.adwClientKey = [0 for _ in range(4)]
        self.szIP = str(['\0' for _ in range((int)LGEMiscellaneous.LG_MAX_HOST_LENGTH + 1)])


class SPacketGiveGuildPriv:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.type = 0
        self.value = 0
        self.guild_id = 0
        self.duration_sec = time_t()

class SPacketGiveEmpirePriv:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.type = 0
        self.value = 0
        self.empire = 0
        self.duration_sec = time_t()

class SPacketGiveCharacterPriv:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.type = 0
        self.value = 0
        self.pid = 0

class SPacketRemoveGuildPriv:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.type = 0
        self.guild_id = 0

class SPacketRemoveEmpirePriv:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.type = 0
        self.empire = 0


class SPacketDGChangeCharacterPriv:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.type = 0
        self.value = 0
        self.pid = 0
        self.bLog = 0


class SPacketDGChangeGuildPriv:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.type = 0
        self.value = 0
        self.guild_id = 0
        self.bLog = 0
        self.end_time_sec = time_t()


class SPacketDGChangeEmpirePriv:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.type = 0
        self.value = 0
        self.empire = 0
        self.bLog = 0
        self.end_time_sec = time_t()


class SPacketGDGuildMoney:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.dwGuild = 0
        self.iGold = 0


class SPacketDGGuildMoneyChange:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.dwGuild = 0
        self.iTotalGold = 0


class SPacketDGGuildMoneyWithdraw:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.dwGuild = 0
        self.iChangeGold = 0


class SPacketGDGuildMoneyWithdrawGiveReply:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.dwGuild = 0
        self.iChangeGold = 0
        self.bGiveSuccess = 0


class SPacketSetEventFlag:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.szFlagName = str(['\0' for _ in range((int)LGEMiscellaneous.EVENT_FLAG_NAME_MAX_LEN + 1)])
        self.lValue = 0


class SPacketLoginOnSetup:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.dwID = 0
        self.szLogin = str(['\0' for _ in range((int)LGEMiscellaneous.LOGIN_MAX_LEN + 1)])
        self.szSocialID = str(['\0' for _ in range((int)LGEMiscellaneous.SOCIAL_ID_MAX_LEN + 1)])
        self.szHost = str(['\0' for _ in range((int)LGEMiscellaneous.LG_MAX_HOST_LENGTH + 1)])
        self.dwLoginKey = 0
        self.adwClientKey = [0 for _ in range(4)]
        self.bLanguage = 0

# Laniatus Games Studio Inc. |  TODO TASK: There is no preprocessor in Python:
##if __MULTI_LANGUAGE_SYSTEM__
##endif

class SPacketGDCreateObject:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.dwVnum = 0
        self.dwLandID = 0
        self.lMapIndex = 0
        self.x = 0
        self.y = 0
        self.xRot = 0
        self.yRot = 0
        self.zRot = 0


class SGuildReserve:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.dwID = 0
        self.dwGuildFrom = 0
        self.dwGuildTo = 0
        self.dwTime = 0
        self.bType = 0
        self.lWarPrice = 0
        self.lInitialScore = 0
        self.bStarted = False
        self.dwBetFrom = 0
        self.dwBetTo = 0
        self.lPowerFrom = 0
        self.lPowerTo = 0
        self.lHandicap = 0


class TPacketGDGuildWarBet:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.dwWarID = 0
        self.szLogin = str(['\0' for _ in range((int)LGEMiscellaneous.LOGIN_MAX_LEN + 1)])
        self.lldGold = 0
        self.dwGuild = 0


class TPacketMarriageAdd:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.dwPID1 = 0
        self.dwPID2 = 0
        self.tMarryTime = time_t()
        self.szName1 = str(['\0' for _ in range((int)LGEMiscellaneous.CHARACTER_NAME_MAX_LEN + 1)])
        self.szName2 = str(['\0' for _ in range((int)LGEMiscellaneous.CHARACTER_NAME_MAX_LEN + 1)])


class TPacketMarriageUpdate:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.dwPID1 = 0
        self.dwPID2 = 0
        self.iLovePoint = 0
        self.byMarried = 0


class TPacketMarriageRemove:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.dwPID1 = 0
        self.dwPID2 = 0


class TPacketWeddingRequest:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.dwPID1 = 0
        self.dwPID2 = 0


class TPacketWeddingReady:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.dwPID1 = 0
        self.dwPID2 = 0
        self.dwMapIndex = 0


class TPacketWeddingStart:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.dwPID1 = 0
        self.dwPID2 = 0


class TPacketWeddingEnd:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.dwPID1 = 0
        self.dwPID2 = 0



class SPacketMyshopPricelistHeader:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.dwOwnerID = 0
        self.wCount = 0


class SItemPriceInfo:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.dwVnum = 0
        self.lldPrice = 0


class SItemPriceListTable:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.dwOwnerID = 0
        self.wCount = 0
        self.aPriceInfo = [SItemPriceInfo() for _ in range((int)LGEMiscellaneous.SHOP_PRICELIST_MAX_NUM)]


class TPacketBlockChat:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.szName = str(['\0' for _ in range((int)LGEMiscellaneous.CHARACTER_NAME_MAX_LEN + 1)])
        self.lDuration = 0


class TAdminInfo:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.m_ID = 0
        self.m_szAccount = str(['\0' for _ in range(32)])
        self.m_szName = str(['\0' for _ in range(32)])
        self.m_szContactIP = str(['\0' for _ in range(16)])
        self.m_szServerIP = str(['\0' for _ in range(16)])
        self.m_Authority = 0


class tLocale:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.szValue = str(['\0' for _ in range(32)])
        self.szKey = str(['\0' for _ in range(32)])


class SPacketReloadAdmin:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.szIP = str(['\0' for _ in range(16)])


class tChangeGuildMaster:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.dwGuildID = 0
        self.idFrom = 0
        self.idTo = 0


class tItemIDRange:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.dwMin = 0
        self.dwMax = 0
        self.dwUsableItemIDMin = 0


class tUpdateHorseName:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.dwPlayerID = 0
        self.szHorseName = str(['\0' for _ in range((int)LGEMiscellaneous.CHARACTER_NAME_MAX_LEN + 1)])


class tDC:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.login = str(['\0' for _ in range((int)LGEMiscellaneous.LOGIN_MAX_LEN + 1)])


class tNeedLoginLogInfo:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.dwPlayerID = 0
        self.bLanguage = 0

# Laniatus Games Studio Inc. |  TODO TASK: There is no preprocessor in Python:
##if __MULTI_LANGUAGE_SYSTEM__
##endif

class tItemAwardInformer:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.login = str(['\0' for _ in range((int)LGEMiscellaneous.LOGIN_MAX_LEN + 1)])
        self.command = str(['\0' for _ in range(20)])
        self.vnum = 0


class tDeleteAwardID:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.dwID = 0


class SChannelStatus:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.nPort = 0
        self.bStatus = 0


# Laniatus Games Studio Inc. |  TODO TASK: There is no preprocessor in Python:
##if __MULTI_LANGUAGE_SYSTEM__
class SRequestChangeLanguage:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.dwAID = 0
        self.bLanguage = 0

# Laniatus Games Studio Inc. |  TODO TASK: Typedefs defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
#typedef SRequestChangeLanguage TRequestChangeLanguage;
##endif

# Laniatus Games Studio Inc. |  TODO TASK: There is no preprocessor in Python:
##pragma pack()
