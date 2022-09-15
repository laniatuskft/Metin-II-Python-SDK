public class CPythonGuild
{
//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetGradeData(byte byGradeNumber, TGuildGradeData rGuildGradeData)
	{
		m_GradeDataMap[byGradeNumber] = rGuildGradeData;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void RegisterMember(TGuildMemberData rGuildMemberData)
	{
		TGuildMemberData pGuildMemberData;
		if (GetMemberDataPtrByPID(rGuildMemberData.dwPID, pGuildMemberData))
		{
			pGuildMemberData.byGeneralFlag = rGuildMemberData.byGeneralFlag;
			pGuildMemberData.byGrade = rGuildMemberData.byGrade;
			pGuildMemberData.byLevel = rGuildMemberData.byLevel;
			pGuildMemberData.dwOffer = rGuildMemberData.dwOffer;
		}
		else
		{
			m_GuildMemberDataVector.push_back(rGuildMemberData);
		}
    
		__CalculateLevelAverage();
		__SortMember();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool GetGradeDataPtr(uint dwGradeNumber, TGuildGradeData[] ppData)
	{
		TGradeDataMap.iterator itor = m_GradeDataMap.find(dwGradeNumber);
		if (m_GradeDataMap.end() == itor)
		{
			return false;
		}
    
		ppData[0] = &(itor.second);
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool GetMemberDataPtr(uint dwIndex, TGuildMemberData[] ppData)
	{
		if (dwIndex >= m_GuildMemberDataVector.size())
		{
			return false;
		}
    
		ppData[0] = &m_GuildMemberDataVector[dwIndex];
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool GetMemberDataPtrByPID(uint dwPID, TGuildMemberData[] ppData)
	{
		TGuildMemberDataVector.iterator itor = new TGuildMemberDataVector.iterator();
		itor = std::find_if(m_GuildMemberDataVector.begin(), m_GuildMemberDataVector.end(), CPythonGuild_FFindGuildMemberByPID(dwPID));
    
		if (m_GuildMemberDataVector.end() == itor)
		{
			return false;
		}
    
		ppData[0] = &(*itor);
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool GetMemberDataPtrByName(string c_szName, TGuildMemberData[] ppData)
	{
		TGuildMemberDataVector.iterator itor = new TGuildMemberDataVector.iterator();
		itor = std::find_if(m_GuildMemberDataVector.begin(), m_GuildMemberDataVector.end(), CPythonGuild_FFindGuildMemberByName(c_szName));
    
		if (m_GuildMemberDataVector.end() == itor)
		{
			return false;
		}
    
		ppData[0] = &(*itor);
		return true;
	}
}