/*
 * jmemsys.h
 *
 * Copyright (C) 1992-1997, Thomas G. Lane.
 * This file is part of the Independent JPEG Group's software.
 * For conditions of distribution and use, see the accompanying README file.
 *
 * This include file defines the interface between the system-independent
 * and system-dependent portions of the JPEG memory manager.  No other
 * modules need include it.  (The system-independent portion is jmemmgr.c;
 * there are several different versions of the system-dependent portion.)
 *
 * This file works as-is for the system-dependent memory managers supplied
 * in the IJG distribution.  You may need to modify it if you write a
 * custom memory manager.  If system-dependent changes are needed in
 * this file, the best method is to #ifdef them based on a configuration
 * symbol supplied in jconfig.h, as we have done with USE_MSDOS_MEMMGR
 * and USE_MAC_MEMMGR.
 */


/* Short forms of external names for systems with brain-damaged linkers. */

#if NEED_SHORT_EXTERNAL_NAMES
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jpeg_get_small jGetSmall
#define jpeg_get_small
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jpeg_free_small jFreeSmall
#define jpeg_free_small
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jpeg_get_large jGetLarge
#define jpeg_get_large
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jpeg_free_large jFreeLarge
#define jpeg_free_large
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jpeg_mem_available jMemAvail
#define jpeg_mem_available
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jpeg_open_backing_store jOpenBackStore
#define jpeg_open_backing_store
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jpeg_mem_init jMemInit
#define jpeg_mem_init
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jpeg_mem_term jMemTerm
#define jpeg_mem_term
#endif // NEED_SHORT_EXTERNAL_NAMES


/*
 * These two functions are used to allocate and release small chunks of
 * memory.  (Typically the total amount requested through jpeg_get_small is
 * no more than 20K or so; this will be requested in chunks of a few K each.)
 * Behavior should be the same as for the standard library functions malloc
 * and free; in particular, jpeg_get_small must return NULL on failure.
 * On most systems, these ARE malloc and free.  jpeg_free_small is passed the
 * size of the object being freed, just in case it's needed.
 * On an 80x86 machine using small-data memory model, these manage near heap.
 */

//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
EXTERN(object*) jGetSmall JPP((j_common_ptr cinfo, size_t sizeofobject));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
EXTERN() jFreeSmall JPP((j_common_ptr cinfo, object * @object, size_t sizeofobject));

/*
 * These two functions are used to allocate and release large chunks of
 * memory (up to the total free space designated by jpeg_mem_available).
 * The interface is the same as above, except that on an 80x86 machine,
 * far pointers are used.  On most other machines these are identical to
 * the jpeg_get/free_small routines; but we keep them separate anyway,
 * in case a different allocation strategy is desirable for large chunks.
 */

//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
EXTERN(void FAR *) jGetLarge JPP((j_common_ptr cinfo, size_t sizeofobject));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
EXTERN() jFreeLarge JPP((j_common_ptr cinfo, void FAR * @object, size_t sizeofobject));

/*
 * The macro MAX_ALLOC_CHUNK designates the maximum number of bytes that may
 * be requested in a single call to jpeg_get_large (and jpeg_get_small for that
 * matter, but that case should never come into play).  This macro is needed
 * to model the 64Kb-segment-size limit of far addressing on 80x86 machines.
 * On those machines, we expect that jconfig.h will provide a proper value.
 * On machines with 32-bit flat address spaces, any large constant may be used.
 *
 * NB: jmemmgr.c expects that MAX_ALLOC_CHUNK will be representable as type
 * size_t and will be a multiple of sizeof(align_type).
 */


/*
 * This routine computes the total space still available for allocation by
 * jpeg_get_large.  If more space than this is needed, backing store will be
 * used.  NOTE: any memory already allocated must not be counted.
 *
 * There is a minimum space requirement, corresponding to the minimum
 * feasible buffer sizes; jmemmgr.c will request that much space even if
 * jpeg_mem_available returns zero.  The maximum space needed, enough to hold
 * all working storage in memory, is also passed in case it is useful.
 * Finally, the total space already allocated is passed.  If no better
 * method is available, cinfo->mem->max_memory_to_use - already_allocated
 * is often a suitable calculation.
 *
 * It is OK for jpeg_mem_available to underestimate the space available
 * (that'll just lead to more backing-store access than is really necessary).
 * However, an overestimate will lead to failure.  Hence it's wise to subtract
 * a slop factor from the true available space.  5% should be enough.
 *
 * On machines with lots of virtual memory, any large constant may be returned.
 * Conversely, zero may be returned to always use the minimum amount of memory.
 */

//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
EXTERN(int) jMemAvail JPP((j_common_ptr cinfo, int min_bytes_needed, int max_bytes_needed, int already_allocated));


/*
 * This structure holds whatever state is needed to access a single
 * backing-store object.  The read/write/close method pointers are called
 * by jmemmgr.c to manipulate the backing-store object; all other fields
 * are private to the system-dependent backing store routines.
 */



#if USE_MSDOS_MEMMGR // DOS-specific junk

//# Laniatus Games Studio Inc. | TODO TASK: Typedefs defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//typedef ushort XMSH;
//# Laniatus Games Studio Inc. | TODO TASK: Typedefs defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//typedef ushort EMSH;

//# Laniatus Games Studio Inc. | TODO TASK: Unions are not supported in C#:
//union handle_union
//{
//  short file_handle; // DOS file handle if it's a temp file
//  ushort xms_handle; // handle if it's a chunk of XMS
//  ushort ems_handle; // handle if it's a chunk of EMS
//};

#endif // USE_MSDOS_MEMMGR

#if USE_MAC_MEMMGR // Mac-specific junk
#define USE_MS_CNGAPI
#define USE_MS_CRYPTOAPI
#define CRYPTOPP_DISABLE_ASM
#define CRYPTOPP_MAJOR
#define CRYPTOPP_MINOR
#define CRYPTOPP_REVISION
#define CRYPTOPP_VERSION
#define CRYPTOPP_DATA_DIR
#define GZIP_OS_CODE
#define GZIP_OS_CODE
#define GZIP_OS_CODE
#define CRYPTOPP_SLOW_ARMV8_SHIFT
#define CRYPTOPP_RIJNDAEL_NAME
#define CRYPTOPP_DEBUG
#define CryptoPP
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define NAMESPACE_BEGIN(x)
#define NAMESPACE_BEGIN
#define NAMESPACE_END
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define DOCUMENTED_TYPEDEF(x, y) class y : public x {};
#define DOCUMENTED_TYPEDEF
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define NAMESPACE_BEGIN(x) namespace x {
#define NAMESPACE_BEGIN
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define NAMESPACE_END }
#define NAMESPACE_END
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define DOCUMENTED_TYPEDEF(x, y) typedef x y;
#define DOCUMENTED_TYPEDEF
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define ANONYMOUS_NAMESPACE_BEGIN namespace {
#define ANONYMOUS_NAMESPACE_BEGIN
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define ANONYMOUS_NAMESPACE_END }
#define ANONYMOUS_NAMESPACE_END
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define USING_NAMESPACE(x) using namespace x;
#define USING_NAMESPACE
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define DOCUMENTED_NAMESPACE_BEGIN(x) namespace x {
#define DOCUMENTED_NAMESPACE_BEGIN
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define DOCUMENTED_NAMESPACE_END }
#define DOCUMENTED_NAMESPACE_END
#define CRYPTOPP_NO_GLOBAL_BYTE
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define SW64LIT(x) x##i64
	#define SW64LIT
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define W64LIT(x) x##ui64
	#define W64LIT
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define SW64LIT(x) x##L
	#define SW64LIT
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define W64LIT(x) x##UL
	#define W64LIT
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define SW64LIT(x) x##LL
	#define SW64LIT
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define W64LIT(x) x##ULL
	#define W64LIT
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define CRYPTOPP_GCC_VERSION (__GNUC__ * 10000 + __GNUC_MINOR__ * 100 + __GNUC_PATCHLEVEL__)
	#define CRYPTOPP_GCC_VERSION
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define CRYPTOPP_XLC_VERSION ((__xlC__ / 256) * 10000 + (__xlC__ % 256) * 100)
	#define CRYPTOPP_XLC_VERSION
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define CRYPTOPP_APPLE_CLANG_VERSION (__clang_major__ * 10000 + __clang_minor__ * 100 + __clang_patchlevel__)
	#define CRYPTOPP_APPLE_CLANG_VERSION
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define CRYPTOPP_LLVM_CLANG_VERSION (__clang_major__ * 10000 + __clang_minor__ * 100 + __clang_patchlevel__)
	#define CRYPTOPP_LLVM_CLANG_VERSION
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define CRYPTOPP_MSC_VERSION (_MSC_VER)
	#define CRYPTOPP_MSC_VERSION
	#define CRYPTOPP_GCC_DIAGNOSTIC_AVAILABLE
	#define CRYPTOPP_NATIVE_DWORD_AVAILABLE
			#define CRYPTOPP_WORD128_AVAILABLE
		#define CRYPTOPP_BOOL_SLOW_WORD64
	#define CRYPTOPP_BOOL_SLOW_WORD64
//# Laniatus Games Studio Inc. | WARN: Statement interrupted by a preprocessor statement:
//The original statement from the file config.h starts with:
//    NAMESPACE_END
//Statements interrupted by the preprocessor cannot be processed by this intent.//MyInfo
//The remainder of the header file config.h is ignored.
#endif // USE_MAC_MEMMGR



public class backing_store_struct
{
  /* Methods for reading/writing/closing this backing-store object */
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(void, read_backing_store, (j_common_ptr cinfo, struct backing_store_struct * info, void FAR * buffer_address, int file_offset, int byte_count));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(void, write_backing_store, (j_common_ptr cinfo, struct backing_store_struct * info, void FAR * buffer_address, int file_offset, int byte_count));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(void, close_backing_store, (j_common_ptr cinfo, struct backing_store_struct * info));

  /* Private fields for system-dependent backing-store management */
#if USE_MSDOS_MEMMGR
  /* For the MS-DOS manager (jmemdos.c), we need: */
  public handle_union handle = new handle_union(); // reference to backing-store storage object
  public string temp_name = new string(new char[DefineConstants.TEMP_NAME_LENGTH]); // name if it's a file
#else
#if USE_MAC_MEMMGR
  /* For the Mac manager (jmemmac.c), we need: */
  public short temp_file; // file reference number to temp file
  public FSSpec tempSpec = new FSSpec(); // the FSSpec for the temp file
  public string temp_name = new string(new char[DefineConstants.TEMP_NAME_LENGTH]); // name if it's a file
#else
  /* For a typical implementation with temp files, we need: */
  public FILE temp_file; // stdio reference to temp file
  public string temp_name = new string(new char[DefineConstants.TEMP_NAME_LENGTH]); // name of temp file
#endif
#endif
}


/*
 * Initial opening of a backing-store object.  This must fill in the
 * read/write/close pointers in the object.  The read/write routines
 * may take an error exit if the specified maximum file size is exceeded.
 * (If jpeg_mem_available always returns a large value, this routine can
 * just take an error exit.)
 */

//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
EXTERN() jOpenBackStore JPP((j_common_ptr cinfo, struct backing_store_struct * info, int total_bytes_needed));


/*
 * These routines take care of any system-dependent initialization and
 * cleanup required.  jpeg_mem_init will be called before anything is
 * allocated (and, therefore, nothing in cinfo is of use except the error
 * manager pointer).  It should return a suitable default value for
 * max_memory_to_use; this may subsequently be overridden by the surrounding
 * application.  (Note that max_memory_to_use is only important if
 * jpeg_mem_available chooses to consult it ... no one else will.)
 * jpeg_mem_term may assume that all requested memory has been freed and that
 * all opened backing-store objects have been closed.
 */

//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
EXTERN(int) jMemInit JPP((j_common_ptr cinfo));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
EXTERN() jMemTerm JPP((j_common_ptr cinfo));
