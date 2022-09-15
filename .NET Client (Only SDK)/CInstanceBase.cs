public class CInstanceBase
{
//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool IsFlyTargetObject()
	{
		return m_GraphicThingInstance.IsFlyTargetObject();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public float GetFlyTargetDistance()
	{
		return m_GraphicThingInstance.GetFlyTargetDistance();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void ClearFlyTargetInstance()
	{
		m_GraphicThingInstance.ClearFlyTarget();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetFlyTargetInstance(CInstanceBase rkInstDst)
	{
		m_GraphicThingInstance.SetFlyTarget(rkInstDst.GetGraphicThingInstancePtr());
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void AddFlyTargetPosition(in TPixelPosition c_rkPPosDst)
	{
		m_GraphicThingInstance.AddFlyTarget(c_rkPPosDst);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void AddFlyTargetInstance(CInstanceBase rkInstDst)
	{
		m_GraphicThingInstance.AddFlyTarget(rkInstDst.GetGraphicThingInstancePtr());
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public float NEW_GetDistanceFromDestInstance(CInstanceBase rkInstDst)
	{
		TPixelPosition kPPosDst = new TPixelPosition();
		rkInstDst.NEW_GetPixelPosition(kPPosDst);
    
		return NEW_GetDistanceFromDestPixelPosition(kPPosDst);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public float NEW_GetDistanceFromDestPixelPosition(in TPixelPosition c_rkPPosDst)
	{
		TPixelPosition kPPosCur = new TPixelPosition();
		NEW_GetPixelPosition(kPPosCur);
    
		TPixelPosition kPPosDir = new TPixelPosition();
	//# Laniatus Games Studio Inc. | TODO TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'CopyFrom' method should be created:
	//Original Metin2 CPlus Line: kPPosDir=c_rkPPosDst-kPPosCur;
		kPPosDir.CopyFrom(c_rkPPosDst - kPPosCur);
    
		return NEW_GetDistanceFromDirPixelPosition(kPPosDir);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public float NEW_GetDistanceFromDirPixelPosition(in TPixelPosition c_rkPPosDir)
	{
		return sqrtf(c_rkPPosDir.x * c_rkPPosDir.x + c_rkPPosDir.y * c_rkPPosDir.y);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public float NEW_GetRotation()
	{
		float fCurRot = GetRotation();
		return NEW_UnsignedDegreeToSignedDegree(fCurRot);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public float NEW_GetRotationFromDirPixelPosition(in TPixelPosition c_rkPPosDir)
	{
		return NEW_GetSignedDegreeFromDirPixelPosition(c_rkPPosDir);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public float NEW_GetRotationFromDestPixelPosition(in TPixelPosition c_rkPPosDst)
	{
		TPixelPosition kPPosCur = new TPixelPosition();
		NEW_GetPixelPosition(kPPosCur);
    
		TPixelPosition kPPosDir = new TPixelPosition();
	//# Laniatus Games Studio Inc. | TODO TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'CopyFrom' method should be created:
	//Original Metin2 CPlus Line: kPPosDir=c_rkPPosDst-kPPosCur;
		kPPosDir.CopyFrom(c_rkPPosDst - kPPosCur);
    
		return NEW_GetRotationFromDirPixelPosition(kPPosDir);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public float NEW_GetRotationFromDestInstance(CInstanceBase rkInstDst)
	{
		TPixelPosition kPPosDst = new TPixelPosition();
		rkInstDst.NEW_GetPixelPosition(kPPosDst);
    
		return NEW_GetRotationFromDestPixelPosition(kPPosDst);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void NEW_GetRandomPositionInFanRange(CInstanceBase rkInstTarget, TPixelPosition pkPPosDst)
	{
		float fDstDirRot = NEW_GetRotationFromDestInstance(rkInstTarget);
    
		float fRot = frandom(fDstDirRot - 10.0f, fDstDirRot + 10.0f);
    
		_D3DMATRIX kMatRot = new _D3DMATRIX();
		D3DXMatrixRotationZ(kMatRot, ((-fRot) * (((float) 3.141592654f) / 180.0f)));
    
		_D3DVECTOR v3Src = new _D3DVECTOR(0.0f, 8000.0f, 0.0f);
		_D3DVECTOR v3Pos = new _D3DVECTOR();
		D3DXVec3TransformCoord(v3Pos, v3Src, kMatRot);
    
		TPixelPosition c_rkPPosCur = NEW_GetCurPixelPositionRef();
    
		pkPPosDst.x = c_rkPPosCur.x + v3Pos.x;
		pkPPosDst.y = c_rkPPosCur.y + v3Pos.y;
		pkPPosDst.z = __GetBackgroundHeight(c_rkPPosCur.x, c_rkPPosCur.y);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool NEW_GetFrontInstance(CInstanceBase[] ppoutTargetInstance, float fDistance)
	{
		const float HALF_FAN_ROT_MIN = 10.0f;
		const float HALF_FAN_ROT_MAX = 50.0f;
		const float HALF_FAN_ROT_MIN_DISTANCE = 1000.0f;
		float RPM = (HALF_FAN_ROT_MAX - HALF_FAN_ROT_MIN) / HALF_FAN_ROT_MIN_DISTANCE;
    
		float fDstRot = NEW_GetRotation();
    
		std::multimap<float, CInstanceBase> kMap_pkInstNear = new std::multimap<float, CInstanceBase>();
		{
			CPythonCharacterManager rkChrMgr = CPythonCharacterManager.Instance();
			CPythonCharacterManager.CharacterIterator LaniatusDefVariables = new CPythonCharacterManager.CharacterIterator();
			for (i = rkChrMgr.CharacterInstanceBegin(); LaniatusDefVariables != rkChrMgr.CharacterInstanceEnd(); ++i)
			{
				CInstanceBase pkInstEach = *i;
				if (pkInstEach == this)
				{
					continue;
				}
    
				if (!IsAttackableInstance(pkInstEach))
				{
					continue;
				}
    
				if (NEW_GetDistanceFromDestInstance(pkInstEach) > fDistance)
				{
					continue;
				}
    
				float fEachInstDistance = Math.Min(NEW_GetDistanceFromDestInstance(pkInstEach), HALF_FAN_ROT_MIN_DISTANCE);
				float fEachInstDirRot = NEW_GetRotationFromDestInstance(pkInstEach);
    
				float fHalfFanRot = (HALF_FAN_ROT_MAX - HALF_FAN_ROT_MIN) - RPM * fEachInstDistance + HALF_FAN_ROT_MIN;
    
				float fMinDstDirRot = fDstRot - fHalfFanRot;
				float fMaxDstDirRot = fDstRot + fHalfFanRot;
    
				if (fEachInstDirRot >= fMinDstDirRot && fEachInstDirRot <= fMaxDstDirRot)
				{
					kMap_pkInstNear.insert(std::multimap<float, CInstanceBase>.value_type(fEachInstDistance, pkInstEach));
				}
			}
		}
    
		if (kMap_pkInstNear.empty())
		{
			return false;
		}
    
		ppoutTargetInstance[0] = kMap_pkInstNear.begin().second;
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool NEW_GetInstanceVectorInFanRange(float fSkillDistance, CInstanceBase rkInstTarget, List<CInstanceBase> pkVct_pkInst)
	{
		const float HALF_FAN_ROT_MIN = 20.0f;
		const float HALF_FAN_ROT_MAX = 40.0f;
		const float HALF_FAN_ROT_MIN_DISTANCE = 1000.0f;
		float RPM = (HALF_FAN_ROT_MAX - HALF_FAN_ROT_MIN) / HALF_FAN_ROT_MIN_DISTANCE;
    
		float fDstDirRot = NEW_GetRotationFromDestInstance(rkInstTarget);
    
		std::multimap<float, CInstanceBase> kMap_pkInstNear = new std::multimap<float, CInstanceBase>();
		{
			CPythonCharacterManager rkChrMgr = CPythonCharacterManager.Instance();
			CPythonCharacterManager.CharacterIterator LaniatusDefVariables = new CPythonCharacterManager.CharacterIterator();
			for (i = rkChrMgr.CharacterInstanceBegin(); LaniatusDefVariables != rkChrMgr.CharacterInstanceEnd(); ++i)
			{
				CInstanceBase pkInstEach = *i;
				if (pkInstEach == this)
				{
					continue;
				}
    
				if (!IsAttackableInstance(pkInstEach))
				{
					continue;
				}
    
				if (m_GraphicThingInstance.IsClickableDistanceDestInstance(pkInstEach.m_GraphicThingInstance, fSkillDistance))
				{
					float fEachInstDistance = Math.Min(NEW_GetDistanceFromDestInstance(pkInstEach), HALF_FAN_ROT_MIN_DISTANCE);
					float fEachInstDirRot = NEW_GetRotationFromDestInstance(pkInstEach);
    
					float fHalfFanRot = (HALF_FAN_ROT_MAX - HALF_FAN_ROT_MIN) - RPM * fEachInstDistance + HALF_FAN_ROT_MIN;
    
					float fMinDstDirRot = fDstDirRot - fHalfFanRot;
					float fMaxDstDirRot = fDstDirRot + fHalfFanRot;
    
					if (fEachInstDirRot >= fMinDstDirRot && fEachInstDirRot <= fMaxDstDirRot)
					{
						kMap_pkInstNear.insert(std::multimap<float, CInstanceBase>.value_type(fEachInstDistance, pkInstEach));
					}
				}
			}
		}
    
		{
			std::multimap<float, CInstanceBase>.iterator LaniatusDefVariables = kMap_pkInstNear.begin();
			for (i = kMap_pkInstNear.begin(); LaniatusDefVariables != kMap_pkInstNear.end(); ++i)
			{
				pkVct_pkInst.Add(i.second);
			}
		}
    
		if (pkVct_pkInst.Count == 0)
		{
			return false;
		}
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool NEW_GetInstanceVectorInCircleRange(float fSkillDistance, List<CInstanceBase> pkVct_pkInst)
	{
		std::multimap<float, CInstanceBase> kMap_pkInstNear = new std::multimap<float, CInstanceBase>();
    
		{
			CPythonCharacterManager rkChrMgr = CPythonCharacterManager.Instance();
			CPythonCharacterManager.CharacterIterator LaniatusDefVariables = new CPythonCharacterManager.CharacterIterator();
			for (i = rkChrMgr.CharacterInstanceBegin(); LaniatusDefVariables != rkChrMgr.CharacterInstanceEnd(); ++i)
			{
				CInstanceBase pkInstEach = *i;
    
				if (pkInstEach == this)
				{
					continue;
				}
    
				if (!IsAttackableInstance(pkInstEach))
				{
					continue;
				}
    
				if (m_GraphicThingInstance.IsClickableDistanceDestInstance(pkInstEach.m_GraphicThingInstance, fSkillDistance))
				{
					float fEachInstDistance = NEW_GetDistanceFromDestInstance(pkInstEach);
					kMap_pkInstNear.insert(Tuple.Create(fEachInstDistance, pkInstEach));
				}
			}
		}
    
		{
			std::multimap<float, CInstanceBase>.iterator LaniatusDefVariables = kMap_pkInstNear.begin();
			for (i = kMap_pkInstNear.begin(); LaniatusDefVariables != kMap_pkInstNear.end(); ++i)
			{
				pkVct_pkInst.Add(i.second);
			}
		}
    
		if (pkVct_pkInst.Count == 0)
		{
			return false;
		}
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool NEW_IsClickableDistanceDestPixelPosition(in TPixelPosition c_rkPPosDst)
	{
		float fDistance = NEW_GetDistanceFromDestPixelPosition(c_rkPPosDst);
    
		if (fDistance > 150.0f)
		{
			return false;
		}
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool NEW_IsClickableDistanceDestInstance(CInstanceBase rkInstDst)
	{
		float fDistance = 150.0f;
    
		if (IsBowMode())
		{
			fDistance = __GetBowRange();
		}
    
		if (rkInstDst.IsNPC())
		{
			fDistance = 500.0f;
		}
    
		if (rkInstDst.IsResource())
		{
			fDistance = 100.0f;
		}
    
		return m_GraphicThingInstance.IsClickableDistanceDestInstance(rkInstDst.m_GraphicThingInstance, fDistance);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool NEW_UseSkill(uint uSkill, uint uMot, uint uMotLoopCount, bool isMovingSkill)
	{
		if (IsDead())
		{
			return false;
		}
    
		if (IsStun())
		{
			return false;
		}
    
		if (IsKnockDown())
		{
			return false;
		}
    
		if (isMovingSkill)
		{
			if (!IsWalking())
			{
				StartWalking();
			}
    
			m_isGoing = true;
		}
		else
		{
			if (IsWalking())
			{
				EndWalking();
			}
    
			m_isGoing = false;
		}
    
		float fCurRot = m_GraphicThingInstance.GetTargetRotation();
		SetAdvancingRotation(fCurRot);
    
		m_GraphicThingInstance.InterceptOnceMotion(CRaceMotionData.NAME_SKILL + uMot, 0.1f, uSkill, 1.0f);
    
		m_GraphicThingInstance.__OnUseSkill(uMot, uMotLoopCount, isMovingSkill);
    
		if (uMotLoopCount > 0)
		{
			m_GraphicThingInstance.SetMotionLoopCount(uMotLoopCount);
		}
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void NEW_Attack()
	{
		float fDirRot = GetRotation();
		NEW_Attack(fDirRot);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void NEW_Attack(float fDirRot)
	{
		if (IsDead())
		{
			return;
		}
    
		if (IsStun())
		{
			return;
		}
    
		if (IsKnockDown())
		{
			return;
		}
    
		if (IsUsingSkill())
		{
			return;
		}
    
		if (IsWalking())
		{
			EndWalking();
		}
    
		m_isGoing = false;
    
		if (IsPoly())
		{
			InputNormalAttack(fDirRot);
		}
		else
		{
			if (m_kHorse.IsMounting())
			{
				InputComboAttack(fDirRot);
			}
			else
			{
				InputComboAttack(fDirRot);
			}
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void NEW_AttackToDestPixelPositionDirection(in TPixelPosition c_rkPPosDst)
	{
		float fDirRot = NEW_GetRotationFromDestPixelPosition(c_rkPPosDst);
    
		NEW_Attack(fDirRot);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool NEW_AttackToDestInstanceDirection(CInstanceBase rkInstDst, IFlyEventHandler pkFlyHandler)
	{
		return NEW_AttackToDestInstanceDirection(rkInstDst);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool NEW_AttackToDestInstanceDirection(CInstanceBase rkInstDst)
	{
		TPixelPosition kPPosDst = new TPixelPosition();
		rkInstDst.NEW_GetPixelPosition(kPPosDst);
		NEW_AttackToDestPixelPositionDirection(kPPosDst);
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void AttackProcess()
	{
		if (!m_GraphicThingInstance.CanCheckAttacking())
		{
			return;
		}
    
		CInstanceBase pkInstLast = null;
		CPythonCharacterManager rkChrMgr = CPythonCharacterManager.Instance();
		CPythonCharacterManager.CharacterIterator LaniatusDefVariables = rkChrMgr.CharacterInstanceBegin();
		while (rkChrMgr.CharacterInstanceEnd() != i)
		{
			CInstanceBase pkInstEach = *i;
			++i;
    
			if (!IsAttackableInstance(pkInstEach))
			{
				continue;
			}
    
			if (pkInstEach != this)
			{
				if (CheckAttacking(pkInstEach))
				{
					pkInstLast = pkInstEach;
				}
			}
		}
    
		if (pkInstLast != null)
		{
			m_dwLastDmgActorVID = pkInstLast.GetVirtualID();
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void InputNormalAttack(float fAtkDirRot)
	{
		m_GraphicThingInstance.InputNormalAttackCommand(fAtkDirRot);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void InputComboAttack(float fAtkDirRot)
	{
		m_GraphicThingInstance.InputComboAttackCommand(fAtkDirRot);
		__ComboProcess();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void RunNormalAttack(float fAtkDirRot)
	{
		EndGoing();
		m_GraphicThingInstance.NormalAttack(fAtkDirRot);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void RunComboAttack(float fAtkDirRot, uint wMotionIndex)
	{
		EndGoing();
		m_GraphicThingInstance.ComboAttack(wMotionIndex, fAtkDirRot);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool CheckAdvancing()
	{
		if (!__IsMainInstance() && !IsAttacking())
		{
			if (IsPC() && IsWalking())
			{
				CPythonCharacterManager rkChrMgr = CPythonCharacterManager.Instance();
				for (CPythonCharacterManager.CharacterIterator LaniatusDefVariables = rkChrMgr.CharacterInstanceBegin(); LaniatusDefVariables != rkChrMgr.CharacterInstanceEnd();++i)
				{
					CInstanceBase pkInstEach = *i;
					if (pkInstEach == this)
					{
						continue;
					}
					if (!pkInstEach.IsDoor())
					{
						continue;
					}
    
					if (m_GraphicThingInstance.TestActorCollision(pkInstEach.GetGraphicThingInstanceRef()))
					{
						BlockMovement();
						return true;
					}
				}
			}
			return false;
		}
    
		if (m_GraphicThingInstance.CanSkipCollision())
		{
			return false;
		}
    
    
		bool bUsingSkill = m_GraphicThingInstance.IsUsingSkill();
    
		m_dwAdvActorVID = 0;
		uint uCollisionCount = 0;
    
		CPythonCharacterManager rkChrMgr = CPythonCharacterManager.Instance();
		for (CPythonCharacterManager.CharacterIterator LaniatusDefVariables = rkChrMgr.CharacterInstanceBegin(); LaniatusDefVariables != rkChrMgr.CharacterInstanceEnd();++i)
		{
			CInstanceBase pkInstEach = *i;
			if (pkInstEach == this)
			{
				continue;
			}
    
			CActorInstance rkActorSelf = m_GraphicThingInstance;
			CActorInstance rkActorEach = pkInstEach.GetGraphicThingInstanceRef();
    
			if (bUsingSkill && !rkActorEach.IsDoor())
			{
				continue;
			}
    
			if (rkActorSelf.TestActorCollision(rkActorEach))
			{
				uCollisionCount++;
				if (uCollisionCount == 2)
				{
					rkActorSelf.BlockMovement();
					return true;
				}
				rkActorSelf.AdjustDynamicCollisionMovement(rkActorEach);
    
				if (rkActorSelf.TestActorCollision(rkActorEach))
				{
					rkActorSelf.BlockMovement();
					return true;
				}
				else
				{
					NEW_MoveToDestPixelPositionDirection(NEW_GetDstPixelPositionRef());
				}
			}
		}
    
		CPythonBackground rkBG = CPythonBackground.Instance();
		_D3DVECTOR rv3Position = m_GraphicThingInstance.GetPosition();
		_D3DVECTOR rv3MoveDirection = m_GraphicThingInstance.GetMovementVectorRef();
    
		int iStep = D3DXVec3Length(rv3MoveDirection) / 10.0f;
		_D3DVECTOR v3CheckStep = rv3MoveDirection / (float)iStep;
		_D3DVECTOR v3CheckPosition = new _D3DVECTOR(rv3Position);
		for (int j = 0; j < iStep; ++j)
		{
			v3CheckPosition += v3CheckStep;
    
			if (rkBG.isAttrOn(v3CheckPosition.x, -v3CheckPosition.y, CTerrainImpl.ATTRIBUTE_BLOCK))
			{
				BlockMovement();
			}
		}
    
		_D3DVECTOR v3NextPosition = rv3Position + rv3MoveDirection;
		if (rkBG.isAttrOn(v3NextPosition.x, -v3NextPosition.y, CTerrainImpl.ATTRIBUTE_BLOCK))
		{
			BlockMovement();
			return true;
		}
    
		return false;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool CheckAttacking(CInstanceBase rkInstVictim)
	{
		if (IsInSafe())
		{
			return false;
		}
    
		if (rkInstVictim.IsInSafe())
		{
			return false;
		}
    
		if (!m_GraphicThingInstance.AttackingProcess(rkInstVictim.m_GraphicThingInstance))
		{
			return false;
		}
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool isNormalAttacking()
	{
		return m_GraphicThingInstance.isNormalAttacking();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool isComboAttacking()
	{
		return m_GraphicThingInstance.isComboAttacking();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool IsUsingSkill()
	{
		return m_GraphicThingInstance.IsUsingSkill();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool IsUsingMovingSkill()
	{
		return m_GraphicThingInstance.IsUsingMovingSkill();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool CanCancelSkill()
	{
		return m_GraphicThingInstance.CanCancelSkill();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool CanAttackHorseLevel()
	{
		if (!IsMountingHorse())
		{
			return false;
		}
    
		return m_kHorse.CanAttack();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool IsAffect(uint uAffect)
	{
		return m_kAffectFlagContainer.IsSet(uAffect);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public MOTION_KEY GetNormalAttackIndex()
	{
		return m_GraphicThingInstance.GetNormalAttackIndex();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public uint GetComboIndex()
	{
		return m_GraphicThingInstance.GetComboIndex();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public float GetAttackingElapsedTime()
	{
		return m_GraphicThingInstance.GetAttackingElapsedTime();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void ProcessHitting(uint dwMotionKey, CInstanceBase pVictimInstance)
	{
		Debug.Assert(!"-_-" && "CInstanceBase::ProcessHitting");
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void ProcessHitting(uint dwMotionKey, byte byEventIndex, CInstanceBase pVictimInstance)
	{
		Debug.Assert(!"-_-" && "CInstanceBase::ProcessHitting");
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void GetBlendingPosition(TPixelPosition pPixelPosition)
	{
		m_GraphicThingInstance.GetBlendingPosition(pPixelPosition);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetBlendingPosition(in TPixelPosition c_rPixelPosition)
	{
		m_GraphicThingInstance.SetBlendingPosition(c_rPixelPosition);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void Revive()
	{
		m_isGoing = false;
		m_GraphicThingInstance.Revive();
    
		__AttachHorseSaddle();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void Stun()
	{
		NEW_Stop();
		m_GraphicThingInstance.Stun();
    
		__AttachEffect(EFFECT_STUN);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void Die()
	{
		__DetachHorseSaddle();
    
		if (IsAffect(AFFECT_SPAWN))
		{
			__AttachEffect(EFFECT_SPAWN_DISAPPEAR);
		}
    
		__ClearAffects();
    
		OnUnselected();
		OnUntargeted();
    
		m_GraphicThingInstance.Die();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void Hide()
	{
		m_GraphicThingInstance.SetAlphaValue(0.0f);
		m_GraphicThingInstance.BlendAlphaValue(0.0f, 0.1f);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void Show()
	{
		m_GraphicThingInstance.SetAlphaValue(1.0f);
		m_GraphicThingInstance.BlendAlphaValue(1.0f, 0.1f);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetEmpireNameMode(bool isEnable)
	{
		g_isEmpireNameMode = isEnable;
    
		if (isEnable)
		{
			g_akD3DXClrName[NAMECOLOR_MOB] = g_akD3DXClrName[NAMECOLOR_EMPIRE_MOB];
			g_akD3DXClrName[NAMECOLOR_NPC] = g_akD3DXClrName[NAMECOLOR_EMPIRE_NPC];
			g_akD3DXClrName[NAMECOLOR_PC] = g_akD3DXClrName[NAMECOLOR_NORMAL_PC];
    
			for (uint uEmpire = 1; uEmpire < EMPIRE_NUM; ++uEmpire)
			{
				g_akD3DXClrName[NAMECOLOR_PC + uEmpire] = g_akD3DXClrName[NAMECOLOR_EMPIRE_PC + uEmpire];
			}
    
		}
		else
		{
			g_akD3DXClrName[NAMECOLOR_MOB] = g_akD3DXClrName[NAMECOLOR_NORMAL_MOB];
			g_akD3DXClrName[NAMECOLOR_NPC] = g_akD3DXClrName[NAMECOLOR_NORMAL_NPC];
    
			for (uint uEmpire = 0; uEmpire < EMPIRE_NUM; ++uEmpire)
			{
				g_akD3DXClrName[NAMECOLOR_PC + uEmpire] = g_akD3DXClrName[NAMECOLOR_NORMAL_PC];
			}
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public D3DXCOLOR GetIndexedNameColor(uint eNameColor)
	{
		if (eNameColor >= NAMECOLOR_NUM)
		{
	//# Laniatus Games Studio Inc. |: This static local variable declaration (not allowed in C#) has been moved just prior to the method:
	//		static D3DXCOLOR s_kD3DXClrNameDefault(0xffffffff);
			return GetIndexedNameColor_s_kD3DXClrNameDefault;
		}
    
		return g_akD3DXClrName[eNameColor];
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void AddDamageEffect(uint damage, byte flag, bool bSelf, bool bTarget)
	{
		if (CPythonSystem.Instance().IsShowDamage())
		{
			SEffectDamage sDamage = new SEffectDamage();
			sDamage.bSelf = bSelf;
			sDamage.bTarget = bTarget;
			sDamage.damage = damage;
			sDamage.flag = flag;
			m_DamageQueue.push_back(sDamage);
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void ProcessDamage()
	{
		if (m_DamageQueue.empty())
		{
			return;
		}
    
		SEffectDamage sDamage = m_DamageQueue.front();
    
		m_DamageQueue.pop_front();
    
		uint damage = sDamage.damage;
		byte flag = sDamage.flag;
		bool bSelf = sDamage.bSelf;
		bool bTarget = sDamage.bTarget;
    
		CCamera pCamera = CCameraManager.Instance().GetCurrentCamera();
		float cameraAngle = GetDegreeFromPosition2(pCamera.GetTarget().x,pCamera.GetTarget().y,pCamera.GetEye().x,pCamera.GetEye().y);
    
		uint FONT_WIDTH = 30;
    
		CEffectManager rkEftMgr = CEffectManager.Instance();
    
		_D3DVECTOR v3Pos = m_GraphicThingInstance.GetPosition();
		v3Pos.z += (float)m_GraphicThingInstance.GetHeight();
    
		_D3DVECTOR v3Rot = D3DXVECTOR3(0.0f, 0.0f, cameraAngle);
    
		if ((flag & DAMAGE_DODGE) != 0 || (flag & DAMAGE_BLOCK) != 0)
		{
			if (bSelf)
			{
				rkEftMgr.CreateEffect(ms_adwCRCAffectEffect[EFFECT_DAMAGE_MISS],v3Pos,v3Rot);
			}
			else
			{
				rkEftMgr.CreateEffect(ms_adwCRCAffectEffect[EFFECT_DAMAGE_TARGETMISS],v3Pos,v3Rot);
			}
			return;
		}
		else if (flag & DAMAGE_CRITICAL)
		{
			rkEftMgr.CreateEffect(ms_adwCRCAffectEffect[EFFECT_DAMAGE_CRITICAL],v3Pos,v3Rot);
		}
		else if (flag & DAMAGE_PENETRATE)
		{
			rkEftMgr.CreateEffect(ms_adwCRCAffectEffect[EFFECT_DAMAGE_PENETRATE], v3Pos, v3Rot);
		}
    
		string strDamageType = "";
		uint rdwCRCEft = 0;
    
		{
			if (bSelf)
			{
				strDamageType = "damage_";
				if (m_bDamageEffectType == 0)
				{
					rdwCRCEft = EFFECT_DAMAGE_SELFDAMAGE;
				}
				else
				{
					rdwCRCEft = EFFECT_DAMAGE_SELFDAMAGE2;
				}
				m_bDamageEffectType = !m_bDamageEffectType;
			}
			else if (bTarget == false)
			{
				strDamageType = "nontarget_";
				rdwCRCEft = EFFECT_DAMAGE_NOT_TARGET;
				return;
			}
			else
			{
				strDamageType = "target_";
				rdwCRCEft = EFFECT_DAMAGE_TARGET;
			}
		}
    
		uint index = 0;
		uint num = 0;
		List<string> textures = new List<string>();
		while (damage > 0)
		{
			if (index > 7)
			{
				TraceError("ProcessDamage???ѷ??? ???ɼ?");
				break;
			}
			num = damage % 10;
			damage /= 10;
			string numBuf = new string(new char[MAX_PATH]);
			sprintf(numBuf,"%d.dds",num);
			textures.Add("t:/laniaworkstate/effect/affect/damagevalue/" + strDamageType + numBuf);
    
			rkEftMgr.SetEffectTextures(ms_adwCRCAffectEffect[rdwCRCEft],textures);
    
			_D3DMATRIX matrix = new _D3DMATRIX();
			_D3DMATRIX matTrans = new _D3DMATRIX();
			D3DXMatrixIdentity(matrix);
			matrix._41 = v3Pos.x;
			matrix._42 = v3Pos.y;
			matrix._43 = v3Pos.z;
			D3DXMatrixTranslation(matrix, v3Pos.x, v3Pos.y, v3Pos.z);
			D3DXMatrixMultiply(matrix, pCamera.GetInverseViewMatrix(), matrix);
			D3DXMatrixTranslation(matTrans, FONT_WIDTH * index, 0, 0);
			matTrans._41 = -matTrans._41;
	//# Laniatus Games Studio Inc. | TODO TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'CopyFrom' method should be created:
	//Original Metin2 CPlus Line: matrix = matTrans *matrix;
			matrix.CopyFrom(matTrans * matrix);
			D3DXMatrixMultiply(matrix, pCamera.GetViewMatrix(), matrix);
    
			rkEftMgr.CreateEffect(ms_adwCRCAffectEffect[rdwCRCEft],D3DXVECTOR3(matrix._41,matrix._42,matrix._43),v3Rot);
    
			textures.Clear();
    
			index++;
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void AttachSpecialEffect(uint effect)
	{
		__AttachEffect(effect);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void LevelUp()
	{
		__AttachEffect(EFFECT_LEVELUP);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SkillUp()
	{
		__AttachEffect(EFFECT_SKILLUP);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void CreateSpecialEffect(uint iEffectIndex)
	{
		_D3DMATRIX c_rmatGlobal = m_GraphicThingInstance.GetTransform();
    
		uint dwEffectIndex = CEffectManager.Instance().GetEmptyIndex();
		uint dwEffectCRC = ms_adwCRCAffectEffect[iEffectIndex];
		CEffectManager.Instance().CreateEffectInstance(dwEffectIndex, dwEffectCRC);
		CEffectManager.Instance().SelectEffectInstance(dwEffectIndex);
		CEffectManager.Instance().SetEffectInstanceGlobalMatrix(c_rmatGlobal);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __EffectContainer_Destroy()
	{
		SortedDictionary<uint, uint> rkDctEftID = __EffectContainer_GetDict();
    
		SortedDictionary<uint, uint>.Enumerator i;
		for (i = rkDctEftID.GetEnumerator(); i.MoveNext();)
		{
			__DetachEffect(i.Current.Value);
		}
    
		rkDctEftID.Clear();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __EffectContainer_Initialize()
	{
		SortedDictionary<uint, uint> rkDctEftID = __EffectContainer_GetDict();
		rkDctEftID.Clear();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public CInstanceBase.SEffectContainer.Dict __EffectContainer_GetDict()
	{
		return m_kEffectContainer.m_kDct_dwEftID;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public uint __EffectContainer_AttachEffect(uint dwEftKey)
	{
		SortedDictionary<uint, uint> rkDctEftID = __EffectContainer_GetDict();
		SortedDictionary<uint, uint>.Enumerator f = rkDctEftID.find(dwEftKey);
		if (rkDctEftID.end() != f)
		{
			return 0;
		}
    
		uint dwEftID = __AttachEffect(dwEftKey);
		rkDctEftID.insert(SortedDictionary<uint, uint>.value_type(dwEftKey, dwEftID));
		return dwEftID;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __EffectContainer_DetachEffect(uint dwEftKey)
	{
		SortedDictionary<uint, uint> rkDctEftID = __EffectContainer_GetDict();
		SortedDictionary<uint, uint>.Enumerator f = rkDctEftID.find(dwEftKey);
		if (rkDctEftID.end() == f)
		{
			return;
		}
    
	//# Laniatus Games Studio Inc. | TODO TASK: Iterators are only converted within the context of 'while' and 'for' loops:
		__DetachEffect(f.second);
    
		rkDctEftID.Remove(f);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __AttachEmpireEffect(uint eEmpire)
	{
		if (!__IsExistMainInstance())
		{
			return;
		}
    
		CInstanceBase pkInstMain = __GetMainInstancePtr();
    
		if (IsWarp())
		{
			return;
		}
		if (IsObject())
		{
			return;
		}
		if (IsFlag())
		{
			return;
		}
		if (IsResource())
		{
			return;
		}
		if (IsNPC())
		{
			return;
		}
		if (IsMount())
		{
			return;
		}
		if (IsPet())
		{
			return;
		}
    
		if (pkInstMain.IsGameMaster())
		{
		}
		else
		{
			if (pkInstMain.IsSameEmpire(this))
			{
				return;
			}
    
			if (IsAffect(AFFECT_EUNHYEONG))
			{
				return;
			}
		}
    
		if (IsGameMaster())
		{
			return;
		}
    
		__EffectContainer_AttachEffect(EFFECT_EMPIRE + eEmpire);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __AttachSelectEffect()
	{
		__EffectContainer_AttachEffect(EFFECT_SELECT);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __DetachSelectEffect()
	{
		__EffectContainer_DetachEffect(EFFECT_SELECT);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __AttachTargetEffect()
	{
		__EffectContainer_AttachEffect(EFFECT_TARGET);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __DetachTargetEffect()
	{
		__EffectContainer_DetachEffect(EFFECT_TARGET);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __StoneSmoke_Inialize()
	{
		m_kStoneSmoke.m_dwEftID = 0;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __StoneSmoke_Destroy()
	{
		if (!m_kStoneSmoke.m_dwEftID)
		{
			return;
		}
    
		__DetachEffect(m_kStoneSmoke.m_dwEftID);
		m_kStoneSmoke.m_dwEftID = 0;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __StoneSmoke_Create(uint eSmoke)
	{
		m_kStoneSmoke.m_dwEftID = m_GraphicThingInstance.AttachSmokeEffect(eSmoke);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetAlpha(float fAlpha)
	{
		__SetBlendRenderingMode();
		__SetAlphaValue(fAlpha);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool UpdateDeleting()
	{
		Update();
		Transform();
    
		IAbstractApplication rApp = IAbstractApplication.GetSingleton();
    
		float fAlpha = __GetAlphaValue() - (rApp.GetGlobalElapsedTime() * 1.5f);
		__SetAlphaValue(fAlpha);
    
		if (fAlpha < 0.0f)
		{
			return false;
		}
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void DeleteBlendOut()
	{
		__SetBlendRenderingMode();
		__SetAlphaValue(1.0f);
		DetachTextTail();
    
		IAbstractPlayer rkPlayer = IAbstractPlayer.GetSingleton();
		rkPlayer.NotifyDeletingCharacterInstance(GetVirtualID());
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void ClearPVPKeySystem()
	{
		g_kSet_dwPVPReadyKey.clear();
		g_kSet_dwPVPKey.clear();
		g_kSet_dwGVGKey.clear();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void InsertPVPKey(uint dwVIDSrc, uint dwVIDDst)
	{
		uint dwPVPKey = __GetPVPKey(dwVIDSrc, dwVIDDst);
    
		g_kSet_dwPVPKey.insert(dwPVPKey);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void InsertPVPReadyKey(uint dwVIDSrc, uint dwVIDDst)
	{
		uint dwPVPReadyKey = __GetPVPKey(dwVIDSrc, dwVIDDst);
    
		g_kSet_dwPVPKey.insert(dwPVPReadyKey);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void RemovePVPKey(uint dwVIDSrc, uint dwVIDDst)
	{
		uint dwPVPKey = __GetPVPKey(dwVIDSrc, dwVIDDst);
    
		g_kSet_dwPVPKey.erase(dwPVPKey);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void InsertGVGKey(uint dwSrcGuildVID, uint dwDstGuildVID)
	{
		uint dwGVGKey = __GetPVPKey(dwSrcGuildVID, dwDstGuildVID);
		g_kSet_dwGVGKey.insert(dwGVGKey);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void RemoveGVGKey(uint dwSrcGuildVID, uint dwDstGuildVID)
	{
		uint dwGVGKey = __GetPVPKey(dwSrcGuildVID, dwDstGuildVID);
		g_kSet_dwGVGKey.erase(dwGVGKey);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public uint __GetPVPKey(uint dwVIDSrc, uint dwVIDDst)
	{
		if (dwVIDSrc > dwVIDDst)
		{
			std::swap(dwVIDSrc, dwVIDDst);
		}
    
		uint[] awSrc = new uint[2];
		awSrc[0] = dwVIDSrc;
		awSrc[1] = dwVIDDst;
    
	//# Laniatus Games Studio Inc. | TODO TASK: Pointer arithmetic is detected on this variable, so pointers on this variable are left unchanged:
		byte * s = (byte) awSrc;
	//# Laniatus Games Studio Inc. | TODO TASK: C# does not have an equivalent to pointers to value types:
	//Original Metin2 CPlus Line: const byte * end = s + sizeof(awSrc);
		byte end = s + sizeof(uint);
		uint h = 0;
    
		while (s < end)
		{
			h *= 16777619;
			h ^= (byte) * (byte)(s++);
		}
    
		return h;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool __FindPVPKey(uint dwVIDSrc, uint dwVIDDst)
	{
		uint dwPVPKey = __GetPVPKey(dwVIDSrc, dwVIDDst);
    
		if (g_kSet_dwPVPKey.end() == g_kSet_dwPVPKey.find(dwPVPKey))
		{
			return false;
		}
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool __FindPVPReadyKey(uint dwVIDSrc, uint dwVIDDst)
	{
		uint dwPVPKey = __GetPVPKey(dwVIDSrc, dwVIDDst);
    
		if (g_kSet_dwPVPReadyKey.end() == g_kSet_dwPVPReadyKey.find(dwPVPKey))
		{
			return false;
		}
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool __FindGVGKey(uint dwSrcGuildID, uint dwDstGuildID)
	{
		uint dwGVGKey = __GetPVPKey(dwSrcGuildID, dwDstGuildID);
    
		if (g_kSet_dwGVGKey.end() == g_kSet_dwGVGKey.find(dwGVGKey))
		{
			return false;
		}
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool IsPVPInstance(CInstanceBase rkInstSel)
	{
		uint dwVIDSrc = GetVirtualID();
		uint dwVIDDst = rkInstSel.GetVirtualID();
    
		uint dwGuildIDSrc = GetGuildID();
		uint dwGuildIDDst = rkInstSel.GetGuildID();
    
		return __FindPVPKey(dwVIDSrc, dwVIDDst) || __FindGVGKey(dwGuildIDSrc, dwGuildIDDst);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public D3DXCOLOR GetNameColor()
	{
		return GetIndexedNameColor(GetNameColorIndex());
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public uint GetNameColorIndex()
	{
		if (IsPC())
		{
			if (m_isKiller)
			{
				return NAMECOLOR_PK;
			}
    
			if (__IsExistMainInstance() && !__IsMainInstance())
			{
				CInstanceBase pkInstMain = __GetMainInstancePtr();
				if (pkInstMain == null)
				{
					TraceError("CInstanceBase::GetNameColorIndex - MainInstance is NULL");
					return NAMECOLOR_PC;
				}
				uint dwVIDMain = pkInstMain.GetVirtualID();
				uint dwVIDSelf = GetVirtualID();
    
				if (pkInstMain.IsSameEmpire(this))
				{
					if (__FindPVPKey(dwVIDMain, dwVIDSelf))
					{
						return NAMECOLOR_PVP;
					}
    
					uint dwGuildIDMain = pkInstMain.GetGuildID();
					uint dwGuildIDSelf = GetGuildID();
					if (__FindGVGKey(dwGuildIDMain, dwGuildIDSelf))
					{
						return NAMECOLOR_PVP;
					}
				}
				else
				{
					return NAMECOLOR_PVP;
				}
			}
    
			IAbstractPlayer rPlayer = IAbstractPlayer.GetSingleton();
			if (rPlayer.IsPartyMemberByVID(GetVirtualID()))
			{
				return NAMECOLOR_PARTY;
			}
    
			return NAMECOLOR_PC + GetEmpireID();
    
		}
		else if (IsNPC())
		{
			return NAMECOLOR_NPC;
		}
		else if (IsMount())
		{
			return NAMECOLOR_MOUNT;
		}
		else if (IsPet())
		{
			return NAMECOLOR_PET;
		}
		else if (IsEnemy())
		{
			return NAMECOLOR_MOB;
		}
		else if (IsPoly())
		{
			return NAMECOLOR_MOB;
		}
		else if (IsStone())
		{
			return NAMECOLOR_METIN;
		}
    
    
		return D3DXCOLOR(0xffffffff);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public D3DXCOLOR GetTitleColor()
	{
		uint uGrade = GetAlignmentGrade();
		if (uGrade >= TITLE_NUM)
		{
	//# Laniatus Games Studio Inc. |: This static local variable declaration (not allowed in C#) has been moved just prior to the method:
	//		static D3DXCOLOR s_kD3DXClrTitleDefault(0xffffffff);
			return GetTitleColor_s_kD3DXClrTitleDefault;
		}
    
		return g_akD3DXClrTitle[uGrade];
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void AttachTextTail()
	{
		if (m_isTextTail)
		{
			TraceError("CInstanceBase::AttachTextTail - VID [%d] ALREADY EXIST", GetVirtualID());
			return;
		}
    
		m_isTextTail = true;
    
		uint dwVID = GetVirtualID();
    
		float fTextTailHeight = IsMountingHorse() ? 110.0f : 10.0f;
    
	//# Laniatus Games Studio Inc. |: This static local variable declaration (not allowed in C#) has been moved just prior to the method:
	//	static D3DXCOLOR s_kD3DXClrTextTail=D3DXCOLOR(1.0f, 1.0f, 1.0f, 1.0f);
		CPythonTextTail.Instance().RegisterCharacterTextTail(m_dwGuildID, dwVID, AttachTextTail_s_kD3DXClrTextTail, fTextTailHeight);
    
		if (m_dwLevel)
		{
			UpdateTextTailLevel(m_dwLevel);
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void DetachTextTail()
	{
		if (!m_isTextTail)
		{
			return;
		}
    
		m_isTextTail = false;
		CPythonTextTail.Instance().DeleteCharacterTextTail(GetVirtualID());
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void UpdateTextTailLevel(uint level)
	{
	//# Laniatus Games Studio Inc. |: This static local variable declaration (not allowed in C#) has been moved just prior to the method:
	//	static D3DXCOLOR s_kLevelColor = D3DXCOLOR(152.0f / 255.0f, 255.0f / 255.0f, 51.0f / 255.0f, 1.0f);
		string szText = new string(new char[256]);
		sprintf(szText, "Lv. %d", level);
		m_dwLevel = level;
		CPythonTextTail.Instance().AttachLevel(GetVirtualID(), szText, UpdateTextTailLevel_s_kLevelColor);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void RefreshTextTail()
	{
		CPythonTextTail.Instance().SetCharacterTextTailColor(GetVirtualID(), GetNameColor());
    
		int iAlignmentGrade = GetAlignmentGrade();
		if (TITLE_NONE == iAlignmentGrade)
		{
			CPythonTextTail.Instance().DetachTitle(GetVirtualID());
		}
		else
		{
			SortedDictionary<int, string>.Enumerator itor = g_TitleNameMap.find(iAlignmentGrade);
			if (g_TitleNameMap.end() != itor)
			{
	//# Laniatus Games Studio Inc. | TODO TASK: Iterators are only converted within the context of 'while' and 'for' loops:
				string c_rstrTitleName = itor.second;
				CPythonTextTail.Instance().AttachTitle(GetVirtualID(), c_rstrTitleName, GetTitleColor());
			}
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void RefreshTextTailTitle()
	{
		RefreshTextTail();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __ClearAffectFlagContainer()
	{
		m_kAffectFlagContainer.Clear();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __ClearAffects()
	{
		if (IsStone())
		{
			__StoneSmoke_Destroy();
		}
		else
		{
			for (int iAffect = 0; iAffect < AFFECT_NUM; ++iAffect)
			{
				__DetachEffect(m_adwCRCAffectEffect[iAffect]);
				m_adwCRCAffectEffect[iAffect] = 0;
			}
    
			__ClearAffectFlagContainer();
		}
    
		m_GraphicThingInstance.__OnClearAffects();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __SetNormalAffectFlagContainer(in CAffectFlagContainer c_rkAffectFlagContainer)
	{
		for (int LaniatusDefVariables = 0; LaniatusDefVariables < CAffectFlagContainer.BIT_SIZE; ++i)
		{
			bool isOldSet = m_kAffectFlagContainer.IsSet(i);
			bool isNewSet = c_rkAffectFlagContainer.IsSet(i);
    
			if (isOldSet != isNewSet)
			{
				__SetAffect(i, isNewSet);
    
				if (isNewSet)
				{
					m_GraphicThingInstance.__OnSetAffect(i);
				}
				else
				{
					m_GraphicThingInstance.__OnResetAffect(i);
				}
			}
		}
    
		m_kAffectFlagContainer.CopyInstance(c_rkAffectFlagContainer);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __SetStoneSmokeFlagContainer(in CAffectFlagContainer c_rkAffectFlagContainer)
	{
		m_kAffectFlagContainer.CopyInstance(c_rkAffectFlagContainer);
    
		uint eSmoke;
		if (m_kAffectFlagContainer.IsSet(STONE_SMOKE8))
		{
			eSmoke = 3;
		}
		else if (m_kAffectFlagContainer.IsSet(STONE_SMOKE5) | m_kAffectFlagContainer.IsSet(STONE_SMOKE6) | m_kAffectFlagContainer.IsSet(STONE_SMOKE7))
		{
			eSmoke = 2;
		}
		else if (m_kAffectFlagContainer.IsSet(STONE_SMOKE2) | m_kAffectFlagContainer.IsSet(STONE_SMOKE3) | m_kAffectFlagContainer.IsSet(STONE_SMOKE4))
		{
			eSmoke = 1;
		}
		else
		{
			eSmoke = 0;
		}
    
		__StoneSmoke_Destroy();
		__StoneSmoke_Create(eSmoke);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetAffectFlagContainer(in CAffectFlagContainer c_rkAffectFlagContainer)
	{
		if (IsBuilding())
		{
			return;
		}
		else if (IsStone())
		{
			__SetStoneSmokeFlagContainer(c_rkAffectFlagContainer);
		}
		else
		{
			__SetNormalAffectFlagContainer(c_rkAffectFlagContainer);
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SCRIPT_SetAffect(uint eAffect, bool isVisible)
	{
		__SetAffect(eAffect, isVisible);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __SetReviveInvisibilityAffect(bool isVisible)
	{
		if (isVisible)
		{
			if (IsWearingDress())
			{
				return;
			}
    
			m_GraphicThingInstance.BlendAlphaValue(0.5f, 1.0f);
		}
		else
		{
			m_GraphicThingInstance.BlendAlphaValue(1.0f, 1.0f);
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __Assassin_SetEunhyeongAffect(bool isVisible)
	{
		if (isVisible)
		{
			if (IsWearingDress())
			{
				return;
			}
    
			if (__IsMainInstance() || __MainCanSeeHiddenThing())
			{
				m_GraphicThingInstance.BlendAlphaValue(0.5f, 1.0f);
			}
			else
			{
				m_GraphicThingInstance.BlendAlphaValue(0.0f, 1.0f);
				m_GraphicThingInstance.HideAllAttachingEffect();
			}
		}
		else
		{
			m_GraphicThingInstance.BlendAlphaValue(1.0f, 1.0f);
			m_GraphicThingInstance.ShowAllAttachingEffect();
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __Shaman_SetParalysis(bool isParalysis)
	{
		m_GraphicThingInstance.SetParalysis(isParalysis);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __Warrior_SetGeomgyeongAffect(bool isVisible)
	{
		if (isVisible)
		{
			if (IsWearingDress())
			{
				return;
			}
    
			if (m_kWarrior.m_dwGeomgyeongEffect)
			{
				__DetachEffect(m_kWarrior.m_dwGeomgyeongEffect);
			}
    
			m_GraphicThingInstance.SetReachScale(1.5f);
			if (m_GraphicThingInstance.IsTwoHandMode())
			{
				m_kWarrior.m_dwGeomgyeongEffect = __AttachEffect(EFFECT_WEAPON + WEAPON_TWOHAND);
			}
			else
			{
				m_kWarrior.m_dwGeomgyeongEffect = __AttachEffect(EFFECT_WEAPON + WEAPON_ONEHAND);
			}
		}
		else
		{
			m_GraphicThingInstance.SetReachScale(1.0f);
    
			__DetachEffect(m_kWarrior.m_dwGeomgyeongEffect);
			m_kWarrior.m_dwGeomgyeongEffect = 0;
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __SetAffect(uint eAffect, bool isVisible)
	{
		switch (eAffect)
		{
			case AFFECT_YMIR:
				if (IsAffect(AFFECT_INVISIBILITY))
				{
					return;
				}
				break;
			case AFFECT_CHEONGEUN:
				m_GraphicThingInstance.SetResistFallen(isVisible);
				break;
			case AFFECT_GEOMGYEONG:
				__Warrior_SetGeomgyeongAffect(isVisible);
				return;
				break;
			case AFFECT_REVIVE_INVISIBILITY:
				__Assassin_SetEunhyeongAffect(isVisible);
				break;
			case AFFECT_EUNHYEONG:
				__Assassin_SetEunhyeongAffect(isVisible);
				break;
			case AFFECT_GYEONGGONG:
			case AFFECT_KWAESOK:
				if (isVisible)
				{
					if (!IsWalking())
					{
						return;
					}
				}
				break;
			case AFFECT_INVISIBILITY:
				if (isVisible)
				{
					m_GraphicThingInstance.ClearAttachingEffect();
					__EffectContainer_Destroy();
					DetachTextTail();
				}
				else
				{
					m_GraphicThingInstance.BlendAlphaValue(1.0f, 1.0f);
					AttachTextTail();
					RefreshTextTail();
				}
				return;
				break;
			case AFFECT_STUN:
				m_GraphicThingInstance.SetSleep(isVisible);
				break;
		}
    
		if (eAffect >= AFFECT_NUM)
		{
			TraceError("CInstanceBase[VID:%d]::SetAffect(eAffect:%d<AFFECT_NUM:%d, isVisible=%d)", GetVirtualID(), eAffect, isVisible);
			return;
		}
    
		if (isVisible)
		{
			if (!m_adwCRCAffectEffect[eAffect])
			{
				m_adwCRCAffectEffect[eAffect] = __AttachEffect(EFFECT_AFFECT + eAffect);
			}
		}
		else
		{
			if (m_adwCRCAffectEffect[eAffect])
			{
				__DetachEffect(m_adwCRCAffectEffect[eAffect]);
				m_adwCRCAffectEffect[eAffect] = 0;
			}
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool IsPossibleEmoticon()
	{
		CEffectManager rkEftMgr = CEffectManager.Instance();
		for (uint eEmoticon = 0; eEmoticon < EMOTICON_NUM; eEmoticon++)
		{
			uint effectID = ms_adwCRCAffectEffect[EFFECT_EMOTICON + eEmoticon];
			if (effectID != 0 && rkEftMgr.IsAliveEffect(effectID))
			{
				return false;
			}
		}
    
		if (ELTimer_GetMSec() - m_dwEmoticonTime < 1000)
		{
			TraceError("ELTimer_GetMSec() - m_dwEmoticonTime");
			return false;
		}
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetFishEmoticon()
	{
		SetEmoticon(EMOTICON_FISH);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetEmoticon(uint eEmoticon)
	{
		if (eEmoticon >= EMOTICON_NUM)
		{
			TraceError("CInstanceBase[VID:%d]::SetEmoticon(eEmoticon:%d<EMOTICON_NUM:%d, isVisible=%d)", GetVirtualID(), eEmoticon);
			return;
		}
		if (IsPossibleEmoticon())
		{
			_D3DVECTOR v3Pos = m_GraphicThingInstance.GetPosition();
			v3Pos.z += (float)m_GraphicThingInstance.GetHeight();
    
			CCamera pCamera = CCameraManager.Instance().GetCurrentCamera();
    
			_D3DVECTOR v3Dir = (pCamera.GetEye() - v3Pos) * 9 / 10;
			v3Pos = pCamera.GetEye() - v3Dir;
    
			v3Pos = D3DXVECTOR3(0,0,0);
			v3Pos.z += (float)m_GraphicThingInstance.GetHeight();
    
			m_GraphicThingInstance.AttachEffectByID(0, null, ms_adwCRCAffectEffect[EFFECT_EMOTICON + eEmoticon], v3Pos);
			m_dwEmoticonTime = ELTimer_GetMSec();
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetDustGap(float fDustGap)
	{
		ms_fDustGap = fDustGap;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetHorseDustGap(float fDustGap)
	{
		ms_fHorseDustGap = fDustGap;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __DetachEffect(uint dwEID)
	{
		m_GraphicThingInstance.DettachEffect(dwEID);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public uint __AttachEffect(uint eEftType)
	{
		if (IsAffect(AFFECT_INVISIBILITY))
		{
			return 0;
		}
    
		if (eEftType >= EFFECT_NUM)
		{
			return 0;
		}
    
		if (ms_astAffectEffectAttachBone[eEftType].empty())
		{
			return m_GraphicThingInstance.AttachEffectByID(0, null, ms_adwCRCAffectEffect[eEftType]);
		}
		else
		{
			string rstrBoneName = ms_astAffectEffectAttachBone[eEftType];
			string c_szBoneName;
    
			if (0 == string.CompareOrdinal(rstrBoneName, "PART_WEAPON"))
			{
				if (m_GraphicThingInstance.GetAttachingBoneName(CRaceData.PART_WEAPON, c_szBoneName))
				{
					return m_GraphicThingInstance.AttachEffectByID(0, c_szBoneName, ms_adwCRCAffectEffect[eEftType]);
				}
			}
			else if (0 == string.CompareOrdinal(rstrBoneName, "PART_WEAPON_LEFT"))
			{
				if (m_GraphicThingInstance.GetAttachingBoneName(CRaceData.PART_WEAPON_LEFT, c_szBoneName))
				{
					return m_GraphicThingInstance.AttachEffectByID(0, c_szBoneName, ms_adwCRCAffectEffect[eEftType]);
				}
			}
			else
			{
				return m_GraphicThingInstance.AttachEffectByID(0, rstrBoneName, ms_adwCRCAffectEffect[eEftType]);
			}
		}
    
		return 0;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __ComboProcess()
	{
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RegisterEffect(uint eEftType, string c_szEftAttachBone, string c_szEftName, bool isCache)
	{
		if (eEftType >= EFFECT_NUM)
		{
			return false;
		}
    
		ms_astAffectEffectAttachBone[eEftType] = c_szEftAttachBone;
    
	//# Laniatus Games Studio Inc. | TODO TASK: C# does not have an equivalent to references to value types:
	//Original Metin2 CPlus Line: uint& rdwCRCEft=ms_adwCRCAffectEffect[eEftType];
		uint rdwCRCEft = ms_adwCRCAffectEffect[eEftType];
		if (!CEffectManager.Instance().RegisterEffect2(c_szEftName, rdwCRCEft, isCache))
		{
			TraceError("CInstanceBase::RegisterEffect(eEftType=%d, c_szEftAttachBone=%s, c_szEftName=%s, isCache=%d) - Error", eEftType, c_szEftAttachBone, c_szEftName, isCache);
			rdwCRCEft = 0;
			return false;
		}
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void RegisterTitleName(int iIndex, string c_szTitleName)
	{
		g_TitleNameMap.insert(Tuple.Create(iIndex, c_szTitleName));
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RegisterNameColor(uint uIndex, uint r, uint g, uint b)
	{
		if (uIndex >= NAMECOLOR_NUM)
		{
			return false;
		}
    
		g_akD3DXClrName[uIndex] = __RGBToD3DXColoru(r, g, b);
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RegisterTitleColor(uint uIndex, uint r, uint g, uint b)
	{
		if (uIndex >= TITLE_NUM)
		{
			return false;
		}
    
		g_akD3DXClrTitle[uIndex] = __RGBToD3DXColoru(r, g, b);
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public CActorInstance.IEventHandler GetEventHandlerRef()
	{
		return m_GraphicThingInstance.__GetEventHandlerRef();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public CActorInstance.IEventHandler GetEventHandlerPtr()
	{
		return m_GraphicThingInstance.__GetEventHandlerPtr();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetEventHandler(CActorInstance.IEventHandler pkEventHandler)
	{
		m_GraphicThingInstance.SetEventHandler(pkEventHandler);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetMotionMode(int iMotionMode)
	{
		m_GraphicThingInstance.SetMotionMode(iMotionMode);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public int GetMotionMode(uint dwMotionIndex)
	{
		return m_GraphicThingInstance.GetMotionMode();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetLoopMotion(ushort wMotion, float fBlendTime, float fSpeedRatio)
	{
		m_GraphicThingInstance.SetLoopMotion(wMotion, fBlendTime, fSpeedRatio);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void PushOnceMotion(ushort wMotion, float fBlendTime, float fSpeedRatio)
	{
		m_GraphicThingInstance.PushOnceMotion(wMotion, fBlendTime, fSpeedRatio);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void PushLoopMotion(ushort wMotion, float fBlendTime, float fSpeedRatio)
	{
		m_GraphicThingInstance.PushLoopMotion(wMotion, fBlendTime, fSpeedRatio);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void ResetLocalTime()
	{
		m_GraphicThingInstance.ResetLocalTime();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetEndStopMotion()
	{
		m_GraphicThingInstance.SetEndStopMotion();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool isLock()
	{
		return m_GraphicThingInstance.isLock();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void StartFishing(float frot)
	{
		BlendRotation(frot);
    
		TPixelPosition c_rkPPosCur = m_GraphicThingInstance.NEW_GetCurPixelPositionRef();
		float fRot = m_GraphicThingInstance.GetTargetRotation();
    
		TPixelPosition kPPosFishing = new TPixelPosition();
		ELPlainCoord_GetRotatedPixelPosition(c_rkPPosCur.x, c_rkPPosCur.y, c_fFishingDistance, fRot, kPPosFishing.x, kPPosFishing.y);
		if (!__Background_GetWaterHeight(kPPosFishing, kPPosFishing.z))
		{
			kPPosFishing.z = c_rkPPosCur.z;
		}
    
		_D3DVECTOR v3Fishing = new _D3DVECTOR();
		PixelPositionToD3DXVECTOR3(kPPosFishing, v3Fishing);
		m_GraphicThingInstance.SetFishingPosition(v3Fishing);
    
		PushOnceMotion(CRaceMotionData.NAME_FISHING_THROW);
		PushLoopMotion(CRaceMotionData.NAME_FISHING_WAIT);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void StopFishing()
	{
		m_GraphicThingInstance.InterceptOnceMotion(CRaceMotionData.NAME_FISHING_STOP);
		PushLoopMotion(CRaceMotionData.NAME_WAIT);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void ReactFishing()
	{
		PushOnceMotion(CRaceMotionData.NAME_FISHING_REACT);
		PushLoopMotion(CRaceMotionData.NAME_FISHING_WAIT);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void CatchSuccess()
	{
		m_GraphicThingInstance.InterceptOnceMotion(CRaceMotionData.NAME_FISHING_CATCH);
		PushLoopMotion(CRaceMotionData.NAME_WAIT);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void CatchFail()
	{
		m_GraphicThingInstance.InterceptOnceMotion(CRaceMotionData.NAME_FISHING_FAIL);
		PushLoopMotion(CRaceMotionData.NAME_WAIT);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool GetFishingRot(ref int pirot)
	{
		TPixelPosition c_rkPPosCur = m_GraphicThingInstance.NEW_GetCurPixelPositionRef();
		float fCharacterRot = m_GraphicThingInstance.GetRotation();
    
		for (float fRot = 0.0f; fRot <= 180.0f; fRot += 10.0f)
		{
			TPixelPosition kPPosFishingRight = new TPixelPosition();
			ELPlainCoord_GetRotatedPixelPosition(c_rkPPosCur.x, c_rkPPosCur.y, c_fFishingDistance, fCharacterRot + fRot, kPPosFishingRight.x, kPPosFishingRight.y);
			if (__Background_IsWaterPixelPosition(kPPosFishingRight))
			{
				pirot = (int)(fCharacterRot + fRot);
				return true;
			}
    
			TPixelPosition kPPosFishingLeft = new TPixelPosition();
			ELPlainCoord_GetRotatedPixelPosition(c_rkPPosCur.x, c_rkPPosCur.y, c_fFishingDistance, fCharacterRot - fRot, kPPosFishingLeft.x, kPPosFishingLeft.y);
			if (__Background_IsWaterPixelPosition(kPPosFishingLeft))
			{
				pirot = (int)(fCharacterRot - fRot);
				return true;
			}
		}
    
		return false;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __EnableChangingTCPState()
	{
		m_bEnableTCPState = true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __DisableChangingTCPState()
	{
		m_bEnableTCPState = false;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void ActDualEmotion(CInstanceBase rkDstInst, ushort wMotionNumber1, ushort wMotionNumber2)
	{
		if (!IsWaiting())
		{
			m_GraphicThingInstance.SetLoopMotion(CRaceMotionData.NAME_WAIT, 0.05f);
		}
		if (!rkDstInst.IsWaiting())
		{
			rkDstInst.m_GraphicThingInstance.SetLoopMotion(CRaceMotionData.NAME_WAIT, 0.05f);
		}
    
		const float c_fEmotionDistance = 100.0f;
		TPixelPosition c_rMainPosition = NEW_GetCurPixelPositionRef();
		TPixelPosition c_rTargetPosition = rkDstInst.NEW_GetCurPixelPositionRef();
		TPixelPosition kDirection = c_rMainPosition - c_rTargetPosition;
		float fDistance = sqrtf((kDirection.x * kDirection.x) + (kDirection.y * kDirection.y));
		TPixelPosition kDstPosition = new TPixelPosition();
		kDstPosition.x = c_rTargetPosition.x + (kDirection.x / fDistance) * c_fEmotionDistance;
		kDstPosition.y = c_rTargetPosition.y + (kDirection.y / fDistance) * c_fEmotionDistance;
    
		uint dwCurTime = ELTimer_GetServerMSec() + 500;
		PushTCPStateExpanded(dwCurTime, kDstPosition, 0.0f, FUNC_EMOTION, MAKELONG(wMotionNumber1, wMotionNumber2), rkDstInst.GetVirtualID());
    
		__DisableChangingTCPState();
		rkDstInst.__DisableChangingTCPState();
    
		if (__IsMainInstance() || rkDstInst.__IsMainInstance())
		{
			IAbstractPlayer rPlayer = IAbstractPlayer.GetSingleton();
			rPlayer.StartEmotionProcess();
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void ActEmotion(uint dwMotionNumber)
	{
		PushOnceMotion(dwMotionNumber);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetAttackSpeed(uint uAtkSpd)
	{
		if (uAtkSpd > 1100)
		{
			uAtkSpd = 0;
		}
    
		m_GraphicThingInstance.SetAttackSpeed(uAtkSpd / 100.0f);
		m_kHorse.SetAttackSpeed(uAtkSpd);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetMoveSpeed(uint uMovSpd)
	{
		if (uMovSpd > 1100)
		{
			uMovSpd = 0;
		}
    
		m_GraphicThingInstance.SetMoveSpeed(uMovSpd / 100.0f);
		m_kHorse.SetMoveSpeed(uMovSpd);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetRotationSpeed(float fRotSpd)
	{
		m_fMaxRotSpd = fRotSpd;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void NEW_Stop()
	{
		if (__IsSyncing())
		{
			return;
		}
    
		if (isLock())
		{
			return;
		}
    
		if (IsUsingSkill())
		{
			return;
		}
    
		if (!IsWaiting())
		{
			EndWalking();
		}
    
		m_GraphicThingInstance.__OnStop();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void NEW_SyncPixelPosition(ref int nPPosX, ref int nPPosY)
	{
		m_GraphicThingInstance.TEMP_Push(nPPosX, nPPosY);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool NEW_CanMoveToDestPixelPosition(in TPixelPosition c_rkPPosDst)
	{
		TPixelPosition kPPosCur = new TPixelPosition();
		NEW_GetPixelPosition(kPPosCur);
    
		if (kPPosCur.x == c_rkPPosDst.x && kPPosCur.y == c_rkPPosDst.y)
		{
			return false;
		}
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public float NEW_GetAdvancingRotationFromDirPixelPosition(in TPixelPosition c_rkPPosDir)
	{
		float fDirRot = CInstanceBase_GetDegreeFromPosition(c_rkPPosDir.x, -c_rkPPosDir.y);
		float fClampDirRot = ClampDegree(fDirRot);
    
		return fClampDirRot;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public float NEW_GetAdvancingRotationFromDestPixelPosition(in TPixelPosition c_rkPPosDst)
	{
		TPixelPosition kPPosCur = new TPixelPosition();
		NEW_GetPixelPosition(kPPosCur);
		return NEW_GetAdvancingRotationFromPixelPosition(kPPosCur, c_rkPPosDst);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public float NEW_GetAdvancingRotationFromPixelPosition(in TPixelPosition c_rkPPosSrc, in TPixelPosition c_rkPPosDst)
	{
		TPixelPosition kPPosDelta = new TPixelPosition();
	//# Laniatus Games Studio Inc. | TODO TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'CopyFrom' method should be created:
	//Original Metin2 CPlus Line: kPPosDelta=c_rkPPosDst-c_rkPPosSrc;
		kPPosDelta.CopyFrom(c_rkPPosDst - c_rkPPosSrc);
		return NEW_GetAdvancingRotationFromDirPixelPosition(kPPosDelta);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void NEW_SetAdvancingRotationFromDirPixelPosition(in TPixelPosition c_rkPPosDir)
	{
		float fClampDirRot = NEW_GetAdvancingRotationFromDirPixelPosition(c_rkPPosDir);
		m_GraphicThingInstance.SetAdvancingRotation(fClampDirRot);
    
		float fCurRot = m_GraphicThingInstance.GetRotation();
		float fAdvRot = m_GraphicThingInstance.GetAdvancingRotation();
    
		m_iRotatingDirection = GetRotatingDirection(fCurRot, fAdvRot);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void NEW_SetAdvancingRotationFromPixelPosition(in TPixelPosition c_rkPPosSrc, in TPixelPosition c_rkPPosDst)
	{
		TPixelPosition kPPosDelta = new TPixelPosition();
	//# Laniatus Games Studio Inc. | TODO TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'CopyFrom' method should be created:
	//Original Metin2 CPlus Line: kPPosDelta=c_rkPPosDst-c_rkPPosSrc;
		kPPosDelta.CopyFrom(c_rkPPosDst - c_rkPPosSrc);
    
		NEW_SetAdvancingRotationFromDirPixelPosition(kPPosDelta);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool NEW_SetAdvancingRotationFromDestPixelPosition(in TPixelPosition c_rkPPosDst)
	{
		if (!NEW_CanMoveToDestPixelPosition(c_rkPPosDst))
		{
			Tracenf("Failed to move next position (%f,%f, %f)", c_rkPPosDst.x, c_rkPPosDst.y, c_rkPPosDst.z);
			return false;
		}
    
		TPixelPosition kPPosSrc = new TPixelPosition();
		NEW_GetPixelPosition(kPPosSrc);
		NEW_SetAdvancingRotationFromPixelPosition(kPPosSrc, c_rkPPosDst);
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetAdvancingRotation(float fRotation)
	{
		float frotDifference = GetDegreeDifference(GetRotation(), fRotation);
    
		if (frotDifference > 45.0f)
		{
			m_fRotSpd = m_fMaxRotSpd;
		}
		else
		{
			m_fRotSpd = m_fMaxRotSpd * 5 / 12;
		}
    
		m_GraphicThingInstance.SetAdvancingRotation(ClampDegree(fRotation));
		m_iRotatingDirection = GetRotatingDirection(m_GraphicThingInstance.GetRotation(), m_GraphicThingInstance.GetAdvancingRotation());
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void StartWalking()
	{
		m_GraphicThingInstance.Move();
    
		if (IsAffect(AFFECT_GYEONGGONG))
		{
			m_adwCRCAffectEffect[AFFECT_GYEONGGONG] = __EffectContainer_AttachEffect(EFFECT_AFFECT_GYEONGGONG);
		}
		else if (IsAffect(AFFECT_KWAESOK))
		{
			m_adwCRCAffectEffect[AFFECT_KWAESOK] = __EffectContainer_AttachEffect(EFFECT_AFFECT_KWAESOK);
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void EndWalking(float fBlendingTime)
	{
		Debug.Assert(!IsWaiting() && "CInstanceBase::EndWalking");
    
		m_isGoing = false;
    
		if (IsWalking() || !IsAttacked())
		{
			m_GraphicThingInstance.Stop(fBlendingTime);
			if (IsAffect(AFFECT_GYEONGGONG))
			{
				__EffectContainer_DetachEffect(EFFECT_AFFECT_GYEONGGONG);
			}
			else if (IsAffect(AFFECT_KWAESOK))
			{
				__EffectContainer_DetachEffect(EFFECT_AFFECT_KWAESOK);
			}
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void EndWalkingWithoutBlending()
	{
		EndWalking(0.0f);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool IsWaiting()
	{
		return m_GraphicThingInstance.IsWaiting();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool IsWalking()
	{
		return m_GraphicThingInstance.IsMoving();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool IsPushing()
	{
		return m_GraphicThingInstance.IsPushing();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool IsAttacked()
	{
		return m_GraphicThingInstance.IsAttacked();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool IsKnockDown()
	{
		if (!m_GraphicThingInstance.IsKnockDown())
		{
			return false;
		}
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool IsAttacking()
	{
		return m_GraphicThingInstance.isAttacking();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool IsActingEmotion()
	{
		return m_GraphicThingInstance.IsActEmotion();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool IsGoing()
	{
		return m_isGoing;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void NEW_MoveToDestInstanceDirection(CInstanceBase rkInstDst)
	{
		TPixelPosition kPPosDst = new TPixelPosition();
		rkInstDst.NEW_GetPixelPosition(kPPosDst);
    
		NEW_MoveToDestPixelPositionDirection(kPPosDst);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool NEW_MoveToDestPixelPositionDirection(in TPixelPosition c_rkPPosDst)
	{
		TPixelPosition kPPosCur = new TPixelPosition();
		NEW_GetPixelPosition(kPPosCur);
		float fDstRot = NEW_GetAdvancingRotationFromPixelPosition(kPPosCur, c_rkPPosDst);
    
		return NEW_Goto(c_rkPPosDst, fDstRot);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool NEW_Goto(in TPixelPosition c_rkPPosDst, float fDstRot)
	{
		if (__IsSyncing())
		{
			return false;
		}
    
		if (m_GraphicThingInstance.IsUsingMovingSkill())
		{
			SetAdvancingRotation(fDstRot);
			return true;
		}
    
		if (isLock())
		{
			return false;
		}
    
		if (!NEW_CanMoveToDestPixelPosition(c_rkPPosDst))
		{
			if (!IsWaiting())
			{
				EndWalking();
			}
    
			return true;
		}
    
		NEW_SetSrcPixelPosition(NEW_GetCurPixelPositionRef());
		NEW_SetDstPixelPosition(c_rkPPosDst);
		NEW_SetDstPixelPositionZ(NEW_GetSrcPixelPositionRef().z);
		m_fDstRot = fDstRot;
		m_isGoing = true;
    
		if (!IsWalking())
		{
			StartWalking();
		}
    
		NEW_SetAdvancingRotationFromPixelPosition(NEW_GetSrcPixelPositionRef(), NEW_GetDstPixelPositionRef());
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void NEW_MoveToDirection(float fDirRot)
	{
		if (__IsSyncing())
		{
			return;
		}
    
		if (m_GraphicThingInstance.IsUsingMovingSkill())
		{
			SetAdvancingRotation(fDirRot);
			return;
		}
    
		if (isLock())
		{
			return;
		}
    
		m_isGoing = false;
    
		SetAdvancingRotation(fDirRot);
    
		if (!IsWalking())
		{
			StartWalking();
		}
    
		TPixelPosition kPPosCur = new TPixelPosition();
		NEW_GetPixelPosition(kPPosCur);
    
		_D3DVECTOR kD3DVt3Cur = new _D3DVECTOR(kPPosCur.x, -kPPosCur.y, kPPosCur.z);
		_D3DVECTOR kD3DVt3Dst = new _D3DVECTOR();
    
		_D3DVECTOR kD3DVt3AdvDir = new _D3DVECTOR(0.0f, -1.0f, 0.0f);
		_D3DMATRIX kD3DMatAdv = new _D3DMATRIX();
		D3DXMatrixRotationZ(kD3DMatAdv, ((fDirRot) * (((float) 3.141592654f) / 180.0f)));
		D3DXVec3TransformCoord(kD3DVt3AdvDir, kD3DVt3AdvDir, kD3DMatAdv);
		D3DXVec3Scale(kD3DVt3AdvDir, kD3DVt3AdvDir, 300.0f);
		D3DXVec3Add(kD3DVt3Dst, kD3DVt3AdvDir, kD3DVt3Cur);
    
		TPixelPosition kPPosDst = new TPixelPosition();
		kPPosDst.x = +kD3DVt3Dst.x;
		kPPosDst.y = -kD3DVt3Dst.y;
		kPPosDst.z = +kD3DVt3Dst.z;
    
		NEW_SetSrcPixelPosition(kPPosCur);
		NEW_SetDstPixelPosition(kPPosDst);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void EndGoing()
	{
		if (!IsWaiting())
		{
			EndWalking();
		}
    
		m_isGoing = false;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetRunMode()
	{
		m_GraphicThingInstance.SetRunMode();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetWalkMode()
	{
		m_GraphicThingInstance.SetWalkMode();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SCRIPT_SetPixelPosition(float fx, float fy)
	{
		float fz = __GetBackgroundHeight(fx, fy);
		NEW_SetPixelPosition(TPixelPosition(fx, fy, fz));
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void NEW_SetPixelPosition(in TPixelPosition c_rPixelPosition)
	{
		m_GraphicThingInstance.SetCurPixelPosition(c_rPixelPosition);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void NEW_GetPixelPosition(TPixelPosition pPixelPosition)
	{
		pPixelPosition = m_GraphicThingInstance.NEW_GetCurPixelPositionRef();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetRotation(float fRotation)
	{
		m_GraphicThingInstance.SetRotation(fRotation);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void BlendRotation(float fRotation, float fBlendTime)
	{
		m_GraphicThingInstance.BlendRotation(fRotation, fBlendTime);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void NEW_LookAtFlyTarget()
	{
		m_GraphicThingInstance.LookAtFlyTarget();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void NEW_LookAtDestPixelPosition(in TPixelPosition c_rkPPosDst)
	{
		m_GraphicThingInstance.LookAt(c_rkPPosDst.x, -c_rkPPosDst.y);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void NEW_LookAtDestInstance(CInstanceBase rkInstDst)
	{
		m_GraphicThingInstance.LookAt(rkInstDst.m_GraphicThingInstance);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public float GetRotation()
	{
		return m_GraphicThingInstance.GetRotation();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public float GetAdvancingRotation()
	{
		return m_GraphicThingInstance.GetAdvancingRotation();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetDirection(int dir)
	{
		float fDegree = GetDegreeFromDirection(dir);
		SetRotation(fDegree);
		SetAdvancingRotation(fDegree);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void BlendDirection(int dir, float blendTime)
	{
		m_GraphicThingInstance.BlendRotation(GetDegreeFromDirection(dir), blendTime);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public float GetDegreeFromDirection(int dir)
	{
		if (dir < 0)
		{
			return 0.0f;
		}
    
		if (dir >= DIR_MAX_NUM)
		{
			return 0.0f;
		}
    
	//# Laniatus Games Studio Inc. |: This static local variable declaration (not allowed in C#) has been moved just prior to the method:
	//	static float s_dirRot[DIR_MAX_NUM]= { +45.0f * 4, +45.0f * 3, +45.0f * 2, +45.0f, +0.0f, 360.0f-45.0f, 360.0f-45.0f * 2, 360.0f-45.0f * 3};
    
		return GetDegreeFromDirection_s_dirRot[dir];
	}
}