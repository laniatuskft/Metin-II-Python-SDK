class CLoginData:
    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self._m_dwKey = 0
        self._m_adwClientKey = [0 for _ in range(4)]
        self._m_dwConnectedPeerHandle = 0
        self._m_dwLogonTime = 0
        self._m_lRemainSecs = 0
        self._m_szIP = str(['\0' for _ in range((int)LGEMiscellaneous.LG_MAX_HOST_LENGTH+1)])
        self._m_bDeleted = False
        self._m_stLogin = ""
        self._m_aiPremiumTimes = [0 for _ in range((int)EPremiumTypes.PREMIUM_MAX_NUM)]

        self._m_dwKey = 0
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memset(self._m_adwClientKey, 0, sizeof(self._m_adwClientKey))
        self._m_dwConnectedPeerHandle = 0
        self._m_dwLogonTime = 0
        self._m_lRemainSecs = 0
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memset(self._m_szIP, 0, sizeof(self._m_szIP))
        self._m_bDeleted = LGEMiscellaneous.DEFINECONSTANTS.false
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memset(self._m_aiPremiumTimes, 0, sizeof(self._m_aiPremiumTimes))

    def SetClientKey(self, c_pdwClientKey):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memcpy' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memcpy(self._m_adwClientKey, c_pdwClientKey, sizeof(uint) * 4)

## Laniatus Games Studio Inc. | WARNING: Python has no equivalent to methods returning pointers to value types:
#ORIGINAL METINII C CODE: const uint * GetClientKey()
    def GetClientKey(self):
        return self._m_adwClientKey[0]

    def SetKey(self, dwKey):
        self._m_dwKey = dwKey

    def GetKey(self):
        return self._m_dwKey

    def SetLogin(self, c_pszLogin):
        self._m_stLogin = c_pszLogin

    def GetLogin(self):
        return self._m_stLogin

    def SetConnectedPeerHandle(self, dwHandle):
        self._m_dwConnectedPeerHandle = dwHandle

    def GetConnectedPeerHandle(self):
        return self._m_dwConnectedPeerHandle

    def SetLogonTime(self):
        self._m_dwLogonTime = get_dword_time()

    def GetLogonTime(self):
        return self._m_dwLogonTime

    def SetIP(self, c_pszIP):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        strncpy_s(self._m_szIP, sizeof(self._m_szIP), c_pszIP, _TRUNCATE)

    def GetIP(self):
        return self._m_szIP

    def SetRemainSecs(self, l):
        self._m_lRemainSecs = l
        #sys_log(0, "SetRemainSecs %s %d", self._m_stLogin, self._m_lRemainSecs)

    def GetRemainSecs(self):
        return self._m_lRemainSecs

    def SetDeleted(self, bSet):
        self._m_bDeleted = bSet

    def IsDeleted(self):
        return self._m_bDeleted

    def SetPremium(self, paiPremiumTimes):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memcpy' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memcpy(self._m_aiPremiumTimes, paiPremiumTimes.arg_value, sizeof(self._m_aiPremiumTimes))

    def GetPremium(self, type):
        if type >= EPremiumTypes.PREMIUM_MAX_NUM:
            return 0

        return self._m_aiPremiumTimes[type]

## Laniatus Games Studio Inc. | WARNING: Python has no equivalent to methods returning pointers to value types:
#ORIGINAL METINII C CODE: int * GetPremiumPtr()
    def GetPremiumPtr(self):
        return self._m_aiPremiumTimes[0]
