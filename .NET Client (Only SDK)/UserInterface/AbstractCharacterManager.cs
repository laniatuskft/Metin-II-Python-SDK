//# Laniatus Games Studio Inc. |: C# has no need of forward class declarations:
//class CInstanceBase;

public class IAbstractCharacterManager : TAbstractSingleton<IAbstractCharacterManager>
{
		public IAbstractCharacterManager()
		{
		}
		public virtual void Dispose()
		{
		}

		public abstract void Destroy();
		public abstract CInstanceBase GetInstancePtr(uint dwVID);
}