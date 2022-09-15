#Laniatus Games Studio Inc. | Python Metin II Server Warnings Statement interrupted by a preprocessor statement:
#The original statement from the file sal.h starts with:
#    __inner_fallthrough_dec
#Preprocessor-interrupted statements cannot be handled by this converter.
#The remainder of the header file sal.h is ignored.

class SItemAward:

class ItemAwardManager(singleton):
    def __init__(self):
        pass

    def close(self):
        pass

    def RequestLoad(self):
        szQuery = str(['\0' for _ in range(DefineConstants.QUERY_MAX_LEN)])
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        snprintf(szQuery, sizeof(szQuery), "SELECT id,login,vnum,count,socket0,socket1,socket2,mall,why FROM item_award WHERE taken_time IS NULL and id > %d", g_dwLastCachedItemAwardID)
        CDBManager.instance().ReturnQuery(szQuery, QID_ITEM_AWARD_LOAD, 0, None)

    def Load(self, pMsg):
        pRes = pMsg.Get().pSQLResult

        i = 0
        while i < pMsg.Get().uiNumRows:
            row = mysql_fetch_row(pRes)
            col = 0

            dwID = 0
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(dwID, row[col++]);
            str_to_number(dwID, row[col])
            col += 1

            if m_map_award.find(dwID) != m_map_award.end():
                continue

            kData = SItemAward()
# Laniatus Games Studio Inc. |  TODO TASK: The memory management function 'memset' has no equivalent in Python:
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
            memset(kData, 0, sizeof(SItemAward))

            kData.dwID = dwID
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: trim_and_lower(row[col++], kData->szLogin, sizeof(kData->szLogin));
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
            trim_and_lower(row[col], kData.szLogin, sizeof(kData.szLogin))
            col += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(kData->dwVnum, row[col++]);
            str_to_number(kData.dwVnum, row[col])
            col += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(kData->dwCount, row[col++]);
            str_to_number(kData.dwCount, row[col])
            col += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(kData->dwSocket0, row[col++]);
            str_to_number(kData.dwSocket0, row[col])
            col += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(kData->dwSocket1, row[col++]);
            str_to_number(kData.dwSocket1, row[col])
            col += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(kData->dwSocket2, row[col++]);
            str_to_number(kData.dwSocket2, row[col])
            col += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(kData->bMall, row[col++]);
            str_to_number(kData.bMall, row[col])
            col += 1

            if row[col]:
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
                strlcpy(kData.szWhy, row[col], sizeof(kData.szWhy))
                whyStr = kData.szWhy
                cmdStr = ""
                strcpy(cmdStr,whyStr)
                command = ""
                strcpy(command,CClientManager.instance().GetCommand(cmdStr))
                if not(strcmp(command,"GIFT")):
                    giftData = TPacketItemAwardInfromer()
                    strcpy(giftData.login, kData.szLogin)
                    strcpy(giftData.command, command)
                    giftData.vnum = kData.dwVnum
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
                    CClientManager.instance().ForwardPacket(LG_HEADER_DG_ITEMAWARD_INFORMER, giftData, sizeof(TPacketItemAwardInfromer))

            m_map_award.insert((dwID, kData))

            printf("ITEM_AWARD load id %u bMall %d \n", kData.dwID, kData.bMall)
            sys_log(0, "ITEM_AWARD: load id %lu login %s vnum %lu count %u socket %lu", kData.dwID, kData.szLogin, kData.dwVnum, kData.dwCount, kData.dwSocket0)
            kSet = m_map_kSetAwardByLogin[kData.szLogin]
            kSet.insert(kData)

            if dwID > g_dwLastCachedItemAwardID:
                g_dwLastCachedItemAwardID = dwID
            i += 1

    def GetByLogin(self, c_pszLogin):
        it = m_map_kSetAwardByLogin.find(c_pszLogin)

        if it == m_map_kSetAwardByLogin.end():
            return None

        return it.second

    def Taken(self, dwAwardID, dwItemID):
        it = m_map_award.find(dwAwardID)

        if it == m_map_award.end():
            sys_log(0, "ITEM_AWARD: Taken ID not exist %lu", dwAwardID)
            return

        k = it.second
        k.bTaken = ((not DefineConstants.false))

        szQuery = str(['\0' for _ in range(DefineConstants.QUERY_MAX_LEN)])

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        snprintf(szQuery, sizeof(szQuery), "UPDATE item_award SET taken_time=NOW(),item_id=%u WHERE id=%u AND taken_time IS NULL", dwItemID, dwAwardID)

        CDBManager.instance().ReturnQuery(szQuery, QID_ITEM_AWARD_TAKEN, 0, None)

    def GetMapAward(self):
        return m_map_award

    def GetMapkSetAwardByLogin(self):
        return m_map_kSetAwardByLogin
