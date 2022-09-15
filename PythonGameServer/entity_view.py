def ViewCleanup():
    it = m_map_view.begin()

    while it is not m_map_view.end():
        entity = it.first
        it += 1

        entity.ViewRemove(self, LGEMiscellaneous.DEFINECONSTANTS.false)

    m_map_view.clear()

def ViewReencode():
    if m_bIsObserver:
        return

    EncodeRemovePacket(self)
    EncodeInsertPacket(self)

    it = m_map_view.begin()

    while it is not m_map_view.end():
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: CEntity* entity = (it++)->first;
        entity = (it).first
        it += 1

        EncodeRemovePacket(entity)
        if not m_bIsObserver:
            EncodeInsertPacket(entity)

        if not entity.m_bIsObserver:
            entity.EncodeInsertPacket(self)


def ViewInsert(entity, recursive):
    if self is entity:
        return

    it = m_map_view.find(entity)

    if m_map_view.end() != it:
        it.second = m_iViewAge
        return

    m_map_view.insert(ENTITY_MAP.value_type(entity, m_iViewAge))

    if not entity.m_bIsObserver:
        entity.EncodeInsertPacket(self)

    if recursive:
        entity.ViewInsert(self, LGEMiscellaneous.DEFINECONSTANTS.false)

def ViewRemove(entity, recursive):
    it = m_map_view.find(entity)

    if it == m_map_view.end():
        return

    m_map_view.erase(it)

    if not entity.m_bIsObserver:
        entity.EncodeRemovePacket(self)

    if recursive:
        entity.ViewRemove(self, LGEMiscellaneous.DEFINECONSTANTS.false)

class CFuncViewInsert:


    def __init__(self, ent):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self._dwViewRange = 0
        self.m_me = None

        self._dwViewRange = VIEW_RANGE + VIEW_BONUS_RANGE
        self.m_me = ent

    def functor_method(self, ent):
        if not ent.IsType(EEntityTypes.ENTITY_OBJECT):
            if Globals.DISTANCE_APPROX(ent.GetX() - self.m_me.GetX(), ent.GetY() - self.m_me.GetY()) > self._dwViewRange:
                return

        self.m_me.ViewInsert(ent, ((not DefineConstants.false)))

        if ent.IsType(EEntityTypes.ENTITY_CHARACTER) and self.m_me.IsType(EEntityTypes.ENTITY_CHARACTER):
            chMe = self.m_me
            chEnt = ent

            if chMe.IsPC() and (not chEnt.IsPC()) and (not chEnt.IsWarp()) and not chEnt.IsGoto():
                chEnt.StartStateMachine(1)

def UpdateSectree():
    if not GetSectree():
        if IsType(EEntityTypes.ENTITY_CHARACTER):
            tch = self
            #lani_err("null sectree name: %s %d %d", tch.GetName(LOCALE_LANIATUS), GetX(), GetY())

        return

    m_iViewAge += 1

    f = CFuncViewInsert(self)
    GetSectree().ForEachAround(f.functor_method)

    if m_bObserverModeChange:
        if m_bIsObserver:
            it = m_map_view.begin()

            while it is not m_map_view.end():
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: auto this_it = it++;
                this_it = it
                it += 1
                if this_it.second < m_iViewAge:
                    ent = this_it.first
                    ent.EncodeRemovePacket(self)
                    m_map_view.erase(this_it)
                    ent.ViewRemove(self, LGEMiscellaneous.DEFINECONSTANTS.false)
                else:
                    ent = this_it.first
                    EncodeRemovePacket(ent)
        else:
            it = m_map_view.begin()

            while it is not m_map_view.end():
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: auto this_it = it++;
                this_it = it
                it += 1

                if this_it.second < m_iViewAge:
                    ent = this_it.first
                    ent.EncodeRemovePacket(self)
                    m_map_view.erase(this_it)
                    ent.ViewRemove(self, LGEMiscellaneous.DEFINECONSTANTS.false)
                else:
                    ent = this_it.first
                    ent.EncodeInsertPacket(self)
                    EncodeInsertPacket(ent)

                    ent.ViewInsert(self, ((not LGEMiscellaneous.DEFINECONSTANTS.false)))

        m_bObserverModeChange = LGEMiscellaneous.DEFINECONSTANTS.false
    else:
        if not m_bIsObserver:
            it = m_map_view.begin()

            while it is not m_map_view.end():
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: auto this_it = it++;
                this_it = it
                it += 1

                if this_it.second < m_iViewAge:
                    ent = this_it.first
                    ent.EncodeRemovePacket(self)
                    m_map_view.erase(this_it)
                    ent.ViewRemove(self, LGEMiscellaneous.DEFINECONSTANTS.false)

