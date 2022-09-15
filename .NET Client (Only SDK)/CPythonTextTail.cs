public class CPythonTextTail
{
//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void UpdateTextTail(TTextTail pTextTail)
	{
		if (!pTextTail.pOwner)
		{
			return;
		}
    
		CPythonGraphic rpyGraphic = CPythonGraphic.Instance();
		rpyGraphic.Identity();
    
		_D3DVECTOR c_rv3Position = pTextTail.pOwner.GetPosition();
		rpyGraphic.ProjectPosition(c_rv3Position.x, c_rv3Position.y, c_rv3Position.z + pTextTail.fHeight, pTextTail.x, pTextTail.y, pTextTail.z);
    
		pTextTail.x = floorf(pTextTail.x);
		pTextTail.y = floorf(pTextTail.y);
    
		if (pTextTail.fDistanceFromPlayer < 1300.0f)
		{
			pTextTail.z = 0.0f;
		}
		else
		{
			pTextTail.z = pTextTail.z * CPythonGraphic.Instance().GetOrthoDepth() * -1.0f;
			pTextTail.z += 10.0f;
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void RenderTextTailBox(TTextTail pTextTail)
	{
		CPythonGraphic.Instance().SetDiffuseColor(0.0f, 0.0f, 0.0f, 1.0f);
		CPythonGraphic.Instance().RenderBox2d(pTextTail.x + pTextTail.xStart, pTextTail.y + pTextTail.yStart, pTextTail.x + pTextTail.xEnd, pTextTail.y + pTextTail.yEnd, pTextTail.z);
    
		CPythonGraphic.Instance().SetDiffuseColor(0.0f, 0.0f, 0.0f, 0.3f);
		CPythonGraphic.Instance().RenderBar2d(pTextTail.x + pTextTail.xStart, pTextTail.y + pTextTail.yStart, pTextTail.x + pTextTail.xEnd, pTextTail.y + pTextTail.yEnd, pTextTail.z);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void RenderTextTailName(TTextTail pTextTail)
	{
		pTextTail.pTextInstance.Render();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void UpdateDistance(in TPixelPosition c_rCenterPosition, TTextTail pTextTail)
	{
		_D3DVECTOR c_rv3Position = pTextTail.pOwner.GetPosition();
		D3DXVECTOR2 v2Distance = new D3DXVECTOR2(c_rv3Position.x - c_rCenterPosition.x, -c_rv3Position.y - c_rCenterPosition.y);
		pTextTail.fDistanceFromPlayer = D3DXVec2Length(v2Distance);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void DeleteTextTail(TTextTail pTextTail)
	{
		if (pTextTail.pTextInstance)
		{
			CGraphicTextInstance.Delete(pTextTail.pTextInstance);
			pTextTail.pTextInstance = null;
		}
		if (pTextTail.pOwnerTextInstance)
		{
			CGraphicTextInstance.Delete(pTextTail.pOwnerTextInstance);
			pTextTail.pOwnerTextInstance = null;
		}
		if (pTextTail.pMarkInstance)
		{
			CGraphicMarkInstance.Delete(pTextTail.pMarkInstance);
			pTextTail.pMarkInstance = null;
		}
		if (pTextTail.pGuildNameTextInstance)
		{
			CGraphicTextInstance.Delete(pTextTail.pGuildNameTextInstance);
			pTextTail.pGuildNameTextInstance = null;
		}
		if (pTextTail.pTitleTextInstance)
		{
			CGraphicTextInstance.Delete(pTextTail.pTitleTextInstance);
			pTextTail.pTitleTextInstance = null;
		}
		if (pTextTail.pLevelTextInstance)
		{
			CGraphicTextInstance.Delete(pTextTail.pLevelTextInstance);
			pTextTail.pLevelTextInstance = null;
		}
    
		m_TextTailPool.Free(pTextTail);
	}
}