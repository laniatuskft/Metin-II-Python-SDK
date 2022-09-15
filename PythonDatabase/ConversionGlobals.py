class Globals:
#Laniatus Games Studio Inc. | Python Metin II Server Note 'extern' variable declarations are not required in Python:
    #extern CPacketInfo g_item_info
#Laniatus Games Studio Inc. | Python Metin II Server Note 'extern' variable declarations are not required in Python:
    #extern int g_iPlayerCacheFlushSeconds
#Laniatus Games Studio Inc. | Python Metin II Server Note 'extern' variable declarations are not required in Python:
    #extern int g_iItemCacheFlushSeconds
#Laniatus Games Studio Inc. | Python Metin II Server Note 'extern' variable declarations are not required in Python:
    #extern int g_test_server
#Laniatus Games Studio Inc. | Python Metin II Server Note 'extern' variable declarations are not required in Python:
    #extern int g_iItemPriceListTableCacheFlushSeconds
#Laniatus Games Studio Inc. | Python Metin II Server Note 'extern' variable declarations are not required in Python:
    #extern int g_item_count



    @staticmethod
    def __GetWarType(n):
        if n == 0:
            return "�п�"
        if (n == 0) or (n == 1):
            return "����"
        if (n == 0) or (n == 1) or (n == 2):
            return "��ȣ"

        if True:
            return "���� ��ȣ"
    #Laniatus Games Studio Inc. | Python Metin II Server Warnings Statement interrupted by a preprocessor statement:
    #The original statement from the file sal.h starts with:
    #    __inner_fallthrough_dec
    #Preprocessor-interrupted statements cannot be handled by this converter.
    #The remainder of the header file sal.h is ignored.



#Laniatus Games Studio Inc. | Python Metin II Server Note 'extern' variable declarations are not required in Python:
    #extern str g_stLocale
//Laniatus Games Studio Inc. T.F | TODO TASK: The implementation of the following method could not be found:
    //CreatePlayerTableFromRes(res, pkTab)
#Laniatus Games Studio Inc. | Python Metin II Server Note 'extern' variable declarations are not required in Python:
    #extern int g_test_server
#Laniatus Games Studio Inc. | Python Metin II Server Note 'extern' variable declarations are not required in Python:
    #extern int g_log

    @staticmethod
    def CreateAccountTableFromRes(res):
        input_pwd = str(['\0' for _ in range(PASSWD_MAX_LEN + 1)])
        row = None
        col = None

        row = mysql_fetch_row(res)
        col = 0

        pkTab = TAccountTable()
# Laniatus Games Studio Inc. |  TODO TASK: The memory management function 'memset' has no equivalent in Python:
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        memset(pkTab, 0, sizeof(TAccountTable))

#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: strlcpy(input_pwd, row[col++], sizeof(input_pwd));
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        strlcpy(input_pwd, row[col], sizeof(input_pwd))
        col += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(pkTab->id, row[col++]);
        str_to_number(pkTab.id, row[col])
        col += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: strlcpy(pkTab->login, row[col++], sizeof(pkTab->login));
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        strlcpy(pkTab.login, row[col], sizeof(pkTab.login))
        col += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: strlcpy(pkTab->passwd, row[col++], sizeof(pkTab->passwd));
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        strlcpy(pkTab.passwd, row[col], sizeof(pkTab.passwd))
        col += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: strlcpy(pkTab->social_id, row[col++], sizeof(pkTab->social_id));
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        strlcpy(pkTab.social_id, row[col], sizeof(pkTab.social_id))
        col += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(pkTab->bEmpire, row[col++]);
        str_to_number(pkTab.bEmpire, row[col])
        col += 1
    # Laniatus Games Studio Inc. |  TODO TASK: There is no preprocessor in Python:
    ##if __MULTI_LANGUAGE_SYSTEM__
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(pkTab->bLanguage, row[col++]);
        str_to_number(pkTab.bLanguage, row[col])
        col += 1
    ##endif

        j = 0
        while j < PLAYER_PER_ACCOUNT:
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(pkTab->players[j].dwID, row[col++]);
            str_to_number(pkTab.players[j].dwID, row[col])
            col += 1
            j += 1

#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: strlcpy(pkTab->status, row[col++], sizeof(pkTab->status));
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        strlcpy(pkTab.status, row[col], sizeof(pkTab.status))
        col += 1

        if strcmp(pkTab.passwd, input_pwd):
            pkTab = None
            return None

        return pkTab

    @staticmethod
    def CreateAccountPlayerDataFromRes(pRes, pkTab):
        if pRes is None:
            return

        i = 0
        while i < mysql_num_rows(pRes):
            row = mysql_fetch_row(pRes)
            col = 0

            player_id = 0
# Laniatus Games Studio Inc. |  TODO TASK: The following assignments within expression was not converted by Laniatus Games Studio Inc. T.F |:
#ORIGINAL LINE: !row[col++] ? 0 : str_to_number(player_id, row[col - 1]);
            0 if (not row[col++]) else str_to_number(player_id, row[col - 1])

            if player_id == 0:
                continue

            j = None

            j = 0
            while j < PLAYER_PER_ACCOUNT:
                if pkTab.players[j].dwID == player_id:
                    pc = CClientManager.instance().GetPlayerCache(player_id)
                    pt = pc.Get(DefineConstants.false) if pc is not None else None

                    if pt:
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
                        strlcpy(pkTab.players[j].szName, pt.name, sizeof(pkTab.players[j].szName))

                        pkTab.players[j].byJob = pt.job
                        pkTab.players[j].byLevel = pt.level
                        pkTab.players[j].dwPlayMinutes = pt.playtime
                        pkTab.players[j].byST = pt.st
                        pkTab.players[j].byHT = pt.ht
                        pkTab.players[j].byDX = pt.dx
                        pkTab.players[j].byIQ = pt.iq
                        pkTab.players[j].wMainPart = pt.parts[PART_MAIN]
                        pkTab.players[j].wHairPart = pt.parts[PART_HAIR]
                        pkTab.players[j].dwAccePart = pt.parts[PART_ACCE]
                        pkTab.players[j].x = pt.x
                        pkTab.players[j].y = pt.y
                        pkTab.players[j].LG_SKILL_group = pt.LG_SKILL_group
                        pkTab.players[j].bChangeName = 0
                    else:
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: if (!row[col++])
                        if not row[col]:
                            col += 1
                            *pkTab.players[j].szName = '\0'
                        else:
                            col += 1
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
                            strlcpy(pkTab.players[j].szName, row[col - 1], sizeof(pkTab.players[j].szName))

                        pkTab.players[j].byJob = 0
                        pkTab.players[j].byLevel = 0
                        pkTab.players[j].dwPlayMinutes = 0
                        pkTab.players[j].byST = 0
                        pkTab.players[j].byHT = 0
                        pkTab.players[j].byDX = 0
                        pkTab.players[j].byIQ = 0
                        pkTab.players[j].wMainPart = 0
                        pkTab.players[j].wHairPart = 0
                        pkTab.players[j].dwAccePart = 0
                        pkTab.players[j].x = 0
                        pkTab.players[j].y = 0
                        pkTab.players[j].LG_SKILL_group = 0
                        pkTab.players[j].bChangeName = 0

#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(pkTab->players[j].byJob, row[col++]);
                        str_to_number(pkTab.players[j].byJob, row[col])
                        col += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(pkTab->players[j].byLevel, row[col++]);
                        str_to_number(pkTab.players[j].byLevel, row[col])
                        col += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(pkTab->players[j].dwPlayMinutes, row[col++]);
                        str_to_number(pkTab.players[j].dwPlayMinutes, row[col])
                        col += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(pkTab->players[j].byST, row[col++]);
                        str_to_number(pkTab.players[j].byST, row[col])
                        col += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(pkTab->players[j].byHT, row[col++]);
                        str_to_number(pkTab.players[j].byHT, row[col])
                        col += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(pkTab->players[j].byDX, row[col++]);
                        str_to_number(pkTab.players[j].byDX, row[col])
                        col += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(pkTab->players[j].byIQ, row[col++]);
                        str_to_number(pkTab.players[j].byIQ, row[col])
                        col += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(pkTab->players[j].wMainPart, row[col++]);
                        str_to_number(pkTab.players[j].wMainPart, row[col])
                        col += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(pkTab->players[j].wHairPart, row[col++]);
                        str_to_number(pkTab.players[j].wHairPart, row[col])
                        col += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(pkTab->players[j].dwAccePart, row[col++]);
                        str_to_number(pkTab.players[j].dwAccePart, row[col])
                        col += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(pkTab->players[j].x, row[col++]);
                        str_to_number(pkTab.players[j].x, row[col])
                        col += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(pkTab->players[j].y, row[col++]);
                        str_to_number(pkTab.players[j].y, row[col])
                        col += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(pkTab->players[j].LG_SKILL_group, row[col++]);
                        str_to_number(pkTab.players[j].LG_SKILL_group, row[col])
                        col += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(pkTab->players[j].bChangeName, row[col++]);
                        str_to_number(pkTab.players[j].bChangeName, row[col])
                        col += 1

                    sys_log(0, "%s %lu %lu hair %u", pkTab.players[j].szName, pkTab.players[j].x, pkTab.players[j].y, pkTab.players[j].wHairPart)
                    break
                j += 1
            i += 1
    #Laniatus Games Studio Inc. | Python Metin II Server Warnings Statement interrupted by a preprocessor statement:
    #The original statement from the file sal.h starts with:
    #    __inner_fallthrough_dec
    #Preprocessor-interrupted statements cannot be handled by this converter.
    #The remainder of the header file sal.h is ignored.

#Laniatus Games Studio Inc. | Python Metin II Server Note 'extern' variable declarations are not required in Python:
    #extern str g_stLocale
#Laniatus Games Studio Inc. | Python Metin II Server Note 'extern' variable declarations are not required in Python:
    #extern int g_test_server
#Laniatus Games Studio Inc. | Python Metin II Server Note 'extern' variable declarations are not required in Python:
    #extern int g_log

    @staticmethod
    def CreateItemTableFromRes(res, pVec, dwPID):
        if res is None:
            pVec.clear()
            return ((not DefineConstants.false))

        rows = None

# Laniatus Games Studio Inc. |  TODO TASK: The following assignments within expression was not converted by Laniatus Games Studio Inc. T.F |:
#ORIGINAL LINE: if ((rows = mysql_num_rows(res)) <= 0)
        if (rows = mysql_num_rows(res)) <= 0:
            pVec.clear()
            return ((not DefineConstants.false))

        pVec.resize(rows)

        for i in range(0, rows):
            row = mysql_fetch_row(res)
            item = pVec[i]

            cur = 0

#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(item.id, row[cur++]);
            str_to_number(item.id, row[cur])
            cur += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(item.window, row[cur++]);
            str_to_number(item.window, row[cur])
            cur += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(item.pos, row[cur++]);
            str_to_number(item.pos, row[cur])
            cur += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(item.count, row[cur++]);
            str_to_number(item.count, row[cur])
            cur += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(item.vnum, row[cur++]);
            str_to_number(item.vnum, row[cur])
            cur += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(item.alSockets[0], row[cur++]);
            str_to_number(item.alSockets[0], row[cur])
            cur += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(item.alSockets[1], row[cur++]);
            str_to_number(item.alSockets[1], row[cur])
            cur += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(item.alSockets[2], row[cur++]);
            str_to_number(item.alSockets[2], row[cur])
            cur += 1

            j = 0
            while j < ITEM_ATTRIBUTE_MAX_NUM:
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(item.aAttr[j].bType, row[cur++]);
                str_to_number(item.aAttr[j].bType, row[cur])
                cur += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(item.aAttr[j].sValue, row[cur++]);
                str_to_number(item.aAttr[j].sValue, row[cur])
                cur += 1
                j += 1

            item.owner = dwPID

        return ((not DefineConstants.false))

    #Laniatus Games Studio Inc. | Python Metin II Server Note This was formerly a static local variable declaration (not allowed in Python):
    CreatePlayerSaveQuery_text = str(['\0' for _ in range(8192 + 1)])

    @staticmethod
    def CreatePlayerSaveQuery(pszQuery, querySize, pkTab):
        queryLen = size_t()

        queryLen = snprintf(pszQuery.arg_value, querySize, "UPDATE player%s SET " + "job = %d, " + "voice = %d, " + "dir = %d, " + "x = %d, " + "y = %d, " + "z = %d, " + "map_index = %d, " + "exit_x = %ld, " + "exit_y = %ld, " + "exit_map_index = %ld, " + "hp = %d, " + "mp = %d, " + "stamina = %d, " + "random_hp = %d, " + "random_sp = %d, " + "playtime = %d, " + "level = %d, " + "level_step = %d, " + "st = %d, " + "ht = %d, " + "dx = %d, " + "iq = %d, " + "gold = %lld, " + "exp = %u, " + "stat_point = %d, " + "LG_SKILL_point = %d, " + "sub_LG_SKILL_point = %d, " + "stat_reset_count = %d, " + "ip = '%s', " + "part_main = %d, " + "part_hair = %d, " + "part_acce = %d, " + "last_play = NOW(), " + "LG_SKILL_group = %d, " + "alignment = %ld, " + "horse_level = %d, " + "horse_riding = %d, " + "horse_hp = %d, " + "horse_hp_droptime = %u, " + "horse_stamina = %d, " + "horse_LG_SKILL_point = %d, ", GetTablePostfix(), pkTab.job, pkTab.voice, pkTab.dir, pkTab.x, pkTab.y, pkTab.z, pkTab.lMapIndex, pkTab.lExitX, pkTab.lExitY, pkTab.lExitMapIndex, pkTab.hp, pkTab.sp, pkTab.stamina, pkTab.sRandomHP, pkTab.sRandomSP, pkTab.playtime, pkTab.level, pkTab.level_step, pkTab.st, pkTab.ht, pkTab.dx, pkTab.iq, pkTab.gold, pkTab.exp, pkTab.stat_point, pkTab.LG_SKILL_point, pkTab.sub_LG_SKILL_point, pkTab.stat_reset_count, pkTab.ip, pkTab.parts[PART_MAIN], pkTab.parts[PART_HAIR], pkTab.parts[PART_ACCE], pkTab.LG_SKILL_group, pkTab.lAlignment, pkTab.horse.bLevel, pkTab.horse.bRiding, pkTab.horse.sHealth, pkTab.horse.dwHorseHealthDropTime, pkTab.horse.sStamina, pkTab.horse_LG_SKILL_point)

        #Laniatus Games Studio Inc. | Python Metin II Server Note This static local variable declaration (not allowed in Python) has been moved just prior to the method:
        #    static char text[8192 + 1]

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        CDBManager.instance().EscapeString(CreatePlayerSaveQuery_text, pkTab.skills, sizeof(pkTab.skills))
        queryLen += snprintf(pszQuery.arg_value + queryLen, querySize - queryLen, "LG_SKILL_level = '%s', ", CreatePlayerSaveQuery_text)

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        CDBManager.instance().EscapeString(CreatePlayerSaveQuery_text, pkTab.quickslot, sizeof(pkTab.quickslot))
        queryLen += snprintf(pszQuery.arg_value + queryLen, querySize - queryLen, "quickslot = '%s' ", CreatePlayerSaveQuery_text)

        queryLen += snprintf(pszQuery.arg_value + queryLen, querySize - queryLen, " WHERE id=%d", pkTab.id)
        return size_t(queryLen)

    #Laniatus Games Studio Inc. | Python Metin II Server Note This was formerly a static local variable declaration (not allowed in Python):
    QUERY_PLAYER_LOAD_s_items = []

    @staticmethod
    def CreatePlayerTableFromRes(res, pkTab):
        if mysql_num_rows(res) == 0:
            return DefineConstants.false

# Laniatus Games Studio Inc. |  TODO TASK: The memory management function 'memset' has no equivalent in Python:
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        memset(pkTab, 0, sizeof(TPlayerTable))

        row = mysql_fetch_row(res)

        col = 0

#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(pkTab->id, row[col++]);
        str_to_number(pkTab.id, row[col])
        col += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: strlcpy(pkTab->name, row[col++], sizeof(pkTab->name));
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        strlcpy(pkTab.name, row[col], sizeof(pkTab.name))
        col += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(pkTab->job, row[col++]);
        str_to_number(pkTab.job, row[col])
        col += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(pkTab->voice, row[col++]);
        str_to_number(pkTab.voice, row[col])
        col += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(pkTab->dir, row[col++]);
        str_to_number(pkTab.dir, row[col])
        col += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(pkTab->x, row[col++]);
        str_to_number(pkTab.x, row[col])
        col += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(pkTab->y, row[col++]);
        str_to_number(pkTab.y, row[col])
        col += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(pkTab->z, row[col++]);
        str_to_number(pkTab.z, row[col])
        col += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(pkTab->lMapIndex, row[col++]);
        str_to_number(pkTab.lMapIndex, row[col])
        col += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(pkTab->lExitX, row[col++]);
        str_to_number(pkTab.lExitX, row[col])
        col += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(pkTab->lExitY, row[col++]);
        str_to_number(pkTab.lExitY, row[col])
        col += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(pkTab->lExitMapIndex, row[col++]);
        str_to_number(pkTab.lExitMapIndex, row[col])
        col += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(pkTab->hp, row[col++]);
        str_to_number(pkTab.hp, row[col])
        col += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(pkTab->sp, row[col++]);
        str_to_number(pkTab.sp, row[col])
        col += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(pkTab->stamina, row[col++]);
        str_to_number(pkTab.stamina, row[col])
        col += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(pkTab->sRandomHP, row[col++]);
        str_to_number(pkTab.sRandomHP, row[col])
        col += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(pkTab->sRandomSP, row[col++]);
        str_to_number(pkTab.sRandomSP, row[col])
        col += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(pkTab->playtime, row[col++]);
        str_to_number(pkTab.playtime, row[col])
        col += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(pkTab->gold, row[col++]);
        str_to_number(pkTab.gold, row[col])
        col += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(pkTab->level, row[col++]);
        str_to_number(pkTab.level, row[col])
        col += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(pkTab->level_step, row[col++]);
        str_to_number(pkTab.level_step, row[col])
        col += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(pkTab->st, row[col++]);
        str_to_number(pkTab.st, row[col])
        col += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(pkTab->ht, row[col++]);
        str_to_number(pkTab.ht, row[col])
        col += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(pkTab->dx, row[col++]);
        str_to_number(pkTab.dx, row[col])
        col += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(pkTab->iq, row[col++]);
        str_to_number(pkTab.iq, row[col])
        col += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(pkTab->exp, row[col++]);
        str_to_number(pkTab.exp, row[col])
        col += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(pkTab->stat_point, row[col++]);
        str_to_number(pkTab.stat_point, row[col])
        col += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(pkTab->LG_SKILL_point, row[col++]);
        str_to_number(pkTab.LG_SKILL_point, row[col])
        col += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(pkTab->sub_LG_SKILL_point, row[col++]);
        str_to_number(pkTab.sub_LG_SKILL_point, row[col])
        col += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(pkTab->stat_reset_count, row[col++]);
        str_to_number(pkTab.stat_reset_count, row[col])
        col += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(pkTab->part_base, row[col++]);
        str_to_number(pkTab.part_base, row[col])
        col += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(pkTab->parts[PART_HAIR], row[col++]);
        str_to_number(pkTab.parts[PART_HAIR], row[col])
        col += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(pkTab->parts[PART_ACCE], row[col++]);
        str_to_number(pkTab.parts[PART_ACCE], row[col])
        col += 1

        if row[col]:
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
            thecore_memcpy(pkTab.skills, row[col], sizeof(pkTab.skills))
        else:
# Laniatus Games Studio Inc. |  TODO TASK: The memory management function 'memset' has no equivalent in Python:
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
            memset(pkTab.skills, 0, sizeof(pkTab.skills))

        col += 1

        if row[col]:
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
            thecore_memcpy(pkTab.quickslot, row[col], sizeof(pkTab.quickslot))
        else:
# Laniatus Games Studio Inc. |  TODO TASK: The memory management function 'memset' has no equivalent in Python:
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
            memset(pkTab.quickslot, 0, sizeof(pkTab.quickslot))

        col += 1

#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(pkTab->LG_SKILL_group, row[col++]);
        str_to_number(pkTab.LG_SKILL_group, row[col])
        col += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(pkTab->lAlignment, row[col++]);
        str_to_number(pkTab.lAlignment, row[col])
        col += 1

#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(pkTab->horse.bLevel, row[col++]);
        str_to_number(pkTab.horse.bLevel, row[col])
        col += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(pkTab->horse.bRiding, row[col++]);
        str_to_number(pkTab.horse.bRiding, row[col])
        col += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(pkTab->horse.sHealth, row[col++]);
        str_to_number(pkTab.horse.sHealth, row[col])
        col += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(pkTab->horse.dwHorseHealthDropTime, row[col++]);
        str_to_number(pkTab.horse.dwHorseHealthDropTime, row[col])
        col += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(pkTab->horse.sStamina, row[col++]);
        str_to_number(pkTab.horse.sStamina, row[col])
        col += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(pkTab->logoff_interval, row[col++]);
        str_to_number(pkTab.logoff_interval, row[col])
        col += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str_to_number(pkTab->horse_LG_SKILL_point, row[col++]);
        str_to_number(pkTab.horse_LG_SKILL_point, row[col])

            col += 1
            pkTab.skills[123].bLevel = 0

            if pkTab.level > 9:
                max_point = pkTab.level - 9

                LG_SKILL_point = MIN(20, pkTab.skills[121].bLevel) + MIN(20, pkTab.skills[124].bLevel) + MIN(10, pkTab.skills[131].bLevel) + MIN(20, pkTab.skills[141].bLevel) + MIN(20, pkTab.skills[142].bLevel)

                pkTab.sub_LG_SKILL_point = max_point - LG_SKILL_point
            else:
                pkTab.sub_LG_SKILL_point = 0

        return ((not DefineConstants.false))

    #Laniatus Games Studio Inc. | Python Metin II Server Note This was formerly a static local variable declaration (not allowed in Python):
    RESULT_ITEM_LOAD_s_items = []

    #Laniatus Games Studio Inc. | Python Metin II Server Note This was formerly a static local variable declaration (not allowed in Python):
    RESULT_AFFECT_LOAD_s_elements = []

    #Laniatus Games Studio Inc. | Python Metin II Server Note This was formerly a static local variable declaration (not allowed in Python):
    RESULT_QUEST_LOAD_s_table = []

    s_createTimeByAccountID = {}

    #Laniatus Games Studio Inc. | Python Metin II Server Note This was formerly a static local variable declaration (not allowed in Python):
    __QUERY_PLAYER_CREATE_text = str(['\0' for _ in range(4096 + 1)])

#Laniatus Games Studio Inc. | Python Metin II Server Note 'extern' variable declarations are not required in Python:
    #extern int g_iLogoutSeconds

    @staticmethod
    def Trim(str):
        str = str[0:str.find_last_not_of(" \t\r\n") + 1]
        str = str[0:0] + str[0 + str.find_first_not_of(" \t\r\n"):]
        return str

    @staticmethod
    def Lower(original):
        original = original.casefold()
        return original



#Laniatus Games Studio Inc. | Python Metin II Server Note 'extern' variable declarations are not required in Python:
    #extern str g_stLocale

#Laniatus Games Studio Inc. | Python Metin II Server Note 'extern' variable declarations are not required in Python:
    #extern CPacketInfo g_query_info
#Laniatus Games Studio Inc. | Python Metin II Server Note 'extern' variable declarations are not required in Python:
    #extern int g_query_count[2]
    #Laniatus Games Studio Inc. | Python Metin II Server Warnings Statement interrupted by a preprocessor statement:
    #The original statement from the file sal.h starts with:
    #    __inner_fallthrough_dec
    #Preprocessor-interrupted statements cannot be handled by this converter.
    #The remainder of the header file sal.h is ignored.

    GUILD_WARP_WAR_CHANNEL = 99

#Laniatus Games Studio Inc. | Python Metin II Server Note Python has no need of forward class declarations:
    #class CGuildWarReserve

    def less_than(self, a, b):
        return a.GID < b.GID or a.GID == b.GID and a.dwSkillVnum < b.dwSkillVnum

    GUILD_RANK_MAX_NUM = 20

    @staticmethod
    def GetGuildWarWaitStartDuration():
        return 60

    @staticmethod
    def GetGuildWarReserveSeconds():
        return 180

    ##define for_all(cont, it) for (auto it = (cont).begin(); it != (cont).end(); ++it)

    c_aiScoreByLevel = [500, 500, 1000, 2000, 3000, 4000, 6000, 8000, 10000, 12000, 15000, 18000, 21000, 24000, 28000, 32000, 36000, 40000, 45000, 50000, 55000] + [0 for _ in range(GUILD_MAX_LEVEL+1 - 21)]

    c_aiScoreByRanking = [0, 55000, 50000, 45000, 40000, 36000, 32000, 28000, 24000, 21000, 18000, 15000, 12000, 10000, 8000, 6000, 4000, 3000, 2000, 1000, 500] + [0 for _ in range(GUILD_RANK_MAX_NUM+1 - 21)]

    @staticmethod
    def GetAverageGuildMemberLevel(dwGID):
        szQuery = str(['\0' for _ in range(DefineConstants.QUERY_MAX_LEN)])

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        snprintf(szQuery, sizeof(szQuery), "SELECT AVG(level) FROM guild_member%s, player%s AS p WHERE guild_id=%u AND guild_member%s.pid=p.id", GetTablePostfix(), GetTablePostfix(), dwGID, GetTablePostfix())

        msg = std::unique_ptr(CDBManager.instance().DirectQuery(szQuery))

        row = MYSQL_ROW()
        row = mysql_fetch_row(msg.Get().pSQLResult)

        nAverageLevel = 0
        str_to_number(nAverageLevel, row[0])
        return nAverageLevel

    @staticmethod
    def GetGuildMemberCount(dwGID):
        szQuery = str(['\0' for _ in range(DefineConstants.QUERY_MAX_LEN)])

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        snprintf(szQuery, sizeof(szQuery), "SELECT COUNT(*) FROM guild_member%s WHERE guild_id=%u", GetTablePostfix(), dwGID)

        msg = std::unique_ptr(CDBManager.instance().DirectQuery(szQuery))

        row = MYSQL_ROW()
        row = mysql_fetch_row(msg.Get().pSQLResult)

        dwCount = 0
        str_to_number(dwCount, row[0])
        return int(dwCount)








    g_dwLastCachedItemAwardID = 0

    #Laniatus Games Studio Inc. | Python Metin II Server Warnings Statement interrupted by a preprocessor statement:
    #The original statement from the file sal.h starts with:
    #    __inner_fallthrough_dec
    #Preprocessor-interrupted statements cannot be handled by this converter.
    #The remainder of the header file sal.h is ignored.

    @staticmethod
    def SetPlayerDBName(c_pszPlayerDBName):
        if (not c_pszPlayerDBName) != '\0' or (not c_pszPlayerDBName[0]) != '\0':
            g_stPlayerDBName = ""
        else:
            g_stPlayerDBName = c_pszPlayerDBName
            g_stPlayerDBName += "."

    @staticmethod
    def SetTablePostfix(c_pszTablePostfix):
        if (not c_pszTablePostfix) != '\0' or (not c_pszTablePostfix[0]) != '\0':
            g_stTablePostfix = ""
        else:
            g_stTablePostfix = c_pszTablePostfix

    @staticmethod
    def Start():
        if not CConfig.instance().LoadFile("conf.txt"):
            fprintf(stderr, "Loading conf.txt failed.\n")
            return DefineConstants.false

        if not CConfig.instance().GetValue("TEST_SERVER", g_test_server):
            fprintf(stderr, "Real Server\n")
        else:
            fprintf(stderr, "Test Server\n")

        if not CConfig.instance().GetValue("LOG", g_log):
            fprintf(stderr, "Log Off")
            g_log= 0
        else:
            g_log = 1
            fprintf(stderr, "Log On")


        tmpValue = None

        heart_beat = 50
        if not CConfig.instance().GetValue("CLIENT_HEART_FPS", heart_beat):
            fprintf(stderr, "Cannot find CLIENT_HEART_FPS configuration.\n")
            return DefineConstants.false

        log_set_expiration_days(3)

        if CConfig.instance().GetValue("LOG_KEEP_DAYS", tmpValue):
            tmpValue = MINMAX(3, tmpValue, 30)
            log_set_expiration_days(tmpValue)
            fprintf(stderr, "Setting log keeping days to %d\n", tmpValue)

        thecore_init(heart_beat, emptybeat)
        signal_timer_enable(60)

        szBuf = str(['\0' for _ in range(256+1)])

        if CConfig.instance().GetValue("LOCALE", szBuf, 256):
            g_stLocale = szBuf
            sys_log(0, "LOCALE set to %s", g_stLocale.c_str())

        iNoTXT = 0
        if CConfig.instance().GetValue("NO_TXT", iNoTXT):
            if iNoTXT == 1:
                sys_log(0, "CONFIG: NO_TXT")
                g_noTXT = ((not DefineConstants.false))

        if not CConfig.instance().GetValue("TABLE_POSTFIX", szBuf, 256):
            szBuf[0] = '\0'

        SetTablePostfix(szBuf)

        if CConfig.instance().GetValue("PLAYER_CACHE_FLUSH_SECONDS", szBuf, 256):
            str_to_number(g_iPlayerCacheFlushSeconds, szBuf)
            sys_log(0, "PLAYER_CACHE_FLUSH_SECONDS: %d", g_iPlayerCacheFlushSeconds)

        if CConfig.instance().GetValue("ITEM_CACHE_FLUSH_SECONDS", szBuf, 256):
            str_to_number(g_iItemCacheFlushSeconds, szBuf)
            sys_log(0, "ITEM_CACHE_FLUSH_SECONDS: %d", g_iItemCacheFlushSeconds)

        if CConfig.instance().GetValue("ITEM_PRICELIST_CACHE_FLUSH_SECONDS", szBuf, 256):
            str_to_number(g_iItemPriceListTableCacheFlushSeconds, szBuf)
            sys_log(0, "ITEM_PRICELIST_CACHE_FLUSH_SECONDS: %d", g_iItemPriceListTableCacheFlushSeconds)

        if CConfig.instance().GetValue("CACHE_FLUSH_LIMIT_PER_SECOND", szBuf, 256):
            dwVal = 0
            str_to_number(dwVal, szBuf)
            CClientManager.instance().SetCacheFlushCountLimit(dwVal)

        iIDStart = None
        if not CConfig.instance().GetValue("PLAYER_ID_START", iIDStart):
            sys_err("PLAYER_ID_START not configured")
            return DefineConstants.false

        CClientManager.instance().SetPlayerIDStart(iIDStart)

        if CConfig.instance().GetValue("NAME_COLUMN", szBuf, 256):
            fprintf(stderr, "%s %s", g_stLocaleNameColumn.c_str(), szBuf)
            g_stLocaleNameColumn = szBuf

        szAddr = str(['\0' for _ in range(64)])
        szDB = str(['\0' for _ in range(64)])
        szUser = str(['\0' for _ in range(64)])
        szPassword = str(['\0' for _ in range(64)])
        iPort = None
        line = str(['\0' for _ in range(256+1)])

        if CConfig.instance().GetValue("SQL_PLAYER", line, 256):
            sscanf(line, " %s %s %s %s %d ", szAddr, szDB, szUser, szPassword, iPort)
            sys_log(0, "connecting to MySQL server (player)")

            iRetry = 5

            condition = True
            while condition:
                if CDBManager.instance().Connect(SQL_PLAYER, szAddr, iPort, szDB, szUser, szPassword):
                    sys_log(0, "   OK")
                    break

                sys_log(0, "   failed, retrying in 5 seconds")
                fprintf(stderr, "   failed, retrying in 5 seconds")
                sleep(5)
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: } while (iRetry--);
                condition = iRetry
            iRetry -= 1
            fprintf(stderr, "Success PLAYER\n")
            SetPlayerDBName(szDB)
        else:
            sys_err("SQL_PLAYER not configured")
            return DefineConstants.false

        if CConfig.instance().GetValue("SQL_ACCOUNT", line, 256):
            sscanf(line, " %s %s %s %s %d ", szAddr, szDB, szUser, szPassword, iPort)
            sys_log(0, "connecting to MySQL server (account)")

            iRetry = 5

            condition = True
            while condition:
                if CDBManager.instance().Connect(SQL_ACCOUNT, szAddr, iPort, szDB, szUser, szPassword):
                    sys_log(0, "   OK")
                    break

                sys_log(0, "   failed, retrying in 5 seconds")
                fprintf(stderr, "   failed, retrying in 5 seconds")
                sleep(5)
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: } while (iRetry--);
                condition = iRetry
            iRetry -= 1
            fprintf(stderr, "Success ACCOUNT\n")
        else:
            sys_err("SQL_ACCOUNT not configured")
            return DefineConstants.false

        if CConfig.instance().GetValue("SQL_COMMON", line, 256):
            sscanf(line, " %s %s %s %s %d ", szAddr, szDB, szUser, szPassword, iPort)
            sys_log(0, "connecting to MySQL server (common)")

            iRetry = 5

            condition = True
            while condition:
                if CDBManager.instance().Connect(SQL_COMMON, szAddr, iPort, szDB, szUser, szPassword):
                    sys_log(0, "   OK")
                    break

                sys_log(0, "   failed, retrying in 5 seconds")
                fprintf(stderr, "   failed, retrying in 5 seconds")
                sleep(5)
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: } while (iRetry--);
                condition = iRetry
            iRetry -= 1
            fprintf(stderr, "Success COMMON\n")
        else:
            sys_err("SQL_COMMON not configured")
            return DefineConstants.false

        if not CNetPoller.instance().Create():
            sys_err("Cannot create network poller")
            return DefineConstants.false

        sys_log(0, "ClientManager initialization.. ")

        if not CClientManager.instance().Initialize():
            sys_log(0, "   failed")
            return DefineConstants.false

        sys_log(0, "   OK")

        signal(SIGUSR1, emergency_sig)
        signal(SIGSEGV, emergency_sig)
        return 1 if ((not DefineConstants.false)) else 0

    g_stTablePostfix = ""
    g_stLocaleNameColumn = "name"
    g_stLocale = "latin1"
    g_stPlayerDBName = ""
    g_test_server = DefineConstants.false
    g_noTXT = DefineConstants.false

    g_iPlayerCacheFlushSeconds = 60 *7
    g_iItemCacheFlushSeconds = 60 *5
    g_iLogoutSeconds = 60 *10
    g_log = 1
    g_iItemPriceListTableCacheFlushSeconds = 540

//Laniatus Games Studio Inc. T.F | TODO TASK: The implementation of the following method could not be found:
    //WriteVersion()

    @staticmethod
    def emergency_sig(sig):
        if sig == SIGSEGV:
            sys_log(0, "SIGNAL: SIGSEGV")
        elif sig == SIGUSR1:
            sys_log(0, "SIGNAL: SIGUSR1")

        if sig == SIGSEGV:
            abort()

    @staticmethod
    def emptybeat(heart, pulse):
        if not(math.fmod(pulse, heart.passes_per_sec)):
            pass

    @staticmethod
    def GetTablePostfix():
        return g_stTablePostfix.c_str()

    @staticmethod
    def GetPlayerDBName():
        return g_stPlayerDBName.c_str()





    PRIV_DURATION = 60 *60 *12
    CHARACTER_GOOD_PRIV_DURATION = 2 *60 *60
    CHARACTER_BAD_PRIV_DURATION = 60 *60
    @staticmethod
    def WriteVersion():
        fp = FILE(fopen("VERSION.txt", "w"))
        if None is not fp:
            fprintf(fp, "game perforce revision: %s\n", DefineConstants.VERSION)
            fclose(fp)
        else:
            fprintf(stderr, "cannot open VERSION.txt\n")
            exit(0)


//Laniatus Games Studio Inc. T.F | TODO TASK: The implementation of the following method could not be found:
    //Start()
//Laniatus Games Studio Inc. T.F | TODO TASK: The implementation of the following method could not be found:
    //GetTablePostfix()
//Laniatus Games Studio Inc. T.F | TODO TASK: The implementation of the following method could not be found:
    //GetPlayerDBName()

    # Laniatus Games Studio Inc. |  TODO TASK: There is no preprocessor in Python:
    ##if _WIN32
    # Laniatus Games Studio Inc. |  TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
    ##define INLINE inline
    ##else
    # Laniatus Games Studio Inc. |  TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
    ##define INLINE __inline__
    ##endif

    # Laniatus Games Studio Inc. |  TODO TASK: There is no preprocessor in Python:
    ##if ! _WIN32
    # Laniatus Games Studio Inc. |  TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
    ##define true (!false)
    ##endif

    #Laniatus Games Studio Inc. | Python Metin II Server Note The following #define macro was replaced in-line:
    #ORIGINAL LINE: #define FALSE false
    #Laniatus Games Studio Inc. | Python Metin II Server Note The following #define macro was replaced in-line:
    #ORIGINAL LINE: #define TRUE (!FALSE)

    # Laniatus Games Studio Inc. |  TODO TASK: There is no preprocessor in Python:
    ##if _WIN32
    ##define WIN32_LEAN_AND_MEAN

    #Laniatus Games Studio Inc. | Python Metin II Server Warnings Statement interrupted by a preprocessor statement:
    #The original statement from the file sal.h starts with:
    #    __inner_fallthrough_dec
    #Preprocessor-interrupted statements cannot be handled by this converter.
    #The remainder of the header file sal.h is ignored.

    #Laniatus Games Studio Inc. | Python Metin II Server Warnings The following #include directive was ignored:
    ##include "xdirent.h"
    #Laniatus Games Studio Inc. | Python Metin II Server Warnings The following #include directive was ignored:
    ##include "xgetopt.h"

    # Laniatus Games Studio Inc. |  TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
    ##define S_ISDIR(m) (m & _S_IFDIR)

    # Laniatus Games Studio Inc. |  TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
    ##define strlcat(dst, src, size) strcat_s(dst, size, src)
    # Laniatus Games Studio Inc. |  TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
    ##define strlcpy(dst, src, size) strncpy_s(dst, size, src, _TRUNCATE)
    # Laniatus Games Studio Inc. |  TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
    ##define strcasecmp(s1, s2) _stricmp(s1, s2)
    # Laniatus Games Studio Inc. |  TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
    ##define strncasecmp(s1, s2, n) _strnicmp(s1, s2, n)
    # Laniatus Games Studio Inc. |  TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
    ##define strtok_r(s, delim, ptrptr) strtok_s(s, delim, ptrptr)
    # Laniatus Games Studio Inc. |  TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
    ##define localtime_r(timet, result) localtime_s(result, timet)


    @staticmethod
    def usleep(usec):
        Sleep(math.trunc(usec / float(1000)))

    @staticmethod
    def sleep(sec):
        Sleep(sec * 1000)
        return 0

    # Laniatus Games Studio Inc. |  TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
    ##define PATH_MAX _MAX_PATH
    ##else
    #Laniatus Games Studio Inc. | Python Metin II Server Warnings The following #include directive was ignored:
    ##include <unistd.h>
    #Laniatus Games Studio Inc. | Python Metin II Server Warnings The following #include directive was ignored:
    ##include <dirent.h>


    #Laniatus Games Studio Inc. | Python Metin II Server Warnings The following #include directive was ignored:
    ##include <netinet/in.h>
    #Laniatus Games Studio Inc. | Python Metin II Server Warnings The following #include directive was ignored:
    ##include <arpa/inet.h>
    #Laniatus Games Studio Inc. | Python Metin II Server Warnings The following #include directive was ignored:
    ##include <netdb.h>
    #Laniatus Games Studio Inc. | Python Metin II Server Warnings The following #include directive was ignored:
    ##include <sys/socket.h>

    #Laniatus Games Studio Inc. | Python Metin II Server Warnings The following #include directive was ignored:
    ##include <sys/wait.h>

    #Laniatus Games Studio Inc. | Python Metin II Server Warnings The following #include directive was ignored:
    ##include <pthread.h>
    #Laniatus Games Studio Inc. | Python Metin II Server Warnings Statement interrupted by a preprocessor statement:
    #The original statement from the file DriverSpecs.h starts with:
    #    __ANNOTATION(SAL_landmark(__In_impl_ char *);)
    #Preprocessor-interrupted statements cannot be handled by this converter.
    #The remainder of the header file DriverSpecs.h is ignored.
    ##endif

    #Laniatus Games Studio Inc. | Python Metin II Server Warnings The following #include directive was ignored:
    ##include "typedef.h"
    #Laniatus Games Studio Inc. | Python Metin II Server Warnings The following #include directive was ignored:
    ##include "heart.h"
    #Laniatus Games Studio Inc. | Python Metin II Server Warnings The following #include directive was ignored:
    ##include "fdwatch.h"
    #Laniatus Games Studio Inc. | Python Metin II Server Warnings The following #include directive was ignored:
    ##include "socket.h"
    #Laniatus Games Studio Inc. | Python Metin II Server Warnings The following #include directive was ignored:
    ##include "kstbl.h"
    #Laniatus Games Studio Inc. | Python Metin II Server Warnings The following #include directive was ignored:
    ##include "hangul.h"
    #Laniatus Games Studio Inc. | Python Metin II Server Warnings The following #include directive was ignored:
    ##include "buffer.h"
    #Laniatus Games Studio Inc. | Python Metin II Server Warnings The following #include directive was ignored:
    ##include "log.h"
    #Laniatus Games Studio Inc. | Python Metin II Server Warnings The following #include directive was ignored:
    ##include "utils.h"
    #Laniatus Games Studio Inc. | Python Metin II Server Warnings The following #include directive was ignored:
    ##include "crypt.h"
    #Laniatus Games Studio Inc. | Python Metin II Server Warnings The following #include directive was ignored:
    ##include "memcpy.h"
