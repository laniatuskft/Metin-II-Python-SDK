public class SObjectInstance
{
//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetTree(float x, float y, float z, uint dwTreeCRC, string c_szTreeName)
	{
		CSpeedTreeForestDirectX8 rkForest = CSpeedTreeForestDirectX8.Instance();
		pTree = rkForest.CreateInstance(x, y, z, dwTreeCRC, c_szTreeName);
		dwType = prt.PROPERTY_TYPE_TREE;
	}
}