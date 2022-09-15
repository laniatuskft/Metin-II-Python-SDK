## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if ! _WIN32
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
##define #lani_err(fmt, args...) _#lani_err(__FUNCTION__, __LINE__, fmt, ##args)
##else
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
##define #lani_err(fmt, ...) _#lani_err(__FUNCTION__, __LINE__, fmt, __VA_ARGS__)
##endif

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if __cplusplus
##endif



class LogManager(singleton):
    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self._m_sql = CAsyncSQL()
        self._m_bIsConnect = False

        self._m_bIsConnect = LGEMiscellaneous.DEFINECONSTANTS.false

    def close(self):
        pass

    def IsConnected(self):
        return self._m_bIsConnect

    def Connect(self, host, port, user, pwd, db):
        if self._m_sql.Setup(host, user, pwd, db, g_stLocale.c_str(), LGEMiscellaneous.DEFINECONSTANTS.false, port):
            self._m_bIsConnect = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        return self._m_bIsConnect

    def CubeLog(self, dwPID, szName, item_vnum, item_id, item_count, success):
        Query("INSERT DELAYED INTO cube%s (pid, date, name, item_vnum, item_id, item_count, success) VALUES(%u, NOW(), '%s', %u, %u, %u, %u)", get_table_postfix(), dwPID, szName, item_vnum, item_id, item_count,1 if success 1 else 0)

    def GMCommandLog(self, szName, szCommand):
        temp_ref___escape_hint = RefObject(Globals.__escape_hint);
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self._m_sql.EscapeString(temp_ref___escape_hint, sizeof(Globals.__escape_hint), szCommand, strlen(szCommand))
        Globals.__escape_hint = temp_ref___escape_hint.arg_value

        Query("INSERT DELAYED INTO command%s (date, name, command) VALUES(NOW(), '%s', '%s') ", get_table_postfix(), szName, Globals.__escape_hint)

    def ChangeNameLog(self, pid, old_name, new_name, ip):
        Query("INSERT DELAYED INTO change_name%s (pid, old_name, new_name, date, ip) VALUES(%u, '%s', '%s', NOW(), '%s') ", get_table_postfix(), pid, old_name, new_name, ip)

    def BootLog(self, c_pszHostName, bChannel):
        Query("INSERT INTO boot(date, hostname, channel) VALUES(NOW(), '%s', %d)", c_pszHostName, bChannel)

    def QuestRewardLog(self, c_pszQuestName, dwPID, dwLevel, iValue1, iValue2):
        Query("INSERT INTO quest_reward%s VALUES('%s',%u,%u,2,%u,%u,NOW())", get_table_postfix(), c_pszQuestName, dwPID, dwLevel, iValue1, iValue2)

    def ExchangeLogGold(self, from_, to, gold, fromAccID, toAccID):
        Query("INSERT INTO exchange_gold%s (date, `from`, `to`, gold ,fromAccID, toAccID) VALUES(NOW(), '%s', '%s', %lld, %d, %d)", get_table_postfix(), from_, to, gold, fromAccID, toAccID)

    def ExchangeLogItems(self, from_, to, itemname, itemid, count, fromAccID, toAccID):
        Query("INSERT INTO exchange_items%s (date, `from`, `to`, itemname, itemid, count, fromAccID, toAccID) VALUES(NOW(), '%s', '%s', '%s', %d, %d, %d, %d)", get_table_postfix(), from_, to, itemname, itemid, count, fromAccID, toAccID)

    def RefineLog(self, name, itemname, itemid, newitemid, status):
        Query("INSERT INTO refine%s (date, name, itemname, itemid, newitemid, status) VALUES(NOW(), '%s', '%s', %d, %d, '%s')", get_table_postfix(), name, itemname, itemid, newitemid, status)

    def HackLog(self, accountid, name, why):
        Query("INSERT INTO hack%s (date, accountid, name, why) VALUES(NOW(), %d, '%s', '%s')", get_table_postfix(), accountid, name, why)

    def _Query(self, c_pszFormat, *LegacyParamArray):
        szQuery = str(['\0' for _ in range(4096)])
        args = None

        ParamCount = -1
#        va_start(args, c_pszFormat)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        vsnprintf(szQuery, sizeof(szQuery), c_pszFormat, args)
#        va_end(args)

        if test_server:
            #sys_log(0, "LOG: %s", szQuery)

        self._m_sql.AsyncQuery(szQuery)
