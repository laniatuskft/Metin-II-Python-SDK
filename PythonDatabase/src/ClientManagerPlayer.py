def GetPlayerCache(id):
    it = m_map_playerCache.find(id)

    if it is m_map_playerCache.end():
        return None

    pTable = it.second.Get(DefineConstants.false)
    pTable.logoff_interval = GetCurrentTime() - it.second.GetLastUpdateTime()
    return it.second

def PutPlayerCache(pNew):
    c = None

    c = GetPlayerCache(pNew.id)

    if c is None:
        c = CPlayerTableCache()
        m_map_playerCache.insert(TPlayerTableCacheMap.value_type(pNew.id, c))

    c.Put(pNew)

def QUERY_PLAYER_LOAD(peer, dwHandle, packet):
    c = None
    pTab = None

    pLoginData = GetLoginDataByAID(packet.account_id)

    if pLoginData:
        n = 0
        while n < PLAYER_PER_ACCOUNT:
            if pLoginData.GetAccountRef().players[n].dwID != 0:
                DeleteLogoutPlayer(pLoginData.GetAccountRef().players[n].dwID)
            n += 1

# Laniatus Games Studio Inc. |  TODO TASK: The following assignments within expression was not converted by Laniatus Games Studio Inc. T.F |:
#ORIGINAL LINE: if ((c = GetPlayerCache(packet->player_id)))
    if (c = GetPlayerCache(packet.player_id)):
        pkLD = GetLoginDataByAID(packet.account_id)

        if pkLD is None or pkLD.IsPlay():
            sys_log(0, "PLAYER_LOAD_ERROR: LoginData %p IsPlay %d", pkLD,pkLD.IsPlay() if pkLD is not None else 0)
            peer.EncodeHeader(LG_HEADER_DG_PLAYER_LOAD_FAILED, dwHandle, 0)
            return

        pTab = c.Get()

        pkLD.SetPlay(((not DefineConstants.false)))
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        thecore_memcpy(pTab.aiPremiumTimes, pkLD.GetPremiumPtr(), sizeof(pTab.aiPremiumTimes))

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        peer.EncodeHeader(LG_HEADER_DG_PLAYER_LOAD_SUCCESS, dwHandle, sizeof(TPlayerTable))
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        peer.Encode(pTab, sizeof(TPlayerTable))

        if packet.player_id != pkLD.GetLastPlayerID():
            logInfo = TPacketNeedLoginLogInfo()
            logInfo.dwPlayerID = packet.player_id

            pkLD.SetLastPlayerID(packet.player_id)

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
            peer.EncodeHeader(LG_HEADER_DG_NEED_LOGIN_LOG, dwHandle, sizeof(TPacketNeedLoginLogInfo))
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
            peer.Encode(logInfo, sizeof(TPacketNeedLoginLogInfo))

        szQuery = [0, '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0']

        pSet = GetItemCacheSet(pTab.id)

        sys_log(0, "[PLAYER_LOAD] ID %s pid %d gold %lld ", pTab.name, pTab.id, pTab.gold)

        if pSet:
            #Laniatus Games Studio Inc. | Python Metin II Server Note This static local variable declaration (not allowed in Python) has been moved just prior to the method:
            #            static list<TPlayerItem> s_items
            QUERY_PLAYER_LOAD_s_items.resize(pSet.size())

            dwCount = 0
            it = pSet.begin()

            while it is not pSet.end():
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: CItemCache * c = *it++;
                c = *it
                it += 1
                p = c.Get()

                if p.vnum:
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: thecore_memcpy(&s_items[dwCount++], p, sizeof(TPlayerItem));
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
                    thecore_memcpy(QUERY_PLAYER_LOAD_s_items[dwCount], p, sizeof(TPlayerItem))
                    dwCount += 1

            if g_test_server:
                sys_log(0, "ITEM_CACHE: HIT! %s count: %u", pTab.name, dwCount)

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
            peer.EncodeHeader(LG_HEADER_DG_ITEM_LOAD, dwHandle, sizeof(uint) + sizeof(TPlayerItem) * dwCount)
            peer.EncodeDWORD(dwCount)

            if dwCount != 0:
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
                peer.Encode(QUERY_PLAYER_LOAD_s_items[0], sizeof(TPlayerItem) * dwCount)

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
            snprintf(szQuery, sizeof(szQuery), "SELECT dwPID,szName,szState,lValue FROM quest%s WHERE dwPID=%d AND lValue<>0", GetTablePostfix(), pTab.id)

            CDBManager.instance().ReturnQuery(szQuery, QID_QUEST, peer.GetHandle(), ClientHandleInfo(dwHandle,0,packet.account_id))

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
            snprintf(szQuery, sizeof(szQuery), "SELECT dwPID,bType,bApplyOn,lApplyValue,dwFlag,lDuration,lSPCost FROM affect%s WHERE dwPID=%d", GetTablePostfix(), pTab.id)
            CDBManager.instance().ReturnQuery(szQuery, QID_AFFECT, peer.GetHandle(), ClientHandleInfo(dwHandle, pTab.id))
        else:
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
            snprintf(szQuery, sizeof(szQuery), "SELECT " + "id," + "window+0," + "pos," + "count," + "vnum," + "socket0,socket1,socket2," + "attrtype0,attrvalue0," + "attrtype1,attrvalue1," + "attrtype2,attrvalue2," + "attrtype3,attrvalue3," + "attrtype4,attrvalue4," + "attrtype5,attrvalue5," + "attrtype6,attrvalue6 " + "FROM item%s " + "WHERE owner_id=%d AND (window < %d or window = %d) ", GetTablePostfix(), pTab.id, SAFEBOX, DRAGON_SOUL_INVENTORY)

            CDBManager.instance().ReturnQuery(szQuery, QID_ITEM, peer.GetHandle(), ClientHandleInfo(dwHandle, pTab.id))
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
            snprintf(szQuery, sizeof(szQuery), "SELECT dwPID, szName, szState, lValue FROM quest%s WHERE dwPID=%d", GetTablePostfix(), pTab.id)

            CDBManager.instance().ReturnQuery(szQuery, QID_QUEST, peer.GetHandle(), ClientHandleInfo(dwHandle, pTab.id))
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
            snprintf(szQuery, sizeof(szQuery), "SELECT dwPID, bType, bApplyOn, lApplyValue, dwFlag, lDuration, lSPCost FROM affect%s WHERE dwPID=%d", GetTablePostfix(), pTab.id)

            CDBManager.instance().ReturnQuery(szQuery, QID_AFFECT, peer.GetHandle(), ClientHandleInfo(dwHandle, pTab.id))
    else:
        sys_log(0, "[PLAYER_LOAD] Load from PlayerDB pid[%d]", packet.player_id)

        queryStr = str(['\0' for _ in range(DefineConstants.QUERY_MAX_LEN)])

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        snprintf(queryStr, sizeof(queryStr), "SELECT " + "id,name,job,voice,dir,x,y,z,map_index,exit_x,exit_y,exit_map_index,hp,mp,stamina,random_hp,random_sp,playtime," + "gold,level,level_step,st,ht,dx,iq,exp," + "stat_point,LG_SKILL_point,sub_LG_SKILL_point,stat_reset_count,part_base,part_hair," + "part_acce," + "LG_SKILL_level,quickslot,LG_SKILL_group,alignment,horse_level,horse_riding,horse_hp,horse_hp_droptime,horse_stamina," + "UNIX_TIMESTAMP(NOW())-UNIX_TIMESTAMP(last_play),horse_LG_SKILL_point FROM player%s WHERE id=%d", GetTablePostfix(), packet.player_id)

        pkInfo = ClientHandleInfo(dwHandle, packet.player_id)
        pkInfo.account_id = packet.account_id
        CDBManager.instance().ReturnQuery(queryStr, QID_PLAYER, peer.GetHandle(), pkInfo)

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        snprintf(queryStr, sizeof(queryStr), "SELECT " + "id," + "window+0," + "pos," + "count," + "vnum," + "socket0,socket1,socket2," + "attrtype0,attrvalue0," + "attrtype1,attrvalue1," + "attrtype2,attrvalue2," + "attrtype3,attrvalue3," + "attrtype4,attrvalue4," + "attrtype5,attrvalue5," + "attrtype6,attrvalue6 " + "FROM item%s " + "WHERE owner_id=%d AND (window < %d or window = %d) ", GetTablePostfix(), packet.player_id, SAFEBOX, DRAGON_SOUL_INVENTORY)
        CDBManager.instance().ReturnQuery(queryStr, QID_ITEM, peer.GetHandle(), ClientHandleInfo(dwHandle, packet.player_id))

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        snprintf(queryStr, sizeof(queryStr), "SELECT dwPID,szName,szState,lValue FROM quest%s WHERE dwPID=%d", GetTablePostfix(), packet.player_id)
        CDBManager.instance().ReturnQuery(queryStr, QID_QUEST, peer.GetHandle(), ClientHandleInfo(dwHandle, packet.player_id,packet.account_id))

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        snprintf(queryStr, sizeof(queryStr), "SELECT dwPID,bType,bApplyOn,lApplyValue,dwFlag,lDuration,lSPCost FROM affect%s WHERE dwPID=%d", GetTablePostfix(), packet.player_id)
        CDBManager.instance().ReturnQuery(queryStr, QID_AFFECT, peer.GetHandle(), ClientHandleInfo(dwHandle, packet.player_id))


def ItemAward(peer, login):
    login_t = ""
    strlcpy(login_t,login.arg_value,LOGIN_MAX_LEN + 1)
    pSet = ItemAwardManager.instance().GetByLogin(login_t)
    if pSet is None:
        return
    it = pSet.begin()
    while it is not pSet.end():
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: SItemAward * pItemAward = *(it++);
        pItemAward = *(it)
        it += 1
        whyStr = pItemAward.szWhy
        cmdStr = ""
        strcpy(cmdStr,whyStr)
        command = ""
        strcpy(command,GetCommand(cmdStr))
        if not(strcmp(command,"GIFT")):
            giftData = TPacketItemAwardInfromer()
            strcpy(giftData.login, pItemAward.szLogin)
            strcpy(giftData.command, command)
            giftData.vnum = pItemAward.dwVnum
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
            ForwardPacket(LG_HEADER_DG_ITEMAWARD_INFORMER, giftData, sizeof(TPacketItemAwardInfromer))
def GetCommand(str):
    command = ""
    tok = None

    if str.arg_value[0] == '[':
        tok = strtok(str.arg_value,"]")
        strcat(command, tok[1])

    return command

def RESULT_COMPOSITE_PLAYER(peer, pMsg, dwQID):
    qi = pMsg.pvUserData
    info = std::unique_ptr(qi.pvData)

    pSQLResult = pMsg.Get().pSQLResult
    if pSQLResult is None:
        sys_err("null MYSQL_RES QID %u", dwQID)
        return

    if dwQID == QID_PLAYER:
        sys_log(0, "QID_PLAYER %u %u", info.dwHandle, info.player_id)
        RESULT_PLAYER_LOAD(peer, pSQLResult, info.get())


    elif dwQID == QID_ITEM:
        sys_log(0, "QID_ITEM %u", info.dwHandle)
        RESULT_ITEM_LOAD(peer, pSQLResult, info.dwHandle, info.player_id)

    elif dwQID == QID_QUEST:
            sys_log(0, "QID_QUEST %u", info.dwHandle)
            RESULT_QUEST_LOAD(peer, pSQLResult, info.dwHandle, info.player_id)

            temp1 = info.get()
            if temp1 is None:
                break

            pLoginData1 = GetLoginDataByAID(temp1.account_id)

            if pLoginData1.GetAccountRef().login is None:
                break
            if pLoginData1 is None:
                break
            sys_log(0,"info of pLoginData1 before call ItemAwardfunction %d",pLoginData1)
            ItemAward(peer,pLoginData1.GetAccountRef().login)

    elif dwQID == QID_AFFECT:
        sys_log(0, "QID_AFFECT %u", info.dwHandle)
        RESULT_AFFECT_LOAD(peer, pSQLResult, info.dwHandle, info.player_id)



def RESULT_PLAYER_LOAD(peer, pRes, pkInfo):
    tab = TPlayerTable()

    if not CreatePlayerTableFromRes(pRes, tab):
        peer.EncodeHeader(LG_HEADER_DG_PLAYER_LOAD_FAILED, pkInfo.dwHandle, 0)
        return

    pkLD = GetLoginDataByAID(pkInfo.account_id)

    if pkLD is None or pkLD.IsPlay():
        sys_log(0, "PLAYER_LOAD_ERROR: LoginData %p IsPlay %d", pkLD,pkLD.IsPlay() if pkLD is not None else 0)
        peer.EncodeHeader(LG_HEADER_DG_PLAYER_LOAD_FAILED, pkInfo.dwHandle, 0)
        return

    pkLD.SetPlay(((not DefineConstants.false)))
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    thecore_memcpy(tab.aiPremiumTimes, pkLD.GetPremiumPtr(), sizeof(tab.aiPremiumTimes))

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    peer.EncodeHeader(LG_HEADER_DG_PLAYER_LOAD_SUCCESS, pkInfo.dwHandle, sizeof(TPlayerTable))
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    peer.Encode(tab, sizeof(TPlayerTable))

    if tab.id != pkLD.GetLastPlayerID():
        logInfo = TPacketNeedLoginLogInfo()
        logInfo.dwPlayerID = tab.id

        pkLD.SetLastPlayerID(tab.id)

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        peer.EncodeHeader(LG_HEADER_DG_NEED_LOGIN_LOG, pkInfo.dwHandle, sizeof(TPacketNeedLoginLogInfo))
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        peer.Encode(logInfo, sizeof(TPacketNeedLoginLogInfo))

def RESULT_ITEM_LOAD(peer, pRes, dwHandle, dwPID):
    #Laniatus Games Studio Inc. | Python Metin II Server Note This static local variable declaration (not allowed in Python) has been moved just prior to the method:
    #    static list<TPlayerItem> s_items
    CreateItemTableFromRes(pRes, RESULT_ITEM_LOAD_s_items, dwPID)
    dwCount = RESULT_ITEM_LOAD_s_items.size()

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    peer.EncodeHeader(LG_HEADER_DG_ITEM_LOAD, dwHandle, sizeof(uint) + sizeof(TPlayerItem) * dwCount)
    peer.EncodeDWORD(dwCount)

    CreateItemCacheSet(dwPID)

    sys_log(0, "ITEM_LOAD: count %u pid %u", dwCount, dwPID)

    if dwCount != 0:
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        peer.Encode(RESULT_ITEM_LOAD_s_items[0], sizeof(TPlayerItem) * dwCount)

        for i in range(0, dwCount):
            PutItemCache(RESULT_ITEM_LOAD_s_items[i], ((not DefineConstants.false)))

def RESULT_AFFECT_LOAD(peer, pRes, dwHandle, dwRealPID):
    iNumRows = None

# Laniatus Games Studio Inc. |  TODO TASK: The following assignments within expression was not converted by Laniatus Games Studio Inc. T.F |:
#ORIGINAL LINE: if ((iNumRows = mysql_num_rows(pRes)) == 0)
    if (iNumRows = mysql_num_rows(pRes)) == 0:
        count = 0
        sys_log(0, "AFFECT_LOAD: NOT LOADING AFFECT FOR %d - NO RESULTS FOUND!", dwRealPID)
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        peer.EncodeHeader(LG_HEADER_DG_AFFECT_LOAD, dwHandle, sizeof(uint) + sizeof(uint))
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        peer.Encode(dwRealPID, sizeof(uint))
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        peer.Encode(count, sizeof(uint))
        return

    #Laniatus Games Studio Inc. | Python Metin II Server Note This static local variable declaration (not allowed in Python) has been moved just prior to the method:
    #    static list<TPacketAffectElement> s_elements
    RESULT_AFFECT_LOAD_s_elements.resize(iNumRows)

    dwPID = 0

    row = MYSQL_ROW()

    for i in range(0, iNumRows):
        r = RESULT_AFFECT_LOAD_s_elements[i]
        row = mysql_fetch_row(pRes)

        if dwPID == 0:
            str_to_number(dwPID, row[0])

        str_to_number(r.dwType, row[1])
        str_to_number(r.bApplyOn, row[2])
        str_to_number(r.lApplyValue, row[3])
        str_to_number(r.dwFlag, row[4])
        str_to_number(r.lDuration, row[5])
        str_to_number(r.lSPCost, row[6])

    sys_log(0, "AFFECT_LOAD: count %d PID %u", RESULT_AFFECT_LOAD_s_elements.size(), dwPID)

    dwCount = RESULT_AFFECT_LOAD_s_elements.size()

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    peer.EncodeHeader(LG_HEADER_DG_AFFECT_LOAD, dwHandle, sizeof(uint) + sizeof(uint) + sizeof(TPacketAffectElement) * dwCount)
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    peer.Encode(dwPID, sizeof(uint))
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    peer.Encode(dwCount, sizeof(uint))
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    peer.Encode(RESULT_AFFECT_LOAD_s_elements[0], sizeof(TPacketAffectElement) * dwCount)

def RESULT_QUEST_LOAD(peer, pRes, dwHandle, pid):
    iNumRows = None

# Laniatus Games Studio Inc. |  TODO TASK: The following assignments within expression was not converted by Laniatus Games Studio Inc. T.F |:
#ORIGINAL LINE: if ((iNumRows = mysql_num_rows(pRes)) == 0)
    if (iNumRows = mysql_num_rows(pRes)) == 0:
        dwCount = 0
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        peer.EncodeHeader(LG_HEADER_DG_QUEST_LOAD, dwHandle, sizeof(uint))
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        peer.Encode(dwCount, sizeof(uint))
        return

    #Laniatus Games Studio Inc. | Python Metin II Server Note This static local variable declaration (not allowed in Python) has been moved just prior to the method:
    #    static list<TQuestTable> s_table
    RESULT_QUEST_LOAD_s_table.resize(iNumRows)

    row = MYSQL_ROW()

    for i in range(0, iNumRows):
        r = RESULT_QUEST_LOAD_s_table[i]

        row = mysql_fetch_row(pRes)

        str_to_number(r.dwPID, row[0])
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        strlcpy(r.szName, row[1], sizeof(r.szName))
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        strlcpy(r.szState, row[2], sizeof(r.szState))
        str_to_number(r.lValue, row[3])

    sys_log(0, "QUEST_LOAD: count %d PID %u", RESULT_QUEST_LOAD_s_table.size(), RESULT_QUEST_LOAD_s_table[0].dwPID)

    dwCount = RESULT_QUEST_LOAD_s_table.size()

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    peer.EncodeHeader(LG_HEADER_DG_QUEST_LOAD, dwHandle, sizeof(uint) + sizeof(TQuestTable) * dwCount)
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    peer.Encode(dwCount, sizeof(uint))
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    peer.Encode(RESULT_QUEST_LOAD_s_table[0], sizeof(TQuestTable) * dwCount)

def QUERY_PLAYER_SAVE(peer, dwHandle, pkTab):
    if g_test_server:
        sys_log(0, "PLAYER_SAVE: %s", pkTab.name)

    PutPlayerCache(pkTab)

def __QUERY_PLAYER_CREATE(peer, dwHandle, packet):
    queryStr = str(['\0' for _ in range(DefineConstants.QUERY_MAX_LEN)])
    queryLen = None
    player_id = None

    it = s_createTimeByAccountID.find(packet.account_id)

    if it is not s_createTimeByAccountID.end():
        curtime = time(0)

        if curtime - it.second < 30:
            peer.EncodeHeader(LG_HEADER_DG_PLAYER_CREATE_FAILED, dwHandle, 0)
            return

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    queryLen = snprintf(queryStr, sizeof(queryStr), "SELECT pid%u FROM player_index%s WHERE id=%d", packet.account_index + 1, GetTablePostfix(), packet.account_id)

    pMsg0 = std::unique_ptr(CDBManager.instance().DirectQuery(queryStr))

    if pMsg0.Get().uiNumRows != 0:
        if not pMsg0.Get().pSQLResult:
            peer.EncodeHeader(LG_HEADER_DG_PLAYER_CREATE_FAILED, dwHandle, 0)
            return

        row = mysql_fetch_row(pMsg0.Get().pSQLResult)

        dwPID = 0
        str_to_number(dwPID, row[0])
        if row[0] and dwPID > 0:
            peer.EncodeHeader(LG_HEADER_DG_PLAYER_CREATE_ALREADY, dwHandle, 0)
            sys_log(0, "ALREADY EXIST AccountChrIdx %d ID %d", packet.account_index, dwPID)
            return
    else:
        peer.EncodeHeader(LG_HEADER_DG_PLAYER_CREATE_FAILED, dwHandle, 0)
        return


# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    snprintf(queryStr, sizeof(queryStr), "SELECT COUNT(*) as count FROM player%s WHERE name='%s'", GetTablePostfix(), packet.player_table.name)

    pMsg1 = std::unique_ptr(CDBManager.instance().DirectQuery(queryStr))

    if pMsg1.Get().uiNumRows:
        if not pMsg1.Get().pSQLResult:
            peer.EncodeHeader(LG_HEADER_DG_PLAYER_CREATE_FAILED, dwHandle, 0)
            return

        row = mysql_fetch_row(pMsg1.Get().pSQLResult)

        if *row[0] != '0':
            sys_log(0, "ALREADY EXIST name %s, row[0] %s query %s", packet.player_table.name, row[0], queryStr)
            peer.EncodeHeader(LG_HEADER_DG_PLAYER_CREATE_ALREADY, dwHandle, 0)
            return
    else:
        peer.EncodeHeader(LG_HEADER_DG_PLAYER_CREATE_FAILED, dwHandle, 0)
        return

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    queryLen = snprintf(queryStr, sizeof(queryStr), "INSERT INTO player%s " + "(id, " + "account_id, " + "name, " + "level, " + "st, " + "ht, " + "dx, " + "iq, " + "job, " + "voice, " + "dir, " + "x, " + "y, " + "z, " + "hp, " + "mp, " + "random_hp, " + "random_sp, " + "stat_point, " + "stamina, " + "part_base, " + "part_main, " + "part_hair, " + "part_acce, " + "gold, " + "playtime, " + "LG_SKILL_level, " + "quickslot) " + "VALUES" + "(0, " + "%u, " + "'%s', " + "%d, " + "%d, " + "%d, " + "%d, " + "%d, " + "%d, " + "%d, " + "%d, " + "%d, " + "%d, " + "%d, " + "%d, " + "%d, " + "%d, " + "%d, " + "%d, " + "%d, " + "%d, " + "%d, " + "%d, " + "0, " + "%lld, " + "0, ", GetTablePostfix(), packet.account_id, packet.player_table.name, packet.player_table.level, packet.player_table.st, packet.player_table.ht, packet.player_table.dx, packet.player_table.iq, packet.player_table.job, packet.player_table.voice, packet.player_table.dir, packet.player_table.x, packet.player_table.y, packet.player_table.z, packet.player_table.hp, packet.player_table.sp, packet.player_table.sRandomHP, packet.player_table.sRandomSP, packet.player_table.stat_point, packet.player_table.stamina, packet.player_table.part_base, packet.player_table.part_base, packet.player_table.part_base, packet.player_table.gold)

    sys_log(0, "PlayerCreate accountid %d name %s level %d gold %lld, st %d ht %d job %d",packet.account_id, packet.player_table.name, packet.player_table.level, packet.player_table.gold, packet.player_table.st, packet.player_table.ht, packet.player_table.job)

    #Laniatus Games Studio Inc. | Python Metin II Server Note This static local variable declaration (not allowed in Python) has been moved just prior to the method:
    #    static char text[4096 + 1]

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    CDBManager.instance().EscapeString(__QUERY_PLAYER_CREATE_text, packet.player_table.skills, sizeof(packet.player_table.skills))
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    queryLen += snprintf(queryStr[queryLen:], sizeof(queryStr) - queryLen, "'%s', ", __QUERY_PLAYER_CREATE_text)
    if g_test_server:
        sys_log(0, "Create_Player queryLen[%d] TEXT[%s]", queryLen, __QUERY_PLAYER_CREATE_text)

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    CDBManager.instance().EscapeString(__QUERY_PLAYER_CREATE_text, packet.player_table.quickslot, sizeof(packet.player_table.quickslot))
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    queryLen += snprintf(queryStr[queryLen:], sizeof(queryStr) - queryLen, "'%s')", __QUERY_PLAYER_CREATE_text)

    pMsg2 = std::unique_ptr(CDBManager.instance().DirectQuery(queryStr))
    if g_test_server:
        sys_log(0, "Create_Player queryLen[%d] TEXT[%s]", queryLen, __QUERY_PLAYER_CREATE_text)

    if pMsg2.Get().uiAffectedRows <= 0:
        peer.EncodeHeader(LG_HEADER_DG_PLAYER_CREATE_ALREADY, dwHandle, 0)
        sys_log(0, "ALREADY EXIST3 query: %s AffectedRows %lu", queryStr, pMsg2.Get().uiAffectedRows)
        return

    player_id = pMsg2.Get().uiInsertID

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    snprintf(queryStr, sizeof(queryStr), "UPDATE player_index%s SET pid%d=%d WHERE id=%d", GetTablePostfix(), packet.account_index + 1, player_id, packet.account_id)
    pMsg3 = std::unique_ptr(CDBManager.instance().DirectQuery(queryStr))

    if pMsg3.Get().uiAffectedRows <= 0:
        sys_err("QUERY_ERROR: %s", queryStr)

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        snprintf(queryStr, sizeof(queryStr), "DELETE FROM player%s WHERE id=%d", GetTablePostfix(), player_id)
        CDBManager.instance().DirectQuery(queryStr)

        peer.EncodeHeader(LG_HEADER_DG_PLAYER_CREATE_FAILED, dwHandle, 0)
        return

    pack = TPacketDGCreateSuccess()
# Laniatus Games Studio Inc. |  TODO TASK: The memory management function 'memset' has no equivalent in Python:
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    memset(pack, 0, sizeof(pack))

    pack.bAccountCharacterIndex = packet.account_index

    pack.player.dwID = player_id
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    strlcpy(pack.player.szName, packet.player_table.name, sizeof(pack.player.szName))
    pack.player.byJob = packet.player_table.job
    pack.player.byLevel = 1
    pack.player.dwPlayMinutes = 0
    pack.player.byST = packet.player_table.st
    pack.player.byHT = packet.player_table.ht
    pack.player.byDX = packet.player_table.dx
    pack.player.byIQ = packet.player_table.iq
    pack.player.wMainPart = packet.player_table.part_base
    pack.player.x = packet.player_table.x
    pack.player.y = packet.player_table.y

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    peer.EncodeHeader(LG_HEADER_DG_PLAYER_CREATE_SUCCESS, dwHandle, sizeof(TPacketDGCreateSuccess))
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    peer.Encode(pack, sizeof(TPacketDGCreateSuccess))

    sys_log(0, "7 name %s job %d", pack.player.szName, pack.player.byJob)

    s_createTimeByAccountID[packet.account_id] = time(0)

def __QUERY_PLAYER_DELETE(peer, dwHandle, packet):
    if (not packet.login[0]) or (not packet.player_id) or packet.account_index >= PLAYER_PER_ACCOUNT:
        return

    ld = GetLoginDataByLogin(packet.login)
    r = ld.GetAccountRef()

    if strlen(r.social_id) < 7 or strncmp(packet.private_code, r.social_id + strlen(r.social_id) - 7, 7):
        sys_log(0, "PLAYER_DELETE FAILED len(%d)", strlen(r.social_id))
        peer.EncodeHeader(LG_HEADER_DG_PLAYER_DELETE_FAILED, dwHandle, 1)
        peer.EncodeBYTE(packet.account_index)
        return

    if ld is None:
        peer.EncodeHeader(LG_HEADER_DG_PLAYER_DELETE_FAILED, dwHandle, 1)
        peer.EncodeBYTE(packet.account_index)
        return

    szQuery = str(['\0' for _ in range(128)])
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    snprintf(szQuery, sizeof(szQuery), "SELECT p.id, p.level, p.name FROM player_index%s AS i, player%s AS p WHERE pid%u=%u AND pid%u=p.id", GetTablePostfix(), GetTablePostfix(), packet.account_index + 1, packet.player_id, packet.account_index + 1)

    pi = ClientHandleInfo(dwHandle, packet.player_id)
    pi.account_index = packet.account_index

    sys_log(0, "PLAYER_DELETE TRY: %s %d pid%d", packet.login, packet.player_id, packet.account_index + 1)
    CDBManager.instance().ReturnQuery(szQuery, QID_PLAYER_DELETE, peer.GetHandle(), pi)

def __RESULT_PLAYER_DELETE(peer, msg):
    qi = msg.pvUserData
    pi = qi.pvData

    if msg.Get() and msg.Get().uiNumRows:
        row = mysql_fetch_row(msg.Get().pSQLResult)

        dwPID = 0
        str_to_number(dwPID, row[0])

        deletedLevelLimit = 0
        str_to_number(deletedLevelLimit, row[1])

        szName = str(['\0' for _ in range(64)])
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        strlcpy(szName, row[2], sizeof(szName))

        if deletedLevelLimit >= m_iPlayerDeleteLevelLimit:
            sys_log(0, "PLAYER_DELETE FAILED LEVEL %u >= DELETE LIMIT %d", deletedLevelLimit, m_iPlayerDeleteLevelLimit)
            peer.EncodeHeader(LG_HEADER_DG_PLAYER_DELETE_FAILED, pi.dwHandle, 1)
            peer.EncodeBYTE(pi.account_index)
            return

        if deletedLevelLimit < m_iPlayerDeleteLevelLimitLower:
            sys_log(0, "PLAYER_DELETE FAILED LEVEL %u < DELETE LIMIT %d", deletedLevelLimit, m_iPlayerDeleteLevelLimitLower)
            peer.EncodeHeader(LG_HEADER_DG_PLAYER_DELETE_FAILED, pi.dwHandle, 1)
            peer.EncodeBYTE(pi.account_index)
            return

        queryStr = str(['\0' for _ in range(DefineConstants.QUERY_MAX_LEN)])

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        snprintf(queryStr, sizeof(queryStr), "INSERT INTO player%s_deleted SELECT * FROM player%s WHERE id=%d", GetTablePostfix(), GetTablePostfix(), pi.player_id)
        pIns = std::unique_ptr(CDBManager.instance().DirectQuery(queryStr))

        if pIns.Get().uiAffectedRows == 0 or pIns.Get().uiAffectedRows == -1:
            sys_log(0, "PLAYER_DELETE FAILED %u CANNOT INSERT TO player%s_deleted", dwPID, GetTablePostfix())

            peer.EncodeHeader(LG_HEADER_DG_PLAYER_DELETE_FAILED, pi.dwHandle, 1)
            peer.EncodeBYTE(pi.account_index)
            return

        sys_log(0, "PLAYER_DELETE SUCCESS %u", dwPID)

        account_index_string = str(['\0' for _ in range(16)])

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        snprintf(account_index_string, sizeof(account_index_string), "player_id%d", m_iPlayerIDStart + pi.account_index)

        pkPlayerCache = GetPlayerCache(pi.player_id)

        if pkPlayerCache:
            m_map_playerCache.erase(pi.player_id)
            pkPlayerCache = None

        pSet = GetItemCacheSet(pi.player_id)

        if pSet:
            it = pSet.begin()

            while it is not pSet.end():
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: CItemCache * pkItemCache = *it++;
                pkItemCache = *it
                it += 1
                DeleteItemCache(pkItemCache.Get().id)

            pSet.clear()
            pSet = None

            m_map_pkItemCacheSetPtr.erase(pi.player_id)

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        snprintf(queryStr, sizeof(queryStr), "UPDATE player_index%s SET pid%u=0 WHERE pid%u=%d", GetTablePostfix(), pi.account_index + 1, pi.account_index + 1, pi.player_id)

        pMsg = std::unique_ptr(CDBManager.instance().DirectQuery(queryStr))

        if pMsg.Get().uiAffectedRows == 0 or pMsg.Get().uiAffectedRows == -1:
            sys_log(0, "PLAYER_DELETE FAIL WHEN UPDATE account table")
            peer.EncodeHeader(LG_HEADER_DG_PLAYER_DELETE_FAILED, pi.dwHandle, 1)
            peer.EncodeBYTE(pi.account_index)
            return

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        snprintf(queryStr, sizeof(queryStr), "DELETE FROM player%s WHERE id=%d", GetTablePostfix(), pi.player_id)
        CDBManager.instance().DirectQuery(queryStr) = None

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        snprintf(queryStr, sizeof(queryStr), "DELETE FROM item%s WHERE owner_id=%d AND (window < %d or window = %d)", GetTablePostfix(), pi.player_id, SAFEBOX, DRAGON_SOUL_INVENTORY)
        CDBManager.instance().DirectQuery(queryStr) = None

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        snprintf(queryStr, sizeof(queryStr), "DELETE FROM quest%s WHERE dwPID=%d", GetTablePostfix(), pi.player_id)
        CDBManager.instance().AsyncQuery(queryStr)

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        snprintf(queryStr, sizeof(queryStr), "DELETE FROM affect%s WHERE dwPID=%d", GetTablePostfix(), pi.player_id)
        CDBManager.instance().AsyncQuery(queryStr)

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        snprintf(queryStr, sizeof(queryStr), "DELETE FROM guild_member%s WHERE pid=%d", GetTablePostfix(), pi.player_id)
        CDBManager.instance().AsyncQuery(queryStr)

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        snprintf(queryStr, sizeof(queryStr), "DELETE FROM myshop_pricelist%s WHERE owner_id=%d", GetTablePostfix(), pi.player_id)
        CDBManager.instance().AsyncQuery(queryStr)

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        snprintf(queryStr, sizeof(queryStr), "DELETE FROM messenger_list%s WHERE account='%s' OR companion='%s'", GetTablePostfix(), szName, szName)
        CDBManager.instance().AsyncQuery(queryStr)

        peer.EncodeHeader(LG_HEADER_DG_PLAYER_DELETE_SUCCESS, pi.dwHandle, 1)
        peer.EncodeBYTE(pi.account_index)
    else:
        sys_log(0, "PLAYER_DELETE FAIL NO ROW")
        peer.EncodeHeader(LG_HEADER_DG_PLAYER_DELETE_FAILED, pi.dwHandle, 1)
        peer.EncodeBYTE(pi.account_index)

def QUERY_ADD_AFFECT(peer, p):
    queryStr = str(['\0' for _ in range(DefineConstants.QUERY_MAX_LEN)])

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    snprintf(queryStr, sizeof(queryStr), "REPLACE INTO affect%s (dwPID, bType, bApplyOn, lApplyValue, dwFlag, lDuration, lSPCost) " + "VALUES(%u, %u, %u, %ld, %u, %ld, %ld)", GetTablePostfix(), p.dwPID, p.elem.dwType, p.elem.bApplyOn, p.elem.lApplyValue, p.elem.dwFlag, p.elem.lDuration, p.elem.lSPCost)

    CDBManager.instance().AsyncQuery(queryStr)

def QUERY_REMOVE_AFFECT(peer, p):
    queryStr = str(['\0' for _ in range(DefineConstants.QUERY_MAX_LEN)])

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    snprintf(queryStr, sizeof(queryStr), "DELETE FROM affect%s WHERE dwPID=%u AND bType=%u AND bApplyOn=%u", GetTablePostfix(), p.dwPID, p.dwType, p.bApplyOn)

    CDBManager.instance().AsyncQuery(queryStr)


def QUERY_HIGHSCORE_REGISTER(peer, data):
    szQuery = str(['\0' for _ in range(128)])
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    snprintf(szQuery, sizeof(szQuery), "SELECT value FROM highscore%s WHERE board='%s' AND pid = %u", GetTablePostfix(), data.szBoard, data.dwPID)

    sys_log(0, "LG_HEADER_GD_HIGHSCORE_REGISTER: PID %u", data.dwPID)

    pi = ClientHandleInfo(0)
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    strlcpy(pi.login, data.szBoard, sizeof(pi.login))
    pi.account_id = data.lValue
    pi.player_id = data.dwPID
    pi.account_index = (data.cDir > 0)

    CDBManager.instance().ReturnQuery(szQuery, QID_HIGHSCORE_REGISTER, peer.GetHandle(), pi)

def RESULT_HIGHSCORE_REGISTER(pkPeer, msg):
    qi = msg.pvUserData
    pi = qi.pvData

    szBoard = str(['\0' for _ in range(21)])
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    strlcpy(szBoard, pi.login, sizeof(szBoard))
    value = int(pi.account_id)

    res = msg.Get()

    if res.uiNumRows == 0:
        buf = str(['\0' for _ in range(256)])
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        snprintf(buf, sizeof(buf), "INSERT INTO highscore%s VALUES('%s', %u, %d)", GetTablePostfix(), szBoard, pi.player_id, value)
        CDBManager.instance().AsyncQuery(buf)
    else:
        if not res.pSQLResult:
            pi = None
            return

        row = mysql_fetch_row(res.pSQLResult)
        if row is not None and row[0]:
            current_value = 0
            str_to_number(current_value, row[0])
            if pi.account_index and current_value >= value or (not pi.account_index) and current_value <= value:
                value = current_value
            else:
                buf = str(['\0' for _ in range(256)])
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
                snprintf(buf, sizeof(buf), "REPLACE INTO highscore%s VALUES('%s', %u, %d)", GetTablePostfix(), szBoard, pi.player_id, value)
                CDBManager.instance().AsyncQuery(buf)
        else:
            buf = str(['\0' for _ in range(256)])
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
            snprintf(buf, sizeof(buf), "INSERT INTO highscore%s VALUES('%s', %u, %d)", GetTablePostfix(), szBoard, pi.player_id, value)
            CDBManager.instance().AsyncQuery(buf)
    pi = None

def InsertLogoutPlayer(pid):
    it = m_map_logout.find(pid)

    if it is not m_map_logout.end():
        if g_log:
            sys_log(0, "LOGOUT: Update player time pid(%d)", pid)

        it.second.time = time(0)
        return

    pLogout = TLogoutPlayer()
    pLogout.pid = pid
    pLogout.time = time(0)
    m_map_logout.insert((pid, pLogout))

    if g_log:
        sys_log(0, "LOGOUT: Insert player pid(%d)", pid)

def DeleteLogoutPlayer(pid):
    it = m_map_logout.find(pid)

    if it is not m_map_logout.end():
        it.second = None
        m_map_logout.erase(it)

def UpdateLogoutPlayer():
    now = time(0)

    it = m_map_logout.begin()

    while it is not m_map_logout.end():
        pLogout = it.second

        if now - g_iLogoutSeconds > pLogout.time:
            FlushItemCacheSet(pLogout.pid)
            FlushPlayerCacheSet(pLogout.pid)

            pLogout = None
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: m_map_logout.erase(it++);
            m_map_logout.erase(it)
            it += 1
        else:
            it += 1

def FlushPlayerCacheSet(pid):
    it = m_map_playerCache.find(pid)

    if it is not m_map_playerCache.end():
        c = it.second
        m_map_playerCache.erase(it)

        c.Flush()
        c = None

