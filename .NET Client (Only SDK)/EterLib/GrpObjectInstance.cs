using System.Collections.Generic;
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

public class CGraphicObjectInstance : CGraphicCollisionObject
{
		public CGraphicObjectInstance()
		{
			m_CullingHandle = 0;
			Initialize();
		}

		public virtual void Dispose()
		{
			Initialize();
		}

//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: virtual int GetType() const = 0;
		public abstract int GetType();

//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: const struct _D3DVECTOR & GetPosition() const
		public _D3DVECTOR GetPosition()
		{
			return m_v3Position;
		}

//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: const struct _D3DVECTOR & GetScale() const
		public _D3DVECTOR GetScale()
		{
			return m_v3Scale;
		}

		public float GetRotation()
		{
			return GetRoll();
		}

		public float GetYaw()
		{
			return m_fYaw;
		}

		public float GetPitch()
		{
			return m_fPitch;
		}

		public float GetRoll()
		{
			return m_fRoll;
		}

		public void SetPosition(float x, float y, float z)
		{
			m_v3Position.x = x;
			m_v3Position.y = y;
			m_v3Position.z = z;
		}

		public void SetPosition(in _D3DVECTOR newposition)
		{
			m_v3Position = newposition;
		}

		public void SetScale(float x, float y, float z)
		{
			m_v3Scale.x = x;
			m_v3Scale.y = y;
			m_v3Scale.z = z;
		}

		public void SetRotation(float fRotation)
		{
			m_fYaw = 0;
			m_fPitch = 0;
			m_fRoll = fRotation;

			D3DXMatrixRotationZ(m_mRotation, ((fRotation) * (((float) 3.141592654f) / 180.0f)));
		}

		public void SetRotation(float fYaw, float fPitch, float fRoll)
		{
			m_fYaw = fYaw;
			m_fPitch = fPitch;
			m_fRoll = fRoll;

			D3DXMatrixRotationYawPitchRoll(m_mRotation, ((fYaw) * (((float) 3.141592654f) / 180.0f)), ((fPitch) * (((float) 3.141592654f) / 180.0f)), ((fRoll) * (((float) 3.141592654f) / 180.0f)));
		}

		public void SetRotationQuaternion(in D3DXQUATERNION q)
		{
			D3DXMatrixRotationQuaternion(m_mRotation, q);
		}

		public void SetRotationMatrix(in _D3DMATRIX m)
		{
			m_mRotation = m;
		}

		public void Clear()
		{
			if (m_CullingHandle)
			{
				CCullingManager.Instance().Unregister(m_CullingHandle);
				m_CullingHandle = null;
			}

			ClearHeightInstance();

			m_isVisible = true;

			m_v3Position.x = m_v3Position.y = m_v3Position.z = 0.0f;
			m_v3Scale.x = m_v3Scale.y = m_v3Scale.z = 1.0f;
			m_fYaw = m_fPitch = m_fRoll = 0.0f;
			D3DXMatrixIdentity(m_worldMatrix);

			m_v3ScaleAcce.x = m_v3ScaleAcce.y = m_v3ScaleAcce.z = 0.0f;
			m_bAttachedAcceRace = 0;
			D3DXMatrixIdentity(m_matAbsoluteTrans);
			D3DXMatrixIdentity(m_matScale);
			D3DXMatrixIdentity(m_matScaleWorld);

			ZeroMemory(m_abyPortalID, sizeof(m_abyPortalID));

			OnClear();
		}

		public void Update()
		{
			OnUpdate();

			UpdateBoundingSphere();
		}

		public bool Render()
		{
			if (!isShow())
			{
				return false;
			}

			OnRender();
			return true;
		}

		public void BlendRender()
		{
			if (!isShow())
			{
				return;
			}

			OnBlendRender();
		}

		public void RenderToShadowMap()
		{
			if (!isShow())
			{
				return;
			}

			OnRenderToShadowMap();
		}

		public void RenderShadow()
		{
			if (!isShow())
			{
				return;
			}

			OnRenderShadow();
		}

		public void RenderPCBlocker()
		{
			if (!isShow())
			{
				return;
			}

			OnRenderPCBlocker();
		}

		public void Deform()
		{
			if (!isShow())
			{
				return;
			}

			OnDeform();
		}

		public void Transform()
		{
			m_worldMatrix = m_matScaleWorld * m_mRotation;
			m_worldMatrix._41 += m_v3Position.x;
			m_worldMatrix._42 += m_v3Position.y;
			m_worldMatrix._43 += m_v3Position.z;
		}

		public void Show()
		{
			m_isVisible = true;
		}

		public void Hide()
		{
			m_isVisible = false;
		}

		public bool isShow()
		{
			return m_isVisible;
		}

		public void BlockCamera(bool bBlock)
		{
			m_BlockCamera = bBlock;
		}
		public bool BlockCamera()
		{
			return m_BlockCamera;
		}

		public bool isIntersect(in CRay c_rRay, ref float pu, ref float pv, ref float pt)
		{
			_D3DVECTOR v3Start = new _D3DVECTOR();
			_D3DVECTOR v3Dir = new _D3DVECTOR();
			float fRayRange;
			c_rRay.GetStartPoint(v3Start);
			c_rRay.GetDirection(v3Dir, fRayRange);

			_D3DVECTOR[] posVertices = Arrays.InitializeWithDefaultInstances<_D3DVECTOR>(8);

			posVertices[0] = TPosition(m_v3TBBoxMin.x, m_v3TBBoxMin.y, m_v3TBBoxMin.z);
			posVertices[1] = TPosition(m_v3TBBoxMax.x, m_v3TBBoxMin.y, m_v3TBBoxMin.z);
			posVertices[2] = TPosition(m_v3TBBoxMin.x, m_v3TBBoxMax.y, m_v3TBBoxMin.z);
			posVertices[3] = TPosition(m_v3TBBoxMax.x, m_v3TBBoxMax.y, m_v3TBBoxMin.z);
			posVertices[4] = TPosition(m_v3TBBoxMin.x, m_v3TBBoxMin.y, m_v3TBBoxMax.z);
			posVertices[5] = TPosition(m_v3TBBoxMax.x, m_v3TBBoxMin.y, m_v3TBBoxMax.z);
			posVertices[6] = TPosition(m_v3TBBoxMin.x, m_v3TBBoxMax.y, m_v3TBBoxMax.z);
			posVertices[7] = TPosition(m_v3TBBoxMax.x, m_v3TBBoxMax.y, m_v3TBBoxMax.z);

			ushort[] Indices = {0, 1, 2, 1, 3, 2, 2, 0, 6, 0, 4, 6, 0, 1, 4, 1, 5, 4, 1, 3, 5, 3, 7, 5, 3, 2, 7, 2, 6, 7, 4, 5, 6, 5, 7, 6};

			int triCount = 12;
//# Laniatus Games Studio Inc. | TODO TASK: Pointer arithmetic is detected on this variable, so pointers on this variable are left unchanged:
			ushort * pcurIdx = (ushort)Indices;

			while ((triCount--) != 0)
			{
				if (IntersectTriangle(v3Start, v3Dir, posVertices[pcurIdx[0]], posVertices[pcurIdx[1]], posVertices[pcurIdx[2]], pu, pv, pt))
				{
					return true;
				}

				pcurIdx += 3;
			}

			return false;
		}

		public D3DXVECTOR4 GetWTBBoxVertex(in byte c_rucNumTBBoxVertex)
		{
			return m_v4TBBox[c_rucNumTBBoxVertex];
		}

		public _D3DVECTOR GetTBBoxMin()
		{
			return m_v3TBBoxMin;
		}
		public _D3DVECTOR GetTBBoxMax()
		{
			return m_v3TBBoxMax;
		}
		public _D3DVECTOR GetBBoxMin()
		{
			return m_v3BBoxMin;
		}
		public _D3DVECTOR GetBBoxMax()
		{
			return m_v3BBoxMax;
		}

		 public _D3DMATRIX GetTransform()
		 {
			 return m_worldMatrix;
		 }

		public _D3DMATRIX GetWorldMatrix()
		{
			return m_worldMatrix;
		}

		public void SetPortal(uint dwIndex, int iID)
		{
			if (dwIndex >= PORTAL_ID_MAX_NUM)
			{
				Debug.Assert(dwIndex < PORTAL_ID_MAX_NUM);
				return;
			}

			m_abyPortalID[dwIndex] = iID;
		}

		public int GetPortal(uint dwIndex)
		{
			if (dwIndex >= PORTAL_ID_MAX_NUM)
			{
				Debug.Assert(dwIndex < PORTAL_ID_MAX_NUM);
				return 0;
			}

			return m_abyPortalID[dwIndex];
		}

		public void Initialize()
		{
			if (m_CullingHandle)
			{
				CCullingManager.Instance().Unregister(m_CullingHandle);
			}
			m_CullingHandle = 0;

			m_pHeightAttributeInstance = null;

			m_isVisible = true;

			m_BlockCamera = false;

			m_v3Position.x = m_v3Position.y = m_v3Position.z = 0.0f;
			m_v3Scale.x = m_v3Scale.y = m_v3Scale.z = 1.0f;
			m_fYaw = m_fPitch = m_fRoll = 0.0f;

			D3DXMatrixIdentity(m_worldMatrix);
			D3DXMatrixIdentity(m_mRotation);

			m_v3ScaleAcce.x = m_v3ScaleAcce.y = m_v3ScaleAcce.z = 0.0f;
			D3DXMatrixIdentity(m_matAbsoluteTrans);
			D3DXMatrixIdentity(m_matScale);
			D3DXMatrixIdentity(m_matScaleWorld);
			m_bActorRace = 0;

			OnInitialize();
		}

		public virtual void OnInitialize()
		{
			ZeroMemory(m_abyPortalID, sizeof(m_abyPortalID));
		}

		public void UpdateBoundingSphere()
		{
			if (m_CullingHandle)
			{
				Vector3d center = new Vector3d();
				float radius;
				GetBoundingSphere(center,radius);
				if (radius != m_CullingHandle.GetRadius())
				{
					m_CullingHandle.NewPosRadius(center,radius);
				}
				else
				{
					m_CullingHandle.NewPos(center);
				}
			}
		}

		public void RegisterBoundingSphere()
		{
			if (m_CullingHandle)
			{
				CCullingManager.Instance().Unregister(m_CullingHandle);
			}

			m_CullingHandle = CCullingManager.Instance().Register(this);
		}

		public abstract bool GetBoundingSphere(_D3DVECTOR v3Center, ref float fRadius);

		public abstract void OnRender();
		public abstract void OnBlendRender();
		public abstract void OnRenderToShadowMap();
		public abstract void OnRenderShadow();
		public abstract void OnRenderPCBlocker();
		public virtual void OnClear()
		{
		}
		public virtual void OnUpdate()
		{
		}
		public virtual void OnDeform()
		{
		}

		protected _D3DVECTOR m_v3Position = new _D3DVECTOR();
		protected _D3DVECTOR m_v3Scale = new _D3DVECTOR();

		protected float m_fYaw;
		protected float m_fPitch;
		protected float m_fRoll;

		protected _D3DMATRIX m_mRotation = new _D3DMATRIX();

		protected bool m_isVisible;
		protected _D3DMATRIX m_worldMatrix = new _D3DMATRIX();

		protected bool m_BlockCamera;

		protected D3DXVECTOR4[] m_v4TBBox = Arrays.InitializeWithDefaultInstances<D3DXVECTOR4>(8);
		protected _D3DVECTOR m_v3TBBoxMin = new _D3DVECTOR();
		protected _D3DVECTOR m_v3TBBoxMax = new _D3DVECTOR();
		protected _D3DVECTOR m_v3BBoxMin = new _D3DVECTOR();
		protected _D3DVECTOR m_v3BBoxMax = new _D3DVECTOR();

		protected byte[] m_abyPortalID = new byte[PORTAL_ID_MAX_NUM];
		protected byte m_bActorRace;

		protected SpherePack m_CullingHandle;

		public void AddCollision(CStaticCollisionData pscd, _D3DMATRIX pMat)
		{
			m_StaticCollisionInstanceVector.push_back(CBaseCollisionInstance.BuildCollisionInstance(pscd, pMat));
		}

		public void ClearCollision()
		{
			List<CBaseCollisionInstance>.Enumerator it;
			for (it = m_StaticCollisionInstanceVector.begin(); it.MoveNext();)
			{
				it.Current.Destroy();
			}
			m_StaticCollisionInstanceVector.clear();
		}

//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: bool CollisionDynamicSphere(const CDynamicSphereInstance & s) const
		public bool CollisionDynamicSphere(in CDynamicSphereInstance s)
		{
			List<CBaseCollisionInstance>.Enumerator it;
			for (it = m_StaticCollisionInstanceVector.begin(); it.MoveNext();)
			{
				if (it.Current.CollisionDynamicSphere(s))
				{
					return true;
				}
			}
			return false;
		}

//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: bool MovementCollisionDynamicSphere(const CDynamicSphereInstance & s) const
		public bool MovementCollisionDynamicSphere(in CDynamicSphereInstance s)
		{
			List<CBaseCollisionInstance>.Enumerator it;
			for (it = m_StaticCollisionInstanceVector.begin(); it.MoveNext();)
			{
				if (it.Current.MovementCollisionDynamicSphere(s))
				{
					return true;
				}
			}
			return false;
		}

//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: struct _D3DVECTOR GetCollisionMovementAdjust(const CDynamicSphereInstance & s) const
		public _D3DVECTOR GetCollisionMovementAdjust(in CDynamicSphereInstance s)
		{
			List<CBaseCollisionInstance>.Enumerator it;
			for (it = m_StaticCollisionInstanceVector.begin(); it.MoveNext();)
			{
				if (it.Current.MovementCollisionDynamicSphere(s))
				{
					return it.Current.GetCollisionMovementAdjust(s);
				}
			}

			return struct _D3DVECTOR(0.0f,0.0f,0.0f);
		}

		public void UpdateCollisionData(List<CStaticCollisionData> pscdVector = null)
		{
			ClearCollision();
			OnUpdateCollisionData(pscdVector);
		}

		protected List<CBaseCollisionInstance> m_StaticCollisionInstanceVector = new List<CBaseCollisionInstance>();
		protected abstract void OnUpdateCollisionData(List<CStaticCollisionData> pscdVector);

		public uint GetCollisionInstanceCount()
		{
			return (uint)m_StaticCollisionInstanceVector.size();
		}

		public CBaseCollisionInstance GetCollisionInstanceData(uint dwIndex)
		{
			if (dwIndex > m_StaticCollisionInstanceVector.size())
			{
				return null;
			}
			return m_StaticCollisionInstanceVector[dwIndex];
		}

		public void SetHeightInstance(CAttributeInstance pAttributeInstance)
		{
			m_pHeightAttributeInstance = pAttributeInstance;
		}

		public void ClearHeightInstance()
		{
			m_pHeightAttributeInstance = null;
		}

		public void UpdateHeightInstance(CAttributeInstance pAttributeInstance = null)
		{
			ClearHeightInstance();
			OnUpdateHeighInstance(pAttributeInstance);
		}

		public bool IsObjectHeight()
		{
			if (m_pHeightAttributeInstance)
			{
				return true;
			}

			return false;
		}

		public bool GetObjectHeight(float fX, float fY, ref float pfHeight)
		{
			if (!m_pHeightAttributeInstance)
			{
				return false;
			}

			return OnGetObjectHeight(fX, fY, pfHeight);
		}

		protected CAttributeInstance m_pHeightAttributeInstance;
		protected abstract void OnUpdateHeighInstance(CAttributeInstance pAttributeInstance);
		protected abstract bool OnGetObjectHeight(float fX, float fY, ref float pfHeight);

		public void SetScaleWorld(float x, float y, float z)
		{
			m_v3Scale.x = x;
			m_v3Scale.y = y;
			m_v3Scale.z = z;
			D3DXMatrixScaling(m_matScaleWorld, x, y, z);
		}

		public void SetAcceScale(float x, float y, float z)
		{
			m_v3ScaleAcce.x = x;
			m_v3ScaleAcce.y = y;
			m_v3ScaleAcce.z = z;
		}

		public void SetAcceScale(in _D3DVECTOR rv3Scale, byte bRace)
		{
			m_v3ScaleAcce = rv3Scale;
			m_bAttachedAcceRace = bRace;
		}

		protected byte m_bAttachedAcceRace;
		protected _D3DVECTOR m_v3ScaleAcce = new _D3DVECTOR();
		protected _D3DMATRIX m_matAbsoluteTrans = new _D3DMATRIX();
		protected _D3DMATRIX m_matScale = new _D3DMATRIX();
		protected _D3DMATRIX m_matScaleWorld = new _D3DMATRIX();
}
