from enum import Enum
import math

class SGuildMaster:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.pid = 0



class SGuildMember:

    def _initialize_instance_fields(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.pid = 0
        self.grade = 0
        self.is_general = 0
        self.job = 0
        self.level = 0
        self.offer_exp = 0
        self._dummy = 0
        self.name = ""



## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to multiple constructors:
#ORIGINAL METINII C CODE: SGuildMember(CHARACTER* ch, byte grade, uint offer_exp) : pid(ch->GetPlayerID()), grade(grade), is_general(0), job(ch->GetJob()), level(ch->GetLevel()), offer_exp(offer_exp), name(ch->GetName())
    def __init__(self, ch, grade, offer_exp):
        self._initialize_instance_fields()

        self.pid = ch.GetPlayerID()
        self.grade = grade
        self.is_general = 0
        self.job = ch.GetJob()
        self.level = byte(ch.GetLevel())
        self.offer_exp = offer_exp
        self.name = ch.GetName(LOCALE_LANIATUS)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to multiple constructors:
#ORIGINAL METINII C CODE: SGuildMember(uint pid, byte grade, byte is_general, byte job, byte level, uint offer_exp, char* name) : pid(pid), grade(grade), is_general(is_general), job(job), level(level), offer_exp(offer_exp), name(name)
    def __init__(self, pid, grade, is_general, job, level, offer_exp, name):
        self._initialize_instance_fields()

        self.pid = pid
        self.grade = grade
        self.is_general = is_general
        self.job = job
        self.level = level
        self.offer_exp = offer_exp
        self.name = name.arg_value


## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##pragma pack(1)
class SGuildMemberPacketData:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.pid = 0
        self.grade = 0
        self.is_general = 0
        self.job = 0
        self.level = 0
        self.offer = 0
        self.name_flag = 0
        self.name = str(['\0' for _ in range((int)LGEMiscellaneous.CHARACTER_NAME_MAX_LEN+1)])


class packet_guild_sub_info:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.member_count = 0
        self.max_member_count = 0
        self.guild_id = 0
        self.master_pid = 0
        self.exp = 0
        self.level = 0
        self.name = str(['\0' for _ in range((int)LGEMiscellaneous.GUILD_NAME_MAX_LEN+1)])
        self.gold = 0
        self.has_land = 0


class SGuildGrade:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.grade_name = str(['\0' for _ in range(Globals.GUILD_GRADE_NAME_MAX_LEN+1)])
        self.auth_flag = 0


class TOneGradeNamePacket:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.grade = 0
        self.grade_name = str(['\0' for _ in range(Globals.GUILD_GRADE_NAME_MAX_LEN+1)])


class TOneGradeAuthPacket:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.grade = 0
        self.auth = 0


class SGuildData:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.guild_id = 0
        self.master_pid = 0
        self.exp = 0
        self.level = 0
        self.name = str(['\0' for _ in range((int)LGEMiscellaneous.GUILD_NAME_MAX_LEN+1)])
        self.grade_array = [SGuildGrade() for _ in range(Globals.GUILD_GRADE_COUNT)]
        self.LG_SKILL_point = 0
        self.abySkill = [0 for _ in range((int)LaniatusETalentXes.GUILD_LG_SKILL_COUNT)]
        self.power = 0
        self.max_power = 0
        self.ladder_point = 0
        self.win = 0
        self.draw = 0
        self.loss = 0
        self.gold = 0








class TGuildCreateParameter:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.master = None
        self.name = str(['\0' for _ in range((int)LGEMiscellaneous.GUILD_NAME_MAX_LEN+1)])


class SGuildWar:

    def __init__(self, type):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.war_start_time = 0
        self.score = 0
        self.state = 0
        self.type = 0
        self.map_index = 0

        self.war_start_time = 0
        self.score = 0
        self.state = EGuildWarState.GUILD_WAR_RECV_DECLARE
        self.type = type
        self.map_index = 0
## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: bool IsWarBegin() const
    def IsWarBegin(self):
        return self.state == EGuildWarState.GUILD_WAR_ON_WAR

class CGuild:

    def _initialize_instance_fields(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self._m_data = SGuildData()
        self._m_general_count = 0
        self._m_iMemberCountBonus = 0
        self._m_member = {}
        self._m_memberOnline = boost.unordered_set()
        self._m_memberP2POnline = std::set()
        self._m_EnemyGuild = {}
        self._m_mapGuildWarEndTime = {}
        self._abSkillUsable = [False for _ in range((int)LaniatusETalentXes.GUILD_LG_SKILL_COUNT)]
        self._m_GuildInviteEventMap = EventMap()
        self.m_guildPostCommentPulse = 0

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to multiple constructors:
#ORIGINAL METINII C CODE: CGuild(TGuildCreateParameter & cp)
    def __init__(self, cp):
        self._initialize_instance_fields()

        self._Initialize()

        self._m_general_count = 0

        self._m_iMemberCountBonus = 0

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        strncpy_s(self._m_data.name, sizeof(self._m_data.name), cp.name, _TRUNCATE)
        self._m_data.master_pid = cp.master.GetPlayerID()
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if __MULTI_LANGUAGE_SYSTEM__
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        strncpy_s(self._m_data.grade_array[0].grade_name, sizeof(self._m_data.grade_array[0].grade_name), "Leader", _TRUNCATE)
##else
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        strncpy_s(self._m_data.grade_array[0].grade_name, sizeof(self._m_data.grade_array[0].grade_name), LC_TEXT("Leader"), _TRUNCATE)
##endif
        self._m_data.grade_array[0].auth_flag = byte(Globals.GUILD_AUTH_ADD_MEMBER | Globals.GUILD_AUTH_REMOVE_MEMBER | Globals.GUILD_AUTH_NOTICE | Globals.GUILD_AUTH_USE_SKILL)

        LaniatusDefVariables = 1
        while LaniatusDefVariables < Globals.GUILD_GRADE_COUNT:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if __MULTI_LANGUAGE_SYSTEM__
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            strncpy_s(self._m_data.grade_array[LaniatusDefVariables].grade_name, sizeof(self._m_data.grade_array[LaniatusDefVariables].grade_name), "...", _TRUNCATE)
##else
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            strncpy_s(self._m_data.grade_array[LaniatusDefVariables].grade_name, sizeof(self._m_data.grade_array[LaniatusDefVariables].grade_name), LC_TEXT("Member"), _TRUNCATE)
##endif
            self._m_data.grade_array[LaniatusDefVariables].auth_flag = 0
            LaniatusDefVariables += 1

        ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The typedef 'SQLMsg' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
        pmsg = std::unique_ptr(DBManager.instance().DirectQuery("INSERT INTO guild%s(name, master, sp, level, exp, LG_SKILL_point, skill) " + "VALUES('%s', %u, 1000, 1, 0, 0, '\\0\\0\\0\\0\\0\\0\\0\\0\\0\\0\\0\\0')", get_table_postfix(), self._m_data.name, self._m_data.master_pid))

        self._m_data.guild_id = pmsg.Get().uiInsertID

        LaniatusDefVariables = 0
        while LaniatusDefVariables < Globals.GUILD_GRADE_COUNT:
            DBManager.instance().Query("INSERT INTO guild_grade%s VALUES(%u, %d, '%s', %d)", get_table_postfix(), self._m_data.guild_id, LaniatusDefVariables + 1, self._m_data.grade_array[LaniatusDefVariables].grade_name, self._m_data.grade_array[LaniatusDefVariables].auth_flag)
            LaniatusDefVariables += 1

        self.ComputeGuildPoints()
        self._m_data.power = self._m_data.max_power
        self._m_data.ladder_point = 0
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        db_clientdesc.DBPacket(Globals.LG_HEADER_GD_GUILD_CREATE, 0, self._m_data.guild_id, sizeof(uint))

        guild_skill = SPacketGuildSkillUpdate()
        guild_skill.guild_id = self._m_data.guild_id
        guild_skill.amount = 0
        guild_skill.LG_SKILL_point = 0
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
        memset(guild_skill.LG_SKILL_levels, 0, LaniatusETalentXes.GUILD_LG_SKILL_COUNT)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        db_clientdesc.DBPacket(Globals.LG_HEADER_GD_GUILD_LG_SKILL_UPDATE, 0, guild_skill, sizeof(guild_skill))

        CHARACTER_MANAGER.instance().for_each_pc.functor_method(FGuildNameSender(self.GetID(), self.GetName()))
        self.RequestAddMember(cp.master, Globals.GUILD_LEADER_GRADE)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to multiple constructors:
#ORIGINAL METINII C CODE: explicit CGuild(uint guild_id)
    def __init__(self, guild_id):
        self._initialize_instance_fields()

        self.Load(guild_id)
    def close(self):
        pass

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: uint GetID() const
    def GetID(self):
        return self._m_data.guild_id
## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: const char* GetName() const
    def GetName(self):
        return self._m_data.name
## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: int GetSP() const
    def GetSP(self):
        return self._m_data.power
    def GetMaxSP(self):
        return self._m_data.max_power
## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: uint GetMasterPID() const
    def GetMasterPID(self):
        return self._m_data.master_pid
    def GetMasterCharacter(self):
        return CHARACTER_MANAGER.instance().FindByPID(self.GetMasterPID())

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: byte GetLevel() const
    def GetLevel(self):
        return self._m_data.level
    def Reset(self):
        self._m_data.power = self._m_data.max_power
    def RequestDisband(self, pid):
        if self._m_data.master_pid != pid:
            return

        gd_guild = SPacketGuild()
        gd_guild.dwGuild = self.GetID()
        gd_guild.dwInfo = 0
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        db_clientdesc.DBPacket(Globals.LG_HEADER_GD_GUILD_DISBAND, 0, gd_guild, sizeof(SPacketGuild))
        building.CManager.instance().ClearLandByGuildID(self.GetID())

    def Disband(self):
        #sys_log(0, "GUILD: Disband %s:%u", self.GetName(), self.GetID())

        it = m_memberOnline.begin()
        while it is not self._m_memberOnline.end():
            ch = *it
            ch.SetGuild(None)
            self.SendOnlineRemoveOnePacket(ch.GetPlayerID())
            ch.SetQuestFlag("guild_manage.new_withdraw_time", get_global_time())
            it += 1

        it = m_member.begin()
        while it is not self._m_member.end():
            CGuildManager.instance().Unlink(it.first)
            it += 1


    def RequestAddMember(self, ch, grade = 15):
        if ch.GetGuild():
            return

        gd = SPacketGDGuildAddMember()

        if ch.GetPlayerID() in self._m_member.keys():
            #lani_err("Already a member in guild %s[%d]", ch.GetName(LOCALE_LANIATUS), ch.GetPlayerID())
            return

        gd.dwPID = ch.GetPlayerID()
        gd.dwGuild = self.GetID()
        gd.bGrade = byte(grade)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        db_clientdesc.DBPacket(Globals.LG_HEADER_GD_GUILD_ADD_MEMBER, 0, gd, sizeof(SPacketGDGuildAddMember))

    def AddMember(self, p):
        it = TGuildMemberContainer.iterator()

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((it = m_member.find(p->dwPID)) == m_member.end())
        if (it = self._m_member.find(p.dwPID)) is self._m_member.end():
            self._m_member.update({p.dwPID: TGuildMember(p.dwPID, p.bGrade, p.isGeneral, p.bJob, p.bLevel, p.dwOffer, p.szName)})
        else:
            r_gm = it.second
            r_gm.pid = p.dwPID
            r_gm.grade = p.bGrade
            r_gm.job = p.bJob
            r_gm.offer_exp = p.dwOffer
            r_gm.is_general = p.isGeneral

        CGuildManager.instance().Link(p.dwPID, self)

        self.SendListOneToAll(p.dwPID)

        ch = CHARACTER_MANAGER.instance().FindByPID(p.dwPID)

        #sys_log(0, "GUILD: AddMember PID %u, grade %u, job %u, level %u, offer %u, name %s ptr %p", p.dwPID, p.bGrade, p.bJob, p.bLevel, p.dwOffer, p.szName, Globals.get_pointer(ch))

        if ch:
            self.LoginMember(ch)
        else:
            self.P2PLoginMember(p.dwPID)

    def RequestRemoveMember(self, pid):
        it = TGuildMemberContainer.iterator()

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((it = m_member.find(pid)) == m_member.end())
        if (it = self._m_member.find(pid)) is self._m_member.end():
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if it.second.grade == Globals.GUILD_LEADER_GRADE:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        gd_guild = SPacketGuild()

        gd_guild.dwGuild = self.GetID()
        gd_guild.dwInfo = pid

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        db_clientdesc.DBPacket(Globals.LG_HEADER_GD_GUILD_REMOVE_MEMBER, 0, gd_guild, sizeof(SPacketGuild))
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def RemoveMember(self, pid):
        #sys_log(0, "Receive Guild P2P RemoveMember")
        it = TGuildMemberContainer.iterator()

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((it = m_member.find(pid)) == m_member.end())
        if (it = self._m_member.find(pid)) is self._m_member.end():
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if it.second.grade == Globals.GUILD_LEADER_GRADE:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if it.second.is_general:
            self._m_general_count -= 1

        self._m_member.pop(it)
        self.SendOnlineRemoveOnePacket(pid)

        CGuildManager.instance().Unlink(pid)

        ch = CHARACTER_MANAGER.instance().FindByPID(pid)

        if ch:
            self._m_memberOnline.erase(ch)
            ch.SetGuild(None)

        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def LoginMember(self, ch):
        if ch.GetPlayerID() not in self._m_member.keys():
            #lani_err("GUILD %s[%d] is not a memeber of guild.", ch.GetName(LOCALE_LANIATUS), ch.GetPlayerID())
            return

        ch.SetGuild(self)

        it = m_memberOnline.begin()
        while it is not self._m_memberOnline.end():
            SendLoginPacket(*it, ch)
            it += 1

        self._m_memberOnline.insert(ch)

        self.SendAllGradePacket(ch)
        self.SendGuildInfoPacket(ch)
        self.SendListPacket(ch)
        self.SendSkillInfoPacket(ch)
        self.SendEnemyGuild(ch)

    def P2PLoginMember(self, pid):
        if pid not in self._m_member.keys():
            #lani_err("GUILD [%d] is not a memeber of guild.", pid)
            return

        self._m_memberP2POnline.insert(pid)

        it = m_memberOnline.begin()
        while it is not self._m_memberOnline.end():
            SendLoginPacket(*it, pid)
            it += 1

    def LogoutMember(self, ch):
        if ch.GetPlayerID() not in self._m_member.keys():
            #lani_err("GUILD %s[%d] is not a memeber of guild.", ch.GetName(LOCALE_LANIATUS), ch.GetPlayerID())
            return

        self._m_memberOnline.erase(ch)

        it = m_memberOnline.begin()
        while it is not self._m_memberOnline.end():
            SendLogoutPacket(*it, ch)
            it += 1

    def P2PLogoutMember(self, pid):
        if pid not in self._m_member.keys():
            #lani_err("GUILD [%d] is not a memeber of guild.", pid)
            return

        self._m_memberP2POnline.erase(pid)

        it = m_memberOnline.begin()
        while it is not self._m_memberOnline.end():
            SendLogoutPacket(*it, pid)
            it += 1

    def ChangeMemberGrade(self, pid, grade):
        if grade == 1:
            return

        it = self._m_member.find(pid)

        if it is self._m_member.end():
            return

        it.second.grade = grade

        itOnline = self._m_memberOnline.begin()

        pack = packet_guild()
        pack.header = byte(Globals.LG_HEADER_GC_GUILD)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        pack.size = sizeof(pack)+5
        pack.subheader = byte(Globals.GUILD_SUBLG_HEADER_GC_CHANGE_MEMBER_GRADE)

        while itOnline is not self._m_memberOnline.end():
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: DESC* d = (*(itOnline++))->GetDesc();
            d = (*(itOnline)).GetDesc()
            itOnline += 1

            if d is None:
                continue

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            d.BufferedPacket(pack, sizeof(pack))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            d.BufferedPacket(pid, sizeof(pid))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            d.Packet(grade, sizeof(grade))

        self.SaveMember(pid)

        gd_guild = SPacketGuildChangeMemberData()

        gd_guild.guild_id = self.GetID()
        gd_guild.pid = pid
        gd_guild.offer = it.second.offer_exp
        gd_guild.level = it.second.level
        gd_guild.grade = grade

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        db_clientdesc.DBPacket(Globals.LG_HEADER_GD_GUILD_CHANGE_MEMBER_DATA, 0, gd_guild, sizeof(gd_guild))

    def OfferExp(self, ch, amount):
        cit = self._m_member.find(ch.GetPlayerID())

        if cit is self._m_member.end():
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if self._m_data.exp+amount < self._m_data.exp:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if amount < 0:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if ch.GetExp() < amount:
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> Provided Experience is larger then left Experience."))
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if ch.GetExp() - amount > ch.GetExp():
            #lani_err("Wrong guild offer amount %d by %s[%u]", amount, ch.GetName(LOCALE_LANIATUS), ch.GetPlayerID())
            return LGEMiscellaneous.DEFINECONSTANTS.false

        ch.PointChange(EPointTypes.LG_POINT_EXP, -amount, DefineConstants.false, DefineConstants.false)

        guild_exp = SPacketGuildExpUpdate()
        guild_exp.guild_id = self.GetID()
        guild_exp.amount = math.trunc(amount / float(100))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        db_clientdesc.DBPacket(Globals.LG_HEADER_GD_GUILD_EXP_UPDATE, 0, guild_exp, sizeof(guild_exp))
        self.GuildPointChange(EPointTypes.LG_POINT_EXP, math.trunc(amount / float(100)), ((not LGEMiscellaneous.DEFINECONSTANTS.false)))

        cit.second.offer_exp += math.trunc(amount / float(100))
        cit.second._dummy = 0

        pack = packet_guild()
        pack.header = byte(Globals.LG_HEADER_GC_GUILD)

        it = m_memberOnline.begin()
        while it is not self._m_memberOnline.end():
            d = it.GetDesc()
            if d:
                pack.subheader = byte(Globals.GUILD_SUBLG_HEADER_GC_LIST)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                pack.size = sizeof(pack) + 13
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                d.BufferedPacket(pack, sizeof(pack))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                d.Packet((cit.second), sizeof(uint) * 3 + 1)
            it += 1

        self.SaveMember(ch.GetPlayerID())

        gd_guild = SPacketGuildChangeMemberData()

        gd_guild.guild_id = self.GetID()
        gd_guild.pid = ch.GetPlayerID()
        gd_guild.offer = cit.second.offer_exp
        gd_guild.level = byte(ch.GetLevel())
        gd_guild.grade = cit.second.grade

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        db_clientdesc.DBPacket(Globals.LG_HEADER_GD_GUILD_CHANGE_MEMBER_DATA, 0, gd_guild, sizeof(gd_guild))
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def LevelChange(self, pid, level):
        cit = self._m_member.find(pid)

        if cit is self._m_member.end():
            return

        cit.second.level = level

        gd_guild = SPacketGuildChangeMemberData()

        gd_guild.guild_id = self.GetID()
        gd_guild.pid = pid
        gd_guild.offer = cit.second.offer_exp
        gd_guild.grade = cit.second.grade
        gd_guild.level = level

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        db_clientdesc.DBPacket(Globals.LG_HEADER_GD_GUILD_CHANGE_MEMBER_DATA, 0, gd_guild, sizeof(gd_guild))

        pack = packet_guild()
        pack.header = byte(Globals.LG_HEADER_GC_GUILD)
        cit.second._dummy = 0

        it = m_memberOnline.begin()
        while it is not self._m_memberOnline.end():
            d = it.GetDesc()

            if d:
                pack.subheader = byte(Globals.GUILD_SUBLG_HEADER_GC_LIST)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                pack.size = sizeof(pack) + 13
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                d.BufferedPacket(pack, sizeof(pack))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                d.Packet((cit.second), sizeof(uint) * 3 + 1)
            it += 1

    def ChangeMemberData(self, pid, offer, level, grade):
        cit = self._m_member.find(pid)

        if cit is self._m_member.end():
            return

        cit.second.offer_exp = offer
        cit.second.level = level
        cit.second.grade = grade
        cit.second._dummy = 0

        pack = packet_guild()
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memset(pack, 0, sizeof(pack))
        pack.header = byte(Globals.LG_HEADER_GC_GUILD)

        it = m_memberOnline.begin()
        while it is not self._m_memberOnline.end():
            d = it.GetDesc()
            if d:
                pack.subheader = byte(Globals.GUILD_SUBLG_HEADER_GC_LIST)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                pack.size = sizeof(pack) + 13
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                d.BufferedPacket(pack, sizeof(pack))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                d.Packet((cit.second), sizeof(uint) * 3 + 1)
            it += 1

    def ChangeGradeName(self, grade, grade_name):
        if grade == 1:
            return

        if grade < 1 or grade > 15:
            #lani_err("Wrong guild grade value %d", grade)
            return

        if len(grade_name) > LGEMiscellaneous.GUILD_NAME_MAX_LEN:
            return

        if (not grade_name[0]) != '\0':
            return

        text = str(['\0' for _ in range((int)LGEMiscellaneous.GUILD_NAME_MAX_LEN * 2 + 1)])

        temp_ref_text = RefObject(text);
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        DBManager.instance().EscapeString(temp_ref_text, sizeof(text), grade_name, len(grade_name))
        text = temp_ref_text.arg_value
        DBManager.instance().FuncAfterQuery(FSendChangeGrade(self.GetID(), grade), "UPDATE guild_grade%s SET name = '%s' where guild_id = %u and grade = %d", get_table_postfix(), text, self._m_data.guild_id, grade)

        grade -= 1
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        strncpy_s(self._m_data.grade_array[grade].grade_name, sizeof(self._m_data.grade_array[grade].grade_name), grade_name, _TRUNCATE)

        pack = packet_guild()
        pack.header = byte(Globals.LG_HEADER_GC_GUILD)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        pack.size = sizeof(pack)
        pack.subheader = byte(Globals.GUILD_SUBLG_HEADER_GC_GRADE_NAME)

        pack2 = TOneGradeNamePacket()
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        pack.size+=sizeof(pack2)
        pack2.grade = byte(grade+1)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        strncpy_s(pack2.grade_name, sizeof(pack2.grade_name), grade_name, _TRUNCATE)

        buf = TEMP_BUFFER(8192, DefineConstants.false)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        buf.write(pack, sizeof(pack))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        buf.write(pack2, sizeof(pack2))

        it = m_memberOnline.begin()
        while it is not self._m_memberOnline.end():
            d = it.GetDesc()

            if d:
                d.Packet(buf.read_peek(), buf.size())
            it += 1

    def ChangeGradeAuth(self, grade, auth):
        if grade == 1:
            return

        if grade < 1 or grade > 15:
            #lani_err("Wrong guild grade value %d", grade)
            return

        DBManager.instance().FuncAfterQuery(FSendChangeGrade(self.GetID(), grade), "UPDATE guild_grade%s SET auth = %d where guild_id = %u and grade = %d", get_table_postfix(), auth, self._m_data.guild_id, grade)

        grade -= 1

        self._m_data.grade_array[grade].auth_flag = auth

        pack = packet_guild()
        pack.header = byte(Globals.LG_HEADER_GC_GUILD)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        pack.size = sizeof(pack)
        pack.subheader = byte(Globals.GUILD_SUBLG_HEADER_GC_GRADE_AUTH)

        pack2 = TOneGradeAuthPacket()
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        pack.size += sizeof(pack2)
        pack2.grade = byte(grade + 1)
        pack2.auth = auth

        buf = TEMP_BUFFER(8192, DefineConstants.false)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        buf.write(pack, sizeof(pack))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        buf.write(pack2, sizeof(pack2))

        it = m_memberOnline.begin()
        while it is not self._m_memberOnline.end():
            d = it.GetDesc()

            if d:
                d.Packet(buf.read_peek(), buf.size())
            it += 1

    def P2PChangeGrade(self, grade):
        DBManager.instance().FuncQuery(std::bind(self.__P2PUpdateGrade, self, std::placeholders._1), "SELECT grade, name, auth+0 FROM guild_grade%s WHERE guild_id = %u and grade = %d", get_table_postfix(), self._m_data.guild_id, grade)

    def ChangeMemberGeneral(self, pid, is_general):
        if is_general != 0 and self.GetGeneralCount() >= self.GetMaxGeneralCount():
            return LGEMiscellaneous.DEFINECONSTANTS.false

        it = self._m_member.find(pid)
        if it is self._m_member.end():
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        is_general = byte(1 if is_general != 0 1 else 0)

        if it.second.is_general == is_general:
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        if is_general != 0:
            self._m_general_count += 1
        else:
            self._m_general_count -= 1

        it.second.is_general = is_general

        itOnline = self._m_memberOnline.begin()

        pack = packet_guild()
        pack.header = byte(Globals.LG_HEADER_GC_GUILD)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        pack.size = sizeof(pack)+5
        pack.subheader = byte(Globals.GUILD_SUBLG_HEADER_GC_CHANGE_MEMBER_GENERAL)

        while itOnline is not self._m_memberOnline.end():
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: DESC* d = (*(itOnline++))->GetDesc();
            d = (*(itOnline)).GetDesc()
            itOnline += 1

            if d is None:
                continue

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            d.BufferedPacket(pack, sizeof(pack))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            d.BufferedPacket(pid, sizeof(pid))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            d.Packet(is_general, sizeof(is_general))

        self.SaveMember(pid)
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def ChangeMasterTo(self, dwPID):
        if self.GetMember(dwPID) is None:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        p = tChangeGuildMaster()
        p.dwGuildID = self.GetID()
        p.idFrom = self.GetMasterPID()
        p.idTo = dwPID

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        db_clientdesc.DBPacket(Globals.LG_HEADER_GD_REQ_CHANGE_GUILD_MASTER, 0, p, sizeof(p))

        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def Packet(self, buf, size):
        it = m_memberOnline.begin()
        while it is not self._m_memberOnline.end():
            d = it.GetDesc()

            if d:
                d.Packet(buf, size)
            it += 1

    def SendOnlineRemoveOnePacket(self, pid):
        pack = packet_guild()
        pack.header = byte(Globals.LG_HEADER_GC_GUILD)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        pack.size = sizeof(pack)+4
        pack.subheader = byte(Globals.GUILD_SUBLG_HEADER_GC_REMOVE)

        buf = TEMP_BUFFER(8192, DefineConstants.false)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        buf.write(pack, sizeof(pack))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        buf.write(pid, sizeof(pid))

        it = m_memberOnline.begin()
        while it is not self._m_memberOnline.end():
            d = it.GetDesc()

            if d:
                d.Packet(buf.read_peek(), buf.size())
            it += 1

    def SendAllGradePacket(self, ch):
        d = ch.GetDesc()
        if d is None:
            return

        pack = packet_guild()
        pack.header = byte(Globals.LG_HEADER_GC_GUILD)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        pack.size = sizeof(pack)+1+Globals.GUILD_GRADE_COUNT*(sizeof(SGuildGrade)+1)
        pack.subheader = byte(Globals.GUILD_SUBLG_HEADER_GC_GRADE)

        buf = TEMP_BUFFER(8192, DefineConstants.false)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        buf.write(pack, sizeof(pack))
        n = 15
        buf.write(n, 1)

        LaniatusDefVariables = 0
        while i<Globals.GUILD_GRADE_COUNT:
            j = byte(i+1)
            buf.write(j, 1)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            buf.write(self._m_data.grade_array[LaniatusDefVariables], sizeof(SGuildGrade))
            LaniatusDefVariables += 1

        d.Packet(buf.read_peek(), buf.size())

    def SendListPacket(self, ch):
        d = None
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if (!(d=ch->GetDesc()))
        if not(d = ch.GetDesc()):
            return

        pack = packet_guild()
        pack.header = byte(Globals.LG_HEADER_GC_GUILD)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        pack.size = sizeof(packet_guild)
        pack.subheader = byte(Globals.GUILD_SUBLG_HEADER_GC_LIST)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        pack.size += sizeof(SGuildMemberPacketData) * len(self._m_member)

        buf = TEMP_BUFFER(8192, DefineConstants.false)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        buf.write(pack, sizeof(pack))

        c = str(['\0' for _ in range((int)LGEMiscellaneous.CHARACTER_NAME_MAX_LEN+1)])

        it = m_member.begin()
        while it is not self._m_member.end():
            it.second._dummy = 1

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            buf.write((it.second), sizeof(uint)*3+1)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            strncpy_s(c, MIN(sizeof(c), it.second.name.length() + 1), it.second.name.c_str(), _TRUNCATE)

            buf.write(c, LGEMiscellaneous.CHARACTER_NAME_MAX_LEN+1)

            if test_server:
                #sys_log(0,"name %s job %d  ", it.second.name.c_str(), it.second.job)
            it += 1

        d.Packet(buf.read_peek(), buf.size())

        it = m_memberOnline.begin()
        while it is not self._m_memberOnline.end():
            SendLoginPacket(ch, *it)
            it += 1

        it = m_memberP2POnline.begin()
        while it is not self._m_memberP2POnline.end():
            SendLoginPacket(ch, *it)
            it += 1


    def SendListOneToAll(self, pid):

        pack = packet_guild()
        pack.header = byte(Globals.LG_HEADER_GC_GUILD)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        pack.size = sizeof(packet_guild)
        pack.subheader = byte(Globals.GUILD_SUBLG_HEADER_GC_LIST)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        pack.size += sizeof(SGuildMemberPacketData)

        c = str(['\0' for _ in range((int)LGEMiscellaneous.CHARACTER_NAME_MAX_LEN+1)])
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memset(c, 0, sizeof(c))

        cit = self._m_member.find(pid)
        if cit is self._m_member.end():
            return

        it = m_memberOnline.begin()
        while it is not self._m_memberOnline.end():
            d = it.GetDesc()
            if d is None:
                continue

            buf = TEMP_BUFFER(8192, DefineConstants.false)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            buf.write(pack, sizeof(pack))

            cit.second._dummy = 1

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            buf.write((cit.second), sizeof(uint) * 3 +1)
            buf.write(cit.second.name.c_str(), cit.second.name.length())
            buf.write(c, LGEMiscellaneous.CHARACTER_NAME_MAX_LEN + 1 - cit.second.name.length())
            d.Packet(buf.read_peek(), buf.size())
            it += 1

    def SendListOneToAll(self, ch):
        self.SendListOneToAll(ch.GetPlayerID())

    def SendLoginPacket(self, ch, chLogin):
        self.SendLoginPacket(ch, chLogin.GetPlayerID())

    def SendLogoutPacket(self, ch, chLogout):
        self.SendLogoutPacket(ch, chLogout.GetPlayerID())

    def SendLoginPacket(self, ch, pid):
        if ch.GetDesc() is None:
            return

        pack = packet_guild()
        pack.header = byte(Globals.LG_HEADER_GC_GUILD)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        pack.size = sizeof(pack)+4
        pack.subheader = byte(Globals.GUILD_SUBLG_HEADER_GC_LOGIN)

        buf = TEMP_BUFFER(8192, DefineConstants.false)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        buf.write(pack, sizeof(pack))

        buf.write(pid, 4)

        ch.GetDesc().Packet(buf.read_peek(), buf.size())

    def SendLogoutPacket(self, ch, pid):
        if ch.GetDesc() is None:
            return

        pack = packet_guild()
        pack.header = byte(Globals.LG_HEADER_GC_GUILD)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        pack.size = sizeof(pack)+4
        pack.subheader = byte(Globals.GUILD_SUBLG_HEADER_GC_LOGOUT)

        buf = TEMP_BUFFER(8192, DefineConstants.false)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        buf.write(pack, sizeof(pack))
        buf.write(pid, 4)

        ch.GetDesc().Packet(buf.read_peek(), buf.size())

    def SendGuildInfoPacket(self, ch):
        d = ch.GetDesc()

        if d is None:
            return

        pack = packet_guild()
        pack.header = byte(Globals.LG_HEADER_GC_GUILD)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        pack.size = sizeof(packet_guild) + sizeof(packet_guild_sub_info)
        pack.subheader = byte(Globals.GUILD_SUBLG_HEADER_GC_INFO)

        pack_sub = packet_guild_sub_info()

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memset(pack_sub, 0, sizeof(packet_guild_sub_info))
        pack_sub.member_count = ushort(self.GetMemberCount())
        pack_sub.max_member_count = ushort(self.GetMaxMemberCount())
        pack_sub.guild_id = self._m_data.guild_id
        pack_sub.master_pid = self._m_data.master_pid
        pack_sub.exp = self._m_data.exp
        pack_sub.level = self._m_data.level
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        strncpy_s(pack_sub.name, sizeof(pack_sub.name), self._m_data.name, _TRUNCATE)
        pack_sub.gold = uint(self._m_data.gold)
        pack_sub.has_land = 1 if self.HasLand() else 0

        #sys_log(0, "GMC guild_name %s", self._m_data.name)
        #sys_log(0, "GMC master %d", self._m_data.master_pid)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        d.BufferedPacket(pack, sizeof(packet_guild))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        d.Packet(pack_sub, sizeof(packet_guild_sub_info))

    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The typedef 'SQLMsg' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
    def SendGuildDataUpdateToAllMember(self, pmsg):
        iter = self._m_memberOnline.begin()

        while iter is not self._m_memberOnline.end():
            self.SendGuildInfoPacket(iter)
            self.SendAllGradePacket(iter)
            iter += 1

    def Load(self, guild_id):
        self._Initialize()

        self._m_data.guild_id = guild_id

        DBManager.instance().FuncQuery(std::bind(self.LoadGuildData, self, std::placeholders._1), "SELECT master, level, exp, name, LG_SKILL_point, skill, sp, ladder_point, win, draw, loss, gold FROM guild%s WHERE id = %u", get_table_postfix(), self._m_data.guild_id)

        #sys_log(0, "GUILD: loading guild id %12s %u", self._m_data.name, guild_id)

        DBManager.instance().FuncQuery(std::bind(self.LoadGuildGradeData, self, std::placeholders._1), "SELECT grade, name, auth+0 FROM guild_grade%s WHERE guild_id = %u", get_table_postfix(), self._m_data.guild_id)

        DBManager.instance().FuncQuery(std::bind(self.LoadGuildMemberData, self, std::placeholders._1), "SELECT pid, grade, is_general, offer, level, job, name FROM guild_member%s, player%s WHERE guild_id = %u and pid = id", get_table_postfix(), get_table_postfix(), guild_id)

    def SaveLevel(self):
        DBManager.instance().Query("UPDATE guild%s SET level=%d, exp=%u, LG_SKILL_point=%d WHERE id = %u", get_table_postfix(), self._m_data.level,self._m_data.exp, self._m_data.LG_SKILL_point,self._m_data.guild_id)

    def SaveSkill(self):
        text = str(['\0' for _ in range((int)LaniatusETalentXes.GUILD_LG_SKILL_COUNT * 2 + 1)])

        temp_ref_text = RefObject(text);
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        DBManager.instance().EscapeString(temp_ref_text, sizeof(text), str(self._m_data.abySkill), sizeof(self._m_data.abySkill))
        text = temp_ref_text.arg_value
        DBManager.instance().Query("UPDATE guild%s SET sp = %d, LG_SKILL_point=%d, skill='%s' WHERE id = %u", get_table_postfix(), self._m_data.power, self._m_data.LG_SKILL_point, text, self._m_data.guild_id)

    def SaveMember(self, pid):
        it = self._m_member.find(pid)

        if it is self._m_member.end():
            return

        DBManager.instance().Query("UPDATE guild_member%s SET grade = %d, offer = %u, is_general = %d WHERE pid = %u and guild_id = %u", get_table_postfix(), it.second.grade, it.second.offer_exp, it.second.is_general, pid, self._m_data.guild_id)

    def GetMaxMemberCount(self):
        if self._m_iMemberCountBonus < 0 or self._m_iMemberCountBonus > 18:
            self._m_iMemberCountBonus = 0

        return 32 + 2 * (self._m_data.level-1) + self._m_iMemberCountBonus

    def GetMemberCount(self):
        return len(self._m_member)
## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: int GetTotalLevel() const
    def GetTotalLevel(self):
        total = 0

        it = m_member.begin()
        while it is not self._m_member.end():
            total += it.second.level
            it += 1

        return total

    def SetMemberCountBonus(self, iBonus):
        self._m_iMemberCountBonus = iBonus
        #sys_log(0, "GUILD_IS_FULL_BUG : Bonus set to %d(val:%d)", iBonus, self._m_iMemberCountBonus)

    def BroadcastMemberCountBonus(self):
        p1 = SPacketGGGuild()

        p1.bHeader = byte(Globals.LG_HEADER_GG_GUILD)
        p1.bSubHeader = byte(Globals.GUILD_SUBLG_HEADER_GG_SET_MEMBER_COUNT_BONUS)
        p1.dwGuild = self.GetID()

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        P2P_MANAGER.instance().Send(p1, sizeof(SPacketGGGuild), NULL)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        P2P_MANAGER.instance().Send(self._m_iMemberCountBonus, sizeof(int), NULL)

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: int GetMaxGeneralCount() const
    def GetMaxGeneralCount(self):
        return 1
## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: int GetGeneralCount() const
    def GetGeneralCount(self):
        return self._m_general_count
    def GetMember(self, pid):
        it = self._m_member.find(pid)
        if it is self._m_member.end():
            return None

        return it.second

    def GetMemberPID(self, strName):
        iter = m_member.begin()
        while iter is not self._m_member.end():
            if iter.second.name == strName:
                return iter.first
            iter += 1

        return 0

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: bool HasGradeAuth(int grade, int auth_flag) const
    def HasGradeAuth(self, grade, auth_flag):
        return bool((self._m_data.grade_array[grade-1].auth_flag & auth_flag))
    def AddComment(self, ch, str):
        if len(str) > Globals.GUILD_COMMENT_MAX_LEN or len(str) == 0:
            return

        if self.m_guildPostCommentPulse > thecore_pulse():
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
            deltaInSeconds = ((self.m_guildPostCommentPulse / ((1) * passes_per_sec)) - (thecore_pulse() / ((1) * passes_per_sec)))
            minutes = math.trunc(deltaInSeconds / float(60))
            seconds = (deltaInSeconds - (minutes * 60))

            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You can write another comment in %02d minutes and %02d seconds!"), minutes, seconds)
            return

        text = str(['\0' for _ in range(Globals.GUILD_COMMENT_MAX_LEN * 2 + 1)])
        temp_ref_text = RefObject(text);
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        DBManager.instance().EscapeString(temp_ref_text, sizeof(text), str, len(str))
        text = temp_ref_text.arg_value

        DBManager.instance().FuncAfterQuery(std::bind(self.RefreshCommentForce, self, ch.GetPlayerID()), "INSERT INTO guild_comment%s(guild_id, name, notice, content, time) VALUES(%u, '%s', %d, '%s', NOW())", get_table_postfix(), self._m_data.guild_id, ch.GetName(LOCALE_LANIATUS),1 if (str[0] == '!') else 0, text)

        self.m_guildPostCommentPulse = thecore_pulse() + ((5 *60) * passes_per_sec)

    def DeleteComment(self, ch, comment_id):
        ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The typedef 'SQLMsg' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
        pmsg = None

        if self.GetMember(ch.GetPlayerID()).grade == Globals.GUILD_LEADER_GRADE:
            pmsg = DBManager.instance().DirectQuery("DELETE FROM guild_comment%s WHERE id = %u AND guild_id = %u",get_table_postfix(), comment_id, self._m_data.guild_id)
        else:
            pmsg = DBManager.instance().DirectQuery("DELETE FROM guild_comment%s WHERE id = %u AND guild_id = %u AND name = '%s'",get_table_postfix(), comment_id, self._m_data.guild_id, ch.GetName(LOCALE_LANIATUS))

        if pmsg.Get().uiAffectedRows == 0 or pmsg.Get().uiAffectedRows == -1:
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> The message cannot be deleted."))
        else:
            self.RefreshCommentForce(ch.GetPlayerID())

        LG_DEL_MEM(pmsg)

    def RefreshComment(self, ch):
        self.RefreshCommentForce(ch.GetPlayerID())

    def RefreshCommentForce(self, player_id):
        ch = CHARACTER_MANAGER.instance().FindByPID(player_id)
        if ch is None:
            return

        ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The typedef 'SQLMsg' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
        pmsg = std::unique_ptr(DBManager.instance().DirectQuery("SELECT id, name, content FROM guild_comment%s WHERE guild_id = %u ORDER BY notice DESC, id DESC LIMIT %d", get_table_postfix(), self._m_data.guild_id, Globals.GUILD_COMMENT_MAX_COUNT))

        pack = packet_guild()
        pack.header = byte(Globals.LG_HEADER_GC_GUILD)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        pack.size = sizeof(pack)+1
        pack.subheader = byte(Globals.GUILD_SUBLG_HEADER_GC_COMMENTS)

        count = pmsg.Get().uiNumRows

        d = ch.GetDesc()

        if d is None:
            return

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        pack.size += (sizeof(uint)+LGEMiscellaneous.CHARACTER_NAME_MAX_LEN+1+Globals.GUILD_COMMENT_MAX_LEN+1)*count
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        d.BufferedPacket(pack, sizeof(pack))
        d.BufferedPacket(count, 1)
        szName = str(['\0' for _ in range((int)LGEMiscellaneous.CHARACTER_NAME_MAX_LEN + 1)])
        szContent = str(['\0' for _ in range(Globals.GUILD_COMMENT_MAX_LEN + 1)])
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memset(szName, 0, sizeof(szName))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memset(szContent, 0, sizeof(szContent))

        LaniatusDefVariables = 0
        while LaniatusDefVariables < pmsg.Get().uiNumRows:
            row = mysql_fetch_row(pmsg.Get().pSQLResult)
            id = strtoul(row[0], None, 10)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            strncpy_s(szName, sizeof(szName), row[1], _TRUNCATE)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            strncpy_s(szContent, sizeof(szContent), row[2], _TRUNCATE)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            d.BufferedPacket(id, sizeof(id))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            d.BufferedPacket(szName, sizeof(szName))

            if LaniatusDefVariables == pmsg.Get().uiNumRows - 1:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                d.Packet(szContent, sizeof(szContent))
            else:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                d.BufferedPacket(szContent, sizeof(szContent))
            LaniatusDefVariables += 1

    def GetSkillLevel(self, vnum):
        dwRealVnum = vnum - uint(LaniatusETalentXes.GUILD_LG_SKILL_START)

        if dwRealVnum >= LaniatusETalentXes.GUILD_LG_SKILL_COUNT:
            return 0

        return self._m_data.abySkill[dwRealVnum]

    def SkillLevelUp(self, dwVnum):
        dwRealVnum = dwVnum - uint(LaniatusETalentXes.GUILD_LG_SKILL_START)

        if dwRealVnum >= LaniatusETalentXes.GUILD_LG_SKILL_COUNT:
            return

        pkSk = CSkillManager.instance().Get(dwVnum)

        if pkSk is None:
            #lani_err("There is no such guild skill by number %u", dwVnum)
            return

        if self._m_data.abySkill[dwRealVnum] >= pkSk.bMaxLevel:
            return

        if self._m_data.LG_SKILL_point <= 0:
            return
        self._m_data.LG_SKILL_point -= 1

        self._m_data.abySkill[dwRealVnum] += 1

        self.ComputeGuildPoints()
        self.SaveSkill()
        self.SendDBSkillUpdate(0)
        for_each(self._m_memberOnline.begin(), self._m_memberOnline.end(), std::bind(self.SendSkillInfoPacket, self, std::placeholders._1))

        #sys_log(0, "Guild SkillUp: %s %d level %d type %u", self.GetName(), pkSk.dwVnum, self._m_data.abySkill[dwRealVnum], pkSk.dwType)

    def UseSkill(self, dwVnum, ch, pid):
        victim = None

        if self.GetMember(ch.GetPlayerID()) is None or not self.HasGradeAuth(self.GetMember(ch.GetPlayerID()).grade, Globals.GUILD_AUTH_USE_SKILL):
            return

        #sys_log(0,"GUILD_USE_SKILL : cname(%s), skill(%d)",ch.GetName(LOCALE_LANIATUS) if ch is not None else "", dwVnum)

        dwRealVnum = dwVnum - uint(LaniatusETalentXes.GUILD_LG_SKILL_START)

        if not ch.CanMove():
            return

        if dwRealVnum >= LaniatusETalentXes.GUILD_LG_SKILL_COUNT:
            return

        pkSk = CSkillManager.instance().Get(dwVnum)

        if pkSk is None:
            #lani_err("There is no such guild skill by number %u", dwVnum)
            return

        if self._m_data.abySkill[dwRealVnum] == 0:
            return

        if (pkSk.dwFlag & uint(ESkillFlags.LG_SKILL_FLAG_SELFONLY)) != 0:
            if ch.FindAffect(pkSk.dwVnum, APPLY_NONE):
                return

            victim = ch

        if ch.IsAffectFlag(EAffectBits.AFF_REVIVE_INVISIBLE):
            ch.RemoveAffect(LaniatusEAffectTypes.LANIA_AFFECT_REVIVE_INVISIBLE)

        if ch.IsAffectFlag(EAffectBits.AFF_EUNHYUNG):
            ch.RemoveAffect(LaniatusETalentXes.LG_SKILL_EUNHYUNG)

        k = 1.0 *self._m_data.abySkill[dwRealVnum]/pkSk.bMaxLevel
        pkSk.kSPCostPoly.SetVar("k", k)
        iNeededSP = int(pkSk.kSPCostPoly.Eval())

        if self.GetSP() < iNeededSP:
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> Not enough Dragon ghost. (%d, %d)"), self.GetSP(), iNeededSP)
            return

        pkSk.kCooldownPoly.SetVar("k", k)
        iCooltime = int(pkSk.kCooldownPoly.Eval())

        if not self._abSkillUsable[dwRealVnum]:
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> You cannot use Guild Skills yet."))
            return

            p = SPacketGuildUseSkill()
            p.dwGuild = self.GetID()
            p.dwSkillVnum = pkSk.dwVnum
            p.dwCooltime = uint(iCooltime)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            db_clientdesc.DBPacket(Globals.LG_HEADER_GD_GUILD_USE_SKILL, 0, p, sizeof(p))
        self._abSkillUsable[dwRealVnum] = LGEMiscellaneous.DEFINECONSTANTS.false

        if test_server:
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> %d Skills used (%d, %d) to %u"), dwVnum, self.GetSP(), iNeededSP, pid)

        if dwVnum == LaniatusETalentXes.GUILD_LG_SKILL_TELEPORT:
            self.SendDBSkillUpdate(-iNeededSP)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((victim = (CHARACTER_MANAGER::instance().FindByPID(pid))))
            if (victim = (CHARACTER_MANAGER.instance().FindByPID(pid))):
                ch.WarpSet(victim.GetX(), victim.GetY(), 0)
            else:
                if self._m_memberP2POnline.find(pid) != self._m_memberP2POnline.end():
                    pcci = P2P_MANAGER.instance().FindByPID(pid)

                    if pcci.bChannel != g_bChannel:
                        ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> The player is in channel %d. (Current channel: %d)"), pcci.bChannel, g_bChannel)
                    else:
                        p = SPacketGGFindPosition()
                        p.header = byte(Globals.LG_HEADER_GG_FIND_POSITION)
                        p.dwFromPID = ch.GetPlayerID()
                        p.dwTargetPID = pid
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                        pcci.pkDesc.Packet(p, sizeof(SPacketGGFindPosition))
                        if test_server:
                            ch.ChatPacket(EChatType.CHAT_TYPE_PARTY, "sent find position packet for guild teleport")
                else:
                    ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> The player is not online."))

        else:

                if self.UnderAnyWar(GUILD_WAR_TYPE_MAX_NUM) == 0:
                    ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> This Guild Skill can be used in war only."))
                    return

                self.SendDBSkillUpdate(-iNeededSP)

                it = m_memberOnline.begin()
                while it is not self._m_memberOnline.end():
                    victim = *it
                    victim.RemoveAffect(dwVnum)
                    ch.ComputeSkill(dwVnum, victim, self._m_data.abySkill[dwRealVnum])
                    it += 1

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: void SendSkillInfoPacket(CHARACTER* ch) const
    def SendSkillInfoPacket(self, ch):
        d = ch.GetDesc()

        if d is None:
            return

        pack = packet_guild()

        pack.header = byte(Globals.LG_HEADER_GC_GUILD)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        pack.size = sizeof(pack) + 6 + LaniatusETalentXes.GUILD_LG_SKILL_COUNT
        pack.subheader = byte(Globals.GUILD_SUBLG_HEADER_GC_LG_SKILL_INFO)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        d.BufferedPacket(pack, sizeof(pack))
        d.BufferedPacket(self._m_data.LG_SKILL_point, 1)
        d.BufferedPacket(self._m_data.abySkill, LaniatusETalentXes.GUILD_LG_SKILL_COUNT)
        d.BufferedPacket(self._m_data.power, 2)
        d.Packet(self._m_data.max_power, 2)

    def ComputeGuildPoints(self):
        self._m_data.max_power = Globals.GUILD_BASE_POWER + (self._m_data.level-1) * Globals.GUILD_POWER_PER_LEVEL

        self._m_data.power = MINMAX(0, self._m_data.power, self._m_data.max_power)

    def GuildPointChange(self, type, amount, save = LGEMiscellaneous.DefineConstants.false):
        if type == EPointTypes.LG_POINT_SP:
            self._m_data.power += amount

            self._m_data.power = MINMAX(0, self._m_data.power, self._m_data.max_power)

            if save:
                self.SaveSkill()

            for_each(self._m_memberOnline.begin(), self._m_memberOnline.end(), std::bind(self.SendSkillInfoPacket, self, std::placeholders._1))

        elif type == EPointTypes.LG_POINT_EXP:
            if amount < 0 and self._m_data.exp < (uint) - amount:
                self._m_data.exp = 0
            else:
                self._m_data.exp += uint(amount)

                while self._m_data.exp >= Globals.__guild_levelup_exp(self._m_data.level):

                    if self._m_data.level < LGEMiscellaneous.GUILD_MAX_LEVEL:
                        self._m_data.exp -= Globals.__guild_levelup_exp(self._m_data.level)
                        self._m_data.level += 1
                        self._m_data.LG_SKILL_point += 1

                        if self._m_data.level > LGEMiscellaneous.GUILD_MAX_LEVEL:
                            self._m_data.level = LGEMiscellaneous.GUILD_MAX_LEVEL

                        self.ComputeGuildPoints()
                        self.GuildPointChange(EPointTypes.LG_POINT_SP, self._m_data.max_power-self._m_data.power, DefineConstants.false)

                        if save:
                            self.ChangeLadderPoint(Globals.GUILD_LADDER_LG_POINT_PER_LEVEL)

                        for_each(self._m_memberOnline.begin(), self._m_memberOnline.end(), std::bind(self.SendGuildInfoPacket, self, std::placeholders._1))

                    if self._m_data.level == LGEMiscellaneous.GUILD_MAX_LEVEL:
                        self._m_data.exp = 0

            pack = packet_guild()
            pack.header = byte(Globals.LG_HEADER_GC_GUILD)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            pack.size = sizeof(pack)+5
            pack.subheader = byte(Globals.GUILD_SUBLG_HEADER_GC_CHANGE_EXP)

            buf = TEMP_BUFFER(8192, DefineConstants.false)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            buf.write(pack, sizeof(pack))
            buf.write(self._m_data.level, 1)
            buf.write(self._m_data.exp, 4)

            it = m_memberOnline.begin()
            while it is not self._m_memberOnline.end():
                d = it.GetDesc()

                if d:
                    d.Packet(buf.read_peek(), buf.size())
                it += 1

            if save:
                self.SaveLevel()


    def UpdateSkill(self, LG_SKILL_point, LG_SKILL_levels):
        self._m_data.LG_SKILL_point = LG_SKILL_point
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memcpy' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memcpy(self._m_data.abySkill, LG_SKILL_levels.arg_value, sizeof(byte) * LaniatusETalentXes.GUILD_LG_SKILL_COUNT)
        self.ComputeGuildPoints()

    def SendDBSkillUpdate(self, amount = 0):
        guild_skill = SPacketGuildSkillUpdate()
        guild_skill.guild_id = self._m_data.guild_id
        guild_skill.amount = amount
        guild_skill.LG_SKILL_point = self._m_data.LG_SKILL_point
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memcpy' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memcpy(guild_skill.LG_SKILL_levels, self._m_data.abySkill, sizeof(byte) * LaniatusETalentXes.GUILD_LG_SKILL_COUNT)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        db_clientdesc.DBPacket(Globals.LG_HEADER_GD_GUILD_LG_SKILL_UPDATE, 0, guild_skill, sizeof(guild_skill))

    def SkillRecharge(self):
        pass

    def ChargeSP(self, ch, iSP):
        gold = iSP * 100

        if gold < iSP or ch.GetGold() < gold:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        iRemainSP = self._m_data.max_power - self._m_data.power

        if iSP > iRemainSP:
            iSP = iRemainSP
            gold = iSP * 100

        ch.PointChange(EPointTypes.LG_POINT_GOLD, -gold, DefineConstants.false, DefineConstants.false)

        self.SendDBSkillUpdate(iSP)
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> %u Dragon ghost restored."), iSP)
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def Chat(self, c_pszText):
        std::for_each(self._m_memberOnline.begin(), self._m_memberOnline.end(), FGuildChat(c_pszText))

        p1 = SPacketGGGuild()
        p2 = SPacketGGGuildChat()

        p1.bHeader = byte(Globals.LG_HEADER_GG_GUILD)
        p1.bSubHeader = byte(Globals.GUILD_SUBLG_HEADER_GG_CHAT)
        p1.dwGuild = self.GetID()
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        strncpy_s(p2.szText, sizeof(p2.szText), c_pszText, _TRUNCATE)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        P2P_MANAGER.instance().Send(p1, sizeof(SPacketGGGuild), NULL)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        P2P_MANAGER.instance().Send(p2, sizeof(SPacketGGGuildChat), NULL)

    def P2PChat(self, c_pszText):
        std::for_each(self._m_memberOnline.begin(), self._m_memberOnline.end(), FGuildChat(c_pszText))

    def SkillUsableChange(self, dwSkillVnum, bUsable):
        dwRealVnum = dwSkillVnum - uint(LaniatusETalentXes.GUILD_LG_SKILL_START)

        if dwRealVnum >= LaniatusETalentXes.GUILD_LG_SKILL_COUNT:
            return

        self._abSkillUsable[dwRealVnum] = bUsable
        #sys_log(0, "CGuild::SkillUsableChange(guild=%s, skill=%d, usable=%d)", self.GetName(), dwSkillVnum, bUsable)

    def AdvanceLevel(self, iLevel):
        if self._m_data.level == iLevel:
            return

        self._m_data.level = MIN(LGEMiscellaneous.GUILD_MAX_LEVEL, iLevel)

    def RequestDepositMoney(self, ch, iGold):
        if LGEMiscellaneous.DEFINECONSTANTS.false==ch.CanDeposit():
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> Please use after a while."))
            return

        if ch.GetGold() < iGold:
            return


        ch.PointChange(EPointTypes.LG_POINT_GOLD, -iGold, DefineConstants.false, DefineConstants.false)

        p = SPacketGDGuildMoney()
        p.dwGuild = self.GetID()
        p.iGold = iGold
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        db_clientdesc.DBPacket(Globals.LG_HEADER_GD_GUILD_DEPOSIT_MONEY, 0, p, sizeof(p))

        ch.UpdateDepositPulse()
        #sys_log(0, "GUILD: DEPOSIT %s:%u player %s[%u] gold %lld", self.GetName(), self.GetID(), ch.GetName(LOCALE_LANIATUS), ch.GetPlayerID(), iGold)

    def RequestWithdrawMoney(self, ch, iGold):
        if LGEMiscellaneous.DEFINECONSTANTS.false==ch.CanDeposit():
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> Please use after a while."))
            return

        if ch.GetPlayerID() != self.GetMasterPID():
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> Only the Guild master can take out Yang."))
            return

        if self._m_data.gold < iGold:
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> You do not have enough Yang."))
            return

        p = SPacketGDGuildMoney()
        p.dwGuild = self.GetID()
        p.iGold = iGold
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        db_clientdesc.DBPacket(Globals.LG_HEADER_GD_GUILD_WITHDRAW_MONEY, 0, p, sizeof(p))

        ch.UpdateDepositPulse()

    def RecvMoneyChange(self, iGold):
        self._m_data.gold = int(iGold)

        p = packet_guild()
        p.header = byte(Globals.LG_HEADER_GC_GUILD)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        p.size = sizeof(p) + sizeof(int)
        p.subheader = byte(Globals.GUILD_SUBLG_HEADER_GC_MONEY_CHANGE)

        it = m_memberOnline.begin()
        while it is not self._m_memberOnline.end():
            ch = *it
            d = ch.GetDesc()
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            d.BufferedPacket(p, sizeof(p))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            d.Packet(iGold, sizeof(long))
            it += 1

    def RecvWithdrawMoneyGive(self, iChangeGold):
        ch = self.GetMasterCharacter()

        if ch:
            ch.PointChange(EPointTypes.LG_POINT_GOLD, iChangeGold, DefineConstants.false, DefineConstants.false)
            #sys_log(0, "GUILD: WITHDRAW %s:%u player %s[%u] gold %d", self.GetName(), self.GetID(), ch.GetName(LOCALE_LANIATUS), ch.GetPlayerID(), iChangeGold)

        p = SPacketGDGuildMoneyWithdrawGiveReply()
        p.dwGuild = self.GetID()
        p.iChangeGold = iChangeGold
        p.bGiveSuccess = byte(1 if ch is not None else 0)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        db_clientdesc.DBPacket(Globals.LG_HEADER_GD_GUILD_WITHDRAW_MONEY_GIVE_REPLY, 0, p, sizeof(p))

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: long GetGuildMoney() const
    def GetGuildMoney(self):
        return self._m_data.gold
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    GuildWarPacket(guild_id, bWarType, bWarState)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    SendEnemyGuild(ch)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    GetGuildWarState(guild_id)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    CanStartWar(bGuildWarType)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    GetWarStartTime(guild_id)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    UnderWar(guild_id)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    UnderAnyWar(bType = EGuildWarType.GUILD_WAR_TYPE_MAX_NUM)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    SetGuildWarMapIndex(dwGuildID, lMapIndex)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    GetGuildWarType(dwGuildOpponent)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    GetGuildWarMapIndex(dwGuildOpponent)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    GuildWarEntryAsk(guild_opp)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    GuildWarEntryAccept(guild_opp, ch)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    NotifyGuildMaster(msg)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    RequestDeclareWar(guild_id, type)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    RequestRefuseWar(guild_id)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    DeclareWar(guild_id, type, state)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    RefuseWar(guild_id)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    WaitStartWar(guild_id)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    CheckStartWar(guild_id)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    StartWar(guild_id)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    EndWar(guild_id)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    ReserveWar(guild_id, type)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    SetWarScoreAgainstTo(guild_opponent, newpoint)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    GetWarScoreAgainstTo(guild_opponent)
## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: int GetLadderPoint() const
    def GetLadderPoint(self):
        return self._m_data.ladder_point
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    SetLadderPoint(point)
    def SetWarData(self, iWin, iDraw, iLoss):
        self._m_data.win = iWin, self._m_data.draw = iDraw, self._m_data.loss = iLoss
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    ChangeLadderPoint(iChange)
## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: int GetGuildWarWinCount() const
    def GetGuildWarWinCount(self):
        return self._m_data.win
## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: int GetGuildWarDrawCount() const
    def GetGuildWarDrawCount(self):
        return self._m_data.draw
## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: int GetGuildWarLossCount() const
    def GetGuildWarLossCount(self):
        return self._m_data.loss
    def HasLand(self):
        return building.CManager.instance().FindLandByGuild(self.GetID()) is not None

    def Invite(self, pchInviter, pchInvitee):
        if quest.CQuestManager.instance().GetPCForce(pchInviter.GetPlayerID()).IsRunning() == ((not LGEMiscellaneous.DEFINECONSTANTS.false)):
            return


        if quest.CQuestManager.instance().GetPCForce(pchInvitee.GetPlayerID()).IsRunning() == ((not LGEMiscellaneous.DEFINECONSTANTS.false)):
            return

        if pchInvitee.IsBlockMode(EBlockAction.BLOCK_GUILD_INVITE):
            pchInviter.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> The player declines the Guild invitation."))
            return
        elif not self.HasGradeAuth(self.GetMember(pchInviter.GetPlayerID()).grade, Globals.GUILD_AUTH_ADD_MEMBER):
            pchInviter.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> You cannot invite someone into the Guild."))
            return
        elif pchInvitee.GetEmpire() != pchInviter.GetEmpire():
            pchInviter.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> You cannot invite players from another Kingdom into the Guild."))
            return

        errcode = self._VerifyGuildJoinableCondition(pchInvitee)
        if errcode == GuildJoinErrCode.GERR_NONE:
            pass
        elif errcode == GuildJoinErrCode.GERR_WITHDRAWPENALTY:
            pchInviter.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> The player can be invited again after %d days."), quest.CQuestManager.instance().GetEventFlag("guild_withdraw_delay"))
            return
        elif (errcode == GuildJoinErrCode.GERR_WITHDRAWPENALTY) or (errcode == GuildJoinErrCode.GERR_COMMISSIONPENALTY):
            pchInviter.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> After the rearrangement you can invite members again after %d days."), quest.CQuestManager.instance().GetEventFlag("guild_disband_delay"))
            return
        elif (errcode == GuildJoinErrCode.GERR_WITHDRAWPENALTY) or (errcode == GuildJoinErrCode.GERR_COMMISSIONPENALTY) or (errcode == GuildJoinErrCode.GERR_ALREADYJOIN):
            pchInviter.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> This person is already a member of another Guild."))
            return
        elif (errcode == GuildJoinErrCode.GERR_WITHDRAWPENALTY) or (errcode == GuildJoinErrCode.GERR_COMMISSIONPENALTY) or (errcode == GuildJoinErrCode.GERR_ALREADYJOIN) or (errcode == GuildJoinErrCode.GERR_GUILDISFULL):
            pchInviter.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> The Guild capacity reached its upper limit."))
            return
        elif (errcode == GuildJoinErrCode.GERR_WITHDRAWPENALTY) or (errcode == GuildJoinErrCode.GERR_COMMISSIONPENALTY) or (errcode == GuildJoinErrCode.GERR_ALREADYJOIN) or (errcode == GuildJoinErrCode.GERR_GUILDISFULL) or (errcode == GuildJoinErrCode.GERR_GUILD_IS_IN_WAR):
            pchInviter.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> The Guild is at war."))
            return
        elif (errcode == GuildJoinErrCode.GERR_WITHDRAWPENALTY) or (errcode == GuildJoinErrCode.GERR_COMMISSIONPENALTY) or (errcode == GuildJoinErrCode.GERR_ALREADYJOIN) or (errcode == GuildJoinErrCode.GERR_GUILDISFULL) or (errcode == GuildJoinErrCode.GERR_GUILD_IS_IN_WAR) or (errcode == GuildJoinErrCode.GERR_INVITE_LIMIT):
            pchInviter.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> You can't invite more people."))
            return


        if errcode != GERR_NONE:
            #lani_err("ignore guild join error(%d)", errcode)
            return

        if self._m_GuildInviteEventMap.end() != self._m_GuildInviteEventMap.find(pchInvitee.GetPlayerID()):
            return

        pInfo = Globals.AllocEventInfo()
        pInfo.dwInviteePID = pchInvitee.GetPlayerID()
        pInfo.dwGuildID = self.GetID()

        ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The typedef 'EventMap' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
        self._m_GuildInviteEventMap.insert(EventMap.value_type(pchInvitee.GetPlayerID(), event_create_ex(GuildInviteEvent, pInfo, ((10) * passes_per_sec))))
        gid = self.GetID()

        p = packet_guild()
        p.header = byte(Globals.LG_HEADER_GC_GUILD)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        p.size = sizeof(p) + sizeof(uint) + LGEMiscellaneous.GUILD_NAME_MAX_LEN + 1
        p.subheader = byte(Globals.GUILD_SUBLG_HEADER_GC_GUILD_INVITE)

        buf = TEMP_BUFFER(8192, DefineConstants.false)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        buf.write(p, sizeof(p))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        buf.write(gid, sizeof(uint))
        buf.write(self.GetName(), LGEMiscellaneous.GUILD_NAME_MAX_LEN + 1)

        pchInvitee.GetDesc().Packet(buf.read_peek(), buf.size())

    def InviteAccept(self, pchInvitee):
        itFind = self._m_GuildInviteEventMap.find(pchInvitee.GetPlayerID())
        if itFind == self._m_GuildInviteEventMap.end():
            #sys_log(0, "GuildInviteAccept from not invited character(invite guild: %s, invitee: %s)", self.GetName(), pchInvitee.GetName(LOCALE_LANIATUS))
            return

        event_cancel(itFind.second)
        self._m_GuildInviteEventMap.erase(itFind)

        errcode = self._VerifyGuildJoinableCondition(pchInvitee)
        if errcode == GuildJoinErrCode.GERR_NONE:
            pass
        elif errcode == GuildJoinErrCode.GERR_WITHDRAWPENALTY:
            pchInvitee.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> The player can be invited again after %d days."), quest.CQuestManager.instance().GetEventFlag("guild_withdraw_delay"))
            return
        elif (errcode == GuildJoinErrCode.GERR_WITHDRAWPENALTY) or (errcode == GuildJoinErrCode.GERR_COMMISSIONPENALTY):
            pchInvitee.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> After the rearrangement you can invite members again after %d days."), quest.CQuestManager.instance().GetEventFlag("guild_disband_delay"))
            return
        elif (errcode == GuildJoinErrCode.GERR_WITHDRAWPENALTY) or (errcode == GuildJoinErrCode.GERR_COMMISSIONPENALTY) or (errcode == GuildJoinErrCode.GERR_ALREADYJOIN):
            pchInvitee.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> This person is already a member of another Guild."))
            return
        elif (errcode == GuildJoinErrCode.GERR_WITHDRAWPENALTY) or (errcode == GuildJoinErrCode.GERR_COMMISSIONPENALTY) or (errcode == GuildJoinErrCode.GERR_ALREADYJOIN) or (errcode == GuildJoinErrCode.GERR_GUILDISFULL):
            pchInvitee.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> The Guild capacity reached its upper limit."))
            return
        elif (errcode == GuildJoinErrCode.GERR_WITHDRAWPENALTY) or (errcode == GuildJoinErrCode.GERR_COMMISSIONPENALTY) or (errcode == GuildJoinErrCode.GERR_ALREADYJOIN) or (errcode == GuildJoinErrCode.GERR_GUILDISFULL) or (errcode == GuildJoinErrCode.GERR_GUILD_IS_IN_WAR):
            pchInvitee.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> The Guild is at war."))
            return
        elif (errcode == GuildJoinErrCode.GERR_WITHDRAWPENALTY) or (errcode == GuildJoinErrCode.GERR_COMMISSIONPENALTY) or (errcode == GuildJoinErrCode.GERR_ALREADYJOIN) or (errcode == GuildJoinErrCode.GERR_GUILDISFULL) or (errcode == GuildJoinErrCode.GERR_GUILD_IS_IN_WAR) or (errcode == GuildJoinErrCode.GERR_INVITE_LIMIT):
            pchInvitee.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Guild> You can't invite more people."))
            return


        if errcode != GERR_NONE:
            #lani_err("ignore guild join error(%d)", errcode)
            return

        self.RequestAddMember(pchInvitee, 15)

    def InviteDeny(self, dwPID):
        itFind = self._m_GuildInviteEventMap.find(dwPID)
        if itFind == self._m_GuildInviteEventMap.end():
            #sys_log(0, "GuildInviteDeny from not invited character(invite guild: %s, invitee PID: %d)", self.GetName(), dwPID)
            return

        event_cancel(itFind.second)
        self._m_GuildInviteEventMap.erase(itFind)

    def _Initialize(self):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memset(self._m_data, 0, sizeof(self._m_data))
        self._m_data.level = 1

        LaniatusDefVariables = 0
        while LaniatusDefVariables < LaniatusETalentXes.GUILD_LG_SKILL_COUNT:
            self._abSkillUsable[LaniatusDefVariables] = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
            LaniatusDefVariables += 1

        self._m_iMemberCountBonus = 0





    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The typedef 'SQLMsg' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
    def _LoadGuildData(self, pmsg):
        if pmsg.Get().uiNumRows == 0:
            #lani_err("Query failed: getting guild data %s", pmsg.stQuery.c_str())
            return

        row = mysql_fetch_row(pmsg.Get().pSQLResult)
        self._m_data.master_pid = strtoul(row[0], str(None), 10)
        self._m_data.level = byte(int(strtoul(row[1], str(None), 10)))
        self._m_data.exp = strtoul(row[2], str(None), 10)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        strncpy_s(self._m_data.name, sizeof(self._m_data.name), row[3], _TRUNCATE)

        self._m_data.LG_SKILL_point = byte(int(strtoul(row[4], str(None), 10)))
        if row[5]:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memcpy' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            memcpy(self._m_data.abySkill, row[5], sizeof(byte) * LaniatusETalentXes.GUILD_LG_SKILL_COUNT)
        else:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            memset(self._m_data.abySkill, 0, sizeof(byte) * LaniatusETalentXes.GUILD_LG_SKILL_COUNT)

        self._m_data.power = MAX(0, strtoul(row[6], str(None), 10))

        temp_ref_ladder_point = RefObject(self._m_data.ladder_point);
        Globals.str_to_number(temp_ref_ladder_point, row[7])
        self._m_data.ladder_point = temp_ref_ladder_point.arg_value

        if self._m_data.ladder_point < 0:
            self._m_data.ladder_point = 0

        temp_ref_win = RefObject(self._m_data.win);
        Globals.str_to_number(temp_ref_win, row[8])
        self._m_data.win = temp_ref_win.arg_value
        temp_ref_draw = RefObject(self._m_data.draw);
        Globals.str_to_number(temp_ref_draw, row[9])
        self._m_data.draw = temp_ref_draw.arg_value
        temp_ref_loss = RefObject(self._m_data.loss);
        Globals.str_to_number(temp_ref_loss, row[10])
        self._m_data.loss = temp_ref_loss.arg_value
        temp_ref_gold = RefObject(self._m_data.gold);
        Globals.str_to_number(temp_ref_gold, row[11])
        self._m_data.gold = temp_ref_gold.arg_value

        self.ComputeGuildPoints()

    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The typedef 'SQLMsg' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
    def _LoadGuildGradeData(self, pmsg):
        LaniatusDefVariables = 0
        while LaniatusDefVariables < pmsg.Get().uiNumRows:
            row = mysql_fetch_row(pmsg.Get().pSQLResult)
            grade = 0
            temp_ref_grade = RefObject(grade);
            Globals.str_to_number(temp_ref_grade, row[0])
            grade = temp_ref_grade.arg_value
            name = row[1]
            auth = strtoul(row[2], None, 10)

            if grade >= 1 and grade <= 15:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                strncpy_s(self._m_data.grade_array[grade-1].grade_name, sizeof(self._m_data.grade_array[grade-1].grade_name), name, _TRUNCATE)
                self._m_data.grade_array[grade-1].auth_flag = byte(auth)
            LaniatusDefVariables += 1

    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The typedef 'SQLMsg' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
    def _LoadGuildMemberData(self, pmsg):
        if pmsg.Get().uiNumRows == 0:
            return

        self._m_general_count = 0

        self._m_member.clear()

        LaniatusDefVariables = 0
        while LaniatusDefVariables < pmsg.Get().uiNumRows:
            row = mysql_fetch_row(pmsg.Get().pSQLResult)

            pid = strtoul(row[0], str(None), 10)
            grade = byte(int(strtoul(row[1], str(None), 10)))
            is_general = 0

            if row[2] and *row[2] == '1':
                is_general = 1

            offer = strtoul(row[3], str(None), 10)
            level = byte(int(strtoul(row[4], str(None), 10)))
            job = byte(int(strtoul(row[5], str(None), 10)))
            name = row[6]

            if is_general != 0:
                self._m_general_count += 1

            self._m_member.update({pid: TGuildMember(pid, grade, is_general, job, level, offer, name)})
            CGuildManager.instance().Link(pid, self)
            LaniatusDefVariables += 1

    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The typedef 'SQLMsg' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
    def _P2PUpdateGrade(self, pmsg):
        if pmsg.Get().uiNumRows:
            row = mysql_fetch_row(pmsg.Get().pSQLResult)

            grade = 0
            name = row[1]
            auth = 0

            temp_ref_grade = RefObject(grade);
            Globals.str_to_number(temp_ref_grade, row[0])
            grade = temp_ref_grade.arg_value
            temp_ref_auth = RefObject(auth);
            Globals.str_to_number(temp_ref_auth, row[2])
            auth = temp_ref_auth.arg_value

            if grade <= 0:
                return

            grade -= 1

            if 0 != strcmp(self._m_data.grade_array[grade].grade_name, name):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                strncpy_s(self._m_data.grade_array[grade].grade_name, sizeof(self._m_data.grade_array[grade].grade_name), name, _TRUNCATE)

                pack = packet_guild()

                pack.header = byte(Globals.LG_HEADER_GC_GUILD)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                pack.size = sizeof(pack)
                pack.subheader = byte(Globals.GUILD_SUBLG_HEADER_GC_GRADE_NAME)

                pack2 = TOneGradeNamePacket()

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                pack.size += sizeof(pack2)
                pack2.grade = byte(grade + 1)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                strncpy_s(pack2.grade_name, sizeof(pack2.grade_name), name, _TRUNCATE)

                buf = TEMP_BUFFER(8192, DefineConstants.false)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                buf.write(pack, sizeof(pack))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                buf.write(pack2, sizeof(pack2))

                it = m_memberOnline.begin()
                while it is not self._m_memberOnline.end():
                    d = it.GetDesc()

                    if d:
                        d.Packet(buf.read_peek(), buf.size())
                    it += 1

            if self._m_data.grade_array[grade].auth_flag != auth:
                self._m_data.grade_array[grade].auth_flag = byte(auth)

                pack = packet_guild()
                pack.header = byte(Globals.LG_HEADER_GC_GUILD)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                pack.size = sizeof(pack)
                pack.subheader = byte(Globals.GUILD_SUBLG_HEADER_GC_GRADE_AUTH)

                pack2 = TOneGradeAuthPacket()
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                pack.size+=sizeof(pack2)
                pack2.grade = byte(grade+1)
                pack2.auth = byte(auth)

                buf = TEMP_BUFFER(8192, DefineConstants.false)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                buf.write(pack, sizeof(pack))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                buf.write(pack2, sizeof(pack2))

                it = m_memberOnline.begin()
                while it is not self._m_memberOnline.end():
                    d = it.GetDesc()
                    if d:
                        d.Packet(buf.read_peek(), buf.size())
                    it += 1




    class GuildJoinErrCode(Enum):
        GERR_NONE = 0
        GERR_WITHDRAWPENALTY = 1
        GERR_COMMISSIONPENALTY = 2
        GERR_ALREADYJOIN = 3
        GERR_GUILDISFULL = 4
        GERR_GUILD_IS_IN_WAR = 5
        GERR_INVITE_LIMIT = 6
        GERR_MAX = 7

    def _VerifyGuildJoinableCondition(self, pchInvitee):
        if get_global_time() - pchInvitee.GetQuestFlag("guild_manage.new_withdraw_time") < CGuildManager.instance().GetWithdrawDelay():
            return GuildJoinErrCode.GERR_WITHDRAWPENALTY
        elif get_global_time() - pchInvitee.GetQuestFlag("guild_manage.new_disband_time") < CGuildManager.instance().GetDisbandDelay():
            return GuildJoinErrCode.GERR_COMMISSIONPENALTY
        elif pchInvitee.GetGuild():
            return GuildJoinErrCode.GERR_ALREADYJOIN
        elif self.GetMemberCount() >= self.GetMaxMemberCount():
            #sys_log(1, "GuildName = %s, GetMemberCount() = %d, GetMaxMemberCount() = %d (32 + MAX(level(%d)-10, 0) * 2 + bonus(%d)", self.GetName(), self.GetMemberCount(), self.GetMaxMemberCount(), self._m_data.level, self._m_iMemberCountBonus)
            return GuildJoinErrCode.GERR_GUILDISFULL
        elif self.UnderAnyWar(GUILD_WAR_TYPE_MAX_NUM) != 0:
            return GuildJoinErrCode.GERR_GUILD_IS_IN_WAR

        return GuildJoinErrCode.GERR_NONE

    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The typedef 'EventMap' was defined in multiple preprocessor conditionals and cannot be replaced in-line:


## Laniatus Games Studio Inc. | NOTE: Anonymous namespaces are not defined:
#namespace
class FGuildNameSender:
    def __init__(self, id, guild_name):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.id = 0
        self.name = '\0'
        self.p = packet_guild()

        self.id = id
        self.name = guild_name
        self.p.header = byte(Globals.LG_HEADER_GC_GUILD)
        self.p.subheader = byte(Globals.GUILD_SUBLG_HEADER_GC_GUILD_NAME)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.p.size = sizeof(self.p) + sizeof(uint) + LGEMiscellaneous.GUILD_NAME_MAX_LEN

    def functor_method(self, ch):
        d = ch.GetDesc()

        if d:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            d.BufferedPacket(self.p, sizeof(self.p))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            d.BufferedPacket(self.id, sizeof(self.id))
            d.Packet(self.name, LGEMiscellaneous.GUILD_NAME_MAX_LEN)


## Laniatus Games Studio Inc. | NOTE: Anonymous namespaces are not defined:
#namespace
class FSendChangeGrade:

    def __init__(self, guild_id, grade):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.grade = 0
        self.p = SPacketGuild()

        self.grade = grade
        self.p.dwGuild = guild_id
        self.p.dwInfo = grade

    def functor_method(self):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        db_clientdesc.DBPacket(Globals.LG_HEADER_GD_GUILD_CHANGE_GRADE, 0, self.p, sizeof(self.p))

## Laniatus Games Studio Inc. | NOTE: Anonymous namespaces are not defined:
#namespace
class FGuildChat:

    def __init__(self, c_pszText):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.c_pszText = '\0'

        self.c_pszText = c_pszText

    def functor_method(self, ch):
        ch.ChatPacket(EChatType.CHAT_TYPE_GUILD, "%s", self.c_pszText)


class TInviteGuildEventInfo(event_info_data):

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.dwInviteePID = 0
        self.dwGuildID = 0

        self.dwInviteePID = 0
        self.dwGuildID = 0