from enum import Enum
import math

class CSpecialAttrGroup:
    def __init__(self, vnum):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.m_dwVnum = 0
        self.m_stEffectFileName = ""
        self.m_vecAttrs = []

        self.m_dwVnum = vnum
    class CSpecialAttrInfo:
        def __init__(self, _apply_type, _apply_value):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.apply_type = 0
            self.apply_value = 0

            self.apply_type = _apply_type
            self.apply_value = _apply_value


class CSpecialItemGroup:
    class EGiveType(Enum):
        NONE = 0
        GOLD = 1
        EXP = 2
        MOB = 3
        SLOW = 4
        DRAIN_HP = 5
        POISON = 6
        MOB_GROUP = 7
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if ENABLE_WOLFMAN
        BLEEDING = 8
##endif

    class ESIGType(Enum):
        NORMAL = 0
        PCT = 1
        QUEST = 2
        SPECIAL = 3

    class CSpecialItemInfo:

        def __init__(self, _vnum, _count, _rare):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.vnum = 0
            self.count = 0
            self.rare = 0

            self.vnum = _vnum
            self.count = _count
            self.rare = _rare

    def __init__(self, vnum, type = 0):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.m_dwVnum = 0
        self.m_bType = 0
        self.m_vecProbs = []
        self.m_vecItems = []

        self.m_dwVnum = vnum
        self.m_bType = type

    def AddItem(self, vnum, count, prob, rare):
        if prob == 0:
            return
        if self.m_vecProbs:
            prob += self.m_vecProbs[len(self.m_vecProbs) - 1]
        self.m_vecProbs.append(prob)
        self.m_vecItems.append(CSpecialItemInfo(vnum, count, rare))

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: bool IsEmpty() const
    def IsEmpty(self):
        return not self.m_vecProbs

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: int GetMultiIndex(list<int> &idx_vec) const
    def GetMultiIndex(self, idx_vec):
        idx_vec.clear()
        if self.m_bType == ESIGType.PCT:
            count = 0
            if number(1,100) <= self.m_vecProbs[0]:
                idx_vec.append(0)
                count += 1
            i = 1
            while i < len(self.m_vecProbs):
                if number(1,100) <= self.m_vecProbs[i] - self.m_vecProbs[i-1]:
                    idx_vec.append(int(i))
                    count += 1
                i += 1
            return count
        else:
            idx_vec.append(self.GetOneIndex())
            return 1

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: int GetOneIndex() const
    def GetOneIndex(self):
        n = number(1, self.m_vecProbs[len(self.m_vecProbs) - 1])
        it = lower_bound(self.m_vecProbs.begin(), self.m_vecProbs.end(), n)
        return std::distance(self.m_vecProbs.begin(), it)

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: int GetVnum(int idx) const
    def GetVnum(self, idx):
        return int(self.m_vecItems[idx].vnum)

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: int GetCount(int idx) const
    def GetCount(self, idx):
        return self.m_vecItems[idx].count

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: int GetRarePct(int idx) const
    def GetRarePct(self, idx):
        return self.m_vecItems[idx].rare

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: bool Contains(uint dwVnum) const
    def Contains(self, dwVnum):
        i = 0
        while i < len(self.m_vecItems):
            if self.m_vecItems[i].vnum == dwVnum:
                return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
            i += 1
        return LGEMiscellaneous.DEFINECONSTANTS.false

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: uint GetAttrVnum(uint dwVnum) const
    def GetAttrVnum(self, dwVnum):
        if CSpecialItemGroup.ESIGType.SPECIAL != self.m_bType:
            return 0
        for it in self.m_vecItems:
            if it.vnum == dwVnum:
                return it.count
        return 0


class CMobItemGroup:
    class SMobItemGroupInfo:

        def __init__(self, dwItemVnum, iCount, iRarePct):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.dwItemVnum = 0
            self.iCount = 0
            self.iRarePct = 0

            self.dwItemVnum = dwItemVnum
            self.iCount = iCount
            self.iRarePct = iRarePct

    def __init__(self, dwMobVnum, iKillDrop, r_stName):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self._m_dwMobVnum = 0
        self._m_iKillDrop = 0
        self._m_stName = ""
        self._m_vecProbs = []
        self._m_vecItems = []

        self._m_dwMobVnum = dwMobVnum
        self._m_iKillDrop = iKillDrop
        self._m_stName = r_stName

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: int GetKillPerDrop() const
    def GetKillPerDrop(self):
        return self._m_iKillDrop

    def AddItem(self, dwItemVnum, iCount, iPartPct, iRarePct):
        if self._m_vecProbs:
            iPartPct += self._m_vecProbs[len(self._m_vecProbs) - 1]
        self._m_vecProbs.append(iPartPct)
        self._m_vecItems.append(SMobItemGroupInfo(dwItemVnum, iCount, iRarePct))

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: bool IsEmpty() const
    def IsEmpty(self):
        return not self._m_vecProbs

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: int GetOneIndex() const
    def GetOneIndex(self):
        n = number(1, self._m_vecProbs[len(self._m_vecProbs) - 1])
        it = lower_bound(self._m_vecProbs.begin(), self._m_vecProbs.end(), n)
        return std::distance(self._m_vecProbs.begin(), it)

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: const SMobItemGroupInfo& GetOne() const
    def GetOne(self):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
#ORIGINAL METINII C CODE: return m_vecItems[GetOneIndex()];
        return CMobItemGroup.SMobItemGroupInfo(self._m_vecItems[self.GetOneIndex()])


class CDropItemGroup:
    class SDropItemGroupInfo:

        def __init__(self, dwVnum, dwPct, iCount):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.dwVnum = 0
            self.dwPct = 0
            self.iCount = 0

            self.dwVnum = dwVnum
            self.dwPct = dwPct
            self.iCount = iCount

    def __init__(self, dwVnum, dwMobVnum, r_stName):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self._m_dwVnum = 0
        self._m_dwMobVnum = 0
        self._m_stName = ""
        self._m_vec_items = []

        self._m_dwVnum = dwVnum
        self._m_dwMobVnum = dwMobVnum
        self._m_stName = r_stName

    def GetVector(self):
        return list(self._m_vec_items)

    def AddItem(self, dwItemVnum, dwPct, iCount):
        self._m_vec_items.append(SDropItemGroupInfo(dwItemVnum, dwPct, iCount))


class CLevelItemGroup:
    class SLevelItemGroupInfo:

        def __init__(self, dwVnum, dwPct, iCount):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.dwVNum = 0
            self.dwPct = 0
            self.iCount = 0

            self.dwVNum = dwVnum
            self.dwPct = dwPct
            self.iCount = iCount


    def __init__(self, dwLevelLimit):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self._m_dwLevelLimit = 0
        self._m_stName = ""
        self._m_vec_items = []

        self._m_dwLevelLimit = dwLevelLimit

    def GetLevelLimit(self):
        return self._m_dwLevelLimit

    def AddItem(self, dwItemVnum, dwPct, iCount):
        self._m_vec_items.append(SLevelItemGroupInfo(dwItemVnum, dwPct, iCount))

    def GetVector(self):
        return list(self._m_vec_items)

class CBuyerThiefGlovesItemGroup:
    class SThiefGroupInfo:

        def __init__(self, dwVnum, dwPct, iCount):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.dwVnum = 0
            self.dwPct = 0
            self.iCount = 0

            self.dwVnum = dwVnum
            self.dwPct = dwPct
            self.iCount = iCount

    def __init__(self, dwVnum, dwMobVnum, r_stName):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self._m_dwVnum = 0
        self._m_dwMobVnum = 0
        self._m_stName = ""
        self._m_vec_items = []

        self._m_dwVnum = dwVnum
        self._m_dwMobVnum = dwMobVnum
        self._m_stName = r_stName

    def GetVector(self):
        return list(self._m_vec_items)

    def AddItem(self, dwItemVnum, dwPct, iCount):
        self._m_vec_items.append(SThiefGroupInfo(dwItemVnum, dwPct, iCount))


## Laniatus Games Studio Inc. | NOTE: Python has no need of forward class declarations:
#class ITEM

class ITEM_MANAGER(singleton):
    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.m_vec_prototype = []
        self.m_vec_item_vnum_range_info = []
        self.m_map_ItemRefineFrom = {}
        self.m_iTopOfTable = 0
        self.m_VIDMap = {}
        self.m_dwVIDCount = 0
        self.m_dwCurrentID = 0
        self.m_ItemIDRange = tItemIDRange()
        self.m_ItemIDSpareRange = tItemIDRange()
        self.m_set_pkItemForDelayedSave = _boost_func_of_void.unordered_set()
        self.m_map_pkItemByID = {}
        self.m_map_dwEtcItemDropProb = {}
        self.m_map_pkDropItemGroup = {}
        self.m_map_pkSpecialItemGroup = {}
        self.m_map_pkQuestItemGroup = {}
        self.m_map_pkSpecialAttrGroup = {}
        self.m_map_pkMobItemGroup = {}
        self.m_map_pkLevelItemGroup = {}
        self.m_map_pkGloveItemGroup = {}
        self.m_ItemToSpecialGroup = {}
        self._m_map_new_to_ori = {}
        self.m_map_vid = {}

        self.m_iTopOfTable = 0
        self.m_dwVIDCount = 0
        self.m_dwCurrentID = 0
        self.m_ItemIDRange.dwMin = self.m_ItemIDRange.dwMax = self.m_ItemIDRange.dwUsableItemIDMin = 0
        self.m_ItemIDSpareRange.dwMin = self.m_ItemIDSpareRange.dwMax = self.m_ItemIDSpareRange.dwUsableItemIDMin = 0

    def close(self):
        self.Destroy()

    def Initialize(self, table, size):
        if self.m_vec_prototype:
            self.m_vec_prototype.clear()

        i = None

        self.m_vec_prototype.resize(size)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memcpy' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memcpy(self.m_vec_prototype[0], table, sizeof(SItemTable) * size)
        for i in range(0, size):
            if 0 != self.m_vec_prototype[i].dwVnumRange:
                self.m_vec_item_vnum_range_info.append(self.m_vec_prototype[i])

        self.m_map_ItemRefineFrom.clear()
        for i in range(0, size):

            if (self.m_vec_prototype[i].dwRefinedVnum) != 0:
                self.m_map_ItemRefineFrom.update({self.m_vec_prototype[i].dwRefinedVnum: self.m_vec_prototype[i].dwVnum})

            ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'IS_SET' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
            if self.m_vec_prototype[i].bType == EItemTypes.ITEM_QUEST or IS_SET(self.m_vec_prototype[i].dwFlags, EItemFlag.ITEM_FLAG_QUEST_USE | EItemFlag.ITEM_FLAG_QUEST_USE_MULTIPLE):
                quest.CQuestManager.instance().RegisterNPCVnum(self.m_vec_prototype[i].dwVnum)

            if self.m_vec_prototype[i].bType == EItemTypes.ITEM_COSTUME and self.m_vec_prototype[i].bSubType == ECostumeSubTypes.COSTUME_MOUNT:
                CMobManager.instance().InsertCostumeMount(uint(self.m_vec_prototype[i].alValues[0]))

            self.m_map_vid.insert(dict.value_type(self.m_vec_prototype[i].dwVnum, self.m_vec_prototype[i]))
            if test_server:
                #sys_log(0, "ITEM_INFO %d %s ", self.m_vec_prototype[i].dwVnum, self.m_vec_prototype[i].szName)

        len = 0
        len2 = None
        buf = str(['\0' for _ in range(512)])

        for i in range(0, size):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            len2 = snprintf(buf[len:], sizeof(buf) - len, "%5u %-16s", self.m_vec_prototype[i].dwVnum, self.m_vec_prototype[i].szLocaleName)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            if len2 < 0 or len2 >= int(sizeof(buf)) - len:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                len += (sizeof(buf) - len) - 1
            else:
                len += len2

            if (math.fmod((i + 1), 4)) == 0:
                if not test_server:
                    #sys_log(0, "%s", buf)
                len = 0
            else:
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: buf[len++] = '\t';
                buf[len] = '\t'
                len += 1
                buf[len] = '\0'

        if (math.fmod((i + 1), 4)) != 0:
            if not test_server:
                #sys_log(0, "%s", buf)

        it = self.m_VIDMap.begin()

        #sys_log(1, "ITEM_VID_MAP %d", len(self.m_VIDMap))

        while it is not self.m_VIDMap.end():
            item = it.second
            it += 1

            tableInfo = self.GetTable(item.GetOriginalVnum())

            if None is tableInfo:
                #lani_err("cannot reset item table")
                item.SetProto(None)

            item.SetProto(tableInfo)

        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def Destroy(self):
        it = self.m_VIDMap.begin()
        while it is not self.m_VIDMap.end():
            LG_DEL_MEM(it.second)
            it += 1
        self.m_VIDMap.clear()

    def Update(self):
        it = self.m_set_pkItemForDelayedSave.begin()

        while it is not self.m_set_pkItemForDelayedSave.end():
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: auto this_it = it++;
            this_it = it
            it += 1
            item = *this_it

            ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'IS_SET' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
            if item.GetOwner() is not None and IS_SET(item.GetFlag(), EItemFlag.ITEM_FLAG_SLOW_QUERY):
                continue

            self.SaveSingleItem(item)

            self.m_set_pkItemForDelayedSave.erase(this_it)

    def GracefulShutdown(self):
        it = self.m_set_pkItemForDelayedSave.begin()

        while it is not self.m_set_pkItemForDelayedSave.end():
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: SaveSingleItem(*(it++));
            self.SaveSingleItem((it))
            it += 1

        self.m_set_pkItemForDelayedSave.clear()

# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    GetNewID()
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    SetMaxItemID(range)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    SetMaxSpareItemID(range)
    def DelayedSave(self, item):
        if item.GetID() != 0:
            self.m_set_pkItemForDelayedSave.insert(item)

    def FlushDelayedSave(self, item):
        it = self.m_set_pkItemForDelayedSave.find(item)

        if it == self.m_set_pkItemForDelayedSave.end():
            return

        self.m_set_pkItemForDelayedSave.erase(it)
        self.SaveSingleItem(item)

    def SaveSingleItem(self, item):
        if item.GetOwner() is None:
            dwID = item.GetID()
            dwOwnerID = item.GetLastOwnerPID()

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            db_clientdesc.DBPacketHeader(Globals.LG_HEADER_GD_ITEM_DESTROY, 0, sizeof(uint) + sizeof(uint))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            db_clientdesc.Packet(dwID, sizeof(uint))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            db_clientdesc.Packet(dwOwnerID, sizeof(uint))

            #sys_log(1, "ITEM_DELETE %s:%u", item.GetName(LOCALE_LANIATUS), dwID)
            return

        #sys_log(1, "ITEM_SAVE %s:%d in %s window %d", item.GetName(LOCALE_LANIATUS), item.GetID(), item.GetOwner().GetName(LOCALE_LANIATUS), item.GetWindow())

        t = SPlayerItem()

        t.id = item.GetID()
        t.window = item.GetWindow()
        t.pos = item.GetCell() - ushort(LGEMiscellaneous.INVENTORY_MAX_NUM) if t.window == EWindows.EQUIPMENT else item.GetCell()
        t.count = item.GetCount()
        t.vnum = item.GetOriginalVnum()
        t.owner = item.GetOwner().GetDesc().GetAccountTable().id if (t.window == EWindows.SAFEBOX or t.window == EWindows.MALL) else item.GetOwner().GetPlayerID()
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memcpy' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memcpy(t.alSockets, item.GetSockets(), sizeof(t.alSockets))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memcpy' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memcpy(t.aAttr, item.GetAttributes(), sizeof(t.aAttr))

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        db_clientdesc.DBPacketHeader(Globals.LG_HEADER_GD_ITEM_SAVE, 0, sizeof(SPlayerItem))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        db_clientdesc.Packet(t, sizeof(SPlayerItem))

    def CreateItem(self, vnum, count = 1, id = 0, bTryMagic = LGEMiscellaneous.DefineConstants.false, iRarePct = -1, bSkipSave = LGEMiscellaneous.DefineConstants.false):
        if 0 == vnum:
            return None

        dwMaskVnum = 0
        if self.GetMaskVnum(vnum) != 0:
            dwMaskVnum = self.GetMaskVnum(vnum)

        table = self.GetTable(vnum)

        if None is table:
            return None

        item = None

        if id in self.m_map_pkItemByID.keys():
            item = self.m_map_pkItemByID[id]
            owner = item.GetOwner()
            #lani_err("ITEM_ID_DUP: %u %s owner %p", id, item.GetName(LOCALE_LANIATUS), Globals.get_pointer(owner))
            return None

        item = LG_NEW_M2 CItem(vnum)
        bIsNewItem = (0 == id)
        item.Initialize()
        item.SetProto(table)
        item.SetMaskVnum(dwMaskVnum)

        if item.GetType() == EItemTypes.ITEM_ELK:
            item.SetSkipSave(((not LGEMiscellaneous.DEFINECONSTANTS.false)))

        elif not bIsNewItem:
            item.SetID(id)
            item.SetSkipSave(((not LGEMiscellaneous.DEFINECONSTANTS.false)))
        else:
            item.SetID(self.GetNewID())

            if item.GetType() == EItemTypes.ITEM_UNIQUE:
                if item.GetValue(2) == 0:
                    item.SetSocket(EItemUniqueSockets.LG_ITEM_SOCKET_UNIQUE_REMAIN_TIME, item.GetValue(0), ((not DefineConstants.false)))
                else:
                    item.SetSocket(EItemUniqueSockets.LG_ITEM_SOCKET_UNIQUE_REMAIN_TIME, get_global_time() + item.GetValue(0), ((not DefineConstants.false)))


        if (item.GetVnum() == Globals.ITEM_AUTO_HP_RECOVERY_S) or (item.GetVnum() == Globals.ITEM_AUTO_HP_RECOVERY_M) or (item.GetVnum() == Globals.ITEM_AUTO_HP_RECOVERY_L) or (item.GetVnum() == Globals.ITEM_AUTO_HP_RECOVERY_X) or (item.GetVnum() == Globals.ITEM_AUTO_SP_RECOVERY_S) or (item.GetVnum() == Globals.ITEM_AUTO_SP_RECOVERY_M) or (item.GetVnum() == Globals.ITEM_AUTO_SP_RECOVERY_L) or (item.GetVnum() == Globals.ITEM_AUTO_SP_RECOVERY_X) or (item.GetVnum() == Globals.REWARD_BOX_ITEM_AUTO_SP_RECOVERY_XS) or (item.GetVnum() == Globals.REWARD_BOX_ITEM_AUTO_SP_RECOVERY_S) or (item.GetVnum() == Globals.REWARD_BOX_ITEM_AUTO_HP_RECOVERY_XS) or (item.GetVnum() == Globals.REWARD_BOX_ITEM_AUTO_HP_RECOVERY_S) or (item.GetVnum() == Globals.FUCKING_BRAZIL_ITEM_AUTO_SP_RECOVERY_S) or (item.GetVnum() == Globals.FUCKING_BRAZIL_ITEM_AUTO_HP_RECOVERY_S):
            if bIsNewItem:
                item.SetSocket(2, item.GetValue(0), ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
            else:
                item.SetSocket(2, item.GetValue(0), LGEMiscellaneous.DEFINECONSTANTS.false)

        if CItemVnumHelper.IsAcceItem(item.GetVnum()):
            item.SetSocket(0, item.GetProto().aApplies[0].lValue, ((not DefineConstants.false)))

        if item.GetType() == EItemTypes.ITEM_ELK:
            pass
        elif item.IsStackable():
            count = MINMAX(1, count, EItemMisc.ITEM_MAX_COUNT)

            ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'IS_SET' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
            if bTryMagic and count <= 1 and IS_SET(item.GetFlag(), EItemFlag.ITEM_FLAG_MAKECOUNT):
                count = uint(item.GetValue(1))
        else:
            count = 1

        self.m_dwVIDCount += 1
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: item->SetVID(++m_dwVIDCount);
        item.SetVID(self.m_dwVIDCount)

        if bSkipSave == LGEMiscellaneous.DEFINECONSTANTS.false:
            self.m_VIDMap.insert(ITEM_VID_MAP.value_type(item.GetVID(), item))

        if item.GetID() != 0 and bSkipSave == LGEMiscellaneous.DEFINECONSTANTS.false:
            self.m_map_pkItemByID.insert(dict.value_type(item.GetID(), item))

        if not item.SetCount(count):
            return None

        item.SetSkipSave(LGEMiscellaneous.DEFINECONSTANTS.false)

        if item.GetType() == EItemTypes.ITEM_UNIQUE and item.GetValue(2) != 0:
            item.StartUniqueExpireEvent()

        i = 0
        while i < EItemMisc.ITEM_LIMIT_MAX_NUM:
            if ELimitTypes.LIMIT_REAL_TIME == item.GetLimitType(uint(i)):
                if item.GetLimitValue(uint(i)) != 0:
                    item.SetSocket(0, time(0) + item.GetLimitValue(uint(i)), ((not DefineConstants.false)))
                else:
                    item.SetSocket(0, time(0) + 60 *60 *24 *7, ((not DefineConstants.false)))

                item.StartRealTimeExpireEvent()

            elif ELimitTypes.LIMIT_TIMER_BASED_ON_WEAR == item.GetLimitType(uint(i)):
                if ((not LGEMiscellaneous.DEFINECONSTANTS.false)) == item.IsEquipped():
                    item.StartTimerBasedOnWearExpireEvent()
                elif 0 == id:
                    duration = item.GetSocket(0)
                    if 0 == duration:
                        duration = item.GetLimitValue(uint(i))

                    if 0 == duration:
                        duration = 60 * 60 * 10

                    item.SetSocket(0, duration, ((not DefineConstants.false)))
            i += 1

        if id == 0:
            if EItemTypes.ITEM_BLEND == item.GetType():
                if Blend_Item_find(item.GetVnum()):
                    Blend_Item_set_value(item)
                    return item

            if table.sAddonType != 0:
                item.ApplyAddon(table.sAddonType)

            if bTryMagic:
                if iRarePct == -1:
                    iRarePct = table.bAlterToMagicItemPct

                if number(1, 100) <= iRarePct:
                    item.AlterToMagicItem(0, 0)

            if table.bGainSocketPct != 0:
                item.AlterToSocketItem(table.bGainSocketPct)

            if vnum == 50300 or vnum == Globals.ITEM_SKILLFORGET_VNUM:
                dwSkillVnum = None

                condition = True
                while condition:
                    dwSkillVnum = number(1, 111)

                    if None is not CSkillManager.instance().Get(dwSkillVnum):
                        break
                    condition = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

                item.SetSocket(0, int(dwSkillVnum), ((not DefineConstants.false)))
            elif Globals.ITEM_SKILLFORGET2_VNUM == vnum:
                dwSkillVnum = None

                condition = True
                while condition:
                    dwSkillVnum = number(112, 119)

                    if None is not CSkillManager.instance().Get(dwSkillVnum):
                        break
                    condition = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

                item.SetSocket(0, int(dwSkillVnum), ((not DefineConstants.false)))

        if item.GetType() == EItemTypes.ITEM_QUEST:
            it = m_map_pkQuestItemGroup.begin()
            while it is not self.m_map_pkQuestItemGroup.end():
                if it.second.m_bType == CSpecialItemGroup.ESIGType.QUEST and it.second.Contains(vnum):
                    item.SetSIGVnum(it.first)
                it += 1
        elif item.GetType() == EItemTypes.ITEM_UNIQUE:
            it = m_map_pkSpecialItemGroup.begin()
            while it is not self.m_map_pkSpecialItemGroup.end():
                if it.second.m_bType == CSpecialItemGroup.ESIGType.SPECIAL and it.second.Contains(vnum):
                    item.SetSIGVnum(it.first)
                it += 1

        if item.IsDragonSoul() and 0 == id:
            DSManager.instance().DragonSoulItemInitialize(item)
        return item

    def DestroyItem(self, item):
        if item.GetSectree():
            item.RemoveFromGround()

        if item.GetOwner():
            if CHARACTER_MANAGER.instance().Find(item.GetOwner().GetPlayerID()) is not None:
                #lani_err("DestroyItem: GetOwner %s %s!!", item.GetName(LOCALE_LANIATUS), item.GetOwner().GetName(LOCALE_LANIATUS))
                item.RemoveFromCharacter()
            else:
                #lani_err("WTH! Invalid item owner. owner pointer : %p", item.GetOwner())

        it = self.m_set_pkItemForDelayedSave.find(item)

        if it != self.m_set_pkItemForDelayedSave.end():
            self.m_set_pkItemForDelayedSave.erase(it)

        dwID = item.GetID()
        #sys_log(2, "ITEM_DESTROY %s:%u", item.GetName(LOCALE_LANIATUS), dwID)

        if (not item.GetSkipSave()) and dwID != 0:
            dwOwnerID = item.GetLastOwnerPID()

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            db_clientdesc.DBPacketHeader(Globals.LG_HEADER_GD_ITEM_DESTROY, 0, sizeof(uint) + sizeof(uint))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            db_clientdesc.Packet(dwID, sizeof(uint))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            db_clientdesc.Packet(dwOwnerID, sizeof(uint))
        else:
            #sys_log(2, "ITEM_DESTROY_SKIP %s:%u (skip=%d)", item.GetName(LOCALE_LANIATUS), dwID, item.GetSkipSave())

        if dwID != 0:
            self.m_map_pkItemByID.pop(dwID)

        self.m_VIDMap.pop(item.GetVID())
        LG_DEL_MEM(item)

    def RemoveItem(self, item, c_pszReason = None):
        o = None

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((o = item->GetOwner()))
        if (o = item.GetOwner()):
            if item.GetWindow() == EWindows.MALL or item.GetWindow() == EWindows.SAFEBOX:
                pSafebox = o.GetMall() if item.GetWindow() == EWindows.MALL else o.GetSafebox()
                if pSafebox:
                    pSafebox.Remove(item.GetCell())
            else:
                o.SyncQuickslot(byte(Globals.LG_QUICKSLOT_TYPE_ITEM), byte(item.GetCell()), 255)
                item.RemoveFromCharacter()

        ITEM_MANAGER.instance().DestroyItem(item)

    def Find(self, id):
        it = self.m_map_pkItemByID.find(id)
        if it is self.m_map_pkItemByID.end():
            return None
        return it.second

    def FindByVID(self, vid):
        it = self.m_VIDMap.find(vid)

        if it is self.m_VIDMap.end():
            return None

        return (it.second)

    def GetTable(self, vnum):
        rnum = self.RealNumber(vnum)

        if rnum < 0:
            i = 0
            while i < len(self.m_vec_item_vnum_range_info):
                p = self.m_vec_item_vnum_range_info[i]
                if (p.dwVnum < vnum) and vnum < (p.dwVnum + p.dwVnumRange):
                    return p
                i += 1

            return None

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
#ORIGINAL METINII C CODE: return &m_vec_prototype[rnum];
        return SItemTable(self.m_vec_prototype[rnum])

    def GetVnum(self, c_pszName, r_dwVnum):
        len = len(c_pszName)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Pointer arithmetic is detected on this variable:
#ORIGINAL METINII C CODE: SItemTable * pTable = &m_vec_prototype[0];
        pTable = self.m_vec_prototype[0]

        i = 0
        while i < len(self.m_vec_prototype):
            if not _strnicmp(c_pszName, pTable.szLocaleName, len):
                r_dwVnum.arg_value = pTable.dwVnum
                return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
            i += 1
            pTable += 1

        return LGEMiscellaneous.DEFINECONSTANTS.false

    def GetVnumByOriginalName(self, c_pszName, r_dwVnum):
        len = len(c_pszName)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Pointer arithmetic is detected on this variable:
#ORIGINAL METINII C CODE: SItemTable * pTable = &m_vec_prototype[0];
        pTable = self.m_vec_prototype[0]

        i = 0
        while i < len(self.m_vec_prototype):
            if not _strnicmp(c_pszName, pTable.szName, len):
                r_dwVnum.arg_value = pTable.dwVnum
                return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
            i += 1
            pTable += 1

        return LGEMiscellaneous.DEFINECONSTANTS.false

    def GetDropPct(self, pkChr, pkKiller, iDeltaPercent, iRandRange):
        if None is pkChr or None is pkKiller:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        iLevel = pkKiller.GetLevel()
        iDeltaPercent.arg_value = 100

        if (not pkChr.IsStone()) and pkChr.GetMobRank() >= EMobRank.MOB_RANK_BOSS:
            iDeltaPercent.arg_value = aiPercentByDeltaLevForBoss[MINMAX(0, (pkChr.GetLevel() + 15) - pkKiller.GetLevel(), LGEMiscellaneous.DEFINECONSTANTS.MAX_EXP_DELTA_OF_LEV - 1)]
        else:
            iDeltaPercent.arg_value = aiPercentByDeltaLev[MINMAX(0, (pkChr.GetLevel() + 15) - pkKiller.GetLevel(), LGEMiscellaneous.DEFINECONSTANTS.MAX_EXP_DELTA_OF_LEV - 1)]

        bRank = pkChr.GetMobRank()

        if 1 == number(1, 50000):
            iDeltaPercent.arg_value += 1000
        elif 1 == number(1, 10000):
            iDeltaPercent.arg_value += 500

        #sys_log(3, "CreateDropItem for level: %d rank: %u pct: %d", iLevel, bRank, iDeltaPercent.arg_value)
        iDeltaPercent.arg_value = math.trunc(iDeltaPercent.arg_value * CHARACTER_MANAGER.instance().GetMobItemRate(pkKiller) / float(100))

        if pkKiller.GetPremiumRemainSeconds(EPremiumTypes.PREMIUM_ITEM) > 0 or pkKiller.IsEquipUniqueGroup(uint(Globals.UNIQUE_GROUP_DOUBLE_ITEM)):
            iDeltaPercent.arg_value += iDeltaPercent.arg_value

        iRandRange.arg_value = 4000000
        iRandRange.arg_value = math.trunc(iRandRange.arg_value * 100 / float(100 if 100 + CPrivManager.instance().GetPriv(pkKiller, EPrivType.PRIV_ITEM_DROP) + pkKiller.IsEquipUniqueItem(uint(Globals.UNIQUE_ITEM_DOUBLE_ITEM)) 0 else 0))

        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if ENABLE_TARGET_INFO
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if ENABLE_TARGET_INFO
    def CreateDropItemVector(self, pkChr, pkKiller, vec_item):
        if pkChr is None or pkKiller is None:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if pkChr.IsPolymorphed() or pkChr.IsPC():
            return LGEMiscellaneous.DEFINECONSTANTS.false

        iLevel = pkKiller.GetLevel()

        bRank = pkChr.GetMobRank()
        item = None

        for c_rInfo in g_vec_pkCommonDropItem[bRank]:

            if iLevel < c_rInfo.m_iLevelStart or iLevel > c_rInfo.m_iLevelEnd:
                continue

            table = self.GetTable(c_rInfo.m_dwVnum)

            if table is None:
                continue

            item = None

            if table.bType == EItemTypes.ITEM_POLYMORPH:
                if c_rInfo.m_dwVnum == pkChr.GetPolymorphItemVnum():
                    item = self.CreateItem(c_rInfo.m_dwVnum, 1, 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), -1, DefineConstants.false)

                    if item:
                        item.SetSocket(0, pkChr.GetRaceNum(), ((not DefineConstants.false)))
            else:
                item = self.CreateItem(c_rInfo.m_dwVnum, 1, 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), -1, DefineConstants.false)

            if item:
                vec_item.append(item)

            it = self.m_map_pkDropItemGroup.find(pkChr.GetRaceNum())

            if it is not self.m_map_pkDropItemGroup.end():
                for groupItem in it.second.GetVector():
                    item = self.CreateItem(groupItem.dwVnum, groupItem.iCount, 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), -1, DefineConstants.false)

                    if item:
                        if item.GetType() == EItemTypes.ITEM_POLYMORPH:
                            if item.GetVnum() == pkChr.GetPolymorphItemVnum():
                                item.SetSocket(0, pkChr.GetRaceNum(), ((not DefineConstants.false)))

                        vec_item.append(item)

            it = self.m_map_pkMobItemGroup.find(pkChr.GetRaceNum())

            if it is not self.m_map_pkMobItemGroup.end():
                pGroup = it.second

                if pGroup is not None and not pGroup.IsEmpty():
                    info = pGroup.GetOne()
                    item = self.CreateItem(info.dwItemVnum, uint(info.iCount), 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), info.iRarePct, DefineConstants.false)

                    if item:
                        vec_item.append(item)

            it = self.m_map_pkLevelItemGroup.find(pkChr.GetRaceNum())
            if it is not self.m_map_pkLevelItemGroup.end():
                group = it.second

                if group.GetLevelLimit() <= iLevel:
                    for groupItem in group.GetVector():
                        item = self.CreateItem(groupItem.dwVNum, groupItem.iCount, 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), -1, DefineConstants.false)
                        if item:
                            vec_item.append(item)

            if pkKiller.GetPremiumRemainSeconds(EPremiumTypes.PREMIUM_ITEM) > 0 or pkKiller.IsEquipUniqueGroup(uint(Globals.UNIQUE_GROUP_DOUBLE_ITEM)):
                it = self.m_map_pkGloveItemGroup.find(pkChr.GetRaceNum())

                if it is not self.m_map_pkGloveItemGroup.end():
                    for groupItem in it.second.GetVector():
                        item = self.CreateItem(groupItem.dwVnum, groupItem.iCount, 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), -1, DefineConstants.false)
                        if item:
                            vec_item.append(item)

        if pkChr.GetMobDropItemVnum() != 0:

            it = self.m_map_dwEtcItemDropProb.find(pkChr.GetMobDropItemVnum())

            if it is not self.m_map_dwEtcItemDropProb.end():
                item = self.CreateItem(pkChr.GetMobDropItemVnum(), 1, 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), -1, DefineConstants.false)

                if item:
                    vec_item.append(item)

        if pkChr.IsStone():
            if pkChr.GetDropMetinStoneVnum() != 0:
                item = self.CreateItem(pkChr.GetDropMetinStoneVnum(), 1, 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), -1, DefineConstants.false)
                if item:
                    vec_item.append(item)

        return len(vec_item)
##endif

##endif
    def CreateDropItem(self, pkChr, pkKiller, vec_item):
        iLevel = pkKiller.GetLevel()

        iDeltaPercent = None
        iRandRange = None
        temp_ref_iDeltaPercent = RefObject(iDeltaPercent);
        temp_ref_iRandRange = RefObject(iRandRange);
        if not self.GetDropPct(pkChr, pkKiller, temp_ref_iDeltaPercent, temp_ref_iRandRange):
            iRandRange = temp_ref_iRandRange.arg_value
            iDeltaPercent = temp_ref_iDeltaPercent.arg_value
            return LGEMiscellaneous.DEFINECONSTANTS.false
        else:
            iRandRange = temp_ref_iRandRange.arg_value
            iDeltaPercent = temp_ref_iDeltaPercent.arg_value

        bRank = pkChr.GetMobRank()
        item = None

        it = g_vec_pkCommonDropItem[bRank].begin()

        while it is not g_vec_pkCommonDropItem[bRank].end():
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: const CItemDropInfo & c_rInfo = *(it++);
            c_rInfo = *(it)
            it += 1

            if iLevel < c_rInfo.m_iLevelStart or iLevel > c_rInfo.m_iLevelEnd:
                continue

            iPercent = math.trunc((c_rInfo.m_iPercent * iDeltaPercent) / float(100))
            #sys_log(3, "CreateDropItem %d ~ %d %d(%d)", c_rInfo.m_iLevelStart, c_rInfo.m_iLevelEnd, c_rInfo.m_dwVnum, iPercent, c_rInfo.m_iPercent)

            if iPercent >= number(1, iRandRange):
                table = self.GetTable(c_rInfo.m_dwVnum)

                if table is None:
                    continue

                item = None

                if table.bType == EItemTypes.ITEM_POLYMORPH:
                    if c_rInfo.m_dwVnum == pkChr.GetPolymorphItemVnum():
                        item = self.CreateItem(c_rInfo.m_dwVnum, 1, 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), -1, DefineConstants.false)

                        if item:
                            item.SetSocket(0, pkChr.GetRaceNum(), ((not DefineConstants.false)))
                else:
                    item = self.CreateItem(c_rInfo.m_dwVnum, 1, 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), -1, DefineConstants.false)

                if item:
                    vec_item.append(item)

            it = self.m_map_pkDropItemGroup.find(pkChr.GetRaceNum())

            if it is not self.m_map_pkDropItemGroup.end():
                v = it.second.GetVector()

                i = 0
                while i < v.size():
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
                    iPercent = (v[i].dwPct * iDeltaPercent) / 100

                    if iPercent >= number(1, iRandRange):
                        item = self.CreateItem(v[i].dwVnum, v[i].iCount, 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), -1, DefineConstants.false)

                        if item:
                            if item.GetType() == EItemTypes.ITEM_POLYMORPH:
                                if item.GetVnum() == pkChr.GetPolymorphItemVnum():
                                    item.SetSocket(0, pkChr.GetRaceNum(), ((not DefineConstants.false)))

                            vec_item.append(item)
                    i += 1

            it = self.m_map_pkMobItemGroup.find(pkChr.GetRaceNum())

            if it is not self.m_map_pkMobItemGroup.end():
                pGroup = it.second

                if pGroup is not None and not pGroup.IsEmpty():
                    iPercent = math.trunc(40000 * iDeltaPercent / float(pGroup.GetKillPerDrop()))
                    if iPercent >= number(1, iRandRange):
                        info = pGroup.GetOne()
                        item = self.CreateItem(info.dwItemVnum, uint(info.iCount), 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), info.iRarePct, DefineConstants.false)

                        if item:
                            vec_item.append(item)

            it = self.m_map_pkLevelItemGroup.find(pkChr.GetRaceNum())

            if it is not self.m_map_pkLevelItemGroup.end():
                if it.second.GetLevelLimit() <= iLevel:
                    v = it.second.GetVector()

                    i = 0
                    while i < v.size():
                        if v[i].dwPct >= number(1, 1000000):
                            dwVnum = v[i].dwVNum
                            item = self.CreateItem(dwVnum, v[i].iCount, 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), -1, DefineConstants.false)
                            if item:
                                vec_item.append(item)
                        i += 1

            if pkKiller.GetPremiumRemainSeconds(EPremiumTypes.PREMIUM_ITEM) > 0 or pkKiller.IsEquipUniqueGroup(uint(Globals.UNIQUE_GROUP_DOUBLE_ITEM)):
                it = self.m_map_pkGloveItemGroup.find(pkChr.GetRaceNum())

                if it is not self.m_map_pkGloveItemGroup.end():
                    v = it.second.GetVector()

                    i = 0
                    while i < v.size():
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
                        iPercent = (v[i].dwPct * iDeltaPercent) / 100

                        if iPercent >= number(1, iRandRange):
                            dwVnum = v[i].dwVnum
                            item = self.CreateItem(dwVnum, v[i].iCount, 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), -1, DefineConstants.false)
                            if item:
                                vec_item.append(item)
                        i += 1

        if pkChr.GetMobDropItemVnum() != 0:
            it = self.m_map_dwEtcItemDropProb.find(pkChr.GetMobDropItemVnum())

            if it is not self.m_map_dwEtcItemDropProb.end():
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
                iPercent = (it.second * iDeltaPercent) / 100

                if iPercent >= number(1, iRandRange):
                    item = self.CreateItem(pkChr.GetMobDropItemVnum(), 1, 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), -1, DefineConstants.false)
                    if item:
                        vec_item.append(item)

        if pkChr.IsStone():
            if pkChr.GetDropMetinStoneVnum() != 0:
                iPercent = (pkChr.GetDropMetinStonePct() * iDeltaPercent) * 400

                if iPercent >= number(1, iRandRange):
                    item = self.CreateItem(pkChr.GetDropMetinStoneVnum(), 1, 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), -1, DefineConstants.false)
                    if item:
                        vec_item.append(item)

        if pkKiller.IsHorseRiding() and Globals.GetDropPerKillPct(1000, 1000000, iDeltaPercent, "horse_LG_SKILL_book_drop") >= number(1, iRandRange):
            #sys_log(0, "EVENT HORSE_LG_SKILL_BOOK_DROP")

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((item = CreateItem(ITEM_HORSE_LG_SKILL_TRAIN_BOOK, 1, 0, (!DefineConstants.false))))
            if (item = self.CreateItem(uint(Globals.ITEM_HORSE_LG_SKILL_TRAIN_BOOK), 1, 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), -1, DefineConstants.false)):
                vec_item.append(item)

        self.CreateQuestDropItem(pkChr, pkKiller, vec_item, iDeltaPercent, iRandRange)

        for it in vec_item:
            item = *it

        return len(vec_item)

# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    ReadCommonDropItemFile(c_pszFileName)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    ReadEtcDropItemFile(c_pszFileName)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    ReadDropItemGroup(c_pszFileName)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    ReadMonsterDropItemGroup(c_pszFileName)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    ReadSpecialDropItemFile(c_pszFileName)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    ConvSpecialDropItemFile()
    def GetRefineFromVnum(self, dwVnum):
        it = self.m_map_ItemRefineFrom.find(dwVnum)
        if it is not self.m_map_ItemRefineFrom.end():
            return it.second
        return 0

    @staticmethod
    def CopyAllAttrTo(pkOldItem, pkNewItem):
        if pkOldItem.IsAccessoryForSocket():
            i = 0
            while i < EItemMisc.LG_ITEM_SOCKET_MAX_NUM:
                pkNewItem.SetSocket(i, pkOldItem.GetSocket(i), ((not DefineConstants.false)))
                i += 1
        else:
            i = 0
            while i < EItemMisc.LG_ITEM_SOCKET_MAX_NUM:
                if pkOldItem.GetSocket(i) == 0:
                    break
                else:
                    pkNewItem.SetSocket(i, 1, ((not DefineConstants.false)))
                i += 1

            slot = 0

            i = 0
            while i < EItemMisc.LG_ITEM_SOCKET_MAX_NUM:
                socket = pkOldItem.GetSocket(i)
                ITEM_BROKEN_METIN_VNUM = 28960
                if socket > 2 and socket != ITEM_BROKEN_METIN_VNUM:
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: pkNewItem->SetSocket(slot++, socket);
                    pkNewItem.SetSocket(slot, socket, ((not DefineConstants.false)))
                    slot += 1
                i += 1

        pkOldItem.CopyAttributeTo(pkNewItem)

    def GetSpecialItemGroup(self, dwVnum):
        it = self.m_map_pkSpecialItemGroup.find(dwVnum)
        if it is not self.m_map_pkSpecialItemGroup.end():
            return it.second
        return None

    def GetSpecialAttrGroup(self, dwVnum):
        it = self.m_map_pkSpecialAttrGroup.find(dwVnum)
        if it is not self.m_map_pkSpecialAttrGroup.end():
            return it.second
        return None

    def GetTable(self):
        return list(self.m_vec_prototype)
## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: int GetSpecialGroupFromItem(uint dwVnum) const
    def GetSpecialGroupFromItem(self, dwVnum):
        it = self.m_ItemToSpecialGroup.find(dwVnum)
        return 0 if (it is self.m_ItemToSpecialGroup.end()) else it.second

    def RealNumber(self, vnum):
        bot = None
        top = None
        mid = None

        bot = 0
        top = len(self.m_vec_prototype)

        pTable = self.m_vec_prototype[0]

        while True:
            mid = (bot + top) >> 1

            if (pTable + mid).dwVnum == vnum:
                return (mid)

            if bot >= top:
                return (-1)

            if (pTable + mid).dwVnum > vnum:
                top = mid - 1
            else:
                bot = mid + 1

    def CreateQuestDropItem(self, pkChr, pkKiller, vec_item, iDeltaPercent, iRandRange):
        item = None

        if pkChr is None:
            return

        if pkKiller is None:
            return

        #sys_log(1, "CreateQuestDropItem victim(%s), killer(%s)", pkChr.GetName(LOCALE_LANIATUS), pkKiller.GetName(LOCALE_LANIATUS))

        if (quest.CQuestManager.instance().GetEventFlag("xmas_sock")) != 0:
            SOCK_ITEM_VNUM = 50010

            iDropPerKill = [2000, 1000, 300, 50, 0, 0] + [0 for _ in range(EMobRank.MOB_RANK_MAX_NUM - 6)]

            if iDropPerKill[pkChr.GetMobRank()] != 0:
                iPercent = math.trunc(40000 * iDeltaPercent / float(iDropPerKill[pkChr.GetMobRank()]))

                #sys_log(0, "SOCK DROP %d %d", iPercent, iRandRange)
                if iPercent >= number(1, iRandRange):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((item = CreateItem(SOCK_ITEM_VNUM, 1, 0, (!DefineConstants.false))))
                    if (item = self.CreateItem(SOCK_ITEM_VNUM, 1, 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), -1, DefineConstants.false)):
                        vec_item.append(item)

        if (quest.CQuestManager.instance().GetEventFlag("drop_moon")) != 0:
            ITEM_VNUM = 50011

            iDropPerKill = [2000, 1000, 300, 50, 0, 0] + [0 for _ in range(EMobRank.MOB_RANK_MAX_NUM - 6)]

            if iDropPerKill[pkChr.GetMobRank()] != 0:
                iPercent = math.trunc(40000 * iDeltaPercent / float(iDropPerKill[pkChr.GetMobRank()]))

                if iPercent >= number(1, iRandRange):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((item = CreateItem(ITEM_VNUM, 1, 0, (!DefineConstants.false))))
                    if (item = self.CreateItem(ITEM_VNUM, 1, 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), -1, DefineConstants.false)):
                        vec_item.append(item)

        if pkKiller.GetLevel() >= 15 and abs(pkKiller.GetLevel() - pkChr.GetLevel()) <= 5:
            pct = quest.CQuestManager.instance().GetEventFlag("hc_drop")

            if pct > 0:
                ITEM_VNUM = 30178

                if number(1,100) <= pct:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((item = CreateItem(ITEM_VNUM, 1, 0, (!DefineConstants.false))))
                    if (item = self.CreateItem(ITEM_VNUM, 1, 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), -1, DefineConstants.false)):
                        vec_item.append(item)

        if Globals.GetDropPerKillPct(100, 2000, iDeltaPercent, "2006_drop") >= number(1, iRandRange):
            #sys_log(0, "�������� DROP EVENT ")

            DWVNUM = 50037

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((item = CreateItem(dwVnum, 1, 0, (!DefineConstants.false))))
            if (item = self.CreateItem(DWVNUM, 1, 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), -1, DefineConstants.false)):
                vec_item.append(item)


        if Globals.GetDropPerKillPct(100, 2000, iDeltaPercent, "2007_drop") >= number(1, iRandRange):
            #sys_log(0, "�������� DROP EVENT ")

            DWVNUM = 50043

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((item = CreateItem(dwVnum, 1, 0, (!DefineConstants.false))))
            if (item = self.CreateItem(DWVNUM, 1, 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), -1, DefineConstants.false)):
                vec_item.append(item)

        if Globals.GetDropPerKillPct(100, 1000, iDeltaPercent, "newyear_fire") >= number(1, iRandRange):
            ITEM_VNUM_FIRE = 50107

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((item = CreateItem(ITEM_VNUM_FIRE, 1, 0, (!DefineConstants.false))))
            if (item = self.CreateItem(ITEM_VNUM_FIRE, 1, 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), -1, DefineConstants.false)):
                vec_item.append(item)

        if Globals.GetDropPerKillPct(100, 500, iDeltaPercent, "newyear_moon") >= number(1, iRandRange):
            #sys_log(0, "EVENT NEWYEAR_MOON DROP")

            wonso_items = [50016, 50017, 50018, 50019, 50019, 50019]
            dwVnum = wonso_items[number(0,5)]

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((item = CreateItem(dwVnum, 1, 0, (!DefineConstants.false))))
            if (item = self.CreateItem(dwVnum, 1, 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), -1, DefineConstants.false)):
                vec_item.append(item)

        if Globals.GetDropPerKillPct(1, 2000, iDeltaPercent, "valentine_drop") >= number(1, iRandRange):
            #sys_log(0, "EVENT VALENTINE_DROP")

            valentine_items = [50024, 50025]
            dwVnum = valentine_items[number(0, 1)]

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((item = CreateItem(dwVnum, 1, 0, (!DefineConstants.false))))
            if (item = self.CreateItem(dwVnum, 1, 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), -1, DefineConstants.false)):
                vec_item.append(item)

        if Globals.GetDropPerKillPct(100, 2000, iDeltaPercent, "icecream_drop") >= number(1, iRandRange):
            ICECREAM = 50123

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((item = CreateItem(icecream, 1, 0, (!DefineConstants.false))))
            if (item = self.CreateItem(ICECREAM, 1, 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), -1, DefineConstants.false)):
                vec_item.append(item)

        if (pkKiller.CountSpecifyItem(53002, -1) > 0) and (Globals.GetDropPerKillPct(50, 100, iDeltaPercent, "new_xmas_event") >= number(1, iRandRange)):
            XMAS_SOCK = 50010
            pkKiller.AutoGiveItem(XMAS_SOCK, 1)

        if (pkKiller.CountSpecifyItem(53007, -1) > 0) and (Globals.GetDropPerKillPct(50, 100, iDeltaPercent, "new_xmas_event") >= number(1, iRandRange)):
            XMAS_SOCK = 50010
            pkKiller.AutoGiveItem(XMAS_SOCK, 1)

        if Globals.GetDropPerKillPct(100, 2000, iDeltaPercent, "halloween_drop") >= number(1, iRandRange):
            HALLOWEEN_ITEM = 30321

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((item=CreateItem(halloween_item, 1, 0, (!DefineConstants.false))))
            if (item = self.CreateItem(HALLOWEEN_ITEM, 1, 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), -1, DefineConstants.false)):
                vec_item.append(item)

        if Globals.GetDropPerKillPct(100, 2000, iDeltaPercent, "ramadan_drop") >= number(1, iRandRange):
            RAMADAN_ITEM = 30315

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((item=CreateItem(ramadan_item, 1, 0, (!DefineConstants.false))))
            if (item = self.CreateItem(RAMADAN_ITEM, 1, 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), -1, DefineConstants.false)):
                vec_item.append(item)

        if Globals.GetDropPerKillPct(100, 2000, iDeltaPercent, "easter_drop") >= number(1, iRandRange):
            EASTER_ITEM_BASE = 50160

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((item=CreateItem(easter_item_base+number(0,19), 1, 0, (!DefineConstants.false))))
            if (item = self.CreateItem(EASTER_ITEM_BASE+number(0,19), 1, 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), -1, DefineConstants.false)):
                vec_item.append(item)

        if Globals.GetDropPerKillPct(100, 2000, iDeltaPercent, "football_drop") >= number(1, iRandRange):
            FOOTBALL_ITEM = 50096

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((item=CreateItem(football_item, 1, 0, (!DefineConstants.false))))
            if (item = self.CreateItem(FOOTBALL_ITEM, 1, 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), -1, DefineConstants.false)):
                vec_item.append(item)

        if Globals.GetDropPerKillPct(100, 2000, iDeltaPercent, "whiteday_drop") >= number(1, iRandRange):
            #sys_log(0, "EVENT WHITEDAY_DROP")
            whiteday_items = [Globals.ITEM_WHITEDAY_ROSE, Globals.ITEM_WHITEDAY_CANDY]
            dwVnum = whiteday_items[number(0,1)]

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((item = CreateItem(dwVnum, 1, 0, (!DefineConstants.false))))
            if (item = self.CreateItem(dwVnum, 1, 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), -1, DefineConstants.false)):
                vec_item.append(item)

        if pkKiller.GetLevel()>=50:
            if Globals.GetDropPerKillPct(100, 1000, iDeltaPercent, "kids_day_drop_high") >= number(1, iRandRange):
                ITEM_QUIZ_BOX = 50034

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((item = CreateItem(ITEM_QUIZ_BOX, 1, 0, (!DefineConstants.false))))
                if (item = self.CreateItem(ITEM_QUIZ_BOX, 1, 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), -1, DefineConstants.false)):
                    vec_item.append(item)
        else:
            if Globals.GetDropPerKillPct(100, 1000, iDeltaPercent, "kids_day_drop") >= number(1, iRandRange):
                ITEM_QUIZ_BOX = 50034

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((item = CreateItem(ITEM_QUIZ_BOX, 1, 0, (!DefineConstants.false))))
                if (item = self.CreateItem(ITEM_QUIZ_BOX, 1, 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), -1, DefineConstants.false)):
                    vec_item.append(item)

        if pkChr.GetLevel() >= 30 and Globals.GetDropPerKillPct(50, 100, iDeltaPercent, "medal_part_drop") >= number(1, iRandRange):
            drop_items = [30265, 30266, 30267, 30268, 30269]
            i = number(0, 4)
            item = self.CreateItem(drop_items[i], 1, 0, DefineConstants.false, -1, DefineConstants.false)
            if item is not None:
                vec_item.append(item)

        if pkChr.GetLevel() >= 40 and pkChr.GetMobRank() >= EMobRank.MOB_RANK_BOSS and math.trunc(Globals.GetDropPerKillPct(1, 1000, iDeltaPercent, "three_LG_SKILL_item") / float(Globals.GetThreeSkillLevelAdjust(pkChr.GetLevel()))) >= number(1, iRandRange):
            ITEM_VNUM = 50513

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((item = CreateItem(ITEM_VNUM, 1, 0, (!DefineConstants.false))))
            if (item = self.CreateItem(ITEM_VNUM, 1, 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), -1, DefineConstants.false)):
                vec_item.append(item)

        if pkKiller.GetLevel() >= 15 and (quest.CQuestManager.instance().GetEventFlag("mars_drop")) != 0:
            ITEM_HANIRON = 70035
            iDropMultiply = [50, 30, 5, 1, 0, 0] + [0 for _ in range(EMobRank.MOB_RANK_MAX_NUM - 6)]

            if iDropMultiply[pkChr.GetMobRank()] != 0 and Globals.GetDropPerKillPct(1000, 1500, iDeltaPercent, "mars_drop") >= number(1, iRandRange) * iDropMultiply[pkChr.GetMobRank()]:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((item = CreateItem(ITEM_HANIRON, 1, 0, (!DefineConstants.false))))
                if (item = self.CreateItem(ITEM_HANIRON, 1, 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), -1, DefineConstants.false)):
                    vec_item.append(item)




    def GetMaskVnum(self, dwVnum):
        it = self._m_map_new_to_ori.find(dwVnum)
        if it is not self._m_map_new_to_ori.end():
            return it.second
        else:
            return 0

    def GetVIDMap(self):
        return dict(self.m_map_vid)
    def GetVecProto(self):
        return list(self.m_vec_prototype)

    MAX_NORM_ATTR_NUM = 5
    MAX_RARE_ATTR_NUM = 2
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    ReadItemVnumMaskTable(c_pszFileName)

## Laniatus Games Studio Inc. | NOTE: The following #define macro was replaced in-line:
#ORIGINAL METINII C CODE: #define M2_DESTROY_ITEM(ptr) ITEM_MANAGER::instance().DestroyItem(ptr)

class CItemDropInfo:
    def __init__(self, iLevelStart, iLevelEnd, iPercent, dwVnum):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.m_iLevelStart = 0
        self.m_iLevelEnd = 0
        self.m_iPercent = 0
        self.m_dwVnum = 0

        self.m_iLevelStart = iLevelStart
        self.m_iLevelEnd = iLevelEnd
        self.m_iPercent = iPercent
        self.m_dwVnum = dwVnum


## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python has no concept of a 'friend' function:
#ORIGINAL METINII C CODE: friend bool operator < (const CItemDropInfo & l, const CItemDropInfo & r)
    def less_than(self, l, r):
        return l.m_iLevelEnd < r.m_iLevelEnd