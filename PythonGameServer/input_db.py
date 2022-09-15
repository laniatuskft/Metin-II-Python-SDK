from building import *

import math

def LoginSuccess(dwHandle, data):
    #sys_log(0, "LoginSuccess")

    pTab = data

    it = g_sim.find(pTab.id)
    if g_sim.end() != it:
        #sys_log(0, "CInputDB::LoginSuccess - already exist sim [%s]", pTab.login)
        it.second.SendLoad()
        return

    d = DESC_MANAGER.instance().FindByHandle(dwHandle)

    if d is None:
        #sys_log(0, "CInputDB::LoginSuccess - cannot find handle [%s]", pTab.login)

        pack = SLogoutPacket()

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        strncpy_s(pack.login, sizeof(pack.login), pTab.login, _TRUNCATE)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        db_clientdesc.DBPacket(LG_HEADER_GD_LOGOUT, dwHandle, pack, sizeof(pack))
        return

    if strcmp(pTab.status, "OK"):
        #sys_log(0, "CInputDB::LoginSuccess - status[%s] is not OK [%s]", pTab.status, pTab.login)

        pack = SLogoutPacket()

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        strncpy_s(pack.login, sizeof(pack.login), pTab.login, _TRUNCATE)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        db_clientdesc.DBPacket(LG_HEADER_GD_LOGOUT, dwHandle, pack, sizeof(pack))

        LoginFailure(d, pTab.status)
        return

    i = 0
    while i != LGEMiscellaneous.PLAYER_PER_ACCOUNT:
        player = pTab.players[i]
        #sys_log(0, "\tplayer(%s).job(%d)", player.szName, player.byJob)
        i += 1

    bFound = GetServerLocation(pTab, pTab.bEmpire)

    d.BindAccountTable(pTab)

    if not bFound:
        pe = packet_empire()
        pe.bHeader = byte(LG_HEADER_GC_EMPIRE)
        pe.bEmpire = number(1, 3)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        d.Packet(pe, sizeof(pe))
    else:
        pe = packet_empire()
        pe.bHeader = byte(LG_HEADER_GC_EMPIRE)
        pe.bEmpire = d.GetEmpire()
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        d.Packet(pe, sizeof(pe))

    d.SetPhase(EPhase.PHASE_SELECT)
    d.SendLoginSuccessPacket()

    #sys_log(0, "InputDB::login_success: %s", pTab.login)

def PlayerCreateFailure(d, bType):
    if d is None:
        return

    pack = packet_create_failure()

    pack.header = byte(LG_HEADER_GC_CHARACTER_CREATE_FAILURE)
    pack.bType = bType

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    d.Packet(pack, sizeof(pack))

def PlayerCreateSuccess(d, data):
    if d is None:
        return

    pPacketDB = data

    if pPacketDB.bAccountCharacterIndex >= LGEMiscellaneous.PLAYER_PER_ACCOUNT:
        d.Packet(encode_byte(LG_HEADER_GC_CHARACTER_CREATE_FAILURE), 1)
        return

    lIndex = 0

    temp_ref_lIndex = RefObject(lIndex);
    temp_ref_lAddr = RefObject(pPacketDB.player.lAddr);
    temp_ref_wPort = RefObject(pPacketDB.player.wPort);
    if not CMapLocation.instance().Get(pPacketDB.player.x, pPacketDB.player.y, temp_ref_lIndex, temp_ref_lAddr, temp_ref_wPort):
        pPacketDB.player.wPort = temp_ref_wPort.arg_value
        pPacketDB.player.lAddr = temp_ref_lAddr.arg_value
        lIndex = temp_ref_lIndex.arg_value
        #lani_err("InputDB::PlayerCreateSuccess: cannot find server for mapindex %d %d x %d (name %s)", lIndex, pPacketDB.player.x, pPacketDB.player.y, pPacketDB.player.szName)
    else:
        pPacketDB.player.wPort = temp_ref_wPort.arg_value
        pPacketDB.player.lAddr = temp_ref_lAddr.arg_value
        lIndex = temp_ref_lIndex.arg_value

    r_Tab = d.GetAccountTable()
## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: r_Tab.players[pPacketDB->bAccountCharacterIndex] = pPacketDB->player;
    r_Tab.players[pPacketDB.bAccountCharacterIndex].copy_from(pPacketDB.player)

    pack = command_player_create_success()

    pack.header = byte(LG_HEADER_GC_CHARACTER_CREATE_SUCCESS)
    pack.bAccountCharacterIndex = pPacketDB.bAccountCharacterIndex
## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: pack.player = pPacketDB->player;
    pack.player.copy_from(pPacketDB.player)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    d.Packet(pack, sizeof(command_player_create_success))
    t = SPlayerItem()
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    memset(t, 0, sizeof(t))

def PlayerDeleteSuccess(d, data):
    if d is None:
        return

    account_index = None
    account_index = decode_byte(data)
    d.BufferedPacket(encode_byte(LG_HEADER_GC_CHARACTER_DELETE_SUCCESS), 1)
    d.Packet(encode_byte(account_index), 1)

    d.GetAccountTable().players[account_index].dwID = 0

def PlayerDeleteFail(d):
    if d is None:
        return

    d.Packet(encode_byte(LG_HEADER_GC_CHARACTER_DELETE_WRONG_SOCIAL_ID), 1)

def ChangeName(d, data):
    if d is None:
        return

    p = data

    r = d.GetAccountTable()

    if r.id == 0:
        return

    i = 0
    while i < LGEMiscellaneous.PLAYER_PER_ACCOUNT:
        if r.players[i].dwID == p.pid:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            strncpy_s(r.players[i].szName, sizeof(r.players[i].szName), p.name, _TRUNCATE)
            r.players[i].bChangeName = 0

            pgc = SPacketGCChangeName()

            pgc.header = byte(LG_HEADER_GC_CHANGE_NAME)
            pgc.pid = p.pid
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            strncpy_s(pgc.name, sizeof(pgc.name), p.name, _TRUNCATE)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            d.Packet(pgc, sizeof(SPacketGCChangeName))
            break
        i += 1

def PlayerLoad(d, data):
    pTab = data

    if d is None:
        return

    lMapIndex = pTab.lMapIndex
    pos = pixel_position_s()

    if lMapIndex == 0:
        lMapIndex = SECTREE_MANAGER.instance().GetMapIndex(pTab.x, pTab.y)

        if lMapIndex == 0:
            lMapIndex = int(EMPIRE_START_MAP(d.GetAccountTable().bEmpire))
            pos.x = int(EMPIRE_START_X(d.GetAccountTable().bEmpire))
            pos.y = int(EMPIRE_START_Y(d.GetAccountTable().bEmpire))
        else:
            pos.x = pTab.x
            pos.y = pTab.y
    pTab.lMapIndex = lMapIndex

    temp_ref_lMapIndex = RefObject(lMapIndex);
    if not SECTREE_MANAGER.instance().GetValidLocation(pTab.lMapIndex, pTab.x, pTab.y, temp_ref_lMapIndex, pos, d.GetEmpire()):
        lMapIndex = temp_ref_lMapIndex.arg_value
        #lani_err("InputDB::PlayerLoad : cannot find valid location %d x %d (name: %s)", pTab.x, pTab.y, pTab.name)
        d.SetPhase(EPhase.PHASE_CLOSE)
        return
    else:
        lMapIndex = temp_ref_lMapIndex.arg_value

    pTab.x = pos.x
    pTab.y = pos.y
    pTab.lMapIndex = lMapIndex

    if d.GetCharacter() is not None or d.IsPhase(EPhase.PHASE_GAME):
        p = d.GetCharacter()
        #lani_err("login state already has main state (character %s %p)", p.GetName(LOCALE_LANIATUS), get_pointer(p))
        return

    if None is not CHARACTER_MANAGER.Instance().FindPC(pTab.name):
        #lani_err("InputDB: PlayerLoad : %s already exist in game", pTab.name)
        return

    ch = CHARACTER_MANAGER.instance().CreateCharacter(pTab.name, pTab.id)

    ch.BindDesc(d)
    ch.SetPlayerProto(pTab)
    ch.SetEmpire(d.GetEmpire())

    d.BindCharacter(ch)

        p = SPacketGGLogin()

        p.bHeader = byte(LG_HEADER_GG_LOGIN)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        strncpy_s(p.szName, sizeof(p.szName), ch.GetName(LOCALE_LANIATUS), _TRUNCATE)
        p.dwPID = ch.GetPlayerID()
        p.bEmpire = ch.GetEmpire()
        p.lMapIndex = SECTREE_MANAGER.instance().GetMapIndex(ch.GetX(), ch.GetY())
        p.bChannel = g_bChannel
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if __MULTI_LANGUAGE_SYSTEM__
        p.bLanguage = d.GetLanguage() if d is not None else LaniatusLocalization.LOCALE_LANIATUS
##endif

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        P2P_MANAGER.instance().Send(p, sizeof(SPacketGGLogin), NULL)

    d.SetPhase(EPhase.PHASE_LOADING)
    ch.MainCharacterPacket()

    lPublicMapIndex = math.trunc(lMapIndex / float(10000)) if lMapIndex >= 10000 else lMapIndex

    if not map_allow_find(lPublicMapIndex):
        #lani_err("InputDB::PlayerLoad : entering %d map is not allowed here (name: %s, empire %u)", lMapIndex, pTab.name, d.GetEmpire())

        ch.SetWarpLocation(int(EMPIRE_START_MAP(d.GetEmpire())), math.trunc(EMPIRE_START_X(d.GetEmpire()) / float(100)), math.trunc(EMPIRE_START_Y(d.GetEmpire()) / float(100)))

        d.SetPhase(EPhase.PHASE_CLOSE)
        return

    quest.CQuestManager.instance().BroadcastEventFlagOnLogin(ch)

    i = 0
    while i < LGEMiscellaneous.LG_QUICKSLOT_MAX_NUM:
        ch.SetQuickslot(byte(i), pTab.quickslot[i])
        i += 1

    ch.PointsPacket()
    ch.SkillLevelPacket()

    #sys_log(0, "InputDB: player_load %s %dx%dx%d LEVEL %d MOV_SPEED %d JOB %d ATG %d DFG %d GMLv %d", pTab.name, ch.GetX(), ch.GetY(), ch.GetZ(), ch.GetLevel(), ch.GetPoint(EPointTypes.LG_POINT_MOV_SPEED), ch.GetJob(), ch.GetPoint(EPointTypes.LG_POINT_ATT_GRADE), ch.GetPoint(EPointTypes.LG_POINT_DEF_GRADE), ch.GetGMLevel())

    ch.QuerySafeboxSize()

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Pointer arithmetic is detected on the parameter 'data':
#ORIGINAL METINII C CODE: void CInputDB::Boot(const char* data)
def Boot(data):
    signal_timer_disable()
    dwPacketSize = uint(decode_4bytes(data))
    data += 4

    bVersion = decode_byte(data)
    data += 1

    #sys_log(0, "BOOT: PACKET: %d", dwPacketSize)
    #sys_log(0, "BOOT: VERSION: %d", bVersion)
    if bVersion != 6:
        #lani_err("boot version error")
        thecore_shutdown()

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    #sys_log(0, "sizeof(TMobTable) = %d", sizeof(SMobTable))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    #sys_log(0, "sizeof(TItemTable) = %d", sizeof(SItemTable))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    #sys_log(0, "sizeof(TShopTable) = %d", sizeof(SShopTable))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    #sys_log(0, "sizeof(TSkillTable) = %d", sizeof(SSkillTable))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    #sys_log(0, "sizeof(TRefineTable) = %d", sizeof(SRefineTable))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    #sys_log(0, "sizeof(TItemAttrTable) = %d", sizeof(TItemAttrTable))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    #sys_log(0, "sizeof(TItemRareTable) = %d", sizeof(TItemAttrTable))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    #sys_log(0, "sizeof(TLand) = %d", sizeof(SLand))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    #sys_log(0, "sizeof(TObjectProto) = %d", sizeof(SObjectProto))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    #sys_log(0, "sizeof(TObject) = %d", sizeof(SObject))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    #sys_log(0, "sizeof(TAdminManager) = %d", sizeof(TAdminInfo))

    size = None

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    if decode_2bytes(data)!=sizeof(SMobTable):
        #lani_err("mob table size error")
        thecore_shutdown()
        return
    data += 2

    size = decode_2bytes(data)
    data += 2
    #sys_log(0, "BOOT: MOB: %d", size)

    if size != 0:
        CMobManager.instance().Initialize(data, size)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        data += size * sizeof(SMobTable)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    if decode_2bytes(data) != sizeof(SItemTable):
        #lani_err("item table size error")
        thecore_shutdown()
        return
    data += 2

    size = decode_2bytes(data)
    data += 2
    #sys_log(0, "BOOT: ITEM: %d", size)


    if size != 0:
        ITEM_MANAGER.instance().Initialize(data, size)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        data += size * sizeof(SItemTable)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    if decode_2bytes(data) != sizeof(SShopTable):
        #lani_err("shop table size error")
        thecore_shutdown()
        return
    data += 2

    size = decode_2bytes(data)
    data += 2
    #sys_log(0, "BOOT: SHOP: %d", size)


    if size != 0:
        if not CShopManager.instance().Initialize(data, size):
            #lani_err("shop table Initialize error")
            thecore_shutdown()
            return
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        data += size * sizeof(SShopTable)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    if decode_2bytes(data) != sizeof(SSkillTable):
        #lani_err("skill table size error")
        thecore_shutdown()
        return
    data += 2

    size = decode_2bytes(data)
    data += 2
    #sys_log(0, "BOOT: SKILL: %d", size)

    if size != 0:
        if not CSkillManager.instance().Initialize(data, size):
            #lani_err("cannot initialize skill table")
            thecore_shutdown()
            return

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        data += size * sizeof(SSkillTable)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    if decode_2bytes(data) != sizeof(SRefineTable):
        #lani_err("refine table size error")
        thecore_shutdown()
        return
    data += 2

    size = decode_2bytes(data)
    data += 2
    #sys_log(0, "BOOT: REFINE: %d", size)

    if size != 0:
        CRefineManager.instance().Initialize(data, size)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        data += size * sizeof(SRefineTable)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    if decode_2bytes(data) != sizeof(TItemAttrTable):
        #lani_err("item attr table size error")
        thecore_shutdown()
        return
    data += 2

    size = decode_2bytes(data)
    data += 2
    #sys_log(0, "BOOT: ITEM_ATTR: %d", size)

    if size != 0:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Pointer arithmetic is detected on this variable:
#ORIGINAL METINII C CODE: TItemAttrTable * p = (TItemAttrTable *) data;
        p = data

        i = 0
        while i < size:
            if p.dwApplyIndex >= EApplyTypes.MAX_APPLY_NUM:
                continue

            g_map_itemAttr[p.dwApplyIndex] = *p
            #sys_log(0, "ITEM_ATTR[%d]: %s %u", p.dwApplyIndex, p.szApply, p.dwProb)
            i += 1
            p += 1

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    data += size * sizeof(TItemAttrTable)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    if decode_2bytes(data) != sizeof(TItemAttrTable):
        #lani_err("item rare table size error")
        thecore_shutdown()
        return
    data += 2

    size = decode_2bytes(data)
    data += 2
    #sys_log(0, "BOOT: ITEM_RARE: %d", size)

    if size != 0:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Pointer arithmetic is detected on this variable:
#ORIGINAL METINII C CODE: TItemAttrTable * p = (TItemAttrTable *) data;
        p = data

        i = 0
        while i < size:
            if p.dwApplyIndex >= EApplyTypes.MAX_APPLY_NUM:
                continue

            g_map_itemRare[p.dwApplyIndex] = *p
            #sys_log(0, "ITEM_RARE[%d]: %s %u", p.dwApplyIndex, p.szApply, p.dwProb)
            i += 1
            p += 1

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    data += size * sizeof(TItemAttrTable)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        if decode_2bytes(data) != sizeof(TLand):
            #lani_err("land table size error")
            thecore_shutdown()
            return
        data += 2

        size = decode_2bytes(data)
        data += 2

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Pointer arithmetic is detected on this variable:
#ORIGINAL METINII C CODE: TLand * kLand = (TLand *) data;
        kLand = data
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        data += size * sizeof(TLand)

        i = 0
        while i < size:
            CManager.instance().LoadLand(TLand(kLand))
            i += 1
            kLand += 1

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        if decode_2bytes(data) != sizeof(TObjectProto):
            #lani_err("object proto table size error")
            thecore_shutdown()
            return
        data += 2

        size = decode_2bytes(data)
        data += 2

        CManager.instance().LoadObjectProto(data, size)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        data += size * sizeof(TObjectProto)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        if decode_2bytes(data) != sizeof(TObject):
            #lani_err("object table size error")
            thecore_shutdown()
            return
        data += 2

        size = decode_2bytes(data)
        data += 2

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Pointer arithmetic is detected on this variable:
#ORIGINAL METINII C CODE: TObject * kObj = (TObject *) data;
        kObj = data
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        data += size * sizeof(TObject)

        i = 0
        while i < size:
            CManager.instance().LoadObject(TObject(kObj), ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
            i += 1
            kObj += 1
    set_global_time(data)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    data += sizeof(time_t)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    if decode_2bytes(data) != sizeof(tItemIDRange):
        #lani_err("ITEM ID RANGE size error")
        thecore_shutdown()
        return
    data += 2

    size = decode_2bytes(data)
    data += 2

    range = data
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    data += size * sizeof(tItemIDRange)

    rangespare = data
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    data += size * sizeof(tItemIDRange)

    ChunkSize = decode_2bytes(data)
    data += 2
    HostSize = decode_2bytes(data)
    data += 2
    #sys_log(0, "GM Value Count %d %d", HostSize, ChunkSize)
    for n in range(0, HostSize):
        gm_new_host_inert(data)
        #sys_log(0, "GM HOST : IP[%s] ", data)
        data += ChunkSize


    data += 2
    adminsize = decode_2bytes(data)
    data += 2

    for n in range(0, adminsize):
        rAdminInfo = data

        gm_new_insert(rAdminInfo)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        data += sizeof(rAdminInfo)

    endCheck = decode_2bytes(data)
    if endCheck != 0xffff:
        #lani_err("boot packet end check error [%x]!=0xffff", endCheck)
        thecore_shutdown()
        return
    else:
        #sys_log(0, "boot packet end check ok [%x]==0xffff", endCheck)
    data +=2

    if not ITEM_MANAGER.instance().SetMaxItemID(range):
        #lani_err("not enough item id contact your administrator!")
        thecore_shutdown()
        return

    if not ITEM_MANAGER.instance().SetMaxSpareItemID(rangespare):
        #lani_err("not enough item id for spare contact your administrator!")
        thecore_shutdown()
        return

    FILE_NAME_LEN = 256
    szCommonDropItemFileName = str(['\0' for _ in range(FILE_NAME_LEN)])
    szETCDropItemFileName = str(['\0' for _ in range(FILE_NAME_LEN)])
    szMOBDropItemFileName = str(['\0' for _ in range(FILE_NAME_LEN)])
    szDropItemGroupFileName = str(['\0' for _ in range(FILE_NAME_LEN)])
    szSpecialItemGroupFileName = str(['\0' for _ in range(FILE_NAME_LEN)])
    szMapIndexFileName = str(['\0' for _ in range(FILE_NAME_LEN)])
    szItemVnumMaskTableFileName = str(['\0' for _ in range(FILE_NAME_LEN)])
    szDragonSoulTableFileName = str(['\0' for _ in range(FILE_NAME_LEN)])

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    snprintf(szCommonDropItemFileName, sizeof(szCommonDropItemFileName), "%s/common_drop_item.txt", LocaleService_GetBasePath())
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    snprintf(szETCDropItemFileName, sizeof(szETCDropItemFileName), "%s/etc_drop_item.txt", LocaleService_GetBasePath())
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    snprintf(szMOBDropItemFileName, sizeof(szMOBDropItemFileName), "%s/mob_drop_item.txt", LocaleService_GetBasePath())
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    snprintf(szSpecialItemGroupFileName, sizeof(szSpecialItemGroupFileName), "%s/special_item_group.txt", LocaleService_GetBasePath())
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    snprintf(szDropItemGroupFileName, sizeof(szDropItemGroupFileName), "%s/drop_item_group.txt", LocaleService_GetBasePath())
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    snprintf(szMapIndexFileName, sizeof(szMapIndexFileName), "%s/index", LocaleService_GetMapPath())
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    snprintf(szItemVnumMaskTableFileName, sizeof(szItemVnumMaskTableFileName), "%s/ori_to_new_table.txt", LocaleService_GetBasePath())
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    snprintf(szDragonSoulTableFileName, sizeof(szDragonSoulTableFileName), "%s/dragon_soul_table.txt", LocaleService_GetBasePath())

    #sys_log(0, "Initializing Informations of Cube System")
    if not Cube_InformationInitialize():
        #lani_err("cannot init cube infomation.")
        thecore_shutdown()
        return

    #sys_log(0, "LoadLocaleFile: CommonDropItem: %s", szCommonDropItemFileName)
    if not ITEM_MANAGER.instance().ReadCommonDropItemFile(szCommonDropItemFileName):
        #lani_err("cannot load CommonDropItem: %s", szCommonDropItemFileName)
        thecore_shutdown()
        return

    #sys_log(0, "LoadLocaleFile: ETCDropItem: %s", szETCDropItemFileName)
    if not ITEM_MANAGER.instance().ReadEtcDropItemFile(szETCDropItemFileName):
        #lani_err("cannot load ETCDropItem: %s", szETCDropItemFileName)
        thecore_shutdown()
        return

    #sys_log(0, "LoadLocaleFile: DropItemGroup: %s", szDropItemGroupFileName)
    if not ITEM_MANAGER.instance().ReadDropItemGroup(szDropItemGroupFileName):
        #lani_err("cannot load DropItemGroup: %s", szDropItemGroupFileName)
        thecore_shutdown()
        return

    #sys_log(0, "LoadLocaleFile: SpecialItemGroup: %s", szSpecialItemGroupFileName)
    if not ITEM_MANAGER.instance().ReadSpecialDropItemFile(szSpecialItemGroupFileName):
        #lani_err("cannot load SpecialItemGroup: %s", szSpecialItemGroupFileName)
        thecore_shutdown()
        return

    #sys_log(0, "LoadLocaleFile: ItemVnumMaskTable : %s", szItemVnumMaskTableFileName)
    if not ITEM_MANAGER.instance().ReadItemVnumMaskTable(szItemVnumMaskTableFileName):
        #sys_log(0, "Could not open MaskItemTable")

    #sys_log(0, "LoadLocaleFile: MOBDropItemFile: %s", szMOBDropItemFileName)
    if not ITEM_MANAGER.instance().ReadMonsterDropItemGroup(szMOBDropItemFileName):
        #lani_err("cannot load MOBDropItemFile: %s", szMOBDropItemFileName)
        thecore_shutdown()
        return

    #sys_log(0, "LoadLocaleFile: MapIndex: %s", szMapIndexFileName)
    if (SECTREE_MANAGER.instance().Build(szMapIndexFileName, LocaleService_GetMapPath())) == 0:
        #lani_err("cannot load MapIndex: %s", szMapIndexFileName)
        thecore_shutdown()
        return

    #sys_log(0, "LoadLocaleFile: DragonSoulTable: %s", szDragonSoulTableFileName)
    if not DSManager.instance().ReadDragonSoulTableFile(szDragonSoulTableFileName):
        #lani_err("cannot load DragonSoulTable: %s", szDragonSoulTableFileName)

    building.CManager.instance().FinalizeBoot()

    CMotionManager.instance().Build()

    signal_timer_enable(30)

    if test_server:
        CMobManager.instance().DumpRegenCount("mob_count")

class quest_login_event_info(event_info_data):

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.dwPID = 0

        self.dwPID = 0

def QuestLoad(d, c_pData):
    if None is d:
        return

    ch = d.GetCharacter()

    if None is ch:
        return

    dwCount = uint(decode_4bytes(c_pData))

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no equivalent to 'reinterpret_cast' in Python:
    pQuestTable = reinterpret_cast<const SQuestTable>(c_pData[4:])

    if None != pQuestTable:
        if dwCount != 0:
            if ch.GetPlayerID() != pQuestTable[0].dwPID:
                #lani_err("PID differs %u %u", ch.GetPlayerID(), pQuestTable[0].dwPID)
                return

        #sys_log(0, "QUEST_LOAD: count %d", dwCount)

        pkPC = quest.CQuestManager.instance().GetPCForce(ch.GetPlayerID())

        if pkPC is None:
            #lani_err("null quest::PC with id %u", pQuestTable[0].dwPID)
            return

        if pkPC.IsLoaded():
            return

        for i in range(0, dwCount):
            st = pQuestTable[i].szName

            st += "."
            st += pQuestTable[i].szState

            #sys_log(0, "            %s %d", st, pQuestTable[i].lValue)
            pkPC.SetFlag(st, pQuestTable[i].lValue, LGEMiscellaneous.DEFINECONSTANTS.false)

        pkPC.SetLoaded()
        pkPC.Build()

        if ch.GetDesc().IsPhase(EPhase.PHASE_GAME):
            #sys_log(0, "QUEST_LOAD: Login pc %d", pQuestTable[0].dwPID)
            quest.CQuestManager.instance().Login(pQuestTable[0].dwPID, NULL)
        else:
            info = AllocEventInfo()
            info.dwPID = ch.GetPlayerID()

            event_create_ex(quest_login_event, info, ((1) * passes_per_sec))

def SafeboxLoad(d, c_pData):
    if d is None:
        return

    p = c_pData

    if d.GetAccountTable().id != p.dwID:
        #lani_err("SafeboxLoad: safebox has different id %u != %u", d.GetAccountTable().id, p.dwID)
        return

    if d.GetCharacter() is None:
        return

    bSize = 1

    ch = d.GetCharacter()

    if ch.GetShopOwner() is not None or ch.GetExchange() is not None or ch.GetMyShop() is not None or ch.IsCubeOpen() or ch.IsAcceWindowOpen():
        d.GetCharacter().ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You cannot open a storage if another Trade Window is open."))
        d.GetCharacter().CancelSafeboxLoad()
        return

    if d.GetCharacter().GetPremiumRemainSeconds(EPremiumTypes.PREMIUM_SAFEBOX) > 0 or d.GetCharacter().IsEquipUniqueGroup(uint(UNIQUE_GROUP_LARGE_SAFEBOX)):
        bSize = 3

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    d.GetCharacter().LoadSafebox(bSize * SAFEBOX_PAGE_SIZE, p.lldGold, p.wItemCount, (c_pData + sizeof(SSafeboxTable)))

def SafeboxChangeSize(d, c_pData):
    if d is None:
        return

    bSize = ord(c_pData)

    if d.GetCharacter() is None:
        return

    d.GetCharacter().ChangeSafeboxSize(bSize)

def SafeboxWrongPassword(d):
    if d is None:
        return

    if d.GetCharacter() is None:
        return

    p = packet_safebox_wrong_password()
    p.bHeader = byte(LG_HEADER_GC_SAFEBOX_WRONG_PASSWORD)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    d.Packet(p, sizeof(p))

    d.GetCharacter().CancelSafeboxLoad()

def SafeboxChangePasswordAnswer(d, c_pData):
    if d is None:
        return

    if d.GetCharacter() is None:
        return

    p = c_pData
    if p.flag != 0:
        d.GetCharacter().ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Storages> Storage password changed."))
    else:
        d.GetCharacter().ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Storages> You entered the wrong password."))

def MallLoad(d, c_pData):
    if d is None:
        return

    p = c_pData

    if d.GetAccountTable().id != p.dwID:
        #lani_err("safebox has different id %u != %u", d.GetAccountTable().id, p.dwID)
        return

    if d.GetCharacter() is None:
        return

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    d.GetCharacter().LoadMall(p.wItemCount, (c_pData + sizeof(SSafeboxTable)))

def LoginAlready(d, c_pData):
    if d is None:
        return

        p = c_pData

        d2 = DESC_MANAGER.instance().FindByLoginName(p.szLogin)

        if d2:
            d2.DisconnectOfSameLogin()
        else:
            pgg = SPacketGGDisconnect()

            pgg.bHeader = byte(LG_HEADER_GG_DISCONNECT)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            strncpy_s(pgg.szLogin, sizeof(pgg.szLogin), p.szLogin, _TRUNCATE)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            P2P_MANAGER.instance().Send(pgg, sizeof(SPacketGGDisconnect), NULL)
    LoginFailure(d, "ALREADY")

def EmpireSelect(d, c_pData):
    #sys_log(0, "EmpireSelect %p", get_pointer(d))

    if d is None:
        return

    rTable = d.GetAccountTable()
    rTable.bEmpire = ord(c_pData)

    pe = packet_empire()
    pe.bHeader = byte(LG_HEADER_GC_EMPIRE)
    pe.bEmpire = rTable.bEmpire
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    d.Packet(pe, sizeof(pe))

    i = 0
    while i < LGEMiscellaneous.PLAYER_PER_ACCOUNT:
        if (rTable.players[i].dwID) != 0:
            rTable.players[i].x = int(EMPIRE_START_X(rTable.bEmpire))
            rTable.players[i].y = int(EMPIRE_START_Y(rTable.bEmpire))
        i += 1

    GetServerLocation(d.GetAccountTable(), rTable.bEmpire)

    d.SendLoginSuccessPacket()

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Pointer arithmetic is detected on the parameter 'c_pData':
#ORIGINAL METINII C CODE: void CInputDB::MapLocations(const char * c_pData)
def MapLocations(c_pData):
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: byte bCount = *(byte *)(c_pData++);
    bCount = ord((c_pData))
    c_pData += 1

    #sys_log(0, "InputDB::MapLocations %d", bCount)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Pointer arithmetic is detected on this variable:
#ORIGINAL METINII C CODE: SMapLocation * pLoc = (SMapLocation *) c_pData;
    pLoc = c_pData

## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: while (bCount--)
    while (bCount) != 0:
        bCount -= 1
        for i in range(0, 32):
            if 0 == pLoc.alMaps[i]:
                break

            CMapLocation.instance().Insert(pLoc.alMaps[i], pLoc.szHost, pLoc.wPort)

        pLoc += 1
    bCount -= 1

def P2P(c_pData):
## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
#    extern LPFDWATCH main_fdw

    p = c_pData

    mgr = P2P_MANAGER.instance()

    if LGEMiscellaneous.DEFINECONSTANTS.false == DESC_MANAGER.instance().IsP2PDescExist(p.szHost, p.wPort):
        pkDesc = None
        #sys_log(0, "InputDB:P2P %s:%u", p.szHost, p.wPort)
        pkDesc = DESC_MANAGER.instance().CreateConnectionDesc(main_fdw, p.szHost, p.wPort, EPhase.PHASE_P2P, LGEMiscellaneous.DEFINECONSTANTS.false)
        mgr.RegisterConnector(pkDesc)
        pkDesc.SetP2P(p.szHost, p.wPort, p.bChannel)

def GuildLoad(c_pData):
    CGuildManager.instance().LoadGuild(c_pData)

def GuildSkillUpdate(c_pData):
    p = c_pData

    g = CGuildManager.instance().TouchGuild(p.guild_id)

    if g:
        temp_ref_LG_SKILL_levels = RefObject(p.LG_SKILL_levels);
        g.UpdateSkill(p.LG_SKILL_point, temp_ref_LG_SKILL_levels)
        p.LG_SKILL_levels = temp_ref_LG_SKILL_levels.arg_value
        g.GuildPointChange(EPointTypes.LG_POINT_SP, p.amount,((not LGEMiscellaneous.DEFINECONSTANTS.false)) if p.save != 0 ) else LGEMiscellaneous.DEFINECONSTANTS.false)

def GuildWar(c_pData):
    p = c_pData

    #sys_log(0, "InputDB::GuildWar %u %u state %d", p.dwGuildFrom, p.dwGuildTo, p.bWar)

    if (p.bWar == EGuildWarState.GUILD_WAR_SEND_DECLARE) or (p.bWar == EGuildWarState.GUILD_WAR_RECV_DECLARE):
        CGuildManager.instance().DeclareWar(p.dwGuildFrom, p.dwGuildTo, p.bType)

    elif p.bWar == EGuildWarState.GUILD_WAR_REFUSE:
        CGuildManager.instance().RefuseWar(p.dwGuildFrom, p.dwGuildTo)

    elif p.bWar == EGuildWarState.GUILD_WAR_WAIT_START:
        CGuildManager.instance().WaitStartWar(p.dwGuildFrom, p.dwGuildTo)

    elif p.bWar == EGuildWarState.GUILD_WAR_CANCEL:
        CGuildManager.instance().CancelWar(p.dwGuildFrom, p.dwGuildTo)

    elif p.bWar == EGuildWarState.GUILD_WAR_ON_WAR:
        CGuildManager.instance().StartWar(p.dwGuildFrom, p.dwGuildTo)

    elif p.bWar == EGuildWarState.GUILD_WAR_END:
        CGuildManager.instance().EndWar(p.dwGuildFrom, p.dwGuildTo)

    elif p.bWar == EGuildWarState.GUILD_WAR_OVER:
        CGuildManager.instance().WarOver(p.dwGuildFrom, p.dwGuildTo, p.bType != 0)

    elif p.bWar == EGuildWarState.GUILD_WAR_RESERVE:
        CGuildManager.instance().ReserveWar(p.dwGuildFrom, p.dwGuildTo, p.bType)

    else:
        #lani_err("Unknown guild war state")

def GuildWarScore(c_pData):
    p = c_pData
    g = CGuildManager.instance().TouchGuild(p.dwGuildGainPoint)
    g.SetWarScoreAgainstTo(p.dwGuildOpponent, p.lScore)

def GuildSkillRecharge():
    CGuildManager.instance().SkillRecharge()

def GuildExpUpdate(c_pData):
    p = c_pData
    #sys_log(1, "GuildExpUpdate %d", p.amount)

    g = CGuildManager.instance().TouchGuild(p.guild_id)

    if g:
        g.GuildPointChange(EPointTypes.LG_POINT_EXP, p.amount, DefineConstants.false)

def GuildAddMember(c_pData):
    p = c_pData
    g = CGuildManager.instance().TouchGuild(p.dwGuild)

    if g:
        g.AddMember(p)

def GuildRemoveMember(c_pData):
    p = c_pData
    g = CGuildManager.instance().TouchGuild(p.dwGuild)

    if g:
        g.RemoveMember(p.dwInfo)

def GuildChangeGrade(c_pData):
    p = c_pData
    g = CGuildManager.instance().TouchGuild(p.dwGuild)

    if g:
        g.P2PChangeGrade(byte(int(p.dwInfo)))

def GuildChangeMemberData(c_pData):
    #sys_log(0, "Recv GuildChangeMemberData")
    p = c_pData
    g = CGuildManager.instance().TouchGuild(p.guild_id)

    if g:
        g.ChangeMemberData(p.pid, p.offer, p.level, p.grade)

def GuildDisband(c_pData):
    p = c_pData
    CGuildManager.instance().DisbandGuild(p.dwGuild)

def GuildLadder(c_pData):
    p = c_pData
    #sys_log(0, "Recv GuildLadder %u %d / w %d d %d l %d", p.dwGuild, p.lLadderPoint, p.lWin, p.lDraw, p.lLoss)
    g = CGuildManager.instance().TouchGuild(p.dwGuild)

    g.SetLadderPoint(p.lLadderPoint)
    g.SetWarData(p.lWin, p.lDraw, p.lLoss)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Pointer arithmetic is detected on the parameter 'c_pData':
#ORIGINAL METINII C CODE: void CInputDB::ItemLoad(DESC* d, const char * c_pData)
def ItemLoad(d, c_pData):
    ch = None

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if (!d || !(ch = d->GetCharacter()))
    if d is None or not(ch = d.GetCharacter()):
        return

    if ch.IsItemLoaded():
        return

    dwCount = uint(decode_4bytes(c_pData))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    c_pData += sizeof(uint)

    #sys_log(0, "ITEM_LOAD: COUNT %s %u", ch.GetName(LOCALE_LANIATUS), dwCount)

    v = []

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Pointer arithmetic is detected on this variable:
#ORIGINAL METINII C CODE: SPlayerItem * p = (SPlayerItem *) c_pData;
    p = c_pData

    i = 0
    while i < dwCount:
        item = ITEM_MANAGER.instance().CreateItem(p.vnum, p.count, p.id, DefineConstants.false, -1, DefineConstants.false)

        if item is None:
            #lani_err("cannot create item by vnum %u (name %s id %u)", p.vnum, ch.GetName(LOCALE_LANIATUS), p.id)
            continue

        item.SetSkipSave(((not LGEMiscellaneous.DEFINECONSTANTS.false)))
        item.SetSockets(p.alSockets)
        item.SetAttributes(p.aAttr)

        if (p.window == EWindows.INVENTORY and ch.GetInventoryItem(p.pos)) or (p.window == EWindows.EQUIPMENT and ch.GetWear(p.pos)):
            #sys_log(0, "ITEM_RESTORE: %s %s", ch.GetName(LOCALE_LANIATUS), item.GetName(LOCALE_LANIATUS))
            v.append(item)
        else:
            if (p.window == EWindows.INVENTORY) or (p.window == EWindows.DRAGON_SOUL_INVENTORY):
                item.AddToCharacter(ch, TItemPos(p.window, p.pos))

            elif p.window == EWindows.EQUIPMENT:
                if item.CheckItemUseLevel(ch.GetLevel()) == ((not LGEMiscellaneous.DEFINECONSTANTS.false)):
                    if item.EquipTo(ch, byte(p.pos)) == LGEMiscellaneous.DEFINECONSTANTS.false:
                        v.append(item)
                else:
                    v.append(item)

        if LGEMiscellaneous.DEFINECONSTANTS.false == item.OnAfterCreatedItem():
            #lani_err("Failed to call ITEM::OnAfterCreatedItem (vnum: %d, id: %d)", item.GetVnum(), item.GetID())

        item.SetSkipSave(LGEMiscellaneous.DEFINECONSTANTS.false)
        i += 1
        p += 1

    it = v.begin()

    while it is not v.end():
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: CItem* item = *(it++);
        item = *(it)
        it += 1

        pos = ch.GetEmptyInventory(item.GetSize())

        if pos < 0:
            coord = pixel_position_s()
            coord.x = ch.GetX()
            coord.y = ch.GetY()

            item.AddToGround(ch.GetMapIndex(), coord, DefineConstants.false)
            item.SetOwnership(ch, 180)
            item.StartDestroyEvent(300)
        else:
            item.AddToCharacter(ch, TItemPos(EWindows.INVENTORY, pos))

    ch.CheckMaximumPoints()
    ch.PointsPacket()

    ch.SetItemLoaded()

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Pointer arithmetic is detected on the parameter 'c_pData':
#ORIGINAL METINII C CODE: void CInputDB::AffectLoad(DESC* d, const char * c_pData)
def AffectLoad(d, c_pData):
    if d is None:
        return

    if d.GetCharacter() is None:
        return

    ch = d.GetCharacter()

    dwPID = uint(decode_4bytes(c_pData))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    c_pData += sizeof(uint)

    dwCount = uint(decode_4bytes(c_pData))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    c_pData += sizeof(uint)

    if ch.GetPlayerID() != dwPID:
        return

    ch.LoadAffect(dwCount, c_pData)




def PartyCreate(c_pData):
    p = c_pData
    CPartyManager.instance().P2PCreateParty(p.dwLeaderPID)

def PartyDelete(c_pData):
    p = c_pData
    CPartyManager.instance().P2PDeleteParty(p.dwLeaderPID)

def PartyAdd(c_pData):
    p = c_pData
    CPartyManager.instance().P2PJoinParty(p.dwLeaderPID, p.dwPID, p.bState)

def PartyRemove(c_pData):
    p = c_pData
    CPartyManager.instance().P2PQuitParty(p.dwPID)

def PartyStateChange(c_pData):
    p = c_pData
    pParty = CPartyManager.instance().P2PCreateParty(p.dwLeaderPID)

    if pParty is None:
        return

    pParty.SetRole(p.dwPID, p.bRole, p.bFlag != 0)

def PartySetMemberLevel(c_pData):
    p = c_pData
    pParty = CPartyManager.instance().P2PCreateParty(p.dwLeaderPID)

    if pParty is None:
        return

    pParty.P2PSetMemberLevel(p.dwPID, p.bLevel)

def Time(c_pData):
    set_global_time(c_pData)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Pointer arithmetic is detected on the parameter 'c_pData':
#ORIGINAL METINII C CODE: void CInputDB::ReloadProto(const char * c_pData)
def ReloadProto(c_pData):
    wSize = None

    wSize = decode_2bytes(c_pData)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    c_pData += sizeof(ushort)
    if wSize != 0:
        CSkillManager.instance().Initialize(c_pData, wSize)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    c_pData += sizeof(SSkillTable) * wSize

    wSize = decode_2bytes(c_pData)
    c_pData += 2
    #sys_log(0, "RELOAD: ITEM: %d", wSize)

    if wSize != 0:
        ITEM_MANAGER.instance().Initialize(c_pData, wSize)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        c_pData += wSize * sizeof(SItemTable)

    wSize = decode_2bytes(c_pData)
    c_pData += 2
    #sys_log(0, "RELOAD: MOB: %d", wSize)

    if wSize != 0:
        CMobManager.instance().Initialize(c_pData, wSize)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        c_pData += wSize * sizeof(SMobTable)

    CMotionManager.instance().Build()

    CHARACTER_MANAGER.instance().for_each_pc(std::mem_fn(CHARACTER.ComputePoints))

def GuildSkillUsableChange(c_pData):
    p = c_pData

    g = CGuildManager.instance().TouchGuild(p.dwGuild)

    g.SkillUsableChange(p.dwSkillVnum,((not LGEMiscellaneous.DEFINECONSTANTS.false)) if p.bUsable != 0 ) else LGEMiscellaneous.DEFINECONSTANTS.false)

def AuthLogin(d, c_pData):
    if d is None:
        return

    bResult = ord(c_pData)

    ptoc = packet_auth_success()

    ptoc.bHeader = byte(LG_HEADER_GC_AUTH_SUCCESS)

    if bResult != 0:
        ptoc.dwLoginKey = d.GetLoginKey()
    else:
        ptoc.dwLoginKey = 0

    ptoc.bResult = bResult

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    d.Packet(ptoc, sizeof(packet_auth_success))
    #sys_log(0, "AuthLogin result %u key %u", bResult, d.GetLoginKey())

def ChangeEmpirePriv(c_pData):
    p = c_pData
    CPrivManager.instance().GiveEmpirePriv(p.empire, p.type, p.value, p.bLog, time_t(p.end_time_sec))

def ChangeGuildPriv(c_pData):
    p = c_pData
    CPrivManager.instance().GiveGuildPriv(p.guild_id, p.type, p.value, p.bLog, time_t(p.end_time_sec))

def ChangeCharacterPriv(c_pData):
    p = c_pData
    CPrivManager.instance().GiveCharacterPriv(p.pid, p.type, p.value, p.bLog)

def GuildMoneyChange(c_pData):
    p = c_pData

    g = CGuildManager.instance().TouchGuild(p.dwGuild)
    if g:
        g.RecvMoneyChange(p.iTotalGold)

def GuildWithdrawMoney(c_pData):
    p = c_pData

    g = CGuildManager.instance().TouchGuild(p.dwGuild)
    if g:
        g.RecvWithdrawMoneyGive(p.iChangeGold)

def SetEventFlag(c_pData):
    p = c_pData
    quest.CQuestManager.instance().SetEventFlag(p.szFlagName, p.lValue)

def CreateObject(c_pData):
    CManager.instance().LoadObject(c_pData, DefineConstants.false)

def DeleteObject(c_pData):
    CManager.instance().DeleteObject(c_pData)

def UpdateLand(c_pData):
    CManager.instance().UpdateLand(c_pData)

def Notice(c_pData):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if __MULTI_LANGUAGE_SYSTEM__
## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
#    extern void SendNotice(const char* c_pszBuf, ...)
##else
## Laniatus Games Studio Inc. | NOTE: 'extern' variable declarations are not required in Python:
#    extern void SendNotice(const char* c_pszBuf)
##endif

    szBuf = str(['\0' for _ in range(256+1)])
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    strncpy_s(szBuf, sizeof(szBuf), c_pData, _TRUNCATE)

    #sys_log(0, "InputDB:: Notice: %s", szBuf)
    SendNotice(szBuf)

def GuildWarReserveAdd(p):
    CGuildManager.instance().ReserveWarAdd(p)

def GuildWarReserveDelete(dwID):
    CGuildManager.instance().ReserveWarDelete(dwID)

def GuildWarBet(p):
    CGuildManager.instance().ReserveWarBet(p)

def MarriageAdd(p):
    #sys_log(0, "MarriageAdd %u %u %u %s %s", p.dwPID1, p.dwPID2, p.tMarryTime, p.szName1, p.szName2)
    marriage.CManager.instance().Add(p.dwPID1, p.dwPID2, time_t(p.tMarryTime), p.szName1, p.szName2)

def MarriageUpdate(p):
    #sys_log(0, "MarriageUpdate %u %u %d %d", p.dwPID1, p.dwPID2, p.iLovePoint, p.byMarried)
    marriage.CManager.instance().Update(p.dwPID1, p.dwPID2, p.iLovePoint, p.byMarried)

def MarriageRemove(p):
    #sys_log(0, "MarriageRemove %u %u", p.dwPID1, p.dwPID2)
    marriage.CManager.instance().Remove(p.dwPID1, p.dwPID2)

def WeddingRequest(p):
    marriage.WeddingManager.instance().Request(p.dwPID1, p.dwPID2)

def WeddingReady(p):
    #sys_log(0, "WeddingReady %u %u %u", p.dwPID1, p.dwPID2, p.dwMapIndex)
    marriage.CManager.instance().WeddingReady(p.dwPID1, p.dwPID2, p.dwMapIndex)

def WeddingStart(p):
    #sys_log(0, "WeddingStart %u %u", p.dwPID1, p.dwPID2)
    marriage.CManager.instance().WeddingStart(p.dwPID1, p.dwPID2)

def WeddingEnd(p):
    #sys_log(0, "WeddingEnd %u %u", p.dwPID1, p.dwPID2)
    marriage.CManager.instance().WeddingEnd(p.dwPID1, p.dwPID2)

def MyshopPricelistRes(d, p):
    ch = None

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if (!d || !(ch = d->GetCharacter()))
    if d is None or not(ch = d.GetCharacter()):
        return

    #sys_log(0, "RecvMyshopPricelistRes name[%s]", ch.GetName(LOCALE_LANIATUS))
    ch.UseSilkBotaryReal(p)


## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Pointer arithmetic is detected on the parameter 'c_pData':
#ORIGINAL METINII C CODE: void CInputDB::ReloadAdmin(const char * c_pData)
def ReloadAdmin(c_pData):
    gm_new_clear()
    ChunkSize = decode_2bytes(c_pData)
    c_pData += 2
    HostSize = decode_2bytes(c_pData)
    c_pData += 2

    for n in range(0, HostSize):
        gm_new_host_inert(c_pData)
        c_pData += ChunkSize


    c_pData += 2
    size = decode_2bytes(c_pData)
    c_pData += 2

    for n in range(0, size):
        rAdminInfo = c_pData

        gm_new_insert(rAdminInfo)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        c_pData += sizeof(TAdminInfo)

        pChar = CHARACTER_MANAGER.instance().FindPC(rAdminInfo.m_szName)
        if pChar:
            pChar.SetGMLevel()


def Analyze(d, bHeader, c_pData):
    if bHeader == LG_HEADER_DG_BOOT:
        Boot(c_pData)

    elif bHeader == LG_HEADER_DG_LOGIN_SUCCESS:
        LoginSuccess(m_dwHandle, c_pData)

    elif bHeader == LG_HEADER_DG_LOGIN_NOT_EXIST:
        LoginFailure(DESC_MANAGER.instance().FindByHandle(m_dwHandle), "NOID")

    elif bHeader == LG_HEADER_DG_LOGIN_WRONG_PASSWD:
        LoginFailure(DESC_MANAGER.instance().FindByHandle(m_dwHandle), "WRONGPWD")

    elif bHeader == LG_HEADER_DG_LOGIN_ALREADY:
        LoginAlready(DESC_MANAGER.instance().FindByHandle(m_dwHandle), c_pData)

    elif bHeader == LG_HEADER_DG_PLAYER_LOAD_SUCCESS:
        PlayerLoad(DESC_MANAGER.instance().FindByHandle(m_dwHandle), c_pData)

    elif bHeader == LG_HEADER_DG_PLAYER_CREATE_SUCCESS:
        PlayerCreateSuccess(DESC_MANAGER.instance().FindByHandle(m_dwHandle), c_pData)

    elif bHeader == LG_HEADER_DG_PLAYER_CREATE_FAILED:
        PlayerCreateFailure(DESC_MANAGER.instance().FindByHandle(m_dwHandle), 0)

    elif bHeader == LG_HEADER_DG_PLAYER_CREATE_ALREADY:
        PlayerCreateFailure(DESC_MANAGER.instance().FindByHandle(m_dwHandle), 1)

    elif bHeader == LG_HEADER_DG_PLAYER_DELETE_SUCCESS:
        PlayerDeleteSuccess(DESC_MANAGER.instance().FindByHandle(m_dwHandle), c_pData)

    elif bHeader == LG_HEADER_DG_PLAYER_LOAD_FAILED:
        pass

    elif bHeader == LG_HEADER_DG_PLAYER_DELETE_FAILED:
        PlayerDeleteFail(DESC_MANAGER.instance().FindByHandle(m_dwHandle))

    elif bHeader == LG_HEADER_DG_ITEM_LOAD:
        ItemLoad(DESC_MANAGER.instance().FindByHandle(m_dwHandle), c_pData)

    elif bHeader == LG_HEADER_DG_QUEST_LOAD:
        QuestLoad(DESC_MANAGER.instance().FindByHandle(m_dwHandle), c_pData)

    elif bHeader == LG_HEADER_DG_LANIA_AFFECT_LOAD:
        AffectLoad(DESC_MANAGER.instance().FindByHandle(m_dwHandle), c_pData)

    elif bHeader == LG_HEADER_DG_SAFEBOX_LOAD:
        SafeboxLoad(DESC_MANAGER.instance().FindByHandle(m_dwHandle), c_pData)

    elif bHeader == LG_HEADER_DG_SAFEBOX_CHANGE_SIZE:
        SafeboxChangeSize(DESC_MANAGER.instance().FindByHandle(m_dwHandle), c_pData)

    elif bHeader == LG_HEADER_DG_SAFEBOX_WRONG_PASSWORD:
        SafeboxWrongPassword(DESC_MANAGER.instance().FindByHandle(m_dwHandle))

    elif bHeader == LG_HEADER_DG_SAFEBOX_CHANGE_PASSWORD_ANSWER:
        SafeboxChangePasswordAnswer(DESC_MANAGER.instance().FindByHandle(m_dwHandle), c_pData)

    elif bHeader == LG_HEADER_DG_MALL_LOAD:
        MallLoad(DESC_MANAGER.instance().FindByHandle(m_dwHandle), c_pData)

    elif bHeader == LG_HEADER_DG_EMPIRE_SELECT:
        EmpireSelect(DESC_MANAGER.instance().FindByHandle(m_dwHandle), c_pData)

    elif bHeader == LG_HEADER_DG_MAP_LOCATIONS:
        MapLocations(c_pData)

    elif bHeader == LG_HEADER_DG_P2P:
        P2P(c_pData)

    elif bHeader == LG_HEADER_DG_GUILD_LG_SKILL_UPDATE:
        GuildSkillUpdate(c_pData)

    elif bHeader == LG_HEADER_DG_GUILD_LOAD:
        GuildLoad(c_pData)

    elif bHeader == LG_HEADER_DG_GUILD_LG_SKILL_RECHARGE:
        GuildSkillRecharge()

    elif bHeader == LG_HEADER_DG_GUILD_EXP_UPDATE:
        GuildExpUpdate(c_pData)

    elif bHeader == LG_HEADER_DG_PARTY_CREATE:
        PartyCreate(c_pData)

    elif bHeader == LG_HEADER_DG_PARTY_DELETE:
        PartyDelete(c_pData)

    elif bHeader == LG_HEADER_DG_PARTY_ADD:
        PartyAdd(c_pData)

    elif bHeader == LG_HEADER_DG_PARTY_REMOVE:
        PartyRemove(c_pData)

    elif bHeader == LG_HEADER_DG_PARTY_STATE_CHANGE:
        PartyStateChange(c_pData)

    elif bHeader == LG_HEADER_DG_PARTY_SET_MEMBER_LEVEL:
        PartySetMemberLevel(c_pData)

    elif bHeader == LG_HEADER_DG_TIME:
        Time(c_pData)

    elif bHeader == LG_HEADER_DG_GUILD_ADD_MEMBER:
        GuildAddMember(c_pData)

    elif bHeader == LG_HEADER_DG_GUILD_REMOVE_MEMBER:
        GuildRemoveMember(c_pData)

    elif bHeader == LG_HEADER_DG_GUILD_CHANGE_GRADE:
        GuildChangeGrade(c_pData)

    elif bHeader == LG_HEADER_DG_GUILD_CHANGE_MEMBER_DATA:
        GuildChangeMemberData(c_pData)

    elif bHeader == LG_HEADER_DG_GUILD_DISBAND:
        GuildDisband(c_pData)

    elif bHeader == LG_HEADER_DG_RELOAD_PROTO:
        ReloadProto(c_pData)

    elif bHeader == LG_HEADER_DG_GUILD_WAR:
        GuildWar(c_pData)

    elif bHeader == LG_HEADER_DG_GUILD_WAR_SCORE:
        GuildWarScore(c_pData)

    elif bHeader == LG_HEADER_DG_GUILD_LADDER:
        GuildLadder(c_pData)

    elif bHeader == LG_HEADER_DG_GUILD_LG_SKILL_USABLE_CHANGE:
        GuildSkillUsableChange(c_pData)

    elif bHeader == LG_HEADER_DG_CHANGE_NAME:
        ChangeName(DESC_MANAGER.instance().FindByHandle(m_dwHandle), c_pData)

    elif bHeader == LG_HEADER_DG_AUTH_LOGIN:
        AuthLogin(DESC_MANAGER.instance().FindByHandle(m_dwHandle), c_pData)

    elif bHeader == LG_HEADER_DG_CHANGE_EMPIRE_PRIV:
        ChangeEmpirePriv(c_pData)

    elif bHeader == LG_HEADER_DG_CHANGE_GUILD_PRIV:
        ChangeGuildPriv(c_pData)

    elif bHeader == LG_HEADER_DG_CHANGE_CHARACTER_PRIV:
        ChangeCharacterPriv(c_pData)

    elif bHeader == LG_HEADER_DG_GUILD_WITHDRAW_MONEY_GIVE:
        GuildWithdrawMoney(c_pData)

    elif bHeader == LG_HEADER_DG_GUILD_MONEY_CHANGE:
        GuildMoneyChange(c_pData)

    elif bHeader == LG_HEADER_DG_SET_EVENT_FLAG:
        SetEventFlag(c_pData)

    elif bHeader == LG_HEADER_DG_CREATE_OBJECT:
        CreateObject(c_pData)

    elif bHeader == LG_HEADER_DG_DELETE_OBJECT:
        DeleteObject(c_pData)

    elif bHeader == LG_HEADER_DG_UPDATE_LAND:
        UpdateLand(c_pData)

    elif bHeader == LG_HEADER_DG_NOTICE:
        Notice(c_pData)

    elif bHeader == LG_HEADER_DG_GUILD_WAR_RESERVE_ADD:
        GuildWarReserveAdd(c_pData)

    elif bHeader == LG_HEADER_DG_GUILD_WAR_RESERVE_DEL:
        GuildWarReserveDelete(c_pData)

    elif bHeader == LG_HEADER_DG_GUILD_WAR_BET:
        GuildWarBet(c_pData)

    elif bHeader == LG_HEADER_DG_MARRIAGE_ADD:
        MarriageAdd(c_pData)

    elif bHeader == LG_HEADER_DG_MARRIAGE_UPDATE:
        MarriageUpdate(c_pData)

    elif bHeader == LG_HEADER_DG_MARRIAGE_REMOVE:
        MarriageRemove(c_pData)

    elif bHeader == LG_HEADER_DG_WEDDING_REQUEST:
        WeddingRequest(c_pData)

    elif bHeader == LG_HEADER_DG_WEDDING_READY:
        WeddingReady(c_pData)

    elif bHeader == LG_HEADER_DG_WEDDING_START:
        WeddingStart(c_pData)

    elif bHeader == LG_HEADER_DG_WEDDING_END:
        WeddingEnd(c_pData)

    elif bHeader == LG_HEADER_DG_MYSHOP_PRICELIST_RES:
        MyshopPricelistRes(DESC_MANAGER.instance().FindByHandle(m_dwHandle), c_pData)

    elif bHeader == LG_HEADER_DG_RELOAD_ADMIN:
        ReloadAdmin(c_pData)

    elif bHeader == LG_HEADER_DG_ACK_CHANGE_GUILD_MASTER:
        self.GuildChangeMaster(c_pData)
    elif bHeader == LG_HEADER_DG_ACK_SPARE_ITEM_ID_RANGE:
        ITEM_MANAGER.instance().SetMaxSpareItemID(c_pData)

    elif (bHeader == LG_HEADER_DG_UPDATE_HORSE_NAME) or (bHeader == LG_HEADER_DG_ACK_HORSE_NAME):
        CHorseNameManager.instance().UpdateHorseName((c_pData).dwPlayerID, (c_pData).szHorseName, DefineConstants.false)

    elif bHeader == LG_HEADER_DG_NEED_LOGIN_LOG:
        pass

    elif bHeader == LG_HEADER_DG_ITEMAWARD_INFORMER:
        ItemAwardInformer(c_pData)

    elif bHeader == LG_HEADER_DG_RESPOND_CHANNELSTATUS:
        RespondChannelStatus(DESC_MANAGER.instance().FindByHandle(m_dwHandle), c_pData)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if ! _IMPROVED_PACKET_ENCRYPTION_
    elif bHeader == LG_HEADER_DG_SHUTDOWN:
            p = c_pData
            g_isShutdowned = p.state
##endif

    else:
        return (-1)

    return 0

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Pointer arithmetic is detected on the parameter 'd':
#ORIGINAL METINII C CODE: bool CInputDB::Process(DESC* d, const object* orig, int bytes, int & r_iBytesProceed)
def Process(d, orig, bytes, r_iBytesProceed):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Pointer arithmetic is detected on this variable:
#ORIGINAL METINII C CODE: const char * c_pData = (const char *) orig;
    c_pData = str(orig)
    bHeader = None
    bLastHeader = 0
    iSize = None
    iLastPacketLen = 0

    m_iBufferLeft = bytes
    while m_iBufferLeft > 0:
        if m_iBufferLeft < 9:
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        bHeader = ord((c_pData))
        m_dwHandle = (c_pData + 1)
        iSize = (c_pData + 5)

        #sys_log(1, "DBCLIENT: header %d handle %d size %d bytes %d", bHeader, m_dwHandle, iSize, bytes)

        if m_iBufferLeft - 9 < iSize:
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to pointers to value types:
#ORIGINAL METINII C CODE: const char * pRealData = (c_pData + 9);
        pRealData = (c_pData + 9)

        if Analyze(d, bHeader, pRealData) < 0:
            #lani_err("in InputDB: UNKNOWN HEADER: %d, LAST HEADER: %d(%d), REMAIN BYTES: %d, DESC: %d", bHeader, bLastHeader, iLastPacketLen, m_iBufferLeft, d.GetSocket())

        c_pData += 9 + iSize
        m_iBufferLeft -= 9 + iSize
        r_iBytesProceed.arg_value += 9 + iSize

        iLastPacketLen = 9 + iSize
        bLastHeader = bHeader

    return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

def GuildChangeMaster(p):
    CGuildManager.instance().ChangeMaster(p.dwGuildID)

def ItemAwardInformer(data):
    d = DESC_MANAGER.instance().FindByLoginName(data.login)

    if d is None:
        return
    else:
        if d.GetCharacter():
            ch = d.GetCharacter()
            ch.SetItemAward_vnum(data.vnum)
            temp_ref_command = RefObject(data.command);
            ch.SetItemAward_cmd(temp_ref_command)
            data.command = temp_ref_command.arg_value

            if d.IsPhase(EPhase.PHASE_GAME):
                quest.CQuestManager.instance().ItemInformer(ch.GetPlayerID(), ch.GetItemAward_vnum())

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Pointer arithmetic is detected on the parameter 'pcData':
#ORIGINAL METINII C CODE: void CInputDB::RespondChannelStatus(DESC* desc, const char* pcData)
def RespondChannelStatus(desc, pcData):
    if desc is None:
        return
    nSize = decode_4bytes(pcData)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    pcData += sizeof(nSize)

    bHeader = byte(LG_HEADER_GC_RESPOND_CHANNELSTATUS)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    desc.BufferedPacket(bHeader, sizeof(byte))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    desc.BufferedPacket(nSize, sizeof(nSize))
    if 0 < nSize:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        desc.BufferedPacket(pcData, sizeof(SChannelStatus)*nSize)
    bSuccess = 1
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    desc.Packet(bSuccess, sizeof(bSuccess))
    desc.SetChannelStatusRequested(LGEMiscellaneous.DEFINECONSTANTS.false)
