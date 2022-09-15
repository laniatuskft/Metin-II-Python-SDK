public class CPythonApplication
{
//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __UpdateCamera()
	{
		CCamera pMainCamera = CCameraManager.Instance().GetCurrentCamera();
		if (pMainCamera == null)
		{
			return;
		}
    
		if (CAMERA_MODE_BLEND == m_iCameraMode)
		{
			float fcurTime = CTimer.Instance().GetCurrentSecond();
			float fElapsedTime = fcurTime - m_fBlendCameraStartTime;
    
			float fxCenter = BlendValueByLinear(fElapsedTime, m_fBlendCameraBlendTime, m_kEventCameraSetting.v3CenterPosition.x, m_kEndBlendCameraSetting.v3CenterPosition.x);
			float fyCenter = BlendValueByLinear(fElapsedTime, m_fBlendCameraBlendTime, m_kEventCameraSetting.v3CenterPosition.y, m_kEndBlendCameraSetting.v3CenterPosition.y);
			float fzCenter = BlendValueByLinear(fElapsedTime, m_fBlendCameraBlendTime, m_kEventCameraSetting.v3CenterPosition.z, m_kEndBlendCameraSetting.v3CenterPosition.z);
    
			float fDistance = BlendValueByLinear(fElapsedTime, m_fBlendCameraBlendTime, m_kEventCameraSetting.fZoom, m_kEndBlendCameraSetting.fZoom);
			float fPitch = BlendValueByLinear(fElapsedTime, m_fBlendCameraBlendTime, m_kEventCameraSetting.fPitch, m_kEndBlendCameraSetting.fPitch);
			float fRotation = BlendValueByLinear(fElapsedTime, m_fBlendCameraBlendTime, m_kEventCameraSetting.fRotation, m_kEndBlendCameraSetting.fRotation);
    
			float fUpDir = BlendValueByLinear(fElapsedTime, m_fBlendCameraBlendTime, m_kEventCameraSetting.kCmrPos.m_fUpDir, m_kEndBlendCameraSetting.kCmrPos.m_fUpDir);
			float fViewDir = BlendValueByLinear(fElapsedTime, m_fBlendCameraBlendTime, m_kEventCameraSetting.kCmrPos.m_fViewDir, m_kEndBlendCameraSetting.kCmrPos.m_fViewDir);
			float fCrossDir = BlendValueByLinear(fElapsedTime, m_fBlendCameraBlendTime, m_kEventCameraSetting.kCmrPos.m_fCrossDir, m_kEndBlendCameraSetting.kCmrPos.m_fCrossDir);
    
			pMainCamera.Unlock();
			m_pyGraphic.SetPositionCamera(fxCenter, fyCenter, fzCenter, fDistance, fPitch, fRotation);
			pMainCamera.MoveVertical(fUpDir);
			pMainCamera.MoveFront(fViewDir);
			pMainCamera.MoveAlongCross(fCrossDir);
			pMainCamera.Lock();
		}
		else if (CAMERA_MODE_STAND == m_iCameraMode)
		{
			float fDistance;
			float fPitch;
			float fRotation;
			float fHeight;
			GetCamera(fDistance, fPitch, fRotation, fHeight);
			m_pyGraphic.SetPositionCamera(m_kEventCameraSetting.v3CenterPosition.x, m_kEventCameraSetting.v3CenterPosition.y, m_kEventCameraSetting.v3CenterPosition.z + pMainCamera.GetTargetHeight(), fDistance, fPitch, fRotation);
		}
		else if (CAMERA_MODE_NORMAL == m_iCameraMode)
		{
			float fDistance;
			float fPitch;
			float fRotation;
			float fHeight;
			GetCamera(fDistance, fPitch, fRotation, fHeight);
			m_pyGraphic.SetPositionCamera(m_v3CenterPosition.x, m_v3CenterPosition.y, m_v3CenterPosition.z + pMainCamera.GetTargetHeight(), fDistance, fPitch, fRotation);
		}
    
		if (0.0f != m_fRotationSpeed)
		{
			pMainCamera.Roll(m_fRotationSpeed);
		}
		if (0.0f != m_fPitchSpeed)
		{
			pMainCamera.Pitch(m_fPitchSpeed);
		}
		if (0.0f != m_fZoomSpeed)
		{
			pMainCamera.Zoom(m_fZoomSpeed);
		}
    
		if (0.0f != m_kCmrSpd.m_fViewDir)
		{
			m_kCmrPos.m_fViewDir += m_kCmrSpd.m_fViewDir;
		}
		if (0.0f != m_kCmrSpd.m_fCrossDir)
		{
			m_kCmrPos.m_fCrossDir += m_kCmrSpd.m_fCrossDir;
		}
		if (0.0f != m_kCmrSpd.m_fUpDir)
		{
			m_kCmrPos.m_fUpDir += m_kCmrSpd.m_fUpDir;
		}
    
		if (0.0f != m_kCmrPos.m_fViewDir)
		{
			pMainCamera.MoveFront(m_kCmrPos.m_fViewDir);
		}
		if (0.0f != m_kCmrPos.m_fCrossDir)
		{
			pMainCamera.MoveAlongCross(m_kCmrPos.m_fCrossDir);
		}
		if (0.0f != m_kCmrPos.m_fUpDir)
		{
			pMainCamera.MoveVertical(m_kCmrPos.m_fUpDir);
		}
    
		if (pMainCamera.IsDraging())
		{
			SkipRenderBuffering(3000);
		}
    
		_D3DVECTOR c_rv3CameraDirection = pMainCamera.GetView();
		_D3DVECTOR c_rv3CameraUp = pMainCamera.GetUp();
		m_SoundManager.SetPosition(m_v3CenterPosition.x, m_v3CenterPosition.y, m_v3CenterPosition.z);
		m_SoundManager.SetDirection(c_rv3CameraDirection.x, c_rv3CameraDirection.y, c_rv3CameraDirection.z, c_rv3CameraUp.x, c_rv3CameraUp.y, c_rv3CameraUp.z);
		m_SoundManager.Update();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetViewDirCameraSpeed(float fSpeed)
	{
		if (IsLockCurrentCamera())
		{
			return;
		}
    
		m_kCmrSpd.m_fViewDir = fSpeed;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetCrossDirCameraSpeed(float fSpeed)
	{
		if (IsLockCurrentCamera())
		{
			return;
		}
    
		m_kCmrSpd.m_fCrossDir = fSpeed;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetUpDirCameraSpeed(float fSpeed)
	{
		if (IsLockCurrentCamera())
		{
			return;
		}
    
		m_kCmrSpd.m_fUpDir = fSpeed;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetCamera(float Distance, float Pitch, float Rotation, float fDestinationHeight)
	{
		if (IsLockCurrentCamera())
		{
			return;
		}
    
		CCamera pCurrentCamera = CCameraManager.Instance().GetCurrentCamera();
		if (pCurrentCamera == null)
		{
			return;
		}
    
		_D3DVECTOR v3Target = pCurrentCamera.GetTarget();
		m_pyGraphic.SetPositionCamera(v3Target.x, v3Target.y, v3Target.z, Distance, Pitch, Rotation);
    
		CCamera pMainCamera = CCameraManager.Instance().GetCurrentCamera();
		if (pMainCamera != null)
		{
			pMainCamera.SetTargetHeight(fDestinationHeight);
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void GetCamera(ref float Distance, ref float Pitch, ref float Rotation, ref float DestinationHeight)
	{
		CCamera pCurrentCamera = CCameraManager.Instance().GetCurrentCamera();
		Distance = pCurrentCamera.GetDistance();
		Pitch = pCurrentCamera.GetPitch();
		Rotation = pCurrentCamera.GetRoll();
		DestinationHeight = pCurrentCamera.GetTarget().z;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void RotateCamera(int iDirection)
	{
		if (IsLockCurrentCamera())
		{
			return;
		}
    
		float fDegree = m_fCameraRotateSpeed * (float)iDirection;
		m_fRotationSpeed = fDegree;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void PitchCamera(int iDirection)
	{
		if (IsLockCurrentCamera())
		{
			return;
		}
    
		float fDegree = m_fCameraPitchSpeed * (float)iDirection;
		m_fPitchSpeed = fDegree;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void ZoomCamera(int iDirection)
	{
		if (IsLockCurrentCamera())
		{
			return;
		}
    
		float fRatio = 1.0f + m_fCameraZoomSpeed * (float)iDirection;
		m_fZoomSpeed = fRatio;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void MovieRotateCamera(int iDirection)
	{
		if (IsLockCurrentCamera())
		{
			return;
		}
    
		float fDegree = m_fCameraRotateSpeed * (float)iDirection;
		if (m_isSpecialCameraMode)
		{
			if ((GetKeyState(VK_SCROLL) & 1) != 0)
			{
				SetCrossDirCameraSpeed(-fDegree * 6.0f);
				return;
			}
		}
		m_fRotationSpeed = fDegree;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void MoviePitchCamera(int iDirection)
	{
		if (IsLockCurrentCamera())
		{
			return;
		}
    
		float fDegree = m_fCameraPitchSpeed * (float)iDirection;
		if (m_isSpecialCameraMode)
		{
			if ((GetKeyState(VK_SCROLL) & 1) != 0)
			{
				SetViewDirCameraSpeed(-fDegree * 6.0f);
				return;
			}
		}
		m_fPitchSpeed = fDegree;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void MovieZoomCamera(int iDirection)
	{
		if (IsLockCurrentCamera())
		{
			return;
		}
    
		float fRatio = 1.0f + m_fCameraZoomSpeed * (float)iDirection;
		if (m_isSpecialCameraMode)
		{
			if ((GetKeyState(VK_SCROLL) & 1) != 0)
			{
				SetUpDirCameraSpeed((1.0f - fRatio) * 200.0f);
				return;
			}
		}
		m_fZoomSpeed = fRatio;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void MovieResetCamera()
	{
		if (IsLockCurrentCamera())
		{
			return;
		}
    
		if (m_isSpecialCameraMode)
		{
			SetCrossDirCameraSpeed(0.0f);
			SetViewDirCameraSpeed(0.0f);
			SetUpDirCameraSpeed(0.0f);
    
			m_kCmrPos.m_fViewDir = 0;
			m_kCmrPos.m_fCrossDir = 0;
			m_kCmrPos.m_fUpDir = 0;
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public float GetRotation()
	{
		return CCameraManager.Instance().GetCurrentCamera().GetRoll();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public float GetPitch()
	{
		return CCameraManager.Instance().GetCurrentCamera().GetPitch();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool IsLockCurrentCamera()
	{
		CCamera pCamera = CCameraManager.Instance().GetCurrentCamera();
		if (pCamera == null)
		{
			return false;
		}
    
		return pCamera.IsLock();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetEventCamera(in SCameraSetting c_rCameraSetting)
	{
		if (CCameraManager.DEFAULT_PERSPECTIVE_CAMERA == CCameraManager.Instance().GetCurrentCameraNum())
		{
			GetCameraSetting(m_DefaultCameraSetting);
		}
    
		CCameraManager.Instance().SetCurrentCamera(EVENT_CAMERA_NUMBER);
		CCamera pCamera = CCameraManager.Instance().GetCurrentCamera();
		if (pCamera == null)
		{
			return;
		}
    
		SetCameraSetting(c_rCameraSetting);
		m_kEventCameraSetting = c_rCameraSetting;
		m_iCameraMode = CAMERA_MODE_STAND;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void BlendEventCamera(in SCameraSetting c_rCameraSetting, float fBlendTime)
	{
		m_iCameraMode = CAMERA_MODE_BLEND;
		m_fBlendCameraStartTime = CTimer.Instance().GetCurrentSecond();
		m_fBlendCameraBlendTime = fBlendTime;
		m_kEndBlendCameraSetting = c_rCameraSetting;
    
		CCamera pCamera = CCameraManager.Instance().GetCurrentCamera();
		if (pCamera != null)
		{
			pCamera.Lock();
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetDefaultCamera()
	{
		m_iCameraMode = CAMERA_MODE_NORMAL;
		m_fBlendCameraStartTime = 0.0f;
		m_fBlendCameraBlendTime = 0.0f;
    
		CCamera pCamera = CCameraManager.Instance().GetCurrentCamera();
		if (pCamera != null)
		{
			pCamera.Unlock();
		}
    
		if (CCameraManager.DEFAULT_PERSPECTIVE_CAMERA != CCameraManager.Instance().GetCurrentCameraNum())
		{
			CCameraManager.Instance().SetCurrentCamera(CCameraManager.DEFAULT_PERSPECTIVE_CAMERA);
			SetCameraSetting(m_DefaultCameraSetting);
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetCameraSetting(in SCameraSetting c_rCameraSetting)
	{
		CCamera pCamera = CCameraManager.Instance().GetCurrentCamera();
		if (pCamera == null)
		{
			return;
		}
    
		m_pyGraphic.SetPositionCamera(c_rCameraSetting.v3CenterPosition.x, c_rCameraSetting.v3CenterPosition.y, c_rCameraSetting.v3CenterPosition.z, c_rCameraSetting.fZoom, c_rCameraSetting.fPitch, c_rCameraSetting.fRotation);
    
		if (0.0f != c_rCameraSetting.kCmrPos.m_fViewDir)
		{
			pCamera.MoveFront(c_rCameraSetting.kCmrPos.m_fViewDir);
		}
		if (0.0f != c_rCameraSetting.kCmrPos.m_fCrossDir)
		{
			pCamera.MoveAlongCross(c_rCameraSetting.kCmrPos.m_fCrossDir);
		}
		if (0.0f != c_rCameraSetting.kCmrPos.m_fUpDir)
		{
			pCamera.MoveVertical(c_rCameraSetting.kCmrPos.m_fUpDir);
		}
    
		m_kCmrPos.m_fUpDir = 0.0f;
		m_kCmrPos.m_fViewDir = 0.0f;
		m_kCmrPos.m_fCrossDir = 0.0f;
		m_kCmrSpd.m_fUpDir = 0.0f;
		m_kCmrSpd.m_fViewDir = 0.0f;
		m_kCmrSpd.m_fCrossDir = 0.0f;
		m_fZoomSpeed = 0.0f;
		m_fPitchSpeed = 0.0f;
		m_fRotationSpeed = 0.0f;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void GetCameraSetting(SCameraSetting pCameraSetting)
	{
		pCameraSetting.v3CenterPosition = m_v3CenterPosition;
		pCameraSetting.kCmrPos = m_kCmrPos;
    
		if (CCameraManager.Instance().GetCurrentCamera())
		{
			pCameraSetting.v3CenterPosition.z += CCameraManager.Instance().GetCurrentCamera().GetTargetHeight();
		}
    
		float fHeight;
		GetCamera(pCameraSetting.fZoom, pCameraSetting.fPitch, pCameraSetting.fRotation, fHeight);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SaveCameraSetting(string c_szFileName)
	{
		SCameraSetting CameraSetting = new SCameraSetting();
		GetCameraSetting(CameraSetting);
    
		FILE File = fopen(c_szFileName, "w");
		SetFileAttributes(c_szFileName, FILE_ATTRIBUTE_NORMAL);
    
		PrintfTabs(File, 0, "CenterPos %f %f %f\n", CameraSetting.v3CenterPosition.x, CameraSetting.v3CenterPosition.y, CameraSetting.v3CenterPosition.z);
		PrintfTabs(File, 0, "CameraSetting %f %f %f\n", CameraSetting.fZoom, CameraSetting.fPitch, CameraSetting.fRotation);
		PrintfTabs(File, 0, "CmrPos %f %f %f\n", CameraSetting.kCmrPos.m_fUpDir, CameraSetting.kCmrPos.m_fViewDir, CameraSetting.kCmrPos.m_fCrossDir);
		PrintfTabs(File, 0, "Line \"x;%d|y;%d|z;%d|distance;%d|pitch;%d|rot;%d|up;%d|view;%d|cross;%d\"\n", (int)CameraSetting.v3CenterPosition.x, (int)CameraSetting.v3CenterPosition.y, (int)CameraSetting.v3CenterPosition.z, (int)CameraSetting.fZoom, (int)CameraSetting.fPitch, (int)CameraSetting.fRotation, (int)CameraSetting.kCmrPos.m_fUpDir, (int)CameraSetting.kCmrPos.m_fViewDir, (int)CameraSetting.kCmrPos.m_fCrossDir);
    
		fclose(File);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool LoadCameraSetting(string c_szFileName)
	{
		CTextFileLoader TextFileLoader = new CTextFileLoader();
		if (!TextFileLoader.Load(c_szFileName))
		{
			return false;
		}
    
		TextFileLoader.SetTop();
    
		_D3DVECTOR v3CenterPosition = new _D3DVECTOR();
		CTokenVector pCameraSetting;
		CTokenVector pCmrPos;
		if (TextFileLoader.GetTokenVector3("centerpos", v3CenterPosition))
		{
		if (TextFileLoader.GetTokenVector("camerasetting", pCameraSetting))
		{
		if (TextFileLoader.GetTokenVector("cmrpos", pCmrPos))
		{
		if (3 == pCameraSetting.size())
		{
		if (3 == pCmrPos.size())
		{
			SCameraSetting CameraSetting = new SCameraSetting();
			CameraSetting.v3CenterPosition = v3CenterPosition;
    
			CameraSetting.fZoom = atof(pCameraSetting.at(0).c_str());
			CameraSetting.fPitch = atof(pCameraSetting.at(1).c_str());
			CameraSetting.fRotation = atof(pCameraSetting.at(2).c_str());
    
			CameraSetting.kCmrPos.m_fUpDir = atof(pCmrPos.at(0).c_str());
			CameraSetting.kCmrPos.m_fViewDir = atof(pCmrPos.at(1).c_str());
			CameraSetting.kCmrPos.m_fCrossDir = atof(pCmrPos.at(2).c_str());
    
			SetEventCamera(CameraSetting);
			return true;
		}
		}
		}
		}
		}
    
		return false;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool CreateCursors()
	{
		NANOBEGIN m_bCursorVisible = true;
		m_bLiarCursorOn = false;
    
		int[] ResourceID = Arrays.PadValueTypeArrayWithDefaultInstances(CURSOR_COUNT, new int[] {IDC_CURSOR_NORMAL, IDC_CURSOR_ATTACK, IDC_CURSOR_ATTACK, IDC_CURSOR_TALK, IDC_CURSOR_NO, IDC_CURSOR_PICK, IDC_CURSOR_DOOR, IDC_CURSOR_CHAIR, IDC_CURSOR_CHAIR, IDC_CURSOR_BUY, IDC_CURSOR_SELL, IDC_CURSOR_CAMERA_ROTATE, IDC_CURSOR_HSIZE, IDC_CURSOR_VSIZE, IDC_CURSOR_HVSIZE});
    
		m_CursorHandleMap.clear();
    
		for (int LaniatusDefVariables = 0; LaniatusDefVariables < CURSOR_COUNT; ++i)
		{
			IntPtr hCursor = LoadImage(ms_hInstance, MAKEINTRESOURCE(ResourceID[i]), IMAGE_CURSOR, 32, 32, LR_VGACOLOR);
    
			if (null == hCursor)
			{
				return false;
			}
    
			m_CursorHandleMap.insert(TCursorHandleMap.value_type(i, hCursor));
		}
    
		NANOEND return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void DestroyCursors()
	{
		TCursorHandleMap.iterator itor = new TCursorHandleMap.iterator();
		for (itor = m_CursorHandleMap.begin(); itor != m_CursorHandleMap.end(); ++itor)
		{
			DestroyCursor((IntPtr) itor.second);
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetCursorVisible(bool bFlag, bool bLiarCursorOn)
	{
		m_bCursorVisible = bFlag;
		m_bLiarCursorOn = bLiarCursorOn;
    
		if (CURSOR_MODE_HARDWARE == m_iCursorMode)
		{
			int iShowNum;
			if (false == m_bCursorVisible)
			{
				do
				{
					iShowNum = ShowCursor(m_bCursorVisible);
				} while (iShowNum >= 0);
			}
			else
			{
				do
				{
					iShowNum = ShowCursor(m_bCursorVisible);
				} while (iShowNum < 0);
			}
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool GetCursorVisible()
	{
		return m_bCursorVisible;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool GetLiarCursorOn()
	{
		return m_bLiarCursorOn;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public int GetCursorMode()
	{
		return m_iCursorMode;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool __IsContinuousChangeTypeCursor(int iCursorNum)
	{
		switch (iCursorNum)
		{
			case CURSOR_SHAPE_NORMAL:
			case CURSOR_SHAPE_ATTACK:
			case CURSOR_SHAPE_TARGET:
			case CURSOR_SHAPE_MAGIC:
			case CURSOR_SHAPE_BUY:
			case CURSOR_SHAPE_SELL:
				return true;
				break;
		}
    
		return false;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SetCursorNum(int iCursorNum)
	{
		if (CURSOR_SHAPE_NORMAL == iCursorNum)
		{
			if (!__IsContinuousChangeTypeCursor(m_iCursorNum))
			{
				iCursorNum = m_iContinuousCursorNum;
			}
		}
		else
		{
			if (__IsContinuousChangeTypeCursor(m_iCursorNum))
			{
				m_iContinuousCursorNum = m_iCursorNum;
			}
		}
    
		if (CURSOR_MODE_HARDWARE == m_iCursorMode)
		{
			TCursorHandleMap.iterator itor = m_CursorHandleMap.find(iCursorNum);
			if (m_CursorHandleMap.end() == itor)
			{
				return false;
			}
    
			IntPtr hCursor = (IntPtr)itor.second;
    
			SetCursor(hCursor);
			m_hCurrentCursor = hCursor;
		}
    
		m_iCursorNum = iCursorNum;
    
		PyCallClassMemberFunc(m_poMouseHandler, "ChangeCursor", Py_BuildValue("(i)", m_iCursorNum));
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetCursorMode(int iMode)
	{
		switch (iMode)
		{
			case CURSOR_MODE_HARDWARE:
				m_iCursorMode = CURSOR_MODE_HARDWARE;
				ShowCursor(true);
				break;
    
			case CURSOR_MODE_SOFTWARE:
				m_iCursorMode = CURSOR_MODE_SOFTWARE;
				SetCursor(null);
				ShowCursor(false);
				break;
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void OnCameraUpdate()
	{
		if (m_pyBackground.IsMapReady())
		{
			CCamera pkCameraMgr = CCameraManager.Instance().GetCurrentCamera();
			if (pkCameraMgr != null)
			{
				pkCameraMgr.Update();
			}
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void OnUIUpdate()
	{
		UI.CWindowManager rkUIMgr = UI.CWindowManager.Instance();
		rkUIMgr.Update();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void OnUIRender()
	{
		UI.CWindowManager rkUIMgr = UI.CWindowManager.Instance();
		rkUIMgr.Render();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void OnSizeChange(int width, int height)
	{
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void OnMouseMiddleButtonDown(int x, int y)
	{
		CCameraManager rkCmrMgr = CCameraManager.Instance();
		CCamera pkCmrCur = rkCmrMgr.GetCurrentCamera();
		if (pkCmrCur != null)
		{
			pkCmrCur.BeginDrag(x, y);
		}
    
		if (!m_pyBackground.IsMapReady())
		{
			return;
		}
    
		SetCursorNum(CAMERA_ROTATE);
		if (CURSOR_MODE_HARDWARE == GetCursorMode())
		{
			SetCursorVisible(false, true);
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void OnMouseMiddleButtonUp(int x, int y)
	{
		CCameraManager rkCmrMgr = CCameraManager.Instance();
		CCamera pkCmrCur = rkCmrMgr.GetCurrentCamera();
		if (pkCmrCur != null)
		{
			pkCmrCur.EndDrag();
		}
    
		if (!m_pyBackground.IsMapReady())
		{
			return;
		}
    
		SetCursorNum(NORMAL);
		if (CURSOR_MODE_HARDWARE == GetCursorMode())
		{
			SetCursorVisible(true);
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void OnMouseWheel(int nLen)
	{
		UI.CWindowManager rkWndMgr = UI.CWindowManager.Instance();
		if (!rkWndMgr.RunMouseWheel(nLen))
		{
			CCameraManager rkCmrMgr = CCameraManager.Instance();
			CCamera pkCmrCur = rkCmrMgr.GetCurrentCamera();
			if (pkCmrCur != null)
			{
				pkCmrCur.Wheel(nLen);
			}
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void OnMouseMove(int x, int y)
	{
		CCameraManager rkCmrMgr = CCameraManager.Instance();
		CCamera pkCmrCur = rkCmrMgr.GetCurrentCamera();
    
		POINT Point = new POINT();
		if (pkCmrCur != null)
		{
			if (CPythonBackground.Instance().IsMapReady() && pkCmrCur.Drag(x, y, Point))
			{
				x = Point.x;
				y = Point.y;
				ClientToScreen(m_hWnd, Point);
				SetCursorPos(Point.x, Point.y);
    
			}
		}
    
		RECT rcWnd = new RECT();
		GetClientRect(rcWnd);
    
		UI.CWindowManager rkWndMgr = UI.CWindowManager.Instance();
		rkWndMgr.SetResolution(rcWnd.right - rcWnd.left, rcWnd.bottom - rcWnd.top);
    
		rkWndMgr.RunMouseMove(x, y);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void OnMouseLeftButtonDown(int x, int y)
	{
		UI.CWindowManager rkWndMgr = UI.CWindowManager.Instance();
		rkWndMgr.RunMouseLeftButtonDown(x, y);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void OnMouseLeftButtonUp(int x, int y)
	{
		UI.CWindowManager rkWndMgr = UI.CWindowManager.Instance();
		rkWndMgr.RunMouseLeftButtonUp(x, y);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void OnMouseLeftButtonDoubleClick(int x, int y)
	{
		UI.CWindowManager rkWndMgr = UI.CWindowManager.Instance();
		rkWndMgr.RunMouseLeftButtonDown(x, y);
		rkWndMgr.RunMouseLeftButtonDoubleClick(x, y);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void OnMouseRightButtonDown(int x, int y)
	{
		UI.CWindowManager rkWndMgr = UI.CWindowManager.Instance();
		rkWndMgr.RunMouseRightButtonDown(x, y);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void OnMouseRightButtonUp(int x, int y)
	{
		UI.CWindowManager rkWndMgr = UI.CWindowManager.Instance();
		rkWndMgr.RunMouseRightButtonUp(x, y);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void OnKeyDown(int iIndex)
	{
		UI.CWindowManager rkWndMgr = UI.CWindowManager.Instance();
    
		if (DIK_ESCAPE == iIndex)
		{
			rkWndMgr.RunPressEscapeKey();
		}
    
		rkWndMgr.RunKeyDown(iIndex);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void OnKeyUp(int iIndex)
	{
		UI.CWindowManager rkWndMgr = UI.CWindowManager.Instance();
		rkWndMgr.RunKeyUp(iIndex);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void RunIMEUpdate()
	{
		UI.CWindowManager rkWndMgr = UI.CWindowManager.Instance();
		rkWndMgr.RunIMEUpdate();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void RunIMETabEvent()
	{
		UI.CWindowManager rkWndMgr = UI.CWindowManager.Instance();
		rkWndMgr.RunIMETabEvent();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void RunIMEReturnEvent()
	{
		UI.CWindowManager rkWndMgr = UI.CWindowManager.Instance();
		rkWndMgr.RunIMEReturnEvent();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void OnIMEKeyDown(int iIndex)
	{
		UI.CWindowManager rkWndMgr = UI.CWindowManager.Instance();
		rkWndMgr.RunIMEKeyDown(iIndex);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void RunIMEChangeCodePage()
	{
		UI.CWindowManager rkWndMgr = UI.CWindowManager.Instance();
		rkWndMgr.RunChangeCodePage();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void RunIMEOpenCandidateListEvent()
	{
		UI.CWindowManager rkWndMgr = UI.CWindowManager.Instance();
		rkWndMgr.RunOpenCandidate();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void RunIMECloseCandidateListEvent()
	{
		UI.CWindowManager rkWndMgr = UI.CWindowManager.Instance();
		rkWndMgr.RunCloseCandidate();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void RunIMEOpenReadingWndEvent()
	{
		UI.CWindowManager rkWndMgr = UI.CWindowManager.Instance();
		rkWndMgr.RunOpenReading();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void RunIMECloseReadingWndEvent()
	{
		UI.CWindowManager rkWndMgr = UI.CWindowManager.Instance();
		rkWndMgr.RunCloseReading();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void RunPressExitKey()
	{
		UI.CWindowManager rkWndMgr = UI.CWindowManager.Instance();
		rkWndMgr.RunPressExitKey();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void OnMouseUpdate()
	{
	#if DEBUG
		if (!m_poMouseHandler)
		{
			return;
		}
	#endif DEBUG
    
		UI.CWindowManager rkWndMgr = UI.CWindowManager.Instance();
		int lx;
		int ly;
		rkWndMgr.GetMousePosition(lx, ly);
		PyCallClassMemberFunc(m_poMouseHandler, "Update", Py_BuildValue("(ii)", lx, ly));
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void OnMouseRender()
	{
	#if DEBUG
		if (!m_poMouseHandler)
		{
			return;
		}
	#endif DEBUG
    
		PyCallClassMemberFunc(m_poMouseHandler, "Render", Py_BuildValue("()"));
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public int OnLogoOpen(ref string szName)
	{
		m_pLogoTex = null;
		m_pLogoTex = new CGraphicImageTexture();
		m_pCaptureBuffer = null;
		m_lBufferSize = 0;
		m_bLogoError = true;
		m_bLogoPlay = false;
    
		m_pGraphBuilder = null;
		m_pFilterSG = null;
		m_pSampleGrabber = null;
		m_pMediaCtrl = null;
		m_pMediaEvent = null;
		m_pVideoWnd = null;
		m_pBasicVideo = null;
    
		m_nLeft = 0;
		m_nRight = 0;
		m_nTop = 0;
		m_nBottom = 0;
    
		if (!m_pLogoTex.Create(1, 1, D3DFMT_A8R8G8B8))
		{
			return 0;
		}
    
		if (FAILED(CoCreateInstance(CLSID_FilterGraph, null, CLSCTX_INPROC_SERVER, IID_IGraphBuilder, (object)(m_pGraphBuilder))))
		{
			return 0;
		}
		if (FAILED(CoCreateInstance(CLSID_SampleGrabber, null, CLSCTX_INPROC_SERVER, IID_IBaseFilter, (object) & m_pFilterSG)))
		{
			return 0;
		}
		if (FAILED(m_pGraphBuilder.AddFilter(m_pFilterSG, "SampleGrabber")))
		{
			return 0;
		}
    
		AM_MEDIA_TYPE mediaType = new AM_MEDIA_TYPE();
		ZeroMemory(mediaType, sizeof(AM_MEDIA_TYPE));
		mediaType.majortype = MEDIATYPE_Video;
		mediaType.subtype = MEDIASUBTYPE_RGB32;
		if (FAILED(m_pFilterSG.QueryInterface(IID_ISampleGrabber, (object) & m_pSampleGrabber)))
		{
			return 0;
		}
		if (FAILED(m_pSampleGrabber.SetMediaType(mediaType)))
		{
			return 0;
		}
    
		string wFileName = new string(new char[MAX_PATH]);
		MultiByteToWideChar(CP_ACP, 0, szName, -1, wFileName, MAX_PATH);
		if (FAILED(m_pGraphBuilder.RenderFile(wFileName, null)))
		{
			return 0;
		}
    
		IBaseFilter pSrc;
		m_pGraphBuilder.AddSourceFilter(wFileName, "Source", pSrc);
    
		if (FAILED(m_pGraphBuilder.QueryInterface(IID_IMediaControl, (object) & m_pMediaCtrl)))
		{
			return 0;
		}
    
		if (FAILED(m_pGraphBuilder.QueryInterface(IID_IVideoWindow, (object) & m_pVideoWnd)))
		{
			return 0;
		}
		if (FAILED(m_pVideoWnd.put_MessageDrain((OAHWND)this.m_hWnd)))
		{
			return 0;
		}
    
		if (FAILED(m_pGraphBuilder.QueryInterface(IID_IBasicVideo, (object) & m_pBasicVideo)))
		{
			return 0;
		}
    
		if (FAILED(m_pGraphBuilder.QueryInterface(IID_IMediaEventEx, (object) & m_pMediaEvent)))
		{
			return 0;
		}
    
		m_pVideoWnd.SetWindowPosition(3000, 3000, 0, 0);
		m_pVideoWnd.put_Visible(0);
		m_pSampleGrabber.SetBufferSamples(true);
    
		m_pVideoWnd.put_Owner((OAHWND)m_hWnd);
		m_pMediaEvent.SetNotifyWindow((OAHWND)m_hWnd, WM_APP + 1, 0);
    
		bInitializedLogo = true;
    
		return 1;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public int OnLogoUpdate()
	{
		if (m_pGraphBuilder == null || m_pFilterSG == null || m_pSampleGrabber == null || m_pMediaCtrl == null || m_pMediaEvent == null || m_pVideoWnd == null || false == bInitializedLogo)
		{
			return 0;
		}
    
	//# Laniatus Games Studio Inc. | TODO TASK: C# does not have an equivalent to pointers to value types:
	//Original Metin2 CPlus Line: byte* pBuffer = m_pCaptureBuffer;
		byte pBuffer = m_pCaptureBuffer;
		int lBufferSize = m_lBufferSize;
    
		if (!m_bLogoPlay)
		{
			m_pMediaCtrl.Run();
			m_bLogoPlay = true;
		}
    
		if (lBufferSize == 0)
		{
			m_pSampleGrabber.GetCurrentBuffer(m_lBufferSize, null);
    
			SAFE_DELETE_ARRAY(m_pCaptureBuffer);
			m_pCaptureBuffer = new byte[m_lBufferSize];
			pBuffer = m_pCaptureBuffer;
			lBufferSize = m_lBufferSize;
		}
    
		if (FAILED(m_pSampleGrabber.GetCurrentBuffer(m_lBufferSize, (int)m_pCaptureBuffer)))
		{
			m_bLogoError = true;
    
			LPDIRECT3DTEXTURE8 tex = m_pLogoTex.GetD3DTexture();
			D3DLOCKED_RECT rt = new D3DLOCKED_RECT();
			ZeroMemory(rt, sizeof(D3DLOCKED_RECT));
    
			tex.LockRect(0, rt, 0, 0);
			byte[] destb = (byte)rt.pBits;
			for (int a = 0; a < 4; a += 4)
			{
				byte[] dest = destb[a];
				dest[0] = 0;
				dest[1] = 0;
				dest[2] = 0;
				dest[3] = 0xff;
			}
			tex.UnlockRect(0);
    
			return 1;
		}
    
		m_bLogoError = false;
    
		int lWidth;
		int lHeight;
		m_pBasicVideo.GetVideoSize(lWidth, lHeight);
    
		if (lWidth >= lHeight)
		{
			m_nLeft = 0;
			m_nRight = this.GetWidth();
			m_nTop = (this.GetHeight() >> 1) - ((this.GetWidth() * lHeight / lWidth) >> 1);
			m_nBottom = (this.GetHeight() >> 1) + ((this.GetWidth() * lHeight / lWidth) >> 1);
		}
		else
		{
			m_nTop = 0;
			m_nBottom = this.GetHeight();
			m_nLeft = (this.GetWidth() >> 1) - ((this.GetHeight() * lWidth / lHeight) >> 1);
			m_nRight = (this.GetWidth() >> 1) - ((this.GetHeight() * lWidth / lHeight) >> 1);
		}
    
		if (m_pLogoTex.GetWidth() == 1)
		{
			m_pLogoTex.Destroy();
			m_pLogoTex.Create(lWidth, lHeight, D3DFMT_A8R8G8B8);
    
		}
    
		LPDIRECT3DTEXTURE8 tex = m_pLogoTex.GetD3DTexture();
		D3DLOCKED_RECT rt = new D3DLOCKED_RECT();
		ZeroMemory(rt, sizeof(D3DLOCKED_RECT));
    
		tex.LockRect(0, rt, 0, 0);
		byte[] destb = (byte)rt.pBits;
		for (int a = 0; a < lBufferSize; a += 4)
		{
			byte[] src = &m_pCaptureBuffer[a];
			byte[] dest = destb[a];
			dest[0] = src[0];
			dest[1] = src[1];
			dest[2] = src[2];
			dest[3] = 0xff;
		}
		tex.UnlockRect(0);
    
		int evCode;
		int param1;
		int param2;
		while (SUCCEEDED(m_pMediaEvent.GetEvent(evCode, param1, param2, 0)))
		{
			switch (evCode)
			{
			case EC_COMPLETE:
				return 0;
			case EC_USERABORT:
				return 0;
			case EC_ERRORABORT:
				return 0;
			}
    
			m_pMediaEvent.FreeEventParams(evCode, param1, param2);
		}
    
		if ((GetAsyncKeyState(VK_ESCAPE) & 0x8000) != 0)
		{
			return 0;
		}
    
		return 1;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void OnLogoRender()
	{
		if (!m_pLogoTex.IsEmpty() && !m_bLogoError && true == bInitializedLogo)
		{
			(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_MINFILTER, D3DTEXF_LINEAR);
			(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_MAGFILTER, D3DTEXF_LINEAR);
			m_pLogoTex.SetTextureStage(0);
			CPythonGraphic.instance().RenderTextureBox(m_nLeft, m_nTop, m_nRight, m_nBottom, 0.0f, 0.0f, 1.0f, 1.0f, 0.0f);
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void OnLogoClose()
	{
		if (false == bInitializedLogo)
		{
			return;
		}
    
		if (m_pCaptureBuffer != null)
		{
			m_pCaptureBuffer = null;
			m_pCaptureBuffer = null;
		}
		if (m_pLogoTex != null)
		{
			m_pLogoTex.Destroy();
			m_pLogoTex = null;
			m_pLogoTex = null;
		}
    
		if (m_pMediaEvent != null)
		{
			m_pMediaEvent.SetNotifyWindow(null, 0, 0);
			m_pMediaEvent.Release();
			m_pMediaEvent = null;
		}
		if (m_pBasicVideo != null)
		{
			m_pBasicVideo.Release();
		}
		m_pBasicVideo = null;
		if (m_pVideoWnd != null)
		{
			m_pVideoWnd.Release();
		}
		m_pVideoWnd = null;
		if (m_pMediaCtrl != null)
		{
			m_pMediaCtrl.Release();
		}
		m_pMediaCtrl = null;
		if (m_pSampleGrabber != null)
		{
			m_pSampleGrabber.Release();
		}
		m_pSampleGrabber = null;
		if (m_pFilterSG != null)
		{
			m_pFilterSG.Release();
		}
		m_pFilterSG = null;
		if (m_pGraphBuilder != null)
		{
			m_pGraphBuilder.Release();
		}
		m_pGraphBuilder = null;
    
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_MINFILTER, D3DTEXF_POINT);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_MAGFILTER, D3DTEXF_POINT);
    
    
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SafeSetCapture()
	{
		SetCapture(m_hWnd);
		gs_nMouseCaptureRef++;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SafeReleaseCapture()
	{
		gs_nMouseCaptureRef--;
		if (gs_nMouseCaptureRef == 0)
		{
			ReleaseCapture();
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __SetFullScreenWindow(IntPtr hWnd, uint dwWidth, uint dwHeight, uint dwBPP)
	{
		DEVMODE DevMode = new DEVMODE();
		DevMode.dmSize = sizeof(DEVMODE);
		DevMode.dmBitsPerPel = dwBPP;
		DevMode.dmPelsWidth = dwWidth;
		DevMode.dmPelsHeight = dwHeight;
		DevMode.dmFields = DM_BITSPERPEL | DM_PELSWIDTH | DM_PELSHEIGHT;
    
		int Error = ChangeDisplaySettings(DevMode, CDS_FULLSCREEN);
		if (Error == DISP_CHANGE_RESTART)
		{
			ChangeDisplaySettings(0,0);
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __MinimizeFullScreenWindow(IntPtr hWnd, uint dwWidth, uint dwHeight)
	{
		ChangeDisplaySettings(0, 0);
		SetWindowPos(hWnd, 0, 0, 0, dwWidth, dwHeight, SWP_SHOWWINDOW);
		ShowWindow(hWnd, SW_MINIMIZE);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public int WindowProcedure(IntPtr hWnd, uint uiMsg, IntPtr wParam, IntPtr lParam)
	{
		const int c_DoubleClickTime = 300;
		const int c_DoubleClickBox = 5;
	//# Laniatus Games Studio Inc. |: This static local variable declaration (not allowed in C#) has been moved just prior to the method:
	//	static int s_xDownPosition = 0;
	//# Laniatus Games Studio Inc. |: This static local variable declaration (not allowed in C#) has been moved just prior to the method:
	//	static int s_yDownPosition = 0;
    
		switch (uiMsg)
		{
			case WM_ACTIVATEAPP:
			{
					m_isActivateWnd = (wParam == WA_ACTIVE) || (wParam == WA_CLICKACTIVE);
    
					if (m_isActivateWnd)
					{
						m_SoundManager.RestoreVolume();
    
						if (m_isWindowFullScreenEnable)
						{
							__SetFullScreenWindow(hWnd, m_dwWidth, m_dwHeight, m_pySystem.GetBPP());
						}
					}
					else
					{
						m_SoundManager.SaveVolume();
    
						if (m_isWindowFullScreenEnable)
						{
							__MinimizeFullScreenWindow(hWnd, m_dwWidth, m_dwHeight);
						}
					}
			}
				break;
    
			case WM_INPUTLANGCHANGE:
				return CPythonIME.Instance().WMInputLanguage(hWnd, uiMsg, wParam, lParam);
				break;
    
			case WM_IME_STARTCOMPOSITION:
				return CPythonIME.Instance().WMStartComposition(hWnd, uiMsg, wParam, lParam);
				break;
    
			case WM_IME_COMPOSITION:
				return CPythonIME.Instance().WMComposition(hWnd, uiMsg, wParam, lParam);
				break;
    
			case WM_IME_ENDCOMPOSITION:
				return CPythonIME.Instance().WMEndComposition(hWnd, uiMsg, wParam, lParam);
				break;
    
			case WM_IME_NOTIFY:
				return CPythonIME.Instance().WMNotify(hWnd, uiMsg, wParam, lParam);
				break;
    
			case WM_IME_SETCONTEXT:
				lParam &= ~(ISC_SHOWUICOMPOSITIONWINDOW | ISC_SHOWUIALLCANDIDATEWINDOW);
				break;
    
			case WM_CHAR:
				return CPythonIME.Instance().WMChar(hWnd, uiMsg, wParam, lParam);
				break;
    
			case WM_KEYDOWN:
				OnIMEKeyDown(((U16)((U32)wParam)));
				break;
    
			case WM_LBUTTONDOWN:
				SafeSetCapture();
    
				if (ELTimer_GetMSec() - m_dwLButtonDownTime < c_DoubleClickTime && Math.Abs(((U16)((U32)lParam)) - WindowProcedure_s_xDownPosition) < c_DoubleClickBox && Math.Abs((((U32)lParam)>>16) - WindowProcedure_s_yDownPosition) < c_DoubleClickBox)
				{
					m_dwLButtonDownTime = 0;
    
					OnMouseLeftButtonDoubleClick((short)((U16)((U32)lParam)), (short)(((U32)lParam) >> 16));
				}
				else
				{
					m_dwLButtonDownTime = ELTimer_GetMSec();
    
					OnMouseLeftButtonDown((short)((U16)((U32)lParam)), (short)(((U32)lParam) >> 16));
				}
    
				WindowProcedure_s_xDownPosition = ((U16)((U32)lParam));
				WindowProcedure_s_yDownPosition = (((U32)lParam) >> 16);
				return 0;
    
			case WM_LBUTTONUP:
				m_dwLButtonUpTime = ELTimer_GetMSec();
    
				if (hWnd == GetCapture())
				{
					SafeReleaseCapture();
					OnMouseLeftButtonUp((short)((U16)((U32)lParam)), (short)(((U32)lParam) >> 16));
				}
				return 0;
    
			case WM_MBUTTONDOWN:
				SafeSetCapture();
    
				UI.CWindowManager.Instance().RunMouseMiddleButtonDown((short)((U16)((U32)lParam)), (short)(((U32)lParam) >> 16));
				break;
    
			case WM_MBUTTONUP:
				if (GetCapture() == hWnd)
				{
					SafeReleaseCapture();
    
					UI.CWindowManager.Instance().RunMouseMiddleButtonUp((short)((U16)((U32)lParam)), (short)(((U32)lParam) >> 16));
				}
				break;
    
			case WM_RBUTTONDOWN:
				SafeSetCapture();
				OnMouseRightButtonDown((short)((U16)((U32)lParam)), (short)(((U32)lParam) >> 16));
				return 0;
    
			case WM_RBUTTONUP:
				if (hWnd == GetCapture())
				{
					SafeReleaseCapture();
    
					OnMouseRightButtonUp((short)((U16)((U32)lParam)), (short)(((U32)lParam) >> 16));
				}
				return 0;
    
			case 0x20a:
				if (CefWebBrowser_IsVisible())
				{
				}
				else
				{
					OnMouseWheel((short)(((U32)wParam) >> 16));
				}
				break;
    
			case WM_SIZE:
				switch (wParam)
				{
					case SIZE_RESTORED:
					case SIZE_MAXIMIZED:
					{
							RECT rcWnd = new RECT();
							GetClientRect(rcWnd);
    
							uint uWidth = rcWnd.right - rcWnd.left;
							uint uHeight = rcWnd.bottom - rcWnd.left;
							m_grpDevice.ResizeBackBuffer(uWidth, uHeight);
					}
						break;
				}
    
				if (wParam == SIZE_MINIMIZED)
				{
					m_isMinimizedWnd = true;
				}
				else
				{
					m_isMinimizedWnd = false;
				}
    
				OnSizeChange((short)((U16)((U32)lParam)), (short)(((U32)lParam) >> 16));
    
				break;
    
			case WM_EXITSIZEMOVE:
			{
					RECT rcWnd = new RECT();
					GetClientRect(rcWnd);
    
					uint uWidth = rcWnd.right - rcWnd.left;
					uint uHeight = rcWnd.bottom - rcWnd.left;
					m_grpDevice.ResizeBackBuffer(uWidth, uHeight);
					OnSizeChange((short)((U16)((U32)lParam)), (short)(((U32)lParam) >> 16));
			}
				break;
    
			case WM_SYSKEYDOWN:
				switch (((U16)((U32)wParam)))
				{
					case VK_F10:
						break;
				}
				break;
    
			case WM_SYSKEYUP:
				switch (((U16)((U32)wParam)))
				{
					case 18:
						return false ? 1 : 0;
						break;
					case VK_F10:
						break;
				}
				break;
    
			case WM_SETCURSOR:
				if (IsActive())
				{
					if (m_bCursorVisible && CURSOR_MODE_HARDWARE == m_iCursorMode)
					{
						SetCursor((IntPtr) m_hCurrentCursor);
						return 0;
					}
					else
					{
						SetCursor(((object)0));
						return 0;
					}
				}
				break;
    
			case WM_CLOSE:
	#if DEBUG
				PostQuitMessage(0);
	#else
				RunPressExitKey();
	#endif
				return 0;
    
			case WM_DESTROY:
				return 0;
			default:
				break;
		}
    
		return CMSApplication.WindowProcedure(hWnd, uiMsg, wParam, lParam);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool IsWebPageMode()
	{
		return CefWebBrowser_IsVisible() ? true : false;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void ShowWebPage(string c_szURL, in RECT c_rcWebPage)
	{
		if (CefWebBrowser_IsVisible())
		{
			return;
		}
    
		m_grpDevice.EnableWebBrowserMode(c_rcWebPage);
		if (!CefWebBrowser_Show(GetWindowHandle(), c_szURL, c_rcWebPage))
		{
			TraceError("CREATE_WEBBROWSER_ERROR:%d", GetLastError());
		}
    
		SetCursorMode(CURSOR_MODE_HARDWARE);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void MoveWebPage(in RECT c_rcWebPage)
	{
		if (CefWebBrowser_IsVisible())
		{
			m_grpDevice.MoveWebBrowserRect(c_rcWebPage);
			CefWebBrowser_Move(c_rcWebPage);
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void HideWebPage()
	{
		if (CefWebBrowser_IsVisible())
		{
			CefWebBrowser_Hide();
    
			m_grpDevice.DisableWebBrowserMode();
    
			if (m_pySystem.IsSoftwareCursor())
			{
				SetCursorMode(CURSOR_MODE_SOFTWARE);
			}
			else
			{
				SetCursorMode(CURSOR_MODE_HARDWARE);
			}
		}
	}
}