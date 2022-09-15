public class CRaceMotionData
{
//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool GetMotionEventDataPointer(byte byIndex, CRaceMotionData.TMotionEventData[] c_ppData)
	{
		if (byIndex >= m_MotionEventDataVector.size())
		{
			return false;
		}
    
		c_ppData[0] = m_MotionEventDataVector[byIndex];
    
		return true;
	}
}