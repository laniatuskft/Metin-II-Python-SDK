class SMobSplashAttackInfo:

    def __init__(self, dwTiming, dwHitDistance):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.dwTiming = 0
        self.dwHitDistance = 0

        self.dwTiming = dwTiming
        self.dwHitDistance = dwHitDistance

class SMobSkillInfo:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.dwSkillVnum = 0
        self.bSkillLevel = 0
        self.vecSplashAttack = []


class CMob:
    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.m_table = SMobTable()
        self.m_mobSkillInfo = [TMobSkillInfo() for _ in range((int)LGEMiscellaneous.MOB_LG_SKILL_MAX_NUM)]

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memset(self.m_table, 0, sizeof(self.m_table))

        i = 0
        while i < LGEMiscellaneous.MOB_LG_SKILL_MAX_NUM:
            self.m_mobSkillInfo[i].dwSkillVnum = 0
            self.m_mobSkillInfo[i].bSkillLevel = 0
            self.m_mobSkillInfo[i].vecSplashAttack.clear()
            i += 1

    def close(self):
        pass

    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The typedef 'TMobSkillInfo' was defined in multiple preprocessor conditionals and cannot be replaced in-line:

    def AddSkillSplash(self, iIndex, dwTiming, dwHitDistance):
        if iIndex >= LGEMiscellaneous.MOB_LG_SKILL_MAX_NUM or iIndex < 0:
            return

        #sys_log(0, "MOB_SPLASH %s idx %d timing %u hit_distance %u", self.m_table.szLocaleName, iIndex, dwTiming, dwHitDistance)

        self.m_mobSkillInfo[iIndex].vecSplashAttack.push_back(TMobSplashAttackInfo(dwTiming, dwHitDistance))

class CMobInstance:
    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.m_posLastAttacked = pixel_position_s()
        self.m_dwLastAttackedTime = 0
        self.m_dwLastWarpTime = 0
        self.m_IsBerserk = False
        self.m_IsGodSpeed = False
        self.m_IsRevive = False

        self.m_IsBerserk = LGEMiscellaneous.DEFINECONSTANTS.false
        self.m_IsGodSpeed = LGEMiscellaneous.DEFINECONSTANTS.false
        self.m_IsRevive = LGEMiscellaneous.DEFINECONSTANTS.false
        self.m_dwLastAttackedTime = get_dword_time()
        self.m_dwLastWarpTime = get_dword_time()

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memset(self.m_posLastAttacked, 0, sizeof(self.m_posLastAttacked))



class CMobGroupGroup:
    def __init__(self, dwVnum):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.m_dwVnum = 0
        self.m_vec_dwMemberVnum = []
        self.m_vec_iProbs = []

        self.m_dwVnum = dwVnum

    def AddMember(self, dwVnum, prob = 1):
        if prob == 0:
            return

        if self.m_vec_iProbs:
            prob += self.m_vec_iProbs[len(self.m_vec_iProbs) - 1]

        self.m_vec_iProbs.append(prob)
        self.m_vec_dwMemberVnum.append(dwVnum)

    def GetMember(self):
        if not self.m_vec_dwMemberVnum:
            return 0

        n = number(1, self.m_vec_iProbs[len(self.m_vec_iProbs) - 1])
        it = lower_bound(self.m_vec_iProbs.begin(), self.m_vec_iProbs.end(), n)

        return self.m_vec_dwMemberVnum[std::distance(self.m_vec_iProbs.begin(), it)]


class CMobGroup:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.m_dwVnum = 0
        self.m_stName = ""
        self.m_vec_dwMemberVnum = []

    def Create(self, dwVnum, r_stName):
        self.m_dwVnum = dwVnum
        self.m_stName = r_stName

    def GetMemberVector(self):
        return list(self.m_vec_dwMemberVnum)

    def GetMemberCount(self):
        return len(self.m_vec_dwMemberVnum)

    def AddMember(self, dwVnum):
        self.m_vec_dwMemberVnum.append(dwVnum)


class CMobManager(singleton):

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self._m_map_pkMobByVnum = {}
        self._m_map_pkMobByName = {}
        self._m_map_pkMobGroup = {}
        self._m_map_pkMobGroupGroup = {}
        self._m_mapRegenCount = {}
        self._m_set_CostumeMounts = std::set()


    def close(self):
        pass

    def Initialize(self, pTable, iSize):
        self._m_map_pkMobByVnum.clear()
        self._m_map_pkMobByName.clear()

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Pointer arithmetic is detected on this variable:
#ORIGINAL METINII C CODE: SMobTable * t = pTable;
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
        t = SMobTable(pTable)


        i = 0
        while i < iSize:
            pkMob = LG_NEW_M2 CMob

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memcpy' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            memcpy(pkMob.m_table, t, sizeof(SMobTable))

            self._m_map_pkMobByVnum.insert(dict.value_type(t.dwVnum, pkMob))
            self._m_map_pkMobByName.insert(dict.value_type(t.szLocaleName, pkMob))

            SkillCount = 0

            j = 0
            while j < LGEMiscellaneous.MOB_LG_SKILL_MAX_NUM:
                if (pkMob.m_table.Skills[j].dwVnum) != 0:
                    SkillCount += 1
                j += 1

            #sys_log(0, "MOB: #%-5d %-30s LEVEL %u HP %u DEF %u EXP %u DROP_ITEM_VNUM %u LG_SKILL_COUNT %d", t.dwVnum, t.szLocaleName, t.bLevel, t.dwMaxHP, t.wDef, t.dwExp, t.dwDropItemVnum, SkillCount)

            if t.bType == ECharType.CHAR_TYPE_NPC or t.bType == ECharType.CHAR_TYPE_WARP or t.bType == ECharType.CHAR_TYPE_GOTO:
                CHARACTER_MANAGER.instance().RegisterRaceNum(t.dwVnum)

            quest.CQuestManager.instance().RegisterNPCVnum(t.dwVnum)
            i += 1
            t += 1

        FILE_NAME_LEN = 256
        szGroupFileName = str(['\0' for _ in range(FILE_NAME_LEN)])
        szGroupGroupFileName = str(['\0' for _ in range(FILE_NAME_LEN)])

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        snprintf(szGroupFileName, sizeof(szGroupGroupFileName), "%s/group.txt", LocaleService_GetBasePath().c_str())
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        snprintf(szGroupGroupFileName, sizeof(szGroupGroupFileName), "%s/group_group.txt", LocaleService_GetBasePath().c_str())

        if not self.LoadGroup(szGroupFileName):
            #lani_err("cannot load %s", szGroupFileName)
            thecore_shutdown()
        if not self.LoadGroupGroup(szGroupGroupFileName):
            #lani_err("cannot load %s", szGroupGroupFileName)
            thecore_shutdown()

        CHARACTER_MANAGER.instance().for_each_pc(std::bind(self.RebindMobProto, self, std::placeholders._1))
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    Destroy()
    def LoadGroup(self, c_pszFileName):
        loader = CTextFileLoader()

        if not loader.Load(c_pszFileName):
            return LGEMiscellaneous.DEFINECONSTANTS.false

        stName = ""

        i = 0
        while i < loader.GetChildNodeCount():
            loader.SetChildNode(i)

            loader.GetCurrentNodeName(stName)

            iVnum = None

            temp_ref_iVnum = RefObject(iVnum);
            if not loader.GetTokenInteger("vnum", temp_ref_iVnum):
                iVnum = temp_ref_iVnum.arg_value
                #lani_err("LoadGroup : Syntax error %s : no vnum, node %s", c_pszFileName, stName)
                loader.SetParentNode()
                continue
            else:
                iVnum = temp_ref_iVnum.arg_value

            pTok = None

            if not loader.GetTokenVector("leader", pTok):
                #lani_err("LoadGroup : Syntax error %s : no leader, node %s", c_pszFileName, stName)
                loader.SetParentNode()
                continue

            if len(pTok) < 2:
                #lani_err("LoadGroup : Syntax error %s : no leader vnum, node %s", c_pszFileName, stName)
                loader.SetParentNode()
                continue

            pkGroup = LG_NEW_M2 CMobGroup

            pkGroup.Create(uint(iVnum), stName)
            vnum = 0
            temp_ref_vnum = RefObject(vnum);
            Globals.str_to_number(temp_ref_vnum, pTok[1])
            vnum = temp_ref_vnum.arg_value
            pkGroup.AddMember(vnum)

            #sys_log(0, "GROUP: %-5d %s", iVnum, stName)
            #sys_log(0, "               %s %s", pTok[0], pTok[1])

            for k in range(1, 256):
                buf = str(['\0' for _ in range(4)])
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                snprintf(buf, sizeof(buf), "%d", k)

                if loader.GetTokenVector(buf, pTok):
                    #sys_log(0, "               %s %s", pTok[0], pTok[1])
                    vnum = 0
                    temp_ref_vnum2 = RefObject(vnum);
                    Globals.str_to_number(temp_ref_vnum2, pTok[1])
                    vnum = temp_ref_vnum2.arg_value
                    pkGroup.AddMember(vnum)
                    continue

                break

            loader.SetParentNode()
            self._m_map_pkMobGroup.insert(dict.value_type(iVnum, pkGroup))
            i += 1

        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def LoadGroupGroup(self, c_pszFileName):
        loader = CTextFileLoader()

        if not loader.Load(c_pszFileName):
            return LGEMiscellaneous.DEFINECONSTANTS.false

        stName = ""

        i = 0
        while i < loader.GetChildNodeCount():
            loader.SetChildNode(i)

            loader.GetCurrentNodeName(stName)

            iVnum = None

            temp_ref_iVnum = RefObject(iVnum);
            if not loader.GetTokenInteger("vnum", temp_ref_iVnum):
                iVnum = temp_ref_iVnum.arg_value
                #lani_err("LoadGroupGroup : Syntax error %s : no vnum, node %s", c_pszFileName, stName)
                loader.SetParentNode()
                continue
            else:
                iVnum = temp_ref_iVnum.arg_value

            pTok = None

            pkGroup = LG_NEW_M2 CMobGroupGroup(uint(iVnum))

            for k in range(1, 256):
                buf = str(['\0' for _ in range(4)])
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                snprintf(buf, sizeof(buf), "%d", k)

                if loader.GetTokenVector(buf, pTok):
                    dwMobVnum = 0
                    temp_ref_dwMobVnum = RefObject(dwMobVnum);
                    Globals.str_to_number(temp_ref_dwMobVnum, pTok[0])
                    dwMobVnum = temp_ref_dwMobVnum.arg_value

                    prob = 1
                    if len(pTok) > 1:
                        temp_ref_prob = RefObject(prob);
                        Globals.str_to_number(temp_ref_prob, pTok[1])
                        prob = temp_ref_prob.arg_value

                    if dwMobVnum != 0:
                        pkGroup.AddMember(dwMobVnum, 1)

                    continue

                break

            loader.SetParentNode()

            self._m_map_pkMobGroupGroup.update({iVnum: pkGroup})
            i += 1

        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def GetGroup(self, dwVnum):
        it = self._m_map_pkMobGroup.find(dwVnum)

        if it is self._m_map_pkMobGroup.end():
            return None

        return it.second

    def GetGroupFromGroupGroup(self, dwVnum):
        it = self._m_map_pkMobGroupGroup.find(dwVnum)

        if it is self._m_map_pkMobGroupGroup.end():
            return 0

        return it.second.GetMember()

    def Get(self, dwVnum):
        it = self._m_map_pkMobByVnum.find(dwVnum)

        if it is self._m_map_pkMobByVnum.end():
            return None

        return it.second

    def Get(self, c_pszName, bIsAbbrev):
        if not bIsAbbrev:
            it = self._m_map_pkMobByName.find(c_pszName)

            if it is self._m_map_pkMobByName.end():
                return None

            return it.second

        len = len(c_pszName)
        it = self._m_map_pkMobByName.begin()

        while it is not self._m_map_pkMobByName.end():
            if not strncmp(it.first.c_str(), c_pszName, len):
                return it.second

            it += 1

        return None

    def begin(self):
        return self._m_map_pkMobByVnum.begin()
    def end(self):
        return self._m_map_pkMobByVnum.end()
    def RebindMobProto(self, ch):
        if ch.IsPC():
            return

        pMob = self.Get(ch.GetRaceNum())

        if pMob:
            ch.SetProto(pMob)

    def IncRegenCount(self, bRegenType, dwVnum, iCount, iTime):
        if bRegenType == Globals.REGEN_TYPE_MOB:
            self._m_mapRegenCount[dwVnum] += iCount * 86400.0 / iTime

        elif bRegenType == Globals.REGEN_TYPE_GROUP:
                pkGroup = CMobManager.Instance().GetGroup(dwVnum)
                if pkGroup is None:
                    return
                c_rdwMembers = pkGroup.GetMemberVector()

                i = 0
                while i<len(c_rdwMembers):
                    self._m_mapRegenCount[c_rdwMembers[i]] += iCount * 86400.0 / iTime
                    i += 1

        elif bRegenType == Globals.REGEN_TYPE_GROUP_GROUP:
                it = self._m_map_pkMobGroupGroup.find(dwVnum)

                if it is self._m_map_pkMobGroupGroup.end():
                    return

                v = it.second.m_vec_dwMemberVnum
                i = 0
                while i<len(v):
                    pkGroup = CMobManager.Instance().GetGroup(list(v[i]))
                    if pkGroup is None:
                        return
                    c_rdwMembers = pkGroup.GetMemberVector()

                    i = 0
                    while i<len(c_rdwMembers):
                        self._m_mapRegenCount[c_rdwMembers[i]] += iCount * 86400.0 / iTime / len(v)
                        i += 1
                    i += 1

    def InsertCostumeMount(self, dwVnum):
        if dwVnum == 0:
            return

        if self._m_set_CostumeMounts.find(dwVnum) != self._m_set_CostumeMounts.end():
            return

        self._m_set_CostumeMounts.insert(dwVnum)

    def IsCostumeMount(self, dwVnum):
        if self._m_set_CostumeMounts.find(dwVnum) != self._m_set_CostumeMounts.end():
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        return LGEMiscellaneous.DEFINECONSTANTS.false

    def DumpRegenCount(self, c_szFilename):
        fp = fopen(c_szFilename, "w")

        if fp:
            fprintf(fp,"MOB_VNUM\tCOUNT\n")

            it = m_mapRegenCount.begin()
            while it is not self._m_mapRegenCount.end():
                fprintf(fp,"%u\t%g\n", it.first, it.second)
                it += 1

            fclose(fp)


