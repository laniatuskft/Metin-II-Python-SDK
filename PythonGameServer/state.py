class CState:
    def close(self):
        pass

    def ExecuteBeginState(self):
        pass
    def ExecuteState(self):
        pass
    def ExecuteEndState(self):
        pass

class CStateTemplate(CState):
    class PFNSTATE:
        def invoke(self):
            pass



    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.m_pInstance = None
        self.m_pfnBeginState = PFNSTATE()
        self.m_pfnState = PFNSTATE()
        self.m_pfnEndState = PFNSTATE()

        self.m_pInstance = None
        self.m_pfnBeginState = PFNSTATE(0)
        self.m_pfnState = PFNSTATE(0)
        self.m_pfnEndState = PFNSTATE(0)

    def Set(self, pInstance, pfnBeginState, pfnState, pfnEndState):
        pInstance = assert()
        self.m_pInstance = pInstance

        pfnBeginState = assert()
        self.m_pfnBeginState = lambda : pfnBeginState.invoke()

        pfnState = assert()
        self.m_pfnState = lambda : pfnState.invoke()

        pfnEndState = assert()
        self.m_pfnEndState = lambda : pfnEndState.invoke()

    def ExecuteBeginState(self):
        assert self.m_pInstance and self.m_pfnBeginState
        self.m_pfnBeginState.invoke()

    def ExecuteState(self):
        assert self.m_pInstance and self.m_pfnState
        self.m_pfnState.invoke()

    def ExecuteEndState(self):
        assert self.m_pInstance and self.m_pfnEndState
        self.m_pfnEndState.invoke()
