#define BITS_IN_JSAMPLE

/*
 * jmorecfg.h
 *
 * Copyright (C) 1991-1997, Thomas G. Lane.
 * Modified 1997-2013 by Guido Vollbeding.
 * This file is part of the Independent JPEG Group's software.
 * For conditions of distribution and use, see the accompanying README file.
 *
 * This file contains additional configuration options that customize the
 * JPEG software for special applications or support machine-dependent
 * optimizations.  Most users will not need to touch this file.
 */


/*
 * Define BITS_IN_JSAMPLE as either
 *   8   for 8-bit sample values (the usual setting)
 *   9   for 9-bit sample values
 *   10  for 10-bit sample values
 *   11  for 11-bit sample values
 *   12  for 12-bit sample values
 * Only 8, 9, 10, 11, and 12 bits sample data precision are supported for
 * full-feature DCT processing.  Further depths up to 16-bit may be added
 * later for the lossless modes of operation.
 * Run-time selection and conversion of data precision will be added later
 * and are currently not supported, sorry.
 * Exception:  The transcoding part (jpegtran) supports all settings in a
 * single instance, since it operates on the level of DCT coefficients and
 * not sample values.  The DCT coefficients are of the same type (16 bits)
 * in all cases (see below).
 */



/*
 * Maximum number of components (color channels) allowed in JPEG image.
 * To meet the letter of the JPEG spec, set this to 255.  However, darn
 * few applications need more than 4 channels (maybe 5 for CMYK + alpha
 * mask).  We recommend 10 as a reasonable compromise; use 4 if you are
 * really short on memory.  (Each allowed component costs a hundred or so
 * bytes of storage, whether actually used in an image or not.)
 */



/*
 * Basic data types.
 * You may need to change these if you have a machine with unusual data
 * type sizes; for example, "char" not 8 bits, "short" not 16 bits,
 * or "long" not 32 bits.  We don't care whether "int" is 16 or 32 bits,
 * but it had better be at least 16.
 */

/* Representation of a single sample (pixel element value).
 * We frequently allocate large arrays of these, so it's important to keep
 * them small.  But if you have memory to burn and access to char or short
 * arrays is very slow on your hardware, you might want to change these.
 */

//# Laniatus Games Studio Inc. | TODO TASK: C# does not allow setting or comparing #define constants:
#if BITS_IN_JSAMPLE == 8
/* JSAMPLE should be the smallest type that will hold the values 0..255.
 * You can use a signed char by having GETJSAMPLE mask it with 0xFF.
 */

#if HAVE_UNSIGNED_CHAR

//# Laniatus Games Studio Inc. | TODO TASK: Typedefs defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//typedef byte JSAMPLE;
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GETJSAMPLE(value) ((int) (value))
#define GETJSAMPLE

#else // not HAVE_UNSIGNED_CHAR

//# Laniatus Games Studio Inc. | TODO TASK: Typedefs defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//typedef char JSAMPLE;
#if CHAR_IS_UNSIGNED
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GETJSAMPLE(value) ((int) (value))
#define GETJSAMPLE
#else
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GETJSAMPLE(value) ((int) (value) & 0xFF)
#define GETJSAMPLE
#endif // CHAR_IS_UNSIGNED

#endif // HAVE_UNSIGNED_CHAR

#define MAXJSAMPLE
#define CENTERJSAMPLE

#endif // BITS_IN_JSAMPLE == 8


//# Laniatus Games Studio Inc. | TODO TASK: C# does not allow setting or comparing #define constants:
#if BITS_IN_JSAMPLE == 9
/* JSAMPLE should be the smallest type that will hold the values 0..511.
 * On nearly all machines "short" will do nicely.
 */

//# Laniatus Games Studio Inc. | TODO TASK: Typedefs defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//typedef short JSAMPLE;
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GETJSAMPLE(value) ((int) (value))
#define GETJSAMPLE

#define MAXJSAMPLE
#define CENTERJSAMPLE

#endif // BITS_IN_JSAMPLE == 9


//# Laniatus Games Studio Inc. | TODO TASK: C# does not allow setting or comparing #define constants:
#if BITS_IN_JSAMPLE == 10
/* JSAMPLE should be the smallest type that will hold the values 0..1023.
 * On nearly all machines "short" will do nicely.
 */

//# Laniatus Games Studio Inc. | TODO TASK: Typedefs defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//typedef short JSAMPLE;
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GETJSAMPLE(value) ((int) (value))
#define GETJSAMPLE

#define MAXJSAMPLE
#define CENTERJSAMPLE

#endif // BITS_IN_JSAMPLE == 10


//# Laniatus Games Studio Inc. | TODO TASK: C# does not allow setting or comparing #define constants:
#if BITS_IN_JSAMPLE == 11
/* JSAMPLE should be the smallest type that will hold the values 0..2047.
 * On nearly all machines "short" will do nicely.
 */

//# Laniatus Games Studio Inc. | TODO TASK: Typedefs defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//typedef short JSAMPLE;
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GETJSAMPLE(value) ((int) (value))
#define GETJSAMPLE

#define MAXJSAMPLE
#define CENTERJSAMPLE

#endif // BITS_IN_JSAMPLE == 11


//# Laniatus Games Studio Inc. | TODO TASK: C# does not allow setting or comparing #define constants:
#if BITS_IN_JSAMPLE == 12
/* JSAMPLE should be the smallest type that will hold the values 0..4095.
 * On nearly all machines "short" will do nicely.
 */

//# Laniatus Games Studio Inc. | TODO TASK: Typedefs defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//typedef short JSAMPLE;
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GETJSAMPLE(value) ((int) (value))
#define GETJSAMPLE

#define MAXJSAMPLE
#define CENTERJSAMPLE

#endif // BITS_IN_JSAMPLE == 12


/* Representation of a DCT frequency coefficient.
 * This should be a signed value of at least 16 bits; "short" is usually OK.
 * Again, we allocate large arrays of these, but you can change to int
 * if you have memory to burn and "short" is really slow.
 */



/* Compressed datastreams are represented as arrays of JOCTET.
 * These must be EXACTLY 8 bits wide, at least once they are written to
 * external storage.  Note that when using the stdio data source/destination
 * managers, this is also the data type passed to fread/fwrite.
 */

#if HAVE_UNSIGNED_CHAR

//# Laniatus Games Studio Inc. | TODO TASK: Typedefs defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//typedef byte JOCTET;
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GETJOCTET(value) (value)
#define GETJOCTET

#else // not HAVE_UNSIGNED_CHAR

//# Laniatus Games Studio Inc. | TODO TASK: Typedefs defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//typedef char JOCTET;
#if CHAR_IS_UNSIGNED
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GETJOCTET(value) (value)
#define GETJOCTET
#else
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GETJOCTET(value) ((value) & 0xFF)
#define GETJOCTET
#endif // CHAR_IS_UNSIGNED

#endif // HAVE_UNSIGNED_CHAR


/* These typedefs are used for various table entries and so forth.
 * They must be at least as wide as specified; but making them too big
 * won't cost a huge amount of memory, so we don't provide special
 * extraction code like we did for JSAMPLE.  (In other words, these
 * typedefs live at a different point on the speed/space tradeoff curve.)
 */

/* UINT8 must hold at least the values 0..255. */

#if HAVE_UNSIGNED_CHAR
#else // not HAVE_UNSIGNED_CHAR
#if CHAR_IS_UNSIGNED
#else // not CHAR_IS_UNSIGNED
#endif // CHAR_IS_UNSIGNED
#endif // HAVE_UNSIGNED_CHAR

/* UINT16 must hold at least the values 0..65535. */

#if HAVE_UNSIGNED_SHORT
#else // not HAVE_UNSIGNED_SHORT
#endif // HAVE_UNSIGNED_SHORT

/* INT16 must hold at least the values -32768..32767. */

#if ! XMD_H // X11/xmd.h correctly defines INT16
#endif

/* INT32 must hold at least signed 32-bit values. */

#if ! XMD_H // X11/xmd.h correctly defines INT32
#if ! _BASETSD_H_ // Microsoft defines it in basetsd.h
#if ! _BASETSD_H // MinGW is slightly different
#if ! QGLOBAL_H // Qt defines it in qglobal.h
#endif
#endif
#endif
#endif

/* Datatype used for image dimensions.  The JPEG standard only supports
 * images up to 64K*64K due to 16-bit fields in SOF markers.  Therefore
 * "unsigned int" is sufficient on all machines.  However, if you need to
 * handle larger images and you don't mind deviating from the spec, you
 * can change this datatype.
 */




/* These macros are used in all function definitions and extern declarations.
 * You could modify them if you need to change function linkage conventions;
 * in particular, you'll need to do that to make the library a Windows DLL.
 * Another application is to make all functions global for use with debuggers
 * or code profilers that require it.
 */

/* a function called through method pointers: */
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define METHODDEF(type) static type
/* a function used only in its module: */
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LOCAL(type) static type
/* a function referenced thru EXTERNs: */
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GLOBAL(type) type
/* a reference to a GLOBAL function: */
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define EXTERN(type) extern type


/* This macro is used to declare a "method", that is, a function pointer.
 * We want to supply prototype parameters if the compiler can cope.
 * Note that the arglist parameter must be parenthesized!
 * Again, you can customize this if you need special linkage keywords.
 */

#if HAVE_PROTOTYPES
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define JMETHOD(type,methodname,arglist) type (*methodname) arglist
#define JMETHOD
#else
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define JMETHOD(type,methodname,arglist) type (*methodname) ()
#define JMETHOD
#endif


/* The noreturn type identifier is used to declare functions
 * which cannot return.
 * Compilers can thus create more optimized code and perform
 * better checks for warnings and errors.
 * Static analyzer tools can make improved inferences about
 * execution paths and are prevented from giving false alerts.
 *
 * Unfortunately, the proposed specifications of corresponding
 * extensions in the Dec 2011 ISO C standard revision (C11),
 * GCC, MSVC, etc. are not viable.
 * Thus we introduce a user defined type to declare noreturn
 * functions at least for clarity.  A proper compiler would
 * have a suitable noreturn type to match in place of void.
 */

#if ! HAVE_NORETURN_T
//# Laniatus Games Studio Inc. | TODO TASK: Typedefs defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//typedef void noreturn_t;
#endif


/* Here is the pseudo-keyword for declaring pointers that must be "far"
 * on 80x86 machines.  Most of the specialized coding for 80x86 is handled
 * by just saying "FAR *" where such a pointer is needed.  In a few places
 * explicit coding is needed; see uses of the NEED_FAR_POINTERS symbol.
 */

#if ! FAR
#if NEED_FAR_POINTERS
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define FAR far
#define FAR
#else
#define FAR
#endif
#endif


/*
 * On a few systems, type boolean and/or its values FALSE, TRUE may appear
 * in standard header files.  Or you may have conflicts with application-
 * specific header files that you want to include together with these files.
 * Defining HAVE_BOOLEAN before including jpeglib.h should make it work.
 */

#if ! HAVE_BOOLEAN
#if FALSE || TRUE || QGLOBAL_H
/* Qt3 defines FALSE and TRUE as "const" variables in qglobal.h */
//# Laniatus Games Studio Inc. | TODO TASK: Typedefs defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//typedef int boolean;
#else
public enum int
{
	FALSE = 0,
	TRUE = 1
}
#endif
#endif


/*
 * The remaining options affect code selection within the JPEG library,
 * but they don't need to be visible to most applications using the library.
 * To minimize application namespace pollution, the symbols won't be
 * defined unless JPEG_INTERNALS or JPEG_INTERNAL_OPTIONS has been defined.
 */

#if JPEG_INTERNALS
#define JPEG_INTERNAL_OPTIONS
#endif

#if JPEG_INTERNAL_OPTIONS


/*
 * These defines indicate whether to include various optional functions.
 * Undefining some of these symbols will produce a smaller but less capable
 * library.  Note that you can leave certain source files out of the
 * compilation/linking process if you've #undef'd the corresponding symbols.
 * (You may HAVE to do that if your compiler doesn't like null source files.)
 */

/* Capability options common to encoder and decoder: */

#define DCT_ISLOW_SUPPORTED // slow but accurate integer algorithm
#define DCT_IFAST_SUPPORTED // faster, less accurate integer method
#define DCT_FLOAT_SUPPORTED // floating-point: accurate, fast on fast HW

/* Encoder capability options: */

#define C_ARITH_CODING_SUPPORTED // Arithmetic coding back end?
#define C_MULTISCAN_FILES_SUPPORTED // Multiple-scan JPEG files?
#define C_PROGRESSIVE_SUPPORTED // Progressive JPEG? (Requires MULTISCAN)
#define DCT_SCALING_SUPPORTED // Input rescaling via DCT? (Requires DCT_ISLOW)
#define ENTROPY_OPT_SUPPORTED // Optimization of entropy coding parms?
/* Note: if you selected more than 8-bit data precision, it is dangerous to
 * turn off ENTROPY_OPT_SUPPORTED.  The standard Huffman tables are only
 * good for 8-bit precision, so arithmetic coding is recommended for higher
 * precision.  The Huffman encoder normally uses entropy optimization to
 * compute usable tables for higher precision.  Otherwise, you'll have to
 * supply different default Huffman tables.
 * The exact same statements apply for progressive JPEG: the default tables
 * don't work for progressive mode.  (This may get fixed, however.)
 */
#define INPUT_SMOOTHING_SUPPORTED // Input image smoothing option?

/* Decoder capability options: */

#define D_ARITH_CODING_SUPPORTED // Arithmetic coding back end?
#define D_MULTISCAN_FILES_SUPPORTED // Multiple-scan JPEG files?
#define D_PROGRESSIVE_SUPPORTED // Progressive JPEG? (Requires MULTISCAN)
#define IDCT_SCALING_SUPPORTED // Output rescaling via IDCT? (Requires DCT_ISLOW)
#define SAVE_MARKERS_SUPPORTED // jpeg_save_markers() needed?
#define BLOCK_SMOOTHING_SUPPORTED // Block smoothing? (Progressive only)
#undef UPSAMPLE_SCALING_SUPPORTED // Output rescaling at upsample stage?
#define UPSAMPLE_MERGING_SUPPORTED // Fast path for sloppy upsampling?
#define QUANT_1PASS_SUPPORTED // 1-pass color quantization?
#define QUANT_2PASS_SUPPORTED // 2-pass color quantization?

/* more capability options later, no doubt */


/*
 * Ordering of RGB data in scanlines passed to or from the application.
 * If your application wants to deal with data in the order B,G,R, just
 * change these macros.  You can also deal with formats such as R,G,B,X
 * (one extra byte per pixel) by changing RGB_PIXELSIZE.  Note that changing
 * the offsets will also change the order in which colormap data is organized.
 * RESTRICTIONS:
 * 1. The sample applications cjpeg,djpeg do NOT support modified RGB formats.
 * 2. The color quantizer modules will not behave desirably if RGB_PIXELSIZE
 *    is not 3 (they don't understand about dummy color components!).  So you
 *    can't use color quantization if you change that value.
 */

#define RGB_RED
#define RGB_GREEN
#define RGB_BLUE
#define RGB_PIXELSIZE


/* Definitions for speed-related optimizations. */


/* If your compiler supports inline functions, define INLINE
 * as the inline keyword; otherwise define it as empty.
 */

#if ! INLINE
#if __GNUC__ // for instance, GNU C knows about inline
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define INLINE __inline__
#define INLINE
#endif
#define INLINE // default is to define it as empty
#endif


/* On some machines (notably 68000 series) "int" is 32 bits, but multiplying
 * two 16-bit shorts is faster than multiplying two ints.  Define MULTIPLIER
 * as short on such a machine.  MULTIPLIER must be at least 16 bits wide.
 */

//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MULTIPLIER int
#define MULTIPLIER // type for fastest integer multiply


/* FAST_FLOAT should be either float or double, whichever is done faster
 * by your compiler.  (Note that this type is only used in the floating point
 * DCT routines, so it only matters if you've defined DCT_FLOAT_SUPPORTED.)
 * Typically, float is faster in ANSI C compilers, while double is faster in
 * pre-ANSI compilers (because they insist on converting to double anyway).
 * The code below therefore chooses float if we have ANSI-style prototypes.
 */

#if ! FAST_FLOAT
#if HAVE_PROTOTYPES
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define FAST_FLOAT float
#define FAST_FLOAT
#else
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define FAST_FLOAT double
#define FAST_FLOAT
#endif
#endif

#endif // JPEG_INTERNAL_OPTIONS
