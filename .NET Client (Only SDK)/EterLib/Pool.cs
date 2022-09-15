using System.Collections.Generic;
using System.Diagnostics;

//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define CHECK_RETURN(flag, string) if (flag) { LogBox(string); return; }

//# Laniatus Games Studio Inc. | WARN: The original C++ template specifier was replaced with a C# generic specifier, which may not produce the same behavior:
//Original Metin2 CPlus Line: template<typename T>
public class CDynamicPool <T> : System.IDisposable
{
		public CDynamicPool()
		{
			m_uInitCapacity = 0;
			m_uUsedCapacity = 0;
		}
		public virtual void Dispose()
		{
			Debug.Assert(m_kVct_pkData.Count == 0);
		}

		public void SetName(string c_szName)
		{
		}

		public void Clear()
		{
			Destroy();
		}

		public void Destroy()
		{
			m_kVct_pkData.ForEach(Delete);
			m_kVct_pkData.Clear();
			m_kVct_pkFree.Clear();
		}

		public void Create(uint uCapacity)
		{
			m_uInitCapacity = uCapacity;
			m_kVct_pkData.Capacity = uCapacity;
			m_kVct_pkFree.Capacity = uCapacity;
		}
		public T Alloc()
		{
			if (m_kVct_pkFree.Count == 0)
			{
				T pkNewData = new default(T);
				m_kVct_pkData.Add(pkNewData);
				++m_uUsedCapacity;
				return pkNewData;
			}

			T pkFreeData = m_kVct_pkFree[m_kVct_pkFree.Count - 1];
			m_kVct_pkFree.RemoveAt(m_kVct_pkFree.Count - 1);
			return pkFreeData;
		}
		public void Free(T pkData)
		{
#if DYNAMIC_POOL_STRICT
			Debug.Assert(__IsValidData(pkData));
			Debug.Assert(!__IsFreeData(pkData));
#endif
			m_kVct_pkFree.Add(pkData);
		}
		public void FreeAll()
		{
			m_kVct_pkFree = new List<T>(m_kVct_pkData);
		}

		public uint GetCapacity()
		{
			return (uint)m_kVct_pkData.Count;
		}

		protected bool __IsValidData(T pkData)
		{
			if (m_kVct_pkData.end() == std::find(m_kVct_pkData.GetEnumerator(), m_kVct_pkData.end(), pkData))
			{
				return false;
			}
			return true;
		}
		protected bool __IsFreeData(T pkData)
		{
			if (m_kVct_pkFree.end() == std::find(m_kVct_pkFree.GetEnumerator(), m_kVct_pkFree.end(), pkData))
			{
				return false;
			}

			return true;
		}

		protected static void Delete(T pkData)
		{
			pkData = null;
		}

		protected List<T> m_kVct_pkData = new List<T>();
		protected List<T> m_kVct_pkFree = new List<T>();

		protected uint m_uInitCapacity;
		protected uint m_uUsedCapacity;
}


//# Laniatus Games Studio Inc. | WARN: The original C++ template specifier was replaced with a C# generic specifier, which may not produce the same behavior:
//Original Metin2 CPlus Line: template<typename T>
public class CDynamicPoolEx <T> : System.IDisposable
{
		public CDynamicPoolEx()
		{
			m_uInitCapacity = 0;
			m_uUsedCapacity = 0;
		}
		public virtual void Dispose()
		{
			Debug.Assert(m_kVct_pkFree.Count == m_kVct_pkData.Count);
			Destroy();

#if DEBUG
			string szText = new string(new char[256]);
			sprintf(szText, "--------------------------------------------------------------------- %s Pool Capacity %d\n", typeof(T).name(), m_uUsedCapacity);
			OutputDebugString(szText);
			printf(szText);
#endif
		}

		public void Clear()
		{
			Destroy();
		}

		public void Destroy()
		{
#if DEBUG
			if (m_kVct_pkData.Count > 0)
			{
				string szText = new string(new char[256]);
				sprintf(szText, "--------------------------------------------------------------------- %s Pool Destroy\n", typeof(T).name());
				OutputDebugString(szText);
				printf(szText);
			}
#endif
			m_kVct_pkData.ForEach(Delete);
			m_kVct_pkData.Clear();
			m_kVct_pkFree.Clear();
		}

		public void Create(uint uCapacity)
		{
			m_uInitCapacity = uCapacity;
			m_kVct_pkData.Capacity = uCapacity;
			m_kVct_pkFree.Capacity = uCapacity;
		}
		public T Alloc()
		{
			if (m_kVct_pkFree.Count == 0)
			{
				T pkNewData = New();
				m_kVct_pkData.Add(pkNewData);
				++m_uUsedCapacity;
				return pkNewData;
			}

			T pkFreeData = m_kVct_pkFree[m_kVct_pkFree.Count - 1];
			m_kVct_pkFree.RemoveAt(m_kVct_pkFree.Count - 1);
			return pkFreeData;
		}
		public void Free(T pkData)
		{
#if DYNAMIC_POOL_STRICT
			Debug.Assert(__IsValidData(pkData));
			Debug.Assert(!__IsFreeData(pkData));
#endif
			m_kVct_pkFree.Add(pkData);
		}
		public void FreeAll()
		{
			m_kVct_pkFree = new List<T>(m_kVct_pkData);
		}

		public uint GetCapacity()
		{
			return (uint)m_kVct_pkData.Count;
		}

		protected bool __IsValidData(T pkData)
		{
			if (m_kVct_pkData.end() == std::find(m_kVct_pkData.GetEnumerator(), m_kVct_pkData.end(), pkData))
			{
				return false;
			}
			return true;
		}
		protected bool __IsFreeData(T pkData)
		{
			if (m_kVct_pkFree.end() == std::find(m_kVct_pkFree.GetEnumerator(), m_kVct_pkFree.end(), pkData))
			{
				return false;
			}

			return true;
		}

		protected static T New()
		{
			return (T).operator new(sizeof(T));
		}
		protected static void Delete(T pkData)
		{
			global::operator delete = new global::operator(pkData);
		}

		protected List<T> m_kVct_pkData = new List<T>();
		protected List<T> m_kVct_pkFree = new List<T>();

		protected uint m_uInitCapacity;
		protected uint m_uUsedCapacity;

}

//# Laniatus Games Studio Inc. | WARN: The original C++ template specifier was replaced with a C# generic specifier, which may not produce the same behavior:
//Original Metin2 CPlus Line: template <class T>
public class CPooledObject <T> : System.IDisposable
{
		public CPooledObject()
		{
		}
		public virtual void Dispose()
		{
		}

//# Laniatus Games Studio Inc. | TODO TASK: The new operator cannot be overloaded in C#:
		public static object operator new(uint UnnamedParameter)
		{
			return ms_kPool.Alloc();
		}

//# Laniatus Games Studio Inc. | TODO TASK: The delete operator cannot be overloaded in C#:
		public static void operator delete(object pT)
		{
			ms_kPool.Free((T)pT);
		}


		public static void DestroySystem()
		{
			ms_kPool.Destroy();
		}

		public static void DeleteAll()
		{
			ms_kPool.FreeAll();
		}

		protected static CDynamicPoolEx<T> ms_kPool = new CDynamicPoolEx<T>();
}

//# Laniatus Games Studio Inc. | WARN: The original C++ template specifier was replaced with a C# generic specifier, which may not produce the same behavior:
//Original Metin2 CPlus Line: template <class T>