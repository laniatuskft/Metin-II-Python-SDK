#Laniatus Games Studio Inc. | Python Metin II Server Warnings Statement interrupted by a preprocessor statement:
#The original statement from the file sal.h starts with:
#    __inner_fallthrough_dec
#Preprocessor-interrupted statements cannot be handled by this converter.
#The remainder of the header file sal.h is ignored.


def GuildCreate(peer, dwGuildID):
    sys_log(0, "GuildCreate %u", dwGuildID)
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    ForwardPacket(LG_HEADER_DG_GUILD_LOAD, dwGuildID, sizeof(uint))

    CGuildManager.instance().Load(dwGuildID)

def GuildChangeGrade(peer, p):
    sys_log(0, "GuildChangeGrade %u %u", p.dwGuild, p.dwInfo)
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    ForwardPacket(LG_HEADER_DG_GUILD_CHANGE_GRADE, p, sizeof(TPacketGuild))

def GuildAddMember(peer, p):
    CGuildManager.instance().TouchGuild(p.dwGuild)
    sys_log(0, "GuildAddMember %u %u", p.dwGuild, p.dwPID)

    szQuery = str(['\0' for _ in range(512)])

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    snprintf(szQuery, sizeof(szQuery), "INSERT INTO guild_member%s VALUES(%u, %u, %d, 0, 0)", GetTablePostfix(), p.dwPID, p.dwGuild, p.bGrade)

    pmsg_insert = std::unique_ptr(CDBManager.instance().DirectQuery(szQuery))

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    snprintf(szQuery, sizeof(szQuery), "SELECT pid, grade, is_general, offer, level, job, name FROM guild_member%s, player%s WHERE guild_id = %u and pid = id and pid = %u", GetTablePostfix(), GetTablePostfix(), p.dwGuild, p.dwPID)

    pmsg = std::unique_ptr(CDBManager.instance().DirectQuery(szQuery))

    if pmsg.Get().uiNumRows == 0:
        sys_err("Query failed when getting guild member data %s", pmsg.stQuery.c_str())
        return

    row = mysql_fetch_row(pmsg.Get().pSQLResult)

    if (not row[0]) or not row[1]:
        return

    dg = TPacketDGGuildMember()

    dg.dwGuild = p.dwGuild
    str_to_number(dg.dwPID, row[0])
    str_to_number(dg.bGrade, row[1])
    str_to_number(dg.isGeneral, row[2])
    str_to_number(dg.dwOffer, row[3])
    str_to_number(dg.bLevel, row[4])
    str_to_number(dg.bJob, row[5])
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    strlcpy(dg.szName, row[6], sizeof(dg.szName))

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    ForwardPacket(LG_HEADER_DG_GUILD_ADD_MEMBER, dg, sizeof(TPacketDGGuildMember))

def GuildRemoveMember(peer, p):
    sys_log(0, "GuildRemoveMember %u %u", p.dwGuild, p.dwInfo)

    szQuery = str(['\0' for _ in range(512)])
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    snprintf(szQuery, sizeof(szQuery), "DELETE FROM guild_member%s WHERE pid=%u and guild_id=%u", GetTablePostfix(), p.dwInfo, p.dwGuild)
    CDBManager.instance().AsyncQuery(szQuery)

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    snprintf(szQuery, sizeof(szQuery), "REPLACE INTO quest%s (dwPID, szName, szState, lValue) VALUES(%u, 'guild_manage', 'withdraw_time', %u)", GetTablePostfix(), p.dwInfo, GetCurrentTime())
    CDBManager.instance().AsyncQuery(szQuery)

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    ForwardPacket(LG_HEADER_DG_GUILD_REMOVE_MEMBER, p, sizeof(TPacketGuild))

def GuildSkillUpdate(peer, p):
    sys_log(0, "GuildSkillUpdate %d", p.amount)
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    ForwardPacket(LG_HEADER_DG_GUILD_LG_SKILL_UPDATE, p, sizeof(TPacketGuildSkillUpdate))

def GuildExpUpdate(peer, p):
    sys_log(0, "GuildExpUpdate %d", p.amount)
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    ForwardPacket(LG_HEADER_DG_GUILD_EXP_UPDATE, p, sizeof(TPacketGuildExpUpdate), 0, peer)

def GuildChangeMemberData(peer, p):
    sys_log(0, "GuildChangeMemberData %u %u %d %d", p.pid, p.offer, p.level, p.grade)
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    ForwardPacket(LG_HEADER_DG_GUILD_CHANGE_MEMBER_DATA, p, sizeof(TPacketGuildChangeMemberData), 0, peer)

def GuildDisband(peer, p):
    sys_log(0, "GuildDisband %u", p.dwGuild)

    szQuery = str(['\0' for _ in range(512)])

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    snprintf(szQuery, sizeof(szQuery), "DELETE FROM guild%s WHERE id=%u", GetTablePostfix(), p.dwGuild)
    CDBManager.instance().AsyncQuery(szQuery)

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    snprintf(szQuery, sizeof(szQuery), "DELETE FROM guild_grade%s WHERE guild_id=%u", GetTablePostfix(), p.dwGuild)
    CDBManager.instance().AsyncQuery(szQuery)

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    snprintf(szQuery, sizeof(szQuery), "REPLACE INTO quest%s (dwPID, szName, szState, lValue) SELECT pid, 'guild_manage', 'withdraw_time', %u FROM guild_member%s WHERE guild_id = %u", GetTablePostfix(), GetCurrentTime(), GetTablePostfix(), p.dwGuild)
    CDBManager.instance().AsyncQuery(szQuery)

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    snprintf(szQuery, sizeof(szQuery), "DELETE FROM guild_member%s WHERE guild_id=%u", GetTablePostfix(), p.dwGuild)
    CDBManager.instance().AsyncQuery(szQuery)

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    snprintf(szQuery, sizeof(szQuery), "DELETE FROM guild_comment%s WHERE guild_id=%u", GetTablePostfix(), p.dwGuild)
    CDBManager.instance().AsyncQuery(szQuery)

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    ForwardPacket(LG_HEADER_DG_GUILD_DISBAND, p, sizeof(TPacketGuild))

def GuildWar(peer, p):
    if p.bWar == GUILD_WAR_SEND_DECLARE:
        sys_log(0, "GuildWar: GUILD_WAR_SEND_DECLARE type(%s) guild(%d - %d)", __GetWarType(p.bType), p.dwGuildFrom, p.dwGuildTo)
        CGuildManager.instance().AddDeclare(p.bType, p.dwGuildFrom, p.dwGuildTo)

    elif p.bWar == GUILD_WAR_REFUSE:
        sys_log(0, "GuildWar: GUILD_WAR_REFUSE type(%s) guild(%d - %d)", __GetWarType(p.bType), p.dwGuildFrom, p.dwGuildTo)
        CGuildManager.instance().RemoveDeclare(p.dwGuildFrom, p.dwGuildTo)


    elif p.bWar == GUILD_WAR_WAIT_START:
        sys_log(0, "GuildWar: GUILD_WAR_WAIT_START type(%s) guild(%d - %d)", __GetWarType(p.bType), p.dwGuildFrom, p.dwGuildTo)
    elif (p.bWar == GUILD_WAR_WAIT_START) or (p.bWar == GUILD_WAR_RESERVE):
        if p.bWar != GUILD_WAR_WAIT_START:
            sys_log(0, "GuildWar: GUILD_WAR_RESERVE type(%s) guild(%d - %d)", __GetWarType(p.bType), p.dwGuildFrom, p.dwGuildTo)
        CGuildManager.instance().RemoveDeclare(p.dwGuildFrom, p.dwGuildTo)

        if not CGuildManager.instance().ReserveWar(p):
            p.bWar = GUILD_WAR_CANCEL
        else:
            p.bWar = GUILD_WAR_RESERVE


    elif p.bWar == GUILD_WAR_ON_WAR:
        sys_log(0, "GuildWar: GUILD_WAR_ON_WAR type(%s) guild(%d - %d)", __GetWarType(p.bType), p.dwGuildFrom, p.dwGuildTo)
        CGuildManager.instance().RemoveDeclare(p.dwGuildFrom, p.dwGuildTo)
        CGuildManager.instance().StartWar(p.bType, p.dwGuildFrom, p.dwGuildTo)

    elif p.bWar == GUILD_WAR_OVER:
        sys_log(0, "GuildWar: GUILD_WAR_OVER type(%s) guild(%d - %d)", __GetWarType(p.bType), p.dwGuildFrom, p.dwGuildTo)
        CGuildManager.instance().RecvWarOver(p.dwGuildFrom, p.dwGuildTo, p.bType, p.lWarPrice)

    elif p.bWar == GUILD_WAR_END:
        sys_log(0, "GuildWar: GUILD_WAR_END type(%s) guild(%d - %d)", __GetWarType(p.bType), p.dwGuildFrom, p.dwGuildTo)
        CGuildManager.instance().RecvWarEnd(p.dwGuildFrom, p.dwGuildTo)
        return

    elif (p.bWar == GUILD_WAR_END) or (p.bWar == GUILD_WAR_CANCEL):
        sys_log(0, "GuildWar: GUILD_WAR_CANCEL type(%s) guild(%d - %d)", __GetWarType(p.bType), p.dwGuildFrom, p.dwGuildTo)
        CGuildManager.instance().CancelWar(p.dwGuildFrom, p.dwGuildTo)

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    ForwardPacket(LG_HEADER_DG_GUILD_WAR, p, sizeof(TPacketGuildWar))

def GuildWarScore(peer, p):
    CGuildManager.instance().UpdateScore(p.dwGuildGainPoint, p.dwGuildOpponent, p.lScore, p.lBetScore)

def GuildChangeLadderPoint(p):
    sys_log(0, "GuildChangeLadderPoint Recv %u %d", p.dwGuild, p.lChange)
    CGuildManager.instance().ChangeLadderPoint(p.dwGuild, p.lChange)

def GuildUseSkill(p):
    sys_log(0, "GuildUseSkill Recv %u %d", p.dwGuild, p.dwSkillVnum)
    CGuildManager.instance().UseSkill(p.dwGuild, p.dwSkillVnum, p.dwCooltime)
    SendGuildSkillUsable(p.dwGuild, p.dwSkillVnum, DefineConstants.false)

def SendGuildSkillUsable(guild_id, dwSkillVnum, bUsable):
    sys_log(0, "SendGuildSkillUsable Send %u %d %s", guild_id, dwSkillVnum,"true" if bUsable " else "False")

    p = TPacketGuildSkillUsableChange()

    p.dwGuild = guild_id
    p.dwSkillVnum = dwSkillVnum
    p.bUsable = bUsable

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
    ForwardPacket(LG_HEADER_DG_GUILD_LG_SKILL_USABLE_CHANGE, p, sizeof(TPacketGuildSkillUsableChange))

def GuildChangeMaster(p):
    if CGuildManager.instance().ChangeMaster(p.dwGuildID, p.idFrom, p.idTo) == ((not DefineConstants.false)):
        packet = TPacketChangeGuildMaster()
        packet.dwGuildID = p.dwGuildID
        packet.idFrom = 0
        packet.idTo = 0

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        ForwardPacket(LG_HEADER_DG_ACK_CHANGE_GUILD_MASTER, packet, sizeof(packet))

