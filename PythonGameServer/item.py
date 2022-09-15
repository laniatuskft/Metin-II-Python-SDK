import math

class CItem(CEntity):
    def EncodeInsertPacket(self, ent):
        d = None

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if (!(d = ent->GetDesc()))
        if not(d = ent.GetDesc()):
            return

        c_pos = self.GetXYZ()

        pack = packet_item_ground_add()

        pack.bHeader = byte(Globals.LG_HEADER_GC_ITEM_GROUND_ADD)
        pack.x = c_pos.x
        pack.y = c_pos.y
        pack.z = c_pos.z
        pack.dwVnum = self.GetVnum()
        pack.dwVID = self._m_dwVID

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        d.Packet(pack, sizeof(pack))

        if self._m_pkOwnershipEvent is not None:
            info = if isinstance(self._m_pkOwnershipEvent.info, item_event_info) else None

            if info is None:
                #lani_err("CItem::EncodeInsertPacket> <Factor> Null pointer")
                return

            p = packet_item_ownership()

            p.bHeader = byte(Globals.LG_HEADER_GC_ITEM_OWNERSHIP)
            p.dwVID = self._m_dwVID
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            strncpy_s(p.szName, sizeof(p.szName), info.szOwnerName, _TRUNCATE)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            d.Packet(p, sizeof(packet_item_ownership))

    def EncodeRemovePacket(self, ent):
        d = None

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if (!(d = ent->GetDesc()))
        if not(d = ent.GetDesc()):
            return

        pack = packet_item_ground_del()

        pack.bHeader = byte(Globals.LG_HEADER_GC_ITEM_GROUND_DEL)
        pack.dwVID = self._m_dwVID

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        d.Packet(pack, sizeof(pack))
        #sys_log(2, "Item::EncodeRemovePacket %s to %s", self.GetName(LOCALE_LANIATUS), (ent).GetName())

    def __init__(self, dwVnum):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self._m_pProto = None
        self._m_dwVnum = 0
        self._m_pOwner = None
        self._m_bWindow = 0
        self._m_dwID = 0
        self._m_bEquipped = False
        self._m_dwVID = 0
        self._m_wCell = 0
        self._m_dwCount = 0
        self._m_lFlag = 0
        self._m_dwLastOwnerPID = 0
        self._m_bExchanging = False
        self._m_alSockets = [0 for _ in range((int)EItemMisc.LG_ITEM_SOCKET_MAX_NUM)]
        self._m_aAttr = [TPlayerItemAttribute() for _ in range((int)EItemMisc.ITEM_ATTRIBUTE_MAX_NUM)]
        self._m_pkDestroyEvent = _boost_func_of_void.intrusive_ptr()
        self._m_pkExpireEvent = _boost_func_of_void.intrusive_ptr()
        self._m_pkUniqueExpireEvent = _boost_func_of_void.intrusive_ptr()
        self._m_pkTimerBasedOnWearExpireEvent = _boost_func_of_void.intrusive_ptr()
        self._m_pkRealTimeExpireEvent = _boost_func_of_void.intrusive_ptr()
        self._m_pkAccessorySocketExpireEvent = _boost_func_of_void.intrusive_ptr()
        self._m_pkOwnershipEvent = _boost_func_of_void.intrusive_ptr()
        self._m_dwOwnershipPID = 0
        self._m_bSkipSave = False
        self._m_isLocked = False
        self._m_dwMaskVnum = 0
        self._m_dwSIGVnum = 0

        self._m_dwVnum = dwVnum
        self._m_bWindow = 0
        self._m_dwID = 0
        self._m_bEquipped = LGEMiscellaneous.DEFINECONSTANTS.false
        self._m_dwVID = 0
        self._m_wCell = 0
        self._m_dwCount = 0
        self._m_lFlag = 0
        self._m_dwLastOwnerPID = 0
        self._m_bExchanging = LGEMiscellaneous.DEFINECONSTANTS.false
        self._m_pkDestroyEvent = None
        self._m_pkUniqueExpireEvent = None
        self._m_pkTimerBasedOnWearExpireEvent = None
        self._m_pkRealTimeExpireEvent = None
        self._m_pkExpireEvent = None
        self._m_pkAccessorySocketExpireEvent = None
        self._m_pkOwnershipEvent = None
        self._m_dwOwnershipPID = 0
        self._m_bSkipSave = LGEMiscellaneous.DEFINECONSTANTS.false
        self._m_isLocked = LGEMiscellaneous.DEFINECONSTANTS.false
        self._m_dwMaskVnum = 0
        self._m_dwSIGVnum = 0
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memset(self._m_alSockets, 0, sizeof(self._m_alSockets))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memset(self._m_aAttr, 0, sizeof(self._m_aAttr))

    def close(self):
        self.Destroy()

    def GetLevelLimit(self):
        i = 0
        while i < EItemMisc.ITEM_LIMIT_MAX_NUM:
            if self._m_pProto.aLimits[i].bType == ELimitTypes.LIMIT_LEVEL:
                return self._m_pProto.aLimits[i].lValue
            i += 1
        return 0

    def CheckItemUseLevel(self, nLevel):
        i = 0
        while i < EItemMisc.ITEM_LIMIT_MAX_NUM:
            if self._m_pProto.aLimits[i].bType == ELimitTypes.LIMIT_LEVEL:
                if self._m_pProto.aLimits[i].lValue > nLevel:
                    return LGEMiscellaneous.DEFINECONSTANTS.false
                else:
                    return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
            i += 1
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def FindApplyValue(self, bApplyType):
        if self._m_pProto is None:
            return 0

        i = 0
        while i < EItemMisc.ITEM_APPLY_MAX_NUM:
            if self._m_pProto.aApplies[i].bType == bApplyType:
                return self._m_pProto.aApplies[i].lValue
            i += 1

        return 0

    def IsStackable(self):
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false)) if (self.GetFlag() & int(EItemFlag.ITEM_FLAG_STACKABLE)) != 0 ) else LGEMiscellaneous.DEFINECONSTANTS.false
    def Initialize(self):
        super().Initialize(EEntityTypes.ENTITY_ITEM)

        self._m_bWindow = EWindows.RESERVED_WINDOW
        self._m_pOwner = None
        self._m_dwID = 0
        self._m_bEquipped = LGEMiscellaneous.DEFINECONSTANTS.false
        self._m_dwVID = self._m_wCell = ushort(self._m_dwCount) = self._m_lFlag = 0
        self._m_pProto = None
        self._m_bExchanging = LGEMiscellaneous.DEFINECONSTANTS.false
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memset(self._m_alSockets, 0, sizeof(self._m_alSockets))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memset(self._m_aAttr, 0, sizeof(self._m_aAttr))

        self._m_pkDestroyEvent = None
        self._m_pkOwnershipEvent = None
        self._m_dwOwnershipPID = 0
        self._m_pkUniqueExpireEvent = None
        self._m_pkTimerBasedOnWearExpireEvent = None
        self._m_pkRealTimeExpireEvent = None

        self._m_pkAccessorySocketExpireEvent = None

        self._m_bSkipSave = LGEMiscellaneous.DEFINECONSTANTS.false
        self._m_dwLastOwnerPID = 0

    def Destroy(self):
        event_cancel(self._m_pkDestroyEvent)
        event_cancel(self._m_pkOwnershipEvent)
        event_cancel(self._m_pkUniqueExpireEvent)
        event_cancel(self._m_pkTimerBasedOnWearExpireEvent)
        event_cancel(self._m_pkRealTimeExpireEvent)
        event_cancel(self._m_pkAccessorySocketExpireEvent)

        super().Destroy()

        if self.GetSectree():
            self.GetSectree().RemoveEntity(self)

    def Save(self):
        if self._m_bSkipSave:
            return

        ITEM_MANAGER.instance().DelayedSave(self)

    def SetWindow(self, b):
        self._m_bWindow = b
    def GetWindow(self):
        return self._m_bWindow
    def SetID(self, id):
        self._m_dwID = id
    def GetID(self):
        return self._m_dwID
    def SetProto(self, table):
        assert table is not None
        self._m_pProto = table
        self.SetFlag(int(self._m_pProto.dwFlags))

    def GetProto(self):
        return self._m_pProto
    def GetGold(self):
        ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'IS_SET' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
        if IS_SET(self.GetFlag(), EItemFlag.ITEM_FLAG_COUNT_PER_1GOLD):
            if self.GetProto().lldGold == 0:
                return self.GetCount()
            else:
                return math.trunc(self.GetCount() / float(self.GetProto().lldGold))
        else:
            return self.GetProto().lldGold

    def GetShopBuyPrice(self):
        return self.GetProto().lldShopBuyPrice

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if __MULTI_LANGUAGE_SYSTEM__
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if __MULTI_LANGUAGE_SYSTEM__ && !__ITEM_DROP_RENEWAL__
    def GetName(self, bLocale = LaniatusLocalization.LOCALE_LANIATUS):
        if bLocale == LaniatusLocalization.LOCALE_LANIATUS and self.GetOwner() is not None and self.GetOwner().GetDesc() is not None:
            bLocale = self.GetOwner().GetDesc().GetLanguage()

        return LC_LOCALE_ITEM_TEXT(self.GetVnum(), bLocale) if self._m_pProto is not None else None
##endif

##else
    def GetName(self):
        return self._m_pProto.szLocaleName if self._m_pProto is not None else None
##endif
    def GetBaseName(self):
        return self._m_pProto.szName if self._m_pProto is not None else None
    def GetSize(self):
        return self._m_pProto.bSize if self._m_pProto is not None else 0
    def SetFlag(self, flag):
        self._m_lFlag = flag
    def GetFlag(self):
        return self._m_lFlag
    def AddFlag(self, bit):
        ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'SET_BIT' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
        SET_BIT(self._m_lFlag, bit)

    def RemoveFlag(self, bit):
        ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'REMOVE_BIT' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
        REMOVE_BIT(self._m_lFlag, bit)

    def GetWearFlag(self):
        return self._m_pProto.dwWearFlags if self._m_pProto is not None else 0
    def GetAntiFlag(self):
        return self._m_pProto.dwAntiFlags if self._m_pProto is not None else 0
    def GetImmuneFlag(self):
        return self._m_pProto.dwImmuneFlag if self._m_pProto is not None else 0

    def GetRealImmuneFlag(self):
        dwImmuneFlag = self.GetImmuneFlag()

        i = 0
        while i < EItemMisc.ITEM_ATTRIBUTE_MAX_NUM:
            if (self.GetAttribute(i).sValue) == 0:
                continue

            if self.GetAttribute(i).bType == EApplyTypes.APPLY_IMMUNE_STUN:
                ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'SET_BIT' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
                SET_BIT(dwImmuneFlag, EImmuneFlags.IMMUNE_STUN)
            elif self.GetAttribute(i).bType == EApplyTypes.APPLY_IMMUNE_SLOW:
                ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'SET_BIT' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
                SET_BIT(dwImmuneFlag, EImmuneFlags.IMMUNE_SLOW)
            elif self.GetAttribute(i).bType == EApplyTypes.APPLY_IMMUNE_FALL:
                ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'SET_BIT' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
                SET_BIT(dwImmuneFlag, EImmuneFlags.IMMUNE_FALL)
            i += 1

        return dwImmuneFlag

    def SetVID(self, vid):
        self._m_dwVID = vid
    def GetVID(self):
        return self._m_dwVID
    def SetCount(self, count):
        if self.GetType() == EItemTypes.ITEM_ELK:
            self._m_dwCount = MIN(count, numeric_limits.max())
        else:
            self._m_dwCount = MIN(count, EItemMisc.ITEM_MAX_COUNT)

        if count == 0 and self._m_pOwner:
            if self.GetSubType() == EUseSubTypes.USE_ABILITY_UP or self.GetSubType() == EUseSubTypes.USE_POTION or self.GetVnum() == 70020:
                pOwner = self.GetOwner()
                wCell = self.GetCell()

                self.RemoveFromCharacter()

                if not self.IsDragonSoul():
                    pItem = pOwner.FindSpecifyItem(self.GetVnum())

                    if None is not pItem:
                        pOwner.ChainQuickslotItem(pItem, byte(Globals.LG_QUICKSLOT_TYPE_ITEM), byte(wCell))
                    else:
                        pOwner.SyncQuickslot(byte(Globals.LG_QUICKSLOT_TYPE_ITEM), byte(wCell), 255)

                ITEM_MANAGER.instance().DestroyItem(self)
            else:
                if not self.IsDragonSoul():
                    self._m_pOwner.SyncQuickslot(byte(Globals.LG_QUICKSLOT_TYPE_ITEM), byte(self._m_wCell), 255)
                ITEM_MANAGER.instance().DestroyItem(self.RemoveFromCharacter())

            return LGEMiscellaneous.DEFINECONSTANTS.false

        self.UpdatePacket()

        self.Save()
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def GetCount(self):


        if self.GetType() == EItemTypes.ITEM_ELK:
            return MIN(self._m_dwCount, numeric_limits.max())
        else:
            return MIN(self._m_dwCount, EItemMisc.ITEM_MAX_COUNT)

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: uint GetVnum() const
    def GetVnum(self):
        return self._m_dwMaskVnum if self._m_dwMaskVnum != 0 else self._m_dwVnum
## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: uint GetOriginalVnum() const
    def GetOriginalVnum(self):
        return self._m_dwVnum
## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: byte GetType() const
    def GetType(self):
        return self._m_pProto.bType if self._m_pProto is not None else 0
## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: byte GetSubType() const
    def GetSubType(self):
        return self._m_pProto.bSubType if self._m_pProto is not None else 0
## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: byte GetLimitType(uint idx) const
    def GetLimitType(self, idx):
        return self._m_pProto.aLimits[idx].bType if self._m_pProto is not None else 0
## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: int GetLimitValue(uint idx) const
    def GetLimitValue(self, idx):
        return self._m_pProto.aLimits[idx].lValue if self._m_pProto is not None else 0
    def GetValue(self, idx):
        assert idx < EItemMisc.ITEM_VALUES_MAX_NUM
        return self.GetProto().alValues[idx]

    def SetCell(self, ch, pos):
        self._m_pOwner = ch, self._m_wCell = pos
    def GetCell(self):
        return self._m_wCell
    def RemoveFromCharacter(self):
        if self._m_pOwner is None:
            #lani_err("Item::RemoveFromCharacter owner null")
            return (self)

        pOwner = self._m_pOwner

        if self._m_bEquipped:
            self.Unequip()
            self.SetWindow(EWindows.RESERVED_WINDOW)
            self.Save()
            return (self)
        else:
            if self.GetWindow() != EWindows.SAFEBOX and self.GetWindow() != EWindows.MALL:
                if self.IsDragonSoul():
                    if self._m_wCell >= EDSInventoryMaxNum.DRAGON_SOUL_INVENTORY_MAX_NUM:
                        #lani_err("CItem::RemoveFromCharacter: pos >= DRAGON_SOUL_INVENTORY_MAX_NUM")
                    else:
                        pOwner.SetItem(TItemPos(self._m_bWindow, self._m_wCell), None)
                else:
                    cell = TItemPos(EWindows.INVENTORY, self._m_wCell)

                    if LGEMiscellaneous.DEFINECONSTANTS.false == cell.IsDefaultInventoryPosition() and LGEMiscellaneous.DEFINECONSTANTS.false == cell.IsBeltInventoryPosition():
                        #lani_err("CItem::RemoveFromCharacter: Invalid Item Position")
                    else:
                        pOwner.SetItem(TItemPos(cell), None)

            self._m_pOwner = None
            self._m_wCell = 0

            self.SetWindow(EWindows.RESERVED_WINDOW)
            self.Save()
            return (self)

# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    AddToCharacter(ch, Cell)
    def GetOwner(self):
        return self._m_pOwner
    def RemoveFromGround(self):
        if self.GetSectree():
            self.SetOwnership(None, 10)

            self.GetSectree().RemoveEntity(self)

            ViewCleanup()

            self.Save()

        return (self)

    def AddToGround(self, lMapIndex, pos, skipOwnerCheck = LGEMiscellaneous.DefineConstants.false):
        if 0 == lMapIndex:
            #lani_err("wrong map index argument: %d", lMapIndex)
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if self.GetSectree():
            #lani_err("sectree already assigned")
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if (not skipOwnerCheck) and self._m_pOwner:
            #lani_err("owner pointer not null")
            return LGEMiscellaneous.DEFINECONSTANTS.false

        tree = SECTREE_MANAGER.instance().Get(uint(lMapIndex), uint(pos.x), uint(pos.y))

        if tree is None:
            #lani_err("cannot find sectree by %dx%d", pos.x, pos.y)
            return LGEMiscellaneous.DEFINECONSTANTS.false

        self.SetWindow(EWindows.GROUND)
        self.SetXYZ(pos.x, pos.y, pos.z)
        tree.InsertEntity(self)
        UpdateSectree()
        self.Save()
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def FindEquipCell(self, ch, iCandidateCell = -1):

        if ((not self.GetWearFlag()) or EItemTypes.ITEM_TOTEM == self.GetType()) and not Globals.__IsWearableWithoutWearFlags(self.GetType()):
            return -1

        if self.GetType() == EItemTypes.ITEM_DS or self.GetType() == EItemTypes.ITEM_SPECIAL_DS:
            if iCandidateCell < 0:
                return EWearPositions.WEAR_MAX_NUM + self.GetSubType()
            else:
                i = 0
                while i < EDragonSoulDeckType.DRAGON_SOUL_DECK_MAX_NUM:
                    if EWearPositions.WEAR_MAX_NUM + i * int(EDragonSoulSubType.DS_SLOT_MAX) + self.GetSubType() == iCandidateCell:
                        return iCandidateCell
                    i += 1
                return -1
        elif self.GetType() == EItemTypes.ITEM_COSTUME:
            if self.GetSubType() == ECostumeSubTypes.COSTUME_BODY:
                return EWearPositions.WEAR_COSTUME_BODY
            elif self.GetSubType() == ECostumeSubTypes.COSTUME_HAIR:
                return EWearPositions.WEAR_COSTUME_HAIR
            elif self.GetSubType() == ECostumeSubTypes.COSTUME_MOUNT:
                return EWearPositions.WEAR_COSTUME_MOUNT
            elif self.GetSubType() == ECostumeSubTypes.COSTUME_PET:
                return EWearPositions.WEAR_COSTUME_PET
            elif self.GetSubType() == ECostumeSubTypes.COSTUME_ACCE:
                return EWearPositions.WEAR_COSTUME_ACCE
            elif self.GetSubType() == ECostumeSubTypes.COSTUME_WEAPON:
                return EWearPositions.WEAR_COSTUME_WEAPON
        elif self.GetType() == EItemTypes.ITEM_RING:
            if ch.GetWear(EWearPositions.WEAR_RING1):
                return EWearPositions.WEAR_RING2
            else:
                return EWearPositions.WEAR_RING1
        elif self.GetType() == EItemTypes.ITEM_BELT:
            return EWearPositions.WEAR_BELT
        elif (self.GetWearFlag() & uint(EItemWearableFlag.WEARABLE_BODY)) != 0:
            return EWearPositions.WEAR_BODY
        elif (self.GetWearFlag() & uint(EItemWearableFlag.WEARABLE_HEAD)) != 0:
            return EWearPositions.WEAR_HEAD
        elif (self.GetWearFlag() & uint(EItemWearableFlag.WEARABLE_FOOTS)) != 0:
            return EWearPositions.WEAR_FOOTS
        elif (self.GetWearFlag() & uint(EItemWearableFlag.WEARABLE_WRIST)) != 0:
            return EWearPositions.WEAR_WRIST
        elif (self.GetWearFlag() & uint(EItemWearableFlag.WEARABLE_WEAPON)) != 0:
            return EWearPositions.WEAR_WEAPON
        elif (self.GetWearFlag() & uint(EItemWearableFlag.WEARABLE_SHIELD)) != 0:
            return EWearPositions.WEAR_SHIELD
        elif (self.GetWearFlag() & uint(EItemWearableFlag.WEARABLE_NECK)) != 0:
            return EWearPositions.WEAR_NECK
        elif (self.GetWearFlag() & uint(EItemWearableFlag.WEARABLE_EAR)) != 0:
            return EWearPositions.WEAR_EAR
        elif (self.GetWearFlag() & uint(EItemWearableFlag.WEARABLE_ARROW)) != 0:
            return EWearPositions.WEAR_ARROW
        elif (self.GetWearFlag() & uint(EItemWearableFlag.WEARABLE_UNIQUE)) != 0:
            if ch.GetWear(EWearPositions.WEAR_UNIQUE1):
                return EWearPositions.WEAR_UNIQUE2
            else:
                return EWearPositions.WEAR_UNIQUE1
        elif (self.GetWearFlag() & uint(EItemWearableFlag.WEARABLE_PENDANT)) != 0:
            return EWearPositions.WEAR_PENDANT

        return -1

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: bool IsEquipped() const
    def IsEquipped(self):
        return self._m_bEquipped
    def EquipTo(self, ch, bWearCell):
        if ch is None:
            #lani_err("EquipTo: nil character")
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if self.IsDragonSoul():
            if bWearCell < EWearPositions.WEAR_MAX_NUM or bWearCell >= EWearPositions.WEAR_MAX_NUM + EDragonSoulDeckType.DRAGON_SOUL_DECK_MAX_NUM * EDragonSoulSubType.DS_SLOT_MAX:
                #lani_err("EquipTo: invalid dragon soul cell (this: #%d %s wearflag: %d cell: %d)", self.GetOriginalVnum(), self.GetName(LOCALE_LANIATUS), self.GetSubType(), bWearCell - byte(EWearPositions.WEAR_MAX_NUM))
                return LGEMiscellaneous.DEFINECONSTANTS.false
        else:
            if bWearCell >= EWearPositions.WEAR_MAX_NUM:
                #lani_err("EquipTo: invalid wear cell (this: #%d %s wearflag: %d cell: %d)", self.GetOriginalVnum(), self.GetName(LOCALE_LANIATUS), self.GetWearFlag(), bWearCell)
                return LGEMiscellaneous.DEFINECONSTANTS.false

        if ch.GetWear(bWearCell):
            #lani_err("EquipTo: item already exist (this: #%d %s cell: %d %s)", self.GetOriginalVnum(), self.GetName(LOCALE_LANIATUS), bWearCell, ch.GetWear(bWearCell).GetName(LOCALE_LANIATUS))
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if self.GetOwner():
            self.RemoveFromCharacter()

        ch.SetWear(bWearCell, self)

        self._m_pOwner = ch
        self._m_bEquipped = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
        self._m_wCell = LGEMiscellaneous.INVENTORY_MAX_NUM + bWearCell

        dwImmuneFlag = 0

        i = 0
        while i < EWearPositions.WEAR_MAX_NUM:
            pItem = self._m_pOwner.GetWear(ushort(i))
            if self._m_pOwner.GetWear(ushort(i)):
                ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'SET_BIT' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
                SET_BIT(dwImmuneFlag, pItem.GetRealImmuneFlag())
            i += 1

        self._m_pOwner.SetImmuneFlag(dwImmuneFlag)

        if self.IsDragonSoul():
            DSManager.instance().ActivateDragonSoul(self)
        else:
            self.ModifyPoints(((not LGEMiscellaneous.DEFINECONSTANTS.false)))
            self.StartUniqueExpireEvent()
            if -1 != self.GetProto().cLimitTimerBasedOnWearIndex:
                self.StartTimerBasedOnWearExpireEvent()

            self.StartAccessorySocketExpireEvent()

        ch.BuffOnAttr_AddBuffsFromItem(self)

        self._m_pOwner.ComputeBattlePoints()

        self._m_pOwner.UpdatePacket()

        self.Save()

        return (((not LGEMiscellaneous.DEFINECONSTANTS.false)))

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: bool IsEquipable() const
    def IsEquipable(self):
        if (self.GetType() == EItemTypes.ITEM_COSTUME) or (self.GetType() == EItemTypes.ITEM_ARMOR) or (self.GetType() == EItemTypes.ITEM_WEAPON) or (self.GetType() == EItemTypes.ITEM_ROD) or (self.GetType() == EItemTypes.ITEM_PICK) or (self.GetType() == EItemTypes.ITEM_UNIQUE) or (self.GetType() == EItemTypes.ITEM_DS) or (self.GetType() == EItemTypes.ITEM_SPECIAL_DS) or (self.GetType() == EItemTypes.ITEM_RING) or (self.GetType() == EItemTypes.ITEM_BELT):
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        return LGEMiscellaneous.DEFINECONSTANTS.false

    def CanUsedBy(self, ch):
        if ch.GetJob() == EJobs.JOB_LG_PAWN_WARRIOR:
            if (self.GetAntiFlag() & uint(LaniatusEITMAntiFlagDcs.ITEM_ANTIFLAG_LG_PAWN_WARRIOR)) != 0:
                return LGEMiscellaneous.DEFINECONSTANTS.false

        elif ch.GetJob() == EJobs.JOB_LG_PAWN_ASSASSIN:
            if (self.GetAntiFlag() & uint(LaniatusEITMAntiFlagDcs.ITEM_ANTIFLAG_LG_PAWN_ASSASSIN)) != 0:
                return LGEMiscellaneous.DEFINECONSTANTS.false

        elif ch.GetJob() == EJobs.JOB_LG_PAWN_MAGE:
            if (self.GetAntiFlag() & uint(LaniatusEITMAntiFlagDcs.ITEM_ANTIFLAG_LG_PAWN_MAGE)) != 0:
                return LGEMiscellaneous.DEFINECONSTANTS.false

        elif ch.GetJob() == EJobs.JOB_LG_PAWN_SHURA:
            if (self.GetAntiFlag() & uint(LaniatusEITMAntiFlagDcs.ITEM_ANTIFLAG_LG_PAWN_SHURA)) != 0:
                return LGEMiscellaneous.DEFINECONSTANTS.false
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if ENABLE_WOLFMAN
        elif ch.GetJob() == EJobs.JOB_WOLFMAN:
            if (self.GetAntiFlag() & uint(LaniatusEITMAntiFlagDcs.ITEM_ANTIFLAG_WOLFMAN)) != 0:
                return LGEMiscellaneous.DEFINECONSTANTS.false
##endif

        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def DistanceValid(self, ch):
        if self.GetSectree() is None:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        iDist = uint(Globals.DISTANCE_APPROX(self.GetX() - ch.GetX(), self.GetY() - ch.GetY()))
        max_distance = ushort(500 if ch.IsRiding() else 300)
        tolerance = 150

        if iDist > max_distance + tolerance:
            if test_server:
                ch.ChatPacket(EChatType.CHAT_TYPE_INFO, "%d: Distance is not valid: %d > %d", self.GetID(), iDist, max_distance + tolerance)
            return LGEMiscellaneous.DEFINECONSTANTS.false
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def UpdatePacket(self):
        if self._m_pOwner is None or self._m_pOwner.GetDesc() is None:
            return

        pack = packet_item_update()

        pack.header = byte(Globals.LG_HEADER_GC_ITEM_UPDATE)
        pack.Cell = TItemPos(self.GetWindow(), self._m_wCell)
        pack.count = ushort(self._m_dwCount)

        i = 0
        while i < EItemMisc.LG_ITEM_SOCKET_MAX_NUM:
            pack.alSockets[i] = self._m_alSockets[i]
            i += 1

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memcpy' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memcpy(pack.aAttr, self.GetAttributes(), sizeof(pack.aAttr))

        #sys_log(2, "UpdatePacket %s -> %s", self.GetName(LOCALE_LANIATUS), self._m_pOwner.GetName(LOCALE_LANIATUS))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self._m_pOwner.GetDesc().Packet(pack, sizeof(pack))

    def UsePacketEncode(self, ch, victim, packet):
        if self.GetVnum() == 0:
            return

        packet.header = byte(Globals.LG_HEADER_GC_ITEM_USE)
        packet.ch_vid = ch.GetVID()
        packet.victim_vid = victim.GetVID()
        packet.Cell = TItemPos(self.GetWindow(), self._m_wCell)
        packet.vnum = self.GetVnum()

    def SetExchanging(self, bOn = (!LGEMiscellaneous.DefineConstants.false)):
        self._m_bExchanging = bOn

    def IsExchanging(self):
        return self._m_bExchanging
    def IsPolymorphItem(self):
        return self.GetType() == EItemTypes.ITEM_POLYMORPH

    def ModifyPoints(self, bAdd):
        if self.IsCostumeMountItem() and not self._m_pOwner.IsRiding():
            return

        accessoryGrade = None

        if LGEMiscellaneous.DEFINECONSTANTS.false == self.IsAccessoryForSocket():
            if (self._m_pProto.bType == EItemTypes.ITEM_WEAPON or self._m_pProto.bType == EItemTypes.ITEM_ARMOR) and self._m_pProto.bSubType != EWeaponSubTypes.WEAPON_QUIVER:
                i = 0
                while i < EItemMisc.LG_ITEM_SOCKET_MAX_NUM:
                    dwVnum = None

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((dwVnum = GetSocket(i)) <= 2)
                    if (dwVnum = uint(self.GetSocket(i))) <= 2:
                        continue

                    p = ITEM_MANAGER.instance().GetTable(dwVnum)

                    if p is None:
                        #lani_err("cannot find table by vnum %u", dwVnum)
                        continue

                    if EItemTypes.ITEM_METIN == p.bType:
                        i = 0
                        while i < EItemMisc.ITEM_APPLY_MAX_NUM:
                            if p.aApplies[i].bType == EApplyTypes.APPLY_NONE:
                                continue

                            if p.aApplies[i].bType == EApplyTypes.APPLY_SKILL:
                                self._m_pOwner.ApplyPoint(p.aApplies[i].bType,p.aApplies[i].lValue if bAdd else p.aApplies[i].lValue ^ 0x00800000)
                            else:
                                self._m_pOwner.ApplyPoint(p.aApplies[i].bType,p.aApplies[i].lValue if bAdd else -p.aApplies[i].lValue)
                            i += 1
                    i += 1

            accessoryGrade = 0
        else:
            accessoryGrade = MIN(self.GetAccessorySocketGrade(), Globals.ITEM_ACCESSORY_SOCKET_MAX_NUM)

        i = 0
        while i < EItemMisc.ITEM_APPLY_MAX_NUM:
            if self._m_pProto.aApplies[i].bType == EApplyTypes.APPLY_NONE:
                continue

            type = self._m_pProto.aApplies[i].bType
            value = self._m_pProto.aApplies[i].lValue

            if EItemTypes.ITEM_COSTUME == self.GetType() and ECostumeSubTypes.COSTUME_ACCE == self.GetSubType() and self.GetSocket(1) > 0:
                acceInItemTable = ITEM_MANAGER.instance().GetTable(uint(self.GetSocket(1)))
                if acceInItemTable:
                    type = acceInItemTable.aApplies[i].bType
                    value = acceInItemTable.aApplies[i].lValue
                    drainPct = self.GetSocket(0)
                    value = 1 if value < 0 else int((float(value) / 100) * drainPct)

            if self._m_pProto.aApplies[i].bType == EApplyTypes.APPLY_SKILL:
                self._m_pOwner.ApplyPoint(self._m_pProto.aApplies[i].bType,value if bAdd else value ^ 0x00800000)
            else:
                if 0 != accessoryGrade:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
                    value += MAX(accessoryGrade, value * aiAccessorySocketEffectivePct[accessoryGrade] / 100)

                self._m_pOwner.ApplyPoint(self._m_pProto.aApplies[i].bType,value if bAdd else -value)
            i += 1
        if ((not LGEMiscellaneous.DEFINECONSTANTS.false)) == CItemVnumHelper.IsRamadanMoonRing(self.GetVnum()) or ((not LGEMiscellaneous.DEFINECONSTANTS.false)) == CItemVnumHelper.IsHalloweenCandy(self.GetVnum()) or ((not LGEMiscellaneous.DEFINECONSTANTS.false)) == CItemVnumHelper.IsHappinessRing(self.GetVnum()) or ((not LGEMiscellaneous.DEFINECONSTANTS.false)) == CItemVnumHelper.IsLovePendant(self.GetVnum()):
            pass
        else:
            i = 0
            while i < EItemMisc.ITEM_ATTRIBUTE_MAX_NUM:
                if self.GetAttributeType(i) != 0:
                    ia = self.GetAttribute(i)
                    value = ia.sValue

                    if EItemTypes.ITEM_COSTUME == self.GetType() and ECostumeSubTypes.COSTUME_ACCE == self.GetSubType():
                        drainPct = self.GetSocket(0)
                        value = 1 if value < 0 else short((float(value) / 100) * drainPct)

                    if ia.bType == EApplyTypes.APPLY_SKILL:
                        self._m_pOwner.ApplyPoint(ia.bType,value if bAdd else value ^ 0x00800000)
                    else:
                        self._m_pOwner.ApplyPoint(ia.bType,value if bAdd else -value)
                i += 1

        if (self._m_pProto.bType == EItemTypes.ITEM_PICK) or (self._m_pProto.bType == EItemTypes.ITEM_ROD):
                if bAdd:
                    if self._m_wCell == LGEMiscellaneous.INVENTORY_MAX_NUM + EWearPositions.WEAR_WEAPON:
                        self._m_pOwner.SetPart(EParts.PART_WEAPON, self.GetVnum())
                else:
                    if self._m_wCell == LGEMiscellaneous.INVENTORY_MAX_NUM + EWearPositions.WEAR_WEAPON:
                        self._m_pOwner.SetPart(EParts.PART_WEAPON, self._m_pOwner.GetOriginalPart(EParts.PART_WEAPON))

        elif self._m_pProto.bType == EItemTypes.ITEM_WEAPON:
                pkCostumeWeapon = self._m_pOwner.GetWear(EWearPositions.WEAR_COSTUME_WEAPON)
                if pkCostumeWeapon is not None and bAdd and self._m_pProto.bSubType != EWeaponSubTypes.WEAPON_ARROW and self._m_pProto.bSubType != EWeaponSubTypes.WEAPON_QUIVER:
                    if pkCostumeWeapon.GetValue(3) == self.GetSubType() and bAdd:
                        self._m_pOwner.SetPart(EParts.PART_WEAPON, pkCostumeWeapon.GetVnum())
                        break
                    else:
                        self._m_pOwner.SetPart(EParts.PART_WEAPON, self.GetVnum())
                        break

                if bAdd:
                    if self._m_wCell == LGEMiscellaneous.INVENTORY_MAX_NUM + EWearPositions.WEAR_WEAPON:
                        self._m_pOwner.SetPart(EParts.PART_WEAPON, self.GetVnum())
                else:
                    if self._m_wCell == LGEMiscellaneous.INVENTORY_MAX_NUM + EWearPositions.WEAR_WEAPON:
                        self._m_pOwner.SetPart(EParts.PART_WEAPON, self._m_pOwner.GetOriginalPart(EParts.PART_WEAPON))

        elif self._m_pProto.bType == EItemTypes.ITEM_ARMOR:
                if None is not self._m_pOwner.GetWear(EWearPositions.WEAR_COSTUME_BODY):
                    break

                if self.GetSubType() == EArmorSubTypes.ARMOR_BODY or self.GetSubType() == EArmorSubTypes.ARMOR_HEAD or self.GetSubType() == EArmorSubTypes.ARMOR_FOOTS or self.GetSubType() == EArmorSubTypes.ARMOR_SHIELD:
                    if bAdd:
                        if self.GetProto().bSubType == EArmorSubTypes.ARMOR_BODY:
                            self._m_pOwner.SetPart(EParts.PART_MAIN, self.GetVnum())
                    else:
                        if self.GetProto().bSubType == EArmorSubTypes.ARMOR_BODY:
                            self._m_pOwner.SetPart(EParts.PART_MAIN, self._m_pOwner.GetOriginalPart(EParts.PART_MAIN))

        elif self._m_pProto.bType == EItemTypes.ITEM_COSTUME:
                toSetValue = self.GetVnum()
                toSetPart = EParts.PART_MAX_NUM

                if self.GetSubType() == ECostumeSubTypes.COSTUME_BODY:
                    toSetPart = EParts.PART_MAIN

                    if LGEMiscellaneous.DEFINECONSTANTS.false == bAdd:
                        pArmor = self._m_pOwner.GetWear(EWearPositions.WEAR_BODY)
                        toSetValue = pArmor.GetVnum() if (None is not pArmor) else self._m_pOwner.GetOriginalPart(EParts.PART_MAIN)


                elif self.GetSubType() == ECostumeSubTypes.COSTUME_HAIR:
                    toSetPart = EParts.PART_HAIR
                    toSetValue = uint(self.GetValue(3)) if (((not LGEMiscellaneous.DEFINECONSTANTS.false)) == bAdd) else 0

                elif self.GetSubType() == ECostumeSubTypes.COSTUME_ACCE:
                    toSetPart = EParts.PART_ACCE
                    toSetValue = self.GetVnum() if (((not LGEMiscellaneous.DEFINECONSTANTS.false)) == bAdd) else 0

                elif self.GetSubType() == ECostumeSubTypes.COSTUME_WEAPON:
                    toSetPart = EParts.PART_WEAPON

                    resetToItem = self._m_pOwner.GetWear(EWearPositions.WEAR_WEAPON)
                    if resetToItem:
                        if bAdd:
                            if resetToItem.GetSubType() != self.GetValue(3):
                                toSetValue = resetToItem.GetVnum()
                        else:
                            toSetValue = resetToItem.GetVnum()
                    else:
                        toSetValue = 0

                if EParts.PART_MAX_NUM != toSetPart:
                    self._m_pOwner.SetPart(byte(int(toSetPart)), toSetValue)
                    self._m_pOwner.UpdatePacket()
        elif self._m_pProto.bType == EItemTypes.ITEM_UNIQUE:
                if 0 != self.GetSIGVnum():
                    pItemGroup = ITEM_MANAGER.instance().GetSpecialItemGroup(self.GetSIGVnum())
                    if None is pItemGroup:
                        break

                    dwAttrVnum = pItemGroup.GetAttrVnum(self.GetVnum())
                    pAttrGroup = ITEM_MANAGER.instance().GetSpecialAttrGroup(dwAttrVnum)

                    if None is pAttrGroup:
                        break

                    for it in pAttrGroup.m_vecAttrs:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if _WIN32
                        self._m_pOwner.ApplyPoint(it.apply_type,it.apply_value if bAdd else -int(it.apply_value))
##else
                        self._m_pOwner.ApplyPoint(it.apply_type,it.apply_value if bAdd else -it.apply_value)
##endif

    def CreateSocket(self, bSlot, bGold):
        assert bSlot < EItemMisc.LG_ITEM_SOCKET_MAX_NUM

        if self._m_alSockets[bSlot] != 0:
            #lani_err("Item::CreateSocket : socket already exist %s %d", self.GetName(LOCALE_LANIATUS), bSlot)
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if bGold != 0:
            self._m_alSockets[bSlot] = 2
        else:
            self._m_alSockets[bSlot] = 1

        self.UpdatePacket()

        self.Save()
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

## Laniatus Games Studio Inc. | WARNING: Python has no equivalent to methods returning pointers to value types:
#ORIGINAL METINII C CODE: const int *GetSockets()
    def GetSockets(self):
        return self._m_alSockets[0]
    def GetSocket(self, i):
        return self._m_alSockets[i]
    def SetSockets(self, c_al):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memcpy' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memcpy(self._m_alSockets, c_al, sizeof(self._m_alSockets))
        self.Save()

    def SetSocket(self, i, v, bLog = (!LGEMiscellaneous.DefineConstants.false)):
        assert i < EItemMisc.LG_ITEM_SOCKET_MAX_NUM
        self._m_alSockets[i] = v
        self.UpdatePacket()
        self.Save()

    def GetSocketCount(self):
        i = 0
        while i < EItemMisc.LG_ITEM_SOCKET_MAX_NUM:
            if self.GetSocket(i) == 0:
                return i
            i += 1
        return EItemMisc.LG_ITEM_SOCKET_MAX_NUM

    def AddSocket(self):
        count = self.GetSocketCount()
        if count == EItemMisc.LG_ITEM_SOCKET_MAX_NUM:
            return LGEMiscellaneous.DEFINECONSTANTS.false
        self._m_alSockets[count] = 1
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def GetAttributes(self):
        return self._m_aAttr
    def GetAttribute(self, i):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
#ORIGINAL METINII C CODE: return m_aAttr[i];
        return TPlayerItemAttribute(self._m_aAttr[i])
    def GetAttributeType(self, i):
        return self._m_aAttr[i].bType
    def GetAttributeValue(self, i):
        return self._m_aAttr[i].sValue
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    SetAttributes(c_pAttribute)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    FindAttribute(bType)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    RemoveAttributeAt(index)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    RemoveAttributeType(bType)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    HasAttr(bApply)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    HasRareAttr(bApply)
    def SetDestroyEvent(self, pkEvent):
## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: m_pkDestroyEvent = pkEvent;
        self._m_pkDestroyEvent.copy_from(pkEvent)

    def StartDestroyEvent(self, iSec = 300):
        if self._m_pkDestroyEvent:
            return

        info = Globals.AllocEventInfo()
        info.item = self

        self.SetDestroyEvent(event_create_ex(item_destroy_event, info, ((iSec) * passes_per_sec)))

    def GetRefinedVnum(self):
        return self._m_pProto.dwRefinedVnum if self._m_pProto is not None else 0
    def GetRefineFromVnum(self):
        return ITEM_MANAGER.instance().GetRefineFromVnum(self.GetVnum())

    def GetRefineLevel(self):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to pointers to value types:
#ORIGINAL METINII C CODE: const char* name = GetBaseName();
        name = self.GetBaseName()
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to pointers to value types:
#ORIGINAL METINII C CODE: char* p = const_cast<char*>(strrchr(name, '+'));
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no equivalent to 'const_cast' in Python:
        p = const_cast<char>(strrchr(name, '+'))

        if (not p) != '\0':
            return 0

        rtn = 0
        temp_ref_rtn = RefObject(rtn);
        Globals.str_to_number(temp_ref_rtn, p+1)
        rtn = temp_ref_rtn.arg_value

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to pointers to value types:
#ORIGINAL METINII C CODE: const char* locale_name = GetName();
        locale_name = self.GetName(LOCALE_LANIATUS)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no equivalent to 'const_cast' in Python:
        p = const_cast<char>(strrchr(locale_name, '+'))

        if p != '\0':
            locale_rtn = 0
            temp_ref_locale_rtn = RefObject(locale_rtn);
            Globals.str_to_number(temp_ref_locale_rtn, p+1)
            locale_rtn = temp_ref_locale_rtn.arg_value
            if locale_rtn != rtn:
                #lani_err("refine_level_based_on_NAME(%d) is not equal to refine_level_based_on_LOCALE_NAME(%d).", rtn, locale_rtn)

        return rtn

    def SetSkipSave(self, b):
        self._m_bSkipSave = b
    def GetSkipSave(self):
        return self._m_bSkipSave
    def IsOwnership(self, ch):
        if self._m_pkOwnershipEvent is None:
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        return ((not LGEMiscellaneous.DEFINECONSTANTS.false)) if self._m_dwOwnershipPID == ch.GetPlayerID() else LGEMiscellaneous.DEFINECONSTANTS.false

    def SetOwnership(self, ch, iSec = 10):
        if ch is None:
            if self._m_pkOwnershipEvent:
                event_cancel(self._m_pkOwnershipEvent)
                self._m_dwOwnershipPID = 0

                p = packet_item_ownership()

                p.bHeader = byte(Globals.LG_HEADER_GC_ITEM_OWNERSHIP)
                p.dwVID = self._m_dwVID
                p.szName[0] = '\0'

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                PacketAround(p, sizeof(p))
            return

        if self._m_pkOwnershipEvent:
            return

        if iSec <= 10:
            iSec = 30

        self._m_dwOwnershipPID = ch.GetPlayerID()

        info = Globals.AllocEventInfo()
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        strncpy_s(info.szOwnerName, sizeof(info.szOwnerName), ch.GetName(LOCALE_LANIATUS), _TRUNCATE)
        info.item = self

        self.SetOwnershipEvent(event_create_ex(ownership_event, info, ((iSec) * passes_per_sec)))

        p = packet_item_ownership()

        p.bHeader = byte(Globals.LG_HEADER_GC_ITEM_OWNERSHIP)
        p.dwVID = self._m_dwVID
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        strncpy_s(p.szName, sizeof(p.szName), ch.GetName(LOCALE_LANIATUS), _TRUNCATE)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        PacketAround(p, sizeof(p))

    def SetOwnershipEvent(self, pkEvent):
## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: m_pkOwnershipEvent = pkEvent;
        self._m_pkOwnershipEvent.copy_from(pkEvent)

    def GetLastOwnerPID(self):
        return self._m_dwLastOwnerPID
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    GetAttributeSetIndex()
    def AlterToMagicItem(self, iSecondPct = 0, iThirdPct = 0):
        idx = self.GetAttributeSetIndex()

        if idx < 0:
            return

        if self.GetType() == EItemTypes.ITEM_WEAPON:
            iSecondPct = 20
            iThirdPct = 5
        elif self.GetType() == EItemTypes.ITEM_COSTUME:
            iSecondPct = 30
            iThirdPct = 20
        elif self.GetType() == EItemTypes.ITEM_ARMOR:
            if self.GetSubType() == EArmorSubTypes.ARMOR_BODY:
                iSecondPct = 10
                iThirdPct = 2
            else:
                iSecondPct = 10
                iThirdPct = 1

        else:
            return

        self.PutAttribute(aiItemMagicAttributePercentHigh)

        if number(1, 100) <= iSecondPct:
            self.PutAttribute(aiItemMagicAttributePercentLow)

        if number(1, 100) <= iThirdPct:
            self.PutAttribute(aiItemMagicAttributePercentLow)

    def AlterToSocketItem(self, iSocketCount):
        if iSocketCount >= EItemMisc.LG_ITEM_SOCKET_MAX_NUM:
            #sys_log(0, "Invalid Socket Count %d, set to maximum", EItemMisc.LG_ITEM_SOCKET_MAX_NUM)
            iSocketCount = EItemMisc.LG_ITEM_SOCKET_MAX_NUM

        for i in range(0, iSocketCount):
            self.SetSocket(i, 1, ((not DefineConstants.false)))

    def GetRefineSet(self):
        return self._m_pProto.wRefineSet if self._m_pProto is not None else 0
    def StartUniqueExpireEvent(self):
        if self.GetType() != EItemTypes.ITEM_UNIQUE:
            return

        if self._m_pkUniqueExpireEvent:
            return

        if self.IsRealTimeItem():
            return

        if self.GetVnum() == Globals.UNIQUE_ITEM_HIDE_ALIGNMENT_TITLE:
            self._m_pOwner.ShowAlignment(LGEMiscellaneous.DEFINECONSTANTS.false)

        iSec = self.GetSocket(EItemUniqueSockets.LG_ITEM_SOCKET_UNIQUE_SAVE_TIME)

        if iSec == 0:
            iSec = 60
        else:
            iSec = MIN(iSec, 60)

        self.SetSocket(EItemUniqueSockets.LG_ITEM_SOCKET_UNIQUE_SAVE_TIME, 0, ((not DefineConstants.false)))

        info = Globals.AllocEventInfo()
        info.item = self

        self.SetUniqueExpireEvent(event_create_ex(unique_expire_event, info, ((iSec) * passes_per_sec)))

    def SetUniqueExpireEvent(self, pkEvent):
## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: m_pkUniqueExpireEvent = pkEvent;
        self._m_pkUniqueExpireEvent.copy_from(pkEvent)

    def StartTimerBasedOnWearExpireEvent(self):
        if self._m_pkTimerBasedOnWearExpireEvent:
            return

        if self.IsRealTimeItem():
            return

        if -1 == self.GetProto().cLimitTimerBasedOnWearIndex:
            return

        iSec = self.GetSocket(0)

        if 0 != iSec:
            iSec = math.fmod(iSec, 60)
            if 0 == iSec:
                iSec = 60

        info = Globals.AllocEventInfo()
        info.item = self

        self.SetTimerBasedOnWearExpireEvent(event_create_ex(timer_based_on_wear_expire_event, info, ((iSec) * passes_per_sec)))

    def SetTimerBasedOnWearExpireEvent(self, pkEvent):
## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: m_pkTimerBasedOnWearExpireEvent = pkEvent;
        self._m_pkTimerBasedOnWearExpireEvent.copy_from(pkEvent)

    def StartRealTimeExpireEvent(self):
        if self._m_pkRealTimeExpireEvent:
            return
        i = 0
        while i < EItemMisc.ITEM_LIMIT_MAX_NUM:
            if ELimitTypes.LIMIT_REAL_TIME == self.GetProto().aLimits[i].bType or ELimitTypes.LIMIT_REAL_TIME_START_FIRST_USE == self.GetProto().aLimits[i].bType:
                info = Globals.AllocEventInfo()
                info.item_vid = self.GetVID()

                self._m_pkRealTimeExpireEvent = event_create_ex(real_time_expire_event, info, ((1) * passes_per_sec))

                #sys_log(0, "REAL_TIME_EXPIRE: StartRealTimeExpireEvent")

                return
            i += 1

    def IsRealTimeItem(self):
        if self.GetProto() is None:
            return LGEMiscellaneous.DEFINECONSTANTS.false
        i = 0
        while i < EItemMisc.ITEM_LIMIT_MAX_NUM:
            if ELimitTypes.LIMIT_REAL_TIME == self.GetProto().aLimits[i].bType:
                return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
            i += 1
        return LGEMiscellaneous.DEFINECONSTANTS.false

    def StopUniqueExpireEvent(self):
        if self._m_pkUniqueExpireEvent is None:
            return

        if self.GetValue(2) != 0:
            return

        if self.GetVnum() == Globals.UNIQUE_ITEM_HIDE_ALIGNMENT_TITLE:
            self._m_pOwner.ShowAlignment(((not LGEMiscellaneous.DEFINECONSTANTS.false)))

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        self.SetSocket(EItemUniqueSockets.LG_ITEM_SOCKET_UNIQUE_SAVE_TIME, event_time(self._m_pkUniqueExpireEvent) / passes_per_sec, ((not DefineConstants.false)))
        event_cancel(self._m_pkUniqueExpireEvent)

        ITEM_MANAGER.instance().SaveSingleItem(self)

    def StopTimerBasedOnWearExpireEvent(self):
        if self._m_pkTimerBasedOnWearExpireEvent is None:
            return

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        remain_time = self.GetSocket(Globals.LG_ITEM_SOCKET_REMAIN_SEC) - event_processing_time(self._m_pkTimerBasedOnWearExpireEvent) / passes_per_sec

        self.SetSocket(Globals.LG_ITEM_SOCKET_REMAIN_SEC, remain_time, ((not DefineConstants.false)))
        event_cancel(self._m_pkTimerBasedOnWearExpireEvent)

        ITEM_MANAGER.instance().SaveSingleItem(self)

    def StopAccessorySocketExpireEvent(self):
        if self._m_pkAccessorySocketExpireEvent is None:
            return

        if not self.IsAccessoryForSocket():
            return

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        new_time = self.GetAccessorySocketDownGradeTime() - (60 - event_time(self._m_pkAccessorySocketExpireEvent) / passes_per_sec)

        event_cancel(self._m_pkAccessorySocketExpireEvent)

        if new_time <= 1:
            self.AccessorySocketDegrade()
        else:
            self.SetAccessorySocketDownGradeTime(uint(new_time))

    def GetDuration(self):
        if self.GetProto() is None:
            return -1

        i = 0
        while i < EItemMisc.ITEM_LIMIT_MAX_NUM:
            if ELimitTypes.LIMIT_REAL_TIME == self.GetProto().aLimits[i].bType:
                return self.GetProto().aLimits[i].lValue
            i += 1

        if -1 != self.GetProto().cLimitTimerBasedOnWearIndex:
            return self.GetProto().aLimits[self.GetProto().cLimitTimerBasedOnWearIndex].lValue

        return -1

# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    GetAttributeCount()
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    ClearAttribute()
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    ChangeAttribute(aiChangeProb = NULL)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    AddAttribute()
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    AddAttribute(bType, sValue)
    def ApplyAddon(self, iAddonType):
        CItemAddonManager.instance().ApplyAddonTo(iAddonType, self)

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: int GetSpecialGroup() const
    def GetSpecialGroup(self):
        return ITEM_MANAGER.instance().GetSpecialGroupFromItem(self.GetVnum())

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: bool IsSameSpecialGroup(const CItem* item) const
    def IsSameSpecialGroup(self, item):
        if self.GetVnum() == item.GetVnum():
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        if self.GetSpecialGroup() != 0 and (item.GetSpecialGroup() == self.GetSpecialGroup()):
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        return LGEMiscellaneous.DEFINECONSTANTS.false

    def IsAccessoryForSocket(self):
        return (self._m_pProto.bType == EItemTypes.ITEM_ARMOR and (self._m_pProto.bSubType == EArmorSubTypes.ARMOR_WRIST or self._m_pProto.bSubType == EArmorSubTypes.ARMOR_NECK or self._m_pProto.bSubType == EArmorSubTypes.ARMOR_EAR)) or (self._m_pProto.bType == EItemTypes.ITEM_BELT)

    def GetAccessorySocketGrade(self):
        return MINMAX(0, self.GetSocket(0), self.GetAccessorySocketMaxGrade())

    def GetAccessorySocketMaxGrade(self):
        return MINMAX(0, self.GetSocket(1), Globals.ITEM_ACCESSORY_SOCKET_MAX_NUM)

    def GetAccessorySocketDownGradeTime(self):
        return MINMAX(0, self.GetSocket(2), aiAccessorySocketDegradeTime[self.GetAccessorySocketGrade()])

    def SetAccessorySocketGrade(self, iGrade):
        self.SetSocket(0, MINMAX(0, iGrade, self.GetAccessorySocketMaxGrade()), ((not DefineConstants.false)))

        iDownTime = aiAccessorySocketDegradeTime[self.GetAccessorySocketGrade()]
        self.SetAccessorySocketDownGradeTime(uint(iDownTime))

    def SetAccessorySocketMaxGrade(self, iMaxGrade):
        self.SetSocket(1, MINMAX(0, iMaxGrade, Globals.ITEM_ACCESSORY_SOCKET_MAX_NUM), ((not DefineConstants.false)))

    def SetAccessorySocketDownGradeTime(self, time):
        self.SetSocket(2, int(time), ((not DefineConstants.false)))

        if test_server and self.GetOwner():
            self.GetOwner().ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Time remaining %d seconds."), self.GetName(LOCALE_LANIATUS), time)

    def AccessorySocketDegrade(self):
        if self.GetAccessorySocketGrade() > 0:
            ch = self.GetOwner()

            if ch:
                ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("The Gems of %s vanish."), self.GetName(LOCALE_LANIATUS))

            self.ModifyPoints(LGEMiscellaneous.DEFINECONSTANTS.false)
            self.SetAccessorySocketGrade(self.GetAccessorySocketGrade()-1)
            self.ModifyPoints(((not LGEMiscellaneous.DEFINECONSTANTS.false)))

            iDownTime = aiAccessorySocketDegradeTime[self.GetAccessorySocketGrade()]

            if test_server:
                iDownTime = math.trunc(iDownTime / float(60))

            self.SetAccessorySocketDownGradeTime(uint(iDownTime))

            if iDownTime != 0:
                self.StartAccessorySocketExpireEvent()

    def StartAccessorySocketExpireEvent(self):
        if not self.IsAccessoryForSocket():
            return

        if self._m_pkAccessorySocketExpireEvent:
            return

        if self.GetAccessorySocketMaxGrade() == 0:
            return

        if self.GetAccessorySocketGrade() == 0:
            return

        iSec = self.GetAccessorySocketDownGradeTime()
        self.SetAccessorySocketExpireEvent(None)

        if iSec <= 1:
            iSec = 5
        else:
            iSec = MIN(iSec, 60)

        info = Globals.AllocEventInfo()
        info.item_vid = self.GetVID()

        self.SetAccessorySocketExpireEvent(event_create_ex(accessory_socket_expire_event, info, ((iSec) * passes_per_sec)))

    def SetAccessorySocketExpireEvent(self, pkEvent):
## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: m_pkAccessorySocketExpireEvent = pkEvent;
        self._m_pkAccessorySocketExpireEvent.copy_from(pkEvent)

    class JewelAccessoryInfo:
    def CanPutInto(self, item):
        if item.GetType() == EItemTypes.ITEM_BELT:
            return self.GetSubType() == EUseSubTypes.USE_PUT_INTO_BELT_SOCKET

        elif item.GetType() == EItemTypes.ITEM_RING:
            return Globals.CanPutIntoRing(item, self)

        elif item.GetType() != EItemTypes.ITEM_ARMOR:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        vnum = item.GetVnum()

        infos = [[ 50634, 14420, 16220, 17220 ], [ 50635, 14500, 16500, 17500 ], [ 50636, 14520, 16520, 17520 ], [ 50637, 14540, 16540, 17540 ], [ 50638, 14560, 16560, 17560 ], [ 50639, 14570, 16570, 17570 ]]

        item_type = (math.trunc(item.GetVnum() / float(10))) * 10
        i = 0
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
## Laniatus Games Studio Inc. | WARNING: This 'sizeof' ratio was replaced with a direct reference to the array length:
#ORIGINAL METINII C CODE: for (int i = 0; i < sizeof(infos) / sizeof(infos[0]); i++)
        while i < len(infos):
            info = infos[i]
            if item.GetSubType() == EArmorSubTypes.ARMOR_WRIST:
                if info.wrist == item_type:
                    if info.jewel == self.GetVnum():
                        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
                    else:
                        return LGEMiscellaneous.DEFINECONSTANTS.false
            elif item.GetSubType() == EArmorSubTypes.ARMOR_NECK:
                if info.neck == item_type:
                    if info.jewel == self.GetVnum():
                        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
                    else:
                        return LGEMiscellaneous.DEFINECONSTANTS.false
            elif item.GetSubType() == EArmorSubTypes.ARMOR_EAR:
                if info.ear == item_type:
                    if info.jewel == self.GetVnum():
                        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
                    else:
                        return LGEMiscellaneous.DEFINECONSTANTS.false
            i += 1
        if item.GetSubType() == EArmorSubTypes.ARMOR_WRIST:
            vnum -= 14000
        elif item.GetSubType() == EArmorSubTypes.ARMOR_NECK:
            vnum -= 16000
        elif item.GetSubType() == EArmorSubTypes.ARMOR_EAR:
            vnum -= 17000
        else:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        type = math.trunc(vnum / float(20))

        if type < 0 or type > 11:
            type = math.trunc((vnum - 170) / float(20))

            if 50623 + type != self.GetVnum():
                return LGEMiscellaneous.DEFINECONSTANTS.false
            else:
                return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
        elif item.GetVnum() >= 16210 and item.GetVnum() <= 16219:
            if 50625 != self.GetVnum():
                return LGEMiscellaneous.DEFINECONSTANTS.false
            else:
                return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
        elif item.GetVnum() >= 16230 and item.GetVnum() <= 16239:
            if 50626 != self.GetVnum():
                return LGEMiscellaneous.DEFINECONSTANTS.false
            else:
                return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        return 50623 + type == self.GetVnum()

# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    CopyAttributeTo(pItem)
    def CopySocketTo(self, pItem):
        i = 0
        while i < EItemMisc.LG_ITEM_SOCKET_MAX_NUM:
            pItem._m_alSockets[i] = self._m_alSockets[i]
            i += 1

# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    GetRareAttrCount()
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    AddRareAttribute()
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    ChangeRareAttribute()
    def Lock(self, f):
        self._m_isLocked = f
## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: bool isLocked() const
    def isLocked(self):
        return self._m_isLocked

# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    _SetAttribute(i, bType, sValue)

# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    SetForceAttribute(i, bType, sValue)

    def Unequip(self):
        if self._m_pOwner is None or self.GetCell() < LGEMiscellaneous.INVENTORY_MAX_NUM:
            #lani_err("%s %u m_pOwner %p, GetCell %d", self.GetName(LOCALE_LANIATUS), self.GetID(), Globals.get_pointer(self._m_pOwner), self.GetCell())

            return LGEMiscellaneous.DEFINECONSTANTS.false

        if self is not self._m_pOwner.GetWear(self.GetCell() - ushort(LGEMiscellaneous.INVENTORY_MAX_NUM)):
            #lani_err("m_pOwner->GetWear() != this")
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if self.IsRideItem():
            self.ClearMountAttributeAndAffect()

        if self.IsDragonSoul():
            DSManager.instance().DeactivateDragonSoul(self, DefineConstants.false)
        else:
            self.ModifyPoints(LGEMiscellaneous.DEFINECONSTANTS.false)

        self.StopUniqueExpireEvent()

        if -1 != self.GetProto().cLimitTimerBasedOnWearIndex:
            self.StopTimerBasedOnWearExpireEvent()

        self.StopAccessorySocketExpireEvent()

        self._m_pOwner.BuffOnAttr_RemoveBuffsFromItem(self)

        self._m_pOwner.SetWear(self.GetCell() - ushort(LGEMiscellaneous.INVENTORY_MAX_NUM), None)

        dwImmuneFlag = 0

        i = 0
        while i < EWearPositions.WEAR_MAX_NUM:
            pItem = self._m_pOwner.GetWear(ushort(i))
            if pItem:
                ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'SET_BIT' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
                SET_BIT(dwImmuneFlag, self._m_pOwner.GetWear(ushort(i)).GetImmuneFlag())
            i += 1

        self._m_pOwner.ComputeBattlePoints()

        self._m_pOwner.UpdatePacket()

        self._m_pOwner = None
        self._m_wCell = 0
        self._m_bEquipped = LGEMiscellaneous.DEFINECONSTANTS.false

        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    AddAttr(bApply, bLevel)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    PutAttribute(aiAttrPercentTable)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    PutAttributeWithLevel(bLevel)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python has no concept of a 'friend' class:
#    friend class CInputDB
    def OnAfterCreatedItem(self):
        if -1 != self.GetProto().cLimitRealTimeFirstUseIndex:
            if 0 != self.GetSocket(1):
                self.StartRealTimeExpireEvent()

        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def IsRideItem(self):
        if EItemTypes.ITEM_UNIQUE == self.GetType() and EUniqueSubTypes.UNIQUE_SPECIAL_RIDE == self.GetSubType():
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
        if EItemTypes.ITEM_UNIQUE == self.GetType() and EUniqueSubTypes.UNIQUE_SPECIAL_MOUNT_RIDE == self.GetSubType():
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
        return LGEMiscellaneous.DEFINECONSTANTS.false

    def ClearMountAttributeAndAffect(self):
        ch = self.GetOwner()

        ch.RemoveAffect(LaniatusEAffectTypes.LANIA_AFFECT_MOUNT)
        ch.RemoveAffect(LaniatusEAffectTypes.LANIA_AFFECT_MOUNT_BONUS)

        ch.MountVnum(0)

        ch.PointChange(EPointTypes.LG_POINT_ST, 0, DefineConstants.false, DefineConstants.false)
        ch.PointChange(EPointTypes.LG_POINT_DX, 0, DefineConstants.false, DefineConstants.false)
        ch.PointChange(EPointTypes.LG_POINT_HT, 0, DefineConstants.false, DefineConstants.false)
        ch.PointChange(EPointTypes.LG_POINT_IQ, 0, DefineConstants.false, DefineConstants.false)

    def IsNewMountItem(self):
        if (self.GetVnum() == 76000) or (self.GetVnum() == 76001) or (self.GetVnum() == 76002) or (self.GetVnum() == 76003) or (self.GetVnum() == 76004) or (self.GetVnum() == 76005) or (self.GetVnum() == 76006) or (self.GetVnum() == 76007) or (self.GetVnum() == 76008) or (self.GetVnum() == 76009) or (self.GetVnum() == 76010) or (self.GetVnum() == 76011) or (self.GetVnum() == 76012) or (self.GetVnum() == 76013) or (self.GetVnum() == 76014):
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
        return LGEMiscellaneous.DEFINECONSTANTS.false

    def IsCostumeMountItem(self):
        return self.GetType() == EItemTypes.ITEM_COSTUME and self.GetSubType() == ECostumeSubTypes.COSTUME_MOUNT

    def IsCostumePetItem(self):
        return self.GetType() == EItemTypes.ITEM_COSTUME and self.GetSubType() == ECostumeSubTypes.COSTUME_PET

    def SetMaskVnum(self, vnum):
        self._m_dwMaskVnum = vnum
    def GetMaskVnum(self):
        return self._m_dwMaskVnum
    def IsMaskedItem(self):
        return self._m_dwMaskVnum != 0
    def IsDragonSoul(self):
        return self.GetType() == EItemTypes.ITEM_DS

    def GiveMoreTime_Per(self, fPercent):
        if self.IsDragonSoul():
            duration = uint(DSManager.instance().GetDuration(self))
            remain_sec = self.GetSocket(Globals.LG_ITEM_SOCKET_REMAIN_SEC)
            given_time = int(fPercent * duration / 100)
            if remain_sec == duration:
                return LGEMiscellaneous.DEFINECONSTANTS.false
            if (given_time + remain_sec) >= duration:
                self.SetSocket(Globals.LG_ITEM_SOCKET_REMAIN_SEC, int(duration), ((not DefineConstants.false)))
                return int(duration - remain_sec)
            else:
                self.SetSocket(Globals.LG_ITEM_SOCKET_REMAIN_SEC, given_time + remain_sec, ((not DefineConstants.false)))
                return given_time
        else:
            return 0

    def GiveMoreTime_Fix(self, dwTime):
        if self.IsDragonSoul():
            duration = uint(DSManager.instance().GetDuration(self))
            remain_sec = self.GetSocket(Globals.LG_ITEM_SOCKET_REMAIN_SEC)
            if remain_sec == duration:
                return LGEMiscellaneous.DEFINECONSTANTS.false
            if (dwTime + remain_sec) >= duration:
                self.SetSocket(Globals.LG_ITEM_SOCKET_REMAIN_SEC, int(duration), ((not DefineConstants.false)))
                return int(duration - remain_sec)
            else:
                self.SetSocket(Globals.LG_ITEM_SOCKET_REMAIN_SEC, int(dwTime + remain_sec), ((not DefineConstants.false)))
                return int(dwTime)
        else:
            return 0


    def SetSIGVnum(self, dwSIG):
        self._m_dwSIGVnum = dwSIG
## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: uint GetSIGVnum() const
    def GetSIGVnum(self):
        return self._m_dwSIGVnum

class item_event_info(event_info_data):

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.item = []
        self.szOwnerName = str(['\0' for _ in range((int)LGEMiscellaneous.CHARACTER_NAME_MAX_LEN)])

        self.item = CItem(0)
        memset(self.szOwnerName, 0, LGEMiscellaneous.CHARACTER_NAME_MAX_LEN)

class item_vid_event_info(event_info_data):

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.item_vid = 0

        self.item_vid = 0

def AddToCharacter(ch, Cell):
    GetSectree is None
    m_pOwner is None
    pos = Cell.cell
    window_type = Cell.window_type

    if EWindows.INVENTORY == window_type:
        if m_wCell >= LGEMiscellaneous.INVENTORY_MAX_NUM and LGEMiscellaneous2.BELT_INVENTORY_SLOT_START > m_wCell:
            #lani_err("CItem::AddToCharacter: cell overflow: %s to %s cell %d", m_pProto.szName, ch.GetName(LOCALE_LANIATUS), m_wCell)
            return LGEMiscellaneous.DEFINECONSTANTS.false
    elif EWindows.DRAGON_SOUL_INVENTORY == window_type:
        if m_wCell >= EDSInventoryMaxNum.DRAGON_SOUL_INVENTORY_MAX_NUM:
            #lani_err("CItem::AddToCharacter: cell overflow: %s to %s cell %d", m_pProto.szName, ch.GetName(LOCALE_LANIATUS), m_wCell)
            return LGEMiscellaneous.DEFINECONSTANTS.false

    if ch.GetDesc():
        m_dwLastOwnerPID = ch.GetPlayerID()

    event_cancel(m_pkDestroyEvent)

    ch.SetItem(TItemPos(window_type, pos), self)
    m_pOwner = ch

    Save()
    return ((not LGEMiscellaneous.DEFINECONSTANTS.false))