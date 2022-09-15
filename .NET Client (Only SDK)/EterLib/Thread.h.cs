using System;

public abstract class CThread
{
	public CThread()
	{
		this.m_pArg = null;
		this.m_hThread = null;
		this.m_uThreadID = 0;
	}
	public int Create(object arg)
	{
		Arg(arg);
		m_hThread = (IntPtr) _beginthreadex(null, 0, EntryPoint, this, 0, m_uThreadID);
    
		if (!m_hThread)
		{
			return false ? 1 : 0;
		}
    
		SetThreadPriority(m_hThread, THREAD_PRIORITY_NORMAL);
		return true ? 1 : 0;
	}

//# Laniatus Games Studio Inc. |: CALLBACK is not available in C#:
//Original Metin2 CPlus Line: static uint CALLBACK EntryPoint(object* pThis);
	public uint EntryPoint(object pThis)
	{
		CThread pThread = (CThread) pThis;
		return pThread.Run(pThread.Arg());
	}

		protected abstract uint Setup();
		protected abstract uint Execute(object arg);

	public uint Run(object arg)
	{
		if (!Setup())
		{
			return 0;
		}
    
		return (Execute(arg));
	}

//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: object* Arg() const
		protected object Arg()
		{
			return m_pArg;
		}
		protected void Arg(object arg)
		{
			m_pArg = arg;
		}

		protected IntPtr m_hThread;

		private object m_pArg;
		private uint m_uThreadID;
}

