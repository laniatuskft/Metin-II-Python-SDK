public class CEffectMeshScript
{
//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool GetMeshDataPointer(uint dwMeshIndex, TMeshData[] ppMeshData)
	{
		if (!CheckMeshIndex(dwMeshIndex))
		{
			return false;
		}
    
		ppMeshData[0] = &m_MeshDataVector[dwMeshIndex];
    
		return true;
	}
}