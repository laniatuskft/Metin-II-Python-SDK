﻿from enum import Enum

#Laniatus Games Studio Inc. | Python Metin II Server Warnings Statement interrupted by a preprocessor statement:
#The original statement from the file sal.h starts with:
#    __inner_fallthrough_dec
#Preprocessor-interrupted statements cannot be handled by this converter.
#The remainder of the header file sal.h is ignored.
##define SQL_SAFE_LENGTH(size) (size * 2 + 1)
##define QUERY_SAFE_LENGTH(size) (1024 + SQL_SAFE_LENGTH(size))

class CQueryInfo:

class eSQL_SLOT(Enum):
    SQL_PLAYER = 0
    SQL_ACCOUNT = 1
    SQL_COMMON = 2
    SQL_MAX_NUM = 3

class CDBManager(singleton):
    def Initialize(self):
        LaniatusDefVariables = 0
        while LaniatusDefVariables < SQL_MAX_NUM:
            m_mainSQL[LaniatusDefVariables] = None
            m_directSQL[LaniatusDefVariables] = None
            m_asyncSQL[LaniatusDefVariables] = None
            LaniatusDefVariables += 1

    def Destroy(self):
        Clear()

    def __init__(self):
        Initialize()

    def close(self):
        Destroy()

    def Clear(self):
        LaniatusDefVariables = 0
        while LaniatusDefVariables < SQL_MAX_NUM:
            if m_mainSQL[LaniatusDefVariables]:
                m_mainSQL[LaniatusDefVariables] = None
                m_mainSQL[LaniatusDefVariables] = None

            if m_directSQL[LaniatusDefVariables]:
                m_directSQL[LaniatusDefVariables] = None
                m_directSQL[LaniatusDefVariables] = None

            if m_asyncSQL[LaniatusDefVariables]:
                m_asyncSQL[LaniatusDefVariables] = None
                m_asyncSQL[LaniatusDefVariables] = None
            LaniatusDefVariables += 1

        Initialize()

    def Quit(self):
        LaniatusDefVariables = 0
        while LaniatusDefVariables < SQL_MAX_NUM:
            if m_mainSQL[LaniatusDefVariables]:
                m_mainSQL[LaniatusDefVariables].Quit()

            if m_asyncSQL[LaniatusDefVariables]:
                m_asyncSQL[LaniatusDefVariables].Quit()

            if m_directSQL[LaniatusDefVariables]:
                m_directSQL[LaniatusDefVariables].Quit()
            LaniatusDefVariables += 1

    def Connect(self, iSlot, db_address, db_port, db_name, user, pwd):
        if db_address is None or db_name is None:
            return DefineConstants.false

        if iSlot < 0 or iSlot >= SQL_MAX_NUM:
            return DefineConstants.false

        sys_log(0, "CREATING DIRECT_SQL")
        m_directSQL[iSlot] = CAsyncSQL2()
        if not m_directSQL[iSlot].Setup(db_address, user, pwd, db_name, g_stLocale.c_str(), ((not DefineConstants.false)), db_port):
            Clear()
            return DefineConstants.false


        sys_log(0, "CREATING MAIN_SQL")
        m_mainSQL[iSlot] = CAsyncSQL2()
        if not m_mainSQL[iSlot].Setup(db_address, user, pwd, db_name, g_stLocale.c_str(), DefineConstants.false, db_port):
            Clear()
            return DefineConstants.false

        sys_log(0, "CREATING ASYNC_SQL")
        m_asyncSQL[iSlot] = CAsyncSQL2()
        if not m_asyncSQL[iSlot].Setup(db_address, user, pwd, db_name, g_stLocale.c_str(), DefineConstants.false, db_port):
            Clear()
            return DefineConstants.false

        return 1 if ((not DefineConstants.false)) else 0

//Laniatus Games Studio Inc. T.F | TODO TASK: The implementation of the following method could not be found:
//    ReturnQuery(c_pszQuery, iType, dwIdent, pvData, iSlot = SQL_PLAYER)
    def AsyncQuery(self, c_pszQuery, iSlot = SQL_PLAYER):
        assert iSlot < SQL_MAX_NUM
        m_asyncSQL[iSlot].AsyncQuery(c_pszQuery)
        g_query_count[1] += 1

    def DirectQuery(self, c_pszQuery, iSlot = SQL_PLAYER):
        return m_directSQL[iSlot].DirectQuery(c_pszQuery)

    def PopResult(self):
        p = None

        LaniatusDefVariables = 0
        while LaniatusDefVariables < SQL_MAX_NUM:
            if m_mainSQL[LaniatusDefVariables] and m_mainSQL[LaniatusDefVariables].PopResult(p):
                return p
            LaniatusDefVariables += 1

        return None

    def PopResult(self, slot):
        p = None

        if m_mainSQL[slot] and m_mainSQL[slot].PopResult(p):
            return p

        return None

    def EscapeString(self, to, from_, length, iSlot = SQL_PLAYER):
        assert iSlot < SQL_MAX_NUM
        return mysql_real_escape_string(m_directSQL[iSlot].GetSQLHandle(), str(to), str(from_), length)

    def CountReturnQuery(self, i):
        return uint(m_mainSQL[LaniatusDefVariables].CountQuery() if m_mainSQL[LaniatusDefVariables] else 0)
    def CountReturnResult(self, i):
        return uint(m_mainSQL[LaniatusDefVariables].CountResult() if m_mainSQL[LaniatusDefVariables] else 0)
    def CountReturnQueryFinished(self, i):
        return uint(m_mainSQL[LaniatusDefVariables].CountQueryFinished() if m_mainSQL[LaniatusDefVariables] else 0)
    def CountReturnCopiedQuery(self, i):
        return uint(m_mainSQL[LaniatusDefVariables].GetCopiedQueryCount() if m_mainSQL[LaniatusDefVariables] else 0)
    def CountAsyncQuery(self, i):
        return uint(m_asyncSQL[LaniatusDefVariables].CountQuery() if m_asyncSQL[LaniatusDefVariables] else 0)
    def CountAsyncResult(self, i):
        return uint(m_asyncSQL[LaniatusDefVariables].CountResult() if m_asyncSQL[LaniatusDefVariables] else 0)
    def CountAsyncQueryFinished(self, i):
        return uint(m_asyncSQL[LaniatusDefVariables].CountQueryFinished() if m_asyncSQL[LaniatusDefVariables] else 0)
    def CountAsyncCopiedQuery(self, i):
        return uint(m_asyncSQL[LaniatusDefVariables].GetCopiedQueryCount() if m_asyncSQL[LaniatusDefVariables] else 0)

    def ResetCounter(self):
        LaniatusDefVariables = 0
        while LaniatusDefVariables < SQL_MAX_NUM:
            if m_mainSQL[LaniatusDefVariables]:
                m_mainSQL[LaniatusDefVariables].ResetQueryFinished()
                m_mainSQL[LaniatusDefVariables].ResetCopiedQueryCount()

            if m_asyncSQL[LaniatusDefVariables]:
                m_asyncSQL[LaniatusDefVariables].ResetQueryFinished()
                m_asyncSQL[LaniatusDefVariables].ResetCopiedQueryCount()
            LaniatusDefVariables += 1



    def SetLocale(self, szLocale):
        stLocale = szLocale
        sys_log(0, "SetLocale start")
        n = 0
        while n < SQL_MAX_NUM:
            m_mainSQL[n].SetLocale(stLocale)
            m_directSQL[n].SetLocale(stLocale)
            m_asyncSQL[n].SetLocale(stLocale)
            n += 1
        sys_log(0, "End setlocale %s", szLocale)

    def QueryLocaleSet(self):
        n = 0
        while n < SQL_MAX_NUM:
            m_mainSQL[n].QueryLocaleSet()
            m_directSQL[n].QueryLocaleSet()
            m_asyncSQL[n].QueryLocaleSet()
            n += 1


def ReturnQuery(c_pszQuery, iType, dwIdent, udata, iSlot):
    assert iSlot < SQL_MAX_NUM
    p = CQueryInfo()

    p.iType = iType
    p.dwIdent = dwIdent
    p.pvData = udata

    m_mainSQL[iSlot].ReturnQuery(c_pszQuery, p)

    g_query_count[0] += 1

