using System.Diagnostics;

//# Laniatus Games Studio Inc. | WARN: The original C++ template specifier was replaced with a C# generic specifier, which may not produce the same behavior:
//Original Metin2 CPlus Line: template <typename T>
public class CSingleton <T> : System.IDisposable
{
	private static T ms_singleton;

	public CSingleton()
	{
		Debug.Assert(!ms_singleton);
		int offset = (int)(T) 1 - (int)(Globals.CSingleton <T>)(T) 1;
		ms_singleton = (T)((int) this + offset);
	}

	public virtual void Dispose()
	{
		Debug.Assert(ms_singleton);
		ms_singleton = null;
	}

	public static T Instance()
	{
		Debug.Assert(ms_singleton);
		return (ms_singleton);
	}

	public static T InstancePtr()
	{
		return (ms_singleton);
	}

	public static T instance()
	{
		Debug.Assert(ms_singleton);
		return (ms_singleton);
	}
}

//# Laniatus Games Studio Inc. | WARN: The original C++ template specifier was replaced with a C# generic specifier, which may not produce the same behavior:
//Original Metin2 CPlus Line: template <typename T>
public class singleton <T> : System.IDisposable
{
	private static T ms_singleton;

	public singleton()
	{
		Debug.Assert(!ms_singleton);
		int offset = (int)(T) 1 - (int)(Globals.singleton <T>)(T) 1;
		ms_singleton = (T)((int) this + offset);
	}

	public virtual void Dispose()
	{
		Debug.Assert(ms_singleton);
		ms_singleton = null;
	}

	public static T Instance()
	{
		Debug.Assert(ms_singleton);
		return (ms_singleton);
	}

	public static T InstancePtr()
	{
		return (ms_singleton);
	}

	public static T instance()
	{
		Debug.Assert(ms_singleton);
		return (ms_singleton);
	}
}

//# Laniatus Games Studio Inc. | WARN: The original C++ template specifier was replaced with a C# generic specifier, which may not produce the same behavior:
//Original Metin2 CPlus Line: template <typename T>