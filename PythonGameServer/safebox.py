## Laniatus Games Studio Inc. | NOTE: Python has no need of forward class declarations:
#class CHARACTER
## Laniatus Games Studio Inc. | NOTE: Python has no need of forward class declarations:
#class CItem
## Laniatus Games Studio Inc. | NOTE: Python has no need of forward class declarations:
#class CGrid

class CSafebox:
    def __init__(self, pkChrOwner, iSize, lldGold):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.m_pkChrOwner = None
        self.m_pkItems = [None for _ in range((int)LGEMiscellaneous.DEFINECONSTANTS.SAFEBOX_MAX_NUM)]
        self.m_pkGrid = None
        self.m_iSize = 0
        self.m_lGold = 0
        self.m_bWindowMode = 0

        self.m_pkChrOwner = pkChrOwner
        self.m_iSize = iSize
        self.m_lGold = lldGold
        assert self.m_pkChrOwner is not None
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memset(self.m_pkItems, 0, sizeof(self.m_pkItems))

        if self.m_iSize != 0:
            self.m_pkGrid = LG_NEW_M2 CGrid(5, self.m_iSize)
        else:
            self.m_pkGrid = None

        self.m_bWindowMode = EWindows.SAFEBOX

    def close(self):
        self.__Destroy()

    def Add(self, dwPos, pkItem):
        if not self.IsValidPosition(dwPos):
            #lani_err("SAFEBOX: item on wrong position at %d (size of grid = %d)", dwPos, self.m_pkGrid.GetSize())
            return LGEMiscellaneous.DEFINECONSTANTS.false

        pkItem.SetWindow(self.m_bWindowMode)
        pkItem.SetCell(self.m_pkChrOwner, ushort(dwPos))
        pkItem.Save()
        ITEM_MANAGER.instance().FlushDelayedSave(pkItem)

        self.m_pkGrid.Put(int(dwPos), 1, pkItem.GetSize())
        self.m_pkItems[dwPos] = pkItem

        pack = packet_item_set()

        pack.header = byte(Globals.LG_HEADER_GC_SAFEBOX_SET) if self.m_bWindowMode == EWindows.SAFEBOX else byte(Globals.LG_HEADER_GC_MALL_SET)
        pack.Cell = TItemPos(self.m_bWindowMode, dwPos)
        pack.vnum = pkItem.GetVnum()
        pack.count = ushort(pkItem.GetCount())
        pack.flags = uint(pkItem.GetFlag())
        pack.anti_flags = pkItem.GetAntiFlag()
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memcpy' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memcpy(pack.alSockets, pkItem.GetSockets(), sizeof(pack.alSockets))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memcpy' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memcpy(pack.aAttr, pkItem.GetAttributes(), sizeof(pack.aAttr))

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.m_pkChrOwner.GetDesc().Packet(pack, sizeof(pack))
        #sys_log(1, "SAFEBOX: ADD %s %s count %d", self.m_pkChrOwner.GetName(LOCALE_LANIATUS), pkItem.GetName(LOCALE_LANIATUS), pkItem.GetCount())
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def Get(self, dwPos):
        if dwPos >= self.m_pkGrid.GetSize():
            return None

        return self.m_pkItems[dwPos]

    def Remove(self, dwPos):
        pkItem = self.Get(dwPos)

        if pkItem is None:
            return None

        if self.m_pkGrid is None:
            #lani_err("Safebox::Remove : nil grid")
        else:
            self.m_pkGrid.Get(int(dwPos), 1, pkItem.GetSize())

        pkItem.RemoveFromCharacter()

        self.m_pkItems[dwPos] = None

        pack = packet_item_del()

        pack.header = byte(Globals.LG_HEADER_GC_SAFEBOX_DEL) if self.m_bWindowMode == EWindows.SAFEBOX else byte(Globals.LG_HEADER_GC_MALL_DEL)
        pack.pos = byte(dwPos)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.m_pkChrOwner.GetDesc().Packet(pack, sizeof(pack))
        #sys_log(1, "SAFEBOX: REMOVE %s %s count %d", self.m_pkChrOwner.GetName(LOCALE_LANIATUS), pkItem.GetName(LOCALE_LANIATUS), pkItem.GetCount())
        return pkItem

    def ChangeSize(self, iSize):
        if self.m_iSize >= iSize:
            return

        self.m_iSize = iSize

        pkOldGrid = self.m_pkGrid

        if pkOldGrid:
            self.m_pkGrid = LG_NEW_M2 CGrid(pkOldGrid, 5, self.m_iSize)
            if pkOldGrid is not None:
                pkOldGrid.close()
        else:
            self.m_pkGrid = LG_NEW_M2 CGrid(5, self.m_iSize)

    def MoveItem(self, bCell, bDestCell, count):
        item = None

        max_position = 5 * self.m_iSize

        if bCell >= max_position or bDestCell >= max_position:
            return LGEMiscellaneous.DEFINECONSTANTS.false

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if (!(item = GetItem(bCell)))
        if not(item = self.GetItem(bCell)):
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if item.IsExchanging():
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if item.GetCount() < count:
            return LGEMiscellaneous.DEFINECONSTANTS.false

            item2 = None

            ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'IS_SET' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
            ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'IS_SET' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((item2 = GetItem(bDestCell)) && item != item2 && item2->IsStackable() && !IS_SET(item2->GetAntiFlag(), ITEM_ANTIFLAG_STACK) && item2->GetVnum() == item->GetVnum())
            if (item2 = self.GetItem(bDestCell)) and item is not item2 and item2.IsStackable() and (not IS_SET(item2.GetAntiFlag(), LaniatusEITMAntiFlagDcs.ITEM_ANTIFLAG_STACK)) and item2.GetVnum() == item.GetVnum():
                LaniatusDefVariables = 0
                while LaniatusDefVariables < EItemMisc.LG_ITEM_SOCKET_MAX_NUM:
                    if item2.GetSocket(i) != item.GetSocket(i):
                        return LGEMiscellaneous.DEFINECONSTANTS.false
                    LaniatusDefVariables += 1

                if count == 0:
                    count = ushort(item.GetCount())

                count = MIN(EItemMisc.ITEM_MAX_COUNT - item2.GetCount(), count)

                if item.GetCount() >= count:
                    self.Remove(bCell)

                item.SetCount(item.GetCount() - count)
                item2.SetCount(item2.GetCount() + count)

                #sys_log(1, "SAFEBOX: STACK %s %d -> %d %s count %d", self.m_pkChrOwner.GetName(LOCALE_LANIATUS), bCell, bDestCell, item2.GetName(LOCALE_LANIATUS), item2.GetCount())
                return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

            if not self.IsEmpty(bDestCell, item.GetSize()):
                return LGEMiscellaneous.DEFINECONSTANTS.false

            self.m_pkGrid.Get(bCell, 1, item.GetSize())

            if not self.m_pkGrid.Put(bDestCell, 1, item.GetSize()):
                self.m_pkGrid.Put(bCell, 1, item.GetSize())
                return LGEMiscellaneous.DEFINECONSTANTS.false
            else:
                self.m_pkGrid.Get(bDestCell, 1, item.GetSize())
                self.m_pkGrid.Put(bCell, 1, item.GetSize())

            #sys_log(1, "SAFEBOX: MOVE %s %d -> %d %s count %d", self.m_pkChrOwner.GetName(LOCALE_LANIATUS), bCell, bDestCell, item.GetName(LOCALE_LANIATUS), item.GetCount())

            self.Remove(bCell)
            self.Add(bDestCell, item)

        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def GetItem(self, bCell):
        if bCell >= 5 * self.m_iSize:
            #lani_err("CHARACTER::GetItem: invalid item cell %d", bCell)
            return None

        return self.m_pkItems[bCell]

    def Save(self):
        t = SSafeboxTable()

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memset(t, 0, sizeof(SSafeboxTable))

        t.dwID = self.m_pkChrOwner.GetDesc().GetAccountTable().id
        t.lldGold = self.m_lGold

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        db_clientdesc.DBPacket(Globals.LG_HEADER_GD_SAFEBOX_SAVE, 0, t, sizeof(SSafeboxTable))
        #sys_log(1, "SAFEBOX: SAVE %s", self.m_pkChrOwner.GetName(LOCALE_LANIATUS))

    def IsEmpty(self, dwPos, bSize):
        if self.m_pkGrid is None:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        return self.m_pkGrid.IsEmpty(int(dwPos), 1, bSize)

    def IsValidPosition(self, dwPos):
        if self.m_pkGrid is None:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if dwPos >= self.m_pkGrid.GetSize():
            return LGEMiscellaneous.DEFINECONSTANTS.false

        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def SetWindowMode(self, bMode):
        self.m_bWindowMode = bMode

    def __Destroy(self):
        for LaniatusDefVariables in range(0, LGEMiscellaneous.DEFINECONSTANTS.SAFEBOX_MAX_NUM):
            if self.m_pkItems[LaniatusDefVariables]:
                self.m_pkItems[LaniatusDefVariables].SetSkipSave(((not LGEMiscellaneous.DEFINECONSTANTS.false)))
                ITEM_MANAGER.instance().FlushDelayedSave(self.m_pkItems[LaniatusDefVariables])

                ITEM_MANAGER.instance().DestroyItem(self.m_pkItems[LaniatusDefVariables].RemoveFromCharacter())
                self.m_pkItems[LaniatusDefVariables] = None

        if self.m_pkGrid:
            LG_DEL_MEM(self.m_pkGrid)
            self.m_pkGrid = None


