def InsertLogonAccount(c_pszLogin, dwHandle, c_pszIP):
    szLogin = str(['\0' for _ in range(LOGIN_MAX_LEN + 1)])
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    trim_and_lower(c_pszLogin, szLogin, sizeof(szLogin))

    it = m_map_kLogonAccount.find(szLogin)

    if m_map_kLogonAccount.end() != it:
        return DefineConstants.false

    pkLD = GetLoginDataByLogin(c_pszLogin)

    if pkLD is None:
        return DefineConstants.false

    pkLD.SetConnectedPeerHandle(dwHandle)
    pkLD.SetIP(c_pszIP)

    m_map_kLogonAccount.insert(TLogonAccountMap.value_type(szLogin, pkLD))
    return ((not DefineConstants.false))

def DeleteLogonAccount(c_pszLogin, dwHandle):
    szLogin = str(['\0' for _ in range(LOGIN_MAX_LEN + 1)])
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    trim_and_lower(c_pszLogin, szLogin, sizeof(szLogin))

    it = m_map_kLogonAccount.find(szLogin)

    if it == m_map_kLogonAccount.end():
        return DefineConstants.false

    pkLD = it.second

    if pkLD.GetConnectedPeerHandle() != dwHandle:
        sys_err("%s tried to logout in other peer handle %lu, current handle %lu", szLogin, dwHandle, pkLD.GetConnectedPeerHandle())
        return DefineConstants.false

    if pkLD.IsPlay():
        pkLD.SetPlay(DefineConstants.false)

    if pkLD.IsDeleted():
        pkLD = None

    m_map_kLogonAccount.erase(it)
    return ((not DefineConstants.false))

def FindLogonAccount(c_pszLogin):
    szLogin = str(['\0' for _ in range(LOGIN_MAX_LEN + 1)])
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    trim_and_lower(c_pszLogin, szLogin, sizeof(szLogin))

    if m_map_kLogonAccount.end() == m_map_kLogonAccount.find(szLogin):
        return DefineConstants.false

    return ((not DefineConstants.false))

def QUERY_LOGIN_BY_KEY(pkPeer, dwHandle, p):

    pkLoginData = GetLoginData(p.dwLoginKey)
    szLogin = str(['\0' for _ in range(LOGIN_MAX_LEN + 1)])
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    trim_and_lower(p.szLogin, szLogin, sizeof(szLogin))

    if pkLoginData is None:
        sys_log(0, "LOGIN_BY_KEY key not exist %s %lu", szLogin, p.dwLoginKey)
        pkPeer.EncodeReturn(LG_HEADER_DG_LOGIN_NOT_EXIST, dwHandle)
        return

    r = pkLoginData.GetAccountRef()

    if FindLogonAccount(r.login):
        sys_log(0, "LOGIN_BY_KEY already login %s %lu", r.login, p.dwLoginKey)
        ptog = TPacketDGLoginAlready()
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        strlcpy(ptog.szLogin, szLogin, sizeof(ptog.szLogin))
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        pkPeer.EncodeHeader(LG_HEADER_DG_LOGIN_ALREADY, dwHandle, sizeof(TPacketDGLoginAlready))
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        pkPeer.Encode(ptog, sizeof(TPacketDGLoginAlready))
        return

    if strcasecmp(r.login, szLogin):
        sys_log(0, "LOGIN_BY_KEY login differ %s %lu input %s", r.login, p.dwLoginKey, szLogin)
        pkPeer.EncodeReturn(LG_HEADER_DG_LOGIN_NOT_EXIST, dwHandle)
        return

# Laniatus Games Studio Inc. |  TODO TASK: The memory management function 'memcmp' has no equivalent in Python:
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    if memcmp(pkLoginData.GetClientKey(), p.adwClientKey, sizeof(uint) * 4):
        pdwClientKey = pkLoginData.GetClientKey()

        sys_log(0, "LOGIN_BY_KEY client key differ %s %lu %lu %lu %lu, %lu %lu %lu %lu", r.login, p.adwClientKey[0], p.adwClientKey[1], p.adwClientKey[2], p.adwClientKey[3], pdwClientKey[0], pdwClientKey[1], pdwClientKey[2], pdwClientKey[3])

        pkPeer.EncodeReturn(LG_HEADER_DG_LOGIN_NOT_EXIST, dwHandle)
        return

    pkTab = TAccountTable()
# Laniatus Games Studio Inc. |  TODO TASK: The memory management function 'memset' has no equivalent in Python:
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    memset(pkTab, 0, sizeof(TAccountTable))

    pkTab.id = r.id
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    trim_and_lower(r.login, pkTab.login, sizeof(pkTab.login))
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    strlcpy(pkTab.passwd, r.passwd, sizeof(pkTab.passwd))
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    strlcpy(pkTab.social_id, r.social_id, sizeof(pkTab.social_id))
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    strlcpy(pkTab.status, "OK", sizeof(pkTab.status))
# Laniatus Games Studio Inc. |  TODO TASK: There is no preprocessor in Python:
##if __MULTI_LANGUAGE_SYSTEM__
    pkTab.bLanguage = r.bLanguage
##endif

    info = ClientHandleInfo(dwHandle)
    info.pAccountTable = pkTab
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    strlcpy(info.ip, p.szIP, sizeof(info.ip))

    sys_log(0, "LOGIN_BY_KEY success %s %lu %s", r.login, p.dwLoginKey, info.ip)
    szQuery = str(['\0' for _ in range(DefineConstants.QUERY_MAX_LEN)])
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    snprintf(szQuery, sizeof(szQuery), "SELECT pid1, pid2, pid3, pid4, empire FROM player_index%s WHERE id=%u", GetTablePostfix(), r.id)
    CDBManager.instance().ReturnQuery(szQuery, QID_LOGIN_BY_KEY, pkPeer.GetHandle(), info)

def RESULT_LOGIN_BY_KEY(peer, msg):
    qi = msg.pvUserData
    info = qi.pvData

    if msg.uiSQLErrno != 0:
        peer.EncodeReturn(LG_HEADER_DG_LOGIN_NOT_EXIST, info.dwHandle)
        info = None
        return

    szQuery = str(['\0' for _ in range(DefineConstants.QUERY_MAX_LEN)])

    if msg.Get().uiNumRows == 0:
        account_id = info.pAccountTable.id
        szQuery = str(['\0' for _ in range(DefineConstants.QUERY_MAX_LEN)])
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        snprintf(szQuery, sizeof(szQuery), "SELECT pid1, pid2, pid3, pid4, empire FROM player_index%s WHERE id=%u", GetTablePostfix(), account_id)
        pMsg = std::unique_ptr(CDBManager.instance().DirectQuery(szQuery, SQL_PLAYER))

        sys_log(0, "RESULT_LOGIN_BY_KEY FAIL player_index's NULL : ID:%d", account_id)

        if pMsg.Get().uiNumRows == 0:
            sys_log(0, "RESULT_LOGIN_BY_KEY FAIL player_index's NULL : ID:%d", account_id)
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
            snprintf(szQuery, sizeof(szQuery), "INSERT INTO player_index%s (id) VALUES(%u)", GetTablePostfix(), info.pAccountTable.id)
            CDBManager.instance().ReturnQuery(szQuery, QID_PLAYER_INDEX_CREATE, peer.GetHandle(), info)
        return

    row = mysql_fetch_row(msg.Get().pSQLResult)

    col = 0

    while col < PLAYER_PER_ACCOUNT:
        str_to_number(info.pAccountTable.players[col].dwID, row[col])
        col += 1

#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(info->pAccountTable->bEmpire, row[col++]);
    str_to_number(info.pAccountTable.bEmpire, row[col])
    col += 1
    info.account_index = 1

#Laniatus Games Studio Inc. | Python Metin II Server Note 'extern' variable declarations are not required in Python:
#    extern str g_stLocale
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    snprintf(szQuery, sizeof(szQuery), "SELECT id," + "name," + "job," + "level," + "playtime," + "st," + "ht," + "dx," + "iq," + "part_main," + "part_hair," + "part_acce," + "x," + "y," + "LG_SKILL_group," + "change_name " + "FROM player%s WHERE account_id=%u",GetTablePostfix(), info.pAccountTable.id)

    CDBManager.instance().ReturnQuery(szQuery, QID_LOGIN, peer.GetHandle(), info)

def RESULT_PLAYER_INDEX_CREATE(pkPeer, msg):
    qi = msg.pvUserData
    info = qi.pvData

    szQuery = str(['\0' for _ in range(DefineConstants.QUERY_MAX_LEN)])
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    snprintf(szQuery, sizeof(szQuery), "SELECT pid1, pid2, pid3, pid4, empire FROM player_index%s WHERE id=%u", GetTablePostfix(), info.pAccountTable.id)
    CDBManager.instance().ReturnQuery(szQuery, QID_LOGIN_BY_KEY, pkPeer.GetHandle(), info)

def RESULT_LOGIN(peer, msg):
    qi = msg.pvUserData
    info = qi.pvData

    if info.account_index == 0:
        if msg.Get().uiNumRows == 0:
            sys_log(0, "RESULT_LOGIN: no account")
            peer.EncodeHeader(LG_HEADER_DG_LOGIN_NOT_EXIST, info.dwHandle, 0)
            info = None
            return

        info.pAccountTable = CreateAccountTableFromRes(msg.Get().pSQLResult)

        if not info.pAccountTable:
            sys_log(0, "RESULT_LOGIN: no account : WRONG_PASSWD")
            peer.EncodeReturn(LG_HEADER_DG_LOGIN_WRONG_PASSWD, info.dwHandle)
            info = None
        else:
            info.account_index += 1

            queryStr = str(['\0' for _ in range(512)])
#Laniatus Games Studio Inc. | Python Metin II Server Note 'extern' variable declarations are not required in Python:
#            extern str g_stLocale
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
            snprintf(queryStr, sizeof(queryStr), "SELECT id," + "name," + "job," + "level," + "playtime," + "st," + "ht," + "dx," + "iq," + "part_main," + "part_hair," + "part_acce," + "x," + "y," + "LG_SKILL_group," + "change_name " + "FROM player%s WHERE account_id=%u",GetTablePostfix(), info.pAccountTable.id)

            CDBManager.instance().ReturnQuery(queryStr, QID_LOGIN, peer.GetHandle(), info)
        return
    else:
        if not info.pAccountTable:
            peer.EncodeReturn(LG_HEADER_DG_LOGIN_WRONG_PASSWD, info.dwHandle)
            info = None
            return

        if not InsertLogonAccount(info.pAccountTable.login, peer.GetHandle(), info.ip):
            sys_log(0, "RESULT_LOGIN: already logon %s", info.pAccountTable.login)

            p = TPacketDGLoginAlready()
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
            strlcpy(p.szLogin, info.pAccountTable.login, sizeof(p.szLogin))

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
            peer.EncodeHeader(LG_HEADER_DG_LOGIN_ALREADY, info.dwHandle, sizeof(TPacketDGLoginAlready))
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
            peer.Encode(p, sizeof(p))
        else:
            sys_log(0, "RESULT_LOGIN: login success %s rows: %lu", info.pAccountTable.login, msg.Get().uiNumRows)

            if msg.Get().uiNumRows > 0:
                CreateAccountPlayerDataFromRes(msg.Get().pSQLResult, info.pAccountTable)

            p = GetLoginDataByLogin(info.pAccountTable.login)
# Laniatus Games Studio Inc. |  TODO TASK: The memory management function 'memcpy' has no equivalent in Python:
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
            memcpy(p.GetAccountRef(), info.pAccountTable, sizeof(TAccountTable))

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
            peer.EncodeHeader(LG_HEADER_DG_LOGIN_SUCCESS, info.dwHandle, sizeof(TAccountTable))
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
            peer.Encode(info.pAccountTable, sizeof(TAccountTable))


        info.pAccountTable = None
        info.pAccountTable = None
        info = None

def QUERY_LOGOUT(peer, dwHandle, data):
    packet = data

    if !*packet.login:
        return

    pLoginData = GetLoginDataByLogin(packet.login)

    if pLoginData is None:
        return

    pid = [0 for _ in range(PLAYER_PER_ACCOUNT)]

    n = 0
    while n < PLAYER_PER_ACCOUNT:
        if pLoginData.GetAccountRef().players[n].dwID == 0:
            if g_test_server:
                sys_log(0, "LOGOUT %s %d", packet.login, pLoginData.GetAccountRef().players[n].dwID)
            continue

        pid[n] = pLoginData.GetAccountRef().players[n].dwID

        if g_log:
            sys_log(0, "LOGOUT InsertLogoutPlayer %s %d", packet.login, pid[n])

        InsertLogoutPlayer(pid[n])
        n += 1

    if DeleteLogonAccount(packet.login, peer.GetHandle()):
        if g_log:
            sys_log(0, "LOGOUT %s ", packet.login)

def QUERY_CHANGE_NAME(peer, dwHandle, p):
    queryStr = str(['\0' for _ in range(DefineConstants.QUERY_MAX_LEN)])

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    snprintf(queryStr, sizeof(queryStr), "SELECT COUNT(*) as count FROM player%s WHERE name='%s' AND id <> %u", GetTablePostfix(), p.name, p.pid)

    pMsg = std::unique_ptr(CDBManager.instance().DirectQuery(queryStr, SQL_PLAYER))

    if pMsg.Get().uiNumRows:
        if not pMsg.Get().pSQLResult:
            peer.EncodeHeader(LG_HEADER_DG_PLAYER_CREATE_FAILED, dwHandle, 0)
            return

        row = mysql_fetch_row(pMsg.Get().pSQLResult)

        if *row[0] != '0':
            peer.EncodeHeader(LG_HEADER_DG_PLAYER_CREATE_ALREADY, dwHandle, 0)
            return
    else:
        peer.EncodeHeader(LG_HEADER_DG_PLAYER_CREATE_FAILED, dwHandle, 0)
        return

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    snprintf(queryStr, sizeof(queryStr), "UPDATE player%s SET name='%s',change_name=0 WHERE id=%u", GetTablePostfix(), p.name, p.pid)

    pMsg0 = std::unique_ptr(CDBManager.instance().DirectQuery(queryStr, SQL_PLAYER))

    pdg = TPacketDGChangeName()
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    peer.EncodeHeader(LG_HEADER_DG_CHANGE_NAME, dwHandle, sizeof(TPacketDGChangeName))
    pdg.pid = p.pid
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    strlcpy(pdg.name, p.name, sizeof(pdg.name))
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    peer.Encode(pdg, sizeof(TPacketDGChangeName))

