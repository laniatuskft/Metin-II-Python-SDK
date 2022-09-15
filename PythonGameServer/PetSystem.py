from enum import Enum
import math

## Laniatus Games Studio Inc. | NOTE: Python has no need of forward class declarations:
#class CHARACTER

class SPetAbility:
    pass

class CPetActor:
    class EPetOptions(Enum):
        EPETOPTION_FOLLOWABLE = 1 << 0
        EPETOPTION_MOUNTABLE = 1 << 1
        EPETOPTION_SUMMONABLE = 1 << 2
        EPETOPTION_COMBATABLE = 1 << 3


## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python has no concept of a 'friend' class:
#    friend class CPetSystem

    def __init__(self, owner, vnum, options = EPetOptions.EPetOption_Followable | EPetOptions.EPetOption_Summonable):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self._m_dwVnum = 0
        self._m_dwVID = 0
        self._m_dwOptions = 0
        self._m_dwLastActionTime = 0
        self._m_dwSummonItemVID = 0
        self._m_dwSummonItemVnum = 0
        self._m_originalMoveSpeed = 0
        self._m_name = ""
        self._m_pkChar = None
        self._m_pkOwner = None

        self._m_dwVnum = vnum
        self._m_dwVID = 0
        self._m_dwOptions = options
        self._m_dwLastActionTime = 0

        self._m_pkChar = None
        self._m_pkOwner = owner

        self._m_originalMoveSpeed = 0

        self._m_dwSummonItemVID = 0
        self._m_dwSummonItemVnum = 0

    def close(self):
        self.Unsummon()

        self._m_pkOwner = None

    def Update(self, deltaTime):
        bResult = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        if self._m_pkOwner.IsDead() or (self.IsSummoned() and self._m_pkChar.IsDead()) or None is ITEM_MANAGER.instance().FindByVID(self.GetSummonItemVID()) or ITEM_MANAGER.instance().FindByVID(self.GetSummonItemVID()).GetOwner() is not self.GetOwner():
            self.Unsummon()
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        if self.IsSummoned() and self.HasOption(EPetOptions.EPETOPTION_FOLLOWABLE):
            bResult = bResult and self._UpdateFollowAI()

        return bResult

    def _UpdateFollowAI(self):
        if None is self._m_pkChar.m_pkMobData:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if 0 == self._m_originalMoveSpeed:
            mobData = CMobManager.Instance().Get(self._m_dwVnum)

            if None is not mobData:
                self._m_originalMoveSpeed = mobData.m_table.sMovingSpeed
        START_FOLLOW_DISTANCE = 300.0
        START_RUN_DISTANCE = 900.0

        RESPAWN_DISTANCE = 4500.0
        APPROACH = 200

        bDoMoveAlone = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
        bRun = LGEMiscellaneous.DEFINECONSTANTS.false

        currentTime = get_dword_time()

        ownerX = self._m_pkOwner.GetX()
        ownerY = self._m_pkOwner.GetY()
        charX = self._m_pkChar.GetX()
        charY = self._m_pkChar.GetY()

        fDist = Globals.DISTANCE_APPROX(charX - ownerX, charY - ownerY)

        if fDist >= RESPAWN_DISTANCE:
            fOwnerRot = self._m_pkOwner.GetRotation() * 3.141592 / 180.0
            fx = -APPROACH * math.cos(fOwnerRot)
            fy = -APPROACH * math.sin(fOwnerRot)
            if self._m_pkChar.Show(self._m_pkOwner.GetMapIndex(), int(ownerX + fx), int(ownerY + fy), LONG_MAX, DefineConstants.false):
                return ((not LGEMiscellaneous.DEFINECONSTANTS.false))


        if fDist >= START_FOLLOW_DISTANCE:
            if fDist >= START_RUN_DISTANCE:
                bRun = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

            self._m_pkChar.SetNowWalking((not bRun))

            self._Follow(APPROACH)

            self._m_pkChar.SetLastAttacked(currentTime)
            self._m_dwLastActionTime = currentTime
        else:
            self._m_pkChar.SendMovePacket(EMoveFuncType.FUNC_WAIT, 0, 0, 0, 0, 0, -1)

        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def _UpdatAloneActionAI(self, fMinDist, fMaxDist):
        fDist = number(fMinDist, fMaxDist)
        r = float(number(0, 359))
        dest_x = self.GetOwner().GetX() + fDist * math.cos(r)
        dest_y = self.GetOwner().GetY() + fDist * math.sin(r)
        self._m_pkChar.SetNowWalking(((not LGEMiscellaneous.DEFINECONSTANTS.false)))

        if (not self._m_pkChar.IsStateMove()) and self._m_pkChar.Goto(int(dest_x), int(dest_y)):
            self._m_pkChar.SendMovePacket(EMoveFuncType.FUNC_WAIT, 0, 0, 0, 0, 0, -1)

        self._m_dwLastActionTime = get_dword_time()

        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def _Follow(self, fMinDistance = 50.0):
        if self._m_pkOwner is None or self._m_pkChar is None:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        fOwnerX = self._m_pkOwner.GetX()
        fOwnerY = self._m_pkOwner.GetY()

        fPetX = self._m_pkChar.GetX()
        fPetY = self._m_pkChar.GetY()

        fDist = Globals.DISTANCE_SQRT(int(fOwnerX - fPetX), int(fOwnerY - fPetY))
        if fDist <= fMinDistance:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        self._m_pkChar.SetRotationToXY(int(fOwnerX), int(fOwnerY))

        fx = None
        fy = None

        fDistToGo = fDist - fMinDistance
        GetDeltaByDegree(self._m_pkChar.GetRotation(), fDistToGo, fx, fy)

        if not self._m_pkChar.Goto(int((fPetX+fx+0.5)), int((fPetY+fy+0.5))):
            return LGEMiscellaneous.DEFINECONSTANTS.false

        self._m_pkChar.SendMovePacket(EMoveFuncType.FUNC_WAIT, 0, 0, 0, 0, 0, -1)

        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: CHARACTER* GetCharacter() const
    def GetCharacter(self):
        return self._m_pkChar
## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: CHARACTER* GetOwner() const
    def GetOwner(self):
        return self._m_pkOwner
## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: uint GetVID() const
    def GetVID(self):
        return self._m_dwVID
## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: uint GetVnum() const
    def GetVnum(self):
        return self._m_dwVnum
## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: bool HasOption(EPetOptions option) const
    def HasOption(self, option):
        return (self._m_dwOptions & uint(option)) != 0
    def SetName(self, name):
        petName = self._m_pkOwner.GetName(LOCALE_LANIATUS)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if ! __MULTI_LANGUAGE_SYSTEM__
        if None is not self._m_pkOwner and None == name and None != self._m_pkOwner.GetName(LOCALE_LANIATUS):
            petName += "'s Pet"
        else:
            petName += name
##endif

        if ((not LGEMiscellaneous.DEFINECONSTANTS.false)) == self.IsSummoned():
            self._m_pkChar.SetName(petName)

        self._m_name = petName

    def Mount(self):
        if None is self._m_pkOwner:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if ((not LGEMiscellaneous.DEFINECONSTANTS.false)) == self.HasOption(EPetOptions.EPETOPTION_MOUNTABLE):
            self._m_pkOwner.MountVnum(self._m_dwVnum)

        return self._m_pkOwner.GetMountVnum() == self._m_dwVnum

    def Unmount(self):
        if None is self._m_pkOwner:
            return

        if self._m_pkOwner.IsHorseRiding():
            self._m_pkOwner.StopRiding()

    def Summon(self, petName, pSummonItem, bSpawnFar = LGEMiscellaneous.DefineConstants.false):
        x = self._m_pkOwner.GetX()
        y = self._m_pkOwner.GetY()
        z = self._m_pkOwner.GetZ()

        if ((not LGEMiscellaneous.DEFINECONSTANTS.false)) == bSpawnFar:
            x += (number(0, 1) * 2 - 1) * number(2000, 2500)
            y += (number(0, 1) * 2 - 1) * number(2000, 2500)
        else:
            x += number(-100, 100)
            y += number(-100, 100)

        if None is not self._m_pkChar:
            self._m_pkChar.Show(self._m_pkOwner.GetMapIndex(), x, y, LONG_MAX, DefineConstants.false)
            self._m_dwVID = self._m_pkChar.GetVID()

            return self._m_dwVID

        self._m_pkChar = CHARACTER_MANAGER.instance().SpawnMob(self._m_dwVnum, self._m_pkOwner.GetMapIndex(), x, y, z, LGEMiscellaneous.DEFINECONSTANTS.false, int((self._m_pkOwner.GetRotation()+180)), LGEMiscellaneous.DEFINECONSTANTS.false)

        if None is self._m_pkChar:
            #lani_err("[CPetSystem::Summon] Failed to summon the pet. (vnum: %d)", self._m_dwVnum)
            return 0

        self._m_pkChar.SetPet()
        self._m_pkChar.SetEmpire(self._m_pkOwner.GetEmpire())
        self._m_dwVID = self._m_pkChar.GetVID()
        self._m_pkChar.SetName(petName)
        self.SetSummonItem(pSummonItem)
        self._m_pkOwner.ComputePoints()
        self._m_pkChar.Show(self._m_pkOwner.GetMapIndex(), x, y, z, DefineConstants.false)

        return self._m_dwVID

    def Unsummon(self):
        if ((not LGEMiscellaneous.DEFINECONSTANTS.false)) == self.IsSummoned():
            self.ClearBuff()
            self.SetSummonItem(None)
            if None is not self._m_pkOwner:
                self._m_pkOwner.ComputePoints()

            if None is not self._m_pkChar:
                CHARACTER_MANAGER.instance().DestroyCharacter(self._m_pkChar)

            self._m_pkChar = None
            self._m_dwVID = 0

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: bool IsSummoned() const
    def IsSummoned(self):
        return None is not self._m_pkChar
    def SetSummonItem(self, pItem):
        if None is pItem:
            self._m_dwSummonItemVID = 0
            self._m_dwSummonItemVnum = 0
            return

        self._m_dwSummonItemVID = pItem.GetVID()
        self._m_dwSummonItemVnum = pItem.GetVnum()

    def GetSummonItemVID(self):
        return self._m_dwSummonItemVID
    def GiveBuff(self):
        if 34004 == self._m_dwVnum or 34009 == self._m_dwVnum:
            if None is self._m_pkOwner.GetDungeon():
                return
        item = ITEM_MANAGER.instance().FindByVID(self._m_dwSummonItemVID)
        if None is not item:
            item.ModifyPoints(((not LGEMiscellaneous.DEFINECONSTANTS.false)))
        return

    def ClearBuff(self):
        if None is self._m_pkOwner:
            return
        item_proto = ITEM_MANAGER.instance().GetTable(self._m_dwSummonItemVnum)
        if None is item_proto:
            return
        i = 0
        while i < EItemMisc.ITEM_APPLY_MAX_NUM:
            if item_proto.aApplies[i].bType == EApplyTypes.APPLY_NONE:
                continue
            self._m_pkOwner.ApplyPoint(item_proto.aApplies[i].bType, -item_proto.aApplies[i].lValue)
            i += 1

        return


class CPetSystem:

    def __init__(self, owner):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self._m_petActorMap = _boost_func_of_void.unordered_map()
        self._m_pkOwner = None
        self._m_dwUpdatePeriod = 0
        self._m_dwLastUpdateTime = 0
        self._m_pkPetSystemUpdateEvent = _boost_func_of_void.intrusive_ptr()

        self._m_pkOwner = owner
        self._m_dwUpdatePeriod = 400

        self._m_dwLastUpdateTime = 0

    def close(self):
        self.Destroy()

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: CPetActor* GetByVID(uint vid) const
    def GetByVID(self, vid):
        petActor = None

        bFound = LGEMiscellaneous.DEFINECONSTANTS.false

        iter = m_petActorMap.begin()
        while iter is not self._m_petActorMap.end():
            petActor = iter.second

            if None is petActor:
                #lani_err("[CPetSystem::GetByVID(%d)] Null Pointer (petActor)", vid)
                continue

            bFound = petActor.GetVID() == vid

            if ((not LGEMiscellaneous.DEFINECONSTANTS.false)) == bFound:
                break
            iter += 1

        return petActor if bFound else None

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: CPetActor* GetByVnum(uint vnum) const
    def GetByVnum(self, vnum):
        petActor = None

        iter = self._m_petActorMap.find(vnum)

        if self._m_petActorMap.end() != iter:
            petActor = iter.second

        return petActor

    def Update(self, deltaTime):
        bResult = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        currentTime = get_dword_time()

        if self._m_dwUpdatePeriod > currentTime - self._m_dwLastUpdateTime:
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        v_garbageActor = []

        iter = m_petActorMap.begin()
        while iter is not self._m_petActorMap.end():
            petActor = iter.second

            if None is not petActor and petActor.IsSummoned():
                pPet = petActor.GetCharacter()

                if None is CHARACTER_MANAGER.instance().Find(pPet.GetVID()):
                    v_garbageActor.append(petActor)
                else:
                    bResult = bResult and petActor.Update(deltaTime)
            iter += 1
        for it in v_garbageActor:
            DeletePet(*it)

        self._m_dwLastUpdateTime = currentTime

        return bResult

    def Destroy(self):
        iter = m_petActorMap.begin()
        while iter is not self._m_petActorMap.end():
            petActor = iter.second

            if None is not petActor:
                if petActor is not None:
                    petActor.close()
            iter += 1
        event_cancel(self._m_pkPetSystemUpdateEvent)
        self._m_petActorMap.clear()

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: size_t CountSummoned() const
    def CountSummoned(self):
        count = 0

        iter = m_petActorMap.begin()
        while iter is not self._m_petActorMap.end():
            petActor = iter.second

            if None is not petActor:
                if petActor.IsSummoned():
                    count += 1
            iter += 1

        return size_t(count)

# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    SetUpdatePeriod(ms)
    def Summon(self, mobVnum, pSummonItem, petName, bSpawnFar, options = CPetActor.EPetOptions.EPetOption_Followable | CPetActor.EPetOptions.EPetOption_Summonable):
        petActor = self.GetByVnum(mobVnum)

        if None is petActor:
            petActor = LG_NEW_M2 CPetActor(self._m_pkOwner, mobVnum, options)
            self._m_petActorMap.insert((mobVnum, petActor))

        petVID = petActor.Summon(petName, pSummonItem, bSpawnFar)

        if None is self._m_pkPetSystemUpdateEvent:
            info = Globals.AllocEventInfo()

            info.pPetSystem = self

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
            self._m_pkPetSystemUpdateEvent = event_create_ex(petsystem_update_event, info, ((1) * passes_per_sec) / 4)

        return petActor

    def HandlePetCostumeItem(self):
        if self.CountSummoned():
            for it in self._m_petActorMap:
                petActor = it.second

                if petActor:
                    petActor.Unsummon()

        pkPetCostume = self._m_pkOwner.GetWear(EWearPositions.WEAR_COSTUME_PET)
        if pkPetCostume is None:
            return

        dwPetVnum = uint(pkPetCostume.GetValue(0))
        if dwPetVnum == 0:
            return

        mob = CMobManager.instance().Get(dwPetVnum)
        if mob is None:
            return

        nameBuf = str(['\0' for _ in range((int)LGEMiscellaneous.CHARACTER_NAME_MAX_LEN)])
        sprintf(nameBuf, "%s - %s", self._m_pkOwner.GetName(LOCALE_LANIATUS), mob.m_table.szLocaleName)

        self.Summon(dwPetVnum, pkPetCostume, nameBuf, LGEMiscellaneous.DEFINECONSTANTS.false, CPetActor.EPetOption_Followable | CPetActor.EPetOption_Summonable)

    def Unsummon(self, vnum, bDeleteFromList = LGEMiscellaneous.DefineConstants.false):
        actor = self.GetByVnum(vnum)

        if None is actor:
            #lani_err("[CPetSystem::GetByVnum(%d)] Null Pointer (petActor)", vnum)
            return
        actor.Unsummon()

        if ((not LGEMiscellaneous.DEFINECONSTANTS.false)) == bDeleteFromList:
            self.DeletePet(actor)

        bActive = LGEMiscellaneous.DEFINECONSTANTS.false
        it = m_petActorMap.begin()
        while it is not self._m_petActorMap.end():
            bActive |= it.second.IsSummoned()
            it += 1
        if LGEMiscellaneous.DEFINECONSTANTS.false == bActive:
            event_cancel(self._m_pkPetSystemUpdateEvent)
            self._m_pkPetSystemUpdateEvent = None

# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    Unsummon(petActor, bDeleteFromList = LGEMiscellaneous.DefineConstants.false)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    AddPet(mobVnum, petName, ability, options = CPetActor.EPetOptions.EPetOption_Followable | CPetActor.EPetOptions.EPetOption_Summonable | CPetActor.EPetOptions.EPetOption_Combatable)
    def DeletePet(self, mobVnum):
        iter = self._m_petActorMap.find(mobVnum)

        if self._m_petActorMap.end() == iter:
            #lani_err("[CPetSystem::DeletePet] Can't find pet on my list (VNUM: %d)", mobVnum)
            return

        petActor = iter.second

        if None is petActor:
            #lani_err("[CPetSystem::DeletePet] Null Pointer (petActor)")
        else:
            if petActor is not None:
                petActor.close()

        self._m_petActorMap.erase(iter)

    def DeletePet(self, petActor):
        iter = m_petActorMap.begin()
        while iter is not self._m_petActorMap.end():
            if iter.second is petActor:
                if petActor is not None:
                    petActor.close()
                self._m_petActorMap.erase(iter)

                return
            iter += 1

        #lani_err("[CPetSystem::DeletePet] Can't find petActor(0x%x) on my list(size: %d) ", petActor, self._m_petActorMap.size())

    def RefreshBuff(self):
        iter = m_petActorMap.begin()
        while iter is not self._m_petActorMap.end():
            petActor = iter.second

            if None is not petActor:
                if petActor.IsSummoned():
                    petActor.GiveBuff()
            iter += 1

class petsystem_event_info(event_info_data):

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.pPetSystem = None
