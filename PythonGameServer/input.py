class CInputProcessor:
    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.m_pPacketInfo = None
        self.m_iBufferLeft = 0
        self.m_packetInfoCG = CPacketInfoCG()

        self.m_pPacketInfo = None
        self.m_iBufferLeft = 0
        if self.m_pPacketInfo is None:
            self.BindPacketInfo(self.m_packetInfoCG)

    def close(self):
        pass

    def Process(self, lpDesc, c_pvOrig, iBytes, r_iBytesProceed):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Pointer arithmetic is detected on this variable:
#ORIGINAL METINII C CODE: const char * c_pData = (const char *) c_pvOrig;
        c_pData = str(c_pvOrig)

        bLastHeader = 0
        iLastPacketLen = 0
        iPacketLen = None

        if self.m_pPacketInfo is None:
            #lani_err("No packet info has been binded to")
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        m_iBufferLeft = iBytes
        while self.m_iBufferLeft > 0:
            bHeader = (byte) *(c_pData)
            c_pszName = None

            if bHeader == 0:
                iPacketLen = 1
            else:
                temp_ref_iPacketLen = RefObject(iPacketLen);
                if not self.m_pPacketInfo.Get(bHeader, temp_ref_iPacketLen, c_pszName):
                    iPacketLen = temp_ref_iPacketLen.arg_value
                    #lani_err("UNKNOWN HEADER: %d, LAST HEADER: %d(%d), REMAIN BYTES: %d, fd: %d", bHeader, bLastHeader, iLastPacketLen, self.m_iBufferLeft, lpDesc.GetSocket())
    
                    lpDesc.SetPhase(EPhase.PHASE_CLOSE)
                    return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
                else:
                    iPacketLen = temp_ref_iPacketLen.arg_value

            if self.m_iBufferLeft < iPacketLen:
                return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

            if bHeader != 0:
                if test_server and bHeader != Globals.LG_HEADER_CG_MOVE:
                    #sys_log(0, "Packet Analyze [Header %d][bufferLeft %d] ", bHeader, self.m_iBufferLeft)

                self.m_pPacketInfo.Start()

                iExtraPacketSize = self.Analyze(lpDesc, bHeader, c_pData)

                if iExtraPacketSize < 0:
                    return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

                iPacketLen += iExtraPacketSize
                lpDesc.Log("%s %d", c_pszName, iPacketLen)
                self.m_pPacketInfo.End()

            if bHeader == Globals.LG_HEADER_CG_PONG:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                #sys_log(0, "PONG! %u %u", self.m_pPacketInfo.IsSequence(bHeader), int((c_pData + iPacketLen - sizeof(byte))))

            if self.m_pPacketInfo.IsSequence(bHeader):
                bSeq = lpDesc.GetSequence()
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                bSeqReceived = byte(int((c_pData + iPacketLen - sizeof(byte))))

                if bSeq != bSeqReceived:
                    if bHeader != 254:
                        #lani_err("SEQUENCE %x mismatch 0x%x != 0x%x header %u", Globals.get_pointer(lpDesc), bSeq, bSeqReceived, bHeader)

                        ch = lpDesc.GetCharacter()

                        buf = str(['\0' for _ in range(1024)])
                        offset = None
                        len = None

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                        offset = snprintf(buf, sizeof(buf), "SEQUENCE_LOG [%s]-------------\n",ch.GetName(LOCALE_LANIATUS) if ch is not None else "UNKNOWN")

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                        if offset < 0 or offset >= int(sizeof(buf)):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                            offset = sizeof(buf) - 1

                        i = 0
                        while i < len(lpDesc.m_seq_vector):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                            len = snprintf(buf[offset:], sizeof(buf) - offset, "\t[%03d : 0x%x]\n", lpDesc.m_seq_vector[i].hdr, lpDesc.m_seq_vector[i].seq)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                            if len < 0 or len >= int(sizeof(buf)) - offset:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                                offset += (sizeof(buf) - offset) - 1
                            else:
                                offset += len
                            i += 1

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                        snprintf(buf[offset:], sizeof(buf) - offset, "\t[%03d : 0x%x]\n", bHeader, bSeq)
                        #lani_err("%s", buf)

                        lpDesc.SetPhase(EPhase.PHASE_CLOSE)
                        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
                else:
                    lpDesc.push_seq(bHeader, bSeq)
                    lpDesc.SetNextSequence()
                    ##lani_err("SEQUENCE %x match %u next %u header %u", lpDesc, bSeq, lpDesc->GetSequence(), bHeader)

            c_pData += iPacketLen
            self.m_iBufferLeft -= iPacketLen
            r_iBytesProceed.arg_value += iPacketLen

            iLastPacketLen = iPacketLen
            bLastHeader = bHeader

            if self.GetType() != lpDesc.GetInputProcessor().GetType():
                return LGEMiscellaneous.DEFINECONSTANTS.false

        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def GetType(self):
        pass

    def BindPacketInfo(self, pPacketInfo):
        self.m_pPacketInfo = pPacketInfo

    def Pong(self, d):
        d.SetPong(((not LGEMiscellaneous.DEFINECONSTANTS.false)))

    def Handshake(self, d, c_pData):
        p = c_pData

        if d.GetHandshake() != p.dwHandshake:
            #lani_err("Invalid Handshake on %d", d.GetSocket())
            d.SetPhase(EPhase.PHASE_CLOSE)
        else:
            if d.IsPhase(EPhase.PHASE_HANDSHAKE):
                if d.HandshakeProcess(p.dwTime, p.lDelta, LGEMiscellaneous.DEFINECONSTANTS.false):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if _IMPROVED_PACKET_ENCRYPTION_
                    d.SendKeyAgreement()
##else
                    if g_bAuthServer:
                        d.SetPhase(EPhase.PHASE_AUTH)
                    else:
                        d.SetPhase(EPhase.PHASE_LOGIN)
##endif
            else:
                d.HandshakeProcess(p.dwTime, p.lDelta, ((not LGEMiscellaneous.DEFINECONSTANTS.false)))

    def Version(self, ch, c_pData):
        if ch is None:
            return

        p = c_pData
        #sys_log(0, "VERSION: %s %s %s", ch.GetName(LOCALE_LANIATUS), p.timestamp, p.filename)
        ch.GetDesc().SetClientVersion(p.timestamp)

    def Analyze(self, d, bHeader, c_pData):
        pass



class CInputClose(CInputProcessor):
    def GetType(self):
        return byte(Globals.INPROC_CLOSE)

    def Analyze(self, d, bHeader, c_pData):
        return self.m_iBufferLeft

class CInputHandshake(CInputProcessor):
    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.m_pMainPacketInfo = None

        pkPacketInfo = LG_NEW_M2 CPacketInfoCG
        pkPacketInfo.SetSequence(Globals.LG_HEADER_CG_PONG, LGEMiscellaneous.DEFINECONSTANTS.false)

        self.m_pMainPacketInfo = self.m_pPacketInfo
        self.BindPacketInfo(pkPacketInfo)

    def close(self):
        if None is not self.m_pPacketInfo:
            LG_DEL_MEM(self.m_pPacketInfo)
            self.m_pPacketInfo = None

    def GetType(self):
        return byte(Globals.INPROC_HANDSHAKE)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Pointer arithmetic is detected on the parameter 'c_pData':
#ORIGINAL METINII C CODE: virtual int Analyze(DESC* d, byte bHeader, const char * c_pData)
    def Analyze(self, d, bHeader, c_pData):
        if bHeader == 10:
            return 0

        if bHeader == Globals.LG_HEADER_CG_TEXT:
            c_pData += 1
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Pointer arithmetic is detected on this variable:
#ORIGINAL METINII C CODE: const char * c_pSep;
            c_pSep = None

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if (!(c_pSep = strchr(c_pData, '\n')))
            if not(c_pSep = strchr(c_pData, '\n')):
                return -1

            if *(c_pSep - 1) == '\r':
                c_pSep -= 1

            stResult = ""
            stBuf = ""
            stBuf.assign(c_pData, 0, c_pSep - c_pData)

            #sys_log(0, "SOCKET_CMD: FROM(%s) CMD(%s)", d.GetHostName(), stBuf)

            if not stBuf.compare("IS_SERVER_UP"):
                if g_bNoMoreClient:
                    stResult = "NO"
                else:
                    stResult = "YES"
            elif not stBuf.compare("USER_COUNT"):
                szTmp = str(['\0' for _ in range(64)])
                iTotal = None
                paiEmpireUserCount = []
                iLocal = None
                temp_ref_iTotal = RefObject(iTotal);
                temp_ref_iLocal = RefObject(iLocal);
                DESC_MANAGER.instance().GetUserCount(temp_ref_iTotal, paiEmpireUserCount, temp_ref_iLocal)
                iLocal = temp_ref_iLocal.arg_value
                iTotal = temp_ref_iTotal.arg_value
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                snprintf(szTmp, sizeof(szTmp), "%d %d %d %d %d", iTotal, paiEmpireUserCount[1], paiEmpireUserCount[2], paiEmpireUserCount[3], iLocal)
                stResult += szTmp
            elif not stBuf.compare("CHECK_P2P_CONNECTIONS"):
                oss = std::ostringstream(std::ostringstream.out)

                oss << "P2P CONNECTION NUMBER : " << P2P_MANAGER.instance().GetDescCount() << "\n"
                hostNames = ""
                P2P_MANAGER.Instance().GetP2PHostNames(hostNames)
                oss << hostNames
                stResult = oss.str()
                packet = SPacketGGCheckAwakeness()
                packet.bHeader = byte(Globals.LG_HEADER_GG_CHECK_AWAKENESS)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                P2P_MANAGER.instance().Send(packet, sizeof(packet), NULL)
            elif not stBuf.compare("PACKET_INFO"):
                self.m_pMainPacketInfo.Log("packet_info.txt")
                stResult = "OK"
            elif not stBuf.compare("PROFILE"):
                CProfiler.instance().Log("profile.txt")
                stResult = "OK"

            elif not stBuf.compare(0,15,"DELETE_AWARDID "):
                szTmp = str(['\0' for _ in range(64)])
                msg = stBuf[15:41]

                p = tDeleteAwardID()
                p.dwID = uint((int(msg)))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                snprintf(szTmp,sizeof(szTmp),"Sent to DB cache to delete ItemAward, id: %d",p.dwID)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                db_clientdesc.DBPacket(Globals.LG_HEADER_GD_DELETE_AWARDID, 0, p, sizeof(p))
                stResult += szTmp
            else:
                stResult = "UNKNOWN"

            #sys_log(1, "TEXT %s RESULT %s", stBuf, stResult)
            stResult += "\n"
            d.Packet(stResult, len(stResult))
            return (c_pSep - c_pData) + 1
        elif bHeader == Globals.LG_HEADER_CG_MARK_LOGIN:
            if not guild_mark_server:
                #lani_err("Guild Mark login requested but i'm not a mark server!")
                d.SetPhase(EPhase.PHASE_CLOSE)
                return 0

            #sys_log(0, "MARK_SERVER: Login")
            d.SetPhase(EPhase.PHASE_LOGIN)
            return 0
        elif bHeader == Globals.LG_HEADER_CG_STATE_CHECKER:
            if d.isChannelStatusRequested():
                return 0
            d.SetChannelStatusRequested(((not LGEMiscellaneous.DEFINECONSTANTS.false)))
            db_clientdesc.DBPacket(Globals.LG_HEADER_GD_REQUEST_CHANNELSTATUS, d.GetHandle(), None, 0)
        elif bHeader == Globals.LG_HEADER_CG_PONG:
            self.Pong(d)
        elif bHeader == Globals.LG_HEADER_CG_HANDSHAKE:
            self.Handshake(d, c_pData)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if _IMPROVED_PACKET_ENCRYPTION_
        elif bHeader == Globals.LG_HEADER_CG_KEY_AGREEMENT:
            d.SendKeyAgreementCompleted()
            d.ProcessOutput()

            p = c_pData
            if not d.IsCipherPrepared():
                #lani_err("Cipher isn't prepared. %s maybe a Hacker.", inet_ntoa(d.GetAddr().sin_addr))
                d.DelayedDisconnect(5)
                return 0
            if d.FinishHandshake(p.wAgreedLength, p.data, p.wDataLength):
                if g_bAuthServer:
                    d.SetPhase(EPhase.PHASE_AUTH)
                else:
                    d.SetPhase(EPhase.PHASE_LOGIN)
            else:
                #sys_log(0, "[CInputHandshake] Key agreement failed: al=%u dl=%u", p.wAgreedLength, p.wDataLength)
                d.SetPhase(EPhase.PHASE_CLOSE)
##endif
        else:
            #lani_err("Handshake phase does not handle packet %d (fd %d)", bHeader, d.GetSocket())

        return 0

# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    GuildMarkLogin(d, c_pData)


class CInputLogin(CInputProcessor):
    def GetType(self):
        return byte(Globals.INPROC_LOGIN)

# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    Analyze(d, bHeader, c_pData)

# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    Login(d, data)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    LoginByKey(d, data)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    CharacterSelect(d, data)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    CharacterCreate(d, data)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    CharacterDelete(d, data)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    Entergame(d, data)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    Empire(d, c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    GuildMarkCRCList(d, c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    GuildMarkIDXList(d, c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    GuildMarkUpload(d, c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    GuildSymbolUpload(d, c_pData, uiBytes)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    GuildSymbolCRC(d, c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    ChangeName(d, data)

class CInputMain(CInputProcessor):
    def GetType(self):
        return byte(Globals.INPROC_MAIN)

# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    Analyze(d, bHeader, c_pData)

# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    Attack(ch, header, data)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    Whisper(ch, data, uiBytes)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    Chat(ch, data, uiBytes)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    ItemUse(ch, data)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    ItemDrop(ch, data)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    ItemDrop2(ch, data)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    ItemDestroy(ch, data)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    ItemMove(ch, data)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    ItemPickup(ch, data)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    ItemToItem(ch, pcData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    QuickslotAdd(ch, data)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    QuickslotDelete(ch, data)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    QuickslotSwap(ch, data)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    Shop(ch, data, uiBytes)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    OnClick(ch, data)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    Exchange(ch, data)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    Position(ch, data)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    Move(ch, data)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    SyncPosition(ch, data, uiBytes)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    FlyTarget(ch, pcData, bHeader)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    UseSkill(ch, pcData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    ScriptAnswer(ch, pvData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    ScriptButton(ch, pvData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    ScriptSelectItem(ch, pvData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    QuestInputString(ch, pvData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    QuestConfirm(ch, pvData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    Target(ch, pcData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    Warp(ch, pcData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    SafeboxCheckin(ch, c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    SafeboxCheckout(ch, c_pData, bMall)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    SafeboxItemMove(ch, data)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    Messenger(ch, c_pData, uiBytes)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    PartyInvite(ch, c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    PartyInviteAnswer(ch, c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    PartyRemove(ch, c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    PartySetState(ch, c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    PartyUseSkill(ch, c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    PartyParameter(ch, c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    Guild(ch, data, uiBytes)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    AnswerMakeGuild(ch, c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    Fishing(ch, c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    ItemGive(ch, c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    Hack(ch, c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    MyShop(ch, c_pData, uiBytes)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    Refine(ch, c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    AcceRefine(ch, data, uiBytes)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if ENABLE_TARGET_INFO
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    TargetInfoLoad(ch, c_pData)
##endif
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if __MULTI_LANGUAGE_SYSTEM__
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    ChangeLanguage(ch, bLanguage)
##endif
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if __EXTENDED_WHISPER_DETAILS__
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    WhisperDetails(ch, c_pData)
##endif

class CInputDead(CInputMain):
    def GetType(self):
        return byte(Globals.INPROC_DEAD)

# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    Analyze(d, bHeader, c_pData)

class CInputDB(CInputProcessor):

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.m_dwHandle = 0

# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    Process(d, c_pvOrig, iBytes, r_iBytesProceed)
    def GetType(self):
        return byte(Globals.INPROC_DB)

# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    Analyze(d, bHeader, c_pData)

# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    MapLocations(c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    LoginSuccess(dwHandle, data)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    PlayerCreateFailure(d, bType)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    PlayerDeleteSuccess(d, data)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    PlayerDeleteFail(d)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    PlayerLoad(d, data)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    PlayerCreateSuccess(d, data)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    Boot(data)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    QuestLoad(d, c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    SafeboxLoad(d, c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    SafeboxChangeSize(d, c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    SafeboxWrongPassword(d)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    SafeboxChangePasswordAnswer(d, c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    MallLoad(d, c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    EmpireSelect(d, c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    P2P(c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    ItemLoad(d, c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    AffectLoad(d, c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    GuildLoad(c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    GuildSkillUpdate(c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    GuildSkillRecharge()
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    GuildExpUpdate(c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    GuildAddMember(c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    GuildRemoveMember(c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    GuildChangeGrade(c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    GuildChangeMemberData(c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    GuildDisband(c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    GuildLadder(c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    GuildWar(c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    GuildWarScore(c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    GuildSkillUsableChange(c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    GuildMoneyChange(c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    GuildWithdrawMoney(c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    GuildWarReserveAdd(p)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    GuildWarReserveUpdate(p)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    GuildWarReserveDelete(dwID)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    GuildWarBet(p)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    GuildChangeMaster(p)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    LoginAlready(d, c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    PartyCreate(c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    PartyDelete(c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    PartyAdd(c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    PartyRemove(c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    PartyStateChange(c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    PartySetMemberLevel(c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    Time(c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    ReloadProto(c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    ChangeName(d, data)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    AuthLogin(d, c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    ItemAward(c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    ChangeEmpirePriv(c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    ChangeGuildPriv(c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    ChangeCharacterPriv(c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    SetEventFlag(c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    CreateObject(c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    DeleteObject(c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    UpdateLand(c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    Notice(c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    MarriageAdd(p)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    MarriageUpdate(p)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    MarriageRemove(p)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    WeddingRequest(p)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    WeddingReady(p)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    WeddingStart(p)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    WeddingEnd(p)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    MyshopPricelistRes(d, p)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    ReloadAdmin(c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    ItemAwardInformer(data)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    RespondChannelStatus(desc, pcData)


class CInputUDP(CInputProcessor):
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    CInputUDP()
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    Process(d, c_pvOrig, iBytes, r_iBytesProceed)
    def GetType(self):
        return byte(Globals.INPROC_UDP)
    def SetSockAddr(self, rSockAddr):
## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: m_SockAddr = rSockAddr;
        self.m_SockAddr.copy_from(rSockAddr)

# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    Analyze(d, bHeader, c_pData)

# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    Handshake(lpDesc, c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    StateChecker(c_pData)


class CInputP2P(CInputProcessor):
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    CInputP2P()
    def GetType(self):
        return byte(Globals.INPROC_P2P)

# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    Analyze(d, bHeader, c_pData)

# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    Setup(d, c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    Login(d, c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    Logout(d, c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    Relay(d, c_pData, uiBytes)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    Notice(d, c_pData, uiBytes)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    Guild(d, c_pData, uiBytes)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    Shout(c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    Disconnect(c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    MessengerAdd(c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    MessengerRemove(c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    FindPosition(d, c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    WarpCharacter(c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    GuildWarZoneMapIndex(c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    Transfer(c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    XmasWarpSanta(c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    XmasWarpSantaReply(c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    LoginPing(d, c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    BlockChat(c_pData)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    IamAwake(d, c_pData)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if __MULTI_LANGUAGE_SYSTEM__
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    LocaleNotice(c_pData)
##endif


class CInputAuth(CInputProcessor):
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    CInputAuth()
    def GetType(self):
        return byte(Globals.INPROC_AUTH)

# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    Analyze(d, bHeader, c_pData)

# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    Login(d, c_pData)
