//# Laniatus Games Studio Inc. | TODO TASK: There is no equivalent to most C++ 'pragma' directives in C#:
//#pragma warning(disable:4710)
//# Laniatus Games Studio Inc. | TODO TASK: There is no equivalent to most C++ 'pragma' directives in C#:
//#pragma warning(disable:4786)
//# Laniatus Games Studio Inc. | TODO TASK: There is no equivalent to most C++ 'pragma' directives in C#:
//#pragma warning(disable:4244)

//# Laniatus Games Studio Inc. | TODO TASK: There is no equivalent to most C++ 'pragma' directives in C#:
//#pragma warning(disable:4018)
//# Laniatus Games Studio Inc. | TODO TASK: There is no equivalent to most C++ 'pragma' directives in C#:
//#pragma warning(disable:4245)
//# Laniatus Games Studio Inc. | TODO TASK: There is no equivalent to most C++ 'pragma' directives in C#:
//#pragma warning(disable:4512)
//# Laniatus Games Studio Inc. | TODO TASK: There is no equivalent to most C++ 'pragma' directives in C#:
//#pragma warning(disable:4201)

//# Laniatus Games Studio Inc. | TODO TASK: C# does not allow setting or comparing #define constants:
#if _MSC_VER >= 1400
//# Laniatus Games Studio Inc. | TODO TASK: There is no equivalent to most C++ 'pragma' directives in C#:
//#pragma warning(disable:4201 4512 4238 4239)
#endif




//# Laniatus Games Studio Inc. | TODO TASK: There is no equivalent to most C++ 'pragma' directives in C#:
//#pragma warning ( disable : 4201 )
//# Laniatus Games Studio Inc. | TODO TASK: There is no equivalent to most C++ 'pragma' directives in C#:
//#pragma warning ( default : 4201 )

//# Laniatus Games Studio Inc. | TODO TASK: There is no equivalent to most C++ 'pragma' directives in C#:
//#pragma comment(lib, "winmm.lib")
//# Laniatus Games Studio Inc. | TODO TASK: There is no equivalent to most C++ 'pragma' directives in C#:
//#pragma comment(lib, "d3d8.lib")
//# Laniatus Games Studio Inc. | TODO TASK: There is no equivalent to most C++ 'pragma' directives in C#:
//#pragma comment(lib, "d3dx8.lib")


//# Laniatus Games Studio Inc. | TODO TASK: There is no equivalent to most C++ 'pragma' directives in C#:
//#pragma warning(disable:4710)
//# Laniatus Games Studio Inc. | TODO TASK: There is no equivalent to most C++ 'pragma' directives in C#:
//#pragma warning(disable:4786)
//# Laniatus Games Studio Inc. | TODO TASK: There is no equivalent to most C++ 'pragma' directives in C#:
//#pragma warning(disable:4244)

//# Laniatus Games Studio Inc. | TODO TASK: There is no equivalent to most C++ 'pragma' directives in C#:
//#pragma warning ( disable : 4201 )
//# Laniatus Games Studio Inc. | TODO TASK: There is no equivalent to most C++ 'pragma' directives in C#:
//#pragma warning ( default : 4201 )

//# Laniatus Games Studio Inc. | TODO TASK: There is no equivalent to most C++ 'pragma' directives in C#:
//#pragma warning ( push, 3 )

//# Laniatus Games Studio Inc. | TODO TASK: There is no equivalent to most C++ 'pragma' directives in C#:
//#pragma warning ( pop )

//# Laniatus Games Studio Inc. | TODO TASK: C# does not allow setting or comparing #define constants:
#if _MSC_VER >= 1400
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define stricmp _stricmp
#define stricmp
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define strnicmp _strnicmp
#define strnicmp
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define strupt _strupr
#define strupt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define strcmpi _strcmpi
#define strcmpi
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define fileno _fileno
#define fileno
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define atoi _atoi64
#define atoi
#endif

#if ! NANOBEGIN
	#if __BORLANDC__
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define NANOBEGIN __emit__ (0xEB,0x03,0xD6,0xD7,0x01)
		#define NANOBEGIN
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define NANOEND __emit__ (0xEB,0x03,0xD6,0xD7,0x00)
		#define NANOEND
	#else
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define NANOBEGIN __asm _emit 0xEB __asm _emit 0x03 __asm _emit 0xD6 __asm _emit 0xD7 __asm _emit 0x01
		#define NANOBEGIN
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define NANOEND __asm _emit 0xEB __asm _emit 0x03 __asm _emit 0xD6 __asm _emit 0xD7 __asm _emit 0x00
		#define NANOEND
	#endif
#endif


//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define CHECK_RETURN(flag, string) if (flag) { LogBox(string); return; }
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define CP_THAI CP_874
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define CP_JAPANESE CP_932
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define CP_CHINESE_SIMPLE CP_936
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define CP_HANGUL CP_949
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define CP_CHINESE_TRAD CP_950
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define CP_EASTEUROPE CP_1250
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define CP_CYRILLIC CP_1251
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define CP_LATIN CP_1252
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define CP_GREEK CP_1253
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define CP_TURKISH CP_1254
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define CP_HEBREW CP_1255
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define CP_ARABIC CP_1256
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define CP_BALTIC CP_1257
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define CP_VIETNAMESE CP_1258

#if ! VC_EXTRALEAN
#endif


//# Laniatus Games Studio Inc. | TODO TASK: There is no equivalent to most C++ 'pragma' directives in C#:
//#pragma warning(disable:4786)


//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define SAFE_DELETE(p) { if (p) { delete (p); (p) = NULL; } }
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define SAFE_DELETE_ARRAY(p) { if (p) { delete[] (p); (p) = NULL; } }
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define SAFE_RELEASE(p) { if (p) { (p)->Release(); (p) = NULL; } }
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define SAFE_FREE_GLOBAL(p) { if (p) { ::GlobalFree(p); (p) = NULL; } }
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define SAFE_FREE_LIBRARY(p) { if (p) { ::FreeLibrary(p); (p) = NULL; } }
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define AssertLog(str) TraceError(str); assert(!str)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MAKEFOURCC(ch0, ch1, ch2, ch3) ((DWORD)(BYTE) (ch0 ) | ((DWORD)(BYTE) (ch1) << 8) | ((DWORD)(BYTE) (ch2) << 16) | ((DWORD)(BYTE) (ch3) << 24))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define IS_SET(flag,bit) ((flag) & (bit))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define SET_BIT(var,bit) ((var) |= (bit))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define REMOVE_BIT(var,bit) ((var) &= ~(bit))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define TOGGLE_BIT(var,bit) ((var) = (var) ^ (bit))

#if ! NANOBEGIN
	#if __BORLANDC__
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define NANOBEGIN __emit__ (0xEB,0x03,0xD6,0xD7,0x01)
		#define NANOBEGIN
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define NANOEND __emit__ (0xEB,0x03,0xD6,0xD7,0x00)
		#define NANOEND
	#else
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define NANOBEGIN __asm _emit 0xEB __asm _emit 0x03 __asm _emit 0xD6 __asm _emit 0xD7 __asm _emit 0x01
		#define NANOBEGIN
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define NANOEND __asm _emit 0xEB __asm _emit 0x03 __asm _emit 0xD6 __asm _emit 0xD7 __asm _emit 0x00
		#define NANOEND
	#endif
#endif


#if DEBUG
	#undef DEBUG
#define PY_RELEASE_LEVEL_ALPHA
#define PY_RELEASE_LEVEL_BETA
#define PY_RELEASE_LEVEL_GAMMA
#define PY_RELEASE_LEVEL_FINAL
#define PY_MAJOR_VERSION
#define PY_MINOR_VERSION
#define PY_MICRO_VERSION
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PY_RELEASE_LEVEL PY_RELEASE_LEVEL_FINAL
#define PY_RELEASE_LEVEL
#define PY_RELEASE_SERIAL
#define PY_VERSION
#define PY_PATCHLEVEL_REVISION
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PY_VERSION_HEX ((PY_MAJOR_VERSION << 24) | (PY_MINOR_VERSION << 16) | (PY_MICRO_VERSION << 8) | (PY_RELEASE_LEVEL << 4) | (PY_RELEASE_SERIAL << 0))
#define PY_VERSION_HEX
#define MS_WINCE
#define _CRT_SECURE_NO_DEPRECATE
#define _CRT_NONSTDC_NO_DEPRECATE
#define HAVE_IO_H
#define HAVE_SYS_UTIME_H
#define HAVE_TEMPNAM
#define HAVE_TMPFILE
#define HAVE_TMPNAM
#define HAVE_CLOCK
#define HAVE_STRERROR
#define HAVE_HYPOT
#define HAVE_STRFTIME
#define DONT_HAVE_SIG_ALARM
#define DONT_HAVE_SIG_PAUSE
#define LONG_BIT
#define WORD_BIT
#define PREFIX
#define EXEC_PREFIX
#define MS_WIN32 // only support win32 and greater.
#define MS_WINDOWS
#define NT_THREADS
#define WITH_THREAD
#define USE_SOCKET
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define strdup _strdup
#define strdup
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define getenv(v) (NULL)
#define getenv
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define environ (NULL)
#define environ
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Py_PASTE_VERSION(SUFFIX) ("[MSC v." _Py_STRINGIZE(_MSC_VER) " " SUFFIX "]")
#define _Py_PASTE_VERSION
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Py_STRINGIZE(X) _Py_STRINGIZE1((X))
#define _Py_STRINGIZE
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Py_STRINGIZE1(X) _Py_STRINGIZE2 ## X
#define _Py_STRINGIZE1
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Py_STRINGIZE2(X) #X
#define _Py_STRINGIZE2
#define MS_WIN64
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define COMPILER _Py_PASTE_VERSION("64 bit (Itanium)")
#define COMPILER
#define MS_WINI64
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define COMPILER _Py_PASTE_VERSION("64 bit (AMD64)")
#define COMPILER
#define MS_WINX64
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define COMPILER _Py_PASTE_VERSION("64 bit (Unknown)")
#define COMPILER
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_WINVER _WIN32_WINNT_WINXP
#define Py_WINVER
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_NTDDI NTDDI_WINXP
#define Py_NTDDI
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_WINVER _WIN32_WINNT_WIN2K
#define Py_WINVER
#define Py_WINVER
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_NTDDI NTDDI_WIN2KSP4
#define Py_NTDDI
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define NTDDI_VERSION Py_NTDDI
#define NTDDI_VERSION
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define WINVER Py_WINVER
#define WINVER
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _WIN32_WINNT Py_WINVER
#define _WIN32_WINNT
#define HAVE_SSIZE_T
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define COMPILER _Py_PASTE_VERSION("32 bit (Intel)")
#define COMPILER
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define COMPILER _Py_PASTE_VERSION("32 bit (Unknown)")
#define COMPILER
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_IS_NAN _isnan
#define Py_IS_NAN
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_IS_INFINITY(X) (!_finite(X) && !_isnan(X))
#define Py_IS_INFINITY
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_IS_FINITE(X) _finite(X)
#define Py_IS_FINITE
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define copysign _copysign
#define copysign
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define hypot _hypot
#define hypot
#define COMPILER
#define HAVE_UTIME_H
#define HAVE_DIRENT_H
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _chsize chsize
#define _chsize
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _setmode setmode
#define _setmode
#define COMPILER
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define hypot _hypot
#define hypot
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PY_LONG_LONG long long
#define PY_LONG_LONG
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PY_LLONG_MIN LLONG_MIN
#define PY_LLONG_MIN
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PY_LLONG_MAX LLONG_MAX
#define PY_LLONG_MAX
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PY_ULLONG_MAX ULLONG_MAX
#define PY_ULLONG_MAX
#define COMPILER
#define HAVE_LONG_LONG
#define HAVE_DECLSPEC_DLL
#define SIZEOF_SHORT
#define SIZEOF_INT
#define SIZEOF_LONG
#define SIZEOF_LONG_LONG
#define SIZEOF_DOUBLE
#define SIZEOF_FLOAT
#define HAVE_UINTPTR_T
#define HAVE_INTPTR_T
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_LL(x) x##I64
#define Py_LL
#define HAVE_UINT32_T
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PY_UINT32_T unsigned int
#define PY_UINT32_T
#define HAVE_UINT32_T
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PY_UINT32_T unsigned long
#define PY_UINT32_T
#define HAVE_UINT64_T
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PY_UINT64_T unsigned PY_LONG_LONG
#define PY_UINT64_T
#define HAVE_INT32_T
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PY_INT32_T int
#define PY_INT32_T
#define HAVE_INT32_T
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PY_INT32_T long
#define PY_INT32_T
#define HAVE_INT64_T
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PY_INT64_T PY_LONG_LONG
#define PY_INT64_T
#define HAVE_COPYSIGN
#define HAVE_DECL_ISINF
#define HAVE_DECL_ISNAN
#define HAVE_CONIO_H
#define HAVE_DIRECT_H
#define HAVE_TZNAME
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define RETSIGTYPE void
#define RETSIGTYPE
#define STDC_HEADERS
#define HAVE_PUTENV
#define HAVE_PROTOTYPES
#define WITH_DOC_STRINGS
#define Py_USING_UNICODE
#define Py_UNICODE_SIZE
#define WITH_PYMALLOC
#define HAVE_DYNAMIC_LOADING
#define HAVE_FTIME
#define HAVE_GETPEERNAME
#define HAVE_GETPID
#define HAVE_MKTIME
#define HAVE_SETVBUF
#define HAVE_WCSCOLL
#define HAVE_ZLIB_COPY
#define HAVE_ERRNO_H
#define HAVE_FCNTL_H
#define HAVE_PROCESS_H
#define HAVE_SIGNAL_H
#define HAVE_STDARG_PROTOTYPES
#define HAVE_STDDEF_H
#define HAVE_SYS_STAT_H
#define HAVE_SYS_TYPES_H
#define HAVE_WCHAR_H
#define HAVE_LIBNSL
#define HAVE_LIBSOCKET
#define Py_SOCKET_FD_CAN_BE_GE_FD_SETSIZE
#define DOUBLE_IS_LITTLE_ENDIAN_IEEE754
#define VA_LIST_IS_ARRAY
#define HAVE_LARGEFILE_SUPPORT
#define SIZEOF__BOOL
#define SIZEOF__BOOL
#define SIZEOF_LONG
#define SIZEOF_PTHREAD_T
#define SIZEOF_SIZE_T
#define SIZEOF_TIME_T
#define SIZEOF_VOID_P
#define SIZEOF_UINTPTR_T
#define SIZEOF_PTHREAD_T
#define SIZEOF__BOOL
#define SIZEOF__BOOL
#define SIZEOF_LONG
#define SIZEOF_PTHREAD_T
#define SIZEOF_SIZE_T
#define SIZEOF_TIME_T
#define SIZEOF_VOID_P
#define SIZEOF_UINTPTR_T
#define SIZEOF_PTHREAD_T
#define WORDS_BIGENDIAN
#define DOUBLE_IS_BIG_ENDIAN_IEEE754
#define DOUBLE_IS_LITTLE_ENDIAN_IEEE754
#define HAVE_GCC_ASM_FOR_X87
#define WITH_CYCLE_GC
#define _SGI_MP_SOURCE
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_PROTO(x) x
#define Py_PROTO
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_PROTO(x) ()
#define Py_PROTO
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_FPROTO(x) Py_PROTO(x)
#define Py_FPROTO
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PY_LONG_LONG long long
#define PY_LONG_LONG
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PY_LLONG_MIN LLONG_MIN
#define PY_LLONG_MIN
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PY_LLONG_MAX LLONG_MAX
#define PY_LLONG_MAX
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PY_ULLONG_MAX ULLONG_MAX
#define PY_ULLONG_MAX
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PY_LLONG_MAX __LONG_LONG_MAX__
#define PY_LLONG_MAX
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PY_LLONG_MIN (-PY_LLONG_MAX-1)
#define PY_LLONG_MIN
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PY_ULLONG_MAX (__LONG_LONG_MAX__*2ULL + 1ULL)
#define PY_ULLONG_MAX
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PY_ULLONG_MAX (~0ULL)
#define PY_ULLONG_MAX
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PY_LLONG_MAX ((long long)(PY_ULLONG_MAX>>1))
#define PY_LLONG_MAX
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PY_LLONG_MIN (-PY_LLONG_MAX-1)
#define PY_LLONG_MIN
#define HAVE_UINT32_T
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PY_UINT32_T uint32_t
#define PY_UINT32_T
#define HAVE_UINT64_T
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PY_UINT64_T uint64_t
#define PY_UINT64_T
#define HAVE_INT32_T
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PY_INT32_T int32_t
#define PY_INT32_T
#define HAVE_INT64_T
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PY_INT64_T int64_t
#define PY_INT64_T
#define PYLONG_BITS_IN_DIGIT
#define PYLONG_BITS_IN_DIGIT
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PY_SIZE_MAX SIZE_MAX
#define PY_SIZE_MAX
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PY_SIZE_MAX ((size_t)-1)
#define PY_SIZE_MAX
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PY_SSIZE_T_MAX ((Py_ssize_t)(((size_t)-1)>>1))
#define PY_SSIZE_T_MAX
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PY_SSIZE_T_MIN (-PY_SSIZE_T_MAX-1)
#define PY_SSIZE_T_MIN
#define PY_FORMAT_SIZE_T
#define PY_FORMAT_SIZE_T
#define PY_FORMAT_SIZE_T
#define PY_FORMAT_LONG_LONG
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_LOCAL(type) static type __fastcall
#define Py_LOCAL
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_LOCAL_INLINE(type) static __inline type __fastcall
#define Py_LOCAL_INLINE
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_LOCAL(type) static type
#define Py_LOCAL
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_LOCAL_INLINE(type) static inline type
#define Py_LOCAL_INLINE
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_LOCAL(type) static type
#define Py_LOCAL
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_LOCAL_INLINE(type) static type
#define Py_LOCAL_INLINE
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_MEMCPY(target, source, length) do { size_t i_, n_ = (length); char *t_ = (void*) (target); const char *s_ = (void*) (source); if (n_ >= 16) memcpy(t_, s_, n_); else for (i_ = 0; i_ < n_; i_++) t_[i_] = s_[i_]; } while (0)
#define Py_MEMCPY
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_MEMCPY memcpy
#define Py_MEMCPY
#define HAVE_STAT
#define HAVE_FSTAT
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __CRT_WARNING( _Number, _Description ) message("" __FILE__ "(" _CRT_STRINGIZE(__LINE__) ") : " "warning CRT" _CRT_STRINGIZE(_Number) ": " _CRT_STRINGIZE(_Description))
#define __CRT_WARNING
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _CRT_WARNING( _Id ) __CRT_WARNING( _CRTWRN_WNUMBER_##_Id, _CRTWRN_MESSAGE_##_Id )
#define _CRT_WARNING
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __CRT_WARNING_MANAGED( _Number, _Description ) [System::Obsolete("warning CRT" _CRT_STRINGIZE(_Number) ": " _CRT_STRINGIZE(_Description))]
#define __CRT_WARNING_MANAGED
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _CRT_WARNING_MANAGED( _Id ) __CRT_WARNING_MANAGED( _CRTWRN_WNUMBER_##_Id, _CRTWRN_MESSAGE_##_Id )
#define _CRT_WARNING_MANAGED
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _CRT_WARNING_MANAGED( _Id )
#define _CRT_WARNING_MANAGED
#define _CRTWRN_WNUMBER__VCCLRIT_DEPRECATED
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _CRTWRN_MESSAGE__VCCLRIT_DEPRECATED _vcclrit.h is deprecated
#define _CRTWRN_MESSAGE__VCCLRIT_DEPRECATED
#define _CRTWRN_WNUMBER__EXPLICIT_KEYWORD
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _CRTWRN_MESSAGE__EXPLICIT_KEYWORD 'explicit' keyword not recognized
#define _CRTWRN_MESSAGE__EXPLICIT_KEYWORD
#define _CRTWRN_WNUMBER__NO_32BIT_TIME_T
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _CRTWRN_MESSAGE__NO_32BIT_TIME_T _USE_32BIT_TIME_T ignored.You cannot use 32-bit time_t with _WIN64
#define _CRTWRN_MESSAGE__NO_32BIT_TIME_T
#define _CRTWRN_WNUMBER__NO_SPECIAL_TRANSFER
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _CRTWRN_MESSAGE__NO_SPECIAL_TRANSFER Special transfer of control routines not for this platform
#define _CRTWRN_MESSAGE__NO_SPECIAL_TRANSFER
#define _CRTWRN_WNUMBER__NO_ITERATOR_DEBUGGING
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _CRTWRN_MESSAGE__NO_ITERATOR_DEBUGGING Iterator debugging not supported in retail builds.\n Setting _HAS_ITERA##TOR_DEBUGGING=0
#define _CRTWRN_MESSAGE__NO_ITERATOR_DEBUGGING
#define _CRTWRN_WNUMBER__CLR_AND_STATIC_CPPLIB
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _CRTWRN_MESSAGE__CLR_AND_STATIC_CPPLIB STATIC CPPLIB is not supported while building with /clr or /clr:pure
#define _CRTWRN_MESSAGE__CLR_AND_STATIC_CPPLIB
#define _CRTWRN_WNUMBER_FLOATING_POINT_CONTROL_DEPRECATED
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _CRTWRN_MESSAGE_FLOATING_POINT_CONTROL_DEPRECATED Manipulation of the floating point control and status words is not reliable in managed code
#define _CRTWRN_MESSAGE_FLOATING_POINT_CONTROL_DEPRECATED
#define _INO_T_DEFINED
#define _DEV_T_DEFINED
#define _OFF_T_DEFINED
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __stat64 _stat64
#define __stat64
#define _STAT_DEFINED
#define _S_IFMT
#define _S_IFDIR
#define _S_IFCHR
#define _S_IFIFO
#define _S_IFREG
#define _S_IREAD
#define _S_IWRITE
#define _S_IEXEC
#define _WSTAT_DEFINED
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define S_IFMT _S_IFMT
#define S_IFMT
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define S_IFDIR _S_IFDIR
#define S_IFDIR
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define S_IFCHR _S_IFCHR
#define S_IFCHR
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define S_IFREG _S_IFREG
#define S_IFREG
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define S_IREAD _S_IREAD
#define S_IREAD
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define S_IWRITE _S_IWRITE
#define S_IWRITE
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define S_IEXEC _S_IEXEC
#define S_IEXEC
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define S_IFMT (S_IFDIR|S_IFCHR|S_IFREG)
#define S_IFMT
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define S_ISREG(x) (((x) & S_IFMT) == S_IFREG)
#define S_ISREG
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define S_ISDIR(x) (((x) & S_IFMT) == S_IFDIR)
#define S_ISDIR
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_ARITHMETIC_RIGHT_SHIFT(TYPE, I, J) ((I) < 0 ? -1-((-1-(I)) >> (J)) : (I) >> (J))
#define Py_ARITHMETIC_RIGHT_SHIFT
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_ARITHMETIC_RIGHT_SHIFT(TYPE, I, J) ((I) >> (J))
#define Py_ARITHMETIC_RIGHT_SHIFT
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_FORCE_EXPANSION(X) X
#define Py_FORCE_EXPANSION
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_SAFE_DOWNCAST(VALUE, WIDE, NARROW) (assert((WIDE)(NARROW)(VALUE) == (VALUE)), (NARROW)(VALUE))
#define Py_SAFE_DOWNCAST
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_SAFE_DOWNCAST(VALUE, WIDE, NARROW) (NARROW)(VALUE)
#define Py_SAFE_DOWNCAST
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Py_SET_EDOM_FOR_NAN(X) if (isnan(X)) errno = EDOM;
#define _Py_SET_EDOM_FOR_NAN
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Py_SET_EDOM_FOR_NAN(X) ;
#define _Py_SET_EDOM_FOR_NAN
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_SET_ERRNO_ON_MATH_ERROR(X) do { if (errno == 0) { if ((X) == Py_HUGE_VAL || (X) == -Py_HUGE_VAL) errno = ERANGE; else _Py_SET_EDOM_FOR_NAN(X) } } while(0)
#define Py_SET_ERRNO_ON_MATH_ERROR
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_SET_ERANGE_IF_OVERFLOW(X) Py_SET_ERRNO_ON_MATH_ERROR(X)
#define Py_SET_ERANGE_IF_OVERFLOW
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_ADJUST_ERANGE1(X) do { if (errno == 0) { if ((X) == Py_HUGE_VAL || (X) == -Py_HUGE_VAL) errno = ERANGE; } else if (errno == ERANGE && (X) == 0.0) errno = 0; } while(0)
#define Py_ADJUST_ERANGE1
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_ADJUST_ERANGE2(X, Y) do { if ((X) == Py_HUGE_VAL || (X) == -Py_HUGE_VAL || (Y) == Py_HUGE_VAL || (Y) == -Py_HUGE_VAL) { if (errno == 0) errno = ERANGE; } else if (errno == ERANGE) errno = 0; } while(0)
#define Py_ADJUST_ERANGE2
#define HAVE_PY_SET_53BIT_PRECISION
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Py_SET_53BIT_PRECISION_HEADER unsigned short old_387controlword, new_387controlword
#define _Py_SET_53BIT_PRECISION_HEADER
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Py_SET_53BIT_PRECISION_START do { old_387controlword = _Py_get_387controlword(); new_387controlword = (old_387controlword & ~0x0f00) | 0x0200; if (new_387controlword != old_387controlword) _Py_set_387controlword(new_387controlword); } while (0)
#define _Py_SET_53BIT_PRECISION_START
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Py_SET_53BIT_PRECISION_END if (new_387controlword != old_387controlword) _Py_set_387controlword(old_387controlword)
#define _Py_SET_53BIT_PRECISION_END
#define HAVE_PY_SET_53BIT_PRECISION
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Py_SET_53BIT_PRECISION_HEADER unsigned int old_387controlword, new_387controlword, out_387controlword
#define _Py_SET_53BIT_PRECISION_HEADER
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Py_SET_53BIT_PRECISION_START do { __control87_2(0, 0, &old_387controlword, NULL); new_387controlword = (old_387controlword & ~(_MCW_PC | _MCW_RC)) | (_PC_53 | _RC_NEAR); if (new_387controlword != old_387controlword) __control87_2(new_387controlword, _MCW_PC | _MCW_RC, &out_387controlword, NULL); } while (0)
#define _Py_SET_53BIT_PRECISION_START
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Py_SET_53BIT_PRECISION_END do { if (new_387controlword != old_387controlword) __control87_2(old_387controlword, _MCW_PC | _MCW_RC, &out_387controlword, NULL); } while (0)
#define _Py_SET_53BIT_PRECISION_END
#define _Py_SET_53BIT_PRECISION_HEADER
#define _Py_SET_53BIT_PRECISION_START
#define _Py_SET_53BIT_PRECISION_END
#define PY_NO_SHORT_FLOAT_REPR
#define PY_NO_SHORT_FLOAT_REPR
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_DEPRECATED(VERSION_UNUSED)
#define Py_DEPRECATED
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_DEPRECATED(VERSION_UNUSED)
#define Py_DEPRECATED
#define _PY_PORT_CTYPE_UTF8_ISSUE
#define _PY_PORT_CTYPE_UTF8_ISSUE
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define isalnum(c) iswalnum(btowc(c))
#define isalnum
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define isalpha(c) iswalpha(btowc(c))
#define isalpha
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define islower(c) iswlower(btowc(c))
#define islower
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define isspace(c) iswspace(btowc(c))
#define isspace
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define isupper(c) iswupper(btowc(c))
#define isupper
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define tolower(c) towlower(btowc(c))
#define tolower
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define toupper(c) towupper(btowc(c))
#define toupper
#define HAVE_DECLSPEC_DLL
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyAPI_FUNC(RTYPE) __declspec(dllexport) RTYPE
#define PyAPI_FUNC
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyAPI_DATA(RTYPE) extern __declspec(dllexport) RTYPE
#define PyAPI_DATA
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyMODINIT_FUNC __declspec(dllexport) void
#define PyMODINIT_FUNC
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyMODINIT_FUNC void
#define PyMODINIT_FUNC
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyAPI_FUNC(RTYPE) __declspec(dllimport) RTYPE
#define PyAPI_FUNC
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyAPI_DATA(RTYPE) extern __declspec(dllimport) RTYPE
#define PyAPI_DATA
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyMODINIT_FUNC extern "C" __declspec(dllexport) void
#define PyMODINIT_FUNC
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyMODINIT_FUNC __declspec(dllexport) void
#define PyMODINIT_FUNC
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyAPI_FUNC(RTYPE) RTYPE
#define PyAPI_FUNC
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyAPI_DATA(RTYPE) extern RTYPE
#define PyAPI_DATA
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyMODINIT_FUNC extern "C" void
#define PyMODINIT_FUNC
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyMODINIT_FUNC void
#define PyMODINIT_FUNC
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define DL_IMPORT(RTYPE) __declspec(dllexport) RTYPE
#define DL_IMPORT
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define DL_EXPORT(RTYPE) __declspec(dllexport) RTYPE
#define DL_EXPORT
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define DL_IMPORT(RTYPE) __declspec(dllimport) RTYPE
#define DL_IMPORT
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define DL_EXPORT(RTYPE) __declspec(dllexport) RTYPE
#define DL_EXPORT
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define DL_EXPORT(RTYPE) RTYPE
#define DL_EXPORT
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define DL_IMPORT(RTYPE) RTYPE
#define DL_IMPORT
#define INT_MAX
#define LONG_MAX
#define LONG_MAX
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LONG_MIN (-LONG_MAX-1)
#define LONG_MIN
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LONG_BIT (8 * SIZEOF_LONG)
#define LONG_BIT
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_GCC_ATTRIBUTE(x)
#define Py_GCC_ATTRIBUTE
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_GCC_ATTRIBUTE(x) __attribute__(x)
#define Py_GCC_ATTRIBUTE
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_FORMAT_PARSETUPLE(func,p1,p2)
#define Py_FORMAT_PARSETUPLE
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_FORMAT_PARSETUPLE(func,p1,p2)
#define Py_FORMAT_PARSETUPLE
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_ALIGNED(x)
#define Py_ALIGNED
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_ALIGNED(x)
#define Py_ALIGNED
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_LL(x) x##LL
#define Py_LL
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_ULL(x) Py_LL(x##U)
#define Py_ULL
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define DL_IMPORT(RTYPE) RTYPE
#define DL_IMPORT
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define DL_EXPORT(RTYPE) RTYPE
#define DL_EXPORT
#define PYMALLOC_DEBUG
#define Py_MATH_PIl
#define Py_MATH_PI
#define Py_MATH_El
#define Py_MATH_E
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_FORCE_DOUBLE(X) (_Py_force_double(X))
#define Py_FORCE_DOUBLE
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_FORCE_DOUBLE(X) (X)
#define Py_FORCE_DOUBLE
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_IS_NAN(X) isnan(X)
#define Py_IS_NAN
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_IS_NAN(X) ((X) != (X))
#define Py_IS_NAN
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_IS_INFINITY(X) isinf(X)
#define Py_IS_INFINITY
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_IS_INFINITY(X) ((X) && (Py_FORCE_DOUBLE(X)*0.5 == Py_FORCE_DOUBLE(X)))
#define Py_IS_INFINITY
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_IS_FINITE(X) isfinite(X)
#define Py_IS_FINITE
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_IS_FINITE(X) finite(X)
#define Py_IS_FINITE
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_IS_FINITE(X) (!Py_IS_INFINITY(X) && !Py_IS_NAN(X))
#define Py_IS_FINITE
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_HUGE_VAL HUGE_VAL
#define Py_HUGE_VAL
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_NAN (Py_HUGE_VAL * 0.)
#define Py_NAN
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_OVERFLOWED(X) isinf(X)
#define Py_OVERFLOWED
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_OVERFLOWED(X) ((X) != 0.0 && (errno == ERANGE || (X) == Py_HUGE_VAL || (X) == -Py_HUGE_VAL))
#define Py_OVERFLOWED
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyMem_MALLOC _PyMem_DebugMalloc
#define PyMem_MALLOC
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyMem_REALLOC _PyMem_DebugRealloc
#define PyMem_REALLOC
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyMem_FREE _PyMem_DebugFree
#define PyMem_FREE
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyMem_MALLOC(n) ((size_t)(n) > (size_t)PY_SSIZE_T_MAX ? NULL : malloc((n) ? (n) : 1))
#define PyMem_MALLOC
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyMem_REALLOC(p, n) ((size_t)(n) > (size_t)PY_SSIZE_T_MAX ? NULL : realloc((p), (n) ? (n) : 1))
#define PyMem_REALLOC
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyMem_FREE free
#define PyMem_FREE
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyMem_New(type, n) ( ((size_t)(n) > PY_SSIZE_T_MAX / sizeof(type)) ? NULL : ( (type *) PyMem_Malloc((n) * sizeof(type)) ) )
#define PyMem_New
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyMem_NEW(type, n) ( ((size_t)(n) > PY_SSIZE_T_MAX / sizeof(type)) ? NULL : ( (type *) PyMem_MALLOC((n) * sizeof(type)) ) )
#define PyMem_NEW
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyMem_Resize(p, type, n) ( (p) = ((size_t)(n) > PY_SSIZE_T_MAX / sizeof(type)) ? NULL : (type *) PyMem_Realloc((p), (n) * sizeof(type)) )
#define PyMem_Resize
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyMem_RESIZE(p, type, n) ( (p) = ((size_t)(n) > PY_SSIZE_T_MAX / sizeof(type)) ? NULL : (type *) PyMem_REALLOC((p), (n) * sizeof(type)) )
#define PyMem_RESIZE
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyMem_Del PyMem_Free
#define PyMem_Del
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyMem_DEL PyMem_FREE
#define PyMem_DEL
#define Py_TRACE_REFS
#define Py_REF_DEBUG
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _PyObject_HEAD_EXTRA struct _object *_ob_next; struct _object *_ob_prev;
#define _PyObject_HEAD_EXTRA
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _PyObject_EXTRA_INIT 0, 0,
#define _PyObject_EXTRA_INIT
#define _PyObject_HEAD_EXTRA
#define _PyObject_EXTRA_INIT
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyObject_HEAD _PyObject_HEAD_EXTRA Py_ssize_t ob_refcnt; struct _typeobject *ob_type;
#define PyObject_HEAD
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyObject_HEAD_INIT(type) _PyObject_EXTRA_INIT 1, type,
#define PyObject_HEAD_INIT
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyVarObject_HEAD_INIT(type, size) PyObject_HEAD_INIT(type) size,
#define PyVarObject_HEAD_INIT
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyObject_VAR_HEAD PyObject_HEAD Py_ssize_t ob_size;
#define PyObject_VAR_HEAD
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_INVALID_SIZE (Py_ssize_t)-1
#define Py_INVALID_SIZE
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_REFCNT(ob) (((PyObject*)(ob))->ob_refcnt)
#define Py_REFCNT
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_TYPE(ob) (((PyObject*)(ob))->ob_type)
#define Py_TYPE
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_SIZE(ob) (((PyVarObject*)(ob))->ob_size)
#define Py_SIZE
#define PyBUF_SIMPLE
#define PyBUF_WRITABLE
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyBUF_WRITEABLE PyBUF_WRITABLE
#define PyBUF_WRITEABLE
#define PyBUF_FORMAT
#define PyBUF_ND
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyBUF_STRIDES (0x0010 | PyBUF_ND)
#define PyBUF_STRIDES
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyBUF_C_CONTIGUOUS (0x0020 | PyBUF_STRIDES)
#define PyBUF_C_CONTIGUOUS
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyBUF_F_CONTIGUOUS (0x0040 | PyBUF_STRIDES)
#define PyBUF_F_CONTIGUOUS
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyBUF_ANY_CONTIGUOUS (0x0080 | PyBUF_STRIDES)
#define PyBUF_ANY_CONTIGUOUS
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyBUF_INDIRECT (0x0100 | PyBUF_STRIDES)
#define PyBUF_INDIRECT
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyBUF_CONTIG (PyBUF_ND | PyBUF_WRITABLE)
#define PyBUF_CONTIG
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyBUF_CONTIG_RO (PyBUF_ND)
#define PyBUF_CONTIG_RO
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyBUF_STRIDED (PyBUF_STRIDES | PyBUF_WRITABLE)
#define PyBUF_STRIDED
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyBUF_STRIDED_RO (PyBUF_STRIDES)
#define PyBUF_STRIDED_RO
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyBUF_RECORDS (PyBUF_STRIDES | PyBUF_WRITABLE | PyBUF_FORMAT)
#define PyBUF_RECORDS
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyBUF_RECORDS_RO (PyBUF_STRIDES | PyBUF_FORMAT)
#define PyBUF_RECORDS_RO
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyBUF_FULL (PyBUF_INDIRECT | PyBUF_WRITABLE | PyBUF_FORMAT)
#define PyBUF_FULL
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyBUF_FULL_RO (PyBUF_INDIRECT | PyBUF_FORMAT)
#define PyBUF_FULL_RO
#define PyBUF_READ
#define PyBUF_WRITE
#define PyBUF_SHADOW
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyHeapType_GET_MEMBERS(etype) ((PyMemberDef *)(((char *)etype) + Py_TYPE(etype)->tp_basicsize))
#define PyHeapType_GET_MEMBERS
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyObject_TypeCheck(ob, tp) (Py_TYPE(ob) == (tp) || PyType_IsSubtype(Py_TYPE(ob), (tp)))
#define PyObject_TypeCheck
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyType_Check(op) PyType_FastSubclass(Py_TYPE(op), Py_TPFLAGS_TYPE_SUBCLASS)
#define PyType_Check
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyType_CheckExact(op) (Py_TYPE(op) == &PyType_Type)
#define PyType_CheckExact
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyObject_Bytes PyObject_Str
#define PyObject_Bytes
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyObject_REPR(obj) PyString_AS_STRING(PyObject_Repr(obj))
#define PyObject_REPR
#define Py_PRINT_RAW
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_TPFLAGS_HAVE_GETCHARBUFFER (1L<<0)
#define Py_TPFLAGS_HAVE_GETCHARBUFFER
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_TPFLAGS_HAVE_SEQUENCE_IN (1L<<1)
#define Py_TPFLAGS_HAVE_SEQUENCE_IN
#define Py_TPFLAGS_GC
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_TPFLAGS_HAVE_INPLACEOPS (1L<<3)
#define Py_TPFLAGS_HAVE_INPLACEOPS
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_TPFLAGS_CHECKTYPES (1L<<4)
#define Py_TPFLAGS_CHECKTYPES
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_TPFLAGS_HAVE_RICHCOMPARE (1L<<5)
#define Py_TPFLAGS_HAVE_RICHCOMPARE
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_TPFLAGS_HAVE_WEAKREFS (1L<<6)
#define Py_TPFLAGS_HAVE_WEAKREFS
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_TPFLAGS_HAVE_ITER (1L<<7)
#define Py_TPFLAGS_HAVE_ITER
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_TPFLAGS_HAVE_CLASS (1L<<8)
#define Py_TPFLAGS_HAVE_CLASS
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_TPFLAGS_HEAPTYPE (1L<<9)
#define Py_TPFLAGS_HEAPTYPE
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_TPFLAGS_BASETYPE (1L<<10)
#define Py_TPFLAGS_BASETYPE
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_TPFLAGS_READY (1L<<12)
#define Py_TPFLAGS_READY
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_TPFLAGS_READYING (1L<<13)
#define Py_TPFLAGS_READYING
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_TPFLAGS_HAVE_GC (1L<<14)
#define Py_TPFLAGS_HAVE_GC
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_TPFLAGS_HAVE_STACKLESS_EXTENSION (3L<<15)
#define Py_TPFLAGS_HAVE_STACKLESS_EXTENSION
#define Py_TPFLAGS_HAVE_STACKLESS_EXTENSION
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_TPFLAGS_HAVE_INDEX (1L<<17)
#define Py_TPFLAGS_HAVE_INDEX
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_TPFLAGS_HAVE_VERSION_TAG (1L<<18)
#define Py_TPFLAGS_HAVE_VERSION_TAG
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_TPFLAGS_VALID_VERSION_TAG (1L<<19)
#define Py_TPFLAGS_VALID_VERSION_TAG
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_TPFLAGS_IS_ABSTRACT (1L<<20)
#define Py_TPFLAGS_IS_ABSTRACT
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_TPFLAGS_HAVE_NEWBUFFER (1L<<21)
#define Py_TPFLAGS_HAVE_NEWBUFFER
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_TPFLAGS_INT_SUBCLASS (1L<<23)
#define Py_TPFLAGS_INT_SUBCLASS
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_TPFLAGS_LONG_SUBCLASS (1L<<24)
#define Py_TPFLAGS_LONG_SUBCLASS
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_TPFLAGS_LIST_SUBCLASS (1L<<25)
#define Py_TPFLAGS_LIST_SUBCLASS
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_TPFLAGS_TUPLE_SUBCLASS (1L<<26)
#define Py_TPFLAGS_TUPLE_SUBCLASS
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_TPFLAGS_STRING_SUBCLASS (1L<<27)
#define Py_TPFLAGS_STRING_SUBCLASS
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_TPFLAGS_UNICODE_SUBCLASS (1L<<28)
#define Py_TPFLAGS_UNICODE_SUBCLASS
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_TPFLAGS_DICT_SUBCLASS (1L<<29)
#define Py_TPFLAGS_DICT_SUBCLASS
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_TPFLAGS_BASE_EXC_SUBCLASS (1L<<30)
#define Py_TPFLAGS_BASE_EXC_SUBCLASS
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_TPFLAGS_TYPE_SUBCLASS (1L<<31)
#define Py_TPFLAGS_TYPE_SUBCLASS
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_TPFLAGS_DEFAULT_EXTERNAL ( Py_TPFLAGS_HAVE_GETCHARBUFFER | Py_TPFLAGS_HAVE_SEQUENCE_IN | Py_TPFLAGS_HAVE_INPLACEOPS | Py_TPFLAGS_HAVE_RICHCOMPARE | Py_TPFLAGS_HAVE_WEAKREFS | Py_TPFLAGS_HAVE_ITER | Py_TPFLAGS_HAVE_CLASS | Py_TPFLAGS_HAVE_STACKLESS_EXTENSION | Py_TPFLAGS_HAVE_INDEX | 0)
#define Py_TPFLAGS_DEFAULT_EXTERNAL
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_TPFLAGS_DEFAULT_CORE (Py_TPFLAGS_DEFAULT_EXTERNAL | Py_TPFLAGS_HAVE_VERSION_TAG)
#define Py_TPFLAGS_DEFAULT_CORE
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_TPFLAGS_DEFAULT Py_TPFLAGS_DEFAULT_CORE
#define Py_TPFLAGS_DEFAULT
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_TPFLAGS_DEFAULT Py_TPFLAGS_DEFAULT_EXTERNAL
#define Py_TPFLAGS_DEFAULT
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyType_HasFeature(t,f) (((t)->tp_flags & (f)) != 0)
#define PyType_HasFeature
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyType_FastSubclass(t,f) PyType_HasFeature(t,f)
#define PyType_FastSubclass
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Py_INC_REFTOTAL _Py_RefTotal++
#define _Py_INC_REFTOTAL
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Py_DEC_REFTOTAL _Py_RefTotal--
#define _Py_DEC_REFTOTAL
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Py_REF_DEBUG_COMMA ,
#define _Py_REF_DEBUG_COMMA
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Py_CHECK_REFCNT(OP) { if (((PyObject*)OP)->ob_refcnt < 0) _Py_NegativeRefcount(__FILE__, __LINE__, (PyObject *)(OP)); }
#define _Py_CHECK_REFCNT
#define _Py_INC_REFTOTAL
#define _Py_DEC_REFTOTAL
#define _Py_REF_DEBUG_COMMA
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Py_CHECK_REFCNT(OP) ;
#define _Py_CHECK_REFCNT
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Py_INC_TPALLOCS(OP) inc_count(Py_TYPE(OP))
#define _Py_INC_TPALLOCS
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Py_INC_TPFREES(OP) dec_count(Py_TYPE(OP))
#define _Py_INC_TPFREES
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Py_DEC_TPFREES(OP) Py_TYPE(OP)->tp_frees--
#define _Py_DEC_TPFREES
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Py_COUNT_ALLOCS_COMMA ,
#define _Py_COUNT_ALLOCS_COMMA
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Py_INC_TPALLOCS(OP)
#define _Py_INC_TPALLOCS
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Py_INC_TPFREES(OP)
#define _Py_INC_TPFREES
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Py_DEC_TPFREES(OP)
#define _Py_DEC_TPFREES
#define _Py_COUNT_ALLOCS_COMMA
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Py_NewReference(op) ( _Py_INC_TPALLOCS(op) _Py_COUNT_ALLOCS_COMMA _Py_INC_REFTOTAL _Py_REF_DEBUG_COMMA Py_REFCNT(op) = 1)
#define _Py_NewReference
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Py_ForgetReference(op) _Py_INC_TPFREES(op)
#define _Py_ForgetReference
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Py_Dealloc(op) ( _Py_INC_TPFREES(op) _Py_COUNT_ALLOCS_COMMA (*Py_TYPE(op)->tp_dealloc)((PyObject *)(op)))
#define _Py_Dealloc
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_INCREF(op) ( _Py_INC_REFTOTAL _Py_REF_DEBUG_COMMA ((PyObject*)(op))->ob_refcnt++)
#define Py_INCREF
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_DECREF(op) do { if (_Py_DEC_REFTOTAL _Py_REF_DEBUG_COMMA --((PyObject*)(op))->ob_refcnt != 0) _Py_CHECK_REFCNT(op) else _Py_Dealloc((PyObject *)(op)); } while (0)
#define Py_DECREF
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_CLEAR(op) do { if (op) { PyObject *_py_tmp = (PyObject *)(op); (op) = NULL; Py_DECREF(_py_tmp); } } while (0)
#define Py_CLEAR
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_XINCREF(op) do { if ((op) == NULL) ; else Py_INCREF(op); } while (0)
#define Py_XINCREF
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_XDECREF(op) do { if ((op) == NULL) ; else Py_DECREF(op); } while (0)
#define Py_XDECREF
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_None (&_Py_NoneStruct)
#define Py_None
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_RETURN_NONE return Py_INCREF(Py_None), Py_None
#define Py_RETURN_NONE
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_NotImplemented (&_Py_NotImplementedStruct)
#define Py_NotImplemented
#define Py_LT
#define Py_LE
#define Py_EQ
#define Py_NE
#define Py_GT
#define Py_GE
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define staticforward static
#define staticforward
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define statichere static
#define statichere
#define PyTrash_UNWIND_LEVEL
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_TRASHCAN_SAFE_BEGIN(op) do { PyThreadState *_tstate = PyThreadState_GET(); if (!_tstate || _tstate->trash_delete_nesting < PyTrash_UNWIND_LEVEL) { if (_tstate) ++_tstate->trash_delete_nesting;
#define Py_TRASHCAN_SAFE_BEGIN
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_TRASHCAN_SAFE_END(op) if (_tstate) { --_tstate->trash_delete_nesting; if (_tstate->trash_delete_later && _tstate->trash_delete_nesting <= 0) _PyTrash_thread_destroy_chain(); } } else _PyTrash_thread_deposit_object((PyObject*)op); } while (0);
#define Py_TRASHCAN_SAFE_END
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyObject_MALLOC _PyObject_DebugMalloc
#define PyObject_MALLOC
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyObject_Malloc _PyObject_DebugMalloc
#define PyObject_Malloc
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyObject_REALLOC _PyObject_DebugRealloc
#define PyObject_REALLOC
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyObject_Realloc _PyObject_DebugRealloc
#define PyObject_Realloc
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyObject_FREE _PyObject_DebugFree
#define PyObject_FREE
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyObject_Free _PyObject_DebugFree
#define PyObject_Free
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyObject_MALLOC PyObject_Malloc
#define PyObject_MALLOC
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyObject_REALLOC PyObject_Realloc
#define PyObject_REALLOC
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyObject_FREE PyObject_Free
#define PyObject_FREE
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyObject_MALLOC PyMem_MALLOC
#define PyObject_MALLOC
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyObject_REALLOC PyMem_REALLOC
#define PyObject_REALLOC
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyObject_FREE PyMem_FREE
#define PyObject_FREE
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyObject_Del PyObject_Free
#define PyObject_Del
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyObject_DEL PyObject_FREE
#define PyObject_DEL
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _PyObject_Del PyObject_Free
#define _PyObject_Del
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyObject_New(type, typeobj) ( (type *) _PyObject_New(typeobj) )
#define PyObject_New
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyObject_NewVar(type, typeobj, n) ( (type *) _PyObject_NewVar((typeobj), (n)) )
#define PyObject_NewVar
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyObject_INIT(op, typeobj) ( Py_TYPE(op) = (typeobj), _Py_NewReference((PyObject *)(op)), (op) )
#define PyObject_INIT
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyObject_INIT_VAR(op, typeobj, size) ( Py_SIZE(op) = (size), PyObject_INIT((op), (typeobj)) )
#define PyObject_INIT_VAR
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _PyObject_SIZE(typeobj) ( (typeobj)->tp_basicsize )
#define _PyObject_SIZE
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _PyObject_VAR_SIZE(typeobj, nitems) (size_t) ( ( (typeobj)->tp_basicsize + (nitems)*(typeobj)->tp_itemsize + (SIZEOF_VOID_P - 1) ) & ~(SIZEOF_VOID_P - 1) )
#define _PyObject_VAR_SIZE
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyObject_NEW(type, typeobj) ( (type *) PyObject_Init( (PyObject *) PyObject_MALLOC( _PyObject_SIZE(typeobj) ), (typeobj)) )
#define PyObject_NEW
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyObject_NEW_VAR(type, typeobj, n) ( (type *) PyObject_InitVar( (PyVarObject *) PyObject_MALLOC(_PyObject_VAR_SIZE((typeobj),(n)) ), (typeobj), (n)) )
#define PyObject_NEW_VAR
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyType_IS_GC(t) PyType_HasFeature((t), Py_TPFLAGS_HAVE_GC)
#define PyType_IS_GC
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyObject_IS_GC(o) (PyType_IS_GC(Py_TYPE(o)) && (Py_TYPE(o)->tp_is_gc == NULL || Py_TYPE(o)->tp_is_gc(o)))
#define PyObject_IS_GC
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyObject_GC_Resize(type, op, n) ( (type *) _PyObject_GC_Resize((PyVarObject *)(op), (n)) )
#define PyObject_GC_Resize
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _PyObject_GC_Del PyObject_GC_Del
#define _PyObject_GC_Del
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Py_AS_GC(o) ((PyGC_Head *)(o)-1)
#define _Py_AS_GC
#define _PyGC_REFS_UNTRACKED
#define _PyGC_REFS_REACHABLE
#define _PyGC_REFS_TENTATIVELY_UNREACHABLE
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _PyObject_GC_TRACK(o) do { PyGC_Head *g = _Py_AS_GC(o); if (g->gc.gc_refs != _PyGC_REFS_UNTRACKED) Py_FatalError("GC object already tracked"); g->gc.gc_refs = _PyGC_REFS_REACHABLE; g->gc.gc_next = _PyGC_generation0; g->gc.gc_prev = _PyGC_generation0->gc.gc_prev; g->gc.gc_prev->gc.gc_next = g; _PyGC_generation0->gc.gc_prev = g; } while (0);
#define _PyObject_GC_TRACK
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _PyObject_GC_UNTRACK(o) do { PyGC_Head *g = _Py_AS_GC(o); assert(g->gc.gc_refs != _PyGC_REFS_UNTRACKED); g->gc.gc_refs = _PyGC_REFS_UNTRACKED; g->gc.gc_prev->gc.gc_next = g->gc.gc_next; g->gc.gc_next->gc.gc_prev = g->gc.gc_prev; g->gc.gc_next = NULL; } while (0);
#define _PyObject_GC_UNTRACK
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _PyObject_GC_IS_TRACKED(o) ((_Py_AS_GC(o))->gc.gc_refs != _PyGC_REFS_UNTRACKED)
#define _PyObject_GC_IS_TRACKED
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _PyObject_GC_MAY_BE_TRACKED(obj) (PyObject_IS_GC(obj) && (!PyTuple_CheckExact(obj) || _PyObject_GC_IS_TRACKED(obj)))
#define _PyObject_GC_MAY_BE_TRACKED
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyObject_GC_New(type, typeobj) ( (type *) _PyObject_GC_New(typeobj) )
#define PyObject_GC_New
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyObject_GC_NewVar(type, typeobj, n) ( (type *) _PyObject_GC_NewVar((typeobj), (n)) )
#define PyObject_GC_NewVar
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_VISIT(op) do { if (op) { int vret = visit((PyObject *)(op), arg); if (vret) return vret; } } while (0)
#define Py_VISIT
#define PyGC_HEAD_SIZE
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyObject_GC_Init(op)
#define PyObject_GC_Init
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyObject_GC_Fini(op)
#define PyObject_GC_Fini
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyObject_AS_GC(op) (op)
#define PyObject_AS_GC
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyObject_FROM_GC(op) (op)
#define PyObject_FROM_GC
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyType_SUPPORTS_WEAKREFS(t) (PyType_HasFeature((t), Py_TPFLAGS_HAVE_WEAKREFS) && ((t)->tp_weaklistoffset > 0))
#define PyType_SUPPORTS_WEAKREFS
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyObject_GET_WEAKREFS_LISTPTR(o) ((PyObject **) (((char *) (o)) + Py_TYPE(o)->tp_weaklistoffset))
#define PyObject_GET_WEAKREFS_LISTPTR
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_GETENV(s) (Py_IgnoreEnvironmentFlag ? NULL : getenv(s))
#define Py_GETENV
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_Check(op) 0
#define PyUnicode_Check
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_CheckExact(op) 0
#define PyUnicode_CheckExact
#define Py_UNICODE_WIDE
#define HAVE_USABLE_WCHAR_T
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PY_UNICODE_TYPE wchar_t
#define PY_UNICODE_TYPE
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PY_UNICODE_TYPE Py_UCS4
#define PY_UNICODE_TYPE
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_AsASCIIString PyUnicodeUCS2_AsASCIIString
#define PyUnicode_AsASCIIString
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_AsCharmapString PyUnicodeUCS2_AsCharmapString
#define PyUnicode_AsCharmapString
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_AsEncodedObject PyUnicodeUCS2_AsEncodedObject
#define PyUnicode_AsEncodedObject
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_AsEncodedString PyUnicodeUCS2_AsEncodedString
#define PyUnicode_AsEncodedString
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_AsLatin1String PyUnicodeUCS2_AsLatin1String
#define PyUnicode_AsLatin1String
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_AsRawUnicodeEscapeString PyUnicodeUCS2_AsRawUnicodeEscapeString
#define PyUnicode_AsRawUnicodeEscapeString
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_AsUTF32String PyUnicodeUCS2_AsUTF32String
#define PyUnicode_AsUTF32String
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_AsUTF16String PyUnicodeUCS2_AsUTF16String
#define PyUnicode_AsUTF16String
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_AsUTF8String PyUnicodeUCS2_AsUTF8String
#define PyUnicode_AsUTF8String
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_AsUnicode PyUnicodeUCS2_AsUnicode
#define PyUnicode_AsUnicode
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_AsUnicodeEscapeString PyUnicodeUCS2_AsUnicodeEscapeString
#define PyUnicode_AsUnicodeEscapeString
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_AsWideChar PyUnicodeUCS2_AsWideChar
#define PyUnicode_AsWideChar
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_ClearFreeList PyUnicodeUCS2_ClearFreelist
#define PyUnicode_ClearFreeList
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_Compare PyUnicodeUCS2_Compare
#define PyUnicode_Compare
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_Concat PyUnicodeUCS2_Concat
#define PyUnicode_Concat
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_Contains PyUnicodeUCS2_Contains
#define PyUnicode_Contains
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_Count PyUnicodeUCS2_Count
#define PyUnicode_Count
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_Decode PyUnicodeUCS2_Decode
#define PyUnicode_Decode
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_DecodeASCII PyUnicodeUCS2_DecodeASCII
#define PyUnicode_DecodeASCII
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_DecodeCharmap PyUnicodeUCS2_DecodeCharmap
#define PyUnicode_DecodeCharmap
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_DecodeLatin1 PyUnicodeUCS2_DecodeLatin1
#define PyUnicode_DecodeLatin1
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_DecodeRawUnicodeEscape PyUnicodeUCS2_DecodeRawUnicodeEscape
#define PyUnicode_DecodeRawUnicodeEscape
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_DecodeUTF32 PyUnicodeUCS2_DecodeUTF32
#define PyUnicode_DecodeUTF32
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_DecodeUTF32Stateful PyUnicodeUCS2_DecodeUTF32Stateful
#define PyUnicode_DecodeUTF32Stateful
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_DecodeUTF16 PyUnicodeUCS2_DecodeUTF16
#define PyUnicode_DecodeUTF16
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_DecodeUTF16Stateful PyUnicodeUCS2_DecodeUTF16Stateful
#define PyUnicode_DecodeUTF16Stateful
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_DecodeUTF8 PyUnicodeUCS2_DecodeUTF8
#define PyUnicode_DecodeUTF8
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_DecodeUTF8Stateful PyUnicodeUCS2_DecodeUTF8Stateful
#define PyUnicode_DecodeUTF8Stateful
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_DecodeUnicodeEscape PyUnicodeUCS2_DecodeUnicodeEscape
#define PyUnicode_DecodeUnicodeEscape
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_Encode PyUnicodeUCS2_Encode
#define PyUnicode_Encode
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_EncodeASCII PyUnicodeUCS2_EncodeASCII
#define PyUnicode_EncodeASCII
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_EncodeCharmap PyUnicodeUCS2_EncodeCharmap
#define PyUnicode_EncodeCharmap
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_EncodeDecimal PyUnicodeUCS2_EncodeDecimal
#define PyUnicode_EncodeDecimal
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_EncodeLatin1 PyUnicodeUCS2_EncodeLatin1
#define PyUnicode_EncodeLatin1
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_EncodeRawUnicodeEscape PyUnicodeUCS2_EncodeRawUnicodeEscape
#define PyUnicode_EncodeRawUnicodeEscape
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_EncodeUTF32 PyUnicodeUCS2_EncodeUTF32
#define PyUnicode_EncodeUTF32
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_EncodeUTF16 PyUnicodeUCS2_EncodeUTF16
#define PyUnicode_EncodeUTF16
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_EncodeUTF8 PyUnicodeUCS2_EncodeUTF8
#define PyUnicode_EncodeUTF8
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_EncodeUnicodeEscape PyUnicodeUCS2_EncodeUnicodeEscape
#define PyUnicode_EncodeUnicodeEscape
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_Find PyUnicodeUCS2_Find
#define PyUnicode_Find
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_Format PyUnicodeUCS2_Format
#define PyUnicode_Format
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_FromEncodedObject PyUnicodeUCS2_FromEncodedObject
#define PyUnicode_FromEncodedObject
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_FromFormat PyUnicodeUCS2_FromFormat
#define PyUnicode_FromFormat
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_FromFormatV PyUnicodeUCS2_FromFormatV
#define PyUnicode_FromFormatV
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_FromObject PyUnicodeUCS2_FromObject
#define PyUnicode_FromObject
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_FromOrdinal PyUnicodeUCS2_FromOrdinal
#define PyUnicode_FromOrdinal
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_FromString PyUnicodeUCS2_FromString
#define PyUnicode_FromString
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_FromStringAndSize PyUnicodeUCS2_FromStringAndSize
#define PyUnicode_FromStringAndSize
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_FromUnicode PyUnicodeUCS2_FromUnicode
#define PyUnicode_FromUnicode
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_FromWideChar PyUnicodeUCS2_FromWideChar
#define PyUnicode_FromWideChar
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_GetDefaultEncoding PyUnicodeUCS2_GetDefaultEncoding
#define PyUnicode_GetDefaultEncoding
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_GetMax PyUnicodeUCS2_GetMax
#define PyUnicode_GetMax
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_GetSize PyUnicodeUCS2_GetSize
#define PyUnicode_GetSize
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_Join PyUnicodeUCS2_Join
#define PyUnicode_Join
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_Partition PyUnicodeUCS2_Partition
#define PyUnicode_Partition
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_RPartition PyUnicodeUCS2_RPartition
#define PyUnicode_RPartition
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_RSplit PyUnicodeUCS2_RSplit
#define PyUnicode_RSplit
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_Replace PyUnicodeUCS2_Replace
#define PyUnicode_Replace
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_Resize PyUnicodeUCS2_Resize
#define PyUnicode_Resize
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_RichCompare PyUnicodeUCS2_RichCompare
#define PyUnicode_RichCompare
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_SetDefaultEncoding PyUnicodeUCS2_SetDefaultEncoding
#define PyUnicode_SetDefaultEncoding
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_Split PyUnicodeUCS2_Split
#define PyUnicode_Split
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_Splitlines PyUnicodeUCS2_Splitlines
#define PyUnicode_Splitlines
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_Tailmatch PyUnicodeUCS2_Tailmatch
#define PyUnicode_Tailmatch
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_Translate PyUnicodeUCS2_Translate
#define PyUnicode_Translate
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_TranslateCharmap PyUnicodeUCS2_TranslateCharmap
#define PyUnicode_TranslateCharmap
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _PyUnicode_AsDefaultEncodedString _PyUnicodeUCS2_AsDefaultEncodedString
#define _PyUnicode_AsDefaultEncodedString
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _PyUnicode_Fini _PyUnicodeUCS2_Fini
#define _PyUnicode_Fini
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _PyUnicode_Init _PyUnicodeUCS2_Init
#define _PyUnicode_Init
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _PyUnicode_IsAlpha _PyUnicodeUCS2_IsAlpha
#define _PyUnicode_IsAlpha
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _PyUnicode_IsDecimalDigit _PyUnicodeUCS2_IsDecimalDigit
#define _PyUnicode_IsDecimalDigit
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _PyUnicode_IsDigit _PyUnicodeUCS2_IsDigit
#define _PyUnicode_IsDigit
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _PyUnicode_IsLinebreak _PyUnicodeUCS2_IsLinebreak
#define _PyUnicode_IsLinebreak
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _PyUnicode_IsLowercase _PyUnicodeUCS2_IsLowercase
#define _PyUnicode_IsLowercase
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _PyUnicode_IsNumeric _PyUnicodeUCS2_IsNumeric
#define _PyUnicode_IsNumeric
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _PyUnicode_IsTitlecase _PyUnicodeUCS2_IsTitlecase
#define _PyUnicode_IsTitlecase
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _PyUnicode_IsUppercase _PyUnicodeUCS2_IsUppercase
#define _PyUnicode_IsUppercase
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _PyUnicode_IsWhitespace _PyUnicodeUCS2_IsWhitespace
#define _PyUnicode_IsWhitespace
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _PyUnicode_ToDecimalDigit _PyUnicodeUCS2_ToDecimalDigit
#define _PyUnicode_ToDecimalDigit
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _PyUnicode_ToDigit _PyUnicodeUCS2_ToDigit
#define _PyUnicode_ToDigit
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _PyUnicode_ToLowercase _PyUnicodeUCS2_ToLowercase
#define _PyUnicode_ToLowercase
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _PyUnicode_ToNumeric _PyUnicodeUCS2_ToNumeric
#define _PyUnicode_ToNumeric
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _PyUnicode_ToTitlecase _PyUnicodeUCS2_ToTitlecase
#define _PyUnicode_ToTitlecase
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _PyUnicode_ToUppercase _PyUnicodeUCS2_ToUppercase
#define _PyUnicode_ToUppercase
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_AsASCIIString PyUnicodeUCS4_AsASCIIString
#define PyUnicode_AsASCIIString
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_AsCharmapString PyUnicodeUCS4_AsCharmapString
#define PyUnicode_AsCharmapString
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_AsEncodedObject PyUnicodeUCS4_AsEncodedObject
#define PyUnicode_AsEncodedObject
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_AsEncodedString PyUnicodeUCS4_AsEncodedString
#define PyUnicode_AsEncodedString
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_AsLatin1String PyUnicodeUCS4_AsLatin1String
#define PyUnicode_AsLatin1String
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_AsRawUnicodeEscapeString PyUnicodeUCS4_AsRawUnicodeEscapeString
#define PyUnicode_AsRawUnicodeEscapeString
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_AsUTF32String PyUnicodeUCS4_AsUTF32String
#define PyUnicode_AsUTF32String
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_AsUTF16String PyUnicodeUCS4_AsUTF16String
#define PyUnicode_AsUTF16String
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_AsUTF8String PyUnicodeUCS4_AsUTF8String
#define PyUnicode_AsUTF8String
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_AsUnicode PyUnicodeUCS4_AsUnicode
#define PyUnicode_AsUnicode
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_AsUnicodeEscapeString PyUnicodeUCS4_AsUnicodeEscapeString
#define PyUnicode_AsUnicodeEscapeString
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_AsWideChar PyUnicodeUCS4_AsWideChar
#define PyUnicode_AsWideChar
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_ClearFreeList PyUnicodeUCS4_ClearFreelist
#define PyUnicode_ClearFreeList
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_Compare PyUnicodeUCS4_Compare
#define PyUnicode_Compare
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_Concat PyUnicodeUCS4_Concat
#define PyUnicode_Concat
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_Contains PyUnicodeUCS4_Contains
#define PyUnicode_Contains
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_Count PyUnicodeUCS4_Count
#define PyUnicode_Count
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_Decode PyUnicodeUCS4_Decode
#define PyUnicode_Decode
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_DecodeASCII PyUnicodeUCS4_DecodeASCII
#define PyUnicode_DecodeASCII
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_DecodeCharmap PyUnicodeUCS4_DecodeCharmap
#define PyUnicode_DecodeCharmap
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_DecodeLatin1 PyUnicodeUCS4_DecodeLatin1
#define PyUnicode_DecodeLatin1
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_DecodeRawUnicodeEscape PyUnicodeUCS4_DecodeRawUnicodeEscape
#define PyUnicode_DecodeRawUnicodeEscape
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_DecodeUTF32 PyUnicodeUCS4_DecodeUTF32
#define PyUnicode_DecodeUTF32
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_DecodeUTF32Stateful PyUnicodeUCS4_DecodeUTF32Stateful
#define PyUnicode_DecodeUTF32Stateful
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_DecodeUTF16 PyUnicodeUCS4_DecodeUTF16
#define PyUnicode_DecodeUTF16
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_DecodeUTF16Stateful PyUnicodeUCS4_DecodeUTF16Stateful
#define PyUnicode_DecodeUTF16Stateful
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_DecodeUTF8 PyUnicodeUCS4_DecodeUTF8
#define PyUnicode_DecodeUTF8
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_DecodeUTF8Stateful PyUnicodeUCS4_DecodeUTF8Stateful
#define PyUnicode_DecodeUTF8Stateful
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_DecodeUnicodeEscape PyUnicodeUCS4_DecodeUnicodeEscape
#define PyUnicode_DecodeUnicodeEscape
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_Encode PyUnicodeUCS4_Encode
#define PyUnicode_Encode
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_EncodeASCII PyUnicodeUCS4_EncodeASCII
#define PyUnicode_EncodeASCII
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_EncodeCharmap PyUnicodeUCS4_EncodeCharmap
#define PyUnicode_EncodeCharmap
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_EncodeDecimal PyUnicodeUCS4_EncodeDecimal
#define PyUnicode_EncodeDecimal
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_EncodeLatin1 PyUnicodeUCS4_EncodeLatin1
#define PyUnicode_EncodeLatin1
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_EncodeRawUnicodeEscape PyUnicodeUCS4_EncodeRawUnicodeEscape
#define PyUnicode_EncodeRawUnicodeEscape
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_EncodeUTF32 PyUnicodeUCS4_EncodeUTF32
#define PyUnicode_EncodeUTF32
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_EncodeUTF16 PyUnicodeUCS4_EncodeUTF16
#define PyUnicode_EncodeUTF16
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_EncodeUTF8 PyUnicodeUCS4_EncodeUTF8
#define PyUnicode_EncodeUTF8
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_EncodeUnicodeEscape PyUnicodeUCS4_EncodeUnicodeEscape
#define PyUnicode_EncodeUnicodeEscape
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_Find PyUnicodeUCS4_Find
#define PyUnicode_Find
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_Format PyUnicodeUCS4_Format
#define PyUnicode_Format
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_FromEncodedObject PyUnicodeUCS4_FromEncodedObject
#define PyUnicode_FromEncodedObject
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_FromFormat PyUnicodeUCS4_FromFormat
#define PyUnicode_FromFormat
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_FromFormatV PyUnicodeUCS4_FromFormatV
#define PyUnicode_FromFormatV
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_FromObject PyUnicodeUCS4_FromObject
#define PyUnicode_FromObject
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_FromOrdinal PyUnicodeUCS4_FromOrdinal
#define PyUnicode_FromOrdinal
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_FromString PyUnicodeUCS4_FromString
#define PyUnicode_FromString
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_FromStringAndSize PyUnicodeUCS4_FromStringAndSize
#define PyUnicode_FromStringAndSize
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_FromUnicode PyUnicodeUCS4_FromUnicode
#define PyUnicode_FromUnicode
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_FromWideChar PyUnicodeUCS4_FromWideChar
#define PyUnicode_FromWideChar
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_GetDefaultEncoding PyUnicodeUCS4_GetDefaultEncoding
#define PyUnicode_GetDefaultEncoding
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_GetMax PyUnicodeUCS4_GetMax
#define PyUnicode_GetMax
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_GetSize PyUnicodeUCS4_GetSize
#define PyUnicode_GetSize
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_Join PyUnicodeUCS4_Join
#define PyUnicode_Join
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_Partition PyUnicodeUCS4_Partition
#define PyUnicode_Partition
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_RPartition PyUnicodeUCS4_RPartition
#define PyUnicode_RPartition
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_RSplit PyUnicodeUCS4_RSplit
#define PyUnicode_RSplit
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_Replace PyUnicodeUCS4_Replace
#define PyUnicode_Replace
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_Resize PyUnicodeUCS4_Resize
#define PyUnicode_Resize
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_RichCompare PyUnicodeUCS4_RichCompare
#define PyUnicode_RichCompare
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_SetDefaultEncoding PyUnicodeUCS4_SetDefaultEncoding
#define PyUnicode_SetDefaultEncoding
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_Split PyUnicodeUCS4_Split
#define PyUnicode_Split
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_Splitlines PyUnicodeUCS4_Splitlines
#define PyUnicode_Splitlines
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_Tailmatch PyUnicodeUCS4_Tailmatch
#define PyUnicode_Tailmatch
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_Translate PyUnicodeUCS4_Translate
#define PyUnicode_Translate
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_TranslateCharmap PyUnicodeUCS4_TranslateCharmap
#define PyUnicode_TranslateCharmap
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _PyUnicode_AsDefaultEncodedString _PyUnicodeUCS4_AsDefaultEncodedString
#define _PyUnicode_AsDefaultEncodedString
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _PyUnicode_Fini _PyUnicodeUCS4_Fini
#define _PyUnicode_Fini
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _PyUnicode_Init _PyUnicodeUCS4_Init
#define _PyUnicode_Init
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _PyUnicode_IsAlpha _PyUnicodeUCS4_IsAlpha
#define _PyUnicode_IsAlpha
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _PyUnicode_IsDecimalDigit _PyUnicodeUCS4_IsDecimalDigit
#define _PyUnicode_IsDecimalDigit
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _PyUnicode_IsDigit _PyUnicodeUCS4_IsDigit
#define _PyUnicode_IsDigit
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _PyUnicode_IsLinebreak _PyUnicodeUCS4_IsLinebreak
#define _PyUnicode_IsLinebreak
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _PyUnicode_IsLowercase _PyUnicodeUCS4_IsLowercase
#define _PyUnicode_IsLowercase
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _PyUnicode_IsNumeric _PyUnicodeUCS4_IsNumeric
#define _PyUnicode_IsNumeric
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _PyUnicode_IsTitlecase _PyUnicodeUCS4_IsTitlecase
#define _PyUnicode_IsTitlecase
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _PyUnicode_IsUppercase _PyUnicodeUCS4_IsUppercase
#define _PyUnicode_IsUppercase
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _PyUnicode_IsWhitespace _PyUnicodeUCS4_IsWhitespace
#define _PyUnicode_IsWhitespace
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _PyUnicode_ToDecimalDigit _PyUnicodeUCS4_ToDecimalDigit
#define _PyUnicode_ToDecimalDigit
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _PyUnicode_ToDigit _PyUnicodeUCS4_ToDigit
#define _PyUnicode_ToDigit
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _PyUnicode_ToLowercase _PyUnicodeUCS4_ToLowercase
#define _PyUnicode_ToLowercase
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _PyUnicode_ToNumeric _PyUnicodeUCS4_ToNumeric
#define _PyUnicode_ToNumeric
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _PyUnicode_ToTitlecase _PyUnicodeUCS4_ToTitlecase
#define _PyUnicode_ToTitlecase
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _PyUnicode_ToUppercase _PyUnicodeUCS4_ToUppercase
#define _PyUnicode_ToUppercase
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_UNICODE_ISSPACE(ch) iswspace(ch)
#define Py_UNICODE_ISSPACE
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_UNICODE_ISLOWER(ch) iswlower(ch)
#define Py_UNICODE_ISLOWER
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_UNICODE_ISUPPER(ch) iswupper(ch)
#define Py_UNICODE_ISUPPER
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_UNICODE_ISTITLE(ch) _PyUnicode_IsTitlecase(ch)
#define Py_UNICODE_ISTITLE
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_UNICODE_ISLINEBREAK(ch) _PyUnicode_IsLinebreak(ch)
#define Py_UNICODE_ISLINEBREAK
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_UNICODE_TOLOWER(ch) towlower(ch)
#define Py_UNICODE_TOLOWER
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_UNICODE_TOUPPER(ch) towupper(ch)
#define Py_UNICODE_TOUPPER
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_UNICODE_TOTITLE(ch) _PyUnicode_ToTitlecase(ch)
#define Py_UNICODE_TOTITLE
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_UNICODE_ISDECIMAL(ch) _PyUnicode_IsDecimalDigit(ch)
#define Py_UNICODE_ISDECIMAL
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_UNICODE_ISDIGIT(ch) _PyUnicode_IsDigit(ch)
#define Py_UNICODE_ISDIGIT
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_UNICODE_ISNUMERIC(ch) _PyUnicode_IsNumeric(ch)
#define Py_UNICODE_ISNUMERIC
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_UNICODE_TODECIMAL(ch) _PyUnicode_ToDecimalDigit(ch)
#define Py_UNICODE_TODECIMAL
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_UNICODE_TODIGIT(ch) _PyUnicode_ToDigit(ch)
#define Py_UNICODE_TODIGIT
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_UNICODE_TONUMERIC(ch) _PyUnicode_ToNumeric(ch)
#define Py_UNICODE_TONUMERIC
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_UNICODE_ISALPHA(ch) iswalpha(ch)
#define Py_UNICODE_ISALPHA
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_UNICODE_ISSPACE(ch) ((ch) < 128U ? _Py_ascii_whitespace[(ch)] : _PyUnicode_IsWhitespace(ch))
#define Py_UNICODE_ISSPACE
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_UNICODE_ISLOWER(ch) _PyUnicode_IsLowercase(ch)
#define Py_UNICODE_ISLOWER
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_UNICODE_ISUPPER(ch) _PyUnicode_IsUppercase(ch)
#define Py_UNICODE_ISUPPER
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_UNICODE_ISTITLE(ch) _PyUnicode_IsTitlecase(ch)
#define Py_UNICODE_ISTITLE
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_UNICODE_ISLINEBREAK(ch) _PyUnicode_IsLinebreak(ch)
#define Py_UNICODE_ISLINEBREAK
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_UNICODE_TOLOWER(ch) _PyUnicode_ToLowercase(ch)
#define Py_UNICODE_TOLOWER
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_UNICODE_TOUPPER(ch) _PyUnicode_ToUppercase(ch)
#define Py_UNICODE_TOUPPER
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_UNICODE_TOTITLE(ch) _PyUnicode_ToTitlecase(ch)
#define Py_UNICODE_TOTITLE
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_UNICODE_ISDECIMAL(ch) _PyUnicode_IsDecimalDigit(ch)
#define Py_UNICODE_ISDECIMAL
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_UNICODE_ISDIGIT(ch) _PyUnicode_IsDigit(ch)
#define Py_UNICODE_ISDIGIT
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_UNICODE_ISNUMERIC(ch) _PyUnicode_IsNumeric(ch)
#define Py_UNICODE_ISNUMERIC
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_UNICODE_TODECIMAL(ch) _PyUnicode_ToDecimalDigit(ch)
#define Py_UNICODE_TODECIMAL
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_UNICODE_TODIGIT(ch) _PyUnicode_ToDigit(ch)
#define Py_UNICODE_TODIGIT
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_UNICODE_TONUMERIC(ch) _PyUnicode_ToNumeric(ch)
#define Py_UNICODE_TONUMERIC
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_UNICODE_ISALPHA(ch) _PyUnicode_IsAlpha(ch)
#define Py_UNICODE_ISALPHA
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_UNICODE_ISALNUM(ch) (Py_UNICODE_ISALPHA(ch) || Py_UNICODE_ISDECIMAL(ch) || Py_UNICODE_ISDIGIT(ch) || Py_UNICODE_ISNUMERIC(ch))
#define Py_UNICODE_ISALNUM
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_UNICODE_COPY(target, source, length) Py_MEMCPY((target), (source), (length)*sizeof(Py_UNICODE))
#define Py_UNICODE_COPY
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_UNICODE_FILL(target, value, length) do {Py_ssize_t i_; Py_UNICODE *t_ = (target); Py_UNICODE v_ = (value); for (i_ = 0; i_ < (length); i_++) t_[i_] = v_; } while (0)
#define Py_UNICODE_FILL
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_UNICODE_MATCH(string, offset, substring) ((*((string)->str + (offset)) == *((substring)->str)) && ((*((string)->str + (offset) + (substring)->length-1) == *((substring)->str + (substring)->length-1))) && !memcmp((string)->str + (offset), (substring)->str, (substring)->length*sizeof(Py_UNICODE)))
#define Py_UNICODE_MATCH
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_Check(op) PyType_FastSubclass(Py_TYPE(op), Py_TPFLAGS_UNICODE_SUBCLASS)
#define PyUnicode_Check
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_CheckExact(op) (Py_TYPE(op) == &PyUnicode_Type)
#define PyUnicode_CheckExact
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_GET_SIZE(op) (((PyUnicodeObject *)(op))->length)
#define PyUnicode_GET_SIZE
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_GET_DATA_SIZE(op) (((PyUnicodeObject *)(op))->length * sizeof(Py_UNICODE))
#define PyUnicode_GET_DATA_SIZE
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_AS_UNICODE(op) (((PyUnicodeObject *)(op))->str)
#define PyUnicode_AS_UNICODE
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyUnicode_AS_DATA(op) ((const char *)((PyUnicodeObject *)(op))->str)
#define PyUnicode_AS_DATA
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_UNICODE_REPLACEMENT_CHARACTER ((Py_UNICODE) 0xFFFD)
#define Py_UNICODE_REPLACEMENT_CHARACTER
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyInt_Check(op) PyType_FastSubclass((op)->ob_type, Py_TPFLAGS_INT_SUBCLASS)
#define PyInt_Check
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyInt_CheckExact(op) ((op)->ob_type == &PyInt_Type)
#define PyInt_CheckExact
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyInt_AS_LONG(op) (((PyIntObject *)(op))->ob_ival)
#define PyInt_AS_LONG
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyBool_Check(x) (Py_TYPE(x) == &PyBool_Type)
#define PyBool_Check
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_False ((PyObject *) &_Py_ZeroStruct)
#define Py_False
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_True ((PyObject *) &_Py_TrueStruct)
#define Py_True
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_RETURN_TRUE return Py_INCREF(Py_True), Py_True
#define Py_RETURN_TRUE
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_RETURN_FALSE return Py_INCREF(Py_False), Py_False
#define Py_RETURN_FALSE
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyLong_Check(op) PyType_FastSubclass(Py_TYPE(op), Py_TPFLAGS_LONG_SUBCLASS)
#define PyLong_Check
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyLong_CheckExact(op) (Py_TYPE(op) == &PyLong_Type)
#define PyLong_CheckExact
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _PyLong_AsSsize_t PyLong_AsSsize_t
#define _PyLong_AsSsize_t
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _PyLong_FromSize_t PyLong_FromSize_t
#define _PyLong_FromSize_t
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _PyLong_FromSsize_t PyLong_FromSsize_t
#define _PyLong_FromSsize_t
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyFloat_Check(op) PyObject_TypeCheck(op, &PyFloat_Type)
#define PyFloat_Check
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyFloat_CheckExact(op) (Py_TYPE(op) == &PyFloat_Type)
#define PyFloat_CheckExact
#define PyFloat_STR_PRECISION
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_RETURN_NAN return PyFloat_FromDouble(Py_NAN)
#define Py_RETURN_NAN
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_RETURN_INF(sign) do if (copysign(1., sign) == 1.) { return PyFloat_FromDouble(Py_HUGE_VAL); } else { return PyFloat_FromDouble(-Py_HUGE_VAL); } while(0)
#define Py_RETURN_INF
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyFloat_AS_DOUBLE(op) (((PyFloatObject *)(op))->ob_fval)
#define PyFloat_AS_DOUBLE
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define c_sum _Py_c_sum
#define c_sum
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define c_diff _Py_c_diff
#define c_diff
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define c_neg _Py_c_neg
#define c_neg
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define c_prod _Py_c_prod
#define c_prod
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define c_quot _Py_c_quot
#define c_quot
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define c_pow _Py_c_pow
#define c_pow
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define c_abs _Py_c_abs
#define c_abs
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyComplex_Check(op) PyObject_TypeCheck(op, &PyComplex_Type)
#define PyComplex_Check
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyComplex_CheckExact(op) (Py_TYPE(op) == &PyComplex_Type)
#define PyComplex_CheckExact
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyRange_Check(op) (Py_TYPE(op) == &PyRange_Type)
#define PyRange_Check
#define SSTATE_NOT_INTERNED
#define SSTATE_INTERNED_MORTAL
#define SSTATE_INTERNED_IMMORTAL
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyString_Check(op) PyType_FastSubclass(Py_TYPE(op), Py_TPFLAGS_STRING_SUBCLASS)
#define PyString_Check
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyString_CheckExact(op) (Py_TYPE(op) == &PyString_Type)
#define PyString_CheckExact
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyString_CHECK_INTERNED(op) (((PyStringObject *)(op))->ob_sstate)
#define PyString_CHECK_INTERNED
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyString_AS_STRING(op) (((PyStringObject *)(op))->ob_sval)
#define PyString_AS_STRING
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyString_GET_SIZE(op) Py_SIZE(op)
#define PyString_GET_SIZE
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyMemoryView_Check(op) (Py_TYPE(op) == &PyMemoryView_Type)
#define PyMemoryView_Check
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyMemoryView_GET_BUFFER(op) (&((PyMemoryViewObject *)(op))->view)
#define PyMemoryView_GET_BUFFER
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyMemoryView_GET_BASE(op) (((PyMemoryViewObject *)(op))->view.obj)
#define PyMemoryView_GET_BASE
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyBuffer_Check(op) (Py_TYPE(op) == &PyBuffer_Type)
#define PyBuffer_Check
#define Py_END_OF_BUFFER
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyBytesObject PyStringObject
#define PyBytesObject
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyBytes_Type PyString_Type
#define PyBytes_Type
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyBytes_Check PyString_Check
#define PyBytes_Check
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyBytes_CheckExact PyString_CheckExact
#define PyBytes_CheckExact
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyBytes_CHECK_INTERNED PyString_CHECK_INTERNED
#define PyBytes_CHECK_INTERNED
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyBytes_AS_STRING PyString_AS_STRING
#define PyBytes_AS_STRING
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyBytes_GET_SIZE PyString_GET_SIZE
#define PyBytes_GET_SIZE
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_TPFLAGS_BYTES_SUBCLASS Py_TPFLAGS_STRING_SUBCLASS
#define Py_TPFLAGS_BYTES_SUBCLASS
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyBytes_FromStringAndSize PyString_FromStringAndSize
#define PyBytes_FromStringAndSize
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyBytes_FromString PyString_FromString
#define PyBytes_FromString
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyBytes_FromFormatV PyString_FromFormatV
#define PyBytes_FromFormatV
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyBytes_FromFormat PyString_FromFormat
#define PyBytes_FromFormat
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyBytes_Size PyString_Size
#define PyBytes_Size
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyBytes_AsString PyString_AsString
#define PyBytes_AsString
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyBytes_Repr PyString_Repr
#define PyBytes_Repr
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyBytes_Concat PyString_Concat
#define PyBytes_Concat
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyBytes_ConcatAndDel PyString_ConcatAndDel
#define PyBytes_ConcatAndDel
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _PyBytes_Resize _PyString_Resize
#define _PyBytes_Resize
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _PyBytes_Eq _PyString_Eq
#define _PyBytes_Eq
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyBytes_Format PyString_Format
#define PyBytes_Format
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _PyBytes_FormatLong _PyString_FormatLong
#define _PyBytes_FormatLong
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyBytes_DecodeEscape PyString_DecodeEscape
#define PyBytes_DecodeEscape
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _PyBytes_Join _PyString_Join
#define _PyBytes_Join
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyBytes_AsStringAndSize PyString_AsStringAndSize
#define PyBytes_AsStringAndSize
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _PyBytes_InsertThousandsGrouping _PyString_InsertThousandsGrouping
#define _PyBytes_InsertThousandsGrouping
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyByteArray_Check(self) PyObject_TypeCheck(self, &PyByteArray_Type)
#define PyByteArray_Check
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyByteArray_CheckExact(self) (Py_TYPE(self) == &PyByteArray_Type)
#define PyByteArray_CheckExact
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyByteArray_AS_STRING(self) (assert(PyByteArray_Check(self)), Py_SIZE(self) ? ((PyByteArrayObject *)(self))->ob_bytes : _PyByteArray_empty_string)
#define PyByteArray_AS_STRING
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyByteArray_GET_SIZE(self) (assert(PyByteArray_Check(self)),Py_SIZE(self))
#define PyByteArray_GET_SIZE
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyTuple_Check(op) PyType_FastSubclass(Py_TYPE(op), Py_TPFLAGS_TUPLE_SUBCLASS)
#define PyTuple_Check
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyTuple_CheckExact(op) (Py_TYPE(op) == &PyTuple_Type)
#define PyTuple_CheckExact
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyTuple_GET_ITEM(op, i) (((PyTupleObject *)(op))->ob_item[LaniatusDefVariables])
#define PyTuple_GET_ITEM
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyTuple_GET_SIZE(op) Py_SIZE(op)
#define PyTuple_GET_SIZE
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyTuple_SET_ITEM(op, i, v) (((PyTupleObject *)(op))->ob_item[LaniatusDefVariables] = v)
#define PyTuple_SET_ITEM
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyList_Check(op) PyType_FastSubclass(Py_TYPE(op), Py_TPFLAGS_LIST_SUBCLASS)
#define PyList_Check
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyList_CheckExact(op) (Py_TYPE(op) == &PyList_Type)
#define PyList_CheckExact
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyList_GET_ITEM(op, i) (((PyListObject *)(op))->ob_item[LaniatusDefVariables])
#define PyList_GET_ITEM
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyList_SET_ITEM(op, i, v) (((PyListObject *)(op))->ob_item[LaniatusDefVariables] = (v))
#define PyList_SET_ITEM
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyList_GET_SIZE(op) Py_SIZE(op)
#define PyList_GET_SIZE
#define PyDict_MINSIZE
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyDict_Check(op) PyType_FastSubclass(Py_TYPE(op), Py_TPFLAGS_DICT_SUBCLASS)
#define PyDict_Check
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyDict_CheckExact(op) (Py_TYPE(op) == &PyDict_Type)
#define PyDict_CheckExact
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyDictKeys_Check(op) (Py_TYPE(op) == &PyDictKeys_Type)
#define PyDictKeys_Check
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyDictItems_Check(op) (Py_TYPE(op) == &PyDictItems_Type)
#define PyDictItems_Check
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyDictValues_Check(op) (Py_TYPE(op) == &PyDictValues_Type)
#define PyDictValues_Check
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyDictViewSet_Check(op) (PyDictKeys_Check(op) || PyDictItems_Check(op))
#define PyDictViewSet_Check
#define PySet_MINSIZE
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyFrozenSet_CheckExact(ob) (Py_TYPE(ob) == &PyFrozenSet_Type)
#define PyFrozenSet_CheckExact
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyAnySet_CheckExact(ob) (Py_TYPE(ob) == &PySet_Type || Py_TYPE(ob) == &PyFrozenSet_Type)
#define PyAnySet_CheckExact
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyAnySet_Check(ob) (Py_TYPE(ob) == &PySet_Type || Py_TYPE(ob) == &PyFrozenSet_Type || PyType_IsSubtype(Py_TYPE(ob), &PySet_Type) || PyType_IsSubtype(Py_TYPE(ob), &PyFrozenSet_Type))
#define PyAnySet_Check
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PySet_Check(ob) (Py_TYPE(ob) == &PySet_Type || PyType_IsSubtype(Py_TYPE(ob), &PySet_Type))
#define PySet_Check
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyFrozenSet_Check(ob) (Py_TYPE(ob) == &PyFrozenSet_Type || PyType_IsSubtype(Py_TYPE(ob), &PyFrozenSet_Type))
#define PyFrozenSet_Check
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PySet_GET_SIZE(so) (((PySetObject *)(so))->used)
#define PySet_GET_SIZE
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyCFunction_Check(op) (Py_TYPE(op) == &PyCFunction_Type)
#define PyCFunction_Check
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyCFunction_GET_FUNCTION(func) (((PyCFunctionObject *)func) -> m_ml -> ml_meth)
#define PyCFunction_GET_FUNCTION
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyCFunction_GET_SELF(func) (((PyCFunctionObject *)func) -> m_self)
#define PyCFunction_GET_SELF
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyCFunction_GET_FLAGS(func) (((PyCFunctionObject *)func) -> m_ml -> ml_flags)
#define PyCFunction_GET_FLAGS
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyCFunction_New(ML, SELF) PyCFunction_NewEx((ML), (SELF), NULL)
#define PyCFunction_New
#define METH_OLDARGS
#define METH_VARARGS
#define METH_KEYWORDS
#define METH_NOARGS
#define METH_O
#define METH_CLASS
#define METH_STATIC
#define METH_COEXIST
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyModule_Check(op) PyObject_TypeCheck(op, &PyModule_Type)
#define PyModule_Check
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyModule_CheckExact(op) (Py_TYPE(op) == &PyModule_Type)
#define PyModule_CheckExact
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyFunction_Check(op) (Py_TYPE(op) == &PyFunction_Type)
#define PyFunction_Check
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyFunction_GET_CODE(func) (((PyFunctionObject *)func) -> func_code)
#define PyFunction_GET_CODE
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyFunction_GET_GLOBALS(func) (((PyFunctionObject *)func) -> func_globals)
#define PyFunction_GET_GLOBALS
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyFunction_GET_MODULE(func) (((PyFunctionObject *)func) -> func_module)
#define PyFunction_GET_MODULE
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyFunction_GET_DEFAULTS(func) (((PyFunctionObject *)func) -> func_defaults)
#define PyFunction_GET_DEFAULTS
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyFunction_GET_CLOSURE(func) (((PyFunctionObject *)func) -> func_closure)
#define PyFunction_GET_CLOSURE
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyClass_Check(op) ((op)->ob_type == &PyClass_Type)
#define PyClass_Check
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyInstance_Check(op) ((op)->ob_type == &PyInstance_Type)
#define PyInstance_Check
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyMethod_Check(op) ((op)->ob_type == &PyMethod_Type)
#define PyMethod_Check
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyMethod_GET_FUNCTION(meth) (((PyMethodObject *)meth) -> im_func)
#define PyMethod_GET_FUNCTION
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyMethod_GET_SELF(meth) (((PyMethodObject *)meth) -> im_self)
#define PyMethod_GET_SELF
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyMethod_GET_CLASS(meth) (((PyMethodObject *)meth) -> im_class)
#define PyMethod_GET_CLASS
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyFile_Check(op) PyObject_TypeCheck(op, &PyFile_Type)
#define PyFile_Check
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyFile_CheckExact(op) (Py_TYPE(op) == &PyFile_Type)
#define PyFile_CheckExact
#define PY_STDIOTEXTMODE
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _PyVerify_fd(fd) (_get_osfhandle(fd) >= 0)
#define _PyVerify_fd
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _PyVerify_fd(A) (1)
#define _PyVerify_fd // dummy
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _PyIsSelectable_fd(FD) (((FD) >= 0) && ((FD) < FD_SETSIZE))
 #define _PyIsSelectable_fd
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _PyIsSelectable_fd(FD) (1)
 #define _PyIsSelectable_fd
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyCObject_Check(op) (Py_TYPE(op) == &PyCObject_Type)
#define PyCObject_Check
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyCapsule_CheckExact(op) (Py_TYPE(op) == &PyCapsule_Type)
#define PyCapsule_CheckExact
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyTraceBack_Check(v) (Py_TYPE(v) == &PyTraceBack_Type)
#define PyTraceBack_Check
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_Ellipsis (&_Py_EllipsisObject)
#define Py_Ellipsis
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PySlice_Check(op) (Py_TYPE(op) == &PySlice_Type)
#define PySlice_Check
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyCell_Check(op) (Py_TYPE(op) == &PyCell_Type)
#define PyCell_Check
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyCell_GET(op) (((PyCellObject *)(op))->ob_ref)
#define PyCell_GET
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyCell_SET(op, v) (((PyCellObject *)(op))->ob_ref = v)
#define PyCell_SET
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PySeqIter_Check(op) (Py_TYPE(op) == &PySeqIter_Type)
#define PySeqIter_Check
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyCallIter_Check(op) (Py_TYPE(op) == &PyCallIter_Type)
#define PyCallIter_Check
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyGen_Check(op) PyObject_TypeCheck(op, &PyGen_Type)
#define PyGen_Check
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyGen_CheckExact(op) (Py_TYPE(op) == &PyGen_Type)
#define PyGen_CheckExact
#define PyWrapperFlag_KEYWORDS
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyDescr_COMMON PyObject_HEAD PyTypeObject *d_type; PyObject *d_name
#define PyDescr_COMMON
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyDescr_IsData(d) (Py_TYPE(d)->tp_descr_set != NULL)
#define PyDescr_IsData
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyErr_WarnPy3k(msg, stacklevel) (Py_Py3kWarningFlag ? PyErr_WarnEx(PyExc_DeprecationWarning, msg, stacklevel) : 0)
#define PyErr_WarnPy3k
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyErr_Warn(category, msg) PyErr_WarnEx(category, msg, 1)
#define PyErr_Warn
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyWeakref_CheckRef(op) PyObject_TypeCheck(op, &_PyWeakref_RefType)
#define PyWeakref_CheckRef
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyWeakref_CheckRefExact(op) (Py_TYPE(op) == &_PyWeakref_RefType)
#define PyWeakref_CheckRefExact
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyWeakref_CheckProxy(op) ((Py_TYPE(op) == &_PyWeakref_ProxyType) || (Py_TYPE(op) == &_PyWeakref_CallableProxyType))
#define PyWeakref_CheckProxy
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyWeakref_Check(op) (PyWeakref_CheckRef(op) || PyWeakref_CheckProxy(op))
#define PyWeakref_Check
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyWeakref_GET_OBJECT(ref) (Py_REFCNT(((PyWeakReference *)(ref))->wr_object) > 0 ? ((PyWeakReference *)(ref))->wr_object : Py_None)
#define PyWeakref_GET_OBJECT
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _PyErr_OCCURRED() PyErr_Occurred()
#define _PyErr_OCCURRED
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _PyErr_OCCURRED() (_PyThreadState_Current->curexc_type)
#define _PyErr_OCCURRED
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyExceptionClass_Check(x) (PyClass_Check((x)) || (PyType_Check((x)) && PyType_FastSubclass((PyTypeObject*)(x), Py_TPFLAGS_BASE_EXC_SUBCLASS)))
#define PyExceptionClass_Check
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyExceptionInstance_Check(x) (PyInstance_Check((x)) || PyType_FastSubclass((x)->ob_type, Py_TPFLAGS_BASE_EXC_SUBCLASS))
#define PyExceptionInstance_Check
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyExceptionClass_Name(x) (PyClass_Check((x)) ? PyString_AS_STRING(((PyClassObject*)(x))->cl_name) : (char *)(((PyTypeObject*)(x))->tp_name))
#define PyExceptionClass_Name
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyExceptionInstance_Class(x) ((PyInstance_Check((x)) ? (PyObject*)((PyInstanceObject*)(x))->in_class : (PyObject*)((x)->ob_type)))
#define PyExceptionInstance_Class
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyErr_BadInternalCall() _PyErr_BadInternalCall(__FILE__, __LINE__)
#define PyErr_BadInternalCall
#define HAVE_SNPRINTF
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define snprintf _snprintf
#define snprintf
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define vsnprintf _vsnprintf
#define vsnprintf
#define PyTrace_CALL
#define PyTrace_EXCEPTION
#define PyTrace_LINE
#define PyTrace_RETURN
#define PyTrace_C_CALL
#define PyTrace_C_EXCEPTION
#define PyTrace_C_RETURN
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyThreadState_GET() PyThreadState_Get()
#define PyThreadState_GET
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyThreadState_GET() (_PyThreadState_Current)
#define PyThreadState_GET
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyArg_Parse _PyArg_Parse_SizeT
#define PyArg_Parse
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyArg_ParseTuple _PyArg_ParseTuple_SizeT
#define PyArg_ParseTuple
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyArg_ParseTupleAndKeywords _PyArg_ParseTupleAndKeywords_SizeT
#define PyArg_ParseTupleAndKeywords
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyArg_VaParse _PyArg_VaParse_SizeT
#define PyArg_VaParse
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyArg_VaParseTupleAndKeywords _PyArg_VaParseTupleAndKeywords_SizeT
#define PyArg_VaParseTupleAndKeywords
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_BuildValue _Py_BuildValue_SizeT
#define Py_BuildValue
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_VaBuildValue _Py_VaBuildValue_SizeT
#define Py_VaBuildValue
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyModule_AddIntMacro(m, c) PyModule_AddIntConstant(m, #c, c)
#define PyModule_AddIntMacro
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyModule_AddStringMacro(m, c) PyModule_AddStringConstant(m, #c, c)
#define PyModule_AddStringMacro
#define PYTHON_API_VERSION
#define PYTHON_API_STRING
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_InitModule4 Py_InitModule4_64
#define Py_InitModule4
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_InitModule4 Py_InitModule4TraceRefs_64
 #define Py_InitModule4
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_InitModule4 Py_InitModule4TraceRefs
 #define Py_InitModule4
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_InitModule(name, methods) Py_InitModule4(name, methods, (char *)NULL, (PyObject *)NULL, PYTHON_API_VERSION)
#define Py_InitModule
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_InitModule3(name, methods, doc) Py_InitModule4(name, methods, doc, (PyObject *)NULL, PYTHON_API_VERSION)
#define Py_InitModule3
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyCF_MASK (CO_FUTURE_DIVISION | CO_FUTURE_ABSOLUTE_IMPORT | CO_FUTURE_WITH_STATEMENT | CO_FUTURE_PRINT_FUNCTION | CO_FUTURE_UNICODE_LITERALS)
#define PyCF_MASK
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyCF_MASK_OBSOLETE (CO_NESTED)
#define PyCF_MASK_OBSOLETE
#define PyCF_SOURCE_IS_UTF8
#define PyCF_DONT_IMPLY_DEDENT
#define PyCF_ONLY_AST
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyParser_SimpleParseString(S, B) PyParser_SimpleParseStringFlags(S, B, 0)
#define PyParser_SimpleParseString
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyParser_SimpleParseFile(FP, S, B) PyParser_SimpleParseFileFlags(FP, S, B, 0)
#define PyParser_SimpleParseFile
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_CompileString(str, p, s) Py_CompileStringFlags(str, p, s, NULL)
#define Py_CompileString
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyRun_String(str, s, g, l) PyRun_StringFlags(str, s, g, l, NULL)
#define PyRun_String
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyRun_AnyFile(fp, name) PyRun_AnyFileExFlags(fp, name, 0, NULL)
#define PyRun_AnyFile
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyRun_AnyFileEx(fp, name, closeit) PyRun_AnyFileExFlags(fp, name, closeit, NULL)
#define PyRun_AnyFileEx
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyRun_AnyFileFlags(fp, name, flags) PyRun_AnyFileExFlags(fp, name, 0, flags)
#define PyRun_AnyFileFlags
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyRun_SimpleString(s) PyRun_SimpleStringFlags(s, NULL)
#define PyRun_SimpleString
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyRun_SimpleFile(f, p) PyRun_SimpleFileExFlags(f, p, 0, NULL)
#define PyRun_SimpleFile
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyRun_SimpleFileEx(f, p, c) PyRun_SimpleFileExFlags(f, p, c, NULL)
#define PyRun_SimpleFileEx
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyRun_InteractiveOne(f, p) PyRun_InteractiveOneFlags(f, p, NULL)
#define PyRun_InteractiveOne
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyRun_InteractiveLoop(f, p) PyRun_InteractiveLoopFlags(f, p, NULL)
#define PyRun_InteractiveLoop
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyRun_File(fp, p, s, g, l) PyRun_FileExFlags(fp, p, s, g, l, 0, NULL)
#define PyRun_File
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyRun_FileEx(fp, p, s, g, l, c) PyRun_FileExFlags(fp, p, s, g, l, c, NULL)
#define PyRun_FileEx
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyRun_FileFlags(fp, p, s, g, l, flags) PyRun_FileExFlags(fp, p, s, g, l, 0, flags)
#define PyRun_FileFlags
#define PYOS_STACK_MARGIN
#define USE_STACKCHECK
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyEval_CallObject(func,arg) PyEval_CallObjectWithKeywords(func, arg, (PyObject *)NULL)
#define PyEval_CallObject
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_EnterRecursiveCall(where) (_Py_MakeRecCheck(PyThreadState_GET()->recursion_depth) && _Py_CheckRecursiveCall(where))
#define Py_EnterRecursiveCall
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_LeaveRecursiveCall() (--PyThreadState_GET()->recursion_depth)
#define Py_LeaveRecursiveCall
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Py_MakeRecCheck(x) (++(x) > --_Py_CheckRecursionLimit)
#define _Py_MakeRecCheck
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Py_MakeRecCheck(x) (++(x) > _Py_CheckRecursionLimit)
#define _Py_MakeRecCheck
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_BEGIN_ALLOW_THREADS { PyThreadState *_save; _save = PyEval_SaveThread();
#define Py_BEGIN_ALLOW_THREADS
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_BLOCK_THREADS PyEval_RestoreThread(_save);
#define Py_BLOCK_THREADS
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_UNBLOCK_THREADS _save = PyEval_SaveThread();
#define Py_UNBLOCK_THREADS
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_END_ALLOW_THREADS PyEval_RestoreThread(_save); }
#define Py_END_ALLOW_THREADS
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_BEGIN_ALLOW_THREADS {
#define Py_BEGIN_ALLOW_THREADS
#define Py_BLOCK_THREADS
#define Py_UNBLOCK_THREADS
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_END_ALLOW_THREADS }
#define Py_END_ALLOW_THREADS
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyImport_ImportModuleEx(n, g, l, f) PyImport_ImportModuleLevel(n, g, l, f, -1)
#define PyImport_ImportModuleEx
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _PyImport_AcquireLock()
#define _PyImport_AcquireLock
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _PyImport_ReleaseLock() 1
#define _PyImport_ReleaseLock
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyObject_CallFunction _PyObject_CallFunction_SizeT
#define PyObject_CallFunction
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyObject_CallMethod _PyObject_CallMethod_SizeT
#define PyObject_CallMethod
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyObject_DelAttrString(O,A) PyObject_SetAttrString((O),(A),NULL)
#define PyObject_DelAttrString
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyObject_DelAttr(O,A) PyObject_SetAttr((O),(A),NULL)
#define PyObject_DelAttr
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyObject_Length PyObject_Size
#define PyObject_Length
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyObject_CheckBuffer(obj) (((obj)->ob_type->tp_as_buffer != NULL) && (PyType_HasFeature((obj)->ob_type, Py_TPFLAGS_HAVE_NEWBUFFER)) && ((obj)->ob_type->tp_as_buffer->bf_getbuffer != NULL))
#define PyObject_CheckBuffer
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyIter_Check(obj) (PyType_HasFeature((obj)->ob_type, Py_TPFLAGS_HAVE_ITER) && (obj)->ob_type->tp_iternext != NULL && (obj)->ob_type->tp_iternext != &_PyObject_NextNotImplemented)
#define PyIter_Check
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyIndex_Check(obj) ((obj)->ob_type->tp_as_number != NULL && PyType_HasFeature((obj)->ob_type, Py_TPFLAGS_HAVE_INDEX) && (obj)->ob_type->tp_as_number->nb_index != NULL)
#define PyIndex_Check
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PySequence_Length PySequence_Size
#define PySequence_Length
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PySequence_Fast_GET_SIZE(o) (PyList_Check(o) ? PyList_GET_SIZE(o) : PyTuple_GET_SIZE(o))
#define PySequence_Fast_GET_SIZE
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PySequence_Fast_GET_ITEM(o, i) (PyList_Check(o) ? PyList_GET_ITEM(o, i) : PyTuple_GET_ITEM(o, i))
#define PySequence_Fast_GET_ITEM
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PySequence_ITEM(o, i) ( Py_TYPE(o)->tp_as_sequence->sq_item(o, i) )
#define PySequence_ITEM
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PySequence_Fast_ITEMS(sf) (PyList_Check(sf) ? ((PyListObject *)(sf))->ob_item : ((PyTupleObject *)(sf))->ob_item)
#define PySequence_Fast_ITEMS
#define PY_ITERSEARCH_COUNT
#define PY_ITERSEARCH_INDEX
#define PY_ITERSEARCH_CONTAINS
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PySequence_In PySequence_Contains
#define PySequence_In
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyMapping_Length PyMapping_Size
#define PyMapping_Length
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyMapping_DelItemString(O,K) PyObject_DelItemString((O),(K))
#define PyMapping_DelItemString
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyMapping_DelItem(O,K) PyObject_DelItem((O),(K))
#define PyMapping_DelItem
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyMapping_Keys(O) PyObject_CallMethod(O,"keys",NULL)
#define PyMapping_Keys
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyMapping_Values(O) PyObject_CallMethod(O,"values",NULL)
#define PyMapping_Values
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyMapping_Items(O) PyObject_CallMethod(O,"items",NULL)
#define PyMapping_Items
#define CO_OPTIMIZED
#define CO_NEWLOCALS
#define CO_VARARGS
#define CO_VARKEYWORDS
#define CO_NESTED
#define CO_GENERATOR
#define CO_NOFREE
#define CO_FUTURE_DIVISION
#define CO_FUTURE_ABSOLUTE_IMPORT
#define CO_FUTURE_WITH_STATEMENT
#define CO_FUTURE_PRINT_FUNCTION
#define CO_FUTURE_UNICODE_LITERALS
#define PY_PARSER_REQUIRES_FUTURE_KEYWORD
#define CO_MAXBLOCKS
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyCode_Check(op) (Py_TYPE(op) == &PyCode_Type)
#define PyCode_Check
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyCode_GetNumFree(op) (PyTuple_GET_SIZE((op)->co_freevars))
#define PyCode_GetNumFree
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _PyCode_GETCODEPTR(co, pp) ((*Py_TYPE((co)->co_code)->tp_as_buffer->bf_getreadbuffer) ((co)->co_code, 0, (void **)(pp)))
#define _PyCode_GETCODEPTR
#define FUTURE_NESTED_SCOPES
#define FUTURE_GENERATORS
#define FUTURE_DIVISION
#define FUTURE_ABSOLUTE_IMPORT
#define FUTURE_WITH_STATEMENT
#define FUTURE_PRINT_FUNCTION
#define FUTURE_UNICODE_LITERALS
#define PY_CTF_LOWER
#define PY_CTF_UPPER
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PY_CTF_ALPHA (PY_CTF_LOWER|PY_CTF_UPPER)
#define PY_CTF_ALPHA
#define PY_CTF_DIGIT
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PY_CTF_ALNUM (PY_CTF_ALPHA|PY_CTF_DIGIT)
#define PY_CTF_ALNUM
#define PY_CTF_SPACE
#define PY_CTF_XDIGIT
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_ISLOWER(c) (_Py_ctype_table[Py_CHARMASK(c)] & PY_CTF_LOWER)
#define Py_ISLOWER
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_ISUPPER(c) (_Py_ctype_table[Py_CHARMASK(c)] & PY_CTF_UPPER)
#define Py_ISUPPER
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_ISALPHA(c) (_Py_ctype_table[Py_CHARMASK(c)] & PY_CTF_ALPHA)
#define Py_ISALPHA
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_ISDIGIT(c) (_Py_ctype_table[Py_CHARMASK(c)] & PY_CTF_DIGIT)
#define Py_ISDIGIT
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_ISXDIGIT(c) (_Py_ctype_table[Py_CHARMASK(c)] & PY_CTF_XDIGIT)
#define Py_ISXDIGIT
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_ISALNUM(c) (_Py_ctype_table[Py_CHARMASK(c)] & PY_CTF_ALNUM)
#define Py_ISALNUM
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_ISSPACE(c) (_Py_ctype_table[Py_CHARMASK(c)] & PY_CTF_SPACE)
#define Py_ISSPACE
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_TOLOWER(c) (_Py_ctype_tolower[Py_CHARMASK(c)])
#define Py_TOLOWER
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_TOUPPER(c) (_Py_ctype_toupper[Py_CHARMASK(c)])
#define Py_TOUPPER
#define Py_DTSF_SIGN
#define Py_DTSF_ADD_DOT_0
#define Py_DTSF_ALT
#define Py_DTST_FINITE
#define Py_DTST_INFINITE
#define Py_DTST_NAN
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyOS_strnicmp strnicmp
#define PyOS_strnicmp
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyOS_stricmp stricmp
#define PyOS_stricmp
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyOS_strnicmp PyOS_mystrnicmp
#define PyOS_strnicmp
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyOS_stricmp PyOS_mystricmp
#define PyOS_stricmp
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyArg_GetInt(v, a) PyArg_Parse((v), "i", (a))
#define PyArg_GetInt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyArg_NoArgs(v) PyArg_Parse(v, "")
#define PyArg_NoArgs
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Py_CHARMASK(c) ((unsigned char)((c) & 0xff))
#define Py_CHARMASK
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyFPE_START_PROTECT(err_string, leave_stmt) if (!PyFPE_counter++ && setjmp(PyFPE_jbuf)) { PyErr_SetString(PyExc_FloatingPointError, err_string); PyFPE_counter = 0; leave_stmt; }
#define PyFPE_START_PROTECT
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyFPE_END_PROTECT(v) PyFPE_counter -= (int)PyFPE_dummy(&(v));
#define PyFPE_END_PROTECT
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyFPE_START_PROTECT(err_string, leave_stmt)
#define PyFPE_START_PROTECT
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyFPE_END_PROTECT(v)
#define PyFPE_END_PROTECT
#define Py_single_input
#define Py_file_input
#define Py_eval_input
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyDoc_VAR(name) static char name[]
#define PyDoc_VAR
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyDoc_STRVAR(name,str) PyDoc_VAR(name) = PyDoc_STR(str)
#define PyDoc_STRVAR
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyDoc_STR(str) str
#define PyDoc_STR
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PyDoc_STR(str) ""
#define PyDoc_STR
	#define DEBUG
#else
#endif

public abstract class IPythonExceptionSender
{
		public void Clear()
		{
			m_strExceptionString = "";
		}

		public void RegisterExceptionString(string c_szString)
		{
			m_strExceptionString += c_szString;
		}

		public abstract void Send();

		protected string m_strExceptionString = "";
}