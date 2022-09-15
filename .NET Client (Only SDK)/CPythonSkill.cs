public class CPythonSkill
{
//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __RegisterGradeIconImage(TSkillData rData, string c_szHeader, string c_szImageName)
	{
		for (int j = 0; j < SKILL_GRADE_COUNT; ++j)
		{
			TGradeData rGradeData = rData.GradeData[j];
    
			string szCount = new string(new char[8 + 1]);
			_snprintf(szCount, sizeof(char), "_%02d", j + 1);
    
			string strFileName = "";
			strFileName += c_szHeader;
			strFileName += c_szImageName;
			strFileName += szCount;
			strFileName += ".sub";
			rGradeData.pImage = (CGraphicImage)CResourceManager.Instance().GetResourcePointer(strFileName);
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __RegisterNormalIconImage(TSkillData rData, string c_szHeader, string c_szImageName)
	{
		string strFileName = "";
		strFileName += c_szHeader;
		strFileName += c_szImageName;
		strFileName += ".sub";
		rData.pImage = (CGraphicImage)CResourceManager.Instance().GetResourcePointer(strFileName);
		for (int j = 0; j < SKILL_GRADE_COUNT; ++j)
		{
			TGradeData rGradeData = rData.GradeData[j];
			rGradeData.pImage = rData.pImage;
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool GetSkillData(uint dwSkillIndex, TSkillData[] ppSkillData)
	{
		TSkillDataMap.iterator it = m_SkillDataMap.find(dwSkillIndex);
    
		if (m_SkillDataMap.end() == it)
		{
			return false;
		}
    
		ppSkillData[0] = &(it.second);
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool GetSkillDataByName(string c_szName, TSkillData[] ppSkillData)
	{
		TSkillDataMap.iterator itor = m_SkillDataMap.begin();
		for (; itor != m_SkillDataMap.end(); ++itor)
		{
			TSkillData pData = &(itor.second);
			if (0 == pData.strName.compare(c_szName))
			{
				ppSkillData[0] = &(itor.second);
				return true;
			}
		}
		return false;
	}
}