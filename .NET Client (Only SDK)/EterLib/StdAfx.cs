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

