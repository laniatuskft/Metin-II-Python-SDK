from enum import Enum

class ETargetTypes(Enum):
    TARGET_TYPE_POS = (1 << 0)
    TARGET_TYPE_VID = (1 << 1)

class TargetInfo(event_info_data):

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.iID = 0
        self.dwPID = 0
        self.dwQuestIndex = 0
        self.szTargetName = str(['\0' for _ in range(32+1)])
        self.szTargetDesc = str(['\0' for _ in range(32+1)])
        self.iType = 0
        self.iArg1 = 0
        self.iArg2 = 0
        self.iMapIndex = 0
        self.iOldX = 0
        self.iOldY = 0
        self.bSendToClient = False

        self.iID = 0
        self.dwPID = 0
        self.dwQuestIndex = 0
        self.iType = 0
        self.iArg1 = 0
        self.iArg2 = 0
        self.iMapIndex = 0
        self.iOldX = 0
        self.iOldY = 0
        self.bSendToClient = LGEMiscellaneous.DEFINECONSTANTS.false
        memset(self.szTargetName, 0, 32+1)
        memset(self.szTargetDesc, 0, 32+1)

class CTargetManager(singleton):
    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.m_map_kListEvent = {}
        self.m_iID = 0

        self.m_iID = 0

    def close(self):
        pass

    def CreateTarget(self, dwPID, dwQuestIndex, c_pszTargetName, iType, iArg1, iArg2, iMapIndex, c_pszTargetDesc = None, iSendFlag = 1):
        #sys_log(0, "CreateTarget : target pid %u quest %u name %s arg %d %d %d", dwPID, dwQuestIndex, c_pszTargetName, iType, iArg1, iArg2)

        pkChr = CHARACTER_MANAGER.instance().FindByPID(dwPID)

        if pkChr is None:
            #lani_err("Cannot find character ptr by PID %u", dwPID)
            return

        if pkChr.GetMapIndex() != iMapIndex:
            return

        it = self.m_map_kListEvent.find(dwPID)

        if it is not self.m_map_kListEvent.end():
            it2 = it.second.begin()

            while it2 is not it.second.end():
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: _boost_func_of_void::intrusive_ptr<struct event> pkEvent = *(it2++);
                pkEvent = *(it2)
                it2 += 1
                existInfo = if isinstance(pkEvent.info, TargetInfo) else None

                if None is existInfo:
                    #lani_err("CreateTarget : event already exist, but have no info")
                    return

                if existInfo.dwQuestIndex == dwQuestIndex and not strcmp(existInfo.szTargetName, c_pszTargetName):
                    #sys_log(0, "CreateTarget : same target will be replaced")

                    if existInfo.bSendToClient:
                        Globals.SendTargetDeletePacket(pkChr.GetDesc(), existInfo.iID)

                    if c_pszTargetDesc != '\0':
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                        strncpy_s(existInfo.szTargetDesc, sizeof(existInfo.szTargetDesc), c_pszTargetDesc, _TRUNCATE)
                    else:
                        existInfo.szTargetDesc[0] = '\0'

                    self.m_iID += 1
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: existInfo->iID = ++m_iID;
                    existInfo.iID = self.m_iID
                    existInfo.iType = iType
                    existInfo.iArg1 = iArg1
                    existInfo.iArg2 = iArg2
                    existInfo.iOldX = 0
                    existInfo.iOldY = 0
                    existInfo.bSendToClient = ((not LGEMiscellaneous.DEFINECONSTANTS.false)) if iSendFlag != 0 else LGEMiscellaneous.DEFINECONSTANTS.false

                    Globals.SendTargetCreatePacket(pkChr.GetDesc(), existInfo)
                    return

        newInfo = Globals.AllocEventInfo()

        if c_pszTargetDesc != '\0':
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            strncpy_s(newInfo.szTargetDesc, sizeof(newInfo.szTargetDesc), c_pszTargetDesc, _TRUNCATE)
        else:
            newInfo.szTargetDesc[0] = '\0'

        self.m_iID += 1
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: newInfo->iID = ++m_iID;
        newInfo.iID = self.m_iID
        newInfo.dwPID = dwPID
        newInfo.dwQuestIndex = dwQuestIndex
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        strncpy_s(newInfo.szTargetName, sizeof(newInfo.szTargetName), c_pszTargetName, _TRUNCATE)
        newInfo.iType = iType
        newInfo.iArg1 = iArg1
        newInfo.iArg2 = iArg2
        newInfo.iMapIndex = iMapIndex
        newInfo.iOldX = 0
        newInfo.iOldY = 0
        newInfo.bSendToClient = ((not LGEMiscellaneous.DEFINECONSTANTS.false)) if iSendFlag != 0 else LGEMiscellaneous.DEFINECONSTANTS.false

        event = event_create_ex(target_event, newInfo, ((1) * passes_per_sec))

        if None is not event:
            self.m_map_kListEvent[dwPID].push_back(event)

            Globals.SendTargetCreatePacket(pkChr.GetDesc(), newInfo)

    def DeleteTarget(self, dwPID, dwQuestIndex, c_pszTargetName):
        it = self.m_map_kListEvent.find(dwPID)

        if it is self.m_map_kListEvent.end():
            return

        it2 = it.second.begin()

        while it2 is not it.second.end():
            pkEvent = *it2
            info = if isinstance(pkEvent.info, TargetInfo) else None

            if info is None:
                #lani_err("CTargetManager::DeleteTarget> <Factor> Null pointer")
                it2 += 1
                continue

            if dwQuestIndex == info.dwQuestIndex:
                if (not c_pszTargetName) != '\0' or not strcmp(info.szTargetName, c_pszTargetName):
                    if info.bSendToClient:
                        pkChr = CHARACTER_MANAGER.instance().FindByPID(info.dwPID)
                        if pkChr is not None:
                            Globals.SendTargetDeletePacket(pkChr.GetDesc(), info.iID)

                    event_cancel(pkEvent)
                    it2 = it.second.erase(it2)
                    continue

            it2 += 1

    def Logout(self, dwPID):
        it = self.m_map_kListEvent.find(dwPID)

        if it is self.m_map_kListEvent.end():
            return

        it2 = it.second.begin()

        while it2 is not it.second.end():
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: event_cancel(&(*(it2++)));
            event_cancel((*(it2)))
            it2 += 1

        self.m_map_kListEvent.pop(it)

    def GetTargetInfo(self, dwPID, iType, iArg1):
        it = self.m_map_kListEvent.find(dwPID)

        if it is self.m_map_kListEvent.end():
            return None

        it2 = it.second.begin()

        while it2 is not it.second.end():
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: _boost_func_of_void::intrusive_ptr<struct event> pkEvent = *(it2++);
            pkEvent = *(it2)
            it2 += 1
            info = if isinstance(pkEvent.info, TargetInfo) else None

            if info is None:
                #lani_err("CTargetManager::GetTargetInfo> <Factor> Null pointer")

                continue

            ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'IS_SET' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
            if not IS_SET(info.iType, iType):
                continue

            if info.iArg1 != iArg1:
                continue

            return info

        return None

    def GetTargetEvent(self, dwPID, dwQuestIndex, c_pszTargetName):
        it = self.m_map_kListEvent.find(dwPID)

        if it is self.m_map_kListEvent.end():
            return None

        it2 = it.second.begin()

        while it2 is not it.second.end():
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: _boost_func_of_void::intrusive_ptr<struct event> pkEvent = *(it2++);
            pkEvent = *(it2)
            it2 += 1
            info = if isinstance(pkEvent.info, TargetInfo) else None

            if info is None:
                #lani_err("CTargetManager::GetTargetEvent> <Factor> Null pointer")

                continue

            if info.dwQuestIndex != dwQuestIndex:
                continue

            if strcmp(info.szTargetName, c_pszTargetName):
                continue

            return _boost_func_of_void.intrusive_ptr(pkEvent)

        return None
