from enum import Enum

## Laniatus Games Studio Inc. | NOTE: The following #define macro was replaced in-line:
#ORIGINAL METINII C CODE: #define INDUCTION_LEVEL3 (1 << 0)
## Laniatus Games Studio Inc. | NOTE: The following #define macro was replaced in-line:
#ORIGINAL METINII C CODE: #define INDUCTION_LEVEL8 (1 << 1)
## Laniatus Games Studio Inc. | NOTE: The following #define macro was replaced in-line:
#ORIGINAL METINII C CODE: #define INDUCTION_LEVEL2 (1 << 2)
## Laniatus Games Studio Inc. | WARNING: The following #include directive was ignored:
##include <lua/lua.hpp>

class quest: #this class replaces the original namespace 'quest'
    QUEST_NO_NPC = 0
    QUEST_ATTR_NPC_START = 100000
    QUEST_ATTR0_NPC = QUEST_ATTR_NPC_START
    QUEST_ATTR1_NPC = 100000
    QUEST_ATTR2_NPC = 100001
    QUEST_ATTR3_NPC = 100002
    QUEST_ATTR4_NPC = 100003
    QUEST_ATTR5_NPC = 100004
    QUEST_ATTR6_NPC = 100005
    QUEST_ATTR7_NPC = 100006
    QUEST_ATTR8_NPC = 100007
    QUEST_ATTR9_NPC = 100008
    QUEST_ATTR10_NPC = 100009
    QUEST_ATTR11_NPC = 100010
    QUEST_ATTR12_NPC = 100011
    QUEST_ATTR13_NPC = 100012
    QUEST_ATTR14_NPC = 100013
    QUEST_ATTR15_NPC = 100014

    QUEST_CLICK_EVENT = 0
    QUEST_KILL_EVENT = 1
    QUEST_TIMER_EVENT = 2
    QUEST_LEVELUP_EVENT = 3
    QUEST_LOGIN_EVENT = 4
    QUEST_LOGOUT_EVENT = 5
    QUEST_BUTTON_EVENT = 6
    QUEST_INFO_EVENT = 7
    QUEST_CHAT_EVENT = 8
    QUEST_ATTR_IN_EVENT = 9
    QUEST_ATTR_OUT_EVENT = 10
    QUEST_ITEM_USE_EVENT = 11
    QUEST_SERVER_TIMER_EVENT = 12
    QUEST_ENTER_STATE_EVENT = 13
    QUEST_LEAVE_STATE_EVENT = 14
    QUEST_LETTER_EVENT = 15
    QUEST_ITEM_TAKE_EVENT = 16
    QUEST_TARGET_EVENT = 17
    QUEST_PARTY_KILL_EVENT = 18
    QUEST_UNMOUNT_EVENT = 19
    QUEST_ITEM_PICK_EVENT = 20
    QUEST_SIG_USE_EVENT = 21
    QUEST_ITEM_INFORMER_EVENT = 22
    QUEST_EVENT_COUNT = 23

    SUSPEND_STATE_NONE = 0
    SUSPEND_STATE_PAUSE = 1
    SUSPEND_STATE_SELECT = 2
    SUSPEND_STATE_INPUT = 3
    SUSPEND_STATE_CONFIRM = 4
    SUSPEND_STATE_SELECT_ITEM = 5

    class EQuestConfirmType(Enum):
        CONFIRM_NO = 0
        CONFIRM_YES = 1
        CONFIRM_TIMEOUT = 2

    class AStateScriptType:

        def __init__(self):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.m_code = []

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: int GetSize() const
        def GetSize(self):
            return len(self.m_code)
## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: const char* GetCode() const
        def GetCode(self):
            return self.m_code[0]


    class AArgScript:

        def __init__(self):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.arg = ""
            self.when_condition = []
            self.script = AStateScriptType()
            self.quest_index = 0
            self.state_index = 0

            self.quest_index = 0
            self.state_index = 0

    class QuestState:



        def __init__(self):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.co = None
            self.ico = 0
            self.args = 0
            self.suspend_state = 0
            self.iIndex = 0
            self.bStart = False
            self.st = 0
            self._title = ""
            self._clock_name = ""
            self._counter_name = ""
            self._clock_value = 0
            self._counter_value = 0
            self._icon_file = ""
            self.chat_scripts = []

            self.co = None
            self.ico = 0
            self.args = 0
            self.suspend_state = SUSPEND_STATE_NONE
            self.iIndex = 0
            self.bStart = False
            self.st = -1
            self._clock_value = 0
            self._counter_value = 0
