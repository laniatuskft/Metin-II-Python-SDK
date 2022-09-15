public class CArea
{
//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __SetObjectInstance(TObjectInstance pObjectInstance, TObjectData c_pData)
	{
		CProperty pProperty;
		if (!CPropertyManager.Instance().Get(c_pData.dwCRC, pProperty))
		{
			return;
		}
    
		string c_szPropertyType;
    
		if (!pProperty.GetString("PropertyType", c_szPropertyType))
		{
			return;
		}
    
		switch (prt.GetPropertyType(c_szPropertyType))
		{
			case prt.PROPERTY_TYPE_TREE:
				__SetObjectInstance_SetTree(pObjectInstance, c_pData, pProperty);
				break;
    
			case prt.PROPERTY_TYPE_BUILDING:
				__SetObjectInstance_SetBuilding(pObjectInstance, c_pData, pProperty);
				break;
    
			case prt.PROPERTY_TYPE_EFFECT:
				__SetObjectInstance_SetEffect(pObjectInstance, c_pData, pProperty);
				break;
    
			case prt.PROPERTY_TYPE_AMBIENCE:
				__SetObjectInstance_SetAmbience(pObjectInstance, c_pData, pProperty);
				break;
    
			case prt.PROPERTY_TYPE_DUNGEON_BLOCK:
				__SetObjectInstance_SetDungeonBlock(pObjectInstance, c_pData, pProperty);
				break;
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __SetObjectInstance_SetEffect(TObjectInstance pObjectInstance, TObjectData c_pData, CProperty pProperty)
	{
		prt.TPropertyEffect Data = new prt.TPropertyEffect();
		if (!prt.PropertyEffectStringToData(pProperty, Data))
		{
			return;
		}
    
		pObjectInstance.dwType = prt.PROPERTY_TYPE_EFFECT;
		pObjectInstance.dwEffectID = GetCaseCRC32(Data.strFileName.c_str(), Data.strFileName.size());
		CEffectManager rem = CEffectManager.Instance();
		CEffectData pData;
		if (!rem.GetEffectData(pObjectInstance.dwEffectID, pData))
		{
			if (!rem.RegisterEffect(Data.strFileName.c_str()))
			{
				pObjectInstance.dwEffectID = 0xffffffff;
				TraceError("CArea::SetEffect effect register error %s\n",Data.strFileName.c_str());
				return;
			}
		}
    
		CEffectInstance pEffectInstance;
		rem.CreateUnsafeEffectInstance(pObjectInstance.dwEffectID, pEffectInstance);
    
		_D3DMATRIX mat = new _D3DMATRIX();
		D3DXMatrixRotationYawPitchRoll(mat, ((c_pData.m_fYaw) * (((float) 3.141592654f) / 180.0f)), ((c_pData.m_fPitch) * (((float) 3.141592654f) / 180.0f)), ((c_pData.m_fRoll) * (((float) 3.141592654f) / 180.0f)));
    
		mat._41 = c_pData.Position.x;
		mat._42 = c_pData.Position.y;
		mat._43 = c_pData.Position.z + c_pData.m_fHeightBias;
    
		pEffectInstance.SetGlobalMatrix(mat);
    
		pObjectInstance.dwEffectInstanceIndex = m_EffectInstanceMap.size();
	//# Laniatus Games Studio Inc. | TODO TASK: The typedef 'TEffectInstanceMap' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
		m_EffectInstanceMap.insert(TEffectInstanceMap.value_type(pObjectInstance.dwEffectInstanceIndex, pEffectInstance));
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __SetObjectInstance_SetTree(TObjectInstance pObjectInstance, TObjectData c_pData, CProperty pProperty)
	{
		string c_szTreeName;
		if (!pProperty.GetString("TreeFile", c_szTreeName))
		{
			return;
		}
    
		pObjectInstance.SetTree(c_pData.Position.x, c_pData.Position.y, c_pData.Position.z + c_pData.m_fHeightBias, c_pData.dwCRC, c_szTreeName);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __SetObjectInstance_SetBuilding(TObjectInstance pObjectInstance, TObjectData c_pData, CProperty pProperty)
	{
		prt.TPropertyBuilding Data = new prt.TPropertyBuilding();
		if (!prt.PropertyBuildingStringToData(pProperty, Data))
		{
			return;
		}
    
		CResourceManager rkResMgr = CResourceManager.Instance();
    
		CGraphicThing pThing = (CGraphicThing)rkResMgr.GetResourcePointer(Data.strFileName.c_str());
		pThing.AddReference();
    
		if (pThing.IsEmpty())
		{
	#if DEBUG
			TraceError("CArea::SetBuilding: There is no data: %s", Data.strFileName.c_str());
	#endif
			return;
		}
    
		int iModelCount = pThing.GetModelCount();
		int iMotionCount = pThing.GetMotionCount();
    
		pObjectInstance.dwType = prt.PROPERTY_TYPE_BUILDING;
		pObjectInstance.pThingInstance = CGraphicThingInstance.New();
		pObjectInstance.pThingInstance.Initialize();
		pObjectInstance.pThingInstance.ReserveModelThing(iModelCount);
		pObjectInstance.pThingInstance.ReserveModelInstance(iModelCount);
		pObjectInstance.pThingInstance.RegisterModelThing(0, pThing);
		for (int j = 0; j < PORTAL_ID_MAX_NUM; ++j)
		{
			if (0 != c_pData.abyPortalID[j])
			{
				pObjectInstance.pThingInstance.SetPortal(j, c_pData.abyPortalID[j]);
			}
		}
    
		for (int LaniatusDefVariables = 0; LaniatusDefVariables < iModelCount; ++i)
		{
			pObjectInstance.pThingInstance.SetModelInstance(i, 0, i);
		}
    
		if (iMotionCount != 0)
		{
			pObjectInstance.pThingInstance.RegisterMotionThing(0, pThing);
		}
    
		pObjectInstance.pThingInstance.SetPosition(c_pData.Position.x, c_pData.Position.y, c_pData.Position.z + c_pData.m_fHeightBias);
		pObjectInstance.pThingInstance.SetRotation(c_pData.m_fYaw, c_pData.m_fPitch, c_pData.m_fRoll);
		pObjectInstance.isShadowFlag = Data.isShadowFlag;
		pObjectInstance.pThingInstance.RegisterBoundingSphere();
		__LoadAttribute(pObjectInstance, Data.strAttributeDataFileName.c_str());
		pThing.Release();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __SetObjectInstance_SetAmbience(TObjectInstance pObjectInstance, TObjectData c_pData, CProperty pProperty)
	{
		pObjectInstance.pAmbienceInstance = ms_AmbienceInstancePool.Alloc();
		 if (!prt.PropertyAmbienceStringToData(pProperty, pObjectInstance.pAmbienceInstance.AmbienceData))
		 {
			return;
		 }
    
		pObjectInstance.dwType = prt.PROPERTY_TYPE_AMBIENCE;
    
		TAmbienceInstance pAmbienceInstance = pObjectInstance.pAmbienceInstance;
		pAmbienceInstance.fx = c_pData.Position.x;
		pAmbienceInstance.fy = c_pData.Position.y;
		pAmbienceInstance.fz = c_pData.Position.z + c_pData.m_fHeightBias;
		pAmbienceInstance.dwRange = c_pData.dwRange;
		pAmbienceInstance.fMaxVolumeAreaPercentage = c_pData.fMaxVolumeAreaPercentage;
    
		if (0 == pAmbienceInstance.AmbienceData.strPlayType.compare("ONCE"))
		{
			pAmbienceInstance.Update = &TAmbienceInstance.UpdateOnceSound;
		}
		else if (0 == pAmbienceInstance.AmbienceData.strPlayType.compare("STEP"))
		{
			pAmbienceInstance.Update = &TAmbienceInstance.UpdateStepSound;
		}
		else if (0 == pAmbienceInstance.AmbienceData.strPlayType.compare("LOOP"))
		{
			pAmbienceInstance.Update = &TAmbienceInstance.UpdateLoopSound;
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __SetObjectInstance_SetDungeonBlock(TObjectInstance pObjectInstance, TObjectData c_pData, CProperty pProperty)
	{
		prt.TPropertyDungeonBlock Data = new prt.TPropertyDungeonBlock();
		if (!prt.PropertyDungeonBlockStringToData(pProperty, Data))
		{
			return;
		}
    
		pObjectInstance.dwType = prt.PROPERTY_TYPE_DUNGEON_BLOCK;
		pObjectInstance.pDungeonBlock = ms_DungeonBlockInstancePool.Alloc();
		pObjectInstance.pDungeonBlock.Load(Data.strFileName.c_str());
		pObjectInstance.pDungeonBlock.SetPosition(c_pData.Position.x, c_pData.Position.y, c_pData.Position.z + c_pData.m_fHeightBias);
		pObjectInstance.pDungeonBlock.SetRotation(c_pData.m_fYaw, c_pData.m_fPitch, c_pData.m_fRoll);
		pObjectInstance.pDungeonBlock.Update();
		pObjectInstance.pDungeonBlock.BuildBoundingSphere();
		pObjectInstance.pDungeonBlock.RegisterBoundingSphere();
		for (int j = 0; j < PORTAL_ID_MAX_NUM; ++j)
		{
			if (0 != c_pData.abyPortalID[j])
			{
				pObjectInstance.pDungeonBlock.SetPortal(j, c_pData.abyPortalID[j]);
			}
		}
		__LoadAttribute(pObjectInstance, Data.strAttributeDataFileName.c_str());
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __LoadAttribute(TObjectInstance pObjectInstance, string c_szAttributeFileName)
	{
		bool bFileExist = CResourceManager.Instance().IsFileExist(c_szAttributeFileName);
    
		CAttributeData pAttributeData = (CAttributeData) CResourceManager.Instance().GetResourcePointer(c_szAttributeFileName);
    
		CAttributeInstance pAttrInstance = ms_AttributeInstancePool.Alloc();
		pAttrInstance.Clear();
		pAttrInstance.SetObjectPointer(pAttributeData);
    
		if (false == bFileExist)
		{
			string attrFileName = c_szAttributeFileName;
			boost.algorithm.to_lower(attrFileName);
			bool bIsDungeonObject = (-1 != attrFileName.IndexOf("/dungeon/")) || (-1 != attrFileName.IndexOf("\\dungeon\\"));
    
			if (pAttributeData.IsEmpty() && false == bIsDungeonObject)
			{
				if (null != pObjectInstance && null != pObjectInstance.pThingInstance)
				{
					CGraphicThingInstance @object = pObjectInstance.pThingInstance;
    
					_D3DVECTOR v3Min = new _D3DVECTOR();
					_D3DVECTOR v3Max = new _D3DVECTOR();
    
					@object.GetBoundingAABB(v3Min, v3Max);
    
					CStaticCollisionData collision = new CStaticCollisionData();
					collision.dwType = COLLISION_TYPE_OBB;
					D3DXQuaternionRotationYawPitchRoll(collision.quatRotation, @object.GetYaw(), @object.GetPitch(), @object.GetRoll());
					strcpy(collision.szName, "DummyCollisionOBB");
					collision.v3Position = (v3Min + v3Max) * 0.5f;
    
					_D3DVECTOR vDelta = (v3Max - v3Min);
					collision.fDimensions[0] = vDelta.x * 0.5f;
					collision.fDimensions[1] = vDelta.y * 0.5f;
					collision.fDimensions[2] = vDelta.z * 0.5f;
    
					pAttributeData.AddCollisionData(collision);
				}
			}
		}
    
		if (!pAttributeData.IsEmpty())
		{
			pObjectInstance.pAttributeInstance = pAttrInstance;
		}
		else
		{
			pAttrInstance.Clear();
			ms_AttributeInstancePool.Free(pAttrInstance);
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool GetObjectDataPointer(uint dwIndex, TObjectData[] ppObjectData)
	{
		if (!CheckObjectIndex(dwIndex))
		{
			Debug.Assert(!"Setting Object Index is corrupted!");
			return false;
		}
    
		ppObjectData[0] = &m_ObjectDataVector[dwIndex];
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool GetObjectInstancePointer(in uint dwIndex, TObjectInstance[] ppObjectInstance)
	{
		if (dwIndex >= m_ObjectInstanceVector.size())
		{
			return false;
		}
    
		ppObjectInstance[0] = m_ObjectInstanceVector[dwIndex];
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __Clear_DestroyObjectInstance(TObjectInstance pObjectInstance)
	{
		if (pObjectInstance.dwEffectInstanceIndex != 0xffffffff)
		{
			TEffectInstanceIterator f = m_EffectInstanceMap.find(pObjectInstance.dwEffectInstanceIndex);
			if (m_EffectInstanceMap.end() != f)
			{
				CEffectInstance pEffectInstance = f.second;
				m_EffectInstanceMap.erase(f);
    
				if (CEffectManager.InstancePtr())
				{
					CEffectManager.Instance().DestroyUnsafeEffectInstance(pEffectInstance);
				}
			}
			pObjectInstance.dwEffectInstanceIndex = 0xffffffff;
		}
    
		if (pObjectInstance.pAttributeInstance)
		{
			pObjectInstance.pAttributeInstance.Clear();
			ms_AttributeInstancePool.Free(pObjectInstance.pAttributeInstance);
			pObjectInstance.pAttributeInstance = null;
		}
    
		if (pObjectInstance.pTree)
		{
			pObjectInstance.pTree.Clear();
			CSpeedTreeForestDirectX8.Instance().DeleteInstance(pObjectInstance.pTree);
			pObjectInstance.pTree = null;
		}
    
		if (pObjectInstance.pThingInstance)
		{
			CGraphicThingInstance.Delete(pObjectInstance.pThingInstance);
			pObjectInstance.pThingInstance = null;
		}
    
		if (pObjectInstance.pAmbienceInstance)
		{
			ms_AmbienceInstancePool.Free(pObjectInstance.pAmbienceInstance);
			pObjectInstance.pAmbienceInstance = null;
		}
    
		if (pObjectInstance.pDungeonBlock)
		{
			ms_DungeonBlockInstancePool.Free(pObjectInstance.pDungeonBlock);
			pObjectInstance.pDungeonBlock = null;
		}
    
		pObjectInstance.Clear();
    
		ms_ObjectInstancePool.Free(pObjectInstance);
	}
}