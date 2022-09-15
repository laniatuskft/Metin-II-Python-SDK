class CItemDropInfo:
    def __init__(self, iLevelStart, iLevelEnd, iPercent, dwVnum):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.m_iLevelStart = 0
        self.m_iLevelEnd = 0
        self.m_iPercent = 0
        self.m_dwVnum = 0

        self.m_iLevelStart = iLevelStart
        self.m_iLevelEnd = iLevelEnd
        self.m_iPercent = iPercent
        self.m_dwVnum = dwVnum


## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python has no concept of a 'friend' function:
#ORIGINAL METINII C CODE: friend bool operator < (const CItemDropInfo & l, const CItemDropInfo & r)
    def less_than(self, l, r):
        return l.m_iLevelEnd < r.m_iLevelEnd

class SDropItem:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.iLvStart = 0
        self.iLvEnd = 0
        self.fPercent = 0
        self.szItemName = str(['\0' for _ in range(ITEM_NAME_MAX_LEN + 1)])
        self.iCount = 0


