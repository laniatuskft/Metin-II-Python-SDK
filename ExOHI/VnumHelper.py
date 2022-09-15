class CItemVnumHelper:
    @staticmethod
    def IsPhoenix(vnum):
        return 53001 == vnum
    @staticmethod
    def IsRamadanMoonRing(vnum):
        return 71135 == vnum
    @staticmethod
    def IsHalloweenCandy(vnum):
        return 71136 == vnum
    @staticmethod
    def IsHappinessRing(vnum):
        return 71143 == vnum
    @staticmethod
    def IsLovePendant(vnum):
        return 71145 == vnum
    @staticmethod
    def IsAcceItem(vnum):
        if (vnum >= 85001 and vnum <= 85008) or (vnum >= 85011 and vnum <= 85018) or (vnum >= 85021 and vnum <= 85024) or (vnum >= 86001 and vnum <= 86008) or (vnum >= 86011 and vnum <= 86018) or (vnum >= 86021 and vnum <= 86028) or (vnum >= 86031 and vnum <= 86038) or (vnum >= 86041 and vnum <= 86048) or (vnum >= 86051 and vnum <= 86058) or (vnum >= 86061 and vnum <= 86068):
            return True
        return False

class CMobVnumHelper:
    @staticmethod
    def IsPhoenix(vnum):
        return 34001 == vnum
    @staticmethod
    def IsIcePhoenix(vnum):
        return 34003 == vnum
    @staticmethod
    def IsPetUsingPetSystem(vnum):
        return (CMobVnumHelper.IsPhoenix(vnum) or CMobVnumHelper.IsReindeerYoung(vnum)) or CMobVnumHelper.IsIcePhoenix(vnum)
    @staticmethod
    def IsReindeerYoung(vnum):
        return 34002 == vnum
    @staticmethod
    def IsRamadanBlackHorse(vnum):
        return 20119 == vnum or 20219 == vnum or 22022 == vnum

class CVnumHelper:
    pass
