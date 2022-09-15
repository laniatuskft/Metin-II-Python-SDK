class CLIENT_DESC(DESC):
    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.m_iPhaseWhenSucceed = 0
        self.m_bRetryWhenClosed = False
        self.m_LastTryToConnectTime = time_t()
        self.m_tLastChannelStatusUpdateTime = time_t()
        self.m_inputDB = CInputDB()
        self.m_inputP2P = CInputP2P()

        self.m_iPhaseWhenSucceed = 0
        self.m_bRetryWhenClosed = LGEMiscellaneous.DEFINECONSTANTS.false
        self.m_LastTryToConnectTime = 0
        self.m_tLastChannelStatusUpdateTime = 0

    def close(self):
        pass

    def GetType(self):
        return EDescType.DESC_TYPE_CONNECTOR
    def Destroy(self):
        if self.m_sock is LGEMiscellaneous.DEFINECONSTANTS.INVALID_SOCKET:
            return

        P2P_MANAGER.instance().UnregisterConnector(self)

        if self is Globals.db_clientdesc:
            CPartyManager.instance().DeleteAllParty()
            CPartyManager.instance().DisablePCParty()
            CGuildManager.instance().StopAllGuildWar()

        fdwatch_del_fd(self.m_lpFdw, self.m_sock)

        #sys_log(0, "SYSTEM: closing client socket. DESC #%d", self.m_sock)

        socket_close(self.m_sock)
        self.m_sock = LGEMiscellaneous.DEFINECONSTANTS.INVALID_SOCKET

        super().Destroy()

    ## Laniatus Games Studio Inc. | NOTE: This was formerly a static local variable declaration (not allowed in Python):

    def SetPhase(self, iPhase):
        if iPhase == EPhase.PHASE_CLIENT_CONNECTING:
            #sys_log(1, "PHASE_CLIENT_DESC::CONNECTING")
            self.m_pInputProcessor = None

        elif iPhase == EPhase.PHASE_DBCLIENT:
                #sys_log(1, "PHASE_DBCLIENT")

                if not g_bAuthServer:
                    ## Laniatus Games Studio Inc. | NOTE: This static local variable declaration (not allowed in Python) has been moved just prior to the method:
                    #                        static bool bSentBoot = DefineConstants.false

                    if not SetPhase_bSentBoot:
                        SetPhase_bSentBoot = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
                        p = SPacketGDBoot()
                        p.dwItemIDRange[0] = 0
                        p.dwItemIDRange[1] = 0
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memcpy' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
                        memcpy(p.szIP, g_szPublicIP, 16)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                        self.DBPacket(byte(Globals.LG_HEADER_GD_BOOT), 0, p, sizeof(p))

                buf = TEMP_BUFFER(8192, DefineConstants.false)

                p = SPacketGDSetup()

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                memset(p, 0, sizeof(p))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                strncpy_s(p.szPublicIP, sizeof(p.szPublicIP), g_szPublicIP, _TRUNCATE)

                if not g_bAuthServer:
                    p.bChannel = g_bChannel
                    p.wListenPort = mother_port
                    p.wP2PPort = p2p_port
                    p.bAuthServer = LGEMiscellaneous.DEFINECONSTANTS.false
                    map_allow_copy(p.alMaps, 32)

                    c_set = DESC_MANAGER.instance().GetClientSet()

                    it = c_set.begin()
                    while it is not c_set.end():
                        d = *it

                        if d.GetAccountTable().id != 0:
                            p.dwLoginCount += 1
                        it += 1

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                    buf.write(p, sizeof(p))

                    if p.dwLoginCount != 0:
                        pck = SPacketLoginOnSetup()

                        it = c_set.begin()
                        while it is not c_set.end():
                            d = *it

                            r = d.GetAccountTable()

                            if r.id != 0:
                                pck.dwID = r.id
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                                strncpy_s(pck.szLogin, sizeof(pck.szLogin), r.login, _TRUNCATE)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                                strncpy_s(pck.szSocialID, sizeof(pck.szSocialID), r.social_id, _TRUNCATE)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                                strncpy_s(pck.szHost, sizeof(pck.szHost), d.GetHostName(), _TRUNCATE)
                                pck.dwLoginKey = d.GetLoginKey()
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if __MULTI_LANGUAGE_SYSTEM__
                                pck.bLanguage = r.bLanguage
##endif
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if ! _IMPROVED_PACKET_ENCRYPTION_
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memcpy' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
                                memcpy(pck.adwClientKey, d.GetDecryptionKey(), 16)
##endif

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                                buf.write(pck, sizeof(SPacketLoginOnSetup))
                            it += 1

                    #sys_log(0, "DB_SETUP current user %d size %d", p.dwLoginCount, buf.size())

                    CPartyManager.instance().EnablePCParty()
                else:
                    p.bAuthServer = 1 if ((not LGEMiscellaneous.DEFINECONSTANTS.false)) else 0
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                    buf.write(p, sizeof(p))

                self.DBPacket(byte(Globals.LG_HEADER_GD_SETUP), 0, buf.read_peek(), uint(buf.size()))
                self.m_pInputProcessor = self.m_inputDB

        elif iPhase == EPhase.PHASE_P2P:
            #sys_log(1, "PHASE_P2P")

            if self.m_lpInputBuffer:
                buffer_reset(self.m_lpInputBuffer)

            if self.m_lpOutputBuffer:
                buffer_reset(self.m_lpOutputBuffer)

            self.m_pInputProcessor = self.m_inputP2P

        elif iPhase == EPhase.PHASE_CLOSE:
            self.m_pInputProcessor = None


        self.m_iPhase = iPhase

    def Connect(self, iPhaseWhenSucceed = 0):
        if iPhaseWhenSucceed != 0:
            self.m_iPhaseWhenSucceed = iPhaseWhenSucceed

        if get_global_time() - self.m_LastTryToConnectTime < 3:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        self.m_LastTryToConnectTime = get_global_time()

        if self.m_sock is not LGEMiscellaneous.DEFINECONSTANTS.INVALID_SOCKET:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        #sys_log(0, "SYSTEM: Trying to connect to %s:%d", self.m_stHost, self.m_wPort)

        self.m_sock = socket_connect(self.m_stHost, self.m_wPort)

        if self.m_sock is not LGEMiscellaneous.DEFINECONSTANTS.INVALID_SOCKET:
            #sys_log(0, "SYSTEM: connected to server (fd %d, ptr %p)", self.m_sock, self)
            fdwatch_add_fd(self.m_lpFdw, self.m_sock, self, EFdwatch.FDW_READ, LGEMiscellaneous.DEFINECONSTANTS.false)
            fdwatch_add_fd(self.m_lpFdw, self.m_sock, self, EFdwatch.FDW_WRITE, LGEMiscellaneous.DEFINECONSTANTS.false)
            self.SetPhase(self.m_iPhaseWhenSucceed)
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
        else:
            self.SetPhase(EPhase.PHASE_CLIENT_CONNECTING)
            return LGEMiscellaneous.DEFINECONSTANTS.false

    def Setup(self, _fdw, _host, _port):
## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: m_lpFdw = _fdw;
        self.m_lpFdw.copy_from(_fdw)
        self.m_stHost = _host
        self.m_wPort = _port

        self._InitializeBuffers()

        self.m_sock = LGEMiscellaneous.DEFINECONSTANTS.INVALID_SOCKET

    def SetRetryWhenClosed(self, b):
        self.m_bRetryWhenClosed = b

    def DBPacketHeader(self, bHeader, dwHandle, dwSize):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        buffer_write(self.m_lpOutputBuffer, Globals.encode_byte(bHeader), sizeof(byte))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        buffer_write(self.m_lpOutputBuffer, Globals.encode_4bytes(int(dwHandle)), sizeof(uint))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        buffer_write(self.m_lpOutputBuffer, Globals.encode_4bytes(int(dwSize)), sizeof(uint))

    def DBPacket(self, bHeader, dwHandle, c_pvData, dwSize):
        if self.m_sock is LGEMiscellaneous.DEFINECONSTANTS.INVALID_SOCKET:
            #sys_log(0, "CLIENT_DESC [%s] trying DBPacket() while not connected", Globals.GetKnownClientDescName(self))
            return
        #sys_log(1, "DB_PACKET: header %d handle %d size %d buffer_size %d", bHeader, dwHandle, dwSize, buffer_size(self.m_lpOutputBuffer))
        self.DBPacketHeader(bHeader, dwHandle, dwSize)

        if c_pvData:
            buffer_write(self.m_lpOutputBuffer, c_pvData, dwSize)

    def Packet(self, c_pvData, iSize):
        if self.m_sock is LGEMiscellaneous.DEFINECONSTANTS.INVALID_SOCKET:
            #sys_log(0, "CLIENT_DESC [%s] trying Packet() while not connected", Globals.GetKnownClientDescName(self))
            return
        buffer_write(self.m_lpOutputBuffer, c_pvData, iSize)

    def IsRetryWhenClosed(self):
        return (0 == thecore_is_shutdowned() and self.m_bRetryWhenClosed)

    def Update(self, t):
        if not g_bAuthServer:
            self.UpdateChannelStatus(t, LGEMiscellaneous.DEFINECONSTANTS.false)

    def UpdateChannelStatus(self, t, fForce):
        CHANNELSTATUS_UPDATE_PERIOD = 5 *60 *1000
        if fForce or self.m_tLastChannelStatusUpdateTime+CHANNELSTATUS_UPDATE_PERIOD < t:
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

            channelStatus = SChannelStatus()
            channelStatus.nPort = mother_port

            if g_bNoMoreClient:
                channelStatus.bStatus = 0
            else:
                channelStatus.bStatus = 3 if iTotal > g_iFullUserCount else byte(2 if iTotal > g_iBusyUserCount else 1)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            self.DBPacket(byte(Globals.LG_HEADER_GD_UPDATE_CHANNELSTATUS), 0, channelStatus, sizeof(channelStatus))
            self.m_tLastChannelStatusUpdateTime = t

    def Reset(self):
        fdw = LPFDWATCH(self.m_lpFdw)
        host = self.m_stHost
        port = self.m_wPort

        self.Destroy()
        Initialize()

## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: m_lpFdw = fdw;
        self.m_lpFdw.copy_from(fdw)
        self.m_stHost = host
        self.m_wPort = port

        self._InitializeBuffers()

    def _InitializeBuffers(self):
        self.m_lpOutputBuffer = buffer_new(1024 * 1024)
        self.m_lpInputBuffer = buffer_new(1024 * 1024)
        self.m_iMinInputBufferLen = 1024 * 1024
