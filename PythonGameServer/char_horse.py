def StartRiding():
    if IsDead() == ((not LGEMiscellaneous.DEFINECONSTANTS.false)):
        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You cannot ride while falling."))
        return LGEMiscellaneous.DEFINECONSTANTS.false

    if IsPolymorphed():
        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You cannot ride a Horse as long as you are transformed."))
        return LGEMiscellaneous.DEFINECONSTANTS.false

    armor = GetWear(EWearPositions.WEAR_BODY)

    if armor is not None and (armor.GetVnum() >= 11901 and armor.GetVnum() <= 11904):
        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You cannot ride while wearing a Wedding Robe or a Smoking."))
        return LGEMiscellaneous.DEFINECONSTANTS.false

    dwMountVnum = m_chHorse.GetRaceNum() if m_chHorse else GetMyHorseVnum()

    if LGEMiscellaneous.DEFINECONSTANTS.false == CHorseRider.StartRiding():
        if GetHorseLevel() <= 0:
            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You do not have a Horse."))
        elif GetHorseHealth() <= 0:
            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Your Horse is dead."))
        elif GetHorseStamina() <= 0:
            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("The endurance of your Horse is too low."))

        return LGEMiscellaneous.DEFINECONSTANTS.false

    HorseSummon(LGEMiscellaneous.DEFINECONSTANTS.false)

    MountVnum(dwMountVnum)

    if test_server:
        #sys_log(0, "Ride Horse : %s ", GetName())

    return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

def StopRiding():
    if CHorseRider.StopRiding():
        quest.CQuestManager.instance().Unmount(GetPlayerID())

        if (not IsDead()) and not IsStun():
            dwOldVnum = GetMountVnum()
            MountVnum(0)
            HorseSummon(((not LGEMiscellaneous.DEFINECONSTANTS.false)), LGEMiscellaneous.DEFINECONSTANTS.false, dwOldVnum)
        else:
            m_dwMountVnum = 0
            ComputePoints()
            UpdatePacket()

        PointChange(EPointTypes.LG_POINT_ST, 0)
        PointChange(EPointTypes.LG_POINT_DX, 0)
        PointChange(EPointTypes.LG_POINT_HT, 0)
        PointChange(EPointTypes.LG_POINT_IQ, 0)

        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    return LGEMiscellaneous.DEFINECONSTANTS.false

def SetRider(ch):
    if m_chRider:
        m_chRider.ClearHorseInfo()

    m_chRider = ch

    if m_chRider:
        m_chRider.SendHorseInfo()

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: CHARACTER* CHARACTER::GetRider() const
def GetRider():
    return m_chRider


def HorseSummon(bSummon, bFromFar, dwVnum, pPetName):
    if bSummon:
        if m_chHorse is not None:
            return

        if GetHorseLevel() <= 0:
            return

        if IsRiding():
            return

        #sys_log(0, "HorseSummon : %s lv:%d bSummon:%d fromFar:%d", GetName(), GetLevel(), bSummon, bFromFar)

        x = GetX()
        y = GetY()

        if GetHorseHealth() <= 0:
            bFromFar = LGEMiscellaneous.DEFINECONSTANTS.false

        if bFromFar:
            x += (number(0, 1) * 2 - 1) * number(2000, 2500)
            y += (number(0, 1) * 2 - 1) * number(2000, 2500)
        else:
            x += number(-100, 100)
            y += number(-100, 100)

        m_chHorse = CHARACTER_MANAGER.instance().SpawnMob(GetMyHorseVnum() if (0 == dwVnum) else dwVnum, GetMapIndex(), x, y, GetZ(), LGEMiscellaneous.DEFINECONSTANTS.false, int((GetRotation()+180)), LGEMiscellaneous.DEFINECONSTANTS.false)

        if not m_chHorse:
            ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("Calling the Horse failed."))
            return

        if GetHorseHealth() <= 0:
            m_chHorse.SetPosition(EPositions.POS_DEAD)
            info = AllocEventInfo()
            info.ch = self
            m_chHorse.m_pkDeadEvent = event_create_ex(horse_dead_event, info, ((60) * passes_per_sec))

        m_chHorse.SetLevel(GetHorseLevel())

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to pointers to value types:
#ORIGINAL METINII C CODE: const char* pHorseName = CHorseNameManager::instance().GetHorseName(GetPlayerID());
        pHorseName = CHorseNameManager.instance().GetHorseName(GetPlayerID())

        if pHorseName is not None and len(pHorseName) != 0:
            m_chHorse.m_stName = pHorseName
        else:
            pkMountCostume = GetWear(EWearPositions.WEAR_COSTUME_MOUNT)
            if pkMountCostume:
                pMob = CMobManager.instance().Get(uint(pkMountCostume.GetValue(0)))
                if pMob is None:
                    #lani_err("Cannot find mount_vnum %d for mount_costume %d", pkMountCostume.GetValue(0), pkMountCostume.GetVnum())
                else:
                    m_chHorse.m_stName = GetName()
                    m_chHorse.m_stName += " - "
                    m_chHorse.m_stName += pMob.m_table.szLocaleName

        if len(m_chHorse.m_stName.c_str()) == 0:
            m_chHorse.m_stName = GetName()
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if ! __MULTI_LANGUAGE_SYSTEM__
            m_chHorse.m_stName += LC_TEXT("Horse")
##endif

        if not m_chHorse.Show(GetMapIndex(), x, y, GetZ()):
            CHARACTER_MANAGER.instance().DestroyCharacter(m_chHorse)
            #lani_err("cannot show monster")
            m_chHorse = None
            return

        if (GetHorseHealth() <= 0):
            pack = packet_dead()
            pack.header = byte(LG_HEADER_GC_DEAD)
            pack.vid = m_chHorse.GetVID()
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            PacketAround(pack, sizeof(pack))

        m_chHorse.SetRider(self)
    else:
        if not m_chHorse:
            return

        chHorse = m_chHorse

        chHorse.SetRider(None)

        if not bFromFar:
            CHARACTER_MANAGER.instance().DestroyCharacter(chHorse)
        else:
            chHorse.SetNowWalking(LGEMiscellaneous.DEFINECONSTANTS.false)
            fx = None
            fy = None
            chHorse.SetRotation(GetDegreeFromPositionXY(chHorse.GetX(), chHorse.GetY(), GetX(), GetY())+180)
            GetDeltaByDegree(chHorse.GetRotation(), 3500, fx, fy)
            chHorse.Goto(int((chHorse.GetX()+fx)), int((chHorse.GetY()+fy)))
            chHorse.SendMovePacket(EMoveFuncType.FUNC_WAIT, 0, 0, 0, 0, 0, -1)

        m_chHorse = None

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: uint CHARACTER::GetMyHorseVnum() const
def GetMyHorseVnum():
    delta = 0

    if GetGuild():
        delta += 1

        if GetGuild().GetMasterPID() == GetPlayerID():
            delta += 1

    pkCostumeMount = GetWear(EWearPositions.WEAR_COSTUME_MOUNT)
    if pkCostumeMount:
        return uint(pkCostumeMount.GetValue(0))

    return c_aHorseStat[GetHorseLevel()].iNPCRace + delta

def HorseDie():
    CHorseRider.HorseDie()
    HorseSummon(LGEMiscellaneous.DEFINECONSTANTS.false)

def ReviveHorse():
    if CHorseRider.ReviveHorse():
        HorseSummon(LGEMiscellaneous.DEFINECONSTANTS.false)
        HorseSummon(((not LGEMiscellaneous.DEFINECONSTANTS.false)))
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
    return LGEMiscellaneous.DEFINECONSTANTS.false

def ClearHorseInfo():
    if not IsHorseRiding():
        ChatPacket(EChatType.CHAT_TYPE_COMMAND, "hide_horse_state")

        m_bSendHorseLevel = 0
        m_bSendHorseHealthGrade = 0
        m_bSendHorseStaminaGrade = 0

    m_chHorse = None


def SendHorseInfo():
    if m_chHorse or IsHorseRiding():
        iHealthGrade = None
        iStaminaGrade = None

        if GetHorseHealth() == 0:
            iHealthGrade = 0
        elif GetHorseHealth() * 10 <= GetHorseMaxHealth() * 3:
            iHealthGrade = 1
        elif GetHorseHealth() * 10 <= GetHorseMaxHealth() * 7:
            iHealthGrade = 2
        else:
            iHealthGrade = 3

        if GetHorseStamina() * 10 <= GetHorseMaxStamina():
            iStaminaGrade = 0
        elif GetHorseStamina() * 10 <= GetHorseMaxStamina() * 3:
            iStaminaGrade = 1
        elif GetHorseStamina() * 10 <= GetHorseMaxStamina() * 7:
            iStaminaGrade = 2
        else:
            iStaminaGrade = 3

        if m_bSendHorseLevel != GetHorseLevel() or m_bSendHorseHealthGrade != iHealthGrade or m_bSendHorseStaminaGrade != iStaminaGrade:
            ChatPacket(EChatType.CHAT_TYPE_COMMAND, "horse_state %d %d %d", GetHorseLevel(), iHealthGrade, iStaminaGrade)

            m_bSendHorseLevel = GetHorseLevel()
            m_bSendHorseHealthGrade = iHealthGrade
            m_bSendHorseStaminaGrade = iStaminaGrade

def CanUseHorseSkill():
    if IsRiding():
        if GetHorseGrade() == 3:
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
        else:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if GetMountVnum():
            if GetMountVnum() >= 20209 and GetMountVnum() <= 20212:
                return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

            if CMobVnumHelper.IsRamadanBlackHorse(GetMountVnum()):
                return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
        else:
            return LGEMiscellaneous.DEFINECONSTANTS.false


    return LGEMiscellaneous.DEFINECONSTANTS.false

def SetHorseLevel(iLevel):
    CHorseRider.SetHorseLevel(iLevel)
    SetSkillLevel(LaniatusETalentXes.LG_SKILL_HORSE, GetHorseLevel())

