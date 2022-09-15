class SApply:
    def __init__(self, at, av, p = 0.0):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.apply_type = 0
        self.apply_value = 0
        self.prob = 0

        self.apply_type = EApplyTypes(at)
        self.apply_value = av
        self.prob = p

class DragonSoulTable:
    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self._m_pLoader = None
        self._stFileName = ""
        self._m_pApplyNumSettingNode = None
        self._m_pWeightTableNode = None
        self._m_pRefineGradeTableNode = None
        self._m_pRefineStepTableNode = None
        self._m_pRefineStrengthTableNode = None
        self._m_pDragonHeartExtTableNode = None
        self._m_pDragonSoulExtTableNode = None
        self._m_vecDragonSoulNames = []
        self._m_vecDragonSoulTypes = []
        self._m_map_name_to_type = {}
        self._m_map_type_to_name = {}
        self._m_map_basic_applys_group = {}
        self._m_map_additional_applys_group = {}

        self._m_pLoader = None

    def close(self):
        if self._m_pLoader:
            if self._m_pLoader is not None:
                self._m_pLoader.close()


    def ReadDragonSoulTableFile(self, c_pszFileName):
        self._m_pLoader = CGroupTextParseTreeLoader()
        loader = self._m_pLoader

        if LGEMiscellaneous.DEFINECONSTANTS.false == loader.Load(c_pszFileName):
            #lani_err("dragon_soul_table.txt load error")
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if not self._ReadVnumMapper():
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if not self._ReadBasicApplys():
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if not self._ReadAdditionalApplys():
            return LGEMiscellaneous.DEFINECONSTANTS.false

        self._m_pApplyNumSettingNode = loader.GetGroup("applynumsettings")
        self._m_pWeightTableNode = loader.GetGroup("weighttables")
        self._m_pRefineGradeTableNode = loader.GetGroup("refinegradetables")
        self._m_pRefineStepTableNode = loader.GetGroup("refinesteptables")
        self._m_pRefineStrengthTableNode = loader.GetGroup("refinestrengthtables")
        self._m_pDragonHeartExtTableNode = loader.GetGroup("dragonheartexttables")
        self._m_pDragonSoulExtTableNode = loader.GetGroup("dragonsoulexttables")

        if self._CheckApplyNumSettings() and self._CheckWeightTables() and self._CheckRefineGradeTables() and self._CheckRefineStepTables() and self._CheckRefineStrengthTables() and self._CheckDragonHeartExtTables() and self._CheckDragonSoulExtTables():
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
        else:
            #lani_err("DragonSoul table Check failed.")
            return LGEMiscellaneous.DEFINECONSTANTS.false

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: bool GetDragonSoulGroupName(byte bType, str& stGroupName) const
    def GetDragonSoulGroupName(self, bType, stGroupName):
        it = self._m_map_type_to_name.find(bType)
        if it is not self._m_map_type_to_name.end():
            stGroupName.arg_value = it.second
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
        else:
            #lani_err("Invalid DragonSoul Type(%d)", bType)
            return LGEMiscellaneous.DEFINECONSTANTS.false

# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    GetBasicApplys(ds_type, vec_basic_applys)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    GetAdditionalApplys(ds_type, vec_additional_attrs)
    def GetApplyNumSettings(self, ds_type, grade_idx, basis, add_min, add_max):
        if grade_idx >= EDragonSoulGradeTypes.DRAGON_SOUL_GRADE_MAX:
            #lani_err("Invalid dragon soul grade_idx(%d).", grade_idx)
            return LGEMiscellaneous.DEFINECONSTANTS.false

        stValue = ""
        stDragonSoulName = ""
        temp_ref_stDragonSoulName = RefObject(stDragonSoulName);
        if not self.GetDragonSoulGroupName(ds_type, temp_ref_stDragonSoulName):
            stDragonSoulName = temp_ref_stDragonSoulName.arg_value
            #lani_err("Invalid dragon soul type(%d).", ds_type)
            return LGEMiscellaneous.DEFINECONSTANTS.false
        else:
            stDragonSoulName = temp_ref_stDragonSoulName.arg_value

        if not self._m_pApplyNumSettingNode.GetGroupValue(stDragonSoulName, "basis", Globals.g_astGradeName[grade_idx], basis.arg_value):
            #lani_err("Invalid basis value. DragonSoulGroup(%s) Grade(%s)", stDragonSoulName, Globals.g_astGradeName[grade_idx])
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if not self._m_pApplyNumSettingNode.GetGroupValue(stDragonSoulName, "add_min", Globals.g_astGradeName[grade_idx], add_min.arg_value):
            #lani_err("Invalid add_min value. DragonSoulGroup(%s) Grade(%s)", stDragonSoulName, Globals.g_astGradeName[grade_idx])
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if not self._m_pApplyNumSettingNode.GetGroupValue(stDragonSoulName, "add_max", Globals.g_astGradeName[grade_idx], add_max.arg_value):
            #lani_err("Invalid add_max value. DragonSoulGroup(%s) Grade(%s)", stDragonSoulName, Globals.g_astGradeName[grade_idx])
            return LGEMiscellaneous.DEFINECONSTANTS.false

        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def GetWeight(self, ds_type, grade_idx, step_index, strength_idx, fWeight):
        if grade_idx >= EDragonSoulGradeTypes.DRAGON_SOUL_GRADE_MAX or step_index >= EDragonSoulStepTypes.DRAGON_SOUL_STEP_MAX or strength_idx >= LGEMiscellaneous.DEFINECONSTANTS.DRAGON_SOUL_STRENGTH_MAX:
            #lani_err("Invalid dragon soul grade_idx(%d) step_index(%d) strength_idx(%d).", grade_idx, step_index, strength_idx)
            return LGEMiscellaneous.DEFINECONSTANTS.false

        stValue = ""
        stDragonSoulName = ""
        temp_ref_stDragonSoulName = RefObject(stDragonSoulName);
        if not self.GetDragonSoulGroupName(ds_type, temp_ref_stDragonSoulName):
            stDragonSoulName = temp_ref_stDragonSoulName.arg_value
            #lani_err("Invalid dragon soul type(%d).", ds_type)
            return LGEMiscellaneous.DEFINECONSTANTS.false
        else:
            stDragonSoulName = temp_ref_stDragonSoulName.arg_value

        pDragonSoulGroup = self._m_pWeightTableNode.GetChildNode(stDragonSoulName)
        if None is not pDragonSoulGroup:
            if pDragonSoulGroup.GetGroupValue(Globals.g_astGradeName[grade_idx], Globals.g_astStepName[step_index], strength_idx, fWeight.arg_value):
                return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        pDragonSoulGroup = self._m_pWeightTableNode.GetChildNode("default")
        if None is not pDragonSoulGroup:
            if not pDragonSoulGroup.GetGroupValue(Globals.g_astGradeName[grade_idx], Globals.g_astStepName[step_index], strength_idx, fWeight.arg_value):
                #lani_err("Invalid float. DragonSoulGroup(%s) Grade(%s) Row(%s) Col(%d))", stDragonSoulName, Globals.g_astGradeName[grade_idx], Globals.g_astStepName[step_index], strength_idx)
                return LGEMiscellaneous.DEFINECONSTANTS.false
            else:
                return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
        #lani_err("Invalid value. DragonSoulGroup(%s) Grade(%s) Row(%s) Col(%d))", stDragonSoulName, Globals.g_astGradeName[grade_idx], Globals.g_astStepName[step_index], strength_idx)
        return LGEMiscellaneous.DEFINECONSTANTS.false

    def GetRefineGradeValues(self, ds_type, grade_idx, need_count, fee, vec_probs):
        if grade_idx >= EDragonSoulGradeTypes.DRAGON_SOUL_GRADE_MAX -1:
            #lani_err("Invalid dragon soul grade_idx(%d).", grade_idx)
            return LGEMiscellaneous.DEFINECONSTANTS.false

        stValue = ""
        stDragonSoulName = ""
        temp_ref_stDragonSoulName = RefObject(stDragonSoulName);
        if not self.GetDragonSoulGroupName(ds_type, temp_ref_stDragonSoulName):
            stDragonSoulName = temp_ref_stDragonSoulName.arg_value
            #lani_err("Invalid dragon soul type(%d).", ds_type)
            return LGEMiscellaneous.DEFINECONSTANTS.false
        else:
            stDragonSoulName = temp_ref_stDragonSoulName.arg_value

        pRow = None
        if not self._m_pRefineGradeTableNode.GetGroupRow(stDragonSoulName, Globals.g_astGradeName[grade_idx], pRow):
            #lani_err("Invalid row. DragonSoulGroup(%s) Grade(%s)", stDragonSoulName, Globals.g_astGradeName[grade_idx])
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if not pRow.GetValue("need_count", need_count.arg_value):
            #lani_err("Invalid value. DragonSoulGroup(%s) Grade(%s) Col(need_count)", stDragonSoulName, Globals.g_astGradeName[grade_idx])
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if not pRow.GetValue("fee", fee.arg_value):
            #lani_err("Invalid value. DragonSoulGroup(%s) Grade(%s) Col(fee)", stDragonSoulName, Globals.g_astGradeName[grade_idx])
            return LGEMiscellaneous.DEFINECONSTANTS.false

        vec_probs.resize(EDragonSoulGradeTypes.DRAGON_SOUL_GRADE_MAX)
        i = 0
        while i < EDragonSoulGradeTypes.DRAGON_SOUL_GRADE_MAX:
            if not pRow.GetValue(Globals.g_astGradeName[i], vec_probs[i]):
                #lani_err("Invalid value. DragonSoulGroup(%s) Grade(%s) Col(%s)", stDragonSoulName, Globals.g_astGradeName[grade_idx], Globals.g_astGradeName[i])
                return LGEMiscellaneous.DEFINECONSTANTS.false
            i += 1

        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def GetRefineStepValues(self, ds_type, step_idx, need_count, fee, vec_probs):
        if step_idx >= EDragonSoulStepTypes.DRAGON_SOUL_STEP_MAX - 1:
            #lani_err("Invalid dragon soul step_idx(%d).", step_idx)
            return LGEMiscellaneous.DEFINECONSTANTS.false

        stValue = ""
        stDragonSoulName = ""
        temp_ref_stDragonSoulName = RefObject(stDragonSoulName);
        if not self.GetDragonSoulGroupName(ds_type, temp_ref_stDragonSoulName):
            stDragonSoulName = temp_ref_stDragonSoulName.arg_value
            #lani_err("Invalid dragon soul type(%d).", ds_type)
            return LGEMiscellaneous.DEFINECONSTANTS.false
        else:
            stDragonSoulName = temp_ref_stDragonSoulName.arg_value

        pRow = None
        if not self._m_pRefineStepTableNode.GetGroupRow(stDragonSoulName, Globals.g_astStepName[step_idx], pRow):
            #lani_err("Invalid row. DragonSoulGroup(%s) Step(%s)", stDragonSoulName, Globals.g_astStepName[step_idx])
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if not pRow.GetValue("need_count", need_count.arg_value):
            #lani_err("Invalid value. DragonSoulGroup(%s) Step(%s) Col(need_count)", stDragonSoulName, Globals.g_astStepName[step_idx])
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if not pRow.GetValue("fee", fee.arg_value):
            #lani_err("Invalid value. DragonSoulGroup(%s) Step(%s) Col(fee)", stDragonSoulName, Globals.g_astStepName[step_idx])
            return LGEMiscellaneous.DEFINECONSTANTS.false

        vec_probs.resize(EDragonSoulStepTypes.DRAGON_SOUL_STEP_MAX)
        i = 0
        while i < EDragonSoulStepTypes.DRAGON_SOUL_STEP_MAX:
            if not pRow.GetValue(Globals.g_astStepName[i], vec_probs[i]):
                #lani_err("Invalid value. DragonSoulGroup(%s) Step(%s) Col(%s)", stDragonSoulName, Globals.g_astStepName[step_idx], Globals.g_astStepName[i])
                return LGEMiscellaneous.DEFINECONSTANTS.false
            i += 1

        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def GetRefineStrengthValues(self, ds_type, material_type, strength_idx, fee, prob):
        if material_type < EMaterialSubTypes.MATERIAL_DS_REFINE_NORMAL or material_type > EMaterialSubTypes.MATERIAL_DS_REFINE_HOLLY:
            #lani_err("Invalid dragon soul material_type(%d).", material_type)
            return LGEMiscellaneous.DEFINECONSTANTS.false

        stValue = ""
        stDragonSoulName = ""
        temp_ref_stDragonSoulName = RefObject(stDragonSoulName);
        if not self.GetDragonSoulGroupName(ds_type, temp_ref_stDragonSoulName):
            stDragonSoulName = temp_ref_stDragonSoulName.arg_value
            #lani_err("Invalid dragon soul type(%d).", ds_type)
            return LGEMiscellaneous.DEFINECONSTANTS.false
        else:
            stDragonSoulName = temp_ref_stDragonSoulName.arg_value

        if not self._m_pRefineStrengthTableNode.GetGroupValue(stDragonSoulName, Globals.g_astMaterialName[material_type], "fee", fee.arg_value):
            #lani_err("Invalid fee. DragonSoulGroup(%s) Material(%s)", stDragonSoulName, Globals.g_astMaterialName[material_type])
            return LGEMiscellaneous.DEFINECONSTANTS.false
        stStrengthIdx = _boost_func_of_void.lexical_cast  (int(strength_idx))

        if not self._m_pRefineStrengthTableNode.GetGroupValue(stDragonSoulName, Globals.g_astMaterialName[material_type], stStrengthIdx, prob.arg_value):
            #lani_err("Invalid prob. DragonSoulGroup(%s) Material(%s) Strength(%d)", stDragonSoulName, Globals.g_astMaterialName[material_type], strength_idx)
            return LGEMiscellaneous.DEFINECONSTANTS.false

        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def GetDragonHeartExtValues(self, ds_type, grade_idx, vec_chargings, vec_probs):
        if grade_idx >= EDragonSoulGradeTypes.DRAGON_SOUL_GRADE_MAX:
            #lani_err("Invalid dragon soul grade_idx(%d).", grade_idx)
            return LGEMiscellaneous.DEFINECONSTANTS.false

        stDragonSoulName = ""
        temp_ref_stDragonSoulName = RefObject(stDragonSoulName);
        if not self.GetDragonSoulGroupName(ds_type, temp_ref_stDragonSoulName):
            stDragonSoulName = temp_ref_stDragonSoulName.arg_value
            #lani_err("Invalid dragon soul type(%d).", ds_type)
            return LGEMiscellaneous.DEFINECONSTANTS.false
        else:
            stDragonSoulName = temp_ref_stDragonSoulName.arg_value

        pRow = None
        if not self._m_pDragonHeartExtTableNode.GetGroupRow(stDragonSoulName, "charging", pRow):
            #lani_err("Invalid CHARGING row. DragonSoulGroup(%s)", stDragonSoulName)
            return LGEMiscellaneous.DEFINECONSTANTS.false
        n = pRow.GetSize()
        vec_chargings.resize(n)
        for i in range(0, n):
            if not pRow.GetValue(i, vec_chargings[i]):
                #lani_err("Invalid CHARGING value. DragonSoulGroup(%s), Col(%d)", stDragonSoulName, i)
                return LGEMiscellaneous.DEFINECONSTANTS.false

        if not self._m_pDragonHeartExtTableNode.GetGroupRow(stDragonSoulName, Globals.g_astGradeName[grade_idx], pRow):
            #lani_err("Invalid row. DragonSoulGroup(%s) Grade(%s)", stDragonSoulName, Globals.g_astGradeName[grade_idx])
            return LGEMiscellaneous.DEFINECONSTANTS.false

        m = pRow.GetSize()
        if n != m:
            #lani_err("Invalid row size(%d). It must be same CHARGING row size(%d). DragonSoulGroup(%s) Grade(%s)", m, n, stDragonSoulName, Globals.g_astGradeName[grade_idx])
            return LGEMiscellaneous.DEFINECONSTANTS.false
        vec_probs.resize(m)
        for i in range(0, m):
            if not pRow.GetValue(i, vec_probs[i]):
                #lani_err("Invalid value. DragonSoulGroup(%s), Grade(%s) Col(%d)", stDragonSoulName, Globals.g_astGradeName[grade_idx], i)
                return LGEMiscellaneous.DEFINECONSTANTS.false

        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def GetDragonSoulExtValues(self, ds_type, grade_idx, prob, by_product):
        if grade_idx >= EDragonSoulGradeTypes.DRAGON_SOUL_GRADE_MAX:
            #lani_err("Invalid dragon soul grade_idx(%d).", grade_idx)
            return LGEMiscellaneous.DEFINECONSTANTS.false

        stValue = ""
        stDragonSoulName = ""
        temp_ref_stDragonSoulName = RefObject(stDragonSoulName);
        if not self.GetDragonSoulGroupName(ds_type, temp_ref_stDragonSoulName):
            stDragonSoulName = temp_ref_stDragonSoulName.arg_value
            #lani_err("Invalid dragon soul type(%d).", ds_type)
            return LGEMiscellaneous.DEFINECONSTANTS.false
        else:
            stDragonSoulName = temp_ref_stDragonSoulName.arg_value

        if not self._m_pDragonSoulExtTableNode.GetGroupValue(stDragonSoulName, Globals.g_astGradeName[grade_idx], "prob", prob.arg_value):
            #lani_err("Invalid Prob. DragonSoulGroup(%s) Grade(%s)", stDragonSoulName, Globals.g_astGradeName[grade_idx], Globals.g_astGradeName[grade_idx])
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if not self._m_pDragonSoulExtTableNode.GetGroupValue(stDragonSoulName, Globals.g_astGradeName[grade_idx], "byproduct", by_product.arg_value):
            #lani_err("Invalid fee. DragonSoulGroup(%s) Grade(%d)", stDragonSoulName, Globals.g_astGradeName[grade_idx], grade_idx)
            return LGEMiscellaneous.DEFINECONSTANTS.false

        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))





    def _ReadVnumMapper(self):
        stName = ""

        pGroupNode = self._m_pLoader.GetGroup("vnummapper")

        if None is pGroupNode:
            #lani_err("dragon_soul_table.txt need VnumMapper.")
            return LGEMiscellaneous.DEFINECONSTANTS.false
            n = pGroupNode.GetRowCount()
            if 0 == n:
                #lani_err("Group VnumMapper is Empty.")
                return LGEMiscellaneous.DEFINECONSTANTS.false

            setTypes = std::set()

            for i in range(0, n):
                pRow = None
                pGroupNode.GetRow(i, pRow)

                stDragonSoulName = ""
                bType = None
                if not pRow.GetValue("dragonsoulname", stDragonSoulName):
                    #lani_err("In Group VnumMapper, No DragonSoulName column.")
                    return LGEMiscellaneous.DEFINECONSTANTS.false
                if not pRow.GetValue("type", bType):
                    #lani_err("In Group VnumMapper, %s's Vnum is invalid", stDragonSoulName)
                    return LGEMiscellaneous.DEFINECONSTANTS.false

                if setTypes.end() != setTypes.find(bType):
                    #lani_err("In Group VnumMapper, duplicated vnum exist.")
                    return LGEMiscellaneous.DEFINECONSTANTS.false
                self._m_map_name_to_type.insert(TMapNameToType.value_type(stDragonSoulName, bType))
                self._m_map_type_to_name.insert(TMapTypeToName.value_type(bType, stDragonSoulName))
                self._m_vecDragonSoulTypes.append(bType)
                self._m_vecDragonSoulNames.append(stDragonSoulName)
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def _ReadBasicApplys(self):
        pGroupNode = self._m_pLoader.GetGroup("basicapplys")

        if None is pGroupNode:
            #lani_err("dragon_soul_table.txt need BasicApplys.")
            return LGEMiscellaneous.DEFINECONSTANTS.false

        i = 0
        while i < len(self._m_vecDragonSoulNames):
            pChild = None
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if (NULL == (pChild = pGroupNode->GetChildNode(m_vecDragonSoulNames[i])))
            if None is (pChild = pGroupNode.GetChildNode(self._m_vecDragonSoulNames[i])):
                #lani_err("In Group BasicApplys, %s group is not defined.", self._m_vecDragonSoulNames[i])
                return LGEMiscellaneous.DEFINECONSTANTS.false
            vecApplys = TVecApplys()
            n = pChild.GetRowCount()

            for j in range(1, n + 1):
                ss = std::stringstream()
                ss << j
                pRow = None

                pChild.GetRow(ss.str(), pRow)
                if None is pRow:
                    #lani_err("In Group BasicApplys, No %d row.", j)
                at = None
                av = None

                stTypeName = ""
                if not pRow.GetValue("apply_type", stTypeName):
                    #lani_err("In Group BasicApplys, %s group's apply_type is empty.", self._m_vecDragonSoulNames[i])
                    return LGEMiscellaneous.DEFINECONSTANTS.false
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if (!(at = (EApplyTypes)FN_get_apply_type(stTypeName.c_str())))
                if not(at = FN_get_apply_type(stTypeName)):
                    #lani_err("In Group BasicApplys, %s group's apply_type %s is invalid.", self._m_vecDragonSoulNames[i], stTypeName)
                    return LGEMiscellaneous.DEFINECONSTANTS.false
                if not pRow.GetValue("apply_value", av):
                    #lani_err("In Group BasicApplys, %s group's apply_value %s is invalid.", self._m_vecDragonSoulNames[i], av)
                    return LGEMiscellaneous.DEFINECONSTANTS.false
                vecApplys.push_back(SApply(at, av, 0.0))
            self._m_map_basic_applys_group.insert(TMapApplyGroup.value_type(self._m_map_name_to_type[self._m_vecDragonSoulNames[i]], vecApplys))
            i += 1

        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def _ReadAdditionalApplys(self):
        pGroupNode = self._m_pLoader.GetGroup("additionalapplys")
        if None is pGroupNode:
            #lani_err("dragon_soul_table.txt need AdditionalApplys.")
            return LGEMiscellaneous.DEFINECONSTANTS.false

        i = 0
        while i < len(self._m_vecDragonSoulNames):
            pChild = None
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if (NULL == (pChild = pGroupNode->GetChildNode(m_vecDragonSoulNames[i])))
            if None is (pChild = pGroupNode.GetChildNode(self._m_vecDragonSoulNames[i])):
                #lani_err("In Group AdditionalApplys, %s group is not defined.", self._m_vecDragonSoulNames[i])
                return LGEMiscellaneous.DEFINECONSTANTS.false
            vecApplys = TVecApplys()

            n = pChild.GetRowCount()

            for j in range(0, n):
                pRow = None

                pChild.GetRow(j, pRow)

                at = None
                av = None
                prob = None
                stTypeName = ""
                if not pRow.GetValue("apply_type", stTypeName):
                    #lani_err("In Group AdditionalApplys, %s group's apply_type is empty.", self._m_vecDragonSoulNames[i])
                    return LGEMiscellaneous.DEFINECONSTANTS.false
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if (!(at = (EApplyTypes)FN_get_apply_type(stTypeName.c_str())))
                if not(at = FN_get_apply_type(stTypeName)):
                    #lani_err("In Group AdditionalApplys, %s group's apply_type %s is invalid.", self._m_vecDragonSoulNames[i], stTypeName)
                    return LGEMiscellaneous.DEFINECONSTANTS.false
                if not pRow.GetValue("apply_value", av):
                    #lani_err("In Group AdditionalApplys, %s group's apply_value %s is invalid.", self._m_vecDragonSoulNames[i], av)
                    return LGEMiscellaneous.DEFINECONSTANTS.false
                if not pRow.GetValue("prob", prob):
                    #lani_err("In Group AdditionalApplys, %s group's probability %s is invalid.", self._m_vecDragonSoulNames[i], prob)
                    return LGEMiscellaneous.DEFINECONSTANTS.false
                vecApplys.push_back(SApply(at, av, prob))
            self._m_map_additional_applys_group.insert(TMapApplyGroup.value_type(self._m_map_name_to_type[self._m_vecDragonSoulNames[i]], vecApplys))
            i += 1

        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def _CheckApplyNumSettings(self):
        if None is self._m_pApplyNumSettingNode:
            #lani_err("dragon_soul_table.txt need ApplyNumSettings.")
            return LGEMiscellaneous.DEFINECONSTANTS.false
        else:
            i = 0
            while i < len(self._m_vecDragonSoulTypes):
                j = 0
                while j < EDragonSoulGradeTypes.DRAGON_SOUL_GRADE_MAX:
                    basis = None
                    add_min = None
                    add_max = None
                    temp_ref_basis = RefObject(basis);
                    temp_ref_add_min = RefObject(add_min);
                    temp_ref_add_max = RefObject(add_max);
                    if not self.GetApplyNumSettings(list(self._m_vecDragonSoulTypes[i]), byte(j), temp_ref_basis, temp_ref_add_min, temp_ref_add_max):
                        add_max = temp_ref_add_max.arg_value
                        add_min = temp_ref_add_min.arg_value
                        basis = temp_ref_basis.arg_value
                        #lani_err("In %s group of ApplyNumSettings, values in Grade(%s) row is invalid.", self._m_vecDragonSoulNames[i], Globals.g_astGradeName[j])
                        return LGEMiscellaneous.DEFINECONSTANTS.false
                    else:
                        add_max = temp_ref_add_max.arg_value
                        add_min = temp_ref_add_min.arg_value
                        basis = temp_ref_basis.arg_value
                    j += 1
                i += 1

        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def _CheckWeightTables(self):
        if None is self._m_pWeightTableNode:
            #lani_err("dragon_soul_table.txt need WeightTables.")
            return LGEMiscellaneous.DEFINECONSTANTS.false
        else:
            i = 0
            while i < len(self._m_vecDragonSoulTypes):
                j = 0
                while j < EDragonSoulGradeTypes.DRAGON_SOUL_GRADE_MAX:
                    k = 0
                    while k < EDragonSoulStepTypes.DRAGON_SOUL_STEP_MAX:
                        for l in range(0, LGEMiscellaneous.DEFINECONSTANTS.DRAGON_SOUL_STRENGTH_MAX):
                            fWeight = None
                            temp_ref_fWeight = RefObject(fWeight);
                            if not self.GetWeight(list(self._m_vecDragonSoulTypes[i]), byte(j), byte(k), l, temp_ref_fWeight):
                                fWeight = temp_ref_fWeight.arg_value
                                #lani_err("In %s group of WeightTables, value(Grade(%s), Step(%s), Strength(%d) is invalid.", self._m_vecDragonSoulNames[i], Globals.g_astGradeName[j], Globals.g_astStepName[k], l)
                            else:
                                fWeight = temp_ref_fWeight.arg_value
                        k += 1
                    j += 1
                i += 1
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def _CheckRefineGradeTables(self):
        if None is self._m_pRefineGradeTableNode:
            #lani_err("dragon_soul_table.txt need RefineGradeTables.")
            return LGEMiscellaneous.DEFINECONSTANTS.false
        else:
            i = 0
            while i < len(self._m_vecDragonSoulTypes):
                j = 0
                while j < EDragonSoulGradeTypes.DRAGON_SOUL_GRADE_MAX - 1:
                    need_count = None
                    fee = None
                    vec_probs = []
                    temp_ref_need_count = RefObject(need_count);
                    temp_ref_fee = RefObject(fee);
                    if not self.GetRefineGradeValues(list(self._m_vecDragonSoulTypes[i]), byte(j), temp_ref_need_count, temp_ref_fee, vec_probs):
                        fee = temp_ref_fee.arg_value
                        need_count = temp_ref_need_count.arg_value
                        #lani_err("In %s group of RefineGradeTables, values in Grade(%s) row is invalid.", self._m_vecDragonSoulNames[i], Globals.g_astGradeName[j])
                        return LGEMiscellaneous.DEFINECONSTANTS.false
                    else:
                        fee = temp_ref_fee.arg_value
                        need_count = temp_ref_need_count.arg_value
                    if need_count < 1:
                        #lani_err("In %s group of RefineGradeTables, need_count of Grade(%s) is less than 1.", self._m_vecDragonSoulNames[i], Globals.g_astGradeName[j])
                        return LGEMiscellaneous.DEFINECONSTANTS.false
                    if fee < 0:
                        #lani_err("In %s group of RefineGradeTables, fee of Grade(%s) is less than 0.", self._m_vecDragonSoulNames[i], Globals.g_astGradeName[j])
                        return LGEMiscellaneous.DEFINECONSTANTS.false
                    if EDragonSoulGradeTypes.DRAGON_SOUL_GRADE_MAX != len(vec_probs):
                        #lani_err("In %s group of RefineGradeTables, probability list size is not %d.", EDragonSoulGradeTypes.DRAGON_SOUL_GRADE_MAX)
                        return LGEMiscellaneous.DEFINECONSTANTS.false
                    k = 0
                    while k < len(vec_probs):
                        if vec_probs[k] < 0.0:
                            #lani_err("In %s group of RefineGradeTables, probability(index : %d) is less than 0.", k)
                            return LGEMiscellaneous.DEFINECONSTANTS.false
                        k += 1
                    j += 1
                i += 1

        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def _CheckRefineStepTables(self):
        if None is self._m_pRefineStrengthTableNode:
            #lani_err("dragon_soul_table.txt need RefineStepTables.")
            return LGEMiscellaneous.DEFINECONSTANTS.false
        else:
            i = 0
            while i < len(self._m_vecDragonSoulTypes):
                j = 0
                while j < EDragonSoulStepTypes.DRAGON_SOUL_STEP_MAX - 1:
                    need_count = None
                    fee = None
                    vec_probs = []
                    temp_ref_need_count = RefObject(need_count);
                    temp_ref_fee = RefObject(fee);
                    if not self.GetRefineStepValues(list(self._m_vecDragonSoulTypes[i]), byte(j), temp_ref_need_count, temp_ref_fee, vec_probs):
                        fee = temp_ref_fee.arg_value
                        need_count = temp_ref_need_count.arg_value
                        #lani_err("In %s group of RefineStepTables, values in Step(%s) row is invalid.", self._m_vecDragonSoulNames[i], Globals.g_astStepName[j])
                        return LGEMiscellaneous.DEFINECONSTANTS.false
                    else:
                        fee = temp_ref_fee.arg_value
                        need_count = temp_ref_need_count.arg_value
                    if need_count < 1:
                        #lani_err("In %s group of RefineStepTables, need_count of Step(%s) is less than 1.", self._m_vecDragonSoulNames[i], Globals.g_astStepName[j])
                        return LGEMiscellaneous.DEFINECONSTANTS.false
                    if fee < 0:
                        #lani_err("In %s group of RefineStepTables, fee of Step(%s) is less than 0.", self._m_vecDragonSoulNames[i], Globals.g_astStepName[j])
                        return LGEMiscellaneous.DEFINECONSTANTS.false

                    if EDragonSoulStepTypes.DRAGON_SOUL_STEP_MAX != len(vec_probs):
                        #lani_err("In %s group of RefineStepTables, probability list size is not %d.", self._m_vecDragonSoulNames[i], EDragonSoulStepTypes.DRAGON_SOUL_STEP_MAX)
                        return LGEMiscellaneous.DEFINECONSTANTS.false

                    k = 0
                    while k < len(vec_probs):
                        if vec_probs[k] < 0.0:
                            #lani_err("In %s group of RefineStepTables, probability(index : %d) is less than 0.", self._m_vecDragonSoulNames[i], k)
                            return LGEMiscellaneous.DEFINECONSTANTS.false
                        k += 1
                    j += 1
                i += 1

        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def _CheckRefineStrengthTables(self):
        pGroupNode = self._m_pRefineStrengthTableNode

        if None is pGroupNode:
            #lani_err("dragon_soul_table.txt need RefineStrengthTables.")
            return LGEMiscellaneous.DEFINECONSTANTS.false
        i = 0
        while i < len(self._m_vecDragonSoulTypes):
            j = MATERIAL_DS_REFINE_NORMAL
            while j <= EMaterialSubTypes.MATERIAL_DS_REFINE_HOLLY:
                fee = None
                prob = None
                for k in range(0, LGEMiscellaneous.DEFINECONSTANTS.DRAGON_SOUL_STRENGTH_MAX -1):
                    temp_ref_fee = RefObject(fee);
                    temp_ref_prob = RefObject(prob);
                    if not self.GetRefineStrengthValues(list(self._m_vecDragonSoulTypes[i]), byte(j), k, temp_ref_fee, temp_ref_prob):
                        prob = temp_ref_prob.arg_value
                        fee = temp_ref_fee.arg_value
                        #lani_err("In %s group of RefineStrengthTables, value(Material(%s), Strength(%d)) or fee are invalid.", self._m_vecDragonSoulNames[i], Globals.g_astMaterialName[j], k)
                        return LGEMiscellaneous.DEFINECONSTANTS.false
                    else:
                        prob = temp_ref_prob.arg_value
                        fee = temp_ref_fee.arg_value
                    if fee < 0:
                        #lani_err("In %s group of RefineStrengthTables, fee of Material(%s) is less than 0.", self._m_vecDragonSoulNames[i], Globals.g_astMaterialName[j])
                        return LGEMiscellaneous.DEFINECONSTANTS.false
                    if prob < 0.0:
                        #lani_err("In %s group of RefineStrengthTables, probability(Material(%s), Strength(%d)) is less than 0.", self._m_vecDragonSoulNames[i], Globals.g_astMaterialName[j], k)
                        return LGEMiscellaneous.DEFINECONSTANTS.false
                j += 1
            i += 1

        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def _CheckDragonHeartExtTables(self):
        if None is self._m_pDragonHeartExtTableNode:
            #lani_err("dragon_soul_table.txt need DragonHeartExtTables.")
            return LGEMiscellaneous.DEFINECONSTANTS.false
        i = 0
        while i < len(self._m_vecDragonSoulTypes):
            j = 0
            while j < EDragonSoulGradeTypes.DRAGON_SOUL_GRADE_MAX:
                vec_chargings = []
                vec_probs = []

                if not self.GetDragonHeartExtValues(list(self._m_vecDragonSoulTypes[i]), byte(j), vec_chargings, vec_probs):
                    #lani_err("In %s group of DragonHeartExtTables, CHARGING row or Grade(%s) row are invalid.", self._m_vecDragonSoulNames[i], Globals.g_astGradeName[j])
                    return LGEMiscellaneous.DEFINECONSTANTS.false
                if len(vec_chargings) != len(vec_probs):
                    #lani_err("In %s group of DragonHeartExtTables, CHARGING row size(%d) are not equal Grade(%s) row size(%d).", self._m_vecDragonSoulNames[i], len(vec_chargings), len(vec_probs))
                    return LGEMiscellaneous.DEFINECONSTANTS.false
                k = 0
                while k < len(vec_chargings):
                    if vec_chargings[k] < 0.0:
                        #lani_err("In %s group of DragonHeartExtTables, CHARGING value(index : %d) is less than 0", self._m_vecDragonSoulNames[i], k)
                        return LGEMiscellaneous.DEFINECONSTANTS.false
                    k += 1
                k = 0
                while k < len(vec_probs):
                    if vec_probs[k] < 0.0:
                        #lani_err("In %s group of DragonHeartExtTables, Probability(Grade : %s, index : %d) is less than 0", self._m_vecDragonSoulNames[i], Globals.g_astGradeName[j], k)
                        return LGEMiscellaneous.DEFINECONSTANTS.false
                    k += 1
                j += 1
            i += 1

        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def _CheckDragonSoulExtTables(self):
        if None is self._m_pDragonSoulExtTableNode:
            #lani_err("dragon_soul_table.txt need DragonSoulExtTables.")
            return LGEMiscellaneous.DEFINECONSTANTS.false
        i = 0
        while i < len(self._m_vecDragonSoulTypes):
            j = 0
            while j < EDragonSoulGradeTypes.DRAGON_SOUL_GRADE_MAX:
                prob = None
                by_product = None
                temp_ref_prob = RefObject(prob);
                temp_ref_by_product = RefObject(by_product);
                if not self.GetDragonSoulExtValues(list(self._m_vecDragonSoulTypes[i]), byte(j), temp_ref_prob, temp_ref_by_product):
                    by_product = temp_ref_by_product.arg_value
                    prob = temp_ref_prob.arg_value
                    #lani_err("In %s group of DragonSoulExtTables, Grade(%s) row is invalid.", self._m_vecDragonSoulNames[i], Globals.g_astGradeName[j])
                    return LGEMiscellaneous.DEFINECONSTANTS.false
                else:
                    by_product = temp_ref_by_product.arg_value
                    prob = temp_ref_prob.arg_value
                if prob < 0.0:
                    #lani_err("In %s group of DragonSoulExtTables, Probability(Grade : %s) is less than 0", self._m_vecDragonSoulNames[i], Globals.g_astGradeName[j])
                    return LGEMiscellaneous.DEFINECONSTANTS.false
                if 0 != by_product and None is ITEM_MANAGER.instance().GetTable(by_product):
                    #lani_err("In %s group of DragonSoulExtTables, ByProduct(%d) of Grade %s is not exist.", self._m_vecDragonSoulNames[i], by_product, Globals.g_astGradeName[j])
                    return LGEMiscellaneous.DEFINECONSTANTS.false
                j += 1
            i += 1
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

def GetBasicApplys(ds_type, vec_basic_applys):
    it = m_map_basic_applys_group.find(ds_type)
    if m_map_basic_applys_group.end() == it:
        return LGEMiscellaneous.DEFINECONSTANTS.false
    vec_basic_applys.arg_value = it.second
    return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

def GetAdditionalApplys(ds_type, vec_additional_applys):
    it = m_map_additional_applys_group.find(ds_type)
    if m_map_additional_applys_group.end() == it:
        return LGEMiscellaneous.DEFINECONSTANTS.false
    vec_additional_applys.arg_value = it.second
    return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
