namespace CActorInstance
{

	public class IEventHandler
	{
//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
		public CActorInstance.IEventHandler GetEmptyPtr()
		{
			CEmptyEventHandler s_kEmptyEventHandler = new CEmptyEventHandler();
        
			return new CEmptyEventHandler(s_kEmptyEventHandler);
		}
	}
}