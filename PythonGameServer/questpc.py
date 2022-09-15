from enum import Enum

## Laniatus Games Studio Inc. | NOTE: Python has no need of forward class declarations:
#class CHARACTER

class quest: #this class replaces the original namespace 'quest'

    class RewardData:
        class RewardType(Enum):
            REWARD_TYPE_NONE = 0
            REWARD_TYPE_EXP = 1
            REWARD_TYPE_ITEM = 2


        def __init__(self, t, value1, value2 = 0):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.type = 0
            self.value1 = 0
            self.value2 = 0

            self.type = quest.RewardData.RewardType(t)
            self.value1 = value1
            self.value2 = value2

    class PC:


        def __init__(self):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.QUEST_SEND_ISBEGIN = (1 << 0)
            self.QUEST_SEND_TITLE = (1 << 1)
            self.QUEST_SEND_CLOCK_NAME = (1 << 2)
            self.QUEST_SEND_CLOCK_VALUE = (1 << 3)
            self.QUEST_SEND_COUNTER_NAME = (1 << 4)
            self.QUEST_SEND_COUNTER_VALUE = (1 << 5)
            self.QUEST_SEND_ICON_FILE = (1 << 6)
            self._m_QuestStateChange = []
            self._m_vRewardData = []
            self._m_bIsGivenReward = False
            self._m_bShouldSendDone = False
            self._m_dwID = 0
            self._m_QuestInfo = {}
            self._m_RunningQuestState = None
            self._m_stCurQuest = ""
            self._m_FlagMap = {}
            self._m_FlagSaveMap = {}
            self._m_TimerMap = {}
            self._m_iSendToClient = 0
            self._m_bLoaded = False
            self._m_iLastState = 0
            self._m_dwWaitConfirmFromPID = 0
            self._m_bConfirmWait = False

            self._m_bIsGivenReward = LGEMiscellaneous.DEFINECONSTANTS.false
            self._m_bShouldSendDone = LGEMiscellaneous.DEFINECONSTANTS.false
            self._m_dwID = 0
            self._m_RunningQuestState = None
            self._m_iSendToClient = 0
            self._m_bLoaded = LGEMiscellaneous.DEFINECONSTANTS.false
            self._m_iLastState = 0
            self._m_dwWaitConfirmFromPID = 0
            self._m_bConfirmWait = LGEMiscellaneous.DEFINECONSTANTS.false

        def close(self):
            self.Destroy()

        def Destroy(self):
            self.ClearTimer()

        def SetID(self, dwID):
            self._m_dwID = dwID
            self._m_bShouldSendDone = LGEMiscellaneous.DEFINECONSTANTS.false

        def GetID(self):
            return self._m_dwID

        def HasQuest(self, quest_name):
            qi = CQuestManager.instance().GetQuestIndexByName(quest_name)
            return qi in self._m_QuestInfo.keys()

        def GetQuest(self, quest_name):
            qi = CQuestManager.instance().GetQuestIndexByName(quest_name)
            return self._m_QuestInfo[qi]

        def quest_begin(self):
            return self._m_QuestInfo.begin()

        def quest_end(self):
            return self._m_QuestInfo.end()

        def quest_find(self, quest_index):
            return self._m_QuestInfo.find(quest_index)

        def IsRunning(self):
            return self._m_RunningQuestState is not None

        def EndRunning(self):
                npc = CQuestManager.instance().GetCurrentNPCCharacterPtr()
                ch = CQuestManager.instance().GetCurrentCharacterPtr()
                if npc is not None and not npc.IsPC():
                    if ch.GetPlayerID() == npc.GetQuestNPCID():
                        npc.SetQuestNPCID(0)
                        #sys_log(0, "QUEST NPC lock isn't unlocked : pid %u", ch.GetPlayerID())
                        CQuestManager.instance().WriteRunningStateToSyserr()

            if self.HasReward():
                self.Save()

                ch = CQuestManager.instance().GetCurrentCharacterPtr()
                if ch is not None:
                    self.Reward(ch)
                    ch.Save()
            self._m_bIsGivenReward = LGEMiscellaneous.DEFINECONSTANTS.false

            if self._m_iSendToClient != 0:
                #sys_log(1, "QUEST end running %d", self._m_iSendToClient)
                self._SendQuestInfoPakcet()

            if self._m_RunningQuestState is None:
                #sys_log(0, "Entered PC::EndRunning() with invalid running quest state")
                return
            pOldState = self._m_RunningQuestState
            iNowState = self._m_RunningQuestState.st

            self._m_RunningQuestState = None

            if self._m_iLastState != iNowState:
                ch = CQuestManager.instance().GetCurrentCharacterPtr()
                dwQuestIndex = CQuestManager.instance().GetQuestIndexByName(self._m_stCurQuest)
                if ch:
                    self.SetFlag(self._m_stCurQuest + ".__status", self._m_iLastState, DefineConstants.false)
                    CQuestManager.instance().LeaveState(ch.GetPlayerID(), dwQuestIndex, self._m_iLastState)
                    pOldState.st = iNowState
                    self.SetFlag(self._m_stCurQuest + ".__status", iNowState, DefineConstants.false)
                    CQuestManager.instance().EnterState(ch.GetPlayerID(), dwQuestIndex, iNowState)
                    if self.GetFlag(self._m_stCurQuest + ".__status") == iNowState:
                        CQuestManager.instance().Letter(ch.GetPlayerID(), dwQuestIndex, iNowState)


            self._DoQuestStateChange()

        def CancelRunning(self):
            self._m_RunningQuestState = None
            self._m_iSendToClient = 0
            self._m_bShouldSendDone = LGEMiscellaneous.DEFINECONSTANTS.false

        def GetRunningQuestState(self):
            return self._m_RunningQuestState

        def SetQuest(self, quest_name, qs):
            qi = CQuestManager.instance().GetQuestIndexByName(quest_name)
            it = self._m_QuestInfo.find(qi)

            if it is self._m_QuestInfo.end():
                self._m_QuestInfo.update({qi: qs})
            else:
                it.second = qs

            self._m_stCurQuest = quest_name
            self._m_RunningQuestState = self._m_QuestInfo[qi]
            self._m_iSendToClient = 0

            self._m_iLastState = qs.st
            self.SetFlag(quest_name + ".__status", qs.st, DefineConstants.false)

            self._m_RunningQuestState.iIndex = int(qi)
            self._m_bShouldSendDone = LGEMiscellaneous.DEFINECONSTANTS.false

        def SetCurrentQuestStateName(self, state_name):
            self.SetFlag(self._m_stCurQuest + ".__status", CQuestManager.Instance().GetQuestStateIndex(self._m_stCurQuest, state_name), DefineConstants.false)

        def SetQuestState(self, quest_name, state_name):
            self.SetQuestState(quest_name, CQuestManager.Instance().GetQuestStateIndex(quest_name, state_name))

        def SetQuestState(self, quest_name, new_state_index):
            iNowState = self.GetFlag(quest_name + ".__status")

            if iNowState != new_state_index:
                self._AddQuestStateChange(quest_name, iNowState, new_state_index)

        def ClearQuest(self, quest_name):
            quest_name_with_dot = quest_name + '.'
            it = m_FlagMap.begin()
            while it is not self._m_FlagMap.end():
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: auto itNow = it++;
                itNow = it
                it += 1
                if itNow.second != 0 and itNow.first.compare(0, len(quest_name_with_dot), quest_name_with_dot) == 0:
                    self.SetFlag(itNow.first, 0, DefineConstants.false)

            self.ClearTimer()

            it = self.quest_begin()
            questindex = quest.CQuestManager.instance().GetQuestIndexByName(quest_name)

            while it is not self.quest_end():
                if it.first == questindex:
                    it.second.st = 0
                    break

                it += 1

        def _AddQuestStateChange(self, quest_name, prev_state, next_state):
            dwQuestIndex = CQuestManager.instance().GetQuestIndexByName(quest_name)
            #sys_log(0, "QUEST reserve Quest State Change quest %s[%u] from %d to %d", quest_name, dwQuestIndex, prev_state, next_state)
            self._m_QuestStateChange.append(TQuestStateChangeInfo(dwQuestIndex, prev_state, next_state))

        def _DoQuestStateChange(self):
            ch = CQuestManager.instance().GetCurrentCharacterPtr()

            vecQuestStateChange = []
            self._m_QuestStateChange.swap(vecQuestStateChange)

            i = 0
            while i<len(vecQuestStateChange):
                rInfo = vecQuestStateChange[i]
                if rInfo.quest_idx == 0:
                    continue

                dwQuestIdx = rInfo.quest_idx
                it = self.quest_find(dwQuestIdx)
                stQuestName = CQuestManager.instance().GetQuestNameByIndex(dwQuestIdx)

                if it is self.quest_end():
                    qs = QuestState()
                    qs.st = 0

                    self._m_QuestInfo.update({dwQuestIdx: qs})
                    self.SetFlag(stQuestName + ".__status", 0, DefineConstants.false)

## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: it = quest_find(dwQuestIdx);
                    it.copy_from(self.quest_find(dwQuestIdx))

                #sys_log(0, "QUEST change reserved Quest State Change quest %u from %d to %d (%d %d)", dwQuestIdx, rInfo.prev_state, rInfo.next_state, it.second.st, rInfo.prev_state)

                assert it.second.st == rInfo.prev_state

                CQuestManager.instance().LeaveState(ch.GetPlayerID(), dwQuestIdx, rInfo.prev_state)
                it.second.st = rInfo.next_state
                self.SetFlag(stQuestName + ".__status", rInfo.next_state, DefineConstants.false)

                CQuestManager.instance().EnterState(ch.GetPlayerID(), dwQuestIdx, rInfo.next_state)

                if self.GetFlag(stQuestName + ".__status") == rInfo.next_state:
                    CQuestManager.instance().Letter(ch.GetPlayerID(), dwQuestIdx, rInfo.next_state)
                i += 1

        class TQuestStateChangeInfo:

            def __init__(self, _quest_idx, _prev_state, _next_state):
                #instance fields found by # Laniatus Games Studio Inc. |:
                self.quest_idx = 0
                self.prev_state = 0
                self.next_state = 0

                self.quest_idx = _quest_idx
                self.prev_state = _prev_state
                self.next_state = _next_state


        def SetFlag(self, name, value, bSkipSave = LGEMiscellaneous.DefineConstants.false):
            if test_server:
                #sys_log(0, "QUEST Setting flag %s %d", name,value)
            else:
                #sys_log(1, "QUEST Setting flag %s %d", name,value)

            if value == 0:
                self.DeleteFlag(name)
                return

            it = self._m_FlagMap.find(name)

            if it is self._m_FlagMap.end():
                self._m_FlagMap.update({name: value})
            elif it.second != value:
                it.second = value
            else:
                bSkipSave = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

            if not bSkipSave:
                self._SaveFlag(name, value)

        def GetFlag(self, name):
            it = self._m_FlagMap.find(name)

            if it is not self._m_FlagMap.end():
                #sys_log(1, "QUEST getting flag %s %d", name,it.second)
                return it.second
            return 0

        def DeleteFlag(self, name):
            it = self._m_FlagMap.find(name)

            if it is not self._m_FlagMap.end():
                self._m_FlagMap.pop(it)
                self._SaveFlag(name, 0)
                return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

            return LGEMiscellaneous.DEFINECONSTANTS.false

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: const str & GetCurrentQuestName() const
        def GetCurrentQuestName(self):
            return self._m_stCurQuest

        def GetCurrentQuestIndex(self):
            return int(CQuestManager.instance().GetQuestIndexByName(self.GetCurrentQuestName()))

        def RemoveTimer(self, name):
            it = self._m_TimerMap.find(name)

            if it is not self._m_TimerMap.end():
                #sys_log(0, "QUEST remove timer %p", Globals.get_pointer(it.second))
                CancelTimerEvent(it.second)
                self._m_TimerMap.pop(it)

            #sys_log(1, "QUEST timer map size %d by RemoveTimer", len(self._m_TimerMap))

        def RemoveTimerNotCancel(self, name):
            it = self._m_TimerMap.find(name)

            if it is not self._m_TimerMap.end():
                #sys_log(0, "QUEST remove with no cancel %p", Globals.get_pointer(it.second))
                self._m_TimerMap.pop(it)

            #sys_log(1, "QUEST timer map size %d by RemoveTimerNotCancel", len(self._m_TimerMap))

        def AddTimer(self, name, pEvent):
            self.RemoveTimer(name)
            self._m_TimerMap.update({name: pEvent})
            #sys_log(0, "QUEST add timer %p %d", Globals.get_pointer(pEvent), len(self._m_TimerMap))

        def ClearTimer(self):
            #sys_log(0, "QUEST clear timer %d", len(self._m_TimerMap))
            it = self._m_TimerMap.begin()

            while it is not self._m_TimerMap.end():
                CancelTimerEvent(it.second)
                it += 1

            self._m_TimerMap.clear()

        def SetCurrentQuestStartFlag(self):
            if self._GetCurrentQuestBeginFlag() == 0:
                self._SetCurrentQuestBeginFlag()

        def SetCurrentQuestDoneFlag(self):
            if self._GetCurrentQuestBeginFlag() != 0:
                self._ClearCurrentQuestBeginFlag()

        def SetQuestTitle(self, quest, title):
            it = self._m_QuestInfo.find(CQuestManager.instance().GetQuestIndexByName(quest))

            if it is not self._m_QuestInfo.end():
                old = self._m_RunningQuestState
                old2 = self._m_iSendToClient
                oldquestname = self._m_stCurQuest
                self._m_stCurQuest = quest
                self._m_RunningQuestState = it.second
                self._m_iSendToClient = self.QUEST_SEND_TITLE
                self._m_RunningQuestState.iIndex = self._GetCurrentQuestBeginFlag()

                self.SetCurrentQuestTitle(title)

                self._SendQuestInfoPakcet()

                self._m_stCurQuest = oldquestname
                self._m_RunningQuestState = old
                self._m_iSendToClient = old2

        def SetCurrentQuestTitle(self, title):
            self._SetSendFlag(self.QUEST_SEND_TITLE)
            self._m_RunningQuestState._title = title

        def SetCurrentQuestClockName(self, name):
            self._SetSendFlag(self.QUEST_SEND_CLOCK_NAME)
            self._m_RunningQuestState._clock_name = name

        def SetCurrentQuestClockValue(self, value):
            self._SetSendFlag(self.QUEST_SEND_CLOCK_VALUE)
            self._m_RunningQuestState._clock_value = value

        def SetCurrentQuestCounterName(self, name):
            self._SetSendFlag(self.QUEST_SEND_COUNTER_NAME)
            self._m_RunningQuestState._counter_name = name

        def SetCurrentQuestCounterValue(self, value):
            self._SetSendFlag(self.QUEST_SEND_COUNTER_VALUE)
            self._m_RunningQuestState._counter_value = value

        def SetCurrentQuestIconFile(self, icon_file):
            self._SetSendFlag(self.QUEST_SEND_ICON_FILE)
            self._m_RunningQuestState._icon_file = icon_file

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: bool IsLoaded() const
        def IsLoaded(self):
            return self._m_bLoaded
        def SetLoaded(self):
            self._m_bLoaded = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
        def Build(self):
            it = m_FlagMap.begin()
            while it is not self._m_FlagMap.end():
                if it.first.size()>9 and it.first.compare(it.first.size()-9,9, ".__status") == 0:
                    dwQuestIndex = CQuestManager.instance().GetQuestIndexByName(it.first.substr(0, it.first.size()-9))
                    state = it.second
                    qs = QuestState()
                    qs.st = state

                    self._m_QuestInfo.update({dwQuestIndex: qs})
                it += 1

        ## Laniatus Games Studio Inc. | NOTE: This was formerly a static local variable declaration (not allowed in Python):

        def Save(self):
            if not self._m_FlagSaveMap:
                return

            ## Laniatus Games Studio Inc. | NOTE: This static local variable declaration (not allowed in Python) has been moved just prior to the method:
            #            static list<SQuestTable> s_table
            Save_s_table.resize(len(self._m_FlagSaveMap))

            i = 0

            it = self._m_FlagSaveMap.begin()

            while it is not self._m_FlagSaveMap.end():
                stComp = it.first
                lValue = it.second

                it += 1

                iPos = stComp.find(".")

                if iPos < 0:
                    #lani_err("quest::PC::Save : cannot find . in FlagMap")
                    continue

                stName = ""
                stName.assign(stComp, 0, iPos)

                stState = ""
                stState.assign(stComp, iPos + 1, len(stComp))

                if len(stName) == 0 or len(stState) == 0:
                    #lani_err("quest::PC::Save : invalid quest data: %s", stComp)
                    continue

                #sys_log(1, "QUEST Save Flag %s, %s %d (%d)", stName, stState, lValue, i)

                if len(stName) >= LGEMiscellaneous.DEFINECONSTANTS.QUEST_NAME_MAX_LEN:
                    #lani_err("quest::PC::Save : quest name overflow")
                    continue

                if len(stState) >= LGEMiscellaneous.DEFINECONSTANTS.QUEST_STATE_MAX_LEN:
                    #lani_err("quest::PC::Save : quest state overflow")
                    continue

## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: SQuestTable & r = s_table[i++];
                r = Save_s_table[i]
                i += 1

                r.dwPID = self._m_dwID
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                strncpy_s(r.szName, sizeof(r.szName), stName, _TRUNCATE)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                strncpy_s(r.szState, sizeof(r.szState), stState, _TRUNCATE)
                r.lValue = lValue

            if i > 0:
                #sys_log(1, "QuestPC::Save %d", i)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                db_clientdesc.DBPacketHeader(Globals.LG_HEADER_GD_QUEST_SAVE, 0, sizeof(SQuestTable) * i)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                db_clientdesc.Packet(Save_s_table[0], sizeof(SQuestTable) * i)

            self._m_FlagSaveMap.clear()

        def HasReward(self):
            return self._m_vRewardData or self._m_bIsGivenReward
        def Reward(self, ch):
            if self._m_bIsGivenReward:
                ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Quest> The reward was given out, you are too late."))
                self._m_bIsGivenReward = LGEMiscellaneous.DEFINECONSTANTS.false

            for it in self._m_vRewardData:
                if it.type == RewardData.REWARD_TYPE_EXP:
                    #sys_log(0, "EXP cur %d add %d next %d",ch.GetExp(), it.value1, ch.GetNextExp())

                    if ch.GetExp() + it.value1 > ch.GetNextExp():
                        ch.PointChange(EPointTypes.LG_POINT_EXP, ch.GetNextExp() - 1 - ch.GetExp(), DefineConstants.false, DefineConstants.false)
                    else:
                        ch.PointChange(EPointTypes.LG_POINT_EXP, it.value1, DefineConstants.false, DefineConstants.false)


                elif it.type == RewardData.REWARD_TYPE_ITEM:
                    ch.AutoGiveItem(it.value1, it.value2)

                else:
                    #lani_err("Invalid RewardData type")

            self._m_vRewardData.clear()

        def GiveItem(self, label, dwVnum, count):
            #sys_log(1, "QUEST GiveItem %s %d %d", label,dwVnum,count)
            if self.GetFlag(self._m_stCurQuest+"."+label) == 0:
                self._m_vRewardData.append(RewardData(RewardData.REWARD_TYPE_ITEM, dwVnum, count))
            else:
                self._m_bIsGivenReward = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        def GiveExp(self, label, exp):
            #sys_log(1, "QUEST GiveExp %s %d", label,exp)

            if self.GetFlag(self._m_stCurQuest+"."+label) == 0:
                self._m_vRewardData.append(RewardData(RewardData.REWARD_TYPE_EXP, exp, 0))
            else:
                self._m_bIsGivenReward = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        def SetSendDoneFlag(self):
            self._m_bShouldSendDone = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
        def GetAndResetDoneFlag(self):
            temp = self._m_bShouldSendDone
            self._m_bShouldSendDone = LGEMiscellaneous.DEFINECONSTANTS.false
            return temp

        def SendFlagList(self, ch):
            it = m_FlagMap.begin()
            while it is not self._m_FlagMap.end():
                if it.first.size()>9 and it.first.compare(it.first.size()-9,9, ".__status") == 0:
                    quest_name = it.first.substr(0, it.first.size()-9)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to pointers to value types:
#ORIGINAL METINII C CODE: const char* state_name = CQuestManager::instance().GetQuestStateName(quest_name, it->second);
                    state_name = CQuestManager.instance().GetQuestStateName(quest_name, it.second)
                    ch.ChatPacket(EChatType.CHAT_TYPE_INFO, "%s %s (%d)", quest_name, state_name, it.second)
                else:
                    ch.ChatPacket(EChatType.CHAT_TYPE_INFO, "%s %d", it.first.c_str(), it.second)
                it += 1

# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#        SetQuestState(szQuestName, szStateName)

        def SetConfirmWait(self, dwPID):
            self._m_bConfirmWait = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
            self._m_dwWaitConfirmFromPID = dwPID
        def ClearConfirmWait(self):
            self._m_bConfirmWait = LGEMiscellaneous.DEFINECONSTANTS.false
## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: bool IsConfirmWait() const
        def IsConfirmWait(self):
            return self._m_bConfirmWait
## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: bool IsConfirmWait(uint dwPID) const
        def IsConfirmWait(self, dwPID):
            return self._m_bConfirmWait and dwPID == self._m_dwWaitConfirmFromPID

        def _SetSendFlag(self, idx):
            self._m_iSendToClient |= idx

        def _ClearSendFlag(self):
            self._m_iSendToClient = 0
        def _SaveFlag(self, name, value):
            it = self._m_FlagSaveMap.find(name)

            if it is self._m_FlagSaveMap.end():
                self._m_FlagSaveMap.update({name: value})
            elif it.second != value:
                it.second = value

        def _ClearCurrentQuestBeginFlag(self):
            self._SetSendFlag(self.QUEST_SEND_ISBEGIN)
            self._m_RunningQuestState.bStart = LGEMiscellaneous.DEFINECONSTANTS.false

        def _SetCurrentQuestBeginFlag(self):
            q = CQuestManager.instance()
            iQuestIndex = int(q.GetQuestIndexByName(self._m_stCurQuest))
            self._m_RunningQuestState.bStart = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
            self._m_RunningQuestState.iIndex = iQuestIndex

            self._SetSendFlag(self.QUEST_SEND_ISBEGIN)

        def _GetCurrentQuestBeginFlag(self):
            return self._m_RunningQuestState.iIndex if self._m_RunningQuestState is not None x else 0

        def _SendQuestInfoPakcet(self):
            m_iSendToClient = assert()
            m_RunningQuestState = assert()

            qi = packet_quest_info()

            qi.header = byte(Globals.LG_HEADER_GC_QUEST_INFO)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            qi.size = sizeof(packet_quest_info)
            qi.index = m_RunningQuestState.iIndex
            qi.flag = m_iSendToClient
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if __QUEST_RENEWAL__
            qi.c_index = ushort(CQuestManager.instance().GetQuestCategoryByQuestIndex(qi.index))
##endif

            buf = TEMP_BUFFER(8192, DefineConstants.false)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            buf.write(qi, sizeof(qi))

            if m_iSendToClient & self.QUEST_SEND_ISBEGIN:
                temp = byte(1 if m_RunningQuestState.bStart 1 else 0)
                buf.write(temp, 1)
                qi.size+=1

                #sys_log(1, "QUEST BeginFlag %d", int(temp))
            if m_iSendToClient & self.QUEST_SEND_TITLE:
                m_RunningQuestState._title.reserve(30+1)
                buf.write(m_RunningQuestState._title.c_str(), 30+1)
                qi.size+=ushort(30+1)

                #sys_log(1, "QUEST Title %s", m_RunningQuestState._title.c_str())
            if m_iSendToClient & self.QUEST_SEND_CLOCK_NAME:
                m_RunningQuestState._clock_name.reserve(16+1)
                buf.write(m_RunningQuestState._clock_name.c_str(), 16+1)
                qi.size+=ushort(16+1)

                #sys_log(1, "QUEST Clock Name %s", m_RunningQuestState._clock_name.c_str())
            if m_iSendToClient & self.QUEST_SEND_CLOCK_VALUE:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                buf.write(m_RunningQuestState._clock_value, sizeof(int))
                qi.size+=4

                #sys_log(1, "QUEST Clock Value %d", m_RunningQuestState._clock_value)
            if m_iSendToClient & self.QUEST_SEND_COUNTER_NAME:
                m_RunningQuestState._counter_name.reserve(16+1)
                buf.write(m_RunningQuestState._counter_name.c_str(), 16+1)
                qi.size+=ushort(16+1)

                #sys_log(1, "QUEST Counter Name %s", m_RunningQuestState._counter_name.c_str())
            if m_iSendToClient & self.QUEST_SEND_COUNTER_VALUE:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                buf.write(m_RunningQuestState._counter_value, sizeof(int))
                qi.size+=4

                #sys_log(1, "QUEST Counter Value %d", m_RunningQuestState._counter_value)
            if m_iSendToClient & self.QUEST_SEND_ICON_FILE:
                m_RunningQuestState._icon_file.reserve(24+1)
                buf.write(m_RunningQuestState._icon_file.c_str(), 24+1)
                qi.size+=ushort(24+1)

                #sys_log(1, "QUEST Icon File %s", m_RunningQuestState._icon_file.c_str())

            CQuestManager.instance().GetCurrentCharacterPtr().GetDesc().Packet(buf.read_peek(), buf.size())

            m_iSendToClient = 0














