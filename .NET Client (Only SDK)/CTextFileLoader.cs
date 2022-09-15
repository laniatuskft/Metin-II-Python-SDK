public class CTextFileLoader
{
//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool LoadGroup(TGroupNode pGroupNode)
	{
		CTokenVector stTokenVector = new CTokenVector();
		int nLocalGroupDepth = 0;
    
		for (; m_dwcurLineIndex < m_textFileLoader.GetLineCount(); ++m_dwcurLineIndex)
		{
			int iRet;
    
			if ((iRet = m_textFileLoader.SplitLine2(m_dwcurLineIndex, stTokenVector)) != 0)
			{
				if (iRet == -2)
				{
					TraceError("cannot find \" in %s:%lu", m_strFileName.c_str(), m_dwcurLineIndex);
				}
				continue;
			}
    
			stl_lowers(stTokenVector[0]);
    
			if ('{' == stTokenVector[0][0])
			{
				nLocalGroupDepth++;
				continue;
			}
    
			if ('}' == stTokenVector[0][0])
			{
				nLocalGroupDepth--;
				break;
			}
    
			if (0 == stTokenVector[0].compare("group"))
			{
				if (2 != stTokenVector.size())
				{
					Debug.Assert(!"There is no group name!");
					continue;
				}
    
				TGroupNode pNewNode = TGroupNode.New();
				m_kVct_pkNode.push_back(pNewNode);
    
				pNewNode.pParentNode = pGroupNode;
				pNewNode.SetGroupName(stTokenVector[1]);
				pGroupNode.ChildNodeVector.push_back(pNewNode);
    
				++m_dwcurLineIndex;
    
				if (false == LoadGroup(pNewNode))
				{
					return false;
				}
			}
			else if (0 == stTokenVector[0].compare("list"))
			{
				if (2 != stTokenVector.size())
				{
					Debug.Assert(!"There is no list name!");
					continue;
				}
    
				CTokenVector stSubTokenVector = new CTokenVector();
    
				stl_lowers(stTokenVector[1]);
				string key = stTokenVector[1];
    
				stTokenVector.clear();
    
				++m_dwcurLineIndex;
				for (; m_dwcurLineIndex < m_textFileLoader.GetLineCount(); ++m_dwcurLineIndex)
				{
					if (!m_textFileLoader.SplitLine(m_dwcurLineIndex, stSubTokenVector))
					{
						continue;
					}
    
					if ('{' == stSubTokenVector[0][0])
					{
						continue;
					}
    
					if ('}' == stSubTokenVector[0][0])
					{
						break;
					}
    
					for (uint j = 0; j < stSubTokenVector.size(); ++j)
					{
						stTokenVector.push_back(stSubTokenVector[j]);
					}
				}
    
				pGroupNode.InsertTokenVector(key, stTokenVector);
			}
			else
			{
				string key = stTokenVector[0];
    
				if (1 == stTokenVector.size())
				{
					TraceError("CTextFileLoader::LoadGroup : must have a value (filename: %s line: %d key: %s)", m_strFileName.c_str(), m_dwcurLineIndex, key);
					break;
				}
    
				stTokenVector.erase(stTokenVector.begin());
				pGroupNode.InsertTokenVector(key, stTokenVector);
			}
		}
    
		return (nLocalGroupDepth == 0);
	}
}