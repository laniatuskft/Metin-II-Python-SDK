## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: LaniaCAffects * CHARACTER::FindAffect(uint dwType, byte bApply) const
def FindAffect(dwType, bApply):
    it = m_list_pkAffect.begin()

    while it is not m_list_pkAffect.end():
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: LaniaCAffects * pkAffect = *it++;
        pkAffect = *it
        it += 1

        if pkAffect.dwType == dwType and (bApply == EApplyTypes.APPLY_NONE or bApply == pkAffect.bApplyOn):
            return pkAffect

    return None

def UpdateAffect():
    if GetPoint(EPointTypes.LG_POINT_HP_RECOVERY) > 0:
        if GetMaxHP() <= GetHP():
            PointChange(EPointTypes.LG_POINT_HP_RECOVERY, -GetPoint(EPointTypes.LG_POINT_HP_RECOVERY))
        else:
            iVal = 0

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
            iVal = MIN(GetPoint(EPointTypes.LG_POINT_HP_RECOVERY), GetMaxHP() * 7 / 100)

            PointChange(EPointTypes.LG_POINT_HP, iVal)
            PointChange(EPointTypes.LG_POINT_HP_RECOVERY, -iVal)

    if GetPoint(EPointTypes.LG_POINT_SP_RECOVERY) > 0:
        if GetMaxSP() <= GetSP():
            PointChange(EPointTypes.LG_POINT_SP_RECOVERY, -GetPoint(EPointTypes.LG_POINT_SP_RECOVERY))
        else:
            iVal = None
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
            iVal = MIN(GetPoint(EPointTypes.LG_POINT_SP_RECOVERY), GetMaxSP() * 7 / 100)

            PointChange(EPointTypes.LG_POINT_SP, iVal)
            PointChange(EPointTypes.LG_POINT_SP_RECOVERY, -iVal)

    if GetPoint(EPointTypes.LG_POINT_HP_RECOVER_CONTINUE) > 0:
        PointChange(EPointTypes.LG_POINT_HP, GetPoint(EPointTypes.LG_POINT_HP_RECOVER_CONTINUE))

    if GetPoint(EPointTypes.LG_POINT_SP_RECOVER_CONTINUE) > 0:
        PointChange(EPointTypes.LG_POINT_SP, GetPoint(EPointTypes.LG_POINT_SP_RECOVER_CONTINUE))

    AutoRecoveryItemProcess(LaniatusEAffectTypes.LANIA_AFFECT_AUTO_HP_RECOVERY)
    AutoRecoveryItemProcess(LaniatusEAffectTypes.LANIA_AFFECT_AUTO_SP_RECOVERY)

    if GetMaxStamina() > GetStamina():
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        iSec = (get_dword_time() - GetStopTime()) / 3000
        if iSec != 0:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
            PointChange(EPointTypes.LG_POINT_STAMINA, GetMaxStamina()/1)

    if ProcessAffect():
        if GetPoint(EPointTypes.LG_POINT_HP_RECOVERY) == 0 and GetPoint(EPointTypes.LG_POINT_SP_RECOVERY) == 0 and GetStamina() == GetMaxStamina():
            m_pkAffectEvent = None
            return LGEMiscellaneous.DEFINECONSTANTS.false

    return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

def StartAffectEvent():
    if m_pkAffectEvent:
        return

    info = AllocEventInfo()
    info.ch = self
    m_pkAffectEvent = event_create_ex(affect_event, info, passes_per_sec)
    #sys_log(1, "StartAffectEvent %s %p %p", GetName(), self, get_pointer(m_pkAffectEvent))

def ClearAffect(bSave):
    afOld = m_afAffectFlag
    wMovSpd = ushort(GetPoint(EPointTypes.LG_POINT_MOV_SPEED))
    wAttSpd = ushort(GetPoint(EPointTypes.LG_POINT_ATT_SPEED))

    it = m_list_pkAffect.begin()

    while it is not m_list_pkAffect.end():
        pkAff = *it

        if bSave:
            if ((pkAff.dwType) == LaniatusEAffectTypes.LANIA_AFFECT_BLOCK_CHAT or ((pkAff.dwType) >= 500 and (pkAff.dwType) < 600)) or ((pkAff.dwType) == LaniatusEAffectTypes.LANIA_AFFECT_WAR_FLAG or (pkAff.dwType) == LaniatusEAffectTypes.LANIA_AFFECT_REVIVE_INVISIBLE or ((pkAff.dwType) >= LaniatusEAffectTypes.LANIA_AFFECT_PREMIUM_START and (pkAff.dwType) <= LaniatusEAffectTypes.LANIA_AFFECT_PREMIUM_END)):
                it += 1
                continue

            if IsPC():
                SendAffectRemovePacket(GetDesc(), GetPlayerID(), pkAff.dwType, pkAff.bApplyOn)

        ComputeAffect(pkAff, LGEMiscellaneous.DEFINECONSTANTS.false)

        it = m_list_pkAffect.erase(it)
        LaniaCAffects.Release(pkAff)

    if afOld is not m_afAffectFlag or wMovSpd != GetPoint(EPointTypes.LG_POINT_MOV_SPEED) or wAttSpd != GetPoint(EPointTypes.LG_POINT_ATT_SPEED):
        UpdatePacket()

    CheckMaximumPoints()

    if m_list_pkAffect.empty():
        event_cancel(m_pkAffectEvent)

def ProcessAffect():
    bDiff = LGEMiscellaneous.DEFINECONSTANTS.false
    pkAff = None

    LaniatusDefVariables = 0
    while LaniatusDefVariables <= EPremiumTypes.PREMIUM_MAX_NUM:
        aff_idx = LaniatusDefVariables + int(LaniatusEAffectTypes.LANIA_AFFECT_PREMIUM_START)

        pkAff = FindAffect(aff_idx)

        if pkAff is None:
            continue

        remain = GetPremiumRemainSeconds(i)

        if remain < 0:
            RemoveAffect(aff_idx)
            bDiff = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
        else:
            pkAff.lDuration = remain + 1
        LaniatusDefVariables += 1

    pkAff = FindAffect(LaniatusEAffectTypes.LANIA_AFFECT_HAIR)
    if pkAff:
        if self.GetQuestFlag("hair.limit_time") < get_global_time():
            self.SetPart(EParts.PART_HAIR, 0)
            RemoveAffect(LaniatusEAffectTypes.LANIA_AFFECT_HAIR)
        else:
            ++(pkAff.lDuration)

    CHorseNameManager.instance().Validate(self)

    afOld = m_afAffectFlag
    lMovSpd = GetPoint(EPointTypes.LG_POINT_MOV_SPEED)
    lAttSpd = GetPoint(EPointTypes.LG_POINT_ATT_SPEED)
    it = m_list_pkAffect.begin()

    while it is not m_list_pkAffect.end():
        pkAff = *it

        bEnd = LGEMiscellaneous.DEFINECONSTANTS.false

        if pkAff.dwType >= LaniatusETalentXes.GUILD_LG_SKILL_START and pkAff.dwType <= LaniatusETalentXes.GUILD_LG_SKILL_END:
            if (not GetGuild()) or not GetGuild().UnderAnyWar():
                bEnd = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        if pkAff.lSPCost > 0:
            if GetSP() < pkAff.lSPCost:
                bEnd = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
            else:
                PointChange(EPointTypes.LG_POINT_SP, -pkAff.lSPCost)

        pkAff.lDuration -= 1
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: if (--pkAff->lDuration <= 0)
        if pkAff.lDuration <= 0:
            bEnd = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        if bEnd:
            it = m_list_pkAffect.erase(it)
            ComputeAffect(pkAff, LGEMiscellaneous.DEFINECONSTANTS.false)
            bDiff = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
            if IsPC():
                SendAffectRemovePacket(GetDesc(), GetPlayerID(), pkAff.dwType, pkAff.bApplyOn)

            LaniaCAffects.Release(pkAff)

            continue

        it += 1

    if bDiff:
        if afOld is not m_afAffectFlag or lMovSpd != GetPoint(EPointTypes.LG_POINT_MOV_SPEED) or lAttSpd != GetPoint(EPointTypes.LG_POINT_ATT_SPEED):
            UpdatePacket()

        CheckMaximumPoints()

    if m_list_pkAffect.empty():
        return 1 if ((not LGEMiscellaneous.DEFINECONSTANTS.false)) else 0

    return LGEMiscellaneous.DEFINECONSTANTS.false

def SaveAffect():
    p = SPacketGDAddAffect()

    it = m_list_pkAffect.begin()

    while it is not m_list_pkAffect.end():
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: LaniaCAffects * pkAff = *it++;
        pkAff = *it
        it += 1

        if ((pkAff.dwType) == LaniatusEAffectTypes.LANIA_AFFECT_WAR_FLAG or (pkAff.dwType) == LaniatusEAffectTypes.LANIA_AFFECT_REVIVE_INVISIBLE or ((pkAff.dwType) >= LaniatusEAffectTypes.LANIA_AFFECT_PREMIUM_START and (pkAff.dwType) <= LaniatusEAffectTypes.LANIA_AFFECT_PREMIUM_END)):
            continue

        #sys_log(1, "LANIA_AFFECT_SAVE: %u %u %d %d", pkAff.dwType, pkAff.bApplyOn, pkAff.lApplyValue, pkAff.lDuration)

        p.dwPID = GetPlayerID()
        p.elem.dwType = pkAff.dwType
        p.elem.bApplyOn = pkAff.bApplyOn
        p.elem.lApplyValue = pkAff.lApplyValue
        p.elem.dwFlag = pkAff.dwFlag
        p.elem.lDuration = pkAff.lDuration
        p.elem.lSPCost = pkAff.lSPCost
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        db_clientdesc.DBPacket(LG_HEADER_GD_ADD_AFFECT, 0, p, sizeof(p))

class load_affect_login_event_info(event_info_data):

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.pid = 0
        self.count = 0
        self.data = '\0'

        self.pid = 0
        self.count = 0
        self.data = 0

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Pointer arithmetic is detected on the parameter 'pElements':
#ORIGINAL METINII C CODE: void CHARACTER::LoadAffect(uint dwCount, TPacketAffectElement * pElements)
def LoadAffect(dwCount, pElements):
    m_bIsLoadedAffect = LGEMiscellaneous.DEFINECONSTANTS.false

    if not GetDesc().IsPhase(EPhase.PHASE_GAME):
        if test_server:
            #sys_log(0, "LOAD_AFFECT: Creating Event", GetName(), dwCount)

        info = AllocEventInfo()

        info.pid = GetPlayerID()
        info.count = dwCount
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        info.data = LG_NEW_M2 char[sizeof(TPacketAffectElement) * dwCount]
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memcpy' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memcpy(info.data, pElements, sizeof(TPacketAffectElement) * dwCount)

        event_create_ex(load_affect_login_event, info, ((1) * passes_per_sec))

        return

    ClearAffect(((not LGEMiscellaneous.DEFINECONSTANTS.false)))

    if test_server:
        #sys_log(0, "LOAD_AFFECT: %s count %d", GetName(), dwCount)

    afOld = m_afAffectFlag

    lMovSpd = GetPoint(EPointTypes.LG_POINT_MOV_SPEED)
    lAttSpd = GetPoint(EPointTypes.LG_POINT_ATT_SPEED)

    LaniatusDefVariables = 0
    while LaniatusDefVariables < dwCount:
        if pElements.dwType == LaniatusETalentXes.LG_SKILL_MUYEONG:
            continue

        if LaniatusEAffectTypes.LANIA_AFFECT_AUTO_HP_RECOVERY == pElements.dwType or LaniatusEAffectTypes.LANIA_AFFECT_AUTO_SP_RECOVERY == pElements.dwType:
            item = FindItemByID(pElements.dwFlag)

            if None is item:
                continue

            item.Lock(((not LGEMiscellaneous.DEFINECONSTANTS.false)))

        if pElements.bApplyOn >= LGEMiscellaneous.LG_POINT_MAX_NUM:
            #lani_err("invalid affect data %s ApplyOn %u ApplyValue %d", GetName(), pElements.bApplyOn, pElements.lApplyValue)
            continue

        if test_server:
            #sys_log(0, "Load Affect : Affect %s %d %d", GetName(), pElements.dwType, pElements.bApplyOn)

        pkAff = LaniaCAffects.Acquire()
        m_list_pkAffect.push_back(pkAff)

        pkAff.dwType = pElements.dwType
        pkAff.bApplyOn = pElements.bApplyOn
        pkAff.lApplyValue = pElements.lApplyValue
        pkAff.dwFlag = pElements.dwFlag
        pkAff.lDuration = pElements.lDuration
        pkAff.lSPCost = pElements.lSPCost

        SendAffectAddPacket(GetDesc(), pkAff)

        ComputeAffect(pkAff, ((not LGEMiscellaneous.DEFINECONSTANTS.false)))


        LaniatusDefVariables += 1
        pElements += 1

    if afOld is not m_afAffectFlag or lMovSpd != GetPoint(EPointTypes.LG_POINT_MOV_SPEED) or lAttSpd != GetPoint(EPointTypes.LG_POINT_ATT_SPEED):
        UpdatePacket()

    StartAffectEvent()
    m_bIsLoadedAffect = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
    DragonSoul_Initialize()

def AddAffect(dwType, bApplyOn, lApplyValue, dwFlag, lDuration, lSPCost, bOverride, IsCube):
    if dwType == LaniatusEAffectTypes.LANIA_AFFECT_BLOCK_CHAT and lDuration > 1:
        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Your chat was blocked by a GM."))

    if lDuration == 0:
        #lani_err("Character::AddAffect lDuration == 0 type %d", lDuration, dwType)
        lDuration = 1

    pkAff = None

    if IsCube:
        pkAff = FindAffect(dwType,bApplyOn)
    else:
        pkAff = FindAffect(dwType)

    if dwFlag == EAffectBits.AFF_STUN:
        if m_posDest.x != GetX() or m_posDest.y != GetY():
            m_posDest.x = m_posStart.x = GetX()
            m_posDest.y = m_posStart.y = GetY()
            battle_end(self)

            SyncPacket()

    if pkAff is not None and bOverride:
        ComputeAffect(pkAff, LGEMiscellaneous.DEFINECONSTANTS.false)

        if GetDesc():
            SendAffectRemovePacket(GetDesc(), GetPlayerID(), pkAff.dwType, pkAff.bApplyOn)
    else:
        pkAff = LaniaCAffects.Acquire()
        m_list_pkAffect.push_back(pkAff)


    #sys_log(1, "AddAffect %s type %d apply %d %d flag %u duration %d", GetName(), dwType, bApplyOn, lApplyValue, dwFlag, lDuration)
    #sys_log(0, "AddAffect %s type %d apply %d %d flag %u duration %d", GetName(), dwType, bApplyOn, lApplyValue, dwFlag, lDuration)

    pkAff.dwType = dwType
    pkAff.bApplyOn = bApplyOn
    pkAff.lApplyValue = lApplyValue
    pkAff.dwFlag = dwFlag
    pkAff.lDuration = lDuration
    pkAff.lSPCost = lSPCost

    wMovSpd = ushort(GetPoint(EPointTypes.LG_POINT_MOV_SPEED))
    wAttSpd = ushort(GetPoint(EPointTypes.LG_POINT_ATT_SPEED))

    ComputeAffect(pkAff, ((not LGEMiscellaneous.DEFINECONSTANTS.false)))

    if pkAff.dwFlag != 0 or wMovSpd != GetPoint(EPointTypes.LG_POINT_MOV_SPEED) or wAttSpd != GetPoint(EPointTypes.LG_POINT_ATT_SPEED):
        UpdatePacket()

    StartAffectEvent()

    if IsPC():
        SendAffectAddPacket(GetDesc(), pkAff)

        if ((pkAff.dwType) == LaniatusEAffectTypes.LANIA_AFFECT_WAR_FLAG or (pkAff.dwType) == LaniatusEAffectTypes.LANIA_AFFECT_REVIVE_INVISIBLE or ((pkAff.dwType) >= LaniatusEAffectTypes.LANIA_AFFECT_PREMIUM_START and (pkAff.dwType) <= LaniatusEAffectTypes.LANIA_AFFECT_PREMIUM_END)):
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        p = SPacketGDAddAffect()
        p.dwPID = GetPlayerID()
        p.elem.dwType = pkAff.dwType
        p.elem.bApplyOn = pkAff.bApplyOn
        p.elem.lApplyValue = pkAff.lApplyValue
        p.elem.dwFlag = pkAff.dwFlag
        p.elem.lDuration = pkAff.lDuration
        p.elem.lSPCost = pkAff.lSPCost
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        db_clientdesc.DBPacket(LG_HEADER_GD_ADD_AFFECT, 0, p, sizeof(p))

    return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

def RefreshAffect():
    it = m_list_pkAffect.begin()

    while it is not m_list_pkAffect.end():
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: LaniaCAffects * pkAff = *it++;
        pkAff = *it
        it += 1
        ComputeAffect(pkAff, ((not LGEMiscellaneous.DEFINECONSTANTS.false)))

def ComputeAffect(pkAff, bAdd):
    if bAdd and pkAff.dwType >= LaniatusETalentXes.GUILD_LG_SKILL_START and pkAff.dwType <= LaniatusETalentXes.GUILD_LG_SKILL_END:
        if not GetGuild():
            return

        if not GetGuild().UnderAnyWar():
            return

    if pkAff.dwFlag != 0:
        if not bAdd:
            m_afAffectFlag.Reset(pkAff.dwFlag)
        else:
            m_afAffectFlag.Set(pkAff.dwFlag)

    if bAdd:
        PointChange(pkAff.bApplyOn, pkAff.lApplyValue)
    else:
        PointChange(pkAff.bApplyOn, -pkAff.lApplyValue)

    if pkAff.dwType == LaniatusETalentXes.LG_SKILL_MUYEONG:
        if bAdd:
            StartMuyeongEvent()
        else:
            StopMuyeongEvent()

def RemoveAffect(pkAff):
    if pkAff is None:
        return LGEMiscellaneous.DEFINECONSTANTS.false

    m_list_pkAffect.remove(pkAff)
    ComputeAffect(pkAff, LGEMiscellaneous.DEFINECONSTANTS.false)

    if LaniatusEAffectTypes.LANIA_AFFECT_REVIVE_INVISIBLE != pkAff.dwType:
        ComputePoints()
    else:
        UpdatePacket()
    CheckMaximumPoints()

    if test_server:
        #sys_log(0, "LANIA_AFFECT_REMOVE: %s (flag %u apply: %u)", GetName(), pkAff.dwFlag, pkAff.bApplyOn)

    if IsPC():
        SendAffectRemovePacket(GetDesc(), GetPlayerID(), pkAff.dwType, pkAff.bApplyOn)

    LaniaCAffects.Release(pkAff)
    return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

def RemoveAffect(dwType):
    if dwType == LaniatusEAffectTypes.LANIA_AFFECT_BLOCK_CHAT:
        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Your chat block is lifted."))

    flag = LGEMiscellaneous.DEFINECONSTANTS.false

    pkAff = None

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: while ((pkAff = FindAffect(dwType)))
    while (pkAff = FindAffect(dwType)):
        RemoveAffect(pkAff)
        flag = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    return flag

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: bool CHARACTER::IsAffectFlag(uint dwAff) const
def IsAffectFlag(dwAff):
    return m_afAffectFlag.IsSet(dwAff)

def RemoveGoodAffect():
    RemoveAffect(LaniatusEAffectTypes.LANIA_AFFECT_MOV_SPEED)
    RemoveAffect(LaniatusEAffectTypes.LANIA_AFFECT_ATT_SPEED)
    RemoveAffect(LaniatusEAffectTypes.LANIA_AFFECT_STR)
    RemoveAffect(LaniatusEAffectTypes.LANIA_AFFECT_DEX)
    RemoveAffect(LaniatusEAffectTypes.LANIA_AFFECT_INT)
    RemoveAffect(LaniatusEAffectTypes.LANIA_AFFECT_CON)
    RemoveAffect(LaniatusEAffectTypes.LANIA_AFFECT_CHINA_FIREWORK)

    RemoveAffect(LaniatusETalentXes.LG_SKILL_JEONGWI)
    RemoveAffect(LaniatusETalentXes.LG_SKILL_GEOMKYUNG)
    RemoveAffect(LaniatusETalentXes.LG_SKILL_CHUNKEON)
    RemoveAffect(LaniatusETalentXes.LG_SKILL_EUNHYUNG)
    RemoveAffect(LaniatusETalentXes.LG_SKILL_GYEONGGONG)
    RemoveAffect(LaniatusETalentXes.LG_SKILL_GWIGEOM)
    RemoveAffect(LaniatusETalentXes.LG_SKILL_TERROR)
    RemoveAffect(LaniatusETalentXes.LG_SKILL_JUMAGAP)
    RemoveAffect(LaniatusETalentXes.LG_SKILL_MANASHILED)
    RemoveAffect(LaniatusETalentXes.LG_SKILL_HOSIN)
    RemoveAffect(LaniatusETalentXes.LG_SKILL_REFLECT)
    RemoveAffect(LaniatusETalentXes.LG_SKILL_KWAESOK)
    RemoveAffect(LaniatusETalentXes.LG_SKILL_JEUNGRYEOK)
    RemoveAffect(LaniatusETalentXes.LG_SKILL_GICHEON)

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: bool CHARACTER::IsGoodAffect(byte bAffectType) const
def IsGoodAffect(bAffectType):

    if (bAffectType == (LaniatusEAffectTypes.LANIA_AFFECT_MOV_SPEED)) or (bAffectType == (LaniatusEAffectTypes.LANIA_AFFECT_ATT_SPEED)) or (bAffectType == (LaniatusEAffectTypes.LANIA_AFFECT_STR)) or (bAffectType == (LaniatusEAffectTypes.LANIA_AFFECT_DEX)) or (bAffectType == (LaniatusEAffectTypes.LANIA_AFFECT_INT)) or (bAffectType == (LaniatusEAffectTypes.LANIA_AFFECT_CON)) or (bAffectType == (LaniatusEAffectTypes.LANIA_AFFECT_CHINA_FIREWORK)) or (bAffectType == (LaniatusETalentXes.LG_SKILL_JEONGWI)) or (bAffectType == (LaniatusETalentXes.LG_SKILL_GEOMKYUNG)) or (bAffectType == (LaniatusETalentXes.LG_SKILL_CHUNKEON)) or (bAffectType == (LaniatusETalentXes.LG_SKILL_EUNHYUNG)) or (bAffectType == (LaniatusETalentXes.LG_SKILL_GYEONGGONG)) or (bAffectType == (LaniatusETalentXes.LG_SKILL_GWIGEOM)) or (bAffectType == (LaniatusETalentXes.LG_SKILL_TERROR)) or (bAffectType == (LaniatusETalentXes.LG_SKILL_JUMAGAP)) or (bAffectType == (LaniatusETalentXes.LG_SKILL_MANASHILED)) or (bAffectType == (LaniatusETalentXes.LG_SKILL_HOSIN)) or (bAffectType == (LaniatusETalentXes.LG_SKILL_REFLECT)) or (bAffectType == (LaniatusETalentXes.LG_SKILL_KWAESOK)) or (bAffectType == (LaniatusETalentXes.LG_SKILL_JEUNGRYEOK)) or (bAffectType == (LaniatusETalentXes.LG_SKILL_GICHEON)):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if ENABLE_WOLFMAN
    if (bAffectType == (LaniatusEAffectTypes.LANIA_AFFECT_MOV_SPEED)) or (bAffectType == (LaniatusEAffectTypes.LANIA_AFFECT_ATT_SPEED)) or (bAffectType == (LaniatusEAffectTypes.LANIA_AFFECT_STR)) or (bAffectType == (LaniatusEAffectTypes.LANIA_AFFECT_DEX)) or (bAffectType == (LaniatusEAffectTypes.LANIA_AFFECT_INT)) or (bAffectType == (LaniatusEAffectTypes.LANIA_AFFECT_CON)) or (bAffectType == (LaniatusEAffectTypes.LANIA_AFFECT_CHINA_FIREWORK)) or (bAffectType == (LaniatusETalentXes.LG_SKILL_JEONGWI)) or (bAffectType == (LaniatusETalentXes.LG_SKILL_GEOMKYUNG)) or (bAffectType == (LaniatusETalentXes.LG_SKILL_CHUNKEON)) or (bAffectType == (LaniatusETalentXes.LG_SKILL_EUNHYUNG)) or (bAffectType == (LaniatusETalentXes.LG_SKILL_GYEONGGONG)) or (bAffectType == (LaniatusETalentXes.LG_SKILL_GWIGEOM)) or (bAffectType == (LaniatusETalentXes.LG_SKILL_TERROR)) or (bAffectType == (LaniatusETalentXes.LG_SKILL_JUMAGAP)) or (bAffectType == (LaniatusETalentXes.LG_SKILL_MANASHILED)) or (bAffectType == (LaniatusETalentXes.LG_SKILL_HOSIN)) or (bAffectType == (LaniatusETalentXes.LG_SKILL_REFLECT)) or (bAffectType == (LaniatusETalentXes.LG_SKILL_KWAESOK)) or (bAffectType == (LaniatusETalentXes.LG_SKILL_JEUNGRYEOK)) or (bAffectType == (LaniatusETalentXes.LG_SKILL_GICHEON)) or (bAffectType == (LaniatusETalentXes.LG_SKILL_JEOKRANG)) or (bAffectType == (LaniatusETalentXes.LG_SKILL_CHEONGRANG)):
##endif
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
    return LGEMiscellaneous.DEFINECONSTANTS.false

def RemoveBadAffect():
    #sys_log(0, "RemoveBadAffect %s", GetName())

    RemovePoison()
    RemoveFire()
    RemoveAffect(LaniatusEAffectTypes.LANIA_AFFECT_STUN)
    RemoveAffect(LaniatusEAffectTypes.LANIA_AFFECT_SLOW)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if ENABLE_WOLFMAN
    RemoveAffect(LaniatusEAffectTypes.LANIA_AFFECT_BLEEDING)
##endif
    RemoveAffect(LaniatusETalentXes.LG_SKILL_TUSOK)


