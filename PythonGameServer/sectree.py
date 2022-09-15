from enum import Enum
import math

class ESectree(Enum):
    SECTREE_SIZE = 6400
    SECTREE_HALF_SIZE = 3200
    CELL_SIZE = 50

class sectree_coord:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not allow bit fields:
    uint x : 16
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not allow bit fields:
    uint y : 16

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Unions are not supported in Python:
#union sectreeid

class FCollectEntity:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.result = []

    def functor_method(self, entity):

        self.result.append(entity)
    def ForEach(self, f):
        it = self.result.begin()
        while it is not self.result.end():
            entity = *it
            f(entity)
            it += 1

## Laniatus Games Studio Inc. | NOTE: Python has no need of forward class declarations:
#class CAttribute

class SECTREE:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python has no concept of a 'friend' class:
#    friend class SECTREE_MANAGER
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python has no concept of a 'friend' class:
#    friend class SECTREE_MAP

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: CEntity* find_if(_Func & func) const
    def find_if(self, func):
        it_tree = self._m_neighbor_list.begin()

        while it_tree is not self._m_neighbor_list.end():
            it_entity = it_tree.m_set_entity.begin()

            while it_entity is not it_tree.m_set_entity.end():
                if func(*it_entity):
                    return (*it_entity)

                it_entity += 1

            it_tree += 1

        return None

    def ForEachAround(self, func):
        collector = FCollectEntity()
        it = self._m_neighbor_list.begin()
        while it is not self._m_neighbor_list.end():
            sectree = *it
            sectree._for_each_entity(collector.functor_method)
            it += 1
        collector.ForEach(func)

    def for_each_for_find_victim(self, func):
        it_tree = self._m_neighbor_list.begin()

        while it_tree is not self._m_neighbor_list.end():
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: if ((*(it_tree++))->for_each_entity_for_find_victim(func))
            if (*(it_tree)).for_each_entity_for_find_victim(func):
                it_tree += 1
                return
            else:
                it_tree += 1
    def for_each_entity_for_find_victim(self, func):
        it = self._m_set_entity.begin()

        while it is not self._m_set_entity.end():
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: if (func(*it++))
            if func(*it):
                it += 1
                return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
            else:
                it += 1
        return LGEMiscellaneous.DEFINECONSTANTS.false


    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self._m_id = SECTREEID()
        self._m_set_entity = boost.unordered_set()
        self._m_neighbor_list = std::list()
        self._m_iPCCount = 0
        self._isClone = False
        self._m_pkAttribute = None

        self.Initialize()

    def close(self):
        self.Destroy()

    def Initialize(self):
        self._m_id.package = 0
        self._m_pkAttribute = None
        self._m_iPCCount = 0
        self._isClone = LGEMiscellaneous.DEFINECONSTANTS.false

    def Destroy(self):
        if not self._m_set_entity.empty():
            #lani_err("Sectree: entity set not empty!!")

            it = self._m_set_entity.begin()

            while it is not self._m_set_entity.end():
                ent = *it

                if ent.IsType(EEntityTypes.ENTITY_CHARACTER):
                    ch = ent

                    #lani_err("Sectree: destroying character: %s is_pc %d", ch.GetName(LOCALE_LANIATUS),1 if ch.IsPC() else 0)

                    if ch.GetDesc():
                        DESC_MANAGER.instance().DestroyDesc(ch.GetDesc(), ((not DefineConstants.false)))
                    else:
                        CHARACTER_MANAGER.instance().DestroyCharacter(ch)
                elif ent.IsType(EEntityTypes.ENTITY_ITEM):
                    item = ent

                    #lani_err("Sectree: destroying Item: %s", item.GetName(LOCALE_LANIATUS))

                    ITEM_MANAGER.instance().DestroyItem(item)
                else:
                    #lani_err("Sectree: unknown type: %d", ent.GetType())
                it += 1
        self._m_set_entity.clear()

        if (not self._isClone) and self._m_pkAttribute:
            LG_DEL_MEM(self._m_pkAttribute)
            self._m_pkAttribute = None

    def GetID(self):
        return SECTREEID(self._m_id)

    def InsertEntity(self, pkEnt):
        pkCurTree = None

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((pkCurTree = pkEnt->GetSectree()) == this)
        if (pkCurTree = pkEnt.GetSectree()) is self:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if self._m_set_entity.find(pkEnt) != self._m_set_entity.end():
            #lani_err("entity %p already exist in this sectree!", Globals.get_pointer(pkEnt))
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if pkCurTree:
            pkCurTree._m_set_entity.erase(pkEnt)

        pkEnt.SetSectree(self)
        pkEnt.UpdateSectree()

        self._m_set_entity.insert(pkEnt)

        if pkEnt.IsType(EEntityTypes.ENTITY_CHARACTER):
            pkChr = pkEnt

            if pkChr.IsPC():
                self.IncreasePC()

                if pkCurTree:
                    pkCurTree.DecreasePC()
            elif self._m_iPCCount > 0 and (not pkChr.IsWarp()) and not pkChr.IsGoto():
                pkChr.StartStateMachine(1)

        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def RemoveEntity(self, pkEnt):
        it = self._m_set_entity.find(pkEnt)

        if it == self._m_set_entity.end():
            return
        self._m_set_entity.erase(it)

        pkEnt.SetSectree(None)

        if pkEnt.IsType(EEntityTypes.ENTITY_CHARACTER):
            if (pkEnt).IsPC():
                self.DecreasePC()

    def IncreasePC(self):
        it_tree = self._m_neighbor_list.begin()

        while it_tree is not self._m_neighbor_list.end():
            ++it_tree.m_iPCCount
            it_tree += 1

    def DecreasePC(self):
        it_tree = self._m_neighbor_list.begin()

        while it_tree is not self._m_neighbor_list.end():
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Pointer arithmetic is detected on this variable:
#ORIGINAL METINII C CODE: SECTREE* tree = *it_tree++;
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
            tree = *it_tree
            it_tree += 1

            tree._m_iPCCount -= 1
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: if (--tree->m_iPCCount <= 0)
            if tree._m_iPCCount <= 0:
                if tree._m_iPCCount < 0:
                    #lani_err("tree pc count lower than zero (value %d coord %d %d)", tree._m_iPCCount, tree._m_id.coord.x, tree._m_id.coord.y)
                    tree._m_iPCCount = 0

                it_entity = tree._m_set_entity.begin()

                while it_entity is not tree._m_set_entity.end():
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: CEntity* pkEnt = *(it_entity++);
                    pkEnt = *(it_entity)
                    it_entity += 1

                    if pkEnt.IsType(EEntityTypes.ENTITY_CHARACTER):
                        ch = pkEnt
                        ch.StopStateMachine()

    def BindAttribute(self, pkAttribute):
        self._m_pkAttribute = pkAttribute

    def GetAttributePtr(self):
        return self._m_pkAttribute
    def GetAttribute(self, x, y):
        assert self._m_pkAttribute is not None
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        return self._m_pkAttribute.Get((math.fmod(x, ESectree.SECTREE_SIZE)) / ESectree.CELL_SIZE, (math.fmod(y, ESectree.SECTREE_SIZE)) / ESectree.CELL_SIZE)

    def IsAttr(self, x, y, dwFlag):
        ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'IS_SET' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
        if IS_SET(self.GetAttribute(x, y), dwFlag):
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        return LGEMiscellaneous.DEFINECONSTANTS.false

    def CloneAttribute(self, tree):
        self._m_pkAttribute = tree._m_pkAttribute
        self._isClone = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def GetEventAttribute(self, x, y):
        return self.GetAttribute(x, y) >> 8

    def SetAttribute(self, x, y, dwAttr):
        assert self._m_pkAttribute is not None
        self._m_pkAttribute.Set(x, y, dwAttr)

    def RemoveAttribute(self, x, y, dwAttr):
        assert self._m_pkAttribute is not None
        self._m_pkAttribute.Remove(x, y, dwAttr)

    def _for_each_entity(self, func):
        it = self._m_set_entity.begin()
        while it is not self._m_set_entity.end():
            entity = *it

            if entity.GetSectree() is not self:
                #lani_err("<Factor> SECTREE-ENTITY relationship mismatch")
                self._m_set_entity.erase(it)
                continue
            func(entity)
            it += 1


