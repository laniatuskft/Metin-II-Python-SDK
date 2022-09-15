using System.Diagnostics;

//# Laniatus Games Studio Inc. | WARN: The original C++ template specifier was replaced with a C# generic specifier, which may not produce the same behavior:
//Original Metin2 CPlus Line: template<typename T>
public class CDynamic <T> : System.IDisposable
{
		public class FClear
		{
			public void functorMethod(CDynamic<T> rDynamic)
			{
				rDynamic.Clear();
			}
		}

		public CDynamic()
		{
			Initialize();
		}

		public void Dispose()
		{
			Clear();
		}

		public void Clear()
		{
			if (m_pObject != null)
			{
				ms_objectPool.Free(m_pObject);
			}

			Initialize();
		}

		public T GetUsablePointer()
		{
			if (m_pObject == null)
			{
				m_pObject = ms_objectPool.Alloc();
			}

			return m_pObject;
		}

//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: bool IsNull() const
		public bool IsNull()
		{
			if (m_pObject != null)
			{
				return false;
			}
			return true;
		}

//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: T* GetPointer() const
		public T GetPointer()
		{
			Debug.Assert(m_pObject != null);
			return m_pObject;
		}

//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: T* operator ->() const
		public T Dereference()
		{
			Debug.Assert(m_pObject != null);
			return m_pObject;
		}

		private T m_pObject;

		private void Initialize()
		{
			m_pObject = null;
		}

		private static CDynamicPool<T> ms_objectPool = new CDynamicPool<T>();
}

//# Laniatus Games Studio Inc. | WARN: The original C++ template specifier was replaced with a C# generic specifier, which may not produce the same behavior:
//Original Metin2 CPlus Line: template<typename T>