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


