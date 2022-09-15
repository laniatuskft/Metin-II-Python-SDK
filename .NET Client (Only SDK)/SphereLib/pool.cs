//# Laniatus Games Studio Inc. | WARN: The original C++ template specifier was replaced with a C# generic specifier, which may not produce the same behavior:
//Original Metin2 CPlus Line: template <class Type>
public class Pool <Type> : System.IDisposable
{
	public Pool()
	{
		mHead = null;
		mFree = null;
		mData = 0;
		mCurrent = null;
		mFreeCount = 0;
		mUsedCount = 0;
	}

	public void Dispose()
	{
		if (mData)
		{
			Arrays.DeleteArray(mData);
		}
	}


	public void Release()
	{
		if (mData)
		{
			mData = null;
		}

		mHead = null;
		mFree = null;

		mData = 0;
		mCurrent = null;
		mFreeCount = 0;
		mUsedCount = 0;
	}

	public void Set(int maxitems)
	{
		if (mData)
		{
			mData = null;
		}
		mMaxItems = maxitems;
		mData = Arrays.InitializeWithDefaultInstances<Type>(mMaxItems);
		mFree = mData;
		mHead = null;
		int loopValue = (mMaxItems - 1);
		for (int LaniatusDefVariables = 0; LaniatusDefVariables < loopValue; i++)
		{
			mData[i].SetNext(mData[i + 1]);
			if (i == 0)
			{
				mData[i].SetPrevious(0);
			}
			else
			{
				mData[i].SetPrevious(mData[i - 1]);
			}
		}

		mData[loopValue].SetNext(0);
		mData[loopValue].SetPrevious(mData[loopValue-1]);
		mCurrent = null;
		mFreeCount = maxitems;
		mUsedCount = 0;
	}


	public Type GetNext(ref bool looped)
	{

		looped = false;

		if (mHead == null)
		{
			return null;
		}
		Type ret;

		if (mCurrent == null)
		{
			ret = mHead;
			looped = true;
		}
		else
		{
			ret = mCurrent;
		}

		if (ret != null)
		{
			mCurrent = ret.GetNext();
		}


		return ret;
	}

//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: bool IsEmpty() const
	public bool IsEmpty()
	{
		if (mHead == null)
		{
			return true;
		}
		return false;
	}

	public int Begin()
	{
		mCurrent = mHead;
		return mUsedCount;
	}

//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: int GetUsedCount() const
	public int GetUsedCount()
	{
		return mUsedCount;
	}
//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: int GetFreeCount() const
	public int GetFreeCount()
	{
		return mFreeCount;
	}

	public Type GetNext()
	{
		if (mHead == null)
		{
			return null;
		}

		Type ret;

		if (mCurrent == null)
		{
			ret = mHead;
		}
		else
		{
			ret = mCurrent;
		}

		if (ret != null)
		{
			mCurrent = ret.GetNext();
		}


		return ret;
	}

//# Laniatus Games Studio Inc. | TODO TASK: Pointer arithmetic is detected on the parameter 't', so pointers on this parameter are left unchanged:
	public void Release(Type * t)
	{

		if (t == mCurrent)
		{
			mCurrent = t.GetNext();
		}

		Type prev = t.GetPrevious();

		if (prev != null)
		{
			Type next = t.GetNext();
			prev.SetNext(next);
			if (next != null)
			{
				next.SetPrevious(prev);
			}
		}
		else
		{
			Type next = t.GetNext();
			mHead = next;
			if (mHead != null)
			{
				mHead.SetPrevious(0);
			}
		}

		Type temp = mFree;
		mFree = t;
		t.SetPrevious(0);
		t.SetNext(temp);

		mUsedCount--;
		mFreeCount++;
	}

	public Type GetFreeNoLink()
	{
		if (mFree == null)
		{
			return null;
		}
		Type ret = mFree;
		mFree = ret.GetNext();
		mUsedCount++;
		mFreeCount--;
		ret.SetNext(0);
		ret.SetPrevious(0);
		return ret;
	}

	public Type GetFreeLink()
	{
		if (mFree == null)
		{
			return null;
		}
		Type ret = mFree;
		mFree = ret.GetNext();
		Type temp = mHead;
		mHead = ret;
		if (temp != null)
		{
			temp.SetPrevious(ret);
		}
		mHead.SetNext(temp);
		mHead.SetPrevious(0);
		mUsedCount++;
		mFreeCount--;
		return ret;
	}

	public void AddAfter(Type e, Type item)
	{
		if (e != null)
		{
			Type eprev = e.GetPrevious();
			Type enext = e.GetNext();
			e.SetNext(item);
			item.SetNext(enext);
			item.SetPrevious(e);
			if (enext != null)
			{
				enext.SetPrevious(item);
			}
		}
		else
		{
			mHead = item;
			item.SetPrevious(0);
			item.SetNext(0);
		}

	}

	public void AddBefore(Type e, Type item)
	{
		Type eprev = e.GetPrevious();
		Type enext = e.GetNext();

		if (eprev == null)
		{
			mHead = item;
		}
		else
		{
			eprev.SetNext(item);
		}

		item.SetPrevious(eprev);
		item.SetNext(e);

		e.SetPrevious(item);

	}


	private int mMaxItems;
	private Type mCurrent;
	private Type[] mData;
	private Type mHead;
	private Type mFree;
	private int mUsedCount;
	private int mFreeCount;
}
