import math

class mining: #this class replaces the original namespace 'mining'
    @staticmethod
    def CreateMiningEvent(ch, load, count):
        info = Globals.AllocEventInfo()
        info.pid = ch.GetPlayerID()
        info.vid_load = load.GetVID()

        return event_create_ex(mining_event, info, ((2 * count) * passes_per_sec))

    @staticmethod
    def GetRawOreFromLoad(dwLoadVnum):
        for i in range(0, mining.MAX_ORE):
            if mining.info[i].dwLoadVnum == dwLoadVnum:
                return mining.info[i].dwRawOreVnum
        return 0

    @staticmethod
    def OreRefine(ch, npc, item, cost, pct, metinstone_item):
        if ch is None or npc is None:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if item.GetOwner() is not ch:
            #lani_err("wrong owner")
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if item.GetCount() < mining.ORE_COUNT_FOR_REFINE:
            #lani_err("not enough count")
            return LGEMiscellaneous.DEFINECONSTANTS.false

        dwRefinedVnum = mining.GetRefineFromRawOre(item.GetVnum())

        if dwRefinedVnum == 0:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        ch.SetRefineNPC(npc)
        item.SetCount(item.GetCount() - mining.ORE_COUNT_FOR_REFINE)
        iCost = ch.ComputeRefineFee(cost, 1)

        if ch.GetGold() < iCost:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        ch.PayRefineFee(iCost)

        if metinstone_item:
            ITEM_MANAGER.instance().RemoveItem(metinstone_item, "REMOVE (MELT)")

        if number(1, 100) <= pct:
            ch.AutoGiveItem(dwRefinedVnum, 1)
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        return LGEMiscellaneous.DEFINECONSTANTS.false

    @staticmethod
    def GetFractionCount():
        r = number(1, 100)

        for i in range(0, mining.MAX_FRACTION_COUNT):
            if r <= mining.fraction_info[i][0]:
                return number(mining.fraction_info[i][1], mining.fraction_info[i][2])
            else:
                r -= mining.fraction_info[i][0]

        return 0

    @staticmethod
    def RealRefinePick(ch, item):
        if ch is None or item is None:
            return 2

        rkItemMgr = ITEM_MANAGER.instance()

        if not mining.Pick_Check(item):
            #lani_err("REFINE_PICK_HACK pid(%u) item(%s:%d) type(%d)", ch.GetPlayerID(), item.GetName(LOCALE_LANIATUS), item.GetID(), item.GetType())
            return 2

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to references to variables:
#ORIGINAL METINII C CODE: CItem& rkOldPick = *item;
        rkOldPick = item

        if not mining.Pick_Refinable(rkOldPick):
            return 2

        iAdv = math.trunc(rkOldPick.GetValue(0) / float(10))

        if rkOldPick.IsEquipped() == ((not LGEMiscellaneous.DEFINECONSTANTS.false)):
            return 2

        if mining.Pick_IsRefineSuccess(rkOldPick):
            pkNewPick = ITEM_MANAGER.instance().CreateItem(rkOldPick.GetRefinedVnum(), 1, 0, DefineConstants.false, -1, DefineConstants.false)
            if pkNewPick:
                wCell = rkOldPick.GetCell()
                rkItemMgr.RemoveItem(item, "REMOVE (REFINE PICK)")
                pkNewPick.AddToCharacter(ch, TItemPos(EWindows.INVENTORY, wCell))
                return 1

            return 2
        else:
            pkNewPick = ITEM_MANAGER.instance().CreateItem(uint(rkOldPick.GetValue(4)), 1, 0, DefineConstants.false, -1, DefineConstants.false)

            if pkNewPick:
                wCell = rkOldPick.GetCell()
                rkItemMgr.RemoveItem(item, "REMOVE (REFINE PICK)")
                pkNewPick.AddToCharacter(ch, TItemPos(EWindows.INVENTORY, wCell))
                return 0

            return 2

    @staticmethod
    def CHEAT_MAX_PICK(ch, item):
        if item is None:
            return

        if not mining.Pick_Check(item):
            return

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to references to variables:
#ORIGINAL METINII C CODE: CItem& pick = *item;
        pick = item
        mining.Pick_MaxCurExp(pick)

        ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Your Mining points are raised to the Limit. (%d)."), mining.Pick_GetCurExp(pick))

    @staticmethod
    def IsVeinOfOre(vnum):
        for i in range(0, mining.MAX_ORE):
            if mining.info[i].dwLoadVnum == vnum:
                return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
        return LGEMiscellaneous.DEFINECONSTANTS.false


class mining: #this class replaces the original namespace 'mining'
    MAX_ORE = 18
    MAX_FRACTION_COUNT = 9
    ORE_COUNT_FOR_REFINE = 100

    class SInfo:

        def __init__(self):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.dwLoadVnum = 0
            self.dwRawOreVnum = 0
            self.dwRefineVnum = 0


    info = [SInfo(20047, 50601, 50621), SInfo(20048, 50602, 50622), SInfo(20049, 50603, 50623), SInfo(20050, 50604, 50624), SInfo(20051, 50605, 50625), SInfo(20052, 50606, 50626), SInfo(20053, 50607, 50627), SInfo(20054, 50608, 50628), SInfo(20055, 50609, 50629), SInfo(20056, 50610, 50630), SInfo(20057, 50611, 50631), SInfo(20058, 50612, 50632), SInfo(20059, 50613, 50633), SInfo(30301, 50614, 50634), SInfo(30302, 50615, 50635), SInfo(30303, 50616, 50636), SInfo(30304, 50617, 50637), SInfo(30305, 50618, 50638)]

    fraction_info = [[ 20, 1, 10 ], [ 30, 11, 20 ], [ 20, 21, 30 ], [ 15, 31, 40 ], [ 5, 41, 50 ], [ 4, 51, 60 ], [ 3, 61, 70 ], [ 2, 71, 80 ], [ 1, 81, 90 ]]

    PickGradeAddPct = [3, 5, 8, 11, 15, 20, 26, 32, 40, 50]

    SkillLevelAddPct = [0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 11] + [0 for _ in range(LGEMiscellaneous.LG_SKILL_MAX_LEVEL + 1 - 41)]

    @staticmethod
    def GetRefineFromRawOre(dwRawOreVnum):
        for i in range(0, mining.MAX_ORE):
            if mining.info[i].dwRawOreVnum == dwRawOreVnum:
                return mining.info[i].dwRefineVnum
        return 0

    @staticmethod
    def OreDrop(ch, dwLoadVnum):
        dwRawOreVnum = mining.GetRawOreFromLoad(dwLoadVnum)

        iFractionCount = mining.GetFractionCount()

        if iFractionCount == 0:
            #lani_err("Wrong ore fraction count")
            return

        item = ITEM_MANAGER.instance().CreateItem(dwRawOreVnum, uint(mining.GetFractionCount()), 0, DefineConstants.false, -1, DefineConstants.false)

        if item is None:
            #lani_err("cannot create item vnum %d", dwRawOreVnum)
            return

        pos = pixel_position_s()
        pos.x = ch.GetX() + number(-200, 200)
        pos.y = ch.GetY() + number(-200, 200)

        item.AddToGround(ch.GetMapIndex(), pos, DefineConstants.false)
        item.StartDestroyEvent(300)
        item.SetOwnership(ch, 15)

    @staticmethod
    def GetOrePct(ch):
        defaultPct = 20
        iSkillLevel = ch.GetSkillLevel(LaniatusETalentXes.LG_SKILL_MINING)

        pick = ch.GetWear(EWearPositions.WEAR_WEAPON)

        if pick is None or pick.GetType() != EItemTypes.ITEM_PICK:
            return 0

        return defaultPct + mining.SkillLevelAddPct[MINMAX(0, iSkillLevel, 40)] + mining.PickGradeAddPct[MINMAX(0, pick.GetRefineLevel(), 9)]

    class mining_event_info(event_info_data):

        def __init__(self):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.pid = 0
            self.vid_load = 0

            self.pid = 0
            self.vid_load = 0

    @staticmethod
    def Pick_Check(item):
        if item.GetType() != EItemTypes.ITEM_PICK:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    @staticmethod
    def Pick_GetMaxExp(pick):
        return pick.GetValue(2)

    @staticmethod
    def Pick_GetCurExp(pick):
        return pick.GetSocket(0)

    @staticmethod
    def Pick_IncCurExp(pick):
        cur = mining.Pick_GetCurExp(pick)
        pick.SetSocket(0, cur + 1, ((not DefineConstants.false)))

    @staticmethod
    def Pick_MaxCurExp(pick):
        max = mining.Pick_GetMaxExp(pick)
        pick.SetSocket(0, max, ((not DefineConstants.false)))

    @staticmethod
    def Pick_Refinable(item):
        if mining.Pick_GetCurExp(item) < mining.Pick_GetMaxExp(item):
            return LGEMiscellaneous.DEFINECONSTANTS.false

        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    @staticmethod
    def Pick_IsPracticeSuccess(pick):
        return (number(1,pick.GetValue(1))==1)

    @staticmethod
    def Pick_IsRefineSuccess(pick):
        return (number(1,100) <= pick.GetValue(3))

    @staticmethod
    def PracticePick(ch, item):
        if item is None:
            return

        if not mining.Pick_Check(item):
            return

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to references to variables:
#ORIGINAL METINII C CODE: CItem& pick = *item;
        pick = item
        if pick.GetRefinedVnum()<=0:
            return

        if mining.Pick_IsPracticeSuccess(pick):

            if mining.Pick_Refinable(pick):
                ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Your Mining Points are raised to the highest Level."))
                ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You can upgrade your Pick Axe with the help of a Lumberjack."))
            else:
                mining.Pick_IncCurExp(pick)

                ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Your Mining Points raised! (%d/%d)"), mining.Pick_GetCurExp(pick), mining.Pick_GetMaxExp(pick))

                if mining.Pick_Refinable(pick):
                    ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Your Mining Points are raised to the highest Level."))
                    ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You can upgrade your Pick Axe with the help of a Lumberjack."))

    @staticmethod
    def (UnnamedParameter):
        info = if isinstance(event.info, mining_event_info) else None

        if info is None:
            #lani_err("mining_event_info> <Factor> Null pointer")
            return 0

        ch = CHARACTER_MANAGER.instance().FindByPID(info.pid)
        load = CHARACTER_MANAGER.instance().Find(info.vid_load)

        if ch is None:
            return 0

        ch.mining_take()

        pick = ch.GetWear(EWearPositions.WEAR_WEAPON)

        if pick is None or not mining.Pick_Check(pick):
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Without a Pick Axe you cannot mine."))
            return 0

        if load is None:
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Nothing to mine here."))
            return 0

        iPct = mining.GetOrePct(ch)

        if number(1, 100) <= iPct:
            mining.OreDrop(ch, load.GetRaceNum())
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("The mining was successful."))
        else:
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("The mining failed."))

        mining.PracticePick(ch, pick)

        return 0

