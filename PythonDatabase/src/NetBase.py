#Laniatus Games Studio Inc. | Python Metin II Server Warnings Statement interrupted by a preprocessor statement:
#The original statement from the file sal.h starts with:
#    __inner_fallthrough_dec
#Preprocessor-interrupted statements cannot be handled by this converter.
#The remainder of the header file sal.h is ignored.

class CNetBase:
    def __init__(self):
        pass

    def close(self):
        pass

    m_fdWatcher = None

class CNetPoller(CNetBase, singleton):
    def __init__(self):
        pass

    def close(self):
        Destroy()

    def Create(self):
        sys_log(1, "NetPoller::Create()")

        if m_fdWatcher:
            return ((not DefineConstants.false))

        m_fdWatcher = fdwatch_new(512)

        if not m_fdWatcher:
            Destroy()
            return DefineConstants.false

        return ((not DefineConstants.false))

    def Destroy(self):
        sys_log(1, "NetPoller::Destroy()")

        if m_fdWatcher:
            fdwatch_delete(m_fdWatcher)
            m_fdWatcher = None

        thecore_destroy()


