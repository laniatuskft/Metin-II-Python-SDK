public class CSkyObject
{
//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void Destroy()
	{
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void Update()
	{
		_D3DVECTOR v3Eye = CCameraManager.Instance().GetCurrentCamera().GetEye();
    
		if (m_v3Position == v3Eye)
		{
			if (m_bSkyMatrixUpdated == false)
			{
				return;
			}
		}
    
		m_v3Position = v3Eye;
    
		m_matWorld._41 = m_v3Position.x;
		m_matWorld._42 = m_v3Position.y;
		m_matWorld._43 = m_v3Position.z;
    
		m_matWorldCloud._41 = m_v3Position.x;
		m_matWorldCloud._42 = m_v3Position.y;
		m_matWorldCloud._43 = m_v3Position.z + m_fCloudHeight;
    
		if (m_bSkyMatrixUpdated)
		{
			m_bSkyMatrixUpdated = false;
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void Render()
	{
	}
}