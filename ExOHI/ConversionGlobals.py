class Globals:
    LG_ITEM_SOCKET_REMAIN_SEC = 0

    ABSORB = 0
    COMBINE = 1

    ACCE_SLOT_LEFT = 0
    ACCE_SLOT_RIGHT = 1
    ACCE_SLOT_RESULT = 2
    ACCE_SLOT_MAX_NUM = 3


    LG_QUICKSLOT_TYPE_NONE = 0
    LG_QUICKSLOT_TYPE_ITEM = 1
    LG_QUICKSLOT_TYPE_SKILL = 2
    LG_QUICKSLOT_TYPE_COMMAND = 3
    LG_QUICKSLOT_TYPE_MAX_NUM = 4

    LG_LG_SKILL_ATTR_TYPE_NORMAL = 1
    LG_LG_SKILL_ATTR_TYPE_MELEE = 2
    LG_LG_SKILL_ATTR_TYPE_RANGE = 3
    LG_LG_SKILL_ATTR_TYPE_MAGIC = 4

    LG_SKILL_NORMAL = 0
    LG_SKILL_MASTER = 1
    LG_SKILL_GRAND_MASTER = 2
    LG_SKILL_PERFECT_MASTER = 3
# Laniatus Games Studio Inc. |  TODO TASK: There is no equivalent in Python to templates on variables:
    singleton = None

    # Laniatus Games Studio Inc. |  TODO TASK: There is no preprocessor in Python:
    ##if ! itertype
    # Laniatus Games Studio Inc. |  TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
    ##define itertype(v) __typeof((v).begin())
    ##endif

    @staticmethod
    def stl_lowers(rstRet):
        LaniatusDefVariables = 0
        while LaniatusDefVariables < len(rstRet):
            rstRet[LaniatusDefVariables] = tolower(rstRet[LaniatusDefVariables])
            LaniatusDefVariables += 1


    LG_HEADER_GD_LOGIN = 1
    LG_HEADER_GD_LOGOUT = 2
    LG_HEADER_GD_PLAYER_LOAD = 3
    LG_HEADER_GD_PLAYER_SAVE = 4
    LG_HEADER_GD_PLAYER_CREATE = 5
    LG_HEADER_GD_PLAYER_DELETE = 6
    LG_HEADER_GD_LOGIN_KEY = 7
    LG_HEADER_GD_BOOT = 9
    LG_HEADER_GD_PLAYER_COUNT = 10
    LG_HEADER_GD_QUEST_SAVE = 11
    LG_HEADER_GD_SAFEBOX_LOAD = 12
    LG_HEADER_GD_SAFEBOX_SAVE = 13
    LG_HEADER_GD_SAFEBOX_CHANGE_SIZE = 14
    LG_HEADER_GD_EMPIRE_SELECT = 15
    LG_HEADER_GD_SAFEBOX_CHANGE_PASSWORD = 16
    LG_HEADER_GD_SAFEBOX_CHANGE_PASSWORD_SECOND = 17
    LG_HEADER_GD_DIRECT_ENTER = 18
    LG_HEADER_GD_GUILD_LG_SKILL_UPDATE = 19
    LG_HEADER_GD_GUILD_EXP_UPDATE = 20
    LG_HEADER_GD_GUILD_ADD_MEMBER = 21
    LG_HEADER_GD_GUILD_REMOVE_MEMBER = 22
    LG_HEADER_GD_GUILD_CHANGE_GRADE = 23
    LG_HEADER_GD_GUILD_CHANGE_MEMBER_DATA = 24
    LG_HEADER_GD_GUILD_DISBAND = 25
    LG_HEADER_GD_GUILD_WAR = 26
    LG_HEADER_GD_GUILD_WAR_SCORE = 27
    LG_HEADER_GD_GUILD_CREATE = 28
    LG_HEADER_GD_ITEM_SAVE = 30
    LG_HEADER_GD_ITEM_DESTROY = 31
    LG_HEADER_GD_ADD_AFFECT = 32
    LG_HEADER_GD_REMOVE_AFFECT = 33
    LG_HEADER_GD_HIGHSCORE_REGISTER = 34
    LG_HEADER_GD_ITEM_FLUSH = 35
    LG_HEADER_GD_PARTY_CREATE = 36
    LG_HEADER_GD_PARTY_DELETE = 37
    LG_HEADER_GD_PARTY_ADD = 38
    LG_HEADER_GD_PARTY_REMOVE = 39
    LG_HEADER_GD_PARTY_STATE_CHANGE = 40
    LG_HEADER_GD_PARTY_HEAL_USE = 41
    LG_HEADER_GD_FLUSH_CACHE = 42
    LG_HEADER_GD_RELOAD_PROTO = 43
    LG_HEADER_GD_CHANGE_NAME = 44
    LG_HEADER_GD_GUILD_CHANGE_LADDER_POINT = 46
    LG_HEADER_GD_GUILD_USE_SKILL = 47
    LG_HEADER_GD_REQUEST_EMPIRE_PRIV = 48
    LG_HEADER_GD_REQUEST_GUILD_PRIV = 49
    LG_HEADER_GD_GUILD_DEPOSIT_MONEY = 51
    LG_HEADER_GD_GUILD_WITHDRAW_MONEY = 52
    LG_HEADER_GD_GUILD_WITHDRAW_MONEY_GIVE_REPLY = 53
    LG_HEADER_GD_REQUEST_CHARACTER_PRIV = 54
    LG_HEADER_GD_SET_EVENT_FLAG = 55
    LG_HEADER_GD_PARTY_SET_MEMBER_LEVEL = 56
    LG_HEADER_GD_GUILD_WAR_BET = 57
    LG_HEADER_GD_CREATE_OBJECT = 60
    LG_HEADER_GD_DELETE_OBJECT = 61
    LG_HEADER_GD_UPDATE_LAND = 62
    LG_HEADER_GD_MARRIAGE_ADD = 70
    LG_HEADER_GD_MARRIAGE_UPDATE = 71
    LG_HEADER_GD_MARRIAGE_REMOVE = 72
    LG_HEADER_GD_WEDDING_REQUEST = 73
    LG_HEADER_GD_WEDDING_READY = 74
    LG_HEADER_GD_WEDDING_END = 75
    LG_HEADER_GD_AUTH_LOGIN = 100
    LG_HEADER_GD_LOGIN_BY_KEY = 101
    LG_HEADER_GD_MALL_LOAD = 107
    LG_HEADER_GD_MYSHOP_PRICELIST_UPDATE = 108
    LG_HEADER_GD_MYSHOP_PRICELIST_REQ = 109
    LG_HEADER_GD_BLOCK_CHAT = 110
    LG_HEADER_GD_RELOAD_ADMIN = 115
    LG_HEADER_GD_BREAK_MARRIAGE = 116
    LG_HEADER_GD_REQ_CHANGE_GUILD_MASTER = 129
    LG_HEADER_GD_REQ_SPARE_ITEM_ID_RANGE = 130
    LG_HEADER_GD_UPDATE_HORSE_NAME = 131
    LG_HEADER_GD_REQ_HORSE_NAME = 132
    LG_HEADER_GD_DC = 133
    LG_HEADER_GD_VALID_LOGOUT = 134
    LG_HEADER_GD_REQUEST_CHARGE_CASH = 137
    LG_HEADER_GD_DELETE_AWARDID = 138
    LG_HEADER_GD_UPDATE_CHANNELSTATUS = 139
    LG_HEADER_GD_REQUEST_CHANNELSTATUS = 140
    int #if __MULTI_LANGUAGE_SYSTEM__ = 141
    LG_HEADER_GD_REQUEST_CHANGE_LANGUAGE = 146
    int #endif = 147
    int #if (not _IMPROVED_PACKET_ENCRYPTION_) = 148
    LG_HEADER_GD_SHUTDOWN = 149
    int #endif = 150
    LG_HEADER_GD_SETUP = 0xff
    LG_HEADER_DG_NOTICE = 1
    LG_HEADER_DG_LOGIN_SUCCESS = 30
    LG_HEADER_DG_LOGIN_NOT_EXIST = 31
    LG_HEADER_DG_LOGIN_WRONG_PASSWD = 33
    LG_HEADER_DG_LOGIN_ALREADY = 34
    LG_HEADER_DG_PLAYER_LOAD_SUCCESS = 35
    LG_HEADER_DG_PLAYER_LOAD_FAILED = 36
    LG_HEADER_DG_PLAYER_CREATE_SUCCESS = 37
    LG_HEADER_DG_PLAYER_CREATE_ALREADY = 38
    LG_HEADER_DG_PLAYER_CREATE_FAILED = 39
    LG_HEADER_DG_PLAYER_DELETE_SUCCESS = 40
    LG_HEADER_DG_PLAYER_DELETE_FAILED = 41
    LG_HEADER_DG_ITEM_LOAD = 42
    LG_HEADER_DG_BOOT = 43
    LG_HEADER_DG_QUEST_LOAD = 44
    LG_HEADER_DG_SAFEBOX_LOAD = 45
    LG_HEADER_DG_SAFEBOX_CHANGE_SIZE = 46
    LG_HEADER_DG_SAFEBOX_WRONG_PASSWORD = 47
    LG_HEADER_DG_SAFEBOX_CHANGE_PASSWORD_ANSWER = 48
    LG_HEADER_DG_EMPIRE_SELECT = 49
    LG_HEADER_DG_AFFECT_LOAD = 50
    LG_HEADER_DG_MALL_LOAD = 51
    LG_HEADER_DG_DIRECT_ENTER = 55
    LG_HEADER_DG_GUILD_LG_SKILL_UPDATE = 56
    LG_HEADER_DG_GUILD_LG_SKILL_RECHARGE = 57
    LG_HEADER_DG_GUILD_EXP_UPDATE = 58
    LG_HEADER_DG_PARTY_CREATE = 59
    LG_HEADER_DG_PARTY_DELETE = 60
    LG_HEADER_DG_PARTY_ADD = 61
    LG_HEADER_DG_PARTY_REMOVE = 62
    LG_HEADER_DG_PARTY_STATE_CHANGE = 63
    LG_HEADER_DG_PARTY_HEAL_USE = 64
    LG_HEADER_DG_PARTY_SET_MEMBER_LEVEL = 65
    LG_HEADER_DG_TIME = 90
    LG_HEADER_DG_ITEM_ID_RANGE = 91
    LG_HEADER_DG_GUILD_ADD_MEMBER = 92
    LG_HEADER_DG_GUILD_REMOVE_MEMBER = 93
    LG_HEADER_DG_GUILD_CHANGE_GRADE = 94
    LG_HEADER_DG_GUILD_CHANGE_MEMBER_DATA = 95
    LG_HEADER_DG_GUILD_DISBAND = 96
    LG_HEADER_DG_GUILD_WAR = 97
    LG_HEADER_DG_GUILD_WAR_SCORE = 98
    LG_HEADER_DG_GUILD_TIME_UPDATE = 99
    LG_HEADER_DG_GUILD_LOAD = 100
    LG_HEADER_DG_GUILD_LADDER = 101
    LG_HEADER_DG_GUILD_LG_SKILL_USABLE_CHANGE = 102
    LG_HEADER_DG_GUILD_MONEY_CHANGE = 103
    LG_HEADER_DG_GUILD_WITHDRAW_MONEY_GIVE = 104
    LG_HEADER_DG_SET_EVENT_FLAG = 105
    LG_HEADER_DG_GUILD_WAR_RESERVE_ADD = 106
    LG_HEADER_DG_GUILD_WAR_RESERVE_DEL = 107
    LG_HEADER_DG_GUILD_WAR_BET = 108
    LG_HEADER_DG_RELOAD_PROTO = 120
    LG_HEADER_DG_CHANGE_NAME = 121
    LG_HEADER_DG_AUTH_LOGIN = 122
    LG_HEADER_DG_CHANGE_EMPIRE_PRIV = 124
    LG_HEADER_DG_CHANGE_GUILD_PRIV = 125
    LG_HEADER_DG_CHANGE_CHARACTER_PRIV = 127
    LG_HEADER_DG_CREATE_OBJECT = 140
    LG_HEADER_DG_DELETE_OBJECT = 141
    LG_HEADER_DG_UPDATE_LAND = 142
    LG_HEADER_DG_MARRIAGE_ADD = 150
    LG_HEADER_DG_MARRIAGE_UPDATE = 151
    LG_HEADER_DG_MARRIAGE_REMOVE = 152
    LG_HEADER_DG_WEDDING_REQUEST = 153
    LG_HEADER_DG_WEDDING_READY = 154
    LG_HEADER_DG_WEDDING_START = 155
    LG_HEADER_DG_WEDDING_END = 156
    LG_HEADER_DG_MYSHOP_PRICELIST_RES = 157
    LG_HEADER_DG_RELOAD_ADMIN = 158
    LG_HEADER_DG_BREAK_MARRIAGE = 159
    LG_HEADER_DG_ACK_CHANGE_GUILD_MASTER = 173
    LG_HEADER_DG_ACK_SPARE_ITEM_ID_RANGE = 174
    LG_HEADER_DG_UPDATE_HORSE_NAME = 175
    LG_HEADER_DG_ACK_HORSE_NAME = 176
    LG_HEADER_DG_NEED_LOGIN_LOG = 177
    LG_HEADER_DG_RESULT_CHARGE_CASH = 179
    LG_HEADER_DG_ITEMAWARD_INFORMER = 180
    LG_HEADER_DG_RESPOND_CHANNELSTATUS = 181
    int #if (not _IMPROVED_PACKET_ENCRYPTION_) = 182
    LG_HEADER_DG_SHUTDOWN = 184
    int #endif = 185
    LG_HEADER_DG_MAP_LOCATIONS = 0xfe
    LG_HEADER_DG_P2P = 0xff
    @staticmethod
    def str_to_number(out, in_):
        if None==in_ or None==in_[0]:
            return False

        out.arg_value = (strtol(in_, None, 10) != 0)
        return True

    @staticmethod
    def str_to_number(out, in_):
        if None==in_ or None==in_[0]:
            return False

        out.arg_value = (char) strtol(in_, None, 10)
        return True

    @staticmethod
    def str_to_number(out, in_):
        if None==in_ or None==in_[0]:
            return False

        out.arg_value = byte(int(strtoul(in_, None, 10)))
        return True

    @staticmethod
    def str_to_number(out, in_):
        if None==in_ or None==in_[0]:
            return False

        out.arg_value = short(int(strtol(in_, None, 10)))
        return True

    @staticmethod
    def str_to_number(out, in_):
        if None==in_ or None==in_[0]:
            return False

        out.arg_value = strtoul(in_, None, 10)
        return True

    @staticmethod
    def str_to_number(out, in_):
        if None==in_ or None==in_[0]:
            return False

        out.arg_value = int(strtol(in_, None, 10))
        return True

    @staticmethod
    def str_to_number(out, in_):
        if None==in_ or None==in_[0]:
            return False

        out.arg_value = strtoul(in_, None, 10)
        return True

    @staticmethod
    def str_to_number(out, in_):
        if None==in_ or None==in_[0]:
            return False

        out.arg_value = int(strtol(in_, None, 10))
        return True

    @staticmethod
    def str_to_number(out, in_):
        if None==in_ or None==in_[0]:
            return False

        out.arg_value = strtoul(in_, None, 10)
        return True

    @staticmethod
    def str_to_number(out, in_):
        if None==in_ or None==in_[0]:
            return False

        out.arg_value = int(strtoull(in_, None, 10))
        return True

    @staticmethod
    def str_to_number(out, in_):
        if None==in_ or None==in_[0]:
            return False

        out.arg_value = float(strtof(in_, None))
        return True

    @staticmethod
    def str_to_number(out, in_):
        if None==in_ or None==in_[0]:
            return False

        out.arg_value = float(strtod(in_, None))
        return True

    # Laniatus Games Studio Inc. |  TODO TASK: There is no preprocessor in Python:
    ##if __FreeBSD__
    @staticmethod
    def str_to_number(out, in_):
        if None==in_ or None==in_[0]:
            return False

        out.arg_value = float(strtold(in_, None))
        return True
    ##endif
