from enum import Enum

class SUseTime:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.dwLoginKey = 0
        self.szLogin = str(['\0' for _ in range((int)LGEMiscellaneous.LOGIN_MAX_LEN+1)])
        self.dwUseSec = 0
        self.szIP = str(['\0' for _ in range((int)LGEMiscellaneous.LG_MAX_HOST_LENGTH+1)])


class CQueryInfo:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.iQueryType = 0


class CReturnQueryInfo(CQueryInfo):

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.iType = 0
        self.dwIdent = 0
        self.pvData = None


class CFuncQueryInfo(CQueryInfo):

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.f = _boost_func_of_SQLMsg.any()


class CFuncAfterQueryInfo(CQueryInfo):

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.f = _boost_func_of_void.any()


## Laniatus Games Studio Inc. | NOTE: Python has no need of forward class declarations:
#class CLoginData

class DBManager(singleton):
    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self._m_sql = CAsyncSQL()
        self._m_sql_direct = CAsyncSQL()
        self._m_bIsConnect = False
        self._m_map_pkLoginData = {}
        self._m_vec_kUseTime = []

        self._m_bIsConnect = LGEMiscellaneous.DEFINECONSTANTS.false

    def close(self):
        pass

    def IsConnected(self):
        return self._m_bIsConnect

    def Connect(self, host, port, user, pwd, db):
        if self._m_sql.Setup(host, user, pwd, db, g_stLocale.c_str(), LGEMiscellaneous.DEFINECONSTANTS.false, port):
            self._m_bIsConnect = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        if not self._m_sql_direct.Setup(host, user, pwd, db, g_stLocale.c_str(), ((not LGEMiscellaneous.DEFINECONSTANTS.false)), port):
            #lani_err("cannot open direct sql connection to host %s", host)

        return self._m_bIsConnect

    def Query(self, c_pszFormat, *LegacyParamArray):
        szQuery = str(['\0' for _ in range(4096)])
        args = None

        ParamCount = -1
#        va_start(args, c_pszFormat)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        vsnprintf(szQuery, sizeof(szQuery), c_pszFormat, args)
#        va_end(args)

        self._m_sql.AsyncQuery(szQuery)

    def DirectQuery(self, c_pszFormat, *LegacyParamArray):
        szQuery = str(['\0' for _ in range(4096)])
        args = None

        ParamCount = -1
#        va_start(args, c_pszFormat)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        vsnprintf(szQuery, sizeof(szQuery), c_pszFormat, args)
#        va_end(args)

        return self._m_sql_direct.DirectQuery(szQuery)

    def ReturnQuery(self, iType, dwIdent, pvData, c_pszFormat, *LegacyParamArray):
        szQuery = str(['\0' for _ in range(4096)])
        args = None

        ParamCount = -1
#        va_start(args, c_pszFormat)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        vsnprintf(szQuery, sizeof(szQuery), c_pszFormat, args)
#        va_end(args)

        p = LG_NEW_M2 CReturnQueryInfo

        p.iQueryType = Globals.QUERY_TYPE_RETURN
        p.iType = iType
        p.dwIdent = dwIdent
        p.pvData = pvData

        self._m_sql.ReturnQuery(szQuery, p)

    def Process(self):
        pMsg = None

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: while ((pMsg = PopResult()))
        while (pMsg = self._PopResult()):
            if None != pMsg.pvUserData:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no equivalent to 'reinterpret_cast' in Python:
                if reinterpret_cast<CQueryInfo>(pMsg.pvUserData).iQueryType == Globals.QUERY_TYPE_RETURN:
                    self.AnalyzeReturnQuery(pMsg)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no equivalent to 'reinterpret_cast' in Python:
                elif reinterpret_cast<CQueryInfo>(pMsg.pvUserData).iQueryType == Globals.QUERY_TYPE_FUNCTION:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no equivalent to 'reinterpret_cast' in Python:
                        qi = reinterpret_cast<CFuncQueryInfo>(pMsg.pvUserData)
                        qi.f.functor_method(pMsg)
                        LG_DEL_MEM(qi)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no equivalent to 'reinterpret_cast' in Python:
                elif reinterpret_cast<CQueryInfo>(pMsg.pvUserData).iQueryType == Globals.QUERY_TYPE_AFTER_FUNCTION:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no equivalent to 'reinterpret_cast' in Python:
                        qi = reinterpret_cast<CFuncAfterQueryInfo>(pMsg.pvUserData)
                        qi.f()
                        LG_DEL_MEM(qi)

            if pMsg is not None:
                pMsg.close()

    def AnalyzeReturnQuery(self, pMsg):
        qi = pMsg.pvUserData

        if qi.iType == Globals.QID_AUTH_LOGIN:
                pinfo = qi.pvData
                d = DESC_MANAGER.instance().FindByLoginKey(qi.dwIdent)

                if d is None:
                    LG_DEL_MEM(pinfo)
                    break
                d.SetLogin(pinfo.login)

                #sys_log(0, "QID_AUTH_LOGIN: START %u %p", qi.dwIdent, Globals.get_pointer(d))

                if pMsg.Get().uiNumRows == 0:
                    #sys_log(0, "   NOID")
                    LoginFailure(d, "NOID")
                    LG_DEL_MEM(pinfo)
                    return
                else:
                    row = mysql_fetch_row(pMsg.Get().pSQLResult)
                    col = 0

                    szEncrytPassword = str(['\0' for _ in range(45 + 1)])
                    szPassword = str(['\0' for _ in range(45 + 1)])
                    szSocialID = str(['\0' for _ in range((int)LGEMiscellaneous.SOCIAL_ID_MAX_LEN + 1)])
                    szStatus = str(['\0' for _ in range((int)LGEMiscellaneous.ACCOUNT_STATUS_MAX_LEN + 1)])
                    dwID = 0
                    gmLevel = EGMLevels.GM_PLAYER
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if __MULTI_LANGUAGE_SYSTEM__
                    bLanguage = LaniatusLocalization.LOCALE_DEFAULT
##endif

                    if not row[col]:
                        #lani_err("error column %d", col)
                        LG_DEL_MEM(pinfo)
                        break

## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: strncpy_s(szEncrytPassword, sizeof(szEncrytPassword), row[col++], _TRUNCATE);
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                    strncpy_s(szEncrytPassword, sizeof(szEncrytPassword), row[col], _TRUNCATE)
                    col += 1

                    if not row[col]:
                        #lani_err("error column %d", col)
                        LG_DEL_MEM(pinfo)
                        break

## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: strncpy_s(szPassword, sizeof(szPassword), row[col++], _TRUNCATE);
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                    strncpy_s(szPassword, sizeof(szPassword), row[col], _TRUNCATE)
                    col += 1

                    if not row[col]:
                        #lani_err("error column %d", col)
                        LG_DEL_MEM(pinfo)
                        break

## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: strncpy_s(szSocialID, sizeof(szSocialID), row[col++], _TRUNCATE);
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                    strncpy_s(szSocialID, sizeof(szSocialID), row[col], _TRUNCATE)
                    col += 1

                    if not row[col]:
                        #lani_err("error column %d", col)
                        LG_DEL_MEM(pinfo)
                        break

                    temp_ref_dwID = RefObject(dwID);
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: str_to_number(dwID, row[col++]);
                    Globals.str_to_number(temp_ref_dwID, row[col])
                    col += 1
                    dwID = temp_ref_dwID.arg_value

                    if not row[col]:
                        #lani_err("error column %d", col)
                        LG_DEL_MEM(pinfo)
                        break

## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: strncpy_s(szStatus, sizeof(szStatus), row[col++], _TRUNCATE);
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                    strncpy_s(szStatus, sizeof(szStatus), row[col], _TRUNCATE)
                    col += 1

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if __MULTI_LANGUAGE_SYSTEM__
                    if not row[col]:
                        #lani_err("error column %d", col)
                        LG_DEL_MEM(pinfo)
                        break
                    temp_ref_bLanguage = RefObject(bLanguage);
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: str_to_number(bLanguage, row[col++]);
                    Globals.str_to_number(temp_ref_bLanguage, row[col])
                    col += 1
                    bLanguage = temp_ref_bLanguage.arg_value
##endif

                    if not row[col]:
                        #lani_err("error column %d", col)
                        LG_DEL_MEM(pinfo)
                        break

                    temp_ref_gmLevel = RefObject(gmLevel);
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: str_to_number(gmLevel, row[col++]);
                    Globals.str_to_number(temp_ref_gmLevel, row[col])
                    col += 1
                    gmLevel = temp_ref_gmLevel.arg_value

                    bNotAvail = 0
                    temp_ref_bNotAvail = RefObject(bNotAvail);
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: str_to_number(bNotAvail, row[col++]);
                    Globals.str_to_number(temp_ref_bNotAvail, row[col])
                    col += 1
                    bNotAvail = temp_ref_bNotAvail.arg_value

                    aiPremiumTimes = [0 for _ in range((int)EPremiumTypes.PREMIUM_MAX_NUM)]
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                    memset(aiPremiumTimes, 0, sizeof(aiPremiumTimes))

                    szCreateDate = "00000000"

## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: str_to_number(aiPremiumTimes[PREMIUM_EXP], row[col++]);
                    Globals.str_to_number(aiPremiumTimes[(int)EPremiumTypes.PREMIUM_EXP] != 0, row[col])
                    col += 1
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: str_to_number(aiPremiumTimes[PREMIUM_ITEM], row[col++]);
                    Globals.str_to_number(aiPremiumTimes[(int)EPremiumTypes.PREMIUM_ITEM] != 0, row[col])
                    col += 1
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: str_to_number(aiPremiumTimes[PREMIUM_SAFEBOX], row[col++]);
                    Globals.str_to_number(aiPremiumTimes[(int)EPremiumTypes.PREMIUM_SAFEBOX] != 0, row[col])
                    col += 1
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: str_to_number(aiPremiumTimes[PREMIUM_AUTOLOOT], row[col++]);
                    Globals.str_to_number(aiPremiumTimes[(int)EPremiumTypes.PREMIUM_AUTOLOOT] != 0, row[col])
                    col += 1
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: str_to_number(aiPremiumTimes[PREMIUM_FISH_MIND], row[col++]);
                    Globals.str_to_number(aiPremiumTimes[(int)EPremiumTypes.PREMIUM_FISH_MIND] != 0, row[col])
                    col += 1
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: str_to_number(aiPremiumTimes[PREMIUM_MARRIAGE_FAST], row[col++]);
                    Globals.str_to_number(aiPremiumTimes[(int)EPremiumTypes.PREMIUM_MARRIAGE_FAST] != 0, row[col])
                    col += 1
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: str_to_number(aiPremiumTimes[PREMIUM_GOLD], row[col++]);
                    Globals.str_to_number(aiPremiumTimes[(int)EPremiumTypes.PREMIUM_GOLD] != 0, row[col])
                    col += 1

                    if test_server:
                        retValue = 0
                        temp_ref_retValue = RefObject(retValue);
                        Globals.str_to_number(temp_ref_retValue, row[col])
                        retValue = temp_ref_retValue.arg_value

                        create_time = retValue
                        tm1 = None
                        tm1 = localtime(create_time)
                        strftime(szCreateDate, 255, "%Y%m%d", tm1)

                        #sys_log(0, "Create_Time %d %s", retValue, szCreateDate)
                        #sys_log(0, "Block Time %d ", strncmp(szCreateDate, g_stBlockDate.c_str(), 8))
                        col += 1

                    nPasswordDiff = strcmp(szEncrytPassword, szPassword)

                    if nPasswordDiff != 0:
                        LoginFailure(d, "WRONGPWD")
                        #sys_log(0, "   WRONGPWD")
                        LG_DEL_MEM(pinfo)
                    elif bNotAvail != 0:
                        LoginFailure(d, "NOTAVAIL")
                        #sys_log(0, "   NOTAVAIL")
                        LG_DEL_MEM(pinfo)
                    elif DESC_MANAGER.instance().FindByLoginName(pinfo.login):
                        LoginFailure(d, "ALREADY")
                        #sys_log(0, "   ALREADY")
                        LG_DEL_MEM(pinfo)
                    elif strcmp(szStatus, "OK"):
                        LoginFailure(d, szStatus)
                        #sys_log(0, "   STATUS: %s", szStatus)
                        LG_DEL_MEM(pinfo)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if __MULTI_LANGUAGE_SYSTEM__
                    elif pinfo.bLanguage >= LaniatusLocalization.LOCALE_MAX_NUM:
                        LoginFailure(d, "INVLANG")
                        #sys_log(0, "Invalid language selected.")
                        LG_DEL_MEM(pinfo)
                    elif pinfo.bLanguage == 0:
                        LoginFailure(d, "NOLANG")
                        #sys_log(0, "No language selected.")
                        LG_DEL_MEM(pinfo)
##endif
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if ! _IMPROVED_PACKET_ENCRYPTION_
                    elif g_isShutdowned and gmLevel == EGMLevels.GM_PLAYER:
                        #sys_log(0, "   SHUTDOWN")
                        LoginFailure(d, "SHUTDOWN")
                        LG_DEL_MEM(pinfo)
                        return
##endif
                    else:
                        if strncmp(szCreateDate, g_stBlockDate.c_str(), 8) >= 0:
                            LoginFailure(d, "BLKLOGIN")
                            #sys_log(0, "   BLKLOGIN")
                            LG_DEL_MEM(pinfo)
                            break

                        szQuery = str(['\0' for _ in range(1024)])
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if __MULTI_LANGUAGE_SYSTEM__
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                        snprintf(szQuery, sizeof(szQuery), "UPDATE account SET last_play=NOW(), language=%u WHERE id=%u", pinfo.bLanguage, dwID)
##else
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                        snprintf(szQuery, sizeof(szQuery), "UPDATE account SET last_play=NOW() WHERE id=%u", dwID)
##endif
                        msg = std::unique_ptr(DBManager.instance().DirectQuery(szQuery))

                        r = d.GetAccountTable()

                        r.id = dwID
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                        trim_and_lower(pinfo.login, r.login, sizeof(r.login))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                        strncpy_s(r.passwd, sizeof(r.passwd), pinfo.passwd, _TRUNCATE)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                        strncpy_s(r.social_id, sizeof(r.social_id), szSocialID, _TRUNCATE)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if __MULTI_LANGUAGE_SYSTEM__
                        r.bLanguage = pinfo.bLanguage
##endif
                        DESC_MANAGER.instance().ConnectAccount(r.login, d)

                        temp_ref_adwClientKey = RefObject(pinfo.adwClientKey);
                        temp_ref_aiPremiumTimes = RefObject(aiPremiumTimes);
                        self.LoginPrepare(d, temp_ref_adwClientKey, temp_ref_aiPremiumTimes)
                        aiPremiumTimes = temp_ref_aiPremiumTimes.arg_value
                        pinfo.adwClientKey = temp_ref_adwClientKey.arg_value
                        LG_DEL_MEM(pinfo)
                        break

                        #sys_log(0, "QID_AUTH_LOGIN: SUCCESS %s", pinfo.login)

        elif qi.iType == Globals.QID_SAFEBOX_SIZE:
                ch = CHARACTER_MANAGER.instance().FindByPID(qi.dwIdent)

                if ch:
                    if pMsg.Get().uiNumRows > 0:
                        row = mysql_fetch_row(pMsg.Get().pSQLResult)
                        size = 0
                        temp_ref_size = RefObject(size);
                        Globals.str_to_number(temp_ref_size, row[0])
                        size = temp_ref_size.arg_value
                        ch.SetSafeboxSize(Globals.SAFEBOX_PAGE_SIZE * size)

        elif qi.iType == Globals.QID_HIGHSCORE_REGISTER:
                info = qi.pvData
                bQuery = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

                if pMsg.Get().uiNumRows:
                    row = mysql_fetch_row(pMsg.Get().pSQLResult)

                    if row is not None and row[0]:
                        iCur = 0
                        temp_ref_iCur = RefObject(iCur);
                        Globals.str_to_number(temp_ref_iCur, row[0])
                        iCur = temp_ref_iCur.arg_value

                        if (info.bOrder and iCur >= info.iValue) or ((not info.bOrder) and iCur <= info.iValue):
                            bQuery = LGEMiscellaneous.DEFINECONSTANTS.false

                if bQuery:
                    Query("REPLACE INTO highscore%s VALUES('%s', %u, %d)", get_table_postfix(), info.szBoard, info.dwPID, info.iValue)

                LG_DEL_MEM(info)

        elif qi.iType == Globals.QID_HIGHSCORE_SHOW:

        elif qi.iType == Globals.QID_BLOCK_CHAT_LIST:
                ch = CHARACTER_MANAGER.instance().FindByPID(qi.dwIdent)

                if ch is None:
                    break
                if pMsg.Get().uiNumRows:
                    row = MYSQL_ROW()
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: while ((row = mysql_fetch_row(pMsg->Get()->pSQLResult)))
                    while (row = mysql_fetch_row(pMsg.Get().pSQLResult)):
                        ch.ChatPacket(EChatType.CHAT_TYPE_INFO, "%s %s sec", row[0], row[1])
                else:
                    ch.ChatPacket(EChatType.CHAT_TYPE_INFO, "No one currently blocked.")

        else:
            #lani_err("FATAL ERROR!!! Unhandled return query id %d", qi.iType)

        LG_DEL_MEM(qi)

    def LoginPrepare(self, d, pdwClientKey, paiPremiumTimes = None):
        r = d.GetAccountTable()

        pkLD = LG_NEW_M2 CLoginData

        pkLD.SetKey(d.GetLoginKey())
        pkLD.SetLogin(r.login)
        pkLD.SetIP(d.GetHostName())
        pkLD.SetClientKey(pdwClientKey.arg_value)

        if paiPremiumTimes.arg_value:
            pkLD.SetPremium(paiPremiumTimes)

        self.InsertLoginData(pkLD)
        self.SendAuthLogin(d)

    def SendAuthLogin(self, d):
        r = d.GetAccountTable()

        pkLD = self.GetLoginData(d.GetLoginKey())

        if pkLD is None:
            return

        ptod = SPacketGDAuthLogin()
        ptod.dwID = r.id

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        trim_and_lower(r.login, ptod.szLogin, sizeof(ptod.szLogin))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        strncpy_s(ptod.szSocialID, sizeof(ptod.szSocialID), r.social_id, _TRUNCATE)
        ptod.dwLoginKey = d.GetLoginKey()
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if __MULTI_LANGUAGE_SYSTEM__
        ptod.bLanguage = r.bLanguage
##endif

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memcpy' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memcpy(ptod.iPremiumTimes, pkLD.GetPremiumPtr(), sizeof(ptod.iPremiumTimes))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memcpy' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memcpy(ptod.adwClientKey, pkLD.GetClientKey(), sizeof(uint) * 4)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        db_clientdesc.DBPacket(Globals.LG_HEADER_GD_AUTH_LOGIN, d.GetHandle(), ptod, sizeof(SPacketGDAuthLogin))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if __MULTI_LANGUAGE_SYSTEM__
        #sys_log(0, "SendAuthLogin %s language %d key %u", ptod.szLogin, ptod.bLanguage, ptod.dwID)
##else
        #sys_log(0, "SendAuthLogin %s key %u", ptod.szLogin, ptod.dwID)
##endif

        self.SendLoginPing(r.login)

    def SendLoginPing(self, c_pszLogin):
        ptog = SPacketGGLoginPing()

        ptog.bHeader = byte(Globals.LG_HEADER_GG_LOGIN_PING)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        strncpy_s(ptog.szLogin, sizeof(ptog.szLogin), c_pszLogin, _TRUNCATE)

        if not g_pkAuthMasterDesc:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            P2P_MANAGER.instance().Send(ptog, sizeof(SPacketGGLoginPing), NULL)
        else:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            g_pkAuthMasterDesc.Packet(ptog, sizeof(SPacketGGLoginPing))

    def InsertLoginData(self, pkLD):
        self._m_map_pkLoginData.update({pkLD.GetKey(): pkLD})

    def DeleteLoginData(self, pkLD):
        it = self._m_map_pkLoginData.find(pkLD.GetKey())

        if it is self._m_map_pkLoginData.end():
            return

        #sys_log(0, "DeleteLoginData %s %p", pkLD.GetLogin(), pkLD)

        LG_DEL_MEM(it.second)
        self._m_map_pkLoginData.pop(it)

    def GetLoginData(self, dwKey):
        it = self._m_map_pkLoginData.find(dwKey)

        if it is self._m_map_pkLoginData.end():
            return None

        return it.second

    def CountQuery(self):
        return self._m_sql.CountQuery()
    def CountQueryResult(self):
        return self._m_sql.CountResult()
    def ResetQueryResult(self):
        self._m_sql.ResetQueryFinished()

    def FuncQuery(self, f, c_pszFormat, *LegacyParamArray):
        szQuery = str(['\0' for _ in range(4096)])
        args = None

        ParamCount = -1
#        va_start(args, c_pszFormat)
        vsnprintf(szQuery, 4096, c_pszFormat, args)
#        va_end(args)

        p = LG_NEW_M2 CFuncQueryInfo

        p.iQueryType = Globals.QUERY_TYPE_FUNCTION
        p.f = f

        self._m_sql.ReturnQuery(szQuery, p)

    def FuncAfterQuery(self, f, c_pszFormat, *LegacyParamArray):
        szQuery = str(['\0' for _ in range(4096)])
        args = None

        ParamCount = -1
#        va_start(args, c_pszFormat)
        vsnprintf(szQuery, 4096, c_pszFormat, args)
#        va_end(args)

        p = LG_NEW_M2 CFuncAfterQueryInfo

        p.iQueryType = Globals.QUERY_TYPE_AFTER_FUNCTION
        p.f = f

        self._m_sql.ReturnQuery(szQuery, p)

    def EscapeString(self, dst, dstSize, src, srcSize):
        return size_t(self._m_sql_direct.EscapeString(dst, size_t(dstSize), src, size_t(srcSize)))

    def _PopResult(self):
        p = None

        if self._m_sql.PopResult(p):
            return p

        return None


class SHighscoreRegisterQueryInfo:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.szBoard = str(['\0' for _ in range(20+1)])
        self.dwPID = 0
        self.iValue = 0
        self.bOrder = False


class AccountDB(singleton):
    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self._m_sql_direct = CAsyncSQL2()
        self._m_sql = CAsyncSQL2()
        self._m_IsConnect = False

        self._m_IsConnect = LGEMiscellaneous.DEFINECONSTANTS.false

    def IsConnected(self):
        return self._m_IsConnect

    def Connect(self, host, port, user, pwd, db):
        self._m_IsConnect = self._m_sql_direct.Setup(host, user, pwd, db, "", ((not LGEMiscellaneous.DEFINECONSTANTS.false)), port)

        if LGEMiscellaneous.DEFINECONSTANTS.false == self._m_IsConnect:
            fprintf(stderr, "cannot open direct sql connection to host: %s user: %s db: %s\n", host, user, db)
            return LGEMiscellaneous.DEFINECONSTANTS.false

        return self._m_IsConnect

    def ConnectAsync(self, host, port, user, pwd, db, locale):
        self._m_sql.Setup(host, user, pwd, db, locale, LGEMiscellaneous.DEFINECONSTANTS.false, port)
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def DirectQuery(self, query):
        return self._m_sql_direct.DirectQuery(query)

    def ReturnQuery(self, iType, dwIdent, pvData, c_pszFormat, *LegacyParamArray):
        szQuery = str(['\0' for _ in range(4096)])
        args = None

        ParamCount = -1
#        va_start(args, c_pszFormat)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        vsnprintf(szQuery, sizeof(szQuery), c_pszFormat, args)
#        va_end(args)

        p = LG_NEW_M2 CReturnQueryInfo

        p.iQueryType = Globals.QUERY_TYPE_RETURN
        p.iType = iType
        p.dwIdent = dwIdent
        p.pvData = pvData

        self._m_sql.ReturnQuery(szQuery, p)

    def AsyncQuery(self, query):
        self._m_sql.AsyncQuery(query)

    def SetLocale(self, stLocale):
        self._m_sql_direct.SetLocale(stLocale)
        self._m_sql_direct.QueryLocaleSet()

    def Process(self):
        pMsg = None

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: while ((pMsg = PopResult()))
        while (pMsg = self._PopResult()):
            qi = pMsg.pvUserData

            if qi.iQueryType == Globals.QUERY_TYPE_RETURN:
                self._AnalyzeReturnQuery(pMsg)

        if pMsg is not None:
            pMsg.close()

    def _PopResult(self):
        p = None

        if self._m_sql.PopResult(p):
            return p

        return None

    def _AnalyzeReturnQuery(self, pMsg):
        qi = pMsg.pvUserData

        if qi.iType == EAccountQID.QID_SPAM_DB:
                if pMsg.Get().uiNumRows > 0:
                    row = MYSQL_ROW()

                    SpamManager.instance().Clear()

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: while ((row = mysql_fetch_row(pMsg->Get()->pSQLResult)))
                    while (row = mysql_fetch_row(pMsg.Get().pSQLResult)):
                        SpamManager.instance().Insert(row[0], atoi(row[1]))

        LG_DEL_MEM(qi)



class EAccountQID(Enum):
    QID_SPAM_DB = 0

class reload_spam_event_info(event_info_data):

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.empty = 0
