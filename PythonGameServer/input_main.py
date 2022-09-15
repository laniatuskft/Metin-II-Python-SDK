import math

def TargetInfoLoad(ch, c_pData):
    p = c_pData
    pInfo = packet_target_info()
    pInfo.header = byte(LG_HEADER_GC_TARGET_INFO)
    ## Laniatus Games Studio Inc. | NOTE: This static local variable declaration (not allowed in Python) has been moved just prior to the method:
    #    static list<CItem*> s_vec_item
    TargetInfoLoad_s_vec_item.clear()
    pkInfoItem = None
    m_pkChrTarget = CHARACTER_MANAGER.instance().Find(p.dwVID)


    if ch is None or m_pkChrTarget is None:
        return

    if ITEM_MANAGER.instance().CreateDropItemVector(m_pkChrTarget, ch, TargetInfoLoad_s_vec_item) and (m_pkChrTarget.IsMonster() or m_pkChrTarget.IsStone()):
        if TargetInfoLoad_s_vec_item.size() == 0:
            pass
        elif TargetInfoLoad_s_vec_item.size() == 1:
            pkInfoItem = TargetInfoLoad_s_vec_item[0]
            pInfo.dwVID = m_pkChrTarget.GetVID()
            pInfo.race = m_pkChrTarget.GetRaceNum()
            pInfo.dwVnum = pkInfoItem.GetVnum()
            pInfo.count = ushort(pkInfoItem.GetCount())
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            ch.GetDesc().Packet(pInfo, sizeof(packet_target_info))
        else:
            iItemIdx = TargetInfoLoad_s_vec_item.size() - 1
            while iItemIdx >= 0:
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: pkInfoItem = s_vec_item[iItemIdx--];
                pkInfoItem = TargetInfoLoad_s_vec_item[iItemIdx]
                iItemIdx -= 1

                if pkInfoItem is None:
                    #lani_err("pkInfoItem null in vector idx %d", iItemIdx + 1)
                    continue

                pInfo.dwVID = m_pkChrTarget.GetVID()
                pInfo.race = m_pkChrTarget.GetRaceNum()
                pInfo.dwVnum = pkInfoItem.GetVnum()
                pInfo.count = ushort(pkInfoItem.GetCount())
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                ch.GetDesc().Packet(pInfo, sizeof(packet_target_info))

class spam_event_info(event_info_data):

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.host = str(['\0' for _ in range((int)LGEMiscellaneous.LG_MAX_HOST_LENGTH+1)])

        memset(self.host, 0, LGEMiscellaneous.LG_MAX_HOST_LENGTH+1)

def Whisper(ch, data, uiBytes):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no equivalent to 'reinterpret_cast' in Python:
    pinfo = reinterpret_cast<const command_whisper>(data)

    if uiBytes < pinfo.wSize:
        return -1

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    iExtraLen = pinfo.wSize - sizeof(command_whisper)

    if iExtraLen < 0:
        #lani_err("invalid packet length (len %d size %u buffer %u)", iExtraLen, pinfo.wSize, uiBytes)
        ch.GetDesc().SetPhase(EPhase.PHASE_CLOSE)
        return -1

    if ch.GetLastPMPulse() < thecore_pulse():
        ch.ClearPMCounter()

    if ch.GetPMCounter() > 6 and ch.GetLastPMPulse() > thecore_pulse():
        ch.GetDesc().SetPhase(EPhase.PHASE_CLOSE)
        return -1

    if ch.FindAffect(LaniatusEAffectTypes.LANIA_AFFECT_BLOCK_CHAT, APPLY_NONE):
        ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Your Chat is blocked."))
        return (iExtraLen)

    pkChr = CHARACTER_MANAGER.instance().FindPC(pinfo.szNameTo)

    if pkChr is ch:
        return (iExtraLen)

    ch.IncreasePMCounter()
    ch.SetLastPMPulse()
    pkDesc = None

    bOpponentEmpire = 0

    if test_server:
        if pkChr is None:
            #sys_log(0, "Whisper to %s(%s) from %s", "Null", pinfo.szNameTo, ch.GetName(LOCALE_LANIATUS))
        else:
            #sys_log(0, "Whisper to %s(%s) from %s", pkChr.GetName(LOCALE_LANIATUS), pinfo.szNameTo, ch.GetName(LOCALE_LANIATUS))

    if ch.IsBlockMode(EBlockAction.BLOCK_WHISPER):
        if ch.GetDesc():
            pack = packet_whisper()
            pack.bHeader = byte(LG_HEADER_GC_WHISPER)
            pack.bType = EWhisperType.WHISPER_TYPE_SENDER_BLOCKED
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            pack.wSize = sizeof(packet_whisper)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            strncpy_s(pack.szNameFrom, sizeof(pack.szNameFrom), pinfo.szNameTo, _TRUNCATE)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            ch.GetDesc().Packet(pack, sizeof(pack))
        return iExtraLen

    if pkChr is None:
        pkCCI = P2P_MANAGER.instance().Find(pinfo.szNameTo)

        if pkCCI:
            pkDesc = pkCCI.pkDesc
            pkDesc.SetRelay(pinfo.szNameTo)
            bOpponentEmpire = pkCCI.bEmpire

            if test_server:
                #sys_log(0, "Whisper to %s from %s (Channel %d Mapindex %d)", "Null", ch.GetName(LOCALE_LANIATUS), pkCCI.bChannel, pkCCI.lMapIndex)
    else:
        pkDesc = pkChr.GetDesc()
        bOpponentEmpire = pkChr.GetEmpire()

    if pkDesc is None:
        if ch.GetDesc():
            pack = packet_whisper()

            pack.bHeader = byte(LG_HEADER_GC_WHISPER)
            pack.bType = EWhisperType.WHISPER_TYPE_NOT_EXIST
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            pack.wSize = sizeof(packet_whisper)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            strncpy_s(pack.szNameFrom, sizeof(pack.szNameFrom), pinfo.szNameTo, _TRUNCATE)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            ch.GetDesc().Packet(pack, sizeof(packet_whisper))
            #sys_log(0, "WHISPER: no player")
    else:
        if ch.IsBlockMode(EBlockAction.BLOCK_WHISPER):
            if ch.GetDesc():
                pack = packet_whisper()
                pack.bHeader = byte(LG_HEADER_GC_WHISPER)
                pack.bType = EWhisperType.WHISPER_TYPE_SENDER_BLOCKED
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                pack.wSize = sizeof(packet_whisper)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                strncpy_s(pack.szNameFrom, sizeof(pack.szNameFrom), pinfo.szNameTo, _TRUNCATE)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                ch.GetDesc().Packet(pack, sizeof(pack))
        elif pkChr is not None and pkChr.IsBlockMode(EBlockAction.BLOCK_WHISPER):
            if ch.GetDesc():
                pack = packet_whisper()
                pack.bHeader = byte(LG_HEADER_GC_WHISPER)
                pack.bType = EWhisperType.WHISPER_TYPE_TARGET_BLOCKED
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                pack.wSize = sizeof(packet_whisper)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                strncpy_s(pack.szNameFrom, sizeof(pack.szNameFrom), pinfo.szNameTo, _TRUNCATE)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                ch.GetDesc().Packet(pack, sizeof(pack))
        else:
            bType = EWhisperType.WHISPER_TYPE_NORMAL

            buf = str(['\0' for _ in range((int)LGEMiscellaneous.CHAT_MAX_LEN + 1)])
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            strncpy_s(buf, MIN(iExtraLen + 1, sizeof(buf)), data + sizeof(command_whisper), _TRUNCATE)
            buflen = len(buf)

            if ((not LGEMiscellaneous.DEFINECONSTANTS.false)) == SpamBlockCheck(ch, buf, buflen):
                if pkChr is None:
                    pkCCI = P2P_MANAGER.instance().Find(pinfo.szNameTo)

                    if pkCCI:
                        pkDesc.SetRelay("")
                return iExtraLen

            processReturn = ProcessTextTag(ch, buf, buflen)
            if 0!=processReturn:
                if ch.GetDesc():
                    pTable = ITEM_MANAGER.instance().GetTable(uint(ITEM_PRISM))

                    if pTable:
                        buf = str(['\0' for _ in range(128)])
                        len = None
                        if 3==processReturn:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                            len = snprintf(buf, sizeof(buf), LC_TEXT("You can't use a private shop now."), pTable.szLocaleName)
                        else:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if __MULTI_LANGUAGE_SYSTEM__
                            bLocale = ch.GetDesc().GetLanguage()
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                            len = snprintf(buf, sizeof(buf), LC_TEXT("%s is required."), LC_LOCALE_ITEM_TEXT(ITEM_PRISM, bLocale))
##else
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                            len = snprintf(buf, sizeof(buf), LC_TEXT("%s is required."), pTable.szLocaleName)
##endif


## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                            if len < 0 or len >= int(sizeof(buf)):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                                len = sizeof(buf) - 1

                            len += 1

                            pack = packet_whisper()

                            pack.bHeader = byte(LG_HEADER_GC_WHISPER)
                            pack.bType = EWhisperType.WHISPER_TYPE_ERROR
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                            pack.wSize = sizeof(packet_whisper) + len
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                            strncpy_s(pack.szNameFrom, sizeof(pack.szNameFrom), pinfo.szNameTo, _TRUNCATE)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                            ch.GetDesc().BufferedPacket(pack, sizeof(pack))
                            ch.GetDesc().Packet(buf, len)

                            #sys_log(0, "WHISPER: not enough %s: char: %s", pTable.szLocaleName, ch.GetName(LOCALE_LANIATUS))
                    pkDesc.SetRelay("")
                    return (iExtraLen)

                if ch.IsGM():
                    bType = byte((bType & 0xF0) | EWhisperType.WHISPER_TYPE_GM)

                if buflen > 0:
                    pack = packet_whisper()

                    pack.bHeader = byte(LG_HEADER_GC_WHISPER)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                    pack.wSize = sizeof(packet_whisper) + buflen
                    pack.bType = bType
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                    strncpy_s(pack.szNameFrom, sizeof(pack.szNameFrom), ch.GetName(LOCALE_LANIATUS), _TRUNCATE)
                    tmpbuf = TEMP_BUFFER(8192, DefineConstants.false)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                    tmpbuf.write(pack, sizeof(pack))
                    tmpbuf.write(buf, buflen)

                    pkDesc.Packet(tmpbuf.read_peek(), tmpbuf.size())
        if pkDesc:
            pkDesc.SetRelay("")

        return (iExtraLen)

    struct RawPacketToCharacterFunc
        m_buf = None
        m_buf_len = None

        RawPacketToCharacterFunc(object* buf, int buf_len) : m_buf(buf), m_buf_len(buf_len)

        void operator ()(CHARACTER* c)
            if not c.GetDesc():
                return

            c.GetDesc().Packet(m_buf, m_buf_len)

    struct FEmpireChatPacket
        p = None
        orig_msg = None
        orig_len = None
        converted_msg = str(['\0' for _ in range((int)LGEMiscellaneous.CHAT_MAX_LEN + 1)])

        bEmpire = None
        iMapIndex = None
        namelen = None

        FEmpireChatPacket(packet_chat& p, const char* chat_msg, int len, byte bEmpire, int iMapIndex, int iNameLen) : p(p), orig_msg(chat_msg), orig_len(len), bEmpire(bEmpire), iMapIndex(iMapIndex), namelen(iNameLen)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            memset(converted_msg, 0, sizeof(converted_msg))

        void operator ()(DESC* d)
            if not d.GetCharacter():
                return

            if d.GetCharacter().GetMapIndex() != iMapIndex:
                return

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            d.BufferedPacket(p, sizeof(packet_chat))

            if d.GetEmpire() == bEmpire or bEmpire == 0 or d.GetCharacter().GetGMLevel() > EGMLevels.GM_PLAYER or d.GetCharacter().IsEquipUniqueGroup(UNIQUE_GROUP_RING_OF_LANGUAGE):
                d.Packet(orig_msg, orig_len)
            else:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                len = strncpy_s(converted_msg, sizeof(converted_msg), orig_msg, _TRUNCATE)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                if len >= sizeof(converted_msg):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                    len = sizeof(converted_msg) - 1

                ConvertEmpireText(bEmpire, converted_msg[namelen:], len - namelen, 10 + 2 * d.GetCharacter().GetSkillPower(LaniatusETalentXes.LG_SKILL_LANGUAGE1 + bEmpire - 1))
                d.Packet(converted_msg, orig_len)

    struct FYmirChatPacket
        packet = None
        m_szChat = None
        m_lenChat = None
        m_szName = None

        m_iMapIndex = None
        m_bEmpire = None
        m_ring = None

        m_orig_msg = str(['\0' for _ in range((int)LGEMiscellaneous.CHAT_MAX_LEN + 1)])
        m_len_orig_msg = None
        m_conv_msg = str(['\0' for _ in range((int)LGEMiscellaneous.CHAT_MAX_LEN + 1)])
        m_len_conv_msg = None

        FYmirChatPacket(packet_chat& p, const char* chat, int len_chat, const char* name, int len_name, int iMapIndex, byte empire, bool ring) : packet(p), m_szChat(chat), m_lenChat(len_chat), m_szName(name), m_iMapIndex(iMapIndex), m_bEmpire(empire), m_ring(ring)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            m_len_orig_msg = snprintf(m_orig_msg, sizeof(m_orig_msg), "%s : %s", m_szName, m_szChat) + 1

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            if m_len_orig_msg < 0 or m_len_orig_msg >= int(sizeof(m_orig_msg)):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                m_len_orig_msg = sizeof(m_orig_msg) - 1

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            m_len_conv_msg = snprintf(m_conv_msg, sizeof(m_conv_msg), "??? : %s", m_szChat) + 1

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            if m_len_conv_msg < 0 or m_len_conv_msg >= int(sizeof(m_conv_msg)):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                m_len_conv_msg = sizeof(m_conv_msg) - 1

            ConvertEmpireText(m_bEmpire, m_conv_msg[6:], m_len_conv_msg - 6, 10)

        void operator ()(DESC* d)
            if not d.GetCharacter():
                return

            if d.GetCharacter().GetMapIndex() != m_iMapIndex:
                return

            if m_ring or d.GetEmpire() == m_bEmpire or d.GetCharacter().GetGMLevel() > EGMLevels.GM_PLAYER or d.GetCharacter().IsEquipUniqueGroup(UNIQUE_GROUP_RING_OF_LANGUAGE):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                packet.size = m_len_orig_msg + sizeof(packet_chat)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                d.BufferedPacket(packet, sizeof(packet_chat))
                d.Packet(m_orig_msg, m_len_orig_msg)
            else:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                packet.size = m_len_conv_msg + sizeof(packet_chat)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                d.BufferedPacket(packet, sizeof(packet_chat))
                d.Packet(m_conv_msg, m_len_conv_msg)

    int CInputMain.Chat(CHARACTER* ch, const char data[0], int uiBytes)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no equivalent to 'reinterpret_cast' in Python:
        pinfo = reinterpret_cast<const command_chat>(data)

        if uiBytes < pinfo.size:
            return -1

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        iExtraLen = pinfo.size - sizeof(command_chat)

        if iExtraLen < 0:
            #lani_err("invalid packet length (len %d size %u buffer %u)", iExtraLen, pinfo.size, uiBytes)
            ch.GetDesc().SetPhase(EPhase.PHASE_CLOSE)
            return -1

        buf = str(['\0' for _ in range((int)LGEMiscellaneous.CHAT_MAX_LEN - (LGEMiscellaneous.CHARACTER_NAME_MAX_LEN + 3) + 1)])
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        strncpy_s(buf, MIN(iExtraLen + 1, sizeof(buf)), data + sizeof(command_chat), _TRUNCATE)
        buflen = len(buf)

        if buflen > 1 and buf[0] == '/':
            interpret_command(ch, buf[1:], buflen - 1)
            return iExtraLen

        if ch.IncreaseChatCounter() >= 10:
            if ch.GetChatCounter() == 10:
                #sys_log(0, "CHAT_HACK: %s", ch.GetName(LOCALE_LANIATUS))
                ch.GetDesc().DelayedDisconnect(5)

            return iExtraLen

        pAffect = ch.FindAffect(LaniatusEAffectTypes.LANIA_AFFECT_BLOCK_CHAT, APPLY_NONE)

        if pAffect is not None:
            SendBlockChatInfo(ch, pAffect.lDuration)
            return iExtraLen

        if ((not LGEMiscellaneous.DEFINECONSTANTS.false)) == SpamBlockCheck(ch, buf, buflen):
            return iExtraLen

        chatbuf = str(['\0' for _ in range((int)LGEMiscellaneous.CHAT_MAX_LEN + 1)])
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        len = snprintf(chatbuf, sizeof(chatbuf), "%s: %s", ch.GetName(LOCALE_LANIATUS), buf)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        if len < 0 or len >= int(sizeof(chatbuf)):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            len = sizeof(chatbuf) - 1

        processReturn = ProcessTextTag(ch, chatbuf, len)
        if 0!=processReturn:
            pTable = ITEM_MANAGER.instance().GetTable(uint(ITEM_PRISM))

            if None is not pTable:
                if 3==processReturn:
                    ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You can't use a private shop now."), pTable.szLocaleName)
                else:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if __MULTI_LANGUAGE_SYSTEM__
                    bLocale = ch.GetDesc().GetLanguage()
                    ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("%s is required."), LC_LOCALE_ITEM_TEXT(ITEM_PRISM, bLocale))
##else
                    ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("%s is required."), pTable.szLocaleName)
##endif


                return iExtraLen

            if pinfo.type == EChatType.CHAT_TYPE_SHOUT:
                SHOUT_LIMIT_LEVEL = 15

                if ch.GetLevel() < SHOUT_LIMIT_LEVEL:
                    ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You need Level %d to be able to call."), SHOUT_LIMIT_LEVEL)
                    return (iExtraLen)

                if thecore_heart.pulse - int(ch.GetLastShoutPulse()) < passes_per_sec * 15:
                    return (iExtraLen)

                ch.SetLastShoutPulse(thecore_heart.pulse)

                kingdoms = ["|cFFff0000|H|h[Shinsoo]|cFFa7FFD4|H|h", "|cFFFFFF00|H|h[Chunjo]|cFFA7FFD4|H|h", "|cFF0080FF|H|h[Jinno]|cFFA7FFD4|H|h"]
                chatbuf_global = str(['\0' for _ in range((int)LGEMiscellaneous.CHAT_MAX_LEN + 1)])
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if __MULTI_LANGUAGE_SYSTEM__
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                len_global = snprintf(chatbuf_global, sizeof(chatbuf_global), "|L%s|l %s %s", LC_LOCALE(ch.GetDesc().GetLanguage()), kingdoms[ch.GetEmpire()-1], chatbuf)
##else
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                len_global = snprintf(chatbuf_global, sizeof(chatbuf_global), "%s %s", kingdoms[ch.GetEmpire() - 1], chatbuf)
##endif

                p = SPacketGGShout()

                p.bHeader = byte(LG_HEADER_GG_SHOUT)
                p.bEmpire = ch.GetEmpire()
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                strncpy_s(p.szText, sizeof(p.szText), chatbuf_global, _TRUNCATE)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                P2P_MANAGER.instance().Send(p, sizeof(SPacketGGShout), NULL)

                SendShout(chatbuf_global, ch.GetEmpire())

                return (iExtraLen)

            pack_chat = packet_chat()

            pack_chat.header = byte(LG_HEADER_GC_CHAT)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            pack_chat.size = sizeof(packet_chat) + len
            pack_chat.type = pinfo.type
            pack_chat.id = ch.GetVID()

            if pinfo.type == EChatType.CHAT_TYPE_TALKING:
                    c_ref_set = DESC_MANAGER.instance().GetClientSet()

                    if ((not LGEMiscellaneous.DEFINECONSTANTS.false)):
                        std::for_each(c_ref_set.begin(), c_ref_set.end(), FYmirChatPacket(pack_chat, buf, len(buf), ch.GetName(LOCALE_LANIATUS), len(ch.GetName(LOCALE_LANIATUS)), ch.GetMapIndex(), ch.GetEmpire(), ch.IsEquipUniqueGroup(uint(UNIQUE_GROUP_RING_OF_LANGUAGE))))
                    else:
                        std::for_each(c_ref_set.begin(), c_ref_set.end(), FEmpireChatPacket(pack_chat, chatbuf, len, byte(0 if (ch.GetGMLevel() >= EGMLevels.GM_PLAYER or ch.IsEquipUniqueGroup(uint(UNIQUE_GROUP_RING_OF_LANGUAGE))) else ch.GetEmpire()), ch.GetMapIndex(), len(ch.GetName(LOCALE_LANIATUS))))

            elif pinfo.type == EChatType.CHAT_TYPE_PARTY:
                    if ch.GetParty() is None:
                        ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You are not in this Group."))
                    else:
                        tbuf = TEMP_BUFFER(8192, DefineConstants.false)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                        tbuf.write(pack_chat, sizeof(pack_chat))
                        tbuf.write(chatbuf, len)

                        f = RawPacketToCharacterFunc(tbuf.read_peek(), tbuf.size())
                        ch.GetParty().ForEachOnlineMember(f.functor_method)

            elif pinfo.type == EChatType.CHAT_TYPE_GUILD:
                    if ch.GetGuild() is None:
                        ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You did not join this Guild."))
                    else:
                        ch.GetGuild().Chat(chatbuf)

            else:
                #lani_err("Unknown chat type %d", pinfo.type)

            return (iExtraLen)

        void CInputMain.ItemUse(CHARACTER* ch, const char data[0])
            ch.UseItem((data).Cell, NPOS)

        void CInputMain.ItemToItem(CHARACTER* ch, const char * pcData)
            p = pcData
            if ch:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
#ORIGINAL METINII C CODE: ch->UseItem(p->Cell, p->TargetCell);
                ch.UseItem(SItemPos(p.Cell), SItemPos(p.TargetCell))

        void CInputMain.ItemDrop(CHARACTER* ch, const char data[0])
            pinfo = data

            if ch is None:
                return

            if pinfo.gold > 0:
                ch.DropGold(pinfo.gold)
            else:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
#ORIGINAL METINII C CODE: ch->DropItem(pinfo->Cell);
                ch.DropItem(SItemPos(pinfo.Cell), 0)

        void CInputMain.ItemDrop2(CHARACTER* ch, const char data[0])
            pinfo = data

            if ch is None:
                return
            if pinfo.gold > 0:
                ch.DropGold(pinfo.gold)
            else:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
#ORIGINAL METINII C CODE: ch->DropItem(pinfo->Cell, pinfo->count);
                ch.DropItem(SItemPos(pinfo.Cell), pinfo.count)

        void CInputMain.ItemDestroy(CHARACTER* ch, const chardata[0])
            pinfo = data

            if ch:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
#ORIGINAL METINII C CODE: ch->DestroyItem(pinfo->Cell);
                ch.DestroyItem(SItemPos(pinfo.Cell))

        void CInputMain.ItemMove(CHARACTER* ch, const char data[0])
            pinfo = data

            if ch:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
#ORIGINAL METINII C CODE: ch->MoveItem(pinfo->Cell, pinfo->CellTo, pinfo->count);
                ch.MoveItem(SItemPos(pinfo.Cell), SItemPos(pinfo.CellTo), pinfo.count)

        struct RangePickupSingle
            pkCharacter = None

            RangePickupSingle(CHARACTER* _ch) : pkCharacter(_ch)

            bool operator ()(CEntity* pEnt)
                if pEnt.IsType(EEntityTypes.ENTITY_ITEM):
                    item = pEnt
                    if item is None:
                        return LGEMiscellaneous.DEFINECONSTANTS.false

                    if not item.DistanceValid(pkCharacter):
                        return LGEMiscellaneous.DEFINECONSTANTS.false

                    return 1 if ((not LGEMiscellaneous.DEFINECONSTANTS.false)) else 0

                return LGEMiscellaneous.DEFINECONSTANTS.false

        struct RangePickupAll
            pkCharacter = None

            RangePickupAll(CHARACTER* ch) : pkCharacter(ch)

            void operator ()(CEntity* pEnt)
                if pkCharacter is None:
                    return

                if pEnt.IsType(EEntityTypes.ENTITY_ITEM):
                    item = pEnt
                    if item is None:
                        return

                    pkCharacter.PickupItem(item, 0)

        void CInputMain.ItemPickup(CHARACTER* ch, const char data[0])
            if ch is None:
                return

            sectree = ch.GetSectree()
            if sectree is None:
                return

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no equivalent to 'reinterpret_cast' in Python:
            pinfo = reinterpret_cast<const command_item_pickup>(data)

            if ch.GetPickupMode() == EPickupModes.PICKUP_MODE_SINGLE:
                f = RangePickupSingle(ch)
                pEnt = sectree.find_if(f.functor_method)
                if pEnt is None:
                    return

                item = pEnt
                if item is None:
                    return

                ch.PickupItem(item, pinfo.vid)
            elif ch.GetPickupMode() == EPickupModes.PICKUP_MODE_ALL:
                if pinfo.vid != 0:
                    ch.PickupItem(None, pinfo.vid)
                else:
                    f = RangePickupAll(ch)
                    sectree.ForEachAround(f.functor_method)

        void CInputMain.QuickslotAdd(CHARACTER* ch, const char data[0])
            pinfo = data
            ch.SetQuickslot(pinfo.pos, pinfo.slot)

        void CInputMain.QuickslotDelete(CHARACTER* ch, const char data[0])
            pinfo = data
            ch.DelQuickslot(pinfo.pos)

        void CInputMain.QuickslotSwap(CHARACTER* ch, const char data[0])
            pinfo = data
            ch.SwapQuickslot(pinfo.pos, pinfo.change_pos)

        int CInputMain.Messenger(CHARACTER* ch, const char* c_pData, int uiBytes)
            p = c_pData

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            if uiBytes < sizeof(command_messenger):
                return -1

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            c_pData += sizeof(command_messenger)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            uiBytes -= sizeof(command_messenger)

            if p.subheader == MESSENGER_SUBLG_HEADER_CG_ADD_BY_VID:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                    if uiBytes < sizeof(command_messenger_add_by_vid):
                        return -1

                    p2 = c_pData
                    ch_companion = CHARACTER_MANAGER.instance().Find(p2.vid)

                    if ch_companion is None:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                        return sizeof(command_messenger_add_by_vid)

                    if ch.IsObserverMode():
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                        return sizeof(command_messenger_add_by_vid)

                    if ch_companion.IsBlockMode(EBlockAction.BLOCK_MESSENGER_INVITE):
                        ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("The player declines to be added to the messenger."))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                        return sizeof(command_messenger_add_by_vid)

                    d = ch_companion.GetDesc()

                    if d is None:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                        return sizeof(command_messenger_add_by_vid)

                    if ch.GetGMLevel() == EGMLevels.GM_PLAYER and ch_companion.GetGMLevel() != EGMLevels.GM_PLAYER:
                        ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Messenger> GM cannot be added on Messenger."))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                        return sizeof(command_messenger_add_by_vid)

                    if ch.GetDesc() is d:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                        return sizeof(command_messenger_add_by_vid)

                    MessengerManager.instance().RequestToAdd(ch, ch_companion)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                return sizeof(command_messenger_add_by_vid)

            if (p.subheader == MESSENGER_SUBLG_HEADER_CG_ADD_BY_VID) or (p.subheader == MESSENGER_SUBLG_HEADER_CG_ADD_BY_NAME):
                    if uiBytes < LGEMiscellaneous.CHARACTER_NAME_MAX_LEN:
                        return -1

                    name = str(['\0' for _ in range((int)LGEMiscellaneous.CHARACTER_NAME_MAX_LEN + 1)])
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                    strncpy_s(name, sizeof(name), c_pData, _TRUNCATE)

                    if ch.GetGMLevel() == EGMLevels.GM_PLAYER and gm_get_level(name, NULL, NULL) != EGMLevels.GM_PLAYER:
                        ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Messenger> GM cannot be added on Messenger."))
                        return LGEMiscellaneous.CHARACTER_NAME_MAX_LEN

                    tch = CHARACTER_MANAGER.instance().FindPC(name)

                    if tch is None:
                        ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("%s is not in the game."), name)
                    else:
                        if tch is ch:
                            return LGEMiscellaneous.CHARACTER_NAME_MAX_LEN

                        if tch.IsBlockMode(EBlockAction.BLOCK_MESSENGER_INVITE) == ((not LGEMiscellaneous.DEFINECONSTANTS.false)):
                            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("The player declines to be added to the messenger."))
                        else:
                            MessengerManager.instance().RequestToAdd(ch, tch)
                return LGEMiscellaneous.CHARACTER_NAME_MAX_LEN

            if (p.subheader == MESSENGER_SUBLG_HEADER_CG_ADD_BY_VID) or (p.subheader == MESSENGER_SUBLG_HEADER_CG_ADD_BY_NAME) or (p.subheader == MESSENGER_SUBLG_HEADER_CG_REMOVE):
                    if uiBytes < LGEMiscellaneous.CHARACTER_NAME_MAX_LEN:
                        return -1

                    char_name = str(['\0' for _ in range((int)LGEMiscellaneous.CHARACTER_NAME_MAX_LEN + 1)])
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                    strncpy_s(char_name, sizeof(char_name), c_pData, _TRUNCATE)
                    MessengerManager.instance().RemoveFromList(ch.GetName(LOCALE_LANIATUS), char_name)
                return LGEMiscellaneous.CHARACTER_NAME_MAX_LEN


            if True:
                #lani_err("CInputMain::Messenger : Unknown subheader %d : %s", p.subheader, ch.GetName(LOCALE_LANIATUS))

            return 0

        int CInputMain.Shop(CHARACTER* ch, const chardata[0], int uiBytes)
            p = data

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            if uiBytes < sizeof(command_shop):
                return -1

            if test_server:
                #sys_log(0, "CInputMain::Shop() ==> SubHeader %d", p.subheader)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            c_pData = data + sizeof(command_shop)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            uiBytes -= sizeof(command_shop)

            if p.subheader == SHOP_SUBLG_HEADER_CG_END:
                #sys_log(1, "INPUT: %s SHOP: END", ch.GetName(LOCALE_LANIATUS))
                CShopManager.instance().StopShopping(ch)
                return 0

            if (p.subheader == SHOP_SUBLG_HEADER_CG_END) or (p.subheader == SHOP_SUBLG_HEADER_CG_BUY):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                    if uiBytes < sizeof(byte) + sizeof(byte):
                        return -1

                    bPos = c_pData[1]
                    #sys_log(1, "INPUT: %s SHOP: BUY %d", ch.GetName(LOCALE_LANIATUS), bPos)
                    CShopManager.instance().Buy(ch, bPos)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                    return (sizeof(byte) + sizeof(byte))

            if (p.subheader == SHOP_SUBLG_HEADER_CG_END) or (p.subheader == SHOP_SUBLG_HEADER_CG_BUY) or (p.subheader == SHOP_SUBLG_HEADER_CG_SELL):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                    if uiBytes < sizeof(byte):
                        return -1

                    pos = c_pData[0]

                    #sys_log(0, "INPUT: %s SHOP: SELL", ch.GetName(LOCALE_LANIATUS))
                    CShopManager.instance().Sell(ch, pos, 0)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                    return sizeof(byte)

            if (p.subheader == SHOP_SUBLG_HEADER_CG_END) or (p.subheader == SHOP_SUBLG_HEADER_CG_BUY) or (p.subheader == SHOP_SUBLG_HEADER_CG_SELL) or (p.subheader == SHOP_SUBLG_HEADER_CG_SELL2):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                    if uiBytes < sizeof(byte) + sizeof(ushort):
                        return -1

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no equivalent to 'reinterpret_cast' in Python:
                    pos = *reinterpret_cast<const byte>(c_pData)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                    count = c_pData[sizeof(byte)]

                    #sys_log(0, "INPUT: %s SHOP: SELL2", ch.GetName(LOCALE_LANIATUS))
                    CShopManager.instance().Sell(ch, pos, count)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                    return sizeof(byte) + sizeof(ushort)


            if True:
                #lani_err("CInputMain::Shop : Unknown subheader %d : %s", p.subheader, ch.GetName(LOCALE_LANIATUS))

            return 0

        void CInputMain.OnClick(CHARACTER* ch, const char data[0])
            pinfo = data
            victim = None

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((victim = CHARACTER_MANAGER::instance().Find(pinfo->vid)))
            if (victim = CHARACTER_MANAGER.instance().Find(pinfo.vid)):
                victim.OnClick(ch)

        void CInputMain.Exchange(CHARACTER* ch, const char data[0])
            pinfo = data
            to_ch = None

            if not ch.CanHandleItem(DefineConstants.false, DefineConstants.false):
                return

            iPulse = thecore_pulse()

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((to_ch = CHARACTER_MANAGER::instance().Find(pinfo->arg1)))
            if (to_ch = CHARACTER_MANAGER.instance().Find(pinfo.arg1)):
                if iPulse - to_ch.GetSafeboxLoadTime() < ((g_nPortalLimitTime) * passes_per_sec):
                    to_ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("After you traded you can open a Warehouse after %d seconds."), g_nPortalLimitTime)
                    return

                if ((not LGEMiscellaneous.DEFINECONSTANTS.false)) == to_ch.IsDead():
                    return

            #sys_log(0, "CInputMain()::Exchange()  SubHeader %d ", pinfo.sub_header)

            if iPulse - ch.GetSafeboxLoadTime() < ((g_nPortalLimitTime) * passes_per_sec):
                ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("After you traded you can open a Warehouse after %d seconds."), g_nPortalLimitTime)
                return


            if pinfo.sub_header == EXCHANGE_SUBLG_HEADER_CG_START:
                if ch.GetExchange() is None:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((to_ch = CHARACTER_MANAGER::instance().Find(pinfo->arg1)))
                    if (to_ch = CHARACTER_MANAGER.instance().Find(pinfo.arg1)):
                        if iPulse - ch.GetSafeboxLoadTime() < ((g_nPortalLimitTime) * passes_per_sec):
                            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You can trade again in %d seconds."), g_nPortalLimitTime)

                            if test_server:
                                ch.ChatPacket(EChatType.CHAT_TYPE_INFO, "[TestOnly][Safebox]Pulse %d LoadTime %d PASS %d", iPulse, ch.GetSafeboxLoadTime(), ((g_nPortalLimitTime) * passes_per_sec))
                            return

                        if iPulse - to_ch.GetSafeboxLoadTime() < ((g_nPortalLimitTime) * passes_per_sec):
                            to_ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You can trade again in %d seconds."), g_nPortalLimitTime)


                            if test_server:
                                to_ch.ChatPacket(EChatType.CHAT_TYPE_INFO, "[TestOnly][Safebox]Pulse %d LoadTime %d PASS %d", iPulse, to_ch.GetSafeboxLoadTime(), ((g_nPortalLimitTime) * passes_per_sec))
                            return

                        if ch.GetGold() >= MaxGold.GOLD_MAX:
                            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You have more than 2 Billion Yang. You cannot trade."))

                            #lani_err("[OVERFLOG_GOLD] START (%lld) id %u name %s ", ch.GetGold(), ch.GetPlayerID(), ch.GetName(LOCALE_LANIATUS))
                            return

                        if to_ch.IsPC():
                            if quest.CQuestManager.instance().GiveItemToPC(ch.GetPlayerID(), to_ch):
                                #sys_log(0, "Exchange canceled by quest %s %s", ch.GetName(LOCALE_LANIATUS), to_ch.GetName(LOCALE_LANIATUS))
                                return


                        if ch.GetMyShop() is not None or ch.IsOpenSafebox() or ch.GetShopOwner() is not None or ch.IsCubeOpen() or ch.IsAcceWindowOpen():
                            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You cannot open a private shop as long as you trade with others."))
                            return

                        ch.ExchangeStart(to_ch)

            elif pinfo.sub_header == EXCHANGE_SUBLG_HEADER_CG_ITEM_ADD:
                if ch.GetExchange():
                    if ch.GetExchange().GetCompany().GetAcceptStatus() != ((not LGEMiscellaneous.DEFINECONSTANTS.false)):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
#ORIGINAL METINII C CODE: ch->GetExchange()->AddItem(pinfo->Pos, pinfo->arg2);
                        ch.GetExchange().AddItem(SItemPos(pinfo.Pos), pinfo.arg2)

            elif pinfo.sub_header == EXCHANGE_SUBLG_HEADER_CG_ITEM_DEL:
                if ch.GetExchange():
                    if ch.GetExchange().GetCompany().GetAcceptStatus() != ((not LGEMiscellaneous.DEFINECONSTANTS.false)):
                        ch.GetExchange().RemoveItem(byte(pinfo.arg1))

            elif pinfo.sub_header == EXCHANGE_SUBLG_HEADER_CG_ELK_ADD:
                if ch.GetExchange():
                    nTotalGold = int(ch.GetExchange().GetCompany().GetOwner().GetGold()) + int(pinfo.arg1)

                    if MaxGold.GOLD_MAX <= nTotalGold:
                        ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("The player has more than 2 Billion Yang. You cannot trade with him."))

                        #lani_err("[OVERFLOW_GOLD] ELK_ADD (%lld) id %u name %s ", ch.GetExchange().GetCompany().GetOwner().GetGold(), ch.GetExchange().GetCompany().GetOwner().GetPlayerID(), ch.GetExchange().GetCompany().GetOwner().GetName(LOCALE_LANIATUS))

                        return

                    if ch.GetExchange().GetCompany().GetAcceptStatus() != ((not LGEMiscellaneous.DEFINECONSTANTS.false)):
                        ch.GetExchange().AddGold(pinfo.arg1)

            elif pinfo.sub_header == EXCHANGE_SUBLG_HEADER_CG_ACCEPT:
                if ch.GetExchange():
                    #sys_log(0, "CInputMain()::Exchange() ==> ACCEPT ")
                    ch.GetExchange().Accept(((not LGEMiscellaneous.DEFINECONSTANTS.false)))


            elif pinfo.sub_header == EXCHANGE_SUBLG_HEADER_CG_CANCEL:
                if ch.GetExchange():
                    ch.GetExchange().Cancel()

        void CInputMain.Position(CHARACTER* ch, const char data[0])
            pinfo = data

            if pinfo.position == ECharacterPosition.POSITION_GENERAL:
                ch.Standup()

            elif pinfo.position == ECharacterPosition.POSITION_SITTING_CHAIR:
                ch.Sitdown(0)

            elif pinfo.position == ECharacterPosition.POSITION_SITTING_GROUND:
                ch.Sitdown(1)

        ComboSequenceBySkillLevel = [[ 14, 15, 16, 17, 0, 0, 0, 0 ], [ 14, 15, 16, 18, 20, 0, 0, 0 ], [ 14, 15, 16, 18, 19, 17, 0, 0 ]]


        uint ClacValidComboInterval(CHARACTER* ch, byte bArg)
            nInterval = 300
            fAdjustNum = 1.5

            if ch is None:
                #lani_err("ClacValidComboInterval() ch is NULL")
                return nInterval

            if bArg == 13:
                normalAttackDuration = CMotionManager.instance().GetNormalAttackDuration(ch.GetRaceNum())
                nInterval = int((normalAttackDuration / ((float(ch.GetPoint(EPointTypes.LG_POINT_ATT_SPEED)) / 100.0) * 900.0) + fAdjustNum))
            elif bArg == 14:
                nInterval = int((ani_combo_speed(ch, 1) / ((ch.GetPoint(EPointTypes.LG_POINT_ATT_SPEED) / 100.0) + fAdjustNum)))
            elif bArg > 14 and (bArg << 22) != 0:
                nInterval = int((ani_combo_speed(ch, bArg - 13) / ((ch.GetPoint(EPointTypes.LG_POINT_ATT_SPEED) / 100.0) + fAdjustNum)))
            else:
                #lani_err("ClacValidComboInterval() Invalid bArg(%d) ch(%s)", bArg, ch.GetName(LOCALE_LANIATUS))

            return nInterval

        bool CheckComboHack(CHARACTER* ch, byte bArg, uint dwTime, bool CheckSpeedHack)

            if ch.IsStun() or ch.IsDead():
                return LGEMiscellaneous.DEFINECONSTANTS.false
            ComboInterval = dwTime - ch.GetLastComboTime()
            HackScalar = 0

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if false
            #	#sys_log(0, "COMBO: %s arg:%u seq:%u delta:%d checkspeedhack:%d",
            #			ch->GetName(), bArg, ch->GetComboSequence(), ComboInterval - ch->GetValidComboInterval(), CheckSpeedHack)
##endif
            if bArg == 14:
                if CheckSpeedHack and ComboInterval > 0 and ComboInterval < ch.GetValidComboInterval() - LGEMiscellaneous.DEFINECONSTANTS.COMBO_HACK_ALLOWABLE_MS:
                    pass

                ch.SetComboSequence(1)
                ch.SetValidComboInterval(int(ClacValidComboInterval(ch, bArg)))
                ch.SetLastComboTime(dwTime)
            elif bArg > 14 and bArg < 22:
                idx = MIN(2, ch.GetComboIndex())

                if ch.GetComboSequence() > 5:
                    HackScalar = 1
                    ch.SetValidComboInterval(300)
                    #sys_log(0, "COMBO_HACK: 5 %s combo_seq:%d", ch.GetName(LOCALE_LANIATUS), ch.GetComboSequence())
                elif bArg == 21 and idx == 2 and ch.GetComboSequence() == 5 and ch.GetJob() == EJobs.JOB_ASSASSIN and ch.GetWear(EWearPositions.WEAR_WEAPON) is not None and ch.GetWear(EWearPositions.WEAR_WEAPON).GetSubType() == EWeaponSubTypes.WEAPON_DAGGER:
                    ch.SetValidComboInterval(300)
                elif ComboSequenceBySkillLevel[idx][ch.GetComboSequence()] != bArg:
                    HackScalar = 1
                    ch.SetValidComboInterval(300)

                    #sys_log(0, "COMBO_HACK: 3 %s arg:%u valid:%u combo_idx:%d combo_seq:%d", ch.GetName(LOCALE_LANIATUS), bArg, ComboSequenceBySkillLevel[idx][ch.GetComboSequence()], idx, ch.GetComboSequence())
                else:
                    if CheckSpeedHack and ComboInterval < ch.GetValidComboInterval() - LGEMiscellaneous.DEFINECONSTANTS.COMBO_HACK_ALLOWABLE_MS:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
                        HackScalar = 1 + (ch.GetValidComboInterval() - ComboInterval) / 100

                        #sys_log(0, "COMBO_HACK: 2 %s arg:%u interval:%d valid:%u atkspd:%u riding:%s", ch.GetName(LOCALE_LANIATUS), bArg, ComboInterval, ch.GetValidComboInterval(), ch.GetPoint(EPointTypes.LG_POINT_ATT_SPEED),"yes" if ch.IsRiding() else "no")

                    if ch.IsRiding():
                        ch.SetComboSequence(byte(2 if ch.GetComboSequence() == 1 else 1))
                    else:
                        ch.SetComboSequence(byte(ch.GetComboSequence() + 1))

                    ch.SetValidComboInterval(int(ClacValidComboInterval(ch, bArg)))
                    ch.SetLastComboTime(dwTime)
            elif bArg == 13:
                if CheckSpeedHack and ComboInterval > 0 and ComboInterval < ch.GetValidComboInterval() - LGEMiscellaneous.DEFINECONSTANTS.COMBO_HACK_ALLOWABLE_MS:
                    pass

                if ch.GetRaceNum() >= MAIN_RACE_MAX_NUM:
                    ch.SetValidComboInterval(int(ClacValidComboInterval(ch, bArg)))
                    ch.SetLastComboTime(dwTime)
                else:
                    pass
            else:
                if ch.GetDesc().DelayedDisconnect(number(2, 9)):
                    LogManager.instance().HackLog(ch.GetAID(), ch.GetName(LOCALE_LANIATUS), "Hacker")
                    #sys_log(0, "HACKER: %s arg %u", ch.GetName(LOCALE_LANIATUS), bArg)

                HackScalar = 10
                ch.SetValidComboInterval(300)

            if HackScalar != 0:
                if get_dword_time() - ch.GetLastMountTime() > 1500:
                    ch.IncreaseComboHackCount(1 + HackScalar)

                ch.SkipComboAttackByTime(ch.GetValidComboInterval())

            return HackScalar

        void CInputMain.Move(CHARACTER* ch, const char data[0])
            if not ch.CanMove():
                return

            pinfo = data

            if pinfo.bFunc >= EMoveFuncType.FUNC_MAX_NUM and (pinfo.bFunc & 0x80) == 0:
                #lani_err("invalid move type: %s", ch.GetName(LOCALE_LANIATUS))
                return

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
                fDist = DISTANCE_SQRT((ch.GetX() - pinfo.lX) / 100, (ch.GetY() - pinfo.lY) / 100)

                if ((LGEMiscellaneous.DEFINECONSTANTS.false == ch.IsRiding() and fDist > 25) or fDist > 40) and LGEMiscellaneous.DEFINECONSTANTS.OXEVENT_MAP_INDEX != ch.GetMapIndex():
                    #sys_log(0, "MOVE: %s trying to move too far (dist: %.1fm) Riding(%d)", ch.GetName(LOCALE_LANIATUS), fDist, ch.IsRiding())

                    ch.Show(ch.GetMapIndex(), ch.GetX(), ch.GetY(), ch.GetZ(), DefineConstants.false)
                    ch.Stop()
                    return

                    if ch.IsPC() and ch.IsDead():
                        #sys_log(0, "MOVE: %s trying to move as dead", ch.GetName(LOCALE_LANIATUS))
                        ch.Show(ch.GetMapIndex(), ch.GetX(), ch.GetY(), ch.GetZ(), DefineConstants.false)
                        ch.Stop()
                        return

                dwCurTime = get_dword_time()

                CheckSpeedHack = (LGEMiscellaneous.DEFINECONSTANTS.false == ch.GetDesc().IsHandshaking() and dwCurTime - ch.GetDesc().GetClientTime() > 7000)

                if CheckSpeedHack:
                    iDelta = int((pinfo.dwTime - ch.GetDesc().GetClientTime()))
                    iServerDelta = int((dwCurTime - ch.GetDesc().GetClientTime()))

                    iDelta = int((dwCurTime - pinfo.dwTime))

                    if iDelta >= 30000:
                        #sys_log(0, "SPEEDHACK: slow timer name %s delta %d", ch.GetName(LOCALE_LANIATUS), iDelta)
                        ch.GetDesc().DelayedDisconnect(3)
                    elif iDelta < -(math.trunc(iServerDelta / float(50))):
                        #sys_log(0, "SPEEDHACK: DETECTED! %s (delta %d %d)", ch.GetName(LOCALE_LANIATUS), iDelta, iServerDelta)
                        ch.GetDesc().DelayedDisconnect(3)

                if pinfo.bFunc == EMoveFuncType.FUNC_COMBO and g_bCheckMultiHack:
                    CheckComboHack(ch, pinfo.bArg, pinfo.dwTime, CheckSpeedHack)

            if pinfo.bFunc == EMoveFuncType.FUNC_MOVE:
                if ch.GetLimitPoint(EPointTypes.LG_POINT_MOV_SPEED) == 0:
                    return

                ch.SetRotation(pinfo.bRot * 5)
                ch.ResetStopTime()

                ch.Goto(pinfo.lX, pinfo.lY)
            else:
                if pinfo.bFunc == EMoveFuncType.FUNC_ATTACK or pinfo.bFunc == EMoveFuncType.FUNC_COMBO:
                    ch.OnMove(((not LGEMiscellaneous.DEFINECONSTANTS.false)))
                elif (pinfo.bFunc & byte(EMoveFuncType.FUNC_SKILL)) != 0:
                    MASK_LG_SKILL_MOTION = 0x7F
                    motion = uint(pinfo.bFunc & MASK_LG_SKILL_MOTION)

                    if not ch.IsUsableSkillMotion(motion):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to pointers to value types:
#ORIGINAL METINII C CODE: const char* name = ch->GetName();
                        name = ch.GetName(LOCALE_LANIATUS)
                        job = ch.GetJob()
                        group = ch.GetSkillGroup()

                        szBuf = str(['\0' for _ in range(256)])
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                        snprintf(szBuf, sizeof(szBuf), "LG_SKILL_HACK: name=%s, job=%d, group=%d, motion=%d", name, job, group, motion)
                        LogManager.instance().HackLog(ch.GetAID(), ch.GetName(LOCALE_LANIATUS), "SKILLHACK")
                        #sys_log(0, "%s", szBuf)

                        if test_server:
                            ch.GetDesc().DelayedDisconnect(number(2, 8))
                            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, szBuf)
                        else:
                            ch.GetDesc().DelayedDisconnect(number(150, 500))

                    ch.OnMove(DefineConstants.false)

                ch.SetRotation(pinfo.bRot * 5)
                ch.ResetStopTime()

                ch.Move(pinfo.lX, pinfo.lY)
                ch.Stop()
                ch.StopStaminaConsume()

            pack = packet_move()

            pack.bHeader = byte(LG_HEADER_GC_MOVE)
            pack.bFunc = pinfo.bFunc
            pack.bArg = pinfo.bArg
            pack.bRot = pinfo.bRot
            pack.dwVID = ch.GetVID()
            pack.lX = pinfo.lX
            pack.lY = pinfo.lY
            pack.dwTime = pinfo.dwTime
            pack.dwDuration = ch.GetCurrentMoveDuration() if (pinfo.bFunc == EMoveFuncType.FUNC_MOVE) else 0

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            ch.PacketAround(pack, sizeof(packet_move), ch)

        void CInputMain.Attack(CHARACTER* ch, const byte header, const chardata[0])
            if None is ch:
                return

            struct type_identifier
                header = None
                type = None

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no equivalent to 'reinterpret_cast' in Python:
            type = reinterpret_cast<const struct type_identifier>(data)

            if type.type > 0:
                if LGEMiscellaneous.DEFINECONSTANTS.false == ch.CanUseSkill(type.type):
                    return

                if (type.type == LaniatusETalentXes.LG_SKILL_GEOMPUNG) or (type.type == LaniatusETalentXes.LG_SKILL_SANGONG) or (type.type == LaniatusETalentXes.LG_SKILL_YEONSA) or (type.type == LaniatusETalentXes.LG_SKILL_KWANKYEOK) or (type.type == LaniatusETalentXes.LG_SKILL_HWAJO) or (type.type == LaniatusETalentXes.LG_SKILL_GIGUNG) or (type.type == LaniatusETalentXes.LG_SKILL_PABEOB) or (type.type == LaniatusETalentXes.LG_SKILL_MARYUNG) or (type.type == LaniatusETalentXes.LG_SKILL_TUSOK) or (type.type == LaniatusETalentXes.LG_SKILL_MAHWAN) or (type.type == LaniatusETalentXes.LG_SKILL_BIPABU) or (type.type == LaniatusETalentXes.LG_SKILL_NOEJEON) or (type.type == LaniatusETalentXes.LG_SKILL_CHAIN) or (type.type == LaniatusETalentXes.LG_SKILL_HORSE_WILDATTACK_RANGE):
                    if LG_HEADER_CG_SHOOT != type.header:
                        if test_server:
                            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Attack :name[%s] Vnum[%d] can't use skill by attack(warning)"), type.type)
                        return

            if header == LG_HEADER_CG_ATTACK:
                    if None is ch.GetDesc():
                        return

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no equivalent to 'reinterpret_cast' in Python:
                    packMelee = reinterpret_cast<const command_attack>(data)

                    ch.GetDesc().AssembleCRCMagicCube(packMelee.bCRCMagicCubeProcPiece, packMelee.bCRCMagicCubeFilePiece)

                    victim = CHARACTER_MANAGER.instance().Find(packMelee.dwVID)

                    if None is victim or ch is victim:
                        return

                    if (victim.GetCharType() == ECharType.CHAR_TYPE_NPC) or (victim.GetCharType() == ECharType.CHAR_TYPE_WARP) or (victim.GetCharType() == ECharType.CHAR_TYPE_GOTO):
                        return

                    if packMelee.bType > 0:
                        if LGEMiscellaneous.DEFINECONSTANTS.false == ch.CheckSkillHitCount(packMelee.bType, victim.GetVID()):
                            return

                    ch.Attack(victim, packMelee.bType)

            if (header == LG_HEADER_CG_ATTACK) or (header == LG_HEADER_CG_SHOOT):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no equivalent to 'reinterpret_cast' in Python:
                    packShoot = reinterpret_cast<const packet_shoot>(data)

                    ch.Shoot(packShoot.bType)

        int CInputMain.SyncPosition(CHARACTER* ch, const char * c_pcData, int uiBytes)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no equivalent to 'reinterpret_cast' in Python:
            pinfo = reinterpret_cast<const command_sync_position>(c_pcData)

            if uiBytes < pinfo.wSize:
                return -1

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            iExtraLen = pinfo.wSize - sizeof(command_sync_position)

            if iExtraLen < 0:
                #lani_err("invalid packet length (len %d size %u buffer %u)", iExtraLen, pinfo.wSize, uiBytes)
                ch.GetDesc().SetPhase(EPhase.PHASE_CLOSE)
                return -1

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            if 0 != (math.fmod(iExtraLen, sizeof(command_sync_position_element))):
                #lani_err("invalid packet length %d (name: %s)", pinfo.wSize, ch.GetName(LOCALE_LANIATUS))
                return iExtraLen

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            iCount = iExtraLen / sizeof(command_sync_position_element)

            if iCount <= 0:
                return iExtraLen

            NCOUNTLIMIT = 16

            if iCount > NCOUNTLIMIT:
                #lani_err("Too many SyncPosition Count(%d) from Name(%s)", iCount, ch.GetName(LOCALE_LANIATUS))
                iCount = NCOUNTLIMIT

            tbuf = TEMP_BUFFER(8192, DefineConstants.false)
            lpBuf = tbuf.getptr()

            pHeader = buffer_write_peek(lpBuf)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            buffer_write_proceed(lpBuf, sizeof(packet_sync_position))

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Pointer arithmetic is detected on this variable:
#ORIGINAL METINII C CODE: const command_sync_position_element* e = reinterpret_cast<const command_sync_position_element*>(c_pcData + sizeof(command_sync_position));
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no equivalent to 'reinterpret_cast' in Python:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            e = reinterpret_cast<const command_sync_position_element>(c_pcData + sizeof(command_sync_position))

            tvCurTime = timeval()
            gettimeofday(tvCurTime, None)

            i = 0
            while i < iCount:
                victim = CHARACTER_MANAGER.instance().Find(e.dwVID)

                if victim is None:
                    continue

                if (victim.GetCharType() == ECharType.CHAR_TYPE_NPC) or (victim.GetCharType() == ECharType.CHAR_TYPE_WARP) or (victim.GetCharType() == ECharType.CHAR_TYPE_GOTO):
                    continue

                if not victim.SetSyncOwner(ch, ((not DefineConstants.false))):
                    continue

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
                fDistWithSyncOwner = DISTANCE_SQRT((victim.GetX() - ch.GetX()) / 100, (victim.GetY() - ch.GetY()) / 100)
                fLimitDistWithSyncOwner = 2500.0 + 1000.0

                if fDistWithSyncOwner > fLimitDistWithSyncOwner:
                    if ch.GetSyncHackCount() < g_iSyncHackLimitCount:
                        ch.SetSyncHackCount(ch.GetSyncHackCount() + 1)
                        continue
                    else:
                        LogManager.instance().HackLog(ch.GetAID(), ch.GetName(LOCALE_LANIATUS), "SYNC_POSITION_HACK")

                        #lani_err("Too far SyncPosition DistanceWithSyncOwner(%f)(%s) from Name(%s) CH(%d,%d) VICTIM(%d,%d) SYNC(%d,%d)", fDistWithSyncOwner, victim.GetName(LOCALE_LANIATUS), ch.GetName(LOCALE_LANIATUS), ch.GetX(), ch.GetY(), victim.GetX(), victim.GetY(), e.lX, e.lY)

                        ch.GetDesc().SetPhase(EPhase.PHASE_CLOSE)

                        return -1

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
                fDist = DISTANCE_SQRT((victim.GetX() - e.lX) / 100, (victim.GetY() - e.lY) / 100)
                G_LVALIDSYNCINTERVAL = 50 * 1000
                tvLastSyncTime = victim.GetLastSyncTime()
                tvDiff = timediff(tvCurTime, tvLastSyncTime)

                if tvDiff.tv_sec == 0 and tvDiff.tv_usec < G_LVALIDSYNCINTERVAL:
                    if ch.GetSyncHackCount() < g_iSyncHackLimitCount:
                        ch.SetSyncHackCount(ch.GetSyncHackCount() + 1)
                        continue
                    else:
                        LogManager.instance().HackLog(ch.GetAID(), ch.GetName(LOCALE_LANIATUS), "SYNC_POSITION_HACK")

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
                        #lani_err("Too often SyncPosition Interval(%ldms)(%s) from Name(%s) VICTIM(%d,%d) SYNC(%d,%d)", tvDiff.tv_sec * 1000 + tvDiff.tv_usec / 1000, victim.GetName(LOCALE_LANIATUS), ch.GetName(LOCALE_LANIATUS), victim.GetX(), victim.GetY(), e.lX, e.lY)

                        ch.GetDesc().SetPhase(EPhase.PHASE_CLOSE)

                        return -1
                elif fDist > 25.0:
                    LogManager.instance().HackLog(ch.GetAID(), ch.GetName(LOCALE_LANIATUS), "SYNC_POSITION_HACK")

                    #lani_err("Too far SyncPosition Distance(%f)(%s) from Name(%s) CH(%d,%d) VICTIM(%d,%d) SYNC(%d,%d)", fDist, victim.GetName(LOCALE_LANIATUS), ch.GetName(LOCALE_LANIATUS), ch.GetX(), ch.GetY(), victim.GetX(), victim.GetY(), e.lX, e.lY)

                    ch.GetDesc().SetPhase(EPhase.PHASE_CLOSE)

                    return -1
                else:
                    victim.SetLastSyncTime(tvCurTime)
                    victim.Sync(e.lX, e.lY)
                    temp_ref_lpBuf = RefObject(lpBuf);
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
#ORIGINAL METINII C CODE: buffer_write(lpBuf, e, sizeof(command_sync_position_element));
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                    buffer_write(temp_ref_lpBuf, command_sync_position_element(e), sizeof(command_sync_position_element))
                    lpBuf = temp_ref_lpBuf.arg_value
                i += 1
                e += 1

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            if buffer_size(lpBuf) != sizeof(packet_sync_position):
                pHeader.bHeader = byte(LG_HEADER_GC_SYNC_POSITION)
                pHeader.wSize = ushort(buffer_size(lpBuf))

                ch.PacketAround(buffer_read_peek(lpBuf), buffer_size(lpBuf), ch)

            return iExtraLen

        void CInputMain.FlyTarget(CHARACTER* ch, const char * pcData, byte bHeader)
            p = pcData
            ch.FlyTarget(p.dwTargetVID, p.x, p.y, bHeader)

        void CInputMain.UseSkill(CHARACTER* ch, const char * pcData)
            p = pcData
            ch.UseSkill(p.dwVnum, CHARACTER_MANAGER.instance().Find(p.dwVID), ((not DefineConstants.false)))

        void CInputMain.ScriptButton(CHARACTER* ch, const object* c_pData)
            p = c_pData
            #sys_log(0, "QUEST ScriptButton pid %d idx %u", ch.GetPlayerID(), p.idx)

            pc = quest.CQuestManager.instance().GetPCForce(ch.GetPlayerID())
            if pc is not None and pc.IsConfirmWait():
                quest.CQuestManager.instance().Confirm(ch.GetPlayerID(), quest.EQuestConfirmType.CONFIRM_TIMEOUT, 0)
            elif (p.idx & 0x80000000) != 0:
                quest.CQuestManager.Instance().QuestInfo(ch.GetPlayerID(), p.idx & 0x7fffffff)
            else:
                quest.CQuestManager.Instance().QuestButton(ch.GetPlayerID(), p.idx)

        void CInputMain.ScriptAnswer(CHARACTER* ch, const object* c_pData)
            p = c_pData
            #sys_log(0, "QUEST ScriptAnswer pid %d answer %d", ch.GetPlayerID(), p.answer)

            if p.answer > 250:
                quest.CQuestManager.Instance().Resume(ch.GetPlayerID())
            else:
                quest.CQuestManager.Instance().Select(ch.GetPlayerID(), p.answer)

        void CInputMain.ScriptSelectItem(CHARACTER* ch, const object* c_pData)
            p = c_pData
            #sys_log(0, "QUEST ScriptSelectItem pid %d answer %d", ch.GetPlayerID(), p.selection)
            quest.CQuestManager.Instance().SelectItem(ch.GetPlayerID(), p.selection)

        void CInputMain.QuestInputString(CHARACTER* ch, const object* c_pData)
            p = c_pData

            msg = str(['\0' for _ in range(65)])
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            strncpy_s(msg, sizeof(msg), p.msg, _TRUNCATE)
            #sys_log(0, "QUEST InputString pid %u msg %s", ch.GetPlayerID(), msg)

            quest.CQuestManager.Instance().Input(ch.GetPlayerID(), msg)

        void CInputMain.QuestConfirm(CHARACTER* ch, const object* c_pData)
            p = c_pData
            ch_wait = CHARACTER_MANAGER.instance().FindByPID(p.requestPID)
            if p.answer != 0:
                p.answer = quest.EQuestConfirmType.CONFIRM_YES
            #sys_log(0, "QuestConfirm from %s pid %u name %s answer %d", ch.GetName(LOCALE_LANIATUS), p.requestPID,ch_wait.GetName(LOCALE_LANIATUS) if (ch_wait) is not None ) else "", p.answer)
            if ch_wait:
                quest.CQuestManager.Instance().Confirm(ch_wait.GetPlayerID(), p.answer, ch.GetPlayerID())

        void CInputMain.Target(CHARACTER* ch, const char * pcData)
            p = pcData

            pkObj = building.CManager.instance().FindObjectByVID(p.dwVID)

            if pkObj:
                pckTarget = packet_target()
                pckTarget.header = byte(LG_HEADER_GC_TARGET)
                pckTarget.dwVID = p.dwVID
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                ch.GetDesc().Packet(pckTarget, sizeof(packet_target))
            else:
                ch.SetTarget(CHARACTER_MANAGER.instance().Find(p.dwVID))

        void CInputMain.Warp(CHARACTER* ch, const char * pcData)
            ch.WarpEnd()

        void CInputMain.SafeboxCheckin(CHARACTER* ch, const char * c_pData)
            if quest.CQuestManager.instance().GetPCForce(ch.GetPlayerID()).IsRunning() == ((not LGEMiscellaneous.DEFINECONSTANTS.false)):
                return

            p = c_pData

            if not ch.CanHandleItem(DefineConstants.false, DefineConstants.false):
                return

            pkSafebox = ch.GetSafebox()
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
#ORIGINAL METINII C CODE: CItem* pkItem = ch->GetItem(p->ItemPos);
            pkItem = ch.GetItem(SItemPos(p.ItemPos))

            if pkSafebox is None or pkItem is None:
                return

            if pkItem.GetType() == EItemTypes.ITEM_BELT and pkItem.IsEquipped():

                ch.ChatPacket(EChatType.CHAT_TYPE_INFO, "Empty your belt before inventory !")
                return

            ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'IS_SET' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
            if pkItem.GetCell() >= LGEMiscellaneous.INVENTORY_MAX_NUM and IS_SET(pkItem.GetFlag(), EItemFlag.ITEM_FLAG_IRREMOVABLE):
                ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Storage> Cannot move items in safebox."))
                return

            if not pkSafebox.IsEmpty(p.bSafePos, pkItem.GetSize()):
                ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Storages> No movement possible."))
                return

            if pkItem.GetVnum() == UNIQUE_ITEM_SAFEBOX_EXPAND:
                ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Storages> The Item cannot be stored."))
                return

            ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'IS_SET' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
            if IS_SET(pkItem.GetAntiFlag(), LaniatusEITMAntiFlagDcs.ITEM_ANTIFLAG_SAFEBOX):
                ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Storages> The Item cannot be stored."))
                return

            if ((not LGEMiscellaneous.DEFINECONSTANTS.false)) == pkItem.isLocked():
                ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Storages> The Item cannot be stored."))
                return

            pkItem.RemoveFromCharacter()
            if not pkItem.IsDragonSoul():
                ch.SyncQuickslot(byte(LG_QUICKSLOT_TYPE_ITEM), byte(p.ItemPos.cell), 255)
            pkSafebox.Add(p.bSafePos, pkItem)

        void CInputMain.SafeboxCheckout(CHARACTER* ch, const char * c_pData, bool bMall)
            p = c_pData

            if not ch.CanHandleItem(DefineConstants.false, DefineConstants.false):
                return

            pkSafebox = None

            if bMall:
                pkSafebox = ch.GetMall()
            else:
                pkSafebox = ch.GetSafebox()

            if pkSafebox is None:
                return

            pkItem = pkSafebox.Get(p.bSafePos)

            if pkItem is None:
                return

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
#ORIGINAL METINII C CODE: if (!ch->IsEmptyItemGrid(p->ItemPos, pkItem->GetSize()))
            if not ch.IsEmptyItemGrid(SItemPos(p.ItemPos), pkItem.GetSize(), -1):
                return

            belt_index = BELT_INVENTORY_SLOT_START
            while belt_index < LGEMiscellaneous2.BELT_INVENTORY_SLOT_END:
                if pkItem.GetType() != 3 and p.ItemPos.cell == belt_index:
                    if pkItem.GetSubType() != 0 or pkItem.GetSubType() != 11 or pkItem.GetSubType() != 7:
                        return
                belt_index += 1

            if pkItem.IsDragonSoul():
                if bMall:
                    DSManager.instance().DragonSoulItemInitialize(pkItem)

                if EWindows.DRAGON_SOUL_INVENTORY != p.ItemPos.window_type:
                    ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Storages> No movement possible."))
                    return

                DestPos = p.ItemPos
                if not DSManager.instance().IsValidCellForThisItem(pkItem, DestPos):
                    iCell = ch.GetEmptyDragonSoulInventory(pkItem)
                    if iCell < 0:
                        ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Storages> No movement possible."))
                        return
                    DestPos = TItemPos(EWindows.DRAGON_SOUL_INVENTORY, iCell)

                pkSafebox.Remove(p.bSafePos)
                pkItem.AddToCharacter(ch, TItemPos(DestPos))
                ITEM_MANAGER.instance().FlushDelayedSave(pkItem)
            else:
                if EWindows.DRAGON_SOUL_INVENTORY == p.ItemPos.window_type:
                    ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Storages> No movement possible."))
                    return

                pkSafebox.Remove(p.bSafePos)
                if bMall:
                    if None is pkItem.GetProto():
                        #lani_err("pkItem->GetProto() == NULL (id : %d)",pkItem.GetID())
                        return

                    if 100 == pkItem.GetProto().bAlterToMagicItemPct and 0 == pkItem.GetAttributeCount():
                        pkItem.AlterToMagicItem(0, 0)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
#ORIGINAL METINII C CODE: pkItem->AddToCharacter(ch, p->ItemPos);
                pkItem.AddToCharacter(ch, SItemPos(p.ItemPos))
                ITEM_MANAGER.instance().FlushDelayedSave(pkItem)

            dwID = pkItem.GetID()
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            db_clientdesc.DBPacketHeader(LG_HEADER_GD_ITEM_FLUSH, 0, sizeof(uint))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            db_clientdesc.Packet(dwID, sizeof(uint))

        void CInputMain.SafeboxItemMove(CHARACTER* ch, const char data[0])
            pinfo = data

            if not ch.CanHandleItem(DefineConstants.false, DefineConstants.false):
                return

            if ch.GetSafebox() is None:
                return

            ch.GetSafebox().MoveItem(byte(pinfo.Cell.cell), byte(pinfo.CellTo.cell), pinfo.count)

        void CInputMain.PartyInvite(CHARACTER* ch, const char * c_pData)
            p = c_pData
            pInvitee = CHARACTER_MANAGER.instance().Find(p.vid)

            if ch is None:
                return

            if pInvitee is None or ch.GetDesc() is None or pInvitee.GetDesc() is None or (not pInvitee.IsPC()) or not ch.IsPC():
                #lani_err("PARTY Cannot find invited character")
                return

            ch.PartyInvite(pInvitee)

        void CInputMain.PartyInviteAnswer(CHARACTER* ch, const char * c_pData)
            p = c_pData
            pInviter = CHARACTER_MANAGER.instance().Find(p.leader_vid)

            if ch is None:
                return

            if pInviter is None or not pInviter.IsPC():
                ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Group> The player who invited is not online."))
            elif p.accept == 0:
                pInviter.PartyInviteDeny(ch.GetPlayerID())
            else:
                pInviter.PartyInviteAccept(ch)

        void CInputMain.PartySetState(CHARACTER* ch, const char* c_pData)
            if not CPartyManager.instance().IsEnablePCParty():
                ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Group> The server cannot execute the Group request."))
                return

            p = c_pData

            if ch.GetParty() is None:
                return

            if ch.GetParty().GetLeaderPID() != ch.GetPlayerID():
                ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Group> Only the Group leader can change this."))
                return

            if not ch.GetParty().IsMember(p.pid):
                ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Group> The target is no member of your Group."))
                return

            pid = p.pid
            #sys_log(0, "PARTY SetRole pid %d to role %d state %s", pid, p.byRole,"on" if p.flag != 0 else "off")

            if p.byRole == EPartyRole.PARTY_ROLE_NORMAL:
                pass

            elif (p.byRole == EPartyRole.PARTY_ROLE_ATTACKER) or (p.byRole == EPartyRole.PARTY_ROLE_TANKER) or (p.byRole == EPartyRole.PARTY_ROLE_BUFFER) or (p.byRole == EPartyRole.PARTY_ROLE_LG_SKILL_MASTER) or (p.byRole == EPartyRole.PARTY_ROLE_HASTE) or (p.byRole == EPartyRole.PARTY_ROLE_DEFENDER):
                if ch.GetParty().SetRole(pid, p.byRole, p.flag != 0):
                    pack = SPacketPartyStateChange()
                    pack.dwLeaderPID = ch.GetPlayerID()
                    pack.dwPID = p.pid
                    pack.bRole = p.byRole
                    pack.bFlag = p.flag
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                    db_clientdesc.DBPacket(LG_HEADER_GD_PARTY_STATE_CHANGE, 0, pack, sizeof(pack))

            else:
                #lani_err("wrong byRole in PartySetState Packet name %s state %d", ch.GetName(LOCALE_LANIATUS), p.byRole)

        void CInputMain.PartyRemove(CHARACTER* ch, const char* c_pData)
            if not CPartyManager.instance().IsEnablePCParty():
                ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Group> The server cannot execute the Group request."))
                return

            if ch.GetDungeon():
                ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Group> You cannot kick a player while you are in a dungeon."))
                return

            p = c_pData

            if ch.GetParty() is None:
                return

            pParty = ch.GetParty()
            if pParty.GetLeaderPID() == ch.GetPlayerID():
                if ch.GetDungeon():
                    ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Group> You cannot kick a player while you are in a dungeon."))
                else:
                    if p.pid == ch.GetPlayerID() or pParty.GetMemberCount() == 2:
                        CPartyManager.instance().DeleteParty(pParty)
                    else:
                        B = CHARACTER_MANAGER.instance().FindByPID(p.pid)
                        if B:
                            B.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Group> You were kicked from the Group."))
                        pParty.Quit(p.pid)
            else:
                if p.pid == ch.GetPlayerID():
                    if ch.GetDungeon():
                        ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Group> You cannot leave a Group while being in a dungeon."))
                    else:
                        if pParty.GetMemberCount() == 2:
                            CPartyManager.instance().DeleteParty(pParty)
                        else:
                            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Group> You left the Group."))
                            pParty.Quit(ch.GetPlayerID())
                else:
                    ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Group> You cannot kick Group members."))

        void CInputMain.AnswerMakeGuild(CHARACTER* ch, const char* c_pData)
            p = c_pData

            if ch.GetGold() < 200000:
                return

            if get_global_time() - ch.GetQuestFlag("guild_manage.new_disband_time") < CGuildManager.instance().GetDisbandDelay():
                ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> After the deletion of the Guild, you cannot create a new one for %d days."), quest.CQuestManager.instance().GetEventFlag("guild_disband_delay"))
                return

            if get_global_time() - ch.GetQuestFlag("guild_manage.new_withdraw_time") < CGuildManager.instance().GetWithdrawDelay():
                ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> You cannot create a new guild for %d days."), quest.CQuestManager.instance().GetEventFlag("guild_withdraw_delay"))
                return

            if ch.GetGuild():
                return

            gm = CGuildManager.instance()

            cp = TGuildCreateParameter()
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            memset(cp, 0, sizeof(cp))

            cp.master = ch
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            strncpy_s(cp.name, sizeof(cp.name), p.guild_name, _TRUNCATE)

            if cp.name[0] == 0 or not check_name(cp.name):
                ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("This Guild name is invalid"))
                return

            dwGuildID = gm.CreateGuild(cp)

            if dwGuildID != 0:
                ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> [%s] Guild was created."), cp.name)

                GuildCreateFee = None
                GuildCreateFee = 200000

                ch.PointChange(EPointTypes.LG_POINT_GOLD, -GuildCreateFee, DefineConstants.false, DefineConstants.false)
            else:
                ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> Creation of Guild failed."))

        void CInputMain.PartyUseSkill(CHARACTER* ch, const char* c_pData)
            p = c_pData
            if ch.GetParty() is None:
                return

            if ch.GetPlayerID() != ch.GetParty().GetLeaderPID():
                ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Group> Only the Group leader can use Group Skills."))
                return

            if p.bySkillIndex == PARTY_LG_SKILL_HEAL:
                ch.GetParty().HealParty()
            elif p.bySkillIndex == PARTY_LG_SKILL_WARP:
                    pch = CHARACTER_MANAGER.instance().Find(p.vid)
                    if pch is not None and pch.IsPC():
                        ch.GetParty().SummonToLeader(pch.GetPlayerID())
                    else:
                        ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Group> The target was not found."))

        void CInputMain.PartyParameter(CHARACTER* ch, const char * c_pData)
            p = c_pData

            if ch.GetParty() is not None and ch.GetParty().GetLeaderPID() == ch.GetPlayerID():
                ch.GetParty().SetParameter(p.bDistributeMode)

        int GetSubPacketSize(const GUILD_SUBLG_HEADER_CG& header)
            if header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_DEPOSIT_MONEY:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                return sizeof(int)
            if (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_DEPOSIT_MONEY) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_WITHDRAW_MONEY):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                return sizeof(int)
            if (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_DEPOSIT_MONEY) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_WITHDRAW_MONEY) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_ADD_MEMBER):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                return sizeof(uint)
            if (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_DEPOSIT_MONEY) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_WITHDRAW_MONEY) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_ADD_MEMBER) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_REMOVE_MEMBER):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                return sizeof(uint)
            if (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_DEPOSIT_MONEY) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_WITHDRAW_MONEY) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_ADD_MEMBER) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_REMOVE_MEMBER) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_CHANGE_GRADE_NAME):
                return 10
            if (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_DEPOSIT_MONEY) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_WITHDRAW_MONEY) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_ADD_MEMBER) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_REMOVE_MEMBER) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_CHANGE_GRADE_NAME) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_CHANGE_GRADE_AUTHORITY):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                return sizeof(byte) + sizeof(byte)
            if (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_DEPOSIT_MONEY) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_WITHDRAW_MONEY) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_ADD_MEMBER) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_REMOVE_MEMBER) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_CHANGE_GRADE_NAME) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_CHANGE_GRADE_AUTHORITY) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_OFFER):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                return sizeof(uint)
            if (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_DEPOSIT_MONEY) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_WITHDRAW_MONEY) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_ADD_MEMBER) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_REMOVE_MEMBER) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_CHANGE_GRADE_NAME) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_CHANGE_GRADE_AUTHORITY) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_OFFER) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_CHARGE_GSP):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                return sizeof(int)
            if (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_DEPOSIT_MONEY) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_WITHDRAW_MONEY) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_ADD_MEMBER) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_REMOVE_MEMBER) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_CHANGE_GRADE_NAME) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_CHANGE_GRADE_AUTHORITY) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_OFFER) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_CHARGE_GSP) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_POST_COMMENT):
                return 1
            if (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_DEPOSIT_MONEY) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_WITHDRAW_MONEY) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_ADD_MEMBER) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_REMOVE_MEMBER) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_CHANGE_GRADE_NAME) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_CHANGE_GRADE_AUTHORITY) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_OFFER) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_CHARGE_GSP) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_POST_COMMENT) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_DELETE_COMMENT):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                return sizeof(uint)
            if (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_DEPOSIT_MONEY) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_WITHDRAW_MONEY) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_ADD_MEMBER) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_REMOVE_MEMBER) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_CHANGE_GRADE_NAME) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_CHANGE_GRADE_AUTHORITY) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_OFFER) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_CHARGE_GSP) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_POST_COMMENT) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_DELETE_COMMENT) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_REFRESH_COMMENT):
                return 0
            if (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_DEPOSIT_MONEY) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_WITHDRAW_MONEY) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_ADD_MEMBER) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_REMOVE_MEMBER) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_CHANGE_GRADE_NAME) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_CHANGE_GRADE_AUTHORITY) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_OFFER) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_CHARGE_GSP) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_POST_COMMENT) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_DELETE_COMMENT) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_REFRESH_COMMENT) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_CHANGE_MEMBER_GRADE):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                return sizeof(uint) + sizeof(byte)
            if (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_DEPOSIT_MONEY) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_WITHDRAW_MONEY) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_ADD_MEMBER) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_REMOVE_MEMBER) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_CHANGE_GRADE_NAME) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_CHANGE_GRADE_AUTHORITY) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_OFFER) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_CHARGE_GSP) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_POST_COMMENT) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_DELETE_COMMENT) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_REFRESH_COMMENT) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_CHANGE_MEMBER_GRADE) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_USE_SKILL):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                return sizeof(command_guild_use_skill)
            if (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_DEPOSIT_MONEY) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_WITHDRAW_MONEY) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_ADD_MEMBER) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_REMOVE_MEMBER) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_CHANGE_GRADE_NAME) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_CHANGE_GRADE_AUTHORITY) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_OFFER) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_CHARGE_GSP) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_POST_COMMENT) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_DELETE_COMMENT) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_REFRESH_COMMENT) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_CHANGE_MEMBER_GRADE) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_USE_SKILL) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_CHANGE_MEMBER_GENERAL):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                return sizeof(uint) + sizeof(byte)
            if (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_DEPOSIT_MONEY) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_WITHDRAW_MONEY) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_ADD_MEMBER) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_REMOVE_MEMBER) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_CHANGE_GRADE_NAME) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_CHANGE_GRADE_AUTHORITY) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_OFFER) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_CHARGE_GSP) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_POST_COMMENT) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_DELETE_COMMENT) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_REFRESH_COMMENT) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_CHANGE_MEMBER_GRADE) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_USE_SKILL) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_CHANGE_MEMBER_GENERAL) or (header == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_GUILD_INVITE_ANSWER):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                return sizeof(uint) + sizeof(byte)

            return 0

        int CInputMain.Guild(CHARACTER* ch, const char data[0], int uiBytes)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            if uiBytes < sizeof(command_guild):
                return -1

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no equivalent to 'reinterpret_cast' in Python:
            p = reinterpret_cast<const command_guild>(data)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to pointers to value types:
#ORIGINAL METINII C CODE: const char* c_pData = data + sizeof(command_guild);
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            c_pData = data + sizeof(command_guild)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            uiBytes -= sizeof(command_guild)

            SubHeader = p.subheader
            SubPacketLen = GetSubPacketSize(SubHeader)

            if uiBytes < SubPacketLen:
                return -1

            pGuild = ch.GetGuild()

            if None is pGuild:
                if SubHeader != GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_GUILD_INVITE_ANSWER:
                    ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> It does not belong to the Guild."))
                    return SubPacketLen

            if SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_DEPOSIT_MONEY:
                    return SubPacketLen

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no equivalent to 'reinterpret_cast' in Python:
                    gold = MIN(*reinterpret_cast<const int>(c_pData), __deposit_limit())

                    if gold < 0:
                        ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> That is not the correct Yang sum."))
                        return SubPacketLen

                    if ch.GetGold() < gold:
                        ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> You do not have enough Yang."))
                        return SubPacketLen

                    pGuild.RequestDepositMoney(ch, gold)
                return SubPacketLen

            if (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_DEPOSIT_MONEY) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_WITHDRAW_MONEY):
                    return SubPacketLen

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no equivalent to 'reinterpret_cast' in Python:
                    gold = MIN(*reinterpret_cast<const int>(c_pData), 500000)

                    if gold < 0:
                        ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> That is not the correct Yang sum."))
                        return SubPacketLen

                    pGuild.RequestWithdrawMoney(ch, gold)
                return SubPacketLen

            if (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_DEPOSIT_MONEY) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_WITHDRAW_MONEY) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_ADD_MEMBER):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no equivalent to 'reinterpret_cast' in Python:
                    vid = *reinterpret_cast<const uint>(c_pData)
                    newmember = CHARACTER_MANAGER.instance().Find(vid)

                    if newmember is None:
                        ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> The wanted person cannot be found."))
                        return SubPacketLen

                    if not newmember.IsPC():
                        return SubPacketLen

                    pGuild.Invite(ch, newmember)
                return SubPacketLen

            if (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_DEPOSIT_MONEY) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_WITHDRAW_MONEY) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_ADD_MEMBER) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_REMOVE_MEMBER):
                    if pGuild.UnderAnyWar(GUILD_WAR_TYPE_MAX_NUM) != 0:
                        ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> During a guild war, you cannot kick out other guild members."))
                        return SubPacketLen

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no equivalent to 'reinterpret_cast' in Python:
                    pid = *reinterpret_cast<const uint>(c_pData)
                    m = pGuild.GetMember(ch.GetPlayerID())

                    if None is m:
                        return -1

                    member = CHARACTER_MANAGER.instance().FindByPID(pid)

                    if member:
                        if member.GetGuild() is not pGuild:
                            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> This person is not in the same Guild."))
                            return SubPacketLen

                        if not pGuild.HasGradeAuth(m.grade, GUILD_AUTH_REMOVE_MEMBER):
                            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> You cannot kick Guild members."))
                            return SubPacketLen

                        member.SetQuestFlag("guild_manage.new_withdraw_time", get_global_time())
                        pGuild.RequestRemoveMember(member.GetPlayerID())
                    else:
                        if not pGuild.HasGradeAuth(m.grade, GUILD_AUTH_REMOVE_MEMBER):
                            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> You cannot kick Guild members."))
                            return SubPacketLen

                        if pGuild.RequestRemoveMember(pid):
                            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> You kicked a Guild member."))
                        else:
                            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> The wanted person cannot be found."))
                return SubPacketLen

            if (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_DEPOSIT_MONEY) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_WITHDRAW_MONEY) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_ADD_MEMBER) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_REMOVE_MEMBER) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_CHANGE_GRADE_NAME):
                    gradename = str(['\0' for _ in range(GUILD_GRADE_NAME_MAX_LEN + 1)])
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                    strncpy_s(gradename, sizeof(gradename), c_pData + 1, _TRUNCATE)

                    m = pGuild.GetMember(ch.GetPlayerID())

                    if None is m:
                        return -1

                    if m.grade != GUILD_LEADER_GRADE:
                        ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> You cannot change your Rank name."))
                    elif c_pData == GUILD_LEADER_GRADE:
                        ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> The name of the rank of the Guild master cannot be changed."))
                    elif not check_name(gradename):
                        ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> This Rank name is invalid."))
                    else:
                        pGuild.ChangeGradeName(c_pData, gradename)
                return SubPacketLen

            if (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_DEPOSIT_MONEY) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_WITHDRAW_MONEY) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_ADD_MEMBER) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_REMOVE_MEMBER) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_CHANGE_GRADE_NAME) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_CHANGE_GRADE_AUTHORITY):
                    m = pGuild.GetMember(ch.GetPlayerID())

                    if None is m:
                        return -1

                    if m.grade != GUILD_LEADER_GRADE:
                        ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> You cannot change your position."))
                    elif c_pData == GUILD_LEADER_GRADE:
                        ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> The powers of the Guild master cannot be changed."))
                    else:
                        pGuild.ChangeGradeAuth(c_pData, (c_pData + 1))
                return SubPacketLen

            if (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_DEPOSIT_MONEY) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_WITHDRAW_MONEY) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_ADD_MEMBER) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_REMOVE_MEMBER) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_CHANGE_GRADE_NAME) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_CHANGE_GRADE_AUTHORITY) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_OFFER):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no equivalent to 'reinterpret_cast' in Python:
                    offer = *reinterpret_cast<uint>(c_pData)

                    if pGuild.GetLevel() >= LGEMiscellaneous.GUILD_MAX_LEVEL:
                        ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> The Guild has already reached maximum level."))
                    else:
                        offer = math.trunc(offer / float(100))
                        offer *= 100

                        if pGuild.OfferExp(ch, int(offer)):
                            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> %u 's Experience used."), offer)
                        else:
                            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> Experience usage failed."))
                return SubPacketLen

            if (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_DEPOSIT_MONEY) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_WITHDRAW_MONEY) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_ADD_MEMBER) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_REMOVE_MEMBER) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_CHANGE_GRADE_NAME) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_CHANGE_GRADE_AUTHORITY) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_OFFER) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_CHARGE_GSP):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no equivalent to 'reinterpret_cast' in Python:
                    offer = *reinterpret_cast<const int>(c_pData)
                    gold = offer * 100

                    if offer < 0 or gold < offer or gold < 0 or ch.GetGold() < gold:
                        ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> Not enough Yang."))
                        return SubPacketLen

                    if not pGuild.ChargeSP(ch, offer):
                        ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> Dragon ghost was not restored."))
                return SubPacketLen

            if (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_DEPOSIT_MONEY) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_WITHDRAW_MONEY) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_ADD_MEMBER) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_REMOVE_MEMBER) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_CHANGE_GRADE_NAME) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_CHANGE_GRADE_AUTHORITY) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_OFFER) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_CHARGE_GSP) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_POST_COMMENT):
                    length = c_pData

                    if length > GUILD_COMMENT_MAX_LEN:
                        #lani_err("POST_COMMENT: %s comment too long (length: %u)", ch.GetName(LOCALE_LANIATUS), length)
                        ch.GetDesc().SetPhase(EPhase.PHASE_CLOSE)
                        return -1

                    if uiBytes < 1 + length:
                        return -1

                    m = pGuild.GetMember(ch.GetPlayerID())

                    if None is m:
                        return -1

                    if length != 0 and (not pGuild.HasGradeAuth(m.grade, GUILD_AUTH_NOTICE)) and *(c_pData + 1) == '!':
                        ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> You cannot make an announcement."))
                    else:
                        str = str(length, c_pData + 1)
                        pGuild.AddComment(ch, str)

                    return (1 + length)

            if (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_DEPOSIT_MONEY) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_WITHDRAW_MONEY) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_ADD_MEMBER) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_REMOVE_MEMBER) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_CHANGE_GRADE_NAME) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_CHANGE_GRADE_AUTHORITY) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_OFFER) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_CHARGE_GSP) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_POST_COMMENT) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_DELETE_COMMENT):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no equivalent to 'reinterpret_cast' in Python:
                    comment_id = *reinterpret_cast<const uint>(c_pData)

                    pGuild.DeleteComment(ch, comment_id)
                return SubPacketLen

            if (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_DEPOSIT_MONEY) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_WITHDRAW_MONEY) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_ADD_MEMBER) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_REMOVE_MEMBER) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_CHANGE_GRADE_NAME) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_CHANGE_GRADE_AUTHORITY) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_OFFER) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_CHARGE_GSP) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_POST_COMMENT) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_DELETE_COMMENT) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_REFRESH_COMMENT):
                pGuild.RefreshComment(ch)
                return SubPacketLen

            if (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_DEPOSIT_MONEY) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_WITHDRAW_MONEY) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_ADD_MEMBER) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_REMOVE_MEMBER) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_CHANGE_GRADE_NAME) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_CHANGE_GRADE_AUTHORITY) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_OFFER) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_CHARGE_GSP) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_POST_COMMENT) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_DELETE_COMMENT) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_REFRESH_COMMENT) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_CHANGE_MEMBER_GRADE):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no equivalent to 'reinterpret_cast' in Python:
                    pid = *reinterpret_cast<const uint>(c_pData)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                    grade = *(c_pData + sizeof(uint))
                    m = pGuild.GetMember(ch.GetPlayerID())

                    if None is m:
                        return -1

                    if m.grade != GUILD_LEADER_GRADE:
                        ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> You cannot change your position."))
                    elif ch.GetPlayerID() == pid:
                        ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> The rank of the Guild master cannot be changed."))
                    elif grade == 1:
                        ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> You cannot make yourself Guild master."))
                    else:
                        pGuild.ChangeMemberGrade(pid, grade)
                return SubPacketLen

            if (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_DEPOSIT_MONEY) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_WITHDRAW_MONEY) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_ADD_MEMBER) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_REMOVE_MEMBER) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_CHANGE_GRADE_NAME) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_CHANGE_GRADE_AUTHORITY) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_OFFER) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_CHARGE_GSP) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_POST_COMMENT) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_DELETE_COMMENT) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_REFRESH_COMMENT) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_CHANGE_MEMBER_GRADE) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_USE_SKILL):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no equivalent to 'reinterpret_cast' in Python:
                    p = reinterpret_cast<const command_guild_use_skill>(c_pData)

                    pGuild.UseSkill(p.dwVnum, ch, p.dwPID)
                return SubPacketLen

            if (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_DEPOSIT_MONEY) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_WITHDRAW_MONEY) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_ADD_MEMBER) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_REMOVE_MEMBER) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_CHANGE_GRADE_NAME) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_CHANGE_GRADE_AUTHORITY) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_OFFER) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_CHARGE_GSP) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_POST_COMMENT) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_DELETE_COMMENT) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_REFRESH_COMMENT) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_CHANGE_MEMBER_GRADE) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_USE_SKILL) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_CHANGE_MEMBER_GENERAL):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no equivalent to 'reinterpret_cast' in Python:
                    pid = *reinterpret_cast<const uint>(c_pData)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                    is_general = *(c_pData + sizeof(uint))
                    m = pGuild.GetMember(ch.GetPlayerID())

                    if None is m:
                        return -1

                    if m.grade != GUILD_LEADER_GRADE:
                        ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> You cannot choose the leader."))
                    else:
                        if not pGuild.ChangeMemberGeneral(pid, is_general):
                            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> You cannot choose more leaders."))
                return SubPacketLen

            if (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_DEPOSIT_MONEY) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_WITHDRAW_MONEY) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_ADD_MEMBER) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_REMOVE_MEMBER) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_CHANGE_GRADE_NAME) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_CHANGE_GRADE_AUTHORITY) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_OFFER) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_CHARGE_GSP) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_POST_COMMENT) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_DELETE_COMMENT) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_REFRESH_COMMENT) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_CHANGE_MEMBER_GRADE) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_USE_SKILL) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_CHANGE_MEMBER_GENERAL) or (SubHeader == GUILD_SUBLG_HEADER_CG.GUILD_SUBLG_HEADER_CG_GUILD_INVITE_ANSWER):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no equivalent to 'reinterpret_cast' in Python:
                    guild_id = *reinterpret_cast<const uint>(c_pData)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                    accept = *(c_pData + sizeof(uint))

                    g = CGuildManager.instance().FindGuild(guild_id)

                    if g:
                        if accept != 0:
                            g.InviteAccept(ch)
                        else:
                            g.InviteDeny(ch.GetPlayerID())
                return SubPacketLen


            return 0

        void CInputMain.Fishing(CHARACTER* ch, const char* c_pData)
            p = c_pData
            ch.SetRotation(p.dir * 5)
            ch.fishing()
            return

        void CInputMain.ItemGive(CHARACTER* ch, const char* c_pData)
            p = c_pData
            to_ch = CHARACTER_MANAGER.instance().Find(p.dwTargetVID)

            if to_ch:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
#ORIGINAL METINII C CODE: ch->GiveItem(to_ch, p->ItemPos);
                ch.GiveItem(to_ch, SItemPos(p.ItemPos))
            else:
                ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You cannot trade this Item."))

        void CInputMain.Hack(CHARACTER* ch, const char * c_pData)
            p = c_pData

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            buf = str(['\0' for _ in range(sizeof(p.szBuf))])
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            strncpy_s(buf, sizeof(buf), p.szBuf, _TRUNCATE)

            #lani_err("HACK_DETECT: %s %s", ch.GetName(LOCALE_LANIATUS), buf)

            ch.GetDesc().SetPhase(EPhase.PHASE_CLOSE)

        int CInputMain.MyShop(CHARACTER* ch, const char * c_pData, int uiBytes)
            p = c_pData
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            iExtraLen = p.wCount * sizeof(SShopItemTable)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            if uiBytes < sizeof(SPacketCGMyShop) + iExtraLen:
                return -1

            if ch.IsStun() or ch.IsDead():
                return (iExtraLen)

            if ch.GetExchange() is not None or ch.IsOpenSafebox() or ch.GetShopOwner() is not None or ch.IsCubeOpen() or ch.IsAcceWindowOpen():
                ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You cannot open a private shop as long as you trade with others."))
                return (iExtraLen)

            #sys_log(0, "MyShop count %d", p.wCount)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            ch.OpenMyShop(p.szSign, (c_pData + sizeof(SPacketCGMyShop)), p.wCount)
            return (iExtraLen)

        void CInputMain.Refine(CHARACTER* ch, const char* c_pData)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no equivalent to 'reinterpret_cast' in Python:
            p = reinterpret_cast<const SPacketCGRefine>(c_pData)

            if ch.GetExchange() is not None or ch.IsOpenSafebox() or ch.GetShopOwner() is not None or ch.GetMyShop() is not None or ch.IsCubeOpen() or ch.IsAcceWindowOpen():
                ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You cannot advance now."))
                ch.ClearRefineMode()
                return

            if p.type == 255:
                ch.ClearRefineMode()
                return

            if p.pos >= LGEMiscellaneous.INVENTORY_MAX_NUM:
                ch.ClearRefineMode()
                return

            item = ch.GetInventoryItem(p.pos)

            if item is None:
                ch.ClearRefineMode()
                return

            ch.SetRefineTime()

            if p.type == ERefineType.REFINE_TYPE_NORMAL:
                #sys_log(0, "refine_type_noraml")
                ch.DoRefine(item, DefineConstants.false)
            elif p.type == ERefineType.REFINE_TYPE_SCROLL or p.type == ERefineType.REFINE_TYPE_HYUNIRON or p.type == ERefineType.REFINE_TYPE_MUSIN or p.type == ERefineType.REFINE_TYPE_BDRAGON:
                #sys_log(0, "refine_type_scroll, ...")
                ch.DoRefineWithScroll(item)
            elif p.type == ERefineType.REFINE_TYPE_MONEY_ONLY:
                item = ch.GetInventoryItem(p.pos)

                if None is not item:
                    if 500 <= item.GetRefineSet():
                        LogManager.instance().HackLog(ch.GetAID(), ch.GetName(LOCALE_LANIATUS), "DEVIL_TOWER_REFINE_HACK")
                    else:
                        if ch.GetQuestFlag("deviltower_zone.can_refine") != 0:
                            if ch.DoRefine(item, ((not LGEMiscellaneous.DEFINECONSTANTS.false))):
                                ch.SetQuestFlag("deviltower_zone.can_refine", 0)
                        else:
                            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, "You can only be rewarded once for the Demon Tower Quest.")

            ch.ClearRefineMode()

        int GetAcceSubPacketSize(const ACCE_SUBLG_HEADER_CG& header)
            if header == ACCE_SUBLG_HEADER_CG.ACCE_SUBLG_HEADER_CG_REFINE_CHECKIN:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                return sizeof(command_acce_checkin)
            if (header == ACCE_SUBLG_HEADER_CG.ACCE_SUBLG_HEADER_CG_REFINE_CHECKIN) or (header == ACCE_SUBLG_HEADER_CG.ACCE_SUBLG_HEADER_CG_REFINE_CHECKOUT):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                return sizeof(command_acce_checkout)
            if (header == ACCE_SUBLG_HEADER_CG.ACCE_SUBLG_HEADER_CG_REFINE_CHECKIN) or (header == ACCE_SUBLG_HEADER_CG.ACCE_SUBLG_HEADER_CG_REFINE_CHECKOUT) or (header == ACCE_SUBLG_HEADER_CG.ACCE_SUBLG_HEADER_CG_REFINE_ACCEPT):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                return sizeof(command_acce_accept)
            if (header == ACCE_SUBLG_HEADER_CG.ACCE_SUBLG_HEADER_CG_REFINE_CHECKIN) or (header == ACCE_SUBLG_HEADER_CG.ACCE_SUBLG_HEADER_CG_REFINE_CHECKOUT) or (header == ACCE_SUBLG_HEADER_CG.ACCE_SUBLG_HEADER_CG_REFINE_ACCEPT) or (header == ACCE_SUBLG_HEADER_CG.ACCE_SUBLG_HEADER_CG_REFINE_CANCEL):
                return 0

            return 0

        int CInputMain.AcceRefine(CHARACTER* ch, const chardata[0], int uiBytes)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            if uiBytes < sizeof(command_acce):
                return -1

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no equivalent to 'reinterpret_cast' in Python:
            p = reinterpret_cast<const command_acce>(data)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to pointers to value types:
#ORIGINAL METINII C CODE: const char* c_pData = data + sizeof(command_acce);
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            c_pData = data + sizeof(command_acce)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            uiBytes -= sizeof(command_acce)

            SubHeader = p.subheader
            SubPacketLen = GetAcceSubPacketSize(SubHeader)

            if uiBytes < SubPacketLen:
                return -1

            if p.subheader == ACCE_SUBLG_HEADER_CG.ACCE_SUBLG_HEADER_CG_REFINE_CHECKIN:
                    subpkt = c_pData
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
#ORIGINAL METINII C CODE: ch->AcceRefineCheckin(subpkt->bAccePos, subpkt->ItemPos);
                    ch.AcceRefineCheckin(subpkt.bAccePos, SItemPos(subpkt.ItemPos))
                return SubPacketLen

            if (p.subheader == ACCE_SUBLG_HEADER_CG.ACCE_SUBLG_HEADER_CG_REFINE_CHECKIN) or (p.subheader == ACCE_SUBLG_HEADER_CG.ACCE_SUBLG_HEADER_CG_REFINE_CHECKOUT):
                    subpkt = c_pData

                    ch.AcceRefineCheckout(subpkt.bAccePos)

                return SubPacketLen

            if (p.subheader == ACCE_SUBLG_HEADER_CG.ACCE_SUBLG_HEADER_CG_REFINE_CHECKIN) or (p.subheader == ACCE_SUBLG_HEADER_CG.ACCE_SUBLG_HEADER_CG_REFINE_CHECKOUT) or (p.subheader == ACCE_SUBLG_HEADER_CG.ACCE_SUBLG_HEADER_CG_REFINE_ACCEPT):
                    subpkt = c_pData

                    ch.AcceRefineAccept(subpkt.windowType)

                return SubPacketLen

            if (p.subheader == ACCE_SUBLG_HEADER_CG.ACCE_SUBLG_HEADER_CG_REFINE_CHECKIN) or (p.subheader == ACCE_SUBLG_HEADER_CG.ACCE_SUBLG_HEADER_CG_REFINE_CHECKOUT) or (p.subheader == ACCE_SUBLG_HEADER_CG.ACCE_SUBLG_HEADER_CG_REFINE_ACCEPT) or (p.subheader == ACCE_SUBLG_HEADER_CG.ACCE_SUBLG_HEADER_CG_REFINE_CANCEL):
                ch.AcceRefineCancel()
                return SubPacketLen


            return 0

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if __MULTI_LANGUAGE_SYSTEM__
        void CInputMain.ChangeLanguage(CHARACTER* ch, byte bLanguage)
            if ch is None:
                return

            if ch.GetDesc() is None:
                return

            bCurrentLanguage = ch.GetDesc().GetLanguage()

            if bCurrentLanguage == bLanguage:
                return

            if bLanguage > LaniatusLocalization.LOCALE_LANIATUS and bLanguage < LaniatusLocalization.LOCALE_MAX_NUM:
                packet = SRequestChangeLanguage()
                packet.dwAID = ch.GetDesc().GetAccountTable().id
                packet.bLanguage = bLanguage

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                db_clientdesc.DBPacketHeader(LG_HEADER_GD_REQUEST_CHANGE_LANGUAGE, 0, sizeof(SRequestChangeLanguage))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                db_clientdesc.Packet(packet, sizeof(packet))

                ch.ChangeLanguage(bLanguage)
##endif

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if __EXTENDED_WHISPER_DETAILS__
        void CInputMain.WhisperDetails(CHARACTER* ch, const char* c_pData)
            CGWhisperDetails = c_pData

            if (not CGWhisperDetails.name[0]) != '\0':
                return

            GCWhisperDetails = SPacketGCWhisperDetails()
            GCWhisperDetails.header = byte(LG_HEADER_GC_WHISPER_DETAILS)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            GCWhisperDetails.name = CGWhisperDetails.name[0:sizeof(GCWhisperDetails.name) - 1]

            bLanguage = LaniatusLocalization.LOCALE_DEFAULT

            pkChr = CHARACTER_MANAGER.instance().FindPC(CGWhisperDetails.name)

            if pkChr is None:
                pkDesc = None
                pkCCI = P2P_MANAGER.instance().Find(CGWhisperDetails.name)

                if pkCCI:
                    pkDesc = pkCCI.pkDesc
                    if pkDesc:
                        bLanguage = pkCCI.bLanguage
            else:
                if pkChr.GetDesc():
                    bLanguage = pkChr.GetDesc().GetLanguage()

            GCWhisperDetails.bLanguage = bLanguage
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            ch.GetDesc().Packet(GCWhisperDetails, sizeof(GCWhisperDetails))
##endif

        int CInputMain.Analyze(DESC* d, byte bHeader, const char * c_pData)
            ch = None

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if (!(ch = d->GetCharacter()))
            if not(ch = d.GetCharacter()):
                #lani_err("no character on desc")
                d.SetPhase(EPhase.PHASE_CLOSE)
                return (0)

            iExtraLen = 0

            if test_server and bHeader != LG_HEADER_CG_MOVE:
                #sys_log(0, "CInputMain::Analyze() ==> Header [%d] ", bHeader)

            if bHeader == LG_HEADER_CG_PONG:
                Pong(d)

            elif bHeader == LG_HEADER_CG_TIME_SYNC:
                Handshake(d, c_pData)

            elif bHeader == LG_HEADER_CG_CHAT:
                if test_server:
                    pBuf = str(c_pData)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                    #sys_log(0, "%s", pBuf + sizeof(command_chat))

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((iExtraLen = Chat(ch, c_pData, m_iBufferLeft)) < 0)
                if (iExtraLen = Chat(ch, c_pData, m_iBufferLeft)) < 0:
                    return -1

            elif bHeader == LG_HEADER_CG_WHISPER:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((iExtraLen = Whisper(ch, c_pData, m_iBufferLeft)) < 0)
                if (iExtraLen = Whisper(ch, c_pData, m_iBufferLeft)) < 0:
                    return -1

            elif bHeader == LG_HEADER_CG_MOVE:
                Move(ch, c_pData)
                if 0 != g_stClientVersion.compare(d.GetClientVersion()):
                    ch.ChatPacket(EChatType.CHAT_TYPE_NOTICE, LC_TEXT("Client version error."))
                    d.DelayedDisconnect(20)
                    LogManager.instance().HackLog(ch.GetAID(), ch.GetName(LOCALE_LANIATUS), "WRONG CLIENT VERSION")

            elif bHeader == LG_HEADER_CG_CHARACTER_POSITION:
                Position(ch, c_pData)

            elif bHeader == LG_HEADER_CG_ITEM_USE:
                if not ch.IsObserverMode():
                    ItemUse(ch, c_pData)

            elif bHeader == LG_HEADER_CG_ITEM_DROP:
                if not ch.IsObserverMode():
                    ItemDrop(ch, c_pData)

            elif bHeader == LG_HEADER_CG_ITEM_DROP2:
                if not ch.IsObserverMode():
                    ItemDrop2(ch, c_pData)

            elif bHeader == LG_HEADER_CG_ITEM_DESTROY:
                if not ch.IsObserverMode():
                    ItemDestroy(ch, c_pData)

            elif bHeader == LG_HEADER_CG_ITEM_MOVE:
                if not ch.IsObserverMode():
                    ItemMove(ch, c_pData)

            elif bHeader == LG_HEADER_CG_ITEM_PICKUP:
                if not ch.IsObserverMode():
                    ItemPickup(ch, c_pData)

            elif bHeader == LG_HEADER_CG_ITEM_USE_TO_ITEM:
                if not ch.IsObserverMode():
                    ItemToItem(ch, c_pData)

            elif bHeader == LG_HEADER_CG_ITEM_GIVE:
                if not ch.IsObserverMode():
                    ItemGive(ch, c_pData)

            elif bHeader == LG_HEADER_CG_EXCHANGE:
                if not ch.IsObserverMode():
                    Exchange(ch, c_pData)

            elif (bHeader == LG_HEADER_CG_ATTACK) or (bHeader == LG_HEADER_CG_SHOOT):
                if not ch.IsObserverMode():
                    Attack(ch, bHeader, c_pData)

            elif bHeader == LG_HEADER_CG_USE_SKILL:
                if not ch.IsObserverMode():
                    UseSkill(ch, c_pData)

            elif bHeader == LG_HEADER_CG_LG_QUICKSLOT_ADD:
                QuickslotAdd(ch, c_pData)

            elif bHeader == LG_HEADER_CG_LG_QUICKSLOT_DEL:
                QuickslotDelete(ch, c_pData)

            elif bHeader == LG_HEADER_CG_LG_QUICKSLOT_SWAP:
                QuickslotSwap(ch, c_pData)

            elif bHeader == LG_HEADER_CG_SHOP:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((iExtraLen = Shop(ch, c_pData, m_iBufferLeft)) < 0)
                if (iExtraLen = Shop(ch, c_pData, m_iBufferLeft)) < 0:
                    return -1

            elif bHeader == LG_HEADER_CG_MESSENGER:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((iExtraLen = Messenger(ch, c_pData, m_iBufferLeft))<0)
                if (iExtraLen = Messenger(ch, c_pData, m_iBufferLeft))<0:
                    return -1

            elif bHeader == LG_HEADER_CG_ON_CLICK:
                OnClick(ch, c_pData)

            elif bHeader == LG_HEADER_CG_SYNC_POSITION:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((iExtraLen = SyncPosition(ch, c_pData, m_iBufferLeft)) < 0)
                if (iExtraLen = SyncPosition(ch, c_pData, m_iBufferLeft)) < 0:
                    return -1

            elif (bHeader == LG_HEADER_CG_ADD_FLY_TARGETING) or (bHeader == LG_HEADER_CG_FLY_TARGETING):
                FlyTarget(ch, c_pData, bHeader)

            elif bHeader == LG_HEADER_CG_SCRIPT_BUTTON:
                ScriptButton(ch, c_pData)

            elif bHeader == LG_HEADER_CG_SCRIPT_SELECT_ITEM:
                ScriptSelectItem(ch, c_pData)

            elif bHeader == LG_HEADER_CG_SCRIPT_ANSWER:
                ScriptAnswer(ch, c_pData)

            elif bHeader == LG_HEADER_CG_QUEST_INPUT_STRING:
                QuestInputString(ch, c_pData)

            elif bHeader == LG_HEADER_CG_QUEST_CONFIRM:
                QuestConfirm(ch, c_pData)

            elif bHeader == LG_HEADER_CG_TARGET:
                Target(ch, c_pData)

            elif bHeader == LG_HEADER_CG_WARP:
                Warp(ch, c_pData)

            elif bHeader == LG_HEADER_CG_SAFEBOX_CHECKIN:
                SafeboxCheckin(ch, c_pData)

            elif bHeader == LG_HEADER_CG_SAFEBOX_CHECKOUT:
                SafeboxCheckout(ch, c_pData, LGEMiscellaneous.DEFINECONSTANTS.false)

            elif bHeader == LG_HEADER_CG_SAFEBOX_ITEM_MOVE:
                SafeboxItemMove(ch, c_pData)

            elif bHeader == LG_HEADER_CG_MALL_CHECKOUT:
                SafeboxCheckout(ch, c_pData, ((not LGEMiscellaneous.DEFINECONSTANTS.false)))

            elif bHeader == LG_HEADER_CG_PARTY_INVITE:
                PartyInvite(ch, c_pData)

            elif bHeader == LG_HEADER_CG_PARTY_REMOVE:
                PartyRemove(ch, c_pData)

            elif bHeader == LG_HEADER_CG_PARTY_INVITE_ANSWER:
                PartyInviteAnswer(ch, c_pData)

            elif bHeader == LG_HEADER_CG_PARTY_SET_STATE:
                PartySetState(ch, c_pData)

            elif bHeader == LG_HEADER_CG_PARTY_USE_SKILL:
                PartyUseSkill(ch, c_pData)

            elif bHeader == LG_HEADER_CG_PARTY_PARAMETER:
                PartyParameter(ch, c_pData)

            elif bHeader == LG_HEADER_CG_ANSWER_MAKE_GUILD:
                AnswerMakeGuild(ch, c_pData)

            elif bHeader == LG_HEADER_CG_GUILD:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((iExtraLen = Guild(ch, c_pData, m_iBufferLeft)) < 0)
                if (iExtraLen = Guild(ch, c_pData, m_iBufferLeft)) < 0:
                    return -1

            elif bHeader == LG_HEADER_CG_FISHING:
                Fishing(ch, c_pData)

            elif bHeader == LG_HEADER_CG_HACK:
                Hack(ch, c_pData)

            elif bHeader == LG_HEADER_CG_MYSHOP:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((iExtraLen = MyShop(ch, c_pData, m_iBufferLeft)) < 0)
                if (iExtraLen = MyShop(ch, c_pData, m_iBufferLeft)) < 0:
                    return -1

            elif bHeader == LG_HEADER_CG_REFINE:
                Refine(ch, c_pData)

            elif bHeader == LG_HEADER_CG_CLIENT_VERSION:
                Version(ch, c_pData)

            elif bHeader == LG_HEADER_CG_DRAGON_SOUL_REFINE:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no equivalent to 'reinterpret_cast' in Python:
                    p = reinterpret_cast <SPacketCGDragonSoulRefine>(c_pData)
                    if p.bSubType == EPacketCGDragonSoulSubHeaderType.DS_SUB_LG_HEADER_CLOSE:
                        ch.DragonSoul_RefineWindow_Close()
                    elif p.bSubType == EPacketCGDragonSoulSubHeaderType.DS_SUB_LG_HEADER_DO_REFINE_GRADE:
                            DSManager.instance().DoRefineGrade(ch, p.ItemGrid)
                    elif p.bSubType == EPacketCGDragonSoulSubHeaderType.DS_SUB_LG_HEADER_DO_REFINE_STEP:
                            DSManager.instance().DoRefineStep(ch, p.ItemGrid)
                    elif p.bSubType == EPacketCGDragonSoulSubHeaderType.DS_SUB_LG_HEADER_DO_REFINE_STRENGTH:
                            DSManager.instance().DoRefineStrength(ch, p.ItemGrid)


## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if __MULTI_LANGUAGE_SYSTEM__
            elif (bHeader == LG_HEADER_CG_DRAGON_SOUL_REFINE) or (bHeader == LG_HEADER_CG_CHANGE_LANGUAGE):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no equivalent to 'reinterpret_cast' in Python:
                    p = reinterpret_cast <SPacketChangeLanguage>(c_pData)
                    ChangeLanguage(ch, p.bLanguage)
##endif

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if __EXTENDED_WHISPER_DETAILS__
            elif bHeader == LG_HEADER_CG_WHISPER_DETAILS:
                    WhisperDetails(ch, c_pData)
##endif

            elif bHeader == LG_HEADER_CG_ACCE:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((iExtraLen = AcceRefine(ch, c_pData, m_iBufferLeft)) < 0)
                    if (iExtraLen = AcceRefine(ch, c_pData, m_iBufferLeft)) < 0:
                        return -1

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if ENABLE_TARGET_INFO
            elif bHeader == LG_HEADER_CG_TARGET_INFO_LOAD:
                    TargetInfoLoad(ch, c_pData)
##endif
            return (iExtraLen)

        int CInputDead.Analyze(DESC* d, byte bHeader, const char * c_pData)
            ch = None

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if (!(ch = d->GetCharacter()))
            if not(ch = d.GetCharacter()):
                #lani_err("no character on desc")
                return 0

            iExtraLen = 0

            if bHeader == LG_HEADER_CG_PONG:
                Pong(d)

            elif bHeader == LG_HEADER_CG_TIME_SYNC:
                Handshake(d, c_pData)

            elif bHeader == LG_HEADER_CG_CHAT:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((iExtraLen = Chat(ch, c_pData, m_iBufferLeft)) < 0)
                if (iExtraLen = Chat(ch, c_pData, m_iBufferLeft)) < 0:
                    return -1


            elif bHeader == LG_HEADER_CG_WHISPER:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((iExtraLen = Whisper(ch, c_pData, m_iBufferLeft)) < 0)
                if (iExtraLen = Whisper(ch, c_pData, m_iBufferLeft)) < 0:
                    return -1


            elif bHeader == LG_HEADER_CG_HACK:
                Hack(ch, c_pData)

            else:
                return (0)

            return (iExtraLen)
