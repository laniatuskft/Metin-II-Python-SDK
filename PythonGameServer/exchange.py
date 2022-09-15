from enum import Enum

## Laniatus Games Studio Inc. | NOTE: Python has no need of forward class declarations:
#class CGrid

class EExchangeValues(Enum):
    EXCHANGE_ITEM_MAX_NUM = 12
    EXCHANGE_MAX_DISTANCE = 1000

class CExchange:
    def __init__(self, pOwner):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self._m_pCompany = None
        self._m_pOwner = None
        self._m_aItemPos = [TItemPos() for _ in range((int)EExchangeValues.EXCHANGE_ITEM_MAX_NUM)]
        self._m_apItems = [None for _ in range((int)EExchangeValues.EXCHANGE_ITEM_MAX_NUM)]
        self._m_abItemDisplayPos = [0 for _ in range((int)EExchangeValues.EXCHANGE_ITEM_MAX_NUM)]
        self._m_bAccept = False
        self._m_lGold = 0
        self._m_pGrid = None

        self._m_pCompany = None

        self._m_bAccept = LGEMiscellaneous.DEFINECONSTANTS.false

        i = 0
        while i < EExchangeValues.EXCHANGE_ITEM_MAX_NUM:
            self._m_apItems[i] = None
            self._m_aItemPos[i] = NPOS
            self._m_abItemDisplayPos[i] = 0
            i += 1

        self._m_lGold = 0

        self._m_pOwner = pOwner
        pOwner.SetExchange(self)

        self._m_pGrid = LG_NEW_M2 CGrid(4, 3)

    def close(self):
        LG_DEL_MEM(self._m_pGrid)

    def Accept(self, bAccept = (!LGEMiscellaneous.DefineConstants.false)):
        if self._m_bAccept == bAccept:
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        self._m_bAccept = bAccept

        if self._m_bAccept and self.GetCompany()._m_bAccept:
            iItemCount = None

            victim = self.GetCompany().GetOwner()

            self.GetOwner().SetExchangeTime()
            victim.SetExchangeTime()

            temp_ref_iItemCount = RefObject(iItemCount);
            if not self._Check(temp_ref_iItemCount):
                iItemCount = temp_ref_iItemCount.arg_value
                self.GetOwner().ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Not enough Yang or no space in the inventory."))
                victim.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("The other person does not have enough Yang or no space in the inventory left."))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There are no gotos or labels in Python:
                goto EXCHANGE_END
            else:
                iItemCount = temp_ref_iItemCount.arg_value

            if not self._CheckSpace():
                self.GetOwner().ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("The other person has no space in the inventory left."))
                victim.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("There isn't enough space in the inventory."))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There are no gotos or labels in Python:
                goto EXCHANGE_END

            temp_ref_iItemCount2 = RefObject(iItemCount);
            if not self.GetCompany()._Check(temp_ref_iItemCount2):
                iItemCount = temp_ref_iItemCount2.arg_value
                victim.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Not enough Yang or no space in the inventory."))
                self.GetOwner().ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("The other person does not have enough Yang or no space in the inventory left."))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There are no gotos or labels in Python:
                goto EXCHANGE_END
            else:
                iItemCount = temp_ref_iItemCount2.arg_value

            if not self.GetCompany()._CheckSpace():
                victim.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("The other person has no space in the inventory left."))
                self.GetOwner().ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("There isn't enough space in the inventory."))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There are no gotos or labels in Python:
                goto EXCHANGE_END

            if db_clientdesc.GetSocket() == LGEMiscellaneous.DEFINECONSTANTS.INVALID_SOCKET:
                #lani_err("Cannot use exchange feature while DB cache connection is dead.")
                victim.ChatPacket(EChatType.CHAT_TYPE_INFO, "Unknown error")
                self.GetOwner().ChatPacket(EChatType.CHAT_TYPE_INFO, "Unknown error")
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There are no gotos or labels in Python:
                goto EXCHANGE_END

            if self._Done():
                if self._m_lGold != 0:
                    self.GetOwner().Save()

                if self.GetCompany()._Done():
                    if (self.GetCompany()._m_lGold) != 0:
                        victim.Save()

                    self.GetOwner().ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("The trade with %s was successful."), victim.GetName(LOCALE_LANIATUS))
                    victim.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("The trade with %s was successful."), self.GetOwner().GetName(LOCALE_LANIATUS))

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There are no gotos or labels in Python:
            EXCHANGE_END:
            self.Cancel()
            return LGEMiscellaneous.DEFINECONSTANTS.false
        else:
            Globals.exchange_packet(self.GetOwner(), EPacketTradeSubHeaders.EXCHANGE_SUBLG_HEADER_GC_ACCEPT, ((not LGEMiscellaneous.DEFINECONSTANTS.false)),1 if self._m_bAccept else 0, NPOS, 0, NULL)
            Globals.exchange_packet(self.GetCompany().GetOwner(), EPacketTradeSubHeaders.EXCHANGE_SUBLG_HEADER_GC_ACCEPT, LGEMiscellaneous.DEFINECONSTANTS.false,1 if self._m_bAccept else 0, NPOS, 0, NULL)
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def Cancel(self):
        Globals.exchange_packet(self.GetOwner(), EPacketTradeSubHeaders.EXCHANGE_SUBLG_HEADER_GC_END, False, 0, NPOS, 0, NULL)
        self.GetOwner().SetExchange(None)

        i = 0
        while i < EExchangeValues.EXCHANGE_ITEM_MAX_NUM:
            if self._m_apItems[i]:
                self._m_apItems[i].SetExchanging(LGEMiscellaneous.DEFINECONSTANTS.false)
            i += 1

        if self.GetCompany():
            self.GetCompany().SetCompany(None)
            self.GetCompany().Cancel()

        LG_DEL_MEM(self)

    def AddGold(self, gold):
        if gold <= 0:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if self.GetOwner().GetGold() < gold:
            Globals.exchange_packet(self.GetOwner(), EPacketTradeSubHeaders.EXCHANGE_SUBLG_HEADER_GC_LESS_GOLD, False, 0, NPOS, 0, NULL)
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if self._m_lGold > 0:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        self.Accept(LGEMiscellaneous.DEFINECONSTANTS.false)
        self.GetCompany().Accept(LGEMiscellaneous.DEFINECONSTANTS.false)

        self._m_lGold = gold

        Globals.exchange_packet(self.GetOwner(), EPacketTradeSubHeaders.EXCHANGE_SUBLG_HEADER_GC_GOLD_ADD, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), self._m_lGold, NPOS, 0, NULL)
        Globals.exchange_packet(self.GetCompany().GetOwner(), EPacketTradeSubHeaders.EXCHANGE_SUBLG_HEADER_GC_GOLD_ADD, LGEMiscellaneous.DEFINECONSTANTS.false, self._m_lGold, NPOS, 0, NULL)
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def AddItem(self, item_pos, display_pos):
        assert self._m_pOwner is not None and self.GetCompany()

        if not item_pos.IsValidItemPosition():
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if item_pos.IsEquipPosition():
            return LGEMiscellaneous.DEFINECONSTANTS.false

        item = None

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if (!(item = m_pOwner->GetItem(item_pos)))
        if not(item = self._m_pOwner.GetItem(TItemPos(item_pos))):
            return LGEMiscellaneous.DEFINECONSTANTS.false

        ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'IS_SET' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
        if IS_SET(item.GetAntiFlag(), LaniatusEITMAntiFlagDcs.ITEM_ANTIFLAG_GIVE):
            self._m_pOwner.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You cannot trade this Item."))
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if ((not LGEMiscellaneous.DEFINECONSTANTS.false)) == item.isLocked():
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if item.IsExchanging():
            #sys_log(0, "EXCHANGE under exchanging")
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if not self._m_pGrid.IsEmpty(display_pos, 1, item.GetSize()):
            #sys_log(0, "EXCHANGE not empty item_pos %d %d %d", display_pos, 1, item.GetSize())
            return LGEMiscellaneous.DEFINECONSTANTS.false

        self.Accept(LGEMiscellaneous.DEFINECONSTANTS.false)
        self.GetCompany().Accept(LGEMiscellaneous.DEFINECONSTANTS.false)

        i = 0
        while i < EExchangeValues.EXCHANGE_ITEM_MAX_NUM:
            if self._m_apItems[i]:
                continue

            self._m_apItems[i] = item
## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: m_aItemPos[i] = item_pos;
            self._m_aItemPos[i].copy_from(item_pos)
            self._m_abItemDisplayPos[i] = display_pos
            self._m_pGrid.Put(display_pos, 1, item.GetSize())

            item.SetExchanging(((not LGEMiscellaneous.DEFINECONSTANTS.false)))

            Globals.exchange_packet(self._m_pOwner, EPacketTradeSubHeaders.EXCHANGE_SUBLG_HEADER_GC_ITEM_ADD, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), item.GetVnum(), TItemPos(EWindows.RESERVED_WINDOW, display_pos), item.GetCount(), item)

            Globals.exchange_packet(self.GetCompany().GetOwner(), EPacketTradeSubHeaders.EXCHANGE_SUBLG_HEADER_GC_ITEM_ADD, LGEMiscellaneous.DEFINECONSTANTS.false, item.GetVnum(), TItemPos(EWindows.RESERVED_WINDOW, display_pos), item.GetCount(), item)

            #sys_log(0, "EXCHANGE AddItem success %s pos(%d, %d) %d", item.GetName(LOCALE_LANIATUS), item_pos.window_type, item_pos.cell, display_pos)

            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
            i += 1

        return LGEMiscellaneous.DEFINECONSTANTS.false

    def RemoveItem(self, pos):
        if pos >= EExchangeValues.EXCHANGE_ITEM_MAX_NUM:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if self._m_apItems[pos] is None:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        PosOfInventory = self._m_aItemPos[pos]
        self._m_apItems[pos].SetExchanging(LGEMiscellaneous.DEFINECONSTANTS.false)

        self._m_pGrid.Get(self._m_abItemDisplayPos[pos], 1, self._m_apItems[pos].GetSize())

        Globals.exchange_packet(self.GetOwner(), EPacketTradeSubHeaders.EXCHANGE_SUBLG_HEADER_GC_ITEM_DEL, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), pos, NPOS, 0, NULL)
        Globals.exchange_packet(self.GetCompany().GetOwner(), EPacketTradeSubHeaders.EXCHANGE_SUBLG_HEADER_GC_ITEM_DEL, LGEMiscellaneous.DEFINECONSTANTS.false, pos, TItemPos(PosOfInventory), 0, NULL)

        self.Accept(LGEMiscellaneous.DEFINECONSTANTS.false)
        self.GetCompany().Accept(LGEMiscellaneous.DEFINECONSTANTS.false)

        self._m_apItems[pos] = None
        self._m_aItemPos[pos] = NPOS
        self._m_abItemDisplayPos[pos] = 0
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def GetOwner(self):
        return self._m_pOwner
    def GetCompany(self):
        return self._m_pCompany
    def GetAcceptStatus(self):
        return self._m_bAccept
    def SetCompany(self, pExchange):
        self._m_pCompany = pExchange

    def _Done(self):
        empty_pos = None
        i = None
        item = None

        victim = self.GetCompany().GetOwner()

        i = 0
        while i < EExchangeValues.EXCHANGE_ITEM_MAX_NUM:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if (!(item = m_apItems[i]))
            if not(item = self._m_apItems[i]):
                continue

            if item.IsDragonSoul():
                empty_pos = victim.GetEmptyDragonSoulInventory(item)
            else:
                empty_pos = victim.GetEmptyInventory(item.GetSize())

            if empty_pos < 0:
                #lani_err("Exchange::Done : Cannot find blank position in inventory %s <-> %s item %s", self._m_pOwner.GetName(LOCALE_LANIATUS), victim.GetName(LOCALE_LANIATUS), item.GetName(LOCALE_LANIATUS))
                continue

            assert empty_pos >= 0

            self._m_pOwner.SyncQuickslot(byte(Globals.LG_QUICKSLOT_TYPE_ITEM), byte(item.GetCell()), 255)

            item.RemoveFromCharacter()
            if item.IsDragonSoul():
                item.AddToCharacter(victim, TItemPos(EWindows.DRAGON_SOUL_INVENTORY, empty_pos))
            else:
                item.AddToCharacter(victim, TItemPos(EWindows.INVENTORY, empty_pos))
            ITEM_MANAGER.instance().FlushDelayedSave(item)

            item.SetExchanging(LGEMiscellaneous.DEFINECONSTANTS.false)
                LogManager.instance().ExchangeLogItems(self.GetOwner().GetName(LOCALE_LANIATUS), victim.GetName(LOCALE_LANIATUS), item.GetName(LOCALE_LANIATUS), item.GetID(), ushort(item.GetCount()), self.GetOwner().GetAID(), victim.GetAID())

            self._m_apItems[i] = None
            i += 1

        if self._m_lGold != 0:
            self.GetOwner().PointChange(EPointTypes.LG_POINT_GOLD, -self._m_lGold, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), DefineConstants.false)
            victim.PointChange(EPointTypes.LG_POINT_GOLD, self._m_lGold, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), DefineConstants.false)

            if self._m_lGold >= 10000000:
                LogManager.instance().ExchangeLogGold(self.GetOwner().GetName(LOCALE_LANIATUS), victim.GetName(LOCALE_LANIATUS), self._m_lGold, self.GetOwner().GetAID(), victim.GetAID())

        self._m_pGrid.Clear()
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def _Check(self, piItemCount):
        if self.GetOwner().GetGold() < self._m_lGold:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        item_count = 0

        i = 0
        while i < EExchangeValues.EXCHANGE_ITEM_MAX_NUM:
            if self._m_apItems[i] is None:
                continue

            if not self._m_aItemPos[i].IsValidItemPosition():
                return LGEMiscellaneous.DEFINECONSTANTS.false

            if self._m_apItems[i] is not self.GetOwner().GetItem(self._m_aItemPos[i]):
                return LGEMiscellaneous.DEFINECONSTANTS.false

            item_count += 1
            i += 1

        piItemCount.arg_value = item_count
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    ## Laniatus Games Studio Inc. | NOTE: This was formerly a static local variable declaration (not allowed in Python):
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    CheckSpace_s_grid1(UnnamedParameter, INVENTORY_PAGE_NUM)
    ## Laniatus Games Studio Inc. | NOTE: This was formerly a static local variable declaration (not allowed in Python):
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    CheckSpace_s_grid2(UnnamedParameter, INVENTORY_PAGE_NUM)
    ## Laniatus Games Studio Inc. | NOTE: This was formerly a static local variable declaration (not allowed in Python):
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    CheckSpace_s_grid3(UnnamedParameter, INVENTORY_PAGE_NUM)
    ## Laniatus Games Studio Inc. | NOTE: This was formerly a static local variable declaration (not allowed in Python):
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    CheckSpace_s_grid4(UnnamedParameter, INVENTORY_PAGE_NUM)
    ## Laniatus Games Studio Inc. | NOTE: This was formerly a static local variable declaration (not allowed in Python):
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    CheckSpace_s_vDSGrid(UnnamedParameter)

    def _CheckSpace(self):
        ## Laniatus Games Studio Inc. | NOTE: This static local variable declaration (not allowed in Python) has been moved just prior to the method:
        #        static CGrid s_grid1(INVENTORY_WIDTH, INVENTORY_MAX_NUM / INVENTORY_WIDTH / INVENTORY_PAGE_NUM)
        ## Laniatus Games Studio Inc. | NOTE: This static local variable declaration (not allowed in Python) has been moved just prior to the method:
        #        static CGrid s_grid2(INVENTORY_WIDTH, INVENTORY_MAX_NUM / INVENTORY_WIDTH / INVENTORY_PAGE_NUM)
        ## Laniatus Games Studio Inc. | NOTE: This static local variable declaration (not allowed in Python) has been moved just prior to the method:
        #        static CGrid s_grid3(INVENTORY_WIDTH, INVENTORY_MAX_NUM / INVENTORY_WIDTH / INVENTORY_PAGE_NUM)
        ## Laniatus Games Studio Inc. | NOTE: This static local variable declaration (not allowed in Python) has been moved just prior to the method:
        #        static CGrid s_grid4(INVENTORY_WIDTH, INVENTORY_MAX_NUM / INVENTORY_WIDTH / INVENTORY_PAGE_NUM)

        _CheckSpace_s_grid1.Clear()
        _CheckSpace_s_grid2.Clear()
        _CheckSpace_s_grid3.Clear()
        _CheckSpace_s_grid4.Clear()

        victim = self.GetCompany().GetOwner()
        item = None

        i = None

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        perPageSlotCount = LGEMiscellaneous.INVENTORY_MAX_NUM / LGEMiscellaneous.INVENTORY_PAGE_NUM

        i = 0
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        while i < LGEMiscellaneous.INVENTORY_MAX_NUM / LGEMiscellaneous.INVENTORY_PAGE_NUM:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if (!(item = victim->GetInventoryItem(i)))
            if not(item = victim.GetInventoryItem(ushort(i))):
                continue

            _CheckSpace_s_grid1.Put(i, 1, item.GetSize())
            i += 1
        i = (INVENTORY_MAX_NUM / INVENTORY_PAGE_NUM) * 1
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        while i < (LGEMiscellaneous.INVENTORY_MAX_NUM / LGEMiscellaneous.INVENTORY_PAGE_NUM) * 2:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if (!(item = victim->GetInventoryItem(i)))
            if not(item = victim.GetInventoryItem(ushort(i))):
                continue

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
            _CheckSpace_s_grid2.Put(i - (LGEMiscellaneous.INVENTORY_MAX_NUM / LGEMiscellaneous.INVENTORY_PAGE_NUM) * 1, 1, item.GetSize())
            i += 1
        i = (INVENTORY_MAX_NUM / INVENTORY_PAGE_NUM) * 2
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        while i < (LGEMiscellaneous.INVENTORY_MAX_NUM / LGEMiscellaneous.INVENTORY_PAGE_NUM) * 3:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if (!(item = victim->GetInventoryItem(i)))
            if not(item = victim.GetInventoryItem(ushort(i))):
                continue

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
            _CheckSpace_s_grid3.Put(i - (LGEMiscellaneous.INVENTORY_MAX_NUM / LGEMiscellaneous.INVENTORY_PAGE_NUM) * 2, 1, item.GetSize())
            i += 1
        i = (INVENTORY_MAX_NUM / INVENTORY_PAGE_NUM) * 3
        while i < LGEMiscellaneous.INVENTORY_MAX_NUM:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if (!(item = victim->GetInventoryItem(i)))
            if not(item = victim.GetInventoryItem(ushort(i))):
                continue

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
            _CheckSpace_s_grid4.Put(i - (LGEMiscellaneous.INVENTORY_MAX_NUM / LGEMiscellaneous.INVENTORY_PAGE_NUM) * 3, 1, item.GetSize())
            i += 1

        ## Laniatus Games Studio Inc. | NOTE: This static local variable declaration (not allowed in Python) has been moved just prior to the method:
        #        static list<ushort> s_vDSGrid(DRAGON_SOUL_INVENTORY_MAX_NUM)
        bDSInitialized = LGEMiscellaneous.DEFINECONSTANTS.false

        i = 0
        while i < EExchangeValues.EXCHANGE_ITEM_MAX_NUM:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if (!(item = m_apItems[i]))
            if not(item = self._m_apItems[i]):
                continue

            if item.IsDragonSoul():
                if not victim.DragonSoul_IsQualified():
                    return LGEMiscellaneous.DEFINECONSTANTS.false

                if not bDSInitialized:
                    bDSInitialized = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
                    victim.CopyDragonSoulItemGrid(_CheckSpace_s_vDSGrid)

                bExistEmptySpace = LGEMiscellaneous.DEFINECONSTANTS.false
                wBasePos = DSManager.instance().GetBasePosition(item)
                if wBasePos >= EDSInventoryMaxNum.DRAGON_SOUL_INVENTORY_MAX_NUM:
                    return LGEMiscellaneous.DEFINECONSTANTS.false

                i = 0
                while i < LGEMiscellaneous.DRAGON_SOUL_BOX_SIZE:
                    wPos = ushort(wBasePos + i)
                    if 0 == _CheckSpace_s_vDSGrid[wPos]:
                        bEmpty = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
                        j = 1
                        while j < item.GetSize():
                            if _CheckSpace_s_vDSGrid[wPos + j * int(LGEMiscellaneous.DRAGON_SOUL_BOX_COLUMN_NUM)]:
                                bEmpty = LGEMiscellaneous.DEFINECONSTANTS.false
                                break
                            j += 1
                        if bEmpty:
                            j = 0
                            while j < item.GetSize():
                                _CheckSpace_s_vDSGrid[wPos + j * int(LGEMiscellaneous.DRAGON_SOUL_BOX_COLUMN_NUM)] = wPos + 1
                                j += 1
                            bExistEmptySpace = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
                            break
                    if bExistEmptySpace:
                        break
                    i += 1
                if not bExistEmptySpace:
                    return LGEMiscellaneous.DEFINECONSTANTS.false
            else:
                iPos = _CheckSpace_s_grid1.FindBlank(1, item.GetSize())

                if iPos >= 0:
                    _CheckSpace_s_grid1.Put(iPos, 1, item.GetSize())
                else:
                    iPos = _CheckSpace_s_grid2.FindBlank(1, item.GetSize())

                    if iPos >= 0:
                        _CheckSpace_s_grid2.Put(iPos, 1, item.GetSize())
                    else:
                        iPos = _CheckSpace_s_grid3.FindBlank(1, item.GetSize())

                        if iPos >= 0:
                            _CheckSpace_s_grid3.Put(iPos, 1, item.GetSize())
                        else:
                            iPos = _CheckSpace_s_grid4.FindBlank(1, item.GetSize())

                            if iPos >= 0:
                                _CheckSpace_s_grid4.Put(iPos, 1, item.GetSize())
                            else:
                                return LGEMiscellaneous.DEFINECONSTANTS.false
            i += 1
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))


def ExchangeStart(victim):
    if self is victim:
        return LGEMiscellaneous.DEFINECONSTANTS.false

    if IsObserverMode():
        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You cannot trade while observing."))
        return LGEMiscellaneous.DEFINECONSTANTS.false

    if victim.IsNPC():
        return LGEMiscellaneous.DEFINECONSTANTS.false

    if IsOpenSafebox() or GetShopOwner() or GetMyShop() or IsCubeOpen() or IsAcceWindowOpen():
        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("If the Trade Window is open, you cannot trade with others."))
        return LGEMiscellaneous.DEFINECONSTANTS.false

    if victim.IsOpenSafebox() or victim.GetShopOwner() is not None or victim.GetMyShop() is not None or victim.IsCubeOpen() or victim.IsAcceWindowOpen():
        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("The other person is already trading."))
        return LGEMiscellaneous.DEFINECONSTANTS.false

    iDist = DISTANCE_APPROX(GetX() - victim.GetX(), GetY() - victim.GetY())

    if iDist >= EExchangeValues.EXCHANGE_MAX_DISTANCE:
        return LGEMiscellaneous.DEFINECONSTANTS.false

    if GetExchange():
        return LGEMiscellaneous.DEFINECONSTANTS.false

    if victim.GetExchange():
        exchange_packet(self, EPacketTradeSubHeaders.EXCHANGE_SUBLG_HEADER_GC_ALREADY, False, 0, NPOS, 0, NULL)
        return LGEMiscellaneous.DEFINECONSTANTS.false

    if victim.IsBlockMode(EBlockAction.BLOCK_EXCHANGE):
        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("The other person cancelled the Trade."))
        return LGEMiscellaneous.DEFINECONSTANTS.false

    SetExchange(LG_NEW_M2 CExchange(self))
    victim.SetExchange(LG_NEW_M2 CExchange(victim))

    victim.GetExchange().SetCompany(GetExchange())
    GetExchange().SetCompany(victim.GetExchange())

    SetExchangeTime()
    victim.SetExchangeTime()

    exchange_packet(victim, EPacketTradeSubHeaders.EXCHANGE_SUBLG_HEADER_GC_START, False, GetVID(), NPOS, 0, NULL)
    exchange_packet(self, EPacketTradeSubHeaders.EXCHANGE_SUBLG_HEADER_GC_START, False, victim.GetVID(), NPOS, 0, NULL)

    return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
