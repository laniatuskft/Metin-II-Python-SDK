public class CGraphicFontTexture
{
//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public SCharacterInfomation UpdateCharacterInfomation(TCharacterKey code)
	{
		IntPtr hDC = m_dib.GetDCHandle();
		SelectObject(hDC, GetFont(code.first));
    
		char keyValue = code.second;
    
		if (keyValue == 0x08)
		{
			keyValue = ' ';
		}
    
		ABCFLOAT stABC = new ABCFLOAT();
		SIZE size = new SIZE();
    
		if (!GetTextExtentPoint32W(hDC, keyValue, 1, size) || !GetCharABCWidthsFloatW(hDC, keyValue, keyValue, stABC))
		{
			return null;
		}
    
		size.cx = stABC.abcfB;
		if (stABC.abcfA > 0.0f)
		{
			size.cx += ceilf(stABC.abcfA);
		}
		if (stABC.abcfC > 0.0f)
		{
			size.cx += ceilf(stABC.abcfC);
		}
		size.cx++;
    
		int lAdvance = ceilf(stABC.abcfA + stABC.abcfB + stABC.abcfC);
    
		int width = m_dib.GetWidth();
		int height = m_dib.GetHeight();
    
		if (m_x + size.cx >= (width - 1))
		{
			m_y += (m_step + 1);
			m_step = 0;
			m_x = 0;
    
			if (m_y + size.cy >= (height - 1))
			{
				if (!UpdateTexture())
				{
					return null;
				}
    
				if (!AppendTexture())
				{
					return null;
				}
    
				m_y = 0;
			}
		}
		int i_add = (strstr(m_fontName, "Tahoma") == 0) ? 1 : 0;
		TextOutW(hDC, m_x + i_add, m_y, keyValue, 1);
    
		int nChrX;
		int nChrY;
		int nChrWidth = size.cx;
		int nChrHeight = size.cy;
		int nDIBWidth = m_dib.GetWidth();
    
    
	//# Laniatus Games Studio Inc. | TODO TASK: C# does not have an equivalent to pointers to value types:
	//Original Metin2 CPlus Line: uint *pdwDIBData=(uint*)m_dib.GetPointer();
		uint pdwDIBData = (uint)m_dib.GetPointer();
	//# Laniatus Games Studio Inc. | TODO TASK: C# does not have an equivalent to pointers to value types:
	//Original Metin2 CPlus Line: uint *pdwDIBBase=pdwDIBData+nDIBWidth *m_y+m_x;
		uint pdwDIBBase = pdwDIBData + nDIBWidth * m_y + m_x;
	//# Laniatus Games Studio Inc. | TODO TASK: Pointer arithmetic is detected on this variable, so pointers on this variable are left unchanged:
		uint * pdwDIBRow;
    
		pdwDIBRow = pdwDIBBase;
		for (nChrY = 0; nChrY < nChrHeight; ++nChrY, pdwDIBRow += (uint)nDIBWidth)
		{
			for (nChrX = 0; nChrX < nChrWidth; ++nChrX)
			{
				pdwDIBRow[nChrX] = (pdwDIBRow[nChrX] & 0xff) != 0 ? 0xffff : 0;
			}
		}
    
		float rhwidth = 1.0f / (float)width;
		float rhheight = 1.0f / (float)height;
    
		TCharacterInfomation rNewCharInfo = m_charInfoMap[code];
    
		rNewCharInfo.index = m_pFontTextureVector.size() - 1;
		rNewCharInfo.width = size.cx;
		rNewCharInfo.height = size.cy;
		rNewCharInfo.left = (float)m_x * rhwidth;
		rNewCharInfo.top = (float)m_y * rhheight;
		rNewCharInfo.right = (float)(m_x + size.cx) * rhwidth;
		rNewCharInfo.bottom = (float)(m_y + size.cy) * rhheight;
		rNewCharInfo.advance = (float) lAdvance;
    
		m_x += size.cx;
    
		if (m_step < size.cy)
		{
			m_step = size.cy;
		}
    
		m_isDirty = true;
    
		return rNewCharInfo;
	}
}