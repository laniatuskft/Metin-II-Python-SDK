public class CNetworkPacketHeaderMap
{
//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void Set(int header, TPacketType rPacketType)
	{
		m_headerMap[header] = rPacketType;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool Get(int header, TPacketType pPacketType)
	{
		SortedDictionary<int, TPacketType>.Enumerator f = m_headerMap.find(header);
    
		if (m_headerMap.end() == f)
		{
			return false;
		}
    
	//# Laniatus Games Studio Inc. | TODO TASK: Iterators are only converted within the context of 'while' and 'for' loops:
		pPacketType = f.second;
    
		return true;
	}
}