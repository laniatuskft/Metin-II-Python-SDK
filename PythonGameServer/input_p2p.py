def __init__():
    BindPacketInfo(m_packetInfoGG)

def Login(d, c_pData):
    P2P_MANAGER.instance().Login(d, c_pData)

def Logout(d, c_pData):
    p = c_pData
    P2P_MANAGER.instance().Logout(p.szName)

def Relay(d, c_pData, uiBytes):
    p = c_pData

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    if uiBytes < sizeof(SPacketGGRelay) + p.lSize:
        return -1

    if p.lSize < 0:
        #lani_err("invalid packet length %d", p.lSize)
        d.SetPhase(EPhase.PHASE_CLOSE)
        return -1

    #sys_log(0, "InputP2P::Relay : %s size %d", p.szName, p.lSize)

    pkChr = CHARACTER_MANAGER.instance().FindPC(p.szName)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to pointers to value types:
#ORIGINAL METINII C CODE: const byte* c_pbData = (const byte*)(c_pData + sizeof(SPacketGGRelay));
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    c_pbData = byte(int((c_pData + sizeof(SPacketGGRelay))))

    if pkChr is None:
        return p.lSize

    if c_pbData == LG_HEADER_GC_WHISPER:
        if pkChr.IsBlockMode(EBlockAction.BLOCK_WHISPER):
            return p.lSize

        buf = str(['\0' for _ in range(1024)])
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memcpy' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memcpy(buf, c_pbData, MIN(p.lSize, sizeof(buf)))

        p2 = buf

        bToEmpire = byte((p2.bType >> 4))
        p2.bType = byte(p2.bType & 0x0F)

        if p2.bType == 0x0F:
            p2.bType = EWhisperType.WHISPER_TYPE_SYSTEM
        else:
            if not pkChr.IsEquipUniqueGroup(uint(UNIQUE_GROUP_RING_OF_LANGUAGE)):
                if bToEmpire >= 1 and bToEmpire <= 3 and pkChr.GetEmpire() != bToEmpire:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                    ConvertEmpireText(bToEmpire, buf + sizeof(packet_whisper), p2.wSize - sizeof(packet_whisper), 10 + 2 * pkChr.GetSkillPower(LaniatusETalentXes.LG_SKILL_LANGUAGE1 + bToEmpire - 1, 0))

        pkChr.GetDesc().Packet(buf, p.lSize)
    else:
        pkChr.GetDesc().Packet(c_pbData, p.lSize)

    return (p.lSize)

def Notice(d, c_pData, uiBytes):
    p = c_pData

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    if uiBytes < sizeof(SPacketGGNotice) + p.lSize:
        return -1

    if p.lSize < 0:
        #lani_err("invalid packet length %d", p.lSize)
        d.SetPhase(EPhase.PHASE_CLOSE)
        return -1

    szBuf = str(['\0' for _ in range(256+1)])
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    strncpy_s(szBuf, MIN(p.lSize + 1, sizeof(szBuf)), c_pData + sizeof(SPacketGGNotice), _TRUNCATE)
    SendNotice(szBuf)
    return (p.lSize)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Pointer arithmetic is detected on the parameter 'c_pData':
#ORIGINAL METINII C CODE: int CInputP2P::Guild(DESC* d, const char* c_pData, int uiBytes)
def Guild(d, c_pData, uiBytes):
    p = c_pData
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    uiBytes -= sizeof(SPacketGGGuild)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    c_pData += sizeof(SPacketGGGuild)

    g = CGuildManager.instance().FindGuild(p.dwGuild)

    if p.bSubHeader == GUILD_SUBLG_HEADER_GG_CHAT:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            if uiBytes < sizeof(SPacketGGGuildChat):
                return -1

            p = c_pData

            if g:
                g.P2PChat(p.szText)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            return sizeof(SPacketGGGuildChat)

    if (p.bSubHeader == GUILD_SUBLG_HEADER_GG_CHAT) or (p.bSubHeader == GUILD_SUBLG_HEADER_GG_SET_MEMBER_COUNT_BONUS):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            if uiBytes < sizeof(int):
                return -1

            iBonus = ord(c_pData)
            pGuild = CGuildManager.instance().FindGuild(p.dwGuild)
            if pGuild:
                pGuild.SetMemberCountBonus(iBonus)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            return sizeof(int)

    if True:
        #lani_err("UNKNOWN GUILD SUB PACKET")
    return 0


class FuncShout:

    def __init__(self, str, bEmpire):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.m_str = '\0'
        self.m_bEmpire = 0

        self.m_str = str
        self.m_bEmpire = bEmpire

    def functor_method(self, d):
        if d.GetCharacter() is None:
            return

        d.GetCharacter().ChatPacket(EChatType.CHAT_TYPE_SHOUT, "%s", self.m_str)

def Shout(c_pData):
    p = c_pData
    SendShout(p.szText, p.bEmpire)

def LocaleNotice(c_pData):
    p = c_pData
    SendLCNotice(p.szNotice[0], p.bBigFont, p.szNotice[1], p.szNotice[2], p.szNotice[3], p.szNotice[4], p.szNotice[5])
##endif

def Disconnect(c_pData):
    p = c_pData

    d = DESC_MANAGER.instance().FindByLoginName(p.szLogin)

    if d is None:
        return

    if d.GetCharacter() is None:
        d.SetPhase(EPhase.PHASE_CLOSE)
    else:
        d.DisconnectOfSameLogin()

def Setup(d, c_pData):
    p = c_pData
    #sys_log(0, "P2P: Setup %s:%d", d.GetHostName(), p.wPort)
    d.SetP2P(d.GetHostName(), p.wPort, p.bChannel)

def MessengerAdd(c_pData):
    p = c_pData
    #sys_log(0, "P2P: Messenger Add %s %s", p.szAccount, p.szCompanion)
    MessengerManager.instance().__AddToList(p.szAccount, p.szCompanion)

def MessengerRemove(c_pData):
    p = c_pData
    #sys_log(0, "P2P: Messenger Remove %s %s", p.szAccount, p.szCompanion)
    MessengerManager.instance().__RemoveFromList(p.szAccount, p.szCompanion)

def FindPosition(d, c_pData):
    p = c_pData
    ch = CHARACTER_MANAGER.instance().FindByPID(p.dwTargetPID)
    if ch is not None and ch.GetMapIndex() < 10000:
        pw = SPacketGGWarpCharacter()
        pw.header = byte(LG_HEADER_GG_WARP_CHARACTER)
        pw.pid = p.dwFromPID
        pw.x = ch.GetX()
        pw.y = ch.GetY()
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        d.Packet(pw, sizeof(pw))

def WarpCharacter(c_pData):
    p = c_pData
    ch = CHARACTER_MANAGER.instance().FindByPID(p.pid)
    if ch:
        ch.WarpSet(p.x, p.y, 0)

def GuildWarZoneMapIndex(c_pData):
    p = c_pData
    gm = CGuildManager.instance()

    #sys_log(0, "P2P: GuildWarZoneMapIndex g1(%u) vs g2(%u), mapIndex(%d)", p.dwGuildID1, p.dwGuildID2, p.lMapIndex)

    g1 = gm.FindGuild(p.dwGuildID1)
    g2 = gm.FindGuild(p.dwGuildID2)

    if g1 is not None and g2 is not None:
        g1.SetGuildWarMapIndex(p.dwGuildID2, p.lMapIndex)
        g2.SetGuildWarMapIndex(p.dwGuildID1, p.lMapIndex)

def Transfer(c_pData):
    p = c_pData

    ch = CHARACTER_MANAGER.instance().FindPC(p.szName)

    if ch:
        ch.WarpSet(p.lX, p.lY, 0)

def XmasWarpSanta(c_pData):
    p = c_pData

    if p.bChannel == g_bChannel and map_allow_find(p.lMapIndex):
        iNextSpawnDelay = 50 * 60

        xmas.SpawnSanta(p.lMapIndex, iNextSpawnDelay)

        pack_reply = SPacketGGXmasWarpSantaReply()
        pack_reply.bHeader = byte(LG_HEADER_GG_XMAS_WARP_SANTA_REPLY)
        pack_reply.bChannel = g_bChannel
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        P2P_MANAGER.instance().Send(pack_reply, sizeof(pack_reply), NULL)

def XmasWarpSantaReply(c_pData):
    p = c_pData

    if p.bChannel == g_bChannel:
        LaniatusDefVariables = CharacterVectorInteractor()

        if CHARACTER_MANAGER.instance().GetCharactersByRaceNum(uint(xmas.MOB_SANTA_VNUM), i):
            it = i.begin()

            while it is not i.end():
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: CHARACTER_MANAGER::instance().DestroyCharacter(*it++);
                CHARACTER_MANAGER.instance().DestroyCharacter(it)
                it += 1

def LoginPing(d, c_pData):
    p = c_pData

    if not g_pkAuthMasterDesc:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        P2P_MANAGER.instance().Send(p, sizeof(SPacketGGLoginPing), d)

def BlockChat(c_pData):
    p = c_pData

    ch = CHARACTER_MANAGER.instance().FindPC(p.szName)

    if ch:
        #sys_log(0, "BLOCK CHAT apply name %s dur %d", p.szName, p.lBlockDuration)
        ch.AddAffect(LaniatusEAffectTypes.LANIA_AFFECT_BLOCK_CHAT, EPointTypes.LG_POINT_NONE, 0, EAffectBits.AFF_NONE, p.lBlockDuration, 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), DefineConstants.false)
    else:
        #sys_log(0, "BLOCK CHAT fail name %s dur %d", p.szName, p.lBlockDuration)

def IamAwake(d, c_pData):
    hostNames = ""
    P2P_MANAGER.instance().GetP2PHostNames(hostNames)
    #sys_log(0, "P2P Awakeness check from %s. My P2P connection number is %d. and details...\n%s", d.GetHostName(), P2P_MANAGER.instance().GetDescCount(), hostNames)

def Analyze(d, bHeader, c_pData):
    if test_server:
        #sys_log(0, "CInputP2P::Anlayze[Header %d]", bHeader)

    iExtraLen = 0

    if bHeader == LG_HEADER_GG_SETUP:
        Setup(d, c_pData)

    elif bHeader == LG_HEADER_GG_LOGIN:
        Login(d, c_pData)

    elif bHeader == LG_HEADER_GG_LOGOUT:
        Logout(d, c_pData)

    elif bHeader == LG_HEADER_GG_RELAY:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((iExtraLen = Relay(d, c_pData, m_iBufferLeft)) < 0)
        if (iExtraLen = Relay(d, c_pData, m_iBufferLeft)) < 0:
            return -1

    elif bHeader == LG_HEADER_GG_NOTICE:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((iExtraLen = Notice(d, c_pData, m_iBufferLeft)) < 0)
        if (iExtraLen = Notice(d, c_pData, m_iBufferLeft)) < 0:
            return -1

    elif bHeader == LG_HEADER_GG_SHUTDOWN:
        #lani_err("Accept shutdown p2p command from %s.", d.GetHostName())
        Shutdown(10)

    elif bHeader == LG_HEADER_GG_GUILD:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((iExtraLen = Guild(d, c_pData, m_iBufferLeft)) < 0)
        if (iExtraLen = Guild(d, c_pData, m_iBufferLeft)) < 0:
            return -1

    elif bHeader == LG_HEADER_GG_SHOUT:
        Shout(c_pData)

    elif bHeader == LG_HEADER_GG_DISCONNECT:
        Disconnect(c_pData)

    elif bHeader == LG_HEADER_GG_MESSENGER_ADD:
        MessengerAdd(c_pData)

    elif bHeader == LG_HEADER_GG_MESSENGER_REMOVE:
        MessengerRemove(c_pData)

    elif bHeader == LG_HEADER_GG_FIND_POSITION:
        FindPosition(d, c_pData)

    elif bHeader == LG_HEADER_GG_WARP_CHARACTER:
        WarpCharacter(c_pData)

    elif bHeader == LG_HEADER_GG_GUILD_WAR_ZONE_MAP_INDEX:
        GuildWarZoneMapIndex(c_pData)

    elif bHeader == LG_HEADER_GG_TRANSFER:
        Transfer(c_pData)

    elif bHeader == LG_HEADER_GG_XMAS_WARP_SANTA:
        XmasWarpSanta(c_pData)

    elif bHeader == LG_HEADER_GG_XMAS_WARP_SANTA_REPLY:
        XmasWarpSantaReply(c_pData)

    elif bHeader == LG_HEADER_GG_RELOAD_CRC_LIST:
        LoadValidCRCList()

    elif bHeader == LG_HEADER_GG_CHECK_CLIENT_VERSION:
        CheckClientVersion()

    elif bHeader == LG_HEADER_GG_LOGIN_PING:
        LoginPing(d, c_pData)

    elif bHeader == LG_HEADER_GG_BLOCK_CHAT:
        BlockChat(c_pData)

    elif bHeader == LG_HEADER_GG_CHECK_AWAKENESS:
        IamAwake(d, c_pData)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if __MULTI_LANGUAGE_SYSTEM__
    elif bHeader == LG_HEADER_GG_LOCALE_NOTICE:
        LocaleNotice(c_pData)
##endif


    return (iExtraLen)
