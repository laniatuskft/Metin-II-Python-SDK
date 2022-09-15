namespace CTsfUiLessMode
{

	public class CUIElementSink
	{
//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
		public STDAPI_(uint UnnamedParameter) AddRef()
		{
			return ++_cRef;
		}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
		public STDAPI_(uint UnnamedParameter) Release()
		{
			int cr = --_cRef;
        
			if (_cRef == 0)
			{
				this = null;
			}
        
			return cr;
		}
	}
}