class STriggerFunction:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.func = funcDelegate()

    class funcDelegate:
        def invoke(self, ch, causer):
            pass


def AssignTriggers(table):
    if table.bOnClickType >= EOnClickEvents.ON_CLICK_MAX_NUM:
        #lani_err("%s has invalid OnClick value %d", GetName(), table.bOnClickType)
        abort()

    m_triggerOnClick.bType = table.bOnClickType
    m_triggerOnClick.pFunc = OnClickTriggers[table.bOnClickType].func

class FuncFindMobVictim:
    def __init__(self, pkChr, iMaxDistance):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self._m_pkChr = None
        self._m_iMinDistance = 0
        self._m_iMaxDistance = 0
        self._m_lx = 0
        self._m_ly = 0
        self._m_pkChrVictim = None
        self._m_pkChrBuilding = None

        self._m_pkChr = pkChr
        self._m_iMinDistance = ~(1 << 31)
        self._m_iMaxDistance = iMaxDistance
        self._m_lx = pkChr.GetX()
        self._m_ly = pkChr.GetY()
        self._m_pkChrVictim = None
        self._m_pkChrBuilding = None

    def functor_method(self, ent):
        if not ent.IsType(EEntityTypes.ENTITY_CHARACTER):
            return LGEMiscellaneous.DEFINECONSTANTS.false

        pkChr = ent

        if pkChr.IsBuilding() and (pkChr.IsAffectFlag(EAffectBits.AFF_BUILDING_CONSTRUCTION_SMALL) or pkChr.IsAffectFlag(EAffectBits.AFF_BUILDING_CONSTRUCTION_LARGE) or pkChr.IsAffectFlag(EAffectBits.AFF_BUILDING_UPGRADE)):
            self._m_pkChrBuilding = pkChr

        if pkChr.IsNPC():
            if (not pkChr.IsMonster()) or (not self._m_pkChr.IsAttackMob()) or self._m_pkChr.IsAggressive():
                return LGEMiscellaneous.DEFINECONSTANTS.false


        if pkChr.IsDead():
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if pkChr.IsAffectFlag(EAffectBits.AFF_EUNHYUNG) or pkChr.IsAffectFlag(EAffectBits.AFF_INVISIBILITY) or pkChr.IsAffectFlag(EAffectBits.AFF_REVIVE_INVISIBLE):
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if pkChr.IsAffectFlag(EAffectBits.AFF_TERROR) and self._m_pkChr.IsImmune(EImmuneFlags.IMMUNE_TERROR) == LGEMiscellaneous.DEFINECONSTANTS.false:
            if pkChr.GetLevel() >= self._m_pkChr.GetLevel():
                return LGEMiscellaneous.DEFINECONSTANTS.false

        if self._m_pkChr.IsNoAttackShinsu():
            if pkChr.GetEmpire() == 1:
                return LGEMiscellaneous.DEFINECONSTANTS.false

        if self._m_pkChr.IsNoAttackChunjo():
            if pkChr.GetEmpire() == 2:
                return LGEMiscellaneous.DEFINECONSTANTS.false


        if self._m_pkChr.IsNoAttackJinno():
            if pkChr.GetEmpire() == 3:
                return LGEMiscellaneous.DEFINECONSTANTS.false

        iDistance = Globals.DISTANCE_APPROX(self._m_lx - pkChr.GetX(), self._m_ly - pkChr.GetY())

        if iDistance < self._m_iMinDistance and iDistance <= self._m_iMaxDistance:
            self._m_pkChrVictim = pkChr
            self._m_iMinDistance = iDistance
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def GetVictim(self):
        if self._m_pkChrBuilding is not None and self._m_pkChr.GetHP() * 2 > self._m_pkChr.GetMaxHP() or self._m_pkChrVictim is None:
            return self._m_pkChrBuilding

        return (self._m_pkChrVictim)


