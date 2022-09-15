class cache:
    def __init__(self):
        #instance fields found by Laniatus Games Studio Inc. T.F |:
        self.m_data = None
        self.m_bNeedQuery = False
        self.m_expireTime = time_t()
        self.m_lastUpdateTime = time_t()
        self.m_lastFlushTime = time_t()

        self.m_bNeedQuery = False
        self.m_expireTime = 600
        self.m_lastUpdateTime = 0
        self.m_lastFlushTime = time(0)

# Laniatus Games Studio Inc. |  TODO TASK: The memory management function 'memset' has no equivalent in Python:
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        memset(self.m_data, 0, sizeof(self.m_data))

    def Get(self, bUpdateTime = True):
        if bUpdateTime:
            self.m_lastUpdateTime = time(0)

        return self.m_data

    def Put(self, pNew, bSkipQuery = False):
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        thecore_memcpy(self.m_data, pNew, sizeof(T))
        self.m_lastUpdateTime = time(0)

        if not bSkipQuery:
            self.m_bNeedQuery = True

    def CheckFlushTimeout(self):
        if self.m_bNeedQuery and time(0) - self.m_lastFlushTime > self.m_expireTime:
            return True

        return False

    def CheckTimeout(self):
        if time(0) - self.m_lastUpdateTime > self.m_expireTime:
            return True

        return False

    def Flush(self):
        if not self.m_bNeedQuery:
            return

        self.OnFlush()
        self.m_bNeedQuery = False
        self.m_lastFlushTime = time(0)

    def OnFlush(self):
        pass


