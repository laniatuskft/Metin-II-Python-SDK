from enum import Enum

class LGEMiscellaneous(Enum):
    LG_MAX_HOST_LENGTH = 15
    LG_IP_ADDRESS_LENGTH = 15
    LOGIN_MAX_LEN = 30
    PASSWD_MAX_LEN = 16
    PLAYER_PER_ACCOUNT = 4
    ACCOUNT_STATUS_MAX_LEN = 8
    CHARACTER_NAME_MAX_LEN = 48
    SHOP_SIGN_MAX_LEN = 32
    ABILITY_MAX_NUM = 50
    EMPIRE_MAX_NUM = 4
    SOCIAL_ID_MAX_LEN = 18
    GUILD_NAME_MAX_LEN = 12
    SHOP_HOST_ITEM_MAX_NUM = 40
    SHOP_GUEST_ITEM_MAX_NUM = 18
    SHOP_PRICELIST_MAX_NUM = 40
    CHAT_MAX_LEN = 512
    LG_QUICKSLOT_MAX_NUM = 36
    QUERY_MAX_LEN = 8192
    PLAYER_EXP_TABLE_MAX = 150
    PLAYER_MAX_LEVEL_CONST = 150
    GUILD_MAX_LEVEL = 20
    LG_SKILL_MAX_NUM = 255
    SKILLBOOK_DELAY_MIN = 64800
    SKILLBOOK_DELAY_MAX = 108000
    LG_SKILL_MAX_LEVEL = 40
    APPLY_NAME_MAX_LEN = 32
    EVENT_FLAG_NAME_MAX_LEN = 32
    MOB_LG_SKILL_MAX_NUM = 5
    LG_POINT_MAX_NUM = 255
    DRAGON_SOUL_BOX_SIZE = 32
    DRAGON_SOUL_BOX_COLUMN_NUM = 8
    DRAGON_SOUL_BOX_ROW_NUM = DRAGON_SOUL_BOX_SIZE / DRAGON_SOUL_BOX_COLUMN_NUM
    DRAGON_SOUL_REFINE_GRID_SIZE = 15
    MAX_AMOUNT_OF_MALL_BONUS = 20
    SHOP_TAB_NAME_MAX = 32
    SHOP_TAB_COUNT_MAX = 3
    BELT_INVENTORY_SLOT_WIDTH = 4
    BELT_INVENTORY_SLOT_HEIGHT = 4
    BELT_INVENTORY_SLOT_COUNT = BELT_INVENTORY_SLOT_WIDTH * BELT_INVENTORY_SLOT_HEIGHT
    INVENTORY_PAGE_NUM = 4
    INVENTORY_HEIGHT = 9
    INVENTORY_WIDTH = 5
    INVENTORY_MAX_NUM = INVENTORY_HEIGHT * INVENTORY_WIDTH * INVENTORY_PAGE_NUM

class MaxGold(Enum):
    GOLD_MAX = 1000000000000001L

class EWearPositions(Enum):
    WEAR_BODY = 0
    WEAR_HEAD = 1
    WEAR_FOOTS = 2
    WEAR_WRIST = 3
    WEAR_WEAPON = 4
    WEAR_NECK = 5
    WEAR_EAR = 6
    WEAR_UNIQUE1 = 7
    WEAR_UNIQUE2 = 8
    WEAR_ARROW = 9
    WEAR_SHIELD = 10
    WEAR_RING1 = 11
    WEAR_RING2 = 12
    WEAR_BELT = 13
    WEAR_PENDANT = 14
    WEAR_COSTUME_BODY = 15
    WEAR_COSTUME_HAIR = 16
    WEAR_COSTUME_ACCE = 17
    WEAR_COSTUME_WEAPON = 18
    WEAR_COSTUME_MOUNT = 19
    WEAR_COSTUME_PET = 20
    WEAR_MAX_NUM = 21

class EDragonSoulDeckType(Enum):
    DRAGON_SOUL_DECK_0 = 0
    DRAGON_SOUL_DECK_1 = 1
    DRAGON_SOUL_DECK_MAX_NUM = 2
    DRAGON_SOUL_DECK_RESERVED_MAX_NUM = 3

class ESex(Enum):
    LG_SEX_MALE = 0
    LG_SEX_FEMALE = 1

class EDirection(Enum):
    DIR_NORTH = 0
    DIR_NORTHEAST = 1
    DIR_EAST = 2
    DIR_SOUTHEAST = 3
    DIR_SOUTH = 4
    DIR_SOUTHWEST = 5
    DIR_WEST = 6
    DIR_NORTHWEST = 7
    DIR_MAX_NUM = 8


class EAbilityDifficulty(Enum):
    DIFFICULTY_EASY = 0
    DIFFICULTY_NORMAL = 1
    DIFFICULTY_HARD = 2
    DIFFICULTY_VERY_HARD = 3
    DIFFICULTY_NUM_TYPES = 4

class EAbilityCategory(Enum):
    CATEGORY_PHYSICAL = 0
    CATEGORY_MENTAL = 1
    CATEGORY_ATTRIBUTE = 2
    CATEGORY_NUM_TYPES = 3

class EJobs(Enum):
    JOB_WARRIOR = 0
    JOB_ASSASSIN = 1
    JOB_SURA = 2
    JOB_SHAMAN = 3
# Laniatus Games Studio Inc. |  TODO TASK: There is no preprocessor in Python:
##if ENABLE_WOLFMAN
    JOB_WOLFMAN = 4
##endif
    JOB_MAX_NUM = 5

class ESkillGroups(Enum):
    LG_SKILL_GROUP_MAX_NUM = 2

class ERaceFlags(Enum):
    RACE_FLAG_ANIMAL = (1 << 0)
    RACE_FLAG_UNDEAD = (1 << 1)
    RACE_FLAG_DEVIL = (1 << 2)
    RACE_FLAG_HUMAN = (1 << 3)
    RACE_FLAG_ORC = (1 << 4)
    RACE_FLAG_MILGYO = (1 << 5)
    RACE_FLAG_INSECT = (1 << 6)
    RACE_FLAG_FIRE = (1 << 7)
    RACE_FLAG_ICE = (1 << 8)
    RACE_FLAG_DESERT = (1 << 9)
    RACE_FLAG_TREE = (1 << 10)
    RACE_FLAG_ATT_ELEC = (1 << 11)
    RACE_FLAG_ATT_FIRE = (1 << 12)
    RACE_FLAG_ATT_ICE = (1 << 13)
    RACE_FLAG_ATT_WIND = (1 << 14)
    RACE_FLAG_ATT_EARTH = (1 << 15)
    RACE_FLAG_ATT_DARK = (1 << 16)
    RACE_FLAG_ZODIAC = (1 << 17)

class ELoads(Enum):
    LOAD_NONE = 0
    LOAD_LIGHT = 1
    LOAD_NORMAL = 2
    LOAD_HEAVY = 3
    LOAD_MASSIVE = 4

class EParts(Enum):
    PART_MAIN = 0
    PART_WEAPON = 1
    PART_HEAD = 2
    PART_HAIR = 3
    PART_ACCE = 4
    PART_MAX_NUM = 5
    PART_WEAPON_SUB = 6

class EChatType(Enum):
    CHAT_TYPE_TALKING = 0
    CHAT_TYPE_INFO = 1
    CHAT_TYPE_NOTICE = 2
    CHAT_TYPE_PARTY = 3
    CHAT_TYPE_GUILD = 4
    CHAT_TYPE_COMMAND = 5
    CHAT_TYPE_SHOUT = 6
    CHAT_TYPE_WHISPER = 7
    CHAT_TYPE_BIG_NOTICE = 8
    CHAT_TYPE_MAX_NUM = 9

class EWhisperType(Enum):
    WHISPER_TYPE_NORMAL = 0
    WHISPER_TYPE_NOT_EXIST = 1
    WHISPER_TYPE_TARGET_BLOCKED = 2
    WHISPER_TYPE_SENDER_BLOCKED = 3
    WHISPER_TYPE_ERROR = 4
    WHISPER_TYPE_GM = 5
    WHISPER_TYPE_SYSTEM = 0XFF

class ECharacterPosition(Enum):
    POSITION_GENERAL = 0
    POSITION_BATTLE = 1
    POSITION_DYING = 2
    POSITION_SITTING_CHAIR = 3
    POSITION_SITTING_GROUND = 4
    POSITION_INTRO = 5
    POSITION_MAX_NUM = 6

class EGMLevels(Enum):
    GM_PLAYER = 0
    GM_LOW_WIZARD = 1
    GM_WIZARD = 2
    GM_HIGH_WIZARD = 3
    GM_GOD = 4
    GM_IMPLEMENTOR = 5

class EMobRank(Enum):
    MOB_RANK_PAWN = 0
    MOB_RANK_S_PAWN = 1
    MOB_RANK_KNIGHT = 2
    MOB_RANK_S_KNIGHT = 3
    MOB_RANK_BOSS = 4
    MOB_RANK_KING = 5
    MOB_RANK_MAX_NUM = 6

class ECharType(Enum):
    CHAR_TYPE_MONSTER = 0
    CHAR_TYPE_NPC = 1
    CHAR_TYPE_STONE = 2
    CHAR_TYPE_WARP = 3
    CHAR_TYPE_DOOR = 4
    CHAR_TYPE_BUILDING = 5
    CHAR_TYPE_PC = 6
    CHAR_TYPE_POLYMORPH_PC = 7
    CHAR_TYPE_HORSE = 8
    CHAR_TYPE_GOTO = 9
    CHAR_TYPE_MOUNT = 10
    CHAR_TYPE_PET = 11

class EBattleType(Enum):
    BATTLE_TYPE_MELEE = 0
    BATTLE_TYPE_RANGE = 1
    BATTLE_TYPE_MAGIC = 2
    BATTLE_TYPE_SPECIAL = 3
    BATTLE_TYPE_POWER = 4
    BATTLE_TYPE_TANKER = 5
    BATTLE_TYPE_SUPER_POWER = 6
    BATTLE_TYPE_SUPER_TANKER = 7
    BATTLE_TYPE_MAX_NUM = 8

class EApplyTypes(Enum):
    APPLY_NONE = 0
    APPLY_MAX_HP = 1
    APPLY_MAX_SP = 2
    APPLY_CON = 3
    APPLY_INT = 4
    APPLY_STR = 5
    APPLY_DEX = 6
    APPLY_ATT_SPEED = 7
    APPLY_MOV_SPEED = 8
    APPLY_CAST_SPEED = 9
    APPLY_HP_REGEN = 10
    APPLY_SP_REGEN = 11
    APPLY_POISON_PCT = 12
    APPLY_STUN_PCT = 13
    APPLY_SLOW_PCT = 14
    APPLY_CRITICAL_PCT = 15
    APPLY_PENETRATE_PCT = 16
    APPLY_ATTBONUS_HUMAN = 17
    APPLY_ATTBONUS_ANIMAL = 18
    APPLY_ATTBONUS_ORC = 19
    APPLY_ATTBONUS_MILGYO = 20
    APPLY_ATTBONUS_UNDEAD = 21
    APPLY_ATTBONUS_DEVIL = 22
    APPLY_STEAL_HP = 23
    APPLY_STEAL_SP = 24
    APPLY_MANA_BURN_PCT = 25
    APPLY_DAMAGE_SP_RECOVER = 26
    APPLY_BLOCK = 27
    APPLY_DODGE = 28
    APPLY_RESIST_SWORD = 29
    APPLY_RESIST_TWOHAND = 30
    APPLY_RESIST_DAGGER = 31
    APPLY_RESIST_BELL = 32
    APPLY_RESIST_FAN = 33
    APPLY_RESIST_BOW = 34
    APPLY_RESIST_FIRE = 35
    APPLY_RESIST_ELEC = 36
    APPLY_RESIST_MAGIC = 37
    APPLY_RESIST_WIND = 38
    APPLY_REFLECT_MELEE = 39
    APPLY_REFLECT_CURSE = 40
    APPLY_POISON_REDUCE = 41
    APPLY_KILL_SP_RECOVER = 42
    APPLY_EXP_DOUBLE_BONUS = 43
    APPLY_GOLD_DOUBLE_BONUS = 44
    APPLY_ITEM_DROP_BONUS = 45
    APPLY_POTION_BONUS = 46
    APPLY_KILL_HP_RECOVER = 47
    APPLY_IMMUNE_STUN = 48
    APPLY_IMMUNE_SLOW = 49
    APPLY_IMMUNE_FALL = 50
    APPLY_SKILL = 51
    APPLY_BOW_DISTANCE = 52
    APPLY_ATT_GRADE_BONUS = 53
    APPLY_DEF_GRADE_BONUS = 54
    APPLY_MAGIC_ATT_GRADE = 55
    APPLY_MAGIC_DEF_GRADE = 56
    APPLY_CURSE_PCT = 57
    APPLY_MAX_STAMINA = 58
    APPLY_ATTBONUS_WARRIOR = 59
    APPLY_ATTBONUS_ASSASSIN = 60
    APPLY_ATTBONUS_SURA = 61
    APPLY_ATTBONUS_SHAMAN = 62
    APPLY_ATTBONUS_MONSTER = 63
    APPLY_MALL_ATTBONUS = 64
    APPLY_MALL_DEFBONUS = 65
    APPLY_MALL_EXPBONUS = 66
    APPLY_MALL_ITEMBONUS = 67
    APPLY_MALL_GOLDBONUS = 68
    APPLY_MAX_HP_PCT = 69
    APPLY_MAX_SP_PCT = 70
    APPLY_LG_SKILL_DAMAGE_BONUS = 71
    APPLY_NORMAL_HIT_DAMAGE_BONUS = 72
    APPLY_LG_SKILL_DEFEND_BONUS = 73
    APPLY_NORMAL_HIT_DEFEND_BONUS = 74
    APPLY_PC_BANG_EXP_BONUS = 75
    APPLY_PC_BANG_DROP_BONUS = 76
    APPLY_EXTRACT_HP_PCT = 77
    APPLY_RESIST_WARRIOR = 78
    APPLY_RESIST_ASSASSIN = 79
    APPLY_RESIST_SURA = 80
    APPLY_RESIST_SHAMAN = 81
    APPLY_ENERGY = 82
    APPLY_DEF_GRADE = 83
    APPLY_COSTUME_ATTR_BONUS = 84
    APPLY_MAGIC_ATTBONUS_PER = 85
    APPLY_MELEE_MAGIC_ATTBONUS_PER = 86
    APPLY_RESIST_ICE = 87
    APPLY_RESIST_EARTH = 88
    APPLY_RESIST_DARK = 89
    APPLY_ANTI_CRITICAL_PCT = 90
    APPLY_ANTI_PENETRATE_PCT = 91
# Laniatus Games Studio Inc. |  TODO TASK: There is no preprocessor in Python:
##if ENABLE_WOLFMAN
    APPLY_BLEEDING_REDUCE = 92
    APPLY_BLEEDING_PCT = 93
    APPLY_ATTBONUS_WOLFMAN = 94
    APPLY_RESIST_WOLFMAN = 95
    APPLY_RESIST_CLAW = 96
##endif
    APPLY_RESIST_MAGIC_REDUCTION = 97
    APPLY_RESIST_HUMAN = 98
    APPLY_ACCEDRAIN_RATE = 99
    APPLY_ENCHANT_ELECT = 100
    APPLY_ENCHANT_FIRE = 101
    APPLY_ENCHANT_ICE = 102
    APPLY_ENCHANT_WIND = 103
    APPLY_ENCHANT_EARTH = 104
    APPLY_ENCHANT_DARK = 105
    MAX_APPLY_NUM = 106

class EOnClickEvents(Enum):
    ON_CLICK_NONE = 0
    ON_CLICK_SHOP = 1
    ON_CLICK_TALK = 2
    ON_CLICK_MAX_NUM = 3

class EOnIdleEvents(Enum):
    ON_IDLE_NONE = 0
    ON_IDLE_GENERAL = 1
    ON_IDLE_MAX_NUM = 2

class EWindows(Enum):
    RESERVED_WINDOW = 0
    INVENTORY = 1
    EQUIPMENT = 2
    SAFEBOX = 3
    MALL = 4
    DRAGON_SOUL_INVENTORY = 5
    BELT_INVENTORY = 6
    ACCE_REFINE = 7
    GROUND = 8

class EMobSizes(Enum):
    MOBSIZE_RESERVED = 0
    MOBSIZE_SMALL = 1
    MOBSIZE_MEDIUM = 2
    MOBSIZE_BIG = 3

class EAIFlags(Enum):
    AIFLAG_AGGRESSIVE = (1 << 0)
    AIFLAG_NOMOVE = (1 << 1)
    AIFLAG_COWARD = (1 << 2)
    AIFLAG_NOATTACKSHINSU = (1 << 3)
    AIFLAG_NOATTACKJINNO = (1 << 4)
    AIFLAG_NOATTACKCHUNJO = (1 << 5)
    AIFLAG_ATTACKMOB = (1 << 6)
    AIFLAG_BERSERK = (1 << 7)
    AIFLAG_STONESKIN = (1 << 8)
    AIFLAG_GODSPEED = (1 << 9)
    AIFLAG_DEATHBLOW = (1 << 10)
    AIFLAG_REVIVE = (1 << 11)

class EMobStatType(Enum):
    MOB_STATTYPE_POWER = 0
    MOB_STATTYPE_TANKER = 1
    MOB_STATTYPE_SUPER_POWER = 2
    MOB_STATTYPE_SUPER_TANKER = 3
    MOB_STATTYPE_RANGE = 4
    MOB_STATTYPE_MAGIC = 5
    MOB_STATTYPE_MAX_NUM = 6

class EImmuneFlags(Enum):
    IMMUNE_STUN = (1 << 0)
    IMMUNE_SLOW = (1 << 1)
    IMMUNE_FALL = (1 << 2)
    IMMUNE_CURSE = (1 << 3)
    IMMUNE_POISON = (1 << 4)
    IMMUNE_TERROR = (1 << 5)
    IMMUNE_REFLECT = (1 << 6)

class EMobEnchants(Enum):
    MOB_ENCHANT_CURSE = 0
    MOB_ENCHANT_SLOW = 1
    MOB_ENCHANT_POISON = 2
    MOB_ENCHANT_STUN = 3
    MOB_ENCHANT_CRITICAL = 4
    MOB_ENCHANT_PENETRATE = 5
    MOB_ENCHANTS_MAX_NUM = 6

class EMobResists(Enum):
    MOB_RESIST_SWORD = 0
    MOB_RESIST_TWOHAND = 1
    MOB_RESIST_DAGGER = 2
    MOB_RESIST_BELL = 3
    MOB_RESIST_FAN = 4
    MOB_RESIST_BOW = 5
# Laniatus Games Studio Inc. |  TODO TASK: There is no preprocessor in Python:
##if ENABLE_WOLFMAN
    MOB_RESIST_CLAW = 6
##endif
    MOB_RESIST_FIRE = 7
    MOB_RESIST_ELECT = 8
    MOB_RESIST_MAGIC = 9
    MOB_RESIST_WIND = 10
    MOB_RESIST_POISON = 11
# Laniatus Games Studio Inc. |  TODO TASK: There is no preprocessor in Python:
##if ENABLE_WOLFMAN
    MOB_RESIST_BLEEDING = 12
##endif
    MOB_RESISTS_MAX_NUM = 13

class EGuildWarType(Enum):
    GUILD_WAR_TYPE_FIELD = 0
    GUILD_WAR_TYPE_BATTLE = 1
    GUILD_WAR_TYPE_FLAG = 2
    GUILD_WAR_TYPE_MAX_NUM = 3

class EGuildWarState(Enum):
    GUILD_WAR_NONE = 0
    GUILD_WAR_SEND_DECLARE = 1
    GUILD_WAR_REFUSE = 2
    GUILD_WAR_RECV_DECLARE = 3
    GUILD_WAR_WAIT_START = 4
    GUILD_WAR_CANCEL = 5
    GUILD_WAR_ON_WAR = 6
    GUILD_WAR_END = 7
    GUILD_WAR_OVER = 8
    GUILD_WAR_RESERVE = 9
    GUILD_WAR_DURATION = 30 *60
    GUILD_WAR_WIN_POINT = 1000
    GUILD_WAR_LADDER_HALF_PENALTY_TIME = 12 *60 *60

class EAttributeSet(Enum):
    ATTRIBUTE_SET_WEAPON = 0
    ATTRIBUTE_SET_BODY = 1
    ATTRIBUTE_SET_WRIST = 2
    ATTRIBUTE_SET_FOOTS = 3
    ATTRIBUTE_SET_NECK = 4
    ATTRIBUTE_SET_HEAD = 5
    ATTRIBUTE_SET_SHIELD = 6
    ATTRIBUTE_SET_EAR = 7
    ATTRIBUTE_SET_MAX_NUM = 8

class EPrivType(Enum):
    PRIV_NONE = 0
    PRIV_ITEM_DROP = 1
    PRIV_GOLD_DROP = 2
    PRIV_GOLD10_DROP = 3
    PRIV_EXP_PCT = 4
    MAX_PRIV_NUM = 5

class EPremiumTypes(Enum):
    PREMIUM_EXP = 0
    PREMIUM_ITEM = 1
    PREMIUM_SAFEBOX = 2
    PREMIUM_AUTOLOOT = 3
    PREMIUM_FISH_MIND = 4
    PREMIUM_MARRIAGE_FAST = 5
    PREMIUM_GOLD = 6
    PREMIUM_MAX_NUM = 9

class SPECIAL_EFFECT(Enum):
    SE_NONE = 0
    SE_HPUP_RED = 1
    SE_SPUP_BLUE = 2
    SE_SPEEDUP_GREEN = 3
    SE_DXUP_PURPLE = 4
    SE_CRITICAL = 5
    SE_PENETRATE = 6
    SE_BLOCK = 7
    SE_DODGE = 8
    SE_CHINA_FIREWORK = 9
    SE_SPIN_TOP = 10
    SE_SUCCESS = 11
    SE_FAIL = 12
    SE_FR_SUCCESS = 13
    SE_LEVELUP_ON_14_FOR_GERMANY = 14
    SE_LEVELUP_UNDER_15_FOR_GERMANY = 15
    SE_PERCENT_DAMAGE1 = 16
    SE_PERCENT_DAMAGE2 = 17
    SE_PERCENT_DAMAGE3 = 18
    SE_AUTO_HPUP = 19
    SE_AUTO_SPUP = 20
    SE_EQUIP_RAMADAN_RING = 21
    SE_EQUIP_HALLOWEEN_CANDY = 22
    SE_EQUIP_HAPPINESS_RING = 23
    SE_EQUIP_LOVE_PENDANT = 24
    SE_ACCE_SUCESS_ABSORB = 25
    SE_ACCE_EQUIP = 26
    SE_ACCE_BACK = 27


class EDragonSoulRefineWindowSize(Enum):
    DRAGON_SOUL_REFINE_GRID_MAX = 15

class LGEMiscellaneous2(Enum):
    DRAGON_SOUL_EQUIP_SLOT_START = LGEMiscellaneous.INVENTORY_MAX_NUM + EWEARPOSITIONS.WEAR_MAX_NUM
    DRAGON_SOUL_EQUIP_SLOT_END = DRAGON_SOUL_EQUIP_SLOT_START + (EDRAGONSOULSUBTYPE.DS_SLOT_MAX * EDRAGONSOULDECKTYPE.DRAGON_SOUL_DECK_MAX_NUM)
    DRAGON_SOUL_EQUIP_RESERVED_SLOT_END = DRAGON_SOUL_EQUIP_SLOT_END + (EDRAGONSOULSUBTYPE.DS_SLOT_MAX * EDRAGONSOULDECKTYPE.DRAGON_SOUL_DECK_RESERVED_MAX_NUM)
    BELT_INVENTORY_SLOT_START = DRAGON_SOUL_EQUIP_RESERVED_SLOT_END
    BELT_INVENTORY_SLOT_END = BELT_INVENTORY_SLOT_START + LGEMiscellaneous.BELT_INVENTORY_SLOT_COUNT
    INVENTORY_AND_EQUIP_SLOT_MAX = BELT_INVENTORY_SLOT_END

# Laniatus Games Studio Inc. |  TODO TASK: There is no preprocessor in Python:
##pragma pack(push, 1)

class SItemPos:

    def _initialize_instance_fields(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.window_type = 0
        self.cell = 0

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to multiple constructors:
#ORIGINAL LINE: SItemPos()
    def __init__(self):
        self._initialize_instance_fields()

        self.window_type = EWindows.INVENTORY
        self.cell = DefineConstants.WORD_MAX

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to multiple constructors:
#ORIGINAL LINE: SItemPos(byte _window_type, ushort _cell)
    def __init__(self, _window_type, _cell):
        self._initialize_instance_fields()

        self.window_type = _window_type
        self.cell = _cell

#Laniatus Games Studio Inc. | Python Metin II Server Warnings 'const' methods are not available in Python:
#ORIGINAL LINE: bool IsValidItemPosition() const
    def IsValidItemPosition(self):
        if self.window_type == EWindows.RESERVED_WINDOW:
            return False
        if (self.window_type == EWindows.RESERVED_WINDOW) or (self.window_type == EWindows.INVENTORY) or (self.window_type == EWindows.EQUIPMENT) or (self.window_type == EWindows.BELT_INVENTORY):
            return self.cell < LGEMiscellaneous2.INVENTORY_AND_EQUIP_SLOT_MAX
        if (self.window_type == EWindows.RESERVED_WINDOW) or (self.window_type == EWindows.INVENTORY) or (self.window_type == EWindows.EQUIPMENT) or (self.window_type == EWindows.BELT_INVENTORY) or (self.window_type == EWindows.DRAGON_SOUL_INVENTORY):
            return self.cell < (EDSInventoryMaxNum.DRAGON_SOUL_INVENTORY_MAX_NUM)
        if (self.window_type == EWindows.RESERVED_WINDOW) or (self.window_type == EWindows.INVENTORY) or (self.window_type == EWindows.EQUIPMENT) or (self.window_type == EWindows.BELT_INVENTORY) or (self.window_type == EWindows.DRAGON_SOUL_INVENTORY) or (self.window_type == EWindows.SAFEBOX) or (self.window_type == EWindows.MALL):
            return False

        if True:
            return False
        return False

#Laniatus Games Studio Inc. | Python Metin II Server Warnings 'const' methods are not available in Python:
#ORIGINAL LINE: bool IsEquipPosition() const
    def IsEquipPosition(self):
        return ((EWindows.INVENTORY == self.window_type or EWindows.EQUIPMENT == self.window_type) and self.cell >= LGEMiscellaneous.INVENTORY_MAX_NUM and self.cell < LGEMiscellaneous.INVENTORY_MAX_NUM + EWearPositions.WEAR_MAX_NUM) or self.IsDragonSoulEquipPosition()

#Laniatus Games Studio Inc. | Python Metin II Server Warnings 'const' methods are not available in Python:
#ORIGINAL LINE: bool IsDragonSoulEquipPosition() const
    def IsDragonSoulEquipPosition(self):
        return (LGEMiscellaneous2.DRAGON_SOUL_EQUIP_SLOT_START <= self.cell) and (LGEMiscellaneous2.DRAGON_SOUL_EQUIP_SLOT_END > self.cell)

#Laniatus Games Studio Inc. | Python Metin II Server Warnings 'const' methods are not available in Python:
#ORIGINAL LINE: bool IsBeltInventoryPosition() const
    def IsBeltInventoryPosition(self):
        return (LGEMiscellaneous2.BELT_INVENTORY_SLOT_START <= self.cell) and (LGEMiscellaneous2.BELT_INVENTORY_SLOT_END > self.cell)

#Laniatus Games Studio Inc. | Python Metin II Server Warnings 'const' methods are not available in Python:
#ORIGINAL LINE: bool IsDefaultInventoryPosition() const
    def IsDefaultInventoryPosition(self):
        return EWindows.INVENTORY == self.window_type and self.cell < LGEMiscellaneous.INVENTORY_MAX_NUM

#Laniatus Games Studio Inc. | Python Metin II Server Warnings 'const' methods are not available in Python:
#ORIGINAL LINE: bool operator ==(const struct SItemPos& rhs) const
    def equals_to(self, rhs):
        return (self.window_type == rhs.window_type) and (self.cell == rhs.cell)
#Laniatus Games Studio Inc. | Python Metin II Server Warnings 'const' methods are not available in Python:
#ORIGINAL LINE: bool operator <(const struct SItemPos& rhs) const
    def less_than(self, rhs):
        return (self.window_type < rhs.window_type) or ((self.window_type == rhs.window_type) and (self.cell < rhs.cell))

# Laniatus Games Studio Inc. |  TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
const SItemPos NPOS(RESERVED_WINDOW, DefineConstants.WORD_MAX)

class EShopCoinType(Enum):
    SHOP_COIN_TYPE_GOLD = 0
    SHOP_COIN_TYPE_SECONDARY_COIN = 1

# Laniatus Games Studio Inc. |  TODO TASK: There is no preprocessor in Python:
##if __MULTI_LANGUAGE_SYSTEM__
class EMultiLocale(Enum):
    MAX_QUEST_NOTICE_ARGS = 5

class LaniatusLocalization(Enum):
    LOCALE_LANIATUS = 0 # Korea
    LOCALE_EN = 1 # United Kingdom
    LOCALE_DE = 2 # Germany
    #	LOCALE_PT, // Portugal
    #	LOCALE_ES, // Spain
    #	LOCALE_FR, // France
    #	LOCALE_RO, // Romania
    #	LOCALE_PL, // Poland
    #	LOCALE_IT, // Italy
    #	LOCALE_CZ, // Czech
    #	LOCALE_HU, // Hungary
    #	LOCALE_TR, // Turkey 
    LOCALE_MAX_NUM = 3
    LOCALE_DEFAULT = LOCALE_EN
##endif

# Laniatus Games Studio Inc. |  TODO TASK: There is no preprocessor in Python:
##pragma pack(pop)
