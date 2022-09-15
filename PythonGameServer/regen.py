from enum import Enum
import math

class regen:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.prev = None
        self.next = None
        self.lMapIndex = 0
        self.type = 0
        self.sx = 0
        self.sy = 0
        self.ex = 0
        self.ey = 0
        self.z_section = 0
        self.direction = 0
        self.time = 0
        self.max_count = 0
        self.count = 0
        self.vnum = 0
        self.is_aggressive = False
        self.event = _boost_func_of_void.intrusive_ptr()
        self.id = size_t()

        self.prev = None
        self.next = None
        self.lMapIndex = 0
        self.type = 0
        self.sx = 0
        self.sy = 0
        self.ex = 0
        self.ey = 0
        self.z_section = 0
        self.direction = 0
        self.time = 0
        self.max_count = 0
        self.count = 0
        self.vnum = 0
        self.is_aggressive = False
        self.event = None
        self.id = 0

class regen_event_info(event_info_data):

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.regen = None

        self.regen = None


class regen_exception:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.prev = None
        self.next = None
        self.sx = 0
        self.sy = 0
        self.ex = 0
        self.ey = 0
        self.z_section = 0



## Laniatus Games Studio Inc. | NOTE: Python has no need of forward class declarations:
#class CDungeon

class dungeon_regen_event_info(event_info_data):

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.regen = None
        self.dungeon_id = uint32_t()

        self.regen = None
        self.dungeon_id = 0

class ERegenModes(Enum):
    MODE_TYPE = 0
    MODE_SX = 1
    MODE_SY = 2
    MODE_EX = 3
    MODE_EY = 4
    MODE_Z_SECTION = 5
    MODE_DIRECTION = 6
    MODE_REGEN_TIME = 7
    MODE_REGEN_PERCENT = 8
    MODE_MAX_COUNT = 9
    MODE_VNUM = 10