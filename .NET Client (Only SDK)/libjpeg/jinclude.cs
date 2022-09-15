#define HAVE_STDDEF_H
#define HAVE_STDLIB_H

/*
 * jinclude.h
 *
 * Copyright (C) 1991-1994, Thomas G. Lane.
 * Modified 2017 by Guido Vollbeding.
 * This file is part of the Independent JPEG Group's software.
 * For conditions of distribution and use, see the accompanying README file.
 *
 * This file exists to provide a single place to fix any problems with
 * including the wrong system include files.  (Common problems are taken
 * care of by the standard jconfig symbols, but on really weird systems
 * you may have to edit this file.)
 *
 * NOTE: this file is NOT intended to be included by applications using the
 * JPEG library.  Most applications need only include jpeglib.h.
 */


/* Include auto-config file to find out which system include files we need. */


/*
 * We need the NULL macro and size_t typedef.
 * On an ANSI-conforming system it is sufficient to include <stddef.h>.
 * Otherwise, we get them from <stdlib.h> or <stdio.h>; we may have to
 * pull in <sys/types.h> as well.
 * Note that the core JPEG library does not require <stdio.h>;
 * only the default error handler and data source/destination modules do.
 * But we must pull it in because of the references to FILE in jpeglib.h.
 * You can remove those references if you want to compile without <stdio.h>.
 */

#if HAVE_STDDEF_H
#endif

#if HAVE_STDLIB_H
#endif

#if NEED_SYS_TYPES_H
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _CRTIMP __declspec(dllimport)
#define _CRTIMP
#define _CRTIMP
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __STR2WSTR(str) L##str
#define __STR2WSTR
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _STR2WSTR(str) __STR2WSTR(str)
#define _STR2WSTR
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __FILEW__ _STR2WSTR(__FILE__)
#define __FILEW__
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __FUNCTIONW__ _STR2WSTR(__FUNCTION__)
#define __FUNCTIONW__
#define _CRT_SECURE_CPP_OVERLOAD_STANDARD_NAMES
#define _CRT_SECURE_CPP_OVERLOAD_STANDARD_NAMES_COUNT
#define _CRT_SECURE_CPP_OVERLOAD_SECURE_NAMES
#define _STATIC_CPPLIB
#define _CRTEXP
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _SAL_VERSION_SAL2(_A) SAL_2_Clean_Violation_using ## _A
  #define _SAL_VERSION_SAL2
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _SAL_VERSION_SAL2(_A)
  #define _SAL_VERSION_SAL2
  #define _SAL2_STRICT
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _SAL_VERSION_CHECK(_A) _SAL_VERSION_SAL2(_A)
  #define _SAL_VERSION_CHECK
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _SAL_VERSION_CHECK(_A)
  #define _SAL_VERSION_CHECK
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define SAL_VERSION_CHECK(_A) _SAL_VERSION_CHECK(_A)
  #define SAL_VERSION_CHECK
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define SAL_VERSION_SAL2(_A) _SAL_VERSION_SAL2(_A)
  #define SAL_VERSION_SAL2
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _SAL_L_Source_(Name, args, annotes) _SA_annotes3(SAL_name, #Name, "", "2") _Group_(annotes _SAL_nop_impl_)
#define _SAL_L_Source_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _SAL_L_Source_(Name, args, annotes) _SA_annotes3(SAL_name, #Name, "", "2") _GrouP_(annotes _SAL_nop_impl_)
#define _SAL_L_Source_
#define __ATTR_SAL
#define _SAL_VERSION
#define __SAL_H_VERSION
#define _USE_DECLSPECS_FOR_SAL
#define _USE_ATTRIBUTES_FOR_SAL
#define _USE_ATTRIBUTES_FOR_SAL
#define _USE_ATTRIBUTES_FOR_SAL
#define _USE_ATTRIBUTES_FOR_SAL
#define _USE_DECLSPECS_FOR_SAL
#define _USE_DECLSPECS_FOR_SAL
#define _USE_ATTRIBUTES_FOR_SAL
#define _USE_DECLSPECS_FOR_SAL
#define _USE_ATTRIBUTES_FOR_SAL
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _SAL1_Source_(Name, args, annotes) _SA_annotes3(SAL_name, #Name, "", "1") _GrouP_(annotes _SAL_nop_impl_)
#define _SAL1_Source_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _SAL1_1_Source_(Name, args, annotes) _SA_annotes3(SAL_name, #Name, "", "1.1") _GrouP_(annotes _SAL_nop_impl_)
#define _SAL1_1_Source_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _SAL1_2_Source_(Name, args, annotes) _SA_annotes3(SAL_name, #Name, "", "1.2") _GrouP_(annotes _SAL_nop_impl_)
#define _SAL1_2_Source_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _SAL2_Source_(Name, args, annotes) _SA_annotes3(SAL_name, #Name, "", "2") _GrouP_(annotes _SAL_nop_impl_)
#define _SAL2_Source_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _SAL_L_Source_(Name, args, annotes) _SA_annotes3(SAL_name, #Name, "", "2") _GrouP_(annotes _SAL_nop_impl_)
#define _SAL_L_Source_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _SAL1_Source_(Name, args, annotes) _SA_annotes3(SAL_name, #Name, "", "1") _Group_(annotes _SAL_nop_impl_)
#define _SAL1_Source_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _SAL1_1_Source_(Name, args, annotes) _SA_annotes3(SAL_name, #Name, "", "1.1") _Group_(annotes _SAL_nop_impl_)
#define _SAL1_1_Source_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _SAL1_2_Source_(Name, args, annotes) _SA_annotes3(SAL_name, #Name, "", "1.2") _Group_(annotes _SAL_nop_impl_)
#define _SAL1_2_Source_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _SAL2_Source_(Name, args, annotes) _SA_annotes3(SAL_name, #Name, "", "2") _Group_(annotes _SAL_nop_impl_)
#define _SAL2_Source_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _SAL_L_Source_(Name, args, annotes) _SA_annotes3(SAL_name, #Name, "", "2") _Group_(annotes _SAL_nop_impl_)
#define _SAL_L_Source_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _At_(target, annos) _At_impl_(target, annos _SAL_nop_impl_)
#define _At_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _At_buffer_(target, iter, bound, annos) _At_buffer_impl_(target, iter, bound, annos _SAL_nop_impl_)
#define _At_buffer_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _When_(expr, annos) _When_impl_(expr, annos _SAL_nop_impl_)
#define _When_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Group_(annos) _Group_impl_(annos _SAL_nop_impl_)
#define _Group_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _GrouP_(annos) _GrouP_impl_(annos _SAL_nop_impl_)
#define _GrouP_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Success_(expr) _SAL2_Source_(_Success_, (expr), _Success_impl_(expr))
#define _Success_
//# Laniatus Games Studio Inc. | TODO TASK: Conditional typedefs are not handled by # Laniatus Games Studio Inc. |:
//#define _Return_type_success_(expr) _SAL2_Source_(_Return_type_success_, (expr), _Success_impl_(expr))
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _On_failure_(annos) _On_failure_impl_(annos _SAL_nop_impl_)
#define _On_failure_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Always_(annos) _Always_impl_(annos _SAL_nop_impl_)
#define _Always_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Use_decl_annotations_ _Use_decl_anno_impl_
#define _Use_decl_annotations_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Notref_ _Notref_impl_
#define _Notref_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_defensive_ _SA_annotes0(SAL_pre_defensive)
#define _Pre_defensive_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Post_defensive_ _SA_annotes0(SAL_post_defensive)
#define _Post_defensive_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _In_defensive_(annotes) _Pre_defensive_ _Group_(annotes)
#define _In_defensive_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_defensive_(annotes) _Post_defensive_ _Group_(annotes)
#define _Out_defensive_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Inout_defensive_(annotes) _Pre_defensive_ _Post_defensive_ _Group_(annotes)
#define _Inout_defensive_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Reserved_ _SAL2_Source_(_Reserved_, (), _Pre1_impl_(__null_impl))
#define _Reserved_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Const_ _SAL2_Source_(_Const_, (), _Pre1_impl_(__readaccess_impl_notref))
#define _Const_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _In_ _SAL2_Source_(_In_, (), _Pre1_impl_(__notnull_impl_notref) _Pre_valid_impl_ _Deref_pre1_impl_(__readaccess_impl_notref))
#define _In_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _In_opt_ _SAL2_Source_(_In_opt_, (), _Pre1_impl_(__maybenull_impl_notref) _Pre_valid_impl_ _Deref_pre_readonly_)
#define _In_opt_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _In_z_ _SAL2_Source_(_In_z_, (), _In_ _Pre1_impl_(__zterm_impl))
#define _In_z_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _In_opt_z_ _SAL2_Source_(_In_opt_z_, (), _In_opt_ _Pre1_impl_(__zterm_impl))
#define _In_opt_z_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _In_reads_(size) _SAL2_Source_(_In_reads_, (size), _Pre_count_(size) _Deref_pre_readonly_)
#define _In_reads_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _In_reads_opt_(size) _SAL2_Source_(_In_reads_opt_, (size), _Pre_opt_count_(size) _Deref_pre_readonly_)
#define _In_reads_opt_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _In_reads_bytes_(size) _SAL2_Source_(_In_reads_bytes_, (size), _Pre_bytecount_(size) _Deref_pre_readonly_)
#define _In_reads_bytes_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _In_reads_bytes_opt_(size) _SAL2_Source_(_In_reads_bytes_opt_, (size), _Pre_opt_bytecount_(size) _Deref_pre_readonly_)
#define _In_reads_bytes_opt_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _In_reads_z_(size) _SAL2_Source_(_In_reads_z_, (size), _In_reads_(size) _Pre_z_)
#define _In_reads_z_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _In_reads_opt_z_(size) _SAL2_Source_(_In_reads_opt_z_, (size), _Pre_opt_count_(size) _Deref_pre_readonly_ _Pre_opt_z_)
#define _In_reads_opt_z_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _In_reads_or_z_(size) _SAL2_Source_(_In_reads_or_z_, (size), _In_ _When_(_String_length_(_Curr_) < (size), _Pre_z_) _When_(_String_length_(_Curr_) >= (size), _Pre1_impl_(__count_impl(size))))
#define _In_reads_or_z_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _In_reads_or_z_opt_(size) _SAL2_Source_(_In_reads_or_z_opt_, (size), _In_opt_ _When_(_String_length_(_Curr_) < (size), _Pre_z_) _When_(_String_length_(_Curr_) >= (size), _Pre1_impl_(__count_impl(size))))
#define _In_reads_or_z_opt_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _In_reads_to_ptr_(ptr) _SAL2_Source_(_In_reads_to_ptr_, (ptr), _Pre_ptrdiff_count_(ptr) _Deref_pre_readonly_)
#define _In_reads_to_ptr_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _In_reads_to_ptr_opt_(ptr) _SAL2_Source_(_In_reads_to_ptr_opt_, (ptr), _Pre_opt_ptrdiff_count_(ptr) _Deref_pre_readonly_)
#define _In_reads_to_ptr_opt_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _In_reads_to_ptr_z_(ptr) _SAL2_Source_(_In_reads_to_ptr_z_, (ptr), _In_reads_to_ptr_(ptr) _Pre_z_)
#define _In_reads_to_ptr_z_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _In_reads_to_ptr_opt_z_(ptr) _SAL2_Source_(_In_reads_to_ptr_opt_z_, (ptr), _Pre_opt_ptrdiff_count_(ptr) _Deref_pre_readonly_ _Pre_opt_z_)
#define _In_reads_to_ptr_opt_z_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_ _SAL2_Source_(_Out_, (), _Out_impl_)
#define _Out_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_opt_ _SAL2_Source_(_Out_opt_, (), _Out_opt_impl_)
#define _Out_opt_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_writes_(size) _SAL2_Source_(_Out_writes_, (size), _Pre_cap_(size) _Post_valid_impl_)
#define _Out_writes_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_writes_opt_(size) _SAL2_Source_(_Out_writes_opt_, (size), _Pre_opt_cap_(size) _Post_valid_impl_)
#define _Out_writes_opt_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_writes_bytes_(size) _SAL2_Source_(_Out_writes_bytes_, (size), _Pre_bytecap_(size) _Post_valid_impl_)
#define _Out_writes_bytes_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_writes_bytes_opt_(size) _SAL2_Source_(_Out_writes_bytes_opt_, (size), _Pre_opt_bytecap_(size) _Post_valid_impl_)
#define _Out_writes_bytes_opt_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_writes_z_(size) _SAL2_Source_(_Out_writes_z_, (size), _Pre_cap_(size) _Post_valid_impl_ _Post_z_)
#define _Out_writes_z_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_writes_opt_z_(size) _SAL2_Source_(_Out_writes_opt_z_, (size), _Pre_opt_cap_(size) _Post_valid_impl_ _Post_z_)
#define _Out_writes_opt_z_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_writes_to_(size,count) _SAL2_Source_(_Out_writes_to_, (size,count), _Pre_cap_(size) _Post_valid_impl_ _Post_count_(count))
#define _Out_writes_to_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_writes_to_opt_(size,count) _SAL2_Source_(_Out_writes_to_opt_, (size,count), _Pre_opt_cap_(size) _Post_valid_impl_ _Post_count_(count))
#define _Out_writes_to_opt_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_writes_all_(size) _SAL2_Source_(_Out_writes_all_, (size), _Out_writes_to_(_Old_(size), _Old_(size)))
#define _Out_writes_all_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_writes_all_opt_(size) _SAL2_Source_(_Out_writes_all_opt_, (size), _Out_writes_to_opt_(_Old_(size), _Old_(size)))
#define _Out_writes_all_opt_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_writes_bytes_to_(size,count) _SAL2_Source_(_Out_writes_bytes_to_, (size,count), _Pre_bytecap_(size) _Post_valid_impl_ _Post_bytecount_(count))
#define _Out_writes_bytes_to_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_writes_bytes_to_opt_(size,count) _SAL2_Source_(_Out_writes_bytes_to_opt_, (size,count), _Pre_opt_bytecap_(size) _Post_valid_impl_ _Post_bytecount_(count))
#define _Out_writes_bytes_to_opt_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_writes_bytes_all_(size) _SAL2_Source_(_Out_writes_bytes_all_, (size), _Out_writes_bytes_to_(_Old_(size), _Old_(size)))
#define _Out_writes_bytes_all_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_writes_bytes_all_opt_(size) _SAL2_Source_(_Out_writes_bytes_all_opt_, (size), _Out_writes_bytes_to_opt_(_Old_(size), _Old_(size)))
#define _Out_writes_bytes_all_opt_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_writes_to_ptr_(ptr) _SAL2_Source_(_Out_writes_to_ptr_, (ptr), _Pre_ptrdiff_cap_(ptr) _Post_valid_impl_)
#define _Out_writes_to_ptr_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_writes_to_ptr_opt_(ptr) _SAL2_Source_(_Out_writes_to_ptr_opt_, (ptr), _Pre_opt_ptrdiff_cap_(ptr) _Post_valid_impl_)
#define _Out_writes_to_ptr_opt_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_writes_to_ptr_z_(ptr) _SAL2_Source_(_Out_writes_to_ptr_z_, (ptr), _Pre_ptrdiff_cap_(ptr) _Post_valid_impl_ Post_z_)
#define _Out_writes_to_ptr_z_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_writes_to_ptr_opt_z_(ptr) _SAL2_Source_(_Out_writes_to_ptr_opt_z_, (ptr), _Pre_opt_ptrdiff_cap_(ptr) _Post_valid_impl_ Post_z_)
#define _Out_writes_to_ptr_opt_z_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Inout_ _SAL2_Source_(_Inout_, (), _Prepost_valid_)
#define _Inout_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Inout_opt_ _SAL2_Source_(_Inout_opt_, (), _Prepost_opt_valid_)
#define _Inout_opt_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Inout_z_ _SAL2_Source_(_Inout_z_, (), _Prepost_z_)
#define _Inout_z_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Inout_opt_z_ _SAL2_Source_(_Inout_opt_z_, (), _Prepost_opt_z_)
#define _Inout_opt_z_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Inout_updates_(size) _SAL2_Source_(_Inout_updates_, (size), _Pre_cap_(size) _Pre_valid_impl_ _Post_valid_impl_)
#define _Inout_updates_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Inout_updates_opt_(size) _SAL2_Source_(_Inout_updates_opt_, (size), _Pre_opt_cap_(size) _Pre_valid_impl_ _Post_valid_impl_)
#define _Inout_updates_opt_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Inout_updates_z_(size) _SAL2_Source_(_Inout_updates_z_, (size), _Pre_cap_(size) _Pre_valid_impl_ _Post_valid_impl_ _Pre1_impl_(__zterm_impl) _Post1_impl_(__zterm_impl))
#define _Inout_updates_z_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Inout_updates_opt_z_(size) _SAL2_Source_(_Inout_updates_opt_z_, (size), _Pre_opt_cap_(size) _Pre_valid_impl_ _Post_valid_impl_ _Pre1_impl_(__zterm_impl) _Post1_impl_(__zterm_impl))
#define _Inout_updates_opt_z_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Inout_updates_to_(size,count) _SAL2_Source_(_Inout_updates_to_, (size,count), _Out_writes_to_(size,count) _Pre_valid_impl_ _Pre1_impl_(__count_impl(size)))
#define _Inout_updates_to_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Inout_updates_to_opt_(size,count) _SAL2_Source_(_Inout_updates_to_opt_, (size,count), _Out_writes_to_opt_(size,count) _Pre_valid_impl_ _Pre1_impl_(__count_impl(size)))
#define _Inout_updates_to_opt_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Inout_updates_all_(size) _SAL2_Source_(_Inout_updates_all_, (size), _Inout_updates_to_(_Old_(size), _Old_(size)))
#define _Inout_updates_all_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Inout_updates_all_opt_(size) _SAL2_Source_(_Inout_updates_all_opt_, (size), _Inout_updates_to_opt_(_Old_(size), _Old_(size)))
#define _Inout_updates_all_opt_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Inout_updates_bytes_(size) _SAL2_Source_(_Inout_updates_bytes_, (size), _Pre_bytecap_(size) _Pre_valid_impl_ _Post_valid_impl_)
#define _Inout_updates_bytes_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Inout_updates_bytes_opt_(size) _SAL2_Source_(_Inout_updates_bytes_opt_, (size), _Pre_opt_bytecap_(size) _Pre_valid_impl_ _Post_valid_impl_)
#define _Inout_updates_bytes_opt_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Inout_updates_bytes_to_(size,count) _SAL2_Source_(_Inout_updates_bytes_to_, (size,count), _Out_writes_bytes_to_(size,count) _Pre_valid_impl_ _Pre1_impl_(__bytecount_impl(size)))
#define _Inout_updates_bytes_to_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Inout_updates_bytes_to_opt_(size,count) _SAL2_Source_(_Inout_updates_bytes_to_opt_, (size,count), _Out_writes_bytes_to_opt_(size,count) _Pre_valid_impl_ _Pre1_impl_(__bytecount_impl(size)))
#define _Inout_updates_bytes_to_opt_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Inout_updates_bytes_all_(size) _SAL2_Source_(_Inout_updates_bytes_all_, (size), _Inout_updates_bytes_to_(_Old_(size), _Old_(size)))
#define _Inout_updates_bytes_all_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Inout_updates_bytes_all_opt_(size) _SAL2_Source_(_Inout_updates_bytes_all_opt_, (size), _Inout_updates_bytes_to_opt_(_Old_(size), _Old_(size)))
#define _Inout_updates_bytes_all_opt_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Outptr_ _SAL2_Source_(_Outptr_, (), _Out_impl_ _Deref_post2_impl_(__notnull_impl_notref, __count_impl(1)))
#define _Outptr_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Outptr_result_maybenull_ _SAL2_Source_(_Outptr_result_maybenull_, (), _Out_impl_ _Deref_post2_impl_(__maybenull_impl_notref, __count_impl(1)))
#define _Outptr_result_maybenull_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Outptr_opt_ _SAL2_Source_(_Outptr_opt_, (), _Out_opt_impl_ _Deref_post2_impl_(__notnull_impl_notref, __count_impl(1)))
#define _Outptr_opt_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Outptr_opt_result_maybenull_ _SAL2_Source_(_Outptr_opt_result_maybenull_, (), _Out_opt_impl_ _Deref_post2_impl_(__maybenull_impl_notref, __count_impl(1)))
#define _Outptr_opt_result_maybenull_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Outptr_result_z_ _SAL2_Source_(_Outptr_result_z_, (), _Out_impl_ _Deref_post_z_)
#define _Outptr_result_z_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Outptr_opt_result_z_ _SAL2_Source_(_Outptr_opt_result_z_, (), _Out_opt_impl_ _Deref_post_z_)
#define _Outptr_opt_result_z_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Outptr_result_maybenull_z_ _SAL2_Source_(_Outptr_result_maybenull_z_, (), _Out_impl_ _Deref_post_opt_z_)
#define _Outptr_result_maybenull_z_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Outptr_opt_result_maybenull_z_ _SAL2_Source_(_Outptr_opt_result_maybenull_z_, (), _Out_opt_impl_ _Deref_post_opt_z_)
#define _Outptr_opt_result_maybenull_z_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Outptr_result_nullonfailure_ _SAL2_Source_(_Outptr_result_nullonfailure_, (), _Outptr_ _On_failure_(_Deref_post_null_))
#define _Outptr_result_nullonfailure_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Outptr_opt_result_nullonfailure_ _SAL2_Source_(_Outptr_opt_result_nullonfailure_, (), _Outptr_opt_ _On_failure_(_Deref_post_null_))
#define _Outptr_opt_result_nullonfailure_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _COM_Outptr_ _SAL2_Source_(_COM_Outptr_, (), _Outptr_ _On_failure_(_Deref_post_null_))
#define _COM_Outptr_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _COM_Outptr_result_maybenull_ _SAL2_Source_(_COM_Outptr_result_maybenull_, (), _Outptr_result_maybenull_ _On_failure_(_Deref_post_null_))
#define _COM_Outptr_result_maybenull_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _COM_Outptr_opt_ _SAL2_Source_(_COM_Outptr_opt_, (), _Outptr_opt_ _On_failure_(_Deref_post_null_))
#define _COM_Outptr_opt_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _COM_Outptr_opt_result_maybenull_ _SAL2_Source_(_COM_Outptr_opt_result_maybenull_, (), _Outptr_opt_result_maybenull_ _On_failure_(_Deref_post_null_))
#define _COM_Outptr_opt_result_maybenull_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Outptr_result_buffer_(size) _SAL2_Source_(_Outptr_result_buffer_, (size), _Out_impl_ _Deref_post2_impl_(__notnull_impl_notref, __cap_impl(size)))
#define _Outptr_result_buffer_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Outptr_opt_result_buffer_(size) _SAL2_Source_(_Outptr_opt_result_buffer_, (size), _Out_opt_impl_ _Deref_post2_impl_(__notnull_impl_notref, __cap_impl(size)))
#define _Outptr_opt_result_buffer_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Outptr_result_buffer_to_(size, count) _SAL2_Source_(_Outptr_result_buffer_to_, (size, count), _Out_impl_ _Deref_post3_impl_(__notnull_impl_notref, __cap_impl(size), __count_impl(count)))
#define _Outptr_result_buffer_to_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Outptr_opt_result_buffer_to_(size, count) _SAL2_Source_(_Outptr_opt_result_buffer_to_, (size, count), _Out_opt_impl_ _Deref_post3_impl_(__notnull_impl_notref, __cap_impl(size), __count_impl(count)))
#define _Outptr_opt_result_buffer_to_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Outptr_result_buffer_all_(size) _SAL2_Source_(_Outptr_result_buffer_all_, (size), _Out_impl_ _Deref_post2_impl_(__notnull_impl_notref, __count_impl(size)))
#define _Outptr_result_buffer_all_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Outptr_opt_result_buffer_all_(size) _SAL2_Source_(_Outptr_opt_result_buffer_all_, (size), _Out_opt_impl_ _Deref_post2_impl_(__notnull_impl_notref, __count_impl(size)))
#define _Outptr_opt_result_buffer_all_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Outptr_result_buffer_maybenull_(size) _SAL2_Source_(_Outptr_result_buffer_maybenull_, (size), _Out_impl_ _Deref_post2_impl_(__maybenull_impl_notref, __cap_impl(size)))
#define _Outptr_result_buffer_maybenull_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Outptr_opt_result_buffer_maybenull_(size) _SAL2_Source_(_Outptr_opt_result_buffer_maybenull_, (size), _Out_opt_impl_ _Deref_post2_impl_(__maybenull_impl_notref, __cap_impl(size)))
#define _Outptr_opt_result_buffer_maybenull_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Outptr_result_buffer_to_maybenull_(size, count) _SAL2_Source_(_Outptr_result_buffer_to_maybenull_, (size, count), _Out_impl_ _Deref_post3_impl_(__maybenull_impl_notref, __cap_impl(size), __count_impl(count)))
#define _Outptr_result_buffer_to_maybenull_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Outptr_opt_result_buffer_to_maybenull_(size, count) _SAL2_Source_(_Outptr_opt_result_buffer_to_maybenull_, (size, count), _Out_opt_impl_ _Deref_post3_impl_(__maybenull_impl_notref, __cap_impl(size), __count_impl(count)))
#define _Outptr_opt_result_buffer_to_maybenull_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Outptr_result_buffer_all_maybenull_(size) _SAL2_Source_(_Outptr_result_buffer_all_maybenull_, (size), _Out_impl_ _Deref_post2_impl_(__maybenull_impl_notref, __count_impl(size)))
#define _Outptr_result_buffer_all_maybenull_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Outptr_opt_result_buffer_all_maybenull_(size) _SAL2_Source_(_Outptr_opt_result_buffer_all_maybenull_, (size), _Out_opt_impl_ _Deref_post2_impl_(__maybenull_impl_notref, __count_impl(size)))
#define _Outptr_opt_result_buffer_all_maybenull_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Outptr_result_bytebuffer_(size) _SAL2_Source_(_Outptr_result_bytebuffer_, (size), _Out_impl_ _Deref_post2_impl_(__notnull_impl_notref, __bytecap_impl(size)))
#define _Outptr_result_bytebuffer_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Outptr_opt_result_bytebuffer_(size) _SAL2_Source_(_Outptr_opt_result_bytebuffer_, (size), _Out_opt_impl_ _Deref_post2_impl_(__notnull_impl_notref, __bytecap_impl(size)))
#define _Outptr_opt_result_bytebuffer_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Outptr_result_bytebuffer_to_(size, count) _SAL2_Source_(_Outptr_result_bytebuffer_to_, (size, count), _Out_impl_ _Deref_post3_impl_(__notnull_impl_notref, __bytecap_impl(size), __bytecount_impl(count)))
#define _Outptr_result_bytebuffer_to_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Outptr_opt_result_bytebuffer_to_(size, count) _SAL2_Source_(_Outptr_opt_result_bytebuffer_to_, (size, count), _Out_opt_impl_ _Deref_post3_impl_(__notnull_impl_notref, __bytecap_impl(size), __bytecount_impl(count)))
#define _Outptr_opt_result_bytebuffer_to_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Outptr_result_bytebuffer_all_(size) _SAL2_Source_(_Outptr_result_bytebuffer_all_, (size), _Out_impl_ _Deref_post2_impl_(__notnull_impl_notref, __bytecount_impl(size)))
#define _Outptr_result_bytebuffer_all_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Outptr_opt_result_bytebuffer_all_(size) _SAL2_Source_(_Outptr_opt_result_bytebuffer_all_, (size), _Out_opt_impl_ _Deref_post2_impl_(__notnull_impl_notref, __bytecount_impl(size)))
#define _Outptr_opt_result_bytebuffer_all_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Outptr_result_bytebuffer_maybenull_(size) _SAL2_Source_(_Outptr_result_bytebuffer_maybenull_, (size), _Out_impl_ _Deref_post2_impl_(__maybenull_impl_notref, __bytecap_impl(size)))
#define _Outptr_result_bytebuffer_maybenull_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Outptr_opt_result_bytebuffer_maybenull_(size) _SAL2_Source_(_Outptr_opt_result_bytebuffer_maybenull_, (size), _Out_opt_impl_ _Deref_post2_impl_(__maybenull_impl_notref, __bytecap_impl(size)))
#define _Outptr_opt_result_bytebuffer_maybenull_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Outptr_result_bytebuffer_to_maybenull_(size, count) _SAL2_Source_(_Outptr_result_bytebuffer_to_maybenull_, (size, count), _Out_impl_ _Deref_post3_impl_(__maybenull_impl_notref, __bytecap_impl(size), __bytecount_impl(count)))
#define _Outptr_result_bytebuffer_to_maybenull_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Outptr_opt_result_bytebuffer_to_maybenull_(size, count) _SAL2_Source_(_Outptr_opt_result_bytebuffer_to_maybenull_, (size, count), _Out_opt_impl_ _Deref_post3_impl_(__maybenull_impl_notref, __bytecap_impl(size), __bytecount_impl(count)))
#define _Outptr_opt_result_bytebuffer_to_maybenull_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Outptr_result_bytebuffer_all_maybenull_(size) _SAL2_Source_(_Outptr_result_bytebuffer_all_maybenull_, (size), _Out_impl_ _Deref_post2_impl_(__maybenull_impl_notref, __bytecount_impl(size)))
#define _Outptr_result_bytebuffer_all_maybenull_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Outptr_opt_result_bytebuffer_all_maybenull_(size) _SAL2_Source_(_Outptr_opt_result_bytebuffer_all_maybenull_, (size), _Out_opt_impl_ _Deref_post2_impl_(__maybenull_impl_notref, __bytecount_impl(size)))
#define _Outptr_opt_result_bytebuffer_all_maybenull_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Outref_ _SAL2_Source_(_Outref_, (), _Out_impl_ _Post_notnull_)
#define _Outref_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Outref_result_maybenull_ _SAL2_Source_(_Outref_result_maybenull_, (), _Pre2_impl_(__notnull_impl_notref, __cap_c_one_notref_impl) _Post_maybenull_ _Post_valid_impl_)
#define _Outref_result_maybenull_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Outref_result_buffer_(size) _SAL2_Source_(_Outref_result_buffer_, (size), _Outref_ _Post1_impl_(__cap_impl(size)))
#define _Outref_result_buffer_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Outref_result_bytebuffer_(size) _SAL2_Source_(_Outref_result_bytebuffer_, (size), _Outref_ _Post1_impl_(__bytecap_impl(size)))
#define _Outref_result_bytebuffer_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Outref_result_buffer_to_(size, count) _SAL2_Source_(_Outref_result_buffer_to_, (size, count), _Outref_result_buffer_(size) _Post1_impl_(__count_impl(count)))
#define _Outref_result_buffer_to_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Outref_result_bytebuffer_to_(size, count) _SAL2_Source_(_Outref_result_bytebuffer_to_, (size, count), _Outref_result_bytebuffer_(size) _Post1_impl_(__bytecount_impl(count)))
#define _Outref_result_bytebuffer_to_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Outref_result_buffer_all_(size) _SAL2_Source_(_Outref_result_buffer_all_, (size), _Outref_result_buffer_to_(size, _Old_(size)))
#define _Outref_result_buffer_all_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Outref_result_bytebuffer_all_(size) _SAL2_Source_(_Outref_result_bytebuffer_all_, (size), _Outref_result_bytebuffer_to_(size, _Old_(size)))
#define _Outref_result_bytebuffer_all_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Outref_result_buffer_maybenull_(size) _SAL2_Source_(_Outref_result_buffer_maybenull_, (size), _Outref_result_maybenull_ _Post1_impl_(__cap_impl(size)))
#define _Outref_result_buffer_maybenull_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Outref_result_bytebuffer_maybenull_(size) _SAL2_Source_(_Outref_result_bytebuffer_maybenull_, (size), _Outref_result_maybenull_ _Post1_impl_(__bytecap_impl(size)))
#define _Outref_result_bytebuffer_maybenull_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Outref_result_buffer_to_maybenull_(size, count) _SAL2_Source_(_Outref_result_buffer_to_maybenull_, (size, count), _Outref_result_buffer_maybenull_(size) _Post1_impl_(__count_impl(count)))
#define _Outref_result_buffer_to_maybenull_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Outref_result_bytebuffer_to_maybenull_(size, count) _SAL2_Source_(_Outref_result_bytebuffer_to_maybenull_, (size, count), _Outref_result_bytebuffer_maybenull_(size) _Post1_impl_(__bytecount_impl(count)))
#define _Outref_result_bytebuffer_to_maybenull_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Outref_result_buffer_all_maybenull_(size) _SAL2_Source_(_Outref_result_buffer_all_maybenull_, (size), _Outref_result_buffer_to_maybenull_(size, _Old_(size)))
#define _Outref_result_buffer_all_maybenull_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Outref_result_bytebuffer_all_maybenull_(size) _SAL2_Source_(_Outref_result_bytebuffer_all_maybenull_, (size), _Outref_result_bytebuffer_to_maybenull_(size, _Old_(size)))
#define _Outref_result_bytebuffer_all_maybenull_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Outref_result_nullonfailure_ _SAL2_Source_(_Outref_result_nullonfailure_, (), _Outref_ _On_failure_(_Post_null_))
#define _Outref_result_nullonfailure_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Result_nullonfailure_ _SAL2_Source_(_Result_nullonfailure_, (), _On_failure_(_Notref_impl_ _Deref_impl_ _Post_null_))
#define _Result_nullonfailure_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Result_zeroonfailure_ _SAL2_Source_(_Result_zeroonfailure_, (), _On_failure_(_Notref_impl_ _Deref_impl_ _Out_range_(==, 0)))
#define _Result_zeroonfailure_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Ret_z_ _SAL2_Source_(_Ret_z_, (), _Ret2_impl_(__notnull_impl, __zterm_impl) _Ret_valid_impl_)
#define _Ret_z_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Ret_maybenull_z_ _SAL2_Source_(_Ret_maybenull_z_, (), _Ret2_impl_(__maybenull_impl,__zterm_impl) _Ret_valid_impl_)
#define _Ret_maybenull_z_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Ret_notnull_ _SAL2_Source_(_Ret_notnull_, (), _Ret1_impl_(__notnull_impl))
#define _Ret_notnull_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Ret_maybenull_ _SAL2_Source_(_Ret_maybenull_, (), _Ret1_impl_(__maybenull_impl))
#define _Ret_maybenull_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Ret_null_ _SAL2_Source_(_Ret_null_, (), _Ret1_impl_(__null_impl))
#define _Ret_null_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Ret_valid_ _SAL2_Source_(_Ret_valid_, (), _Ret1_impl_(__notnull_impl_notref) _Ret_valid_impl_)
#define _Ret_valid_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Ret_writes_(size) _SAL2_Source_(_Ret_writes_, (size), _Ret2_impl_(__notnull_impl, __count_impl(size)) _Ret_valid_impl_)
#define _Ret_writes_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Ret_writes_z_(size) _SAL2_Source_(_Ret_writes_z_, (size), _Ret3_impl_(__notnull_impl, __count_impl(size), __zterm_impl) _Ret_valid_impl_)
#define _Ret_writes_z_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Ret_writes_bytes_(size) _SAL2_Source_(_Ret_writes_bytes_, (size), _Ret2_impl_(__notnull_impl, __bytecount_impl(size)) _Ret_valid_impl_)
#define _Ret_writes_bytes_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Ret_writes_maybenull_(size) _SAL2_Source_(_Ret_writes_maybenull_, (size), _Ret2_impl_(__maybenull_impl,__count_impl(size)) _Ret_valid_impl_)
#define _Ret_writes_maybenull_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Ret_writes_maybenull_z_(size) _SAL2_Source_(_Ret_writes_maybenull_z_, (size), _Ret3_impl_(__maybenull_impl,__count_impl(size),__zterm_impl) _Ret_valid_impl_)
#define _Ret_writes_maybenull_z_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Ret_writes_bytes_maybenull_(size) _SAL2_Source_(_Ret_writes_bytes_maybenull_, (size), _Ret2_impl_(__maybenull_impl,__bytecount_impl(size)) _Ret_valid_impl_)
#define _Ret_writes_bytes_maybenull_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Ret_writes_to_(size,count) _SAL2_Source_(_Ret_writes_to_, (size,count), _Ret3_impl_(__notnull_impl, __cap_impl(size), __count_impl(count)) _Ret_valid_impl_)
#define _Ret_writes_to_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Ret_writes_bytes_to_(size,count) _SAL2_Source_(_Ret_writes_bytes_to_, (size,count), _Ret3_impl_(__notnull_impl, __bytecap_impl(size), __bytecount_impl(count)) _Ret_valid_impl_)
#define _Ret_writes_bytes_to_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Ret_writes_to_maybenull_(size,count) _SAL2_Source_(_Ret_writes_to_maybenull_, (size,count), _Ret3_impl_(__maybenull_impl, __cap_impl(size), __count_impl(count)) _Ret_valid_impl_)
#define _Ret_writes_to_maybenull_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Ret_writes_bytes_to_maybenull_(size,count) _SAL2_Source_(_Ret_writes_bytes_to_maybenull_, (size,count), _Ret3_impl_(__maybenull_impl, __bytecap_impl(size), __bytecount_impl(count)) _Ret_valid_impl_)
#define _Ret_writes_bytes_to_maybenull_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Points_to_data_ _SAL2_Source_(_Points_to_data_, (), _Pre_ _Points_to_data_impl_)
#define _Points_to_data_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Literal_ _SAL2_Source_(_Literal_, (), _Pre_ _Literal_impl_)
#define _Literal_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Notliteral_ _SAL2_Source_(_Notliteral_, (), _Pre_ _Notliteral_impl_)
#define _Notliteral_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Check_return_ _SAL2_Source_(_Check_return_, (), _Check_return_impl_)
#define _Check_return_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Must_inspect_result_ _SAL2_Source_(_Must_inspect_result_, (), _Must_inspect_impl_ _Check_return_impl_)
#define _Must_inspect_result_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Printf_format_string_ _SAL2_Source_(_Printf_format_string_, (), _Printf_format_string_impl_)
#define _Printf_format_string_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Scanf_format_string_ _SAL2_Source_(_Scanf_format_string_, (), _Scanf_format_string_impl_)
#define _Scanf_format_string_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Scanf_s_format_string_ _SAL2_Source_(_Scanf_s_format_string_, (), _Scanf_s_format_string_impl_)
#define _Scanf_s_format_string_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Format_string_impl_(kind,where) _SA_annotes2(SAL_IsFormatString2, kind, where)
#define _Format_string_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Printf_format_string_params_(x) _SAL2_Source_(_Printf_format_string_params_, (x), _Format_string_impl_("printf", x))
#define _Printf_format_string_params_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Scanf_format_string_params_(x) _SAL2_Source_(_Scanf_format_string_params_, (x), _Format_string_impl_("scanf", x))
#define _Scanf_format_string_params_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Scanf_s_format_string_params_(x) _SAL2_Source_(_Scanf_s_format_string_params_, (x), _Format_string_impl_("scanf_s", x))
#define _Scanf_s_format_string_params_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _In_range_(lb,ub) _SAL2_Source_(_In_range_, (lb,ub), _In_range_impl_(lb,ub))
#define _In_range_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_range_(lb,ub) _SAL2_Source_(_Out_range_, (lb,ub), _Out_range_impl_(lb,ub))
#define _Out_range_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Ret_range_(lb,ub) _SAL2_Source_(_Ret_range_, (lb,ub), _Ret_range_impl_(lb,ub))
#define _Ret_range_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_in_range_(lb,ub) _SAL2_Source_(_Deref_in_range_, (lb,ub), _Deref_in_range_impl_(lb,ub))
#define _Deref_in_range_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_out_range_(lb,ub) _SAL2_Source_(_Deref_out_range_, (lb,ub), _Deref_out_range_impl_(lb,ub))
#define _Deref_out_range_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_ret_range_(lb,ub) _SAL2_Source_(_Deref_ret_range_, (lb,ub), _Deref_ret_range_impl_(lb,ub))
#define _Deref_ret_range_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_equal_to_(expr) _SAL2_Source_(_Pre_equal_to_, (expr), _In_range_(==, expr))
#define _Pre_equal_to_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Post_equal_to_(expr) _SAL2_Source_(_Post_equal_to_, (expr), _Out_range_(==, expr))
#define _Post_equal_to_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Unchanged_(e) _SAL2_Source_(_Unchanged_, (e), _At_(e, _Post_equal_to_(_Old_(e)) _Const_))
#define _Unchanged_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_satisfies_(cond) _SAL2_Source_(_Pre_satisfies_, (cond), _Pre_satisfies_impl_(cond))
#define _Pre_satisfies_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Post_satisfies_(cond) _SAL2_Source_(_Post_satisfies_, (cond), _Post_satisfies_impl_(cond))
#define _Post_satisfies_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Struct_size_bytes_(size) _SAL2_Source_(_Struct_size_bytes_, (size), _Writable_bytes_(size))
#define _Struct_size_bytes_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Field_size_(size) _SAL2_Source_(_Field_size_, (size), _Notnull_ _Writable_elements_(size))
#define _Field_size_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Field_size_opt_(size) _SAL2_Source_(_Field_size_opt_, (size), _Maybenull_ _Writable_elements_(size))
#define _Field_size_opt_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Field_size_part_(size, count) _SAL2_Source_(_Field_size_part_, (size, count), _Notnull_ _Writable_elements_(size) _Readable_elements_(count))
#define _Field_size_part_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Field_size_part_opt_(size, count) _SAL2_Source_(_Field_size_part_opt_, (size, count), _Maybenull_ _Writable_elements_(size) _Readable_elements_(count))
#define _Field_size_part_opt_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Field_size_full_(size) _SAL2_Source_(_Field_size_full_, (size), _Field_size_part_(size, size))
#define _Field_size_full_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Field_size_full_opt_(size) _SAL2_Source_(_Field_size_full_opt_, (size), _Field_size_part_opt_(size, size))
#define _Field_size_full_opt_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Field_size_bytes_(size) _SAL2_Source_(_Field_size_bytes_, (size), _Notnull_ _Writable_bytes_(size))
#define _Field_size_bytes_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Field_size_bytes_opt_(size) _SAL2_Source_(_Field_size_bytes_opt_, (size), _Maybenull_ _Writable_bytes_(size))
#define _Field_size_bytes_opt_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Field_size_bytes_part_(size, count) _SAL2_Source_(_Field_size_bytes_part_, (size, count), _Notnull_ _Writable_bytes_(size) _Readable_bytes_(count))
#define _Field_size_bytes_part_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Field_size_bytes_part_opt_(size, count) _SAL2_Source_(_Field_size_bytes_part_opt_, (size, count), _Maybenull_ _Writable_bytes_(size) _Readable_bytes_(count))
#define _Field_size_bytes_part_opt_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Field_size_bytes_full_(size) _SAL2_Source_(_Field_size_bytes_full_, (size), _Field_size_bytes_part_(size, size))
#define _Field_size_bytes_full_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Field_size_bytes_full_opt_(size) _SAL2_Source_(_Field_size_bytes_full_opt_, (size), _Field_size_bytes_part_opt_(size, size))
#define _Field_size_bytes_full_opt_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Field_z_ _SAL2_Source_(_Field_z_, (), _Null_terminated_)
#define _Field_z_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Field_range_(min,max) _SAL2_Source_(_Field_range_, (min,max), _Field_range_impl_(min,max))
#define _Field_range_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_ _Pre_impl_
#define _Pre_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Post_ _Post_impl_
#define _Post_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Valid_ _Valid_impl_
#define _Valid_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Notvalid_ _Notvalid_impl_
#define _Notvalid_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Maybevalid_ _Maybevalid_impl_
#define _Maybevalid_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Readable_bytes_(size) _SAL2_Source_(_Readable_bytes_, (size), _Readable_bytes_impl_(size))
#define _Readable_bytes_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Readable_elements_(size) _SAL2_Source_(_Readable_elements_, (size), _Readable_elements_impl_(size))
#define _Readable_elements_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Writable_bytes_(size) _SAL2_Source_(_Writable_bytes_, (size), _Writable_bytes_impl_(size))
#define _Writable_bytes_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Writable_elements_(size) _SAL2_Source_(_Writable_elements_, (size), _Writable_elements_impl_(size))
#define _Writable_elements_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Null_terminated_ _SAL2_Source_(_Null_terminated_, (), _Null_terminated_impl_)
#define _Null_terminated_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _NullNull_terminated_ _SAL2_Source_(_NullNull_terminated_, (), _NullNull_terminated_impl_)
#define _NullNull_terminated_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_readable_size_(size) _SAL2_Source_(_Pre_readable_size_, (size), _Pre1_impl_(__count_impl(size)) _Pre_valid_impl_)
#define _Pre_readable_size_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_writable_size_(size) _SAL2_Source_(_Pre_writable_size_, (size), _Pre1_impl_(__cap_impl(size)))
#define _Pre_writable_size_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_readable_byte_size_(size) _SAL2_Source_(_Pre_readable_byte_size_, (size), _Pre1_impl_(__bytecount_impl(size)) _Pre_valid_impl_)
#define _Pre_readable_byte_size_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_writable_byte_size_(size) _SAL2_Source_(_Pre_writable_byte_size_, (size), _Pre1_impl_(__bytecap_impl(size)))
#define _Pre_writable_byte_size_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Post_readable_size_(size) _SAL2_Source_(_Post_readable_size_, (size), _Post1_impl_(__count_impl(size)) _Post_valid_impl_)
#define _Post_readable_size_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Post_writable_size_(size) _SAL2_Source_(_Post_writable_size_, (size), _Post1_impl_(__cap_impl(size)))
#define _Post_writable_size_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Post_readable_byte_size_(size) _SAL2_Source_(_Post_readable_byte_size_, (size), _Post1_impl_(__bytecount_impl(size)) _Post_valid_impl_)
#define _Post_readable_byte_size_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Post_writable_byte_size_(size) _SAL2_Source_(_Post_writable_byte_size_, (size), _Post1_impl_(__bytecap_impl(size)))
#define _Post_writable_byte_size_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Null_ _SAL2_Source_(_Null_, (), _Null_impl_)
#define _Null_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Notnull_ _SAL2_Source_(_Notnull_, (), _Notnull_impl_)
#define _Notnull_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Maybenull_ _SAL2_Source_(_Maybenull_, (), _Maybenull_impl_)
#define _Maybenull_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_z_ _SAL2_Source_(_Pre_z_, (), _Pre1_impl_(__zterm_impl) _Pre_valid_impl_)
#define _Pre_z_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_valid_ _SAL2_Source_(_Pre_valid_, (), _Pre1_impl_(__notnull_impl_notref) _Pre_valid_impl_)
#define _Pre_valid_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_opt_valid_ _SAL2_Source_(_Pre_opt_valid_, (), _Pre1_impl_(__maybenull_impl_notref) _Pre_valid_impl_)
#define _Pre_opt_valid_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_invalid_ _SAL2_Source_(_Pre_invalid_, (), _Deref_pre1_impl_(__notvalid_impl))
#define _Pre_invalid_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_unknown_ _SAL2_Source_(_Pre_unknown_, (), _Pre1_impl_(__maybevalid_impl))
#define _Pre_unknown_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_notnull_ _SAL2_Source_(_Pre_notnull_, (), _Pre1_impl_(__notnull_impl_notref))
#define _Pre_notnull_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_maybenull_ _SAL2_Source_(_Pre_maybenull_, (), _Pre1_impl_(__maybenull_impl_notref))
#define _Pre_maybenull_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_null_ _SAL2_Source_(_Pre_null_, (), _Pre1_impl_(__null_impl_notref))
#define _Pre_null_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Post_z_ _SAL2_Source_(_Post_z_, (), _Post1_impl_(__zterm_impl) _Post_valid_impl_)
#define _Post_z_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Post_valid_ _SAL2_Source_(_Post_valid_, (), _Post_valid_impl_)
#define _Post_valid_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Post_invalid_ _SAL2_Source_(_Post_invalid_, (), _Deref_post1_impl_(__notvalid_impl))
#define _Post_invalid_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Post_ptr_invalid_ _SAL2_Source_(_Post_ptr_invalid_, (), _Post1_impl_(__notvalid_impl))
#define _Post_ptr_invalid_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Post_notnull_ _SAL2_Source_(_Post_notnull_, (), _Post1_impl_(__notnull_impl))
#define _Post_notnull_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Post_null_ _SAL2_Source_(_Post_null_, (), _Post1_impl_(__null_impl))
#define _Post_null_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Post_maybenull_ _SAL2_Source_(_Post_maybenull_, (), _Post1_impl_(__maybenull_impl))
#define _Post_maybenull_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Prepost_z_ _SAL2_Source_(_Prepost_z_, (), _Pre_z_ _Post_z_)
#define _Prepost_z_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _In_count_(size) _SAL1_1_Source_(_In_count_, (size), _Pre_count_(size) _Deref_pre_readonly_)
#define _In_count_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _In_opt_count_(size) _SAL1_1_Source_(_In_opt_count_, (size), _Pre_opt_count_(size) _Deref_pre_readonly_)
#define _In_opt_count_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _In_bytecount_(size) _SAL1_1_Source_(_In_bytecount_, (size), _Pre_bytecount_(size) _Deref_pre_readonly_)
#define _In_bytecount_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _In_opt_bytecount_(size) _SAL1_1_Source_(_In_opt_bytecount_, (size), _Pre_opt_bytecount_(size) _Deref_pre_readonly_)
#define _In_opt_bytecount_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _In_count_c_(size) _SAL1_1_Source_(_In_count_c_, (size), _Pre_count_c_(size) _Deref_pre_readonly_)
#define _In_count_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _In_opt_count_c_(size) _SAL1_1_Source_(_In_opt_count_c_, (size), _Pre_opt_count_c_(size) _Deref_pre_readonly_)
#define _In_opt_count_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _In_bytecount_c_(size) _SAL1_1_Source_(_In_bytecount_c_, (size), _Pre_bytecount_c_(size) _Deref_pre_readonly_)
#define _In_bytecount_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _In_opt_bytecount_c_(size) _SAL1_1_Source_(_In_opt_bytecount_c_, (size), _Pre_opt_bytecount_c_(size) _Deref_pre_readonly_)
#define _In_opt_bytecount_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _In_z_count_(size) _SAL1_1_Source_(_In_z_count_, (size), _Pre_z_ _Pre_count_(size) _Deref_pre_readonly_)
#define _In_z_count_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _In_opt_z_count_(size) _SAL1_1_Source_(_In_opt_z_count_, (size), _Pre_opt_z_ _Pre_opt_count_(size) _Deref_pre_readonly_)
#define _In_opt_z_count_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _In_z_bytecount_(size) _SAL1_1_Source_(_In_z_bytecount_, (size), _Pre_z_ _Pre_bytecount_(size) _Deref_pre_readonly_)
#define _In_z_bytecount_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _In_opt_z_bytecount_(size) _SAL1_1_Source_(_In_opt_z_bytecount_, (size), _Pre_opt_z_ _Pre_opt_bytecount_(size) _Deref_pre_readonly_)
#define _In_opt_z_bytecount_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _In_z_count_c_(size) _SAL1_1_Source_(_In_z_count_c_, (size), _Pre_z_ _Pre_count_c_(size) _Deref_pre_readonly_)
#define _In_z_count_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _In_opt_z_count_c_(size) _SAL1_1_Source_(_In_opt_z_count_c_, (size), _Pre_opt_z_ _Pre_opt_count_c_(size) _Deref_pre_readonly_)
#define _In_opt_z_count_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _In_z_bytecount_c_(size) _SAL1_1_Source_(_In_z_bytecount_c_, (size), _Pre_z_ _Pre_bytecount_c_(size) _Deref_pre_readonly_)
#define _In_z_bytecount_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _In_opt_z_bytecount_c_(size) _SAL1_1_Source_(_In_opt_z_bytecount_c_, (size), _Pre_opt_z_ _Pre_opt_bytecount_c_(size) _Deref_pre_readonly_)
#define _In_opt_z_bytecount_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _In_ptrdiff_count_(size) _SAL1_1_Source_(_In_ptrdiff_count_, (size), _Pre_ptrdiff_count_(size) _Deref_pre_readonly_)
#define _In_ptrdiff_count_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _In_opt_ptrdiff_count_(size) _SAL1_1_Source_(_In_opt_ptrdiff_count_, (size), _Pre_opt_ptrdiff_count_(size) _Deref_pre_readonly_)
#define _In_opt_ptrdiff_count_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _In_count_x_(size) _SAL1_1_Source_(_In_count_x_, (size), _Pre_count_x_(size) _Deref_pre_readonly_)
#define _In_count_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _In_opt_count_x_(size) _SAL1_1_Source_(_In_opt_count_x_, (size), _Pre_opt_count_x_(size) _Deref_pre_readonly_)
#define _In_opt_count_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _In_bytecount_x_(size) _SAL1_1_Source_(_In_bytecount_x_, (size), _Pre_bytecount_x_(size) _Deref_pre_readonly_)
#define _In_bytecount_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _In_opt_bytecount_x_(size) _SAL1_1_Source_(_In_opt_bytecount_x_, (size), _Pre_opt_bytecount_x_(size) _Deref_pre_readonly_)
#define _In_opt_bytecount_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_cap_(size) _SAL1_1_Source_(_Out_cap_, (size), _Pre_cap_(size) _Post_valid_impl_)
#define _Out_cap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_opt_cap_(size) _SAL1_1_Source_(_Out_opt_cap_, (size), _Pre_opt_cap_(size) _Post_valid_impl_)
#define _Out_opt_cap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_bytecap_(size) _SAL1_1_Source_(_Out_bytecap_, (size), _Pre_bytecap_(size) _Post_valid_impl_)
#define _Out_bytecap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_opt_bytecap_(size) _SAL1_1_Source_(_Out_opt_bytecap_, (size), _Pre_opt_bytecap_(size) _Post_valid_impl_)
#define _Out_opt_bytecap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_cap_c_(size) _SAL1_1_Source_(_Out_cap_c_, (size), _Pre_cap_c_(size) _Post_valid_impl_)
#define _Out_cap_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_opt_cap_c_(size) _SAL1_1_Source_(_Out_opt_cap_c_, (size), _Pre_opt_cap_c_(size) _Post_valid_impl_)
#define _Out_opt_cap_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_bytecap_c_(size) _SAL1_1_Source_(_Out_bytecap_c_, (size), _Pre_bytecap_c_(size) _Post_valid_impl_)
#define _Out_bytecap_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_opt_bytecap_c_(size) _SAL1_1_Source_(_Out_opt_bytecap_c_, (size), _Pre_opt_bytecap_c_(size) _Post_valid_impl_)
#define _Out_opt_bytecap_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_cap_m_(mult,size) _SAL1_1_Source_(_Out_cap_m_, (mult,size), _Pre_cap_m_(mult,size) _Post_valid_impl_)
#define _Out_cap_m_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_opt_cap_m_(mult,size) _SAL1_1_Source_(_Out_opt_cap_m_, (mult,size), _Pre_opt_cap_m_(mult,size) _Post_valid_impl_)
#define _Out_opt_cap_m_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_z_cap_m_(mult,size) _SAL1_1_Source_(_Out_z_cap_m_, (mult,size), _Pre_cap_m_(mult,size) _Post_valid_impl_ _Post_z_)
#define _Out_z_cap_m_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_opt_z_cap_m_(mult,size) _SAL1_1_Source_(_Out_opt_z_cap_m_, (mult,size), _Pre_opt_cap_m_(mult,size) _Post_valid_impl_ _Post_z_)
#define _Out_opt_z_cap_m_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_ptrdiff_cap_(size) _SAL1_1_Source_(_Out_ptrdiff_cap_, (size), _Pre_ptrdiff_cap_(size) _Post_valid_impl_)
#define _Out_ptrdiff_cap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_opt_ptrdiff_cap_(size) _SAL1_1_Source_(_Out_opt_ptrdiff_cap_, (size), _Pre_opt_ptrdiff_cap_(size) _Post_valid_impl_)
#define _Out_opt_ptrdiff_cap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_cap_x_(size) _SAL1_1_Source_(_Out_cap_x_, (size), _Pre_cap_x_(size) _Post_valid_impl_)
#define _Out_cap_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_opt_cap_x_(size) _SAL1_1_Source_(_Out_opt_cap_x_, (size), _Pre_opt_cap_x_(size) _Post_valid_impl_)
#define _Out_opt_cap_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_bytecap_x_(size) _SAL1_1_Source_(_Out_bytecap_x_, (size), _Pre_bytecap_x_(size) _Post_valid_impl_)
#define _Out_bytecap_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_opt_bytecap_x_(size) _SAL1_1_Source_(_Out_opt_bytecap_x_, (size), _Pre_opt_bytecap_x_(size) _Post_valid_impl_)
#define _Out_opt_bytecap_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_z_cap_(size) _SAL1_1_Source_(_Out_z_cap_, (size), _Pre_cap_(size) _Post_valid_impl_ _Post_z_)
#define _Out_z_cap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_opt_z_cap_(size) _SAL1_1_Source_(_Out_opt_z_cap_, (size), _Pre_opt_cap_(size) _Post_valid_impl_ _Post_z_)
#define _Out_opt_z_cap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_z_bytecap_(size) _SAL1_1_Source_(_Out_z_bytecap_, (size), _Pre_bytecap_(size) _Post_valid_impl_ _Post_z_)
#define _Out_z_bytecap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_opt_z_bytecap_(size) _SAL1_1_Source_(_Out_opt_z_bytecap_, (size), _Pre_opt_bytecap_(size) _Post_valid_impl_ _Post_z_)
#define _Out_opt_z_bytecap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_z_cap_c_(size) _SAL1_1_Source_(_Out_z_cap_c_, (size), _Pre_cap_c_(size) _Post_valid_impl_ _Post_z_)
#define _Out_z_cap_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_opt_z_cap_c_(size) _SAL1_1_Source_(_Out_opt_z_cap_c_, (size), _Pre_opt_cap_c_(size) _Post_valid_impl_ _Post_z_)
#define _Out_opt_z_cap_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_z_bytecap_c_(size) _SAL1_1_Source_(_Out_z_bytecap_c_, (size), _Pre_bytecap_c_(size) _Post_valid_impl_ _Post_z_)
#define _Out_z_bytecap_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_opt_z_bytecap_c_(size) _SAL1_1_Source_(_Out_opt_z_bytecap_c_, (size), _Pre_opt_bytecap_c_(size) _Post_valid_impl_ _Post_z_)
#define _Out_opt_z_bytecap_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_z_cap_x_(size) _SAL1_1_Source_(_Out_z_cap_x_, (size), _Pre_cap_x_(size) _Post_valid_impl_ _Post_z_)
#define _Out_z_cap_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_opt_z_cap_x_(size) _SAL1_1_Source_(_Out_opt_z_cap_x_, (size), _Pre_opt_cap_x_(size) _Post_valid_impl_ _Post_z_)
#define _Out_opt_z_cap_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_z_bytecap_x_(size) _SAL1_1_Source_(_Out_z_bytecap_x_, (size), _Pre_bytecap_x_(size) _Post_valid_impl_ _Post_z_)
#define _Out_z_bytecap_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_opt_z_bytecap_x_(size) _SAL1_1_Source_(_Out_opt_z_bytecap_x_, (size), _Pre_opt_bytecap_x_(size) _Post_valid_impl_ _Post_z_)
#define _Out_opt_z_bytecap_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_cap_post_count_(cap,count) _SAL1_1_Source_(_Out_cap_post_count_, (cap,count), _Pre_cap_(cap) _Post_valid_impl_ _Post_count_(count))
#define _Out_cap_post_count_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_opt_cap_post_count_(cap,count) _SAL1_1_Source_(_Out_opt_cap_post_count_, (cap,count), _Pre_opt_cap_(cap) _Post_valid_impl_ _Post_count_(count))
#define _Out_opt_cap_post_count_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_bytecap_post_bytecount_(cap,count) _SAL1_1_Source_(_Out_bytecap_post_bytecount_, (cap,count), _Pre_bytecap_(cap) _Post_valid_impl_ _Post_bytecount_(count))
#define _Out_bytecap_post_bytecount_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_opt_bytecap_post_bytecount_(cap,count) _SAL1_1_Source_(_Out_opt_bytecap_post_bytecount_, (cap,count), _Pre_opt_bytecap_(cap) _Post_valid_impl_ _Post_bytecount_(count))
#define _Out_opt_bytecap_post_bytecount_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_z_cap_post_count_(cap,count) _SAL1_1_Source_(_Out_z_cap_post_count_, (cap,count), _Pre_cap_(cap) _Post_valid_impl_ _Post_z_count_(count))
#define _Out_z_cap_post_count_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_opt_z_cap_post_count_(cap,count) _SAL1_1_Source_(_Out_opt_z_cap_post_count_, (cap,count), _Pre_opt_cap_(cap) _Post_valid_impl_ _Post_z_count_(count))
#define _Out_opt_z_cap_post_count_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_z_bytecap_post_bytecount_(cap,count) _SAL1_1_Source_(_Out_z_bytecap_post_bytecount_, (cap,count), _Pre_bytecap_(cap) _Post_valid_impl_ _Post_z_bytecount_(count))
#define _Out_z_bytecap_post_bytecount_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_opt_z_bytecap_post_bytecount_(cap,count) _SAL1_1_Source_(_Out_opt_z_bytecap_post_bytecount_, (cap,count), _Pre_opt_bytecap_(cap) _Post_valid_impl_ _Post_z_bytecount_(count))
#define _Out_opt_z_bytecap_post_bytecount_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_capcount_(capcount) _SAL1_1_Source_(_Out_capcount_, (capcount), _Pre_cap_(capcount) _Post_valid_impl_ _Post_count_(capcount))
#define _Out_capcount_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_opt_capcount_(capcount) _SAL1_1_Source_(_Out_opt_capcount_, (capcount), _Pre_opt_cap_(capcount) _Post_valid_impl_ _Post_count_(capcount))
#define _Out_opt_capcount_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_bytecapcount_(capcount) _SAL1_1_Source_(_Out_bytecapcount_, (capcount), _Pre_bytecap_(capcount) _Post_valid_impl_ _Post_bytecount_(capcount))
#define _Out_bytecapcount_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_opt_bytecapcount_(capcount) _SAL1_1_Source_(_Out_opt_bytecapcount_, (capcount), _Pre_opt_bytecap_(capcount) _Post_valid_impl_ _Post_bytecount_(capcount))
#define _Out_opt_bytecapcount_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_capcount_x_(capcount) _SAL1_1_Source_(_Out_capcount_x_, (capcount), _Pre_cap_x_(capcount) _Post_valid_impl_ _Post_count_x_(capcount))
#define _Out_capcount_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_opt_capcount_x_(capcount) _SAL1_1_Source_(_Out_opt_capcount_x_, (capcount), _Pre_opt_cap_x_(capcount) _Post_valid_impl_ _Post_count_x_(capcount))
#define _Out_opt_capcount_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_bytecapcount_x_(capcount) _SAL1_1_Source_(_Out_bytecapcount_x_, (capcount), _Pre_bytecap_x_(capcount) _Post_valid_impl_ _Post_bytecount_x_(capcount))
#define _Out_bytecapcount_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_opt_bytecapcount_x_(capcount) _SAL1_1_Source_(_Out_opt_bytecapcount_x_, (capcount), _Pre_opt_bytecap_x_(capcount) _Post_valid_impl_ _Post_bytecount_x_(capcount))
#define _Out_opt_bytecapcount_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_z_capcount_(capcount) _SAL1_1_Source_(_Out_z_capcount_, (capcount), _Pre_cap_(capcount) _Post_valid_impl_ _Post_z_count_(capcount))
#define _Out_z_capcount_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_opt_z_capcount_(capcount) _SAL1_1_Source_(_Out_opt_z_capcount_, (capcount), _Pre_opt_cap_(capcount) _Post_valid_impl_ _Post_z_count_(capcount))
#define _Out_opt_z_capcount_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_z_bytecapcount_(capcount) _SAL1_1_Source_(_Out_z_bytecapcount_, (capcount), _Pre_bytecap_(capcount) _Post_valid_impl_ _Post_z_bytecount_(capcount))
#define _Out_z_bytecapcount_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_opt_z_bytecapcount_(capcount) _SAL1_1_Source_(_Out_opt_z_bytecapcount_, (capcount), _Pre_opt_bytecap_(capcount) _Post_valid_impl_ _Post_z_bytecount_(capcount))
#define _Out_opt_z_bytecapcount_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Inout_count_(size) _SAL1_1_Source_(_Inout_count_, (size), _Prepost_count_(size))
#define _Inout_count_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Inout_opt_count_(size) _SAL1_1_Source_(_Inout_opt_count_, (size), _Prepost_opt_count_(size))
#define _Inout_opt_count_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Inout_bytecount_(size) _SAL1_1_Source_(_Inout_bytecount_, (size), _Prepost_bytecount_(size))
#define _Inout_bytecount_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Inout_opt_bytecount_(size) _SAL1_1_Source_(_Inout_opt_bytecount_, (size), _Prepost_opt_bytecount_(size))
#define _Inout_opt_bytecount_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Inout_count_c_(size) _SAL1_1_Source_(_Inout_count_c_, (size), _Prepost_count_c_(size))
#define _Inout_count_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Inout_opt_count_c_(size) _SAL1_1_Source_(_Inout_opt_count_c_, (size), _Prepost_opt_count_c_(size))
#define _Inout_opt_count_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Inout_bytecount_c_(size) _SAL1_1_Source_(_Inout_bytecount_c_, (size), _Prepost_bytecount_c_(size))
#define _Inout_bytecount_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Inout_opt_bytecount_c_(size) _SAL1_1_Source_(_Inout_opt_bytecount_c_, (size), _Prepost_opt_bytecount_c_(size))
#define _Inout_opt_bytecount_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Inout_z_count_(size) _SAL1_1_Source_(_Inout_z_count_, (size), _Prepost_z_ _Prepost_count_(size))
#define _Inout_z_count_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Inout_opt_z_count_(size) _SAL1_1_Source_(_Inout_opt_z_count_, (size), _Prepost_z_ _Prepost_opt_count_(size))
#define _Inout_opt_z_count_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Inout_z_bytecount_(size) _SAL1_1_Source_(_Inout_z_bytecount_, (size), _Prepost_z_ _Prepost_bytecount_(size))
#define _Inout_z_bytecount_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Inout_opt_z_bytecount_(size) _SAL1_1_Source_(_Inout_opt_z_bytecount_, (size), _Prepost_z_ _Prepost_opt_bytecount_(size))
#define _Inout_opt_z_bytecount_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Inout_z_count_c_(size) _SAL1_1_Source_(_Inout_z_count_c_, (size), _Prepost_z_ _Prepost_count_c_(size))
#define _Inout_z_count_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Inout_opt_z_count_c_(size) _SAL1_1_Source_(_Inout_opt_z_count_c_, (size), _Prepost_z_ _Prepost_opt_count_c_(size))
#define _Inout_opt_z_count_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Inout_z_bytecount_c_(size) _SAL1_1_Source_(_Inout_z_bytecount_c_, (size), _Prepost_z_ _Prepost_bytecount_c_(size))
#define _Inout_z_bytecount_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Inout_opt_z_bytecount_c_(size) _SAL1_1_Source_(_Inout_opt_z_bytecount_c_, (size), _Prepost_z_ _Prepost_opt_bytecount_c_(size))
#define _Inout_opt_z_bytecount_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Inout_ptrdiff_count_(size) _SAL1_1_Source_(_Inout_ptrdiff_count_, (size), _Pre_ptrdiff_count_(size))
#define _Inout_ptrdiff_count_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Inout_opt_ptrdiff_count_(size) _SAL1_1_Source_(_Inout_opt_ptrdiff_count_, (size), _Pre_opt_ptrdiff_count_(size))
#define _Inout_opt_ptrdiff_count_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Inout_count_x_(size) _SAL1_1_Source_(_Inout_count_x_, (size), _Prepost_count_x_(size))
#define _Inout_count_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Inout_opt_count_x_(size) _SAL1_1_Source_(_Inout_opt_count_x_, (size), _Prepost_opt_count_x_(size))
#define _Inout_opt_count_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Inout_bytecount_x_(size) _SAL1_1_Source_(_Inout_bytecount_x_, (size), _Prepost_bytecount_x_(size))
#define _Inout_bytecount_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Inout_opt_bytecount_x_(size) _SAL1_1_Source_(_Inout_opt_bytecount_x_, (size), _Prepost_opt_bytecount_x_(size))
#define _Inout_opt_bytecount_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Inout_cap_(size) _SAL1_1_Source_(_Inout_cap_, (size), _Pre_valid_cap_(size) _Post_valid_)
#define _Inout_cap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Inout_opt_cap_(size) _SAL1_1_Source_(_Inout_opt_cap_, (size), _Pre_opt_valid_cap_(size) _Post_valid_)
#define _Inout_opt_cap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Inout_bytecap_(size) _SAL1_1_Source_(_Inout_bytecap_, (size), _Pre_valid_bytecap_(size) _Post_valid_)
#define _Inout_bytecap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Inout_opt_bytecap_(size) _SAL1_1_Source_(_Inout_opt_bytecap_, (size), _Pre_opt_valid_bytecap_(size) _Post_valid_)
#define _Inout_opt_bytecap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Inout_cap_c_(size) _SAL1_1_Source_(_Inout_cap_c_, (size), _Pre_valid_cap_c_(size) _Post_valid_)
#define _Inout_cap_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Inout_opt_cap_c_(size) _SAL1_1_Source_(_Inout_opt_cap_c_, (size), _Pre_opt_valid_cap_c_(size) _Post_valid_)
#define _Inout_opt_cap_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Inout_bytecap_c_(size) _SAL1_1_Source_(_Inout_bytecap_c_, (size), _Pre_valid_bytecap_c_(size) _Post_valid_)
#define _Inout_bytecap_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Inout_opt_bytecap_c_(size) _SAL1_1_Source_(_Inout_opt_bytecap_c_, (size), _Pre_opt_valid_bytecap_c_(size) _Post_valid_)
#define _Inout_opt_bytecap_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Inout_cap_x_(size) _SAL1_1_Source_(_Inout_cap_x_, (size), _Pre_valid_cap_x_(size) _Post_valid_)
#define _Inout_cap_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Inout_opt_cap_x_(size) _SAL1_1_Source_(_Inout_opt_cap_x_, (size), _Pre_opt_valid_cap_x_(size) _Post_valid_)
#define _Inout_opt_cap_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Inout_bytecap_x_(size) _SAL1_1_Source_(_Inout_bytecap_x_, (size), _Pre_valid_bytecap_x_(size) _Post_valid_)
#define _Inout_bytecap_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Inout_opt_bytecap_x_(size) _SAL1_1_Source_(_Inout_opt_bytecap_x_, (size), _Pre_opt_valid_bytecap_x_(size) _Post_valid_)
#define _Inout_opt_bytecap_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Inout_z_cap_(size) _SAL1_1_Source_(_Inout_z_cap_, (size), _Pre_z_cap_(size) _Post_z_)
#define _Inout_z_cap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Inout_opt_z_cap_(size) _SAL1_1_Source_(_Inout_opt_z_cap_, (size), _Pre_opt_z_cap_(size) _Post_z_)
#define _Inout_opt_z_cap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Inout_z_bytecap_(size) _SAL1_1_Source_(_Inout_z_bytecap_, (size), _Pre_z_bytecap_(size) _Post_z_)
#define _Inout_z_bytecap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Inout_opt_z_bytecap_(size) _SAL1_1_Source_(_Inout_opt_z_bytecap_, (size), _Pre_opt_z_bytecap_(size) _Post_z_)
#define _Inout_opt_z_bytecap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Inout_z_cap_c_(size) _SAL1_1_Source_(_Inout_z_cap_c_, (size), _Pre_z_cap_c_(size) _Post_z_)
#define _Inout_z_cap_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Inout_opt_z_cap_c_(size) _SAL1_1_Source_(_Inout_opt_z_cap_c_, (size), _Pre_opt_z_cap_c_(size) _Post_z_)
#define _Inout_opt_z_cap_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Inout_z_bytecap_c_(size) _SAL1_1_Source_(_Inout_z_bytecap_c_, (size), _Pre_z_bytecap_c_(size) _Post_z_)
#define _Inout_z_bytecap_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Inout_opt_z_bytecap_c_(size) _SAL1_1_Source_(_Inout_opt_z_bytecap_c_, (size), _Pre_opt_z_bytecap_c_(size) _Post_z_)
#define _Inout_opt_z_bytecap_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Inout_z_cap_x_(size) _SAL1_1_Source_(_Inout_z_cap_x_, (size), _Pre_z_cap_x_(size) _Post_z_)
#define _Inout_z_cap_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Inout_opt_z_cap_x_(size) _SAL1_1_Source_(_Inout_opt_z_cap_x_, (size), _Pre_opt_z_cap_x_(size) _Post_z_)
#define _Inout_opt_z_cap_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Inout_z_bytecap_x_(size) _SAL1_1_Source_(_Inout_z_bytecap_x_, (size), _Pre_z_bytecap_x_(size) _Post_z_)
#define _Inout_z_bytecap_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Inout_opt_z_bytecap_x_(size) _SAL1_1_Source_(_Inout_opt_z_bytecap_x_, (size), _Pre_opt_z_bytecap_x_(size) _Post_z_)
#define _Inout_opt_z_bytecap_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Ret_ _SAL1_1_Source_(_Ret_, (), _Ret_valid_)
#define _Ret_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Ret_opt_ _SAL1_1_Source_(_Ret_opt_, (), _Ret_opt_valid_)
#define _Ret_opt_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _In_bound_ _SAL1_1_Source_(_In_bound_, (), _In_bound_impl_)
#define _In_bound_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_bound_ _SAL1_1_Source_(_Out_bound_, (), _Out_bound_impl_)
#define _Out_bound_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Ret_bound_ _SAL1_1_Source_(_Ret_bound_, (), _Ret_bound_impl_)
#define _Ret_bound_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_in_bound_ _SAL1_1_Source_(_Deref_in_bound_, (), _Deref_in_bound_impl_)
#define _Deref_in_bound_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_out_bound_ _SAL1_1_Source_(_Deref_out_bound_, (), _Deref_out_bound_impl_)
#define _Deref_out_bound_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_inout_bound_ _SAL1_1_Source_(_Deref_inout_bound_, (), _Deref_in_bound_ _Deref_out_bound_)
#define _Deref_inout_bound_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_ret_bound_ _SAL1_1_Source_(_Deref_ret_bound_, (), _Deref_ret_bound_impl_)
#define _Deref_ret_bound_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_out_ _SAL1_1_Source_(_Deref_out_, (), _Out_ _Deref_post_valid_)
#define _Deref_out_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_out_opt_ _SAL1_1_Source_(_Deref_out_opt_, (), _Out_ _Deref_post_opt_valid_)
#define _Deref_out_opt_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_opt_out_ _SAL1_1_Source_(_Deref_opt_out_, (), _Out_opt_ _Deref_post_valid_)
#define _Deref_opt_out_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_opt_out_opt_ _SAL1_1_Source_(_Deref_opt_out_opt_, (), _Out_opt_ _Deref_post_opt_valid_)
#define _Deref_opt_out_opt_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_out_z_ _SAL1_1_Source_(_Deref_out_z_, (), _Out_ _Deref_post_z_)
#define _Deref_out_z_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_out_opt_z_ _SAL1_1_Source_(_Deref_out_opt_z_, (), _Out_ _Deref_post_opt_z_)
#define _Deref_out_opt_z_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_opt_out_z_ _SAL1_1_Source_(_Deref_opt_out_z_, (), _Out_opt_ _Deref_post_z_)
#define _Deref_opt_out_z_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_opt_out_opt_z_ _SAL1_1_Source_(_Deref_opt_out_opt_z_, (), _Out_opt_ _Deref_post_opt_z_)
#define _Deref_opt_out_opt_z_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_pre_z_ _SAL1_1_Source_(_Deref_pre_z_, (), _Deref_pre1_impl_(__notnull_impl_notref) _Deref_pre1_impl_(__zterm_impl) _Pre_valid_impl_)
#define _Deref_pre_z_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_pre_opt_z_ _SAL1_1_Source_(_Deref_pre_opt_z_, (), _Deref_pre1_impl_(__maybenull_impl_notref) _Deref_pre1_impl_(__zterm_impl) _Pre_valid_impl_)
#define _Deref_pre_opt_z_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_pre_cap_(size) _SAL1_1_Source_(_Deref_pre_cap_, (size), _Deref_pre1_impl_(__notnull_impl_notref) _Deref_pre1_impl_(__cap_impl(size)))
#define _Deref_pre_cap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_pre_opt_cap_(size) _SAL1_1_Source_(_Deref_pre_opt_cap_, (size), _Deref_pre1_impl_(__maybenull_impl_notref) _Deref_pre1_impl_(__cap_impl(size)))
#define _Deref_pre_opt_cap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_pre_bytecap_(size) _SAL1_1_Source_(_Deref_pre_bytecap_, (size), _Deref_pre1_impl_(__notnull_impl_notref) _Deref_pre1_impl_(__bytecap_impl(size)))
#define _Deref_pre_bytecap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_pre_opt_bytecap_(size) _SAL1_1_Source_(_Deref_pre_opt_bytecap_, (size), _Deref_pre1_impl_(__maybenull_impl_notref) _Deref_pre1_impl_(__bytecap_impl(size)))
#define _Deref_pre_opt_bytecap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_pre_cap_c_(size) _SAL1_1_Source_(_Deref_pre_cap_c_, (size), _Deref_pre1_impl_(__notnull_impl_notref) _Deref_pre1_impl_(__cap_c_impl(size)))
#define _Deref_pre_cap_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_pre_opt_cap_c_(size) _SAL1_1_Source_(_Deref_pre_opt_cap_c_, (size), _Deref_pre1_impl_(__maybenull_impl_notref) _Deref_pre1_impl_(__cap_c_impl(size)))
#define _Deref_pre_opt_cap_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_pre_bytecap_c_(size) _SAL1_1_Source_(_Deref_pre_bytecap_c_, (size), _Deref_pre1_impl_(__notnull_impl_notref) _Deref_pre1_impl_(__bytecap_c_impl(size)))
#define _Deref_pre_bytecap_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_pre_opt_bytecap_c_(size) _SAL1_1_Source_(_Deref_pre_opt_bytecap_c_, (size), _Deref_pre1_impl_(__maybenull_impl_notref) _Deref_pre1_impl_(__bytecap_c_impl(size)))
#define _Deref_pre_opt_bytecap_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_pre_cap_x_(size) _SAL1_1_Source_(_Deref_pre_cap_x_, (size), _Deref_pre1_impl_(__notnull_impl_notref) _Deref_pre1_impl_(__cap_x_impl(size)))
#define _Deref_pre_cap_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_pre_opt_cap_x_(size) _SAL1_1_Source_(_Deref_pre_opt_cap_x_, (size), _Deref_pre1_impl_(__maybenull_impl_notref) _Deref_pre1_impl_(__cap_x_impl(size)))
#define _Deref_pre_opt_cap_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_pre_bytecap_x_(size) _SAL1_1_Source_(_Deref_pre_bytecap_x_, (size), _Deref_pre1_impl_(__notnull_impl_notref) _Deref_pre1_impl_(__bytecap_x_impl(size)))
#define _Deref_pre_bytecap_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_pre_opt_bytecap_x_(size) _SAL1_1_Source_(_Deref_pre_opt_bytecap_x_, (size), _Deref_pre1_impl_(__maybenull_impl_notref) _Deref_pre1_impl_(__bytecap_x_impl(size)))
#define _Deref_pre_opt_bytecap_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_pre_z_cap_(size) _SAL1_1_Source_(_Deref_pre_z_cap_, (size), _Deref_pre1_impl_(__notnull_impl_notref) _Deref_pre2_impl_(__zterm_impl,__cap_impl(size)) _Pre_valid_impl_)
#define _Deref_pre_z_cap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_pre_opt_z_cap_(size) _SAL1_1_Source_(_Deref_pre_opt_z_cap_, (size), _Deref_pre1_impl_(__maybenull_impl_notref) _Deref_pre2_impl_(__zterm_impl,__cap_impl(size)) _Pre_valid_impl_)
#define _Deref_pre_opt_z_cap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_pre_z_bytecap_(size) _SAL1_1_Source_(_Deref_pre_z_bytecap_, (size), _Deref_pre1_impl_(__notnull_impl_notref) _Deref_pre2_impl_(__zterm_impl,__bytecap_impl(size)) _Pre_valid_impl_)
#define _Deref_pre_z_bytecap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_pre_opt_z_bytecap_(size) _SAL1_1_Source_(_Deref_pre_opt_z_bytecap_, (size), _Deref_pre1_impl_(__maybenull_impl_notref) _Deref_pre2_impl_(__zterm_impl,__bytecap_impl(size)) _Pre_valid_impl_)
#define _Deref_pre_opt_z_bytecap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_pre_z_cap_c_(size) _SAL1_1_Source_(_Deref_pre_z_cap_c_, (size), _Deref_pre1_impl_(__notnull_impl_notref) _Deref_pre2_impl_(__zterm_impl,__cap_c_impl(size)) _Pre_valid_impl_)
#define _Deref_pre_z_cap_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_pre_opt_z_cap_c_(size) _SAL1_1_Source_(_Deref_pre_opt_z_cap_c_, (size), _Deref_pre1_impl_(__maybenull_impl_notref) _Deref_pre2_impl_(__zterm_impl,__cap_c_impl(size)) _Pre_valid_impl_)
#define _Deref_pre_opt_z_cap_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_pre_z_bytecap_c_(size) _SAL1_1_Source_(_Deref_pre_z_bytecap_c_, (size), _Deref_pre1_impl_(__notnull_impl_notref) _Deref_pre2_impl_(__zterm_impl,__bytecap_c_impl(size)) _Pre_valid_impl_)
#define _Deref_pre_z_bytecap_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_pre_opt_z_bytecap_c_(size) _SAL1_1_Source_(_Deref_pre_opt_z_bytecap_c_, (size), _Deref_pre1_impl_(__maybenull_impl_notref) _Deref_pre2_impl_(__zterm_impl,__bytecap_c_impl(size)) _Pre_valid_impl_)
#define _Deref_pre_opt_z_bytecap_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_pre_z_cap_x_(size) _SAL1_1_Source_(_Deref_pre_z_cap_x_, (size), _Deref_pre1_impl_(__notnull_impl_notref) _Deref_pre2_impl_(__zterm_impl,__cap_x_impl(size)) _Pre_valid_impl_)
#define _Deref_pre_z_cap_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_pre_opt_z_cap_x_(size) _SAL1_1_Source_(_Deref_pre_opt_z_cap_x_, (size), _Deref_pre1_impl_(__maybenull_impl_notref) _Deref_pre2_impl_(__zterm_impl,__cap_x_impl(size)) _Pre_valid_impl_)
#define _Deref_pre_opt_z_cap_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_pre_z_bytecap_x_(size) _SAL1_1_Source_(_Deref_pre_z_bytecap_x_, (size), _Deref_pre1_impl_(__notnull_impl_notref) _Deref_pre2_impl_(__zterm_impl,__bytecap_x_impl(size)) _Pre_valid_impl_)
#define _Deref_pre_z_bytecap_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_pre_opt_z_bytecap_x_(size) _SAL1_1_Source_(_Deref_pre_opt_z_bytecap_x_, (size), _Deref_pre1_impl_(__maybenull_impl_notref) _Deref_pre2_impl_(__zterm_impl,__bytecap_x_impl(size)) _Pre_valid_impl_)
#define _Deref_pre_opt_z_bytecap_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_pre_valid_cap_(size) _SAL1_1_Source_(_Deref_pre_valid_cap_, (size), _Deref_pre1_impl_(__notnull_impl_notref) _Deref_pre1_impl_(__cap_impl(size)) _Pre_valid_impl_)
#define _Deref_pre_valid_cap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_pre_opt_valid_cap_(size) _SAL1_1_Source_(_Deref_pre_opt_valid_cap_, (size), _Deref_pre1_impl_(__maybenull_impl_notref) _Deref_pre1_impl_(__cap_impl(size)) _Pre_valid_impl_)
#define _Deref_pre_opt_valid_cap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_pre_valid_bytecap_(size) _SAL1_1_Source_(_Deref_pre_valid_bytecap_, (size), _Deref_pre1_impl_(__notnull_impl_notref) _Deref_pre1_impl_(__bytecap_impl(size)) _Pre_valid_impl_)
#define _Deref_pre_valid_bytecap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_pre_opt_valid_bytecap_(size) _SAL1_1_Source_(_Deref_pre_opt_valid_bytecap_, (size), _Deref_pre1_impl_(__maybenull_impl_notref) _Deref_pre1_impl_(__bytecap_impl(size)) _Pre_valid_impl_)
#define _Deref_pre_opt_valid_bytecap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_pre_valid_cap_c_(size) _SAL1_1_Source_(_Deref_pre_valid_cap_c_, (size), _Deref_pre1_impl_(__notnull_impl_notref) _Deref_pre1_impl_(__cap_c_impl(size)) _Pre_valid_impl_)
#define _Deref_pre_valid_cap_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_pre_opt_valid_cap_c_(size) _SAL1_1_Source_(_Deref_pre_opt_valid_cap_c_, (size), _Deref_pre1_impl_(__maybenull_impl_notref) _Deref_pre1_impl_(__cap_c_impl(size)) _Pre_valid_impl_)
#define _Deref_pre_opt_valid_cap_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_pre_valid_bytecap_c_(size) _SAL1_1_Source_(_Deref_pre_valid_bytecap_c_, (size), _Deref_pre1_impl_(__notnull_impl_notref) _Deref_pre1_impl_(__bytecap_c_impl(size)) _Pre_valid_impl_)
#define _Deref_pre_valid_bytecap_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_pre_opt_valid_bytecap_c_(size) _SAL1_1_Source_(_Deref_pre_opt_valid_bytecap_c_, (size), _Deref_pre1_impl_(__maybenull_impl_notref) _Deref_pre1_impl_(__bytecap_c_impl(size)) _Pre_valid_impl_)
#define _Deref_pre_opt_valid_bytecap_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_pre_valid_cap_x_(size) _SAL1_1_Source_(_Deref_pre_valid_cap_x_, (size), _Deref_pre1_impl_(__notnull_impl_notref) _Deref_pre1_impl_(__cap_x_impl(size)) _Pre_valid_impl_)
#define _Deref_pre_valid_cap_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_pre_opt_valid_cap_x_(size) _SAL1_1_Source_(_Deref_pre_opt_valid_cap_x_, (size), _Deref_pre1_impl_(__maybenull_impl_notref) _Deref_pre1_impl_(__cap_x_impl(size)) _Pre_valid_impl_)
#define _Deref_pre_opt_valid_cap_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_pre_valid_bytecap_x_(size) _SAL1_1_Source_(_Deref_pre_valid_bytecap_x_, (size), _Deref_pre1_impl_(__notnull_impl_notref) _Deref_pre1_impl_(__bytecap_x_impl(size)) _Pre_valid_impl_)
#define _Deref_pre_valid_bytecap_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_pre_opt_valid_bytecap_x_(size) _SAL1_1_Source_(_Deref_pre_opt_valid_bytecap_x_, (size), _Deref_pre1_impl_(__maybenull_impl_notref) _Deref_pre1_impl_(__bytecap_x_impl(size)) _Pre_valid_impl_)
#define _Deref_pre_opt_valid_bytecap_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_pre_count_(size) _SAL1_1_Source_(_Deref_pre_count_, (size), _Deref_pre1_impl_(__notnull_impl_notref) _Deref_pre1_impl_(__count_impl(size)) _Pre_valid_impl_)
#define _Deref_pre_count_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_pre_opt_count_(size) _SAL1_1_Source_(_Deref_pre_opt_count_, (size), _Deref_pre1_impl_(__maybenull_impl_notref) _Deref_pre1_impl_(__count_impl(size)) _Pre_valid_impl_)
#define _Deref_pre_opt_count_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_pre_bytecount_(size) _SAL1_1_Source_(_Deref_pre_bytecount_, (size), _Deref_pre1_impl_(__notnull_impl_notref) _Deref_pre1_impl_(__bytecount_impl(size)) _Pre_valid_impl_)
#define _Deref_pre_bytecount_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_pre_opt_bytecount_(size) _SAL1_1_Source_(_Deref_pre_opt_bytecount_, (size), _Deref_pre1_impl_(__maybenull_impl_notref) _Deref_pre1_impl_(__bytecount_impl(size)) _Pre_valid_impl_)
#define _Deref_pre_opt_bytecount_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_pre_count_c_(size) _SAL1_1_Source_(_Deref_pre_count_c_, (size), _Deref_pre1_impl_(__notnull_impl_notref) _Deref_pre1_impl_(__count_c_impl(size)) _Pre_valid_impl_)
#define _Deref_pre_count_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_pre_opt_count_c_(size) _SAL1_1_Source_(_Deref_pre_opt_count_c_, (size), _Deref_pre1_impl_(__maybenull_impl_notref) _Deref_pre1_impl_(__count_c_impl(size)) _Pre_valid_impl_)
#define _Deref_pre_opt_count_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_pre_bytecount_c_(size) _SAL1_1_Source_(_Deref_pre_bytecount_c_, (size), _Deref_pre1_impl_(__notnull_impl_notref) _Deref_pre1_impl_(__bytecount_c_impl(size)) _Pre_valid_impl_)
#define _Deref_pre_bytecount_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_pre_opt_bytecount_c_(size) _SAL1_1_Source_(_Deref_pre_opt_bytecount_c_, (size), _Deref_pre1_impl_(__maybenull_impl_notref) _Deref_pre1_impl_(__bytecount_c_impl(size)) _Pre_valid_impl_)
#define _Deref_pre_opt_bytecount_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_pre_count_x_(size) _SAL1_1_Source_(_Deref_pre_count_x_, (size), _Deref_pre1_impl_(__notnull_impl_notref) _Deref_pre1_impl_(__count_x_impl(size)) _Pre_valid_impl_)
#define _Deref_pre_count_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_pre_opt_count_x_(size) _SAL1_1_Source_(_Deref_pre_opt_count_x_, (size), _Deref_pre1_impl_(__maybenull_impl_notref) _Deref_pre1_impl_(__count_x_impl(size)) _Pre_valid_impl_)
#define _Deref_pre_opt_count_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_pre_bytecount_x_(size) _SAL1_1_Source_(_Deref_pre_bytecount_x_, (size), _Deref_pre1_impl_(__notnull_impl_notref) _Deref_pre1_impl_(__bytecount_x_impl(size)) _Pre_valid_impl_)
#define _Deref_pre_bytecount_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_pre_opt_bytecount_x_(size) _SAL1_1_Source_(_Deref_pre_opt_bytecount_x_, (size), _Deref_pre1_impl_(__maybenull_impl_notref) _Deref_pre1_impl_(__bytecount_x_impl(size)) _Pre_valid_impl_)
#define _Deref_pre_opt_bytecount_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_pre_valid_ _SAL1_1_Source_(_Deref_pre_valid_, (), _Deref_pre1_impl_(__notnull_impl_notref) _Pre_valid_impl_)
#define _Deref_pre_valid_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_pre_opt_valid_ _SAL1_1_Source_(_Deref_pre_opt_valid_, (), _Deref_pre1_impl_(__maybenull_impl_notref) _Pre_valid_impl_)
#define _Deref_pre_opt_valid_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_pre_invalid_ _SAL1_1_Source_(_Deref_pre_invalid_, (), _Deref_pre1_impl_(__notvalid_impl))
#define _Deref_pre_invalid_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_pre_notnull_ _SAL1_1_Source_(_Deref_pre_notnull_, (), _Deref_pre1_impl_(__notnull_impl_notref))
#define _Deref_pre_notnull_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_pre_maybenull_ _SAL1_1_Source_(_Deref_pre_maybenull_, (), _Deref_pre1_impl_(__maybenull_impl_notref))
#define _Deref_pre_maybenull_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_pre_null_ _SAL1_1_Source_(_Deref_pre_null_, (), _Deref_pre1_impl_(__null_impl_notref))
#define _Deref_pre_null_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_pre_readonly_ _SAL1_1_Source_(_Deref_pre_readonly_, (), _Deref_pre1_impl_(__readaccess_impl_notref))
#define _Deref_pre_readonly_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_pre_writeonly_ _SAL1_1_Source_(_Deref_pre_writeonly_, (), _Deref_pre1_impl_(__writeaccess_impl_notref))
#define _Deref_pre_writeonly_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_post_z_ _SAL1_1_Source_(_Deref_post_z_, (), _Deref_post1_impl_(__notnull_impl_notref) _Deref_post1_impl_(__zterm_impl) _Post_valid_impl_)
#define _Deref_post_z_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_post_opt_z_ _SAL1_1_Source_(_Deref_post_opt_z_, (), _Deref_post1_impl_(__maybenull_impl_notref) _Deref_post1_impl_(__zterm_impl) _Post_valid_impl_)
#define _Deref_post_opt_z_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_post_cap_(size) _SAL1_1_Source_(_Deref_post_cap_, (size), _Deref_post1_impl_(__notnull_impl_notref) _Deref_post1_impl_(__cap_impl(size)))
#define _Deref_post_cap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_post_opt_cap_(size) _SAL1_1_Source_(_Deref_post_opt_cap_, (size), _Deref_post1_impl_(__maybenull_impl_notref) _Deref_post1_impl_(__cap_impl(size)))
#define _Deref_post_opt_cap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_post_bytecap_(size) _SAL1_1_Source_(_Deref_post_bytecap_, (size), _Deref_post1_impl_(__notnull_impl_notref) _Deref_post1_impl_(__bytecap_impl(size)))
#define _Deref_post_bytecap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_post_opt_bytecap_(size) _SAL1_1_Source_(_Deref_post_opt_bytecap_, (size), _Deref_post1_impl_(__maybenull_impl_notref) _Deref_post1_impl_(__bytecap_impl(size)))
#define _Deref_post_opt_bytecap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_post_cap_c_(size) _SAL1_1_Source_(_Deref_post_cap_c_, (size), _Deref_post1_impl_(__notnull_impl_notref) _Deref_post1_impl_(__cap_c_impl(size)))
#define _Deref_post_cap_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_post_opt_cap_c_(size) _SAL1_1_Source_(_Deref_post_opt_cap_c_, (size), _Deref_post1_impl_(__maybenull_impl_notref) _Deref_post1_impl_(__cap_c_impl(size)))
#define _Deref_post_opt_cap_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_post_bytecap_c_(size) _SAL1_1_Source_(_Deref_post_bytecap_c_, (size), _Deref_post1_impl_(__notnull_impl_notref) _Deref_post1_impl_(__bytecap_c_impl(size)))
#define _Deref_post_bytecap_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_post_opt_bytecap_c_(size) _SAL1_1_Source_(_Deref_post_opt_bytecap_c_, (size), _Deref_post1_impl_(__maybenull_impl_notref) _Deref_post1_impl_(__bytecap_c_impl(size)))
#define _Deref_post_opt_bytecap_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_post_cap_x_(size) _SAL1_1_Source_(_Deref_post_cap_x_, (size), _Deref_post1_impl_(__notnull_impl_notref) _Deref_post1_impl_(__cap_x_impl(size)))
#define _Deref_post_cap_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_post_opt_cap_x_(size) _SAL1_1_Source_(_Deref_post_opt_cap_x_, (size), _Deref_post1_impl_(__maybenull_impl_notref) _Deref_post1_impl_(__cap_x_impl(size)))
#define _Deref_post_opt_cap_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_post_bytecap_x_(size) _SAL1_1_Source_(_Deref_post_bytecap_x_, (size), _Deref_post1_impl_(__notnull_impl_notref) _Deref_post1_impl_(__bytecap_x_impl(size)))
#define _Deref_post_bytecap_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_post_opt_bytecap_x_(size) _SAL1_1_Source_(_Deref_post_opt_bytecap_x_, (size), _Deref_post1_impl_(__maybenull_impl_notref) _Deref_post1_impl_(__bytecap_x_impl(size)))
#define _Deref_post_opt_bytecap_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_post_z_cap_(size) _SAL1_1_Source_(_Deref_post_z_cap_, (size), _Deref_post1_impl_(__notnull_impl_notref) _Deref_post2_impl_(__zterm_impl,__cap_impl(size)) _Post_valid_impl_)
#define _Deref_post_z_cap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_post_opt_z_cap_(size) _SAL1_1_Source_(_Deref_post_opt_z_cap_, (size), _Deref_post1_impl_(__maybenull_impl_notref) _Deref_post2_impl_(__zterm_impl,__cap_impl(size)) _Post_valid_impl_)
#define _Deref_post_opt_z_cap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_post_z_bytecap_(size) _SAL1_1_Source_(_Deref_post_z_bytecap_, (size), _Deref_post1_impl_(__notnull_impl_notref) _Deref_post2_impl_(__zterm_impl,__bytecap_impl(size)) _Post_valid_impl_)
#define _Deref_post_z_bytecap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_post_opt_z_bytecap_(size) _SAL1_1_Source_(_Deref_post_opt_z_bytecap_, (size), _Deref_post1_impl_(__maybenull_impl_notref) _Deref_post2_impl_(__zterm_impl,__bytecap_impl(size)) _Post_valid_impl_)
#define _Deref_post_opt_z_bytecap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_post_z_cap_c_(size) _SAL1_1_Source_(_Deref_post_z_cap_c_, (size), _Deref_post1_impl_(__notnull_impl_notref) _Deref_post2_impl_(__zterm_impl,__cap_c_impl(size)) _Post_valid_impl_)
#define _Deref_post_z_cap_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_post_opt_z_cap_c_(size) _SAL1_1_Source_(_Deref_post_opt_z_cap_c_, (size), _Deref_post1_impl_(__maybenull_impl_notref) _Deref_post2_impl_(__zterm_impl,__cap_c_impl(size)) _Post_valid_impl_)
#define _Deref_post_opt_z_cap_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_post_z_bytecap_c_(size) _SAL1_1_Source_(_Deref_post_z_bytecap_c_, (size), _Deref_post1_impl_(__notnull_impl_notref) _Deref_post2_impl_(__zterm_impl,__bytecap_c_impl(size)) _Post_valid_impl_)
#define _Deref_post_z_bytecap_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_post_opt_z_bytecap_c_(size) _SAL1_1_Source_(_Deref_post_opt_z_bytecap_c_, (size), _Deref_post1_impl_(__maybenull_impl_notref) _Deref_post2_impl_(__zterm_impl,__bytecap_c_impl(size)) _Post_valid_impl_)
#define _Deref_post_opt_z_bytecap_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_post_z_cap_x_(size) _SAL1_1_Source_(_Deref_post_z_cap_x_, (size), _Deref_post1_impl_(__notnull_impl_notref) _Deref_post2_impl_(__zterm_impl,__cap_x_impl(size)) _Post_valid_impl_)
#define _Deref_post_z_cap_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_post_opt_z_cap_x_(size) _SAL1_1_Source_(_Deref_post_opt_z_cap_x_, (size), _Deref_post1_impl_(__maybenull_impl_notref) _Deref_post2_impl_(__zterm_impl,__cap_x_impl(size)) _Post_valid_impl_)
#define _Deref_post_opt_z_cap_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_post_z_bytecap_x_(size) _SAL1_1_Source_(_Deref_post_z_bytecap_x_, (size), _Deref_post1_impl_(__notnull_impl_notref) _Deref_post2_impl_(__zterm_impl,__bytecap_x_impl(size)) _Post_valid_impl_)
#define _Deref_post_z_bytecap_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_post_opt_z_bytecap_x_(size) _SAL1_1_Source_(_Deref_post_opt_z_bytecap_x_, (size), _Deref_post1_impl_(__maybenull_impl_notref) _Deref_post2_impl_(__zterm_impl,__bytecap_x_impl(size)) _Post_valid_impl_)
#define _Deref_post_opt_z_bytecap_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_post_valid_cap_(size) _SAL1_1_Source_(_Deref_post_valid_cap_, (size), _Deref_post1_impl_(__notnull_impl_notref) _Deref_post1_impl_(__cap_impl(size)) _Post_valid_impl_)
#define _Deref_post_valid_cap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_post_opt_valid_cap_(size) _SAL1_1_Source_(_Deref_post_opt_valid_cap_, (size), _Deref_post1_impl_(__maybenull_impl_notref) _Deref_post1_impl_(__cap_impl(size)) _Post_valid_impl_)
#define _Deref_post_opt_valid_cap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_post_valid_bytecap_(size) _SAL1_1_Source_(_Deref_post_valid_bytecap_, (size), _Deref_post1_impl_(__notnull_impl_notref) _Deref_post1_impl_(__bytecap_impl(size)) _Post_valid_impl_)
#define _Deref_post_valid_bytecap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_post_opt_valid_bytecap_(size) _SAL1_1_Source_(_Deref_post_opt_valid_bytecap_, (size), _Deref_post1_impl_(__maybenull_impl_notref) _Deref_post1_impl_(__bytecap_impl(size)) _Post_valid_impl_)
#define _Deref_post_opt_valid_bytecap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_post_valid_cap_c_(size) _SAL1_1_Source_(_Deref_post_valid_cap_c_, (size), _Deref_post1_impl_(__notnull_impl_notref) _Deref_post1_impl_(__cap_c_impl(size)) _Post_valid_impl_)
#define _Deref_post_valid_cap_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_post_opt_valid_cap_c_(size) _SAL1_1_Source_(_Deref_post_opt_valid_cap_c_, (size), _Deref_post1_impl_(__maybenull_impl_notref) _Deref_post1_impl_(__cap_c_impl(size)) _Post_valid_impl_)
#define _Deref_post_opt_valid_cap_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_post_valid_bytecap_c_(size) _SAL1_1_Source_(_Deref_post_valid_bytecap_c_, (size), _Deref_post1_impl_(__notnull_impl_notref) _Deref_post1_impl_(__bytecap_c_impl(size)) _Post_valid_impl_)
#define _Deref_post_valid_bytecap_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_post_opt_valid_bytecap_c_(size) _SAL1_1_Source_(_Deref_post_opt_valid_bytecap_c_, (size), _Deref_post1_impl_(__maybenull_impl_notref) _Deref_post1_impl_(__bytecap_c_impl(size)) _Post_valid_impl_)
#define _Deref_post_opt_valid_bytecap_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_post_valid_cap_x_(size) _SAL1_1_Source_(_Deref_post_valid_cap_x_, (size), _Deref_post1_impl_(__notnull_impl_notref) _Deref_post1_impl_(__cap_x_impl(size)) _Post_valid_impl_)
#define _Deref_post_valid_cap_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_post_opt_valid_cap_x_(size) _SAL1_1_Source_(_Deref_post_opt_valid_cap_x_, (size), _Deref_post1_impl_(__maybenull_impl_notref) _Deref_post1_impl_(__cap_x_impl(size)) _Post_valid_impl_)
#define _Deref_post_opt_valid_cap_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_post_valid_bytecap_x_(size) _SAL1_1_Source_(_Deref_post_valid_bytecap_x_, (size), _Deref_post1_impl_(__notnull_impl_notref) _Deref_post1_impl_(__bytecap_x_impl(size)) _Post_valid_impl_)
#define _Deref_post_valid_bytecap_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_post_opt_valid_bytecap_x_(size) _SAL1_1_Source_(_Deref_post_opt_valid_bytecap_x_, (size), _Deref_post1_impl_(__maybenull_impl_notref) _Deref_post1_impl_(__bytecap_x_impl(size)) _Post_valid_impl_)
#define _Deref_post_opt_valid_bytecap_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_post_count_(size) _SAL1_1_Source_(_Deref_post_count_, (size), _Deref_post1_impl_(__notnull_impl_notref) _Deref_post1_impl_(__count_impl(size)) _Post_valid_impl_)
#define _Deref_post_count_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_post_opt_count_(size) _SAL1_1_Source_(_Deref_post_opt_count_, (size), _Deref_post1_impl_(__maybenull_impl_notref) _Deref_post1_impl_(__count_impl(size)) _Post_valid_impl_)
#define _Deref_post_opt_count_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_post_bytecount_(size) _SAL1_1_Source_(_Deref_post_bytecount_, (size), _Deref_post1_impl_(__notnull_impl_notref) _Deref_post1_impl_(__bytecount_impl(size)) _Post_valid_impl_)
#define _Deref_post_bytecount_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_post_opt_bytecount_(size) _SAL1_1_Source_(_Deref_post_opt_bytecount_, (size), _Deref_post1_impl_(__maybenull_impl_notref) _Deref_post1_impl_(__bytecount_impl(size)) _Post_valid_impl_)
#define _Deref_post_opt_bytecount_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_post_count_c_(size) _SAL1_1_Source_(_Deref_post_count_c_, (size), _Deref_post1_impl_(__notnull_impl_notref) _Deref_post1_impl_(__count_c_impl(size)) _Post_valid_impl_)
#define _Deref_post_count_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_post_opt_count_c_(size) _SAL1_1_Source_(_Deref_post_opt_count_c_, (size), _Deref_post1_impl_(__maybenull_impl_notref) _Deref_post1_impl_(__count_c_impl(size)) _Post_valid_impl_)
#define _Deref_post_opt_count_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_post_bytecount_c_(size) _SAL1_1_Source_(_Deref_post_bytecount_c_, (size), _Deref_post1_impl_(__notnull_impl_notref) _Deref_post1_impl_(__bytecount_c_impl(size)) _Post_valid_impl_)
#define _Deref_post_bytecount_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_post_opt_bytecount_c_(size) _SAL1_1_Source_(_Deref_post_opt_bytecount_c_, (size), _Deref_post1_impl_(__maybenull_impl_notref) _Deref_post1_impl_(__bytecount_c_impl(size)) _Post_valid_impl_)
#define _Deref_post_opt_bytecount_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_post_count_x_(size) _SAL1_1_Source_(_Deref_post_count_x_, (size), _Deref_post1_impl_(__notnull_impl_notref) _Deref_post1_impl_(__count_x_impl(size)) _Post_valid_impl_)
#define _Deref_post_count_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_post_opt_count_x_(size) _SAL1_1_Source_(_Deref_post_opt_count_x_, (size), _Deref_post1_impl_(__maybenull_impl_notref) _Deref_post1_impl_(__count_x_impl(size)) _Post_valid_impl_)
#define _Deref_post_opt_count_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_post_bytecount_x_(size) _SAL1_1_Source_(_Deref_post_bytecount_x_, (size), _Deref_post1_impl_(__notnull_impl_notref) _Deref_post1_impl_(__bytecount_x_impl(size)) _Post_valid_impl_)
#define _Deref_post_bytecount_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_post_opt_bytecount_x_(size) _SAL1_1_Source_(_Deref_post_opt_bytecount_x_, (size), _Deref_post1_impl_(__maybenull_impl_notref) _Deref_post1_impl_(__bytecount_x_impl(size)) _Post_valid_impl_)
#define _Deref_post_opt_bytecount_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_post_valid_ _SAL1_1_Source_(_Deref_post_valid_, (), _Deref_post1_impl_(__notnull_impl_notref) _Post_valid_impl_)
#define _Deref_post_valid_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_post_opt_valid_ _SAL1_1_Source_(_Deref_post_opt_valid_, (), _Deref_post1_impl_(__maybenull_impl_notref) _Post_valid_impl_)
#define _Deref_post_opt_valid_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_post_notnull_ _SAL1_1_Source_(_Deref_post_notnull_, (), _Deref_post1_impl_(__notnull_impl_notref))
#define _Deref_post_notnull_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_post_maybenull_ _SAL1_1_Source_(_Deref_post_maybenull_, (), _Deref_post1_impl_(__maybenull_impl_notref))
#define _Deref_post_maybenull_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_post_null_ _SAL1_1_Source_(_Deref_post_null_, (), _Deref_post1_impl_(__null_impl_notref))
#define _Deref_post_null_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_ret_z_ _SAL1_1_Source_(_Deref_ret_z_, (), _Deref_ret1_impl_(__notnull_impl_notref) _Deref_ret1_impl_(__zterm_impl))
#define _Deref_ret_z_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_ret_opt_z_ _SAL1_1_Source_(_Deref_ret_opt_z_, (), _Deref_ret1_impl_(__maybenull_impl_notref) _Ret1_impl_(__zterm_impl))
#define _Deref_ret_opt_z_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref2_pre_readonly_ _SAL1_1_Source_(_Deref2_pre_readonly_, (), _Deref2_pre1_impl_(__readaccess_impl_notref))
#define _Deref2_pre_readonly_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Ret_opt_valid_ _SAL1_1_Source_(_Ret_opt_valid_, (), _Ret1_impl_(__maybenull_impl_notref) _Ret_valid_impl_)
#define _Ret_opt_valid_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Ret_opt_z_ _SAL1_1_Source_(_Ret_opt_z_, (), _Ret2_impl_(__maybenull_impl,__zterm_impl) _Ret_valid_impl_)
#define _Ret_opt_z_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Ret_cap_(size) _SAL1_1_Source_(_Ret_cap_, (size), _Ret1_impl_(__notnull_impl_notref) _Ret1_impl_(__cap_impl(size)))
#define _Ret_cap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Ret_opt_cap_(size) _SAL1_1_Source_(_Ret_opt_cap_, (size), _Ret1_impl_(__maybenull_impl_notref) _Ret1_impl_(__cap_impl(size)))
#define _Ret_opt_cap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Ret_bytecap_(size) _SAL1_1_Source_(_Ret_bytecap_, (size), _Ret1_impl_(__notnull_impl_notref) _Ret1_impl_(__bytecap_impl(size)))
#define _Ret_bytecap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Ret_opt_bytecap_(size) _SAL1_1_Source_(_Ret_opt_bytecap_, (size), _Ret1_impl_(__maybenull_impl_notref) _Ret1_impl_(__bytecap_impl(size)))
#define _Ret_opt_bytecap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Ret_cap_c_(size) _SAL1_1_Source_(_Ret_cap_c_, (size), _Ret1_impl_(__notnull_impl_notref) _Ret1_impl_(__cap_c_impl(size)))
#define _Ret_cap_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Ret_opt_cap_c_(size) _SAL1_1_Source_(_Ret_opt_cap_c_, (size), _Ret1_impl_(__maybenull_impl_notref) _Ret1_impl_(__cap_c_impl(size)))
#define _Ret_opt_cap_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Ret_bytecap_c_(size) _SAL1_1_Source_(_Ret_bytecap_c_, (size), _Ret1_impl_(__notnull_impl_notref) _Ret1_impl_(__bytecap_c_impl(size)))
#define _Ret_bytecap_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Ret_opt_bytecap_c_(size) _SAL1_1_Source_(_Ret_opt_bytecap_c_, (size), _Ret1_impl_(__maybenull_impl_notref) _Ret1_impl_(__bytecap_c_impl(size)))
#define _Ret_opt_bytecap_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Ret_cap_x_(size) _SAL1_1_Source_(_Ret_cap_x_, (size), _Ret1_impl_(__notnull_impl_notref) _Ret1_impl_(__cap_x_impl(size)))
#define _Ret_cap_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Ret_opt_cap_x_(size) _SAL1_1_Source_(_Ret_opt_cap_x_, (size), _Ret1_impl_(__maybenull_impl_notref) _Ret1_impl_(__cap_x_impl(size)))
#define _Ret_opt_cap_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Ret_bytecap_x_(size) _SAL1_1_Source_(_Ret_bytecap_x_, (size), _Ret1_impl_(__notnull_impl_notref) _Ret1_impl_(__bytecap_x_impl(size)))
#define _Ret_bytecap_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Ret_opt_bytecap_x_(size) _SAL1_1_Source_(_Ret_opt_bytecap_x_, (size), _Ret1_impl_(__maybenull_impl_notref) _Ret1_impl_(__bytecap_x_impl(size)))
#define _Ret_opt_bytecap_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Ret_z_cap_(size) _SAL1_1_Source_(_Ret_z_cap_, (size), _Ret1_impl_(__notnull_impl_notref) _Ret2_impl_(__zterm_impl,__cap_impl(size)) _Ret_valid_impl_)
#define _Ret_z_cap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Ret_opt_z_cap_(size) _SAL1_1_Source_(_Ret_opt_z_cap_, (size), _Ret1_impl_(__maybenull_impl_notref) _Ret2_impl_(__zterm_impl,__cap_impl(size)) _Ret_valid_impl_)
#define _Ret_opt_z_cap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Ret_z_bytecap_(size) _SAL1_1_Source_(_Ret_z_bytecap_, (size), _Ret1_impl_(__notnull_impl_notref) _Ret2_impl_(__zterm_impl,__bytecap_impl(size)) _Ret_valid_impl_)
#define _Ret_z_bytecap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Ret_opt_z_bytecap_(size) _SAL1_1_Source_(_Ret_opt_z_bytecap_, (size), _Ret1_impl_(__maybenull_impl_notref) _Ret2_impl_(__zterm_impl,__bytecap_impl(size)) _Ret_valid_impl_)
#define _Ret_opt_z_bytecap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Ret_count_(size) _SAL1_1_Source_(_Ret_count_, (size), _Ret1_impl_(__notnull_impl_notref) _Ret1_impl_(__count_impl(size)) _Ret_valid_impl_)
#define _Ret_count_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Ret_opt_count_(size) _SAL1_1_Source_(_Ret_opt_count_, (size), _Ret1_impl_(__maybenull_impl_notref) _Ret1_impl_(__count_impl(size)) _Ret_valid_impl_)
#define _Ret_opt_count_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Ret_bytecount_(size) _SAL1_1_Source_(_Ret_bytecount_, (size), _Ret1_impl_(__notnull_impl_notref) _Ret1_impl_(__bytecount_impl(size)) _Ret_valid_impl_)
#define _Ret_bytecount_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Ret_opt_bytecount_(size) _SAL1_1_Source_(_Ret_opt_bytecount_, (size), _Ret1_impl_(__maybenull_impl_notref) _Ret1_impl_(__bytecount_impl(size)) _Ret_valid_impl_)
#define _Ret_opt_bytecount_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Ret_count_c_(size) _SAL1_1_Source_(_Ret_count_c_, (size), _Ret1_impl_(__notnull_impl_notref) _Ret1_impl_(__count_c_impl(size)) _Ret_valid_impl_)
#define _Ret_count_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Ret_opt_count_c_(size) _SAL1_1_Source_(_Ret_opt_count_c_, (size), _Ret1_impl_(__maybenull_impl_notref) _Ret1_impl_(__count_c_impl(size)) _Ret_valid_impl_)
#define _Ret_opt_count_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Ret_bytecount_c_(size) _SAL1_1_Source_(_Ret_bytecount_c_, (size), _Ret1_impl_(__notnull_impl_notref) _Ret1_impl_(__bytecount_c_impl(size)) _Ret_valid_impl_)
#define _Ret_bytecount_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Ret_opt_bytecount_c_(size) _SAL1_1_Source_(_Ret_opt_bytecount_c_, (size), _Ret1_impl_(__maybenull_impl_notref) _Ret1_impl_(__bytecount_c_impl(size)) _Ret_valid_impl_)
#define _Ret_opt_bytecount_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Ret_count_x_(size) _SAL1_1_Source_(_Ret_count_x_, (size), _Ret1_impl_(__notnull_impl_notref) _Ret1_impl_(__count_x_impl(size)) _Ret_valid_impl_)
#define _Ret_count_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Ret_opt_count_x_(size) _SAL1_1_Source_(_Ret_opt_count_x_, (size), _Ret1_impl_(__maybenull_impl_notref) _Ret1_impl_(__count_x_impl(size)) _Ret_valid_impl_)
#define _Ret_opt_count_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Ret_bytecount_x_(size) _SAL1_1_Source_(_Ret_bytecount_x_, (size), _Ret1_impl_(__notnull_impl_notref) _Ret1_impl_(__bytecount_x_impl(size)) _Ret_valid_impl_)
#define _Ret_bytecount_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Ret_opt_bytecount_x_(size) _SAL1_1_Source_(_Ret_opt_bytecount_x_, (size), _Ret1_impl_(__maybenull_impl_notref) _Ret1_impl_(__bytecount_x_impl(size)) _Ret_valid_impl_)
#define _Ret_opt_bytecount_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Ret_z_count_(size) _SAL1_1_Source_(_Ret_z_count_, (size), _Ret1_impl_(__notnull_impl_notref) _Ret2_impl_(__zterm_impl,__count_impl(size)) _Ret_valid_impl_)
#define _Ret_z_count_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Ret_opt_z_count_(size) _SAL1_1_Source_(_Ret_opt_z_count_, (size), _Ret1_impl_(__maybenull_impl_notref) _Ret2_impl_(__zterm_impl,__count_impl(size)) _Ret_valid_impl_)
#define _Ret_opt_z_count_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Ret_z_bytecount_(size) _SAL1_1_Source_(_Ret_z_bytecount_, (size), _Ret1_impl_(__notnull_impl_notref) _Ret2_impl_(__zterm_impl,__bytecount_impl(size)) _Ret_valid_impl_)
#define _Ret_z_bytecount_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Ret_opt_z_bytecount_(size) _SAL1_1_Source_(_Ret_opt_z_bytecount_, (size), _Ret1_impl_(__maybenull_impl_notref) _Ret2_impl_(__zterm_impl,__bytecount_impl(size)) _Ret_valid_impl_)
#define _Ret_opt_z_bytecount_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_opt_z_ _SAL1_1_Source_(_Pre_opt_z_, (), _Pre1_impl_(__maybenull_impl_notref) _Pre1_impl_(__zterm_impl) _Pre_valid_impl_)
#define _Pre_opt_z_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_readonly_ _SAL1_1_Source_(_Pre_readonly_, (), _Pre1_impl_(__readaccess_impl_notref))
#define _Pre_readonly_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_writeonly_ _SAL1_1_Source_(_Pre_writeonly_, (), _Pre1_impl_(__writeaccess_impl_notref))
#define _Pre_writeonly_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_cap_(size) _SAL1_1_Source_(_Pre_cap_, (size), _Pre1_impl_(__notnull_impl_notref) _Pre1_impl_(__cap_impl(size)))
#define _Pre_cap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_opt_cap_(size) _SAL1_1_Source_(_Pre_opt_cap_, (size), _Pre1_impl_(__maybenull_impl_notref) _Pre1_impl_(__cap_impl(size)))
#define _Pre_opt_cap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_bytecap_(size) _SAL1_1_Source_(_Pre_bytecap_, (size), _Pre1_impl_(__notnull_impl_notref) _Pre1_impl_(__bytecap_impl(size)))
#define _Pre_bytecap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_opt_bytecap_(size) _SAL1_1_Source_(_Pre_opt_bytecap_, (size), _Pre1_impl_(__maybenull_impl_notref) _Pre1_impl_(__bytecap_impl(size)))
#define _Pre_opt_bytecap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_cap_c_(size) _SAL1_1_Source_(_Pre_cap_c_, (size), _Pre1_impl_(__notnull_impl_notref) _Pre1_impl_(__cap_c_impl(size)))
#define _Pre_cap_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_opt_cap_c_(size) _SAL1_1_Source_(_Pre_opt_cap_c_, (size), _Pre1_impl_(__maybenull_impl_notref) _Pre1_impl_(__cap_c_impl(size)))
#define _Pre_opt_cap_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_bytecap_c_(size) _SAL1_1_Source_(_Pre_bytecap_c_, (size), _Pre1_impl_(__notnull_impl_notref) _Pre1_impl_(__bytecap_c_impl(size)))
#define _Pre_bytecap_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_opt_bytecap_c_(size) _SAL1_1_Source_(_Pre_opt_bytecap_c_, (size), _Pre1_impl_(__maybenull_impl_notref) _Pre1_impl_(__bytecap_c_impl(size)))
#define _Pre_opt_bytecap_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_cap_c_one_ _SAL1_1_Source_(_Pre_cap_c_one_, (), _Pre1_impl_(__notnull_impl_notref) _Pre1_impl_(__cap_c_one_notref_impl))
#define _Pre_cap_c_one_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_opt_cap_c_one_ _SAL1_1_Source_(_Pre_opt_cap_c_one_, (), _Pre1_impl_(__maybenull_impl_notref) _Pre1_impl_(__cap_c_one_notref_impl))
#define _Pre_opt_cap_c_one_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_cap_m_(mult,size) _SAL1_1_Source_(_Pre_cap_m_, (mult,size), _Pre1_impl_(__notnull_impl_notref) _Pre1_impl_(__mult_impl(mult,size)))
#define _Pre_cap_m_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_opt_cap_m_(mult,size) _SAL1_1_Source_(_Pre_opt_cap_m_, (mult,size), _Pre1_impl_(__maybenull_impl_notref) _Pre1_impl_(__mult_impl(mult,size)))
#define _Pre_opt_cap_m_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_cap_for_(param) _SAL1_1_Source_(_Pre_cap_for_, (param), _Pre1_impl_(__notnull_impl_notref) _Pre1_impl_(__cap_for_impl(param)))
#define _Pre_cap_for_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_opt_cap_for_(param) _SAL1_1_Source_(_Pre_opt_cap_for_, (param), _Pre1_impl_(__maybenull_impl_notref) _Pre1_impl_(__cap_for_impl(param)))
#define _Pre_opt_cap_for_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_cap_x_(size) _SAL1_1_Source_(_Pre_cap_x_, (size), _Pre1_impl_(__notnull_impl_notref) _Pre1_impl_(__cap_x_impl(size)))
#define _Pre_cap_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_opt_cap_x_(size) _SAL1_1_Source_(_Pre_opt_cap_x_, (size), _Pre1_impl_(__maybenull_impl_notref) _Pre1_impl_(__cap_x_impl(size)))
#define _Pre_opt_cap_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_bytecap_x_(size) _SAL1_1_Source_(_Pre_bytecap_x_, (size), _Pre1_impl_(__notnull_impl_notref) _Pre1_impl_(__bytecap_x_impl(size)))
#define _Pre_bytecap_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_opt_bytecap_x_(size) _SAL1_1_Source_(_Pre_opt_bytecap_x_, (size), _Pre1_impl_(__maybenull_impl_notref) _Pre1_impl_(__bytecap_x_impl(size)))
#define _Pre_opt_bytecap_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_ptrdiff_cap_(ptr) _SAL1_1_Source_(_Pre_ptrdiff_cap_, (ptr), _Pre1_impl_(__notnull_impl_notref) _Pre1_impl_(__cap_x_impl(__ptrdiff(ptr))))
#define _Pre_ptrdiff_cap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_opt_ptrdiff_cap_(ptr) _SAL1_1_Source_(_Pre_opt_ptrdiff_cap_, (ptr), _Pre1_impl_(__maybenull_impl_notref) _Pre1_impl_(__cap_x_impl(__ptrdiff(ptr))))
#define _Pre_opt_ptrdiff_cap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_z_cap_(size) _SAL1_1_Source_(_Pre_z_cap_, (size), _Pre1_impl_(__notnull_impl_notref) _Pre2_impl_(__zterm_impl,__cap_impl(size)) _Pre_valid_impl_)
#define _Pre_z_cap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_opt_z_cap_(size) _SAL1_1_Source_(_Pre_opt_z_cap_, (size), _Pre1_impl_(__maybenull_impl_notref) _Pre2_impl_(__zterm_impl,__cap_impl(size)) _Pre_valid_impl_)
#define _Pre_opt_z_cap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_z_bytecap_(size) _SAL1_1_Source_(_Pre_z_bytecap_, (size), _Pre1_impl_(__notnull_impl_notref) _Pre2_impl_(__zterm_impl,__bytecap_impl(size)) _Pre_valid_impl_)
#define _Pre_z_bytecap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_opt_z_bytecap_(size) _SAL1_1_Source_(_Pre_opt_z_bytecap_, (size), _Pre1_impl_(__maybenull_impl_notref) _Pre2_impl_(__zterm_impl,__bytecap_impl(size)) _Pre_valid_impl_)
#define _Pre_opt_z_bytecap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_z_cap_c_(size) _SAL1_1_Source_(_Pre_z_cap_c_, (size), _Pre1_impl_(__notnull_impl_notref) _Pre2_impl_(__zterm_impl,__cap_c_impl(size)) _Pre_valid_impl_)
#define _Pre_z_cap_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_opt_z_cap_c_(size) _SAL1_1_Source_(_Pre_opt_z_cap_c_, (size), _Pre1_impl_(__maybenull_impl_notref) _Pre2_impl_(__zterm_impl,__cap_c_impl(size)) _Pre_valid_impl_)
#define _Pre_opt_z_cap_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_z_bytecap_c_(size) _SAL1_1_Source_(_Pre_z_bytecap_c_, (size), _Pre1_impl_(__notnull_impl_notref) _Pre2_impl_(__zterm_impl,__bytecap_c_impl(size)) _Pre_valid_impl_)
#define _Pre_z_bytecap_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_opt_z_bytecap_c_(size) _SAL1_1_Source_(_Pre_opt_z_bytecap_c_, (size), _Pre1_impl_(__maybenull_impl_notref) _Pre2_impl_(__zterm_impl,__bytecap_c_impl(size)) _Pre_valid_impl_)
#define _Pre_opt_z_bytecap_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_z_cap_x_(size) _SAL1_1_Source_(_Pre_z_cap_x_, (size), _Pre1_impl_(__notnull_impl_notref) _Pre2_impl_(__zterm_impl,__cap_x_impl(size)) _Pre_valid_impl_)
#define _Pre_z_cap_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_opt_z_cap_x_(size) _SAL1_1_Source_(_Pre_opt_z_cap_x_, (size), _Pre1_impl_(__maybenull_impl_notref) _Pre2_impl_(__zterm_impl,__cap_x_impl(size)) _Pre_valid_impl_)
#define _Pre_opt_z_cap_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_z_bytecap_x_(size) _SAL1_1_Source_(_Pre_z_bytecap_x_, (size), _Pre1_impl_(__notnull_impl_notref) _Pre2_impl_(__zterm_impl,__bytecap_x_impl(size)) _Pre_valid_impl_)
#define _Pre_z_bytecap_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_opt_z_bytecap_x_(size) _SAL1_1_Source_(_Pre_opt_z_bytecap_x_, (size), _Pre1_impl_(__maybenull_impl_notref) _Pre2_impl_(__zterm_impl,__bytecap_x_impl(size)) _Pre_valid_impl_)
#define _Pre_opt_z_bytecap_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_valid_cap_(size) _SAL1_1_Source_(_Pre_valid_cap_, (size), _Pre1_impl_(__notnull_impl_notref) _Pre1_impl_(__cap_impl(size)) _Pre_valid_impl_)
#define _Pre_valid_cap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_opt_valid_cap_(size) _SAL1_1_Source_(_Pre_opt_valid_cap_, (size), _Pre1_impl_(__maybenull_impl_notref) _Pre1_impl_(__cap_impl(size)) _Pre_valid_impl_)
#define _Pre_opt_valid_cap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_valid_bytecap_(size) _SAL1_1_Source_(_Pre_valid_bytecap_, (size), _Pre1_impl_(__notnull_impl_notref) _Pre1_impl_(__bytecap_impl(size)) _Pre_valid_impl_)
#define _Pre_valid_bytecap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_opt_valid_bytecap_(size) _SAL1_1_Source_(_Pre_opt_valid_bytecap_, (size), _Pre1_impl_(__maybenull_impl_notref) _Pre1_impl_(__bytecap_impl(size)) _Pre_valid_impl_)
#define _Pre_opt_valid_bytecap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_valid_cap_c_(size) _SAL1_1_Source_(_Pre_valid_cap_c_, (size), _Pre1_impl_(__notnull_impl_notref) _Pre1_impl_(__cap_c_impl(size)) _Pre_valid_impl_)
#define _Pre_valid_cap_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_opt_valid_cap_c_(size) _SAL1_1_Source_(_Pre_opt_valid_cap_c_, (size), _Pre1_impl_(__maybenull_impl_notref) _Pre1_impl_(__cap_c_impl(size)) _Pre_valid_impl_)
#define _Pre_opt_valid_cap_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_valid_bytecap_c_(size) _SAL1_1_Source_(_Pre_valid_bytecap_c_, (size), _Pre1_impl_(__notnull_impl_notref) _Pre1_impl_(__bytecap_c_impl(size)) _Pre_valid_impl_)
#define _Pre_valid_bytecap_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_opt_valid_bytecap_c_(size) _SAL1_1_Source_(_Pre_opt_valid_bytecap_c_, (size), _Pre1_impl_(__maybenull_impl_notref) _Pre1_impl_(__bytecap_c_impl(size)) _Pre_valid_impl_)
#define _Pre_opt_valid_bytecap_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_valid_cap_x_(size) _SAL1_1_Source_(_Pre_valid_cap_x_, (size), _Pre1_impl_(__notnull_impl_notref) _Pre1_impl_(__cap_x_impl(size)) _Pre_valid_impl_)
#define _Pre_valid_cap_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_opt_valid_cap_x_(size) _SAL1_1_Source_(_Pre_opt_valid_cap_x_, (size), _Pre1_impl_(__maybenull_impl_notref) _Pre1_impl_(__cap_x_impl(size)) _Pre_valid_impl_)
#define _Pre_opt_valid_cap_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_valid_bytecap_x_(size) _SAL1_1_Source_(_Pre_valid_bytecap_x_, (size), _Pre1_impl_(__notnull_impl_notref) _Pre1_impl_(__bytecap_x_impl(size)) _Pre_valid_impl_)
#define _Pre_valid_bytecap_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_opt_valid_bytecap_x_(size) _SAL1_1_Source_(_Pre_opt_valid_bytecap_x_, (size), _Pre1_impl_(__maybenull_impl_notref) _Pre1_impl_(__bytecap_x_impl(size)) _Pre_valid_impl_)
#define _Pre_opt_valid_bytecap_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_count_(size) _SAL1_1_Source_(_Pre_count_, (size), _Pre1_impl_(__notnull_impl_notref) _Pre1_impl_(__count_impl(size)) _Pre_valid_impl_)
#define _Pre_count_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_opt_count_(size) _SAL1_1_Source_(_Pre_opt_count_, (size), _Pre1_impl_(__maybenull_impl_notref) _Pre1_impl_(__count_impl(size)) _Pre_valid_impl_)
#define _Pre_opt_count_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_bytecount_(size) _SAL1_1_Source_(_Pre_bytecount_, (size), _Pre1_impl_(__notnull_impl_notref) _Pre1_impl_(__bytecount_impl(size)) _Pre_valid_impl_)
#define _Pre_bytecount_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_opt_bytecount_(size) _SAL1_1_Source_(_Pre_opt_bytecount_, (size), _Pre1_impl_(__maybenull_impl_notref) _Pre1_impl_(__bytecount_impl(size)) _Pre_valid_impl_)
#define _Pre_opt_bytecount_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_count_c_(size) _SAL1_1_Source_(_Pre_count_c_, (size), _Pre1_impl_(__notnull_impl_notref) _Pre1_impl_(__count_c_impl(size)) _Pre_valid_impl_)
#define _Pre_count_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_opt_count_c_(size) _SAL1_1_Source_(_Pre_opt_count_c_, (size), _Pre1_impl_(__maybenull_impl_notref) _Pre1_impl_(__count_c_impl(size)) _Pre_valid_impl_)
#define _Pre_opt_count_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_bytecount_c_(size) _SAL1_1_Source_(_Pre_bytecount_c_, (size), _Pre1_impl_(__notnull_impl_notref) _Pre1_impl_(__bytecount_c_impl(size)) _Pre_valid_impl_)
#define _Pre_bytecount_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_opt_bytecount_c_(size) _SAL1_1_Source_(_Pre_opt_bytecount_c_, (size), _Pre1_impl_(__maybenull_impl_notref) _Pre1_impl_(__bytecount_c_impl(size)) _Pre_valid_impl_)
#define _Pre_opt_bytecount_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_count_x_(size) _SAL1_1_Source_(_Pre_count_x_, (size), _Pre1_impl_(__notnull_impl_notref) _Pre1_impl_(__count_x_impl(size)) _Pre_valid_impl_)
#define _Pre_count_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_opt_count_x_(size) _SAL1_1_Source_(_Pre_opt_count_x_, (size), _Pre1_impl_(__maybenull_impl_notref) _Pre1_impl_(__count_x_impl(size)) _Pre_valid_impl_)
#define _Pre_opt_count_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_bytecount_x_(size) _SAL1_1_Source_(_Pre_bytecount_x_, (size), _Pre1_impl_(__notnull_impl_notref) _Pre1_impl_(__bytecount_x_impl(size)) _Pre_valid_impl_)
#define _Pre_bytecount_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_opt_bytecount_x_(size) _SAL1_1_Source_(_Pre_opt_bytecount_x_, (size), _Pre1_impl_(__maybenull_impl_notref) _Pre1_impl_(__bytecount_x_impl(size)) _Pre_valid_impl_)
#define _Pre_opt_bytecount_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_ptrdiff_count_(ptr) _SAL1_1_Source_(_Pre_ptrdiff_count_, (ptr), _Pre1_impl_(__notnull_impl_notref) _Pre1_impl_(__count_x_impl(__ptrdiff(ptr))) _Pre_valid_impl_)
#define _Pre_ptrdiff_count_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_opt_ptrdiff_count_(ptr) _SAL1_1_Source_(_Pre_opt_ptrdiff_count_, (ptr), _Pre1_impl_(__maybenull_impl_notref) _Pre1_impl_(__count_x_impl(__ptrdiff(ptr))) _Pre_valid_impl_)
#define _Pre_opt_ptrdiff_count_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Post_maybez_ _SAL_L_Source_(_Post_maybez_, (), _Post1_impl_(__maybezterm_impl))
#define _Post_maybez_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Post_cap_(size) _SAL1_1_Source_(_Post_cap_, (size), _Post1_impl_(__cap_impl(size)))
#define _Post_cap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Post_bytecap_(size) _SAL1_1_Source_(_Post_bytecap_, (size), _Post1_impl_(__bytecap_impl(size)))
#define _Post_bytecap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Post_count_(size) _SAL1_1_Source_(_Post_count_, (size), _Post1_impl_(__count_impl(size)) _Post_valid_impl_)
#define _Post_count_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Post_bytecount_(size) _SAL1_1_Source_(_Post_bytecount_, (size), _Post1_impl_(__bytecount_impl(size)) _Post_valid_impl_)
#define _Post_bytecount_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Post_count_c_(size) _SAL1_1_Source_(_Post_count_c_, (size), _Post1_impl_(__count_c_impl(size)) _Post_valid_impl_)
#define _Post_count_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Post_bytecount_c_(size) _SAL1_1_Source_(_Post_bytecount_c_, (size), _Post1_impl_(__bytecount_c_impl(size)) _Post_valid_impl_)
#define _Post_bytecount_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Post_count_x_(size) _SAL1_1_Source_(_Post_count_x_, (size), _Post1_impl_(__count_x_impl(size)) _Post_valid_impl_)
#define _Post_count_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Post_bytecount_x_(size) _SAL1_1_Source_(_Post_bytecount_x_, (size), _Post1_impl_(__bytecount_x_impl(size)) _Post_valid_impl_)
#define _Post_bytecount_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Post_z_count_(size) _SAL1_1_Source_(_Post_z_count_, (size), _Post2_impl_(__zterm_impl,__count_impl(size)) _Post_valid_impl_)
#define _Post_z_count_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Post_z_bytecount_(size) _SAL1_1_Source_(_Post_z_bytecount_, (size), _Post2_impl_(__zterm_impl,__bytecount_impl(size)) _Post_valid_impl_)
#define _Post_z_bytecount_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Post_z_count_c_(size) _SAL1_1_Source_(_Post_z_count_c_, (size), _Post2_impl_(__zterm_impl,__count_c_impl(size)) _Post_valid_impl_)
#define _Post_z_count_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Post_z_bytecount_c_(size) _SAL1_1_Source_(_Post_z_bytecount_c_, (size), _Post2_impl_(__zterm_impl,__bytecount_c_impl(size)) _Post_valid_impl_)
#define _Post_z_bytecount_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Post_z_count_x_(size) _SAL1_1_Source_(_Post_z_count_x_, (size), _Post2_impl_(__zterm_impl,__count_x_impl(size)) _Post_valid_impl_)
#define _Post_z_count_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Post_z_bytecount_x_(size) _SAL1_1_Source_(_Post_z_bytecount_x_, (size), _Post2_impl_(__zterm_impl,__bytecount_x_impl(size)) _Post_valid_impl_)
#define _Post_z_bytecount_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Prepost_opt_z_ _SAL1_1_Source_(_Prepost_opt_z_, (), _Pre_opt_z_ _Post_z_)
#define _Prepost_opt_z_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Prepost_count_(size) _SAL1_1_Source_(_Prepost_count_, (size), _Pre_count_(size) _Post_count_(size))
#define _Prepost_count_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Prepost_opt_count_(size) _SAL1_1_Source_(_Prepost_opt_count_, (size), _Pre_opt_count_(size) _Post_count_(size))
#define _Prepost_opt_count_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Prepost_bytecount_(size) _SAL1_1_Source_(_Prepost_bytecount_, (size), _Pre_bytecount_(size) _Post_bytecount_(size))
#define _Prepost_bytecount_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Prepost_opt_bytecount_(size) _SAL1_1_Source_(_Prepost_opt_bytecount_, (size), _Pre_opt_bytecount_(size) _Post_bytecount_(size))
#define _Prepost_opt_bytecount_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Prepost_count_c_(size) _SAL1_1_Source_(_Prepost_count_c_, (size), _Pre_count_c_(size) _Post_count_c_(size))
#define _Prepost_count_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Prepost_opt_count_c_(size) _SAL1_1_Source_(_Prepost_opt_count_c_, (size), _Pre_opt_count_c_(size) _Post_count_c_(size))
#define _Prepost_opt_count_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Prepost_bytecount_c_(size) _SAL1_1_Source_(_Prepost_bytecount_c_, (size), _Pre_bytecount_c_(size) _Post_bytecount_c_(size))
#define _Prepost_bytecount_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Prepost_opt_bytecount_c_(size) _SAL1_1_Source_(_Prepost_opt_bytecount_c_, (size), _Pre_opt_bytecount_c_(size) _Post_bytecount_c_(size))
#define _Prepost_opt_bytecount_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Prepost_count_x_(size) _SAL1_1_Source_(_Prepost_count_x_, (size), _Pre_count_x_(size) _Post_count_x_(size))
#define _Prepost_count_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Prepost_opt_count_x_(size) _SAL1_1_Source_(_Prepost_opt_count_x_, (size), _Pre_opt_count_x_(size) _Post_count_x_(size))
#define _Prepost_opt_count_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Prepost_bytecount_x_(size) _SAL1_1_Source_(_Prepost_bytecount_x_, (size), _Pre_bytecount_x_(size) _Post_bytecount_x_(size))
#define _Prepost_bytecount_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Prepost_opt_bytecount_x_(size) _SAL1_1_Source_(_Prepost_opt_bytecount_x_, (size), _Pre_opt_bytecount_x_(size) _Post_bytecount_x_(size))
#define _Prepost_opt_bytecount_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Prepost_valid_ _SAL1_1_Source_(_Prepost_valid_, (), _Pre_valid_ _Post_valid_)
#define _Prepost_valid_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Prepost_opt_valid_ _SAL1_1_Source_(_Prepost_opt_valid_, (), _Pre_opt_valid_ _Post_valid_)
#define _Prepost_opt_valid_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_prepost_z_ _SAL1_1_Source_(_Deref_prepost_z_, (), _Deref_pre_z_ _Deref_post_z_)
#define _Deref_prepost_z_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_prepost_opt_z_ _SAL1_1_Source_(_Deref_prepost_opt_z_, (), _Deref_pre_opt_z_ _Deref_post_opt_z_)
#define _Deref_prepost_opt_z_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_prepost_cap_(size) _SAL1_1_Source_(_Deref_prepost_cap_, (size), _Deref_pre_cap_(size) _Deref_post_cap_(size))
#define _Deref_prepost_cap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_prepost_opt_cap_(size) _SAL1_1_Source_(_Deref_prepost_opt_cap_, (size), _Deref_pre_opt_cap_(size) _Deref_post_opt_cap_(size))
#define _Deref_prepost_opt_cap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_prepost_bytecap_(size) _SAL1_1_Source_(_Deref_prepost_bytecap_, (size), _Deref_pre_bytecap_(size) _Deref_post_bytecap_(size))
#define _Deref_prepost_bytecap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_prepost_opt_bytecap_(size) _SAL1_1_Source_(_Deref_prepost_opt_bytecap_, (size), _Deref_pre_opt_bytecap_(size) _Deref_post_opt_bytecap_(size))
#define _Deref_prepost_opt_bytecap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_prepost_cap_x_(size) _SAL1_1_Source_(_Deref_prepost_cap_x_, (size), _Deref_pre_cap_x_(size) _Deref_post_cap_x_(size))
#define _Deref_prepost_cap_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_prepost_opt_cap_x_(size) _SAL1_1_Source_(_Deref_prepost_opt_cap_x_, (size), _Deref_pre_opt_cap_x_(size) _Deref_post_opt_cap_x_(size))
#define _Deref_prepost_opt_cap_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_prepost_bytecap_x_(size) _SAL1_1_Source_(_Deref_prepost_bytecap_x_, (size), _Deref_pre_bytecap_x_(size) _Deref_post_bytecap_x_(size))
#define _Deref_prepost_bytecap_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_prepost_opt_bytecap_x_(size) _SAL1_1_Source_(_Deref_prepost_opt_bytecap_x_, (size), _Deref_pre_opt_bytecap_x_(size) _Deref_post_opt_bytecap_x_(size))
#define _Deref_prepost_opt_bytecap_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_prepost_z_cap_(size) _SAL1_1_Source_(_Deref_prepost_z_cap_, (size), _Deref_pre_z_cap_(size) _Deref_post_z_cap_(size))
#define _Deref_prepost_z_cap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_prepost_opt_z_cap_(size) _SAL1_1_Source_(_Deref_prepost_opt_z_cap_, (size), _Deref_pre_opt_z_cap_(size) _Deref_post_opt_z_cap_(size))
#define _Deref_prepost_opt_z_cap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_prepost_z_bytecap_(size) _SAL1_1_Source_(_Deref_prepost_z_bytecap_, (size), _Deref_pre_z_bytecap_(size) _Deref_post_z_bytecap_(size))
#define _Deref_prepost_z_bytecap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_prepost_opt_z_bytecap_(size) _SAL1_1_Source_(_Deref_prepost_opt_z_bytecap_, (size), _Deref_pre_opt_z_bytecap_(size) _Deref_post_opt_z_bytecap_(size))
#define _Deref_prepost_opt_z_bytecap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_prepost_valid_cap_(size) _SAL1_1_Source_(_Deref_prepost_valid_cap_, (size), _Deref_pre_valid_cap_(size) _Deref_post_valid_cap_(size))
#define _Deref_prepost_valid_cap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_prepost_opt_valid_cap_(size) _SAL1_1_Source_(_Deref_prepost_opt_valid_cap_, (size), _Deref_pre_opt_valid_cap_(size) _Deref_post_opt_valid_cap_(size))
#define _Deref_prepost_opt_valid_cap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_prepost_valid_bytecap_(size) _SAL1_1_Source_(_Deref_prepost_valid_bytecap_, (size), _Deref_pre_valid_bytecap_(size) _Deref_post_valid_bytecap_(size))
#define _Deref_prepost_valid_bytecap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_prepost_opt_valid_bytecap_(size) _SAL1_1_Source_(_Deref_prepost_opt_valid_bytecap_, (size), _Deref_pre_opt_valid_bytecap_(size) _Deref_post_opt_valid_bytecap_(size))
#define _Deref_prepost_opt_valid_bytecap_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_prepost_valid_cap_x_(size) _SAL1_1_Source_(_Deref_prepost_valid_cap_x_, (size), _Deref_pre_valid_cap_x_(size) _Deref_post_valid_cap_x_(size))
#define _Deref_prepost_valid_cap_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_prepost_opt_valid_cap_x_(size) _SAL1_1_Source_(_Deref_prepost_opt_valid_cap_x_, (size), _Deref_pre_opt_valid_cap_x_(size) _Deref_post_opt_valid_cap_x_(size))
#define _Deref_prepost_opt_valid_cap_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_prepost_valid_bytecap_x_(size) _SAL1_1_Source_(_Deref_prepost_valid_bytecap_x_, (size), _Deref_pre_valid_bytecap_x_(size) _Deref_post_valid_bytecap_x_(size))
#define _Deref_prepost_valid_bytecap_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_prepost_opt_valid_bytecap_x_(size) _SAL1_1_Source_(_Deref_prepost_opt_valid_bytecap_x_, (size), _Deref_pre_opt_valid_bytecap_x_(size) _Deref_post_opt_valid_bytecap_x_(size))
#define _Deref_prepost_opt_valid_bytecap_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_prepost_count_(size) _SAL1_1_Source_(_Deref_prepost_count_, (size), _Deref_pre_count_(size) _Deref_post_count_(size))
#define _Deref_prepost_count_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_prepost_opt_count_(size) _SAL1_1_Source_(_Deref_prepost_opt_count_, (size), _Deref_pre_opt_count_(size) _Deref_post_opt_count_(size))
#define _Deref_prepost_opt_count_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_prepost_bytecount_(size) _SAL1_1_Source_(_Deref_prepost_bytecount_, (size), _Deref_pre_bytecount_(size) _Deref_post_bytecount_(size))
#define _Deref_prepost_bytecount_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_prepost_opt_bytecount_(size) _SAL1_1_Source_(_Deref_prepost_opt_bytecount_, (size), _Deref_pre_opt_bytecount_(size) _Deref_post_opt_bytecount_(size))
#define _Deref_prepost_opt_bytecount_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_prepost_count_x_(size) _SAL1_1_Source_(_Deref_prepost_count_x_, (size), _Deref_pre_count_x_(size) _Deref_post_count_x_(size))
#define _Deref_prepost_count_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_prepost_opt_count_x_(size) _SAL1_1_Source_(_Deref_prepost_opt_count_x_, (size), _Deref_pre_opt_count_x_(size) _Deref_post_opt_count_x_(size))
#define _Deref_prepost_opt_count_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_prepost_bytecount_x_(size) _SAL1_1_Source_(_Deref_prepost_bytecount_x_, (size), _Deref_pre_bytecount_x_(size) _Deref_post_bytecount_x_(size))
#define _Deref_prepost_bytecount_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_prepost_opt_bytecount_x_(size) _SAL1_1_Source_(_Deref_prepost_opt_bytecount_x_, (size), _Deref_pre_opt_bytecount_x_(size) _Deref_post_opt_bytecount_x_(size))
#define _Deref_prepost_opt_bytecount_x_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_prepost_valid_ _SAL1_1_Source_(_Deref_prepost_valid_, (), _Deref_pre_valid_ _Deref_post_valid_)
#define _Deref_prepost_valid_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_prepost_opt_valid_ _SAL1_1_Source_(_Deref_prepost_opt_valid_, (), _Deref_pre_opt_valid_ _Deref_post_opt_valid_)
#define _Deref_prepost_opt_valid_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_out_z_cap_c_(size) _SAL1_1_Source_(_Deref_out_z_cap_c_, (size), _Deref_pre_cap_c_(size) _Deref_post_z_)
#define _Deref_out_z_cap_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_inout_z_cap_c_(size) _SAL1_1_Source_(_Deref_inout_z_cap_c_, (size), _Deref_pre_z_cap_c_(size) _Deref_post_z_)
#define _Deref_inout_z_cap_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_out_z_bytecap_c_(size) _SAL1_1_Source_(_Deref_out_z_bytecap_c_, (size), _Deref_pre_bytecap_c_(size) _Deref_post_z_)
#define _Deref_out_z_bytecap_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_inout_z_bytecap_c_(size) _SAL1_1_Source_(_Deref_inout_z_bytecap_c_, (size), _Deref_pre_z_bytecap_c_(size) _Deref_post_z_)
#define _Deref_inout_z_bytecap_c_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_inout_z_ _SAL1_1_Source_(_Deref_inout_z_, (), _Deref_prepost_z_)
#define _Deref_inout_z_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Always_impl_(annos) _Group_(annos _SAL_nop_impl_) _On_failure_impl_(annos _SAL_nop_impl_)
#define _Always_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Bound_impl_ _SA_annotes0(SAL_bound)
#define _Bound_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Field_range_impl_(min,max) _Range_impl_(min,max)
#define _Field_range_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Literal_impl_ _SA_annotes1(SAL_constant, __yes)
#define _Literal_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Maybenull_impl_ _SA_annotes1(SAL_null, __maybe)
#define _Maybenull_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Maybevalid_impl_ _SA_annotes1(SAL_valid, __maybe)
#define _Maybevalid_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Must_inspect_impl_ _Post_impl_ _SA_annotes0(SAL_mustInspect)
#define _Must_inspect_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Notliteral_impl_ _SA_annotes1(SAL_constant, __no)
#define _Notliteral_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Notnull_impl_ _SA_annotes1(SAL_null, __no)
#define _Notnull_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Notvalid_impl_ _SA_annotes1(SAL_valid, __no)
#define _Notvalid_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _NullNull_terminated_impl_ _Group_(_SA_annotes1(SAL_nullTerminated, __yes) _SA_annotes1(SAL_readableTo,inexpressibleCount("NullNull terminated string")))
#define _NullNull_terminated_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Null_impl_ _SA_annotes1(SAL_null, __yes)
#define _Null_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Null_terminated_impl_ _SA_annotes1(SAL_nullTerminated, __yes)
#define _Null_terminated_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_impl_ _Pre1_impl_(__notnull_impl_notref) _Pre1_impl_(__cap_c_one_notref_impl) _Post_valid_impl_
#define _Out_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_opt_impl_ _Pre1_impl_(__maybenull_impl_notref) _Pre1_impl_(__cap_c_one_notref_impl) _Post_valid_impl_
#define _Out_opt_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Points_to_data_impl_ _At_(*_Curr_, _SA_annotes1(SAL_mayBePointer, __no))
#define _Points_to_data_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Post_satisfies_impl_(cond) _Post_impl_ _Satisfies_impl_(cond)
#define _Post_satisfies_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Post_valid_impl_ _Post1_impl_(__valid_impl)
#define _Post_valid_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_satisfies_impl_(cond) _Pre_impl_ _Satisfies_impl_(cond)
#define _Pre_satisfies_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_valid_impl_ _Pre1_impl_(__valid_impl)
#define _Pre_valid_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Range_impl_(min,max) _SA_annotes2(SAL_range, min, max)
#define _Range_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Readable_bytes_impl_(size) _SA_annotes1(SAL_readableTo, byteCount(size))
#define _Readable_bytes_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Readable_elements_impl_(size) _SA_annotes1(SAL_readableTo, elementCount(size))
#define _Readable_elements_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Ret_valid_impl_ _Ret1_impl_(__valid_impl)
#define _Ret_valid_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Satisfies_impl_(cond) _SA_annotes1(SAL_satisfies, cond)
#define _Satisfies_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Valid_impl_ _SA_annotes1(SAL_valid, __yes)
#define _Valid_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Writable_bytes_impl_(size) _SA_annotes1(SAL_writableTo, byteCount(size))
#define _Writable_bytes_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Writable_elements_impl_(size) _SA_annotes1(SAL_writableTo, elementCount(size))
#define _Writable_elements_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _In_range_impl_(min,max) _Pre_impl_ _Range_impl_(min,max)
#define _In_range_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_range_impl_(min,max) _Post_impl_ _Range_impl_(min,max)
#define _Out_range_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Ret_range_impl_(min,max) _Post_impl_ _Range_impl_(min,max)
#define _Ret_range_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_in_range_impl_(min,max) _Deref_pre_impl_ _Range_impl_(min,max)
#define _Deref_in_range_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_out_range_impl_(min,max) _Deref_post_impl_ _Range_impl_(min,max)
#define _Deref_out_range_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_ret_range_impl_(min,max) _Deref_post_impl_ _Range_impl_(min,max)
#define _Deref_ret_range_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_pre_impl_ _Pre_impl_ _Notref_impl_ _Deref_impl_
#define _Deref_pre_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_post_impl_ _Post_impl_ _Notref_impl_ _Deref_impl_
#define _Deref_post_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __AuToQuOtE _SA_annotes0(SAL_AuToQuOtE)
#define __AuToQuOtE
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deferTypecheck _SA_annotes0(SAL_deferTypecheck)
#define __deferTypecheck
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _SA_SPECSTRIZE( x ) #x
#define _SA_SPECSTRIZE
#define _SAL_nop_impl_ // nothing
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __nop_impl(x) x
#define __nop_impl
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _SA_annotes0(n) [SAL_annotes(Name=#n)]
#define _SA_annotes0
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _SA_annotes1(n,pp1) [SAL_annotes(Name=#n, p1=_SA_SPECSTRIZE(pp1))]
#define _SA_annotes1
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _SA_annotes2(n,pp1,pp2) [SAL_annotes(Name=#n, p1=_SA_SPECSTRIZE(pp1), p2=_SA_SPECSTRIZE(pp2))]
#define _SA_annotes2
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _SA_annotes3(n,pp1,pp2,pp3) [SAL_annotes(Name=#n, p1=_SA_SPECSTRIZE(pp1), p2=_SA_SPECSTRIZE(pp2), p3=_SA_SPECSTRIZE(pp3))]
#define _SA_annotes3
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_impl_ [SAL_pre]
#define _Pre_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Post_impl_ [SAL_post]
#define _Post_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_impl_ [SAL_deref]
#define _Deref_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Notref_impl_ [SAL_notref]
#define _Notref_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __ANNOTATION(fun) _SA_annotes0(SAL_annotation) void __SA_##fun;
#define __ANNOTATION
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __PRIMOP(type, fun) _SA_annotes0(SAL_primop) type __SA_##fun;
#define __PRIMOP
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __QUALIFIER(fun) _SA_annotes0(SAL_qualifier) void __SA_##fun;
#define __QUALIFIER
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __In_impl_ [SA_Pre(Valid=SA_Yes)] [SA_Pre(Deref=1, Notref=1, Access=SA_Read)] __declspec("SAL_pre SAL_valid")
#define __In_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _SA_annotes0(n) __declspec(#n)
#define _SA_annotes0
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _SA_annotes1(n,pp1) __declspec(#n "(" _SA_SPECSTRIZE(pp1) ")" )
#define _SA_annotes1
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _SA_annotes2(n,pp1,pp2) __declspec(#n "(" _SA_SPECSTRIZE(pp1) "," _SA_SPECSTRIZE(pp2) ")")
#define _SA_annotes2
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _SA_annotes3(n,pp1,pp2,pp3) __declspec(#n "(" _SA_SPECSTRIZE(pp1) "," _SA_SPECSTRIZE(pp2) "," _SA_SPECSTRIZE(pp3) ")")
#define _SA_annotes3
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_impl_ _SA_annotes0(SAL_pre)
#define _Pre_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Post_impl_ _SA_annotes0(SAL_post)
#define _Post_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_impl_ _SA_annotes0(SAL_deref)
#define _Deref_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Notref_impl_ _SA_annotes0(SAL_notref)
#define _Notref_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __ANNOTATION(fun) _SA_annotes0(SAL_annotation) void __SA_##fun
#define __ANNOTATION
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __PRIMOP(type, fun) _SA_annotes0(SAL_primop) type __SA_##fun
#define __PRIMOP
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __QUALIFIER(fun) _SA_annotes0(SAL_qualifier) void __SA_##fun;
#define __QUALIFIER
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __In_impl_ _Pre_impl_ _SA_annotes0(SAL_valid) _Pre_impl_ _Deref_impl_ _Notref_impl_ _SA_annotes0(SAL_readonly)
#define __In_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _SA_annotes0(n)
#define _SA_annotes0
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _SA_annotes1(n,pp1)
#define _SA_annotes1
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _SA_annotes2(n,pp1,pp2)
#define _SA_annotes2
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _SA_annotes3(n,pp1,pp2,pp3)
#define _SA_annotes3
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __ANNOTATION(fun)
#define __ANNOTATION
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __PRIMOP(type, fun)
#define __PRIMOP
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __QUALIFIER(type, fun)
#define __QUALIFIER
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Check_return_impl_ [SA_Post(MustCheck=SA_Yes)]
#define _Check_return_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Success_impl_(expr) [SA_Success(Condition=#expr)]
#define _Success_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _On_failure_impl_(annos) [SAL_context(p1="SAL_failed")] _Group_(_Post_impl_ _Group_(annos _SAL_nop_impl_))
#define _On_failure_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Printf_format_string_impl_ [SA_FormatString(Style="printf")]
#define _Printf_format_string_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Scanf_format_string_impl_ [SA_FormatString(Style="scanf")]
#define _Scanf_format_string_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Scanf_s_format_string_impl_ [SA_FormatString(Style="scanf_s")]
#define _Scanf_s_format_string_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _In_bound_impl_ [SA_PreBound(Deref=0)]
#define _In_bound_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_bound_impl_ [SA_PostBound(Deref=0)]
#define _Out_bound_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Ret_bound_impl_ [SA_PostBound(Deref=0)]
#define _Ret_bound_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_in_bound_impl_ [SA_PreBound(Deref=1)]
#define _Deref_in_bound_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_out_bound_impl_ [SA_PostBound(Deref=1)]
#define _Deref_out_bound_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_ret_bound_impl_ [SA_PostBound(Deref=1)]
#define _Deref_ret_bound_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __valid_impl Valid=SA_Yes
#define __valid_impl
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __maybevalid_impl Valid=SA_Maybe
#define __maybevalid_impl
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __notvalid_impl Valid=SA_No
#define __notvalid_impl
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __null_impl Null=SA_Yes
#define __null_impl
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __maybenull_impl Null=SA_Maybe
#define __maybenull_impl
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __notnull_impl Null=SA_No
#define __notnull_impl
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __null_impl_notref Null=SA_Yes,Notref=1
#define __null_impl_notref
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __maybenull_impl_notref Null=SA_Maybe,Notref=1
#define __maybenull_impl_notref
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __notnull_impl_notref Null=SA_No,Notref=1
#define __notnull_impl_notref
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __zterm_impl NullTerminated=SA_Yes
#define __zterm_impl
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __maybezterm_impl NullTerminated=SA_Maybe
#define __maybezterm_impl
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __maybzterm_impl NullTerminated=SA_Maybe
#define __maybzterm_impl
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __notzterm_impl NullTerminated=SA_No
#define __notzterm_impl
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __readaccess_impl Access=SA_Read
#define __readaccess_impl
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __writeaccess_impl Access=SA_Write
#define __writeaccess_impl
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __allaccess_impl Access=SA_ReadWrite
#define __allaccess_impl
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __readaccess_impl_notref Access=SA_Read,Notref=1
#define __readaccess_impl_notref
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __writeaccess_impl_notref Access=SA_Write,Notref=1
#define __writeaccess_impl_notref
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __allaccess_impl_notref Access=SA_ReadWrite,Notref=1
#define __allaccess_impl_notref
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __cap_impl(size) WritableElements="\n"#size
#define __cap_impl
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __bytecap_impl(size) WritableBytes="\n"#size
#define __bytecap_impl
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __bytecount_impl(size) ValidBytes="\n"#size
#define __bytecount_impl
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __count_impl(size) ValidElements="\n"#size
#define __count_impl
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __cap_impl(size) WritableElements=#size
#define __cap_impl
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __bytecap_impl(size) WritableBytes=#size
#define __bytecap_impl
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __bytecount_impl(size) ValidBytes=#size
#define __bytecount_impl
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __count_impl(size) ValidElements=#size
#define __count_impl
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __cap_c_impl(size) WritableElementsConst=size
#define __cap_c_impl
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __cap_c_one_notref_impl WritableElementsConst=1,Notref=1
#define __cap_c_one_notref_impl
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __cap_for_impl(param) WritableElementsLength=#param
#define __cap_for_impl
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __cap_x_impl(size) WritableElements="\n@"#size
#define __cap_x_impl
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __bytecap_c_impl(size) WritableBytesConst=size
#define __bytecap_c_impl
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __bytecap_x_impl(size) WritableBytes="\n@"#size
#define __bytecap_x_impl
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __mult_impl(mult,size) __cap_impl((mult)*(size))
#define __mult_impl
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __count_c_impl(size) ValidElementsConst=size
#define __count_c_impl
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __count_x_impl(size) ValidElements="\n@"#size
#define __count_x_impl
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __bytecount_c_impl(size) ValidBytesConst=size
#define __bytecount_c_impl
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __bytecount_x_impl(size) ValidBytes="\n@"#size
#define __bytecount_x_impl
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _At_impl_(target, annos) [SAL_at(p1=#target)] _Group_(annos)
#define _At_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _At_buffer_impl_(target, iter, bound, annos) [SAL_at_buffer(p1=#target, p2=#iter, p3=#bound)] _Group_(annos)
#define _At_buffer_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _When_impl_(expr, annos) [SAL_when(p1=#expr)] _Group_(annos)
#define _When_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Group_impl_(annos) [SAL_begin] annos [SAL_end]
#define _Group_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _GrouP_impl_(annos) [SAL_BEGIN] annos [SAL_END]
#define _GrouP_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Use_decl_anno_impl_ _SA_annotes0(SAL_useHeader)
#define _Use_decl_anno_impl_ // this is a special case!
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre1_impl_(p1) [SA_Pre(p1)]
#define _Pre1_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre2_impl_(p1,p2) [SA_Pre(p1,p2)]
#define _Pre2_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre3_impl_(p1,p2,p3) [SA_Pre(p1,p2,p3)]
#define _Pre3_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Post1_impl_(p1) [SA_Post(p1)]
#define _Post1_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Post2_impl_(p1,p2) [SA_Post(p1,p2)]
#define _Post2_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Post3_impl_(p1,p2,p3) [SA_Post(p1,p2,p3)]
#define _Post3_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Ret1_impl_(p1) [SA_Post(p1)]
#define _Ret1_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Ret2_impl_(p1,p2) [SA_Post(p1,p2)]
#define _Ret2_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Ret3_impl_(p1,p2,p3) [SA_Post(p1,p2,p3)]
#define _Ret3_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_pre1_impl_(p1) [SA_Pre(Deref=1,p1)]
#define _Deref_pre1_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_pre2_impl_(p1,p2) [SA_Pre(Deref=1,p1,p2)]
#define _Deref_pre2_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_pre3_impl_(p1,p2,p3) [SA_Pre(Deref=1,p1,p2,p3)]
#define _Deref_pre3_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_post1_impl_(p1) [SA_Post(Deref=1,p1)]
#define _Deref_post1_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_post2_impl_(p1,p2) [SA_Post(Deref=1,p1,p2)]
#define _Deref_post2_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_post3_impl_(p1,p2,p3) [SA_Post(Deref=1,p1,p2,p3)]
#define _Deref_post3_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_ret1_impl_(p1) [SA_Post(Deref=1,p1)]
#define _Deref_ret1_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_ret2_impl_(p1,p2) [SA_Post(Deref=1,p1,p2)]
#define _Deref_ret2_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_ret3_impl_(p1,p2,p3) [SA_Post(Deref=1,p1,p2,p3)]
#define _Deref_ret3_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref2_pre1_impl_(p1) [SA_Pre(Deref=2,Notref=1,p1)]
#define _Deref2_pre1_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref2_post1_impl_(p1) [SA_Post(Deref=2,Notref=1,p1)]
#define _Deref2_post1_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref2_ret1_impl_(p1) [SA_Post(Deref=2,Notref=1,p1)]
#define _Deref2_ret1_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __inner_typefix(ctype) [SAL_typefix(p1=_SA_SPECSTRIZE(ctype))]
#define __inner_typefix
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __inner_exceptthat [SAL_except]
#define __inner_exceptthat
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Check_return_impl_ __post _SA_annotes0(SAL_checkReturn)
#define _Check_return_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Success_impl_(expr) _SA_annotes1(SAL_success, expr)
#define _Success_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _On_failure_impl_(annos) _SA_annotes1(SAL_context, SAL_failed) _Group_(_Post_impl_ _Group_(_SAL_nop_impl_ annos))
#define _On_failure_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Printf_format_string_impl_ _SA_annotes1(SAL_IsFormatString, "printf")
#define _Printf_format_string_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Scanf_format_string_impl_ _SA_annotes1(SAL_IsFormatString, "scanf")
#define _Scanf_format_string_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Scanf_s_format_string_impl_ _SA_annotes1(SAL_IsFormatString, "scanf_s")
#define _Scanf_s_format_string_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _In_bound_impl_ _Pre_impl_ _Bound_impl_
#define _In_bound_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_bound_impl_ _Post_impl_ _Bound_impl_
#define _Out_bound_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Ret_bound_impl_ _Post_impl_ _Bound_impl_
#define _Ret_bound_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_in_bound_impl_ _Deref_pre_impl_ _Bound_impl_
#define _Deref_in_bound_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_out_bound_impl_ _Deref_post_impl_ _Bound_impl_
#define _Deref_out_bound_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_ret_bound_impl_ _Deref_post_impl_ _Bound_impl_
#define _Deref_ret_bound_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __null_impl _SA_annotes0(SAL_null)
#define __null_impl // _SA_annotes1(SAL_null, __yes)
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __notnull_impl _SA_annotes0(SAL_notnull)
#define __notnull_impl // _SA_annotes1(SAL_null, __no)
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __maybenull_impl _SA_annotes0(SAL_maybenull)
#define __maybenull_impl // _SA_annotes1(SAL_null, __maybe)
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __valid_impl _SA_annotes0(SAL_valid)
#define __valid_impl // _SA_annotes1(SAL_valid, __yes)
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __notvalid_impl _SA_annotes0(SAL_notvalid)
#define __notvalid_impl // _SA_annotes1(SAL_valid, __no)
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __maybevalid_impl _SA_annotes0(SAL_maybevalid)
#define __maybevalid_impl // _SA_annotes1(SAL_valid, __maybe)
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __null_impl_notref _Notref_ _Null_impl_
#define __null_impl_notref
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __maybenull_impl_notref _Notref_ _Maybenull_impl_
#define __maybenull_impl_notref
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __notnull_impl_notref _Notref_ _Notnull_impl_
#define __notnull_impl_notref
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __zterm_impl _SA_annotes1(SAL_nullTerminated, __yes)
#define __zterm_impl
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __maybezterm_impl _SA_annotes1(SAL_nullTerminated, __maybe)
#define __maybezterm_impl
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __maybzterm_impl _SA_annotes1(SAL_nullTerminated, __maybe)
#define __maybzterm_impl
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __notzterm_impl _SA_annotes1(SAL_nullTerminated, __no)
#define __notzterm_impl
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __readaccess_impl _SA_annotes1(SAL_access, 0x1)
#define __readaccess_impl
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __writeaccess_impl _SA_annotes1(SAL_access, 0x2)
#define __writeaccess_impl
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __allaccess_impl _SA_annotes1(SAL_access, 0x3)
#define __allaccess_impl
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __readaccess_impl_notref _Notref_ _SA_annotes1(SAL_access, 0x1)
#define __readaccess_impl_notref
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __writeaccess_impl_notref _Notref_ _SA_annotes1(SAL_access, 0x2)
#define __writeaccess_impl_notref
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __allaccess_impl_notref _Notref_ _SA_annotes1(SAL_access, 0x3)
#define __allaccess_impl_notref
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __cap_impl(size) _SA_annotes1(SAL_writableTo,elementCount(size))
#define __cap_impl
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __cap_c_impl(size) _SA_annotes1(SAL_writableTo,elementCount(size))
#define __cap_c_impl
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __cap_c_one_notref_impl _Notref_ _SA_annotes1(SAL_writableTo,elementCount(1))
#define __cap_c_one_notref_impl
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __cap_for_impl(param) _SA_annotes1(SAL_writableTo,inexpressibleCount(sizeof(param)))
#define __cap_for_impl
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __cap_x_impl(size) _SA_annotes1(SAL_writableTo,inexpressibleCount(#size))
#define __cap_x_impl
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __bytecap_impl(size) _SA_annotes1(SAL_writableTo,byteCount(size))
#define __bytecap_impl
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __bytecap_c_impl(size) _SA_annotes1(SAL_writableTo,byteCount(size))
#define __bytecap_c_impl
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __bytecap_x_impl(size) _SA_annotes1(SAL_writableTo,inexpressibleCount(#size))
#define __bytecap_x_impl
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __mult_impl(mult,size) _SA_annotes1(SAL_writableTo,(mult)*(size))
#define __mult_impl
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __count_impl(size) _SA_annotes1(SAL_readableTo,elementCount(size))
#define __count_impl
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __count_c_impl(size) _SA_annotes1(SAL_readableTo,elementCount(size))
#define __count_c_impl
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __count_x_impl(size) _SA_annotes1(SAL_readableTo,inexpressibleCount(#size))
#define __count_x_impl
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __bytecount_impl(size) _SA_annotes1(SAL_readableTo,byteCount(size))
#define __bytecount_impl
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __bytecount_c_impl(size) _SA_annotes1(SAL_readableTo,byteCount(size))
#define __bytecount_c_impl
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __bytecount_x_impl(size) _SA_annotes1(SAL_readableTo,inexpressibleCount(#size))
#define __bytecount_x_impl
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _At_impl_(target, annos) _SA_annotes0(SAL_at(target)) _Group_(annos)
#define _At_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _At_buffer_impl_(target, iter, bound, annos) _SA_annotes3(SAL_at_buffer, target, iter, bound) _Group_(annos)
#define _At_buffer_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Group_impl_(annos) _SA_annotes0(SAL_begin) annos _SA_annotes0(SAL_end)
#define _Group_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _GrouP_impl_(annos) _SA_annotes0(SAL_BEGIN) annos _SA_annotes0(SAL_END)
#define _GrouP_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _When_impl_(expr, annos) _SA_annotes0(SAL_when(expr)) _Group_(annos)
#define _When_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Use_decl_anno_impl_ __declspec("SAL_useHeader()")
#define _Use_decl_anno_impl_ // this is a special case!
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre1_impl_(p1) _Pre_impl_ p1
#define _Pre1_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre2_impl_(p1,p2) _Pre_impl_ p1 _Pre_impl_ p2
#define _Pre2_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre3_impl_(p1,p2,p3) _Pre_impl_ p1 _Pre_impl_ p2 _Pre_impl_ p3
#define _Pre3_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Post1_impl_(p1) _Post_impl_ p1
#define _Post1_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Post2_impl_(p1,p2) _Post_impl_ p1 _Post_impl_ p2
#define _Post2_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Post3_impl_(p1,p2,p3) _Post_impl_ p1 _Post_impl_ p2 _Post_impl_ p3
#define _Post3_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Ret1_impl_(p1) _Post_impl_ p1
#define _Ret1_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Ret2_impl_(p1,p2) _Post_impl_ p1 _Post_impl_ p2
#define _Ret2_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Ret3_impl_(p1,p2,p3) _Post_impl_ p1 _Post_impl_ p2 _Post_impl_ p3
#define _Ret3_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_pre1_impl_(p1) _Deref_pre_impl_ p1
#define _Deref_pre1_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_pre2_impl_(p1,p2) _Deref_pre_impl_ p1 _Deref_pre_impl_ p2
#define _Deref_pre2_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_pre3_impl_(p1,p2,p3) _Deref_pre_impl_ p1 _Deref_pre_impl_ p2 _Deref_pre_impl_ p3
#define _Deref_pre3_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_post1_impl_(p1) _Deref_post_impl_ p1
#define _Deref_post1_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_post2_impl_(p1,p2) _Deref_post_impl_ p1 _Deref_post_impl_ p2
#define _Deref_post2_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_post3_impl_(p1,p2,p3) _Deref_post_impl_ p1 _Deref_post_impl_ p2 _Deref_post_impl_ p3
#define _Deref_post3_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_ret1_impl_(p1) _Deref_post_impl_ p1
#define _Deref_ret1_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_ret2_impl_(p1,p2) _Deref_post_impl_ p1 _Deref_post_impl_ p2
#define _Deref_ret2_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_ret3_impl_(p1,p2,p3) _Deref_post_impl_ p1 _Deref_post_impl_ p2 _Deref_post_impl_ p3
#define _Deref_ret3_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref2_pre1_impl_(p1) _Deref_pre_impl_ _Notref_impl_ _Deref_impl_ p1
#define _Deref2_pre1_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref2_post1_impl_(p1) _Deref_post_impl_ _Notref_impl_ _Deref_impl_ p1
#define _Deref2_post1_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref2_ret1_impl_(p1) _Deref_post_impl_ _Notref_impl_ _Deref_impl_ p1
#define _Deref2_ret1_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __inner_typefix(ctype) _SA_annotes1(SAL_typefix, ctype)
#define __inner_typefix
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __inner_exceptthat _SA_annotes0(SAL_except)
#define __inner_exceptthat
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define SA( id ) id
#define SA
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define REPEATABLE [repeatable]
#define REPEATABLE
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define SA( id ) SA_##id
#define SA
#define REPEATABLE
#define _SAL_nop_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _At_impl_(target, annos) [__A_(__d_=0)]
#define _At_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _At_buffer_impl_(target, iter, bound, annos) [__A_(__d_=0)]
#define _At_buffer_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _When_impl_(expr, annos) annos
#define _When_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Group_impl_(annos) annos
#define _Group_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _GrouP_impl_(annos) annos
#define _GrouP_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Use_decl_anno_impl_ [__M_(__d_=0)]
#define _Use_decl_anno_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Points_to_data_impl_ [__P_impl(__d_=0)]
#define _Points_to_data_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Literal_impl_ [__P_impl(__d_=0)]
#define _Literal_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Notliteral_impl_ [__P_impl(__d_=0)]
#define _Notliteral_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_valid_impl_ [__P_impl(__d_=0)]
#define _Pre_valid_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Post_valid_impl_ [__P_impl(__d_=0)]
#define _Post_valid_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Ret_valid_impl_ [__R_impl(__d_=0)]
#define _Ret_valid_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Check_return_impl_ [__R_impl(__d_=0)]
#define _Check_return_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Must_inspect_impl_ [__R_impl(__d_=0)]
#define _Must_inspect_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Success_impl_(expr) [__M_(__d_=0)]
#define _Success_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _On_failure_impl_(expr) [__M_(__d_=0)]
#define _On_failure_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Always_impl_(expr) [__M_(__d_=0)]
#define _Always_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Printf_format_string_impl_ [__P_impl(__d_=0)]
#define _Printf_format_string_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Scanf_format_string_impl_ [__P_impl(__d_=0)]
#define _Scanf_format_string_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Scanf_s_format_string_impl_ [__P_impl(__d_=0)]
#define _Scanf_s_format_string_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Raises_SEH_exception_impl_ [__M_(__d_=0)]
#define _Raises_SEH_exception_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Maybe_raises_SEH_exception_impl_ [__M_(__d_=0)]
#define _Maybe_raises_SEH_exception_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _In_bound_impl_ [__P_impl(__d_=0)]
#define _In_bound_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_bound_impl_ [__P_impl(__d_=0)]
#define _Out_bound_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Ret_bound_impl_ [__R_impl(__d_=0)]
#define _Ret_bound_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_in_bound_impl_ [__P_impl(__d_=0)]
#define _Deref_in_bound_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_out_bound_impl_ [__P_impl(__d_=0)]
#define _Deref_out_bound_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_ret_bound_impl_ [__R_impl(__d_=0)]
#define _Deref_ret_bound_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Range_impl_(min,max) [__P_impl(__d_=0)]
#define _Range_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _In_range_impl_(min,max) [__P_impl(__d_=0)]
#define _In_range_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_range_impl_(min,max) [__P_impl(__d_=0)]
#define _Out_range_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Ret_range_impl_(min,max) [__R_impl(__d_=0)]
#define _Ret_range_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_in_range_impl_(min,max) [__P_impl(__d_=0)]
#define _Deref_in_range_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_out_range_impl_(min,max) [__P_impl(__d_=0)]
#define _Deref_out_range_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_ret_range_impl_(min,max) [__R_impl(__d_=0)]
#define _Deref_ret_range_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Field_range_impl_(min,max) [__F_(__d_=0)]
#define _Field_range_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_satisfies_impl_(cond) [__A_(__d_=0)]
#define _Pre_satisfies_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Post_satisfies_impl_(cond) [__A_(__d_=0)]
#define _Post_satisfies_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Satisfies_impl_(cond) [__A_(__d_=0)]
#define _Satisfies_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Null_impl_ [__A_(__d_=0)]
#define _Null_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Notnull_impl_ [__A_(__d_=0)]
#define _Notnull_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Maybenull_impl_ [__A_(__d_=0)]
#define _Maybenull_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Valid_impl_ [__A_(__d_=0)]
#define _Valid_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Notvalid_impl_ [__A_(__d_=0)]
#define _Notvalid_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Maybevalid_impl_ [__A_(__d_=0)]
#define _Maybevalid_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Readable_bytes_impl_(size) [__A_(__d_=0)]
#define _Readable_bytes_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Readable_elements_impl_(size) [__A_(__d_=0)]
#define _Readable_elements_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Writable_bytes_impl_(size) [__A_(__d_=0)]
#define _Writable_bytes_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Writable_elements_impl_(size) [__A_(__d_=0)]
#define _Writable_elements_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Null_terminated_impl_ [__A_(__d_=0)]
#define _Null_terminated_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _NullNull_terminated_impl_ [__A_(__d_=0)]
#define _NullNull_terminated_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_impl_ [__P_impl(__d_=0)]
#define _Pre_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre1_impl_(p1) [__P_impl(__d_=0)]
#define _Pre1_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre2_impl_(p1,p2) [__P_impl(__d_=0)]
#define _Pre2_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre3_impl_(p1,p2,p3) [__P_impl(__d_=0)]
#define _Pre3_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Post_impl_ [__P_impl(__d_=0)]
#define _Post_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Post1_impl_(p1) [__P_impl(__d_=0)]
#define _Post1_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Post2_impl_(p1,p2) [__P_impl(__d_=0)]
#define _Post2_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Post3_impl_(p1,p2,p3) [__P_impl(__d_=0)]
#define _Post3_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Ret1_impl_(p1) [__R_impl(__d_=0)]
#define _Ret1_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Ret2_impl_(p1,p2) [__R_impl(__d_=0)]
#define _Ret2_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Ret3_impl_(p1,p2,p3) [__R_impl(__d_=0)]
#define _Ret3_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_pre1_impl_(p1) [__P_impl(__d_=0)]
#define _Deref_pre1_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_pre2_impl_(p1,p2) [__P_impl(__d_=0)]
#define _Deref_pre2_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_pre3_impl_(p1,p2,p3) [__P_impl(__d_=0)]
#define _Deref_pre3_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_post1_impl_(p1) [__P_impl(__d_=0)]
#define _Deref_post1_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_post2_impl_(p1,p2) [__P_impl(__d_=0)]
#define _Deref_post2_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_post3_impl_(p1,p2,p3) [__P_impl(__d_=0)]
#define _Deref_post3_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_ret1_impl_(p1) [__R_impl(__d_=0)]
#define _Deref_ret1_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_ret2_impl_(p1,p2) [__R_impl(__d_=0)]
#define _Deref_ret2_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_ret3_impl_(p1,p2,p3) [__R_impl(__d_=0)]
#define _Deref_ret3_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref2_pre1_impl_(p1)
#define _Deref2_pre1_impl_ //[__P_impl(__d_=0)]
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref2_post1_impl_(p1)
#define _Deref2_post1_impl_ //[__P_impl(__d_=0)]
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref2_ret1_impl_(p1)
#define _Deref2_ret1_impl_ //[__P_impl(__d_=0)]
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _SAL_nop_impl_ X
#define _SAL_nop_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _At_impl_(target, annos)
#define _At_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _When_impl_(expr, annos)
#define _When_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Group_impl_(annos)
#define _Group_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _GrouP_impl_(annos)
#define _GrouP_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _At_buffer_impl_(target, iter, bound, annos)
#define _At_buffer_impl_
#define _Use_decl_anno_impl_
#define _Points_to_data_impl_
#define _Literal_impl_
#define _Notliteral_impl_
#define _Notref_impl_
#define _Pre_valid_impl_
#define _Post_valid_impl_
#define _Ret_valid_impl_
#define _Check_return_impl_
#define _Must_inspect_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Success_impl_(expr)
#define _Success_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _On_failure_impl_(annos)
#define _On_failure_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Always_impl_(annos)
#define _Always_impl_
#define _Printf_format_string_impl_
#define _Scanf_format_string_impl_
#define _Scanf_s_format_string_impl_
#define _In_bound_impl_
#define _Out_bound_impl_
#define _Ret_bound_impl_
#define _Deref_in_bound_impl_
#define _Deref_out_bound_impl_
#define _Deref_ret_bound_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Range_impl_(min,max)
#define _Range_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _In_range_impl_(min,max)
#define _In_range_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Out_range_impl_(min,max)
#define _Out_range_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Ret_range_impl_(min,max)
#define _Ret_range_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_in_range_impl_(min,max)
#define _Deref_in_range_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_out_range_impl_(min,max)
#define _Deref_out_range_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_ret_range_impl_(min,max)
#define _Deref_ret_range_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Satisfies_impl_(expr)
#define _Satisfies_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre_satisfies_impl_(expr)
#define _Pre_satisfies_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Post_satisfies_impl_(expr)
#define _Post_satisfies_impl_
#define _Null_impl_
#define _Notnull_impl_
#define _Maybenull_impl_
#define _Valid_impl_
#define _Notvalid_impl_
#define _Maybevalid_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Field_range_impl_(min,max)
#define _Field_range_impl_
#define _Pre_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre1_impl_(p1)
#define _Pre1_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre2_impl_(p1,p2)
#define _Pre2_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Pre3_impl_(p1,p2,p3)
#define _Pre3_impl_
#define _Post_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Post1_impl_(p1)
#define _Post1_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Post2_impl_(p1,p2)
#define _Post2_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Post3_impl_(p1,p2,p3)
#define _Post3_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Ret1_impl_(p1)
#define _Ret1_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Ret2_impl_(p1,p2)
#define _Ret2_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Ret3_impl_(p1,p2,p3)
#define _Ret3_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_pre1_impl_(p1)
#define _Deref_pre1_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_pre2_impl_(p1,p2)
#define _Deref_pre2_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_pre3_impl_(p1,p2,p3)
#define _Deref_pre3_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_post1_impl_(p1)
#define _Deref_post1_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_post2_impl_(p1,p2)
#define _Deref_post2_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_post3_impl_(p1,p2,p3)
#define _Deref_post3_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_ret1_impl_(p1)
#define _Deref_ret1_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_ret2_impl_(p1,p2)
#define _Deref_ret2_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref_ret3_impl_(p1,p2,p3)
#define _Deref_ret3_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref2_pre1_impl_(p1)
#define _Deref2_pre1_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref2_post1_impl_(p1)
#define _Deref2_post1_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Deref2_ret1_impl_(p1)
#define _Deref2_ret1_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Readable_bytes_impl_(size)
#define _Readable_bytes_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Readable_elements_impl_(size)
#define _Readable_elements_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Writable_bytes_impl_(size)
#define _Writable_bytes_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Writable_elements_impl_(size)
#define _Writable_elements_impl_
#define _Null_terminated_impl_
#define _NullNull_terminated_impl_
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __inner_typefix(ctype)
#define __inner_typefix
#define __inner_exceptthat
#define __specstrings
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __nothrow __declspec(nothrow)
#define __nothrow
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _SA_SPECSTRIZE( x ) #x
	#define _SA_SPECSTRIZE
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __null _Null_impl_
	#define __null
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __notnull _Notnull_impl_
	#define __notnull
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __maybenull _Maybenull_impl_
	#define __maybenull
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __readonly _Pre1_impl_(__readaccess_impl)
	#define __readonly
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __notreadonly _Pre1_impl_(__allaccess_impl)
	#define __notreadonly
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __maybereadonly _Pre1_impl_(__readaccess_impl)
	#define __maybereadonly
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __valid _Valid_impl_
	#define __valid
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __notvalid _Notvalid_impl_
	#define __notvalid
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __maybevalid _Maybevalid_impl_
	#define __maybevalid
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __readableTo(extent) _SA_annotes1(SAL_readableTo, extent)
	#define __readableTo
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __elem_readableTo(size) _SA_annotes1(SAL_readableTo, elementCount( size ))
	#define __elem_readableTo
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __byte_readableTo(size) _SA_annotes1(SAL_readableTo, byteCount(size))
	#define __byte_readableTo
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __writableTo(size) _SA_annotes1(SAL_writableTo, size)
	#define __writableTo
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __elem_writableTo(size) _SA_annotes1(SAL_writableTo, elementCount( size ))
	#define __elem_writableTo
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __byte_writableTo(size) _SA_annotes1(SAL_writableTo, byteCount( size))
	#define __byte_writableTo
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref _Deref_impl_
	#define __deref
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __pre _Pre_impl_
	#define __pre
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __post _Post_impl_
	#define __post
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __precond(expr) __pre
	#define __precond
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __postcond(expr) __post
	#define __postcond
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __exceptthat __inner_exceptthat
	#define __exceptthat
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __refparam _Notref_ __deref __notreadonly
	#define __refparam
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __inner_control_entrypoint(category) _SA_annotes2(SAL_entrypoint, controlEntry, #category)
	#define __inner_control_entrypoint
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __inner_data_entrypoint(category) _SA_annotes2(SAL_entrypoint, dataEntry, #category)
	#define __inner_data_entrypoint
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __inner_override _SA_annotes0(__override)
	#define __inner_override
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __inner_callback _SA_annotes0(__callback)
	#define __inner_callback
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __inner_blocksOn(resource) _SA_annotes1(SAL_blocksOn, resource)
	#define __inner_blocksOn
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __inner_fallthrough_dec __inline __nothrow void __FallThrough() {}
	#define __inner_fallthrough_dec
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __inner_fallthrough __FallThrough();
	#define __inner_fallthrough
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __post_except_maybenull __post __inner_exceptthat _Maybenull_impl_
	#define __post_except_maybenull
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __pre_except_maybenull __pre __inner_exceptthat _Maybenull_impl_
	#define __pre_except_maybenull
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __post_deref_except_maybenull __post __deref __inner_exceptthat _Maybenull_impl_
	#define __post_deref_except_maybenull
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __pre_deref_except_maybenull __pre __deref __inner_exceptthat _Maybenull_impl_
	#define __pre_deref_except_maybenull
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __inexpressible_readableTo(size) _Readable_elements_impl_(_Inexpressible_(size))
	#define __inexpressible_readableTo
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __inexpressible_writableTo(size) _Writable_elements_impl_(_Inexpressible_(size))
	#define __inexpressible_writableTo
	#define __null
	#define __notnull
	#define __maybenull
	#define __readonly
	#define __notreadonly
	#define __maybereadonly
	#define __valid
	#define __notvalid
	#define __maybevalid
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __readableTo(extent)
	#define __readableTo
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __elem_readableTo(size)
	#define __elem_readableTo
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __byte_readableTo(size)
	#define __byte_readableTo
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __writableTo(size)
	#define __writableTo
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __elem_writableTo(size)
	#define __elem_writableTo
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __byte_writableTo(size)
	#define __byte_writableTo
	#define __deref
	#define __pre
	#define __post
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __precond(expr)
	#define __precond
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __postcond(expr)
	#define __postcond
	#define __exceptthat
	#define __inner_override
	#define __inner_callback
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __inner_blocksOn(resource)
	#define __inner_blocksOn
	#define __inner_fallthrough_dec
	#define __inner_fallthrough
	#define __refparam
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __inner_control_entrypoint(category)
	#define __inner_control_entrypoint
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __inner_data_entrypoint(category)
	#define __inner_data_entrypoint
	#define __post_except_maybenull
	#define __pre_except_maybenull
	#define __post_deref_except_maybenull
	#define __pre_deref_except_maybenull
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __inexpressible_readableTo(size)
	#define __inexpressible_readableTo
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __inexpressible_writableTo(size)
	#define __inexpressible_writableTo
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __ecount(size) _SAL1_Source_(__ecount, (size), __notnull __elem_writableTo(size))
#define __ecount
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __bcount(size) _SAL1_Source_(__bcount, (size), __notnull __byte_writableTo(size))
#define __bcount
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __in _SAL1_Source_(__in, (), _In_)
#define __in
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __in_ecount(size) _SAL1_Source_(__in_ecount, (size), _In_reads_(size))
#define __in_ecount
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __in_bcount(size) _SAL1_Source_(__in_bcount, (size), _In_reads_bytes_(size))
#define __in_bcount
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __in_z _SAL1_Source_(__in_z, (), _In_z_)
#define __in_z
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __in_ecount_z(size) _SAL1_Source_(__in_ecount_z, (size), _In_reads_z_(size))
#define __in_ecount_z
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __in_bcount_z(size) _SAL1_Source_(__in_bcount_z, (size), __in_bcount(size) __pre __nullterminated)
#define __in_bcount_z
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __in_nz _SAL1_Source_(__in_nz, (), __in)
#define __in_nz
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __in_ecount_nz(size) _SAL1_Source_(__in_ecount_nz, (size), __in_ecount(size))
#define __in_ecount_nz
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __in_bcount_nz(size) _SAL1_Source_(__in_bcount_nz, (size), __in_bcount(size))
#define __in_bcount_nz
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __out _SAL1_Source_(__out, (), _Out_)
#define __out
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __out_ecount(size) _SAL1_Source_(__out_ecount, (size), _Out_writes_(size))
#define __out_ecount
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __out_bcount(size) _SAL1_Source_(__out_bcount, (size), _Out_writes_bytes_(size))
#define __out_bcount
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __out_ecount_part(size,length) _SAL1_Source_(__out_ecount_part, (size,length), _Out_writes_to_(size,length))
#define __out_ecount_part
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __out_bcount_part(size,length) _SAL1_Source_(__out_bcount_part, (size,length), _Out_writes_bytes_to_(size,length))
#define __out_bcount_part
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __out_ecount_full(size) _SAL1_Source_(__out_ecount_full, (size), _Out_writes_all_(size))
#define __out_ecount_full
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __out_bcount_full(size) _SAL1_Source_(__out_bcount_full, (size), _Out_writes_bytes_all_(size))
#define __out_bcount_full
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __out_z _SAL1_Source_(__out_z, (), __post __valid __refparam __post __nullterminated)
#define __out_z
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __out_z_opt _SAL1_Source_(__out_z_opt, (), __post __valid __refparam __post __nullterminated __pre_except_maybenull)
#define __out_z_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __out_ecount_z(size) _SAL1_Source_(__out_ecount_z, (size), __ecount(size) __post __valid __refparam __post __nullterminated)
#define __out_ecount_z
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __out_bcount_z(size) _SAL1_Source_(__out_bcount_z, (size), __bcount(size) __post __valid __refparam __post __nullterminated)
#define __out_bcount_z
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __out_ecount_part_z(size,length) _SAL1_Source_(__out_ecount_part_z, (size,length), __out_ecount_part(size,length) __post __nullterminated)
#define __out_ecount_part_z
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __out_bcount_part_z(size,length) _SAL1_Source_(__out_bcount_part_z, (size,length), __out_bcount_part(size,length) __post __nullterminated)
#define __out_bcount_part_z
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __out_ecount_full_z(size) _SAL1_Source_(__out_ecount_full_z, (size), __out_ecount_full(size) __post __nullterminated)
#define __out_ecount_full_z
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __out_bcount_full_z(size) _SAL1_Source_(__out_bcount_full_z, (size), __out_bcount_full(size) __post __nullterminated)
#define __out_bcount_full_z
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __out_nz _SAL1_Source_(__out_nz, (), __post __valid __refparam)
#define __out_nz
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __out_nz_opt _SAL1_Source_(__out_nz_opt, (), __post __valid __refparam __post_except_maybenull_)
#define __out_nz_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __out_ecount_nz(size) _SAL1_Source_(__out_ecount_nz, (size), __ecount(size) __post __valid __refparam)
#define __out_ecount_nz
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __out_bcount_nz(size) _SAL1_Source_(__out_bcount_nz, (size), __bcount(size) __post __valid __refparam)
#define __out_bcount_nz
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __inout _SAL1_Source_(__inout, (), _Inout_)
#define __inout
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __inout_ecount(size) _SAL1_Source_(__inout_ecount, (size), _Inout_updates_(size))
#define __inout_ecount
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __inout_bcount(size) _SAL1_Source_(__inout_bcount, (size), _Inout_updates_bytes_(size))
#define __inout_bcount
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __inout_ecount_part(size,length) _SAL1_Source_(__inout_ecount_part, (size,length), _Inout_updates_to_(size,length))
#define __inout_ecount_part
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __inout_bcount_part(size,length) _SAL1_Source_(__inout_bcount_part, (size,length), _Inout_updates_bytes_to_(size,length))
#define __inout_bcount_part
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __inout_ecount_full(size) _SAL1_Source_(__inout_ecount_full, (size), _Inout_updates_all_(size))
#define __inout_ecount_full
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __inout_bcount_full(size) _SAL1_Source_(__inout_bcount_full, (size), _Inout_updates_bytes_all_(size))
#define __inout_bcount_full
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __inout_z _SAL1_Source_(__inout_z, (), _Inout_z_)
#define __inout_z
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __inout_ecount_z(size) _SAL1_Source_(__inout_ecount_z, (size), _Inout_updates_z_(size))
#define __inout_ecount_z
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __inout_bcount_z(size) _SAL1_Source_(__inout_bcount_z, (size), __inout_bcount(size) __pre __nullterminated __post __nullterminated)
#define __inout_bcount_z
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __inout_nz _SAL1_Source_(__inout_nz, (), __inout)
#define __inout_nz
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __inout_ecount_nz(size) _SAL1_Source_(__inout_ecount_nz, (size), __inout_ecount(size))
#define __inout_ecount_nz
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __inout_bcount_nz(size) _SAL1_Source_(__inout_bcount_nz, (size), __inout_bcount(size))
#define __inout_bcount_nz
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __ecount_opt(size) _SAL1_Source_(__ecount_opt, (size), __ecount(size) __pre_except_maybenull)
#define __ecount_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __bcount_opt(size) _SAL1_Source_(__bcount_opt, (size), __bcount(size) __pre_except_maybenull)
#define __bcount_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __in_opt _SAL1_Source_(__in_opt, (), _In_opt_)
#define __in_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __in_ecount_opt(size) _SAL1_Source_(__in_ecount_opt, (size), _In_reads_opt_(size))
#define __in_ecount_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __in_bcount_opt(size) _SAL1_Source_(__in_bcount_opt, (size), _In_reads_bytes_opt_(size))
#define __in_bcount_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __in_z_opt _SAL1_Source_(__in_z_opt, (), _In_opt_z_)
#define __in_z_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __in_ecount_z_opt(size) _SAL1_Source_(__in_ecount_z_opt, (size), __in_ecount_opt(size) __pre __nullterminated)
#define __in_ecount_z_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __in_bcount_z_opt(size) _SAL1_Source_(__in_bcount_z_opt, (size), __in_bcount_opt(size) __pre __nullterminated)
#define __in_bcount_z_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __in_nz_opt _SAL1_Source_(__in_nz_opt, (), __in_opt)
#define __in_nz_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __in_ecount_nz_opt(size) _SAL1_Source_(__in_ecount_nz_opt, (size), __in_ecount_opt(size))
#define __in_ecount_nz_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __in_bcount_nz_opt(size) _SAL1_Source_(__in_bcount_nz_opt, (size), __in_bcount_opt(size))
#define __in_bcount_nz_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __out_opt _SAL1_Source_(__out_opt, (), _Out_opt_)
#define __out_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __out_ecount_opt(size) _SAL1_Source_(__out_ecount_opt, (size), _Out_writes_opt_(size))
#define __out_ecount_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __out_bcount_opt(size) _SAL1_Source_(__out_bcount_opt, (size), _Out_writes_bytes_opt_(size))
#define __out_bcount_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __out_ecount_part_opt(size,length) _SAL1_Source_(__out_ecount_part_opt, (size,length), __out_ecount_part(size,length) __pre_except_maybenull)
#define __out_ecount_part_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __out_bcount_part_opt(size,length) _SAL1_Source_(__out_bcount_part_opt, (size,length), __out_bcount_part(size,length) __pre_except_maybenull)
#define __out_bcount_part_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __out_ecount_full_opt(size) _SAL1_Source_(__out_ecount_full_opt, (size), __out_ecount_full(size) __pre_except_maybenull)
#define __out_ecount_full_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __out_bcount_full_opt(size) _SAL1_Source_(__out_bcount_full_opt, (size), __out_bcount_full(size) __pre_except_maybenull)
#define __out_bcount_full_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __out_ecount_z_opt(size) _SAL1_Source_(__out_ecount_z_opt, (size), __out_ecount_opt(size) __post __nullterminated)
#define __out_ecount_z_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __out_bcount_z_opt(size) _SAL1_Source_(__out_bcount_z_opt, (size), __out_bcount_opt(size) __post __nullterminated)
#define __out_bcount_z_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __out_ecount_part_z_opt(size,length) _SAL1_Source_(__out_ecount_part_z_opt, (size,length), __out_ecount_part_opt(size,length) __post __nullterminated)
#define __out_ecount_part_z_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __out_bcount_part_z_opt(size,length) _SAL1_Source_(__out_bcount_part_z_opt, (size,length), __out_bcount_part_opt(size,length) __post __nullterminated)
#define __out_bcount_part_z_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __out_ecount_full_z_opt(size) _SAL1_Source_(__out_ecount_full_z_opt, (size), __out_ecount_full_opt(size) __post __nullterminated)
#define __out_ecount_full_z_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __out_bcount_full_z_opt(size) _SAL1_Source_(__out_bcount_full_z_opt, (size), __out_bcount_full_opt(size) __post __nullterminated)
#define __out_bcount_full_z_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __out_ecount_nz_opt(size) _SAL1_Source_(__out_ecount_nz_opt, (size), __out_ecount_opt(size) __post __nullterminated)
#define __out_ecount_nz_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __out_bcount_nz_opt(size) _SAL1_Source_(__out_bcount_nz_opt, (size), __out_bcount_opt(size) __post __nullterminated)
#define __out_bcount_nz_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __inout_opt _SAL1_Source_(__inout_opt, (), _Inout_opt_)
#define __inout_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __inout_ecount_opt(size) _SAL1_Source_(__inout_ecount_opt, (size), __inout_ecount(size) __pre_except_maybenull)
#define __inout_ecount_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __inout_bcount_opt(size) _SAL1_Source_(__inout_bcount_opt, (size), __inout_bcount(size) __pre_except_maybenull)
#define __inout_bcount_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __inout_ecount_part_opt(size,length) _SAL1_Source_(__inout_ecount_part_opt, (size,length), __inout_ecount_part(size,length) __pre_except_maybenull)
#define __inout_ecount_part_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __inout_bcount_part_opt(size,length) _SAL1_Source_(__inout_bcount_part_opt, (size,length), __inout_bcount_part(size,length) __pre_except_maybenull)
#define __inout_bcount_part_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __inout_ecount_full_opt(size) _SAL1_Source_(__inout_ecount_full_opt, (size), __inout_ecount_full(size) __pre_except_maybenull)
#define __inout_ecount_full_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __inout_bcount_full_opt(size) _SAL1_Source_(__inout_bcount_full_opt, (size), __inout_bcount_full(size) __pre_except_maybenull)
#define __inout_bcount_full_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __inout_z_opt _SAL1_Source_(__inout_z_opt, (), __inout_opt __pre __nullterminated __post __nullterminated)
#define __inout_z_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __inout_ecount_z_opt(size) _SAL1_Source_(__inout_ecount_z_opt, (size), __inout_ecount_opt(size) __pre __nullterminated __post __nullterminated)
#define __inout_ecount_z_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __inout_ecount_z_opt(size) _SAL1_Source_(__inout_ecount_z_opt, (size), __inout_ecount_opt(size) __pre __nullterminated __post __nullterminated)
#define __inout_ecount_z_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __inout_bcount_z_opt(size) _SAL1_Source_(__inout_bcount_z_opt, (size), __inout_bcount_opt(size))
#define __inout_bcount_z_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __inout_nz_opt _SAL1_Source_(__inout_nz_opt, (), __inout_opt)
#define __inout_nz_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __inout_ecount_nz_opt(size) _SAL1_Source_(__inout_ecount_nz_opt, (size), __inout_ecount_opt(size))
#define __inout_ecount_nz_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __inout_bcount_nz_opt(size) _SAL1_Source_(__inout_bcount_nz_opt, (size), __inout_bcount_opt(size))
#define __inout_bcount_nz_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_ecount(size) _SAL1_Source_(__deref_ecount, (size), _Notref_ __ecount(1) __post _Notref_ __elem_readableTo(1) __post _Notref_ __deref _Notref_ __notnull __post __deref __elem_writableTo(size))
#define __deref_ecount
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_bcount(size) _SAL1_Source_(__deref_bcount, (size), _Notref_ __ecount(1) __post _Notref_ __elem_readableTo(1) __post _Notref_ __deref _Notref_ __notnull __post __deref __byte_writableTo(size))
#define __deref_bcount
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_out _SAL1_Source_(__deref_out, (), _Outptr_)
#define __deref_out
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_out_ecount(size) _SAL1_Source_(__deref_out_ecount, (size), _Outptr_result_buffer_(size))
#define __deref_out_ecount
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_out_bcount(size) _SAL1_Source_(__deref_out_bcount, (size), _Outptr_result_bytebuffer_(size))
#define __deref_out_bcount
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_out_ecount_part(size,length) _SAL1_Source_(__deref_out_ecount_part, (size,length), _Outptr_result_buffer_to_(size,length))
#define __deref_out_ecount_part
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_out_bcount_part(size,length) _SAL1_Source_(__deref_out_bcount_part, (size,length), _Outptr_result_bytebuffer_to_(size,length))
#define __deref_out_bcount_part
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_out_ecount_full(size) _SAL1_Source_(__deref_out_ecount_full, (size), __deref_out_ecount_part(size,size))
#define __deref_out_ecount_full
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_out_bcount_full(size) _SAL1_Source_(__deref_out_bcount_full, (size), __deref_out_bcount_part(size,size))
#define __deref_out_bcount_full
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_out_z _SAL1_Source_(__deref_out_z, (), _Outptr_result_z_)
#define __deref_out_z
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_out_ecount_z(size) _SAL1_Source_(__deref_out_ecount_z, (size), __deref_out_ecount(size) __post __deref __nullterminated)
#define __deref_out_ecount_z
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_out_bcount_z(size) _SAL1_Source_(__deref_out_bcount_z, (size), __deref_out_bcount(size) __post __deref __nullterminated)
#define __deref_out_bcount_z
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_out_nz _SAL1_Source_(__deref_out_nz, (), __deref_out)
#define __deref_out_nz
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_out_ecount_nz(size) _SAL1_Source_(__deref_out_ecount_nz, (size), __deref_out_ecount(size))
#define __deref_out_ecount_nz
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_out_bcount_nz(size) _SAL1_Source_(__deref_out_bcount_nz, (size), __deref_out_ecount(size))
#define __deref_out_bcount_nz
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_inout _SAL1_Source_(__deref_inout, (), _Notref_ __notnull _Notref_ __elem_readableTo(1) __pre __deref __valid __post _Notref_ __deref __valid __refparam)
#define __deref_inout
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_inout_z _SAL1_Source_(__deref_inout_z, (), __deref_inout __pre __deref __nullterminated __post _Notref_ __deref __nullterminated)
#define __deref_inout_z
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_inout_ecount(size) _SAL1_Source_(__deref_inout_ecount, (size), __deref_inout __pre __deref __elem_writableTo(size) __post _Notref_ __deref __elem_writableTo(size))
#define __deref_inout_ecount
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_inout_bcount(size) _SAL1_Source_(__deref_inout_bcount, (size), __deref_inout __pre __deref __byte_writableTo(size) __post _Notref_ __deref __byte_writableTo(size))
#define __deref_inout_bcount
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_inout_ecount_part(size,length) _SAL1_Source_(__deref_inout_ecount_part, (size,length), __deref_inout_ecount(size) __pre __deref __elem_readableTo(length) __post __deref __elem_readableTo(length))
#define __deref_inout_ecount_part
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_inout_bcount_part(size,length) _SAL1_Source_(__deref_inout_bcount_part, (size,length), __deref_inout_bcount(size) __pre __deref __byte_readableTo(length) __post __deref __byte_readableTo(length))
#define __deref_inout_bcount_part
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_inout_ecount_full(size) _SAL1_Source_(__deref_inout_ecount_full, (size), __deref_inout_ecount_part(size,size))
#define __deref_inout_ecount_full
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_inout_bcount_full(size) _SAL1_Source_(__deref_inout_bcount_full, (size), __deref_inout_bcount_part(size,size))
#define __deref_inout_bcount_full
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_inout_ecount_z(size) _SAL1_Source_(__deref_inout_ecount_z, (size), __deref_inout_ecount(size) __pre __deref __nullterminated __post __deref __nullterminated)
#define __deref_inout_ecount_z
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_inout_bcount_z(size) _SAL1_Source_(__deref_inout_bcount_z, (size), __deref_inout_bcount(size) __pre __deref __nullterminated __post __deref __nullterminated)
#define __deref_inout_bcount_z
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_inout_nz _SAL1_Source_(__deref_inout_nz, (), __deref_inout)
#define __deref_inout_nz
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_inout_ecount_nz(size) _SAL1_Source_(__deref_inout_ecount_nz, (size), __deref_inout_ecount(size))
#define __deref_inout_ecount_nz
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_inout_bcount_nz(size) _SAL1_Source_(__deref_inout_bcount_nz, (size), __deref_inout_ecount(size))
#define __deref_inout_bcount_nz
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_ecount_opt(size) _SAL1_Source_(__deref_ecount_opt, (size), __deref_ecount(size) __post_deref_except_maybenull)
#define __deref_ecount_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_bcount_opt(size) _SAL1_Source_(__deref_bcount_opt, (size), __deref_bcount(size) __post_deref_except_maybenull)
#define __deref_bcount_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_out_opt _SAL1_Source_(__deref_out_opt, (), __deref_out __post_deref_except_maybenull)
#define __deref_out_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_out_ecount_opt(size) _SAL1_Source_(__deref_out_ecount_opt, (size), __deref_out_ecount(size) __post_deref_except_maybenull)
#define __deref_out_ecount_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_out_bcount_opt(size) _SAL1_Source_(__deref_out_bcount_opt, (size), __deref_out_bcount(size) __post_deref_except_maybenull)
#define __deref_out_bcount_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_out_ecount_part_opt(size,length) _SAL1_Source_(__deref_out_ecount_part_opt, (size,length), __deref_out_ecount_part(size,length) __post_deref_except_maybenull)
#define __deref_out_ecount_part_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_out_bcount_part_opt(size,length) _SAL1_Source_(__deref_out_bcount_part_opt, (size,length), __deref_out_bcount_part(size,length) __post_deref_except_maybenull)
#define __deref_out_bcount_part_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_out_ecount_full_opt(size) _SAL1_Source_(__deref_out_ecount_full_opt, (size), __deref_out_ecount_full(size) __post_deref_except_maybenull)
#define __deref_out_ecount_full_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_out_bcount_full_opt(size) _SAL1_Source_(__deref_out_bcount_full_opt, (size), __deref_out_bcount_full(size) __post_deref_except_maybenull)
#define __deref_out_bcount_full_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_out_z_opt _SAL1_Source_(__deref_out_z_opt, (), _Outptr_result_maybenull_z_)
#define __deref_out_z_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_out_ecount_z_opt(size) _SAL1_Source_(__deref_out_ecount_z_opt, (size), __deref_out_ecount_opt(size) __post __deref __nullterminated)
#define __deref_out_ecount_z_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_out_bcount_z_opt(size) _SAL1_Source_(__deref_out_bcount_z_opt, (size), __deref_out_bcount_opt(size) __post __deref __nullterminated)
#define __deref_out_bcount_z_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_out_nz_opt _SAL1_Source_(__deref_out_nz_opt, (), __deref_out_opt)
#define __deref_out_nz_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_out_ecount_nz_opt(size) _SAL1_Source_(__deref_out_ecount_nz_opt, (size), __deref_out_ecount_opt(size))
#define __deref_out_ecount_nz_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_out_bcount_nz_opt(size) _SAL1_Source_(__deref_out_bcount_nz_opt, (size), __deref_out_bcount_opt(size))
#define __deref_out_bcount_nz_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_inout_opt _SAL1_Source_(__deref_inout_opt, (), __deref_inout __pre_deref_except_maybenull __post_deref_except_maybenull)
#define __deref_inout_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_inout_ecount_opt(size) _SAL1_Source_(__deref_inout_ecount_opt, (size), __deref_inout_ecount(size) __pre_deref_except_maybenull __post_deref_except_maybenull)
#define __deref_inout_ecount_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_inout_bcount_opt(size) _SAL1_Source_(__deref_inout_bcount_opt, (size), __deref_inout_bcount(size) __pre_deref_except_maybenull __post_deref_except_maybenull)
#define __deref_inout_bcount_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_inout_ecount_part_opt(size,length) _SAL1_Source_(__deref_inout_ecount_part_opt, (size,length), __deref_inout_ecount_part(size,length) __pre_deref_except_maybenull __post_deref_except_maybenull)
#define __deref_inout_ecount_part_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_inout_bcount_part_opt(size,length) _SAL1_Source_(__deref_inout_bcount_part_opt, (size,length), __deref_inout_bcount_part(size,length) __pre_deref_except_maybenull __post_deref_except_maybenull)
#define __deref_inout_bcount_part_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_inout_ecount_full_opt(size) _SAL1_Source_(__deref_inout_ecount_full_opt, (size), __deref_inout_ecount_full(size) __pre_deref_except_maybenull __post_deref_except_maybenull)
#define __deref_inout_ecount_full_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_inout_bcount_full_opt(size) _SAL1_Source_(__deref_inout_bcount_full_opt, (size), __deref_inout_bcount_full(size) __pre_deref_except_maybenull __post_deref_except_maybenull)
#define __deref_inout_bcount_full_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_inout_z_opt _SAL1_Source_(__deref_inout_z_opt, (), __deref_inout_opt __pre __deref __nullterminated __post __deref __nullterminated)
#define __deref_inout_z_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_inout_ecount_z_opt(size) _SAL1_Source_(__deref_inout_ecount_z_opt, (size), __deref_inout_ecount_opt(size) __pre __deref __nullterminated __post __deref __nullterminated)
#define __deref_inout_ecount_z_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_inout_bcount_z_opt(size) _SAL1_Source_(__deref_inout_bcount_z_opt, (size), __deref_inout_bcount_opt(size) __pre __deref __nullterminated __post __deref __nullterminated)
#define __deref_inout_bcount_z_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_inout_nz_opt _SAL1_Source_(__deref_inout_nz_opt, (), __deref_inout_opt)
#define __deref_inout_nz_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_inout_ecount_nz_opt(size) _SAL1_Source_(__deref_inout_ecount_nz_opt, (size), __deref_inout_ecount_opt(size))
#define __deref_inout_ecount_nz_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_inout_bcount_nz_opt(size) _SAL1_Source_(__deref_inout_bcount_nz_opt, (size), __deref_inout_bcount_opt(size))
#define __deref_inout_bcount_nz_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_opt_ecount(size) _SAL1_Source_(__deref_opt_ecount, (size), __deref_ecount(size) __pre_except_maybenull)
#define __deref_opt_ecount
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_opt_bcount(size) _SAL1_Source_(__deref_opt_bcount, (size), __deref_bcount(size) __pre_except_maybenull)
#define __deref_opt_bcount
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_opt_out _SAL1_Source_(__deref_opt_out, (), _Outptr_opt_)
#define __deref_opt_out
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_opt_out_z _SAL1_Source_(__deref_opt_out_z, (), _Outptr_opt_result_z_)
#define __deref_opt_out_z
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_opt_out_ecount(size) _SAL1_Source_(__deref_opt_out_ecount, (size), __deref_out_ecount(size) __pre_except_maybenull)
#define __deref_opt_out_ecount
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_opt_out_bcount(size) _SAL1_Source_(__deref_opt_out_bcount, (size), __deref_out_bcount(size) __pre_except_maybenull)
#define __deref_opt_out_bcount
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_opt_out_ecount_part(size,length) _SAL1_Source_(__deref_opt_out_ecount_part, (size,length), __deref_out_ecount_part(size,length) __pre_except_maybenull)
#define __deref_opt_out_ecount_part
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_opt_out_bcount_part(size,length) _SAL1_Source_(__deref_opt_out_bcount_part, (size,length), __deref_out_bcount_part(size,length) __pre_except_maybenull)
#define __deref_opt_out_bcount_part
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_opt_out_ecount_full(size) _SAL1_Source_(__deref_opt_out_ecount_full, (size), __deref_out_ecount_full(size) __pre_except_maybenull)
#define __deref_opt_out_ecount_full
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_opt_out_bcount_full(size) _SAL1_Source_(__deref_opt_out_bcount_full, (size), __deref_out_bcount_full(size) __pre_except_maybenull)
#define __deref_opt_out_bcount_full
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_opt_inout _SAL1_Source_(__deref_opt_inout, (), _Inout_opt_)
#define __deref_opt_inout
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_opt_inout_ecount(size) _SAL1_Source_(__deref_opt_inout_ecount, (size), __deref_inout_ecount(size) __pre_except_maybenull)
#define __deref_opt_inout_ecount
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_opt_inout_bcount(size) _SAL1_Source_(__deref_opt_inout_bcount, (size), __deref_inout_bcount(size) __pre_except_maybenull)
#define __deref_opt_inout_bcount
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_opt_inout_ecount_part(size,length) _SAL1_Source_(__deref_opt_inout_ecount_part, (size,length), __deref_inout_ecount_part(size,length) __pre_except_maybenull)
#define __deref_opt_inout_ecount_part
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_opt_inout_bcount_part(size,length) _SAL1_Source_(__deref_opt_inout_bcount_part, (size,length), __deref_inout_bcount_part(size,length) __pre_except_maybenull)
#define __deref_opt_inout_bcount_part
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_opt_inout_ecount_full(size) _SAL1_Source_(__deref_opt_inout_ecount_full, (size), __deref_inout_ecount_full(size) __pre_except_maybenull)
#define __deref_opt_inout_ecount_full
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_opt_inout_bcount_full(size) _SAL1_Source_(__deref_opt_inout_bcount_full, (size), __deref_inout_bcount_full(size) __pre_except_maybenull)
#define __deref_opt_inout_bcount_full
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_opt_inout_z _SAL1_Source_(__deref_opt_inout_z, (), __deref_opt_inout __pre __deref __nullterminated __post __deref __nullterminated)
#define __deref_opt_inout_z
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_opt_inout_ecount_z(size) _SAL1_Source_(__deref_opt_inout_ecount_z, (size), __deref_opt_inout_ecount(size) __pre __deref __nullterminated __post __deref __nullterminated)
#define __deref_opt_inout_ecount_z
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_opt_inout_bcount_z(size) _SAL1_Source_(__deref_opt_inout_bcount_z, (size), __deref_opt_inout_bcount(size) __pre __deref __nullterminated __post __deref __nullterminated)
#define __deref_opt_inout_bcount_z
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_opt_inout_nz _SAL1_Source_(__deref_opt_inout_nz, (), __deref_opt_inout)
#define __deref_opt_inout_nz
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_opt_inout_ecount_nz(size) _SAL1_Source_(__deref_opt_inout_ecount_nz, (size), __deref_opt_inout_ecount(size))
#define __deref_opt_inout_ecount_nz
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_opt_inout_bcount_nz(size) _SAL1_Source_(__deref_opt_inout_bcount_nz, (size), __deref_opt_inout_bcount(size))
#define __deref_opt_inout_bcount_nz
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_opt_ecount_opt(size) _SAL1_Source_(__deref_opt_ecount_opt, (size), __deref_ecount_opt(size) __pre_except_maybenull)
#define __deref_opt_ecount_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_opt_bcount_opt(size) _SAL1_Source_(__deref_opt_bcount_opt, (size), __deref_bcount_opt(size) __pre_except_maybenull)
#define __deref_opt_bcount_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_opt_out_opt _SAL1_Source_(__deref_opt_out_opt, (), _Outptr_opt_result_maybenull_)
#define __deref_opt_out_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_opt_out_ecount_opt(size) _SAL1_Source_(__deref_opt_out_ecount_opt, (size), __deref_out_ecount_opt(size) __pre_except_maybenull)
#define __deref_opt_out_ecount_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_opt_out_bcount_opt(size) _SAL1_Source_(__deref_opt_out_bcount_opt, (size), __deref_out_bcount_opt(size) __pre_except_maybenull)
#define __deref_opt_out_bcount_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_opt_out_ecount_part_opt(size,length) _SAL1_Source_(__deref_opt_out_ecount_part_opt, (size,length), __deref_out_ecount_part_opt(size,length) __pre_except_maybenull)
#define __deref_opt_out_ecount_part_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_opt_out_bcount_part_opt(size,length) _SAL1_Source_(__deref_opt_out_bcount_part_opt, (size,length), __deref_out_bcount_part_opt(size,length) __pre_except_maybenull)
#define __deref_opt_out_bcount_part_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_opt_out_ecount_full_opt(size) _SAL1_Source_(__deref_opt_out_ecount_full_opt, (size), __deref_out_ecount_full_opt(size) __pre_except_maybenull)
#define __deref_opt_out_ecount_full_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_opt_out_bcount_full_opt(size) _SAL1_Source_(__deref_opt_out_bcount_full_opt, (size), __deref_out_bcount_full_opt(size) __pre_except_maybenull)
#define __deref_opt_out_bcount_full_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_opt_out_z_opt _SAL1_Source_(__deref_opt_out_z_opt, (), __post __deref __valid __refparam __pre_except_maybenull __pre_deref_except_maybenull __post_deref_except_maybenull __post __deref __nullterminated)
#define __deref_opt_out_z_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_opt_out_ecount_z_opt(size) _SAL1_Source_(__deref_opt_out_ecount_z_opt, (size), __deref_opt_out_ecount_opt(size) __post __deref __nullterminated)
#define __deref_opt_out_ecount_z_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_opt_out_bcount_z_opt(size) _SAL1_Source_(__deref_opt_out_bcount_z_opt, (size), __deref_opt_out_bcount_opt(size) __post __deref __nullterminated)
#define __deref_opt_out_bcount_z_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_opt_out_nz_opt _SAL1_Source_(__deref_opt_out_nz_opt, (), __deref_opt_out_opt)
#define __deref_opt_out_nz_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_opt_out_ecount_nz_opt(size) _SAL1_Source_(__deref_opt_out_ecount_nz_opt, (size), __deref_opt_out_ecount_opt(size))
#define __deref_opt_out_ecount_nz_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_opt_out_bcount_nz_opt(size) _SAL1_Source_(__deref_opt_out_bcount_nz_opt, (size), __deref_opt_out_bcount_opt(size))
#define __deref_opt_out_bcount_nz_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_opt_inout_opt _SAL1_Source_(__deref_opt_inout_opt, (), __deref_inout_opt __pre_except_maybenull)
#define __deref_opt_inout_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_opt_inout_ecount_opt(size) _SAL1_Source_(__deref_opt_inout_ecount_opt, (size), __deref_inout_ecount_opt(size) __pre_except_maybenull)
#define __deref_opt_inout_ecount_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_opt_inout_bcount_opt(size) _SAL1_Source_(__deref_opt_inout_bcount_opt, (size), __deref_inout_bcount_opt(size) __pre_except_maybenull)
#define __deref_opt_inout_bcount_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_opt_inout_ecount_part_opt(size,length) _SAL1_Source_(__deref_opt_inout_ecount_part_opt, (size,length), __deref_inout_ecount_part_opt(size,length) __pre_except_maybenull)
#define __deref_opt_inout_ecount_part_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_opt_inout_bcount_part_opt(size,length) _SAL1_Source_(__deref_opt_inout_bcount_part_opt, (size,length), __deref_inout_bcount_part_opt(size,length) __pre_except_maybenull)
#define __deref_opt_inout_bcount_part_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_opt_inout_ecount_full_opt(size) _SAL1_Source_(__deref_opt_inout_ecount_full_opt, (size), __deref_inout_ecount_full_opt(size) __pre_except_maybenull)
#define __deref_opt_inout_ecount_full_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_opt_inout_bcount_full_opt(size) _SAL1_Source_(__deref_opt_inout_bcount_full_opt, (size), __deref_inout_bcount_full_opt(size) __pre_except_maybenull)
#define __deref_opt_inout_bcount_full_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_opt_inout_z_opt _SAL1_Source_(__deref_opt_inout_z_opt, (), __deref_opt_inout_opt __pre __deref __nullterminated __post __deref __nullterminated)
#define __deref_opt_inout_z_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_opt_inout_ecount_z_opt(size) _SAL1_Source_(__deref_opt_inout_ecount_z_opt, (size), __deref_opt_inout_ecount_opt(size) __pre __deref __nullterminated __post __deref __nullterminated)
#define __deref_opt_inout_ecount_z_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_opt_inout_bcount_z_opt(size) _SAL1_Source_(__deref_opt_inout_bcount_z_opt, (size), __deref_opt_inout_bcount_opt(size) __pre __deref __nullterminated __post __deref __nullterminated)
#define __deref_opt_inout_bcount_z_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_opt_inout_nz_opt _SAL1_Source_(__deref_opt_inout_nz_opt, (), __deref_opt_inout_opt)
#define __deref_opt_inout_nz_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_opt_inout_ecount_nz_opt(size) _SAL1_Source_(__deref_opt_inout_ecount_nz_opt, (size), __deref_opt_inout_ecount_opt(size))
#define __deref_opt_inout_ecount_nz_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __deref_opt_inout_bcount_nz_opt(size) _SAL1_Source_(__deref_opt_inout_bcount_nz_opt, (size), __deref_opt_inout_bcount_opt(size))
#define __deref_opt_inout_bcount_nz_opt
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __success(expr) _SAL1_1_Source_(__success, (expr), _Success_(expr))
#define __success
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __nullterminated _SAL1_Source_(__nullterminated, (), _Null_terminated_)
#define __nullterminated
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __nullnullterminated _SAL1_Source_(__nullnulltermiated, (), _SAL_nop_impl_)
#define __nullnullterminated
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __reserved _SAL1_Source_(__reserved, (), _Reserved_)
#define __reserved
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __checkReturn _SAL1_Source_(__checkReturn, (), _Check_return_)
#define __checkReturn
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __typefix(ctype) _SAL1_Source_(__typefix, (ctype), __inner_typefix(ctype))
#define __typefix
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __override __inner_override
#define __override
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __callback __inner_callback
#define __callback
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __format_string _SAL1_1_Source_(__format_string, (), _Printf_format_string_)
#define __format_string
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __blocksOn(resource) _SAL_L_Source_(__blocksOn, (resource), __inner_blocksOn(resource))
#define __blocksOn
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __control_entrypoint(category) _SAL_L_Source_(__control_entrypoint, (category), __inner_control_entrypoint(category))
#define __control_entrypoint
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __data_entrypoint(category) _SAL_L_Source_(__data_entrypoint, (category), __inner_data_entrypoint(category))
#define __data_entrypoint
#define __useHeader
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __useHeader _Use_decl_anno_impl_
#define __useHeader
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __on_failure(annotes)
#define __on_failure
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __on_failure(annotes) _SAL1_1_Source_(__on_failure, (annotes), _On_failure_impl_(annotes _SAL_nop_impl_))
#define __on_failure
//# Laniatus Games Studio Inc. | WARN: Statement interrupted by a preprocessor statement:
//The original statement from the file sal.h starts with:
//    __inner_fallthrough_dec
//Statements interrupted by the preprocessor cannot be processed by this intent.//MyInfo
//The remainder of the header file sal.h is ignored.
#endif


/*
 * We need memory copying and zeroing functions, plus strncpy().
 * ANSI and System V implementations declare these in <string.h>.
 * BSD doesn't have the mem() functions, but it does have bcopy()/bzero().
 * Some systems may declare memset and memcpy in <memory.h>.
 *
 * NOTE: we assume the size parameters to these functions are of type size_t.
 * Change the casts in these macros if not!
 */

#if NEED_BSD_STRINGS

#define IDS_DETAILS_WITHOUT_SUMMARY_LABEL
#define IDS_FORM_CALENDAR_CLEAR
#define IDS_FORM_CALENDAR_TODAY
#define IDS_FORM_SUBMIT_LABEL
#define IDS_FORM_INPUT_ALT
#define IDS_FORM_RESET_LABEL
#define IDS_FORM_FILE_BUTTON_LABEL
#define IDS_FORM_MULTIPLE_FILES_BUTTON_LABEL
#define IDS_FORM_FILE_NO_FILE_LABEL
#define IDS_FORM_FILE_MULTIPLE_UPLOAD
#define IDS_FORM_OTHER_COLOR_LABEL
#define IDS_FORM_OTHER_DATE_LABEL
#define IDS_FORM_OTHER_MONTH_LABEL
#define IDS_FORM_OTHER_WEEK_LABEL
#define IDS_FORM_PLACEHOLDER_FOR_DAY_OF_MONTH_FIELD
#define IDS_FORM_PLACEHOLDER_FOR_MONTH_FIELD
#define IDS_FORM_PLACEHOLDER_FOR_YEAR_FIELD
#define IDS_FORM_SELECT_MENU_LIST_TEXT
#define IDS_FORM_THIS_MONTH_LABEL
#define IDS_FORM_THIS_WEEK_LABEL
#define IDS_FORM_WEEK_NUMBER_LABEL
#define IDS_AX_CALENDAR_SHOW_DATE_PICKER
#define IDS_AX_CALENDAR_SHOW_MONTH_SELECTOR
#define IDS_AX_CALENDAR_SHOW_NEXT_MONTH
#define IDS_AX_CALENDAR_SHOW_PREVIOUS_MONTH
#define IDS_AX_CALENDAR_WEEK_DESCRIPTION
#define IDS_AX_ROLE_ARTICLE
#define IDS_AX_ROLE_AUDIO
#define IDS_AX_ROLE_BANNER
#define IDS_AX_ROLE_CODE
#define IDS_AX_ROLE_COLOR_WELL
#define IDS_AX_ROLE_COMMENT
#define IDS_AX_ROLE_COMMENT_SECTION
#define IDS_AX_ROLE_COMPLEMENTARY
#define IDS_AX_ROLE_CONTENT_DELETION
#define IDS_AX_ROLE_CONTENT_INSERTION
#define IDS_AX_ROLE_CHECK_BOX
#define IDS_AX_ROLE_CONTENT_INFO
#define IDS_AX_ROLE_DATE
#define IDS_AX_ROLE_DATE_TIME_LOCAL
#define IDS_AX_ROLE_DEFINITION
#define IDS_AX_ROLE_DESCRIPTION_LIST
#define IDS_AX_ROLE_DESCRIPTION_TERM
#define IDS_AX_ROLE_DETAILS
#define IDS_AX_ROLE_DISCLOSURE_TRIANGLE
#define IDS_AX_ROLE_DOC_ABSTRACT
#define IDS_AX_ROLE_DOC_ACKNOWLEDGMENTS
#define IDS_AX_ROLE_DOC_AFTERWORD
#define IDS_AX_ROLE_DOC_APPENDIX
#define IDS_AX_ROLE_DOC_BACKLINK
#define IDS_AX_ROLE_DOC_BIBLIO_ENTRY
#define IDS_AX_ROLE_DOC_BIBLIOGRAPHY
#define IDS_AX_ROLE_DOC_BIBLIO_REF
#define IDS_AX_ROLE_DOC_CHAPTER
#define IDS_AX_ROLE_DOC_COLOPHON
#define IDS_AX_ROLE_DOC_CONCLUSION
#define IDS_AX_ROLE_DOC_COVER
#define IDS_AX_ROLE_DOC_CREDIT
#define IDS_AX_ROLE_DOC_CREDITS
#define IDS_AX_ROLE_DOC_DEDICATION
#define IDS_AX_ROLE_DOC_ENDNOTE
#define IDS_AX_ROLE_DOC_ENDNOTES
#define IDS_AX_ROLE_DOC_EPIGRAPH
#define IDS_AX_ROLE_DOC_EPILOGUE
#define IDS_AX_ROLE_DOC_ERRATA
#define IDS_AX_ROLE_DOC_EXAMPLE
#define IDS_AX_ROLE_DOC_FOOTNOTE
#define IDS_AX_ROLE_DOC_FOREWORD
#define IDS_AX_ROLE_DOC_GLOSSARY
#define IDS_AX_ROLE_DOC_GLOSS_REF
#define IDS_AX_ROLE_DOC_INDEX
#define IDS_AX_ROLE_DOC_INTRODUCTION
#define IDS_AX_ROLE_DOC_NOTE_REF
#define IDS_AX_ROLE_DOC_NOTICE
#define IDS_AX_ROLE_DOC_PAGE_BREAK
#define IDS_AX_ROLE_DOC_PAGE_LIST
#define IDS_AX_ROLE_DOC_PART
#define IDS_AX_ROLE_DOC_PREFACE
#define IDS_AX_ROLE_DOC_PROLOGUE
#define IDS_AX_ROLE_DOC_PULLQUOTE
#define IDS_AX_ROLE_DOC_QNA
#define IDS_AX_ROLE_DOC_SUBTITLE
#define IDS_AX_ROLE_DOC_TIP
#define IDS_AX_ROLE_DOC_TOC
#define IDS_AX_ROLE_EMPHASIS
#define IDS_AX_ROLE_FEED
#define IDS_AX_ROLE_FIGURE
#define IDS_AX_ROLE_FORM
#define IDS_AX_ROLE_FOOTER
#define IDS_AX_ROLE_GRAPHICS_DOCUMENT
#define IDS_AX_ROLE_GRAPHICS_OBJECT
#define IDS_AX_ROLE_GRAPHICS_SYMBOL
#define IDS_AX_ROLE_EMAIL
#define IDS_AX_AUTOFILL_POPUP_ACCESSIBLE_NODE_DATA
#define IDS_AX_ROLE_TOGGLE_BUTTON
#define IDS_AX_ROLE_HEADER
#define IDS_AX_ROLE_HEADING
#define IDS_AX_ROLE_LINK
#define IDS_AX_ROLE_MAIN_CONTENT
#define IDS_AX_ROLE_MARK
#define IDS_AX_ROLE_MATH
#define IDS_AX_ROLE_METER
#define IDS_AX_ROLE_NAVIGATIONAL_LINK
#define IDS_AX_ROLE_OUTPUT
#define IDS_AX_ROLE_REGION
#define IDS_AX_ROLE_REVISION
#define IDS_AX_ROLE_SEARCH_BOX
#define IDS_AX_ROLE_SECTION
#define IDS_AX_ROLE_STATUS
#define IDS_AX_ROLE_STRONG
#define IDS_AX_ROLE_SUGGESTION
#define IDS_AX_ROLE_SWITCH
#define IDS_AX_ROLE_TELEPHONE
#define IDS_AX_ROLE_TIME
#define IDS_AX_ROLE_URL
#define IDS_AX_ROLE_WEB_AREA
#define IDS_AX_ROLE_WEEK
#define IDS_AX_UNLABELED_IMAGE_ROLE_DESCRIPTION
#define IDS_AX_IMAGE_ELIGIBLE_FOR_ANNOTATION
#define IDS_AX_IMAGE_ANNOTATION_PENDING
#define IDS_AX_IMAGE_ANNOTATION_ADULT
#define IDS_AX_IMAGE_ANNOTATION_NO_DESCRIPTION
#define IDS_AX_IMAGE_ANNOTATION_OCR_CONTEXT
#define IDS_AX_IMAGE_ANNOTATION_DESCRIPTION_CONTEXT
#define IDS_AX_AM_PM_FIELD_TEXT
#define IDS_AX_DAY_OF_MONTH_FIELD_TEXT
#define IDS_AX_HOUR_FIELD_TEXT
#define IDS_AX_MEDIA_DEFAULT
#define IDS_AX_MEDIA_AUDIO_ELEMENT
#define IDS_AX_MEDIA_VIDEO_ELEMENT
#define IDS_AX_MEDIA_MUTE_BUTTON
#define IDS_AX_MEDIA_UNMUTE_BUTTON
#define IDS_AX_MEDIA_PLAY_BUTTON
#define IDS_AX_MEDIA_PAUSE_BUTTON
#define IDS_AX_MEDIA_CURRENT_TIME_DISPLAY
#define IDS_AX_MEDIA_TIME_REMAINING_DISPLAY
#define IDS_AX_MEDIA_ENTER_FULL_SCREEN_BUTTON
#define IDS_AX_MEDIA_EXIT_FULL_SCREEN_BUTTON
#define IDS_AX_MEDIA_DISPLAY_CUT_OUT_FULL_SCREEN_BUTTON
#define IDS_AX_MEDIA_ENTER_PICTURE_IN_PICTURE_BUTTON
#define IDS_AX_MEDIA_EXIT_PICTURE_IN_PICTURE_BUTTON
#define IDS_AX_MEDIA_LOADING_PANEL
#define IDS_AX_MEDIA_SHOW_CLOSED_CAPTIONS_MENU_BUTTON
#define IDS_AX_MEDIA_HIDE_CLOSED_CAPTIONS_MENU_BUTTON
#define IDS_AX_MEDIA_CAST_OFF_BUTTON
#define IDS_AX_MEDIA_CAST_ON_BUTTON
#define IDS_AX_MEDIA_DOWNLOAD_BUTTON
#define IDS_AX_MEDIA_OVERFLOW_BUTTON
#define IDS_AX_MEDIA_AUDIO_ELEMENT_HELP
#define IDS_AX_MEDIA_VIDEO_ELEMENT_HELP
#define IDS_AX_MEDIA_AUDIO_SLIDER_HELP
#define IDS_AX_MEDIA_VIDEO_SLIDER_HELP
#define IDS_AX_MEDIA_VOLUME_SLIDER_HELP
#define IDS_AX_MEDIA_CURRENT_TIME_DISPLAY_HELP
#define IDS_AX_MEDIA_TIME_REMAINING_DISPLAY_HELP
#define IDS_AX_MEDIA_OVERFLOW_BUTTON_HELP
#define IDS_AX_MILLISECOND_FIELD_TEXT
#define IDS_AX_MINUTE_FIELD_TEXT
#define IDS_AX_MONTH_FIELD_TEXT
#define IDS_AX_SECOND_FIELD_TEXT
#define IDS_AX_WEEK_OF_YEAR_FIELD_TEXT
#define IDS_AX_YEAR_FIELD_TEXT
#define IDS_FORM_INPUT_WEEK_TEMPLATE
#define IDS_FORM_VALIDATION_VALUE_MISSING_MULTIPLE_FILE
#define IDS_FORM_VALIDATION_TYPE_MISMATCH
#define IDS_FORM_VALIDATION_TYPE_MISMATCH_EMAIL_EMPTY
#define IDS_FORM_VALIDATION_TYPE_MISMATCH_EMAIL_EMPTY_DOMAIN
#define IDS_FORM_VALIDATION_TYPE_MISMATCH_EMAIL_EMPTY_LOCAL
#define IDS_FORM_VALIDATION_TYPE_MISMATCH_EMAIL_INVALID_DOMAIN
#define IDS_FORM_VALIDATION_TYPE_MISMATCH_EMAIL_INVALID_DOTS
#define IDS_FORM_VALIDATION_TYPE_MISMATCH_EMAIL_INVALID_LOCAL
#define IDS_FORM_VALIDATION_TYPE_MISMATCH_EMAIL_NO_AT_SIGN
#define IDS_FORM_VALIDATION_TYPE_MISMATCH_MULTIPLE_EMAIL
#define IDS_FORM_VALIDATION_RANGE_UNDERFLOW
#define IDS_FORM_VALIDATION_RANGE_UNDERFLOW_DATETIME
#define IDS_FORM_VALIDATION_RANGE_OVERFLOW
#define IDS_FORM_VALIDATION_RANGE_OVERFLOW_DATETIME
#define IDS_FORM_VALIDATION_BAD_INPUT_DATETIME
#define IDS_FORM_VALIDATION_BAD_INPUT_NUMBER
#define IDS_FORM_VALIDATION_VALUE_MISSING
#define IDS_FORM_VALIDATION_VALUE_MISSING_CHECKBOX
#define IDS_FORM_VALIDATION_VALUE_MISSING_FILE
#define IDS_FORM_VALIDATION_VALUE_MISSING_RADIO
#define IDS_FORM_VALIDATION_VALUE_MISSING_SELECT
#define IDS_FORM_VALIDATION_TYPE_MISMATCH_EMAIL
#define IDS_FORM_VALIDATION_TYPE_MISMATCH_URL
#define IDS_FORM_VALIDATION_PATTERN_MISMATCH
#define IDS_FORM_VALIDATION_STEP_MISMATCH
#define IDS_FORM_VALIDATION_STEP_MISMATCH_CLOSE_TO_LIMIT
#define IDS_FORM_VALIDATION_TOO_LONG
#define IDS_FORM_VALIDATION_TOO_SHORT
#define IDS_FORM_VALIDATION_TOO_SHORT_PLURAL
#define IDS_MEDIA_SESSION_FILE_SOURCE
#define IDS_MEDIA_OVERFLOW_MENU_CLOSED_CAPTIONS
#define IDS_MEDIA_OVERFLOW_MENU_CLOSED_CAPTIONS_SUBMENU_TITLE
#define IDS_MEDIA_OVERFLOW_MENU_CAST
#define IDS_MEDIA_OVERFLOW_MENU_ENTER_FULLSCREEN
#define IDS_MEDIA_OVERFLOW_MENU_EXIT_FULLSCREEN
#define IDS_MEDIA_OVERFLOW_MENU_MUTE
#define IDS_MEDIA_OVERFLOW_MENU_UNMUTE
#define IDS_MEDIA_OVERFLOW_MENU_PLAY
#define IDS_MEDIA_OVERFLOW_MENU_PAUSE
#define IDS_MEDIA_OVERFLOW_MENU_DOWNLOAD
#define IDS_MEDIA_OVERFLOW_MENU_ENTER_PICTURE_IN_PICTURE
#define IDS_MEDIA_OVERFLOW_MENU_EXIT_PICTURE_IN_PICTURE
#define IDS_MEDIA_PICTURE_IN_PICTURE_INTERSTITIAL_TEXT
#define IDS_MEDIA_REMOTING_CAST_TEXT
#define IDS_MEDIA_REMOTING_CAST_TO_UNKNOWN_DEVICE_TEXT
#define IDS_MEDIA_REMOTING_STOP_TEXT
#define IDS_MEDIA_REMOTING_STOP_BY_PLAYBACK_QUALITY_TEXT
#define IDS_MEDIA_REMOTING_STOP_BY_ERROR_TEXT
#define IDS_MEDIA_SCRUBBING_MESSAGE_TEXT
#define IDS_MEDIA_TRACKS_NO_LABEL
#define IDS_MEDIA_TRACKS_OFF
#define IDS_PLUGIN_INITIALIZATION_ERROR
#define IDS_MEDIA_PLAYBACK_ERROR
#define IDS_UNITS_KIBIBYTES
#define IDS_UNITS_MEBIBYTES
#define IDS_UNITS_GIBIBYTES
#define IDS_UNITS_TEBIBYTES
#define IDS_UNITS_PEBIBYTES
#define CONTENT_INVALID_TRUE
#define CONTENT_INVALID_SPELLING
#define CONTENT_INVALID_GRAMMAR
#define IDS_TEXT_FILES
#define IDS_CONTENT_CONTEXT_NO_SPELLING_SUGGESTIONS
#define IDS_SETTINGS_ABOUT_PROGRAM
#define IDS_SETTINGS_GET_HELP_USING_CHROME
#define IDS_SETTINGS_UPGRADE_UPDATING
#define IDS_SETTINGS_UPGRADE_UPDATING_PERCENT
#define IDS_SETTINGS_UPGRADE_SUCCESSFUL_RELAUNCH
#define IDS_SETTINGS_UPGRADE_UP_TO_DATE
#define IDS_SETTINGS_SITE_SETTINGS_DELETE_DATA_POST_SESSION
#define IDS_SETTINGS_GOOGLE_PAYMENTS_CACHED
#define IDS_SETTINGS_DEFAULT_BROWSER_DEFAULT
#define IDS_SETTINGS_DEFAULT_BROWSER_MAKE_DEFAULT
#define IDS_SETTINGS_DEFAULT_BROWSER_ERROR
#define IDS_SETTINGS_DEFAULT_BROWSER_SECONDARY
#define IDS_SETTINGS_SPELLING_PREF_DESC
#define IDS_SETTINGS_RESTART_TO_APPLY_CHANGES
#define IDS_SETTINGS_SIGNIN_ALLOWED
#define IDS_SETTINGS_SIGNIN_ALLOWED_DESC
#define IDS_SETTINGS_SYNC_DISCONNECT_DELETE_PROFILE_WARNING_WITH_COUNTS_SINGULAR
#define IDS_SETTINGS_SYNC_DISCONNECT_DELETE_PROFILE_WARNING_WITH_COUNTS_PLURAL
#define IDS_SETTINGS_SYNC_DISCONNECT_DELETE_PROFILE_WARNING_WITHOUT_COUNTS
#define IDS_SETTINGS_PROFILE_NAME_AND_PICTURE
#define IDS_SETTINGS_PEOPLE_SIGN_IN_PROMPT_SECONDARY_WITH_ACCOUNT
#define IDS_SETTINGS_SYNC_SIGNIN
#define IDS_SETTINGS_SYNC_DATA_ENCRYPTED_TEXT
#define IDS_SETTINGS_SYNC_DISCONNECT_TITLE
#define IDS_DRIVE_SUGGEST_PREF_DESC
#define IDS_SETTINGS_SYNC_SIGN_IN_PROMPT_WITH_NO_ACCOUNT
#define IDS_SETTINGS_SYNC_SIGN_IN_PROMPT_WITH_ACCOUNT
#define IDS_SETTINGS_LANGUAGES_IS_DISPLAYED_IN_THIS_LANGUAGE
#define IDS_SETTINGS_LANGUAGES_DISPLAY_IN_THIS_LANGUAGE
#define IDS_SETTINGS_SYSTEM_BACKGROUND_APPS_LABEL
#define IDS_SETTINGS_RESET_PROFILE_FEEDBACK
#define IDS_PRODUCT_NAME
#define IDS_SHORT_PRODUCT_NAME
#define IDS_SXS_SHORTCUT_NAME
#define IDS_SHORTCUT_NAME_BETA
#define IDS_SHORTCUT_NAME_DEV
#define IDS_PRODUCT_DESCRIPTION
#define IDS_SHORT_PRODUCT_LOGO_ALT_TEXT
#define IDS_PRODUCT_LOGO_ENTERPRISE_ALT_TEXT
#define IDS_SHORTCUT_NEW_WINDOW
#define IDS_TASK_MANAGER_TITLE
#define IDS_SESSION_CRASHED_VIEW_UMA_OPTIN
#define IDS_BROWSER_WINDOW_TITLE_FORMAT
#define IDS_ACCESSIBLE_BROWSER_WINDOW_TITLE_FORMAT
#define IDS_ACCESSIBLE_BETA_BROWSER_WINDOW_TITLE_FORMAT
#define IDS_ACCESSIBLE_DEV_BROWSER_WINDOW_TITLE_FORMAT
#define IDS_ACCESSIBLE_CANARY_BROWSER_WINDOW_TITLE_FORMAT
#define IDS_ABOUT_VERSION_COMPANY_NAME
#define IDS_ABOUT_VERSION_COPYRIGHT
#define IDS_ABOUT_TERMS_OF_SERVICE
#define IDS_WIN_XP_VISTA_OBSOLETE
#define IDS_ACCNAME_APP
#define IDS_BROWSER_HUNGBROWSER_MESSAGE
#define IDS_UNINSTALL_CLOSE_APP
#define IDS_UNINSTALL_VERIFY
#define IDS_UNINSTALL_CHROME
#define IDS_FR_CUSTOMIZE_DEFAULT_BROWSER
#define IDS_STATUS_TRAY_KEEP_CHROME_RUNNING_IN_BACKGROUND
#define IDS_CANT_WRITE_USER_DIRECTORY_SUMMARY
#define IDS_PROFILE_TOO_NEW_ERROR
#define IDS_PREFERENCES_UNREADABLE_ERROR
#define IDS_PREFERENCES_CORRUPT_ERROR
#define IDS_CRASH_RECOVERY_TITLE
#define IDS_CRASH_RECOVERY_CONTENT
#define IDS_PASSWORD_GENERATION_PROMPT
#define IDS_PASSWORD_MANAGER_ONBOARDING_DETAILS_C
#define IDS_PASSWORD_MANAGER_TITLE_BRAND
#define IDS_PASSWORDS_PAGE_AUTHENTICATION_PROMPT
#define IDS_PASSWORDS_PAGE_EXPORT_AUTHENTICATION_PROMPT
#define IDS_INSTALL_HIGHER_VERSION
#define IDS_INSTALL_FAILED
#define IDS_SAME_VERSION_REPAIR_FAILED
#define IDS_SETUP_PATCH_FAILED
#define IDS_INSTALL_OS_NOT_SUPPORTED
#define IDS_INSTALL_OS_ERROR
#define IDS_INSTALL_SINGLETON_ACQUISITION_FAILED
#define IDS_INSTALL_TEMP_DIR_FAILED
#define IDS_INSTALL_UNCOMPRESSION_FAILED
#define IDS_INSTALL_INVALID_ARCHIVE
#define IDS_INSTALL_INSUFFICIENT_RIGHTS
#define IDS_INSTALL_EXISTING_VERSION_LAUNCHED
#define IDS_SHORTCUT_TOOLTIP
#define IDS_UNINSTALL_DELETE_PROFILE
#define IDS_UNINSTALL_SET_DEFAULT_BROWSER
#define IDS_UNINSTALL_BUTTON_TEXT
#define IDS_DEFAULT_BROWSER_INFOBAR_TEXT
#define IDS_TRY_TOAST_HEADING
#define IDS_TRY_TOAST_HEADING2
#define IDS_TRY_TOAST_HEADING3
#define IDS_TRY_TOAST_HEADING4
#define IDS_TRY_TOAST_HEADING_SKYPE
#define IDS_PRINT_PREVIEW_NO_PLUGIN
#define IDS_DOWNLOAD_STATUS_CRX_INSTALL_RUNNING
#define IDS_PROMPT_DOWNLOAD_CHANGES_SETTINGS
#define IDS_PROMPT_MALICIOUS_DOWNLOAD_URL
#define IDS_PROMPT_MALICIOUS_DOWNLOAD_CONTENT
#define IDS_BLOCK_REASON_DANGEROUS_DOWNLOAD
#define IDS_BLOCK_REASON_UNWANTED_DOWNLOAD
#define IDS_ABANDON_DOWNLOAD_DIALOG_BROWSER_MESSAGE
#define IDS_MISSING_GOOGLE_API_KEYS
#define IDS_EXTENSION_INSTALLED_HEADING
#define IDS_EXTENSION_UNINSTALL_PROMPT_REMOVE_DATA_CHECKBOX
#define IDS_EXTENSIONS_HIDE_BUTTON_IN_MENU
#define IDS_EXTENSIONS_INCOGNITO_WARNING
#define IDS_EXTENSIONS_UNINSTALL
#define IDS_EXTENSIONS_SHORTCUT_SCOPE_IN_CHROME
#define IDS_EXTENSIONS_MULTIPLE_UNSUPPORTED_DISABLED_BODY
#define IDS_EXTENSIONS_SINGLE_UNSUPPORTED_DISABLED_BODY
#define IDS_APPMENU_TOOLTIP
#define IDS_APPMENU_TOOLTIP_UPDATE_AVAILABLE
#define IDS_APPMENU_TOOLTIP_ALERT
#define IDS_OPEN_IN_CHROME
#define IDS_ABOUT
#define IDS_UPDATE_NOW
#define IDS_CHROME_SIGNIN_TITLE
#define IDS_PROFILES_DICE_SYNC_PROMO
#define IDS_ONE_CLICK_SIGNIN_DIALOG_TITLE_NEW
#define IDS_ONE_CLICK_SIGNIN_DIALOG_MESSAGE_NEW
#define IDS_SYNC_WRONG_EMAIL
#define IDS_SYNC_USED_PROFILE_ERROR
#define IDS_ENTERPRISE_SIGNIN_TITLE
#define IDS_ENTERPRISE_SIGNIN_EXPLANATION_WITHOUT_PROFILE_CREATION
#define IDS_ENTERPRISE_SIGNIN_EXPLANATION_WITH_PROFILE_CREATION
#define IDS_ABOUT_BROWSER_SWITCH_DESCRIPTION_UNKNOWN_BROWSER
#define IDS_ABOUT_BROWSER_SWITCH_DESCRIPTION_KNOWN_BROWSER
#define IDS_SIGNIN_EMAIL_CONFIRMATION_TITLE
#define IDS_CHROME_CLEANUP_PROMPT_EXPLANATION
#define IDS_SYNC_PASSPHRASE_ERROR_BUBBLE_VIEW_MESSAGE
#define IDS_SYNC_SIGN_IN_ERROR_BUBBLE_VIEW_MESSAGE
#define IDS_SYNC_UNAVAILABLE_ERROR_BUBBLE_VIEW_MESSAGE
#define IDS_SYNC_OTHER_SIGN_IN_ERROR_BUBBLE_VIEW_MESSAGE
#define IDS_SYNC_PAUSED_REASON_CLEAR_COOKIES_ON_EXIT
#define IDS_SYNC_PAUSED_REASON_CLEAR_COOKIES_ON_EXIT_LINK_TEXT
#define IDS_APP_SHORTCUTS_SUBDIR_NAME
#define IDS_APP_SHORTCUTS_SUBDIR_NAME_CANARY
#define IDS_APP_SHORTCUTS_SUBDIR_NAME_BETA
#define IDS_APP_SHORTCUTS_SUBDIR_NAME_DEV
#define IDS_MEDIA_STREAM_STATUS_TRAY_TEXT_AUDIO_AND_VIDEO
#define IDS_MEDIA_STREAM_STATUS_TRAY_TEXT_AUDIO_ONLY
#define IDS_MEDIA_STREAM_STATUS_TRAY_TEXT_VIDEO_ONLY
#define IDS_LOGIN_POD_USER_REMOVE_WARNING_SYNC
#define IDS_USER_MANAGER_TUTORIAL_SLIDE_INTRO_TITLE
#define IDS_USER_MANAGER_TUTORIAL_SLIDE_INTRO_TEXT
#define IDS_USER_MANAGER_TUTORIAL_SLIDE_YOUR_CHROME_TITLE
#define IDS_USER_MANAGER_TUTORIAL_SLIDE_YOUR_CHROME_TEXT
#define IDS_USER_MANAGER_TUTORIAL_SLIDE_GUEST_TEXT
#define IDS_USER_MANAGER_TUTORIAL_SLIDE_FRIENDS_TEXT
#define IDS_USER_MANAGER_TUTORIAL_SLIDE_OUTRO_TEXT
#define IDS_USER_MANAGER_TUTORIAL_SLIDE_OUTRO_ADD_USER
#define IDS_EXTENSIONS_SETTINGS_API_FIRST_LINE_START_PAGES_SPECIFIC
#define IDS_EXTENSIONS_SETTINGS_API_FIRST_LINE_START_PAGES
#define IDS_EXTENSIONS_SETTINGS_API_SECOND_LINE_START_PAGES
#define IDS_EXTENSIONS_SETTINGS_API_SECOND_LINE_START_AND_HOME
#define IDS_EXTENSIONS_SETTINGS_API_SECOND_LINE_START_AND_SEARCH
#define IDS_WEBSTORE_APP_DESCRIPTION
#define IDS_INBOUND_MDNS_RULE_NAME
#define IDS_INBOUND_MDNS_RULE_NAME_BETA
#define IDS_INBOUND_MDNS_RULE_NAME_CANARY
#define IDS_INBOUND_MDNS_RULE_NAME_DEV
#define IDS_INBOUND_MDNS_RULE_DESCRIPTION
#define IDS_INBOUND_MDNS_RULE_DESCRIPTION_BETA
#define IDS_INBOUND_MDNS_RULE_DESCRIPTION_CANARY
#define IDS_INBOUND_MDNS_RULE_DESCRIPTION_DEV
#define IDS_CONTENT_CONTEXT_ACCESSIBILITY_LABELS_BUBBLE_TEXT
#define IDS_CONTENT_CONTEXT_ACCESSIBILITY_LABELS_BUBBLE_TEXT_ONCE
#define IDS_CONTENT_CONTEXT_SPELLING_BUBBLE_TEXT
#define IDS_CONTENT_CONTEXT_OPENLINKNEWTAB_INAPP
#define IDS_CONTENT_CONTEXT_OPENLINKOFFTHERECORD_INAPP
#define IDS_UPDATE_RECOMMENDED_DIALOG_TITLE
#define IDS_UPDATE_RECOMMENDED
#define IDS_RELAUNCH_AND_UPDATE
#define IDS_UPDATE_OTHER_INSTANCES_SAME_USER_DIALOG_TITLE
#define IDS_UPDATE_OTHER_INSTANCES_SAME_USER_DIALOG_MESSAGE
#define IDS_UPDATE_OTHER_INSTANCES_OTHER_USER_AUTHENTICATION_PROMPT
#define IDS_REINSTALL_APP
#define IDS_UPGRADE_BUBBLE_MENU_ITEM
#define IDS_UPGRADE_BUBBLE_TITLE
#define IDS_UPGRADE_BUBBLE_TEXT
#define IDS_SYNC_ERROR_USER_MENU_UPGRADE_MESSAGE
#define IDS_SYNC_ERROR_USER_MENU_UPGRADE_BUTTON
#define IDS_SYNC_UPGRADE_CLIENT
#define IDS_SYNC_UPGRADE_CLIENT_LINK_LABEL
#define IDS_RECOVERY_BUBBLE_TITLE
#define IDS_RUN_RECOVERY
#define IDS_RECOVERY_BUBBLE_TEXT
#define IDS_CRITICAL_NOTIFICATION_TITLE
#define IDS_CRITICAL_NOTIFICATION_TITLE_ALTERNATE
#define IDS_CRITICAL_NOTIFICATION_TEXT
#define IDS_DESKTOP_MEDIA_PICKER_SOURCE_TYPE_TAB
#define IDS_WELCOME_HEADER
#define IDS_WIN_NOTIFICATION_SETTINGS_CONTEXT_MENU_ITEM_NAME
#define IDS_RELAUNCH_RECOMMENDED_TITLE
#define IDS_RELAUNCH_RECOMMENDED_BODY
#define IDS_RELAUNCH_REQUIRED_TITLE_DAYS
#define IDS_RELAUNCH_REQUIRED_TITLE_HOURS
#define IDS_RELAUNCH_REQUIRED_TITLE_MINUTES
#define IDS_RELAUNCH_REQUIRED_TITLE_SECONDS
#define IDS_RELAUNCH_REQUIRED_BODY
#define IDS_ENTERPRISE_STARTUP_CLOUD_POLICY_ENROLLMENT_TOOLTIP
#define IDS_ENTERPRISE_STARTUP_CLOUD_POLICY_ENROLLMENT_ERROR
#define IDS_ENTERPRISE_STARTUP_RELAUNCH_BUTTON
#define IDS_DESKTOP_MEDIA_PICKER_TITLE_WEB_CONTENTS_ONLY
#define IDS_HATS_BUBBLE_TITLE
#define IDS_JAVASCRIPT_MESSAGEBOX_TITLE
#define IDS_JAVASCRIPT_MESSAGEBOX_TITLE_IFRAME
#define IDS_JAVASCRIPT_MESSAGEBOX_TITLE_NONSTANDARD_URL
#define IDS_JAVASCRIPT_MESSAGEBOX_TITLE_NONSTANDARD_URL_IFRAME
#define IDS_JAVASCRIPT_MESSAGEBOX_SUPPRESS_OPTION
#define IDS_BEFOREUNLOAD_MESSAGEBOX_TITLE
#define IDS_BEFOREUNLOAD_APP_MESSAGEBOX_TITLE
#define IDS_BEFOREUNLOAD_MESSAGEBOX_OK_BUTTON_LABEL
#define IDS_BEFOREUNLOAD_MESSAGEBOX_MESSAGE
#define IDS_BEFORERELOAD_MESSAGEBOX_TITLE
#define IDS_BEFORERELOAD_APP_MESSAGEBOX_TITLE
#define IDS_BEFORERELOAD_MESSAGEBOX_OK_BUTTON_LABEL
#define IDS_AUTOFILL_ASSISTANT_PAYMENT_INFO_CONFIRM
#define IDS_AUTOFILL_ASSISTANT_DEFAULT_ERROR
#define IDS_AUTOFILL_ASSISTANT_LOADING
#define IDS_AUTOFILL_ASSISTANT_GIVE_UP
#define IDS_AUTOFILL_SYNC_PROMO_MESSAGE
#define IDS_AUTOFILL_NO_THANKS_DESKTOP_LOCAL_SAVE
#define IDS_AUTOFILL_NO_THANKS_DESKTOP_UPLOAD_SAVE
#define IDS_AUTOFILL_FIELD_LABEL_PHONE
#define IDS_AUTOFILL_FIELD_LABEL_BILLING_ADDRESS
#define IDS_AUTOFILL_SAVE_CARD_BUBBLE_LOCAL_SAVE_ACCEPT
#define IDS_AUTOFILL_SAVE_CARD_BUBBLE_UPLOAD_SAVE_ACCEPT
#define IDS_AUTOFILL_SAVE_CARD_PROMPT_CONTINUE
#define IDS_AUTOFILL_SAVE_CARD_PROMPT_TITLE_LOCAL
#define IDS_AUTOFILL_FIX_FLOW_PROMPT_SAVE_CARD_LABEL
#define IDS_AUTOFILL_SAVE_CARD_PROMPT_TITLE_TO_CLOUD
#define IDS_AUTOFILL_SAVE_CARD_PROMPT_TITLE_TO_CLOUD_V3
#define IDS_AUTOFILL_SAVE_CARD_PROMPT_TITLE_TO_CLOUD_V4
#define IDS_AUTOFILL_CARD_SAVED
#define IDS_AUTOFILL_MANAGE_CARDS
#define IDS_AUTOFILL_DONE
#define IDS_AUTOFILL_FAILURE_BUBBLE_TITLE
#define IDS_AUTOFILL_FAILURE_BUBBLE_EXPLANATION
#define IDS_AUTOFILL_SAVE_CARD_PROMPT_UPLOAD_EXPLANATION
#define IDS_AUTOFILL_SAVE_CARD_PROMPT_UPLOAD_EXPLANATION_V3
#define IDS_AUTOFILL_SAVE_CARD_PROMPT_UPLOAD_EXPLANATION_V3_WITH_DEVICE
#define IDS_AUTOFILL_SAVE_CARD_PROMPT_UPLOAD_EXPLANATION_V3_WITH_NAME
#define IDS_AUTOFILL_SAVE_CARD_PROMPT_UPLOAD_EXPLANATION_V3_WITH_NAME_AND_DEVICE
#define IDS_AUTOFILL_SAVE_CARD_PROMPT_CARDHOLDER_NAME
#define IDS_AUTOFILL_SAVE_CARD_PROMPT_CARDHOLDER_NAME_TOOLTIP
#define IDS_AUTOFILL_SAVE_CARD_CARDHOLDER_NAME_FIX_FLOW_HEADER
#define IDS_AUTOFILL_SAVE_CARD_UPDATE_EXPIRATION_DATE_TITLE
#define IDS_AUTOFILL_SAVE_CARD_PROMPT_UPLOAD_EXPLANATION_TOOLTIP
#define IDS_AUTOFILL_SAVE_CARD_PROMPT_UPLOAD_EXPLANATION_AND_CARDHOLDER_NAME_TOOLTIP
#define IDS_AUTOFILL_GOOGLE_PAY_LOGO_ACCESSIBLE_NAME
#define IDS_AUTOFILL_LOCAL_CARD_MIGRATION_ANIMATION_LABEL
#define IDS_AUTOFILL_LOCAL_CARD_MIGRATION_BUBBLE_TITLE
#define IDS_AUTOFILL_LOCAL_CARD_MIGRATION_BUBBLE_BUTTON_LABEL
#define IDS_AUTOFILL_LOCAL_CARD_MIGRATION_BUBBLE_BODY_TEXT
#define IDS_AUTOFILL_LOCAL_CARD_MIGRATION_DIALOG_TITLE_OFFER
#define IDS_AUTOFILL_LOCAL_CARD_MIGRATION_DIALOG_TITLE_DONE
#define IDS_AUTOFILL_LOCAL_CARD_MIGRATION_DIALOG_TITLE_FIX
#define IDS_AUTOFILL_LOCAL_CARD_MIGRATION_DIALOG_CHECKBOX_UNCHECK_WARNING
#define IDS_AUTOFILL_LOCAL_CARD_MIGRATION_DIALOG_MESSAGE_OFFER
#define IDS_AUTOFILL_LOCAL_CARD_MIGRATION_DIALOG_MESSAGE_DONE
#define IDS_AUTOFILL_LOCAL_CARD_MIGRATION_DIALOG_MESSAGE_ERROR
#define IDS_AUTOFILL_LOCAL_CARD_MIGRATION_DIALOG_MESSAGE_FIX
#define IDS_AUTOFILL_LOCAL_CARD_MIGRATION_DIALOG_MESSAGE_INVALID_CARD_REMOVED
#define IDS_AUTOFILL_LOCAL_CARD_MIGRATION_DIALOG_BUTTON_LABEL_SAVE
#define IDS_AUTOFILL_LOCAL_CARD_MIGRATION_DIALOG_BUTTON_LABEL_CANCEL
#define IDS_AUTOFILL_LOCAL_CARD_MIGRATION_DIALOG_BUTTON_LABEL_DONE
#define IDS_AUTOFILL_LOCAL_CARD_MIGRATION_DIALOG_BUTTON_LABEL_VIEW_CARDS
#define IDS_AUTOFILL_LOCAL_CARD_MIGRATION_DIALOG_LABEL_INVALID_CARDS
#define IDS_AUTOFILL_LOCAL_CARD_MIGRATION_DIALOG_TRASH_CAN_BUTTON_TOOLTIP
#define IDS_AUTOFILL_CARD_UNMASK_PROMPT_ERROR_TRY_AGAIN_CVC
#define IDS_AUTOFILL_CARD_UNMASK_PROMPT_ERROR_TRY_AGAIN_CVC_AND_EXPIRATION_V2
#define IDS_AUTOFILL_CARD_UNMASK_PROMPT_ERROR_PERMANENT
#define IDS_AUTOFILL_CARD_UNMASK_PROMPT_ERROR_NETWORK
#define IDS_AUTOFILL_CARD_UNMASK_PROMPT_TITLE
#define IDS_AUTOFILL_CARD_UNMASK_PROMPT_TITLE_V2
#define IDS_AUTOFILL_CARD_UNMASK_PROMPT_EXPIRED_TITLE
#define IDS_AUTOFILL_CARD_UNMASK_PROMPT_INSTRUCTIONS
#define IDS_AUTOFILL_CARD_UNMASK_PROMPT_INSTRUCTIONS_LOCAL_CARD
#define IDS_AUTOFILL_CARD_UNMASK_PROMPT_INSTRUCTIONS_V2
#define IDS_AUTOFILL_CARD_UNMASK_CVC_IMAGE_DESCRIPTION
#define IDS_AUTOFILL_CARD_UNMASK_PROMPT_STORAGE_CHECKBOX
#define IDS_AUTOFILL_CARD_UNMASK_CONFIRM_BUTTON
#define IDS_AUTOFILL_CARD_UNMASK_VERIFY_BUTTON
#define IDS_AUTOFILL_CARD_UNMASK_EXPIRATION_MONTH
#define IDS_AUTOFILL_CARD_UNMASK_EXPIRATION_YEAR
#define IDS_AUTOFILL_CARD_UNMASK_VERIFICATION_IN_PROGRESS
#define IDS_AUTOFILL_CARD_UNMASK_VERIFICATION_SUCCESS
#define IDS_AUTOFILL_CARD_UNMASK_INVALID_EXPIRATION_DATE
#define IDS_AUTOFILL_EXPIRATION_DATE_SEPARATOR
#define IDS_AUTOFILL_CARD_UNMASK_NEW_CARD_LINK
#define IDS_AUTOFILL_DIALOG_PLACEHOLDER_CVC
#define IDS_AUTOFILL_WEBAUTHN_OPT_IN_DIALOG_TITLE
#define IDS_AUTOFILL_WEBAUTHN_OPT_IN_DIALOG_TITLE_ERROR
#define IDS_AUTOFILL_WEBAUTHN_OPT_IN_DIALOG_INSTRUCTION
#define IDS_AUTOFILL_WEBAUTHN_OPT_IN_DIALOG_OK_BUTTON_LABEL
#define IDS_AUTOFILL_WEBAUTHN_OPT_IN_DIALOG_INSTRUCTION_ERROR
#define IDS_AUTOFILL_WEBAUTHN_OPT_IN_DIALOG_CANCEL_BUTTON_LABEL
#define IDS_AUTOFILL_WEBAUTHN_OPT_IN_DIALOG_CANCEL_BUTTON_LABEL_ERROR
#define IDS_AUTOFILL_WEBAUTHN_VERIFY_PENDING_DIALOG_TITLE
#define IDS_AUTOFILL_WEBAUTHN_VERIFY_PENDING_DIALOG_CANCEL_BUTTON_LABEL
#define IDS_AUTOFILL_WALLET_MANAGEMENT_LINK_TEXT
#define IDS_AUTOFILL_FROM_GOOGLE_ACCOUNT_LONG
#define IDS_AUTOFILL_CLEAR_FORM_MENU_ITEM
#define IDS_AUTOFILL_WARNING_INSECURE_CONNECTION
#define IDS_AUTOFILL_CREDIT_CARD_SIGNIN_PROMO
#define IDS_AUTOFILL_DELETE_AUTOCOMPLETE_SUGGESTION_CONFIRMATION_BODY
#define IDS_AUTOFILL_DELETE_CREDIT_CARD_SUGGESTION_CONFIRMATION_BODY
#define IDS_AUTOFILL_DELETE_PROFILE_SUGGESTION_CONFIRMATION_BODY
#define IDS_AUTOFILL_CC_AMEX
#define IDS_AUTOFILL_CC_AMEX_SHORT
#define IDS_AUTOFILL_CC_DINERS
#define IDS_AUTOFILL_CC_DISCOVER
#define IDS_AUTOFILL_CC_ELO
#define IDS_AUTOFILL_CC_GOOGLE_PAY
#define IDS_AUTOFILL_CC_JCB
#define IDS_AUTOFILL_CC_MASTERCARD
#define IDS_AUTOFILL_CC_MIR
#define IDS_AUTOFILL_CC_UNION_PAY
#define IDS_AUTOFILL_CC_VISA
#define IDS_AUTOFILL_CC_GENERIC
#define IDS_AUTOFILL_ADDRESS_SUMMARY_SEPARATOR
#define IDS_AUTOFILL_FIELD_LABEL_STATE
#define IDS_AUTOFILL_FIELD_LABEL_AREA
#define IDS_AUTOFILL_FIELD_LABEL_COUNTY
#define IDS_AUTOFILL_FIELD_LABEL_DEPARTMENT
#define IDS_AUTOFILL_FIELD_LABEL_DISTRICT
#define IDS_AUTOFILL_FIELD_LABEL_EMIRATE
#define IDS_AUTOFILL_FIELD_LABEL_ISLAND
#define IDS_AUTOFILL_FIELD_LABEL_PARISH
#define IDS_AUTOFILL_FIELD_LABEL_PREFECTURE
#define IDS_AUTOFILL_FIELD_LABEL_PROVINCE
#define IDS_AUTOFILL_FIELD_LABEL_ZIP_CODE
#define IDS_AUTOFILL_FIELD_LABEL_POSTAL_CODE
#define IDS_AUTOFILL_HIDE_SUGGESTIONS
#define IDS_AUTOFILL_MANAGE
#define IDS_AUTOFILL_MANAGE_ADDRESSES
#define IDS_AUTOFILL_MANAGE_PAYMENT_METHODS
#define IDS_AUTOFILL_MANAGE_PASSWORDS
#define IDS_AUTOFILL_SCAN_CREDIT_CARD
#define IDS_AUTOFILL_SHOW_ALL_SAVED_FALLBACK
#define IDS_AUTOFILL_SHOW_ACCOUNT_CARDS
#define IDS_AUTOFILL_POPUP_ACCESSIBLE_NODE_DATA
#define IDS_AUTOFILL_SUGGESTION_LABEL_SEPARATOR
#define IDS_AUTOFILL_CREDIT_CARD_EXPIRATION_DATE_ABBR
#define IDS_AUTOFILL_CREDIT_CARD_EXPIRATION_DATE_ABBR_V2
#define IDS_AUTOFILL_CREDIT_CARD_TWO_LINE_LABEL_FROM_NAME
#define IDS_AUTOFILL_CREDIT_CARD_TWO_LINE_LABEL_FROM_CARD_NUMBER
#define IDS_AUTOFILL_LOADING_REGIONS
#define IDS_AUTOFILL_SELECT
#define IDS_AUTOFILL_NO_SAVED_ADDRESS
#define IDS_AUTOFILL_ADDRESSES
#define IDS_AUTOFILL_ENABLE_PROFILES_TOGGLE_SUBLABEL
#define IDS_AUTOFILL_ENABLE_CREDIT_CARDS_TOGGLE_SUBLABEL
#define IDS_AUTOFILL_ADDRESSES_SETTINGS_TITLE
#define IDS_AUTOFILL_PAYMENT_METHODS
#define IDS_AUTOFILL_ENABLE_PROFILES_TOGGLE_LABEL
#define IDS_AUTOFILL_ENABLE_CREDIT_CARDS_TOGGLE_LABEL
#define IDS_ENABLE_CREDIT_CARD_FIDO_AUTH_LABEL
#define IDS_ENABLE_CREDIT_CARD_FIDO_AUTH_SUBLABEL
#define IDS_AUTOFILL_ENABLE_PAYMENTS_INTEGRATION_CHECKBOX_LABEL
#define IDS_BOOKMARK_BAR_FOLDER_NAME
#define IDS_BOOKMARK_BAR_MOBILE_FOLDER_NAME
#define IDS_BOOKMARK_BAR_OTHER_FOLDER_NAME
#define IDS_BOOKMARK_BAR_MANAGED_FOLDER_DOMAIN_NAME
#define IDS_BOOKMARK_BAR_MANAGED_FOLDER_DEFAULT_NAME
#define IDS_BOOKMARK_EDITOR_TITLE
#define IDS_BOOKMARK_EDITOR_NEW_FOLDER_NAME
#define IDS_BOOKMARK_BUBBLE_REMOVE_BOOKMARK
#define IDS_BOOKMARK_MANAGER_NAME_INPUT_PLACE_HOLDER
#define IDS_BOOKMARK_MANAGER_URL_INPUT_PLACE_HOLDER
#define IDS_TOOLTIP_STAR
#define IDS_CLEAR_BROWSING_DATA_CALCULATING
#define IDS_DEL_BROWSING_HISTORY_COUNTER
#define IDS_DEL_BROWSING_HISTORY_COUNTER_SYNCED
#define IDS_DEL_CACHE_COUNTER_UPPER_ESTIMATE
#define IDS_DEL_CACHE_COUNTER_ALMOST_EMPTY
#define IDS_DEL_CACHE_COUNTER_BASIC
#define IDS_DEL_CACHE_COUNTER_UPPER_ESTIMATE_BASIC
#define IDS_DEL_CACHE_COUNTER_ALMOST_EMPTY_BASIC
#define IDS_DEL_PASSWORDS_COUNTER
#define IDS_DEL_PASSWORDS_COUNTER_SYNCED
#define IDS_DEL_PASSWORDS_DOMAINS_DISPLAY
#define IDS_DEL_PASSWORDS_COUNTER_AND_X_MORE
#define IDS_DEL_SIGNIN_DATA_COUNTER
#define IDS_DEL_PASSWORDS_AND_SIGNIN_DATA_COUNTER_NONE
#define IDS_DEL_PASSWORDS_AND_SIGNIN_DATA_COUNTER_COMBINATION
#define IDS_DEL_SITE_SETTINGS_COUNTER
#define IDS_DEL_AUTOFILL_COUNTER_EMPTY
#define IDS_DEL_AUTOFILL_COUNTER_CREDIT_CARDS
#define IDS_DEL_AUTOFILL_COUNTER_ADDRESSES
#define IDS_DEL_AUTOFILL_COUNTER_SUGGESTIONS
#define IDS_DEL_AUTOFILL_COUNTER_SUGGESTIONS_LONG
#define IDS_DEL_AUTOFILL_COUNTER_SUGGESTIONS_SHORT
#define IDS_DEL_AUTOFILL_COUNTER_ONE_TYPE_SYNCED
#define IDS_DEL_AUTOFILL_COUNTER_TWO_TYPES
#define IDS_DEL_AUTOFILL_COUNTER_TWO_TYPES_SYNCED
#define IDS_DEL_AUTOFILL_COUNTER_THREE_TYPES
#define IDS_DEL_AUTOFILL_COUNTER_THREE_TYPES_SYNCED
#define IDS_DEL_COOKIES_COUNTER
#define IDS_DEL_COOKIES_COUNTER_ADVANCED
#define IDS_DEL_COOKIES_COUNTER_ADVANCED_WITH_EXCEPTION
#define IDS_DEL_DOWNLOADS_COUNTER
#define IDS_DEL_HOSTED_APPS_COUNTER
#define IDS_DEL_HOSTED_APPS_COUNTER_AND_X_MORE
#define IDS_SETTINGS_TITLE
#define IDS_SETTINGS_HIDE_ADVANCED_SETTINGS
#define IDS_SETTINGS_SHOW_ADVANCED_SETTINGS
#define IDS_NETWORK_PREDICTION_ENABLED_DESCRIPTION
#define IDS_OPTIONS_PROXIES_CONFIGURE_BUTTON
#define IDS_CRASH_TITLE
#define IDS_CRASH_CRASH_COUNT_BANNER_FORMAT
#define IDS_CRASH_CRASH_LG_HEADER_FORMAT
#define IDS_CRASH_CRASH_LG_HEADER_FORMAT_LOCAL_ONLY
#define IDS_CRASH_UPLOAD_TIME_FORMAT
#define IDS_CRASH_CAPTURE_AND_UPLOAD_TIME_FORMAT
#define IDS_CRASH_CRASH_NOT_UPLOADED
#define IDS_CRASH_CRASH_PENDING
#define IDS_CRASH_CRASH_USER_REQUESTED
#define IDS_CRASH_BUG_LINK_LABEL
#define IDS_CRASH_NO_CRASHES_MESSAGE
#define IDS_CRASH_DISABLED_HEADER
#define IDS_CRASH_UPLOAD_MESSAGE
#define IDS_CRASH_UPLOAD_NOW_LINK_TEXT
#define IDS_CRASH_SIZE_MESSAGE
#define IDS_HTTP_POST_WARNING_TITLE
#define IDS_HTTP_POST_WARNING
#define IDS_HTTP_POST_WARNING_RESEND
#define IDS_DOM_DISTILLER_JAVASCRIPT_DISABLED_CONTENT
#define IDS_DOM_DISTILLER_WEBUI_ENTRY_URL
#define IDS_DOM_DISTILLER_WEBUI_ENTRY_ADD
#define IDS_DOM_DISTILLER_WEBUI_ENTRY_ADD_FAILED
#define IDS_DOM_DISTILLER_WEBUI_VIEW_URL
#define IDS_DOM_DISTILLER_WEBUI_VIEW_URL_FAILED
#define IDS_DOM_DISTILLER_WEBUI_REFRESH
#define IDS_DOM_DISTILLER_WEBUI_FETCHING_ENTRIES
#define IDS_DOM_DISTILLER_VIEWER_FAILED_TO_FIND_ARTICLE_TITLE
#define IDS_DOM_DISTILLER_VIEWER_FAILED_TO_FIND_ARTICLE_CONTENT
#define IDS_DOM_DISTILLER_VIEWER_LOADING_TITLE
#define IDS_DOM_DISTILLER_VIEWER_NO_DATA_CONTENT
#define IDS_DOM_DISTILLER_QUALITY_QUESTION
#define IDS_DOM_DISTILLER_QUALITY_ANSWER_YES
#define IDS_DOM_DISTILLER_QUALITY_ANSWER_NO
#define IDS_DOM_DISTILLER_WEBUI_TITLE
#define IDS_ERRORPAGE_NET_BUTTON_DETAILS
#define IDS_ERRORPAGE_NET_BUTTON_HIDE_DETAILS
#define IDS_ERRORPAGES_BUTTON_RELOAD
#define IDS_ERRORPAGES_BUTTON_SHOW_SAVED_COPY
#define IDS_ERRORPAGE_FUN_DISABLED
#define IDS_ERRORPAGES_SUGGESTION_VISIT_GOOGLE_CACHE
#define IDS_ERRORPAGES_SUGGESTION_CORRECTED_URL
#define IDS_ERRORPAGES_SUGGESTION_ALTERNATE_URL
#define IDS_ERRORPAGES_SUGGESTION_RELOAD_REPOST_SUMMARY
#define IDS_ERRORPAGES_SUGGESTION_CHECK_CONNECTION_HEADER
#define IDS_ERRORPAGES_SUGGESTION_CHECK_CONNECTION_BODY
#define IDS_ERRORPAGES_SUGGESTION_DNS_CONFIG_HEADER
#define IDS_ERRORPAGES_SUGGESTION_DNS_CONFIG_BODY
#define IDS_ERRORPAGES_SUGGESTION_NETWORK_PREDICTION_HEADER
#define IDS_ERRORPAGES_SUGGESTION_FIREWALL_CONFIG_BODY
#define IDS_ERRORPAGES_SUGGESTION_PROXY_CONFIG_HEADER
#define IDS_ERRORPAGES_SUGGESTION_PROXY_CONFIG_BODY
#define IDS_ERRORPAGES_SUGGESTION_VIEW_POLICIES_HEADER
#define IDS_ERRORPAGES_SUGGESTION_VIEW_POLICIES_BODY
#define IDS_ERRORPAGES_SUGGESTION_UNSUPPORTED_CIPHER_HEADER
#define IDS_ERRORPAGES_SUGGESTION_UNSUPPORTED_CIPHER_BODY
#define IDS_ERRORPAGES_SUGGESTION_NAVIGATE_TO_ORIGIN
#define IDS_ERRORPAGES_HEADING_NOT_AVAILABLE
#define IDS_ERRORPAGES_HEADING_NETWORK_ACCESS_DENIED
#define IDS_ERRORPAGES_HEADING_INTERNET_DISCONNECTED
#define IDS_ERRORPAGES_HEADING_CACHE_READ_FAILURE
#define IDS_ERRORPAGES_HEADING_CONNECTION_INTERRUPTED
#define IDS_ERRORPAGES_HEADING_NOT_FOUND
#define IDS_ERRORPAGES_HEADING_FILE_NOT_FOUND
#define IDS_ERRORPAGES_HEADING_BLOCKED
#define IDS_ERRORPAGES_SUMMARY_NOT_AVAILABLE
#define IDS_ERRORPAGES_SUMMARY_TIMED_OUT
#define IDS_ERRORPAGES_SUMMARY_CONNECTION_RESET
#define IDS_ERRORPAGES_SUMMARY_CONNECTION_CLOSED
#define IDS_ERRORPAGES_SUMMARY_CONNECTION_FAILED
#define IDS_ERRORPAGES_SUMMARY_NETWORK_CHANGED
#define IDS_ERRORPAGES_SUMMARY_CONNECTION_REFUSED
#define IDS_ERRORPAGES_SUMMARY_NAME_NOT_RESOLVED
#define IDS_ERRORPAGES_SUMMARY_ICANN_NAME_COLLISION
#define IDS_ERRORPAGES_SUMMARY_ADDRESS_UNREACHABLE
#define IDS_ERRORPAGES_SUMMARY_FILE_ACCESS_DENIED
#define IDS_ERRORPAGES_SUMMARY_NETWORK_ACCESS_DENIED
#define IDS_ERRORPAGES_SUMMARY_PROXY_CONNECTION_FAILED
#define IDS_ERRORPAGES_SUMMARY_CACHE_READ_FAILURE
#define IDS_ERRORPAGES_SUMMARY_NETWORK_IO_SUSPENDED
#define IDS_ERRORPAGES_SUMMARY_NOT_FOUND
#define IDS_ERRORPAGES_SUMMARY_FILE_NOT_FOUND
#define IDS_ERRORPAGES_SUMMARY_TOO_MANY_REDIRECTS
#define IDS_ERRORPAGES_SUMMARY_EMPTY_RESPONSE
#define IDS_ERRORPAGES_SUMMARY_INVALID_RESPONSE
#define IDS_ERRORPAGES_SUMMARY_DNS_PROBE_RUNNING
#define IDS_ERRORPAGES_HEADING_ACCESS_DENIED
#define IDS_ERRORPAGES_HEADING_FILE_ACCESS_DENIED
#define IDS_ERRORPAGES_SUMMARY_FORBIDDEN
#define IDS_ERRORPAGES_SUMMARY_GONE
#define IDS_ERRORPAGES_HEADING_PAGE_NOT_WORKING
#define IDS_ERRORPAGES_SUMMARY_CONTACT_SITE_OWNER
#define IDS_ERRORPAGES_SUMMARY_WEBSITE_CANNOT_HANDLE_REQUEST
#define IDS_ERRORPAGES_SUMMARY_GATEWAY_TIMEOUT
#define IDS_ERRORPAGES_SUMMARY_SSL_SECURITY_ERROR
#define IDS_ERRORPAGES_SUMMARY_SSL_VERSION_OR_CIPHER_MISMATCH
#define IDS_ERRORPAGES_HEADING_INSECURE_CONNECTION
#define IDS_ERRORPAGES_SUMMARY_BAD_SSL_CLIENT_AUTH_CERT
#define IDS_ERRORPAGES_SUMMARY_BLOCKED_BY_EXTENSION
#define IDS_ERRORPAGES_SUMMARY_BLOCKED_BY_ADMINISTRATOR
#define IDS_ERRORPAGES_HTTP_POST_WARNING
#define IDS_ERRORPAGES_SUGGESTION_LIST_HEADER
#define IDS_ERRORPAGES_SUGGESTION_CHECK_CONNECTION_SUMMARY
#define IDS_ERRORPAGES_SUGGESTION_CHECK_PROXY_FIREWALL_DNS_SUMMARY
#define IDS_ERRORPAGES_SUGGESTION_CHECK_FIREWALL_ANTIVIRUS_SUMMARY
#define IDS_ERRORPAGES_SUGGESTION_CHECK_PROXY_FIREWALL_SUMMARY
#define IDS_ERRORPAGES_SUGGESTION_CHECK_PROXY_ADDRESS_SUMMARY
#define IDS_ERRORPAGES_SUGGESTION_CONTACT_ADMIN_SUMMARY
#define IDS_ERRORPAGES_SUGGESTION_CONTACT_ADMIN_SUMMARY_STANDALONE
#define IDS_ERRORPAGES_SUGGESTION_LEARNMORE_SUMMARY
#define IDS_ERRORPAGES_SUGGESTION_LEARNMORE_SUMMARY_STANDALONE
#define IDS_ERRORPAGES_SUGGESTION_CLEAR_COOKIES_SUMMARY
#define IDS_ERRORPAGES_SUGGESTION_CHECK_HARDWARE_SUMMARY
#define IDS_ERRORPAGES_SUGGESTION_CHECK_WIFI_SUMMARY
#define IDS_ERRORPAGES_SUGGESTION_DIAGNOSE_CONNECTION_SUMMARY
#define IDS_ERRORPAGES_SUGGESTION_COMPLETE_SETUP_SUMMARY
#define IDS_ERRORPAGES_SUGGESTION_DISABLE_EXTENSION_SUMMARY
#define IDS_ERRORPAGES_SUGGESTION_GOOGLE_SEARCH_SUMMARY
#define IDS_ERRORPAGES_SUGGESTION_DIAGNOSE
#define IDS_ERRORPAGES_SUGGESTION_DIAGNOSE_STANDALONE
#define IDS_FIND_IN_PAGE_ACCESSIBLE_TITLE
#define IDS_FIND_IN_PAGE_COUNT
#define IDS_ACCESSIBLE_FIND_IN_PAGE_COUNT
#define IDS_ACCESSIBLE_FIND_IN_PAGE_NO_RESULTS
#define IDS_FIND_IN_PAGE_PREVIOUS_TOOLTIP
#define IDS_FIND_IN_PAGE_NEXT_TOOLTIP
#define IDS_FIND_IN_PAGE_CLOSE_TOOLTIP
#define IDS_FLAGS_UI_SEARCH_PLACEHOLDER
#define IDS_FLAGS_UI_TITLE
#define IDS_FLAGS_UI_PAGE_RESET
#define IDS_FLAGS_UI_PAGE_WARNING
#define IDS_FLAGS_UI_PAGE_WARNING_EXPLANATION
#define IDS_FLAGS_UI_OWNER_WARNING
#define IDS_FLAGS_UI_AVAILABLE_FEATURE
#define IDS_FLAGS_UI_UNAVAILABLE_FEATURE
#define IDS_FLAGS_UI_ENABLED_FEATURE
#define IDS_FLAGS_UI_DISABLED_FEATURE
#define IDS_FLAGS_UI_NO_RESULTS
#define IDS_FLAGS_UI_NOT_AVAILABLE_ON_PLATFORM
#define IDS_FLAGS_UI_RELAUNCH
#define IDS_FLAGS_UI_CLEAR_SEARCH
#define IDS_FLAGS_UI_RESET_ACKNOWLEDGED
#define IDS_FLAGS_UI_EXPERIMENT_ENABLED
#define IDS_FLAGS_UI_SEARCH_RESULTS_SINGULAR
#define IDS_FLAGS_UI_SEARCH_RESULTS_PLURAL
#define IDS_DEPRECATED_FEATURES_PAGE_RESET
#define IDS_DEPRECATED_FEATURES_OWNER_WARNING
#define IDS_DEPRECATED_FEATURES_AVAILABLE_FEATURE
#define IDS_DEPRECATED_FEATURES_UNAVAILABLE_FEATURE
#define IDS_DEPRECATED_FEATURES_ENABLED_FEATURE
#define IDS_DEPRECATED_FEATURES_DISABLED_FEATURE
#define IDS_DEPRECATED_FEATURES_NOT_AVAILABLE_ON_PLATFORM
#define IDS_DEPRECATED_FEATURES_RELAUNCH
#define IDS_DEPRECATED_FEATURES_SEARCH_PLACEHOLDER
#define IDS_DEPRECATED_FEATURES_TITLE
#define IDS_DEPRECATED_FEATURES_HEADING
#define IDS_DEPRECATED_FEATURES_PAGE_WARNING_EXPLANATION
#define IDS_DEPRECATED_FEATURES_NO_RESULTS
#define IDS_DEPRECATED_UI_CLEAR_SEARCH
#define IDS_DEPRECATED_UI_RESET_ACKNOWLEDGED
#define IDS_DEPRECATED_UI_EXPERIMENT_ENABLED
#define IDS_ENTERPRISE_UI_SEARCH_RESULTS_SINGULAR
#define IDS_ENTERPRISE_UI_SEARCH_RESULTS_PLURAL
#define IDS_HISTORY_ACTION_MENU_DESCRIPTION
#define IDS_HISTORY_ARIA_ROLE_DESCRIPTION
#define IDS_HISTORY_CANCEL_EDITING_BUTTON
#define IDS_HISTORY_DATE_WITH_RELATIVE_TIME
#define IDS_HISTORY_DELETE_PRIOR_VISITS_CONFIRM_BUTTON
#define IDS_HISTORY_DELETE_PRIOR_VISITS_WARNING
#define IDS_HISTORY_DELETE_SELECTED_ENTRIES_BUTTON
#define IDS_HISTORY_ENTRY_ACCESSIBILITY_DELETE
#define IDS_HISTORY_ENTRY_ACCESSIBILITY_LABEL
#define IDS_HISTORY_ENTRY_BOOKMARKED
#define IDS_HISTORY_ENTRY_SUMMARY
#define IDS_HISTORY_FOUND_SEARCH_RESULTS
#define IDS_HISTORY_OTHER_FORMS_OF_HISTORY
#define IDS_HISTORY_LOADING
#define IDS_HISTORY_MORE_FROM_SITE
#define IDS_HISTORY_NO_RESULTS
#define IDS_HISTORY_NO_SEARCH_RESULTS
#define IDS_HISTORY_OPEN_CLEAR_BROWSING_DATA_DIALOG
#define IDS_HISTORY_OTHER_SESSIONS_COLLAPSE_SESSION
#define IDS_HISTORY_OTHER_SESSIONS_EXPAND_SESSION
#define IDS_HISTORY_OTHER_SESSIONS_HIDE_FOR_NOW
#define IDS_HISTORY_OTHER_SESSIONS_OPEN_ALL
#define IDS_HISTORY_REMOVE_BOOKMARK
#define IDS_HISTORY_REMOVE_PAGE
#define IDS_HISTORY_REMOVE_SELECTED_ITEMS
#define IDS_HISTORY_SEARCH_BUTTON
#define IDS_HISTORY_SEARCH_RESULT
#define IDS_HISTORY_SEARCH_RESULTS
#define IDS_HISTORY_SHOW_HISTORY
#define IDS_HISTORY_SHOWFULLHISTORY_LINK
#define IDS_HISTORY_START_EDITING_BUTTON
#define IDS_HISTORY_TITLE
#define IDS_HISTORY_UNKNOWN_DEVICE
#define IDS_LOGIN_DIALOG_TITLE
#define IDS_LOGIN_DIALOG_OK_BUTTON_LABEL
#define IDS_LOGIN_DIALOG_AUTHORITY
#define IDS_LOGIN_DIALOG_PROXY_AUTHORITY
#define IDS_LOGIN_DIALOG_NOT_PRIVATE
#define IDS_LOGIN_DIALOG_USERNAME_FIELD
#define IDS_LOGIN_DIALOG_PASSWORD_FIELD
#define IDS_MEDIA_MESSAGE_CENTER_MEDIA_NOTIFICATION_ACTION_PREVIOUS_TRACK
#define IDS_MEDIA_MESSAGE_CENTER_MEDIA_NOTIFICATION_ACTION_SEEK_BACKWARD
#define IDS_MEDIA_MESSAGE_CENTER_MEDIA_NOTIFICATION_ACTION_PLAY
#define IDS_MEDIA_MESSAGE_CENTER_MEDIA_NOTIFICATION_ACTION_PAUSE
#define IDS_MEDIA_MESSAGE_CENTER_MEDIA_NOTIFICATION_ACTION_SEEK_FORWARD
#define IDS_MEDIA_MESSAGE_CENTER_MEDIA_NOTIFICATION_ACTION_NEXT_TRACK
#define IDS_MEDIA_MESSAGE_CENTER_MEDIA_NOTIFICATION_ACCESSIBLE_NAME
#define IDS_DEFAULT_TAB_TITLE
#define IDS_DOWNLOAD_TAB_TITLE
#define IDS_SAD_TAB_TITLE
#define IDS_SAD_TAB_MESSAGE
#define IDS_SAD_TAB_HELP_MESSAGE
#define IDS_SAD_TAB_HELP_LINK
#define IDS_SAD_TAB_RELOAD_LABEL
#define IDS_SAD_TAB_OOM_TITLE
#define IDS_SAD_TAB_RELOAD_TITLE
#define IDS_SAD_TAB_OOM_MESSAGE_TABS
#define IDS_SAD_TAB_OOM_MESSAGE_NOTABS
#define IDS_SAD_TAB_RELOAD_TRY
#define IDS_SAD_TAB_RELOAD_INCOGNITO
#define IDS_SAD_TAB_RELOAD_RESTART_BROWSER
#define IDS_SAD_TAB_RELOAD_RESTART_DEVICE
#define IDS_NEW_TAB_TITLE
#define IDS_NEW_TAB_OTR_HEADING
#define IDS_NEW_TAB_OTR_DESCRIPTION
#define IDS_NEW_TAB_OTR_LEARN_MORE_LINK
#define IDS_NEW_TAB_OTR_MESSAGE_WARNING
#define IDS_NEW_TAB_UNDO_THUMBNAIL_REMOVE
#define IDS_NEW_TAB_OTR_TITLE
#define IDS_NEW_TAB_OTR_SUBTITLE
#define IDS_NEW_TAB_OTR_NOT_SAVED
#define IDS_NEW_TAB_OTR_VISIBLE
#define IDS_NEW_TAB_OTR_COOKIE_CONTROLS_CONTROLLED_TOOLTIP_TEXT
#define IDS_NTP_ARTICLE_SUGGESTIONS_NOT_AVAILABLE
#define IDS_NTP_ARTICLE_SUGGESTIONS_SECTION_HEADER
#define IDS_NTP_ARTICLE_SUGGESTIONS_SECTION_LG_HEADER_BRANDED
#define IDS_NTP_SUGGESTIONS_SECTION_HEADER
#define IDS_NTP_ARTICLE_SUGGESTIONS_SECTION_EMPTY
#define IDS_NTP_PHYSICAL_WEB_PAGE_SUGGESTIONS_SECTION_HEADER
#define IDS_NTP_PHYSICAL_WEB_PAGE_SUGGESTIONS_SECTION_EMPTY
#define IDS_NTP_READING_LIST_SUGGESTIONS_SECTION_HEADER
#define IDS_NTP_READING_LIST_SUGGESTIONS_SECTION_EMPTY
#define IDS_NTP_RECENT_TAB_SUGGESTIONS_SECTION_HEADER
#define IDS_NTP_RECENT_TAB_SUGGESTIONS_SECTION_EMPTY
#define IDS_NTP_NOTIFICATIONS_READ_THIS_STORY_AND_MORE
#define IDS_AUTOCOMPLETE_SEARCH_DESCRIPTION
#define IDS_EMPTY_KEYWORD_VALUE
#define IDS_LINK_FROM_CLIPBOARD
#define IDS_TEXT_FROM_CLIPBOARD
#define IDS_IMAGE_FROM_CLIPBOARD
#define IDS_COPIED_TEXT_FROM_CLIPBOARD
#define IDS_SECURE_CONNECTION_EV
#define IDS_SECURE_VERBOSE_STATE
#define IDS_NOT_SECURE_VERBOSE_STATE
#define IDS_DANGEROUS_VERBOSE_STATE
#define IDS_OFFLINE_VERBOSE_STATE
#define IDS_OMNIBOX_TAB_SUGGEST_HINT
#define IDS_OMNIBOX_TAB_SUGGEST_SHORT_HINT
#define IDS_PHYSICAL_WEB_OVERFLOW_DESCRIPTION
#define IDS_PHYSICAL_WEB_OVERFLOW
#define IDS_PHYSICAL_WEB_OVERFLOW_EMPTY_TITLE
#define IDS_OMNIBOX_FILE
#define IDS_DRIVE_SUGGESTION_DOCUMENT
#define IDS_DRIVE_SUGGESTION_FORM
#define IDS_DRIVE_SUGGESTION_SPREADSHEET
#define IDS_DRIVE_SUGGESTION_PRESENTATION
#define IDS_DRIVE_SUGGESTION_GENERAL
#define IDS_DRIVE_SUGGESTION_DESCRIPTION_TEMPLATE
#define IDS_OMNIBOX_PEDAL_CLEAR_BROWSING_DATA_HINT
#define IDS_OMNIBOX_PEDAL_CLEAR_BROWSING_DATA_HINT_SHORT
#define IDS_OMNIBOX_PEDAL_CLEAR_BROWSING_DATA_SUGGESTION_CONTENTS
#define IDS_OMNIBOX_PEDAL_CHANGE_SEARCH_ENGINE_HINT
#define IDS_OMNIBOX_PEDAL_CHANGE_SEARCH_ENGINE_HINT_SHORT
#define IDS_OMNIBOX_PEDAL_CHANGE_SEARCH_ENGINE_SUGGESTION_CONTENTS
#define IDS_OMNIBOX_PEDAL_MANAGE_PASSWORDS_HINT
#define IDS_OMNIBOX_PEDAL_MANAGE_PASSWORDS_HINT_SHORT
#define IDS_OMNIBOX_PEDAL_MANAGE_PASSWORDS_SUGGESTION_CONTENTS
#define IDS_OMNIBOX_PEDAL_CHANGE_HOME_PAGE_HINT
#define IDS_OMNIBOX_PEDAL_CHANGE_HOME_PAGE_HINT_SHORT
#define IDS_OMNIBOX_PEDAL_CHANGE_HOME_PAGE_SUGGESTION_CONTENTS
#define IDS_OMNIBOX_PEDAL_UPDATE_CREDIT_CARD_HINT
#define IDS_OMNIBOX_PEDAL_UPDATE_CREDIT_CARD_HINT_SHORT
#define IDS_OMNIBOX_PEDAL_UPDATE_CREDIT_CARD_SUGGESTION_CONTENTS
#define IDS_OMNIBOX_PEDAL_LAUNCH_INCOGNITO_HINT
#define IDS_OMNIBOX_PEDAL_LAUNCH_INCOGNITO_HINT_SHORT
#define IDS_OMNIBOX_PEDAL_LAUNCH_INCOGNITO_SUGGESTION_CONTENTS
#define IDS_OMNIBOX_PEDAL_TRANSLATE_HINT
#define IDS_OMNIBOX_PEDAL_TRANSLATE_HINT_SHORT
#define IDS_OMNIBOX_PEDAL_TRANSLATE_SUGGESTION_CONTENTS
#define IDS_OMNIBOX_PEDAL_UPDATE_CHROME_HINT
#define IDS_OMNIBOX_PEDAL_UPDATE_CHROME_HINT_SHORT
#define IDS_OMNIBOX_PEDAL_UPDATE_CHROME_SUGGESTION_CONTENTS
#define IDS_ACC_AUTOCOMPLETE_HISTORY
#define IDS_ACC_AUTOCOMPLETE_SEARCH_HISTORY
#define IDS_ACC_AUTOCOMPLETE_SEARCH
#define IDS_ACC_AUTOCOMPLETE_SUGGESTED_SEARCH
#define IDS_ACC_AUTOCOMPLETE_SUGGESTED_SEARCH_ENTITY
#define IDS_ACC_AUTOCOMPLETE_QUICK_ANSWER
#define IDS_ACC_AUTOCOMPLETE_BOOKMARK
#define IDS_ACC_AUTOCOMPLETE_CLIPBOARD_IMAGE
#define IDS_ACC_AUTOCOMPLETE_CLIPBOARD_TEXT
#define IDS_ACC_AUTOCOMPLETE_CLIPBOARD_URL
#define IDS_ACC_SEARCH_ICON
#define IDS_ACC_AUTOCOMPLETE_N_OF_M
#define IDS_ACC_TAB_SWITCH_SUFFIX
#define IDS_ACC_TAB_SWITCH_BUTTON_FOCUSED_PREFIX
#define IDS_ACC_TAB_SWITCH_BUTTON
#define IDS_PAGE_INFO_SECURE_SUMMARY
#define IDS_PAGE_INFO_MIXED_CONTENT_SUMMARY
#define IDS_PAGE_INFO_NOT_SECURE_SUMMARY
#define IDS_PAGE_INFO_MALWARE_SUMMARY
#define IDS_PAGE_INFO_SOCIAL_ENGINEERING_SUMMARY
#define IDS_PAGE_INFO_UNWANTED_SOFTWARE_SUMMARY
#define IDS_PAGE_INFO_EXTENSION_PAGE
#define IDS_PAGE_INFO_VIEW_SOURCE_PAGE
#define IDS_PAGE_INFO_DEVTOOLS_PAGE
#define IDS_PAGE_INFO_SAFETY_TIP_BAD_REPUTATION_TITLE
#define IDS_PAGE_INFO_SAFETY_TIP_BAD_REPUTATION_DESCRIPTION
#define IDS_PAGE_INFO_SAFETY_TIP_MORE_INFO_LINK
#define IDS_PAGE_INFO_SAFETY_TIP_LEAVE_BUTTON
#define IDS_PAGE_INFO_SAFETY_TIP_LOOKALIKE_TITLE
#define IDS_PAGE_INFO_SAFETY_TIP_LOOKALIKE_DESCRIPTION
#define IDS_PAGE_INFO_FILE_PAGE
#define IDS_PAGE_INFO_SECURE_DETAILS
#define IDS_PAGE_INFO_MIXED_CONTENT_DETAILS
#define IDS_PAGE_INFO_LEGACY_TLS_DETAILS
#define IDS_PAGE_INFO_NOT_SECURE_DETAILS
#define IDS_PAGE_INFO_MALWARE_DETAILS
#define IDS_PAGE_INFO_SOCIAL_ENGINEERING_DETAILS
#define IDS_PAGE_INFO_UNWANTED_SOFTWARE_DETAILS
#define IDS_PAGE_INFO_SECURITY_TAB_INSECURE_IDENTITY
#define IDS_PAGE_INFO_INVALID_CERTIFICATE_DESCRIPTION
#define IDS_PAGE_INFO_RESET_INVALID_CERTIFICATE_DECISIONS_BUTTON
#define IDS_PAGE_INFO_HELP_CENTER_LINK
#define IDS_PAGE_INFO_SECURITY_TAB_DEPRECATED_SIGNATURE_ALGORITHM
#define IDS_PAGE_INFO_SECURITY_TAB_ENCRYPTED_CONNECTION_TEXT
#define IDS_PAGE_INFO_SECURITY_TAB_ENCRYPTED_INSECURE_CONTENT_ERROR
#define IDS_PAGE_INFO_SECURITY_TAB_ENCRYPTED_INSECURE_CONTENT_WARNING
#define IDS_PAGE_INFO_SECURITY_TAB_ENCRYPTED_INSECURE_FORM_WARNING
#define IDS_PAGE_INFO_SECURITY_TAB_ENCRYPTED_SENTENCE_LINK
#define IDS_PAGE_INFO_SECURITY_TAB_ENCRYPTION_DETAILS
#define IDS_PAGE_INFO_SECURITY_TAB_ENCRYPTION_DETAILS_AEAD
#define IDS_PAGE_INFO_SECURITY_TAB_NON_UNIQUE_NAME
#define IDS_PAGE_INFO_SECURITY_TAB_NOT_ENCRYPTED_CONNECTION_TEXT
#define IDS_PAGE_INFO_SECURITY_TAB_SSL_VERSION
#define IDS_PAGE_INFO_SECURITY_TAB_UNKNOWN_PARTY
#define IDS_PAGE_INFO_SECURITY_TAB_WEAK_ENCRYPTION_CONNECTION_TEXT
#define IDS_PAGE_INFO_CERT_INFO_BUTTON
#define IDS_PAGE_INFO_ADDRESS
#define IDS_PAGE_INFO_PARTIAL_ADDRESS
#define IDS_PAGE_INFO_SECURITY_TAB_SECURE_IDENTITY_EV_VERIFIED
#define IDS_PAGE_INFO_CERTIFICATE
#define IDS_PAGE_INFO_CERTIFICATE_VALID_LINK
#define IDS_PAGE_INFO_CERTIFICATE_INVALID_LINK
#define IDS_PAGE_INFO_CERTIFICATE_BUTTON_TEXT
#define IDS_PAGE_INFO_CERTIFICATE_VALID_PARENTHESIZED
#define IDS_PAGE_INFO_CERTIFICATE_INVALID_PARENTHESIZED
#define IDS_PAGE_INFO_CERTIFICATE_VALID_LINK_TOOLTIP
#define IDS_PAGE_INFO_CERTIFICATE_INVALID_LINK_TOOLTIP
#define IDS_PAGE_INFO_COOKIES
#define IDS_PAGE_INFO_COOKIES_BUTTON_TEXT
#define IDS_PAGE_INFO_NUM_COOKIES_PARENTHESIZED
#define IDS_PAGE_INFO_COOKIES_TOOLTIP
#define IDS_PAGE_INFO_TYPE_ADS
#define IDS_PAGE_INFO_TYPE_PROTECTED_MEDIA_IDENTIFIER
#define IDS_PAGE_INFO_TYPE_BACKGROUND_SYNC
#define IDS_PAGE_INFO_TYPE_IMAGES
#define IDS_PAGE_INFO_TYPE_JAVASCRIPT
#define IDS_PAGE_INFO_TYPE_POPUPS_REDIRECTS
#define IDS_PAGE_INFO_TYPE_FLASH
#define IDS_PAGE_INFO_TYPE_LOCATION
#define IDS_PAGE_INFO_TYPE_NOTIFICATIONS
#define IDS_PAGE_INFO_TYPE_MIC
#define IDS_PAGE_INFO_TYPE_CAMERA
#define IDS_PAGE_INFO_TYPE_MIDI_SYSEX
#define IDS_PAGE_INFO_TYPE_SOUND
#define IDS_PAGE_INFO_TYPE_CLIPBOARD
#define IDS_PAGE_INFO_TYPE_SENSORS
#define IDS_PAGE_INFO_TYPE_MOTION_SENSORS
#define IDS_PAGE_INFO_TYPE_USB
#define IDS_PAGE_INFO_TYPE_SERIAL
#define IDS_PAGE_INFO_TYPE_NATIVE_FILE_SYSTEM_WRITE
#define IDS_PAGE_INFO_TYPE_BLUETOOTH_SCANNING
#define IDS_PAGE_INFO_TYPE_NFC
#define IDS_PAGE_INFO_BUTTON_TEXT_ALLOWED_BY_USER
#define IDS_PAGE_INFO_BUTTON_TEXT_BLOCKED_BY_USER
#define IDS_PAGE_INFO_BUTTON_TEXT_MUTED_BY_USER
#define IDS_PAGE_INFO_BUTTON_TEXT_ASK_BY_USER
#define IDS_PAGE_INFO_BUTTON_TEXT_DETECT_IMPORTANT_CONTENT_BY_USER
#define IDS_PAGE_INFO_BUTTON_TEXT_ALLOWED_BY_DEFAULT
#define IDS_PAGE_INFO_BUTTON_TEXT_AUTOMATIC_BY_DEFAULT
#define IDS_PAGE_INFO_BUTTON_TEXT_BLOCKED_BY_DEFAULT
#define IDS_PAGE_INFO_BUTTON_TEXT_MUTED_BY_DEFAULT
#define IDS_PAGE_INFO_BUTTON_TEXT_ASK_BY_DEFAULT
#define IDS_PAGE_INFO_BUTTON_TEXT_DETECT_IMPORTANT_CONTENT_BY_DEFAULT
#define IDS_PAGE_INFO_MENU_ITEM_DEFAULT_ALLOW
#define IDS_PAGE_INFO_MENU_ITEM_DEFAULT_BLOCK
#define IDS_PAGE_INFO_MENU_ITEM_DEFAULT_ASK
#define IDS_PAGE_INFO_MENU_ITEM_DEFAULT_DETECT_IMPORTANT_CONTENT
#define IDS_PAGE_INFO_MENU_ITEM_ALLOW
#define IDS_PAGE_INFO_MENU_ITEM_BLOCK
#define IDS_PAGE_INFO_MENU_ITEM_ASK
#define IDS_PAGE_INFO_MENU_ITEM_DETECT_IMPORTANT_CONTENT
#define IDS_PAGE_INFO_MENU_ITEM_ADS_BLOCK
#define IDS_PAGE_INFO_SELECTOR_TOOLTIP
#define IDS_PAGE_INFO_USB_DEVICE_SECONDARY_LABEL
#define IDS_PAGE_INFO_USB_DEVICE_ALLOWED_BY_POLICY_LABEL
#define IDS_PAGE_INFO_DELETE_USB_DEVICE
#define IDS_PAGE_INFO_SERIAL_PORT_SECONDARY_LABEL
#define IDS_PAGE_INFO_DELETE_SERIAL_PORT
#define IDS_PAGE_INFO_SITE_SETTINGS_LINK
#define IDS_PAGE_INFO_SITE_SETTINGS_TOOLTIP
#define IDS_PAGE_INFO_PERMISSION_ALLOWED_BY_POLICY
#define IDS_PAGE_INFO_PERMISSION_BLOCKED_BY_POLICY
#define IDS_PAGE_INFO_PERMISSION_ASK_BY_POLICY
#define IDS_PAGE_INFO_PERMISSION_ALLOWED_BY_EXTENSION
#define IDS_PAGE_INFO_PERMISSION_BLOCKED_BY_EXTENSION
#define IDS_PAGE_INFO_PERMISSION_ASK_BY_EXTENSION
#define IDS_PAGE_INFO_PERMISSION_AUTOMATICALLY_BLOCKED
#define IDS_PAGE_INFO_PERMISSION_ADS_SUBTITLE
#define IDS_PAGE_INFO_INFOBAR_TEXT
#define IDS_PAGE_INFO_INFOBAR_BUTTON
#define IDS_PAGE_INFO_CHANGE_PASSWORD_SUMMARY
#define IDS_PAGE_INFO_CHANGE_PASSWORD_DETAILS
#define IDS_PAGE_INFO_CHANGE_PASSWORD_DETAILS_SAVED
#define IDS_PAGE_INFO_CHANGE_PASSWORD_DETAILS_SAVED_1_DOMAIN
#define IDS_PAGE_INFO_CHANGE_PASSWORD_DETAILS_SAVED_2_DOMAINS
#define IDS_PAGE_INFO_CHANGE_PASSWORD_DETAILS_SAVED_3_DOMAINS
#define IDS_PAGE_INFO_CHANGE_PASSWORD_DETAILS_SYNC
#define IDS_PAGE_INFO_CHANGE_PASSWORD_DETAILS_SIGNED_IN_NON_SYNC
#define IDS_PAGE_INFO_CHANGE_PASSWORD_DETAILS_ENTERPRISE
#define IDS_PAGE_INFO_CHANGE_PASSWORD_DETAILS_ENTERPRISE_WITH_ORG_NAME
#define IDS_PAGE_INFO_CHANGE_PASSWORD_BUTTON
#define IDS_PAGE_INFO_PROTECT_ACCOUNT_BUTTON
#define IDS_PAGE_INFO_IGNORE_PASSWORD_WARNING_BUTTON
#define IDS_PAGE_INFO_WHITELIST_PASSWORD_REUSE_BUTTON
#define IDS_PAGE_INFO_BILLING_SUMMARY
#define IDS_PAGE_INFO_BILLING_DETAILS
#define IDS_PAGE_INFO_VR_PRESENTING_TEXT
#define IDS_PAGE_INFO_VR_TURN_OFF_BUTTON_TEXT
#define IDS_PAINT_PREVIEW_COMPOSITOR_SERVICE_DISPLAY_NAME
#define IDS_LEAK_CHECK_CREDENTIALS
#define IDS_CREDENTIAL_LEAK_TITLE_CHANGE
#define IDS_CREDENTIAL_LEAK_TITLE_CHECK
#define IDS_CREDENTIAL_LEAK_CHECK_PASSWORDS_MESSAGE
#define IDS_CREDENTIAL_LEAK_CHANGE_PASSWORD_MESSAGE
#define IDS_CREDENTIAL_LEAK_CHANGE_AND_CHECK_PASSWORDS_MESSAGE
#define IDS_PASSWORD_MANAGER_LEAK_HELP_MESSAGE
#define IDS_MANAGE_PASSWORDS_AUTO_SIGNIN_TITLE
#define IDS_PASSWORD_MANAGER_EMPTY_LOGIN
#define IDS_PASSWORD_MANAGER_MANAGE_PASSWORDS
#define IDS_PASSWORD_MANAGER_GENERATE_PASSWORD
#define IDS_PASSWORD_MANAGER_EXCEPTIONS_TAB_TITLE
#define IDS_PASSWORD_MANAGER_SHOW_PASSWORDS_TAB_TITLE
#define IDS_PASSWORD_MANAGER_SMART_LOCK
#define IDS_PASSWORD_MANAGER_DEFAULT_EXPORT_FILENAME
#define IDS_PAYMENTS_TITLE
#define IDS_PAYMENTS_ERROR_MESSAGE_DIALOG_TITLE
#define IDS_PAYMENTS_METHOD_OF_PAYMENT_LABEL
#define IDS_PAYMENTS_CONTACT_DETAILS_LABEL
#define IDS_PAYMENTS_ADD_CONTACT_DETAILS_LABEL
#define IDS_PAYMENTS_EDIT_CONTACT_DETAILS_LABEL
#define IDS_PAYMENTS_ADD_CARD_LABEL
#define IDS_PAYMENTS_ADD_BILLING_ADDRESS
#define IDS_PAYMENTS_ADD_NAME_ON_CARD
#define IDS_PAYMENTS_ADD_VALID_CARD_NUMBER
#define IDS_PAYMENTS_ADD_MORE_INFORMATION
#define IDS_PAYMENTS_EDIT_CARD
#define IDS_PAYMENTS_ADD_PHONE_NUMBER
#define IDS_PAYMENTS_ADD_RECIPIENT
#define IDS_PAYMENTS_ADD_VALID_ADDRESS
#define IDS_PAYMENTS_ADD_EMAIL
#define IDS_PAYMENTS_ADD_NAME
#define IDS_PAYMENTS_ORDER_SUMMARY_LABEL
#define IDS_PAYMENT_REQUEST_PAYMENT_METHOD_SECTION_NAME
#define IDS_PAYMENT_ACCOUNT_BALANCE
#define IDS_PAYMENT_REQUEST_CONTACT_INFO_SECTION_NAME
#define IDS_PAYMENTS_SHIPPING_SUMMARY_LABEL
#define IDS_PAYMENTS_SHIPPING_ADDRESS_LABEL
#define IDS_PAYMENTS_SHIPPING_OPTION_LABEL
#define IDS_PAYMENTS_DELIVERY_SUMMARY_LABEL
#define IDS_PAYMENTS_DELIVERY_ADDRESS_LABEL
#define IDS_PAYMENTS_DELIVERY_OPTION_LABEL
#define IDS_PAYMENTS_PICKUP_SUMMARY_LABEL
#define IDS_PAYMENTS_PICKUP_ADDRESS_LABEL
#define IDS_PAYMENTS_PICKUP_OPTION_LABEL
#define IDS_PAYMENTS_EDIT_BUTTON
#define IDS_PAYMENTS_PAY_BUTTON
#define IDS_PAYMENTS_ADD_CONTACT
#define IDS_PAYMENTS_ADD_CARD
#define IDS_PAYMENTS_ADD_ADDRESS
#define IDS_PAYMENTS_EDIT_ADDRESS
#define IDS_PAYMENTS_CANCEL_PAYMENT
#define IDS_PAYMENTS_NAME_FIELD_IN_CONTACT_DETAILS
#define IDS_PAYMENTS_PHONE_FIELD_IN_CONTACT_DETAILS
#define IDS_PAYMENTS_EMAIL_FIELD_IN_CONTACT_DETAILS
#define IDS_PAYMENTS_SAVE_CARD_TO_DEVICE_CHECKBOX
#define IDS_PAYMENTS_ACCEPTED_CARDS_LABEL
#define IDS_PAYMENTS_ACCEPTED_CREDIT_CARDS_LABEL
#define IDS_PAYMENTS_ACCEPTED_DEBIT_CARDS_LABEL
#define IDS_PAYMENTS_ACCEPTED_PREPAID_CARDS_LABEL
#define IDS_PAYMENTS_ACCEPTED_CREDIT_DEBIT_CARDS_LABEL
#define IDS_PAYMENTS_ACCEPTED_CREDIT_PREPAID_CARDS_LABEL
#define IDS_PAYMENTS_ACCEPTED_DEBIT_PREPAID_CARDS_LABEL
#define IDS_PAYMENTS_CREDIT_CARD_EXPIRATION_DATE_ABBR
#define IDS_PAYMENTS_LOADING_MESSAGE
#define IDS_PAYMENTS_PROCESSING_MESSAGE
#define IDS_PAYMENTS_CHECKING_OPTION
#define IDS_PAYMENTS_UPDATED_LABEL
#define IDS_PAYMENT_COMPLETE_MESSAGE
#define IDS_PAYMENTS_CREDIT_CARDS_ARE_ACCEPTED_LABEL
#define IDS_PAYMENTS_DEBIT_CARDS_ARE_ACCEPTED_LABEL
#define IDS_PAYMENTS_PREPAID_CARDS_ARE_ACCEPTED_LABEL
#define IDS_PAYMENTS_CREDIT_DEBIT_CARDS_ARE_ACCEPTED_LABEL
#define IDS_PAYMENTS_CREDIT_PREPAID_CARDS_ARE_ACCEPTED_LABEL
#define IDS_PAYMENTS_DEBIT_PREPAID_CARDS_ARE_ACCEPTED_LABEL
#define IDS_PAYMENTS_ERROR_MESSAGE
#define IDS_PAYMENTS_CARD_AND_ADDRESS_SETTINGS
#define IDS_PAYMENTS_CARD_AND_ADDRESS_SETTINGS_SIGNED_IN
#define IDS_PAYMENTS_CARD_AND_ADDRESS_SETTINGS_SIGNED_OUT
#define IDS_SETTINGS_CAN_MAKE_PAYMENT_TOGGLE_LABEL
#define IDS_PAYMENTS_REQUIRED_FIELD_MESSAGE
#define IDS_PAYMENTS_VALIDATION_INVALID_NAME
#define IDS_PAYMENTS_VALIDATION_INVALID_CREDIT_CARD_EXPIRATION_YEAR
#define IDS_PAYMENTS_VALIDATION_INVALID_CREDIT_CARD_EXPIRATION_MONTH
#define IDS_PAYMENTS_VALIDATION_INVALID_CREDIT_CARD_EXPIRED
#define IDS_PAYMENTS_VALIDATION_UNSUPPORTED_CREDIT_CARD_TYPE
#define IDS_PAYMENTS_PHONE_INVALID_VALIDATION_MESSAGE
#define IDS_PAYMENTS_EMAIL_INVALID_VALIDATION_MESSAGE
#define IDS_PAYMENTS_CARD_NUMBER_INVALID_VALIDATION_MESSAGE
#define IDS_PAYMENTS_CARD_EXPIRATION_INVALID_VALIDATION_MESSAGE
#define IDS_PAYMENTS_INVALID_ADDRESS
#define IDS_PAYMENTS_BILLING_ADDRESS_REQUIRED
#define IDS_PAYMENTS_NAME_ON_CARD_REQUIRED
#define IDS_PAYMENTS_CARD_BILLING_ADDRESS_REQUIRED
#define IDS_PAYMENTS_MORE_INFORMATION_REQUIRED
#define IDS_PAYMENTS_PHONE_NUMBER_REQUIRED
#define IDS_PAYMENTS_RECIPIENT_REQUIRED
#define IDS_PAYMENTS_EMAIL_REQUIRED
#define IDS_PAYMENTS_NAME_REQUIRED
#define IDS_PREF_EDIT_DIALOG_FIELD_REQUIRED_VALIDATION_MESSAGE
#define IDS_PAYMENT_REQUEST_ORDER_SUMMARY_SECTION_TOTAL_FORMAT
#define IDS_PAYMENT_REQUEST_ORDER_SUMMARY_SHEET_TOTAL_FORMAT
#define IDS_PAYMENT_REQUEST_ORDER_SUMMARY_MORE_ITEMS
#define IDS_PAYMENT_REQUEST_ORDER_SUMMARY_MULTIPLE_CURRENCY_INDICATOR
#define IDS_PAYMENTS_SELECT_SHIPPING_ADDRESS_FOR_SHIPPING_METHODS
#define IDS_PAYMENTS_UNSUPPORTED_SHIPPING_ADDRESS
#define IDS_PAYMENTS_UNSUPPORTED_SHIPPING_OPTION
#define IDS_PAYMENTS_SELECT_DELIVERY_ADDRESS_FOR_DELIVERY_METHODS
#define IDS_PAYMENTS_UNSUPPORTED_DELIVERY_ADDRESS
#define IDS_PAYMENTS_UNSUPPORTED_DELIVERY_OPTION
#define IDS_PAYMENTS_SELECT_PICKUP_ADDRESS_FOR_PICKUP_METHODS
#define IDS_PAYMENTS_UNSUPPORTED_PICKUP_ADDRESS
#define IDS_PAYMENTS_UNSUPPORTED_PICKUP_OPTION
#define IDS_PAYMENTS_ANDROID_APP_ERROR
#define IDS_UTILITY_PROCESS_PAYMENT_MANIFEST_PARSER_NAME
#define IDS_PAYMENT_REQUEST_PAYMENT_METHODS_PREVIEW
#define IDS_PAYMENT_REQUEST_SHIPPING_ADDRESSES_PREVIEW
#define IDS_PAYMENT_REQUEST_SHIPPING_OPTIONS_PREVIEW
#define IDS_PAYMENT_REQUEST_CONTACTS_PREVIEW
#define IDS_PAYMENTS_BACK
#define IDS_PAYMENTS_EDIT
#define IDS_PAYMENTS_ROW_ACCESSIBLE_NAME_FORMAT
#define IDS_PAYMENTS_ROW_ACCESSIBLE_NAME_SELECTED_FORMAT
#define IDS_PAYMENTS_PROFILE_LABELS_ACCESSIBLE_FORMAT
#define IDS_PAYMENTS_ACCESSIBLE_LABEL_WITH_ERROR
#define IDS_PAYMENTS_ORDER_SUMMARY_ACCESSIBLE_LABEL
#define IDS_PAYMENT_HANDLER_SHEET_DESCRIPTION
#define IDS_PAYMENT_HANDLER_SHEET_OPENED_HALF
#define IDS_PAYMENT_HANDLER_SHEET_OPENED_FULL
#define IDS_PAYMENT_HANDLER_SHEET_CLOSED
#define IDS_PDF_NEED_PASSWORD
#define IDS_PDF_PASSWORD_DIALOG_TITLE
#define IDS_PDF_PASSWORD_SUBMIT
#define IDS_PDF_PASSWORD_INVALID
#define IDS_PDF_PAGE_LOADING
#define IDS_PDF_ERROR_DIALOG_TITLE
#define IDS_PDF_PAGE_LOAD_FAILED
#define IDS_PDF_PAGE_RELOAD_BUTTON
#define IDS_PDF_BOOKMARKS
#define IDS_PDF_TOOLTIP_ROTATE_CW
#define IDS_PDF_TOOLTIP_DOWNLOAD
#define IDS_PDF_TOOLTIP_PRINT
#define IDS_PDF_TOOLTIP_FIT_PAGE
#define IDS_PDF_TOOLTIP_FIT_WIDTH
#define IDS_PDF_TOOLTIP_ZOOM_IN
#define IDS_PDF_TOOLTIP_ZOOM_OUT
#define IDS_PDF_LABEL_PAGE_NUMBER
#define IDS_PDF_PAGE_INDEX
#define IDS_PDF_DOCUMENT_PAGE_COUNT
#define IDS_AX_ROLE_DESCRIPTION_PDF_HIGHLIGHT
#define IDS_POLICY_DM_STATUS_SUCCESS
#define IDS_POLICY_DM_STATUS_REQUEST_INVALID
#define IDS_POLICY_DM_STATUS_REQUEST_FAILED
#define IDS_POLICY_DM_STATUS_TEMPORARY_UNAVAILABLE
#define IDS_POLICY_DM_STATUS_HTTP_STATUS_ERROR
#define IDS_POLICY_DM_STATUS_RESPONSE_DECODING_ERROR
#define IDS_POLICY_DM_STATUS_SERVICE_MANAGEMENT_NOT_SUPPORTED
#define IDS_POLICY_DM_STATUS_SERVICE_DEVICE_NOT_FOUND
#define IDS_POLICY_DM_STATUS_SERVICE_MANAGEMENT_TOKEN_INVALID
#define IDS_POLICY_DM_STATUS_SERVICE_ACTIVATION_PENDING
#define IDS_POLICY_DM_STATUS_SERVICE_INVALID_SERIAL_NUMBER
#define IDS_POLICY_DM_STATUS_SERVICE_DEVICE_ID_CONFLICT
#define IDS_POLICY_DM_STATUS_SERVICE_MISSING_LICENSES
#define IDS_POLICY_DM_STATUS_SERVICE_DEPROVISIONED
#define IDS_POLICY_DM_STATUS_SERVICE_POLICY_NOT_FOUND
#define IDS_POLICY_DM_STATUS_UNKNOWN_ERROR
#define IDS_POLICY_DM_STATUS_SERVICE_DOMAIN_MISMATCH
#define IDS_POLICY_DM_STATUS_CANNOT_SIGN_REQUEST
#define IDS_POLICY_DM_STATUS_REQUEST_TOO_LARGE
#define IDS_POLICY_DM_STATUS_CONSUMER_ACCOUNT_WITH_PACKAGED_LICENSE
#define IDS_POLICY_VALIDATION_OK
#define IDS_POLICY_VALIDATION_BAD_INITIAL_SIGNATURE
#define IDS_POLICY_VALIDATION_BAD_SIGNATURE
#define IDS_POLICY_VALIDATION_ERROR_CODE_PRESENT
#define IDS_POLICY_VALIDATION_PAYLOAD_PARSE_ERROR
#define IDS_POLICY_VALIDATION_WRONG_POLICY_TYPE
#define IDS_POLICY_VALIDATION_WRONG_SETTINGS_ENTITY_ID
#define IDS_POLICY_VALIDATION_BAD_TIMESTAMP
#define IDS_POLICY_VALIDATION_BAD_DM_TOKEN
#define IDS_POLICY_VALIDATION_BAD_DEVICE_ID
#define IDS_POLICY_VALIDATION_BAD_USER
#define IDS_POLICY_VALIDATION_POLICY_PARSE_ERROR
#define IDS_POLICY_VALIDATION_BAD_KEY_VERIFICATION_SIGNATURE
#define IDS_POLICY_VALIDATION_VALUE_WARNING
#define IDS_POLICY_VALIDATION_VALUE_ERROR
#define IDS_POLICY_VALIDATION_UNKNOWN_ERROR
#define IDS_POLICY_STORE_STATUS_OK
#define IDS_POLICY_STORE_STATUS_LOAD_ERROR
#define IDS_POLICY_STORE_STATUS_STORE_ERROR
#define IDS_POLICY_STORE_STATUS_PARSE_ERROR
#define IDS_POLICY_STORE_STATUS_SERIALIZE_ERROR
#define IDS_POLICY_STORE_STATUS_VALIDATION_ERROR
#define IDS_POLICY_STORE_STATUS_BAD_STATE
#define IDS_POLICY_STORE_STATUS_UNKNOWN_ERROR
#define IDS_POLICY_ASSOCIATION_STATE_ACTIVE
#define IDS_POLICY_ASSOCIATION_STATE_UNMANAGED
#define IDS_POLICY_ASSOCIATION_STATE_DEPROVISIONED
#define IDS_POLICY_TYPE_ERROR
#define IDS_POLICY_OUT_OF_RANGE_ERROR
#define IDS_POLICY_VALUE_FORMAT_ERROR
#define IDS_POLICY_DEFAULT_SEARCH_DISABLED
#define IDS_POLICY_NOT_SPECIFIED_ERROR
#define IDS_POLICY_EXTENSION_SETTINGS_ORIGIN_LIMIT_WARNING
#define IDS_POLICY_SUBKEY_ERROR
#define IDS_POLICY_LIST_ENTRY_ERROR
#define IDS_POLICY_SCHEMA_VALIDATION_ERROR
#define IDS_POLICY_INVALID_JSON_ERROR
#define IDS_POLICY_INVALID_SEARCH_URL_ERROR
#define IDS_POLICY_INVALID_SECURE_DNS_MODE_ERROR
#define IDS_POLICY_SECURE_DNS_MODE_NOT_SUPPORTED_ERROR
#define IDS_POLICY_SECURE_DNS_TEMPLATES_INVALID_ERROR
#define IDS_POLICY_SECURE_DNS_TEMPLATES_IRRELEVANT_MODE_ERROR
#define IDS_POLICY_SECURE_DNS_TEMPLATES_INVALID_MODE_ERROR
#define IDS_POLICY_SECURE_DNS_TEMPLATES_UNSET_MODE_ERROR
#define IDS_POLICY_SECURE_DNS_TEMPLATES_NOT_SPECIFIED_ERROR
#define IDS_POLICY_INVALID_PROXY_MODE_ERROR
#define IDS_POLICY_INVALID_UPDATE_URL_ERROR
#define IDS_POLICY_OFF_CWS_URL_ERROR
#define IDS_POLICY_HOMEPAGE_LOCATION_ERROR
#define IDS_POLICY_PROXY_MODE_DISABLED_ERROR
#define IDS_POLICY_PROXY_MODE_AUTO_DETECT_ERROR
#define IDS_POLICY_PROXY_MODE_PAC_URL_ERROR
#define IDS_POLICY_PROXY_MODE_FIXED_SERVERS_ERROR
#define IDS_POLICY_PROXY_MODE_SYSTEM_ERROR
#define IDS_POLICY_PROXY_BOTH_SPECIFIED_ERROR
#define IDS_POLICY_PROXY_NEITHER_SPECIFIED_ERROR
#define IDS_POLICY_OVERRIDDEN
#define IDS_POLICY_DEPRECATED
#define IDS_POLICY_VALUE_DEPRECATED
#define IDS_POLICY_LEVEL_ERROR
#define IDS_POLICY_OK
#define IDS_POLICY_UNSET
#define IDS_POLICY_UNKNOWN
#define IDS_POLICY_TITLE
#define IDS_POLICY_FILTER_PLACEHOLDER
#define IDS_POLICY_RELOAD_POLICIES
#define IDS_EXPORT_POLICIES_JSON
#define IDS_POLICY_STATUS
#define IDS_POLICY_STATUS_DEVICE
#define IDS_POLICY_STATUS_USER
#define IDS_POLICY_STATUS_MACHINE
#define IDS_POLICY_LABEL_ENTERPRISE_ENROLLMENT_DOMAIN
#define IDS_POLICY_LABEL_ENTERPRISE_DISPLAY_DOMAIN
#define IDS_POLICY_LABEL_MACHINE_ENROLLMENT_DOMAIN
#define IDS_POLICY_LABEL_MACHINE_ENROLLMENT_TOKEN
#define IDS_POLICY_LABEL_MACHINE_ENROLLMENT_DEVICE_ID
#define IDS_POLICY_LABEL_MACHINE_ENROLLMENT_MACHINE_NAME
#define IDS_POLICY_LABEL_USERNAME
#define IDS_POLICY_LABEL_GAIA_ID
#define IDS_POLICY_LABEL_CLIENT_ID
#define IDS_POLICY_LABEL_ASSET_ID
#define IDS_POLICY_LABEL_LOCATION
#define IDS_POLICY_LABEL_DIRECTORY_API_ID
#define IDS_POLICY_LABEL_TIME_SINCE_LAST_REFRESH
#define IDS_POLICY_NOT_SPECIFIED
#define IDS_POLICY_LABEL_PUSH_POLICIES
#define IDS_POLICY_PUSH_POLICIES_ON
#define IDS_POLICY_PUSH_POLICIES_OFF
#define IDS_POLICY_NEVER_FETCHED
#define IDS_POLICY_LABEL_REFRESH_INTERVAL
#define IDS_POLICY_LABEL_CONFLICT
#define IDS_POLICY_LABEL_ERROR
#define IDS_POLICY_LABEL_IGNORED
#define IDS_POLICY_LABEL_VALUE
#define IDS_POLICY_LABEL_STATUS
#define IDS_POLICY_SHOW_UNSET
#define IDS_POLICY_NO_POLICIES_SET
#define IDS_POLICY_LG_HEADER_SCOPE
#define IDS_POLICY_LG_HEADER_LEVEL
#define IDS_POLICY_LG_HEADER_NAME
#define IDS_POLICY_LG_HEADER_VALUE
#define IDS_POLICY_LG_HEADER_STATUS
#define IDS_POLICY_LG_HEADER_SOURCE
#define IDS_POLICY_LG_HEADER_WARNING
#define IDS_POLICY_SHOW_MORE
#define IDS_POLICY_SHOW_LESS
#define IDS_POLICY_LEARN_MORE
#define IDS_POLICY_SCOPE_USER
#define IDS_POLICY_SCOPE_DEVICE
#define IDS_POLICY_LEVEL_RECOMMENDED
#define IDS_POLICY_LEVEL_MANDATORY
#define IDS_POLICY_SOURCE_ENTERPRISE_DEFAULT
#define IDS_POLICY_SOURCE_CLOUD
#define IDS_POLICY_SOURCE_MERGED
#define IDS_POLICY_SOURCE_ACTIVE_DIRECTORY
#define IDS_POLICY_SOURCE_PLATFORM
#define IDS_POLICY_SOURCE_DEVICE_LOCAL_ACCOUNT_OVERRIDE
#define IDS_POLICY_RISK_TAG_FULL_ADMIN_ACCESS
#define IDS_POLICY_RISK_TAG_SYSTEM_SECURITY
#define IDS_POLICY_RISK_TAG_WEBSITE_SHARING
#define IDS_POLICY_RISK_TAG_ADMIN_SHARING
#define IDS_POLICY_RISK_TAG_FILTERING
#define IDS_POLICY_RISK_TAG_LOCAL_DATA_ACCESS
#define IDS_POLICY_RISK_TAG_GOOGLE_SHARING
#define IDS_POLICY_SHOW_EXPANDED_STATUS
#define IDS_POLICY_HIDE_EXPANDED_STATUS
#define IDS_POLICY_LIST_MERGING_WRONG_POLICY_TYPE_SPECIFIED
#define IDS_POLICY_DICTIONARY_MERGING_WRONG_POLICY_TYPE_SPECIFIED
#define IDS_POLICY_DICTIONARY_MERGING_POLICY_NOT_ALLOWED
#define IDS_POLICY_CONFLICT_SAME_VALUE
#define IDS_POLICY_CONFLICT_DIFF_VALUE
#define IDS_POLICY_MIGRATED_OLD_POLICY
#define IDS_POLICY_MIGRATED_NEW_POLICY
#define IDS_POLICY_BLOCKED
#define IDS_POLICY_IGNORED_BY_GROUP_MERGING
#define IDS_POLICY_INVALID_VALUE
#define IDS_POLICY_SPELLCHECK_UNKNOWN_LANGUAGE
#define IDS_POLICY_SPELLCHECK_BLACKLIST_IGNORE
#define IDS_POLICY_LABEL_IS_AFFILIATED
#define IDS_POLICY_IS_AFFILIATED_YES
#define IDS_POLICY_IS_AFFILIATED_NO
#define IDS_POLICY_LABEL_IS_OFFHOURS_ACTIVE
#define IDS_POLICY_OFFHOURS_ACTIVE
#define IDS_POLICY_OFFHOURS_NOT_ACTIVE
#define IDS_POLICY_SIGNIN_PROFILE
#define PRINT_PREVIEW_MEDIA_ASME_F_28X40IN
#define PRINT_PREVIEW_MEDIA_ISO_2A0_1189X1682MM
#define PRINT_PREVIEW_MEDIA_ISO_A0_841X1189MM
#define PRINT_PREVIEW_MEDIA_ISO_A10_26X37MM
#define PRINT_PREVIEW_MEDIA_ISO_A1_594X841MM
#define PRINT_PREVIEW_MEDIA_ISO_A2_420X594MM
#define PRINT_PREVIEW_MEDIA_ISO_A3_297X420MM
#define PRINT_PREVIEW_MEDIA_ISO_A4_210X297MM
#define PRINT_PREVIEW_MEDIA_ISO_A4_EXTRA_235_5X322_3MM
#define PRINT_PREVIEW_MEDIA_ISO_A4_TAB_225X297MM
#define PRINT_PREVIEW_MEDIA_ISO_A5_148X210MM
#define PRINT_PREVIEW_MEDIA_ISO_A5_EXTRA_174X235MM
#define PRINT_PREVIEW_MEDIA_ISO_A6_105X148MM
#define PRINT_PREVIEW_MEDIA_ISO_A7_74X105MM
#define PRINT_PREVIEW_MEDIA_ISO_A8_52X74MM
#define PRINT_PREVIEW_MEDIA_ISO_A9_37X52MM
#define PRINT_PREVIEW_MEDIA_ISO_B0_1000X1414MM
#define PRINT_PREVIEW_MEDIA_ISO_B10_31X44MM
#define PRINT_PREVIEW_MEDIA_ISO_B1_707X1000MM
#define PRINT_PREVIEW_MEDIA_ISO_B2_500X707MM
#define PRINT_PREVIEW_MEDIA_ISO_B3_353X500MM
#define PRINT_PREVIEW_MEDIA_ISO_B4_250X353MM
#define PRINT_PREVIEW_MEDIA_ISO_B5_176X250MM
#define PRINT_PREVIEW_MEDIA_ISO_B5_EXTRA_201X276MM
#define PRINT_PREVIEW_MEDIA_ISO_B6C4_125X324MM
#define PRINT_PREVIEW_MEDIA_ISO_B6_125X176MM
#define PRINT_PREVIEW_MEDIA_ISO_B7_88X125MM
#define PRINT_PREVIEW_MEDIA_ISO_B8_62X88MM
#define PRINT_PREVIEW_MEDIA_ISO_B9_44X62MM
#define PRINT_PREVIEW_MEDIA_ISO_C0_917X1297MM
#define PRINT_PREVIEW_MEDIA_ISO_C10_28X40MM
#define PRINT_PREVIEW_MEDIA_ISO_C1_648X917MM
#define PRINT_PREVIEW_MEDIA_ISO_C2_458X648MM
#define PRINT_PREVIEW_MEDIA_ISO_C3_324X458MM
#define PRINT_PREVIEW_MEDIA_ISO_C4_229X324MM
#define PRINT_PREVIEW_MEDIA_ISO_C5_162X229MM
#define PRINT_PREVIEW_MEDIA_ISO_C6C5_114X229MM
#define PRINT_PREVIEW_MEDIA_ISO_C6_114X162MM
#define PRINT_PREVIEW_MEDIA_ISO_C7C6_81X162MM
#define PRINT_PREVIEW_MEDIA_ISO_C7_81X114MM
#define PRINT_PREVIEW_MEDIA_ISO_C8_57X81MM
#define PRINT_PREVIEW_MEDIA_ISO_C9_40X57MM
#define PRINT_PREVIEW_MEDIA_ISO_DL_110X220MM
#define PRINT_PREVIEW_MEDIA_JIS_EXEC_216X330MM
#define PRINT_PREVIEW_MEDIA_JPN_CHOU2_111_1X146MM
#define PRINT_PREVIEW_MEDIA_JPN_CHOU3_120X235MM
#define PRINT_PREVIEW_MEDIA_JPN_CHOU4_90X205MM
#define PRINT_PREVIEW_MEDIA_JPN_HAGAKI_100X148MM
#define PRINT_PREVIEW_MEDIA_JPN_KAHU_240X322_1MM
#define PRINT_PREVIEW_MEDIA_JPN_KAKU2_240X332MM
#define PRINT_PREVIEW_MEDIA_JPN_OUFUKU_148X200MM
#define PRINT_PREVIEW_MEDIA_JPN_YOU4_105X235MM
#define PRINT_PREVIEW_MEDIA_NA_10X11_10X11IN
#define PRINT_PREVIEW_MEDIA_NA_10X13_10X13IN
#define PRINT_PREVIEW_MEDIA_NA_10X14_10X14IN
#define PRINT_PREVIEW_MEDIA_NA_10X15_10X15IN
#define PRINT_PREVIEW_MEDIA_NA_11X12_11X12IN
#define PRINT_PREVIEW_MEDIA_NA_11X15_11X15IN
#define PRINT_PREVIEW_MEDIA_NA_12X19_12X19IN
#define PRINT_PREVIEW_MEDIA_NA_5X7_5X7IN
#define PRINT_PREVIEW_MEDIA_NA_6X9_6X9IN
#define PRINT_PREVIEW_MEDIA_NA_7X9_7X9IN
#define PRINT_PREVIEW_MEDIA_NA_9X11_9X11IN
#define PRINT_PREVIEW_MEDIA_NA_A2_4_375X5_75IN
#define PRINT_PREVIEW_MEDIA_NA_ARCH_A_9X12IN
#define PRINT_PREVIEW_MEDIA_NA_ARCH_B_12X18IN
#define PRINT_PREVIEW_MEDIA_NA_ARCH_C_18X24IN
#define PRINT_PREVIEW_MEDIA_NA_ARCH_D_24X36IN
#define PRINT_PREVIEW_MEDIA_NA_ARCH_E_36X48IN
#define PRINT_PREVIEW_MEDIA_NA_B_PLUS_12X19_17IN
#define PRINT_PREVIEW_MEDIA_NA_C5_6_5X9_5IN
#define PRINT_PREVIEW_MEDIA_NA_C_17X22IN
#define PRINT_PREVIEW_MEDIA_NA_D_22X34IN
#define PRINT_PREVIEW_MEDIA_NA_EDP_11X14IN
#define PRINT_PREVIEW_MEDIA_NA_EUR_EDP_12X14IN
#define PRINT_PREVIEW_MEDIA_NA_E_34X44IN
#define PRINT_PREVIEW_MEDIA_NA_FANFOLD_EUR_8_5X12IN
#define PRINT_PREVIEW_MEDIA_NA_FANFOLD_US_11X14_875IN
#define PRINT_PREVIEW_MEDIA_NA_FOOLSCAP_8_5X13IN
#define PRINT_PREVIEW_MEDIA_NA_F_44X68IN
#define PRINT_PREVIEW_MEDIA_NA_GOVT_LEGAL_8X13IN
#define PRINT_PREVIEW_MEDIA_NA_GOVT_LETTER_8X10IN
#define PRINT_PREVIEW_MEDIA_NA_INDEX_3X5_3X5IN
#define PRINT_PREVIEW_MEDIA_NA_INDEX_4X6_4X6IN
#define PRINT_PREVIEW_MEDIA_NA_INDEX_4X6_EXT_6X8IN
#define PRINT_PREVIEW_MEDIA_NA_INDEX_5X8_5X8IN
#define PRINT_PREVIEW_MEDIA_NA_INVOICE_5_5X8_5IN
#define PRINT_PREVIEW_MEDIA_NA_LEDGER_11X17IN
#define PRINT_PREVIEW_MEDIA_NA_LEGAL_8_5X14IN
#define PRINT_PREVIEW_MEDIA_NA_LEGAL_EXTRA_9_5X15IN
#define PRINT_PREVIEW_MEDIA_NA_LETTER_8_5X11IN
#define PRINT_PREVIEW_MEDIA_NA_LETTER_EXTRA_9_5X12IN
#define PRINT_PREVIEW_MEDIA_NA_LETTER_PLUS_8_5X12_69IN
#define PRINT_PREVIEW_MEDIA_NA_NUMBER_10_4_125X9_5IN
#define PRINT_PREVIEW_MEDIA_NA_NUMBER_11_4_5X10_375IN
#define PRINT_PREVIEW_MEDIA_NA_NUMBER_12_4_75X11IN
#define PRINT_PREVIEW_MEDIA_NA_NUMBER_14_5X11_5IN
#define PRINT_PREVIEW_MEDIA_NA_PERSONAL_3_625X6_5IN
#define PRINT_PREVIEW_MEDIA_NA_SUPER_A_8_94X14IN
#define PRINT_PREVIEW_MEDIA_NA_SUPER_B_13X19IN
#define PRINT_PREVIEW_MEDIA_NA_WIDE_FORMAT_30X42IN
#define PRINT_PREVIEW_MEDIA_OM_DAI_PA_KAI_275X395MM
#define PRINT_PREVIEW_MEDIA_OM_FOLIO_SP_215X315MM
#define PRINT_PREVIEW_MEDIA_OM_INVITE_220X220MM
#define PRINT_PREVIEW_MEDIA_OM_ITALIAN_110X230MM
#define PRINT_PREVIEW_MEDIA_OM_JUURO_KU_KAI_198X275MM
#define PRINT_PREVIEW_MEDIA_OM_LARGE_PHOTO_200X300
#define PRINT_PREVIEW_MEDIA_OM_PA_KAI_267X389MM
#define PRINT_PREVIEW_MEDIA_OM_POSTFIX_114X229MM
#define PRINT_PREVIEW_MEDIA_OM_SMALL_PHOTO_100X150MM
#define PRINT_PREVIEW_MEDIA_PRC_10_324X458MM
#define PRINT_PREVIEW_MEDIA_PRC_16K_146X215MM
#define PRINT_PREVIEW_MEDIA_PRC_1_102X165MM
#define PRINT_PREVIEW_MEDIA_PRC_2_102X176MM
#define PRINT_PREVIEW_MEDIA_PRC_32K_97X151MM
#define PRINT_PREVIEW_MEDIA_PRC_3_125X176MM
#define PRINT_PREVIEW_MEDIA_PRC_4_110X208MM
#define PRINT_PREVIEW_MEDIA_PRC_5_110X220MM
#define PRINT_PREVIEW_MEDIA_PRC_6_120X320MM
#define PRINT_PREVIEW_MEDIA_PRC_7_160X230MM
#define PRINT_PREVIEW_MEDIA_PRC_8_120X309MM
#define PRINT_PREVIEW_MEDIA_ROC_16K_7_75X10_75IN
#define PRINT_PREVIEW_MEDIA_ROC_8K_10_75X15_5IN
#define PRINT_PREVIEW_MEDIA_JIS_B0_1030X1456MM
#define PRINT_PREVIEW_MEDIA_JIS_B1_728X1030MM
#define PRINT_PREVIEW_MEDIA_JIS_B2_515X728MM
#define PRINT_PREVIEW_MEDIA_JIS_B3_364X515MM
#define PRINT_PREVIEW_MEDIA_JIS_B4_257X364MM
#define PRINT_PREVIEW_MEDIA_JIS_B5_182X257MM
#define PRINT_PREVIEW_MEDIA_JIS_B6_128X182MM
#define PRINT_PREVIEW_MEDIA_JIS_B7_91X128MM
#define PRINT_PREVIEW_MEDIA_JIS_B8_64X91MM
#define PRINT_PREVIEW_MEDIA_JIS_B9_45X64MM
#define PRINT_PREVIEW_MEDIA_JIS_B10_32X45MM
#define IDS_PRINT_PREVIEW_FRIENDLY_WIN_NETWORK_PRINTER_NAME
#define IDS_PDF_COMPOSITOR_SERVICE_DISPLAY_NAME
#define IDS_RESET_PASSWORD_TITLE
#define IDS_RESET_PASSWORD_WARNING_HEADING
#define IDS_RESET_PASSWORD_HEADING
#define IDS_RESET_PASSWORD_WARNING_EXPLANATION_PARAGRAPH
#define IDS_RESET_PASSWORD_WARNING_EXPLANATION_PARAGRAPH_WITH_ORG_NAME
#define IDS_RESET_PASSWORD_BUTTON
#define IDS_RESET_PASSWORD_EXPLANATION_PARAGRAPH
#define IDS_RESET_PASSWORD_EXPLANATION_PARAGRAPH_WITH_ORG_NAME
#define IDS_SB_UNDER_CONSTRUCTION
#define IDS_SSL_OPEN_DETAILS_BUTTON
#define IDS_SSL_CLOSE_DETAILS_BUTTON
#define IDS_CAPTIVE_PORTAL_AUTHORIZATION_DIALOG_NAME
#define IDS_CAPTIVE_PORTAL_HEADING_WIRED
#define IDS_CAPTIVE_PORTAL_HEADING_WIFI
#define IDS_CAPTIVE_PORTAL_PRIMARY_PARAGRAPH_WIRED
#define IDS_CAPTIVE_PORTAL_PRIMARY_PARAGRAPH_WIFI
#define IDS_CAPTIVE_PORTAL_PRIMARY_PARAGRAPH_WIFI_SSID
#define IDS_CAPTIVE_PORTAL_PRIMARY_PARAGRAPH_NO_LOGIN_URL_WIRED
#define IDS_CAPTIVE_PORTAL_PRIMARY_PARAGRAPH_NO_LOGIN_URL_WIFI
#define IDS_CAPTIVE_PORTAL_PRIMARY_PARAGRAPH_NO_LOGIN_URL_WIFI_SSID
#define IDS_CAPTIVE_PORTAL_BUTTON_OPEN_LOGIN_PAGE
#define IDS_MITM_SOFTWARE_HEADING
#define IDS_MITM_SOFTWARE_PRIMARY_PARAGRAPH_ENTERPRISE
#define IDS_MITM_SOFTWARE_PRIMARY_PARAGRAPH_NONENTERPRISE
#define IDS_MITM_SOFTWARE_EXPLANATION_ENTERPRISE
#define IDS_MITM_SOFTWARE_EXPLANATION_NONENTERPRISE
#define IDS_MITM_SOFTWARE_EXPLANATION
#define IDS_BLOCKED_INTERCEPTION_HEADING
#define IDS_LOOKALIKE_URL_TITLE
#define IDS_LOOKALIKE_URL_HEADING
#define IDS_LOOKALIKE_URL_IGNORE
#define IDS_LOOKALIKE_URL_CONTINUE
#define IDS_LOOKALIKE_URL_PRIMARY_PARAGRAPH
#define IDS_CLOCK_ERROR_TITLE
#define IDS_CLOCK_ERROR_AHEAD_HEADING
#define IDS_CLOCK_ERROR_BEHIND_HEADING
#define IDS_CLOCK_ERROR_UPDATE_DATE_AND_TIME
#define IDS_CLOCK_ERROR_PRIMARY_PARAGRAPH
#define IDS_CLOCK_ERROR_EXPLANATION
#define IDS_SSL_V2_TITLE
#define IDS_SSL_V2_HEADING
#define IDS_SSL_V2_PRIMARY_PARAGRAPH
#define IDS_SSL_V2_RECURRENT_ERROR_PARAGRAPH
#define IDS_SSL_OVERRIDABLE_SAFETY_BUTTON
#define IDS_SSL_OVERRIDABLE_PROCEED_PARAGRAPH
#define IDS_SSL_RELOAD
#define IDS_SSL_NONOVERRIDABLE_PINNED
#define IDS_SSL_NONOVERRIDABLE_HSTS
#define IDS_SSL_NONOVERRIDABLE_REVOKED
#define IDS_SSL_NONOVERRIDABLE_MORE
#define IDS_SSL_NONOVERRIDABLE_INVALID
#define IDS_SAFEBROWSING_V3_TITLE
#define IDS_SAFEBROWSING_V3_OPEN_DETAILS_BUTTON
#define IDS_SAFEBROWSING_V3_CLOSE_DETAILS_BUTTON
#define IDS_SAFEBROWSING_OVERRIDABLE_SAFETY_BUTTON
#define IDS_MALWARE_V3_HEADING
#define IDS_MALWARE_V3_PRIMARY_PARAGRAPH
#define IDS_MALWARE_V3_EXPLANATION_PARAGRAPH
#define IDS_MALWARE_V3_EXPLANATION_PARAGRAPH_SUBRESOURCE
#define IDS_MALWARE_V3_PROCEED_PARAGRAPH
#define IDS_SAFE_BROWSING_PRIVACY_POLICY_PAGE
#define IDS_SAFE_BROWSING_SCOUT_REPORTING_AGREE
#define IDS_HARMFUL_V3_HEADING
#define IDS_HARMFUL_V3_PRIMARY_PARAGRAPH
#define IDS_HARMFUL_V3_EXPLANATION_PARAGRAPH
#define IDS_HARMFUL_V3_PROCEED_PARAGRAPH
#define IDS_PHISHING_V4_HEADING
#define IDS_PHISHING_V4_PRIMARY_PARAGRAPH
#define IDS_PHISHING_V4_EXPLANATION_PARAGRAPH
#define IDS_PHISHING_V4_PROCEED_AND_REPORT_PARAGRAPH
#define IDS_MALWARE_WEBVIEW_HEADING
#define IDS_MALWARE_WEBVIEW_EXPLANATION_PARAGRAPH
#define IDS_PHISHING_WEBVIEW_HEADING
#define IDS_PHISHING_WEBVIEW_EXPLANATION_PARAGRAPH
#define IDS_HARMFUL_WEBVIEW_HEADING
#define IDS_HARMFUL_WEBVIEW_EXPLANATION_PARAGRAPH
#define IDS_BILLING_WEBVIEW_HEADING
#define IDS_BILLING_WEBVIEW_EXPLANATION_PARAGRAPH
#define IDS_CONNECTION_HELP_SHOW_MORE
#define IDS_CONNECTION_HELP_SHOW_LESS
#define IDS_CONNECTION_HELP_TITLE
#define IDS_CONNECTION_HELP_HEADING
#define IDS_CONNECTION_HELP_GENERAL_HELP
#define IDS_CONNECTION_HELP_SPECIFIC_ERROR_HEADING
#define IDS_CONNECTION_HELP_CONNECTION_NOT_PRIVATE_TITLE
#define IDS_CONNECTION_HELP_CONNECT_TO_NETWORK_TITLE
#define IDS_CONNECTION_HELP_INCORRECT_CLOCK_TITLE
#define IDS_CONNECTION_HELP_CONNECTION_NOT_PRIVATE_DETAILS
#define IDS_CONNECTION_HELP_CONNECT_TO_NETWORK_DETAILS
#define IDS_CONNECTION_HELP_INCORRECT_CLOCK_DETAILS
#define IDS_CONNECTION_HELP_MITM_SOFTWARE_TITLE
#define IDS_CONNECTION_HELP_MITM_SOFTWARE_DETAILS
#define IDS_BILLING_TITLE
#define IDS_BILLING_HEADING
#define IDS_BILLING_PRIMARY_PARAGRAPH
#define IDS_BILLING_PRIMARY_BUTTON
#define IDS_BILLING_PROCEED_BUTTON
#define IDS_ORIGIN_POLICY_TITLE
#define IDS_ORIGIN_POLICY_HEADING
#define IDS_ORIGIN_POLICY_INFO
#define IDS_ORIGIN_POLICY_INFO2
#define IDS_ORIGIN_POLICY_BUTTON
#define IDS_ORIGIN_POLICY_DETAILS
#define IDS_ORIGIN_POLICY_EXPLANATION_CANNOT_LOAD
#define IDS_ORIGIN_POLICY_EXPLANATION_SHOULD_NOT_REDIRECT
#define IDS_ORIGIN_POLICY_EXPLANATION_OTHER
#define IDS_ORIGIN_POLICY_FINAL_PARAGRAPH
#define IDS_ORIGIN_POLICY_CLOSE
#define IDS_SAFETY_TIP_ANDROID_LEAVE_BUTTON
#define IDS_SAFETY_TIP_ANDROID_LOOKALIKE_TITLE
#define IDS_SAFETY_TIP_ANDROID_LOOKALIKE_DESCRIPTION
#define IDS_KNOWN_INTERCEPTION_TITLE
#define IDS_KNOWN_INTERCEPTION_HEADER
#define IDS_KNOWN_INTERCEPTION_BODY1
#define IDS_KNOWN_INTERCEPTION_BODY2
#define IDS_KNOWN_INTERCEPTION_INFOBAR_HEADING
#define IDS_KNOWN_INTERCEPTION_INFOBAR_BUTTON_TEXT
#define IDS_ERROR_PAGE_SUMMARY
#define IDS_NON_CRYPTO_SECURE_SUMMARY
#define IDS_HTTP_NONSECURE_SUMMARY
#define IDS_EDITED_NONSECURE
#define IDS_EDITED_NONSECURE_DESCRIPTION
#define IDS_SAFEBROWSING_WARNING
#define IDS_SAFEBROWSING_WARNING_SUMMARY
#define IDS_SAFEBROWSING_WARNING_DESCRIPTION
#define IDS_SHA1
#define IDS_SHA1_DESCRIPTION
#define IDS_SUBJECT_ALT_NAME_MISSING
#define IDS_SUBJECT_ALT_NAME_MISSING_DESCRIPTION
#define IDS_CERTIFICATE_TITLE
#define IDS_CERTIFICATE_CHAIN_ERROR
#define IDS_CERTIFICATE_CHAIN_ERROR_DESCRIPTION_FORMAT
#define IDS_VALID_SERVER_CERTIFICATE
#define IDS_VALID_SERVER_CERTIFICATE_DESCRIPTION
#define IDS_CERTIFICATE_EXPIRING_SOON
#define IDS_CERTIFICATE_EXPIRING_SOON_DESCRIPTION
#define IDS_SSL_CONNECTION_TITLE
#define IDS_SECURE_SSL_SUMMARY
#define IDS_PRIVATE_KEY_PINNING_BYPASSED
#define IDS_PRIVATE_KEY_PINNING_BYPASSED_DESCRIPTION
#define IDS_SSL_DESCRIPTION
#define IDS_OBSOLETE_SSL_SUMMARY
#define IDS_CIPHER_WITH_MAC
#define IDS_SSL_KEY_EXCHANGE_WITH_GROUP
#define IDS_SSL_RECOMMEND_PROTOCOL
#define IDS_SSL_RECOMMEND_KEY_EXCHANGE
#define IDS_SSL_RECOMMEND_CIPHER
#define IDS_SSL_RECOMMEND_SIGNATURE
#define IDS_RESOURCE_SECURITY_TITLE
#define IDS_SECURE_RESOURCES_SUMMARY
#define IDS_SECURE_RESOURCES_DESCRIPTION
#define IDS_MIXED_PASSIVE_CONTENT_SUMMARY
#define IDS_MIXED_PASSIVE_CONTENT_DESCRIPTION
#define IDS_MIXED_ACTIVE_CONTENT_SUMMARY
#define IDS_MIXED_ACTIVE_CONTENT_DESCRIPTION
#define IDS_CERT_ERROR_PASSIVE_CONTENT_SUMMARY
#define IDS_CERT_ERROR_PASSIVE_CONTENT_DESCRIPTION
#define IDS_CERT_ERROR_ACTIVE_CONTENT_SUMMARY
#define IDS_CERT_ERROR_ACTIVE_CONTENT_DESCRIPTION
#define IDS_NON_SECURE_FORM_SUMMARY
#define IDS_NON_SECURE_FORM_DESCRIPTION
#define IDS_SECURITY_TAB_SAFETY_TIP_TITLE
#define IDS_SECURITY_TAB_SAFETY_TIP_BAD_REPUTATION_SUMMARY
#define IDS_SECURITY_TAB_SAFETY_TIP_BAD_REPUTATION_DESCRIPTION
#define IDS_SECURITY_TAB_SAFETY_TIP_LOOKALIKE_SUMMARY
#define IDS_SECURITY_TAB_SAFETY_TIP_LOOKALIKE_DESCRIPTION
#define IDS_SHARING_DEVICE_TYPE_COMPUTER
#define IDS_SHARING_DEVICE_TYPE_DEVICE
#define IDS_SHARING_DEVICE_TYPE_PHONE
#define IDS_SHARING_DEVICE_TYPE_TABLET
#define IDS_CERT_ERROR_NO_SUBJECT_ALTERNATIVE_NAMES_DETAILS
#define IDS_CERT_ERROR_COMMON_NAME_INVALID_DETAILS
#define IDS_CERT_ERROR_COMMON_NAME_INVALID_DESCRIPTION
#define IDS_CERT_ERROR_EXPIRED_DETAILS
#define IDS_CERT_ERROR_EXPIRED_DESCRIPTION
#define IDS_CERT_ERROR_NOT_YET_VALID_DETAILS
#define IDS_CERT_ERROR_NOT_YET_VALID_DESCRIPTION
#define IDS_CERT_ERROR_NOT_VALID_AT_THIS_TIME_DETAILS
#define IDS_CERT_ERROR_NOT_VALID_AT_THIS_TIME_DESCRIPTION
#define IDS_CERT_ERROR_AUTHORITY_INVALID_DESCRIPTION
#define IDS_CERT_ERROR_CONTAINS_ERRORS_DETAILS
#define IDS_CERT_ERROR_CONTAINS_ERRORS_DESCRIPTION
#define IDS_CERT_ERROR_UNABLE_TO_CHECK_REVOCATION_DETAILS
#define IDS_CERT_ERROR_UNABLE_TO_CHECK_REVOCATION_DESCRIPTION
#define IDS_CERT_ERROR_NO_REVOCATION_MECHANISM_DETAILS
#define IDS_CERT_ERROR_NO_REVOCATION_MECHANISM_DESCRIPTION
#define IDS_CERT_ERROR_REVOKED_CERT_DETAILS
#define IDS_CERT_ERROR_REVOKED_CERT_DESCRIPTION
#define IDS_CERT_ERROR_INVALID_CERT_DETAILS
#define IDS_CERT_ERROR_INVALID_CERT_DESCRIPTION
#define IDS_CERT_ERROR_WEAK_SIGNATURE_ALGORITHM_DETAILS
#define IDS_CERT_ERROR_WEAK_SIGNATURE_ALGORITHM_DESCRIPTION
#define IDS_CERT_ERROR_WEAK_KEY_DETAILS
#define IDS_CERT_ERROR_WEAK_KEY_DESCRIPTION
#define IDS_CERT_ERROR_NAME_CONSTRAINT_VIOLATION_DETAILS
#define IDS_CERT_ERROR_NAME_CONSTRAINT_VIOLATION_DESCRIPTION
#define IDS_CERT_ERROR_VALIDITY_TOO_LONG_DETAILS
#define IDS_CERT_ERROR_VALIDITY_TOO_LONG_DESCRIPTION
#define IDS_CERT_ERROR_UNKNOWN_ERROR_DETAILS
#define IDS_CERT_ERROR_UNKNOWN_ERROR_DESCRIPTION
#define IDS_CERT_ERROR_SUMMARY_PINNING_FAILURE_DETAILS
#define IDS_CERT_ERROR_SUMMARY_PINNING_FAILURE_DESCRIPTION
#define IDS_CERT_ERROR_CERTIFICATE_TRANSPARENCY_REQUIRED_DETAILS
#define IDS_CERT_ERROR_CERTIFICATE_TRANSPARENCY_REQUIRED_DESCRIPTION
#define IDS_CERT_ERROR_AUTHORITY_INVALID_DETAILS
#define IDS_SYNC_BASIC_ENCRYPTION_DATA
#define IDS_SYNC_CONFIGURE_ENCRYPTION
#define IDS_SYNC_DATATYPE_AUTOFILL
#define IDS_SYNC_DATATYPE_BOOKMARKS
#define IDS_SYNC_DATATYPE_PASSWORDS
#define IDS_SYNC_DATATYPE_PREFERENCES
#define IDS_SYNC_DATATYPE_TABS
#define IDS_SYNC_DATATYPE_TYPED_URLS
#define IDS_SYNC_DATATYPE_READING_LIST
#define IDS_SYNC_EMPTY_PASSPHRASE_ERROR
#define IDS_SYNC_ENCRYPTION_SECTION_TITLE
#define IDS_SYNC_ENTER_GOOGLE_PASSPHRASE_BODY
#define IDS_SYNC_FULL_ENCRYPTION_DATA
#define IDS_SYNC_LOGIN_SETTING_UP
#define IDS_SYNC_PASSPHRASE_LABEL
#define IDS_SYNC_PASSPHRASE_MISMATCH_ERROR
#define IDS_SYNC_SERVICE_UNAVAILABLE
#define IDS_SYNC_ENTER_PASSPHRASE_BODY_WITH_DATE
#define IDS_SYNC_ENTER_GOOGLE_PASSPHRASE_BODY_WITH_DATE
#define IDS_SYNC_ENTER_PASSPHRASE_BODY
#define IDS_TRANSLATE_INFOBAR_OPTIONS_MORE_LANGUAGE
#define IDS_TRANSLATE_INFOBAR_OPTIONS_NOT_SOURCE_LANGUAGE
#define IDS_TRANSLATE_INFOBAR_OPTIONS_NEVER_TRANSLATE_LANG
#define IDS_TRANSLATE_INFOBAR_OPTIONS_NEVER_TRANSLATE_SITE
#define IDS_TRANSLATE_INFOBAR_OPTIONS_ALWAYS
#define IDS_TRANSLATE_INFOBAR_OPTIONS_REPORT_ERROR
#define IDS_TRANSLATE_INFOBAR_OPTIONS_ABOUT
#define IDS_TRANSLATE_INFOBAR_ACCEPT
#define IDS_TRANSLATE_INFOBAR_DENY
#define IDS_TRANSLATE_INFOBAR_NEVER_TRANSLATE
#define IDS_TRANSLATE_INFOBAR_ALWAYS_TRANSLATE
#define IDS_TRANSLATE_INFOBAR_TRANSLATING_TO
#define IDS_TRANSLATE_INFOBAR_AFTER_MESSAGE
#define IDS_TRANSLATE_INFOBAR_AFTER_MESSAGE_AUTODETERMINED_SOURCE_LANGUAGE
#define IDS_TRANSLATE_INFOBAR_REVERT
#define IDS_TRANSLATE_INFOBAR_RETRY
#define IDS_TRANSLATE_INFOBAR_ERROR_CANT_CONNECT
#define IDS_TRANSLATE_INFOBAR_ERROR_CANT_TRANSLATE
#define IDS_TRANSLATE_INFOBAR_UNKNOWN_PAGE_LANGUAGE
#define IDS_TRANSLATE_INFOBAR_ERROR_SAME_LANGUAGE
#define IDS_TRANSLATE_INFOBAR_UNSUPPORTED_PAGE_LANGUAGE
#define IDS_TRANSLATE_NOTIFICATION_ERROR
#define IDS_TRANSLATE_NOTIFICATION_ALWAYS_TRANSLATE
#define IDS_TRANSLATE_NOTIFICATION_LANGUAGE_NEVER
#define IDS_TRANSLATE_NOTIFICATION_SITE_NEVER
#define IDS_TRANSLATE_NOTIFICATION_UNDO
#define IDS_TRANSLATE_UNKNOWN_SOURCE_LANGUAGE
#define IDS_BOOKMARK_BAR_UNDO
#define IDS_BOOKMARK_BAR_REDO
#define IDS_BOOKMARK_BAR_UNDO_ADD
#define IDS_BOOKMARK_BAR_REDO_ADD
#define IDS_BOOKMARK_BAR_UNDO_DELETE
#define IDS_BOOKMARK_BAR_REDO_DELETE
#define IDS_BOOKMARK_BAR_UNDO_EDIT
#define IDS_BOOKMARK_BAR_REDO_EDIT
#define IDS_BOOKMARK_BAR_UNDO_MOVE
#define IDS_BOOKMARK_BAR_REDO_MOVE
#define IDS_BOOKMARK_BAR_UNDO_REORDER
#define IDS_BOOKMARK_BAR_REDO_REORDER
#define IDS_VERSION_UI_TITLE
#define IDS_VERSION_UI_OFFICIAL
#define IDS_VERSION_UI_UNOFFICIAL
#define IDS_VERSION_UI_32BIT
#define IDS_VERSION_UI_64BIT
#define IDS_VERSION_UI_REVISION
#define IDS_VERSION_UI_OS
#define IDS_VERSION_UI_USER_AGENT
#define IDS_VERSION_UI_COMMAND_LINE
#define IDS_VERSION_UI_EXECUTABLE_PATH
#define IDS_VERSION_UI_PROFILE_PATH
#define IDS_VERSION_UI_PATH_NOTFOUND
#define IDS_VERSION_UI_VARIATIONS
#define IDS_VERSION_UI_VARIATIONS_CMD
#define IDS_VERSION_UI_COHORT_NAME
#define IDS_MANAGEMENT_TITLE
#define IDS_MANAGEMENT_TOOLBAR_TITLE
#define IDS_MANAGEMENT_SUBTITLE
#define IDS_MANAGEMENT_SUBTITLE_MANAGED_BY
#define IDS_MANAGEMENT_NOT_MANAGED_SUBTITLE
#define IDS_MANAGEMENT_BROWSER_NOTICE
#define IDS_MANAGEMENT_NOT_MANAGED_NOTICE
#define IDS_MANAGEMENT_EXTENSION_REPORTING
#define IDS_MANAGEMENT_EXTENSIONS_INSTALLED
#define IDS_MANAGEMENT_EXTENSIONS_INSTALLED_BY
#define IDS_MANAGEMENT_EXTENSIONS_NAME
#define IDS_MANAGEMENT_EXTENSIONS_PERMISSIONS
#define IDS_MANAGEMENT_BROWSER_REPORTING
#define IDS_MANAGEMENT_BROWSER_REPORTING_EXPLANATION
#define IDS_MANAGEMENT_EXTENSION_REPORT_MACHINE_NAME
#define IDS_MANAGEMENT_EXTENSION_REPORT_MACHINE_NAME_ADDRESS
#define IDS_MANAGEMENT_EXTENSION_REPORT_USERNAME
#define IDS_MANAGEMENT_EXTENSION_REPORT_VERSION
#define IDS_MANAGEMENT_EXTENSION_REPORT_EXTENSIONS_PLUGINS
#define IDS_MANAGEMENT_EXTENSION_REPORT_SAFE_BROWSING_WARNINGS
#define IDS_MANAGEMENT_EXTENSION_REPORT_USER_BROWSING_DATA
#define IDS_MANAGEMENT_EXTENSION_REPORT_PERF_CRASH
#define IDS_MANAGEMENT_THREAT_PROTECTION
#define IDS_MANAGEMENT_THREAT_PROTECTION_DESCRIPTION
#define IDS_MANAGEMENT_THREAT_PROTECTION_DESCRIPTION_BY
#define IDS_MANAGEMENT_DATA_LOSS_PREVENTION_NAME
#define IDS_MANAGEMENT_DATA_LOSS_PREVENTION_PERMISSIONS
#define IDS_MANAGEMENT_MALWARE_SCANNING_NAME
#define IDS_MANAGEMENT_MALWARE_SCANNING_PERMISSIONS
#define IDS_MANAGEMENT_ENTERPRISE_REPORTING_NAME
#define IDS_MANAGEMENT_ENTERPRISE_REPORTING_PERMISSIONS
#define IDS_CANCEL
#define IDS_CLOSE
#define IDS_CLEAR
#define IDS_DONE
#define IDS_LEARN_MORE
#define IDS_OK
#define IDS_ADD
#define IDS_REMOVE
#define IDS_SAVE
#define IDS_MENU
#define IDS_NO_THANKS
#define IDS_NOT_NOW
#define IDS_TURN_OFF
#define IDS_PLUGIN_NOT_SUPPORTED
#define IDS_PRINT
#define IDS_RECENTLY_CLOSED
#define IDS_CHOOSE
#define IDS_ACCNAME_BACK
#define IDS_ACCNAME_FORWARD
#define IDS_ACCNAME_OK
#define IDS_ACCNAME_CANCEL
#define IDS_ACCNAME_DONE
#define IDS_ACCNAME_SAVE
#define IDS_ACCNAME_CLOSE
#define IDS_ACCNAME_OPEN
#define IDS_ACCNAME_PREVIOUS
#define IDS_ACCNAME_NEXT
#define IDS_ACCNAME_LOCATION
#define IDS_ACCNAME_PARTICLE_DISC
#define IDS_ACCNAME_TAB_LIST
#define IDS_UTILITY_PROCESS_JSON_PARSER_NAME
#define IDS_SESSION_CRASHED_VIEW_RESTORE_BUTTON
#define IDS_SESSION_CRASHED_VIEW_STARTUP_PAGES_BUTTON
#define IDS_OPTIONS_ADVANCED_SECTION_TITLE_PRIVACY
#define IDS_PATCH_SERVICE_DISPLAY_NAME
#define IDS_UNZIP_SERVICE_DISPLAY_NAME
#define IDS_EXTENSION_BAD_FILE_ENCODING
#define IDS_EXTENSION_CANT_GET_ABSOLUTE_PATH
#define IDS_EXTENSION_CONTAINS_PRIVATE_KEY
#define IDS_EXTENSION_CRX_EXISTS
#define IDS_EXTENSION_DIRECTORY_NO_EXISTS
#define IDS_EXTENSION_ERROR_WHILE_SIGNING
#define IDS_EXTENSION_FAILED_DURING_PACKAGING
#define IDS_EXTENSION_LOAD_ABOUT_PAGE_FAILED
#define IDS_EXTENSION_LOAD_BACKGROUND_SCRIPT_FAILED
#define IDS_EXTENSION_LOAD_BACKGROUND_PAGE_FAILED
#define IDS_EXTENSION_LOAD_CSS_FAILED
#define IDS_EXTENSION_LOAD_ICON_FAILED
#define IDS_EXTENSION_LOAD_ICON_NOT_SUFFICIENTLY_VISIBLE
#define IDS_EXTENSION_LOAD_JAVASCRIPT_FAILED
#define IDS_EXTENSION_LOAD_OPTIONS_PAGE_FAILED
#define IDS_EXTENSION_LOCALES_NO_DEFAULT_LOCALE_SPECIFIED
#define IDS_EXTENSION_MANIFEST_UNREADABLE
#define IDS_EXTENSION_MANIFEST_INVALID
#define IDS_EXTENSION_PACKAGE_IMAGE_ERROR
#define IDS_EXTENSION_PACKAGE_UNZIP_ERROR
#define IDS_EXTENSION_PRIVATE_KEY_EXISTS
#define IDS_EXTENSION_PRIVATE_KEY_FAILED_TO_READ
#define IDS_EXTENSION_PRIVATE_KEY_FAILED_TO_EXPORT
#define IDS_EXTENSION_PRIVATE_KEY_FAILED_TO_GENERATE
#define IDS_EXTENSION_PRIVATE_KEY_FAILED_TO_OUTPUT
#define IDS_EXTENSION_PRIVATE_KEY_INVALID
#define IDS_EXTENSION_PRIVATE_KEY_NO_EXISTS
#define IDS_EXTENSION_PRIVATE_KEY_INVALID_PATH
#define IDS_EXTENSION_PRIVATE_KEY_INVALID_FORMAT
#define IDS_EXTENSION_PUBLIC_KEY_FAILED_TO_EXPORT
#define IDS_EXTENSION_SHARING_VIOLATION
#define IDS_EXTENSION_CANT_INSTALL_POLICY_BLOCKED
#define IDS_EXTENSION_CANT_MODIFY_POLICY_REQUIRED
#define IDS_EXTENSION_CANT_UNINSTALL_POLICY_REQUIRED
#define IDS_EXTENSION_DISABLED_UPDATE_REQUIRED_BY_POLICY
#define IDS_DEVICE_NAME_WITH_PRODUCT_SERIAL
#define IDS_DEVICE_NAME_WITH_PRODUCT_UNKNOWN_VENDOR
#define IDS_DEVICE_NAME_WITH_PRODUCT_UNKNOWN_VENDOR_SERIAL
#define IDS_DEVICE_NAME_WITH_PRODUCT_VENDOR
#define IDS_DEVICE_NAME_WITH_PRODUCT_VENDOR_SERIAL
#define IDS_DEVICE_NAME_WITH_UNKNOWN_PRODUCT_UNKNOWN_VENDOR
#define IDS_DEVICE_NAME_WITH_UNKNOWN_PRODUCT_UNKNOWN_VENDOR_SERIAL
#define IDS_DEVICE_NAME_WITH_UNKNOWN_PRODUCT_VENDOR
#define IDS_DEVICE_NAME_WITH_UNKNOWN_PRODUCT_VENDOR_SERIAL
#define IDS_DEVICE_PERMISSIONS_PROMPT_SINGLE_SELECTION
#define IDS_DEVICE_PERMISSIONS_PROMPT_MULTIPLE_SELECTION
#define IDS_CAMERA_FACING_USER
#define IDS_CAMERA_FACING_ENVIRONMENT
#define IDS_EXTENSION_USB_DEVICE_PRODUCT_NAME_AND_VENDOR
#define IDS_EXTENSION_TASK_MANAGER_APPVIEW_TAG_PREFIX
#define IDS_EXTENSION_TASK_MANAGER_EXTENSIONOPTIONS_TAG_PREFIX
#define IDS_EXTENSION_TASK_MANAGER_MIMEHANDLERVIEW_TAG_PREFIX
#define IDS_EXTENSION_TASK_MANAGER_WEBVIEW_TAG_PREFIX
#define IDS_EXTENSION_WARNINGS_NETWORK_DELAY
#define IDS_EXTENSION_WARNINGS_DOWNLOAD_FILENAME_CONFLICT
#define IDS_EXTENSION_WARNING_RELOAD_TOO_FREQUENT
#define IDS_EXTENSION_WARNING_RULESET_FAILED_TO_LOAD
#define IDS_EXTENSION_INSTALL_PROCESS_CRASHED
#define IDS_EXTENSION_PACKAGE_ERROR_CODE
#define IDS_EXTENSION_PACKAGE_ERROR_MESSAGE
#define IDS_EXTENSION_PACKAGE_INSTALL_ERROR
#define IDS_EXTENSION_UNPACK_FAILED
#define IDS_EXTENSION_WEBGL_NOT_SUPPORTED
#define IDS_BOOKMARK_GROUP_FROM_IE
#define IDS_BOOKMARK_GROUP_FROM_EDGE
#define IDS_BOOKMARK_GROUP_FROM_FIREFOX
#define IDS_BOOKMARK_GROUP_FROM_SAFARI
#define IDS_BOOKMARK_GROUP
#define IDS_BOOKMARK_BAR_SHOW_APPS_SHORTCUT
#define IDS_BOOKMARK_BAR_SHOW_MANAGED_BOOKMARKS_DEFAULT_NAME
#define IDS_BOOKMARK_BAR_SHOW_MANAGED_BOOKMARKS
#define IDS_BOOKMARK_BAR_APPS_SHORTCUT_NAME
#define IDS_BOOKMARK_BAR_APPS_SHORTCUT_TOOLTIP
#define IDS_BOOKMARK_BAR_OPEN_ALL
#define IDS_BOOKMARK_BAR_OPEN_ALL_COUNT
#define IDS_BOOKMARK_BAR_OPEN_ALL_COUNT_NEW_WINDOW
#define IDS_BOOKMARK_BAR_OPEN_ALL_COUNT_INCOGNITO
#define IDS_BOOKMARK_BAR_OPEN_IN_NEW_TAB
#define IDS_BOOKMARK_BAR_OPEN_IN_NEW_WINDOW
#define IDS_BOOKMARK_BAR_OPEN_INCOGNITO
#define IDS_BOOKMARK_BAR_EDIT
#define IDS_BOOKMARK_BAR_RENAME_FOLDER
#define IDS_BOOKMARK_BAR_REMOVE
#define IDS_BOOKMARK_BAR_ADD_NEW_BOOKMARK
#define IDS_BOOKMARK_BAR_NEW_FOLDER
#define IDS_SHOW_BOOKMARK_BAR
#define IDS_BOOKMARK_BAR_SHOULD_OPEN_ALL
#define IDS_BOOKMARK_BUBBLE_PAGE_BOOKMARKED
#define IDS_BOOKMARK_BUBBLE_PAGE_BOOKMARK
#define IDS_BOOKMARK_BUBBLE_NAME_LABEL
#define IDS_BOOKMARK_AX_BUBBLE_NAME_LABEL
#define IDS_BOOKMARK_BUBBLE_FOLDER_LABEL
#define IDS_BOOKMARK_AX_BUBBLE_FOLDER_LABEL
#define IDS_BOOKMARK_BUBBLE_OPTIONS
#define IDS_BOOKMARK_BUBBLE_CHOOSER_ANOTHER_FOLDER
#define IDS_BOOKMARK_DICE_PROMO_SYNC_MESSAGE
#define IDS_BOOKMARK_BUBBLE_DESKTOP_TO_IOS_PROMO_TITLE
#define IDS_BOOKMARK_BUBBLE_DESKTOP_TO_IOS_PROMO_TITLE_V2
#define IDS_BOOKMARK_BUBBLE_DESKTOP_TO_IOS_PROMO_TITLE_V3
#define IDS_BOOKMARK_FOOTNOTE_DESKTOP_TO_IOS_PROMO_MESSAGE
#define IDS_BOOKMARK_EDITOR_NAME_LABEL
#define IDS_BOOKMARK_AX_EDITOR_NAME_LABEL
#define IDS_BOOKMARK_AX_EDITOR_URL_LABEL
#define IDS_BOOKMARK_EDITOR_URL_LABEL
#define IDS_BOOKMARK_EDITOR_CONFIRM_DELETE
#define IDS_BOOKMARK_EDITOR_NEW_FOLDER_BUTTON
#define IDS_BOOKMARK_EDITOR_NEW_FOLDER_MENU_ITEM
#define IDS_BOOKMARK_FOLDER_EDITOR_WINDOW_TITLE
#define IDS_BOOKMARK_FOLDER_EDITOR_WINDOW_TITLE_NEW
#define IDS_BOOKMARK_ALL_TABS_DIALOG_TITLE
#define IDS_BOOKMARK_MANAGER_TITLE
#define IDS_BOOKMARK_MANAGER_SEARCH_BUTTON
#define IDS_BOOKMARK_MANAGER
#define IDS_BOOKMARK_MANAGER_ORGANIZE_MENU
#define IDS_BOOKMARK_MANAGER_INVALID_URL
#define IDS_EXPORT_BOOKMARKS_DEFAULT_FILENAME
#define IDS_BOOKMARK_MANAGER_ADD_BOOKMARK_TITLE
#define IDS_BOOKMARK_MANAGER_ADD_FOLDER_TITLE
#define IDS_BOOKMARK_MANAGER_CLEAR_SEARCH
#define IDS_BOOKMARK_MANAGER_EMPTY_LIST
#define IDS_BOOKMARK_MANAGER_EMPTY_UNMODIFIABLE_LIST
#define IDS_BOOKMARK_MANAGER_FOLDER_LABEL
#define IDS_BOOKMARK_MANAGER_FOLDER_RENAME_TITLE
#define IDS_BOOKMARK_MANAGER_FOLDER_LIST_CHANGED
#define IDS_BOOKMARK_MANAGER_LIST_AX_LABEL
#define IDS_BOOKMARK_MANAGER_MENU_ADD_BOOKMARK
#define IDS_BOOKMARK_MANAGER_MENU_ADD_FOLDER
#define IDS_BOOKMARK_MANAGER_MENU_CUT
#define IDS_BOOKMARK_MANAGER_MENU_COPY
#define IDS_BOOKMARK_MANAGER_MENU_COPY_URL
#define IDS_BOOKMARK_MANAGER_MENU_PASTE
#define IDS_BOOKMARK_MANAGER_MENU_EXPORT
#define IDS_BOOKMARK_MANAGER_MENU_HELP_CENTER
#define IDS_BOOKMARK_MANAGER_MENU_IMPORT
#define IDS_BOOKMARK_MANAGER_MENU_OPEN_ALL
#define IDS_BOOKMARK_MANAGER_MENU_OPEN_ALL_NEW_WINDOW
#define IDS_BOOKMARK_MANAGER_MENU_OPEN_ALL_INCOGNITO
#define IDS_BOOKMARK_MANAGER_MENU_OPEN_IN_NEW_TAB
#define IDS_BOOKMARK_MANAGER_MENU_OPEN_IN_NEW_WINDOW
#define IDS_BOOKMARK_MANAGER_MENU_OPEN_INCOGNITO
#define IDS_BOOKMARK_MANAGER_MENU_RENAME
#define IDS_BOOKMARK_MANAGER_MENU_SHOW_IN_FOLDER
#define IDS_BOOKMARK_MANAGER_MENU_SORT
#define IDS_BOOKMARK_MANAGER_MORE_ACTIONS
#define IDS_BOOKMARK_MANAGER_MORE_ACTIONS_AX_LABEL
#define IDS_BOOKMARK_MANAGER_MORE_ACTIONS_MULTI_AX_LABEL
#define IDS_BOOKMARK_MANAGER_OPEN_DIALOG_TITLE
#define IDS_BOOKMARK_MANAGER_OPEN_DIALOG_CONFIRM
#define IDS_BOOKMARK_MANAGER_ITEMS_SELECTED
#define IDS_BOOKMARK_MANAGER_SIDEBAR_AX_LABEL
#define IDS_BOOKMARK_MANAGER_TOAST_FOLDER_SORTED
#define IDS_BOOKMARK_MANAGER_TOAST_ITEM_DELETED
#define IDS_BOOKMARK_MANAGER_TOAST_ITEMS_DELETED
#define IDS_BOOKMARK_MANAGER_TOAST_URL_COPIED
#define IDS_BOOKMARK_MANAGER_TOAST_ITEM_COPIED
#define IDS_BOOKMARK_MANAGER_TOAST_ITEMS_COPIED
#define IDS_BOOKMARKS_MENU
#define IDS_BOOKMARK_THIS_TAB
#define IDS_BOOKMARK_ALL_TABS
#define IDS_TOOLTIP_STARRED
#define IDS_APP_MANAGEMENT_CAMERA
#define IDS_APP_MANAGEMENT_LOCATION
#define IDS_APP_MANAGEMENT_MICROPHONE
#define IDS_APP_MANAGEMENT_NO_APPS_FOUND
#define IDS_APP_MANAGEMENT_NOTIFICATIONS
#define IDS_APP_MANAGEMENT_PERMISSIONS
#define IDS_APP_MANAGEMENT_MORE_SETTINGS
#define IDS_APP_MANAGEMENT_PIN_TO_SHELF
#define IDS_APP_MANAGEMENT_SEARCH_PROMPT
#define IDS_APP_MANAGEMENT_UNINSTALL_APP
#define IDS_APP_MANAGEMENT_CONTACTS
#define IDS_APP_MANAGEMENT_STORAGE
#define IDS_APP_MANAGEMENT_POLICY_APP_POLICY_STRING
#define IDS_MEDIA_ROUTER_ICON_TOOLTIP_TEXT
#define IDS_MEDIA_ROUTER_MENU_ITEM_TITLE
#define IDS_MEDIA_ROUTER_PRESENTATION_CAST_MODE
#define IDS_MEDIA_ROUTER_DESKTOP_MIRROR_CAST_MODE
#define IDS_MEDIA_ROUTER_TAB_MIRROR_CAST_MODE
#define IDS_MEDIA_ROUTER_LOCAL_FILE_CAST_MODE
#define IDS_MEDIA_ROUTER_CAST_LOCAL_MEDIA_TITLE
#define IDS_MEDIA_ROUTER_ALTERNATIVE_SOURCES_BUTTON
#define IDS_MEDIA_ROUTER_ABOUT
#define IDS_MEDIA_ROUTER_CLOUD_SERVICES_TOGGLE
#define IDS_MEDIA_ROUTER_HELP
#define IDS_MEDIA_ROUTER_ALWAYS_SHOW_TOOLBAR_ACTION
#define IDS_MEDIA_ROUTER_REPORT_ISSUE
#define IDS_MEDIA_ROUTER_SHOWN_BY_POLICY
#define IDS_MEDIA_ROUTER_TOGGLE_MEDIA_REMOTING
#define IDS_MEDIA_ROUTER_ISSUE_CREATE_ROUTE_TIMEOUT
#define IDS_MEDIA_ROUTER_ISSUE_CREATE_ROUTE_TIMEOUT_FOR_DESKTOP
#define IDS_MEDIA_ROUTER_ISSUE_CREATE_ROUTE_TIMEOUT_FOR_TAB
#define IDS_MEDIA_ROUTER_ISSUE_UNABLE_TO_CAST_DESKTOP
#define IDS_MEDIA_ROUTER_ISSUE_FILE_CAST_GENERIC_ERROR
#define IDS_MEDIA_ROUTER_ISSUE_FILE_CAST_ERROR
#define IDS_MEDIA_ROUTER_ISSUE_TAB_AUDIO_NOT_SUPPORTED
#define IDS_MEDIA_ROUTER_STATUS_LOOKING_FOR_DEVICES
#define IDS_MEDIA_ROUTER_STATUS_NO_DEVICES_FOUND
#define IDS_MEDIA_ROUTER_NO_DEVICES_FOUND_BUTTON
#define IDS_MEDIA_ROUTER_DESTINATION_MISSING
#define IDS_MEDIA_ROUTER_SINK_AVAILABLE
#define IDS_MEDIA_ROUTER_SINK_CONNECTING
#define IDS_MEDIA_ROUTER_SINK_DISCONNECTING
#define IDS_MEDIA_ROUTER_STOP_CASTING
#define IDS_MEDIA_ROUTER_SOURCE_NOT_SUPPORTED
#define IDS_MEDIA_ROUTER_FILE_DIALOG_AUDIO_VIDEO_FILTER
#define IDS_MEDIA_ROUTER_REMOTING_DIALOG_TITLE
#define IDS_MEDIA_ROUTER_REMOTING_DIALOG_BODY_TEXT
#define IDS_MEDIA_ROUTER_REMOTING_DIALOG_CHECKBOX
#define IDS_MEDIA_ROUTER_REMOTING_DIALOG_OPTIMIZE_BUTTON
#define IDS_MEDIA_ROUTER_REMOTING_DIALOG_CANCEL_BUTTON
#define IDS_MEDIA_ROUTER_REMOTING_DIALOG_CANCEL_BUTTON_MACOS
#define IDS_MEDIA_ROUTER_CLOUD_SERVICES_DIALOG_TITLE
#define IDS_MEDIA_ROUTER_CLOUD_SERVICES_DIALOG_BODY
#define IDS_MEDIA_ROUTER_CLOUD_SERVICES_DIALOG_ENABLE
#define IDS_MEDIA_ROUTER_CLOUD_SERVICES_DIALOG_CANCEL
#define IDS_MEDIA_ROUTER_WIRED_DISPLAY_ROUTE_DESCRIPTION
#define IDS_MEDIA_ROUTER_WIRED_DISPLAY_SINK_NAME
#define IDS_GLOBAL_MEDIA_CONTROLS_BACK_TO_TAB
#define IDS_GLOBAL_MEDIA_CONTROLS_ICON_TOOLTIP_TEXT
#define IDS_GLOBAL_MEDIA_CONTROLS_DISMISS_ICON_TOOLTIP_TEXT
#define IDS_LEGACY_SUPERVISED_USER_INFO
#define IDS_CHILD_INFO_ONE_CUSTODIAN
#define IDS_CHILD_INFO_TWO_CUSTODIANS
#define IDS_LEGACY_SUPERVISED_USER_AVATAR_LABEL
#define IDS_GENERIC_USER_AVATAR_LABEL
#define IDS_INCOGNITO_BUBBLE_ACCESSIBLE_TITLE
#define IDS_AVATAR_BUTTON_INCOGNITO
#define IDS_AVATAR_BUTTON_INCOGNITO_TOOLTIP
#define IDS_AVATAR_BUTTON_SYNC_ERROR
#define IDS_AVATAR_BUTTON_SYNC_ERROR_TOOLTIP
#define IDS_AVATAR_BUTTON_SYNC_PAUSED
#define IDS_AVATAR_BUTTON_SYNC_PAUSED_TOOLTIP
#define IDS_LEGACY_SUPERVISED_USER_NEW_AVATAR_LABEL
#define IDS_CHILD_AVATAR_LABEL
#define IDS_BLOCK_INTERSTITIAL_DEFAULT_FEEDBACK_TEXT
#define IDS_PROFILES_OPTIONS_GROUP_NAME
#define IDS_PROFILES_PROFILE_BUBBLE_ACCESSIBLE_TITLE
#define IDS_PROFILES_PROFILE_SIGNOUT_BUTTON
#define IDS_PROFILES_EXIT_PROFILE_BUTTON
#define IDS_PROFILES_GAIA_SIGNIN_TITLE
#define IDS_PROFILES_ACCOUNT_REMOVAL_TITLE
#define IDS_PROFILES_SYNC_COMPLETE_TITLE
#define IDS_PROFILES_OPEN_SYNC_SETTINGS_BUTTON
#define IDS_PROFILES_DICE_SIGNIN_BUTTON
#define IDS_PROFILES_DICE_NOT_SYNCING_TITLE
#define IDS_PROFILES_DICE_SIGNIN_FIRST_ACCOUNT_BUTTON
#define IDS_PROFILES_DICE_SIGNIN_FIRST_ACCOUNT_BUTTON_NO_NAME
#define IDS_PROFILES_DICE_SYNC_DISABLED_TITLE
#define IDS_PROFILES_DICE_SYNC_PAUSED_TITLE
#define IDS_PROFILES_EXIT_GUEST
#define IDS_PROFILES_CLOSE_X_WINDOWS_BUTTON
#define IDS_PROFILES_SIGNIN_PROMO
#define IDS_PROFILES_PASSWORDS_LINK
#define IDS_PROFILES_CREDIT_CARDS_LINK
#define IDS_PROFILES_ADDRESSES_LINK
#define IDS_PROFILES_OTHER_PROFILES_TITLE
#define IDS_PROFILES_PROFILE_MANAGE_ACCOUNTS_BUTTON
#define IDS_PROFILES_PROFILE_HIDE_MANAGE_ACCOUNTS_BUTTON
#define IDS_PROFILES_MANAGE_USERS_BUTTON
#define IDS_PROFILES_OPEN_GUEST_PROFILE_BUTTON
#define IDS_PROFILES_CLOSE_ALL_WINDOWS_BUTTON
#define IDS_PROFILES_EDIT_PROFILE_ACCESSIBLE_NAME
#define IDS_PROFILES_EDIT_SIGNED_IN_PROFILE_ACCESSIBLE_NAME
#define IDS_PROFILES_GUEST_PROFILE_NAME
#define IDS_DEFAULT_PROFILE_NAME
#define IDS_LEGACY_DEFAULT_PROFILE_NAME
#define IDS_NUMBERED_PROFILE_NAME
#define IDS_NEW_NUMBERED_PROFILE_NAME
#define IDS_SINGLE_PROFILE_DISPLAY_NAME
#define IDS_GUEST_PROFILE_NAME
#define IDS_DEFAULT_AVATAR_NAME_8
#define IDS_DEFAULT_AVATAR_NAME_9
#define IDS_DEFAULT_AVATAR_NAME_10
#define IDS_DEFAULT_AVATAR_NAME_11
#define IDS_DEFAULT_AVATAR_NAME_12
#define IDS_DEFAULT_AVATAR_NAME_13
#define IDS_DEFAULT_AVATAR_NAME_14
#define IDS_DEFAULT_AVATAR_NAME_15
#define IDS_DEFAULT_AVATAR_NAME_16
#define IDS_DEFAULT_AVATAR_NAME_17
#define IDS_DEFAULT_AVATAR_NAME_18
#define IDS_DEFAULT_AVATAR_NAME_19
#define IDS_DEFAULT_AVATAR_NAME_20
#define IDS_DEFAULT_AVATAR_NAME_21
#define IDS_DEFAULT_AVATAR_NAME_22
#define IDS_DEFAULT_AVATAR_NAME_23
#define IDS_DEFAULT_AVATAR_NAME_24
#define IDS_DEFAULT_AVATAR_NAME_25
#define IDS_DEFAULT_AVATAR_NAME_26
#define IDS_DEFAULT_AVATAR_LABEL_0
#define IDS_DEFAULT_AVATAR_LABEL_1
#define IDS_DEFAULT_AVATAR_LABEL_2
#define IDS_DEFAULT_AVATAR_LABEL_3
#define IDS_DEFAULT_AVATAR_LABEL_4
#define IDS_DEFAULT_AVATAR_LABEL_5
#define IDS_DEFAULT_AVATAR_LABEL_6
#define IDS_DEFAULT_AVATAR_LABEL_7
#define IDS_DEFAULT_AVATAR_LABEL_8
#define IDS_DEFAULT_AVATAR_LABEL_9
#define IDS_DEFAULT_AVATAR_LABEL_10
#define IDS_DEFAULT_AVATAR_LABEL_11
#define IDS_DEFAULT_AVATAR_LABEL_12
#define IDS_DEFAULT_AVATAR_LABEL_13
#define IDS_DEFAULT_AVATAR_LABEL_14
#define IDS_DEFAULT_AVATAR_LABEL_15
#define IDS_DEFAULT_AVATAR_LABEL_16
#define IDS_DEFAULT_AVATAR_LABEL_17
#define IDS_DEFAULT_AVATAR_LABEL_18
#define IDS_DEFAULT_AVATAR_LABEL_19
#define IDS_DEFAULT_AVATAR_LABEL_20
#define IDS_DEFAULT_AVATAR_LABEL_21
#define IDS_DEFAULT_AVATAR_LABEL_22
#define IDS_DEFAULT_AVATAR_LABEL_23
#define IDS_DEFAULT_AVATAR_LABEL_24
#define IDS_DEFAULT_AVATAR_LABEL_25
#define IDS_DEFAULT_AVATAR_LABEL_27
#define IDS_DEFAULT_AVATAR_LABEL_28
#define IDS_DEFAULT_AVATAR_LABEL_29
#define IDS_DEFAULT_AVATAR_LABEL_30
#define IDS_DEFAULT_AVATAR_LABEL_31
#define IDS_DEFAULT_AVATAR_LABEL_32
#define IDS_DEFAULT_AVATAR_LABEL_33
#define IDS_DEFAULT_AVATAR_LABEL_34
#define IDS_DEFAULT_AVATAR_LABEL_35
#define IDS_DEFAULT_AVATAR_LABEL_36
#define IDS_DEFAULT_AVATAR_LABEL_37
#define IDS_DEFAULT_AVATAR_LABEL_38
#define IDS_DEFAULT_AVATAR_LABEL_39
#define IDS_DEFAULT_AVATAR_LABEL_40
#define IDS_DEFAULT_AVATAR_LABEL_41
#define IDS_DEFAULT_AVATAR_LABEL_42
#define IDS_DEFAULT_AVATAR_LABEL_43
#define IDS_DEFAULT_AVATAR_LABEL_44
#define IDS_DEFAULT_AVATAR_LABEL_45
#define IDS_DEFAULT_AVATAR_LABEL_46
#define IDS_DEFAULT_AVATAR_LABEL_47
#define IDS_DEFAULT_AVATAR_LABEL_48
#define IDS_DEFAULT_AVATAR_LABEL_49
#define IDS_DEFAULT_AVATAR_LABEL_50
#define IDS_DEFAULT_AVATAR_LABEL_51
#define IDS_DEFAULT_AVATAR_LABEL_52
#define IDS_DEFAULT_AVATAR_LABEL_53
#define IDS_DEFAULT_AVATAR_LABEL_54
#define IDS_DEFAULT_AVATAR_LABEL_55
#define IDS_PROFILES_LOCAL_PROFILE_STATE
#define IDS_PROFILES_CREATE_BUTTON_LABEL
#define IDS_PROFILES_MANAGE_BUTTON_LABEL
#define IDS_PROFILES_DEFAULT_NAME
#define IDS_SYNC_LOGIN_NAME_PROHIBITED
#define IDS_SUPERVISED_USER_NOT_ALLOWED_BY_POLICY
#define IDS_OLD_PROFILES_DISABLED_TITLE
#define IDS_OLD_PROFILES_DISABLED_MESSAGE
#define IDS_OLD_PROFILES_DISABLED_ADD_PERSON_SUGGESTION
#define IDS_OLD_PROFILES_DISABLED_ADD_PERSON_SUGGESTION_WITH_DOMAIN
#define IDS_OLD_PROFILES_DISABLED_REMOVED_OLD_PROFILE
#define IDS_SYNC_USER_NAME_IN_USE_ERROR
#define IDS_SYNC_USER_NAME_IN_USE_BY_ERROR
#define IDS_PROFILES_CREATE_TITLE
#define IDS_PROFILES_CREATE_NAME_PLACEHOLDER
#define IDS_PROFILES_CREATE_LOCAL_ERROR
#define IDS_PROFILES_CREATE_DESKTOP_SHORTCUT_LABEL
#define IDS_PROFILES_CREATE_SUPERVISED_JUST_SIGNED_IN
#define IDS_IMPORT_EXISTING_LEGACY_SUPERVISED_USER_TITLE
#define IDS_IMPORT_EXISTING_LEGACY_SUPERVISED_USER_TEXT
#define IDS_CREATE_NEW_LEGACY_SUPERVISED_USER_LINK
#define IDS_IMPORT_EXISTING_LEGACY_SUPERVISED_USER_OK
#define IDS_ADD_USER_BUTTON
#define IDS_LOGIN_POD_USER_REMOVE_WARNING_BUTTON
#define IDS_CREATE_LEGACY_SUPERVISED_USER_MENU_LABEL
#define IDS_SCREEN_LOCK_SIGN_OUT
#define IDS_BROWSE_AS_GUEST_BUTTON
#define IDS_MORE_OPTIONS_BUTTON
#define IDS_SCREEN_LOCK_ACTIVE_USER
#define IDS_LOGIN_ERROR_AUTHENTICATING
#define IDS_LOGIN_ERROR_AUTHENTICATING_OFFLINE
#define IDS_LOGIN_POD_EMPTY_PASSWORD_TEXT
#define IDS_LOGIN_POD_SIGNING_IN
#define IDS_LOGIN_POD_PASSWORD_FIELD_ACCESSIBLE_NAME
#define IDS_LOGIN_POD_SUBMIT_BUTTON_ACCESSIBLE_NAME
#define IDS_LOGIN_POD_MENU_BUTTON_ACCESSIBLE_NAME
#define IDS_LOGIN_POD_MENU_REMOVE_ITEM_ACCESSIBLE_NAME
#define IDS_LOGIN_POD_LEGACY_SUPERVISED_USER_REMOVE_WARNING
#define IDS_LOGIN_POD_NON_OWNER_USER_REMOVE_WARNING
#define IDS_USER_MANAGER_GO_GUEST_PROFILES_LOCKED_ERROR
#define IDS_USER_MANAGER_REMOVE_PROFILE_PROFILES_LOCKED_ERROR
#define IDS_USER_MANAGER_ADD_PROFILE_PROFILES_LOCKED_ERROR
#define IDS_USER_MANAGER_PROMPT_MESSAGE
#define IDS_LOGIN_POD_USER_REMOVE_WARNING_NONSYNC
#define IDS_LOGIN_POD_USER_REMOVE_WARNING_HISTORY
#define IDS_LOGIN_POD_USER_REMOVE_WARNING_PASSWORDS
#define IDS_LOGIN_POD_USER_REMOVE_WARNING_BOOKMARKS
#define IDS_LOGIN_POD_USER_REMOVE_WARNING_AUTOFILL
#define IDS_LOGIN_POD_USER_REMOVE_WARNING_CALCULATING
#define IDS_USER_MANAGER_TUTORIAL_NEXT
#define IDS_USER_MANAGER_TUTORIAL_DONE
#define IDS_USER_MANAGER_TUTORIAL_SLIDE_GUEST_TITLE
#define IDS_USER_MANAGER_TUTORIAL_SLIDE_FRIENDS_TITLE
#define IDS_USER_MANAGER_TUTORIAL_SLIDE_OUTRO_TITLE
#define IDS_USER_MANAGER_TUTORIAL_SLIDE_OUTRO_USER_NOT_FOUND
#define IDS_SETTINGS_EMPTY_STRING
#define IDS_SETTINGS_CONTINUE
#define IDS_SETTINGS_MORE_ACTIONS
#define IDS_SETTINGS_TURN_ON
#define IDS_SETTINGS_ABOUT_PAGE_BROWSER_VERSION
#define IDS_SETTINGS_ABOUT_PAGE_RELAUNCH
#define IDS_SETTINGS_ABOUT_PAGE_RELEASE_NOTES
#define IDS_SETTINGS_ABOUT_PAGE_SHOW_RELEASE_NOTES
#define IDS_SETTINGS_ABOUT_UPGRADE_CHECK_STARTED
#define IDS_SETTINGS_CAPTIONS
#define IDS_SETTINGS_CAPTIONS_SETTINGS
#define IDS_SETTINGS_CAPTIONS_PREVIEW
#define IDS_SETTINGS_CAPTIONS_TEXT_SIZE
#define IDS_SETTINGS_CAPTIONS_TEXT_FONT
#define IDS_SETTINGS_CAPTIONS_TEXT_COLOR
#define IDS_SETTINGS_CAPTIONS_TEXT_OPACITY
#define IDS_SETTINGS_CAPTIONS_BACKGROUND_OPACITY
#define IDS_SETTINGS_CAPTIONS_OPACITY_OPAQUE
#define IDS_SETTINGS_CAPTIONS_OPACITY_SEMI_TRANSPARENT
#define IDS_SETTINGS_CAPTIONS_OPACITY_TRANSPARENT
#define IDS_SETTINGS_CAPTIONS_TEXT_SHADOW
#define IDS_SETTINGS_CAPTIONS_TEXT_SHADOW_NONE
#define IDS_SETTINGS_CAPTIONS_TEXT_SHADOW_RAISED
#define IDS_SETTINGS_CAPTIONS_TEXT_SHADOW_DEPRESSED
#define IDS_SETTINGS_CAPTIONS_TEXT_SHADOW_UNIFORM
#define IDS_SETTINGS_CAPTIONS_TEXT_SHADOW_DROP_SHADOW
#define IDS_SETTINGS_CAPTIONS_BACKGROUND_COLOR
#define IDS_SETTINGS_CAPTIONS_COLOR_BLACK
#define IDS_SETTINGS_CAPTIONS_COLOR_WHITE
#define IDS_SETTINGS_CAPTIONS_COLOR_RED
#define IDS_SETTINGS_CAPTIONS_COLOR_GREEN
#define IDS_SETTINGS_CAPTIONS_COLOR_BLUE
#define IDS_SETTINGS_CAPTIONS_COLOR_YELLOW
#define IDS_SETTINGS_CAPTIONS_COLOR_CYAN
#define IDS_SETTINGS_CAPTIONS_COLOR_MAGENTA
#define IDS_SETTINGS_CAPTIONS_DEFAULT_SETTING
#define IDS_SETTINGS_ACCESSIBILITY
#define IDS_SETTINGS_ACCESSIBILITY_WEB_STORE
#define IDS_SETTINGS_MORE_FEATURES_LINK
#define IDS_SETTINGS_MORE_FEATURES_LINK_DESCRIPTION
#define IDS_SETTINGS_ACCESSIBLE_IMAGE_LABELS_TITLE
#define IDS_SETTINGS_ACCESSIBLE_IMAGE_LABELS_SUBTITLE
#define IDS_SETTINGS_APPEARANCE
#define IDS_SETTINGS_CUSTOM_WEB_ADDRESS
#define IDS_SETTINGS_ENTER_CUSTOM_WEB_ADDRESS
#define IDS_SETTINGS_HOME_BUTTON_DISABLED
#define IDS_SETTINGS_THEMES
#define IDS_SETTINGS_RESET_TO_DEFAULT_THEME
#define IDS_SETTINGS_CHROME_COLORS
#define IDS_SETTINGS_SHOW_HOME_BUTTON
#define IDS_SETTINGS_SHOW_BOOKMARKS_BAR
#define IDS_SETTINGS_HOME_PAGE_NTP
#define IDS_SETTINGS_CHANGE_HOME_PAGE
#define IDS_SETTINGS_WEB_STORE
#define IDS_SETTINGS_ADVANCED
#define IDS_SETTINGS_BASIC
#define IDS_SETTINGS_MENU_BUTTON_LABEL
#define IDS_SETTINGS_MENU_EXTENSIONS_LINK_TOOLTIP
#define IDS_SETTINGS_SEARCH_PROMPT
#define IDS_SETTINGS_SEARCH_NO_RESULTS_HELP
#define IDS_SETTINGS_SETTINGS
#define IDS_SETTINGS_ALT_PAGE_TITLE
#define IDS_SETTINGS_SUBPAGE_BUTTON
#define IDS_SETTINGS_RESTART
#define IDS_SETTINGS_CONTROLLED_BY_EXTENSION
#define IDS_SETTINGS_CLEAR
#define IDS_SETTINGS_DELETE
#define IDS_SETTINGS_EDIT
#define IDS_SETTINGS_TOGGLE_ON
#define IDS_SETTINGS_TOGGLE_OFF
#define IDS_SETTINGS_NOT_VALID
#define IDS_SETTINGS_NOT_VALID_WEB_ADDRESS
#define IDS_SETTINGS_NOT_VALID_WEB_ADDRESS_FOR_CONTENT_TYPE
#define IDS_SETTINGS_RETRY
#define IDS_SETTINGS_SLIDER_MIN_MAX_ARIA_ROLE_DESCRIPTION
#define IDS_SETTINGS_AUTOFILL
#define IDS_SETTINGS_GOOGLE_PAYMENTS
#define IDS_SETTINGS_AUTOFILL_ADDRESSES_ADD_TITLE
#define IDS_SETTINGS_AUTOFILL_ADDRESSES_EDIT_TITLE
#define IDS_SETTINGS_AUTOFILL_ADDRESSES_COUNTRY
#define IDS_SETTINGS_AUTOFILL_ADDRESSES_PHONE
#define IDS_SETTINGS_AUTOFILL_ADDRESSES_EMAIL
#define IDS_SETTINGS_AUTOFILL_CREDIT_CARD_TYPE_COLUMN_LABEL
#define IDS_SETTINGS_AUTOFILL_DETAIL
#define IDS_SETTINGS_ADDRESS_REMOVE
#define IDS_SETTINGS_CREDIT_CARD_REMOVE
#define IDS_SETTINGS_CREDIT_CARD_CLEAR
#define IDS_SETTINGS_EDIT_CREDIT_CARD_TITLE
#define IDS_SETTINGS_PAYMENTS_MANAGE_CREDIT_CARDS
#define IDS_SETTINGS_PAYMENTS_SAVED_TO_THIS_DEVICE_ONLY
#define IDS_SETTINGS_ADD_CREDIT_CARD_TITLE
#define IDS_SETTINGS_MIGRATABLE_CARDS_LABEL
#define IDS_SETTINGS_SINGLE_MIGRATABLE_CARD_INFO
#define IDS_SETTINGS_MULTIPLE_MIGRATABLE_CARDS_INFO
#define IDS_SETTINGS_NAME_ON_CREDIT_CARD
#define IDS_SETTINGS_CREDIT_CARD_NUMBER
#define IDS_SETTINGS_CREDIT_CARD_EXPIRATION_DATE
#define IDS_SETTINGS_CREDIT_CARD_EXPIRATION_MONTH
#define IDS_SETTINGS_CREDIT_CARD_EXPIRATION_YEAR
#define IDS_SETTINGS_CREDIT_CARD_EXPIRED
#define IDS_SETTINGS_PASSWORDS
#define IDS_SETTINGS_PASSWORDS_SAVE_PASSWORDS_TOGGLE_LABEL
#define IDS_SETTINGS_PASSWORDS_AUTOSIGNIN_CHECKBOX_LABEL
#define IDS_SETTINGS_PASSWORDS_AUTOSIGNIN_CHECKBOX_DESC
#define IDS_SETTINGS_PASSWORDS_LEAK_DETECTION_LABEL
#define IDS_SETTINGS_PASSWORDS_LEAK_DETECTION_SIGNED_OUT_ENABLED_DESC
#define IDS_SETTINGS_PASSWORDS_SAVED_HEADING
#define IDS_SETTINGS_PASSWORDS_EXCEPTIONS_HEADING
#define IDS_SETTINGS_PASSWORDS_DELETE_EXCEPTION
#define IDS_SETTINGS_PASSWORD_REMOVE
#define IDS_SETTINGS_PASSWORD_SEARCH
#define IDS_SETTINGS_PASSWORD_SHOW
#define IDS_SETTINGS_PASSWORD_HIDE
#define IDS_SETTINGS_PASSWORDS_VIEW_DETAILS_TITLE
#define IDS_SETTINGS_PASSWORD_DETAILS
#define IDS_SETTINGS_PASSWORDS_WEBSITE
#define IDS_SETTINGS_PASSWORDS_USERNAME
#define IDS_SETTINGS_PASSWORDS_PASSWORD
#define IDS_SETTINGS_ADDRESS_NONE
#define IDS_SETTINGS_PAYMENT_METHODS_NONE
#define IDS_SETTINGS_PASSWORDS_NONE
#define IDS_SETTINGS_PASSWORDS_EXCEPTIONS_NONE
#define IDS_SETTINGS_PASSWORD_UNDO
#define IDS_SETTINGS_PASSWORD_DELETED_PASSWORD
#define IDS_SETTINGS_PASSWORDS_MANAGE_PASSWORDS
#define IDS_SETTINGS_PASSWORDS_EXPORT_MENU_ITEM
#define IDS_SETTINGS_PASSWORDS_EXPORT_TITLE
#define IDS_SETTINGS_PASSWORDS_EXPORT_DESCRIPTION
#define IDS_SETTINGS_PASSWORDS_EXPORT
#define IDS_SETTINGS_PASSWORDS_EXPORT_TRY_AGAIN
#define IDS_SETTINGS_PASSWORDS_EXPORTING_TITLE
#define IDS_SETTINGS_PASSWORDS_EXPORTING_FAILURE_TITLE
#define IDS_SETTINGS_PASSWORDS_EXPORTING_FAILURE_TIPS
#define IDS_SETTINGS_PASSWORDS_EXPORTING_FAILURE_TIP_ENOUGH_SPACE
#define IDS_SETTINGS_PASSWORDS_EXPORTING_FAILURE_TIP_ANOTHER_FOLDER
#define IDS_SETTINGS_PASSWORD_ROW_MORE_ACTIONS
#define IDS_SETTINGS_PASSWORD_ROW_FEDERATED_MORE_ACTIONS
#define IDS_SETTINGS_DEFAULT_BROWSER
#define IDS_SETTINGS_DEFAULT_BROWSER_MAKE_DEFAULT_BUTTON
#define IDS_SETTINGS_CLEAR_PERIOD_TITLE
#define IDS_SETTINGS_CLEAR_BROWSING_DATA_WITH_SYNC
#define IDS_SETTINGS_CLEAR_BROWSING_DATA_WITH_SYNC_ERROR
#define IDS_SETTINGS_CLEAR_BROWSING_DATA_WITH_SYNC_PASSPHRASE_ERROR
#define IDS_SETTINGS_CLEAR_BROWSING_DATA_WITH_SYNC_PAUSED
#define IDS_SETTINGS_CLEAR_BROWSING_HISTORY
#define IDS_SETTINGS_CLEAR_COOKIES_AND_SITE_DATA_SUMMARY_BASIC
#define IDS_SETTINGS_CLEAR_COOKIES_AND_SITE_DATA_SUMMARY_BASIC_WITH_EXCEPTION
#define IDS_SETTINGS_CLEAR_BROWSING_HISTORY_SUMMARY
#define IDS_SETTINGS_CLEAR_BROWSING_HISTORY_SUMMARY_SIGNED_IN
#define IDS_SETTINGS_CLEAR_BROWSING_HISTORY_SUMMARY_SYNCED
#define IDS_SETTINGS_CLEAR_DOWNLOAD_HISTORY
#define IDS_SETTINGS_CLEAR_CACHE
#define IDS_SETTINGS_CLEAR_COOKIES
#define IDS_SETTINGS_CLEAR_COOKIES_FLASH
#define IDS_SETTINGS_CLEAR_PASSWORDS
#define IDS_SETTINGS_CLEAR_FORM_DATA
#define IDS_SETTINGS_CLEAR_HOSTED_APP_DATA
#define IDS_SETTINGS_CLEAR_PERIOD_HOUR
#define IDS_SETTINGS_CLEAR_PERIOD_24_HOURS
#define IDS_SETTINGS_CLEAR_PERIOD_7_DAYS
#define IDS_SETTINGS_CLEAR_PERIOD_FOUR_WEEKS
#define IDS_SETTINGS_CLEAR_PERIOD_EVERYTHING
#define IDS_SETTINGS_NOTIFICATION_WARNING
#define IDS_SETTINGS_PRINTING
#define IDS_SETTINGS_PRINTING_CLOUD_PRINT_LEARN_MORE_LABEL
#define IDS_SETTINGS_PRINTING_NOTIFICATIONS_LABEL
#define IDS_SETTINGS_PRINTING_MANAGE_CLOUD_PRINT_DEVICES
#define IDS_SETTINGS_PRINTING_LOCAL_PRINTERS_TITLE
#define IDS_SETTINGS_PRINTING_CLOUD_PRINTERS
#define IDS_SETTINGS_DOWNLOADS
#define IDS_SETTINGS_DOWNLOAD_LOCATION
#define IDS_SETTINGS_CHANGE_DOWNLOAD_LOCATION
#define IDS_SETTINGS_PROMPT_FOR_DOWNLOAD
#define IDS_SETTINGS_DISCONNECT_GOOGLE_DRIVE
#define IDS_SETTINGS_OPEN_FILE_TYPES_AUTOMATICALLY
#define IDS_SETTINGS_ON_STARTUP
#define IDS_SETTINGS_ON_STARTUP_OPEN_NEW_TAB
#define IDS_SETTINGS_ON_STARTUP_CONTINUE
#define IDS_SETTINGS_ON_STARTUP_OPEN_SPECIFIC
#define IDS_SETTINGS_ON_STARTUP_USE_CURRENT
#define IDS_SETTINGS_ON_STARTUP_ADD_NEW_PAGE
#define IDS_SETTINGS_ON_STARTUP_EDIT_PAGE
#define IDS_SETTINGS_ON_STARTUP_SITE_URL
#define IDS_SETTINGS_ON_STARTUP_REMOVE
#define IDS_SETTINGS_ON_STARTUP_PAGE_TOOLTIP
#define IDS_SETTINGS_INVALID_URL
#define IDS_SETTINGS_URL_TOOL_LONG
#define IDS_SETTINGS_LANGUAGES_PAGE_TITLE
#define IDS_SETTINGS_LANGUAGES_LANGUAGES_LIST_TITLE
#define IDS_SETTINGS_LANGUAGE_SEARCH
#define IDS_SETTINGS_LANGUAGES_EXPAND_ACCESSIBILITY_LABEL
#define IDS_SETTINGS_LANGUAGES_LANGUAGES_LIST_ORDERING_INSTRUCTIONS
#define IDS_SETTINGS_LANGUAGES_LANGUAGES_LIST_MOVE_TO_TOP
#define IDS_SETTINGS_LANGUAGES_LANGUAGES_LIST_MOVE_UP
#define IDS_SETTINGS_LANGUAGES_LANGUAGES_LIST_MOVE_DOWN
#define IDS_SETTINGS_LANGUAGES_LANGUAGES_LIST_REMOVE
#define IDS_SETTINGS_LANGUAGES_LANGUAGES_ADD
#define IDS_SETTINGS_LANGUAGES_OFFER_TO_TRANSLATE_IN_THIS_LANGUAGE
#define IDS_SETTINGS_LANGUAGES_OFFER_TO_ENABLE_TRANSLATE
#define IDS_SETTINGS_LANGUAGES_TRANSLATE_TARGET
#define IDS_SETTINGS_LANGUAGES_MANAGE_LANGUAGES_TITLE
#define IDS_SETTINGS_LANGUAGES_ALL_LANGUAGES
#define IDS_SETTINGS_LANGUAGES_ENABLED_LANGUAGES
#define IDS_SETTINGS_LANGUAGES_SPELL_CHECK_TITLE
#define IDS_SETTINGS_LANGUAGES_SPELL_CHECK_BASIC_LABEL
#define IDS_SETTINGS_LANGUAGES_SPELL_CHECK_ENHANCED_LABEL
#define IDS_SETTINGS_LANGUAGES_SPELL_CHECK_ENHANCED_DESCRIPTION
#define IDS_SETTING_LANGUAGES_SPELL_CHECK_DISABLED_REASON
#define IDS_SETTINGS_LANGUAGES_SPELL_CHECK_LANGUAGES_LIST_TITLE
#define IDS_SETTINGS_LANGUAGES_SPELL_CHECK_MANAGE
#define IDS_SETTINGS_LANGUAGES_EDIT_DICTIONARY_TITLE
#define IDS_SETTINGS_LANGUAGES_ADD_DICTIONARY_WORD
#define IDS_SETTINGS_LANGUAGES_ADD_DICTIONARY_WORD_BUTTON
#define IDS_SETTINGS_LANGUAGES_ADD_DICTIONARY_WORD_DUPLICATE_ERROR
#define IDS_SETTINGS_LANGUAGES_ADD_DICTIONARY_WORD_LENGTH_ERROR
#define IDS_SETTINGS_LANGUAGES_DELETE_DICTIONARY_WORD_BUTTON
#define IDS_SETTINGS_LANGUAGES_DICTIONARY_WORDS
#define IDS_SETTINGS_LANGUAGES_DICTIONARY_WORDS_NONE
#define IDS_SETTINGS_LANGUAGES_DICTIONARY_DOWNLOAD_FAILED
#define IDS_SETTINGS_LANGUAGES_DICTIONARY_DOWNLOAD_FAILED_HELP
#define IDS_SETTINGS_PRIVACY
#define IDS_SETTINGS_PRIVACY_MORE
#define IDS_SETTINGS_LINKDOCTOR_PREF
#define IDS_SETTINGS_LINKDOCTOR_PREF_DESC
#define IDS_SETTINGS_SUGGEST_PREF
#define IDS_SETTINGS_SUGGEST_PREF_DESC
#define IDS_SETTINGS_NETWORK_PREDICTION_ENABLED_LABEL
#define IDS_SETTINGS_NETWORK_PREDICTION_ENABLED_DESC
#define IDS_SETTINGS_SAFEBROWSING_ENABLEPROTECTION
#define IDS_SETTINGS_SAFEBROWSING_ENABLEPROTECTION_DESC
#define IDS_SETTINGS_SAFEBROWSING_ENABLE_REPORTING
#define IDS_SETTINGS_SAFEBROWSING_ENABLE_REPORTING_DESC
#define IDS_SETTINGS_SPELLING_PREF
#define IDS_SETTINGS_ENABLE_LOGGING_PREF
#define IDS_SETTINGS_ENABLE_LOGGING_PREF_DESC
#define IDS_SETTINGS_ENABLE_URL_KEYED_ANONYMIZED_DATA_COLLECTION
#define IDS_SETTINGS_ENABLE_URL_KEYED_ANONYMIZED_DATA_COLLECTION_DESC
#define IDS_SETTINGS_ENABLE_DO_NOT_TRACK
#define IDS_SETTINGS_ENABLE_DO_NOT_TRACK_DIALOG_TITLE
#define IDS_SETTINGS_ENABLE_DO_NOT_TRACK_DIALOG_TEXT
#define IDS_SETTINGS_ENABLE_CONTENT_PROTECTION_ATTESTATION
#define IDS_SETTINGS_WAKE_ON_WIFI_DESCRIPTION
#define IDS_SETTINGS_MANAGE_CERTIFICATES
#define IDS_SETTINGS_MANAGE_CERTIFICATES_DESCRIPTION
#define IDS_SETTINGS_CONTENT_SETTINGS
#define IDS_SETTINGS_SITE_SETTINGS
#define IDS_SETTINGS_SITE_SETTINGS_DESCRIPTION
#define IDS_SETTINGS_CLEAR_DATA
#define IDS_SETTINGS_CLEAR_BROWSING_DATA
#define IDS_SETTINGS_CLEAR_DATA_DESCRIPTION
#define IDS_SETTINGS_TITLE_AND_COUNT
#define IDS_SETTINGS_SYNC_AND_GOOGLE_SERVICES_PRIVACY_DESC_UNIFIED_CONSENT
#define IDS_SETTINGS_RESET
#define IDS_SETTINGS_RESET_SETTINGS_TRIGGER
#define IDS_SETTINGS_RESET_AUTOMATED_DIALOG_TITLE
#define IDS_SETTINGS_RESET_BANNER_TEXT
#define IDS_SETTINGS_RESET_BANNER_RESET_BUTTON_TEXT
#define IDS_SETTINGS_SEARCH
#define IDS_SETTINGS_SEARCH_EXPLANATION
#define IDS_SETTINGS_SEARCH_MANAGE_SEARCH_ENGINES
#define IDS_SETTINGS_SEARCH_ENGINES
#define IDS_SETTINGS_SEARCH_ENGINES_SEARCH
#define IDS_SETTINGS_SEARCH_ENGINES_ADD_SEARCH_ENGINE
#define IDS_SETTINGS_SEARCH_ENGINES_EDIT_SEARCH_ENGINE
#define IDS_SETTINGS_SEARCH_ENGINES_DEFAULT_ENGINES
#define IDS_SETTINGS_SEARCH_ENGINES_OTHER_ENGINES
#define IDS_SETTINGS_SEARCH_ENGINES_NO_OTHER_ENGINES
#define IDS_SETTINGS_SEARCH_ENGINES_EXTENSION_ENGINES
#define IDS_SETTINGS_SEARCH_ENGINES_SEARCH_ENGINE
#define IDS_SETTINGS_SEARCH_ENGINES_KEYWORD
#define IDS_SETTINGS_SEARCH_ENGINES_QUERY_URL
#define IDS_SETTINGS_SEARCH_ENGINES_QUERY_URL_EXPLANATION
#define IDS_SETTINGS_SEARCH_ENGINES_MAKE_DEFAULT
#define IDS_SETTINGS_SEARCH_ENGINES_REMOVE_FROM_LIST
#define IDS_SETTINGS_SEARCH_ENGINES_MANAGE_EXTENSION
#define IDS_SETTINGS_EXCEPTIONS_EMBEDDED_ON_HOST
#define IDS_SETTINGS_EXCEPTIONS_EMBEDDED_ON_ANY_HOST
#define IDS_SETTINGS_SITE_SETTINGS_CATEGORY
#define IDS_SETTINGS_SITE_SETTINGS_ALL_SITES
#define IDS_SETTINGS_SITE_SETTINGS_ALL_SITES_DESCRIPTION
#define IDS_SETTINGS_SITE_SETTINGS_ALL_SITES_SEARCH
#define IDS_SETTINGS_SITE_SETTINGS_ALL_SITES_SORT
#define IDS_SETTINGS_SITE_SETTINGS_ALL_SITES_SORT_METHOD_MOST_VISITED
#define IDS_SETTINGS_SITE_SETTINGS_ALL_SITES_SORT_METHOD_STORAGE
#define IDS_SETTINGS_SITE_SETTINGS_ALL_SITES_SORT_METHOD_NAME
#define IDS_SETTINGS_SITE_SETTINGS_SITE_REPRESENTATION_SEPARATOR
#define IDS_SETTINGS_SITE_SETTINGS_ADS
#define IDS_SETTINGS_SITE_SETTINGS_AUTOMATIC_DOWNLOADS
#define IDS_SETTINGS_SITE_SETTINGS_BACKGROUND_SYNC
#define IDS_SETTINGS_SITE_SETTINGS_CAMERA
#define IDS_SETTINGS_SITE_SETTINGS_CAMERA_LABEL
#define IDS_SETTINGS_SITE_SETTINGS_CLIPBOARD
#define IDS_SETTINGS_SITE_SETTINGS_CLIPBOARD_ASK
#define IDS_SETTINGS_SITE_SETTINGS_CLIPBOARD_ASK_RECOMMENDED
#define IDS_SETTINGS_SITE_SETTINGS_CLIPBOARD_BLOCK
#define IDS_SETTINGS_SITE_SETTINGS_COOKIES
#define IDS_SETTINGS_SITE_SETTINGS_HANDLERS
#define IDS_SETTINGS_SITE_SETTINGS_LOCATION
#define IDS_SETTINGS_SITE_SETTINGS_MIC
#define IDS_SETTINGS_SITE_SETTINGS_MIC_LABEL
#define IDS_SETTINGS_SITE_SETTINGS_NOTIFICATIONS
#define IDS_SETTINGS_SITE_SETTINGS_IMAGES
#define IDS_SETTINGS_SITE_SETTINGS_INSECURE_CONTENT
#define IDS_SETTINGS_SITE_SETTINGS_INSECURE_CONTENT_BLOCK
#define IDS_SETTINGS_SITE_SETTINGS_JAVASCRIPT
#define IDS_SETTINGS_SITE_SETTINGS_FLASH
#define IDS_SETTINGS_SITE_SETTINGS_PAYMENT_HANDLER
#define IDS_SETTINGS_SITE_SETTINGS_PAYMENT_HANDLER_ALLOW
#define IDS_SETTINGS_SITE_SETTINGS_PAYMENT_HANDLER_ALLOW_RECOMMENDED
#define IDS_SETTINGS_SITE_SETTINGS_PAYMENT_HANDLER_BLOCK
#define IDS_SETTINGS_SITE_SETTINGS_PDF_DOCUMENTS
#define IDS_SETTINGS_SITE_SETTINGS_PDF_DOWNLOAD_PDFS
#define IDS_SETTINGS_SITE_SETTINGS_POPUPS
#define IDS_SETTINGS_SITE_SETTINGS_PROTECTED_CONTENT
#define IDS_SETTINGS_SITE_SETTINGS_PROTECTED_CONTENT_IDENTIFIERS
#define IDS_SETTINGS_SITE_SETTINGS_PROTECTED_CONTENT_ENABLE
#define IDS_SETTINGS_SITE_SETTINGS_PROTECTED_CONTENT_IDENTIFIERS_EXPLANATION
#define IDS_SETTINGS_SITE_SETTINGS_PROTECTED_CONTENT_ENABLE_IDENTIFIERS
#define IDS_SETTINGS_SITE_SETTINGS_UNSANDBOXED_PLUGINS
#define IDS_SETTINGS_SITE_SETTINGS_MIDI_DEVICES
#define IDS_SETTINGS_SITE_SETTINGS_MIDI_DEVICES_ASK
#define IDS_SETTINGS_SITE_SETTINGS_MIDI_DEVICES_ASK_RECOMMENDED
#define IDS_SETTINGS_SITE_SETTINGS_MIDI_DEVICES_BLOCK
#define IDS_SETTINGS_SITE_SETTINGS_SOUND
#define IDS_SETTINGS_SITE_SETTINGS_SENSORS
#define IDS_SETTINGS_SITE_SETTINGS_MOTION_SENSORS
#define IDS_SETTINGS_SITE_SETTINGS_USB_DEVICES
#define IDS_SETTINGS_SITE_SETTINGS_USB_DEVICES_ASK
#define IDS_SETTINGS_SITE_SETTINGS_USB_DEVICES_ASK_RECOMMENDED
#define IDS_SETTINGS_SITE_SETTINGS_USB_DEVICES_BLOCK
#define IDS_SETTINGS_SITE_SETTINGS_SERIAL_PORTS
#define IDS_SETTINGS_SITE_SETTINGS_SERIAL_PORTS_ASK
#define IDS_SETTINGS_SITE_SETTINGS_SERIAL_PORTS_ASK_RECOMMENDED
#define IDS_SETTINGS_SITE_SETTINGS_SERIAL_PORTS_BLOCK
#define IDS_SETTINGS_SITE_SETTINGS_NATIVE_FILE_SYSTEM_WRITE
#define IDS_SETTINGS_SITE_SETTINGS_NATIVE_FILE_SYSTEM_WRITE_ASK
#define IDS_SETTINGS_SITE_SETTINGS_NATIVE_FILE_SYSTEM_WRITE_ASK_RECOMMENDED
#define IDS_SETTINGS_SITE_SETTINGS_NATIVE_FILE_SYSTEM_WRITE_BLOCK
#define IDS_SETTINGS_SITE_SETTINGS_REMOVE_ZOOM_LEVEL
#define IDS_SETTINGS_SITE_SETTINGS_ZOOM_LEVELS
#define IDS_SETTINGS_SITE_SETTINGS_MAY_SAVE_COOKIES
#define IDS_SETTINGS_SITE_SETTINGS_ASK_FIRST
#define IDS_SETTINGS_SITE_SETTINGS_ASK_FIRST_RECOMMENDED
#define IDS_SETTINGS_SITE_SETTINGS_ASK_BEFORE_ACCESSING
#define IDS_SETTINGS_SITE_SETTINGS_ASK_BEFORE_ACCESSING_RECOMMENDED
#define IDS_SETTINGS_SITE_SETTINGS_ASK_BEFORE_SENDING
#define IDS_SETTINGS_SITE_SETTINGS_ASK_BEFORE_SENDING_RECOMMENDED
#define IDS_SETTINGS_SITE_SETTINGS_AUTOMATICALLY_BLOCKED_NOTIFICATIONS
#define IDS_SETTINGS_SITE_SETTINGS_SHOW_BLOCKED_NOTIFICATIONS_INDICATOR
#define IDS_SETTINGS_SITE_SETTINGS_ENABLE_QUIET_NOTIFICATION_PROMPTS
#define IDS_SETTINGS_SITE_SETTINGS_ENABLE_QUIET_NOTIFICATION_PROMPTS_DESCRIPTION
#define IDS_SETTINGS_SITE_SETTINGS_NOTIFICATIONS_BLOCK
#define IDS_SETTINGS_SITE_SETTINGS_NOTIFICATIONS_ASK
#define IDS_SETTINGS_SITE_SETTINGS_DONT_SHOW_IMAGES
#define IDS_SETTINGS_SITE_SETTINGS_SHOW_ALL
#define IDS_SETTINGS_SITE_SETTINGS_SHOW_ALL_RECOMMENDED
#define IDS_SETTINGS_SITE_SETTINGS_COOKIES_ALLOW_SITES
#define IDS_SETTINGS_SITE_SETTINGS_COOKIES_ALLOW_SITES_RECOMMENDED
#define IDS_SETTINGS_SITE_SETTINGS_FLASH_BLOCK
#define IDS_SETTINGS_SITE_SETTINGS_FLASH_BLOCK_RECOMMENDED
#define IDS_SETTINGS_SITE_SETTINGS_FLASH_PERMISSIONS_ARE_EPHEMERAL
#define IDS_SETTINGS_SITE_SETTINGS_ALLOW_RECENTLY_CLOSED_SITES
#define IDS_SETTINGS_SITE_SETTINGS_ALLOW_RECENTLY_CLOSED_SITES_RECOMMENDED
#define IDS_SETTINGS_SITE_SETTINGS_BACKGROUND_SYNC_BLOCKED
#define IDS_SETTINGS_SITE_SETTINGS_HANDLERS_ASK
#define IDS_SETTINGS_SITE_SETTINGS_HANDLERS_ASK_RECOMMENDED
#define IDS_SETTINGS_SITE_SETTINGS_HANDLERS_BLOCKED
#define IDS_SETTINGS_SITE_SETTINGS_ADS_BLOCK
#define IDS_SETTINGS_SITE_SETTINGS_ADS_BLOCK_RECOMMENDED
#define IDS_SETTINGS_SITE_SETTINGS_SOUND_ALLOW
#define IDS_SETTINGS_SITE_SETTINGS_SOUND_ALLOW_RECOMMENDED
#define IDS_SETTINGS_SITE_SETTINGS_SOUND_BLOCK
#define IDS_SETTINGS_SITE_SETTINGS_SENSORS_ALLOW
#define IDS_SETTINGS_SITE_SETTINGS_MOTION_SENSORS_ALLOW
#define IDS_SETTINGS_SITE_SETTINGS_SENSORS_BLOCK
#define IDS_SETTINGS_SITE_SETTINGS_MOTION_SENSORS_BLOCK
#define IDS_SETTINGS_SITE_SETTINGS_AUTOMATIC_DOWNLOAD_ASK
#define IDS_SETTINGS_SITE_SETTINGS_AUTOMATIC_DOWNLOAD_ASK_RECOMMENDED
#define IDS_SETTINGS_SITE_SETTINGS_AUTOMATIC_DOWNLOAD_BLOCK
#define IDS_SETTINGS_SITE_SETTINGS_UNSANDBOXED_PLUGINS_ASK
#define IDS_SETTINGS_SITE_SETTINGS_UNSANDBOXED_PLUGINS_ASK_RECOMMENDED
#define IDS_SETTINGS_SITE_SETTINGS_UNSANDBOXED_PLUGINS_BLOCK
#define IDS_SETTINGS_SITE_SETTINGS_ALLOWED
#define IDS_SETTINGS_SITE_SETTINGS_ALLOWED_RECOMMENDED
#define IDS_SETTINGS_SITE_SETTINGS_BLOCKED
#define IDS_SETTINGS_SITE_SETTINGS_BLOCKED_RECOMMENDED
#define IDS_SETTINGS_SITE_SETTINGS_ALLOW
#define IDS_SETTINGS_SITE_SETTINGS_BLOCK
#define IDS_SETTINGS_SITE_SETTINGS_BLOCK_SOUND
#define IDS_SETTINGS_SITE_SETTINGS_SESSION_ONLY
#define IDS_SETTINGS_SITE_SETTINGS_SITE_URL
#define IDS_SETTINGS_SITE_SETTINGS_ASK_DEFAULT_MENU
#define IDS_SETTINGS_SITE_SETTINGS_ALLOW_DEFAULT_MENU
#define IDS_SETTINGS_SITE_SETTINGS_AUTOMATIC_DEFAULT_MENU
#define IDS_SETTINGS_SITE_SETTINGS_BLOCK_DEFAULT_MENU
#define IDS_SETTINGS_SITE_SETTINGS_MUTE_DEFAULT_MENU
#define IDS_SETTINGS_SITE_SETTINGS_ALLOW_MENU
#define IDS_SETTINGS_SITE_SETTINGS_BLOCK_MENU
#define IDS_SETTINGS_SITE_SETTINGS_ASK_MENU
#define IDS_SETTINGS_SITE_SETTINGS_MUTE_MENU
#define IDS_SETTINGS_SITE_SETTINGS_RESET_MENU
#define IDS_SETTINGS_SITE_SETTINGS_SESSION_ONLY_MENU
#define IDS_SETTINGS_SITE_SETTINGS_USAGE
#define IDS_SETTINGS_SITE_SETTINGS_USAGE_NONE
#define IDS_SETTINGS_SITE_SETTINGS_PERMISSIONS
#define IDS_SETTINGS_SITE_SETTINGS_SOURCE_DRM_DISABLED
#define IDS_SETTINGS_SITE_SETTINGS_ADS_BLOCK_BLACKLISTED_SINGULAR
#define IDS_SETTINGS_SITE_SETTINGS_ADS_BLOCK_NOT_BLACKLISTED_SINGULAR
#define IDS_SETTINGS_SITE_SETTINGS_SOURCE_KILL_SWITCH
#define IDS_SETTINGS_SITE_SETTINGS_SOURCE_INSECURE_ORIGIN
#define IDS_SETTINGS_SITE_SETTINGS_RESET_BUTTON
#define IDS_SETTINGS_SITE_SETTINGS_DELETE
#define IDS_SETTINGS_SITE_SETTINGS_GROUP_RESET
#define IDS_SETTINGS_SITE_SETTINGS_GROUP_DELETE
#define IDS_SETTINGS_SITE_SETTINGS_COOKIE_HEADER
#define IDS_SETTINGS_SITE_SETTINGS_COOKIE_LINK
#define IDS_SETTINGS_SITE_SETTINGS_COOKIE_REMOVE
#define IDS_SETTINGS_SITE_SETTINGS_COOKIE_REMOVE_ALL
#define IDS_SETTINGS_SITE_SETTINGS_COOKIE_REMOVE_ALL_SHOWN
#define IDS_SETTINGS_SITE_SETTINGS_COOKIE_REMOVE_ALL_THIRD_PARTY
#define IDS_SETTINGS_SITE_SETTINGS_THIRD_PARTY_COOKIE_REMOVE_DIALOG_TITLE
#define IDS_SETTINGS_SITE_SETTINGS_THIRD_PARTY_COOKIE_REMOVE_CONFIRMATION
#define IDS_SETTINGS_SITE_SETTINGS_CLEAR_THIRD_PARTY_COOKIES
#define IDS_SETTINGS_SITE_SETTINGS_THIRD_PARTY_COOKIES_EXCEPTION_LABEL
#define IDS_SETTINGS_SITE_SETTINGS_COOKIE_REMOVE_DIALOG_TITLE
#define IDS_SETTINGS_SITE_SETTINGS_COOKIE_SUBPAGE
#define IDS_SETTINGS_SITE_SETTINGS_SITE_RESET_CONFIRMATION
#define IDS_SETTINGS_SITE_SETTINGS_SITE_CLEAR_STORAGE_DIALOG_TITLE
#define IDS_SETTINGS_SITE_SETTINGS_SITE_CLEAR_STORAGE_CONFIRMATION
#define IDS_SETTINGS_SITE_SETTINGS_SITE_CLEAR_STORAGE_CONFIRMATION_NEW
#define IDS_SETTINGS_SITE_SETTINGS_SITE_CLEAR_STORAGE_SIGN_OUT
#define IDS_SETTINGS_SITE_SETTINGS_SITE_CLEAR_STORAGE_OFFLINE_DATA
#define IDS_SETTINGS_SITE_SETTINGS_SITE_CLEAR_STORAGE_APPS
#define IDS_SETTINGS_SITE_SETTINGS_SITE_GROUP_RESET_DIALOG_TITLE
#define IDS_SETTINGS_SITE_SETTINGS_SITE_GROUP_RESET_CONFIRMATION
#define IDS_SETTINGS_SITE_SETTINGS_SITE_GROUP_DELETE_DIALOG_TITLE
#define IDS_SETTINGS_SITE_SETTINGS_SITE_GROUP_DELETE_CONFIRMATION
#define IDS_SETTINGS_SITE_SETTINGS_SITE_GROUP_DELETE_CONFIRMATION_NEW
#define IDS_SETTINGS_SITE_SETTINGS_SITE_GROUP_DELETE_SIGN_OUT
#define IDS_SETTINGS_SITE_SETTINGS_SITE_GROUP_DELETE_OFFLINE_DATA
#define IDS_SETTINGS_SITE_SETTINGS_SITE_GROUP_DELETE_APPS
#define IDS_SETTINGS_SITE_SETTINGS_COOKIE_REMOVE_MULTIPLE
#define IDS_SETTINGS_SITE_SETTINGS_COOKIE_REMOVE_SITE
#define IDS_SETTINGS_SITE_SETTINGS_COOKIES_CLEAR_ALL
#define IDS_SETTINGS_SITE_SETTINGS_SITE_RESET_ALL
#define IDS_SETTINGS_SITE_SETTINGS_SITE_CLEAR_STORAGE
#define IDS_SETTINGS_SITE_SETTINGS_COOKIE_SEARCH
#define IDS_SETTINGS_SITE_SETTINGS_THIRD_PARTY_COOKIE
#define IDS_SETTINGS_SITE_SETTINGS_THIRD_PARTY_COOKIE_SUBLABEL
#define IDS_SETTINGS_SITE_SETTINGS_ADOBE_FLASH_SETTINGS
#define IDS_SETTINGS_SITE_SETTINGS_HANDLER_IS_DEFAULT
#define IDS_SETTINGS_SITE_SETTINGS_HANDLER_SET_DEFAULT
#define IDS_SETTINGS_SITE_SETTINGS_REMOVE
#define IDS_SETTINGS_SITE_SETTINGS_INCOGNITO_ONLY
#define IDS_SETTINGS_SITE_SETTINGS_INCOGNITO
#define IDS_SETTINGS_SITE_SETTINGS_INCOGNITO_EMBEDDED
#define IDS_SETTINGS_SITE_SETTINGS_NO_ZOOMED_SITES
#define IDS_SETTINGS_SITE_NO_SITES_ADDED
#define IDS_SETTINGS_SITE_SETTINGS_BLOCK_AUTOPLAY
#define IDS_SETTINGS_SITE_SETTINGS_EMPTY_ALL_SITES_PAGE
#define IDS_SETTINGS_SITE_SETTINGS_NO_SITES_FOUND
#define IDS_SETTINGS_SITE_SETTINGS_BLUETOOTH_SCANNING
#define IDS_SETTINGS_SITE_SETTINGS_BLUETOOTH_SCANNING_ASK
#define IDS_SETTINGS_SITE_SETTINGS_BLUETOOTH_SCANNING_ASK_RECOMMENDED
#define IDS_SETTINGS_SITE_SETTINGS_BLUETOOTH_SCANNING_BLOCK
#define IDS_SETTINGS_NO_USB_DEVICES_FOUND
#define IDS_SETTINGS_NO_SERIAL_PORTS_FOUND
#define IDS_SETTINGS_ADD_SITE_EXCEPTION_PLACEHOLDER
#define IDS_SETTINGS_ADD_SITE_TITLE
#define IDS_SETTINGS_EDIT_SITE_TITLE
#define IDS_SETTINGS_ADD_SITE
#define IDS_SETTINGS_COOKIES_COOKIE_NAME_LABEL
#define IDS_SETTINGS_COOKIES_COOKIE_CONTENT_LABEL
#define IDS_SETTINGS_COOKIES_COOKIE_DOMAIN_LABEL
#define IDS_SETTINGS_COOKIES_COOKIE_PATH_LABEL
#define IDS_SETTINGS_COOKIES_COOKIE_SENDFOR_LABEL
#define IDS_SETTINGS_COOKIES_COOKIE_ACCESSIBLE_TO_SCRIPT_LABEL
#define IDS_SETTINGS_COOKIES_COOKIE_CREATED_LABEL
#define IDS_SETTINGS_COOKIES_COOKIE_EXPIRES_LABEL
#define IDS_SETTINGS_COOKIES_APPLICATION_CACHE
#define IDS_SETTINGS_COOKIES_FLASH_LSO
#define IDS_SETTINGS_COOKIES_APPLICATION_CACHE_MANIFEST_LABEL
#define IDS_SETTINGS_SITE_SETTINGS_NUM_COOKIES
#define IDS_SETTINGS_COOKIES_LOCAL_STORAGE_ORIGIN_LABEL
#define IDS_SETTINGS_COOKIES_LOCAL_STORAGE_SIZE_ON_DISK_LABEL
#define IDS_SETTINGS_COOKIES_LOCAL_STORAGE_LAST_MODIFIED_LABEL
#define IDS_SETTINGS_COOKIES_DATABASE_STORAGE
#define IDS_SETTINGS_COOKIES_LOCAL_STORAGE
#define IDS_SETTINGS_COOKIES_MEDIA_LICENSE
#define IDS_SETTINGS_COOKIES_FILE_SYSTEM
#define IDS_SETTINGS_COOKIES_FILE_SYSTEM_TEMPORARY_USAGE_LABEL
#define IDS_SETTINGS_COOKIES_FILE_SYSTEM_PERSISTENT_USAGE_LABEL
#define IDS_SETTINGS_COOKIES_SERVICE_WORKER
#define IDS_SETTINGS_COOKIES_SHARED_WORKER
#define IDS_SETTINGS_COOKIES_SHARED_WORKER_WORKER_LABEL
#define IDS_SETTINGS_COOKIES_CACHE_STORAGE
#define IDS_SETTINGS_PEOPLE
#define IDS_SETTINGS_PEOPLE_MANAGE_OTHER_PEOPLE
#define IDS_SETTINGS_CHANGE_PICTURE_PROFILE_PHOTO
#define IDS_SETTINGS_PEOPLE_SIGN_OUT
#define IDS_SETTINGS_PEOPLE_DOMAIN_MANAGED_PROFILE
#define IDS_SETTINGS_PEOPLE_SIGN_IN
#define IDS_SETTINGS_PEOPLE_SIGN_IN_PROMPT
#define IDS_SETTINGS_PEOPLE_SYNC_ANOTHER_ACCOUNT
#define IDS_SETTINGS_PEOPLE_SYNCING_TO_ACCOUNT
#define IDS_SETTINGS_PEOPLE_SYNC_TURN_OFF
#define IDS_SETTINGS_PEOPLE_SYNC_NOT_WORKING
#define IDS_SETTINGS_PEOPLE_SYNC_PASSWORDS_NOT_WORKING
#define IDS_SETTINGS_PEOPLE_SYNC_PAUSED
#define IDS_SETTINGS_SYNC_DISCONNECT_MANAGED_PROFILE_EXPLANATION
#define IDS_SETTINGS_EDIT_PERSON
#define IDS_SETTINGS_PROFILE_SHORTCUT_TOGGLE_LABEL
#define IDS_SETTINGS_TURN_OFF_SYNC_AND_SIGN_OUT_DIALOG_TITLE
#define IDS_SETTINGS_TURN_OFF_SYNC_DIALOG_MANAGED_CONFIRM
#define IDS_SETTINGS_TURN_OFF_SYNC_DIALOG_CHECKBOX
#define IDS_SETTINGS_SYNC_SETTINGS_SAVED_TOAST_LABEL
#define IDS_SETTINGS_SYNC_OVERVIEW
#define IDS_SETTINGS_SYNC_DISCONNECT_EXPLANATION
#define IDS_SETTINGS_SYNC_DISCONNECT_AND_SIGN_OUT_EXPLANATION
#define IDS_SETTINGS_SYNC_DISCONNECT_EXPAND_ACCESSIBILITY_LABEL
#define IDS_SETTINGS_SYNC_DISCONNECT_DELETE_PROFILE
#define IDS_SETTINGS_SYNC_DISCONNECT_CONFIRM
#define IDS_SETTINGS_SYNC
#define IDS_SETTINGS_NON_PERSONALIZED_SERVICES_SECTION_LABEL
#define IDS_SETTINGS_SYNC_SYNC_AND_NON_PERSONALIZED_SERVICES
#define IDS_SETTINGS_SYNC_ADVANCED_PAGE_TITLE
#define IDS_SETTINGS_SYNC_LOADING
#define IDS_SETTINGS_SYNC_WILL_START
#define IDS_SETTINGS_SYNC_SETTINGS_CANCEL_SYNC
#define IDS_SETTINGS_SYNC_SETUP_CANCEL_DIALOG_TITLE
#define IDS_SETTINGS_SYNC_SETUP_CANCEL_DIALOG_BODY
#define IDS_SETTINGS_SYNC_TIMEOUT
#define IDS_SETTINGS_SYNC_EVERYTHING_CHECKBOX_LABEL
#define IDS_SETTINGS_MANAGE_GOOGLE_ACCOUNT
#define IDS_SETTINGS_APPS_CHECKBOX_LABEL
#define IDS_SETTINGS_EXTENSIONS_CHECKBOX_LABEL
#define IDS_SETTINGS_SETTINGS_CHECKBOX_LABEL
#define IDS_SETTINGS_AUTOFILL_CHECKBOX_LABEL
#define IDS_SETTINGS_HISTORY_CHECKBOX_LABEL
#define IDS_SETTINGS_THEMES_AND_WALLPAPERS_CHECKBOX_LABEL
#define IDS_SETTINGS_BOOKMARKS_CHECKBOX_LABEL
#define IDS_SETTINGS_PASSWORDS_CHECKBOX_LABEL
#define IDS_SETTINGS_OPEN_TABS_CHECKBOX_LABEL
#define IDS_DRIVE_SUGGEST_PREF
#define IDS_SETTINGS_USER_EVENTS_CHECKBOX_LABEL
#define IDS_SETTINGS_USER_EVENTS_CHECKBOX_TEXT
#define IDS_SETTINGS_MANAGE_SYNCED_DATA_TITLE
#define IDS_SETTINGS_MANAGE_SYNCED_DATA_TITLE_UNIFIED_CONSENT
#define IDS_SETTINGS_EXISTING_PASSPHRASE_TITLE
#define IDS_SETTINGS_ENCRYPTION_OPTIONS
#define IDS_SETTINGS_ENCRYPT_WITH_GOOGLE_CREDENTIALS_LABEL
#define IDS_SETTINGS_ENCRYPT_WITH_SYNC_PASSPHRASE_LABEL
#define IDS_SETTINGS_PASSPHRASE_EXPLANATION_TEXT
#define IDS_SETTINGS_PASSPHRASE_RESET_HINT_ENCRYPTION
#define IDS_SETTINGS_PASSPHRASE_RESET_HINT_TOGGLE
#define IDS_SETTINGS_EMPTY_PASSPHRASE_ERROR
#define IDS_SETTINGS_MISMATCHED_PASSPHRASE_ERROR
#define IDS_SETTINGS_INCORRECT_PASSPHRASE_ERROR
#define IDS_SETTINGS_PASSPHRASE_RECOVER
#define IDS_SETTINGS_PASSPHRASE_PLACEHOLDER
#define IDS_SETTINGS_PASSPHRASE_CONFIRMATION_PLACEHOLDER
#define IDS_SETTINGS_SUBMIT_PASSPHRASE
#define IDS_SETTINGS_USE_DEFAULT_SETTINGS
#define IDS_SETTINGS_PERSONALIZE_GOOGLE_SERVICES_TITLE
#define IDS_SETTINGS_IMPORT_SETTINGS_TITLE
#define IDS_SETTINGS_IMPORT_FROM_LABEL
#define IDS_SETTINGS_IMPORT_ITEMS_LABEL
#define IDS_SETTINGS_IMPORT_LOADING_PROFILES
#define IDS_SETTINGS_IMPORT_HISTORY_CHECKBOX
#define IDS_SETTINGS_IMPORT_FAVORITES_CHECKBOX
#define IDS_SETTINGS_IMPORT_PASSWORDS_CHECKBOX
#define IDS_SETTINGS_IMPORT_SEARCH_ENGINES_CHECKBOX
#define IDS_SETTINGS_IMPORT_AUTOFILL_FORM_DATA_CHECKBOX
#define IDS_SETTINGS_IMPORT_CHOOSE_FILE
#define IDS_SETTINGS_IMPORT_COMMIT
#define IDS_SETTINGS_IMPORT_SUCCESS
#define IDS_SETTINGS_IMPORT_NO_PROFILE_FOUND
#define IDS_SETTINGS_WEB_CONTENT
#define IDS_SETTINGS_PAGE_ZOOM_LABEL
#define IDS_SETTINGS_FONT_SIZE_LABEL
#define IDS_SETTINGS_VERY_SMALL_FONT
#define IDS_SETTINGS_SMALL_FONT
#define IDS_SETTINGS_MEDIUM_FONT
#define IDS_SETTINGS_LARGE_FONT
#define IDS_SETTINGS_VERY_LARGE_FONT
#define IDS_SETTINGS_CUSTOM
#define IDS_SETTINGS_CUSTOMIZE_FONTS
#define IDS_SETTINGS_FONTS
#define IDS_SETTINGS_STANDARD_FONT_LABEL
#define IDS_SETTINGS_SERIF_FONT_LABEL
#define IDS_SETTINGS_SANS_SERIF_FONT_LABEL
#define IDS_SETTINGS_FIXED_WIDTH_FONT_LABEL
#define IDS_SETTINGS_MINIMUM_FONT_SIZE_LABEL
#define IDS_SETTINGS_TINY_FONT_SIZE
#define IDS_SETTINGS_HUGE_FONT_SIZE
#define IDS_SETTINGS_LOREM_IPSUM
#define IDS_SETTINGS_LOADING
#define IDS_SETTINGS_ADVANCED_FONT_SETTINGS
#define IDS_SETTINGS_OPEN_ADVANCED_FONT_SETTINGS
#define IDS_SETTINGS_QUICK_BROWN_FOX
#define IDS_SETTINGS_REQUIRES_WEB_STORE_EXTENSION
#define IDS_SETTINGS_SYSTEM
#define IDS_SETTINGS_SYSTEM_HARDWARE_ACCELERATION_LABEL
#define IDS_SETTINGS_SYSTEM_PROXY_SETTINGS_LABEL
#define IDS_SETTINGS_SYSTEM_PROXY_SETTINGS_EXTENSION_LABEL
#define IDS_SETTINGS_SYSTEM_PROXY_SETTINGS_POLICY_LABEL
#define IDS_SETTINGS_CHANGE_PASSWORD_TITLE
#define IDS_SETTINGS_CHANGE_PASSWORD_BUTTON
#define IDS_PAGE_NOT_AVAILABLE_FOR_GUEST_HEADING
#define IDS_SETTINGS_SECURITY_KEYS_TITLE
#define IDS_SETTINGS_SECURITY_KEYS_DESC
#define IDS_SETTINGS_SECURITY_KEYS_SET_PIN
#define IDS_SETTINGS_SECURITY_KEYS_SET_PIN_DESC
#define IDS_SETTINGS_SECURITY_KEYS_SET_PIN_INITIAL_TITLE
#define IDS_SETTINGS_SECURITY_KEYS_SET_PIN_CREATE_TITLE
#define IDS_SETTINGS_SECURITY_KEYS_SET_PIN_CHANGE_TITLE
#define IDS_SETTINGS_SECURITY_KEYS_RESET
#define IDS_SETTINGS_SECURITY_KEYS_RESET_DESC
#define IDS_SETTINGS_SECURITY_KEYS_RESET_TITLE
#define IDS_SETTINGS_SECURITY_KEYS_RESET_CONFIRM_TITLE
#define IDS_SETTINGS_SECURITY_KEYS_RESET_STEP1
#define IDS_SETTINGS_SECURITY_KEYS_RESET_STEP2
#define IDS_SETTINGS_SECURITY_KEYS_NO_RESET
#define IDS_SETTINGS_SECURITY_KEYS_RESET_ERROR
#define IDS_SETTINGS_SECURITY_KEYS_RESET_SUCCESS
#define IDS_SETTINGS_SECURITY_KEYS_RESET_NOTALLOWED
#define IDS_SETTINGS_SECURITY_KEYS_NO_PIN
#define IDS_SETTINGS_SECURITY_KEYS_CURRENT_PIN_INTRO
#define IDS_SETTINGS_SECURITY_KEYS_PIN_INCORRECT
#define IDS_SETTINGS_SECURITY_KEYS_PIN_INCORRECT_RETRIES_SIN
#define IDS_SETTINGS_SECURITY_KEYS_PIN_INCORRECT_RETRIES_PL
#define IDS_SETTINGS_SECURITY_KEYS_NEW_PIN
#define IDS_SETTINGS_SECURITY_KEYS_SET_PIN_CONFIRM
#define IDS_SETTINGS_SECURITY_KEYS_CURRENT_PIN
#define IDS_SETTINGS_SECURITY_KEYS_PIN
#define IDS_SETTINGS_SECURITY_KEYS_PIN_ERROR_TOO_SHORT_SMALL
#define IDS_SETTINGS_SECURITY_KEYS_PIN_ERROR_TOO_LONG
#define IDS_SETTINGS_SECURITY_KEYS_PIN_ERROR_INVALID
#define IDS_SETTINGS_SECURITY_KEYS_PIN_ERROR_MISMATCH
#define IDS_SETTINGS_SECURITY_KEYS_CONFIRM_PIN
#define IDS_SETTINGS_SECURITY_KEYS_PIN_SUCCESS
#define IDS_SETTINGS_SECURITY_KEYS_PIN_ERROR
#define IDS_SETTINGS_SECURITY_KEYS_PIN_HARD_LOCK
#define IDS_SETTINGS_SECURITY_KEYS_PIN_SOFT_LOCK
#define IDS_SETTINGS_SECURITY_KEYS_SHOW_PINS
#define IDS_SETTINGS_SECURITY_KEYS_HIDE_PINS
#define IDS_SETTINGS_SECURITY_KEYS_CREDENTIAL_MANAGEMENT_LABEL
#define IDS_SETTINGS_SECURITY_KEYS_CREDENTIAL_MANAGEMENT_DESC
#define IDS_SETTINGS_SECURITY_KEYS_CREDENTIAL_MANAGEMENT_DIALOG_TITLE
#define IDS_SETTINGS_SECURITY_KEYS_CREDENTIAL_WEBSITE
#define IDS_SETTINGS_SECURITY_KEYS_CREDENTIAL_USERNAME
#define IDS_SETTINGS_SECURITY_KEYS_CREDENTIAL_MANAGEMENT_NO_CREDENTIALS
#define IDS_SETTINGS_SECURITY_KEYS_NO_CREDENTIAL_MANAGEMENT
#define IDS_SETTINGS_SECURITY_KEYS_CREDENTIAL_MANAGEMENT_REMOVED
#define IDS_SETTINGS_SECURITY_KEYS_CREDENTIAL_MANAGEMENT_NO_PIN
#define IDS_SETTINGS_SECURITY_KEYS_CREDENTIAL_MANAGEMENT_ERROR
#define IDS_SETTINGS_SECURITY_KEYS_CREDENTIAL_MANAGEMENT_SUCCESS
#define IDS_SETTINGS_SECURITY_KEYS_CREDENTIAL_MANAGEMENT_FAILED
#define IDS_SETTINGS_SECURITY_KEYS_BIO_ENROLLMENT_SUBPAGE_LABEL
#define IDS_SETTINGS_SECURITY_KEYS_BIO_ENROLLMENT_SUBPAGE_DESCRIPTION
#define IDS_SETTINGS_SECURITY_KEYS_BIO_ENROLLMENT_DIALOG_TITLE
#define IDS_SETTINGS_SECURITY_KEYS_BIO_ENROLLMENT_ADD_TITLE
#define IDS_SETTINGS_SECURITY_KEYS_BIO_CHOOSE_NAME
#define IDS_SETTINGS_SECURITY_KEYS_BIO_NAME_LABEL
#define IDS_SETTINGS_SECURITY_KEYS_BIO_ENROLLMENT_NO_ENROLLMENTS_LABEL
#define IDS_SETTINGS_SECURITY_KEYS_BIO_ENROLLMENT_ENROLLMENTS_LABEL
#define IDS_SETTINGS_SECURITY_KEYS_BIO_ENROLLMENT_ENROLLING_LABEL
#define IDS_SETTINGS_SECURITY_KEYS_BIO_ENROLLMENT_ENROLLING_COMPLETE_LABEL
#define IDS_SETTINGS_SECURITY_KEYS_NO_BIOMETRIC_ENROLLMENT
#define IDS_SETTINGS_SECURITY_KEYS_BIO_ENROLLMENT_DELETE
#define IDS_SETTINGS_SECURITY_KEYS_TOUCH_TO_CONTINUE
#define IDS_SETTINGS_SECURITY_KEYS_PIN_PROMPT
#define IDS_EXTENSIONS_ALLOW_FILE_ACCESS
#define IDS_EXTENSIONS_ALLOW_ON_ALL_URLS
#define IDS_EXTENSIONS_ALLOW_ON_FOLLOWING_SITES
#define IDS_EXTENSIONS_VIEW_ACTIVITY_LOG
#define IDS_EXTENSIONS_BACKGROUND_PAGE
#define IDS_EXTENSIONS_CORRUPTED_EXTENSION
#define IDS_EXTENSIONS_ENABLE_ERROR_COLLECTION
#define IDS_EXTENSIONS_ERROR_NO_ERRORS_CODE_MESSAGE
#define IDS_EXTENSIONS_INSTALL_DROP_TARGET
#define IDS_EXTENSIONS_INSTALL_WARNINGS
#define IDS_EXTENSIONS_LOG_LEVEL_ERROR
#define IDS_EXTENSIONS_LOG_LEVEL_INFO
#define IDS_EXTENSIONS_LOG_LEVEL_WARN
#define IDS_EXTENSIONS_PATH
#define IDS_EXTENSIONS_RELOAD_TERMINATED
#define IDS_EXTENSIONS_REPAIR_CORRUPTED
#define IDS_EXTENSIONS_VIEW_IFRAME
#define IDS_EXTENSIONS_VIEW_INACTIVE
#define IDS_EXTENSIONS_VIEW_INCOGNITO
#define IDS_EXTENSIONS_DEVELOPER_MODE
#define IDS_EXTENSIONS_DISABLED_UPDATE_REQUIRED_BY_POLICY
#define IDS_EXTENSIONS_MENU_BUTTON_LABEL
#define IDS_EXTENSIONS_ERROR_PAGE_HEADING
#define IDS_EXTENSIONS_ERROR_ANONYMOUS_FUNCTION
#define IDS_EXTENSIONS_ERROR_CONTEXT
#define IDS_EXTENSIONS_ERROR_CONTEXT_UNKNOWN
#define IDS_EXTENSIONS_CLEAR_ACTIVITIES
#define IDS_EXTENSIONS_ERROR_CLEAR_ALL
#define IDS_EXTENSIONS_A11Y_CLEAR_ENTRY
#define IDS_EXTENSIONS_ERROR_STACK_TRACE
#define IDS_EXTENSIONS_ERROR_LINES_NOT_SHOWN
#define IDS_EXTENSIONS_HOST_PERMISSIONS_DESCRIPTION
#define IDS_EXTENSIONS_HOST_PERMISSIONS_EDIT
#define IDS_EXTENSIONS_ITEM_ERRORS
#define IDS_EXTENSIONS_ITEM_HOST_PERMISSIONS_HEADING
#define IDS_EXTENSIONS_HOST_ACCESS_ON_CLICK
#define IDS_EXTENSIONS_HOST_ACCESS_ON_SPECIFIC_SITES
#define IDS_EXTENSIONS_HOST_ACCESS_ON_ALL_SITES
#define IDS_EXTENSIONS_ITEM_ALLOWED_HOSTS
#define IDS_EXTENSIONS_ACCESSIBILITY_ERROR_LINE
#define IDS_EXTENSIONS_ACCESSIBILITY_ERROR_MULTI_LINE
#define IDS_EXTENSIONS_ACTIVITY_LOG_PAGE_HEADING
#define IDS_EXTENSIONS_ACTIVITY_LOG_SEARCH_LABEL
#define IDS_EXTENSIONS_ACTIVITY_LOG_TYPE_COLUMN
#define IDS_EXTENSIONS_ACTIVITY_LOG_NAME_COLUMN
#define IDS_EXTENSIONS_ACTIVITY_LOG_COUNT_COLUMN
#define IDS_EXTENSIONS_ACTIVITY_LOG_TIME_COLUMN
#define IDS_EXTENSIONS_ACTIVITY_LOG_HISTORY_TAB_HEADING
#define IDS_EXTENSIONS_ACTIVITY_LOG_STREAM_TAB_HEADING
#define IDS_EXTENSIONS_START_ACTIVITY_STREAM
#define IDS_EXTENSIONS_STOP_ACTIVITY_STREAM
#define IDS_EXTENSIONS_EMPTY_STREAM_STARTED
#define IDS_EXTENSIONS_EMPTY_STREAM_STOPPED
#define IDS_EXTENSIONS_ACTIVITY_ARGUMENTS_HEADING
#define IDS_EXTENSIONS_WEB_REQUEST_INFO_HEADING
#define IDS_EXTENSIONS_ACTIVITY_LOG_MORE_ACTIONS_LABEL
#define IDS_EXTENSIONS_ACTIVITY_LOG_EXPAND_ALL
#define IDS_EXTENSIONS_ACTIVITY_LOG_COLLAPSE_ALL
#define IDS_EXTENSIONS_ACTIVITY_LOG_EXPORT_HISTORY
#define IDS_EXTENSIONS_ITEM_ID
#define IDS_EXTENSIONS_ITEM_INSPECT_VIEWS
#define IDS_EXTENSIONS_ITEM_INSPECT_VIEWS_EXTRA
#define IDS_EXTENSIONS_ITEM_NO_ACTIVE_VIEWS
#define IDS_EXTENSIONS_ITEM_ALLOW_INCOGNITO
#define IDS_EXTENSIONS_ITEM_DEPENDENCIES
#define IDS_EXTENSIONS_DEPENDENT_ENTRY
#define IDS_EXTENSIONS_ITEM_DESCRIPTION
#define IDS_EXTENSIONS_ITEM_DETAILS
#define IDS_EXTENSIONS_EXTENSION_A11Y_ASSOCIATION
#define IDS_EXTENSIONS_APP_ICON
#define IDS_EXTENSIONS_EXTENSION_ICON
#define IDS_EXTENSIONS_ITEM_ID_HEADING
#define IDS_EXTENSIONS_EXTENSION_ENABLED
#define IDS_EXTENSIONS_APP_ENABLED
#define IDS_EXTENSIONS_ITEM_OFF
#define IDS_EXTENSIONS_ITEM_ON
#define IDS_EXTENSIONS_ITEM_EXTENSION_WEBSITE
#define IDS_EXTENSIONS_ITEM_CHROME_WEB_STORE
#define IDS_EXTENSIONS_ITEM_OPTIONS
#define IDS_EXTENSIONS_ITEM_PERMISSIONS
#define IDS_EXTENSIONS_ITEM_PERMISSIONS_EMPTY
#define IDS_EXTENSIONS_ITEM_REMOVE_EXTENSION
#define IDS_EXTENSIONS_ITEM_SITE_ACCESS
#define IDS_EXTENSIONS_ITEM_SITE_ACCESS_ADD_HOST
#define IDS_EXTENSIONS_ITEM_SITE_ACCESS_EMPTY
#define IDS_EXTENSIONS_ITEM_SOURCE
#define IDS_EXTENSIONS_ITEM_SOURCE_POLICY
#define IDS_EXTENSIONS_ITEM_SOURCE_SIDELOADED
#define IDS_EXTENSIONS_ITEM_SOURCE_UNPACKED
#define IDS_EXTENSIONS_ITEM_SOURCE_WEBSTORE
#define IDS_EXTENSIONS_ITEM_VERSION
#define IDS_EXTENSIONS_ITEM_RELOADED
#define IDS_EXTENSIONS_ITEM_RELOADING
#define IDS_EXTENSIONS_LOAD_ERROR_HEADING
#define IDS_EXTENSIONS_LOAD_ERROR_ERROR_LABEL
#define IDS_EXTENSIONS_LOAD_ERROR_FILE_LABEL
#define IDS_EXTENSIONS_LOAD_ERROR_COULD_NOT_LOAD_MANIFEST
#define IDS_EXTENSIONS_LOAD_ERROR_RETRY
#define IDS_EXTENSIONS_LOADING_ACTIVITIES
#define IDS_MISSING_OR_UNINSTALLED_EXTENSION
#define IDS_EXTENSIONS_NO_ACTIVITIES
#define IDS_EXTENSIONS_NO_INSTALLED_ITEMS
#define IDS_EXTENSIONS_NO_DESCRIPTION
#define IDS_EXTENSIONS_PACK_DIALOG_TITLE
#define IDS_EXTENSIONS_PACK_DIALOG_WARNING_TITLE
#define IDS_EXTENSIONS_PACK_DIALOG_ERROR_TITLE
#define IDS_EXTENSIONS_PACK_DIALOG_PROCEED_ANYWAY
#define IDS_EXTENSIONS_PACK_DIALOG_BROWSE_BUTTON
#define IDS_EXTENSIONS_PACK_DIALOG_EXTENSION_ROOT_LABEL
#define IDS_EXTENSIONS_PACK_DIALOG_KEY_FILE_LABEL
#define IDS_EXTENSIONS_PACK_DIALOG_CONFIRM_BUTTON
#define IDS_EXTENSIONS_TOOLBAR_TITLE
#define IDS_EXTENSIONS_SEARCH
#define IDS_EXTENSIONS_SHORTCUT_NOT_SET
#define IDS_EXTENSIONS_SHORTCUT_SCOPE_LABEL
#define IDS_EXTENSIONS_SHORTCUT_SCOPE_GLOBAL
#define IDS_EXTENSIONS_APPS_TITLE
#define IDS_EXTENSIONS_REMOVE
#define IDS_EXTENSIONS_RUNTIME_HOSTS_DIALOG_TITLE
#define IDS_EXTENSIONS_RUNTIME_HOSTS_DIALOG_INPUT_ERROR
#define IDS_EXTENSIONS_RUNTIME_HOSTS_DIALOG_INPUT_LABEL
#define IDS_EXTENSIONS_SIDEBAR_EXTENSIONS
#define IDS_EXTENSIONS_SIDEBAR_OPEN_CHROME_WEB_STORE
#define IDS_EXTENSIONS_SIDEBAR_KEYBOARD_SHORTCUTS
#define IDS_EXTENSIONS_TOOLBAR_LOAD_UNPACKED
#define IDS_EXTENSIONS_TOOLBAR_PACK
#define IDS_EXTENSIONS_TOOLBAR_UPDATE_NOW
#define IDS_EXTENSIONS_TOOLBAR_UPDATE_NOW_TOOLTIP
#define IDS_EXTENSIONS_TOOLBAR_UPDATE_DONE
#define IDS_EXTENSIONS_TOOLBAR_UPDATING_TOAST
#define IDS_EXTENSIONS_TYPE_A_SHORTCUT
#define IDS_EXTENSIONS_INCLUDE_START_MODIFIER
#define IDS_EXTENSIONS_TOO_MANY_MODIFIERS
#define IDS_EXTENSIONS_NEED_CHARACTER
#define IDS_WELCOME_NEXT
#define IDS_WELCOME_SKIP
#define IDS_WELCOME_BOOKMARK_ADDED
#define IDS_WELCOME_BOOKMARKS_ADDED
#define IDS_WELCOME_BOOKMARK_REMOVED
#define IDS_WELCOME_BOOKMARKS_REMOVED
#define IDS_DEFAULT_BROWSER_CHANGED
#define IDS_WELCOME_GOOGLE_APPS_DESCRIPTION
#define IDS_WELCOME_GOOGLE_GMAIL
#define IDS_WELCOME_GOOGLE_APPS_MAPS
#define IDS_WELCOME_GOOGLE_APPS_NEWS
#define IDS_WELCOME_GOOGLE_APPS_TRANSLATE
#define IDS_WELCOME_GOOGLE_APPS_YOUTUBE
#define IDS_WELCOME_NTP_BACKGROUND_DESCRIPTION
#define IDS_WELCOME_NTP_BACKGROUND_DEFAULT_TITLE
#define IDS_WELCOME_NTP_BACKGROUND_ART_TITLE
#define IDS_WELCOME_NTP_BACKGROUND_LANDSCAPE_TITLE
#define IDS_WELCOME_NTP_BACKGROUND_CITYSCAPE_TITLE
#define IDS_WELCOME_NTP_BACKGROUND_EARTH_TITLE
#define IDS_WELCOME_NTP_BACKGROUND_GEOMETRIC_SHAPES_TITLE
#define IDS_WELCOME_NTP_BACKGROUND_PHOTO_BY_LABEL
#define IDS_WELCOME_NTP_BACKGROUND_PREVIEW_UPDATED
#define IDS_WELCOME_NTP_BACKGROUND_RESET
#define IDS_WELCOME_SET_AS_DEFAULT_HEADER
#define IDS_WELCOME_SET_AS_DEFAULT_SUB_HEADER
#define IDS_WELCOME_SET_AS_DEFAULT_SET_AS_DEFAULT
#define IDS_WELCOME_LANDING_TITLE
#define IDS_WELCOME_LANDING_DESCRIPTION
#define IDS_WELCOME_LANDING_NEW_USER
#define IDS_WELCOME_LANDING_EXISTING_USER
#define IDS_WELCOME_SIGNIN_VIEW_HEADER
#define IDS_WELCOME_SIGNIN_VIEW_SUB_HEADER
#define IDS_WELCOME_SIGNIN_VIEW_SIGNIN
#define IDS_UTILITY_PROCESS_PRINTING_SERVICE_NAME
#define IDS_PRINT_INVALID_PRINTER_SETTINGS
#define IDS_PRINT_PREVIEW_TITLE
#define IDS_PRINT_PREVIEW_LOADING
#define IDS_PRINT_PREVIEW_FAILED
#define IDS_PRINT_PREVIEW_INVALID_PRINTER_SETTINGS
#define IDS_PRINT_PREVIEW_UNSUPPORTED_CLOUD_PRINTER
#define IDS_PRINT_PREVIEW_PRINT_BUTTON
#define IDS_PRINT_PREVIEW_SAVE_BUTTON
#define IDS_PRINT_PREVIEW_PRINTING
#define IDS_PRINT_PREVIEW_SAVING
#define IDS_PRINT_PREVIEW_OPTION_ALL_PAGES
#define IDS_PRINT_PREVIEW_OPTION_CUSTOM_PAGES
#define IDS_PRINT_PREVIEW_DESTINATION_LABEL
#define IDS_PRINT_PREVIEW_OPTION_BW
#define IDS_PRINT_PREVIEW_OPTION_COLLATE
#define IDS_PRINT_PREVIEW_OPTION_COLOR
#define IDS_PRINT_PREVIEW_OPTION_LANDSCAPE
#define IDS_PRINT_PREVIEW_OPTION_PORTRAIT
#define IDS_PRINT_PREVIEW_OPTION_TWO_SIDED
#define IDS_PRINT_PREVIEW_PRINT_ON_BOTH_SIDES_LABEL
#define IDS_PRINT_PREVIEW_OPTION_LONG_EDGE
#define IDS_PRINT_PREVIEW_OPTION_SHORT_EDGE
#define IDS_PRINT_PREVIEW_PAGES_LABEL
#define IDS_PRINT_PREVIEW_LAYOUT_LABEL
#define IDS_PRINT_PREVIEW_COPIES_LABEL
#define IDS_PRINT_PREVIEW_SCALING_LABEL
#define IDS_PRINT_PREVIEW_OPTION_DEFAULT_SCALING
#define IDS_PRINT_PREVIEW_OPTION_CUSTOM_SCALING
#define IDS_PRINT_PREVIEW_PAGES_PER_SHEET_LABEL
#define IDS_PRINT_PREVIEW_EXAMPLE_PAGE_RANGE_TEXT
#define IDS_PRINT_PREVIEW_PRINT_TO_PDF
#define IDS_PRINT_PREVIEW_PRINT_TO_GOOGLE_DRIVE
#define IDS_PRINT_PREVIEW_SUMMARY_FORMAT_SHORT
#define IDS_PRINT_PREVIEW_NEW_SUMMARY_FORMAT_SHORT
#define IDS_PRINT_PREVIEW_SHEETS_LABEL_PLURAL
#define IDS_PRINT_PREVIEW_SHEETS_LABEL_SINGULAR
#define IDS_PRINT_PREVIEW_PAGE_LABEL_SINGULAR
#define IDS_PRINT_PREVIEW_PAGE_LABEL_PLURAL
#define IDS_PRINT_PREVIEW_PAGE_RANGE_SYNTAX_INSTRUCTION
#define IDS_PRINT_PREVIEW_PAGE_RANGE_LIMIT_INSTRUCTION_WITH_VALUE
#define IDS_PRINT_PREVIEW_COPIES_INSTRUCTION
#define IDS_PRINT_PREVIEW_SCALING_INSTRUCTION
#define IDS_PRINT_PREVIEW_PRINT_PAGES_LABEL
#define IDS_PRINT_PREVIEW_OPTIONS_LABEL
#define IDS_PRINT_PREVIEW_OPTION_LG_HEADER_FOOTER
#define IDS_PRINT_PREVIEW_OPTION_FIT_TO_PAGE
#define IDS_PRINT_PREVIEW_OPTION_FIT_TO_PAPER
#define IDS_PRINT_PREVIEW_OPTION_BACKGROUND_COLORS_AND_IMAGES
#define IDS_PRINT_PREVIEW_OPTION_SELECTION_ONLY
#define IDS_PRINT_PREVIEW_OPTION_RASTERIZE
#define IDS_PRINT_PREVIEW_MARGINS_LABEL
#define IDS_PRINT_PREVIEW_DEFAULT_MARGINS
#define IDS_PRINT_PREVIEW_NO_MARGINS
#define IDS_PRINT_PREVIEW_CUSTOM_MARGINS
#define IDS_PRINT_PREVIEW_MINIMUM_MARGINS
#define IDS_PRINT_PREVIEW_TOP_MARGIN_LABEL
#define IDS_PRINT_PREVIEW_BOTTOM_MARGIN_LABEL
#define IDS_PRINT_PREVIEW_LEFT_MARGIN_LABEL
#define IDS_PRINT_PREVIEW_RIGHT_MARGIN_LABEL
#define IDS_PRINT_PREVIEW_MEDIA_SIZE_LABEL
#define IDS_PRINT_PREVIEW_DPI_LABEL
#define IDS_PRINT_PREVIEW_NON_ISOTROPIC_DPI_ITEM_LABEL
#define IDS_PRINT_PREVIEW_DPI_ITEM_LABEL
#define IDS_PRINT_PREVIEW_DESTINATION_SEARCH_TITLE
#define IDS_PRINT_PREVIEW_ACCOUNT_SELECT_TITLE
#define IDS_PRINT_PREVIEW_ADD_ACCOUNT_TITLE
#define IDS_PRINT_PREVIEW_CLOUD_PRINT_PROMOTION
#define IDS_PRINT_PREVIEW_SEARCH_BOX_PLACEHOLDER
#define IDS_PRINT_PREVIEW_NO_DESTINATIONS_MESSAGE
#define IDS_PRINT_PREVIEW_RECENT_DESTINATIONS_TITLE
#define IDS_PRINT_PREVIEW_PRINT_DESTINATIONS_TITLE
#define IDS_PRINT_PREVIEW_MANAGE
#define IDS_PRINT_PREVIEW_SEE_MORE
#define IDS_PRINT_PREVIEW_SEE_MORE_DESTINATIONS_LABEL
#define IDS_PRINT_PREVIEW_OFFLINE_FOR_YEAR
#define IDS_PRINT_PREVIEW_OFFLINE_FOR_MONTH
#define IDS_PRINT_PREVIEW_OFFLINE_FOR_WEEK
#define IDS_PRINT_PREVIEW_OFFLINE
#define IDS_PRINT_PREVIEW_NO_LONGER_SUPPORTED_FRAGMENT
#define IDS_PRINT_PREVIEW_NO_LONGER_SUPPORTED
#define IDS_PRINT_PREVIEW_EXTENSION_DESTINATION_ICON_TOOLTIP
#define IDS_MORE_OPTIONS_LABEL
#define IDS_PRINT_PREVIEW_COULD_NOT_PRINT
#define IDS_PRINT_PREVIEW_ADVANCED_SETTINGS_SEARCH_BOX_PLACEHOLDER
#define IDS_PRINT_PREVIEW_ADVANCED_SETTINGS_DIALOG_TITLE
#define IDS_PRINT_PREVIEW_NO_ADVANCED_SETTINGS_MATCH_SEARCH_HINT
#define IDS_PRINT_PREVIEW_ADVANCED_SETTINGS_DIALOG_CONFIRM
#define IDS_PRINT_PREVIEW_NEW_SHOW_ADVANCED_OPTIONS
#define IDS_PRINT_PREVIEW_ACCEPT_INVITE
#define IDS_PRINT_PREVIEW_ACCEPT_GROUP_INVITE
#define IDS_PRINT_PREVIEW_REJECT_INVITE
#define IDS_PRINT_PREVIEW_GROUP_INVITE_TEXT
#define IDS_PRINT_PREVIEW_INVITE_TEXT
#define IDS_PRINT_PREVIEW_BUTTON_SELECT
#define IDS_PRINT_PREVIEW_BUTTON_GO_BACK
#define IDS_PRINT_PREVIEW_RESOLVE_EXTENSION_USB_DIALOG_TITLE
#define IDS_PRINT_PREVIEW_RESOLVE_EXTENSION_USB_PERMISSION_MESSAGE
#define IDS_PRINT_PREVIEW_RESOLVE_EXTENSION_USB_ERROR_MESSAGE
#define IDS_PRINT_PREVIEW_MANAGED_SETTINGS_TEXT
#define IDS_PRINT_PREVIEW_SYSTEM_DIALOG_OPTION
#define IDS_DEFAULT_PRINT_DOCUMENT_TITLE
#define IDS_PRINT_SPOOL_FAILED_TITLE_TEXT
#define IDS_PRINT_SPOOL_FAILED_ERROR_TEXT
#define IDS_CLOUD_PRINT_REGISTER_PRINTER_FAILED
#define IDS_CLOUD_PRINT_ZOMBIE_PRINTER
#define IDS_CLOUD_PRINT_ENUM_FAILED
#define IDS_SERVICE_CRASH_RECOVERY_CONTENT
#define IDS_PRESS_APP_TO_EXIT
#define IDS_VR_SHELL_SITE_IS_TRACKING_LOCATION
#define IDS_VR_SHELL_SITE_IS_USING_MICROPHONE
#define IDS_VR_SHELL_SITE_IS_USING_CAMERA
#define IDS_VR_SHELL_SITE_IS_SHARING_SCREEN
#define IDS_VR_SHELL_BG_IS_USING_MICROPHONE
#define IDS_VR_SHELL_BG_IS_USING_CAMERA
#define IDS_VR_SHELL_BG_IS_SHARING_SCREEN
#define IDS_VR_SHELL_SITE_CAN_TRACK_LOCATION
#define IDS_VR_SHELL_SITE_CAN_USE_MICROPHONE
#define IDS_VR_SHELL_SITE_CAN_USE_CAMERA
#define IDS_VR_SHELL_SITE_CAN_SHARE_SCREEN
#define IDS_VR_SHELL_SITE_IS_USING_BLUETOOTH
#define IDS_VR_SHELL_SITE_CAN_USE_BLUETOOTH
#define IDS_DESKTOP_PROMPT_DOFF_HEADSET
#define IDS_VR_DESKTOP_GENERIC_PERMISSION_PROMPT
#define IDS_VR_SHELL_SITE_IS_USING_USB
#define IDS_VR_SHELL_SITE_IS_USING_MIDI
#define IDS_VR_SHELL_SITE_CAN_USE_MIDI
#define IDS_VR_UPDATE_KEYBOARD_PROMPT
#define IDS_VR_SHELL_EXIT_PROMPT_DESCRIPTION
#define IDS_VR_SHELL_EXIT_PROMPT_DESCRIPTION_SITE_INFO
#define IDS_VR_SHELL_AUDIO_PERMISSION_PROMPT_DESCRIPTION
#define IDS_VR_SHELL_AUDIO_PERMISSION_PROMPT_ABORT_BUTTON
#define IDS_VR_SHELL_AUDIO_PERMISSION_PROMPT_CONTINUE_BUTTON
#define IDS_VR_SHELL_EXIT_PROMPT_EXIT_VR_BUTTON
#define IDS_VR_BROWSER_UNSUPPORTED_PAGE
#define IDS_VR_WEB_VR_TIMEOUT_MESSAGE
#define IDS_VR_WEB_VR_EXIT_BUTTON_LABEL
#define IDS_VR_NO_SPEECH_RECOGNITION_RESULT
#define IDS_VR_BUTTON_TRACKPAD
#define IDS_VR_BUTTON_EXIT
#define IDS_VR_BUTTON_BACK
#define IDS_VR_BUTTON_TRACKPAD_REPOSITION
#define IDS_VR_BUTTON_APP_REPOSITION
#define IDS_VR_MENU_NEW_INCOGNITO_TAB
#define IDS_VR_MENU_PREFERENCES
#define IDS_VR_MENU_CLOSE_INCOGNITO_TABS
#define IDS_VR_TABS_BUTTON_REGULAR
#define IDS_VR_TABS_BUTTON_INCOGNITO
#define IDS_XR_CONSENT_DIALOG_TITLE
#define IDS_XR_CONSENT_DIALOG_DESCRIPTION_DEFAULT
#define IDS_XR_CONSENT_DIALOG_DESCRIPTION_PHYSICAL_FEATURES
#define IDS_XR_CONSENT_DIALOG_DESCRIPTION_FLOOR_PLAN
#define IDS_XR_CONSENT_DIALOG_BUTTON_ALLOW_AND_ENTER_VR
#define IDS_BACK_BUTTON_AUTHENTICATOR_REQUEST_DIALOG
#define IDS_BACKGROUND_APP_INSTALLED_BALLOON_TITLE
#define IDS_BACKGROUND_APP_INSTALLED_BALLOON_BODY
#define IDS_BACKGROUND_CRASHED_APP_BALLOON_MESSAGE
#define IDS_BACKGROUND_CRASHED_EXTENSION_BALLOON_MESSAGE
#define IDS_BACKGROUND_APP_NOT_INSTALLED
#define IDS_PERMISSIONS_BUBBLE_PROMPT
#define IDS_PERMISSION_ALLOW
#define IDS_PERMISSION_DENY
#define IDS_PERMISSION_CUSTOMIZE
#define IDS_ALTERNATE_NAV_URL_VIEW_LABEL
#define IDS_DOWNLOAD_TITLE
#define IDS_TAB_LOADING_TITLE
#define IDS_HOVER_CARD_FILE_URL_SOURCE
#define IDS_HOVER_CARD_CRASHED_TITLE
#define IDS_HISTORY_SEARCH_PROMPT
#define IDS_HISTORY_CLEAR_SEARCH
#define IDS_HISTORY_DELETE
#define IDS_HISTORY_ITEMS_SELECTED
#define IDS_HISTORY_HISTORY_MENU_DESCRIPTION
#define IDS_HISTORY_HISTORY_MENU_ITEM
#define IDS_HISTORY_NO_SYNCED_RESULTS
#define IDS_HISTORY_OPEN_TABS_MENU_ITEM
#define IDS_HISTORY_SIGN_IN_BUTTON
#define IDS_HISTORY_SIGN_IN_PROMO
#define IDS_HISTORY_SIGN_IN_PROMO_DESC
#define IDS_HISTORY_MENU_PROMO
#define IDS_HISTORY_CLOSE_MENU_PROMO
#define IDS_EDIT
#define IDS_CONFIRM
#define IDS_DISABLE
#define IDS_SEARCH_CLEARED
#define IDS_SEARCH_RESULTS
#define IDS_SEARCH_RESULTS_SINGULAR
#define IDS_SEARCH_RESULTS_PLURAL
#define IDS_SEARCH_NO_RESULTS
#define IDS_SHOW_BUBBLE_INACTIVE_DESCRIPTION
#define IDS_CONTENT_CONTEXT_INSPECTELEMENT
#define IDS_CONTENT_CONTEXT_ACCESSIBILITY_LABELS_DIALOG_TITLE
#define IDS_CONTENT_CONTEXT_ACCESSIBILITY_LABELS_BUBBLE_ENABLE
#define IDS_CONTENT_CONTEXT_ACCESSIBILITY_LABELS_BUBBLE_DISABLE
#define IDS_CONTENT_CONTEXT_BACK
#define IDS_CONTENT_CONTEXT_FORWARD
#define IDS_CONTENT_CONTEXT_SAVEPAGEAS
#define IDS_CONTENT_CONTEXT_PRINT
#define IDS_CONTENT_CONTEXT_VIEWPAGESOURCE
#define IDS_CONTENT_CONTEXT_OPENLINKWITH
#define IDS_CONTENT_CONTEXT_OPENLINKWITH_CONFIGURE
#define IDS_CONTENT_CONTEXT_INSPECTBACKGROUNDPAGE
#define IDS_CONTENT_CONTEXT_RELOAD
#define IDS_CONTENT_CONTEXT_RESTART_APP
#define IDS_CONTENT_CONTEXT_RELOAD_PACKAGED_APP
#define IDS_CONTENT_CONTEXT_TRANSLATE
#define IDS_CONTENT_CONTEXT_EXIT_FULLSCREEN
#define IDS_CONTENT_CONTEXT_RELOADFRAME
#define IDS_CONTENT_CONTEXT_VIEWFRAMESOURCE
#define IDS_CONTENT_CONTEXT_OPENLINKNEWTAB
#define IDS_CONTENT_CONTEXT_OPENLINKNEWWINDOW
#define IDS_CONTENT_CONTEXT_OPENLINKOFFTHERECORD
#define IDS_CONTENT_CONTEXT_OPENLINKINPROFILES
#define IDS_CONTENT_CONTEXT_OPENLINKINPROFILE
#define IDS_CONTENT_CONTEXT_OPENLINKBOOKMARKAPP
#define IDS_CONTENT_CONTEXT_OPENLINKBOOKMARKAPP_SAMEAPP
#define IDS_CONTENT_CONTEXT_SAVELINKAS
#define IDS_CONTENT_CONTEXT_COPYLINKLOCATION
#define IDS_CONTENT_CONTEXT_COPYEMAILADDRESS
#define IDS_CONTENT_CONTEXT_COPYLINKTEXT
#define IDS_CONTENT_CONTEXT_SAVEIMAGEAS
#define IDS_CONTENT_CONTEXT_COPYIMAGELOCATION
#define IDS_CONTENT_CONTEXT_COPYIMAGE
#define IDS_CONTENT_CONTEXT_OPENIMAGENEWTAB
#define IDS_CONTENT_CONTEXT_OPEN_ORIGINAL_IMAGE_NEW_TAB
#define IDS_CONTENT_CONTEXT_LOAD_IMAGE
#define IDS_CONTENT_CONTEXT_LOOP
#define IDS_CONTENT_CONTEXT_CONTROLS
#define IDS_CONTENT_CONTEXT_ROTATECW
#define IDS_CONTENT_CONTEXT_ROTATECCW
#define IDS_CONTENT_CONTEXT_SAVEVIDEOAS
#define IDS_CONTENT_CONTEXT_COPYVIDEOLOCATION
#define IDS_CONTENT_CONTEXT_OPENVIDEONEWTAB
#define IDS_CONTENT_CONTEXT_SAVEAUDIOAS
#define IDS_CONTENT_CONTEXT_COPYAUDIOLOCATION
#define IDS_CONTENT_CONTEXT_OPENAUDIONEWTAB
#define IDS_CONTENT_CONTEXT_PICTUREINPICTURE
#define IDS_CONTENT_CONTEXT_UNDO
#define IDS_CONTENT_CONTEXT_REDO
#define IDS_CONTENT_CONTEXT_CUT
#define IDS_CONTENT_CONTEXT_COPY
#define IDS_CONTENT_CONTEXT_PASTE
#define IDS_CONTENT_CONTEXT_PASTE_AND_MATCH_STYLE
#define IDS_CONTENT_CONTEXT_ADD_TO_DICTIONARY
#define IDS_CONTENT_CONTEXT_ACCESSIBILITY_LABELS_MENU_OPTION
#define IDS_CONTENT_CONTEXT_ACCESSIBILITY_LABELS_SEND
#define IDS_CONTENT_CONTEXT_ACCESSIBILITY_LABELS_SEND_ONCE
#define IDS_CONTENT_CONTEXT_SPELLING_ASK_GOOGLE
#define IDS_CONTENT_CONTEXT_SPELLING_BUBBLE_TITLE
#define IDS_CONTENT_CONTEXT_SPELLING_BUBBLE_ENABLE
#define IDS_CONTENT_CONTEXT_SPELLING_BUBBLE_DISABLE
#define IDS_CONTENT_CONTEXT_SPELLING_CHECKING
#define IDS_CONTENT_CONTEXT_SPELLING_NO_SUGGESTIONS_FROM_GOOGLE
#define IDS_CONTENT_CONTEXT_SELECTALL
#define IDS_CONTENT_CONTEXT_SEARCHWEBFOR
#define IDS_CONTENT_CONTEXT_SEARCHWEBFORIMAGE
#define IDS_CONTENT_CONTEXT_GOTOURL
#define IDS_CONTENT_CONTEXT_GENERATEPASSWORD
#define IDS_CONTENT_CONTEXT_MORE_APPS
#define IDS_CONTENT_CONTEXT_OPEN_WITH_APP
#define IDS_CONTENT_CONTEXT_PLUGIN_RUN
#define IDS_CONTENT_CONTEXT_PLUGIN_HIDE
#define IDS_CONTENT_CONTEXT_ENABLE_FLASH
#define IDS_CONTENT_CONTEXT_SPELLCHECK_MENU
#define IDS_CONTENT_CONTEXT_LANGUAGE_SETTINGS
#define IDS_CONTENT_CONTEXT_SPELLCHECK_MULTI_LINGUAL
#define IDS_CONTENT_CONTEXT_CHECK_SPELLING_WHILE_TYPING
#define IDS_NEW_TAB
#define IDS_SHOW_AS_TAB
#define IDS_NEW_WINDOW
#define IDS_NEW_INCOGNITO_WINDOW
#define IDS_PIN_TO_START_SCREEN
#define IDS_EDIT2
#define IDS_CUT
#define IDS_COPY
#define IDS_PASTE
#define IDS_DELETE
#define IDS_FIND
#define IDS_SAVE_PAGE
#define IDS_DISTILL_PAGE
#define IDS_MORE_TOOLS_MENU
#define IDS_ZOOM_MENU
#define IDS_ZOOM_MENU2
#define IDS_ZOOM_PLUS
#define IDS_ZOOM_PLUS2
#define IDS_ZOOM_NORMAL
#define IDS_ZOOM_MINUS
#define IDS_ZOOM_MINUS2
#define IDS_COPY_URL
#define IDS_OPEN_IN_APP_WINDOW
#define IDS_ACCNAME_ZOOM_PLUS2
#define IDS_ACCNAME_ZOOM_MINUS2
#define IDS_VIEW_SOURCE
#define IDS_FEEDBACK
#define IDS_DEV_TOOLS
#define IDS_DEV_TOOLS_ELEMENTS
#define IDS_DEV_TOOLS_CONSOLE
#define IDS_DEV_TOOLS_DEVICES
#define IDS_TASK_MANAGER
#define IDS_TAKE_SCREENSHOT
#define IDS_RESTORE_TAB
#define IDS_RESTORE_WINDOW
#define IDS_TOS_NOTIFICATION_TITLE
#define IDS_TOS_NOTIFICATION_BODY_TEXT
#define IDS_TOS_NOTIFICATION_ACK_BUTTON_TEXT
#define IDS_TOS_NOTIFICATION_REVIEW_BUTTON_TEXT
#define IDS_TOS_NOTIFICATION_LINK
#define IDS_HELP_MENU
#define IDS_MANAGED
#define IDS_MANAGED_BY
#define IDS_IMPORT_SETTINGS_MENU_LABEL
#define IDS_PROFILING_ENABLED
#define IDS_FULLSCREEN
#define IDS_CLEAR_BROWSING_DATA
#define IDS_SHOW_DOWNLOADS
#define IDS_SHOW_EXTENSIONS
#define IDS_SETTINGS
#define IDS_OPTIONS
#define IDS_HELP_PAGE
#define IDS_BETA_FORUM
#define IDS_GET_HELP
#define IDS_EXIT
#define IDS_AUTOCOMPLETE_MATCH_DESCRIPTION_SEPARATOR
#define IDS_EDIT_SEARCH_ENGINES
#define IDS_SEARCH_ENGINES_EDITOR_KEYWORD_COLUMN
#define IDS_SEARCH_ENGINES_EDITOR_DESCRIPTION_COLUMN
#define IDS_SEARCH_ENGINES_EDITOR_DEFAULT_ENGINE
#define IDS_ACCNAME_DOWNLOADS_BAR
#define IDS_HIDE_DOWNLOADS
#define IDS_SHOW_ALL_DOWNLOADS
#define IDS_DOWNLOAD_STARTED
#define IDS_DOWNLOAD_INTERRUPTED_STATUS
#define IDS_DOWNLOAD_INTERRUPTED_STATUS_ACCESS_DENIED
#define IDS_DOWNLOAD_INTERRUPTED_DESCRIPTION_ACCESS_DENIED
#define IDS_DOWNLOAD_INTERRUPTED_STATUS_PATH_TOO_LONG
#define IDS_DOWNLOAD_INTERRUPTED_DESCRIPTION_PATH_TOO_LONG
#define IDS_DOWNLOAD_INTERRUPTED_STATUS_DISK_FULL
#define IDS_DOWNLOAD_INTERRUPTED_DESCRIPTION_DISK_FULL
#define IDS_DOWNLOAD_INTERRUPTED_STATUS_FILE_TOO_LARGE
#define IDS_DOWNLOAD_INTERRUPTED_DESCRIPTION_FILE_TOO_LARGE
#define IDS_DOWNLOAD_INTERRUPTED_STATUS_TEMPORARY_PROBLEM
#define IDS_DOWNLOAD_INTERRUPTED_DESCRIPTION_TEMPORARY_PROBLEM
#define IDS_DOWNLOAD_INTERRUPTED_STATUS_VIRUS
#define IDS_DOWNLOAD_INTERRUPTED_DESCRIPTION_VIRUS
#define IDS_DOWNLOAD_INTERRUPTED_STATUS_BLOCKED
#define IDS_DOWNLOAD_INTERRUPTED_DESCRIPTION_BLOCKED
#define IDS_DOWNLOAD_INTERRUPTED_STATUS_CONTENT_LENGTH_MISMATCH
#define IDS_DOWNLOAD_INTERRUPTED_DESCRIPTION_CONTENT_LENGTH_MISMATCH
#define IDS_DOWNLOAD_INTERRUPTED_STATUS_SECURITY_CHECK_FAILED
#define IDS_DOWNLOAD_INTERRUPTED_DESCRIPTION_SECURITY_CHECK_FAILED
#define IDS_DOWNLOAD_INTERRUPTED_STATUS_FILE_TOO_SHORT
#define IDS_DOWNLOAD_INTERRUPTED_DESCRIPTION_FILE_TOO_SHORT
#define IDS_DOWNLOAD_INTERRUPTED_STATUS_FILE_SAME_AS_SOURCE
#define IDS_DOWNLOAD_INTERRUPTED_DESCRIPTION_FILE_SAME_AS_SOURCE
#define IDS_DOWNLOAD_INTERRUPTED_STATUS_NETWORK_TIMEOUT
#define IDS_DOWNLOAD_INTERRUPTED_DESCRIPTION_NETWORK_TIMEOUT
#define IDS_DOWNLOAD_INTERRUPTED_STATUS_NETWORK_DISCONNECTED
#define IDS_DOWNLOAD_INTERRUPTED_DESCRIPTION_NETWORK_DISCONNECTED
#define IDS_DOWNLOAD_INTERRUPTED_STATUS_SERVER_DOWN
#define IDS_DOWNLOAD_INTERRUPTED_DESCRIPTION_SERVER_DOWN
#define IDS_DOWNLOAD_INTERRUPTED_STATUS_NETWORK_ERROR
#define IDS_DOWNLOAD_INTERRUPTED_DESCRIPTION_NETWORK_ERROR
#define IDS_DOWNLOAD_INTERRUPTED_STATUS_NO_FILE
#define IDS_DOWNLOAD_INTERRUPTED_DESCRIPTION_NO_FILE
#define IDS_DOWNLOAD_INTERRUPTED_STATUS_SERVER_PROBLEM
#define IDS_DOWNLOAD_INTERRUPTED_DESCRIPTION_SERVER_PROBLEM
#define IDS_DOWNLOAD_INTERRUPTED_STATUS_SHUTDOWN
#define IDS_DOWNLOAD_INTERRUPTED_DESCRIPTION_SHUTDOWN
#define IDS_DOWNLOAD_INTERRUPTED_STATUS_CRASH
#define IDS_DOWNLOAD_INTERRUPTED_DESCRIPTION_CRASH
#define IDS_DOWNLOAD_INTERRUPTED_STATUS_UNAUTHORIZED
#define IDS_DOWNLOAD_INTERRUPTED_DESCRIPTION_UNAUTHORIZED
#define IDS_DOWNLOAD_INTERRUPTED_STATUS_SERVER_CERT_PROBLEM
#define IDS_DOWNLOAD_INTERRUPTED_DESCRIPTION_SERVER_CERT_PROBLEM
#define IDS_DOWNLOAD_INTERRUPTED_STATUS_FORBIDDEN
#define IDS_DOWNLOAD_INTERRUPTED_DESCRIPTION_FORBIDDEN
#define IDS_DOWNLOAD_INTERRUPTED_STATUS_UNREACHABLE
#define IDS_DOWNLOAD_INTERRUPTED_DESCRIPTION_UNREACHABLE
#define IDS_DOWNLOAD_NOTIFICATION_LABEL_OPEN_WHEN_COMPLETE
#define IDS_DOWNLOAD_NOTIFICATION_LABEL_OPEN
#define IDS_DOWNLOAD_STATUS_STARTING
#define IDS_DOWNLOAD_STATUS_IN_PROGRESS
#define IDS_DOWNLOAD_STATUS_SIZES
#define IDS_DOWNLOAD_STATUS_OPEN_IN
#define IDS_DOWNLOAD_STATUS_OPEN_WHEN_COMPLETE
#define IDS_DOWNLOAD_STATUS_OPENING
#define IDS_DOWNLOAD_STATUS_IN_PROGRESS_SHORT
#define IDS_DOWNLOAD_STATUS_CANCELLED
#define IDS_DOWNLOAD_STATUS_REMOVED
#define IDS_DOWNLOAD_STATUS_INTERRUPTED
#define IDS_DOWNLOAD_UNCONFIRMED_PREFIX
#define IDS_PROMPT_DANGEROUS_DOWNLOAD
#define IDS_PROMPT_DANGEROUS_DOWNLOAD_EXTENSION
#define IDS_PROMPT_UNCOMMON_DOWNLOAD_CONTENT
#define IDS_PROMPT_UNCOMMON_DOWNLOAD_CONTENT_IN_ADVANCED_PROTECTION
#define IDS_PROMPT_DEEP_SCANNING_DOWNLOAD
#define IDS_PROMPT_DOWNLOAD_BLOCKED_TOO_LARGE
#define IDS_PROMPT_DOWNLOAD_BLOCKED_PASSWORD_PROTECTED
#define IDS_PROMPT_DOWNLOAD_DEEP_SCANNED_SAFE
#define IDS_PROMPT_DOWNLOAD_SENSITIVE_CONTENT_WARNING
#define IDS_PROMPT_DOWNLOAD_SENSITIVE_CONTENT_BLOCKED
#define IDS_PROMPT_DOWNLOAD_DEEP_SCANNED_OPENED_DANGEROUS
#define IDS_PROMPT_APP_DEEP_SCANNING
#define IDS_BLOCK_REASON_UNCOMMON_DOWNLOAD
#define IDS_BLOCK_REASON_UNCOMMON_DOWNLOAD_IN_ADVANCED_PROTECTION
#define IDS_BLOCK_REASON_GENERIC_DOWNLOAD
#define IDS_DEEP_SCANNED_SAFE_DESCRIPTION
#define IDS_DEEP_SCANNED_OPENED_DANGEROUS_DESCRIPTION
#define IDS_BLOCK_REASON_SENSITIVE_CONTENT_WARNING
#define IDS_SENSITIVE_CONTENT_BLOCKED_DESCRIPTION
#define IDS_BLOCKED_TOO_LARGE_DESCRIPTION
#define IDS_BLOCKED_PASSWORD_PROTECTED_DESCRIPTION
#define IDS_CONFIRM_KEEP_DANGEROUS_DOWNLOAD_TITLE
#define IDS_KEEP_DANGEROUS_DOWNLOAD_TITLE
#define IDS_KEEP_UNCOMMON_DOWNLOAD_TITLE
#define IDS_PROMPT_CONFIRM_KEEP_DANGEROUS_DOWNLOAD
#define IDS_PROMPT_CONFIRM_KEEP_MALICIOUS_DOWNLOAD_BODY
#define IDS_CONFIRM_DOWNLOAD_AGAIN
#define IDS_CONFIRM_DOWNLOAD
#define IDS_CONFIRM_DOWNLOAD_RESTORE
#define IDS_CONTINUE_EXTENSION_DOWNLOAD
#define IDS_DISCARD_DOWNLOAD
#define IDS_OPEN_DOWNLOAD_NOW
#define IDS_SCAN_DOWNLOAD
#define IDS_DOWNLOAD_LINK_PAUSE
#define IDS_DOWNLOAD_SEARCH
#define IDS_DOWNLOAD_CLEAR_SEARCH
#define IDS_DOWNLOAD_NO_DOWNLOADS
#define IDS_DOWNLOAD_ITEM_DROPDOWN_BUTTON_ACCESSIBLE_TEXT
#define IDS_DOWNLOAD_LINK_RESUME
#define IDS_DOWNLOAD_LINK_REMOVE
#define IDS_DOWNLOAD_LINK_REMOVE_ARIA_LABEL
#define IDS_DOWNLOAD_LINK_CANCEL
#define IDS_DOWNLOAD_LINK_RETRY
#define IDS_DOWNLOAD_LINK_SHOW
#define IDS_DOWNLOAD_TAB_CANCELLED
#define IDS_DOWNLOAD_FILE_REMOVED
#define IDS_DOWNLOAD_TAB_PROGRESS_STATUS_TIME_UNKNOWN
#define IDS_DOWNLOAD_TAB_PROGRESS_STATUS
#define IDS_DOWNLOAD_TAB_PROGRESS_SIZE
#define IDS_DOWNLOAD_PROGRESS_PAUSED
#define IDS_DOWNLOAD_LINK_CLEAR_ALL
#define IDS_DOWNLOAD_LINK_OPEN_DOWNLOADS_FOLDER
#define IDS_DOWNLOAD_MORE_ACTIONS
#define IDS_DOWNLOAD_ACTION_MENU_DESCRIPTION
#define IDS_DOWNLOAD_BY_EXTENSION_URL
#define IDS_DOWNLOAD_IN_INCOGNITO
#define IDS_UNDO_DESCRIPTION
#define IDS_DOWNLOAD_UNDO
#define IDS_DOWNLOAD_TOAST_REMOVED_FROM_LIST
#define IDS_DOWNLOAD_TOAST_CLEARED_ALL
#define IDS_DOWNLOAD_STATUS_IN_PROGRESS_ACCESSIBLE_ALERT
#define IDS_DOWNLOAD_STATUS_PERCENT_COMPLETE_ACCESSIBLE_ALERT
#define IDS_DOWNLOAD_STATUS_TIME_REMAINING_ACCESSIBLE_ALERT
#define IDS_DOWNLOAD_FAILED_ACCESSIBLE_ALERT
#define IDS_DOWNLOAD_CANCELLED_ACCESSIBLE_ALERT
#define IDS_DOWNLOAD_COMPLETE_ACCESSIBLE_ALERT
#define IDS_DOWNLOAD_NOTIFICATION_COPY_TO_CLIPBOARD
#define IDS_DOWNLOAD_NOTIFICATION_ANNOTATE
#define IDS_DOWNLOAD_MENU_SHOW
#define IDS_DOWNLOAD_MENU_OPEN_WHEN_COMPLETE
#define IDS_DOWNLOAD_MENU_OPEN
#define IDS_DOWNLOAD_MENU_ALWAYS_OPEN_TYPE
#define IDS_DOWNLOAD_MENU_PLATFORM_OPEN
#define IDS_DOWNLOAD_MENU_PLATFORM_OPEN_ALWAYS
#define IDS_DOWNLOAD_MENU_CANCEL
#define IDS_DOWNLOAD_MENU_PAUSE_ITEM
#define IDS_DOWNLOAD_MENU_RESUME_ITEM
#define IDS_DOWNLOAD_MENU_DISCARD
#define IDS_DOWNLOAD_MENU_KEEP
#define IDS_DOWNLOAD_MENU_LEARN_MORE_SCANNING
#define IDS_DOWNLOAD_MENU_LEARN_MORE_INTERRUPTED
#define IDS_DOWNLOAD_MENU_ALWAYS_OPEN_PDF_IN_READER
#define IDS_ABANDON_DOWNLOAD_DIALOG_TITLE
#define IDS_ABANDON_DOWNLOAD_DIALOG_CONTINUE_BUTTON
#define IDS_ABANDON_DOWNLOAD_DIALOG_INCOGNITO_MESSAGE
#define IDS_ABANDON_DOWNLOAD_DIALOG_GUEST_MESSAGE
#define IDS_ABANDON_DOWNLOAD_DIALOG_EXIT_BUTTON
#define IDS_FEEDBACK_SERVICE_DIALOG_EXPLANATION_SCOUT
#define IDS_FEEDBACK_SERVICE_DIALOG_OK_BUTTON_LABEL
#define IDS_FEEDBACK_SERVICE_DIALOG_CANCEL_BUTTON_LABEL
#define IDS_OMNIBOX_PWA_INSTALL_ICON_LABEL
#define IDS_OMNIBOX_PWA_INSTALL_ICON_TOOLTIP
#define IDS_ADD_TO_OS_LAUNCH_SURFACE_BUBBLE_TITLE
#define IDS_CREATE_SHORTCUTS_BUTTON_LABEL
#define IDS_INSTALL_TO_OS_LAUNCH_SURFACE_BUBBLE_TITLE
#define IDS_INSTALL_PWA_BUTTON_LABEL
#define IDS_BOOKMARK_APP_AX_BUBBLE_NAME_LABEL
#define IDS_BOOKMARK_APP_BUBBLE_OPEN_AS_WINDOW
#define IDS_FINISH_POLICY_WEB_APP_INSTALLATION
#define IDS_FINISH_POLICY_WEB_APP_INSTALATION_RESTART
#define IDS_FINISH_POLICY_WEB_APP_INSTALLATION_NOT_NOW
#define IDS_ADD_TO_OS_LAUNCH_SURFACE
#define IDS_INSTALL_TO_OS_LAUNCH_SURFACE
#define IDS_UNINSTALL_FROM_OS_LAUNCH_SURFACE
#define IDS_APPLICATION_INFO_WEB_STORE_LINK
#define IDS_APPLICATION_INFO_HOMEPAGE_LINK
#define IDS_ARC_APPLICATION_INFO_MANAGE_LINK
#define IDS_APPLICATION_INFO_APP_OVERVIEW_TITLE
#define IDS_APPLICATION_INFO_APP_PERMISSIONS_TITLE
#define IDS_APPLICATION_INFO_UNINSTALL_BUTTON_TEXT
#define IDS_APPLICATION_INFO_LICENSES_BUTTON_TEXT
#define IDS_APPLICATION_INFO_SIZE_LABEL
#define IDS_APPLICATION_INFO_VERSION_LABEL
#define IDS_APPLICATION_INFO_CREATE_SHORTCUTS_BUTTON_TEXT
#define IDS_APPLICATION_INFO_LAUNCH_OPTIONS_ACCNAME
#define IDS_APPLICATION_INFO_SIZE_LOADING_LABEL
#define IDS_APPLICATION_INFO_SIZE_SMALL_LABEL
#define IDS_APPLICATION_INFO_REVOKE_PERMISSION_ALT_TEXT
#define IDS_APPLICATION_INFO_APP_NO_PERMISSIONS_TEXT
#define IDS_APPLICATION_INFO_EXTENSION_NO_PERMISSIONS_TEXT
#define IDS_APPLICATION_INFO_RETAINED_FILES
#define IDS_APPLICATION_INFO_RETAINED_DEVICES
#define IDS_CREATE_SHORTCUTS_TITLE
#define IDS_CREATE_SHORTCUTS_LABEL
#define IDS_CREATE_SHORTCUTS_DESKTOP_CHKBOX
#define IDS_CREATE_SHORTCUTS_MENU_CHKBOX
#define IDS_CREATE_SHORTCUTS_COMMIT
#define IDS_CREATE_SHORTCUTS_START_MENU_CHKBOX
#define IDS_CREATE_SHORTCUTS_QUICK_LAUNCH_BAR_CHKBOX
#define IDS_PIN_TO_TASKBAR_CHKBOX
#define IDS_WEBSHARE_TARGET_PICKER_TITLE
#define IDS_WEBSHARE_TARGET_PICKER_LABEL
#define IDS_WEBSHARE_TARGET_PICKER_COMMIT
#define IDS_WEBSHARE_TARGET_DIALOG_ITEM_TEXT
#define IDS_MANAGE
#define IDS_LIST_BULLET
#define IDS_AUTOMATIC_DOWNLOADS_TAB_LABEL
#define IDS_BLOCKED_DOWNLOAD_NO_ACTION
#define IDS_BLOCKED_DOWNLOAD_UNBLOCK
#define IDS_BLOCKED_DOWNLOADS_LINK
#define IDS_ALLOWED_DOWNLOAD_TITLE
#define IDS_BLOCKED_DOWNLOAD_TITLE
#define IDS_BLOCKED_DOWNLOADS_EXPLANATION
#define IDS_ALLOWED_DOWNLOAD_NO_ACTION
#define IDS_ALLOWED_DOWNLOAD_BLOCK
#define IDS_BLOCKED_COOKIES_TITLE
#define IDS_ACCESSED_COOKIES_TITLE
#define IDS_BLOCKED_COOKIES_MESSAGE
#define IDS_ACCESSED_COOKIES_MESSAGE
#define IDS_BLOCKED_COOKIES_LINK
#define IDS_BLOCKED_COOKIES_INFO
#define IDS_BLOCKED_IMAGES_TITLE
#define IDS_BLOCKED_IMAGES_MESSAGE
#define IDS_BLOCKED_COOKIES_UNBLOCK
#define IDS_BLOCKED_IMAGES_UNBLOCK
#define IDS_BLOCKED_COOKIES_NO_ACTION
#define IDS_ALLOWED_COOKIES_NO_ACTION
#define IDS_ALLOWED_COOKIES_BLOCK
#define IDS_BLOCKED_IMAGES_NO_ACTION
#define IDS_BLOCKED_POPUPS_TOOLTIP
#define IDS_BLOCKED_POPUPS_TITLE
#define IDS_BLOCKED_POPUPS_REDIRECTS_UNBLOCK
#define IDS_BLOCKED_POPUPS_REDIRECTS_NO_ACTION
#define IDS_BLOCKED_POPUPS_LINK
#define IDS_BLOCKED_MEDIASTREAM_MIC_AND_CAMERA_ALLOW
#define IDS_BLOCKED_MEDIASTREAM_MIC_ALLOW
#define IDS_BLOCKED_MEDIASTREAM_CAMERA_ALLOW
#define IDS_BLOCKED_MEDIASTREAM_MIC_AND_CAMERA_ASK
#define IDS_BLOCKED_MEDIASTREAM_MIC_ASK
#define IDS_BLOCKED_MEDIASTREAM_CAMERA_ASK
#define IDS_ALLOWED_MEDIASTREAM_MIC_AND_CAMERA_BLOCK
#define IDS_ALLOWED_MEDIASTREAM_MIC_BLOCK
#define IDS_ALLOWED_MEDIASTREAM_CAMERA_BLOCK
#define IDS_BLOCKED_MEDIASTREAM_MIC_AND_CAMERA_NO_ACTION
#define IDS_BLOCKED_MEDIASTREAM_MIC_NO_ACTION
#define IDS_BLOCKED_MEDIASTREAM_CAMERA_NO_ACTION
#define IDS_ALLOWED_MEDIASTREAM_MIC_AND_CAMERA_NO_ACTION
#define IDS_ALLOWED_MEDIASTREAM_MIC_NO_ACTION
#define IDS_ALLOWED_MEDIASTREAM_CAMERA_NO_ACTION
#define IDS_BLOCKED_POPUPS_EXPLANATORY_TEXT
#define IDS_BLOCKED_PLUGIN_EXPLANATORY_TEXT
#define IDS_BLOCKED_JAVASCRIPT_TITLE
#define IDS_BLOCKED_JAVASCRIPT_MESSAGE
#define IDS_BLOCKED_JAVASCRIPT_UNBLOCK
#define IDS_BLOCKED_JAVASCRIPT_NO_ACTION
#define IDS_BLOCKED_PLUGINS_TITLE
#define IDS_BLOCKED_PLUGINS_MESSAGE
#define IDS_BLOCKED_PLUGINS_LOAD_ALL
#define IDS_BLOCKED_SOUND_TITLE
#define IDS_BLOCKED_SOUND_UNBLOCK
#define IDS_BLOCKED_SOUND_NO_ACTION
#define IDS_NOTIFICATIONS_OFF_EXPLANATORY_TEXT
#define IDS_NOTIFICATIONS_QUIET_PERMISSION_BUBBLE_TITLE
#define IDS_NOTIFICATIONS_QUIET_PERMISSION_BUBBLE_DESCRIPTION
#define IDS_NOTIFICATIONS_QUIET_PERMISSION_BUBBLE_ALLOW_BUTTON
#define IDS_NOTIFICATIONS_QUIET_PERMISSION_EARLY_PROMO
#define IDS_NOTIFICATIONS_QUIET_PERMISSION_NEW_REQUEST_PROMO
#define IDS_NOTIFICATIONS_QUIET_PERMISSION_BUBBLE_CROWD_DENY_DESCRIPTION
#define IDS_COOKIE_CONTROLS_DIALOG_TITLE
#define IDS_COOKIE_CONTROLS_DIALOG_TITLE_OFF
#define IDS_COOKIE_CONTROLS_TURN_ON_BUTTON
#define IDS_COOKIE_CONTROLS_TURN_OFF_BUTTON
#define IDS_COOKIE_CONTROLS_NOT_WORKING_TITLE
#define IDS_COOKIE_CONTROLS_NOT_WORKING_DESCRIPTION
#define IDS_COOKIE_CONTROLS_BLOCKED_MESSAGE
#define IDS_COOKIE_CONTROLS_TOOLTIP
#define IDS_COOKIE_CONTROLS_HELP
#define IDS_CERT_SELECTOR_SUBJECT_COLUMN
#define IDS_CERT_SELECTOR_ISSUER_COLUMN
#define IDS_CERT_SELECTOR_PROVIDER_COLUMN
#define IDS_CERT_SELECTOR_SERIAL_COLUMN
#define IDS_CERT_INFO_SUBJECT_GROUP
#define IDS_CERT_INFO_ISSUER_GROUP
#define IDS_CERT_INFO_COMMON_NAME_LABEL
#define IDS_CERT_INFO_ORGANIZATION_LABEL
#define IDS_CERT_INFO_ORGANIZATIONAL_UNIT_LABEL
#define IDS_CERT_INFO_SERIAL_NUMBER_LABEL
#define IDS_CERT_INFO_VALIDITY_GROUP
#define IDS_CERT_INFO_ISSUED_ON_LABEL
#define IDS_CERT_INFO_EXPIRES_ON_LABEL
#define IDS_CERT_INFO_FINGERPRINTS_GROUP
#define IDS_CERT_INFO_SHA256_FINGERPRINT_LABEL
#define IDS_CERT_INFO_SHA1_FINGERPRINT_LABEL
#define IDS_CERT_DETAILS_EXTENSIONS
#define IDS_CERT_X509_SUBJECT_ALT_NAME
#define IDS_CERT_EXPORT_TYPE_BASE64
#define IDS_CERT_EXPORT_TYPE_BASE64_CHAIN
#define IDS_CERT_EXPORT_TYPE_DER
#define IDS_CERT_EXPORT_TYPE_PKCS7
#define IDS_CERT_EXPORT_TYPE_PKCS7_CHAIN
#define IDS_CERT_INFO_DIALOG_TITLE
#define IDS_CERT_INFO_GENERAL_TAB_LABEL
#define IDS_CERT_INFO_DETAILS_TAB_LABEL
#define IDS_CERT_INFO_VERIFIED_USAGES_GROUP
#define IDS_CERT_USAGE_SSL_CLIENT
#define IDS_CERT_USAGE_SSL_SERVER
#define IDS_CERT_USAGE_SSL_SERVER_WITH_STEPUP
#define IDS_CERT_USAGE_EMAIL_SIGNER
#define IDS_CERT_USAGE_EMAIL_RECEIVER
#define IDS_CERT_USAGE_OBJECT_SIGNER
#define IDS_CERT_USAGE_SSL_CA
#define IDS_CERT_USAGE_STATUS_RESPONDER
#define IDS_CERT_INFO_IDN_VALUE_FORMAT
#define IDS_CERT_INFO_FIELD_NOT_PRESENT
#define IDS_CERT_DETAILS_CERTIFICATE_HIERARCHY_LABEL
#define IDS_CERT_DETAILS_CERTIFICATE_FIELDS_LABEL
#define IDS_CERT_DETAILS_CERTIFICATE_FIELD_VALUE_LABEL
#define IDS_CERT_DETAILS_CERTIFICATE
#define IDS_CERT_DETAILS_VERSION
#define IDS_CERT_DETAILS_VERSION_FORMAT
#define IDS_CERT_DETAILS_SERIAL_NUMBER
#define IDS_CERT_DETAILS_CERTIFICATE_SIG_ALG
#define IDS_CERT_DETAILS_ISSUER
#define IDS_CERT_DETAILS_VALIDITY
#define IDS_CERT_DETAILS_NOT_BEFORE
#define IDS_CERT_DETAILS_NOT_AFTER
#define IDS_CERT_DETAILS_SUBJECT
#define IDS_CERT_DETAILS_SUBJECT_KEY_INFO
#define IDS_CERT_DETAILS_SUBJECT_KEY_ALG
#define IDS_CERT_DETAILS_SUBJECT_KEY
#define IDS_CERT_RSA_PUBLIC_KEY_DUMP_FORMAT
#define IDS_CERT_DETAILS_CERTIFICATE_SIG_VALUE
#define IDS_CERT_DETAILS_EXPORT_CERTIFICATE
#define IDS_CERT_OID_AVA_COMMON_NAME
#define IDS_CERT_OID_AVA_STATE_OR_PROVINCE
#define IDS_CERT_OID_AVA_ORGANIZATION_NAME
#define IDS_CERT_OID_AVA_ORGANIZATIONAL_UNIT_NAME
#define IDS_CERT_OID_AVA_DN_QUALIFIER
#define IDS_CERT_OID_AVA_COUNTRY_NAME
#define IDS_CERT_OID_AVA_SERIAL_NUMBER
#define IDS_CERT_OID_AVA_LOCALITY
#define IDS_CERT_OID_AVA_DC
#define IDS_CERT_OID_RFC1274_MAIL
#define IDS_CERT_OID_RFC1274_UID
#define IDS_CERT_OID_PKCS9_EMAIL_ADDRESS
#define IDS_CERT_OID_BUSINESS_CATEGORY
#define IDS_CERT_OID_EV_INCORPORATION_LOCALITY
#define IDS_CERT_OID_EV_INCORPORATION_STATE
#define IDS_CERT_OID_EV_INCORPORATION_COUNTRY
#define IDS_CERT_OID_AVA_STREET_ADDRESS
#define IDS_CERT_OID_AVA_POSTAL_CODE
#define IDS_CERT_OID_PKCS1_RSA_ENCRYPTION
#define IDS_CERT_OID_PKCS1_MD2_WITH_RSA_ENCRYPTION
#define IDS_CERT_OID_PKCS1_MD4_WITH_RSA_ENCRYPTION
#define IDS_CERT_OID_PKCS1_MD5_WITH_RSA_ENCRYPTION
#define IDS_CERT_OID_PKCS1_SHA1_WITH_RSA_ENCRYPTION
#define IDS_CERT_OID_PKCS1_SHA256_WITH_RSA_ENCRYPTION
#define IDS_CERT_OID_PKCS1_SHA384_WITH_RSA_ENCRYPTION
#define IDS_CERT_OID_PKCS1_SHA512_WITH_RSA_ENCRYPTION
#define IDS_CERT_OID_ANSIX962_ECDSA_SHA1_SIGNATURE
#define IDS_CERT_OID_ANSIX962_ECDSA_SHA256_SIGNATURE
#define IDS_CERT_OID_ANSIX962_ECDSA_SHA384_SIGNATURE
#define IDS_CERT_OID_ANSIX962_ECDSA_SHA512_SIGNATURE
#define IDS_CERT_OID_ANSIX962_EC_PUBLIC_KEY
#define IDS_CERT_OID_SECG_EC_SECP256R1
#define IDS_CERT_OID_SECG_EC_SECP384R1
#define IDS_CERT_OID_SECG_EC_SECP521R1
#define IDS_CERT_EXT_NS_CERT_TYPE
#define IDS_CERT_EXT_NS_CERT_TYPE_EMAIL
#define IDS_CERT_EXT_NS_CERT_TYPE_EMAIL_CA
#define IDS_CERT_EXT_NS_CERT_BASE_URL
#define IDS_CERT_EXT_NS_CERT_REVOCATION_URL
#define IDS_CERT_EXT_NS_CA_REVOCATION_URL
#define IDS_CERT_EXT_NS_CERT_RENEWAL_URL
#define IDS_CERT_EXT_NS_CA_POLICY_URL
#define IDS_CERT_EXT_NS_SSL_SERVER_NAME
#define IDS_CERT_EXT_NS_COMMENT
#define IDS_CERT_EXT_NS_LOST_PASSWORD_URL
#define IDS_CERT_EXT_NS_CERT_RENEWAL_TIME
#define IDS_CERT_X509_SUBJECT_DIRECTORY_ATTR
#define IDS_CERT_X509_SUBJECT_KEYID
#define IDS_CERT_KEYID_FORMAT
#define IDS_CERT_ISSUER_FORMAT
#define IDS_CERT_SERIAL_NUMBER_FORMAT
#define IDS_CERT_X509_KEY_USAGE
#define IDS_CERT_X509_ISSUER_ALT_NAME
#define IDS_CERT_X509_BASIC_CONSTRAINTS
#define IDS_CERT_X509_NAME_CONSTRAINTS
#define IDS_CERT_X509_CRL_DIST_POINTS
#define IDS_CERT_X509_CERT_POLICIES
#define IDS_CERT_X509_POLICY_MAPPINGS
#define IDS_CERT_X509_POLICY_CONSTRAINTS
#define IDS_CERT_X509_AUTH_KEYID
#define IDS_CERT_X509_EXT_KEY_USAGE
#define IDS_CERT_X509_AUTH_INFO_ACCESS
#define IDS_CERT_X509_KEY_USAGE_SIGNING
#define IDS_CERT_X509_KEY_USAGE_NONREP
#define IDS_CERT_X509_KEY_USAGE_ENCIPHERMENT
#define IDS_CERT_X509_KEY_USAGE_DATA_ENCIPHERMENT
#define IDS_CERT_X509_KEY_USAGE_KEY_AGREEMENT
#define IDS_CERT_X509_KEY_USAGE_CERT_SIGNER
#define IDS_CERT_X509_KEY_USAGE_CRL_SIGNER
#define IDS_CERT_X509_KEY_USAGE_ENCIPHER_ONLY
#define IDS_CERT_X509_BASIC_CONSTRAINT_IS_CA
#define IDS_CERT_X509_BASIC_CONSTRAINT_IS_NOT_CA
#define IDS_CERT_X509_BASIC_CONSTRAINT_PATH_LEN
#define IDS_CERT_X509_BASIC_CONSTRAINT_PATH_LEN_UNLIMITED
#define IDS_CERT_PKIX_CPS_POINTER_QUALIFIER
#define IDS_CERT_PKIX_USER_NOTICE_QUALIFIER
#define IDS_CERT_REVOCATION_REASON_UNUSED
#define IDS_CERT_REVOCATION_REASON_KEY_COMPROMISE
#define IDS_CERT_REVOCATION_REASON_CA_COMPROMISE
#define IDS_CERT_REVOCATION_REASON_AFFILIATION_CHANGED
#define IDS_CERT_REVOCATION_REASON_SUPERSEDED
#define IDS_CERT_REVOCATION_REASON_CESSATION_OF_OPERATION
#define IDS_CERT_REVOCATION_REASON_CERTIFICATE_HOLD
#define IDS_CERT_OCSP_RESPONDER_FORMAT
#define IDS_CERT_CA_ISSUERS_FORMAT
#define IDS_CERT_UNKNOWN_OID_INFO_FORMAT
#define IDS_CERT_EXT_KEY_USAGE_FORMAT
#define IDS_CERT_MULTILINE_INFO_START_FORMAT
#define IDS_CERT_GENERAL_NAME_RFC822_NAME
#define IDS_CERT_GENERAL_NAME_DNS_NAME
#define IDS_CERT_GENERAL_NAME_X400_ADDRESS
#define IDS_CERT_GENERAL_NAME_DIRECTORY_NAME
#define IDS_CERT_GENERAL_NAME_EDI_PARTY_NAME
#define IDS_CERT_GENERAL_NAME_URI
#define IDS_CERT_GENERAL_NAME_IP_ADDRESS
#define IDS_CERT_GENERAL_NAME_REGISTERED_ID
#define IDS_CERT_EXT_MS_CERT_TYPE
#define IDS_CERT_EXT_MS_CA_VERSION
#define IDS_CERT_EXT_MS_NT_PRINCIPAL_NAME
#define IDS_CERT_EXT_MS_NTDS_REPLICATION
#define IDS_CERT_EKU_TLS_WEB_SERVER_AUTHENTICATION
#define IDS_CERT_EKU_TLS_WEB_CLIENT_AUTHENTICATION
#define IDS_CERT_EKU_CODE_SIGNING
#define IDS_CERT_EKU_EMAIL_PROTECTION
#define IDS_CERT_EKU_TIME_STAMPING
#define IDS_CERT_EKU_OCSP_SIGNING
#define IDS_CERT_EKU_MS_INDIVIDUAL_CODE_SIGNING
#define IDS_CERT_EKU_MS_COMMERCIAL_CODE_SIGNING
#define IDS_CERT_EKU_MS_TRUST_LIST_SIGNING
#define IDS_CERT_EKU_MS_TIME_STAMPING
#define IDS_CERT_EKU_MS_SERVER_GATED_CRYPTO
#define IDS_CERT_EKU_MS_ENCRYPTING_FILE_SYSTEM
#define IDS_CERT_EKU_MS_FILE_RECOVERY
#define IDS_CERT_EKU_MS_WINDOWS_HARDWARE_DRIVER_VERIFICATION
#define IDS_CERT_EKU_MS_QUALIFIED_SUBORDINATION
#define IDS_CERT_EKU_MS_KEY_RECOVERY
#define IDS_CERT_EKU_MS_DOCUMENT_SIGNING
#define IDS_CERT_EKU_MS_LIFETIME_SIGNING
#define IDS_CERT_EKU_MS_SMART_CARD_LOGON
#define IDS_CERT_EKU_MS_KEY_RECOVERY_AGENT
#define IDS_CERT_EKU_NETSCAPE_INTERNATIONAL_STEP_UP
#define IDS_CERT_EXTENSION_CRITICAL
#define IDS_CERT_EXTENSION_NON_CRITICAL
#define IDS_CERT_EXTENSION_DUMP_ERROR
#define IDS_CERTIFICATE_MANAGER_TITLE
#define IDS_CERT_MANAGER_HARDWARE_BACKED_KEY_FORMAT
#define IDS_CERT_MANAGER_HARDWARE_BACKED
#define IDS_CERT_MANAGER_EXTENSION_PROVIDED_FORMAT
#define IDS_DEV_TOOLS_INFOBAR_LABEL
#define IDS_DEV_TOOLS_CONFIRM_ADD_FILE_SYSTEM_MESSAGE
#define IDS_DEV_TOOLS_CONFIRM_ALLOW_BUTTON
#define IDS_DEV_TOOLS_CONFIRM_DENY_BUTTON
#define IDS_RELOAD_MENU_NORMAL_RELOAD_ITEM
#define IDS_RELOAD_MENU_HARD_RELOAD_ITEM
#define IDS_RELOAD_MENU_EMPTY_AND_HARD_RELOAD_ITEM
#define IDS_EXIT_FULLSCREEN_MODE
#define IDS_TAB_SHARING_INFOBAR_SHARING_CURRENT_TAB_LABEL
#define IDS_TAB_SHARING_INFOBAR_SHARING_ANOTHER_UNTITLED_TAB_LABEL
#define IDS_TAB_SHARING_INFOBAR_SHARING_ANOTHER_TAB_LABEL
#define IDS_TAB_SHARING_INFOBAR_SHARE_BUTTON
#define IDS_TAB_SHARING_INFOBAR_STOP_BUTTON
#define IDS_TASK_MANAGER_KILL
#define IDS_TASK_MANAGER_PROCESS_ID_COLUMN
#define IDS_TASK_MANAGER_GDI_HANDLES_COLUMN
#define IDS_TASK_MANAGER_USER_HANDLES_COLUMN
#define IDS_TASK_MANAGER_TASK_COLUMN
#define IDS_TASK_MANAGER_NACL_DEBUG_STUB_PORT_COLUMN
#define IDS_TASK_MANAGER_NET_COLUMN
#define IDS_TASK_MANAGER_CPU_COLUMN
#define IDS_TASK_MANAGER_START_TIME_COLUMN
#define IDS_TASK_MANAGER_CPU_TIME_COLUMN
#define IDS_TASK_MANAGER_MEM_FOOTPRINT_COLUMN
#define IDS_TASK_MANAGER_SWAPPED_MEM_COLUMN
#define IDS_TASK_MANAGER_PROFILE_NAME_COLUMN
#define IDS_TASK_MANAGER_IDLE_WAKEUPS_COLUMN
#define IDS_TASK_MANAGER_HARD_FAULTS_COLUMN
#define IDS_TASK_MANAGER_OPEN_FD_COUNT_COLUMN
#define IDS_TASK_MANAGER_PROCESS_PRIORITY_COLUMN
#define IDS_TASK_MANAGER_WEBCORE_IMAGE_CACHE_COLUMN
#define IDS_TASK_MANAGER_WEBCORE_SCRIPTS_CACHE_COLUMN
#define IDS_TASK_MANAGER_WEBCORE_CSS_CACHE_COLUMN
#define IDS_TASK_MANAGER_VIDEO_MEMORY_COLUMN
#define IDS_TASK_MANAGER_SQLITE_MEMORY_USED_COLUMN
#define IDS_TASK_MANAGER_JAVASCRIPT_MEMORY_ALLOCATED_COLUMN
#define IDS_TASK_MANAGER_KEEPALIVE_COUNT_COLUMN
#define IDS_TASK_MANAGER_MEM_CELL_TEXT
#define IDS_TASK_MANAGER_CACHE_SIZE_CELL_TEXT
#define IDS_TASK_MANAGER_NA_CELL_TEXT
#define IDS_TASK_MANAGER_BACKGROUNDED_TEXT
#define IDS_TASK_MANAGER_FOREGROUNDED_TEXT
#define IDS_TASK_MANAGER_UNKNOWN_VALUE_TEXT
#define IDS_TASK_MANAGER_DISABLED_NACL_DBG_TEXT
#define IDS_TASK_MANAGER_HANDLES_CELL_TEXT
#define IDS_TASK_MANAGER_WEB_BROWSER_CELL_TEXT
#define IDS_TASK_MANAGER_EXTENSION_PREFIX
#define IDS_TASK_MANAGER_EXTENSION_INCOGNITO_PREFIX
#define IDS_TASK_MANAGER_APP_PREFIX
#define IDS_TASK_MANAGER_APP_INCOGNITO_PREFIX
#define IDS_TASK_MANAGER_TAB_PREFIX
#define IDS_TASK_MANAGER_TAB_INCOGNITO_PREFIX
#define IDS_TASK_MANAGER_BACKGROUND_APP_PREFIX
#define IDS_TASK_MANAGER_BACKGROUND_PREFIX
#define IDS_TASK_MANAGER_PLUGIN_PREFIX
#define IDS_TASK_MANAGER_PLUGIN_BROKER_PREFIX
#define IDS_TASK_MANAGER_PRERENDER_PREFIX
#define IDS_TASK_MANAGER_RENDERER_PREFIX
#define IDS_TASK_MANAGER_SERVICE_WORKER_PREFIX
#define IDS_TASK_MANAGER_UNKNOWN_PLUGIN_NAME
#define IDS_TASK_MANAGER_UTILITY_PREFIX
#define IDS_TASK_MANAGER_NACL_PREFIX
#define IDS_TASK_MANAGER_NACL_BROKER_PREFIX
#define IDS_TASK_MANAGER_GPU_PREFIX
#define IDS_TASK_MANAGER_PRINT_PREFIX
#define IDS_TASK_MANAGER_SUBFRAME_PREFIX
#define IDS_TASK_MANAGER_SUBFRAME_INCOGNITO_PREFIX
#define IDS_TASK_MANAGER_ARC_PREFIX
#define IDS_TASK_MANAGER_ARC_PREFIX_BACKGROUND_SERVICE
#define IDS_TASK_MANAGER_ARC_PREFIX_RECEIVER
#define IDS_TASK_MANAGER_ARC_SYSTEM
#define IDS_TASK_MANAGER_LINUX_VM_PREFIX
#define IDS_TASK_MANAGER_PLUGIN_VM_PREFIX
#define IDS_UTILITY_PROCESS_FILE_UTILITY_NAME
#define IDS_UTILITY_PROCESS_PROFILE_IMPORTER_NAME
#define IDS_UTILITY_PROCESS_WIFI_CREDENTIALS_GETTER_NAME
#define IDS_UTILITY_PROCESS_IMAGE_WRITER_NAME
#define IDS_UTILITY_PROCESS_MEDIA_GALLERY_UTILITY_NAME
#define IDS_UTILITY_PROCESS_NOOP_SERVICE_NAME
#define IDS_THEME_INSTALL_INFOBAR_LABEL
#define IDS_THEME_INSTALL_INFOBAR_UNDO_BUTTON
#define IDS_CRITICAL_NOTIFICATION_RESTART
#define IDS_EXTENSION_DISABLED_ERROR_LABEL
#define IDS_EXTENSION_IS_BLACKLISTED
#define IDS_EXTENSION_DISABLED_REMOTE_INSTALL_ERROR_TITLE
#define IDS_EXTENSION_DISABLED_ERROR_TITLE
#define IDS_EXTENSION_BLOCKED_ACTION_BUBBLE_HEADING
#define IDS_EXTENSION_BLOCKED_ACTION_BUBBLE_OK_BUTTON
#define IDS_APP_UNINSTALL_PROMPT_TITLE
#define IDS_NON_PLATFORM_APP_UNINSTALL_PROMPT_HEADING
#define IDS_ARC_APP_UNINSTALL_PROMPT_DATA_REMOVAL_WARNING
#define IDS_EXTENSION_UNINSTALL_PROMPT_TITLE
#define IDS_EXTENSION_CONFIRM_PERMISSIONS
#define IDS_EXTENSION_DELEGATED_INSTALL_PROMPT_TITLE
#define IDS_EXTENSION_INSTALL_PROMPT_TITLE
#define IDS_EXTENSION_UNINSTALL_PROMPT_HEADING
#define IDS_EXTENSION_PROGRAMMATIC_UNINSTALL_PROMPT_HEADING
#define IDS_EXTENSION_RE_ENABLE_PROMPT_TITLE
#define IDS_EXTENSION_PERMISSIONS_PROMPT_TITLE
#define IDS_EXTENSION_POST_INSTALL_PERMISSIONS_PROMPT_TITLE
#define IDS_EXTENSION_REMOTE_INSTALL_PROMPT_TITLE
#define IDS_EXTENSION_REPAIR_PROMPT_TITLE
#define IDS_EXTENSION_EXTERNAL_INSTALL_PROMPT_TITLE_APP
#define IDS_EXTENSION_EXTERNAL_INSTALL_PROMPT_TITLE_EXTENSION
#define IDS_EXTENSION_EXTERNAL_INSTALL_PROMPT_TITLE_THEME
#define IDS_EXTENSION_EXTERNAL_INSTALL_PROMPT_ACCEPT_BUTTON_EXTENSION
#define IDS_EXTENSION_EXTERNAL_INSTALL_PROMPT_ACCEPT_BUTTON_APP
#define IDS_EXTENSION_EXTERNAL_INSTALL_PROMPT_ACCEPT_BUTTON_THEME
#define IDS_EXTENSION_EXTERNAL_INSTALL_PROMPT_ABORT_BUTTON
#define IDS_EXTENSION_ALERT_TITLE
#define IDS_EXTENSION_ALERT_ITEM_EXTERNAL
#define IDS_EXTENSION_ALERT_ITEM_BLACKLISTED
#define IDS_APP_ALERT_ITEM_EXTERNAL
#define IDS_APP_ALERT_ITEM_BLACKLISTED
#define IDS_EXTENSION_ALERT_ITEM_OK
#define IDS_EXTENSION_ALERT_ITEM_DETAILS
#define IDS_EXTENSION_PROMPT_APP_CONNECT_FROM_INCOGNITO
#define IDS_EXTENSION_PROMPT_EXTENSION_CONNECT_FROM_INCOGNITO
#define IDS_EXTENSION_PROMPT_WILL_HAVE_ACCESS_TO
#define IDS_EXTENSION_PROMPT_WILL_NOW_HAVE_ACCESS_TO
#define IDS_EXTENSION_PROMPT_WANTS_ACCESS_TO
#define IDS_EXTENSION_PROMPT_CAN_ACCESS
#define IDS_EXTENSION_NO_SPECIAL_PERMISSIONS
#define IDS_EXTENSION_PERMISSION_LINE
#define IDS_EXTENSION_RATING_COUNT
#define IDS_EXTENSION_PROMPT_RATING_ACCESSIBLE_TEXT
#define IDS_EXTENSION_PROMPT_NO_RATINGS_ACCESSIBLE_TEXT
#define IDS_EXTENSION_USER_COUNT
#define IDS_EXTENSION_PROMPT_STORE_LINK
#define IDS_EXTENSION_PROMPT_RETAINED_FILES
#define IDS_EXTENSION_PROMPT_RETAINED_DEVICES
#define IDS_EXTENSION_PROMPT_WARNING_FULL_ACCESS
#define IDS_EXTENSION_PROMPT_WARNING_ALL_HOSTS
#define IDS_EXTENSION_PROMPT_WARNING_CURRENT_HOST
#define IDS_EXTENSION_PROMPT_WARNING_ALL_HOSTS_READ_ONLY
#define IDS_EXTENSION_PROMPT_WARNING_AUDIO_CAPTURE
#define IDS_EXTENSION_PROMPT_WARNING_VIDEO_CAPTURE
#define IDS_EXTENSION_PROMPT_WARNING_AUDIO_AND_VIDEO_CAPTURE
#define IDS_EXTENSION_PROMPT_WARNING_BLUETOOTH
#define IDS_EXTENSION_PROMPT_WARNING_BLUETOOTH_DEVICES
#define IDS_EXTENSION_PROMPT_WARNING_BLUETOOTH_PRIVATE
#define IDS_EXTENSION_PROMPT_WARNING_BLUETOOTH_SERIAL
#define IDS_EXTENSION_PROMPT_WARNING_BOOKMARKS
#define IDS_EXTENSION_PROMPT_WARNING_CLIPBOARD
#define IDS_EXTENSION_PROMPT_WARNING_CLIPBOARD_READWRITE
#define IDS_EXTENSION_PROMPT_WARNING_CLIPBOARD_WRITE
#define IDS_EXTENSION_PROMPT_WARNING_DEBUGGER
#define IDS_EXTENSION_PROMPT_WARNING_DECLARATIVE_WEB_REQUEST
#define IDS_EXTENSION_PROMPT_WARNING_DECLARATIVE_NET_REQUEST
#define IDS_EXTENSION_PROMPT_WARNING_DOCUMENT_SCAN
#define IDS_EXTENSION_PROMPT_WARNING_ENTERPRISE_HARDWARE_PLATFORM
#define IDS_EXTENSION_PROMPT_WARNING_FAVICON
#define IDS_EXTENSION_PROMPT_WARNING_GEOLOCATION
#define IDS_EXTENSION_PROMPT_WARNING_HISTORY_READ
#define IDS_EXTENSION_PROMPT_WARNING_HISTORY_READ_AND_SESSIONS
#define IDS_EXTENSION_PROMPT_WARNING_HISTORY_WRITE
#define IDS_EXTENSION_PROMPT_WARNING_HISTORY_WRITE_AND_SESSIONS
#define IDS_EXTENSION_PROMPT_WARNING_HOME_PAGE_SETTING_OVERRIDE
#define IDS_EXTENSION_PROMPT_WARNING_1_HOST
#define IDS_EXTENSION_PROMPT_WARNING_1_HOST_READ_ONLY
#define IDS_EXTENSION_PROMPT_WARNING_2_HOSTS
#define IDS_EXTENSION_PROMPT_WARNING_2_HOSTS_READ_ONLY
#define IDS_EXTENSION_PROMPT_WARNING_3_HOSTS
#define IDS_EXTENSION_PROMPT_WARNING_3_HOSTS_READ_ONLY
#define IDS_EXTENSION_PROMPT_WARNING_HOSTS_LIST
#define IDS_EXTENSION_PROMPT_WARNING_HOSTS_LIST_READ_ONLY
#define IDS_EXTENSION_PROMPT_WARNING_HOST_AND_SUBDOMAIN
#define IDS_EXTENSION_PROMPT_WARNING_HOST_AND_SUBDOMAIN_LIST
#define IDS_EXTENSION_PROMPT_WARNING_INPUT
#define IDS_EXTENSION_PROMPT_WARNING_LOGIN
#define IDS_EXTENSION_PROMPT_WARNING_LOGIN_SCREEN_UI
#define IDS_EXTENSION_PROMPT_WARNING_LOGIN_SCREEN_STORAGE
#define IDS_EXTENSION_PROMPT_WARNING_MANAGEMENT
#define IDS_EXTENSION_PROMPT_WARNING_MDNS
#define IDS_EXTENSION_PROMPT_WARNING_NETWORK_STATE
#define IDS_EXTENSION_PROMPT_WARNING_NETWORKING_CONFIG
#define IDS_EXTENSION_PROMPT_WARNING_NETWORKING_PRIVATE
#define IDS_EXTENSION_PROMPT_WARNING_PRINTING
#define IDS_EXTENSION_PROMPT_WARNING_PRINTING_METRICS
#define IDS_EXTENSION_PROMPT_WARNING_SEARCH_SETTINGS_OVERRIDE
#define IDS_EXTENSION_PROMPT_WARNING_SERIAL
#define IDS_EXTENSION_PROMPT_WARNING_SOCKET_ANY_HOST
#define IDS_EXTENSION_PROMPT_WARNING_SOCKET_HOSTS_IN_DOMAIN
#define IDS_EXTENSION_PROMPT_WARNING_SOCKET_HOSTS_IN_DOMAINS
#define IDS_EXTENSION_PROMPT_WARNING_SOCKET_SPECIFIC_HOST
#define IDS_EXTENSION_PROMPT_WARNING_SOCKET_SPECIFIC_HOSTS
#define IDS_EXTENSION_PROMPT_WARNING_START_PAGE_SETTING_OVERRIDE
#define IDS_EXTENSION_PROMPT_WARNING_SYSTEM_STORAGE
#define IDS_EXTENSION_PROMPT_WARNING_TOPSITES
#define IDS_EXTENSION_PROMPT_WARNING_TTS_ENGINE
#define IDS_EXTENSION_PROMPT_WARNING_U2F_DEVICES
#define IDS_EXTENSION_PROMPT_WARNING_NOTIFICATIONS
#define IDS_EXTENSION_PROMPT_WARNING_USB_DEVICE
#define IDS_EXTENSION_PROMPT_WARNING_USB_DEVICE_LIST
#define IDS_EXTENSION_PROMPT_WARNING_USB_DEVICE_LIST_ITEM_UNKNOWN_PRODUCT
#define IDS_EXTENSION_PROMPT_WARNING_USB_DEVICE_LIST_ITEM_UNKNOWN_VENDOR
#define IDS_EXTENSION_PROMPT_WARNING_USB_DEVICE_UNKNOWN_PRODUCT
#define IDS_EXTENSION_PROMPT_WARNING_USB_DEVICE_UNKNOWN_VENDOR
#define IDS_EXTENSION_PROMPT_WARNING_VPN
#define IDS_EXTENSION_PROMPT_WARNING_WEB_CONNECTABLE
#define IDS_EXTENSION_PROMPT_WARNING_CONTENT_SETTINGS
#define IDS_EXTENSION_PROMPT_WARNING_PRIVACY
#define IDS_EXTENSION_PROMPT_WARNING_SIGNED_IN_DEVICES
#define IDS_EXTENSION_PROMPT_WARNING_DOWNLOADS
#define IDS_EXTENSION_PROMPT_WARNING_DOWNLOADS_OPEN
#define IDS_EXTENSION_PROMPT_WARNING_IDENTITY_EMAIL
#define IDS_EXTENSION_PROMPT_WARNING_WALLPAPER
#define IDS_EXTENSION_PROMPT_WARNING_FILE_SYSTEM_DIRECTORY
#define IDS_EXTENSION_PROMPT_WARNING_FILE_SYSTEM_WRITE_DIRECTORY
#define IDS_EXTENSION_PROMPT_WARNING_MEDIA_GALLERIES_READ
#define IDS_EXTENSION_PROMPT_WARNING_MEDIA_GALLERIES_READ_WRITE
#define IDS_EXTENSION_PROMPT_WARNING_MEDIA_GALLERIES_READ_DELETE
#define IDS_EXTENSION_PROMPT_WARNING_MEDIA_GALLERIES_READ_WRITE_DELETE
#define IDS_EXTENSION_PROMPT_WARNING_SYNCFILESYSTEM
#define IDS_EXTENSION_PROMPT_WARNING_MUSIC_MANAGER_PRIVATE
#define IDS_EXTENSION_PROMPT_WARNING_NATIVE_MESSAGING
#define IDS_EXTENSION_PROMPT_WARNING_SCREENLOCK_PRIVATE
#define IDS_EXTENSION_PROMPT_WARNING_OVERRIDE_BOOKMARKS_UI
#define IDS_EXTENSION_PROMPT_WARNING_ACTIVITY_LOG_PRIVATE
#define IDS_EXTENSION_PROMPT_WARNING_DESKTOP_CAPTURE
#define IDS_EXTENSION_PROMPT_WARNING_ACCESSIBILITY_FEATURES_MODIFY
#define IDS_EXTENSION_PROMPT_WARNING_ACCESSIBILITY_FEATURES_READ
#define IDS_EXTENSION_PROMPT_WARNING_ACCESSIBILITY_FEATURES_READ_MODIFY
#define IDS_EXTENSION_PROMPT_WARNING_PLATFORMKEYS
#define IDS_EXTENSION_PROMPT_WARNING_CERTIFICATEPROVIDER
#define IDS_EXTENSION_PROMPT_WARNING_SETTINGS_PRIVATE
#define IDS_EXTENSION_PROMPT_WARNING_AUTOFILL_PRIVATE
#define IDS_EXTENSION_PROMPT_WARNING_PASSWORDS_PRIVATE
#define IDS_EXTENSION_PROMPT_WARNING_USERS_PRIVATE
#define IDS_EXTENSION_PROMPT_WARNING_DISPLAY_SOURCE
#define IDS_EXTENSION_PROMPT_WARNING_NEW_TAB_PAGE_OVERRIDE
#define IDS_EXTENSION_PROMPT_WARNING_TRANSIENT_BACKGROUND
#define IDS_EXTENSION_CANT_DOWNGRADE_VERSION
#define IDS_APP_CANT_DOWNGRADE_VERSION
#define IDS_EXTENSION_MOVE_DIRECTORY_TO_PROFILE_FAILED
#define IDS_EXTENSION_INSTALL_NOT_ENABLED
#define IDS_EXTENSION_INSTALL_INCORRECT_APP_CONTENT_TYPE
#define IDS_EXTENSION_INSTALL_INCORRECT_INSTALL_HOST
#define IDS_EXTENSION_INSTALL_UNEXPECTED_ID
#define IDS_EXTENSION_INSTALL_DISALLOWED_ON_SITE
#define IDS_EXTENSION_INSTALL_UNEXPECTED_VERSION
#define IDS_EXTENSION_INSTALL_DEPENDENCY_OLD_VERSION
#define IDS_EXTENSION_INSTALL_DEPENDENCY_NOT_SHARED_MODULE
#define IDS_EXTENSION_INSTALL_DEPENDENCY_NOT_WHITELISTED
#define IDS_EXTENSION_INSTALL_GALLERY_ONLY
#define IDS_EXTENSION_INSTALL_KIOSK_MODE_ONLY
#define IDS_EXTENSION_OVERLAPPING_WEB_EXTENT
#define IDS_EXTENSION_INVALID_IMAGE_PATH
#define IDS_EXTENSION_LOAD_ICON_FOR_PAGE_ACTION_FAILED
#define IDS_EXTENSION_LOAD_ICON_FOR_BROWSER_ACTION_FAILED
#define IDS_EXTENSION_INSTALLED_PAGE_ACTION_INFO
#define IDS_EXTENSION_INSTALLED_PAGE_ACTION_INFO_WITH_SHORTCUT
#define IDS_EXTENSION_INSTALLED_BROWSER_ACTION_INFO
#define IDS_EXTENSION_INSTALLED_BROWSER_ACTION_INFO_WITH_SHORTCUT
#define IDS_EXTENSION_INSTALLED_OMNIBOX_KEYWORD_INFO
#define IDS_EXTENSION_INSTALLED_MANAGE_INFO
#define IDS_EXTENSION_INSTALLED_MANAGE_SHORTCUTS
#define IDS_EXTENSION_INSTALLED_DICE_PROMO_SYNC_MESSAGE
#define IDS_EXTENSIONS_DIRECTORY_CONFIRMATION_DIALOG_TITLE
#define IDS_EXTENSIONS_DIRECTORY_CONFIRMATION_DIALOG_MESSAGE_READ_ONLY
#define IDS_EXTENSIONS_DIRECTORY_CONFIRMATION_DIALOG_MESSAGE_WRITABLE
#define IDS_EXTENSIONS_LOAD_ERROR_ALERT_HEADING
#define IDS_EXTENSIONS_LOAD_ERROR_MESSAGE
#define IDS_EXTENSIONS_WANTS_ACCESS_TO_SITE
#define IDS_EXTENSIONS_HAS_ACCESS_TO_SITE
#define IDS_EXTENSIONS_CONTEXT_MENU_CANT_ACCESS_PAGE
#define IDS_EXTENSIONS_CONTEXT_MENU_PAGE_ACCESS
#define IDS_EXTENSIONS_CONTEXT_MENU_PAGE_ACCESS_RUN_ON_CLICK
#define IDS_EXTENSIONS_CONTEXT_MENU_PAGE_ACCESS_RUN_ON_SITE
#define IDS_EXTENSIONS_CONTEXT_MENU_PAGE_ACCESS_RUN_ON_ALL_SITES
#define IDS_EXTENSIONS_CONTEXT_MENU_PAGE_ACCESS_LEARN_MORE
#define IDS_EXTENSIONS_OPTIONS_MENU_ITEM
#define IDS_EXTENSIONS_INSTALLED_BY_ADMIN
#define IDS_EXTENSIONS_DISABLE
#define IDS_EXTENSIONS_HIDE_BUTTON
#define IDS_EXTENSIONS_KEEP_BUTTON_IN_TOOLBAR
#define IDS_EXTENSIONS_SHOW_BUTTON_IN_TOOLBAR
#define IDS_EXTENSIONS_PIN_TO_TOOLBAR
#define IDS_EXTENSIONS_UNPIN_FROM_TOOLBAR
#define IDS_MANAGE_EXTENSION
#define IDS_EXTENSION_ACTION_INSPECT_POPUP
#define IDS_EXTENSIONS_LOCKED_SUPERVISED_USER
#define IDS_EXTENSIONS_INSTALLED_BY_SUPERVISED_USER_CUSTODIAN
#define IDS_EXTENSION_LOAD_FROM_DIRECTORY
#define IDS_EXTENSION_COMMANDS_GENERIC_ACTIVATE
#define IDS_EXTENSION_PACK_DIALOG_HEADING
#define IDS_EXTENSION_PACK_DIALOG_SELECT_KEY
#define IDS_EXTENSION_PACK_DIALOG_KEY_FILE_TYPE_DESCRIPTION
#define IDS_EXTENSION_PACK_DIALOG_ERROR_ROOT_REQUIRED
#define IDS_EXTENSION_PACK_DIALOG_ERROR_ROOT_INVALID
#define IDS_EXTENSION_PACK_DIALOG_ERROR_KEY_INVALID
#define IDS_EXTENSION_PACK_DIALOG_SUCCESS_BODY_NEW
#define IDS_EXTENSION_PACK_DIALOG_SUCCESS_BODY_UPDATE
#define IDS_EXTENSION_PROMPT_INSTALL_BUTTON
#define IDS_EXTENSION_INSTALL_PROMPT_ACCEPT_BUTTON_EXTENSION
#define IDS_EXTENSION_INSTALL_PROMPT_ACCEPT_BUTTON_APP
#define IDS_EXTENSION_INSTALL_PROMPT_ACCEPT_BUTTON_THEME
#define IDS_EXTENSION_PROMPT_UNINSTALL_BUTTON
#define IDS_EXTENSION_PROMPT_UNINSTALL_REPORT_ABUSE
#define IDS_EXTENSION_PROMPT_UNINSTALL_REPORT_ABUSE_FROM_EXTENSION
#define IDS_EXTENSION_PROMPT_UNINSTALL_TITLE
#define IDS_EXTENSION_PROMPT_UNINSTALL_APP_BUTTON
#define IDS_EXTENSION_PROMPT_UNINSTALL_TRIGGERED_BY_EXTENSION
#define IDS_EXTENSION_PROMPT_RE_ENABLE_BUTTON
#define IDS_EXTENSION_PROMPT_PERMISSIONS_BUTTON
#define IDS_EXTENSION_PROMPT_PERMISSIONS_ACCEPT_BUTTON
#define IDS_EXTENSION_PROMPT_PERMISSIONS_ABORT_BUTTON
#define IDS_EXTENSION_PROMPT_PERMISSIONS_CLEAR_RETAINED_FILES_BUTTON
#define IDS_EXTENSION_PROMPT_PERMISSIONS_CLEAR_RETAINED_DEVICES_BUTTON
#define IDS_EXTENSION_PROMPT_PERMISSIONS_CLEAR_RETAINED_FILES_AND_DEVICES_BUTTON
#define IDS_EXTENSION_PROMPT_REMOTE_INSTALL_BUTTON_EXTENSION
#define IDS_EXTENSION_PROMPT_REMOTE_INSTALL_BUTTON_APP
#define IDS_EXTENSION_PROMPT_REPAIR_BUTTON_EXTENSION
#define IDS_EXTENSION_PROMPT_REPAIR_BUTTON_APP
#define IDS_EXTENSION_WEB_STORE_TITLE
#define IDS_EXTENSION_WEB_STORE_TITLE_SHORT
#define IDS_EXTENSIONS_SHOW_DETAILS
#define IDS_EXTENSIONS_HIDE_DETAILS
#define IDS_WEBSTORE_DOWNLOAD_ACCESS_DENIED
#define IDS_EXTENSION_WARNINGS_WRENCH_MENU_ITEM
#define IDS_EXTENSION_EXTERNAL_INSTALL_ALERT_EXTENSION
#define IDS_EXTENSION_EXTERNAL_INSTALL_ALERT_APP
#define IDS_EXTENSION_EXTERNAL_INSTALL_ALERT_THEME
#define IDS_EXTENSION_EXTERNAL_INSTALL_ALERT_BUBBLE_TITLE
#define IDS_EXTENSION_EXTERNAL_INSTALL_ALERT_BUBBLE_HEADING_APP
#define IDS_EXTENSION_EXTERNAL_INSTALL_ALERT_BUBBLE_HEADING_EXTENSION
#define IDS_EXTENSION_EXTERNAL_INSTALL_ALERT_BUBBLE_HEADING_THEME
#define IDS_EXTENSIONS_UNSUPPORTED_DISABLED_TITLE
#define IDS_EXTENSIONS_DISABLED_AND_N_MORE
#define IDS_EXTENSIONS_UNSUPPORTED_DISABLED_BUTTON
#define IDS_EXTENSIONS_ADDED_WITHOUT_KNOWLEDGE
#define IDS_EXTENSIONS_DISABLE_DEVELOPER_MODE_TITLE
#define IDS_EXTENSIONS_DISABLE_DEVELOPER_MODE_BODY
#define IDS_EXTENSIONS_MENU_TITLE
#define IDS_EXTENSIONS_MENU_CONTEXT_MENU_TOOLTIP
#define IDS_EXTENSIONS_MENU_PIN_BUTTON_TOOLTIP
#define IDS_EXTENSIONS_MENU_UNPIN_BUTTON_TOOLTIP
#define IDS_EXTENSIONS_MENU_ACCESSING_SITE_DATA
#define IDS_EXTENSIONS_MENU_WANTS_TO_ACCESS_SITE_DATA
#define IDS_EXTENSIONS_MENU_CANT_ACCESS_SITE_DATA
#define IDS_EXTENSIONS_SETTINGS_API_TITLE_HOME_PAGE_BUBBLE
#define IDS_EXTENSIONS_SETTINGS_API_TITLE_STARTUP_PAGES_BUBBLE
#define IDS_EXTENSIONS_SETTINGS_API_TITLE_SEARCH_ENGINE_BUBBLE
#define IDS_EXTENSIONS_NTP_CONTROLLED_TITLE_HOME_PAGE_BUBBLE
#define IDS_EXTENSIONS_PROXY_CONTROLLED_TITLE_HOME_PAGE_BUBBLE
#define IDS_EXTENSIONS_SETTINGS_API_FIRST_LINE_SEARCH_ENGINE_SPECIFIC
#define IDS_EXTENSIONS_SETTINGS_API_FIRST_LINE_SEARCH_ENGINE
#define IDS_EXTENSIONS_SETTINGS_API_FIRST_LINE_HOME_PAGE_SPECIFIC
#define IDS_EXTENSIONS_SETTINGS_API_FIRST_LINE_HOME_PAGE
#define IDS_EXTENSIONS_SETTINGS_API_SECOND_LINE_SEARCH_ENGINE
#define IDS_EXTENSIONS_SETTINGS_API_SECOND_LINE_HOME_PAGE
#define IDS_EXTENSIONS_SETTINGS_API_SECOND_LINE_HOME_AND_SEARCH
#define IDS_EXTENSIONS_NTP_CONTROLLED_FIRST_LINE
#define IDS_EXTENSIONS_PROXY_CONTROLLED_FIRST_LINE
#define IDS_EXTENSIONS_PROXY_CONTROLLED_FIRST_LINE_EXTENSION_SPECIFIC
#define IDS_EXTENSIONS_SETTINGS_API_THIRD_LINE_CONFIRMATION
#define IDS_EXTENSION_CONTROLLED_RESTORE_SETTINGS
#define IDS_EXTENSION_CONTROLLED_KEEP_CHANGES
#define IDS_WEB_APP_MENU_BUTTON_TOOLTIP
#define IDS_COMPONENTS_TITLE
#define IDS_COMPONENTS_VERSION
#define IDS_COMPONENTS_NONE_INSTALLED
#define IDS_COMPONENTS_NO_COMPONENTS
#define IDS_COMPONENTS_CHECK_FOR_UPDATE
#define IDS_COMPONENTS_STATUS_LABEL
#define IDS_COMPONENTS_CHECKING_LABEL
#define IDS_COMPONENTS_SVC_STATUS_NEW
#define IDS_COMPONENTS_SVC_STATUS_CHECKING
#define IDS_COMPONENTS_SVC_STATUS_UPDATE
#define IDS_COMPONENTS_SVC_STATUS_DNL_DIFF
#define IDS_COMPONENTS_SVC_STATUS_DNL
#define IDS_COMPONENTS_SVC_STATUS_DOWNLOADED
#define IDS_COMPONENTS_SVC_STATUS_UPDT_DIFF
#define IDS_COMPONENTS_SVC_STATUS_UPDATING
#define IDS_COMPONENTS_SVC_STATUS_UPDATED
#define IDS_COMPONENTS_SVC_STATUS_UPTODATE
#define IDS_COMPONENTS_SVC_STATUS_UPDATE_ERROR
#define IDS_COMPONENTS_UNKNOWN
#define IDS_COMPONENTS_EVT_STATUS_STARTED
#define IDS_COMPONENTS_EVT_STATUS_SLEEPING
#define IDS_COMPONENTS_EVT_STATUS_FOUND
#define IDS_COMPONENTS_EVT_STATUS_READY
#define IDS_COMPONENTS_EVT_STATUS_UPDATED
#define IDS_COMPONENTS_EVT_STATUS_NOTUPDATED
#define IDS_COMPONENTS_EVT_STATUS_UPDATE_ERROR
#define IDS_COMPONENTS_EVT_STATUS_DOWNLOADING
#define IDS_PLUGINS_DISABLED_PLUGIN
#define IDS_PASSWORD_MANAGER_ACCOUNT_CHOOSER_TITLE
#define IDS_PASSWORD_MANAGER_CONFIRM_SAVED_TITLE
#define IDS_PASSWORD_MANAGER_SYNC_PROMO_TITLE
#define IDS_PASSWORD_GENERATION_SUGGESTION
#define IDS_PASSWORD_GENERATION_EDITING_SUGGESTION
#define IDS_SAVE_PASSWORD
#define IDS_SAVE_ACCOUNT
#define IDS_UPDATE_PASSWORD
#define IDS_SAVE_PASSWORD_DIFFERENT_DOMAINS_TITLE
#define IDS_UPDATE_PASSWORD_DIFFERENT_DOMAINS_TITLE
#define IDS_SAVE_PASSWORD_FOOTER
#define IDS_PASSWORD_MANAGER_ACCOUNT_CHOOSER_SIGN_IN
#define IDS_PASSWORD_MANAGER_MANAGE_PASSWORDS_BUTTON
#define IDS_PASSWORD_MANAGER_ONBOARDING_TITLE_A
#define IDS_PASSWORD_MANAGER_ONBOARDING_TITLE_B
#define IDS_PASSWORD_MANAGER_ONBOARDING_TITLE_C
#define IDS_PASSWORD_MANAGER_ONBOARDING_DETAILS_A
#define IDS_PASSWORD_MANAGER_ONBOARDING_DETAILS_B
#define IDS_PASSWORD_MANAGER_DICE_PROMO_SIGNIN_MESSAGE
#define IDS_PASSWORD_MANAGER_DICE_PROMO_SYNC_MESSAGE
#define IDS_PASSWORD_MANAGER_DESKTOP_TO_IOS_PROMO_TITLE
#define IDS_PASSWORD_MANAGER_DESKTOP_TO_IOS_PROMO_TITLE_V2
#define IDS_PASSWORD_MANAGER_DESKTOP_TO_IOS_PROMO_TITLE_V3
#define IDS_DESKTOP_TO_IOS_PROMO_SEND_TO_PHONE
#define IDS_DESKTOP_TO_IOS_PROMO_NO_THANKS
#define IDS_PREVIEWS_INFOBAR_TIMESTAMP_MINUTES
#define IDS_PREVIEWS_INFOBAR_TIMESTAMP_ONE_HOUR
#define IDS_PREVIEWS_INFOBAR_TIMESTAMP_HOURS
#define IDS_PREVIEWS_INFOBAR_TIMESTAMP_UPDATED_NOW
#define IDS_LITE_PAGE_PREVIEWS_MESSAGE
#define IDS_LITE_PAGE_PREVIEWS_SETTINGS_LINK
#define IDS_WEBRTC_LOGS_TITLE
#define IDS_WEBRTC_TEXT_LOGS_LOG_COUNT_BANNER_FORMAT
#define IDS_WEBRTC_EVENT_LOGS_LOG_COUNT_BANNER_FORMAT
#define IDS_WEBRTC_LOGS_LOG_LG_HEADER_FORMAT
#define IDS_WEBRTC_LOGS_LOG_LOCAL_FILE_LABEL_FORMAT
#define IDS_WEBRTC_LOGS_NO_LOCAL_LOG_FILE_MESSAGE
#define IDS_WEBRTC_LOGS_LOG_UPLOAD_TIME_FORMAT
#define IDS_WEBRTC_LOGS_LOG_FAILED_UPLOAD_TIME_FORMAT
#define IDS_WEBRTC_LOGS_LOG_REPORT_ID_FORMAT
#define IDS_WEBRTC_LOGS_BUG_LINK_LABEL
#define IDS_WEBRTC_LOGS_LOG_PENDING_MESSAGE
#define IDS_WEBRTC_LOGS_LOG_ACTIVELY_UPLOADED_MESSAGE
#define IDS_WEBRTC_LOGS_LOG_NOT_UPLOADED_MESSAGE
#define IDS_WEBRTC_LOGS_EVENT_LOG_LOCAL_LOG_ID
#define IDS_WEBRTC_LOGS_NO_TEXT_LOGS_MESSAGE
#define IDS_WEBRTC_LOGS_NO_EVENT_LOGS_MESSAGE
#define IDS_PLUGIN_HIDE
#define IDS_PLUGIN_UPDATE
#define IDS_PLUGIN_BLOCKED
#define IDS_PLUGIN_BLOCKED_BY_POLICY
#define IDS_PLUGIN_BLOCKED_NO_LOADING
#define IDS_PLUGIN_OUTDATED
#define IDS_PLUGIN_NOT_AUTHORIZED
#define IDS_PLUGIN_DOWNLOADING
#define IDS_PLUGIN_DOWNLOAD_ERROR
#define IDS_PLUGIN_DOWNLOAD_ERROR_SHORT
#define IDS_PLUGIN_UPDATING
#define IDS_PLUGIN_DISABLED
#define IDS_PLUGIN_PREFER_HTML_BY_DEFAULT
#define IDS_SESSION_CRASHED_BUBBLE_TITLE
#define IDS_SESSION_CRASHED_BUBBLE_UMA_LINK_TEXT
#define IDS_BAD_FLAGS_WARNING_MESSAGE
#define IDS_BAD_FEATURES_WARNING_MESSAGE
#define IDS_BAD_ENVIRONMENT_VARIABLES_WARNING_MESSAGE
#define IDS_PEPPER_BROKER_MESSAGE
#define IDS_PEPPER_BROKER_ALLOW_BUTTON
#define IDS_PEPPER_BROKER_DENY_BUTTON
#define IDS_BLOCKED_PPAPI_BROKER_TITLE
#define IDS_ALLOWED_PPAPI_BROKER_TITLE
#define IDS_BLOCKED_PPAPI_BROKER_MESSAGE
#define IDS_ALLOWED_PPAPI_BROKER_MESSAGE
#define IDS_BLOCKED_PPAPI_BROKER_UNBLOCK
#define IDS_BLOCKED_PPAPI_BROKER_NO_ACTION
#define IDS_ALLOWED_PPAPI_BROKER_NO_ACTION
#define IDS_ALLOWED_PPAPI_BROKER_BLOCK
#define IDS_BLOCKED_DISPLAYING_INSECURE_CONTENT_TITLE
#define IDS_BLOCKED_DISPLAYING_INSECURE_CONTENT
#define IDS_ALLOW_INSECURE_CONTENT_BUTTON
#define IDS_ADD_TO_SHELF_INFOBAR_TITLE
#define IDS_ADD_TO_SHELF_INFOBAR_ADD_BUTTON
#define IDS_ABOUT_SYS_TITLE
#define IDS_ABOUT_SYS_DESC
#define IDS_ABOUT_SYS_TABLE_TITLE
#define IDS_ABOUT_SYS_LOG_FILE_TABLE_TITLE
#define IDS_ABOUT_SYS_EXPAND_ALL
#define IDS_ABOUT_SYS_COLLAPSE_ALL
#define IDS_ABOUT_SYS_EXPAND
#define IDS_ABOUT_SYS_COLLAPSE
#define IDS_ABOUT_SYS_PARSE_ERROR
#define IDS_ABOUT_BROWSER_SWITCH_TITLE
#define IDS_ABOUT_BROWSER_SWITCH_OPENING_TITLE_UNKNOWN_BROWSER
#define IDS_ABOUT_BROWSER_SWITCH_OPENING_TITLE_KNOWN_BROWSER
#define IDS_ABOUT_BROWSER_SWITCH_ERROR_TITLE_UNKNOWN_BROWSER
#define IDS_ABOUT_BROWSER_SWITCH_ERROR_TITLE_KNOWN_BROWSER
#define IDS_ABOUT_BROWSER_SWITCH_COUNTDOWN_TITLE_UNKNOWN_BROWSER
#define IDS_ABOUT_BROWSER_SWITCH_COUNTDOWN_TITLE_KNOWN_BROWSER
#define IDS_ABOUT_BROWSER_SWITCH_GENERIC_ERROR_UNKNOWN_BROWSER
#define IDS_ABOUT_BROWSER_SWITCH_GENERIC_ERROR_KNOWN_BROWSER
#define IDS_ABOUT_BROWSER_SWITCH_PROTOCOL_ERROR
#define IDS_NACL_APP_MISSING_ARCH_MESSAGE
#define IDS_ABOUT_BOX_ERROR_DURING_UPDATE_CHECK
#define IDS_ABOUT_BOX_ERROR_UPDATE_CHECK_FAILED
#define IDS_ABOUT_BOX_EXTERNAL_UPDATE_IS_RUNNING
#define IDS_ABOUT_BOX_GOOGLE_UPDATE_ERROR
#define IDS_OMNIBOX_PLACEHOLDER_TEXT
#define IDS_PASTE_AND_GO
#define IDS_PASTE_AND_SEARCH
#define IDS_SHOW_URL
#define IDS_OMNIBOX_KEYWORD_HINT
#define IDS_OMNIBOX_EXTENSION_KEYWORD_HINT
#define IDS_OMNIBOX_KEYWORD_HINT_KEY_ACCNAME
#define IDS_OMNIBOX_KEYWORD_HINT_TOUCH
#define IDS_OMNIBOX_EXTENSION_KEYWORD_HINT_TOUCH
#define IDS_OMNIBOX_KEYWORD_TEXT
#define IDS_OMNIBOX_KEYWORD_TEXT_MD
#define IDS_CLICK_TO_VIEW_DOODLE
#define IDS_OMNIBOX_CLEAR_ALL
#define IDS_SEARCH_OR_TYPE_WEB_ADDRESS
#define IDS_OMNIBOX_WHY_THIS_SUGGESTION
#define IDS_OMNIBOX_REMOVE_SUGGESTION
#define IDS_OMNIBOX_REMOVE_SUGGESTION_BUBBLE_TITLE
#define IDS_OMNIBOX_REMOVE_SUGGESTION_BUBBLE_DESCRIPTION
#define IDS_GOOGLE_SEARCH_BOX_EMPTY_HINT
#define IDS_GOOGLE_SEARCH_BOX_EMPTY_HINT_MD
#define IDS_GOOGLE_SEARCH_BOX_EMPTY_HINT_SHORT
#define IDS_NTP_CUSTOM_LINKS_ADD_SHORTCUT_TOOLTIP
#define IDS_NTP_CUSTOM_LINKS_ADD_SHORTCUT_TITLE
#define IDS_NTP_CUSTOM_LINKS_EDIT_SHORTCUT_TOOLTIP
#define IDS_NTP_CUSTOM_LINKS_EDIT_SHORTCUT
#define IDS_UPLOAD_IMAGE_FORMAT
#define IDS_NTP_CUSTOM_LINKS_NAME
#define IDS_NTP_CUSTOM_LINKS_URL
#define IDS_NTP_CUSTOM_LINKS_REMOVE
#define IDS_NTP_CUSTOM_LINKS_CANCEL
#define IDS_NTP_CUSTOM_LINKS_DONE
#define IDS_NTP_CUSTOM_LINKS_INVALID_URL
#define IDS_NTP_CUSTOM_LINKS_SHORTCUT_EXISTS
#define IDS_NTP_CUSTOM_LINKS_CANT_CREATE
#define IDS_NTP_CUSTOM_LINKS_CANT_EDIT
#define IDS_NTP_CUSTOM_LINKS_CANT_REMOVE
#define IDS_NTP_CONFIRM_MSG_SHORTCUT_REMOVED
#define IDS_NTP_CONFIRM_MSG_SHORTCUT_EDITED
#define IDS_NTP_CONFIRM_MSG_SHORTCUT_ADDED
#define IDS_NTP_CONFIRM_MSG_RESTORE_DEFAULTS
#define IDS_NTP_CUSTOM_BG_CHROME_WALLPAPERS
#define IDS_NTP_CUSTOM_BG_UPLOAD_AN_IMAGE
#define IDS_NTP_CUSTOM_BG_SELECT_A_COLLECTION
#define IDS_NTP_CUSTOM_BG_DAILY_REFRESH
#define IDS_NTP_CUSTOM_BG_SURPRISE_ME
#define IDS_NTP_CUSTOM_BG_RESTORE_DEFAULT
#define IDS_NTP_CUSTOM_BG_CANCEL
#define IDS_NTP_CONNECTION_ERROR_NO_PERIOD
#define IDS_NTP_CONNECTION_ERROR
#define IDS_NTP_ERROR_MORE_INFO
#define IDS_NTP_CUSTOM_BG_BACKGROUNDS_UNAVAILABLE
#define IDS_NTP_CUSTOM_BG_IMAGE_UNAVAILABLE
#define IDS_NTP_CUSTOM_BG_IMAGE_NOT_USABLE
#define IDS_NTP_CUSTOM_BG_BACK_LABEL
#define IDS_NTP_CUSTOM_BG_IMAGE_SELECTED
#define IDS_NTP_CUSTOM_BG_CUSTOMIZE_NTP_LABEL
#define IDS_NTP_DISMISS_PROMO
#define IDS_NTP_DOODLE_SHARE_LABEL
#define IDS_NTP_DOODLE_SHARE_DIALOG_CLOSE_LABEL
#define IDS_NTP_DOODLE_SHARE_DIALOG_FACEBOOK_LABEL
#define IDS_NTP_DOODLE_SHARE_DIALOG_TWITTER_LABEL
#define IDS_NTP_DOODLE_SHARE_DIALOG_MAIL_LABEL
#define IDS_NTP_DOODLE_SHARE_DIALOG_COPY_LABEL
#define IDS_NTP_DOODLE_SHARE_DIALOG_LINK_LABEL
#define IDS_NTP_CUSTOMIZE_BUTTON_LABEL
#define IDS_NTP_CUSTOMIZE_MENU_BACKGROUND_LABEL
#define IDS_NTP_CUSTOMIZE_MENU_BACKGROUND_DISABLED_LABEL
#define IDS_NTP_CUSTOMIZE_MENU_SHORTCUTS_LABEL
#define IDS_NTP_CUSTOMIZE_MENU_COLOR_LABEL
#define IDS_NTP_CUSTOMIZE_NO_BACKGROUND_LABEL
#define IDS_NTP_CUSTOMIZE_UPLOAD_FROM_DEVICE_LABEL
#define IDS_NTP_CUSTOMIZE_HIDE_SHORTCUTS_LABEL
#define IDS_NTP_CUSTOMIZE_HIDE_SHORTCUTS_DESC
#define IDS_NTP_CUSTOMIZE_MY_SHORTCUTS_LABEL
#define IDS_NTP_CUSTOMIZE_MOST_VISITED_LABEL
#define IDS_NTP_CUSTOMIZE_MOST_VISITED_DESC
#define IDS_NTP_CUSTOMIZE_MY_SHORTCUTS_DESC
#define IDS_NTP_CUSTOMIZE_3PT_THEME_DESC
#define IDS_NTP_CUSTOMIZE_3PT_THEME_UNINSTALL
#define IDS_NTP_CUSTOMIZE_COLOR_PICKER_LABEL
#define IDS_NTP_CUSTOMIZE_DEFAULT_LABEL
#define IDS_NTP_COLORS_WARM_GREY
#define IDS_NTP_COLORS_COOL_GREY
#define IDS_NTP_COLORS_MIDNIGHT_BLUE
#define IDS_NTP_COLORS_BLACK
#define IDS_NTP_COLORS_BEIGE_AND_WHITE
#define IDS_NTP_COLORS_YELLOW_AND_WHITE
#define IDS_NTP_COLORS_GREEN_AND_WHITE
#define IDS_NTP_COLORS_LIGHT_TEAL_AND_WHITE
#define IDS_NTP_COLORS_LIGHT_PURPLE_AND_WHITE
#define IDS_NTP_COLORS_PINK_AND_WHITE
#define IDS_NTP_COLORS_BEIGE
#define IDS_NTP_COLORS_ORANGE
#define IDS_NTP_COLORS_LIGHT_GREEN
#define IDS_NTP_COLORS_LIGHT_TEAL
#define IDS_NTP_COLORS_LIGHT_BLUE
#define IDS_NTP_COLORS_PINK
#define IDS_NTP_COLORS_DARK_PINK_AND_RED
#define IDS_NTP_COLORS_DARK_RED_AND_ORANGE
#define IDS_NTP_COLORS_DARK_GREEN
#define IDS_NTP_COLORS_DARK_TEAL
#define IDS_NTP_COLORS_DARK_BLUE
#define IDS_NTP_COLORS_DARK_PURPLE
#define IDS_EXTENSIONS_PROMO_PERFORMANCE
#define IDS_EXTENSIONS_PROMO_PRIVACY
#define IDS_EXTENSIONS_PROMO_NEUTRAL
#define IDS_TOOLTIP_BACK
#define IDS_ACCDESCRIPTION_BACK
#define IDS_TOOLTIP_FORWARD
#define IDS_ACCDESCRIPTION_FORWARD
#define IDS_TOOLTIP_HOME
#define IDS_TOOLTIP_RELOAD
#define IDS_TOOLTIP_RELOAD_WITH_MENU
#define IDS_TOOLTIP_STOP
#define IDS_TOOLTIP_EXTENSIONS_BUTTON
#define IDS_TOOLTIP_LOCATION_ICON
#define IDS_TOOLTIP_NEW_TAB
#define IDS_TOOLTIP_MIC_SEARCH
#define IDS_TOOLTIP_SAVE_CREDIT_CARD
#define IDS_TOOLTIP_SAVE_CREDIT_CARD_PENDING
#define IDS_TOOLTIP_SAVE_CREDIT_CARD_FAILURE
#define IDS_TOOLTIP_MIGRATE_LOCAL_CARD
#define IDS_TOOLTIP_TRANSLATE
#define IDS_TOOLTIP_ZOOM
#define IDS_TOOLTIP_ZOOM_EXTENSION_ICON
#define IDS_ZOOM_SET_DEFAULT
#define IDS_TOOLTIP_FIND
#define IDS_TOOLTIP_WEBUI_TAB_STRIP_TAB_COUNTER
#define IDS_TOOLTIP_INTENT_PICKER_ICON
#define IDS_INTENT_PICKER_BUBBLE_VIEW_OPEN_WITH
#define IDS_INTENT_PICKER_BUBBLE_VIEW_REMEMBER_SELECTION
#define IDS_INTENT_PICKER_BUBBLE_VIEW_OPEN
#define IDS_INTENT_PICKER_BUBBLE_VIEW_STAY_IN_CHROME
#define IDS_INTENT_PICKER_BUBBLE_VIEW_INITIATING_ORIGIN
#define IDS_ACCESSIBLE_INCOGNITO_WINDOW_TITLE_FORMAT
#define IDS_ACCESSIBLE_GUEST_WINDOW_TITLE_FORMAT
#define IDS_ACCESSIBLE_WINDOW_TITLE_WITH_PROFILE_FORMAT
#define IDS_ACCNAME_APP_UPGRADE_RECOMMENDED
#define IDS_ACCNAME_FULLSCREEN
#define IDS_ACCNAME_HOME
#define IDS_ACCNAME_RELOAD
#define IDS_ACCNAME_FIND
#define IDS_ACCNAME_BOOKMARKS
#define IDS_ACCNAME_BOOKMARKS_CHEVRON
#define IDS_ACCNAME_BOOKMARKS_MENU
#define IDS_ACCNAME_SEPARATOR
#define IDS_ACCNAME_EXTENSIONS
#define IDS_ACCNAME_NEWTAB
#define IDS_ACCNAME_MINIMIZE
#define IDS_ACCNAME_MAXIMIZE
#define IDS_ACCNAME_RESTORE
#define IDS_ACCNAME_CLOSE_TAB
#define IDS_ACCNAME_ZOOM_SET_DEFAULT
#define IDS_ACCESSIBILITY_EVENTS_PERMISSION_FRAGMENT
#define IDS_CLIPBOARD_PERMISSION_FRAGMENT
#define IDS_ALLOWED_CLIPBOARD_TITLE
#define IDS_BLOCKED_CLIPBOARD_TITLE
#define IDS_ALLOWED_CLIPBOARD_MESSAGE
#define IDS_ALLOWED_CLIPBOARD_BLOCK
#define IDS_ALLOWED_CLIPBOARD_NO_ACTION
#define IDS_BLOCKED_CLIPBOARD_MESSAGE
#define IDS_BLOCKED_CLIPBOARD_UNBLOCK
#define IDS_BLOCKED_CLIPBOARD_NO_ACTION
#define IDS_BOOKMARK_PROMO_0
#define IDS_BOOKMARK_PROMO_1
#define IDS_BOOKMARK_PROMO_2
#define IDS_GLOBAL_MEDIA_CONTROLS_PROMO
#define IDS_INCOGNITOWINDOW_PROMO_0
#define IDS_INCOGNITOWINDOW_PROMO_1
#define IDS_INCOGNITOWINDOW_PROMO_2
#define IDS_INCOGNITOWINDOW_PROMO_3
#define IDS_NEWTAB_PROMO_0
#define IDS_NEWTAB_PROMO_1
#define IDS_NEWTAB_PROMO_2
#define IDS_REOPEN_TAB_PROMO
#define IDS_REOPEN_TAB_PROMO_SCREENREADER
#define IDS_WEBUI_TAB_STRIP_PROMO
#define IDS_BROWSER_HANGMONITOR
#define IDS_BROWSER_HANGMONITOR_RENDERER_TITLE
#define IDS_BROWSER_HANGMONITOR_RENDERER
#define IDS_BROWSER_HANGMONITOR_RENDERER_INFOBAR
#define IDS_BROWSER_HANGMONITOR_IFRAME_TITLE
#define IDS_BROWSER_HANGMONITOR_RENDERER_INFOBAR_END
#define IDS_BROWSER_HANGMONITOR_RENDERER_WAIT
#define IDS_BROWSER_HANGMONITOR_RENDERER_END
#define IDS_BROWSER_HANGMONITOR_PLUGIN_INFOBAR
#define IDS_BROWSER_HANGMONITOR_PLUGIN_INFOBAR_KILLBUTTON
#define IDS_PASSWORDS_AUTO_SIGNIN_TITLE
#define IDS_PASSWORDS_AUTO_SIGNIN_DESCRIPTION
#define IDS_PASSWORDS_VIA_FEDERATION
#define IDS_PASSWORDS_PAGE_VIEW_HIDE_BUTTON
#define IDS_CONFIRM_MESSAGEBOX_YES_BUTTON_LABEL
#define IDS_CONFIRM_MESSAGEBOX_NO_BUTTON_LABEL
#define IDS_PASSWORD_MANAGER_CANCEL_BUTTON
#define IDS_PASSWORD_MANAGER_SAVE_BUTTON
#define IDS_PASSWORD_MANAGER_UPDATE_BUTTON
#define IDS_PASSWORD_MANAGER_BUBBLE_BLACKLIST_BUTTON
#define IDS_PASSWORD_MANAGER_TOOLTIP_SAVE
#define IDS_PASSWORD_MANAGER_TOOLTIP_MANAGE
#define IDS_PASSWORD_MANAGER_IMPORT_BUTTON
#define IDS_PASSWORD_MANAGER_IMPORT_DIALOG_TITLE
#define IDS_PASSWORD_MANAGER_EXPORT_DIALOG_TITLE
#define IDS_PASSWORD_MANAGER_USERNAME_LABEL
#define IDS_PASSWORD_MANAGER_PASSWORD_LABEL
#define IDS_IMPORT_FROM_IE
#define IDS_IMPORT_FROM_EDGE
#define IDS_IMPORT_FROM_FIREFOX
#define IDS_IMPORT_FROM_ICEWEASEL
#define IDS_IMPORT_FROM_SAFARI
#define IDS_IMPORT_FROM_BOOKMARKS_HTML_FILE
#define IDS_IMPORTER_LOCK_TITLE
#define IDS_IMPORTER_LOCK_TEXT
#define IDS_IMPORTER_LOCK_OK
#define IDS_FEEDBACK_REPORT_PAGE_TITLE
#define IDS_FEEDBACK_REPORT_PAGE_TITLE_SAD_TAB_FLOW
#define IDS_FEEDBACK_MINIMIZE_BUTTON_LABEL
#define IDS_FEEDBACK_CLOSE_BUTTON_LABEL
#define IDS_FEEDBACK_REPORT_URL_LABEL
#define IDS_FEEDBACK_USER_EMAIL_LABEL
#define IDS_FEEDBACK_ANONYMOUS_EMAIL_OPTION
#define IDS_FEEDBACK_SCREENSHOT_LABEL
#define IDS_FEEDBACK_SCREENSHOT_A11Y_TEXT
#define IDS_FEEDBACK_INCLUDE_PERFORMANCE_TRACE_CHECKBOX
#define IDS_FEEDBACK_BLUETOOTH_LOGS_CHECKBOX
#define IDS_FEEDBACK_ASSISTANT_LOGS_MESSAGE
#define IDS_FEEDBACK_BLUETOOTH_LOGS_MESSAGE
#define IDS_FEEDBACK_OFFLINE_DIALOG_TITLE
#define IDS_FEEDBACK_OFFLINE_DIALOG_TEXT
#define IDS_FEEDBACK_INCLUDE_SYSTEM_INFORMATION_CHKBOX
#define IDS_FEEDBACK_INCLUDE_ASSISTANT_INFORMATION_CHKBOX
#define IDS_FEEDBACK_ATTACH_FILE_NOTE
#define IDS_FEEDBACK_ATTACH_FILE_LABEL
#define IDS_FEEDBACK_READING_FILE
#define IDS_FEEDBACK_ATTACH_FILE_TO_BIG
#define IDS_FEEDBACK_IWLWIFI_DEBUG_DUMP_EXPLAINER
#define IDS_FEEDBACK_PRIVACY_NOTE
#define IDS_FEEDBACK_NO_DESCRIPTION
#define IDS_FEEDBACK_SEND_REPORT
#define IDS_FEEDBACK_SYSINFO_PAGE_TITLE
#define IDS_FEEDBACK_SYSINFO_PAGE_LOADING
#define IDS_FEEDBACK_ADDITIONAL_INFO_LABEL
#define IDS_CLEAR_BROWSING_DATA_TITLE
#define IDS_FLASH_PERMISSION_FRAGMENT
#define IDS_CLEAR_BROWSING_DATA_HISTORY_NOTICE
#define IDS_CLEAR_BROWSING_DATA_HISTORY_NOTICE_TITLE
#define IDS_CLEAR_BROWSING_DATA_HISTORY_NOTICE_OK
#define IDS_MEDIA_SELECTED_MIC_LABEL
#define IDS_MEDIA_SELECTED_CAMERA_LABEL
#define IDS_MEDIA_MENU_NO_DEVICE_TITLE
#define IDS_HANDLERS_BUBBLE_MANAGE_LINK
#define IDS_ZOOMLEVELS_CHROME_ERROR_PAGES_LABEL
#define IDS_UPGRADE_ERROR
#define IDS_UPGRADE_ERROR_DETAILS
#define IDS_UPGRADE_DISABLED_BY_POLICY
#define IDS_UPGRADE_DISABLED_BY_POLICY_MANUAL
#define IDS_REPORT_AN_ISSUE
#define IDS_CHROME_CLEANUP_PROMPT_DETAILS_BUTTON_LABEL
#define IDS_CHROME_CLEANUP_PROMPT_REMOVE_BUTTON_LABEL
#define IDS_CHROME_CLEANUP_PROMPT_TITLE
#define IDS_CHROME_CLEANUP_REBOOT_PROMPT_TITLE
#define IDS_CHROME_CLEANUP_REBOOT_PROMPT_RESTART_BUTTON_LABEL
#define IDS_CHROME_CLEANUP_LOGS_PERMISSION
#define IDS_SETTINGS_RESET_PROMPT_TITLE_SEARCH_ENGINE
#define IDS_SETTINGS_RESET_PROMPT_TITLE_STARTUP_PAGE
#define IDS_SETTINGS_RESET_PROMPT_TITLE_HOMEPAGE
#define IDS_SETTINGS_RESET_PROMPT_ACCEPT_BUTTON_LABEL
#define IDS_SETTINGS_RESET_PROMPT_EXPLANATION_FOR_SEARCH_ENGINE_NO_EXTENSIONS
#define IDS_SETTINGS_RESET_PROMPT_EXPLANATION_FOR_STARTUP_PAGE_SINGLE_NO_EXTENSIONS
#define IDS_SETTINGS_RESET_PROMPT_EXPLANATION_FOR_STARTUP_PAGE_MULTIPLE_NO_EXTENSIONS
#define IDS_SETTINGS_RESET_PROMPT_EXPLANATION_FOR_HOMEPAGE_NO_EXTENSIONS
#define IDS_REENABLE_UPDATES
#define IDS_PICTURE_IN_PICTURE_TITLE_TEXT
#define IDS_PICTURE_IN_PICTURE_PAUSE_CONTROL_TEXT
#define IDS_PICTURE_IN_PICTURE_PLAY_CONTROL_TEXT
#define IDS_PICTURE_IN_PICTURE_REPLAY_CONTROL_TEXT
#define IDS_PICTURE_IN_PICTURE_BACK_TO_TAB_CONTROL_TEXT
#define IDS_PICTURE_IN_PICTURE_MUTE_CONTROL_TEXT
#define IDS_PICTURE_IN_PICTURE_UNMUTE_CONTROL_TEXT
#define IDS_PICTURE_IN_PICTURE_SKIP_AD_CONTROL_TEXT
#define IDS_PICTURE_IN_PICTURE_CLOSE_CONTROL_TEXT
#define IDS_PICTURE_IN_PICTURE_RESIZE_HANDLE_TEXT
#define IDS_PICTURE_IN_PICTURE_PLAY_PAUSE_CONTROL_ACCESSIBLE_TEXT
#define IDS_PICTURE_IN_PICTURE_NEXT_TRACK_CONTROL_ACCESSIBLE_TEXT
#define IDS_PICTURE_IN_PICTURE_PREVIOUS_TRACK_CONTROL_ACCESSIBLE_TEXT
#define IDS_PICTURE_IN_PICTURE_CONFIRM_CLOSE_TITLE
#define IDS_PICTURE_IN_PICTURE_CONFIRM_LEAVE_TITLE
#define IDS_PICTURE_IN_PICTURE_CONFIRM_DESCRIPTION
#define IDS_PICTURE_IN_PICTURE_CONFIRM_CLOSE_TEXT
#define IDS_PICTURE_IN_PICTURE_CONFIRM_LEAVE_TEXT
#define IDS_PICTURE_IN_PICTURE_CANCEL_TEXT
#define IDS_LOAD_STATE_WAITING_FOR_SOCKET_SLOT
#define IDS_LOAD_STATE_WAITING_FOR_DELEGATE
#define IDS_LOAD_STATE_WAITING_FOR_DELEGATE_GENERIC
#define IDS_LOAD_STATE_WAITING_FOR_CACHE
#define IDS_LOAD_STATE_WAITING_FOR_APPCACHE
#define IDS_LOAD_STATE_ESTABLISHING_PROXY_TUNNEL
#define IDS_LOAD_STATE_RESOLVING_PROXY_FOR_URL
#define IDS_LOAD_STATE_RESOLVING_HOST_IN_PAC_FILE
#define IDS_LOAD_STATE_DOWNLOADING_PAC_FILE
#define IDS_LOAD_STATE_RESOLVING_HOST
#define IDS_LOAD_STATE_CONNECTING
#define IDS_LOAD_STATE_SSL_HANDSHAKE
#define IDS_LOAD_STATE_SENDING_REQUEST
#define IDS_LOAD_STATE_SENDING_REQUEST_WITH_PROGRESS
#define IDS_LOAD_STATE_WAITING_FOR_RESPONSE
#define IDS_TAB_CXMENU_NEWTABTORIGHT
#define IDS_TAB_CXMENU_RELOAD
#define IDS_TAB_CXMENU_DUPLICATE
#define IDS_TAB_CXMENU_CLOSETAB
#define IDS_TAB_CXMENU_CLOSEOTHERTABS
#define IDS_TAB_CXMENU_CLOSETABSTORIGHT
#define IDS_TAB_CXMENU_FOCUS_THIS_TAB
#define IDS_TAB_CXMENU_PIN_TAB
#define IDS_TAB_CXMENU_UNPIN_TAB
#define IDS_TAB_CXMENU_SOUND_MUTE_SITE
#define IDS_TAB_CXMENU_SOUND_UNMUTE_SITE
#define IDS_TAB_CXMENU_ADD_TAB_TO_NEW_GROUP
#define IDS_TAB_CXMENU_ADD_TAB_TO_EXISTING_GROUP
#define IDS_TAB_CXMENU_REMOVE_TAB_FROM_GROUP
#define IDS_TAB_CXMENU_PLACEHOLDER_GROUP_TITLE
#define IDS_TAB_GROUP_LG_HEADER_CXMENU_NEW_TAB_IN_GROUP
#define IDS_TAB_GROUP_LG_HEADER_CXMENU_UNGROUP
#define IDS_TAB_GROUP_LG_HEADER_CXMENU_CLOSE_GROUP
#define IDS_TAB_GROUP_LG_HEADER_CXMENU_SEND_FEEDBACK
#define IDS_APP_MENU_RELOAD
#define IDS_APP_MENU_NEW_WEB_PAGE
#define IDS_APP_MENU_BUTTON_UPDATE
#define IDS_APP_MENU_BUTTON_ERROR
#define IDS_MEDIA_SCREEN_CAPTURE_CONFIRMATION_TITLE
#define IDS_MEDIA_SCREEN_CAPTURE_CONFIRMATION_TEXT
#define IDS_MEDIA_SCREEN_AND_AUDIO_CAPTURE_CONFIRMATION_TEXT
#define IDS_MEDIA_SCREEN_CAPTURE_NOTIFICATION_TEXT
#define IDS_MEDIA_SCREEN_CAPTURE_NOTIFICATION_TEXT_DELEGATED
#define IDS_MEDIA_SCREEN_CAPTURE_WITH_AUDIO_NOTIFICATION_TEXT
#define IDS_MEDIA_SCREEN_CAPTURE_WITH_AUDIO_NOTIFICATION_TEXT_DELEGATED
#define IDS_MEDIA_WINDOW_CAPTURE_NOTIFICATION_TEXT
#define IDS_MEDIA_WINDOW_CAPTURE_NOTIFICATION_TEXT_DELEGATED
#define IDS_MEDIA_TAB_CAPTURE_NOTIFICATION_TEXT
#define IDS_MEDIA_TAB_CAPTURE_NOTIFICATION_TEXT_DELEGATED
#define IDS_MEDIA_TAB_CAPTURE_WITH_AUDIO_NOTIFICATION_TEXT
#define IDS_MEDIA_TAB_CAPTURE_WITH_AUDIO_NOTIFICATION_TEXT_DELEGATED
#define IDS_MEDIA_SCREEN_CAPTURE_NOTIFICATION_SOURCE
#define IDS_MEDIA_SCREEN_CAPTURE_NOTIFICATION_STOP
#define IDS_PLATFORM_KEYS_SELECT_CERT_DIALOG_TEXT
#define IDS_UNSAFE_FRAME_MESSAGE
#define IDS_CLIENT_CERT_DIALOG_TITLE
#define IDS_CLIENT_CERT_DIALOG_TEXT
#define IDS_CRYPTO_MODULE_AUTH_DIALOG_TITLE
#define IDS_CRYPTO_MODULE_AUTH_DIALOG_TEXT_CERT_ENROLLMENT
#define IDS_CRYPTO_MODULE_AUTH_DIALOG_TEXT_CLIENT_AUTH
#define IDS_CRYPTO_MODULE_AUTH_DIALOG_TEXT_LIST_CERTS
#define IDS_CRYPTO_MODULE_AUTH_DIALOG_TEXT_CERT_IMPORT
#define IDS_CRYPTO_MODULE_AUTH_DIALOG_TEXT_CERT_EXPORT
#define IDS_CRYPTO_MODULE_AUTH_DIALOG_PASSWORD_FIELD
#define IDS_CRYPTO_MODULE_AUTH_DIALOG_OK_BUTTON_LABEL
#define IDS_FR_ENABLE_LOGGING
#define IDS_CRASHED_TAB_FEEDBACK_MESSAGE
#define IDS_CRASHED_TAB_FEEDBACK_LINK
#define IDS_KILLED_TAB_FEEDBACK_MESSAGE
#define IDS_HIDE_ICONS_NOT_SUPPORTED
#define IDS_RELAUNCH_BUTTON
#define IDS_TOOLBAR_INFORM_SET_HOME_PAGE
#define IDS_MANAGE_EXTENSIONS_SETTING_WINDOWS_TITLE
#define IDS_GOOGLE_CLOUD_PRINT
#define IDS_CLOUD_PRINT_CONNECTOR_DISABLED_BUTTON
#define IDS_CLOUD_PRINT_CONNECTOR_ENABLED_LABEL
#define IDS_CLOUD_PRINT_CONNECTOR_ENABLED_BUTTON
#define IDS_CLOUD_PRINT_CONNECTOR_ENABLING_BUTTON
#define IDS_CONTROLLED_SETTING_POLICY
#define IDS_CONTROLLED_SETTING_EXTENSION
#define IDS_CONTROLLED_SETTING_EXTENSION_WITHOUT_NAME
#define IDS_CONTROLLED_SETTING_RECOMMENDED
#define IDS_CONTROLLED_SETTING_HAS_RECOMMENDATION
#define IDS_CONTROLLED_SETTING_CHILD_RESTRICTION
#define IDS_EXTENSIONS_INSTALL_LOCATION_UNKNOWN
#define IDS_EXTENSIONS_INSTALL_LOCATION_3RD_PARTY
#define IDS_EXTENSIONS_INSTALL_LOCATION_ENTERPRISE
#define IDS_EXTENSIONS_INSTALL_LOCATION_SHARED_MODULE
#define IDS_EXTENSIONS_BLACKLISTED_MALWARE
#define IDS_EXTENSIONS_BLACKLISTED_SECURITY_VULNERABILITY
#define IDS_EXTENSIONS_BLACKLISTED_CWS_POLICY_VIOLATION
#define IDS_EXTENSIONS_BLACKLISTED_POTENTIALLY_UNWANTED
#define IDS_RESET_PROFILE_SETTINGS_EXPLANATION
#define IDS_TRIGGERED_RESET_PROFILE_SETTINGS_TITLE
#define IDS_TRIGGERED_RESET_PROFILE_SETTINGS_EXPLANATION
#define IDS_TRIGGERED_RESET_PROFILE_SETTINGS_DEFAULT_TOOL_NAME
#define IDS_RESET_PROFILE_SETTINGS_LOCALE
#define IDS_RESET_PROFILE_SETTINGS_STARTUP_URLS
#define IDS_RESET_PROFILE_SETTINGS_STARTUP_TYPE
#define IDS_RESET_PROFILE_SETTINGS_HOMEPAGE
#define IDS_RESET_PROFILE_SETTINGS_HOMEPAGE_IS_NTP
#define IDS_RESET_PROFILE_SETTINGS_YES
#define IDS_RESET_PROFILE_SETTINGS_NO
#define IDS_RESET_PROFILE_SETTINGS_SHOW_HOME_BUTTON
#define IDS_RESET_PROFILE_SETTINGS_DSE
#define IDS_RESET_PROFILE_SETTINGS_EXTENSIONS
#define IDS_RESET_PROFILE_SETTINGS_SHORTCUTS
#define IDS_RESET_PROFILE_SETTINGS_PROCESSING_SHORTCUTS
#define IDS_AUTOFILL_DIALOG_PLACEHOLDER_EXPIRY_MONTH
#define IDS_AUTOFILL_DIALOG_PLACEHOLDER_EXPIRY_YEAR
#define IDS_AUTOFILL_FROM_GOOGLE_ACCOUNT
#define IDS_OMNIBOX_ICON_SEND_TAB_TO_SELF
#define IDS_OMNIBOX_TOOLTIP_SEND_TAB_TO_SELF
#define IDS_OMNIBOX_BUBBLE_ITEM_SUBTITLE_TODAY_SEND_TAB_TO_SELF
#define IDS_OMNIBOX_BUBBLE_ITEM_SUBTITLE_DAY_SEND_TAB_TO_SELF
#define IDS_OMNIBOX_BUBBLE_ITEM_SUBTITLE_DAYS_SEND_TAB_TO_SELF
#define IDS_CONTEXT_MENU_SEND_TAB_TO_SELF_SINGLE_TARGET
#define IDS_CONTEXT_MENU_SEND_TAB_TO_SELF
#define IDS_LINK_MENU_SEND_TAB_TO_SELF
#define IDS_LINK_MENU_SEND_TAB_TO_SELF_SINGLE_TARGET
#define IDS_CONTEXT_MENU_GENERATE_QR_CODE_PAGE
#define IDS_CONTEXT_MENU_GENERATE_QR_CODE_IMAGE
#define IDS_OMNIBOX_QRCODE_GENERATOR_ICON_LABEL
#define IDS_OMNIBOX_QRCODE_GENERATOR_ICON_TOOLTIP
#define IDS_BROWSER_SHARING_QR_CODE_DIALOG_TITLE
#define IDS_BROWSER_SHARING_QR_CODE_DIALOG_URL_TEXTFIELD_ACCESSIBLE_NAME
#define IDS_BROWSER_SHARING_QR_CODE_DIALOG_TOOLTIP
#define IDS_BROWSER_SHARING_QR_CODE_DIALOG_DOWNLOAD_BUTTON_LABEL
#define IDS_SHARING_REMOTE_COPY_NOTIFICATION_TITLE_TEXT_CONTENT_UNKNOWN_DEVICE
#define IDS_SHARING_REMOTE_COPY_NOTIFICATION_TITLE_TEXT_CONTENT
#define IDS_SHARING_REMOTE_COPY_NOTIFICATION_TITLE_IMAGE_CONTENT_UNKNOWN_DEVICE
#define IDS_SHARING_REMOTE_COPY_NOTIFICATION_TITLE_IMAGE_CONTENT
#define IDS_SHARING_REMOTE_COPY_NOTIFICATION_DESCRIPTION
#define IDS_CONTENT_CONTEXT_SHARING_CLICK_TO_CALL_MULTIPLE_DEVICES
#define IDS_CONTENT_CONTEXT_SHARING_CLICK_TO_CALL_SINGLE_DEVICE
#define IDS_CONTENT_CONTEXT_SHARING_SHARED_CLIPBOARD_MULTIPLE_DEVICES
#define IDS_CONTENT_CONTEXT_SHARING_SHARED_CLIPBOARD_SINGLE_DEVICE
#define IDS_CONTENT_CONTEXT_SHARING_SHARED_CLIPBOARD_NOTIFICATION_TITLE_UNKNOWN_DEVICE
#define IDS_CONTENT_CONTEXT_SHARING_SHARED_CLIPBOARD_NOTIFICATION_TITLE
#define IDS_CONTENT_CONTEXT_SHARING_SHARED_CLIPBOARD_NOTIFICATION_DESCRIPTION
#define IDS_OMNIBOX_TOOLTIP_SHARED_CLIPBOARD
#define IDS_COLLECTED_COOKIES_DIALOG_TITLE
#define IDS_COLLECTED_COOKIES_ALLOWED_COOKIES_LABEL
#define IDS_COLLECTED_COOKIES_BLOCKED_COOKIES_LABEL
#define IDS_COLLECTED_COOKIES_BLOCKED_THIRD_PARTY_BLOCKING_ENABLED
#define IDS_COLLECTED_COOKIES_ALLOW_BUTTON
#define IDS_COLLECTED_COOKIES_SESSION_ONLY_BUTTON
#define IDS_COLLECTED_COOKIES_BLOCK_BUTTON
#define IDS_COLLECTED_COOKIES_ALLOW_RULE_CREATED
#define IDS_COLLECTED_COOKIES_BLOCK_RULE_CREATED
#define IDS_COLLECTED_COOKIES_SESSION_RULE_CREATED
#define IDS_COLLECTED_COOKIES_ALLOWED_COOKIES_TAB_LABEL
#define IDS_COLLECTED_COOKIES_BLOCKED_COOKIES_TAB_LABEL
#define IDS_COLLECTED_COOKIES_ALLOWED_AUX_TEXT
#define IDS_COLLECTED_COOKIES_BLOCKED_AUX_TEXT
#define IDS_COLLECTED_COOKIES_CLEAR_ON_EXIT_AUX_TEXT
#define IDS_COLLECTED_COOKIES_INFOBAR_MESSAGE
#define IDS_COLLECTED_COOKIES_INFOBAR_BUTTON
#define IDS_ACCNAME_INFOBAR_CONTAINER
#define IDS_ACCNAME_INFOBAR
#define IDS_ONE_CLICK_BUBBLE_UNDO
#define IDS_ONE_CLICK_SIGNIN_BUBBLE_MESSAGE
#define IDS_ONE_CLICK_SIGNIN_DIALOG_OK_BUTTON
#define IDS_ONE_CLICK_SIGNIN_DIALOG_UNDO_BUTTON
#define IDS_ONE_CLICK_SIGNIN_DIALOG_ADVANCED
#define IDS_ENTERPRISE_SIGNIN_CANCEL
#define IDS_ENTERPRISE_SIGNIN_CREATE_NEW_PROFILE
#define IDS_ENTERPRISE_SIGNIN_CONTINUE
#define IDS_ENTERPRISE_SIGNIN_ALERT
#define IDS_PROFILE_WILL_BE_DELETED_DIALOG_TITLE
#define IDS_PROFILE_WILL_BE_DELETED_DIALOG_DESCRIPTION
#define IDS_MANAGED_WITH_HYPERLINK
#define IDS_MANAGED_BY_WITH_HYPERLINK
#define IDS_COOKIES_REMOVE_LABEL
#define IDS_COOKIES_COOKIE_NAME_LABEL
#define IDS_COOKIES_COOKIE_CONTENT_LABEL
#define IDS_COOKIES_COOKIE_DOMAIN_LABEL
#define IDS_COOKIES_COOKIE_PATH_LABEL
#define IDS_COOKIES_COOKIE_SENDFOR_LABEL
#define IDS_COOKIES_COOKIE_CREATED_LABEL
#define IDS_COOKIES_COOKIE_EXPIRES_LABEL
#define IDS_COOKIES_COOKIE_EXPIRES_SESSION
#define IDS_COOKIES_COOKIE_SENDFOR_ANY
#define IDS_COOKIES_COOKIE_SENDFOR_SECURE
#define IDS_COOKIES_COOKIE_SENDFOR_SAME_SITE
#define IDS_COOKIES_COOKIE_SENDFOR_SECURE_SAME_SITE
#define IDS_COOKIES_COOKIE_ACCESSIBLE_TO_SCRIPT_YES
#define IDS_COOKIES_COOKIE_ACCESSIBLE_TO_SCRIPT_NO
#define IDS_COOKIES_COOKIE_NONESELECTED
#define IDS_COOKIES_LOCAL_STORAGE_ORIGIN_LABEL
#define IDS_COOKIES_LOCAL_STORAGE_SIZE_ON_DISK_LABEL
#define IDS_COOKIES_LOCAL_STORAGE_LAST_MODIFIED_LABEL
#define IDS_COOKIES_COOKIES
#define IDS_COOKIES_APPLICATION_CACHES
#define IDS_COOKIES_APPLICATION_CACHE
#define IDS_COOKIES_APPLICATION_CACHE_MANIFEST_LABEL
#define IDS_COOKIES_WEB_DATABASES
#define IDS_COOKIES_LOCAL_STORAGE
#define IDS_COOKIES_SESSION_STORAGE
#define IDS_COOKIES_INDEXED_DBS
#define IDS_COOKIES_MEDIA_LICENSE
#define IDS_COOKIES_MEDIA_LICENSES
#define IDS_COOKIES_FILE_SYSTEM
#define IDS_COOKIES_FILE_SYSTEMS
#define IDS_COOKIES_FILE_SYSTEM_USAGE_NONE
#define IDS_COOKIES_LAST_ACCESSED_LABEL
#define IDS_COOKIES_SERVICE_WORKER
#define IDS_COOKIES_SERVICE_WORKERS
#define IDS_COOKIES_SHARED_WORKERS
#define IDS_COOKIES_CACHE_STORAGE
#define IDS_CLIENT_CERT_ECDSA_SIGN
#define IDS_APP_DEFAULT_PAGE_NAME
#define IDS_APP_LAUNCHER_TAB_TITLE
#define IDS_NEW_TAB_GUEST_SESSION_HEADING
#define IDS_NEW_TAB_GUEST_SESSION_DESCRIPTION
#define IDS_NEW_TAB_TILE_GRID_ACCESSIBLE_DESCRIPTION
#define IDS_NEW_TAB_APP_INSTALL_HINT_LABEL
#define IDS_NEW_TAB_MOST_VISITED
#define IDS_NEW_TAB_RESTORE_THUMBNAILS_SHORT_LINK
#define IDS_NEW_TAB_ATTRIBUTION_INTRO
#define IDS_NEW_TAB_THUMBNAIL_REMOVED_NOTIFICATION
#define IDS_NEW_TAB_REMOVE_THUMBNAIL_TOOLTIP
#define IDS_NEW_TAB_PAGE_SWITCHER_CHANGE_TITLE
#define IDS_NEW_TAB_PAGE_SWITCHER_SAME_TITLE
#define IDS_NEW_TAB_VOICE_AUDIO_ERROR
#define IDS_NEW_TAB_VOICE_CLOSE_TOOLTIP
#define IDS_NEW_TAB_VOICE_DETAILS
#define IDS_NEW_TAB_VOICE_LANGUAGE_ERROR
#define IDS_NEW_TAB_VOICE_LISTENING
#define IDS_NEW_TAB_VOICE_NETWORK_ERROR
#define IDS_NEW_TAB_VOICE_NO_TRANSLATION
#define IDS_NEW_TAB_VOICE_NO_VOICE
#define IDS_NEW_TAB_VOICE_OTHER_ERROR
#define IDS_NEW_TAB_VOICE_PERMISSION_ERROR
#define IDS_NEW_TAB_VOICE_READY
#define IDS_NEW_TAB_VOICE_TRY_AGAIN
#define IDS_NEW_TAB_VOICE_WAITING
#define IDS_NEW_TAB_APP_OPTIONS
#define IDS_NEW_TAB_APP_DETAILS
#define IDS_NEW_TAB_APP_CREATE_SHORTCUT
#define IDS_NEW_TAB_APP_INSTALL_LOCALLY
#define IDS_APP_CONTEXT_MENU_SHOW_INFO
#define IDS_APP_CONTEXT_MENU_OPEN_PINNED
#define IDS_APP_CONTEXT_MENU_OPEN_REGULAR
#define IDS_APP_CONTEXT_MENU_OPEN_WINDOW
#define IDS_APP_CONTEXT_MENU_OPEN_FULLSCREEN
#define IDS_APP_CONTEXT_MENU_OPEN_MAXIMIZED
#define IDS_APP_CONTEXT_MENU_OPEN_TAB
#define IDS_SYNC_CONFIRMATION_TITLE
#define IDS_SYNC_CONFIRMATION_SYNC_INFO_TITLE
#define IDS_SYNC_CONFIRMATION_SYNC_INFO_DESC
#define IDS_SYNC_CONFIRMATION_SETTINGS_INFO
#define IDS_SYNC_CONFIRMATION_CONFIRM_BUTTON_LABEL
#define IDS_SYNC_CONFIRMATION_SETTINGS_BUTTON_LABEL
#define IDS_SYNC_DISABLED_CONFIRMATION_CHROME_SYNC_TITLE
#define IDS_SYNC_DISABLED_CONFIRMATION_DETAILS
#define IDS_SYNC_DISABLED_CONFIRMATION_CONFIRM_BUTTON_LABEL
#define IDS_SYNC_DISABLED_CONFIRMATION_UNDO_BUTTON_LABEL
#define IDS_SIGNIN_ERROR_TITLE
#define IDS_SIGNIN_ERROR_EMAIL_TITLE
#define IDS_SIGNIN_ERROR_DICE_EMAIL_TITLE
#define IDS_SIGNIN_ERROR_CLOSE_BUTTON_LABEL
#define IDS_SIGNIN_ERROR_OK_BUTTON_LABEL
#define IDS_SIGNIN_ERROR_SWITCH_BUTTON_LABEL
#define IDS_SIGNIN_ACCESSIBLE_CLOSE_BUTTON
#define IDS_SIGNIN_ACCESSIBLE_BACK_BUTTON
#define IDS_SIGNIN_EMAIL_CONFIRMATION_CREATE_PROFILE_RADIO_BUTTON_TITLE
#define IDS_SIGNIN_EMAIL_CONFIRMATION_CREATE_PROFILE_RADIO_BUTTON_SUBTITLE
#define IDS_SIGNIN_EMAIL_CONFIRMATION_START_SYNC_RADIO_BUTTON_TITLE
#define IDS_SIGNIN_EMAIL_CONFIRMATION_START_SYNC_RADIO_BUTTON_SUBTITLE
#define IDS_SIGNIN_EMAIL_CONFIRMATION_CLOSE_BUTTON_LABEL
#define IDS_SIGNIN_EMAIL_CONFIRMATION_CONFIRM_BUTTON_LABEL
#define IDS_PLUGIN_OUTDATED_PROMPT
#define IDS_PLUGIN_DEPRECATED_PROMPT
#define IDS_PLUGIN_ENABLE_TEMPORARILY
#define IDS_PLUGIN_CRASHED_PROMPT
#define IDS_PLUGIN_DISCONNECTED_PROMPT
#define IDS_RELOAD_PAGE_WITH_PLUGIN
#define IDS_PLUGIN_INITIALIZATION_ERROR_PROMPT
#define IDS_PLUGIN_FLASH_DEPRECATION_PROMPT
#define IDS_EXTERNAL_PROTOCOL_TITLE
#define IDS_EXTERNAL_PROTOCOL_MESSAGE_WITH_INITIATING_ORIGIN
#define IDS_EXTERNAL_PROTOCOL_MESSAGE
#define IDS_EXTERNAL_PROTOCOL_OK_BUTTON_TEXT
#define IDS_EXTERNAL_PROTOCOL_CANCEL_BUTTON_TEXT
#define IDS_EXTERNAL_PROTOCOL_CHECKBOX_TEXT
#define IDS_DIRECTORY_LISTING_HEADER
#define IDS_DIRECTORY_LISTING_PARENT
#define IDS_DIRECTORY_LISTING_NAME
#define IDS_DIRECTORY_LISTING_SIZE
#define IDS_DIRECTORY_LISTING_DATE_MODIFIED
#define IDS_DIRECTORY_LISTING_PARSING_ERROR_BOX_TEXT
#define IDS_SAVE_PAGE_DESC_HTML_ONLY
#define IDS_SAVE_PAGE_DESC_SINGLE_FILE
#define IDS_SAVE_PAGE_DESC_COMPLETE
#define IDS_PROFILE_ERROR_DIALOG_TITLE
#define IDS_COULDNT_OPEN_PROFILE_ERROR
#define IDS_OPEN_PROFILE_DATA_LOSS
#define IDS_PROFILE_ERROR_DIALOG_CHECKBOX
#define IDS_PROFILE_ERROR_FEEDBACK_DESCRIPTION
#define IDS_COULDNT_STARTUP_PROFILE_ERROR
#define IDS_REFUSE_TO_RUN_AS_ROOT
#define IDS_REFUSE_TO_RUN_AS_ROOT_2
#define IDS_PROFILE_ON_NETWORK_WARNING
#define IDS_CANT_WRITE_USER_DIRECTORY_TITLE
#define IDS_MULTI_DOWNLOAD_WARNING
#define IDS_MULTI_DOWNLOAD_PERMISSION_FRAGMENT
#define IDS_RECENT_TABS_MENU
#define IDS_RECENTLY_CLOSED_WINDOW
#define IDS_RECENT_TABS_NO_DEVICE_TABS
#define IDS_HISTORY_MENU
#define IDS_DEFAULT_DOWNLOAD_FILENAME
#define IDS_DEFAULT_BROWSER_INFOBAR_OK_BUTTON_LABEL
#define IDS_USED_EXISTING_BROWSER
#define IDS_DECLINE_RECOVERY
#define IDS_SYNC_ACCOUNT_INFO
#define IDS_SYNC_ACCOUNT_SYNCING
#define IDS_SYNC_ACCOUNT_SYNCING_CUSTOM_DATA_TYPES
#define IDS_SIGNIN_ERROR_DISPLAY_SOURCE
#define IDS_SIGNIN_ERROR_BUBBLE_VIEW_TITLE
#define IDS_SYNC_ERROR_BUBBLE_VIEW_TITLE
#define IDS_SYNC_ERROR_USER_MENU_TITLE
#define IDS_SYNC_ERROR_USER_MENU_SIGNIN_MESSAGE
#define IDS_SYNC_ERROR_USER_MENU_SIGNIN_BUTTON
#define IDS_SYNC_ERROR_USER_MENU_PASSPHRASE_MESSAGE
#define IDS_SYNC_ERROR_USER_MENU_PASSPHRASE_BUTTON
#define IDS_SYNC_ERROR_USER_MENU_RETRIEVE_KEYS_MESSAGE
#define IDS_SYNC_ERROR_USER_MENU_RETRIEVE_KEYS_BUTTON
#define IDS_SYNC_ERROR_USER_MENU_SIGNIN_AGAIN_MESSAGE
#define IDS_SYNC_ERROR_USER_MENU_SIGNIN_AGAIN_BUTTON
#define IDS_SYNC_ERROR_USER_MENU_SIGNOUT_MESSAGE
#define IDS_SYNC_ERROR_USER_MENU_SIGNOUT_BUTTON
#define IDS_SYNC_ERROR_USER_MENU_CONFIRM_SYNC_SETTINGS_BUTTON
#define IDS_SYNC_UNAVAILABLE_ERROR_BUBBLE_VIEW_ACCEPT
#define IDS_SYNC_SIGN_IN_ERROR_BUBBLE_VIEW_ACCEPT
#define IDS_SYNC_SIGN_IN_ERROR_WRENCH_MENU_ITEM
#define IDS_SYNC_OVERVIEW
#define IDS_SYNC_START_SYNC_BUTTON_LABEL
#define IDS_SIGNED_IN_WITH_SYNC_DISABLED_BY_POLICY
#define IDS_SIGNED_IN_WITH_SYNC_STOPPED_VIA_DASHBOARD
#define IDS_SYNC_SETTINGS_NOT_CONFIRMED
#define IDS_SYNC_SETUP_IN_PROGRESS
#define IDS_SYNC_STATUS_UNRECOVERABLE_ERROR
#define IDS_SYNC_STATUS_UNRECOVERABLE_ERROR_NEEDS_SIGNOUT
#define IDS_SYNC_STATUS_NEEDS_PASSWORD
#define IDS_SYNC_STATUS_NEEDS_PASSWORD_LINK_LABEL
#define IDS_SYNC_STATUS_NEEDS_KEYS_LINK_LABEL
#define IDS_SYNC_SERVER_IS_UNREACHABLE
#define IDS_SYNC_RELOGIN_ERROR
#define IDS_SYNC_RELOGIN_LINK_LABEL
#define IDS_SYNC_ADVANCED_OPTIONS
#define IDS_SYNC_FULL_ENCRYPTION_BODY_CUSTOM
#define IDS_SYNC_FULL_ENCRYPTION_BODY_CUSTOM_WITH_DATE
#define IDS_SYNC_FULL_ENCRYPTION_BODY_GOOGLE_WITH_DATE
#define IDS_SYNC_PROMO_NOT_SIGNED_IN_STATUS_HEADER
#define IDS_SYNC_PROMO_NOT_SIGNED_IN_STATUS_SUB_HEADER
#define IDS_SYNC_PROMO_NOT_SIGNED_IN_STATUS_LINK
#define IDS_TRANSLATE_BUBBLE_BEFORE_TRANSLATE_TITLE
#define IDS_TRANSLATE_BUBBLE_BEFORE_TRANSLATE_NEW
#define IDS_TRANSLATE_BUBBLE_ADVANCED_TITLE
#define IDS_TRANSLATE_BUBBLE_TRANSLATED_TITLE
#define IDS_TRANSLATE_BUBBLE_COULD_NOT_TRANSLATE_TITLE
#define IDS_TRANSLATE_BUBBLE_ADVANCED_LINK
#define IDS_TRANSLATE_BUBBLE_ADVANCED_BUTTON
#define IDS_TRANSLATE_BUBBLE_ADVANCED_MENU_BUTTON
#define IDS_TRANSLATE_BUBBLE_CHANGE_TARGET_LANGUAGE
#define IDS_TRANSLATE_BUBBLE_CHANGE_SOURCE_LANGUAGE
#define IDS_TRANSLATE_BUBBLE_ACCEPT
#define IDS_TRANSLATE_BUBBLE_DENY
#define IDS_TRANSLATE_BUBBLE_ALWAYS_TRANSLATE_LANG
#define IDS_TRANSLATE_BUBBLE_NEVER_TRANSLATE_LANG
#define IDS_TRANSLATE_BUBBLE_NEVER_TRANSLATE_SITE
#define IDS_TRANSLATE_BUBBLE_TRANSLATING
#define IDS_TRANSLATE_BUBBLE_TRANSLATED
#define IDS_TRANSLATE_BUBBLE_REVERT
#define IDS_TRANSLATE_BUBBLE_TRY_AGAIN
#define IDS_TRANSLATE_BUBBLE_ALWAYS
#define IDS_TRANSLATE_BUBBLE_ALWAYS_DO_THIS
#define IDS_TRANSLATE_BUBBLE_OPTIONS_MENU_BUTTON
#define IDS_TRANSLATE_BUBBLE_COULD_NOT_TRANSLATE
#define IDS_TRANSLATE_BUBBLE_PAGE_LANGUAGE
#define IDS_TRANSLATE_BUBBLE_TRANSLATION_LANGUAGE
#define IDS_TRANSLATE_BUBBLE_LANGUAGE_SETTINGS
#define IDS_TRANSLATE_BUBBLE_ADVANCED_TARGET
#define IDS_TRANSLATE_BUBBLE_ADVANCED_SOURCE
#define IDS_TRANSLATE_BUBBLE_UNKNOWN_LANGUAGE
#define IDS_TRANSLATE_BUBBLE_RESET
#define IDS_NOTIFICATIONS_INFOBAR_TEXT
#define IDS_NOTIFICATION_PERMISSIONS_FRAGMENT
#define IDS_NOTIFICATION_BUTTON_SETTINGS
#define IDS_NOTIFICATION_BUTTON_CLOSE
#define IDS_NOTIFICATION_BUTTON_MORE
#define IDS_NOTIFICATION_REPLY_PLACEHOLDER
#define IDS_GEOLOCATION_INFOBAR_TEXT
#define IDS_GEOLOCATION_INFOBAR_PERMISSION_FRAGMENT
#define IDS_GEOLOCATION_BUBBLE_SECTION_ALLOWED
#define IDS_GEOLOCATION_BUBBLE_SECTION_DENIED
#define IDS_GEOLOCATION_BUBBLE_REQUIRE_RELOAD_TO_CLEAR
#define IDS_GEOLOCATION_BUBBLE_CLEAR_LINK
#define IDS_GEOLOCATION_BUBBLE_MANAGE_LINK
#define IDS_GEOLOCATION_ALLOWED_TOOLTIP
#define IDS_GEOLOCATION_BLOCKED_TOOLTIP
#define IDS_MIDI_SYSEX_INFOBAR_TEXT
#define IDS_MIDI_SYSEX_PERMISSION_FRAGMENT
#define IDS_MIDI_SYSEX_ALLOWED_TOOLTIP
#define IDS_MIDI_SYSEX_BLOCKED_TOOLTIP
#define IDS_MIDI_SYSEX_BUBBLE_ALLOWED
#define IDS_MIDI_SYSEX_BUBBLE_DENIED
#define IDS_MIDI_SYSEX_BUBBLE_REQUIRE_RELOAD_TO_CLEAR
#define IDS_MIDI_SYSEX_BUBBLE_CLEAR_LINK
#define IDS_MIDI_SYSEX_BUBBLE_MANAGE_LINK
#define IDS_REGISTER_PROTOCOL_HANDLER_TOOLTIP
#define IDS_MEDIASTREAM_BUBBLE_MANAGE_LINK
#define IDS_MICROPHONE_CAMERA_ALLOWED
#define IDS_MICROPHONE_CAMERA_BLOCKED
#define IDS_MICROPHONE_ACCESSED
#define IDS_CAMERA_ACCESSED
#define IDS_MICROPHONE_BLOCKED
#define IDS_CAMERA_BLOCKED
#define IDS_MICROPHONE_CAMERA_ALLOWED_TITLE
#define IDS_MICROPHONE_CAMERA_BLOCKED_TITLE
#define IDS_MICROPHONE_ACCESSED_TITLE
#define IDS_CAMERA_ACCESSED_TITLE
#define IDS_MICROPHONE_BLOCKED_TITLE
#define IDS_CAMERA_BLOCKED_TITLE
#define IDS_MEDIASTREAM_SETTING_CHANGED_MESSAGE
#define IDS_MANAGE_PASSWORDS_CONFIRM_GENERATED_TEXT
#define IDS_PASSWORDS_WEB_LINK
#define IDS_MANAGE_PASSWORDS_LINK
#define IDS_MANAGE_PASSWORDS_TITLE
#define IDS_MANAGE_PASSWORDS_NO_PASSWORDS_TITLE
#define IDS_MANAGE_PASSWORDS_DIFFERENT_DOMAIN_TITLE
#define IDS_MANAGE_PASSWORDS_DIFFERENT_DOMAIN_NO_PASSWORDS_TITLE
#define IDS_MANAGE_PASSWORDS_DELETED
#define IDS_MANAGE_PASSWORDS_UNDO
#define IDS_MANAGE_PASSWORDS_UNDO_TOOLTIP
#define IDS_MANAGE_PASSWORDS_DELETE
#define IDS_MANAGE_PASSWORDS_SHOW_PASSWORD
#define IDS_MANAGE_PASSWORDS_HIDE_PASSWORD
#define IDS_MANAGE_PASSWORDS_AUTO_SIGNIN_TITLE_MD
#define IDS_AUTO_SIGNIN_FIRST_RUN_TITLE_MANY_DEVICES
#define IDS_AUTO_SIGNIN_FIRST_RUN_TITLE_LOCAL_DEVICE
#define IDS_AUTO_SIGNIN_FIRST_RUN_TEXT
#define IDS_AUTO_SIGNIN_FIRST_RUN_OK
#define IDS_FILE_SELECTION_DIALOG_INFOBAR
#define IDS_IMAGE_FILES
#define IDS_AUDIO_FILES
#define IDS_VIDEO_FILES
#define IDS_CUSTOM_FILES
#define IDS_FULLSCREEN_USER_ENTERED_FULLSCREEN
#define IDS_FULLSCREEN_EXTENSION_TRIGGERED_FULLSCREEN
#define IDS_FULLSCREEN_UNKNOWN_EXTENSION_TRIGGERED_FULLSCREEN
#define IDS_FULLSCREEN_SITE_ENTERED_FULLSCREEN
#define IDS_FULLSCREEN_ENTERED_FULLSCREEN
#define IDS_FULLSCREEN_SITE_ENTERED_FULLSCREEN_MOUSELOCK
#define IDS_FULLSCREEN_ENTERED_FULLSCREEN_MOUSELOCK
#define IDS_FULLSCREEN_SITE_ENTERED_MOUSELOCK
#define IDS_FULLSCREEN_ENTERED_MOUSELOCK
#define IDS_FULLSCREEN_PRESS_ESC_TO_EXIT_FULLSCREEN
#define IDS_FULLSCREEN_PRESS_ESC_TO_EXIT_MOUSELOCK
#define IDS_FULLSCREEN_HOLD_ESC_TO_EXIT_FULLSCREEN
#define IDS_REGISTER_PROTOCOL_HANDLER_MAILTO_NAME
#define IDS_REGISTER_PROTOCOL_HANDLER_WEBCAL_NAME
#define IDS_REGISTER_PROTOCOL_HANDLER_CONFIRM
#define IDS_REGISTER_PROTOCOL_HANDLER_CONFIRM_REPLACE
#define IDS_REGISTER_PROTOCOL_HANDLER_CONFIRM_FRAGMENT
#define IDS_REGISTER_PROTOCOL_HANDLER_CONFIRM_REPLACE_FRAGMENT
#define IDS_REGISTER_PROTOCOL_HANDLER_ACCEPT
#define IDS_REGISTER_PROTOCOL_HANDLER_DENY
#define IDS_REGISTER_PROTOCOL_HANDLER_IGNORE
#define IDS_MEDIA_CAPTURE_AUDIO_AND_VIDEO_INFOBAR_TEXT
#define IDS_MEDIA_CAPTURE_AUDIO_ONLY_INFOBAR_TEXT
#define IDS_MEDIA_CAPTURE_VIDEO_ONLY_INFOBAR_TEXT
#define IDS_MEDIA_CAPTURE_SCREEN_INFOBAR_TEXT
#define IDS_MEDIA_CAPTURE_AUDIO_ONLY_PERMISSION_FRAGMENT
#define IDS_MEDIA_CAPTURE_VIDEO_ONLY_PERMISSION_FRAGMENT
#define IDS_SENSORS_ALLOWED_TOOLTIP
#define IDS_MOTION_SENSORS_ALLOWED_TOOLTIP
#define IDS_SENSORS_BLOCKED_TOOLTIP
#define IDS_MOTION_SENSORS_BLOCKED_TOOLTIP
#define IDS_BLOCKED_SENSORS_UNBLOCK
#define IDS_BLOCKED_SENSORS_NO_ACTION
#define IDS_ALLOWED_SENSORS_TITLE
#define IDS_BLOCKED_SENSORS_TITLE
#define IDS_ALLOWED_SENSORS_MESSAGE
#define IDS_ALLOWED_MOTION_SENSORS_MESSAGE
#define IDS_BLOCKED_SENSORS_MESSAGE
#define IDS_BLOCKED_MOTION_SENSORS_MESSAGE
#define IDS_ALLOWED_SENSORS_NO_ACTION
#define IDS_ALLOWED_SENSORS_BLOCK
#define IDS_REQUEST_QUOTA_INFOBAR_TEXT
#define IDS_REQUEST_LARGE_QUOTA_INFOBAR_TEXT
#define IDS_REQUEST_QUOTA_PERMISSION_FRAGMENT
#define IDS_HIGH_CONTRAST_TITLE
#define IDS_HIGH_CONTRAST_HEADER
#define IDS_HIGH_CONTRAST_EXT
#define IDS_DARK_THEME
#define IDS_MEDIA_GALLERIES_DIALOG_HEADER
#define IDS_MEDIA_GALLERIES_DIALOG_SUBTEXT_READ_WRITE
#define IDS_MEDIA_GALLERIES_DIALOG_SUBTEXT_READ_DELETE
#define IDS_MEDIA_GALLERIES_DIALOG_SUBTEXT_READ_ONLY
#define IDS_MEDIA_GALLERIES_PERMISSION_SUGGESTIONS
#define IDS_MEDIA_GALLERIES_LAST_ATTACHED
#define IDS_MEDIA_GALLERIES_DIALOG_ADD_GALLERY
#define IDS_MEDIA_GALLERIES_DIALOG_CONFIRM
#define IDS_MEDIA_GALLERIES_DIALOG_ADD_GALLERY_TITLE
#define IDS_MEDIA_GALLERIES_DIALOG_DEVICE_ATTACHED
#define IDS_MEDIA_GALLERIES_DIALOG_DEVICE_NOT_ATTACHED
#define IDS_MEDIA_GALLERIES_DIALOG_DELETE
#define IDS_CHROME_SHORTCUT_DESCRIPTION
#define IDS_WEBSTORE_NAME_STORE
#define IDS_DESKTOP_MEDIA_PICKER_TITLE
#define IDS_DESKTOP_MEDIA_PICKER_TITLE_SCREEN_ONLY
#define IDS_DESKTOP_MEDIA_PICKER_TITLE_WINDOW_ONLY
#define IDS_DESKTOP_MEDIA_PICKER_TEXT
#define IDS_DESKTOP_MEDIA_PICKER_TEXT_DELEGATED
#define IDS_DESKTOP_MEDIA_PICKER_AUDIO_SHARE
#define IDS_DESKTOP_MEDIA_PICKER_SOURCE_TYPE_SCREEN
#define IDS_DESKTOP_MEDIA_PICKER_SOURCE_TYPE_WINDOW
#define IDS_DESKTOP_MEDIA_PICKER_SINGLE_SCREEN_NAME
#define IDS_DESKTOP_MEDIA_PICKER_MULTIPLE_SCREEN_NAME
#define IDS_LOCAL_DISCOVERY_REGISTER_CANCELED_ON_PRINTER
#define IDS_LOCAL_DISCOVERY_REGISTER_TIMEOUT_ON_PRINTER
#define IDS_CLOUD_PRINT_REGISTER_PRINTER_INFORMATION
#define IDS_TOOLTIP_TAB_ALERT_STATE_MEDIA_RECORDING
#define IDS_TOOLTIP_TAB_ALERT_STATE_TAB_CAPTURING
#define IDS_TOOLTIP_TAB_ALERT_STATE_AUDIO_PLAYING
#define IDS_TOOLTIP_TAB_ALERT_STATE_AUDIO_MUTING
#define IDS_TOOLTIP_TAB_ALERT_STATE_BLUETOOTH_CONNECTED
#define IDS_TOOLTIP_TAB_ALERT_STATE_USB_CONNECTED
#define IDS_TOOLTIP_TAB_ALERT_STATE_HID_CONNECTED
#define IDS_TOOLTIP_TAB_ALERT_STATE_SERIAL_CONNECTED
#define IDS_TOOLTIP_TAB_ALERT_STATE_PIP_PLAYING
#define IDS_TOOLTIP_TAB_ALERT_STATE_DESKTOP_CAPTURING
#define IDS_TOOLTIP_TAB_ALERT_STATE_VR_PRESENTING
#define IDS_TAB_AX_LABEL_MEDIA_RECORDING_FORMAT
#define IDS_TAB_AX_LABEL_TAB_CAPTURING_FORMAT
#define IDS_TAB_AX_LABEL_PIP_PLAYING_FORMAT
#define IDS_TAB_AX_LABEL_AUDIO_PLAYING_FORMAT
#define IDS_TAB_AX_LABEL_AUDIO_MUTING_FORMAT
#define IDS_TAB_AX_LABEL_BLUETOOTH_CONNECTED_FORMAT
#define IDS_TAB_AX_LABEL_USB_CONNECTED_FORMAT
#define IDS_TAB_AX_LABEL_HID_CONNECTED_FORMAT
#define IDS_TAB_AX_LABEL_SERIAL_CONNECTED_FORMAT
#define IDS_TAB_AX_LABEL_NETWORK_ERROR_FORMAT
#define IDS_TAB_AX_LABEL_CRASHED_FORMAT
#define IDS_TAB_AX_LABEL_DESKTOP_CAPTURING_FORMAT
#define IDS_TAB_AX_LABEL_VR_PRESENTING
#define IDS_PROFILE_IN_USE_LINUX_QUIT
#define IDS_PROFILE_IN_USE_LINUX_RELAUNCH
#define IDS_DESKTOP_MEDIA_PICKER_SHARE
#define IDS_PUSH_MESSAGING_GENERIC_NOTIFICATION_BODY
#define IDS_DEVICE_PERMISSIONS_DIALOG_SELECT
#define IDS_DEVICE_LOG_TITLE
#define IDS_DEVICE_AUTO_REFRESH
#define IDS_DEVICE_LOG_REFRESH
#define IDS_DEVICE_LOG_CLEAR
#define IDS_DEVICE_LOG_NO_ENTRIES
#define IDS_DEVICE_LOG_LEVEL_SHOW
#define IDS_DEVICE_LOG_LEVEL_ERROR
#define IDS_DEVICE_LOG_LEVEL_USER
#define IDS_DEVICE_LOG_LEVEL_EVENT
#define IDS_DEVICE_LOG_LEVEL_DEBUG
#define IDS_DEVICE_LOG_TYPE_LOGIN
#define IDS_DEVICE_LOG_TYPE_NETWORK
#define IDS_DEVICE_LOG_TYPE_POWER
#define IDS_DEVICE_LOG_TYPE_BLUETOOTH
#define IDS_DEVICE_LOG_TYPE_USB
#define IDS_DEVICE_LOG_TYPE_HID
#define IDS_DEVICE_LOG_TYPE_PRINTER
#define IDS_DEVICE_LOG_TYPE_FIDO
#define IDS_DEVICE_LOG_FILEINFO
#define IDS_DEVICE_LOG_TIME_DETAIL
#define IDS_DEVICE_LOG_ENTRY
#define IDS_WEBUSB_DEVICE_DETECTED_NOTIFICATION
#define IDS_WEBUSB_DEVICE_DETECTED_NOTIFICATION_TITLE
#define IDS_DEFAULT_AUDIO_DEVICE_NAME
#define IDS_COMMUNICATIONS_AUDIO_DEVICE_NAME
#define IDS_BLUETOOTH_DEVICE_CHOOSER_PROMPT_ORIGIN
#define IDS_BLUETOOTH_DEVICE_CHOOSER_PROMPT_EXTENSION_NAME
#define IDS_BLUETOOTH_DEVICE_CHOOSER_NO_DEVICES_FOUND_PROMPT
#define IDS_BLUETOOTH_DEVICE_CHOOSER_TURN_ADAPTER_OFF
#define IDS_BLUETOOTH_DEVICE_CHOOSER_TURN_ON_BLUETOOTH_LINK_TEXT
#define IDS_BLUETOOTH_DEVICE_CHOOSER_SCANNING
#define IDS_BLUETOOTH_DEVICE_CHOOSER_RE_SCAN
#define IDS_BLUETOOTH_DEVICE_CHOOSER_RE_SCAN_TOOLTIP
#define IDS_BLUETOOTH_DEVICE_CHOOSER_SCANNING_LABEL
#define IDS_BLUETOOTH_DEVICE_CHOOSER_SCANNING_LABEL_TOOLTIP
#define IDS_BLUETOOTH_DEVICE_CHOOSER_PAIR_BUTTON_TEXT
#define IDS_DEVICE_CHOOSER_GET_HELP_LINK_WITH_SCANNING_STATUS
#define IDS_DEVICE_CHOOSER_GET_HELP_LINK_WITH_RE_SCAN_LINK
#define IDS_DEVICE_CHOOSER_PAIRED_STATUS_TEXT
#define IDS_DEVICE_CHOOSER_DEVICE_NAME_AND_PAIRED_STATUS_TEXT
#define IDS_USB_DEVICE_CHOOSER_PROMPT_ORIGIN
#define IDS_USB_DEVICE_CHOOSER_PROMPT_EXTENSION_NAME
#define IDS_DEVICE_CHOOSER_DEVICE_NAME_WITH_ID
#define IDS_DEVICE_CHOOSER_NO_DEVICES_FOUND_PROMPT
#define IDS_USB_DEVICE_CHOOSER_CONNECT_BUTTON_TEXT
#define IDS_DEVICE_CHOOSER_CANCEL_BUTTON_TEXT
#define IDS_DEVICE_CHOOSER_DEVICE_NAME_UNKNOWN_DEVICE_WITH_VENDOR_NAME
#define IDS_DEVICE_CHOOSER_DEVICE_NAME_UNKNOWN_DEVICE_WITH_VENDOR_ID_AND_PRODUCT_ID
#define IDS_BLUETOOTH_SCANNING_PROMPT_NO_DEVICES_FOUND_PROMPT
#define IDS_BLUETOOTH_SCANNING_PROMPT_ORIGIN
#define IDS_BLUETOOTH_SCANNING_PROMPT_ALLOW_BUTTON_TEXT
#define IDS_BLUETOOTH_SCANNING_PROMPT_BLOCK_BUTTON_TEXT
#define IDS_BLUETOOTH_SCANNING_DEVICE_UNKNOWN
#define IDS_DEVICE_DESCRIPTION_FOR_PRODUCT_ID_AND_VENDOR_NAME
#define IDS_DEVICE_DESCRIPTION_FOR_PRODUCT_ID_AND_VENDOR_ID
#define IDS_DEVICE_DESCRIPTION_FOR_VENDOR_ID
#define IDS_DEVICE_DESCRIPTION_FOR_VENDOR_NAME
#define IDS_DEVICE_DESCRIPTION_FOR_ANY_VENDOR
#define IDS_SERIAL_PORT_CHOOSER_PROMPT_ORIGIN
#define IDS_SERIAL_PORT_CHOOSER_PROMPT_EXTENSION_NAME
#define IDS_SERIAL_PORT_CHOOSER_NAME_WITH_PATH
#define IDS_SERIAL_PORT_CHOOSER_PATH_ONLY
#define IDS_SERIAL_PORT_CHOOSER_CONNECT_BUTTON_TEXT
#define IDS_HID_CHOOSER_PROMPT_ORIGIN
#define IDS_HID_CHOOSER_PROMPT_EXTENSION_NAME
#define IDS_HID_CHOOSER_ITEM_WITHOUT_NAME
#define IDS_HID_CHOOSER_ITEM_WITH_NAME
#define IDS_IME_API_ACTIVATED_WARNING
#define IDS_IME_API_NEVER_SHOW
#define IDS_ALWAYS_ALLOW_ADS
#define IDS_BLOCKED_ADS_INFOBAR_MESSAGE
#define IDS_BLOCKED_ADS_PROMPT_TITLE
#define IDS_BLOCKED_ADS_PROMPT_EXPLANATION
#define IDS_BLOCKED_ADS_PROMPT_TOOLTIP
#define IDS_HEAVY_AD_INTERVENTION_BUTTON_DETAILS
#define IDS_HEAVY_AD_INTERVENTION_HEADING
#define IDS_HEAVY_AD_INTERVENTION_SUMMARY
#define IDS_UTILITY_PROCESS_UTILITY_WIN_NAME
#define IDS_UTILITY_PROCESS_QUARANTINE_SERVICE_NAME
#define IDS_REDIRECT_BLOCKED_MESSAGE
#define IDS_REDIRECT_BLOCKED_TITLE
#define IDS_REDIRECT_BLOCKED_TOOLTIP
#define IDS_WIN10_TOAST_BROWSE_FAST
#define IDS_WIN10_TOAST_BROWSE_SAFELY
#define IDS_WIN10_TOAST_BROWSE_SMART
#define IDS_WIN10_TOAST_SWITCH_FAST
#define IDS_WIN10_TOAST_SWITCH_SMART
#define IDS_WIN10_TOAST_SWITCH_SECURE
#define IDS_WIN10_TOAST_SWITCH_SMART_AND_SECURE
#define IDS_WIN10_TOAST_RECOMMENDATION
#define IDS_WIN10_TOAST_OPEN_CHROME
#define IDS_WIN10_TOAST_NO_THANKS
#define IDS_NTP_DOWNLOAD_SUGGESTIONS_SECTION_HEADER
#define IDS_NTP_DOWNLOADS_SUGGESTIONS_SECTION_EMPTY
#define IDS_CONTROLLED_BY_AUTOMATION
#define IDS_SECURITY_KEY_ATTESTATION_PERMISSION_FRAGMENT
#define IDS_VIDEO_CALL_NOTIFICATION_TEXT_2
#define IDS_AUDIO_CALL_NOTIFICATION_TEXT_2
#define IDS_VIDEO_AUDIO_CALL_NOTIFICATION_TEXT_2
#define IDS_VIDEO_CALL_INCOGNITO_NOTIFICATION_TEXT_2
#define IDS_AUDIO_CALL_INCOGNITO_NOTIFICATION_TEXT_2
#define IDS_VIDEO_AUDIO_CALL_INCOGNITO_NOTIFICATION_TEXT_2
#define IDS_DOWNLOAD_OPEN_CONFIRMATION_DIALOG_TITLE
#define IDS_DOWNLOAD_OPEN_CONFIRMATION_DIALOG_MESSAGE
#define IDS_CONFIRM_FILE_UPLOAD_TITLE
#define IDS_CONFIRM_FILE_UPLOAD_TEXT
#define IDS_CONFIRM_FILE_UPLOAD_OK_BUTTON
#define IDS_NATIVE_FILE_SYSTEM_WRITE_PERMISSION_TITLE
#define IDS_NATIVE_FILE_SYSTEM_WRITE_PERMISSION_FILE_TEXT
#define IDS_NATIVE_FILE_SYSTEM_WRITE_PERMISSION_DIRECTORY_TEXT
#define IDS_NATIVE_FILE_SYSTEM_WRITE_PERMISSION_ALLOW_TEXT
#define IDS_NATIVE_FILE_SYSTEM_WRITE_USAGE_TOOLTIP
#define IDS_NATIVE_FILE_SYSTEM_DIRECTORY_USAGE_TOOLTIP
#define IDS_NATIVE_FILE_SYSTEM_USAGE_BUBBLE_SINGLE_WRITABLE_FILE_TEXT
#define IDS_NATIVE_FILE_SYSTEM_USAGE_BUBBLE_WRITABLE_FILES_TEXT
#define IDS_NATIVE_FILE_SYSTEM_USAGE_BUBBLE_SINGLE_WRITABLE_DIRECTORY_TEXT
#define IDS_NATIVE_FILE_SYSTEM_USAGE_BUBBLE_WRITABLE_DIRECTORIES_TEXT
#define IDS_NATIVE_FILE_SYSTEM_USAGE_BUBBLE_WRITABLE_FILES_AND_DIRECTORIES_TEXT
#define IDS_NATIVE_FILE_SYSTEM_USAGE_BUBBLE_SINGLE_READABLE_DIRECTORY_TEXT
#define IDS_NATIVE_FILE_SYSTEM_USAGE_BUBBLE_READABLE_DIRECTORIES_TEXT
#define IDS_NATIVE_FILE_SYSTEM_USAGE_BUBBLE_READ_AND_WRITE
#define IDS_NATIVE_FILE_SYSTEM_USAGE_BUBBLE_SAVE_CHANGES
#define IDS_NATIVE_FILE_SYSTEM_USAGE_BUBBLE_VIEW_CHANGES
#define IDS_NATIVE_FILE_SYSTEM_USAGE_BUBBLE_FILES_TEXT
#define IDS_NATIVE_FILE_SYSTEM_USAGE_EXPAND
#define IDS_NATIVE_FILE_SYSTEM_USAGE_COLLAPSE
#define IDS_NATIVE_FILE_SYSTEM_USAGE_REMOVE_ACCESS
#define IDS_NATIVE_FILE_SYSTEM_RESTRICTED_DIRECTORY_TITLE
#define IDS_NATIVE_FILE_SYSTEM_RESTRICTED_DIRECTORY_TEXT
#define IDS_NATIVE_FILE_SYSTEM_RESTRICTED_DIRECTORY_BUTTON
#define IDS_NATIVE_FILE_SYSTEM_RESTRICTED_FILE_TITLE
#define IDS_NATIVE_FILE_SYSTEM_RESTRICTED_FILE_TEXT
#define IDS_NATIVE_FILE_SYSTEM_RESTRICTED_FILE_BUTTON
#define IDS_NATIVE_FILE_SYSTEM_DIRECTORY_ACCESS_CONFIRMATION_TITLE
#define IDS_NATIVE_FILE_SYSTEM_DIRECTORY_ACCESS_CONFIRMATION_TEXT
#define IDS_NATIVE_FILE_SYSTEM_DIRECTORY_ACCESS_ALLOW_BUTTON
#define IDS_RELAUNCH_ACCEPT_BUTTON
#define IDS_RELAUNCH_REQUIRED_CANCEL_BUTTON
#define IDS_WEBAUTHN_GENERIC_TITLE
#define IDS_WEBAUTHN_WELCOME_SCREEN_TITLE
#define IDS_WEBAUTHN_WELCOME_SCREEN_DESCRIPTION
#define IDS_WEBAUTHN_WELCOME_SCREEN_NEXT
#define IDS_WEBAUTHN_TRANSPORT_SELECTION_TITLE
#define IDS_WEBAUTHN_TRANSPORT_SELECTION_DESCRIPTION
#define IDS_WEBAUTHN_TRANSPORT_BLE
#define IDS_WEBAUTHN_TRANSPORT_USB
#define IDS_WEBAUTHN_TRANSPORT_NFC
#define IDS_WEBAUTHN_TRANSPORT_INTERNAL
#define IDS_WEBAUTHN_TRANSPORT_CABLE
#define IDS_WEBAUTHN_TRANSPORT_POPUP_DIFFERENT_AUTHENTICATOR_WIN
#define IDS_WEBAUTHN_USB_ACTIVATE_DESCRIPTION
#define IDS_WEBAUTHN_ERROR_GENERIC_TITLE
#define IDS_WEBAUTHN_ERROR_WRONG_KEY_TITLE
#define IDS_WEBAUTHN_ERROR_WRONG_KEY_REGISTER_DESCRIPTION
#define IDS_WEBAUTHN_ERROR_WRONG_KEY_SIGN_DESCRIPTION
#define IDS_WEBAUTHN_ERROR_TIMEOUT_DESCRIPTION
#define IDS_WEBAUTHN_ERROR_INTERNAL_UNRECOGNIZED_TITLE
#define IDS_WEBAUTHN_ERROR_INTERNAL_UNRECOGNIZED_DESCRIPTION
#define IDS_WEBAUTHN_ERROR_NO_TRANSPORTS_TITLE
#define IDS_WEBAUTHN_ERROR_NO_TRANSPORTS_DESCRIPTION
#define IDS_WEBAUTHN_BLUETOOTH_POWER_ON_AUTO_TITLE
#define IDS_WEBAUTHN_BLUETOOTH_POWER_ON_AUTO_DESCRIPTION
#define IDS_WEBAUTHN_BLUETOOTH_POWER_ON_AUTO_NEXT
#define IDS_WEBAUTHN_BLUETOOTH_POWER_ON_MANUAL_TITLE
#define IDS_WEBAUTHN_BLUETOOTH_POWER_ON_MANUAL_DESCRIPTION
#define IDS_WEBAUTHN_BLUETOOTH_POWER_ON_MANUAL_NEXT
#define IDS_WEBAUTHN_BLE_PAIRING_BEGIN_TITLE
#define IDS_WEBAUTHN_BLE_PAIRING_BEGIN_DESCRIPTION
#define IDS_WEBAUTHN_BLE_PAIRING_BEGIN_NEXT
#define IDS_WEBAUTHN_BLE_ENTER_PAIRING_MODE_TITLE
#define IDS_WEBAUTHN_BLE_ENTER_PAIRING_MODE_DESCRIPTION
#define IDS_WEBAUTHN_BLE_DEVICE_SELECTION_TITLE
#define IDS_WEBAUTHN_BLE_DEVICE_SELECTION_DESCRIPTION
#define IDS_WEBAUTHN_BLE_DEVICE_SELECTION_SEARCHING_LABEL
#define IDS_WEBAUTHN_BLE_DEVICE_SELECTION_REMINDER_LABEL
#define IDS_WEBAUTHN_BLE_PIN_ENTRY_TITLE
#define IDS_WEBAUTHN_BLE_PIN_ENTRY_DESCRIPTION
#define IDS_WEBAUTHN_BLE_PIN_ENTRY_PIN_LABEL
#define IDS_WEBAUTHN_BLE_PIN_ENTRY_NEXT
#define IDS_WEBAUTHN_BLE_VERIFYING_TITLE
#define IDS_WEBAUTHN_BLE_ACTIVATE_DESCRIPTION
#define IDS_WEBAUTHN_TRANSPORT_POPUP_LABEL
#define IDS_WEBAUTHN_TRANSPORT_POPUP_USB
#define IDS_WEBAUTHN_TRANSPORT_POPUP_BLE
#define IDS_WEBAUTHN_TRANSPORT_POPUP_PAIR_PHONE
#define IDS_WEBAUTHN_TRANSPORT_POPUP_ANOTHER_BLE
#define IDS_WEBAUTHN_TRANSPORT_POPUP_NFC
#define IDS_WEBAUTHN_TRANSPORT_POPUP_INTERNAL
#define IDS_WEBAUTHN_TRANSPORT_POPUP_CABLE
#define IDS_WEBAUTHN_CABLE_ACTIVATE_TITLE
#define IDS_WEBAUTHN_CABLE_ACTIVATE_DESCRIPTION
#define IDS_WEBAUTHN_CABLE_QR_TITLE
#define IDS_WEBAUTHN_CABLE_QR_DESCRIPTION
#define IDS_WEBAUTHN_PIN_ENTRY_TITLE
#define IDS_WEBAUTHN_PIN_ENTRY_DESCRIPTION
#define IDS_WEBAUTHN_PIN_ENTRY_PIN_LABEL
#define IDS_WEBAUTHN_PIN_ENTRY_NEXT
#define IDS_WEBAUTHN_PIN_SETUP_DESCRIPTION
#define IDS_WEBAUTHN_PIN_SETUP_CONFIRMATION_LABEL
#define IDS_WEBAUTHN_PIN_ENTRY_ERROR_INVALID_CHARACTERS
#define IDS_WEBAUTHN_PIN_ENTRY_ERROR_TOO_SHORT
#define IDS_WEBAUTHN_PIN_ENTRY_ERROR_FAILED_RETRIES
#define IDS_WEBAUTHN_PIN_ENTRY_ERROR_FAILED
#define IDS_WEBAUTHN_PIN_SETUP_ERROR_FAILED
#define IDS_WEBAUTHN_PIN_TAP_AGAIN_DESCRIPTION
#define IDS_WEBAUTHN_PIN_ENTRY_ERROR_MISMATCH
#define IDS_WEBAUTHN_CLIENT_PIN_SOFT_BLOCK_DESCRIPTION
#define IDS_WEBAUTHN_CLIENT_PIN_HARD_BLOCK_DESCRIPTION
#define IDS_WEBAUTHN_CLIENT_PIN_AUTHENTICATOR_REMOVED_DESCRIPTION
#define IDS_WEBAUTHN_ACCOUNT_COLUMN
#define IDS_WEBAUTHN_NAME_COLUMN
#define IDS_WEBAUTHN_SELECT_ACCOUNT
#define IDS_WEBAUTHN_UNKNOWN_ACCOUNT
#define IDS_WEBAUTHN_RESIDENT_KEY_PRIVACY
#define IDS_WEBAUTHN_ERROR_MISSING_CAPABILITY_TITLE
#define IDS_WEBAUTHN_ERROR_MISSING_CAPABILITY_DESC
#define IDS_WEBAUTHN_STORAGE_FULL_DESC
#define IDS_WEBAUTHN_REQUEST_ATTESTATION_PERMISSION_TITLE
#define IDS_WEBAUTHN_REQUEST_ATTESTATION_PERMISSION_DESC
#define IDS_WEBAUTHN_ALLOW_ATTESTATION
#define IDS_WEBAUTHN_RETRY
#define IDS_INCOGNITO_PROFILE_MENU_TITLE
#define IDS_INCOGNITO_WINDOW_COUNT_MESSAGE
#define IDS_INCOGNITO_PROFILE_MENU_CLOSE_BUTTON
#define IDS_HATS_BUBBLE_OK_LABEL
#define IDS_HATS_BUBBLE_TEXT
#define IDS_NOTIFICATION_DEFAULT_HELPFUL_BUTTON_TEXT
#define IDS_NOTIFICATION_DEFAULT_UNHELPFUL_BUTTON_TEXT
#define IDS_DEEP_SCANNING_DIALOG_TITLE
#define IDS_DEEP_SCANNING_DIALOG_MESSAGE
#define IDS_DEEP_SCANNING_DIALOG_OPEN_NOW_TITLE
#define IDS_DEEP_SCANNING_DIALOG_OPEN_NOW_MESSAGE
#define IDS_DEEP_SCANNING_DIALOG_OPEN_NOW_ACCEPT_BUTTON
#define IDS_DEEP_SCANNING_INFO_DIALOG_TITLE
#define IDS_DEEP_SCANNING_INFO_DIALOG_MESSAGE
#define IDS_DEEP_SCANNING_INFO_DIALOG_ACCEPT_BUTTON
#define IDS_DEEP_SCANNING_INFO_DIALOG_CANCEL_BUTTON
#define IDS_DEEP_SCANNING_INFO_DIALOG_OPEN_NOW_BUTTON
#define IDS_DEEP_SCANNING_TIMED_OUT_DIALOG_TITLE
#define IDS_DEEP_SCANNING_TIMED_OUT_DIALOG_MESSAGE
#define IDS_DEEP_SCANNING_TIMED_OUT_DIALOG_ACCEPT_BUTTON
#define IDS_DEEP_SCANNING_TIMED_OUT_DIALOG_CANCEL_BUTTON
#define IDS_DEEP_SCANNING_TIMED_OUT_DIALOG_OPEN_NOW_BUTTON
#define IDS_SMS_INFOBAR_TITLE
#define IDS_SMS_INFOBAR_STATUS_SMS_RECEIVED
#define IDS_SMS_INFOBAR_BUTTON_OK
#define IDS_APP_PAUSE_PROMPT_TITLE
#define IDS_APP_PAUSE_HEADING
#define IDS_SPELLCHECK_DICTIONARY
#define IDS_EXTENSION_WIPEOUT_BUBBLE_WIDTH_CHARS
#define IDS_EXTENSION_TOOLBAR_REDESIGN_NOTIFICATION_BUBBLE_WIDTH_CHARS
#define IDS_EDITBOOKMARK_DIALOG_WIDTH_CHARS
#define IDS_EDITBOOKMARK_DIALOG_HEIGHT_LINES
#define IDS_DOWNLOAD_BIG_PROGRESS_SIZE
#define IDS_THEMES_GALLERY_URL
#define IDS_WEBSTORE_URL
#define IDS_FLASH_STORAGE_URL
#define IDS_FLASH_GLOBAL_PRIVACY_URL
#define IDS_FLASH_WEBSITE_PRIVACY_URL
#define IDS_SYNC_UNRECOVERABLE_ERROR_HELP_URL
#define IDS_CREATE_SHORTCUTS_DIALOG_WIDTH_CHARS
#define IDS_METRO_FLOW_WIDTH_CHARS
#define IDS_METRO_FLOW_HEIGHT_LINES
#define IDS_MEDIA_GALLERIES_DIALOG_CONTENT_WIDTH_CHARS
#define IDS_SETTINGS_CLEAR_DATA_MYACTIVITY_URL_IN_DIALOG
#define IDS_SETTINGS_CLEAR_DATA_MYACTIVITY_URL_IN_HISTORY
#define IDS_STANDARD_FONT_FAMILY
#define IDS_FIXED_FONT_FAMILY
#define IDS_FIXED_FONT_FAMILY_ALT_WIN
#define IDS_SERIF_FONT_FAMILY
#define IDS_SANS_SERIF_FONT_FAMILY
#define IDS_NTP_FONT_FAMILY
#define IDS_CURSIVE_FONT_FAMILY
#define IDS_FANTASY_FONT_FAMILY
#define IDS_PICTOGRAPH_FONT_FAMILY
#define IDS_STANDARD_FONT_FAMILY_CYRILLIC
#define IDS_FIXED_FONT_FAMILY_ARABIC
#define IDS_FIXED_FONT_FAMILY_CYRILLIC
#define IDS_SANS_SERIF_FONT_FAMILY_ARABIC
#define IDS_SERIF_FONT_FAMILY_CYRILLIC
#define IDS_SANS_SERIF_FONT_FAMILY_CYRILLIC
#define IDS_STANDARD_FONT_FAMILY_GREEK
#define IDS_FIXED_FONT_FAMILY_GREEK
#define IDS_SERIF_FONT_FAMILY_GREEK
#define IDS_SANS_SERIF_FONT_FAMILY_GREEK
#define IDS_STANDARD_FONT_FAMILY_JAPANESE
#define IDS_FIXED_FONT_FAMILY_JAPANESE
#define IDS_SERIF_FONT_FAMILY_JAPANESE
#define IDS_SANS_SERIF_FONT_FAMILY_JAPANESE
#define IDS_STANDARD_FONT_FAMILY_KOREAN
#define IDS_FIXED_FONT_FAMILY_KOREAN
#define IDS_SERIF_FONT_FAMILY_KOREAN
#define IDS_SANS_SERIF_FONT_FAMILY_KOREAN
#define IDS_CURSIVE_FONT_FAMILY_KOREAN
#define IDS_STANDARD_FONT_FAMILY_SIMPLIFIED_HAN
#define IDS_FIXED_FONT_FAMILY_SIMPLIFIED_HAN
#define IDS_SERIF_FONT_FAMILY_SIMPLIFIED_HAN
#define IDS_SANS_SERIF_FONT_FAMILY_SIMPLIFIED_HAN
#define IDS_CURSIVE_FONT_FAMILY_SIMPLIFIED_HAN
#define IDS_STANDARD_FONT_FAMILY_TRADITIONAL_HAN
#define IDS_FIXED_FONT_FAMILY_TRADITIONAL_HAN
#define IDS_SERIF_FONT_FAMILY_TRADITIONAL_HAN
#define IDS_SANS_SERIF_FONT_FAMILY_TRADITIONAL_HAN
#define IDS_CURSIVE_FONT_FAMILY_TRADITIONAL_HAN
#define IDS_MINIMUM_FONT_SIZE
#define IDS_MINIMUM_LOGICAL_FONT_SIZE
#define IDS_PROXY_RESOLVER_DISPLAY_NAME
#define IDS_TIME_SECS
#define IDS_TIME_LONG_SECS
#define IDS_TIME_LONG_SECS_2ND
#define IDS_TIME_MINS
#define IDS_TIME_LONG_MINS
#define IDS_TIME_LONG_MINS_1ST
#define IDS_TIME_LONG_MINS_2ND
#define IDS_TIME_HOURS
#define IDS_TIME_HOURS_1ST
#define IDS_TIME_HOURS_2ND
#define IDS_TIME_DAYS
#define IDS_TIME_DAYS_1ST
#define IDS_TIME_MONTHS
#define IDS_TIME_YEARS
#define IDS_TIME_REMAINING_SECS
#define IDS_TIME_REMAINING_LONG_SECS
#define IDS_TIME_REMAINING_MINS
#define IDS_TIME_REMAINING_LONG_MINS
#define IDS_TIME_REMAINING_HOURS
#define IDS_TIME_REMAINING_DAYS
#define IDS_TIME_REMAINING_MONTHS
#define IDS_TIME_REMAINING_YEARS
#define IDS_TIME_ELAPSED_SECS
#define IDS_TIME_ELAPSED_LONG_SECS
#define IDS_TIME_ELAPSED_MINS
#define IDS_TIME_ELAPSED_LONG_MINS
#define IDS_TIME_ELAPSED_HOURS
#define IDS_TIME_ELAPSED_DAYS
#define IDS_TIME_ELAPSED_MONTHS
#define IDS_TIME_ELAPSED_YEARS
#define IDS_PAST_TIME_TODAY
#define IDS_PAST_TIME_YESTERDAY
#define IDS_APP_MENU_EMPTY_SUBMENU
#define IDS_APP_UNTITLED_SHORTCUT_FILE_NAME
#define IDS_APP_SAVEAS_ALL_FILES
#define IDS_APP_SAVEAS_EXTENSION_FORMAT
#define IDS_SELECT_UPLOAD_FOLDER_DIALOG_TITLE
#define IDS_CONTENT_CONTEXT_WRITING_DIRECTION_MENU
#define IDS_CONTENT_CONTEXT_WRITING_DIRECTION_DEFAULT
#define IDS_CONTENT_CONTEXT_WRITING_DIRECTION_LTR
#define IDS_CONTENT_CONTEXT_WRITING_DIRECTION_RTL
#define IDS_SELECT_FOLDER_DIALOG_TITLE
#define IDS_SAVE_AS_DIALOG_TITLE
#define IDS_OPEN_FILE_DIALOG_TITLE
#define IDS_OPEN_FILES_DIALOG_TITLE
#define IDS_SAVEAS_ALL_FILES
#define IDS_SELECT_UPLOAD_FOLDER_DIALOG_UPLOAD_BUTTON
#define IDS_AX_ACTIVATE_ACTION_VERB
#define IDS_AX_CHECK_ACTION_VERB
#define IDS_AX_CLICK_ACTION_VERB
#define IDS_AX_CLICK_ANCESTOR_ACTION_VERB
#define IDS_AX_JUMP_ACTION_VERB
#define IDS_AX_OPEN_ACTION_VERB
#define IDS_AX_PRESS_ACTION_VERB
#define IDS_AX_SELECT_ACTION_VERB
#define IDS_AX_UNCHECK_ACTION_VERB
#define IDS_APP_ACCNAME_BACK
#define IDS_APP_ACCNAME_CLOSE
#define IDS_APP_ACCNAME_MINIMIZE
#define IDS_APP_ACCNAME_MAXIMIZE
#define IDS_APP_ACCNAME_RESTORE
#define IDS_APP_ACCNAME_MENU
#define IDS_APP_ACCNAME_COLOR_CHOOSER_HEX_INPUT
#define IDS_APP_SCROLLBAR_CXMENU_SCROLLHERE
#define IDS_APP_SCROLLBAR_CXMENU_SCROLLLEFTEDGE
#define IDS_APP_SCROLLBAR_CXMENU_SCROLLRIGHTEDGE
#define IDS_APP_SCROLLBAR_CXMENU_SCROLLHOME
#define IDS_APP_SCROLLBAR_CXMENU_SCROLLEND
#define IDS_APP_SCROLLBAR_CXMENU_SCROLLPAGEUP
#define IDS_APP_SCROLLBAR_CXMENU_SCROLLPAGEDOWN
#define IDS_APP_SCROLLBAR_CXMENU_SCROLLLEFT
#define IDS_APP_SCROLLBAR_CXMENU_SCROLLRIGHT
#define IDS_APP_SCROLLBAR_CXMENU_SCROLLUP
#define IDS_APP_SCROLLBAR_CXMENU_SCROLLDOWN
#define IDS_APP_UNDO
#define IDS_APP_CUT
#define IDS_APP_COPY
#define IDS_APP_PASTE
#define IDS_APP_DELETE
#define IDS_APP_SELECT_ALL
#define IDS_CONTENT_CONTEXT_EMOJI
#define IDS_APP_OK
#define IDS_APP_CANCEL
#define IDS_APP_CLOSE
#define IDS_APP_ESC_KEY
#define IDS_APP_TAB_KEY
#define IDS_APP_INSERT_KEY
#define IDS_APP_HOME_KEY
#define IDS_APP_DELETE_KEY
#define IDS_APP_END_KEY
#define IDS_APP_PAGEUP_KEY
#define IDS_APP_PAGEDOWN_KEY
#define IDS_APP_LEFT_ARROW_KEY
#define IDS_APP_RIGHT_ARROW_KEY
#define IDS_APP_UP_ARROW_KEY
#define IDS_APP_DOWN_ARROW_KEY
#define IDS_APP_ENTER_KEY
#define IDS_APP_SPACE_KEY
#define IDS_APP_F1_KEY
#define IDS_APP_F11_KEY
#define IDS_APP_BACKSPACE_KEY
#define IDS_APP_COMMA_KEY
#define IDS_APP_PERIOD_KEY
#define IDS_APP_MEDIA_NEXT_TRACK_KEY
#define IDS_APP_MEDIA_PLAY_PAUSE_KEY
#define IDS_APP_MEDIA_PREV_TRACK_KEY
#define IDS_APP_MEDIA_STOP_KEY
#define IDS_APP_ALT_KEY
#define IDS_APP_COMMAND_KEY
#define IDS_APP_CTRL_KEY
#define IDS_APP_SEARCH_KEY
#define IDS_APP_SHIFT_KEY
#define IDS_APP_WINDOWS_KEY
#define IDS_APP_ACCELERATOR_WITH_MODIFIER
#define IDS_APP_BYTES
#define IDS_APP_KIBIBYTES
#define IDS_APP_MEBIBYTES
#define IDS_APP_GIBIBYTES
#define IDS_APP_TEBIBYTES
#define IDS_APP_PEBIBYTES
#define IDS_APP_BYTES_PER_SECOND
#define IDS_APP_KIBIBYTES_PER_SECOND
#define IDS_APP_MEBIBYTES_PER_SECOND
#define IDS_APP_GIBIBYTES_PER_SECOND
#define IDS_APP_TEBIBYTES_PER_SECOND
#define IDS_APP_PEBIBYTES_PER_SECOND
#define IDS_MESSAGE_CENTER_ACCESSIBLE_NAME
#define IDS_MESSAGE_CENTER_NOTIFICATION_ACCESSIBLE_NAME
#define IDS_MESSAGE_CENTER_NOTIFICATION_ACCESSIBLE_NAME_PLURAL
#define IDS_MESSAGE_CENTER_EXPAND_NOTIFICATION
#define IDS_MESSAGE_CENTER_COLLAPSE_NOTIFICATION
#define IDS_MESSAGE_CENTER_LIST_NOTIFICATION_MESSAGE_WITH_DIVIDER
#define IDS_MESSAGE_CENTER_LIST_NOTIFICATION_LG_HEADER_OVERFLOW_INDICATOR
#define IDS_MESSAGE_CENTER_NOTIFICATION_PROGRESS_PERCENTAGE
#define IDS_MESSAGE_CENTER_NOTIFICATION_CHROMEOS_SYSTEM
#define IDS_MESSAGE_CENTER_NOTIFICATION_INLINE_REPLY_PLACEHOLDER
#define IDS_MESSAGE_NOTIFICATION_NOW_STRING_SHORTEST
#define IDS_MESSAGE_NOTIFICATION_DURATION_MINUTES_SHORTEST
#define IDS_MESSAGE_NOTIFICATION_DURATION_HOURS_SHORTEST
#define IDS_MESSAGE_NOTIFICATION_DURATION_DAYS_SHORTEST
#define IDS_MESSAGE_NOTIFICATION_DURATION_YEARS_SHORTEST
#define IDS_MESSAGE_NOTIFICATION_DURATION_MINUTES_SHORTEST_FUTURE
#define IDS_MESSAGE_NOTIFICATION_DURATION_HOURS_SHORTEST_FUTURE
#define IDS_MESSAGE_NOTIFICATION_DURATION_DAYS_SHORTEST_FUTURE
#define IDS_MESSAGE_NOTIFICATION_DURATION_YEARS_SHORTEST_FUTURE
#define IDS_MESSAGE_CENTER_BLOCK_ALL_NOTIFICATIONS_SITE
#define IDS_MESSAGE_CENTER_BLOCK_ALL_NOTIFICATIONS_APP
#define IDS_MESSAGE_CENTER_BLOCK_ALL_NOTIFICATIONS
#define IDS_MESSAGE_CENTER_DONT_BLOCK_NOTIFICATIONS
#define IDS_MESSAGE_CENTER_SETTINGS_DONE
#define IDS_MESSAGE_CENTER_CLOSE_NOTIFICATION_BUTTON_ACCESSIBLE_NAME
#define IDS_MESSAGE_CENTER_CLOSE_NOTIFICATION_BUTTON_TOOLTIP
#define IDS_MESSAGE_CENTER_NOTIFICATION_SNOOZE_BUTTON_TOOLTIP
#define IDS_MESSAGE_NOTIFICATION_SETTINGS_BUTTON_ACCESSIBLE_NAME
#define IDS_MESSAGE_NOTIFICATION_ACCESSIBLE_NAME
#define IDS_MESSAGE_NOTIFICATION_SEND_TAB_TO_SELF_DEVICE_INFO
#define IDS_MESSAGE_NOTIFICATION_SEND_TAB_TO_SELF_CONFIRMATION_SUCCESS
#define IDS_MESSAGE_NOTIFICATION_SEND_TAB_TO_SELF_CONFIRMATION_FAILURE_TITLE
#define IDS_MESSAGE_NOTIFICATION_SEND_TAB_TO_SELF_CONFIRMATION_FAILURE_MESSAGE
#define IDS_SUGGESTED_APPS_INDICATOR
#define IDS_FREQUENTLY_USED_INDICATOR
#define IDS_RECOMMENDED_APPS_INDICATOR
#define IDS_MOST_LIKELY_INDICATOR
#define IDS_APP_SUGGESTIONS_INDICATOR
#define IDS_ALL_APPS_INDICATOR
#define IDS_APP_LIST_APP_DRAG_LOCATION_ACCESSIBILE_NAME
#define IDS_APP_LIST_APP_DRAG_CREATE_FOLDER_ACCESSIBILE_NAME
#define IDS_APP_LIST_APP_DRAG_MOVE_TO_FOLDER_ACCESSIBILE_NAME
#define IDS_APP_LIST_APP_KEYBOARD_CREATE_FOLDER_ACCESSIBILE_NAME
#define IDS_APP_LIST_APP_KEYBOARD_MOVE_TO_FOLDER_ACCESSIBILE_NAME
#define IDS_APP_LIST_BACK
#define IDS_APP_LIST_FOLDER_NAME_PLACEHOLDER
#define IDS_APP_LIST_SEARCH_BOX_AUTOCOMPLETE
#define IDS_APP_LIST_FOLDER_BUTTON_ACCESSIBILE_NAME
#define IDS_APP_LIST_FOLDER_OPEN_FOLDER_ACCESSIBILE_NAME
#define IDS_APP_LIST_FOLDER_CLOSE_FOLDER_ACCESSIBILE_NAME
#define IDS_APP_LIST_EXPAND_BUTTON
#define IDS_APP_LIST_ALL_APPS_ACCESSIBILITY_ANNOUNCEMENT
#define IDS_APP_LIST_SUGGESTED_APPS_ACCESSIBILITY_ANNOUNCEMENT
#define IDS_APP_LIST_CLEAR_SEARCHBOX
#define IDS_APP_LIST_SEARCHBOX_RESULTS_ACCESSIBILITY_ANNOUNCEMENT_ZERO_STATE
#define IDS_APP_LIST_SEARCHBOX_RESULTS_ACCESSIBILITY_ANNOUNCEMENT
#define IDS_APP_LIST_SEARCHBOX_RESULTS_ACCESSIBILITY_ANNOUNCEMENT_SINGLE_RESULT
#define IDS_SHELF_ALIGNMENT_BOTTOM
#define IDS_SHELF_ALIGNMENT_LEFT
#define IDS_SHELF_ALIGNMENT_RIGHT
#define IDS_SHELF_STATE_ALWAYS_SHOWN
#define IDS_SHELF_STATE_ALWAYS_HIDDEN
#define IDS_SHELF_STATE_AUTO_HIDE
#define IDS_SHELF_ITEM_GENERIC_NAME
#define IDS_SHELF_ITEM_WAS_PINNED
#define IDS_SHELF_ITEM_WAS_UNPINNED
#define IDS_SHELF_NEXT
#define IDS_SHELF_PREVIOUS
#define IDS_REMOVE_ZERO_STATE_SUGGESTION_TITLE
#define IDS_REMOVE_ZERO_STATE_SUGGESTION_DETAILS
#define IDS_REMOVE_SUGGESTION_BUTTON_LABEL
#define IDS_APP_LIST_START_ASSISTANT
#define IDS_APP_LIST_PAGE_SWITCHER
#define IDS_APP_LIST_CONTINUE_READING_ACCESSIBILE_NAME
#define IDS_APP_LIST_LEARN_MORE
#define IDS_APP_LIST_ASSISTANT_PRIVACY_INFO
#define IDS_APP_LIST_ASSISTANT_PRIVACY_INFO_CLOSE
#define IDS_APP_ACCESSIBILITY_APP_WITH_STAR_RATING_ARC
#define IDS_APP_ACCESSIBILITY_APP_WITH_PRICE_ARC
#define IDS_APP_ACCESSIBILITY_ARC_APP_ANNOUNCEMENT
#define IDS_APP_ACCESSIBILITY_INSTALLED_APP_ANNOUNCEMENT
#define IDS_APP_ACCESSIBILITY_INTERNAL_APP_ANNOUNCEMENT
#define IDS_APP_ACCESSIBILITY_APP_RECOMMENDATION_ARC
#define IDS_DISPLAY_TOUCH_CALIBRATION_EXIT_LABEL
#define IDS_DISPLAY_TOUCH_CALIBRATION_HINT_LABEL_TEXT
#define IDS_DISPLAY_TOUCH_CALIBRATION_HINT_SUBLABEL_TEXT
#define IDS_DISPLAY_TOUCH_CALIBRATION_TAP_HERE_LABEL
#define IDS_DISPLAY_TOUCH_CALIBRATION_FINISH_LABEL
#define IDS_DISPLAY_NAME_UNKNOWN
#define IDS_DISPLAY_NAME_INTERNAL
#define IDS_CROSTINI_USE_LOW_DENSITY
#define IDS_CROSTINI_USE_HIGH_DENSITY
#define IDS_CROSTINI_APP_RESTART_BODY
#define IDS_CROSTINI_APP_RESTART_BUTTON
#define IDS_CROSTINI_NOT_NOW_BUTTON
#define IDS_SATURATED_BADGE_CONTENT
#define IDS_BADGE_UNREAD_NOTIFICATIONS_SATURATED
#define IDS_BADGE_UNREAD_NOTIFICATIONS_UNSPECIFIED
#define IDS_BADGE_UNREAD_NOTIFICATIONS
#define IDS_BROWSER_SHARING_CLICK_TO_CALL_DIALOG_TITLE_LABEL
#define IDS_BROWSER_SHARING_CLICK_TO_CALL_DIALOG_TITLE_NO_DEVICES
#define IDS_BROWSER_SHARING_CLICK_TO_CALL_DIALOG_HELP_TEXT_NO_DEVICES
#define IDS_BROWSER_SHARING_CLICK_TO_CALL_DIALOG_HELP_TEXT_NO_DEVICES_ORIGIN
#define IDS_BROWSER_SHARING_CLICK_TO_CALL_DIALOG_TROUBLESHOOT_LINK
#define IDS_BROWSER_SHARING_CLICK_TO_CALL_DIALOG_CALL_BUTTON_LABEL
#define IDS_BROWSER_SHARING_OMNIBOX_SENDING_LABEL
#define IDS_BROWSER_SHARING_DIALOG_DEVICE_SUBTITLE_LAST_ACTIVE_DAYS
#define IDS_BROWSER_SHARING_CLICK_TO_CALL_DIALOG_INITIATING_ORIGIN
#define IDS_BROWSER_SHARING_CONTENT_TYPE_TEXT
#define IDS_BROWSER_SHARING_CONTENT_TYPE_NUMBER
#define IDS_BROWSER_SHARING_ERROR_DIALOG_TITLE_GENERIC_ERROR
#define IDS_BROWSER_SHARING_ERROR_DIALOG_TITLE_INTERNAL_ERROR
#define IDS_BROWSER_SHARING_ERROR_DIALOG_TEXT_DEVICE_NOT_FOUND
#define IDS_BROWSER_SHARING_ERROR_DIALOG_TEXT_NETWORK_ERROR
#define IDS_BROWSER_SHARING_ERROR_DIALOG_TEXT_DEVICE_ACK_TIMEOUT
#define IDS_BROWSER_SHARING_ERROR_DIALOG_TEXT_INTERNAL_ERROR
#define IDS_BROWSER_SHARING_SHARED_CLIPBOARD_ERROR_DIALOG_TITLE_PAYLOAD_TOO_LARGE
#define IDS_BROWSER_SHARING_SHARED_CLIPBOARD_ERROR_DIALOG_TEXT_PAYLOAD_TOO_LARGE
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MEMZERO(target,size) bzero((void *)(target), (size_t)(size))
#define MEMZERO
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MEMCOPY(dest,src,size) bcopy((const void *)(src), (void *)(dest), (size_t)(size))
#define MEMCOPY

#else // not BSD, assume ANSI/SysV string lib

//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MEMZERO(target,size) memset((void *)(target), 0, (size_t)(size))
#define MEMZERO
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MEMCOPY(dest,src,size) memcpy((void *)(dest), (const void *)(src), (size_t)(size))
#define MEMCOPY

#endif

/*
 * In ANSI C, and indeed any rational implementation, size_t is also the
 * type returned by sizeof().  However, it seems there are some irrational
 * implementations out there, in which sizeof() returns an int even though
 * size_t is defined as long or unsigned long.  To ensure consistent results
 * we always use this SIZEOF() macro in place of using sizeof() directly.
 */

//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define SIZEOF(object) ((size_t) sizeof(object))

/*
 * The modules that use fread() and fwrite() always invoke them through
 * these macros.  On some systems you may need to twiddle the argument casts.
 * CAUTION: argument order is different from underlying functions!
 *
 * Furthermore, macros are provided for fflush() and ferror() in order
 * to facilitate adaption by applications using an own FILE class.
 */

//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define JFREAD(file,buf,sizeofbuf) ((size_t) fread((void *) (buf), (size_t) 1, (size_t) (sizeofbuf), (file)))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define JFWRITE(file,buf,sizeofbuf) ((size_t) fwrite((const void *) (buf), (size_t) 1, (size_t) (sizeofbuf), (file)))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define JFFLUSH(file) fflush(file)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define JFERROR(file) ferror(file)
