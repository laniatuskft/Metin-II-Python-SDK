using System.Collections.Generic;

//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define COMBO_KEY DWORD
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MAKE_COMBO_KEY(motion_mode, combo_type) ( (DWORD(motion_mode) << 16) | (DWORD(combo_type)) )
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define COMBO_KEY_GET_MOTION_MODE(key) ( WORD(DWORD(key) >> 16 & 0xFFFF) )
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define COMBO_KEY_GET_COMBO_TYPE(key) ( WORD(DWORD(key) & 0xFFFF) )
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define POLY_NONE POLY_MAXVALUE
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define POLY_ROOT POLY_MAXVALUE + 1
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define POLY_MUL POLY_MAXVALUE + 2
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define POLY_PLU POLY_MAXVALUE + 3
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define POLY_POW POLY_MAXVALUE + 4
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define POLY_MIN POLY_MAXVALUE + 5
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define POLY_DIV POLY_MAXVALUE + 6
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define POLY_OPEN POLY_MAXVALUE + 7
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define POLY_CLOSE POLY_MAXVALUE + 8
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define POLY_NUM POLY_MAXVALUE + 9
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define POLY_ID POLY_MAXVALUE + 10
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define POLY_EOS POLY_MAXVALUE + 11
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define POLY_COS POLY_MAXVALUE + 12
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define POLY_SIN POLY_MAXVALUE + 13
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define POLY_TAN POLY_MAXVALUE + 14
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define POLY_COSEC POLY_MAXVALUE + 15
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define POLY_CSC POLY_COSEC
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define POLY_SEC POLY_MAXVALUE + 16
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define POLY_COT POLY_MAXVALUE + 17
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define POLY_PI POLY_ID
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define POLY_EXP POLY_ID
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define POLY_LOG POLY_MAXVALUE + 18
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define POLY_LN POLY_MAXVALUE + 19
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define POLY_LOG10 POLY_MAXVALUE + 20
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define POLY_ABS POLY_MAXVALUE + 21
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define POLY_MINF POLY_MAXVALUE + 22
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define POLY_MAXF POLY_MAXVALUE + 23
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define POLY_IRAND POLY_MAXVALUE + 24
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define POLY_FRAND POLY_MAXVALUE + 25
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define POLY_MOD POLY_MAXVALUE + 26
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define POLY_FLOOR POLY_MAXVALUE + 27

//# Laniatus Games Studio Inc. |: C# has no need of forward class declarations:
//class CInstanceBase;

//# Laniatus Games Studio Inc. | TODO TASK: Multiple inheritance is not available in C#:
public class CPythonPlayer : CSingleton<CPythonPlayer>, IAbstractPlayer, System.IDisposable
{

		public const int CATEGORY_NONE = 0;
		public const int CATEGORY_ACTIVE = 1;
		public const int CATEGORY_PASSIVE = 2;
		public const int CATEGORY_MAX_NUM = 3;
		public const int STATUS_INDEX_ST = 1;
		public const int STATUS_INDEX_DX = 2;
		public const int STATUS_INDEX_IQ = 3;
		public const int STATUS_INDEX_HT = 4;

		public const int MBT_LEFT = 0;
		public const int MBT_RIGHT = 1;
		public const int MBT_MIDDLE = 2;
		public const int MBT_NUM = 3;

		public const int MBF_SMART = 0;
		public const int MBF_MOVE = 1;
		public const int MBF_CAMERA = 2;
		public const int MBF_ATTACK = 3;
		public const int MBF_SKILL = 4;
		public const int MBF_AUTO = 5;

		public const int MBS_CLICK = 0;
		public const int MBS_PRESS = 1;

		public enum EMode
		{
			MODE_NONE,
			MODE_CLICK_POSITION,
			MODE_CLICK_ITEM,
			MODE_CLICK_ACTOR,
			MODE_USE_SKILL
		}

		public enum EEffect
		{
			EFFECT_PICK,
			EFFECT_NUM
		}

		public enum EMetinSocketType
		{
			METIN_SOCKET_TYPE_NONE,
			METIN_SOCKET_TYPE_SILVER,
			METIN_SOCKET_TYPE_GOLD
		}

#if ENABLE_LOAD_PLAYERSETTING
		public enum EEmotions
		{
			EMOTION_CLAP = 1,
			EMOTION_CONGRATULATION,
			EMOTION_FORGIVE,
			EMOTION_ANGRY,
			EMOTION_ATTRACTIVE,
			EMOTION_SAD,
			EMOTION_SHY,
			EMOTION_CHEERUP,
			EMOTION_BANTER,
			EMOTION_JOY,
			EMOTION_CHEERS_1,
			EMOTION_CHEERS_2,
			EMOTION_DANCE_1,
			EMOTION_DANCE_2,
			EMOTION_DANCE_3,
			EMOTION_DANCE_4,
			EMOTION_DANCE_5,
			EMOTION_DANCE_6,
			EMOTION_KISS = 51,
			EMOTION_FRENCH_KISS,
			EMOTION_SLAP
		}
#endif

		public class SSkillInstance
		{
			public uint dwIndex;
			public int iType;
			public int iGrade;
			public int iLevel;
			public float fcurEfficientPercentage;
			public float fnextEfficientPercentage;
			public bool isCoolTime;

			public float fCoolTime;
			public float fLastUsedTime;
			public bool bActive;
		}

		public enum EKeyBoard_UD
		{
			KEYBOARD_UD_NONE,
			KEYBOARD_UD_UP,
			KEYBOARD_UD_DOWN
		}

		public enum EKeyBoard_LR
		{
			KEYBOARD_LR_NONE,
			KEYBOARD_LR_LEFT,
			KEYBOARD_LR_RIGHT
		}

		public const int DIR_UP = 0;
		public const int DIR_DOWN = 1;
		public const int DIR_LEFT = 2;
		public const int DIR_RIGHT = 3;

		public class SPlayerStatus
		{
			public TItemData[] aItem = Arrays.InitializeWithDefaultInstances<TItemData>(c_Inventory_Count);
			public TItemData[] aDSItem = Arrays.InitializeWithDefaultInstances<TItemData>(c_DragonSoul_Inventory_Count);
			public TQuickSlot[] aQuickSlot = Arrays.InitializeWithDefaultInstances<TQuickSlot>(QUICKSLOT_MAX_NUM);
			public TSkillInstance[] aSkill = Arrays.InitializeWithDefaultInstances<TSkillInstance>(DefineConstants.SKILL_MAX_NUM);
			public long[] m_alPoint = new long[POINT_MAX_NUM];
			public int lQuickPageIndex;

	public void SetPoint(uint ePoint, long lPoint)
	{
		m_alPoint[ePoint] = lPoint ^ POINT_MAGIC_NUMBER;
	}
	public long GetPoint(uint ePoint)
	{
		return m_alPoint[ePoint] ^ POINT_MAGIC_NUMBER;
	}
		}

		public class SPartyMemberInfo
		{
			public SPartyMemberInfo(uint _dwPID, string c_szName)
			{
				this.dwPID = _dwPID;
				this.strName = c_szName;
				this.dwVID = 0;
				this.byState = 0;
				this.byHPPercentage = 0;
//# Laniatus Games Studio Inc. | TODO TASK: The memory management function 'memset' has no equivalent in C#:
				memset(sAffects, 0, sizeof(short));
			}

			public uint dwVID;
			public uint dwPID;
			public string strName = "";
			public byte byState;
			public byte byHPPercentage;
			public short[] sAffects = new short[PARTY_AFFECT_SLOT_MAX_NUM];
		}

		public enum EPartyRole
		{
			PARTY_ROLE_NORMAL,
			PARTY_ROLE_LEADER,
			PARTY_ROLE_ATTACKER,
			PARTY_ROLE_TANKER,
			PARTY_ROLE_BUFFER,
			PARTY_ROLE_SKILL_MASTER,
			PARTY_ROLE_BERSERKER,
			PARTY_ROLE_DEFENDER,
			PARTY_ROLE_MAX_NUM
		}

		public const int SKILL_NORMAL = 0;
		public const int SKILL_MASTER = 1;
		public const int SKILL_GRAND_MASTER = 2;
		public const int SKILL_PERFECT_MASTER = 3;

		public class SAutoPotionInfo
		{
			public SAutoPotionInfo()
			{
				this.bActivated = false;
				this.totalAmount = 0;
				this.currentAmount = 0;
				this.inventorySlotIndex = 0;
			}

			public bool bActivated;
			public int currentAmount;
			public int totalAmount;
			public int inventorySlotIndex;
		}

		public enum EAutoPotionType
		{
			AUTO_POTION_TYPE_HP = 0,
			AUTO_POTION_TYPE_SP = 1,
			AUTO_POTION_TYPE_NUM
		}

		public const int ABSORB = 0;
		public const int COMBINE = 1;

		public const int ACCE_SLOT_LEFT = 0;
		public const int ACCE_SLOT_RIGHT = 1;
		public const int ACCE_SLOT_RESULT = 2;
		public const int ACCE_SLOT_MAX_NUM = 3;

	public CPythonPlayer()
	{
		SetMovableGroundDistance(40.0f);
    
		m_kMap_dwAffectIndexToSkillIndex.insert(Tuple.Create((int)CInstanceBase.AFFECT_JEONGWI, 3));
		m_kMap_dwAffectIndexToSkillIndex.insert(Tuple.Create((int)CInstanceBase.AFFECT_GEOMGYEONG, 4));
		m_kMap_dwAffectIndexToSkillIndex.insert(Tuple.Create((int)CInstanceBase.AFFECT_CHEONGEUN, 19));
		m_kMap_dwAffectIndexToSkillIndex.insert(Tuple.Create((int)CInstanceBase.AFFECT_GYEONGGONG, 49));
		m_kMap_dwAffectIndexToSkillIndex.insert(Tuple.Create((int)CInstanceBase.AFFECT_EUNHYEONG, 34));
		m_kMap_dwAffectIndexToSkillIndex.insert(Tuple.Create((int)CInstanceBase.AFFECT_GONGPO, 64));
		m_kMap_dwAffectIndexToSkillIndex.insert(Tuple.Create((int)CInstanceBase.AFFECT_JUMAGAP, 65));
		m_kMap_dwAffectIndexToSkillIndex.insert(Tuple.Create((int)CInstanceBase.AFFECT_HOSIN, 94));
		m_kMap_dwAffectIndexToSkillIndex.insert(Tuple.Create((int)CInstanceBase.AFFECT_BOHO, 95));
		m_kMap_dwAffectIndexToSkillIndex.insert(Tuple.Create((int)CInstanceBase.AFFECT_KWAESOK, 110));
		m_kMap_dwAffectIndexToSkillIndex.insert(Tuple.Create((int)CInstanceBase.AFFECT_GICHEON, 96));
		m_kMap_dwAffectIndexToSkillIndex.insert(Tuple.Create((int)CInstanceBase.AFFECT_JEUNGRYEOK, 111));
		m_kMap_dwAffectIndexToSkillIndex.insert(Tuple.Create((int)CInstanceBase.AFFECT_PABEOP, 66));
		m_kMap_dwAffectIndexToSkillIndex.insert(Tuple.Create((int)CInstanceBase.AFFECT_FALLEN_CHEONGEUN, 19));
		m_kMap_dwAffectIndexToSkillIndex.insert(Tuple.Create((int)CInstanceBase.AFFECT_GWIGEOM, 63));
		m_kMap_dwAffectIndexToSkillIndex.insert(Tuple.Create((int)CInstanceBase.AFFECT_MUYEONG, 78));
		m_kMap_dwAffectIndexToSkillIndex.insert(Tuple.Create((int)CInstanceBase.AFFECT_HEUKSIN, 79));
	#if ENABLE_WOLFMAN
		m_kMap_dwAffectIndexToSkillIndex.insert(Tuple.Create((int)CInstanceBase.AFFECT_RED_POSSESSION, 174));
		m_kMap_dwAffectIndexToSkillIndex.insert(Tuple.Create((int)CInstanceBase.AFFECT_BLUE_POSSESSION, 175));
	#endif
    
		m_ppyGameWindow = null;
    
		m_sysIsCoolTime = true;
		m_sysIsLevelLimit = true;
		m_dwPlayTime = 0;
    
		m_aeMBFButton[MBT_LEFT] = CPythonPlayer.MBF_SMART;
		m_aeMBFButton[MBT_RIGHT] = CPythonPlayer.MBF_CAMERA;
		m_aeMBFButton[MBT_MIDDLE] = CPythonPlayer.MBF_CAMERA;
    
	//# Laniatus Games Studio Inc. | TODO TASK: The memory management function 'memset' has no equivalent in C#:
		memset(m_adwEffect, 0, sizeof(m_adwEffect));
    
		m_isDestPosition = false;
		m_ixDestPos = 0;
		m_iyDestPos = 0;
		m_iLastAlarmTime = 0;
    
		Clear();
	}
	public void Dispose()
	{
	}

	public void PickCloseMoney()
	{
		CInstanceBase pkInstMain = NEW_GetMainActorPtr();
		if (pkInstMain == null)
		{
			return;
		}
    
		TPixelPosition kPPosMain = new TPixelPosition();
		pkInstMain.NEW_GetPixelPosition(kPPosMain);
    
		uint dwItemID;
		CPythonItem rkItem = CPythonItem.Instance();
		if (!rkItem.GetCloseMoney(kPPosMain, dwItemID, __GetPickableDistance()))
		{
			return;
		}
    
		SendClickItemPacket(dwItemID);
	}
	public void PickCloseItem()
	{
		CInstanceBase pkInstMain = NEW_GetMainActorPtr();
		if (pkInstMain == null)
		{
			return;
		}
    
		TPixelPosition kPPosMain = new TPixelPosition();
		pkInstMain.NEW_GetPixelPosition(kPPosMain);
    
		uint dwItemID;
		CPythonItem rkItem = CPythonItem.Instance();
		if (!rkItem.GetCloseItem(kPPosMain, dwItemID, __GetPickableDistance()))
		{
			return;
		}
    
		SendClickItemPacket(dwItemID);
	}

	public void SetGameWindow(PyObject ppyObject)
	{
		m_ppyGameWindow = ppyObject;
	}

	public void SetObserverMode(bool isEnable)
	{
		m_isObserverMode = isEnable;
	}
	public bool IsObserverMode()
	{
		return m_isObserverMode;
	}

	public void SetQuickCameraMode(bool isEnable)
	{
		if (isEnable)
		{
		}
		else
		{
			NEW_SetMouseCameraState(MBS_CLICK);
		}
	}

	public void SetAttackKeyState(bool isPress)
	{
		if (isPress)
		{
			CInstanceBase pkInstMain = NEW_GetMainActorPtr();
			if (pkInstMain != null)
			{
			if (pkInstMain.IsFishingMode())
			{
				NEW_Fishing();
				return;
			}
			}
		}
    
		m_isAtkKey = isPress;
	}

	public void NEW_GetMainActorPosition(TPixelPosition pkPPosActor)
	{
		TPixelPosition kPPosMainActor = new TPixelPosition();
    
		IAbstractPlayer rkPlayer = IAbstractPlayer.GetSingleton();
		CInstanceBase pInstance = rkPlayer.NEW_GetMainActorPtr();
		if (pInstance != null)
		{
			pInstance.NEW_GetPixelPosition(pkPPosActor);
		}
		else
		{
			CPythonApplication.Instance().GetCenterPosition(pkPPosActor);
		}
	}

	public bool RegisterEffect(uint dwEID, string c_szFileName, bool isCache)
	{
		if (dwEID >= EFFECT_NUM)
		{
			return false;
		}
    
		CEffectManager rkEftMgr = CEffectManager.Instance();
		rkEftMgr.RegisterEffect2(c_szFileName, m_adwEffect[dwEID], isCache);
		return true;
	}

	public bool NEW_SetMouseState(int eMBT, int eMBS)
	{
		if (eMBT >= MBT_NUM)
		{
			return false;
		}
    
		int eMBF = m_aeMBFButton[eMBT];
		switch (eMBF)
		{
			case MBF_MOVE:
				if (__CanMove())
				{
					NEW_SetMouseMoveState(eMBS);
				}
				break;
			case MBF_SMART:
				if (CPythonApplication.Instance().IsPressed(DIK_LCONTROL) || CPythonApplication.Instance().IsPressed(DIK_RCONTROL))
				{
					NEW_Attack();
				}
				else
				{
					NEW_SetMouseSmartState(eMBS, false);
				}
				break;
			case MBF_CAMERA:
				NEW_SetMouseCameraState(eMBS);
				break;
			case MBF_AUTO:
				NEW_SetMouseSmartState(eMBS, true);
				break;
			case MBF_ATTACK:
				NEW_Attack();
				break;
			case MBF_SKILL:
				if (CPythonApplication.Instance().IsPressed(DIK_LCONTROL))
				{
					NEW_SetMouseCameraState(eMBS);
				}
				else
				{
					if (MBS_PRESS == eMBS)
					{
						 __ChangeTargetToPickedInstance();
						__UseCurrentSkill();
					}
				}
				break;
		}
    
		return true;
	}
	public bool NEW_SetMouseFunc(int eMBT, int eMBF)
	{
		if (eMBT >= MBT_NUM)
		{
			return false;
		}
    
		m_aeMBFButton[eMBT] = eMBF;
    
		return true;
	}
	public int NEW_GetMouseFunc(int eMBT)
	{
		if (eMBT >= MBT_NUM)
		{
			return false ? 1 : 0;
		}
    
		return m_aeMBFButton[eMBT];
	}
	public void NEW_SetMouseMiddleButtonState(int eMBState)
	{
		NEW_SetMouseCameraState(eMBState);
	}

	public void NEW_SetAutoCameraRotationSpeed(float fRotSpd)
	{
		m_fCmrRotSpd = fRotSpd;
	}
	public void NEW_ResetCameraRotation()
	{
		CCamera pkCmrCur = CCameraManager.Instance().GetCurrentCamera();
		CPythonApplication rkApp = CPythonApplication.Instance();
    
		pkCmrCur.EndDrag();
    
		rkApp.SetCursorNum(CPythonApplication.NORMAL);
		if (CPythonApplication.CURSOR_MODE_HARDWARE == rkApp.GetCursorMode())
		{
			rkApp.SetCursorVisible(true);
		}
	}

	public void NEW_SetSingleDirKeyState(int eDirKey, bool isPress)
	{
		switch (eDirKey)
		{
			case DIR_UP:
				m_isUp = isPress;
				break;
			case DIR_DOWN:
				m_isDown = isPress;
				break;
			case DIR_LEFT:
				m_isLeft = isPress;
				break;
			case DIR_RIGHT:
				m_isRight = isPress;
				break;
		}
    
		m_isDirKey = (m_isUp || m_isDown || m_isLeft || m_isRight);
    
		NEW_SetMultiDirKeyState(m_isLeft, m_isRight, m_isUp, m_isDown);
	}
	public void NEW_SetSingleDIKKeyState(int eDIKKey, bool isPress)
	{
		if (NEW_CancelFishing())
		{
			return;
		}
    
		switch (eDIKKey)
		{
			case DIK_UP:
				NEW_SetSingleDirKeyState(DIR_UP, isPress);
				break;
			case DIK_DOWN:
				NEW_SetSingleDirKeyState(DIR_DOWN, isPress);
				break;
			case DIK_LEFT:
				NEW_SetSingleDirKeyState(DIR_LEFT, isPress);
				break;
			case DIK_RIGHT:
				NEW_SetSingleDirKeyState(DIR_RIGHT, isPress);
				break;
		}
	}
	public void NEW_SetMultiDirKeyState(bool isLeft, bool isRight, bool isUp, bool isDown)
	{
		if (!__CanMove())
		{
			return;
		}
    
		bool isAny = (isLeft || isRight || isUp || isDown);
    
		if (isAny)
		{
			float fDirRot = 0.0f;
			NEW_GetMultiKeyDirRotation(isLeft, isRight, isUp, isDown, fDirRot);
    
			if (!NEW_MoveToDirection(fDirRot))
			{
				Tracen("CPythonPlayer::NEW_SetMultiKeyState - NEW_Move -> ERROR");
				return;
			}
		}
		else
		{
			NEW_Stop();
		}
	}

	public void NEW_Attack()
	{
		if (IsOpenPrivateShop())
		{
			return;
		}
    
		if (!__CanAttack())
		{
			return;
		}
    
		CInstanceBase pkInstMain = NEW_GetMainActorPtr();
		if (pkInstMain == null)
		{
			return;
		}
    
		if (pkInstMain.IsBowMode())
		{
    
			CInstanceBase pkInstTarget = __GetAliveTargetInstancePtr();
			if (pkInstTarget == null)
			{
				__ChangeTargetToPickedInstance();
				pkInstTarget = __GetAliveTargetInstancePtr();
			}
    
			if (pkInstTarget != null)
			{
				if (!__CanShot(pkInstMain, pkInstTarget))
				{
					return;
				}
    
				if (!pkInstMain.NEW_IsClickableDistanceDestInstance(pkInstTarget))
				{
					__ReserveClickActor(pkInstTarget.GetVirtualID());
					return;
				}
    
				if (pkInstMain.IsAttackableInstance(pkInstTarget))
				{
					pkInstMain.NEW_LookAtDestInstance(pkInstTarget);
					pkInstMain.NEW_AttackToDestInstanceDirection(pkInstTarget);
				}
			}
			else
			{
				PyCallClassMemberFunc(m_ppyGameWindow, "OnCannotUseSkill", Py_BuildValue("(is)", GetMainCharacterIndex(), "NEED_TARGET"));
				return;
			}
		}
		else if (m_isDirKey)
		{
			float fDirRot = 0.0f;
			NEW_GetMultiKeyDirRotation(m_isLeft, m_isRight, m_isUp, m_isDown, fDirRot);
    
			CCamera pkCmrCur = CCameraManager.Instance().GetCurrentCamera();
			if (pkCmrCur != null)
			{
				float fCmrCurRot = CameraRotationToCharacterRotation(pkCmrCur.GetRoll());
    
				fDirRot = fmod(360.0f + fCmrCurRot + fDirRot, 360.0f);
			}
    
			pkInstMain.NEW_Attack(fDirRot);
		}
		else
		{
			if (pkInstMain.IsMountingHorse())
			{
				if (pkInstMain.IsHandMode())
				{
					return;
				}
			}
    
			pkInstMain.NEW_Attack();
		}
	}
	public void NEW_Fishing()
	{
		CInstanceBase pkInstMain = NEW_GetMainActorPtr();
		if (pkInstMain == null)
		{
			return;
		}
    
		if (pkInstMain.IsFishing())
		{
			CPythonNetworkStream.Instance().SendFishingPacket(0);
		}
		else
		{
			if (pkInstMain.CanFishing())
			{
				int irot;
				if (pkInstMain.GetFishingRot(irot))
				{
					CPythonNetworkStream.Instance().SendFishingPacket(irot);
				}
				else
				{
					PyCallClassMemberFunc(m_ppyGameWindow, "OnFishingWrongPlace", Py_BuildValue("()"));
				}
			}
		}
	}
	public bool NEW_CancelFishing()
	{
		CInstanceBase pkInstMain = NEW_GetMainActorPtr();
		if (pkInstMain == null)
		{
			return false;
		}
    
		if (pkInstMain.IsFishing())
		{
	//# Laniatus Games Studio Inc. |: This static local variable declaration (not allowed in C#) has been moved just prior to the method:
	//		static uint s_dwLastCancelTime = 0;
			if (CTimer.Instance().GetCurrentMillisecond() < NEW_CancelFishing_s_dwLastCancelTime + 500)
			{
				return false;
			}
    
			CPythonNetworkStream.Instance().SendFishingPacket(0);
			NEW_CancelFishing_s_dwLastCancelTime = CTimer.Instance().GetCurrentMillisecond();
			return true;
		}
    
		return false;
	}

//# Laniatus Games Studio Inc. | TODO TASK: The implementation of the following method could not be found:
//		void NEW_LookAtFocusActor();
//# Laniatus Games Studio Inc. | TODO TASK: The implementation of the following method could not be found:
//		bool NEW_IsAttackableDistanceFocusActor();


//# Laniatus Games Studio Inc. | TODO TASK: The implementation of the following method could not be found:
//		bool NEW_MoveToDestPixelPositionDirection(in TPixelPosition c_rkPPosDst);
//# Laniatus Games Studio Inc. | TODO TASK: The implementation of the following method could not be found:
//		bool NEW_MoveToMousePickedDirection();
	public bool NEW_MoveToMouseScreenDirection()
	{
		UI.CWindowManager rkWndMgr = UI.CWindowManager.Instance();
    
		int lMouseX;
		int lMouseY;
		rkWndMgr.GetMousePosition(lMouseX, lMouseY);
    
		int lScrWidth = rkWndMgr.GetScreenWidth();
		int lScrHeight = rkWndMgr.GetScreenHeight();
		float fMouseX = lMouseX / (float)lScrWidth;
		float fMouseY = lMouseY / (float)lScrHeight;
    
		float fDirRot;
		NEW_GetMouseDirRotation(fMouseX, fMouseY, fDirRot);
    
		return NEW_MoveToDirection(fDirRot);
	}
	public bool NEW_MoveToDirection(float fDirRot)
	{
		if (IsOpenPrivateShop())
		{
			return true;
		}
    
		__ClearReservedAction();
    
		CInstanceBase pkInstMain = NEW_GetMainActorPtr();
		if (pkInstMain == null)
		{
			return false;
		}
    
		if (pkInstMain.isLock())
		{
			if (!pkInstMain.IsUsingMovingSkill())
			{
				return true;
			}
		}
    
		CCamera pkCmrCur = CCameraManager.Instance().GetCurrentCamera();
		if (pkCmrCur != null)
		{
			float fCmrCurRot = CameraRotationToCharacterRotation(pkCmrCur.GetRoll());
    
			if (m_isCmrRot)
			{
				float fSigDirRot = fDirRot;
				if (fSigDirRot > 180.0f)
				{
					fSigDirRot = fSigDirRot - 360.0f;
				}
    
				float fRotRat = fSigDirRot;
				if (fRotRat > 90.0f)
				{
					fRotRat = (180.0f - fRotRat);
				}
				else if (fRotRat < -90.0f)
				{
					fRotRat = (-180.0f - fRotRat);
				}
    
				float fElapsedTime = CPythonApplication.Instance().GetGlobalElapsedTime();
    
				float fRotDeg = -m_fCmrRotSpd * fElapsedTime * fRotRat / 90.0f;
				pkCmrCur.Roll(fRotDeg);
			}
    
			fDirRot = fmod(360.0f + fCmrCurRot + fDirRot, 360.0f);
		}
    
		pkInstMain.NEW_MoveToDirection(fDirRot);
    
		return true;
	}
	public void NEW_Stop()
	{
		CInstanceBase pkInstMain = NEW_GetMainActorPtr();
		if (pkInstMain == null)
		{
			return;
		}
    
		pkInstMain.NEW_Stop();
		m_isLeft = false;
		m_isRight = false;
		m_isUp = false;
		m_isDown = false;
	}

	public bool NEW_IsEmptyReservedDelayTime(float fElapsedTime)
	{
		m_fReservedDelayTime -= fElapsedTime;
    
		if (m_fReservedDelayTime <= 0.0f)
		{
			m_fReservedDelayTime = 0.0f;
			return true;
		}
    
		return false;
	}

	public void SetDungeonDestinationPosition(int ix, int iy)
	{
		m_isDestPosition = true;
		m_ixDestPos = ix;
		m_iyDestPos = iy;
    
		AlarmHaveToGo();
	}
	public void AlarmHaveToGo()
	{
		m_iLastAlarmTime = CTimer.Instance().GetCurrentMillisecond();
    
		CInstanceBase pInstance = NEW_GetMainActorPtr();
		if (pInstance == null)
		{
			return;
		}
    
		TPixelPosition PixelPosition = new TPixelPosition();
		pInstance.NEW_GetPixelPosition(PixelPosition);
    
		float fAngle = GetDegreeFromPosition2(PixelPosition.x, PixelPosition.y, (float)m_ixDestPos, (float)m_iyDestPos);
		fAngle = fmod(540.0f - fAngle, 360.0f);
		_D3DVECTOR v3Rotation = new _D3DVECTOR(0.0f, 0.0f, fAngle);
    
		PixelPosition.y *= -1.0f;
    
		CEffectManager.Instance().RegisterEffect("t:/laniaworkstate/effect/etc/compass/appear_middle.mse");
		CEffectManager.Instance().CreateEffect("t:/laniaworkstate/effect/etc/compass/appear_middle.mse", PixelPosition, v3Rotation);
	}


	public CInstanceBase NEW_FindActorPtr(uint dwVID)
	{
		CPythonCharacterManager rkChrMgr = CPythonCharacterManager.Instance();
		return rkChrMgr.GetInstancePtr(dwVID);
	}
	public CInstanceBase NEW_GetMainActorPtr()
	{
		return NEW_FindActorPtr(m_dwMainCharacterIndex);
	}

	public void Clear()
	{
	//# Laniatus Games Studio Inc. | TODO TASK: The memory management function 'memset' has no equivalent in C#:
		memset(m_playerStatus, 0, sizeof(m_playerStatus));
		NEW_ClearSkillData(true);
    
		m_bisProcessingEmotion = false;
    
		m_dwSendingTargetVID = 0;
		m_fTargetUpdateTime = 0.0f;
    
		m_stName = "";
		m_dwMainCharacterIndex = 0;
		m_dwRace = 0;
		m_dwWeaponMinPower = 0;
		m_dwWeaponMaxPower = 0;
		m_dwWeaponMinMagicPower = 0;
		m_dwWeaponMaxMagicPower = 0;
		m_dwWeaponAddPower = 0;
    
		m_MovingCursorPosition = TPixelPosition(0, 0, 0);
		m_fMovingCursorSettingTime = 0.0f;
    
		m_eReservedMode = MODE_NONE;
		m_fReservedDelayTime = 0.0f;
		m_kPPosReserved = TPixelPosition(0, 0, 0);
		m_dwVIDReserved = 0;
		m_dwIIDReserved = 0;
		m_dwSkillSlotIndexReserved = 0;
		m_dwSkillRangeReserved = 0;
    
		m_isUp = false;
		m_isDown = false;
		m_isLeft = false;
		m_isRight = false;
		m_isSmtMov = false;
		m_isDirMov = false;
		m_isDirKey = false;
		m_isAtkKey = false;
    
		m_isCmrRot = true;
		m_fCmrRotSpd = 20.0f;
    
		m_iComboOld = 0;
    
		m_dwVIDPicked = 0;
		m_dwIIDPicked = 0;
    
		m_dwcurSkillSlotIndex = (uint)-1;
    
		m_dwTargetVID = 0;
		m_dwTargetEndTime = 0;
    
		m_PartyMemberMap.clear();
    
		m_ChallengeInstanceSet.clear();
		m_RevengeInstanceSet.clear();
    
		m_isOpenPrivateShop = false;
		m_isObserverMode = false;
    
		m_isConsumingStamina = false;
		m_fConsumeStaminaPerSec = 0.0f;
		m_fCurrentStamina = 0.0f;
    
		m_inGuildAreaID = 0xffffffff;
    
		__ClearAutoAttackTargetActorID();
		m_ItemAcceInstanceVector.clear();
		m_ItemAcceInstanceVector.resize(3);
    
		for (uint LaniatusDefVariables = 0; LaniatusDefVariables < m_ItemAcceInstanceVector.size(); ++i)
		{
			TItemData rInstance = m_ItemAcceInstanceVector[LaniatusDefVariables];
			ZeroMemory(rInstance, sizeof(TItemData));
		}
    
		m_acceRefineWindowIsOpen = false;
		m_acceRefineWindowType = 3;
		m_acceRefineActivedSlot[0] = -1;
		m_acceRefineActivedSlot[1] = -1;
		m_acceRefineActivedSlot[2] = -1;
	}
	public void ClearSkillDict()
	{
		m_skillSlotDict.clear();
		m_isOpenPrivateShop = false;
		m_isObserverMode = false;
    
		m_isConsumingStamina = false;
		m_fConsumeStaminaPerSec = 0.0f;
		m_fCurrentStamina = 0.0f;
    
		__ClearAutoAttackTargetActorID();
	}
	public void NEW_ClearSkillData(bool bAll)
	{
		SortedDictionary<uint, uint>.Enumerator it;
    
		for (it = m_skillSlotDict.begin(); it.MoveNext();)
		{
			if (bAll || __GetSkillType(it.Current.Key) == CPythonSkill.SKILL_TYPE_ACTIVE)
			{
				it = m_skillSlotDict.erase(it);
			}
			else
			{
			}
		}
    
		for (int LaniatusDefVariables = 0; LaniatusDefVariables < SKILL_MAX_NUM; ++i)
		{
			ZeroMemory(m_playerStatus.aSkill[LaniatusDefVariables], sizeof(TSkillInstance));
		}
    
		for (int j = 0; j < SKILL_MAX_NUM; ++j)
		{
			m_playerStatus.aSkill[j].iGrade = 0;
			m_playerStatus.aSkill[j].fcurEfficientPercentage = 0.0f;
			m_playerStatus.aSkill[j].fnextEfficientPercentage = 0.05f;
		}
    
		if (m_ppyGameWindow)
		{
			PyCallClassMemberFunc(m_ppyGameWindow, "BINARY_CheckGameButton", Py_BuildNone());
		}
	}

	public void Update()
	{
		NEW_RefreshMouseWalkingDirection();
    
		CPythonPlayerEventHandler rkPlayerEventHandler = CPythonPlayerEventHandler.GetSingleton();
		rkPlayerEventHandler.FlushVictimList();
    
		if (m_isDestPosition)
		{
			CInstanceBase pInstance = NEW_GetMainActorPtr();
			if (pInstance != null)
			{
				TPixelPosition PixelPosition = new TPixelPosition();
				pInstance.NEW_GetPixelPosition(PixelPosition);
    
				if (Math.Abs((int)PixelPosition.x - m_ixDestPos) + Math.Abs((int)PixelPosition.y - m_iyDestPos) < 10000)
				{
					m_isDestPosition = false;
				}
				else
				{
					if (CTimer.Instance().GetCurrentMillisecond() - m_iLastAlarmTime > 20000)
					{
						AlarmHaveToGo();
					}
				}
			}
		}
    
		if (m_isConsumingStamina)
		{
			float fElapsedTime = CTimer.Instance().GetElapsedSecond();
			m_fCurrentStamina -= (fElapsedTime * m_fConsumeStaminaPerSec);
    
			SetStatus(POINT_STAMINA, (uint)m_fCurrentStamina);
    
			PyCallClassMemberFunc(m_ppyGameWindow, "RefreshStamina", Py_BuildValue("()"));
		}
    
		__Update_AutoAttack();
		__Update_NotifyGuildAreaEvent();
	}

	public uint GetPlayTime()
	{
		return m_dwPlayTime;
	}
	public void SetPlayTime(uint dwPlayTime)
	{
		m_dwPlayTime = dwPlayTime;
	}

	public void SetMainCharacterIndex(int iIndex)
	{
		m_dwMainCharacterIndex = iIndex;
    
		CInstanceBase pkInstMain = NEW_GetMainActorPtr();
		if (pkInstMain != null)
		{
			CPythonPlayerEventHandler rkPlayerEventHandler = CPythonPlayerEventHandler.GetSingleton();
			pkInstMain.SetEventHandler(rkPlayerEventHandler);
		}
	}

	public uint GetMainCharacterIndex()
	{
		return m_dwMainCharacterIndex;
	}
	public bool IsMainCharacterIndex(uint dwIndex)
	{
		return (m_dwMainCharacterIndex == dwIndex);
	}
	public uint GetGuildID()
	{
		CInstanceBase pkInstMain = NEW_GetMainActorPtr();
		if (pkInstMain == null)
		{
			return 0xffffffff;
		}
    
		return pkInstMain.GetGuildID();
	}
	public void NotifyDeletingCharacterInstance(uint dwVID)
	{
		if (m_dwMainCharacterIndex == dwVID)
		{
			m_dwMainCharacterIndex = 0;
		}
	}
	public void NotifyCharacterDead(uint dwVID)
	{
		if (__IsSameTargetVID(dwVID))
		{
			SetTarget(0);
		}
	}
	public void NotifyCharacterUpdate(uint dwVID)
	{
		if (__IsSameTargetVID(dwVID))
		{
			CInstanceBase pMainInstance = NEW_GetMainActorPtr();
			CInstanceBase pTargetInstance = CPythonCharacterManager.Instance().GetInstancePtr(dwVID);
			if (pMainInstance != null && pTargetInstance != null)
			{
				if (!pMainInstance.IsTargetableInstance(pTargetInstance))
				{
					SetTarget(0);
					PyCallClassMemberFunc(m_ppyGameWindow, "CloseTargetBoard", Py_BuildValue("()"));
				}
				else
				{
					PyCallClassMemberFunc(m_ppyGameWindow, "RefreshTargetBoardByVID", Py_BuildValue("(i)", dwVID));
				}
			}
		}
	}
	public void NotifyDeadMainCharacter()
	{
		__ClearAutoAttackTargetActorID();
	}
	public void NotifyChangePKMode()
	{
		PyCallClassMemberFunc(m_ppyGameWindow, "OnChangePKMode", Py_BuildValue("()"));
	}

	public string GetName()
	{
		return m_stName.c_str();
	}
	public void SetName(string name)
	{
		m_stName = name;
	}

	public void SetRace(uint dwRace)
	{
		m_dwRace = dwRace;
	}
	public uint GetRace()
	{
		return m_dwRace;
	}

	public void SetWeaponPower(uint dwMinPower, uint dwMaxPower, uint dwMinMagicPower, uint dwMaxMagicPower, uint dwAddPower)
	{
		m_dwWeaponMinPower = dwMinPower;
		m_dwWeaponMaxPower = dwMaxPower;
		m_dwWeaponMinMagicPower = dwMinMagicPower;
		m_dwWeaponMaxMagicPower = dwMaxMagicPower;
		m_dwWeaponAddPower = dwAddPower;
    
		__UpdateBattleStatus();
	}
	public void SetStatus(uint dwType, long lValue)
	{
		if (dwType >= POINT_MAX_NUM)
		{
			Debug.Assert(!" CPythonPlayer::SetStatus - Strange Status Type!");
			Tracef("CPythonPlayer::SetStatus - Set Status Type Error\n");
			return;
		}
    
		if (dwType == POINT_LEVEL)
		{
			CInstanceBase pkPlayer = NEW_GetMainActorPtr();
    
			if (pkPlayer != null)
			{
				pkPlayer.UpdateTextTailLevel(lValue);
			}
		}
    
		switch (dwType)
		{
			case POINT_MIN_WEP:
			case POINT_MAX_WEP:
			case POINT_MIN_ATK:
			case POINT_MAX_ATK:
			case POINT_HIT_RATE:
			case POINT_EVADE_RATE:
			case POINT_LEVEL:
			case POINT_ST:
			case POINT_DX:
			case POINT_IQ:
				m_playerStatus.SetPoint(dwType, lValue);
				__UpdateBattleStatus();
				break;
			default:
				m_playerStatus.SetPoint(dwType, lValue);
				break;
		}
	}
	public long GetStatus(uint dwType)
	{
		if (dwType >= POINT_MAX_NUM)
		{
			Debug.Assert(!" CPythonPlayer::GetStatus - Strange Status Type!");
			Tracef("CPythonPlayer::GetStatus - Get Status Type Error\n");
			return 0;
		}
    
		return m_playerStatus.GetPoint(dwType);
	}

	public void MoveItemData(TItemPos SrcCell, TItemPos DstCell)
	{
		if (!SrcCell.IsValidCell() || !DstCell.IsValidCell())
		{
			return;
		}
    
		TItemData src_item = new TItemData(*GetItemData(SrcCell));
		TItemData dst_item = new TItemData(*GetItemData(DstCell));
		SetItemData(DstCell, src_item);
		SetItemData(SrcCell, dst_item);
	}
	public void SetItemData(TItemPos Cell, in TItemData c_rkItemInst)
	{
		if (!Cell.IsValidCell())
		{
			return;
		}
    
		if (c_rkItemInst.vnum != 0)
		{
			CItemData pItemData;
			if (!CItemManager.Instance().GetItemDataPointer(c_rkItemInst.vnum, pItemData))
			{
				TraceError("CPythonPlayer::SetItemData(window_type : %d, dwSlotIndex=%d, itemIndex=%d) - Failed to item data\n", Cell.window_type, Cell.cell, c_rkItemInst.vnum);
				return;
			}
		}
    
		switch (Cell.window_type)
		{
		case INVENTORY:
		case EQUIPMENT:
			m_playerStatus.aItem[Cell.cell] = c_rkItemInst;
			break;
		case DRAGON_SOUL_INVENTORY:
			m_playerStatus.aDSItem[Cell.cell] = c_rkItemInst;
			break;
		}
	}
//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: const TItemData * GetItemData(TItemPos Cell) const;
	public TItemData GetItemData(TItemPos Cell)
	{
		if (!Cell.IsValidCell())
		{
			return null;
		}
    
		switch (Cell.window_type)
		{
		case INVENTORY:
		case EQUIPMENT:
			return m_playerStatus.aItem[Cell.cell];
		case DRAGON_SOUL_INVENTORY:
			return m_playerStatus.aDSItem[Cell.cell];
		default:
			return null;
		}
	}
	public void SetItemCount(TItemPos Cell, ushort wCount)
	{
		if (!Cell.IsValidCell())
		{
			return;
		}
    
	//# Laniatus Games Studio Inc. | TODO TASK: There is no equivalent to 'const_cast' in C#:
		(const_cast <TItemData>(GetItemData(Cell))).count = wCount;
		PyCallClassMemberFunc(m_ppyGameWindow, "RefreshInventory", Py_BuildValue("()"));
	}
	public void SetItemMetinSocket(TItemPos Cell, uint dwMetinSocketIndex, uint dwMetinNumber)
	{
		if (!Cell.IsValidCell())
		{
			return;
		}
		if (dwMetinSocketIndex >= ITEM_SOCKET_SLOT_MAX_NUM)
		{
			return;
		}
    
	//# Laniatus Games Studio Inc. | TODO TASK: There is no equivalent to 'const_cast' in C#:
		(const_cast <TItemData>(GetItemData(Cell))).alSockets[dwMetinSocketIndex] = dwMetinNumber;
	}
	public void SetItemAttribute(TItemPos Cell, uint dwAttrIndex, byte byType, short sValue)
	{
		if (!Cell.IsValidCell())
		{
			return;
		}
		if (dwAttrIndex >= ITEM_ATTRIBUTE_SLOT_MAX_NUM)
		{
			return;
		}
    
	//# Laniatus Games Studio Inc. | TODO TASK: There is no equivalent to 'const_cast' in C#:
		(const_cast <TItemData>(GetItemData(Cell))).aAttr[dwAttrIndex].bType = byType;
	//# Laniatus Games Studio Inc. | TODO TASK: There is no equivalent to 'const_cast' in C#:
		(const_cast <TItemData>(GetItemData(Cell))).aAttr[dwAttrIndex].sValue = sValue;
	}
	public uint GetItemIndex(TItemPos Cell)
	{
		if (!Cell.IsValidCell())
		{
			return 0;
		}
    
		return GetItemData(Cell).vnum;
	}
	public uint GetItemFlags(TItemPos Cell)
	{
		if (!Cell.IsValidCell())
		{
			return 0;
		}
		TItemData pItem = GetItemData(Cell);
		Debug.Assert(pItem != null);
		return pItem.flags;
	}
	public uint GetItemCount(TItemPos Cell)
	{
		if (!Cell.IsValidCell())
		{
			return 0;
		}
		TItemData pItem = GetItemData(Cell);
		if (pItem == null)
		{
			return 0;
		}
		else
		{
			return pItem.count;
		}
	}
	public uint GetItemCountByVnum(uint dwVnum)
	{
		uint dwCount = 0;
    
		for (int LaniatusDefVariables = 0; LaniatusDefVariables < c_Inventory_Count; ++i)
		{
			TItemData c_rItemData = m_playerStatus.aItem[LaniatusDefVariables];
			if (c_rItemData.vnum == dwVnum)
			{
				dwCount += c_rItemData.count;
			}
		}
    
		return dwCount;
	}
	public uint GetItemMetinSocket(TItemPos Cell, uint dwMetinSocketIndex)
	{
		if (!Cell.IsValidCell())
		{
			return 0;
		}
    
		if (dwMetinSocketIndex >= ITEM_SOCKET_SLOT_MAX_NUM)
		{
			return 0;
		}
    
		return GetItemData(Cell).alSockets[dwMetinSocketIndex];
	}
	public void GetItemAttribute(TItemPos Cell, uint dwAttrSlotIndex, ref byte pbyType, ref short psValue)
	{
		pbyType = null;
		psValue = null;
    
		if (!Cell.IsValidCell())
		{
			return;
		}
    
		if (dwAttrSlotIndex >= ITEM_ATTRIBUTE_SLOT_MAX_NUM)
		{
			return;
		}
    
		pbyType = GetItemData(Cell).aAttr[dwAttrSlotIndex].bType;
		psValue = GetItemData(Cell).aAttr[dwAttrSlotIndex].sValue;
	}
	public void SendClickItemPacket(uint dwIID)
	{
		if (IsObserverMode())
		{
			return;
		}
    
	//# Laniatus Games Studio Inc. |: This static local variable declaration (not allowed in C#) has been moved just prior to the method:
	//	static uint s_dwNextTCPTime = 0;
    
		uint dwCurTime = ELTimer_GetMSec();
    
		if (dwCurTime >= SendClickItemPacket_s_dwNextTCPTime)
		{
			SendClickItemPacket_s_dwNextTCPTime = dwCurTime + 100;
    
			string c_szOwnerName;
			if (!CPythonItem.Instance().GetOwnership(dwIID, c_szOwnerName))
			{
				return;
			}
    
			if (strlen(c_szOwnerName) > 0)
			{
			if (0 != strcmp(c_szOwnerName, GetName()))
			{
				CItemData pItemData;
				if (!CItemManager.Instance().GetItemDataPointer(CPythonItem.Instance().GetVirtualNumberOfGroundItem(dwIID), pItemData))
				{
					Tracenf("CPythonPlayer::SendClickItemPacket(dwIID=%d) : Non-exist item.", dwIID);
					return;
				}
				if (!IsPartyMemberByName(c_szOwnerName) || pItemData.IsAntiFlag(CItemData.ITEM_ANTIFLAG_DROP | CItemData.ITEM_ANTIFLAG_GIVE))
				{
					PyCallClassMemberFunc(m_ppyGameWindow, "OnCannotPickItem", Py_BuildValue("()"));
					return;
				}
			}
			}
    
			CPythonNetworkStream rkNetStream = CPythonNetworkStream.Instance();
			rkNetStream.SendItemPickUpPacket(dwIID);
		}
	}
	public void SendPickupItemPacket()
	{
		if (IsObserverMode())
		{
			return;
		}
    
	//# Laniatus Games Studio Inc. |: This static local variable declaration (not allowed in C#) has been moved just prior to the method:
	//	static uint s_dwNextTCPTime = 0;
    
		uint dwCurTime = ELTimer_GetMSec();
    
		if (dwCurTime >= SendPickupItemPacket_s_dwNextTCPTime)
		{
			SendPickupItemPacket_s_dwNextTCPTime = dwCurTime + 100;
    
			CPythonNetworkStream rkNetStream = CPythonNetworkStream.Instance();
			rkNetStream.SendItemPickUpPacket(0);
		}
	}
	public void RequestAddLocalQuickSlot(uint dwLocalSlotIndex, uint dwWndType, uint dwWndItemPos)
	{
		if (dwLocalSlotIndex >= QUICKSLOT_MAX_COUNT_PER_LINE)
		{
			return;
		}
    
		uint dwGlobalSlotIndex = LocalQuickSlotIndexToGlobalQuickSlotIndex(dwLocalSlotIndex);
    
		CPythonNetworkStream rkNetStream = CPythonNetworkStream.Instance();
		rkNetStream.SendQuickSlotAddPacket((byte)dwGlobalSlotIndex, (byte)dwWndType, (byte)dwWndItemPos);
	}
	public void RequestAddToEmptyLocalQuickSlot(uint dwWndType, uint dwWndItemPos)
	{
		for (int LaniatusDefVariables = 0; LaniatusDefVariables < QUICKSLOT_MAX_COUNT_PER_LINE; ++i)
		{
			TQuickSlot rkQuickSlot = __RefLocalQuickSlot(i);
    
			if (0 == rkQuickSlot.Type)
			{
				uint dwGlobalQuickSlotIndex = LocalQuickSlotIndexToGlobalQuickSlotIndex(i);
				CPythonNetworkStream rkNetStream = CPythonNetworkStream.Instance();
				rkNetStream.SendQuickSlotAddPacket((byte)dwGlobalQuickSlotIndex, (byte)dwWndType, (byte)dwWndItemPos);
				return;
			}
		}
    
	}
	public void RequestMoveGlobalQuickSlotToLocalQuickSlot(uint dwGlobalSrcSlotIndex, uint dwLocalDstSlotIndex)
	{
		uint dwGlobalDstSlotIndex = LocalQuickSlotIndexToGlobalQuickSlotIndex(dwLocalDstSlotIndex);
    
		CPythonNetworkStream rkNetStream = CPythonNetworkStream.Instance();
		rkNetStream.SendQuickSlotMovePacket((byte) dwGlobalSrcSlotIndex, (byte)dwGlobalDstSlotIndex);
	}
	public void RequestDeleteGlobalQuickSlot(uint dwGlobalSlotIndex)
	{
		if (dwGlobalSlotIndex >= QUICKSLOT_MAX_COUNT)
		{
			return;
		}
    
		CPythonNetworkStream rkNetStream = CPythonNetworkStream.Instance();
		rkNetStream.SendQuickSlotDelPacket((byte)dwGlobalSlotIndex);
	}
	public void RequestUseLocalQuickSlot(uint dwLocalSlotIndex)
	{
		if (dwLocalSlotIndex >= QUICKSLOT_MAX_COUNT_PER_LINE)
		{
			return;
		}
    
		uint dwRegisteredType;
		uint dwRegisteredItemPos;
		GetLocalQuickSlotData(dwLocalSlotIndex, dwRegisteredType, dwRegisteredItemPos);
    
		switch (dwRegisteredType)
		{
			case SLOT_TYPE_INVENTORY:
			{
				CPythonNetworkStream rkNetStream = CPythonNetworkStream.Instance();
				rkNetStream.SendItemUsePacket(TItemPos(INVENTORY, (ushort)dwRegisteredItemPos));
				break;
			}
			case SLOT_TYPE_SKILL:
			{
				ClickSkillSlot(dwRegisteredItemPos);
				break;
			}
			case SLOT_TYPE_EMOTION:
			{
				PyCallClassMemberFunc(m_ppyGameWindow, "BINARY_ActEmotion", Py_BuildValue("(i)", dwRegisteredItemPos));
				break;
			}
		}
	}
	public uint LocalQuickSlotIndexToGlobalQuickSlotIndex(uint dwLocalSlotIndex)
	{
		return m_playerStatus.lQuickPageIndex * QUICKSLOT_MAX_COUNT_PER_LINE + dwLocalSlotIndex;
	}

	public void GetGlobalQuickSlotData(uint dwGlobalSlotIndex, ref uint pdwWndType, ref uint pdwWndItemPos)
	{
		TQuickSlot rkQuickSlot = __RefGlobalQuickSlot(dwGlobalSlotIndex);
		pdwWndType = rkQuickSlot.Type;
		pdwWndItemPos = rkQuickSlot.Position;
	}
	public void GetLocalQuickSlotData(uint dwSlotPos, ref uint pdwWndType, ref uint pdwWndItemPos)
	{
		TQuickSlot rkQuickSlot = __RefLocalQuickSlot(dwSlotPos);
		pdwWndType = rkQuickSlot.Type;
		pdwWndItemPos = rkQuickSlot.Position;
	}
	public void RemoveQuickSlotByValue(int iType, int iPosition)
	{
		for (byte LaniatusDefVariables = 0; LaniatusDefVariables < QUICKSLOT_MAX_NUM; ++i)
		{
			if (iType == m_playerStatus.aQuickSlot[LaniatusDefVariables].Type)
			{
				if (iPosition == m_playerStatus.aQuickSlot[LaniatusDefVariables].Position)
				{
					CPythonNetworkStream.Instance().SendQuickSlotDelPacket(i);
				}
			}
		}
	}

	public char IsItem(TItemPos Cell)
	{
		if (!Cell.IsValidCell())
		{
			return 0;
		}
    
		return 0 != GetItemData(Cell).vnum;
	}

	public bool IsBeltInventorySlot(TItemPos Cell)
	{
		return Cell.IsBeltInventoryCell();
	}

	public bool IsInventorySlot(TItemPos Cell)
	{
		return !Cell.IsEquipCell() && Cell.IsValidCell();
	}
	public bool IsEquipmentSlot(TItemPos Cell)
	{
		return Cell.IsEquipCell();
	}

	public bool IsEquipItemInSlot(TItemPos Cell)
	{
		if (!Cell.IsEquipCell())
		{
			return false;
		}
    
		TItemData pData = GetItemData(Cell);
    
		if (null == pData)
		{
			return false;
		}
    
		uint dwItemIndex = pData.vnum;
    
		CItemManager.Instance().SelectItemData(dwItemIndex);
		CItemData pItemData = CItemManager.Instance().GetSelectedItemDataPointer();
		if (pItemData == null)
		{
			TraceError("Failed to find ItemData - CPythonPlayer::IsEquipItem(window_type=%d, iSlotindex=%d)\n", Cell.window_type, Cell.cell);
			return false;
		}
    
		return pItemData.IsEquipment() ? true : false;
	}

	public void SetAcceItemData(uint dwSlotIndex, TItemPos srcPos, in TItemData rItemInstance)
	{
		if (dwSlotIndex >= m_ItemAcceInstanceVector.size())
		{
			TraceError("CPythonSafeBox::SetAcceItemData(dwSlotIndex=%d) - Strange slot index", dwSlotIndex);
			return;
		}
    
		if (dwSlotIndex != ACCE_SLOT_RESULT)
		{
			PyCallClassMemberFunc(m_ppyGameWindow, "ActivateAcceSlot", Py_BuildValue("(i)", srcPos.cell));
		}
    
		m_ItemAcceInstanceVector[dwSlotIndex] = rItemInstance;
	}
	public void DelAcceItemData(uint dwSlotIndex, TItemPos srcPos)
	{
		if (dwSlotIndex >= m_ItemAcceInstanceVector.size())
		{
			TraceError("CPythonPlayer::DelAcceItemData(dwSlotIndex=%d) - Strange slot index", dwSlotIndex);
			return;
		}
    
		TItemData rInstance = m_ItemAcceInstanceVector[dwSlotIndex];
    
		CItemData pItemData = null;
		if (CItemManager.instance().GetItemDataPointer(rInstance.vnum, pItemData))
		{
			if (dwSlotIndex == ACCE_SLOT_LEFT)
			{
				DelAcceItemData(ACCE_SLOT_RESULT);
			}
    
			if (pItemData.GetType() == CItemData.ITEM_TYPE_WEAPON || pItemData.GetType() == CItemData.ITEM_TYPE_ARMOR)
			{
				DelAcceItemData(ACCE_SLOT_RESULT);
			}
    
			if (srcPos != NPOS)
			{
				PyCallClassMemberFunc(this.m_ppyGameWindow, "DeactivateAcceSlot", Py_BuildValue("(i)", srcPos.cell));
			}
    
			ZeroMemory(rInstance, sizeof(TItemData));
		}
	}
	public int GetCurrentAcceSize()
	{
		return m_ItemAcceInstanceVector.size();
	}
	public bool GetAcceSlotItemID(uint dwSlotIndex, ref uint pdwItemID)
	{
		if (dwSlotIndex >= m_ItemAcceInstanceVector.size())
		{
			TraceError("CPythonPlayer::GetAcceSlotItemID(dwSlotIndex=%d) - Strange slot index", dwSlotIndex);
			return false;
		}
    
		pdwItemID = m_ItemAcceInstanceVector[dwSlotIndex].vnum;
    
		return true;
	}
	public bool GetAcceItemDataPtr(uint dwSlotIndex, TItemData[] ppInstance)
	{
		if (dwSlotIndex >= m_ItemAcceInstanceVector.size())
		{
			TraceError("CPythonPlayer::GetAcceItemDataPtr(dwSlotIndex=%d) - Strange slot index", dwSlotIndex);
			return false;
		}
    
		ppInstance[0] = &m_ItemAcceInstanceVector[dwSlotIndex];
    
		return true;
	}
	public bool IsEmtpyAcceWindow()
	{
		foreach (var LaniatusDefVariables in m_ItemAcceInstanceVector)
		{
    
			if (i.vnum)
			{
				break;
			}
    
			return false;
		}
    
		return true;
	}
	public int GetCurrentAcceItemCount()
	{
		int itemCount = 0;
		foreach (var LaniatusDefVariables in m_ItemAcceInstanceVector)
		{
    
			if (i.vnum)
			{
				++itemCount;
			}
		}
    
		return itemCount;
	}
	public void SetAcceRefineWindowOpen(int type)
	{
		bool isOpen = m_acceRefineWindowIsOpen == 0;
		m_acceRefineWindowType = type;
		m_acceRefineWindowIsOpen = isOpen;
	}
	public void SetActivedAcceSlot(int acceSlot, int itemPos)
	{
		m_acceRefineActivedSlot[acceSlot] = itemPos;
	}
	public int FindActivedSlot(int acceSlot)
	{
		for (int LaniatusDefVariables = 0; LaniatusDefVariables < 3; ++i)
		{
			if (m_acceRefineActivedSlot[LaniatusDefVariables] == acceSlot)
			{
				return i;
			}
		}
    
		return 3;
	}
	public int FindUsingSlot(int acceSlot)
	{
		if (acceSlot == 3)
		{
			return -1;
		}
		return m_acceRefineActivedSlot[acceSlot];
	}

	public int GetQuickPage()
	{
		return m_playerStatus.lQuickPageIndex;
	}
	public void SetQuickPage(int nQuickPageIndex)
	{
		if (nQuickPageIndex < 0)
		{
			m_playerStatus.lQuickPageIndex = QUICKSLOT_MAX_LINE + nQuickPageIndex;
		}
		else if (nQuickPageIndex >= QUICKSLOT_MAX_LINE)
		{
			m_playerStatus.lQuickPageIndex = nQuickPageIndex % QUICKSLOT_MAX_LINE;
		}
		else
		{
			m_playerStatus.lQuickPageIndex = nQuickPageIndex;
		}
    
		PyCallClassMemberFunc(m_ppyGameWindow, "RefreshInventory", Py_BuildValue("()"));
	}
	public void AddQuickSlot(int QuickSlotIndex, char IconType, char IconPosition)
	{
		if (QuickSlotIndex < 0 || QuickSlotIndex >= QUICKSLOT_MAX_NUM)
		{
			return;
		}
    
		m_playerStatus.aQuickSlot[QuickSlotIndex].Type = IconType;
		m_playerStatus.aQuickSlot[QuickSlotIndex].Position = IconPosition;
	}
	public void DeleteQuickSlot(int QuickSlotIndex)
	{
		if (QuickSlotIndex < 0 || QuickSlotIndex >= QUICKSLOT_MAX_NUM)
		{
			return;
		}
    
		m_playerStatus.aQuickSlot[QuickSlotIndex].Type = 0;
		m_playerStatus.aQuickSlot[QuickSlotIndex].Position = 0;
	}
	public void MoveQuickSlot(int Source, int Target)
	{
		if (Source < 0 || Source >= QUICKSLOT_MAX_NUM)
		{
			return;
		}
    
		if (Target < 0 || Target >= QUICKSLOT_MAX_NUM)
		{
			return;
		}
    
		TQuickSlot rkSrcSlot = __RefGlobalQuickSlot(Source);
		TQuickSlot rkDstSlot = __RefGlobalQuickSlot(Target);
    
		std::swap(rkSrcSlot, rkDstSlot);
	}

	public void SetSkill(uint dwSlotIndex, uint dwSkillIndex)
	{
		if (dwSlotIndex >= SKILL_MAX_NUM)
		{
			return;
		}
    
		m_playerStatus.aSkill[dwSlotIndex].dwIndex = dwSkillIndex;
		m_skillSlotDict[dwSkillIndex] = dwSlotIndex;
	}
	public bool GetSkillSlotIndex(uint dwSkillIndex, ref uint pdwSlotIndex)
	{
		SortedDictionary<uint, uint>.Enumerator f = m_skillSlotDict.find(dwSkillIndex);
		if (m_skillSlotDict.end() == f)
		{
			return false;
		}
    
	//# Laniatus Games Studio Inc. | TODO TASK: Iterators are only converted within the context of 'while' and 'for' loops:
		pdwSlotIndex = f.second;
    
		return true;
	}
	public int GetSkillIndex(uint dwSlotIndex)
	{
		if (dwSlotIndex >= SKILL_MAX_NUM)
		{
			return 0;
		}
    
		return m_playerStatus.aSkill[dwSlotIndex].dwIndex;
	}
	public int GetSkillGrade(uint dwSlotIndex)
	{
		if (dwSlotIndex >= SKILL_MAX_NUM)
		{
			return 0;
		}
    
		return m_playerStatus.aSkill[dwSlotIndex].iGrade;
	}
	public int GetSkillLevel(uint dwSlotIndex)
	{
		if (dwSlotIndex >= SKILL_MAX_NUM)
		{
			return 0;
		}
    
		return m_playerStatus.aSkill[dwSlotIndex].iLevel;
	}
	public float GetSkillCurrentEfficientPercentage(uint dwSlotIndex)
	{
		if (dwSlotIndex >= SKILL_MAX_NUM)
		{
			return 0F;
		}
    
		return m_playerStatus.aSkill[dwSlotIndex].fcurEfficientPercentage;
	}
	public float GetSkillNextEfficientPercentage(uint dwSlotIndex)
	{
		if (dwSlotIndex >= SKILL_MAX_NUM)
		{
			return 0F;
		}
    
		return m_playerStatus.aSkill[dwSlotIndex].fnextEfficientPercentage;
	}
	public void SetSkillLevel(uint dwSlotIndex, uint dwSkillLevel)
	{
		Debug.Assert(!"CPythonPlayer::SetSkillLevel - ??????? ?ʴ? ?Լ?");
		if (dwSlotIndex >= SKILL_MAX_NUM)
		{
			return;
		}
    
		m_playerStatus.aSkill[dwSlotIndex].iGrade = -1;
		m_playerStatus.aSkill[dwSlotIndex].iLevel = dwSkillLevel;
	}
	public void SetSkillLevel_(uint dwSkillIndex, uint dwSkillGrade, uint dwSkillLevel)
	{
		uint dwSlotIndex;
		if (!GetSkillSlotIndex(dwSkillIndex, dwSlotIndex))
		{
			return;
		}
    
		if (dwSlotIndex >= SKILL_MAX_NUM)
		{
			return;
		}
    
		switch (dwSkillGrade)
		{
			case 0:
				m_playerStatus.aSkill[dwSlotIndex].iGrade = dwSkillGrade;
				m_playerStatus.aSkill[dwSlotIndex].iLevel = dwSkillLevel;
				break;
			case 1:
				m_playerStatus.aSkill[dwSlotIndex].iGrade = dwSkillGrade;
				m_playerStatus.aSkill[dwSlotIndex].iLevel = dwSkillLevel - 20 + 1;
				break;
			case 2:
				m_playerStatus.aSkill[dwSlotIndex].iGrade = dwSkillGrade;
				m_playerStatus.aSkill[dwSlotIndex].iLevel = dwSkillLevel - 30 + 1;
				break;
			case 3:
				m_playerStatus.aSkill[dwSlotIndex].iGrade = dwSkillGrade;
				m_playerStatus.aSkill[dwSlotIndex].iLevel = dwSkillLevel - 40 + 1;
				break;
		}
    
		const uint SKILL_MAX_LEVEL = 40;
    
    
    
    
    
		if (dwSkillLevel > SKILL_MAX_LEVEL)
		{
			m_playerStatus.aSkill[dwSlotIndex].fcurEfficientPercentage = 0.0f;
			m_playerStatus.aSkill[dwSlotIndex].fnextEfficientPercentage = 0.0f;
    
			TraceError("CPythonPlayer::SetSkillLevel(SlotIndex=%d, SkillLevel=%d)", dwSlotIndex, dwSkillLevel);
			return;
		}
    
		m_playerStatus.aSkill[dwSlotIndex].fcurEfficientPercentage = LocaleService_GetSkillPower(dwSkillLevel) / 100.0f;
		m_playerStatus.aSkill[dwSlotIndex].fnextEfficientPercentage = LocaleService_GetSkillPower(dwSkillLevel + 1) / 100.0f;
    
	}
	public bool IsToggleSkill(uint dwSlotIndex)
	{
		if (dwSlotIndex >= SKILL_MAX_NUM)
		{
			return false;
		}
    
		uint dwSkillIndex = m_playerStatus.aSkill[dwSlotIndex].dwIndex;
    
		CPythonSkill.TSkillData pSkillData;
		if (!CPythonSkill.Instance().GetSkillData(dwSkillIndex, pSkillData))
		{
			return false;
		}
    
		return pSkillData.IsToggleSkill();
	}
	public void ClickSkillSlot(uint dwSlotIndex)
	{
		if (dwSlotIndex >= DefineConstants.SKILL_MAX_NUM)
		{
			return;
		}
    
		TSkillInstance rkSkillInst = m_playerStatus.aSkill[dwSlotIndex];
    
		SSkillData pSkillData;
		if (!CPythonSkill.Instance().GetSkillData(rkSkillInst.dwIndex, pSkillData))
		{
			return;
		}
    
		if (CPythonSkill.SKILL_TYPE_GUILD == pSkillData.byType)
		{
			UseGuildSkill(dwSlotIndex);
			return;
		}
    
		if (!pSkillData.IsCanUseSkill())
		{
			return;
		}
    
		if (pSkillData.IsStandingSkill())
		{
			if (pSkillData.IsToggleSkill())
			{
				if (IsSkillActive(dwSlotIndex))
				{
					CInstanceBase pkInstMain = NEW_GetMainActorPtr();
					if (pkInstMain == null)
					{
						return;
					}
					if (pkInstMain.IsUsingSkill())
					{
						return;
					}
    
					CPythonNetworkStream.Instance().SendUseSkillPacket(rkSkillInst.dwIndex);
					return;
				}
			}
    
			__UseSkill(dwSlotIndex);
			return;
		}
    
		if (m_dwcurSkillSlotIndex == dwSlotIndex)
		{
			__UseSkill(m_dwcurSkillSlotIndex);
			return;
		}
    
		if (!__IsRightButtonSkillMode())
		{
			__UseSkill(dwSlotIndex);
		}
		else
		{
			m_dwcurSkillSlotIndex = dwSlotIndex;
			PyCallClassMemberFunc(m_ppyGameWindow, "ChangeCurrentSkill", Py_BuildValue("(i)", dwSlotIndex));
		}
	}
	public void ChangeCurrentSkillNumberOnly(uint dwSlotIndex)
	{
		if (dwSlotIndex >= DefineConstants.SKILL_MAX_NUM)
		{
			return;
		}
    
		TSkillInstance rkSkillInst = m_playerStatus.aSkill[dwSlotIndex];
    
		SSkillData pSkillData;
		if (!CPythonSkill.Instance().GetSkillData(rkSkillInst.dwIndex, pSkillData))
		{
			return;
		}
    
		if (!pSkillData.IsCanUseSkill())
		{
			return;
		}
    
		if (!__IsRightButtonSkillMode())
		{
			if (!__IsTarget())
			{
				PyCallClassMemberFunc(m_ppyGameWindow, "OnCannotUseSkill", Py_BuildValue("(is)", GetMainCharacterIndex(), "NEED_TARGET"));
				return;
			}
    
			ClickSkillSlot(dwSlotIndex);
		}
		else
		{
			m_dwcurSkillSlotIndex = dwSlotIndex;
			PyCallClassMemberFunc(m_ppyGameWindow, "ChangeCurrentSkill", Py_BuildValue("(i)", dwSlotIndex));
		}
	}
	public bool FindSkillSlotIndexBySkillIndex(uint dwSkillIndex, ref uint pdwSkillSlotIndex)
	{
		for (int LaniatusDefVariables = 0; LaniatusDefVariables < DefineConstants.SKILL_MAX_NUM; ++i)
		{
			TSkillInstance rkSkillInst = m_playerStatus.aSkill[LaniatusDefVariables];
			if (dwSkillIndex == rkSkillInst.dwIndex)
			{
				pdwSkillSlotIndex = (uint)i;
				return true;
			}
		}
    
		return false;
	}

	public void SetSkillCoolTime(uint dwSkillIndex)
	{
		uint dwSlotIndex;
		if (!GetSkillSlotIndex(dwSkillIndex, dwSlotIndex))
		{
			Tracenf("CPythonPlayer::SetSkillCoolTime(dwSkillIndex=%d) - FIND SLOT ERROR", dwSkillIndex);
			return;
		}
    
		if (dwSlotIndex >= SKILL_MAX_NUM)
		{
			Tracenf("CPythonPlayer::SetSkillCoolTime(dwSkillIndex=%d) - dwSlotIndex=%d/%d OUT OF RANGE", dwSkillIndex, dwSlotIndex, SKILL_MAX_NUM);
			return;
		}
    
		m_playerStatus.aSkill[dwSlotIndex].isCoolTime = true;
	}
	public void EndSkillCoolTime(uint dwSkillIndex)
	{
		uint dwSlotIndex;
		if (!GetSkillSlotIndex(dwSkillIndex, dwSlotIndex))
		{
			Tracenf("CPythonPlayer::EndSkillCoolTime(dwSkillIndex=%d) - FIND SLOT ERROR", dwSkillIndex);
			return;
		}
    
		if (dwSlotIndex >= SKILL_MAX_NUM)
		{
			Tracenf("CPythonPlayer::EndSkillCoolTime(dwSkillIndex=%d) - dwSlotIndex=%d/%d OUT OF RANGE", dwSkillIndex, dwSlotIndex, SKILL_MAX_NUM);
			return;
		}
    
		m_playerStatus.aSkill[dwSlotIndex].isCoolTime = false;
	}

	public float GetSkillCoolTime(uint dwSlotIndex)
	{
		if (dwSlotIndex >= SKILL_MAX_NUM)
		{
			return 0.0f;
		}
    
		return m_playerStatus.aSkill[dwSlotIndex].fCoolTime;
	}
	public float GetSkillElapsedCoolTime(uint dwSlotIndex)
	{
		if (dwSlotIndex >= SKILL_MAX_NUM)
		{
			return 0.0f;
		}
    
		return CTimer.Instance().GetCurrentSecond() - m_playerStatus.aSkill[dwSlotIndex].fLastUsedTime;
	}
	public bool IsSkillActive(uint dwSlotIndex)
	{
		if (dwSlotIndex >= SKILL_MAX_NUM)
		{
			return false;
		}
    
		return m_playerStatus.aSkill[dwSlotIndex].bActive;
	}
	public bool IsSkillCoolTime(uint dwSlotIndex)
	{
		if (!__CheckRestSkillCoolTime(dwSlotIndex))
		{
			return false;
		}
    
		return true;
	}
	public void UseGuildSkill(uint dwSkillSlotIndex)
	{
		CInstanceBase pkInstMain = NEW_GetMainActorPtr();
		if (pkInstMain == null)
		{
			return;
		}
		if (!pkInstMain.CanUseSkill())
		{
			return;
		}
    
		if (dwSkillSlotIndex >= DefineConstants.SKILL_MAX_NUM)
		{
			Tracenf("CPythonPlayer::UseGuildSkill(dwSkillSlotIndex=%d) It's not available skill slot number", dwSkillSlotIndex);
			return;
		}
    
		TSkillInstance rkSkillInst = m_playerStatus.aSkill[dwSkillSlotIndex];
    
		uint dwSkillIndex = rkSkillInst.dwIndex;
    
		SSkillData pSkillData;
		if (!CPythonSkill.Instance().GetSkillData(dwSkillIndex, pSkillData))
		{
			return;
		}
    
		if (__CheckRestSkillCoolTime(dwSkillSlotIndex))
		{
			PyCallClassMemberFunc(m_ppyGameWindow, "OnCannotUseSkill", Py_BuildValue("(is)", GetMainCharacterIndex(), "WAIT_COOLTIME"));
			return;
		}
    
		if (pSkillData.IsOnlyForGuildWar())
		{
			if (!CPythonGuild.Instance().IsDoingGuildWar())
			{
				PyCallClassMemberFunc(m_ppyGameWindow, "OnCannotUseSkill", Py_BuildValue("(is)", GetMainCharacterIndex(), "ONLY_FOR_GUILD_WAR"));
				return;
			}
		}
    
		uint dwMotionIndex = pSkillData.GetSkillMotionIndex();
		if (!pkInstMain.NEW_UseSkill(dwSkillIndex, dwMotionIndex, 1, false))
		{
			Tracenf("CPythonPlayer::UseGuildSkill(%d) - pkInstMain->NEW_UseSkill - ERROR", dwSkillIndex);
		}
    
		CPythonNetworkStream.Instance().SendGuildUseSkillPacket(dwSkillIndex, 0);
		__RunCoolTime(dwSkillSlotIndex);
	}
	public bool AffectIndexToSkillSlotIndex(uint uAffect, ref uint pdwSkillSlotIndex)
	{
		uint dwSkillIndex = m_kMap_dwAffectIndexToSkillIndex[uAffect];
    
		return GetSkillSlotIndex(dwSkillIndex, pdwSkillSlotIndex);
	}
	public bool AffectIndexToSkillIndex(uint dwAffectIndex, ref uint pdwSkillIndex)
	{
		if (m_kMap_dwAffectIndexToSkillIndex.end() == m_kMap_dwAffectIndexToSkillIndex.find(dwAffectIndex))
		{
			return false;
		}
    
		pdwSkillIndex = m_kMap_dwAffectIndexToSkillIndex[dwAffectIndex];
		return true;
	}

	public void SetAffect(uint uAffect)
	{
		PyCallClassMemberFunc(m_ppyGameWindow, "SetAffect", Py_BuildValue("(i)", uAffect));
    
		uint dwSkillIndex;
		if (!AffectIndexToSkillIndex(uAffect, dwSkillIndex))
		{
			return;
		}
    
		SSkillData pSkillData;
		if (!CPythonSkill.Instance().GetSkillData(dwSkillIndex, pSkillData))
		{
			return;
		}
    
		if (!pSkillData.IsToggleSkill())
		{
			return;
		}
    
		uint dwSkillSlotIndex;
		if (!GetSkillSlotIndex(dwSkillIndex, dwSkillSlotIndex))
		{
			return;
		}
    
		__ActivateSkillSlot(dwSkillSlotIndex);
	}
	public void ResetAffect(uint uAffect)
	{
		PyCallClassMemberFunc(m_ppyGameWindow, "ResetAffect", Py_BuildValue("(i)", uAffect));
    
		uint dwSkillIndex;
		if (!AffectIndexToSkillIndex(uAffect, dwSkillIndex))
		{
			return;
		}
    
		SSkillData pSkillData;
		if (!CPythonSkill.Instance().GetSkillData(dwSkillIndex, pSkillData))
		{
			return;
		}
    
		if (!pSkillData.IsToggleSkill())
		{
			return;
		}
    
		uint dwSkillSlotIndex;
		if (!GetSkillSlotIndex(dwSkillIndex, dwSkillSlotIndex))
		{
			return;
		}
    
		__DeactivateSkillSlot(dwSkillSlotIndex);
	}
	public void ClearAffects()
	{
		PyCallClassMemberFunc(m_ppyGameWindow, "ClearAffects", Py_BuildValue("()"));
	}

	public void SetTarget(uint dwVID, bool bForceChange)
	{
		CInstanceBase pkInstMain = NEW_GetMainActorPtr();
		if (pkInstMain == null)
		{
			return;
		}
    
		if (!pkInstMain.CanChangeTarget())
		{
			return;
		}
    
		uint dwCurrentTime = CTimer.Instance().GetCurrentMillisecond();
    
		if (__IsSameTargetVID(dwVID))
		{
			if (dwVID == pkInstMain.GetVirtualID())
			{
				__SetTargetVID(0);
    
				pkInstMain.OnUntargeted();
				pkInstMain.ClearFlyTargetInstance();
				CPythonNetworkStream.Instance().SendTargetPacket(0);
				return;
			}
			m_dwTargetEndTime = dwCurrentTime + 1000;
			return;
		}
    
		if (bForceChange)
		{
			m_dwTargetEndTime = dwCurrentTime + 2000;
		}
		else
		{
			if (m_dwTargetEndTime > dwCurrentTime)
			{
				return;
			}
    
			m_dwTargetEndTime = dwCurrentTime + 1000;
		}
    
		if (__IsTarget())
		{
			CInstanceBase pTargetedInstance = __GetTargetActorPtr();
			if (pTargetedInstance != null)
			{
				pTargetedInstance.OnUntargeted();
			}
		}
    
    
		CInstanceBase pkInstTarget = CPythonCharacterManager.Instance().GetInstancePtr(dwVID);
		if (pkInstTarget != null)
		{
			if (pkInstMain.IsTargetableInstance(pkInstTarget))
			{
				__SetTargetVID(dwVID);
    
				pkInstTarget.OnTargeted();
				pkInstMain.SetFlyTargetInstance(pkInstTarget);
				pkInstMain.GetGraphicThingInstanceRef().SetFlyEventHandler(CPythonPlayerEventHandler.GetSingleton().GetNormalBowAttackFlyEventHandler(pkInstMain, pkInstTarget));
				CPythonNetworkStream.Instance().SendTargetPacket(dwVID);
    
				return;
			}
		}
    
		__SetTargetVID(0);
    
		pkInstMain.ClearFlyTargetInstance();
		CPythonNetworkStream.Instance().SendTargetPacket(0);
    
	}
	public void OpenCharacterMenu(uint dwVictimActorID)
	{
		CInstanceBase pkInstMain = CPythonPlayer.Instance().NEW_GetMainActorPtr();
		if (pkInstMain == null)
		{
			return;
		}
    
		CInstanceBase pkInstTarget = CPythonCharacterManager.Instance().GetInstancePtr(dwVictimActorID);
		if (pkInstTarget == null)
		{
			return;
		}
    
		if (!pkInstTarget.IsPC() && !pkInstTarget.IsBuilding())
		{
			return;
		}
    
		PyCallClassMemberFunc(m_ppyGameWindow, "SetPCTargetBoard", Py_BuildValue("(is)", pkInstTarget.GetVirtualID(), pkInstTarget.GetNameString()));
	}
	public uint GetTargetVID()
	{
		return __GetTargetVID();
	}

	public void ExitParty()
	{
		m_PartyMemberMap.clear();
    
		CPythonCharacterManager.Instance().RefreshAllPCTextTail();
	}
	public void AppendPartyMember(uint dwPID, string c_szName)
	{
		m_PartyMemberMap.insert(Tuple.Create(dwPID, TPartyMemberInfo(dwPID, c_szName)));
	}
	public void LinkPartyMember(uint dwPID, uint dwVID)
	{
		TPartyMemberInfo pPartyMemberInfo;
		if (!GetPartyMemberPtr(dwPID, pPartyMemberInfo))
		{
			TraceError(" CPythonPlayer::LinkPartyMember(dwPID=%d, dwVID=%d) - Failed to find party member", dwPID, dwVID);
			return;
		}
    
		pPartyMemberInfo.dwVID = dwVID;
    
		CInstanceBase pInstance = NEW_FindActorPtr(dwVID);
		if (pInstance != null)
		{
			pInstance.RefreshTextTail();
		}
	}
	public void UnlinkPartyMember(uint dwPID)
	{
		TPartyMemberInfo pPartyMemberInfo;
		if (!GetPartyMemberPtr(dwPID, pPartyMemberInfo))
		{
			TraceError(" CPythonPlayer::UnlinkPartyMember(dwPID=%d) - Failed to find party member", dwPID);
			return;
		}
    
		pPartyMemberInfo.dwVID = 0;
	}
	public void UpdatePartyMemberInfo(uint dwPID, byte byState, byte byHPPercentage)
	{
		TPartyMemberInfo pPartyMemberInfo;
		if (!GetPartyMemberPtr(dwPID, pPartyMemberInfo))
		{
			TraceError(" CPythonPlayer::UpdatePartyMemberInfo(dwPID=%d, byState=%d, byHPPercentage=%d) - Failed to find character", dwPID, byState, byHPPercentage);
			return;
		}
    
		pPartyMemberInfo.byState = byState;
		pPartyMemberInfo.byHPPercentage = byHPPercentage;
	}
	public void UpdatePartyMemberAffect(uint dwPID, byte byAffectSlotIndex, short sAffectNumber)
	{
		if (byAffectSlotIndex >= PARTY_AFFECT_SLOT_MAX_NUM)
		{
			TraceError(" CPythonPlayer::UpdatePartyMemberAffect(dwPID=%d, byAffectSlotIndex=%d, sAffectNumber=%d) - Strange affect slot index", dwPID, byAffectSlotIndex, sAffectNumber);
			return;
		}
    
		TPartyMemberInfo pPartyMemberInfo;
		if (!GetPartyMemberPtr(dwPID, pPartyMemberInfo))
		{
			TraceError(" CPythonPlayer::UpdatePartyMemberAffect(dwPID=%d, byAffectSlotIndex=%d, sAffectNumber=%d) - Failed to find character", dwPID, byAffectSlotIndex, sAffectNumber);
			return;
		}
    
		pPartyMemberInfo.sAffects[byAffectSlotIndex] = sAffectNumber;
	}
	public void RemovePartyMember(uint dwPID)
	{
		uint dwVID = 0;
		TPartyMemberInfo pPartyMemberInfo;
		if (GetPartyMemberPtr(dwPID, pPartyMemberInfo))
		{
			dwVID = pPartyMemberInfo.dwVID;
		}
    
		m_PartyMemberMap.erase(dwPID);
    
		if (dwVID > 0)
		{
			CInstanceBase pInstance = NEW_FindActorPtr(dwVID);
			if (pInstance != null)
			{
				pInstance.RefreshTextTail();
			}
		}
	}
	public bool IsPartyMemberByVID(uint dwVID)
	{
		SortedDictionary<uint, TPartyMemberInfo>.Enumerator itor = m_PartyMemberMap.begin();
		while (itor.MoveNext())
		{
			TPartyMemberInfo rPartyMemberInfo = itor.Current.Value;
			if (dwVID == rPartyMemberInfo.dwVID)
			{
				return true;
			}
		}
    
		return false;
	}
	public bool IsPartyMemberByName(string c_szName)
	{
		SortedDictionary<uint, TPartyMemberInfo>.Enumerator itor = m_PartyMemberMap.begin();
		while (itor.MoveNext())
		{
			TPartyMemberInfo rPartyMemberInfo = itor.Current.Value;
			if (0 == rPartyMemberInfo.strName.compare(c_szName))
			{
				return true;
			}
		}
    
		return false;
	}
	public bool GetPartyMemberPtr(uint dwPID, TPartyMemberInfo[] ppPartyMemberInfo)
	{
		SortedDictionary<uint, TPartyMemberInfo>.Enumerator itor = m_PartyMemberMap.find(dwPID);
    
		if (m_PartyMemberMap.end() == itor)
		{
			return false;
		}
    
	//# Laniatus Games Studio Inc. | TODO TASK: Iterators are only converted within the context of 'while' and 'for' loops:
		ppPartyMemberInfo[0] = &(itor.second);
    
		return true;
	}
	public bool PartyMemberPIDToVID(uint dwPID, ref uint pdwVID)
	{
		SortedDictionary<uint, TPartyMemberInfo>.Enumerator itor = m_PartyMemberMap.find(dwPID);
    
		if (m_PartyMemberMap.end() == itor)
		{
			return false;
		}
    
	//# Laniatus Games Studio Inc. | TODO TASK: Iterators are only converted within the context of 'while' and 'for' loops:
		TPartyMemberInfo c_rPartyMemberInfo = itor.second;
		pdwVID = c_rPartyMemberInfo.dwVID;
    
		return true;
	}
	public bool PartyMemberVIDToPID(uint dwVID, ref uint pdwPID)
	{
		SortedDictionary<uint, TPartyMemberInfo>.Enumerator itor = m_PartyMemberMap.begin();
		while (itor.MoveNext())
		{
			TPartyMemberInfo rPartyMemberInfo = itor.Current.Value;
			if (dwVID == rPartyMemberInfo.dwVID)
			{
				pdwPID = rPartyMemberInfo.dwPID;
				return true;
			}
		}
    
		return false;
	}
	public bool IsSamePartyMember(uint dwVID1, uint dwVID2)
	{
		return (IsPartyMemberByVID(dwVID1) && IsPartyMemberByVID(dwVID2));
	}

	public void RememberChallengeInstance(uint dwVID)
	{
		m_RevengeInstanceSet.erase(dwVID);
		m_ChallengeInstanceSet.insert(dwVID);
	}
	public void RememberRevengeInstance(uint dwVID)
	{
		m_ChallengeInstanceSet.erase(dwVID);
		m_RevengeInstanceSet.insert(dwVID);
	}
	public void RememberCantFightInstance(uint dwVID)
	{
		m_CantFightInstanceSet.insert(dwVID);
	}
	public void ForgetInstance(uint dwVID)
	{
		m_ChallengeInstanceSet.erase(dwVID);
		m_RevengeInstanceSet.erase(dwVID);
		m_CantFightInstanceSet.erase(dwVID);
	}
	public bool IsChallengeInstance(uint dwVID)
	{
		return m_ChallengeInstanceSet.end() != m_ChallengeInstanceSet.find(dwVID);
	}
	public bool IsRevengeInstance(uint dwVID)
	{
		return m_RevengeInstanceSet.end() != m_RevengeInstanceSet.find(dwVID);
	}
	public bool IsCantFightInstance(uint dwVID)
	{
		return m_CantFightInstanceSet.end() != m_CantFightInstanceSet.find(dwVID);
	}

	public void OpenPrivateShop()
	{
		m_isOpenPrivateShop = true;
	}
	public void ClosePrivateShop()
	{
		m_isOpenPrivateShop = false;
	}
	public bool IsOpenPrivateShop()
	{
		return m_isOpenPrivateShop;
	}

	public void StartStaminaConsume(uint dwConsumePerSec, uint dwCurrentStamina)
	{
		m_isConsumingStamina = true;
		m_fConsumeStaminaPerSec = (float)dwConsumePerSec;
		m_fCurrentStamina = (float)dwCurrentStamina;
    
		SetStatus(POINT_STAMINA, dwCurrentStamina);
	}
	public void StopStaminaConsume(uint dwCurrentStamina)
	{
		m_isConsumingStamina = false;
		m_fConsumeStaminaPerSec = 0.0f;
		m_fCurrentStamina = (float)dwCurrentStamina;
    
		SetStatus(POINT_STAMINA, dwCurrentStamina);
	}

	public uint GetPKMode()
	{
		CInstanceBase pInstance = NEW_GetMainActorPtr();
		if (pInstance == null)
		{
			return 0;
		}
    
		return pInstance.GetPKMode();
	}

	public void SetComboSkillFlag(bool bFlag)
	{
		uint dwSlotIndex;
		if (!GetSkillSlotIndex(c_iSkillIndex_Combo, dwSlotIndex))
		{
			Tracef("CPythonPlayer::SetComboSkillFlag(killIndex=%d) - Can't Find Slot Index\n", c_iSkillIndex_Combo);
			return;
		}
    
		int iLevel = GetSkillLevel(dwSlotIndex);
		if (iLevel <= 0)
		{
			Tracef("CPythonPlayer::SetComboSkillFlag(skillIndex=%d, skillLevel=%d) - Invalid Combo Skill Level\n", c_iSkillIndex_Combo, iLevel);
			return;
		}
    
		iLevel = MIN(iLevel, 2);
    
		CInstanceBase pkInstMain = NEW_GetMainActorPtr();
		if (pkInstMain == null)
		{
			return;
		}
    
		if (bFlag)
		{
			pkInstMain.SetComboType(iLevel);
			__ActivateSkillSlot(dwSlotIndex);
		}
		else
		{
			pkInstMain.SetComboType(0);
			__DeactivateSkillSlot(dwSlotIndex);
		}
	}

	public void SetMovableGroundDistance(float fDistance)
	{
		MOVABLE_GROUND_DISTANCE = fDistance;
	}

	public void ActEmotion(uint dwEmotionID)
	{
		CInstanceBase pkInstTarget = __GetAliveTargetInstancePtr();
		if (pkInstTarget == null)
		{
			PyCallClassMemberFunc(m_ppyGameWindow, "OnCannotShotError", Py_BuildValue("(is)", GetMainCharacterIndex(), "NEED_TARGET"));
			return;
		}
    
		CPythonNetworkStream.Instance().SendChatPacket(_getf("/kiss %s", pkInstTarget.GetNameString()));
	}
	public void StartEmotionProcess()
	{
		__ClearReservedAction();
		__ClearAutoAttackTargetActorID();
    
		m_bisProcessingEmotion = true;
	}
	public void EndEmotionProcess()
	{
		m_bisProcessingEmotion = false;
	}

	public bool __ToggleCoolTime()
	{
		m_sysIsCoolTime = 1 - m_sysIsCoolTime;
		return m_sysIsCoolTime;
	}
	public bool __ToggleLevelLimit()
	{
		m_sysIsLevelLimit = 1 - m_sysIsLevelLimit;
		return m_sysIsLevelLimit;
	}

//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: inline const SAutoPotionInfo& GetAutoPotionInfo(int type) const
		public SAutoPotionInfo GetAutoPotionInfo(int type)
		{
//# Laniatus Games Studio Inc. | TODO TASK: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
//Original Metin2 CPlus Line: return m_kAutoPotionInfo[type];
			return new CPythonPlayer.SAutoPotionInfo(m_kAutoPotionInfo[type]);
		}
		public SAutoPotionInfo GetAutoPotionInfo(int type)
		{
//# Laniatus Games Studio Inc. | TODO TASK: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
//Original Metin2 CPlus Line: return m_kAutoPotionInfo[type];
			return new CPythonPlayer.SAutoPotionInfo(m_kAutoPotionInfo[type]);
		}
		public void SetAutoPotionInfo(int type, in SAutoPotionInfo info)
		{
//# Laniatus Games Studio Inc. | TODO TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'CopyFrom' method should be created:
//Original Metin2 CPlus Line: m_kAutoPotionInfo[type] = info;
			m_kAutoPotionInfo[type].CopyFrom(info);
		}

	public TQuickSlot __RefLocalQuickSlot(int SlotIndex)
	{
		return __RefGlobalQuickSlot(LocalQuickSlotIndexToGlobalQuickSlotIndex(SlotIndex));
	}
	public TQuickSlot __RefGlobalQuickSlot(int SlotIndex)
	{
		if (SlotIndex < 0 || SlotIndex >= QUICKSLOT_MAX_NUM)
		{
	//# Laniatus Games Studio Inc. |: This static local variable declaration (not allowed in C#) has been moved just prior to the method:
	//		static TQuickSlot s_kQuickSlot;
			__RefGlobalQuickSlot_s_kQuickSlot.Type = 0;
			__RefGlobalQuickSlot_s_kQuickSlot.Position = 0;
			return __RefGlobalQuickSlot_s_kQuickSlot;
		}
    
		return m_playerStatus.aQuickSlot[SlotIndex];
	}


	public uint __GetLevelAtk()
	{
		return 2 * GetStatus(POINT_LEVEL);
	}
	public uint __GetStatAtk()
	{
		return (4 * GetStatus(POINT_ST) + 2 * __GetRaceStat()) / 3;
	}
	public uint __GetWeaponAtk(uint dwWeaponPower)
	{
		return (uint)(2 * dwWeaponPower);
	}
	public uint __GetTotalAtk(uint dwWeaponPower, uint dwRefineBonus)
	{
		uint dwLvAtk = __GetLevelAtk();
		uint dwStAtk = __GetStatAtk();
    
		uint dwWepAtk;
		uint dwTotalAtk;
    
		int hr = __GetHitRate();
		dwWepAtk = __GetWeaponAtk(dwWeaponPower + dwRefineBonus);
		dwTotalAtk = dwLvAtk + (dwStAtk + dwWepAtk) * hr / 100;
    
		return dwTotalAtk;
	}
	public uint __GetRaceStat()
	{
		switch (GetRace())
		{
		case NPlayerData.MAIN_RACE_WARRIOR_M:
		case NPlayerData.MAIN_RACE_WARRIOR_W:
			return GetStatus(POINT_ST);
			break;
		case NPlayerData.MAIN_RACE_ASSASSIN_M:
		case NPlayerData.MAIN_RACE_ASSASSIN_W:
			return GetStatus(POINT_DX);
			break;
		case NPlayerData.MAIN_RACE_SURA_M:
		case NPlayerData.MAIN_RACE_SURA_W:
			return GetStatus(POINT_ST);
			break;
		case NPlayerData.MAIN_RACE_SHAMAN_M:
		case NPlayerData.MAIN_RACE_SHAMAN_W:
			return GetStatus(POINT_IQ);
			break;
	#if ENABLE_WOLFMAN
	//# Laniatus Games Studio Inc. | TODO TASK: C# does not allow fall-through from a non-empty 'case':
		case NPlayerData.MAIN_RACE_WOLFMAN_M:
			return GetStatus(POINT_DX);
			break;
	#endif
	break;
		}
		return GetStatus(POINT_ST);
	}
	public uint __GetHitRate()
	{
		int src = 0;
		src = (GetStatus(POINT_DX) * 4 + GetStatus(POINT_LEVEL) * 2) / 6;
    
		return (uint)(100 * (Math.Min(90, src) + 210) / 300);
	}
	public uint __GetEvadeRate()
	{
		return 30 * (2 * GetStatus(POINT_DX) + 5) / (GetStatus(POINT_DX) + 95);
	}

	public void __UpdateBattleStatus()
	{
		m_playerStatus.SetPoint(POINT_NONE, 0);
		m_playerStatus.SetPoint(POINT_EVADE_RATE, __GetEvadeRate());
		m_playerStatus.SetPoint(POINT_HIT_RATE, __GetHitRate());
		m_playerStatus.SetPoint(POINT_MIN_WEP, m_dwWeaponMinPower + m_dwWeaponAddPower);
		m_playerStatus.SetPoint(POINT_MAX_WEP, m_dwWeaponMaxPower + m_dwWeaponAddPower);
		m_playerStatus.SetPoint(POINT_MIN_MAGIC_WEP, m_dwWeaponMinMagicPower + m_dwWeaponAddPower);
		m_playerStatus.SetPoint(POINT_MAX_MAGIC_WEP, m_dwWeaponMaxMagicPower + m_dwWeaponAddPower);
		m_playerStatus.SetPoint(POINT_MIN_ATK, __GetTotalAtk(m_dwWeaponMinPower, m_dwWeaponAddPower));
		m_playerStatus.SetPoint(POINT_MAX_ATK, __GetTotalAtk(m_dwWeaponMaxPower, m_dwWeaponAddPower));
	}

	public void __DeactivateSkillSlot(uint dwSlotIndex)
	{
		if (dwSlotIndex >= SKILL_MAX_NUM)
		{
			Tracenf("CPythonPlayer::DeactivavteSkill(dwSlotIndex=%d/%d) - OUT OF RANGE", dwSlotIndex, SKILL_MAX_NUM);
			return;
		}
    
		m_playerStatus.aSkill[dwSlotIndex].bActive = false;
		PyCallClassMemberFunc(m_ppyGameWindow, "DeactivateSkillSlot", Py_BuildValue("(i)", dwSlotIndex));
	}
	public void __ActivateSkillSlot(uint dwSlotIndex)
	{
		if (dwSlotIndex >= SKILL_MAX_NUM)
		{
			Tracenf("CPythonPlayer::ActivavteSkill(dwSlotIndex=%d/%d) - OUT OF RANGE", dwSlotIndex, SKILL_MAX_NUM);
			return;
		}
    
		m_playerStatus.aSkill[dwSlotIndex].bActive = true;
		PyCallClassMemberFunc(m_ppyGameWindow, "ActivateSkillSlot", Py_BuildValue("(i)", dwSlotIndex));
	}

	public void __OnPressSmart(CInstanceBase rkInstMain, bool isAuto)
	{
		uint dwPickedItemID;
		uint dwPickedActorID;
		TPixelPosition kPPosPickedGround = new TPixelPosition();
    
		bool isPickedItemID = __GetPickedItemID(dwPickedItemID);
		bool isPickedActorID = __GetPickedActorID(dwPickedActorID);
		bool isPickedGroundPos = __GetPickedGroundPos(kPPosPickedGround);
    
		if (isPickedItemID)
		{
			__OnPressItem(rkInstMain, dwPickedItemID);
		}
		else if (isPickedActorID && dwPickedActorID != GetMainCharacterIndex())
		{
			__OnPressActor(rkInstMain, dwPickedActorID, isAuto);
		}
		else if (isPickedGroundPos)
		{
			__OnPressGround(rkInstMain, kPPosPickedGround);
		}
		else
		{
			__OnPressScreen(rkInstMain);
		}
	}
	public void __OnClickSmart(CInstanceBase rkInstMain, bool isAuto)
	{
		uint dwPickedItemID;
		uint dwPickedActorID;
		TPixelPosition kPPosPickedGround = new TPixelPosition();
		if (__GetPickedItemID(dwPickedItemID))
		{
			__OnClickItem(rkInstMain, dwPickedItemID);
		}
		else if (__GetPickedActorID(dwPickedActorID))
		{
			__OnClickActor(rkInstMain, dwPickedActorID, isAuto);
		}
		else if (__GetPickedGroundPos(kPPosPickedGround))
		{
			__OnClickGround(rkInstMain, kPPosPickedGround);
		}
		else
		{
			rkInstMain.NEW_Stop();
		}
	}

	public void __OnPressItem(CInstanceBase rkInstMain, uint dwPickedItemID)
	{
	//# Laniatus Games Studio Inc. |: This static local variable declaration (not allowed in C#) has been moved just prior to the method:
	//	static uint s_dwLastPickItemID=0;
    
		if (__OnPressItem_s_dwLastPickItemID == dwPickedItemID)
		{
			Logn(1, "CPythonPlayer::__OnPressItem - ALREADY PICKED ITEM");
			return;
		}
    
		__ClearReservedAction();
		__ClearAutoAttackTargetActorID();
    
		CPythonItem rkItem = CPythonItem.Instance();
    
		TPixelPosition kPPosPickedItem = new TPixelPosition();
		if (!rkItem.GetGroundItemPosition(dwPickedItemID, kPPosPickedItem))
		{
			return;
		}
    
		if (!rkInstMain.NEW_IsClickableDistanceDestPixelPosition(kPPosPickedItem))
		{
			__ReserveClickItem(dwPickedItemID);
			return;
		}
    
		rkInstMain.NEW_Stop();
		SendClickItemPacket(dwPickedItemID);
	}
	public void __OnPressActor(CInstanceBase rkInstMain, uint dwPickedActorID, bool isAuto)
	{
		if (MODE_USE_SKILL == m_eReservedMode)
		{
			if (__GetTargetVID() == dwPickedActorID)
			{
				return;
			}
    
			if (__CheckDashAffect(rkInstMain))
			{
				m_dwVIDReserved = dwPickedActorID;
				return;
			}
		}
    
		__ChangeTargetToPickedInstance();
		__ClearReservedAction();
    
		if (!__CanAttack())
		{
			return;
		}
    
		CInstanceBase pkInstVictim = NEW_FindActorPtr(dwPickedActorID);
		if (pkInstVictim == null)
		{
			return;
		}
    
	//# Laniatus Games Studio Inc. | TODO TASK: C# does not have an equivalent to references to variables:
	//Original Metin2 CPlus Line: CInstanceBase& rkInstVictim=*pkInstVictim;
		CInstanceBase rkInstVictim = pkInstVictim;
    
		if (isAuto)
		{
			if (rkInstMain.IsAttackableInstance(rkInstVictim))
			{
				__SetAutoAttackTargetActorID(rkInstVictim.GetVirtualID());
			}
		}
    
		if (rkInstMain.IsBowMode())
		{
			if (rkInstMain.IsAttackableInstance(rkInstVictim))
			{
				if (!__CanShot(rkInstMain, rkInstVictim))
				{
					return;
				}
			}
		}
    
		if (!rkInstMain.NEW_IsClickableDistanceDestInstance(rkInstVictim))
		{
			__ReserveClickActor(dwPickedActorID);
			return;
		}
    
		if (!rkInstMain.IsAttackableInstance(rkInstVictim))
		{
			return;
		}
    
		CPythonPlayerEventHandler rkPlayerEventHandler = CPythonPlayerEventHandler.GetSingleton();
		rkInstMain.NEW_AttackToDestInstanceDirection(rkInstVictim, rkPlayerEventHandler.GetNormalBowAttackFlyEventHandler(rkInstMain, rkInstVictim));
	}
	public void __OnPressGround(CInstanceBase rkInstMain, in TPixelPosition c_rkPPosPickedGround)
	{
		__ClearReservedAction();
		__ClearAutoAttackTargetActorID();
    
		if (NEW_CancelFishing())
		{
			return;
		}
    
		if (!__IsMovableGroundDistance(rkInstMain, c_rkPPosPickedGround))
		{
			return;
		}
    
		if (!rkInstMain.NEW_MoveToDestPixelPositionDirection(c_rkPPosPickedGround))
		{
			__ReserveClickGround(c_rkPPosPickedGround);
			return;
		}
	}
	public void __OnPressScreen(CInstanceBase rkInstMain)
	{
		__ClearReservedAction();
    
		NEW_MoveToMouseScreenDirection();
	}

	public void __OnClickActor(CInstanceBase rkInstMain, uint dwPickedActorID, bool isAuto)
	{
		if (MODE_USE_SKILL == m_eReservedMode)
		{
			if (__GetTargetVID() == dwPickedActorID)
			{
				return;
			}
    
			if (__CheckDashAffect(rkInstMain))
			{
				m_dwVIDReserved = dwPickedActorID;
				return;
			}
		}
    
		__ClearReservedAction();
    
		CInstanceBase pkInstVictim = NEW_FindActorPtr(dwPickedActorID);
	//# Laniatus Games Studio Inc. | TODO TASK: C# does not have an equivalent to references to variables:
	//Original Metin2 CPlus Line: CInstanceBase& rkInstVictim=*pkInstVictim;
		CInstanceBase rkInstVictim = pkInstVictim;
		if (pkInstVictim == null)
		{
			return;
		}
    
		if (rkInstMain.IsAttackableInstance(pkInstVictim))
		{
			if (!__CanAttack())
			{
				return;
			}
		}
    
		if (!rkInstMain.NEW_IsClickableDistanceDestInstance(rkInstVictim))
		{
			__ReserveClickActor(dwPickedActorID);
			return;
		}
    
		if (rkInstVictim.IsNPC())
		{
			__SendClickActorPacket(rkInstVictim);
		}
    
		rkInstMain.NEW_Stop();
		return;
	}
	public void __OnClickItem(CInstanceBase rkInstMain, uint dwItemID)
	{
	}
	public void __OnClickGround(CInstanceBase rkInstMain, in TPixelPosition c_rkPPosPickedGround)
	{
		if (!__IsMovableGroundDistance(rkInstMain, c_rkPPosPickedGround))
		{
			return;
		}
    
		if (rkInstMain.NEW_MoveToDestPixelPositionDirection(c_rkPPosPickedGround))
		{
			__ShowPickedEffect(c_rkPPosPickedGround);
		}
	}

	public bool __IsMovableGroundDistance(CInstanceBase rkInstMain, in TPixelPosition c_rkPPosPickedGround)
	{
		float fDistance = rkInstMain.NEW_GetDistanceFromDestPixelPosition(c_rkPPosPickedGround);
    
		if (fDistance < MOVABLE_GROUND_DISTANCE)
		{
			return false;
		}
    
		return true;
	}

	public bool __GetPickedActorPtr(CInstanceBase[] ppkInstPicked)
	{
		CPythonCharacterManager rkChrMgr = CPythonCharacterManager.Instance();
		CInstanceBase pkInstPicked = rkChrMgr.OLD_GetPickedInstancePtr();
		if (pkInstPicked == null)
		{
			return false;
		}
    
	//# Laniatus Games Studio Inc. | TODO TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'CopyFrom' method should be created:
	//Original Metin2 CPlus Line: *ppkInstPicked=pkInstPicked;
		ppkInstPicked[0].CopyFrom(pkInstPicked);
		return true;
	}

	public bool __GetPickedActorID(ref uint pdwActorID)
	{
		CPythonCharacterManager rkChrMgr = CPythonCharacterManager.Instance();
		return rkChrMgr.OLD_GetPickedInstanceVID(pdwActorID);
	}
	public bool __GetPickedItemID(ref uint pdwItemID)
	{
		CPythonItem rkItemMgr = CPythonItem.Instance();
		return rkItemMgr.GetPickedItemID(pdwItemID);
	}
	public bool __GetPickedGroundPos(TPixelPosition pkPPosPicked)
	{
		CPythonBackground rkBG = CPythonBackground.Instance();
    
		TPixelPosition kPPosPicked = new TPixelPosition();
		if (rkBG.GetPickingPoint(pkPPosPicked))
		{
			pkPPosPicked.y = -pkPPosPicked.y;
			return true;
		}
    
		return false;
	}

	public void __ClearReservedAction()
	{
		m_eReservedMode = MODE_NONE;
	}
	public void __ReserveClickItem(uint dwItemID)
	{
		m_eReservedMode = MODE_CLICK_ITEM;
		m_dwIIDReserved = dwItemID;
	}
	public void __ReserveClickActor(uint dwActorID)
	{
		m_eReservedMode = MODE_CLICK_ACTOR;
		m_dwVIDReserved = dwActorID;
	}
	public void __ReserveClickGround(in TPixelPosition c_rkPPosPickedGround)
	{
		m_eReservedMode = MODE_CLICK_POSITION;
		m_kPPosReserved = c_rkPPosPickedGround;
		m_fReservedDelayTime = 0.1f;
	}
	public void __ReserveUseSkill(uint dwActorID, uint dwSkillSlotIndex, uint dwRange)
	{
		m_eReservedMode = MODE_USE_SKILL;
		m_dwVIDReserved = dwActorID;
		m_dwSkillSlotIndexReserved = dwSkillSlotIndex;
		m_dwSkillRangeReserved = dwRange;
    
		if (m_dwSkillRangeReserved > 100)
		{
			m_dwSkillRangeReserved -= 10;
		}
	}

	public void __ReserveProcess_ClickActor()
	{
		CInstanceBase pkInstMain = NEW_GetMainActorPtr();
		CInstanceBase pkInstReserved = NEW_FindActorPtr(m_dwVIDReserved);
		if (pkInstMain == null || pkInstReserved == null)
		{
			__ClearReservedAction();
			return;
		}
    
		if (!pkInstMain.NEW_IsClickableDistanceDestInstance(pkInstReserved))
		{
			pkInstMain.NEW_MoveToDestInstanceDirection(pkInstReserved);
			return;
		}
    
		if (!pkInstMain.IsAttackableInstance(pkInstReserved))
		{
			pkInstMain.NEW_Stop();
			__SendClickActorPacket(pkInstReserved);
			__ClearReservedAction();
			return;
		}
    
		if (pkInstReserved.IsDead())
		{
			__ClearReservedAction();
			return;
		}
    
		if (pkInstMain.IsInSafe())
		{
			PyCallClassMemberFunc(m_ppyGameWindow, "OnCannotAttack", Py_BuildValue("(is)", GetMainCharacterIndex(), "IN_SAFE"));
			pkInstMain.NEW_Stop();
			__ClearReservedAction();
			return;
		}
    
		if (pkInstReserved.IsInSafe())
		{
			PyCallClassMemberFunc(m_ppyGameWindow, "OnCannotAttack", Py_BuildValue("(is)", GetMainCharacterIndex(), "DEST_IN_SAFE"));
			pkInstMain.NEW_Stop();
			__ClearReservedAction();
			return;
		}
    
		if (__CheckDashAffect(pkInstMain))
		{
			return;
		}
    
		if (pkInstMain.IsBowMode())
		{
			if (!__HasEnoughArrow())
			{
				PyCallClassMemberFunc(m_ppyGameWindow, "OnCannotShot", Py_BuildValue("(is)", GetMainCharacterIndex(), "EMPTY_ARROW"));
				pkInstMain.NEW_Stop();
				__ClearReservedAction();
				return;
			}
		}
    
		if (pkInstReserved.GetVirtualID() != GetTargetVID())
		{
			SetTarget(pkInstReserved.GetVirtualID());
		}
    
		pkInstMain.NEW_AttackToDestInstanceDirection(pkInstReserved);
		__ClearReservedAction();
	}

	public void __ShowPickedEffect(in TPixelPosition c_rkPPosPickedGround)
	{
		NEW_ShowEffect(EFFECT_PICK, c_rkPPosPickedGround);
	}
	public void __SendClickActorPacket(CInstanceBase rkInstVictim)
	{
		CInstanceBase pkInstMain = NEW_GetMainActorPtr();
		if (pkInstMain != null)
		{
		if (pkInstMain.IsHoldingPickAxe())
		{
		if (pkInstMain.IsMountingHorse())
		{
		if (rkInstVictim.IsResource())
		{
			PyCallClassMemberFunc(m_ppyGameWindow, "OnCannotMining", Py_BuildValue("()"));
			return;
		}
		}
		}
		}
    
	//# Laniatus Games Studio Inc. |: This static local variable declaration (not allowed in C#) has been moved just prior to the method:
	//	static uint s_dwNextTCPTime = 0;
    
		uint dwCurTime = ELTimer_GetMSec();
    
		if (dwCurTime >= __SendClickActorPacket_s_dwNextTCPTime)
		{
			__SendClickActorPacket_s_dwNextTCPTime = dwCurTime+1000;
    
			CPythonNetworkStream rkNetStream = CPythonNetworkStream.Instance();
    
			uint dwVictimVID = rkInstVictim.GetVirtualID();
			rkNetStream.SendOnClickPacket(dwVictimVID);
		}
	}

	public void __ClearAutoAttackTargetActorID()
	{
		__SetAutoAttackTargetActorID(0);
	}
	public void __SetAutoAttackTargetActorID(uint dwVID)
	{
		 m_dwAutoAttackTargetVID = dwVID;
	}

	public void NEW_ShowEffect(int dwEID, TPixelPosition kPPosDst)
	{
		if (dwEID >= EFFECT_NUM)
		{
			return;
		}
    
		_D3DVECTOR kD3DVt3Pos = new _D3DVECTOR(kPPosDst.x, -kPPosDst.y, kPPosDst.z);
		_D3DVECTOR kD3DVt3Dir = new _D3DVECTOR(0.0f, 0.0f, 1.0f);
    
		CEffectManager rkEftMgr = CEffectManager.Instance();
		rkEftMgr.CreateEffect(m_adwEffect[dwEID], kD3DVt3Pos, kD3DVt3Dir);
	}

	public void NEW_SetMouseSmartState(int eMBS, bool isAuto)
	{
		CInstanceBase pkInstMain = NEW_GetMainActorPtr();
		if (pkInstMain == null)
		{
			return;
		}
    
		if (IsOpenPrivateShop())
		{
			m_isSmtMov = false;
			return;
		}
    
		if (__IsProcessingEmotion())
		{
			return;
		}
    
		if (pkInstMain.IsSleep())
		{
			return;
		}
    
		if (MBS_PRESS == eMBS)
		{
			m_isSmtMov = true;
    
			__OnPressSmart(pkInstMain, isAuto);
		}
		else if (MBS_CLICK == eMBS)
		{
			m_isSmtMov = false;
    
			__OnClickSmart(pkInstMain, isAuto);
		}
	}
	public void NEW_SetMouseMoveState(int eMBS)
	{
		if (MBS_PRESS == eMBS)
		{
			NEW_MoveToMouseScreenDirection();
    
			m_isDirMov = true;
		}
		else if (MBS_CLICK == eMBS)
		{
			NEW_Stop();
    
			m_isDirMov = false;
		}
	}
	public void NEW_SetMouseCameraState(int eMBS)
	{
		CPythonApplication rkApp = CPythonApplication.Instance();
		CPythonBackground rkBG = CPythonBackground.Instance();
		CCamera pkCmrCur = CCameraManager.Instance().GetCurrentCamera();
    
		if (pkCmrCur != null)
		{
			if (MBS_PRESS == eMBS)
			{
				UI.CWindowManager rkWndMgr = UI.CWindowManager.Instance();
    
				int lMouseX;
				int lMouseY;
				rkWndMgr.GetMousePosition(lMouseX, lMouseY);
    
				pkCmrCur.BeginDrag(lMouseX, lMouseY);
    
				if (!rkBG.IsMapReady())
				{
					return;
				}
    
				rkApp.SetCursorNum(CPythonApplication.CAMERA_ROTATE);
				if (CPythonApplication.CURSOR_MODE_HARDWARE == rkApp.GetCursorMode())
				{
					rkApp.SetCursorVisible(false, true);
				}
    
			}
			else if (MBS_CLICK == eMBS)
			{
				bool isCameraDrag = pkCmrCur.EndDrag();
    
				if (!rkBG.IsMapReady())
				{
					return;
				}
    
				rkApp.SetCursorNum(CPythonApplication.NORMAL);
				if (CPythonApplication.CURSOR_MODE_HARDWARE == rkApp.GetCursorMode())
				{
					rkApp.SetCursorVisible(true);
				}
    
				if (!isCameraDrag)
				{
					__ChangeTargetToPickedInstance();
    
					CInstanceBase pkInstPicked;
					if (__GetPickedActorPtr(pkInstPicked))
					{
						OpenCharacterMenu(pkInstPicked.GetVirtualID());
					}
				}
			}
		}
	}
	public void NEW_GetMouseDirRotation(float fScrX, float fScrY, ref float pfDirRot)
	{
		int lWidth = UI.CWindowManager.Instance().GetScreenWidth();
		int lHeight = UI.CWindowManager.Instance().GetScreenHeight();
		int nScrPosX = (int)(lWidth * fScrX);
		int nScrPosY = (int)(lHeight * fScrY);
		int nScrWidth = lWidth;
		int nScrHeight = lHeight;
		int nScrCenterX = nScrWidth / 2;
		int nScrCenterY = nScrHeight / 2;
    
		float finputRotation = GetDegreeFromPosition(nScrPosX, nScrPosY, nScrCenterX, nScrCenterY);
		pfDirRot = finputRotation;
	}
	public void NEW_GetMultiKeyDirRotation(bool isLeft, bool isRight, bool isUp, bool isDown, ref float pfDirRot)
	{
		float fScrX = 0.0f;
		float fScrY = 0.0f;
    
		if (isLeft)
		{
			fScrX = 0.0f;
		}
		else if (isRight)
		{
			fScrX = 1.0f;
		}
		else
		{
			fScrX = 0.5f;
		}
    
		if (isUp)
		{
			fScrY = 0.0f;
		}
		else if (isDown)
		{
			fScrY = 1.0f;
		}
		else
		{
			fScrY = 0.5f;
		}
    
		NEW_GetMouseDirRotation(fScrX, fScrY, pfDirRot);
	}

	public float GetDegreeFromDirection(int iUD, int iLR)
	{
		switch (iUD)
		{
			case KEYBOARD_UD_UP:
				if (KEYBOARD_LR_LEFT == iLR)
				{
					return +45.0f;
				}
				else if (KEYBOARD_LR_RIGHT == iLR)
				{
					return -45.0f;
				}
    
				return 0.0f;
				break;
    
			case KEYBOARD_UD_DOWN:
				if (KEYBOARD_LR_LEFT == iLR)
				{
					return +135.0f;
				}
				else if (KEYBOARD_LR_RIGHT == iLR)
				{
					return -135.0f;
				}
    
				return +180.0f;
				break;
    
			case KEYBOARD_UD_NONE:
				if (KEYBOARD_LR_LEFT == iLR)
				{
					return +90.0f;
				}
				else if (KEYBOARD_LR_RIGHT == iLR)
				{
					return -90.0f;
				}
				break;
		}
    
		return 0.0f;
	}
	public float GetDegreeFromPosition(int ix, int iy, int iHalfWidth, int iHalfHeight)
	{
		_D3DVECTOR vtDir = new _D3DVECTOR((float)(ix - iHalfWidth), (float)(iy - iHalfHeight), 0.0f);
		D3DXVec3Normalize(vtDir, vtDir);
    
		_D3DVECTOR vtStan = new _D3DVECTOR(0, -1, 0);
		float ret = ((acosf(D3DXVec3Dot(vtDir, vtStan))) * (180.0f / ((float) 3.141592654f)));
    
		if (vtDir.x < 0.0f)
		{
			ret = 360.0f - ret;
		}
    
		return 360.0f - ret;
	}

//# Laniatus Games Studio Inc. | TODO TASK: The implementation of the following method could not be found:
//		bool CheckCategory(int iCategory);
//# Laniatus Games Studio Inc. | TODO TASK: The implementation of the following method could not be found:
//		bool CheckAbilitySlot(int iSlotIndex);

//# Laniatus Games Studio Inc. | TODO TASK: The implementation of the following method could not be found:
//		void RefreshKeyWalkingDirection();
	public void NEW_RefreshMouseWalkingDirection()
	{
		CInstanceBase pkInstMain = NEW_GetMainActorPtr();
		if (pkInstMain == null)
		{
			return;
		}
    
		switch (m_eReservedMode)
		{
			case MODE_CLICK_ITEM:
			{
				CPythonItem rkIT = CPythonItem.Instance();
    
				TPixelPosition kPPosPickedItem = new TPixelPosition();
				if (rkIT.GetGroundItemPosition(m_dwIIDReserved, kPPosPickedItem))
				{
					if (pkInstMain.NEW_GetDistanceFromDestPixelPosition(kPPosPickedItem) < 20.0f)
					{
						CPythonNetworkStream rkNetStream = CPythonNetworkStream.Instance();
    
						TPixelPosition kPPosCur = new TPixelPosition();
						pkInstMain.NEW_GetPixelPosition(kPPosCur);
    
						float fCurRot = pkInstMain.GetRotation();
						rkNetStream.SendCharacterStatePacket(kPPosCur, fCurRot, CInstanceBase.FUNC_WAIT, 0);
						SendClickItemPacket(m_dwIIDReserved);
    
						pkInstMain.NEW_Stop();
    
						__ClearReservedAction();
					}
					else
					{
						pkInstMain.NEW_MoveToDestPixelPositionDirection(kPPosPickedItem);
					}
				}
				else
				{
					__ClearReservedAction();
				}
    
				break;
			}
    
			case MODE_CLICK_ACTOR:
			{
				__ReserveProcess_ClickActor();
				break;
			}
    
			case MODE_CLICK_POSITION:
			{
				if (!pkInstMain.isLock())
				{
				if (NEW_IsEmptyReservedDelayTime(CPythonApplication.Instance().GetGlobalElapsedTime()))
				{
					pkInstMain.NEW_MoveToDestPixelPositionDirection(m_kPPosReserved);
					__ClearReservedAction();
				}
				}
				break;
			}
    
			case MODE_USE_SKILL:
			{
				CInstanceBase pkInstReserved = NEW_FindActorPtr(m_dwVIDReserved);
				if (pkInstReserved != null)
				{
					float fDistance = pkInstMain.GetDistance(pkInstReserved);
    
	//# Laniatus Games Studio Inc. |: 'extern' variable declarations are not required in C#:
	//				extern bool IS_HUGE_RACE(uint vnum);
					if (IS_HUGE_RACE(pkInstReserved.GetRace()))
					{
						fDistance -= 200.0f;
					}
    
					if (fDistance < (float)m_dwSkillRangeReserved)
					{
						SetTarget(m_dwVIDReserved);
						if (__UseSkill(m_dwSkillSlotIndexReserved))
						{
							__ClearReservedAction();
						}
					}
					else
					{
						pkInstMain.NEW_MoveToDestInstanceDirection(pkInstReserved);
					}
				}
				else
				{
					__ClearReservedAction();
				}
				break;
			}
		}
    
		if (m_isSmtMov)
		{
			__OnPressSmart(pkInstMain, false);
		}
    
		if (m_isDirMov)
		{
			NEW_MoveToMouseScreenDirection();
		}
    
		if (m_isDirKey)
		{
			NEW_SetMultiDirKeyState(m_isLeft, m_isRight, m_isUp, m_isDown);
		}
    
		if (m_isAtkKey)
		{
			NEW_Attack();
		}
    
		m_iComboOld = pkInstMain.GetComboIndex();
	}

//# Laniatus Games Studio Inc. | TODO TASK: The implementation of the following method could not be found:
//		void RefreshInstances();

	public bool __CanShot(CInstanceBase rkInstMain, CInstanceBase rkInstTarget)
	{
		if (!__HasEnoughArrow())
		{
			PyCallClassMemberFunc(m_ppyGameWindow, "OnCannotShot", Py_BuildValue("(is)", GetMainCharacterIndex(), "EMPTY_ARROW"));
			return false;
		}
    
		if (rkInstMain.IsInSafe())
		{
			PyCallClassMemberFunc(m_ppyGameWindow, "OnCannotShot", Py_BuildValue("(is)", GetMainCharacterIndex(), "IN_SAFE"));
			return false;
		}
    
		if (rkInstTarget.IsInSafe())
		{
			PyCallClassMemberFunc(m_ppyGameWindow, "OnCannotShot", Py_BuildValue("(is)", GetMainCharacterIndex(), "DEST_IN_SAFE"));
			return false;
		}
    
		return true;
	}
	public bool __CanUseSkill()
	{
		CInstanceBase pkInstMain = NEW_GetMainActorPtr();
		if (pkInstMain == null)
		{
			return false;
		}
    
		if (IsObserverMode())
		{
			return false;
		}
    
		if (pkInstMain.IsMountingHorse() && (GetSkillGrade(109) < 1 && GetSkillLevel(109) < 20))
		{
			return false;
		}
    
		return pkInstMain.CanUseSkill();
	}

	public bool __CanMove()
	{
		if (__IsProcessingEmotion())
		{
			return false;
		}
    
		CInstanceBase pkInstMain = NEW_GetMainActorPtr();
		if (pkInstMain == null)
		{
			return false;
		}
    
		if (!pkInstMain.CanMove())
		{
			if (!pkInstMain.IsUsingMovingSkill())
			{
				return false;
			}
		}
    
		return true;
	}

	public bool __CanAttack()
	{
		if (__IsProcessingEmotion())
		{
			return false;
		}
    
		if (IsOpenPrivateShop())
		{
			return false;
		}
    
		if (IsObserverMode())
		{
			return false;
		}
    
		CInstanceBase pkInstMain = NEW_GetMainActorPtr();
		if (pkInstMain == null)
		{
			return false;
		}
    
		if (pkInstMain.IsMountingHorse() && pkInstMain.IsNewMount() && (GetSkillGrade(109) < 1 && GetSkillLevel(109) < 11))
		{
			return false;
		}
    
		return pkInstMain.CanAttack();
	}
	public bool __CanChangeTarget()
	{
		CInstanceBase pkInstMain = NEW_GetMainActorPtr();
		if (pkInstMain == null)
		{
			return false;
		}
    
		return pkInstMain.CanChangeTarget();
	}

	public bool __CheckSkillUsable(uint dwSlotIndex)
	{
		CInstanceBase pkInstMain = NEW_GetMainActorPtr();
		if (pkInstMain == null)
		{
			return false;
		}
    
		if (dwSlotIndex >= DefineConstants.SKILL_MAX_NUM)
		{
			return false;
		}
    
		TSkillInstance rkSkillInst = m_playerStatus.aSkill[dwSlotIndex];
    
		SSkillData pSkillData;
		if (!CPythonSkill.Instance().GetSkillData(rkSkillInst.dwIndex, pSkillData))
		{
			return false;
		}
    
		if (pkInstMain.IsMountingHorse())
		{
			if (!pSkillData.IsHorseSkill())
			{
				PyCallClassMemberFunc(m_ppyGameWindow, "OnCannotUseSkill", Py_BuildValue("(is)", GetMainCharacterIndex(), "NOT_HORSE_SKILL"));
				return false;
			}
		}
    
		if (pSkillData.IsHorseSkill())
		{
			if (!pkInstMain.IsMountingHorse())
			{
				PyCallClassMemberFunc(m_ppyGameWindow, "OnCannotUseSkill", Py_BuildValue("(is)", GetMainCharacterIndex(), "HAVE_TO_RIDE"));
				return false;
			}
		}
    
		if (pSkillData.IsAttackSkill())
		{
			if (pkInstMain.IsInSafe())
			{
				PyCallClassMemberFunc(m_ppyGameWindow, "OnCannotUseSkill", Py_BuildValue("(is)", GetMainCharacterIndex(), "IN_SAFE"));
    
				return false;
			}
		}
    
		if (!pSkillData.IsCanUseSkill())
		{
			return false;
		}
    
		if (pSkillData.IsNeedEmptyBottle())
		{
			if (!__HasItem(27995))
			{
				PyCallClassMemberFunc(m_ppyGameWindow, "OnCannotUseSkill", Py_BuildValue("(is)", GetMainCharacterIndex(), "NEED_EMPTY_BOTTLE"));
				return false;
			}
		}
    
		if (pSkillData.IsNeedPoisonBottle())
		{
			if (!__HasItem(27996))
			{
				PyCallClassMemberFunc(m_ppyGameWindow, "OnCannotUseSkill", Py_BuildValue("(is)", GetMainCharacterIndex(), "NEED_POISON_BOTTLE"));
				return false;
			}
		}
    
		if (pkInstMain.IsFishingMode())
		{
			PyCallClassMemberFunc(m_ppyGameWindow, "OnCannotUseSkill", Py_BuildValue("(is)", GetMainCharacterIndex(), "REMOVE_FISHING_ROD"));
			return false;
		}
    
		if (m_sysIsLevelLimit)
		{
			if (rkSkillInst.iLevel <= 0)
			{
				PyCallClassMemberFunc(m_ppyGameWindow, "OnCannotUseSkill", Py_BuildValue("(is)", GetMainCharacterIndex(), "NOT_YET_LEARN"));
				return false;
			}
		}
    
		if (!pSkillData.CanUseWeaponType(pkInstMain.GetWeaponType()))
		{
			PyCallClassMemberFunc(m_ppyGameWindow, "OnCannotUseSkill", Py_BuildValue("(is)", GetMainCharacterIndex(), "NOT_MATCHABLE_WEAPON"));
			return false;
		}
    
		if (!pSkillData.IsHorseSkill())
		{
			if (__CheckShortArrow(rkSkillInst, pSkillData))
			{
				return false;
			}
    
			if (pSkillData.IsNeedBow())
			{
				if (!__HasEnoughArrow())
				{
					return false;
				}
			}
		}
    
		if (__CheckDashAffect(pkInstMain))
		{
			if (!pSkillData.IsChargeSkill())
			{
				if (__CheckRestSkillCoolTime(dwSlotIndex))
				{
					PyCallClassMemberFunc(m_ppyGameWindow, "OnCannotUseSkill", Py_BuildValue("(is)", GetMainCharacterIndex(), "WAIT_COOLTIME"));
					return false;
				}
			}
		}
		else
		{
			if (__CheckRestSkillCoolTime(dwSlotIndex))
			{
				PyCallClassMemberFunc(m_ppyGameWindow, "OnCannotUseSkill", Py_BuildValue("(is)", GetMainCharacterIndex(), "WAIT_COOLTIME"));
				return false;
			}
    
			if (__CheckShortLife(rkSkillInst, pSkillData))
			{
				PyCallClassMemberFunc(m_ppyGameWindow, "OnCannotUseSkill", Py_BuildValue("(is)", GetMainCharacterIndex(), "NOT_ENOUGH_HP"));
				return false;
			}
    
			if (__CheckShortMana(rkSkillInst, pSkillData))
			{
				PyCallClassMemberFunc(m_ppyGameWindow, "OnCannotUseSkill", Py_BuildValue("(is)", GetMainCharacterIndex(), "NOT_ENOUGH_SP"));
				return false;
			}
		}
		return true;
	}
	public void __UseCurrentSkill()
	{
		__UseSkill(m_dwcurSkillSlotIndex);
	}
//# Laniatus Games Studio Inc. | TODO TASK: The implementation of the following method could not be found:
//		void __UseChargeSkill(uint dwSkillSlotIndex);
	public bool __UseSkill(uint dwSlotIndex)
	{
		if (IsOpenPrivateShop())
		{
			return true;
		}
    
		if (!__CanUseSkill())
		{
			return false;
		}
    
		if (dwSlotIndex >= DefineConstants.SKILL_MAX_NUM)
		{
			Tracenf("CPythonPlayer::__UseSkill(dwSlotIndex=%d) It's not available skill slot number", dwSlotIndex);
			return false;
		}
    
		TSkillInstance rkSkillInst = m_playerStatus.aSkill[dwSlotIndex];
    
		if (__CheckSpecialSkill(rkSkillInst.dwIndex))
		{
			return true;
		}
    
		SSkillData pSkillData;
		if (!CPythonSkill.Instance().GetSkillData(rkSkillInst.dwIndex, pSkillData))
		{
			Tracenf("CPythonPlayer::__UseSkill(dwSlotIndex=%d) There is no skill data", dwSlotIndex);
			return false;
		}
    
		if (pSkillData.IsToggleSkill())
		{
			if (IsSkillActive(dwSlotIndex))
			{
				CPythonNetworkStream.Instance().SendUseSkillPacket(rkSkillInst.dwIndex, dwSlotIndex);
				return false;
			}
		}
    
		if (!__CheckSkillUsable(dwSlotIndex))
		{
			return false;
		}
    
		CInstanceBase pkInstMain = NEW_GetMainActorPtr();
		if (pkInstMain == null)
		{
			Tracenf("CPythonPlayer::__UseSkill(dwSlotIndex=%d) There is no main player", dwSlotIndex);
			return false;
		}
    
		if (pkInstMain.IsUsingSkill())
		{
			return false;
		}
    
		CInstanceBase pkInstTarget = null;
    
		if (pSkillData.IsNeedTarget() || pSkillData.CanChangeDirection() || pSkillData.IsAutoSearchTarget())
		{
			if (pSkillData.IsNeedCorpse())
			{
				pkInstTarget = __GetDeadTargetInstancePtr();
			}
			else
			{
				pkInstTarget = __GetAliveTargetInstancePtr();
			}
    
			if (pkInstTarget == null)
			{
				__ChangeTargetToPickedInstance();
    
				if (pSkillData.IsNeedCorpse())
				{
					pkInstTarget = __GetDeadTargetInstancePtr();
				}
				else
				{
					pkInstTarget = __GetAliveTargetInstancePtr();
				}
			}
    
			if (pkInstTarget != null)
			{
				if (pSkillData.IsOnlyForAlliance())
				{
					if (pkInstMain == pkInstTarget)
					{
						if (!pSkillData.CanUseForMe())
						{
							PyCallClassMemberFunc(m_ppyGameWindow, "OnCannotUseSkill", Py_BuildValue("(is)", GetMainCharacterIndex(), "CANNOT_USE_SELF"));
							return false;
						}
					}
					else if (!pkInstMain.IsAttackableInstance(pkInstTarget) && pkInstTarget.IsPC())
					{
						uint dwSkillRange = __GetSkillTargetRange(pSkillData);
    
						if (dwSkillRange > 0)
						{
							float fDistance = pkInstMain.GetDistance(pkInstTarget);
							if (fDistance >= (float)dwSkillRange)
							{
								__ReserveUseSkill(pkInstTarget.GetVirtualID(), dwSlotIndex, dwSkillRange);
								return false;
							}
						}
					}
					else
					{
						if (pSkillData.CanUseForMe())
						{
							pkInstTarget = pkInstMain;
							Tracef(" [ALERT] ???ῡ?? ?????? ????ӿ??? ?????? Ÿ???? ?Ǿ??־ ?ڽſ??Է? ?缳??\n");
						}
						else
						{
							PyCallClassMemberFunc(m_ppyGameWindow, "OnCannotUseSkill", Py_BuildValue("(is)", GetMainCharacterIndex(), "ONLY_FOR_ALLIANCE"));
							return false;
						}
					}
				}
				else
				{
					if (pkInstTarget.IsInSafe())
					{
						PyCallClassMemberFunc(m_ppyGameWindow, "OnCannotUseSkill", Py_BuildValue("(is)", GetMainCharacterIndex(), "CANNOT_ATTACK_ENEMY_IN_SAFE_AREA"));
						return false;
					}
    
					if (pkInstMain.IsAttackableInstance(pkInstTarget))
					{
						if (!__ProcessEnemySkillTargetRange(pkInstMain, pkInstTarget, pSkillData, dwSlotIndex))
						{
							return false;
						}
					}
					else
					{
						PyCallClassMemberFunc(m_ppyGameWindow, "OnCannotUseSkill", Py_BuildValue("(is)", GetMainCharacterIndex(), "CANNOT_ATTACK"));
						return false;
					}
				}
    
				pkInstMain.SetFlyTargetInstance(pkInstTarget);
    
				if (pkInstMain != pkInstTarget)
				{
					if (pkInstMain.IsFlyTargetObject())
					{
						pkInstMain.NEW_LookAtFlyTarget();
					}
					else
					{
						pkInstMain.NEW_LookAtDestInstance(pkInstTarget);
					}
				}
			}
			else
			{
				if (pSkillData.IsAutoSearchTarget())
				{
					if (pkInstMain.NEW_GetFrontInstance(pkInstTarget, 2000.0f))
					{
						SetTarget(pkInstTarget.GetVirtualID());
						if (!__ProcessEnemySkillTargetRange(pkInstMain, pkInstTarget, pSkillData, dwSlotIndex))
						{
							return false;
						}
					}
					else
					{
						PyCallClassMemberFunc(m_ppyGameWindow, "OnCannotUseSkill", Py_BuildValue("(is)", GetMainCharacterIndex(), "NEED_TARGET"));
						return false;
					}
				}
    
				if (pSkillData.CanUseForMe())
				{
					pkInstTarget = pkInstMain;
					pkInstMain.SetFlyTargetInstance(pkInstMain);
					Tracef(" [ALERT] Ÿ???? ??? ?÷??̾?? ???????\n");
				}
				else if (pSkillData.IsNeedCorpse())
				{
					PyCallClassMemberFunc(m_ppyGameWindow, "OnCannotUseSkill", Py_BuildValue("(is)", GetMainCharacterIndex(), "ONLY_FOR_CORPSE"));
					return false;
				}
				else
				{
					PyCallClassMemberFunc(m_ppyGameWindow, "OnCannotUseSkill", Py_BuildValue("(is)", GetMainCharacterIndex(), "NEED_TARGET"));
					return false;
				}
			}
		}
    
		if (pSkillData.CanChangeDirection())
		{
			uint dwPickedActorID;
			TPixelPosition kPPosPickedGround = new TPixelPosition();
    
			if (pkInstTarget != null && pkInstTarget != pkInstMain)
			{
				pkInstMain.NEW_LookAtDestInstance(pkInstTarget);
			}
			else if (__GetPickedActorID(dwPickedActorID))
			{
				CInstanceBase pkInstVictim = NEW_FindActorPtr(dwPickedActorID);
				if (pkInstVictim != null)
				{
					pkInstMain.NEW_LookAtDestInstance(pkInstVictim);
				}
			}
			else if (__GetPickedGroundPos(kPPosPickedGround))
			{
				pkInstMain.NEW_LookAtDestPixelPosition(kPPosPickedGround);
			}
			else
			{
				Tracenf("CPythonPlayer::__UseSkill(%d) - ȭ?? ???? ???? ?????? ?ؾ???", dwSlotIndex);
			}
		}
    
		uint dwTargetMaxCount = pSkillData.GetTargetCount(rkSkillInst.fcurEfficientPercentage);
		uint dwRange = __GetSkillTargetRange(pSkillData);
		if (dwTargetMaxCount > 0 && pkInstTarget != null)
		{
			uint dwTargetCount = 1;
			List<CInstanceBase> kVct_pkInstTarget = new List<CInstanceBase>();
    
			if (pSkillData.IsFanRange())
			{
				if (pkInstMain.NEW_GetInstanceVectorInFanRange((float)dwRange, pkInstTarget, kVct_pkInstTarget))
				{
					List<CInstanceBase>.Enumerator i;
					for (i = kVct_pkInstTarget.GetEnumerator(); i.MoveNext();)
					{
						if (dwTargetCount >= dwTargetMaxCount)
						{
							break;
						}
    
						CInstanceBase pkInstEach = i.Current;
    
						if (pkInstTarget != pkInstEach && !pkInstEach.IsDead())
						{
							pkInstMain.AddFlyTargetInstance(pkInstEach);
							CPythonNetworkStream.Instance().SendAddFlyTargetingPacket(pkInstEach.GetVirtualID(), pkInstEach.GetGraphicThingInstanceRef().OnGetFlyTargetPosition());
    
							dwTargetCount++;
						}
					}
				}
			}
			else if (pSkillData.IsCircleRange())
			{
				if (pkInstMain.NEW_GetInstanceVectorInCircleRange((float)dwRange, kVct_pkInstTarget))
				{
					List<CInstanceBase>.Enumerator i;
					for (i = kVct_pkInstTarget.GetEnumerator(); i.MoveNext();)
					{
						if (dwTargetCount >= dwTargetMaxCount)
						{
							break;
						}
    
						CInstanceBase pkInstEach = i.Current;
    
						if (pkInstTarget != pkInstEach && !pkInstEach.IsDead())
						{
							pkInstMain.AddFlyTargetInstance(pkInstEach);
							CPythonNetworkStream.Instance().SendAddFlyTargetingPacket(pkInstEach.GetVirtualID(), pkInstEach.GetGraphicThingInstanceRef().OnGetFlyTargetPosition());
    
							dwTargetCount++;
						}
					}
				}
			}
    
			if (dwTargetCount < dwTargetMaxCount)
			{
				while (dwTargetCount < dwTargetMaxCount)
				{
					TPixelPosition kPPosDst = new TPixelPosition();
					pkInstMain.NEW_GetRandomPositionInFanRange(pkInstTarget, kPPosDst);
    
					kPPosDst.x = kPPosDst.x;
					kPPosDst.y = -kPPosDst.y;
    
					pkInstMain.AddFlyTargetPosition(kPPosDst);
					CPythonNetworkStream.Instance().SendAddFlyTargetingPacket(0, kPPosDst);
    
					dwTargetCount++;
				}
			}
		}
    
		__ClearReservedAction();
    
		if (!pSkillData.IsNoMotion())
		{
			uint dwMotionIndex = pSkillData.GetSkillMotionIndex(rkSkillInst.iGrade);
			uint dwLoopCount = pSkillData.GetMotionLoopCount(rkSkillInst.fcurEfficientPercentage);
			if (!pkInstMain.NEW_UseSkill(rkSkillInst.dwIndex, dwMotionIndex, dwLoopCount, pSkillData.IsMovingSkill() ? true : false))
			{
				Tracenf("CPythonPlayer::__UseSkill(%d) - pkInstMain->NEW_UseSkill - ERROR", dwSlotIndex);
				return false;
			}
		}
    
		uint dwTargetVID = (uint)(pkInstTarget != null ? pkInstTarget.GetVirtualID() : 0);
    
		__SendUseSkill(dwSlotIndex, dwTargetVID);
		return true;
	}
	public bool __CheckSpecialSkill(uint dwSkillIndex)
	{
		CInstanceBase pkInstMain = NEW_GetMainActorPtr();
		if (pkInstMain == null)
		{
			return false;
		}
    
		if (c_iSkillIndex_Fishing == dwSkillIndex)
		{
			if (pkInstMain.IsFishingMode())
			{
				NEW_Fishing();
			}
			else
			{
				PyCallClassMemberFunc(m_ppyGameWindow, "OnCannotUseSkill", Py_BuildValue("(is)", GetMainCharacterIndex(), "EQUIP_FISHING_ROD"));
			}
			return true;
		}
    
		else if (c_iSkillIndex_Combo == dwSkillIndex)
		{
			uint dwSlotIndex;
			if (!GetSkillSlotIndex(dwSkillIndex, dwSlotIndex))
			{
				return false;
			}
    
			int iLevel = GetSkillLevel(dwSlotIndex);
			if (iLevel > 0)
			{
				CPythonNetworkStream.Instance().SendUseSkillPacket(dwSkillIndex);
			}
			else
			{
				PyCallClassMemberFunc(m_ppyGameWindow, "OnCannotUseSkill", Py_BuildValue("(is)", GetMainCharacterIndex(), "NOT_YET_LEARN"));
			}
    
			return true;
		}
    
		return false;
	}

	public bool __CheckRestSkillCoolTime(uint dwSlotIndex)
	{
		if (!m_sysIsCoolTime)
		{
			return false;
		}
    
		if (dwSlotIndex >= DefineConstants.SKILL_MAX_NUM)
		{
			return false;
		}
    
		float fElapsedTime = CTimer.Instance().GetCurrentSecond() - m_playerStatus.aSkill[dwSlotIndex].fLastUsedTime;
		if (fElapsedTime >= m_playerStatus.aSkill[dwSlotIndex].fCoolTime)
		{
			return false;
		}
    
		return true;
	}
	public bool __CheckShortLife(TSkillInstance rkSkillInst, SSkillData rkSkillData)
	{
		if (!rkSkillData.IsUseHPSkill())
		{
			return false;
		}
    
		uint dwNeedHP = rkSkillData.GetNeedSP(rkSkillInst.fcurEfficientPercentage);
		if (dwNeedHP <= GetStatus(POINT_HP))
		{
			return false;
		}
    
		return true;
	}
	public bool __CheckShortMana(TSkillInstance rkSkillInst, SSkillData rkSkillData)
	{
	#if ! ENABLE_LOAD_PLAYERSETTING
	//# Laniatus Games Studio Inc. |: 'extern' variable declarations are not required in C#:
	//	extern const uint c_iSkillIndex_Summon;
	#endif
		if (c_iSkillIndex_Summon == rkSkillInst.dwIndex)
		{
			return false;
		}
    
		int iNeedSP = rkSkillData.GetNeedSP(rkSkillInst.fcurEfficientPercentage);
		int icurSP = GetStatus(POINT_SP);
    
		if (!rkSkillData.IsToggleSkill())
		{
			if (iNeedSP == 0)
			{
				CPythonChat.Instance().AppendChat(CHAT_TYPE_INFO, "!!! Find strange game data. Please reinstall metin2.");
				return true;
			}
		}
    
		if (rkSkillData.CanUseIfNotEnough())
		{
			if (icurSP <= 0)
			{
				return true;
			}
		}
		else
		{
			if (-1 != iNeedSP)
			{
				if (iNeedSP > icurSP)
				{
					return true;
				}
			}
		}
    
		return false;
	}
	public bool __CheckShortArrow(TSkillInstance rkSkillInst, SSkillData rkSkillData)
	{
		if (!rkSkillData.IsNeedBow())
		{
			return false;
		}
    
		if (__HasEnoughArrow())
		{
			return false;
		}
    
		return true;
	}
	public bool __CheckDashAffect(CInstanceBase rkInstMain)
	{
		return rkInstMain.IsAffect(CInstanceBase.AFFECT_DASH);
	}

	public void __SendUseSkill(uint dwSkillSlotIndex, uint dwTargetVID)
	{
		TSkillInstance rkSkillInst = m_playerStatus.aSkill[dwSkillSlotIndex];
    
		CPythonNetworkStream rkNetStream = CPythonNetworkStream.Instance();
		rkNetStream.SendUseSkillPacket(rkSkillInst.dwIndex, dwTargetVID);
    
		__RunCoolTime(dwSkillSlotIndex);
	}
	public void __RunCoolTime(uint dwSkillSlotIndex)
	{
		TSkillInstance rkSkillInst = m_playerStatus.aSkill[dwSkillSlotIndex];
    
		SSkillData pkSkillData;
		if (!CPythonSkill.Instance().GetSkillData(rkSkillInst.dwIndex, pkSkillData))
		{
			TraceError("CPythonPlayer::__SendUseSkill(dwSkillSlotIndex=%d) - NOT CHECK", dwSkillSlotIndex);
			return;
		}
    
	//# Laniatus Games Studio Inc. | TODO TASK: C# does not have an equivalent to references to variables:
	//Original Metin2 CPlus Line: SSkillData& rkSkillData=*pkSkillData;
		SSkillData rkSkillData = pkSkillData;
    
		rkSkillInst.fCoolTime = rkSkillData.GetSkillCoolTime(rkSkillInst.fcurEfficientPercentage);
		rkSkillInst.fLastUsedTime = CTimer.Instance().GetCurrentSecond();
    
		int iSpd = 100 - GetStatus(POINT_CASTING_SPEED);
		if (iSpd > 0)
		{
			iSpd = 100 + iSpd;
		}
		else if (iSpd < 0)
		{
			iSpd = 10000 / (100 - iSpd);
		}
		else
		{
			iSpd = 100;
		}
    
		rkSkillInst.fCoolTime = rkSkillInst.fCoolTime * iSpd / 100;
    
		PyCallClassMemberFunc(m_ppyGameWindow, "RunUseSkillEvent", Py_BuildValue("(if)", dwSkillSlotIndex, rkSkillInst.fCoolTime));
	}

	public byte __GetSkillType(uint dwSkillSlotIndex)
	{
		TSkillInstance rkSkillInst = m_playerStatus.aSkill[dwSkillSlotIndex];
    
		SSkillData pkSkillData;
		CPythonSkill rkPythonSkill = CPythonSkill.Instance();
		if (!rkPythonSkill.GetSkillData(rkSkillInst.dwIndex, pkSkillData))
		{
			return 0;
		}
		return pkSkillData.GetType();
	}

	public bool __IsReservedUseSkill(uint dwSkillSlotIndex)
	{
		if (MODE_USE_SKILL != m_eReservedMode)
		{
			return false;
		}
    
		if (m_dwSkillSlotIndexReserved != dwSkillSlotIndex)
		{
			return false;
		}
    
		return true;
	}
//# Laniatus Games Studio Inc. | TODO TASK: The implementation of the following method could not be found:
//		bool __IsMeleeSkill(SSkillData rkSkillData);
//# Laniatus Games Studio Inc. | TODO TASK: The implementation of the following method could not be found:
//		bool __IsChargeSkill(SSkillData rkSkillData);
	public uint __GetSkillTargetRange(SSkillData rkSkillData)
	{
		return rkSkillData.GetTargetRange() + GetStatus(POINT_BOW_DISTANCE) * 100;
	}
//# Laniatus Games Studio Inc. | TODO TASK: The implementation of the following method could not be found:
//		bool __SearchNearTarget();
	public bool __IsUsingChargeSkill()
	{
		CInstanceBase pkInstMain = NEW_GetMainActorPtr();
		if (pkInstMain == null)
		{
			return false;
		}
    
		if (__CheckDashAffect(pkInstMain))
		{
			return true;
		}
    
		if (MODE_USE_SKILL != m_eReservedMode)
		{
			return false;
		}
    
		if (m_dwSkillSlotIndexReserved >= SKILL_MAX_NUM)
		{
			return false;
		}
    
		TSkillInstance rkSkillInst = m_playerStatus.aSkill[m_dwSkillSlotIndexReserved];
    
		CPythonSkill.TSkillData pSkillData;
		if (!CPythonSkill.Instance().GetSkillData(rkSkillInst.dwIndex, pSkillData))
		{
			return false;
		}
    
		return pSkillData.IsChargeSkill() ? true : false;
	}

	public bool __ProcessEnemySkillTargetRange(CInstanceBase rkInstMain, CInstanceBase rkInstTarget, SSkillData rkSkillData, uint dwSkillSlotIndex)
	{
		uint dwSkillTargetRange = __GetSkillTargetRange(rkSkillData);
		float fSkillTargetRange = dwSkillTargetRange;
		if (fSkillTargetRange <= 0.0f)
		{
			return true;
		}
    
		float fTargetDistance = rkInstMain.GetDistance(rkInstTarget);
    
	//# Laniatus Games Studio Inc. |: 'extern' variable declarations are not required in C#:
	//	extern bool IS_HUGE_RACE(uint vnum);
		if (IS_HUGE_RACE(rkInstTarget.GetRace()))
		{
			fTargetDistance -= 200.0f;
		}
    
		if (fTargetDistance >= fSkillTargetRange)
		{
			if (rkSkillData.IsChargeSkill())
			{
				if (!__IsReservedUseSkill(dwSkillSlotIndex))
				{
					__SendUseSkill(dwSkillSlotIndex, 0);
				}
			}
    
			__ReserveUseSkill(rkInstTarget.GetVirtualID(), dwSkillSlotIndex, dwSkillTargetRange);
    
			return false;
		}
    
		TPixelPosition kPPosTarget = new TPixelPosition();
		rkInstTarget.NEW_GetPixelPosition(kPPosTarget);
    
		IBackground rkBG = IBackground.Instance();
		if (rkBG.IsBlock(kPPosTarget.x, kPPosTarget.y))
		{
			PyCallClassMemberFunc(m_ppyGameWindow, "OnCannotUseSkill", Py_BuildValue("(is)", GetMainCharacterIndex(), "CANNOT_APPROACH"));
			return false;
		}
    
		return true;
	}

	public bool __HasEnoughArrow()
	{
		CItemData pItemData;
		if (CItemManager.Instance().GetItemDataPointer(GetItemIndex(TItemPos(INVENTORY, c_Equipment_Arrow)), pItemData))
		{
		if (CItemData.ITEM_TYPE_WEAPON == pItemData.GetType())
		{
		if (CItemData.WEAPON_ARROW == pItemData.GetSubType() || CItemData.WEAPON_QUIVER == pItemData.GetSubType())
		{
			return true;
		}
		}
		}
    
		PyCallClassMemberFunc(m_ppyGameWindow, "OnCannotShotError", Py_BuildValue("(is)", GetMainCharacterIndex(), "EMPTY_ARROW"));
		return false;
	}
	public bool __HasItem(uint dwItemID)
	{
		for (int LaniatusDefVariables = 0; LaniatusDefVariables < c_Inventory_Count; ++i)
		{
			if (dwItemID == GetItemIndex(TItemPos(INVENTORY, i)))
			{
				return true;
			}
		}
		for (int LaniatusDefVariables = 0; LaniatusDefVariables < c_DragonSoul_Inventory_Count; ++i)
		{
			if (dwItemID == GetItemIndex(TItemPos(DRAGON_SOUL_INVENTORY, i)))
			{
				return true;
			}
		}
    
		return false;
	}
	public uint __GetPickableDistance()
	{
		CInstanceBase pkInstMain = NEW_GetMainActorPtr();
		if (pkInstMain != null)
		{
			if (pkInstMain.IsMountingHorse())
			{
				return 500;
			}
		}
    
		return 300;
	}

	public CInstanceBase __GetTargetActorPtr()
	{
		return NEW_FindActorPtr(__GetTargetVID());
	}
	public void __ClearTarget()
	{
		if (!__IsTarget())
		{
			return;
		}
    
		CInstanceBase pkInstMain = NEW_GetMainActorPtr();
		if (pkInstMain == null)
		{
			return;
		}
    
		pkInstMain.ClearFlyTargetInstance();
    
		CInstanceBase pTargetedInstance = __GetTargetActorPtr();
		if (pTargetedInstance != null)
		{
			pTargetedInstance.OnUntargeted();
		}
    
		__SetTargetVID(0);
    
		CPythonNetworkStream.Instance().SendTargetPacket(0);
	}
	public uint __GetTargetVID()
	{
		return m_dwTargetVID;
	}
	public void __SetTargetVID(uint dwVID)
	{
		m_dwTargetVID = dwVID;
	}
	public bool __IsSameTargetVID(uint dwVID)
	{
		return dwVID == __GetTargetVID();
	}
	public bool __IsTarget()
	{
		return 0 != __GetTargetVID();
	}
	public bool __ChangeTargetToPickedInstance()
	{
		uint dwVID;
		if (!CPythonCharacterManager.Instance().OLD_GetPickedInstanceVID(dwVID))
		{
			return false;
		}
    
		SetTarget(dwVID);
		return true;
	}

	public CInstanceBase __GetSkillTargetInstancePtr(SSkillData rkSkillData)
	{
		if (rkSkillData.IsNeedCorpse())
		{
			return __GetDeadTargetInstancePtr();
		}
    
		return __GetAliveTargetInstancePtr();
	}
	public CInstanceBase __GetAliveTargetInstancePtr()
	{
		if (!__IsTarget())
		{
			return null;
		}
    
		CInstanceBase pkInstTarget = __GetTargetActorPtr();
    
		if (pkInstTarget == null)
		{
			return null;
		}
    
		if (pkInstTarget.IsDead())
		{
			return null;
		}
    
		return pkInstTarget;
	}
	public CInstanceBase __GetDeadTargetInstancePtr()
	{
		if (!__IsTarget())
		{
			return null;
		}
    
		CInstanceBase pkInstTarget = __GetTargetActorPtr();
    
		if (pkInstTarget == null)
		{
			return null;
		}
    
		if (!pkInstTarget.IsDead())
		{
			return null;
		}
    
		return pkInstTarget;
	}

	public bool __IsRightButtonSkillMode()
	{
		return MBF_SKILL == m_aeMBFButton[MBT_RIGHT];
	}

	public void __Update_AutoAttack()
	{
		if (0 == m_dwAutoAttackTargetVID)
		{
			return;
		}
    
		CInstanceBase pkInstMain = NEW_GetMainActorPtr();
		if (pkInstMain == null)
		{
			return;
		}
    
		if (__IsUsingChargeSkill())
		{
			return;
		}
    
		CInstanceBase pkInstVictim = NEW_FindActorPtr(m_dwAutoAttackTargetVID);
		if (pkInstVictim == null)
		{
			__ClearAutoAttackTargetActorID();
		}
		else
		{
			if (pkInstVictim.IsDead())
			{
				__ClearAutoAttackTargetActorID();
			}
			else if (pkInstMain.IsMountingHorse() && !pkInstMain.CanAttackHorseLevel())
			{
				__ClearAutoAttackTargetActorID();
			}
			else if (pkInstMain.IsAttackableInstance(pkInstVictim))
			{
				if (pkInstMain.IsSleep())
				{
				}
				else
				{
					__ReserveClickActor(m_dwAutoAttackTargetVID);
				}
			}
		}
	}
	public void __Update_NotifyGuildAreaEvent()
	{
		CInstanceBase pkInstMain = NEW_GetMainActorPtr();
		if (pkInstMain != null)
		{
			TPixelPosition kPixelPosition = new TPixelPosition();
			pkInstMain.NEW_GetPixelPosition(kPixelPosition);
    
			uint dwAreaID = CPythonMiniMap.Instance().GetGuildAreaID((uint)kPixelPosition.x, (uint)kPixelPosition.y);
    
			if (dwAreaID != m_inGuildAreaID)
			{
				if (0xffffffff != dwAreaID)
				{
					PyCallClassMemberFunc(m_ppyGameWindow, "BINARY_Guild_EnterGuildArea", Py_BuildValue("(i)", dwAreaID));
				}
				else
				{
					PyCallClassMemberFunc(m_ppyGameWindow, "BINARY_Guild_ExitGuildArea", Py_BuildValue("(i)", dwAreaID));
				}
    
				m_inGuildAreaID = dwAreaID;
			}
		}
	}
	public bool __IsProcessingEmotion()
	{
		return m_bisProcessingEmotion;
	}


		protected PyObject m_ppyGameWindow;
		protected SortedDictionary<uint, uint> m_skillSlotDict = new SortedDictionary<uint, uint>();
		protected string m_stName = "";
		protected uint m_dwMainCharacterIndex;
		protected uint m_dwRace;
		protected uint m_dwWeaponMinPower;
		protected uint m_dwWeaponMaxPower;
		protected uint m_dwWeaponMinMagicPower;
		protected uint m_dwWeaponMaxMagicPower;
		protected uint m_dwWeaponAddPower;
		protected uint m_dwSendingTargetVID;
		protected float m_fTargetUpdateTime;
		protected uint m_dwAutoAttackTargetVID;
		protected EMode m_eReservedMode;
		protected float m_fReservedDelayTime;

		protected float m_fMovDirRot;

		protected bool m_isUp;
		protected bool m_isDown;
		protected bool m_isLeft;
		protected bool m_isRight;
		protected bool m_isAtkKey;
		protected bool m_isDirKey;
		protected bool m_isCmrRot;
		protected bool m_isSmtMov;
		protected bool m_isDirMov;

		protected float m_fCmrRotSpd;

		protected SPlayerStatus m_playerStatus = new SPlayerStatus();

		protected uint m_iComboOld;
		protected uint m_dwVIDReserved;
		protected uint m_dwIIDReserved;

		protected uint m_dwcurSkillSlotIndex;
		protected uint m_dwSkillSlotIndexReserved;
		protected uint m_dwSkillRangeReserved;

		protected TPixelPosition m_kPPosInstPrev = new TPixelPosition();
		protected TPixelPosition m_kPPosReserved = new TPixelPosition();
		protected bool m_bisProcessingEmotion;
		protected bool m_isDestPosition;
		protected int m_ixDestPos;
		protected int m_iyDestPos;
		protected int m_iLastAlarmTime;
		protected SortedDictionary<uint, SPartyMemberInfo> m_PartyMemberMap = new SortedDictionary<uint, SPartyMemberInfo>();

		protected SortedSet<uint> m_ChallengeInstanceSet = new SortedSet<uint>();
		protected SortedSet<uint> m_RevengeInstanceSet = new SortedSet<uint>();
		protected SortedSet<uint> m_CantFightInstanceSet = new SortedSet<uint>();

		protected bool m_isOpenPrivateShop;
		protected bool m_isObserverMode;
		protected bool m_isConsumingStamina;
		protected float m_fCurrentStamina;
		protected float m_fConsumeStaminaPerSec;

		protected uint m_inGuildAreaID;

		protected bool m_sysIsCoolTime;
		protected bool m_sysIsLevelLimit;

		protected TPixelPosition m_MovingCursorPosition = new TPixelPosition();
		protected float m_fMovingCursorSettingTime;
		protected uint[] m_adwEffect = new uint[(int)EEffect.EFFECT_NUM];

		protected uint m_dwVIDPicked;
		protected uint m_dwIIDPicked;
		protected int[] m_aeMBFButton = new int[MBT_NUM];

		protected uint m_dwTargetVID;
		protected uint m_dwTargetEndTime;
		protected uint m_dwPlayTime;

		protected SAutoPotionInfo[] m_kAutoPotionInfo = Arrays.InitializeWithDefaultInstances<SAutoPotionInfo>((int)EAutoPotionType.AUTO_POTION_TYPE_NUM);

		protected float MOVABLE_GROUND_DISTANCE;

		private SortedDictionary<uint, uint> m_kMap_dwAffectIndexToSkillIndex = new SortedDictionary<uint, uint>();
		private List<packet_item> m_ItemAcceInstanceVector = new List<packet_item>();
	public byte m_acceRefineWindowIsOpen;
	public uint m_acceRefineWindowType;
	public int[] m_acceRefineActivedSlot = new int[3];
}