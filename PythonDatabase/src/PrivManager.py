#Laniatus Games Studio Inc. | Python Metin II Server Warnings Statement interrupted by a preprocessor statement:
#The original statement from the file sal.h starts with:
#    __inner_fallthrough_dec
#Preprocessor-interrupted statements cannot be handled by this converter.
#The remainder of the header file sal.h is ignored.

class TPrivEmpireData:


    def __init__(self, type, value, empire, end_time_sec):
        self.type = type
        self.value = value
        self.bRemoved = DefineConstants.false
        self.empire = empire
        self.end_time_sec = end_time_sec

class TPrivGuildData:


    def __init__(self, type, value, guild_id, _end_time_sec):
        self.type = type
        self.value = value
        self.bRemoved = DefineConstants.false
        self.guild_id = guild_id
        self.end_time_sec = _end_time_sec

class TPrivCharData:
    def __init__(self, type, value, pid):
        self.type = type
        self.value = value
        self.bRemoved = DefineConstants.false
        self.pid = pid

class CPrivManager(singleton):
    def __init__(self):
        type = 0
        while type < MAX_PRIV_NUM:
            empire = 0
            while empire < EMPIRE_MAX_NUM:
                m_aaPrivEmpire[type][empire] = 0
                empire += 1
            type += 1

    def close(self):
        pass

    def AddGuildPriv(self, guild_id, type, value, duration_sec):
        if MAX_PRIV_NUM <= type:
            sys_err("PRIV_MANAGER: AddGuildPriv: wrong guild priv type(%u) recved", type)
            return

        it = m_aPrivGuild[type].find(guild_id)

        now = CClientManager.instance().GetCurrentTime()
        end = now + duration_sec
        p = TPrivGuildData(type, value, guild_id, end)
        m_pqPrivGuild.push((end, p))

        if it != m_aPrivGuild[type].end():
            it.second = p
        else:
            m_aPrivGuild[type].insert((guild_id, p))

        SendChangeGuildPriv(guild_id, type, value, end)

        sys_log(0, "Guild Priv guild(%d) type(%d) value(%d) duration_sec(%d)", guild_id, type, value, duration_sec)

    def AddEmpirePriv(self, empire, type, value, duration_sec):
        if MAX_PRIV_NUM <= type:
            sys_err("PRIV_MANAGER: AddEmpirePriv: wrong empire priv type(%u) recved", type)
            return

        if duration_sec < 0:
            duration_sec = 0

        now = CClientManager.instance().GetCurrentTime()
        end = now+duration_sec

            if m_aaPrivEmpire[type][empire]:
                m_aaPrivEmpire[type][empire].bRemoved = ((not DefineConstants.false))

        p = TPrivEmpireData(type, value, empire, end)
        m_pqPrivEmpire.push((end, p))
        m_aaPrivEmpire[type][empire] = p

        SendChangeEmpirePriv(empire, type, value, end)

        sys_log(0, "Empire Priv empire(%d) type(%d) value(%d) duration_sec(%d)", empire, type, value, duration_sec)

    def AddCharPriv(self, pid, type, value):
        if MAX_PRIV_NUM <= type:
            sys_err("PRIV_MANAGER: AddCharPriv: wrong char priv type(%u) recved", type)
            return

        it = m_aPrivChar[type].find(pid)

        if it != m_aPrivChar[type].end():
            return

        if value == 0:
            return

        now = CClientManager.instance().GetCurrentTime()
        p = TPrivCharData(type, value, pid)

        iDuration = CHARACTER_BAD_PRIV_DURATION

        if value > 0:
            iDuration = CHARACTER_GOOD_PRIV_DURATION

        m_pqPrivChar.push((now+iDuration, p))
        m_aPrivChar[type].insert((pid, p))

        sys_log(0, "AddCharPriv %d %d %d", pid, type, value)
        SendChangeCharPriv(pid, type, value)

    def Update(self):
        now = CClientManager.instance().GetCurrentTime()

        while (not m_pqPrivGuild.empty()) and m_pqPrivGuild.top().first <= now:
            p = m_pqPrivGuild.top().second
            m_pqPrivGuild.pop()

            if p.value != 0 and not p.bRemoved:

                it = m_aPrivGuild[p.type].find(p.guild_id)

                if it is not m_aPrivGuild[p.type].end() and it.second is p:
                    m_aPrivGuild[p.type].erase(it)
                    SendChangeGuildPriv(p.guild_id, p.type, 0, 0)

            p = None

        while (not m_pqPrivEmpire.empty()) and m_pqPrivEmpire.top().first <= now:
            p = (m_pqPrivEmpire.top().second)
            m_pqPrivEmpire.pop()

            if p.value != 0 and not p.bRemoved:
                SendChangeEmpirePriv(p.empire, p.type, 0, 0)
                m_aaPrivEmpire[p.type][p.empire] = 0

            p = None

        while (not m_pqPrivChar.empty()) and m_pqPrivChar.top().first <= now:
            p = (m_pqPrivChar.top().second)
            m_pqPrivChar.pop()

            if not p.bRemoved:
                SendChangeCharPriv(p.pid, p.type, 0)
                it = m_aPrivChar[p.type].find(p.pid)
                if it is not m_aPrivChar[p.type].end():
                    m_aPrivChar[p.type].erase(it)
            p = None

    def SendPrivOnSetup(self, peer):
        LaniatusDefVariables = 1
        while LaniatusDefVariables < MAX_PRIV_NUM:
            e = 0
            while e < EMPIRE_MAX_NUM:
                pPrivEmpireData = m_aaPrivEmpire[LaniatusDefVariables][e]
                if pPrivEmpireData:
                    FSendChangeEmpirePriv(e, i, pPrivEmpireData.value, pPrivEmpireData.end_time_sec)(peer)
                e += 1

            it = m_aPrivGuild[LaniatusDefVariables].begin()
            while it is not m_aPrivGuild[LaniatusDefVariables].end():
                FSendChangeGuildPriv(it.first, i, it.second.value, it.second.end_time_sec)(peer)
                it += 1
            it = m_aPrivChar[LaniatusDefVariables].begin()
            while it is not m_aPrivChar[LaniatusDefVariables].end():
                FSendChangeCharPriv(it.first, i, it.second.value)(peer)
                it += 1
            LaniatusDefVariables += 1

    def SendChangeGuildPriv(self, guild_id, type, value, end_time_sec):
        CClientManager.instance().for_each_peer(FSendChangeGuildPriv(guild_id, type, value, end_time_sec))

    def SendChangeEmpirePriv(self, empire, type, value, end_time_sec):
        CClientManager.instance().for_each_peer(FSendChangeEmpirePriv(empire, type, value, end_time_sec))

    def SendChangeCharPriv(self, pid, type, value):
        CClientManager.instance().for_each_peer(FSendChangeCharPriv(pid, type, value))




class FSendChangeGuildPriv:
    def __init__(self, guild_id, type, value, end_time_sec):
        p.guild_id = guild_id
        p.type = type
        p.value = value
        p.bLog = 1
        p.end_time_sec = end_time_sec

    def functor_method(self, peer):
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        peer.EncodeHeader(LG_HEADER_DG_CHANGE_GUILD_PRIV, 0, sizeof(TPacketDGChangeGuildPriv))
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        peer.Encode(p, sizeof(TPacketDGChangeGuildPriv))
        p.bLog = 0


class FSendChangeEmpirePriv:
    def __init__(self, empire, type, value, end_time_sec):
        p.empire = empire
        p.type = type
        p.value = value
        p.bLog = 1
        p.end_time_sec = end_time_sec

    def functor_method(self, peer):
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        peer.EncodeHeader(LG_HEADER_DG_CHANGE_EMPIRE_PRIV, 0, sizeof(TPacketDGChangeEmpirePriv))
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        peer.Encode(p, sizeof(TPacketDGChangeEmpirePriv))
        p.bLog = 0


class FSendChangeCharPriv:
    def __init__(self, pid, type, value):
        p.pid = pid
        p.type = type
        p.value = value
        p.bLog = 1
    def functor_method(self, peer):
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        peer.EncodeHeader(LG_HEADER_DG_CHANGE_CHARACTER_PRIV, 0, sizeof(TPacketDGChangeCharacterPriv))
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        peer.Encode(p, sizeof(TPacketDGChangeCharacterPriv))
        p.bLog = 0
