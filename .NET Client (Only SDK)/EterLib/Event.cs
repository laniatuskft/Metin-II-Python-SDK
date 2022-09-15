using System.Collections.Generic;

public abstract class IEvent : System.IDisposable
{
//# Laniatus Games Studio Inc. | TODO TASK: The implementation of the following method could not be found:
//		IEvent();
//# Laniatus Games Studio Inc. | TODO TASK: The implementation of the following method could not be found:
//		public void Dispose();

		public abstract void Run();

		public void SetStartTime(float fTime)
		{
			m_fStartTime = fTime;
		}
		public float GetStartTime()
		{
			return m_fStartTime;
		}

		protected float m_fStartTime;
}

public class CEventManager : CSingleton<CEventManager>, System.IDisposable
{
//# Laniatus Games Studio Inc. | TODO TASK: The implementation of the following method could not be found:
//		CEventManager();
		public virtual void Dispose()
		{
			Destroy();
		}

		public void Destroy()
		{
			while (!m_eventQueue.empty())
			{
				IEvent pEvent = m_eventQueue.top();
				m_eventQueue.pop();
				if (pEvent != null)
				{
					pEvent.Dispose();
				}
			}
		}

		public void Register(IEvent pEvent)
		{
			m_eventQueue.push(pEvent);
		}

		public void Update(float fCurrentTime)
		{
			while (!m_eventQueue.empty())
			{
				IEvent pEvent = m_eventQueue.top();

				if (pEvent.GetStartTime() < fCurrentTime)
				{
					break;
				}

				m_eventQueue.pop();
				float fTime = pEvent.GetStartTime();
				pEvent.Run();
				if (pEvent != null)
				{
					pEvent.Dispose();
				}
			}
		}

		protected class EventComparisonFunc
		{
//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: bool operator ()(IEvent * left, IEvent * right) const
			public bool functorMethod(IEvent left, IEvent right)
			{
				return left.GetStartTime() > right.GetStartTime();
			}
		}

		protected std::priority_queue<IEvent , List<IEvent >, EventComparisonFunc> m_eventQueue = new std::priority_queue<IEvent , List<IEvent >, EventComparisonFunc>();
}
