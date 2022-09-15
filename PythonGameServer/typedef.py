from enum import Enum

## Laniatus Games Studio Inc. | NOTE: The following #define macro was replaced in-line:
#ORIGINAL METINII C CODE: #define itertype(v) decltype((v).begin())

## Laniatus Games Studio Inc. | NOTE: Python has no need of forward class declarations:
#class DESC

## Laniatus Games Studio Inc. | NOTE: Python has no need of forward class declarations:
#class CLIENT_DESC

## Laniatus Games Studio Inc. | NOTE: Python has no need of forward class declarations:
#class DESC_P2P

## Laniatus Games Studio Inc. | NOTE: Python has no need of forward class declarations:
#class CHARACTER

## Laniatus Games Studio Inc. | NOTE: Python has no need of forward class declarations:
#class CItem

class building: #this class replaces the original namespace 'building'
## Laniatus Games Studio Inc. | NOTE: Python has no need of forward class declarations:
#    class CObject


## Laniatus Games Studio Inc. | NOTE: Python has no need of forward class declarations:
#class CEntity

## Laniatus Games Studio Inc. | NOTE: Python has no need of forward class declarations:
#class SECTREE

## Laniatus Games Studio Inc. | NOTE: Python has no need of forward class declarations:
#class SECTREE_MAP

## Laniatus Games Studio Inc. | NOTE: Python has no need of forward class declarations:
#class CDungeon

## Laniatus Games Studio Inc. | NOTE: Python has no need of forward class declarations:
#class CParty

class pixel_position_s:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.x = 0
        self.y = 0
        self.z = 0


class EEntityTypes(Enum):
    ENTITY_CHARACTER = 0
    ENTITY_ITEM = 1
    ENTITY_OBJECT = 2

