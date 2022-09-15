class CMapLocation(singleton):

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.m_map_address = {}

    class SLocation:

        def __init__(self):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.addr = 0
            self.port = 0


    def Get(self, x, y, lIndex, lAddr, wPort):
        lIndex.arg_value = SECTREE_MANAGER.instance().GetMapIndex(x, y)

        return self.Get(lIndex.arg_value, lAddr, wPort)

    def Get(self, iIndex, lAddr, wPort):
        if iIndex == 0:
            #sys_log(0, "CMapLocation::Get - Error MapIndex[%d]", iIndex)
            return DefineConstants.false

        it = self.m_map_address.find(iIndex)

        if self.m_map_address.end() is it:
            #sys_log(0, "CMapLocation::Get - Error MapIndex[%d]", iIndex)
            i = m_map_address.begin()
            while i is not self.m_map_address.end():
                #sys_log(0, "Map(%d): Server(%x:%d)", i.first, i.second.addr, i.second.port)
                i += 1
            return DefineConstants.false

        lAddr.arg_value = it.second.addr
        wPort.arg_value = it.second.port
        return ((not DefineConstants.false))

    def Insert(self, lIndex, c_pszHost, wPort):
        loc = TLocation()

        loc.addr = inet_addr(c_pszHost)
        loc.port = wPort

        self.m_map_address.update({lIndex: loc})
        #sys_log(0, "MapLocation::Insert : %d %s %d", lIndex, c_pszHost, wPort)
