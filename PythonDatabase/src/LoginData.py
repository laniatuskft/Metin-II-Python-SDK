#Laniatus Games Studio Inc. | Python Metin II Server Warnings Statement interrupted by a preprocessor statement:
#The original statement from the file sal.h starts with:
#    __inner_fallthrough_dec
#Preprocessor-interrupted statements cannot be handled by this converter.
#The remainder of the header file sal.h is ignored.

class CLoginData:
    def __init__(self):
        m_dwKey = 0
# Laniatus Games Studio Inc. |  TODO TASK: The memory management function 'memset' has no equivalent in Python:
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        memset(m_adwClientKey, 0, sizeof(m_adwClientKey))
        m_dwConnectedPeerHandle = 0
        m_dwLogonTime = 0
# Laniatus Games Studio Inc. |  TODO TASK: The memory management function 'memset' has no equivalent in Python:
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        memset(m_szIP, 0, sizeof(m_szIP))
        m_bPlay = DefineConstants.false
        m_bDeleted = DefineConstants.false
        m_lastPlayTime = 0
        m_dwLastPlayerID = 0

# Laniatus Games Studio Inc. |  TODO TASK: The memory management function 'memset' has no equivalent in Python:
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        memset(m_data, 0, sizeof(TAccountTable))

    def GetAccountRef(self):
        return m_data

    def SetClientKey(self, c_pdwClientKey):
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        thecore_memcpy(m_adwClientKey, c_pdwClientKey, sizeof(uint) * 4)

#Laniatus Games Studio Inc. | Python Metin II Server Warnings Python has no equivalent to methods returning pointers to value types:
#ORIGINAL LINE: const uint * GetClientKey()
    def GetClientKey(self):
        return m_adwClientKey[0]

    def SetKey(self, dwKey):
        m_dwKey = dwKey

    def GetKey(self):
        return m_dwKey

    def SetConnectedPeerHandle(self, dwHandle):
        m_dwConnectedPeerHandle = dwHandle

    def GetConnectedPeerHandle(self):
        return m_dwConnectedPeerHandle

    def SetLogonTime(self):
        m_dwLogonTime = get_dword_time()

    def GetLogonTime(self):
        return m_dwLogonTime

    def SetIP(self, c_pszIP):
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        strlcpy(m_szIP, c_pszIP, sizeof(m_szIP))

    def GetIP(self):
        return m_szIP

    def SetPlay(self, bOn):
        if bOn:
            sys_log(0, "SetPlay on %lu %s", GetKey(), m_data.login)
            SetLogonTime()
        else:
            sys_log(0, "SetPlay off %lu %s", GetKey(), m_data.login)

        m_bPlay = bOn
        m_lastPlayTime = CClientManager.instance().GetCurrentTime()

    def IsPlay(self):
        return m_bPlay

    def SetDeleted(self, bSet):
        m_bDeleted = bSet

    def IsDeleted(self):
        return m_bDeleted

    def GetLastPlayTime(self):
        return m_lastPlayTime
    def SetPremium(self, paiPremiumTimes):
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        thecore_memcpy(m_aiPremiumTimes, paiPremiumTimes.arg_value, sizeof(m_aiPremiumTimes))

    def GetPremium(self, type):
        if type >= PREMIUM_MAX_NUM:
            return 0

        return m_aiPremiumTimes[type]

#Laniatus Games Studio Inc. | Python Metin II Server Warnings Python has no equivalent to methods returning pointers to value types:
#ORIGINAL LINE: int * GetPremiumPtr()
    def GetPremiumPtr(self):
        return m_aiPremiumTimes[0]

#Laniatus Games Studio Inc. | Python Metin II Server Warnings 'const' methods are not available in Python:
#ORIGINAL LINE: uint GetLastPlayerID() const
    def GetLastPlayerID(self):
        return m_dwLastPlayerID
    def SetLastPlayerID(self, id):
        m_dwLastPlayerID = id


