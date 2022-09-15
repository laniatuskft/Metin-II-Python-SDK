from enum import Enum

class POLYMORPH_BONUS_TYPE(Enum):
    POLYMORPH_NO_BONUS = 0
    POLYMORPH_ATK_BONUS = 1
    POLYMORPH_DEF_BONUS = 2
    POLYMORPH_SPD_BONUS = 3

class CPolymorphUtils(singleton):

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self._m_mapSPDType = _boost_func_of_void.unordered_map()
        self._m_mapATKType = _boost_func_of_void.unordered_map()
        self._m_mapDEFType = _boost_func_of_void.unordered_map()

        self._m_mapSPDType.insert((101, 101))
        self._m_mapSPDType.insert((1901, 1901))

    def GetBonusType(self, dwVnum):
        iter = self._m_mapSPDType.find(dwVnum)

        if iter != self._m_mapSPDType.end():
            return POLYMORPH_BONUS_TYPE.POLYMORPH_SPD_BONUS

        iter = self._m_mapATKType.find(dwVnum)

        if iter != self._m_mapATKType.end():
            return POLYMORPH_BONUS_TYPE.POLYMORPH_ATK_BONUS

        iter = self._m_mapDEFType.find(dwVnum)

        if iter != self._m_mapDEFType.end():
            return POLYMORPH_BONUS_TYPE.POLYMORPH_DEF_BONUS

        return POLYMORPH_BONUS_TYPE.POLYMORPH_NO_BONUS

    def PolymorphCharacter(self, pChar, pItem, pMob):
        bySkillLevel = byte(pChar.GetSkillLevel(LGEMiscellaneous.DEFINECONSTANTS.POLYMORPH_LG_SKILL_ID))
        dwDuration = 0
        dwBonusPercent = 0
        iPolyPercent = 0

        if pChar.GetSkillMasterType(LGEMiscellaneous.DEFINECONSTANTS.POLYMORPH_LG_SKILL_ID) == Globals.LG_SKILL_NORMAL:
            dwDuration = 10

        elif pChar.GetSkillMasterType(LGEMiscellaneous.DEFINECONSTANTS.POLYMORPH_LG_SKILL_ID) == Globals.LG_SKILL_MASTER:
            dwDuration = 15

        elif pChar.GetSkillMasterType(LGEMiscellaneous.DEFINECONSTANTS.POLYMORPH_LG_SKILL_ID) == Globals.LG_SKILL_GRAND_MASTER:
            dwDuration = 20

        elif pChar.GetSkillMasterType(LGEMiscellaneous.DEFINECONSTANTS.POLYMORPH_LG_SKILL_ID) == Globals.LG_SKILL_PERFECT_MASTER:
            dwDuration = 25

        else:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        iPolyPercent = pChar.GetLevel() - pMob.m_table.bLevel + pItem.GetSocket(2) + (29 + bySkillLevel)

        if iPolyPercent <= 0:
            pChar.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You have failed to transform."))
            return LGEMiscellaneous.DEFINECONSTANTS.false
        else:
            if number(1, 100) > iPolyPercent:
                pChar.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You have failed to transform."))
                return LGEMiscellaneous.DEFINECONSTANTS.false

        pChar.AddAffect(LaniatusEAffectTypes.LANIA_AFFECT_POLYMORPH, EPointTypes.LG_POINT_POLYMORPH, int(pMob.m_table.dwVnum), EAffectBits.AFF_POLYMORPH, int(dwDuration), 0, ((not LGEMiscellaneous.DEFINECONSTANTS.false)), DefineConstants.false)

        dwBonusPercent = uint(bySkillLevel + pItem.GetSocket(2))

        if self.GetBonusType(pMob.m_table.dwVnum) == POLYMORPH_BONUS_TYPE.POLYMORPH_ATK_BONUS:
            pChar.AddAffect(LaniatusEAffectTypes.LANIA_AFFECT_POLYMORPH, EPointTypes.LG_POINT_ATT_BONUS, int(dwBonusPercent), EAffectBits.AFF_POLYMORPH, int(dwDuration - 1), 0, LGEMiscellaneous.DEFINECONSTANTS.false, DefineConstants.false)

        elif self.GetBonusType(pMob.m_table.dwVnum) == POLYMORPH_BONUS_TYPE.POLYMORPH_DEF_BONUS:
            pChar.AddAffect(LaniatusEAffectTypes.LANIA_AFFECT_POLYMORPH, EPointTypes.LG_POINT_DEF_BONUS, int(dwBonusPercent), EAffectBits.AFF_POLYMORPH, int(dwDuration - 1), 0, LGEMiscellaneous.DEFINECONSTANTS.false, DefineConstants.false)

        elif self.GetBonusType(pMob.m_table.dwVnum) == POLYMORPH_BONUS_TYPE.POLYMORPH_SPD_BONUS:
            pChar.AddAffect(LaniatusEAffectTypes.LANIA_AFFECT_POLYMORPH, EPointTypes.LG_POINT_MOV_SPEED, int(dwBonusPercent), EAffectBits.AFF_POLYMORPH, int(dwDuration - 1), 0, LGEMiscellaneous.DEFINECONSTANTS.false, DefineConstants.false)

        else:

        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def UpdateBookPracticeGrade(self, pChar, pItem):
        if pChar is None or pItem is None:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if pItem.GetSocket(1) > 0:
            pItem.SetSocket(1, pItem.GetSocket(1) - 1, ((not DefineConstants.false)))
        else:
            pChar.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You have finished your training. Please get it from your master."))

        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def GiveBook(self, pChar, dwMobVnum, dwPracticeCount, BookLevel, LevelLimit):
        if pChar is None:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        pItem = pChar.AutoGiveItem(LGEMiscellaneous.DEFINECONSTANTS.POLYMORPH_BOOK_ID, 1)

        if pItem is None:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if CMobManager.instance().Get(dwMobVnum) is None:
            #lani_err("Wrong Polymorph vnum passed: CPolymorphUtils::GiveBook(PID(%d), %d %d %d %d)", pChar.GetPlayerID(), dwMobVnum, dwPracticeCount, BookLevel, LevelLimit)
            return LGEMiscellaneous.DEFINECONSTANTS.false

        pItem.SetSocket(0, int(dwMobVnum), ((not DefineConstants.false)))
        pItem.SetSocket(1, int(dwPracticeCount), ((not DefineConstants.false)))
        pItem.SetSocket(2, BookLevel, ((not DefineConstants.false)))
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def BookUpgrade(self, pChar, pItem):
        if pChar is None or pItem is None:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        pItem.SetSocket(1, pItem.GetSocket(2) * 50, ((not DefineConstants.false)))
        pItem.SetSocket(2, pItem.GetSocket(2)+1, ((not DefineConstants.false)))
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
