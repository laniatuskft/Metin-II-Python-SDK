class CLoginSim:
    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.auth = SPacketGDAuthLogin()
        self.login = SPacketGDLoginByKey()
        self.load = SPlayerLoadPacket()
        self.logout = SLogoutPacket()
        self.vecID = []
        self.vecIdx = 0
        self.bCheck = False

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memset(self.auth, 0, sizeof(self.auth))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memset(self.login, 0, sizeof(self.login))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memset(self.load, 0, sizeof(self.load))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memset(self.logout, 0, sizeof(self.logout))
        self.vecIdx = 0
        self.bCheck = False

    def AddPlayer(self, dwID):
        self.vecID.append(dwID)
        #sys_log(0, "AddPlayer %lu", dwID)

    def IsCheck(self):
        return self.bCheck

    def SendLogin(self):
        self.bCheck = True

        if self.IsDone():
            return

        if self.vecIdx == 0:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            db_clientdesc.DBPacket(Globals.LG_HEADER_GD_AUTH_LOGIN, 0, self.auth, sizeof(SPacketGDAuthLogin))

## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: load.player_id = vecID[vecIdx++];
        self.load.player_id = self.vecID[self.vecIdx]
        self.vecIdx += 1
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        db_clientdesc.DBPacket(Globals.LG_HEADER_GD_LOGIN_BY_KEY, 0, self.login, sizeof(SPacketGDLoginByKey))

    def SendLoad(self):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        db_clientdesc.DBPacket(Globals.LG_HEADER_GD_PLAYER_LOAD, 0, self.load, sizeof(SPlayerLoadPacket))

    def SendLogout(self):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        db_clientdesc.DBPacket(Globals.LG_HEADER_GD_LOGOUT, 0, self.logout, sizeof(SLogoutPacket))
        self.SendLogin()

    def IsDone(self):
        if self.vecIdx >= len(self.vecID):
            return True

        return False


