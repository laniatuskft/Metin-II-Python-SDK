from enum import Enum
import math

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if _IMPROVED_PACKET_ENCRYPTION_
##endif

## Laniatus Games Studio Inc. | NOTE: Python has no need of forward class declarations:
#class CInputProcessor

class EDescType(Enum):
    DESC_TYPE_ACCEPTOR = 0
    DESC_TYPE_CONNECTOR = 1

class CLoginKey:
    def __init__(self, dwKey, pkDesc):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.m_dwKey = 0
        self.m_dwExpireTime = 0
        self.m_pkDesc = None

        self.m_dwKey = dwKey
        self.m_pkDesc = pkDesc
        self.m_dwExpireTime = 0

    def Expire(self):
        self.m_dwExpireTime = get_dword_time()
        self.m_pkDesc = None

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: operator uint() const
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following operator cannot be converted to Python:
    #operator uint() const
    #        {
    #            return m_dwKey
    #        }


class seq_t:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.hdr = 0
        self.seq = 0


class DESC:
    class desc_event_info(event_info_data):

        def __init__(self):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.desc = None

            self.desc = None

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.m_pInputProcessor = None
        self.m_inputClose = CInputClose()
        self.m_inputHandshake = CInputHandshake()
        self.m_inputLogin = CInputLogin()
        self.m_inputMain = CInputMain()
        self.m_inputDead = CInputDead()
        self.m_inputAuth = CInputAuth()
        self.m_lpFdw = LPFDWATCH()
        self.m_sock = socket_t()
        self.m_iPhase = 0
        self.m_dwHandle = 0
        self.m_stHost = ""
        self.m_wPort = 0
        self.m_LastTryToConnectTime = time_t()
        self.m_lpInputBuffer = None
        self.m_iMinInputBufferLen = 0
        self.m_dwHandshake = 0
        self.m_dwHandshakeSentTime = 0
        self.m_iHandshakeRetry = 0
        self.m_dwClientTime = 0
        self.m_bHandshaking = False
        self.m_lpBufferedOutputBuffer = None
        self.m_lpOutputBuffer = None
        self.m_pkPingEvent = _boost_func_of_void.intrusive_ptr()
        self.m_lpCharacter = None
        self.m_accountTable = SAccountTable()
        self.m_SockAddr = sockaddr_in()
        self.m_UDPSockAddr = sockaddr_in()
        self.m_pLogFile = None
        self.m_stRelayName = ""
        self.m_stP2PHost = ""
        self.m_wP2PPort = 0
        self.m_bP2PChannel = 0
        self.m_bPong = False
        self.m_iCurrentSequence = 0
        self.m_pkLoginKey = None
        self.m_dwLoginKey = 0
        self.m_bCRCMagicCubeIdx = 0
        self.m_dwProcCRC = 0
        self.m_dwFileCRC = 0
        self.m_bHackCRCQuery = False
        self.m_stClientVersion = ""
        self.m_Login = ""
        self.m_outtime = 0
        self.m_playtime = 0
        self.m_offtime = 0
        self.m_bDestroyed = False
        self.m_bChannelStatusRequested = False
        self.cipher_ = Cipher()
        self.m_bEncrypted = False
        self.m_adwDecryptionKey = [0 for _ in range(4)]
        self.m_adwEncryptionKey = [0 for _ in range(4)]
        self.m_pkDisconnectEvent = _boost_func_of_void.intrusive_ptr()
        self.m_seq_vector = []

        self.Initialize()

    def close(self):
        pass

    def GetType(self):
        return EDescType.DESC_TYPE_ACCEPTOR
    def Destroy(self):
        if self.m_bDestroyed:
            return
        self.m_bDestroyed = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        if self.m_pkLoginKey:
            self.m_pkLoginKey.Expire()

        if (self.GetAccountTable().id) != 0:
            DESC_MANAGER.instance().DisconnectAccount(self.GetAccountTable().login)

        if self.m_pLogFile:
            fclose(self.m_pLogFile)
            self.m_pLogFile = None

        if self.m_lpCharacter:
            self.m_lpCharacter.Disconnect("DESC::~DESC")
            self.m_lpCharacter = None

            if self.m_lpOutputBuffer is not None:
                buffer_delete(self.m_lpOutputBuffer)
                self.m_lpOutputBuffer = None
            if self.m_lpInputBuffer is not None:
                buffer_delete(self.m_lpInputBuffer)
                self.m_lpInputBuffer = None

        event_cancel(self.m_pkPingEvent)
        event_cancel(self.m_pkDisconnectEvent)

        if not g_bAuthServer:
            if self.m_accountTable.login[0] != '\0' and self.m_accountTable.passwd[0] != '\0':
                pack = SLogoutPacket()

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                strncpy_s(pack.login, sizeof(pack.login), self.m_accountTable.login, _TRUNCATE)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                strncpy_s(pack.passwd, sizeof(pack.passwd), self.m_accountTable.passwd, _TRUNCATE)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                db_clientdesc.DBPacket(Globals.LG_HEADER_GD_LOGOUT, self.m_dwHandle, pack, sizeof(SLogoutPacket))

        if self.m_sock is not LGEMiscellaneous.DEFINECONSTANTS.INVALID_SOCKET:
            #sys_log(0, "SYSTEM: closing socket. DESC #%d", self.m_sock)
            self.Log("SYSTEM: closing socket. DESC #%d", socket_t(self.m_sock))
            fdwatch_del_fd(self.m_lpFdw, self.m_sock)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if _IMPROVED_PACKET_ENCRYPTION_
            self.cipher_.CleanUp()
##endif

            socket_close(self.m_sock)
            self.m_sock = LGEMiscellaneous.DEFINECONSTANTS.INVALID_SOCKET

        self.m_seq_vector.clear()

    def SetPhase(self, _phase):
        self.m_iPhase = _phase

        pack = packet_phase()
        pack.header = byte(Globals.LG_HEADER_GC_PHASE)
        pack.phase = byte(_phase)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Packet(pack, sizeof(packet_phase))

        if self.m_iPhase == EPhase.PHASE_CLOSE:
            self.m_pInputProcessor = self.m_inputClose

        elif self.m_iPhase == EPhase.PHASE_HANDSHAKE:
            self.m_pInputProcessor = self.m_inputHandshake

        elif (self.m_iPhase == EPhase.PHASE_SELECT) or (self.m_iPhase == EPhase.PHASE_LOGIN) or (self.m_iPhase == EPhase.PHASE_LOADING):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if ! _IMPROVED_PACKET_ENCRYPTION_
            self.m_bEncrypted = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
##endif
            self.m_pInputProcessor = self.m_inputLogin

        elif (self.m_iPhase == EPhase.PHASE_GAME) or (self.m_iPhase == EPhase.PHASE_DEAD):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if ! _IMPROVED_PACKET_ENCRYPTION_
            self.m_bEncrypted = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
##endif
            self.m_pInputProcessor = self.m_inputMain

        elif self.m_iPhase == EPhase.PHASE_AUTH:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if ! _IMPROVED_PACKET_ENCRYPTION_
            self.m_bEncrypted = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
##endif
            self.m_pInputProcessor = self.m_inputAuth
            #sys_log(0, "AUTH_PHASE %p", self)

    def FlushOutput(self):
        if self.m_sock is LGEMiscellaneous.DEFINECONSTANTS.INVALID_SOCKET:
            return

        if buffer_size(self.m_lpOutputBuffer) <= 0:
            return

        sleep_tv = timeval()
        now_tv = timeval()
        start_tv = timeval()
        event_triggered = LGEMiscellaneous.DEFINECONSTANTS.false

        gettimeofday(start_tv, None)

        socket_block(self.m_sock)
        #sys_log(0, "FLUSH START %d", buffer_size(self.m_lpOutputBuffer))

        while buffer_size(self.m_lpOutputBuffer) > 0:
            gettimeofday(now_tv, None)

            iSecondsPassed = now_tv.tv_sec - start_tv.tv_sec

            if iSecondsPassed > 10:
                if event_triggered == 0 or iSecondsPassed > 20:
                    self.SetPhase(EPhase.PHASE_CLOSE)
                    break

            sleep_tv.tv_sec = 0
            sleep_tv.tv_usec = 10000

            num_events = fdwatch(self.m_lpFdw, sleep_tv)

            if num_events < 0:
                #lani_err("num_events < 0 : %d", num_events)
                break

            event_idx = None

            for event_idx in range(0, num_events):
                d2 = fdwatch_get_client_data(self.m_lpFdw, event_idx)

                if d2 is not self:
                    continue

                if fdwatch_check_event(self.m_lpFdw, self.m_sock, event_idx) == EFdwatch.FDW_WRITE:
                    event_triggered = 1 if ((not LGEMiscellaneous.DEFINECONSTANTS.false)) else 0

                    if self.ProcessOutput() < 0:
                        #lani_err("Cannot flush output buffer")
                        self.SetPhase(EPhase.PHASE_CLOSE)

                elif fdwatch_check_event(self.m_lpFdw, self.m_sock, event_idx) == EFdwatch.FDW_EOF:
                    self.SetPhase(EPhase.PHASE_CLOSE)

            if self.IsPhase(EPhase.PHASE_CLOSE):
                break

        if buffer_size(self.m_lpOutputBuffer) == 0:
            #sys_log(0, "FLUSH SUCCESS")
        else:
            #sys_log(0, "FLUSH FAIL")

        Globals.usleep(250000)

    def Setup(self, _fdw, _fd, c_rSockAddr, _handle, _handshake):
## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: m_lpFdw = _fdw;
        self.m_lpFdw.copy_from(_fdw)
## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: m_sock = _fd;
        self.m_sock.copy_from(_fd)

        self.m_stHost = inet_ntoa(c_rSockAddr.sin_addr)
        self.m_wPort = c_rSockAddr.sin_port
        self.m_dwHandle = _handle

        self.m_lpOutputBuffer = buffer_new(LGEMiscellaneous.DEFINECONSTANTS.DEFAULT_PACKET_BUFFER_SIZE * 2)

        self.m_iMinInputBufferLen = LGEMiscellaneous.DEFINECONSTANTS.MAX_INPUT_LEN >> 1
        self.m_lpInputBuffer = buffer_new(LGEMiscellaneous.DEFINECONSTANTS.MAX_INPUT_LEN)

## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: m_SockAddr = c_rSockAddr;
        self.m_SockAddr.copy_from(c_rSockAddr)

        fdwatch_add_fd(self.m_lpFdw, self.m_sock, self, EFdwatch.FDW_READ, LGEMiscellaneous.DEFINECONSTANTS.false)

        info = Globals.AllocEventInfo()

        info.desc = self
        m_pkPingEvent is None

        m_pkPingEvent = event_create_ex(ping_event, info, ping_event_second_cycle)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if ! _IMPROVED_PACKET_ENCRYPTION_
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memcpy' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memcpy(self.m_adwEncryptionKey, LGEMiscellaneous.DEFINECONSTANTS.LSS_SECURITY_KEY, sizeof(uint) * 4)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memcpy' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memcpy(self.m_adwDecryptionKey, LGEMiscellaneous.DEFINECONSTANTS.LSS_SECURITY_KEY, sizeof(uint) * 4)
##endif

        self.SetPhase(EPhase.PHASE_HANDSHAKE)
        self.StartHandshake(_handshake)

        #sys_log(0, "SYSTEM: new connection from [%s] fd: %d handshake %u output input_len %d, ptr %p", self.m_stHost, self.m_sock, self.m_dwHandshake, buffer_size(self.m_lpInputBuffer), self)

        Log("SYSTEM: new connection from [%s] fd: %d handshake %u ptr %p", self.m_stHost, self.m_sock, self.m_dwHandshake, self)
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: socket_t GetSocket() const
    def GetSocket(self):
        return socket_t(self.m_sock)
    def GetHostName(self):
        return self.m_stHost
    def GetPort(self):
        return self.m_wPort
    def SetP2P(self, h, w, b):
        self.m_stP2PHost = h
        self.m_wP2PPort = w
        self.m_bP2PChannel = b
    def GetP2PHost(self):
        return self.m_stP2PHost
## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: ushort GetP2PPort() const
    def GetP2PPort(self):
        return self.m_wP2PPort
## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: byte GetP2PChannel() const
    def GetP2PChannel(self):
        return self.m_bP2PChannel
    def BufferedPacket(self, c_pvData, iSize):
        if self.m_iPhase == EPhase.PHASE_CLOSE:
            return

        if self.m_lpBufferedOutputBuffer is None:
            self.m_lpBufferedOutputBuffer = buffer_new(MAX(1024, iSize))

        buffer_write(self.m_lpBufferedOutputBuffer, c_pvData, iSize)

    def Packet(self, c_pvData, iSize):
        assert iSize > 0

        if self.m_iPhase == EPhase.PHASE_CLOSE:
            return

        if len(self.m_stRelayName) != 0:
            p = SPacketGGRelay()

            p.bHeader = byte(Globals.LG_HEADER_GG_RELAY)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            strncpy_s(p.szName, sizeof(p.szName), self.m_stRelayName, _TRUNCATE)
            p.lSize = iSize

            ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no direct equivalent in Python to the following C++ macro:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            if not Globals.__packet_encode(self.m_lpOutputBuffer, p, sizeof(p), __FILE__, __LINE__):
                self.m_iPhase = EPhase.PHASE_CLOSE
                return

            self.m_stRelayName = ""

            ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no direct equivalent in Python to the following C++ macro:
            if not Globals.__packet_encode(self.m_lpOutputBuffer, c_pvData, iSize, __FILE__, __LINE__):
                self.m_iPhase = EPhase.PHASE_CLOSE
                return
        else:
            if self.m_lpBufferedOutputBuffer:
                buffer_write(self.m_lpBufferedOutputBuffer, c_pvData, iSize)

                c_pvData = buffer_read_peek(self.m_lpBufferedOutputBuffer)
                iSize = buffer_size(self.m_lpBufferedOutputBuffer)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if _IMPROVED_PACKET_ENCRYPTION_
            buf = buffer_write_peek(self.m_lpOutputBuffer)

            ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no direct equivalent in Python to the following C++ macro:
            if Globals.__packet_encode(self.m_lpOutputBuffer, c_pvData, iSize, __FILE__, __LINE__):
                if self.cipher_.activated():
                    self.cipher_.Encrypt(buf, iSize)
            else:
                self.m_iPhase = EPhase.PHASE_CLOSE
##else
            if not self.m_bEncrypted:
                ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no direct equivalent in Python to the following C++ macro:
                if not Globals.__packet_encode(self.m_lpOutputBuffer, c_pvData, iSize, __FILE__, __LINE__):
                    self.m_iPhase = EPhase.PHASE_CLOSE
            else:
                if buffer_has_space(self.m_lpOutputBuffer) < iSize + 8:
                    #lani_err("desc buffer mem_size overflow. memsize(%u) write_pos(%u) iSize(%d)", self.m_lpOutputBuffer.mem_size, self.m_lpOutputBuffer.write_LG_POINT_pos, iSize)

                    self.m_iPhase = EPhase.PHASE_CLOSE
                else:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to pointers to value types:
#ORIGINAL METINII C CODE: uint * pdwWritePoint = (uint *) buffer_write_peek(m_lpOutputBuffer);
                    pdwWritePoint = buffer_write_peek(self.m_lpOutputBuffer)

                    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no direct equivalent in Python to the following C++ macro:
                    if Globals.__packet_encode(self.m_lpOutputBuffer, c_pvData, iSize, __FILE__, __LINE__):
                        iSize2 = TEA_Encrypt(pdwWritePoint, pdwWritePoint, self.GetEncryptionKey(), iSize)

                        if iSize2 > iSize:
                            buffer_write_proceed(self.m_lpOutputBuffer, iSize2 - iSize)
##endif

                if self.m_lpBufferedOutputBuffer is not None:
                    buffer_delete(self.m_lpBufferedOutputBuffer)
                    self.m_lpBufferedOutputBuffer = None

        if self.m_iPhase != EPhase.PHASE_CLOSE:
            fdwatch_add_fd(self.m_lpFdw, self.m_sock, self, EFdwatch.FDW_WRITE, ((not LGEMiscellaneous.DEFINECONSTANTS.false)))

    def LargePacket(self, c_pvData, iSize):
        buffer_adjust_size(self.m_lpOutputBuffer, iSize)
        #sys_log(0, "LargePacket Size %d", iSize, buffer_size(self.m_lpOutputBuffer))

        self.Packet(c_pvData, iSize)

    def ProcessInput(self):
        bytes_read = None

        if self.m_lpInputBuffer is None:
            #lani_err("DESC::ProcessInput : nil input buffer")
            return -1

        buffer_adjust_size(self.m_lpInputBuffer, self.m_iMinInputBufferLen)
        bytes_read = socket_read(self.m_sock, str(buffer_write_peek(self.m_lpInputBuffer)), buffer_has_space(self.m_lpInputBuffer))

        if bytes_read < 0:
            return -1
        elif bytes_read == 0:
            return 0

        buffer_write_proceed(self.m_lpInputBuffer, bytes_read)

        if self.m_pInputProcessor is None:
            #lani_err("no input processor")

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if _IMPROVED_PACKET_ENCRYPTION_
        else:
            if self.cipher_.activated():
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no equivalent to 'const_cast' in Python:
                self.cipher_.Decrypt(const_cast<object>(buffer_read_peek(self.m_lpInputBuffer)), buffer_size(self.m_lpInputBuffer))

            iBytesProceed = 0

            temp_ref_iBytesProceed = RefObject(iBytesProceed);
            while not self.m_pInputProcessor.Process(self, buffer_read_peek(self.m_lpInputBuffer), buffer_size(self.m_lpInputBuffer), temp_ref_iBytesProceed):
                iBytesProceed = temp_ref_iBytesProceed.arg_value
                buffer_read_proceed(self.m_lpInputBuffer, iBytesProceed)
                iBytesProceed = 0
            iBytesProceed = temp_ref_iBytesProceed.arg_value

            buffer_read_proceed(self.m_lpInputBuffer, iBytesProceed)
##else
        elif not self.m_bEncrypted:
            iBytesProceed = 0

            temp_ref_iBytesProceed2 = RefObject(iBytesProceed);
            while not self.m_pInputProcessor.Process(self, buffer_read_peek(self.m_lpInputBuffer), buffer_size(self.m_lpInputBuffer), temp_ref_iBytesProceed2):
                iBytesProceed = temp_ref_iBytesProceed2.arg_value
                buffer_read_proceed(self.m_lpInputBuffer, iBytesProceed)
                iBytesProceed = 0
            iBytesProceed = temp_ref_iBytesProceed2.arg_value

            buffer_read_proceed(self.m_lpInputBuffer, iBytesProceed)
        else:
            iSizeBuffer = buffer_size(self.m_lpInputBuffer)

            if (iSizeBuffer & 7) != 0:
                iSizeBuffer -= iSizeBuffer & 7

            if iSizeBuffer > 0:
                lpBufferDecrypt = buffer_new(iSizeBuffer)

                iSizeAfter = TEA_Decrypt(buffer_write_peek(lpBufferDecrypt), buffer_read_peek(self.m_lpInputBuffer), self.GetDecryptionKey(), iSizeBuffer)

                buffer_write_proceed(lpBufferDecrypt, iSizeAfter)

                iBytesProceed = 0

                temp_ref_iBytesProceed3 = RefObject(iBytesProceed);
                while not self.m_pInputProcessor.Process(self, buffer_read_peek(lpBufferDecrypt), buffer_size(lpBufferDecrypt), temp_ref_iBytesProceed3):
                    iBytesProceed = temp_ref_iBytesProceed3.arg_value
                    if iBytesProceed > iSizeBuffer:
                        buffer_read_proceed(self.m_lpInputBuffer, iSizeBuffer)
                        iSizeBuffer = 0
                        iBytesProceed = 0
                        break

                    buffer_read_proceed(self.m_lpInputBuffer, iBytesProceed)
                    iSizeBuffer -= iBytesProceed

                    buffer_read_proceed(lpBufferDecrypt, iBytesProceed)
                    iBytesProceed = 0
                iBytesProceed = temp_ref_iBytesProceed3.arg_value

                buffer_delete(lpBufferDecrypt)
                buffer_read_proceed(self.m_lpInputBuffer, iBytesProceed)
##endif

        return (bytes_read)

    def ProcessOutput(self):
        if buffer_size(self.m_lpOutputBuffer) <= 0:
            return 0

        buffer_left = fdwatch_get_buffer_size(self.m_lpFdw, self.m_sock)

        if buffer_left <= 0:
            return 0

        bytes_to_write = MIN(buffer_left, buffer_size(self.m_lpOutputBuffer))

        if bytes_to_write == 0:
            return 0

        result = socket_write(self.m_sock, str(buffer_read_peek(self.m_lpOutputBuffer)), bytes_to_write)

        if result == 0:
            max_bytes_written = MAX(bytes_to_write, max_bytes_written)

            total_bytes_written += bytes_to_write
            current_bytes_written += bytes_to_write

            buffer_read_proceed(self.m_lpOutputBuffer, bytes_to_write)

            if buffer_size(self.m_lpOutputBuffer) != 0:
                fdwatch_add_fd(self.m_lpFdw, self.m_sock, self, EFdwatch.FDW_WRITE, ((not LGEMiscellaneous.DEFINECONSTANTS.false)))

        return (result)

    def GetInputProcessor(self):
        return self.m_pInputProcessor
## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: uint GetHandle() const
    def GetHandle(self):
        return self.m_dwHandle
    def GetOutputBuffer(self):
        return self.m_lpOutputBuffer
    def BindAccountTable(self, pAccountTable):
        assert pAccountTable is not None
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memcpy' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memcpy(self.m_accountTable, pAccountTable, sizeof(SAccountTable))
        DESC_MANAGER.instance().ConnectAccount(self.m_accountTable.login, self)

    def GetAccountTable(self):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
#ORIGINAL METINII C CODE: return m_accountTable;
        return SAccountTable(self.m_accountTable)
    def BindCharacter(self, ch):
        self.m_lpCharacter = ch

    def GetCharacter(self):
        return self.m_lpCharacter
## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: bool IsPhase(int phase) const
    def IsPhase(self, phase):
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false)) if self.m_iPhase == phase else LGEMiscellaneous.DEFINECONSTANTS.false
    def GetAddr(self):
        return sockaddr_in(self.m_SockAddr)
    def UDPGrant(self, c_rSockAddr):
## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: m_UDPSockAddr = c_rSockAddr;
        self.m_UDPSockAddr.copy_from(c_rSockAddr)

        pack = packet_bindudp()

        pack.header = byte(Globals.LG_HEADER_GC_BINDUDP)
        pack.addr = self.m_UDPSockAddr.sin_addr.s_addr
        pack.port = self.m_UDPSockAddr.sin_port

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Packet(pack, sizeof(packet_bindudp))

    def GetUDPAddr(self):
        return sockaddr_in(self.m_UDPSockAddr)
    def Log(self, format, *LegacyParamArray):
        if self.m_pLogFile is None:
            return

        args = None

        ct = get_global_time()
        tm = *localtime(ct)

        fprintf(self.m_pLogFile, "%02d %02d %02d:%02d:%02d | ", tm.tm_mon + 1, tm.tm_mday, tm.tm_hour, tm.tm_min, tm.tm_sec)

        ParamCount = -1
#        va_start(args, format)
        vfprintf(self.m_pLogFile, format, args)
#        va_end(args)

        fputs("\n", self.m_pLogFile)

        fflush(self.m_pLogFile)

    def StartHandshake(self, _handshake):
        self.m_dwHandshake = _handshake
        self.SendHandshake(get_dword_time(), 0)
        self.m_iHandshakeRetry = 0

    def SendHandshake(self, dwCurTime, lNewDelta):
        pack = packet_handshake()

        pack.bHeader = byte(Globals.LG_HEADER_GC_HANDSHAKE)
        pack.dwHandshake = self.m_dwHandshake
        pack.dwTime = dwCurTime
        pack.lDelta = lNewDelta

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Packet(pack, sizeof(packet_handshake))

        self.m_dwHandshakeSentTime = dwCurTime
        self.m_bHandshaking = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def HandshakeProcess(self, dwTime, lDelta, bInfiniteRetry = LGEMiscellaneous.DefineConstants.false):
        dwCurTime = get_dword_time()

        if lDelta < 0:
            #lani_err("Desc::HandshakeProcess : value error (lDelta %d, ip %s)", lDelta, self.m_stHost)
            return LGEMiscellaneous.DEFINECONSTANTS.false

        bias = int((dwCurTime - (dwTime + lDelta)))

        if bias >= 0 and bias <= 50:
            if bInfiniteRetry:
                bHeader = byte(Globals.LG_HEADER_GC_TIME_SYNC)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                self.Packet(bHeader, sizeof(byte))

            if self.GetCharacter():
                #sys_log(0, "Handshake: client_time %u server_time %u name: %s", self.m_dwClientTime, dwCurTime, self.GetCharacter().GetName(LOCALE_LANIATUS))
            else:
                #sys_log(0, "Handshake: client_time %u server_time %u", self.m_dwClientTime, dwCurTime, lDelta)

            self.m_dwClientTime = dwCurTime
            self.m_bHandshaking = LGEMiscellaneous.DEFINECONSTANTS.false
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        lNewDelta = math.trunc(int((dwCurTime - dwTime)) / float(2))

        if lNewDelta < 0:
            #sys_log(0, "Handshake: lower than zero %d", lNewDelta)
            lNewDelta = math.trunc((dwCurTime - self.m_dwHandshakeSentTime) / float(2))

        #sys_log(1, "Handshake: ServerTime %u dwTime %u lDelta %d SentTime %u lNewDelta %d", dwCurTime, dwTime, lDelta, self.m_dwHandshakeSentTime, lNewDelta)

        if not bInfiniteRetry:
            self.m_iHandshakeRetry += 1
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: if (++m_iHandshakeRetry > DefineConstants.HANDSHAKE_RETRY_LIMIT)
            if self.m_iHandshakeRetry > LGEMiscellaneous.DEFINECONSTANTS.HANDSHAKE_RETRY_LIMIT:
                #lani_err("handshake retry limit reached! (limit %d character %s)", LGEMiscellaneous.DEFINECONSTANTS.HANDSHAKE_RETRY_LIMIT,self.GetCharacter().GetName(LOCALE_LANIATUS) if self.GetCharacter() is not None else "!NO CHARACTER!")
                self.SetPhase(EPhase.PHASE_CLOSE)
                return LGEMiscellaneous.DEFINECONSTANTS.false

        self.SendHandshake(dwCurTime, lNewDelta)
        return LGEMiscellaneous.DEFINECONSTANTS.false

    def IsHandshaking(self):
        return self.m_bHandshaking

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: uint GetHandshake() const
    def GetHandshake(self):
        return self.m_dwHandshake
    def GetClientTime(self):
        return self.m_dwClientTime

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if _IMPROVED_PACKET_ENCRYPTION_
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if _IMPROVED_PACKET_ENCRYPTION_
    def SendKeyAgreement(self):
        packet = TPacketKeyAgreement()

        data_length = TPacketKeyAgreement.MAX_DATA_LEN
        agreed_length = self.cipher_.Prepare(packet.data, data_length)
        if agreed_length == 0:
            self.SetPhase(EPhase.PHASE_CLOSE)
            return
        assert data_length <= TPacketKeyAgreement.MAX_DATA_LEN

        packet.bHeader = byte(Globals.LG_HEADER_GC_KEY_AGREEMENT)
        packet.wAgreedLength = agreed_length
        packet.wDataLength = data_length

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Packet(packet, sizeof(packet))

    def SendKeyAgreementCompleted(self):
        packet = TPacketKeyAgreementCompleted()

        packet.bHeader = byte(Globals.LG_HEADER_GC_KEY_AGREEMENT_COMPLETED)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Packet(packet, sizeof(packet))

    def FinishHandshake(self, agreed_length, buffer, length):
        return self.cipher_.Activate(LGEMiscellaneous.DEFINECONSTANTS.false, size_t(agreed_length), buffer, size_t(length))

    def IsCipherPrepared(self):
        return self.cipher_.IsKeyPrepared()

##else
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if ! _IMPROVED_PACKET_ENCRYPTION_
    def SetSecurityKey(self, c_pdwKey):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to pointers to value types:
#ORIGINAL METINII C CODE: const byte * c_pszKey = (const byte *) "JyTxtHljHJlVJHorRM301vf@4fvj10-v";
        c_pszKey = byte(int("JyTxtHljHJlVJHorRM301vf@4fvj10-v"))

        c_pszKey = byte(Globals.GetKey_20050304Myevan() + 37)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memcpy' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
        memcpy(self.m_adwDecryptionKey, c_pdwKey, 16)
        TEA_Encrypt(self.m_adwEncryptionKey[0], self.m_adwDecryptionKey[0], c_pszKey, 16)

        #sys_log(0, "SetSecurityKey decrypt %u %u %u %u encrypt %u %u %u %u", self.m_adwDecryptionKey[0], self.m_adwDecryptionKey[1], self.m_adwDecryptionKey[2], self.m_adwDecryptionKey[3], self.m_adwEncryptionKey[0], self.m_adwEncryptionKey[1], self.m_adwEncryptionKey[2], self.m_adwEncryptionKey[3])
##endif

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: const uint * GetEncryptionKey() const
## Laniatus Games Studio Inc. | WARNING: Python has no equivalent to methods returning pointers to value types:
    def GetEncryptionKey(self):
        return self.m_adwEncryptionKey[0]
## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: const uint * GetDecryptionKey() const
## Laniatus Games Studio Inc. | WARNING: Python has no equivalent to methods returning pointers to value types:
    def GetDecryptionKey(self):
        return self.m_adwDecryptionKey[0]
##endif
    def GetEmpire(self):
        return self.m_accountTable.bEmpire

    def SetRelay(self, c_pszName):
        self.m_stRelayName = c_pszName

    def DelayedDisconnect(self, iSec):
        if self.m_pkDisconnectEvent is not None:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        info = Globals.AllocEventInfo()
        info.desc = self

        self.m_pkDisconnectEvent = event_create_ex(disconnect_event, info, ((iSec) * passes_per_sec))
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def DisconnectOfSameLogin(self):
        if self.GetCharacter():
            if self.m_pkDisconnectEvent:
                return

            self.GetCharacter().ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Someone logged in with your account. You will be disconnected."))
            self.DelayedDisconnect(5)
        else:
            self.SetPhase(EPhase.PHASE_CLOSE)

    def SetPong(self, b):
        self.m_bPong = b

    def IsPong(self):
        return self.m_bPong

    def GetSequence(self):
        return gc_abSequence[self.m_iCurrentSequence]

    def SetNextSequence(self):
        self.m_iCurrentSequence += 1
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: if (++m_iCurrentSequence == DefineConstants.SEQUENCE_MAX_NUM)
        if self.m_iCurrentSequence == LGEMiscellaneous.DEFINECONSTANTS.SEQUENCE_MAX_NUM:
            self.m_iCurrentSequence = 0

    def SendLoginSuccessPacket(self):
        rTable = self.GetAccountTable()

        p = packet_login_success()

        p.bHeader = byte(Globals.LG_HEADER_GC_LOGIN_SUCCESS_NEWSLOT)

        p.handle = self.GetHandle()
        p.random_key = DESC_MANAGER.instance().MakeRandomKey(self.GetHandle())
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memcpy' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memcpy(p.players, rTable.players, sizeof(rTable.players))

        LaniatusDefVariables = 0
        while LaniatusDefVariables < LGEMiscellaneous.PLAYER_PER_ACCOUNT:
            g = CGuildManager.instance().GetLinkedGuild(rTable.players[LaniatusDefVariables].dwID)

            if g:
                p.guild_id[LaniatusDefVariables] = g.GetID()
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                strncpy_s(p.guild_name[LaniatusDefVariables], sizeof(p.guild_name[LaniatusDefVariables]), g.GetName(), _TRUNCATE)
            else:
                p.guild_id[LaniatusDefVariables] = 0
                p.guild_name[LaniatusDefVariables][0] = '\0'
            LaniatusDefVariables += 1

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Packet(p, sizeof(packet_login_success))

    def SetLoginKey(self, dwKey):
        self.m_dwLoginKey = dwKey

    def SetLoginKey(self, pkKey):
        self.m_pkLoginKey = pkKey
        #sys_log(0, "SetLoginKey %u", self.m_pkLoginKey.m_dwKey)

    def GetLoginKey(self):
        if self.m_pkLoginKey:
            return self.m_pkLoginKey.m_dwKey

        return self.m_dwLoginKey

    ## Laniatus Games Studio Inc. | NOTE: This was formerly a static local variable declaration (not allowed in Python):

    def AssembleCRCMagicCube(self, bProcPiece, bFilePiece):
        ## Laniatus Games Studio Inc. | NOTE: This static local variable declaration (not allowed in Python) has been moved just prior to the method:
        #        static byte abXORTable[32] = { 102, 30, 0, 0, 0, 0, 0, 0, 188, 44, 0, 0, 0, 0, 0, 0, 39, 201, 0, 0, 0, 0, 0, 0, 43, 5, 0, 0, 0, 0, 0, 0}

        bProcPiece = byte((bProcPiece ^ AssembleCRCMagicCube_abXORTable[self.m_bCRCMagicCubeIdx]))
        bFilePiece = byte((bFilePiece ^ AssembleCRCMagicCube_abXORTable[self.m_bCRCMagicCubeIdx+1]))

        self.m_dwProcCRC |= uint(bProcPiece << self.m_bCRCMagicCubeIdx)
        self.m_dwFileCRC |= uint(bFilePiece << self.m_bCRCMagicCubeIdx)

        self.m_bCRCMagicCubeIdx += 8

        if (self.m_bCRCMagicCubeIdx & 31) == 0:
            self.m_dwProcCRC = 0
            self.m_dwFileCRC = 0
            self.m_bCRCMagicCubeIdx = 0

    def SetClientVersion(self, c_pszTimestamp):
        self.m_stClientVersion = c_pszTimestamp
    def GetClientVersion(self):
        return self.m_stClientVersion
## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: bool isChannelStatusRequested() const
    def isChannelStatusRequested(self):
        return self.m_bChannelStatusRequested
    def SetChannelStatusRequested(self, bChannelStatusRequested):
        self.m_bChannelStatusRequested = bChannelStatusRequested
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if __MULTI_LANGUAGE_SYSTEM__
    def SetLanguage(self, bLanguage):
        self.m_accountTable.bLanguage = bLanguage
    def GetLanguage(self):
        return self.m_accountTable.bLanguage
##endif

    def Initialize(self):
        self.m_bDestroyed = LGEMiscellaneous.DEFINECONSTANTS.false

        self.m_pInputProcessor = None
        self.m_lpFdw = None
        self.m_sock = LGEMiscellaneous.DEFINECONSTANTS.INVALID_SOCKET
        self.m_iPhase = EPhase.PHASE_CLOSE
        self.m_dwHandle = 0

        self.m_wPort = 0
        self.m_LastTryToConnectTime = 0

        self.m_lpInputBuffer = None
        self.m_iMinInputBufferLen = 0

        self.m_dwHandshake = 0
        self.m_dwHandshakeSentTime = 0
        self.m_iHandshakeRetry = 0
        self.m_dwClientTime = 0
        self.m_bHandshaking = LGEMiscellaneous.DEFINECONSTANTS.false

        self.m_lpBufferedOutputBuffer = None
        self.m_lpOutputBuffer = None

        self.m_pkPingEvent = None
        self.m_lpCharacter = None
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memset(self.m_accountTable, 0, sizeof(self.m_accountTable))

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memset(self.m_SockAddr, 0, sizeof(self.m_SockAddr))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memset(self.m_UDPSockAddr, 0, sizeof(self.m_UDPSockAddr))

        self.m_pLogFile = None

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if ! _IMPROVED_PACKET_ENCRYPTION_
        self.m_bEncrypted = LGEMiscellaneous.DEFINECONSTANTS.false
##endif

        self.m_wP2PPort = 0
        self.m_bP2PChannel = 0
        self.m_bPong = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
        self.m_bChannelStatusRequested = LGEMiscellaneous.DEFINECONSTANTS.false

        self.m_iCurrentSequence = 0

        self.m_pkLoginKey = None
        self.m_dwLoginKey = 0

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if ! _IMPROVED_PACKET_ENCRYPTION_
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memset(self.m_adwDecryptionKey, 0, sizeof(self.m_adwDecryptionKey))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memset(self.m_adwEncryptionKey, 0, sizeof(self.m_adwEncryptionKey))
##endif

        self.m_bCRCMagicCubeIdx = 0
        self.m_dwProcCRC = 0
        self.m_dwFileCRC = 0
        self.m_bHackCRCQuery = False

        self.m_outtime = 0
        self.m_playtime = 0
        self.m_offtime = 0

        self.m_pkDisconnectEvent = None

        self.m_seq_vector.clear()

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if _IMPROVED_PACKET_ENCRYPTION_
##else
##endif


    def SetLogin(self, login):
        self.m_Login = login
    def SetLogin(self, login):
        self.m_Login = login
    def GetLogin(self):
        return self.m_Login
    def SetOutTime(self, outtime):
        self.m_outtime = outtime
    def SetOffTime(self, offtime):
        self.m_offtime = offtime
    def SetPlayTime(self, playtime):
        self.m_playtime = playtime
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    RawPacket(c_pvData, iSize)
    def ChatPacket(self, type, format, *LegacyParamArray):
        chatbuf = str(['\0' for _ in range((int)LGEMiscellaneous.CHAT_MAX_LEN + 1)])
        args = None

        ParamCount = -1
#        va_start(args, format)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        len = vsnprintf(chatbuf, sizeof(chatbuf), format, args)
#        va_end(args)

        pack_chat = packet_chat()

        pack_chat.header = byte(Globals.LG_HEADER_GC_CHAT)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        pack_chat.size = sizeof(packet_chat) + len
        pack_chat.type = type
        pack_chat.id = 0
        pack_chat.bEmpire = self.GetEmpire()

        buf = TEMP_BUFFER(8192, DefineConstants.false)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        buf.write(pack_chat, sizeof(packet_chat))
        buf.write(chatbuf, len)

        self.Packet(buf.read_peek(), buf.size())

    def push_seq(self, hdr, seq):
        if len(self.m_seq_vector)>=20:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no direct equivalent to the STL vector 'erase' method in Python:
            self.m_seq_vector.erase(self.m_seq_vector.begin())

        info = seq_t(hdr, seq)
        self.m_seq_vector.append(info)
