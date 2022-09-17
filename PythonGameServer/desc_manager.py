import math

## Laniatus Games Studio Inc. | NOTE: Python has no need of forward class declarations:
#class CLoginKey

class DESC_MANAGER(singleton):

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self._m_bDisconnectInvalidCRC = False
        self._m_map_handle_random_key = {}
        self._m_set_pkClientDesc = _boost_func_of_void.unordered_set()
        self._m_set_pkDesc = _boost_func_of_void.unordered_set()
        self._m_map_handle = {}
        self._m_map_handshake = {}
        self._m_map_loginName = _boost_func_of_void.unordered_map()
        self._m_map_pkLoginKey = {}
        self._m_iSocketsConnected = 0
        self._m_iHandleCount = 0
        self._m_iLocalUserCount = 0
        self._m_aiEmpireUserCount = [0 for _ in range((int)LGEMiscellaneous.EMPIRE_MAX_NUM)]
        self._m_bDestroyed = False

        self._m_bDestroyed = LGEMiscellaneous.DEFINECONSTANTS.false
        self.Initialize()

    def close(self):
        self.Destroy()

    def Initialize(self):
        self._m_iSocketsConnected = 0
        self._m_iHandleCount = 0
        self._m_iLocalUserCount = 0
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memset(self._m_aiEmpireUserCount, 0, sizeof(self._m_aiEmpireUserCount))
        self._m_bDisconnectInvalidCRC = LGEMiscellaneous.DEFINECONSTANTS.false

    def Destroy(self):
        if self._m_bDestroyed:
            return
        self._m_bDestroyed = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        LaniatusDefVariables = self._m_set_pkDesc.begin()

        while LaniatusDefVariables is not self._m_set_pkDesc.end():
            d = *i
            ci = auto(i)
            LaniatusDefVariables += 1

            if d.GetType() == EDescType.DESC_TYPE_CONNECTOR:
                continue

            if d.IsPhase(EPhase.PHASE_P2P):
                continue

            self.DestroyDesc(d, LGEMiscellaneous.DEFINECONSTANTS.false)
            self._m_set_pkDesc.erase(ci)

        LaniatusDefVariables = self._m_set_pkDesc.begin()

        while LaniatusDefVariables is not self._m_set_pkDesc.end():
            d = *i
            ci = auto(i)
            LaniatusDefVariables += 1

            self.DestroyDesc(d, LGEMiscellaneous.DEFINECONSTANTS.false)
            self._m_set_pkDesc.erase(ci)

        self._m_set_pkClientDesc.clear()
        self._m_map_loginName.clear()
        self._m_map_handle.clear()

        self.Initialize()

    ## Laniatus Games Studio Inc. | NOTE: This was formerly a static local variable declaration (not allowed in Python):
    ## Laniatus Games Studio Inc. | NOTE: This was formerly a static local variable declaration (not allowed in Python):

    def AcceptDesc(self, fdw, s):
        desc = socket_t()
        newd = None
        ## Laniatus Games Studio Inc. | NOTE: This static local variable declaration (not allowed in Python) has been moved just prior to the method:
        #        static struct sockaddr_in peer
        ## Laniatus Games Studio Inc. | NOTE: This static local variable declaration (not allowed in Python) has been moved just prior to the method:
        #        static char host[LG_MAX_HOST_LENGTH + 1]

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((desc = socket_accept(s, &peer)) == -1)
        if (desc = socket_accept(s, peer)) == -1:
            return None

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        strncpy_s(AcceptDesc_host, sizeof(AcceptDesc_host), inet_ntoa(peer.sin_addr), _TRUNCATE)

        if Globals.IsValidIP(Globals.admin_ip, AcceptDesc_host) == 0:
            if self._m_iSocketsConnected >= LGEMiscellaneous.DEFINECONSTANTS.MAX_ALLOW_USER:
                #lani_err("max connection reached. MAX_ALLOW_USER = %d", LGEMiscellaneous.DEFINECONSTANTS.MAX_ALLOW_USER)
                socket_close(desc)
                return None

        newd = LG_NEW_M2 DESC
        handshake = self.CreateHandshake()

        self._m_iHandleCount += 1
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: if (!newd->Setup(fdw, desc, peer, ++m_iHandleCount, handshake))
        if not newd.Setup(LPFDWATCH(fdw), socket_t(desc), peer, uint(self._m_iHandleCount), handshake):
            socket_close(desc)
            LG_DEL_MEM(newd)
            return None

        self._m_map_handshake.insert(DESC_HANDSHAKE_MAP.value_type(handshake, newd))
        self._m_map_handle.insert(DESC_HANDLE_MAP.value_type(newd.GetHandle(), newd))

        self._m_set_pkDesc.insert(newd)
        self._m_iSocketsConnected += 1
        return (newd)

    def AcceptP2PDesc(self, fdw, bind_fd):
        fd = socket_t()
        peer = sockaddr_in()
        host = str(['\0' for _ in range((int)LGEMiscellaneous.LG_MAX_HOST_LENGTH + 1)])

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((fd = socket_accept(bind_fd, &peer)) == -1)
        if (fd = socket_accept(bind_fd, peer)) == -1:
            return None

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        strncpy_s(host, sizeof(host), inet_ntoa(peer.sin_addr), _TRUNCATE)

        pkDesc = LG_NEW_M2 DESC_P2P

        if not pkDesc.Setup(LPFDWATCH(fdw), socket_t(fd), host, peer.sin_port):
            #lani_err("DESC_MANAGER::AcceptP2PDesc : Setup failed")
            socket_close(fd)
            LG_DEL_MEM(pkDesc)
            return None

        self._m_set_pkDesc.insert(pkDesc)
        self._m_iSocketsConnected += 1

        #sys_log(0, "DESC_MANAGER::AcceptP2PDesc  %s:%u", host, peer.sin_port)
        P2P_MANAGER.instance().RegisterAcceptor(pkDesc)
        return (pkDesc)

    def DestroyDesc(self, d, bEraseFromSet = (!LGEMiscellaneous.DefineConstants.false)):
        if bEraseFromSet:
            self._m_set_pkDesc.erase(d)

        if d.GetHandshake() != 0:
            self._m_map_handshake.pop(d.GetHandshake())

        if d.GetHandle() != 0:
            self._m_map_handle.pop(d.GetHandle())
        else:
            self._m_set_pkClientDesc.erase(d)

        d.Destroy()

        LG_DEL_MEM(d)
        self._m_iSocketsConnected -= 1

    def CreateHandshake(self):
        crc_buf = str(['\0' for _ in range(8)])
        crc = None
        it = DESC_HANDSHAKE_MAP.iterator()

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There are no gotos or labels in Python:
        RETRY:
        condition = True
        while condition:
            val = math.fmod(thecore_random(), (1024 * 1024))

            (crc_buf) = val
            crc_buf[1:] = get_global_time()

            crc = GetCRC32(crc_buf, 8)
            it = self._m_map_handshake.find(crc)
            condition = it is not self._m_map_handshake.end()

        if crc == 0:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There are no gotos or labels in Python:
            goto RETRY

        return (crc)

    def CreateConnectionDesc(self, fdw, host, port, iPhaseWhenSucceed, bRetryWhenClosed):
        newd = None

        newd = LG_NEW_M2 CLIENT_DESC

        newd.Setup(LPFDWATCH(fdw), host, port)
        newd.Connect(iPhaseWhenSucceed)
        newd.SetRetryWhenClosed(bRetryWhenClosed)

        self._m_set_pkDesc.insert(newd)
        self._m_set_pkClientDesc.insert(newd)

        self._m_iSocketsConnected += 1
        return (newd)

    def TryConnect(self):
        f = FuncTryConnect()
        std::for_each(self._m_set_pkClientDesc.begin(), self._m_set_pkClientDesc.end(), f.functor_method)

    def FindByHandle(self, handle):
        it = self._m_map_handle.find(handle)

        if self._m_map_handle.end() is it:
            return None

        return (it.second)

    def FindByHandshake(self, dwHandshake):
        it = self._m_map_handshake.find(dwHandshake)

        if it is self._m_map_handshake.end():
            return None

        return (it.second)

    def FindByCharacterName(self, name):
        it = std::find_if(self._m_set_pkDesc.begin(), self._m_set_pkDesc.end(), name_with_desc_func(name))
        return None if (it is self._m_set_pkDesc.end()) else (*it)

    def FindByLoginName(self, login):
        it = self._m_map_loginName.find(login)

        if self._m_map_loginName.end() == it:
            return None

        return (it.second)

    def ConnectAccount(self, login, d):
        self._m_map_loginName.insert(DESC_LOGINNAME_MAP.value_type(login,d))

    def DisconnectAccount(self, login):
        self._m_map_loginName.erase(login)

    def DestroyClosed(self):
        LaniatusDefVariables = self._m_set_pkDesc.begin()

        while LaniatusDefVariables is not self._m_set_pkDesc.end():
            d = *i
            ci = auto(i)
            LaniatusDefVariables += 1

            if d.IsPhase(EPhase.PHASE_CLOSE):
                if d.GetType() == EDescType.DESC_TYPE_CONNECTOR:
                    client_desc = d

                    if client_desc.IsRetryWhenClosed():
                        client_desc.Reset()
                        continue

                self.DestroyDesc(d, LGEMiscellaneous.DEFINECONSTANTS.false)
                self._m_set_pkDesc.erase(ci)

    def UpdateLocalUserCount(self):
        c_ref_set = self.GetClientSet()
        f = FuncWho()
        f = std::for_each(c_ref_set.begin(), c_ref_set.end(), f.functor_method)

        self._m_iLocalUserCount = f.iTotalCount
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memcpy' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memcpy(self._m_aiEmpireUserCount, f.aiEmpireUserCount, sizeof(self._m_aiEmpireUserCount))

        self._m_aiEmpireUserCount[1] += P2P_MANAGER.instance().GetEmpireUserCount(1)
        self._m_aiEmpireUserCount[2] += P2P_MANAGER.instance().GetEmpireUserCount(2)
        self._m_aiEmpireUserCount[3] += P2P_MANAGER.instance().GetEmpireUserCount(3)

    def GetLocalUserCount(self):
        return uint(self._m_iLocalUserCount)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to pointers to value types:
#ORIGINAL METINII C CODE: void GetUserCount(int & iTotal, int ** paiEmpireUserCount, int & iLocalCount)
    def GetUserCount(self, iTotal, paiEmpireUserCount, iLocalCount):
        paiEmpireUserCount[0] = self._m_aiEmpireUserCount[0]

        iCount = P2P_MANAGER.instance().GetCount()
        if iCount < 0:
            #lani_err("P2P_MANAGER::instance().GetCount() == -1")
        iTotal.arg_value = self._m_iLocalUserCount + iCount
        iLocalCount.arg_value = self._m_iLocalUserCount

    def GetClientSet(self):
        return _boost_func_of_void.unordered_set(self._m_set_pkDesc)

    def MakeRandomKey(self, dwHandle):
        random_key = thecore_random()
        self._m_map_handle_random_key.update({dwHandle: random_key})
        return random_key

    def GetRandomKey(self, dwHandle, prandom_key):
        it = self._m_map_handle_random_key.find(dwHandle)

        if it is self._m_map_handle_random_key.end():
            return LGEMiscellaneous.DEFINECONSTANTS.false

        prandom_key.arg_value = it.second
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def CreateLoginKey(self, d):
        dwKey = 0

        condition = True
        while condition:
            dwKey = number(1, numeric_limits.max())

            if dwKey in self._m_map_pkLoginKey.keys():
                continue

            pkKey = LG_NEW_M2 CLoginKey(dwKey, d)
            d.SetLoginKey(pkKey)
            self._m_map_pkLoginKey.update({dwKey: pkKey})
            break
            condition = 1

        return dwKey

    def FindByLoginKey(self, dwKey):
        it = self._m_map_pkLoginKey.find(dwKey)

        if it is self._m_map_pkLoginKey.end():
            return None

        return it.second.m_pkDesc

    def ProcessExpiredLoginKey(self):
        dwCurrentTime = get_dword_time()
        it = self._m_map_pkLoginKey.begin()

        while it is not self._m_map_pkLoginKey.end():
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: auto it2 = it++;
            it2 = it
            it += 1

            if it2.second.m_dwExpireTime == 0:
                continue

            if dwCurrentTime - it2.second.m_dwExpireTime > 60000:
                LG_DEL_MEM(it2.second)
                self._m_map_pkLoginKey.pop(it2)

    def IsDisconnectInvalidCRC(self):
        return self._m_bDisconnectInvalidCRC
    def SetDisconnectInvalidCRCMode(self, bMode):
        self._m_bDisconnectInvalidCRC = bMode
    def IsP2PDescExist(self, szHost, wPort):
        it = self._m_set_pkClientDesc.begin()

        while it is not self._m_set_pkClientDesc.end():
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: CLIENT_DESC* d = *(it++);
            d = *(it)
            it += 1

            if (not strcmp(d.GetP2PHost(), szHost)) and d.GetP2PPort() == wPort:
                return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        return LGEMiscellaneous.DEFINECONSTANTS.false



class valid_ip:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.ip = '\0'
        self.network = 0
        self.mask = 0


class name_with_desc_func:

    def __init__(self, name):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.m_name = '\0'

        self.m_name = name

    def functor_method(self, d):
        if d.GetCharacter() is not None and not strcmp(d.GetCharacter().GetName(LOCALE_LANIATUS), self.m_name):
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        return LGEMiscellaneous.DEFINECONSTANTS.false

class FuncTryConnect:
    def functor_method(self, d):
        (d).Connect()

class FuncWho:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.iTotalCount = 0
        self.aiEmpireUserCount = [0 for _ in range((int)LGEMiscellaneous.EMPIRE_MAX_NUM)]

        self.iTotalCount = 0
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memset(self.aiEmpireUserCount, 0, sizeof(self.aiEmpireUserCount))

    def functor_method(self, d):
        if d.GetCharacter():
            self.iTotalCount += 1
            self.aiEmpireUserCount[d.GetEmpire()] += 1
