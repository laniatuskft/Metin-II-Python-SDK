public class CRaceData
{
//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool CreateMotionModeIterator(ref TMotionModeDataIterator itor)
	{
		if (m_pMotionModeDataMap.empty())
		{
			return false;
		}
    
		itor = m_pMotionModeDataMap.begin();
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool NextMotionModeIterator(TMotionModeDataIterator itor)
	{
		++itor;
    
		return m_pMotionModeDataMap.end() != itor;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool GetMotionModeDataPointer(ushort wMotionMode, TMotionModeData[] ppMotionModeData)
	{
		TMotionModeDataIterator itor = m_pMotionModeDataMap.find(wMotionMode);
		if (itor == m_pMotionModeDataMap.end())
		{
			return false;
		}
    
		ppMotionModeData[0] = itor.second;
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool GetModelDataPointer(uint dwModelIndex, TModelData[] c_ppModelData)
	{
		TModelDataMapIterator itor = m_ModelDataMap.find(dwModelIndex);
		if (m_ModelDataMap.end() == itor)
		{
			return false;
		}
    
		c_ppModelData[0] = itor.second;
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool GetMotionVectorPointer(ushort wMotionMode, ushort wMotionIndex, TMotionVector[] ppMotionVector)
	{
		TMotionModeData pMotionModeData;
		if (!GetMotionModeDataPointer(wMotionMode, pMotionModeData))
		{
			return false;
		}
    
		TMotionVectorMap.iterator itor = pMotionModeData.MotionVectorMap.find(wMotionIndex);
		if (pMotionModeData.MotionVectorMap.end() == itor)
		{
			return false;
		}
    
		ppMotionVector[0] = itor.second;
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool GetMotionVectorPointer(ushort wMotionMode, ushort wMotionIndex, TMotionVector[] c_ppMotionVector)
	{
		TMotionVector pMotionVector;
		if (!GetMotionVectorPointer(wMotionMode, wMotionIndex, pMotionVector))
		{
			return false;
		}
    
	//# Laniatus Games Studio Inc. | TODO TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'CopyFrom' method should be created:
	//Original Metin2 CPlus Line: *c_ppMotionVector = pMotionVector;
		c_ppMotionVector[0].CopyFrom(pMotionVector);
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __OLD_RegisterMotion(ushort wMotionMode, ushort wMotionIndex, in TMotion rMotion)
	{
		TMotionModeData pMotionModeData;
		if (!GetMotionModeDataPointer(wMotionMode, pMotionModeData))
		{
			TraceError("Failed getting motion mode data!");
			Debug.Assert(!"Failed getting motion mode data!");
			return;
		}
    
		TMotionVectorMap.iterator itor = pMotionModeData.MotionVectorMap.find(wMotionIndex);
		if (pMotionModeData.MotionVectorMap.end() == itor)
		{
			TMotionVector MotionVector = new TMotionVector();
			MotionVector.push_back(rMotion);
    
			pMotionModeData.MotionVectorMap.insert(TMotionVectorMap.value_type(wMotionIndex, MotionVector));
		}
		else
		{
			TMotionVector rMotionVector = itor.second;
			rMotionVector.push_back(rMotion);
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool GetComboDataPointer(ushort wMotionModeIndex, ushort wComboType, TComboData[] ppComboData)
	{
		TComboAttackDataIterator itor = m_ComboAttackDataMap.find((((uint)wMotionModeIndex << 16) | ((uint)wComboType)));
    
		if (m_ComboAttackDataMap.end() == itor)
		{
			return false;
		}
    
		ppComboData[0] = itor.second;
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool LoadRaceData(string c_szFileName)
	{
		CTextFileLoader TextFileLoader = new CTextFileLoader();
		if (!TextFileLoader.Load(c_szFileName))
		{
			return false;
		}
    
		TextFileLoader.SetTop();
    
		TextFileLoader.GetTokenString("basemodelfilename", m_strBaseModelFileName);
		TextFileLoader.GetTokenString("treefilename", m_strTreeFileName);
		TextFileLoader.GetTokenString("attributefilename", m_strAttributeFileName);
		TextFileLoader.GetTokenString("smokebonename", m_strSmokeBoneName);
		TextFileLoader.GetTokenString("motionlistfilename", m_strMotionListFileName);
    
		if (!m_strTreeFileName.empty())
		{
			CFileNameHelper.StringPath(m_strTreeFileName);
		}
    
		List<string> pSmokeTokenVector;
		if (TextFileLoader.GetTokenVector("smokefilename", pSmokeTokenVector))
		{
			if (pSmokeTokenVector.Count % 2 != 0)
			{
				TraceError("SmokeFileName ArgCount[%d]%2==0", pSmokeTokenVector.Count);
				return false;
			}
    
			uint uLineCount = (uint)(pSmokeTokenVector.Count / 2);
    
			for (uint uLine = 0; uLine < uLineCount; ++uLine)
			{
				int eSmoke = atoi(pSmokeTokenVector[uLine * 2 + 0]);
				if (eSmoke < 0 || eSmoke >= SMOKE_NUM)
				{
					TraceError("SmokeFileName SmokeNum[%d] OUT OF RANGE", eSmoke);
					return false;
				}
    
				string c_rstrEffectFileName = pSmokeTokenVector[uLine * 2 + 1];
    
	//# Laniatus Games Studio Inc. | TODO TASK: C# does not have an equivalent to references to value types:
	//Original Metin2 CPlus Line: uint& rdwCRCEft=m_adwSmokeEffectID[eSmoke];
				uint rdwCRCEft = m_adwSmokeEffectID[eSmoke];
				if (!CEffectManager.Instance().RegisterEffect2(c_rstrEffectFileName, rdwCRCEft))
				{
					TraceError("CRaceData::RegisterEffect2(%s) ERROR", c_rstrEffectFileName);
					rdwCRCEft = 0;
					return false;
				}
			}
		}
    
		if (TextFileLoader.SetChildNode("shapedata"))
		{
			string strPathName = "";
			uint dwShapeDataCount = 0;
			if (TextFileLoader.GetTokenString("pathname", strPathName) && TextFileLoader.GetTokenDoubleWord("shapedatacount", dwShapeDataCount))
			{
				for (uint LaniatusDefVariables = 0; LaniatusDefVariables < dwShapeDataCount; ++i)
				{
					if (!TextFileLoader.SetChildNode("shapedata", i))
					{
						continue;
					}
    
					TextFileLoader.GetTokenString("specialpath", strPathName);
    
					uint dwShapeIndex;
					if (!TextFileLoader.GetTokenDoubleWord("shapeindex", dwShapeIndex))
					{
						continue;
					}
    
					string strModel = "";
					if (TextFileLoader.GetTokenString("model", strModel))
					{
						SetShapeModel(dwShapeIndex, (strPathName + strModel).c_str());
					}
					else
					{
						if (!TextFileLoader.GetTokenString("local_model", strModel))
						{
							continue;
						}
    
						SetShapeModel(dwShapeIndex, strModel);
					}
    
					string strSourceSkin = "";
					string strTargetSkin = "";
    
					if (TextFileLoader.GetTokenString("local_sourceskin", strSourceSkin) && TextFileLoader.GetTokenString("local_targetskin", strTargetSkin))
					{
						AppendShapeSkin(dwShapeIndex, 0, strSourceSkin, strTargetSkin);
					}
    
					if (TextFileLoader.GetTokenString("sourceskin", strSourceSkin) && TextFileLoader.GetTokenString("targetskin", strTargetSkin))
					{
						AppendShapeSkin(dwShapeIndex, 0, (strPathName + strSourceSkin).c_str(), (strPathName + strTargetSkin).c_str());
					}
    
					if (TextFileLoader.GetTokenString("sourceskin2", strSourceSkin) && TextFileLoader.GetTokenString("targetskin2", strTargetSkin))
					{
						AppendShapeSkin(dwShapeIndex, 0, (strPathName + strSourceSkin).c_str(), (strPathName + strTargetSkin).c_str());
					}
    
					TextFileLoader.SetParentNode();
				}
			}
    
			TextFileLoader.SetParentNode();
		}
    
		if (TextFileLoader.SetChildNode("hairdata"))
		{
			string strPathName = "";
			uint dwHairDataCount = 0;
			if (TextFileLoader.GetTokenString("pathname", strPathName) && TextFileLoader.GetTokenDoubleWord("hairdatacount", dwHairDataCount))
			{
    
				for (uint LaniatusDefVariables = 0; LaniatusDefVariables < dwHairDataCount; ++i)
				{
					if (!TextFileLoader.SetChildNode("hairdata", i))
					{
						continue;
					}
    
					TextFileLoader.GetTokenString("specialpath", strPathName);
    
					uint dwShapeIndex;
					if (!TextFileLoader.GetTokenDoubleWord("hairindex", dwShapeIndex))
					{
						continue;
					}
    
					string strModel = "";
					string strSourceSkin = "";
					string strTargetSkin = "";
					if (TextFileLoader.GetTokenString("model", strModel) && TextFileLoader.GetTokenString("sourceskin", strSourceSkin) && TextFileLoader.GetTokenString("targetskin", strTargetSkin))
					{
						SetHairSkin(dwShapeIndex, 0, (strPathName + strModel).c_str(), (strPathName + strSourceSkin).c_str(), (strPathName + strTargetSkin).c_str());
					}
    
					TextFileLoader.SetParentNode();
				}
			}
    
			TextFileLoader.SetParentNode();
		}
    
    
		if (TextFileLoader.SetChildNode("attachingdata"))
		{
			if (!NRaceData.LoadAttachingData(TextFileLoader, m_AttachingDataVector))
			{
				return false;
			}
    
			TextFileLoader.SetParentNode();
		}
    
		return true;
	}
}