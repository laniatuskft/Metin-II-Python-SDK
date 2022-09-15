from quest import *

import math

def GuildWarPacket(dwOppGID, bWarType, bWarState):
    pack = packet_guild()
    pack2 = packet_guild_war()

    pack.header = byte(LG_HEADER_GC_GUILD)
    pack.subheader = byte(GUILD_SUBLG_HEADER_GC_WAR)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    pack.size = sizeof(pack) + sizeof(pack2)
    pack2.dwGuildSelf = GetID()
    pack2.dwGuildOpp = dwOppGID
    pack2.bWarState = bWarState
    pack2.bType = bWarType

    it = m_memberOnline.begin()
    while it is not m_memberOnline.end():
        ch = *it

        if bWarState == EGuildWarState.GUILD_WAR_ON_WAR:
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> Guild Skills only affect players in war."))

        d = ch.GetDesc()

        if d:
            ch.SendGuildName(dwOppGID)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            d.BufferedPacket(pack, sizeof(pack))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            d.Packet(pack2, sizeof(pack2))
        it += 1

def SendEnemyGuild(ch):
    d = ch.GetDesc()

    if d is None:
        return

    pack = packet_guild()
    pack2 = packet_guild_war()
    pack.header = byte(LG_HEADER_GC_GUILD)
    pack.subheader = byte(GUILD_SUBLG_HEADER_GC_WAR)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    pack.size = sizeof(pack) + sizeof(pack2)
    pack2.dwGuildSelf = GetID()

    p = packet_guild()
    p.header = byte(LG_HEADER_GC_GUILD)
    p.subheader = byte(GUILD_SUBLG_HEADER_GC_WAR_SCORE)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    p.size = sizeof(p) + sizeof(uint) + sizeof(uint) + sizeof(int)

    it = m_EnemyGuild.begin()
    while it is not m_EnemyGuild.end():
        ch.SendGuildName(it.first)

        pack2.dwGuildOpp = it.first
        pack2.bType = it.second.type
        pack2.bWarState = it.second.state

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        d.BufferedPacket(pack, sizeof(pack))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        d.Packet(pack2, sizeof(pack2))

        if it.second.state == EGuildWarState.GUILD_WAR_ON_WAR:
            lScore = None

            lScore = GetWarScoreAgainstTo(pack2.dwGuildOpp)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            d.BufferedPacket(p, sizeof(p))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            d.BufferedPacket(pack2.dwGuildSelf, sizeof(uint))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            d.BufferedPacket(pack2.dwGuildOpp, sizeof(uint))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            d.Packet(lScore, sizeof(int))

            lScore = CGuildManager.instance().TouchGuild(pack2.dwGuildOpp).GetWarScoreAgainstTo(pack2.dwGuildSelf)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            d.BufferedPacket(p, sizeof(p))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            d.BufferedPacket(pack2.dwGuildOpp, sizeof(uint))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            d.BufferedPacket(pack2.dwGuildSelf, sizeof(uint))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            d.Packet(lScore, sizeof(int))
        it += 1

def GetGuildWarState(dwOppGID):
    if dwOppGID == GetID():
        return EGuildWarState.GUILD_WAR_NONE

    it = m_EnemyGuild.find(dwOppGID)
    return (it.second.state) if (it != m_EnemyGuild.end()) else EGuildWarState.GUILD_WAR_NONE

def GetGuildWarType(dwOppGID):
    git = m_EnemyGuild.find(dwOppGID)

    if git == m_EnemyGuild.end():
        return EGuildWarType.GUILD_WAR_TYPE_FIELD

    return git.second.type

def GetGuildWarMapIndex(dwOppGID):
    git = m_EnemyGuild.find(dwOppGID)

    if git == m_EnemyGuild.end():
        return 0

    return git.second.map_index

def CanStartWar(bGuildWarType):
    if bGuildWarType >= EGuildWarType.GUILD_WAR_TYPE_MAX_NUM:
        return LGEMiscellaneous.DEFINECONSTANTS.false

    if test_server or quest.CQuestManager.instance().GetEventFlag("guild_war_test") != 0:
        return GetLadderPoint() > 0

    return GetLadderPoint() > 0 and GetMemberCount() >= GUILD_WAR_MIN_MEMBER_COUNT

def UnderWar(dwOppGID):
    if dwOppGID == GetID():
        return LGEMiscellaneous.DEFINECONSTANTS.false

    it = m_EnemyGuild.find(dwOppGID)
    return (it != m_EnemyGuild.end()) and (it.second.IsWarBegin())

def UnderAnyWar(bType):
    it = m_EnemyGuild.begin()
    while it is not m_EnemyGuild.end():
        if bType < EGuildWarType.GUILD_WAR_TYPE_MAX_NUM:
            if it.second.type != bType:
                continue

        if it.second.IsWarBegin():
            return it.first
        it += 1

    return 0

def SetWarScoreAgainstTo(dwOppGID, iScore):
    dwSelfGID = GetID()

    #sys_log(0, "GuildWarScore Set %u from %u %d", dwSelfGID, dwOppGID, iScore)
    it = m_EnemyGuild.find(dwOppGID)

    if it != m_EnemyGuild.end():
        it.second.score = iScore

        if it.second.type != EGuildWarType.GUILD_WAR_TYPE_FIELD:
            gOpp = CGuildManager.instance().TouchGuild(dwOppGID)
            pMap = CWarMapManager.instance().Find(it.second.map_index)

            if pMap:
                pMap.UpdateScore(dwSelfGID, iScore, dwOppGID, gOpp.GetWarScoreAgainstTo(dwSelfGID))
        else:
            p = packet_guild()

            p.header = byte(LG_HEADER_GC_GUILD)
            p.subheader = byte(GUILD_SUBLG_HEADER_GC_WAR_SCORE)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            p.size = sizeof(p) + sizeof(uint) + sizeof(uint) + sizeof(int)

            buf = TEMP_BUFFER(8192, DefineConstants.false)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            buf.write(p, sizeof(p))

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            buf.write(dwSelfGID, sizeof(uint))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            buf.write(dwOppGID, sizeof(uint))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            buf.write(iScore, sizeof(int))

            Packet(buf.read_peek(), buf.size())

            gOpp = CGuildManager.instance().TouchGuild(dwOppGID)

            if gOpp:
                gOpp.Packet(buf.read_peek(), buf.size())

def GetWarScoreAgainstTo(dwOppGID):
    it = m_EnemyGuild.find(dwOppGID)

    if it != m_EnemyGuild.end():
        #sys_log(0, "GuildWarScore Get %u from %u %d", GetID(), dwOppGID, it.second.score)
        return it.second.score

    #sys_log(0, "GuildWarScore Get %u from %u No data", GetID(), dwOppGID)
    return 0

def GetWarStartTime(dwOppGID):
    if dwOppGID == GetID():
        return 0

    it = m_EnemyGuild.find(dwOppGID)

    if it == m_EnemyGuild.end():
        return 0

    return it.second.war_start_time

def NotifyGuildMaster(msg):
    ch = GetMasterCharacter()
    if ch:
        ch.ChatPacket(EChatType.CHAT_TYPE_INFO, msg)

def RequestDeclareWar(dwOppGID, type):
    if dwOppGID == GetID():
        #sys_log(0, "GuildWar.DeclareWar.DECLARE_WAR_SELF id(%d -> %d), type(%d)", GetID(), dwOppGID, type)
        return

    if type >= EGuildWarType.GUILD_WAR_TYPE_MAX_NUM:
        #sys_log(0, "GuildWar.DeclareWar.UNKNOWN_WAR_TYPE id(%d -> %d), type(%d)", GetID(), dwOppGID, type)
        return

    it = m_EnemyGuild.find(dwOppGID)
    if it == m_EnemyGuild.end():
        if not GuildWar_IsWarMap(type):
            #lani_err("GuildWar.DeclareWar.NOT_EXIST_MAP id(%d -> %d), type(%d), map(%d)", GetID(), dwOppGID, type, GuildWar_GetTypeMapIndex(type))

            map_allow_log()
            NotifyGuildMaster(LC_TEXT("The Guild Battle can't start because the server isn't online."))
            return

        p = SPacketGuildWar()
        p.bType = type
        p.bWar = EGuildWarState.GUILD_WAR_SEND_DECLARE
        p.dwGuildFrom = GetID()
        p.dwGuildTo = dwOppGID
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        db_clientdesc.DBPacket(LG_HEADER_GD_GUILD_WAR, 0, p, sizeof(p))
        #sys_log(0, "GuildWar.DeclareWar id(%d -> %d), type(%d)", GetID(), dwOppGID, type)
        return

    if it.second.state == EGuildWarState.GUILD_WAR_RECV_DECLARE:
            saved_type = it.second.type

            if saved_type == EGuildWarType.GUILD_WAR_TYPE_FIELD:
                p = SPacketGuildWar()
                p.bType = byte(saved_type)
                p.bWar = EGuildWarState.GUILD_WAR_ON_WAR
                p.dwGuildFrom = GetID()
                p.dwGuildTo = dwOppGID
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                db_clientdesc.DBPacket(LG_HEADER_GD_GUILD_WAR, 0, p, sizeof(p))
                #sys_log(0, "GuildWar.AcceptWar id(%d -> %d), type(%d)", GetID(), dwOppGID, saved_type)
                return

            if not GuildWar_IsWarMap(saved_type):
                #lani_err("GuildWar.AcceptWar.NOT_EXIST_MAP id(%d -> %d), type(%d), map(%d)", GetID(), dwOppGID, type, GuildWar_GetTypeMapIndex(type))

                map_allow_log()
                NotifyGuildMaster(LC_TEXT("The Guild Battle can't start because the server isn't online."))
                return

            guildWarInfo = GuildWar_GetTypeInfo(saved_type)

            p = SPacketGuildWar()
            p.bType = byte(saved_type)
            p.bWar = EGuildWarState.GUILD_WAR_WAIT_START
            p.dwGuildFrom = GetID()
            p.dwGuildTo = dwOppGID
            p.lWarPrice = guildWarInfo.iWarPrice
            p.lInitialScore = guildWarInfo.iInitialScore

            if test_server:
                p.lInitialScore = math.trunc(p.lInitialScore / float(10))

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            db_clientdesc.DBPacket(LG_HEADER_GD_GUILD_WAR, 0, p, sizeof(p))

            #sys_log(0, "GuildWar.WaitStartSendToDB id(%d vs %d), type(%d), bet(%lld), map_index(%d)", GetID(), dwOppGID, saved_type, guildWarInfo.iWarPrice, guildWarInfo.lMapIndex)

    elif it.second.state == EGuildWarState.GUILD_WAR_SEND_DECLARE:
            NotifyGuildMaster(LC_TEXT("You already declared war on this Guild."))
    else:
        #lani_err("GuildWar.DeclareWar.UNKNOWN_STATE[%d]: id(%d vs %d), type(%d), guild(%s:%u)", it.second.state, GetID(), dwOppGID, type, GetName(), GetID())

def DeclareWar(dwOppGID, type, state):
    if m_EnemyGuild.find(dwOppGID) != m_EnemyGuild.end():
        return LGEMiscellaneous.DEFINECONSTANTS.false

    gw = SGuildWar(type)
    gw.state = state

    m_EnemyGuild.insert((dwOppGID, gw))

    GuildWarPacket(dwOppGID, type, state)
    return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

def CheckStartWar(dwOppGID):
    it = m_EnemyGuild.find(dwOppGID)

    if it == m_EnemyGuild.end():
        return LGEMiscellaneous.DEFINECONSTANTS.false

    gw = SGuildWar(it.second)

    if gw.state == EGuildWarState.GUILD_WAR_ON_WAR:
        return LGEMiscellaneous.DEFINECONSTANTS.false

    return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

def StartWar(dwOppGID):
    it = m_EnemyGuild.find(dwOppGID)

    if it == m_EnemyGuild.end():
        return

    gw = SGuildWar(it.second)

    if gw.state == EGuildWarState.GUILD_WAR_ON_WAR:
        return

    gw.state = EGuildWarState.GUILD_WAR_ON_WAR
    gw.war_start_time = get_global_time()

    GuildWarPacket(dwOppGID, gw.type, EGuildWarState.GUILD_WAR_ON_WAR)

    if gw.type != EGuildWarType.GUILD_WAR_TYPE_FIELD:
        GuildWarEntryAsk(dwOppGID)

def WaitStartWar(dwOppGID):
    if dwOppGID == GetID():
        #sys_log(0,"GuildWar.WaitStartWar.DECLARE_WAR_SELF id(%u -> %u)", GetID(), dwOppGID)
        return LGEMiscellaneous.DEFINECONSTANTS.false

    it = m_EnemyGuild.find(dwOppGID)
    if it == m_EnemyGuild.end():
        #sys_log(0,"GuildWar.WaitStartWar.UNKNOWN_ENEMY id(%u -> %u)", GetID(), dwOppGID)
        return LGEMiscellaneous.DEFINECONSTANTS.false

    gw = SGuildWar(it.second)

    if gw.state == EGuildWarState.GUILD_WAR_WAIT_START:
        #sys_log(0,"GuildWar.WaitStartWar.UNKNOWN_STATE id(%u -> %u), state(%d)", GetID(), dwOppGID, gw.state)
        return LGEMiscellaneous.DEFINECONSTANTS.false

    gw.state = EGuildWarState.GUILD_WAR_WAIT_START

    g = CGuildManager.instance().FindGuild(dwOppGID)
    if g is None:
        #sys_log(0,"GuildWar.WaitStartWar.NOT_EXIST_GUILD id(%u -> %u)", GetID(), dwOppGID)
        return LGEMiscellaneous.DEFINECONSTANTS.false

    rkGuildWarInfo = GuildWar_GetTypeInfo(gw.type)

    if gw.type == EGuildWarType.GUILD_WAR_TYPE_FIELD:
        #sys_log(0,"GuildWar.WaitStartWar.FIELD_TYPE id(%u -> %u)", GetID(), dwOppGID)
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    #sys_log(0,"GuildWar.WaitStartWar.CheckWarServer id(%u -> %u), type(%d), map(%d)", GetID(), dwOppGID, gw.type, rkGuildWarInfo.lMapIndex)

    if not map_allow_find(rkGuildWarInfo.lMapIndex):
        #sys_log(0,"GuildWar.WaitStartWar.SKIP_WAR_MAP id(%u -> %u)", GetID(), dwOppGID)
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))


    id1 = GetID()
    id2 = dwOppGID

    if id1 > id2:
        std::swap(id1, id2)

    lMapIndex = uint(CWarMapManager.instance().CreateWarMap(rkGuildWarInfo, id1, id2))
    if lMapIndex == 0:
        #lani_err("GuildWar.WaitStartWar.CREATE_WARMAP_ERROR id(%u vs %u), type(%u), map(%d)", id1, id2, gw.type, rkGuildWarInfo.lMapIndex)
        CGuildManager.instance().RequestEndWar(GetID(), dwOppGID)
        return LGEMiscellaneous.DEFINECONSTANTS.false

    #sys_log(0, "GuildWar.WaitStartWar.CreateMap id(%u vs %u), type(%u), map(%d) -> map_inst(%u)", id1, id2, gw.type, rkGuildWarInfo.lMapIndex, lMapIndex)

    gw.map_index = lMapIndex
    SetGuildWarMapIndex(dwOppGID, lMapIndex)
    g.SetGuildWarMapIndex(GetID(), int(lMapIndex))

    p = SPacketGGGuildWarMapIndex()

    p.bHeader = byte(LG_HEADER_GG_GUILD_WAR_ZONE_MAP_INDEX)
    p.dwGuildID1 = id1
    p.dwGuildID2 = id2
    p.lMapIndex = int(lMapIndex)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    P2P_MANAGER.instance().Send(p, sizeof(p), NULL)

    return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

def RequestRefuseWar(dwOppGID):
    if dwOppGID == GetID():
        return

    it = m_EnemyGuild.find(dwOppGID)

    if it != m_EnemyGuild.end() and it.second.state == EGuildWarState.GUILD_WAR_RECV_DECLARE:
        p = SPacketGuildWar()
        p.bWar = EGuildWarState.GUILD_WAR_REFUSE
        p.dwGuildFrom = GetID()
        p.dwGuildTo = dwOppGID

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        db_clientdesc.DBPacket(LG_HEADER_GD_GUILD_WAR, 0, p, sizeof(p))

def RefuseWar(dwOppGID):
    if dwOppGID == GetID():
        return

    it = m_EnemyGuild.find(dwOppGID)

    if it != m_EnemyGuild.end() and (it.second.state == EGuildWarState.GUILD_WAR_SEND_DECLARE or it.second.state == EGuildWarState.GUILD_WAR_RECV_DECLARE):
        type = it.second.type
        m_EnemyGuild.erase(dwOppGID)

        GuildWarPacket(dwOppGID, type, EGuildWarState.GUILD_WAR_END)

def ReserveWar(dwOppGID, type):
    if dwOppGID == GetID():
        return

    it = m_EnemyGuild.find(dwOppGID)

    if it == m_EnemyGuild.end():
        gw = SGuildWar(type)
        gw.state = EGuildWarState.GUILD_WAR_RESERVE
        m_EnemyGuild.insert((dwOppGID, gw))
    else:
        it.second.state = EGuildWarState.GUILD_WAR_RESERVE

    #sys_log(0, "Guild::ReserveWar %u", dwOppGID)

def EndWar(dwOppGID):
    if dwOppGID == GetID():
        return

    it = m_EnemyGuild.find(dwOppGID)

    if it != m_EnemyGuild.end():
        pMap = CWarMapManager.instance().Find(it.second.map_index)

        if pMap:
            pMap.SetEnded()

        GuildWarPacket(dwOppGID, it.second.type, EGuildWarState.GUILD_WAR_END)
        m_EnemyGuild.erase(it)

        if not UnderAnyWar():
            it = m_memberOnline.begin()
            while it != m_memberOnline.end():
                ch = *it
                ch.RemoveAffect(LaniatusETalentXes.GUILD_LG_SKILL_BLOOD)
                ch.RemoveAffect(LaniatusETalentXes.GUILD_LG_SKILL_BLESS)
                ch.RemoveAffect(LaniatusETalentXes.GUILD_LG_SKILL_SEONGHWI)
                ch.RemoveAffect(LaniatusETalentXes.GUILD_LG_SKILL_ACCEL)
                ch.RemoveAffect(LaniatusETalentXes.GUILD_LG_SKILL_BUNNO)
                ch.RemoveAffect(LaniatusETalentXes.GUILD_LG_SKILL_JUMUN)

                ch.RemoveBadAffect()
                it += 1

def SetGuildWarMapIndex(dwOppGID, lMapIndex):
    it = m_EnemyGuild.find(dwOppGID)

    if it == m_EnemyGuild.end():
        return

    it.second.map_index = lMapIndex
    #sys_log(0, "GuildWar.SetGuildWarMapIndex id(%d -> %d), map(%d)", GetID(), dwOppGID, lMapIndex)

def GuildWarEntryAccept(dwOppGID, ch):
    git = m_EnemyGuild.find(dwOppGID)

    if git == m_EnemyGuild.end():
        return

    gw = SGuildWar(git.second)

    if gw.type == EGuildWarType.GUILD_WAR_TYPE_FIELD:
        return

    if gw.state != EGuildWarState.GUILD_WAR_ON_WAR:
        ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("The war is already over."))
        return

    if gw.map_index == 0:
        return

    pos = pixel_position_s()

    if not CWarMapManager.instance().GetStartPosition(int(gw.map_index), byte(0 if GetID() < dwOppGID else 1), pos):
        return

    pPC = quest.CQuestManager.instance().GetPC(ch.GetPlayerID())
    pPC.SetFlag("war.is_war_member", 1, DefineConstants.false)

    ch.SaveExitLocation()
    ch.WarpSet(pos.x, pos.y, int(gw.map_index))

def GuildWarEntryAsk(dwOppGID):
    git = m_EnemyGuild.find(dwOppGID)
    if git == m_EnemyGuild.end():
        #lani_err("GuildWar.GuildWarEntryAsk.UNKNOWN_ENEMY(%d)", dwOppGID)
        return

    gw = SGuildWar(git.second)

    #sys_log(0, "GuildWar.GuildWarEntryAsk id(%d vs %d), map(%d)", GetID(), dwOppGID, gw.map_index)
    if gw.map_index == 0:
        #lani_err("GuildWar.GuildWarEntryAsk.NOT_EXIST_MAP id(%d vs %d)", GetID(), dwOppGID)
        return

    pos = pixel_position_s()
    if not CWarMapManager.instance().GetStartPosition(int(gw.map_index), byte(0 if GetID() < dwOppGID else 1), pos):
        #lani_err("GuildWar.GuildWarEntryAsk.START_POSITION_ERROR id(%d vs %d), pos(%d, %d)", GetID(), dwOppGID, pos.x, pos.y)
        return

    #sys_log(0, "GuildWar.GuildWarEntryAsk.OnlineMemberCount(%d)", m_memberOnline.size())

    it = m_memberOnline.begin()

    while it is not m_memberOnline.end():
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: CHARACTER* ch = *it++;
        ch = *it
        it += 1

        questIndex = CQuestManager.instance().GetQuestIndexByName("guild_war_join")
        if questIndex != 0:
            #sys_log(0, "GuildWar.GuildWarEntryAsk.SendLetterToMember pid(%d), qid(%d)", ch.GetPlayerID(), questIndex)
            CQuestManager.instance().Letter(ch.GetPlayerID(), questIndex, 0)
        else:
            #lani_err("GuildWar.GuildWarEntryAsk.SendLetterToMember.QUEST_ERROR pid(%d), quest_name('guild_war_join.quest')", ch.GetPlayerID(), questIndex)
            break

def SetLadderPoint(point):
    if m_data.ladder_point != point:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if ! __MULTI_LANGUAGE_SYSTEM__
        buf = str(['\0' for _ in range(256)])
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        snprintf(buf, sizeof(buf), LC_TEXT("<Guild> Rank reached %d Points."), point)
        it = m_memberOnline.begin()
##endif
        while it is not m_memberOnline.end():
            ch = (*it)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if __MULTI_LANGUAGE_SYSTEM__
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> Rank reached %d Points."), point)
##else
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, buf)
##endif
            it += 1
    m_data.ladder_point = point

def ChangeLadderPoint(iChange):
    p = SPacketGuildLadderPoint()
    p.dwGuild = GetID()
    p.lChange = iChange
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    db_clientdesc.DBPacket(LG_HEADER_GD_GUILD_CHANGE_LADDER_POINT, 0, p, sizeof(p))
