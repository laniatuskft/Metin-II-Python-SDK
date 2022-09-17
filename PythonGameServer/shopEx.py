import math

## Laniatus Games Studio Inc. | NOTE: Python has no need of forward class declarations:
#struct SShopTable
class SShopTableEx(SShopTable):

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.name = ""
        self.coinType = 0


## Laniatus Games Studio Inc. | NOTE: Python has no need of forward class declarations:
#class CGroupNode

class CShopEx(CShop):

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self._m_vec_shopTabs = []

    def Create(self, dwVnum, dwNPCVnum):
        self.m_dwVnum = dwVnum
        self.m_dwNPCVnum = dwNPCVnum
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def AddShopTable(self, shopTable):
        for it in self._m_vec_shopTabs:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to references to variables:
#ORIGINAL METINII C CODE: const SShopTableEx& _shopTable = *it;
            _shopTable = *it
            if 0 != _shopTable.dwVnum and _shopTable.dwVnum == shopTable.dwVnum:
                return LGEMiscellaneous.DEFINECONSTANTS.false
            if 0 != _shopTable.dwNPCVnum and _shopTable.dwNPCVnum == shopTable.dwVnum:
                return LGEMiscellaneous.DEFINECONSTANTS.false
        self._m_vec_shopTabs.append(shopTable)
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: virtual bool IsShopEx() const
    def IsShopEx(self):
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
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
        pack.subheader = EPacketShopSubHeaders.SHOP_SUBLG_HEADER_GC_START_EX

        pack2 = packet_shop_start_ex()

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memset(pack2, 0, sizeof(pack2))

        pack2.owner_vid = owner_vid
        pack2.shop_tab_count = len(self._m_vec_shopTabs)
        temp = str(['\0' for _ in range(8096)])
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Pointer arithmetic is detected on this variable:
#ORIGINAL METINII C CODE: char* buf = &temp[0];
        buf = temp[0]
        size = 0
        for it in self._m_vec_shopTabs:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to references to variables:
#ORIGINAL METINII C CODE: const SShopTableEx& shop_tab = *it;
            shop_tab = *it
            pack_tab = packet_shop_start_ex.TSubPacketShopTab()
            pack_tab.coin_type = shop_tab.coinType
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memcpy' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
            memcpy(pack_tab.name, shop_tab.name, LGEMiscellaneous.SHOP_TAB_NAME_MAX)

            LaniatusDefVariables = 0
            while LaniatusDefVariables < LGEMiscellaneous.SHOP_HOST_ITEM_MAX_NUM:
                pack_tab.items[LaniatusDefVariables].vnum = shop_tab.items[LaniatusDefVariables].vnum
                pack_tab.items[LaniatusDefVariables].count = shop_tab.items[LaniatusDefVariables].count
                if shop_tab.coinType == EShopCoinType.SHOP_COIN_TYPE_GOLD:
                    pack_tab.items[LaniatusDefVariables].price = shop_tab.items[LaniatusDefVariables].price
                elif shop_tab.coinType == EShopCoinType.SHOP_COIN_TYPE_SECONDARY_COIN:
                    pack_tab.items[LaniatusDefVariables].price = shop_tab.items[LaniatusDefVariables].price
                pack_tab.items[LaniatusDefVariables].price_type = shop_tab.items[LaniatusDefVariables].price_type
                pack_tab.items[LaniatusDefVariables].price_vnum = shop_tab.items[LaniatusDefVariables].price_vnum
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memcpy' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                memcpy(pack_tab.items[LaniatusDefVariables].aAttr, shop_tab.items[LaniatusDefVariables].aAttr, sizeof(pack_tab.items[LaniatusDefVariables].aAttr))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memcpy' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                memcpy(pack_tab.items[LaniatusDefVariables].alSockets, shop_tab.items[LaniatusDefVariables].alSockets, sizeof(pack_tab.items[LaniatusDefVariables].alSockets))
                LaniatusDefVariables += 1

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memcpy' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            memcpy(buf, pack_tab, sizeof(pack_tab))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            buf += sizeof(pack_tab)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            size += sizeof(pack_tab)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        pack.size = sizeof(pack) + sizeof(pack2) + size

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        ch.GetDesc().BufferedPacket(pack, sizeof(packet_shop))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        ch.GetDesc().BufferedPacket(pack2, sizeof(packet_shop_start_ex))
        ch.GetDesc().Packet(temp, size)

        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def SetPCShop(self, ch):
        return
    def IsPCShop(self):
        return LGEMiscellaneous.DEFINECONSTANTS.false
    def Buy(self, ch, pos):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        tabIdx = byte(pos / byte(LGEMiscellaneous.SHOP_HOST_ITEM_MAX_NUM))
        slotPos = math.fmod(pos, LGEMiscellaneous.SHOP_HOST_ITEM_MAX_NUM)
        if tabIdx >= self.GetTabCount():
            #sys_log(0, "ShopEx::Buy : invalid position %d : %s", pos, ch.GetName(LOCALE_LANIATUS))
            return EPacketShopSubHeaders.SHOP_SUBLG_HEADER_GC_INVALID_POS

        #sys_log(0, "ShopEx::Buy : name %s pos %d", ch.GetName(LOCALE_LANIATUS), pos)

        it = self.m_map_guest.find(ch)

        if it == self.m_map_guest.end():
            return EPacketShopSubHeaders.SHOP_SUBLG_HEADER_GC_END

        shopTab = self._m_vec_shopTabs[tabIdx]
        r_item = shopTab.items[slotPos]

        if r_item.price <= 0:
            LogManager.instance().HackLog(ch.GetAID(), ch.GetName(LOCALE_LANIATUS), "SHOP_BUY_GOLD_OVERFLOW")
            return EPacketShopSubHeaders.SHOP_SUBLG_HEADER_GC_NOT_ENOUGH_MONEY

        lldPrice = r_item.price
        if r_item.price_type == EX_GOLD:
            if (decltype(lldPrice))ch.GetGold() < lldPrice:
                return EPacketShopSubHeaders.SHOP_SUBLG_HEADER_GC_NOT_ENOUGH_MONEY
        elif r_item.price_type == EX_SECONDARY:
            if (decltype(lldPrice))ch.CountSpecifyTypeItem(EItemTypes.ITEM_SECONDARY_COIN) < lldPrice:
                return EPacketShopSubHeaders.SHOP_SUBLG_HEADER_GC_NOT_ENOUGH_MONEY_EX
        elif r_item.price_type == EX_ITEM:
            if (decltype(lldPrice))ch.CountSpecifyItem(r_item.price_vnum, -1) < lldPrice:
                return EPacketShopSubHeaders.SHOP_SUBLG_HEADER_GC_NOT_ENOUGH_ITEM
        elif r_item.price_type == EX_EXP:
            if ch.GetExp() < lldPrice:
                return EPacketShopSubHeaders.SHOP_SUBLG_HEADER_GC_NOT_ENOUGH_EXP

        item = None

        item = ITEM_MANAGER.instance().CreateItem(r_item.vnum, r_item.count, 0, DefineConstants.false, -1, DefineConstants.false)

        if item is None:
            return EPacketShopSubHeaders.SHOP_SUBLG_HEADER_GC_SOLD_OUT

        iEmptyPos = None
        # if item.IsDragonSoul():
            # iEmptyPos = ch.GetEmptyDragonSoulInventory(item)
        # else:
            iEmptyPos = ch.GetEmptyInventory(item.GetSize())

        if iEmptyPos < 0:
            #sys_log(1, "ShopEx::Buy : Inventory full : %s size %d", ch.GetName(LOCALE_LANIATUS), item.GetSize())
            ITEM_MANAGER.instance().DestroyItem(item)
            return EPacketShopSubHeaders.SHOP_SUBLG_HEADER_GC_INVENTORY_FULL

        if r_item.price_type == EX_GOLD:
            ch.PointChange(EPointTypes.LG_POINT_GOLD, -int(lldPrice), LGEMiscellaneous.DEFINECONSTANTS.false, DefineConstants.false)
        elif r_item.price_type == EX_SECONDARY:
            ch.RemoveSpecifyTypeItem(EItemTypes.ITEM_SECONDARY_COIN, uint(lldPrice))
        elif r_item.price_type == EX_ITEM:
            ch.RemoveSpecifyItem(r_item.price_vnum, uint(lldPrice), -1)
        elif r_item.price_type == EX_EXP:
            ch.PointChange(EPointTypes.LG_POINT_EXP, -int(lldPrice), LGEMiscellaneous.DEFINECONSTANTS.false, DefineConstants.false)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Only expression lambdas are converted by # Laniatus Games Studio Inc. |:
#        if ((not std::all_of(r_item.aAttr.begin(), r_item.aAttr.end(), [](TPlayerItemAttribute& s) { return (not s.bType); })))
        #        {
        #            item->SetAttributes(r_item.aAttr)
        #        }

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Only expression lambdas are converted by # Laniatus Games Studio Inc. |:
#        if ((not std::all_of(r_item.alSockets.begin(), r_item.alSockets.end(), [](int& s) { return (not s); })))
        #        {
        #            item->SetSockets(r_item.alSockets)
        #        }

        # if item.IsDragonSoul():
            # item.AddToCharacter(ch, TItemPos(EWindows.DRAGON_SOUL_INVENTORY, iEmptyPos))
        # else:
            item.AddToCharacter(ch, TItemPos(EWindows.INVENTORY, iEmptyPos))

        ITEM_MANAGER.instance().FlushDelayedSave(item)

        if item:
            #sys_log(0, "ShopEx: BUY: name %s %s(x %d):%u price %lld", ch.GetName(LOCALE_LANIATUS), item.GetName(LOCALE_LANIATUS), item.GetCount(), item.GetID(), lldPrice)

        ch.Save()

        return (EPacketShopSubHeaders.SHOP_SUBLG_HEADER_GC_OK)

    def IsSellingItem(self, itemID):
        return LGEMiscellaneous.DEFINECONSTANTS.false
    def GetTabCount(self):
        return len(self._m_vec_shopTabs)

