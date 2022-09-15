public class CFileLoaderThread
{
//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool Fetch(TData[] ppData)
	{
		m_CompleteMutex.Lock();
    
		if (m_pCompleteDeque.empty())
		{
			m_CompleteMutex.Unlock();
			return false;
		}
    
		ppData[0] = m_pCompleteDeque.front();
		m_pCompleteDeque.pop_front();
    
		m_CompleteMutex.Unlock();
		return true;
	}
}