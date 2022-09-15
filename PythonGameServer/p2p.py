class _CCI:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.szName = str(['\0' for _ in range((int)LGEMiscellaneous.CHARACTER_NAME_MAX_LEN + 1)])
        self.dwPID = 0
        self.bEmpire = 0
        self.lMapIndex = 0
        self.bChannel = 0
        self.bLanguage = 0
        self.pkDesc = None

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if __MULTI_LANGUAGE_SYSTEM__
##endif

class P2P_MANAGER(singleton):
    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self._m_pkInputProcessor = None
        self._m_iHandleCount = 0
        self._m_set_pkPeers = _boost_func_of_void.unordered_set()
        self._m_map_pkCCI = _boost_func_of_void.unordered_map()
        self._m_map_dwPID_pkCCI = _boost_func_of_void.unordered_map()
        self._m_map_bLocale_pkCCI = _boost_func_of_void.unordered_map()
        self._m_aiEmpireUserCount = [0 for _ in range((int)LGEMiscellaneous.EMPIRE_MAX_NUM)]

        self._m_pkInputProcessor = None
        self._m_iHandleCount = 0

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memset(self._m_aiEmpireUserCount, 0, sizeof(self._m_aiEmpireUserCount))

    def close(self):
        pass

    def RegisterAcceptor(self, d):
        #sys_log(0, "P2P Acceptor opened (host %s)", d.GetHostName())
        self._m_set_pkPeers.insert(d)
        self.Boot(d)

    def UnregisterAcceptor(self, d):
        #sys_log(0, "P2P Acceptor closed (host %s)", d.GetHostName())
        self.EraseUserByDesc(d)
        self._m_set_pkPeers.erase(d)

    def RegisterConnector(self, d):
        #sys_log(0, "P2P Connector opened (host %s)", d.GetHostName())
        self._m_set_pkPeers.insert(d)
        self.Boot(d)

        p = SPacketGGSetup()
        p.bHeader = byte(Globals.LG_HEADER_GG_SETUP)
        p.wPort = p2p_port
        p.bChannel = g_bChannel
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        d.Packet(p, sizeof(p))

    def UnregisterConnector(self, d):
        it = self._m_set_pkPeers.find(d)

        if it is not self._m_set_pkPeers.end():
            #sys_log(0, "P2P Connector closed (host %s)", d.GetHostName())
            self.EraseUserByDesc(d)
            self._m_set_pkPeers.erase(it)

    def EraseUserByDesc(self, d):
        it = self._m_map_pkCCI.begin()

        while it is not self._m_map_pkCCI.end():
            pkCCI = it.second
            it += 1

            if pkCCI.pkDesc is d:
                self._Logout(pkCCI)

    def FlushOutput(self):
        it = self._m_set_pkPeers.begin()

        while it is not self._m_set_pkPeers.end():
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: DESC* pkDesc = *it++;
            pkDesc = *it
            it += 1
            pkDesc.FlushOutput()

    def Boot(self, d):
        map = CHARACTER_MANAGER.instance().GetPCMap()
        it = map.begin()

        p = SPacketGGLogin()

        while it is not map.end():
            ch = it.second
            it += 1

            p.bHeader = byte(Globals.LG_HEADER_GG_LOGIN)
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
            d.Packet(p, sizeof(p))

    def Send(self, c_pvData, iSize, except_ = None):
        it = self._m_set_pkPeers.begin()

        while it is not self._m_set_pkPeers.end():
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: DESC* pkDesc = *it++;
            pkDesc = *it
            it += 1

            if except_ is pkDesc:
                continue

            pkDesc.Packet(c_pvData, iSize)

    def Login(self, d, p):
        pkCCI = self.Find(p.szName)

        UpdateP2P = LGEMiscellaneous.DEFINECONSTANTS.false

        if None is pkCCI:
            UpdateP2P = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
            pkCCI = LG_NEW_M2 _CCI

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            trim_and_lower(p.szName, pkCCI.szName, sizeof(pkCCI.szName))

            pkCCI.dwPID = p.dwPID
            pkCCI.bEmpire = p.bEmpire
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if __MULTI_LANGUAGE_SYSTEM__
            pkCCI.bLanguage = p.bLanguage
##endif

            if p.bChannel == g_bChannel:
                if pkCCI.bEmpire < LGEMiscellaneous.EMPIRE_MAX_NUM:
                    self._m_aiEmpireUserCount[pkCCI.bEmpire] += 1
                else:
                    #lani_err("LOGIN_EMPIRE_ERROR: %d >= MAX(%d)", pkCCI.bEmpire, LGEMiscellaneous.EMPIRE_MAX_NUM)

            self._m_map_pkCCI.insert((pkCCI.szName, pkCCI))
            self._m_map_dwPID_pkCCI.insert((pkCCI.dwPID, pkCCI))

        pkCCI.lMapIndex = p.lMapIndex
        pkCCI.pkDesc = d
        pkCCI.bChannel = p.bChannel
        #sys_log(0, "P2P: Login %s", pkCCI.szName)

        CGuildManager.instance().P2PLoginMember(pkCCI.dwPID)
        CPartyManager.instance().P2PLogin(pkCCI.dwPID, pkCCI.szName)

        if UpdateP2P:
            name = pkCCI.szName
            MessengerManager.instance().P2PLogin(name)

    def Logout(self, c_pszName):
        pkCCI = self.Find(c_pszName)

        if pkCCI is None:
            return

        self._Logout(pkCCI)
        #sys_log(0, "P2P: Logout %s", c_pszName)

    def Find(self, c_pszName):
        it = TCCIMap.const_iterator()

        szName = str(['\0' for _ in range((int)LGEMiscellaneous.CHARACTER_NAME_MAX_LEN + 1)])
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        trim_and_lower(c_pszName, szName, sizeof(szName))

        it = self._m_map_pkCCI.find(szName)

        if it is self._m_map_pkCCI.end():
            return None

        return it.second

    def FindByPID(self, pid):
        it = self._m_map_dwPID_pkCCI.find(pid)

        if it is self._m_map_dwPID_pkCCI.end():
            return None
        return it.second

    def GetCount(self):
        return self._m_aiEmpireUserCount[1] + self._m_aiEmpireUserCount[2] + self._m_aiEmpireUserCount[3]

    def GetEmpireUserCount(self, idx):
        assert idx < LGEMiscellaneous.EMPIRE_MAX_NUM
        return self._m_aiEmpireUserCount[idx]

    def GetDescCount(self):
        return self._m_set_pkPeers.size()

    def GetP2PHostNames(self, hostNames):
        it = self._m_set_pkPeers.begin()

        oss = std::ostringstream(std::ostringstream.out)

        while it is not self._m_set_pkPeers.end():
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: DESC* pkDesc = *it++;
            pkDesc = *it
            it += 1

            oss << pkDesc.GetP2PHost() << " " << pkDesc.GetP2PPort() << "\n"

        hostNames += oss.str()

    def _Logout(self, pkCCI):
        if pkCCI.bChannel == g_bChannel:
            if pkCCI.bEmpire < LGEMiscellaneous.EMPIRE_MAX_NUM:
                self._m_aiEmpireUserCount[pkCCI.bEmpire] -= 1
                if self._m_aiEmpireUserCount[pkCCI.bEmpire] < 0:
                    #lani_err("m_aiEmpireUserCount[%d] < 0", pkCCI.bEmpire)
            else:
                #lani_err("LOGOUT_EMPIRE_ERROR: %d >= MAX(%d)", pkCCI.bEmpire, LGEMiscellaneous.EMPIRE_MAX_NUM)

        name = pkCCI.szName

        CGuildManager.instance().P2PLogoutMember(pkCCI.dwPID)
        CPartyManager.instance().P2PLogout(pkCCI.dwPID)
        MessengerManager.instance().P2PLogout(name)
        marriage.CManager.instance().Logout(pkCCI.dwPID)

        self._m_map_pkCCI.erase(name)
        self._m_map_dwPID_pkCCI.erase(pkCCI.dwPID)
        LG_DEL_MEM(pkCCI)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if __MULTI_LANGUAGE_SYSTEM__
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Typedefs defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
#    typedef _boost_func_of_void::unordered_map<byte, CCI*> TLocaleCCIMap;
##endif
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if __MULTI_LANGUAGE_SYSTEM__
##endif
