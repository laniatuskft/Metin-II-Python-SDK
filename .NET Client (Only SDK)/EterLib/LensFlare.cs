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

public class CFlare
{
	public void Draw(float fBrightScale, int nWidth, int nHeight, int nX, int nY)
	{
		(CStateManager.Instance()).SaveRenderState(D3DRS_DESTBLEND, D3DBLEND_ONE);

		float fDX = (float)nX - (float)nWidth / 2.0f;
		float fDY = (float)nY - (float)nHeight / 2.0f;

		(CStateManager.Instance()).SetTexture(1, null);
		(CStateManager.Instance()).SetVertexShader(D3DFVF_XYZ | D3DFVF_DIFFUSE | D3DFVF_TEX1);

		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLORARG1, D3DTA_TEXTURE);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLORARG2, D3DTA_DIFFUSE);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLOROP, D3DTOP_MODULATE);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_ALPHAARG1, D3DTA_TEXTURE);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_ALPHAARG2, D3DTA_DIFFUSE);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_ALPHAOP, D3DTOP_MODULATE);

		for (uint LaniatusDefVariables = 0; LaniatusDefVariables < m_vFlares.size(); LaniatusDefVariables++)
		{
			float fCenterX = (float)nX - (m_vFlares[LaniatusDefVariables].m_fPosition + 1.0f) * fDX;
			float fCenterY = (float)nY - (m_vFlares[LaniatusDefVariables].m_fPosition + 1.0f) * fDY;
			float fW = m_vFlares[LaniatusDefVariables].m_fWidth;

			D3DXCOLOR d3dColor = new D3DXCOLOR(m_vFlares[LaniatusDefVariables].m_pColor[0] * fBrightScale, m_vFlares[LaniatusDefVariables].m_pColor[1] * fBrightScale, m_vFlares[LaniatusDefVariables].m_pColor[2] * fBrightScale, m_vFlares[LaniatusDefVariables].m_pColor[3] * fBrightScale);

			(CStateManager.Instance()).SetTexture(0, m_vFlares[LaniatusDefVariables].m_imageInstance.GetTexturePointer().GetD3DTexture());

			SVertex[] vertices = Arrays.InitializeWithDefaultInstances<SVertex>(4);

			vertices[0].u = 0.0f;
			vertices[0].v = 0.0f;
			vertices[0].x = fCenterX - fW;
			vertices[0].y = fCenterY - fW;
			vertices[0].z = 0.0f;
			vertices[0].color = d3dColor;

			vertices[1].u = 0.0f;
			vertices[1].v = 1.0f;
			vertices[1].x = fCenterX - fW;
			vertices[1].y = fCenterY + fW;
			vertices[1].z = 0.0f;
			vertices[1].color = d3dColor;

			vertices[2].u = 1.0f;
			vertices[2].v = 0.0f;
			vertices[2].x = fCenterX + fW;
			vertices[2].y = fCenterY - fW;
			vertices[2].z = 0.0f;
			vertices[2].color = d3dColor;

			vertices[3].u = 1.0f;
			vertices[3].v = 1.0f;
			vertices[3].x = fCenterX + fW;
			vertices[3].y = fCenterY + fW;
			vertices[3].z = 0.0f;
			vertices[3].color = d3dColor;

			(CStateManager.Instance()).DrawPrimitiveUP(D3DPT_TRIANGLESTRIP, 2, vertices, sizeof(SVertex));
		}

		(CStateManager.Instance()).RestoreRenderState(D3DRS_DESTBLEND);
	}

	public void Init(string strPath)
	{
		int LaniatusDefVariables = 0;

		while (g_strFiles[LaniatusDefVariables] != "")
		{
			CResource pResource = CResourceManager.Instance().GetResourcePointer((strPath + "/" + new string(g_strFiles[LaniatusDefVariables])).c_str());

			if (!pResource.IsType(CGraphicImage.Type()))
			{
				Debug.Assert(false);
			}

			SFlarePiece pPiece = new SFlarePiece();

			pPiece.m_imageInstance.SetImagePointer((CGraphicImage) pResource);
			pPiece.m_fPosition = g_fPosition[LaniatusDefVariables];
			pPiece.m_fWidth = g_fWidth[LaniatusDefVariables];
			pPiece.m_pColor = g_afColors[LaniatusDefVariables];

			m_vFlares.push_back(pPiece);
			LaniatusDefVariables++;
		}
	}

	public CFlare()
	{
	}

	public virtual void Dispose()
	{
	}

	private class SFlarePiece
	{
		public SFlarePiece()
		{
			this.m_fPosition = 0.0f;
			this.m_fWidth = 0.0f;
			this.m_pColor = null;
		}
	public CGraphicImageInstance m_imageInstance = new CGraphicImageInstance();
	public float m_fPosition;
	public float m_fWidth;
	public float[] m_pColor;
	}

	private List<SFlarePiece > m_vFlares = new List<SFlarePiece >();
}

public class CLensFlare : CScreen
{
	public CLensFlare()
	{
		this.m_fSunSize = 0;
		this.m_fBeforeBright = 0.0f;
		this.m_fAfterBright = 0.0f;
		this.m_bFlareVisible = false;
		this.m_bDrawFlare = true;
		this.m_bDrawBrightScreen = true;
		this.m_bEnabled = true;
		this.m_bShowMainFlare = true;
		this.m_fMaxBrightness = 1.0f;
		m_pControlPixels = new float[c_nDepthTestDimension * c_nDepthTestDimension];
		m_pTestPixels = new float[c_nDepthTestDimension * c_nDepthTestDimension];
		m_afColor[0] = m_afColor[1] = m_afColor[2] = 1.0f;
	}

	public virtual void Dispose()
	{
		Arrays.DeleteArray(m_pControlPixels);
		Arrays.DeleteArray(m_pTestPixels);
	}

	public void Compute(in _D3DVECTOR c_rv3LightDirection)
	{
		float[] afSunPos = new float[3];

		_D3DVECTOR v3Target = CCameraManager.Instance().GetCurrentCamera().GetTarget();

		afSunPos[0] = v3Target.x - c_rv3LightDirection.x * 99999999.0f;
		afSunPos[1] = v3Target.y - c_rv3LightDirection.y * 99999999.0f;
		afSunPos[2] = v3Target.z - c_rv3LightDirection.z * 99999999.0f;

		float fX;
		float fY;
		ProjectPosition(afSunPos[0], afSunPos[1], afSunPos[2], fX, fY);

		SetFlareLocation(fX, fY);

		float fSunVectorMagnitude = sqrtf(afSunPos[0] * afSunPos[0] + afSunPos[1] * afSunPos[1] + afSunPos[2] * afSunPos[2]);
		float[] afSunVector = new float[3];
		afSunVector[0] = -afSunPos[0] / fSunVectorMagnitude;
		afSunVector[1] = -afSunPos[1] / fSunVectorMagnitude;
		afSunVector[2] = -afSunPos[2] / fSunVectorMagnitude;

		float[] afCameraDirection = new float[3];
		afCameraDirection[0] = ms_matView._13;
		afCameraDirection[1] = ms_matView._23;
		afCameraDirection[2] = ms_matView._33;


		float fDotProduct = (afSunVector[0] * afCameraDirection[0]) + (afSunVector[1] * afCameraDirection[1]) + (afSunVector[2] * afCameraDirection[2]);

		if (acosf(fDotProduct) < 0.5f * ((float) 3.141592654f))
		{
			SetVisible(true);
		}
		else
		{
			SetVisible(false);
		}

		fX /= ms_Viewport.Width;
		fY /= ms_Viewport.Height;

		float fDistance = sqrtf(((0.5f - fX) * (0.5f - fX)) + ((0.5f - fY) * (0.5f - fY)));
		float fBeforeBright = Interpolate(0.0f, c_fHalfMaxBright, 1.0f - (fDistance * c_fDistanceScale));
		float fAfterBright = Interpolate(0.0f, 1.0f, 1.0f - (fDistance * c_fDistanceScale));

		SetBrightnesses(fBeforeBright, fAfterBright);
	}

	public void DrawBeforeFlare()
	{
		if (!m_bFlareVisible || !m_bEnabled || !m_bShowMainFlare)
		{
			return;
		}

		if (m_SunFlareImageInstance.IsEmpty())
		{
			return;
		}

		_D3DMATRIX matProj = new _D3DMATRIX();
		D3DXMatrixOrthoOffCenterRH(matProj, 0.0f, 1.0f, 1.0f, 0.0f, -1.0f, 1.0f);
		(CStateManager.Instance()).SaveTransform(D3DTS_PROJECTION, matProj);
		(CStateManager.Instance()).SaveTransform(D3DTS_VIEW, ms_matIdentity);

		_D3DMATRIX matWorld = new _D3DMATRIX();
		D3DXMatrixTranslation(matWorld, m_afFlarePos[0], m_afFlarePos[1], 0.0f);
		(CStateManager.Instance()).SetTransform(D3DTS_WORLD, matWorld);

		(CStateManager.Instance()).SaveRenderState(D3DRS_LIGHTING, false);
		(CStateManager.Instance()).SaveRenderState(D3DRS_ZENABLE, false);
		(CStateManager.Instance()).SaveRenderState(D3DRS_ZWRITEENABLE, false);
		(CStateManager.Instance()).SaveRenderState(D3DRS_CULLMODE, D3DCULL_NONE);
		(CStateManager.Instance()).SaveRenderState(D3DRS_SHADEMODE, D3DSHADE_FLAT);
		(CStateManager.Instance()).SaveRenderState(D3DRS_ALPHATESTENABLE, false);
		(CStateManager.Instance()).SaveRenderState(D3DRS_ALPHABLENDENABLE, true);
		(CStateManager.Instance()).SaveRenderState(D3DRS_SRCBLEND, D3DBLEND_SRCALPHA);
		(CStateManager.Instance()).SaveRenderState(D3DRS_DESTBLEND, D3DBLEND_INVSRCALPHA);

		float fAspectRatio = ms_Viewport.Width / (float)ms_Viewport.Height;
		float fHeight = m_fSunSize * fAspectRatio;
		D3DXCOLOR color = new D3DXCOLOR(1.0f, 1.0f, 1.0f, 1.0f);

		SVertex[] vertices = Arrays.InitializeWithDefaultInstances<SVertex>(4);
		vertices[0].x = -m_fSunSize;
		vertices[0].y = -fHeight;
		vertices[0].z = 0.0f;
		vertices[0].color = color;
		vertices[0].u = 0.0f;
		vertices[0].v = 0.0f;

		vertices[1].x = -m_fSunSize;
		vertices[1].y = fHeight;
		vertices[1].z = 0.0f;
		vertices[1].color = color;
		vertices[1].u = 0.0f;
		vertices[1].v = 1.0f;

		vertices[2].x = m_fSunSize;
		vertices[2].y = -fHeight;
		vertices[2].z = 0.0f;
		vertices[2].color = color;
		vertices[2].u = 1.0f;
		vertices[2].v = 0.0f;

		vertices[3].x = m_fSunSize;
		vertices[3].y = fHeight;
		vertices[3].z = 0.0f;
		vertices[3].color = color;
		vertices[3].u = 1.0f;
		vertices[3].v = 1.0f;

		(CStateManager.Instance()).SetTexture(0, m_SunFlareImageInstance.GetTexturePointer().GetD3DTexture());
		(CStateManager.Instance()).SetTexture(1, null);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLOROP, D3DTOP_MODULATE);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLORARG1, D3DTA_TEXTURE);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLORARG2, D3DTA_DIFFUSE);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_ALPHAOP, D3DTOP_SELECTARG1);
		(CStateManager.Instance()).SetTextureStageState(0, D3DTSS_COLORARG1, D3DTA_TEXTURE);

		(CStateManager.Instance()).SetVertexShader(D3DFVF_XYZ | D3DFVF_DIFFUSE | D3DFVF_TEX1);
		(CStateManager.Instance()).DrawPrimitiveUP(D3DPT_TRIANGLESTRIP, 2, vertices, sizeof(SVertex));

		(CStateManager.Instance()).RestoreRenderState(D3DRS_LIGHTING);
		(CStateManager.Instance()).RestoreRenderState(D3DRS_ZENABLE);
		(CStateManager.Instance()).RestoreRenderState(D3DRS_ZWRITEENABLE);
		(CStateManager.Instance()).RestoreRenderState(D3DRS_CULLMODE);
		(CStateManager.Instance()).RestoreRenderState(D3DRS_SHADEMODE);
		(CStateManager.Instance()).RestoreRenderState(D3DRS_ALPHATESTENABLE);
		(CStateManager.Instance()).RestoreRenderState(D3DRS_ALPHABLENDENABLE);
		(CStateManager.Instance()).RestoreRenderState(D3DRS_SRCBLEND);
		(CStateManager.Instance()).RestoreRenderState(D3DRS_DESTBLEND);

		(CStateManager.Instance()).RestoreTransform(D3DTS_VIEW);
		(CStateManager.Instance()).RestoreTransform(D3DTS_PROJECTION);
	}

	public void DrawAfterFlare()
	{
		if (m_bEnabled && m_fAfterBright != 0.0f && m_bDrawBrightScreen)
		{
			SetDiffuseColor(m_afColor[0], m_afColor[1], m_afColor[2], m_fAfterBright);
			RenderBar2d(0.0f, 0.0f, 1024.0f, 1024.0f);
		}
	}

	public void DrawFlare()
	{
		if (m_bEnabled && m_bFlareVisible && m_bDrawFlare && m_fAfterBright != 0.0f)
		{
			(CStateManager.Instance()).SaveRenderState(D3DRS_LIGHTING, false);
			(CStateManager.Instance()).SaveRenderState(D3DRS_ZENABLE, false);
			(CStateManager.Instance()).SaveRenderState(D3DRS_CULLMODE, D3DCULL_NONE);
			(CStateManager.Instance()).SaveRenderState(D3DRS_ALPHATESTENABLE, false);
			(CStateManager.Instance()).SaveRenderState(D3DRS_ALPHABLENDENABLE, true);

			_D3DMATRIX matProj = new _D3DMATRIX();
			D3DXMatrixOrthoOffCenterRH(matProj, 0.0f, ms_Viewport.Width, ms_Viewport.Height, 0.0f, -1.0f, 1.0f);
			(CStateManager.Instance()).SaveTransform(D3DTS_PROJECTION, matProj);
			(CStateManager.Instance()).SaveTransform(D3DTS_VIEW, ms_matIdentity);

			(CStateManager.Instance()).SetTransform(D3DTS_WORLD, ms_matIdentity);
			DrawAfterFlare();

			m_cFlare.Draw(m_fAfterBright, ms_Viewport.Width, ms_Viewport.Height, (int)m_afFlareWinPos[0], (int)m_afFlareWinPos[1]);

			(CStateManager.Instance()).RestoreRenderState(D3DRS_LIGHTING);
			(CStateManager.Instance()).RestoreRenderState(D3DRS_ZENABLE);
			(CStateManager.Instance()).RestoreRenderState(D3DRS_CULLMODE);
			(CStateManager.Instance()).RestoreRenderState(D3DRS_ALPHABLENDENABLE);
			(CStateManager.Instance()).RestoreRenderState(D3DRS_ALPHATESTENABLE);

			(CStateManager.Instance()).RestoreTransform(D3DTS_PROJECTION);
			(CStateManager.Instance()).RestoreTransform(D3DTS_VIEW);
		}
	}

	public void SetMainFlare(string strSunFile, float fSunSize)
	{
		if (m_bEnabled && m_bShowMainFlare)
		{
			m_fSunSize = fSunSize;
			CResource pResource = CResourceManager.Instance().GetResourcePointer(strSunFile);

			if (!pResource.IsType(CGraphicImage.Type()))
			{
				Debug.Assert(false);
			}

			m_SunFlareImageInstance.SetImagePointer((CGraphicImage) pResource);
		}
	}

	public void Initialize(string strPath)
	{
		if (m_bEnabled)
		{
			m_cFlare.Init(strPath);
		}
	}

	public void SetFlareLocation(double dX, double dY)
	{
		if (m_bEnabled)
		{
			m_afFlareWinPos[0] = (float)dX;
			m_afFlareWinPos[1] = (float)dY;

			m_afFlarePos[0] = (float)dX / ms_Viewport.Width;
			m_afFlarePos[1] = (float)dY / ms_Viewport.Height;
		}
	}

	public void SetVisible(bool bState)
	{
		m_bFlareVisible = bState;
	}
	public bool IsVisible()
	{
		return m_bFlareVisible;
	}

	public void SetBrightnesses(float fBeforeBright, float fAfterBright)
	{
		if (m_bEnabled)
		{
			m_fBeforeBright = fBeforeBright;
			m_fAfterBright = fAfterBright;

			ClampBrightness();
		}
	}

	public void ReadControlPixels()
	{
		if (m_bEnabled)
		{
			ReadDepthPixels(m_pControlPixels);
		}
	}

	public void AdjustBrightness()
	{
		if (m_bEnabled)
		{
			ReadDepthPixels(m_pTestPixels);

			int nDifferent = 0;

			for (int LaniatusDefVariables = 0; LaniatusDefVariables < c_nDepthTestDimension * c_nDepthTestDimension; ++i)
			{
				if (m_pTestPixels[LaniatusDefVariables] != m_pControlPixels[LaniatusDefVariables])
				{
					++nDifferent;
				}
			}

			float fAdjust = ((float)nDifferent / (c_nDepthTestDimension * c_nDepthTestDimension));
			fAdjust = sqrtf(fAdjust) * 0.85f;
			m_fAfterBright *= 1.0f - fAdjust;
		}
	}

	public void CharacterizeFlare(bool bEnabled, bool bShowMainFlare, float fMaxBrightness, in D3DXCOLOR c_rColor)
	{
		m_bEnabled = bEnabled;
		m_bShowMainFlare = bShowMainFlare;
		m_fMaxBrightness = fMaxBrightness;

		m_afColor[0] = c_rColor.r;
		m_afColor[1] = c_rColor.g;
		m_afColor[2] = c_rColor.b;
	}

	protected float Interpolate(float fStart, float fEnd, float fPercent)
	{
		return fStart + (fEnd - fStart) * fPercent;
	}

	private float[] m_afFlarePos = new float[2];
	private float[] m_afFlareWinPos = new float[2];
	private float m_fBeforeBright;
	private float m_fAfterBright;
	private bool m_bFlareVisible;
	private bool m_bDrawFlare;
	private bool m_bDrawBrightScreen;
	private float m_fSunSize;
	private CFlare m_cFlare = new CFlare();
	private float[] m_pControlPixels;
	private float[] m_pTestPixels;
	private bool m_bEnabled;
	private bool m_bShowMainFlare;
	private float m_fMaxBrightness;
	private float[] m_afColor = new float[4];

	private CGraphicImageInstance m_SunFlareImageInstance = new CGraphicImageInstance();

	private void ReadDepthPixels(ref float pPixels)
	{

	}

	private void ClampBrightness()
	{
		if (m_fBeforeBright < 0.0f)
		{
			m_fBeforeBright = 0.0f;
		}
		else if (m_fBeforeBright > 1.0f)
		{
			m_fBeforeBright = 1.0f;
		}

		m_fBeforeBright *= m_fMaxBrightness;

		if (m_fAfterBright < 0.0f)
		{
			m_fAfterBright = 0.0f;
		}
		else if (m_fAfterBright > 1.0f)
		{
			m_fAfterBright = 1.0f;
		}

		m_fAfterBright *= m_fMaxBrightness;
	}
}