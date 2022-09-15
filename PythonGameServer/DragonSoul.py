import math

## Laniatus Games Studio Inc. | NOTE: Python has no need of forward class declarations:
#class CHARACTER
## Laniatus Games Studio Inc. | NOTE: Python has no need of forward class declarations:
#class CItem

## Laniatus Games Studio Inc. | NOTE: Python has no need of forward class declarations:
#class DragonSoulTable

class DSManager(singleton):
    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self._m_pTable = None

        self._m_pTable = None

    def close(self):
        if self._m_pTable:
            if self._m_pTable is not None:
                self._m_pTable.close()

    def ReadDragonSoulTableFile(self, c_pszFileName):
        self._m_pTable = DragonSoulTable()
        return self._m_pTable.ReadDragonSoulTableFile(c_pszFileName)

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: void GetDragonSoulInfo(uint dwVnum, byte& bType, byte& bGrade, byte& bStep, byte& bStrength) const
    def GetDragonSoulInfo(self, dwVnum, bType, bGrade, bStep, bStrength):
        bType.arg_value = Globals.GetType(dwVnum)
        bGrade.arg_value = Globals.GetGradeIdx(dwVnum)
        bStep.arg_value = Globals.GetStepIdx(dwVnum)
        bStrength.arg_value = Globals.GetStrengthIdx(dwVnum)

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: ushort GetBasePosition(const CItem* pItem) const
    def GetBasePosition(self, pItem):
        if None is pItem:
            return LGEMiscellaneous.DEFINECONSTANTS.WORD_MAX

        type = None
        grade_idx = None
        step_idx = None
        strength_idx = None
        temp_ref_type = RefObject(type);
        temp_ref_grade_idx = RefObject(grade_idx);
        temp_ref_step_idx = RefObject(step_idx);
        temp_ref_strength_idx = RefObject(strength_idx);
        self.GetDragonSoulInfo(pItem.GetVnum(), temp_ref_type, temp_ref_grade_idx, temp_ref_step_idx, temp_ref_strength_idx)
        strength_idx = temp_ref_strength_idx.arg_value
        step_idx = temp_ref_step_idx.arg_value
        grade_idx = temp_ref_grade_idx.arg_value
        type = temp_ref_type.arg_value

        col_type = pItem.GetSubType()
        row_type = grade_idx
        if row_type > EDragonSoulGradeTypes.DRAGON_SOUL_GRADE_MAX:
            return LGEMiscellaneous.DEFINECONSTANTS.WORD_MAX

        return col_type * EDragonSoulGradeTypes.DRAGON_SOUL_GRADE_MAX * LGEMiscellaneous.DRAGON_SOUL_BOX_SIZE + row_type * byte(LGEMiscellaneous.DRAGON_SOUL_BOX_SIZE)

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: bool IsValidCellForThisItem(const CItem* pItem, const TItemPos& Cell) const
    def IsValidCellForThisItem(self, pItem, Cell):
        if None is pItem:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        wBaseCell = self.GetBasePosition(pItem)
        if LGEMiscellaneous.DEFINECONSTANTS.WORD_MAX == wBaseCell:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if Cell.window_type != EWindows.DRAGON_SOUL_INVENTORY or (Cell.cell < wBaseCell or Cell.cell >= wBaseCell + ushort(LGEMiscellaneous.DRAGON_SOUL_BOX_SIZE)):
            return LGEMiscellaneous.DEFINECONSTANTS.false
        else:
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))


## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: int GetDuration(const CItem* pItem) const
    def GetDuration(self, pItem):
        return pItem.GetDuration()

    def ExtractDragonHeart(self, ch, pItem, pExtractor = None):
        if None is ch or None is pItem:
            return LGEMiscellaneous.DEFINECONSTANTS.false
        if pItem.IsEquipped():
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("The Dragon Stone cannot be removed."))
            return LGEMiscellaneous.DEFINECONSTANTS.false

        dwVnum = pItem.GetVnum()
        ds_type = None
        grade_idx = None
        step_idx = None
        strength_idx = None
        temp_ref_ds_type = RefObject(ds_type);
        temp_ref_grade_idx = RefObject(grade_idx);
        temp_ref_step_idx = RefObject(step_idx);
        temp_ref_strength_idx = RefObject(strength_idx);
        self.GetDragonSoulInfo(dwVnum, temp_ref_ds_type, temp_ref_grade_idx, temp_ref_step_idx, temp_ref_strength_idx)
        strength_idx = temp_ref_strength_idx.arg_value
        step_idx = temp_ref_step_idx.arg_value
        grade_idx = temp_ref_grade_idx.arg_value
        ds_type = temp_ref_ds_type.arg_value

        iBonus = 0

        if None is not pExtractor:
            iBonus = pExtractor.GetValue(0)

        vec_chargings = []
        vec_probs = []

        if not self._m_pTable.GetDragonHeartExtValues(ds_type, grade_idx, vec_chargings, vec_probs):
            return LGEMiscellaneous.DEFINECONSTANTS.false

        idx = Globals.Gamble(vec_probs)

        sum = 0.0
        if -1 == idx:
            #lani_err("Gamble is failed. ds_type(%d), grade_idx(%d)", ds_type, grade_idx)
            return LGEMiscellaneous.DEFINECONSTANTS.false

        fCharge = vec_chargings[idx] * (100 + iBonus) / 100.0
        fCharge = std::MINMAX  (0.0, fCharge, 100.0)

        if fCharge < FLT_EPSILON:
            pItem.SetCount(pItem.GetCount() - 1)
            if None is not pExtractor:
                pExtractor.SetCount(pExtractor.GetCount() - 1)

            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Dragon Stone remaining duration has been extracted."))
            return LGEMiscellaneous.DEFINECONSTANTS.false
        else:
            pDH = ITEM_MANAGER.instance().CreateItem(uint(Globals.DRAGON_HEART_VNUM), 1, 0, DefineConstants.false, -1, DefineConstants.false)

            if None is pDH:
                #lani_err("Cannot create DRAGON_HEART(%d).", Globals.DRAGON_HEART_VNUM)
                return None

            pItem.SetCount(pItem.GetCount() - 1)
            if None is not pExtractor:
                pExtractor.SetCount(pExtractor.GetCount() - 1)

            iCharge = int((fCharge + 0.5))
            pDH.SetSocket(EItemDragonSoulSockets.LG_ITEM_SOCKET_CHARGING_AMOUNT_IDX, iCharge, ((not DefineConstants.false)))
            ch.AutoGiveItem(pDH, ((not LGEMiscellaneous.DEFINECONSTANTS.false)))

            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Remaining duration extraction failed."))
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def PullOut(self, ch, DestCell, pItem, pExtractor = None):
        if None is ch or None is pItem.arg_value:
            #lani_err("NULL POINTER. ch(%p) or pItem(%p)", ch, pItem.arg_value)
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if not self.IsValidCellForThisItem(pItem.arg_value, DestCell):
            iEmptyCell = ch.GetEmptyDragonSoulInventory(pItem.arg_value)
            if iEmptyCell < 0:
                ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("There isn't enough space in the inventory."))
                return LGEMiscellaneous.DEFINECONSTANTS.false
            else:
                DestCell.window_type = EWindows.DRAGON_SOUL_INVENTORY
                DestCell.cell = iEmptyCell

        if (not pItem.arg_value.IsEquipped()) or not pItem.arg_value.RemoveFromCharacter():
            return LGEMiscellaneous.DEFINECONSTANTS.false

        bSuccess = None
        dwByProduct = 0
        iBonus = 0
        fProb = None
        fDice = None
            dwVnum = pItem.arg_value.GetVnum()

            ds_type = None
            grade_idx = None
            step_idx = None
            strength_idx = None
            temp_ref_ds_type = RefObject(ds_type);
            temp_ref_grade_idx = RefObject(grade_idx);
            temp_ref_step_idx = RefObject(step_idx);
            temp_ref_strength_idx = RefObject(strength_idx);
            self.GetDragonSoulInfo(pItem.arg_value.GetVnum(), temp_ref_ds_type, temp_ref_grade_idx, temp_ref_step_idx, temp_ref_strength_idx)
            strength_idx = temp_ref_strength_idx.arg_value
            step_idx = temp_ref_step_idx.arg_value
            grade_idx = temp_ref_grade_idx.arg_value
            ds_type = temp_ref_ds_type.arg_value

            temp_ref_fProb = RefObject(fProb);
            temp_ref_dwByProduct = RefObject(dwByProduct);
            if not self._m_pTable.GetDragonSoulExtValues(ds_type, grade_idx, temp_ref_fProb, temp_ref_dwByProduct):
                dwByProduct = temp_ref_dwByProduct.arg_value
                fProb = temp_ref_fProb.arg_value
                pItem.arg_value.AddToCharacter(ch, DestCell)
                return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
            else:
                dwByProduct = temp_ref_dwByProduct.arg_value
                fProb = temp_ref_fProb.arg_value


            if None is not pExtractor:
                iBonus = pExtractor.GetValue(EItemValueIdice.ITEM_VALUE_DRAGON_SOUL_POLL_OUT_BONUS_IDX)
                pExtractor.SetCount(pExtractor.GetCount() - 1)
            fDice = fnumber(0.0, 100.0)
            bSuccess = fDice <= (fProb * (100 + iBonus) / 100.0)

            buf = str(['\0' for _ in range(128)])

            if bSuccess:
                ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Dragon Stone has been removed."))
                pItem.arg_value.AddToCharacter(ch, DestCell)
                return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
            else:
                ITEM_MANAGER.instance().DestroyItem(pItem.arg_value)
                pItem.arg_value = None
                if dwByProduct != 0:
                    pByProduct = ch.AutoGiveItem(dwByProduct, ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
                    if pByProduct:
                        ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Removal of Dragon Stone failed. But you have received the following: %s"), pByProduct.GetName(LOCALE_LANIATUS))
                    else:
                        ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Removal of Dragon Stone failed."))
                else:
                    ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Removal of Dragon Stone failed."))

        return bSuccess

    def DoRefineGrade(self, ch, aItemPoses):
        if None is ch:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if None == aItemPoses:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if not ch.DragonSoul_RefineWindow_CanRefine():
            #lani_err("%s do not activate DragonSoulRefineWindow. But how can he come here?", ch.GetName(LOCALE_LANIATUS))
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, "[SYSTEM ERROR]You cannot upgrade dragon soul without refine window.")
            return LGEMiscellaneous.DEFINECONSTANTS.false

        set_items = std::set()
        i = 0
        while i < LGEMiscellaneous.DRAGON_SOUL_REFINE_GRID_SIZE:
            if aItemPoses[i].IsEquipPosition():
                return LGEMiscellaneous.DEFINECONSTANTS.false
            pItem = ch.GetItem(aItemPoses[i])
            if None is not pItem:
                if not pItem.IsDragonSoul():
                    ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("This item is not required for improving the clarity level."))
                    self._SendRefineResultPacket(ch, EPacketCGDragonSoulSubHeaderType.DS_SUB_LG_HEADER_REFINE_FAIL_INVALID_MATERIAL, TItemPos(pItem.GetWindow(), pItem.GetCell()))

                    return LGEMiscellaneous.DEFINECONSTANTS.false

                set_items.insert(pItem)
            i += 1

        if set_items.size() == 0:
            self._SendRefineResultPacket(ch, EPacketCGDragonSoulSubHeaderType.DS_SUB_LG_HEADER_REFINE_FAIL_NOT_ENOUGH_MATERIAL, NPOS)
            return LGEMiscellaneous.DEFINECONSTANTS.false

        count = set_items.size()
        need_count = 0
        fee = 0
        vec_probs = []

        ds_type = None
        grade_idx = None
        step_idx = None
        strength_idx = None
        result_grade = None

        it = set_items.begin()
            pItem = *it

            temp_ref_ds_type = RefObject(ds_type);
            temp_ref_grade_idx = RefObject(grade_idx);
            temp_ref_step_idx = RefObject(step_idx);
            temp_ref_strength_idx = RefObject(strength_idx);
            self.GetDragonSoulInfo(pItem.GetVnum(), temp_ref_ds_type, temp_ref_grade_idx, temp_ref_step_idx, temp_ref_strength_idx)
            strength_idx = temp_ref_strength_idx.arg_value
            step_idx = temp_ref_step_idx.arg_value
            grade_idx = temp_ref_grade_idx.arg_value
            ds_type = temp_ref_ds_type.arg_value

            temp_ref_need_count = RefObject(need_count);
            temp_ref_fee = RefObject(fee);
            if not self._m_pTable.GetRefineGradeValues(ds_type, grade_idx, temp_ref_need_count, temp_ref_fee, vec_probs):
                fee = temp_ref_fee.arg_value
                need_count = temp_ref_need_count.arg_value
                ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("This item cannot be advanced this way."))
                self._SendRefineResultPacket(ch, EPacketCGDragonSoulSubHeaderType.DS_SUB_LG_HEADER_REFINE_FAIL_INVALID_MATERIAL, TItemPos(pItem.GetWindow(), pItem.GetCell()))

                return LGEMiscellaneous.DEFINECONSTANTS.false
            else:
                fee = temp_ref_fee.arg_value
                need_count = temp_ref_need_count.arg_value
        it += 1
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: while (++it != set_items.end())
        while it != set_items.end():
            pItem = *it

            if pItem.IsEquipped():
                return LGEMiscellaneous.DEFINECONSTANTS.false

            if ds_type != Globals.GetType(pItem.GetVnum()) or grade_idx != Globals.GetGradeIdx(pItem.GetVnum()):
                ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("This item cannot be advanced this way."))
                self._SendRefineResultPacket(ch, EPacketCGDragonSoulSubHeaderType.DS_SUB_LG_HEADER_REFINE_FAIL_INVALID_MATERIAL, TItemPos(pItem.GetWindow(), pItem.GetCell()))

                return LGEMiscellaneous.DEFINECONSTANTS.false
            it += 1

        if count != need_count:
            #lani_err("Possiblity of invalid client. Name %s", ch.GetName(LOCALE_LANIATUS))
            bSubHeader = EPacketCGDragonSoulSubHeaderType.DS_SUB_LG_HEADER_REFINE_FAIL_NOT_ENOUGH_MATERIAL if count < need_count else EPacketCGDragonSoulSubHeaderType.DS_SUB_LG_HEADER_REFINE_FAIL_TOO_MUCH_MATERIAL
            self._SendRefineResultPacket(ch, bSubHeader, NPOS)
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if ch.GetGold() < fee:
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Not enough Yang for an advancement."))
            self._SendRefineResultPacket(ch, EPacketCGDragonSoulSubHeaderType.DS_SUB_LG_HEADER_REFINE_FAIL_NOT_ENOUGH_MONEY, NPOS)
            return LGEMiscellaneous.DEFINECONSTANTS.false

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if (-1 == (result_grade = Gamble(vec_probs)))
        if -1 == (result_grade = Globals.Gamble(vec_probs)):
            #lani_err("Gamble failed. See RefineGardeTables' probabilities")
            return LGEMiscellaneous.DEFINECONSTANTS.false

        pResultItem = ITEM_MANAGER.instance().CreateItem(self._MakeDragonSoulVnum(ds_type, byte(int(result_grade)), 0, 0), 1, 0, DefineConstants.false, -1, DefineConstants.false)

        if None is pResultItem:
            #lani_err("INVALID DRAGON SOUL(%d)", self._MakeDragonSoulVnum(ds_type, byte(int(result_grade)), 0, 0))
            return LGEMiscellaneous.DEFINECONSTANTS.false

        ch.PointChange(EPointTypes.LG_POINT_GOLD, -fee, DefineConstants.false, DefineConstants.false)
        left_count = need_count

        it = set_items.begin()
        while it is not set_items.end():
            pItem = *it
            n = int(pItem.GetCount())
            if left_count > n:
                pItem.RemoveFromCharacter()
                ITEM_MANAGER.instance().DestroyItem(pItem)
                left_count -= n
            else:
                pItem.SetCount(uint(n - left_count))
            it += 1

        ch.AutoGiveItem(pResultItem, ((not LGEMiscellaneous.DEFINECONSTANTS.false)))

        if result_grade > grade_idx:
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Improvement of the clarity level successful."))
            self._SendRefineResultPacket(ch, EPacketCGDragonSoulSubHeaderType.DS_SUB_LG_HEADER_REFINE_SUCCEED, TItemPos(pResultItem.GetWindow(), pResultItem.GetCell()))
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
        else:
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Improvement of the clarity level failed."))
            self._SendRefineResultPacket(ch, EPacketCGDragonSoulSubHeaderType.DS_SUB_LG_HEADER_REFINE_FAIL, TItemPos(pResultItem.GetWindow(), pResultItem.GetCell()))
            return LGEMiscellaneous.DEFINECONSTANTS.false

    def DoRefineStep(self, ch, aItemPoses):
        if None is ch:
            return LGEMiscellaneous.DEFINECONSTANTS.false
        if None == aItemPoses:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if not ch.DragonSoul_RefineWindow_CanRefine():
            #lani_err("%s do not activate DragonSoulRefineWindow. But how can he come here?", ch.GetName(LOCALE_LANIATUS))
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, "[SYSTEM ERROR]You cannot use dragon soul refine window.")
            return LGEMiscellaneous.DEFINECONSTANTS.false

        set_items = std::set()
        i = 0
        while i < LGEMiscellaneous.DRAGON_SOUL_REFINE_GRID_SIZE:
            pItem = ch.GetItem(aItemPoses[i])
            if None is not pItem:
                if not pItem.IsDragonSoul():
                    ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("This item is not required for refinement."))
                    self._SendRefineResultPacket(ch, EPacketCGDragonSoulSubHeaderType.DS_SUB_LG_HEADER_REFINE_FAIL_INVALID_MATERIAL, TItemPos(pItem.GetWindow(), pItem.GetCell()))
                    return LGEMiscellaneous.DEFINECONSTANTS.false
                set_items.insert(pItem)
            i += 1

        if set_items.size() == 0:
            self._SendRefineResultPacket(ch, EPacketCGDragonSoulSubHeaderType.DS_SUB_LG_HEADER_REFINE_FAIL_NOT_ENOUGH_MATERIAL, NPOS)
            return LGEMiscellaneous.DEFINECONSTANTS.false

        stGroupName = ""
        count = set_items.size()
        need_count = 0
        fee = 0
        vec_probs = []

        ds_type = None
        grade_idx = None
        step_idx = None
        strength_idx = None
        result_step = None

        it = set_items.begin()
            pItem = *it
            temp_ref_ds_type = RefObject(ds_type);
            temp_ref_grade_idx = RefObject(grade_idx);
            temp_ref_step_idx = RefObject(step_idx);
            temp_ref_strength_idx = RefObject(strength_idx);
            self.GetDragonSoulInfo(pItem.GetVnum(), temp_ref_ds_type, temp_ref_grade_idx, temp_ref_step_idx, temp_ref_strength_idx)
            strength_idx = temp_ref_strength_idx.arg_value
            step_idx = temp_ref_step_idx.arg_value
            grade_idx = temp_ref_grade_idx.arg_value
            ds_type = temp_ref_ds_type.arg_value

            temp_ref_need_count = RefObject(need_count);
            temp_ref_fee = RefObject(fee);
            if not self._m_pTable.GetRefineStepValues(ds_type, step_idx, temp_ref_need_count, temp_ref_fee, vec_probs):
                fee = temp_ref_fee.arg_value
                need_count = temp_ref_need_count.arg_value
                ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("This item cannot be advanced this way."))
                self._SendRefineResultPacket(ch, EPacketCGDragonSoulSubHeaderType.DS_SUB_LG_HEADER_REFINE_FAIL_INVALID_MATERIAL, TItemPos(pItem.GetWindow(), pItem.GetCell()))
                return LGEMiscellaneous.DEFINECONSTANTS.false
            else:
                fee = temp_ref_fee.arg_value
                need_count = temp_ref_need_count.arg_value

        it += 1
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: while(++it != set_items.end())
        while it != set_items.end():
            pItem = *it

            if pItem.IsEquipped():
                return LGEMiscellaneous.DEFINECONSTANTS.false
            if ds_type != Globals.GetType(pItem.GetVnum()) or grade_idx != Globals.GetGradeIdx(pItem.GetVnum()) or step_idx != Globals.GetStepIdx(pItem.GetVnum()):
                ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("This item cannot be advanced this way."))
                self._SendRefineResultPacket(ch, EPacketCGDragonSoulSubHeaderType.DS_SUB_LG_HEADER_REFINE_FAIL_INVALID_MATERIAL, TItemPos(pItem.GetWindow(), pItem.GetCell()))
                return LGEMiscellaneous.DEFINECONSTANTS.false
            it += 1

        if count != need_count:
            #lani_err("Possiblity of invalid client. Name %s", ch.GetName(LOCALE_LANIATUS))
            bSubHeader = EPacketCGDragonSoulSubHeaderType.DS_SUB_LG_HEADER_REFINE_FAIL_NOT_ENOUGH_MATERIAL if count < need_count else EPacketCGDragonSoulSubHeaderType.DS_SUB_LG_HEADER_REFINE_FAIL_TOO_MUCH_MATERIAL
            self._SendRefineResultPacket(ch, bSubHeader, NPOS)
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if ch.GetGold() < fee:
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Not enough Yang for an advancement."))
            self._SendRefineResultPacket(ch, EPacketCGDragonSoulSubHeaderType.DS_SUB_LG_HEADER_REFINE_FAIL_NOT_ENOUGH_MONEY, NPOS)
            return LGEMiscellaneous.DEFINECONSTANTS.false

        sum = 0.0

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if (-1 == (result_step = Gamble(vec_probs)))
        if -1 == (result_step = Globals.Gamble(vec_probs)):
            #lani_err("Gamble failed. See RefineStepTables' probabilities")
            return LGEMiscellaneous.DEFINECONSTANTS.false

        pResultItem = ITEM_MANAGER.instance().CreateItem(self._MakeDragonSoulVnum(ds_type, grade_idx, byte(int(result_step)), 0), 1, 0, DefineConstants.false, -1, DefineConstants.false)

        if None is pResultItem:
            #lani_err("INVALID DRAGON SOUL(%d)", self._MakeDragonSoulVnum(ds_type, grade_idx, byte(int(result_step)), 0))
            return LGEMiscellaneous.DEFINECONSTANTS.false

        ch.PointChange(EPointTypes.LG_POINT_GOLD, -fee, DefineConstants.false, DefineConstants.false)
        left_count = need_count
        it = set_items.begin()
        while it is not set_items.end():
            pItem = *it
            n = int(pItem.GetCount())
            if left_count > n:
                pItem.RemoveFromCharacter()
                ITEM_MANAGER.instance().DestroyItem(pItem)
                left_count -= n
            else:
                pItem.SetCount(uint(n - left_count))
            it += 1

        ch.AutoGiveItem(pResultItem, ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
        if result_step > step_idx:
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Improvement of the clarity level successful."))
            self._SendRefineResultPacket(ch, EPacketCGDragonSoulSubHeaderType.DS_SUB_LG_HEADER_REFINE_SUCCEED, TItemPos(pResultItem.GetWindow(), pResultItem.GetCell()))
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
        else:
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Refinement up one class failed."))
            self._SendRefineResultPacket(ch, EPacketCGDragonSoulSubHeaderType.DS_SUB_LG_HEADER_REFINE_FAIL, TItemPos(pResultItem.GetWindow(), pResultItem.GetCell()))
            return LGEMiscellaneous.DEFINECONSTANTS.false

    def DoRefineStrength(self, ch, aItemPoses):
        if None is ch:
            return LGEMiscellaneous.DEFINECONSTANTS.false
        if None == aItemPoses:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if not ch.DragonSoul_RefineWindow_CanRefine():
            #lani_err("%s do not activate DragonSoulRefineWindow. But how can he come here?", ch.GetName(LOCALE_LANIATUS))
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, "[SYSTEM ERROR]You cannot use dragon soul refine window.")
            return LGEMiscellaneous.DEFINECONSTANTS.false

        set_items = std::set()
        i = 0
        while i < LGEMiscellaneous.DRAGON_SOUL_REFINE_GRID_SIZE:
            pItem = ch.GetItem(aItemPoses[i])
            if pItem:
                set_items.insert(pItem)
            i += 1
        if set_items.size() == 0:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        fee = None

        pRefineStone = None
        pDragonSoul = None
        it = set_items.begin()
        while it is not set_items.end():
            pItem = *it

            if pItem.IsEquipped():
                return LGEMiscellaneous.DEFINECONSTANTS.false

            if pItem.IsDragonSoul():
                if pDragonSoul is not None:
                    self._SendRefineResultPacket(ch, EPacketCGDragonSoulSubHeaderType.DS_SUB_LG_HEADER_REFINE_FAIL_TOO_MUCH_MATERIAL, TItemPos(pItem.GetWindow(), pItem.GetCell()))
                    return LGEMiscellaneous.DEFINECONSTANTS.false
                pDragonSoul = pItem
            elif Globals.IsDragonSoulRefineMaterial(pItem):
                if pRefineStone is not None:
                    self._SendRefineResultPacket(ch, EPacketCGDragonSoulSubHeaderType.DS_SUB_LG_HEADER_REFINE_FAIL_TOO_MUCH_MATERIAL, TItemPos(pItem.GetWindow(), pItem.GetCell()))
                    ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You do not own the materials required to strengthen the Dragon Stone."))
                    return LGEMiscellaneous.DEFINECONSTANTS.false
                pRefineStone = pItem
            else:
                ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("This item is not required for refinement."))
                self._SendRefineResultPacket(ch, EPacketCGDragonSoulSubHeaderType.DS_SUB_LG_HEADER_REFINE_FAIL_INVALID_MATERIAL, TItemPos(pItem.GetWindow(), pItem.GetCell()))
                return LGEMiscellaneous.DEFINECONSTANTS.false
            it += 1

        bType = None
        bGrade = None
        bStep = None
        bStrength = None

        if pDragonSoul is None or pRefineStone is None:
            self._SendRefineResultPacket(ch, EPacketCGDragonSoulSubHeaderType.DS_SUB_LG_HEADER_REFINE_FAIL_NOT_ENOUGH_MATERIAL, NPOS)

            return LGEMiscellaneous.DEFINECONSTANTS.false

        if None is not pDragonSoul:
            temp_ref_bType = RefObject(bType);
            temp_ref_bGrade = RefObject(bGrade);
            temp_ref_bStep = RefObject(bStep);
            temp_ref_bStrength = RefObject(bStrength);
            self.GetDragonSoulInfo(pDragonSoul.GetVnum(), temp_ref_bType, temp_ref_bGrade, temp_ref_bStep, temp_ref_bStrength)
            bStrength = temp_ref_bStrength.arg_value
            bStep = temp_ref_bStep.arg_value
            bGrade = temp_ref_bGrade.arg_value
            bType = temp_ref_bType.arg_value

            fWeight = 0.0
            temp_ref_fWeight = RefObject(fWeight);
            if not self._m_pTable.GetWeight(bType, bGrade, bStep, byte(bStrength + 1), temp_ref_fWeight):
                fWeight = temp_ref_fWeight.arg_value
                ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("This Dragon Stone cannot be used for refinement."))
                self._SendRefineResultPacket(ch, EPacketCGDragonSoulSubHeaderType.DS_SUB_LG_HEADER_REFINE_FAIL_MAX_REFINE, TItemPos(pDragonSoul.GetWindow(), pDragonSoul.GetCell()))
                return LGEMiscellaneous.DEFINECONSTANTS.false
            else:
                fWeight = temp_ref_fWeight.arg_value
            if fWeight < FLT_EPSILON:
                ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("This Dragon Stone cannot be used for refinement."))
                self._SendRefineResultPacket(ch, EPacketCGDragonSoulSubHeaderType.DS_SUB_LG_HEADER_REFINE_FAIL_MAX_REFINE, TItemPos(pDragonSoul.GetWindow(), pDragonSoul.GetCell()))
                return LGEMiscellaneous.DEFINECONSTANTS.false

        fProb = None
        temp_ref_fee = RefObject(fee);
        temp_ref_fProb = RefObject(fProb);
        if not self._m_pTable.GetRefineStrengthValues(bType, pRefineStone.GetSubType(), bStrength, temp_ref_fee, temp_ref_fProb):
            fProb = temp_ref_fProb.arg_value
            fee = temp_ref_fee.arg_value
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("This Dragon Stone cannot be used for refinement."))
            self._SendRefineResultPacket(ch, EPacketCGDragonSoulSubHeaderType.DS_SUB_LG_HEADER_REFINE_FAIL_INVALID_MATERIAL, TItemPos(pDragonSoul.GetWindow(), pDragonSoul.GetCell()))

            return LGEMiscellaneous.DEFINECONSTANTS.false
        else:
            fProb = temp_ref_fProb.arg_value
            fee = temp_ref_fee.arg_value

        if ch.GetGold() < fee:
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Not enough Yang for an advancement."))
            self._SendRefineResultPacket(ch, EPacketCGDragonSoulSubHeaderType.DS_SUB_LG_HEADER_REFINE_FAIL_NOT_ENOUGH_MONEY, NPOS)
            return LGEMiscellaneous.DEFINECONSTANTS.false

        ch.PointChange(EPointTypes.LG_POINT_GOLD, -fee, DefineConstants.false, DefineConstants.false)
        pResult = None
        bSubHeader = None

        if fnumber(0.0, 100.0) <= fProb:
            pResult = ITEM_MANAGER.instance().CreateItem(self._MakeDragonSoulVnum(bType, bGrade, bStep, byte(bStrength + 1)), 1, 0, DefineConstants.false, -1, DefineConstants.false)
            if None is pResult:
                #lani_err("INVALID DRAGON SOUL(%d)", self._MakeDragonSoulVnum(bType, bGrade, bStep, byte(bStrength + 1)))
                return LGEMiscellaneous.DEFINECONSTANTS.false

            pDragonSoul.CopyAttributeTo(pResult)
            self._RefreshItemAttributes(pResult)

            pDragonSoul.SetCount(pDragonSoul.GetCount() - 1)
            pRefineStone.SetCount(pRefineStone.GetCount() - 1)

            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Strengthening was successful."))
            ch.AutoGiveItem(pResult, ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
            bSubHeader = EPacketCGDragonSoulSubHeaderType.DS_SUB_LG_HEADER_REFINE_SUCCEED
        else:
            if bStrength != 0:
                pResult = ITEM_MANAGER.instance().CreateItem(self._MakeDragonSoulVnum(bType, bGrade, bStep, byte(bStrength - 1)), 1, 0, DefineConstants.false, -1, DefineConstants.false)
                if None is pResult:
                    #lani_err("INVALID DRAGON SOUL(%d)", self._MakeDragonSoulVnum(bType, bGrade, bStep, byte(bStrength - 1)))
                    return LGEMiscellaneous.DEFINECONSTANTS.false
                pDragonSoul.CopyAttributeTo(pResult)
                self._RefreshItemAttributes(pResult)
            bSubHeader = EPacketCGDragonSoulSubHeaderType.DS_SUB_LG_HEADER_REFINE_FAIL

            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Strengthening failed."))

            pDragonSoul.SetCount(pDragonSoul.GetCount() - 1)
            pRefineStone.SetCount(pRefineStone.GetCount() - 1)
            if None is not pResult:
                ch.AutoGiveItem(pResult, ((not LGEMiscellaneous.DEFINECONSTANTS.false)))

        self._SendRefineResultPacket(ch, bSubHeader,NPOS if None is pResult is not None else TItemPos(pResult.GetWindow(), pResult.GetCell()))

        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def DragonSoulItemInitialize(self, pItem):
        if None is pItem or not pItem.IsDragonSoul():
            return LGEMiscellaneous.DEFINECONSTANTS.false
        self._PutAttributes(pItem)
        time = DSManager.instance().GetDuration(pItem)
        if time > 0:
            pItem.SetSocket(Globals.LG_ITEM_SOCKET_REMAIN_SEC, time, ((not DefineConstants.false)))
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: bool IsTimeLeftDragonSoul(CItem* pItem) const
    def IsTimeLeftDragonSoul(self, pItem):
        if pItem is None:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if pItem.GetProto().cLimitTimerBasedOnWearIndex >= 0:
            return pItem.GetSocket(Globals.LG_ITEM_SOCKET_REMAIN_SEC) > 0
        else:
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: int LeftTime(CItem* pItem) const
    def LeftTime(self, pItem):
        if pItem is None:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if pItem.GetProto().cLimitTimerBasedOnWearIndex >= 0:
            return pItem.GetSocket(Globals.LG_ITEM_SOCKET_REMAIN_SEC)
        else:
            return numeric_limits.max()

    def ActivateDragonSoul(self, pItem):
        if None is pItem:
            return LGEMiscellaneous.DEFINECONSTANTS.false
        pOwner = pItem.GetOwner()
        if None is pOwner:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        deck_idx = pOwner.DragonSoul_GetActiveDeck()

        if deck_idx < 0:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if LGEMiscellaneous.INVENTORY_MAX_NUM + EWearPositions.WEAR_MAX_NUM + EDragonSoulSubType.DS_SLOT_MAX * deck_idx <= pItem.GetCell() and pItem.GetCell() < LGEMiscellaneous.INVENTORY_MAX_NUM + EWearPositions.WEAR_MAX_NUM + EDragonSoulSubType.DS_SLOT_MAX * (deck_idx + 1):
            if self.IsTimeLeftDragonSoul(pItem) and not self.IsActiveDragonSoul(pItem):
                pItem.ModifyPoints(((not LGEMiscellaneous.DEFINECONSTANTS.false)))
                pItem.SetSocket(EItemDragonSoulSockets.LG_ITEM_SOCKET_DRAGON_SOUL_ACTIVE_IDX, 1, ((not DefineConstants.false)))

                pItem.StartTimerBasedOnWearExpireEvent()
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
        else:
            return LGEMiscellaneous.DEFINECONSTANTS.false

    def DeactivateDragonSoul(self, pItem, bSkipRefreshOwnerActiveState = LGEMiscellaneous.DefineConstants.false):
        if None is pItem:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        pOwner = pItem.GetOwner()
        if None is pOwner:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if not self.IsActiveDragonSoul(pItem):
            return LGEMiscellaneous.DEFINECONSTANTS.false

        pItem.StopTimerBasedOnWearExpireEvent()
        pItem.SetSocket(EItemDragonSoulSockets.LG_ITEM_SOCKET_DRAGON_SOUL_ACTIVE_IDX, 0, ((not DefineConstants.false)))
        pItem.ModifyPoints(LGEMiscellaneous.DEFINECONSTANTS.false)

        if LGEMiscellaneous.DEFINECONSTANTS.false == bSkipRefreshOwnerActiveState:
            self._RefreshDragonSoulState(pOwner)

        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: bool IsActiveDragonSoul(CItem* pItem) const
    def IsActiveDragonSoul(self, pItem):
        return pItem.GetSocket(EItemDragonSoulSockets.LG_ITEM_SOCKET_DRAGON_SOUL_ACTIVE_IDX) != 0

    def _SendRefineResultPacket(self, ch, bSubHeader, pos):
        pack = SPacketGCDragonSoulRefine()
        pack.bSubType = bSubHeader

        if pos.IsValidItemPosition():
            pack.Pos = pos
        d = ch.GetDesc()
        if None is d:
            return
        else:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            d.Packet(pack, sizeof(pack))

    def _RefreshDragonSoulState(self, ch):
        if None is ch:
            return
        i = WEAR_MAX_NUM
        while i < EWearPositions.WEAR_MAX_NUM + EDragonSoulSubType.DS_SLOT_MAX * EDragonSoulDeckType.DRAGON_SOUL_DECK_MAX_NUM:
            pItem = ch.GetWear(ushort(i))
            if pItem is not None:
                if self.IsActiveDragonSoul(pItem):
                    return
            i += 1
        ch.DragonSoul_DeactivateAll()

    def _MakeDragonSoulVnum(self, bType, grade, step, refine):
        return uint(bType * 10000 + grade * 1000 + step * 100 + refine * 10)

    def _PutAttributes(self, pDS):
        if not pDS.IsDragonSoul():
            #lani_err("This item(ID : %d) is not DragonSoul.", pDS.GetID())
            return LGEMiscellaneous.DEFINECONSTANTS.false

        ds_type = None
        grade_idx = None
        step_idx = None
        strength_idx = None
        temp_ref_ds_type = RefObject(ds_type);
        temp_ref_grade_idx = RefObject(grade_idx);
        temp_ref_step_idx = RefObject(step_idx);
        temp_ref_strength_idx = RefObject(strength_idx);
        self.GetDragonSoulInfo(pDS.GetVnum(), temp_ref_ds_type, temp_ref_grade_idx, temp_ref_step_idx, temp_ref_strength_idx)
        strength_idx = temp_ref_strength_idx.arg_value
        step_idx = temp_ref_step_idx.arg_value
        grade_idx = temp_ref_grade_idx.arg_value
        ds_type = temp_ref_ds_type.arg_value

        vec_basic_applys = []
        vec_addtional_applys = []

        if not self._m_pTable.GetBasicApplys(ds_type, vec_basic_applys):
            #lani_err("There is no BasicApply about %d type dragon soul.", ds_type)
            return LGEMiscellaneous.DEFINECONSTANTS.false
        if not self._m_pTable.GetAdditionalApplys(ds_type, vec_addtional_applys):
            #lani_err("There is no AdditionalApply about %d type dragon soul.", ds_type)
            return LGEMiscellaneous.DEFINECONSTANTS.false


        basic_apply_num = None
        add_min = None
        add_max = None
        temp_ref_basic_apply_num = RefObject(basic_apply_num);
        temp_ref_add_min = RefObject(add_min);
        temp_ref_add_max = RefObject(add_max);
        if not self._m_pTable.GetApplyNumSettings(ds_type, grade_idx, temp_ref_basic_apply_num, temp_ref_add_min, temp_ref_add_max):
            add_max = temp_ref_add_max.arg_value
            add_min = temp_ref_add_min.arg_value
            basic_apply_num = temp_ref_basic_apply_num.arg_value
            #lani_err("In ApplyNumSettings, INVALID VALUES Group type(%d), GRADE idx(%d)", ds_type, grade_idx)
            return LGEMiscellaneous.DEFINECONSTANTS.false
        else:
            add_max = temp_ref_add_max.arg_value
            add_min = temp_ref_add_min.arg_value
            basic_apply_num = temp_ref_basic_apply_num.arg_value

        fWeight = 0.0
        temp_ref_fWeight = RefObject(fWeight);
        if not self._m_pTable.GetWeight(ds_type, grade_idx, step_idx, strength_idx, temp_ref_fWeight):
            fWeight = temp_ref_fWeight.arg_value
            return LGEMiscellaneous.DEFINECONSTANTS.false
        else:
            fWeight = temp_ref_fWeight.arg_value
        fWeight /= 100.0

        n = MIN(basic_apply_num, len(vec_basic_applys))
        for i in range(0, n):
            basic_apply = vec_basic_applys[i]
            bType = basic_apply.apply_type
            sValue = short(int((math.ceil(float(basic_apply.apply_value) * fWeight - 0.01))))

            pDS.SetForceAttribute(i, bType, sValue)

        additional_attr_num = MIN(number(add_min, add_max), 3)

        random_set = []
        if additional_attr_num > 0:
            random_set.resize(additional_attr_num)
            list_probs = std::list()
            i = 0
            while i < len(vec_addtional_applys):
                list_probs.push_back(vec_addtional_applys[i].prob)
                i += 1
            if not Globals.MakeDistinctRandomNumberSet(std::list(list_probs), random_set):
                #lani_err("MakeDistinctRandomNumberSet error.")
                return LGEMiscellaneous.DEFINECONSTANTS.false

            for i in range(0, additional_attr_num):
                r = random_set[i]
                additional_attr = vec_addtional_applys[r]
                bType = additional_attr.apply_type
                sValue = short(int((math.ceil(float(additional_attr.apply_value) * fWeight - 0.01))))

                pDS.SetForceAttribute(Globals.DRAGON_SOUL_ADDITIONAL_ATTR_START_IDX + i, bType, sValue)

        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def _RefreshItemAttributes(self, pDS):
        if not pDS.IsDragonSoul():
            #lani_err("This item(ID : %d) is not DragonSoul.", pDS.GetID())
            return LGEMiscellaneous.DEFINECONSTANTS.false

        ds_type = None
        grade_idx = None
        step_idx = None
        strength_idx = None
        temp_ref_ds_type = RefObject(ds_type);
        temp_ref_grade_idx = RefObject(grade_idx);
        temp_ref_step_idx = RefObject(step_idx);
        temp_ref_strength_idx = RefObject(strength_idx);
        self.GetDragonSoulInfo(pDS.GetVnum(), temp_ref_ds_type, temp_ref_grade_idx, temp_ref_step_idx, temp_ref_strength_idx)
        strength_idx = temp_ref_strength_idx.arg_value
        step_idx = temp_ref_step_idx.arg_value
        grade_idx = temp_ref_grade_idx.arg_value
        ds_type = temp_ref_ds_type.arg_value

        vec_basic_applys = []
        vec_addtional_applys = []

        if not self._m_pTable.GetBasicApplys(ds_type, vec_basic_applys):
            #lani_err("There is no BasicApply about %d type dragon soul.", ds_type)
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if not self._m_pTable.GetAdditionalApplys(ds_type, vec_addtional_applys):
            #lani_err("There is no AdditionalApply about %d type dragon soul.", ds_type)
            return LGEMiscellaneous.DEFINECONSTANTS.false

        basic_apply_num = None
        add_min = None
        add_max = None
        temp_ref_basic_apply_num = RefObject(basic_apply_num);
        temp_ref_add_min = RefObject(add_min);
        temp_ref_add_max = RefObject(add_max);
        if not self._m_pTable.GetApplyNumSettings(ds_type, grade_idx, temp_ref_basic_apply_num, temp_ref_add_min, temp_ref_add_max):
            add_max = temp_ref_add_max.arg_value
            add_min = temp_ref_add_min.arg_value
            basic_apply_num = temp_ref_basic_apply_num.arg_value
            #lani_err("In ApplyNumSettings, INVALID VALUES Group type(%d), GRADE idx(%d)", ds_type, grade_idx)
            return LGEMiscellaneous.DEFINECONSTANTS.false
        else:
            add_max = temp_ref_add_max.arg_value
            add_min = temp_ref_add_min.arg_value
            basic_apply_num = temp_ref_basic_apply_num.arg_value

        fWeight = 0.0
        temp_ref_fWeight = RefObject(fWeight);
        if not self._m_pTable.GetWeight(ds_type, grade_idx, step_idx, strength_idx, temp_ref_fWeight):
            fWeight = temp_ref_fWeight.arg_value
            return LGEMiscellaneous.DEFINECONSTANTS.false
        else:
            fWeight = temp_ref_fWeight.arg_value
        fWeight /= 100.0

        n = MIN(basic_apply_num, len(vec_basic_applys))
        for i in range(0, n):
            basic_apply = vec_basic_applys[i]
            bType = basic_apply.apply_type
            sValue = short(int((math.ceil(float(basic_apply.apply_value) * fWeight - 0.01))))

            pDS.SetForceAttribute(i, bType, sValue)

        i = DRAGON_SOUL_ADDITIONAL_ATTR_START_IDX
        while i < EItemMisc.ITEM_ATTRIBUTE_MAX_NUM:
            bType = pDS.GetAttributeType(i)
            sValue = 0
            if EApplyTypes.APPLY_NONE == bType:
                continue
            j = 0
            while j < len(vec_addtional_applys):
                if vec_addtional_applys[j].apply_type == bType:
                    sValue = short(vec_addtional_applys[j].apply_value)
                    break
                j += 1
            pDS.SetForceAttribute(i, bType, short(int((math.ceil(float(sValue) * fWeight - 0.01)))))
            i += 1
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
