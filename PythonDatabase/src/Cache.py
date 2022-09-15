#Laniatus Games Studio Inc. | Python Metin II Server Warnings Statement interrupted by a preprocessor statement:
#The original statement from the file sal.h starts with:
#    __inner_fallthrough_dec
#Preprocessor-interrupted statements cannot be handled by this converter.
#The remainder of the header file sal.h is ignored.


class cache:
    def __init__(self):
        self.m_bNeedQuery = DefineConstants.false
        self.m_expireTime = 600
        self.m_lastUpdateTime = 0
        m_lastFlushTime = time(0)

# Laniatus Games Studio Inc. |  TODO TASK: The memory management function 'memset' has no equivalent in Python:
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        memset(m_data, 0, sizeof(m_data))

    def Get(self, bUpdateTime = (!DefineConstants.false)):
        if bUpdateTime:
            m_lastUpdateTime = time(0)

        return m_data

    def Put(self, pNew, bSkipQuery = DefineConstants.false):
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        thecore_memcpy(m_data, pNew, sizeof(T))
        m_lastUpdateTime = time(0)

        if not bSkipQuery:
            m_bNeedQuery = ((not DefineConstants.false))

    def CheckFlushTimeout(self):
        if m_bNeedQuery and time(0) - m_lastFlushTime > m_expireTime:
            return ((not DefineConstants.false))

        return DefineConstants.false

    def CheckTimeout(self):
        if time(0) - m_lastUpdateTime > m_expireTime:
            return ((not DefineConstants.false))

        return DefineConstants.false

    def Flush(self):
        if not m_bNeedQuery:
            return

        OnFlush()
        m_bNeedQuery = DefineConstants.false
        m_lastFlushTime = time(0)

    def OnFlush(self):
        pass




class CItemCache(cache):
    def __init__(self):
        m_expireTime = MIN(1800, g_iItemCacheFlushSeconds)

    def close(self):
        pass

    def Delete(self):
        if m_data.vnum == 0:
            return

        if g_test_server:
            sys_log(0, "ItemCache::Delete : DELETE %u", m_data.id)

        m_data.vnum = 0
        m_bNeedQuery = ((not DefineConstants.false))
        m_lastUpdateTime = time(0)
        OnFlush()

    def OnFlush(self):
        if m_data.vnum == 0:
            szQuery = str(['\0' for _ in range(DefineConstants.QUERY_MAX_LEN)])
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
            snprintf(szQuery, sizeof(szQuery), "DELETE FROM item%s WHERE id=%u", GetTablePostfix(), m_data.id)
            CDBManager.instance().ReturnQuery(szQuery, QID_ITEM_DESTROY, 0, None)

            if g_test_server:
                sys_log(0, "ItemCache::Flush : DELETE %u %s", m_data.id, szQuery)
        else:
            alSockets = [0 for _ in range(LG_ITEM_SOCKET_MAX_NUM)]
            aAttr = [TPlayerItemAttribute() for _ in range(ITEM_ATTRIBUTE_MAX_NUM)]
            isSocket = DefineConstants.false
            isAttr = DefineConstants.false

# Laniatus Games Studio Inc. |  TODO TASK: The memory management function 'memset' has no equivalent in Python:
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
            memset(alSockets, 0, sizeof(int) * LG_ITEM_SOCKET_MAX_NUM)
# Laniatus Games Studio Inc. |  TODO TASK: The memory management function 'memset' has no equivalent in Python:
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
            memset(aAttr, 0, sizeof(TPlayerItemAttribute) * ITEM_ATTRIBUTE_MAX_NUM)

            p = m_data

# Laniatus Games Studio Inc. |  TODO TASK: The memory management function 'memcmp' has no equivalent in Python:
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
            if memcmp(alSockets, p.alSockets, sizeof(int) * LG_ITEM_SOCKET_MAX_NUM):
                isSocket = ((not DefineConstants.false))

# Laniatus Games Studio Inc. |  TODO TASK: The memory management function 'memcmp' has no equivalent in Python:
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
            if memcmp(aAttr, p.aAttr, sizeof(TPlayerItemAttribute) * ITEM_ATTRIBUTE_MAX_NUM):
                isAttr = ((not DefineConstants.false))

            szColumns = str(['\0' for _ in range(DefineConstants.QUERY_MAX_LEN)])
            szValues = str(['\0' for _ in range(DefineConstants.QUERY_MAX_LEN)])
            szUpdate = str(['\0' for _ in range(DefineConstants.QUERY_MAX_LEN)])

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
            iLen = snprintf(szColumns, sizeof(szColumns), "id, owner_id, window, pos, count, vnum")

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
            iValueLen = snprintf(szValues, sizeof(szValues), "%u, %u, %d, %d, %u, %u", p.id, p.owner, p.window, p.pos, p.count, p.vnum)

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
            iUpdateLen = snprintf(szUpdate, sizeof(szUpdate), "owner_id=%u, window=%d, pos=%d, count=%u, vnum=%u", p.owner, p.window, p.pos, p.count, p.vnum)

            if isSocket:
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
                iLen += snprintf(szColumns[iLen:], sizeof(szColumns) - iLen, ", socket0, socket1, socket2")
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
                iValueLen += snprintf(szValues[iValueLen:], sizeof(szValues) - iValueLen, ", %lu, %lu, %lu", p.alSockets[0], p.alSockets[1], p.alSockets[2])
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
                iUpdateLen += snprintf(szUpdate[iUpdateLen:], sizeof(szUpdate) - iUpdateLen, ", socket0=%lu, socket1=%lu, socket2=%lu", p.alSockets[0], p.alSockets[1], p.alSockets[2])

            if isAttr:
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
                iLen += snprintf(szColumns[iLen:], sizeof(szColumns) - iLen, ", attrtype0, attrvalue0, attrtype1, attrvalue1, attrtype2, attrvalue2, attrtype3, attrvalue3" + ", attrtype4, attrvalue4, attrtype5, attrvalue5, attrtype6, attrvalue6")

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
                iValueLen += snprintf(szValues[iValueLen:], sizeof(szValues) - iValueLen, ", %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d", p.aAttr[0].bType, p.aAttr[0].sValue, p.aAttr[1].bType, p.aAttr[1].sValue, p.aAttr[2].bType, p.aAttr[2].sValue, p.aAttr[3].bType, p.aAttr[3].sValue, p.aAttr[4].bType, p.aAttr[4].sValue, p.aAttr[5].bType, p.aAttr[5].sValue, p.aAttr[6].bType, p.aAttr[6].sValue)

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
                iUpdateLen += snprintf(szUpdate[iUpdateLen:], sizeof(szUpdate) - iUpdateLen, ", attrtype0=%d, attrvalue0=%d" + ", attrtype1=%d, attrvalue1=%d" + ", attrtype2=%d, attrvalue2=%d" + ", attrtype3=%d, attrvalue3=%d" + ", attrtype4=%d, attrvalue4=%d" + ", attrtype5=%d, attrvalue5=%d" + ", attrtype6=%d, attrvalue6=%d", p.aAttr[0].bType, p.aAttr[0].sValue, p.aAttr[1].bType, p.aAttr[1].sValue, p.aAttr[2].bType, p.aAttr[2].sValue, p.aAttr[3].bType, p.aAttr[3].sValue, p.aAttr[4].bType, p.aAttr[4].sValue, p.aAttr[5].bType, p.aAttr[5].sValue, p.aAttr[6].bType, p.aAttr[6].sValue)

            szItemQuery = str(['\0' for _ in range(DefineConstants.QUERY_MAX_LEN + DefineConstants.QUERY_MAX_LEN)])
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
            snprintf(szItemQuery, sizeof(szItemQuery), "REPLACE INTO item%s (%s) VALUES(%s)", GetTablePostfix(), szColumns, szValues)

            if g_test_server:
                sys_log(0, "ItemCache::Flush :REPLACE  (%s)", szItemQuery)

            CDBManager.instance().ReturnQuery(szItemQuery, QID_ITEM_SAVE, 0, None)
            g_item_count += 1

        m_bNeedQuery = DefineConstants.false

class CPlayerTableCache(cache):
    def __init__(self):
        m_expireTime = MIN(1800, g_iPlayerCacheFlushSeconds)

    def close(self):
        pass

    def OnFlush(self):
        if g_test_server:
            sys_log(0, "PlayerTableCache::Flush : %s", m_data.name)

        szQuery = str(['\0' for _ in range(DefineConstants.QUERY_MAX_LEN)])
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        CreatePlayerSaveQuery(szQuery, sizeof(szQuery), m_data)
        CDBManager.instance().ReturnQuery(szQuery, QID_PLAYER_SAVE, 0, None)

    def GetLastUpdateTime(self):
        return m_lastUpdateTime

class CItemPriceListTableCache(cache):
    def __init__(self):
        m_expireTime = MIN(s_nMinFlushSec, g_iItemPriceListTableCacheFlushSeconds)

    def UpdateList(self, pUpdateList):
        if pUpdateList.wCount > SHOP_PRICELIST_MAX_NUM:
            sys_err("Count overflow!")
            return

        m_data.wCount = pUpdateList.wCount
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        thecore_memcpy(m_data.aPriceInfo, pUpdateList.aPriceInfo, sizeof(TItemPriceInfo) * pUpdateList.wCount)
        m_bNeedQuery = ((not DefineConstants.false))
        sys_log(0, "ItemPriceListTableCache::UpdateList : OwnerID[%u] Update [%u] Items, Total [%u] Items", m_data.dwOwnerID, pUpdateList.wCount, m_data.wCount)

    def OnFlush(self):
        szQuery = str(['\0' for _ in range(DefineConstants.QUERY_MAX_LEN)])
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        snprintf(szQuery, sizeof(szQuery), "DELETE FROM myshop_pricelist%s WHERE owner_id = %u", GetTablePostfix(), m_data.dwOwnerID)
        CDBManager.instance().ReturnQuery(szQuery, QID_ITEMPRICE_DESTROY, 0, None)

        idx = 0
        while idx < m_data.wCount:
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
            snprintf(szQuery, sizeof(szQuery), "INSERT INTO myshop_pricelist%s(owner_id, item_vnum, price) VALUES(%u, %u, %lld)", GetTablePostfix(), m_data.dwOwnerID, m_data.aPriceInfo[idx].dwVnum, m_data.aPriceInfo[idx].lldPrice)
            CDBManager.instance().ReturnQuery(szQuery, QID_ITEMPRICE_SAVE, 0, None)
            idx += 1

        sys_log(0, "ItemPriceListTableCache::Flush : OwnerID[%u] Update [%u]Items", m_data.dwOwnerID, m_data.wCount)

        m_bNeedQuery = DefineConstants.false

    s_nMinFlushSec = 1800