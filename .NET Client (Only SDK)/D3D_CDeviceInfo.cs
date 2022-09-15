public class D3D_CDeviceInfo
{
//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool Build(IDirect3D8 rkD3D, uint iD3DAdapterInfo, uint iDevType, D3D_CAdapterDisplayModeList rkD3DADMList, pfnConfirmDeviceDelegate pfnConfirmDevice)
	{
		Debug.Assert(pfnConfirmDevice != null && "D3D_CDeviceInfo::Build");
    
		D3DDEVTYPE c_eD3DDevType = msc_aeD3DDevType[iDevType];
		string c_szD3DDevDesc = msc_aszD3DDevDesc[iDevType];
    
		m_eD3DDevType = c_eD3DDevType;
		rkD3D.GetDeviceCaps(iD3DAdapterInfo, c_eD3DDevType, m_kD3DCaps);
    
		m_szDevDesc = c_szD3DDevDesc;
		m_uD3DModeInfoNum = 0;
		m_canDoWindowed = false;
		m_isWindowed = false;
		m_eD3DMSTFullscreen = D3DMULTISAMPLE_NONE;
		m_eD3DMSTWindowed = D3DMULTISAMPLE_NONE;
    
		bool[] aisFormatConfirmed = new bool[20];
		uint[] adwD3DBehavior = new uint[20];
		D3DFORMAT[] aeD3DFmtDepthStencil = Arrays.InitializeWithDefaultInstances<D3DFORMAT>(20);
    
		bool isHALExists = false;
		bool isHALWindowedCompatible = false;
		bool isHALDesktopCompatible = false;
		bool isHALSampleCompatible = false;
    
		{
			uint uD3DFmtNum = rkD3DADMList.GetPixelFormatNum();
    
			for (uint iFmt = 0; iFmt < uD3DFmtNum; ++iFmt)
			{
				D3DFORMAT eD3DFmtPixel = rkD3DADMList.GetPixelFormatr(iFmt);
				uint dwD3DBehavior = 0;
				bool isFormatConfirmed = false;
    
				aeD3DFmtDepthStencil[iFmt] = D3DFMT_UNKNOWN;
    
				if (FAILED(rkD3D.CheckDeviceType(iD3DAdapterInfo, m_eD3DDevType, eD3DFmtPixel, eD3DFmtPixel, false)))
				{
					continue;
				}
    
				if (D3DDEVTYPE_HAL == m_eD3DDevType)
				{
					isHALExists = true;
    
					if ((m_kD3DCaps.Caps2 & D3DCAPS2_CANRENDERWINDOWED) != 0)
					{
						isHALWindowedCompatible = true;
    
						if (iFmt == 0)
						{
							isHALDesktopCompatible = true;
						}
    
					}
				}
    
				if ((m_kD3DCaps.DevCaps & D3DDEVCAPS_HWTRANSFORMANDLIGHT) != 0)
				{
					if ((m_kD3DCaps.DevCaps & D3DDEVCAPS_PUREDEVICE) != 0)
					{
						dwD3DBehavior = (uint)(D3DCREATE_HARDWARE_VERTEXPROCESSING | D3DCREATE_PUREDEVICE);
    
						if (pfnConfirmDevice(m_kD3DCaps, dwD3DBehavior, eD3DFmtPixel))
						{
							isFormatConfirmed = true;
						}
					}
    
					if (false == isFormatConfirmed)
					{
						dwD3DBehavior = D3DCREATE_HARDWARE_VERTEXPROCESSING;
    
						if (pfnConfirmDevice(m_kD3DCaps, dwD3DBehavior, eD3DFmtPixel))
						{
							isFormatConfirmed = true;
						}
					}
    
					if (false == isFormatConfirmed)
					{
						dwD3DBehavior = D3DCREATE_MIXED_VERTEXPROCESSING;
    
						if (pfnConfirmDevice(m_kD3DCaps, dwD3DBehavior, eD3DFmtPixel))
						{
							isFormatConfirmed = true;
						}
					}
				}
    
				if (false == isFormatConfirmed)
				{
					dwD3DBehavior = D3DCREATE_SOFTWARE_VERTEXPROCESSING;
    
					if (pfnConfirmDevice(m_kD3DCaps, dwD3DBehavior, eD3DFmtPixel))
					{
						isFormatConfirmed = true;
					}
				}
    
				if (isFormatConfirmed)
				{
					if (!FindDepthStencilFormat(rkD3D, iD3DAdapterInfo, c_eD3DDevType, eD3DFmtPixel, aeD3DFmtDepthStencil[iFmt]))
					{
						isFormatConfirmed = true;
					}
    
				}
    
				adwD3DBehavior[iFmt] = dwD3DBehavior;
				aisFormatConfirmed[iFmt] = isFormatConfirmed;
			}
		}
    
		{
			uint uD3DDMNum = rkD3DADMList.GetDisplayModeNum();
			uint uD3DFmtNum = rkD3DADMList.GetPixelFormatNum();
    
    
			for (uint iD3DDM = 0; iD3DDM < uD3DDMNum; ++iD3DDM)
			{
				D3DDISPLAYMODE c_rkD3DDM = rkD3DADMList.GetDisplayModer(iD3DDM);
				for (uint iFmt = 0; iFmt < uD3DFmtNum; ++iFmt)
				{
					if (rkD3DADMList.GetPixelFormatr(iFmt) == c_rkD3DDM.Format)
					{
						if (aisFormatConfirmed[iFmt] == true)
						{
							D3D_SModeInfo rkModeInfo = m_akD3DModeInfo[m_uD3DModeInfoNum++];
							rkModeInfo.m_uScrWidth = c_rkD3DDM.Width;
							rkModeInfo.m_uScrHeight = c_rkD3DDM.Height;
							rkModeInfo.m_eD3DFmtPixel = c_rkD3DDM.Format;
							rkModeInfo.m_dwD3DBehavior = adwD3DBehavior[iFmt];
							rkModeInfo.m_eD3DFmtDepthStencil = aeD3DFmtDepthStencil[iFmt];
    
							if (m_eD3DDevType == D3DDEVTYPE_HAL)
							{
								isHALSampleCompatible = true;
							}
						}
					}
				}
			}
		}
    
		if (aisFormatConfirmed[0] && (m_kD3DCaps.Caps2 & D3DCAPS2_CANRENDERWINDOWED) != 0)
		{
			m_canDoWindowed = true;
			m_isWindowed = true;
		}
    
		if (m_uD3DModeInfoNum > 0)
		{
			return true;
		}
    
		return false;
	}
}