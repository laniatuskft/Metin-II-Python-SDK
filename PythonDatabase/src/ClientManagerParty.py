#Laniatus Games Studio Inc. | Python Metin II Server Warnings Statement interrupted by a preprocessor statement:
#The original statement from the file sal.h starts with:
#    __inner_fallthrough_dec
#Preprocessor-interrupted statements cannot be handled by this converter.
#The remainder of the header file sal.h is ignored.

def QUERY_PARTY_CREATE(peer, p):
    pm = m_map_pkChannelParty[peer.GetChannel()]

    if pm.find(p.dwLeaderPID) == pm.end():
        pm.insert(make_pair(p.dwLeaderPID, TPartyMember()))
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        ForwardPacket(LG_HEADER_DG_PARTY_CREATE, p, sizeof(TPacketPartyCreate), peer.GetChannel(), peer)
        sys_log(0, "PARTY Create [%lu]", p.dwLeaderPID)
    else:
        sys_err("PARTY Create - Already exists [%lu]", p.dwLeaderPID)

def QUERY_PARTY_DELETE(peer, p):
    pm = m_map_pkChannelParty[peer.GetChannel()]
    it = pm.find(p.dwLeaderPID)

    if it == pm.end():
        sys_err("PARTY Delete - Non exists [%lu]", p.dwLeaderPID)
        return

    pm.erase(it)
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    ForwardPacket(LG_HEADER_DG_PARTY_DELETE, p, sizeof(TPacketPartyDelete), peer.GetChannel(), peer)
    sys_log(0, "PARTY Delete [%lu]", p.dwLeaderPID)

def QUERY_PARTY_ADD(peer, p):
    pm = m_map_pkChannelParty[peer.GetChannel()]
    it = pm.find(p.dwLeaderPID)

    if it == pm.end():
        sys_err("PARTY Add - Non exists [%lu]", p.dwLeaderPID)
        return

    if it.second.find(p.dwPID) == it.second.end():
        it.second.insert((p.dwPID, TPartyInfo()))
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        ForwardPacket(LG_HEADER_DG_PARTY_ADD, p, sizeof(TPacketPartyAdd), peer.GetChannel(), peer)
        sys_log(0, "PARTY Add [%lu] to [%lu]", p.dwPID, p.dwLeaderPID)
    else:
        sys_err("PARTY Add - Already [%lu] in party [%lu]", p.dwPID, p.dwLeaderPID)

def QUERY_PARTY_REMOVE(peer, p):
    pm = m_map_pkChannelParty[peer.GetChannel()]
    it = pm.find(p.dwLeaderPID)

    if it == pm.end():
        sys_err("PARTY Remove - Non exists [%lu] cannot remove [%lu]",p.dwLeaderPID, p.dwPID)
        return

    pit = it.second.find(p.dwPID)

    if pit is not it.second.end():
        it.second.erase(pit)
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        ForwardPacket(LG_HEADER_DG_PARTY_REMOVE, p, sizeof(TPacketPartyRemove), peer.GetChannel(), peer)
        sys_log(0, "PARTY Remove [%lu] to [%lu]", p.dwPID, p.dwLeaderPID)
    else:
        sys_err("PARTY Remove - Cannot find [%lu] in party [%lu]", p.dwPID, p.dwLeaderPID)

def QUERY_PARTY_STATE_CHANGE(peer, p):
    pm = m_map_pkChannelParty[peer.GetChannel()]
    it = pm.find(p.dwLeaderPID)

    if it == pm.end():
        sys_err("PARTY StateChange - Non exists [%lu] cannot state change [%lu]",p.dwLeaderPID, p.dwPID)
        return

    pit = it.second.find(p.dwPID)

    if pit is it.second.end():
        sys_err("PARTY StateChange - Cannot find [%lu] in party [%lu]", p.dwPID, p.dwLeaderPID)
        return

    if p.bFlag:
        pit.second.bRole = p.bRole
    else:
        pit.second.bRole = 0

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    ForwardPacket(LG_HEADER_DG_PARTY_STATE_CHANGE, p, sizeof(TPacketPartyStateChange), peer.GetChannel(), peer)
    sys_log(0, "PARTY StateChange [%lu] at [%lu] from %d %d",p.dwPID, p.dwLeaderPID, p.bRole, p.bFlag)

def QUERY_PARTY_SET_MEMBER_LEVEL(peer, p):
    pm = m_map_pkChannelParty[peer.GetChannel()]
    it = pm.find(p.dwLeaderPID)

    if it == pm.end():
        sys_err("PARTY SetMemberLevel - Non exists [%lu] cannot level change [%lu]",p.dwLeaderPID, p.dwPID)
        return

    pit = it.second.find(p.dwPID)

    if pit is it.second.end():
        sys_err("PARTY SetMemberLevel - Cannot find [%lu] in party [%lu]", p.dwPID, p.dwLeaderPID)
        return

    pit.second.bLevel = p.bLevel

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    ForwardPacket(LG_HEADER_DG_PARTY_SET_MEMBER_LEVEL, p, sizeof(TPacketPartySetMemberLevel), peer.GetChannel())
    sys_log(0, "PARTY SetMemberLevel pid [%lu] level %d",p.dwPID, p.bLevel)
