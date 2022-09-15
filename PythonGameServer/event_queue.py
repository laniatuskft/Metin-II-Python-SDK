class TQueueElement:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.pvData = _boost_func_of_void.intrusive_ptr()
        self.iStartTime = 0
        self.iKey = 0
        self.bCancel = False


class CEventQueue:
    class FuncQueueComp:
## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: bool operator ()(TQueueElement * left, TQueueElement * right) const
        def functor_method(self, left, right):
            return (left.iKey > right.iKey)

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self._m_pq_queue = stable_priority_queue(Compare(), Container())


    def close(self):
        self.Destroy()

    def Enqueue(self, pvData, duration, pulse):
        pElem = LG_NEW_M2 TQueueElement

## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: pElem->pvData = pvData;
        pElem.pvData.copy_from(pvData)
        pElem.iStartTime = pulse
        pElem.iKey = duration + pulse
        pElem.bCancel = DefineConstants.false

        self._m_pq_queue.push(pElem)
        return pElem

    def Dequeue(self):
        if self._m_pq_queue.empty():
            return None

        pElem = self._m_pq_queue.top()
        self._m_pq_queue.pop()
        return pElem

    def Delete(self, pElem):
        LG_DEL_MEM(pElem)

# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    Requeue(UnnamedParameter, key)
    def GetTopKey(self):
        if self._m_pq_queue.empty():
            return numeric_limits.max()

        return self._m_pq_queue.top().iKey

    def Size(self):
        return Container.size_type(self._m_pq_queue.size())

    def Destroy(self):
        while not self._m_pq_queue.empty():
            pElem = self._m_pq_queue.top()
            self._m_pq_queue.pop()

            self.Delete(pElem)


