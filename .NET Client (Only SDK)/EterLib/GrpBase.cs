using System;
using System.Diagnostics;

//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define WINAPI_PARTITION_PKG_WINTRUST (WINAPI_FAMILY == WINAPI_FAMILY_SERVER)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define WINAPI_PARTITION_PKG_WEBSERVICES (WINAPI_FAMILY == WINAPI_FAMILY_SERVER)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define WINAPI_PARTITION_PKG_EVENTLOGSERVICE (WINAPI_FAMILY == WINAPI_FAMILY_SERVER)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define WINAPI_PARTITION_PKG_VHD (WINAPI_FAMILY == WINAPI_FAMILY_SERVER)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define WINAPI_PARTITION_PKG_PERFCOUNTER (WINAPI_FAMILY == WINAPI_FAMILY_SERVER)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define WINAPI_PARTITION_PKG_SECURESTARTUP (WINAPI_FAMILY == WINAPI_FAMILY_SERVER)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define WINAPI_PARTITION_PKG_REMOTEFS (WINAPI_FAMILY == WINAPI_FAMILY_SERVER)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define WINAPI_PARTITION_PKG_BOOTABLESKU (WINAPI_FAMILY == WINAPI_FAMILY_SERVER)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define WINAPI_PARTITION_PKG_CMD (WINAPI_FAMILY == WINAPI_FAMILY_SERVER)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define WINAPI_PARTITION_PKG_CMDTOOLS (WINAPI_FAMILY == WINAPI_FAMILY_SERVER)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define WINAPI_PARTITION_PKG_DISM (WINAPI_FAMILY == WINAPI_FAMILY_SERVER)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define WINAPI_PARTITION_PKG_CORESETUP (WINAPI_FAMILY == WINAPI_FAMILY_SERVER)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define WINAPI_PARTITION_PKG_APPRUNTIME (WINAPI_FAMILY == WINAPI_FAMILY_SERVER)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define WINAPI_PARTITION_PKG_ESENT (WINAPI_FAMILY == WINAPI_FAMILY_SERVER)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define WINAPI_PARTITION_PKG_WINMGMT (WINAPI_FAMILY == WINAPI_FAMILY_SERVER)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define WINAPI_FAMILY_APP WINAPI_FAMILY_PC_APP
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define WINAPI_FAMILY WINAPI_FAMILY_DESKTOP_APP
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define WINAPI_PARTITION_DESKTOP (WINAPI_FAMILY == WINAPI_FAMILY_DESKTOP_APP)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define WINAPI_PARTITION_APP (WINAPI_FAMILY == WINAPI_FAMILY_DESKTOP_APP || WINAPI_FAMILY == WINAPI_FAMILY_PC_APP || WINAPI_FAMILY == WINAPI_FAMILY_PHONE_APP)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define WINAPI_PARTITION_PC_APP (WINAPI_FAMILY == WINAPI_FAMILY_DESKTOP_APP || WINAPI_FAMILY == WINAPI_FAMILY_PC_APP)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define WINAPI_PARTITION_PHONE_APP (WINAPI_FAMILY == WINAPI_FAMILY_PHONE_APP)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define WINAPI_PARTITION_SYSTEM (WINAPI_FAMILY == WINAPI_FAMILY_SYSTEM || WINAPI_FAMILY == WINAPI_FAMILY_SERVER)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define WINAPI_PARTITION_PHONE WINAPI_PARTITION_PHONE_APP
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define WINAPI_FAMILY_PARTITION(Partitions) (Partitions)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _WINAPI_DEPRECATED_DECLARATION __declspec(deprecated("This API cannot be used in the context of the caller's application type."))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define APP_DEPRECATED_HRESULT HRESULT _WINAPI_DEPRECATED_DECLARATION
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define POINTER_64 __ptr64
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define POINTER_32 __ptr32
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define POINTER_64 __ptr64
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define POINTER_64 __ptr64
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define FIRMWARE_PTR POINTER_32
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define POINTER_SIGNED __sptr
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define POINTER_UNSIGNED __uptr
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define SPOINTER_32 POINTER_SIGNED POINTER_32
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define UPOINTER_32 POINTER_UNSIGNED POINTER_32
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _W64 __w64
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __int3264 __int64
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __int3264 __int32
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define ADDRESS_TAG_BIT 0x40000000000UI64
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PtrToPtr64( p ) ((void * POINTER_64) p)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Ptr64ToPtr( p ) ((void *) p)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define HandleToHandle64( h ) (PtrToPtr64( h ))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Handle64ToHandle( h ) (Ptr64ToPtr( h ))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define HandleToHandle32( h ) (PtrToPtr32( h ))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define HandleToULong( h ) ((ULONG)(ULONG_PTR)(h) )
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define HandleToLong( h ) ((LONG)(LONG_PTR) (h) )
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define ULongToHandle( ul ) ((HANDLE)(ULONG_PTR) (ul) )
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LongToHandle( h ) ((HANDLE)(LONG_PTR) (h) )
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PtrToUlong( p ) ((ULONG)(ULONG_PTR) (p) )
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PtrToLong( p ) ((LONG)(LONG_PTR) (p) )
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PtrToUint( p ) ((UINT)(UINT_PTR) (p) )
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PtrToInt( p ) ((INT)(INT_PTR) (p) )
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PtrToUshort( p ) ((unsigned short)(ULONG_PTR)(p) )
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PtrToShort( p ) ((short)(LONG_PTR)(p) )
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define IntToPtr( LaniatusDefVariables ) ((VOID *)(INT_PTR)((int)i))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define UIntToPtr( ui ) ((VOID *)(UINT_PTR)((unsigned int)ui))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LongToPtr( l ) ((VOID *)(LONG_PTR)((long)l))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define ULongToPtr( ul ) ((VOID *)(ULONG_PTR)((unsigned long)ul))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Ptr32ToPtr( p ) ((void *) p)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Handle32ToHandle( h ) (Ptr32ToPtr( h ))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PtrToPtr32( p ) ((void * POINTER_32) p)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define HandleToHandle32( h ) (PtrToPtr32( h ))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define HandleToUlong(h) HandleToULong(h)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define UlongToHandle(ul) ULongToHandle(ul)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define UlongToPtr(ul) ULongToPtr(ul)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define UintToPtr(ui) UIntToPtr(ui)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MAXUINT_PTR (~((UINT_PTR)0))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MAXINT_PTR ((INT_PTR)(MAXUINT_PTR >> 1))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MININT_PTR (~MAXINT_PTR)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MAXULONG_PTR (~((ULONG_PTR)0))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MAXLONG_PTR ((LONG_PTR)(MAXULONG_PTR >> 1))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MINLONG_PTR (~MAXLONG_PTR)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MAXUHALF_PTR ((UHALF_PTR)~0)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MAXHALF_PTR ((HALF_PTR)(MAXUHALF_PTR >> 1))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MINHALF_PTR (~MAXHALF_PTR)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MAXUINT8 ((UINT8)~((UINT8)0))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MAXINT8 ((INT8)(MAXUINT8 >> 1))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MININT8 ((INT8)~MAXINT8)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MAXUINT16 ((UINT16)~((UINT16)0))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MAXINT16 ((INT16)(MAXUINT16 >> 1))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MININT16 ((INT16)~MAXINT16)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MAXUINT32 ((UINT32)~((UINT32)0))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MAXINT32 ((INT32)(MAXUINT32 >> 1))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MININT32 ((INT32)~MAXINT32)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MAXUINT64 ((UINT64)~((UINT64)0))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MAXINT64 ((INT64)(MAXUINT64 >> 1))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MININT64 ((INT64)~MAXINT64)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MAXULONG32 ((ULONG32)~((ULONG32)0))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MAXLONG32 ((LONG32)(MAXULONG32 >> 1))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MINLONG32 ((LONG32)~MAXLONG32)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MAXULONG64 ((ULONG64)~((ULONG64)0))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MAXLONG64 ((LONG64)(MAXULONG64 >> 1))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MINLONG64 ((LONG64)~MAXLONG64)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MAXULONGLONG ((ULONGLONG)~((ULONGLONG)0))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MINLONGLONG ((LONGLONG)~MAXLONGLONG)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MAXSIZE_T ((SIZE_T)~((SIZE_T)0))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MAXSSIZE_T ((SSIZE_T)(MAXSIZE_T >> 1))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MINSSIZE_T ((SSIZE_T)~MAXSSIZE_T)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MAXUINT ((UINT)~((UINT)0))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MAXINT ((INT)(MAXUINT >> 1))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MININT ((INT)~MAXINT)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MAXDWORD32 ((DWORD32)~((DWORD32)0))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MAXDWORD64 ((DWORD64)~((DWORD64)0))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define midl_user_allocate MIDL_user_allocate
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define midl_user_free MIDL_user_free
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define DECLSPEC_IMPORT __declspec(dllimport)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define RPCRTAPI DECLSPEC_IMPORT
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define RPCNSAPI DECLSPEC_IMPORT
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define RPCXCWORD (sizeof(jmp_buf)/sizeof(int))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define DECLSPEC_NORETURN __declspec(noreturn)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _SAL_VERSION_SAL2(_A) SAL_2_Clean_Violation_using ## _A
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _SAL_VERSION_SAL2(_A)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _SAL_VERSION_CHECK(_A) _SAL_VERSION_SAL2(_A)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _SAL_VERSION_CHECK(_A)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define SAL_VERSION_CHECK(_A) _SAL_VERSION_CHECK(_A)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define SAL_VERSION_SAL2(_A) _SAL_VERSION_SAL2(_A)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _SAL_L_Source_(Name, args, annotes) _SA_annotes3(SAL_name, #Name, "", "2") _Group_(annotes _SAL_nop_impl_)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _SAL_L_Source_(Name, args, annotes) _SA_annotes3(SAL_name, #Name, "", "2") _GrouP_(annotes _SAL_nop_impl_)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _SAL1_Source_(Name, args, annotes) _SA_annotes3(SAL_name, #Name, "", "1") _GrouP_(annotes _SAL_nop_impl_)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _SAL1_1_Source_(Name, args, annotes) _SA_annotes3(SAL_name, #Name, "", "1.1") _GrouP_(annotes _SAL_nop_impl_)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _SAL1_2_Source_(Name, args, annotes) _SA_annotes3(SAL_name, #Name, "", "1.2") _GrouP_(annotes _SAL_nop_impl_)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _SAL2_Source_(Name, args, annotes) _SA_annotes3(SAL_name, #Name, "", "2") _GrouP_(annotes _SAL_nop_impl_)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _SAL_L_Source_(Name, args, annotes) _SA_annotes3(SAL_name, #Name, "", "2") _GrouP_(annotes _SAL_nop_impl_)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _SAL1_Source_(Name, args, annotes) _SA_annotes3(SAL_name, #Name, "", "1") _Group_(annotes _SAL_nop_impl_)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _SAL1_1_Source_(Name, args, annotes) _SA_annotes3(SAL_name, #Name, "", "1.1") _Group_(annotes _SAL_nop_impl_)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _SAL1_2_Source_(Name, args, annotes) _SA_annotes3(SAL_name, #Name, "", "1.2") _Group_(annotes _SAL_nop_impl_)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _SAL2_Source_(Name, args, annotes) _SA_annotes3(SAL_name, #Name, "", "2") _Group_(annotes _SAL_nop_impl_)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _SAL_L_Source_(Name, args, annotes) _SA_annotes3(SAL_name, #Name, "", "2") _Group_(annotes _SAL_nop_impl_)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _At_(target, annos) _At_impl_(target, annos _SAL_nop_impl_)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _At_buffer_(target, iter, bound, annos) _At_buffer_impl_(target, iter, bound, annos _SAL_nop_impl_)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _When_(expr, annos) _When_impl_(expr, annos _SAL_nop_impl_)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Group_(annos) _Group_impl_(annos _SAL_nop_impl_)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _GrouP_(annos) _GrouP_impl_(annos _SAL_nop_impl_)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Success_(expr) _SAL2_Source_(_Success_, (expr), _Success_impl_(expr))
//# Laniatus Games Studio Inc. | TODO TASK: Conditional typedefs are not handled by # Laniatus Games Studio Inc. |:
//#define _Return_type_success_(expr) _SAL2_Source_(_Return_type_success_, (expr), _Success_impl_(expr))


public class SFace
{
	public ushort[] indices = new ushort[3];
}





//# Laniatus Games Studio Inc. | TODO TASK: Unions are not supported in C#:
//union UDepth
//{
//	float f;
//	int l;
//	uint dw;
//};

public class SVertex
{
	public float x;
	public float y;
	public float z;
	public uint color;
	public float u;
	public float v;
}

public class STVertex
{
	public float x;
	public float y;
	public float z;
	public float rhw;
}

public class SPVertex
{
	public float x;
	public float y;
	public float z;
}

public class SPDVertex
{
	public float x;
	public float y;
	public float z;
	public uint color;
}

public class SPDTVertexRaw
{
	public float px;
	public float py;
	public float pz;
	public uint diffuse;
	public float u;
	public float v;
}

public class SPTVertex
{
	public _D3DVECTOR position = new _D3DVECTOR();
	public D3DXVECTOR2 texCoord = new D3DXVECTOR2();
}

public class SPDTVertex
{
	public _D3DVECTOR position = new _D3DVECTOR();
	public uint diffuse;
	public D3DXVECTOR2 texCoord = new D3DXVECTOR2();
	public static uint kFVF = D3DFVF_XYZ | D3DFVF_DIFFUSE | D3DFVF_TEX1;
}

public class SPNTVertex
{
	public _D3DVECTOR position = new _D3DVECTOR();
	public _D3DVECTOR normal = new _D3DVECTOR();
	public D3DXVECTOR2 texCoord = new D3DXVECTOR2();
}

public class SPNT2Vertex
{
	public _D3DVECTOR position = new _D3DVECTOR();
	public _D3DVECTOR normal = new _D3DVECTOR();
	public D3DXVECTOR2 texCoord = new D3DXVECTOR2();
	public D3DXVECTOR2 texCoord2 = new D3DXVECTOR2();
}

public class SPDT2Vertex
{
	public _D3DVECTOR position = new _D3DVECTOR();
	public uint diffuse;
	public D3DXVECTOR2 texCoord = new D3DXVECTOR2();
	public D3DXVECTOR2 texCoord2 = new D3DXVECTOR2();
}

public class SNameInfo
{
	public uint name;
	public TDepth depth = new TDepth();
}

public class SBoundBox
{
	public float sx;
	public float sy;
	public float sz;
	public float ex;
	public float ey;
	public float ez;
	public int meshIndex;
	public int boneIndex;
}

public class CGraphicBase
{
//# Laniatus Games Studio Inc. |: This was formerly a static local variable declaration (not allowed in C#):
		private static uint GetAvailableTextureMemory_s_dwNextUpdateTime = 0;
//# Laniatus Games Studio Inc. |: This was formerly a static local variable declaration (not allowed in C#):
		private static uint GetAvailableTextureMemory_s_dwTexMemSize = 0;

		public static uint GetAvailableTextureMemory()
		{
			Debug.Assert(ms_lpd3dDevice != null && "CGraphicBase::GetAvailableTextureMemory - D3DDevice is EMPTY");

//# Laniatus Games Studio Inc. |: This static local variable declaration (not allowed in C#) has been moved just prior to the method:
//			static uint s_dwNextUpdateTime=0;
//# Laniatus Games Studio Inc. |: This static local variable declaration (not allowed in C#) has been moved just prior to the method:
//			static uint s_dwTexMemSize=0;

			uint dwCurTime = ELTimer_GetMSec();
			if (GetAvailableTextureMemory_s_dwNextUpdateTime < dwCurTime)
			{
				GetAvailableTextureMemory_s_dwNextUpdateTime = dwCurTime+5000;
				GetAvailableTextureMemory_s_dwTexMemSize = ms_lpd3dDevice.GetAvailableTextureMem();
			}

			return GetAvailableTextureMemory_s_dwTexMemSize;
		}

		public static _D3DMATRIX GetViewMatrix()
		{
			return ms_matView;
		}

		public static _D3DMATRIX GetIdentityMatrix()
		{
			return ms_matIdentity;
		}

		public const int DEFAULT_IB_LINE = 0;
		public const int DEFAULT_IB_LINE_TRI = 1;
		public const int DEFAULT_IB_LINE_RECT = 2;
		public const int DEFAULT_IB_LINE_CUBE = 3;
		public const int DEFAULT_IB_FILL_TRI = 4;
		public const int DEFAULT_IB_FILL_RECT = 5;
		public const int DEFAULT_IB_FILL_CUBE = 6;
		public const int DEFAULT_IB_NUM = 7;

		public CGraphicBase()
		{
		}

		public virtual void Dispose()
		{
		}

		public static IDirect3DVertexBuffer8 GetSmallPdtVertexBuffer()
		{
			return m_smallPdtVertexBuffer;
		}
		public static IDirect3DVertexBuffer8 GetLargePdtVertexBuffer()
		{
			return m_largePdtVertexBuffer;
		}

		public void SetSimpleCamera(float x, float y, float z, float pitch, float roll)
		{
			CCamera pCamera = CCameraManager.Instance().GetCurrentCamera();
			_D3DVECTOR vectorEye = new _D3DVECTOR(x, y, z);

			pCamera.SetViewParams(D3DXVECTOR3(0.0f, y, 0.0f), D3DXVECTOR3(0.0f, 0.0f, 0.0f), D3DXVECTOR3(0.0f, 0.0f, 1.0f));
			pCamera.RotateEyeAroundTarget(pitch, roll);
			pCamera.Move(vectorEye);

			UpdateViewMatrix();

			ms_lpd3dDevice.GetTransform(D3DTS_WORLD, ms_matWorld);
			D3DXMatrixMultiply(ms_matWorldView, ms_matWorld, ms_matView);
		}

		public void SetEyeCamera(float xEye, float yEye, float zEye, float xCenter, float yCenter, float zCenter, float xUp, float yUp, float zUp)
		{
			_D3DVECTOR vectorEye = new _D3DVECTOR(xEye, yEye, zEye);
			_D3DVECTOR vectorCenter = new _D3DVECTOR(xCenter, yCenter, zCenter);
			_D3DVECTOR vectorUp = new _D3DVECTOR(xUp, yUp, zUp);

			CCameraManager.Instance().GetCurrentCamera().SetViewParams(vectorEye, vectorCenter, vectorUp);
			UpdateViewMatrix();
		}

		public void SetAroundCamera(float distance, float pitch, float roll, float lookAtZ = 0.0f)
		{
			CCamera pCamera = CCameraManager.Instance().GetCurrentCamera();
			pCamera.SetViewParams(D3DXVECTOR3(0.0f, -distance, 0.0f), D3DXVECTOR3(0.0f, 0.0f, 0.0f), D3DXVECTOR3(0.0f, 0.0f, 1.0f));
			pCamera.RotateEyeAroundTarget(pitch, roll);
			_D3DVECTOR v3Target = pCamera.GetTarget();
			v3Target.z = lookAtZ;
			pCamera.SetTarget(v3Target);

			UpdateViewMatrix();

			ms_lpd3dDevice.GetTransform(D3DTS_WORLD, ms_matWorld);
			D3DXMatrixMultiply(ms_matWorldView, ms_matWorld, ms_matView);
		}

		public void SetPositionCamera(float fx, float fy, float fz, float distance, float pitch, float roll)
		{
			if (ms_dwWavingEndTime > CTimer.Instance().GetCurrentMillisecond())
			{
				if (ms_iWavingPower > 0)
				{
					fx += (float)(rand() % ms_iWavingPower) / 10.0f;
					fy += (float)(rand() % ms_iWavingPower) / 10.0f;
					fz += (float)(rand() % ms_iWavingPower) / 10.0f;
				}
			}

			CCamera pCamera = CCameraManager.Instance().GetCurrentCamera();
			if (pCamera == null)
			{
				return;
			}

			pCamera.SetViewParams(D3DXVECTOR3(0.0f, -distance, 0.0f), D3DXVECTOR3(0.0f, 0.0f, 0.0f), D3DXVECTOR3(0.0f, 0.0f, 1.0f));
			pitch = fMIN(80.0f, fMAX(-80.0f, pitch));
			pCamera.RotateEyeAroundTarget(pitch, roll);
			pCamera.Move(D3DXVECTOR3(fx, fy, fz));

			UpdateViewMatrix();

			(CStateManager.Instance()).GetTransform(D3DTS_WORLD, ms_matWorld);
			D3DXMatrixMultiply(ms_matWorldView, ms_matWorld, ms_matView);
		}

//# Laniatus Games Studio Inc. | TODO TASK: The implementation of the following method could not be found:
//		void MoveCamera(float fdeltax, float fdeltay, float fdeltaz);

		public void GetTargetPosition(ref float px, ref float py, ref float pz)
		{
			px = CCameraManager.Instance().GetCurrentCamera().GetTarget().x;
			py = CCameraManager.Instance().GetCurrentCamera().GetTarget().y;
			pz = CCameraManager.Instance().GetCurrentCamera().GetTarget().z;
		}

		public void GetCameraPosition(ref float px, ref float py, ref float pz)
		{
			px = CCameraManager.Instance().GetCurrentCamera().GetEye().x;
			py = CCameraManager.Instance().GetCurrentCamera().GetEye().y;
			pz = CCameraManager.Instance().GetCurrentCamera().GetEye().z;
		}

		public void SetOrtho2D(float hres, float vres, float zres)
		{
			D3DXMatrixOrthoOffCenterRH(ms_matProj, 0, hres, vres, 0, 0, zres);
			UpdateProjMatrix();
		}

		public void SetOrtho3D(float hres, float vres, float zmin, float zmax)
		{
			D3DXMatrixOrthoRH(ms_matProj, hres, vres, zmin, zmax);
			UpdateProjMatrix();
		}

		public void SetPerspective(float fov, float aspect, float nearz, float farz)
		{
			ms_fFieldOfView = fov;

			ms_fAspect = aspect;

			ms_fNearY = nearz;
			ms_fFarY = farz;

			D3DXMatrixPerspectiveFovRH(ms_matProj, ((fov) * (((float) 3.141592654f) / 180.0f)), ms_fAspect, nearz, farz);
			UpdateProjMatrix();
		}

		public float GetFOV()
		{
			return ms_fFieldOfView;
		}

		public void GetClipPlane(ref float fNearY, ref float fFarY)
		{
			fNearY = ms_fNearY;
			fFarY = ms_fFarY;
		}

		public void PushMatrix()
		{
			ms_lpd3dMatStack.Push();
		}

		public void MultMatrix(_D3DMATRIX pMat)
		{
			ms_lpd3dMatStack.MultMatrix(pMat);
		}

		public void MultMatrixLocal(_D3DMATRIX pMat)
		{
			ms_lpd3dMatStack.MultMatrixLocal(pMat);
		}

		public void Translate(float x, float y, float z)
		{
			ms_lpd3dMatStack.Translate(x, y, z);
		}

		public void Rotate(float degree, float x, float y, float z)
		{
			_D3DVECTOR vec = new _D3DVECTOR(x, y, z);
			ms_lpd3dMatStack.RotateAxis(vec, ((degree) * (((float) 3.141592654f) / 180.0f)));
		}

		public void RotateLocal(float degree, float x, float y, float z)
		{
			_D3DVECTOR vec = new _D3DVECTOR(x, y, z);
			ms_lpd3dMatStack.RotateAxisLocal(vec, ((degree) * (((float) 3.141592654f) / 180.0f)));
		}

		public void RotateYawPitchRollLocal(float fYaw, float fPitch, float fRoll)
		{
			ms_lpd3dMatStack.RotateYawPitchRollLocal(((fYaw) * (((float) 3.141592654f) / 180.0f)), ((fPitch) * (((float) 3.141592654f) / 180.0f)), ((fRoll) * (((float) 3.141592654f) / 180.0f)));
		}

		public void Scale(float x, float y, float z)
		{
			ms_lpd3dMatStack.Scale(x, y, z);
		}

		public void PopMatrix()
		{
			ms_lpd3dMatStack.Pop();
		}

		public void LoadMatrix(in _D3DMATRIX c_rSrcMatrix)
		{
			ms_lpd3dMatStack.LoadMatrix(c_rSrcMatrix);
		}

//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: void GetMatrix(struct _D3DMATRIX* pRetMatrix) const
		public void GetMatrix(_D3DMATRIX pRetMatrix)
		{
			Debug.Assert(ms_lpd3dMatStack != null);
			pRetMatrix = *ms_lpd3dMatStack.GetTop();
		}

//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: const struct _D3DMATRIX* GetMatrixPointer() const
		public _D3DMATRIX GetMatrixPointer()
		{
			Debug.Assert(ms_lpd3dMatStack != null);
			return ms_lpd3dMatStack.GetTop();
		}

		public void GetSphereMatrix(_D3DMATRIX pMatrix, float fValue = 0.1f)
		{
			D3DXMatrixIdentity(pMatrix);
			pMatrix._11 = fValue * ms_matWorldView._11;
			pMatrix._21 = fValue * ms_matWorldView._21;
			pMatrix._31 = fValue * ms_matWorldView._31;
			pMatrix._41 = fValue;
			pMatrix._12 = -fValue * ms_matWorldView._12;
			pMatrix._22 = -fValue * ms_matWorldView._22;
			pMatrix._32 = -fValue * ms_matWorldView._32;
			pMatrix._42 = -fValue;
		}

		public void InitScreenEffect()
		{
			ms_dwWavingEndTime = 0;
			ms_dwFlashingEndTime = 0;
			ms_iWavingPower = 0;
			ms_FlashingColor = D3DXCOLOR(0.0f, 0.0f, 0.0f, 0.0f);
		}

		public void SetScreenEffectWaving(float fDuringTime, int iPower)
		{
			ms_dwWavingEndTime = CTimer.Instance().GetCurrentMillisecond() + (int)(fDuringTime * 1000.0f);
			ms_iWavingPower = iPower;
		}

		public void SetScreenEffectFlashing(float fDuringTime, in D3DXCOLOR c_rColor)
		{
			ms_dwFlashingEndTime = CTimer.Instance().GetCurrentMillisecond() + (int)(fDuringTime * 1000.0f);
			ms_FlashingColor = c_rColor;
		}

		public uint GetColor(float r, float g, float b, float a = 1.0f)
		{
			byte[] argb = {(byte)(255.0f * b), (byte)(255.0f * g), (byte)(255.0f * r), (byte)(255.0f * a)};

			return ((uint) argb);
		}

		public uint GetFaceCount()
		{
			return ms_faceCount;
		}

		public void ResetFaceCount()
		{
			ms_faceCount = 0;
		}

		public int GetLastResult()
		{
			return ms_hLastResult;
		}

		public void UpdateProjMatrix()
		{
			(CStateManager.Instance()).SetTransform(D3DTS_PROJECTION, ms_matProj);
		}

		public void UpdateViewMatrix()
		{
			CCamera pkCamera = CCameraManager.Instance().GetCurrentCamera();
			if (pkCamera == null)
			{
				return;
			}

			ms_matView = pkCamera.GetViewMatrix();
			(CStateManager.Instance()).SetTransform(D3DTS_VIEW, ms_matView);

			D3DXMatrixInverse(ms_matInverseView, null, ms_matView);
			ms_matInverseViewYAxis._11 = ms_matInverseView._11;
			ms_matInverseViewYAxis._12 = ms_matInverseView._12;
			ms_matInverseViewYAxis._21 = ms_matInverseView._21;
			ms_matInverseViewYAxis._22 = ms_matInverseView._22;
		}

		public void SetViewport(uint dwX, uint dwY, uint dwWidth, uint dwHeight, float fMinZ, float fMaxZ)
		{
			ms_Viewport.X = dwX;
			ms_Viewport.Y = dwY;
			ms_Viewport.Width = dwWidth;
			ms_Viewport.Height = dwHeight;
			ms_Viewport.MinZ = fMinZ;
			ms_Viewport.MaxZ = fMaxZ;
		}

		public static void GetBackBufferSize(ref uint puWidth, ref uint puHeight)
		{
			puWidth = ms_d3dPresentParameter.BackBufferWidth;
			puHeight = ms_d3dPresentParameter.BackBufferHeight;
		}

		public static bool IsTLVertexClipping()
		{
			if ((ms_d3dCaps.PrimitiveMiscCaps & D3DPMISCCAPS_CLIPTLVERTS) != 0)
			{
				return true;
			}

			return false;
		}

		public static bool IsFastTNL()
		{
			if ((ms_dwD3DBehavior & D3DCREATE_HARDWARE_VERTEXPROCESSING) != 0 || (ms_dwD3DBehavior & D3DCREATE_MIXED_VERTEXPROCESSING) != 0)
			{
				if (ms_d3dCaps.VertexShaderVersion > D3DVS_VERSION(1,0))
				{
					return true;
				}
			}
			return false;
		}

		public static bool IsLowTextureMemory()
		{
			return ms_isLowTextureMemory;
		}

		public static bool IsHighTextureMemory()
		{
			return ms_isHighTextureMemory;
		}

		public static void SetDefaultIndexBuffer(uint eDefIB)
		{
			if (eDefIB >= DEFAULT_IB_NUM)
			{
				return;
			}

			(CStateManager.Instance()).SetIndices(ms_alpd3dDefIB[eDefIB], 0);
		}

		public static bool SetPDTStream(SPDTVertexRaw pSrcVertices, uint uVtxCount)
		{
			if (uVtxCount == 0)
			{
				return false;
			}

			Debug.Assert(uVtxCount <= LARGE_PDT_VERTEX_BUFFER_SIZE);

			if (uVtxCount == 0)
			{
				return false;
			}

			IDirect3DVertexBuffer8 vb = null;

			if (uVtxCount <= SMALL_PDT_VERTEX_BUFFER_SIZE)
			{
				vb = GetSmallPdtVertexBuffer();
			}
			else
			{
				vb = GetLargePdtVertexBuffer();
			}

			var bytes = sizeof(SPDTVertex) * uVtxCount;

			SPDTVertex dst;
			if (FAILED(vb.Lock(0, bytes, (byte) dst, D3DLOCK_DISCARD)))
			{
				(CStateManager.Instance()).SetStreamSource(0, null, 0);
				return false;
			}

//# Laniatus Games Studio Inc. | TODO TASK: The memory management function 'memcpy' has no equivalent in C#:
			memcpy(dst, pSrcVertices, bytes);
			vb.Unlock();

			(CStateManager.Instance()).SetStreamSource(0, vb, sizeof(SPDTVertex));
			return true;
		}

		public static bool SetPDTStream(SPDTVertex pVertices, uint uVtxCount)
		{
			return SetPDTStream((SPDTVertexRaw)pVertices, uVtxCount);
		}

		protected static _D3DMATRIX ms_matIdentity = new _D3DMATRIX();

		protected static _D3DMATRIX ms_matView = new _D3DMATRIX();
		protected static _D3DMATRIX ms_matProj = new _D3DMATRIX();
		protected static _D3DMATRIX ms_matInverseView = new _D3DMATRIX();
		protected static _D3DMATRIX ms_matInverseViewYAxis = new _D3DMATRIX();

		protected static _D3DMATRIX ms_matWorld = new _D3DMATRIX();
		protected static _D3DMATRIX ms_matWorldView = new _D3DMATRIX();

		protected void UpdatePipeLineMatrix()
		{
			UpdateProjMatrix();
			UpdateViewMatrix();
		}

		protected static ID3DXMesh ms_lpSphereMesh;
		protected static ID3DXMesh ms_lpCylinderMesh;

		protected static int ms_hLastResult = null;

		protected static int ms_iWidth;
		protected static int ms_iHeight;

		protected static uint ms_iD3DAdapterInfo = 0;
		protected static uint ms_iD3DDevInfo = 0;
		protected static uint ms_iD3DModeInfo = 0;
		protected static D3D_CDisplayModeAutoDetector ms_kD3DDetector = new D3D_CDisplayModeAutoDetector();

		protected static IntPtr ms_hWnd;
		protected static IntPtr ms_hDC;
		protected static LPDIRECT3D8 ms_lpd3d = null;
		protected static LPDIRECT3DDEVICE8 ms_lpd3dDevice = null;
		protected static @interface ID3DXMatrixStack * ms_lpd3dMatStack = new @interface();
		protected static D3DVIEWPORT8 ms_Viewport = new D3DVIEWPORT8();

		protected static uint ms_faceCount = 0;
		protected static D3DCAPS8 ms_d3dCaps = new D3DCAPS8();
		protected static D3DPRESENT_PARAMETERS ms_d3dPresentParameter = new D3DPRESENT_PARAMETERS();

		protected static uint ms_dwD3DBehavior = 0;
		protected static uint ms_ptVS = 0;
		protected static uint ms_pntVS = 0;
		protected static uint ms_pnt2VS = 0;

		protected static _D3DMATRIX ms_matScreen0 = new _D3DMATRIX();
		protected static _D3DMATRIX ms_matScreen1 = new _D3DMATRIX();
		protected static _D3DMATRIX ms_matScreen2 = new _D3DMATRIX();

		protected static _D3DVECTOR ms_vtPickRayOrig = new _D3DVECTOR();
		protected static _D3DVECTOR ms_vtPickRayDir = new _D3DVECTOR();

		protected static float ms_fFieldOfView;
		protected static float ms_fAspect;
		protected static float ms_fNearY;
		protected static float ms_fFarY;

		protected static uint ms_dwWavingEndTime;
		protected static int ms_iWavingPower;
		protected static uint ms_dwFlashingEndTime;
		protected static D3DXCOLOR ms_FlashingColor = new D3DXCOLOR();

		 protected static CRay ms_Ray = new CRay();

		protected static bool ms_bSupportDXT = true;
		protected static bool ms_isLowTextureMemory = false;
		protected static bool ms_isHighTextureMemory = false;

		protected const int PDT_VERTEX_NUM = 16;
		protected const int PDT_VERTEXBUFFER_NUM = 100;


		protected static IDirect3DVertexBuffer8 m_smallPdtVertexBuffer;
		protected static IDirect3DVertexBuffer8 m_largePdtVertexBuffer;
		protected static LPDIRECT3DINDEXBUFFER8[] ms_alpd3dDefIB = Arrays.InitializeWithDefaultInstances<LPDIRECT3DINDEXBUFFER8>(DEFAULT_IB_NUM);
}