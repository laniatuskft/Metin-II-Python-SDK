public class CActorInstance
{
//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public uint AttachSmokeEffect(uint eSmoke)
	{
		if (!m_pkCurRaceData)
		{
			return 0;
		}
    
		uint dwSmokeEffectID = m_pkCurRaceData.GetSmokeEffectID(eSmoke);
    
		return AttachEffectByID(0, m_pkCurRaceData.GetSmokeBone().c_str(), dwSmokeEffectID);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool __IsLeftHandWeapon(uint type)
	{
		if (CItemData.WEAPON_DAGGER == type || (CItemData.WEAPON_FAN == type && __IsMountingHorse()))
		{
			return true;
		}
		else if (CItemData.WEAPON_BOW == type)
		{
			return true;
		}
	#if ENABLE_WOLFMAN
		else if (CItemData.WEAPON_CLAW == type)
		{
			return true;
		}
	#endif
		else
		{
			return false;
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool __IsRightHandWeapon(uint type)
	{
		if (CItemData.WEAPON_DAGGER == type || (CItemData.WEAPON_FAN == type && __IsMountingHorse()))
		{
			return true;
		}
		else if (CItemData.WEAPON_BOW == type)
		{
			return false;
		}
	#if ENABLE_WOLFMAN
		else if (CItemData.WEAPON_CLAW == type)
		{
			return true;
		}
	#endif
		else
		{
			return true;
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool __IsWeaponTrace(uint weaponType)
	{
		switch (weaponType)
		{
		case CItemData.WEAPON_BELL:
		case CItemData.WEAPON_FAN:
		case CItemData.WEAPON_BOW:
			return false;
		default:
			return true;
    
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void AttachWeapon(uint dwItemIndex, uint dwParentPartIndex, uint dwPartIndex)
	{
		if (dwPartIndex >= CRaceData.PART_MAX_NUM)
		{
			return;
		}
    
		m_adwPartItemID[dwPartIndex] = dwItemIndex;
    
		if (USE_VIETNAM_CONVERT_WEAPON_VNUM)
		{
			dwItemIndex = Vietnam_ConvertWeaponVnum(dwItemIndex);
		}
    
		CItemData pItemData;
		if (!CItemManager.Instance().GetItemDataPointer(dwItemIndex, pItemData))
		{
			RegisterModelThing(dwPartIndex, null);
			SetModelInstance(dwPartIndex, dwPartIndex, 0);
    
			RegisterModelThing(CRaceData.PART_WEAPON_LEFT, null);
			SetModelInstance(CRaceData.PART_WEAPON_LEFT, CRaceData.PART_WEAPON_LEFT, 0);
    
			RefreshActorInstance();
			return;
		}
    
		__DestroyWeaponTrace();
    
		if (__IsRightHandWeapon(pItemData.GetWeaponType()))
		{
			AttachWeapon(dwParentPartIndex, CRaceData.PART_WEAPON, pItemData);
		}
		if (__IsLeftHandWeapon(pItemData.GetWeaponType()))
		{
			AttachWeapon(dwParentPartIndex, CRaceData.PART_WEAPON_LEFT, pItemData);
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void AttachAcce(uint dwParentPartIndex, uint dwPartIndex, CItemData pItemData)
	{
		if (pItemData == null)
		{
			return;
		}
    
    
		if (CRaceData.PART_ACCE == dwPartIndex)
		{
			RegisterModelThing(CRaceData.PART_ACCE, pItemData.GetSubModelThing());
		}
		else
		{
			RegisterModelThing(dwPartIndex, pItemData.GetModelThing());
		}
    
		SetModelInstance(dwPartIndex, dwPartIndex, 0);
    
		AttachModelInstance(dwParentPartIndex, "Bip01 Spine2", dwPartIndex);
    
		SMaterialData kMaterialData = new SMaterialData();
		kMaterialData.pImage = null;
		kMaterialData.isSpecularEnable = true;
		kMaterialData.fSpecularPower = pItemData.GetSpecularPowerf();
		kMaterialData.bSphereMapIndex = 1;
		SetMaterialData(dwPartIndex, null, kMaterialData);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void AttachAcce(uint dwItemIndex, uint dwParentPartIndex, uint dwPartIndex)
	{
    
		if (dwPartIndex >= CRaceData.PART_MAX_NUM)
		{
			return;
		}
    
		m_adwPartItemID[dwPartIndex] = dwItemIndex;
    
    
		CItemData pItemData;
		if (!CItemManager.Instance().GetItemDataPointer(dwItemIndex, pItemData) || dwItemIndex == 0)
		{
			RegisterModelThing(dwPartIndex, null);
			SetModelInstance(dwPartIndex, dwPartIndex, 0);
    
			RegisterModelThing(CRaceData.PART_ACCE, null);
			SetModelInstance(CRaceData.PART_ACCE, CRaceData.PART_ACCE, 0);
    
			RefreshActorInstance();
			return;
		}
    
		AttachAcce(dwParentPartIndex, CRaceData.PART_ACCE, pItemData);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool GetAttachingBoneName(uint dwPartIndex, string[] c_pszBoneName)
	{
		return m_pkCurRaceData.GetAttachingBoneName(dwPartIndex, c_pszBoneName);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void AttachWeapon(uint dwParentPartIndex, uint dwPartIndex, CItemData pItemData)
	{
		if (pItemData == null)
		{
			return;
		}
    
		string szBoneName;
		if (!GetAttachingBoneName(dwPartIndex, szBoneName))
		{
			return;
		}
    
		if (CRaceData.PART_WEAPON_LEFT == dwPartIndex)
		{
			RegisterModelThing(dwPartIndex, pItemData.GetSubModelThing());
		}
		else
		{
			RegisterModelThing(dwPartIndex, pItemData.GetModelThing());
		}
    
		SetModelInstance(dwPartIndex, dwPartIndex, 0);
		AttachModelInstance(dwParentPartIndex, szBoneName, dwPartIndex);
    
		if (USE_WEAPON_SPECULAR)
		{
			SMaterialData kMaterialData = new SMaterialData();
			kMaterialData.pImage = null;
			kMaterialData.isSpecularEnable = true;
			kMaterialData.fSpecularPower = pItemData.GetSpecularPowerf();
			kMaterialData.bSphereMapIndex = 1;
			SetMaterialData(dwPartIndex, null, kMaterialData);
		}
    
		if (__IsWeaponTrace(pItemData.GetWeaponType()))
		{
			CWeaponTrace pWeaponTrace = CWeaponTrace.New();
			pWeaponTrace.SetWeaponInstance(this, dwPartIndex, szBoneName);
			m_WeaponTraceVector.push_back(pWeaponTrace);
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void DettachEffect(uint dwEID)
	{
		LinkedList<TAttachingEffect>.Enumerator LaniatusDefVariables = m_AttachingEffectList.begin();
    
		while (i.MoveNext())
		{
			TAttachingEffect rkAttEft = i.Current;
    
			if (rkAttEft.dwEffectIndex == dwEID)
			{
				i = m_AttachingEffectList.erase(i);
				CEffectManager.Instance().DestroyEffectInstance(dwEID);
			}
			else
			{
			}
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public uint AttachEffectByName(uint dwParentPartIndex, string c_pszBoneName, string c_pszEffectName)
	{
		string str = "";
		uint dwCRC;
		StringPath(c_pszEffectName, ref str);
		dwCRC = GetCaseCRC32(str, str.Length);
    
		return AttachEffectByID(dwParentPartIndex, c_pszBoneName, dwCRC);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public uint AttachEffectByID(uint dwParentPartIndex, string c_pszBoneName, uint dwEffectID, _D3DVECTOR c_pv3Position, float fParticleScale, _D3DVECTOR c_pv3MeshScale)
	{
		TAttachingEffect ae = new TAttachingEffect();
		ae.iLifeType = EFFECT_LIFE_INFINITE;
		ae.dwEndTime = 0;
		ae.dwModelIndex = dwParentPartIndex;
		ae.dwEffectIndex = CEffectManager.Instance().GetEmptyIndex();
		ae.isAttaching = true;
		if (c_pv3Position != null)
		{
			D3DXMatrixTranslation(ae.matTranslation, c_pv3Position.x, c_pv3Position.y, c_pv3Position.z);
		}
		else
		{
			D3DXMatrixIdentity(ae.matTranslation);
		}
		CEffectManager rkEftMgr = CEffectManager.Instance();
		if (c_pv3MeshScale != null)
		{
			rkEftMgr.CreateEffectInstance(ae.dwEffectIndex, dwEffectID, fParticleScale, c_pv3MeshScale);
		}
		else
		{
			rkEftMgr.CreateEffectInstance(ae.dwEffectIndex, dwEffectID, fParticleScale);
		}
    
		if (c_pszBoneName != '\0')
		{
			int iBoneIndex;
			if (!FindBoneIndex(dwParentPartIndex, c_pszBoneName, iBoneIndex))
			{
				ae.iBoneIndex = -1;
			}
			else
			{
				ae.iBoneIndex = iBoneIndex;
			}
		}
		else
		{
			ae.iBoneIndex = -1;
		}
    
		m_AttachingEffectList.push_back(ae);
    
		return ae.dwEffectIndex;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void RefreshActorInstance()
	{
		if (!m_pkCurRaceData)
		{
			TraceError("void CActorInstance::RefreshActorInstance() - m_pkCurRaceData=NULL");
			return;
		}
    
		m_BodyPointInstanceList.clear();
		m_DefendingPointInstanceList.clear();
    
		for (uint LaniatusDefVariables = 0; LaniatusDefVariables < m_pkCurRaceData.GetAttachingDataCount(); ++i)
		{
			NRaceData.TAttachingData c_pAttachingData;
    
			if (!m_pkCurRaceData.GetAttachingDataPointer(i, c_pAttachingData))
			{
				continue;
			}
    
			switch (c_pAttachingData.dwType)
			{
				case NRaceData.ATTACHING_DATA_TYPE_COLLISION_DATA:
				{
					NRaceData.TCollisionData c_pCollisionData = c_pAttachingData.pCollisionData;
    
					TCollisionPointInstance PointInstance = new TCollisionPointInstance();
					if (NRaceData.COLLISION_TYPE_ATTACKING == c_pCollisionData.iCollisionType)
					{
						continue;
					}
    
					if (!CreateCollisionInstancePiece(CRaceData.PART_MAIN, c_pAttachingData, PointInstance))
					{
						continue;
					}
    
					switch (c_pCollisionData.iCollisionType)
					{
						case NRaceData.COLLISION_TYPE_ATTACKING:
							break;
						case NRaceData.COLLISION_TYPE_DEFENDING:
							m_DefendingPointInstanceList.push_back(PointInstance);
							break;
						case NRaceData.COLLISION_TYPE_BODY:
							m_BodyPointInstanceList.push_back(PointInstance);
							break;
					}
				}
				break;
    
				case NRaceData.ATTACHING_DATA_TYPE_EFFECT:
					if (c_pAttachingData.isAttaching)
					{
						AttachEffectByName(0, c_pAttachingData.strAttachingBoneName.c_str(), c_pAttachingData.pEffectData.strFileName.c_str());
					}
					else
					{
						AttachEffectByName(0, 0, c_pAttachingData.pEffectData.strFileName.c_str());
					}
					break;
    
				case NRaceData.ATTACHING_DATA_TYPE_OBJECT:
					break;
    
				default:
					Debug.Assert(false);
					break;
			}
		}
    
		for (uint j = 0; j < CRaceData.PART_MAX_NUM; ++j)
		{
			if (0 == m_adwPartItemID[j])
			{
				continue;
			}
    
			CItemData pItemData;
			if (!CItemManager.Instance().GetItemDataPointer(m_adwPartItemID[j], pItemData))
			{
				return;
			}
    
			for (uint k = 0; k < pItemData.GetAttachingDataCount(); ++k)
			{
				NRaceData.TAttachingData c_pAttachingData;
    
				if (!pItemData.GetAttachingDataPointer(k, c_pAttachingData))
				{
					continue;
				}
    
				switch (c_pAttachingData.dwType)
				{
					case NRaceData.ATTACHING_DATA_TYPE_COLLISION_DATA:
					{
							NRaceData.TCollisionData c_pCollisionData = c_pAttachingData.pCollisionData;
    
							TCollisionPointInstance PointInstance = new TCollisionPointInstance();
							if (NRaceData.COLLISION_TYPE_ATTACKING == c_pCollisionData.iCollisionType)
							{
								continue;
							}
							if (!CreateCollisionInstancePiece(j, c_pAttachingData, PointInstance))
							{
								continue;
							}
    
							switch (c_pCollisionData.iCollisionType)
							{
							case NRaceData.COLLISION_TYPE_ATTACKING:
								break;
							case NRaceData.COLLISION_TYPE_DEFENDING:
								m_DefendingPointInstanceList.push_back(PointInstance);
								break;
							case NRaceData.COLLISION_TYPE_BODY:
								m_BodyPointInstanceList.push_back(PointInstance);
								break;
							}
					}
						break;
    
					case NRaceData.ATTACHING_DATA_TYPE_EFFECT:
						if (!m_bEffectInitialized)
						{
							uint dwCRC;
							StringPath(ref c_pAttachingData.pEffectData.strFileName);
							dwCRC = GetCaseCRC32(c_pAttachingData.pEffectData.strFileName.c_str(), c_pAttachingData.pEffectData.strFileName.length());
    
							TAttachingEffect ae = new TAttachingEffect();
							ae.iLifeType = EFFECT_LIFE_INFINITE;
							ae.dwEndTime = 0;
							ae.dwModelIndex = j;
							ae.dwEffectIndex = CEffectManager.Instance().GetEmptyIndex();
							ae.isAttaching = true;
							CEffectManager.Instance().CreateEffectInstance(ae.dwEffectIndex, dwCRC);
    
							int iBoneIndex;
							if (!FindBoneIndex(j, c_pAttachingData.strAttachingBoneName.c_str(), iBoneIndex))
							{
								Tracef("Cannot get Bone Index\n");
								Debug.Assert(false);
							}
							Tracef("Creating %p %d %d\n", this, j,k);
    
							ae.iBoneIndex = iBoneIndex;
    
							m_AttachingEffectList.push_back(ae);
						}
						break;
    
					case NRaceData.ATTACHING_DATA_TYPE_OBJECT:
						break;
    
					default:
						Debug.Assert(false);
						break;
				}
			}
		}
    
		m_bEffectInitialized = true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetWeaponTraceTexture(string szTextureName)
	{
		List<CWeaponTrace>.Enumerator it;
		for (it = m_WeaponTraceVector.begin(); it.MoveNext();)
		{
			it.Current.SetTexture(szTextureName);
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void UseTextureWeaponTrace()
	{
		for_each(m_WeaponTraceVector.begin(), m_WeaponTraceVector.end(), std::mem_fn(CWeaponTrace.UseTexture));
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void UseAlphaWeaponTrace()
	{
		for_each(m_WeaponTraceVector.begin(), m_WeaponTraceVector.end(), std::mem_fn(CWeaponTrace.UseAlpha));
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void UpdateAttachingInstances()
	{
		CEffectManager rkEftMgr = CEffectManager.Instance();
    
		LinkedList<TAttachingEffect>.Enumerator it;
		uint dwCurrentTime = CTimer.Instance().GetCurrentMillisecond();
		for (it = m_AttachingEffectList.begin(); it.MoveNext();)
		{
			if (EFFECT_LIFE_WITH_MOTION == it.iLifeType)
			{
				continue;
			}
    
			if ((EFFECT_LIFE_NORMAL == it.iLifeType && it.dwEndTime < dwCurrentTime) || !rkEftMgr.IsAliveEffect(it.dwEffectIndex))
			{
				rkEftMgr.DestroyEffectInstance(it.dwEffectIndex);
				it = m_AttachingEffectList.erase(it);
			}
			else
			{
				if (it.isAttaching)
				{
					rkEftMgr.SelectEffectInstance(it.dwEffectIndex);
    
					if (it.iBoneIndex == -1)
					{
						_D3DMATRIX matTransform = new _D3DMATRIX();
						matTransform = it.matTranslation;
						matTransform *= m_worldMatrix;
						rkEftMgr.SetEffectInstanceGlobalMatrix(matTransform);
					}
					else
					{
						_D3DMATRIX pBoneMat;
						if (GetBoneMatrix(it.dwModelIndex, it.iBoneIndex, pBoneMat))
						{
							_D3DMATRIX matTransform = new _D3DMATRIX();
	//# Laniatus Games Studio Inc. | TODO TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'CopyFrom' method should be created:
	//Original Metin2 CPlus Line: matTransform = *pBoneMat;
							matTransform.CopyFrom(pBoneMat);
							matTransform *= it.matTranslation;
							matTransform *= m_worldMatrix;
							rkEftMgr.SetEffectInstanceGlobalMatrix(matTransform);
						}
						else
						{
						}
					}
				}
    
			}
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void ShowAllAttachingEffect()
	{
		LinkedList<TAttachingEffect>.Enumerator it;
		for (it = m_AttachingEffectList.begin(); it.MoveNext();)
		{
			CEffectManager.Instance().SelectEffectInstance(it.dwEffectIndex);
			CEffectManager.Instance().ShowEffect();
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void HideAllAttachingEffect()
	{
		LinkedList<TAttachingEffect>.Enumerator it;
		for (it = m_AttachingEffectList.begin(); it.MoveNext();)
		{
			CEffectManager.Instance().SelectEffectInstance(it.dwEffectIndex);
			CEffectManager.Instance().HideEffect();
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __ClearAttachingEffect()
	{
		m_bEffectInitialized = false;
    
		LinkedList<TAttachingEffect>.Enumerator it;
		for (it = m_AttachingEffectList.begin(); it.MoveNext();)
		{
			CEffectManager.Instance().DestroyEffectInstance(it.dwEffectIndex);
		}
		m_AttachingEffectList.clear();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetQuiverEquipped(bool bEquipped)
	{
		m_bIsQuiverEquipped = bEquipped;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetQuiverEffectID(uint dwEffectID)
	{
		m_dwQuiverEffectID = dwEffectID;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetBattleHitEffect(uint dwID)
	{
		m_dwBattleHitEffectID = dwID;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetBattleAttachEffect(uint dwID)
	{
		m_dwBattleAttachEffectID = dwID;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool CanAct()
	{
		if (IsDead())
		{
			return false;
		}
    
		if (IsStun())
		{
			return false;
		}
    
		if (IsParalysis())
		{
			return false;
		}
    
		if (IsFaint())
		{
			return false;
		}
    
		if (IsSleep())
		{
			return false;
		}
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool CanUseSkill()
	{
		if (!CanAct())
		{
			return false;
		}
    
		uint dwCurMotionIndex = __GetCurrentMotionIndex();
    
		switch (dwCurMotionIndex)
		{
			case CRaceMotionData.NAME_FISHING_THROW:
			case CRaceMotionData.NAME_FISHING_WAIT:
			case CRaceMotionData.NAME_FISHING_STOP:
			case CRaceMotionData.NAME_FISHING_REACT:
			case CRaceMotionData.NAME_FISHING_CATCH:
			case CRaceMotionData.NAME_FISHING_FAIL:
				return true;
				break;
		}
    
		if (IsUsingSkill())
		{
			if (m_pkCurRaceMotionData.IsCancelEnableSkill())
			{
				return true;
			}
    
			return false;
		}
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool CanMove()
	{
		if (!CanAct())
		{
			return false;
		}
    
		if (isLock())
		{
			return false;
		}
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool CanAttack()
	{
		if (!CanAct())
		{
			return false;
		}
    
		if (IsUsingSkill())
		{
			if (!CanCancelSkill())
			{
				return false;
			}
		}
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool CanFishing()
	{
		if (!CanAct())
		{
			return false;
		}
    
		if (IsUsingSkill())
		{
			return false;
		}
    
		switch (__GetCurrentMotionIndex())
		{
			case CRaceMotionData.NAME_WAIT:
			case CRaceMotionData.NAME_WALK:
			case CRaceMotionData.NAME_RUN:
				break;
			default:
				return false;
				break;
		}
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool IsClickableDistanceDestInstance(CActorInstance rkInstDst, float fDistance)
	{
		TPixelPosition kPPosSrc = new TPixelPosition();
		GetPixelPosition(kPPosSrc);
    
		_D3DVECTOR kD3DVct3Src = new _D3DVECTOR(kPPosSrc);
    
		TCollisionPointInstanceList rkLstkDefPtInst = rkInstDst.m_DefendingPointInstanceList;
		TCollisionPointInstanceList.iterator LaniatusDefVariables = new TCollisionPointInstanceList.iterator();
    
		for (i = rkLstkDefPtInst.begin(); LaniatusDefVariables != rkLstkDefPtInst.end(); ++i)
		{
			List<CDynamicSphereInstance> rkVctkDefSphere = i.SphereInstanceVector;
    
			List<CDynamicSphereInstance>.Enumerator j;
			for (j = rkVctkDefSphere.GetEnumerator(); j.MoveNext();)
			{
				CDynamicSphereInstance rkSphere = j.Current;
    
				float fMovDistance = D3DXVec3Length(D3DXVECTOR3(rkSphere.v3Position - kD3DVct3Src));
				float fAtkDistance = rkSphere.fRadius + fDistance;
    
				if (fAtkDistance > fMovDistance)
				{
					return true;
				}
			}
		}
    
		return false;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void InputNormalAttackCommand(float fDirRot)
	{
		if (!__CanInputNormalAttackCommand())
		{
			return;
		}
    
		m_fAtkDirRot = fDirRot;
		NormalAttack(m_fAtkDirRot);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool InputComboAttackCommand(float fDirRot)
	{
		m_fAtkDirRot = fDirRot;
    
		if (m_isPreInput)
		{
			return false;
		}
    
		  if (0 == m_dwcurComboIndex)
		  {
			 __RunNextCombo();
			return true;
		  }
		else if (m_pkCurRaceMotionData.IsComboInputTimeData())
		{
			 float fElapsedTime = GetAttackingElapsedTime();
    
			if (fElapsedTime > m_pkCurRaceMotionData.GetComboInputEndTime())
			{
				if (IsBowMode())
				{
					m_isNextPreInput = true;
				}
				return false;
			}
    
			if (fElapsedTime > m_pkCurRaceMotionData.GetNextComboTime())
			{
				__RunNextCombo();
				return true;
			}
			else if (fElapsedTime > m_pkCurRaceMotionData.GetComboInputStartTime())
			{
				m_isPreInput = true;
				return false;
			}
		}
		else
		{
			float fElapsedTime = GetAttackingElapsedTime();
			if (fElapsedTime > m_pkCurRaceMotionData.GetMotionDuration() * 0.9f)
			{
				__RunNextCombo();
				return true;
			}
		}
    
		return false;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void ComboProcess()
	{
		if (0 != m_dwcurComboIndex)
		{
			if (!m_pkCurRaceMotionData)
			{
				Tracef("Attacking motion data is NULL! : %d\n", m_dwcurComboIndex);
				__ClearCombo();
				return;
			}
    
			float fElapsedTime = GetAttackingElapsedTime();
    
			if (m_isPreInput)
			{
				if (fElapsedTime > m_pkCurRaceMotionData.GetNextComboTime())
				{
					  __RunNextCombo();
					m_isPreInput = false;
    
					return;
				}
			}
		}
		else
		{
			m_isPreInput = false;
    
			if (!IsUsingSkill())
			{
			if (m_isNextPreInput)
			{
				__RunNextCombo();
				m_isNextPreInput = false;
			}
			}
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __RunNextCombo()
	{
		 ++m_dwcurComboIndex;
    
		ushort wComboIndex = m_dwcurComboIndex;
		ushort wComboType = __GetCurrentComboType();
    
		if (wComboIndex == 0)
		{
			TraceError("CActorInstance::__RunNextCombo(wComboType=%d, wComboIndex=%d)", wComboType, wComboIndex);
			return;
		}
    
		uint dwComboArrayIndex = (uint)(wComboIndex - 1);
    
		SComboAttackData pComboData;
    
		if (!m_pkCurRaceData.GetComboDataPointer(m_wcurMotionMode, wComboType, pComboData))
		{
			TraceError("CActorInstance::__RunNextCombo(wComboType=%d, wComboIndex=%d) - m_pkCurRaceData->GetComboDataPointer(m_wcurMotionMode=%d, &pComboData) == NULL", wComboType, wComboIndex, m_wcurMotionMode);
			return;
		}
    
		if (dwComboArrayIndex >= pComboData.ComboIndexVector.size())
		{
			TraceError("CActorInstance::__RunNextCombo(wComboType=%d, wComboIndex=%d) - (dwComboArrayIndex=%d) >= (pComboData->ComboIndexVector.size()=%d)", wComboType, wComboIndex, dwComboArrayIndex, pComboData.ComboIndexVector.size());
			return;
		}
    
		ushort wcurComboMotionIndex = pComboData.ComboIndexVector[dwComboArrayIndex];
		ComboAttack(wcurComboMotionIndex, m_fAtkDirRot, 0.1f);
    
		if (m_dwcurComboIndex == pComboData.ComboIndexVector.size())
		{
			__OnEndCombo();
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __OnEndCombo()
	{
		if (__IsMountingHorse())
		{
			m_dwcurComboIndex = 1;
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __ClearCombo()
	{
		m_dwcurComboIndex = 0;
		m_isPreInput = false;
		m_pkCurRaceMotionData = null;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool isAttacking()
	{
		if (isNormalAttacking())
		{
			return true;
		}
    
		if (isComboAttacking())
		{
			return true;
		}
    
		if (IsSplashAttacking())
		{
			return true;
		}
    
		return false;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool isValidAttacking()
	{
		if (!m_pkCurRaceMotionData)
		{
			return false;
		}
    
		if (!m_pkCurRaceMotionData.isAttackingMotion())
		{
			return false;
		}
    
		NRaceData.TMotionAttackData c_pData = m_pkCurRaceMotionData.GetMotionAttackDataPointer();
		float fElapsedTime = GetAttackingElapsedTime();
		NRaceData.THitDataContainer.const_iterator itor = c_pData.HitDataContainer.begin();
		for (; itor != c_pData.HitDataContainer.end(); ++itor)
		{
	//# Laniatus Games Studio Inc. | TODO TASK: C# does not have an equivalent to references to variables:
	//Original Metin2 CPlus Line: const NRaceData::THitData & c_rHitData = *itor;
			NRaceData.THitData c_rHitData = *itor;
			if (fElapsedTime > c_rHitData.fAttackStartTime && fElapsedTime < c_rHitData.fAttackEndTime)
			{
				return true;
			}
		}
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool CanCheckAttacking()
	{
		if (isAttacking())
		{
			return true;
		}
    
		return false;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool __IsInSplashTime()
	{
		if (m_kSplashArea.fDisappearingTime > GetLocalTime())
		{
			return true;
		}
    
		return false;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool isNormalAttacking()
	{
		if (!m_pkCurRaceMotionData)
		{
			return false;
		}
    
		if (!m_pkCurRaceMotionData.isAttackingMotion())
		{
			return false;
		}
    
		NRaceData.TMotionAttackData c_pData = m_pkCurRaceMotionData.GetMotionAttackDataPointer();
		if (NRaceData.MOTION_TYPE_NORMAL != c_pData.iMotionType)
		{
			return false;
		}
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool isComboAttacking()
	{
		if (!m_pkCurRaceMotionData)
		{
			return false;
		}
    
		if (!m_pkCurRaceMotionData.isAttackingMotion())
		{
			return false;
		}
    
		NRaceData.TMotionAttackData c_pData = m_pkCurRaceMotionData.GetMotionAttackDataPointer();
		if (NRaceData.MOTION_TYPE_COMBO != c_pData.iMotionType)
		{
			return false;
		}
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool IsSplashAttacking()
	{
		if (!m_pkCurRaceMotionData)
		{
			return false;
		}
    
		if (m_pkCurRaceMotionData.HasSplashMotionEvent())
		{
			return true;
		}
    
		return false;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool __IsMovingSkill(ushort wSkillNumber)
	{
		const int HORSE_DASH_SKILL_NUMBER = 137;
    
		return HORSE_DASH_SKILL_NUMBER == wSkillNumber;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool IsActEmotion()
	{
		uint dwCurMotionIndex = __GetCurrentMotionIndex();
		switch (dwCurMotionIndex)
		{
			case CRaceMotionData.NAME_FRENCH_KISS_START + 0:
			case CRaceMotionData.NAME_FRENCH_KISS_START + 1:
			case CRaceMotionData.NAME_FRENCH_KISS_START + 2:
			case CRaceMotionData.NAME_FRENCH_KISS_START + 3:
	#if ENABLE_WOLFMAN
	//# Laniatus Games Studio Inc. | TODO TASK: C# does not allow fall-through from a non-empty 'case':
			case CRaceMotionData.NAME_FRENCH_KISS_START + 4:
	#endif
	//# Laniatus Games Studio Inc. | TODO TASK: C# does not allow fall-through from a non-empty 'case':
			case CRaceMotionData.NAME_KISS_START + 0:
			case CRaceMotionData.NAME_KISS_START + 1:
			case CRaceMotionData.NAME_KISS_START + 2:
			case CRaceMotionData.NAME_KISS_START + 3:
	#if ENABLE_WOLFMAN
	//# Laniatus Games Studio Inc. | TODO TASK: C# does not allow fall-through from a non-empty 'case':
			case CRaceMotionData.NAME_KISS_START + 4:
	#endif
				return true;
				break;
		}
    
		return false;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool IsUsingMovingSkill()
	{
		return __IsMovingSkill(m_kCurMotNode.uSkill);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public uint GetComboIndex()
	{
		return m_dwcurComboIndex;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public float GetAttackingElapsedTime()
	{
		return (GetLocalTime() - m_kCurMotNode.fStartTime) * m_kCurMotNode.fSpeedRatio;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool __CanInputNormalAttackCommand()
	{
		if (IsWaiting())
		{
			return true;
		}
    
		if (isNormalAttacking())
		{
			float fElapsedTime = GetAttackingElapsedTime();
    
			if (fElapsedTime > m_pkCurRaceMotionData.GetMotionDuration() * 0.9f)
			{
				return true;
			}
		}
    
		return false;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool NormalAttack(float fDirRot, float fBlendTime)
	{
		ushort wMotionIndex;
		if (!m_pkCurRaceData.GetNormalAttackIndex(m_wcurMotionMode, wMotionIndex))
		{
			return false;
		}
    
		BlendRotation(fDirRot, fBlendTime);
		SetAdvancingRotation(fDirRot);
		InterceptOnceMotion(wMotionIndex, 0.1f, 0, __GetAttackSpeed());
    
		__OnAttack(wMotionIndex);
    
		NEW_SetAtkPixelPosition(NEW_GetCurPixelPositionRef());
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool ComboAttack(uint dwMotionIndex, float fDirRot, float fBlendTime)
	{
		BlendRotation(fDirRot, fBlendTime);
		SetAdvancingRotation(fDirRot);
    
		InterceptOnceMotion(dwMotionIndex, fBlendTime, 0, __GetAttackSpeed());
    
		__OnAttack(dwMotionIndex);
    
		NEW_SetAtkPixelPosition(NEW_GetCurPixelPositionRef());
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __ProcessMotionEventAttackSuccess(uint dwMotionKey, byte byEventIndex, CActorInstance rVictim)
	{
		CRaceMotionData pMotionData;
    
		if (!m_pkCurRaceData.GetMotionDataPointer(dwMotionKey, pMotionData))
		{
			return;
		}
    
		if (byEventIndex >= pMotionData.GetMotionEventDataCount())
		{
			return;
		}
    
		NMotionEvent.SMotionEventDataAttack pMotionEventData;
		if (!pMotionData.GetMotionAttackingEventDataPointer(byEventIndex, pMotionEventData))
		{
			return;
		}
    
		_D3DVECTOR c_rv3VictimPos = rVictim.GetPositionVectorRef();
		__ProcessDataAttackSuccess(pMotionEventData.AttackData, rVictim, c_rv3VictimPos);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __ProcessMotionAttackSuccess(uint dwMotionKey, CActorInstance rVictim)
	{
		CRaceMotionData c_pMotionData;
    
		if (!m_pkCurRaceData.GetMotionDataPointer(dwMotionKey, c_pMotionData))
		{
			return;
		}
    
		_D3DVECTOR c_rv3VictimPos = rVictim.GetPositionVectorRef();
		__ProcessDataAttackSuccess(c_pMotionData.GetMotionAttackDataReference(), rVictim, c_rv3VictimPos);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public uint __GetOwnerVID()
	{
		return m_dwOwnerVID;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public float __GetOwnerTime()
	{
		return GetLocalTime() - m_fOwnerBaseTime;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool __CanPushDestActor(CActorInstance rkActorDst)
	{
		if (rkActorDst.IsBuilding())
		{
			return false;
		}
    
		if (rkActorDst.IsDoor())
		{
			return false;
		}
    
		if (rkActorDst.IsStone())
		{
			return false;
		}
    
		if (rkActorDst.IsNPC())
		{
			return false;
		}
    
	//# Laniatus Games Studio Inc. |: 'extern' variable declarations are not required in C#:
	//	extern bool IS_HUGE_RACE(uint vnum);
		if (IS_HUGE_RACE(rkActorDst.GetRace()))
		{
			return false;
		}
    
		SMobTable mobTable = CPythonNonPlayer.instance().GetTable(rkActorDst.GetRace());
		if (mobTable != null)
		{
			if (mobTable.bRank >= CPythonNonPlayer.MOB_RANK_BOSS)
			{
				return false;
			}
		}
    
		if (rkActorDst.IsStun())
		{
			return true;
		}
    
		if (rkActorDst.__GetOwnerVID() != GetVirtualID())
		{
			return false;
		}
    
		if (rkActorDst.__GetOwnerTime() > 3.0f)
		{
			return false;
		}
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __ProcessDataAttackSuccess(in NRaceData.TAttackData c_rAttackData, CActorInstance rVictim, in _D3DVECTOR c_rv3Position, uint uiSkill, bool isSendPacket)
	{
		if (NRaceData.HIT_TYPE_NONE == c_rAttackData.iHittingType)
		{
			return;
		}
    
		InsertDelay(c_rAttackData.fStiffenTime);
    
		if (__CanPushDestActor(rVictim) && c_rAttackData.fExternalForce > 0.0f)
		{
			__PushCircle(rVictim);
    
			_D3DVECTOR kVictimPos = rVictim.GetPosition();
			rVictim.m_PhysicsObject.IncreaseExternalForce(kVictimPos, c_rAttackData.fExternalForce);
		}
    
		if (IS_PARTY_HUNTING_RACE(rVictim.GetRace()))
		{
			if (uiSkill != 0)
			{
				rVictim.m_fInvisibleTime = CTimer.Instance().GetCurrentSecond() + c_rAttackData.fInvisibleTime;
			}
    
			if (m_isMain)
			{
				rVictim.m_fInvisibleTime = CTimer.Instance().GetCurrentSecond() + c_rAttackData.fInvisibleTime;
			}
		}
		else
		{
			rVictim.m_fInvisibleTime = CTimer.Instance().GetCurrentSecond() + c_rAttackData.fInvisibleTime;
		}
    
		rVictim.InsertDelay(c_rAttackData.fStiffenTime);
    
		_D3DVECTOR vec3Effect = new _D3DVECTOR(rVictim.m_x, rVictim.m_y, rVictim.m_z);
    
	//# Laniatus Games Studio Inc. |: 'extern' variable declarations are not required in C#:
	//	extern bool IS_HUGE_RACE(uint vnum);
		if (IS_HUGE_RACE(rVictim.GetRace()))
		{
	//# Laniatus Games Studio Inc. | TODO TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'CopyFrom' method should be created:
	//Original Metin2 CPlus Line: vec3Effect = c_rv3Position;
			vec3Effect.CopyFrom(c_rv3Position);
		}
    
		_D3DVECTOR v3Pos = GetPosition();
    
		float fHeight = ((Math.Atan2(-vec3Effect.x + v3Pos.x,+vec3Effect.y - v3Pos.y)) * (180.0f / ((float) 3.141592654f)));
    
		if (rVictim.IsBuilding() || rVictim.IsDoor())
		{
			_D3DVECTOR vec3Delta = vec3Effect - v3Pos;
			D3DXVec3Normalize(vec3Delta, vec3Delta);
			vec3Delta *= 30.0f;
    
			CEffectManager rkEftMgr = CEffectManager.Instance();
			if (m_dwBattleHitEffectID)
			{
				rkEftMgr.CreateEffect(m_dwBattleHitEffectID, v3Pos + vec3Delta, D3DXVECTOR3(0.0f, 0.0f, 0.0f));
			}
		}
		else
		{
			CEffectManager rkEftMgr = CEffectManager.Instance();
			if (m_dwBattleHitEffectID)
			{
				rkEftMgr.CreateEffect(m_dwBattleHitEffectID, vec3Effect, D3DXVECTOR3(0.0f, 0.0f, fHeight));
			}
			if (m_dwBattleAttachEffectID)
			{
				rVictim.AttachEffectByID(0, null, m_dwBattleAttachEffectID);
			}
		}
    
		if (rVictim.IsBuilding())
		{
		}
		else if (rVictim.IsStone() || rVictim.IsDoor())
		{
			__HitStone(rVictim);
		}
		else
		{
			if (NRaceData.HIT_TYPE_GOOD == c_rAttackData.iHittingType || rVictim.IsResistFallen())
			{
				__HitGood(rVictim);
			}
			else if (NRaceData.HIT_TYPE_GREAT == c_rAttackData.iHittingType)
			{
				__HitGreate(rVictim);
			}
			else
			{
				TraceError("ProcessSucceedingAttacking: Unknown AttackingData.iHittingType %d", c_rAttackData.iHittingType);
			}
		}
    
		__OnHit(uiSkill, rVictim, isSendPacket);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void OnShootDamage()
	{
		if (IsStun())
		{
			Die();
		}
		else
		{
			__Shake(100);
    
			if (!isLock() && !__IsKnockDownMotion() && !__IsStandUpMotion())
			{
				if (InterceptOnceMotion(CRaceMotionData.NAME_DAMAGE))
				{
					PushLoopMotion(CRaceMotionData.NAME_WAIT);
				}
			}
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __Shake(uint dwDuration)
	{
		uint dwCurTime = ELTimer_GetMSec();
		m_dwShakeTime = dwCurTime + dwDuration;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void ShakeProcess()
	{
		if (m_dwShakeTime)
		{
			_D3DVECTOR v3Pos = new _D3DVECTOR(0.0f, 0.0f, 0.0f);
    
			uint dwCurTime = ELTimer_GetMSec();
    
			if (m_dwShakeTime < dwCurTime)
			{
				m_dwShakeTime = 0;
			}
			else
			{
				int nShakeSize = 10;
    
				switch (rand() % 2)
				{
					case 0:
						v3Pos.x += rand() % nShakeSize;
						break;
					case 1:
						v3Pos.x -= rand() % nShakeSize;
						break;
				}
    
				switch (rand() % 2)
				{
					case 0:
						v3Pos.y += rand() % nShakeSize;
						break;
					case 1:
						v3Pos.y -= rand() % nShakeSize;
						break;
				}
    
				switch (rand() % 2)
				{
					case 0:
						v3Pos.z += rand() % nShakeSize;
						break;
					case 1:
						v3Pos.z -= rand() % nShakeSize;
						break;
				}
			}
    
			m_worldMatrix._41 += v3Pos.x;
			m_worldMatrix._42 += v3Pos.y;
			m_worldMatrix._43 += v3Pos.z;
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __HitStone(CActorInstance rVictim)
	{
		if (rVictim.IsStun())
		{
			rVictim.Die();
		}
		else
		{
			rVictim.__Shake(100);
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __HitGood(CActorInstance rVictim)
	{
		if (rVictim.IsKnockDown())
		{
			return;
		}
    
		if (rVictim.IsStun())
		{
			rVictim.Die();
		}
		else
		{
			rVictim.__Shake(100);
    
			if (!rVictim.isLock())
			{
				float fRotRad = ((GetRotation()) * (((float) 3.141592654f) / 180.0f));
				float fVictimRotRad = ((rVictim.GetRotation()) * (((float) 3.141592654f) / 180.0f));
    
				D3DXVECTOR2 v2Normal = new D3DXVECTOR2(Math.Sin(fRotRad), Math.Cos(fRotRad));
				D3DXVECTOR2 v2VictimNormal = new D3DXVECTOR2(Math.Sin(fVictimRotRad), Math.Cos(fVictimRotRad));
    
				D3DXVec2Normalize(v2Normal, v2Normal);
				D3DXVec2Normalize(v2VictimNormal, v2VictimNormal);
    
				float fScalar = D3DXVec2Dot(v2Normal, v2VictimNormal);
    
				if (fScalar < 0.0f)
				{
					if (rVictim.InterceptOnceMotion(CRaceMotionData.NAME_DAMAGE))
					{
						rVictim.PushLoopMotion(CRaceMotionData.NAME_WAIT);
					}
				}
				else
				{
					if (rVictim.InterceptOnceMotion(CRaceMotionData.NAME_DAMAGE_BACK))
					{
						rVictim.PushLoopMotion(CRaceMotionData.NAME_WAIT);
					}
					else if (rVictim.InterceptOnceMotion(CRaceMotionData.NAME_DAMAGE))
					{
						rVictim.PushLoopMotion(CRaceMotionData.NAME_WAIT);
					}
				}
			}
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __HitGreate(CActorInstance rVictim)
	{
		if (rVictim.IsKnockDown())
		{
			return;
		}
		if (rVictim.__IsStandUpMotion())
		{
			return;
		}
    
		float fRotRad = ((GetRotation()) * (((float) 3.141592654f) / 180.0f));
		float fVictimRotRad = ((rVictim.GetRotation()) * (((float) 3.141592654f) / 180.0f));
    
		D3DXVECTOR2 v2Normal = new D3DXVECTOR2(Math.Sin(fRotRad), Math.Cos(fRotRad));
		D3DXVECTOR2 v2VictimNormal = new D3DXVECTOR2(Math.Sin(fVictimRotRad), Math.Cos(fVictimRotRad));
    
		D3DXVec2Normalize(v2Normal, v2Normal);
		D3DXVec2Normalize(v2VictimNormal, v2VictimNormal);
    
		float fScalar = D3DXVec2Dot(v2Normal, v2VictimNormal);
    
		rVictim.__Shake(100);
    
		if (rVictim.IsUsingSkill())
		{
			return;
		}
    
		if (rVictim.IsStun())
		{
			if (fScalar < 0.0f)
			{
				rVictim.InterceptOnceMotion(CRaceMotionData.NAME_DAMAGE_FLYING);
			}
			else
			{
				if (!rVictim.InterceptOnceMotion(CRaceMotionData.NAME_DAMAGE_FLYING_BACK))
				{
					rVictim.InterceptOnceMotion(CRaceMotionData.NAME_DAMAGE_FLYING);
				}
			}
    
			rVictim.m_isRealDead = true;
		}
		else
		{
			if (fScalar < 0.0f)
			{
				if (rVictim.InterceptOnceMotion(CRaceMotionData.NAME_DAMAGE_FLYING))
				{
					rVictim.PushOnceMotion(CRaceMotionData.NAME_STAND_UP);
					rVictim.PushLoopMotion(CRaceMotionData.NAME_WAIT);
				}
			}
			else
			{
				if (!rVictim.InterceptOnceMotion(CRaceMotionData.NAME_DAMAGE_FLYING_BACK))
				{
					if (rVictim.InterceptOnceMotion(CRaceMotionData.NAME_DAMAGE_FLYING))
					{
						rVictim.PushOnceMotion(CRaceMotionData.NAME_STAND_UP);
						rVictim.PushLoopMotion(CRaceMotionData.NAME_WAIT);
					}
				}
				else
				{
					rVictim.PushOnceMotion(CRaceMotionData.NAME_STAND_UP_BACK);
					rVictim.PushLoopMotion(CRaceMotionData.NAME_WAIT);
				}
			}
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetBlendingPosition(in TPixelPosition c_rPosition, float fBlendingTime)
	{
		TPixelPosition Position = new TPixelPosition();
    
		Position.x = c_rPosition.x - m_x;
		Position.y = c_rPosition.y - m_y;
		Position.z = 0;
    
		m_PhysicsObject.SetLastPosition(Position, fBlendingTime);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void ResetBlendingPosition()
	{
		m_PhysicsObject.Initialize();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void GetBlendingPosition(TPixelPosition pPosition)
	{
		if (m_PhysicsObject.isBlending())
		{
			m_PhysicsObject.GetLastPosition(pPosition);
			pPosition.x += m_x;
			pPosition.y += m_y;
			pPosition.z += m_z;
		}
		else
		{
			pPosition.x = m_x;
			pPosition.y = m_y;
			pPosition.z = m_z;
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __PushCircle(CActorInstance rVictim)
	{
		TPixelPosition c_rkPPosAtk = NEW_GetAtkPixelPositionRef();
    
		_D3DVECTOR v3SrcPos = new _D3DVECTOR(c_rkPPosAtk.x, -c_rkPPosAtk.y, c_rkPPosAtk.z);
    
	//# Laniatus Games Studio Inc. | TODO TASK: C# does not have an equivalent to references to variables:
	//Original Metin2 CPlus Line: const struct _D3DVECTOR& c_rv3SrcPos = v3SrcPos;
		_D3DVECTOR c_rv3SrcPos = v3SrcPos;
		_D3DVECTOR c_rv3DstPos = rVictim.GetPosition();
    
		_D3DVECTOR v3Direction = new _D3DVECTOR();
		v3Direction.x = c_rv3DstPos.x - c_rv3SrcPos.x;
		v3Direction.y = c_rv3DstPos.y - c_rv3SrcPos.y;
		v3Direction.z = 0.0f;
		D3DXVec3Normalize(v3Direction, v3Direction);
    
		rVictim.__SetFallingDirection(v3Direction.x, v3Direction.y);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __PushDirect(CActorInstance rVictim)
	{
		_D3DVECTOR v3Direction = new _D3DVECTOR();
		v3Direction.x = cosf(((m_fcurRotation + 270.0f) * (((float) 3.141592654f) / 180.0f)));
		v3Direction.y = sinf(((m_fcurRotation + 270.0f) * (((float) 3.141592654f) / 180.0f)));
		v3Direction.z = 0.0f;
    
		rVictim.__SetFallingDirection(v3Direction.x, v3Direction.y);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool __isInvisible()
	{
		if (IsDead())
		{
			return true;
		}
    
		if (CTimer.Instance().GetCurrentSecond() >= m_fInvisibleTime)
		{
			return false;
		}
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __SetFallingDirection(float fx, float fy)
	{
		m_PhysicsObject.SetDirection(D3DXVECTOR3(fx, fy, 0.0f));
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void BlendAlphaValue(float fDstAlpha, float fDuration)
	{
		__BlendAlpha_Apply(fDstAlpha, fDuration);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetBlendRenderMode()
	{
		m_iRenderMode = RENDER_MODE_BLEND;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetAlphaValue(float fAlpha)
	{
		m_fAlphaValue = fAlpha;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public float GetAlphaValue()
	{
		return m_fAlphaValue;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __BlendAlpha_Initialize()
	{
		m_kBlendAlpha.m_isBlending = false;
		m_kBlendAlpha.m_fBaseTime = 0.0f;
		m_kBlendAlpha.m_fDuration = 0.0f;
		m_kBlendAlpha.m_fBaseAlpha = 0.0f;
		m_kBlendAlpha.m_fDstAlpha = 0.0f;
		m_kBlendAlpha.m_iOldRenderMode = RENDER_MODE_NORMAL;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __BlendAlpha_Apply(float fDstAlpha, float fDuration)
	{
		m_kBlendAlpha.m_isBlending = true;
		m_kBlendAlpha.m_fBaseAlpha = GetAlphaValue();
		m_kBlendAlpha.m_fBaseTime = GetLocalTime();
		m_kBlendAlpha.m_fDuration = fDuration;
		m_kBlendAlpha.m_fDstAlpha = fDstAlpha;
		m_kBlendAlpha.m_iOldRenderMode = m_iRenderMode;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __BlendAlpha_Update()
	{
		if (!m_kBlendAlpha.m_isBlending)
		{
			return;
		}
    
		float fElapsedTime = __BlendAlpha_GetElapsedTime();
    
		if (fElapsedTime < m_kBlendAlpha.m_fDuration)
		{
			float fCurAlpha = m_kBlendAlpha.m_fBaseAlpha + (m_kBlendAlpha.m_fDstAlpha - m_kBlendAlpha.m_fBaseAlpha) * fElapsedTime / m_kBlendAlpha.m_fDuration;
			SetBlendRenderMode();
			SetAlphaValue(fCurAlpha);
		}
		else
		{
			if (1.0f > m_kBlendAlpha.m_fDstAlpha)
			{
				SetBlendRenderMode();
			}
			else
			{
				m_iRenderMode = m_kBlendAlpha.m_iOldRenderMode;
			}
    
			SetAlphaValue(m_kBlendAlpha.m_fDstAlpha);
    
			__BlendAlpha_UpdateComplete();
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __BlendAlpha_UpdateComplete()
	{
		m_kBlendAlpha.m_isBlending = false;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public float __BlendAlpha_GetElapsedTime()
	{
		float fCurTime = GetLocalTime();
		return fCurTime - m_kBlendAlpha.m_fBaseTime;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __InitializeCollisionData()
	{
		m_canSkipCollision = false;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void EnableSkipCollision()
	{
		m_canSkipCollision = true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void DisableSkipCollision()
	{
		m_canSkipCollision = false;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool CanSkipCollision()
	{
		return m_canSkipCollision;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void UpdatePointInstance()
	{
		TCollisionPointInstanceListIterator itor = new TCollisionPointInstanceListIterator();
		for (itor = m_DefendingPointInstanceList.begin(); itor != m_DefendingPointInstanceList.end(); ++itor)
		{
			UpdatePointInstance((*itor));
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void UpdatePointInstance(TCollisionPointInstance pPointInstance)
	{
		if (pPointInstance == null)
		{
			Debug.Assert(!"CActorInstance::UpdatePointInstance - pPointInstance is NULL");
			return;
		}
    
		_D3DMATRIX matBone = new _D3DMATRIX();
    
		if (pPointInstance.isAttached)
		{
			if (pPointInstance.dwModelIndex >= m_LODControllerVector.size())
			{
				return;
			}
    
			CGrannyLODController pGrnLODController = m_LODControllerVector[pPointInstance.dwModelIndex];
			if (pGrnLODController == null)
			{
				return;
			}
    
			CGrannyModelInstance pModelInstance = pGrnLODController.GetModelInstance();
			if (pModelInstance == null)
			{
				return;
			}
    
			_D3DMATRIX pmatBone = (_D3DMATRIX)pModelInstance.GetBoneMatrixPointer(pPointInstance.dwBoneIndex);
	//# Laniatus Games Studio Inc. | TODO TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'CopyFrom' method should be created:
	//Original Metin2 CPlus Line: matBone = *(struct _D3DMATRIX *)pModelInstance->GetCompositeBoneMatrixPointer(pPointInstance->dwBoneIndex);
			matBone.CopyFrom((_D3DMATRIX)pModelInstance.GetCompositeBoneMatrixPointer(pPointInstance.dwBoneIndex));
			matBone._41 = pmatBone._41;
			matBone._42 = pmatBone._42;
			matBone._43 = pmatBone._43;
			matBone *= m_worldMatrix;
		}
		else
		{
			matBone = m_worldMatrix;
		}
    
		List<CSphereCollisionInstance>.Enumerator sit = pPointInstance.c_pCollisionData.SphereDataVector.begin();
		List<CDynamicSphereInstance>.Enumerator dit = pPointInstance.SphereInstanceVector.begin();
		for (; sit.MoveNext(); ++sit,++dit)
		{
			SSphereData c = sit.GetAttribute();
    
			_D3DMATRIX matPoint = new _D3DMATRIX();
			D3DXMatrixTranslation(matPoint, c.v3Position.x, c.v3Position.y, c.v3Position.z);
	//# Laniatus Games Studio Inc. | TODO TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'CopyFrom' method should be created:
	//Original Metin2 CPlus Line: matPoint = matPoint * matBone;
			matPoint.CopyFrom(matPoint * matBone);
    
			dit.v3LastPosition = dit.v3Position;
			dit.v3Position.x = matPoint._41;
			dit.v3Position.y = matPoint._42;
			dit.v3Position.z = matPoint._43;
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void UpdateAdvancingPointInstance()
	{
		_D3DVECTOR v3Movement = m_v3Movement;
		if (m_pkHorse)
		{
			v3Movement = m_pkHorse.m_v3Movement;
		}
    
		if (m_pkHorse)
		{
			m_pkHorse.UpdateAdvancingPointInstance();
		}
    
		_D3DMATRIX matPoint = new _D3DMATRIX();
		_D3DMATRIX matCenter = new _D3DMATRIX();
    
		TCollisionPointInstanceListIterator itor = m_BodyPointInstanceList.begin();
		for (; itor != m_BodyPointInstanceList.end(); ++itor)
		{
	//# Laniatus Games Studio Inc. | TODO TASK: C# does not have an equivalent to references to variables:
	//Original Metin2 CPlus Line: TCollisionPointInstance & rInstance = *itor;
			TCollisionPointInstance rInstance = *itor;
    
			if (rInstance.isAttached)
			{
				if (rInstance.dwModelIndex >= m_LODControllerVector.size())
				{
					Tracenf("CActorInstance::UpdateAdvancingPointInstance - rInstance.dwModelIndex=%d >= m_LODControllerVector.size()=%d", rInstance.dwModelIndex, m_LODControllerVector.size());
					continue;
				}
    
				CGrannyLODController pGrnLODController = m_LODControllerVector[rInstance.dwModelIndex];
				if (pGrnLODController == null)
				{
					Tracenf("CActorInstance::UpdateAdvancingPointInstance - m_LODControllerVector[rInstance.dwModelIndex=%d] is NULL", rInstance.dwModelIndex);
					continue;
				}
    
				CGrannyModelInstance pModelInstance = pGrnLODController.GetModelInstance();
				if (pModelInstance == null)
				{
					continue;
				}
    
	//# Laniatus Games Studio Inc. | TODO TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'CopyFrom' method should be created:
	//Original Metin2 CPlus Line: matCenter = *(struct _D3DMATRIX *)pModelInstance->GetBoneMatrixPointer(rInstance.dwBoneIndex);
				matCenter.CopyFrom((_D3DMATRIX)pModelInstance.GetBoneMatrixPointer(rInstance.dwBoneIndex));
				matCenter *= m_worldMatrix;
			}
			else
			{
				matCenter = m_worldMatrix;
			}
    
			NRaceData.TCollisionData c_pCollisionData = rInstance.c_pCollisionData;
			if (c_pCollisionData != null)
			{
				for (uint j = 0; j < c_pCollisionData.SphereDataVector.size(); ++j)
				{
					SSphereData c = c_pCollisionData.SphereDataVector[j].GetAttribute();
					CDynamicSphereInstance rSphereInstance = rInstance.SphereInstanceVector[j];
    
					D3DXMatrixTranslation(matPoint, c.v3Position.x, c.v3Position.y, c.v3Position.z);
	//# Laniatus Games Studio Inc. | TODO TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'CopyFrom' method should be created:
	//Original Metin2 CPlus Line: matPoint = matPoint * matCenter;
					matPoint.CopyFrom(matPoint * matCenter);
    
					rSphereInstance.v3LastPosition.x = matPoint._41;
					rSphereInstance.v3LastPosition.y = matPoint._42;
					rSphereInstance.v3LastPosition.z = matPoint._43;
					rSphereInstance.v3Position = rSphereInstance.v3LastPosition;
					rSphereInstance.v3Position += v3Movement;
				}
			}
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool CheckCollisionDetection(List<CDynamicSphereInstance> c_pAttackingSphereVector, _D3DVECTOR pv3Position)
	{
		if (c_pAttackingSphereVector == null)
		{
			Debug.Assert(!"CActorInstance::CheckCollisionDetection - c_pAttackingSphereVector is NULL");
			return false;
		}
    
		TCollisionPointInstanceListIterator itor = new TCollisionPointInstanceListIterator();
		for (itor = m_DefendingPointInstanceList.begin(); itor != m_DefendingPointInstanceList.end(); ++itor)
		{
			List<CDynamicSphereInstance> c_pDefendingSphereVector = itor.SphereInstanceVector;
    
			for (uint LaniatusDefVariables = 0; LaniatusDefVariables < c_pAttackingSphereVector.Count; ++i)
			{
			for (uint j = 0; j < c_pDefendingSphereVector.Count; ++j)
			{
				CDynamicSphereInstance c_rAttackingSphere = c_pAttackingSphereVector[LaniatusDefVariables];
				CDynamicSphereInstance c_rDefendingSphere = c_pDefendingSphereVector[j];
    
				if (DetectCollisionDynamicSphereVSDynamicSphere(c_rAttackingSphere, c_rDefendingSphere))
				{
					pv3Position = (c_rAttackingSphere.v3Position + c_rDefendingSphere.v3Position) / 2.0f;
					return true;
				}
			}
			}
		}
    
		return false;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool CreateCollisionInstancePiece(uint dwAttachingModelIndex, NRaceData.TAttachingData c_pAttachingData, TCollisionPointInstance pPointInstance)
	{
		if (c_pAttachingData == null)
		{
			Debug.Assert(!"CActorInstance::CreateCollisionInstancePiece - c_pAttachingData is NULL");
			return false;
		}
    
		if (!c_pAttachingData.pCollisionData)
		{
			Debug.Assert(!"CActorInstance::CreateCollisionInstancePiece - c_pAttachingData->pCollisionData is NULL");
			return false;
		}
    
		if (pPointInstance == null)
		{
			Debug.Assert(!"CActorInstance::CreateCollisionInstancePiece - pPointInstance is NULL");
			return false;
		}
    
		pPointInstance.dwModelIndex = dwAttachingModelIndex;
		pPointInstance.isAttached = false;
		pPointInstance.dwBoneIndex = 0;
		pPointInstance.c_pCollisionData = c_pAttachingData.pCollisionData;
    
		if (c_pAttachingData.isAttaching)
		{
			int iAttachingBoneIndex;
    
			CGrannyModelInstance pModelInstance = m_LODControllerVector[dwAttachingModelIndex].GetModelInstance();
    
			if (pModelInstance != null && pModelInstance.GetBoneIndexByName(c_pAttachingData.strAttachingBoneName.c_str(), iAttachingBoneIndex))
			{
				pPointInstance.isAttached = true;
				pPointInstance.dwBoneIndex = iAttachingBoneIndex;
			}
			else
			{
				pPointInstance.isAttached = true;
				pPointInstance.dwBoneIndex = 0;
			}
		}
    
    
		List<CSphereCollisionInstance> c_rSphereDataVector = c_pAttachingData.pCollisionData.SphereDataVector;
    
		pPointInstance.SphereInstanceVector.clear();
		pPointInstance.SphereInstanceVector.reserve(c_rSphereDataVector.Count);
    
		List<CSphereCollisionInstance>.Enumerator it;
		CDynamicSphereInstance dsi = new CDynamicSphereInstance();
    
		dsi.v3LastPosition = D3DXVECTOR3(0.0f,0.0f,0.0f);
		dsi.v3Position = D3DXVECTOR3(0.0f,0.0f,0.0f);
		for (it = c_rSphereDataVector.GetEnumerator(); it.MoveNext();)
		{
			SSphereData c_rSphereData = it.GetAttribute();
			dsi.fRadius = c_rSphereData.fRadius;
			pPointInstance.SphereInstanceVector.push_back(dsi);
		}
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool __SplashAttackProcess(CActorInstance rVictim)
	{
		_D3DVECTOR v3Distance = new _D3DVECTOR(rVictim.m_x - m_x, rVictim.m_z - m_z, rVictim.m_z - m_z);
		float fDistance = D3DXVec3LengthSq(v3Distance);
		if (fDistance >= 1000.0f * 1000.0f)
		{
			return false;
		}
    
		if (!__IsInSplashTime())
		{
			return false;
		}
    
		NMotionEvent.SMotionEventDataAttack c_pAttackingEvent = m_kSplashArea.c_pAttackingEvent;
		NRaceData.TAttackData c_rAttackData = c_pAttackingEvent.AttackData;
		THittedInstanceMap rHittedInstanceMap = m_kSplashArea.HittedInstanceMap;
    
		if (rHittedInstanceMap.end() != rHittedInstanceMap.find(rVictim))
		{
			return false;
		}
    
		if (NRaceData.ATTACK_TYPE_SNIPE == c_rAttackData.iAttackType)
		{
			if (__IsFlyTargetPC())
			{
				if (!__IsSameFlyTarget(rVictim))
				{
					return false;
				}
			}
    
		}
    
		_D3DVECTOR v3HitPosition = new _D3DVECTOR();
		if (rVictim.CheckCollisionDetection(m_kSplashArea.SphereInstanceVector, v3HitPosition))
		{
			rHittedInstanceMap.insert(Tuple.Create(rVictim, GetLocalTime() + c_rAttackData.fInvisibleTime));
    
			int iCurrentHitCount = rHittedInstanceMap.size();
			int iMaxHitCount = (0 == c_rAttackData.iHitLimitCount ? MAX_HIT_COUNT : c_rAttackData.iHitLimitCount);
    
			if (iCurrentHitCount > iMaxHitCount)
			{
				return false;
			}
    
			NEW_SetAtkPixelPosition(NEW_GetCurPixelPositionRef());
			__ProcessDataAttackSuccess(c_rAttackData, rVictim, v3HitPosition, m_kSplashArea.uSkill, m_kSplashArea.isEnableHitProcess);
			return true;
		}
    
		return false;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool __NormalAttackProcess(CActorInstance rVictim)
	{
		_D3DVECTOR v3Distance = new _D3DVECTOR(rVictim.m_x - m_x, rVictim.m_z - m_z, rVictim.m_z - m_z);
		float fDistance = D3DXVec3LengthSq(v3Distance);
    
	//# Laniatus Games Studio Inc. |: 'extern' variable declarations are not required in C#:
	//	extern bool IS_HUGE_RACE(uint vnum);
		if (IS_HUGE_RACE(rVictim.GetRace()))
		{
			if (fDistance >= 500.0f * 500.0f)
			{
				return false;
			}
		}
		else
		{
			if (fDistance >= 300.0f * 300.0f)
			{
				return false;
			}
		}
    
		if (!isValidAttacking())
		{
			return false;
		}
    
		const float c_fAttackRadius = 20.0f;
		NRaceData.TMotionAttackData pad = m_pkCurRaceMotionData.GetMotionAttackDataPointer();
    
		float motiontime = GetAttackingElapsedTime();
    
		NRaceData.THitDataContainer.const_iterator itorHitData = pad.HitDataContainer.begin();
		for (; itorHitData != pad.HitDataContainer.end(); ++itorHitData)
		{
	//# Laniatus Games Studio Inc. | TODO TASK: C# does not have an equivalent to references to variables:
	//Original Metin2 CPlus Line: const NRaceData::THitData & c_rHitData = *itorHitData;
			NRaceData.THitData c_rHitData = *itorHitData;
    
			THitDataMap.iterator itHitData = m_HitDataMap.find(c_rHitData);
			if (itHitData != m_HitDataMap.end())
			{
				THittedInstanceMap rHittedInstanceMap = itHitData.second;
    
				THittedInstanceMap.iterator itInstance = new THittedInstanceMap.iterator();
				if ((itInstance = rHittedInstanceMap.find(rVictim)) != rHittedInstanceMap.end())
				{
					if (pad.iMotionType == NRaceData.MOTION_TYPE_COMBO || itInstance.second > GetLocalTime())
					{
						continue;
					}
				}
			}
    
			NRaceData.THitTimePositionMap.const_iterator range_start = new NRaceData.THitTimePositionMap.const_iterator();
			NRaceData.THitTimePositionMap.const_iterator range_end = new NRaceData.THitTimePositionMap.const_iterator();
			range_start = c_rHitData.mapHitPosition.lower_bound(motiontime - CTimer.Instance().GetElapsedSecond());
			range_end = c_rHitData.mapHitPosition.upper_bound(motiontime);
			float c = cosf(((GetRotation()) * (((float) 3.141592654f) / 180.0f)));
			float s = sinf(((GetRotation()) * (((float) 3.141592654f) / 180.0f)));
    
			for (;range_start != range_end;++range_start)
			{
				CDynamicSphereInstance dsiSrc = range_start.second;
    
				CDynamicSphereInstance dsi = new CDynamicSphereInstance();
	//# Laniatus Games Studio Inc. | TODO TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'CopyFrom' method should be created:
	//Original Metin2 CPlus Line: dsi = dsiSrc;
				dsi.CopyFrom(dsiSrc);
				dsi.fRadius = c_fAttackRadius;
				{
					_D3DVECTOR v3SrcDir = dsiSrc.v3Position - dsiSrc.v3LastPosition;
					v3SrcDir *= __GetReachScale();
    
					_D3DVECTOR v3Src = dsiSrc.v3LastPosition + v3SrcDir;
					_D3DVECTOR v3Dst = dsi.v3Position;
					v3Dst.x = v3Src.x * c - v3Src.y * s;
					v3Dst.y = v3Src.x * s + v3Src.y * c;
					v3Dst += GetPosition();
				}
				{
					_D3DVECTOR v3Src = dsiSrc.v3LastPosition;
					_D3DVECTOR v3Dst = dsi.v3LastPosition;
					v3Dst.x = v3Src.x * c - v3Src.y * s;
					v3Dst.y = v3Src.x * s + v3Src.y * c;
					v3Dst += GetPosition();
				}
    
    
				TCollisionPointInstanceList.iterator cpit = new TCollisionPointInstanceList.iterator();
				for (cpit = rVictim.m_DefendingPointInstanceList.begin(); cpit != rVictim.m_DefendingPointInstanceList.end();++cpit)
				{
					int index = 0;
					List<CDynamicSphereInstance> c_DefendingSphereVector = cpit.SphereInstanceVector;
					List<CDynamicSphereInstance>.Enumerator dsit;
					for (dsit = c_DefendingSphereVector.GetEnumerator(); dsit.MoveNext(); ++dsit, ++index)
					{
						CDynamicSphereInstance sub = dsit.Current;
						if (DetectCollisionDynamicZCylinderVSDynamicZCylinder(dsi, sub))
						{
							THitDataMap.iterator itHitData = m_HitDataMap.find(c_rHitData);
							if (itHitData == m_HitDataMap.end())
							{
								THittedInstanceMap HittedInstanceMap = new THittedInstanceMap();
								HittedInstanceMap.insert(Tuple.Create(rVictim, GetLocalTime() + pad.fInvisibleTime));
								m_HitDataMap.insert(Tuple.Create(c_rHitData, HittedInstanceMap));
							}
							else
							{
								itHitData.second.insert(Tuple.Create(rVictim, GetLocalTime() + pad.fInvisibleTime));
    
								int iCurrentHitCount = itHitData.second.size();
								if (NRaceData.MOTION_TYPE_COMBO == pad.iMotionType || NRaceData.MOTION_TYPE_NORMAL == pad.iMotionType)
								{
									if (iCurrentHitCount > MAX_HIT_COUNT)
									{
										return false;
									}
								}
								else
								{
									if (iCurrentHitCount > pad.iHitLimitCount)
									{
										return false;
									}
								}
							}
    
							_D3DVECTOR v3HitPosition = (GetPosition() + rVictim.GetPosition()) * 0.5f;
    
	//# Laniatus Games Studio Inc. |: 'extern' variable declarations are not required in C#:
	//						extern bool IS_HUGE_RACE(uint vnum);
							if (IS_HUGE_RACE(rVictim.GetRace()))
							{
								v3HitPosition = (GetPosition() + sub.v3Position) * 0.5f;
							}
    
							__ProcessDataAttackSuccess(pad, rVictim, v3HitPosition, m_kCurMotNode.uSkill);
							return true;
						}
					}
				}
			}
		}
    
		return false;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool AttackingProcess(CActorInstance rVictim)
	{
		if (rVictim.__isInvisible())
		{
			return false;
		}
    
		if (__SplashAttackProcess(rVictim))
		{
			return true;
		}
    
		if (__NormalAttackProcess(rVictim))
		{
			return true;
		}
    
		return false;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool TestPhysicsBlendingCollision(CActorInstance rVictim)
	{
		if (rVictim.IsDead())
		{
			return false;
		}
    
		TPixelPosition kPPosLast = new TPixelPosition();
		GetBlendingPosition(kPPosLast);
    
		_D3DVECTOR v3Distance = D3DXVECTOR3(rVictim.m_x - kPPosLast.x, rVictim.m_y - kPPosLast.y, rVictim.m_z - kPPosLast.z);
		float fDistance = D3DXVec3LengthSq(v3Distance);
		if (fDistance > 800.0f * 800.0f)
		{
			return false;
		}
    
		TCollisionPointInstanceList pMainList;
		TCollisionPointInstanceList pVictimList;
		if (isAttacking() || IsWaiting())
		{
			pMainList = m_DefendingPointInstanceList;
			pVictimList = rVictim.m_DefendingPointInstanceList;
		}
		else
		{
			pMainList = m_BodyPointInstanceList;
			pVictimList = rVictim.m_BodyPointInstanceList;
		}
    
		TPixelPosition kPDelta = new TPixelPosition();
		m_PhysicsObject.GetLastPosition(kPDelta);
    
		_D3DVECTOR prevLastPosition = new _D3DVECTOR();
		_D3DVECTOR prevPosition = new _D3DVECTOR();
		const int nSubCheckCount = 50;
    
		TCollisionPointInstanceListIterator itorMain = pMainList.begin();
		TCollisionPointInstanceListIterator itorVictim = pVictimList.begin();
		for (; itorMain != pMainList.end(); ++itorMain)
		{
			for (; itorVictim != pVictimList.end(); ++itorVictim)
			{
				List<CDynamicSphereInstance> c_rMainSphereVector = itorMain.SphereInstanceVector;
				List<CDynamicSphereInstance> c_rVictimSphereVector = itorVictim.SphereInstanceVector;
    
				for (uint LaniatusDefVariables = 0; LaniatusDefVariables < c_rMainSphereVector.Count; ++i)
				{
					CDynamicSphereInstance c_rMainSphere = c_rMainSphereVector[LaniatusDefVariables];
					prevLastPosition = c_rMainSphere.v3LastPosition;
					prevPosition = c_rMainSphere.v3Position;
    
					c_rMainSphere.v3LastPosition = prevPosition;
    
					for (int LaniatusDefVariables = 1; LaniatusDefVariables <= nSubCheckCount; ++i)
					{
						c_rMainSphere.v3Position = prevPosition + (float)(i / (float)nSubCheckCount) * kPDelta;
    
						for (uint j = 0; j < c_rVictimSphereVector.Count; ++j)
						{
							CDynamicSphereInstance c_rVictimSphere = c_rVictimSphereVector[j];
    
							if (DetectCollisionDynamicSphereVSDynamicSphere(c_rMainSphere, c_rVictimSphere))
							{
								bool bResult = GetVector3Distance(c_rMainSphere.v3Position, c_rVictimSphere.v3Position) <= GetVector3Distance(c_rMainSphere.v3LastPosition, c_rVictimSphere.v3Position);
    
								c_rMainSphere.v3LastPosition = prevLastPosition;
								c_rMainSphere.v3Position = prevPosition;
    
								return bResult;
							}
						}
					}
					c_rMainSphere.v3LastPosition = prevLastPosition;
					c_rMainSphere.v3Position = prevPosition;
				}
			}
		}
    
		return false;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool TestActorCollision(CActorInstance rVictim)
	{
	#if ENABLE_STOP_COLISSION_GLOBAL
		int[] pListGlobal = {30000, 30001};
		string strMapEventOx = "metin2_map_oxevent";
    
		string stringName = CPythonBackground.Instance().GetWarpMapName();
    
		if (strMapEventOx == stringName)
		{
	#if ENABLE_WOLFMAN
			if (0 <= rVictim.GetRace() && rVictim.GetRace() <= 8)
			{
	#else
			if (0 <= rVictim.GetRace() && rVictim.GetRace() <= 7)
			{
	#endif
				return false;
			}
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public uint GetVirtualID()
	{
		return m_dwSelfVID;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetVirtualID(uint dwVID)
	{
		m_dwSelfVID = dwVID;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void UpdateAttribute()
	{
		if (!m_pAttributeInstance)
		{
			return;
		}
    
		if (!m_bNeedUpdateCollision)
		{
			return;
		}
    
		m_bNeedUpdateCollision = false;
    
		List<CStaticCollisionData> c_rkVec_ColliData = m_pAttributeInstance.GetObjectPointer().GetCollisionDataVector();
		UpdateCollisionData(c_rkVec_ColliData);
    
		m_pAttributeInstance.RefreshObject(GetTransform());
		UpdateHeightInstance(m_pAttributeInstance);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __CreateAttributeInstance(CAttributeData pData)
	{
		m_pAttributeInstance = CAttributeInstance.New();
		m_pAttributeInstance.Clear();
		m_pAttributeInstance.SetObjectPointer(pData);
		if (pData.IsEmpty())
		{
			m_pAttributeInstance.Clear();
			CAttributeInstance.Delete(m_pAttributeInstance);
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public uint GetRace()
	{
		return m_eRace;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SetRace(uint eRace)
	{
		CRaceData pRaceData;
		if (!CRaceManager.Instance().GetRaceDataPointer(eRace, pRaceData))
		{
			m_eRace = 0;
			m_pkCurRaceData = null;
			return false;
		}
    
		m_eRace = eRace;
		m_pkCurRaceData = pRaceData;
    
		CAttributeData pAttributeData = pRaceData.GetAttributeDataPtr();
		if (pAttributeData != null)
		{
			__CreateAttributeInstance(pAttributeData);
		}
    
	//# Laniatus Games Studio Inc. | TODO TASK: The memory management function 'memset' has no equivalent in C#:
		memset(m_adwPartItemID, 0, sizeof(m_adwPartItemID));
    
		__ClearAttachingEffect();
    
		CGraphicThingInstance.Clear();
    
		if (IsPC())
		{
			CGraphicThingInstance.ReserveModelThing(CRaceData.PART_MAX_NUM);
			CGraphicThingInstance.ReserveModelInstance(CRaceData.PART_MAX_NUM);
		}
		else
		{
			CGraphicThingInstance.ReserveModelThing(1);
			CGraphicThingInstance.ReserveModelInstance(1);
		}
    
    
		SortedDictionary<ushort, SMotionModeData>.Enumerator itor;
    
		if (pRaceData.CreateMotionModeIterator(itor))
		{
			do
			{
	//# Laniatus Games Studio Inc. | TODO TASK: Iterators are only converted within the context of 'while' and 'for' loops:
				ushort wMotionMode = itor.first;
	//# Laniatus Games Studio Inc. | TODO TASK: Iterators are only converted within the context of 'while' and 'for' loops:
				SMotionModeData pMotionModeData = itor.second;
    
				SortedDictionary<ushort, List<SMotion>>.Enumerator itorMotion = pMotionModeData.MotionVectorMap.begin();
				while (itorMotion.MoveNext())
				{
					ushort wMotionIndex = itorMotion.Current.Key;
					List<SMotion> c_rMotionVector = itorMotion.Current.Value;
					List<SMotion>.Enumerator it;
					uint i;
					for (i = 0, it = c_rMotionVector.GetEnumerator(); it.MoveNext(); ++i, ++it)
					{
						uint dwMotionKey = MAKE_RANDOM_MOTION_KEY(wMotionMode, wMotionIndex, i);
						CGraphicThingInstance.RegisterMotionThing(dwMotionKey, it.pMotion);
					}
				}
			} while (pRaceData.NextMotionModeIterator(itor));
		}
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetHair(uint eHair)
	{
		m_eHair = eHair;
    
		CRaceData pRaceData;
    
		if (!CRaceManager.Instance().GetRaceDataPointer(m_eRace, pRaceData))
		{
			return;
		}
    
		CRaceData.SHair pkHair = pRaceData.FindHair(eHair);
		if (pkHair != null)
		{
			if (!pkHair.m_stModelFileName.empty())
			{
				CGraphicThing pkHairThing = (CGraphicThing)CResourceManager.Instance().GetResourcePointer(pkHair.m_stModelFileName.c_str());
				RegisterModelThing(CRaceData.PART_HAIR, pkHairThing);
				SetModelInstance(CRaceData.PART_HAIR, CRaceData.PART_HAIR, 0, CRaceData.PART_MAIN);
			}
    
			List<CRaceData.SSkin> c_rkVct_kSkin = pkHair.m_kVct_kSkin;
			List<CRaceData.SSkin>.Enumerator i;
			for (i = c_rkVct_kSkin.GetEnumerator(); i.MoveNext();)
			{
				CRaceData.SSkin c_rkSkinItem = i.Current;
    
				CResource pkRes = CResourceManager.Instance().GetResourcePointer(c_rkSkinItem.m_stDstFileName.c_str());
    
				if (pkRes != null)
				{
					SetMaterialImagePointer(CRaceData.PART_HAIR, c_rkSkinItem.m_stSrcFileName.c_str(), (CGraphicImage)pkRes);
				}
			}
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetShape(uint eShape, float fSpecular)
	{
		m_eShape = eShape;
    
		CRaceData pRaceData;
		if (!CRaceManager.Instance().GetRaceDataPointer(m_eRace, pRaceData))
		{
			return;
		}
    
		CRaceData.SShape pkShape = pRaceData.FindShape(eShape);
		if (pkShape != null)
		{
			CResourceManager rkResMgr = CResourceManager.Instance();
    
			if (pkShape.m_stModelFileName.empty())
			{
				CGraphicThing pModelThing = pRaceData.GetBaseModelThing();
				RegisterModelThing(0, pModelThing);
			}
			else
			{
				CGraphicThing pModelThing = (CGraphicThing)rkResMgr.GetResourcePointer(pkShape.m_stModelFileName.c_str());
				RegisterModelThing(0, pModelThing);
			}
    
			SetModelInstance(0, 0, 0);
    
			List<CRaceData.SSkin> c_rkVct_kSkin = pkShape.m_kVct_kSkin;
			List<CRaceData.SSkin>.Enumerator i;
			for (i = c_rkVct_kSkin.GetEnumerator(); i.MoveNext();)
			{
				CRaceData.SSkin c_rkSkinItem = i.Current;
    
				CResource pkRes = CResourceManager.Instance().GetResourcePointer(c_rkSkinItem.m_stDstFileName.c_str());
    
				if (pkRes != null)
				{
					if (fSpecular > 0.0f)
					{
						SMaterialData kMaterialData = new SMaterialData();
						kMaterialData.pImage = (CGraphicImage)pkRes;
						kMaterialData.isSpecularEnable = true;
						kMaterialData.fSpecularPower = fSpecular;
						kMaterialData.bSphereMapIndex = 0;
						 SetMaterialData(c_rkSkinItem.m_ePart, c_rkSkinItem.m_stSrcFileName.c_str(), kMaterialData);
					}
					else
					{
						 SetMaterialImagePointer(c_rkSkinItem.m_ePart, c_rkSkinItem.m_stSrcFileName.c_str(), (CGraphicImage)pkRes);
					}
				}
			}
		}
		else
		{
			if (pRaceData.IsTree())
			{
				__CreateTree(pRaceData.GetTreeFileName());
			}
			else
			{
				CGraphicThing pModelThing = pRaceData.GetBaseModelThing();
				RegisterModelThing(0, pModelThing);
    
				SetModelInstance(0, 0, 0);
			}
		}
    
		for (uint LaniatusDefVariables = 0; LaniatusDefVariables < pRaceData.GetAttachingDataCount(); ++i)
		{
			NRaceData.TAttachingData c_pAttachingData;
			if (!pRaceData.GetAttachingDataPointer(i, c_pAttachingData))
			{
				continue;
			}
    
			switch (c_pAttachingData.dwType)
			{
				case NRaceData.ATTACHING_DATA_TYPE_EFFECT:
					if (c_pAttachingData.isAttaching)
					{
						AttachEffectByName(0, c_pAttachingData.strAttachingBoneName.c_str(), c_pAttachingData.pEffectData.strFileName.c_str());
					}
					else
					{
						AttachEffectByName(0, 0, c_pAttachingData.pEffectData.strFileName.c_str());
					}
					break;
			}
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void ChangeMaterial(string c_szFileName)
	{
		CRaceData pRaceData;
		if (!CRaceManager.Instance().GetRaceDataPointer(m_eRace, pRaceData))
		{
			return;
		}
    
		CRaceData.SShape pkShape = pRaceData.FindShape(m_eShape);
		if (pkShape == null)
		{
			return;
		}
    
		List<CRaceData.SSkin> c_rkVct_kSkin = pkShape.m_kVct_kSkin;
		if (c_rkVct_kSkin.Count == 0)
		{
			return;
		}
    
		List<CRaceData.SSkin>.Enumerator LaniatusDefVariables = c_rkVct_kSkin.GetEnumerator();
	//# Laniatus Games Studio Inc. | TODO TASK: C# does not have an equivalent to references to variables:
	//Original Metin2 CPlus Line: const CRaceData::SSkin& c_rkSkinItem = *i;
	//# Laniatus Games Studio Inc. | TODO TASK: Iterators are only converted within the context of 'while' and 'for' loops:
		CRaceData.SSkin c_rkSkinItem = i;
    
		string dstFileName = "t:/laniaworkstate/npc/guild_symbol/guild_symbol.dds";
		dstFileName = c_szFileName;
    
		CResource pkRes = CResourceManager.Instance().GetResourcePointer(dstFileName);
		if (pkRes == null)
		{
			return;
		}
    
		 SetMaterialImagePointer(c_rkSkinItem.m_ePart, c_rkSkinItem.m_stSrcFileName.c_str(), (CGraphicImage)pkRes);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public uint GetPartItemID(uint dwPartIndex)
	{
		if (dwPartIndex >= CRaceData.PART_MAX_NUM)
		{
			TraceError("CActorInstance::GetPartIndex(dwPartIndex=%d/CRaceData::PART_MAX_NUM=%d)", dwPartIndex, CRaceData.PART_MAX_NUM);
			return 0;
		}
    
		return m_adwPartItemID[dwPartIndex];
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetSpecularInfo(bool bEnable, int iPart, float fAlpha)
	{
		CRaceData pkRaceData;
		if (!CRaceManager.Instance().GetRaceDataPointer(m_eRace, pkRaceData))
		{
			return;
		}
    
		CRaceData.SShape pkShape = pkRaceData.FindShape(m_eShape);
		if (pkShape.m_kVct_kSkin.empty())
		{
			return;
		}
    
		string filename = pkShape.m_kVct_kSkin[0].m_stSrcFileName.c_str();
		CFileNameHelper.ChangeDosPath(filename);
    
		CGraphicThingInstance.SetSpecularInfo(iPart, filename, bEnable, fAlpha);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetSpecularInfoForce(bool bEnable, int iPart, float fAlpha)
	{
		CGraphicThingInstance.SetSpecularInfo(iPart, null, bEnable, fAlpha);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __OnSyncing()
	{
		IEventHandler rkEventHandler = __GetEventHandlerRef();
    
		IEventHandler.SState kState = new IEventHandler.SState();
		kState.kPPosSelf = NEW_GetCurPixelPositionRef();
		kState.fAdvRotSelf = GetAdvancingRotation();
		rkEventHandler.OnSyncing(kState);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __OnWaiting()
	{
		Debug.Assert(!IsPushing());
    
		IEventHandler rkEventHandler = __GetEventHandlerRef();
    
		IEventHandler.SState kState = new IEventHandler.SState();
		kState.kPPosSelf = NEW_GetCurPixelPositionRef();
		kState.fAdvRotSelf = GetAdvancingRotation();
		rkEventHandler.OnWaiting(kState);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __OnMoving()
	{
		Debug.Assert(!IsPushing());
    
		IEventHandler rkEventHandler = __GetEventHandlerRef();
    
		TPixelPosition c_rkPPosCur = NEW_GetCurPixelPositionRef();
		TPixelPosition c_rkPPosDst = NEW_GetDstPixelPositionRef();
    
		TPixelPosition kPPosDir = c_rkPPosDst - c_rkPPosCur;
		float distance = Math.Sqrt(kPPosDir.x * kPPosDir.x + kPPosDir.y * kPPosDir.y);
    
		IEventHandler.SState kState = new IEventHandler.SState();
    
		if (distance > 1000.0f)
		{
			D3DXVec3Normalize(kPPosDir, kPPosDir);
			D3DXVec3Scale(kPPosDir, kPPosDir, 1000.0f);
			D3DXVec3Add(kState.kPPosSelf, kPPosDir, c_rkPPosCur);
		}
		else
		{
			kState.kPPosSelf = c_rkPPosDst;
		}
		kState.fAdvRotSelf = GetAdvancingRotation();
		rkEventHandler.OnMoving(kState);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __OnMove()
	{
		IEventHandler rkEventHandler = __GetEventHandlerRef();
    
		IEventHandler.SState kState = new IEventHandler.SState();
		kState.kPPosSelf = NEW_GetCurPixelPositionRef();
		kState.fAdvRotSelf = GetAdvancingRotation();
		rkEventHandler.OnMove(kState);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __OnStop()
	{
		IEventHandler rkEventHandler = __GetEventHandlerRef();
    
		IEventHandler.SState kState = new IEventHandler.SState();
		kState.kPPosSelf = NEW_GetCurPixelPositionRef();
		kState.fAdvRotSelf = GetAdvancingRotation();
		rkEventHandler.OnStop(kState);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __OnWarp()
	{
		IEventHandler rkEventHandler = __GetEventHandlerRef();
    
		IEventHandler.SState kState = new IEventHandler.SState();
		kState.kPPosSelf = NEW_GetCurPixelPositionRef();
		kState.fAdvRotSelf = GetAdvancingRotation();
		rkEventHandler.OnWarp(kState);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __OnAttack(ushort wMotionIndex)
	{
		IEventHandler rkEventHandler = __GetEventHandlerRef();
    
		IEventHandler.SState kState = new IEventHandler.SState();
		kState.kPPosSelf = NEW_GetCurPixelPositionRef();
		kState.fAdvRotSelf = GetTargetRotation();
		rkEventHandler.OnAttack(kState, wMotionIndex);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __OnUseSkill(uint uMotSkill, uint uLoopCount, bool isMovingSkill)
	{
		IEventHandler rkEventHandler = __GetEventHandlerRef();
    
		IEventHandler.SState kState = new IEventHandler.SState();
		kState.kPPosSelf = NEW_GetCurPixelPositionRef();
		kState.fAdvRotSelf = GetAdvancingRotation();
    
		uint uArg = uLoopCount;
		if (isMovingSkill)
		{
			uArg |= (uint)(1 << 4);
		}
    
		rkEventHandler.OnUseSkill(kState, uMotSkill, uArg);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __OnHit(uint uSkill, CActorInstance rkActorVictm, bool isSendPacket)
	{
		IEventHandler rkEventHandler = __GetEventHandlerRef();
		rkEventHandler.OnHit(uSkill, rkActorVictm, isSendPacket);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __OnClearAffects()
	{
		IEventHandler rkEventHandler = __GetEventHandlerRef();
		rkEventHandler.OnClearAffects();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __OnSetAffect(uint uAffect)
	{
		IEventHandler rkEventHandler = __GetEventHandlerRef();
		rkEventHandler.OnSetAffect(uAffect);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __OnResetAffect(uint uAffect)
	{
		IEventHandler rkEventHandler = __GetEventHandlerRef();
		rkEventHandler.OnResetAffect(uAffect);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public CActorInstance.IEventHandler __GetEventHandlerRef()
	{
		Debug.Assert(m_pkEventHandler != null && "CActorInstance::GetEventHandlerRef");
		return m_pkEventHandler;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public CActorInstance.IEventHandler __GetEventHandlerPtr()
	{
		return m_pkEventHandler;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetEventHandler(IEventHandler pkEventHandler)
	{
		m_pkEventHandler = pkEventHandler;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public _D3DVECTOR OnGetFlyTargetPosition()
	{
		_D3DVECTOR v3Center = new _D3DVECTOR();
		if (m_fRadius <= 0)
		{
			BuildBoundingSphere();
		}
    
		v3Center = m_v3Center;
		D3DXVec3TransformCoord(v3Center, v3Center, GetTransform());
    
		if (__IsMountingHorse())
		{
    
			v3Center.z += 110.0f;
		}
    
		return new _D3DVECTOR(v3Center);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void ClearFlyTarget()
	{
		m_kFlyTarget.Clear();
		m_kBackupFlyTarget.Clear();
		m_kQue_kFlyTarget.clear();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool IsFlyTargetObject()
	{
		return m_kFlyTarget.IsObject();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool __IsFlyTargetPC()
	{
		if (!IsFlyTargetObject())
		{
			return false;
		}
    
		CActorInstance pFlyInstance = (CActorInstance)m_kFlyTarget.GetFlyTarget();
		if (pFlyInstance.IsPC())
		{
			return true;
		}
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool __IsSameFlyTarget(CActorInstance pInstance)
	{
		if (!IsFlyTargetObject())
		{
			return false;
		}
    
		CActorInstance pFlyInstance = (CActorInstance)m_kFlyTarget.GetFlyTarget();
		if (pInstance == pFlyInstance)
		{
			return true;
		}
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public _D3DVECTOR __GetFlyTargetPosition()
	{
		if (!m_kFlyTarget.IsValidTarget())
		{
			return struct _D3DVECTOR(0.0f, 0.0f, 0.0f);
		}
    
		return m_kFlyTarget.GetFlyTargetPosition();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public float GetFlyTargetDistance()
	{
		_D3DVECTOR c_rv3FlyTargetPos = m_kFlyTarget.GetFlyTargetPosition();
		_D3DVECTOR c_rkPosSrc = GetPosition();
    
		_D3DVECTOR kPPosDelta = c_rv3FlyTargetPos - c_rkPosSrc;
		kPPosDelta.z = 0;
    
		return D3DXVec3Length(kPPosDelta);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void LookAtFlyTarget()
	{
		if (!IsFlyTargetObject())
		{
			return;
		}
    
		_D3DVECTOR c_rv3FlyTargetPos = m_kFlyTarget.GetFlyTargetPosition();
		LookAt(c_rv3FlyTargetPos.x, c_rv3FlyTargetPos.y);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void AddFlyTarget(in CFlyTarget cr_FlyTarget)
	{
		if (m_kFlyTarget.IsValidTarget())
		{
			m_kQue_kFlyTarget.push_back(cr_FlyTarget);
		}
		else
		{
			SetFlyTarget(cr_FlyTarget);
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetFlyTarget(in CFlyTarget cr_FlyTarget)
	{
		m_kFlyTarget = cr_FlyTarget;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void ClearFlyEventHandler()
	{
		m_pFlyEventHandler = 0;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetFlyEventHandler(IFlyEventHandler pHandler)
	{
		m_pFlyEventHandler = pHandler;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool CanChangeTarget()
	{
		if (__IsNeedFlyTargetMotion())
		{
			return false;
		}
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public uint __GetMotionType()
	{
		if (!m_pkCurRaceMotionData)
		{
			return CRaceMotionData.TYPE_NONE;
		}
    
		return m_pkCurRaceMotionData.GetType();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __MotionEventProcess(bool isPC)
	{
		if (isAttacking())
		{
			uint dwNextFrame = GetAttackingElapsedTime() * g_fGameFPS;
			for (; m_kCurMotNode.dwcurFrame < dwNextFrame; ++m_kCurMotNode.dwcurFrame)
			{
				MotionEventProcess();
				SoundEventProcess(!isPC);
			}
		}
		else
		{
			MotionEventProcess();
			SoundEventProcess(!isPC);
    
			++m_kCurMotNode.dwcurFrame;
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void MotionProcess(bool isPC)
	{
		__MotionEventProcess(isPC);
		CurrentMotionProcess();
		ReservingMotionProcess();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void HORSE_MotionProcess(bool isPC)
	{
		__MotionEventProcess(isPC);
    
		if (MOTION_TYPE_LOOP == m_kCurMotNode.iMotionType)
		{
			if (m_kCurMotNode.dwcurFrame >= m_kCurMotNode.dwFrameCount)
			{
				m_kCurMotNode.dwcurFrame = 0;
			}
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void ReservingMotionProcess()
	{
		if (m_MotionDeque.empty())
		{
			return;
		}
    
		TReservingMotionNode rReservingMotionNode = m_MotionDeque.front();
    
		float fCurrentTime = GetLocalTime();
		if (rReservingMotionNode.fStartTime > fCurrentTime)
		{
			return;
		}
    
		uint dwNextMotionIndex = GET_MOTION_INDEX(rReservingMotionNode.dwMotionKey);
		switch (dwNextMotionIndex)
		{
			case CRaceMotionData.NAME_STAND_UP:
			case CRaceMotionData.NAME_STAND_UP_BACK:
				if (IsFaint())
				{
    
					SetEndStopMotion();
    
					TMotionDeque.iterator itor = m_MotionDeque.begin();
					for (; itor != m_MotionDeque.end(); ++itor)
					{
	//# Laniatus Games Studio Inc. | TODO TASK: C# does not have an equivalent to references to variables:
	//Original Metin2 CPlus Line: TReservingMotionNode & rNode = *itor;
						TReservingMotionNode rNode = *itor;
						rNode.fStartTime += 1.0f;
					}
					return;
				}
				break;
		}
    
		SCurrentMotionNode kPrevMotionNode = m_kCurMotNode;
    
		EMotionPushType iMotionType = rReservingMotionNode.iMotionType;
		float fSpeedRatio = rReservingMotionNode.fSpeedRatio;
		float fBlendTime = rReservingMotionNode.fBlendTime;
    
		uint dwMotionKey = rReservingMotionNode.dwMotionKey;
    
		m_MotionDeque.pop_front();
    
		uint dwCurrentMotionIndex = GET_MOTION_INDEX(dwMotionKey);
		switch (dwCurrentMotionIndex)
		{
			case CRaceMotionData.NAME_STAND_UP:
			case CRaceMotionData.NAME_STAND_UP_BACK:
				if (IsDead())
				{
					m_kCurMotNode = kPrevMotionNode;
					__ClearMotion();
					SetEndStopMotion();
					return;
				}
				break;
		}
    
		int iLoopCount;
		if (MOTION_TYPE_ONCE == iMotionType)
		{
			iLoopCount = 1;
		}
		else
		{
			iLoopCount = 0;
		}
    
		SSetMotionData kSetMotData = new SSetMotionData();
		kSetMotData.dwMotKey = dwMotionKey;
		kSetMotData.fBlendTime = fBlendTime;
		kSetMotData.fSpeedRatio = fSpeedRatio;
		kSetMotData.iLoopCount = iLoopCount;
    
		uint dwRealMotionKey = __SetMotion(kSetMotData);
    
		if (0 == dwRealMotionKey)
		{
			return;
		}
    
		float fDurationTime = GetMotionDuration(dwRealMotionKey) / fSpeedRatio;
		float fStartTime = rReservingMotionNode.fStartTime;
		float fEndTime = fStartTime + fDurationTime;
    
		if (dwRealMotionKey == 16777473)
		{
			int bp = 0;
			bp++;
		}
    
		m_kCurMotNode.uSkill = 0;
		m_kCurMotNode.iMotionType = iMotionType;
		m_kCurMotNode.fSpeedRatio = fSpeedRatio;
		m_kCurMotNode.fStartTime = fStartTime;
		m_kCurMotNode.fEndTime = fEndTime;
		m_kCurMotNode.dwMotionKey = dwRealMotionKey;
		m_kCurMotNode.dwcurFrame = 0;
		m_kCurMotNode.dwFrameCount = fDurationTime / (1.0f / g_fGameFPS);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void CurrentMotionProcess()
	{
		if (MOTION_TYPE_LOOP == m_kCurMotNode.iMotionType)
		{
			if (m_kCurMotNode.dwcurFrame >= m_kCurMotNode.dwFrameCount)
			{
				m_kCurMotNode.dwcurFrame = 0;
			}
		}
    
		if (IsDead())
		{
			return;
		}
    
		if (!m_MotionDeque.empty())
		{
			return;
		}
    
		float fCurrentTime = GetLocalTime();
    
		uint dwMotionIndex = GET_MOTION_INDEX(m_kCurMotNode.dwMotionKey);
    
		bool isLooping = false;
    
		if (m_pkCurRaceMotionData && m_pkCurRaceMotionData.IsLoopMotion())
		{
			if (m_kCurMotNode.iLoopCount > 1 || m_kCurMotNode.iLoopCount == -1)
			{
				if (fCurrentTime - m_kCurMotNode.fStartTime > m_pkCurRaceMotionData.GetLoopEndTime())
				{
					m_kCurMotNode.dwcurFrame = (uint)(m_pkCurRaceMotionData.GetLoopStartTime() * g_fGameFPS);
					__SetLocalTime(m_kCurMotNode.fStartTime + m_pkCurRaceMotionData.GetLoopStartTime());
					if (-1 != m_kCurMotNode.iLoopCount)
					{
						--m_kCurMotNode.iLoopCount;
					}
    
					isLooping = true;
				}
			}
			else if (!m_kQue_kFlyTarget.empty())
			{
				if (!m_kBackupFlyTarget.IsObject())
				{
					m_kBackupFlyTarget = m_kFlyTarget;
				}
    
				if (fCurrentTime - m_kCurMotNode.fStartTime > m_pkCurRaceMotionData.GetLoopEndTime())
				{
					m_kCurMotNode.dwcurFrame = (uint)(m_pkCurRaceMotionData.GetLoopStartTime() * g_fGameFPS);
					__SetLocalTime(m_kCurMotNode.fStartTime + m_pkCurRaceMotionData.GetLoopStartTime());
    
					SetFlyTarget(m_kQue_kFlyTarget.front());
					m_kQue_kFlyTarget.pop_front();
    
					isLooping = true;
				}
			}
		}
    
		if (!isLooping)
		{
			if (fCurrentTime > m_kCurMotNode.fEndTime)
			{
				if (m_kBackupFlyTarget.IsValidTarget())
				{
					m_kFlyTarget = m_kBackupFlyTarget;
					m_kBackupFlyTarget.Clear();
				}
    
				if (MOTION_TYPE_ONCE == m_kCurMotNode.iMotionType)
				{
					switch (dwMotionIndex)
					{
						case CRaceMotionData.NAME_DAMAGE_FLYING:
						case CRaceMotionData.NAME_DAMAGE_FLYING_BACK:
						case CRaceMotionData.NAME_DEAD:
						case CRaceMotionData.NAME_INTRO_SELECTED:
						case CRaceMotionData.NAME_INTRO_NOT_SELECTED:
							m_kCurMotNode.fEndTime += 3.0f;
							SetEndStopMotion();
							break;
						default:
							InterceptLoopMotion(CRaceMotionData.NAME_WAIT);
							break;
					}
				}
				else if (MOTION_TYPE_LOOP == m_kCurMotNode.iMotionType)
				{
					if (CRaceMotionData.NAME_WAIT == dwMotionIndex)
					{
						PushLoopMotion(CRaceMotionData.NAME_WAIT, 0.5f);
					}
				}
			}
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetMotionMode(int iMotionMode)
	{
		if (IsPoly())
		{
			iMotionMode = CRaceMotionData.MODE_GENERAL;
		}
    
		m_wcurMotionMode = iMotionMode;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public int GetMotionMode()
	{
		return m_wcurMotionMode;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetMotionLoopCount(int iCount)
	{
		Debug.Assert(iCount >= -1 && iCount < 100);
		m_kCurMotNode.iLoopCount = iCount;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void PushMotion(EMotionPushType iMotionType, uint dwMotionKey, float fBlendTime, float fSpeedRatio)
	{
		if (!CheckMotionThingIndex(dwMotionKey))
		{
			Tracef(" Error - Not found want to using motion : %d\n", GET_MOTION_INDEX(dwMotionKey));
			return;
		}
    
		TReservingMotionNode MotionNode = new TReservingMotionNode();
    
		MotionNode.iMotionType = iMotionType;
		MotionNode.dwMotionKey = dwMotionKey;
		MotionNode.fStartTime = GetLastMotionTime(fBlendTime);
		MotionNode.fBlendTime = fBlendTime;
		MotionNode.fSpeedRatio = fSpeedRatio;
		MotionNode.fDuration = GetMotionDuration(dwMotionKey);
    
		m_MotionDeque.push_back(MotionNode);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool InterceptOnceMotion(uint dwMotion, float fBlendTime, uint uSkill, float fSpeedRatio)
	{
		return InterceptMotion(MOTION_TYPE_ONCE, dwMotion, fBlendTime, uSkill, fSpeedRatio);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool InterceptLoopMotion(uint dwMotion, float fBlendTime)
	{
		return InterceptMotion(MOTION_TYPE_LOOP, dwMotion, fBlendTime);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetLoopMotion(uint dwMotion, float fBlendTime, float fSpeedRatio)
	{
		if (!m_pkCurRaceData)
		{
			Tracenf("CActorInstance::SetLoopMotion(dwMotion=%d, fBlendTime=%f, fSpeedRatio=%f)", dwMotion, fBlendTime, fSpeedRatio);
			return;
		}
    
		MOTION_KEY dwMotionKey = new MOTION_KEY();
		if (!m_pkCurRaceData.GetMotionKey(m_wcurMotionMode, dwMotion, dwMotionKey))
		{
			Tracenf("CActorInstance::SetLoopMotion(dwMotion=%d, fBlendTime=%f, fSpeedRatio=%f) - GetMotionKey(m_wcurMotionMode=%d, dwMotion=%d, &MotionKey) ERROR", dwMotion, fBlendTime, fSpeedRatio, m_wcurMotionMode, dwMotion);
			return;
		}
    
		__ClearMotion();
    
		SSetMotionData kSetMotData = new SSetMotionData();
		kSetMotData.dwMotKey = dwMotionKey;
		kSetMotData.fBlendTime = fBlendTime;
		kSetMotData.fSpeedRatio = fSpeedRatio;
    
		uint dwRealMotionKey = __SetMotion(kSetMotData);
    
		if (0 == dwRealMotionKey)
		{
			return;
		}
    
		m_kCurMotNode.iMotionType = MOTION_TYPE_LOOP;
		m_kCurMotNode.fStartTime = GetLocalTime();
		m_kCurMotNode.dwMotionKey = dwRealMotionKey;
		m_kCurMotNode.fEndTime = 0.0f;
		m_kCurMotNode.fSpeedRatio = fSpeedRatio;
		m_kCurMotNode.dwcurFrame = 0;
		m_kCurMotNode.dwFrameCount = GetMotionDuration(dwRealMotionKey) / (1.0f / g_fGameFPS);
		m_kCurMotNode.uSkill = 0;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool InterceptMotion(EMotionPushType iMotionType, ushort wMotion, float fBlendTime, uint uSkill, float fSpeedRatio)
	{
		if (!m_pkCurRaceData)
		{
			Tracef("CActorInstance::InterceptMotion(iMotionType=%d, wMotion=%d, fBlendTime=%f) - m_pkCurRaceData=NULL", iMotionType, wMotion, fBlendTime);
			return false;
		}
    
		MOTION_KEY dwMotionKey = new MOTION_KEY();
		if (!m_pkCurRaceData.GetMotionKey(m_wcurMotionMode, wMotion, dwMotionKey))
		{
			Tracenf("CActorInstance::InterceptMotion(iLoopType=%d, wMotionMode=%d, wMotion=%d, fBlendTime=%f) - GetMotionKey(m_wcurMotionMode=%d, wMotion=%d, &MotionKey) ERROR", iMotionType, m_wcurMotionMode, wMotion, fBlendTime, m_wcurMotionMode, wMotion);
			return false;
		}
    
		__ClearMotion();
    
		int iLoopCount;
		if (MOTION_TYPE_ONCE == iMotionType)
		{
			iLoopCount = 1;
		}
		else
		{
			iLoopCount = 0;
		}
    
		SSetMotionData kSetMotData = new SSetMotionData();
		kSetMotData.dwMotKey = dwMotionKey;
		kSetMotData.fBlendTime = fBlendTime;
		kSetMotData.iLoopCount = iLoopCount;
		kSetMotData.fSpeedRatio = fSpeedRatio;
		kSetMotData.uSkill = uSkill;
    
		uint dwRealMotionKey = __SetMotion(kSetMotData);
    
		if (0 == dwRealMotionKey)
		{
			return false;
		}
    
		if (m_pFlyEventHandler)
		{
			if (__IsNeedFlyTargetMotion())
			{
				m_pFlyEventHandler.OnSetFlyTarget();
			}
		}
    
		Debug.Assert(null != m_pkCurRaceMotionData);
    
		float fDuration = GetMotionDuration(dwRealMotionKey) / fSpeedRatio;
    
		m_kCurMotNode.iMotionType = iMotionType;
		m_kCurMotNode.fStartTime = GetLocalTime();
		m_kCurMotNode.fEndTime = m_kCurMotNode.fStartTime + fDuration;
		m_kCurMotNode.dwMotionKey = dwRealMotionKey;
		m_kCurMotNode.dwcurFrame = 0;
		m_kCurMotNode.dwFrameCount = fDuration / (1.0f / g_fGameFPS);
		m_kCurMotNode.uSkill = uSkill;
		m_kCurMotNode.fSpeedRatio = fSpeedRatio;
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool PushOnceMotion(uint dwMotion, float fBlendTime, float fSpeedRatio)
	{
		Debug.Assert(m_pkCurRaceData);
    
		MOTION_KEY MotionKey = new MOTION_KEY();
		if (!m_pkCurRaceData.GetMotionKey(m_wcurMotionMode, dwMotion, MotionKey))
		{
			return false;
		}
    
		PushMotion(MOTION_TYPE_ONCE, MotionKey, fBlendTime, fSpeedRatio);
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool PushLoopMotion(uint dwMotion, float fBlendTime, float fSpeedRatio)
	{
		Debug.Assert(m_pkCurRaceData);
    
		MOTION_KEY MotionKey = new MOTION_KEY();
		if (!m_pkCurRaceData.GetMotionKey(m_wcurMotionMode, dwMotion, MotionKey))
		{
			return false;
		}
    
		PushMotion(MOTION_TYPE_LOOP, MotionKey, fBlendTime, fSpeedRatio);
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public ushort __GetCurrentMotionIndex()
	{
		return GET_MOTION_INDEX(m_kCurMotNode.dwMotionKey);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public uint __GetCurrentMotionKey()
	{
		return m_kCurMotNode.dwMotionKey;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool IsUsingSkill()
	{
		uint dwCurMotionIndex = __GetCurrentMotionIndex();
    
		if (dwCurMotionIndex >= CRaceMotionData.NAME_SKILL && dwCurMotionIndex < CRaceMotionData.NAME_SKILL_END)
		{
			return true;
		}
    
		switch (dwCurMotionIndex)
		{
			case CRaceMotionData.NAME_SPECIAL_1:
			case CRaceMotionData.NAME_SPECIAL_2:
			case CRaceMotionData.NAME_SPECIAL_3:
			case CRaceMotionData.NAME_SPECIAL_4:
			case CRaceMotionData.NAME_SPECIAL_5:
			case CRaceMotionData.NAME_SPECIAL_6:
				return true;
		}
    
		return false;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool IsFishing()
	{
		if (!m_pkCurRaceMotionData)
		{
			return false;
		}
    
		if (__GetCurrentMotionIndex() == CRaceMotionData.NAME_FISHING_WAIT || __GetCurrentMotionIndex() == CRaceMotionData.NAME_FISHING_REACT)
		{
			return true;
		}
    
		return false;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool CanCancelSkill()
	{
		Debug.Assert(IsUsingSkill());
		return m_pkCurRaceMotionData.IsCancelEnableSkill();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool isLock()
	{
		uint dwCurMotionIndex = __GetCurrentMotionIndex();
    
		switch (dwCurMotionIndex)
		{
			case CRaceMotionData.NAME_NORMAL_ATTACK:
			case CRaceMotionData.NAME_COMBO_ATTACK_1:
			case CRaceMotionData.NAME_COMBO_ATTACK_2:
			case CRaceMotionData.NAME_COMBO_ATTACK_3:
			case CRaceMotionData.NAME_COMBO_ATTACK_4:
			case CRaceMotionData.NAME_COMBO_ATTACK_5:
			case CRaceMotionData.NAME_COMBO_ATTACK_6:
			case CRaceMotionData.NAME_COMBO_ATTACK_7:
			case CRaceMotionData.NAME_COMBO_ATTACK_8:
			case CRaceMotionData.NAME_SPECIAL_1:
			case CRaceMotionData.NAME_SPECIAL_2:
			case CRaceMotionData.NAME_SPECIAL_3:
			case CRaceMotionData.NAME_SPECIAL_4:
			case CRaceMotionData.NAME_SPECIAL_5:
			case CRaceMotionData.NAME_SPECIAL_6:
			case CRaceMotionData.NAME_FISHING_THROW:
			case CRaceMotionData.NAME_FISHING_WAIT:
			case CRaceMotionData.NAME_FISHING_STOP:
			case CRaceMotionData.NAME_FISHING_REACT:
			case CRaceMotionData.NAME_FISHING_CATCH:
			case CRaceMotionData.NAME_FISHING_FAIL:
			case CRaceMotionData.NAME_CLAP:
			case CRaceMotionData.NAME_DANCE_1:
			case CRaceMotionData.NAME_DANCE_2:
			case CRaceMotionData.NAME_DANCE_3:
			case CRaceMotionData.NAME_DANCE_4:
			case CRaceMotionData.NAME_DANCE_5:
			case CRaceMotionData.NAME_DANCE_6:
			case CRaceMotionData.NAME_CONGRATULATION:
			case CRaceMotionData.NAME_FORGIVE:
			case CRaceMotionData.NAME_ANGRY:
			case CRaceMotionData.NAME_ATTRACTIVE:
			case CRaceMotionData.NAME_SAD:
			case CRaceMotionData.NAME_SHY:
			case CRaceMotionData.NAME_CHEERUP:
			case CRaceMotionData.NAME_BANTER:
			case CRaceMotionData.NAME_JOY:
			case CRaceMotionData.NAME_CHEERS_1:
			case CRaceMotionData.NAME_CHEERS_2:
			case CRaceMotionData.NAME_KISS_WITH_WARRIOR:
			case CRaceMotionData.NAME_KISS_WITH_ASSASSIN:
			case CRaceMotionData.NAME_KISS_WITH_SURA:
			case CRaceMotionData.NAME_KISS_WITH_SHAMAN:
	#if ENABLE_WOLFMAN
	//# Laniatus Games Studio Inc. | TODO TASK: C# does not allow fall-through from a non-empty 'case':
			case CRaceMotionData.NAME_KISS_WITH_WOLFMAN:
	#endif
	//# Laniatus Games Studio Inc. | TODO TASK: C# does not allow fall-through from a non-empty 'case':
			case CRaceMotionData.NAME_FRENCH_KISS_WITH_WARRIOR:
			case CRaceMotionData.NAME_FRENCH_KISS_WITH_ASSASSIN:
			case CRaceMotionData.NAME_FRENCH_KISS_WITH_SURA:
			case CRaceMotionData.NAME_FRENCH_KISS_WITH_SHAMAN:
	#if ENABLE_WOLFMAN
	//# Laniatus Games Studio Inc. | TODO TASK: C# does not allow fall-through from a non-empty 'case':
			case CRaceMotionData.NAME_FRENCH_KISS_WITH_WOLFMAN:
	#endif
	//# Laniatus Games Studio Inc. | TODO TASK: C# does not allow fall-through from a non-empty 'case':
			case CRaceMotionData.NAME_SLAP_HIT_WITH_WARRIOR:
			case CRaceMotionData.NAME_SLAP_HIT_WITH_ASSASSIN:
			case CRaceMotionData.NAME_SLAP_HIT_WITH_SURA:
			case CRaceMotionData.NAME_SLAP_HIT_WITH_SHAMAN:
	#if ENABLE_WOLFMAN
	//# Laniatus Games Studio Inc. | TODO TASK: C# does not allow fall-through from a non-empty 'case':
			case CRaceMotionData.NAME_SLAP_HIT_WITH_WOLFMAN:
	#endif
	//# Laniatus Games Studio Inc. | TODO TASK: C# does not allow fall-through from a non-empty 'case':
			case CRaceMotionData.NAME_SLAP_HURT_WITH_WARRIOR:
			case CRaceMotionData.NAME_SLAP_HURT_WITH_ASSASSIN:
			case CRaceMotionData.NAME_SLAP_HURT_WITH_SURA:
			case CRaceMotionData.NAME_SLAP_HURT_WITH_SHAMAN:
	#if ENABLE_WOLFMAN
	//# Laniatus Games Studio Inc. | TODO TASK: C# does not allow fall-through from a non-empty 'case':
			case CRaceMotionData.NAME_SLAP_HURT_WITH_WOLFMAN:
	#endif
				return true;
				break;
		}
    
		if (IsUsingSkill())
		{
			if (m_pkCurRaceMotionData.IsCancelEnableSkill())
			{
				return false;
			}
    
			return true;
		}
    
		return false;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public float GetLastMotionTime(float fBlendTime)
	{
		if (m_MotionDeque.empty())
		{
			if (MOTION_TYPE_ONCE == m_kCurMotNode.iMotionType)
			{
				return (m_kCurMotNode.fEndTime - fBlendTime);
			}
    
			return GetLocalTime();
		}
    
		TReservingMotionNode rMotionNode = m_MotionDeque[m_MotionDeque.size() - 1];
    
		return rMotionNode.fStartTime + rMotionNode.fDuration - fBlendTime;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public float GetMotionDuration(uint dwMotionKey)
	{
		CGraphicThing pMotion;
    
		if (!GetMotionThingPointer(dwMotionKey, pMotion))
		{
			Tracenf("CActorInstance::GetMotionDuration - Cannot get motion: %d / %d", GET_MOTION_MODE(dwMotionKey), GET_MOTION_INDEX(dwMotionKey));
			return 0.0f;
		}
    
		if (0 == pMotion.GetMotionCount())
		{
	#if DEBUG
			Tracenf("CActorInstance::GetMotionDuration - Invalid Motion Key : %d, %d, %d", GET_MOTION_MODE(dwMotionKey), GET_MOTION_INDEX(dwMotionKey), GET_MOTION_SUB_INDEX(dwMotionKey));
	#endif
			return 0.0f;
		}
    
		CGrannyMotion pGrannyMotion = pMotion.GetMotionPointer(0);
		return pGrannyMotion.GetDuration();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public MOTION_KEY GetRandomMotionKey(MOTION_KEY dwMotionKey)
	{
		ushort wMode = GET_MOTION_MODE(dwMotionKey);
		ushort wIndex = GET_MOTION_INDEX(dwMotionKey);
    
		List<SMotion> c_pMotionVector;
		if (m_pkCurRaceData.GetMotionVectorPointer(wMode, wIndex, c_pMotionVector))
		{
		if (c_pMotionVector.Count > 1)
		{
			int iPercentage = random() % 100;
			for (uint LaniatusDefVariables = 0; LaniatusDefVariables < c_pMotionVector.Count; ++i)
			{
				SMotion c_rMotion = c_pMotionVector[LaniatusDefVariables];
				iPercentage -= c_rMotion.byPercentage;
    
				if (iPercentage < 0)
				{
					dwMotionKey = MAKE_RANDOM_MOTION_KEY(wMode, wIndex, i);
					return new MOTION_KEY(dwMotionKey);
				}
			}
		}
		}
    
		return new MOTION_KEY(dwMotionKey);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void PreAttack()
	{
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __ClearMotion()
	{
		__HideWeaponTrace();
    
		m_MotionDeque.clear();
		m_kCurMotNode.dwcurFrame = 0;
		m_kCurMotNode.dwFrameCount = 0;
		m_kCurMotNode.uSkill = 0;
		m_kCurMotNode.iLoopCount = 0;
		m_kCurMotNode.iMotionType = MOTION_TYPE_NONE;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public uint __SetMotion(in SSetMotionData c_rkSetMotData, uint dwRandMotKey)
	{
		uint dwMotKey = dwRandMotKey;
    
		if (dwMotKey == 0)
		{
			dwMotKey = GetRandomMotionKey(c_rkSetMotData.dwMotKey);
		}
    
		uint uNextMot = GET_MOTION_INDEX(c_rkSetMotData.dwMotKey);
    
		if (IsDead())
		{
			if (uNextMot != CRaceMotionData.NAME_DAMAGE_FLYING && uNextMot != CRaceMotionData.NAME_DAMAGE_FLYING_BACK && uNextMot != CRaceMotionData.NAME_DEAD && uNextMot != CRaceMotionData.NAME_DEAD_BACK)
			{
				return 0;
			}
		}
		if (IsUsingSkill())
		{
			__OnStop();
		}
    
		if (__IsStandUpMotion())
		{
			__OnStop();
		}
    
    
		if (__IsMoveMotion())
		{
			if (uNextMot == CRaceMotionData.NAME_DAMAGE || uNextMot == CRaceMotionData.NAME_DAMAGE_BACK || uNextMot == CRaceMotionData.NAME_DAMAGE_FLYING || uNextMot == CRaceMotionData.NAME_DAMAGE_FLYING_BACK)
			{
				if (!m_isMain)
				{
					Logn(0, "???ΰ??? ??϶?? ?̵????̶? ?????? ?????? ?????? ????");
					return false ? 1 : 0;
				}
			}
    
			if (uNextMot != CRaceMotionData.NAME_RUN && uNextMot != CRaceMotionData.NAME_WALK && !__IsMovingSkill(c_rkSetMotData.uSkill))
			{
				__OnStop();
			}
		}
		else
		{
			if (uNextMot == CRaceMotionData.NAME_RUN || __IsMovingSkill(c_rkSetMotData.uSkill))
			{
				__OnMove();
			}
		}
    
		if (__IsHiding())
		{
			__ShowEvent();
		}
    
    
		if (-1 != m_iFishingEffectID)
		{
			CEffectManager rkEftMgr = CEffectManager.Instance();
			 rkEftMgr.DeactiveEffectInstance(m_iFishingEffectID);
    
			m_iFishingEffectID = -1;
		}
    
		if (m_pkHorse)
		{
			ushort wMotionIndex = GET_MOTION_INDEX(dwMotKey);
			ushort wMotionSubIndex = GET_MOTION_SUB_INDEX(dwMotKey);
			uint dwChildMotKey = MAKE_RANDOM_MOTION_KEY(m_pkHorse.m_wcurMotionMode, wMotionIndex, wMotionSubIndex);
    
			if (CRaceMotionData.NAME_DEAD == wMotionIndex)
			{
				CGraphicThingInstance.ChangeMotion(dwMotKey, c_rkSetMotData.iLoopCount, c_rkSetMotData.fSpeedRatio);
			}
			else
			{
				CGraphicThingInstance.SetMotion(dwMotKey, c_rkSetMotData.fBlendTime, c_rkSetMotData.iLoopCount, c_rkSetMotData.fSpeedRatio);
			}
    
			m_pkHorse.SetMotion(dwChildMotKey, c_rkSetMotData.fBlendTime, c_rkSetMotData.iLoopCount, c_rkSetMotData.fSpeedRatio);
			m_pkHorse.__BindMotionData(dwChildMotKey);
    
			if (c_rkSetMotData.iLoopCount)
			{
				m_pkHorse.m_kCurMotNode.iMotionType = MOTION_TYPE_ONCE;
			}
			else
			{
				m_pkHorse.m_kCurMotNode.iMotionType = MOTION_TYPE_LOOP;
			}
    
			m_pkHorse.m_kCurMotNode.dwFrameCount = m_pkHorse.GetMotionDuration(dwChildMotKey) / (1.0f / g_fGameFPS);
			m_pkHorse.m_kCurMotNode.dwcurFrame = 0;
			m_pkHorse.m_kCurMotNode.dwMotionKey = dwChildMotKey;
		}
		else
		{
			CGraphicThingInstance.SetMotion(dwMotKey, c_rkSetMotData.fBlendTime, c_rkSetMotData.iLoopCount, c_rkSetMotData.fSpeedRatio);
		}
    
		__HideWeaponTrace();
    
		if (__BindMotionData(dwMotKey))
		{
			int iLoopCount = __GetLoopCount();
			SetMotionLoopCount(iLoopCount);
    
			if (__CanAttack())
			{
	#if DEBUG
				__ShowWeaponTrace();
	#endif
    
				m_HitDataMap.clear();
			}
    
			if (__IsComboAttacking())
			{
				if (!__CanNextComboAttack())
				{
					m_dwcurComboIndex = 0;
				}
			}
		}
    
		return dwMotKey;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool __BindMotionData(uint dwMotionKey)
	{
		if (!m_pkCurRaceData.GetMotionDataPointer(dwMotionKey, m_pkCurRaceMotionData))
		{
			Tracen("Failed to bind motion.");
			m_pkCurRaceMotionData = null;
			m_dwcurComboIndex = 0;
			return false;
		}
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public int __GetLoopCount()
	{
		if (!m_pkCurRaceMotionData)
		{
			TraceError("CActorInstance::__GetLoopCount() - m_pkCurRaceMotionData==NULL");
			return -1;
		}
    
		return m_pkCurRaceMotionData.GetLoopCount();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool __CanAttack()
	{
		if (!m_pkCurRaceMotionData)
		{
			TraceError("CActorInstance::__CanAttack() - m_pkCurRaceMotionData==NULL");
			return false;
		}
    
		if (!m_pkCurRaceMotionData.isAttackingMotion())
		{
			return false;
		}
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool __CanNextComboAttack()
	{
		if (!m_pkCurRaceMotionData)
		{
			TraceError("CActorInstance::__CanNextComboAttack() - m_pkCurRaceMotionData==NULL");
			return false;
		}
    
		if (!m_pkCurRaceMotionData.IsComboInputTimeData())
		{
			return false;
		}
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool __IsComboAttacking()
	{
		if (0 == m_dwcurComboIndex)
		{
			return false;
		}
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool __IsNeedFlyTargetMotion()
	{
		if (!m_pkCurRaceMotionData)
		{
			return true;
		}
    
		for (uint LaniatusDefVariables = 0; LaniatusDefVariables < m_pkCurRaceMotionData.GetMotionEventDataCount(); ++i)
		{
			CRaceMotionData.TMotionEventData c_pData;
			if (!m_pkCurRaceMotionData.GetMotionEventDataPointer(i, c_pData))
			{
				continue;
			}
    
	#if ENABLE_WOLFMAN
			if (c_pData.iType == CRaceMotionData.MOTION_EVENT_TYPE_UNK11)
			{
				return true;
			}
	#endif
    
			if (c_pData.iType == CRaceMotionData.MOTION_EVENT_TYPE_WARP)
			{
				return true;
			}
    
			if (c_pData.iType == CRaceMotionData.MOTION_EVENT_TYPE_FLY)
			{
				return true;
			}
    
			if (c_pData.iType == CRaceMotionData.MOTION_EVENT_TYPE_EFFECT_TO_TARGET)
			{
				return true;
			}
		}
    
		return false;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool __HasMotionFlyEvent()
	{
		if (!m_pkCurRaceMotionData)
		{
			return true;
		}
    
		for (uint LaniatusDefVariables = 0; LaniatusDefVariables < m_pkCurRaceMotionData.GetMotionEventDataCount(); ++i)
		{
			CRaceMotionData.TMotionEventData c_pData;
			if (!m_pkCurRaceMotionData.GetMotionEventDataPointer(i, c_pData))
			{
				continue;
			}
    
			if (c_pData.iType == CRaceMotionData.MOTION_EVENT_TYPE_FLY)
			{
				return true;
			}
		}
		return false;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool __IsWaitMotion()
	{
		return (__GetMotionType() == CRaceMotionData.TYPE_WAIT);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool __IsMoveMotion()
	{
		return (__GetMotionType() == CRaceMotionData.TYPE_MOVE);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool __IsAttackMotion()
	{
		return (__GetMotionType() == CRaceMotionData.TYPE_ATTACK);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool __IsComboAttackMotion()
	{
		return (__GetMotionType() == CRaceMotionData.TYPE_COMBO);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool __IsDamageMotion()
	{
		return (__GetMotionType() == CRaceMotionData.TYPE_DAMAGE);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool __IsKnockDownMotion()
	{
		return (__GetMotionType() == CRaceMotionData.TYPE_KNOCKDOWN);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool __IsDieMotion()
	{
		if (__IsKnockDownMotion())
		{
			return true;
		}
    
		return (__GetMotionType() == CRaceMotionData.TYPE_DIE);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool __IsStandUpMotion()
	{
		return (__GetMotionType() == CRaceMotionData.TYPE_STANDUP);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void MotionEventProcess()
	{
		if (!m_pkCurRaceMotionData)
		{
			return;
		}
    
		for (uint LaniatusDefVariables = 0; LaniatusDefVariables < m_pkCurRaceMotionData.GetMotionEventDataCount(); ++i)
		{
			CRaceMotionData.TMotionEventData c_pData;
			if (!m_pkCurRaceMotionData.GetMotionEventDataPointer(i, c_pData))
			{
				continue;
			}
    
			MotionEventProcess(m_kCurMotNode.dwcurFrame, i, c_pData);
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SoundEventProcess(bool bCheckFrequency)
	{
		if (!m_pkCurRaceMotionData)
		{
			return;
		}
    
		CSoundManager rkSndMgr = CSoundManager.Instance();
		List<SSoundInstance> c_pkVct_kSndInst = m_pkCurRaceMotionData.GetSoundInstanceVectorPointer();
		rkSndMgr.UpdateSoundInstance(m_x, m_y, m_z, m_kCurMotNode.dwcurFrame, c_pkVct_kSndInst, bCheckFrequency);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void MotionEventProcess(uint dwcurFrame, int iIndex, CRaceMotionData.TMotionEventData c_pData)
	{
		if (c_pData.dwFrame != dwcurFrame)
		{
			return;
		}
    
		switch (c_pData.iType)
		{
			case CRaceMotionData.MOTION_EVENT_TYPE_EFFECT:
				ProcessMotionEventEffectEvent(c_pData);
				break;
    
			case CRaceMotionData.MOTION_EVENT_TYPE_SCREEN_WAVING:
				CGameEventManager.Instance().ProcessEventScreenWaving(this, (struct NMotionEvent.SMotionEventDataScreenWaving)c_pData);
				break;
    
			case CRaceMotionData.MOTION_EVENT_TYPE_SPECIAL_ATTACKING:
				ProcessMotionEventSpecialAttacking(iIndex, c_pData);
				break;
    
			case CRaceMotionData.MOTION_EVENT_TYPE_SOUND:
				ProcessMotionEventSound(c_pData);
				break;
    
			case CRaceMotionData.MOTION_EVENT_TYPE_FLY:
				ProcessMotionEventFly(c_pData);
				break;
    
			case CRaceMotionData.MOTION_EVENT_TYPE_CHARACTER_SHOW:
				__ShowEvent();
				break;
    
			case CRaceMotionData.MOTION_EVENT_TYPE_CHARACTER_HIDE:
				__HideEvent();
				break;
    
			case CRaceMotionData.MOTION_EVENT_TYPE_WARP:
				ProcessMotionEventWarp(c_pData);
				break;
    
			case CRaceMotionData.MOTION_EVENT_TYPE_EFFECT_TO_TARGET:
				ProcessMotionEventEffectToTargetEvent(c_pData);
				break;
    
	#if ENABLE_WOLFMAN
	//# Laniatus Games Studio Inc. | TODO TASK: C# does not allow fall-through from a non-empty 'case':
			case CRaceMotionData.MOTION_EVENT_TYPE_UNK11:
				ProcessMotionEventUnk11(dwcurFrame, iIndex, c_pData);
				break;
			case CRaceMotionData.MOTION_EVENT_TYPE_UNK12:
				ProcessMotionEventUnk12(dwcurFrame, iIndex, c_pData);
				break;
	#endif
	break;
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __ShowEvent()
	{
		m_isHiding = false;
		RestoreRenderMode();
		SetAlphaValue(1.0f);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __HideEvent()
	{
		m_isHiding = true;
		SetBlendRenderMode();
		SetAlphaValue(0.0f);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool __IsHiding()
	{
		return m_isHiding;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void ProcessMotionEventEffectEvent(CRaceMotionData.TMotionEventData c_pData)
	{
		if (!IsPC() && !IsShowMonsterEffects())
		{
			return;
		}
    
		if (CRaceMotionData.MOTION_EVENT_TYPE_EFFECT != c_pData.iType)
		{
			return;
		}
    
		NMotionEvent.SMotionEventDataEffect c_pEffectData = (struct NMotionEvent.SMotionEventDataEffect)c_pData;
    
		if (c_pEffectData.isIndependent)
		{
			int iIndex = CEffectManager.Instance().CreateEffect(c_pEffectData.dwEffectIndex, D3DXVECTOR3(0.0f, 0.0f, 0.0f), D3DXVECTOR3(0.0f, 0.0f, 0.0f));
    
			_D3DMATRIX matLocalPosition = new _D3DMATRIX();
			D3DXMatrixTranslation(matLocalPosition, c_pEffectData.v3EffectPosition.x, c_pEffectData.v3EffectPosition.y, c_pEffectData.v3EffectPosition.z);
    
			_D3DMATRIX matWorld = new _D3DMATRIX();
	//# Laniatus Games Studio Inc. | TODO TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'CopyFrom' method should be created:
	//Original Metin2 CPlus Line: matWorld = matLocalPosition;
			matWorld.CopyFrom(matLocalPosition);
			matWorld *= m_worldMatrix;
    
			CEffectManager.Instance().SelectEffectInstance(iIndex);
			CEffectManager.Instance().SetEffectInstanceGlobalMatrix(matWorld);
			return;
		}
    
		if (c_pEffectData.isAttaching)
		{
			if (c_pEffectData.isFollowing)
			{
				AttachEffectByID(0, c_pEffectData.strAttachingBoneName.c_str(), c_pEffectData.dwEffectIndex, c_pEffectData.v3EffectPosition);
			}
			else
			{
				int iBoneIndex;
				uint dwPartIndex = 0;
				if (FindBoneIndex(dwPartIndex, c_pEffectData.strAttachingBoneName.c_str(), iBoneIndex))
				{
					_D3DMATRIX pBoneMat;
					GetBoneMatrix(dwPartIndex, iBoneIndex, pBoneMat);
    
					_D3DMATRIX matLocalPosition = new _D3DMATRIX();
					D3DXMatrixTranslation(matLocalPosition, c_pEffectData.v3EffectPosition.x, c_pEffectData.v3EffectPosition.y, c_pEffectData.v3EffectPosition.z);
    
					_D3DMATRIX matWorld = new _D3DMATRIX();
	//# Laniatus Games Studio Inc. | TODO TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'CopyFrom' method should be created:
	//Original Metin2 CPlus Line: matWorld = *pBoneMat;
					matWorld.CopyFrom(pBoneMat);
					matWorld *= matLocalPosition;
					matWorld *= m_worldMatrix;
    
					int iIndex = CEffectManager.Instance().CreateEffect(c_pEffectData.dwEffectIndex, c_pEffectData.v3EffectPosition, D3DXVECTOR3(0.0f, 0.0f, 0.0f));
					CEffectManager.Instance().SelectEffectInstance(iIndex);
					CEffectManager.Instance().SetEffectInstanceGlobalMatrix(matWorld);
				}
			}
		}
		else
		{
			AttachEffectByID(0, null, c_pEffectData.dwEffectIndex, c_pEffectData.v3EffectPosition);
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void ProcessMotionEventEffectToTargetEvent(CRaceMotionData.TMotionEventData c_pData)
	{
		if (!IsPC() && !IsShowMonsterEffects())
		{
			return;
		}
    
		if (CRaceMotionData.MOTION_EVENT_TYPE_EFFECT_TO_TARGET != c_pData.iType)
		{
			return;
		}
    
		NMotionEvent.SMotionEventDataEffectToTarget c_pEffectToTargetData = (struct NMotionEvent.SMotionEventDataEffectToTarget)c_pData;
    
		if (c_pEffectToTargetData.isFishingEffect)
		{
			CEffectManager rkEftMgr = CEffectManager.Instance();
    
			if (-1 != m_iFishingEffectID)
			{
				 rkEftMgr.DeactiveEffectInstance(m_iFishingEffectID);
			}
    
			m_iFishingEffectID = rkEftMgr.CreateEffect(c_pEffectToTargetData.dwEffectIndex, m_v3FishingPosition, D3DXVECTOR3(0.0f, 0.0f, 0.0f));
		}
		else
		{
			if (!m_kFlyTarget.IsValidTarget())
			{
				return;
			}
    
			if (c_pEffectToTargetData.isFollowing && IsFlyTargetObject())
			{
				CActorInstance pTargetInstance = (CActorInstance)m_kFlyTarget.GetFlyTarget();
				_D3DVECTOR v3Position = new _D3DVECTOR(c_pEffectToTargetData.v3EffectPosition.x, c_pEffectToTargetData.v3EffectPosition.y, c_pEffectToTargetData.v3EffectPosition.z);
				pTargetInstance.AttachEffectByID(0, null, c_pEffectToTargetData.dwEffectIndex, v3Position);
			}
			else
			{
				_D3DVECTOR c_rv3FlyTarget = m_kFlyTarget.GetFlyTargetPosition();
				_D3DVECTOR v3Position = new _D3DVECTOR(c_rv3FlyTarget.x + c_pEffectToTargetData.v3EffectPosition.x, c_rv3FlyTarget.y + c_pEffectToTargetData.v3EffectPosition.y, c_rv3FlyTarget.z + c_pEffectToTargetData.v3EffectPosition.z);
				CEffectManager.Instance().CreateEffect(c_pEffectToTargetData.dwEffectIndex, v3Position, D3DXVECTOR3(0.0f, 0.0f, 0.0f));
			}
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void ProcessMotionEventSpecialAttacking(int iMotionEventIndex, CRaceMotionData.TMotionEventData c_pData)
	{
		if (CRaceMotionData.MOTION_EVENT_TYPE_SPECIAL_ATTACKING != c_pData.iType)
		{
			return;
		}
    
		NMotionEvent.SMotionEventDataAttack c_pAttackingData = (struct NMotionEvent.SMotionEventDataAttack)c_pData;
    
		float fRadian = ((270.0f + 360.0f - GetRotation()) * (((float) 3.141592654f) / 180.0f));
		m_kSplashArea.isEnableHitProcess = c_pAttackingData.isEnableHitProcess;
		m_kSplashArea.uSkill = m_kCurMotNode.uSkill;
		m_kSplashArea.MotionKey = m_kCurMotNode.dwMotionKey;
		m_kSplashArea.fDisappearingTime = GetLocalTime() + c_pAttackingData.fDurationTime;
		m_kSplashArea.c_pAttackingEvent = c_pAttackingData;
		m_kSplashArea.HittedInstanceMap.clear();
    
		m_kSplashArea.SphereInstanceVector.clear();
		m_kSplashArea.SphereInstanceVector.resize(c_pAttackingData.CollisionData.SphereDataVector.size());
		for (uint LaniatusDefVariables = 0; LaniatusDefVariables < c_pAttackingData.CollisionData.SphereDataVector.size(); ++i)
		{
			SSphereData c_rSphereData = c_pAttackingData.CollisionData.SphereDataVector[LaniatusDefVariables].GetAttribute();
			CDynamicSphereInstance rSphereInstance = m_kSplashArea.SphereInstanceVector[LaniatusDefVariables];
    
			rSphereInstance.fRadius = c_rSphereData.fRadius;
    
			rSphereInstance.v3Position.x = m_x + c_rSphereData.v3Position.x * sinf(fRadian) + c_rSphereData.v3Position.y * cosf(fRadian);
			rSphereInstance.v3Position.y = m_y + c_rSphereData.v3Position.x * cosf(fRadian) - c_rSphereData.v3Position.y * sinf(fRadian);
			rSphereInstance.v3Position.z = m_z + c_rSphereData.v3Position.z;
			rSphereInstance.v3LastPosition = rSphereInstance.v3Position;
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void ProcessMotionEventSound(CRaceMotionData.TMotionEventData c_pData)
	{
		if (CRaceMotionData.MOTION_EVENT_TYPE_SOUND != c_pData.iType)
		{
			return;
		}
    
		NMotionEvent.SMotionEventDataSound c_pSoundData = (struct NMotionEvent.SMotionEventDataSound)c_pData;
    
		Tracenf("PLAY SOUND: %s", c_pSoundData.strSoundFileName.c_str());
		CSoundManager.Instance().PlaySound3D(m_x, m_y, m_z, c_pSoundData.strSoundFileName.c_str());
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void ProcessMotionEventFly(CRaceMotionData.TMotionEventData c_pData)
	{
		if (!IsPC() && !IsShowMonsterEffects())
		{
			return;
		}
    
		if (CRaceMotionData.MOTION_EVENT_TYPE_FLY != c_pData.iType)
		{
			return;
		}
    
		NMotionEvent.SMotionEventDataFly c_pFlyData = (struct NMotionEvent.SMotionEventDataFly)c_pData;
    
		if (m_kFlyTarget.IsValidTarget())
		{
			CFlyingManager rfm = CFlyingManager.Instance();
    
			_D3DVECTOR v3Start = new _D3DVECTOR(c_pFlyData.v3FlyPosition);
			v3Start += m_v3Position;
    
			if (c_pFlyData.isAttaching)
			{
				_D3DMATRIX pBoneMat;
				int iBoneIndex;
				uint dwPartIndex = 0;
    
				if (FindBoneIndex(dwPartIndex, c_pFlyData.strAttachingBoneName.c_str(), iBoneIndex))
				{
				if (GetBoneMatrix(dwPartIndex, iBoneIndex, pBoneMat))
				{
					v3Start.x += pBoneMat._41;
					v3Start.y += pBoneMat._42;
					v3Start.z += pBoneMat._43;
				}
				}
			}
    
			CFlyingInstance pInstance = null;
			if (m_eRace == CRaceData.RACE_ASSASSIN_W || m_eRace == CRaceData.RACE_ASSASSIN_M)
			{
				CRaceMotionData pRaceMotionData = m_pkCurRaceMotionData;
				if (pRaceMotionData == null)
				{
					return;
				}
    
				NRaceData.TMotionAttackData c_pData = m_pkCurRaceMotionData.GetMotionAttackDataPointer();
				if (NRaceData.MOTION_TYPE_NORMAL == c_pData.iMotionType)
				{
					if (IsEqippedQuiver())
					{
						pInstance = rfm.CreateIndexedFlyingInstanceFlyTarget(GetQuiverEffectID(), v3Start, m_kFlyTarget);
					}
					else
					{
						pInstance = rfm.CreateFlyingInstanceFlyTarget(c_pFlyData.dwFlyIndex, v3Start, m_kFlyTarget, true);
					}
				}
				else if (__IsMountingHorse())
				{
					if (IsEqippedQuiver())
					{
						pInstance = rfm.CreateIndexedFlyingInstanceFlyTarget(GetQuiverEffectID(), v3Start, m_kFlyTarget);
					}
					else
					{
						pInstance = rfm.CreateFlyingInstanceFlyTarget(c_pFlyData.dwFlyIndex, v3Start, m_kFlyTarget, true);
					}
				}
				else
				{
					pInstance = rfm.CreateFlyingInstanceFlyTarget(c_pFlyData.dwFlyIndex, v3Start, m_kFlyTarget, true);
				}
			}
			else
			{
				pInstance = rfm.CreateFlyingInstanceFlyTarget(c_pFlyData.dwFlyIndex, v3Start, m_kFlyTarget, true);
			}
    
			if (pInstance != null)
			{
				pInstance.SetEventHandler(m_pFlyEventHandler);
				pInstance.SetOwner(this);
				pInstance.SetSkillIndex(m_kCurMotNode.uSkill);
			}
    
			if (m_pFlyEventHandler)
			{
				m_pFlyEventHandler.OnShoot(m_kCurMotNode.uSkill);
			}
		}
		else
		{
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void ProcessMotionEventWarp(CRaceMotionData.TMotionEventData c_pData)
	{
		if (CRaceMotionData.MOTION_EVENT_TYPE_WARP != c_pData.iType)
		{
			return;
		}
    
		const float sc_fDistanceFromTarget = 270.0f;
    
		if (m_kFlyTarget.IsValidTarget())
		{
			_D3DVECTOR v3MainPosition = new _D3DVECTOR(m_x, m_y, m_z);
			_D3DVECTOR c_rv3TargetPosition = __GetFlyTargetPosition();
    
			_D3DVECTOR v3Distance = c_rv3TargetPosition - v3MainPosition;
			D3DXVec3Normalize(v3Distance, v3Distance);
			TPixelPosition DestPixelPosition = c_rv3TargetPosition - (v3Distance * sc_fDistanceFromTarget);
    
			IBackground rkBG = GetBackground();
			if (!rkBG.IsBlock(DestPixelPosition.x, -DestPixelPosition.y))
			{
				SetPixelPosition(DestPixelPosition);
			}
    
			LookAt(c_rv3TargetPosition.x, c_rv3TargetPosition.y);
    
			__OnWarp();
		}
		else
		{
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void ProcessMotionEventUnk11(uint dwcurFrame, int iIndex, CRaceMotionData.TMotionEventData c_pData)
	{
		if (CRaceMotionData.MOTION_EVENT_TYPE_UNK11 != c_pData.iType)
		{
			return;
		}
    
		NMotionEvent.SMotionEventDataUnk11 c_pUnk11TargetData = (struct NMotionEvent.SMotionEventDataUnk11)c_pData;
    
		{
			const float sc_fDistanceFromTarget = 270.0f;
    
			if (m_kFlyTarget.IsValidTarget())
			{
				_D3DVECTOR v3MainPosition = new _D3DVECTOR(m_x, m_y, m_z);
				_D3DVECTOR c_rv3TargetPosition = __GetFlyTargetPosition();
    
				_D3DVECTOR v3Distance = c_rv3TargetPosition - v3MainPosition;
				D3DXVec3Normalize(v3Distance, v3Distance);
				TPixelPosition DestPixelPosition = c_rv3TargetPosition - (v3Distance * (sc_fDistanceFromTarget + c_pUnk11TargetData.iAniSpeed));
    
				IBackground rkBG = GetBackground();
				if (!rkBG.IsBlock(DestPixelPosition.x, -DestPixelPosition.y))
				{
					SetPixelPosition(DestPixelPosition);
				}
				LookAt(c_rv3TargetPosition.x, c_rv3TargetPosition.y);
				__OnWarp();
			}
		}
    
		return;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void ProcessMotionEventUnk12(uint dwcurFrame, int iIndex, CRaceMotionData.TMotionEventData c_pData)
	{
		if (CRaceMotionData.MOTION_EVENT_TYPE_UNK12 != c_pData.iType)
		{
			return;
		}
    
		NMotionEvent.SMotionEventDataUnk12 c_pUnk12TargetData = (struct NMotionEvent.SMotionEventDataUnk12)c_pData;
    
		{
		}
    
		return;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public TPixelPosition NEW_GetLastPixelPositionRef()
	{
		GetBlendingPosition(m_kPPosLast);
		m_kPPosLast.y = -m_kPPosLast.y;
    
		return m_kPPosLast;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public _D3DVECTOR GetPositionVectorRef()
	{
		m_v3Pos.x = m_x;
		m_v3Pos.y = m_y;
		m_v3Pos.z = m_z;
		return m_v3Pos;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public _D3DVECTOR GetMovementVectorRef()
	{
		if (m_pkHorse)
		{
			return m_pkHorse.GetMovementVectorRef();
		}
    
		return m_v3Movement;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void NEW_SetAtkPixelPosition(in TPixelPosition c_rkPPosAtk)
	{
		m_kPPosAtk = c_rkPPosAtk;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetCurPixelPosition(in TPixelPosition c_rkPPosCur)
	{
		_D3DVECTOR v3PosCur = new _D3DVECTOR();
		v3PosCur.x = +c_rkPPosCur.x;
		v3PosCur.y = -c_rkPPosCur.y;
		v3PosCur.z = +c_rkPPosCur.z;
    
		SetPixelPosition(v3PosCur);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void NEW_SetSrcPixelPosition(in TPixelPosition c_rkPPosSrc)
	{
		m_kPPosSrc = c_rkPPosSrc;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void NEW_SetDstPixelPositionZ(float z)
	{
		m_kPPosDst.z = z;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void NEW_SetDstPixelPosition(in TPixelPosition c_rkPPosDst)
	{
		m_kPPosDst = c_rkPPosDst;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public TPixelPosition NEW_GetAtkPixelPositionRef()
	{
		return m_kPPosAtk;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public TPixelPosition NEW_GetSrcPixelPositionRef()
	{
		return m_kPPosSrc;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public TPixelPosition NEW_GetDstPixelPositionRef()
	{
		return m_kPPosDst;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public TPixelPosition NEW_GetCurPixelPositionRef()
	{
		m_kPPosCur.x = +m_x;
		m_kPPosCur.y = -m_y;
		m_kPPosCur.z = +m_z;
    
		return m_kPPosCur;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void GetPixelPosition(TPixelPosition pPixelPosition)
	{
		pPixelPosition.x = m_x;
		pPixelPosition.y = m_y;
		pPixelPosition.z = m_z;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetPixelPosition(in TPixelPosition c_rPixelPos)
	{
		if (m_pkTree)
		{
			__SetTreePosition(c_rPixelPos.x, c_rPixelPos.y, c_rPixelPos.z);
		}
    
		if (m_pkHorse)
		{
			m_pkHorse.SetPixelPosition(c_rPixelPos);
		}
    
		m_x = c_rPixelPos.x;
		m_y = c_rPixelPos.y;
		m_z = c_rPixelPos.z;
		m_bNeedUpdateCollision = true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __InitializePositionData()
	{
		m_dwShakeTime = 0;
    
		m_x = 0.0f;
		m_y = 0.0f;
		m_z = 0.0f;
		m_bNeedUpdateCollision = false;
    
		m_kPPosAtk = m_kPPosLast = m_kPPosDst = m_kPPosCur = m_kPPosSrc = TPixelPosition(0.0f, 0.0f, 0.0f);
    
		__InitializeMovement();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool IsDirLine()
	{
		return ms_isDirLine;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void ShowDirectionLine(bool isVisible)
	{
		ms_isDirLine = isVisible;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetMaterialColor(uint dwColor)
	{
		if (m_pkHorse)
		{
			m_pkHorse.SetMaterialColor(dwColor);
		}
    
		m_dwMtrlColor &= 0xff000000;
		m_dwMtrlColor |= (dwColor & 0x00ffffff);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetMaterialAlpha(uint dwAlpha)
	{
		m_dwMtrlAlpha = dwAlpha;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void OnRender()
	{
		D3DMATERIAL8 kMtrl = new D3DMATERIAL8();
		(CStateManager.Instance()).GetMaterial(kMtrl);
    
		kMtrl.Diffuse = D3DXCOLOR(m_dwMtrlColor);
		(CStateManager.Instance()).SetMaterial(kMtrl);
    
		(CStateManager.Instance()).SaveRenderState(D3DRS_CULLMODE, D3DCULL_NONE);
    
		switch (m_iRenderMode)
		{
			case RENDER_MODE_NORMAL:
				BeginDiffuseRender();
					RenderWithOneTexture();
				EndDiffuseRender();
				BeginOpacityRender();
					BlendRenderWithOneTexture();
				EndOpacityRender();
				break;
			case RENDER_MODE_BLEND:
				if (m_fAlphaValue == 1.0f)
				{
					BeginDiffuseRender();
						RenderWithOneTexture();
					EndDiffuseRender();
					BeginOpacityRender();
						BlendRenderWithOneTexture();
					EndOpacityRender();
				}
				else if (m_fAlphaValue > 0.0f)
				{
					BeginBlendRender();
						RenderWithOneTexture();
						BlendRenderWithOneTexture();
					EndBlendRender();
				}
				break;
			case RENDER_MODE_ADD:
				BeginAddRender();
					RenderWithOneTexture();
					BlendRenderWithOneTexture();
				EndAddRender();
				break;
			case RENDER_MODE_MODULATE:
				BeginModulateRender();
					RenderWithOneTexture();
					BlendRenderWithOneTexture();
				EndModulateRender();
				break;
		}
    
		(CStateManager.Instance()).RestoreRenderState(D3DRS_CULLMODE);
    
		kMtrl.Diffuse = D3DXCOLOR(0xffffffff);
		(CStateManager.Instance()).SetMaterial(kMtrl);
    
		if (ms_isDirLine)
		{
			_D3DVECTOR kD3DVt3Cur = new _D3DVECTOR(m_x, m_y, m_z);
    
			_D3DVECTOR kD3DVt3LookDir = new _D3DVECTOR(0.0f, -1.0f, 0.0f);
			_D3DMATRIX kD3DMatLook = new _D3DMATRIX();
			D3DXMatrixRotationZ(kD3DMatLook, ((GetRotation()) * (((float) 3.141592654f) / 180.0f)));
			D3DXVec3TransformCoord(kD3DVt3LookDir, kD3DVt3LookDir, kD3DMatLook);
			D3DXVec3Scale(kD3DVt3LookDir, kD3DVt3LookDir, 200.0f);
			D3DXVec3Add(kD3DVt3LookDir, kD3DVt3LookDir, kD3DVt3Cur);
    
			_D3DVECTOR kD3DVt3AdvDir = new _D3DVECTOR(0.0f, -1.0f, 0.0f);
			_D3DMATRIX kD3DMatAdv = new _D3DMATRIX();
			D3DXMatrixRotationZ(kD3DMatAdv, ((GetAdvancingRotation()) * (((float) 3.141592654f) / 180.0f)));
			D3DXVec3TransformCoord(kD3DVt3AdvDir, kD3DVt3AdvDir, kD3DMatAdv);
			D3DXVec3Scale(kD3DVt3AdvDir, kD3DVt3AdvDir, 200.0f);
			D3DXVec3Add(kD3DVt3AdvDir, kD3DVt3AdvDir, kD3DVt3Cur);
    
	//# Laniatus Games Studio Inc. |: This static local variable declaration (not allowed in C#) has been moved just prior to the method:
	//		static CScreen s_kScreen;
    
			(CStateManager.Instance()).SaveTextureStageState(0, D3DTSS_COLORARG1, D3DTA_DIFFUSE);
			(CStateManager.Instance()).SaveTextureStageState(0, D3DTSS_COLOROP, D3DTOP_SELECTARG1);
			(CStateManager.Instance()).SaveTextureStageState(0, D3DTSS_ALPHAOP, D3DTOP_DISABLE);
			(CStateManager.Instance()).SaveRenderState(D3DRS_ZENABLE, false);
			(CStateManager.Instance()).SetRenderState(D3DRS_LIGHTING, false);
    
			OnRender_s_kScreen.SetDiffuseColor(1.0f, 1.0f, 0.0f);
			OnRender_s_kScreen.RenderLine3d(kD3DVt3Cur.x, kD3DVt3Cur.y, kD3DVt3Cur.z, kD3DVt3AdvDir.x, kD3DVt3AdvDir.y, kD3DVt3AdvDir.z);
    
			OnRender_s_kScreen.SetDiffuseColor(0.0f, 1.0f, 1.0f);
			OnRender_s_kScreen.RenderLine3d(kD3DVt3Cur.x, kD3DVt3Cur.y, kD3DVt3Cur.z, kD3DVt3LookDir.x, kD3DVt3LookDir.y, kD3DVt3LookDir.z);
    
			(CStateManager.Instance()).SetRenderState(D3DRS_LIGHTING, true);
			(CStateManager.Instance()).RestoreRenderState(D3DRS_ZENABLE);
    
			(CStateManager.Instance()).RestoreTextureStageState(0, D3DTSS_COLORARG1);
			(CStateManager.Instance()).RestoreTextureStageState(0, D3DTSS_COLOROP);
			(CStateManager.Instance()).RestoreTextureStageState(0, D3DTSS_ALPHAOP);
			(CStateManager.Instance()).RestoreVertexShader();
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void BeginDiffuseRender()
	{
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLORARG1, D3DTA_TEXTURE);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLORARG2, D3DTA_DIFFUSE);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLOROP, D3DTOP_MODULATE);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_ALPHAARG1, D3DTA_TEXTURE);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_ALPHAARG2, D3DTA_DIFFUSE);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_ALPHAOP, D3DTOP_MODULATE);
    
		(CStateManager.Instance()).SaveRenderState(D3DRS_ALPHABLENDENABLE, false);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void EndDiffuseRender()
	{
		(CStateManager.Instance()).RestoreRenderState(D3DRS_ALPHABLENDENABLE);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void BeginOpacityRender()
	{
		(CStateManager.Instance()).SaveRenderState(D3DRS_ALPHATESTENABLE, true);
		(CStateManager.Instance()).SaveRenderState(D3DRS_ALPHAREF, 0);
		(CStateManager.Instance()).SaveRenderState(D3DRS_ALPHAFUNC, D3DCMP_GREATER);
    
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_ALPHAARG1, D3DTA_TEXTURE);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_ALPHAARG2, D3DTA_DIFFUSE);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_ALPHAOP, D3DTOP_MODULATE);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void EndOpacityRender()
	{
		(CStateManager.Instance()).RestoreRenderState(D3DRS_ALPHATESTENABLE);
		(CStateManager.Instance()).RestoreRenderState(D3DRS_ALPHAREF);
		(CStateManager.Instance()).RestoreRenderState(D3DRS_ALPHAFUNC);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void BeginBlendRender()
	{
		(CStateManager.Instance()).SaveRenderState(D3DRS_ALPHABLENDENABLE, true);
		(CStateManager.Instance()).SaveRenderState(D3DRS_SRCBLEND, D3DBLEND_SRCALPHA);
		(CStateManager.Instance()).SaveRenderState(D3DRS_DESTBLEND, D3DBLEND_INVSRCALPHA);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLORARG1, D3DTA_TEXTURE);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLORARG2, D3DTA_DIFFUSE);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLOROP, D3DTOP_MODULATE);
		(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_COLOROP, D3DTOP_DISABLE);
		(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_ALPHAOP, D3DTOP_DISABLE);
    
		(CStateManager.Instance()).SetRenderState(D3DRS_TEXTUREFACTOR, D3DXCOLOR(1.0f, 1.0f, 1.0f, m_fAlphaValue));
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_ALPHAARG2, D3DTA_TFACTOR);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_ALPHAOP, D3DTOP_SELECTARG2);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void EndBlendRender()
	{
		(CStateManager.Instance()).RestoreRenderState(D3DRS_ALPHABLENDENABLE);
		(CStateManager.Instance()).RestoreRenderState(D3DRS_SRCBLEND);
		(CStateManager.Instance()).RestoreRenderState(D3DRS_DESTBLEND);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void BeginAddRender()
	{
		(CStateManager.Instance()).SetRenderState(D3DRS_TEXTUREFACTOR, m_AddColor);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLORARG1, D3DTA_TEXTURE);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLORARG2, D3DTA_DIFFUSE);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLOROP, D3DTOP_MODULATE);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_ALPHAARG1, D3DTA_TEXTURE);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_ALPHAARG2, D3DTA_DIFFUSE);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_ALPHAOP, D3DTOP_MODULATE);
    
		(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_COLORARG1, D3DTA_CURRENT);
		(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_COLORARG2, D3DTA_TFACTOR);
		(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_COLOROP, D3DTOP_ADD);
		(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_ALPHAOP, D3DTOP_DISABLE);
    
		(CStateManager.Instance()).SaveRenderState(D3DRS_ALPHABLENDENABLE, false);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void EndAddRender()
	{
		(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_COLOROP, D3DTOP_DISABLE);
		(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_ALPHAOP, D3DTOP_DISABLE);
		(CStateManager.Instance()).RestoreRenderState(D3DRS_ALPHABLENDENABLE);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void RestoreRenderMode()
	{
		m_iRenderMode = RENDER_MODE_NORMAL;
		if (m_kBlendAlpha.m_isBlending)
		{
			m_kBlendAlpha.m_iOldRenderMode = m_iRenderMode;
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetAddRenderMode()
	{
		m_iRenderMode = RENDER_MODE_ADD;
		if (m_kBlendAlpha.m_isBlending)
		{
			m_kBlendAlpha.m_iOldRenderMode = m_iRenderMode;
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetRenderMode(int iRenderMode)
	{
		m_iRenderMode = iRenderMode;
		if (m_kBlendAlpha.m_isBlending)
		{
			m_kBlendAlpha.m_iOldRenderMode = iRenderMode;
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetAddColor(in D3DXCOLOR c_rColor)
	{
		m_AddColor = c_rColor;
		m_AddColor.a = 1.0f;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void BeginModulateRender()
	{
		(CStateManager.Instance()).SetRenderState(D3DRS_TEXTUREFACTOR, m_AddColor);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLORARG1, D3DTA_TEXTURE);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLORARG2, D3DTA_DIFFUSE);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLOROP, D3DTOP_MODULATE);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_ALPHAARG1, D3DTA_TEXTURE);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_ALPHAARG2, D3DTA_DIFFUSE);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_ALPHAOP, D3DTOP_MODULATE);
    
		(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_COLORARG1, D3DTA_CURRENT);
		(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_COLORARG2, D3DTA_TFACTOR);
		(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_COLOROP, D3DTOP_MODULATE);
		(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_ALPHAOP, D3DTOP_DISABLE);
    
		(CStateManager.Instance()).SaveRenderState(D3DRS_ALPHABLENDENABLE, false);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void EndModulateRender()
	{
		(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_COLOROP, D3DTOP_DISABLE);
		(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_ALPHAOP, D3DTOP_DISABLE);
		(CStateManager.Instance()).RestoreRenderState(D3DRS_ALPHABLENDENABLE);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetModulateRenderMode()
	{
		m_iRenderMode = RENDER_MODE_MODULATE;
		if (m_kBlendAlpha.m_isBlending)
		{
			m_kBlendAlpha.m_iOldRenderMode = m_iRenderMode;
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void RenderCollisionData()
	{
	//# Laniatus Games Studio Inc. |: This static local variable declaration (not allowed in C#) has been moved just prior to the method:
	//	static CScreen s_Screen;
    
		(CStateManager.Instance()).SetRenderState(D3DRS_LIGHTING, false);
		(CStateManager.Instance()).SaveRenderState(D3DRS_CULLMODE, D3DCULL_NONE);
		if (m_pAttributeInstance)
		{
			for (uint col = 0; col < GetCollisionInstanceCount(); ++col)
			{
				CBaseCollisionInstance pInstance = GetCollisionInstanceData(col);
				pInstance.Render();
			}
		}
    
		(CStateManager.Instance()).SetRenderState(D3DRS_ZENABLE, false);
		RenderCollisionData_s_Screen.SetColorOperation();
		RenderCollisionData_s_Screen.SetDiffuseColor(1.0f, 0.0f, 0.0f);
		TCollisionPointInstanceList.iterator itor = new TCollisionPointInstanceList.iterator();
    
		RenderCollisionData_s_Screen.SetDiffuseColor(1.0f, (isShow())?1.0f:0.0f, 0.0f);
		_D3DVECTOR center = new _D3DVECTOR();
		float r;
		GetBoundingSphere(center,r);
		RenderCollisionData_s_Screen.RenderCircle3d(center.x,center.y,center.z,r);
    
		RenderCollisionData_s_Screen.SetDiffuseColor(0.0f, 0.0f, 1.0f);
		itor = m_DefendingPointInstanceList.begin();
		for (; itor != m_DefendingPointInstanceList.end(); ++itor)
		{
	//# Laniatus Games Studio Inc. | TODO TASK: C# does not have an equivalent to references to variables:
	//Original Metin2 CPlus Line: const TCollisionPointInstance & c_rInstance = *itor;
			TCollisionPointInstance c_rInstance = *itor;
			for (uint LaniatusDefVariables = 0; LaniatusDefVariables < c_rInstance.SphereInstanceVector.size(); ++i)
			{
				CDynamicSphereInstance c_rSphereInstance = c_rInstance.SphereInstanceVector[LaniatusDefVariables];
				RenderCollisionData_s_Screen.RenderCircle3d(c_rSphereInstance.v3Position.x, c_rSphereInstance.v3Position.y, c_rSphereInstance.v3Position.z, c_rSphereInstance.fRadius);
			}
		}
    
		RenderCollisionData_s_Screen.SetDiffuseColor(0.0f, 1.0f, 0.0f);
		itor = m_BodyPointInstanceList.begin();
		for (; itor != m_BodyPointInstanceList.end(); ++itor)
		{
	//# Laniatus Games Studio Inc. | TODO TASK: C# does not have an equivalent to references to variables:
	//Original Metin2 CPlus Line: const TCollisionPointInstance & c_rInstance = *itor;
			TCollisionPointInstance c_rInstance = *itor;
			for (uint LaniatusDefVariables = 0; LaniatusDefVariables < c_rInstance.SphereInstanceVector.size(); ++i)
			{
				CDynamicSphereInstance c_rSphereInstance = c_rInstance.SphereInstanceVector[LaniatusDefVariables];
				RenderCollisionData_s_Screen.RenderCircle3d(c_rSphereInstance.v3Position.x, c_rSphereInstance.v3Position.y, c_rSphereInstance.v3Position.z, c_rSphereInstance.fRadius);
			}
		}
    
		RenderCollisionData_s_Screen.SetDiffuseColor(1.0f, 0.0f, 0.0f);
		{
			List<CDynamicSphereInstance>.Enumerator itor = m_kSplashArea.SphereInstanceVector.begin();
			while (itor.MoveNext())
			{
				CDynamicSphereInstance c_rInstance = itor.Current;
				RenderCollisionData_s_Screen.RenderCircle3d(c_rInstance.v3Position.x, c_rInstance.v3Position.y, c_rInstance.v3Position.z, c_rInstance.fRadius);
			}
		}
    
		(CStateManager.Instance()).SetRenderState(D3DRS_ZENABLE, true);
		(CStateManager.Instance()).RestoreRenderState(D3DRS_CULLMODE);
		(CStateManager.Instance()).SetRenderState(D3DRS_LIGHTING, true);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void RenderToShadowMap()
	{
		if (RENDER_MODE_BLEND == m_iRenderMode)
		{
		if (GetAlphaValue() < 0.5f)
		{
			return;
		}
		}
    
		CGraphicThingInstance.RenderToShadowMap();
    
		if (m_pkHorse)
		{
			m_pkHorse.RenderToShadowMap();
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetXYRotation(float fRotX, float fRotY)
	{
		m_rotX = fRotX;
		m_rotY = fRotY;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetRotation(float fRot)
	{
		if (m_pkHorse)
		{
			m_pkHorse.SetRotation(fRot);
		}
    
		m_fcurRotation = fRot;
		m_rotBegin = m_fcurRotation;
		m_rotEnd = m_fcurRotation;
    
		m_rotBlendTime = 0.0f;
		m_rotBeginTime = 0.0f;
		m_rotEndTime = 0.0f;
    
		m_bNeedUpdateCollision = true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void BlendRotation(float fRot, float fBlendTime)
	{
		if (m_pkHorse)
		{
			m_pkHorse.BlendRotation(fRot, fBlendTime);
		}
    
		if (m_fcurRotation == fRot)
		{
			return;
		}
    
		m_rotBegin = fmod(m_fcurRotation, 360.0f);
		m_rotEnd = fRot;
    
		m_rotBlendTime = fBlendTime;
		m_rotBeginTime = GetLocalTime();
		m_rotEndTime = m_rotBeginTime + m_rotBlendTime;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetAdvancingRotation(float fRot)
	{
		if (m_pkHorse)
		{
			m_pkHorse.SetAdvancingRotation(fRot);
		}
    
		m_fAdvancingRotation = fRot;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void RotationProcess()
	{
		if (m_pkHorse)
		{
			m_pkHorse.RotationProcess();
		}
    
		if (GetLocalTime() < m_rotEndTime)
		{
			m_fcurRotation = GetInterpolatedRotation(m_rotBegin, m_rotEnd, (GetLocalTime() - m_rotBeginTime) / m_rotBlendTime);
			SetAdvancingRotation(m_fcurRotation);
		}
		else
		{
			m_fcurRotation = m_rotEnd;
		}
    
		if (0.0f != m_rotX || 0.0f != m_rotY)
		{
			CGraphicObjectInstance.SetRotation(m_rotX, m_rotY, m_fcurRotation);
		}
		else
		{
			CGraphicObjectInstance.SetRotation(m_fcurRotation);
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void LookAtFromXY(float x, float y, CActorInstance pDestInstance)
	{
		float rot = GetDegreeFromPosition2(pDestInstance.m_x, pDestInstance.m_y, x, y);
    
		LookAt(rot);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void LookAt(float fDirRot)
	{
		BlendRotation(fDirRot, 0.3f);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void LookAt(float fx, float fy)
	{
		float rot = GetDegreeFromPosition2(m_x, m_y, fx, fy);
    
		LookAt(rot);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void LookAt(CActorInstance pInstance)
	{
		TPixelPosition PixelPosition = new TPixelPosition();
		pInstance.GetPixelPosition(PixelPosition);
		LookAt(PixelPosition.x, PixelPosition.y);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void LookWith(CActorInstance pInstance)
	{
		BlendRotation(pInstance.m_rotEnd, 0.3f);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public float GetRotation()
	{
		return m_fcurRotation;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public float GetTargetRotation()
	{
		return m_rotEnd;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public float GetRotatingTime()
	{
		return m_rotEndTime;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public float GetAdvancingRotation()
	{
		return m_fAdvancingRotation;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __Push(int x, int y)
	{
		if (IsResistFallen())
		{
			return;
		}
    
		_D3DVECTOR c_rv3Src = GetPosition();
		_D3DVECTOR c_v3Dst = D3DXVECTOR3(x, -y, c_rv3Src.z);
		_D3DVECTOR c_v3Delta = c_v3Dst - c_rv3Src;
    
		const int LoopValue = 100;
		_D3DVECTOR inc = c_v3Delta / LoopValue;
    
		_D3DVECTOR v3Movement = new _D3DVECTOR(0.0f, 0.0f, 0.0f);
    
		IPhysicsWorld pWorld = IPhysicsWorld.GetPhysicsWorld();
    
		if (pWorld == null)
		{
			return;
		}
    
		for (int LaniatusDefVariables = 0; LaniatusDefVariables < LoopValue; ++i)
		{
			if (pWorld.isPhysicalCollision(c_rv3Src + v3Movement))
			{
				ResetBlendingPosition();
				return;
			}
			v3Movement += inc;
		}
    
		SetBlendingPosition(c_v3Dst);
    
		if (!IsUsingSkill())
		{
			int len = Math.Sqrt(c_v3Delta.x * c_v3Delta.x + c_v3Delta.y * c_v3Delta.y);
			if (len > 150.0f)
			{
				InterceptOnceMotion(CRaceMotionData.NAME_DAMAGE_FLYING);
				PushOnceMotion(CRaceMotionData.NAME_STAND_UP);
			}
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void TEMP_Push(int x, int y)
	{
		__Push(x, y);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool __IsSyncing()
	{
		if (IsDead())
		{
			return true;
		}
    
		if (IsStun())
		{
			return true;
		}
    
		if (IsPushing())
		{
			return true;
		}
    
		return false;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool IsPushing()
	{
		return m_PhysicsObject.isBlending();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void TraceProcess()
	{
		if (!m_WeaponTraceVector.empty())
		{
			List<CWeaponTrace>.Enumerator it;
			for (it = m_WeaponTraceVector.begin(); it.MoveNext();)
			{
				CWeaponTrace pWeaponTrace = it.Current;
				pWeaponTrace.SetPosition(m_x, m_y, m_z);
				pWeaponTrace.SetRotation(m_fcurRotation);
				pWeaponTrace.Update(__GetReachScale());
			}
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void RenderTrace()
	{
		for_each(m_WeaponTraceVector.begin(), m_WeaponTraceVector.end(), std::mem_fn(CWeaponTrace.Render));
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __DestroyWeaponTrace()
	{
		std::for_each(m_WeaponTraceVector.begin(), m_WeaponTraceVector.end(), CWeaponTrace.Delete);
		m_WeaponTraceVector.clear();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __ShowWeaponTrace()
	{
		for_each(m_WeaponTraceVector.begin(), m_WeaponTraceVector.end(), std::mem_fn(CWeaponTrace.TurnOn));
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __HideWeaponTrace()
	{
		for_each(m_WeaponTraceVector.begin(), m_WeaponTraceVector.end(), std::mem_fn(CWeaponTrace.TurnOff));
	}
}