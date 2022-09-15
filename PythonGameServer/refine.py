class CRefineManager(singleton):
    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self._m_map_RefineRecipe = {}


    def close(self):
        pass

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Pointer arithmetic is detected on the parameter 'table':
#ORIGINAL METINII C CODE: bool Initialize(SRefineTable * table, int size)
    def Initialize(self, table, size):
        i = 0
        while i < size:
            #sys_log(0, "REFINE %d prob %d cost %d", table.id, table.prob, table.cost)
            self._m_map_RefineRecipe.update({table.id: *table})
            i += 1
            table += 1

        #sys_log(0, "REFINE: COUNT %d", len(self._m_map_RefineRecipe))
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def GetRefineRecipe(self, vnum):
        if vnum == 0:
            return None

        it = self._m_map_RefineRecipe.find(vnum)
        #sys_log(0, "REFINE: FIND %u %s", vnum,"FALSE" if it is self._m_map_RefineRecipe.end() is not None else "TRUE")

        if it is self._m_map_RefineRecipe.end():
            return None

        return it.second


