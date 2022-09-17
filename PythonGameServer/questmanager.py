## Laniatus Games Studio Inc. | NOTE: Python has no need of forward class declarations:
#class ITEM
## Laniatus Games Studio Inc. | NOTE: Python has no need of forward class declarations:
#class CHARACTER
## Laniatus Games Studio Inc. | NOTE: Python has no need of forward class declarations:
#class CDungeon

class quest: #this class replaces the original namespace 'quest'

# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    IsScriptTrue(code, size)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    ScriptToString(str)

    class CQuestManager(singleton):
        QUEST_SKIN_NOWINDOW = 0
        QUEST_SKIN_NORMAL = 1
        QUEST_SKIN_SCROLL = 4
        QUEST_SKIN_CINEMATIC = 5
        QUEST_SKIN_COUNT = 6


        def __init__(self):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.m_mapEventName = {}
            self._m_pSelectedDungeon = None
            self._m_dwServerTimerArg = 0
            self._m_mapServerTimer = {}
            self._m_iRunningEventIndex = 0
            self._m_mapEventFlag = {}
            self._L = None
            self._m_bNoSend = False
            self._m_registeredNPCVnum = set()
            self._m_mapNPC = {}
            self._m_mapNPCNameID = {}
            self._m_mapTimerID = {}
            self._m_CurrentRunningState = None
            self._m_mapPC = {}
            self._m_pCurrentCharacter = None
            self._m_pCurrentNPCCharacter = None
            self._m_pCurrentPartyMember = None
            self._m_pCurrentPC = None
            self._m_strScript = ""
            self._m_iCurrentSkin = 0
            self._m_hmQuestName = _boost_func_of_void.unordered_map()
            self._m_hmQuestStartScript = _boost_func_of_void.unordered_map()
            self._m_mapQuestNameByIndex = {}
            self._m_bError = False
            self._m_pOtherPCBlockRootPC = None
            self._m_vecPCStack = []
            self.QuestCategoryIndexMap = {}

            self._m_pSelectedDungeon = None
            self._m_dwServerTimerArg = 0
            self._m_iRunningEventIndex = 0
            self._L = None
            self._m_bNoSend = LGEMiscellaneous.DEFINECONSTANTS.false
            self._m_CurrentRunningState = None
            self._m_pCurrentCharacter = None
            self._m_pCurrentNPCCharacter = None
            self._m_pCurrentPartyMember = None
            self._m_pCurrentPC = None
            self._m_iCurrentSkin = 0
            self._m_bError = LGEMiscellaneous.DEFINECONSTANTS.false
            self._m_pOtherPCBlockRootPC = None

        def close(self):
            self.Destroy()

        def Initialize(self):
            if g_bAuthServer:
                return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

            if not self.InitializeLua():
                return LGEMiscellaneous.DEFINECONSTANTS.false

            self._m_pSelectedDungeon = None

            self.m_mapEventName.insert(TEventNameMap.value_type("click", QUEST_CLICK_EVENT))
            self.m_mapEventName.insert(TEventNameMap.value_type("kill", QUEST_KILL_EVENT))
            self.m_mapEventName.insert(TEventNameMap.value_type("timer", QUEST_TIMER_EVENT))
            self.m_mapEventName.insert(TEventNameMap.value_type("levelup", QUEST_LEVELUP_EVENT))
            self.m_mapEventName.insert(TEventNameMap.value_type("login", QUEST_LOGIN_EVENT))
            self.m_mapEventName.insert(TEventNameMap.value_type("logout", QUEST_LOGOUT_EVENT))
            self.m_mapEventName.insert(TEventNameMap.value_type("button", QUEST_BUTTON_EVENT))
            self.m_mapEventName.insert(TEventNameMap.value_type("info", QUEST_INFO_EVENT))
            self.m_mapEventName.insert(TEventNameMap.value_type("chat", QUEST_CHAT_EVENT))
            self.m_mapEventName.insert(TEventNameMap.value_type("in", QUEST_ATTR_IN_EVENT))
            self.m_mapEventName.insert(TEventNameMap.value_type("out", QUEST_ATTR_OUT_EVENT))
            self.m_mapEventName.insert(TEventNameMap.value_type("use", QUEST_ITEM_USE_EVENT))
            self.m_mapEventName.insert(TEventNameMap.value_type("server_timer", QUEST_SERVER_TIMER_EVENT))
            self.m_mapEventName.insert(TEventNameMap.value_type("enter", QUEST_ENTER_STATE_EVENT))
            self.m_mapEventName.insert(TEventNameMap.value_type("leave", QUEST_LEAVE_STATE_EVENT))
            self.m_mapEventName.insert(TEventNameMap.value_type("letter", QUEST_LETTER_EVENT))
            self.m_mapEventName.insert(TEventNameMap.value_type("take", QUEST_ITEM_TAKE_EVENT))
            self.m_mapEventName.insert(TEventNameMap.value_type("target", QUEST_TARGET_EVENT))
            self.m_mapEventName.insert(TEventNameMap.value_type("party_kill", QUEST_PARTY_KILL_EVENT))
            self.m_mapEventName.insert(TEventNameMap.value_type("unmount", QUEST_UNMOUNT_EVENT))
            self.m_mapEventName.insert(TEventNameMap.value_type("pick", QUEST_ITEM_PICK_EVENT))
            self.m_mapEventName.insert(TEventNameMap.value_type("sig_use", QUEST_SIG_USE_EVENT))
            self.m_mapEventName.insert(TEventNameMap.value_type("item_informer", QUEST_ITEM_INFORMER_EVENT))

            self._m_bNoSend = LGEMiscellaneous.DEFINECONSTANTS.false

            self._m_iCurrentSkin = QUEST_SKIN_NORMAL

                inf = ifstream((g_stQuestDir + "/questnpc.txt").c_str())
                line = 0

                if not inf.is_open():
                    #lani_err("QUEST Cannot open 'questnpc.txt'")
                else:
                    #sys_log(0, "QUEST can open 'questnpc.txt' (%s)", g_stQuestDir.c_str())

                while True:
                    vnum = None

                    inf >> vnum

                    line += 1

                    if inf.fail():
                        break

                    s = ""
                    getline(inf, s)
                    li = 0
                    ri = uint(len(s)-1)
                    while li < len(s) and (s[li]).isspace():
                        li += 1
                    while ri > 0 and (s[ri]).isspace():
                        ri -= 1

                    if ri < li:
                        #lani_err("QUEST questnpc.txt:%d:npc name error",line)
                        continue

                    s = s[li:ri+1]

                    n = 0
                    temp_ref_n = RefObject(n);
                    Globals.str_to_number(temp_ref_n, s)
                    n = temp_ref_n.arg_value
                    if n != 0:
                        continue

                    if test_server:
                        #sys_log(0, "QUEST reading script of %s(%d)", s, vnum)
                    self._m_mapNPC[vnum].Set(vnum, s)
                    self._m_mapNPCNameID[s] = vnum
                self._m_mapNPC[0].Set(0, "notarget")
            self.SetEventFlag("guild_withdraw_delay", 1)
            self.SetEventFlag("guild_disband_delay", 1)
            self.ReadQuestCategoryToDict()

            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        def Destroy(self):
            if self._L:
                lua_close(self._L)
                self._L = None

# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#        InitializeLua()
        def GetLuaState(self):
            return self._L
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#        AddLuaFunctionTable(c_pszName, preg)


# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#        OpenState(quest_name, state_index)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#        CloseState(qs)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#        RunState(qs)

        def GetPC(self, pc):
            it = PCMap.iterator()

            pkChr = CHARACTER_MANAGER.instance().FindByPID(pc)

            if pkChr is None:
                return None

            self._m_pCurrentPC = self.GetPCForce(pc)
            self._m_pCurrentCharacter = pkChr
            self._m_pSelectedDungeon = None
            return (self._m_pCurrentPC)

        def GetPCForce(self, pc):
            it = PCMap.iterator()

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((it = m_mapPC.find(pc)) == m_mapPC.end())
            if (it = self._m_mapPC.find(pc)) is self._m_mapPC.end():
                pPC = self._m_mapPC[pc]
                pPC.SetID(pc)
                return pPC

            return it.second

        def GetCurrentNPCRace(self):
            return self.GetCurrentNPCCharacterPtr().GetRaceNum() if self.GetCurrentNPCCharacterPtr() is not None else 0

        def GetCurrentQuestName(self):
            return self.GetCurrentPC().GetCurrentQuestName()

        def FindNPCIDByName(self, name):
            it = self._m_mapNPCNameID.find(name)
            return uint(it.second if it is not self._m_mapNPCNameID.end() is not None else 0)

        def GetCurrentNPCCharacterPtr(self):
            return self.GetCurrentCharacterPtr().GetQuestNPC() if self.GetCurrentCharacterPtr() is not None else None

        def SetCurrentEventIndex(self, index):
            self._m_iRunningEventIndex = index

        def UseItem(self, pc, item, bReceiveAll):
            if test_server:
                #sys_log(0, "questmanager::UseItem Start : itemVnum : %d PC : %d", item.GetOriginalVnum(), pc)
            pPC = None
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((pPC = GetPC(pc)))
            if (pPC = self.GetPC(pc)):
                if not self.CheckQuestLoaded(pPC):
                    ch = CHARACTER_MANAGER.instance().FindByPID(pc)
                    if ch:
                        ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Your request is loading. Please be patient."))
                    return LGEMiscellaneous.DEFINECONSTANTS.false
                self.SetCurrentItem(item)
                return self._m_mapNPC[item.GetVnum()].OnUseItem(pPC, bReceiveAll)
            else:
                #lani_err("QUEST USE_ITEM_EVENT no such pc id : %d", pc)
                return LGEMiscellaneous.DEFINECONSTANTS.false

        def PickupItem(self, pc, item):
            if test_server:
                #sys_log(0, "questmanager::PickupItem Start : itemVnum : %d PC : %d", item.GetOriginalVnum(), pc)
            pPC = None
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((pPC = GetPC(pc)))
            if (pPC = self.GetPC(pc)):
                if not self.CheckQuestLoaded(pPC):
                    ch = CHARACTER_MANAGER.instance().FindByPID(pc)
                    if ch:
                        ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Your request is loading. Please be patient."))
                    return LGEMiscellaneous.DEFINECONSTANTS.false
                self.SetCurrentItem(item)

                return self._m_mapNPC[item.GetVnum()].OnPickupItem(pPC)
            else:
                #lani_err("QUEST PICK_ITEM_EVENT no such pc id : %d", pc)
                return LGEMiscellaneous.DEFINECONSTANTS.false

        def SIGUse(self, pc, sig_vnum, item, bReceiveAll):
            if test_server:
                #sys_log(0, "questmanager::SIGUse Start : itemVnum : %d PC : %d", item.GetOriginalVnum(), pc)
            pPC = None
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((pPC = GetPC(pc)))
            if (pPC = self.GetPC(pc)):
                if not self.CheckQuestLoaded(pPC):
                    ch = CHARACTER_MANAGER.instance().FindByPID(pc)
                    if ch:
                        ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Your request is loading. Please be patient."))
                    return LGEMiscellaneous.DEFINECONSTANTS.false
                self.SetCurrentItem(item)

                return self._m_mapNPC[sig_vnum].OnSIGUse(pPC, bReceiveAll)
            else:
                #lani_err("QUEST USE_ITEM_EVENT no such pc id : %d", pc)
                return LGEMiscellaneous.DEFINECONSTANTS.false

        def TakeItem(self, pc, npc, item):
            pPC = None

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((pPC = GetPC(pc)))
            if (pPC = self.GetPC(pc)):
                if not self.CheckQuestLoaded(pPC):
                    ch = CHARACTER_MANAGER.instance().FindByPID(pc)
                    if ch:
                        ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Your request is loading. Please be patient."))
                    return LGEMiscellaneous.DEFINECONSTANTS.false
                self.SetCurrentItem(item)
                return self._m_mapNPC[npc].OnTakeItem(pPC)
            else:
                #lani_err("QUEST USE_ITEM_EVENT no such pc id : %d", pc)
                return LGEMiscellaneous.DEFINECONSTANTS.false

        def GetCurrentItem(self):
            return self.GetCurrentCharacterPtr().GetQuestItemPtr() if self.GetCurrentCharacterPtr() is not None else None

        def ClearCurrentItem(self):
            if self.GetCurrentCharacterPtr():
                self.GetCurrentCharacterPtr().ClearQuestItemPtr()

        def SetCurrentItem(self, item):
            if self.GetCurrentCharacterPtr():
                self.GetCurrentCharacterPtr().SetQuestItemPtr(item)

        def AddServerTimer(self, name, arg, event):
            #sys_log(0, "XXX AddServerTimer %s %d %p", name, arg, Globals.get_pointer(event))
            if (name, arg) in self._m_mapServerTimer.keys():
                #lani_err("already registered server timer name:%s arg:%u", name, arg)
                return
            self._m_mapServerTimer.update({(name, arg): event})

        def ClearServerTimer(self, name, arg):
            it = self._m_mapServerTimer.find((name, arg))
            if it is not self._m_mapServerTimer.end():
                event = it.second
                event_cancel(event)
                self._m_mapServerTimer.pop(it)

        def ClearServerTimerNotCancel(self, name, arg):
            self._m_mapServerTimer.pop((name, arg))

        def CancelServerTimers(self, arg):
            it = m_mapServerTimer.begin()
            while it is not self._m_mapServerTimer.end():
                if it.first.second != arg:
                    it += 1
                else:
                    event = it.second
                    event_cancel(event)
                    it = self._m_mapServerTimer.pop(it)

        def SetServerTimerArg(self, dwArg):
            self._m_dwServerTimerArg = dwArg

        def GetServerTimerArg(self):
            return self._m_dwServerTimerArg

        def ServerTimer(self, npc, arg):
            self.SetServerTimerArg(arg)
            #sys_log(0, "XXX ServerTimer Call NPC %p", self.GetPCForce(0))
            self._m_pCurrentPC = self.GetPCForce(0)
            self._m_pCurrentCharacter = None
            self._m_pSelectedDungeon = None
            return self._m_mapNPC[npc].OnServerTimer(self._m_pCurrentPC)

        def Login(self, pc, c_pszQuest = None):
            pPC = None

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((pPC = GetPC(pc)))
            if (pPC = self.GetPC(pc)):
                if not self.CheckQuestLoaded(pPC):
                    return

                self._m_mapNPC[QUEST_NO_NPC].OnLogin(pPC, c_pszQuest)
            else:
                #lani_err("QUEST no such pc id : %d", pc)

        def Logout(self, pc):
            pPC = None

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((pPC = GetPC(pc)))
            if (pPC = self.GetPC(pc)):
                if not self.CheckQuestLoaded(pPC):
                    return

                self._m_mapNPC[QUEST_NO_NPC].OnLogout(pPC)
            else:
                #lani_err("QUEST no such pc id : %d", pc)

        def Timer(self, pc, npc):
            pPC = None

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((pPC = GetPC(pc)))
            if (pPC = self.GetPC(pc)):
                if not self.CheckQuestLoaded(pPC):
                    return LGEMiscellaneous.DEFINECONSTANTS.false

                return self._m_mapNPC[npc].OnTimer(pPC)
            else:
                #lani_err("QUEST TIMER_EVENT no such pc id : %d", pc)
                return LGEMiscellaneous.DEFINECONSTANTS.false

        def Click(self, pc, pkChrTarget):
            pPC = self.GetPC(pc)

            if pPC:
                if not self.CheckQuestLoaded(pPC):
                    ch = CHARACTER_MANAGER.instance().FindByPID(pc)

                    if ch:
                        ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Your request is loading. Please be patient."))

                    return LGEMiscellaneous.DEFINECONSTANTS.false

                pInfo = CTargetManager.instance().GetTargetInfo(pc, ETargetTypes.TARGET_TYPE_VID, pkChrTarget.GetVID())
                if test_server:
                    #sys_log(0, "CQuestManager::Click(pid=%d, npc_name=%s) - target_info(%x)", pc, pkChrTarget.GetName(LOCALE_LANIATUS), pInfo)

                if pInfo:
                    bRet = None
                    if self._m_mapNPC[QUEST_NO_NPC].OnTarget(pPC, pInfo.dwQuestIndex, pInfo.szTargetName, "click", bRet):
                        return bRet

                dwCurrentNPCRace = pkChrTarget.GetRaceNum()

                if pkChrTarget.IsNPC():
                    it = self._m_mapNPC.find(dwCurrentNPCRace)

                    if it is self._m_mapNPC.end():
                        #sys_log(0, "CQuestManager::Click(pid=%d, target_npc_name=%s) - NOT EXIST NPC RACE VNUM[%d]", pc, pkChrTarget.GetName(LOCALE_LANIATUS), dwCurrentNPCRace)
                        return LGEMiscellaneous.DEFINECONSTANTS.false

                    if it.second.HasChat():
                        if test_server:
                            #sys_log(0, "CQuestManager::Click->OnChat")

                        if not it.second.OnChat(pPC):
                            if test_server:
                                #sys_log(0, "CQuestManager::Click->OnChat Failed")

                            return it.second.OnClick(pPC)

                        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
                    else:
                        return it.second.OnClick(pPC)
                return LGEMiscellaneous.DEFINECONSTANTS.false
            else:
                #lani_err("QUEST CLICK_EVENT no such pc id : %d", pc)
                return LGEMiscellaneous.DEFINECONSTANTS.false

        def Kill(self, pc, npc):
            pPC = None
            #sys_log(0, "CQuestManager::Kill QUEST_KILL_EVENT (pc=%d, npc=%d)", pc, npc)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((pPC = GetPC(pc)))
            if (pPC = self.GetPC(pc)):
                if not self.CheckQuestLoaded(pPC):
                    return

                if npc >= Globals.MAIN_RACE_MAX_NUM:
                    self._m_mapNPC[npc].OnKill(pPC)

                self._m_mapNPC[QUEST_NO_NPC].OnKill(pPC)

                ch = self.GetCurrentCharacterPtr()
                pParty = ch.GetParty()
                leader = pParty.GetLeaderCharacter() if pParty is not None else ch

                if leader:
                    self._m_pCurrentPartyMember = ch
                    if npc >= Globals.MAIN_RACE_MAX_NUM:
                        self._m_mapNPC[npc].OnPartyKill(self.GetPC(leader.GetPlayerID()))

                    self._m_mapNPC[QUEST_NO_NPC].OnPartyKill(self.GetPC(leader.GetPlayerID()))
                    pPC = self.GetPC(pc)

            else:
                #lani_err("QUEST: no such pc id : %d", pc)

        def LevelUp(self, pc):
            pPC = None

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((pPC = GetPC(pc)))
            if (pPC = self.GetPC(pc)):
                if not self.CheckQuestLoaded(pPC):
                    return

                self._m_mapNPC[QUEST_NO_NPC].OnLevelUp(pPC)
            else:
                #lani_err("QUEST LEVELUP_EVENT no such pc id : %d", pc)

        def AttrIn(self, pc, ch, attr):
            pPC = None
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((pPC = GetPC(pc)))
            if (pPC = self.GetPC(pc)):
                self._m_pCurrentPartyMember = ch
                if not self.CheckQuestLoaded(pPC):
                    return

                self._m_mapNPC[attr+QUEST_ATTR_NPC_START].OnAttrIn(pPC)
            else:

                #lani_err("QUEST no such pc id : %d", pc)

        def AttrOut(self, pc, ch, attr):
            pPC = None
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((pPC = GetPC(pc)))
            if (pPC = self.GetPC(pc)):
                self._m_pCurrentPartyMember = ch
                if not self.CheckQuestLoaded(pPC):
                    return

                self._m_mapNPC[attr+QUEST_ATTR_NPC_START].OnAttrOut(pPC)
            else:
                #lani_err("QUEST no such pc id : %d", pc)

        def Target(self, pc, dwQuestIndex, c_pszTargetName, c_pszVerb):
            pPC = None

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((pPC = GetPC(pc)))
            if (pPC = self.GetPC(pc)):
                if not self.CheckQuestLoaded(pPC):
                    return LGEMiscellaneous.DEFINECONSTANTS.false

                bRet = None
                return self._m_mapNPC[QUEST_NO_NPC].OnTarget(pPC, dwQuestIndex, c_pszTargetName, c_pszVerb, bRet)

            return LGEMiscellaneous.DEFINECONSTANTS.false

        def GiveItemToPC(self, pc, pkChr):
            if not pkChr.IsPC():
                return LGEMiscellaneous.DEFINECONSTANTS.false

            pPC = self.GetPC(pc)

            if pPC:
                if not self.CheckQuestLoaded(pPC):
                    return LGEMiscellaneous.DEFINECONSTANTS.false

                pInfo = CTargetManager.instance().GetTargetInfo(pc, ETargetTypes.TARGET_TYPE_VID, pkChr.GetVID())

                if pInfo:
                    bRet = None

                    if self._m_mapNPC[QUEST_NO_NPC].OnTarget(pPC, pInfo.dwQuestIndex, pInfo.szTargetName, "click", bRet):
                        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

            return LGEMiscellaneous.DEFINECONSTANTS.false

        def Unmount(self, pc):
            pPC = None

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((pPC = GetPC(pc)))
            if (pPC = self.GetPC(pc)):
                if not self.CheckQuestLoaded(pPC):
                    return

                self._m_mapNPC[QUEST_NO_NPC].OnUnmount(pPC)
            else:
                #lani_err("QUEST no such pc id : %d", pc)

        def QuestButton(self, pc, quest_index):
            pPC = None
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((pPC = GetPC(pc)))
            if (pPC = self.GetPC(pc)):
                if not self.CheckQuestLoaded(pPC):
                    ch = CHARACTER_MANAGER.instance().FindByPID(pc)
                    if ch:
                        ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Your request is loading. Please be patient."))
                    return
                self._m_mapNPC[QUEST_NO_NPC].OnButton(pPC, quest_index)
            else:
                #lani_err("QUEST CLICK_EVENT no such pc id : %d", pc)

        def QuestInfo(self, pc, quest_index):
            pPC = None

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((pPC = GetPC(pc)))
            if (pPC = self.GetPC(pc)):
                if not self.CheckQuestLoaded(pPC):
                    ch = CHARACTER_MANAGER.instance().FindByPID(pc)

                    if ch:
                        ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Your request is loading. Please be patient."))

                    return

                self._m_mapNPC[QUEST_NO_NPC].OnInfo(pPC, quest_index)
            else:
                #lani_err("QUEST INFO_EVENT no such pc id : %d", pc)

        def EnterState(self, pc, quest_index, state):
            pPC = None
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((pPC = GetPC(pc)))
            if (pPC = self.GetPC(pc)):
                if not self.CheckQuestLoaded(pPC):
                    return

                self._m_mapNPC[QUEST_NO_NPC].OnEnterState(pPC, quest_index, state)
            else:
                #lani_err("QUEST no such pc id : %d", pc)

        def LeaveState(self, pc, quest_index, state):
            pPC = None
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((pPC = GetPC(pc)))
            if (pPC = self.GetPC(pc)):
                if not self.CheckQuestLoaded(pPC):
                    return

                self._m_mapNPC[QUEST_NO_NPC].OnLeaveState(pPC, quest_index, state)
            else:
                #lani_err("QUEST no such pc id : %d", pc)

# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#        Letter(pc)
        def Letter(self, pc, quest_index, state):
            pPC = None
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((pPC = GetPC(pc)))
            if (pPC = self.GetPC(pc)):
                if not self.CheckQuestLoaded(pPC):
                    return

                self._m_mapNPC[QUEST_NO_NPC].OnLetter(pPC, quest_index, state)
            else:
                #lani_err("QUEST no such pc id : %d", pc)

        def ItemInformer(self, pc, vnum):

            pPC = None
            pPC = self.GetPC(pc)

            self._m_mapNPC[QUEST_NO_NPC].OnItemInformer(pPC,vnum)

        def CheckQuestLoaded(self, pc):
            return pc is not None and pc.IsLoaded()

        def Select(self, pc, selection):
            pPC = None

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((pPC = GetPC(pc)) && pPC->IsRunning() && pPC->GetRunningQuestState()->suspend_state==SUSPEND_STATE_SELECT)
            if (pPC = self.GetPC(pc)) and pPC.IsRunning() and pPC.GetRunningQuestState().suspend_state == SUSPEND_STATE_SELECT:
                pPC.SetSendDoneFlag()

                if pPC.GetRunningQuestState().chat_scripts:
                    old_qs = pPC.GetRunningQuestState()
                    self.CloseState(old_qs)

                    if selection >= len(pPC.GetRunningQuestState().chat_scripts):
                        pPC.SetSendDoneFlag()
                        self._GotoEndState(old_qs)
                        pPC.EndRunning()
                    else:
                        pas = pPC.GetRunningQuestState().chat_scripts[selection]
                        quest.CQuestManager.ExecuteQuestScript(pPC, pas.quest_index, pas.state_index, pas.script.GetCode(), pas.script.GetSize(), NULL, ((not DefineConstants.false)))
                else:
                    pPC.GetRunningQuestState().args = 1
                    lua_pushnumber(pPC.GetRunningQuestState().co,selection+1)

                    if not self.RunState(pPC.GetRunningQuestState()):
                        self.CloseState(pPC.GetRunningQuestState())
                        pPC.EndRunning()
            else:
                #lani_err("wrong QUEST_SELECT request! : %d",pc)

        def Resume(self, pc):
            pPC = None

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((pPC = GetPC(pc)) && pPC->IsRunning() && pPC->GetRunningQuestState()->suspend_state == SUSPEND_STATE_PAUSE)
            if (pPC = self.GetPC(pc)) and pPC.IsRunning() and pPC.GetRunningQuestState().suspend_state == SUSPEND_STATE_PAUSE:
                pPC.SetSendDoneFlag()
                pPC.GetRunningQuestState().args = 0

                if not self.RunState(pPC.GetRunningQuestState()):
                    self.CloseState(pPC.GetRunningQuestState())
                    pPC.EndRunning()
            else:
                #lani_err("wrong QUEST_WAIT request! : %d",pc)

        def Input(self, pc, msg):
            pPC = self.GetPC(pc)
            if pPC is None:
                #lani_err("no pc! : %u",pc)
                return

            if not pPC.IsRunning():
                #lani_err("no quest running for pc, cannot process input : %u", pc)
                return

            if pPC.GetRunningQuestState().suspend_state != SUSPEND_STATE_INPUT:
                #lani_err("not wait for a input : %u %d", pc, pPC.GetRunningQuestState().suspend_state)
                return

            pPC.SetSendDoneFlag()

            pPC.GetRunningQuestState().args = 1
            lua_pushstring(pPC.GetRunningQuestState().co,msg)

            if not self.RunState(pPC.GetRunningQuestState()):
                self.CloseState(pPC.GetRunningQuestState())
                pPC.EndRunning()

        def Confirm(self, pc, confirm, pc2 = 0):
            pPC = self.GetPC(pc)

            if not pPC.IsRunning():
                #lani_err("no quest running for pc, cannot process input : %u", pc)
                return

            if pPC.GetRunningQuestState().suspend_state != SUSPEND_STATE_CONFIRM:
                #lani_err("not wait for a confirm : %u %d", pc, pPC.GetRunningQuestState().suspend_state)
                return

            if pc2 != 0 and not pPC.IsConfirmWait(pc2):
                #lani_err("not wait for a confirm : %u %d", pc, pPC.GetRunningQuestState().suspend_state)
                return

            pPC.ClearConfirmWait()

            pPC.SetSendDoneFlag()

            pPC.GetRunningQuestState().args = 1
            lua_pushnumber(pPC.GetRunningQuestState().co, confirm)

            self.AddScript("[END_CONFIRM_WAIT]")
            self.SetSkinStyle(QUEST_SKIN_NOWINDOW)
            self.SendScript()

            if not self.RunState(pPC.GetRunningQuestState()):
                self.CloseState(pPC.GetRunningQuestState())
                pPC.EndRunning()


        def SelectItem(self, pc, selection):
            pPC = self.GetPC(pc)
            if pPC is not None and pPC.IsRunning() and pPC.GetRunningQuestState().suspend_state == SUSPEND_STATE_SELECT_ITEM:
                pPC.SetSendDoneFlag()
                pPC.GetRunningQuestState().args = 1
                lua_pushnumber(pPC.GetRunningQuestState().co,selection)

                if not self.RunState(pPC.GetRunningQuestState()):
                    self.CloseState(pPC.GetRunningQuestState())
                    pPC.EndRunning()

        def LogoutPC(self, ch):
            pPC = self.GetPC(ch.GetPlayerID())

            if pPC is not None and pPC.IsRunning():
                self.CloseState(pPC.GetRunningQuestState())
                pPC.CancelRunning()

            self.Logout(ch.GetPlayerID())

            if ch is self._m_pCurrentCharacter:
                self._m_pCurrentCharacter = None
                self._m_pCurrentPC = None

        def DisconnectPC(self, ch):
            self._m_mapPC.pop(ch.GetPlayerID())

        def GetCurrentState(self):
            return self._m_CurrentRunningState

        def LoadStartQuest(self, quest_name, idx):
            it = g_setQuestObjectDir.begin()
            while it is not g_setQuestObjectDir.end():
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to references to variables:
#ORIGINAL METINII C CODE: const str& stQuestObjectDir = *it;
                stQuestObjectDir = *it
                full_name = stQuestObjectDir + "/begin_condition/" + quest_name
                inf = ifstream(full_name)

                if inf.is_open():
                    #sys_log(0, "QUEST loading begin condition for %s", quest_name)

                    ib = istreambuf_iterator(inf)
                    ie = istreambuf_iterator()
                    copy(ib, ie, back_inserter(self._m_hmQuestStartScript[idx]))
                it += 1

        def CanStartQuest(self, quest_index, pc):
            return self.CanStartQuest(quest_index)

        def CanStartQuest(self, quest_index):
            it = THashMapQuestStartScript.iterator()

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((it = m_hmQuestStartScript.find(quest_index)) == m_hmQuestStartScript.end())
            if (it = self._m_hmQuestStartScript.find(quest_index)) is self._m_hmQuestStartScript.end():
                return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
            else:
                x = lua_gettop(self._L)
                lua_dobuffer(self._L, (it.second[0]), it.second.size(), "StartScript")
                bStart = lua_toboolean(self._L, -1)
                lua_settop(self._L, x)
                return bStart != 0

        def CanEndQuestAtState(self, quest_name, state_name):
            return LGEMiscellaneous.DEFINECONSTANTS.false

        def GetCurrentCharacterPtr(self):
            return self._m_pCurrentCharacter
        def GetCurrentPartyMember(self):
            return self._m_pCurrentPartyMember
        def GetCurrentPC(self):
            return self._m_pCurrentPC

        def GetCurrentDungeon(self):
            ch = self.GetCurrentCharacterPtr()

            if ch is None:
                if self._m_pSelectedDungeon:
                    return self._m_pSelectedDungeon
                return None

            return ch.GetDungeonForce()

        def SelectDungeon(self, pDungeon):
            self._m_pSelectedDungeon = pDungeon

        def ClearScript(self):
            self._m_strScript = ""
            self._m_iCurrentSkin = QUEST_SKIN_NORMAL

        def SendScript(self):
            if self._m_bNoSend:
                self._m_bNoSend = LGEMiscellaneous.DEFINECONSTANTS.false
                self.ClearScript()
                return

            if self._m_strScript == "[DONE]" or self._m_strScript == "[NEXT]":
                if self._m_pCurrentPC is not None and (not self._m_pCurrentPC.GetAndResetDoneFlag()) and self._m_strScript == "[DONE]" and self._m_iCurrentSkin == QUEST_SKIN_NORMAL and not self.IsError():
                    self.ClearScript()
                    return
                self._m_iCurrentSkin = QUEST_SKIN_NOWINDOW

            packet_script = struct.packet_script()

            packet_script.header = Globals.LG_HEADER_GC_SCRIPT
            packet_script.skin = self._m_iCurrentSkin
            packet_script.src_size = len(self._m_strScript)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            packet_script.size = packet_script.src_size + sizeof(packet_script)

            buf = TEMP_BUFFER(8192, DefineConstants.false)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            buf.write(packet_script, sizeof(packet_script))
            buf.write(self._m_strScript[0], len(self._m_strScript))

            self.GetCurrentCharacterPtr().GetDesc().Packet(buf.read_peek(), buf.size())

            if test_server:
                #sys_log(0, "m_strScript %s size %d", self._m_strScript, buf.size())

            self.ClearScript()

        def AddScript(self, str):
            self._m_strScript+=str

# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#        BuildStateIndexToName(questName)

        def GetQuestStateIndex(self, quest_name, state_name):
            x = lua_gettop(self._L)
            lua_getglobal(self._L, quest_name)
            if lua_isnil(self._L,-1):
                #lani_err("QUEST wrong quest state file %s.%s",quest_name,state_name)
                lua_settop(self._L,x)
                return 0
            lua_pushstring(self._L, state_name)
            lua_gettable(self._L, -2)

            v = int(rint(lua_tonumber(self._L,-1)))
            lua_settop(self._L, x)
            if test_server:
                #sys_log(0,"[QUESTMANAGER] GetQuestStateIndex x(%d) v(%d) %s %s", v,x, quest_name, state_name)
            return v

        def GetQuestStateName(self, quest_name, state_index):
            x = lua_gettop(self._L)
            lua_getglobal(self._L, quest_name)
            if lua_isnil(self._L,-1):
                #lani_err("QUEST wrong quest state file %s.%d", quest_name, state_index)
                lua_settop(self._L,x)
                return ""
            lua_pushnumber(self._L, state_index)
            lua_gettable(self._L, -2)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to pointers to value types:
#ORIGINAL METINII C CODE: const char* str = lua_tostring(L, -1);
            str = lua_tostring(self._L, -1)
            lua_settop(self._L, x)
            return str

        def SetSkinStyle(self, iStyle):
            if iStyle<0 or iStyle >= QUEST_SKIN_COUNT:
                self._m_iCurrentSkin = QUEST_SKIN_NORMAL
            else:
                self._m_iCurrentSkin = iStyle

        def SetNoSend(self):
            self._m_bNoSend = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        def LoadTimerScript(self, name):
            it = None
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((it = m_mapTimerID.find(name)) != m_mapTimerID.end())
            if (it = self._m_mapTimerID.find(name)) is not self._m_mapTimerID.end():
                return it.second
            else:
                new_id = numeric_limits.max() - len(self._m_mapTimerID)

                self._m_mapNPC[new_id].Set(new_id, name)
                self._m_mapTimerID.update({name: new_id})

                return new_id

        def RegisterQuest(self, stQuestName, idx):
            assert idx > 0

            ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'itertype' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
            itertype(m_hmQuestName) it

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((it = m_hmQuestName.find(stQuestName)) != m_hmQuestName.end())
            if (it = self._m_hmQuestName.find(stQuestName)) != self._m_hmQuestName.end():
                return

            self._m_hmQuestName.insert((stQuestName, idx))
            self.LoadStartQuest(stQuestName, idx)
            self._m_mapQuestNameByIndex.update({idx: stQuestName})

            #sys_log(0, "QUEST: Register %4u %s", idx, stQuestName)

        def GetQuestIndexByName(self, name):
            it = self._m_hmQuestName.find(name)

            if it == self._m_hmQuestName.end():
                return 0

            return it.second

        ## Laniatus Games Studio Inc. | NOTE: This was formerly a static local variable declaration (not allowed in Python):

        def GetQuestNameByIndex(self, idx):
            ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'itertype' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
            itertype(m_mapQuestNameByIndex) it

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((it = m_mapQuestNameByIndex.find(idx)) == m_mapQuestNameByIndex.end())
            if (it = self._m_mapQuestNameByIndex.find(idx)) == self._m_mapQuestNameByIndex.end():
                #lani_err("cannot find quest name by index %u", idx)
                assert not "cannot find quest name by index"

                ## Laniatus Games Studio Inc. | NOTE: This static local variable declaration (not allowed in Python) has been moved just prior to the method:
                #                static str st = ""
                return GetQuestNameByIndex_st

            return it.second

        def RequestSetEventFlag(self, name, value):
            p = SPacketSetEventFlag()
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            strncpy_s(p.szFlagName, sizeof(p.szFlagName), name, _TRUNCATE)
            p.lValue = value
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            db_clientdesc.DBPacket(Globals.LG_HEADER_GD_SET_EVENT_FLAG, 0, p, sizeof(SPacketSetEventFlag))

        class SNPCSellFireworkPosition:
        class SEventNPCPosition:
        ## Laniatus Games Studio Inc. | NOTE: This was formerly a static local variable declaration (not allowed in Python):

        def SetEventFlag(self, name, value):
            prev_value = self._m_mapEventFlag[name]

            #sys_log(0, "QUEST eventflag %s %d prev_value %d", name, value, self._m_mapEventFlag[name])
            self._m_mapEventFlag[name] = value

            if name == "mob_item":
                CHARACTER_MANAGER.instance().SetMobItemRate(value)
            elif name == "mob_dam":
                CHARACTER_MANAGER.instance().SetMobDamageRate(value)
            elif name == "mob_gold":
                CHARACTER_MANAGER.instance().SetMobGoldAmountRate(value)
            elif name == "mob_gold_pct":
                CHARACTER_MANAGER.instance().SetMobGoldDropRate(value)
            elif name == "user_dam":
                CHARACTER_MANAGER.instance().SetUserDamageRate(value)
            elif name == "user_dam_buyer":
                CHARACTER_MANAGER.instance().SetUserDamageRatePremium(value)
            elif name == "mob_exp":
                CHARACTER_MANAGER.instance().SetMobExpRate(value)
            elif name == "mob_item_buyer":
                CHARACTER_MANAGER.instance().SetMobItemRatePremium(value)
            elif name == "mob_exp_buyer":
                CHARACTER_MANAGER.instance().SetMobExpRatePremium(value)
            elif name == "mob_gold_buyer":
                CHARACTER_MANAGER.instance().SetMobGoldAmountRatePremium(value)
            elif name == "mob_gold_pct_buyer":
                CHARACTER_MANAGER.instance().SetMobGoldDropRatePremium(value)
            elif name == "crcdisconnect":
                DESC_MANAGER.instance().SetDisconnectInvalidCRCMode(value != 0)
            elif not name.compare(0,5,"xmas_"):
                xmas.ProcessEventFlag(name, prev_value, value)
            elif name == "newyear_boom":
                c_ref_set = DESC_MANAGER.instance().GetClientSet()

                it = c_ref_set.begin()
                while it is not c_ref_set.end():
                    ch = it.GetCharacter()

                    if ch is None:
                        continue

                    ch.ChatPacket(EChatType.CHAT_TYPE_COMMAND, "newyear_boom %d", value)
                    it += 1
            elif name == "eclipse":
                mode = ""

                if value == 1:
                    mode = "dark"
                else:
                    mode = "light"

                c_ref_set = DESC_MANAGER.instance().GetClientSet()

                it = c_ref_set.begin()
                while it is not c_ref_set.end():
                    ch = it.GetCharacter()
                    if ch is None:
                        continue

                    ch.ChatPacket(EChatType.CHAT_TYPE_COMMAND, "DayMode %s", mode)
                    it += 1
            elif name == "day":
                c_ref_set = DESC_MANAGER.instance().GetClientSet()

                it = c_ref_set.begin()
                while it is not c_ref_set.end():
                    ch = it.GetCharacter()
                    if ch is None:
                        continue
                    if value != 0:
                        ch.ChatPacket(EChatType.CHAT_TYPE_COMMAND, "DayMode dark")
                    else:
                        ch.ChatPacket(EChatType.CHAT_TYPE_COMMAND, "DayMode light")
                    it += 1

                if value != 0 and prev_value == 0:
                    positions = [[ 1, 615, 618 ], [ 3, 500, 625 ], [ 21, 598, 665 ], [ 23, 476, 360 ], [ 41, 318, 629 ], [ 43, 478, 375 ], [ 0, 0, 0 ]]

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Pointer arithmetic is detected on this variable:
#ORIGINAL METINII C CODE: SNPCSellFireworkPosition* p = positions;
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
                    p = SNPCSellFireworkPosition(positions)
                    while p.lMapIndex:
                        if map_allow_find(p.lMapIndex):
                            posBase = pixel_position_s()
                            if not SECTREE_MANAGER.instance().GetMapBasePositionByMapIndex(p.lMapIndex, posBase):
                                #lani_err("cannot get map base position %d", p.lMapIndex)
                                p += 1
                                continue

                            CHARACTER_MANAGER.instance().SpawnMob(uint(xmas.MOB_XMAS_FIRWORK_SELLER_VNUM), p.lMapIndex, posBase.x + p.x * 100, posBase.y + p.y * 100, 0, LGEMiscellaneous.DEFINECONSTANTS.false, -1, ((not DefineConstants.false)))
                        p += 1
                elif value == 0 and prev_value != 0:
                    LaniatusDefVariables = CharacterVectorInteractor()

                    if CHARACTER_MANAGER.instance().GetCharactersByRaceNum(uint(xmas.MOB_XMAS_FIRWORK_SELLER_VNUM), i):
                        it = i.begin()

                        while it is not i.end():
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: CHARACTER_MANAGER::instance().DestroyCharacter(*it++);
                            CHARACTER_MANAGER.instance().DestroyCharacter(it)
                            it += 1
            elif name == "pre_event_hc":
                EVENTNPC = 20090

                positions = [[ 3, 588, 617 ], [ 23, 397, 250 ], [ 43, 567, 426 ], [ 0, 0, 0 ]]

                if value != 0 and prev_value == 0:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Pointer arithmetic is detected on this variable:
#ORIGINAL METINII C CODE: SEventNPCPosition* pPosition = positions;
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
                    pPosition = SEventNPCPosition(positions)

                    while pPosition.lMapIndex:
                        if map_allow_find(pPosition.lMapIndex):
                            pos = pixel_position_s()

                            if not SECTREE_MANAGER.instance().GetMapBasePositionByMapIndex(pPosition.lMapIndex, pos):
                                #lani_err("cannot get map base position %d", pPosition.lMapIndex)
                                pPosition += 1
                                continue

                            CHARACTER_MANAGER.instance().SpawnMob(EVENTNPC, pPosition.lMapIndex, pos.x+pPosition.x *100, pos.y+pPosition.y *100, 0, LGEMiscellaneous.DEFINECONSTANTS.false, -1, ((not DefineConstants.false)))
                        pPosition += 1
                elif value == 0 and prev_value != 0:
                    LaniatusDefVariables = CharacterVectorInteractor()

                    if CHARACTER_MANAGER.instance().GetCharactersByRaceNum(EVENTNPC, i):
                        it = i.begin()

                        while it is not i.end():
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: CHARACTER* ch = *it++;
                            ch = *it
                            it += 1

                            if (ch.GetMapIndex() == 3) or (ch.GetMapIndex() == 23) or (ch.GetMapIndex() == 43):
                                CHARACTER_MANAGER.instance().DestroyCharacter(ch)
            elif name == "gold_drop_limit_time":
                Globals.g_GoldDropTimeLimitValue = uint(value * 1000)
            elif name == "new_xmas_event":
                ## Laniatus Games Studio Inc. | NOTE: This static local variable declaration (not allowed in Python) has been moved just prior to the method:
                #                static uint new_santa = 20126
                if value != 0:
                    LaniatusDefVariables = CharacterVectorInteractor()
                    map1_santa_exist = LGEMiscellaneous.DEFINECONSTANTS.false
                    map21_santa_exist = LGEMiscellaneous.DEFINECONSTANTS.false
                    map41_santa_exist = LGEMiscellaneous.DEFINECONSTANTS.false

                    if CHARACTER_MANAGER.instance().GetCharactersByRaceNum(SetEventFlag_new_santa, i):
                        it = i.begin()

                        while it is not i.end():
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: CHARACTER* tch = *(it++);
                            tch = *(it)
                            it += 1

                            if tch.GetMapIndex() == 1:
                                map1_santa_exist = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
                            elif tch.GetMapIndex() == 21:
                                map21_santa_exist = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
                            elif tch.GetMapIndex() == 41:
                                map41_santa_exist = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

                    if map_allow_find(1) and not map1_santa_exist:
                        pkSectreeMap = SECTREE_MANAGER.instance().GetMap(1)
                        CHARACTER_MANAGER.instance().SpawnMob(SetEventFlag_new_santa, 1, pkSectreeMap.m_setting.iBaseX + 60800, pkSectreeMap.m_setting.iBaseY + 61700, 0, LGEMiscellaneous.DEFINECONSTANTS.false, 90, ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
                    if map_allow_find(21) and not map21_santa_exist:
                        pkSectreeMap = SECTREE_MANAGER.instance().GetMap(21)
                        CHARACTER_MANAGER.instance().SpawnMob(SetEventFlag_new_santa, 21, pkSectreeMap.m_setting.iBaseX + 59600, pkSectreeMap.m_setting.iBaseY + 61000, 0, LGEMiscellaneous.DEFINECONSTANTS.false, 110, ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
                    if map_allow_find(41) and not map41_santa_exist:
                        pkSectreeMap = SECTREE_MANAGER.instance().GetMap(41)
                        CHARACTER_MANAGER.instance().SpawnMob(SetEventFlag_new_santa, 41, pkSectreeMap.m_setting.iBaseX + 35700, pkSectreeMap.m_setting.iBaseY + 74300, 0, LGEMiscellaneous.DEFINECONSTANTS.false, 140, ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
                else:
                    LaniatusDefVariables = CharacterVectorInteractor()
                    CHARACTER_MANAGER.instance().GetCharactersByRaceNum(SetEventFlag_new_santa, i)

                    it = i.begin()
                    while it is not i.end():
                        CHARACTER_MANAGER.instance().DestroyCharacter(it)
                        it += 1

        def GetEventFlag(self, name):
            it = self._m_mapEventFlag.find(name)

            if it is self._m_mapEventFlag.end():
                return 0

            return it.second

        def BroadcastEventFlagOnLogin(self, ch):
            iEventFlagValue = None

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((iEventFlagValue = quest::CQuestManager::instance().GetEventFlag("xmas_snow")))
            if (iEventFlagValue = quest.CQuestManager.instance().GetEventFlag("xmas_snow")):
                ch.ChatPacket(EChatType.CHAT_TYPE_COMMAND, "xmas_snow %d", iEventFlagValue)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((iEventFlagValue = quest::CQuestManager::instance().GetEventFlag("xmas_boom")))
            if (iEventFlagValue = quest.CQuestManager.instance().GetEventFlag("xmas_boom")):
                ch.ChatPacket(EChatType.CHAT_TYPE_COMMAND, "xmas_boom %d", iEventFlagValue)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((iEventFlagValue = quest::CQuestManager::instance().GetEventFlag("xmas_tree")))
            if (iEventFlagValue = quest.CQuestManager.instance().GetEventFlag("xmas_tree")):
                ch.ChatPacket(EChatType.CHAT_TYPE_COMMAND, "xmas_tree %d", iEventFlagValue)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((iEventFlagValue = quest::CQuestManager::instance().GetEventFlag("day")))
            if (iEventFlagValue = quest.CQuestManager.instance().GetEventFlag("day")):
                ch.ChatPacket(EChatType.CHAT_TYPE_COMMAND, "DayMode dark")

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((iEventFlagValue = quest::CQuestManager::instance().GetEventFlag("newyear_boom")))
            if (iEventFlagValue = quest.CQuestManager.instance().GetEventFlag("newyear_boom")):
                ch.ChatPacket(EChatType.CHAT_TYPE_COMMAND, "newyear_boom %d", iEventFlagValue)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((iEventFlagValue = quest::CQuestManager::instance().GetEventFlag("eclipse")))
            if (iEventFlagValue = quest.CQuestManager.instance().GetEventFlag("eclipse")):
                mode = ""

                if iEventFlagValue == 1:
                    mode = "dark"
                else:
                    mode = "light"

                ch.ChatPacket(EChatType.CHAT_TYPE_COMMAND, "DayMode %s", mode)

        def SendEventFlagList(self, ch):
            it = m_mapEventFlag.begin()
            while it is not self._m_mapEventFlag.end():
                flagname = it.first
                value = it.second

                if (not test_server) and value == 1 and flagname == "valentine_drop":
                    ch.ChatPacket(EChatType.CHAT_TYPE_INFO, "%s %d prob 800", flagname, value)
                elif (not test_server) and value == 1 and flagname == "newyear_wonso":
                    ch.ChatPacket(EChatType.CHAT_TYPE_INFO, "%s %d prob 500", flagname, value)
                elif (not test_server) and value == 1 and flagname == "newyear_fire":
                    ch.ChatPacket(EChatType.CHAT_TYPE_INFO, "%s %d prob 1000", flagname, value)
                else:
                    ch.ChatPacket(EChatType.CHAT_TYPE_INFO, "%s %d", flagname, value)
                it += 1

        def Reload(self):
            lua_close(self._L)
            self._m_mapNPC.clear()
            self._m_mapNPCNameID.clear()
            self._m_hmQuestName.clear()
            self._m_mapTimerID.clear()
            self._m_hmQuestStartScript.clear()
            self.m_mapEventName.clear()
            self._L = None
            self.Initialize()

            it = m_registeredNPCVnum.begin()
            while it is not self._m_registeredNPCVnum.end():
                buf = str(['\0' for _ in range(256)])
                dwVnum = *it
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                snprintf(buf, sizeof(buf), "%u", dwVnum)
                self._m_mapNPC[dwVnum].Set(dwVnum, buf)
                it += 1

        def SetError(self):
            self._m_bError = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
        def ClearError(self):
            self._m_bError = LGEMiscellaneous.DEFINECONSTANTS.false
        def IsError(self):
            return self._m_bError
        def WriteRunningStateToSyserr(self):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to pointers to value types:
#ORIGINAL METINII C CODE: const char * state_name = GetQuestStateName(GetCurrentQuestName(), GetCurrentState()->st);
            state_name = self.GetQuestStateName(self.GetCurrentQuestName(), self.GetCurrentState().st)

            event_index_name = ""
            it = m_mapEventName.begin()
            while it is not self.m_mapEventName.end():
                if it.second == self._m_iRunningEventIndex:
                    event_index_name = it.first
                    break
                it += 1

            #lani_err("LUA_ERROR: quest %s.%s %s", self.GetCurrentQuestName(), state_name, event_index_name)
            if self.GetCurrentCharacterPtr() is not None and test_server:
                self.GetCurrentCharacterPtr().ChatPacket(EChatType.CHAT_TYPE_PARTY, "LUA_ERROR: quest %s.%s %s", self.GetCurrentQuestName(), state_name, event_index_name)

        def QuestError(self, func, line, fmt, *LegacyParamArray):
            szMsg = str(['\0' for _ in range(4096)])
            args = None

            ParamCount = -1
#            va_start(args, fmt)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            vsnprintf(szMsg, sizeof(szMsg), fmt, args)
#            va_end(args)

            _#lani_err(func, line, "%s", szMsg)
            if test_server:
                ch = self.GetCurrentCharacterPtr()
                if ch:
                    ch.ChatPacket(EChatType.CHAT_TYPE_PARTY, "error occurred on [%s:%d]", func,line)
                    ch.ChatPacket(EChatType.CHAT_TYPE_PARTY, "%s", szMsg)

        def RegisterNPCVnum(self, dwVnum):
            if self._m_registeredNPCVnum.find(dwVnum) != self._m_registeredNPCVnum.end():
                return

            self._m_registeredNPCVnum.insert(dwVnum)

            buf = str(['\0' for _ in range(256)])
            dir = None

            it = g_setQuestObjectDir.begin()
            while it is not g_setQuestObjectDir.end():
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to references to variables:
#ORIGINAL METINII C CODE: const str& stQuestObjectDir = *it;
                stQuestObjectDir = *it
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                snprintf(buf, sizeof(buf), "%s/%u", stQuestObjectDir, dwVnum)
                #sys_log(0, "%s", buf)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((dir = opendir(buf)))
                if (dir = opendir(buf)):
                    closedir(dir)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                    snprintf(buf, sizeof(buf), "%u", dwVnum)
                    #sys_log(0, "%s", buf)

                    self._m_mapNPC[dwVnum].Set(dwVnum, buf)
                it += 1





# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#        _GotoSelectState(qs)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#        _GotoPauseState(qs)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#        _GotoEndState(qs)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#        _GotoInputState(qs)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#        _GotoConfirmState(qs)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#        _GotoSelectItemState(qs)









        class stringhash:
## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: int operator ()(const str& str) const
            def functor_method(self, str):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Pointer arithmetic is detected on this variable:
#ORIGINAL METINII C CODE: const byte * s = (const byte*) str.c_str();
                s = byte(int(str))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to pointers to value types:
#ORIGINAL METINII C CODE: const byte * end = s + str.size();
                end = byte(s + len(str))
                h = 0

                while s < end:
                    h *= 16777619
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: h ^= (byte) *(byte *)(s++);
                    h ^= (byte) *int((s))
                    s += 1

                return h





        @staticmethod
        def ExecuteQuestScript(pc, quest_name, state, code, code_size, pChatScripts = None, bUseCache = (!LGEMiscellaneous.DefineConstants.false)):
            qs = CQuestManager.instance().OpenState(quest_name, state)
            if pChatScripts:
                qs.chat_scripts.swap(pChatScripts)

            if bUseCache:
                lua_getglobal(qs.co, "__codecache")
                lua_pushnumber(qs.co, ord(code))
                lua_rawget(qs.co, -2)

                if lua_isnil(qs.co, -1):
                    lua_pop(qs.co, 1)
                    luaL_loadbuffer(qs.co, code, code_size, quest_name)
                    lua_pushnumber(qs.co, ord(code))
                    lua_pushvalue(qs.co, -2)
                    lua_rawset(qs.co, -4)
                    lua_remove(qs.co, -2)
                else:
                    lua_remove(qs.co, -2)
            else:
                luaL_loadbuffer(qs.co, code, code_size, quest_name)

            pc.SetQuest(quest_name, qs)

            rqs = pc.GetRunningQuestState()
            if not CQuestManager.instance().RunState(rqs):
                CQuestManager.instance().CloseState(rqs)
                pc.EndRunning()
                return LGEMiscellaneous.DEFINECONSTANTS.false
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        @staticmethod
        def ExecuteQuestScript(pc, quest_index, state, code, code_size, pChatScripts = None, bUseCache = (!LGEMiscellaneous.DefineConstants.false)):
            return quest.CQuestManager.ExecuteQuestScript(pc, CQuestManager.instance().GetQuestNameByIndex(quest_index), state, code, code_size, pChatScripts, bUseCache)

        def BeginOtherPCBlock(self, pid):
            ch = self.GetCurrentCharacterPtr()
            if None is ch:
                #lani_err("NULL?")
                return

            if not self._m_vecPCStack:
                self._m_pOtherPCBlockRootPC = self.GetCurrentPC()
            self._m_vecPCStack.append(self.GetCurrentCharacterPtr().GetPlayerID())
            self.GetPC(pid)

        def EndOtherPCBlock(self):
            if len(self._m_vecPCStack) == 0:
                #lani_err("m_vecPCStack is alread empty. CurrentQuest{Name(%s), State(%s)}", self.GetCurrentQuestName(), self.GetCurrentState()._title)
                return
            pc = self._m_vecPCStack[len(self._m_vecPCStack) - 1]
            self._m_vecPCStack.pop(len(self._m_vecPCStack) - 1)
            self.GetPC(pc)

            if not self._m_vecPCStack:
                self._m_pOtherPCBlockRootPC = None

        def IsInOtherPCBlock(self):
            return self._m_vecPCStack

        def GetOtherPCBlockRootPC(self):
            return self._m_pOtherPCBlockRootPC


## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if __QUEST_RENEWAL__
        def ReadQuestCategoryToDict(self):
            if self.QuestCategoryIndexMap:
                self.QuestCategoryIndexMap.clear()

            inf = ifstream((g_stQuestDir + "/questcategory.txt").c_str())

            if not inf.is_open():
                #lani_err("QUEST Cannot open 'questcategory.txt'")
                return

            lineFromFile = ""
            while getline(inf, lineFromFile):
                if len(lineFromFile) == 0:
                    continue

                token = _boost_func_of_void.tokenizer(lineFromFile, _boost_func_of_void.escaped_list_separator('\\', '\t', '\"'))
                data = [token() for _ in range(:)]

                category_num = int(data[0])
                quest_name = data[1]

                quest_index = CQuestManager.instance().GetQuestIndexByName(quest_name)

                if test_server:
                    #sys_log(0, "QUEST_CATEGORY_LINE: %s => %s, %s", lineFromFile, data[0], quest_name)

                if quest_index != 0:
                    self.QuestCategoryIndexMap[quest_index] = category_num
                else:
                    #lani_err("QUEST could not find QuestIndex for name Quest: %s(%d)", quest_name, category_num)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if __QUEST_RENEWAL__
        def GetQuestCategoryByQuestIndex(self, q_index):
            if q_index in self.QuestCategoryIndexMap.keys():
                return self.QuestCategoryIndexMap[q_index]
            else:
                return 0
##endif

##endif

class quest: #this class replaces the original namespace 'quest'


