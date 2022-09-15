using System.Diagnostics;

//# Laniatus Games Studio Inc. | WARN: The original C++ template specifier was replaced with a C# generic specifier, which may not produce the same behavior:
//Original Metin2 CPlus Line: template<typename T>
public class CRef <T> : System.IDisposable
{
		public class FClear
		{
			public void functorMethod(CRef<T> rRef)
			{
				rRef.Clear();
			}
		}

		public CRef()
		{
			this.m_pObject = null;
		}

		public CRef(CReferenceObject pObject)
		{
			m_pObject = null;
			Initialize(pObject);
		}

		public CRef(in CRef c_rRef)
		{
			m_pObject = null;
			Initialize(c_rRef.m_pObject);
		}

		public void Dispose()
		{
			Clear();
		}

//# Laniatus Games Studio Inc. |: This 'CopyFrom' method was converted from the original copy assignment operator:
//Original Metin2 CPlus Line: void operator = (CReferenceObject* pObject)
		public void CopyFrom (CReferenceObject pObject)
		{
			SetPointer(pObject);
		}

//# Laniatus Games Studio Inc. |: This 'CopyFrom' method was converted from the original copy assignment operator:
//Original Metin2 CPlus Line: void operator = (const CRef& c_rRef)
		public void CopyFrom (in CRef c_rRef)
		{
			SetPointer(c_rRef.m_pObject);
		}

		public void Clear()
		{
			if (m_pObject != null)
			{
				m_pObject.Release();
				m_pObject = null;
			}
		}

//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: bool IsNull() const
		public bool IsNull()
		{
			return m_pObject == null ? true : false;
		}

		public void SetPointer(CReferenceObject pObject)
		{
			CReferenceObject pOldObject = m_pObject;

			m_pObject = pObject;

			if (m_pObject != null)
			{
				m_pObject.AddReference();
			}

			if (pOldObject != null)
			{
				pOldObject.Release();
			}
		}

//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: T* GetPointer() const
		public T GetPointer()
		{
			return (T)m_pObject;
		}

//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: T* operator ->() const
		public T Dereference()
		{
			Debug.Assert(m_pObject != null);
			return (T)m_pObject;
		}

		private void Initialize(CReferenceObject pObject)
		{
			Debug.Assert(m_pObject == null);

			m_pObject = pObject;

			if (m_pObject != null)
			{
				m_pObject.AddReference();
			}
		}

		private CReferenceObject m_pObject;
}

