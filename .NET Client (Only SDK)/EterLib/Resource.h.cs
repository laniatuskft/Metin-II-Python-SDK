public abstract class CResource : CReferenceObject, System.IDisposable
{

		public enum EState
		{
			STATE_EMPTY,
			STATE_ERROR,
			STATE_EXIST,
			STATE_LOAD,
			STATE_FREE
		}

	public void Clear()
	{
		OnClear();
		me_state = STATE_EMPTY;
	}

	public CResource.TType StringToType(string c_szType)
	{
		return GetCRC32(c_szType, strlen(c_szType));
	}
	public CResource.TType Type()
	{
	//# Laniatus Games Studio Inc. |: This static local variable declaration (not allowed in C#) has been moved just prior to the method:
	//	static TType s_type = StringToType("CResource");
		return Type_s_type;
	}

	public void Load()
	{
		if (me_state != STATE_EMPTY)
		{
			return;
		}
    
	//# Laniatus Games Studio Inc. | TODO TASK: C# does not have an equivalent to pointers to value types:
	//Original Metin2 CPlus Line: const char * c_szFileName = GetFileName();
		char c_szFileName = GetFileName();
    
		uint dwStart = ELTimer_GetMSec();
		CMappedFile file = new CMappedFile();
		LPCVOID fileData = new LPCVOID();
    
		if (CEterPackManager.Instance().Get(file, c_szFileName, fileData))
		{
			m_dwLoadCostMiliiSecond = ELTimer_GetMSec() - dwStart;
    
			if (OnLoad(file.Size(), fileData))
			{
				me_state = STATE_EXIST;
			}
			else
			{
				Tracef("CResource::Load Error %s\n", c_szFileName);
				me_state = STATE_ERROR;
				return;
			}
		}
		else
		{
			if (OnLoad(0, null))
			{
				me_state = STATE_EXIST;
			}
			else
			{
				Tracef("CResource::Load file not exist %s\n", c_szFileName);
				me_state = STATE_ERROR;
			}
		}
	}
	public void Reload()
	{
		Clear();
		Tracef("CResource::Reload %s\n", GetFileName());
    
		CMappedFile file = new CMappedFile();
		LPCVOID fileData = new LPCVOID();
    
		if (CEterPackManager.Instance().Get(file, GetFileName(), fileData))
		{
			if (OnLoad(file.Size(), fileData))
			{
				me_state = STATE_EXIST;
			}
			else
			{
				me_state = STATE_ERROR;
				return;
			}
		}
		else
		{
			if (OnLoad(0, null))
			{
				me_state = STATE_EXIST;
			}
			else
			{
				me_state = STATE_ERROR;
			}
		}
	}
	public int ConvertPathName(string c_szPathName, char * pszRetPathName, int retLen)
	{
	//# Laniatus Games Studio Inc. | TODO TASK: Pointer arithmetic is detected on this variable, so pointers on this variable are left unchanged:
		char * pc;
		int len = 0;
    
		for (pc = c_szPathName; * pc && len < retLen; ++pc, ++len)
		{
			if (*pc == '/')
			{
				*(pszRetPathName++) = '\\';
			}
			else
			{
				*(pszRetPathName++) = (char) korean_tolower(*pc);
			}
		}
    
		*pszRetPathName = '\0';
		return len;
	}

	public bool CreateDeviceObjects()
	{
		return true;
	}
	public void DestroyDeviceObjects()
	{
	}

	public CResource(string c_szFileName)
	{
		this.me_state = STATE_EMPTY;
		SetFileName(c_szFileName);
	}
	public void Dispose()
	{
	}

	public void SetDeleteImmediately(bool isSet)
	{
		ms_bDeleteImmediately = isSet;
	}

//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: bool IsData() const;
	public bool IsData()
	{
		return me_state != STATE_EMPTY;
	}
//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: bool IsEmpty() const;
	public bool IsEmpty()
	{
		return OnIsEmpty();
	}
	public bool IsType(TType type)
	{
		return OnIsType(type);
	}

		public uint GetLoadCostMilliSecond()
		{
			return m_dwLoadCostMiliiSecond;
		}
//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: const char * GetFileName() const
		public string GetFileName()
		{
			return m_stFileName;
		}
//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: const string& GetFileNameString() const
		public string GetFileNameString()
		{
			return m_stFileName;
		}

		public abstract bool OnLoad(int iSize, object c_pvBuf);

	public void SetFileName(string c_szFileName)
	{
		m_stFileName = c_szFileName;
	}

		protected abstract void OnClear();
//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: virtual bool OnIsEmpty() const = 0;
		protected abstract bool OnIsEmpty();
		protected abstract bool OnIsType(uint type);

	public void OnConstruct()
	{
		Load();
	}
	public void OnSelfDestruct()
	{
		if (ms_bDeleteImmediately)
		{
			Clear();
		}
		else
		{
			CResourceManager.Instance().ReserveDeletingResource(this);
		}
	}

		protected string m_stFileName = "";
		protected uint m_dwLoadCostMiliiSecond;
		protected EState me_state;

		protected static bool ms_bDeleteImmediately;
}
