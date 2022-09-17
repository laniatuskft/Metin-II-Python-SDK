def GetNewID():
    assert m_dwCurrentID != 0

    if m_dwCurrentID >= m_ItemIDRange.dwMax:
        if m_ItemIDSpareRange.dwMin == 0 or m_ItemIDSpareRange.dwMax == 0 or m_ItemIDSpareRange.dwUsableItemIDMin == 0:
            for LaniatusDefVariables in range(0, 10):
                #lani_err("ItemIDRange: FATAL ERROR!!! no more item id")
            touch(".killscript")
            thecore_shutdown()
            return 0
        else:
            #sys_log(0, "ItemIDRange: First Range is full. Change to SpareRange %u ~ %u %u", m_ItemIDSpareRange.dwMin, m_ItemIDSpareRange.dwMax, m_ItemIDSpareRange.dwUsableItemIDMin)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            db_clientdesc.DBPacket(LG_HEADER_GD_REQ_SPARE_ITEM_ID_RANGE, 0, m_ItemIDRange.dwMax, sizeof(uint))

            SetMaxItemID(m_ItemIDSpareRange)

            m_ItemIDSpareRange.dwMin = 0
            m_ItemIDSpareRange.dwMax = 0
            m_ItemIDSpareRange.dwUsableItemIDMin = 0

## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: return (m_dwCurrentID++);
    tempVar = uint((m_dwCurrentID))
    m_dwCurrentID += 1
    return tempVar

def SetMaxItemID(range):
    m_ItemIDRange = range

    if m_ItemIDRange.dwMin == 0 or m_ItemIDRange.dwMax == 0 or m_ItemIDRange.dwUsableItemIDMin == 0:
        for LaniatusDefVariables in range(0, 10):
            #lani_err("ItemIDRange: FATAL ERROR!!! ITEM ID RANGE is not set.")
        touch(".killscript")
        thecore_shutdown()
        return LGEMiscellaneous.DEFINECONSTANTS.false

    m_dwCurrentID = range.dwUsableItemIDMin

    #sys_log(0, "ItemIDRange: %u ~ %u %u", m_ItemIDRange.dwMin, m_ItemIDRange.dwMax, m_dwCurrentID)

    return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

def SetMaxSpareItemID(range):
    if range.dwMin == 0 or range.dwMax == 0 or range.dwUsableItemIDMin == 0:
        for LaniatusDefVariables in range(0, 10):
            #lani_err("ItemIDRange: FATAL ERROR!!! Spare ITEM ID RANGE is not set")
        return LGEMiscellaneous.DEFINECONSTANTS.false

    m_ItemIDSpareRange = range

    #sys_log(0, "ItemIDRange: New Spare ItemID Range Recv %u ~ %u %u", m_ItemIDSpareRange.dwMin, m_ItemIDSpareRange.dwMax, m_ItemIDSpareRange.dwUsableItemIDMin)

    return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

