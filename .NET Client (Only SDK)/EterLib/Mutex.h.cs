public class Mutex : System.IDisposable
{
	public Mutex()
	{
		InitializeCriticalSection(@lock);
	}
	public void Dispose()
	{
		DeleteCriticalSection(@lock);
	}

	public void Lock()
	{
		EnterCriticalSection(@lock);
	}
	public void Unlock()
	{
		LeaveCriticalSection(@lock);
	}
//# Laniatus Games Studio Inc. | TODO TASK: The implementation of the following method could not be found:
//		bool Trylock();

		private CRITICAL_SECTION @lock = new CRITICAL_SECTION();
}

