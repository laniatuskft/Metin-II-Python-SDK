def Login(d, data):
    pinfo = data

    login = str(['\0' for _ in range((int)LGEMiscellaneous.LOGIN_MAX_LEN + 1)])
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    trim_and_lower(pinfo.login, login, sizeof(login))

    #sys_log(0, "InputLogin::Login : %s", login)

    failurePacket = packet_login_failure()

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if _IMPROVED_PACKET_ENCRYPTION_
    if g_bNoMoreClient:
        failurePacket.header = byte(LG_HEADER_GC_LOGIN_FAILURE)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        strncpy_s(failurePacket.szStatus, sizeof(failurePacket.szStatus), "SHUTDOWN", _TRUNCATE)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        d.Packet(failurePacket, sizeof(packet_login_failure))
        return
##endif

    if g_iUserLimit > 0:
        iTotal = None
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to pointers to value types:
#ORIGINAL METINII C CODE: int * paiEmpireUserCount;
        paiEmpireUserCount = None
        iLocal = None

        temp_ref_iTotal = RefObject(iTotal);
        temp_ref_iLocal = RefObject(iLocal);
        DESC_MANAGER.instance().GetUserCount(temp_ref_iTotal, paiEmpireUserCount, temp_ref_iLocal)
        iLocal = temp_ref_iLocal.arg_value
        iTotal = temp_ref_iTotal.arg_value

        if g_iUserLimit <= iTotal:
            failurePacket.header = byte(LG_HEADER_GC_LOGIN_FAILURE)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            strncpy_s(failurePacket.szStatus, sizeof(failurePacket.szStatus), "FULL", _TRUNCATE)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            d.Packet(failurePacket, sizeof(packet_login_failure))
            return

    login_packet = SLoginPacket()

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    strncpy_s(login_packet.login, sizeof(login_packet.login), login, _TRUNCATE)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    strncpy_s(login_packet.passwd, sizeof(login_packet.passwd), pinfo.passwd, _TRUNCATE)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    db_clientdesc.DBPacket(LG_HEADER_GD_LOGIN, d.GetHandle(), login_packet, sizeof(SLoginPacket))

def LoginByKey(d, data):
    pinfo = data

    login = str(['\0' for _ in range((int)LGEMiscellaneous.LOGIN_MAX_LEN + 1)])
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    trim_and_lower(pinfo.login, login, sizeof(login))

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if _IMPROVED_PACKET_ENCRYPTION_
    if g_bNoMoreClient:
        failurePacket = packet_login_failure()

        failurePacket.header = byte(LG_HEADER_GC_LOGIN_FAILURE)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        strncpy_s(failurePacket.szStatus, sizeof(failurePacket.szStatus), "SHUTDOWN", _TRUNCATE)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        d.Packet(failurePacket, sizeof(packet_login_failure))
        return
##endif

    if g_iUserLimit > 0:
        iTotal = None
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to pointers to value types:
#ORIGINAL METINII C CODE: int * paiEmpireUserCount;
        paiEmpireUserCount = None
        iLocal = None

        temp_ref_iTotal = RefObject(iTotal);
        temp_ref_iLocal = RefObject(iLocal);
        DESC_MANAGER.instance().GetUserCount(temp_ref_iTotal, paiEmpireUserCount, temp_ref_iLocal)
        iLocal = temp_ref_iLocal.arg_value
        iTotal = temp_ref_iTotal.arg_value

        if g_iUserLimit <= iTotal:
            failurePacket = packet_login_failure()

            failurePacket.header = byte(LG_HEADER_GC_LOGIN_FAILURE)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            strncpy_s(failurePacket.szStatus, sizeof(failurePacket.szStatus), "FULL", _TRUNCATE)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            d.Packet(failurePacket, sizeof(packet_login_failure))
            return

    #sys_log(0, "LOGIN_BY_KEY: %s key %u", login, pinfo.dwLoginKey)

    d.SetLoginKey(pinfo.dwLoginKey)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if ! _IMPROVED_PACKET_ENCRYPTION_
    d.SetSecurityKey(pinfo.adwClientKey)
##endif

    ptod = SPacketGDLoginByKey()

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    strncpy_s(ptod.szLogin, sizeof(ptod.szLogin), login, _TRUNCATE)
    ptod.dwLoginKey = pinfo.dwLoginKey
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memcpy' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    memcpy(ptod.adwClientKey, pinfo.adwClientKey, sizeof(uint) * 4)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    strncpy_s(ptod.szIP, sizeof(ptod.szIP), d.GetHostName(), _TRUNCATE)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    db_clientdesc.DBPacket(LG_HEADER_GD_LOGIN_BY_KEY, d.GetHandle(), ptod, sizeof(SPacketGDLoginByKey))

def ChangeName(d, data):
    p = data
    c_r = d.GetAccountTable()

    if c_r.id == 0:
        #lani_err("no account table")
        return

    if (c_r.players[p.index].bChangeName) == 0:
        return

    if not check_name(p.name):
        pack = packet_create_failure()
        pack.header = byte(LG_HEADER_GC_CHARACTER_CREATE_FAILURE)
        pack.bType = 0
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        d.Packet(pack, sizeof(pack))
        return

    pdb = SPacketGDChangeName()

    pdb.pid = c_r.players[p.index].dwID
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    strncpy_s(pdb.name, sizeof(pdb.name), p.name, _TRUNCATE)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    db_clientdesc.DBPacket(LG_HEADER_GD_CHANGE_NAME, d.GetHandle(), pdb, sizeof(SPacketGDChangeName))

def CharacterSelect(d, data):
    pinfo = data
    c_r = d.GetAccountTable()

    #sys_log(0, "player_select: login: %s index: %d", c_r.login, pinfo.index)

    if c_r.id == 0:
        #lani_err("no account table")
        return

    if pinfo.index >= LGEMiscellaneous.PLAYER_PER_ACCOUNT:
        #lani_err("index overflow %d, login: %s", pinfo.index, c_r.login)
        return

    if (c_r.players[pinfo.index].bChangeName) != 0:
        #lani_err("name must be changed idx %d, login %s, name %s", pinfo.index, c_r.login, c_r.players[pinfo.index].szName)
        return

    player_load_packet = SPlayerLoadPacket()

    player_load_packet.account_id = c_r.id
    player_load_packet.player_id = c_r.players[pinfo.index].dwID
    player_load_packet.account_index = pinfo.index

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    db_clientdesc.DBPacket(LG_HEADER_GD_PLAYER_LOAD, d.GetHandle(), player_load_packet, sizeof(SPlayerLoadPacket))

def CharacterCreate(d, data):
    pinfo = data
    player_create_packet = SPlayerCreatePacket()

    #sys_log(0, "PlayerCreate: name %s pos %d job %d shape %d", pinfo.name, pinfo.index, pinfo.job, pinfo.shape)

    packFailure = packet_login_failure()
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    memset(packFailure, 0, sizeof(packFailure))
    packFailure.header = byte(LG_HEADER_GC_CHARACTER_CREATE_FAILURE)

    if ((not LGEMiscellaneous.DEFINECONSTANTS.false)) == g_BlockCharCreation:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        d.Packet(packFailure, sizeof(packFailure))
        return

    if (not check_name(pinfo.name)) or pinfo.shape > 1:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        d.Packet(packFailure, sizeof(packFailure))
        return

    c_rAccountTable = d.GetAccountTable()

    if 0 == strcmp(c_rAccountTable.login, pinfo.name):
        pack = packet_create_failure()
        pack.header = byte(LG_HEADER_GC_CHARACTER_CREATE_FAILURE)
        pack.bType = 1

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        d.Packet(pack, sizeof(pack))
        return

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    memset(player_create_packet, 0, sizeof(SPlayerCreatePacket))

    if not NewPlayerTable2(player_create_packet.player_table, pinfo.name, byte(pinfo.job), pinfo.shape, d.GetEmpire()):
        #lani_err("player_prototype error: job %d face %d ", pinfo.job)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        d.Packet(packFailure, sizeof(packFailure))
        return

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    trim_and_lower(c_rAccountTable.login, player_create_packet.login, sizeof(player_create_packet.login))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    strncpy_s(player_create_packet.passwd, sizeof(player_create_packet.passwd), c_rAccountTable.passwd, _TRUNCATE)

    player_create_packet.account_id = c_rAccountTable.id
    player_create_packet.account_index = pinfo.index

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    #sys_log(0, "PlayerCreate: name %s account_id %d, TPlayerCreatePacketSize(%d), Packet->Gold %d", pinfo.name, pinfo.index, sizeof(SPlayerCreatePacket), player_create_packet.player_table.gold)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    db_clientdesc.DBPacket(LG_HEADER_GD_PLAYER_CREATE, d.GetHandle(), player_create_packet, sizeof(SPlayerCreatePacket))

def CharacterDelete(d, data):
    pinfo = data
    c_rAccountTable = d.GetAccountTable()

    if c_rAccountTable.id == 0:
        #lani_err("PlayerDelete: no login data")
        return

    #sys_log(0, "PlayerDelete: login: %s index: %d, social_id %s", c_rAccountTable.login, pinfo.index, pinfo.private_code)

    if pinfo.index >= LGEMiscellaneous.PLAYER_PER_ACCOUNT:
        #lani_err("PlayerDelete: index overflow %d, login: %s", pinfo.index, c_rAccountTable.login)
        return

    if (c_rAccountTable.players[pinfo.index].dwID) == 0:
        #lani_err("PlayerDelete: Wrong Social ID index %d, login: %s", pinfo.index, c_rAccountTable.login)
        d.Packet(encode_byte(LG_HEADER_GC_CHARACTER_DELETE_WRONG_SOCIAL_ID), 1)
        return

    player_delete_packet = SPlayerDeletePacket()

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    trim_and_lower(c_rAccountTable.login, player_delete_packet.login, sizeof(player_delete_packet.login))
    player_delete_packet.player_id = c_rAccountTable.players[pinfo.index].dwID
    player_delete_packet.account_index = pinfo.index
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    strncpy_s(player_delete_packet.private_code, sizeof(player_delete_packet.private_code), pinfo.private_code, _TRUNCATE)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    db_clientdesc.DBPacket(LG_HEADER_GD_PLAYER_DELETE, d.GetHandle(), player_delete_packet, sizeof(SPlayerDeletePacket))

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##pragma pack(1)
class SPacketGTLogin:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.header = 0
        self.empty = 0
        self.id = 0

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##pragma pack()

def Entergame(d, data):
    ch = None

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if (!(ch = d->GetCharacter()))
    if not(ch = d.GetCharacter()):
        d.SetPhase(EPhase.PHASE_CLOSE)
        return

    pos = ch.GetXYZ()

    if not SECTREE_MANAGER.instance().GetMovablePosition(ch.GetMapIndex(), pos.x, pos.y, pos):
        pos2 = pixel_position_s()
        SECTREE_MANAGER.instance().GetRecallPositionByEmpire(ch.GetMapIndex(), ch.GetEmpire(), pos2)

        #lani_err("!GetMovablePosition (name %s %dx%d map %d changed to %dx%d)", ch.GetName(LOCALE_LANIATUS), pos.x, pos.y, ch.GetMapIndex(), pos2.x, pos2.y)
## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: pos = pos2;
        pos.copy_from(pos2)

    CGuildManager.instance().LoginMember(ch)

    ch.Show(ch.GetMapIndex(), pos.x, pos.y, pos.z, DefineConstants.false)

    SECTREE_MANAGER.instance().SendNPCPosition(ch)
    ch.ReviveInvisible(5)

    d.SetPhase(EPhase.PHASE_GAME)

    if ch.GetItemAward_cmd() != '\0':
        quest.CQuestManager.instance().ItemInformer(ch.GetPlayerID(), ch.GetItemAward_vnum())

    #sys_log(0, "ENTERGAME: %s %dx%dx%d %s map_index %d", ch.GetName(LOCALE_LANIATUS), ch.GetX(), ch.GetY(), ch.GetZ(), d.GetHostName(), ch.GetMapIndex())

    if ch.GetHorseLevel() > 0:
        ch.EnterHorse()

    ch.ResetPlayTime(0)

    ch.StartSaveEvent()
    ch.StartRecoveryEvent()
    ch.StartCheckSpeedHackEvent()

    CPVPManager.instance().Connect(ch)
    CPVPManager.instance().SendList(d)

    MessengerManager.instance().Login(ch.GetName(LOCALE_LANIATUS))

    CPartyManager.instance().SetParty(ch)
    CGuildManager.instance().SendGuildWar(ch)

    building.CManager.instance().SendLandList(d, ch.GetMapIndex())

    marriage.CManager.instance().Login(ch)

    p = SPacketGCTime()
    p.bHeader = byte(LG_HEADER_GC_TIME)
## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: p.time = get_global_time();
    p.time.copy_from(get_global_time())
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    d.Packet(p, sizeof(p))

    p2 = packet_channel()
    p2.header = byte(LG_HEADER_GC_CHANNEL)
    p2.channel = g_bChannel
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    d.Packet(p2, sizeof(p2))

    _send_bonus_info(ch)

    i = 0
    while i <= EPremiumTypes.PREMIUM_MAX_NUM:
        remain = ch.GetPremiumRemainSeconds(byte(i))

        if remain <= 0:
            continue

        ch.AddAffect(LaniatusEAffectTypes.LANIA_AFFECT_PREMIUM_START + i, EPointTypes.LG_POINT_NONE, 0, 0, remain, 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), DefineConstants.false)
        #sys_log(0, "PREMIUM: %s type %d %dmin", ch.GetName(LOCALE_LANIATUS), i, remain)
        i += 1

    if (not d.GetClientVersion()) != '\0':
        d.DelayedDisconnect(20)
    else:
        if 0 != g_stClientVersion.compare(d.GetClientVersion()):
            ch.ChatPacket(EChatType.CHAT_TYPE_NOTICE, LC_TEXT("Your client version is not correct. Please install the normal patch."))
            d.DelayedDisconnect(20)
            LogManager.instance().HackLog(ch.GetAID(), ch.GetName(LOCALE_LANIATUS), "VERSION_CONFLICT")
            #sys_log(0, "VERSION : WRONG VERSION USER : account:%s name:%s hostName:%s server_version:%s client_version:%s", d.GetAccountTable().login, ch.GetName(LOCALE_LANIATUS), d.GetHostName(), g_stClientVersion.c_str(), d.GetClientVersion())

    if ch.IsGM() == ((not LGEMiscellaneous.DEFINECONSTANTS.false)):
        ch.ChatPacket(EChatType.CHAT_TYPE_COMMAND, "ConsoleEnable")

    if ch.GetMapIndex() >= 10000:
        if CWarMapManager.instance().IsWarMap(ch.GetMapIndex()):
            ch.SetWarMap(CWarMapManager.instance().Find(ch.GetMapIndex()))
        elif marriage.WeddingManager.instance().IsWeddingMap(uint(ch.GetMapIndex())):
            ch.SetWeddingMap(marriage.WeddingManager.instance().Find(uint(ch.GetMapIndex())))
        else:
            ch.SetDungeon(CDungeonManager.instance().FindByMapIndex(ch.GetMapIndex()))
    elif ch.GetMapIndex() == 113:
        if COXEventManager.instance().Enter(ch) == LGEMiscellaneous.DEFINECONSTANTS.false:
            if ch.GetGMLevel() == EGMLevels.GM_PLAYER:
                ch.WarpSet(int(EMPIRE_START_X(ch.GetEmpire())), int(EMPIRE_START_Y(ch.GetEmpire())), 0)
    else:
        if CWarMapManager.instance().IsWarMap(ch.GetMapIndex()) or marriage.WeddingManager.instance().IsWeddingMap(uint(ch.GetMapIndex())):
            if not test_server:
                ch.WarpSet(int(EMPIRE_START_X(ch.GetEmpire())), int(EMPIRE_START_Y(ch.GetEmpire())), 0)

    if ch.GetHorseLevel() > 0:
        pid = ch.GetPlayerID()

        if pid != 0 and CHorseNameManager.instance().GetHorseName(pid) is None:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            db_clientdesc.DBPacket(LG_HEADER_GD_REQ_HORSE_NAME, 0, pid, sizeof(uint))

    if g_noticeBattleZone:
        if FN_is_battle_zone(ch):
            ch.ChatPacket(EChatType.CHAT_TYPE_NOTICE, LC_TEXT("�� �ʿ��� �������� ������ ������ �� �ֽ��ϴ�."))
            ch.ChatPacket(EChatType.CHAT_TYPE_NOTICE, LC_TEXT("�� ���׿� �������� ������"))
            ch.ChatPacket(EChatType.CHAT_TYPE_NOTICE, LC_TEXT("������ �ּ� �� �μ����� ���ư��ñ� �ٶ��ϴ�."))

    ch.LoadPickup()

    if (not ch.IsRiding()) and ch.GetHorse() is None:
        pkCostumeMount = ch.GetWear(EWearPositions.WEAR_COSTUME_MOUNT)
        if pkCostumeMount:
            ch.HorseSummon(((not LGEMiscellaneous.DEFINECONSTANTS.false)), DefineConstants.false, 0, 0)

    petSystem = ch.GetPetSystem()
    if petSystem:
        petSystem.HandlePetCostumeItem()

def Empire(d, c_pData):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no equivalent to 'reinterpret_cast' in Python:
    p = reinterpret_cast<const command_empire>(c_pData)

    if LGEMiscellaneous.EMPIRE_MAX_NUM <= p.bEmpire:
        d.SetPhase(EPhase.PHASE_CLOSE)
        return

    r = d.GetAccountTable()

    if r.bEmpire != 0:
        i = 0
        while i < LGEMiscellaneous.PLAYER_PER_ACCOUNT:
            if 0 != r.players[i].dwID:
                #lani_err("EmpireSelectFailed %d", r.players[i].dwID)
                return
            i += 1

    pd = SEmpireSelectPacket()

    pd.dwAccountID = r.id
    pd.bEmpire = p.bEmpire

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    db_clientdesc.DBPacket(LG_HEADER_GD_EMPIRE_SELECT, d.GetHandle(), pd, sizeof(pd))

def GuildSymbolUpload(d, c_pData, uiBytes):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    if uiBytes < sizeof(command_symbol_upload):
        return -1

    #sys_log(0, "GuildSymbolUpload uiBytes %u", uiBytes)

    p = c_pData

    if uiBytes < p.size:
        return -1

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    iSymbolSize = p.size - sizeof(command_symbol_upload)

    if iSymbolSize <= 0 or iSymbolSize > 64 * 1024:
        d.SetPhase(EPhase.PHASE_CLOSE)
        return 0

    if not test_server:
        if building.CManager.instance().FindLandByGuild(p.guild_id) is None:
            d.SetPhase(EPhase.PHASE_CLOSE)
            return 0

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    #sys_log(0, "GuildSymbolUpload Do Upload %02X%02X%02X%02X %d", c_pData[7], c_pData[8], c_pData[9], c_pData[10], sizeof(p))

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    CGuildMarkManager.instance().UploadSymbol(p.guild_id, iSymbolSize, byte(int((c_pData + sizeof(p)))))
    CGuildMarkManager.instance().SaveSymbol(LGEMiscellaneous.DEFINECONSTANTS.GUILD_SYMBOL_FILENAME)
    return iSymbolSize

def GuildSymbolCRC(d, c_pData):
    CGPacket = c_pData

    #sys_log(0, "GuildSymbolCRC %u %u %u", CGPacket.guild_id, CGPacket.crc, CGPacket.size)

    pkGS = CGuildMarkManager.instance().GetGuildSymbol(CGPacket.guild_id)

    if pkGS is None:
        return

    #sys_log(0, "  Server %u %u", pkGS.crc, len(pkGS.raw))

    if len(pkGS.raw) != CGPacket.size or pkGS.crc != CGPacket.crc:
        GCPacket = packet_symbol_data()

        GCPacket.header = byte(LG_HEADER_GC_SYMBOL_DATA)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        GCPacket.size = sizeof(GCPacket) + len(pkGS.raw)
        GCPacket.guild_id = CGPacket.guild_id

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        d.BufferedPacket(GCPacket, sizeof(GCPacket))
        d.Packet(pkGS.raw[0], len(pkGS.raw))

        #sys_log(0, "SendGuildSymbolHead %02X%02X%02X%02X Size %d", pkGS.raw[0], pkGS.raw[1], pkGS.raw[2], pkGS.raw[3], len(pkGS.raw))

def GuildMarkUpload(d, c_pData):
    p = c_pData
    rkGuildMgr = CGuildManager.instance()
    pkGuild = None

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if (!(pkGuild = rkGuildMgr.FindGuild(p->gid)))
    if not(pkGuild = rkGuildMgr.FindGuild(p.gid)):
        #lani_err("MARK_SERVER: GuildMarkUpload: no guild. gid %u", p.gid)
        return

    if pkGuild.GetLevel() < guild_mark_min_level:
        #sys_log(0, "MARK_SERVER: GuildMarkUpload: level < %u (%u)", guild_mark_min_level, pkGuild.GetLevel())
        return

    rkMarkMgr = CGuildMarkManager.instance()

    #sys_log(0, "MARK_SERVER: GuildMarkUpload: gid %u", p.gid)

    isEmpty = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    for iPixel in range(0, SGuildMark.SIZE):
        if p.image[iPixel] != 0x00000000:
            isEmpty = LGEMiscellaneous.DEFINECONSTANTS.false

    if isEmpty:
        rkMarkMgr.DeleteMark(p.gid)
    else:
        temp_ref_image = RefObject(p.image);
        rkMarkMgr.SaveMark(p.gid, temp_ref_image)
        p.image = temp_ref_image.arg_value

def GuildMarkIDXList(d, c_pData):
    rkMarkMgr = CGuildMarkManager.instance()

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    bufSize = sizeof(ushort) * 2 * rkMarkMgr.GetMarkCount()
    buf = None

    if bufSize > 0:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'malloc' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
        buf = str(malloc(bufSize))
        temp_ref_buf = RefObject(buf);
        rkMarkMgr.CopyMarkIdx(temp_ref_buf)
        buf = temp_ref_buf.arg_value

    p = packet_mark_idxlist()
    p.header = byte(LG_HEADER_GC_MARK_IDXLIST)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    p.bufSize = sizeof(p) + bufSize
    p.count = ushort(rkMarkMgr.GetMarkCount())

    if buf != '\0':
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        d.BufferedPacket(p, sizeof(p))
        d.LargePacket(buf, int(bufSize))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'free' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
        free(buf)
    else:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        d.Packet(p, sizeof(p))

    #sys_log(0, "MARK_SERVER: GuildMarkIDXList %d bytes sent.", p.bufSize)

def GuildMarkCRCList(d, c_pData):
    pCG = c_pData

    mapDiffBlocks = {}
    CGuildMarkManager.instance().GetDiffBlocks(pCG.imgIdx, pCG.crclist, mapDiffBlocks)

    blockCount = 0
    buf = TEMP_BUFFER(1024 * 1024, DefineConstants.false)

    it = mapDiffBlocks.begin()
    while it is not mapDiffBlocks.end():
        posBlock = it.first
        rkBlock = *it.second

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        buf.write(posBlock, sizeof(byte))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        buf.write(rkBlock.m_sizeCompBuf, sizeof(uint))
        buf.write(rkBlock.m_abCompBuf, lzo_uint(rkBlock.m_sizeCompBuf))

        blockCount += 1
        it += 1

    pGC = packet_mark_block()

    pGC.header = byte(LG_HEADER_GC_MARK_BLOCK)
    pGC.imgIdx = pCG.imgIdx
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    pGC.bufSize = buf.size() + sizeof(packet_mark_block)
    pGC.count = blockCount

    #sys_log(0, "MARK_SERVER: Sending blocks. (imgIdx %u diff %u size %u)", pCG.imgIdx, len(mapDiffBlocks), pGC.bufSize)

    if buf.size() > 0:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        d.BufferedPacket(pGC, sizeof(packet_mark_block))
        d.LargePacket(buf.read_peek(), buf.size())
    else:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        d.Packet(pGC, sizeof(packet_mark_block))

def Analyze(d, bHeader, c_pData):
    iExtraLen = 0

    if bHeader == LG_HEADER_CG_PONG:
        Pong(d)

    elif bHeader == LG_HEADER_CG_TIME_SYNC:
        Handshake(d, c_pData)

    elif bHeader == LG_HEADER_CG_LOGIN:
        Login(d, c_pData)

    elif bHeader == LG_HEADER_CG_LOGIN2:
        LoginByKey(d, c_pData)

    elif bHeader == LG_HEADER_CG_CHARACTER_SELECT:
        CharacterSelect(d, c_pData)

    elif bHeader == LG_HEADER_CG_CHARACTER_CREATE:
        CharacterCreate(d, c_pData)

    elif bHeader == LG_HEADER_CG_CHARACTER_DELETE:
        CharacterDelete(d, c_pData)

    elif bHeader == LG_HEADER_CG_ENTERGAME:
        Entergame(d, c_pData)

    elif bHeader == LG_HEADER_CG_EMPIRE:
        Empire(d, c_pData)

    elif bHeader == LG_HEADER_CG_MOVE:
        pass

    elif bHeader == LG_HEADER_CG_MARK_LOGIN:
        pass

    elif bHeader == LG_HEADER_CG_MARK_CRCLIST:
        GuildMarkCRCList(d, c_pData)

    elif bHeader == LG_HEADER_CG_MARK_IDXLIST:
        GuildMarkIDXList(d, c_pData)

    elif bHeader == LG_HEADER_CG_MARK_UPLOAD:
        GuildMarkUpload(d, c_pData)

    elif bHeader == LG_HEADER_CG_GUILD_SYMBOL_UPLOAD:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((iExtraLen = GuildSymbolUpload(d, c_pData, m_iBufferLeft)) < 0)
        if (iExtraLen = GuildSymbolUpload(d, c_pData, m_iBufferLeft)) < 0:
            return -1

    elif bHeader == LG_HEADER_CG_SYMBOL_CRC:
        GuildSymbolCRC(d, c_pData)

    elif bHeader == LG_HEADER_CG_HACK:
        pass

    elif bHeader == LG_HEADER_CG_CHANGE_NAME:
        ChangeName(d, c_pData)

    elif bHeader == LG_HEADER_CG_CLIENT_VERSION:
        Version(d.GetCharacter(), c_pData)

    elif bHeader == LG_HEADER_CG_CLIENT_VERSION2:
        Version(d.GetCharacter(), c_pData)

    else:
        #lani_err("login phase does not handle this packet! header %d", bHeader)
        return (0)

    return (iExtraLen)

