public class CResource
{
//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool OnIsType(TType type)
	{
		if (CResource.Type() == type)
		{
			return true;
		}
    
		return false;
	}
}