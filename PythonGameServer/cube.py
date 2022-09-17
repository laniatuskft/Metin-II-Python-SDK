from enum import Enum

##define _cube_cpp_


class CUBE_VALUE:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.vnum = 0
        self.count = 0


    def equals_to(self, b):
        return (self.count == b.count) and (self.vnum == b.vnum)

class CUBE_DATA:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.npc_vnum = []
        self.item = []
        self.reward = []
        self.percent = 0
        self.gold = 0

        self.percent = 0
        self.gold = 0

    def can_make_item(self, items, npc_vnum):
        LaniatusDefVariables = None
        end_index = None
        need_vnum = None
        need_count = None
        found_npc = LGEMiscellaneous.DEFINECONSTANTS.false

        end_index = len(self.npc_vnum)
        for LaniatusDefVariables in range(0, end_index):
            if npc_vnum == self.npc_vnum[LaniatusDefVariables]:
                found_npc = 1 if ((not LGEMiscellaneous.DEFINECONSTANTS.false)) else 0
        if LGEMiscellaneous.DEFINECONSTANTS.false==found_npc:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        end_index = len(self.item)
        for LaniatusDefVariables in range(0, end_index):
            need_vnum = self.item[LaniatusDefVariables].vnum
            need_count = self.item[LaniatusDefVariables].count

            if LGEMiscellaneous.DEFINECONSTANTS.false==Globals.FN_check_item_count(items, need_vnum, need_count):
                return LGEMiscellaneous.DEFINECONSTANTS.false

        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def reward_value(self):
        end_index = 0
        reward_index = 0

        end_index = len(self.reward)
        reward_index = number(0, end_index)
        reward_index = number(0, end_index-1)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
#ORIGINAL METINII C CODE: return &this->reward[reward_index];
        return CUBE_VALUE(self.reward[reward_index])

    def remove_material(self, ch):
        LaniatusDefVariables = None
        end_index = None
        need_vnum = None
        need_count = None
        items = ch.GetCubeItem()

        end_index = len(self.item)
        for LaniatusDefVariables in range(0, end_index):
            need_vnum = self.item[LaniatusDefVariables].vnum
            need_count = self.item[LaniatusDefVariables].count

            Globals.FN_remove_material(items, need_vnum, need_count)

class ECubeResultCategory(Enum):
    CUBE_CATEGORY_POTION = 0
    CUBE_CATEGORY_WEAPON = 1
    CUBE_CATEGORY_ARMOR = 2
    CUBE_CATEGORY_ACCESSORY = 3
    CUBE_CATEGORY_ETC = 4


class SCubeMaterialInfo:
    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.reward = CUBE_VALUE()
        self.material = []
        self.gold = 0
        self.complicateMaterial = []
        self.infoText = ""
        self.bHaveComplicateMaterial = False

        self.bHaveComplicateMaterial = LGEMiscellaneous.DEFINECONSTANTS.false


class SItemNameAndLevel:
    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.name = ""
        self.level = 0

        self.level = 0


class CCubeMaterialInfoHelper: