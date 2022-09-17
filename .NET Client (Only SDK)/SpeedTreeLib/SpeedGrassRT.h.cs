using System.Collections.Generic;

#if USE_SPEEDGRASS

//# Laniatus Games Studio Inc. |: C# has no need of forward class declarations:
//class CIdvTerrain;
public class CSpeedGrassRT : System.IDisposable
{
	public CSpeedGrassRT()
	{
		this.m_nNumRegions = 0;
		this.m_nNumRegionCols = 0;
		this.m_nNumRegionRows = 0;
		this.m_pRegions = null;
		this.m_bAllRegionsCulled = false;
		m_afBoundingBox[0] = m_afBoundingBox[1] = m_afBoundingBox[2] = 0.0f;
		m_afBoundingBox[3] = m_afBoundingBox[4] = m_afBoundingBox[5] = 1.0f;
	}
	public void Dispose()
	{
	}

		public class SBlade
		{
//# Laniatus Games Studio Inc. | TODO TASK: The implementation of the following method could not be found:
//			SBlade();
			public float[] m_afPos = new float[3];
			public float[] m_afNormal = new float[3];
			public float m_fSize;
			public byte m_ucWhichTexture;
			public float m_fNoise;
			public float m_fThrow;
			public float[] m_afBottomColor = new float[3];
			public float[] m_afTopColor = new float[3];
		}

		public class SRegion
		{
//# Laniatus Games Studio Inc. | TODO TASK: The implementation of the following method could not be found:
//			SRegion();

			public float[] m_afCenter = new float[3];
			public float[] m_afMin = new float[3];
			public float[] m_afMax = new float[3];

			public bool m_bCulled;
			public float m_fCullingRadius;

			public List<SBlade> m_vBlades = new List<SBlade>();
			public CGraphicVertexBuffer m_VertexBuffer = new CGraphicVertexBuffer();
		}

	public void DeleteRegions()
	{
		m_pRegions = null;
		m_pRegions = null;
		m_nNumRegions = 0;
	}
	public CSpeedGrassRT.SRegion GetRegions(ref uint uiNumRegions)
	{
		uiNumRegions = m_nNumRegions;
    
		return m_pRegions;
	}
	public bool ParseBsfFile(string pFilename, uint nNumBlades, uint uiRows, uint uiCols, float fCollisionDistance)
	{
		bool bSuccess = false;
    
		m_nNumRegionCols = (int)uiCols;
		m_nNumRegionRows = (int)uiRows;
    
		m_afBoundingBox[0] = m_afBoundingBox[1] = m_afBoundingBox[2] = float.MaxValue;
		m_afBoundingBox[3] = m_afBoundingBox[4] = m_afBoundingBox[5] = -float.MaxValue;
    
		CBoundaryShapeManager cManager = new CBoundaryShapeManager();
		vector<SBlade> vSceneBlades = new vector<SBlade>();
    
		if (cManager.LoadBsfFile(pFilename))
		{
			for (uint LaniatusDefVariables = 0; LaniatusDefVariables < nNumBlades; ++i)
			{
				SBlade sBlade = new SBlade();
    
				if (cManager.RandomPoint(sBlade.m_afPos[0], sBlade.m_afPos[1]))
				{
					sBlade.m_afPos[2] = Height(sBlade.m_afPos[0], sBlade.m_afPos[1], sBlade.m_afNormal);
    
					D3DXVECTOR3 v3Normal = new D3DXVECTOR3(sBlade.m_afNormal[0], sBlade.m_afNormal[1], sBlade.m_afNormal[2]);
					D3DXVec3Normalize(v3Normal, v3Normal);
					v3Normal.z = -v3Normal.z;
					sBlade.m_afNormal[0] = v3Normal.x;
					sBlade.m_afNormal[1] = v3Normal.y;
					sBlade.m_afNormal[2] = v3Normal.z;
    
					for (int nAxis = 0; nAxis < 3; ++nAxis)
					{
						m_afBoundingBox[nAxis] = (((m_afBoundingBox[nAxis]) < (sBlade.m_afPos[nAxis])) ? (m_afBoundingBox[nAxis]) : (sBlade.m_afPos[nAxis]));
						m_afBoundingBox[nAxis + 3] = (((m_afBoundingBox[nAxis + 3]) > (sBlade.m_afPos[nAxis])) ? (m_afBoundingBox[nAxis + 3]) : (sBlade.m_afPos[nAxis]));
					}
    
					float fHeightPercent = Color(sBlade.m_afPos[0], sBlade.m_afPos[1], sBlade.m_afNormal, sBlade.m_afTopColor, sBlade.m_afBottomColor);
					sBlade.m_fSize = VecInterpolate(c_fMinBladeSize, c_fMaxBladeSize, fHeightPercent);
    
					sBlade.m_ucWhichTexture = GetRandom(0, c_nNumBladeMaps - 1);
    
					sBlade.m_fNoise = GetRandom(c_fMinBladeNoise, c_fMaxBladeNoise);
					sBlade.m_fThrow = GetRandom(c_fMinBladeThrow, c_fMaxBladeThrow);
    
					vSceneBlades.push_back(sBlade);
				}
			}
    
			bSuccess = true;
		}
		else
		{
			fprintf(stderr, "%s\n", cManager.GetCurrentError().c_str());
		}
    
		if (bSuccess)
		{
			CreateRegions(vSceneBlades, fCollisionDistance);
		}
    
		return bSuccess;
	}
	public bool CustomPlacement(uint uiRows, uint uiCols)
	{
		m_nNumRegionCols = (int)uiCols;
		m_nNumRegionRows = (int)uiRows;
    
		m_afBoundingBox[0] = m_afBoundingBox[1] = m_afBoundingBox[2] = float.MaxValue;
		m_afBoundingBox[3] = m_afBoundingBox[4] = m_afBoundingBox[5] = -float.MaxValue;
    
		vector<SBlade> vSceneBlades = new vector<SBlade>();
    
		SBlade sBlade = new SBlade();
    
		sBlade.m_afPos[0] = 0.0f;
		sBlade.m_afPos[1] = 0.0f;
		sBlade.m_afPos[2] = 0.0f;
    
		sBlade.m_afNormal[0] = 0.0f;
		sBlade.m_afNormal[1] = 0.0f;
		sBlade.m_afNormal[2] = 1.0f;
    
		for (int nAxis = 0; nAxis < 3; ++nAxis)
		{
			m_afBoundingBox[nAxis] = (((m_afBoundingBox[nAxis]) < (sBlade.m_afPos[nAxis])) ? (m_afBoundingBox[nAxis]) : (sBlade.m_afPos[nAxis]));
			m_afBoundingBox[nAxis + 3] = (((m_afBoundingBox[nAxis + 3]) > (sBlade.m_afPos[nAxis])) ? (m_afBoundingBox[nAxis + 3]) : (sBlade.m_afPos[nAxis]));
		}
    
	//# Laniatus Games Studio Inc. | TODO TASK: The memory management function 'memcpy' has no equivalent in C#:
		memcpy(sBlade.m_afBottomColor, sBlade.m_afNormal, 12);
	//# Laniatus Games Studio Inc. | TODO TASK: The memory management function 'memcpy' has no equivalent in C#:
		memcpy(sBlade.m_afTopColor, sBlade.m_afNormal, 12);
    
		sBlade.m_ucWhichTexture = GetRandom(0, c_nNumBladeMaps - 1);
    
		sBlade.m_fNoise = GetRandom(c_fMinBladeNoise, c_fMaxBladeNoise);
		sBlade.m_fThrow = GetRandom(c_fMinBladeThrow, c_fMaxBladeThrow);
    
		sBlade.m_fSize = GetRandom(c_fMinBladeSize, c_fMaxBladeSize);
    
		vSceneBlades.push_back(sBlade);
		CreateRegions(vSceneBlades);
    
		return true;
	}

	public void RotateAxisFromIdentity(D3DXMATRIX pMat, in float c_fAngle, in D3DXVECTOR3 c_rv3Axis)
	{
		float s = sinf((c_fAngle) / 57.29578f);
		float c = cosf((c_fAngle) / 57.29578f);
		float t = 1.0 - c;
    
		float x = c_rv3Axis.x;
		float y = c_rv3Axis.y;
		float z = c_rv3Axis.z;
    
		pMat._11 = t * x * x + c;
		pMat._12 = t * x * y + s * z;
		pMat._13 = t * x * z - s * y;
		pMat._21 = t * x * y - s * z;
		pMat._22 = t * y * y + c;
		pMat._23 = t * y * z + s * x;
		pMat._31 = t * x * z + s * y;
		pMat._32 = t * y * z - s * x;
		pMat._33 = t * z * z + c;
	}

//# Laniatus Games Studio Inc. | WARN: C# has no equivalent to methods returning pointers to value types:
//Original Metin2 CPlus Line: static const float* GetUnitBillboard()
public static float GetUnitBillboard()
{
	return m_afUnitBillboard;
}

	public void GetLodParams(ref float fFarDistance, ref float fTransitionLength)
	{
		fFarDistance = m_fLodFarDistance;
		fTransitionLength = m_fLodTransitionLength;
	}
	public void SetLodParams(float fFarDistance, float fTransitionLength)
	{
		m_fLodFarDistance = fFarDistance;
		m_fLodTransitionLength = fTransitionLength;
	}


//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: bool AllRegionsAreCulled() const
		public bool AllRegionsAreCulled()
		{
			return m_bAllRegionsCulled;
		}
	public void Cull()
	{
		int[] anFrustumCellsMin = new int[2];
		int[] anFrustumCellsMax = new int[2];
		ConvertCoordsToCell(m_afFrustumMin, anFrustumCellsMin);
		ConvertCoordsToCell(m_afFrustumMax, anFrustumCellsMax);
    
		for (int LaniatusDefVariables = 0; LaniatusDefVariables < m_nNumRegions; ++i)
		{
			m_pRegions[LaniatusDefVariables].m_bCulled = true;
		}
    
		int nRegionsDrawn = 0;
    
		if ((anFrustumCellsMin[0] < 0 && anFrustumCellsMax[0] < 0) || (anFrustumCellsMin[0] >= m_nNumRegionCols && anFrustumCellsMax[0] >= m_nNumRegionCols) || (anFrustumCellsMin[1] < 0 && anFrustumCellsMax[1] < 0) || (anFrustumCellsMin[1] >= m_nNumRegionRows && anFrustumCellsMax[1] >= m_nNumRegionRows))
		{
			m_bAllRegionsCulled = true;
		}
		else
		{
			anFrustumCellsMin[0] = (((anFrustumCellsMin[0]) > (0)) ? (anFrustumCellsMin[0]) : (0));
			anFrustumCellsMin[1] = (((anFrustumCellsMin[1]) > (0)) ? (anFrustumCellsMin[1]) : (0));
			anFrustumCellsMax[0] = (((anFrustumCellsMax[0]) < (m_nNumRegionCols - 1)) ? (anFrustumCellsMax[0]) : (m_nNumRegionCols - 1));
			anFrustumCellsMax[1] = (((anFrustumCellsMax[1]) < (m_nNumRegionRows - 1)) ? (anFrustumCellsMax[1]) : (m_nNumRegionRows - 1));
    
			for (i = anFrustumCellsMin[0]; LaniatusDefVariables <= anFrustumCellsMax[0]; ++i)
			{
				for (int j = anFrustumCellsMin[1]; j <= anFrustumCellsMax[1]; ++j)
				{
					SRegion pRegion = m_pRegions + GetRegionIndex(j, i);
					pRegion.m_bCulled = OutsideFrustum(pRegion);
				}
			}
    
			m_bAllRegionsCulled = false;
		}
	}


	public void SetWindDirection(float pWindDir)
	{
	//# Laniatus Games Studio Inc. | TODO TASK: The memory management function 'memcpy' has no equivalent in C#:
		memcpy(m_afWindDir, pWindDir, 3 * sizeof(float));
		m_afWindDir[3] = 0.0f;
	}
//# Laniatus Games Studio Inc. | WARN: C# has no equivalent to methods returning pointers to value types:
//Original Metin2 CPlus Line: static const float* GetWindDirection();
	public float GetWindDirection()
	{
		return m_afWindDir;
	}


//# Laniatus Games Studio Inc. | WARN: C# has no equivalent to methods returning pointers to value types:
//Original Metin2 CPlus Line: static const float* GetCameraPos();
	public float GetCameraPos()
	{
		return m_afCameraPos;
	}
	public void SetCamera(float pPosition, double[] pModelviewMatrix)
	{
	//# Laniatus Games Studio Inc. | TODO TASK: The memory management function 'memcpy' has no equivalent in C#:
		memcpy(m_afCameraPos, pPosition, 3 * sizeof(float));
    
		m_afCameraRight[0] = pModelviewMatrix[0];
		m_afCameraRight[1] = pModelviewMatrix[4];
		m_afCameraRight[2] = pModelviewMatrix[8];
    
		m_afCameraUp[0] = pModelviewMatrix[1];
		m_afCameraUp[1] = pModelviewMatrix[5];
		m_afCameraUp[2] = pModelviewMatrix[9];
    
		m_afCameraOut[0] = pModelviewMatrix[2];
		m_afCameraOut[1] = pModelviewMatrix[6];
		m_afCameraOut[2] = pModelviewMatrix[10];
    
		ComputeUnitBillboard();
    
		ComputeFrustum();
	}
	public void SetPerspective(float fAspectRatio, float fFieldOfView)
	{
		m_fAspectRatio = fAspectRatio;
		m_fFieldOfView = D3DXToRadian(fAspectRatio * fFieldOfView);
	}


//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: virtual float Color(float fX, float fY, const float* pNormal, float* pTopColor, float* pBottomColor) const
public virtual float Color(float fX, float fY, float pNormal, ref float pTopColor, ref float pBottomColor)
{
	return 0.0f;
}
//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: virtual float Height(float fX, float fY, float* pNormal) const
public virtual float Height(float fX, float fY, ref float pNormal)
{
	return 0.0f;
}


	public void CreateRegions(in vector<SBlade> vSceneBlades, float fCollisionDistance)
	{
    
		DeleteRegions();
		m_nNumRegions = (int)(m_nNumRegionRows * m_nNumRegionCols);
		m_pRegions = Arrays.InitializeWithDefaultInstances<SRegion>(m_nNumRegions);
    
		float fCellWidth = (m_afBoundingBox[3] - m_afBoundingBox[0]) / m_nNumRegionCols;
		float fCellHeight = (m_afBoundingBox[4] - m_afBoundingBox[1]) / m_nNumRegionRows;
    
		float fY = m_afBoundingBox[1];
		for (int nRow = 0; nRow < m_nNumRegionRows; ++nRow)
		{
			float fX = m_afBoundingBox[0];
			for (int nCol = 0; nCol < m_nNumRegionCols; ++nCol)
			{
				SRegion pRegion = m_pRegions + GetRegionIndex(nRow, nCol);
    
				pRegion.m_afMin[0] = fX;
				pRegion.m_afMax[0] = fX + fCellWidth;
				pRegion.m_afMin[1] = fY;
				pRegion.m_afMax[1] = fY + fCellHeight;
    
				pRegion.m_afCenter[0] = 0.5f * (pRegion.m_afMin[0] + pRegion.m_afMax[0]);
				pRegion.m_afCenter[1] = 0.5f * (pRegion.m_afMin[1] + pRegion.m_afMax[1]);
    
				pRegion.m_fCullingRadius = 1.1f * Math.Sqrt(((pRegion.m_afMax[0] - pRegion.m_afCenter[0]) * (pRegion.m_afMax[0] - pRegion.m_afCenter[0])) + ((pRegion.m_afMax[1] - pRegion.m_afCenter[1]) * (pRegion.m_afMax[1] - pRegion.m_afCenter[1])));
    
				fX += fCellWidth;
			}
    
			fY += fCellHeight;
		}
    
		for (vector<SBlade>.const_iterator iBlade = vSceneBlades.begin(); iBlade != vSceneBlades.end(); ++iBlade)
		{
			float fPercentAlongX = (iBlade.m_afPos[0] - m_afBoundingBox[0]) / (m_afBoundingBox[3] - m_afBoundingBox[0]);
			float fPercentAlongY = (iBlade.m_afPos[1] - m_afBoundingBox[1]) / (m_afBoundingBox[4] - m_afBoundingBox[1]);
    
			uint uiCol = (((fPercentAlongX * m_nNumRegionCols) < (m_nNumRegionCols - 1)) ? (fPercentAlongX * m_nNumRegionCols) : (m_nNumRegionCols - 1));
			uint uiRow = (((fPercentAlongY * m_nNumRegionRows) < (m_nNumRegionRows - 1)) ? (fPercentAlongY * m_nNumRegionRows) : (m_nNumRegionRows - 1));
    
			m_pRegions[GetRegionIndex(uiRow, uiCol)].m_vBlades.push_back(*iBlade);
		}
    
		for (int LaniatusDefVariables = 0; LaniatusDefVariables < m_nNumRegions; ++i)
		{
			SRegion pRegion = m_pRegions + i;
    
			pRegion.m_afMin[2] = float.MaxValue;
			pRegion.m_afMax[2] = -float.MaxValue;
			for (vector<SBlade>.iterator iBlade = pRegion.m_vBlades.begin(); iBlade != pRegion.m_vBlades.end(); ++iBlade)
			{
				pRegion.m_afMin[2] = (((pRegion.m_afMin[2]) < (iBlade.m_afPos[2])) ? (pRegion.m_afMin[2]) : (iBlade.m_afPos[2]));
				pRegion.m_afMax[2] = (((pRegion.m_afMax[2]) > (iBlade.m_afPos[2] + iBlade.m_fSize)) ? (pRegion.m_afMax[2]) : (iBlade.m_afPos[2] + iBlade.m_fSize));
			}
    
			pRegion.m_afCenter[0] = 0.5f * (pRegion.m_afMin[0] + pRegion.m_afMax[0]);
			pRegion.m_afCenter[1] = 0.5f * (pRegion.m_afMin[1] + pRegion.m_afMax[1]);
			pRegion.m_afCenter[2] = 0.5f * (pRegion.m_afMin[2] + pRegion.m_afMax[2]);
    
			pRegion.m_fCullingRadius = 1.1f * Math.Sqrt(((pRegion.m_afMax[0] - pRegion.m_afCenter[0]) * (pRegion.m_afMax[0] - pRegion.m_afCenter[0])) + ((pRegion.m_afMax[1] - pRegion.m_afCenter[1]) * (pRegion.m_afMax[1] - pRegion.m_afCenter[1])) + ((pRegion.m_afMax[2] - pRegion.m_afCenter[2]) * (pRegion.m_afMax[2] - pRegion.m_afCenter[2])));
		}
    
		if (fCollisionDistance > 0.0f)
		{
			fCollisionDistance *= fCollisionDistance;
			for (int nRow = 0; nRow < m_nNumRegionRows; ++nRow)
			{
				float fX = m_afBoundingBox[0];
				for (int nCol = 0; nCol < m_nNumRegionCols; ++nCol)
				{
					SRegion pRegion = m_pRegions + GetRegionIndex(nRow, nCol);
    
					for (uint LaniatusDefVariables = 0; LaniatusDefVariables < pRegion.m_vBlades.size(); ++i)
					{
						float fX = pRegion.m_vBlades[LaniatusDefVariables].m_afPos[0];
						float fY = pRegion.m_vBlades[LaniatusDefVariables].m_afPos[1];
						bool bCollision = false;
						for (uint j = 0; j < pRegion.m_vBlades.size() && !bCollision; ++j)
						{
							if (i != j)
							{
								float fDistance = (fX - pRegion.m_vBlades[j].m_afPos[0]) * (fX - pRegion.m_vBlades[j].m_afPos[0]) + (fY - pRegion.m_vBlades[j].m_afPos[1]) * (fY - pRegion.m_vBlades[j].m_afPos[1]);
								if (fDistance < fCollisionDistance)
								{
									bCollision = true;
								}
							}
						}
    
						if (bCollision)
						{
							pRegion.m_vBlades.erase(pRegion.m_vBlades.begin() + LaniatusDefVariables--);
						}
					}
				}
			}
		}
	}
	public void ComputeFrustum()
	{
		D3DXVECTOR3 cCameraIn = new D3DXVECTOR3(-m_afCameraOut[0], -m_afCameraOut[1], -m_afCameraOut[2]);
		D3DXVECTOR3 cCameraUp = new D3DXVECTOR3(m_afCameraUp[0], m_afCameraUp[1], m_afCameraUp[2]);
		D3DXVECTOR3 cCameraRight = new D3DXVECTOR3(m_afCameraRight[0], m_afCameraRight[1], m_afCameraRight[2]);
		D3DXVECTOR3 cCameraPos = new D3DXVECTOR3(m_afCameraPos[0], m_afCameraPos[1], m_afCameraPos[2]);
		D3DXVECTOR3 cFarPoint = cCameraPos + cCameraIn * (m_fLodFarDistance + m_fLodTransitionLength);
    
		m_afFrustumPlanes[0][0] = cCameraIn.x;
		m_afFrustumPlanes[0][1] = cCameraIn.y;
		m_afFrustumPlanes[0][2] = cCameraIn.z;
		m_afFrustumPlanes[0][3] = -D3DXVec3Dot(cCameraIn, cFarPoint);
    
		D3DXMATRIX cRotate = new D3DXMATRIX();
		D3DXMatrixIdentity(cRotate);
		D3DXVECTOR3 cNormal = new D3DXVECTOR3();
    
		RotateAxisFromIdentity(cRotate, D3DXToDegree(0.5f * m_fFieldOfView * m_fAspectRatio + c_fHalfPi), cCameraRight);
		D3DXVec3TransformCoord(cNormal, cCameraIn, cRotate);
		D3DXVec3Normalize(cNormal, cNormal);
		m_afFrustumPlanes[1][0] = cNormal.x;
		m_afFrustumPlanes[1][1] = cNormal.y;
		m_afFrustumPlanes[1][2] = cNormal.z;
		m_afFrustumPlanes[1][3] = -D3DXVec3Dot(cNormal, cCameraPos);
    
		RotateAxisFromIdentity(cRotate, D3DXToDegree(0.5f * m_fFieldOfView + c_fHalfPi), cCameraUp);
		D3DXVec3TransformCoord(cNormal, cCameraIn, cRotate);
		D3DXVec3Normalize(cNormal, cNormal);
		m_afFrustumPlanes[2][0] = cNormal.x;
		m_afFrustumPlanes[2][1] = cNormal.y;
		m_afFrustumPlanes[2][2] = cNormal.z;
		m_afFrustumPlanes[2][3] = -D3DXVec3Dot(cNormal, cCameraPos);
    
		RotateAxisFromIdentity(cRotate, -D3DXToDegree(0.5f * m_fFieldOfView * m_fAspectRatio + c_fHalfPi), cCameraRight);
		D3DXVec3TransformCoord(cNormal, cCameraIn, cRotate);
		D3DXVec3Normalize(cNormal, cNormal);
		m_afFrustumPlanes[3][0] = cNormal.x;
		m_afFrustumPlanes[3][1] = cNormal.y;
		m_afFrustumPlanes[3][2] = cNormal.z;
		m_afFrustumPlanes[3][3] = -D3DXVec3Dot(cNormal, cCameraPos);
    
		RotateAxisFromIdentity(cRotate, -D3DXToDegree(0.5f * m_fFieldOfView + c_fHalfPi), cCameraUp);
		D3DXVec3TransformCoord(cNormal, cCameraIn, cRotate);
		D3DXVec3Normalize(cNormal, cNormal);
		m_afFrustumPlanes[4][0] = cNormal.x;
		m_afFrustumPlanes[4][1] = cNormal.y;
		m_afFrustumPlanes[4][2] = cNormal.z;
		m_afFrustumPlanes[4][3] = -D3DXVec3Dot(cNormal, cCameraPos);
    
		float fFrustumHeight = (m_fLodFarDistance + m_fLodTransitionLength) * tanf(0.5f * m_fFieldOfView);
		float fFrustumWidth = (m_fLodFarDistance + m_fLodTransitionLength) * tanf(0.5f * m_fFieldOfView * m_fAspectRatio);
    
		D3DXVECTOR3[] acFrustum = Arrays.InitializeWithDefaultInstances<D3DXVECTOR3>(5);
	//# Laniatus Games Studio Inc. | TODO TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'CopyFrom' method should be created:
	//Original Metin2 CPlus Line: acFrustum[0] = cCameraPos;
		acFrustum[0].CopyFrom(cCameraPos);
	//# Laniatus Games Studio Inc. | TODO TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'CopyFrom' method should be created:
	//Original Metin2 CPlus Line: acFrustum[1] = cFarPoint + cCameraRight * fFrustumWidth + cCameraUp * fFrustumHeight;
		acFrustum[1].CopyFrom(cFarPoint + cCameraRight * fFrustumWidth + cCameraUp * fFrustumHeight);
	//# Laniatus Games Studio Inc. | TODO TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'CopyFrom' method should be created:
	//Original Metin2 CPlus Line: acFrustum[2] = cFarPoint - cCameraRight * fFrustumWidth + cCameraUp * fFrustumHeight;
		acFrustum[2].CopyFrom(cFarPoint - cCameraRight * fFrustumWidth + cCameraUp * fFrustumHeight);
	//# Laniatus Games Studio Inc. | TODO TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'CopyFrom' method should be created:
	//Original Metin2 CPlus Line: acFrustum[3] = cFarPoint - cCameraRight * fFrustumWidth - cCameraUp * fFrustumHeight;
		acFrustum[3].CopyFrom(cFarPoint - cCameraRight * fFrustumWidth - cCameraUp * fFrustumHeight);
	//# Laniatus Games Studio Inc. | TODO TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'CopyFrom' method should be created:
	//Original Metin2 CPlus Line: acFrustum[4] = cFarPoint + cCameraRight * fFrustumWidth - cCameraUp * fFrustumHeight;
		acFrustum[4].CopyFrom(cFarPoint + cCameraRight * fFrustumWidth - cCameraUp * fFrustumHeight);
    
		m_afFrustumMin[0] = m_afFrustumMin[1] = float.MaxValue;
		m_afFrustumMax[0] = m_afFrustumMax[1] = -float.MaxValue;
		for (int LaniatusDefVariables = 0; LaniatusDefVariables < 5; ++i)
		{
			m_afFrustumMin[0] = (((m_afFrustumMin[0]) < (acFrustum[LaniatusDefVariables][0])) ? (m_afFrustumMin[0]) : (acFrustum[LaniatusDefVariables][0]));
			m_afFrustumMax[0] = (((m_afFrustumMax[0]) > (acFrustum[LaniatusDefVariables][0])) ? (m_afFrustumMax[0]) : (acFrustum[LaniatusDefVariables][0]));
			m_afFrustumMin[1] = (((m_afFrustumMin[1]) < (acFrustum[LaniatusDefVariables][1])) ? (m_afFrustumMin[1]) : (acFrustum[LaniatusDefVariables][1]));
			m_afFrustumMax[1] = (((m_afFrustumMax[1]) > (acFrustum[LaniatusDefVariables][1])) ? (m_afFrustumMax[1]) : (acFrustum[LaniatusDefVariables][1]));
		}
	}
	public void ComputeUnitBillboard()
	{
		float fAzimuth = Math.Atan2(-m_afCameraOut[1], -m_afCameraOut[0]);
    
		D3DXMATRIX cTrans = new D3DXMATRIX();
		D3DXMatrixRotationZ(cTrans, fAzimuth);
    
	//# Laniatus Games Studio Inc. |: This static local variable declaration (not allowed in C#) has been moved just prior to the method:
	//	static D3DXVECTOR3 afCorner1(0.0f, 0.5f, 1.0f);
	//# Laniatus Games Studio Inc. |: This static local variable declaration (not allowed in C#) has been moved just prior to the method:
	//	static D3DXVECTOR3 afCorner2(0.0f, -0.5f, 1.0f);
	//# Laniatus Games Studio Inc. |: This static local variable declaration (not allowed in C#) has been moved just prior to the method:
	//	static D3DXVECTOR3 afCorner3(0.0f, -0.5f, 0.0f);
	//# Laniatus Games Studio Inc. |: This static local variable declaration (not allowed in C#) has been moved just prior to the method:
	//	static D3DXVECTOR3 afCorner4(0.0f, 0.5f, 0.0f);
    
		D3DXVECTOR3 afNewCorner1 = new D3DXVECTOR3();
		D3DXVECTOR3 afNewCorner2 = new D3DXVECTOR3();
		D3DXVECTOR3 afNewCorner3 = new D3DXVECTOR3();
		D3DXVECTOR3 afNewCorner4 = new D3DXVECTOR3();
    
		D3DXVec3TransformCoord(afNewCorner1, ComputeUnitBillboard_afCorner1, cTrans);
		D3DXVec3TransformCoord(afNewCorner2, ComputeUnitBillboard_afCorner2, cTrans);
		D3DXVec3TransformCoord(afNewCorner3, ComputeUnitBillboard_afCorner3, cTrans);
		D3DXVec3TransformCoord(afNewCorner4, ComputeUnitBillboard_afCorner4, cTrans);
    
		m_afUnitBillboard[0] = afNewCorner1.x;
		m_afUnitBillboard[1] = afNewCorner1.y;
		m_afUnitBillboard[2] = afNewCorner1.z;
		m_afUnitBillboard[3] = afNewCorner2.x;
		m_afUnitBillboard[4] = afNewCorner2.y;
		m_afUnitBillboard[5] = afNewCorner2.z;
		m_afUnitBillboard[6] = afNewCorner3.x;
		m_afUnitBillboard[7] = afNewCorner3.y;
		m_afUnitBillboard[8] = afNewCorner3.z;
		m_afUnitBillboard[9] = afNewCorner4.x;
		m_afUnitBillboard[10] = afNewCorner4.y;
		m_afUnitBillboard[11] = afNewCorner4.z;
	}
//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: void ConvertCoordsToCell(const float* pCoords, int* pGridCoords) const;
	public void ConvertCoordsToCell(float[] pCoords, int[] pGridCoords)
	{
		float fPercentAlongX = (pCoords[0] - m_afBoundingBox[0]) / (m_afBoundingBox[3] - m_afBoundingBox[0]);
		float fPercentAlongY = (pCoords[1] - m_afBoundingBox[1]) / (m_afBoundingBox[4] - m_afBoundingBox[1]);
    
		if (fPercentAlongX < 0.0f)
		{
			pGridCoords[0] = -1;
		}
		else if (fPercentAlongX > 1.0f)
		{
			pGridCoords[0] = m_nNumRegionCols;
		}
		else
		{
			pGridCoords[0] = fPercentAlongX * m_nNumRegionCols;
		}
    
		if (fPercentAlongY < 0.0f)
		{
			pGridCoords[1] = -1;
		}
		else if (fPercentAlongY > 1.0f)
		{
			pGridCoords[1] = m_nNumRegionRows;
		}
		else
		{
			pGridCoords[1] = fPercentAlongY * m_nNumRegionRows;
		}
	}
//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: uint GetRegionIndex(uint uiRow, uint uiCol) const
		protected uint GetRegionIndex(uint uiRow, uint uiCol)
		{
			return uiRow * m_nNumRegionCols + uiCol;
		}
	public bool OutsideFrustum(CSpeedGrassRT.SRegion pRegion)
	{
		bool bOutside = false;
    
		for (int LaniatusDefVariables = 0; LaniatusDefVariables < 5 && !bOutside; ++i)
		{
			if (m_afFrustumPlanes[LaniatusDefVariables][0] * pRegion.m_afCenter[0] + m_afFrustumPlanes[LaniatusDefVariables][1] * pRegion.m_afCenter[1] + m_afFrustumPlanes[LaniatusDefVariables][2] * pRegion.m_afCenter[2] + m_afFrustumPlanes[LaniatusDefVariables][3] > pRegion.m_fCullingRadius)
			{
				bOutside = true;
			}
		}
    
		return bOutside;
	}

protected static float m_fLodFarDistance;
protected static float m_fLodTransitionLength;
protected static float[] m_afUnitBillboard = new float[12];
protected static float[] m_afWindDir = new float[4];

		protected int m_nNumRegions;
		protected int m_nNumRegionCols;
		protected int m_nNumRegionRows;
		protected SRegion[] m_pRegions;

protected static float[] m_afCameraOut = new float[3];
protected static float[] m_afCameraRight = new float[3];
protected static float[] m_afCameraUp = new float[3];
protected static float[] m_afCameraPos = new float[3];
protected static float m_fFieldOfView;
protected static float m_fAspectRatio;

protected static float[] m_afFrustumBox = new float[6];
protected static float[] m_afFrustumMin = new float[2];
protected static float[] m_afFrustumMax = new float[2];
protected static float[][] m_afFrustumPlanes = RectangularArrays.RectangularFloatArray(5, 4);
		protected float[] m_afBoundingBox = new float[6];
		protected bool m_bAllRegionsCulled;
}