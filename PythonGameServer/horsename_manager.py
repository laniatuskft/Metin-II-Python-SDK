class CHorseNameManager(singleton):
    def _BroadcastHorseName(self, dwPlayerID, szHorseName):
        packet = tUpdateHorseName()
        packet.dwPlayerID = dwPlayerID
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        strncpy_s(packet.szHorseName, sizeof(packet.szHorseName), szHorseName, _TRUNCATE)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        db_clientdesc.DBPacket(Globals.LG_HEADER_GD_UPDATE_HORSE_NAME, 0, packet, sizeof(tUpdateHorseName))

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self._m_mapHorseNames = {}

        self._m_mapHorseNames.clear()

    def GetHorseName(self, dwPlayerID):
        iter = self._m_mapHorseNames.find(dwPlayerID)

        if iter is not self._m_mapHorseNames.end():
            return iter.second.c_str()
        else:
            return None

    def UpdateHorseName(self, dwPlayerID, szHorseName, broadcast = LGEMiscellaneous.DefineConstants.false):
        if szHorseName is None:
            #lani_err("HORSE_NAME: NULL NAME (%u)", dwPlayerID)
            szHorseName = ""

        #sys_log(0, "HORSENAME: update %u %s", dwPlayerID, szHorseName)

        self._m_mapHorseNames[dwPlayerID] = szHorseName

        if broadcast == ((not LGEMiscellaneous.DEFINECONSTANTS.false)):
            self._BroadcastHorseName(dwPlayerID, szHorseName)

    def Validate(self, pChar):
        pkAff = pChar.FindAffect(LaniatusEAffectTypes.LANIA_AFFECT_HORSE_NAME, APPLY_NONE)

        if pkAff is not None:
            if pChar.GetQuestFlag("horse_name.valid_till") < get_global_time():
                pChar.HorseSummon(LGEMiscellaneous.DEFINECONSTANTS.false, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), 0, 0)
                pChar.RemoveAffect(pkAff)
                self.UpdateHorseName(pChar.GetPlayerID(), "", ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
                pChar.HorseSummon(((not LGEMiscellaneous.DEFINECONSTANTS.false)), ((not LGEMiscellaneous.DEFINECONSTANTS.false)), 0, 0)
            else:
                ++(pkAff.lDuration)

