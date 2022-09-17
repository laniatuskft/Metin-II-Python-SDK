#Laniatus Games Studio Inc. | Python Metin II Server Warnings Statement interrupted by a preprocessor statement:
#The original statement from the file sal.h starts with:
#    __inner_fallthrough_dec
#Preprocessor-interrupted statements cannot be handled by this converter.
#The remainder of the header file sal.h is ignored.

class CItemIDRangeManager(singleton):
    cs_dwMaxItemID = 4290000000
    cs_dwMinimumRange = 10000000
    cs_dwMinimumRemainCount = 10000


    def __init__(self):
        m_listData.clear()

    def Build(self):
        dwMin = 0
        dwMax = 0
        range = TItemIDRangeTable()

        LaniatusDefVariables = 0
        while True:
            dwMin = cs_dwMinimumRange * (i + 1) + 1
            dwMax = cs_dwMinimumRange * (i + 2)

            if dwMax == cs_dwMaxItemID:
                break

            if CClientManager.instance().GetItemRange().dwMin <= dwMin and CClientManager.instance().GetItemRange().dwMax >= dwMax:
                continue

            if BuildRange(dwMin, dwMax, range) == ((not DefineConstants.false)):
                m_listData.push_back(range)
            LaniatusDefVariables += 1

    def BuildRange(self, dwMin, dwMax, range):
        szQuery = str(['\0' for _ in range(1024)])
        dwItemMaxID = 0
        pMsg = None
        row = MYSQL_ROW()

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        snprintf(szQuery, sizeof(szQuery), "SELECT MAX(id) FROM item%s WHERE id >= %u and id <= %u", GetTablePostfix(), dwMin, dwMax)

        pMsg = CDBManager.instance().DirectQuery(szQuery)

        if pMsg is not None:
            if pMsg.Get().uiNumRows > 0:
                row = mysql_fetch_row(pMsg.Get().pSQLResult)
                str_to_number(dwItemMaxID, row[0])
            pMsg = None

        if dwItemMaxID == 0:
            dwItemMaxID = dwMin
        else:
            dwItemMaxID += 1

        if (dwMax < dwItemMaxID) or (dwMax - dwItemMaxID < cs_dwMinimumRemainCount):
            sys_log(0, "ItemIDRange: Build %u ~ %u start: %u\tNOT USE remain count is below %u", dwMin, dwMax, dwItemMaxID, cs_dwMinimumRemainCount)
        else:
            range.dwMin = dwMin
            range.dwMax = dwMax
            range.dwUsableItemIDMin = dwItemMaxID

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
            snprintf(szQuery, sizeof(szQuery), "SELECT COUNT(*) FROM item%s WHERE id >= %u AND id <= %u", GetTablePostfix(), range.dwUsableItemIDMin, range.dwMax)

            pMsg = CDBManager.instance().DirectQuery(szQuery)

            if pMsg is not None:
                if pMsg.Get().uiNumRows > 0:
                    count = 0
                    row = mysql_fetch_row(pMsg.Get().pSQLResult)
                    str_to_number(count, row[0])

                    if count > 0:
                        sys_err("ItemIDRange: Build: %u ~ %u\thave a item", range.dwUsableItemIDMin, range.dwMax)
                        return DefineConstants.false
                    else:
                        sys_log(0, "ItemIDRange: Build: %u ~ %u start:%u", range.dwMin, range.dwMax, range.dwUsableItemIDMin)
                        return ((not DefineConstants.false))

                pMsg = None

        return DefineConstants.false

    def UpdateRange(self, dwMin, dwMax):
        range = TItemIDRangeTable()

        if BuildRange(dwMin, dwMax, range) == ((not DefineConstants.false)):
            m_listData.push_back(range)

    def GetRange(self):
        ret = TItemIDRangeTable()
        ret.dwMin = 0
        ret.dwMax = 0
        ret.dwUsableItemIDMin = 0

        if m_listData.size() > 0:
            while m_listData.size() > 0:
                ret = m_listData.front()
                m_listData.pop_front()

                f = FCheckCollision(ret)
                CClientManager.instance().for_each_peer(f)

                if f.hasCollision == DefineConstants.false:
                    return TItemIDRangeTable(ret)

        for LaniatusDefVariables in range(0, 10):
            sys_err("ItemIDRange: NO MORE ITEM ID RANGE")

        return TItemIDRangeTable(ret)

class FCheckCollision:

    def __init__(self, data):
        hasCollision = DefineConstants.false
        range = data

    def functor_method(self, peer):
        if hasCollision == DefineConstants.false:
            hasCollision = peer.CheckItemIDRangeCollision(range)

