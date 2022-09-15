def SyncQuickslot(bType, bOldPos, bNewPos):
    if bOldPos == bNewPos:
        return

    i = 0
    while i < LGEMiscellaneous.LG_QUICKSLOT_MAX_NUM:
        if m_quickslot[i].type == bType and m_quickslot[i].pos == bOldPos:
            if bNewPos == 255:
                DelQuickslot(i)
            else:
                slot = SQuickslot()

                slot.type = bType
                slot.pos = bNewPos

                SetQuickslot(i, slot)
        i += 1

def GetQuickslot(pos, ppSlot):
    if pos >= LGEMiscellaneous.LG_QUICKSLOT_MAX_NUM:
        return LGEMiscellaneous.DEFINECONSTANTS.false

    ppSlot[0] = &m_quickslot[pos]
    return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

def SetQuickslot(pos, rSlot):
    pack_LG_QUICKSLOT_add = packet_LG_QUICKSLOT_add()

    if pos >= LGEMiscellaneous.LG_QUICKSLOT_MAX_NUM:
        return LGEMiscellaneous.DEFINECONSTANTS.false

    if rSlot.type >= LG_QUICKSLOT_TYPE_MAX_NUM:
        return LGEMiscellaneous.DEFINECONSTANTS.false

    i = 0
    while i < LGEMiscellaneous.LG_QUICKSLOT_MAX_NUM:
        if rSlot.type == 0:
            continue
        elif m_quickslot[i].type == rSlot.type and m_quickslot[i].pos == rSlot.pos:
            DelQuickslot(i)
        i += 1

    srcCell = TItemPos(EWindows.INVENTORY, rSlot.pos)

    if rSlot.type == LG_QUICKSLOT_TYPE_ITEM:
        if LGEMiscellaneous.DEFINECONSTANTS.false == srcCell.IsDefaultInventoryPosition() and LGEMiscellaneous.DEFINECONSTANTS.false == srcCell.IsBeltInventoryPosition():
            return LGEMiscellaneous.DEFINECONSTANTS.false


    elif rSlot.type == LG_QUICKSLOT_TYPE_SKILL:
        if int(rSlot.pos) >= LGEMiscellaneous.LG_SKILL_MAX_NUM:
            return LGEMiscellaneous.DEFINECONSTANTS.false


    elif rSlot.type == LG_QUICKSLOT_TYPE_COMMAND:
        pass

    else:
        return LGEMiscellaneous.DEFINECONSTANTS.false

    m_quickslot[pos] = rSlot

    if GetDesc():
        pack_LG_QUICKSLOT_add.header = byte(LG_HEADER_GC_LG_QUICKSLOT_ADD)
        pack_LG_QUICKSLOT_add.pos = pos
        pack_LG_QUICKSLOT_add.slot = m_quickslot[pos]

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        GetDesc().Packet(pack_LG_QUICKSLOT_add, sizeof(pack_LG_QUICKSLOT_add))

    return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

def DelQuickslot(pos):
    pack_LG_QUICKSLOT_del = packet_LG_QUICKSLOT_del()

    if pos >= LGEMiscellaneous.LG_QUICKSLOT_MAX_NUM:
        return LGEMiscellaneous.DEFINECONSTANTS.false

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    memset(m_quickslot[pos], 0, sizeof(SQuickslot))

    pack_LG_QUICKSLOT_del.header = byte(LG_HEADER_GC_LG_QUICKSLOT_DEL)
    pack_LG_QUICKSLOT_del.pos = pos

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    GetDesc().Packet(pack_LG_QUICKSLOT_del, sizeof(pack_LG_QUICKSLOT_del))
    return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

def SwapQuickslot(a, b):
    pack_LG_QUICKSLOT_swap = packet_LG_QUICKSLOT_swap()
    quickslot = SQuickslot()

    if a >= LGEMiscellaneous.LG_QUICKSLOT_MAX_NUM or b >= LGEMiscellaneous.LG_QUICKSLOT_MAX_NUM:
        return LGEMiscellaneous.DEFINECONSTANTS.false

    quickslot = m_quickslot[a]

    m_quickslot[a] = m_quickslot[b]
    m_quickslot[b] = quickslot

    pack_LG_QUICKSLOT_swap.header = byte(LG_HEADER_GC_LG_QUICKSLOT_SWAP)
    pack_LG_QUICKSLOT_swap.pos = a
    pack_LG_QUICKSLOT_swap.pos_to = b

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    GetDesc().Packet(pack_LG_QUICKSLOT_swap, sizeof(pack_LG_QUICKSLOT_swap))
    return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

def ChainQuickslotItem(pItem, bType, bOldPos):
    if pItem.IsDragonSoul():
        return
    i = 0
    while i < LGEMiscellaneous.LG_QUICKSLOT_MAX_NUM:
        if m_quickslot[i].type == bType and m_quickslot[i].pos == bOldPos:
            slot = SQuickslot()
            slot.type = bType
            slot.pos = byte(pItem.GetCell())

            SetQuickslot(i, slot)

            break
        i += 1

