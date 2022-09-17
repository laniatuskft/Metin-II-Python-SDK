/*
 * jpeglib.h
 *
 * Copyright (C) 1991-1998, Thomas G. Lane.
 * Modified 2002-2017 by Guido Vollbeding.
 * This file is part of the Independent JPEG Group's software.
 * For conditions of distribution and use, see the accompanying README file.
 *
 * This file defines the application interface for the JPEG library.
 * Most applications using the library need only include this file,
 * and perhaps jerror.h if they want to know the exact error codes.
 */


/*
 * First we include the configuration files that record how this
 * installation of the JPEG library is set up.  jconfig.h can be
 * generated automatically for many systems.  jmorecfg.h contains
 * manual configuration options that most people need not worry about.
 */

#if ! JCONFIG_INCLUDED // in case jinclude.h already did
#define HAVE_PROTOTYPES
#define HAVE_UNSIGNED_CHAR
#define HAVE_UNSIGNED_SHORT
#define HAVE_STDDEF_H
#define HAVE_STDLIB_H
#define HAVE_BOOLEAN // prevent jmorecfg.h from redefining it
#define BMP_SUPPORTED // BMP image file format
#define GIF_SUPPORTED // GIF image file format
#define PPM_SUPPORTED // PBMPLUS PPM/PGM image file format
#define TARGA_SUPPORTED // Targa image file format
#define TWO_FILE_COMMANDLINE // optional
#define USE_SETMODE // Microsoft has setmode()
#endif
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GETJSAMPLE(value) ((int) (value))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GETJSAMPLE(value) ((int) (value))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GETJSAMPLE(value) ((int) (value) & 0xFF)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GETJSAMPLE(value) ((int) (value))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GETJSAMPLE(value) ((int) (value))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GETJSAMPLE(value) ((int) (value))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GETJSAMPLE(value) ((int) (value))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GETJOCTET(value) (value)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GETJOCTET(value) (value)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GETJOCTET(value) ((value) & 0xFF)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define METHODDEF(type) static type
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LOCAL(type) static type
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GLOBAL(type) type
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define EXTERN(type) extern type
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define JMETHOD(type,methodname,arglist) type (*methodname) arglist
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define JMETHOD(type,methodname,arglist) type (*methodname) ()
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define FAR far
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define INLINE __inline__
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MULTIPLIER int
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define FAST_FLOAT float
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define FAST_FLOAT double


#if __cplusplus
#if ! DONT_USE_EXTERN_C
#endif
#endif

/* Version IDs for the JPEG library.
 * Might be useful for tests like "#if JPEG_LIB_VERSION >= 90".
 */



/* Various constants determining the sizes of things.
 * All of these are specified by the JPEG standard,
 * so don't change them if you want to be compatible.
 */

/* Unfortunately, some bozo at Adobe saw no reason to be bound by the standard;
 * the PostScript DCT filter can emit files with many more than 10 blocks/MCU.
 * If you happen to run across such a file, you can up D_MAX_BLOCKS_IN_MCU
 * to handle it.  We even let you do this from the jconfig.h file.  However,
 * we strongly discourage changing C_MAX_BLOCKS_IN_MCU; just because Adobe
 * sometimes emits noncompliant files doesn't mean you should too.
 */


/* Data structures for images (arrays of samples and of DCT coefficients).
 * On 80x86 machines, the image arrays are too big for near pointers,
 * but the pointer arrays can fit in near memory.
 */





/* Types for JPEG compression parameters and working tables. */


/* DCT coefficient quantization tables. */

public class JQUANT_TBL
{
  /* This array gives the coefficient quantizers in natural array order
   * (not the zigzag order in which they are stored in a JPEG DQT marker).
   * CAUTION: IJG versions prior to v6a kept this array in zigzag order.
   */
  public ushort[] quantval = new ushort[DefineConstants.DCTSIZE2]; // quantization step for each coefficient
  /* This field is used only during compression.  It's initialized FALSE when
   * the table is created, and set TRUE when it's been output to the file.
   * You could suppress output of a table by setting this to TRUE.
   * (See jpeg_suppress_tables for an example.)
   */
  public boolean sent_table; // TRUE when table has been output
}


/* Huffman coding tables. */

public class JHUFF_TBL
{
  /* These two fields directly represent the contents of a JPEG DHT marker */
  public short[] bits = new short[17]; // bits[k] = # of symbols with codes of
				/* length k bits; bits[0] is unused */
  public short[] huffval = new short[256]; // The symbols, in order of incr code length
  /* This field is used only during compression.  It's initialized FALSE when
   * the table is created, and set TRUE when it's been output to the file.
   * You could suppress output of a table by setting this to TRUE.
   * (See jpeg_suppress_tables for an example.)
   */
  public boolean sent_table; // TRUE when table has been output
}


/* Basic info about one component (color channel). */

public class jpeg_component_info
{
  /* These values are fixed over the whole image. */
  /* For compression, they must be supplied by parameter setup; */
  /* for decompression, they are read from the SOF marker. */
  public int component_id; // identifier for this component (0..255)
  public int component_index; // its index in SOF or cinfo->comp_info[]
  public int h_samp_factor; // horizontal sampling factor (1..4)
  public int v_samp_factor; // vertical sampling factor (1..4)
  public int quant_tbl_no; // quantization table selector (0..3)
  /* These values may vary between scans. */
  /* For compression, they must be supplied by parameter setup; */
  /* for decompression, they are read from the SOS marker. */
  /* The decompressor output side may not use these variables. */
  public int dc_tbl_no; // DC entropy table selector (0..3)
  public int ac_tbl_no; // AC entropy table selector (0..3)

  /* Remaining fields should be treated as private by applications. */

  /* These values are computed during compression or decompression startup: */
  /* Component's size in DCT blocks.
   * Any dummy blocks added to complete an MCU are not counted; therefore
   * these values do not depend on whether a scan is interleaved or not.
   */
  public uint width_in_blocks;
  public uint height_in_blocks;
  /* Size of a DCT block in samples,
   * reflecting any scaling we choose to apply during the DCT step.
   * Values from 1 to 16 are supported.
   * Note that different components may receive different DCT scalings.
   */
  public int DCT_h_scaled_size;
  public int DCT_v_scaled_size;
  /* The downsampled dimensions are the component's actual, unpadded number
   * of samples at the main buffer (preprocessing/compression interface);
   * DCT scaling is included, so
   * downsampled_width =
   *   ceil(image_width * Hi/Hmax * DCT_h_scaled_size/block_size)
   * and similarly for height.
   */
  public uint downsampled_width; // actual width in samples
  public uint downsampled_height; // actual height in samples
  /* For decompression, in cases where some of the components will be
   * ignored (eg grayscale output from YCbCr image), we can skip most
   * computations for the unused components.
   * For compression, some of the components will need further quantization
   * scale by factor of 2 after DCT (eg BG_YCC output from normal RGB input).
   * The field is first set TRUE for decompression, FALSE for compression
   * in initial_setup, and then adapted in color conversion setup.
   */
  public boolean component_needed;

  /* These values are computed before starting a scan of the component. */
  /* The decompressor output side may not use these variables. */
  public int MCU_width; // number of blocks per MCU, horizontally
  public int MCU_height; // number of blocks per MCU, vertically
  public int MCU_blocks; // MCU_width * MCU_height
  public int MCU_sample_width; // MCU width in samples: MCU_width * DCT_h_scaled_size
  public int last_col_width; // # of non-dummy blocks across in last MCU
  public int last_row_height; // # of non-dummy blocks down in last MCU

  /* Saved quantization table for component; NULL if none yet saved.
   * See jdinput.c comments about the need for this information.
   * This field is currently used only for decompression.
   */
  public JQUANT_TBL quant_table;

  /* Private per-component storage for DCT or IDCT subsystem. */
  public object dct_table;
}


/* The script for encoding a multiple-scan file is an array of these: */

public class jpeg_scan_info
{
  public int comps_in_scan; // number of components encoded in this scan
  public int[] component_index = new int[DefineConstants.MAX_COMPS_IN_SCAN]; // their SOF/comp_info[] indexes
  public int Ss; // progressive JPEG spectral selection parms
  public int Se;
  public int Ah; // progressive JPEG successive approx. parms
  public int Al;
}

/* The decompressor can save APPn and COM markers in a list of these: */


public class jpeg_marker_struct
{
  public jpeg_marker_struct next; // next in list, or NULL
  public short marker; // marker code: JPEG_COM, or JPEG_APP0+n
  public uint original_length; // # bytes of data in the file
  public uint data_length; // # bytes of data saved at data[]
  public JOCTET[] data; // the data contained in the marker
  /* the marker length word is not counted in data_length or original_length */
}

/* Known color spaces. */

public enum J_COLOR_SPACE
{
	JCS_UNKNOWN, // error/unspecified
	JCS_GRAYSCALE, // monochrome
	JCS_RGB, // red/green/blue, standard RGB (sRGB)
	JCS_YCbCr, // Y/Cb/Cr (also known as YUV), standard YCC
	JCS_CMYK, // C/M/Y/K
	JCS_YCCK, // Y/Cb/Cr/K
	JCS_BG_RGB, // big gamut red/green/blue, bg-sRGB
	JCS_BG_YCC // big gamut Y/Cb/Cr, bg-sYCC
}

/* Supported color transforms. */

public enum J_COLOR_TRANSFORM
{
	JCT_NONE = 0,
	JCT_SUBTRACT_GREEN = 1
}

/* DCT/IDCT algorithm options. */

public enum J_DCT_METHOD
{
	JDCT_ISLOW, // slow but accurate integer algorithm
	JDCT_IFAST, // faster, less accurate integer method
	JDCT_FLOAT // floating-point: accurate, fast on fast HW
}

//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define JDCT_DEFAULT JDCT_ISLOW
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define JDCT_FASTEST JDCT_IFAST

/* Dithering options for decompression. */

public enum J_DITHER_MODE
{
	JDITHER_NONE, // no dithering
	JDITHER_ORDERED, // simple ordered dither
	JDITHER_FS // Floyd-Steinberg error diffusion dither
}


/* Common fields between JPEG compression and decompression master structs. */

//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jpeg_common_fields struct jpeg_error_mgr * err; struct jpeg_memory_mgr * mem; struct jpeg_progress_mgr * progress; void * client_data; boolean is_decompressor; int global_state

/* Routines that are to be used by both halves of the library are declared
 * to receive a pointer to this structure.  There are no actual instances of
 * jpeg_common_struct, only of jpeg_compress_struct and jpeg_decompress_struct.
 */
public class jpeg_common_struct
{
  public jpeg_error_mgr err;
  public jpeg_memory_mgr mem;
  public jpeg_progress_mgr progress;
  public object client_data;
  public boolean is_decompressor;
  public int global_state; // Fields common to both master struct types
  /* Additional fields follow in an actual jpeg_compress_struct or
   * jpeg_decompress_struct.  All three structs must agree on these
   * initial fields!  (This would be a lot cleaner in C++.)
   */
}



/* Master record for a compression instance */

public class jpeg_compress_struct
{
  public jpeg_error_mgr err;
  public jpeg_memory_mgr mem;
  public jpeg_progress_mgr progress;
  public object client_data;
  public boolean is_decompressor;
  public int global_state; // Fields shared with jpeg_decompress_struct

  /* Destination for compressed data */
  public jpeg_destination_mgr[] dest;

  /* Description of source image --- these fields must be filled in by
   * outer application before starting compression.  in_color_space must
   * be correct before you can even call jpeg_set_defaults().
   */

  public uint image_width; // input image width
  public uint image_height; // input image height
  public int input_components; // # of color components in input image
  public J_COLOR_SPACE in_color_space; // colorspace of input image

  public double input_gamma; // image gamma of input image

  /* Compression parameters --- these fields must be set before calling
   * jpeg_start_compress().  We recommend calling jpeg_set_defaults() to
   * initialize everything to reasonable defaults, then changing anything
   * the application specifically wants to change.  That way you won't get
   * burnt when new parameters are added.  Also note that there are several
   * helper routines to simplify changing parameters.
   */

  public uint scale_num; // fraction by which to scale image
  public uint scale_denom;

  public uint jpeg_width; // scaled JPEG image width
  public uint jpeg_height; // scaled JPEG image height
  /* Dimensions of actual JPEG image that will be written to file,
   * derived from input dimensions by scaling factors above.
   * These fields are computed by jpeg_start_compress().
   * You can also use jpeg_calc_jpeg_dimensions() to determine these values
   * in advance of calling jpeg_start_compress().
   */

  public int data_precision; // bits of precision in image data

  public int num_components; // # of color components in JPEG image
  public J_COLOR_SPACE jpeg_color_space; // colorspace of JPEG image

  public jpeg_component_info[] comp_info;
  /* comp_info[LaniatusDefVariables] describes component that appears i'th in SOF */

  public JQUANT_TBL[] quant_tbl_ptrs = new JQUANT_TBL[DefineConstants.NUM_QUANT_TBLS];
  public int[] q_scale_factor = new int[DefineConstants.NUM_QUANT_TBLS];
  /* ptrs to coefficient quantization tables, or NULL if not defined,
   * and corresponding scale factors (percentage, initialized 100).
   */

  public JHUFF_TBL[] dc_huff_tbl_ptrs = new JHUFF_TBL[DefineConstants.NUM_HUFF_TBLS];
  public JHUFF_TBL[] ac_huff_tbl_ptrs = new JHUFF_TBL[DefineConstants.NUM_HUFF_TBLS];
  /* ptrs to Huffman coding tables, or NULL if not defined */

  public short[] arith_dc_L = new short[DefineConstants.NUM_ARITH_TBLS]; // L values for DC arith-coding tables
  public short[] arith_dc_U = new short[DefineConstants.NUM_ARITH_TBLS]; // U values for DC arith-coding tables
  public short[] arith_ac_K = new short[DefineConstants.NUM_ARITH_TBLS]; // Kx values for AC arith-coding tables

  public int num_scans; // # of entries in scan_info array
  public readonly jpeg_scan_info scan_info; // script for multi-scan file, or NULL
  /* The default value of scan_info is NULL, which causes a single-scan
   * sequential JPEG file to be emitted.  To create a multi-scan file,
   * set num_scans and scan_info to point to an array of scan definitions.
   */

  public boolean raw_data_in; // TRUE=caller supplies downsampled data
  public boolean arith_code; // TRUE=arithmetic coding, FALSE=Huffman
  public boolean optimize_coding; // TRUE=optimize entropy encoding parms
  public boolean CCIR601_sampling; // TRUE=first samples are cosited
  public boolean do_fancy_downsampling; // TRUE=apply fancy downsampling
  public int smoothing_factor; // 1..100, or 0 for no input smoothing
  public J_DCT_METHOD dct_method; // DCT algorithm selector

  /* The restart interval can be specified in absolute MCUs by setting
   * restart_interval, or in MCU rows by setting restart_in_rows
   * (in which case the correct restart_interval will be figured
   * for each scan).
   */
  public uint restart_interval; // MCUs per restart, or 0 for no restart
  public int restart_in_rows; // if > 0, MCU rows per restart interval

  /* Parameters controlling emission of special markers. */

  public boolean write_JFIF_header; // should a JFIF marker be written?
  public short JFIF_major_version; // What to write for the JFIF version number
  public short JFIF_minor_version;
  /* These three values are not used by the JPEG code, merely copied */
  /* into the JFIF APP0 marker.  density_unit can be 0 for unknown, */
  /* 1 for dots/inch, or 2 for dots/cm.  Note that the pixel aspect */
  /* ratio is defined by X_density/Y_density even when density_unit=0. */
  public short density_unit; // JFIF code for pixel size units
  public ushort X_density; // Horizontal pixel density
  public ushort Y_density; // Vertical pixel density
  public boolean write_Adobe_marker; // should an Adobe marker be written?

  public J_COLOR_TRANSFORM color_transform;
  /* Color transform identifier, writes LSE marker if nonzero */

  /* State variable: index of next scanline to be written to
   * jpeg_write_scanlines().  Application may use this to control its
   * processing loop, e.g., "while (next_scanline < image_height)".
   */

  public uint next_scanline; // 0 .. image_height-1

  /* Remaining fields are known throughout compressor, but generally
   * should not be touched by a surrounding application.
   */

  /*
   * These fields are computed during compression startup
   */
  public boolean progressive_mode; // TRUE if scan script uses progressive mode
  public int max_h_samp_factor; // largest h_samp_factor
  public int max_v_samp_factor; // largest v_samp_factor

  public int min_DCT_h_scaled_size; // smallest DCT_h_scaled_size of any component
  public int min_DCT_v_scaled_size; // smallest DCT_v_scaled_size of any component

  public uint total_iMCU_rows; // # of iMCU rows to be input to coef ctlr
  /* The coefficient controller receives data in units of MCU rows as defined
   * for fully interleaved scans (whether the JPEG file is interleaved or not).
   * There are v_samp_factor * DCT_v_scaled_size sample rows of each component
   * in an "iMCU" (interleaved MCU) row.
   */

  /*
   * These fields are valid during any one scan.
   * They describe the components and MCUs actually appearing in the scan.
   */
  public int comps_in_scan; // # of JPEG components in this scan
  public jpeg_component_info[] cur_comp_info = new jpeg_component_info[DefineConstants.MAX_COMPS_IN_SCAN];
  /* *cur_comp_info[LaniatusDefVariables] describes component that appears i'th in SOS */

  public uint MCUs_per_row; // # of MCUs across the image
  public uint MCU_rows_in_scan; // # of MCU rows in the image

  public int blocks_in_MCU; // # of DCT blocks per MCU
  public int[] MCU_membership = new int[DefineConstants.C_MAX_BLOCKS_IN_MCU];
  /* MCU_membership[LaniatusDefVariables] is index in cur_comp_info of component owning */
  /* i'th block in an MCU */

  public int Ss; // progressive JPEG parameters for scan
  public int Se;
  public int Ah;
  public int Al;

  public int block_size; // the basic DCT block size: 1..16
  public readonly int[] natural_order; // natural-order position array
  public int lim_Se; // min( Se, DCTSIZE2-1 )

  /*
   * Links to compression subobjects (methods and private variables of modules)
   */
  public jpeg_comp_master master;
  public jpeg_c_main_controller main;
  public jpeg_c_prep_controller prep;
  public jpeg_c_coef_controller coef;
  public jpeg_marker_writer marker;
  public jpeg_color_converter cconvert;
  public jpeg_downsampler downsample;
  public jpeg_forward_dct fdct;
  public jpeg_entropy_encoder entropy;
  public jpeg_scan_info script_space; // workspace for jpeg_simple_progression
  public int script_space_size;
}


/* Master record for a decompression instance */

public class jpeg_decompress_struct
{
  public jpeg_error_mgr err;
  public jpeg_memory_mgr mem;
  public jpeg_progress_mgr progress;
  public object client_data;
  public boolean is_decompressor;
  public int global_state; // Fields shared with jpeg_compress_struct

  /* Source of compressed data */
  public jpeg_source_mgr[] src;

  /* Basic description of image --- filled in by jpeg_read_header(). */
  /* Application may inspect these values to decide how to process image. */

  public uint image_width; // nominal image width (from SOF marker)
  public uint image_height; // nominal image height
  public int num_components; // # of color components in JPEG image
  public J_COLOR_SPACE jpeg_color_space; // colorspace of JPEG image

  /* Decompression processing parameters --- these fields must be set before
   * calling jpeg_start_decompress().  Note that jpeg_read_header() initializes
   * them to default values.
   */

  public J_COLOR_SPACE out_color_space; // colorspace for output

  public uint scale_num; // fraction by which to scale image
  public uint scale_denom;

  public double output_gamma; // image gamma wanted in output

  public boolean buffered_image; // TRUE=multiple output passes
  public boolean raw_data_out; // TRUE=downsampled data wanted

  public J_DCT_METHOD dct_method; // IDCT algorithm selector
  public boolean do_fancy_upsampling; // TRUE=apply fancy upsampling
  public boolean do_block_smoothing; // TRUE=apply interblock smoothing

  public boolean quantize_colors; // TRUE=colormapped output wanted
  /* the following are ignored if not quantize_colors: */
  public J_DITHER_MODE dither_mode; // type of color dithering to use
  public boolean two_pass_quantize; // TRUE=use two-pass color quantization
  public int desired_number_of_colors; // max # colors to use in created colormap
  /* these are significant only in buffered-image mode: */
  public boolean enable_1pass_quant; // enable future use of 1-pass quantizer
  public boolean enable_external_quant; // enable future use of external colormap
  public boolean enable_2pass_quant; // enable future use of 2-pass quantizer

  /* Description of actual output image that will be returned to application.
   * These fields are computed by jpeg_start_decompress().
   * You can also use jpeg_calc_output_dimensions() to determine these values
   * in advance of calling jpeg_start_decompress().
   */

  public uint output_width; // scaled image width
  public uint output_height; // scaled image height
  public int out_color_components; // # of color components in out_color_space
  public int output_components; // # of color components returned
  /* output_components is 1 (a colormap index) when quantizing colors;
   * otherwise it equals out_color_components.
   */
  public int rec_outbuf_height; // min recommended height of scanline buffer
  /* If the buffer passed to jpeg_read_scanlines() is less than this many rows
   * high, space and time will be wasted due to unnecessary data copying.
   * Usually rec_outbuf_height will be 1 or 2, at most 4.
   */

  /* When quantizing colors, the output colormap is described by these fields.
   * The application can supply a colormap by setting colormap non-NULL before
   * calling jpeg_start_decompress; otherwise a colormap is created during
   * jpeg_start_decompress or jpeg_start_output.
   * The map has out_color_components rows and actual_number_of_colors columns.
   */
  public int actual_number_of_colors; // number of entries in use
  public JSAMPLE[] colormap; // The color map as a 2-D pixel array

  /* State variables: these variables indicate the progress of decompression.
   * The application may examine these but must not modify them.
   */

  /* Row index of next scanline to be read from jpeg_read_scanlines().
   * Application may use this to control its processing loop, e.g.,
   * "while (output_scanline < output_height)".
   */
  public uint output_scanline; // 0 .. output_height-1

  /* Current input scan number and number of iMCU rows completed in scan.
   * These indicate the progress of the decompressor input side.
   */
  public int input_scan_number; // Number of SOS markers seen so far
  public uint input_iMCU_row; // Number of iMCU rows completed

  /* The "output scan number" is the notional scan being displayed by the
   * output side.  The decompressor will not allow output scan/row number
   * to get ahead of input scan/row, but it can fall arbitrarily far behind.
   */
  public int output_scan_number; // Nominal scan number being displayed
  public uint output_iMCU_row; // Number of iMCU rows read

  /* Current progression status.  coef_bits[c][LaniatusDefVariables] indicates the precision
   * with which component c's DCT coefficient LaniatusDefVariables (in zigzag order) is known.
   * It is -1 when no data has yet been received, otherwise it is the point
   * transform (shift) value for the most recent scan of the coefficient
   * (thus, 0 at completion of the progression).
   * This pointer is NULL when reading a non-progressive file.
   */
  public int[] coef_bits = new int[DefineConstants.DCTSIZE2]; // -1 or current Al value for each coef

  /* Internal JPEG parameters --- the application usually need not look at
   * these fields.  Note that the decompressor output side may not use
   * any parameters that can change between scans.
   */

  /* Quantization and Huffman tables are carried forward across input
   * datastreams when processing abbreviated JPEG datastreams.
   */

  public JQUANT_TBL[] quant_tbl_ptrs = new JQUANT_TBL[DefineConstants.NUM_QUANT_TBLS];
  /* ptrs to coefficient quantization tables, or NULL if not defined */

  public JHUFF_TBL[] dc_huff_tbl_ptrs = new JHUFF_TBL[DefineConstants.NUM_HUFF_TBLS];
  public JHUFF_TBL[] ac_huff_tbl_ptrs = new JHUFF_TBL[DefineConstants.NUM_HUFF_TBLS];
  /* ptrs to Huffman coding tables, or NULL if not defined */

  /* These parameters are never carried across datastreams, since they
   * are given in SOF/SOS markers or defined to be reset by SOI.
   */

  public int data_precision; // bits of precision in image data

  public jpeg_component_info[] comp_info;
  /* comp_info[LaniatusDefVariables] describes component that appears i'th in SOF */

  public boolean is_baseline; // TRUE if Baseline SOF0 encountered
  public boolean progressive_mode; // TRUE if SOFn specifies progressive mode
  public boolean arith_code; // TRUE=arithmetic coding, FALSE=Huffman

  public short[] arith_dc_L = new short[DefineConstants.NUM_ARITH_TBLS]; // L values for DC arith-coding tables
  public short[] arith_dc_U = new short[DefineConstants.NUM_ARITH_TBLS]; // U values for DC arith-coding tables
  public short[] arith_ac_K = new short[DefineConstants.NUM_ARITH_TBLS]; // Kx values for AC arith-coding tables

  public uint restart_interval; // MCUs per restart interval, or 0 for no restart

  /* These fields record data obtained from optional markers recognized by
   * the JPEG library.
   */
  public boolean saw_JFIF_marker; // TRUE iff a JFIF APP0 marker was found
  /* Data copied from JFIF marker; only valid if saw_JFIF_marker is TRUE: */
  public short JFIF_major_version; // JFIF version number
  public short JFIF_minor_version;
  public short density_unit; // JFIF code for pixel size units
  public ushort X_density; // Horizontal pixel density
  public ushort Y_density; // Vertical pixel density
  public boolean saw_Adobe_marker; // TRUE iff an Adobe APP14 marker was found
  public short Adobe_transform; // Color transform code from Adobe marker

  public J_COLOR_TRANSFORM color_transform;
  /* Color transform identifier derived from LSE marker, otherwise zero */

  public boolean CCIR601_sampling; // TRUE=first samples are cosited

  /* Aside from the specific data retained from APPn markers known to the
   * library, the uninterpreted contents of any or all APPn and COM markers
   * can be saved in a list for examination by the application.
   */
  public jpeg_marker_struct marker_list; // Head of list of saved markers

  /* Remaining fields are known throughout decompressor, but generally
   * should not be touched by a surrounding application.
   */

  /*
   * These fields are computed during decompression startup
   */
  public int max_h_samp_factor; // largest h_samp_factor
  public int max_v_samp_factor; // largest v_samp_factor

  public int min_DCT_h_scaled_size; // smallest DCT_h_scaled_size of any component
  public int min_DCT_v_scaled_size; // smallest DCT_v_scaled_size of any component

  public uint total_iMCU_rows; // # of iMCU rows in image
  /* The coefficient controller's input and output progress is measured in
   * units of "iMCU" (interleaved MCU) rows.  These are the same as MCU rows
   * in fully interleaved JPEG scans, but are used whether the scan is
   * interleaved or not.  We define an iMCU row as v_samp_factor DCT block
   * rows of each component.  Therefore, the IDCT output contains
   * v_samp_factor * DCT_v_scaled_size sample rows of a component per iMCU row.
   */

  public JSAMPLE sample_range_limit; // table for fast range-limiting

  /*
   * These fields are valid during any one scan.
   * They describe the components and MCUs actually appearing in the scan.
   * Note that the decompressor output side must not use these fields.
   */
  public int comps_in_scan; // # of JPEG components in this scan
  public jpeg_component_info[] cur_comp_info = new jpeg_component_info[DefineConstants.MAX_COMPS_IN_SCAN];
  /* *cur_comp_info[LaniatusDefVariables] describes component that appears i'th in SOS */

  public uint MCUs_per_row; // # of MCUs across the image
  public uint MCU_rows_in_scan; // # of MCU rows in the image

  public int blocks_in_MCU; // # of DCT blocks per MCU
  public int[] MCU_membership = new int[DefineConstants.D_MAX_BLOCKS_IN_MCU];
  /* MCU_membership[LaniatusDefVariables] is index in cur_comp_info of component owning */
  /* i'th block in an MCU */

  public int Ss; // progressive JPEG parameters for scan
  public int Se;
  public int Ah;
  public int Al;

  /* These fields are derived from Se of first SOS marker.
   */
  public int block_size; // the basic DCT block size: 1..16
  public readonly int[] natural_order; // natural-order position array for entropy decode
  public int lim_Se; // min( Se, DCTSIZE2-1 ) for entropy decode

  /* This field is shared between entropy decoder and marker parser.
   * It is either zero or the code of a JPEG marker that has been
   * read from the data source, but has not yet been processed.
   */
  public int unread_marker;

  /*
   * Links to decompression subobjects (methods, private variables of modules)
   */
  public jpeg_decomp_master master;
  public jpeg_d_main_controller main;
  public jpeg_d_coef_controller coef;
  public jpeg_d_post_controller post;
  public jpeg_input_controller inputctl;
  public jpeg_marker_reader marker;
  public jpeg_entropy_decoder entropy;
  public jpeg_inverse_dct idct;
  public jpeg_upsampler upsample;
  public jpeg_color_deconverter cconvert;
  public jpeg_color_quantizer cquantize;
}


/* "Object" declarations for JPEG modules that may be supplied or called
 * directly by the surrounding application.
 * As with all objects in the JPEG library, these structs only define the
 * publicly visible methods and state variables of a module.  Additional
 * private fields may exist after the public ones.
 */


/* Error handler object */

public class jpeg_error_mgr
{
  /* Error exit handler: does not return to caller */
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(void, error_exit, (struct jpeg_common_struct * cinfo));
  /* Conditionally emit a trace or warning message */
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(void, emit_message, (struct jpeg_common_struct * cinfo, int msg_level));
  /* Routine that actually outputs a trace or error message */
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(void, output_message, (struct jpeg_common_struct * cinfo));
  /* Format a message string for the most recent JPEG error or message */
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(void, format_message, (struct jpeg_common_struct * cinfo, char * buffer));
	public const int JMSG_LENGTH_MAX = 200; // recommended size of format_message buffer
  /* Reset error state variables at start of a new image */
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(void, reset_error_mgr, (struct jpeg_common_struct * cinfo));

  /* The message ID code and any parameters are saved here.
   * A message can have one string parameter or up to 8 int parameters.
   */
  public int msg_code;
	public const int JMSG_STR_PARM_MAX = 80;
//# Laniatus Games Studio Inc. | TODO TASK: Unions are not supported in C#:
//  union
//  {
//	int i[8];
//	char s[JMSG_STR_PARM_MAX];
//  }
//# Laniatus Games Studio Inc. |: Access declarations are not available in C#:
//  msg_parm;

  /* Standard state variables for error facility */

  public int trace_level; // max msg_level that will be displayed

  /* For recoverable corrupt-data errors, we emit a warning message,
   * but keep going unless emit_message chooses to abort.  emit_message
   * should count warnings in num_warnings.  The surrounding application
   * can check for bad data by seeing if num_warnings is nonzero at the
   * end of processing.
   */
  public int num_warnings; // number of corrupt-data warnings

  /* These fields point to the table(s) of error message strings.
   * An application can change the table pointer to switch to a different
   * message list (typically, to change the language in which errors are
   * reported).  Some applications may wish to add additional error codes
   * that will be handled by the JPEG library error mechanism; the second
   * table pointer is used for this purpose.
   *
   * First table includes all errors generated by JPEG library itself.
   * Error code 0 is reserved for a "no such error string" message.
   */
  public readonly char * * jpeg_message_table; // Library errors
  public int last_jpeg_message; // Table contains strings 0..last_jpeg_message
  /* Second table can be added by application (see cjpeg/djpeg for example).
   * It contains strings numbered first_addon_message..last_addon_message.
   */
  public readonly char * * addon_message_table; // Non-library errors
  public int first_addon_message; // code for first string in addon table
  public int last_addon_message; // code for last string in addon table
}


/* Progress monitor object */

public class jpeg_progress_mgr
{
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(void, progress_monitor, (struct jpeg_common_struct * cinfo));

  public int pass_counter; // work units completed in this pass
  public int pass_limit; // total number of work units in this pass
  public int completed_passes; // passes completed so far
  public int total_passes; // total number of passes expected
}


/* Data destination object for compression */

public class jpeg_destination_mgr
{
  public JOCTET next_output_byte; // => next byte to write in buffer
  public size_t free_in_buffer = new size_t(); // # of byte spaces remaining in buffer

//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(void, init_destination, (struct jpeg_compress_struct * cinfo));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(boolean, empty_output_buffer, (struct jpeg_compress_struct * cinfo));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(void, term_destination, (struct jpeg_compress_struct * cinfo));
}


/* Data source object for decompression */

public class jpeg_source_mgr
{
  public readonly JOCTET next_input_byte; // => next byte to read from buffer
  public size_t bytes_in_buffer = new size_t(); // # of bytes remaining in buffer

//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(void, init_source, (struct jpeg_decompress_struct * cinfo));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(boolean, fill_input_buffer, (struct jpeg_decompress_struct * cinfo));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(void, skip_input_data, (struct jpeg_decompress_struct * cinfo, int num_bytes));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(boolean, resync_to_restart, (struct jpeg_decompress_struct * cinfo, int desired));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(void, term_source, (struct jpeg_decompress_struct * cinfo));
}


/* Memory manager object.
 * Allocates "small" objects (a few K total), "large" objects (tens of K),
 * and "really big" objects (virtual arrays with backing store if needed).
 * The memory manager does not allow individual objects to be freed; rather,
 * each created object is assigned to a pool, and whole pools can be freed
 * at once.  This is faster and more convenient than remembering exactly what
 * to free, especially where malloc()/free() are not too speedy.
 * NB: alloc routines never return NULL.  They exit to error_exit if not
 * successful.
 */




public class jpeg_memory_mgr
{
  /* Method pointers */
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(object*, alloc_small, (struct jpeg_common_struct * cinfo, int pool_id, size_t sizeofobject));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(void FAR *, alloc_large, (struct jpeg_common_struct * cinfo, int pool_id, size_t sizeofobject));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(JSAMPLE FAR * *, alloc_sarray, (struct jpeg_common_struct * cinfo, int pool_id, uint samplesperrow, uint numrows));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(short FAR[DefineConstants.DCTSIZE2] * *, alloc_barray, (struct jpeg_common_struct * cinfo, int pool_id, uint blocksperrow, uint numrows));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(struct jvirt_sarray_control *, request_virt_sarray, (struct jpeg_common_struct * cinfo, int pool_id, boolean pre_zero, uint samplesperrow, uint numrows, uint maxaccess));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(struct jvirt_barray_control *, request_virt_barray, (struct jpeg_common_struct * cinfo, int pool_id, boolean pre_zero, uint blocksperrow, uint numrows, uint maxaccess));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(void, realize_virt_arrays, (struct jpeg_common_struct * cinfo));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(JSAMPLE FAR * *, access_virt_sarray, (struct jpeg_common_struct * cinfo, struct jvirt_sarray_control * ptr, uint start_row, uint num_rows, boolean writable));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(short FAR[DefineConstants.DCTSIZE2] * *, access_virt_barray, (struct jpeg_common_struct * cinfo, struct jvirt_barray_control * ptr, uint start_row, uint num_rows, boolean writable));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(void, free_pool, (struct jpeg_common_struct * cinfo, int pool_id));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(void, self_destruct, (struct jpeg_common_struct * cinfo));

  /* Limit on memory allocation for this JPEG object.  (Note that this is
   * merely advisory, not a guaranteed maximum; it only affects the space
   * used for virtual-array buffers.)  May be changed by outer application
   * after creating the JPEG object.
   */
  public int max_memory_to_use;

  /* Maximum allocation request accepted by alloc_large. */
  public int max_alloc_chunk;
}


/* Routine signature for application-supplied marker processing methods.
 * Need not pass marker code since it is stored in cinfo->unread_marker.
 */
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
typedef JMETHOD(boolean, jpeg_marker_parser_method, (struct jpeg_decompress_struct * cinfo));


/* Declarations for routines called by application.
 * The JPP macro hides prototype parameters from compilers that can't cope.
 * Note JPP requires double parentheses.
 */

#if HAVE_PROTOTYPES
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define JPP(arglist) arglist
#define JPP
#else
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define JPP(arglist) ()
#define JPP
#endif


/* Short forms of external names for systems with brain-damaged linkers.
 * We shorten external names to be unique in the first six letters, which
 * is good enough for all known systems.
 * (If your compiler itself needs names to be unique in less than 15 
 * characters, you are out of luck.  Get a better compiler.)
 */

#if NEED_SHORT_EXTERNAL_NAMES
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jpeg_std_error jStdError
#define jpeg_std_error
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jpeg_CreateCompress jCreaCompress
#define jpeg_CreateCompress
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jpeg_CreateDecompress jCreaDecompress
#define jpeg_CreateDecompress
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jpeg_destroy_compress jDestCompress
#define jpeg_destroy_compress
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jpeg_destroy_decompress jDestDecompress
#define jpeg_destroy_decompress
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jpeg_stdio_dest jStdDest
#define jpeg_stdio_dest
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jpeg_stdio_src jStdSrc
#define jpeg_stdio_src
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jpeg_mem_dest jMemDest
#define jpeg_mem_dest
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jpeg_mem_src jMemSrc
#define jpeg_mem_src
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jpeg_set_defaults jSetDefaults
#define jpeg_set_defaults
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jpeg_set_colorspace jSetColorspace
#define jpeg_set_colorspace
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jpeg_default_colorspace jDefColorspace
#define jpeg_default_colorspace
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jpeg_set_quality jSetQuality
#define jpeg_set_quality
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jpeg_set_linear_quality jSetLQuality
#define jpeg_set_linear_quality
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jpeg_default_qtables jDefQTables
#define jpeg_default_qtables
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jpeg_add_quant_table jAddQuantTable
#define jpeg_add_quant_table
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jpeg_quality_scaling jQualityScaling
#define jpeg_quality_scaling
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jpeg_simple_progression jSimProgress
#define jpeg_simple_progression
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jpeg_suppress_tables jSuppressTables
#define jpeg_suppress_tables
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jpeg_alloc_quant_table jAlcQTable
#define jpeg_alloc_quant_table
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jpeg_alloc_huff_table jAlcHTable
#define jpeg_alloc_huff_table
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jpeg_start_compress jStrtCompress
#define jpeg_start_compress
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jpeg_write_scanlines jWrtScanlines
#define jpeg_write_scanlines
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jpeg_finish_compress jFinCompress
#define jpeg_finish_compress
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jpeg_calc_jpeg_dimensions jCjpegDimensions
#define jpeg_calc_jpeg_dimensions
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jpeg_write_raw_data jWrtRawData
#define jpeg_write_raw_data
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jpeg_write_marker jWrtMarker
#define jpeg_write_marker
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jpeg_write_m_header jWrtMHeader
#define jpeg_write_m_header
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jpeg_write_m_byte jWrtMByte
#define jpeg_write_m_byte
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jpeg_write_tables jWrtTables
#define jpeg_write_tables
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jpeg_read_header jReadHeader
#define jpeg_read_header
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jpeg_start_decompress jStrtDecompress
#define jpeg_start_decompress
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jpeg_read_scanlines jReadScanlines
#define jpeg_read_scanlines
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jpeg_finish_decompress jFinDecompress
#define jpeg_finish_decompress
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jpeg_read_raw_data jReadRawData
#define jpeg_read_raw_data
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jpeg_has_multiple_scans jHasMultScn
#define jpeg_has_multiple_scans
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jpeg_start_output jStrtOutput
#define jpeg_start_output
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jpeg_finish_output jFinOutput
#define jpeg_finish_output
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jpeg_input_complete jInComplete
#define jpeg_input_complete
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jpeg_new_colormap jNewCMap
#define jpeg_new_colormap
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jpeg_consume_input jConsumeInput
#define jpeg_consume_input
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jpeg_core_output_dimensions jCoreDimensions
#define jpeg_core_output_dimensions
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jpeg_calc_output_dimensions jCalcDimensions
#define jpeg_calc_output_dimensions
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jpeg_save_markers jSaveMarkers
#define jpeg_save_markers
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jpeg_set_marker_processor jSetMarker
#define jpeg_set_marker_processor
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jpeg_read_coefficients jReadCoefs
#define jpeg_read_coefficients
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jpeg_write_coefficients jWrtCoefs
#define jpeg_write_coefficients
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jpeg_copy_critical_parameters jCopyCrit
#define jpeg_copy_critical_parameters
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jpeg_abort_compress jAbrtCompress
#define jpeg_abort_compress
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jpeg_abort_decompress jAbrtDecompress
#define jpeg_abort_decompress
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jpeg_abort jAbort
#define jpeg_abort
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jpeg_destroy jDestroy
#define jpeg_destroy
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jpeg_resync_to_restart jResyncRestart
#define jpeg_resync_to_restart
#endif // NEED_SHORT_EXTERNAL_NAMES


/* These marker codes are exported since applications and data source modules
 * are likely to want to use them.
 */



/* If we have a brain-damaged compiler that emits warnings (or worse, errors)
 * for structure definitions that are never filled in, keep it quiet by
 * supplying dummy definitions for the various substructures.
 */

#if INCOMPLETE_TYPES_BROKEN
#if ! JPEG_INTERNALS // will be defined in jpegint.h
public class jvirt_sarray_control
{
	public int dummy;
}
public class jvirt_barray_control
{
	public int dummy;
}
public class jpeg_comp_master
{
	public int dummy;
}
public class jpeg_c_main_controller
{
	public int dummy;
}
public class jpeg_c_prep_controller
{
	public int dummy;
}
public class jpeg_c_coef_controller
{
	public int dummy;
}
public class jpeg_marker_writer
{
	public int dummy;
}
public class jpeg_color_converter
{
	public int dummy;
}
public class jpeg_downsampler
{
	public int dummy;
}
public class jpeg_forward_dct
{
	public int dummy;
}
public class jpeg_entropy_encoder
{
	public int dummy;
}
public class jpeg_decomp_master
{
	public int dummy;
}
public class jpeg_d_main_controller
{
	public int dummy;
}
public class jpeg_d_coef_controller
{
	public int dummy;
}
public class jpeg_d_post_controller
{
	public int dummy;
}
public class jpeg_input_controller
{
	public int dummy;
}
public class jpeg_marker_reader
{
	public int dummy;
}
public class jpeg_entropy_decoder
{
	public int dummy;
}
public class jpeg_inverse_dct
{
	public int dummy;
}
public class jpeg_upsampler
{
	public int dummy;
}
public class jpeg_color_deconverter
{
	public int dummy;
}
public class jpeg_color_quantizer
{
	public int dummy;
}
#endif // JPEG_INTERNALS
#endif // INCOMPLETE_TYPES_BROKEN


/*
 * The JPEG library modules define JPEG_INTERNALS before including this file.
 * The internal structure declarations are read only when that is true.
 * Applications using the library should not include jpegint.h, but may wish
 * to include jerror.h.
 */

#if JPEG_INTERNALS
#define CSTATE_START
#define CSTATE_SCANNING
#define CSTATE_RAW_OK
#define CSTATE_WRCOEFS
#define DSTATE_START
#define DSTATE_INHEADER
#define DSTATE_READY
#define DSTATE_PRELOAD
#define DSTATE_PRESCAN
#define DSTATE_SCANNING
#define DSTATE_RAW_OK
#define DSTATE_BUFIMAGE
#define DSTATE_BUFPOST
#define DSTATE_RDCOEFS
#define DSTATE_STOPPING
#define RANGE_BITS
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define RANGE_CENTER (CENTERJSAMPLE << RANGE_BITS)
#define RANGE_CENTER
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MAX
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MIN(a,b) ((a) < (b) ? (a) : (b))
#define MIN
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define SHIFT_TEMPS INT32 shift_temp;
#define SHIFT_TEMPS
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define RIGHT_SHIFT(x,shft) ((shift_temp = (x)) < 0 ? (shift_temp >> (shft)) | ((~((INT32) 0)) << (32-(shft))) : (shift_temp >> (shft)))
#define RIGHT_SHIFT
#define SHIFT_TEMPS
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define RIGHT_SHIFT(x,shft) ((x) >> (shft))
#define RIGHT_SHIFT
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jinit_compress_master jICompress
#define jinit_compress_master
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jinit_c_master_control jICMaster
#define jinit_c_master_control
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jinit_c_main_controller jICMainC
#define jinit_c_main_controller
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jinit_c_prep_controller jICPrepC
#define jinit_c_prep_controller
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jinit_c_coef_controller jICCoefC
#define jinit_c_coef_controller
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jinit_color_converter jICColor
#define jinit_color_converter
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jinit_downsampler jIDownsampler
#define jinit_downsampler
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jinit_forward_dct jIFDCT
#define jinit_forward_dct
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jinit_huff_encoder jIHEncoder
#define jinit_huff_encoder
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jinit_arith_encoder jIAEncoder
#define jinit_arith_encoder
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jinit_marker_writer jIMWriter
#define jinit_marker_writer
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jinit_master_decompress jIDMaster
#define jinit_master_decompress
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jinit_d_main_controller jIDMainC
#define jinit_d_main_controller
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jinit_d_coef_controller jIDCoefC
#define jinit_d_coef_controller
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jinit_d_post_controller jIDPostC
#define jinit_d_post_controller
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jinit_input_controller jIInCtlr
#define jinit_input_controller
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jinit_marker_reader jIMReader
#define jinit_marker_reader
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jinit_huff_decoder jIHDecoder
#define jinit_huff_decoder
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jinit_arith_decoder jIADecoder
#define jinit_arith_decoder
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jinit_inverse_dct jIIDCT
#define jinit_inverse_dct
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jinit_upsampler jIUpsampler
#define jinit_upsampler
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jinit_color_deconverter jIDColor
#define jinit_color_deconverter
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jinit_1pass_quantizer jI1Quant
#define jinit_1pass_quantizer
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jinit_2pass_quantizer jI2Quant
#define jinit_2pass_quantizer
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jinit_merged_upsampler jIMUpsampler
#define jinit_merged_upsampler
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jinit_memory_mgr jIMemMgr
#define jinit_memory_mgr
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jdiv_round_up jDivRound
#define jdiv_round_up
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jround_up jRound
#define jround_up
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jzero_far jZeroFar
#define jzero_far
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jcopy_sample_rows jCopySamples
#define jcopy_sample_rows
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jcopy_block_row jCopyBlocks
#define jcopy_block_row
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jpeg_zigzag_order jZIGTable
#define jpeg_zigzag_order
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jpeg_natural_order jZAGTable
#define jpeg_natural_order
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jpeg_natural_order7 jZAG7Table
#define jpeg_natural_order7
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jpeg_natural_order6 jZAG6Table
#define jpeg_natural_order6
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jpeg_natural_order5 jZAG5Table
#define jpeg_natural_order5
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jpeg_natural_order4 jZAG4Table
#define jpeg_natural_order4
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jpeg_natural_order3 jZAG3Table
#define jpeg_natural_order3
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jpeg_natural_order2 jZAG2Table
#define jpeg_natural_order2
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define jpeg_aritab jAriTab
#define jpeg_aritab
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define FMEMZERO(target,size) MEMZERO(target,size)
#define FMEMZERO
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define FMEMZERO(target,size) _fmemset((void FAR *)(target), 0, (size_t)(size))
#define FMEMZERO
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define FMEMZERO(target,size) jzero_far(target, size)
#define FMEMZERO
#define JMAKE_ENUM_LIST
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define JMESSAGE(code,string)
#define JMESSAGE
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define JMESSAGE(code,string) code ,
#define JMESSAGE
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define ERREXIT(cinfo,code) ((cinfo)->err->msg_code = (code), (*(cinfo)->err->error_exit) ((j_common_ptr) (cinfo)))
#define ERREXIT
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define ERREXIT1(cinfo,code,p1) ((cinfo)->err->msg_code = (code), (cinfo)->err->msg_parm.i[0] = (p1), (*(cinfo)->err->error_exit) ((j_common_ptr) (cinfo)))
#define ERREXIT1
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define ERREXIT2(cinfo,code,p1,p2) ((cinfo)->err->msg_code = (code), (cinfo)->err->msg_parm.i[0] = (p1), (cinfo)->err->msg_parm.i[1] = (p2), (*(cinfo)->err->error_exit) ((j_common_ptr) (cinfo)))
#define ERREXIT2
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define ERREXIT3(cinfo,code,p1,p2,p3) ((cinfo)->err->msg_code = (code), (cinfo)->err->msg_parm.i[0] = (p1), (cinfo)->err->msg_parm.i[1] = (p2), (cinfo)->err->msg_parm.i[2] = (p3), (*(cinfo)->err->error_exit) ((j_common_ptr) (cinfo)))
#define ERREXIT3
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define ERREXIT4(cinfo,code,p1,p2,p3,p4) ((cinfo)->err->msg_code = (code), (cinfo)->err->msg_parm.i[0] = (p1), (cinfo)->err->msg_parm.i[1] = (p2), (cinfo)->err->msg_parm.i[2] = (p3), (cinfo)->err->msg_parm.i[3] = (p4), (*(cinfo)->err->error_exit) ((j_common_ptr) (cinfo)))
#define ERREXIT4
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define ERREXIT6(cinfo,code,p1,p2,p3,p4,p5,p6) ((cinfo)->err->msg_code = (code), (cinfo)->err->msg_parm.i[0] = (p1), (cinfo)->err->msg_parm.i[1] = (p2), (cinfo)->err->msg_parm.i[2] = (p3), (cinfo)->err->msg_parm.i[3] = (p4), (cinfo)->err->msg_parm.i[4] = (p5), (cinfo)->err->msg_parm.i[5] = (p6), (*(cinfo)->err->error_exit) ((j_common_ptr) (cinfo)))
#define ERREXIT6
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define ERREXITS(cinfo,code,str) ((cinfo)->err->msg_code = (code), strncpy((cinfo)->err->msg_parm.s, (str), JMSG_STR_PARM_MAX), (*(cinfo)->err->error_exit) ((j_common_ptr) (cinfo)))
#define ERREXITS
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MAKESTMT(stuff) do { stuff } while (0)
#define MAKESTMT
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define WARNMS(cinfo,code) ((cinfo)->err->msg_code = (code), (*(cinfo)->err->emit_message) ((j_common_ptr) (cinfo), -1))
#define WARNMS
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define WARNMS1(cinfo,code,p1) ((cinfo)->err->msg_code = (code), (cinfo)->err->msg_parm.i[0] = (p1), (*(cinfo)->err->emit_message) ((j_common_ptr) (cinfo), -1))
#define WARNMS1
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define WARNMS2(cinfo,code,p1,p2) ((cinfo)->err->msg_code = (code), (cinfo)->err->msg_parm.i[0] = (p1), (cinfo)->err->msg_parm.i[1] = (p2), (*(cinfo)->err->emit_message) ((j_common_ptr) (cinfo), -1))
#define WARNMS2
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define TRACEMS(cinfo,lvl,code) ((cinfo)->err->msg_code = (code), (*(cinfo)->err->emit_message) ((j_common_ptr) (cinfo), (lvl)))
#define TRACEMS
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define TRACEMS1(cinfo,lvl,code,p1) ((cinfo)->err->msg_code = (code), (cinfo)->err->msg_parm.i[0] = (p1), (*(cinfo)->err->emit_message) ((j_common_ptr) (cinfo), (lvl)))
#define TRACEMS1
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define TRACEMS2(cinfo,lvl,code,p1,p2) ((cinfo)->err->msg_code = (code), (cinfo)->err->msg_parm.i[0] = (p1), (cinfo)->err->msg_parm.i[1] = (p2), (*(cinfo)->err->emit_message) ((j_common_ptr) (cinfo), (lvl)))
#define TRACEMS2
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define TRACEMS3(cinfo,lvl,code,p1,p2,p3) MAKESTMT(int * _mp = (cinfo)->err->msg_parm.i; _mp[0] = (p1); _mp[1] = (p2); _mp[2] = (p3); (cinfo)->err->msg_code = (code); (*(cinfo)->err->emit_message) ((j_common_ptr) (cinfo), (lvl)); )
#define TRACEMS3
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define TRACEMS4(cinfo,lvl,code,p1,p2,p3,p4) MAKESTMT(int * _mp = (cinfo)->err->msg_parm.i; _mp[0] = (p1); _mp[1] = (p2); _mp[2] = (p3); _mp[3] = (p4); (cinfo)->err->msg_code = (code); (*(cinfo)->err->emit_message) ((j_common_ptr) (cinfo), (lvl)); )
#define TRACEMS4
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define TRACEMS5(cinfo,lvl,code,p1,p2,p3,p4,p5) MAKESTMT(int * _mp = (cinfo)->err->msg_parm.i; _mp[0] = (p1); _mp[1] = (p2); _mp[2] = (p3); _mp[3] = (p4); _mp[4] = (p5); (cinfo)->err->msg_code = (code); (*(cinfo)->err->emit_message) ((j_common_ptr) (cinfo), (lvl)); )
#define TRACEMS5
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define TRACEMS8(cinfo,lvl,code,p1,p2,p3,p4,p5,p6,p7,p8) MAKESTMT(int * _mp = (cinfo)->err->msg_parm.i; _mp[0] = (p1); _mp[1] = (p2); _mp[2] = (p3); _mp[3] = (p4); _mp[4] = (p5); _mp[5] = (p6); _mp[6] = (p7); _mp[7] = (p8); (cinfo)->err->msg_code = (code); (*(cinfo)->err->emit_message) ((j_common_ptr) (cinfo), (lvl)); )
#define TRACEMS8
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define TRACEMSS(cinfo,lvl,code,str) ((cinfo)->err->msg_code = (code), strncpy((cinfo)->err->msg_parm.s, (str), JMSG_STR_PARM_MAX), (*(cinfo)->err->emit_message) ((j_common_ptr) (cinfo), (lvl)))
#define TRACEMSS
#endif

#if __cplusplus
#if ! DONT_USE_EXTERN_C
#endif
#endif

