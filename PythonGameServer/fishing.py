from fishing import *

import math

class fishing: #this class replaces the original namespace 'fishing'
    CAMPFIRE_MOB = 12000
    FISHER_MOB = 9009
    FISH_MIND_PILL_VNUM = 27610

    class fishing_event_info(event_info_data):

        def __init__(self):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.pid = 0
            self.step = 0
            self.hang_time = 0
            self.fish_id = 0

            self.pid = 0
            self.step = 0
            self.hang_time = 0
            self.fish_id = 0

    @staticmethod
    def Initialize():
        fish_info_bak = [SFishInfo() for _ in range(fishing.MAX_FISH)]
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memcpy' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memcpy(fish_info_bak, fishing.fish_info, sizeof(fishing.fish_info))

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memset(fishing.fish_info, 0, sizeof(fishing.fish_info))

        FILE_NAME_LEN = 256
        szFishingFileName = str(['\0' for _ in range(FILE_NAME_LEN+1)])
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        snprintf(szFishingFileName, sizeof(szFishingFileName), "%s/fishing.txt", LocaleService_GetBasePath().c_str())
        fp = fopen(szFishingFileName, "r")

        if fish_info_bak[0].name[0] != '\0':
            SendLog("Reloading fish table.")

        if fp is None:
            SendLog("error! cannot open fishing.txt")

            if fish_info_bak[0].name[0] != '\0':
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memcpy' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                memcpy(fishing.fish_info, fish_info_bak, sizeof(fishing.fish_info))
                SendLog("  restoring to backup")
            return

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memset(fishing.fish_info, 0, sizeof(fishing.fish_info))

        buf = str(['\0' for _ in range(512)])
        idx = 0

        while fgets(buf, 512, fp):
            if buf[0] == '#':
                continue

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to pointers to value types:
#ORIGINAL METINII C CODE: char * p = strrchr(buf, '\n');
            p = strrchr(buf, '\n')
            p = '\0'

            start = buf
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to pointers to value types:
#ORIGINAL METINII C CODE: const char * tab = strchr(start, '\t');
            tab = strchr(start, '\t')

            if (not tab) != '\0':
                print("Tab error on line: {0}\n".format(buf), end = '')
                SendLog("error! parsing fishing.txt")

                if fish_info_bak[0].name[0] != '\0':
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memcpy' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                    memcpy(fishing.fish_info, fish_info_bak, sizeof(fishing.fish_info))
                    SendLog("  restoring to backup")
                break

            szCol = str(['\0' for _ in range(256)])
            szCol2 = str(['\0' for _ in range(256)])
            iColCount = 0

            condition = True
            while condition:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                strncpy_s(szCol2, MIN(sizeof(szCol2), (tab - start) + 1), start, _TRUNCATE)
                szCol2[tab-start] = '\0'

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                trim_and_lower(szCol2, szCol, sizeof(szCol))

                if (not szCol[0]) != '\0' or szCol[0] == '\t':
                    iColCount += 1
                else:
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: case 0:
                    if iColCount == 0:
                            iColCount += 1
                        else:
                            iColCount += 1
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                        strncpy_s(fishing.fish_info[idx].name, sizeof(fishing.fish_info[idx].name), szCol, _TRUNCATE)
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: case 1:
                    elif iColCount == 1:
                            iColCount += 1
                        else:
                            iColCount += 1
                        Globals.str_to_number((fishing.fish_info[idx].vnum) != 0, szCol)
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: case 2:
                    elif iColCount == 2:
                            iColCount += 1
                        else:
                            iColCount += 1
                        Globals.str_to_number((fishing.fish_info[idx].dead_vnum) != 0, szCol)
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: case 3:
                    elif iColCount == 3:
                            iColCount += 1
                        else:
                            iColCount += 1
                        Globals.str_to_number((fishing.fish_info[idx].grill_vnum) != 0, szCol)
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: case 4:
                    elif iColCount == 4:
                            iColCount += 1
                        else:
                            iColCount += 1
                        Globals.str_to_number((fishing.fish_info[idx].prob[0]) != 0, szCol)
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: case 5:
                    elif iColCount == 5:
                            iColCount += 1
                        else:
                            iColCount += 1
                        Globals.str_to_number((fishing.fish_info[idx].prob[1]) != 0, szCol)
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: case 6:
                    elif iColCount == 6:
                            iColCount += 1
                        else:
                            iColCount += 1
                        Globals.str_to_number((fishing.fish_info[idx].prob[2]) != 0, szCol)
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: case 7:
                    elif iColCount == 7:
                            iColCount += 1
                        else:
                            iColCount += 1
                        Globals.str_to_number((fishing.fish_info[idx].prob[3]) != 0, szCol)
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: case 8:
                    elif iColCount == 8:
                            iColCount += 1
                        else:
                            iColCount += 1
                        Globals.str_to_number((fishing.fish_info[idx].difficulty) != 0, szCol)
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: case 9:
                    elif iColCount == 9:
                            iColCount += 1
                        else:
                            iColCount += 1
                        Globals.str_to_number((fishing.fish_info[idx].time_type) != 0, szCol)
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: case 10:
                    elif iColCount == 10:
                            iColCount += 1
                        else:
                            iColCount += 1
                        Globals.str_to_number((fishing.fish_info[idx].length_range[0]) != 0, szCol)
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: case 11:
                    elif iColCount == 11:
                            iColCount += 1
                        else:
                            iColCount += 1
                        Globals.str_to_number((fishing.fish_info[idx].length_range[1]) != 0, szCol)
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: case 12:
                    elif iColCount == 12:
                            iColCount += 1
                        else:
                            iColCount += 1
                        Globals.str_to_number((fishing.fish_info[idx].length_range[2]) != 0, szCol)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: case 22:
                    elif (iColCount++ == 13) or (iColCount++ == 14) or (iColCount++ == 15) or (iColCount++ == 16) or (iColCount++ == 17) or (iColCount++ == 18) or (iColCount++ == 19) or (iColCount++ == 20) or (iColCount++ == 21) or (iColCount++ == 22):
                        Globals.str_to_number((fishing.fish_info[idx].used_table[iColCount-1-12]) != 0, szCol)

                start = tab + 1
                tab = strchr(start, '\t')
                condition = tab

            idx += 1

            if idx == fishing.MAX_FISH:
                break

        fclose(fp)

        for i in range(0, fishing.MAX_FISH):
            #sys_log(0, "FISH: %-24s vnum %5lu prob %4d %4d %4d %4d len %d %d %d", fishing.fish_info[i].name, fishing.fish_info[i].vnum, fishing.fish_info[i].prob[0], fishing.fish_info[i].prob[1], fishing.fish_info[i].prob[2], fishing.fish_info[i].prob[3], fishing.fish_info[i].length_range[0], fishing.fish_info[i].length_range[1], fishing.fish_info[i].length_range[2])

        for j in range(0, fishing.MAX_PROB):
            fishing.g_prob_accumulate[j][0] = fishing.fish_info[0].prob[j]

            for i in range(1, fishing.MAX_FISH):
                fishing.g_prob_accumulate[j][i] = fishing.fish_info[i].prob[j] + fishing.g_prob_accumulate[j][i - 1]

            fishing.g_prob_sum[j] = fishing.g_prob_accumulate[j][fishing.MAX_FISH - 1]
            #sys_log(0, "FISH: prob table %d %d", j, fishing.g_prob_sum[j])

    @staticmethod
    def CreateFishingEvent(ch):
        info = Globals.AllocEventInfo()
        info.pid = ch.GetPlayerID()
        info.step = 0
        info.hang_time = 0

        time = number(10, 40)

        p = packet_fishing()
        p.header = byte(Globals.LG_HEADER_GC_FISHING)
        p.subheader = byte(Globals.FISHING_SUBLG_HEADER_GC_START)
        p.info = ch.GetVID()
        p.dir = byte(int((ch.GetRotation()/5)))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        ch.PacketAround(p, sizeof(packet_fishing))

        return event_create_ex(fishing_event, info, ((time) * passes_per_sec))

    @staticmethod
    def Take(info, ch):
        if info.step == 1:
            ms = int(((get_dword_time() - info.hang_time)))
            item_vnum = 0
            ret = fishing.Compute(uint(info.fish_id), uint(ms), item_vnum, fishing.GetFishingLevel(ch))

            if (ret == -2) or (ret == -3) or (ret == -1):
                    map_idx = ch.GetMapIndex()
                    prob_idx = fishing.GetProbIndexByMapIndex(map_idx)
                fishing.FishingFail(ch)

            elif ret == 0:
                if item_vnum != 0:
                    fishing.FishingSuccess(ch)

                    p = packet_fishing()
                    p.header = byte(Globals.LG_HEADER_GC_FISHING)
                    p.subheader = byte(Globals.FISHING_SUBLG_HEADER_GC_FISH)
                    p.info = item_vnum
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                    ch.GetDesc().Packet(p, sizeof(packet_fishing))

                    item = ch.AutoGiveItem(item_vnum, 1, -1, LGEMiscellaneous.DEFINECONSTANTS.false)
                    if item:
                        item.SetSocket(0, fishing.GetFishLength(info.fish_id), ((not DefineConstants.false)))
                        if test_server:
                            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("The length of the captured fish is %.2fcm."), item.GetSocket(0)/100.0)

                        if quest.CQuestManager.instance().GetEventFlag("fishevent") > 0 and (info.fish_id == 5 or info.fish_id == 6):
                            p = SPacketGDHighscore()
                            p.dwPID = ch.GetPlayerID()
                            p.lValue = item.GetSocket(0)

                            if info.fish_id == 5:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                                strncpy_s(p.szBoard, sizeof(p.szBoard), LC_TEXT("Fishing Event Great Zander?"), _TRUNCATE)
                            elif info.fish_id == 6:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                                strncpy_s(p.szBoard, sizeof(p.szBoard), LC_TEXT("Fishing Event carp"), _TRUNCATE)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                            db_clientdesc.DBPacket(Globals.LG_HEADER_GD_HIGHSCORE_REGISTER, 0, p, sizeof(SPacketGDHighscore))

                    map_idx = ch.GetMapIndex()
                    prob_idx = fishing.GetProbIndexByMapIndex(map_idx)

                else:
                    map_idx = ch.GetMapIndex()
                    prob_idx = fishing.GetProbIndexByMapIndex(map_idx)
                    fishing.FishingFail(ch)
        elif info.step > 1:
            map_idx = ch.GetMapIndex()
            prob_idx = fishing.GetProbIndexByMapIndex(map_idx)
            fishing.FishingFail(ch)
        else:
            p = packet_fishing()
            p.header = byte(Globals.LG_HEADER_GC_FISHING)
            p.subheader = byte(Globals.FISHING_SUBLG_HEADER_GC_STOP)
            p.info = ch.GetVID()
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            ch.PacketAround(p, sizeof(p))

        if info.step != 0:
            fishing.FishingPractice(ch)

    @staticmethod
    def Simulation(level, count, prob_idx, ch):
        fished = {}
        total_count = 0

        for i in range(0, count):
            fish_id = fishing.DetermineFishByProbIndex(prob_idx)
            item = 0
            temp_ref_item = RefObject(item);
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
            fishing.Compute(uint(fish_id), (number(2000, 4000) + number(2000,4000)) / 2, temp_ref_item, level)
            item = temp_ref_item.arg_value

            if item != 0:
                fished[fishing.fish_info[fish_id].name] += 1
                total_count += 1

        it = fished.begin()
        while it is not fished.end():
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("%s: %d"), it.first.c_str(), it.second)
            it += 1

        ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You caught %d of %d ."), len(fished), total_count)

    ## Laniatus Games Studio Inc. | NOTE: This was formerly a static local variable declaration (not allowed in Python):
    UseFish_s_acc_prob = [1000, 1500, 1800, 1900, 1950, 1980, 1990, 1995, 1999, 2000] + [0 for _ in range(NUM_USE_RESULT_COUNT - 10)]

    @staticmethod
    def UseFish(ch, item):
        idx = int(item.GetVnum() - fishing.fish_info[2].vnum+2)

        if idx<=1 or idx >= fishing.MAX_FISH:
            return

        r = number(1, 10000)

        item.SetCount(item.GetCount()-1)

        if r >= 4001:
            ch.AutoGiveItem(fishing.fish_info[idx].dead_vnum, 1, -1, ((not DefineConstants.false)))
        elif r >= 2001:
            ch.AutoGiveItem(fishing.FISH_BONE_VNUM)
        else:
            ## Laniatus Games Studio Inc. | NOTE: This static local variable declaration (not allowed in Python) has been moved just prior to the method:
            #            static int s_acc_prob[NUM_USE_RESULT_COUNT] = { 1000, 1500, 1800, 1900, 1950, 1980, 1990, 1995, 1999, 2000 }
            u_index = std::lower_bound(UseFish_s_acc_prob, UseFish_s_acc_prob + fishing.NUM_USE_RESULT_COUNT, r) - UseFish_s_acc_prob

            if (fishing.fish_info[idx].used_table[u_index] == fishing.USED_TREASURE_MAP) or (fishing.fish_info[idx].used_table[u_index] == fishing.USED_NONE) or (fishing.fish_info[idx].used_table[u_index] == fishing.USED_WATER_STONE):
                ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("The fish vanished into the deep water."))

            elif fishing.fish_info[idx].used_table[u_index] == fishing.USED_SHELLFISH:
                ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("There is a Shell inside the fish."))
                ch.AutoGiveItem(fishing.SHELLFISH_VNUM)

            elif fishing.fish_info[idx].used_table[u_index] == fishing.USED_EARTHWARM:
                ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("There is a Worm inside the fish."))
                ch.AutoGiveItem(fishing.EARTHWORM_VNUM)

            else:
                ch.AutoGiveItem(fishing.fish_info[idx].used_table[u_index])

    @staticmethod
    def Grill(ch, item):
        idx = -1
        vnum = item.GetVnum()
        if vnum >= 27803 and vnum <= 27830:
            idx = int(vnum - 27800)
        if vnum >= 27833 and vnum <= 27860:
            idx = int(vnum - 27830)
        if idx == -1:
            return

        count = int(item.GetCount())

        ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You put %s through the hoops."), item.GetName(LOCALE_LANIATUS))
        item.SetCount(0)
        ch.AutoGiveItem(fishing.fish_info[idx].grill_vnum, count)

    @staticmethod
    def RefinableRod(rod):
        if rod.GetType() != EItemTypes.ITEM_ROD:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if rod.IsEquipped():
            return LGEMiscellaneous.DEFINECONSTANTS.false

        return (rod.GetSocket(0) == rod.GetValue(2))

    @staticmethod
    def RealRefineRod(ch, item):
        if ch is None or item is None:
            return 2

        if not fishing.RefinableRod(item):
            #lani_err("REFINE_ROD_HACK pid(%u) item(%s:%d)", ch.GetPlayerID(), item.GetName(LOCALE_LANIATUS), item.GetID())
            return 2

        rod = item

        iAdv = math.trunc(rod.GetValue(0) / float(10))

        if number(1,100) <= rod.GetValue(3):
            pkNewItem = ITEM_MANAGER.instance().CreateItem(rod.GetRefinedVnum(), 1, 0, DefineConstants.false, -1, DefineConstants.false)

            if pkNewItem:
                wCell = rod.GetCell()
                ITEM_MANAGER.instance().RemoveItem(rod, "REMOVE (REFINE FISH_ROD)")
                pkNewItem.AddToCharacter(ch, TItemPos(EWindows.INVENTORY, wCell))
                return 1

            return 2
        else:
            pkNewItem = ITEM_MANAGER.instance().CreateItem(uint(rod.GetValue(4)), 1, 0, DefineConstants.false, -1, DefineConstants.false)
            if pkNewItem:
                wCell = rod.GetCell()
                ITEM_MANAGER.instance().RemoveItem(rod, "REMOVE (REFINE FISH_ROD)")
                pkNewItem.AddToCharacter(ch, TItemPos(EWindows.INVENTORY, wCell))
                return 0

            return 2


## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if ! __FISHING_MAIN__
##endif

class fishing: #this class replaces the original namespace 'fishing'
    MAX_FISH = 37
    NUM_USE_RESULT_COUNT = 10
    FISH_BONE_VNUM = 27799
    SHELLFISH_VNUM = 27987
    EARTHWORM_VNUM = 27801
    WATER_STONE_VNUM_BEGIN = 28030
    WATER_STONE_VNUM_END = 28045
    FISH_NAME_MAX_LEN = 64
    MAX_PROB = 4

    USED_NONE = 0
    USED_SHELLFISH = 1
    USED_WATER_STONE = 2
    USED_TREASURE_MAP = 3
    USED_EARTHWARM = 4
    MAX_USED_FISH = 5



    FISHING_TIME_NORMAL = 0
    FISHING_TIME_SLOW = 1
    FISHING_TIME_QUICK = 2
    FISHING_TIME_ALL = 3
    FISHING_TIME_EASY = 4
    FISHING_TIME_COUNT = 5
    MAX_FISHING_TIME_COUNT = 31

    FISHING_LIMIT_NONE = 0
    FISHING_LIMIT_APPEAR = 1

    aFishingTime = [[ 0, 0, 0, 0, 0, 2, 4, 8, 12, 16, 20, 22, 25, 30, 50, 80, 50, 30, 25, 22, 20, 16, 12, 8, 4, 2, 0, 0, 0, 0, 0 ], [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 8, 12, 16, 20, 22, 25, 30, 50, 80, 50, 30, 25, 22, 20 ], [ 20, 22, 25, 30, 50, 80, 50, 30, 25, 22, 20, 16, 12, 8, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], [ 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100 ], [ 20, 20, 20, 20, 20, 22, 24, 28, 32, 36, 40, 42, 45, 50, 70, 100, 70, 50, 45, 42, 40, 36, 32, 28, 24, 22, 20, 20, 20, 20, 20 ]]

    class SFishInfo:

        def __init__(self):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.name = str(['\0' for _ in range(FISH_NAME_MAX_LEN)])
            self.vnum = 0
            self.dead_vnum = 0
            self.grill_vnum = 0
            self.prob = [0 for _ in range(MAX_PROB)]
            self.difficulty = 0
            self.time_type = 0
            self.length_range = [0 for _ in range(3)]
            self.used_table = [0 for _ in range(NUM_USE_RESULT_COUNT)]


    def less_than(self, lhs, rhs):
        return lhs.vnum < rhs.vnum

    g_prob_sum = [0 for _ in range(MAX_PROB)]
    g_prob_accumulate = [[] for _ in range(MAX_PROB)]

    fish_info = [SFishInfo("\0")]

    @staticmethod
    def DetermineFishByProbIndex(prob_idx):
        rv = number(1, fishing.g_prob_sum[prob_idx])
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to pointers to value types:
#ORIGINAL METINII C CODE: int * p = std::lower_bound(g_prob_accumulate[prob_idx], g_prob_accumulate[prob_idx]+ MAX_FISH, rv);
        p = std::lower_bound(fishing.g_prob_accumulate[prob_idx], fishing.g_prob_accumulate[prob_idx]+ fishing.MAX_FISH, rv)
        fish_idx = p - fishing.g_prob_accumulate[prob_idx]
        return fish_idx

    @staticmethod
    def GetProbIndexByMapIndex(index):
        if index > 60:
            return -1

        if (index == 1) or (index == 21) or (index == 41):
            return 0

        if (index == 1) or (index == 21) or (index == 41) or (index == 3) or (index == 23) or (index == 43):
            return 1

        return -1

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if ! __FISHING_MAIN__
    @staticmethod
    def DetermineFish(ch):
        map_idx = ch.GetMapIndex()
        prob_idx = fishing.GetProbIndexByMapIndex(map_idx)

        if prob_idx < 0:
            return 0

        if ch.GetPremiumRemainSeconds(EPremiumTypes.PREMIUM_FISH_MIND) > 0 or ch.IsEquipUniqueGroup(uint(Globals.UNIQUE_GROUP_FISH_MIND)):
            if quest.CQuestManager.instance().GetEventFlag("manwoo") != 0:
                prob_idx = 3
            else:
                prob_idx = 2

        adjust = 0
        if quest.CQuestManager.instance().GetEventFlag("fish_miss_pct") != 0:
            fish_pct_value = MINMAX(0, quest.CQuestManager.instance().GetEventFlag("fish_miss_pct"), 200)
            adjust = math.trunc((100-fish_pct_value) * fishing.fish_info[0].prob[prob_idx] / float(100))

        rv = number(adjust + 1, fishing.g_prob_sum[prob_idx])

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to pointers to value types:
#ORIGINAL METINII C CODE: int * p = std::lower_bound(g_prob_accumulate[prob_idx], g_prob_accumulate[prob_idx] + MAX_FISH, rv);
        p = std::lower_bound(fishing.g_prob_accumulate[prob_idx], fishing.g_prob_accumulate[prob_idx] + fishing.MAX_FISH, rv)
        fish_idx = p - fishing.g_prob_accumulate[prob_idx]

        vnum = fishing.fish_info[fish_idx].vnum

        if vnum == 50008 or vnum == 50009 or vnum == 80008:
            return 0

        return (fish_idx)

    @staticmethod
    def FishingReact(ch):
        p = packet_fishing()
        p.header = byte(Globals.LG_HEADER_GC_FISHING)
        p.subheader = byte(Globals.FISHING_SUBLG_HEADER_GC_REACT)
        p.info = ch.GetVID()
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        ch.PacketAround(p, sizeof(p))

    @staticmethod
    def FishingSuccess(ch):
        p = packet_fishing()
        p.header = byte(Globals.LG_HEADER_GC_FISHING)
        p.subheader = byte(Globals.FISHING_SUBLG_HEADER_GC_SUCCESS)
        p.info = ch.GetVID()
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        ch.PacketAround(p, sizeof(p))

    @staticmethod
    def FishingFail(ch):
        p = packet_fishing()
        p.header = byte(Globals.LG_HEADER_GC_FISHING)
        p.subheader = byte(Globals.FISHING_SUBLG_HEADER_GC_FAIL)
        p.info = ch.GetVID()
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        ch.PacketAround(p, sizeof(p))

    @staticmethod
    def FishingPractice(ch):
        rod = ch.GetWear(EWearPositions.WEAR_WEAPON)
        if rod is not None and rod.GetType() == EItemTypes.ITEM_ROD:
            if rod.GetRefinedVnum()>0 and rod.GetSocket(0) < rod.GetValue(2) and number(1,rod.GetValue(1))==1:
                rod.SetSocket(0, rod.GetSocket(0) + 1, ((not DefineConstants.false)))
                ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Your Fishing Points raised! (%d/%d)"),rod.GetSocket(0), rod.GetValue(2))
                if rod.GetSocket(0) == rod.GetValue(2):
                    ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You cannot upgrade your Rod anymore."))
                    ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Upgrade your Rod with the help of a Fisher."))
        rod.SetSocket(2, 0, ((not DefineConstants.false)))

    @staticmethod
    def PredictFish(ch):
        if ch.FindAffect(LaniatusEAffectTypes.LANIA_AFFECT_FISH_MIND_PILL, APPLY_NONE) is not None or ch.GetPremiumRemainSeconds(EPremiumTypes.PREMIUM_FISH_MIND) > 0 or ch.IsEquipUniqueGroup(uint(Globals.UNIQUE_GROUP_FISH_MIND)):
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        return LGEMiscellaneous.DEFINECONSTANTS.false

    @staticmethod
    def (UnnamedParameter):
        info = if isinstance(event.info, fishing_event_info) else None

        if info is None:
            #lani_err("fishing_event> <Factor> Null pointer")
            return 0

        ch = CHARACTER_MANAGER.instance().FindByPID(info.pid)

        if ch is None:
            return 0

        rod = ch.GetWear(EWearPositions.WEAR_WEAPON)

        if not(rod is not None and rod.GetType() == EItemTypes.ITEM_ROD):
            ch.m_pkFishingEvent = None
            return 0

        if info.step == 0:
            info.step += 1
            info.hang_time = get_dword_time()
            info.fish_id = fishing.DetermineFish(ch)
            fishing.FishingReact(ch)

            if fishing.PredictFish(ch):
                p = packet_fishing()
                p.header = byte(Globals.LG_HEADER_GC_FISHING)
                p.subheader = byte(Globals.FISHING_SUBLG_HEADER_GC_FISH)
                p.info = fishing.fish_info[info.fish_id].vnum
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                ch.GetDesc().Packet(p, sizeof(packet_fishing))
            return (((6) * passes_per_sec))


        if True:
            info.step += 1

            if info.step > 5:
                info.step = 5

            ch.m_pkFishingEvent = None
            fishing.FishingFail(ch)
            rod.SetSocket(2, 0, ((not DefineConstants.false)))
            return 0

    @staticmethod
    def GetFishingLevel(ch):
        rod = ch.GetWear(EWearPositions.WEAR_WEAPON)

        if rod is None or rod.GetType()!= EItemTypes.ITEM_ROD:
            return 0

        return rod.GetSocket(2) + rod.GetValue(0)

    @staticmethod
    def Compute(fish_id, ms, item, level):
        if fish_id == 0:
            return -2

        if fish_id >= fishing.MAX_FISH:
            #lani_err("Wrong FISH ID : %d", fish_id)
            return -2

        if ms > 6000:
            return -1

        time_step = MINMAX(0,(math.trunc((ms + 99) / float(200))), fishing.MAX_FISHING_TIME_COUNT - 1)

        if number(1, 100) <= fishing.aFishingTime[fishing.fish_info[fish_id].time_type][time_step]:
            if number(1, fishing.fish_info[fish_id].difficulty) <= level:
                item.arg_value = fishing.fish_info[fish_id].vnum
                return 0
            return -3

        return -1

    @staticmethod
    def GetFishLength(fish_id):
        if number(0,99):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
            return int((fishing.fish_info[fish_id].length_range[0] + (fishing.fish_info[fish_id].length_range[1] - fishing.fish_info[fish_id].length_range[0]) * (number(0,2000)+number(0,2000)+number(0,2000)+number(0,2000)+number(0,2000))/10000))
        else:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
            return int((fishing.fish_info[fish_id].length_range[1] + (fishing.fish_info[fish_id].length_range[2] - fishing.fish_info[fish_id].length_range[1]) * 2 * math.asin(number(0,10000)/10000.0) / LGEMiscellaneous.DEFINECONSTANTS.M_PI))
##endif

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if __FISHING_MAIN__
def main(args):
    srandomdev()

    Initialize()

    i = 0
    while i < MAX_FISH:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following line has a C++ format specifier which cannot be directly translated to Python:
        print("%s\t%u\t%u\t%u\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d".format(fish_info[i].name, fish_info[i].vnum, fish_info[i].dead_vnum, fish_info[i].grill_vnum, fish_info[i].prob[0], fish_info[i].prob[1], fish_info[i].prob[2], fish_info[i].difficulty, fish_info[i].time_type, fish_info[i].length_range[0], fish_info[i].length_range[1], fish_info[i].length_range[2]), end = '')

        j = 0
        while j < NUM_USE_RESULT_COUNT:
            print("\t{0:d}".format(fish_info[i].used_table[j]), end = '')
            j += 1

        print("")
        i += 1

    return 1

##endif
