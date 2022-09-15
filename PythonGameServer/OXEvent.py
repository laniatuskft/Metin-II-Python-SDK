from enum import Enum

class tag_Quiz:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.level = '\0'
        self.Quiz = str(['\0' for _ in range(256)])
        self.answer = False


class OXEventStatus(Enum):
    OXEVENT_FINISH = 0
    OXEVENT_OPEN = 1
    OXEVENT_CLOSE = 2
    OXEVENT_QUIZ = 3

    OXEVENT_ERR = 0XFF

class COXEventManager(singleton):

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self._m_map_char = {}
        self._m_map_attender = {}
        self._m_map_miss = {}
        self._m_vec_quiz = []
        self._m_timedEvent = _boost_func_of_void.intrusive_ptr()




# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    CheckAnswer()

    def EnterAudience(self, pkChar):
        pid = pkChar.GetPlayerID()

        self._m_map_char.update({pid: pid})

        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def EnterAttender(self, pkChar):
        pid = pkChar.GetPlayerID()

        self._m_map_char.update({pid: pid})
        self._m_map_attender.update({pid: pid})

        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def Initialize(self):
        self._m_timedEvent = None
        self._m_map_char.clear()
        self._m_map_attender.clear()
        self._m_vec_quiz.clear()

        self.SetStatus(OXEventStatus.OXEVENT_FINISH)

        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def Destroy(self):
        self.CloseEvent()

        self._m_map_char.clear()
        self._m_map_attender.clear()
        self._m_vec_quiz.clear()

        self.SetStatus(OXEventStatus.OXEVENT_FINISH)

    def GetStatus(self):
        ret = byte(quest.CQuestManager.instance().GetEventFlag("oxevent_status"))

        if ret == 0:
            return OXEventStatus.OXEVENT_FINISH

        if (ret == 0) or (ret == 1):
            return OXEventStatus.OXEVENT_OPEN

        if (ret == 0) or (ret == 1) or (ret == 2):
            return OXEventStatus.OXEVENT_CLOSE

        if (ret == 0) or (ret == 1) or (ret == 2) or (ret == 3):
            return OXEventStatus.OXEVENT_QUIZ


        if True:
            return OXEventStatus.OXEVENT_ERR

        return OXEventStatus.OXEVENT_ERR

    def SetStatus(self, status):
        val = 0

        if status == OXEventStatus.OXEVENT_OPEN:
            val = 1

        elif status == OXEventStatus.OXEVENT_CLOSE:
            val = 2

        elif status == OXEventStatus.OXEVENT_QUIZ:
            val = 3


        if status != OXEVENT_OPEN and status != OXEVENT_CLOSE and status != OXEVENT_QUIZ:
            val = 0
        quest.CQuestManager.instance().RequestSetEventFlag("oxevent_status", val)

# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    LoadQuizScript(szFileName)

    def Enter(self, pkChar):
        if self.GetStatus() == OXEventStatus.OXEVENT_FINISH:
            #sys_log(0, "OXEVENT : map finished. but char enter. %s", pkChar.GetName(LOCALE_LANIATUS))
            return LGEMiscellaneous.DEFINECONSTANTS.false

        pos = pkChar.GetXYZ()

        if pos.x == 896500 and pos.y == 24600:
            return self.EnterAttender(pkChar)
        elif pos.x == 896300 and pos.y == 28900:
            return self.EnterAudience(pkChar)
        else:
            #sys_log(0, "OXEVENT : wrong pos enter %d %d", pos.x, pos.y)
            return LGEMiscellaneous.DEFINECONSTANTS.false

        return LGEMiscellaneous.DEFINECONSTANTS.false

    def CloseEvent(self):
        if self._m_timedEvent is not None:
            event_cancel(self._m_timedEvent)

        iter = self._m_map_char.begin()

        pkChar = None
        while iter is not self._m_map_char.end():
            pkChar = CHARACTER_MANAGER.instance().FindByPID(iter.second)

            if pkChar is not None:
                pkChar.WarpSet(int(Globals.EMPIRE_START_X(pkChar.GetEmpire())), int(Globals.EMPIRE_START_Y(pkChar.GetEmpire())), 0)
            iter += 1

        self._m_map_char.clear()

        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def ClearQuiz(self):
        i = 0
        while i < len(self._m_vec_quiz):
            self._m_vec_quiz[i].clear()
            i += 1

        self._m_vec_quiz.clear()

    def AddQuiz(self, level, pszQuestion, answer):
        if len(self._m_vec_quiz) < int(level) + 1:
            self._m_vec_quiz.resize(level + 1)

        tmpQuiz = tag_Quiz()

        tmpQuiz.level = level
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        strncpy_s(tmpQuiz.Quiz, sizeof(tmpQuiz.Quiz), pszQuestion, _TRUNCATE)
        tmpQuiz.answer = answer

        self._m_vec_quiz[level].append(tmpQuiz)
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def ShowQuizList(self, pkChar):
        c = 0

        i = 0
        while i < len(self._m_vec_quiz):
            j = 0
            while j < len(self._m_vec_quiz[i]):
                pkChar.ChatPacket(EChatType.CHAT_TYPE_INFO, "%d %s %s", self._m_vec_quiz[i][j].level, self._m_vec_quiz[i][j].Quiz,LC_TEXT("��") if self._m_vec_quiz[i][j].answer else LC_TEXT("FALSE"))
                j += 1
                c += 1
            i += 1

        pkChar.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Total number of the Quiz: %d "), c)
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def Quiz(self, level, timelimit):
        if len(self._m_vec_quiz) == 0:
            return LGEMiscellaneous.DEFINECONSTANTS.false
        if level > len(self._m_vec_quiz):
            level = len(self._m_vec_quiz) - 1
        if len(self._m_vec_quiz[level]) <= 0:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if timelimit < 0:
            timelimit = 30

        idx = number(0, len(self._m_vec_quiz[level])-1)

        SendNoticeMap(LC_TEXT("Question."), LGEMiscellaneous.DEFINECONSTANTS.OXEVENT_MAP_INDEX, ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
        SendNoticeMap(self._m_vec_quiz[level][idx].Quiz, LGEMiscellaneous.DEFINECONSTANTS.OXEVENT_MAP_INDEX, ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
        SendNoticeMap(LC_TEXT("If it's correct walk to O, if it's wrong walk to X"), LGEMiscellaneous.DEFINECONSTANTS.OXEVENT_MAP_INDEX, ((not LGEMiscellaneous.DEFINECONSTANTS.false)))

        if self._m_timedEvent is not None:
            event_cancel(self._m_timedEvent)

        answer = Globals.AllocEventInfo()

        answer.answer = self._m_vec_quiz[level][idx].answer

        timelimit -= 15
        self._m_timedEvent = event_create_ex(oxevent_timer, answer, ((timelimit) * passes_per_sec))

        self.SetStatus(OXEventStatus.OXEVENT_QUIZ)

        self._m_vec_quiz[level].pop(idx)
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def GiveItemToAttender(self, dwItemVnum, count):
        iter = self._m_map_attender.begin()

        while iter is not self._m_map_attender.end():
            pkChar = CHARACTER_MANAGER.instance().FindByPID(iter.second)

            if pkChar:
                pkChar.AutoGiveItem(dwItemVnum, count, -1, ((not DefineConstants.false)))
            iter += 1

        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def CheckAnswer(self, answer):
        if len(self._m_map_attender) <= 0:
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        iter = self._m_map_attender.begin()

        self._m_map_miss.clear()

        rect = [0 for _ in range(4)]
        if answer != ((not LGEMiscellaneous.DEFINECONSTANTS.false)):
            rect[0] = 892600
            rect[1] = 22900
            rect[2] = 896300
            rect[3] = 26400
        else:
            rect[0] = 896600
            rect[1] = 22900
            rect[2] = 900300
            rect[3] = 26400

        pkChar = None
        pos = pixel_position_s()
        while iter is not self._m_map_attender.end():
            pkChar = CHARACTER_MANAGER.instance().FindByPID(iter.second)
            if pkChar is not None:
## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: pos = pkChar->GetXYZ();
                pos.copy_from(pkChar.GetXYZ())

                if pos.x < rect[0] or pos.x > rect[2] or pos.y < rect[1] or pos.y > rect[3]:
                    pkChar.EffectPacket(SPECIAL_EFFECT.SE_FAIL)
                    iter_tmp = iter
                    iter += 1
                    self._m_map_attender.pop(iter_tmp)
                    self._m_map_miss.update({pkChar.GetPlayerID(): pkChar.GetPlayerID()})
                else:
                    pkChar.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Correct!"))
                    chatbuf = str(['\0' for _ in range(256)])
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                    len = snprintf(chatbuf, sizeof(chatbuf), "%s %u %u","cheer1" if number(0, 1) == 1 else "cheer2", pkChar.GetVID(), 0)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                    if len < 0 or len >= int(sizeof(chatbuf)):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                        len = sizeof(chatbuf) - 1

                    len += 1

                    pack_chat = packet_chat()
                    pack_chat.header = byte(Globals.LG_HEADER_GC_CHAT)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                    pack_chat.size = sizeof(packet_chat) + len
                    pack_chat.type = EChatType.CHAT_TYPE_COMMAND
                    pack_chat.id = 0

                    buf = TEMP_BUFFER(8192, DefineConstants.false)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                    buf.write(pack_chat, sizeof(packet_chat))
                    buf.write(chatbuf, len)

                    pkChar.PacketAround(buf.read_peek(), buf.size())
                    pkChar.EffectPacket(SPECIAL_EFFECT.SE_SUCCESS)

                    iter += 1
            else:
                err = self._m_map_char.find(iter.first)
                if err is not self._m_map_char.end():
                    self._m_map_char.pop(err)

                err2 = self._m_map_miss.find(iter.first)
                if err2 is not self._m_map_miss.end():
                    self._m_map_miss.pop(err2)

                iter_tmp = iter
                iter += 1
                self._m_map_attender.pop(iter_tmp)
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def WarpToAudience(self):
        if len(self._m_map_miss) <= 0:
            return

        iter = self._m_map_miss.begin()
        pkChar = None

        while iter is not self._m_map_miss.end():
            pkChar = CHARACTER_MANAGER.instance().FindByPID(iter.second)

            if pkChar is not None:
                if number(0, 3) == 0:
                    pkChar.Show(LGEMiscellaneous.DEFINECONSTANTS.OXEVENT_MAP_INDEX, 896300, 28900, LONG_MAX, DefineConstants.false)
                elif number(0, 3) == 1:
                    pkChar.Show(LGEMiscellaneous.DEFINECONSTANTS.OXEVENT_MAP_INDEX, 890900, 28100, LONG_MAX, DefineConstants.false)
                elif number(0, 3) == 2:
                    pkChar.Show(LGEMiscellaneous.DEFINECONSTANTS.OXEVENT_MAP_INDEX, 896600, 20500, LONG_MAX, DefineConstants.false)
                elif number(0, 3) == 3:
                    pkChar.Show(LGEMiscellaneous.DEFINECONSTANTS.OXEVENT_MAP_INDEX, 902500, 28100, LONG_MAX, DefineConstants.false)
                else:
                    pkChar.Show(LGEMiscellaneous.DEFINECONSTANTS.OXEVENT_MAP_INDEX, 896300, 28900, LONG_MAX, DefineConstants.false)
            iter += 1

        self._m_map_miss.clear()

    def LogWinner(self):
        iter = self._m_map_attender.begin()

        while iter is not self._m_map_attender.end():
            pkChar = CHARACTER_MANAGER.instance().FindByPID(iter.second)
            iter += 1

        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def GetAttenderCount(self):
        return len(self._m_map_attender)

class OXEventInfoData(event_info_data):

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.answer = False

        self.answer = LGEMiscellaneous.DEFINECONSTANTS.false