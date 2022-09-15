class TimedEventInfo(event_info_data):

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.ch = DynamicCharacterPtr()
        self.subcmd = 0
        self.left_second = 0
        self.szReason = str(['\0' for _ in range((int)LGEMiscellaneous.DEFINECONSTANTS.MAX_REASON_LEN)])

        self.ch = DynamicCharacterPtr()
        self.subcmd = 0
        self.left_second = 0
        memset(self.szReason, 0, LGEMiscellaneous.DEFINECONSTANTS.MAX_REASON_LEN)

class SendDisconnectFunc:
    def functor_method(self, d):
        if d.GetCharacter():
            d.GetCharacter().SaveReal()
            pid = d.GetCharacter().GetPlayerID()
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            db_clientdesc.DBPacketHeader(Globals.LG_HEADER_GD_FLUSH_CACHE, 0, sizeof(uint))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            db_clientdesc.Packet(pid, sizeof(uint))

            if d.GetCharacter().GetGMLevel() == EGMLevels.GM_PLAYER:
                d.GetCharacter().ChatPacket(EChatType.CHAT_TYPE_COMMAND, "quit Shutdown(SendDisconnectFunc)")

class DisconnectFunc:
    def functor_method(self, d):
        if d.GetType() == EDescType.DESC_TYPE_CONNECTOR:
            return

        if d.IsPhase(EPhase.PHASE_P2P):
            return

        if d.GetCharacter():
            d.GetCharacter().Disconnect("Shutdown(DisconnectFunc)")

        d.SetPhase(EPhase.PHASE_CLOSE)

class shutdown_event_data(event_info_data):

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.seconds = 0

        self.seconds = 0

class GotoInfo:

    def _initialize_instance_fields(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.st_name = ""
        self.empire = 0
        self.mapIndex = 0
        self.x = 0
        self.y = 0



## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to multiple constructors:
#ORIGINAL METINII C CODE: GotoInfo()
    def __init__(self):
        self._initialize_instance_fields()

        self.st_name = ""
        self.empire = 0
        self.mapIndex = 0

        self.x = 0
        self.y = 0

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to multiple constructors:
#ORIGINAL METINII C CODE: GotoInfo(const GotoInfo& c_src)
    def __init__(self, c_src):
        self._initialize_instance_fields()

        self.__copy__(c_src)

## Laniatus Games Studio Inc. | NOTE: This 'copy_from' method was converted from the original copy assignment operator:
#ORIGINAL METINII C CODE: void operator = (const GotoInfo& c_src)
    def copy_from(self, c_src):
        self.__copy__(c_src)

    def __copy__(self, c_src):
        self.st_name = c_src.st_name
        self.empire = c_src.empire
        self.mapIndex = c_src.mapIndex

        self.x = c_src.x
        self.y = c_src.y