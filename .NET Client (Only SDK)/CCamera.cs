public class CCamera
{
//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void ProcessTerrainCollision()
	{
		CPythonBackground rPythonBackground = CPythonBackground.Instance();
		_D3DVECTOR v3CollisionPoint = new _D3DVECTOR();
    
		if (rPythonBackground.GetPickingPointWithRayOnlyTerrain(m_kTargetToCameraBottomRay, v3CollisionPoint))
		{
			SetCameraState(CAMERA_STATE_CANTGODOWN);
			_D3DVECTOR v3CheckVector = m_v3Eye - 2.0f * m_fTerrainCollisionRadius * m_v3Up;
			v3CheckVector.z = rPythonBackground.GetHeight(floorf(v3CheckVector.x), floorf(v3CheckVector.y));
			_D3DVECTOR v3NewEye = v3CheckVector + 2.0f * m_fTerrainCollisionRadius * m_v3Up;
			if (v3NewEye.z > m_v3Eye.z)
			{
				SetEye(v3NewEye);
			}
		}
		else
		{
			SetCameraState(CAMERA_STATE_NORMAL);
		}
    
		if (rPythonBackground.GetPickingPointWithRayOnlyTerrain(m_kCameraBottomToTerrainRay, v3CollisionPoint))
		{
			SetCameraState(CAMERA_STATE_CANTGODOWN);
			if (D3DXVec3Length((m_v3Eye - v3CollisionPoint)) < 2.0f * m_fTerrainCollisionRadius)
			{
				_D3DVECTOR v3NewEye = v3CollisionPoint + 2.0f * m_fTerrainCollisionRadius * m_v3Up;
				SetEye(v3NewEye);
			}
		}
		else
		{
			SetCameraState(CAMERA_STATE_NORMAL);
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void ProcessBuildingCollision()
	{
		float fMoveAmountSmall = 2.0f;
		float fMoveAmountLarge = 4.0f;
    
		_D3DVECTOR v3CheckVector = new _D3DVECTOR();
    
		CDynamicSphereInstance s = new CDynamicSphereInstance();
		s.fRadius = m_fObjectCollisionRadius;
		s.v3LastPosition = m_v3Eye;
    
		Vector3d aVector3d = new Vector3d();
		aVector3d.Set(m_v3Eye.x, m_v3Eye.y, m_v3Eye.z);
    
		CCullingManager rkCullingMgr = CCullingManager.Instance();
    
		{
			v3CheckVector = m_v3Eye - m_fObjectCollisionRadius * m_v3View;
			s.v3Position = v3CheckVector;
    
			List<_D3DVECTOR> kVct_kPosition = new List<_D3DVECTOR>();
			CameraCollisionChecker kCameraCollisionChecker = new CameraCollisionChecker(s, kVct_kPosition);
			rkCullingMgr.ForInRange(aVector3d, m_fObjectCollisionRadius, kCameraCollisionChecker);
			bool bCollide = kCameraCollisionChecker.m_isBlocked;
    
			if (bCollide)
			{
				if (m_v3AngularVelocity.y > 0.0f)
				{
					m_v3AngularVelocity.y = 0.0f;
					m_v3AngularVelocity.z += fMoveAmountLarge;
				}
    
				if (kVct_kPosition.Count > 1)
				{
					 m_v3AngularVelocity.z += fMoveAmountSmall;
				}
				else
				{
					D3DXVec3Cross(v3CheckVector, (kVct_kPosition[0] - m_v3Eye), m_v3View);
					float fDot = D3DXVec3Dot(v3CheckVector, m_v3Up);
					if (fDot < 0F)
					{
						 m_v3AngularVelocity.x -= fMoveAmountSmall;
					}
					else if (fDot > 0F)
					{
						 m_v3AngularVelocity.x += fMoveAmountSmall;
					}
					else
					{
						 m_v3AngularVelocity.z += fMoveAmountSmall;
					}
				}
			}
		}
    
		{
			v3CheckVector = m_v3Eye + 2.0f * m_fObjectCollisionRadius * m_v3Up;
			s.v3Position = v3CheckVector;
    
			List<_D3DVECTOR> kVct_kPosition = new List<_D3DVECTOR>();
			CameraCollisionChecker kCameraCollisionChecker = new CameraCollisionChecker(s, kVct_kPosition);
			rkCullingMgr.ForInRange(aVector3d, m_fObjectCollisionRadius, kCameraCollisionChecker);
			bool bCollide = kCameraCollisionChecker.m_isBlocked;
    
			if (bCollide)
			{
				m_v3AngularVelocity.z = fMIN(-fMoveAmountSmall, m_v3AngularVelocity.y);
			}
		}
    
		{
			v3CheckVector = m_v3Eye + 3.0f * m_fObjectCollisionRadius * m_v3Cross;
			s.v3Position = v3CheckVector;
    
			List<_D3DVECTOR> kVct_kPosition = new List<_D3DVECTOR>();
			CameraCollisionChecker kCameraCollisionChecker = new CameraCollisionChecker(s, kVct_kPosition);
			rkCullingMgr.ForInRange(aVector3d, m_fObjectCollisionRadius, kCameraCollisionChecker);
			bool bCollide = kCameraCollisionChecker.m_isBlocked;
    
			if (bCollide)
			{
				if (m_v3AngularVelocity.x > 0.0f)
				{
					m_v3AngularVelocity.x = 0.0f;
					m_v3AngularVelocity.y += fMoveAmountLarge;
				}
			}
		}
    
		{
			v3CheckVector = m_v3Eye - 3.0f * m_fObjectCollisionRadius * m_v3Cross;
			s.v3Position = v3CheckVector;
    
			List<_D3DVECTOR> kVct_kPosition = new List<_D3DVECTOR>();
			CameraCollisionChecker kCameraCollisionChecker = new CameraCollisionChecker(s, kVct_kPosition);
			rkCullingMgr.ForInRange(aVector3d, m_fObjectCollisionRadius, kCameraCollisionChecker);
			bool bCollide = kCameraCollisionChecker.m_isBlocked;
    
			if (bCollide)
			{
				if (m_v3AngularVelocity.x < 0.0f)
				{
					m_v3AngularVelocity.x = 0.0f;
					m_v3AngularVelocity.y += fMoveAmountLarge;
				}
			}
		}
    
		{
			v3CheckVector = m_v3Eye - 2.0f * m_fTerrainCollisionRadius * m_v3Up;
			s.v3Position = v3CheckVector;
    
			List<_D3DVECTOR> kVct_kPosition = new List<_D3DVECTOR>();
			CameraCollisionChecker kCameraCollisionChecker = new CameraCollisionChecker(s, kVct_kPosition);
			rkCullingMgr.ForInRange(aVector3d, m_fObjectCollisionRadius, kCameraCollisionChecker);
			bool bCollide = kCameraCollisionChecker.m_isBlocked;
    
			if (bCollide)
			{
				if (m_v3AngularVelocity.z < 0.0f)
				{
					m_v3AngularVelocity.z = 0.0f;
					m_v3AngularVelocity.y += fMoveAmountLarge;
				}
			}
		}
    
		{
			v3CheckVector = m_v3Eye + 4.0f * m_fObjectCollisionRadius * m_v3View;
			s.v3Position = v3CheckVector;
    
			List<_D3DVECTOR> kVct_kPosition = new List<_D3DVECTOR>();
			CameraCollisionChecker kCameraCollisionChecker = new CameraCollisionChecker(s, kVct_kPosition);
			rkCullingMgr.ForInRange(aVector3d, m_fObjectCollisionRadius, kCameraCollisionChecker);
			bool bCollide = kCameraCollisionChecker.m_isBlocked;
    
			if (bCollide)
			{
				if (m_v3AngularVelocity.y < 0.0f)
				{
					m_v3AngularVelocity.y = 0.0f;
					m_v3AngularVelocity.z += fMoveAmountLarge;
				}
    
				if (kVct_kPosition.Count > 1)
				{
					 m_v3AngularVelocity.z += fMoveAmountLarge;
				}
				else
				{
					D3DXVec3Cross(v3CheckVector, (kVct_kPosition[0] - m_v3Eye), m_v3View);
					float fDot = D3DXVec3Dot(v3CheckVector, m_v3Up);
					if (fDot < 0F)
					{
						m_v3AngularVelocity.x -= fMoveAmountSmall;
					}
					else if (fDot > 0F)
					{
						m_v3AngularVelocity.x += fMoveAmountSmall;
					}
					else
					{
						m_v3AngularVelocity.z += fMoveAmountSmall;
					}
				}
			}
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void Update()
	{
		RotateEyeAroundTarget(m_v3AngularVelocity.z, m_v3AngularVelocity.x);
    
		float fNewDistance = fMAX(CAMERA_MIN_DISTANCE, fMIN(CAMERA_MAX_DISTANCE, GetDistance() - m_v3AngularVelocity.y));
		SetDistance(fNewDistance);
    
		if (m_bProcessTerrainCollision)
		{
			 ProcessTerrainCollision();
		}
    
		m_v3AngularVelocity *= 0.5f;
		if (Math.Abs(m_v3AngularVelocity.x) < 1.0f)
		{
			m_v3AngularVelocity.x = 0.0f;
		}
		if (Math.Abs(m_v3AngularVelocity.y) < 1.0f)
		{
			m_v3AngularVelocity.y = 0.0f;
		}
		if (Math.Abs(m_v3AngularVelocity.z) < 1.0f)
		{
			m_v3AngularVelocity.z = 0.0f;
		}
    
		float CAMERA_MOVABLE_DISTANCE = CAMERA_MAX_DISTANCE - CAMERA_MIN_DISTANCE;
		float CAMERA_TARGET_DELTA = CAMERA_TARGET_FACE - CAMERA_TARGET_STANDARD;
		float fCameraCurMovableDistance = CAMERA_MAX_DISTANCE - GetDistance();
		float fNewTargetHeight = CAMERA_TARGET_STANDARD + CAMERA_TARGET_DELTA * fCameraCurMovableDistance / CAMERA_MOVABLE_DISTANCE;
    
		SetTargetHeight(fNewTargetHeight);
	}
}