public class CParticleInstance
{
//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void Transform(_D3DMATRIX c_matLocal)
	{
		(CStateManager.Instance()).SetRenderState(D3DRS_TEXTUREFACTOR, m_dcColor);
    
		_D3DVECTOR v3Up = new _D3DVECTOR();
		_D3DVECTOR v3Cross = new _D3DVECTOR();
    
		if (!m_pParticleProperty.m_bStretchFlag)
		{
			CCamera pCurrentCamera = CCameraManager.Instance().GetCurrentCamera();
			_D3DVECTOR c_rv3Up = pCurrentCamera.GetUp();
			_D3DVECTOR c_rv3Cross = pCurrentCamera.GetCross();
    
			_D3DVECTOR v3Rotation = new _D3DVECTOR();
    
			switch (m_pParticleProperty.m_byBillboardType)
			{
			case BILLBOARD_TYPE_LIE:
			{
					float fCos = cosf(((m_fRotation) * (((float) 3.141592654f) / 180.0f)));
					float fSin = sinf(((m_fRotation) * (((float) 3.141592654f) / 180.0f)));
					v3Up.x = fCos;
					v3Up.y = -fSin;
					v3Up.z = 0;
					v3Cross.x = fSin;
					v3Cross.y = fCos;
					v3Cross.z = 0;
			}
				break;
			case BILLBOARD_TYPE_2FACE:
			case BILLBOARD_TYPE_3FACE:
			case BILLBOARD_TYPE_Y:
			{
					v3Up = D3DXVECTOR3(0.0f,0.0f,1.0f);
					_D3DVECTOR c_rv3View = pCurrentCamera.GetView();
					if (v3Up.x * c_rv3View.y - v3Up.y * c_rv3View.x < 0)
					{
						v3Up *= -1;
					}
					D3DXVec3Cross(v3Cross, v3Up, D3DXVECTOR3(c_rv3View.x,c_rv3View.y,0));
					D3DXVec3Normalize(v3Cross, v3Cross);
    
					if (m_fRotation)
					{
						float fCos = -sinf(((m_fRotation) * (((float) 3.141592654f) / 180.0f)));
						float fSin = cosf(((m_fRotation) * (((float) 3.141592654f) / 180.0f)));
    
						_D3DVECTOR v3Temp = v3Up * fCos - v3Cross * fSin;
	//# Laniatus Games Studio Inc. | TODO TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'CopyFrom' method should be created:
	//Original Metin2 CPlus Line: v3Cross = v3Cross * fCos + v3Up * fSin;
						v3Cross.CopyFrom(v3Cross * fCos + v3Up * fSin);
	//# Laniatus Games Studio Inc. | TODO TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'CopyFrom' method should be created:
	//Original Metin2 CPlus Line: v3Up = v3Temp;
						v3Up.CopyFrom(v3Temp);
					}
			}
				break;
			case BILLBOARD_TYPE_ALL:
			default:
			{
					if (m_fRotation == 0.0f)
					{
	//# Laniatus Games Studio Inc. | TODO TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'CopyFrom' method should be created:
	//Original Metin2 CPlus Line: v3Up = -c_rv3Cross;
						v3Up.CopyFrom(-c_rv3Cross);
	//# Laniatus Games Studio Inc. | TODO TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'CopyFrom' method should be created:
	//Original Metin2 CPlus Line: v3Cross = c_rv3Up;
						v3Cross.CopyFrom(c_rv3Up);
					}
					else
					{
						_D3DVECTOR c_rv3View = pCurrentCamera.GetView();
						D3DXQUATERNION q = new D3DXQUATERNION();
						D3DXQUATERNION qc = new D3DXQUATERNION();
						D3DXQuaternionRotationAxis(q, c_rv3View, ((m_fRotation) * (((float) 3.141592654f) / 180.0f)));
						D3DXQuaternionConjugate(qc, q);
    
						{
							D3DXQUATERNION qr = new D3DXQUATERNION(-c_rv3Cross.x, -c_rv3Cross.y, -c_rv3Cross.z, 0);
							D3DXQuaternionMultiply(qr, qc, qr);
							D3DXQuaternionMultiply(qr, qr, q);
							v3Up.x = qr.x;
							v3Up.y = qr.y;
							v3Up.z = qr.z;
						}
						{
							D3DXQUATERNION qr = new D3DXQUATERNION(c_rv3Up.x, c_rv3Up.y, c_rv3Up.z, 0);
							D3DXQuaternionMultiply(qr, qc, qr);
							D3DXQuaternionMultiply(qr, qr, q);
							v3Cross.x = qr.x;
							v3Cross.y = qr.y;
							v3Cross.z = qr.z;
						}
    
					}
			}
				break;
			}
    
		}
		else
		{
			v3Up = m_v3Position - m_v3LastPosition;
    
			if (c_matLocal != null)
			{
				D3DXVec3TransformNormal(v3Up, v3Up, c_matLocal);
			}
    
			float length = D3DXVec3Length(v3Up);
			if (length == 0.0f)
			{
				v3Up = D3DXVECTOR3(0.0f,0.0f,1.0f);
			}
			else
			{
				v3Up *= (1 + Math.Log(1 + length)) / length;
			}
    
			CCamera pCurrentCamera = CCameraManager.Instance().GetCurrentCamera();
			_D3DVECTOR c_rv3View = pCurrentCamera.GetView();
			D3DXVec3Cross(v3Cross, v3Up, c_rv3View);
			D3DXVec3Normalize(v3Cross, v3Cross);
    
		}
    
		v3Cross = -(m_v2HalfSize.x * m_v2Scale.x) * v3Cross;
		v3Up = (m_v2HalfSize.y * m_v2Scale.y) * v3Up;
    
		if (c_matLocal != null && m_pParticleProperty.m_bAttachFlag)
		{
			_D3DVECTOR v3Position = new _D3DVECTOR();
			D3DXVec3TransformCoord(v3Position, m_v3Position, c_matLocal);
			m_ParticleMesh[0].position = v3Position - v3Up + v3Cross;
			m_ParticleMesh[1].position = v3Position - v3Up - v3Cross;
			m_ParticleMesh[2].position = v3Position + v3Up + v3Cross;
			m_ParticleMesh[3].position = v3Position + v3Up - v3Cross;
		}
		else
		{
			m_ParticleMesh[0].position = m_v3Position - v3Up + v3Cross;
			m_ParticleMesh[1].position = m_v3Position - v3Up - v3Cross;
			m_ParticleMesh[2].position = m_v3Position + v3Up + v3Cross;
			m_ParticleMesh[3].position = m_v3Position + v3Up - v3Cross;
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void Transform(_D3DMATRIX c_matLocal, in float c_fZRotation)
	{
		(CStateManager.Instance()).SetRenderState(D3DRS_TEXTUREFACTOR, (uint)m_dcColor);
    
		_D3DVECTOR v3Up = new _D3DVECTOR();
		_D3DVECTOR v3Cross = new _D3DVECTOR();
    
		if (!m_pParticleProperty.m_bStretchFlag)
		{
			CCamera pCurrentCamera = CCameraManager.Instance().GetCurrentCamera();
			_D3DVECTOR c_rv3Up = pCurrentCamera.GetUp();
			_D3DVECTOR c_rv3Cross = pCurrentCamera.GetCross();
    
			_D3DVECTOR v3Rotation = new _D3DVECTOR();
    
			switch (m_pParticleProperty.m_byBillboardType)
			{
			case BILLBOARD_TYPE_LIE:
			{
					float fCos = cosf(((m_fRotation) * (((float) 3.141592654f) / 180.0f)));
					float fSin = sinf(((m_fRotation) * (((float) 3.141592654f) / 180.0f)));
					v3Up.x = fCos;
					v3Up.y = -fSin;
					v3Up.z = 0;
    
					v3Cross.x = fSin;
					v3Cross.y = fCos;
					v3Cross.z = 0;
			}
				break;
			case BILLBOARD_TYPE_2FACE:
			case BILLBOARD_TYPE_3FACE:
			case BILLBOARD_TYPE_Y:
			{
					v3Up = D3DXVECTOR3(0.0f,0.0f,1.0f);
					_D3DVECTOR c_rv3View = pCurrentCamera.GetView();
					if (v3Up.x * c_rv3View.y - v3Up.y * c_rv3View.x < 0)
					{
						v3Up *= -1;
					}
					D3DXVec3Cross(v3Cross, v3Up, D3DXVECTOR3(c_rv3View.x,c_rv3View.y,0));
					D3DXVec3Normalize(v3Cross, v3Cross);
    
					if (m_fRotation)
					{
						float fCos = -sinf(((m_fRotation) * (((float) 3.141592654f) / 180.0f)));
						float fSin = cosf(((m_fRotation) * (((float) 3.141592654f) / 180.0f)));
    
						_D3DVECTOR v3Temp = v3Up * fCos - v3Cross * fSin;
	//# Laniatus Games Studio Inc. | TODO TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'CopyFrom' method should be created:
	//Original Metin2 CPlus Line: v3Cross = v3Cross * fCos + v3Up * fSin;
						v3Cross.CopyFrom(v3Cross * fCos + v3Up * fSin);
	//# Laniatus Games Studio Inc. | TODO TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'CopyFrom' method should be created:
	//Original Metin2 CPlus Line: v3Up = v3Temp;
						v3Up.CopyFrom(v3Temp);
					}
			}
				break;
			case BILLBOARD_TYPE_ALL:
			default:
			{
					if (m_fRotation == 0.0f)
					{
	//# Laniatus Games Studio Inc. | TODO TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'CopyFrom' method should be created:
	//Original Metin2 CPlus Line: v3Up = -c_rv3Cross;
						v3Up.CopyFrom(-c_rv3Cross);
	//# Laniatus Games Studio Inc. | TODO TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'CopyFrom' method should be created:
	//Original Metin2 CPlus Line: v3Cross = c_rv3Up;
						v3Cross.CopyFrom(c_rv3Up);
					}
					else
					{
						_D3DVECTOR c_rv3View = pCurrentCamera.GetView();
						_D3DMATRIX matRotation = new _D3DMATRIX();
    
						D3DXMatrixRotationAxis(matRotation, c_rv3View, ((m_fRotation) * (((float) 3.141592654f) / 180.0f)));
						D3DXVec3TransformCoord(v3Up, (-c_rv3Cross), matRotation);
						D3DXVec3TransformCoord(v3Cross, c_rv3Up, matRotation);
					}
			}
				break;
			}
		}
		else
		{
			v3Up = m_v3Position - m_v3LastPosition;
    
			if (c_matLocal != null)
			{
				D3DXVec3TransformNormal(v3Up, v3Up, c_matLocal);
			}
    
			float length = D3DXVec3Length(v3Up);
			if (length == 0.0f)
			{
				v3Up = D3DXVECTOR3(0.0f,0.0f,1.0f);
			}
			else
			{
				v3Up *= (1 + Math.Log(1 + length)) / length;
			}
    
			CCamera pCurrentCamera = CCameraManager.Instance().GetCurrentCamera();
			_D3DVECTOR c_rv3View = pCurrentCamera.GetView();
			D3DXVec3Cross(v3Cross, v3Up, c_rv3View);
			D3DXVec3Normalize(v3Cross, v3Cross);
    
		}
    
		if (c_fZRotation != 0)
		{
			float x;
			float y;
			float fCos = cosf(c_fZRotation);
			float fSin = sinf(c_fZRotation);
    
			x = v3Up.x;
			y = v3Up.y;
			v3Up.x = x * fCos - y * fSin;
			v3Up.y = y * fCos + x * fSin;
    
			x = v3Cross.x;
			y = v3Cross.y;
			v3Cross.x = x * fCos - y * fSin;
			v3Cross.y = y * fCos + x * fSin;
		}
    
		v3Cross = -(m_v2HalfSize.x * m_v2Scale.x) * v3Cross;
		v3Up = (m_v2HalfSize.y * m_v2Scale.y) * v3Up;
    
		if (c_matLocal != null && m_pParticleProperty.m_bAttachFlag)
		{
			_D3DVECTOR v3Position = new _D3DVECTOR();
			D3DXVec3TransformCoord(v3Position, m_v3Position, c_matLocal);
			m_ParticleMesh[0].position = v3Position - v3Up + v3Cross;
			m_ParticleMesh[1].position = v3Position - v3Up - v3Cross;
			m_ParticleMesh[2].position = v3Position + v3Up + v3Cross;
			m_ParticleMesh[3].position = v3Position + v3Up - v3Cross;
		}
		else
		{
			m_ParticleMesh[0].position = m_v3Position - v3Up + v3Cross;
			m_ParticleMesh[1].position = m_v3Position - v3Up - v3Cross;
			m_ParticleMesh[2].position = m_v3Position + v3Up + v3Cross;
			m_ParticleMesh[3].position = m_v3Position + v3Up - v3Cross;
		}
	}
}