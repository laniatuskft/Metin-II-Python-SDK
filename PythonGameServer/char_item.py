from enum import Enum
import math

class FFindStone:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.m_mapStone = {}


    def functor_method(self, pEnt):
        if pEnt.IsType(EEntityTypes.ENTITY_CHARACTER) == ((not LGEMiscellaneous.DEFINECONSTANTS.false)):
            pChar = pEnt

            if pChar.IsStone() == ((not LGEMiscellaneous.DEFINECONSTANTS.false)):
                self.m_mapStone[pChar.GetVID()] = pChar

def CanHandleItem(bSkipCheckRefine, bSkipObserver):
    if not bSkipObserver:
        if m_bIsObserver:
            return LGEMiscellaneous.DEFINECONSTANTS.false

    if GetMyShop():
        return LGEMiscellaneous.DEFINECONSTANTS.false

    if not bSkipCheckRefine:
        if m_bUnderRefine:
            return LGEMiscellaneous.DEFINECONSTANTS.false

    if IsCubeOpen() or None != DragonSoul_RefineWindow_GetOpener():
        return LGEMiscellaneous.DEFINECONSTANTS.false

    if IsWarping():
        return LGEMiscellaneous.DEFINECONSTANTS.false

    if IsAcceWindowOpen():
        return LGEMiscellaneous.DEFINECONSTANTS.false

    return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: CItem* CHARACTER::GetInventoryItem(ushort wCell) const
def GetInventoryItem(wCell):
    return GetItem(TItemPos(EWindows.INVENTORY, wCell))
## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: CItem* CHARACTER::GetItem(TItemPos Cell) const
def GetItem(Cell):
    if not IsValidItemPosition(Cell):
        return None
    wCell = Cell.cell
    window_type = Cell.window_type
    if (window_type == EWindows.INVENTORY) or (window_type == EWindows.EQUIPMENT):
        if wCell >= LGEMiscellaneous2.INVENTORY_AND_EQUIP_SLOT_MAX:
            #lani_err("CHARACTER::GetInventoryItem: invalid item cell %d", wCell)
            return None
        return m_pointsInstant.pItems[wCell]
    if (window_type == EWindows.INVENTORY) or (window_type == EWindows.EQUIPMENT) or (window_type == EWindows.DRAGON_SOUL_INVENTORY):
        if wCell >= EDSInventoryMaxNum.DRAGON_SOUL_INVENTORY_MAX_NUM:
            #lani_err("CHARACTER::GetInventoryItem: invalid DS item cell %d", wCell)
            return None
        return m_pointsInstant.pDSItems[wCell]


    if True:
        return None
    return None

def SetItem(Cell, pItem):
    wCell = Cell.cell
    window_type = Cell.window_type
    if (pItem) == 0xff or (pItem) == 0xffffffff:
        #lani_err("!!! FATAL ERROR !!! item == 0xff (char: %s cell: %u)", GetName(), wCell)
        core_dump()
        return

    if pItem is not None and pItem.GetOwner() is not None:
        assert not "GetOwner exist"
        return

    if (window_type == EWindows.INVENTORY) or (window_type == EWindows.EQUIPMENT):
            if wCell >= LGEMiscellaneous2.INVENTORY_AND_EQUIP_SLOT_MAX:
                #lani_err("CHARACTER::SetItem: invalid item cell %d", wCell)
                return

            pOld = m_pointsInstant.pItems[wCell]

            if pOld:
                if wCell < LGEMiscellaneous.INVENTORY_MAX_NUM:
                    i = 0
                    while i < pOld.GetSize():
                        p = wCell + (i * 5)

                        if p >= LGEMiscellaneous.INVENTORY_MAX_NUM:
                            continue

                        if m_pointsInstant.pItems[p] and m_pointsInstant.pItems[p] is not pOld:
                            continue

                        m_pointsInstant.wItemGrid[p] = 0
                        i += 1
                else:
                    m_pointsInstant.wItemGrid[wCell] = 0

            if pItem:
                if wCell < LGEMiscellaneous.INVENTORY_MAX_NUM:
                    i = 0
                    while i < pItem.GetSize():
                        p = wCell + (i * 5)

                        if p >= LGEMiscellaneous.INVENTORY_MAX_NUM:
                            continue

                        m_pointsInstant.wItemGrid[p] = wCell + 1
                        i += 1
                else:
                    m_pointsInstant.wItemGrid[wCell] = wCell + 1

            m_pointsInstant.pItems[wCell] = pItem

    elif window_type == EWindows.DRAGON_SOUL_INVENTORY:
            pOld = m_pointsInstant.pDSItems[wCell]

            if pOld:
                if wCell < EDSInventoryMaxNum.DRAGON_SOUL_INVENTORY_MAX_NUM:
                    i = 0
                    while i < pOld.GetSize():
                        p = wCell + (i * int(LGEMiscellaneous.DRAGON_SOUL_BOX_COLUMN_NUM))

                        if p >= EDSInventoryMaxNum.DRAGON_SOUL_INVENTORY_MAX_NUM:
                            continue

                        if m_pointsInstant.pDSItems[p] and m_pointsInstant.pDSItems[p] is not pOld:
                            continue

                        m_pointsInstant.wDSItemGrid[p] = 0
                        i += 1
                else:
                    m_pointsInstant.wDSItemGrid[wCell] = 0

            if pItem:
                if wCell >= EDSInventoryMaxNum.DRAGON_SOUL_INVENTORY_MAX_NUM:
                    #lani_err("CHARACTER::SetItem: invalid DS item cell %d", wCell)
                    return

                if wCell < EDSInventoryMaxNum.DRAGON_SOUL_INVENTORY_MAX_NUM:
                    i = 0
                    while i < pItem.GetSize():
                        p = wCell + (i * int(LGEMiscellaneous.DRAGON_SOUL_BOX_COLUMN_NUM))

                        if p >= EDSInventoryMaxNum.DRAGON_SOUL_INVENTORY_MAX_NUM:
                            continue

                        m_pointsInstant.wDSItemGrid[p] = wCell + 1
                        i += 1
                else:
                    m_pointsInstant.wDSItemGrid[wCell] = wCell + 1

            m_pointsInstant.pDSItems[wCell] = pItem

    else:
        #lani_err("Invalid Inventory type %d", window_type)
        return

    if GetDesc():
        if pItem:
            pack = packet_item_set()
            pack.header = byte(LG_HEADER_GC_ITEM_SET)
## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: pack.Cell = Cell;
            pack.Cell.copy_from(Cell)

            pack.count = ushort(pItem.GetCount())
            pack.vnum = pItem.GetVnum()
            pack.flags = uint(pItem.GetFlag())
            pack.anti_flags = pItem.GetAntiFlag()
            pack.highlight = (Cell.window_type == EWindows.DRAGON_SOUL_INVENTORY)


## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memcpy' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            memcpy(pack.alSockets, pItem.GetSockets(), sizeof(pack.alSockets))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memcpy' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            memcpy(pack.aAttr, pItem.GetAttributes(), sizeof(pack.aAttr))

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            GetDesc().Packet(pack, sizeof(packet_item_set))
        else:
            pack = TPacketGCItemDelDeprecated()
            pack.header = byte(LG_HEADER_GC_ITEM_DEL)
## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: pack.Cell = Cell;
            pack.Cell.copy_from(Cell)
            pack.count = 0
            pack.vnum = 0
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            memset(pack.alSockets, 0, sizeof(pack.alSockets))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            memset(pack.aAttr, 0, sizeof(pack.aAttr))

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            GetDesc().Packet(pack, sizeof(TPacketGCItemDelDeprecated))

    if pItem:
        pItem.SetCell(self, wCell)
        if (window_type == EWindows.INVENTORY) or (window_type == EWindows.EQUIPMENT):
            if (wCell < LGEMiscellaneous.INVENTORY_MAX_NUM) or (LGEMiscellaneous2.BELT_INVENTORY_SLOT_START <= wCell and LGEMiscellaneous2.BELT_INVENTORY_SLOT_END > wCell):
                pItem.SetWindow(EWindows.INVENTORY)
            else:
                pItem.SetWindow(EWindows.EQUIPMENT)
        elif window_type == EWindows.DRAGON_SOUL_INVENTORY:
            pItem.SetWindow(EWindows.DRAGON_SOUL_INVENTORY)

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: CItem* CHARACTER::GetWear(ushort wCell) const
def GetWear(wCell):
    if wCell >= EWearPositions.WEAR_MAX_NUM + EDragonSoulDeckType.DRAGON_SOUL_DECK_MAX_NUM * EDragonSoulSubType.DS_SLOT_MAX:
        #lani_err("CHARACTER::GetWear: invalid wear cell %d", wCell)
        return None

    return m_pointsInstant.pItems[(int)LGEMiscellaneous.INVENTORY_MAX_NUM + wCell]

def SetWear(wCell, item):
    if wCell >= EWearPositions.WEAR_MAX_NUM + EDragonSoulDeckType.DRAGON_SOUL_DECK_MAX_NUM * EDragonSoulSubType.DS_SLOT_MAX:
        #lani_err("CHARACTER::SetItem: invalid item cell %d", wCell)
        return

    SetItem(TItemPos(EWindows.INVENTORY, LGEMiscellaneous.INVENTORY_MAX_NUM + wCell), item)

    if item is None and wCell == EWearPositions.WEAR_WEAPON:
        if IsAffectFlag(EAffectBits.AFF_GWIGUM):
            RemoveAffect(LaniatusETalentXes.LG_SKILL_GWIGEOM)

        if IsAffectFlag(EAffectBits.AFF_GEOMGYEONG):
            RemoveAffect(LaniatusETalentXes.LG_SKILL_GEOMKYUNG)

def ClearItem():
    i = None
    item = None

    i = 0
    while i < LGEMiscellaneous2.INVENTORY_AND_EQUIP_SLOT_MAX:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((item = GetInventoryItem(i)))
        if (item = GetInventoryItem(i)):
            item.SetSkipSave(((not LGEMiscellaneous.DEFINECONSTANTS.false)))
            ITEM_MANAGER.instance().FlushDelayedSave(item)

            item.RemoveFromCharacter()
            ITEM_MANAGER.instance().DestroyItem(item)

            SyncQuickslot(LG_QUICKSLOT_TYPE_ITEM, i, 255)
        i += 1
    i = 0
    while i < EDSInventoryMaxNum.DRAGON_SOUL_INVENTORY_MAX_NUM:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((item = GetItem(TItemPos(DRAGON_SOUL_INVENTORY, i))))
        if (item = GetItem(TItemPos(EWindows.DRAGON_SOUL_INVENTORY, i))):
            item.SetSkipSave(((not LGEMiscellaneous.DEFINECONSTANTS.false)))
            ITEM_MANAGER.instance().FlushDelayedSave(item)

            item.RemoveFromCharacter()
            ITEM_MANAGER.instance().DestroyItem(item)
        i += 1

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: bool CHARACTER::IsEmptyItemGrid(TItemPos Cell, byte bSize, int iExceptionCell) const
def IsEmptyItemGrid(Cell, bSize, iExceptionCell):
    if Cell.window_type == EWindows.INVENTORY:
            wCell = Cell.cell
            iExceptionCell += 1

            if Cell.IsBeltInventoryPosition():
                beltItem = GetWear(EWearPositions.WEAR_BELT)

                if None is beltItem:
                    return LGEMiscellaneous.DEFINECONSTANTS.false

                if LGEMiscellaneous.DEFINECONSTANTS.false == CBeltInventoryHelper.IsAvailableCell(ushort(wCell - ushort(LGEMiscellaneous2.BELT_INVENTORY_SLOT_START)), beltItem.GetValue(0)):
                    return LGEMiscellaneous.DEFINECONSTANTS.false

                if m_pointsInstant.wItemGrid[wCell]:
                    if m_pointsInstant.wItemGrid[wCell] == iExceptionCell:
                        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

                    return LGEMiscellaneous.DEFINECONSTANTS.false

                if bSize == 1:
                    return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

            elif wCell >= LGEMiscellaneous.INVENTORY_MAX_NUM:
                return LGEMiscellaneous.DEFINECONSTANTS.false

            if m_pointsInstant.wItemGrid[wCell]:
                if m_pointsInstant.wItemGrid[wCell] == iExceptionCell:
                    if bSize == 1:
                        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

                    j = 1
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
                    bPage = wCell / (LGEMiscellaneous.INVENTORY_MAX_NUM / LGEMiscellaneous.INVENTORY_PAGE_NUM)

                    condition = True
                    while condition:
                        p = wCell + (LGEMiscellaneous.INVENTORY_WIDTH * j)

                        if p >= LGEMiscellaneous.INVENTORY_MAX_NUM:
                            return LGEMiscellaneous.DEFINECONSTANTS.false

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
                        if p / (LGEMiscellaneous.INVENTORY_MAX_NUM / LGEMiscellaneous.INVENTORY_PAGE_NUM) != bPage:
                            return LGEMiscellaneous.DEFINECONSTANTS.false

                        if m_pointsInstant.wItemGrid[p]:
                            if m_pointsInstant.wItemGrid[p] != iExceptionCell:
                                return LGEMiscellaneous.DEFINECONSTANTS.false
                        j += 1
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: } while (++j < bSize);
                        condition = j < bSize

                    return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
                else:
                    return LGEMiscellaneous.DEFINECONSTANTS.false
            if 1 == bSize:
                return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
            else:
                j = 1
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
                bPage = wCell / (LGEMiscellaneous.INVENTORY_MAX_NUM / LGEMiscellaneous.INVENTORY_PAGE_NUM)

                condition = True
                while condition:
                    p = wCell + (LGEMiscellaneous.INVENTORY_WIDTH * j)

                    if p >= LGEMiscellaneous.INVENTORY_MAX_NUM:
                        return LGEMiscellaneous.DEFINECONSTANTS.false

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
                    if p / (LGEMiscellaneous.INVENTORY_MAX_NUM / LGEMiscellaneous.INVENTORY_PAGE_NUM) != bPage:
                        return LGEMiscellaneous.DEFINECONSTANTS.false

                    if m_pointsInstant.wItemGrid[p]:
                        if m_pointsInstant.wItemGrid[p] != iExceptionCell:
                            return LGEMiscellaneous.DEFINECONSTANTS.false
                    j += 1
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: } while (++j < bSize);
                    condition = j < bSize

                return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
    elif Cell.window_type == EWindows.DRAGON_SOUL_INVENTORY:
            wCell = Cell.cell
            if wCell >= EDSInventoryMaxNum.DRAGON_SOUL_INVENTORY_MAX_NUM:
                return LGEMiscellaneous.DEFINECONSTANTS.false

            iExceptionCell += 1

            if m_pointsInstant.wDSItemGrid[wCell]:
                if m_pointsInstant.wDSItemGrid[wCell] == iExceptionCell:
                    if bSize == 1:
                        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

                    j = 1

                    condition = True
                    while condition:
                        p = wCell + (LGEMiscellaneous.DRAGON_SOUL_BOX_COLUMN_NUM * j)

                        if p >= EDSInventoryMaxNum.DRAGON_SOUL_INVENTORY_MAX_NUM:
                            return LGEMiscellaneous.DEFINECONSTANTS.false

                        if m_pointsInstant.wDSItemGrid[p]:
                            if m_pointsInstant.wDSItemGrid[p] != iExceptionCell:
                                return LGEMiscellaneous.DEFINECONSTANTS.false
                        j += 1
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: } while (++j < bSize);
                        condition = j < bSize

                    return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
                else:
                    return LGEMiscellaneous.DEFINECONSTANTS.false

            if 1 == bSize:
                return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
            else:
                j = 1

                condition = True
                while condition:
                    p = wCell + (LGEMiscellaneous.DRAGON_SOUL_BOX_COLUMN_NUM * j)

                    if p >= EDSInventoryMaxNum.DRAGON_SOUL_INVENTORY_MAX_NUM:
                        return LGEMiscellaneous.DEFINECONSTANTS.false

                    if m_pointsInstant.wItemGrid[p]:
                        if m_pointsInstant.wDSItemGrid[p] != iExceptionCell:
                            return LGEMiscellaneous.DEFINECONSTANTS.false
                    j += 1
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: } while (++j < bSize);
                    condition = j < bSize

                return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
    return LGEMiscellaneous.DEFINECONSTANTS.false

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: int CHARACTER::GetEmptyInventory(byte size) const
def GetEmptyInventory(size):
    i = 0
    while i < LGEMiscellaneous.INVENTORY_MAX_NUM:
        if IsEmptyItemGrid(TItemPos(EWindows.INVENTORY, i), size):
            return i
        i += 1
    return -1

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: int CHARACTER::GetEmptyDragonSoulInventory(CItem* pItem) const
def GetEmptyDragonSoulInventory(pItem):
    if None is pItem or not pItem.IsDragonSoul():
        return -1
    if not DragonSoul_IsQualified():
        return -1
    bSize = pItem.GetSize()
    wBaseCell = DSManager.instance().GetBasePosition(pItem)

    if LGEMiscellaneous.DEFINECONSTANTS.WORD_MAX == wBaseCell:
        return -1

    i = 0
    while i < LGEMiscellaneous.DRAGON_SOUL_BOX_SIZE:
        if IsEmptyItemGrid(TItemPos(EWindows.DRAGON_SOUL_INVENTORY, i + wBaseCell), bSize):
            return i + wBaseCell
        i += 1

    return -1

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: void CHARACTER::CopyDragonSoulItemGrid(list<ushort>& vDragonSoulItemGrid) const
def CopyDragonSoulItemGrid(vDragonSoulItemGrid):
    vDragonSoulItemGrid.resize(EDSInventoryMaxNum.DRAGON_SOUL_INVENTORY_MAX_NUM)

    std::copy(m_pointsInstant.wDSItemGrid, m_pointsInstant.wDSItemGrid + EDSInventoryMaxNum.DRAGON_SOUL_INVENTORY_MAX_NUM, vDragonSoulItemGrid.begin())

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: int CHARACTER::CountEmptyInventory() const
def CountEmptyInventory():
    count = 0

    i = 0
    while i < LGEMiscellaneous.INVENTORY_MAX_NUM:
        if GetInventoryItem(i):
            count += GetInventoryItem(i).GetSize()
        i += 1

    return (LGEMiscellaneous.INVENTORY_MAX_NUM - count)

def SetRefineNPC(ch):
    if ch is not None:
        m_dwRefineNPCVID = ch.GetVID()
    else:
        m_dwRefineNPCVID = 0

def DoRefine(item, bMoneyOnly):
    if not CanHandleItem(((not LGEMiscellaneous.DEFINECONSTANTS.false))):
        ClearRefineMode()
        return LGEMiscellaneous.DEFINECONSTANTS.false

    if quest.CQuestManager.instance().GetEventFlag("update_refine_time") != 0:
        if get_global_time() < quest.CQuestManager.instance().GetEventFlag("update_refine_time") + (60 * 5):
            #sys_log(0, "can't refine %d %s", GetPlayerID(), GetName())
            return LGEMiscellaneous.DEFINECONSTANTS.false

    prt = CRefineManager.instance().GetRefineRecipe(item.GetRefineSet())

    if prt is None:
        return LGEMiscellaneous.DEFINECONSTANTS.false

    result_vnum = item.GetRefinedVnum()

    cost = ComputeRefineFee(prt.cost)

    RefineChance = GetQuestFlag("main_quest_lv7.refine_chance")

    if RefineChance > 0:
        if (not item.CheckItemUseLevel(20)) or item.GetType() != EItemTypes.ITEM_WEAPON:
            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Free advancement is only for weapons up to level 20."))
            return LGEMiscellaneous.DEFINECONSTANTS.false

        cost = 0
        SetQuestFlag("main_quest_lv7.refine_chance", RefineChance - 1)

    if item.GetCount() > 1:
        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You cannot refine a stacked item."))

    if result_vnum == 0:
        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("No advancement possible."))
        return LGEMiscellaneous.DEFINECONSTANTS.false

    if item.GetType() == EItemTypes.ITEM_USE and item.GetSubType() == EUseSubTypes.USE_TUNING:
        return LGEMiscellaneous.DEFINECONSTANTS.false

    pProto = ITEM_MANAGER.instance().GetTable(item.GetRefinedVnum())

    if pProto is None:
        #lani_err("DoRefine NOT GET ITEM PROTO %d", item.GetRefinedVnum())
        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("This Item can't be made better."))
        return LGEMiscellaneous.DEFINECONSTANTS.false

    if GetGold() < cost:
        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Not enough Yang for an advancement."))
        return LGEMiscellaneous.DEFINECONSTANTS.false

    if (not bMoneyOnly) and RefineChance == 0:
        i = 0
        while i < prt.material_count:
            if CountSpecifyItem(prt.materials[i].vnum, item.GetCell()) < prt.materials[i].count:
                if test_server:
                    ChatPacket(EChatType.CHAT_TYPE_INFO, "Find %d, count %d, require %d", prt.materials[i].vnum, CountSpecifyItem(prt.materials[i].vnum), prt.materials[i].count)
                ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Not enough material for an advancement."))
                return LGEMiscellaneous.DEFINECONSTANTS.false
            i += 1

        i = 0
        while i < prt.material_count:
            RemoveSpecifyItem(prt.materials[i].vnum, prt.materials[i].count, item.GetCell())
            i += 1

    prob = number(1, 100)

    if IsRefineThroughGuild() or bMoneyOnly:
        prob -= 10

    if prob <= prt.prob:
        pkNewItem = ITEM_MANAGER.instance().CreateItem(result_vnum, 1, 0, LGEMiscellaneous.DEFINECONSTANTS.false, -1, DefineConstants.false)

        if pkNewItem:
            olditem = item.GetID()
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to pointers to value types:
#ORIGINAL METINII C CODE: const char* itemname = item->GetName();
            itemname = item.GetName(LOCALE_LANIATUS)

            ITEM_MANAGER.CopyAllAttrTo(item, pkNewItem)
            wCell = item.GetCell()
            NotifyRefineSuccess(self, item,"GUILD" if IsRefineThroughGuild() else "POWER")
            ITEM_MANAGER.instance().RemoveItem(item, "REMOVE (REFINE SUCCESS)")
            pkNewItem.AddToCharacter(self, TItemPos(EWindows.INVENTORY, wCell))
            ITEM_MANAGER.instance().FlushDelayedSave(pkNewItem)

            LogManager.instance().RefineLog(GetName(), itemname, olditem, pkNewItem.GetID(), "SUCESS")

            #sys_log(0, "Refine Success %d", cost)
            #sys_log(0, "PayPee %d", cost)
            PayRefineFee(cost)
            #sys_log(0, "PayPee End %d", cost)
        else:
            #lani_err("cannot create item %u", result_vnum)
            NotifyRefineFail(self, item,"GUILD" if IsRefineThroughGuild() else "POWER", 0)
    else:
        LogManager.instance().RefineLog(GetName(), item.GetName(LOCALE_LANIATUS), item.GetID(), 0, "FAILED")
        NotifyRefineFail(self, item,"GUILD" if IsRefineThroughGuild() else "POWER", 0)
        ITEM_MANAGER.instance().RemoveItem(item, "REMOVE (REFINE FAIL)")
        PayRefineFee(cost)

    return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

class enum_RefineScrolls(Enum):
    CHUKBOK_SCROLL = 0
    HYUNIRON_CHN = 1
    YONGSIN_SCROLL = 2
    MUSIN_SCROLL = 3
    YAGONG_SCROLL = 4
    MEMO_SCROLL = 5
    BDRAGON_SCROLL = 6

def DoRefineWithScroll(item):
    if not CanHandleItem(((not LGEMiscellaneous.DEFINECONSTANTS.false))):
        ClearRefineMode()
        return LGEMiscellaneous.DEFINECONSTANTS.false

    ClearRefineMode()

    if quest.CQuestManager.instance().GetEventFlag("update_refine_time") != 0:
        if get_global_time() < quest.CQuestManager.instance().GetEventFlag("update_refine_time") + (60 * 5):
            #sys_log(0, "can't refine %d %s", GetPlayerID(), GetName())
            return LGEMiscellaneous.DEFINECONSTANTS.false

    prt = CRefineManager.instance().GetRefineRecipe(item.GetRefineSet())

    if prt is None:
        return LGEMiscellaneous.DEFINECONSTANTS.false

    pkItemScroll = None

    if m_iRefineAdditionalCell < 0:
        return LGEMiscellaneous.DEFINECONSTANTS.false

    pkItemScroll = GetInventoryItem(m_iRefineAdditionalCell)

    if pkItemScroll is None:
        return LGEMiscellaneous.DEFINECONSTANTS.false

    if not(pkItemScroll.GetType() == EItemTypes.ITEM_USE and pkItemScroll.GetSubType() == EUseSubTypes.USE_TUNING):
        return LGEMiscellaneous.DEFINECONSTANTS.false

    if pkItemScroll.GetVnum() == item.GetVnum():
        return LGEMiscellaneous.DEFINECONSTANTS.false

    result_vnum = item.GetRefinedVnum()
    result_fail_vnum = item.GetRefineFromVnum()

    if item.GetCount() > 1:
        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You cannot refine a stacked item."))

    if result_vnum == 0:
        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("No advancement possible."))
        return LGEMiscellaneous.DEFINECONSTANTS.false

    if pkItemScroll.GetValue(0) == enum_RefineScrolls.MUSIN_SCROLL:
        if item.GetRefineLevel() >= 4:
            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("This Advancement scroll isn't available for you at the moment."))
            return LGEMiscellaneous.DEFINECONSTANTS.false

    elif pkItemScroll.GetValue(0) == enum_RefineScrolls.MEMO_SCROLL:
        if item.GetRefineLevel() != pkItemScroll.GetValue(1):
            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You can't advance with this Scroll."))
            return LGEMiscellaneous.DEFINECONSTANTS.false
    elif pkItemScroll.GetValue(0) == enum_RefineScrolls.BDRAGON_SCROLL:
        if item.GetType() != EItemTypes.ITEM_METIN or item.GetRefineLevel() != 4:
            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You cannot upgrade this item."))
            return LGEMiscellaneous.DEFINECONSTANTS.false

    pProto = ITEM_MANAGER.instance().GetTable(item.GetRefinedVnum())

    if pProto is None:
        #lani_err("DoRefineWithScroll NOT GET ITEM PROTO %d", item.GetRefinedVnum())
        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("This Item can't be made better."))
        return LGEMiscellaneous.DEFINECONSTANTS.false

    if GetGold() < prt.cost:
        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Not enough Yang for an advancement."))
        return LGEMiscellaneous.DEFINECONSTANTS.false

    i = 0
    while i < prt.material_count:
        if CountSpecifyItem(prt.materials[i].vnum, item.GetCell()) < prt.materials[i].count:
            if test_server:
                ChatPacket(EChatType.CHAT_TYPE_INFO, "Find %d, count %d, require %d", prt.materials[i].vnum, CountSpecifyItem(prt.materials[i].vnum), prt.materials[i].count)
            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Not enough material for an advancement."))
            return LGEMiscellaneous.DEFINECONSTANTS.false
        i += 1

    i = 0
    while i < prt.material_count:
        RemoveSpecifyItem(prt.materials[i].vnum, prt.materials[i].count, item.GetCell())
        i += 1

    prob = number(1, 100)
    success_prob = prt.prob
    bDestroyWhenFail = LGEMiscellaneous.DEFINECONSTANTS.false

    szRefineType = "SCROLL"

    if pkItemScroll.GetValue(0) == enum_RefineScrolls.HYUNIRON_CHN or pkItemScroll.GetValue(0) == enum_RefineScrolls.YONGSIN_SCROLL or pkItemScroll.GetValue(0) == enum_RefineScrolls.YAGONG_SCROLL:
        hyuniron_prob = [100, 75, 65, 55, 45, 40, 35, 25, 20]

        yagong_prob = [100, 100, 90, 80, 70, 60, 50, 30, 20]

        if pkItemScroll.GetValue(0) == enum_RefineScrolls.YONGSIN_SCROLL:
            success_prob = hyuniron_prob[MINMAX(0, item.GetRefineLevel(), 8)]
        elif pkItemScroll.GetValue(0) == enum_RefineScrolls.YAGONG_SCROLL:
            success_prob = yagong_prob[MINMAX(0, item.GetRefineLevel(), 8)]
        else:
            if (not pkItemScroll.GetValue(0)) == enum_RefineScrolls.HYUNIRON_CHN:
                #lani_err("REFINE : Unknown refine scroll item. Value0: %d", pkItemScroll.GetValue(0))

        if test_server:
            ChatPacket(EChatType.CHAT_TYPE_INFO, "[Only Test] Success_Prob %d, RefineLevel %d ", success_prob, item.GetRefineLevel())
        if pkItemScroll.GetValue(0) == enum_RefineScrolls.HYUNIRON_CHN:
            bDestroyWhenFail = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        if pkItemScroll.GetValue(0) == enum_RefineScrolls.HYUNIRON_CHN:
            szRefineType = "HYUNIRON"
        elif pkItemScroll.GetValue(0) == enum_RefineScrolls.YONGSIN_SCROLL:
            szRefineType = "GOD_SCROLL"
        elif pkItemScroll.GetValue(0) == enum_RefineScrolls.YAGONG_SCROLL:
            szRefineType = "YAGONG_SCROLL"

    if pkItemScroll.GetValue(0) == enum_RefineScrolls.MUSIN_SCROLL:
        success_prob = 100

        szRefineType = "MUSIN_SCROLL"

    elif pkItemScroll.GetValue(0) == enum_RefineScrolls.MEMO_SCROLL:
        success_prob = 100
        szRefineType = "MEMO_SCROLL"
    elif pkItemScroll.GetValue(0) == enum_RefineScrolls.BDRAGON_SCROLL:
        success_prob = 80
        szRefineType = "BDRAGON_SCROLL"

    pkItemScroll.SetCount(pkItemScroll.GetCount() - 1)

    if prob <= success_prob:
        pkNewItem = ITEM_MANAGER.instance().CreateItem(result_vnum, 1, 0, LGEMiscellaneous.DEFINECONSTANTS.false, -1, DefineConstants.false)

        if pkNewItem:
            olditem = item.GetID()
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to pointers to value types:
#ORIGINAL METINII C CODE: const char* itemname = item->GetName();
            itemname = item.GetName(LOCALE_LANIATUS)

            ITEM_MANAGER.CopyAllAttrTo(item, pkNewItem)
            wCell = item.GetCell()

            NotifyRefineSuccess(self, item, szRefineType)
            ITEM_MANAGER.instance().RemoveItem(item, "REMOVE (REFINE SUCCESS)")

            pkNewItem.AddToCharacter(self, TItemPos(EWindows.INVENTORY, wCell))
            ITEM_MANAGER.instance().FlushDelayedSave(pkNewItem)
            LogManager.instance().RefineLog(GetName(), itemname, olditem, pkNewItem.GetID(), "SUCESS")
            PayRefineFee(prt.cost)
        else:
            #lani_err("cannot create item %u", result_vnum)
            NotifyRefineFail(self, item, szRefineType, 0)
    elif (not bDestroyWhenFail) and result_fail_vnum != 0:
        pkNewItem = ITEM_MANAGER.instance().CreateItem(result_fail_vnum, 1, 0, LGEMiscellaneous.DEFINECONSTANTS.false, -1, DefineConstants.false)

        if pkNewItem:
            olditem = item.GetID()
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to pointers to value types:
#ORIGINAL METINII C CODE: const char* itemname = item->GetName();
            itemname = item.GetName(LOCALE_LANIATUS)

            ITEM_MANAGER.CopyAllAttrTo(item, pkNewItem)
            wCell = item.GetCell()
            NotifyRefineFail(self, item, szRefineType, -1)
            ITEM_MANAGER.instance().RemoveItem(item, "REMOVE (REFINE FAIL)")

            pkNewItem.AddToCharacter(self, TItemPos(EWindows.INVENTORY, wCell))
            ITEM_MANAGER.instance().FlushDelayedSave(pkNewItem)
            LogManager.instance().RefineLog(GetName(), itemname, olditem, pkNewItem.GetID(), "FAILED")
            PayRefineFee(prt.cost)
        else:
            #lani_err("cannot create item %u", result_fail_vnum)
            NotifyRefineFail(self, item, szRefineType, 0)
    else:
        NotifyRefineFail(self, item, szRefineType, 0)

        PayRefineFee(prt.cost)

    return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

def RefineInformation(wCell, bType, iAdditionalCell):
    if wCell > LGEMiscellaneous.INVENTORY_MAX_NUM:
        return LGEMiscellaneous.DEFINECONSTANTS.false

    item = GetInventoryItem(wCell)

    if item is None:
        return LGEMiscellaneous.DEFINECONSTANTS.false

    if bType == ERefineType.REFINE_TYPE_MONEY_ONLY and not GetQuestFlag("deviltower_zone.can_refine"):
        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You can only be rewarded once for the Demon Tower Quest."))
        return LGEMiscellaneous.DEFINECONSTANTS.false

    p = SPacketGCRefineInformaion()

    p.header = byte(LG_HEADER_GC_REFINE_INFORMATION)
    p.pos = byte(wCell)
    p.src_vnum = item.GetVnum()
    p.result_vnum = item.GetRefinedVnum()
    p.type = bType

    if p.result_vnum == 0:
        #lani_err("RefineInformation p.result_vnum == 0")
        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("This Item can't be made better."))
        return LGEMiscellaneous.DEFINECONSTANTS.false

    if item.GetType() == EItemTypes.ITEM_USE and item.GetSubType() == EUseSubTypes.USE_TUNING:
        if bType == 0:
            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("This Item can't be advanced this way."))
            return LGEMiscellaneous.DEFINECONSTANTS.false
        else:
            itemScroll = GetInventoryItem(iAdditionalCell)
            if itemScroll is None or item.GetVnum() == itemScroll.GetVnum():
                ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You can't combine identical Advancement Scrolls."))
                ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("The Blessing Scroll and Magic Metal can be combined"))
                return LGEMiscellaneous.DEFINECONSTANTS.false

    rm = CRefineManager.instance()

    prt = rm.GetRefineRecipe(item.GetRefineSet())

    if prt is None:
        #lani_err("RefineInformation NOT GET REFINE SET %d", item.GetRefineSet())
        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("This Item can't be made better."))
        return LGEMiscellaneous.DEFINECONSTANTS.false

    if GetQuestFlag("main_quest_lv7.refine_chance") > 0:
        if (not item.CheckItemUseLevel(20)) or item.GetType() != EItemTypes.ITEM_WEAPON:
            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Free advancement is only for weapons up to level 20."))
            return LGEMiscellaneous.DEFINECONSTANTS.false
        p.cost = 0
    else:
        p.cost = ComputeRefineFee(prt.cost)

    p.prob = prt.prob
    if bType == ERefineType.REFINE_TYPE_MONEY_ONLY:
        p.material_count = 0
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memset(p.materials, 0, sizeof(p.materials))
    else:
        p.material_count = prt.material_count
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memcpy' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memcpy(p.materials, prt.materials, sizeof(prt.materials))

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    GetDesc().Packet(p, sizeof(SPacketGCRefineInformaion))

    SetRefineMode(iAdditionalCell)
    return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

def RefineItem(pkItem, pkTarget):
    if not CanHandleItem():
        return LGEMiscellaneous.DEFINECONSTANTS.false

    if pkItem.GetSubType() == EUseSubTypes.USE_TUNING:
        if pkItem.GetValue(0) == enum_RefineScrolls.MUSIN_SCROLL:
            RefineInformation(pkTarget.GetCell(), ERefineType.REFINE_TYPE_MUSIN, pkItem.GetCell())
        elif pkItem.GetValue(0) == enum_RefineScrolls.HYUNIRON_CHN:
            RefineInformation(pkTarget.GetCell(), ERefineType.REFINE_TYPE_HYUNIRON, pkItem.GetCell())
        elif pkItem.GetValue(0) == enum_RefineScrolls.BDRAGON_SCROLL:
            if pkTarget.GetRefineSet() != 702:
                return LGEMiscellaneous.DEFINECONSTANTS.false
            RefineInformation(pkTarget.GetCell(), ERefineType.REFINE_TYPE_BDRAGON, pkItem.GetCell())
        else:
            if pkTarget.GetRefineSet() == 501:
                return LGEMiscellaneous.DEFINECONSTANTS.false
            RefineInformation(pkTarget.GetCell(), ERefineType.REFINE_TYPE_SCROLL, pkItem.GetCell())
    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'IS_SET' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
    elif pkItem.GetSubType() == EUseSubTypes.USE_DETACHMENT and IS_SET(pkTarget.GetFlag(), EItemFlag.ITEM_FLAG_REFINEABLE):
        bHasMetinStone = LGEMiscellaneous.DEFINECONSTANTS.false

        i = 0
        while i < EItemMisc.LG_ITEM_SOCKET_MAX_NUM:
            socket = pkTarget.GetSocket(i)
            if socket > 2 and socket != ITEM_BROKEN_METIN_VNUM:
                bHasMetinStone = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
                break
            i += 1

        if bHasMetinStone:
            i = 0
            while i < EItemMisc.LG_ITEM_SOCKET_MAX_NUM:
                socket = pkTarget.GetSocket(i)
                if socket > 2 and socket != ITEM_BROKEN_METIN_VNUM:
                    AutoGiveItem(socket)
                    pkTarget.SetSocket(i, ITEM_BROKEN_METIN_VNUM, ((not DefineConstants.false)))
                i += 1
            pkItem.SetCount(pkItem.GetCount() - 1)
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
        else:
            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("There is no Spirit Stone that can be removed."))
            return LGEMiscellaneous.DEFINECONSTANTS.false

    return LGEMiscellaneous.DEFINECONSTANTS.false

def GiveRecallItem(item):
    idx = GetMapIndex()
    iEmpireByMapIndex = -1

    if idx < 20:
        iEmpireByMapIndex = 1
    elif idx < 40:
        iEmpireByMapIndex = 2
    elif idx < 60:
        iEmpireByMapIndex = 3
    elif idx < 10000:
        iEmpireByMapIndex = 0

    if (idx == 66) or (idx == 216):
        iEmpireByMapIndex = -1

    if iEmpireByMapIndex != 0 and GetEmpire() != iEmpireByMapIndex:
        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You can't save this position."))
        return LGEMiscellaneous.DEFINECONSTANTS.false

    pos = None

    if item.GetCount() == 1:
        item.SetSocket(0, GetX(), ((not DefineConstants.false)))
        item.SetSocket(1, GetY(), ((not DefineConstants.false)))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: else if ((pos = GetEmptyInventory(item->GetSize())) != -1)
    elif (pos = GetEmptyInventory(item.GetSize())) != -1:
        item2 = ITEM_MANAGER.instance().CreateItem(item.GetVnum(), 1, 0, DefineConstants.false, -1, DefineConstants.false)

        if None is not item2:
            item2.SetSocket(0, GetX(), ((not DefineConstants.false)))
            item2.SetSocket(1, GetY(), ((not DefineConstants.false)))
            item2.AddToCharacter(self, TItemPos(EWindows.INVENTORY, pos))

            item.SetCount(item.GetCount() - 1)
    else:
        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("There isn't enough space in the inventory."))
        return LGEMiscellaneous.DEFINECONSTANTS.false

    return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

def ProcessRecallItem(item):
    idx = None

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((idx = SECTREE_MANAGER::instance().GetMapIndex(item->GetSocket(0), item->GetSocket(1))) == 0)
    if (idx = SECTREE_MANAGER.instance().GetMapIndex(item.GetSocket(0), item.GetSocket(1))) == 0:
        return

    iEmpireByMapIndex = -1

    if idx < 20:
        iEmpireByMapIndex = 1
    elif idx < 40:
        iEmpireByMapIndex = 2
    elif idx < 60:
        iEmpireByMapIndex = 3
    elif idx < 10000:
        iEmpireByMapIndex = 0

    if (idx == 66) or (idx == 216):
        iEmpireByMapIndex = -1
    elif (idx == 301) or (idx == 302) or (idx == 303) or (idx == 304):
        if GetLevel() < 90:
            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Your level is lower than the Level of the Item."))
            return
        else:
            break

    if iEmpireByMapIndex != 0 and GetEmpire() != iEmpireByMapIndex:
        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You can't teleport to a safe position in a foreign Kingdom."))
        item.SetSocket(0, 0, ((not DefineConstants.false)))
        item.SetSocket(1, 0, ((not DefineConstants.false)))
    else:
        #sys_log(1, "Recall: %s %d %d -> %d %d", GetName(), GetX(), GetY(), item.GetSocket(0), item.GetSocket(1))
        WarpSet(item.GetSocket(0), item.GetSocket(1))
        item.SetCount(item.GetCount() - 1)

def __OpenPrivateShop():
    bodyPart = GetPart(EParts.PART_MAIN)
    if (bodyPart == 0) or (bodyPart == 1) or (bodyPart == 2):
        ChatPacket(EChatType.CHAT_TYPE_COMMAND, "OpenPrivateShop")
    else:
        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("To open a shop, you have to take off the armor."))

def SendMyShopPriceListCmd(dwItemVnum, dwItemPrice):
    szLine = str(['\0' for _ in range(256)])
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    snprintf(szLine, sizeof(szLine), "MyShopPriceList %u %lld", dwItemVnum, dwItemPrice)
    ChatPacket(EChatType.CHAT_TYPE_COMMAND, szLine)
    #sys_log(0, szLine)

def UseSilkBotaryReal(p):
    pInfo = (p + 1)

    if p.wCount == 0:
        SendMyShopPriceListCmd(1, 0)
    else:
        idx = 0
        while idx < p.wCount:
            SendMyShopPriceListCmd(pInfo[idx].dwVnum, pInfo[idx].lldPrice)
            idx += 1

    __OpenPrivateShop()

def UseSilkBotary():
    if m_bNoOpenedShop:
        dwPlayerID = GetPlayerID()
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        db_clientdesc.DBPacket(LG_HEADER_GD_MYSHOP_PRICELIST_REQ, GetDesc().GetHandle(), dwPlayerID, sizeof(uint))
        m_bNoOpenedShop = LGEMiscellaneous.DEFINECONSTANTS.false
    else:
        __OpenPrivateShop()

class LuckyBagInfo:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.count = 0
        self.prob = 0
        self.vnum = 0

def UseItemEx(item, DestCell):
    iLimitRealtimeStartFirstUseFlagIndex = -1
    iLimitTimerBasedOnWearFlagIndex = -1

    wDestCell = DestCell.cell
    bDestInven = DestCell.window_type
    i = 0
    while i < EItemMisc.ITEM_LIMIT_MAX_NUM:
        limitValue = item.GetProto().aLimits[i].lValue

        if item.GetProto().aLimits[i].bType == ELimitTypes.LIMIT_LEVEL:
            if GetLevel() < limitValue:
                ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Your level is lower than the Level of the Item."))
                return LGEMiscellaneous.DEFINECONSTANTS.false

        elif item.GetProto().aLimits[i].bType == ELimitTypes.LIMIT_REAL_TIME_START_FIRST_USE:
            iLimitRealtimeStartFirstUseFlagIndex = i

        elif item.GetProto().aLimits[i].bType == ELimitTypes.LIMIT_TIMER_BASED_ON_WEAR:
            iLimitTimerBasedOnWearFlagIndex = i
        i += 1

    if test_server:
        #sys_log(0, "USE_ITEM %s, Inven %d, Cell %d, ItemType %d, SubType %d", item.GetName(LOCALE_LANIATUS), bDestInven, wDestCell, item.GetType(), item.GetSubType())

    if -1 != iLimitRealtimeStartFirstUseFlagIndex:
        if 0 == item.GetSocket(1):
            duration = item.GetSocket(0) if (0 != item.GetSocket(0)) else item.GetProto().aLimits[iLimitRealtimeStartFirstUseFlagIndex].lValue

            if 0 == duration:
                duration = 60 * 60 * 24 * 7

            item.SetSocket(0, time(0) + duration, ((not DefineConstants.false)))
            item.StartRealTimeExpireEvent()

        if LGEMiscellaneous.DEFINECONSTANTS.false == item.IsEquipped():
            item.SetSocket(1, item.GetSocket(1) + 1, ((not DefineConstants.false)))

    if item.GetType() == EItemTypes.ITEM_HAIR:
        return ItemProcess_Hair(item, wDestCell)

    if (item.GetType() == EItemTypes.ITEM_HAIR) or (item.GetType() == EItemTypes.ITEM_POLYMORPH):
        return ItemProcess_Polymorph(item)

    if (item.GetType() == EItemTypes.ITEM_HAIR) or (item.GetType() == EItemTypes.ITEM_POLYMORPH) or (item.GetType() == EItemTypes.ITEM_QUEST):
        if IsObserverMode() == ((not LGEMiscellaneous.DEFINECONSTANTS.false)):
            if item.GetVnum() == 50051 or item.GetVnum() == 50052 or item.GetVnum() == 50053:
                ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You can't use this Item in a duel."))
                return LGEMiscellaneous.DEFINECONSTANTS.false

        ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'IS_SET' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
        if not IS_SET(item.GetFlag(), EItemFlag.ITEM_FLAG_QUEST_USE | EItemFlag.ITEM_FLAG_QUEST_USE_MULTIPLE):
            if item.GetSIGVnum() == 0:
                quest.CQuestManager.instance().UseItem(GetPlayerID(), item, LGEMiscellaneous.DEFINECONSTANTS.false)
            else:
                quest.CQuestManager.instance().SIGUse(GetPlayerID(), item.GetSIGVnum(), item, LGEMiscellaneous.DEFINECONSTANTS.false)

    elif item.GetType() == EItemTypes.ITEM_CAMPFIRE:
            fx = None
            fy = None
            GetDeltaByDegree(GetRotation(), 100.0, fx, fy)

            tree = SECTREE_MANAGER.instance().Get(GetMapIndex(), uint(int((GetX()+fx))), uint(int((GetY()+fy))))

            if tree is None:
                ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You can't make a campfire here."))
                return LGEMiscellaneous.DEFINECONSTANTS.false

            if tree.IsAttr(int((GetX()+fx)), int((GetY()+fy)), uint(ATTR_WATER)):
                ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You can't make a campfire under water."))
                return LGEMiscellaneous.DEFINECONSTANTS.false

            campfire = CHARACTER_MANAGER.instance().SpawnMob(uint(fishing.CAMPFIRE_MOB), GetMapIndex(), int((GetX()+fx)), int((GetY()+fy)), 0, LGEMiscellaneous.DEFINECONSTANTS.false, number(0, 359), ((not DefineConstants.false)))

            info = AllocEventInfo()

            info.ch = campfire

## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: campfire->m_pkMiningEvent = event_create_ex(kill_campfire_event, info, ((40) * passes_per_sec));
            campfire.m_pkMiningEvent.copy_from(event_create_ex(kill_campfire_event, info, ((40) * passes_per_sec)))

            item.SetCount(item.GetCount() - 1)

    elif item.GetType() == EItemTypes.ITEM_UNIQUE:
            if item.GetSubType() == EUseSubTypes.USE_ABILITY_UP:
                    if item.GetValue(0) == EApplyTypes.APPLY_MOV_SPEED:
                        AddAffect(LaniatusEAffectTypes.LANIA_AFFECT_UNIQUE_ABILITY, EPointTypes.LG_POINT_MOV_SPEED, item.GetValue(2), EAffectBits.AFF_MOV_SPEED_POTION, item.GetValue(1), 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
                        EffectPacket(SPECIAL_EFFECT.SE_DXUP_PURPLE)

                    elif item.GetValue(0) == EApplyTypes.APPLY_ATT_SPEED:
                        AddAffect(LaniatusEAffectTypes.LANIA_AFFECT_UNIQUE_ABILITY, EPointTypes.LG_POINT_ATT_SPEED, item.GetValue(2), EAffectBits.AFF_ATT_SPEED_POTION, item.GetValue(1), 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
                        EffectPacket(SPECIAL_EFFECT.SE_SPEEDUP_GREEN)

                    elif item.GetValue(0) == EApplyTypes.APPLY_STR:
                        AddAffect(LaniatusEAffectTypes.LANIA_AFFECT_UNIQUE_ABILITY, EPointTypes.LG_POINT_ST, item.GetValue(2), 0, item.GetValue(1), 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), ((not LGEMiscellaneous.DEFINECONSTANTS.false)))

                    elif item.GetValue(0) == EApplyTypes.APPLY_DEX:
                        AddAffect(LaniatusEAffectTypes.LANIA_AFFECT_UNIQUE_ABILITY, EPointTypes.LG_POINT_DX, item.GetValue(2), 0, item.GetValue(1), 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), ((not LGEMiscellaneous.DEFINECONSTANTS.false)))

                    elif item.GetValue(0) == EApplyTypes.APPLY_CON:
                        AddAffect(LaniatusEAffectTypes.LANIA_AFFECT_UNIQUE_ABILITY, EPointTypes.LG_POINT_HT, item.GetValue(2), 0, item.GetValue(1), 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), ((not LGEMiscellaneous.DEFINECONSTANTS.false)))

                    elif item.GetValue(0) == EApplyTypes.APPLY_INT:
                        AddAffect(LaniatusEAffectTypes.LANIA_AFFECT_UNIQUE_ABILITY, EPointTypes.LG_POINT_IQ, item.GetValue(2), 0, item.GetValue(1), 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), ((not LGEMiscellaneous.DEFINECONSTANTS.false)))

                    elif item.GetValue(0) == EApplyTypes.APPLY_CAST_SPEED:
                        AddAffect(LaniatusEAffectTypes.LANIA_AFFECT_UNIQUE_ABILITY, EPointTypes.LG_POINT_CASTING_SPEED, item.GetValue(2), 0, item.GetValue(1), 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), ((not LGEMiscellaneous.DEFINECONSTANTS.false)))

                    elif item.GetValue(0) == EApplyTypes.APPLY_RESIST_MAGIC:
                        AddAffect(LaniatusEAffectTypes.LANIA_AFFECT_UNIQUE_ABILITY, EPointTypes.LG_POINT_RESIST_MAGIC, item.GetValue(2), 0, item.GetValue(1), 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), ((not LGEMiscellaneous.DEFINECONSTANTS.false)))

                    elif item.GetValue(0) == EApplyTypes.APPLY_ATT_GRADE_BONUS:
                        AddAffect(LaniatusEAffectTypes.LANIA_AFFECT_UNIQUE_ABILITY, EPointTypes.LG_POINT_ATT_GRADE_BONUS, item.GetValue(2), 0, item.GetValue(1), 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), ((not LGEMiscellaneous.DEFINECONSTANTS.false)))

                    elif item.GetValue(0) == EApplyTypes.APPLY_DEF_GRADE_BONUS:
                        AddAffect(LaniatusEAffectTypes.LANIA_AFFECT_UNIQUE_ABILITY, EPointTypes.LG_POINT_DEF_GRADE_BONUS, item.GetValue(2), 0, item.GetValue(1), 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), ((not LGEMiscellaneous.DEFINECONSTANTS.false)))

                if GetDungeon():
                    GetDungeon().UsePotion(self)

                if GetWarMap():
                    GetWarMap().UsePotion(self, item)

                item.SetCount(item.GetCount() - 1)


            if True:
                    if item.GetSubType() == EUseSubTypes.USE_SPECIAL:
                        #sys_log(0, "ITEM_UNIQUE: USE_SPECIAL %u", item.GetVnum())

                        if item.GetVnum() == 71049:
                                UseSilkBotary()
                    else:
                        if not item.IsEquipped():
                            EquipItem(item)
                        else:
                            UnequipItem(item)

    elif (item.GetType() == EItemTypes.ITEM_UNIQUE) or (item.GetType() == EItemTypes.ITEM_COSTUME) or (item.GetType() == EItemTypes.ITEM_WEAPON) or (item.GetType() == EItemTypes.ITEM_ARMOR) or (item.GetType() == EItemTypes.ITEM_ROD) or (item.GetType() == EItemTypes.ITEM_RING) or (item.GetType() == EItemTypes.ITEM_BELT) or (item.GetType() == EItemTypes.ITEM_PICK):
        if not item.IsEquipped():
            EquipItem(item)
        else:
            UnequipItem(item)

    elif item.GetType() == EItemTypes.ITEM_DS:
            if not item.IsEquipped():
                return LGEMiscellaneous.DEFINECONSTANTS.false
            temp_ref_item = RefObject(item);
            tempVar = DSManager.instance().PullOut(self, NPOS, temp_ref_item, NULL)
            item = temp_ref_item.arg_value
            return tempVar
            break
    elif item.GetType() == EItemTypes.ITEM_SPECIAL_DS:
        if not item.IsEquipped():
            EquipItem(item)
        else:
            UnequipItem(item)

    elif item.GetType() == EItemTypes.ITEM_FISH:
            if item.GetSubType() == EFishSubTypes.FISH_ALIVE:
                fishing.UseFish(self, item)

    elif item.GetType() == EItemTypes.ITEM_TREASURE_BOX:
            return LGEMiscellaneous.DEFINECONSTANTS.false

    elif item.GetType() == EItemTypes.ITEM_TREASURE_KEY:
            item2 = None

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if (!GetItem(DestCell) || !(item2 = GetItem(DestCell)))
            if (not GetItem(DestCell)) or not(item2 = GetItem(DestCell)):
                return LGEMiscellaneous.DEFINECONSTANTS.false

            if item2.IsExchanging():
                return LGEMiscellaneous.DEFINECONSTANTS.false

            if item2.GetType() != EItemTypes.ITEM_TREASURE_BOX:
                ChatPacket(EChatType.CHAT_TYPE_TALKING, LC_TEXT("This Item can't be opened with a Key."))
                return LGEMiscellaneous.DEFINECONSTANTS.false

            if item.GetValue(0) == item2.GetValue(0):
                dwBoxVnum = item2.GetVnum()
                dwVnums = []
                dwCounts = []
                item_gets = [None for _ in range(0)]
                count = 0

                if GiveItemFromSpecialItemGroup(dwBoxVnum, dwVnums, dwCounts, item_gets, count):
                    ITEM_MANAGER.instance().RemoveItem(item, NULL)
                    ITEM_MANAGER.instance().RemoveItem(item2, NULL)

                    for i in range(0, count):
                        if dwVnums[i] == CSpecialItemGroup.EGiveType.GOLD:
                            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You received %d Yang."), dwCounts[i])
                        elif dwVnums[i] == CSpecialItemGroup.EGiveType.EXP:
                            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Mysterious light comes out of this box."))
                            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You received %d Experience Points."), dwCounts[i])
                        elif dwVnums[i] == CSpecialItemGroup.EGiveType.MOB:
                            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("A monster came out of the box!"))
                        elif dwVnums[i] == CSpecialItemGroup.EGiveType.SLOW:
                            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("If you inhale the red smoke coming out of the box, you will move faster!"))
                        elif dwVnums[i] == CSpecialItemGroup.EGiveType.DRAIN_HP:
                            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("The box exploded suddenly! Your HP are lower."))
                        elif dwVnums[i] == CSpecialItemGroup.EGiveType.POISON:
                            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("If you inhale the green smoke coming from the box, poison will spread in your body!"))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if ENABLE_WOLFMAN
                        elif dwVnums[i] == CSpecialItemGroup.EGiveType.BLEEDING:
                            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("If you inhale the green smoke coming from the box, poison will spread in your body!"))
##endif
                        elif dwVnums[i] == CSpecialItemGroup.EGiveType.MOB_GROUP:
                            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("A monster came out of the box!"))
                        else:
                            if item_gets[i]:
                                if dwCounts[i] > 1:
                                    ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("There are %s of %d in the box."), item_gets[i].GetName(LOCALE_LANIATUS), dwCounts[i])
                                else:
                                    ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("There is %s in the box."), item_gets[i].GetName(LOCALE_LANIATUS))

                else:
                    ChatPacket(EChatType.CHAT_TYPE_TALKING, LC_TEXT("This Key seems not to fit into the lock."))
                    return LGEMiscellaneous.DEFINECONSTANTS.false
            else:
                ChatPacket(EChatType.CHAT_TYPE_TALKING, LC_TEXT("This Key seems not to fit into the lock."))
                return LGEMiscellaneous.DEFINECONSTANTS.false

    elif (item.GetType() == EItemTypes.ITEM_TREASURE_KEY) or (item.GetType() == EItemTypes.ITEM_GIFTBOX):
            dwBoxVnum = item.GetVnum()
            dwVnums = []
            dwCounts = []
            item_gets = [None for _ in range(0)]
            count = 0

            if (dwBoxVnum > 51500 and dwBoxVnum < 52000) or (dwBoxVnum >= 50255 and dwBoxVnum <= 50260):
                if not(self.DragonSoul_IsQualified()):
                    ChatPacket(EChatType.CHAT_TYPE_INFO,LC_TEXT("Before you open the Cor Draconis, you have to complete the Dragon Stone quest and activate the Dragon Stone Alchemy."))
                    return LGEMiscellaneous.DEFINECONSTANTS.false

            if GiveItemFromSpecialItemGroup(dwBoxVnum, dwVnums, dwCounts, item_gets, count):
                item.SetCount(item.GetCount()-1)

                for i in range(0, count):
                    if dwVnums[i] == CSpecialItemGroup.EGiveType.GOLD:
                        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You received %d Yang."), dwCounts[i])
                    elif dwVnums[i] == CSpecialItemGroup.EGiveType.EXP:
                        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Mysterious light comes out of this box."))
                        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You received %d Experience Points."), dwCounts[i])
                    elif dwVnums[i] == CSpecialItemGroup.EGiveType.MOB:
                        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("A monster came out of the box!"))
                    elif dwVnums[i] == CSpecialItemGroup.EGiveType.SLOW:
                        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("If you inhale the red smoke coming out of the box, you will move faster!"))
                    elif dwVnums[i] == CSpecialItemGroup.EGiveType.DRAIN_HP:
                        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("The box exploded suddenly! Your HP are lower."))
                    elif dwVnums[i] == CSpecialItemGroup.EGiveType.POISON:
                        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("If you inhale the green smoke coming from the box, poison will spread in your body!"))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if ENABLE_WOLFMAN
                    elif dwVnums[i] == CSpecialItemGroup.EGiveType.BLEEDING:
                        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("If you inhale the green smoke coming from the box, poison will spread in your body!"))
##endif
                    elif dwVnums[i] == CSpecialItemGroup.EGiveType.MOB_GROUP:
                        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("A monster came out of the box!"))
                    else:
                        if item_gets[i]:
                            if dwCounts[i] > 1:
                                ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("There are %s of %d in the box."), item_gets[i].GetName(LOCALE_LANIATUS), dwCounts[i])
                            else:
                                ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("There is %s in the box."), item_gets[i].GetName(LOCALE_LANIATUS))
            else:
                ChatPacket(EChatType.CHAT_TYPE_TALKING, LC_TEXT("You received nothing."))
                return LGEMiscellaneous.DEFINECONSTANTS.false

    elif (item.GetType() == EItemTypes.ITEM_TREASURE_KEY) or (item.GetType() == EItemTypes.ITEM_GIFTBOX) or (item.GetType() == EItemTypes.ITEM_SKILLFORGET):
            if item.GetSocket(0) == 0:
                ITEM_MANAGER.instance().RemoveItem(item, NULL)
                return LGEMiscellaneous.DEFINECONSTANTS.false

            dwVnum = uint(item.GetSocket(0))

            if SkillLevelDown(dwVnum):
                ITEM_MANAGER.instance().RemoveItem(item, NULL)
                ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You lowered your Skill Level."))
            else:
                ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You can't lower your Skill Level."))

    elif item.GetType() == EItemTypes.ITEM_SKILLBOOK:
            if IsPolymorphed():
                ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You cannot read books while transformed."))
                return LGEMiscellaneous.DEFINECONSTANTS.false

            dwVnum = 0

            if item.GetVnum() == 50300:
                dwVnum = uint(item.GetSocket(0))
            else:
                dwVnum = uint(item.GetValue(0))

            if 0 == dwVnum:
                ITEM_MANAGER.instance().RemoveItem(item, NULL)

                return LGEMiscellaneous.DEFINECONSTANTS.false

            if ((not LGEMiscellaneous.DEFINECONSTANTS.false)) == LearnSkillByBook(dwVnum):
                item.SetCount(item.GetCount()-1)

                iReadDelay = number(LGEMiscellaneous.SKILLBOOK_DELAY_MIN, LGEMiscellaneous.SKILLBOOK_DELAY_MAX)

                SetSkillNextReadTime(dwVnum, get_global_time() + iReadDelay)

    elif item.GetType() == EItemTypes.ITEM_USE:
            if item.GetVnum() > 50800 and item.GetVnum() <= 50820:
                if test_server:
                    #sys_log(0, "ADD addtional effect : vnum(%d) subtype(%d)", item.GetOriginalVnum(), item.GetSubType())

                affect_type = LaniatusEAffectTypes.LANIA_AFFECT_EXP_BONUS_EURO_FREE
                apply_type = aApplyInfo[item.GetValue(0)].bPointType
                apply_value = item.GetValue(2)
                apply_duration = item.GetValue(1)

                if item.GetSubType() == EUseSubTypes.USE_ABILITY_UP:
                    if FindAffect(affect_type, apply_type):
                        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("The effect is already working."))
                        return LGEMiscellaneous.DEFINECONSTANTS.false

                        if item.GetValue(0) == EApplyTypes.APPLY_MOV_SPEED:
                            AddAffect(affect_type, apply_type, apply_value, EAffectBits.AFF_MOV_SPEED_POTION, apply_duration, 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), ((not LGEMiscellaneous.DEFINECONSTANTS.false)))

                        elif item.GetValue(0) == EApplyTypes.APPLY_ATT_SPEED:
                            AddAffect(affect_type, apply_type, apply_value, EAffectBits.AFF_ATT_SPEED_POTION, apply_duration, 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), ((not LGEMiscellaneous.DEFINECONSTANTS.false)))

                        elif (item.GetValue(0) == EApplyTypes.APPLY_STR) or (item.GetValue(0) == EApplyTypes.APPLY_DEX) or (item.GetValue(0) == EApplyTypes.APPLY_CON) or (item.GetValue(0) == EApplyTypes.APPLY_INT) or (item.GetValue(0) == EApplyTypes.APPLY_CAST_SPEED) or (item.GetValue(0) == EApplyTypes.APPLY_RESIST_MAGIC) or (item.GetValue(0) == EApplyTypes.APPLY_ATT_GRADE_BONUS) or (item.GetValue(0) == EApplyTypes.APPLY_DEF_GRADE_BONUS):
                            AddAffect(affect_type, apply_type, apply_value, 0, apply_duration, 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), ((not LGEMiscellaneous.DEFINECONSTANTS.false)))

                    if GetDungeon():
                        GetDungeon().UsePotion(self)

                    if GetWarMap():
                        GetWarMap().UsePotion(self, item)

                    item.SetCount(item.GetCount() - 1)

                if (item.GetSubType() == EUseSubTypes.USE_ABILITY_UP) or (item.GetSubType() == EUseSubTypes.USE_AFFECT):
                        if not IsLoadedAffect():
                            return LGEMiscellaneous.DEFINECONSTANTS.false

                        if FindAffect(LaniatusEAffectTypes.LANIA_AFFECT_EXP_BONUS_EURO_FREE, aApplyInfo[item.GetValue(1)].bPointType):
                            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("The effect is already working."))
                        else:

                            AddAffect(LaniatusEAffectTypes.LANIA_AFFECT_EXP_BONUS_EURO_FREE, aApplyInfo[item.GetValue(1)].bPointType, item.GetValue(2), 0, item.GetValue(3), 0, LGEMiscellaneous.DEFINECONSTANTS.false, ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
                            item.SetCount(item.GetCount() - 1)

                elif item.GetSubType() == EUseSubTypes.USE_POTION_NODELAY:
                        used = LGEMiscellaneous.DEFINECONSTANTS.false

                        if item.GetValue(0) != 0:
                            if GetHP() < GetMaxHP():
                                PointChange(EPointTypes.LG_POINT_HP, math.trunc(item.GetValue(0) * (100 + GetPoint(EPointTypes.LG_POINT_POTION_BONUS)) / float(100)))
                                EffectPacket(SPECIAL_EFFECT.SE_HPUP_RED)
                                used = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

                        if item.GetValue(1) != 0:
                            if GetSP() < GetMaxSP():
                                PointChange(EPointTypes.LG_POINT_SP, math.trunc(item.GetValue(1) * (100 + GetPoint(EPointTypes.LG_POINT_POTION_BONUS)) / float(100)))
                                EffectPacket(SPECIAL_EFFECT.SE_SPUP_BLUE)
                                used = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

                        if item.GetValue(3) != 0:
                            if GetHP() < GetMaxHP():
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
                                PointChange(EPointTypes.LG_POINT_HP, item.GetValue(3) * GetMaxHP() / 100)
                                EffectPacket(SPECIAL_EFFECT.SE_HPUP_RED)
                                used = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

                        if item.GetValue(4) != 0:
                            if GetSP() < GetMaxSP():
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
                                PointChange(EPointTypes.LG_POINT_SP, item.GetValue(4) * GetMaxSP() / 100)
                                EffectPacket(SPECIAL_EFFECT.SE_SPUP_BLUE)
                                used = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

                        if used:
                            if GetDungeon():
                                GetDungeon().UsePotion(self)

                            if GetWarMap():
                                GetWarMap().UsePotion(self, item)

                            item.SetCount(item.GetCount() - 1)

                return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

            if test_server:
                #sys_log(0, "USE_ITEM %s Type %d SubType %d vnum %d", item.GetName(LOCALE_LANIATUS), item.GetType(), item.GetSubType(), item.GetOriginalVnum())

            if item.GetSubType() == EUseSubTypes.USE_TIME_CHARGE_PER:
                    pDestItem = GetItem(DestCell)
                    if None is pDestItem:
                        return LGEMiscellaneous.DEFINECONSTANTS.false

                    if pDestItem.IsDragonSoul():
                        ret = None

                        if item.GetVnum() == DRAGON_HEART_VNUM:
                            ret = pDestItem.GiveMoreTime_Per(float(item.GetSocket(EItemDragonSoulSockets.LG_ITEM_SOCKET_CHARGING_AMOUNT_IDX)))
                        else:
                            ret = pDestItem.GiveMoreTime_Per(float(item.GetValue(EItemValueIdice.ITEM_VALUE_CHARGING_AMOUNT_IDX)))
                        if ret > 0:
                            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("%d seconds have been added."), ret)
                            item.SetCount(item.GetCount() - 1)
                            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
                        else:
                            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You cannot recharge this Dragon Stone."))
                            return LGEMiscellaneous.DEFINECONSTANTS.false
                    else:
                        return LGEMiscellaneous.DEFINECONSTANTS.false
            elif item.GetSubType() == EUseSubTypes.USE_TIME_CHARGE_FIX:
                    pDestItem = GetItem(DestCell)
                    if None is pDestItem:
                        return LGEMiscellaneous.DEFINECONSTANTS.false

                    if pDestItem.IsDragonSoul():
                        ret = pDestItem.GiveMoreTime_Fix(uint(item.GetValue(EItemValueIdice.ITEM_VALUE_CHARGING_AMOUNT_IDX)))

                        if ret != 0:
                            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("%d seconds have been added."), ret)
                            item.SetCount(item.GetCount() - 1)
                            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
                        else:
                            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You cannot recharge this Dragon Stone."))
                            return LGEMiscellaneous.DEFINECONSTANTS.false
                    else:
                        return LGEMiscellaneous.DEFINECONSTANTS.false
            elif item.GetSubType() == EUseSubTypes.USE_SPECIAL:

                if item.GetVnum() == ITEM_NOG_POCKET:
                        if FindAffect(LaniatusEAffectTypes.LANIA_AFFECT_NOG_ABILITY):
                            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("The effect is already working."))
                            return LGEMiscellaneous.DEFINECONSTANTS.false
                        time = item.GetValue(0)
                        moveSpeedPer = item.GetValue(1)
                        attPer = item.GetValue(2)
                        expPer = item.GetValue(3)
                        AddAffect(LaniatusEAffectTypes.LANIA_AFFECT_NOG_ABILITY, EPointTypes.LG_POINT_MOV_SPEED, moveSpeedPer, EAffectBits.AFF_MOV_SPEED_POTION, time, 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
                        EffectPacket(SPECIAL_EFFECT.SE_DXUP_PURPLE)
                        AddAffect(LaniatusEAffectTypes.LANIA_AFFECT_NOG_ABILITY, EPointTypes.LG_POINT_MALL_ATTBONUS, attPer, EAffectBits.AFF_NONE, time, 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
                        AddAffect(LaniatusEAffectTypes.LANIA_AFFECT_NOG_ABILITY, EPointTypes.LG_POINT_MALL_EXPBONUS, expPer, EAffectBits.AFF_NONE, time, 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
                        item.SetCount(item.GetCount() - 1)

                elif item.GetVnum() == ITEM_RAMADAN_CANDY:
                        time = item.GetValue(0)
                        moveSpeedPer = item.GetValue(1)
                        attPer = item.GetValue(2)
                        expPer = item.GetValue(3)
                        AddAffect(LaniatusEAffectTypes.LANIA_AFFECT_RAMADAN_ABILITY, EPointTypes.LG_POINT_MOV_SPEED, moveSpeedPer, EAffectBits.AFF_MOV_SPEED_POTION, time, 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
                        AddAffect(LaniatusEAffectTypes.LANIA_AFFECT_RAMADAN_ABILITY, EPointTypes.LG_POINT_MALL_ATTBONUS, attPer, EAffectBits.AFF_NONE, time, 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
                        AddAffect(LaniatusEAffectTypes.LANIA_AFFECT_RAMADAN_ABILITY, EPointTypes.LG_POINT_MALL_EXPBONUS, expPer, EAffectBits.AFF_NONE, time, 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
                        item.SetCount(item.GetCount() - 1)

                elif item.GetVnum() == ITEM_MARRIAGE_RING:
                        pMarriage = marriage.CManager.instance().Get(GetPlayerID())
                        if pMarriage:
                            consumeSP = CalculateConsumeSP(self)

                            if consumeSP < 0:
                                return LGEMiscellaneous.DEFINECONSTANTS.false

                            PointChange(EPointTypes.LG_POINT_SP, -consumeSP, LGEMiscellaneous.DEFINECONSTANTS.false)

                            WarpToPID(pMarriage.GetOther(GetPlayerID()))
                        else:
                            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You can't wear a Wedding Ring if you aren't married."))

                elif (item.GetVnum() == UNIQUE_ITEM_CAPE_OF_COURAGE) or (item.GetVnum() == 70057) or (item.GetVnum() == REWARD_BOX_UNIQUE_ITEM_CAPE_OF_COURAGE):
                    AggregateMonster()
                    item.SetCount(item.GetCount()-1)

                elif item.GetVnum() == UNIQUE_ITEM_WHITE_FLAG:
                    ForgetMyAttacker()
                    item.SetCount(item.GetCount()-1)

                elif item.GetVnum() == UNIQUE_ITEM_TREASURE_BOX:
                    pass

                elif (item.GetVnum() == 30093) or (item.GetVnum() == 30094) or (item.GetVnum() == 30095) or (item.GetVnum() == 30096):
                        MAX_BAG_INFO = 26
                        b1 = [LuckyBagInfo(1000, 302, 1), LuckyBagInfo(10, 150, 27002), LuckyBagInfo(10, 75, 27003), LuckyBagInfo(10, 100, 27005), LuckyBagInfo(10, 50, 27006), LuckyBagInfo(10, 80, 27001), LuckyBagInfo(10, 50, 27002), LuckyBagInfo(10, 80, 27004), LuckyBagInfo(10, 50, 27005), LuckyBagInfo(1, 10, 50300), LuckyBagInfo(1, 6, 92), LuckyBagInfo(1, 2, 132), LuckyBagInfo(1, 6, 1052), LuckyBagInfo(1, 2, 1092), LuckyBagInfo(1, 6, 2082), LuckyBagInfo(1, 2, 2122), LuckyBagInfo(1, 6, 3082), LuckyBagInfo(1, 2, 3122), LuckyBagInfo(1, 6, 5052), LuckyBagInfo(1, 2, 5082), LuckyBagInfo(1, 6, 7082), LuckyBagInfo(1, 2, 7122), LuckyBagInfo(1, 1, 11282), LuckyBagInfo(1, 1, 11482), LuckyBagInfo(1, 1, 11682), LuckyBagInfo(1, 1, 11882)]

                        b2 = [LuckyBagInfo(1000, 302, 1), LuckyBagInfo(10, 150, 27002), LuckyBagInfo(10, 75, 27002), LuckyBagInfo(10, 100, 27005), LuckyBagInfo(10, 50, 27005), LuckyBagInfo(10, 80, 27001), LuckyBagInfo(10, 50, 27002), LuckyBagInfo(10, 80, 27004), LuckyBagInfo(10, 50, 27005), LuckyBagInfo(1, 10, 50300), LuckyBagInfo(1, 6, 92), LuckyBagInfo(1, 2, 132), LuckyBagInfo(1, 6, 1052), LuckyBagInfo(1, 2, 1092), LuckyBagInfo(1, 6, 2082), LuckyBagInfo(1, 2, 2122), LuckyBagInfo(1, 6, 3082), LuckyBagInfo(1, 2, 3122), LuckyBagInfo(1, 6, 5052), LuckyBagInfo(1, 2, 5082), LuckyBagInfo(1, 6, 7082), LuckyBagInfo(1, 2, 7122), LuckyBagInfo(1, 1, 11282), LuckyBagInfo(1, 1, 11482), LuckyBagInfo(1, 1, 11682), LuckyBagInfo(1, 1, 11882)]

                        bi = None
                        bi = b1

                        pct = number(1, 1000)

                        i = None
                        for i in range(0, MAX_BAG_INFO):
                            if pct <= bi[i].prob:
                                break
                            pct -= bi[i].prob
                        if i>=MAX_BAG_INFO:
                            return LGEMiscellaneous.DEFINECONSTANTS.false

                        if bi[i].vnum == 50300:
                            GiveRandomSkillBook()
                        elif bi[i].vnum == 1:
                            PointChange(EPointTypes.LG_POINT_GOLD, 1000, ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
                        else:
                            AutoGiveItem(bi[i].vnum, bi[i].count)
                        ITEM_MANAGER.instance().RemoveItem(item, NULL)

                elif (item.GetVnum() == 27989) or (item.GetVnum() == 76006):
                        pMap = SECTREE_MANAGER.instance().GetMap(GetMapIndex())

                        if pMap is not None:
                            item.SetSocket(0, item.GetSocket(0) + 1, ((not DefineConstants.false)))

                            f = FFindStone()
                            pMap.for_each(f.functor_method)

                            if len(f.m_mapStone) > 0:
                                stone = f.m_mapStone.begin()

                                max = numeric_limits.max()
                                pTarget = stone.second

                                while stone is not f.m_mapStone.end():
                                    dist = uint(DISTANCE_SQRT(GetX()-stone.second.GetX(), GetY()-stone.second.GetY()))

                                    if dist != 0 and max > dist:
                                        max = dist
                                        pTarget = stone.second
                                    stone += 1

                                if pTarget is not None:
                                    val = 3

                                    if max < 10000:
                                        val = 2
                                    elif max < 70000:
                                        val = 1

                                    ChatPacket(EChatType.CHAT_TYPE_COMMAND, "StoneDetect %u %d %d", GetVID(), val, int(GetDegreeFromPositionXY(GetX(), pTarget.GetY(), pTarget.GetX(), GetY())))
                                else:
                                    ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("There is currently no Metin Stone on this map."))
                            else:
                                ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("There is currently no Metin Stone on this map."))

                            if item.GetSocket(0) >= 6:
                                ChatPacket(EChatType.CHAT_TYPE_COMMAND, "StoneDetect %u 0 0", GetVID())
                                ITEM_MANAGER.instance().RemoveItem(item, NULL)
                        break

                elif item.GetVnum() == 27996:
                    item.SetCount(item.GetCount() - 1)

                elif item.GetVnum() == 27987:
                        item.SetCount(item.GetCount() - 1)

                        r = number(1, 100)

                        if r <= 50:
                            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("There is a Stone inside the Clam."))
                            AutoGiveItem(27990)
                        else:
                            prob_table = [70, 83, 91]

                            if r <= prob_table[0]:
                                ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("The Clam completely vanished."))
                            elif r <= prob_table[1]:
                                ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("There is a White pearl inside the Clam."))
                                AutoGiveItem(27992)
                            elif r <= prob_table[2]:
                                ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("There is a Blue Pearl inside the Clam."))
                                AutoGiveItem(27993)
                            else:
                                ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("There is a Red Pearl inside the Clam."))
                                AutoGiveItem(27994)

                elif item.GetVnum() == 71013:
                    CreateFly(number(FLY_FIREWORK1, FLY_FIREWORK6), self)
                    item.SetCount(item.GetCount() - 1)

                elif (item.GetVnum() == 50100) or (item.GetVnum() == 50101) or (item.GetVnum() == 50102) or (item.GetVnum() == 50103) or (item.GetVnum() == 50104) or (item.GetVnum() == 50105) or (item.GetVnum() == 50106):
                    CreateFly(item.GetVnum() - 50100 + FLY_FIREWORK1, self)
                    item.SetCount(item.GetCount() - 1)

                elif item.GetVnum() == 50200:
                        __OpenPrivateShop()

                elif item.GetVnum() == fishing.FISH_MIND_PILL_VNUM:
                    AddAffect(LaniatusEAffectTypes.LANIA_AFFECT_FISH_MIND_PILL, EPointTypes.LG_POINT_NONE, 0, EAffectBits.AFF_FISH_MIND, 20 *60, 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
                    item.SetCount(item.GetCount() - 1)

                elif (item.GetVnum() == 50301) or (item.GetVnum() == 50302) or (item.GetVnum() == 50303):
                        if IsPolymorphed() == ((not LGEMiscellaneous.DEFINECONSTANTS.false)):
                            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You cannot change your state as long as you are transformed."))
                            return LGEMiscellaneous.DEFINECONSTANTS.false

                        lv = GetSkillLevel(LaniatusETalentXes.LG_SKILL_LEADERSHIP)

                        if lv < item.GetValue(0):
                            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("It isn't easy to understand this Book."))
                            return LGEMiscellaneous.DEFINECONSTANTS.false

                        if lv >= item.GetValue(1):
                            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("This Book won't help you."))
                            return LGEMiscellaneous.DEFINECONSTANTS.false

                        if LearnSkillByBook(LaniatusETalentXes.LG_SKILL_LEADERSHIP):
                            ITEM_MANAGER.instance().RemoveItem(item, NULL)

                            iReadDelay = number(LGEMiscellaneous.SKILLBOOK_DELAY_MIN, LGEMiscellaneous.SKILLBOOK_DELAY_MAX)

                            SetSkillNextReadTime(LaniatusETalentXes.LG_SKILL_LEADERSHIP, get_global_time() + iReadDelay)

                elif (item.GetVnum() == 50304) or (item.GetVnum() == 50305) or (item.GetVnum() == 50306):
                        if IsPolymorphed():
                            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You cannot read books while transformed."))
                            return LGEMiscellaneous.DEFINECONSTANTS.false

                        if GetSkillLevel(LaniatusETalentXes.LG_SKILL_COMBO) == 0 and GetLevel() < 30:
                            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You need Level 30 to understand this."))
                            return LGEMiscellaneous.DEFINECONSTANTS.false

                        if GetSkillLevel(LaniatusETalentXes.LG_SKILL_COMBO) == 1 and GetLevel() < 50:
                            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You need Level 50 to understand this."))
                            return LGEMiscellaneous.DEFINECONSTANTS.false

                        if GetSkillLevel(LaniatusETalentXes.LG_SKILL_COMBO) >= 2:
                            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You can't train any more Combos."))
                            return LGEMiscellaneous.DEFINECONSTANTS.false

                        iPct = item.GetValue(0)

                        if LearnSkillByBook(LaniatusETalentXes.LG_SKILL_COMBO, iPct):
                            ITEM_MANAGER.instance().RemoveItem(item, NULL)

                            iReadDelay = number(LGEMiscellaneous.SKILLBOOK_DELAY_MIN, LGEMiscellaneous.SKILLBOOK_DELAY_MAX)

                            SetSkillNextReadTime(LaniatusETalentXes.LG_SKILL_COMBO, get_global_time() + iReadDelay)
                elif (item.GetVnum() == 50311) or (item.GetVnum() == 50312) or (item.GetVnum() == 50313):
                        if IsPolymorphed():
                            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You cannot read books while transformed."))
                            return LGEMiscellaneous.DEFINECONSTANTS.false

                        dwSkillVnum = uint(item.GetValue(0))
                        iPct = MINMAX(0, item.GetValue(1), 100)
                        if GetSkillLevel(dwSkillVnum)>=20 or dwSkillVnum-LaniatusETalentXes.LG_SKILL_LANGUAGE1+1 == GetEmpire():
                            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You already speak this language fluently."))
                            return LGEMiscellaneous.DEFINECONSTANTS.false

                        if LearnSkillByBook(dwSkillVnum, iPct):
                            ITEM_MANAGER.instance().RemoveItem(item, NULL)

                            iReadDelay = number(LGEMiscellaneous.SKILLBOOK_DELAY_MIN, LGEMiscellaneous.SKILLBOOK_DELAY_MAX)

                            SetSkillNextReadTime(dwSkillVnum, get_global_time() + iReadDelay)

                elif item.GetVnum() == 50061:
                        if IsPolymorphed():
                            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You cannot read books while transformed."))
                            return LGEMiscellaneous.DEFINECONSTANTS.false

                        dwSkillVnum = uint(item.GetValue(0))
                        iPct = MINMAX(0, item.GetValue(1), 100)

                        if GetSkillLevel(dwSkillVnum) >= 10:
                            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You can't raise your Skills anymore."))
                            return LGEMiscellaneous.DEFINECONSTANTS.false

                        if LearnSkillByBook(dwSkillVnum, iPct):
                            ITEM_MANAGER.instance().RemoveItem(item, NULL)

                            iReadDelay = number(LGEMiscellaneous.SKILLBOOK_DELAY_MIN, LGEMiscellaneous.SKILLBOOK_DELAY_MAX)

                            SetSkillNextReadTime(dwSkillVnum, get_global_time() + iReadDelay)

                elif (item.GetVnum() == 50314) or (item.GetVnum() == 50315) or (item.GetVnum() == 50316) or (item.GetVnum() == 50323) or (item.GetVnum() == 50324) or (item.GetVnum() == 50325) or (item.GetVnum() == 50326):
                        if IsPolymorphed() == ((not LGEMiscellaneous.DEFINECONSTANTS.false)):
                            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You cannot change your state as long as you are transformed."))
                            return LGEMiscellaneous.DEFINECONSTANTS.false

                        iSkillLevelLowLimit = item.GetValue(0)
                        iSkillLevelHighLimit = item.GetValue(1)
                        iPct = MINMAX(0, item.GetValue(2), 100)
                        iLevelLimit = item.GetValue(3)
                        dwSkillVnum = 0

                        if (item.GetVnum() == 50314) or (item.GetVnum() == 50315) or (item.GetVnum() == 50316):
                            dwSkillVnum = LaniatusETalentXes.LG_SKILL_POLYMORPH

                        elif (item.GetVnum() == 50323) or (item.GetVnum() == 50324):
                            dwSkillVnum = LaniatusETalentXes.LG_SKILL_ADD_HP

                        elif (item.GetVnum() == 50325) or (item.GetVnum() == 50326):
                            dwSkillVnum = LaniatusETalentXes.LG_SKILL_RESIST_PENETRATE

                        else:
                            return LGEMiscellaneous.DEFINECONSTANTS.false

                        if 0 == dwSkillVnum:
                            return LGEMiscellaneous.DEFINECONSTANTS.false

                        if GetLevel() < iLevelLimit:
                            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You have to raise your Level to understand this Book."))
                            return LGEMiscellaneous.DEFINECONSTANTS.false

                        if GetSkillLevel(dwSkillVnum) >= 40:
                            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You can't raise your Skills anymore."))
                            return LGEMiscellaneous.DEFINECONSTANTS.false

                        if GetSkillLevel(dwSkillVnum) < iSkillLevelLowLimit:
                            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("It isn't easy to understand this Book."))
                            return LGEMiscellaneous.DEFINECONSTANTS.false

                        if GetSkillLevel(dwSkillVnum) >= iSkillLevelHighLimit:
                            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You can't train further with this Book."))
                            return LGEMiscellaneous.DEFINECONSTANTS.false

                        if LearnSkillByBook(dwSkillVnum, iPct):
                            ITEM_MANAGER.instance().RemoveItem(item, NULL)

                            iReadDelay = number(LGEMiscellaneous.SKILLBOOK_DELAY_MIN, LGEMiscellaneous.SKILLBOOK_DELAY_MAX)

                            SetSkillNextReadTime(dwSkillVnum, get_global_time() + iReadDelay)

                elif (item.GetVnum() == 50314) or (item.GetVnum() == 50315) or (item.GetVnum() == 50316) or (item.GetVnum() == 50323) or (item.GetVnum() == 50324) or (item.GetVnum() == 50325) or (item.GetVnum() == 50326) or (item.GetVnum() == 50902) or (item.GetVnum() == 50903) or (item.GetVnum() == 50904):
                        if IsPolymorphed():
                            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You cannot read books while transformed."))
                            return LGEMiscellaneous.DEFINECONSTANTS.false

                        dwSkillVnum = LaniatusETalentXes.LG_SKILL_CREATE
                        iPct = MINMAX(0, item.GetValue(1), 100)

                        if GetSkillLevel(dwSkillVnum)>=40:
                            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You can't raise your Skills anymore."))
                            return LGEMiscellaneous.DEFINECONSTANTS.false

                        if LearnSkillByBook(dwSkillVnum, iPct):
                            ITEM_MANAGER.instance().RemoveItem(item, NULL)

                            iReadDelay = number(LGEMiscellaneous.SKILLBOOK_DELAY_MIN, LGEMiscellaneous.SKILLBOOK_DELAY_MAX)

                            SetSkillNextReadTime(dwSkillVnum, get_global_time() + iReadDelay)

                            if test_server:
                                ChatPacket(EChatType.CHAT_TYPE_INFO, "[TEST_SERVER] Success to learn skill ")
                        else:
                            if test_server:
                                ChatPacket(EChatType.CHAT_TYPE_INFO, "[TEST_SERVER] Failed to learn skill ")

                elif item.GetVnum() == ITEM_MINING_LG_SKILL_TRAIN_BOOK:
                        if IsPolymorphed():
                            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You cannot read books while transformed."))
                            return LGEMiscellaneous.DEFINECONSTANTS.false

                        dwSkillVnum = LaniatusETalentXes.LG_SKILL_MINING
                        iPct = MINMAX(0, item.GetValue(1), 100)

                        if GetSkillLevel(dwSkillVnum)>=40:
                            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You can't raise your Skills anymore."))
                            return LGEMiscellaneous.DEFINECONSTANTS.false

                        if LearnSkillByBook(dwSkillVnum, iPct):
                            ITEM_MANAGER.instance().RemoveItem(item, NULL)

                            iReadDelay = number(LGEMiscellaneous.SKILLBOOK_DELAY_MIN, LGEMiscellaneous.SKILLBOOK_DELAY_MAX)

                            SetSkillNextReadTime(dwSkillVnum, get_global_time() + iReadDelay)

                elif item.GetVnum() == ITEM_HORSE_LG_SKILL_TRAIN_BOOK:
                        if IsPolymorphed():
                            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You cannot read books while transformed."))
                            return LGEMiscellaneous.DEFINECONSTANTS.false

                        dwSkillVnum = LaniatusETalentXes.LG_SKILL_HORSE
                        iPct = MINMAX(0, item.GetValue(1), 100)

                        if GetLevel() < 50:
                            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You don't have the right Level for Rider Training."))
                            return LGEMiscellaneous.DEFINECONSTANTS.false

                        if (not test_server) and get_global_time() < GetSkillNextReadTime(dwSkillVnum):
                            if FindAffect(LaniatusEAffectTypes.LANIA_AFFECT_LG_SKILL_NO_BOOK_DELAY):
                                RemoveAffect(LaniatusEAffectTypes.LANIA_AFFECT_LG_SKILL_NO_BOOK_DELAY)
                                ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You escaped the Evil Ghost Curse with the help of an Exorcism Scroll."))
                            else:
                                SkillLearnWaitMoreTimeMessage(GetSkillNextReadTime(dwSkillVnum) - get_global_time())
                                return LGEMiscellaneous.DEFINECONSTANTS.false

                        if GetPoint(EPointTypes.LG_POINT_HORSE_SKILL) >= 20 or GetSkillLevel(LaniatusETalentXes.LG_SKILL_HORSE_WILDATTACK) + GetSkillLevel(LaniatusETalentXes.LG_SKILL_HORSE_CHARGE) + GetSkillLevel(LaniatusETalentXes.LG_SKILL_HORSE_ESCAPE) >= 60 or GetSkillLevel(LaniatusETalentXes.LG_SKILL_HORSE_WILDATTACK_RANGE) + GetSkillLevel(LaniatusETalentXes.LG_SKILL_HORSE_CHARGE) + GetSkillLevel(LaniatusETalentXes.LG_SKILL_HORSE_ESCAPE) >= 60:
                            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You cannot read more Riding Guides."))
                            return LGEMiscellaneous.DEFINECONSTANTS.false

                        if number(1, 100) <= iPct:
                            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You received Riding Points after reading the Riding Guide."))
                            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You can raise your Riding Skill Level through received Points."))
                            PointChange(EPointTypes.LG_POINT_HORSE_SKILL, 1)

                            iReadDelay = number(LGEMiscellaneous.SKILLBOOK_DELAY_MIN, LGEMiscellaneous.SKILLBOOK_DELAY_MAX)

                            if not test_server:
                                SetSkillNextReadTime(dwSkillVnum, get_global_time() + iReadDelay)
                        else:
                            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You did not understand the Riding Guide."))

                        ITEM_MANAGER.instance().RemoveItem(item, NULL)

                elif (item.GetVnum() == 70102) or (item.GetVnum() == 70103):
                        if GetAlignment() >= 0:
                            return LGEMiscellaneous.DEFINECONSTANTS.false

                        delta = MIN(-GetAlignment(), item.GetValue(0))

                        #sys_log(0, "%s ALIGNMENT ITEM %d", GetName(), delta)

                        UpdateAlignment(delta)
                        item.SetCount(item.GetCount() - 1)

                        if math.trunc(delta / float(10)) > 0:
                            ChatPacket(EChatType.CHAT_TYPE_TALKING, LC_TEXT("Your mind is clear. You can concentrate well now."))
                            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Your Rank raised up to %d ."), math.trunc(delta / float(10)))

                elif item.GetVnum() == 71107:
                        val = item.GetValue(0)
                        interval = item.GetValue(1)
                        pPC = quest.CQuestManager.instance().GetPC(GetPlayerID())
                        last_use_time = pPC.GetFlag("mythical_peach.last_use_time")

                        if get_global_time() - last_use_time < interval * 60 * 60:
                            if test_server == LGEMiscellaneous.DEFINECONSTANTS.false:
                                ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You cannot use it now."))
                                return LGEMiscellaneous.DEFINECONSTANTS.false
                            else:
                                ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Test server time limit passed "))

                        if GetAlignment() == 200000:
                            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Your rank  cannot raise any more."))
                            return LGEMiscellaneous.DEFINECONSTANTS.false

                        if 200000 - GetAlignment() < val * 10:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
                            val = (200000 - GetAlignment()) / 10

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
                        old_alignment = GetAlignment() / 10

                        UpdateAlignment(val *10)

                        item.SetCount(item.GetCount()-1)
                        pPC.SetFlag("mythical_peach.last_use_time", get_global_time(), DefineConstants.false)

                        ChatPacket(EChatType.CHAT_TYPE_TALKING, LC_TEXT("Your mind is clear. You can concentrate well now."))
                        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Your Rank raised up to %d ."), val)

                elif (item.GetVnum() == 71109) or (item.GetVnum() == 72719):
                        item2 = None

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if (!IsValidItemPosition(DestCell) || !(item2 = GetItem(DestCell)))
                        if (not IsValidItemPosition(DestCell)) or not(item2 = GetItem(DestCell)):
                            return LGEMiscellaneous.DEFINECONSTANTS.false

                        if item2.IsExchanging() == ((not LGEMiscellaneous.DEFINECONSTANTS.false)):
                            return LGEMiscellaneous.DEFINECONSTANTS.false

                        if item2.GetSocketCount() == 0:
                            return LGEMiscellaneous.DEFINECONSTANTS.false

                        if item2.IsEquipped():
                            return LGEMiscellaneous.DEFINECONSTANTS.false

                        if item2.GetType() == EItemTypes.ITEM_WEAPON:
                            pass
                        elif item2.GetType() == EItemTypes.ITEM_ARMOR:
                            if (item2.GetSubType() == EArmorSubTypes.ARMOR_EAR) or (item2.GetSubType() == EArmorSubTypes.ARMOR_WRIST) or (item2.GetSubType() == EArmorSubTypes.ARMOR_NECK) or (item2.GetSubType() == EArmorSubTypes.ARMOR_PENDANT):
                                ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("No metin stone to take out."))
                                return LGEMiscellaneous.DEFINECONSTANTS.false


                        if item2.GetType() != ITEM_WEAPON:
                            return LGEMiscellaneous.DEFINECONSTANTS.false

                        socket = std::stack()

                        i = 0
                        while i < EItemMisc.LG_ITEM_SOCKET_MAX_NUM:
                            socket.push(item2.GetSocket(i))
                            i += 1

                        idx = EItemMisc.LG_ITEM_SOCKET_MAX_NUM - 1

                        while socket.size() > 0:
                            if socket.top() > 2 and socket.top() != ITEM_BROKEN_METIN_VNUM:
                                break

                            idx -= 1
                            socket.pop()

                        if socket.size() == 0:
                            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("No metin stone to take out."))
                            return LGEMiscellaneous.DEFINECONSTANTS.false

                        pItemReward = AutoGiveItem(socket.top())

                        if pItemReward is not None:
                            item2.SetSocket(idx, 1, ((not DefineConstants.false)))
                            item.SetCount(item.GetCount() - 1)

                elif (item.GetVnum() == 71109) or (item.GetVnum() == 72719) or (item.GetVnum() == 70201) or (item.GetVnum() == 70202) or (item.GetVnum() == 70203) or (item.GetVnum() == 70204) or (item.GetVnum() == 70205) or (item.GetVnum() == 70206):
                        if GetPart(EParts.PART_HAIR) >= 1001:
                            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You cannot dye or bleach your current Hairstyle."))
                        else:
                            q = quest.CQuestManager.instance()
                            pPC = q.GetPC(GetPlayerID())

                            if pPC:
                                last_dye_level = pPC.GetFlag("dyeing_hair.last_dye_level")

                                if last_dye_level == 0 or last_dye_level+3 <= GetLevel() or item.GetVnum() == 70201:
                                    SetPart(EParts.PART_HAIR, item.GetVnum() - 70201)

                                    if item.GetVnum() == 70201:
                                        pPC.SetFlag("dyeing_hair.last_dye_level", 0, DefineConstants.false)
                                    else:
                                        pPC.SetFlag("dyeing_hair.last_dye_level", GetLevel(), DefineConstants.false)

                                    item.SetCount(item.GetCount() - 1)
                                    UpdatePacket()
                                else:
                                    ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You need to reach Level %d to be able to dye your Hair again."), last_dye_level+3)

                elif item.GetVnum() == ITEM_NEW_YEAR_GREETING_VNUM:
                        dwBoxVnum = uint(ITEM_NEW_YEAR_GREETING_VNUM)
                        dwVnums = []
                        dwCounts = []
                        item_gets = []
                        count = 0

                        if GiveItemFromSpecialItemGroup(dwBoxVnum, dwVnums, dwCounts, item_gets, count):
                            for i in range(0, count):
                                if dwVnums[i] == CSpecialItemGroup.EGiveType.GOLD:
                                    ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You received %d Yang."), dwCounts[i])

                            item.SetCount(item.GetCount() - 1)

                elif (item.GetVnum() == ITEM_VALENTINE_ROSE) or (item.GetVnum() == ITEM_VALENTINE_CHOCOLATE):
                        dwBoxVnum = item.GetVnum()
                        dwVnums = []
                        dwCounts = []
                        item_gets = [None for _ in range(0)]
                        count = 0


                        if item.GetVnum() == ITEM_VALENTINE_ROSE and ESex.LG_SEX_MALE == GET_SEX(self) or item.GetVnum() == ITEM_VALENTINE_CHOCOLATE and ESex.LG_SEX_FEMALE == GET_SEX(self):
                            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("This Item can be opened by the other gender only."))
                            return LGEMiscellaneous.DEFINECONSTANTS.false


                        if GiveItemFromSpecialItemGroup(dwBoxVnum, dwVnums, dwCounts, item_gets, count):
                            item.SetCount(item.GetCount()-1)

                elif (item.GetVnum() == ITEM_WHITEDAY_CANDY) or (item.GetVnum() == ITEM_WHITEDAY_ROSE):
                        dwBoxVnum = item.GetVnum()
                        dwVnums = []
                        dwCounts = []
                        item_gets = [None for _ in range(0)]
                        count = 0


                        if item.GetVnum() == ITEM_WHITEDAY_CANDY and ESex.LG_SEX_MALE == GET_SEX(self) or item.GetVnum() == ITEM_WHITEDAY_ROSE and ESex.LG_SEX_FEMALE == GET_SEX(self):
                            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("This Item can be opened by the other gender only."))
                            return LGEMiscellaneous.DEFINECONSTANTS.false


                        if GiveItemFromSpecialItemGroup(dwBoxVnum, dwVnums, dwCounts, item_gets, count):
                            item.SetCount(item.GetCount()-1)

                elif item.GetVnum() == 50011:
                        dwBoxVnum = 50011
                        dwVnums = []
                        dwCounts = []
                        item_gets = [None for _ in range(0)]
                        count = 0

                        if GiveItemFromSpecialItemGroup(dwBoxVnum, dwVnums, dwCounts, item_gets, count):
                            for i in range(0, count):
                                item.SetCount(item.GetCount() - 1)

                                if dwVnums[i] == CSpecialItemGroup.EGiveType.GOLD:
                                    ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You received %d Yang."), dwCounts[i])

                                elif dwVnums[i] == CSpecialItemGroup.EGiveType.EXP:
                                    ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Mysterious light comes out of this box."))
                                    ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You received %d Experience Points."), dwCounts[i])

                                elif dwVnums[i] == CSpecialItemGroup.EGiveType.MOB:
                                    ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("A monster came out of the box!"))

                                elif dwVnums[i] == CSpecialItemGroup.EGiveType.SLOW:
                                    ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("If you inhale the red smoke coming out of the box, you will move faster!"))

                                elif dwVnums[i] == CSpecialItemGroup.EGiveType.DRAIN_HP:
                                    ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("The box exploded suddenly! Your HP are lower."))

                                elif dwVnums[i] == CSpecialItemGroup.EGiveType.POISON:
                                    ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("If you inhale the green smoke coming from the box, poison will spread in your body!"))

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if ENABLE_WOLFMAN
                                elif dwVnums[i] == CSpecialItemGroup.EGiveType.BLEEDING:
                                    ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("If you inhale the green smoke coming from the box, poison will spread in your body!"))
##endif

                                elif dwVnums[i] == CSpecialItemGroup.EGiveType.MOB_GROUP:
                                    ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("A monster came out of the box!"))

                                else:
                                    if item_gets[i]:
                                        if dwCounts[i] > 1:
                                            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("There are %s of %d in the box."), item_gets[i].GetName(LOCALE_LANIATUS), dwCounts[i])
                                        else:
                                            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("There is %s in the box."), item_gets[i].GetName(LOCALE_LANIATUS))
                        else:
                            ChatPacket(EChatType.CHAT_TYPE_TALKING, LC_TEXT("You received nothing."))
                            return LGEMiscellaneous.DEFINECONSTANTS.false

                elif (item.GetVnum() == 50011) or (item.GetVnum() == ITEM_GIVE_STAT_RESET_COUNT_VNUM):
                        PointChange(EPointTypes.LG_POINT_STAT_RESET_COUNT, 1)
                        item.SetCount(item.GetCount()-1)

                elif item.GetVnum() == 50107:
                        EffectPacket(SPECIAL_EFFECT.SE_CHINA_FIREWORK)
                        AddAffect(LaniatusEAffectTypes.LANIA_AFFECT_CHINA_FIREWORK, EPointTypes.LG_POINT_STUN_PCT, 30, EAffectBits.AFF_CHINA_FIREWORK, 5 *60, 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
                        item.SetCount(item.GetCount()-1)

                elif item.GetVnum() == 50108:
                        EffectPacket(SPECIAL_EFFECT.SE_SPIN_TOP)
                        AddAffect(LaniatusEAffectTypes.LANIA_AFFECT_CHINA_FIREWORK, EPointTypes.LG_POINT_STUN_PCT, 30, EAffectBits.AFF_CHINA_FIREWORK, 5 *60, 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
                        item.SetCount(item.GetCount()-1)

                elif item.GetVnum() == ITEM_WONSO_BEAN_VNUM:
                    PointChange(EPointTypes.LG_POINT_HP, GetMaxHP() - GetHP())
                    item.SetCount(item.GetCount()-1)

                elif item.GetVnum() == ITEM_WONSO_SUGAR_VNUM:
                    PointChange(EPointTypes.LG_POINT_SP, GetMaxSP() - GetSP())
                    item.SetCount(item.GetCount()-1)

                elif item.GetVnum() == ITEM_WONSO_FRUIT_VNUM:
                    PointChange(EPointTypes.LG_POINT_STAMINA, GetMaxStamina()-GetStamina())
                    item.SetCount(item.GetCount()-1)

                elif item.GetVnum() == EItemMisc.ITEM_ELK_VNUM:
                        iGold = item.GetSocket(0)
                        ITEM_MANAGER.instance().RemoveItem(item, NULL)
                        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You received %d Yang."), iGold)
                        PointChange(EPointTypes.LG_POINT_GOLD, iGold)

                elif item.GetVnum() == 27995:

                elif item.GetVnum() == 71092:
                        if m_pkChrTarget is not None:
                            if m_pkChrTarget.IsPolymorphed():
                                m_pkChrTarget.SetPolymorph(0)
                                m_pkChrTarget.RemoveAffect(LaniatusEAffectTypes.LANIA_AFFECT_POLYMORPH)
                        else:
                            if IsPolymorphed():
                                SetPolymorph(0)
                                RemoveAffect(LaniatusEAffectTypes.LANIA_AFFECT_POLYMORPH)

                elif (item.GetVnum() == ITEM_AUTO_HP_RECOVERY_S) or (item.GetVnum() == ITEM_AUTO_HP_RECOVERY_M) or (item.GetVnum() == ITEM_AUTO_HP_RECOVERY_L) or (item.GetVnum() == ITEM_AUTO_HP_RECOVERY_X) or (item.GetVnum() == ITEM_AUTO_SP_RECOVERY_S) or (item.GetVnum() == ITEM_AUTO_SP_RECOVERY_M) or (item.GetVnum() == ITEM_AUTO_SP_RECOVERY_L) or (item.GetVnum() == ITEM_AUTO_SP_RECOVERY_X) or (item.GetVnum() == REWARD_BOX_ITEM_AUTO_SP_RECOVERY_XS) or (item.GetVnum() == REWARD_BOX_ITEM_AUTO_SP_RECOVERY_S) or (item.GetVnum() == REWARD_BOX_ITEM_AUTO_HP_RECOVERY_XS) or (item.GetVnum() == REWARD_BOX_ITEM_AUTO_HP_RECOVERY_S) or (item.GetVnum() == FUCKING_BRAZIL_ITEM_AUTO_SP_RECOVERY_S) or (item.GetVnum() == FUCKING_BRAZIL_ITEM_AUTO_HP_RECOVERY_S):
                        type = LaniatusEAffectTypes.LANIA_AFFECT_NONE
                        isSpecialPotion = LGEMiscellaneous.DEFINECONSTANTS.false

                        if item.GetVnum() == ITEM_AUTO_HP_RECOVERY_X:
                            isSpecialPotion = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

                        if (item.GetVnum() == ITEM_AUTO_HP_RECOVERY_X) or (item.GetVnum() == ITEM_AUTO_HP_RECOVERY_S) or (item.GetVnum() == ITEM_AUTO_HP_RECOVERY_M) or (item.GetVnum() == ITEM_AUTO_HP_RECOVERY_L) or (item.GetVnum() == REWARD_BOX_ITEM_AUTO_HP_RECOVERY_XS) or (item.GetVnum() == REWARD_BOX_ITEM_AUTO_HP_RECOVERY_S) or (item.GetVnum() == FUCKING_BRAZIL_ITEM_AUTO_HP_RECOVERY_S):
                            type = LaniatusEAffectTypes.LANIA_AFFECT_AUTO_HP_RECOVERY

                        elif item.GetVnum() == ITEM_AUTO_SP_RECOVERY_X:
                            isSpecialPotion = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

                        elif (item.GetVnum() == ITEM_AUTO_SP_RECOVERY_X) or (item.GetVnum() == ITEM_AUTO_SP_RECOVERY_S) or (item.GetVnum() == ITEM_AUTO_SP_RECOVERY_M) or (item.GetVnum() == ITEM_AUTO_SP_RECOVERY_L) or (item.GetVnum() == REWARD_BOX_ITEM_AUTO_SP_RECOVERY_XS) or (item.GetVnum() == REWARD_BOX_ITEM_AUTO_SP_RECOVERY_S) or (item.GetVnum() == FUCKING_BRAZIL_ITEM_AUTO_SP_RECOVERY_S):
                            type = LaniatusEAffectTypes.LANIA_AFFECT_AUTO_SP_RECOVERY

                        if LaniatusEAffectTypes.LANIA_AFFECT_NONE == type:
                            break

                        if item.GetCount() > 1:
                            pos = GetEmptyInventory(item.GetSize())

                            if -1 == pos:
                                ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("There isn't enough space in the inventory."))
                                break

                            item.SetCount(item.GetCount() - 1)

                            item2 = ITEM_MANAGER.instance().CreateItem(item.GetVnum(), 1, 0, DefineConstants.false, -1, DefineConstants.false)
                            item2.AddToCharacter(self, TItemPos(EWindows.INVENTORY, pos))

                            if item.GetSocket(1) != 0:
                                item2.SetSocket(1, item.GetSocket(1), ((not DefineConstants.false)))

                            item = item2

                        pAffect = FindAffect(type)

                        if None is pAffect:
                            bonus = EPointTypes.LG_POINT_NONE

                            if ((not LGEMiscellaneous.DEFINECONSTANTS.false)) == isSpecialPotion:
                                if type == LaniatusEAffectTypes.LANIA_AFFECT_AUTO_HP_RECOVERY:
                                    bonus = EPointTypes.LG_POINT_MAX_HP_PCT
                                elif type == LaniatusEAffectTypes.LANIA_AFFECT_AUTO_SP_RECOVERY:
                                    bonus = EPointTypes.LG_POINT_MAX_SP_PCT

                            AddAffect(type, bonus, 4, item.GetID(), AffectVariable.INFINITE_LANIA_AFFECT_DURATION, 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), LGEMiscellaneous.DEFINECONSTANTS.false)

                            item.Lock(((not LGEMiscellaneous.DEFINECONSTANTS.false)))
                            item.SetSocket(0,1 if ((not LGEMiscellaneous.DEFINECONSTANTS.false)) else 0, ((not DefineConstants.false)))

                            AutoRecoveryItemProcess(type)
                        else:
                            if item.GetID() == pAffect.dwFlag:
                                RemoveAffect(pAffect)

                                item.Lock(LGEMiscellaneous.DEFINECONSTANTS.false)
                                item.SetSocket(0, LGEMiscellaneous.DEFINECONSTANTS.false, ((not DefineConstants.false)))
                            else:
                                old = FindItemByID(pAffect.dwFlag)

                                if None is not old:
                                    old.Lock(LGEMiscellaneous.DEFINECONSTANTS.false)
                                    old.SetSocket(0, LGEMiscellaneous.DEFINECONSTANTS.false, ((not DefineConstants.false)))

                                RemoveAffect(pAffect)

                                bonus = EPointTypes.LG_POINT_NONE

                                if ((not LGEMiscellaneous.DEFINECONSTANTS.false)) == isSpecialPotion:
                                    if type == LaniatusEAffectTypes.LANIA_AFFECT_AUTO_HP_RECOVERY:
                                        bonus = EPointTypes.LG_POINT_MAX_HP_PCT
                                    elif type == LaniatusEAffectTypes.LANIA_AFFECT_AUTO_SP_RECOVERY:
                                        bonus = EPointTypes.LG_POINT_MAX_SP_PCT

                                AddAffect(type, bonus, 4, item.GetID(), AffectVariable.INFINITE_LANIA_AFFECT_DURATION, 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), LGEMiscellaneous.DEFINECONSTANTS.false)

                                item.Lock(((not LGEMiscellaneous.DEFINECONSTANTS.false)))
                                item.SetSocket(0,1 if ((not LGEMiscellaneous.DEFINECONSTANTS.false)) else 0, ((not DefineConstants.false)))

                                AutoRecoveryItemProcess(type)

            elif (item.GetSubType() == EUseSubTypes.USE_SPECIAL) or (item.GetSubType() == EUseSubTypes.USE_CLEAR):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
            ##if ENABLE_WOLFMAN
                    if item.GetVnum() == 27124:
                        RemoveBleeding()
            ##endif
                    else:
                        RemoveBadAffect()
                    item.SetCount(item.GetCount() - 1)

            elif (item.GetSubType() == EUseSubTypes.USE_SPECIAL) or (item.GetSubType() == EUseSubTypes.USE_CLEAR) or (item.GetSubType() == EUseSubTypes.USE_INVISIBILITY):
                    if item.GetVnum() == 70026:
                        q = quest.CQuestManager.instance()
                        pPC = q.GetPC(GetPlayerID())

                        if pPC is not None:
                            last_use_time = pPC.GetFlag("mirror_of_disapper.last_use_time")

                            if get_global_time() - last_use_time < 10 *60:
                                ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You cannot use it now."))
                                return LGEMiscellaneous.DEFINECONSTANTS.false

                            pPC.SetFlag("mirror_of_disapper.last_use_time", get_global_time(), DefineConstants.false)

                    AddAffect(LaniatusEAffectTypes.LANIA_AFFECT_INVISIBILITY, EPointTypes.LG_POINT_NONE, 0, EAffectBits.AFF_INVISIBILITY, 300, 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
                    item.SetCount(item.GetCount() - 1)

            elif item.GetSubType() == EUseSubTypes.USE_POTION_NODELAY:
                    used = LGEMiscellaneous.DEFINECONSTANTS.false

                    if item.GetValue(0) != 0:
                        if GetHP() < GetMaxHP():
                            PointChange(EPointTypes.LG_POINT_HP, math.trunc(item.GetValue(0) * (100 + GetPoint(EPointTypes.LG_POINT_POTION_BONUS)) / float(100)))
                            EffectPacket(SPECIAL_EFFECT.SE_HPUP_RED)
                            used = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

                    if item.GetValue(1) != 0:
                        if GetSP() < GetMaxSP():
                            PointChange(EPointTypes.LG_POINT_SP, math.trunc(item.GetValue(1) * (100 + GetPoint(EPointTypes.LG_POINT_POTION_BONUS)) / float(100)))
                            EffectPacket(SPECIAL_EFFECT.SE_SPUP_BLUE)
                            used = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

                    if item.GetValue(3) != 0:
                        if GetHP() < GetMaxHP():
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
                            PointChange(EPointTypes.LG_POINT_HP, item.GetValue(3) * GetMaxHP() / 100)
                            EffectPacket(SPECIAL_EFFECT.SE_HPUP_RED)
                            used = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

                    if item.GetValue(4) != 0:
                        if GetSP() < GetMaxSP():
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
                            PointChange(EPointTypes.LG_POINT_SP, item.GetValue(4) * GetMaxSP() / 100)
                            EffectPacket(SPECIAL_EFFECT.SE_SPUP_BLUE)
                            used = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

                    if used:
                        if GetDungeon():
                            GetDungeon().UsePotion(self)

                        if GetWarMap():
                            GetWarMap().UsePotion(self, item)

                        item.SetCount(item.GetCount() - 1)

            elif item.GetSubType() == EUseSubTypes.USE_POTION:
                if item.GetValue(1) != 0:
                    if GetPoint(EPointTypes.LG_POINT_SP_RECOVERY) + GetSP() >= GetMaxSP():
                        return LGEMiscellaneous.DEFINECONSTANTS.false

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
                    PointChange(EPointTypes.LG_POINT_SP_RECOVERY, item.GetValue(1) * MIN(200, (100 + GetPoint(EPointTypes.LG_POINT_POTION_BONUS))) / 100)
                    StartAffectEvent()
                    EffectPacket(SPECIAL_EFFECT.SE_SPUP_BLUE)

                if item.GetValue(0) != 0:
                    if GetPoint(EPointTypes.LG_POINT_HP_RECOVERY) + GetHP() >= GetMaxHP():
                        return LGEMiscellaneous.DEFINECONSTANTS.false

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
                    PointChange(EPointTypes.LG_POINT_HP_RECOVERY, item.GetValue(0) * MIN(200, (100 + GetPoint(EPointTypes.LG_POINT_POTION_BONUS))) / 100)
                    StartAffectEvent()
                    EffectPacket(SPECIAL_EFFECT.SE_HPUP_RED)

                if GetDungeon():
                    GetDungeon().UsePotion(self)

                if GetWarMap():
                    GetWarMap().UsePotion(self, item)

                item.SetCount(item.GetCount() - 1)

            elif item.GetSubType() == EUseSubTypes.USE_POTION_CONTINUE:
                    if item.GetValue(0) != 0:
                        AddAffect(LaniatusEAffectTypes.LANIA_AFFECT_HP_RECOVER_CONTINUE, EPointTypes.LG_POINT_HP_RECOVER_CONTINUE, item.GetValue(0), 0, item.GetValue(2), 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
                    elif item.GetValue(1) != 0:
                        AddAffect(LaniatusEAffectTypes.LANIA_AFFECT_SP_RECOVER_CONTINUE, EPointTypes.LG_POINT_SP_RECOVER_CONTINUE, item.GetValue(1), 0, item.GetValue(2), 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
                    else:
                        return LGEMiscellaneous.DEFINECONSTANTS.false

                if GetDungeon():
                    GetDungeon().UsePotion(self)

                if GetWarMap():
                    GetWarMap().UsePotion(self, item)

                item.SetCount(item.GetCount() - 1)

            elif item.GetSubType() == EUseSubTypes.USE_ABILITY_UP:
                    if item.GetValue(0) == EApplyTypes.APPLY_MOV_SPEED:
                        AddAffect(LaniatusEAffectTypes.LANIA_AFFECT_MOV_SPEED, EPointTypes.LG_POINT_MOV_SPEED, item.GetValue(2), EAffectBits.AFF_MOV_SPEED_POTION, item.GetValue(1), 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)))

                    elif item.GetValue(0) == EApplyTypes.APPLY_ATT_SPEED:
                        AddAffect(LaniatusEAffectTypes.LANIA_AFFECT_ATT_SPEED, EPointTypes.LG_POINT_ATT_SPEED, item.GetValue(2), EAffectBits.AFF_ATT_SPEED_POTION, item.GetValue(1), 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)))

                    elif item.GetValue(0) == EApplyTypes.APPLY_STR:
                        AddAffect(LaniatusEAffectTypes.LANIA_AFFECT_STR, EPointTypes.LG_POINT_ST, item.GetValue(2), 0, item.GetValue(1), 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)))

                    elif item.GetValue(0) == EApplyTypes.APPLY_DEX:
                        AddAffect(LaniatusEAffectTypes.LANIA_AFFECT_DEX, EPointTypes.LG_POINT_DX, item.GetValue(2), 0, item.GetValue(1), 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)))

                    elif item.GetValue(0) == EApplyTypes.APPLY_CON:
                        AddAffect(LaniatusEAffectTypes.LANIA_AFFECT_CON, EPointTypes.LG_POINT_HT, item.GetValue(2), 0, item.GetValue(1), 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)))

                    elif item.GetValue(0) == EApplyTypes.APPLY_INT:
                        AddAffect(LaniatusEAffectTypes.LANIA_AFFECT_INT, EPointTypes.LG_POINT_IQ, item.GetValue(2), 0, item.GetValue(1), 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)))

                    elif item.GetValue(0) == EApplyTypes.APPLY_CAST_SPEED:
                        AddAffect(LaniatusEAffectTypes.LANIA_AFFECT_CAST_SPEED, EPointTypes.LG_POINT_CASTING_SPEED, item.GetValue(2), 0, item.GetValue(1), 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)))

                    elif item.GetValue(0) == EApplyTypes.APPLY_ATT_GRADE_BONUS:
                        AddAffect(LaniatusEAffectTypes.LANIA_AFFECT_ATT_GRADE, EPointTypes.LG_POINT_ATT_GRADE_BONUS, item.GetValue(2), 0, item.GetValue(1), 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)))

                    elif item.GetValue(0) == EApplyTypes.APPLY_DEF_GRADE_BONUS:
                        AddAffect(LaniatusEAffectTypes.LANIA_AFFECT_DEF_GRADE, EPointTypes.LG_POINT_DEF_GRADE_BONUS, item.GetValue(2), 0, item.GetValue(1), 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)))

                if GetDungeon():
                    GetDungeon().UsePotion(self)

                if GetWarMap():
                    GetWarMap().UsePotion(self, item)

                item.SetCount(item.GetCount() - 1)

            elif (item.GetSubType() == EUseSubTypes.USE_ABILITY_UP) or (item.GetSubType() == EUseSubTypes.USE_TALISMAN):
                    TOWN_PORTAL = 1
                    MEMORY_PORTAL = 2

                    if GetMapIndex() == 200 or GetMapIndex() == 113:
                        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You cannot use this from your current position."))
                        return LGEMiscellaneous.DEFINECONSTANTS.false

                    if m_pkWarpEvent:
                        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You are ready to teleport so you cannot use the Return Scroll."))
                        return LGEMiscellaneous.DEFINECONSTANTS.false

                    consumeLife = CalculateConsume(self)

                    if consumeLife < 0:
                        return LGEMiscellaneous.DEFINECONSTANTS.false

                    if item.GetValue(0) == TOWN_PORTAL:
                        if item.GetSocket(0) == 0:
                            if not GetDungeon():
                                if not GiveRecallItem(item):
                                    return LGEMiscellaneous.DEFINECONSTANTS.false

                            posWarp = pixel_position_s()

                            if SECTREE_MANAGER.instance().GetRecallPositionByEmpire(GetMapIndex(), GetEmpire(), posWarp):
                                PointChange(EPointTypes.LG_POINT_HP, -consumeLife, LGEMiscellaneous.DEFINECONSTANTS.false)
                                WarpSet(posWarp.x, posWarp.y)
                            else:
                                #lani_err("CHARACTER::UseItem : cannot find spawn position (name %s, %d x %d)", GetName(), GetX(), GetY())
                        else:
                            if test_server:
                                ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You are brought back to the place of origin."))

                            ProcessRecallItem(item)
                    elif item.GetValue(0) == MEMORY_PORTAL:
                        if item.GetSocket(0) == 0:
                            if GetDungeon():
                                ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("%s%s cannot be used in a dungeon."), item.GetName(LOCALE_LANIATUS), "")
                                return LGEMiscellaneous.DEFINECONSTANTS.false

                            if not GiveRecallItem(item):
                                return LGEMiscellaneous.DEFINECONSTANTS.false
                        else:
                            PointChange(EPointTypes.LG_POINT_HP, -consumeLife, LGEMiscellaneous.DEFINECONSTANTS.false)
                            ProcessRecallItem(item)

            elif (item.GetSubType() == EUseSubTypes.USE_TUNING) or (item.GetSubType() == EUseSubTypes.USE_DETACHMENT):
                    item2 = None

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if (!IsValidItemPosition(DestCell) || !(item2 = GetItem(DestCell)))
                    if (not IsValidItemPosition(DestCell)) or not(item2 = GetItem(DestCell)):
                        return LGEMiscellaneous.DEFINECONSTANTS.false

                    if item2.IsExchanging():
                        return LGEMiscellaneous.DEFINECONSTANTS.false

                    if item2.IsEquipped():
                        return LGEMiscellaneous.DEFINECONSTANTS.false

                    if CItemVnumHelper.IsAcceItem(item2.GetVnum()):
                        return LGEMiscellaneous.DEFINECONSTANTS.false

                    if item2.GetVnum() >= 28330 and item2.GetVnum() <= 28343:
                        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("+3 spirit stones can not be upgraded by this item."))
                        return LGEMiscellaneous.DEFINECONSTANTS.false

                    if item2.GetVnum() >= 28430 and item2.GetVnum() <= 28443:
                        if item.GetVnum() == 71056:
                            RefineItem(item, item2)
                        else:
                            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("The spirit stone can not be advanced by this item."))
                    else:
                        RefineItem(item, item2)

            elif (item.GetSubType() == EUseSubTypes.USE_PUT_INTO_BELT_SOCKET) or (item.GetSubType() == EUseSubTypes.USE_PUT_INTO_RING_SOCKET) or (item.GetSubType() == EUseSubTypes.USE_PUT_INTO_ACCESSORY_SOCKET) or (item.GetSubType() == EUseSubTypes.USE_ADD_ACCESSORY_SOCKET) or (item.GetSubType() == EUseSubTypes.USE_CLEAN_SOCKET) or (item.GetSubType() == EUseSubTypes.USE_CHANGE_COSTUME_ATTR) or (item.GetSubType() == EUseSubTypes.USE_RESET_COSTUME_ATTR) or (item.GetSubType() == EUseSubTypes.USE_CHANGE_ATTRIBUTE) or (item.GetSubType() == EUseSubTypes.USE_CHANGE_ATTRIBUTE2) or (item.GetSubType() == EUseSubTypes.USE_ADD_ATTRIBUTE) or (item.GetSubType() == EUseSubTypes.USE_ADD_ATTRIBUTE2):
                    item2 = None
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if (!IsValidItemPosition(DestCell) || !(item2 = GetItem(DestCell)))
                    if (not IsValidItemPosition(DestCell)) or not(item2 = GetItem(DestCell)):
                        return LGEMiscellaneous.DEFINECONSTANTS.false

                    if item2.IsEquipped():
                        BuffOnAttr_RemoveBuffsFromItem(item2)

                    if EItemTypes.ITEM_COSTUME == item2.GetType() and ECostumeSubTypes.COSTUME_ACCE == item2.GetSubType():
                        return LGEMiscellaneous.DEFINECONSTANTS.false

                    if EItemTypes.ITEM_COSTUME == item2.GetType() and item.GetVnum() != 70063 and item.GetVnum() != 70064:
                        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You cannot change the bonus of this Item."))
                        return LGEMiscellaneous.DEFINECONSTANTS.false

                    if item2.IsExchanging():
                        return LGEMiscellaneous.DEFINECONSTANTS.false

                    if item2.IsEquipped():
                        return LGEMiscellaneous.DEFINECONSTANTS.false

                    if item.GetSubType() == EUseSubTypes.USE_CLEAN_SOCKET:
                            i = None
                            i = 0
                            while i < EItemMisc.LG_ITEM_SOCKET_MAX_NUM:
                                if item2.GetSocket(i) == ITEM_BROKEN_METIN_VNUM:
                                    break
                                i += 1

                            if i == EItemMisc.LG_ITEM_SOCKET_MAX_NUM:
                                ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("No Stone there to be cleaned."))
                                return LGEMiscellaneous.DEFINECONSTANTS.false

                            j = 0

                            i = 0
                            while i < EItemMisc.LG_ITEM_SOCKET_MAX_NUM:
                                if item2.GetSocket(i) != ITEM_BROKEN_METIN_VNUM and item2.GetSocket(i) != 0:
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: item2->SetSocket(j++, item2->GetSocket(i));
                                    item2.SetSocket(j, item2.GetSocket(i), ((not DefineConstants.false)))
                                    j += 1
                                i += 1

                            while j < EItemMisc.LG_ITEM_SOCKET_MAX_NUM:
                                if item2.GetSocket(j) > 0:
                                    item2.SetSocket(j, 1, ((not DefineConstants.false)))
                                j += 1

                            item.SetCount(item.GetCount() - 1)


                    elif item.GetSubType() == EUseSubTypes.USE_CHANGE_COSTUME_ATTR:
                            if item2.GetType() != EItemTypes.ITEM_COSTUME:
                                return LGEMiscellaneous.DEFINECONSTANTS.false

                            if item2.GetSubType() != ECostumeSubTypes.COSTUME_BODY and item2.GetSubType() != ECostumeSubTypes.COSTUME_HAIR and item2.GetSubType() != ECostumeSubTypes.COSTUME_WEAPON:
                                return LGEMiscellaneous.DEFINECONSTANTS.false

                            if item2.GetAttributeSetIndex() == -1:
                                ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("CHANGE_ATTR_CANNOT_CHANGE_THIS_ITEM"))
                                return LGEMiscellaneous.DEFINECONSTANTS.false

                            if item2.GetAttributeCount() == 0:
                                ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("CHANGE_ATTR_NO_CHANGE_POSSIBLE"))
                                return LGEMiscellaneous.DEFINECONSTANTS.false

                            item2.ChangeAttribute(NULL)
                            item.SetCount(item.GetCount() - 1)

                    elif item.GetSubType() == EUseSubTypes.USE_RESET_COSTUME_ATTR:
                            if item2.GetType() != EItemTypes.ITEM_COSTUME:
                                return LGEMiscellaneous.DEFINECONSTANTS.false

                            if item2.GetSubType() != ECostumeSubTypes.COSTUME_BODY and item2.GetSubType() != ECostumeSubTypes.COSTUME_HAIR and item2.GetSubType() != ECostumeSubTypes.COSTUME_WEAPON:
                                return LGEMiscellaneous.DEFINECONSTANTS.false

                            if item2.GetAttributeSetIndex() == -1:
                                ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("CHANGE_ATTR_CANNOT_CHANGE_THIS_ITEM"))
                                return LGEMiscellaneous.DEFINECONSTANTS.false

                            item2.ClearAttribute()
                            item2.AlterToMagicItem(number(40, 50), number(10, 15))
                            item.SetCount(item.GetCount() - 1)

                    elif item.GetSubType() == EUseSubTypes.USE_CHANGE_ATTRIBUTE:
                        if item2.GetAttributeSetIndex() == -1:
                            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You cannot change the bonus of this Item."))
                            return LGEMiscellaneous.DEFINECONSTANTS.false

                        if item2.GetAttributeCount() == 0:
                            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You have no upgrade you could possibly change."))
                            return LGEMiscellaneous.DEFINECONSTANTS.false

                        if item.GetSubType() == EUseSubTypes.USE_CHANGE_ATTRIBUTE2:
                            aiChangeProb = [0, 0, 30, 40, 3] + [0 for _ in range(EItemMisc.ITEM_ATTRIBUTE_MAX_LEVEL - 5)]

                            item2.ChangeAttribute(aiChangeProb)
                        elif item.GetVnum() == 76014:
                            aiChangeProb = [0, 10, 50, 39, 1] + [0 for _ in range(EItemMisc.ITEM_ATTRIBUTE_MAX_LEVEL - 5)]

                            item2.ChangeAttribute(aiChangeProb)
                        else:
                            if item.GetVnum() == 71151 or item.GetVnum() == 76023:
                                if (item2.GetType() == EItemTypes.ITEM_WEAPON) or (item2.GetType() == EItemTypes.ITEM_ARMOR and item2.GetSubType() == EArmorSubTypes.ARMOR_BODY):
                                    bCanUse = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
                                    i = 0
                                    while i < EItemMisc.ITEM_LIMIT_MAX_NUM:
                                        if item2.GetLimitType(uint(i)) == ELimitTypes.LIMIT_LEVEL and item2.GetLimitValue(uint(i)) > 40:
                                            bCanUse = LGEMiscellaneous.DEFINECONSTANTS.false
                                            break
                                        i += 1
                                    if LGEMiscellaneous.DEFINECONSTANTS.false == bCanUse:
                                        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("This item can only be used on weapons or armor up to level 40."))
                                        break
                                else:
                                    ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("This item cannot be used on accesories."))
                                    break

                            if item.GetVnum() == 71052:
                                if item2.ChangeRareAttribute() == ((not LGEMiscellaneous.DEFINECONSTANTS.false)):
                                    item.SetCount(item.GetCount() - 1)
                            else:
                                item2.ChangeAttribute(NULL)
                                item.SetCount(item.GetCount() - 1)

                        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You changed the item bonus."))

                    elif item.GetSubType() == EUseSubTypes.USE_ADD_ATTRIBUTE:
                        if item2.GetAttributeSetIndex() == -1:
                            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You cannot change the bonus of this Item."))
                            return LGEMiscellaneous.DEFINECONSTANTS.false

                        if item.GetVnum() == 71051:
                            if item2.AddRareAttribute() == ((not LGEMiscellaneous.DEFINECONSTANTS.false)):
                                ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Enhancement successfully added."))
                                item.SetCount(item.GetCount() - 1)
                        elif item2.GetAttributeCount() < 4:
                            if item.GetVnum() == 71152 or item.GetVnum() == 76024:
                                if (item2.GetType() == EItemTypes.ITEM_WEAPON) or (item2.GetType() == EItemTypes.ITEM_ARMOR and item2.GetSubType() == EArmorSubTypes.ARMOR_BODY):
                                    bCanUse = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
                                    i = 0
                                    while i < EItemMisc.ITEM_LIMIT_MAX_NUM:
                                        if item2.GetLimitType(uint(i)) == ELimitTypes.LIMIT_LEVEL and item2.GetLimitValue(uint(i)) > 40:
                                            bCanUse = LGEMiscellaneous.DEFINECONSTANTS.false
                                            break
                                        i += 1
                                    if LGEMiscellaneous.DEFINECONSTANTS.false == bCanUse:
                                        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("This item can only be used on weapons or armor up to level 40."))
                                        break
                                else:
                                    ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("This item cannot be used on accesories."))
                                    break

                            if number(1, 100) <= aiItemAttributeAddPercent[item2.GetAttributeCount()]:
                                item2.AddAttribute()
                                ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Enhancement successfully added."))

                                iAddedIdx = item2.GetAttributeCount() - 1
                            else:
                                ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Enhancement could not be added."))

                            item.SetCount(item.GetCount() - 1)
                        else:
                            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You cannot add any more attributes by using this item."))

                    elif item.GetSubType() == EUseSubTypes.USE_ADD_ATTRIBUTE2:
                        if item2.GetAttributeSetIndex() == -1:
                            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You cannot change the bonus of this Item."))
                            return LGEMiscellaneous.DEFINECONSTANTS.false

                        if item2.GetAttributeCount() == 4:
                            if number(1, 100) <= aiItemAttributeAddPercent[item2.GetAttributeCount()]:
                                item2.AddAttribute()
                                ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Enhancement successfully added."))

                                iAddedIdx = item2.GetAttributeCount() - 1
                            else:
                                ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Enhancement could not be added."))

                            item.SetCount(item.GetCount() - 1)
                        elif item2.GetAttributeCount() == 5:
                            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You cannot use this Item for other Upgrades."))
                        elif item2.GetAttributeCount() < 4:
                            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Please use the Advancement Scroll to add another Upgrade."))
                        else:
                            #lani_err("ADD_ATTRIBUTE2 : Item has wrong AttributeCount(%d)", item2.GetAttributeCount())

                    elif item.GetSubType() == EUseSubTypes.USE_ADD_ACCESSORY_SOCKET:
                            buf = str(['\0' for _ in range(21)])
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                            snprintf(buf, sizeof(buf), "%u", item2.GetID())

                            if item2.IsAccessoryForSocket():
                                if item2.GetAccessorySocketMaxGrade() < ITEM_ACCESSORY_SOCKET_MAX_NUM:
                                    if number(1, 100) <= 50:
                                        item2.SetAccessorySocketMaxGrade(item2.GetAccessorySocketMaxGrade() + 1)
                                        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Socket successfully added."))
                                    else:
                                        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Socket could not be added."))

                                    item.SetCount(item.GetCount() - 1)
                                else:
                                    ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You cannot add more Sockets here."))
                            else:
                                ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You cannot attach a socket into this Item."))

                    elif (item.GetSubType() == EUseSubTypes.USE_PUT_INTO_BELT_SOCKET) or (item.GetSubType() == EUseSubTypes.USE_PUT_INTO_ACCESSORY_SOCKET):
                        if item2.IsAccessoryForSocket() and item.CanPutInto(item2):

                            if item2.GetAccessorySocketGrade() < item2.GetAccessorySocketMaxGrade():
                                if number(1, 100) <= aiAccessorySocketPutPct[item2.GetAccessorySocketGrade()]:
                                    item2.SetAccessorySocketGrade(item2.GetAccessorySocketGrade() + 1)
                                    ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Arming successful."))
                                else:
                                    ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Arming failed."))

                                item.SetCount(item.GetCount() - 1)
                            else:
                                if item2.GetAccessorySocketMaxGrade() == 0:
                                    ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You have to use a Diamond before you can add a Socket."))
                                elif item2.GetAccessorySocketMaxGrade() < ITEM_ACCESSORY_SOCKET_MAX_NUM:
                                    ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Here is no Socket with Gems."))
                                    ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You have to add a Socket if you want to use a Diamond."))
                                else:
                                    ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Here no more Gems can be added."))
                        else:
                            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("This Item cannot be equipped."))
                    if item2.IsEquipped():
                        BuffOnAttr_AddBuffsFromItem(item2)

            elif (item.GetSubType() == EUseSubTypes.USE_PUT_INTO_BELT_SOCKET) or (item.GetSubType() == EUseSubTypes.USE_PUT_INTO_RING_SOCKET) or (item.GetSubType() == EUseSubTypes.USE_PUT_INTO_ACCESSORY_SOCKET) or (item.GetSubType() == EUseSubTypes.USE_ADD_ACCESSORY_SOCKET) or (item.GetSubType() == EUseSubTypes.USE_CLEAN_SOCKET) or (item.GetSubType() == EUseSubTypes.USE_CHANGE_COSTUME_ATTR) or (item.GetSubType() == EUseSubTypes.USE_RESET_COSTUME_ATTR) or (item.GetSubType() == EUseSubTypes.USE_CHANGE_ATTRIBUTE) or (item.GetSubType() == EUseSubTypes.USE_CHANGE_ATTRIBUTE2) or (item.GetSubType() == EUseSubTypes.USE_ADD_ATTRIBUTE) or (item.GetSubType() == EUseSubTypes.USE_ADD_ATTRIBUTE2) or (item.GetSubType() == EUseSubTypes.USE_BAIT):

                    if m_pkFishingEvent:
                        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You cannot change the Bait while fishing."))
                        return LGEMiscellaneous.DEFINECONSTANTS.false

                    weapon = GetWear(EWearPositions.WEAR_WEAPON)

                    if weapon is None or weapon.GetType() != EItemTypes.ITEM_ROD:
                        return LGEMiscellaneous.DEFINECONSTANTS.false

                    if weapon.GetSocket(2) != 0:
                        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You exchange the current Bait with %s."), item.GetName(LOCALE_LANIATUS))
                    else:
                        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Stick the %s Bait to the Hook."), item.GetName(LOCALE_LANIATUS))

                    weapon.SetSocket(2, item.GetValue(0), ((not DefineConstants.false)))
                    item.SetCount(item.GetCount() - 1)

            elif (item.GetSubType() == EUseSubTypes.USE_MOVE) or (item.GetSubType() == EUseSubTypes.USE_TREASURE_BOX) or (item.GetSubType() == EUseSubTypes.USE_MONEYBAG):
                pass

            elif item.GetSubType() == EUseSubTypes.USE_AFFECT:
                    if not IsLoadedAffect():
                        return LGEMiscellaneous.DEFINECONSTANTS.false

                    if FindAffect(item.GetValue(0), aApplyInfo[item.GetValue(1)].bPointType):
                        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("The effect is already working."))
                    else:
                        AddAffect(item.GetValue(0), aApplyInfo[item.GetValue(1)].bPointType, item.GetValue(2), 0, item.GetValue(3), 0, LGEMiscellaneous.DEFINECONSTANTS.false)
                        item.SetCount(item.GetCount() - 1)

            elif item.GetSubType() == EUseSubTypes.USE_CREATE_STONE:
                AutoGiveItem(number(28000, 28013))
                item.SetCount(item.GetCount() - 1)

            elif item.GetSubType() == EUseSubTypes.USE_RECIPE:
                    pSource1 = FindSpecifyItem(item.GetValue(1))
                    dwSourceCount1 = uint(item.GetValue(2))

                    pSource2 = FindSpecifyItem(item.GetValue(3))
                    dwSourceCount2 = uint(item.GetValue(4))

                    if dwSourceCount1 != 0:
                        if pSource1 is None:
                            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Not enough ingrediant to creat the potion."))
                            return LGEMiscellaneous.DEFINECONSTANTS.false

                    if dwSourceCount2 != 0:
                        if pSource2 is None:
                            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Not enough ingrediant to creat the potion."))
                            return LGEMiscellaneous.DEFINECONSTANTS.false

                    if pSource1 is not None:
                        if pSource1.GetCount() < dwSourceCount1:
                            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Not enough ingredient(%s)."), pSource1.GetName(LOCALE_LANIATUS))
                            return LGEMiscellaneous.DEFINECONSTANTS.false

                        pSource1.SetCount(pSource1.GetCount() - dwSourceCount1)

                    if pSource2 is not None:
                        if pSource2.GetCount() < dwSourceCount2:
                            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Not enough ingredient(%s)."), pSource2.GetName(LOCALE_LANIATUS))
                            return LGEMiscellaneous.DEFINECONSTANTS.false

                        pSource2.SetCount(pSource2.GetCount() - dwSourceCount2)

                    pBottle = FindSpecifyItem(50901)

                    if pBottle is None or pBottle.GetCount() < 1:
                        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Not enough empty bottles."))
                        return LGEMiscellaneous.DEFINECONSTANTS.false

                    pBottle.SetCount(pBottle.GetCount() - 1)

                    if number(1, 100) > item.GetValue(5):
                        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Failed to create the potion."))
                        return LGEMiscellaneous.DEFINECONSTANTS.false

                    AutoGiveItem(item.GetValue(0))

            elif item.GetSubType() == EUseSubTypes.USE_CLEAR_ACCE:
                    pDestItem = GetItem(DestCell)
                    if None is pDestItem:
                        return LGEMiscellaneous.DEFINECONSTANTS.false

                    if pDestItem.IsEquipped():
                        return LGEMiscellaneous.DEFINECONSTANTS.false

                    if pDestItem.GetSocket(1) == 0:
                        return LGEMiscellaneous.DEFINECONSTANTS.false

                    pDestItem.ClearAttribute()
                    pDestItem.SetSocket(1, 0, ((not DefineConstants.false)))
                    item.SetCount(item.GetCount() - 1)

    elif (item.GetType() == EItemTypes.ITEM_USE) or (item.GetType() == EItemTypes.ITEM_METIN):
            item2 = None

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if (!IsValidItemPosition(DestCell) || !(item2 = GetItem(DestCell)))
            if (not IsValidItemPosition(DestCell)) or not(item2 = GetItem(DestCell)):
                return LGEMiscellaneous.DEFINECONSTANTS.false

            if item2.IsExchanging():
                return LGEMiscellaneous.DEFINECONSTANTS.false

            if item2.GetType() == EItemTypes.ITEM_PICK:
                return LGEMiscellaneous.DEFINECONSTANTS.false
            if item2.GetType() == EItemTypes.ITEM_ROD:
                return LGEMiscellaneous.DEFINECONSTANTS.false

            i = None

            i = 0
            while i < EItemMisc.LG_ITEM_SOCKET_MAX_NUM:
                dwVnum = None

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((dwVnum = item2->GetSocket(i)) <= 2)
                if (dwVnum = uint(item2.GetSocket(i))) <= 2:
                    continue

                p = ITEM_MANAGER.instance().GetTable(dwVnum)

                if p is None:
                    continue

                if item.GetValue(5) == p.alValues[5]:
                    ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You cannot attach several Spirit Stones of the same kind."))
                    return LGEMiscellaneous.DEFINECONSTANTS.false
                i += 1

            if item2.GetType() == EItemTypes.ITEM_ARMOR:
                ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'IS_SET' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
                if (not IS_SET(item.GetWearFlag(), EItemWearableFlag.WEARABLE_BODY)) or not IS_SET(item2.GetWearFlag(), EItemWearableFlag.WEARABLE_BODY):
                    ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You cannot attach this Stone there."))
                    return LGEMiscellaneous.DEFINECONSTANTS.false
            elif item2.GetType() == EItemTypes.ITEM_WEAPON:
                ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'IS_SET' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
                if not IS_SET(item.GetWearFlag(), EItemWearableFlag.WEARABLE_WEAPON):
                    ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You cannot attach this Stone to a Weapon."))
                    return LGEMiscellaneous.DEFINECONSTANTS.false
            else:
                ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("No slot free."))
                return LGEMiscellaneous.DEFINECONSTANTS.false

            i = 0
            while i < EItemMisc.LG_ITEM_SOCKET_MAX_NUM:
                if item2.GetSocket(i) >= 1 and item2.GetSocket(i) <= 2 and item2.GetSocket(i) >= item.GetValue(2):
                    if number(1, 100) <= 30:
                        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You attached the Stone successfully."))
                        item2.SetSocket(i, int(item.GetVnum()), ((not DefineConstants.false)))
                    else:
                        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You did not attach the Stone."))
                        item2.SetSocket(i, ITEM_BROKEN_METIN_VNUM, ((not DefineConstants.false)))

                    ITEM_MANAGER.instance().RemoveItem(item, "REMOVE (METIN)")
                    break
                i += 1

            if i == EItemMisc.LG_ITEM_SOCKET_MAX_NUM:
                ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("No slot free."))

    elif (item.GetType() == EItemTypes.ITEM_AUTOUSE) or (item.GetType() == EItemTypes.ITEM_MATERIAL) or (item.GetType() == EItemTypes.ITEM_SPECIAL) or (item.GetType() == EItemTypes.ITEM_TOOL) or (item.GetType() == EItemTypes.ITEM_LOTTERY):
        pass

    elif item.GetType() == EItemTypes.ITEM_TOTEM:
            if not item.IsEquipped():
                EquipItem(item)

    elif item.GetType() == EItemTypes.ITEM_BLEND:
        #sys_log(0,"ITEM_BLEND!!")
        if Blend_Item_find(item.GetVnum()):
            affect_type = LaniatusEAffectTypes.LANIA_AFFECT_BLEND
            if item.GetSocket(0) >= _countof(aApplyInfo):
                #lani_err("INVALID BLEND ITEM(id : %d, vnum : %d). APPLY TYPE IS %d.", item.GetID(), item.GetVnum(), item.GetSocket(0))
                return LGEMiscellaneous.DEFINECONSTANTS.false
            apply_type = aApplyInfo[item.GetSocket(0)].bPointType
            apply_value = item.GetSocket(1)
            apply_duration = item.GetSocket(2)

            if FindAffect(affect_type, apply_type):
                ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("The effect is already working."))
            else:
                if FindAffect(LaniatusEAffectTypes.LANIA_AFFECT_EXP_BONUS_EURO_FREE, EPointTypes.LG_POINT_RESIST_MAGIC):
                    ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("The effect is already working."))
                else:
                    AddAffect(affect_type, apply_type, apply_value, 0, apply_duration, 0, LGEMiscellaneous.DEFINECONSTANTS.false)
                    item.SetCount(item.GetCount() - 1)
    elif item.GetType() == EItemTypes.ITEM_EXTRACT:
            pDestItem = GetItem(DestCell)
            if None is pDestItem:
                return LGEMiscellaneous.DEFINECONSTANTS.false
            if item.GetSubType() == EExtractSubTypes.EXTRACT_DRAGON_SOUL:
                if pDestItem.IsDragonSoul():
                    temp_ref_pDestItem = RefObject(pDestItem);
                    tempVar2 = DSManager.instance().PullOut(self, NPOS, temp_ref_pDestItem, item)
                    pDestItem = temp_ref_pDestItem.arg_value
                    return tempVar2
                return LGEMiscellaneous.DEFINECONSTANTS.false
            if (item.GetSubType() == EExtractSubTypes.EXTRACT_DRAGON_SOUL) or (item.GetSubType() == EExtractSubTypes.EXTRACT_DRAGON_HEART):
                if pDestItem.IsDragonSoul():
                    return DSManager.instance().ExtractDragonHeart(self, pDestItem, item)
                return LGEMiscellaneous.DEFINECONSTANTS.false

            if True:
                return LGEMiscellaneous.DEFINECONSTANTS.false

    elif (item.GetType() == EItemTypes.ITEM_EXTRACT) or (item.GetType() == EItemTypes.ITEM_NONE):
        #lani_err("Item type NONE %s", item.GetName(LOCALE_LANIATUS))

    else:
        #sys_log(0, "UseItemEx: Unknown type %s %d", item.GetName(LOCALE_LANIATUS), item.GetType())
        return LGEMiscellaneous.DEFINECONSTANTS.false

    return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

def UseItem(Cell, DestCell):
    wCell = Cell.cell
    window_type = Cell.window_type
    wDestCell = DestCell.cell
    bDestInven = DestCell.window_type
    item = None

    if not CanHandleItem():
        return LGEMiscellaneous.DEFINECONSTANTS.false

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if (!IsValidItemPosition(Cell) || !(item = GetItem(Cell)))
    if (not IsValidItemPosition(Cell)) or not(item = GetItem(Cell)):
        return LGEMiscellaneous.DEFINECONSTANTS.false

    #sys_log(0, "%s: USE_ITEM %s (inven %d, cell: %d)", GetName(), item.GetName(LOCALE_LANIATUS), window_type, wCell)

    if item.IsExchanging():
        return LGEMiscellaneous.DEFINECONSTANTS.false

    if not item.CanUsedBy(self):
        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Your character class can not use this item."))
        return LGEMiscellaneous.DEFINECONSTANTS.false

    if IsStun():
        return LGEMiscellaneous.DEFINECONSTANTS.false

    if LGEMiscellaneous.DEFINECONSTANTS.false == FN_check_item_sex(self, item):
        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("This Item can be used by the other gender only."))
        return LGEMiscellaneous.DEFINECONSTANTS.false

    if IS_SUMMON_ITEM(int(item.GetVnum())):
        if LGEMiscellaneous.DEFINECONSTANTS.false == IS_SUMMONABLE_ZONE(GetMapIndex()):
            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Cannot be used"))
            return LGEMiscellaneous.DEFINECONSTANTS.false

        iPulse = thecore_pulse()

        if iPulse - GetSafeboxLoadTime() < ((g_nPortalLimitTime) * passes_per_sec):
            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You cannot use for %d seconds after opening a Warehouse any Return Scroll."), g_nPortalLimitTime)

            if test_server:
                ChatPacket(EChatType.CHAT_TYPE_INFO, "[TestOnly]Pulse %d LoadTime %d PASS %d", iPulse, GetSafeboxLoadTime(), ((g_nPortalLimitTime) * passes_per_sec))
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if GetExchange() or GetMyShop() or GetShopOwner() or IsOpenSafebox() or IsCubeOpen() or IsAcceWindowOpen():
            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You cannot use the Return Scroll as long as you have opened another window."))
            return LGEMiscellaneous.DEFINECONSTANTS.false

            if iPulse - GetRefineTime() < ((g_nPortalLimitTime) * passes_per_sec):
                ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You cannot teleport for %d seconds after a trade."), g_nPortalLimitTime)
                return LGEMiscellaneous.DEFINECONSTANTS.false

            if iPulse - GetMyShopTime() < ((g_nPortalLimitTime) * passes_per_sec):
                ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You cannot use a Return Scroll %d seconds after opening a Warehouse."), g_nPortalLimitTime)
                return LGEMiscellaneous.DEFINECONSTANTS.false


        if item.GetVnum() != 70302:
            posWarp = pixel_position_s()

            x = 0
            y = 0

            nDist = 0
            NDISTANT = 5000.0

            if item.GetVnum() == 22010:
                x = item.GetSocket(0) - GetX()
                y = item.GetSocket(1) - GetY()
            elif item.GetVnum() == 22000:
                SECTREE_MANAGER.instance().GetRecallPositionByEmpire(GetMapIndex(), GetEmpire(), posWarp)

                if item.GetSocket(0) == 0:
                    x = posWarp.x - GetX()
                    y = posWarp.y - GetY()
                else:
                    x = item.GetSocket(0) - GetX()
                    y = item.GetSocket(1) - GetY()

            nDist = math.sqrt(float(x) ** 2 + float(y) ** 2)

            if NDISTANT > nDist:
                ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You cannot use the Return Scroll because the distance is too small."))
                if test_server:
                    ChatPacket(EChatType.CHAT_TYPE_INFO, "PossibleDistant %f nNowDist %f", NDISTANT,nDist)
                return LGEMiscellaneous.DEFINECONSTANTS.false

        if iPulse - GetExchangeTime() < ((g_nPortalLimitTime) * passes_per_sec):
            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("After a trade you cannot use a Return Scroll for %d seconds."), g_nPortalLimitTime)
            return LGEMiscellaneous.DEFINECONSTANTS.false

    if item.GetVnum() == 50200 or item.GetVnum() == 71049:
        if GetExchange() or GetMyShop() or GetShopOwner() or IsOpenSafebox() or IsCubeOpen() or IsAcceWindowOpen():
            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You cannot open a storage if another Window is already open."))
            return LGEMiscellaneous.DEFINECONSTANTS.false


    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'IS_SET' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
    if IS_SET(item.GetFlag(), EItemFlag.ITEM_FLAG_LOG):
        vid = item.GetVID()
        oldCount = item.GetCount()
        vnum = item.GetVnum()

        hint = str(['\0' for _ in range((int)EItemMisc.ITEM_NAME_MAX_LEN + 32 + 1)])
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        len = snprintf(hint, sizeof(hint) - 32, "%s", item.GetName(LOCALE_LANIATUS))

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        if len < 0 or len >= int(sizeof(hint)) - 32:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            len = (sizeof(hint) - 32) - 1

        ret = UseItemEx(item, DestCell)

        return (ret)
    else:
        return UseItemEx(item, DestCell)

def DestroyItem(Cell):
    if m_iLastItemDestroyPulse > thecore_pulse():
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        deltaInSeconds = ((m_iLastItemDestroyPulse / ((1) * passes_per_sec)) - (thecore_pulse() / ((1) * passes_per_sec)))

        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You can destroy another item in: %d seconds!"), deltaInSeconds)
        return LGEMiscellaneous.DEFINECONSTANTS.false

    item = None

    if not CanHandleItem():
        if None != DragonSoul_RefineWindow_GetOpener():
            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You cannot move the item within the refinement window."))
        return LGEMiscellaneous.DEFINECONSTANTS.false

    if IsDead():
        return LGEMiscellaneous.DEFINECONSTANTS.false

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if (!IsValidItemPosition(Cell) || !(item = GetItem(Cell)))
    if (not IsValidItemPosition(Cell)) or not(item = GetItem(Cell)):
        return LGEMiscellaneous.DEFINECONSTANTS.false

    if item.IsExchanging():
        return LGEMiscellaneous.DEFINECONSTANTS.false

    if ((not LGEMiscellaneous.DEFINECONSTANTS.false)) == item.isLocked():
        return LGEMiscellaneous.DEFINECONSTANTS.false

    if quest.CQuestManager.instance().GetPCForce(GetPlayerID()).IsRunning() == ((not LGEMiscellaneous.DEFINECONSTANTS.false)):
        return LGEMiscellaneous.DEFINECONSTANTS.false

    if item.GetCount() <= 0:
        return LGEMiscellaneous.DEFINECONSTANTS.false

    SyncQuickslot(LG_QUICKSLOT_TYPE_ITEM, Cell.cell, 255)

    ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You have destroyed: %s"), item.GetName(LOCALE_LANIATUS))

    ITEM_MANAGER.instance().RemoveItem(item, NULL)
    m_iLastItemDestroyPulse = thecore_pulse() + ((1) * passes_per_sec)

    return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

def DropItem(Cell, wCount):
    item = None

    if not CanHandleItem():
        if None != DragonSoul_RefineWindow_GetOpener():
            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You cannot move the item within the refinement window."))
        return LGEMiscellaneous.DEFINECONSTANTS.false

    if IsDead():
        return LGEMiscellaneous.DEFINECONSTANTS.false

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if (!IsValidItemPosition(Cell) || !(item = GetItem(Cell)))
    if (not IsValidItemPosition(Cell)) or not(item = GetItem(Cell)):
        return LGEMiscellaneous.DEFINECONSTANTS.false

    if item.IsExchanging():
        return LGEMiscellaneous.DEFINECONSTANTS.false

    if ((not LGEMiscellaneous.DEFINECONSTANTS.false)) == item.isLocked():
        return LGEMiscellaneous.DEFINECONSTANTS.false

    if quest.CQuestManager.instance().GetPCForce(GetPlayerID()).IsRunning() == ((not LGEMiscellaneous.DEFINECONSTANTS.false)):
        return LGEMiscellaneous.DEFINECONSTANTS.false

    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'IS_SET' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
    if IS_SET(item.GetAntiFlag(), LaniatusEITMAntiFlagDcs.ITEM_ANTIFLAG_DROP | LaniatusEITMAntiFlagDcs.ITEM_ANTIFLAG_GIVE):
        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You cannot drop this Item."))
        return LGEMiscellaneous.DEFINECONSTANTS.false

    if wCount == 0 or wCount > item.GetCount():
        wCount = ushort(item.GetCount())

    SyncQuickslot(LG_QUICKSLOT_TYPE_ITEM, Cell.cell, 255)

    pkItemToDrop = None

    if wCount == item.GetCount():
        item.RemoveFromCharacter()
        pkItemToDrop = item
    else:
        if wCount == 0:
            if test_server:
                #sys_log(0, "[DROP_ITEM] drop item count == 0")
            return LGEMiscellaneous.DEFINECONSTANTS.false

        item.SetCount(item.GetCount() - wCount)
        ITEM_MANAGER.instance().FlushDelayedSave(item)

        pkItemToDrop = ITEM_MANAGER.instance().CreateItem(item.GetVnum(), wCount, 0, DefineConstants.false, -1, DefineConstants.false)

        FN_copy_LG_ITEM_SOCKET(pkItemToDrop, item)

    pxPos = GetXYZ()

    if pkItemToDrop.AddToGround(GetMapIndex(), pxPos, DefineConstants.false):
        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("The dropped Item will vanish in 3 minutes."))
        pkItemToDrop.StartDestroyEvent(5)

        ITEM_MANAGER.instance().FlushDelayedSave(pkItemToDrop)

    return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

def DropGold(gold):
    ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You can't drop gold."))
    return LGEMiscellaneous.DEFINECONSTANTS.false

def MoveItem(Cell, DestCell, count):
    item = None

    if not IsValidItemPosition(Cell):
        return LGEMiscellaneous.DEFINECONSTANTS.false

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if (!(item = GetItem(Cell)))
    if not(item = GetItem(Cell)):
        return LGEMiscellaneous.DEFINECONSTANTS.false

    if item.IsExchanging():
        return LGEMiscellaneous.DEFINECONSTANTS.false

    if item.GetCount() < count:
        return LGEMiscellaneous.DEFINECONSTANTS.false

    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'IS_SET' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
    if EWindows.INVENTORY == Cell.window_type and Cell.cell >= LGEMiscellaneous.INVENTORY_MAX_NUM and IS_SET(item.GetFlag(), EItemFlag.ITEM_FLAG_IRREMOVABLE):
        return LGEMiscellaneous.DEFINECONSTANTS.false

    if ((not LGEMiscellaneous.DEFINECONSTANTS.false)) == item.isLocked():
        return LGEMiscellaneous.DEFINECONSTANTS.false

    if not IsValidItemPosition(DestCell):
        return LGEMiscellaneous.DEFINECONSTANTS.false

    if not CanHandleItem():
        if None != DragonSoul_RefineWindow_GetOpener():
            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You cannot move the item within the refinement window."))
        return LGEMiscellaneous.DEFINECONSTANTS.false

    if DestCell.IsBeltInventoryPosition() and LGEMiscellaneous.DEFINECONSTANTS.false == CBeltInventoryHelper.CanMoveIntoBeltInventory(item):
        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You cannot equip this item in your belt inventory."))
        return LGEMiscellaneous.DEFINECONSTANTS.false

    if Cell.IsEquipPosition() and not CanUnequipNow(item):
        return LGEMiscellaneous.DEFINECONSTANTS.false

    if DestCell.IsEquipPosition():
        if GetItem(DestCell):
            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You have already equipped this kind of Dragon Stone."))

            return LGEMiscellaneous.DEFINECONSTANTS.false

        EquipItem(item, DestCell.cell - LGEMiscellaneous.INVENTORY_MAX_NUM)
    else:
        if item.IsDragonSoul():
            if item.IsEquipped():
                temp_ref_item = RefObject(item);
                tempVar = DSManager.instance().PullOut(self, TItemPos(DestCell), temp_ref_item, NULL)
                item = temp_ref_item.arg_value
                return tempVar
            else:
                if DestCell.window_type != EWindows.DRAGON_SOUL_INVENTORY:
                    return LGEMiscellaneous.DEFINECONSTANTS.false

                if not DSManager.instance().IsValidCellForThisItem(item, DestCell):
                    return LGEMiscellaneous.DEFINECONSTANTS.false

        elif EWindows.DRAGON_SOUL_INVENTORY == DestCell.window_type:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        item2 = None

        ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'IS_SET' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
        ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'IS_SET' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((item2 = GetItem(DestCell)) && item != item2 && item2->IsStackable() && !IS_SET(item2->GetAntiFlag(), ITEM_ANTIFLAG_STACK) && item2->GetVnum() == item->GetVnum())
        if (item2 = GetItem(DestCell)) and item is not item2 and item2.IsStackable() and (not IS_SET(item2.GetAntiFlag(), LaniatusEITMAntiFlagDcs.ITEM_ANTIFLAG_STACK)) and item2.GetVnum() == item.GetVnum():
            i = 0
            while i < EItemMisc.LG_ITEM_SOCKET_MAX_NUM:
                if item2.GetSocket(i) != item.GetSocket(i):
                    return LGEMiscellaneous.DEFINECONSTANTS.false
                i += 1

            if count == 0:
                count = ushort(item.GetCount())

            #sys_log(0, "%s: ITEM_STACK %s (window: %d, cell : %d) -> (window:%d, cell %d) count %d", GetName(), item.GetName(LOCALE_LANIATUS), Cell.window_type, Cell.cell, DestCell.window_type, DestCell.cell, count)

            count = MIN(EItemMisc.ITEM_MAX_COUNT - item2.GetCount(), count)

            item.SetCount(item.GetCount() - count)
            item2.SetCount(item2.GetCount() + count)
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        if not IsEmptyItemGrid(DestCell, item.GetSize(), Cell.cell):
            return LGEMiscellaneous.DEFINECONSTANTS.false

        ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'IS_SET' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
        if count == 0 or count >= item.GetCount() or (not item.IsStackable()) or IS_SET(item.GetAntiFlag(), LaniatusEITMAntiFlagDcs.ITEM_ANTIFLAG_STACK):
            #sys_log(0, "%s: ITEM_MOVE %s (window: %d, cell : %d) -> (window:%d, cell %d) count %d", GetName(), item.GetName(LOCALE_LANIATUS), Cell.window_type, Cell.cell, DestCell.window_type, DestCell.cell, count)

            item.RemoveFromCharacter()
            SetItem(DestCell, item)

            if EWindows.INVENTORY == Cell.window_type and EWindows.INVENTORY == DestCell.window_type:
                SyncQuickslot(LG_QUICKSLOT_TYPE_ITEM, Cell.cell, DestCell.cell)
        elif count < item.GetCount():
            #sys_log(0, "%s: ITEM_SPLIT %s (window: %d, cell : %d) -> (window:%d, cell %d) count %d", GetName(), item.GetName(LOCALE_LANIATUS), Cell.window_type, Cell.cell, DestCell.window_type, DestCell.cell, count)

            item.SetCount(item.GetCount() - count)
            item2 = ITEM_MANAGER.instance().CreateItem(item.GetVnum(), count, 0, DefineConstants.false, -1, DefineConstants.false)

            FN_copy_LG_ITEM_SOCKET(item2, item)

            item2.AddToCharacter(self, TItemPos(DestCell))

    if DestCell.IsDefaultInventoryPosition() and Cell.IsEquipPosition():

        if item.IsCostumeMountItem() and GetHorse():
            HorseSummon(LGEMiscellaneous.DEFINECONSTANTS.false)

        if item.IsCostumePetItem() and GetPetSystem():
            GetPetSystem().HandlePetCostumeItem()

    return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

class NPartyPickupDistribute: #this class replaces the original namespace 'NPartyPickupDistribute'
    class FFindOwnership:

        def __init__(self, item):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.item = []
            self.owner = None

            self.item = CItem(item)
            self.owner = None

        def functor_method(self, ch):
            if self.item.IsOwnership(ch):
                self.owner = ch

    class FCountNearMember:

        def __init__(self, center):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.total = 0
            self.x = 0
            self.y = 0

            self.total = 0
            self.x = center.GetX()
            self.y = center.GetY()

        def functor_method(self, ch):
            if Globals.DISTANCE_APPROX(ch.GetX() - self.x, ch.GetY() - self.y) <= Globals.PARTY_DEFAULT_RANGE:
                self.total += 1

    class FMoneyDistributor:

        def __init__(self, center, iMoney):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.total = 0
            self.c = []
            self.x = 0
            self.y = 0
            self.iMoney = 0

            self.total = 0
            self.c = CHARACTER(center)
            self.x = center.GetX()
            self.y = center.GetY()
            self.iMoney = iMoney

        def functor_method(self, ch):
            if ch is not self.c:
                if Globals.DISTANCE_APPROX(ch.GetX() - self.x, ch.GetY() - self.y) <= Globals.PARTY_DEFAULT_RANGE:
                    ch.PointChange(EPointTypes.LG_POINT_GOLD, self.iMoney, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), DefineConstants.false)

def GiveGold(iAmount):
    if iAmount <= 0:
        return

    #sys_log(0, "GIVE_GOLD: %s %d", GetName(), iAmount)

    if GetParty():
        pParty = GetParty()

        lldTotal = iAmount
        lldMyAmount = lldTotal

        funcCountNearMember = NPartyPickupDistribute.FCountNearMember(self)
        pParty.ForEachOnlineMember(funcCountNearMember.functor_method)

        if funcCountNearMember.total > 1:
            dwShare = math.trunc(lldTotal / float(funcCountNearMember.total))
            lldMyAmount -= dwShare * (funcCountNearMember.total - 1)

            funcMoneyDist = NPartyPickupDistribute.FMoneyDistributor(self, int(dwShare))

            pParty.ForEachOnlineMember(funcMoneyDist.functor_method)

        PointChange(EPointTypes.LG_POINT_GOLD, lldMyAmount, ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
    else:
        PointChange(EPointTypes.LG_POINT_GOLD, iAmount, ((not LGEMiscellaneous.DEFINECONSTANTS.false)))

def PickupItem(item, dwVID):
    if item is None and dwVID != 0:
        item = ITEM_MANAGER.instance().FindByVID(dwVID)

    if IsObserverMode():
        return LGEMiscellaneous.DEFINECONSTANTS.false

    if item is None or item.GetSectree() is None:
        return LGEMiscellaneous.DEFINECONSTANTS.false

    if item.DistanceValid(self):
        if dwVID == 0 and IsPickupBlockedItem(item.GetVnum()):
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if item.IsOwnership(self):
            if item.GetType() == EItemTypes.ITEM_ELK:
                GiveGold(item.GetCount())
                item.RemoveFromGround()

                ITEM_MANAGER.instance().DestroyItem(item)

                Save()
            else:
                ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'IS_SET' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
                if item.IsStackable() and not IS_SET(item.GetAntiFlag(), LaniatusEITMAntiFlagDcs.ITEM_ANTIFLAG_STACK):
                    wCount = ushort(item.GetCount())

                    i = 0
                    while i < LGEMiscellaneous.INVENTORY_MAX_NUM:
                        item2 = GetInventoryItem(i)

                        if item2 is None:
                            continue

                        if item2.GetVnum() == item.GetVnum():
                            j = None

                            j = 0
                            while j < EItemMisc.LG_ITEM_SOCKET_MAX_NUM:
                                if item2.GetSocket(j) != item.GetSocket(j):
                                    break
                                j += 1

                            if j != EItemMisc.LG_ITEM_SOCKET_MAX_NUM:
                                continue

                            wCount2 = MIN(EItemMisc.ITEM_MAX_COUNT - item2.GetCount(), wCount)
                            wCount -= wCount2

                            item2.SetCount(item2.GetCount() + wCount2)

                            if wCount == 0:
                                if item.GetCount() > 1:
                                    ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("%dx %s received"), item.GetCount(), item2.GetName(LOCALE_LANIATUS))
                                else:
                                    ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("%s received"), item2.GetName(LOCALE_LANIATUS))

                                ITEM_MANAGER.instance().DestroyItem(item)
                                if item2.GetType() == EItemTypes.ITEM_QUEST:
                                    quest.CQuestManager.instance().PickupItem(GetPlayerID(), item2)
                                return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
                        i += 1

                    item.SetCount(wCount)

                iEmptyCell = None
                if item.IsDragonSoul():
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((iEmptyCell = GetEmptyDragonSoulInventory(item)) == -1)
                    if (iEmptyCell = GetEmptyDragonSoulInventory(item)) == -1:
                        #sys_log(0, "No empty ds inventory pid %u size %ud itemid %u", GetPlayerID(), item.GetSize(), item.GetID())
                        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You carry too many Items."))
                        return LGEMiscellaneous.DEFINECONSTANTS.false
                else:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((iEmptyCell = GetEmptyInventory(item->GetSize())) == -1)
                    if (iEmptyCell = GetEmptyInventory(item.GetSize())) == -1:
                        #sys_log(0, "No empty inventory pid %u size %ud itemid %u", GetPlayerID(), item.GetSize(), item.GetID())
                        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You carry too many Items."))
                        return LGEMiscellaneous.DEFINECONSTANTS.false

                item.RemoveFromGround()

                if item.IsDragonSoul():
                    item.AddToCharacter(self, TItemPos(EWindows.DRAGON_SOUL_INVENTORY, iEmptyCell))
                else:
                    item.AddToCharacter(self, TItemPos(EWindows.INVENTORY, iEmptyCell))

                if item.GetCount() > 1:
                    ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("%dx %s received"), item.GetCount(), item.GetName(LOCALE_LANIATUS))
                else:
                    ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("%s received"), item.GetName(LOCALE_LANIATUS))

                if item.GetType() == EItemTypes.ITEM_QUEST:
                    quest.CQuestManager.instance().PickupItem(GetPlayerID(), item)
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
        ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'IS_SET' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
        elif (not IS_SET(item.GetAntiFlag(), LaniatusEITMAntiFlagDcs.ITEM_ANTIFLAG_GIVE | LaniatusEITMAntiFlagDcs.ITEM_ANTIFLAG_DROP)) and GetParty():
            funcFindOwnership = NPartyPickupDistribute.FFindOwnership(item)
            GetParty().ForEachOnlineMember(funcFindOwnership.functor_method)
            owner = funcFindOwnership.owner

            if owner is None:
                return LGEMiscellaneous.DEFINECONSTANTS.false

            if item.IsStackable():
                iCount = int(item.GetCount())
                i = 0
                while i < LGEMiscellaneous.INVENTORY_MAX_NUM:
                    item2 = owner.GetInventoryItem(ushort(i))

                    if item2 is None:
                        continue

                    if item2.GetVnum() == item.GetVnum():
                        j = None

                        j = 0
                        while j < EItemMisc.LG_ITEM_SOCKET_MAX_NUM:
                            if item2.GetSocket(j) != item.GetSocket(j):
                                break
                            j += 1

                        if j != EItemMisc.LG_ITEM_SOCKET_MAX_NUM:
                            continue

                        wCount2 = MIN(LGEMiscellaneous.DEFINECONSTANTS.MAX_ITEM_STACK - item2.GetCount(), iCount)
                        iCount -= wCount2

                        item2.SetCount(item2.GetCount() + wCount2)

                        if iCount == 0:
                            if owner is self:
                                if item.GetCount() > 1:
                                    ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("%dx %s received"), item.GetCount(), item2.GetName(LOCALE_LANIATUS))
                                else:
                                    ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("%s received"), item2.GetName(LOCALE_LANIATUS))
                            else:
                                if item.GetCount() > 1:
                                    owner.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Received Item: %s, %dx %s "), GetName(), item.GetCount(), item2.GetName(LOCALE_LANIATUS))
                                else:
                                    owner.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Received Item: %s, %s "), GetName(), item2.GetName(LOCALE_LANIATUS))
                            ITEM_MANAGER.instance().DestroyItem(item)
                            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
                    i += 1
                item.SetCount(uint(iCount))

            iEmptyCell = None

            if item.IsDragonSoul():
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if (!(owner && (iEmptyCell = owner->GetEmptyDragonSoulInventory(item)) != -1))
                if not(owner is not None and (iEmptyCell = owner.GetEmptyDragonSoulInventory(item)) != -1):
                    owner = self

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((iEmptyCell = GetEmptyDragonSoulInventory(item)) == -1)
                    if (iEmptyCell = GetEmptyDragonSoulInventory(item)) == -1:
                        owner.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You carry too many Items."))
                        return LGEMiscellaneous.DEFINECONSTANTS.false
            else:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if (!(owner && (iEmptyCell = owner->GetEmptyInventory(item->GetSize())) != -1))
                if not(owner is not None and (iEmptyCell = owner.GetEmptyInventory(item.GetSize())) != -1):
                    owner = self

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((iEmptyCell = GetEmptyInventory(item->GetSize())) == -1)
                    if (iEmptyCell = GetEmptyInventory(item.GetSize())) == -1:
                        owner.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You carry too many Items."))
                        return LGEMiscellaneous.DEFINECONSTANTS.false

            item.RemoveFromGround()

            if item.IsDragonSoul():
                item.AddToCharacter(owner, TItemPos(EWindows.DRAGON_SOUL_INVENTORY, iEmptyCell))
            else:
                item.AddToCharacter(owner, TItemPos(EWindows.INVENTORY, iEmptyCell))

            if owner is self:
                if item.GetCount() > 1:
                    ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("%dx %s received"), item.GetCount(), item.GetName(LOCALE_LANIATUS))
                else:
                    ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("%s received"), item.GetName(LOCALE_LANIATUS))
            else:
                if item.GetCount() > 1:
                    owner.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Received Item: %s, %dx %s "), GetName(), item.GetCount(), item.GetName(LOCALE_LANIATUS))
                else:
                    owner.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Received Item: %s, %s "), GetName(), item.GetName(LOCALE_LANIATUS))

            if item.GetType() == EItemTypes.ITEM_QUEST:
                quest.CQuestManager.instance().PickupItem(owner.GetPlayerID(), item)

            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    return LGEMiscellaneous.DEFINECONSTANTS.false

def SwapItem(wCell, bDestCell):
    if not CanHandleItem():
        return LGEMiscellaneous.DEFINECONSTANTS.false

    srcCell = TItemPos(EWindows.INVENTORY, wCell)
    destCell = TItemPos(EWindows.INVENTORY, bDestCell)

    if srcCell.IsDragonSoulEquipPosition() or destCell.IsDragonSoulEquipPosition():
        return LGEMiscellaneous.DEFINECONSTANTS.false

    if wCell == bDestCell:
        return LGEMiscellaneous.DEFINECONSTANTS.false

    if srcCell.IsEquipPosition() and destCell.IsEquipPosition():
        return LGEMiscellaneous.DEFINECONSTANTS.false

    item1 = None
    item2 = None

    if srcCell.IsEquipPosition():
        item1 = GetInventoryItem(bDestCell)
        item2 = GetInventoryItem(wCell)
    else:
        item1 = GetInventoryItem(wCell)
        item2 = GetInventoryItem(bDestCell)

    if item1 is None or item2 is None:
        return LGEMiscellaneous.DEFINECONSTANTS.false

    if item1 is item2:
        #sys_log(0, "[WARNING][WARNING][HACK USER!] : %s %d %d", m_stName.c_str(), wCell, bDestCell)
        return LGEMiscellaneous.DEFINECONSTANTS.false

    if not IsEmptyItemGrid(TItemPos(EWindows.INVENTORY, item1.GetCell()), item2.GetSize(), item1.GetCell()):
        return LGEMiscellaneous.DEFINECONSTANTS.false

    if TItemPos(EWindows.EQUIPMENT, item2.GetCell()).IsEquipPosition():
        if item1.GetType() == EItemTypes.ITEM_WEAPON and item1.GetSubType() != EWeaponSubTypes.WEAPON_ARROW and item1.GetSubType() != EWeaponSubTypes.WEAPON_QUIVER:
            pkItem = GetWear(EWearPositions.WEAR_COSTUME_WEAPON)
            if pkItem is not None and item1.GetSubType() != pkItem.GetValue(3):
                ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You can't wear a costume weapon who has different type of your weapon."))
                return LGEMiscellaneous.DEFINECONSTANTS.false

        wEquipCell = item2.GetCell() - ushort(LGEMiscellaneous.INVENTORY_MAX_NUM)
        wInvenCell = item1.GetCell()

        if LGEMiscellaneous.DEFINECONSTANTS.false == CanUnequipNow(item2, NPOS, NPOS, LGEMiscellaneous.DEFINECONSTANTS.false) or LGEMiscellaneous.DEFINECONSTANTS.false == CanEquipNow(item1):
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if wEquipCell != item1.FindEquipCell(self, -1):
            return LGEMiscellaneous.DEFINECONSTANTS.false

        item2.RemoveFromCharacter()

        if item1.EquipTo(self, byte(wEquipCell)):
            item2.AddToCharacter(self, TItemPos(EWindows.INVENTORY, wInvenCell))
        else:
            #lani_err("SwapItem cannot equip %s! item1 %s", item2.GetName(LOCALE_LANIATUS), item1.GetName(LOCALE_LANIATUS))
    else:
        wCell1 = item1.GetCell()
        wCell2 = item2.GetCell()

        item1.RemoveFromCharacter()
        item2.RemoveFromCharacter()

        item1.AddToCharacter(self, TItemPos(EWindows.INVENTORY, wCell2))
        item2.AddToCharacter(self, TItemPos(EWindows.INVENTORY, wCell1))

    return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

def UnequipItem(item):
    pos = None

    if LGEMiscellaneous.DEFINECONSTANTS.false == CanUnequipNow(item):
        return LGEMiscellaneous.DEFINECONSTANTS.false

    if item.IsDragonSoul():
        pos = GetEmptyDragonSoulInventory(item)
    else:
        pos = GetEmptyInventory(item.GetSize())

    if item.GetVnum() == UNIQUE_ITEM_HIDE_ALIGNMENT_TITLE:
        ShowAlignment(((not LGEMiscellaneous.DEFINECONSTANTS.false)))

    item.RemoveFromCharacter()
    if item.IsDragonSoul():
        item.AddToCharacter(self, TItemPos(EWindows.DRAGON_SOUL_INVENTORY, pos))
    else:
        item.AddToCharacter(self, TItemPos(EWindows.INVENTORY, pos))

    if item.IsCostumeMountItem():
        if GetHorse():
            HorseSummon(LGEMiscellaneous.DEFINECONSTANTS.false)

    if item.IsCostumePetItem():
        petSystem = GetPetSystem()
        if petSystem:
            petSystem.HandlePetCostumeItem()

    CheckMaximumPoints()

    return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

def EquipItem(item, iCandidateCell):
    if item.IsExchanging():
        return LGEMiscellaneous.DEFINECONSTANTS.false

    if LGEMiscellaneous.DEFINECONSTANTS.false == item.IsEquipable():
        return LGEMiscellaneous.DEFINECONSTANTS.false

    if LGEMiscellaneous.DEFINECONSTANTS.false == CanEquipNow(item):
        return LGEMiscellaneous.DEFINECONSTANTS.false

    iWearCell = item.FindEquipCell(self, iCandidateCell)

    if iWearCell < 0:
        return LGEMiscellaneous.DEFINECONSTANTS.false

    if iWearCell == EWearPositions.WEAR_BODY and IsRiding() and (item.GetVnum() >= 11901 and item.GetVnum() <= 11904):
        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You cannot wear Tuxido on a horse."))
        return LGEMiscellaneous.DEFINECONSTANTS.false

    if iWearCell != EWearPositions.WEAR_ARROW and IsPolymorphed():
        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You cannot change the equipped Items as long as you are transformed."))
        return LGEMiscellaneous.DEFINECONSTANTS.false

    if FN_check_item_sex(self, item) == LGEMiscellaneous.DEFINECONSTANTS.false:
        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("This Item can be used by the other gender only."))
        return LGEMiscellaneous.DEFINECONSTANTS.false

    if item.IsRideItem() and IsRiding():
        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You are already riding a mount."))
        return LGEMiscellaneous.DEFINECONSTANTS.false

    dwCurTime = get_dword_time()

    if iWearCell == EWearPositions.WEAR_WEAPON and (dwCurTime - GetLastAttackTime() <= 1500 or dwCurTime - m_dwLastSkillTime <= 1500):
        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You have to be motionless to equip the Item."))
        return LGEMiscellaneous.DEFINECONSTANTS.false

    if item.IsDragonSoul():
        if GetInventoryItem(LGEMiscellaneous.INVENTORY_MAX_NUM + iWearCell):
            ChatPacket(EChatType.CHAT_TYPE_INFO, "�̹� ���� ������ ��ȥ���� �����ϰ� �ֽ��ϴ�.")
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if not item.EquipTo(self, byte(iWearCell)):
            return LGEMiscellaneous.DEFINECONSTANTS.false
    elif iWearCell != EWearPositions.WEAR_ARROW and (not item.IsEquipped()) and item.GetCount() > 1:
        item.SetCount(item.GetCount() - 1)
        item2 = ITEM_MANAGER.instance().CreateItem(item.GetVnum(), 1, 0, DefineConstants.false, -1, DefineConstants.false)
        return item2.EquipTo(self, byte(iWearCell))
    else:
        ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'IS_SET' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
        if GetWear(iWearCell) and not IS_SET(GetWear(iWearCell).GetFlag(), EItemFlag.ITEM_FLAG_IRREMOVABLE):

            if LGEMiscellaneous.DEFINECONSTANTS.false == SwapItem(item.GetCell(), LGEMiscellaneous.INVENTORY_MAX_NUM + iWearCell):
                return LGEMiscellaneous.DEFINECONSTANTS.false
        else:
            bOldCell = byte(item.GetCell())

            if item.EquipTo(self, byte(iWearCell)):
                SyncQuickslot(LG_QUICKSLOT_TYPE_ITEM, bOldCell, iWearCell)

    if ((not LGEMiscellaneous.DEFINECONSTANTS.false)) == item.IsEquipped():
        if -1 != item.GetProto().cLimitRealTimeFirstUseIndex:
            if 0 == item.GetSocket(1):
                duration = item.GetSocket(0) if (0 != item.GetSocket(0)) else item.GetProto().aLimits[item.GetProto().cLimitRealTimeFirstUseIndex].lValue

                if 0 == duration:
                    duration = 60 * 60 * 24 * 7

                item.SetSocket(0, time(0) + duration, ((not DefineConstants.false)))
                item.StartRealTimeExpireEvent()

            item.SetSocket(1, item.GetSocket(1) + 1, ((not DefineConstants.false)))

        if item.GetVnum() == UNIQUE_ITEM_HIDE_ALIGNMENT_TITLE:
            ShowAlignment(LGEMiscellaneous.DEFINECONSTANTS.false)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to references to value types:
#ORIGINAL METINII C CODE: const uint& dwVnum = item->GetVnum();
        dwVnum = item.GetVnum()

        if ((not LGEMiscellaneous.DEFINECONSTANTS.false)) == CItemVnumHelper.IsRamadanMoonRing(dwVnum):
            self.EffectPacket(SPECIAL_EFFECT.SE_EQUIP_RAMADAN_RING)
        elif ((not LGEMiscellaneous.DEFINECONSTANTS.false)) == CItemVnumHelper.IsHalloweenCandy(dwVnum):
            self.EffectPacket(SPECIAL_EFFECT.SE_EQUIP_HALLOWEEN_CANDY)
        elif ((not LGEMiscellaneous.DEFINECONSTANTS.false)) == CItemVnumHelper.IsHappinessRing(dwVnum):
            self.EffectPacket(SPECIAL_EFFECT.SE_EQUIP_HAPPINESS_RING)
        elif ((not LGEMiscellaneous.DEFINECONSTANTS.false)) == CItemVnumHelper.IsLovePendant(dwVnum):
            self.EffectPacket(SPECIAL_EFFECT.SE_EQUIP_LOVE_PENDANT)
        elif ((not LGEMiscellaneous.DEFINECONSTANTS.false)) == CItemVnumHelper.IsAcceItem(dwVnum):
            self.EffectPacket(SPECIAL_EFFECT.SE_ACCE_EQUIP)
        elif EItemTypes.ITEM_UNIQUE == item.GetType() and 0 != item.GetSIGVnum():
            pGroup = ITEM_MANAGER.instance().GetSpecialItemGroup(item.GetSIGVnum())
            if None is not pGroup:
                pAttrGroup = ITEM_MANAGER.instance().GetSpecialAttrGroup(pGroup.GetAttrVnum(item.GetVnum()))
                if None is not pAttrGroup:
                    std = pAttrGroup.m_stEffectFileName
                    SpecificEffectPacket(std)

        ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'IS_SET' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
        if EUniqueSubTypes.UNIQUE_SPECIAL_RIDE == item.GetSubType() and IS_SET(item.GetFlag(), EItemFlag.ITEM_FLAG_QUEST_USE):
            quest.CQuestManager.instance().UseItem(GetPlayerID(), item, LGEMiscellaneous.DEFINECONSTANTS.false)
        if item.IsCostumeMountItem():
            if GetHorse():
                HorseSummon(LGEMiscellaneous.DEFINECONSTANTS.false)

            HorseSummon(((not LGEMiscellaneous.DEFINECONSTANTS.false)))

        if item.IsCostumePetItem():
            petSystem = GetPetSystem()
            if petSystem:
                petSystem.HandlePetCostumeItem()

    return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

def BuffOnAttr_AddBuffsFromItem(pItem):
    i = 0
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
## Laniatus Games Studio Inc. | WARNING: This 'sizeof' ratio was replaced with a direct reference to the array length:
#ORIGINAL METINII C CODE: for (int i = 0; i < sizeof(g_aBuffOnAttrPoints)/sizeof(g_aBuffOnAttrPoints[0]); i++)
    while i < len(g_aBuffOnAttrPoints):
        it = m_map_buff_on_attrs.find(g_aBuffOnAttrPoints[i])
        if it != m_map_buff_on_attrs.end():
            it.second.AddBuffFromItem(pItem)
        i += 1

def BuffOnAttr_RemoveBuffsFromItem(pItem):
    i = 0
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
## Laniatus Games Studio Inc. | WARNING: This 'sizeof' ratio was replaced with a direct reference to the array length:
#ORIGINAL METINII C CODE: for (int i = 0; i < sizeof(g_aBuffOnAttrPoints)/sizeof(g_aBuffOnAttrPoints[0]); i++)
    while i < len(g_aBuffOnAttrPoints):
        it = m_map_buff_on_attrs.find(g_aBuffOnAttrPoints[i])
        if it != m_map_buff_on_attrs.end():
            it.second.RemoveBuffFromItem(pItem)
        i += 1

def BuffOnAttr_ClearAll():
    it = m_map_buff_on_attrs.begin()
    while it is not m_map_buff_on_attrs.end():
        pBuff = it.second
        if pBuff:
            pBuff.Initialize()
        it += 1

def BuffOnAttr_ValueChange(bType, bOldValue, bNewValue):
    it = m_map_buff_on_attrs.find(bType)

    if 0 == bNewValue:
        if m_map_buff_on_attrs.end() == it:
            return
        else:
            it.second.Off()
    elif 0 == bOldValue:
        pBuff = None
        if m_map_buff_on_attrs.end() == it:
            if bType == EPointTypes.LG_POINT_ENERGY:
                    ## Laniatus Games Studio Inc. | NOTE: This static local variable declaration (not allowed in Python) has been moved just prior to the method:
                    #                    static byte abSlot[] = { WEAR_BODY, WEAR_HEAD, WEAR_FOOTS, WEAR_WRIST, WEAR_WEAPON, WEAR_NECK, WEAR_EAR, WEAR_SHIELD }
                    ## Laniatus Games Studio Inc. | NOTE: This static local variable declaration (not allowed in Python) has been moved just prior to the method:
                    #                    static list<byte> vec_slots(abSlot, abSlot + _countof(abSlot))
                    pBuff = LG_NEW_M2 CBuffOnAttributes(self, bType, BuffOnAttr_ValueChange_vec_slots)
            elif bType == EPointTypes.LG_POINT_COSTUME_ATTR_BONUS:
                    ## Laniatus Games Studio Inc. | NOTE: This static local variable declaration (not allowed in Python) has been moved just prior to the method:
                    #                    static byte abSlot[] = { WEAR_COSTUME_BODY, WEAR_COSTUME_HAIR, WEAR_COSTUME_WEAPON }
                    ## Laniatus Games Studio Inc. | NOTE: This static local variable declaration (not allowed in Python) has been moved just prior to the method:
                    #                    static list<byte> vec_slots(abSlot, abSlot + _countof(abSlot))
                    pBuff = LG_NEW_M2 CBuffOnAttributes(self, bType, BuffOnAttr_ValueChange_vec_slots)
            m_map_buff_on_attrs.insert(TMapBuffOnAttrs.value_type(bType, pBuff))

        else:
            pBuff = it.second

        pBuff.On(bNewValue)
    else:
        if m_map_buff_on_attrs.end() == it:
            return
        else:
            it.second.ChangeBuffValue(bNewValue)


## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: CItem* CHARACTER::FindSpecifyItem(uint vnum) const
def FindSpecifyItem(vnum):
    i = 0
    while i < LGEMiscellaneous.INVENTORY_MAX_NUM:
        if GetInventoryItem(i) and GetInventoryItem(i).GetVnum() == vnum:
            return GetInventoryItem(i)
        i += 1

    return None

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: CItem* CHARACTER::FindItemByID(uint id) const
def FindItemByID(id):
    i = 0
    while i < LGEMiscellaneous.INVENTORY_MAX_NUM:
        if None != GetInventoryItem(i) and GetInventoryItem(i).GetID() == id:
            return GetInventoryItem(i)
        i += 1

    i = BELT_INVENTORY_SLOT_START
    while i < LGEMiscellaneous2.BELT_INVENTORY_SLOT_END:
        if None != GetInventoryItem(i) and GetInventoryItem(i).GetID() == id:
            return GetInventoryItem(i)
        i += 1

    return None

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: int CHARACTER::CountSpecifyItem(uint vnum, int iExceptionCell) const
def CountSpecifyItem(vnum, iExceptionCell):
    count = 0
    item = None

    i = 0
    while i < LGEMiscellaneous.INVENTORY_MAX_NUM:
        if i == iExceptionCell:
            continue

        item = GetInventoryItem(i)
        if None is not item and item.GetVnum() == vnum:
            if m_pkMyShop and m_pkMyShop.IsSellingItem(item.GetID()):
                continue
            else:
                count += int(item.GetCount())
        i += 1

    return count

def RemoveSpecifyItem(vnum, count, iExceptionCell):
    if 0 == count:
        return

    i = 0
    while i < LGEMiscellaneous.INVENTORY_MAX_NUM:
        if i == iExceptionCell:
            continue

        if None == GetInventoryItem(i):
            continue

        if GetInventoryItem(i).GetVnum() != vnum:
            continue

        if m_pkMyShop:
            isItemSelling = m_pkMyShop.IsSellingItem(GetInventoryItem(i).GetID())
            if isItemSelling:
                continue

        if count >= GetInventoryItem(i).GetCount():
            count -= GetInventoryItem(i).GetCount()
            GetInventoryItem(i).SetCount(0)

            if 0 == count:
                return
        else:
            GetInventoryItem(i).SetCount(GetInventoryItem(i).GetCount() - count)
            return
        i += 1

    if count != 0:
        #sys_log(0, "CHARACTER::RemoveSpecifyItem cannot remove enough item vnum %u, still remain %d", vnum, count)

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: int CHARACTER::CountSpecifyTypeItem(byte type) const
def CountSpecifyTypeItem(type):
    count = 0

    i = 0
    while i < LGEMiscellaneous.INVENTORY_MAX_NUM:
        pItem = GetInventoryItem(i)
        if pItem is not None and pItem.GetType() == type:
            count += int(pItem.GetCount())
        i += 1

    return count

def RemoveSpecifyTypeItem(type, count):
    if 0 == count:
        return

    i = 0
    while i < LGEMiscellaneous.INVENTORY_MAX_NUM:
        if None == GetInventoryItem(i):
            continue

        if GetInventoryItem(i).GetType() != type:
            continue

        if m_pkMyShop:
            isItemSelling = m_pkMyShop.IsSellingItem(GetInventoryItem(i).GetID())
            if isItemSelling:
                continue

        if count >= GetInventoryItem(i).GetCount():
            count -= GetInventoryItem(i).GetCount()
            GetInventoryItem(i).SetCount(0)

            if 0 == count:
                return
        else:
            GetInventoryItem(i).SetCount(GetInventoryItem(i).GetCount() - count)
            return
        i += 1

def AutoGiveItem(item, longOwnerShip):
    if None is item:
        #lani_err("NULL point.")
        return
    if item.GetOwner():
        #lani_err("item %d 's owner exists!",item.GetID())
        return

    cell = None
    if item.IsDragonSoul():
        cell = GetEmptyDragonSoulInventory(item)
    else:
        cell = GetEmptyInventory(item.GetSize())

    if cell != -1:
        if item.IsDragonSoul():
            item.AddToCharacter(self, TItemPos(EWindows.DRAGON_SOUL_INVENTORY, cell))
        else:
            item.AddToCharacter(self, TItemPos(EWindows.INVENTORY, cell))

        if item.GetType() == EItemTypes.ITEM_USE and item.GetSubType() == EUseSubTypes.USE_POTION:
            pSlot = None

            if GetQuickslot(0, pSlot) and pSlot.type == LG_QUICKSLOT_TYPE_NONE:
                slot = SQuickslot()
                slot.type = byte(LG_QUICKSLOT_TYPE_ITEM)
                slot.pos = byte(cell)
                SetQuickslot(0, slot)
    else:
        item.AddToGround(GetMapIndex(), GetXYZ(), DefineConstants.false)
        item.StartDestroyEvent(300)

        if longOwnerShip:
            item.SetOwnership(self, 300)
        else:
            item.SetOwnership(self, 60)

def AutoGiveItem(dwItemVnum, wCount, iRarePct, bMsg):
    p = ITEM_MANAGER.instance().GetTable(dwItemVnum)

    if p is None:
        return None

    if (p.dwFlags & uint(EItemFlag.ITEM_FLAG_STACKABLE)) != 0 and p.bType != EItemTypes.ITEM_BLEND:
        i = 0
        while i < LGEMiscellaneous.INVENTORY_MAX_NUM:
            item = GetInventoryItem(i)

            if item is None:
                continue

            if item.GetVnum() == dwItemVnum and FN_check_LG_ITEM_SOCKET(item):
                ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'IS_SET' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
                if IS_SET(p.dwFlags, EItemFlag.ITEM_FLAG_MAKECOUNT):
                    if wCount < p.alValues[1]:
                        wCount = ushort(p.alValues[1])

                wCount2 = MIN(EItemMisc.ITEM_MAX_COUNT - item.GetCount(), wCount)
                wCount -= wCount2

                item.SetCount(item.GetCount() + wCount2)

                if wCount == 0:
                    if bMsg:
                        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("%s received"), item.GetName(LOCALE_LANIATUS))

                    return item
            i += 1

    item = ITEM_MANAGER.instance().CreateItem(dwItemVnum, wCount, 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), -1, DefineConstants.false)

    if item is None:
        #lani_err("cannot create item by vnum %u (name: %s)", dwItemVnum, GetName())
        return None

    if item.GetType() == EItemTypes.ITEM_BLEND:
        i = 0
        while i < LGEMiscellaneous.INVENTORY_MAX_NUM:
            inv_item = GetInventoryItem(i)

            if inv_item is None:
                continue

            if inv_item.GetType() == EItemTypes.ITEM_BLEND:
                if inv_item.GetVnum() == item.GetVnum():
                    if inv_item.GetSocket(0) == item.GetSocket(0) and inv_item.GetSocket(1) == item.GetSocket(1) and inv_item.GetSocket(2) == item.GetSocket(2) and inv_item.GetCount() + item.GetCount() <= EItemMisc.ITEM_MAX_COUNT:
                        inv_item.SetCount(inv_item.GetCount() + item.GetCount())
                        ITEM_MANAGER.instance().DestroyItem(item)
                        return inv_item
            i += 1

    iEmptyCell = None
    if item.IsDragonSoul():
        iEmptyCell = GetEmptyDragonSoulInventory(item)
    else:
        iEmptyCell = GetEmptyInventory(item.GetSize())

    if iEmptyCell != -1:
        if item.IsDragonSoul():
            item.AddToCharacter(self, TItemPos(EWindows.DRAGON_SOUL_INVENTORY, iEmptyCell))
        else:
            item.AddToCharacter(self, TItemPos(EWindows.INVENTORY, iEmptyCell))

        if bMsg:
            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("%s received"), item.GetName(LOCALE_LANIATUS))

        if item.GetType() == EItemTypes.ITEM_USE and item.GetSubType() == EUseSubTypes.USE_POTION:
            pSlot = None

            if GetQuickslot(0, pSlot) and pSlot.type == LG_QUICKSLOT_TYPE_NONE:
                slot = SQuickslot()
                slot.type = byte(LG_QUICKSLOT_TYPE_ITEM)
                slot.pos = byte(iEmptyCell)
                SetQuickslot(0, slot)
    else:
        item.AddToGround(GetMapIndex(), GetXYZ(), DefineConstants.false)
        item.StartDestroyEvent(300)

        ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'IS_SET' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
        if IS_SET(item.GetAntiFlag(), LaniatusEITMAntiFlagDcs.ITEM_ANTIFLAG_DROP):
            item.SetOwnership(self, 300)
        else:
            item.SetOwnership(self, 60)

    #sys_log(0, "7: %d %d", dwItemVnum, wCount)
    return item

def GiveItem(victim, Cell):
    if not CanHandleItem():
        return LGEMiscellaneous.DEFINECONSTANTS.false

    item = GetItem(Cell)

    if item is not None and not item.IsExchanging():
        if victim.CanReceiveItem(self, item):
            victim.ReceiveItem(self, item)
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    return LGEMiscellaneous.DEFINECONSTANTS.false

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: bool CHARACTER::CanReceiveItem(CHARACTER* from, CItem* item) const
def CanReceiveItem(from_, item):
    if IsPC():
        return LGEMiscellaneous.DEFINECONSTANTS.false

    if DISTANCE_APPROX(GetX() - from_.GetX(), GetY() - from_.GetY()) > 2000:
        return LGEMiscellaneous.DEFINECONSTANTS.false

    if GetRaceNum() == fishing.CAMPFIRE_MOB:
        if item.GetType() == EItemTypes.ITEM_FISH and (item.GetSubType() == EFishSubTypes.FISH_ALIVE or item.GetSubType() == EFishSubTypes.FISH_DEAD):
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    elif GetRaceNum() == fishing.FISHER_MOB:
        if item.GetType() == EItemTypes.ITEM_ROD:
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    elif (GetRaceNum() == BLACKSMITH_WEAPON_MOB) or (GetRaceNum() == DEVILTOWER_BLACKSMITH_WEAPON_MOB):
        if item.GetType() == EItemTypes.ITEM_WEAPON and item.GetRefinedVnum() != 0:
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
        else:
            return LGEMiscellaneous.DEFINECONSTANTS.false

    elif (GetRaceNum() == BLACKSMITH_ARMOR_MOB) or (GetRaceNum() == DEVILTOWER_BLACKSMITH_ARMOR_MOB):
        if item.GetType() == EItemTypes.ITEM_ARMOR and (item.GetSubType() == EArmorSubTypes.ARMOR_BODY or item.GetSubType() == EArmorSubTypes.ARMOR_SHIELD or item.GetSubType() == EArmorSubTypes.ARMOR_HEAD) and item.GetRefinedVnum():
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
        else:
            return LGEMiscellaneous.DEFINECONSTANTS.false

    elif (GetRaceNum() == BLACKSMITH_ACCESSORY_MOB) or (GetRaceNum() == DEVILTOWER_BLACKSMITH_ACCESSORY_MOB):
        if item.GetType() == EItemTypes.ITEM_ARMOR and not(item.GetSubType() == EArmorSubTypes.ARMOR_BODY or item.GetSubType() == EArmorSubTypes.ARMOR_SHIELD or item.GetSubType() == EArmorSubTypes.ARMOR_HEAD) and item.GetRefinedVnum():
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
        else:
            return LGEMiscellaneous.DEFINECONSTANTS.false

    elif GetRaceNum() == BLACKSMITH_MOB:
        if item.GetRefinedVnum() != 0 and item.GetRefineSet() < 500:
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
        else:
            return LGEMiscellaneous.DEFINECONSTANTS.false

    elif (GetRaceNum() == BLACKSMITH_MOB) or (GetRaceNum() == GOLDEN_BLACKSMITH_MOB):
        if item.GetRefinedVnum() != 0 and item.GetRefineSet() < 500:
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
        else:
            return LGEMiscellaneous.DEFINECONSTANTS.false

    elif (GetRaceNum() == BLACKSMITH_MOB) or (GetRaceNum() == GOLDEN_BLACKSMITH_MOB) or (GetRaceNum() == BLACKSMITH2_MOB):
        if item.GetRefineSet() >= 500:
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
        else:
            return LGEMiscellaneous.DEFINECONSTANTS.false

    elif (GetRaceNum() == BLACKSMITH_MOB) or (GetRaceNum() == GOLDEN_BLACKSMITH_MOB) or (GetRaceNum() == BLACKSMITH2_MOB) or (GetRaceNum() == ALCHEMIST_MOB):
        if item.GetRefinedVnum() != 0:
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    elif (GetRaceNum() == 20101) or (GetRaceNum() == 20102) or (GetRaceNum() == 20103):
        if item.GetVnum() == ITEM_REVIVE_HORSE_1:
            if not IsDead():
                from_.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You cannot feed a living Horse with Herbs."))
                return LGEMiscellaneous.DEFINECONSTANTS.false
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
        elif item.GetVnum() == ITEM_HORSE_FOOD_1:
            if IsDead():
                from_.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You cannot feed a dead Horse."))
                return LGEMiscellaneous.DEFINECONSTANTS.false
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
        elif item.GetVnum() == ITEM_HORSE_FOOD_2 or item.GetVnum() == ITEM_HORSE_FOOD_3:
            return LGEMiscellaneous.DEFINECONSTANTS.false
    elif (GetRaceNum() == 20104) or (GetRaceNum() == 20105) or (GetRaceNum() == 20106):
        if item.GetVnum() == ITEM_REVIVE_HORSE_2:
            if not IsDead():
                from_.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You cannot feed a living Horse with Herbs."))
                return LGEMiscellaneous.DEFINECONSTANTS.false
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
        elif item.GetVnum() == ITEM_HORSE_FOOD_2:
            if IsDead():
                from_.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You cannot feed a dead Horse."))
                return LGEMiscellaneous.DEFINECONSTANTS.false
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
        elif item.GetVnum() == ITEM_HORSE_FOOD_1 or item.GetVnum() == ITEM_HORSE_FOOD_3:
            return LGEMiscellaneous.DEFINECONSTANTS.false
    elif (GetRaceNum() == 20107) or (GetRaceNum() == 20108) or (GetRaceNum() == 20109):
        if item.GetVnum() == ITEM_REVIVE_HORSE_3:
            if not IsDead():
                from_.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You cannot feed a living Horse with Herbs."))
                return LGEMiscellaneous.DEFINECONSTANTS.false
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
        elif item.GetVnum() == ITEM_HORSE_FOOD_3:
            if IsDead():
                from_.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You cannot feed a dead Horse."))
                return LGEMiscellaneous.DEFINECONSTANTS.false
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
        elif item.GetVnum() == ITEM_HORSE_FOOD_1 or item.GetVnum() == ITEM_HORSE_FOOD_2:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    return LGEMiscellaneous.DEFINECONSTANTS.false

def ReceiveItem(from_, item):
    if IsPC():
        return

    if GetRaceNum() == fishing.CAMPFIRE_MOB:
        if item.GetType() == EItemTypes.ITEM_FISH and (item.GetSubType() == EFishSubTypes.FISH_ALIVE or item.GetSubType() == EFishSubTypes.FISH_DEAD):
            fishing.Grill(from_, item)
        else:
            from_.SetQuestNPCID(GetVID())
            quest.CQuestManager.instance().TakeItem(from_.GetPlayerID(), GetRaceNum(), item)

    elif (GetRaceNum() == DEVILTOWER_BLACKSMITH_WEAPON_MOB) or (GetRaceNum() == DEVILTOWER_BLACKSMITH_ARMOR_MOB) or (GetRaceNum() == DEVILTOWER_BLACKSMITH_ACCESSORY_MOB):
        if item.GetRefinedVnum() != 0 and item.GetRefineSet() != 0 and item.GetRefineSet() < 500:
            from_.SetRefineNPC(self)
            from_.RefineInformation(item.GetCell(), ERefineType.REFINE_TYPE_MONEY_ONLY, -1)
        else:
            from_.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("This Item can't be made better."))

    elif (GetRaceNum() == BLACKSMITH_MOB) or (GetRaceNum() == GOLDEN_BLACKSMITH_MOB) or (GetRaceNum() == BLACKSMITH2_MOB) or (GetRaceNum() == BLACKSMITH_WEAPON_MOB) or (GetRaceNum() == BLACKSMITH_ARMOR_MOB) or (GetRaceNum() == BLACKSMITH_ACCESSORY_MOB):
        if CItemVnumHelper.IsAcceItem(item.GetVnum()):
            return

        if item.GetRefinedVnum() != 0:
            from_.SetRefineNPC(self)
            from_.RefineInformation(item.GetCell(), ERefineType.REFINE_TYPE_NORMAL, -1)
        else:
            from_.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("This Item can't be made better."))

    elif (GetRaceNum() == 20101) or (GetRaceNum() == 20102) or (GetRaceNum() == 20103) or (GetRaceNum() == 20104) or (GetRaceNum() == 20105) or (GetRaceNum() == 20106) or (GetRaceNum() == 20107) or (GetRaceNum() == 20108) or (GetRaceNum() == 20109):
        if item.GetVnum() == ITEM_REVIVE_HORSE_1 or item.GetVnum() == ITEM_REVIVE_HORSE_2 or item.GetVnum() == ITEM_REVIVE_HORSE_3:
            from_.ReviveHorse()
            item.SetCount(item.GetCount()-1)
            from_.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You fed the Horse with Herbs."))
        elif item.GetVnum() == ITEM_HORSE_FOOD_1 or item.GetVnum() == ITEM_HORSE_FOOD_2 or item.GetVnum() == ITEM_HORSE_FOOD_3:
            from_.FeedHorse()
            from_.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You fed the Horse."))
            item.SetCount(item.GetCount()-1)
            EffectPacket(SPECIAL_EFFECT.SE_HPUP_RED)

    else:
        #sys_log(0, "TakeItem %s %d %s", from_.GetName(LOCALE_LANIATUS), GetRaceNum(), item.GetName(LOCALE_LANIATUS))
        from_.SetQuestNPCID(GetVID())
        quest.CQuestManager.instance().TakeItem(from_.GetPlayerID(), GetRaceNum(), item)

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: bool CHARACTER::IsEquipUniqueItem(uint dwItemVnum) const
def IsEquipUniqueItem(dwItemVnum):
        u = GetWear(EWearPositions.WEAR_UNIQUE1)

        if u is not None and u.GetVnum() == dwItemVnum:
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        u = GetWear(EWearPositions.WEAR_UNIQUE2)

        if u is not None and u.GetVnum() == dwItemVnum:
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    if dwItemVnum == UNIQUE_ITEM_RING_OF_LANGUAGE:
        return IsEquipUniqueItem(UNIQUE_ITEM_RING_OF_LANGUAGE_SAMPLE)

    return LGEMiscellaneous.DEFINECONSTANTS.false

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: bool CHARACTER::IsEquipUniqueGroup(uint dwGroupVnum) const
def IsEquipUniqueGroup(dwGroupVnum):
        u = GetWear(EWearPositions.WEAR_UNIQUE1)

        if u is not None and u.GetSpecialGroup() == int(dwGroupVnum):
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        u = GetWear(EWearPositions.WEAR_UNIQUE2)

        if u is not None and u.GetSpecialGroup() == int(dwGroupVnum):
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    return LGEMiscellaneous.DEFINECONSTANTS.false

def SetRefineMode(iAdditionalCell):
    m_iRefineAdditionalCell = iAdditionalCell
    m_bUnderRefine = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

def ClearRefineMode():
    m_bUnderRefine = LGEMiscellaneous.DEFINECONSTANTS.false
    SetRefineNPC(None)

def GiveItemFromSpecialItemGroup(dwGroupNum, dwItemVnums, dwItemCounts, item_gets, count):
    pGroup = ITEM_MANAGER.instance().GetSpecialItemGroup(dwGroupNum)

    if pGroup is None:
        #lani_err("cannot find special item group %d", dwGroupNum)
        return LGEMiscellaneous.DEFINECONSTANTS.false

    idxes = []
    n = pGroup.GetMultiIndex(idxes)

    bSuccess = LGEMiscellaneous.DEFINECONSTANTS.false

    for i in range(0, n):
        idx = idxes[i]
        dwVnum = uint(pGroup.GetVnum(idx))
        dwCount = uint(pGroup.GetCount(idx))
        iRarePct = pGroup.GetRarePct(idx)
        item_get = None
        if dwVnum == CSpecialItemGroup.EGiveType.GOLD:
            PointChange(EPointTypes.LG_POINT_GOLD, dwCount)
            bSuccess = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
        elif dwVnum == CSpecialItemGroup.EGiveType.EXP:
                PointChange(EPointTypes.LG_POINT_EXP, dwCount)
                bSuccess = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        elif dwVnum == CSpecialItemGroup.EGiveType.MOB:
                #sys_log(0, "CSpecialItemGroup::MOB %d", dwCount)
                x = GetX() + number(-500, 500)
                y = GetY() + number(-500, 500)

                ch = CHARACTER_MANAGER.instance().SpawnMob(dwCount, GetMapIndex(), x, y, 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), -1, ((not DefineConstants.false)))
                if ch:
                    ch.SetAggressive()
                bSuccess = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
        elif dwVnum == CSpecialItemGroup.EGiveType.SLOW:
                #sys_log(0, "CSpecialItemGroup::SLOW %d", -int(dwCount))
                AddAffect(LaniatusEAffectTypes.LANIA_AFFECT_SLOW, EPointTypes.LG_POINT_MOV_SPEED, -int(dwCount), EAffectBits.AFF_SLOW, 300, 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
                bSuccess = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
        elif dwVnum == CSpecialItemGroup.EGiveType.DRAIN_HP:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
                iDropHP = GetMaxHP()*dwCount/100
                #sys_log(0, "CSpecialItemGroup::DRAIN_HP %d", -iDropHP)
                iDropHP = MIN(iDropHP, GetHP()-1)
                #sys_log(0, "CSpecialItemGroup::DRAIN_HP %d", -iDropHP)
                PointChange(EPointTypes.LG_POINT_HP, -iDropHP)
                bSuccess = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
        elif dwVnum == CSpecialItemGroup.EGiveType.POISON:
                AttackedByPoison(None)
                bSuccess = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if ENABLE_WOLFMAN
        elif dwVnum == CSpecialItemGroup.EGiveType.BLEEDING:
                AttackedByBleeding(None)
                bSuccess = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
##endif

        elif dwVnum == CSpecialItemGroup.EGiveType.MOB_GROUP:
                sx = GetX() - number(300, 500)
                sy = GetY() - number(300, 500)
                ex = GetX() + number(300, 500)
                ey = GetY() + number(300, 500)
                CHARACTER_MANAGER.instance().SpawnGroup(dwCount, GetMapIndex(), sx, sy, ex, ey, None, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), NULL)

                bSuccess = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
        else:
                item_get = AutoGiveItem(dwVnum, dwCount, iRarePct)

                if item_get:
                    bSuccess = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        if bSuccess:
            dwItemVnums.append(dwVnum)
            dwItemCounts.append(dwCount)
            item_gets.append(item_get)
            count.arg_value += 1

        else:
            return LGEMiscellaneous.DEFINECONSTANTS.false
    return bSuccess

def ItemProcess_Hair(item, iDestCell):
    if item.CheckItemUseLevel(GetLevel()) == LGEMiscellaneous.DEFINECONSTANTS.false:
        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You Level is too low to wear this Hairstyle."))
        return LGEMiscellaneous.DEFINECONSTANTS.false

    hair = item.GetVnum()

    if GetJob() == EJobs.JOB_LG_PAWN_WARRIOR:
        hair -= 72000

    elif GetJob() == EJobs.JOB_LG_PAWN_ASSASSIN:
        hair -= 71250

    elif GetJob() == EJobs.JOB_LG_PAWN_SHURA:
        hair -= 70500

    elif GetJob() == EJobs.JOB_LG_PAWN_MAGE:
        hair -= 69750

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if ENABLE_WOLFMAN
    elif GetJob() == EJobs.JOB_WOLFMAN:
        pass
##endif

    else:
        return LGEMiscellaneous.DEFINECONSTANTS.false

    if hair == GetPart(EParts.PART_HAIR):
        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You already wear this Hairstyle."))
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    item.SetCount(item.GetCount() - 1)

    SetPart(EParts.PART_HAIR, hair)
    UpdatePacket()

    return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

def ItemProcess_Polymorph(item):
    if IsPolymorphed():
        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You are already transformed."))
        return LGEMiscellaneous.DEFINECONSTANTS.false

    if ((not LGEMiscellaneous.DEFINECONSTANTS.false)) == IsRiding():
        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Not available."))
        return LGEMiscellaneous.DEFINECONSTANTS.false

    dwVnum = uint(item.GetSocket(0))

    if dwVnum == 0:
        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("That's the wrong trading item."))
        item.SetCount(item.GetCount()-1)
        return LGEMiscellaneous.DEFINECONSTANTS.false

    pMob = CMobManager.instance().Get(dwVnum)

    if pMob is None:
        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("That's the wrong trading item."))
        item.SetCount(item.GetCount()-1)
        return LGEMiscellaneous.DEFINECONSTANTS.false

    if (item.GetVnum() == 70104) or (item.GetVnum() == 70105) or (item.GetVnum() == 70106) or (item.GetVnum() == 70107) or (item.GetVnum() == 71093):
            #sys_log(0, "USE_POLYMORPH_BALL PID(%d) vnum(%d)", GetPlayerID(), dwVnum)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
            iPolymorphLevelLimit = MAX(0, 20 - GetLevel() * 3 / 10)
            if pMob.m_table.bLevel >= GetLevel() + iPolymorphLevelLimit:
                ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You can't transform into another player who has a higher Level than you."))
                return LGEMiscellaneous.DEFINECONSTANTS.false

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
            iDuration = 5 if GetSkillLevel(LGEMiscellaneous.DEFINECONSTANTS.POLYMORPH_LG_SKILL_ID) == 0 else (5 + (5 + GetSkillLevel(LGEMiscellaneous.DEFINECONSTANTS.POLYMORPH_LG_SKILL_ID)/40 * 25))
            iDuration *= 60

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
            dwBonus = (2 + GetSkillLevel(LGEMiscellaneous.DEFINECONSTANTS.POLYMORPH_LG_SKILL_ID) / 40) * 100

            AddAffect(LaniatusEAffectTypes.LANIA_AFFECT_POLYMORPH, EPointTypes.LG_POINT_POLYMORPH, dwVnum, EAffectBits.AFF_POLYMORPH, iDuration, 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
            AddAffect(LaniatusEAffectTypes.LANIA_AFFECT_POLYMORPH, EPointTypes.LG_POINT_ATT_BONUS, dwBonus, EAffectBits.AFF_POLYMORPH, iDuration, 0, LGEMiscellaneous.DEFINECONSTANTS.false)

            item.SetCount(item.GetCount()-1)

    elif item.GetVnum() == 50322:
            #sys_log(0, "USE_POLYMORPH_BOOK: %s(%u) vnum(%u)", GetName(), GetPlayerID(), dwVnum)

            if CPolymorphUtils.instance().PolymorphCharacter(self, item, pMob) == ((not LGEMiscellaneous.DEFINECONSTANTS.false)):
                CPolymorphUtils.instance().UpdateBookPracticeGrade(self, item)
            else:
                pass

    else:
        #lani_err("POLYMORPH invalid item passed PID(%d) vnum(%d)", GetPlayerID(), item.GetOriginalVnum())
        return LGEMiscellaneous.DEFINECONSTANTS.false

    return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: bool CHARACTER::CanDoCube() const
def CanDoCube():
    if m_bIsObserver:
        return LGEMiscellaneous.DEFINECONSTANTS.false
    if GetShop():
        return LGEMiscellaneous.DEFINECONSTANTS.false
    if GetMyShop():
        return LGEMiscellaneous.DEFINECONSTANTS.false
    if m_bUnderRefine:
        return LGEMiscellaneous.DEFINECONSTANTS.false
    if IsWarping():
        return LGEMiscellaneous.DEFINECONSTANTS.false
    if IsAcceWindowOpen():
        return LGEMiscellaneous.DEFINECONSTANTS.false

    return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

def UnEquipSpecialRideUniqueItem():
    Unique1 = GetWear(EWearPositions.WEAR_UNIQUE1)
    Unique2 = GetWear(EWearPositions.WEAR_UNIQUE2)

    if None is not Unique1:
        if UNIQUE_GROUP_SPECIAL_RIDE == Unique1.GetSpecialGroup():
            return UnequipItem(Unique1)

    if None is not Unique2:
        if UNIQUE_GROUP_SPECIAL_RIDE == Unique2.GetSpecialGroup():
            return UnequipItem(Unique2)

    return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

def AutoRecoveryItemProcess(type):
    if ((not LGEMiscellaneous.DEFINECONSTANTS.false)) == IsDead() or ((not LGEMiscellaneous.DEFINECONSTANTS.false)) == IsStun():
        return

    if LGEMiscellaneous.DEFINECONSTANTS.false == IsPC():
        return

    if LaniatusEAffectTypes.LANIA_AFFECT_AUTO_HP_RECOVERY != type and LaniatusEAffectTypes.LANIA_AFFECT_AUTO_SP_RECOVERY != type:
        return

    if None != FindAffect(LaniatusEAffectTypes.LANIA_AFFECT_STUN):
        return

        stunSkills = [(int)LaniatusETalentXes.LG_SKILL_TANHWAN, LaniatusETalentXes.LG_SKILL_GEOMPUNG, LaniatusETalentXes.LG_SKILL_BYEURAK, (int)LaniatusETalentXes.LG_SKILL_GIGUNG]

        i = 0
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
## Laniatus Games Studio Inc. | WARNING: This 'sizeof' ratio was replaced with a direct reference to the array length:
#ORIGINAL METINII C CODE: for (int i=0 ; i < sizeof(stunSkills)/sizeof(uint) ; ++i)
        while i < len(stunSkills):
            p = FindAffect(stunSkills[i])

            if None is not p and EAffectBits.AFF_STUN == p.dwFlag:
                return
            i += 1

    pAffect = FindAffect(type)
    IDX_OF_AMOUNT_OF_USED = 1
    IDX_OF_AMOUNT_OF_FULL = 2

    if None is not pAffect:
        pItem = FindItemByID(pAffect.dwFlag)

        if None is not pItem and (1 if ((not LGEMiscellaneous.DEFINECONSTANTS.false)) else 0) == pItem.GetSocket(0):
            amount_of_used = pItem.GetSocket(IDX_OF_AMOUNT_OF_USED)
            amount_of_full = pItem.GetSocket(IDX_OF_AMOUNT_OF_FULL)

            avail = amount_of_full - amount_of_used

            amount = 0

            if LaniatusEAffectTypes.LANIA_AFFECT_AUTO_HP_RECOVERY == type:
                amount = GetMaxHP() - (GetHP() + GetPoint(EPointTypes.LG_POINT_HP_RECOVERY))
            elif LaniatusEAffectTypes.LANIA_AFFECT_AUTO_SP_RECOVERY == type:
                amount = GetMaxSP() - (GetSP() + GetPoint(EPointTypes.LG_POINT_SP_RECOVERY))

            if amount > 0:
                if avail > amount:
                    pct_of_used = math.trunc(amount_of_used * 100 / float(amount_of_full))
                    pct_of_will_used = math.trunc((amount_of_used + amount) * 100 / float(amount_of_full))

                    bLog = LGEMiscellaneous.DEFINECONSTANTS.false

                    if (math.trunc(pct_of_will_used / float(10))) - (math.trunc(pct_of_used / float(10))) >= 1:
                        bLog = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
                    pItem.SetSocket(IDX_OF_AMOUNT_OF_USED, amount_of_used + amount, bLog)
                else:
                    amount = avail

                    ITEM_MANAGER.instance().RemoveItem(pItem, NULL)

                if LaniatusEAffectTypes.LANIA_AFFECT_AUTO_HP_RECOVERY == type:
                    PointChange(EPointTypes.LG_POINT_HP_RECOVERY, amount)
                    EffectPacket(SPECIAL_EFFECT.SE_AUTO_HPUP)
                elif LaniatusEAffectTypes.LANIA_AFFECT_AUTO_SP_RECOVERY == type:
                    PointChange(EPointTypes.LG_POINT_SP_RECOVERY, amount)
                    EffectPacket(SPECIAL_EFFECT.SE_AUTO_SPUP)
        else:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no equivalent to 'const_cast' in Python:
            RemoveAffect(const_cast<LaniaCAffects>(pAffect))

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: bool CHARACTER::IsValidItemPosition(TItemPos Pos) const
def IsValidItemPosition(Pos):
    window_type = Pos.window_type
    cell = Pos.cell

    if window_type == EWindows.RESERVED_WINDOW:
        return LGEMiscellaneous.DEFINECONSTANTS.false

    if (window_type == EWindows.RESERVED_WINDOW) or (window_type == EWindows.INVENTORY) or (window_type == EWindows.EQUIPMENT):
        return cell < (LGEMiscellaneous2.INVENTORY_AND_EQUIP_SLOT_MAX)

    if (window_type == EWindows.RESERVED_WINDOW) or (window_type == EWindows.INVENTORY) or (window_type == EWindows.EQUIPMENT) or (window_type == EWindows.DRAGON_SOUL_INVENTORY):
        return cell < (EDSInventoryMaxNum.DRAGON_SOUL_INVENTORY_MAX_NUM)

    if (window_type == EWindows.RESERVED_WINDOW) or (window_type == EWindows.INVENTORY) or (window_type == EWindows.EQUIPMENT) or (window_type == EWindows.DRAGON_SOUL_INVENTORY) or (window_type == EWindows.SAFEBOX):
        if None != m_pkSafebox:
            return m_pkSafebox.IsValidPosition(cell)
        else:
            return LGEMiscellaneous.DEFINECONSTANTS.false

    if (window_type == EWindows.RESERVED_WINDOW) or (window_type == EWindows.INVENTORY) or (window_type == EWindows.EQUIPMENT) or (window_type == EWindows.DRAGON_SOUL_INVENTORY) or (window_type == EWindows.SAFEBOX) or (window_type == EWindows.MALL):
        if None != m_pkMall:
            return m_pkMall.IsValidPosition(cell)
        else:
            return LGEMiscellaneous.DEFINECONSTANTS.false


    if True:
        return LGEMiscellaneous.DEFINECONSTANTS.false

## Laniatus Games Studio Inc. | NOTE: The following #define macro was replaced in-line:
#ORIGINAL METINII C CODE: #define VERIFY_MSG(exp, msg) if (true == (exp)) { ChatPacket(CHAT_TYPE_INFO, LC_TEXT(msg)); return false; }

def CanEquipNow(item, srcCell, destCell):
    itemTable = item.GetProto()
    itemType = item.GetType()
    itemSubType = item.GetSubType()

    if GetJob() == EJobs.JOB_LG_PAWN_WARRIOR:
        if (item.GetAntiFlag() & uint(LaniatusEITMAntiFlagDcs.ITEM_ANTIFLAG_LG_PAWN_WARRIOR)) != 0:
            return LGEMiscellaneous.DEFINECONSTANTS.false

    elif GetJob() == EJobs.JOB_LG_PAWN_ASSASSIN:
        if (item.GetAntiFlag() & uint(LaniatusEITMAntiFlagDcs.ITEM_ANTIFLAG_LG_PAWN_ASSASSIN)) != 0:
            return LGEMiscellaneous.DEFINECONSTANTS.false

    elif GetJob() == EJobs.JOB_LG_PAWN_MAGE:
        if (item.GetAntiFlag() & uint(LaniatusEITMAntiFlagDcs.ITEM_ANTIFLAG_LG_PAWN_MAGE)) != 0:
            return LGEMiscellaneous.DEFINECONSTANTS.false

    elif GetJob() == EJobs.JOB_LG_PAWN_SHURA:
        if (item.GetAntiFlag() & uint(LaniatusEITMAntiFlagDcs.ITEM_ANTIFLAG_LG_PAWN_SHURA)) != 0:
            return LGEMiscellaneous.DEFINECONSTANTS.false

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if ENABLE_WOLFMAN
    elif GetJob() == EJobs.JOB_WOLFMAN:
        if (item.GetAntiFlag() & uint(LaniatusEITMAntiFlagDcs.ITEM_ANTIFLAG_WOLFMAN)) != 0:
            return LGEMiscellaneous.DEFINECONSTANTS.false
##endif

    i = 0
    while i < EItemMisc.ITEM_LIMIT_MAX_NUM:
        limit = itemTable.aLimits[i].lValue
        if itemTable.aLimits[i].bType == ELimitTypes.LIMIT_LEVEL:
            if GetLevel() < limit:
                ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Your Level is too low to equip this."))
                return LGEMiscellaneous.DEFINECONSTANTS.false

        elif itemTable.aLimits[i].bType == ELimitTypes.LIMIT_STR:
            if GetPoint(EPointTypes.LG_POINT_ST) < limit:
                ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You are not strong enough to equip this."))
                return LGEMiscellaneous.DEFINECONSTANTS.false

        elif itemTable.aLimits[i].bType == ELimitTypes.LIMIT_INT:
            if GetPoint(EPointTypes.LG_POINT_IQ) < limit:
                ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Your Intelligence it too low to equip this."))
                return LGEMiscellaneous.DEFINECONSTANTS.false

        elif itemTable.aLimits[i].bType == ELimitTypes.LIMIT_DEX:
            if GetPoint(EPointTypes.LG_POINT_DX) < limit:
                ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Your Agility is too low to equip this."))
                return LGEMiscellaneous.DEFINECONSTANTS.false

        elif itemTable.aLimits[i].bType == ELimitTypes.LIMIT_CON:
            if GetPoint(EPointTypes.LG_POINT_HT) < limit:
                ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You Vitality is too low to equip this."))
                return LGEMiscellaneous.DEFINECONSTANTS.false
        i += 1

    if item.GetType() == EItemTypes.ITEM_RING:
        if (GetWear(EWearPositions.WEAR_RING1) and GetWear(EWearPositions.WEAR_RING1).GetVnum() == item.GetVnum()) or (GetWear(EWearPositions.WEAR_RING2) and GetWear(EWearPositions.WEAR_RING2).GetVnum() == item.GetVnum()):
            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You cannot equip this Item twice."))
            return LGEMiscellaneous.DEFINECONSTANTS.false

    if (item.GetWearFlag() & uint(EItemWearableFlag.WEARABLE_UNIQUE)) != 0:
        if (GetWear(EWearPositions.WEAR_UNIQUE1) and GetWear(EWearPositions.WEAR_UNIQUE1).IsSameSpecialGroup(item)) or (GetWear(EWearPositions.WEAR_UNIQUE2) and GetWear(EWearPositions.WEAR_UNIQUE2).IsSameSpecialGroup(item)):
            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You cannot equip this Item twice."))
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if marriage.CManager.instance().IsMarriageUniqueItem(item.GetVnum()) and not marriage.CManager.instance().IsMarried(GetPlayerID()):
            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You cannot use this Item if you are not married."))
            return LGEMiscellaneous.DEFINECONSTANTS.false


    if item.GetType() == EItemTypes.ITEM_WEAPON and item.GetSubType() != EWeaponSubTypes.WEAPON_ARROW and item.GetSubType() != EWeaponSubTypes.WEAPON_QUIVER:
        pkItem = GetWear(EWearPositions.WEAR_COSTUME_WEAPON)
        if pkItem is None:
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
        elif item.GetSubType() != pkItem.GetValue(3):
            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You can't wear a weapon costume which has a different type than your weapon."))
            return LGEMiscellaneous.DEFINECONSTANTS.false
    elif item.GetType() == EItemTypes.ITEM_COSTUME and item.GetSubType() == ECostumeSubTypes.COSTUME_WEAPON:
        pkItem = GetWear(EWearPositions.WEAR_WEAPON)
        if pkItem is None:
            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You cant wear a weapon costume without wearing a weapon"))
            return LGEMiscellaneous.DEFINECONSTANTS.false
        elif item.GetValue(3) != pkItem.GetSubType():
            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You can't wear a weapon costume which has a different type than your weapon."))
            return LGEMiscellaneous.DEFINECONSTANTS.false

    if item.IsCostumeMountItem():
        if IsRiding():
            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You can't equip a mount skin while riding."))
            return LGEMiscellaneous.DEFINECONSTANTS.false

    return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

def CanUnequipNow(item, srcCell, destCell, checkCostume):
    if EItemTypes.ITEM_BELT == item.GetType():
        if ((not LGEMiscellaneous.DEFINECONSTANTS.false)) == (CBeltInventoryHelper.IsExistItemInBeltInventory(self)):
            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You can only discard the belt when there are no longer any items in its inventory."))
            return LGEMiscellaneous.DEFINECONSTANTS.false

    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'IS_SET' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
    if IS_SET(item.GetFlag(), EItemFlag.ITEM_FLAG_IRREMOVABLE):
        return LGEMiscellaneous.DEFINECONSTANTS.false

    if item.IsCostumeMountItem() and IsRiding():
        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You can't unequip a mount skin while riding."))
        return LGEMiscellaneous.DEFINECONSTANTS.false

        pos = -1

        if item.IsDragonSoul():
            pos = GetEmptyDragonSoulInventory(item)
        else:
            pos = GetEmptyInventory(item.GetSize())

        if ((not LGEMiscellaneous.DEFINECONSTANTS.false)) == (-1 == pos):
            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("There isn't enough space in the inventory."))
            return LGEMiscellaneous.DEFINECONSTANTS.false

    if checkCostume and item.GetType() == EItemTypes.ITEM_WEAPON and item.GetSubType() != EWeaponSubTypes.WEAPON_ARROW and item.GetSubType() != EWeaponSubTypes.WEAPON_QUIVER:
        pkItem = GetWear(EWearPositions.WEAR_COSTUME_WEAPON)
        if pkItem:
            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You cant do this until you unwear your weapon costume."))
            return LGEMiscellaneous.DEFINECONSTANTS.false

    return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

def AcceRefineCheckin(acceSlot, currentCell):
    if GetAcceWindowType() >= 3:
        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Wrong sash window, detected hacker!"))
        return

    for i in range(0, ACCE_SLOT_MAX_NUM):
        if m_pointsInstant.pAcceSlots[i] == currentCell.cell:
            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("This sash is already selected."))
            return

    if IsOpenSafebox() or IsCubeOpen():
        return

    if not IsValidItemPosition(currentCell):
        return

    if IsOpenSafebox():
        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You can't do this while using safebox."))
        return

    if m_pointsInstant.pAcceSlots[acceSlot] != LGEMiscellaneous.DEFINECONSTANTS.WORD_MAX:
        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("This slot is already in use."))
        return

    pkItem = GetItem(currentCell)

    if pkItem is None:
        return

    if ABSORB == GetAcceWindowType():
        if acceSlot == ACCE_SLOT_RIGHT:
            if pkItem.GetType() == EItemTypes.ITEM_COSTUME:
                return

            if pkItem.GetType() != EItemTypes.ITEM_WEAPON and pkItem.GetType() != EItemTypes.ITEM_ARMOR:
                return

            if pkItem.GetType() == EItemTypes.ITEM_ARMOR and pkItem.GetSubType() != EArmorSubTypes.ARMOR_BODY:
                return

            if pkItem.GetType() == EItemTypes.ITEM_WEAPON and pkItem.GetSubType() == EWeaponSubTypes.WEAPON_ARROW or pkItem.GetSubType() == EWeaponSubTypes.WEAPON_QUIVER:
                return
        elif acceSlot == ACCE_SLOT_LEFT:
            if pkItem.GetType() != EItemTypes.ITEM_COSTUME:
                return

            if pkItem.GetSubType() != ECostumeSubTypes.COSTUME_ACCE:
                return

            if not CItemVnumHelper.IsAcceItem(pkItem.GetVnum()):
                return

            if pkItem.GetSocket(1) != 0:
                ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("This sash already absorbed an item."))
                return
    elif COMBINE == GetAcceWindowType():
        if pkItem.IsEquipped():
            return

        if pkItem.GetType() != EItemTypes.ITEM_COSTUME and pkItem.GetSubType() != ECostumeSubTypes.COSTUME_ACCE:
            return

        if acceSlot == ACCE_SLOT_LEFT and pkItem.GetSocket(0) == 25:
            ChatPacket(EChatType.CHAT_TYPE_INFO, "This sash already got the maximum degree, you cant combine it anymore.")
            return

    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'IS_SET' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
    if pkItem.GetCell() >= LGEMiscellaneous.INVENTORY_MAX_NUM and IS_SET(pkItem.GetFlag(), EItemFlag.ITEM_FLAG_IRREMOVABLE):
        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Storage> Cannot move items in safebox."))
        return

    if ((not LGEMiscellaneous.DEFINECONSTANTS.false)) == pkItem.isLocked():
        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Storages> The Item cannot be stored."))
        return

    if COMBINE == GetAcceWindowType():
        if pkItem.GetType() != EItemTypes.ITEM_COSTUME or pkItem.GetSubType() != ECostumeSubTypes.COSTUME_ACCE or not CItemVnumHelper.IsAcceItem(pkItem.GetVnum()):
            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("This item is not a sash."))
            return

        pkAcceChosen = None
        if acceSlot == ACCE_SLOT_LEFT:
            pkAcceChosen = GetItem(TItemPos(EWindows.INVENTORY, m_pointsInstant.pAcceSlots[ACCE_SLOT_RIGHT]))
        elif acceSlot == ACCE_SLOT_RIGHT:
            pkAcceChosen = GetItem(TItemPos(EWindows.INVENTORY, m_pointsInstant.pAcceSlots[ACCE_SLOT_LEFT]))

        gradeOfChosen = 0
        gradeOfNew = uint(GetAcceRefineGrade(pkItem.GetVnum()))

        if pkAcceChosen is not None:
            gradeOfChosen = uint(GetAcceRefineGrade(pkAcceChosen.GetVnum()))

            if gradeOfChosen != 0 and gradeOfNew != 0:
                if gradeOfNew != gradeOfChosen:
                    ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You can't combine sashes with a diffrent grade."))
                    return
            else:
                ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You can't combine sashes with a diffrent grade."))
                return


    m_pointsInstant.pAcceSlots[acceSlot] = currentCell.cell

    if ABSORB == GetAcceWindowType():
        if m_pointsInstant.pAcceSlots[ACCE_SLOT_RIGHT] != LGEMiscellaneous.DEFINECONSTANTS.WORD_MAX and m_pointsInstant.pAcceSlots[ACCE_SLOT_LEFT] != LGEMiscellaneous.DEFINECONSTANTS.WORD_MAX:
            pkAcce = GetItem(TItemPos(EWindows.INVENTORY, m_pointsInstant.pAcceSlots[ACCE_SLOT_LEFT]))
            pkWeaponToAbsorb = GetItem(TItemPos(EWindows.INVENTORY, m_pointsInstant.pAcceSlots[ACCE_SLOT_RIGHT]))
            pShowItem = ITEM_MANAGER.instance().CreateItem(pkAcce.GetVnum(), 1, 0, LGEMiscellaneous.DEFINECONSTANTS.false, -1, ((not LGEMiscellaneous.DEFINECONSTANTS.false)))

            pkWeaponToAbsorb.CopyAttributeTo(pShowItem)
            pShowItem.SetSocket(0, pkAcce.GetSocket(0), ((not DefineConstants.false)))
            pShowItem.SetSocket(1, int(pkWeaponToAbsorb.GetVnum()), ((not DefineConstants.false)))

            pack = packet_acce()
            pack.header = byte(LG_HEADER_GC_ACCE)
            pack.subheader = ACCE_SUBLG_HEADER_GC.ACCE_SUBLG_HEADER_GC_SET_ITEM
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            pack.size = sizeof(packet_acce) + sizeof(packet_item_set)

            pack_sub = packet_item_set()

            pack_sub.header = 0
            pack_sub.Cell = TItemPos(EWindows.ACCE_REFINE, ACCE_SLOT_RESULT)
            pack_sub.vnum = pShowItem.GetVnum()
            pack_sub.count = ushort(pShowItem.GetCount())
            pack_sub.flags = uint(pShowItem.GetFlag())
            pack_sub.anti_flags = pShowItem.GetAntiFlag()

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memcpy' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            memcpy(pack_sub.alSockets, pShowItem.GetSockets(), sizeof(pack_sub.alSockets))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memcpy' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            memcpy(pack_sub.aAttr, pShowItem.GetAttributes(), sizeof(pack_sub.aAttr))

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            GetDesc().BufferedPacket(pack, sizeof(packet_acce))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            GetDesc().BufferedPacket(NPOS, sizeof(TItemPos))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            GetDesc().Packet(pack_sub, sizeof(packet_item_set))

            ITEM_MANAGER.instance().DestroyItem(pShowItem)


    if COMBINE == GetAcceWindowType():
        if m_pointsInstant.pAcceSlots[ACCE_SLOT_LEFT] != LGEMiscellaneous.DEFINECONSTANTS.WORD_MAX:
            pkAcce = GetItem(TItemPos(EWindows.INVENTORY, m_pointsInstant.pAcceSlots[ACCE_SLOT_LEFT]))

            pack = packet_acce()
            pack.header = byte(LG_HEADER_GC_ACCE)
            pack.subheader = ACCE_SUBLG_HEADER_GC.ACCE_SUBLG_HEADER_GC_SET_ITEM
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            pack.size = sizeof(packet_acce) + sizeof(packet_item_set)

            pack_sub = packet_item_set()

            pack_sub.header = 0
            pack_sub.Cell = TItemPos(EWindows.ACCE_REFINE, ACCE_SLOT_RESULT)
            pack_sub.vnum = pkAcce.GetRefinedVnum() if pkAcce.GetRefinedVnum() != 0 else pkAcce.GetVnum()
            pack_sub.count = ushort(pkAcce.GetCount())
            pack_sub.flags = uint(pkAcce.GetFlag())
            pack_sub.anti_flags = pkAcce.GetAntiFlag()

            pShowItem = ITEM_MANAGER.instance().CreateItem(pkAcce.GetRefinedVnum() if pkAcce.GetRefinedVnum() != 0 else pkAcce.GetVnum(), 1, 0, LGEMiscellaneous.DEFINECONSTANTS.false, -1, ((not LGEMiscellaneous.DEFINECONSTANTS.false)))

            pkAcce.CopyAttributeTo(pShowItem)
            pShowItem.SetSocket(1, pkAcce.GetSocket(1), ((not DefineConstants.false)))

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memcpy' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            memcpy(pack_sub.alSockets, pShowItem.GetSockets(), sizeof(pack_sub.alSockets))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memcpy' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            memcpy(pack_sub.aAttr, pShowItem.GetAttributes(), sizeof(pack_sub.aAttr))

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            GetDesc().BufferedPacket(pack, sizeof(packet_acce))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            GetDesc().BufferedPacket(NPOS, sizeof(TItemPos))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            GetDesc().Packet(pack_sub, sizeof(packet_item_set))
            ITEM_MANAGER.instance().DestroyItem(pShowItem)


    pack = packet_acce()
    pack.header = byte(LG_HEADER_GC_ACCE)
    pack.subheader = ACCE_SUBLG_HEADER_GC.ACCE_SUBLG_HEADER_GC_SET_ITEM
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    pack.size = sizeof(packet_acce) + sizeof(packet_item_set) + sizeof(TItemPos)

    pack_sub = packet_item_set()

    pack_sub.header = 0
    pack_sub.Cell = TItemPos(EWindows.ACCE_REFINE, acceSlot)
    pack_sub.vnum = pkItem.GetVnum()
    pack_sub.count = ushort(pkItem.GetCount())
    pack_sub.flags = uint(pkItem.GetFlag())
    pack_sub.anti_flags = pkItem.GetAntiFlag()
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memcpy' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    memcpy(pack_sub.alSockets, pkItem.GetSockets(), sizeof(pack_sub.alSockets))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memcpy' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    memcpy(pack_sub.aAttr, pkItem.GetAttributes(), sizeof(pack_sub.aAttr))

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    GetDesc().BufferedPacket(pack, sizeof(packet_acce))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    GetDesc().BufferedPacket(currentCell, sizeof(TItemPos))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    GetDesc().Packet(pack_sub, sizeof(packet_item_set))

def AcceRefineCheckout(acceSlot):

    if m_pointsInstant.pAcceSlots[acceSlot] == LGEMiscellaneous.DEFINECONSTANTS.WORD_MAX:
        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("This slot is already empty."))
        return

    d = GetDesc()
    if d is None:
        return

    p = packet_acce()
    p.header = byte(LG_HEADER_GC_ACCE)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    p.size = sizeof(packet_acce) + sizeof(ushort) + sizeof(TItemPos)
    p.subheader = ACCE_SUBLG_HEADER_GC.ACCE_SUBLG_HEADER_GC_CLEAR_SLOT

    src = TItemPos(EWindows.INVENTORY, m_pointsInstant.pAcceSlots[acceSlot])

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    d.BufferedPacket(p, sizeof(p))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    d.BufferedPacket(acceSlot, sizeof(ushort))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    d.Packet(src, sizeof(TItemPos))

    m_pointsInstant.pAcceSlots[acceSlot] = LGEMiscellaneous.DEFINECONSTANTS.WORD_MAX

def AcceRefineAccept(windowType):
    if ABSORB == windowType:

        if m_pointsInstant.pAcceSlots[ACCE_SLOT_LEFT] == LGEMiscellaneous.DEFINECONSTANTS.WORD_MAX:
            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You need to insert an sash."))
            return


        if m_pointsInstant.pAcceSlots[ACCE_SLOT_RIGHT] == LGEMiscellaneous.DEFINECONSTANTS.WORD_MAX:
            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You need an item to absorb from."))
            return

        pAcce = GetItem(TItemPos(EWindows.INVENTORY, m_pointsInstant.pAcceSlots[ACCE_SLOT_LEFT]))
        pAbsorbItem = GetItem(TItemPos(EWindows.INVENTORY, m_pointsInstant.pAcceSlots[ACCE_SLOT_RIGHT]))

        if pAcce is not None and pAbsorbItem is not None:
            if not CItemVnumHelper.IsAcceItem(pAcce.GetVnum()):
                AcceRefineCheckout(ACCE_SLOT_LEFT)
                return

            TargetCell = pAcce.GetCell()
            pAcce.RemoveFromCharacter()

            pAbsorbItem.CopyAttributeTo(pAcce)
            pAcce.SetSocket(1, int(pAbsorbItem.GetVnum()), ((not DefineConstants.false)))

            pAcce.AddToCharacter(self, TItemPos(EWindows.INVENTORY, TargetCell))
            pAbsorbItem.RemoveFromCharacter()
            ITEM_MANAGER.instance().RemoveItem(pAbsorbItem, "ACCE_ABSORBED")
            AcceRefineCancel()

            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("The absorb was successful."))

    elif COMBINE == windowType:

        if m_pointsInstant.pAcceSlots[ACCE_SLOT_LEFT] == LGEMiscellaneous.DEFINECONSTANTS.WORD_MAX:
            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You need to insert an sash."))
            return
        if m_pointsInstant.pAcceSlots[ACCE_SLOT_RIGHT] == LGEMiscellaneous.DEFINECONSTANTS.WORD_MAX:
            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You need an item to absorb from."))
            return

        pBaseItem = GetItem(TItemPos(EWindows.INVENTORY, m_pointsInstant.pAcceSlots[ACCE_SLOT_LEFT]))
        pMaterialItem = GetItem(TItemPos(EWindows.INVENTORY, m_pointsInstant.pAcceSlots[ACCE_SLOT_RIGHT]))

        if pBaseItem is not None and pMaterialItem is not None:

            if not CItemVnumHelper.IsAcceItem(pBaseItem.GetVnum()):
                ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You can't use non sash items for combine."))
                return

            if not CItemVnumHelper.IsAcceItem(pMaterialItem.GetVnum()):
                ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You can't use non sash items for combine."))
                return

            if GetAcceRefineGrade(pBaseItem.GetVnum()) != GetAcceRefineGrade(pMaterialItem.GetVnum()):
                ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You can't combine sashes with a diffrent grade."))
                return


            wRefineSet = 0

            if GetAcceRefineGrade(pBaseItem.GetVnum()) == 4 and pBaseItem.GetRefineSet() == 0:
                lowerAcce = ITEM_MANAGER.instance().GetTable(pBaseItem.GetVnum() - 1)
                if lowerAcce:
                    wRefineSet = lowerAcce.wRefineSet
            else:
                wRefineSet = pBaseItem.GetRefineSet()

            prt = CRefineManager.instance().GetRefineRecipe(wRefineSet)

            if prt is None:
                return

            result_vnum = pBaseItem.GetRefinedVnum() if pBaseItem.GetRefinedVnum() != 0 else pBaseItem.GetVnum()
            cost = pBaseItem.GetProto().lldGold

            if GetGold() < cost:
                ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Not enough Yang for an advancement."))
                return

            prob = number(1, 100)

            if prob <= prt.prob:

                pkNewItem = ITEM_MANAGER.instance().CreateItem(result_vnum, 1, 0, LGEMiscellaneous.DEFINECONSTANTS.false, -1, DefineConstants.false)
                if pkNewItem:
                    if GetAcceRefineGrade(pkNewItem.GetVnum()) == 4 and pBaseItem.GetSocket(0) != 25:
                        from_ = 0
                        to = 0
                        newDrain = 0

                        if GetAcceRefineGrade(pBaseItem.GetVnum()) == 3:
                            from_ = pBaseItem.GetProto().aApplies[0].lValue + 1
                            to = 20

                            newDrain = number(from_, to)

                            if newDrain >= 19:
                                ChatPacket(EChatType.CHAT_TYPE_NOTICE, LC_TEXT("The Player %s created a sash with %d%% drain!"), GetName(), newDrain)
                        elif GetAcceRefineGrade(pBaseItem.GetVnum()) == 4:
                            from_ = pBaseItem.GetSocket(0) + 1
                            to = from_ + 4

                            newDrain = number(from_, MIN(25, to))
                            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("New drain %d"), newDrain)

                        pkNewItem.SetSocket(0, newDrain, ((not DefineConstants.false)))
                        if GetAcceRefineGrade(pBaseItem.GetVnum()) != 4:
                            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("The combine of your sash was successful."))

                    if pBaseItem.GetSocket(1) > 0:
                        pkNewItem.SetSocket(1, pBaseItem.GetSocket(1), ((not DefineConstants.false)))

                    if pBaseItem.GetAttributeCount() > 0:
                        pBaseItem.CopyAttributeTo(pkNewItem)

                    Cell = pBaseItem.GetCell()

                    ITEM_MANAGER.instance().RemoveItem(pMaterialItem, "ACCE_MAT")
                    ITEM_MANAGER.instance().RemoveItem(pBaseItem, "ACCE_BASE")

                    pkNewItem.AddToCharacter(self, TItemPos(EWindows.INVENTORY, Cell))
                    ITEM_MANAGER.instance().FlushDelayedSave(pkNewItem)

                    PayRefineFee(cost)
                    AcceRefineCancel()

                    EffectPacket(SPECIAL_EFFECT.SE_ACCE_SUCESS_ABSORB)
                else:
                    #lani_err("cannot create item %u", result_vnum)
                    AcceRefineCancel()
            else:

                ITEM_MANAGER.instance().RemoveItem(pMaterialItem, "ACCE_FAIL")
                AcceRefineCancel()

                ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Your attempt of combining was a failure."))

def AcceRefineCancel():
    pack = packet_acce()
    pack.header = byte(LG_HEADER_GC_ACCE)
    pack.subheader = ACCE_SUBLG_HEADER_GC.ACCE_SUBLG_HEADER_GC_CLEAR_ALL
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    pack.size = sizeof(packet_acce)

    srcLeft = NPOS
    srcRight = NPOS

    if m_pointsInstant.pAcceSlots[ACCE_SLOT_LEFT] != LGEMiscellaneous.DEFINECONSTANTS.WORD_MAX:
        srcLeft = TItemPos(EWindows.INVENTORY, m_pointsInstant.pAcceSlots[ACCE_SLOT_LEFT])

    if m_pointsInstant.pAcceSlots[ACCE_SLOT_RIGHT] != LGEMiscellaneous.DEFINECONSTANTS.WORD_MAX:
        srcRight = TItemPos(EWindows.INVENTORY, m_pointsInstant.pAcceSlots[ACCE_SLOT_RIGHT])

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    GetDesc().BufferedPacket(pack, sizeof(packet_acce))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    GetDesc().BufferedPacket(srcLeft, sizeof(TItemPos))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    GetDesc().Packet(srcRight, sizeof(TItemPos))
    m_pointsInstant.pAcceSlots[ACCE_SLOT_LEFT] = LGEMiscellaneous.DEFINECONSTANTS.WORD_MAX
    m_pointsInstant.pAcceSlots[ACCE_SLOT_RIGHT] = LGEMiscellaneous.DEFINECONSTANTS.WORD_MAX
    m_pointsInstant.pAcceSlots[ACCE_SLOT_RESULT] = LGEMiscellaneous.DEFINECONSTANTS.WORD_MAX

def AcceClose():
    ChatPacket(EChatType.CHAT_TYPE_COMMAND, "acce close")
