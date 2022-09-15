class CItemAddonManager(singleton):
    def __init__(self):
        pass

    def close(self):
        pass

    def ApplyAddonTo(self, iAddonType, pItem):
        if pItem is None:
            #lani_err("ITEM pointer null")
            return

        iSkillBonus = MINMAX(-30, int((gauss_random(0, 5) + 0.5)), 30)
        iNormalHitBonus = 0
        if abs(iSkillBonus) <= 20:
            iNormalHitBonus = -2 * iSkillBonus + abs(number(-8, 8) + number(-8, 8)) + number(1, 4)
        else:
            iNormalHitBonus = -2 * iSkillBonus + number(1, 5)

        pItem.RemoveAttributeType(EApplyTypes.APPLY_LG_SKILL_DAMAGE_BONUS)
        pItem.RemoveAttributeType(EApplyTypes.APPLY_NORMAL_HIT_DAMAGE_BONUS)
        pItem.AddAttribute(EApplyTypes.APPLY_NORMAL_HIT_DAMAGE_BONUS, short(iNormalHitBonus))
        pItem.AddAttribute(EApplyTypes.APPLY_LG_SKILL_DAMAGE_BONUS, short(iSkillBonus))
