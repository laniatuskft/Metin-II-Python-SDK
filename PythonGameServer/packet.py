from enum import Enum

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##pragma pack(1)
class SPacketGGSetup:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.bHeader = 0
        self.wPort = 0
        self.bChannel = 0


class SPacketGGLogin:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.bHeader = 0
        self.szName = str(['\0' for _ in range(CHARACTER_NAME_MAX_LEN + 1)])
        self.dwPID = 0
        self.bEmpire = 0
        self.lMapIndex = 0
        self.bChannel = 0
        self.bLanguage = 0

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if __MULTI_LANGUAGE_SYSTEM__
##endif

class SPacketGGLogout:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.bHeader = 0
        self.szName = str(['\0' for _ in range(CHARACTER_NAME_MAX_LEN + 1)])


class SPacketGGRelay:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.bHeader = 0
        self.szName = str(['\0' for _ in range(CHARACTER_NAME_MAX_LEN + 1)])
        self.lSize = 0


class SPacketGGNotice:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.bHeader = 0
        self.lSize = 0


class SPacketGGShutdown:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.bHeader = 0


class SPacketGGGuild:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.bHeader = 0
        self.bSubHeader = 0
        self.dwGuild = 0


class SPacketGGGuildChat:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.bHeader = 0
        self.bSubHeader = 0
        self.dwGuild = 0
        self.szText = str(['\0' for _ in range(CHAT_MAX_LEN + 1)])


class SPacketGGParty:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.subheader = 0
        self.pid = 0
        self.leaderpid = 0


class SPacketGGDisconnect:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.bHeader = 0
        self.szLogin = str(['\0' for _ in range(LOGIN_MAX_LEN + 1)])


class SPacketGGShout:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.bHeader = 0
        self.bEmpire = 0
        self.szText = str(['\0' for _ in range(CHAT_MAX_LEN + 1)])


class SPacketGGXmasWarpSanta:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.bHeader = 0
        self.bChannel = 0
        self.lMapIndex = 0


class SPacketGGXmasWarpSantaReply:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.bHeader = 0
        self.bChannel = 0


class SPacketGGMessenger:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.bHeader = 0
        self.szAccount = str(['\0' for _ in range(CHARACTER_NAME_MAX_LEN + 1)])
        self.szCompanion = str(['\0' for _ in range(CHARACTER_NAME_MAX_LEN + 1)])


class SPacketGGFindPosition:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.dwFromPID = 0
        self.dwTargetPID = 0


class SPacketGGWarpCharacter:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.pid = 0
        self.x = 0
        self.y = 0


class SPacketGGGuildWarMapIndex:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.bHeader = 0
        self.dwGuildID1 = 0
        self.dwGuildID2 = 0
        self.lMapIndex = 0


class SPacketGGTransfer:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.bHeader = 0
        self.szName = str(['\0' for _ in range(CHARACTER_NAME_MAX_LEN + 1)])
        self.lX = 0
        self.lY = 0


class SPacketGGLoginPing:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.bHeader = 0
        self.szLogin = str(['\0' for _ in range(LOGIN_MAX_LEN + 1)])


class SPacketGGBlockChat:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.bHeader = 0
        self.szName = str(['\0' for _ in range(CHARACTER_NAME_MAX_LEN + 1)])
        self.lBlockDuration = 0


class command_text:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.bHeader = 0


class command_handshake:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.bHeader = 0
        self.dwHandshake = 0
        self.dwTime = 0
        self.lDelta = 0


class command_login:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.login = str(['\0' for _ in range(LOGIN_MAX_LEN + 1)])
        self.passwd = str(['\0' for _ in range(PASSWD_MAX_LEN + 1)])


class command_login2:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.login = str(['\0' for _ in range(LOGIN_MAX_LEN + 1)])
        self.dwLoginKey = 0
        self.adwClientKey = [0 for _ in range(4)]


class command_login3:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.login = str(['\0' for _ in range(LOGIN_MAX_LEN + 1)])
        self.passwd = str(['\0' for _ in range(PASSWD_MAX_LEN + 1)])
        self.adwClientKey = [0 for _ in range(4)]
        self.clientVersion = str(['\0' for _ in range(8)])
        self.bLanguage = 0

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if __MULTI_LANGUAGE_SYSTEM__
##endif

class packet_login_key:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.bHeader = 0
        self.dwLoginKey = 0


class command_player_select:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.index = 0


class command_player_delete:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.index = 0
        self.private_code = str(['\0' for _ in range(8)])


class command_player_create:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.index = 0
        self.name = str(['\0' for _ in range(CHARACTER_NAME_MAX_LEN + 1)])
        self.job = 0
        self.shape = 0
        self.Con = 0
        self.int = 0
        self.Str = 0
        self.Dex = 0


class command_player_create_success:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.bAccountCharacterIndex = 0
        self.player = TSimplePlayer()


class command_attack:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.bHeader = 0
        self.bType = 0
        self.dwVID = 0
        self.bCRCMagicCubeProcPiece = 0
        self.bCRCMagicCubeFilePiece = 0


class EMoveFuncType(Enum):
    FUNC_WAIT = 0
    FUNC_MOVE = 1
    FUNC_ATTACK = 2
    FUNC_COMBO = 3
    FUNC_MOB_SKILL = 4
    _FUNC_SKILL = 5
    FUNC_MAX_NUM = 6
    FUNC_SKILL = 0X80

class command_move:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.bHeader = 0
        self.bFunc = 0
        self.bArg = 0
        self.bRot = 0
        self.lX = 0
        self.lY = 0
        self.dwTime = 0


class command_sync_position_element:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.dwVID = 0
        self.lX = 0
        self.lY = 0


class command_sync_position:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.bHeader = 0
        self.wSize = 0


class command_chat:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.size = 0
        self.type = 0


class command_whisper:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.bHeader = 0
        self.wSize = 0
        self.szNameTo = str(['\0' for _ in range(CHARACTER_NAME_MAX_LEN + 1)])


class command_entergame:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0


class command_item_use:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.Cell = TItemPos()


class command_item_use_to_item:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.Cell = TItemPos()
        self.TargetCell = TItemPos()


class command_item_drop:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.Cell = TItemPos()
        self.gold = 0


class command_item_drop2:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.Cell = TItemPos()
        self.gold = 0
        self.count = 0


class command_item_destroy:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.Cell = TItemPos()


class command_item_move:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.Cell = TItemPos()
        self.CellTo = TItemPos()
        self.count = 0


class command_item_pickup:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.vid = 0


class command_LG_QUICKSLOT_add:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.pos = 0
        self.slot = TQuickslot()


class command_LG_QUICKSLOT_del:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.pos = 0


class command_LG_QUICKSLOT_swap:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.pos = 0
        self.change_pos = 0


class command_shop_buy:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.count = 0


class command_shop_sell:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.pos = 0
        self.count = 0


class command_shop:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.subheader = 0


class command_on_click:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.vid = 0


class command_exchange:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.sub_header = 0
        self.arg1 = 0
        self.arg2 = 0
        self.Pos = TItemPos()


class command_position:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.position = 0


class command_script_answer:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.answer = 0



class command_script_button:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.idx = 0


class command_quest_input_string:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.msg = str(['\0' for _ in range(64+1)])


class command_quest_confirm:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.answer = 0
        self.requestPID = 0


class packet_quest_confirm:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.msg = str(['\0' for _ in range(64+1)])
        self.timeout = 0
        self.requestPID = 0


class packet_handshake:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.bHeader = 0
        self.dwHandshake = 0
        self.dwTime = 0
        self.lDelta = 0


class EPhase(Enum):
    PHASE_CLOSE = 0
    PHASE_HANDSHAKE = 1
    PHASE_LOGIN = 2
    PHASE_SELECT = 3
    PHASE_LOADING = 4
    PHASE_GAME = 5
    PHASE_DEAD = 6
    PHASE_CLIENT_CONNECTING = 7
    PHASE_DBCLIENT = 8
    PHASE_P2P = 9
    PHASE_AUTH = 10

class packet_phase:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.phase = 0


class packet_bindudp:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.addr = 0
        self.port = 0


class packet_login_success:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.bHeader = 0
        self.players = [TSimplePlayer() for _ in range(PLAYER_PER_ACCOUNT)]
        self.guild_id = [0 for _ in range(PLAYER_PER_ACCOUNT)]
        self.guild_name = [[] for _ in range(PLAYER_PER_ACCOUNT)]
        self.handle = 0
        self.random_key = 0



class packet_auth_success:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.bHeader = 0
        self.dwLoginKey = 0
        self.bResult = 0


class packet_login_failure:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.szStatus = str(['\0' for _ in range(ACCOUNT_STATUS_MAX_LEN + 1)])


class packet_create_failure:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.bType = 0


class ECharacterEquipmentPart(Enum):
    CHR_EQUIPPART_ARMOR = 0
    CHR_EQUIPPART_WEAPON = 1
    CHR_EQUIPPART_HEAD = 2
    CHR_EQUIPPART_HAIR = 3
    CHR_EQUIPPART_ACCE = 4
    CHR_EQUIPPART_NUM = 5

class packet_add_char:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.dwVID = 0
        self.angle = 0
        self.x = 0
        self.y = 0
        self.z = 0
        self.bType = 0
        self.wRaceNum = 0
        self.bMovingSpeed = 0
        self.bAttackSpeed = 0
        self.bStateFlag = 0
        self.dwAffectFlag = [0 for _ in range(2)]





class packet_char_additional_info:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.dwVID = 0
        self.name = str(['\0' for _ in range(CHARACTER_NAME_MAX_LEN + 1)])
        self.dwPart = [0 for _ in range((int)ECharacterEquipmentPart.CHR_EQUIPPART_NUM)]
        self.bEmpire = 0
        self.dwGuildID = 0
        self.dwLevel = 0
        self.sAlignment = 0
        self.bPKMode = 0
        self.dwMountVnum = 0
        self.dwArrow = 0
        self.byAcceDrainRate = 0
        self.bLanguage = 0

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if __MULTI_LANGUAGE_SYSTEM__
##endif

class packet_update_char:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.dwVID = 0
        self.dwPart = [0 for _ in range((int)ECharacterEquipmentPart.CHR_EQUIPPART_NUM)]
        self.bMovingSpeed = 0
        self.bAttackSpeed = 0
        self.bStateFlag = 0
        self.dwAffectFlag = [0 for _ in range(2)]
        self.dwGuildID = 0
        self.sAlignment = 0
        self.bPKMode = 0
        self.dwMountVnum = 0
        self.dwArrow = 0
        self.byAcceDrainRate = 0
        self.bLanguage = 0




## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if __MULTI_LANGUAGE_SYSTEM__
##endif

class packet_del_char:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.id = 0


class packet_chat:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.size = 0
        self.type = 0
        self.id = 0
        self.bEmpire = 0


class packet_whisper:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.bHeader = 0
        self.wSize = 0
        self.bType = 0
        self.szNameFrom = str(['\0' for _ in range(CHARACTER_NAME_MAX_LEN + 1)])


class packet_main_character:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.dwVID = 0
        self.wRaceNum = 0
        self.szName = str(['\0' for _ in range(CHARACTER_NAME_MAX_LEN + 1)])
        self.lx = 0
        self.ly = 0
        self.lz = 0
        self.empire = 0
        self.LG_SKILL_group = 0


class packet_main_character3_bgm:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.dwVID = 0
        self.wRaceNum = 0
        self.szChrName = str(['\0' for _ in range(CHARACTER_NAME_MAX_LEN + 1)])
        self.szBGMName = str(['\0' for _ in range(MUSIC_NAME_LEN + 1)])
        self.lx = 0
        self.ly = 0
        self.lz = 0
        self.empire = 0
        self.LG_SKILL_group = 0

    MUSIC_NAME_LEN = 24


class packet_main_character4_bgm_vol:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.dwVID = 0
        self.wRaceNum = 0
        self.szChrName = str(['\0' for _ in range(CHARACTER_NAME_MAX_LEN + 1)])
        self.szBGMName = str(['\0' for _ in range(MUSIC_NAME_LEN + 1)])
        self.fBGMVol = 0
        self.lx = 0
        self.ly = 0
        self.lz = 0
        self.empire = 0
        self.LG_SKILL_group = 0

    MUSIC_NAME_LEN = 24


class packet_points:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.points = [0 for _ in range(LG_POINT_MAX_NUM)]


class packet_LG_SKILL_level:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.bHeader = 0
        self.skills = [TPlayerSkill() for _ in range(LG_SKILL_MAX_NUM)]


class packet_LG_POINT_change:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.dwVID = 0
        self.type = 0
        self.amount = 0
        self.value = 0


class packet_stun:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.vid = 0


class packet_dead:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.vid = 0


class TPacketGCItemDelDeprecated:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.Cell = TItemPos()
        self.vnum = 0
        self.count = 0
        self.alSockets = [0 for _ in range(LG_ITEM_SOCKET_MAX_NUM)]
        self.aAttr = [TPlayerItemAttribute() for _ in range(ITEM_ATTRIBUTE_MAX_NUM)]


class packet_item_set:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.Cell = TItemPos()
        self.vnum = 0
        self.count = 0
        self.flags = 0
        self.anti_flags = 0
        self.highlight = False
        self.alSockets = [0 for _ in range(LG_ITEM_SOCKET_MAX_NUM)]
        self.aAttr = [TPlayerItemAttribute() for _ in range(ITEM_ATTRIBUTE_MAX_NUM)]


class packet_item_del:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.pos = 0


class packet_item_use:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.Cell = TItemPos()
        self.ch_vid = 0
        self.victim_vid = 0
        self.vnum = 0


class packet_item_move:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.Cell = TItemPos()
        self.CellTo = TItemPos()


class packet_item_update:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.Cell = TItemPos()
        self.count = 0
        self.alSockets = [0 for _ in range(LG_ITEM_SOCKET_MAX_NUM)]
        self.aAttr = [TPlayerItemAttribute() for _ in range(ITEM_ATTRIBUTE_MAX_NUM)]


class packet_item_ground_add:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.bHeader = 0
        self.x = 0
        self.y = 0
        self.z = 0
        self.dwVID = 0
        self.dwVnum = 0


class packet_item_ownership:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.bHeader = 0
        self.dwVID = 0
        self.szName = str(['\0' for _ in range(CHARACTER_NAME_MAX_LEN + 1)])


class packet_item_ground_del:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.bHeader = 0
        self.dwVID = 0


class packet_LG_QUICKSLOT_add:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.pos = 0
        self.slot = TQuickslot()


class packet_LG_QUICKSLOT_del:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.pos = 0


class packet_LG_QUICKSLOT_swap:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.pos = 0
        self.pos_to = 0


class packet_motion:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.vid = 0
        self.victim_vid = 0
        self.motion = 0


class EPacketShopSubHeaders(Enum):
    SHOP_SUBLG_HEADER_GC_START = 0
    SHOP_SUBLG_HEADER_GC_END = 1
    SHOP_SUBLG_HEADER_GC_UPDATE_ITEM = 2
    SHOP_SUBLG_HEADER_GC_UPDATE_PRICE = 3
    SHOP_SUBLG_HEADER_GC_OK = 4
    SHOP_SUBLG_HEADER_GC_NOT_ENOUGH_MONEY = 5
    SHOP_SUBLG_HEADER_GC_SOLDOUT = 6
    SHOP_SUBLG_HEADER_GC_INVENTORY_FULL = 7
    SHOP_SUBLG_HEADER_GC_INVALID_POS = 8
    SHOP_SUBLG_HEADER_GC_SOLD_OUT = 9
    SHOP_SUBLG_HEADER_GC_START_EX = 10
    SHOP_SUBLG_HEADER_GC_NOT_ENOUGH_MONEY_EX = 11
    SHOP_SUBLG_HEADER_GC_NOT_ENOUGH_ITEM = 12
    SHOP_SUBLG_HEADER_GC_NOT_ENOUGH_EXP = 13

class packet_shop_item:
    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.vnum = 0
        self.price = 0
        self.count = 0
        self.display_pos = 0
        self.alSockets = [0 for _ in range(LG_ITEM_SOCKET_MAX_NUM)]
        self.aAttr = [TPlayerItemAttribute() for _ in range(ITEM_ATTRIBUTE_MAX_NUM)]
        self.price_type = 1
        self.price_vnum = 0

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memset(self.alSockets, 0, sizeof(self.alSockets))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memset(self.aAttr, 0, sizeof(self.aAttr))

class packet_shop_start:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.owner_vid = 0
        self.items = [packet_shop_item() for _ in range(SHOP_HOST_ITEM_MAX_NUM)]


class packet_shop_start_ex:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.owner_vid = 0
        self.shop_tab_count = 0

    class sub_packet_shop_tab:

        def __init__(self):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.name = str(['\0' for _ in range(SHOP_TAB_NAME_MAX)])
            self.coin_type = 0
            self.items = [packet_shop_item() for _ in range(SHOP_HOST_ITEM_MAX_NUM)]


class packet_shop_update_item:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.pos = 0
        self.item = packet_shop_item()


class packet_shop_update_price:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.iPrice = 0


class packet_shop:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.size = 0
        self.subheader = 0


class packet_exchange:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.sub_header = 0
        self.is_me = 0
        self.arg1 = 0
        self.arg2 = TItemPos()
        self.arg3 = 0
        self.alSockets = [0 for _ in range(LG_ITEM_SOCKET_MAX_NUM)]
        self.aAttr = [TPlayerItemAttribute() for _ in range(ITEM_ATTRIBUTE_MAX_NUM)]


class EPacketTradeSubHeaders(Enum):
    EXCHANGE_SUBLG_HEADER_GC_START = 0
    EXCHANGE_SUBLG_HEADER_GC_ITEM_ADD = 1
    EXCHANGE_SUBLG_HEADER_GC_ITEM_DEL = 2
    EXCHANGE_SUBLG_HEADER_GC_GOLD_ADD = 3
    EXCHANGE_SUBLG_HEADER_GC_ACCEPT = 4
    EXCHANGE_SUBLG_HEADER_GC_END = 5
    EXCHANGE_SUBLG_HEADER_GC_ALREADY = 6
    EXCHANGE_SUBLG_HEADER_GC_LESS_GOLD = 7

class packet_position:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.vid = 0
        self.position = 0


class packet_ping:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0


class packet_script:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.size = 0
        self.skin = 0
        self.src_size = 0


class packet_change_speed:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.vid = 0
        self.moving_speed = 0


class packet_mount:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.vid = 0
        self.mount_vid = 0
        self.pos = 0
        self.x = 0
        self.y = 0


class packet_move:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.bHeader = 0
        self.bFunc = 0
        self.bArg = 0
        self.bRot = 0
        self.dwVID = 0
        self.lX = 0
        self.lY = 0
        self.dwTime = 0
        self.dwDuration = 0


class packet_ownership:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.bHeader = 0
        self.dwOwnerVID = 0
        self.dwVictimVID = 0


class packet_sync_position_element:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.dwVID = 0
        self.lX = 0
        self.lY = 0


class packet_sync_position:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.bHeader = 0
        self.wSize = 0


class packet_fly:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.bHeader = 0
        self.bType = 0
        self.dwStartVID = 0
        self.dwEndVID = 0


class command_fly_targeting:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.bHeader = 0
        self.dwTargetVID = 0
        self.x = 0
        self.y = 0


class packet_fly_targeting:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.bHeader = 0
        self.dwShooterVID = 0
        self.dwTargetVID = 0
        self.x = 0
        self.y = 0


class packet_shoot:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.bHeader = 0
        self.bType = 0


class EPVPModes(Enum):
    PVP_MODE_NONE = 0
    PVP_MODE_AGREE = 1
    PVP_MODE_FIGHT = 2
    PVP_MODE_REVENGE = 3

class packet_pvp:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.bHeader = 0
        self.dwVIDSrc = 0
        self.dwVIDDst = 0
        self.bMode = 0


class command_use_skill:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.bHeader = 0
        self.dwVnum = 0
        self.dwVID = 0


class command_target:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.dwVID = 0


class packet_target:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.dwVID = 0
        self.bHPPercent = 0
        self.iMinHP = 0
        self.iMaxHP = 0
        self.bElement = 0

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if ELEMENT_TARGET
##endif

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if ENABLE_TARGET_INFO
class packet_target_info:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.dwVID = 0
        self.race = 0
        self.dwVnum = 0
        self.count = 0

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Typedefs defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
#typedef packet_target_info TPacketGCTargetInfo;

class packet_target_info_load:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.dwVID = 0

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Typedefs defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
#typedef packet_target_info_load TPacketCGTargetInfoLoad;
##endif

class packet_warp:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.bHeader = 0
        self.lX = 0
        self.lY = 0
        self.lAddr = 0
        self.wPort = 0


class command_warp:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.bHeader = 0


class packet_quest_info:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.size = 0
        self.index = 0
        self.c_index = 0
        self.flag = 0

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if __QUEST_RENEWAL__
##endif

class packet_messenger:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.size = 0
        self.subheader = 0


class packet_messenger_guild_list:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.connected = 0
        self.length = 0


class packet_messenger_guild_login:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.length = 0


class packet_messenger_guild_logout:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.length = 0


class packet_messenger_list_offline:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.connected = 0
        self.length = 0


class packet_messenger_list_online:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.connected = 0
        self.length = 0


class command_messenger:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.subheader = 0


class command_messenger_add_by_vid:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.vid = 0


class command_messenger_add_by_name:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.length = 0



class command_messenger_remove:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.login = str(['\0' for _ in range(LOGIN_MAX_LEN+1)])


class command_safebox_checkout:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.bHeader = 0
        self.bSafePos = 0
        self.ItemPos = TItemPos()


class command_safebox_checkin:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.bHeader = 0
        self.bSafePos = 0
        self.ItemPos = TItemPos()


class command_party_parameter:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.bHeader = 0
        self.bDistributeMode = 0


class paryt_parameter:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.bHeader = 0
        self.bDistributeMode = 0


class packet_party_add:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.pid = 0
        self.name = str(['\0' for _ in range(CHARACTER_NAME_MAX_LEN+1)])


class command_party_invite:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.vid = 0


class packet_party_invite:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.leader_vid = 0


class command_party_invite_answer:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.leader_vid = 0
        self.accept = 0


class packet_party_update:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.pid = 0
        self.role = 0
        self.percent_hp = 0
        self.affects = [0 for _ in range(7)]


class packet_party_remove:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.pid = 0


class packet_party_link:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.pid = 0
        self.vid = 0


class packet_party_unlink:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.pid = 0
        self.vid = 0


class command_party_remove:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.pid = 0


class command_party_set_state:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.pid = 0
        self.byRole = 0
        self.flag = 0


class command_party_use_skill:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.bySkillIndex = 0
        self.vid = 0


class packet_safebox_size:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.bHeader = 0
        self.bSize = 0


class packet_safebox_wrong_password:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.bHeader = 0


class command_empire:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.bHeader = 0
        self.bEmpire = 0


class packet_empire:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.bHeader = 0
        self.bEmpire = 0


class command_safebox_money:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.bHeader = 0
        self.bState = 0
        self.lMoney = 0


class packet_safebox_money_change:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.bHeader = 0
        self.lMoney = 0


class GUILD_SUBLG_HEADER_CG(Enum):
    GUILD_SUBLG_HEADER_CG_ADD_MEMBER = 0
    GUILD_SUBLG_HEADER_CG_REMOVE_MEMBER = 1
    GUILD_SUBLG_HEADER_CG_CHANGE_GRADE_NAME = 2
    GUILD_SUBLG_HEADER_CG_CHANGE_GRADE_AUTHORITY = 3
    GUILD_SUBLG_HEADER_CG_OFFER = 4
    GUILD_SUBLG_HEADER_CG_POST_COMMENT = 5
    GUILD_SUBLG_HEADER_CG_DELETE_COMMENT = 6
    GUILD_SUBLG_HEADER_CG_REFRESH_COMMENT = 7
    GUILD_SUBLG_HEADER_CG_CHANGE_MEMBER_GRADE = 8
    GUILD_SUBLG_HEADER_CG_USE_SKILL = 9
    GUILD_SUBLG_HEADER_CG_CHANGE_MEMBER_GENERAL = 10
    GUILD_SUBLG_HEADER_CG_GUILD_INVITE_ANSWER = 11
    GUILD_SUBLG_HEADER_CG_CHARGE_GSP = 12
    GUILD_SUBLG_HEADER_CG_DEPOSIT_MONEY = 13
    GUILD_SUBLG_HEADER_CG_WITHDRAW_MONEY = 14

class packet_guild:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.size = 0
        self.subheader = 0


class packet_guild_name_t:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.size = 0
        self.subheader = 0
        self.guildID = 0
        self.guildName = str(['\0' for _ in range(GUILD_NAME_MAX_LEN)])


class packet_guild_war:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.dwGuildSelf = 0
        self.dwGuildOpp = 0
        self.bType = 0
        self.bWarState = 0


class command_guild:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.subheader = 0


class command_guild_answer_make_guild:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.guild_name = str(['\0' for _ in range(GUILD_NAME_MAX_LEN+1)])


class command_guild_use_skill:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.dwVnum = 0
        self.dwPID = 0


class command_mark_login:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.handle = 0
        self.random_key = 0


class command_mark_upload:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.gid = 0
        self.image = [0 for _ in range(16 *12 *4)]


class command_mark_idxlist:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0


class command_mark_crclist:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.imgIdx = 0
        self.crclist = [0 for _ in range(80)]


class packet_mark_idxlist:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.bufSize = 0
        self.count = 0


class packet_mark_block:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.bufSize = 0
        self.imgIdx = 0
        self.count = 0


class command_symbol_upload:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.size = 0
        self.guild_id = 0


class command_symbol_crc:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.guild_id = 0
        self.crc = 0
        self.size = 0


class packet_symbol_data:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.size = 0
        self.guild_id = 0


class command_fishing:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.dir = 0


class packet_fishing:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.subheader = 0
        self.info = 0
        self.dir = 0


class command_give_item:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.byHeader = 0
        self.dwTargetVID = 0
        self.ItemPos = TItemPos()
        self.byItemCount = 0


class SPacketCGHack:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.bHeader = 0
        self.szBuf = str(['\0' for _ in range(255 + 1)])


class packet_dungeon:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.bHeader = 0
        self.size = 0
        self.subheader = 0


class packet_dungeon_dest_position:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.x = 0
        self.y = 0


class SPacketGCShopSign:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.bHeader = 0
        self.dwVID = 0
        self.szSign = str(['\0' for _ in range(SHOP_SIGN_MAX_LEN + 1)])


class SPacketCGMyShop:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.bHeader = 0
        self.szSign = str(['\0' for _ in range(SHOP_SIGN_MAX_LEN + 1)])
        self.wCount = 0


class SPacketGCTime:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.bHeader = 0
        self.time = time_t()


class SPacketGCWalkMode:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.vid = 0
        self.mode = 0


class SPacketGCChangeSkillGroup:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.LG_SKILL_group = 0


class SPacketCGRefine:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.pos = 0
        self.type = 0


class SPacketCGRequestRefineInfo:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.pos = 0


class SPacketGCRefineInformaion:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.type = 0
        self.pos = 0
        self.src_vnum = 0
        self.result_vnum = 0
        self.material_count = 0
        self.cost = 0
        self.prob = 0
        self.materials = [TRefineMaterial() for _ in range(REFINE_MATERIAL_MAX_NUM)]


class TNPCPosition:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.bType = 0
        self.name = str(['\0' for _ in range(CHARACTER_NAME_MAX_LEN+1)])
        self.x = 0
        self.y = 0


class SPacketGCNPCPosition:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.size = 0
        self.count = 0


class SPacketGCSpecialEffect:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.type = 0
        self.vid = 0


class SPacketCGChangeName:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.index = 0
        self.name = str(['\0' for _ in range(CHARACTER_NAME_MAX_LEN+1)])


class SPacketGCChangeName:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.pid = 0
        self.name = str(['\0' for _ in range(CHARACTER_NAME_MAX_LEN+1)])



class command_client_version:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.filename = str(['\0' for _ in range(32+1)])
        self.timestamp = str(['\0' for _ in range(32+1)])


class command_client_version2:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.filename = str(['\0' for _ in range(32+1)])
        self.timestamp = str(['\0' for _ in range(32+1)])


class packet_channel:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.channel = 0


class packet_view_equip:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.vid = 0
        self.equips = [AnonymousClass() for _ in range(WEAR_MAX_NUM)]

## Laniatus Games Studio Inc. | NOTE: Classes must be named in Python, so the following class has been named by the converter:
    class AnonymousClass:

        def __init__(self):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.vnum = 0
            self.count = 0
            self.alSockets = [0 for _ in range(LG_ITEM_SOCKET_MAX_NUM)]
            self.aAttr = [TPlayerItemAttribute() for _ in range(ITEM_ATTRIBUTE_MAX_NUM)]


class TLandPacketElement:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.dwID = 0
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0
        self.dwGuildID = 0


class packet_land_list:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.size = 0


class TPacketGCTargetCreate:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.bHeader = 0
        self.lID = 0
        self.szName = str(['\0' for _ in range(32+1)])
        self.dwVID = 0
        self.bType = 0


class TPacketGCTargetUpdate:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.bHeader = 0
        self.lID = 0
        self.lX = 0
        self.lY = 0


class TPacketGCTargetDelete:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.bHeader = 0
        self.lID = 0


class TPacketGLaniaCAffectsAdd:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.bHeader = 0
        self.elem = TPacketAffectElement()


class TPacketGLaniaCAffectsRemove:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.bHeader = 0
        self.dwType = 0
        self.bApplyOn = 0


class packet_lover_info:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.name = str(['\0' for _ in range(CHARACTER_NAME_MAX_LEN + 1)])
        self.love_point = 0


class packet_love_LG_POINT_update:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.love_point = 0


class packet_dig_motion:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.vid = 0
        self.target_vid = 0
        self.count = 0


class command_script_select_item:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.selection = 0


class packet_damage_info:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.dwVID = 0
        self.flag = 0
        self.damage = 0


class SPacketGGCheckAwakeness:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.bHeader = 0


## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if _IMPROVED_PACKET_ENCRYPTION_
class TPacketKeyAgreement:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.bHeader = 0
        self.wAgreedLength = 0
        self.wDataLength = 0
        self.data = [0 for _ in range(TPacketKeyAgreement.MAX_DATA_LEN)]

    MAX_DATA_LEN = 256

class TPacketKeyAgreementCompleted:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.bHeader = 0
        self.data = [0 for _ in range(3)]


##endif

class SPacketGCSpecificEffect:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.vid = 0
        self.effect_file = str(['\0' for _ in range(DefineConstants.MAX_EFFECT_FILE_NAME)])


class EDragonSoulRefineWindowRefineType(Enum):
    DRAGONSOULREFINEWINDOW_UPGRADE = 0
    DRAGONSOULREFINEWINDOW_IMPROVEMENT = 1
    DRAGONSOULREFINEWINDOW_REFINE = 2

class EPacketCGDragonSoulSubHeaderType(Enum):
    DS_SUB_LG_HEADER_OPEN = 0
    DS_SUB_LG_HEADER_CLOSE = 1
    DS_SUB_LG_HEADER_DO_REFINE_GRADE = 2
    DS_SUB_LG_HEADER_DO_REFINE_STEP = 3
    DS_SUB_LG_HEADER_DO_REFINE_STRENGTH = 4
    DS_SUB_LG_HEADER_REFINE_FAIL = 5
    DS_SUB_LG_HEADER_REFINE_FAIL_MAX_REFINE = 6
    DS_SUB_LG_HEADER_REFINE_FAIL_INVALID_MATERIAL = 7
    DS_SUB_LG_HEADER_REFINE_FAIL_NOT_ENOUGH_MONEY = 8
    DS_SUB_LG_HEADER_REFINE_FAIL_NOT_ENOUGH_MATERIAL = 9
    DS_SUB_LG_HEADER_REFINE_FAIL_TOO_MUCH_MATERIAL = 10
    DS_SUB_LG_HEADER_REFINE_SUCCEED = 11
class SPacketCGDragonSoulRefine:
    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.bSubType = 0
        self.ItemGrid = [TItemPos() for _ in range(DRAGON_SOUL_REFINE_GRID_SIZE)]

        self.header = byte(Globals.LG_HEADER_CG_DRAGON_SOUL_REFINE)

class SPacketGCDragonSoulRefine:
    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.bSubType = 0
        self.Pos = TItemPos()

        self.header = byte(Globals.LG_HEADER_GC_DRAGON_SOUL_REFINE)

class SPacketCGStateCheck:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.key = 0
        self.index = 0


class SPacketGCStateCheck:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.key = 0
        self.index = 0
        self.state = 0


class ACCE_SUBLG_HEADER_GC(Enum):
    ACCE_SUBLG_HEADER_GC_SET_ITEM = 0
    ACCE_SUBLG_HEADER_GC_CLEAR_SLOT = 1
    ACCE_SUBLG_HEADER_GC_CLEAR_ALL = 2

class ACCE_SUBLG_HEADER_CG(Enum):
    ACCE_SUBLG_HEADER_CG_REFINE_CHECKIN = 0
    ACCE_SUBLG_HEADER_CG_REFINE_CHECKOUT = 1
    ACCE_SUBLG_HEADER_CG_REFINE_ACCEPT = 2
    ACCE_SUBLG_HEADER_CG_REFINE_CANCEL = 3


class packet_acce:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.size = 0
        self.subheader = 0



class command_acce:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.subheader = 0


class command_acce_checkout:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.bAccePos = 0


class command_acce_checkin:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.bAccePos = 0
        self.ItemPos = TItemPos()


class command_acce_accept:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.windowType = 0


## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if __MULTI_LANGUAGE_SYSTEM__
class SPacketGGLocaleNotice:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.bHeader = 0
        self.bBigFont = False
        self.szNotice = [[] for _ in range(MAX_QUEST_NOTICE_ARGS + 1)]

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Typedefs defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
#typedef SPacketGGLocaleNotice TPacketGGLocaleNotice;

class SPacketChangeLanguage:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.bHeader = 0
        self.bLanguage = 0

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Typedefs defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
#typedef SPacketChangeLanguage TPacketChangeLanguage;
##endif

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if __EXTENDED_WHISPER_DETAILS__
class SPacketCGWhisperDetails:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.name = str(['\0' for _ in range(CHARACTER_NAME_MAX_LEN + 1)])

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Typedefs defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
#typedef SPacketCGWhisperDetails TPacketCGWhisperDetails;

class SPacketGCWhisperDetails:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.name = str(['\0' for _ in range(CHARACTER_NAME_MAX_LEN + 1)])
        self.bLanguage = 0

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if __MULTI_LANGUAGE_SYSTEM__
##endif
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Typedefs defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
#typedef SPacketGCWhisperDetails TPacketGCWhisperDetails;
##endif

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##pragma pack()
