#Laniatus Games Studio Inc. | Python Metin II Server Warnings Statement interrupted by a preprocessor statement:
#The original statement from the file sal.h starts with:
#    __inner_fallthrough_dec
#Preprocessor-interrupted statements cannot be handled by this converter.
#The remainder of the header file sal.h is ignored.

def LoadEventFlag():
    szQuery = str(['\0' for _ in range(1024)])
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    snprintf(szQuery, sizeof(szQuery), "SELECT szName, lValue FROM quest%s WHERE dwPID = 0", GetTablePostfix())
    pmsg = std::unique_ptr(CDBManager.instance().DirectQuery(szQuery))

    pRes = pmsg.Get()
    if pRes.uiNumRows:
        row = MYSQL_ROW()
# Laniatus Games Studio Inc. |  TODO TASK: The following assignments within expression was not converted by Laniatus Games Studio Inc. T.F |:
#ORIGINAL LINE: while ((row = mysql_fetch_row(pRes->pSQLResult)))
        while (row = mysql_fetch_row(pRes.pSQLResult)):
            p = TPacketSetEventFlag()
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
            strlcpy(p.szFlagName, row[0], sizeof(p.szFlagName))
            str_to_number(p.lValue, row[1])
            sys_log(0, "EventFlag Load %s %d", p.szFlagName, p.lValue)
            m_map_lEventFlag.insert((str(p.szFlagName), p.lValue))
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
            ForwardPacket(LG_HEADER_DG_SET_EVENT_FLAG, p, sizeof(TPacketSetEventFlag))

def SetEventFlag(p):
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    ForwardPacket(LG_HEADER_DG_SET_EVENT_FLAG, p, sizeof(TPacketSetEventFlag))

    bChanged = DefineConstants.false

    it = m_map_lEventFlag.find(p.szFlagName)
    if it == m_map_lEventFlag.end():
        bChanged = ((not DefineConstants.false))
        m_map_lEventFlag.insert((str(p.szFlagName), p.lValue))
    elif it.second != p.lValue:
        bChanged = ((not DefineConstants.false))
        it.second = p.lValue

    if bChanged:
        szQuery = str(['\0' for _ in range(1024)])
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        snprintf(szQuery, sizeof(szQuery), "REPLACE INTO quest%s (dwPID, szName, szState, lValue) VALUES(0, '%s', '', %ld)", GetTablePostfix(), p.szFlagName, p.lValue)
        szQuery[1023] = '\0'

        CDBManager.instance().AsyncQuery(szQuery)
        sys_log(0, "LG_HEADER_GD_SET_EVENT_FLAG : Changed CClientmanager::SetEventFlag(%s %d) ", p.szFlagName, p.lValue)
        return
    sys_log(0, "LG_HEADER_GD_SET_EVENT_FLAG : No Changed CClientmanager::SetEventFlag(%s %d) ", p.szFlagName, p.lValue)

def SendEventFlagsOnSetup(peer):
    it = m_map_lEventFlag.begin()
    while it is not m_map_lEventFlag.end():
        p = TPacketSetEventFlag()
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        strlcpy(p.szFlagName, it.first.c_str(), sizeof(p.szFlagName))
        p.lValue = it.second
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        peer.EncodeHeader(LG_HEADER_DG_SET_EVENT_FLAG, 0, sizeof(TPacketSetEventFlag))
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        peer.Encode(p, sizeof(TPacketSetEventFlag))
        it += 1

