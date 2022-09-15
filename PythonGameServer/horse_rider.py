import math

class THorseStat:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.iMinLevel = 0
        self.iNPCRace = 0
        self.iMaxHealth = 0
        self.iMaxStamina = 0
        self.iST = 0
        self.iDX = 0
        self.iHT = 0
        self.iIQ = 0
        self.iDamMean = 0
        self.iDamMin = 0
        self.iDamMax = 0
        self.iArmor = 0


class CHorseRider:
    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self._m_Horse = THorseInfo()
        self._m_eventStaminaRegen = _boost_func_of_void.intrusive_ptr()
        self._m_eventStaminaConsume = _boost_func_of_void.intrusive_ptr()

        self._Initialize()

    def close(self):
        self._Destroy()

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: byte GetHorseLevel() const
    def GetHorseLevel(self):
        return self._m_Horse.bLevel
    def GetHorseGrade(self):
        grade = 0

        if self.GetHorseLevel() != 0:
            grade = math.trunc((self.GetHorseLevel() - 1) / float(10)) + 1

        return grade

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: short GetHorseHealth() const
    def GetHorseHealth(self):
        return self._m_Horse.sHealth
## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: short GetHorseStamina() const
    def GetHorseStamina(self):
        return self._m_Horse.sStamina
    def GetHorseMaxHealth(self):
        level = self.GetHorseLevel()
        return short(Globals.c_aHorseStat[level].iMaxHealth)

    def GetHorseMaxStamina(self):
        level = self.GetHorseLevel()
        return short(Globals.c_aHorseStat[level].iMaxStamina)

    def GetHorseST(self):
        return Globals.c_aHorseStat[self.GetHorseLevel()].iST
    def GetHorseDX(self):
        return Globals.c_aHorseStat[self.GetHorseLevel()].iDX
    def GetHorseHT(self):
        return Globals.c_aHorseStat[self.GetHorseLevel()].iHT
    def GetHorseIQ(self):
        return Globals.c_aHorseStat[self.GetHorseLevel()].iIQ
    def GetHorseArmor(self):
        return Globals.c_aHorseStat[self.GetHorseLevel()].iArmor
    def ReviveHorse(self):
        if self.GetHorseLevel() <= 0:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if self.GetHorseHealth()>0:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        level = self.GetHorseLevel()
        self._m_Horse.sHealth = short(Globals.c_aHorseStat[level].iMaxHealth)
        self._m_Horse.sStamina = short(Globals.c_aHorseStat[level].iMaxStamina)

        self.ResetHorseHealthDropTime()
        self._StartStaminaRegenEvent()
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def FeedHorse(self):
        if self.GetHorseLevel() > 0 and self.GetHorseHealth() > 0:
            self._UpdateHorseHealth(+1, ((not DefineConstants.false)))
            self.ResetHorseHealthDropTime()

    def HorseDie(self):
        #sys_log(0, "HORSE DIE %p %p", Globals.get_pointer(self._m_eventStaminaRegen), Globals.get_pointer(self._m_eventStaminaConsume))
        self._UpdateHorseStamina(-self._m_Horse.sStamina, ((not DefineConstants.false)))
        event_cancel(self._m_eventStaminaRegen)
        event_cancel(self._m_eventStaminaConsume)

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: bool IsHorseRiding() const
    def IsHorseRiding(self):
        return self._m_Horse.bRiding != 0
    def ResetHorseHealthDropTime(self):
        self._m_Horse.dwHorseHealthDropTime = get_global_time() + Globals.HORSE_HEALTH_DROP_INTERVAL

    def SetHorseLevel(self, iLevel):
        self._m_Horse.bLevel = byte(iLevel) = MINMAX(0, iLevel, Globals.HORSE_MAX_LEVEL)

        self._m_Horse.sStamina = short(Globals.c_aHorseStat[iLevel].iMaxStamina)
        self._m_Horse.sHealth = short(Globals.c_aHorseStat[iLevel].iMaxHealth)
        self._m_Horse.dwHorseHealthDropTime = 0

        self.ResetHorseHealthDropTime()

        self.SendHorseInfo()

    def EnterHorse(self):
        if self.GetHorseLevel() <= 0:
            return

        if self.GetHorseHealth() <= 0:
            return

        if self.IsHorseRiding():
            self._m_Horse.bRiding = 1 if self._m_Horse.bRiding == 0 else 0
            self.StartRiding()
        else:
            self._StartStaminaRegenEvent()
        self._CheckHorseHealthDropTime(LGEMiscellaneous.DEFINECONSTANTS.false)

    def SendHorseInfo(self):
        pass
    def ClearHorseInfo(self):
        pass
    def UpdateRideTime(self, interval):
        pass

    def SetHorseData(self, crInfo):
## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: m_Horse = crInfo;
        self._m_Horse.copy_from(crInfo)

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: const THorseInfo& GetHorseData() const
    def GetHorseData(self):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
#ORIGINAL METINII C CODE: return m_Horse;
        return THorseInfo(self._m_Horse)
    def UpdateHorseDataByLogoff(self, dwLogoffTime):
        if self.GetHorseLevel() <= 0:
            return

        if dwLogoffTime >= 12 * 60:
            self._UpdateHorseStamina(math.trunc(dwLogoffTime / float(math.trunc(12 / float(60)))), LGEMiscellaneous.DEFINECONSTANTS.false)

    def StartRiding(self):
        if self._m_Horse.bRiding != 0:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if self.GetHorseLevel() <= 0:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if self.GetHorseHealth() <= 0:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if self.GetHorseStamina() <= 0:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        self._m_Horse.bRiding = 1 if ((not LGEMiscellaneous.DEFINECONSTANTS.false)) else 0
        self._StartStaminaConsumeEvent()
        self.SendHorseInfo()
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def StopRiding(self):
        if self._m_Horse.bRiding == 0:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        self._m_Horse.bRiding = LGEMiscellaneous.DEFINECONSTANTS.false
        self._StartStaminaRegenEvent()
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: virtual uint GetMyHorseVnum() const
    def GetMyHorseVnum(self):
        return 20030

    def _UpdateHorseStamina(self, iStamina, bSend = (!LGEMiscellaneous.DefineConstants.false)):
        level = self.GetHorseLevel()

        self._m_Horse.sStamina = MINMAX(0, self._m_Horse.sStamina + iStamina, Globals.c_aHorseStat[level].iMaxStamina)

        if self.GetHorseStamina() == 0 and self.IsHorseRiding():
            self.StopRiding()

        if bSend:
            self.SendHorseInfo()

    def _StartStaminaConsumeEvent(self):
        if self.GetHorseLevel() <= 0:
            return

        if self.GetHorseHealth() <= 0:
            return

        #sys_log(0,"HORSE STAMINA REGEN EVENT CANCEL %p", Globals.get_pointer(self._m_eventStaminaRegen))
        event_cancel(self._m_eventStaminaRegen)

        if self._m_eventStaminaConsume:
            return

        info = Globals.AllocEventInfo()

        info.hr = self
        self._m_eventStaminaConsume = event_create_ex(horse_stamina_consume_event, info, ((Globals.HORSE_STAMINA_CONSUME_INTERVAL) * passes_per_sec))
        #sys_log(0,"HORSE STAMINA CONSUME EVENT CREATE %p", Globals.get_pointer(self._m_eventStaminaConsume))

    def _StartStaminaRegenEvent(self):
        if self.GetHorseLevel() <= 0:
            return

        if self.GetHorseHealth() <= 0:
            return

        #sys_log(0,"HORSE STAMINA CONSUME EVENT CANCEL %p", Globals.get_pointer(self._m_eventStaminaConsume))
        event_cancel(self._m_eventStaminaConsume)

        if self._m_eventStaminaRegen:
            return

        info = Globals.AllocEventInfo()

        info.hr = self
        self._m_eventStaminaRegen = event_create_ex(horse_stamina_regen_event, info, ((Globals.HORSE_STAMINA_REGEN_INTERVAL) * passes_per_sec))
        #sys_log(0,"HORSE STAMINA REGEN EVENT CREATE %p", Globals.get_pointer(self._m_eventStaminaRegen))

    def _UpdateHorseHealth(self, iHealth, bSend = (!LGEMiscellaneous.DefineConstants.false)):
        level = self.GetHorseLevel()

        self._m_Horse.sHealth = MINMAX(0, self._m_Horse.sHealth + iHealth, Globals.c_aHorseStat[level].iMaxHealth)

        if level != 0 and self._m_Horse.sHealth == 0:
            self.HorseDie()

        if bSend:
            self.SendHorseInfo()

    def _CheckHorseHealthDropTime(self, bSend = (!LGEMiscellaneous.DefineConstants.false)):
        now = get_global_time()

        while self._m_Horse.dwHorseHealthDropTime < now:
            self._m_Horse.dwHorseHealthDropTime += uint(Globals.HORSE_HEALTH_DROP_INTERVAL)
            self._UpdateHorseHealth(-1, bSend)

    def _Initialize(self):
        self._m_eventStaminaRegen = None
        self._m_eventStaminaConsume = None
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memset(self._m_Horse, 0, sizeof(self._m_Horse))

    def _Destroy(self):
        event_cancel(self._m_eventStaminaRegen)
        event_cancel(self._m_eventStaminaConsume)


## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python has no concept of a 'friend' function:
#ORIGINAL METINII C CODE: friend int(horse_stamina_regen_event)(_boost_func_of_void::intrusive_ptr<struct event> event, int processing_time);
    int(horse_stamina_regen_event)(_boost_func_of_void.intrusive_ptr<struct event> event, int processing_time)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python has no concept of a 'friend' function:
#ORIGINAL METINII C CODE: friend int(horse_stamina_consume_event)(_boost_func_of_void::intrusive_ptr<struct event> event, int processing_time);
    int(horse_stamina_consume_event)(_boost_func_of_void.intrusive_ptr<struct event> event, int processing_time)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python has no concept of a 'friend' function:
#ORIGINAL METINII C CODE: friend void(do_horse_set_stat)(CHARACTER* ch, const char *argument, int cmd, int subcmd);
    void(do_horse_set_stat)(CHARACTER* ch, const char *argument, int cmd, int subcmd)

class horserider_info(event_info_data):

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.hr = None

        self.hr = None