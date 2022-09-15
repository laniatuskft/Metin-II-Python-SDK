def ChangeEmpire(empire):
    if GetEmpire() == empire:
        return 1

    szQuery = str(['\0' for _ in range(1024+1)])
    dwAID = None
    dwPID = [0 for _ in range(4)]
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    memset(dwPID, 0, sizeof(dwPID))

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        snprintf(szQuery, sizeof(szQuery), "SELECT id, pid1, pid2, pid3, pid4 FROM player_index%s WHERE pid1=%u OR pid2=%u OR pid3=%u OR pid4=%u AND empire=%u", get_table_postfix(), GetPlayerID(), GetPlayerID(), GetPlayerID(), GetPlayerID(), GetEmpire())

        msg = std::unique_ptr(DBManager.instance().DirectQuery(szQuery))

        if msg.Get().uiNumRows == 0:
            return 0

        row = mysql_fetch_row(msg.Get().pSQLResult)

        temp_ref_dwAID = RefObject(dwAID);
        str_to_number(temp_ref_dwAID, row[0])
        dwAID = temp_ref_dwAID.arg_value
        str_to_number(ushort(short(1 if dwPID[0] != 0 else 0)), row[1])
        str_to_number(ushort(short(1 if dwPID[1] != 0 else 0)), row[2])
        str_to_number(ushort(short(1 if dwPID[2] != 0 else 0)), row[3])
        str_to_number(ushort(short(1 if dwPID[3] != 0 else 0)), row[4])

    LOOP = 4

        dwGuildID = [0 for _ in range(4)]
        pGuild = [None for _ in range(4)]
        pMsg = None

        for i in range(0, LOOP):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            snprintf(szQuery, sizeof(szQuery), "SELECT guild_id FROM guild_member%s WHERE pid=%u", get_table_postfix(), dwPID[i])

            pMsg = DBManager.instance().DirectQuery(szQuery)

            if pMsg is not None:
                if pMsg.Get().uiNumRows > 0:
                    row = mysql_fetch_row(pMsg.Get().pSQLResult)

                    str_to_number(ushort(short(1 if dwGuildID[i] != 0 else 0)), row[0])

                    pGuild[i] = CGuildManager.instance().FindGuild(dwGuildID[i])

                    if pGuild[i] is not None:
                        LG_DEL_MEM(pMsg)
                        return 2
                else:
                    dwGuildID[i] = 0
                    pGuild[i] = None

                LG_DEL_MEM(pMsg)

        for i in range(0, LOOP):
            if marriage.CManager.instance().IsEngagedOrMarried(dwPID[i]) == ((not LGEMiscellaneous.DEFINECONSTANTS.false)):
                return 3

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        snprintf(szQuery, sizeof(szQuery), "UPDATE player_index%s SET empire=%u WHERE pid1=%u OR pid2=%u OR pid3=%u OR pid4=%u AND empire=%u", get_table_postfix(), empire, GetPlayerID(), GetPlayerID(), GetPlayerID(), GetPlayerID(), GetEmpire())

        msg = std::unique_ptr(DBManager.instance().DirectQuery(szQuery))

        if msg.Get().uiAffectedRows > 0:
            SetChangeEmpireCount()
            return 999

    return 0

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: int CHARACTER::GetChangeEmpireCount() const
def GetChangeEmpireCount():
    szQuery = str(['\0' for _ in range(1024+1)])
    dwAID = GetAID()

    if dwAID == 0:
        return 0

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    snprintf(szQuery, sizeof(szQuery), "SELECT change_count FROM change_empire WHERE account_id = %u", dwAID)

    pMsg = DBManager.instance().DirectQuery(szQuery)

    if pMsg is not None:
        if pMsg.Get().uiNumRows == 0:
            LG_DEL_MEM(pMsg)
            return 0

        row = mysql_fetch_row(pMsg.Get().pSQLResult)

        count = 0
        temp_ref_count = RefObject(count);
        str_to_number(temp_ref_count, row[0])
        count = temp_ref_count.arg_value

        LG_DEL_MEM(pMsg)

        return int(count)

    return 0

def SetChangeEmpireCount():
    szQuery = str(['\0' for _ in range(1024+1)])

    dwAID = GetAID()

    if dwAID == 0:
        return

    count = GetChangeEmpireCount()

    if count == 0:
        count += 1
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        snprintf(szQuery, sizeof(szQuery), "INSERT INTO change_empire VALUES(%u, %d, NOW())", dwAID, count)
    else:
        count += 1
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        snprintf(szQuery, sizeof(szQuery), "UPDATE change_empire SET change_count=%d WHERE account_id=%u", count, dwAID)

    pmsg = std::unique_ptr(DBManager.instance().DirectQuery(szQuery))

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: uint CHARACTER::GetAID() const
def GetAID():
    szQuery = str(['\0' for _ in range(1024+1)])
    dwAID = 0

    if GetDesc():
        rkTab = GetDesc().GetAccountTable()
        if rkTab.id != 0:
            return rkTab.id

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    snprintf(szQuery, sizeof(szQuery), "SELECT id FROM player_index%s WHERE pid1=%u OR pid2=%u OR pid3=%u OR pid4=%u AND empire=%u", get_table_postfix(), GetPlayerID(), GetPlayerID(), GetPlayerID(), GetPlayerID(), GetEmpire())

    pMsg = DBManager.instance().DirectQuery(szQuery)

    if pMsg is not None:
        if pMsg.Get().uiNumRows == 0:
            LG_DEL_MEM(pMsg)
            return 0

        row = mysql_fetch_row(pMsg.Get().pSQLResult)

        temp_ref_dwAID = RefObject(dwAID);
        str_to_number(temp_ref_dwAID, row[0])
        dwAID = temp_ref_dwAID.arg_value

        LG_DEL_MEM(pMsg)

        return dwAID
    else:
        return 0

