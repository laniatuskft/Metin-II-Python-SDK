class CBeltInventoryHelper:

    ## Laniatus Games Studio Inc. | NOTE: This was formerly a static local variable declaration (not allowed in Python):
    GetBeltGradeByRefineLevel_beltGradeByLevelTable = [0, 1, 1, 2, 2, 3, 4, 5, 6, 7]

    @staticmethod
    def GetBeltGradeByRefineLevel(level):
        ## Laniatus Games Studio Inc. | NOTE: This static local variable declaration (not allowed in Python) has been moved just prior to the method:
        #        static byte beltGradeByLevelTable[] = { 0, 1, 1, 2, 2, 3, 4, 5, 6, 7}

        if level >= _countof(GetBeltGradeByRefineLevel_beltGradeByLevelTable):
            #lani_err("CBeltInventoryHelper::GetBeltGradeByRefineLevel - Overflow level (%d", level)
            return 0

        return GetBeltGradeByRefineLevel_beltGradeByLevelTable[level]

    ## Laniatus Games Studio Inc. | NOTE: This was formerly a static local variable declaration (not allowed in Python):
    GetAvailableRuleTableByGrade_availableRuleByGrade = [1, 2, 4, 6, 3, 3, 4, 6, 5, 5, 5, 6, 7, 7, 7, 7] + [0 for _ in range(LGEMiscellaneous.BELT_INVENTORY_SLOT_COUNT - 16)]

    @staticmethod
## Laniatus Games Studio Inc. | WARNING: Python has no equivalent to methods returning pointers to value types:
#ORIGINAL METINII C CODE: static const byte* GetAvailableRuleTableByGrade()
    def GetAvailableRuleTableByGrade():
        ## Laniatus Games Studio Inc. | NOTE: This static local variable declaration (not allowed in Python) has been moved just prior to the method:
        #        static byte availableRuleByGrade[BELT_INVENTORY_SLOT_COUNT] = { 1, 2, 4, 6, 3, 3, 4, 6, 5, 5, 5, 6, 7, 7, 7, 7 }

        return GetAvailableRuleTableByGrade_availableRuleByGrade

    @staticmethod
    def IsAvailableCell(cell, beltGrade):
        ruleTable = CBeltInventoryHelper.GetAvailableRuleTableByGrade()

        return ruleTable[cell] <= beltGrade

    @staticmethod
    def IsExistItemInBeltInventory(pc):
        i = BELT_INVENTORY_SLOT_START
        while i < LGEMiscellaneous2.BELT_INVENTORY_SLOT_END:
            beltInventoryItem = pc.GetInventoryItem(i)

            if None is not beltInventoryItem:
                return True
            i += 1

        return False

    @staticmethod
    def CanMoveIntoBeltInventory(item):
        canMove = False

        if item.GetType() == EItemTypes.ITEM_USE:
            if (item.GetSubType() == EUseSubTypes.USE_POTION) or (item.GetSubType() == EUseSubTypes.USE_POTION_NODELAY) or (item.GetSubType() == EUseSubTypes.USE_ABILITY_UP):
                canMove = True

        return canMove

