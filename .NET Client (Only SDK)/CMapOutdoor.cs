public class CMapOutdoor
{
//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetShadowTextureSize(ushort size)
	{
		if (m_wShadowMapSize != size)
		{
			recreate = true;
			Tracenf("ShadowTextureSize changed %d -> %d", m_wShadowMapSize, size);
		}
    
		m_wShadowMapSize = size;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void CreateCharacterShadowTexture()
	{
	//# Laniatus Games Studio Inc. |: 'extern' variable declarations are not required in C#:
	//	extern bool GRAPHICS_CAPS_CAN_NOT_DRAW_SHADOW;
    
		if (GRAPHICS_CAPS_CAN_NOT_DRAW_SHADOW)
		{
			return;
		}
    
		ReleaseCharacterShadowTexture();
    
		if (IsLowTextureMemory())
		{
			SetShadowTextureSize(128);
		}
    
		m_ShadowMapViewport.X = 1;
		m_ShadowMapViewport.Y = 1;
		m_ShadowMapViewport.Width = m_wShadowMapSize - 2;
		m_ShadowMapViewport.Height = m_wShadowMapSize - 2;
		m_ShadowMapViewport.MinZ = 0.0f;
		m_ShadowMapViewport.MaxZ = 1.0f;
    
		if (FAILED(ms_lpd3dDevice.CreateTexture(m_wShadowMapSize, m_wShadowMapSize, 1, (0x00000001), D3DFMT_R5G6B5, D3DPOOL_DEFAULT, m_lpCharacterShadowMapTexture)))
		{
			TraceError("CMapOutdoor Unable to create Character Shadow render target texture\n");
			return;
		}
    
		if (FAILED(m_lpCharacterShadowMapTexture.GetSurfaceLevel(0, m_lpCharacterShadowMapRenderTargetSurface)))
		{
			TraceError("CMapOutdoor Unable to GetSurfaceLevel Character Shadow render target texture\n");
			return;
		}
    
		if (FAILED(ms_lpd3dDevice.CreateDepthStencilSurface(m_wShadowMapSize, m_wShadowMapSize, D3DFMT_D16, D3DMULTISAMPLE_NONE, m_lpCharacterShadowMapDepthSurface)))
		{
			TraceError("CMapOutdoor Unable to create Character Shadow depth Surface\n");
			return;
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void ReleaseCharacterShadowTexture()
	{
		{
			if (m_lpCharacterShadowMapRenderTargetSurface)
			{
				(m_lpCharacterShadowMapRenderTargetSurface).Release();
				(m_lpCharacterShadowMapRenderTargetSurface) = null;
			}
		};
		{
			if (m_lpCharacterShadowMapDepthSurface)
			{
				(m_lpCharacterShadowMapDepthSurface).Release();
				(m_lpCharacterShadowMapDepthSurface) = null;
			}
		};
		{
			if (m_lpCharacterShadowMapTexture)
			{
				(m_lpCharacterShadowMapTexture).Release();
				(m_lpCharacterShadowMapTexture) = null;
			}
		};
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool BeginRenderCharacterShadowToTexture()
	{
		_D3DMATRIX matLightView = new _D3DMATRIX();
		_D3DMATRIX matLightProj = new _D3DMATRIX();
    
		CCamera pCurrentCamera = CCameraManager.Instance().GetCurrentCamera();
    
		if (pCurrentCamera == null)
		{
			return false;
		}
    
		if (recreate)
		{
			CreateCharacterShadowTexture();
			recreate = false;
		}
    
		_D3DVECTOR v3Target = pCurrentCamera.GetTarget();
    
		_D3DVECTOR v3Eye = new _D3DVECTOR(v3Target.x - 1.732f * 1250.0f, v3Target.y - 1250.0f, v3Target.z + 2.0f * 1.732f * 1250.0f);
    
		D3DXMatrixLookAtRH(matLightView, v3Eye, v3Target, D3DXVECTOR3(0.0f, 0.0f, 1.0f));
    
		D3DXMatrixOrthoRH(matLightProj, 2550.0f, 2550.0f, 1.0f, 15000.0f);
    
		(CStateManager.Instance()).SaveTransform(D3DTS_VIEW, matLightView);
		(CStateManager.Instance()).SaveTransform(D3DTS_PROJECTION, matLightProj);
    
		dwLightEnable = (CStateManager.Instance()).GetRenderState(D3DRS_LIGHTING);
		(CStateManager.Instance()).SetRenderState(D3DRS_LIGHTING, false);
    
		(CStateManager.Instance()).SaveRenderState(D3DRS_TEXTUREFACTOR, 0xFF808080);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLOROP, D3DTOP_SELECTARG1);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLORARG1, DefineConstants.D3DTA_TFACTOR);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_ALPHAOP, D3DTOP_DISABLE);
		(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_COLOROP, D3DTOP_DISABLE);
    
		bool bSuccess = true;
    
		if (FAILED(ms_lpd3dDevice.GetRenderTarget(m_lpBackupRenderTargetSurface)))
		{
			TraceError("CMapOutdoor::BeginRenderCharacterShadowToTexture : Unable to Save Window Render Target\n");
			bSuccess = false;
		}
    
		if (FAILED(ms_lpd3dDevice.GetDepthStencilSurface(m_lpBackupDepthSurface)))
		{
			TraceError("CMapOutdoor::BeginRenderCharacterShadowToTexture : Unable to Save Window Depth Surface\n");
			bSuccess = false;
		}
    
		if (FAILED(ms_lpd3dDevice.SetRenderTarget(m_lpCharacterShadowMapRenderTargetSurface, m_lpCharacterShadowMapDepthSurface)))
		{
			TraceError("CMapOutdoor::BeginRenderCharacterShadowToTexture : Unable to Set Shadow Map Render Target\n");
			bSuccess = false;
		}
    
		if (FAILED(ms_lpd3dDevice.Clear(0, null, DefineConstants.D3DCLEAR_TARGET | DefineConstants.D3DCLEAR_ZBUFFER, ((uint)((((0xff) & 0xff) << 24) | (((0xFF) & 0xff) << 16) | (((0xFF) & 0xff) << 8) | ((0xFF) & 0xff))), 1.0f, 0)))
		{
			TraceError("CMapOutdoor::BeginRenderCharacterShadowToTexture : Unable to Clear Render Target");
			bSuccess = false;
		}
    
		if (FAILED(ms_lpd3dDevice.GetViewport(m_BackupViewport)))
		{
			TraceError("CMapOutdoor::BeginRenderCharacterShadowToTexture : Unable to Save Window Viewport\n");
			bSuccess = false;
		}
    
		if (FAILED(ms_lpd3dDevice.SetViewport(m_ShadowMapViewport)))
		{
			TraceError("CMapOutdoor::BeginRenderCharacterShadowToTexture : Unable to Set Shadow Map viewport\n");
			bSuccess = false;
		}
    
		return bSuccess;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void EndRenderCharacterShadowToTexture()
	{
		ms_lpd3dDevice.SetViewport(m_BackupViewport);
    
		ms_lpd3dDevice.SetRenderTarget(m_lpBackupRenderTargetSurface, m_lpBackupDepthSurface);
    
		{
			if (m_lpBackupRenderTargetSurface)
			{
				(m_lpBackupRenderTargetSurface).Release();
				(m_lpBackupRenderTargetSurface) = null;
			}
		};
		{
			if (m_lpBackupDepthSurface)
			{
				(m_lpBackupDepthSurface).Release();
				(m_lpBackupDepthSurface) = null;
			}
		};
    
		(CStateManager.Instance()).RestoreTransform(D3DTS_VIEW);
		(CStateManager.Instance()).RestoreTransform(D3DTS_PROJECTION);
		(CStateManager.Instance()).SetRenderState(D3DRS_LIGHTING, dwLightEnable);
		(CStateManager.Instance()).RestoreRenderState(D3DRS_TEXTUREFACTOR);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetIndexBuffer()
	{
		object pIndices;
		int x;
		int y;
    
		uint dwIndexNum = DefineConstants.TERRAIN_PATCHSIZE * DefineConstants.TERRAIN_PATCHSIZE * 4;
    
		ushort[] count = new ushort[TERRAINPATCH_LODMAX];
		ushort[] count2 = new ushort[TERRAINPATCH_LODMAX];
		byte uci;
		for (uci = 0; uci < TERRAINPATCH_LODMAX; ++uci)
		{
			m_pwaIndices[uci] = new ushort[dwIndexNum];
	//# Laniatus Games Studio Inc. | TODO TASK: The memory management function 'memset' has no equivalent in C#:
			memset(m_pwaIndices[uci], 0, sizeof(ushort) * dwIndexNum);
			count[uci] = 0;
			count2[uci] = 0;
			if (!m_IndexBuffer[uci].Create(dwIndexNum, D3DFMT_INDEX16))
			{
				TraceError("CMapOutdoor::SetIndexBuffer() IndexBuffer Create Error");
			}
		}
    
		byte ucNumLineWarp = DefineConstants.TERRAIN_PATCHSIZE + 1;
    
		for (y = 0; y < DefineConstants.TERRAIN_PATCHSIZE; y++)
		{
			if (y % 2 == 0)
			{
				m_pwaIndices[0][(count[0])++] = count2[0];
				m_pwaIndices[0][(count[0])++] = count2[0] + ucNumLineWarp;
			}
			else
			{
				m_pwaIndices[0][(count[0])++] = count2[0] + ucNumLineWarp;
				m_pwaIndices[0][(count[0])++] = count2[0];
			}
    
			for (x = 0; x < DefineConstants.TERRAIN_PATCHSIZE; x++)
			{
				if (y % 2 == 0)
				{
					m_pwaIndices[0][(count[0])++] = (ushort)(count2[0] + 1);
					m_pwaIndices[0][(count[0])++] = (ushort)(count2[0] + ucNumLineWarp + 1);
					count2[0] += (ushort)((short) 1);
				}
				else
				{
					m_pwaIndices[0][(count[0])++] = (ushort)(count2[0] + ucNumLineWarp - 1);
					m_pwaIndices[0][(count[0])++] = (ushort)(count2[0] - 1);
					count2[0] -= (ushort)((short) 1);
				}
    
				if (0 == x % 2)
				{
					if (0 == y)
					{
						if (0 == x)
						{
							ADDLvl1TL(m_pwaIndices[1], count[1], count2[1], ucNumLineWarp);
						}
						else if ((DefineConstants.TERRAIN_PATCHSIZE - 2) == x)
						{
							ADDLvl1TR(m_pwaIndices[1], count[1], count2[1], ucNumLineWarp);
						}
						else
						{
							ADDLvl1T(m_pwaIndices[1], count[1], count2[1], ucNumLineWarp);
						}
					}
					else if ((DefineConstants.TERRAIN_PATCHSIZE - 2) == y)
					{
						if (0 == x)
						{
							ADDLvl1BL(m_pwaIndices[1], count[1], count2[1], ucNumLineWarp);
						}
						else if ((DefineConstants.TERRAIN_PATCHSIZE - 2) == x)
						{
							ADDLvl1BR(m_pwaIndices[1], count[1], count2[1], ucNumLineWarp);
						}
						else
						{
							ADDLvl1B(m_pwaIndices[1], count[1], count2[1], ucNumLineWarp);
						}
					}
					else if (0 == y % 2)
					{
						if (0 == x)
						{
							ADDLvl1L(m_pwaIndices[1], count[1], count2[1], ucNumLineWarp);
						}
						else if ((DefineConstants.TERRAIN_PATCHSIZE - 2) == x)
						{
							ADDLvl1R(m_pwaIndices[1], count[1], count2[1], ucNumLineWarp);
						}
						else
						{
							ADDLvl1M(m_pwaIndices[1], count[1], count2[1], ucNumLineWarp);
						}
					}
					count2[1] += 2;
				}
    
				if (0 == x % 4)
				{
					if (0 == y)
					{
						if (0 == x)
						{
							ADDLvl2TL(m_pwaIndices[2], count[2], count2[2], ucNumLineWarp);
						}
						else if ((DefineConstants.TERRAIN_PATCHSIZE - 4) == x)
						{
							ADDLvl2TR(m_pwaIndices[2], count[2], count2[2], ucNumLineWarp);
						}
						else
						{
							ADDLvl2T(m_pwaIndices[2], count[2], count2[2], ucNumLineWarp);
						}
					}
					else if ((DefineConstants.TERRAIN_PATCHSIZE - 4) == y)
					{
						if (0 == x)
						{
							ADDLvl2BL(m_pwaIndices[2], count[2], count2[2], ucNumLineWarp);
						}
						else if ((DefineConstants.TERRAIN_PATCHSIZE - 4) == x)
						{
							ADDLvl2BR(m_pwaIndices[2], count[2], count2[2], ucNumLineWarp);
						}
						else
						{
							ADDLvl2B(m_pwaIndices[2], count[2], count2[2], ucNumLineWarp);
						}
					}
					else if (0 == y % 4)
					{
						if (0 == x)
						{
							ADDLvl2L(m_pwaIndices[2], count[2], count2[2], ucNumLineWarp);
						}
						else if ((DefineConstants.TERRAIN_PATCHSIZE - 4) == x)
						{
							ADDLvl2R(m_pwaIndices[2], count[2], count2[2], ucNumLineWarp);
						}
						else
						{
							ADDLvl2M(m_pwaIndices[2], count[2], count2[2], ucNumLineWarp);
						}
					}
					count2[2] += 4;
				}
			}
    
			if (y < DefineConstants.TERRAIN_PATCHSIZE-1)
			{
				m_pwaIndices[0][(count[0])++] = (ushort)(count2[0] + ucNumLineWarp);
				m_pwaIndices[0][(count[0])++] = (ushort)(count2[0] + ucNumLineWarp);
				count2[0] += ucNumLineWarp;
				if (0 == y % 2)
				{
					count2[1] += 2;
				}
				if (0 == y % 4)
				{
					count2[2] += 4;
				}
			}
		}
    
		for (uci = 0; uci < TERRAINPATCH_LODMAX; ++uci)
		{
			m_wNumIndices[uci] = count[uci];
			if (!m_IndexBuffer[uci].Lock((object) & pIndices))
			{
				TraceError("CMapOutdoor::SetIndexBuffer() IndexBuffer Unlock Error");
			}
	//# Laniatus Games Studio Inc. | TODO TASK: The memory management function 'memcpy' has no equivalent in C#:
			memcpy(pIndices, m_pwaIndices[uci], count[uci] * sizeof(ushort));
			m_IndexBuffer[uci].Unlock();
			m_pwaIndices[uci] = null;
			m_pwaIndices[uci] = null;
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void ADDLvl1TL(ushort[] pIndices, ref ushort rwCount, in ushort c_rwCurCount, in byte c_rucNumLineWarp)
	{
		pIndices[rwCount++] = c_rwCurCount;
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp + 1);
    
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp * 2);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp + 1);
    
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp + 1);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp * 2);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp * 2 + 2);
    
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp + 1);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp * 2 + 2);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + 2);
    
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp + 1);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + 2);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + 1);
    
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp + 1);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + 1);
		pIndices[rwCount++] = c_rwCurCount;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void ADDLvl1T(ushort[] pIndices, ref ushort rwCount, in ushort c_rwCurCount, in byte c_rucNumLineWarp)
	{
		pIndices[rwCount++] = c_rwCurCount;
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp * 2);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp + 1);
    
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp * 2);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp * 2 + 2);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp + 1);
    
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp * 2 + 2);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + 2);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp + 1);
    
		pIndices[rwCount++] = (ushort)(c_rwCurCount + 2);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + 1);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp + 1);
    
		pIndices[rwCount++] = (ushort)(c_rwCurCount + 1);
		pIndices[rwCount++] = c_rwCurCount;
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp + 1);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void ADDLvl1TR(ushort[] pIndices, ref ushort rwCount, in ushort c_rwCurCount, in byte c_rucNumLineWarp)
	{
		pIndices[rwCount++] = c_rwCurCount;
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp * 2);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp + 1);
    
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp * 2);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp * 2 + 2);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp + 1);
    
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp * 2 + 2);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp + 2);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp + 1);
    
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp + 2);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + 2);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp + 1);
    
		pIndices[rwCount++] = (ushort)(c_rwCurCount + 2);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + 1);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp + 1);
    
		pIndices[rwCount++] = (ushort)(c_rwCurCount + 1);
		pIndices[rwCount++] = c_rwCurCount;
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp + 1);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void ADDLvl1L(ushort[] pIndices, ref ushort rwCount, in ushort c_rwCurCount, in byte c_rucNumLineWarp)
	{
		pIndices[rwCount++] = c_rwCurCount;
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp + 1);
    
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp * 2);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp + 1);
    
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp * 2);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp * 2 + 2);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp + 1);
    
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp * 2 + 2);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + 2);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp + 1);
    
		pIndices[rwCount++] = (ushort)(c_rwCurCount + 2);
		pIndices[rwCount++] = c_rwCurCount;
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp + 1);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void ADDLvl1R(ushort[] pIndices, ref ushort rwCount, in ushort c_rwCurCount, in byte c_rucNumLineWarp)
	{
		pIndices[rwCount++] = c_rwCurCount;
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp * 2);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp + 1);
    
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp * 2);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp * 2 + 2);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp + 1);
    
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp * 2 + 2);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp + 2);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp + 1);
    
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp + 2);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + 2);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp + 1);
    
		pIndices[rwCount++] = (ushort)(c_rwCurCount + 2);
		pIndices[rwCount++] = c_rwCurCount;
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp + 1);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void ADDLvl1BL(ushort[] pIndices, ref ushort rwCount, in ushort c_rwCurCount, in byte c_rucNumLineWarp)
	{
		pIndices[rwCount++] = c_rwCurCount;
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp + 1);
    
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp * 2);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp + 1);
    
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp + 1);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp * 2);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp * 2 + 1);
    
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp + 1);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp * 2 + 1);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp * 2 + 2);
    
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp * 2 + 2);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + 2);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp + 1);
    
		pIndices[rwCount++] = (ushort)(c_rwCurCount + 2);
		pIndices[rwCount++] = c_rwCurCount;
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp + 1);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void ADDLvl1B(ushort[] pIndices, ref ushort rwCount, in ushort c_rwCurCount, in byte c_rucNumLineWarp)
	{
		pIndices[rwCount++] = c_rwCurCount;
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp * 2);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp + 1);
    
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp * 2);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp * 2 + 1);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp + 1);
    
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp * 2 + 1);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp * 2 + 2);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp + 1);
    
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp * 2 + 2);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + 2);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp + 1);
    
		pIndices[rwCount++] = (ushort)(c_rwCurCount + 2);
		pIndices[rwCount++] = c_rwCurCount;
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp + 1);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void ADDLvl1BR(ushort[] pIndices, ref ushort rwCount, in ushort c_rwCurCount, in byte c_rucNumLineWarp)
	{
		pIndices[rwCount++] = c_rwCurCount;
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp * 2);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp + 1);
    
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp * 2);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp * 2 + 1);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp + 1);
    
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp * 2 + 1);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp * 2 + 2);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp + 1);
    
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp * 2 + 2);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp + 2);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp + 1);
    
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp + 2);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + 2);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp + 1);
    
		pIndices[rwCount++] = (ushort)(c_rwCurCount + 2);
		pIndices[rwCount++] = c_rwCurCount;
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp + 1);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void ADDLvl1M(ushort[] pIndices, ref ushort rwCount, in ushort c_rwCurCount, in byte c_rucNumLineWarp)
	{
		pIndices[rwCount++] = c_rwCurCount;
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp * 2);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + 2);
    
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp * 2);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp * 2 + 2);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + 2);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void ADDLvl2TL(ref ushort pIndices, ref ushort rwCount, in ushort c_rwCurCount, in byte c_rucNumLineWarp)
	{
		ADDLvl1TL(pIndices, rwCount, c_rwCurCount, c_rucNumLineWarp);
		ADDLvl1T(pIndices, rwCount, c_rwCurCount + 2, c_rucNumLineWarp);
		ADDLvl1L(pIndices, rwCount, c_rwCurCount + c_rucNumLineWarp * 2, c_rucNumLineWarp);
		ADDLvl1M(pIndices, rwCount, c_rwCurCount + c_rucNumLineWarp * 2 + 2, c_rucNumLineWarp);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void ADDLvl2T(ushort[] pIndices, ref ushort rwCount, in ushort c_rwCurCount, in byte c_rucNumLineWarp)
	{
		ADDLvl1T(pIndices, rwCount, c_rwCurCount, c_rucNumLineWarp);
		ADDLvl1T(pIndices, rwCount, c_rwCurCount + 2, c_rucNumLineWarp);
    
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp * 2);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp * 4);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp * 2 + 2);
    
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp * 4);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp * 4 + 4);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp * 2 + 2);
    
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp * 4 + 4);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp * 2 + 4);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp * 2 + 2);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void ADDLvl2TR(ref ushort pIndices, ref ushort rwCount, in ushort c_rwCurCount, in byte c_rucNumLineWarp)
	{
		ADDLvl1T(pIndices, rwCount, c_rwCurCount, c_rucNumLineWarp);
		ADDLvl1TR(pIndices, rwCount, c_rwCurCount + 2, c_rucNumLineWarp);
		ADDLvl1M(pIndices, rwCount, c_rwCurCount + c_rucNumLineWarp * 2, c_rucNumLineWarp);
		ADDLvl1R(pIndices, rwCount, c_rwCurCount + c_rucNumLineWarp * 2 + 2, c_rucNumLineWarp);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void ADDLvl2L(ushort[] pIndices, ref ushort rwCount, in ushort c_rwCurCount, in byte c_rucNumLineWarp)
	{
		ADDLvl1L(pIndices, rwCount, c_rwCurCount, c_rucNumLineWarp);
		ADDLvl1L(pIndices, rwCount, c_rwCurCount + c_rucNumLineWarp * 2, c_rucNumLineWarp);
    
		pIndices[rwCount++] = (ushort)(c_rwCurCount + 2);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp * 2 + 2);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + 4);
    
		pIndices[rwCount++] = (ushort)(c_rwCurCount + 4);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp * 2 + 2);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp * 4 + 4);
    
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp * 4 + 4);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp * 2 + 2);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp * 4 + 2);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void ADDLvl2R(ushort[] pIndices, ref ushort rwCount, in ushort c_rwCurCount, in byte c_rucNumLineWarp)
	{
		ADDLvl1R(pIndices, rwCount, c_rwCurCount + 2, c_rucNumLineWarp);
		ADDLvl1R(pIndices, rwCount, c_rwCurCount + c_rucNumLineWarp * 2 + 2, c_rucNumLineWarp);
    
		pIndices[rwCount++] = (ushort)(c_rwCurCount + 2);
		pIndices[rwCount++] = c_rwCurCount;
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp * 2 + 2);
    
		pIndices[rwCount++] = c_rwCurCount;
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp * 4);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp * 2 + 2);
    
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp * 2 + 2);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp * 4);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp * 4 + 2);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void ADDLvl2BL(ref ushort pIndices, ref ushort rwCount, in ushort c_rwCurCount, in byte c_rucNumLineWarp)
	{
		ADDLvl1L(pIndices, rwCount, c_rwCurCount, c_rucNumLineWarp);
		ADDLvl1M(pIndices, rwCount, c_rwCurCount + 2, c_rucNumLineWarp);
		ADDLvl1BL(pIndices, rwCount, c_rwCurCount + c_rucNumLineWarp * 2, c_rucNumLineWarp);
		ADDLvl1B(pIndices, rwCount, c_rwCurCount + c_rucNumLineWarp * 2 + 2, c_rucNumLineWarp);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void ADDLvl2B(ushort[] pIndices, ref ushort rwCount, in ushort c_rwCurCount, in byte c_rucNumLineWarp)
	{
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp * 2);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp * 2 + 2);
		pIndices[rwCount++] = c_rwCurCount;
    
		pIndices[rwCount++] = c_rwCurCount;
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp * 2 + 2);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + 4);
    
		pIndices[rwCount++] = (ushort)(c_rwCurCount + 4);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp * 2 + 2);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp * 2 + 4);
    
		ADDLvl1B(pIndices, rwCount, c_rwCurCount + c_rucNumLineWarp * 2, c_rucNumLineWarp);
		ADDLvl1B(pIndices, rwCount, c_rwCurCount + c_rucNumLineWarp * 2 + 2, c_rucNumLineWarp);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void ADDLvl2BR(ref ushort pIndices, ref ushort rwCount, in ushort c_rwCurCount, in byte c_rucNumLineWarp)
	{
		ADDLvl1M(pIndices, rwCount, c_rwCurCount, c_rucNumLineWarp);
		ADDLvl1R(pIndices, rwCount, c_rwCurCount + 2, c_rucNumLineWarp);
		ADDLvl1B(pIndices, rwCount, c_rwCurCount + c_rucNumLineWarp * 2, c_rucNumLineWarp);
		ADDLvl1BR(pIndices, rwCount, c_rwCurCount + c_rucNumLineWarp * 2 + 2, c_rucNumLineWarp);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void ADDLvl2M(ushort[] pIndices, ref ushort rwCount, in ushort c_rwCurCount, in byte c_rucNumLineWarp)
	{
		pIndices[rwCount++] = c_rwCurCount;
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp * 4);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + 4);
    
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp * 4);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + c_rucNumLineWarp * 4 + 4);
		pIndices[rwCount++] = (ushort)(c_rwCurCount + 4);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool Load(float x, float y, float z)
	{
		Destroy();
    
		CEterPackManager rkPackMgr = CEterPackManager.Instance();
		{
	//# Laniatus Games Studio Inc. |: This static local variable declaration (not allowed in C#) has been moved just prior to the method:
	//		static string s_strOldPathName="";
    
			string c_rstrNewPathName = GetName() + "\\cache";
    
			Load_s_strOldPathName = c_rstrNewPathName;
		}
    
		string strFileName = GetMapDataDirectory() + "\\Setting.txt";
    
		if (!LoadSetting(strFileName))
		{
			TraceError("CMapOutdoor::Load : LoadSetting(%s) Failed", strFileName);
		}
    
		if (!LoadMonsterAreaInfo())
		{
			TraceError("CMapOutdoor::Load - LoadMonsterAreaInfo ERROR");
		}
    
		CreateTerrainPatchProxyList();
		BuildQuadTree();
		LoadWaterTexture();
		CreateCharacterShadowTexture();
    
		m_lOldReadX = -1;
    
		CSpeedTreeForestDirectX8.Instance().SetRenderingDevice(ms_lpd3dDevice);
    
		Update(x, y, z);
    
		__HeightCache_Init();
    
		string local_envDataName = GetMapDataDirectory() + "\\" + m_settings_envDataName;
		if (rkPackMgr.isExist(local_envDataName))
		{
			m_envDataName = local_envDataName;
		}
		else
		{
			const string c_rstrEnvironmentRoot = "t:/laniaworkstate/environment/";
			string c_rstrMapName = GetName();
			m_envDataName = c_rstrEnvironmentRoot + m_settings_envDataName;
    
			if (0 == m_envDataName.compare(c_rstrEnvironmentRoot))
			{
				string strAppendName = c_rstrMapName.Substring(c_rstrMapName.Length - 2, 2);
				m_envDataName = c_rstrEnvironmentRoot + strAppendName + ".msenv";
			}
		}
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public string GetEnvironmentDataName()
	{
		return m_envDataName;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool isTerrainLoaded(ushort wX, ushort wY)
	{
		for (uint LaniatusDefVariables = 0; LaniatusDefVariables < m_TerrainVector.size(); ++i)
		{
			CTerrain pTerrain = m_TerrainVector[LaniatusDefVariables];
			ushort usCoordX;
			ushort usCoordY;
			pTerrain.GetCoordinate(usCoordX, usCoordY);
    
			if (usCoordX == wX && usCoordY == wY)
			{
				return true;
			}
		}
		return false;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool isAreaLoaded(ushort wX, ushort wY)
	{
		for (uint LaniatusDefVariables = 0; LaniatusDefVariables < m_AreaVector.size(); ++i)
		{
			CArea pArea = m_AreaVector[LaniatusDefVariables];
			ushort usCoordX;
			ushort usCoordY;
			pArea.GetCoordinate(usCoordX, usCoordY);
    
			if (usCoordX == wX && usCoordY == wY)
			{
				return true;
			}
		}
		return false;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void AssignTerrainPtr()
	{
		OnPreAssignTerrainPtr();
    
		short sReferenceCoordMinX;
		short sReferenceCoordMaxX;
		short sReferenceCoordMinY;
		short sReferenceCoordMaxY;
		sReferenceCoordMinX = Math.Max(m_CurCoordinate.m_sTerrainCoordX - LOAD_SIZE_WIDTH, 0);
		sReferenceCoordMaxX = Math.Min(m_CurCoordinate.m_sTerrainCoordX + LOAD_SIZE_WIDTH, m_sTerrainCountX - 1);
		sReferenceCoordMinY = Math.Max(m_CurCoordinate.m_sTerrainCoordY - LOAD_SIZE_WIDTH, 0);
		sReferenceCoordMaxY = Math.Min(m_CurCoordinate.m_sTerrainCoordY + LOAD_SIZE_WIDTH, m_sTerrainCountY - 1);
    
		uint i;
		for (i = 0; LaniatusDefVariables < AROUND_AREA_NUM; ++i)
		{
			m_pArea[LaniatusDefVariables] = null;
			m_pTerrain[LaniatusDefVariables] = null;
		}
    
		for (i = 0; LaniatusDefVariables < m_TerrainVector.size(); ++i)
		{
			CTerrain pTerrain = m_TerrainVector[LaniatusDefVariables];
			ushort usCoordX;
			ushort usCoordY;
			pTerrain.GetCoordinate(usCoordX, usCoordY);
    
			if (usCoordX >= sReferenceCoordMinX && usCoordX <= sReferenceCoordMaxX && usCoordY >= sReferenceCoordMinY && usCoordY <= sReferenceCoordMaxY)
			{
				m_pTerrain[(usCoordY - m_CurCoordinate.m_sTerrainCoordY + LOAD_SIZE_WIDTH) * 3 + (usCoordX - m_CurCoordinate.m_sTerrainCoordX + LOAD_SIZE_WIDTH)] = pTerrain;
			}
		}
    
		for (i = 0; LaniatusDefVariables < m_AreaVector.size(); ++i)
		{
			CArea pArea = m_AreaVector[LaniatusDefVariables];
			ushort usCoordX;
			ushort usCoordY;
			pArea.GetCoordinate(usCoordX, usCoordY);
    
			if (usCoordX >= sReferenceCoordMinX && usCoordX <= sReferenceCoordMaxX && usCoordY >= sReferenceCoordMinY && usCoordY <= sReferenceCoordMaxY)
			{
				m_pArea[(usCoordY - m_CurCoordinate.m_sTerrainCoordY + LOAD_SIZE_WIDTH) * 3 + (usCoordX - m_CurCoordinate.m_sTerrainCoordX + LOAD_SIZE_WIDTH)] = pArea;
			}
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool LoadArea(ushort wAreaCoordX, ushort wAreaCoordY, ushort wCellCoordX, ushort wCellCoordY)
	{
		if (isAreaLoaded(wAreaCoordX, wAreaCoordY))
		{
			return true;
		}
	#if DEBUG
		uint dwStartTime = ELTimer_GetMSec();
	#endif
		uint ulID = (uint)(wAreaCoordX) * 1000 + (uint)(wAreaCoordY);
		string szAreaPathName = new string(new char[64 + 1]);
		_snprintf(szAreaPathName, sizeof(char), "%s\\%06u\\", GetMapDataDirectory().c_str(), ulID);
    
		CArea pArea = CArea.New();
		pArea.SetMapOutDoor(this);
	#if DEBUG
		Tracef("CMapOutdoor::LoadArea1 %d\n", ELTimer_GetMSec() - dwStartTime);
		dwStartTime = ELTimer_GetMSec();
	#endif
    
		pArea.SetCoordinate(wAreaCoordX, wAreaCoordY);
		if (!pArea.Load(szAreaPathName))
		{
			TraceError(" CMapOutdoor::LoadArea(%d, %d) LoadShadowMap ERROR", wAreaCoordX, wAreaCoordY);
		}
	#if DEBUG
		Tracef("CMapOutdoor::LoadArea2 %d\n", ELTimer_GetMSec() - dwStartTime);
		dwStartTime = ELTimer_GetMSec();
	#endif
    
		m_AreaVector.push_back(pArea);
    
		pArea.EnablePortal(m_bEnablePortal);
	#if DEBUG
		Tracef("CMapOutdoor::LoadArea3 %d\n", ELTimer_GetMSec() - dwStartTime);
	#endif
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool LoadTerrain(ushort wTerrainCoordX, ushort wTerrainCoordY, ushort wCellCoordX, ushort wCellCoordY)
	{
		if (isTerrainLoaded(wTerrainCoordX, wTerrainCoordY))
		{
			return true;
		}
    
		uint dwStartTime = ELTimer_GetMSec();
    
		uint ulID = (uint)(wTerrainCoordX) * 1000 + (uint)(wTerrainCoordY);
		string filename = new string(new char[256]);
		sprintf(filename, "%s\\%06u\\AreaProperty.txt", GetMapDataDirectory().c_str(), ulID);
    
		SortedDictionary<string, List<string>> stTokenVectorMap = new SortedDictionary<string, List<string>>();
    
		if (!LoadMultipleTextData(filename, stTokenVectorMap))
		{
			TraceError("CMapOutdoor::LoadTerrain AreaProperty Read Error\n");
			return false;
		}
    
		if (stTokenVectorMap.end() == stTokenVectorMap.find("scripttype"))
		{
			TraceError("CMapOutdoor::LoadTerrain AreaProperty FileFormat Error 1\n");
			return false;
		}
    
		if (stTokenVectorMap.end() == stTokenVectorMap.find("areaname"))
		{
			TraceError("CMapOutdoor::LoadTerrain AreaProperty FileFormat Error 2\n");
			return false;
		}
    
		string c_rstrType = stTokenVectorMap["scripttype"][0];
		string c_rstrAreaName = stTokenVectorMap["areaname"][0];
    
		if (c_rstrType != "AreaProperty")
		{
			TraceError("CMapOutdoor::LoadTerrain AreaProperty FileFormat Error 3\n");
			return false;
		}
    
		CTerrain pTerrain = CTerrain.New();
    
		pTerrain.Clear();
		pTerrain.SetMapOutDoor(this);
    
		pTerrain.SetCoordinate(wTerrainCoordX, wTerrainCoordY);
    
		pTerrain.CopySettingFromGlobalSetting();
    
		string szRawHeightFieldname = new string(new char[64 + 1]);
		string szWaterMapName = new string(new char[64 + 1]);
		string szAttrMapName = new string(new char[64 + 1]);
		string szShadowTexName = new string(new char[64 + 1]);
		string szShadowMapName = new string(new char[64 + 1]);
		string szMiniMapTexName = new string(new char[64 + 1]);
		string szSplatName = new string(new char[64 + 1]);
    
		_snprintf(szRawHeightFieldname, sizeof(char), "%s\\%06u\\height.raw", GetMapDataDirectory().c_str(), ulID);
		_snprintf(szSplatName, sizeof(char), "%s\\%06u\\tile.raw", GetMapDataDirectory().c_str(), ulID);
		_snprintf(szAttrMapName, sizeof(char), "%s\\%06u\\attr.atr", GetMapDataDirectory().c_str(), ulID);
		_snprintf(szWaterMapName, sizeof(char), "%s\\%06u\\water.wtr", GetMapDataDirectory().c_str(), ulID);
		_snprintf(szShadowTexName, sizeof(char), "%s\\%06u\\shadowmap.dds", GetMapDataDirectory().c_str(), ulID);
		_snprintf(szShadowMapName, sizeof(char), "%s\\%06u\\shadowmap.raw", GetMapDataDirectory().c_str(), ulID);
		_snprintf(szMiniMapTexName, sizeof(char), "%s\\%06u\\minimap.dds", GetMapDataDirectory().c_str(), ulID);
    
		if (!pTerrain.LoadWaterMap(szWaterMapName))
		{
			TraceError(" CMapOutdoor::LoadTerrain(%d, %d) LoadWaterMap ERROR", wTerrainCoordX, wTerrainCoordY);
		}
    
		if (!pTerrain.LoadHeightMap(szRawHeightFieldname))
		{
			TraceError(" CMapOutdoor::LoadTerrain(%d, %d) LoadHeightMap ERROR", wTerrainCoordX, wTerrainCoordY);
		}
    
		if (!pTerrain.LoadAttrMap(szAttrMapName))
		{
			TraceError(" CMapOutdoor::LoadTerrain(%d, %d) LoadAttrMap ERROR", wTerrainCoordX, wTerrainCoordY);
		}
    
		if (!pTerrain.RAW_LoadTileMap(szSplatName))
		{
			TraceError(" CMapOutdoor::LoadTerrain(%d, %d) RAW_LoadTileMap ERROR", wTerrainCoordX, wTerrainCoordY);
		}
    
		pTerrain.LoadShadowTexture(szShadowTexName);
    
		if (!pTerrain.LoadShadowMap(szShadowMapName))
		{
			TraceError(" CMapOutdoor::LoadTerrain(%d, %d) LoadShadowMap ERROR", wTerrainCoordX, wTerrainCoordY);
		}
    
		pTerrain.LoadMiniMapTexture(szMiniMapTexName);
		pTerrain.SetName(c_rstrAreaName);
		pTerrain.CalculateTerrainPatch();
    
		pTerrain.SetReady();
    
		Tracef("CMapOutdoor::LoadTerrain %d\n", ELTimer_GetMSec() - dwStartTime);
    
		m_TerrainVector.push_back(pTerrain);
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool LoadSetting(string c_szFileName)
	{
		NANOBEGIN SortedDictionary<string, List<string>> stTokenVectorMap;
    
		if (!LoadMultipleTextData(c_szFileName, stTokenVectorMap))
		{
			TraceError("MapOutdoor::LoadSetting(c_szFileName=%s) - LoadMultipleTextData", c_szFileName);
			return false;
		}
    
		if (stTokenVectorMap.end() == stTokenVectorMap.find("scripttype"))
		{
			TraceError("MapOutdoor::LoadSetting(c_szFileName=%s) - FIND 'scripttype' - FAILED", c_szFileName);
			return false;
		}
    
		if (stTokenVectorMap.end() == stTokenVectorMap.find("viewradius"))
		{
			TraceError("MapOutdoor::LoadSetting(c_szFileName=%s) - FIND 'viewradius' - FAILED", c_szFileName);
			return false;
		}
    
		if (stTokenVectorMap.end() == stTokenVectorMap.find("cellscale"))
		{
			TraceError("MapOutdoor::LoadSetting(c_szFileName=%s) - FIND 'cellscale' - FAILED", c_szFileName);
			return false;
		}
    
		if (stTokenVectorMap.end() == stTokenVectorMap.find("heightscale"))
		{
			TraceError("MapOutdoor::LoadSetting(c_szFileName=%s) - FIND 'heightscale' - FAILED", c_szFileName);
			return false;
		}
    
		if (stTokenVectorMap.end() == stTokenVectorMap.find("mapsize"))
		{
			TraceError("MapOutdoor::LoadSetting(c_szFileName=%s) - FIND 'mapsize' - FAILED", c_szFileName);
			return false;
		}
    
		if (stTokenVectorMap.end() == stTokenVectorMap.find("textureset"))
		{
			TraceError("MapOutdoor::LoadSetting(c_szFileName=%s) - FIND 'textureset' - FAILED", c_szFileName);
			return false;
		}
    
		if (stTokenVectorMap.end() != stTokenVectorMap.find("terrainvisible"))
		{
			m_bSettingTerrainVisible = (bool)(atoi(stTokenVectorMap["terrainvisible"][0].c_str()) != 0);
		}
		else
		{
			m_bSettingTerrainVisible = true;
		}
    
		string c_rstrType = stTokenVectorMap["scripttype"][0];
		string c_rstrViewRadius = stTokenVectorMap["viewradius"][0];
		string c_rstrHeightScale = stTokenVectorMap["heightscale"][0];
		string c_rstrMapSizeX = stTokenVectorMap["mapsize"][0];
		string c_rstrMapSizeY = stTokenVectorMap["mapsize"][1];
    
		string strTextureSet = "";
		List<string> rkVec_strToken = stTokenVectorMap["textureset"];
		if (rkVec_strToken.Count > 0)
		{
			strTextureSet = rkVec_strToken[0];
		}
    
		if (c_rstrType != "MapSetting")
		{
			TraceError("MapOutdoor::LoadSetting(c_szFileName=%s) - Resourse Type ERROR", c_szFileName);
			return false;
		}
    
		m_lViewRadius = atol(c_rstrViewRadius);
    
		if (0 >= m_lViewRadius)
		{
			TraceError("MapOutdoor::LoadSetting(c_szFileName=%s) - VIEWRADIUS IS NOT GREATER THAN 0", c_szFileName);
			return false;
		}
    
		m_fHeightScale = atof(c_rstrHeightScale);
    
		SetTerrainCount(atoi(c_rstrMapSizeX), atoi(c_rstrMapSizeY));
    
		m_fTerrainTexCoordBase = 1.0f / (float)(CTerrainImpl.PATCH_XSIZE * CTerrainImpl.CELLSCALE);
    
		if (stTokenVectorMap.end() != stTokenVectorMap.find("baseposition"))
		{
			string c_rstrMapBaseX = stTokenVectorMap["baseposition"][0];
			string c_rstrMapBaseY = stTokenVectorMap["baseposition"][1];
			SetBaseXY((uint)atol(c_rstrMapBaseX), (uint)atol(c_rstrMapBaseY));
		}
    
		string stTextureSetFileName = strTextureSet;
    
		if (0 != stTextureSetFileName.IndexOfAny((Convert.ToString("textureset")).ToCharArray(), 0))
		{
			stTextureSetFileName = "textureset\\" + strTextureSet;
		}
    
		 if (!m_TextureSet.Load(stTextureSetFileName, m_fTerrainTexCoordBase))
		 {
			TraceError("MapOutdoor::LoadSetting(c_szFileName=%s) - LOAD TEXTURE SET(%s) ERROR", c_szFileName, stTextureSetFileName);
			return false;
		 }
    
		CTerrain.SetTextureSet(m_TextureSet);
    
		if (stTokenVectorMap.end() != stTokenVectorMap.find("environment"))
		{
			List<string> c_rEnvironmentVector = stTokenVectorMap["environment"];
			if (c_rEnvironmentVector.Count > 0)
			{
				m_settings_envDataName = c_rEnvironmentVector[0];
			}
			else
			{
				TraceError("CMapOutdoor::LoadSetting(c_szFileName=%s) - Failed to load environment data\n", c_szFileName);
			}
		}
    
		m_fWaterTexCoordBase = 1.0f / (float)(CTerrainImpl.CELLSCALE * 4);
    
		D3DXMatrixScaling(m_matSplatAlpha, +m_fTerrainTexCoordBase * 2.0f * (float)(CTerrainImpl.PATCH_XSIZE) / (float)(CTerrainImpl.SPLATALPHA_RAW_XSIZE-2), -m_fTerrainTexCoordBase * 2.0f * (float)(CTerrainImpl.PATCH_YSIZE) / (float)(CTerrainImpl.SPLATALPHA_RAW_XSIZE-2), 0.0f);
		m_matSplatAlpha._41 = m_fTerrainTexCoordBase * 4.6f;
		m_matSplatAlpha._42 = m_fTerrainTexCoordBase * 4.6f;
    
		D3DXMatrixScaling(m_matStaticShadow, +m_fTerrainTexCoordBase * ((float) CTerrainImpl.PATCH_XSIZE / CTerrainImpl.XSIZE), -m_fTerrainTexCoordBase * ((float) CTerrainImpl.PATCH_YSIZE / CTerrainImpl.XSIZE), 0.0f);
		m_matStaticShadow._41 = 0.0f;
		m_matStaticShadow._42 = 0.0f;
    
		D3DXMatrixScaling(m_matDynamicShadowScale, 1.0f / 2550.0f, -1.0f / 2550.0f, 1.0f);
		m_matDynamicShadowScale._41 = 0.5f;
		m_matDynamicShadowScale._42 = 0.5f;
    
		D3DXMatrixScaling(m_matBuildingTransparent, 1.0f / ((float)ms_iWidth), -1.0f / ((float)ms_iHeight), 1.0f);
		m_matBuildingTransparent._41 = 0.5f;
		m_matBuildingTransparent._42 = 0.5f;
		NANOEND return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool LoadMonsterAreaInfo()
	{
		RemoveAllMonsterAreaInfo();
    
		string c_szFileName = new string(new char[256]);
		sprintf(c_szFileName, "%s\\regen.txt", GetMapDataDirectory().c_str());
    
		LPCVOID pModelData = new LPCVOID();
		CMappedFile File = new CMappedFile();
    
		if (!CEterPackManager.Instance().Get(File, c_szFileName, pModelData))
		{
			return false;
		}
    
		CMemoryTextFileLoader textFileLoader = new CMemoryTextFileLoader();
		List<string> stTokenVector = new List<string>();
    
		textFileLoader.Bind(File.Size(), pModelData);
    
		for (uint LaniatusDefVariables = 0; LaniatusDefVariables < textFileLoader.GetLineCount(); ++i)
		{
			if (!textFileLoader.SplitLine(i, stTokenVector))
			{
				continue;
			}
    
			stl_lowers(stTokenVector[0]);
    
			if (0 == string.CompareOrdinal(stTokenVector[0], "m") || 0 == string.CompareOrdinal(stTokenVector[0], "g"))
			{
				if (stTokenVector.Count < 11)
				{
					TraceError("CMapOutdoorAccessor::LoadMonsterAreaInfo Get MonsterInfo File Format ERROR! continue....");
					continue;
				}
    
				CMonsterAreaInfo.EMonsterAreaInfoType eMonsterAreaInfoType = new CMonsterAreaInfo.EMonsterAreaInfoType();
				if (0 == string.CompareOrdinal(stTokenVector[0], "m"))
				{
					eMonsterAreaInfoType = CMonsterAreaInfo.MONSTERAREAINFOTYPE_MONSTER;
				}
				else if (0 == string.CompareOrdinal(stTokenVector[0], "g"))
				{
					eMonsterAreaInfoType = CMonsterAreaInfo.MONSTERAREAINFOTYPE_GROUP;
				}
				else
				{
					TraceError("CMapOutdoorAccessor::LoadMonsterAreaInfo Get MonsterInfo Data ERROR! continue....");
					continue;
				}
    
				string c_rstrOriginX = stTokenVector[1];
				string c_rstrOriginY = stTokenVector[2];
				string c_rstrSizeX = stTokenVector[3];
				string c_rstrSizeY = stTokenVector[4];
				string c_rstrZ = stTokenVector[5];
				string c_rstrDir = stTokenVector[6];
				string c_rstrTime = stTokenVector[7];
				string c_rstrPercent = stTokenVector[8];
				string c_rstrCount = stTokenVector[9];
				string c_rstrVID = stTokenVector[10];
    
				int lOriginX;
				int lOriginY;
				int lSizeX;
				int lSizeY;
				int lZ;
				int lTime;
				int lPercent;
				CMonsterAreaInfo.EMonsterDir eMonsterDir = new CMonsterAreaInfo.EMonsterDir();
				uint dwMonsterCount;
				uint dwMonsterVID;
    
				lOriginX = atol(c_rstrOriginX);
				lOriginY = atol(c_rstrOriginY);
				lSizeX = atol(c_rstrSizeX);
				lSizeY = atol(c_rstrSizeY);
				lZ = atol(c_rstrZ);
				eMonsterDir = (CMonsterAreaInfo.EMonsterDir) atoi(c_rstrDir);
				lTime = atol(c_rstrTime);
				lPercent = atol(c_rstrPercent);
				dwMonsterCount = (uint) atoi(c_rstrCount);
				dwMonsterVID = (uint) atoi(c_rstrVID);
    
				CMonsterAreaInfo pMonsterAreaInfo = AddMonsterAreaInfo(lOriginX, lOriginY, lSizeX, lSizeY);
				pMonsterAreaInfo.SetMonsterAreaInfoType(eMonsterAreaInfoType);
				if (CMonsterAreaInfo.MONSTERAREAINFOTYPE_MONSTER == eMonsterAreaInfoType)
				{
					pMonsterAreaInfo.SetMonsterVID(dwMonsterVID);
				}
				else if (CMonsterAreaInfo.MONSTERAREAINFOTYPE_GROUP == eMonsterAreaInfoType)
				{
					pMonsterAreaInfo.SetMonsterGroupID(dwMonsterVID);
				}
				pMonsterAreaInfo.SetMonsterCount(dwMonsterCount);
				pMonsterAreaInfo.SetMonsterDirection(eMonsterDir);
			}
		}
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void BuildQuadTree()
	{
		FreeQuadTree();
    
		if (0 == m_wPatchCount)
		{
			TraceError("MapOutdoor::BuildQuadTree : m_wPatchCount is zero, you must call ConvertPatchSplat before call this method.");
			return;
		}
    
		m_pRootNode = AllocQuadTreeNode(0, 0, m_wPatchCount - 1, m_wPatchCount - 1);
		if (!m_pRootNode)
		{
			TraceError("CMapOutdoor::BuildQuadTree() RootNode is NULL");
		}
    
		if (m_pRootNode.Size > 1)
		{
			SubDivideNode(m_pRootNode);
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public CTerrainQuadtreeNode AllocQuadTreeNode(int x0, int y0, int x1, int y1)
	{
		CTerrainQuadtreeNode Node;
		int xsize;
		int ysize;
    
		xsize = x1 - x0 + 1;
		ysize = y1 - y0 + 1;
		if ((xsize == 0) || (ysize == 0))
		{
			return null;
		}
    
		Node = new CTerrainQuadtreeNode();
		Node.x0 = x0;
		Node.y0 = y0;
		Node.x1 = x1;
		Node.y1 = y1;
    
		if (ysize > xsize)
		{
			Node.Size = ysize;
		}
		else
		{
			Node.Size = xsize;
		}
    
		Node.PatchNum = y0 * m_wPatchCount + x0;
    
		Node.center.x = 0.0f;
		Node.center.y = 0.0f;
		Node.center.z = 0.0f;
    
		Node.radius = 0.0f;
    
		return Node;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SubDivideNode(CTerrainQuadtreeNode Node)
	{
		int nw_size;
		CTerrainQuadtreeNode tempnode;
    
		nw_size = Node.Size / 2;
    
		Node.NW_Node = AllocQuadTreeNode(Node.x0, Node.y0, Node.x0 + nw_size-1, Node.y0 + nw_size-1);
		Node.NE_Node = AllocQuadTreeNode(Node.x0 + nw_size, Node.y0, Node.x1, Node.y0 + nw_size-1);
		Node.SW_Node = AllocQuadTreeNode(Node.x0, Node.y0 + nw_size, Node.x0 + nw_size-1, Node.y1);
		Node.SE_Node = AllocQuadTreeNode(Node.x0 + nw_size, Node.y0 + nw_size, Node.x1, Node.y1);
    
		tempnode = (CTerrainQuadtreeNode) Node.NW_Node;
		if ((tempnode != null) && (tempnode.Size > 1))
		{
			SubDivideNode(tempnode);
		}
		tempnode = (CTerrainQuadtreeNode) Node.NE_Node;
		if ((tempnode != null) && (tempnode.Size > 1))
		{
			SubDivideNode(tempnode);
		}
		tempnode = (CTerrainQuadtreeNode) Node.SW_Node;
		if ((tempnode != null) && (tempnode.Size > 1))
		{
			SubDivideNode(tempnode);
		}
		tempnode = (CTerrainQuadtreeNode) Node.SE_Node;
		if ((tempnode != null) && (tempnode.Size > 1))
		{
			SubDivideNode(tempnode);
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void FreeQuadTree()
	{
		if (null == m_pRootNode)
		{
			return;
		}
    
		if (m_pRootNode.NW_Node)
		{
			m_pRootNode.NW_Node = null;
			m_pRootNode.NW_Node = null;
		}
		if (m_pRootNode.NE_Node)
		{
			m_pRootNode.NE_Node = null;
			m_pRootNode.NE_Node = null;
		}
		if (m_pRootNode.SW_Node)
		{
			m_pRootNode.SW_Node = null;
			m_pRootNode.SW_Node = null;
		}
		if (m_pRootNode.SE_Node)
		{
			m_pRootNode.SE_Node = null;
			m_pRootNode.SE_Node = null;
		}
    
		m_pRootNode = null;
		m_pRootNode = null;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void RenderTerrain()
	{
		if (!IsVisiblePart(PART_TERRAIN))
		{
			return;
		}
    
		if (!m_bSettingTerrainVisible)
		{
			return;
		}
    
		if (!m_pTerrainPatchProxyList)
		{
			return;
		}
    
		CCamera pCamera = CCameraManager.Instance().GetCurrentCamera();
		if (pCamera == null)
		{
			return;
		}
    
		BuildViewFrustum(ms_matView * ms_matProj);
    
		_D3DVECTOR v3Eye = pCamera.GetEye();
		m_fXforDistanceCaculation = -v3Eye.x;
		m_fYforDistanceCaculation = -v3Eye.y;
    
		m_PatchVector.clear();
    
		__RenderTerrain_RecurseRenderQuadTree(m_pRootNode);
    
		std::sort(m_PatchVector.begin(),m_PatchVector.end());
    
		if (CTerrainPatch.SOFTWARE_TRANSFORM_PATCH_ENABLE)
		{
			__RenderTerrain_RenderSoftwareTransformPatch();
		}
		else
		{
			__RenderTerrain_RenderHardwareTransformPatch();
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __RenderTerrain_RecurseRenderQuadTree(CTerrainQuadtreeNode Node, bool bCullCheckNeed)
	{
		if (bCullCheckNeed)
		{
			switch (__RenderTerrain_RecurseRenderQuadTree_CheckBoundingCircle(Node.center, Node.radius))
			{
				case VIEW_ALL:
					bCullCheckNeed = false;
					break;
				case VIEW_PART:
					break;
				case VIEW_NONE:
					return;
			}
		}
    
		if (Node.Size == 1)
		{
			_D3DVECTOR v3Center = Node.center;
			float fDistance = fMAX(Math.Abs(v3Center.x + m_fXforDistanceCaculation), Math.Abs(-v3Center.y + m_fYforDistanceCaculation));
			__RenderTerrain_AppendPatch(v3Center, fDistance, Node.PatchNum);
		}
		else
		{
			if (Node.NW_Node != null)
			{
				__RenderTerrain_RecurseRenderQuadTree(Node.NW_Node, bCullCheckNeed);
			}
			if (Node.NE_Node != null)
			{
				__RenderTerrain_RecurseRenderQuadTree(Node.NE_Node, bCullCheckNeed);
			}
			if (Node.SW_Node != null)
			{
				__RenderTerrain_RecurseRenderQuadTree(Node.SW_Node, bCullCheckNeed);
			}
			if (Node.SE_Node != null)
			{
				__RenderTerrain_RecurseRenderQuadTree(Node.SE_Node, bCullCheckNeed);
			}
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public int __RenderTerrain_RecurseRenderQuadTree_CheckBoundingCircle(in _D3DVECTOR c_v3Center, in float c_fRadius)
	{
		const int count = 6;
    
		_D3DVECTOR center = new _D3DVECTOR(c_v3Center);
		center.y = -center.y;
    
		int i;
    
		float[] distance = new float[count];
		for (i = 0; LaniatusDefVariables < count; ++i)
		{
			distance[LaniatusDefVariables] = D3DXPlaneDotCoord(m_plane[LaniatusDefVariables], center);
			if (distance[LaniatusDefVariables] <= -c_fRadius)
			{
				return VIEW_NONE;
			}
		}
    
		for (i = 0; LaniatusDefVariables < count;++i)
		{
			if (distance[LaniatusDefVariables] <= c_fRadius)
			{
				return VIEW_PART;
			}
		}
    
		return VIEW_ALL;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __RenderTerrain_AppendPatch(in _D3DVECTOR c_rv3Center, float fDistance, int lPatchNum)
	{
		Debug.Assert(null != m_pTerrainPatchProxyList && "CMapOutdoor::__RenderTerrain_AppendPatch");
		if (!m_pTerrainPatchProxyList[lPatchNum].isUsed())
		{
			return;
		}
    
		m_pTerrainPatchProxyList[lPatchNum].SetCenterPosition(c_rv3Center);
		m_PatchVector.push_back(Tuple.Create(fDistance, lPatchNum));
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void ApplyLight(uint dwVersion, in _D3DLIGHT8 c_rkLight)
	{
		m_kSTPD.m_dwLightVersion = dwVersion;
		(CStateManager.Instance()).SetLight(0, c_rkLight);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void InitializeVisibleParts()
	{
		m_dwVisiblePartFlags = 0xffffffff;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetVisiblePart(int ePart, bool isVisible)
	{
		uint dwMask = (uint)(1 << ePart);
		if (isVisible)
		{
			m_dwVisiblePartFlags |= dwMask;
		}
		else
		{
			uint dwReverseMask = ~dwMask;
			m_dwVisiblePartFlags &= dwReverseMask;
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool IsVisiblePart(int ePart)
	{
		uint dwMask = (uint)(1 << ePart);
		if ((dwMask & m_dwVisiblePartFlags) != 0)
		{
			return true;
		}
    
		return false;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetSplatLimit(int iSplatNum)
	{
		m_iSplatLimit = iSplatNum;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public List<int> GetRenderedSplatNum(ref int piPatch, ref int piSplat, ref float pfSplatRatio)
	{
		piPatch = m_iRenderedPatchNum;
		piSplat = m_iRenderedSplatNum;
		pfSplatRatio = m_iRenderedSplatNumSqSum / (float)m_iRenderedPatchNum;
    
		return m_RenderedTextureNumVector;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public CArea.TCRCWithNumberVector GetRenderedGraphicThingInstanceNum(ref uint pdwGraphicThingInstanceNum, ref uint pdwCRCNum)
	{
		pdwGraphicThingInstanceNum = m_dwRenderedGraphicThingInstanceNum;
		pdwCRCNum = m_dwRenderedCRCNum;
    
		return m_dwRenderedCRCWithNumberVector;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void RenderBeforeLensFlare()
	{
		m_LensFlare.DrawBeforeFlare();
    
		if (!mc_pEnvironmentData)
		{
			TraceError("CMapOutdoor::RenderBeforeLensFlare mc_pEnvironmentData is NULL");
			return;
		}
    
		m_LensFlare.Compute(mc_pEnvironmentData.DirLights[ENV_DIRLIGHT_BACKGROUND].Direction);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void RenderAfterLensFlare()
	{
		m_LensFlare.AdjustBrightness();
		m_LensFlare.DrawFlare();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void RenderCollision()
	{
		for (int LaniatusDefVariables = 0; LaniatusDefVariables < AROUND_AREA_NUM; ++i)
		{
			CArea pArea;
			if (GetAreaPointer(i, pArea))
			{
				pArea.RenderCollision();
			}
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void RenderScreenFiltering()
	{
		m_ScreenFilter.Render();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void RenderSky()
	{
		if (IsVisiblePart(PART_SKY))
		{
			m_SkyBox.Render();
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void RenderCloud()
	{
		if (IsVisiblePart(PART_CLOUD))
		{
			m_SkyBox.RenderCloud();
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void RenderTree()
	{
		if (IsVisiblePart(PART_TREE))
		{
			CSpeedTreeForestDirectX8.Instance().Render();
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetInverseViewAndDynamicShaodwMatrices()
	{
		CCamera pCamera = CCameraManager.Instance().GetCurrentCamera();
    
		if (pCamera == null)
		{
			return;
		}
    
		m_matViewInverse = pCamera.GetInverseViewMatrix();
    
		_D3DVECTOR v3Target = pCamera.GetTarget();
    
		_D3DVECTOR v3LightEye = new _D3DVECTOR(v3Target.x - 1.732f * 1250.0f, v3Target.y - 1250.0f, v3Target.z + 2.0f * 1.732f * 1250.0f);
    
		D3DXMatrixLookAtRH(m_matLightView, v3LightEye, v3Target, D3DXVECTOR3(0.0f, 0.0f, 1.0f));
		m_matDynamicShadow = m_matViewInverse * m_matLightView * m_matDynamicShadowScale;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void OnRender()
	{
		SetInverseViewAndDynamicShaodwMatrices();
    
		SetBlendOperation();
		RenderArea();
		RenderTree();
		if (!m_bEnableTerrainOnlyForHeight)
		{
			RenderTerrain();
		}
		RenderBlendArea();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void RenderEffect()
	{
		if (!IsVisiblePart(PART_OBJECT))
		{
			return;
		}
		for (int LaniatusDefVariables = 0; LaniatusDefVariables < AROUND_AREA_NUM; ++i)
		{
			CArea pArea;
			if (GetAreaPointer(i, pArea))
			{
				pArea.RenderEffect();
			}
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void RenderArea(bool bRenderAmbience)
	{
		if (!IsVisiblePart(PART_OBJECT))
		{
			return;
		}
    
		m_dwRenderedCRCNum = 0;
		m_dwRenderedGraphicThingInstanceNum = 0;
		m_dwRenderedCRCWithNumberVector.clear();
    
		for (int j = 0; j < AROUND_AREA_NUM; ++j)
		{
			CArea pArea;
			if (GetAreaPointer(j, pArea))
			{
				pArea.RenderDungeon();
			}
		}
    
		std::for_each(m_PCBlockerVector.begin(), m_PCBlockerVector.end(), FPCBlockerHide());
    
		if (m_bDrawShadow && m_bDrawChrShadow)
		{
			if (mc_pEnvironmentData != null)
			{
				(CStateManager.Instance()).SetRenderState(D3DRS_FOGCOLOR, 0xFFFFFFFF);
			}
    
			(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLORARG1, DefineConstants.D3DTA_TEXTURE);
			(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLORARG2, DefineConstants.D3DTA_DIFFUSE);
			(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLOROP, D3DTOP_MODULATE);
			(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_ALPHAOP, D3DTOP_DISABLE);
			(CStateManager.Instance()).SaveTextureStageState(1, D3DTSS_TEXCOORDINDEX, DefineConstants.D3DTSS_TCI_CAMERASPACEPOSITION);
			(CStateManager.Instance()).SaveTextureStageState(1, D3DTSS_TEXTURETRANSFORMFLAGS, D3DTTFF_COUNT2);
    
			(CStateManager.Instance()).SaveTransform(D3DTS_TEXTURE1, m_matDynamicShadow);
			(CStateManager.Instance()).SetTexture(1, m_lpCharacterShadowMapTexture);
    
			(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_COLORARG1, DefineConstants.D3DTA_TEXTURE);
			(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_COLORARG2, DefineConstants.D3DTA_CURRENT);
			(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_COLOROP, D3DTOP_MODULATE);
			(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_ALPHAOP, D3DTOP_DISABLE);
			(CStateManager.Instance()).SaveTextureStageState(1, D3DTSS_ADDRESSU, D3DTADDRESS_BORDER);
			(CStateManager.Instance()).SaveTextureStageState(1, D3DTSS_ADDRESSV, D3DTADDRESS_BORDER);
			(CStateManager.Instance()).SaveTextureStageState(1, D3DTSS_BORDERCOLOR, 0xFFFFFFFF);
    
			std::for_each(m_ShadowReceiverVector.begin(), m_ShadowReceiverVector.end(), FAreaRenderShadow());
    
			(CStateManager.Instance()).RestoreTextureStageState(1, D3DTSS_TEXCOORDINDEX);
			(CStateManager.Instance()).RestoreTextureStageState(1, D3DTSS_TEXTURETRANSFORMFLAGS);
			(CStateManager.Instance()).RestoreTextureStageState(1, D3DTSS_ADDRESSU);
			(CStateManager.Instance()).RestoreTextureStageState(1, D3DTSS_ADDRESSV);
			(CStateManager.Instance()).RestoreTextureStageState(1, D3DTSS_BORDERCOLOR);
    
			(CStateManager.Instance()).RestoreTransform(D3DTS_TEXTURE1);
    
			if (mc_pEnvironmentData != null)
			{
				(CStateManager.Instance()).SetRenderState(D3DRS_FOGCOLOR, mc_pEnvironmentData.FogColor);
			}
		}
    
		(CStateManager.Instance()).SaveRenderState(D3DRS_ZWRITEENABLE, true);
    
		bool m_isDisableSortRendering = false;
    
		if (m_isDisableSortRendering)
		{
			for (int LaniatusDefVariables = 0; LaniatusDefVariables < AROUND_AREA_NUM; ++i)
			{
				CArea pArea;
				if (GetAreaPointer(i, pArea))
				{
					pArea.Render();
    
					m_dwRenderedCRCNum += pArea.DEBUG_GetRenderedCRCNum();
					m_dwRenderedGraphicThingInstanceNum += pArea.DEBUG_GetRenderedGrapphicThingInstanceNum();
    
					CArea.TCRCWithNumberVector rCRCWithNumberVector = pArea.DEBUG_GetRenderedCRCWithNumVector();
    
					CArea.TCRCWithNumberVector.iterator aIterator = rCRCWithNumberVector.begin();
					while (aIterator != rCRCWithNumberVector.end())
					{
						uint dwCRC = (*aIterator++).dwCRC;
    
						CArea.TCRCWithNumberVector.iterator aCRCWithNumberVectorIterator = std::find_if(m_dwRenderedCRCWithNumberVector.begin(), m_dwRenderedCRCWithNumberVector.end(), CArea.FFindIfCRC(dwCRC));
    
						if (m_dwRenderedCRCWithNumberVector.end() == aCRCWithNumberVectorIterator)
						{
							CArea.TCRCWithNumber aCRCWithNumber = new CArea.TCRCWithNumber();
							aCRCWithNumber.dwCRC = dwCRC;
							aCRCWithNumber.dwNumber = 1;
							m_dwRenderedCRCWithNumberVector.push_back(aCRCWithNumber);
						}
						else
						{
	//# Laniatus Games Studio Inc. | TODO TASK: C# does not have an equivalent to references to variables:
	//Original Metin2 CPlus Line: CArea::TCRCWithNumber & rCRCWithNumber = *aCRCWithNumberVectorIterator;
							CArea.TCRCWithNumber rCRCWithNumber = *aCRCWithNumberVectorIterator;
							rCRCWithNumber.dwNumber += 1;
						}
					}
				}
			}
    
			std::sort(m_dwRenderedCRCWithNumberVector.begin(), m_dwRenderedCRCWithNumberVector.end(), CArea.CRCNumComp());
		}
		else
		{
	//# Laniatus Games Studio Inc. |: This static local variable declaration (not allowed in C#) has been moved just prior to the method:
	//		static System.Collections.Generic.List<CGraphicThingInstance*> s_kVct_pkOpaqueThingInstSort;
			RenderArea_s_kVct_pkOpaqueThingInstSort.clear();
    
			for (int LaniatusDefVariables = 0; LaniatusDefVariables < AROUND_AREA_NUM; ++i)
			{
				CArea pArea;
				if (GetAreaPointer(i, pArea))
				{
					pArea.CollectRenderingObject(RenderArea_s_kVct_pkOpaqueThingInstSort);
				}
    
			}
    
			std::sort(RenderArea_s_kVct_pkOpaqueThingInstSort.begin(), RenderArea_s_kVct_pkOpaqueThingInstSort.end(), CMapOutdoor_LessThingInstancePtrRenderOrder());
			std::for_each(RenderArea_s_kVct_pkOpaqueThingInstSort.begin(), RenderArea_s_kVct_pkOpaqueThingInstSort.end(), CMapOutdoor_FOpaqueThingInstanceRender());
		}
    
		(CStateManager.Instance()).RestoreRenderState(D3DRS_ZWRITEENABLE);
    
		if (m_bDrawShadow && m_bDrawChrShadow)
		{
			std::for_each(m_ShadowReceiverVector.begin(), m_ShadowReceiverVector.end(), std::mem_fn(CGraphicObjectInstance.Show));
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void RenderBlendArea()
	{
		if (!IsVisiblePart(PART_OBJECT))
		{
			return;
		}
    
	//# Laniatus Games Studio Inc. |: This static local variable declaration (not allowed in C#) has been moved just prior to the method:
	//	static System.Collections.Generic.List<CGraphicThingInstance*> s_kVct_pkBlendThingInstSort;
		RenderBlendArea_s_kVct_pkBlendThingInstSort.clear();
    
		for (int LaniatusDefVariables = 0; LaniatusDefVariables < AROUND_AREA_NUM; ++i)
		{
			CArea pArea;
			if (GetAreaPointer(i, pArea))
			{
				pArea.CollectBlendRenderingObject(RenderBlendArea_s_kVct_pkBlendThingInstSort);
			}
		}
    
		if (RenderBlendArea_s_kVct_pkBlendThingInstSort.size() != 0)
		{
			std::sort(RenderBlendArea_s_kVct_pkBlendThingInstSort.begin(), RenderBlendArea_s_kVct_pkBlendThingInstSort.end(), CMapOutdoor_LessThingInstancePtrRenderOrder());
    
			(CStateManager.Instance()).SaveRenderState(D3DRS_ZWRITEENABLE, true);
			(CStateManager.Instance()).SaveRenderState(D3DRS_ALPHABLENDENABLE, true);
			(CStateManager.Instance()).SaveRenderState(D3DRS_SRCBLEND, D3DBLEND_SRCALPHA);
			(CStateManager.Instance()).SaveRenderState(D3DRS_DESTBLEND, D3DBLEND_INVSRCALPHA);
			(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_ALPHAARG1, DefineConstants.D3DTA_TEXTURE);
			(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_ALPHAOP, D3DTOP_SELECTARG1);
			(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLORARG1, DefineConstants.D3DTA_TEXTURE);
			(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLORARG2, DefineConstants.D3DTA_DIFFUSE);
			(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_COLORARG1, DefineConstants.D3DTA_TEXTURE);
			(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_COLORARG2, DefineConstants.D3DTA_CURRENT);
			(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_COLOROP, D3DTOP_SELECTARG1);
			(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_ALPHAOP, D3DTOP_DISABLE);
    
			std::for_each(RenderBlendArea_s_kVct_pkBlendThingInstSort.begin(), RenderBlendArea_s_kVct_pkBlendThingInstSort.end(), CMapOutdoor_FBlendThingInstanceRender());
    
			(CStateManager.Instance()).RestoreRenderState(D3DRS_ALPHABLENDENABLE);
			(CStateManager.Instance()).RestoreRenderState(D3DRS_SRCBLEND);
			(CStateManager.Instance()).RestoreRenderState(D3DRS_DESTBLEND);
			(CStateManager.Instance()).RestoreRenderState(D3DRS_ZWRITEENABLE);
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void RenderDungeon()
	{
		for (int LaniatusDefVariables = 0; LaniatusDefVariables < AROUND_AREA_NUM; ++i)
		{
			CArea pArea;
			if (!GetAreaPointer(i, pArea))
			{
				continue;
			}
			pArea.RenderDungeon();
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void RenderPCBlocker()
	{
		if (m_PCBlockerVector.size() != 0)
		{
			(CStateManager.Instance()).SetTexture(0, null);
			(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLORARG1, DefineConstants.D3DTA_TEXTURE);
			(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLORARG2, DefineConstants.D3DTA_CURRENT);
			(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLOROP, D3DTOP_MODULATE);
			(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_ALPHAARG1, DefineConstants.D3DTA_TEXTURE);
			(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_ALPHAOP, D3DTOP_SELECTARG1);
			(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_COLOROP, D3DTOP_SELECTARG1);
			(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_ALPHAOP, D3DTOP_DISABLE);
    
			(CStateManager.Instance()).SaveRenderState(D3DRS_ALPHABLENDENABLE, true);
			(CStateManager.Instance()).SaveTextureStageState(1, D3DTSS_TEXCOORDINDEX, DefineConstants.D3DTSS_TCI_CAMERASPACEPOSITION);
			(CStateManager.Instance()).SaveTextureStageState(1, D3DTSS_TEXTURETRANSFORMFLAGS, D3DTTFF_COUNT2);
			(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_COLORARG1, DefineConstants.D3DTA_CURRENT);
			(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_COLOROP, D3DTOP_SELECTARG1);
			(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_ALPHAARG1, DefineConstants.D3DTA_TEXTURE);
			(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_ALPHAOP, D3DTOP_SELECTARG1);
			(CStateManager.Instance()).SaveTextureStageState(1, D3DTSS_ADDRESSU, D3DTADDRESS_CLAMP);
			(CStateManager.Instance()).SaveTextureStageState(1, D3DTSS_ADDRESSV, D3DTADDRESS_CLAMP);
    
			(CStateManager.Instance()).SaveTransform(D3DTS_TEXTURE1, m_matBuildingTransparent);
			(CStateManager.Instance()).SetTexture(1, m_BuildingTransparentImageInstance.GetTexturePointer().GetD3DTexture());
    
			std::for_each(m_PCBlockerVector.begin(), m_PCBlockerVector.end(), FRenderPCBlocker());
    
			(CStateManager.Instance()).SetTexture(1, null);
			(CStateManager.Instance()).RestoreTransform(D3DTS_TEXTURE1);
    
			(CStateManager.Instance()).RestoreTextureStageState(1, D3DTSS_TEXCOORDINDEX);
			(CStateManager.Instance()).RestoreTextureStageState(1, D3DTSS_TEXTURETRANSFORMFLAGS);
			(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_COLORARG1, DefineConstants.D3DTA_TEXTURE);
			(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_COLOROP, D3DTOP_DISABLE);
			(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_ALPHAARG1, DefineConstants.D3DTA_TEXTURE);
			(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_ALPHAOP, D3DTOP_DISABLE);
			(CStateManager.Instance()).RestoreTextureStageState(1, D3DTSS_ADDRESSU);
			(CStateManager.Instance()).RestoreTextureStageState(1, D3DTSS_ADDRESSV);
			(CStateManager.Instance()).RestoreRenderState(D3DRS_ALPHABLENDENABLE);
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SelectIndexBuffer(byte byLODLevel, ref ushort pwPrimitiveCount, D3DPRIMITIVETYPE pePrimitiveType)
	{
		if (0 == byLODLevel)
		{
			pwPrimitiveCount = m_wNumIndices[byLODLevel] - 2;
			pePrimitiveType = D3DPT_TRIANGLESTRIP;
		}
		else
		{
			pwPrimitiveCount = m_wNumIndices[byLODLevel] / 3;
			pePrimitiveType = D3DPT_TRIANGLELIST;
		}
		(CStateManager.Instance()).SetIndices(m_IndexBuffer[byLODLevel].GetD3DIndexBuffer(), 0);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetPatchDrawVector()
	{
		Debug.Assert(null != m_pTerrainPatchProxyList && "CMapOutdoor::__SetPatchDrawVector");
    
		m_PatchDrawStructVector.clear();
    
		List<Tuple<float, int>>.Enumerator aDistancePatchVectorIterator;
    
		TPatchDrawStruct aPatchDrawStruct = new TPatchDrawStruct();
    
		aDistancePatchVectorIterator = m_PatchVector.begin();
		while (aDistancePatchVectorIterator.MoveNext())
		{
			Tuple<float, int> adistancePatchPair = aDistancePatchVectorIterator.Current;
    
			CTerrainPatchProxy pTerrainPatchProxy = m_pTerrainPatchProxyList[adistancePatchPair.Item2];
    
			if (!pTerrainPatchProxy.isUsed())
			{
				continue;
			}
    
			int lPatchNum = pTerrainPatchProxy.GetPatchNum();
			if (lPatchNum < 0)
			{
				continue;
			}
    
			byte byTerrainNum = pTerrainPatchProxy.GetTerrainNum();
			if (0xFF == byTerrainNum)
			{
				continue;
			}
    
			CTerrain pTerrain;
			if (!GetTerrainPointer(byTerrainNum, pTerrain))
			{
				continue;
			}
    
			aPatchDrawStruct.fDistance = adistancePatchPair.Item1;
			aPatchDrawStruct.byTerrainNum = byTerrainNum;
			aPatchDrawStruct.lPatchNum = lPatchNum;
			aPatchDrawStruct.pTerrainPatchProxy = pTerrainPatchProxy;
    
			m_PatchDrawStructVector.push_back(aPatchDrawStruct);
    
		}
    
		std::stable_sort(m_PatchDrawStructVector.begin(), m_PatchDrawStructVector.end(), FSortPatchDrawStructWithTerrainNum());
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public float __GetNoFogDistance()
	{
		return (float)(CTerrainImpl.CELLSCALE * m_lViewRadius) * 0.5f;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public float __GetFogDistance()
	{
		return (float)(CTerrainImpl.CELLSCALE * m_lViewRadius) * 0.75f;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void NEW_DrawWireFrame(CTerrainPatchProxy pTerrainPatchProxy, ushort wPrimitiveCount, D3DPRIMITIVETYPE ePrimitiveType)
	{
		uint dwFillMode = (CStateManager.Instance()).GetRenderState(D3DRS_FILLMODE);
		(CStateManager.Instance()).SetRenderState(D3DRS_FILLMODE, D3DFILL_WIREFRAME);
    
		uint dwFogEnable = (CStateManager.Instance()).GetRenderState(D3DRS_FOGENABLE);
		(CStateManager.Instance()).SetRenderState(D3DRS_FOGENABLE, false);
    
		(CStateManager.Instance()).SetTexture(0, null);
		(CStateManager.Instance()).SetTexture(1, null);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLOROP, D3DTOP_DISABLE);
    
		(CStateManager.Instance()).DrawIndexedPrimitive(ePrimitiveType, 0, m_iPatchTerrainVertexCount, 0, wPrimitiveCount);
    
		(CStateManager.Instance()).SetRenderState(D3DRS_FILLMODE, dwFillMode);
		(CStateManager.Instance()).SetRenderState(D3DRS_FOGENABLE, dwFogEnable);
    
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLORARG1, DefineConstants.D3DTA_TEXTURE);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLORARG2, DefineConstants.D3DTA_CURRENT);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLOROP, D3DTOP_MODULATE);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void DrawWireFrame(int patchnum, ushort wPrimitiveCount, D3DPRIMITIVETYPE ePrimitiveType)
	{
		Debug.Assert(null != m_pTerrainPatchProxyList && "CMapOutdoor::DrawWireFrame");
    
		CTerrainPatchProxy pTerrainPatchProxy = m_pTerrainPatchProxyList[patchnum];
    
		if (!pTerrainPatchProxy.isUsed())
		{
			return;
		}
    
		int sPatchNum = pTerrainPatchProxy.GetPatchNum();
		if (sPatchNum < 0)
		{
			return;
		}
		byte ucTerrainNum = pTerrainPatchProxy.GetTerrainNum();
		if (0xFF == ucTerrainNum)
		{
			return;
		}
    
		uint dwFillMode = (CStateManager.Instance()).GetRenderState(D3DRS_FILLMODE);
		(CStateManager.Instance()).SetRenderState(D3DRS_FILLMODE, D3DFILL_WIREFRAME);
    
		uint dwFogEnable = (CStateManager.Instance()).GetRenderState(D3DRS_FOGENABLE);
		(CStateManager.Instance()).SetRenderState(D3DRS_FOGENABLE, false);
    
		(CStateManager.Instance()).SetTexture(0, null);
		(CStateManager.Instance()).SetTexture(1, null);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLOROP, D3DTOP_DISABLE);
    
		(CStateManager.Instance()).DrawIndexedPrimitive(ePrimitiveType, 0, m_iPatchTerrainVertexCount, 0, wPrimitiveCount);
    
		(CStateManager.Instance()).SetRenderState(D3DRS_FILLMODE, dwFillMode);
		(CStateManager.Instance()).SetRenderState(D3DRS_FOGENABLE, dwFogEnable);
    
		 (CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLORARG1, DefineConstants.D3DTA_TEXTURE);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLORARG2, DefineConstants.D3DTA_CURRENT);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLOROP, D3DTOP_MODULATE);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void RenderMarkedArea()
	{
		if (!m_pTerrainPatchProxyList)
		{
			return;
		}
    
		m_matWorldForCommonUse._41 = 0.0f;
		m_matWorldForCommonUse._42 = 0.0f;
		(CStateManager.Instance()).SetTransform((D3DTRANSFORMSTATETYPE)(0 + 256), m_matWorldForCommonUse);
    
		ushort wPrimitiveCount;
		D3DPRIMITIVETYPE eType = new D3DPRIMITIVETYPE();
		SelectIndexBuffer(0, wPrimitiveCount, eType);
    
		_D3DMATRIX matTexTransform = new _D3DMATRIX();
		_D3DMATRIX matTexTransformTemp = new _D3DMATRIX();
    
		D3DXMatrixScaling(matTexTransform, m_fTerrainTexCoordBase * 32.0f, -m_fTerrainTexCoordBase * 32.0f, 0.0f);
		D3DXMatrixMultiply(matTexTransform, m_matViewInverse, matTexTransform);
		(CStateManager.Instance()).SaveTransform(D3DTS_TEXTURE0, matTexTransform);
		(CStateManager.Instance()).SaveTransform(D3DTS_TEXTURE1, matTexTransform);
    
		(CStateManager.Instance()).SaveRenderState(D3DRS_ALPHABLENDENABLE, true);
		(CStateManager.Instance()).SaveRenderState(D3DRS_SRCBLEND, D3DBLEND_SRCALPHA);
		(CStateManager.Instance()).SaveRenderState(D3DRS_DESTBLEND, D3DBLEND_INVSRCALPHA);
    
	//# Laniatus Games Studio Inc. |: This static local variable declaration (not allowed in C#) has been moved just prior to the method:
	//	static int lStartTime = timeGetTime();
		float fTime = (float)((timeGetTime() - RenderMarkedArea_lStartTime) % 3000) / 3000.0f;
		float fAlpha = Math.Abs(fTime - 0.5f) / 2.0f + 0.1f;
		(CStateManager.Instance()).SetRenderState(D3DRS_TEXTUREFACTOR, D3DXCOLOR(1.0f, 1.0f, 1.0f, fAlpha));
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLORARG1, DefineConstants.D3DTA_TEXTURE);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLORARG2, DefineConstants.D3DTA_TFACTOR);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLOROP, D3DTOP_SELECTARG2);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_ALPHAARG1, DefineConstants.D3DTA_TEXTURE);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_ALPHAARG2, DefineConstants.D3DTA_TFACTOR);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_ALPHAOP, D3DTOP_SELECTARG2);
		(CStateManager.Instance()).SaveTextureStageState(0, D3DTSS_TEXCOORDINDEX, DefineConstants.D3DTSS_TCI_CAMERASPACEPOSITION);
		(CStateManager.Instance()).SaveTextureStageState(0, D3DTSS_TEXTURETRANSFORMFLAGS, D3DTTFF_COUNT2);
    
		(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_COLORARG1, DefineConstants.D3DTA_CURRENT);
		(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_COLOROP, D3DTOP_SELECTARG1);
		(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_ALPHAARG1, DefineConstants.D3DTA_TEXTURE);
		(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_ALPHAARG2, DefineConstants.D3DTA_CURRENT);
		(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_ALPHAOP, D3DTOP_MODULATE);
		(CStateManager.Instance()).SaveTextureStageState(1, D3DTSS_TEXCOORDINDEX, DefineConstants.D3DTSS_TCI_CAMERASPACEPOSITION);
		(CStateManager.Instance()).SaveTextureStageState(1, D3DTSS_TEXTURETRANSFORMFLAGS, D3DTTFF_COUNT2);
		(CStateManager.Instance()).SaveTextureStageState(1, D3DTSS_MINFILTER, D3DTEXF_POINT);
		(CStateManager.Instance()).SaveTextureStageState(1, D3DTSS_MAGFILTER, D3DTEXF_POINT);
		(CStateManager.Instance()).SaveTextureStageState(1, D3DTSS_MIPFILTER, D3DTEXF_POINT);
		(CStateManager.Instance()).SaveTextureStageState(1, D3DTSS_ADDRESSU, D3DTADDRESS_CLAMP);
		(CStateManager.Instance()).SaveTextureStageState(1, D3DTSS_ADDRESSV, D3DTADDRESS_CLAMP);
    
		(CStateManager.Instance()).SetTexture(0, m_attrImageInstance.GetTexturePointer().GetD3DTexture());
    
		RecurseRenderAttr(m_pRootNode);
    
		(CStateManager.Instance()).RestoreTextureStageState(0, D3DTSS_TEXCOORDINDEX);
		(CStateManager.Instance()).RestoreTextureStageState(0, D3DTSS_TEXTURETRANSFORMFLAGS);
		(CStateManager.Instance()).RestoreTextureStageState(1, D3DTSS_TEXCOORDINDEX);
		(CStateManager.Instance()).RestoreTextureStageState(1, D3DTSS_TEXTURETRANSFORMFLAGS);
		(CStateManager.Instance()).RestoreTextureStageState(1, D3DTSS_MINFILTER);
		(CStateManager.Instance()).RestoreTextureStageState(1, D3DTSS_MAGFILTER);
		(CStateManager.Instance()).RestoreTextureStageState(1, D3DTSS_MIPFILTER);
		(CStateManager.Instance()).RestoreTextureStageState(1, D3DTSS_ADDRESSU);
		(CStateManager.Instance()).RestoreTextureStageState(1, D3DTSS_ADDRESSV);
    
		(CStateManager.Instance()).RestoreTransform(D3DTS_TEXTURE0);
		(CStateManager.Instance()).RestoreTransform(D3DTS_TEXTURE1);
    
		(CStateManager.Instance()).RestoreRenderState(D3DRS_ALPHABLENDENABLE);
		(CStateManager.Instance()).RestoreRenderState(D3DRS_SRCBLEND);
		(CStateManager.Instance()).RestoreRenderState(D3DRS_DESTBLEND);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void RecurseRenderAttr(CTerrainQuadtreeNode Node, bool bCullEnable)
	{
		if (bCullEnable)
		{
			if (__RenderTerrain_RecurseRenderQuadTree_CheckBoundingCircle(Node.center, Node.radius) == VIEW_NONE)
			{
				return;
			}
		}
    
		{
			if (Node.Size == 1)
			{
				DrawPatchAttr(Node.PatchNum);
			}
			else
			{
				if (Node.NW_Node != null)
				{
					RecurseRenderAttr(Node.NW_Node, bCullEnable);
				}
				if (Node.NE_Node != null)
				{
					RecurseRenderAttr(Node.NE_Node, bCullEnable);
				}
				if (Node.SW_Node != null)
				{
					RecurseRenderAttr(Node.SW_Node, bCullEnable);
				}
				if (Node.SE_Node != null)
				{
					RecurseRenderAttr(Node.SE_Node, bCullEnable);
				}
			}
		 }
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void DrawPatchAttr(int patchnum)
	{
		CTerrainPatchProxy pTerrainPatchProxy = m_pTerrainPatchProxyList[patchnum];
		if (!pTerrainPatchProxy.isUsed())
		{
			return;
		}
    
		int sPatchNum = pTerrainPatchProxy.GetPatchNum();
		if (sPatchNum < 0)
		{
			return;
		}
    
		byte ucTerrainNum = pTerrainPatchProxy.GetTerrainNum();
		if (0xFF == ucTerrainNum)
		{
			return;
		}
    
		CTerrain pTerrain;
		if (!GetTerrainPointer(ucTerrainNum, pTerrain))
		{
			return;
		}
    
		if (!pTerrain.IsMarked())
		{
			return;
		}
    
		ushort wCoordX;
		ushort wCoordY;
		pTerrain.GetCoordinate(wCoordX, wCoordY);
    
		m_matWorldForCommonUse._41 = -(float)(wCoordX * CTerrainImpl.XSIZE * CTerrainImpl.CELLSCALE);
		m_matWorldForCommonUse._42 = (float)(wCoordY * CTerrainImpl.YSIZE * CTerrainImpl.CELLSCALE);
    
		_D3DMATRIX matTexTransform = new _D3DMATRIX();
		_D3DMATRIX matTexTransformTemp = new _D3DMATRIX();
		D3DXMatrixMultiply(matTexTransform, m_matViewInverse, m_matWorldForCommonUse);
		D3DXMatrixMultiply(matTexTransform, matTexTransform, m_matStaticShadow);
		(CStateManager.Instance()).SetTransform(D3DTS_TEXTURE1, matTexTransform);
    
		TTerrainSplatPatch rAttrSplatPatch = pTerrain.GetMarkedSplatPatch();
		 (CStateManager.Instance()).SetTexture(1, rAttrSplatPatch.Splats[0].pd3dTexture);
    
		(CStateManager.Instance()).SetVertexShader(DefineConstants.D3DFVF_XYZ | DefineConstants.D3DFVF_NORMAL);
		(CStateManager.Instance()).SetStreamSource(0, pTerrainPatchProxy.HardwareTransformPatch_GetVertexBufferPtr().GetD3DVertexBuffer(), m_iPatchTerrainVertexSize);
		(CStateManager.Instance()).DrawIndexedPrimitive(D3DPT_TRIANGLESTRIP, 0, m_iPatchTerrainVertexCount, 0, m_wNumIndices[0] - 2);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __RenderTerrain_RenderHardwareTransformPatch()
	{
		uint dwFogColor;
		float fFogFarDistance;
		float fFogNearDistance;
		if (mc_pEnvironmentData)
		{
			dwFogColor = mc_pEnvironmentData.FogColor;
			fFogNearDistance = mc_pEnvironmentData.GetFogNearDistance();
			fFogFarDistance = mc_pEnvironmentData.GetFogFarDistance();
		}
		else
		{
			dwFogColor = 0xffffffff;
			fFogNearDistance = 5000.0f;
			fFogFarDistance = 10000.0f;
		}
    
		(CStateManager.Instance()).SaveTextureStageState(0, D3DTSS_TEXCOORDINDEX, DefineConstants.D3DTSS_TCI_CAMERASPACEPOSITION);
		(CStateManager.Instance()).SaveTextureStageState(0, D3DTSS_TEXTURETRANSFORMFLAGS, D3DTTFF_COUNT2);
		(CStateManager.Instance()).SaveTextureStageState(1, D3DTSS_TEXCOORDINDEX, DefineConstants.D3DTSS_TCI_CAMERASPACEPOSITION);
		(CStateManager.Instance()).SaveTextureStageState(1, D3DTSS_TEXTURETRANSFORMFLAGS, D3DTTFF_COUNT2);
    
		(CStateManager.Instance()).SaveRenderState(D3DRS_ALPHABLENDENABLE, true);
		(CStateManager.Instance()).SaveRenderState(D3DRS_ALPHATESTENABLE, true);
		(CStateManager.Instance()).SaveRenderState(D3DRS_ALPHAREF, 0x00000000);
		(CStateManager.Instance()).SaveRenderState(D3DRS_ALPHAFUNC, D3DCMP_GREATER);
    
		(CStateManager.Instance()).SaveRenderState(D3DRS_TEXTUREFACTOR, dwFogColor);
    
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLORARG1, DefineConstants.D3DTA_TEXTURE);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLORARG2, DefineConstants.D3DTA_CURRENT);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLOROP, D3DTOP_MODULATE);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_ALPHAARG1, DefineConstants.D3DTA_TEXTURE);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_ALPHAOP, D3DTOP_SELECTARG1);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_ADDRESSU, D3DTADDRESS_WRAP);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_ADDRESSV, D3DTADDRESS_WRAP);
    
		(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_COLORARG1, DefineConstants.D3DTA_CURRENT);
		(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_COLOROP, D3DTOP_SELECTARG1);
		(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_ALPHAARG1, DefineConstants.D3DTA_TEXTURE);
		(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_ALPHAOP, D3DTOP_SELECTARG1);
		(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_ADDRESSU, D3DTADDRESS_CLAMP);
		(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_ADDRESSV, D3DTADDRESS_CLAMP);
    
		CSpeedTreeWrapper.ms_bSelfShadowOn = true;
		(CStateManager.Instance()).SetBestFiltering(0);
		(CStateManager.Instance()).SetBestFiltering(1);
    
		m_matWorldForCommonUse._41 = 0.0f;
		m_matWorldForCommonUse._42 = 0.0f;
		(CStateManager.Instance()).SetTransform((D3DTRANSFORMSTATETYPE)(0 + 256), m_matWorldForCommonUse);
    
		(CStateManager.Instance()).SaveTransform(D3DTS_TEXTURE0, m_matWorldForCommonUse);
		(CStateManager.Instance()).SaveTransform(D3DTS_TEXTURE1, m_matWorldForCommonUse);
    
		(CStateManager.Instance()).SetVertexShader(DefineConstants.D3DFVF_XYZ | DefineConstants.D3DFVF_NORMAL);
    
		m_iRenderedSplatNumSqSum = 0;
		m_iRenderedPatchNum = 0;
		m_iRenderedSplatNum = 0;
		m_RenderedTextureNumVector.clear();
    
		Tuple<float, int> fog_far = new Tuple<float, int>(fFogFarDistance+1600.0f, 0);
		Tuple<float, int> fog_near = new Tuple<float, int>(fFogNearDistance-3200.0f, 0);
    
		List<Tuple<float,int>>.Enumerator far_it = std::upper_bound(m_PatchVector.begin(),m_PatchVector.end(),fog_far);
		List<Tuple<float,int>>.Enumerator near_it = std::upper_bound(m_PatchVector.begin(),m_PatchVector.end(),fog_near);
    
		ushort wPrimitiveCount;
		D3DPRIMITIVETYPE ePrimitiveType = new D3DPRIMITIVETYPE();
    
		byte byCUrrentLODLevel = 0;
    
		float fLODLevel1Distance = __GetNoFogDistance();
		float fLODLevel2Distance = __GetFogDistance();
    
		SelectIndexBuffer(0, wPrimitiveCount, ePrimitiveType);
    
		uint dwFogEnable = (CStateManager.Instance()).GetRenderState(D3DRS_FOGENABLE);
		List<Tuple<float, int>>.Enumerator it = m_PatchVector.begin();
    
		(CStateManager.Instance()).SetRenderState(D3DRS_FOGENABLE, false);
    
		for (; it != near_it; ++it)
		{
			if (byCUrrentLODLevel == 0 && fLODLevel1Distance <= it.first)
			{
				byCUrrentLODLevel = 1;
				SelectIndexBuffer(1, wPrimitiveCount, ePrimitiveType);
			}
			else if (byCUrrentLODLevel == 1 && fLODLevel2Distance <= it.first)
			{
				byCUrrentLODLevel = 2;
				SelectIndexBuffer(2, wPrimitiveCount, ePrimitiveType);
			}
    
			__HardwareTransformPatch_RenderPatchSplat(it.second, wPrimitiveCount, ePrimitiveType);
			if (m_iRenderedSplatNum >= m_iSplatLimit)
			{
				break;
			}
    
			 if (m_bDrawWireFrame)
			 {
				DrawWireFrame(it.second, wPrimitiveCount, ePrimitiveType);
			 }
		}
    
		(CStateManager.Instance()).SetRenderState(D3DRS_FOGENABLE, dwFogEnable);
    
		if (m_iRenderedSplatNum < m_iSplatLimit)
		{
			for (it = near_it; it != far_it; ++it)
			{
				if (byCUrrentLODLevel == 0 && fLODLevel1Distance <= it.first)
				{
					byCUrrentLODLevel = 1;
					SelectIndexBuffer(1, wPrimitiveCount, ePrimitiveType);
				}
				else if (byCUrrentLODLevel == 1 && fLODLevel2Distance <= it.first)
				{
					byCUrrentLODLevel = 2;
					SelectIndexBuffer(2, wPrimitiveCount, ePrimitiveType);
				}
    
				__HardwareTransformPatch_RenderPatchSplat(it.second, wPrimitiveCount, ePrimitiveType);
    
				if (m_iRenderedSplatNum >= m_iSplatLimit)
				{
					break;
				}
    
				if (m_bDrawWireFrame)
				{
					DrawWireFrame(it.second, wPrimitiveCount, ePrimitiveType);
				}
			}
		}
    
		(CStateManager.Instance()).SetRenderState(D3DRS_FOGENABLE, false);
		(CStateManager.Instance()).SetRenderState(D3DRS_LIGHTING, false);
    
		(CStateManager.Instance()).SetTexture(0, null);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_TEXTURETRANSFORMFLAGS, false);
    
		(CStateManager.Instance()).SetTexture(1, null);
		(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_TEXTURETRANSFORMFLAGS, false);
    
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLORARG1, DefineConstants.D3DTA_TFACTOR);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLOROP, D3DTOP_SELECTARG1);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_ALPHAOP, D3DTOP_DISABLE);
    
		(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_COLOROP, D3DTOP_DISABLE);
		(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_ALPHAOP, D3DTOP_DISABLE);
    
		if (m_iRenderedSplatNum < m_iSplatLimit)
		{
			for (it = far_it; it.MoveNext();)
			{
				if (byCUrrentLODLevel == 0 && fLODLevel1Distance <= it.first)
				{
					byCUrrentLODLevel = 1;
					SelectIndexBuffer(1, wPrimitiveCount, ePrimitiveType);
				}
				else if (byCUrrentLODLevel == 1 && fLODLevel2Distance <= it.first)
				{
					byCUrrentLODLevel = 2;
					SelectIndexBuffer(2, wPrimitiveCount, ePrimitiveType);
				}
    
				__HardwareTransformPatch_RenderPatchNone(it.second, wPrimitiveCount, ePrimitiveType);
    
				if (m_iRenderedSplatNum >= m_iSplatLimit)
				{
					break;
				}
    
				if (m_bDrawWireFrame)
				{
					 DrawWireFrame(it.second, wPrimitiveCount, ePrimitiveType);
				}
			}
		}
    
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLORARG1, DefineConstants.D3DTA_TEXTURE);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLORARG2, DefineConstants.D3DTA_CURRENT);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLOROP, D3DTOP_MODULATE);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_ALPHAARG1, DefineConstants.D3DTA_TEXTURE);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_ALPHAOP, D3DTOP_SELECTARG1);
    
		(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_COLORARG1, DefineConstants.D3DTA_CURRENT);
		(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_COLOROP, D3DTOP_SELECTARG1);
		(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_ALPHAARG1, DefineConstants.D3DTA_TEXTURE);
		(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_ALPHAOP, D3DTOP_SELECTARG1);
    
		(CStateManager.Instance()).SetRenderState(D3DRS_FOGENABLE, dwFogEnable);
		(CStateManager.Instance()).SetRenderState(D3DRS_LIGHTING, true);
    
		std::sort(m_RenderedTextureNumVector.begin(),m_RenderedTextureNumVector.end());
    
		(CStateManager.Instance()).RestoreRenderState(D3DRS_TEXTUREFACTOR);
    
		(CStateManager.Instance()).RestoreTransform(D3DTS_TEXTURE0);
		(CStateManager.Instance()).RestoreTransform(D3DTS_TEXTURE1);
    
		(CStateManager.Instance()).RestoreTextureStageState(0, D3DTSS_TEXCOORDINDEX);
		(CStateManager.Instance()).RestoreTextureStageState(0, D3DTSS_TEXTURETRANSFORMFLAGS);
		(CStateManager.Instance()).RestoreTextureStageState(1, D3DTSS_TEXCOORDINDEX);
		(CStateManager.Instance()).RestoreTextureStageState(1, D3DTSS_TEXTURETRANSFORMFLAGS);
    
		(CStateManager.Instance()).RestoreRenderState(D3DRS_ALPHABLENDENABLE);
		(CStateManager.Instance()).RestoreRenderState(D3DRS_ALPHATESTENABLE);
		(CStateManager.Instance()).RestoreRenderState(D3DRS_ALPHAREF);
		(CStateManager.Instance()).RestoreRenderState(D3DRS_ALPHAFUNC);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __HardwareTransformPatch_RenderPatchSplat(int patchnum, ushort wPrimitiveCount, D3DPRIMITIVETYPE ePrimitiveType)
	{
		Debug.Assert(null != m_pTerrainPatchProxyList && "__HardwareTransformPatch_RenderPatchSplat");
		CTerrainPatchProxy pTerrainPatchProxy = m_pTerrainPatchProxyList[patchnum];
    
		if (!pTerrainPatchProxy.isUsed())
		{
			return;
		}
    
		int sPatchNum = pTerrainPatchProxy.GetPatchNum();
		if (sPatchNum < 0)
		{
			return;
		}
    
		byte ucTerrainNum = pTerrainPatchProxy.GetTerrainNum();
		if (0xFF == ucTerrainNum)
		{
			return;
		}
    
		CTerrain pTerrain;
		if (!GetTerrainPointer(ucTerrainNum, pTerrain))
		{
			return;
		}
    
		uint dwFogColor;
		if (mc_pEnvironmentData)
		{
			dwFogColor = mc_pEnvironmentData.FogColor;
		}
		else
		{
			dwFogColor = 0xffffffff;
		}
    
		ushort wCoordX;
		ushort wCoordY;
		pTerrain.GetCoordinate(wCoordX, wCoordY);
    
		TTerrainSplatPatch rTerrainSplatPatch = pTerrain.GetTerrainSplatPatch();
    
		_D3DMATRIX matTexTransform = new _D3DMATRIX();
		_D3DMATRIX matSplatAlphaTexTransform = new _D3DMATRIX();
		_D3DMATRIX matSplatColorTexTransform = new _D3DMATRIX();
		m_matWorldForCommonUse._41 = -(float)(wCoordX * CTerrainImpl.TERRAIN_XSIZE);
		m_matWorldForCommonUse._42 = (float)(wCoordY * CTerrainImpl.TERRAIN_YSIZE);
		D3DXMatrixMultiply(matTexTransform, m_matViewInverse, m_matWorldForCommonUse);
		D3DXMatrixMultiply(matSplatAlphaTexTransform, matTexTransform, m_matSplatAlpha);
		(CStateManager.Instance()).SetTransform(D3DTS_TEXTURE1, matSplatAlphaTexTransform);
    
		_D3DMATRIX matTiling = new _D3DMATRIX();
		D3DXMatrixScaling(matTiling, 1.0f / 640.0f, -1.0f / 640.0f, 0.0f);
		matTiling._41 = 0.0f;
		matTiling._42 = 0.0f;
    
		D3DXMatrixMultiply(matSplatColorTexTransform, m_matViewInverse, matTiling);
		(CStateManager.Instance()).SetTransform(D3DTS_TEXTURE0, matSplatColorTexTransform);
    
		CGraphicVertexBuffer pkVB = pTerrainPatchProxy.HardwareTransformPatch_GetVertexBufferPtr();
		if (pkVB == null)
		{
			return;
		}
    
		(CStateManager.Instance()).SetStreamSource(0, pkVB.GetD3DVertexBuffer(), m_iPatchTerrainVertexSize);
    
		(CStateManager.Instance()).SetRenderState(D3DRS_LIGHTING, false);
    
		int iPrevRenderedSplatNum = m_iRenderedSplatNum;
    
		bool isFirst = true;
		for (uint j = 1; j < pTerrain.GetNumTextures(); ++j)
		{
			TTerainSplat rSplat = rTerrainSplatPatch.Splats[j];
    
			if (!rSplat.Active)
			{
				continue;
			}
    
			if (rTerrainSplatPatch.PatchTileCount[sPatchNum][j] == 0)
			{
				continue;
			}
    
			STerrainTexture rTexture = m_TextureSet.GetTexture(j);
    
			D3DXMatrixMultiply(matSplatColorTexTransform, m_matViewInverse, rTexture.m_matTransform);
			(CStateManager.Instance()).SetTransform(D3DTS_TEXTURE0, matSplatColorTexTransform);
			if (isFirst)
			{
				(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_ALPHAOP, D3DTOP_DISABLE);
				(CStateManager.Instance()).SetTexture(0, rTexture.pd3dTexture);
				(CStateManager.Instance()).SetTexture(1, rSplat.pd3dTexture);
				(CStateManager.Instance()).DrawIndexedPrimitive(ePrimitiveType, 0, m_iPatchTerrainVertexCount, 0, wPrimitiveCount);
				(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_ALPHAOP, D3DTOP_SELECTARG1);
				isFirst = false;
			}
			else
			{
				(CStateManager.Instance()).SetTexture(0, rTexture.pd3dTexture);
				(CStateManager.Instance()).SetTexture(1, rSplat.pd3dTexture);
				(CStateManager.Instance()).DrawIndexedPrimitive(ePrimitiveType, 0, m_iPatchTerrainVertexCount, 0, wPrimitiveCount);
			}
    
			List<int>.Enumerator aIterator = std::find(m_RenderedTextureNumVector.begin(), m_RenderedTextureNumVector.end(), (int)j);
			if (aIterator == m_RenderedTextureNumVector.end())
			{
				m_RenderedTextureNumVector.push_back(j);
			}
			++m_iRenderedSplatNum;
			if (m_iRenderedSplatNum >= m_iSplatLimit)
			{
				break;
			}
    
		}
    
		if (m_bDrawShadow)
		{
			(CStateManager.Instance()).SetRenderState(D3DRS_LIGHTING, true);
    
			(CStateManager.Instance()).SetRenderState(D3DRS_FOGCOLOR, 0xFFFFFFFF);
			(CStateManager.Instance()).SetRenderState(D3DRS_SRCBLEND, D3DBLEND_ZERO);
			(CStateManager.Instance()).SetRenderState(D3DRS_DESTBLEND, D3DBLEND_SRCCOLOR);
    
			_D3DMATRIX matShadowTexTransform = new _D3DMATRIX();
			D3DXMatrixMultiply(matShadowTexTransform, matTexTransform, m_matStaticShadow);
    
			(CStateManager.Instance()).SetTransform(D3DTS_TEXTURE0, matShadowTexTransform);
			 (CStateManager.Instance()).SetTexture(0, pTerrain.GetShadowTexture());
    
			(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLORARG1, DefineConstants.D3DTA_TEXTURE);
			(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLORARG2, DefineConstants.D3DTA_CURRENT);
			(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLOROP, D3DTOP_MODULATE);
			(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_ALPHAARG1, DefineConstants.D3DTA_TEXTURE);
			(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_ALPHAARG2, DefineConstants.D3DTA_CURRENT);
			(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_ALPHAOP, D3DTOP_DISABLE);
			(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_ADDRESSU, D3DTADDRESS_CLAMP);
			(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_ADDRESSV, D3DTADDRESS_CLAMP);
    
			if (m_bDrawChrShadow)
			{
				(CStateManager.Instance()).SetTransform(D3DTS_TEXTURE1, m_matDynamicShadow);
    
				 (CStateManager.Instance()).SetTexture(1, m_lpCharacterShadowMapTexture);
				(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_COLORARG1, DefineConstants.D3DTA_TEXTURE);
				(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_COLORARG2, DefineConstants.D3DTA_CURRENT);
				(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_COLOROP, D3DTOP_MODULATE);
				(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_ALPHAOP, D3DTOP_DISABLE);
				(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_ADDRESSU, D3DTADDRESS_CLAMP);
				(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_ADDRESSV, D3DTADDRESS_CLAMP);
			}
			else
			{
				(CStateManager.Instance()).SetTexture(1, null);
			}
    
			ms_faceCount += wPrimitiveCount;
			(CStateManager.Instance()).DrawIndexedPrimitive(ePrimitiveType, 0, m_iPatchTerrainVertexCount, 0, wPrimitiveCount);
			  ++m_iRenderedSplatNum;
    
			if (m_bDrawChrShadow)
			{
				(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_COLORARG1, DefineConstants.D3DTA_CURRENT);
				(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_COLOROP, D3DTOP_SELECTARG1);
				(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_ALPHAARG1, DefineConstants.D3DTA_TEXTURE);
				(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_ALPHAOP, D3DTOP_SELECTARG1);
			}
    
			 (CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLORARG1, DefineConstants.D3DTA_TEXTURE);
			(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLORARG2, DefineConstants.D3DTA_CURRENT);
			(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLOROP, D3DTOP_MODULATE);
			(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_ALPHAARG1, DefineConstants.D3DTA_TEXTURE);
			(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_ALPHAOP, D3DTOP_SELECTARG1);
			(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_ADDRESSU, D3DTADDRESS_WRAP);
			(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_ADDRESSV, D3DTADDRESS_WRAP);
    
    
			(CStateManager.Instance()).SetRenderState(D3DRS_SRCBLEND, D3DBLEND_SRCALPHA);
			(CStateManager.Instance()).SetRenderState(D3DRS_DESTBLEND, D3DBLEND_INVSRCALPHA);
			(CStateManager.Instance()).SetRenderState(D3DRS_FOGCOLOR, dwFogColor);
    
			(CStateManager.Instance()).SetRenderState(D3DRS_LIGHTING, false);
		}
		++m_iRenderedPatchNum;
    
		int iCurRenderedSplatNum = m_iRenderedSplatNum - iPrevRenderedSplatNum;
    
		m_iRenderedSplatNumSqSum += iCurRenderedSplatNum * iCurRenderedSplatNum;
    
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __HardwareTransformPatch_RenderPatchNone(int patchnum, ushort wPrimitiveCount, D3DPRIMITIVETYPE ePrimitiveType)
	{
		Debug.Assert(null != m_pTerrainPatchProxyList && "__HardwareTransformPatch_RenderPatchNone");
		CTerrainPatchProxy pTerrainPatchProxy = m_pTerrainPatchProxyList[patchnum];
    
		if (!pTerrainPatchProxy.isUsed())
		{
			return;
		}
    
		CGraphicVertexBuffer pkVB = pTerrainPatchProxy.HardwareTransformPatch_GetVertexBufferPtr();
		if (pkVB == null)
		{
			return;
		}
    
		(CStateManager.Instance()).SetStreamSource(0, pkVB.GetD3DVertexBuffer(), m_iPatchTerrainVertexSize);
		(CStateManager.Instance()).DrawIndexedPrimitive(ePrimitiveType, 0, m_iPatchTerrainVertexCount, 0, wPrimitiveCount);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __RenderTerrain_RenderSoftwareTransformPatch()
	{
		SoftwareTransformPatch_SRenderState kTPRS = new SoftwareTransformPatch_SRenderState();
    
		uint dwFogEnable = (CStateManager.Instance()).GetRenderState(D3DRS_FOGENABLE);
    
		__SoftwareTransformPatch_ApplyRenderState();
    
		__SoftwareTransformPatch_BuildPipeline(kTPRS);
    
		Tuple<float, int> fog_far = new Tuple<float, int>(kTPRS.m_fFogFarDistance+800.0f, 0);
		Tuple<float, int> fog_near = new Tuple<float, int>(kTPRS.m_fFogNearDistance-3200.0f, 0);
    
		List<Tuple<float,int>>.Enumerator far_it = std::upper_bound(m_PatchVector.begin(),m_PatchVector.end(),fog_far);
		List<Tuple<float,int>>.Enumerator near_it = std::upper_bound(m_PatchVector.begin(),m_PatchVector.end(),fog_near);
    
		ushort wPrimitiveCount;
		D3DPRIMITIVETYPE ePrimitiveType = new D3DPRIMITIVETYPE();
    
		byte byCUrrentLODLevel = 0;
    
		float fLODLevel1Distance = __GetNoFogDistance();
		float fLODLevel2Distance = __GetFogDistance();
    
		SelectIndexBuffer(0, wPrimitiveCount, ePrimitiveType);
    
		(CStateManager.Instance()).SetVertexShader(DefineConstants.D3DFVF_XYZRHW | DefineConstants.D3DFVF_DIFFUSE | DefineConstants.D3DFVF_SPECULAR | DefineConstants.D3DFVF_TEX2);
    
		List<Tuple<float, int>>.Enumerator it = m_PatchVector.begin();
    
		for (; it != near_it; ++it)
		{
			if (byCUrrentLODLevel == 0 && fLODLevel1Distance <= it.first)
			{
				byCUrrentLODLevel = 1;
				SelectIndexBuffer(1, wPrimitiveCount, ePrimitiveType);
			}
			else if (byCUrrentLODLevel == 1 && fLODLevel2Distance <= it.first)
			{
				byCUrrentLODLevel = 2;
				SelectIndexBuffer(2, wPrimitiveCount, ePrimitiveType);
			}
    
			__SoftwareTransformPatch_RenderPatchSplat(kTPRS, it.second, wPrimitiveCount, ePrimitiveType, false);
			if (m_iRenderedSplatNum >= m_iSplatLimit)
			{
				break;
			}
    
		}
    
		if (m_iRenderedSplatNum < m_iSplatLimit)
		{
			for (it = near_it; it != far_it; ++it)
			{
				if (byCUrrentLODLevel == 0 && fLODLevel1Distance <= it.first)
				{
					byCUrrentLODLevel = 1;
					SelectIndexBuffer(1, wPrimitiveCount, ePrimitiveType);
				}
				else if (byCUrrentLODLevel == 1 && fLODLevel2Distance <= it.first)
				{
					byCUrrentLODLevel = 2;
					SelectIndexBuffer(2, wPrimitiveCount, ePrimitiveType);
				}
    
				__SoftwareTransformPatch_RenderPatchSplat(kTPRS, it.second, wPrimitiveCount, ePrimitiveType, true);
    
				if (m_iRenderedSplatNum >= m_iSplatLimit)
				{
					break;
				}
    
			}
		}
    
    
		(CStateManager.Instance()).SetTexture(0, null);
		(CStateManager.Instance()).SetTexture(1, null);
    
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLORARG1, DefineConstants.D3DTA_TFACTOR);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLOROP, D3DTOP_SELECTARG1);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_ALPHAOP, D3DTOP_DISABLE);
    
		(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_COLOROP, D3DTOP_DISABLE);
		(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_ALPHAOP, D3DTOP_DISABLE);
    
		(CStateManager.Instance()).SetVertexShader(DefineConstants.D3DFVF_XYZRHW);
    
		if (IsFastTNL())
		{
			if (byCUrrentLODLevel != 2)
			{
				byCUrrentLODLevel = 2;
				SelectIndexBuffer(2, wPrimitiveCount, ePrimitiveType);
			}
    
			if (m_iRenderedSplatNum < m_iSplatLimit)
			{
				for (it = far_it; it.MoveNext();)
				{
					__SoftwareTransformPatch_RenderPatchNone(kTPRS, it.second, wPrimitiveCount, ePrimitiveType);
    
					if (m_iRenderedSplatNum >= m_iSplatLimit)
					{
						break;
					}
    
				}
			}
		}
    
		__SoftwareTransformPatch_RestoreRenderState(dwFogEnable);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __SoftwareTransformPatch_RenderPatchSplat(SoftwareTransformPatch_SRenderState rkTPRS, int patchnum, ushort wPrimitiveCount, D3DPRIMITIVETYPE ePrimitiveType, bool isFogEnable)
	{
		Debug.Assert(null != m_pTerrainPatchProxyList && "CMapOutdoor::__SoftwareTransformPatch_RenderPatchSplat");
    
		CTerrainPatchProxy pTerrainPatchProxy = m_pTerrainPatchProxyList[patchnum];
    
		if (!pTerrainPatchProxy.isUsed())
		{
			return;
		}
    
		bool isDynamicShadow = pTerrainPatchProxy.IsIn(rkTPRS.m_v3Player, 3000.0f);
    
		if (!m_bDrawChrShadow)
		{
			isDynamicShadow = false;
		}
    
		int sPatchNum = pTerrainPatchProxy.GetPatchNum();
    
		if (sPatchNum < 0)
		{
			return;
		}
    
		byte ucTerrainNum = pTerrainPatchProxy.GetTerrainNum();
    
		if (0xFF == ucTerrainNum)
		{
			return;
		}
    
		CTerrain pTerrain;
		if (!GetTerrainPointer(ucTerrainNum, pTerrain))
		{
			return;
		}
    
		ushort wCoordX;
		ushort wCoordY;
		pTerrain.GetCoordinate(wCoordX, wCoordY);
    
		TTerrainSplatPatch rTerrainSplatPatch = pTerrain.GetTerrainSplatPatch();
    
		SoftwareTransformPatch_STLVertex[] akTransVertex = Arrays.InitializeWithDefaultInstances<SoftwareTransformPatch_STLVertex>(CTerrainPatch.TERRAIN_VERTEX_COUNT);
		if (!__SoftwareTransformPatch_SetTransform(rkTPRS, akTransVertex, pTerrainPatchProxy, wCoordX, wCoordY, isFogEnable, isDynamicShadow))
		{
			return;
		}
    
		if (!__SoftwareTransformPatch_SetSplatStream(akTransVertex))
		{
			return;
		}
    
		if (isFogEnable)
		{
			(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLORARG1, DefineConstants.D3DTA_TEXTURE);
			(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLORARG2, DefineConstants.D3DTA_TFACTOR);
			(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLOROP, D3DTOP_BLENDDIFFUSEALPHA);
		}
		else
		{
			(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLORARG1, DefineConstants.D3DTA_TEXTURE);
			(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLORARG2, DefineConstants.D3DTA_DIFFUSE);
			(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLOROP, D3DTOP_SELECTARG1);
		}
    
		int iPrevRenderedSplatNum = m_iRenderedSplatNum;
    
		bool isFirst = true;
		for (uint j = 1; j < pTerrain.GetNumTextures(); ++j)
		{
			TTerainSplat rSplat = rTerrainSplatPatch.Splats[j];
    
			if (!rSplat.Active)
			{
				continue;
			}
    
			if (rTerrainSplatPatch.PatchTileCount[sPatchNum][j] == 0)
			{
				continue;
			}
    
			TTerrainTexture rTexture = m_TextureSet.GetTexture(j);
    
			if (isFirst)
			{
				(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_ALPHAOP, D3DTOP_SELECTARG2);
				(CStateManager.Instance()).SetTexture(0, rTexture.pd3dTexture);
				(CStateManager.Instance()).SetTexture(1, rSplat.pd3dTexture);
				(CStateManager.Instance()).DrawIndexedPrimitive(ePrimitiveType, 0, m_iPatchTerrainVertexCount, 0, wPrimitiveCount);
				(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_ALPHAOP, D3DTOP_SELECTARG1);
				isFirst = false;
			}
			else
			{
				(CStateManager.Instance()).SetTexture(0, rTexture.pd3dTexture);
				(CStateManager.Instance()).SetTexture(1, rSplat.pd3dTexture);
				(CStateManager.Instance()).DrawIndexedPrimitive(ePrimitiveType, 0, m_iPatchTerrainVertexCount, 0, wPrimitiveCount);
			}
    
			List<int>.Enumerator aIterator = std::find(m_RenderedTextureNumVector.begin(), m_RenderedTextureNumVector.end(), (int)j);
			if (aIterator == m_RenderedTextureNumVector.end())
			{
				m_RenderedTextureNumVector.push_back(j);
			}
			++m_iRenderedSplatNum;
			if (m_iRenderedSplatNum >= m_iSplatLimit)
			{
				break;
			}
		}
    
		if (m_bDrawShadow)
		{
			__SoftwareTransformPatch_SetShadowStream(akTransVertex);
			__SoftwareTransformPatch_ApplyStaticShadowRenderState();
    
			if (isDynamicShadow)
			{
				__SoftwareTransformPatch_ApplyDynamicShadowRenderState();
			}
			else
			{
				__SoftwareTransformPatch_ApplyFogShadowRenderState();
			}
    
			if (isFogEnable)
			{
				(CStateManager.Instance()).SetRenderState(D3DRS_FOGENABLE, true);
				(CStateManager.Instance()).SetRenderState(D3DRS_FOGCOLOR, 0xFFFFFFFF);
				(CStateManager.Instance()).SetTexture(0, pTerrain.GetShadowTexture());
				(CStateManager.Instance()).DrawIndexedPrimitive(ePrimitiveType, 0, m_iPatchTerrainVertexCount, 0, wPrimitiveCount);
				(CStateManager.Instance()).SetRenderState(D3DRS_FOGCOLOR, rkTPRS.m_dwFogColor);
				(CStateManager.Instance()).SetRenderState(D3DRS_FOGENABLE, false);
			}
			else
			{
				(CStateManager.Instance()).SetTexture(0, pTerrain.GetShadowTexture());
				(CStateManager.Instance()).DrawIndexedPrimitive(ePrimitiveType, 0, m_iPatchTerrainVertexCount, 0, wPrimitiveCount);
			}
    
			if (isDynamicShadow)
			{
				__SoftwareTransformPatch_RestoreDynamicShadowRenderState();
			}
			else
			{
				__SoftwareTransformPatch_RestoreFogShadowRenderState();
			}
    
			ms_faceCount += wPrimitiveCount;
			  ++m_iRenderedSplatNum;
    
    
    
			__SoftwareTransformPatch_RestoreStaticShadowRenderState();
		}
    
		++m_iRenderedPatchNum;
    
		int iCurRenderedSplatNum = m_iRenderedSplatNum - iPrevRenderedSplatNum;
    
		m_iRenderedSplatNumSqSum += iCurRenderedSplatNum * iCurRenderedSplatNum;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __SoftwareTransformPatch_RenderPatchNone(SoftwareTransformPatch_SRenderState rkTPRS, int patchnum, ushort wPrimitiveCount, D3DPRIMITIVETYPE ePrimitiveType)
	{
		Debug.Assert(null != m_pTerrainPatchProxyList && "CMapOutdoor::__SoftwareTransformPatch_RenderPatchNone");
    
		CTerrainPatchProxy pTerrainPatchProxy = m_pTerrainPatchProxyList[patchnum];
    
		if (!pTerrainPatchProxy.isUsed())
		{
			return;
		}
    
		int sPatchNum = pTerrainPatchProxy.GetPatchNum();
		if (sPatchNum < 0)
		{
			return;
		}
    
		byte ucTerrainNum = pTerrainPatchProxy.GetTerrainNum();
		if (0xFF == ucTerrainNum)
		{
			return;
		}
    
		CTerrain pTerrain;
		if (!GetTerrainPointer(ucTerrainNum, pTerrain))
		{
			return;
		}
    
		ushort wCoordX;
		ushort wCoordY;
		pTerrain.GetCoordinate(wCoordX, wCoordY);
    
		SoftwareTransformPatch_SSourceVertex[] akSrcVertex = pTerrainPatchProxy.SoftwareTransformPatch_GetTerrainVertexDataPtr();
		if (!akSrcVertex)
		{
			return;
		}
    
		float fScreenHalfWidth = rkTPRS.m_fScreenHalfWidth;
		float fScreenHalfHeight = rkTPRS.m_fScreenHalfHeight;
    
		_D3DMATRIX m4Frustum = rkTPRS.m_m4Frustum;
    
		SoftwareTransformPatch_STVertex[] akTransVertex = Arrays.InitializeWithDefaultInstances<SoftwareTransformPatch_STVertex>(CTerrainPatch.TERRAIN_VERTEX_COUNT);
    
		D3DXVECTOR4 akPosition = (D3DXVECTOR4)akTransVertex;
		D3DXVECTOR4 pkPosition;
		for (uint uIndex = 0; uIndex != CTerrainPatch.TERRAIN_VERTEX_COUNT; ++uIndex)
		{
			pkPosition = akPosition + uIndex;
			D3DXVec3Transform(pkPosition, akSrcVertex[uIndex].kPosition, m4Frustum);
			pkPosition.w = 1.0f / pkPosition.w;
			pkPosition.z *= pkPosition.w;
			pkPosition.y = (pkPosition.y * pkPosition.w - 1.0f) * fScreenHalfHeight;
			pkPosition.x = (pkPosition.x * pkPosition.w + 1.0f) * fScreenHalfWidth;
		}
    
    
		IDirect3DVertexBuffer8 pkVB = m_kSTPD.m_pkVBNone[m_kSTPD.m_dwNonePos++];
		m_kSTPD.m_dwNonePos %= SoftwareTransformPatch_SData.NONE_VB_NUM;
		if (pkVB == null)
		{
			return;
		}
    
		uint dwVBSize = sizeof(SoftwareTransformPatch_STVertex) * CTerrainPatch.TERRAIN_VERTEX_COUNT;
		SoftwareTransformPatch_STVertex akDstVertex;
		if (FAILED(pkVB.Lock(0, dwVBSize, (byte) akDstVertex, DefineConstants.D3DLOCK_DISCARD)))
		{
			return;
		}
    
	//# Laniatus Games Studio Inc. | TODO TASK: The memory management function 'memcpy' has no equivalent in C#:
		memcpy(akDstVertex, akTransVertex, dwVBSize);
    
		pkVB.Unlock();
    
		(CStateManager.Instance()).SetStreamSource(0, pkVB, sizeof(SoftwareTransformPatch_STVertex));
		(CStateManager.Instance()).DrawIndexedPrimitive(ePrimitiveType, 0, m_iPatchTerrainVertexCount, 0, wPrimitiveCount);
		ms_faceCount += wPrimitiveCount;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __SoftwareTransformPatch_ApplyStaticShadowRenderState()
	{
		(CStateManager.Instance()).SetRenderState(D3DRS_SRCBLEND, D3DBLEND_ZERO);
		(CStateManager.Instance()).SetRenderState(D3DRS_DESTBLEND, D3DBLEND_SRCCOLOR);
    
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLORARG1, DefineConstants.D3DTA_TEXTURE);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLORARG2, DefineConstants.D3DTA_DIFFUSE);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLOROP, D3DTOP_MODULATE);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_ALPHAARG1, DefineConstants.D3DTA_TEXTURE);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_ALPHAOP, D3DTOP_SELECTARG1);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_ADDRESSU, D3DTADDRESS_CLAMP);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_ADDRESSV, D3DTADDRESS_CLAMP);
    
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __SoftwareTransformPatch_ApplyDynamicShadowRenderState()
	{
		 (CStateManager.Instance()).SetTexture(1, m_lpCharacterShadowMapTexture);
		(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_COLORARG1, DefineConstants.D3DTA_TEXTURE);
		(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_COLORARG2, DefineConstants.D3DTA_CURRENT);
		(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_COLOROP, D3DTOP_MODULATE);
		(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_ALPHAARG1, DefineConstants.D3DTA_CURRENT);
		(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_ALPHAOP, D3DTOP_SELECTARG1);
    
		(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_ADDRESSU, D3DTADDRESS_CLAMP);
		(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_ADDRESSV, D3DTADDRESS_CLAMP);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __SoftwareTransformPatch_ApplyFogShadowRenderState()
	{
		(CStateManager.Instance()).SetTexture(1, null);
		(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_COLORARG1, DefineConstants.D3DTA_CURRENT);
		(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_COLOROP, D3DTOP_SELECTARG1);
		(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_ALPHAARG1, DefineConstants.D3DTA_CURRENT);
		(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_ALPHAOP, D3DTOP_SELECTARG1);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __SoftwareTransformPatch_RestoreStaticShadowRenderState()
	{
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLORARG1, DefineConstants.D3DTA_TEXTURE);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLOROP, D3DTOP_SELECTARG1);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_ALPHAARG1, DefineConstants.D3DTA_TEXTURE);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_ALPHAOP, D3DTOP_SELECTARG1);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_ADDRESSU, D3DTADDRESS_WRAP);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_ADDRESSV, D3DTADDRESS_WRAP);
    
		(CStateManager.Instance()).SetRenderState(D3DRS_SRCBLEND, D3DBLEND_SRCALPHA);
		(CStateManager.Instance()).SetRenderState(D3DRS_DESTBLEND, D3DBLEND_INVSRCALPHA);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __SoftwareTransformPatch_RestoreDynamicShadowRenderState()
	{
		(CStateManager.Instance()).SetTexture(1, null);
		(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_COLORARG1, DefineConstants.D3DTA_CURRENT);
		(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_COLOROP, D3DTOP_SELECTARG1);
		(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_ALPHAARG1, DefineConstants.D3DTA_TEXTURE);
		(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_ALPHAOP, D3DTOP_SELECTARG1);
    
		(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_ADDRESSU, D3DTADDRESS_CLAMP);
		(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_ADDRESSV, D3DTADDRESS_CLAMP);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __SoftwareTransformPatch_RestoreFogShadowRenderState()
	{
		(CStateManager.Instance()).SetRenderState(D3DRS_FOGENABLE, false);
    
		(CStateManager.Instance()).SetTexture(1, null);
		(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_COLORARG1, DefineConstants.D3DTA_CURRENT);
		(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_COLOROP, D3DTOP_SELECTARG1);
		(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_ALPHAARG1, DefineConstants.D3DTA_TEXTURE);
		(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_ALPHAOP, D3DTOP_SELECTARG1);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __SoftwareTransformPatch_ApplyRenderState()
	{
		uint dwFogColor = 0xffffffff;
		if (mc_pEnvironmentData)
		{
			dwFogColor = mc_pEnvironmentData.FogColor;
		}
    
		bool isSoftwareVertexClipping = false;
		if (!IsTLVertexClipping())
		{
			isSoftwareVertexClipping = true;
		}
    
		(CStateManager.Instance()).SaveRenderState(D3DRS_SOFTWAREVERTEXPROCESSING, isSoftwareVertexClipping);
    
		(CStateManager.Instance()).SaveRenderState(D3DRS_ALPHABLENDENABLE, true);
		(CStateManager.Instance()).SaveRenderState(D3DRS_ALPHATESTENABLE, true);
		(CStateManager.Instance()).SaveRenderState(D3DRS_ALPHAREF, 0x00000000);
		(CStateManager.Instance()).SaveRenderState(D3DRS_ALPHAFUNC, D3DCMP_GREATER);
    
		(CStateManager.Instance()).SaveRenderState(D3DRS_TEXTUREFACTOR, dwFogColor);
		(CStateManager.Instance()).SetRenderState(D3DRS_LIGHTING, false);
		(CStateManager.Instance()).SetRenderState(D3DRS_FOGENABLE, false);
    
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLORARG1, DefineConstants.D3DTA_TEXTURE);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLORARG2, DefineConstants.D3DTA_DIFFUSE);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLOROP, D3DTOP_SELECTARG1);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_ALPHAARG1, DefineConstants.D3DTA_TEXTURE);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_ALPHAOP, D3DTOP_SELECTARG1);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_ADDRESSU, D3DTADDRESS_WRAP);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_ADDRESSV, D3DTADDRESS_WRAP);
		(CStateManager.Instance()).SetBestFiltering(0);
    
		(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_COLORARG1, DefineConstants.D3DTA_CURRENT);
		(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_COLORARG2, DefineConstants.D3DTA_TEXTURE);
		(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_COLOROP, D3DTOP_SELECTARG1);
		(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_ALPHAARG1, DefineConstants.D3DTA_TEXTURE);
		(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_ALPHAARG2, DefineConstants.D3DTA_CURRENT);
		(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_ALPHAOP, D3DTOP_SELECTARG1);
		(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_ADDRESSU, D3DTADDRESS_CLAMP);
		(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_ADDRESSV, D3DTADDRESS_CLAMP);
		(CStateManager.Instance()).SetBestFiltering(1);
    
		CSpeedTreeWrapper.ms_bSelfShadowOn = true;
    
		m_iRenderedSplatNumSqSum = 0;
		m_iRenderedPatchNum = 0;
		m_iRenderedSplatNum = 0;
		m_RenderedTextureNumVector.clear();
    
		m_matWorldForCommonUse._41 = 0.0f;
		m_matWorldForCommonUse._42 = 0.0f;
		(CStateManager.Instance()).SetTransform((D3DTRANSFORMSTATETYPE)(0 + 256), m_matWorldForCommonUse);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __SoftwareTransformPatch_RestoreRenderState(uint dwFogEnable)
	{
		(CStateManager.Instance()).SetRenderState(D3DRS_LIGHTING, true);
    
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLORARG1, DefineConstants.D3DTA_TEXTURE);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLORARG2, DefineConstants.D3DTA_CURRENT);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLOROP, D3DTOP_MODULATE);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_ALPHAARG1, DefineConstants.D3DTA_TEXTURE);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_ALPHAOP, D3DTOP_SELECTARG1);
    
		(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_COLORARG1, DefineConstants.D3DTA_CURRENT);
		(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_COLOROP, D3DTOP_SELECTARG1);
		(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_ALPHAARG1, DefineConstants.D3DTA_TEXTURE);
		(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_ALPHAOP, D3DTOP_SELECTARG1);
    
		(CStateManager.Instance()).SetRenderState(D3DRS_FOGENABLE, dwFogEnable);
    
		std::sort(m_RenderedTextureNumVector.begin(),m_RenderedTextureNumVector.end());
    
		(CStateManager.Instance()).RestoreRenderState(D3DRS_TEXTUREFACTOR);
    
		(CStateManager.Instance()).RestoreRenderState(D3DRS_ALPHABLENDENABLE);
		(CStateManager.Instance()).RestoreRenderState(D3DRS_ALPHATESTENABLE);
		(CStateManager.Instance()).RestoreRenderState(D3DRS_ALPHAREF);
		(CStateManager.Instance()).RestoreRenderState(D3DRS_ALPHAFUNC);
    
		(CStateManager.Instance()).RestoreRenderState(D3DRS_SOFTWAREVERTEXPROCESSING);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __SoftwareTransformPatch_BuildPipeline(SoftwareTransformPatch_SRenderState rkTPRS)
	{
	//# Laniatus Games Studio Inc. | TODO TASK: The memory management function 'memset' has no equivalent in C#:
		memset(rkTPRS, 0, sizeof(SoftwareTransformPatch_SRenderState));
    
		if (mc_pEnvironmentData)
		{
			rkTPRS.m_dwFogColor = mc_pEnvironmentData.FogColor;
			rkTPRS.m_fFogNearDistance = mc_pEnvironmentData.GetFogNearDistance();
			rkTPRS.m_fFogFarDistance = mc_pEnvironmentData.GetFogFarDistance();
		}
		else
		{
			rkTPRS.m_dwFogColor = 0xffffffff;
			rkTPRS.m_fFogNearDistance = 5000.0f;
			rkTPRS.m_fFogFarDistance = 10000.0f;
		}
    
		uint uScreenWidth;
		uint uScreenHeight;
		CScreen.GetBackBufferSize(uScreenWidth, uScreenHeight);
    
		rkTPRS.m_fScreenHalfWidth = +(float)uScreenWidth / 2.0f;
		rkTPRS.m_fScreenHalfHeight = -(float)uScreenHeight / 2.0f;
    
		(CStateManager.Instance()).GetLight(0, rkTPRS.m_kLight);
		(CStateManager.Instance()).GetMaterial(rkTPRS.m_kMtrl);
    
		_D3DMATRIX m4View = new _D3DMATRIX();
		(CStateManager.Instance()).GetTransform(D3DTS_VIEW, m4View);
		_D3DMATRIX m4Proj = new _D3DMATRIX();
		(CStateManager.Instance()).GetTransform(D3DTS_PROJECTION, m4Proj);
    
		D3DXMatrixMultiply(rkTPRS.m_m4Frustum, m4View, m4Proj);
    
		rkTPRS.m_v3Player.x = +m_v3Player.x;
		rkTPRS.m_v3Player.y = -m_v3Player.y;
		rkTPRS.m_v3Player.z = +m_v3Player.z;
    
		rkTPRS.m_m4Proj = m4Proj;
		rkTPRS.m_m4DynamicShadow = m_matLightView * m_matDynamicShadowScale;
    
		_D3DVECTOR kFogNearVector = new _D3DVECTOR();
		D3DXVec3TransformCoord(kFogNearVector, D3DXVECTOR3(0.0f, 0.0f, -rkTPRS.m_fFogNearDistance), rkTPRS.m_m4Proj);
    
		_D3DVECTOR kFogFarVector = new _D3DVECTOR();
		D3DXVec3TransformCoord(kFogFarVector, D3DXVECTOR3(0.0f, 0.0f, -rkTPRS.m_fFogFarDistance), rkTPRS.m_m4Proj);
    
		float fFogNear = kFogNearVector.z;
		float fFogFar = kFogFarVector.z;
		float fFogLenInv = 1.0f / (fFogFar - fFogNear);
    
		rkTPRS.m_fFogNearTransZ = fFogNear;
		rkTPRS.m_fFogFarTransZ = fFogFar;
		rkTPRS.m_fFogLenInv = fFogLenInv;
    
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool __SoftwareTransformPatch_SetTransform(SoftwareTransformPatch_SRenderState rkTPRS, SoftwareTransformPatch_STLVertex[] akTransVertex, CTerrainPatchProxy rkTerrainPatchProxy, uint uTerrainX, uint uTerrainY, bool isFogEnable, bool isDynamicShadow)
	{
		SoftwareTransformPatch_SSourceVertex[] akSrcVertex = rkTerrainPatchProxy.SoftwareTransformPatch_GetTerrainVertexDataPtr();
		if (!akSrcVertex)
		{
			return false;
		}
    
		rkTerrainPatchProxy.SoftwareTransformPatch_UpdateTerrainLighting(m_kSTPD.m_dwLightVersion, rkTPRS.m_kLight, rkTPRS.m_kMtrl);
    
		_D3DVECTOR pkSrcPosition;
    
		float fTilePatternX = +1 / 640.0f;
		float fTilePatternY = -1 / 640.0f;
    
		float fTerrainBaseX = -(float)(uTerrainX * CTerrainImpl.TERRAIN_XSIZE) + m_fTerrainTexCoordBase * 12.30769f;
		float fTerrainBaseY = +(float)(uTerrainY * CTerrainImpl.TERRAIN_YSIZE) + m_fTerrainTexCoordBase * 12.30769f;
    
		float fScreenHalfWidth = rkTPRS.m_fScreenHalfWidth;
		float fScreenHalfHeight = rkTPRS.m_fScreenHalfHeight;
    
		float fAlphaPatternX = m_matSplatAlpha._11;
		float fAlphaPatternY = m_matSplatAlpha._22;
		float fAlphaBiasX = m_matSplatAlpha._41;
		float fAlphaBiasY = m_matSplatAlpha._42;
		float fShadowPatternX = +m_fTerrainTexCoordBase * ((float) CTerrainImpl.PATCH_XSIZE / (CTerrainImpl.XSIZE));
		float fShadowPatternY = -m_fTerrainTexCoordBase * ((float) CTerrainImpl.PATCH_YSIZE / (CTerrainImpl.YSIZE));
    
		_D3DMATRIX m4Frustum = rkTPRS.m_m4Frustum;
    
		if (isFogEnable)
		{
			float fFogCur;
			float fFogFar = rkTPRS.m_fFogFarTransZ;
			float fFogLenInv = rkTPRS.m_fFogLenInv;
    
			float fLocalX;
			float fLocalY;
    
			SoftwareTransformPatch_STLVertex kWorkVertex = new SoftwareTransformPatch_STLVertex();
			for (uint uIndex = 0; uIndex != CTerrainPatch.TERRAIN_VERTEX_COUNT; ++uIndex)
			{
				pkSrcPosition = akSrcVertex[uIndex].kPosition;
				D3DXVec3Transform(kWorkVertex.kPosition, pkSrcPosition, m4Frustum);
				fLocalX = pkSrcPosition.x + fTerrainBaseX;
				fLocalY = pkSrcPosition.y + fTerrainBaseY;
				kWorkVertex.kPosition.w = 1.0f / kWorkVertex.kPosition.w;
				kWorkVertex.kPosition.x *= kWorkVertex.kPosition.w;
				kWorkVertex.kPosition.y *= kWorkVertex.kPosition.w;
				kWorkVertex.kPosition.z *= kWorkVertex.kPosition.w;
				kWorkVertex.kPosition.x = (kWorkVertex.kPosition.x + 1.0f) * fScreenHalfWidth;
				kWorkVertex.kPosition.y = (kWorkVertex.kPosition.y - 1.0f) * fScreenHalfHeight;
				kWorkVertex.dwDiffuse = akSrcVertex[uIndex].dwDiffuse;
				kWorkVertex.kTexTile.x = pkSrcPosition.x * fTilePatternX;
				kWorkVertex.kTexTile.y = pkSrcPosition.y * fTilePatternY;
				kWorkVertex.kTexAlpha.x = fLocalX * fAlphaPatternX + fAlphaBiasX;
				kWorkVertex.kTexAlpha.y = fLocalY * fAlphaPatternY + fAlphaBiasY;
				kWorkVertex.kTexStaticShadow.x = fLocalX * fShadowPatternX;
				kWorkVertex.kTexStaticShadow.y = fLocalY * fShadowPatternY;
				kWorkVertex.kTexDynamicShadow.x = 0.0f;
				kWorkVertex.kTexDynamicShadow.y = 0.0f;
    
				fFogCur = (fFogFar - kWorkVertex.kPosition.z) * fFogLenInv;
				if (fFogCur < 0.0f)
				{
					kWorkVertex.dwFog = kWorkVertex.dwDiffuse = 0x0000000 | (kWorkVertex.dwDiffuse & 0xffffff);
				}
				else if (fFogCur > 1.0f)
				{
					kWorkVertex.dwFog = kWorkVertex.dwDiffuse = 0xFF000000 | (kWorkVertex.dwDiffuse & 0xffffff);
				}
				else
				{
					kWorkVertex.dwFog = kWorkVertex.dwDiffuse = (byte)(255.0f * fFogCur) << 24 | (kWorkVertex.dwDiffuse & 0xffffff);
				}
    
	//# Laniatus Games Studio Inc. | TODO TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'CopyFrom' method should be created:
	//Original Metin2 CPlus Line: *(akTransVertex+uIndex)=kWorkVertex;
				akTransVertex[uIndex].CopyFrom(kWorkVertex);
			}
		}
		else
		{
			float fLocalX;
			float fLocalY;
    
			SoftwareTransformPatch_STLVertex kWorkVertex = new SoftwareTransformPatch_STLVertex();
			for (uint uIndex = 0; uIndex != CTerrainPatch.TERRAIN_VERTEX_COUNT; ++uIndex)
			{
				pkSrcPosition = akSrcVertex[uIndex].kPosition;
				D3DXVec3Transform(kWorkVertex.kPosition, pkSrcPosition, m4Frustum);
				fLocalX = pkSrcPosition.x + fTerrainBaseX;
				fLocalY = pkSrcPosition.y + fTerrainBaseY;
				kWorkVertex.kPosition.w = 1.0f / kWorkVertex.kPosition.w;
				kWorkVertex.kPosition.x *= kWorkVertex.kPosition.w;
				kWorkVertex.kPosition.y *= kWorkVertex.kPosition.w;
				kWorkVertex.kPosition.z *= kWorkVertex.kPosition.w;
				kWorkVertex.kPosition.x = (kWorkVertex.kPosition.x + 1.0f) * fScreenHalfWidth;
				kWorkVertex.kPosition.y = (kWorkVertex.kPosition.y - 1.0f) * fScreenHalfHeight;
				kWorkVertex.dwDiffuse = akSrcVertex[uIndex].dwDiffuse;
				kWorkVertex.dwFog = 0xffffffff;
				kWorkVertex.kTexTile.x = pkSrcPosition.x * fTilePatternX;
				kWorkVertex.kTexTile.y = pkSrcPosition.y * fTilePatternY;
				kWorkVertex.kTexAlpha.x = fLocalX * fAlphaPatternX + fAlphaBiasX;
				kWorkVertex.kTexAlpha.y = fLocalY * fAlphaPatternY + fAlphaBiasY;
				kWorkVertex.kTexStaticShadow.x = fLocalX * fShadowPatternX;
				kWorkVertex.kTexStaticShadow.y = fLocalY * fShadowPatternY;
				kWorkVertex.kTexDynamicShadow.x = 0.0f;
				kWorkVertex.kTexDynamicShadow.y = 0.0f;
    
	//# Laniatus Games Studio Inc. | TODO TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'CopyFrom' method should be created:
	//Original Metin2 CPlus Line: *(akTransVertex+uIndex)=kWorkVertex;
				akTransVertex[uIndex].CopyFrom(kWorkVertex);
			}
		}
    
		if (isDynamicShadow)
		{
			_D3DMATRIX m4DynamicShadow = rkTPRS.m_m4DynamicShadow;
    
			_D3DVECTOR v3Shadow = new _D3DVECTOR();
			for (uint uIndex = 0; uIndex != CTerrainPatch.TERRAIN_VERTEX_COUNT; ++uIndex)
			{
				D3DXVec3TransformCoord(v3Shadow, akSrcVertex[uIndex].kPosition, m4DynamicShadow);
				akTransVertex[uIndex].kTexDynamicShadow.x = v3Shadow.x;
				akTransVertex[uIndex].kTexDynamicShadow.y = v3Shadow.y;
			}
		}
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool __SoftwareTransformPatch_SetSplatStream(SoftwareTransformPatch_STLVertex akSrcVertex)
	{
		IDirect3DVertexBuffer8 pkVB = m_kSTPD.m_pkVBSplat[m_kSTPD.m_dwSplatPos++];
		m_kSTPD.m_dwSplatPos %= SoftwareTransformPatch_SData.SPLAT_VB_NUM;
		if (pkVB == null)
		{
			return false;
		}
    
		uint dwVBSize = sizeof(SoftwareTransformPatch_SSplatVertex) * CTerrainPatch.TERRAIN_VERTEX_COUNT;
		SoftwareTransformPatch_SSplatVertex[] akDstVertex;
		if (FAILED(pkVB.Lock(0, dwVBSize, (byte) akDstVertex, 0)))
		{
			return false;
		}
    
		for (uint uIndex = 0; uIndex != CTerrainPatch.TERRAIN_VERTEX_COUNT; ++uIndex)
		{
	//# Laniatus Games Studio Inc. | TODO TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'CopyFrom' method should be created:
	//Original Metin2 CPlus Line: *(akDstVertex+uIndex)=*((SoftwareTransformPatch_SSplatVertex*)(akSrcVertex+uIndex));
			akDstVertex[uIndex].CopyFrom((SoftwareTransformPatch_SSplatVertex)(akSrcVertex + uIndex));
		}
    
		pkVB.Unlock();
    
		(CStateManager.Instance()).SetStreamSource(0, pkVB, sizeof(SoftwareTransformPatch_SSplatVertex));
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool __SoftwareTransformPatch_SetShadowStream(SoftwareTransformPatch_STLVertex akSrcVertex)
	{
		IDirect3DVertexBuffer8 pkVB = m_kSTPD.m_pkVBSplat[m_kSTPD.m_dwSplatPos++];
		m_kSTPD.m_dwSplatPos %= SoftwareTransformPatch_SData.SPLAT_VB_NUM;
		if (pkVB == null)
		{
			return false;
		}
    
		uint dwVBSize = sizeof(SoftwareTransformPatch_SSplatVertex) * CTerrainPatch.TERRAIN_VERTEX_COUNT;
		SoftwareTransformPatch_SSplatVertex akDstVertex;
		if (FAILED(pkVB.Lock(0, dwVBSize, (byte) akDstVertex, 0)))
		{
			return false;
		}
    
		SoftwareTransformPatch_STLVertex pkSrcVertex;
		SoftwareTransformPatch_SSplatVertex pkDstVertex;
		for (uint uIndex = 0; uIndex != CTerrainPatch.TERRAIN_VERTEX_COUNT; ++uIndex)
		{
			pkSrcVertex = akSrcVertex + uIndex;
			pkDstVertex = akDstVertex + uIndex;
			pkDstVertex.kPosition = pkSrcVertex.kPosition;
			pkDstVertex.dwDiffuse = pkSrcVertex.dwDiffuse;
			pkDstVertex.dwSpecular = pkSrcVertex.dwFog;
			pkDstVertex.kTex1 = pkSrcVertex.kTexStaticShadow;
			pkDstVertex.kTex2 = pkSrcVertex.kTexDynamicShadow;
		}
		pkVB.Unlock();
    
    
		ms_lpd3dDevice.SetStreamSource(0, pkVB, sizeof(SoftwareTransformPatch_SSplatVertex));
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __SoftwareTransformPatch_Initialize()
	{
		{
			for (uint uIndex = 0; uIndex != SoftwareTransformPatch_SData.SPLAT_VB_NUM; ++uIndex)
			{
				m_kSTPD.m_pkVBSplat[uIndex] = null;
			}
			m_kSTPD.m_dwSplatPos = 0;
		}
    
		{
			for (uint uIndex = 0; uIndex != SoftwareTransformPatch_SData.NONE_VB_NUM; ++uIndex)
			{
				m_kSTPD.m_pkVBNone[uIndex] = null;
			}
			m_kSTPD.m_dwNonePos = 0;
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool __SoftwareTransformPatch_Create()
	{
		{
			for (uint uIndex = 0; uIndex != SoftwareTransformPatch_SData.SPLAT_VB_NUM; ++uIndex)
			{
				Debug.Assert(null == m_kSTPD.m_pkVBSplat[uIndex]);
				if (FAILED(ms_lpd3dDevice.CreateVertexBuffer(sizeof(SoftwareTransformPatch_SSplatVertex) * CTerrainPatch.TERRAIN_VERTEX_COUNT, (0x00000200) | (0x00000008), DefineConstants.D3DFVF_XYZRHW | DefineConstants.D3DFVF_DIFFUSE | DefineConstants.D3DFVF_SPECULAR | DefineConstants.D3DFVF_TEX2, D3DPOOL_SYSTEMMEM, m_kSTPD.m_pkVBSplat[uIndex])))
				{
					return false;
				}
			}
		}
    
		{
			for (uint uIndex = 0; uIndex != SoftwareTransformPatch_SData.NONE_VB_NUM; ++uIndex)
			{
				Debug.Assert(null == m_kSTPD.m_pkVBNone[uIndex]);
				if (FAILED(ms_lpd3dDevice.CreateVertexBuffer(sizeof(SoftwareTransformPatch_STVertex) * CTerrainPatch.TERRAIN_VERTEX_COUNT, (0x00000200) | (0x00000008), DefineConstants.D3DFVF_XYZRHW, D3DPOOL_SYSTEMMEM, m_kSTPD.m_pkVBNone[uIndex])))
				{
					return false;
				}
			}
		}
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __SoftwareTransformPatch_Destroy()
	{
		{
			for (uint uIndex = 0; uIndex != SoftwareTransformPatch_SData.SPLAT_VB_NUM; ++uIndex)
			{
				if (m_kSTPD.m_pkVBSplat[uIndex])
				{
					m_kSTPD.m_pkVBSplat[uIndex].Release();
				}
			}
		}
    
		{
			for (uint uIndex = 0; uIndex != SoftwareTransformPatch_SData.NONE_VB_NUM; ++uIndex)
			{
				if (m_kSTPD.m_pkVBNone[uIndex])
				{
					m_kSTPD.m_pkVBNone[uIndex].Release();
				}
			}
		}
		__SoftwareTransformPatch_Initialize();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool Update(float fX, float fY, float fZ)
	{
		_D3DVECTOR v3Player = new _D3DVECTOR(fX, fY, fZ);
    
		m_v3Player = v3Player;
    
    
		uint t1 = ELTimer_GetMSec();
    
		int ix;
		int iy;
		{
			PR_FCNV = (fX);
			__asm
			{
				__asm fld PR_FCNV __asm fistp PR_ICNV
			};
			(ix) = PR_ICNV > PR_FCNV ? PR_ICNV - 1 : PR_ICNV;
		};
		if (fY < 0F)
		{
			fY = -fY;
		}
		{
			PR_FCNV = (fY);
			__asm
			{
				__asm fld PR_FCNV __asm fistp PR_ICNV
			};
			(iy) = PR_ICNV > PR_FCNV ? PR_ICNV - 1 : PR_ICNV;
		};
    
		short sCoordX = (short)MINMAX(0, ix / CTerrainImpl.TERRAIN_XSIZE, m_sTerrainCountX - 1);
		short sCoordY = (short)MINMAX(0, iy / CTerrainImpl.TERRAIN_YSIZE, m_sTerrainCountY - 1);
    
		bool bNeedInit = (m_PrevCoordinate.m_sTerrainCoordX == -1 || m_PrevCoordinate.m_sTerrainCoordY == -1);
    
		if (bNeedInit || (m_CurCoordinate.m_sTerrainCoordX / LOAD_SIZE_WIDTH) != (sCoordX / LOAD_SIZE_WIDTH) || (m_CurCoordinate.m_sTerrainCoordY / LOAD_SIZE_WIDTH) != (sCoordY / LOAD_SIZE_WIDTH))
		{
			if (bNeedInit)
			{
				m_PrevCoordinate.m_sTerrainCoordX = sCoordX;
				m_PrevCoordinate.m_sTerrainCoordY = sCoordY;
			}
			else
			{
				m_PrevCoordinate.m_sTerrainCoordX = m_CurCoordinate.m_sTerrainCoordX;
				m_PrevCoordinate.m_sTerrainCoordY = m_CurCoordinate.m_sTerrainCoordY;
			}
    
			m_CurCoordinate.m_sTerrainCoordX = sCoordX;
			m_CurCoordinate.m_sTerrainCoordY = sCoordY;
			m_lCurCoordStartX = sCoordX * CTerrainImpl.TERRAIN_XSIZE;
			m_lCurCoordStartY = sCoordY * CTerrainImpl.TERRAIN_YSIZE;
    
			ushort wCellCoordX = (ix % CTerrainImpl.TERRAIN_XSIZE) / CTerrainImpl.CELLSCALE;
			ushort wCellCoordY = (iy % CTerrainImpl.TERRAIN_YSIZE) / CTerrainImpl.CELLSCALE;
    
			short sReferenceCoordMinX;
			short sReferenceCoordMaxX;
			short sReferenceCoordMinY;
			short sReferenceCoordMaxY;
			sReferenceCoordMinX = Math.Max(m_CurCoordinate.m_sTerrainCoordX - LOAD_SIZE_WIDTH, 0);
			sReferenceCoordMaxX = Math.Min(m_CurCoordinate.m_sTerrainCoordX + LOAD_SIZE_WIDTH, m_sTerrainCountX - 1);
			sReferenceCoordMinY = Math.Max(m_CurCoordinate.m_sTerrainCoordY - LOAD_SIZE_WIDTH, 0);
			sReferenceCoordMaxY = Math.Min(m_CurCoordinate.m_sTerrainCoordY + LOAD_SIZE_WIDTH, m_sTerrainCountY - 1);
    
			for (ushort usY = (ushort)sReferenceCoordMinY; usY <= sReferenceCoordMaxY; ++usY)
			{
				for (ushort usX = (ushort)sReferenceCoordMinX; usX <= sReferenceCoordMaxX; ++usX)
				{
					LoadTerrain(usX, usY, wCellCoordX, wCellCoordY);
					  LoadArea(usX, usY, wCellCoordX, wCellCoordY);
				}
			}
    
			AssignTerrainPtr();
			m_lOldReadX = -1;
    
			Tracenf("Update::Load spent %d ms\n", ELTimer_GetMSec() - t1);
		}
		CSpeedTreeForestDirectX8.Instance().UpdateSystem(CTimer.Instance().GetCurrentSecond());
		__UpdateGarvage();
		UpdateTerrain(fX, fY);
		__UpdateArea(v3Player);
		UpdateSky();
		__HeightCache_Update();
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void UpdateSky()
	{
		m_SkyBox.Update();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void UpdateAroundAmbience(float fX, float fY, float fZ)
	{
		for (int LaniatusDefVariables = 0; LaniatusDefVariables < AROUND_AREA_NUM; ++i)
		{
			CArea pArea;
			if (GetAreaPointer(i, pArea))
			{
				pArea.UpdateAroundAmbience(fX, fY, fZ);
			}
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __UpdateArea(_D3DVECTOR v3Player)
	{
		__Game_UpdateArea(v3Player);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __Game_UpdateArea(_D3DVECTOR v3Player)
	{
		m_PCBlockerVector.clear();
		m_ShadowReceiverVector.clear();
		CCameraManager rCmrMgr = CCameraManager.Instance();
		CCamera pCamera = rCmrMgr.GetCurrentCamera();
		if (pCamera == null)
		{
			return;
		}
    
		float fDistance = pCamera.GetDistance();
    
		_D3DVECTOR v3View = pCamera.GetView();
		_D3DVECTOR v3Target = pCamera.GetTarget();
		_D3DVECTOR v3Eye = pCamera.GetEye();
    
		_D3DVECTOR v3Light = D3DXVECTOR3(1.732f, 1.0f, -3.464f);
		v3Light *= 50.0f / D3DXVec3Length(v3Light);
		__CollectShadowReceiver(v3Player, v3Light);
		__CollectCollisionPCBlocker(v3Eye, v3Player, fDistance);
		__CollectCollisionShadowReceiver(v3Player, v3Light);
		__UpdateAroundAreaList();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __UpdateAroundAreaList()
	{
		uint[] at = new uint[AROUND_AREA_NUM];
		for (int LaniatusDefVariables = 0; LaniatusDefVariables < AROUND_AREA_NUM; ++i)
		{
			uint t1 = timeGetTime();
			CArea pArea;
			if (GetAreaPointer(i, pArea))
			{
				pArea.Update();
			}
			uint t2 = timeGetTime();
    
			at[LaniatusDefVariables] = t2 - t1;
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __CollectShadowReceiver(_D3DVECTOR v3Target, _D3DVECTOR v3Light)
	{
		CDynamicSphereInstance s = new CDynamicSphereInstance();
		s.v3LastPosition = v3Target + v3Light;
		s.v3Position = s.v3LastPosition + v3Light;
		s.fRadius = 50.0f;
    
		Vector3d aVector3d = new Vector3d();
		aVector3d.Set(v3Target.x, v3Target.y, v3Target.z);
    
		CCullingManager rkCullingMgr = CCullingManager.Instance();
    
		FGetShadowReceiverFromHeightData kGetShadowReceiverFromHeightData = new FGetShadowReceiverFromHeightData(v3Target.x, v3Target.y, s.v3Position.x, s.v3Position.y);
		rkCullingMgr.ForInRange(aVector3d, 10.0f, kGetShadowReceiverFromHeightData);
    
		if (kGetShadowReceiverFromHeightData.m_bReceiverFound)
		{
			for (uint LaniatusDefVariables = 0; LaniatusDefVariables < kGetShadowReceiverFromHeightData.GetCollectCount(); ++i)
			{
				CGraphicObjectInstance pObjInstEach = kGetShadowReceiverFromHeightData.GetCollectItem(i);
				if (!__IsInShadowReceiverList(pObjInstEach))
				{
					m_ShadowReceiverVector.push_back(pObjInstEach);
				}
			}
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __CollectCollisionPCBlocker(_D3DVECTOR v3Eye, _D3DVECTOR v3Target, float fDistance)
	{
		Vector3d v3dRayStart = new Vector3d();
		v3dRayStart.Set(v3Eye.x, v3Eye.y, v3Eye.z);
    
		PCBlocker_CDynamicSphereInstanceVector aDynamicSphereInstanceVector = new PCBlocker_CDynamicSphereInstanceVector();
		{
	//# Laniatus Games Studio Inc. | TODO TASK: Pointer arithmetic is detected on this variable, so pointers on this variable are left unchanged:
			CDynamicSphereInstance * pkDSI = aDynamicSphereInstanceVector.Begin();
			pkDSI.fRadius = fDistance * 0.5f;
			pkDSI.v3LastPosition = v3Eye;
			pkDSI.v3Position = v3Eye + 0.5f * (v3Target - v3Eye);
			++pkDSI;
    
			pkDSI.fRadius = fDistance * 0.5f;
			pkDSI.v3LastPosition = v3Eye + 0.5f * (v3Target - v3Eye);
			pkDSI.v3Position = v3Target;
			++pkDSI;
    
			pkDSI.fRadius = fDistance * 0.5f;
			pkDSI.v3LastPosition = v3Target;
			pkDSI.v3Position = v3Eye + 0.5f * (v3Target - v3Eye);
			++pkDSI;
    
			pkDSI.fRadius = fDistance * 0.5f;
			pkDSI.v3LastPosition = v3Eye + 0.5f * (v3Target - v3Eye);
			pkDSI.v3Position = v3Eye;
			++pkDSI;
		}
		CCullingManager rkCullingMgr = CCullingManager.Instance();
    
		PCBlocker_SInstanceList kPCBlockerList = new PCBlocker_SInstanceList(aDynamicSphereInstanceVector);
		RangeTester<PCBlocker_SInstanceList> kPCBlockerRangeTester = new RangeTester<PCBlocker_SInstanceList>(kPCBlockerList);
		rkCullingMgr.RangeTest(v3dRayStart, fDistance, kPCBlockerRangeTester);
    
		if (!kPCBlockerList.IsEmpty())
		{
	//# Laniatus Games Studio Inc. | TODO TASK: The typedef 'Iterator' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
			PCBlocker_SInstanceList.Iterator LaniatusDefVariables = new PCBlocker_SInstanceList.Iterator();
    
			for (i = kPCBlockerList.Begin(); LaniatusDefVariables != kPCBlockerList.End(); ++i)
			{
				CGraphicObjectInstance pObjInstEach = *i;
    
				if (pObjInstEach == null)
				{
					continue;
				}
    
				if (TREE_OBJECT == pObjInstEach.GetType() && !m_bTransparentTree)
				{
					continue;
				}
    
				if (!__IsInShadowReceiverList(pObjInstEach))
				{
					if (!__IsInPCBlockerList(pObjInstEach))
					{
						m_PCBlockerVector.push_back(pObjInstEach);
					}
				}
			}
		}
		std::sort(m_PCBlockerVector.begin(), m_PCBlockerVector.end(), FPCBlockerDistanceSort(v3Eye));
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __CollectCollisionShadowReceiver(_D3DVECTOR v3Target, _D3DVECTOR v3Light)
	{
		CDynamicSphereInstance s = new CDynamicSphereInstance();
		s.fRadius = 50.0f;
		s.v3LastPosition = v3Target + v3Light;
		s.v3Position = s.v3LastPosition + v3Light;
    
		Vector3d aVector3d = new Vector3d();
		aVector3d.Set(v3Target.x, v3Target.y, v3Target.z);
    
		CCullingManager rkCullingMgr = CCullingManager.Instance();
    
		List<CGraphicObjectInstance > kVct_pkShadowReceiver = new List<CGraphicObjectInstance >();
		FGetShadowReceiverFromCollisionData kGetShadowReceiverFromCollisionData = new FGetShadowReceiverFromCollisionData(s, kVct_pkShadowReceiver);
		rkCullingMgr.ForInRange(aVector3d, 100.0f, kGetShadowReceiverFromCollisionData);
		if (!kGetShadowReceiverFromCollisionData.m_bCollide)
		{
			return;
		}
    
		List<CGraphicObjectInstance  >.Enumerator i;
		for (i = kVct_pkShadowReceiver.GetEnumerator(); i.MoveNext();)
		{
			CGraphicObjectInstance pObjInstEach = i.Current;
			if (!__IsInPCBlockerList(pObjInstEach))
			{
				if (!__IsInShadowReceiverList(pObjInstEach))
				{
					m_ShadowReceiverVector.push_back(pObjInstEach);
				}
			}
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool __IsInShadowReceiverList(CGraphicObjectInstance pkObjInstTest)
	{
		if (m_ShadowReceiverVector.end() == std::find(m_ShadowReceiverVector.begin(), m_ShadowReceiverVector.end(), pkObjInstTest))
		{
			return false;
		}
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool __IsInPCBlockerList(CGraphicObjectInstance pkObjInstTest)
	{
		if (m_PCBlockerVector.end() == std::find(m_PCBlockerVector.begin(), m_PCBlockerVector.end(), pkObjInstTest))
		{
			return false;
		}
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void UpdateTerrain(float fX, float fY)
	{
		if (fY < 0F)
		{
			fY = -fY;
		}
    
		int sx;
		int sy;
		{
			PR_FCNV = (fX);
			__asm
			{
				__asm fld PR_FCNV __asm fistp PR_ICNV
			};
			(sx) = PR_ICNV > PR_FCNV ? PR_ICNV - 1 : PR_ICNV;
		};
		{
			PR_FCNV = (fY);
			__asm
			{
				__asm fld PR_FCNV __asm fistp PR_ICNV
			};
			(sy) = PR_ICNV > PR_FCNV ? PR_ICNV - 1 : PR_ICNV;
		};
    
		int lDivider = (CTerrainImpl.CELLSCALE * DefineConstants.TERRAIN_PATCHSIZE);
    
		m_lCenterX = (sx - m_lCurCoordStartX) / lDivider;
		m_lCenterY = (sy - m_lCurCoordStartY) / lDivider;
    
		if ((m_lCenterX != m_lOldReadX) || (m_lCenterY != m_lOldReadY))
		{
			int lRealCenterX = m_lCenterX * DefineConstants.TERRAIN_PATCHSIZE;
			int lRealCenterY = m_lCenterY * DefineConstants.TERRAIN_PATCHSIZE;
			m_lOldReadX = m_lCenterX;
			m_lOldReadY = m_lCenterY;
    
			ConvertTerrainToTnL(lRealCenterX, lRealCenterY);
			UpdateAreaList(lRealCenterX, lRealCenterY);
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __ClearGarvage()
	{
		std::for_each(m_TerrainDeleteVector.begin(), m_TerrainDeleteVector.end(), CTerrain.Delete);
		m_TerrainDeleteVector.clear();
    
		std::for_each(m_AreaDeleteVector.begin(), m_AreaDeleteVector.end(), CArea.Delete);
		m_AreaDeleteVector.clear();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __UpdateGarvage()
	{
		const uint dwTerrainEraseInterval = (uint)(1000 * 60);
	//# Laniatus Games Studio Inc. |: This static local variable declaration (not allowed in C#) has been moved just prior to the method:
	//	static uint dwEraseTime = ELTimer_GetMSec();
    
		if (!m_TerrainDeleteVector.empty())
		{
			if (ELTimer_GetMSec() - __UpdateGarvage_dwEraseTime <= dwTerrainEraseInterval)
			{
				return;
			}
			TTerrainPtrVectorIterator aTerrainPtrDeleteItertor = m_TerrainDeleteVector.begin();
			CTerrain pTerrain = *aTerrainPtrDeleteItertor;
			CTerrain.Delete(pTerrain);
    
			aTerrainPtrDeleteItertor = m_TerrainDeleteVector.erase(aTerrainPtrDeleteItertor);
			__UpdateGarvage_dwEraseTime = ELTimer_GetMSec();
			Trace("Delete Terrain \n");
			return;
		}
    
		if (!m_AreaDeleteVector.empty())
		{
			if (ELTimer_GetMSec() - __UpdateGarvage_dwEraseTime <= dwTerrainEraseInterval)
			{
				return;
			}
			TAreaPtrVectorIterator aAreaPtrDeleteItertor = m_AreaDeleteVector.begin();
    
			CArea pArea = *aAreaPtrDeleteItertor;
			CArea.Delete(pArea);
    
			aAreaPtrDeleteItertor = m_AreaDeleteVector.erase(aAreaPtrDeleteItertor);
			__UpdateGarvage_dwEraseTime = ELTimer_GetMSec();
			Trace("Delete Area \n");
			return;
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void UpdateAreaList(int lCenterX, int lCenterY)
	{
		if (m_TerrainVector.size() <= AROUND_AREA_NUM && m_AreaVector.size() <= AROUND_AREA_NUM)
		{
			return;
		}
    
		__ClearGarvage();
    
		FPushToDeleteVector.EDeleteDir eDeleteLRDir = new FPushToDeleteVector.EDeleteDir();
		FPushToDeleteVector.EDeleteDir eDeleteTBDir = new FPushToDeleteVector.EDeleteDir();
    
		if (lCenterX > CTerrainImpl.XSIZE / 2)
		{
			eDeleteLRDir = FPushToDeleteVector.DELETE_LEFT;
		}
		else
		{
			eDeleteLRDir = FPushToDeleteVector.DELETE_RIGHT;
		}
		if (lCenterY > CTerrainImpl.YSIZE / 2)
		{
			eDeleteTBDir = FPushToDeleteVector.DELETE_TOP;
		}
		else
		{
			eDeleteTBDir = FPushToDeleteVector.DELETE_BOTTOM;
		}
    
		FPushTerrainToDeleteVector rPushTerrainToDeleteVector = std::for_each(m_TerrainVector.begin(), m_TerrainVector.end(), FPushTerrainToDeleteVector(eDeleteLRDir, eDeleteTBDir, m_CurCoordinate));
		FPushAreaToDeleteVector rPushAreaToDeleteVector = std::for_each(m_AreaVector.begin(), m_AreaVector.end(), FPushAreaToDeleteVector(eDeleteLRDir, eDeleteTBDir, m_CurCoordinate));
    
		if (!rPushTerrainToDeleteVector.m_ReturnTerrainVector.empty())
		{
			m_TerrainDeleteVector.resize(rPushTerrainToDeleteVector.m_ReturnTerrainVector.size());
			std::copy(rPushTerrainToDeleteVector.m_ReturnTerrainVector.begin(), rPushTerrainToDeleteVector.m_ReturnTerrainVector.end(), m_TerrainDeleteVector.begin());
    
			for (uint dwIndex = 0; dwIndex < rPushTerrainToDeleteVector.m_ReturnTerrainVector.size(); ++dwIndex)
			{
				bool isDel = false;
				TTerrainPtrVectorIterator aTerrainPtrItertor = m_TerrainVector.begin();
				while (aTerrainPtrItertor != m_TerrainVector.end())
				{
					CTerrain pTerrain = *aTerrainPtrItertor;
					if (pTerrain == rPushTerrainToDeleteVector.m_ReturnTerrainVector[dwIndex])
					{
						aTerrainPtrItertor = m_TerrainVector.erase(aTerrainPtrItertor);
						isDel = true;
					}
					else
					{
						++aTerrainPtrItertor;
					}
				}
			}
		}
		if (!rPushAreaToDeleteVector.m_ReturnAreaVector.empty())
		{
			m_AreaDeleteVector.resize(rPushAreaToDeleteVector.m_ReturnAreaVector.size());
			std::copy(rPushAreaToDeleteVector.m_ReturnAreaVector.begin(), rPushAreaToDeleteVector.m_ReturnAreaVector.end(), m_AreaDeleteVector.begin());
    
			for (uint dwIndex = 0; dwIndex < rPushAreaToDeleteVector.m_ReturnAreaVector.size(); ++dwIndex)
			{
				TAreaPtrVectorIterator aAreaPtrItertor = m_AreaVector.begin();
				while (aAreaPtrItertor != m_AreaVector.end())
				{
					CArea pArea = *aAreaPtrItertor;
					if (pArea == rPushAreaToDeleteVector.m_ReturnAreaVector[dwIndex])
					{
						aAreaPtrItertor = m_AreaVector.erase(aAreaPtrItertor);
					}
					else
					{
						++aAreaPtrItertor;
					}
				}
			}
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void ConvertTerrainToTnL(int lx, int ly)
	{
		Debug.Assert(null != m_pTerrainPatchProxyList && "CMapOutdoor::ConvertTerrainToTnL");
    
		for (int LaniatusDefVariables = 0; LaniatusDefVariables < m_wPatchCount * m_wPatchCount; LaniatusDefVariables++)
		{
			m_pTerrainPatchProxyList[LaniatusDefVariables].SetUsed(false);
		}
    
		lx -= m_lViewRadius;
		ly -= m_lViewRadius;
    
		int diameter = m_lViewRadius * 2;
    
		int x0 = lx / DefineConstants.TERRAIN_PATCHSIZE;
		int y0 = ly / DefineConstants.TERRAIN_PATCHSIZE;
		int x1 = (lx + diameter - 1) / DefineConstants.TERRAIN_PATCHSIZE;
		int y1 = (ly + diameter - 1) / DefineConstants.TERRAIN_PATCHSIZE;
    
		int xw = x1 - x0 + 1;
		int yw = y1 - y0 + 1;
    
		int ex = lx + diameter;
		int ey = ly + diameter;
    
		y0 = ly;
		for (int yp = 0; yp < yw; yp++)
		{
			x0 = lx;
			y1 = (y0 / DefineConstants.TERRAIN_PATCHSIZE + 1) * DefineConstants.TERRAIN_PATCHSIZE;
			if (y1 > ey)
			{
				y1 = ey;
			}
			for (int xp = 0; xp < xw; xp++)
			{
				x1 = (x0 / DefineConstants.TERRAIN_PATCHSIZE + 1) * DefineConstants.TERRAIN_PATCHSIZE;
				if (x1 > ex)
				{
					x1 = ex;
				}
				 AssignPatch(yp * m_wPatchCount + xp, x0, y0, x1, y1);
				x0 = x1;
			}
			y0 = y1;
		}
		UpdateQuadTreeHeights(m_pRootNode);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void AssignPatch(int lPatchNum, int x0, int y0, int x1, int y1)
	{
		Debug.Assert(null != m_pTerrainPatchProxyList && "CMapOutdoor::AssignPatch");
    
		CTerrainPatchProxy pTerrainPatchProxy = m_pTerrainPatchProxyList[lPatchNum];
    
		if (y0 < 0 && y1 <= 0)
		{
			if (x0 < 0 && x1 <= 0)
			{
				pTerrainPatchProxy.SetTerrainNum(0);
				x0 += CTerrainImpl.XSIZE;
				x1 += CTerrainImpl.XSIZE;
			}
			else if (x0 >= CTerrainImpl.XSIZE && x1 > CTerrainImpl.XSIZE)
			{
				pTerrainPatchProxy.SetTerrainNum(2);
				x0 -= CTerrainImpl.XSIZE;
				x1 -= CTerrainImpl.XSIZE;
			}
			else
			{
				pTerrainPatchProxy.SetTerrainNum(1);
			}
    
			y0 += CTerrainImpl.YSIZE;
			y1 += CTerrainImpl.YSIZE;
		}
		else if (y0 >= CTerrainImpl.YSIZE && y1 > CTerrainImpl.YSIZE)
		{
			if (x0 < 0 && x1 <= 0)
			{
				pTerrainPatchProxy.SetTerrainNum(6);
				x0 += CTerrainImpl.XSIZE;
				x1 += CTerrainImpl.XSIZE;
			}
			else if (x0 >= CTerrainImpl.XSIZE && x1 > CTerrainImpl.XSIZE)
			{
				pTerrainPatchProxy.SetTerrainNum(8);
				x0 -= CTerrainImpl.XSIZE;
				x1 -= CTerrainImpl.XSIZE;
			}
			else
			{
				pTerrainPatchProxy.SetTerrainNum(7);
			}
    
			y0 -= CTerrainImpl.YSIZE;
			y1 -= CTerrainImpl.YSIZE;
		}
		else
		{
			if (x0 < 0 && x1 <= 0)
			{
				pTerrainPatchProxy.SetTerrainNum(3);
				x0 += CTerrainImpl.XSIZE;
				x1 += CTerrainImpl.XSIZE;
			}
			else if (x0 >= CTerrainImpl.XSIZE && x1 > CTerrainImpl.XSIZE)
			{
				pTerrainPatchProxy.SetTerrainNum(5);
				x0 -= CTerrainImpl.XSIZE;
				x1 -= CTerrainImpl.XSIZE;
			}
			else
			{
				pTerrainPatchProxy.SetTerrainNum(4);
			}
		}
    
		CTerrain pTerrain;
		if (!GetTerrainPointer(pTerrainPatchProxy.GetTerrainNum(), pTerrain))
		{
			return;
		}
    
		byte byPatchNumX;
		byte byPatchNumY;
		byPatchNumX = x0 / CTerrainImpl.PATCH_XSIZE;
		byPatchNumY = y0 / CTerrainImpl.PATCH_YSIZE;
    
		CTerrainPatch pTerrainPatch = pTerrain.GetTerrainPatchPtr(byPatchNumX, byPatchNumY);
		if (pTerrainPatch == null)
		{
			return;
		}
    
		pTerrainPatchProxy.SetPatchNum(byPatchNumY * CTerrainImpl.PATCH_XCOUNT + byPatchNumX);
		pTerrainPatchProxy.SetTerrainPatch(pTerrainPatch);
		pTerrainPatchProxy.SetUsed(true);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void UpdateQuadTreeHeights(CTerrainQuadtreeNode Node)
	{
		Debug.Assert(null != m_pTerrainPatchProxyList && "CMapOutdoor::UpdateQuadTreeHeights");
		if (!m_pTerrainPatchProxyList)
		{
			return;
		}
    
		float minx;
		float maxx;
		float miny;
		float maxy;
		float minz;
		float maxz;
		minx = maxx = miny = maxy = minz = maxz = 0F;
    
		if (m_pTerrainPatchProxyList[Node.PatchNum].isUsed())
		{
			minx = m_pTerrainPatchProxyList[Node.PatchNum].GetMinX();
			maxx = m_pTerrainPatchProxyList[Node.PatchNum].GetMaxX();
			miny = m_pTerrainPatchProxyList[Node.PatchNum].GetMinY();
			maxy = m_pTerrainPatchProxyList[Node.PatchNum].GetMaxY();
			minz = m_pTerrainPatchProxyList[Node.PatchNum].GetMinZ();
			maxz = m_pTerrainPatchProxyList[Node.PatchNum].GetMaxZ();
		}
    
		for (int y = Node.y0; y <= Node.y1; y++)
		{
			for (int x = Node.x0; x <= Node.x1; x++)
			{
				int patch = y * m_wPatchCount + x;
    
				if (!m_pTerrainPatchProxyList[patch].isUsed())
				{
					continue;
				}
    
				if (m_pTerrainPatchProxyList[patch].GetMinX() < minx)
				{
					minx = m_pTerrainPatchProxyList[patch].GetMinX();
				}
				if (m_pTerrainPatchProxyList[patch].GetMaxX() > maxx)
				{
					maxx = m_pTerrainPatchProxyList[patch].GetMaxX();
				}
    
				if (m_pTerrainPatchProxyList[patch].GetMinY() < miny)
				{
					miny = m_pTerrainPatchProxyList[patch].GetMinY();
				}
				if (m_pTerrainPatchProxyList[patch].GetMaxY() > maxy)
				{
					maxy = m_pTerrainPatchProxyList[patch].GetMaxY();
				}
    
				if (m_pTerrainPatchProxyList[patch].GetMinZ() < minz)
				{
					minz = m_pTerrainPatchProxyList[patch].GetMinZ();
				}
				if (m_pTerrainPatchProxyList[patch].GetMaxZ() > maxz)
				{
					maxz = m_pTerrainPatchProxyList[patch].GetMaxZ();
				}
			}
		}
    
		Node.center.x = (maxx + minx) * 0.5f;
		Node.center.y = (maxy + miny) * 0.5f;
		Node.center.z = (maxz + minz) * 0.5f;
    
		Node.radius = sqrtf((maxx - minx) * (maxx - minx) + (maxy - miny) * (maxy - miny) + (maxz - minz) * (maxz - minz)) / 2.0f;
    
		if (Node.NW_Node != null)
		{
			UpdateQuadTreeHeights(Node.NW_Node);
		}
    
		if (Node.NE_Node != null)
		{
			UpdateQuadTreeHeights(Node.NE_Node);
		}
    
		if (Node.SW_Node != null)
		{
			UpdateQuadTreeHeights(Node.SW_Node);
		}
    
		if (Node.SE_Node != null)
		{
			UpdateQuadTreeHeights(Node.SE_Node);
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void LoadWaterTexture()
	{
		UnloadWaterTexture();
		string buf = new string(new char[256]);
		for (int LaniatusDefVariables = 0; LaniatusDefVariables < 30; ++i)
		{
			sprintf(buf, "d:/ymir Work/special/water/%02d.dds", LaniatusDefVariables + 1);
			m_WaterInstances[LaniatusDefVariables].SetImagePointer((CGraphicImage) CResourceManager.Instance().GetResourcePointer(buf));
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void UnloadWaterTexture()
	{
		for (int LaniatusDefVariables = 0; LaniatusDefVariables < 30; ++i)
		{
			m_WaterInstances[LaniatusDefVariables].Destroy();
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void RenderWater()
	{
		if (m_PatchVector.empty())
		{
			return;
		}
    
		if (!IsVisiblePart(PART_WATER))
		{
			return;
		}
    
		_D3DMATRIX matTexTransformWater = new _D3DMATRIX();
    
		(CStateManager.Instance()).SaveRenderState(D3DRS_ZWRITEENABLE, false);
		(CStateManager.Instance()).SaveRenderState(D3DRS_ALPHABLENDENABLE, true);
		(CStateManager.Instance()).SaveRenderState(D3DRS_CULLMODE, D3DCULL_NONE);
		(CStateManager.Instance()).SaveRenderState(D3DRS_DIFFUSEMATERIALSOURCE, D3DMCS_COLOR1);
		(CStateManager.Instance()).SaveRenderState(D3DRS_COLORVERTEX, true);
    
		(CStateManager.Instance()).SetTexture(0, m_WaterInstances[((ELTimer_GetMSec() / 70) % 30)].GetTexturePointer().GetD3DTexture());
    
		D3DXMatrixScaling(matTexTransformWater, m_fWaterTexCoordBase, -m_fWaterTexCoordBase, 0.0f);
		D3DXMatrixMultiply(matTexTransformWater, m_matViewInverse, matTexTransformWater);
    
		(CStateManager.Instance()).SaveTransform(D3DTS_TEXTURE0, matTexTransformWater);
		(CStateManager.Instance()).SaveVertexShader(DefineConstants.D3DFVF_XYZ | DefineConstants.D3DFVF_DIFFUSE);
    
		(CStateManager.Instance()).SaveTextureStageState(0, D3DTSS_TEXCOORDINDEX, DefineConstants.D3DTSS_TCI_CAMERASPACEPOSITION);
		(CStateManager.Instance()).SaveTextureStageState(0, D3DTSS_TEXTURETRANSFORMFLAGS, D3DTTFF_COUNT2);
		(CStateManager.Instance()).SaveTextureStageState(0, D3DTSS_MINFILTER, D3DTEXF_LINEAR);
		(CStateManager.Instance()).SaveTextureStageState(0, D3DTSS_MAGFILTER, D3DTEXF_LINEAR);
		(CStateManager.Instance()).SaveTextureStageState(0, D3DTSS_MIPFILTER, D3DTEXF_LINEAR);
		(CStateManager.Instance()).SaveTextureStageState(0, D3DTSS_ADDRESSU, D3DTADDRESS_WRAP);
		(CStateManager.Instance()).SaveTextureStageState(0, D3DTSS_ADDRESSV, D3DTADDRESS_WRAP);
    
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLORARG1, DefineConstants.D3DTA_TEXTURE);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLOROP, D3DTOP_SELECTARG1);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_ALPHAARG1, DefineConstants.D3DTA_DIFFUSE);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_ALPHAOP, D3DTOP_SELECTARG1);
    
    
		(CStateManager.Instance()).SetTexture(1,null);
		(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_COLOROP, D3DTOP_DISABLE);
		(CStateManager.Instance()).SetTextureStageState(1, D3DTSS_ALPHAOP, D3DTOP_DISABLE);
    
	//# Laniatus Games Studio Inc. |: This static local variable declaration (not allowed in C#) has been moved just prior to the method:
	//	static float s_fWaterHeightCurrent = 0;
	//# Laniatus Games Studio Inc. |: This static local variable declaration (not allowed in C#) has been moved just prior to the method:
	//	static float s_fWaterHeightBegin = 0;
	//# Laniatus Games Studio Inc. |: This static local variable declaration (not allowed in C#) has been moved just prior to the method:
	//	static float s_fWaterHeightEnd = 0;
	//# Laniatus Games Studio Inc. |: This static local variable declaration (not allowed in C#) has been moved just prior to the method:
	//	static uint s_dwLastHeightChangeTime = CTimer::Instance().GetCurrentMillisecond();
	//# Laniatus Games Studio Inc. |: This static local variable declaration (not allowed in C#) has been moved just prior to the method:
	//	static uint s_dwBlendtime = 300;
    
		if ((CTimer.Instance().GetCurrentMillisecond() - RenderWater_s_dwLastHeightChangeTime) > RenderWater_s_dwBlendtime)
		{
			RenderWater_s_dwBlendtime = random_range(1000, 3000);
    
			if (RenderWater_s_fWaterHeightEnd == 0)
			{
				RenderWater_s_fWaterHeightEnd = -random_range(0, 15);
			}
			else
			{
				RenderWater_s_fWaterHeightEnd = 0;
			}
    
			RenderWater_s_fWaterHeightBegin = RenderWater_s_fWaterHeightCurrent;
			RenderWater_s_dwLastHeightChangeTime = CTimer.Instance().GetCurrentMillisecond();
		}
    
		RenderWater_s_fWaterHeightCurrent = RenderWater_s_fWaterHeightBegin + (RenderWater_s_fWaterHeightEnd - RenderWater_s_fWaterHeightBegin) * (float)((CTimer.Instance().GetCurrentMillisecond() - RenderWater_s_dwLastHeightChangeTime) / (float) RenderWater_s_dwBlendtime);
		m_matWorldForCommonUse._43 = RenderWater_s_fWaterHeightCurrent;
    
		m_matWorldForCommonUse._41 = 0.0f;
		m_matWorldForCommonUse._42 = 0.0f;
		(CStateManager.Instance()).SetTransform((D3DTRANSFORMSTATETYPE)(0 + 256), m_matWorldForCommonUse);
    
		float fFogDistance = __GetFogDistance();
    
		List<Tuple<float, int>>.Enumerator i;
    
		for (i = m_PatchVector.begin(); i.MoveNext();)
		{
			if (i.first < fFogDistance)
			{
				DrawWater(i.second);
			}
		}
    
		(CStateManager.Instance()).SetTexture(0, null);
		(CStateManager.Instance()).SetRenderState(D3DRS_ALPHABLENDENABLE, false);
    
		for (i = m_PatchVector.begin(); i.MoveNext();)
		{
			if (i.first >= fFogDistance)
			{
				DrawWater(i.second);
			}
		}
    
		m_matWorldForCommonUse._43 = 0.0f;
    
		(CStateManager.Instance()).RestoreVertexShader();
		(CStateManager.Instance()).RestoreTransform(D3DTS_TEXTURE0);
		(CStateManager.Instance()).RestoreTextureStageState(0, D3DTSS_MINFILTER);
		(CStateManager.Instance()).RestoreTextureStageState(0, D3DTSS_MAGFILTER);
		(CStateManager.Instance()).RestoreTextureStageState(0, D3DTSS_MIPFILTER);
		(CStateManager.Instance()).RestoreTextureStageState(0, D3DTSS_ADDRESSU);
		(CStateManager.Instance()).RestoreTextureStageState(0, D3DTSS_ADDRESSV);
		(CStateManager.Instance()).RestoreTextureStageState(0, D3DTSS_TEXCOORDINDEX);
		(CStateManager.Instance()).RestoreTextureStageState(0, D3DTSS_TEXTURETRANSFORMFLAGS);
    
		(CStateManager.Instance()).RestoreRenderState(D3DRS_DIFFUSEMATERIALSOURCE);
		(CStateManager.Instance()).RestoreRenderState(D3DRS_COLORVERTEX);
		(CStateManager.Instance()).RestoreRenderState(D3DRS_ZWRITEENABLE);
		(CStateManager.Instance()).RestoreRenderState(D3DRS_ALPHABLENDENABLE);
		(CStateManager.Instance()).RestoreRenderState(D3DRS_CULLMODE);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void DrawWater(int patchnum)
	{
		Debug.Assert(null != m_pTerrainPatchProxyList);
		if (!m_pTerrainPatchProxyList)
		{
			return;
		}
    
		CTerrainPatchProxy rkTerrainPatchProxy = m_pTerrainPatchProxyList[patchnum];
    
		if (!rkTerrainPatchProxy.isUsed())
		{
			return;
		}
    
		if (!rkTerrainPatchProxy.isWaterExists())
		{
			return;
		}
    
		CGraphicVertexBuffer pkVB = rkTerrainPatchProxy.GetWaterVertexBufferPointer();
		if (pkVB == null)
		{
			return;
		}
    
		if (!pkVB.GetD3DVertexBuffer())
		{
			return;
		}
    
		uint uPriCount = rkTerrainPatchProxy.GetWaterFaceCount();
		if (uPriCount == 0)
		{
			return;
		}
    
		(CStateManager.Instance()).SetStreamSource(0, pkVB.GetD3DVertexBuffer(), sizeof(SWaterVertex));
		(CStateManager.Instance()).DrawPrimitive(D3DPT_TRIANGLELIST, 0, uPriCount);
    
		ms_faceCount += uPriCount;
	}
}