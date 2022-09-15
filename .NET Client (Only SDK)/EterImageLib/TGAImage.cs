using System.Diagnostics;



//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __CYGWIN__ __CYGWIN32__
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __IBMC__ __IBMCPP__
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __INTEL_COMPILER __ICL
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __AZTEC_C__ __VERSION
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define ptrdiff_t long
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __far far
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __near near
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __cdecl cdecl
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __far far
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __huge huge
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __near near
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __pascal pascal
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __huge huge
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __cdecl _cdecl
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __far _far
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __huge _huge
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __near _near
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __pascal _pascal
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __cdecl cdecl
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __pascal pascal
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_PP_STRINGIZE(x) #x
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_PP_MACRO_EXPAND(x) LZO_PP_STRINGIZE(x)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_PP_CONCAT2(a,b) a ## b
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_PP_CONCAT3(a,b,c) a ## b ## c
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_PP_CONCAT4(a,b,c,d) a ## b ## c ## d
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_PP_CONCAT5(a,b,c,d,e) a ## b ## c ## d ## e
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_PP_ECONCAT2(a,b) LZO_PP_CONCAT2(a,b)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_PP_ECONCAT3(a,b,c) LZO_PP_CONCAT3(a,b,c)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_PP_ECONCAT4(a,b,c,d) LZO_PP_CONCAT4(a,b,c,d)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_PP_ECONCAT5(a,b,c,d,e) LZO_PP_CONCAT5(a,b,c,d,e)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_CPP_STRINGIZE(x) #x
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_CPP_MACRO_EXPAND(x) LZO_CPP_STRINGIZE(x)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_CPP_CONCAT2(a,b) a ## b
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_CPP_CONCAT3(a,b,c) a ## b ## c
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_CPP_CONCAT4(a,b,c,d) a ## b ## c ## d
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_CPP_CONCAT5(a,b,c,d,e) a ## b ## c ## d ## e
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_CPP_ECONCAT2(a,b) LZO_CPP_CONCAT2(a,b)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_CPP_ECONCAT3(a,b,c) LZO_CPP_CONCAT3(a,b,c)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_CPP_ECONCAT4(a,b,c,d) LZO_CPP_CONCAT4(a,b,c,d)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_CPP_ECONCAT5(a,b,c,d,e) LZO_CPP_CONCAT5(a,b,c,d,e)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __LZO_MASK_GEN(o,b) (((((o) << ((b)-1)) - (o)) << 1) + (o))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_EXTERN_C extern "C"
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_EXTERN_C extern
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_INFO_CCVER LZO_PP_MACRO_EXPAND(__CILLY__)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_INFO_CCVER LZO_PP_MACRO_EXPAND(SDCC)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_CC_PATHSCALE (__PATHCC__ * 0x10000L + __PATHCC_MINOR__ * 0x100 + __PATHCC_PATCHLEVEL__)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_INFO_CCVER __PATHSCALE__
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_INFO_CCVER LZO_PP_MACRO_EXPAND(__INTEL_COMPILER)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_INFO_CCVER LZO_PP_MACRO_EXPAND(__POCC__)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_CC_LLVM (__GNUC__ * 0x10000L + __GNUC_MINOR__ * 0x100 + __GNUC_PATCHLEVEL__)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_CC_LLVM (__GNUC__ * 0x10000L + __GNUC_MINOR__ * 0x100)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_INFO_CCVER __VERSION__
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_CC_GNUC (__GNUC__ * 0x10000L + __GNUC_MINOR__ * 0x100 + __GNUC_PATCHLEVEL__)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_CC_GNUC (__GNUC__ * 0x10000L + __GNUC_MINOR__ * 0x100)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_CC_GNUC (__GNUC__ * 0x10000L)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_INFO_CCVER __VERSION__
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_INFO_CCVER LZO_PP_MACRO_EXPAND(__AZTEC_C__)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_INFO_CCVER LZO_PP_MACRO_EXPAND(__BORLANDC__)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_INFO_CCVER LZO_PP_MACRO_EXPAND(_RELEASE)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_INFO_CCVER LZO_PP_MACRO_EXPAND(__DMC__)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_INFO_CCVER LZO_PP_MACRO_EXPAND(__DECC)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_INFO_CCVER LZO_PP_MACRO_EXPAND(__VER__)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_INFO_CCVER LZO_PP_MACRO_EXPAND(__IBMC__)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_INFO_CCVER LZO_PP_MACRO_EXPAND(__C166__)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_INFO_CCVER LZO_PP_MACRO_EXPAND(__LCC_VERSION__)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_INFO_CCVER LZO_PP_MACRO_EXPAND(_MSC_VER) "." LZO_PP_MACRO_EXPAND(_MSC_FULL_VER)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_INFO_CCVER LZO_PP_MACRO_EXPAND(_MSC_VER)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_INFO_CCVER LZO_PP_MACRO_EXPAND(__MWERKS__)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_INFO_CCVER LZO_PP_MACRO_EXPAND(__PACIFIC__)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_INFO_CCVER LZO_PP_MACRO_EXPAND(__PUREC__)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_INFO_CCVER LZO_PP_MACRO_EXPAND(__SC__)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_CC_SUNPROC __SUNPRO_C
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_INFO_CCVER LZO_PP_MACRO_EXPAND(__SUNPRO_C)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_CC_SUNPROC __SUNPRO_CC
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_INFO_CCVER LZO_PP_MACRO_EXPAND(__SUNPRO_CC)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_INFO_CCVER LZO_PP_MACRO_EXPAND(__TINYC__)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_INFO_CCVER LZO_PP_MACRO_EXPAND(__TSC__)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_INFO_CCVER LZO_PP_MACRO_EXPAND(__WATCOMC__)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_INFO_CCVER LZO_PP_MACRO_EXPAND(__TURBOC__)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_INFO_CCVER LZO_PP_MACRO_EXPAND(__ZTC__)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_MM_AHSHIFT ((unsigned) _AHSHIFT)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_MM_AHSHIFT ((unsigned) _AHSHIFT)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_MM_AHSHIFT ((unsigned) _AHSHIFT)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_MM_AHSHIFT ((unsigned) _AHSHIFT)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_MM_AHSHIFT ((unsigned) _HShift)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_SIZEOF_SHORT (SIZEOF_SHORT)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_SIZEOF_INT (SIZEOF_INT)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_SIZEOF_LONG (SIZEOF_LONG)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_SIZEOF_LONG_LONG (SIZEOF_LONG_LONG)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_SIZEOF___INT16 (SIZEOF___INT16)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_SIZEOF___INT32 (SIZEOF___INT32)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_SIZEOF___INT64 (SIZEOF___INT64)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_SIZEOF_VOID_P (SIZEOF_VOID_P)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_SIZEOF_SIZE_T (SIZEOF_SIZE_T)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_SIZEOF_PTRDIFF_T (SIZEOF_PTRDIFF_T)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __LZO_LSR(x,b) (((x)+0ul) >> (b))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_SIZEOF_LONG_LONG LZO_SIZEOF_LONG
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_SIZEOF_SIZE_T LZO_SIZEOF_INT
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_SIZEOF_PTRDIFF_T LZO_SIZEOF_INT
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_SIZEOF_VOID_P LZO_SIZEOF_LONG
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_SIZEOF_SIZE_T LZO_SIZEOF_LONG
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_SIZEOF_PTRDIFF_T LZO_SIZEOF_LONG
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __LZO_WORDSIZE LZO_SIZEOF_LONG
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_SIZEOF_SIZE_T LZO_SIZEOF_LONG
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_SIZEOF_PTRDIFF_T LZO_SIZEOF_LONG
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_SIZEOF_SIZE_T LZO_SIZEOF_LONG
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_SIZEOF_PTRDIFF_T LZO_SIZEOF_LONG
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_SIZEOF_VOID_P LZO_SIZEOF_LONG
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_WORDSIZE __LZO_WORDSIZE
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_WORDSIZE LZO_SIZEOF_VOID_P
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_SIZEOF_SIZE_T LZO_SIZEOF_VOID_P
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_SIZEOF_PTRDIFF_T LZO_SIZEOF_VOID_P
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_SIZEOF_PTRDIFF_T LZO_SIZEOF_SIZE_T
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_LIBC_UCLIBC (__UCLIBC_MAJOR__ * 0x10000L + __UCLIBC_MINOR__ * 0x100 + __UCLIBC_SUBLEVEL__)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_LIBC_GLIBC (__GLIBC__ * 0x10000L + __GLIBC_MINOR__ * 0x100)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_LIBC_MSL __MSL__
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __lzo_gnuc_extension__ __extension__
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __lzo_gnuc_extension__ __extension__
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __lzo_ua_volatile volatile
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __lzo_alignof(e) __alignof__(e)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __lzo_alignof(e) __alignof__(e)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __lzo_alignof(e) __alignof(e)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __lzo_inline inline
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __lzo_inline __inline
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __lzo_inline __inline__
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __lzo_inline __inline
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __lzo_inline __inline
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __lzo_inline __inline
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __lzo_inline __inline
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __lzo_inline inline
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __lzo_forceinline __inline__
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __lzo_forceinline __forceinline
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __lzo_forceinline __inline__
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __lzo_forceinline __inline__
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __lzo_forceinline __forceinline
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __lzo_noinline __declspec(noinline)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __lzo_noinline __declspec(noinline)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __lzo_noinline __declspec(noinline)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __lzo_noreturn __declspec(noreturn)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __lzo_noreturn __declspec(noreturn)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __lzo_nothrow __declspec(nothrow)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __lzo_nothrow __declspec(nothrow)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __lzo_restrict __restrict__
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __lzo_restrict __restrict__
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __lzo_restrict __restrict__
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __lzo_restrict __restrict
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __lzo_likely(e) (__builtin_expect(!!(e),1))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __lzo_unlikely(e) (__builtin_expect(!!(e),0))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __lzo_likely(e) (__builtin_expect(!!(e),1))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __lzo_unlikely(e) (__builtin_expect(!!(e),0))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __lzo_likely(e) (__builtin_expect(!!(e),1))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __lzo_unlikely(e) (__builtin_expect(!!(e),0))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __lzo_likely(e) (e)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __lzo_unlikely(e) (e)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_UNUSED(var) ((void) &var)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_UNUSED(var) if (&var) ; else
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_UNUSED(var) ((void) var)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_UNUSED(var) if (&var) ; else
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_UNUSED(var) {extern int __lzo_unused[1-2*!(sizeof(var)>0)];}
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_UNUSED(var) ((void) sizeof(var))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_UNUSED(var) ((void) var)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_UNUSED(var) ((void) &var)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_UNUSED_FUNC(func) ((void) func)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_UNUSED_FUNC(func) if (func) ; else
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_UNUSED_FUNC(func) ((void) &func)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_UNUSED_FUNC(func) if (func) ; else
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_UNUSED_FUNC(func) ((void) &func)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_UNUSED_FUNC(func) {extern int __lzo_unused[1-2*!(sizeof((int)func)>0)];}
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_UNUSED_FUNC(func) ((void) func)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_UNUSED_LABEL(l) switch(0) case 1:goto l
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_UNUSED_LABEL(l) if (0) goto l
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_UNUSED_LABEL(l) switch(0) case 1:goto l
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_DEFINE_UNINITIALIZED_VAR(type,var,init) type var = var
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_DEFINE_UNINITIALIZED_VAR(type,var,init) type var = init
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_COMPILE_TIME_ASSERT_HEADER(e) extern int __lzo_cta[1-!(e)];
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_COMPILE_TIME_ASSERT_HEADER(e) extern int __lzo_cta[1u-2*!(e)];
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_COMPILE_TIME_ASSERT_HEADER(e) extern int __lzo_cta[1-!(e)];
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_COMPILE_TIME_ASSERT_HEADER(e) extern int __lzo_cta[1-2*!(e)];
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_COMPILE_TIME_ASSERT(e) {typedef int __lzo_cta_t[1-!(e)];}
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_COMPILE_TIME_ASSERT(e) switch(0) case 1:case !(e):break;
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_COMPILE_TIME_ASSERT(e) switch(0) case 1:case !(e):break;
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_COMPILE_TIME_ASSERT(e) switch(0) case 1:case !(e):break;
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_COMPILE_TIME_ASSERT(e) {typedef int __lzo_cta_t[1-2*!(e)];}
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __lzo_cdecl __cdecl
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __lzo_cdecl_main __cdecl
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __lzo_cdecl_qsort __pascal
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __lzo_cdecl_qsort _stdcall
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __lzo_cdecl_qsort __cdecl
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __lzo_cdecl __cdecl
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __lzo_cdecl __cdecl
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __lzo_cdecl_atexit __cdecl
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __lzo_cdecl_main __cdecl
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __lzo_cdecl_qsort __cdecl
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __lzo_cdecl_sighandler __pascal
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __lzo_cdecl_sighandler _stdcall
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __lzo_cdecl_sighandler __clrcall
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __lzo_cdecl_sighandler _far _cdecl _loadds
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __lzo_cdecl_sighandler _far _cdecl
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __lzo_cdecl_sighandler _cdecl
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __lzo_cdecl_sighandler __cdecl
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __lzo_cdecl __cdecl
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __lzo_cdecl cdecl
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __lzo_cdecl_va __lzo_cdecl
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __LZO_ASM_CLOBBER "cc", "memory"
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __LZO_INFOSTR_MM "." LZO_INFO_MM
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __LZO_INFOSTR_PM "." LZO_INFO_ABI_PM
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __LZO_INFOSTR_ENDIAN "." LZO_INFO_ABI_ENDIAN
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __LZO_INFOSTR_OSNAME LZO_INFO_OS "." LZO_INFO_OS_CONSOLE
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __LZO_INFOSTR_OSNAME LZO_INFO_OS "." LZO_INFO_OS_POSIX
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __LZO_INFOSTR_OSNAME LZO_INFO_OS
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __LZO_INFOSTR_LIBC "." LZO_INFO_LIBC
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __LZO_INFOSTR_CCVER " " LZO_INFO_CCVER
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_INFO_STRING LZO_INFO_ARCH __LZO_INFOSTR_MM __LZO_INFOSTR_PM __LZO_INFOSTR_ENDIAN " " __LZO_INFOSTR_OSNAME __LZO_INFOSTR_LIBC " " LZO_INFO_CC __LZO_INFOSTR_CCVER
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_UINT32_C(c) c ## UL
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_UINT32_C(c) ((c) + 0U)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_INT_MIN (-1LL - LZO_INT_MAX)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_UINT_MAX UINT_MAX
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_INT_MAX INT_MAX
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_INT_MIN INT_MIN
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_UINT_MAX ULONG_MAX
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_INT_MAX LONG_MAX
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_INT_MIN LONG_MIN
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_UINT32_MAX UINT_MAX
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_INT32_MAX INT_MAX
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_INT32_MIN INT_MIN
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_UINT32_MAX ULONG_MAX
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_INT32_MAX LONG_MAX
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_INT32_MIN LONG_MIN
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define lzo_xint lzo_uint
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define lzo_xint lzo_uint32
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __LZO_MMODEL __huge
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define lzo_bytep unsigned char __LZO_MMODEL *
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define lzo_charp char __LZO_MMODEL *
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define lzo_voidp void __LZO_MMODEL *
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define lzo_shortp short __LZO_MMODEL *
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define lzo_ushortp unsigned short __LZO_MMODEL *
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define lzo_uint32p lzo_uint32 __LZO_MMODEL *
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define lzo_int32p lzo_int32 __LZO_MMODEL *
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define lzo_uintp lzo_uint __LZO_MMODEL *
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define lzo_intp lzo_int __LZO_MMODEL *
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define lzo_xintp lzo_xint __LZO_MMODEL *
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define lzo_voidpp lzo_voidp __LZO_MMODEL *
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define lzo_bytepp lzo_bytep __LZO_MMODEL *
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define lzo_byte unsigned char __LZO_MMODEL
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __LZO_EXTERN_C extern "C"
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __LZO_EXTERN_C extern
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __LZO_CDECL __lzo_cdecl
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_PUBLIC(_rettype) __LZO_EXPORT1 _rettype __LZO_EXPORT2 __LZO_CDECL
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_EXTERN(_rettype) __LZO_EXTERN_C LZO_PUBLIC(_rettype)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_PRIVATE(_rettype) static _rettype __LZO_CDECL
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define lzo_callback_p lzo_callback_t __LZO_MMODEL *
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define lzo_sizeof_dict_t ((unsigned)sizeof(lzo_bytep))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define lzo_init() __lzo_init_v2(LZO_VERSION,(int)sizeof(short),(int)sizeof(int), (int)sizeof(long),(int)sizeof(lzo_uint32),(int)sizeof(lzo_uint), (int)lzo_sizeof_dict_t,(int)sizeof(char *),(int)sizeof(lzo_voidp), (int)sizeof(lzo_callback_t))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_PTR_ALIGN_UP(_ptr,_size) ((_ptr) + (lzo_uint) __lzo_align_gap((const lzo_voidp)(_ptr),(lzo_uint)(_size)))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __LZO_ENTRY __LZO_CDECL
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_EXTERN_CDECL LZO_EXTERN
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO_ALIGN LZO_PTR_ALIGN_UP
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define lzo_compress_asm_t lzo_compress_t
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define lzo_decompress_asm_t lzo_decompress_t
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO1X_MEM_COMPRESS LZO1X_1_MEM_COMPRESS
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO1X_1_MEM_COMPRESS ((lzo_uint32) (16384L * lzo_sizeof_dict_t))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO1X_1_11_MEM_COMPRESS ((lzo_uint32) (2048L * lzo_sizeof_dict_t))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO1X_1_12_MEM_COMPRESS ((lzo_uint32) (4096L * lzo_sizeof_dict_t))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO1X_1_15_MEM_COMPRESS ((lzo_uint32) (32768L * lzo_sizeof_dict_t))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LZO1X_999_MEM_COMPRESS ((lzo_uint32) (14 * 16384L * sizeof(short)))


public class CTGAImage : CImage
{
		public enum ETGAImageFlags
		{
			FLAG_RLE_COMPRESS = (1 << 0)
		}

		public CTGAImage()
		{
			this.m_dwFlag = 0;
		}

		public CTGAImage(CImage image)
		{
			this.m_dwFlag = 0;
			int w = image.GetWidth();
			int h = image.GetHeight();

			Create(w, h);

//# Laniatus Games Studio Inc. | TODO TASK: C# does not have an equivalent to pointers to value types:
//Original Metin2 CPlus Line: uint * pdwDest = GetBasePointer();
			uint pdwDest = GetBasePointer();
//# Laniatus Games Studio Inc. | TODO TASK: The memory management function 'memcpy' has no equivalent in C#:
			memcpy(pdwDest, image.GetBasePointer(), w * h * sizeof(uint));
			FlipTopToBottom();
		}

		public override void Dispose()
		{
			base.Dispose();
		}

		public override void Create(int width, int height)
		{
//# Laniatus Games Studio Inc. | TODO TASK: The memory management function 'memset' has no equivalent in C#:
			memset(m_Header, 0, sizeof(TGA_HEADER));

			m_Header.imgType = 2;
			m_Header.width = (ushort)((short) width);
			m_Header.height = (ushort)((short) height);
			m_Header.colorBits = 32;
			m_Header.desc = 0x08;

			base.Create(width, height);
		}

//# Laniatus Games Studio Inc. | TODO TASK: Pointer arithmetic is detected on the parameter 'c_pbMem', so pointers on this parameter are left unchanged:
		public virtual bool LoadFromMemory(int iSize, in byte * c_pbMem)
		{
//# Laniatus Games Studio Inc. | TODO TASK: The memory management function 'memcpy' has no equivalent in C#:
			memcpy(m_Header, c_pbMem, 18);
			c_pbMem += 18;
			iSize -= 18;

			base.Create(m_Header.width, m_Header.height);

			uint hxw = (uint)(m_Header.width * m_Header.height);
			byte r;
			byte g;
			byte b;
			byte a;
			uint i;

			uint[] pdwDest = GetBasePointer();

			switch (m_Header.imgType)
			{
				case 3:
				{
						for (i = 0; LaniatusDefVariables < hxw; ++i)
						{
							a = (char) * (c_pbMem++);
							pdwDest[i] = (uint)((a << 24) | (a << 16) | (a << 8) | a);
						}
				}
					break;

				case 2:
				{
						if (m_Header.colorBits == 16)
						{
							for (i = 0; LaniatusDefVariables < hxw; ++i)
							{
								ushort w;

//# Laniatus Games Studio Inc. | TODO TASK: The memory management function 'memcpy' has no equivalent in C#:
								memcpy(w, c_pbMem, sizeof(ushort));
								c_pbMem += sizeof(ushort);
								iSize -= sizeof(ushort);

								b = (byte)(w & 0x1F);
								g = (byte)((w >> 5) & 0x1F);
								r = (byte)((w >> 10) & 0x1F);

								b <<= 3;
								g <<= 3;
								r <<= 3;
								a = 0xff;

								pdwDest[i] = (uint)((a << 24) | (r << 16) | (g << 8) | b);
							}
						}
						else if (m_Header.colorBits == 24)
						{
							for (i = 0; LaniatusDefVariables < hxw; ++i)
							{
								r = (byte) * (c_pbMem++);
								--iSize;
								g = (byte) * (c_pbMem++);
								--iSize;
								b = (byte) * (c_pbMem++);
								--iSize;
								a = 0xff;

								pdwDest[i] = (uint)((a << 24) | (r << 16) | (g << 8) | b);
							}
						}
						else if (m_Header.colorBits == 32)
						{
							int size = GetWidth();
							size *= GetHeight() * 4;

//# Laniatus Games Studio Inc. | TODO TASK: The memory management function 'memcpy' has no equivalent in C#:
							memcpy(pdwDest, c_pbMem, size);
							c_pbMem += (byte)size;
							iSize -= size;
						}
				}
					break;

				case 10:
				{
						byte rle;

						if (m_Header.colorBits == 24)
						{
							i = 0;
							while (i < hxw)
							{
								rle = (byte) * (c_pbMem++);
								--iSize;

								if (rle < 0x80)
								{
									rle++;

									while (rle != 0)
									{
										b = (byte) * (c_pbMem++);
										--iSize;
										g = (byte) * (c_pbMem++);
										--iSize;
										r = (byte) * (c_pbMem++);
										--iSize;
										a = 0xff;
										pdwDest[i++] = (uint)((a << 24) | (r << 16) | (g << 8) | b);

										if (i > hxw)
										{
											Debug.Assert(!"RLE overflow");
											printf("RLE overflow");
											return false;
										}
										--rle;
									}
								}
								else
								{
									rle -= 127;

									b = (byte) * (c_pbMem++);
									--iSize;
									g = (byte) * (c_pbMem++);
									--iSize;
									r = (byte) * (c_pbMem++);
									--iSize;
									a = 0xff;

									while (rle != 0)
									{
										pdwDest[i++] = (uint)((a << 24) | (r << 16) | (g << 8) | b);

										if (i > hxw)
										{
											Debug.Assert(!"RLE overflow");
											printf("RLE overflow");
											return false;
										}
										--rle;
									}
								}
							}
						}
						else if (m_Header.colorBits == 32)
						{
							i = 0;
							while (i < hxw)
							{
								rle = (byte) * (c_pbMem++);
								--iSize;

								if (rle < 0x80)
								{
									rle++;

									while (rle != 0)
									{
										b = (byte) * (c_pbMem++);
										--iSize;
										g = (byte) * (c_pbMem++);
										--iSize;
										r = (byte) * (c_pbMem++);
										--iSize;
										a = (byte) * (c_pbMem++);
										--iSize;
										pdwDest[i++] = (uint)((a << 24) | (r << 16) | (g << 8) | b);

										if (i > hxw)
										{
											Debug.Assert(!"RLE overflow");
											printf("RLE overflow");
											return false;
										}
										--rle;
									}
								}
								else
								{
									rle -= 127;

									b = (byte) * (c_pbMem++);
									--iSize;
									g = (byte) * (c_pbMem++);
									--iSize;
									r = (byte) * (c_pbMem++);
									--iSize;
									a = (byte) * (c_pbMem++);
									--iSize;

									while (rle != 0)
									{
										pdwDest[i++] = (uint)((a << 24) | (r << 16) | (g << 8) | b);

										if (i > hxw)
										{
											Debug.Assert(!"RLE overflow");
											printf("RLE overflow");
											return false;
										}

										--rle;
									}
								}
							}
						}
				}
					break;
			}

			if ((m_Header.desc & 0x20) == 0)
			{
				FlipTopToBottom();
			}

			return true;
		}

		public virtual bool LoadFromDiskFile(string c_szFileName)
		{
			CMappedFile file = new CMappedFile();

//# Laniatus Games Studio Inc. | TODO TASK: C# does not have an equivalent to pointers to value types:
//Original Metin2 CPlus Line: const byte * c_pbMap;
			byte c_pbMap;

			if (!file.Create(c_szFileName, (object) & c_pbMap, 0, 0))
			{
				return false;
			}

			return LoadFromMemory((int)file.Size(), c_pbMap);
		}

		public virtual bool SaveToDiskFile(string c_szFileName)
		{
			FILE fp = fopen(c_szFileName, "wb");

			if (fp == null)
			{
				return false;
			}

			fwrite(m_Header, 18, 1, fp);

			if (m_Header.imgType == 10)
			{
//# Laniatus Games Studio Inc. | TODO TASK: Pointer arithmetic is detected on this variable, so pointers on this variable are left unchanged:
				uint * data = GetBasePointer();

				while (data < m_pdwEndPtr)
				{
					int rle = GetRLEPixelCount(data);

					if (rle < 4)
					{
						int raw = GetRawPixelCount(data);

						if (raw == 0)
						{
							break;
						}

						fputc(raw - 1, fp);

						while (raw != 0)
						{
							fwrite(data, sizeof(uint), 1, fp);
							data++;
							raw--;
						}
					}
					else
					{
						fputc((rle - 1) | 0x80, fp);
						fwrite(data, sizeof(uint), 1, fp);
						data += (uint)rle;
					}
				}
			}
			else
			{
				int size = GetWidth();
				size *= GetHeight() * 4;
				fwrite(GetBasePointer(), size, 1, fp);
			}

			fclose(fp);
			return true;
		}

		public void SetCompressed(bool isCompress = true)
		{
			if (isCompress)
			{
				m_Header.imgType = 10;
			}
			else
			{
				m_Header.imgType = 2;
			}
		}

		public void SetAlphaChannel(bool isExist = true)
		{
			if (isExist)
			{
				m_Header.desc |= 0x08;
			}
			else
			{
				m_Header.desc &= ~0x08;
			}
		}

		public TGA_HEADER GetHeader()
		{
//# Laniatus Games Studio Inc. | TODO TASK: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
//Original Metin2 CPlus Line: return m_Header;
			return new TGA_HEADER(m_Header);
		}

//# Laniatus Games Studio Inc. | TODO TASK: Pointer arithmetic is detected on the parameter 'data', so pointers on this parameter are left unchanged:
		protected int GetRawPixelCount(in uint * data)
		{
			int LaniatusDefVariables = 0;

			if (data >= m_pdwEndPtr)
			{
				return 0;
			}

			while ((data < m_pdwEndPtr) && (i < 127))
			{
				int rle = GetRLEPixelCount(data);

				if (rle >= 4)
				{
					break;
				}

				data++;
				i++;
			}

			return i;
		}

//# Laniatus Games Studio Inc. | TODO TASK: Pointer arithmetic is detected on the parameter 'data', so pointers on this parameter are left unchanged:
		protected int GetRLEPixelCount(in uint * data)
		{
			int r = 0;
			uint pixel;

			r = 1;

			if (data >= m_pdwEndPtr)
			{
				return 0;
			}

			pixel = *data;

			while ((r < 127) && (data < m_pdwEndPtr))
			{
				if (pixel != *(++data))
				{
					return r;
				}

				r++;
			}

			return r;
		}

		protected TGA_HEADER m_Header = new TGA_HEADER();
		protected uint m_dwFlag;
//# Laniatus Games Studio Inc. | TODO TASK: C# does not have an equivalent to pointers to value types:
//Original Metin2 CPlus Line: uint * m_pdwEndPtr;
		protected uint m_pdwEndPtr;
}
