public class IAbstractChat : TAbstractSingleton<IAbstractChat>
{
		public IAbstractChat()
		{
		}
		public virtual void Dispose()
		{
		}

		public abstract void AppendChat(int iType, string c_szChat);
}