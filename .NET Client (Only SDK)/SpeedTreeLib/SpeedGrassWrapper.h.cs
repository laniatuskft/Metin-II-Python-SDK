#if USE_SPEEDGRASS
//# Laniatus Games Studio Inc. |: C# has no need of forward class declarations:
//class CMapOutdoor;

public class CSpeedGrassWrapper : CSpeedGrassRT, System.IDisposable
{
	public CSpeedGrassWrapper()
	{
		this.m_pMapOutdoor = null;
		this.m_lpD3DTexure8 = null;
	}
	public void Dispose()
	{
	}

		public void SetMapOutdoor(CMapOutdoor pMapOutdoor)
		{
			m_pMapOutdoor = pMapOutdoor;
		}
	public int Draw(float fDensity)
	{
		int nTriangleCount = 0;
		return nTriangleCount;
	}
	public bool InitFromBsfFile(string pFilename, uint nNumBlades, uint uiRows, uint uiCols, float fCollisionDistance)
	{
		bool bSuccess = false;
    
		if (pFilename != '\0')
		{
			if (ParseBsfFile(pFilename, nNumBlades, uiRows, uiCols, fCollisionDistance))
			{
				bSuccess = true;
			}
		}
		InitGraphics();
    
		return bSuccess;
	}

//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: virtual float Color(float fX, float fY, const float* pNormal, float* pTopColor, float* pBottomColor) const;
	public float Color(float fX, float fY, float pNormal, float[] pTopColor, float[] pBottomColor)
	{
		const float c_fColorAdjust = 0.3f;
		const float c_fColorThrow = 1.0f;
		const float c_fColorRandomness = 0.01f;
		const float c_TopLight = 0.75f;
    
		float[] afLowColor = {0.0f, 0F, 0F, 0F};
		float[] afHighColor = {0.0f, 0F, 0F, 0F};
		if (m_pMapOutdoor.GetBrushColor(fX, fY, afLowColor, afHighColor))
		{
			pBottomColor[0] = afLowColor[2];
			pBottomColor[1] = afLowColor[1];
			pBottomColor[2] = afLowColor[0];
    
			float fColorThrow = GetRandom(0.0f, c_fColorThrow);
			pTopColor[0] = VecInterpolate(pBottomColor[0], afHighColor[2], fColorThrow) + GetRandom(-c_fColorRandomness, c_fColorRandomness);
			pTopColor[1] = VecInterpolate(pBottomColor[1], afHighColor[1], fColorThrow) + GetRandom(-c_fColorRandomness, c_fColorRandomness);
			pTopColor[2] = VecInterpolate(pBottomColor[2], afHighColor[0], fColorThrow) + GetRandom(-c_fColorRandomness, c_fColorRandomness);
    
			float fLargest = pTopColor[0];
			if (pTopColor[1] > fLargest)
			{
				fLargest = pTopColor[1];
			}
			if (pTopColor[2] > fLargest)
			{
				fLargest = pTopColor[2];
			}
			if (fLargest > 1.0f)
			{
				pTopColor[0] /= fLargest;
				pTopColor[1] /= fLargest;
				pTopColor[2] /= fLargest;
			}
			pTopColor[0] = Math.Max(0.0f, pTopColor[0]);
			pTopColor[1] = Math.Max(0.0f, pTopColor[1]);
			pTopColor[2] = Math.Max(0.0f, pTopColor[2]);
		}
    
		return afLowColor[3];
	}
//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: virtual float Height(float fX, float fY, float* pNormal) const;
	public float Height(float fX, float fY, float[] pNormal)
	{
		float fHeight = 0.0f;
		float[] afPos = {fX, fY, 0.0f};
		fHeight = m_pMapOutdoor.GetHeight(afPos);
    
		pNormal[0] = 0.0f;
		pNormal[1] = 0.0f;
		pNormal[2] = 1.0f;
    
		return fHeight;
	}
	public void InitGraphics()
	{
    
		CGraphicImage pImage = (CGraphicImage) CResourceManager.Instance().GetResourcePointer("t:/laniaworkstate/special/brush_2.dds");
		m_GrassImageInstance.SetImagePointer(pImage);
		m_lpD3DTexure8 = m_GrassImageInstance.GetTexturePointer().GetD3DTexture();
    
		for (int LaniatusDefVariables = 0; LaniatusDefVariables < m_nNumRegions; ++i)
		{
			SRegion pRegion = m_pRegions + i;
			const int c_nNumCorners = 4;
			uint uiNumBlades = (uint)pRegion.m_vBlades.size();
			uint uiBufferSize = uiNumBlades * c_nNumCorners * c_nGrassVertexTotalSize;
			byte[] pBuffer = new byte[uiBufferSize];
    
	//# Laniatus Games Studio Inc. | TODO TASK: Pointer arithmetic is detected on this variable, so pointers on this variable are left unchanged:
	//# Laniatus Games Studio Inc. | TODO TASK: There is no equivalent to 'reinterpret_cast' in C#:
			float * pTexCoords0 = reinterpret_cast<float>(pBuffer + 0);
	//# Laniatus Games Studio Inc. | TODO TASK: Pointer arithmetic is detected on this variable, so pointers on this variable are left unchanged:
	//# Laniatus Games Studio Inc. | TODO TASK: There is no equivalent to 'reinterpret_cast' in C#:
			float * pTexCoords1 = reinterpret_cast<float>(pTexCoords0 + c_nGrassVertexTexture0Size * uiNumBlades * c_nNumCorners / sizeof(float));
	//# Laniatus Games Studio Inc. | TODO TASK: Pointer arithmetic is detected on this variable, so pointers on this variable are left unchanged:
			byte * pColors = (byte) pTexCoords1 + c_nGrassVertexTexture1Size * uiNumBlades * c_nNumCorners;
	//# Laniatus Games Studio Inc. | TODO TASK: Pointer arithmetic is detected on this variable, so pointers on this variable are left unchanged:
	//# Laniatus Games Studio Inc. | TODO TASK: There is no equivalent to 'reinterpret_cast' in C#:
			float * pPositions = reinterpret_cast<float>(pColors + c_nGrassVertexColorSize * uiNumBlades * c_nNumCorners);
    
			for (vector<SBlade>.const_iterator iBlade = pRegion.m_vBlades.begin(); iBlade != pRegion.m_vBlades.end(); ++iBlade)
			{
				float fS1 = (float)iBlade.m_ucWhichTexture / c_nNumBladeMaps;
				float fS2 = (float)(iBlade.m_ucWhichTexture + 1) / c_nNumBladeMaps;
    
				for (int nCorner = 0; nCorner < c_nNumCorners; ++nCorner)
				{
					switch (nCorner)
					{
					case 0:
						pTexCoords0[0] = fS2;
						pTexCoords0[1] = 1.0f;
						break;
					case 1:
						pTexCoords0[0] = fS1;
						pTexCoords0[1] = 1.0f;
						break;
					case 2:
						pTexCoords0[0] = fS1;
						pTexCoords0[1] = 0.0f;
						break;
					case 3:
						pTexCoords0[0] = fS2;
						pTexCoords0[1] = 0.0f;
						break;
					default:
						Debug.Assert(false);
						break;
					}
					pTexCoords0 += c_nGrassVertexTexture0Size / sizeof(float);
    
					switch (nCorner)
					{
					case 0:
						pTexCoords1[0] = c_nShaderGrassBillboard;
						pTexCoords1[2] = iBlade.m_fThrow;
						break;
					case 1:
						pTexCoords1[0] = c_nShaderGrassBillboard + 1;
						pTexCoords1[2] = iBlade.m_fThrow;
						break;
					case 2:
						pTexCoords1[0] = c_nShaderGrassBillboard + 2;
						pTexCoords1[2] = 0.0f;
						break;
					case 3:
						pTexCoords1[0] = c_nShaderGrassBillboard + 3;
						pTexCoords1[2] = 0.0f;
						break;
					default:
						Debug.Assert(false);
						break;
					}
					pTexCoords1[1] = iBlade.m_fSize;
					pTexCoords1[3] = iBlade.m_fNoise;
					pTexCoords1 += c_nGrassVertexTexture1Size / sizeof(float);
    
					uint ulColor = 0;
					if (nCorner == 0 || nCorner == 1)
					{
						ulColor = (uint)(((int)(iBlade.m_afTopColor[0] * 255.0f) << 0) + ((int)(iBlade.m_afTopColor[1] * 255.0f) << 8) + ((int)(iBlade.m_afTopColor[2] * 255.0f) << 16) + 0xff000000);
					}
					else
					{
						ulColor = (uint)(((int)(iBlade.m_afBottomColor[0] * 255.0f) << 0) + ((int)(iBlade.m_afBottomColor[1] * 255.0f) << 8) + ((int)(iBlade.m_afBottomColor[2] * 255.0f) << 16) + 0xff000000);
					}
	//# Laniatus Games Studio Inc. | TODO TASK: The memory management function 'memcpy' has no equivalent in C#:
					memcpy(pColors, ulColor, c_nGrassVertexColorSize);
					pColors += c_nGrassVertexColorSize;
    
	//# Laniatus Games Studio Inc. | TODO TASK: The memory management function 'memcpy' has no equivalent in C#:
					memcpy(pPositions, iBlade.m_afPos, c_nGrassVertexPositionSize);
					pPositions += c_nGrassVertexPositionSize / sizeof(float);
				}
			}
    
			 uint dwFVF = (uint)(D3DFVF_XYZ | D3DFVF_DIFFUSE | D3DFVF_TEX1);
			pBuffer = null;
		}
	}

		private CMapOutdoor m_pMapOutdoor;

		private LPDIRECT3DTEXTURE8 m_lpD3DTexure8 = new LPDIRECT3DTEXTURE8();

		private CGraphicImageInstance m_GrassImageInstance = new CGraphicImageInstance();
}

#endif
