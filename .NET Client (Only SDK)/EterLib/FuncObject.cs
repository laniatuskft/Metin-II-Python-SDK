//# Laniatus Games Studio Inc. | WARN: The original C++ template specifier was replaced with a C# generic specifier, which may not produce the same behavior:
//Original Metin2 CPlus Line: template<typename T>
public class CFuncObject <T> : System.IDisposable
{
		public CFuncObject()
		{
			Clear();
		}

		public virtual void Dispose()
		{
		}

		public void Clear()
		{
			m_pSelfObject = null;
			m_pFuncObject = null;
		}

		private delegate void pFuncObjectDelegate();

		public void Set(T pSelfObject, pFuncObjectDelegate pFuncObject)
		{
			m_pSelfObject = pSelfObject;
			m_pFuncObject = pFuncObject;
		}

		public bool IsEmpty()
		{
			if (m_pSelfObject != null)
			{
				return false;
			}

			if (m_pFuncObject != null)
			{
				return false;
			}

			return true;
		}

		public void Run()
		{
			if (m_pSelfObject != null)
			{
				if (m_pFuncObject != null)
				{
					m_pFuncObject();
				}
			}
		}

		protected T m_pSelfObject;
		protected delegate void m_pFuncObjectDelegate();
		protected m_pFuncObjectDelegate m_pFuncObject;
}
