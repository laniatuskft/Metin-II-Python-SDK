class quest: #this class replaces the original namespace 'quest'
    class quest_server_event_info(event_info_data):

        def __init__(self):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.time_cycle = 0
            self.npc_id = 0
            self.arg = 0
            self.name = '\0'

            self.time_cycle = 0
            self.npc_id = 0
            self.arg = 0
            self.name = 0

    class quest_event_info(event_info_data):

        def __init__(self):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.time_cycle = 0
            self.player_id = 0
            self.npc_id = 0
            self.name = '\0'

            self.time_cycle = 0
            self.player_id = 0
            self.npc_id = 0
            self.name = 0

    @staticmethod
    def quest_create_server_timer_event(name, when, timernpc = uint(QUEST_NO_NPC), loop = LGEMiscellaneous.DefineConstants.false, arg = 0):
        nameCapacity = len(name) + 1

        ltime_cycle = int((rint(((when) * passes_per_sec))))

        info = Globals.AllocEventInfo()

        info.npc_id = timernpc
        info.time_cycle = ltime_cycle if loop else 0
        info.arg = arg
        info.name = LG_NEW_M2 char[nameCapacity]

        if info.name != '\0':
            strncpy_s(info.name, nameCapacity, name, _TRUNCATE)

        return event_create_ex(quest_server_timer_event, info, ltime_cycle)

    @staticmethod
    def quest_create_timer_event(name, player_id, when, npc_id = uint(QUEST_NO_NPC), loop = LGEMiscellaneous.DefineConstants.false):
        nameCapacity = len(name) + 1

        ltime_cycle = int((rint(((when) * passes_per_sec))))

        info = Globals.AllocEventInfo()

        info.player_id = player_id
        info.npc_id = npc_id
        info.name = LG_NEW_M2 char[nameCapacity]

        if info.name != '\0':
            strncpy_s(info.name, nameCapacity, name, _TRUNCATE)

        #sys_log(0, "QUEST timer name %s cycle %d pc %u npc %u loop? %d",name if name != '\0' else "<noname>", ltime_cycle, player_id, npc_id,1 if loop else 0)

        info.time_cycle = ltime_cycle if loop else 0
        return event_create_ex(quest_timer_event, info, ltime_cycle)

    @staticmethod
    def CancelTimerEvent(ppEvent):
        info = if isinstance(ppEvent.info, quest_event_info) else None

        if info:
            LG_DEL_MEM_ARRAY(info.name)
            info.name = None

        event_cancel(ppEvent)


class quest: #this class replaces the original namespace 'quest'

    @staticmethod
    def (UnnamedParameter):
        info = if isinstance(event.info, quest_server_event_info) else None

        if info is None:
            #lani_err("quest_server_timer_event> <Factor> Null pointer")
            return 0

        q = quest.CQuestManager.instance()

        if not q.ServerTimer(info.npc_id, info.arg):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
            return passes_per_sec / 2 + 1

        if 0 == info.time_cycle:
            q.ClearServerTimerNotCancel(info.name, info.arg)
            LG_DEL_MEM_ARRAY(info.name)
            info.name = None

        return info.time_cycle

    @staticmethod
    def (UnnamedParameter):
        info = if isinstance(event.info, quest_event_info) else None
        if info is None:
            #lani_err("quest_timer_event> <Factor> Null pointer")
            return 0

        q = quest.CQuestManager.instance()

        if CHARACTER_MANAGER.instance().FindByPID(info.player_id):
            if not quest.CQuestManager.instance().Timer(info.player_id, info.npc_id):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
                return (passes_per_sec / 2 + 1)

            if info.time_cycle != 0:
                return info.time_cycle

        if info.name is not None:
            pPC = q.GetPC(info.player_id)
            if pPC:
                pPC.RemoveTimerNotCancel(info.name)
            else:
                #lani_err("quest::PC pointer null. player_id: %u", info.player_id)

            LG_DEL_MEM_ARRAY(info.name)
            info.name = None
        return 0
