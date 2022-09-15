class quest: #this class replaces the original namespace 'quest'

    QUEST_START_STATE_INDEX = 0
    QUEST_CHAT_STATE_INDEX = -1
    QUEST_FISH_REFINE_STATE_INDEX = -2

## Laniatus Games Studio Inc. | NOTE: Python has no need of forward class declarations:
#    class PC

    class NPC:

        def __init__(self):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.m_vnum = 0
            self.m_mapOwnQuest = [None for _ in range(QUEST_EVENT_COUNT)]
            self.m_mapOwnArgQuest = [None for _ in range(QUEST_EVENT_COUNT)]

            self.m_vnum = 0

        def close(self):
            pass

        def Set(self, vnum, script_name):
            self.m_vnum = vnum

            buf = str(['\0' for _ in range(_MAX_PATH)])

            itEventName = CQuestManager.instance().m_mapEventName.begin()

            while itEventName is not CQuestManager.instance().m_mapEventName.end():
                it = itEventName
                itEventName += 1

                itObjectDir = g_setQuestObjectDir.begin()
                while itObjectDir is not g_setQuestObjectDir.end():
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                    is_ = snprintf(buf, sizeof(buf), "%s/%s/%s/", itObjectDir.c_str(), script_name, it.first.c_str())

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                    if is_ < 0 or is_ >= int(sizeof(buf)):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                        is_ = sizeof(buf) - 1

                    event_index = it.second

                    pdir = opendir(buf)

                    if pdir is None:
                        continue

                    pde = None

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: while ((pde = readdir(pdir)))
                    while (pde = readdir(pdir)):
                        if pde.d_name[0] == '.':
                            continue

                        if not _strnicmp(pde.d_name, "CVS", 3):
                            continue

                        #sys_log(1, "QUEST reading %s", pde.d_name)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                        strncpy_s(buf[is_:], sizeof(buf) - is_, pde.d_name, _TRUNCATE)
                        self.LoadStateScript(event_index, buf, pde.d_name)

                    closedir(pdir)
                    itObjectDir += 1

        @staticmethod
        def HasStartState(q):
            return 0 in q.keys()

        @staticmethod
        def HasStartState(q):
            return 0 in q.keys()

        def OnServerTimer(self, pc):
            return self.HandleReceiveAllEvent(pc, QUEST_SERVER_TIMER_EVENT)

        def OnClick(self, pc):
            return self.HandleEvent(pc, QUEST_CLICK_EVENT)

        def OnKill(self, pc):
            if self.m_vnum != 0:
                return self.HandleEvent(pc, QUEST_KILL_EVENT)
            else:
                return self.HandleReceiveAllEvent(pc, QUEST_KILL_EVENT)

        def OnPartyKill(self, pc):
            if self.m_vnum != 0:
                return self.HandleEvent(pc, QUEST_PARTY_KILL_EVENT)
            else:
                return self.HandleReceiveAllEvent(pc, QUEST_PARTY_KILL_EVENT)

        def OnTimer(self, pc):
            return self.HandleEvent(pc, QUEST_TIMER_EVENT)

        def OnLevelUp(self, pc):
            return self.HandleReceiveAllEvent(pc, QUEST_LEVELUP_EVENT)

        def OnLogin(self, pc, c_pszQuestName = None):
            bRet = self.HandleReceiveAllNoWaitEvent(pc, QUEST_LOGIN_EVENT)
            self.HandleReceiveAllEvent(pc, QUEST_LETTER_EVENT)
            return bRet

        def OnLogout(self, pc):
            return self.HandleReceiveAllEvent(pc, QUEST_LOGOUT_EVENT)

        def OnButton(self, pc, quest_index):
            EventIndex = QUEST_BUTTON_EVENT

            if pc.IsRunning():
                if test_server:
                    mgr = CQuestManager.instance()

                    #lani_err("QUEST There's suspended quest state, can't run new quest state (quest: %s pc: %s)", pc.GetCurrentQuestName(),mgr.GetCurrentCharacterPtr().GetName(LOCALE_LANIATUS) if mgr.GetCurrentCharacterPtr() is not None else "<none>")

                return LGEMiscellaneous.DEFINECONSTANTS.false

            itPCQuest = pc.quest_find(quest_index)

            rmapEventOwnQuest = self.m_mapOwnQuest[EventIndex]
            itQuestMap = rmapEventOwnQuest.find(quest_index)

            if itQuestMap == rmapEventOwnQuest.end():
                return LGEMiscellaneous.DEFINECONSTANTS.false

            iState = 0

            if itPCQuest is not pc.quest_end():
                iState = itPCQuest.second.st
            else:
                if CQuestManager.instance().CanStartQuest(itQuestMap.first, pc) and quest.NPC.HasStartState(itQuestMap.second):
                    iState = 0
                else:
                    return LGEMiscellaneous.DEFINECONSTANTS.false

            itQuestScript = itQuestMap.second.find(iState)

            if itQuestScript is itQuestMap.second.end():
                return LGEMiscellaneous.DEFINECONSTANTS.false

            CQuestManager.ExecuteQuestScript(pc, quest_index, iState, itQuestScript.second.GetCode(), itQuestScript.second.GetSize())
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        def OnInfo(self, pc, quest_index):
            EventIndex = QUEST_INFO_EVENT

            if pc.IsRunning():
                if test_server:
                    mgr = CQuestManager.instance()

                    #lani_err("QUEST There's suspended quest state, can't run new quest state (quest: %s pc: %s)", pc.GetCurrentQuestName(),mgr.GetCurrentCharacterPtr().GetName(LOCALE_LANIATUS) if mgr.GetCurrentCharacterPtr() is not None else "<none>")

                return LGEMiscellaneous.DEFINECONSTANTS.false

            itPCQuest = pc.quest_find(quest_index)

            if pc.quest_end() is itPCQuest:
                #lani_err("QUEST no quest by (quest %u)", quest_index)
                return LGEMiscellaneous.DEFINECONSTANTS.false

            rmapEventOwnQuest = self.m_mapOwnQuest[EventIndex]
            itQuestMap = rmapEventOwnQuest.find(quest_index)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to pointers to value types:
#ORIGINAL METINII C CODE: const char * questName = CQuestManager::instance().GetQuestNameByIndex(quest_index).c_str();
            questName = CQuestManager.instance().GetQuestNameByIndex(quest_index)

            if itQuestMap == rmapEventOwnQuest.end():
                #lani_err("QUEST no info event (quest %s)", questName)
                return LGEMiscellaneous.DEFINECONSTANTS.false

            itQuestScript = itQuestMap.second.find(itPCQuest.second.st)

            if itQuestScript is itQuestMap.second.end():
                #lani_err("QUEST no info script by state %d (quest %s)", itPCQuest.second.st, questName)
                return LGEMiscellaneous.DEFINECONSTANTS.false

            CQuestManager.ExecuteQuestScript(pc, quest_index, itPCQuest.second.st, itQuestScript.second.GetCode(), itQuestScript.second.GetSize())
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        def OnAttrIn(self, pc):
            return self.HandleEvent(pc, QUEST_ATTR_IN_EVENT)

        def OnAttrOut(self, pc):
            return self.HandleEvent(pc, QUEST_ATTR_OUT_EVENT)

        def OnUseItem(self, pc, bReceiveAll):
            if bReceiveAll:
                return self.HandleReceiveAllEvent(pc, QUEST_ITEM_USE_EVENT)
            else:
                return self.HandleEvent(pc, QUEST_ITEM_USE_EVENT)

        def OnTakeItem(self, pc):
            return self.HandleEvent(pc, QUEST_ITEM_TAKE_EVENT)

        def OnEnterState(self, pc, quest_index, state):
            return self.ExecuteEventScript(pc, QUEST_ENTER_STATE_EVENT, quest_index, state)

        def OnLeaveState(self, pc, quest_index, state):
            return self.ExecuteEventScript(pc, QUEST_LEAVE_STATE_EVENT, quest_index, state)

        def OnLetter(self, pc, quest_index, state):
            return self.ExecuteEventScript(pc, QUEST_LETTER_EVENT, quest_index, state)

        def OnChat(self, pc):
            if pc.IsRunning():
                if test_server:
                    mgr = CQuestManager.instance()

                    #lani_err("QUEST There's suspended quest state, can't run new quest state (quest: %s pc: %s)", pc.GetCurrentQuestName(),mgr.GetCurrentCharacterPtr().GetName(LOCALE_LANIATUS) if mgr.GetCurrentCharacterPtr() is not None else "<none>")

                return LGEMiscellaneous.DEFINECONSTANTS.false

            EventIndex = QUEST_CHAT_EVENT
            AvailScript = []

            fMatch = FuncMatchChatEvent(AvailScript)
            fMiss = FuncMissChatEvent(AvailScript)
            self.MatchingQuest(pc, self.m_mapOwnArgQuest[EventIndex], fMatch.functor_method, fMiss.functor_method)


            if not AvailScript:
                return LGEMiscellaneous.DEFINECONSTANTS.false

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if __MULTI_LANGUAGE_SYSTEM__
            bLocale = LaniatusLocalization.LOCALE_LANIATUS
            mgr = CQuestManager.instance()
            bLocale = mgr.GetCurrentCharacterPtr().GetDesc().GetLanguage()
##endif


                os = ostringstream()
                os << "select("
                os << '"' << ScriptToString(AvailScript[0].arg) << '"'
                i = 1
                while i < len(AvailScript):
                    os << ",\"" << ScriptToString(AvailScript[i].arg) << '"'
                    i += 1
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if __MULTI_LANGUAGE_SYSTEM__
                os << ", '" << LC_LOCALE_TEXT("Close", bLocale) << "'"
##else
                os << ", '"<<LC_TEXT("Close")<<"'"
##endif
                os << ")"

                CQuestManager.ExecuteQuestScript(pc, "QUEST_CHAT_TEMP_QUEST", 0, os.str().c_str(), len(os.str()), AvailScript, LGEMiscellaneous.DEFINECONSTANTS.false)

            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        def HasChat(self):
            return self.m_mapOwnArgQuest[QUEST_CHAT_EVENT]

        def OnItemInformer(self, pc, vnum):
            return self.HandleEvent(pc, QUEST_ITEM_INFORMER_EVENT)

        def OnTarget(self, pc, dwQuestIndex, c_pszTargetName, c_pszVerb, bRet):
            #sys_log(1, "OnTarget begin %s verb %s qi %u", c_pszTargetName, c_pszVerb, dwQuestIndex)

            bRet.arg_value = LGEMiscellaneous.DEFINECONSTANTS.false

            itPCQuest = pc.quest_find(dwQuestIndex)

            if itPCQuest is pc.quest_end():
                #sys_log(1, "no quest")
                return LGEMiscellaneous.DEFINECONSTANTS.false

            iState = itPCQuest.second.st

            r = self.m_mapOwnArgQuest[QUEST_TARGET_EVENT][dwQuestIndex]
            it = r.find(iState)

            if it == r.end():
                #sys_log(1, "no target event, state %d", iState)
                return LGEMiscellaneous.DEFINECONSTANTS.false

            it_vec = it.second.begin()

            iTargetLen = len(c_pszTargetName)

            while it_vec is not it.second.end():
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: AArgScript & argScript = *(it_vec++);
                argScript = *(it_vec)
                it_vec += 1
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to pointers to value types:
#ORIGINAL METINII C CODE: const char * c_pszArg = argScript.arg.c_str();
                c_pszArg = argScript.arg

                #sys_log(1, "OnTarget compare %s %d", c_pszArg, len(argScript.arg))

                if strncmp(c_pszArg, c_pszTargetName, iTargetLen):
                    continue

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Pointer arithmetic is detected on this variable:
#ORIGINAL METINII C CODE: const char * c_pszArgVerb = strchr(c_pszArg, '.');
                c_pszArgVerb = strchr(c_pszArg, '.')

                if (not c_pszArgVerb) != '\0':
                    continue

                c_pszArgVerb += 1
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: if (strcmp(++c_pszArgVerb, c_pszVerb))
                if strcmp(c_pszArgVerb, c_pszVerb):
                    continue

                if len(argScript.when_condition) > 0:
                    #sys_log(1, "OnTarget when %s size %d", argScript.when_condition[0], len(argScript.when_condition))

                if len(argScript.when_condition) != 0 and not IsScriptTrue(argScript.when_condition[0], len(argScript.when_condition)):
                    continue

                #sys_log(1, "OnTarget execute qi %u st %d code %s", dwQuestIndex, iState, str(argScript.script.GetCode()))
                bRet.arg_value = CQuestManager.ExecuteQuestScript(pc, dwQuestIndex, iState, argScript.script.GetCode(), argScript.script.GetSize(), NULL, ((not DefineConstants.false)))
                bRet.arg_value = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
                return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

            return LGEMiscellaneous.DEFINECONSTANTS.false

        def OnUnmount(self, pc):
            return self.HandleReceiveAllEvent(pc, QUEST_UNMOUNT_EVENT)

        def OnPickupItem(self, pc):
            if self.m_vnum == 0:
                return self.HandleReceiveAllEvent(pc, QUEST_ITEM_PICK_EVENT)
            else:
                return self.HandleEvent(pc, QUEST_ITEM_PICK_EVENT)

        def OnSIGUse(self, pc, bReceiveAll):
            if bReceiveAll:
                return self.HandleReceiveAllEvent(pc, QUEST_SIG_USE_EVENT)
            else:
                return self.HandleEvent(pc, QUEST_SIG_USE_EVENT)


        def HandleEvent(self, pc, EventIndex):
            if EventIndex < 0 or EventIndex >= QUEST_EVENT_COUNT:
                #lani_err("QUEST invalid EventIndex : %d", EventIndex)
                return LGEMiscellaneous.DEFINECONSTANTS.false

            if pc.IsRunning():
                if test_server:
                    mgr = CQuestManager.instance()

                    #lani_err("QUEST There's suspended quest state, can't run new quest state (quest: %s pc: %s)", pc.GetCurrentQuestName(),mgr.GetCurrentCharacterPtr().GetName(LOCALE_LANIATUS) if mgr.GetCurrentCharacterPtr() is not None else "<none>")

                return LGEMiscellaneous.DEFINECONSTANTS.false

            fMiss = FuncMissHandleEvent()
            fMatch = FuncMatchHandleEvent()
            self.MatchingQuest(pc, self.m_mapOwnQuest[EventIndex], fMatch.functor_method, fMiss.functor_method)

            r = LGEMiscellaneous.DEFINECONSTANTS.false
            if fMatch.Matched():
                i = 0
                while i < fMatch.size:
                    if i != 0:
                        pPC = CQuestManager.instance().GetPC(pc.GetID())

                    CQuestManager.ExecuteQuestScript(pc, list(fMatch.vdwQuesIndices[i]), list(fMatch.viPCStates[i]), list(fMatch.vcodes[i]), list(fMatch.vcode_sizes[i]), NULL, ((not DefineConstants.false)))
                    i += 1
                r = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
            if fMiss.Matched():
                rmapEventOwnQuest = self.m_mapOwnQuest[EventIndex]

                i = 0
                while i < fMiss.size:
                    script = rmapEventOwnQuest[fMiss.vdwNewStartQuestIndices[i]][0]
                    CQuestManager.ExecuteQuestScript(pc, list(fMiss.vdwNewStartQuestIndices[i]), 0, script.GetCode(), script.GetSize(), NULL, ((not DefineConstants.false)))
                    i += 1
                r = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
            else:
                return r
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        def HandleReceiveAllEvent(self, pc, EventIndex):
            if EventIndex < 0 or EventIndex >= QUEST_EVENT_COUNT:
                #lani_err("QUEST invalid EventIndex : %d", EventIndex)
                return LGEMiscellaneous.DEFINECONSTANTS.false

            if pc.IsRunning():
                if test_server:
                    mgr = CQuestManager.instance()

                    #lani_err("QUEST There's suspended quest state, can't run new quest state (quest: %s pc: %s)", pc.GetCurrentQuestName(),mgr.GetCurrentCharacterPtr().GetName(LOCALE_LANIATUS) if mgr.GetCurrentCharacterPtr() is not None else "<none>")

                return LGEMiscellaneous.DEFINECONSTANTS.false

            fMiss = FuncMissHandleReceiveAllEvent()
            fMatch = FuncMatchHandleReceiveAllEvent()

            self.MatchingQuest(pc, self.m_mapOwnQuest[EventIndex], fMatch.functor_method, fMiss.functor_method)
            return fMiss.bHandled or fMatch.bHandled

        def HandleReceiveAllNoWaitEvent(self, pc, EventIndex):
            if EventIndex<0 or EventIndex>=QUEST_EVENT_COUNT:
                #lani_err("QUEST invalid EventIndex : %d", EventIndex)
                return LGEMiscellaneous.DEFINECONSTANTS.false

            fMiss = FuncMissHandleReceiveAllNoWaitEvent()
            fMatch = FuncMatchHandleReceiveAllNoWaitEvent()

            rmapEventOwnQuest = self.m_mapOwnQuest[EventIndex]
            self.MatchingQuest(pc, rmapEventOwnQuest, fMatch.functor_method, fMiss.functor_method)

            return fMatch.bHandled or fMiss.bHandled

        def ExecuteEventScript(self, pc, EventIndex, dwQuestIndex, iState):
            rQuest = self.m_mapOwnQuest[EventIndex]

            itQuest = rQuest.find(dwQuestIndex)
            if itQuest == rQuest.end():
                #sys_log(0, "ExecuteEventScript ei %d qi %u is %d - NO QUEST", EventIndex, dwQuestIndex, iState)
                return LGEMiscellaneous.DEFINECONSTANTS.false

            rScript = itQuest.second
            itState = rScript.find(iState)
            if itState == rScript.end():
                #sys_log(0, "ExecuteEventScript ei %d qi %u is %d - NO STATE", EventIndex, dwQuestIndex, iState)
                return LGEMiscellaneous.DEFINECONSTANTS.false

            #sys_log(0, "ExecuteEventScript ei %d qi %u is %d", EventIndex, dwQuestIndex, iState)
            CQuestManager.instance().SetCurrentEventIndex(EventIndex)
            return CQuestManager.ExecuteQuestScript(pc, dwQuestIndex, iState, itState.second.GetCode(), itState.second.GetSize())

        def GetVnum(self):
            return self.m_vnum


        def MatchingQuest(self, pc, QuestMap, fMatch, fMiss):
            if test_server:
                #sys_log(0, "Click Quest : MatchingQuest")

            itPCQuest = pc.quest_begin()
            itQuestMap = QuestMap.begin()

            while itQuestMap is not QuestMap.end():
                if itPCQuest is pc.quest_end() or itPCQuest.first > itQuestMap.first:
                    fMiss(itPCQuest, itQuestMap)
                    itQuestMap += 1
                elif itPCQuest.first < itQuestMap.first:
                    itPCQuest += 1
                else:
                    fMatch(itPCQuest, itQuestMap)
                    itPCQuest += 1
                    itQuestMap += 1

        def LoadStateScript(self, event_index, filename, script_name):
            inf = ifstream(filename)
            s = script_name

            i = s.find('.')

            q = CQuestManager.instance()
            stQuestName = s[0:i]

            quest_index = int(q.GetQuestIndexByName(stQuestName))

            if quest_index == 0:
                fprintf(stderr, "cannot find quest index for %s\n", stQuestName)
                assert not "cannot find quest index"
                return

            stStateName = ""

            j = i
            i = s.find('.', i + 1)

            if i == s.npos:
                stStateName = s[j + 1:j + 1 + s.npos]
            else:
                stStateName = s[j + 1:j + 1 + i - j - 1]

            state_index = q.GetQuestStateIndex(stQuestName, stStateName)

            #sys_log(0, "QUEST loading %s : %s [STATE] %s", filename, stQuestName, stStateName)

            if i == s.npos:
                ib = istreambuf_iterator(inf)
                ie = istreambuf_iterator()
                copy(ib, ie, back_inserter(self.m_mapOwnQuest[event_index][quest_index][q.GetQuestStateIndex(stQuestName, stStateName)].m_code))
            else:
                j = i
                i = s.find('.', i + 1)

                if i == s.npos:
                    #lani_err("invalid QUEST STATE index [%s] [%s]",filename, script_name)
                    return

                index = strtol(s[j + 1:j + 1 + i - j - 1].c_str(), None, 10)
                j = i
                i = s.find('.', i + 1)

                if i != s.npos:
                    #lani_err("invalid QUEST STATE name [%s] [%s]",filename, script_name)
                    return

                type_name = s[j + 1:j + 1 + i - j - 1]

                ib = istreambuf_iterator(inf)
                ie = istreambuf_iterator()

                self.m_mapOwnArgQuest[event_index][quest_index][state_index].resize(MAX(index + 1, self.m_mapOwnArgQuest[event_index][quest_index][state_index].size()))

                if type_name == "when":
                    copy(ib, ie, back_inserter(self.m_mapOwnArgQuest[event_index][quest_index][state_index][index].when_condition))
                elif type_name == "arg":
                    s = ""
                    getline(inf, s)
                    self.m_mapOwnArgQuest[event_index][quest_index][state_index][index].arg.clear()

                    it = s.begin()
                    while it is not s.end():
                        self.m_mapOwnArgQuest[event_index][quest_index][state_index][index].arg+=*it
                        it += 1
                elif type_name == "script":
                    copy(ib, ie, back_inserter(self.m_mapOwnArgQuest[event_index][quest_index][state_index][index].script.m_code))
                    self.m_mapOwnArgQuest[event_index][quest_index][state_index][index].quest_index = quest_index
                    self.m_mapOwnArgQuest[event_index][quest_index][state_index][index].state_index = state_index


## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if __MULTI_LANGUAGE_SYSTEM__
##endif

class quest: #this class replaces the original namespace 'quest'

    class FuncMissHandleEvent:

        def __init__(self):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.vdwNewStartQuestIndices = []
            self.size = 0

            self.vdwNewStartQuestIndices = 0
            self.size = 0

        def Matched(self):
            return len(self.vdwNewStartQuestIndices) != 0

        def functor_method(self, itPCQuest, itQuestMap):
            dwQuestIndex = itQuestMap.first

            if NPC.HasStartState(itQuestMap.second) and CQuestManager.instance().CanStartQuest(dwQuestIndex):
                self.size += 1
                self.vdwNewStartQuestIndices.append(dwQuestIndex)

    class FuncMatchHandleEvent:


        def __init__(self):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.bMatched = False
            self.vdwQuesIndices = []
            self.viPCStates = []
            self.vcodes = []
            self.vcode_sizes = []
            self.size = 0

            self.bMatched = LGEMiscellaneous.DEFINECONSTANTS.false
            self.vdwQuesIndices = 0
            self.viPCStates = 0
            self.vcodes = 0
            self.vcode_sizes = 0
            self.size = 0

        def Matched(self):
            return self.bMatched

        def functor_method(self, itPCQuest, itQuestMap):
            itQuestScript = None

            iState = itPCQuest.second.st
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((itQuestScript = itQuestMap->second.find(iState)) != itQuestMap->second.end())
            if (itQuestScript = itQuestMap.second.find(iState)) is not itQuestMap.second.end():
                self.bMatched = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
                self.size += 1
                self.vdwQuesIndices.append(itQuestMap.first)
                self.viPCStates.append(iState)
                self.vcodes.append(itQuestScript.second.GetCode())
                self.vcode_sizes.append(itQuestScript.second.GetSize())

    class FuncMissHandleReceiveAllEvent:

        def __init__(self):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.bHandled = False

            self.bHandled = LGEMiscellaneous.DEFINECONSTANTS.false

        def functor_method(self, itPCQuest, itQuestMap):
            dwQuestIndex = itQuestMap.first

            if NPC.HasStartState(itQuestMap.second) and CQuestManager.instance().CanStartQuest(dwQuestIndex):
                QuestScript = itQuestMap.second
                it = QuestScript.find(QUEST_START_STATE_INDEX)

                if it is not QuestScript.end():
                    self.bHandled = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
                    CQuestManager.ExecuteQuestScript(CQuestManager.instance().GetCurrentPC(), dwQuestIndex, QUEST_START_STATE_INDEX, it.second.GetCode(), it.second.GetSize())

    class FuncMatchHandleReceiveAllEvent:

        def __init__(self):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.bHandled = False

            self.bHandled = LGEMiscellaneous.DEFINECONSTANTS.false

        def functor_method(self, itPCQuest, itQuestMap):
            QuestScript = itQuestMap.second
            iPCState = itPCQuest.second.st
            itQuestScript = QuestScript.find(iPCState)

            if itQuestScript is not QuestScript.end():
                self.bHandled = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

                CQuestManager.ExecuteQuestScript(CQuestManager.instance().GetCurrentPC(), itQuestMap.first, iPCState, itQuestScript.second.GetCode(), itQuestScript.second.GetSize())

    class FuncDoNothing:
        def functor_method(self, itPCQuest, itQuestMap):
            pass

    class FuncMissHandleReceiveAllNoWaitEvent:

        def __init__(self):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.bHandled = False

            self.bHandled = LGEMiscellaneous.DEFINECONSTANTS.false


        def functor_method(self, itPCQuest, itQuestMap):
            dwQuestIndex = itQuestMap.first

            if NPC.HasStartState(itQuestMap.second) and CQuestManager.instance().CanStartQuest(dwQuestIndex):
                QuestScript = itQuestMap.second
                it = QuestScript.find(QUEST_START_STATE_INDEX)
                if it is not QuestScript.end():
                    self.bHandled = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
                    pPC = CQuestManager.instance().GetCurrentPC()
                    if CQuestManager.ExecuteQuestScript(pPC, dwQuestIndex, QUEST_START_STATE_INDEX, it.second.GetCode(), it.second.GetSize()):
                        #lani_err("QUEST NOT END RUNNING on Login/Logout - %s", CQuestManager.instance().GetQuestNameByIndex(itQuestMap.first))

                        rqs = pPC.GetRunningQuestState()
                        CQuestManager.instance().CloseState(rqs)
                        pPC.EndRunning()

    class FuncMatchHandleReceiveAllNoWaitEvent:

        def __init__(self):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.bHandled = False

            self.bHandled = LGEMiscellaneous.DEFINECONSTANTS.false

        def functor_method(self, itPCQuest, itQuestMap):
            QuestScript = itQuestMap.second
            iPCState = itPCQuest.second.st
            itQuestScript = QuestScript.find(iPCState)

            if itQuestScript is not QuestScript.end():
                pPC = CQuestManager.instance().GetCurrentPC()

                if CQuestManager.ExecuteQuestScript(pPC, itQuestMap.first, iPCState, itQuestScript.second.GetCode(), itQuestScript.second.GetSize()):
                    #lani_err("QUEST NOT END RUNNING on Login/Logout - %s", CQuestManager.instance().GetQuestNameByIndex(itQuestMap.first))

                    rqs = pPC.GetRunningQuestState()
                    CQuestManager.instance().CloseState(rqs)
                    pPC.EndRunning()
                self.bHandled = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    class FuncMissChatEvent:
        def __init__(self, rAvailScript):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.rAvailScript = None

            self.rAvailScript = rAvailScript

        def functor_method(self, itPCQuest, itQuestMap):
            if CQuestManager.instance().CanStartQuest(itQuestMap.first) and NPC.HasStartState(itQuestMap.second):
                i = None
                i = 0
                while i < itQuestMap.second[QUEST_START_STATE_INDEX].size():
                    if itQuestMap.second[QUEST_START_STATE_INDEX][i].when_condition.size() == 0 or IsScriptTrue(itQuestMap.second[QUEST_START_STATE_INDEX][i].when_condition[0], itQuestMap.second[QUEST_START_STATE_INDEX][i].when_condition.size()):
                        self.rAvailScript.append(itQuestMap.second[QUEST_START_STATE_INDEX][i])
                    i += 1


    class FuncMatchChatEvent:
        def __init__(self, rAvailScript):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.rAvailScript = None

            self.rAvailScript = rAvailScript

        def functor_method(self, itPCQuest, itQuestMap):
            iState = itPCQuest.second.st
            itQuestScript = itQuestMap.second.find(iState)
            if itQuestScript is not itQuestMap.second.end():
                i = None
                i = 0
                while i < itQuestMap.second[iState].size():
                    if itQuestMap.second[iState][i].when_condition.size() == 0 or IsScriptTrue(itQuestMap.second[iState][i].when_condition[0], itQuestMap.second[iState][i].when_condition.size()):
                        self.rAvailScript.append(itQuestMap.second[iState][i])
                    i += 1

