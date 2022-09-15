class CFSM:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.m_pCurrentState = None
        self.m_pNewState = None
        self.m_stateInitial = CStateTemplate()

        self.m_stateInitial.Set(self, self.BeginStateInitial, self.StateInitial, self.EndStateInitial)
        self.m_pCurrentState = self.m_stateInitial
        self.m_pNewState = None

    def close(self):
        pass
    def Update(self):
        if self.m_pNewState:
            if None is not self.m_pCurrentState:
                self.m_pCurrentState.ExecuteEndState()

            self.m_pCurrentState = self.m_pNewState
            self.m_pNewState = None
            self.m_pCurrentState.ExecuteBeginState()

        self.m_pCurrentState.ExecuteState()

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: bool IsState(CState & State) const
    def IsState(self, State):
        return (m_pCurrentState is State)

    def GotoState(self, NewState):
        if self.IsState(NewState) and m_pNewState is NewState:
            return True

        self.m_pNewState = NewState
        return True

    def BeginStateInitial(self):
        pass
    def StateInitial(self):
        pass
    def EndStateInitial(self):
        pass
