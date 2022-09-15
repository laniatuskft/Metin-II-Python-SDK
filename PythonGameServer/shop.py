class CShop:
    class shop_item:

        def __init__(self):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.vnum = 0
            self.price = 0
            self.count = 0
            self.pkItem = None
            self.itemid = 0
            self.alSockets = [0 for _ in range((int)EItemMisc.LG_ITEM_SOCKET_MAX_NUM)]
            self.aAttr = [TPlayerItemAttribute() for _ in range((int)EItemMisc.ITEM_ATTRIBUTE_MAX_NUM)]
            self.price_type = 0
            self.price_vnum = 0

            self.vnum = 0
            self.price = 0
            self.count = 0
            self.itemid = 0
            self.pkItem = None
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            self.price_type = 1, self.price_vnum = 0, memset(self.alSockets, 0, sizeof(self.alSockets))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            memset(self.aAttr, 0, sizeof(self.aAttr))

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.m_dwVnum = 0
        self.m_dwNPCVnum = 0
        self.m_pGrid = None
        self.m_map_guest = _boost_func_of_void.unordered_map()
        self.m_itemVector = []
        self.m_pkPC = None

        self.m_dwVnum = 0
        self.m_dwNPCVnum = 0
        self.m_pkPC = None
        self.m_pGrid = LG_NEW_M2 CGrid(5, 9)

    def close(self):
        pack = packet_shop()

        pack.header = byte(Globals.LG_HEADER_GC_SHOP)
        pack.subheader = EPacketShopSubHeaders.SHOP_SUBLG_HEADER_GC_END
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        pack.size = sizeof(packet_shop)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Broadcast(pack, sizeof(pack))

        it = self.m_map_guest.begin()

        while it is not self.m_map_guest.end():
            ch = it.first
            ch.SetShop(None)
            it += 1

        LG_DEL_MEM(self.m_pGrid)

    def Create(self, dwVnum, dwNPCVnum, pTable):
        #sys_log(0, "SHOP #%d (Shopkeeper %d)", dwVnum, dwNPCVnum)

        self.m_dwVnum = dwVnum
        self.m_dwNPCVnum = dwNPCVnum

        wItemCount = None

        wItemCount = 0
        while wItemCount < LGEMiscellaneous.SHOP_HOST_ITEM_MAX_NUM:
            if 0 == (pTable + wItemCount).vnum:
                break
            wItemCount += 1

        self.SetShopItems(pTable, wItemCount)
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Pointer arithmetic is detected on the parameter 'pTable':
#ORIGINAL METINII C CODE: void SetShopItems(SShopItemTable * pTable, ushort wItemCount)
    def SetShopItems(self, pTable, wItemCount):
        if wItemCount > LGEMiscellaneous.SHOP_HOST_ITEM_MAX_NUM:
            return

        self.m_pGrid.Clear()

        self.m_itemVector.resize(LGEMiscellaneous.SHOP_HOST_ITEM_MAX_NUM)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memset(self.m_itemVector[0], 0, sizeof(SHOP_ITEM) * len(self.m_itemVector))

        for i in range(0, wItemCount):
            pkItem = None
            item_table = None

            if self.m_pkPC:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
#ORIGINAL METINII C CODE: pkItem = m_pkPC->GetItem(pTable->pos);
                pkItem = self.m_pkPC.GetItem(SItemPos(pTable.pos))

                if pkItem is None:
                    #lani_err("cannot find item on pos (%d, %d) (name: %s)", pTable.pos.window_type, pTable.pos.cell, self.m_pkPC.GetName(LOCALE_LANIATUS))
                    continue

                item_table = pkItem.GetProto()
            else:
                if pTable.vnum == 0:
                    continue

                item_table = ITEM_MANAGER.instance().GetTable(pTable.vnum)

            if item_table is None:
                #lani_err("Shop: no item table by item vnum #%d", pTable.vnum)
                continue

            iPos = None

            if self.IsPCShop():
                #sys_log(0, "MyShop: use position %d", pTable.display_pos)
                iPos = pTable.display_pos
            else:
                iPos = self.m_pGrid.FindBlank(1, item_table.bSize)

            if iPos < 0:
                #lani_err("not enough shop window")
                continue

            if not self.m_pGrid.IsEmpty(iPos, 1, item_table.bSize):
                if self.IsPCShop():
                    #lani_err("not empty position for pc shop %s[%d]", self.m_pkPC.GetName(LOCALE_LANIATUS), self.m_pkPC.GetPlayerID())
                else:
                    #lani_err("not empty position for npc shop")
                continue

            self.m_pGrid.Put(iPos, 1, item_table.bSize)

            item = self.m_itemVector[iPos]

            item.pkItem = pkItem
            item.itemid = 0

            if item.pkItem:
                item.vnum = pkItem.GetVnum()
                item.count = pkItem.GetCount()
                item.price = pTable.price
                item.itemid = pkItem.GetID()
            else:
                item.vnum = pTable.vnum
                item.count = pTable.count

                ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'IS_SET' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
                if IS_SET(item_table.dwFlags, EItemFlag.ITEM_FLAG_COUNT_PER_1GOLD):
                    if item_table.lldGold == 0:
                        item.price = item.count
                    else:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
                        item.price = item.count / item_table.lldGold
                else:
                    item.price = item_table.lldGold * item.count

            name = str(['\0' for _ in range(36)])
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            snprintf(name, sizeof(name), "%-20s(#%-5d) (x %d)", item_table.szName, int(item.vnum), item.count)

            #sys_log(0, "SHOP_ITEM: %-36s PRICE %-5d", name, item.price)
            pTable += 1

    def SetPCShop(self, ch):
        self.m_pkPC = ch

    def IsPCShop(self):
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false)) if self.m_pkPC is not None else LGEMiscellaneous.DEFINECONSTANTS.false
## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: virtual bool IsShopEx() const
    def IsShopEx(self):
        return LGEMiscellaneous.DEFINECONSTANTS.false
    def AddGuest(self, ch, owner_vid, bOtherEmpire):
        if ch is None:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if ch.GetExchange():
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if ch.GetShop():
            return LGEMiscellaneous.DEFINECONSTANTS.false

        ch.SetShop(self)

        self.m_map_guest.insert(GuestMapType.value_type(ch, bOtherEmpire))

        pack = packet_shop()

        pack.header = byte(Globals.LG_HEADER_GC_SHOP)
        pack.subheader = EPacketShopSubHeaders.SHOP_SUBLG_HEADER_GC_START

        pack2 = packet_shop_start()

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memset(pack2, 0, sizeof(pack2))
        pack2.owner_vid = owner_vid

        i = 0
        while i < len(self.m_itemVector) and i < LGEMiscellaneous.SHOP_HOST_ITEM_MAX_NUM:
            item = self.m_itemVector[i]

            if item.vnum == 70024 or item.vnum == 70035:
                continue

            if self.m_pkPC is not None and not item.pkItem:
                continue

            pack2.items[i].vnum = item.vnum
            pack2.items[i].price = item.price
            pack2.items[i].count = item.count
            pack2.items[i].price_type = 1
            pack2.items[i].price_vnum = 0

            if item.pkItem:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memcpy' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                memcpy(pack2.items[i].alSockets, item.pkItem.GetSockets(), sizeof(pack2.items[i].alSockets))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memcpy' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                memcpy(pack2.items[i].aAttr, item.pkItem.GetAttributes(), sizeof(pack2.items[i].aAttr))
            i += 1

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        pack.size = sizeof(pack) + sizeof(pack2)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        ch.GetDesc().BufferedPacket(pack, sizeof(packet_shop))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        ch.GetDesc().Packet(pack2, sizeof(packet_shop_start))
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def RemoveGuest(self, ch):
        if ch.GetShop() is not self:
            return

        self.m_map_guest.erase(ch)
        ch.SetShop(None)

        pack = packet_shop()

        pack.header = byte(Globals.LG_HEADER_GC_SHOP)
        pack.subheader = EPacketShopSubHeaders.SHOP_SUBLG_HEADER_GC_END
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        pack.size = sizeof(packet_shop)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        ch.GetDesc().Packet(pack, sizeof(pack))

    def Buy(self, ch, pos):
        if pos >= len(self.m_itemVector):
            #sys_log(0, "Shop::Buy : invalid position %d : %s", pos, ch.GetName(LOCALE_LANIATUS))
            return EPacketShopSubHeaders.SHOP_SUBLG_HEADER_GC_INVALID_POS

        #sys_log(0, "Shop::Buy : name %s pos %d", ch.GetName(LOCALE_LANIATUS), pos)

        it = self.m_map_guest.find(ch)

        if it == self.m_map_guest.end():
            return EPacketShopSubHeaders.SHOP_SUBLG_HEADER_GC_END

        r_item = self.m_itemVector[pos]

        if r_item.price < 0:
            LogManager.instance().HackLog(ch.GetAID(), ch.GetName(LOCALE_LANIATUS), "SHOP_BUY_GOLD_OVERFLOW")
            return EPacketShopSubHeaders.SHOP_SUBLG_HEADER_GC_NOT_ENOUGH_MONEY

        pkSelectedItem = ITEM_MANAGER.instance().Find(r_item.itemid)

        if self.IsPCShop() and (pkSelectedItem is None or pkSelectedItem.GetOwner() is not self.m_pkPC):
            return EPacketShopSubHeaders.SHOP_SUBLG_HEADER_GC_SOLDOUT

        lldPrice = r_item.price

        if ch.GetGold() < lldPrice:
            #sys_log(1, "Shop::Buy : Not enough money : %s has %d, price %lld", ch.GetName(LOCALE_LANIATUS), ch.GetGold(), lldPrice)
            return EPacketShopSubHeaders.SHOP_SUBLG_HEADER_GC_NOT_ENOUGH_MONEY

        item = None

        if self.m_pkPC:
            item = r_item.pkItem
        else:
            item = ITEM_MANAGER.instance().CreateItem(r_item.vnum, r_item.count, 0, DefineConstants.false, -1, DefineConstants.false)

        if item is None:
            return EPacketShopSubHeaders.SHOP_SUBLG_HEADER_GC_SOLD_OUT

        if self.m_pkPC is None:
            if item.GetVnum() == 70024 or item.GetVnum() == 70035:
                return EPacketShopSubHeaders.SHOP_SUBLG_HEADER_GC_END

        iEmptyPos = None
        # if item.IsDragonSoul():
            # iEmptyPos = ch.GetEmptyDragonSoulInventory(item)
        # else:
            iEmptyPos = ch.GetEmptyInventory(item.GetSize())

        if iEmptyPos < 0:
            if self.m_pkPC:
                #sys_log(1, "Shop::Buy at PC Shop : Inventory full : %s size %d", ch.GetName(LOCALE_LANIATUS), item.GetSize())
                return EPacketShopSubHeaders.SHOP_SUBLG_HEADER_GC_INVENTORY_FULL
            else:
                #sys_log(1, "Shop::Buy : Inventory full : %s size %d", ch.GetName(LOCALE_LANIATUS), item.GetSize())
                ITEM_MANAGER.instance().DestroyItem(item)
                return EPacketShopSubHeaders.SHOP_SUBLG_HEADER_GC_INVENTORY_FULL

        ch.PointChange(EPointTypes.LG_POINT_GOLD, -lldPrice, LGEMiscellaneous.DEFINECONSTANTS.false, DefineConstants.false)

        iVal = 0

        iVal = quest.CQuestManager.instance().GetEventFlag("personal_shop")

        if 0 < iVal:
            if iVal > 100:
                iVal = 100
        else:
            iVal = 0

        if self.m_pkPC:
            self.m_pkPC.SyncQuickslot(byte(Globals.LG_QUICKSLOT_TYPE_ITEM), byte(item.GetCell()), 255)

            item.RemoveFromCharacter()
            # if item.IsDragonSoul():
                # item.AddToCharacter(ch, TItemPos(EWindows.DRAGON_SOUL_INVENTORY, iEmptyPos))
            # else:
                item.AddToCharacter(ch, TItemPos(EWindows.INVENTORY, iEmptyPos))
            ITEM_MANAGER.instance().FlushDelayedSave(item)

            r_item.pkItem = None
            self.BroadcastUpdateItem(pos)

            self.m_pkPC.PointChange(EPointTypes.LG_POINT_GOLD, lldPrice, LGEMiscellaneous.DEFINECONSTANTS.false, DefineConstants.false)

            if iVal > 0:
                self.m_pkPC.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("%d%% sales tax deducted."), iVal)
        else:
            # if item.IsDragonSoul():
                # item.AddToCharacter(ch, TItemPos(EWindows.DRAGON_SOUL_INVENTORY, iEmptyPos))
            # else:
                item.AddToCharacter(ch, TItemPos(EWindows.INVENTORY, iEmptyPos))

            ITEM_MANAGER.instance().FlushDelayedSave(item)


        if item:
            #sys_log(0, "SHOP: BUY: name %s %s(x %d):%u price %u", ch.GetName(LOCALE_LANIATUS), item.GetName(LOCALE_LANIATUS), item.GetCount(), item.GetID(), lldPrice)

        ch.Save()

        return (EPacketShopSubHeaders.SHOP_SUBLG_HEADER_GC_OK)

    def BroadcastUpdateItem(self, pos):
        pack = packet_shop()
        pack2 = packet_shop_update_item()

        buf = TEMP_BUFFER(8192, DefineConstants.false)

        pack.header = byte(Globals.LG_HEADER_GC_SHOP)
        pack.subheader = EPacketShopSubHeaders.SHOP_SUBLG_HEADER_GC_UPDATE_ITEM
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        pack.size = sizeof(pack) + sizeof(pack2)

        pack2.pos = pos

        if self.m_pkPC is not None and self.m_itemVector[pos].pkItem is None:
            pack2.item.vnum = 0
        else:
            pack2.item.vnum = self.m_itemVector[pos].vnum
            if self.m_itemVector[pos].pkItem:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memcpy' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                memcpy(pack2.item.alSockets, self.m_itemVector[pos].pkItem.GetSockets(), sizeof(pack2.item.alSockets))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memcpy' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                memcpy(pack2.item.aAttr, self.m_itemVector[pos].pkItem.GetAttributes(), sizeof(pack2.item.aAttr))
            else:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                memset(pack2.item.alSockets, 0, sizeof(pack2.item.alSockets))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                memset(pack2.item.aAttr, 0, sizeof(pack2.item.aAttr))

        pack2.item.price = self.m_itemVector[pos].price
        pack2.item.count = self.m_itemVector[pos].count

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        buf.write(pack, sizeof(pack))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        buf.write(pack2, sizeof(pack2))

        self.Broadcast(buf.read_peek(), buf.size())

    def GetNumberByVnum(self, dwVnum):
        itemNumber = 0

        i = 0
        while i < len(self.m_itemVector) and i < LGEMiscellaneous.SHOP_HOST_ITEM_MAX_NUM:
            item = self.m_itemVector[i]

            if item.vnum == dwVnum:
                itemNumber += item.count
            i += 1

        return itemNumber

    def IsSellingItem(self, itemID):
        isSelling = LGEMiscellaneous.DEFINECONSTANTS.false

        i = 0
        while i < len(self.m_itemVector) and i < LGEMiscellaneous.SHOP_HOST_ITEM_MAX_NUM:
            if self.m_itemVector[i].itemid == itemID:
                isSelling = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
                break
            i += 1

        return isSelling


    def GetVnum(self):
        return self.m_dwVnum
    def GetNPCVnum(self):
        return self.m_dwNPCVnum

    def Broadcast(self, data, bytes):
        #sys_log(1, "Shop::Broadcast %p %d", data, bytes)

        it = self.m_map_guest.begin()

        while it is not self.m_map_guest.end():
            ch = it.first

            if ch.GetDesc():
                ch.GetDesc().Packet(data, bytes)

            it += 1

