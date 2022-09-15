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

public class CStreamData
{
		public CStreamData(LPDIRECT3DVERTEXBUFFER8 pStreamData = null, uint Stride = 0)
		{
			this.m_lpStreamData = pStreamData;
			this.m_Stride = Stride;
		}

//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: bool operator == (const CStreamData& rhs) const
		public static bool operator == (CStreamData ImpliedObject, in CStreamData rhs)
		{
			return ((m_lpStreamData == rhs.m_lpStreamData) && (m_Stride == rhs.m_Stride));
		}

		public LPDIRECT3DVERTEXBUFFER8 m_lpStreamData = new LPDIRECT3DVERTEXBUFFER8();
		public uint m_Stride;
}

public class CIndexData
{
		public CIndexData(LPDIRECT3DINDEXBUFFER8 pIndexData = null, uint BaseVertexIndex = 0)
		{
			this.m_lpIndexData = pIndexData;
			this.m_BaseVertexIndex = BaseVertexIndex;
		}

//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: bool operator == (const CIndexData& rhs) const
		public static bool operator == (CIndexData ImpliedObject, in CIndexData rhs)
		{
			return ((m_lpIndexData == rhs.m_lpIndexData) && (m_BaseVertexIndex == rhs.m_BaseVertexIndex));
		}

		public LPDIRECT3DINDEXBUFFER8 m_lpIndexData = new LPDIRECT3DINDEXBUFFER8();
		public uint m_BaseVertexIndex;
}

public enum eStateType
{
	STATE_MATERIAL = 0,
	STATE_RENDER,
	STATE_TEXTURE,
	STATE_TEXTURESTAGE,
	STATE_VSHADER,
	STATE_PSHADER,
	STATE_TRANSFORM,
	STATE_VCONSTANT,
	STATE_PCONSTANT,
	STATE_STREAM,
	STATE_INDEX
}

public class CStateID
{
		public CStateID(eStateType Type, uint dwValue0 = 0, uint dwValue1 = 0)
		{
			this.m_Type = Type;
			this.m_dwValue0 = dwValue0;
			this.m_dwValue1 = dwValue1;
		}

		public CStateID(eStateType Type, uint dwStage, D3DTEXTURESTAGESTATETYPE StageType)
		{
			this.m_Type = Type;
			this.m_dwStage = dwStage;
			this.m_TextureStageStateType = StageType;
		}

		public CStateID(eStateType Type, D3DRENDERSTATETYPE RenderType)
		{
			this.m_Type = Type;
			this.m_RenderStateType = RenderType;
		}

		public eStateType m_Type = new eStateType();

//# Laniatus Games Studio Inc. | TODO TASK: Unions are not supported in C#:
//		union
//		{
//			uint m_dwValue0;
//			uint m_dwStage;
//			D3DRENDERSTATETYPE m_RenderStateType;
//			D3DTRANSFORMSTATETYPE m_TransformStateType;
//		};

//# Laniatus Games Studio Inc. | TODO TASK: Unions are not supported in C#:
//		union
//		{
//			uint m_dwValue1;
//			D3DTEXTURESTAGESTATETYPE m_TextureStageStateType;
//		};
}


public class CStateManagerState
{
		public CStateManagerState()
		{
		}

		public void ResetState()
		{
			uint i;
			uint y;

			for (i = 0; LaniatusDefVariables < STATEMANAGER_MAX_RENDERSTATES; i++)
			{
				m_RenderStates[i] = 0x7FFFFFFF;
			}

			for (i = 0; LaniatusDefVariables < STATEMANAGER_MAX_STAGES; i++)
			{
				for (y = 0; y < STATEMANAGER_MAX_TEXTURESTATES; y++)
				{
					m_TextureStates[i][y] = 0x7FFFFFFF;
				}
			}

			for (i = 0; LaniatusDefVariables < STATEMANAGER_MAX_STREAMS; i++)
			{
				m_StreamData[i] = CStreamData();
			}

			m_IndexData = CIndexData();

			for (i = 0; LaniatusDefVariables < STATEMANAGER_MAX_STAGES; i++)
			{
				m_Textures[i] = null;
			}

			for (i = 0; LaniatusDefVariables < STATEMANAGER_MAX_TRANSFORMSTATES; i++)
			{
				D3DXMatrixIdentity(m_Matrices[i]);
			}

			for (i = 0; LaniatusDefVariables < STATEMANAGER_MAX_VCONSTANTS; i++)
			{
				m_VertexShaderConstants[i] = D3DXVECTOR4(0.0f, 0.0f, 0.0f, 0.0f);
			}

			for (i = 0; LaniatusDefVariables < STATEMANAGER_MAX_PCONSTANTS; i++)
			{
				m_PixelShaderConstants[i] = D3DXVECTOR4(0.0f, 0.0f, 0.0f, 0.0f);
			}

			m_dwPixelShader = 0;
			m_dwVertexShader = D3DFVF_XYZ;

			ZeroMemory(m_Matrices, sizeof(_D3DMATRIX) * STATEMANAGER_MAX_TRANSFORMSTATES);
		}

		public uint[] m_RenderStates = new uint[STATEMANAGER_MAX_RENDERSTATES];
		public uint[][] m_TextureStates = RectangularArrays.RectangularUintArray(STATEMANAGER_MAX_STAGES, STATEMANAGER_MAX_TEXTURESTATES);
		public D3DXVECTOR4[] m_VertexShaderConstants = Arrays.InitializeWithDefaultInstances<D3DXVECTOR4>(STATEMANAGER_MAX_VCONSTANTS);
		public D3DXVECTOR4[] m_PixelShaderConstants = Arrays.InitializeWithDefaultInstances<D3DXVECTOR4>(STATEMANAGER_MAX_PCONSTANTS);
		public LPDIRECT3DBASETEXTURE8[] m_Textures = Arrays.InitializeWithDefaultInstances<LPDIRECT3DBASETEXTURE8>(STATEMANAGER_MAX_STAGES);
		public uint m_dwPixelShader;
		public uint m_dwVertexShader;

		public _D3DMATRIX[] m_Matrices = Arrays.InitializeWithDefaultInstances<_D3DMATRIX>(STATEMANAGER_MAX_TRANSFORMSTATES);

		public D3DMATERIAL8 m_D3DMaterial = new D3DMATERIAL8();

		public CStreamData[] m_StreamData = Arrays.InitializeWithDefaultInstances<CStreamData>(STATEMANAGER_MAX_STREAMS);
		public CIndexData m_IndexData = new CIndexData();
}

public class CStateManager : CSingleton<CStateManager>
{
		public CStateManager(LPDIRECT3DDEVICE8 lpDevice)
		{
			this.m_lpD3DDev = null;
			m_bScene = false;
			m_dwBestMinFilter = D3DTEXF_LINEAR;
			m_dwBestMagFilter = D3DTEXF_LINEAR;
			SetDevice(lpDevice);
		}

		public virtual void Dispose()
		{
			if (m_lpD3DDev)
			{
				m_lpD3DDev.Release();
				m_lpD3DDev = null;
			}
		}

		public void SetDefaultState()
		{
			m_CurrentState.ResetState();
			m_CopyState.ResetState();
			m_ChipState.ResetState();

			m_bScene = false;
			m_bForce = true;

			_D3DMATRIX Identity = new _D3DMATRIX();
			D3DXMatrixIdentity(Identity);

			SetTransform(D3DTS_WORLD, Identity);
			SetTransform(D3DTS_VIEW, Identity);
			SetTransform(D3DTS_PROJECTION, Identity);

			D3DMATERIAL8 DefaultMat = new D3DMATERIAL8();
			ZeroMemory(DefaultMat, sizeof(D3DMATERIAL8));

			DefaultMat.Diffuse.r = 1.0f;
			DefaultMat.Diffuse.g = 1.0f;
			DefaultMat.Diffuse.b = 1.0f;
			DefaultMat.Diffuse.a = 1.0f;
			DefaultMat.Ambient.r = 1.0f;
			DefaultMat.Ambient.g = 1.0f;
			DefaultMat.Ambient.b = 1.0f;
			DefaultMat.Ambient.a = 1.0f;
			DefaultMat.Emissive.r = 0.0f;
			DefaultMat.Emissive.g = 0.0f;
			DefaultMat.Emissive.b = 0.0f;
			DefaultMat.Emissive.a = 0.0f;
			DefaultMat.Specular.r = 0.0f;
			DefaultMat.Specular.g = 0.0f;
			DefaultMat.Specular.b = 0.0f;
			DefaultMat.Specular.a = 0.0f;
			DefaultMat.Power = 0.0f;

			SetMaterial(DefaultMat);

			SetRenderState(D3DRS_DIFFUSEMATERIALSOURCE, D3DMCS_MATERIAL);
			SetRenderState(D3DRS_SPECULARMATERIALSOURCE, D3DMCS_MATERIAL);
			SetRenderState(D3DRS_AMBIENTMATERIALSOURCE, D3DMCS_MATERIAL);
			SetRenderState(D3DRS_EMISSIVEMATERIALSOURCE, D3DMCS_MATERIAL);

			SetRenderState(D3DRS_LINEPATTERN, 0xFFFFFFFF);
			SetRenderState(D3DRS_LASTPIXEL, false);
			SetRenderState(D3DRS_ALPHAREF, 1);
			SetRenderState(D3DRS_ALPHAFUNC, D3DCMP_GREATEREQUAL);
			SetRenderState(D3DRS_ZVISIBLE, false);
			SetRenderState(D3DRS_FOGSTART, 0);
			SetRenderState(D3DRS_FOGEND, 0);
			SetRenderState(D3DRS_FOGDENSITY, 0);
			SetRenderState(D3DRS_EDGEANTIALIAS, false);
			SetRenderState(D3DRS_ZBIAS, 0);
			SetRenderState(D3DRS_STENCILWRITEMASK, 0xFFFFFFFF);
			SetRenderState(D3DRS_AMBIENT, 0x00000000);
			SetRenderState(D3DRS_LOCALVIEWER, false);
			SetRenderState(D3DRS_NORMALIZENORMALS, false);
			SetRenderState(D3DRS_VERTEXBLEND, D3DVBF_DISABLE);
			SetRenderState(D3DRS_CLIPPLANEENABLE, 0);
			SetRenderState(D3DRS_SOFTWAREVERTEXPROCESSING, false);
			SetRenderState(D3DRS_MULTISAMPLEANTIALIAS, false);
			SetRenderState(D3DRS_MULTISAMPLEMASK, 0xFFFFFFFF);
			SetRenderState(D3DRS_INDEXEDVERTEXBLENDENABLE, false);
			SetRenderState(D3DRS_COLORWRITEENABLE, 0xFFFFFFFF);
			SetRenderState(D3DRS_FILLMODE, D3DFILL_SOLID);
			SetRenderState(D3DRS_SHADEMODE, D3DSHADE_GOURAUD);
			SetRenderState(D3DRS_CULLMODE, D3DCULL_CW);
			SetRenderState(D3DRS_ALPHABLENDENABLE, false);
			SetRenderState(D3DRS_BLENDOP, D3DBLENDOP_ADD);
			SetRenderState(D3DRS_SRCBLEND, D3DBLEND_SRCALPHA);
			SetRenderState(D3DRS_DESTBLEND, D3DBLEND_INVSRCALPHA);
			SetRenderState(D3DRS_FOGENABLE, false);
			SetRenderState(D3DRS_FOGCOLOR, 0xFF000000);
			SetRenderState(D3DRS_FOGTABLEMODE, D3DFOG_NONE);
			SetRenderState(D3DRS_FOGVERTEXMODE, D3DFOG_LINEAR);
			SetRenderState(D3DRS_RANGEFOGENABLE, false);
			SetRenderState(D3DRS_ZENABLE, true);
			SetRenderState(D3DRS_ZFUNC, D3DCMP_LESSEQUAL);
			SetRenderState(D3DRS_ZWRITEENABLE, true);
			SetRenderState(D3DRS_DITHERENABLE, true);
			SetRenderState(D3DRS_STENCILENABLE, false);
			SetRenderState(D3DRS_ALPHATESTENABLE, false);
			SetRenderState(D3DRS_CLIPPING, true);
			SetRenderState(D3DRS_LIGHTING, false);
			SetRenderState(D3DRS_SPECULARENABLE, false);
			SetRenderState(D3DRS_COLORVERTEX, false);
			SetRenderState(D3DRS_WRAP0, 0);
			SetRenderState(D3DRS_WRAP1, 0);
			SetRenderState(D3DRS_WRAP2, 0);
			SetRenderState(D3DRS_WRAP3, 0);
			SetRenderState(D3DRS_WRAP4, 0);
			SetRenderState(D3DRS_WRAP5, 0);
			SetRenderState(D3DRS_WRAP6, 0);
			SetRenderState(D3DRS_WRAP7, 0);

			SetTextureStageState(0, D3DTSS_COLOROP, D3DTOP_MODULATE);
			SetTextureStageState(0, D3DTSS_COLORARG1, D3DTA_TEXTURE);
			SetTextureStageState(0, D3DTSS_COLORARG2, D3DTA_CURRENT);
			SetTextureStageState(0, D3DTSS_ALPHAARG1, D3DTA_TEXTURE);
			SetTextureStageState(0, D3DTSS_ALPHAARG2, D3DTA_CURRENT);
			SetTextureStageState(0, D3DTSS_ALPHAOP, D3DTOP_SELECTARG1);

			SetTextureStageState(1, D3DTSS_COLOROP, D3DTOP_DISABLE);
			SetTextureStageState(1, D3DTSS_COLORARG1, D3DTA_TEXTURE);
			SetTextureStageState(1, D3DTSS_COLORARG2, D3DTA_DIFFUSE);
			SetTextureStageState(1, D3DTSS_ALPHAOP, D3DTOP_DISABLE);
			SetTextureStageState(1, D3DTSS_ALPHAARG1, D3DTA_TEXTURE);
			SetTextureStageState(1, D3DTSS_ALPHAARG2, D3DTA_DIFFUSE);

			SetTextureStageState(2, D3DTSS_COLOROP, D3DTOP_DISABLE);
			SetTextureStageState(2, D3DTSS_COLORARG1, D3DTA_TEXTURE);
			SetTextureStageState(2, D3DTSS_COLORARG2, D3DTA_DIFFUSE);
			SetTextureStageState(2, D3DTSS_ALPHAOP, D3DTOP_DISABLE);
			SetTextureStageState(2, D3DTSS_ALPHAARG1, D3DTA_TEXTURE);
			SetTextureStageState(2, D3DTSS_ALPHAARG2, D3DTA_DIFFUSE);

			SetTextureStageState(3, D3DTSS_COLOROP, D3DTOP_DISABLE);
			SetTextureStageState(3, D3DTSS_COLORARG1, D3DTA_TEXTURE);
			SetTextureStageState(3, D3DTSS_COLORARG2, D3DTA_DIFFUSE);
			SetTextureStageState(3, D3DTSS_ALPHAOP, D3DTOP_DISABLE);
			SetTextureStageState(3, D3DTSS_ALPHAARG1, D3DTA_TEXTURE);
			SetTextureStageState(3, D3DTSS_ALPHAARG2, D3DTA_DIFFUSE);

			SetTextureStageState(4, D3DTSS_COLOROP, D3DTOP_DISABLE);
			SetTextureStageState(4, D3DTSS_COLORARG1, D3DTA_TEXTURE);
			SetTextureStageState(4, D3DTSS_COLORARG2, D3DTA_DIFFUSE);
			SetTextureStageState(4, D3DTSS_ALPHAOP, D3DTOP_DISABLE);
			SetTextureStageState(4, D3DTSS_ALPHAARG1, D3DTA_TEXTURE);
			SetTextureStageState(4, D3DTSS_ALPHAARG2, D3DTA_DIFFUSE);

			SetTextureStageState(5, D3DTSS_COLOROP, D3DTOP_DISABLE);
			SetTextureStageState(5, D3DTSS_COLORARG1, D3DTA_TEXTURE);
			SetTextureStageState(5, D3DTSS_COLORARG2, D3DTA_DIFFUSE);
			SetTextureStageState(5, D3DTSS_ALPHAOP, D3DTOP_DISABLE);
			SetTextureStageState(5, D3DTSS_ALPHAARG1, D3DTA_TEXTURE);
			SetTextureStageState(5, D3DTSS_ALPHAARG2, D3DTA_DIFFUSE);

			SetTextureStageState(6, D3DTSS_COLOROP, D3DTOP_DISABLE);
			SetTextureStageState(6, D3DTSS_COLORARG1, D3DTA_TEXTURE);
			SetTextureStageState(6, D3DTSS_COLORARG2, D3DTA_DIFFUSE);
			SetTextureStageState(6, D3DTSS_ALPHAOP, D3DTOP_DISABLE);
			SetTextureStageState(6, D3DTSS_ALPHAARG1, D3DTA_TEXTURE);
			SetTextureStageState(6, D3DTSS_ALPHAARG2, D3DTA_DIFFUSE);

			SetTextureStageState(7, D3DTSS_COLOROP, D3DTOP_DISABLE);
			SetTextureStageState(7, D3DTSS_COLORARG1, D3DTA_TEXTURE);
			SetTextureStageState(7, D3DTSS_COLORARG2, D3DTA_DIFFUSE);
			SetTextureStageState(7, D3DTSS_ALPHAOP, D3DTOP_DISABLE);
			SetTextureStageState(7, D3DTSS_ALPHAARG1, D3DTA_TEXTURE);
			SetTextureStageState(7, D3DTSS_ALPHAARG2, D3DTA_DIFFUSE);

			SetTextureStageState(0, D3DTSS_TEXCOORDINDEX, 0);
			SetTextureStageState(1, D3DTSS_TEXCOORDINDEX, 1);
			SetTextureStageState(2, D3DTSS_TEXCOORDINDEX, 2);
			SetTextureStageState(3, D3DTSS_TEXCOORDINDEX, 3);
			SetTextureStageState(4, D3DTSS_TEXCOORDINDEX, 4);
			SetTextureStageState(5, D3DTSS_TEXCOORDINDEX, 5);
			SetTextureStageState(6, D3DTSS_TEXCOORDINDEX, 6);
			SetTextureStageState(7, D3DTSS_TEXCOORDINDEX, 7);

			SetTextureStageState(0, D3DTSS_MINFILTER, D3DTEXF_LINEAR);
			SetTextureStageState(0, D3DTSS_MAGFILTER, D3DTEXF_LINEAR);
			SetTextureStageState(0, D3DTSS_MIPFILTER, D3DTEXF_LINEAR);

			SetTextureStageState(1, D3DTSS_MINFILTER, D3DTEXF_LINEAR);
			SetTextureStageState(1, D3DTSS_MAGFILTER, D3DTEXF_LINEAR);
			SetTextureStageState(1, D3DTSS_MIPFILTER, D3DTEXF_LINEAR);

			SetTextureStageState(2, D3DTSS_MINFILTER, D3DTEXF_LINEAR);
			SetTextureStageState(2, D3DTSS_MAGFILTER, D3DTEXF_LINEAR);
			SetTextureStageState(2, D3DTSS_MIPFILTER, D3DTEXF_LINEAR);

			SetTextureStageState(3, D3DTSS_MINFILTER, D3DTEXF_LINEAR);
			SetTextureStageState(3, D3DTSS_MAGFILTER, D3DTEXF_LINEAR);
			SetTextureStageState(3, D3DTSS_MIPFILTER, D3DTEXF_LINEAR);

			SetTextureStageState(4, D3DTSS_MINFILTER, D3DTEXF_LINEAR);
			SetTextureStageState(4, D3DTSS_MAGFILTER, D3DTEXF_LINEAR);
			SetTextureStageState(4, D3DTSS_MIPFILTER, D3DTEXF_LINEAR);

			SetTextureStageState(5, D3DTSS_MINFILTER, D3DTEXF_LINEAR);
			SetTextureStageState(5, D3DTSS_MAGFILTER, D3DTEXF_LINEAR);
			SetTextureStageState(5, D3DTSS_MIPFILTER, D3DTEXF_LINEAR);

			SetTextureStageState(6, D3DTSS_MINFILTER, D3DTEXF_LINEAR);
			SetTextureStageState(6, D3DTSS_MAGFILTER, D3DTEXF_LINEAR);
			SetTextureStageState(6, D3DTSS_MIPFILTER, D3DTEXF_LINEAR);

			SetTextureStageState(7, D3DTSS_MINFILTER, D3DTEXF_LINEAR);
			SetTextureStageState(7, D3DTSS_MAGFILTER, D3DTEXF_LINEAR);
			SetTextureStageState(7, D3DTSS_MIPFILTER, D3DTEXF_LINEAR);

			SetTextureStageState(0, D3DTSS_ADDRESSU, D3DTADDRESS_WRAP);
			SetTextureStageState(0, D3DTSS_ADDRESSV, D3DTADDRESS_WRAP);
			SetTextureStageState(1, D3DTSS_ADDRESSU, D3DTADDRESS_WRAP);
			SetTextureStageState(1, D3DTSS_ADDRESSV, D3DTADDRESS_WRAP);
			SetTextureStageState(2, D3DTSS_ADDRESSU, D3DTADDRESS_WRAP);
			SetTextureStageState(2, D3DTSS_ADDRESSV, D3DTADDRESS_WRAP);
			SetTextureStageState(3, D3DTSS_ADDRESSU, D3DTADDRESS_WRAP);
			SetTextureStageState(3, D3DTSS_ADDRESSV, D3DTADDRESS_WRAP);
			SetTextureStageState(4, D3DTSS_ADDRESSU, D3DTADDRESS_WRAP);
			SetTextureStageState(4, D3DTSS_ADDRESSV, D3DTADDRESS_WRAP);
			SetTextureStageState(5, D3DTSS_ADDRESSU, D3DTADDRESS_WRAP);
			SetTextureStageState(5, D3DTSS_ADDRESSV, D3DTADDRESS_WRAP);
			SetTextureStageState(6, D3DTSS_ADDRESSU, D3DTADDRESS_WRAP);
			SetTextureStageState(6, D3DTSS_ADDRESSV, D3DTADDRESS_WRAP);
			SetTextureStageState(7, D3DTSS_ADDRESSU, D3DTADDRESS_WRAP);
			SetTextureStageState(7, D3DTSS_ADDRESSV, D3DTADDRESS_WRAP);

			SetTextureStageState(0, D3DTSS_TEXTURETRANSFORMFLAGS, 0);
			SetTextureStageState(1, D3DTSS_TEXTURETRANSFORMFLAGS, 0);
			SetTextureStageState(2, D3DTSS_TEXTURETRANSFORMFLAGS, 0);
			SetTextureStageState(3, D3DTSS_TEXTURETRANSFORMFLAGS, 0);
			SetTextureStageState(4, D3DTSS_TEXTURETRANSFORMFLAGS, 0);
			SetTextureStageState(5, D3DTSS_TEXTURETRANSFORMFLAGS, 0);
			SetTextureStageState(6, D3DTSS_TEXTURETRANSFORMFLAGS, 0);
			SetTextureStageState(7, D3DTSS_TEXTURETRANSFORMFLAGS, 0);

			SetTexture(0, null);
			SetTexture(1, null);
			SetTexture(2, null);
			SetTexture(3, null);
			SetTexture(4, null);
			SetTexture(5, null);
			SetTexture(6, null);
			SetTexture(7, null);

			SetPixelShader(0);
			SetVertexShader(D3DFVF_XYZ);

			D3DXVECTOR4[] av4Null = Arrays.InitializeWithDefaultInstances<D3DXVECTOR4>(STATEMANAGER_MAX_VCONSTANTS);
//# Laniatus Games Studio Inc. | TODO TASK: The memory management function 'memset' has no equivalent in C#:
			memset(av4Null, 0, sizeof(D3DXVECTOR4));
			SetVertexShaderConstant(0, av4Null, STATEMANAGER_MAX_VCONSTANTS);
			SetPixelShaderConstant(0, av4Null, STATEMANAGER_MAX_PCONSTANTS);

			m_bForce = false;

#if DEBUG
			int i;
			int j;
			for (i = 0; LaniatusDefVariables < STATEMANAGER_MAX_RENDERSTATES; i++)
			{
				m_bRenderStateSavingFlag[i] = false;
			}

			for (j = 0; j < STATEMANAGER_MAX_TRANSFORMSTATES; j++)
			{
				m_bTransformSavingFlag[j] = false;
			}

			for (j = 0; j < STATEMANAGER_MAX_STAGES; ++j)
			{
				for (i = 0; LaniatusDefVariables < STATEMANAGER_MAX_TEXTURESTATES; ++i)
				{
					m_bTextureStageStateSavingFlag[j][i] = false;
				}
			}
#endif DEBUG
		}

		public void Restore()
		{
			int i;
			int j;

			m_bForce = true;

			for (i = 0; LaniatusDefVariables < STATEMANAGER_MAX_RENDERSTATES; ++i)
			{
				SetRenderState(D3DRENDERSTATETYPE(i), m_CurrentState.m_RenderStates[i]);
			}

			for (i = 0; LaniatusDefVariables < STATEMANAGER_MAX_STAGES; ++i)
			{
				for (j = 0; j < STATEMANAGER_MAX_TEXTURESTATES; ++j)
				{
					SetTextureStageState(i, D3DTEXTURESTAGESTATETYPE(j), m_CurrentState.m_TextureStates[i][j]);
				}
			}

			for (i = 0; LaniatusDefVariables < STATEMANAGER_MAX_STAGES; ++i)
			{
				SetTexture(i, m_CurrentState.m_Textures[i]);
			}

			m_bForce = false;
		}

		public bool BeginScene()
		{
			m_bScene = true;

			_D3DMATRIX m4Proj = new _D3DMATRIX();
			_D3DMATRIX m4View = new _D3DMATRIX();
			_D3DMATRIX m4World = new _D3DMATRIX();
			GetTransform(D3DTS_WORLD, m4World);
			GetTransform(D3DTS_PROJECTION, m4Proj);
			GetTransform(D3DTS_VIEW, m4View);
			SetTransform(D3DTS_WORLD, m4World);
			SetTransform(D3DTS_PROJECTION, m4Proj);
			SetTransform(D3DTS_VIEW, m4View);

			if (FAILED(m_lpD3DDev.BeginScene()))
			{
				return false;
			}
			return true;
		}

		public void EndScene()
		{
			m_lpD3DDev.EndScene();
			m_bScene = false;
		}

		public void SaveMaterial()
		{
			m_CopyState.m_D3DMaterial = m_CurrentState.m_D3DMaterial;
		}

		public void SaveMaterial(D3DMATERIAL8 pMaterial)
		{
			m_CopyState.m_D3DMaterial = m_CurrentState.m_D3DMaterial;
			SetMaterial(pMaterial);
		}

		public void RestoreMaterial()
		{
			SetMaterial(m_CopyState.m_D3DMaterial);
		}

		public void SetMaterial(D3DMATERIAL8 pMaterial)
		{
			m_lpD3DDev.SetMaterial(pMaterial);
			m_CurrentState.m_D3DMaterial = pMaterial;
		}

		public void GetMaterial(D3DMATERIAL8 pMaterial)
		{
			pMaterial = m_CurrentState.m_D3DMaterial;
		}

		public void SetLight(uint index, CONST D3DLIGHT8 pLight)
		{
			Debug.Assert(index < SLightData.LIGHT_NUM);
			m_kLightData.m_akD3DLight[index] = pLight;

			m_lpD3DDev.SetLight(index, pLight);
		}

		public void GetLight(uint index, D3DLIGHT8 pLight)
		{
			Debug.Assert(index < 8);
			pLight = m_kLightData.m_akD3DLight[index];
		}

		public void SaveRenderState(D3DRENDERSTATETYPE Type, uint dwValue)
		{
#if DEBUG
			if (m_bRenderStateSavingFlag[Type])
			{
				Tracef(" CStateManager::SaveRenderState - This render state is already saved [%d, %d]\n", Type, dwValue);
				Debug.Assert(!" This render state is already saved!");
			}
			m_bRenderStateSavingFlag[Type] = true;
#endif DEBUG

			m_CopyState.m_RenderStates[Type] = m_CurrentState.m_RenderStates[Type];
			SetRenderState(Type, dwValue);
		}

		public void RestoreRenderState(D3DRENDERSTATETYPE Type)
		{
#if DEBUG
			if (!m_bRenderStateSavingFlag[Type])
			{
				Tracef(" CStateManager::SaveRenderState - This render state was not saved [%d, %d]\n", Type);
				Debug.Assert(!" This render state was not saved!");
			}
			m_bRenderStateSavingFlag[Type] = false;
#endif DEBUG

			SetRenderState(Type, m_CopyState.m_RenderStates[Type]);
		}

		public void SetRenderState(D3DRENDERSTATETYPE Type, uint Value)
		{
			if (m_CurrentState.m_RenderStates[Type] == Value)
			{
				return;
			}

			m_lpD3DDev.SetRenderState(Type, Value);
			m_CurrentState.m_RenderStates[Type] = Value;
		}

		public void GetRenderState(D3DRENDERSTATETYPE Type, ref uint pdwValue)
		{
			pdwValue = m_CurrentState.m_RenderStates[Type];
		}

		public void SaveTexture(uint dwStage, LPDIRECT3DBASETEXTURE8 pTexture)
		{
			m_CopyState.m_Textures[dwStage] = m_CurrentState.m_Textures[dwStage];
			SetTexture(dwStage, pTexture);
		}

		public void RestoreTexture(uint dwStage)
		{
			SetTexture(dwStage, m_CopyState.m_Textures[dwStage]);
		}

		public void SetTexture(uint dwStage, LPDIRECT3DBASETEXTURE8 pTexture)
		{
			if (pTexture == m_CurrentState.m_Textures[dwStage])
			{
				return;
			}

			m_lpD3DDev.SetTexture(dwStage, pTexture);
			m_CurrentState.m_Textures[dwStage] = pTexture;
		}

		public void GetTexture(uint dwStage, LPDIRECT3DBASETEXTURE8 ppTexture)
		{
			ppTexture = m_CurrentState.m_Textures[dwStage];
		}

		public void SaveTextureStageState(uint dwStage, D3DTEXTURESTAGESTATETYPE Type, uint dwValue)
		{
#if DEBUG
			if (m_bTextureStageStateSavingFlag[dwStage][Type])
			{
				Tracef(" CStateManager::SaveTextureStageState - This texture stage state is already saved [%d, %d]\n", dwStage, Type);
				Debug.Assert(!" This texture stage state is already saved!");
			}
			m_bTextureStageStateSavingFlag[dwStage][Type] = true;
#endif DEBUG
			m_CopyState.m_TextureStates[dwStage][Type] = m_CurrentState.m_TextureStates[dwStage][Type];
			SetTextureStageState(dwStage, Type, dwValue);
		}

		public void RestoreTextureStageState(uint dwStage, D3DTEXTURESTAGESTATETYPE Type)
		{
#if DEBUG
			if (!m_bTextureStageStateSavingFlag[dwStage][Type])
			{
				Tracef(" CStateManager::RestoreTextureStageState - This texture stage state was not saved [%d, %d]\n", dwStage, Type);
				Debug.Assert(!" This texture stage state was not saved!");
			}
			m_bTextureStageStateSavingFlag[dwStage][Type] = false;
#endif DEBUG
			SetTextureStageState(dwStage, Type, m_CopyState.m_TextureStates[dwStage][Type]);
		}

		public void SetTextureStageState(uint dwStage, D3DTEXTURESTAGESTATETYPE Type, uint dwValue)
		{
			if (m_CurrentState.m_TextureStates[dwStage][Type] == dwValue)
			{
				return;
			}

			m_lpD3DDev.SetTextureStageState(dwStage, Type, dwValue);
			m_CurrentState.m_TextureStates[dwStage][Type] = dwValue;
		}

		public void GetTextureStageState(uint dwStage, D3DTEXTURESTAGESTATETYPE Type, ref uint pdwValue)
		{
			pdwValue = m_CurrentState.m_TextureStates[dwStage][Type];
		}

		public void SetBestFiltering(uint dwStage)
		{
			SetTextureStageState(dwStage, D3DTSS_MINFILTER, m_dwBestMinFilter);
			SetTextureStageState(dwStage, D3DTSS_MAGFILTER, m_dwBestMagFilter);
			SetTextureStageState(dwStage, D3DTSS_MIPFILTER, D3DTEXF_LINEAR);
		}

		public void SaveVertexShader(uint dwShader)
		{
			m_CopyState.m_dwVertexShader = m_CurrentState.m_dwVertexShader;
			SetVertexShader(dwShader);
		}

		public void RestoreVertexShader()
		{
			SetVertexShader(m_CopyState.m_dwVertexShader);
		}

		public void SetVertexShader(uint dwShader)
		{
			if (m_CurrentState.m_dwVertexShader == dwShader)
			{
				return;
			}

			m_lpD3DDev.SetVertexShader(dwShader);
			m_CurrentState.m_dwVertexShader = dwShader;
		}

		public void GetVertexShader(ref uint pdwShader)
		{
			pdwShader = m_CurrentState.m_dwVertexShader;
		}

		public void SavePixelShader(uint dwShader)
		{
			m_CopyState.m_dwPixelShader = m_CurrentState.m_dwPixelShader;
			SetPixelShader(dwShader);
		}

		public void RestorePixelShader()
		{
			SetPixelShader(m_CopyState.m_dwPixelShader);
		}

		public void SetPixelShader(uint dwShader)
		{
			if (m_CurrentState.m_dwPixelShader == dwShader)
			{
				return;
			}

			m_lpD3DDev.SetPixelShader(dwShader);
			m_CurrentState.m_dwPixelShader = dwShader;
		}

		public void GetPixelShader(ref uint pdwShader)
		{
			pdwShader = m_CurrentState.m_dwPixelShader;
		}

		public void SaveTransform(D3DTRANSFORMSTATETYPE Type, D3DMATRIX pMatrix)
		{
#if DEBUG
			if (m_bTransformSavingFlag[Type])
			{
				Tracef(" CStateManager::SaveTransform - This transform is already saved [%d]\n", Type);
				Debug.Assert(!" This trasform is already saved!");
			}
			m_bTransformSavingFlag[Type] = true;
#endif DEBUG

			m_CopyState.m_Matrices[Type] = m_CurrentState.m_Matrices[Type];
			SetTransform(Type, (_D3DMATRIX)pMatrix);
		}

		public void RestoreTransform(D3DTRANSFORMSTATETYPE Type)
		{
#if DEBUG
			if (!m_bTransformSavingFlag[Type])
			{
				Tracef(" CStateManager::RestoreTransform - This transform was not saved [%d]\n", Type);
				Debug.Assert(!" This render state was not saved!");
			}
			m_bTransformSavingFlag[Type] = false;
#endif DEBUG

			SetTransform(Type, m_CopyState.m_Matrices[Type]);
		}

		public void SetTransform(D3DTRANSFORMSTATETYPE Type, D3DMATRIX pMatrix)
		{
			if (m_bScene)
			{
				m_lpD3DDev.SetTransform(Type, pMatrix);
			}
			else
			{
				Debug.Assert(D3DTS_VIEW == Type || D3DTS_PROJECTION == Type || D3DTS_WORLD == Type);
			}

			m_CurrentState.m_Matrices[Type] = pMatrix;
		}

		public void GetTransform(D3DTRANSFORMSTATETYPE Type, D3DMATRIX pMatrix)
		{
			pMatrix = m_CurrentState.m_Matrices[Type];
		}

		public void SaveVertexShaderConstant(uint dwRegister, CONST object pConstantData, uint dwConstantCount)
		{
			uint i;

			for (i = 0; LaniatusDefVariables < dwConstantCount; i++)
			{
				Debug.Assert((dwRegister + i) < STATEMANAGER_MAX_VCONSTANTS);
				m_CopyState.m_VertexShaderConstants[dwRegister + i] = m_CurrentState.m_VertexShaderConstants[dwRegister + i];
			}

			SetVertexShaderConstant(dwRegister, pConstantData, dwConstantCount);
		}

		public void RestoreVertexShaderConstant(uint dwRegister, uint dwConstantCount)
		{
			SetVertexShaderConstant(dwRegister, m_CopyState.m_VertexShaderConstants[dwRegister], dwConstantCount);
		}

		public void SetVertexShaderConstant(uint dwRegister, CONST object pConstantData, uint dwConstantCount)
		{
			m_lpD3DDev.SetVertexShaderConstant(dwRegister, pConstantData, dwConstantCount);

			for (uint LaniatusDefVariables = 0; LaniatusDefVariables < dwConstantCount; i++)
			{
				Debug.Assert((dwRegister + i) < STATEMANAGER_MAX_VCONSTANTS);
				m_CurrentState.m_VertexShaderConstants[dwRegister + i] = *(((D3DXVECTOR4)pConstantData) + i);
			}
		}

		public void SavePixelShaderConstant(uint dwRegister, CONST object pConstantData, uint dwConstantCount)
		{
			uint i;

			for (i = 0; LaniatusDefVariables < dwConstantCount; i++)
			{
				Debug.Assert((dwRegister + i) < STATEMANAGER_MAX_VCONSTANTS);
				m_CopyState.m_PixelShaderConstants[dwRegister + i] = *(((D3DXVECTOR4)pConstantData) + i);
			}

			SetPixelShaderConstant(dwRegister, pConstantData, dwConstantCount);
		}

		public void RestorePixelShaderConstant(uint dwRegister, uint dwConstantCount)
		{
			SetPixelShaderConstant(dwRegister, m_CopyState.m_PixelShaderConstants[dwRegister], dwConstantCount);
		}

		public void SetPixelShaderConstant(uint dwRegister, CONST object pConstantData, uint dwConstantCount)
		{
			m_lpD3DDev.SetPixelShaderConstant(dwRegister, pConstantData, dwConstantCount);

			for (uint LaniatusDefVariables = 0; LaniatusDefVariables < dwConstantCount; i++)
			{
				Debug.Assert((dwRegister + i) < STATEMANAGER_MAX_VCONSTANTS);
				m_CurrentState.m_PixelShaderConstants[dwRegister + i] = *(((D3DXVECTOR4)pConstantData) + i);
			}
		}

		public void SaveStreamSource(uint StreamNumber, LPDIRECT3DVERTEXBUFFER8 pStreamData, uint Stride)
		{
			m_CopyState.m_StreamData[StreamNumber] = m_CurrentState.m_StreamData[StreamNumber];
			SetStreamSource(StreamNumber, pStreamData, Stride);
		}

		public void RestoreStreamSource(uint StreamNumber)
		{
			SetStreamSource(StreamNumber, m_CopyState.m_StreamData[StreamNumber].m_lpStreamData, m_CopyState.m_StreamData[StreamNumber].m_Stride);
		}

		public void SetStreamSource(uint StreamNumber, LPDIRECT3DVERTEXBUFFER8 pStreamData, uint Stride)
		{
			CStreamData kStreamData = new CStreamData(pStreamData, Stride);
			if (m_CurrentState.m_StreamData[StreamNumber] == kStreamData)
			{
				return;
			}

			m_lpD3DDev.SetStreamSource(StreamNumber, pStreamData, Stride);
			m_CurrentState.m_StreamData[StreamNumber] = kStreamData;
		}

		public void SaveIndices(LPDIRECT3DINDEXBUFFER8 pIndexData, uint BaseVertexIndex)
		{
			m_CopyState.m_IndexData = m_CurrentState.m_IndexData;
			SetIndices(pIndexData, BaseVertexIndex);
		}

		public void RestoreIndices()
		{
			SetIndices(m_CopyState.m_IndexData.m_lpIndexData, m_CopyState.m_IndexData.m_BaseVertexIndex);
		}

		public void SetIndices(LPDIRECT3DINDEXBUFFER8 pIndexData, uint BaseVertexIndex)
		{
			CIndexData kIndexData = new CIndexData(pIndexData, BaseVertexIndex);

			if (m_CurrentState.m_IndexData == kIndexData)
			{
				return;
			}

			m_lpD3DDev.SetIndices(pIndexData, BaseVertexIndex);
			m_CurrentState.m_IndexData = kIndexData;
		}

		public int DrawPrimitive(D3DPRIMITIVETYPE PrimitiveType, uint StartVertex, uint PrimitiveCount)
		{
			return (m_lpD3DDev.DrawPrimitive(PrimitiveType, StartVertex, PrimitiveCount));
		}

		public int DrawPrimitiveUP(D3DPRIMITIVETYPE PrimitiveType, uint PrimitiveCount, object pVertexStreamZeroData, uint VertexStreamZeroStride)
		{
			m_CurrentState.m_StreamData[0] = null;
			return (m_lpD3DDev.DrawPrimitiveUP(PrimitiveType, PrimitiveCount, pVertexStreamZeroData, VertexStreamZeroStride));
		}

		public int DrawIndexedPrimitive(D3DPRIMITIVETYPE PrimitiveType, uint minIndex, uint NumVertices, uint startIndex, uint primCount)
		{
			return (m_lpD3DDev.DrawIndexedPrimitive(PrimitiveType, minIndex, NumVertices, startIndex, primCount));
		}

		public int DrawIndexedPrimitiveUP(D3DPRIMITIVETYPE PrimitiveType, uint MinVertexIndex, uint NumVertexIndices, uint PrimitiveCount, CONST object pIndexData, D3DFORMAT IndexDataFormat, CONST object pVertexStreamZeroData, uint VertexStreamZeroStride)
		{
			m_CurrentState.m_IndexData = null;
			m_CurrentState.m_StreamData[0] = null;
			return (m_lpD3DDev.DrawIndexedPrimitiveUP(PrimitiveType, MinVertexIndex, NumVertexIndices, PrimitiveCount, pIndexData, IndexDataFormat, pVertexStreamZeroData, VertexStreamZeroStride));
		}

		public uint GetRenderState(D3DRENDERSTATETYPE Type)
		{
			return m_CurrentState.m_RenderStates[Type];
		}

		private void SetDevice(LPDIRECT3DDEVICE8 lpDevice)
		{
			Debug.Assert(lpDevice);
			lpDevice.AddRef();

			if (m_lpD3DDev)
			{
				m_lpD3DDev.Release();
				m_lpD3DDev = null;
			}

			m_lpD3DDev = lpDevice;

			D3DCAPS8 d3dCaps = new D3DCAPS8();
			m_lpD3DDev.GetDeviceCaps(d3dCaps);

			if ((d3dCaps.TextureFilterCaps & D3DPTFILTERCAPS_MAGFANISOTROPIC) != 0)
			{
				m_dwBestMagFilter = D3DTEXF_ANISOTROPIC;
			}
			else
			{
				m_dwBestMagFilter = D3DTEXF_LINEAR;
			}

			if ((d3dCaps.TextureFilterCaps & D3DPTFILTERCAPS_MINFANISOTROPIC) != 0)
			{
				m_dwBestMinFilter = D3DTEXF_ANISOTROPIC;
			}
			else
			{
				m_dwBestMinFilter = D3DTEXF_LINEAR;
			}

			uint dwMax = d3dCaps.MaxAnisotropy;
			dwMax = dwMax < 4 ? dwMax : 4;

			for (int LaniatusDefVariables = 0; LaniatusDefVariables < 8; ++i)
			{
				m_lpD3DDev.SetTextureStageState(i, D3DTSS_MAXANISOTROPY, dwMax);
			}

			SetDefaultState();
		}

		private CStateManagerState m_ChipState = new CStateManagerState();
		private CStateManagerState m_CurrentState = new CStateManagerState();
		private CStateManagerState m_CopyState = new CStateManagerState();
		private List<CStateID> m_DirtyStates = new List<CStateID>();
		private bool m_bForce;
		private bool m_bScene;
		private uint m_dwBestMinFilter;
		private uint m_dwBestMagFilter;
		private LPDIRECT3DDEVICE8 m_lpD3DDev = new LPDIRECT3DDEVICE8();

#if DEBUG
		private bool[] m_bRenderStateSavingFlag = new bool[STATEMANAGER_MAX_RENDERSTATES];
		private bool[][] m_bTextureStageStateSavingFlag = RectangularArrays.RectangularBoolArray(STATEMANAGER_MAX_STAGES, STATEMANAGER_MAX_TEXTURESTATES);
		private bool[] m_bTransformSavingFlag = new bool[STATEMANAGER_MAX_TRANSFORMSTATES];
#endif DEBUG
}

//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define STATEMANAGER (CStateManager::Instance())



//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define StateManager_Assert(a) assert(a)

public class SLightData
{
	public const int LIGHT_NUM = 8;
	public D3DLIGHT8[] m_akD3DLight = Arrays.InitializeWithDefaultInstances<D3DLIGHT8>(LIGHT_NUM);
}