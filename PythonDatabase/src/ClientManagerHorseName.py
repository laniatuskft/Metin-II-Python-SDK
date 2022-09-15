#Laniatus Games Studio Inc. | Python Metin II Server Warnings Statement interrupted by a preprocessor statement:
#The original statement from the file sal.h starts with:
#    __inner_fallthrough_dec
#Preprocessor-interrupted statements cannot be handled by this converter.
#The remainder of the header file sal.h is ignored.

def UpdateHorseName(data, peer):
    szQuery = str(['\0' for _ in range(512)])

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    snprintf(szQuery, sizeof(szQuery), "REPLACE INTO horse_name VALUES(%u, '%s')", data.dwPlayerID, data.szHorseName)

    pmsg_insert = std::unique_ptr(CDBManager.instance().DirectQuery(szQuery))

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    ForwardPacket(LG_HEADER_DG_UPDATE_HORSE_NAME, data, sizeof(TPacketUpdateHorseName), 0, peer)

def AckHorseName(dwPID, peer):
    szQuery = str(['\0' for _ in range(512)])

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    snprintf(szQuery, sizeof(szQuery), "SELECT name FROM horse_name WHERE id = %u", dwPID)

    pmsg = std::unique_ptr(CDBManager.instance().DirectQuery(szQuery))

    packet = TPacketUpdateHorseName()
    packet.dwPlayerID = dwPID

    if pmsg.Get().uiNumRows == 0:
# Laniatus Games Studio Inc. |  TODO TASK: The memory management function 'memset' has no equivalent in Python:
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        memset(packet.szHorseName, 0, sizeof(packet.szHorseName))
    else:
        row = mysql_fetch_row(pmsg.Get().pSQLResult)
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        strlcpy(packet.szHorseName, row[0], sizeof(packet.szHorseName))

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    peer.EncodeHeader(LG_HEADER_DG_ACK_HORSE_NAME, 0, sizeof(TPacketUpdateHorseName))
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    peer.Encode(packet, sizeof(TPacketUpdateHorseName))

