# Laniatus Games Studio Inc. |  TODO TASK: Classes cannot inherit from generic type parameters in Python:
class CPoolNode(T):
    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.m_pNext = None
        self.m_pPrev = None

        self.m_pNext = None
        self.m_pPrev = None

    def close(self):
        pass


class CDynamicPool:

    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.m_nodes = None
        self.m_pFreeList = None
        self.m_pUsedList = None
        self.m_nodeCount = 0
        self.m_stName = ""

        self.Initialize()

    def close(self):
        m_pFreeList is None and "CDynamicPool::~CDynamicPool() - NOT Clear"
        m_pUsedList is None and "CDynamicPool::~CDynamicPool() - NOT Clear"
        self.Clear()

    def Initialize(self):
        self.m_nodes = None
        self.m_nodeCount = 0

        self.m_pFreeList = None
        self.m_pUsedList = None

    def SetName(self, c_szName):
        self.m_stName = c_szName

    def GetCapacity(self):
        return self.m_nodeCount

    def Alloc(self):
        pnewNode = None

        if self.m_pFreeList:
            pnewNode = self.m_pFreeList
            self.m_pFreeList = self.m_pFreeList.m_pNext
        else:
            pnewNode = self.AllocNode()

        if pnewNode is None:
            return None

        if self.m_pUsedList is None:
            self.m_pUsedList = pnewNode
            self.m_pUsedList.m_pPrev = self.m_pUsedList.m_pNext = None
        else:
# Laniatus Games Studio Inc. |  TODO TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'copy_from' method should be created:
#ORIGINAL LINE: m_pUsedList->m_pPrev = pnewNode;
            self.m_pUsedList.m_pPrev.copy_from(pnewNode)
# Laniatus Games Studio Inc. |  TODO TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'copy_from' method should be created:
#ORIGINAL LINE: pnewNode->m_pNext = m_pUsedList;
            pnewNode.m_pNext.copy_from(self.m_pUsedList)
            pnewNode.m_pPrev = None
            self.m_pUsedList = pnewNode
        return pnewNode

    def Free(self, pdata):
        pfreeNode = pdata

        if pfreeNode is self.m_pUsedList:
# Laniatus Games Studio Inc. |  TODO TASK: The following assignments within expression was not converted by Laniatus Games Studio Inc. T.F |:
#ORIGINAL LINE: if (NULL != (m_pUsedList = m_pUsedList->m_pNext))
            if None is not (self.m_pUsedList = self.m_pUsedList.m_pNext):
                self.m_pUsedList.m_pPrev = None
        else:
            if pfreeNode.m_pNext:
# Laniatus Games Studio Inc. |  TODO TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'copy_from' method should be created:
#ORIGINAL LINE: pfreeNode->m_pNext->m_pPrev = pfreeNode->m_pPrev;
                pfreeNode.m_pNext.m_pPrev.copy_from(pfreeNode.m_pPrev)

            if pfreeNode.m_pPrev:
# Laniatus Games Studio Inc. |  TODO TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'copy_from' method should be created:
#ORIGINAL LINE: pfreeNode->m_pPrev->m_pNext = pfreeNode->m_pNext;
                pfreeNode.m_pPrev.m_pNext.copy_from(pfreeNode.m_pNext)

        pfreeNode.m_pPrev = None
# Laniatus Games Studio Inc. |  TODO TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'copy_from' method should be created:
#ORIGINAL LINE: pfreeNode->m_pNext = m_pFreeList;
        pfreeNode.m_pNext.copy_from(self.m_pFreeList)
        self.m_pFreeList = pfreeNode

    def FreeAll(self):
        pcurNode = None
        pnextNode = None

        pcurNode = self.m_pUsedList

        while pcurNode:
            pnextNode = pcurNode.m_pNext
            self.Free(pcurNode)
            pcurNode = pnextNode

    def Clear(self):
        pcurNode = None
        pnextNode = None

        count = 0

        pcurNode = self.m_pFreeList
        while pcurNode:
            pnextNode = pcurNode.m_pNext
            if pcurNode is not None:
                pcurNode.close()
            pcurNode = pnextNode
            count += 1
        self.m_pFreeList = None

        pcurNode = self.m_pUsedList
        while pcurNode:
            pnextNode = pcurNode.m_pNext
            if pcurNode is not None:
                pcurNode.close()
            pcurNode = pnextNode
            count += 1

        self.m_pUsedList = None

        count == self.m_nodeCount and "CDynamicPool::Clear()"

        self.m_nodeCount = 0

    def AllocNode(self):
        self.m_nodeCount += 1
        return CPoolNode()


