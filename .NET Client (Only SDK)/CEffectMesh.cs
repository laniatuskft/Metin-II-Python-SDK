public class CEffectMesh
{
//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool GetMeshElementPointer(uint dwMeshIndex, TEffectMeshData[] ppMeshData)
	{
		if (dwMeshIndex >= m_pEffectMeshDataVector.size())
		{
			return false;
		}
    
		ppMeshData[0] = m_pEffectMeshDataVector[dwMeshIndex];
    
		return true;
	}
}