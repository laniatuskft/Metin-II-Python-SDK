public abstract class IBackground : CSingleton<IBackground>, System.IDisposable
{
		public IBackground()
		{
		}
		public virtual void Dispose()
		{
		}

		public abstract bool IsBlock(int x, int y);
}