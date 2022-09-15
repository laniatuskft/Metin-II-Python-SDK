namespace NRaceData
{

	public class NRaceData
	{
//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
			public void DestroySystem()
			{
				g_CollisionDataPool.Destroy();
				g_EffectDataPool.Destroy();
				g_ObjectDataPool.Destroy();
			}
	}
}