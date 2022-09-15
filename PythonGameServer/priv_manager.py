class CPrivManager(singleton):
    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self._m_aakPrivEmpireData = [[] for _ in range((int)EPrivType.MAX_PRIV_NUM)]
        self._m_aPrivGuild = [{} for _ in range((int)EPrivType.MAX_PRIV_NUM)]
        self._m_aPrivChar = [{} for _ in range((int)EPrivType.MAX_PRIV_NUM)]

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memset(self._m_aakPrivEmpireData, 0, sizeof(self._m_aakPrivEmpireData))

    def RequestGiveGuildPriv(self, guild_id, type, value, duration_sec):
        if EPrivType.MAX_PRIV_NUM <= type:
            #lani_err("PRIV_MANAGER: RequestGiveGuildPriv: wrong guild priv type(%u)", type)
            return

        value = MINMAX(0, value, 50)
        duration_sec = MINMAX(0, duration_sec, 60 *60 *24 *7)

        p = SPacketGiveGuildPriv()
        p.type = type
        p.value = value
        p.guild_id = guild_id
## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: p.duration_sec = duration_sec;
        p.duration_sec.copy_from(duration_sec)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        db_clientdesc.DBPacket(Globals.LG_HEADER_GD_REQUEST_GUILD_PRIV, 0, p, sizeof(p))

    def RequestGiveEmpirePriv(self, empire, type, value, duration_sec):
        if EPrivType.MAX_PRIV_NUM <= type:
            #lani_err("PRIV_MANAGER: RequestGiveEmpirePriv: wrong empire priv type(%u)", type)
            return

        value = MINMAX(0, value, 200)
        duration_sec = MINMAX(0, duration_sec, 60 *60 *24 *7)

        p = SPacketGiveEmpirePriv()
        p.type = type
        p.value = value
        p.empire = empire
## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: p.duration_sec = duration_sec;
        p.duration_sec.copy_from(duration_sec)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        db_clientdesc.DBPacket(Globals.LG_HEADER_GD_REQUEST_EMPIRE_PRIV, 0, p, sizeof(p))

    def RequestGiveCharacterPriv(self, pid, type, value):
        if EPrivType.MAX_PRIV_NUM <= type:
            #lani_err("PRIV_MANAGER: RequestGiveCharacterPriv: wrong char priv type(%u)", type)
            return

        value = MINMAX(0, value, 100)

        p = SPacketGiveCharacterPriv()
        p.type = type
        p.value = value
        p.pid = pid

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        db_clientdesc.DBPacket(Globals.LG_HEADER_GD_REQUEST_CHARACTER_PRIV, 0, p, sizeof(p))

    def GiveGuildPriv(self, guild_id, type, value, bLog, end_time_sec):
        if EPrivType.MAX_PRIV_NUM <= type:
            #lani_err("PRIV_MANAGER: GiveGuildPriv: wrong guild priv type(%u)", type)
            return

        #sys_log(0,"Set Guild Priv: guild_id(%u) type(%d) value(%d) duration_sec(%d)", guild_id, type, value, end_time_sec - get_global_time())

        value = MINMAX(0, value, 50)
        end_time_sec = MINMAX(0, end_time_sec, get_global_time()+60 *60 *24 *7)

        self._m_aPrivGuild[type][guild_id].value = value
        self._m_aPrivGuild[type][guild_id].end_time_sec = end_time_sec

        g = CGuildManager.instance().FindGuild(guild_id)

        if g:
            if value != 0:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if __MULTI_LANGUAGE_SYSTEM__
                SendGuildPrivNotice(LC_TEXT("%s of the Guild %s raised up to %d%% !"), g.GetName(), Globals.GetPrivName(type), value)
##else
                buf = str(['\0' for _ in range(100)])
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                snprintf(buf, sizeof(buf), LC_TEXT("%s of the Guild %s raised up to %d%% !"), g.GetName(), Globals.GetPrivName(type), value)
                SendNotice(buf)
##endif
            else:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if __MULTI_LANGUAGE_SYSTEM__
                SendGuildPrivNotice(LC_TEXT("%s of the Guild %s normal again."), g.GetName(), Globals.GetPrivName(type))
##else
                buf = str(['\0' for _ in range(100)])
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                snprintf(buf, sizeof(buf), LC_TEXT("%s of the Guild %s normal again."), g.GetName(), Globals.GetPrivName(type))
                SendNotice(buf)
##endif

    def GiveEmpirePriv(self, empire, type, value, bLog, end_time_sec):
        if EPrivType.MAX_PRIV_NUM <= type:
            #lani_err("PRIV_MANAGER: GiveEmpirePriv: wrong empire priv type(%u)", type)
            return

        #sys_log(0, "Set Empire Priv: empire(%d) type(%d) value(%d) duration_sec(%d)", empire, type, value, end_time_sec-get_global_time())

        value = MINMAX(0, value, 200)
        end_time_sec = MINMAX(0, end_time_sec, get_global_time()+60 *60 *24 *7)

        rkPrivEmpireData = self._m_aakPrivEmpireData[type][empire]
        rkPrivEmpireData.m_value = value
## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: rkPrivEmpireData.m_end_time_sec = end_time_sec;
        rkPrivEmpireData.m_end_time_sec.copy_from(end_time_sec)

        if value != 0:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if __MULTI_LANGUAGE_SYSTEM__
            SendPrivNotice(LC_TEXT("%s 's %s raised up to %d%% !"), Globals.GetEmpireName(empire), Globals.GetPrivName(type), value)
##else
            buf = str(['\0' for _ in range(100)])
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            snprintf(buf, sizeof(buf), LC_TEXT("%s 's %s raised up to %d%% !"), Globals.GetEmpireName(empire), Globals.GetPrivName(type), value)

            if empire != 0:
                SendNotice(buf)
            else:
                SendLog(buf)
##endif
        else:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if __MULTI_LANGUAGE_SYSTEM__
            SendPrivNotice(LC_TEXT("%s 's %s normal again."), Globals.GetEmpireName(empire), Globals.GetPrivName(type))
##else
            buf = str(['\0' for _ in range(100)])
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            snprintf(buf, sizeof(buf), LC_TEXT("%s 's %s normal again."), Globals.GetEmpireName(empire), Globals.GetPrivName(type))

            if empire != 0:
                SendNotice(buf)
            else:
                SendLog(buf)
##endif

    def GiveCharacterPriv(self, pid, type, value, bLog):
        if EPrivType.MAX_PRIV_NUM <= type:
            #lani_err("PRIV_MANAGER: GiveCharacterPriv: wrong char priv type(%u)", type)
            return

        #sys_log(0,"Set Character Priv %u %d %d", pid, type, value)

        value = MINMAX(0, value, 100)

        self._m_aPrivChar[type][pid] = value

    def RemoveGuildPriv(self, guild_id, type):
        if EPrivType.MAX_PRIV_NUM <= type:
            #lani_err("PRIV_MANAGER: RemoveGuildPriv: wrong guild priv type(%u)", type)
            return

        self._m_aPrivGuild[type][guild_id].value = 0
        self._m_aPrivGuild[type][guild_id].end_time_sec = 0

    def RemoveEmpirePriv(self, empire, type):
        if EPrivType.MAX_PRIV_NUM <= type:
            #lani_err("PRIV_MANAGER: RemoveEmpirePriv: wrong empire priv type(%u)", type)
            return

        rkPrivEmpireData = self._m_aakPrivEmpireData[type][empire]
        rkPrivEmpireData.m_value = 0
        rkPrivEmpireData.m_end_time_sec = 0

    def RemoveCharacterPriv(self, pid, type):
        if EPrivType.MAX_PRIV_NUM <= type:
            #lani_err("PRIV_MANAGER: RemoveCharacterPriv: wrong char priv type(%u)", type)
            return

        it = self._m_aPrivChar[type].find(pid)

        if it is not self._m_aPrivChar[type].end():
            self._m_aPrivChar[type].pop(it)

    def GetPriv(self, ch, type):
        val_ch = self.GetPrivByCharacter(ch.GetPlayerID(), type)

        if val_ch < 0 and not ch.IsEquipUniqueItem(uint(Globals.UNIQUE_ITEM_NO_BAD_LUCK_EFFECT)):
            return val_ch
        else:
            val = None

            val = MAX(val_ch, self.GetPrivByEmpire(0, type))
            val = MAX(val, self.GetPrivByEmpire(ch.GetEmpire(), type))

            if ch.GetGuild():
                val = MAX(val, self.GetPrivByGuild(ch.GetGuild().GetID(), type))

            return val

    def GetPrivByEmpire(self, bEmpire, type):
        pkPrivEmpireData = self.GetPrivByEmpireEx(bEmpire, type)

        if pkPrivEmpireData:
            return pkPrivEmpireData.m_value

        return 0

    def GetPrivByGuild(self, guild_id, type):
        if type >= EPrivType.MAX_PRIV_NUM:
            return 0

        itFind = self._m_aPrivGuild[type].find(guild_id)

        if itFind is self._m_aPrivGuild[type].end():
            return 0

        return itFind.second.value

    def GetPrivByCharacter(self, pid, type):
        if type >= EPrivType.MAX_PRIV_NUM:
            return 0

        it = self._m_aPrivChar[type].find(pid)

        if it is not self._m_aPrivChar[type].end():
            return it.second

        return 0

    class SPrivEmpireData:

        def __init__(self):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.m_value = 0
            self.m_end_time_sec = time_t()


    def GetPrivByEmpireEx(self, bEmpire, type):
        if type >= EPrivType.MAX_PRIV_NUM:
            return None

        if bEmpire >= LGEMiscellaneous.EMPIRE_MAX_NUM:
            return None

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
#ORIGINAL METINII C CODE: return &m_aakPrivEmpireData[type][bEmpire];
        return CPrivManager.SPrivEmpireData(self._m_aakPrivEmpireData[type][bEmpire])

    class SPrivGuildData:

        def __init__(self):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.value = 0
            self.end_time_sec = time_t()


## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: const CPrivManager::SPrivGuildData* GetPrivByGuildEx(uint dwGuildID, byte byType) const
    def GetPrivByGuildEx(self, dwGuildID, byType):
        if byType >= EPrivType.MAX_PRIV_NUM:
            return None

        itFind = self._m_aPrivGuild[byType].find(dwGuildID)

        if itFind is self._m_aPrivGuild[byType].end():
            return None

        return itFind.second
