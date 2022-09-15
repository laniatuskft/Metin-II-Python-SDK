/*
 * jpegint.h
 *
 * Copyright (C) 1991-1997, Thomas G. Lane.
 * Modified 1997-2017 by Guido Vollbeding.
 * This file is part of the Independent JPEG Group's software.
 * For conditions of distribution and use, see the accompanying README file.
 *
 * This file provides common declarations for the various JPEG modules.
 * These declarations are considered internal to the JPEG library; most
 * applications using the library shouldn't need to include this file.
 */


/* Declarations for both compression & decompression */

public enum J_BUF_MODE
{ // Operating modes for buffer controllers
	JBUF_PASS_THRU, // Plain stripwise operation
	/* Remaining modes require a full-image buffer to have been created */
	JBUF_SAVE_SOURCE, // Run source subobject only, save output
	JBUF_CRANK_DEST, // Run dest subobject only, using saved data
	JBUF_SAVE_AND_PASS // Run both subobjects, save output
}

/* Values of global_state field (jdapi.c has some dependencies on ordering!) */


/* Declarations for compression modules */

/* Master control module */
public class jpeg_comp_master
{
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(void, prepare_for_pass, (j_compress_ptr cinfo));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(void, pass_startup, (j_compress_ptr cinfo));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(void, finish_pass, (j_compress_ptr cinfo));

  /* State variables made visible to other modules */
  public boolean call_pass_startup = new boolean(); // True if pass_startup must be called
  public boolean is_last_pass = new boolean(); // True during last pass
}

/* Main buffer control (downsampled-data buffer) */
public class jpeg_c_main_controller
{
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(void, start_pass, (j_compress_ptr cinfo, J_BUF_MODE pass_mode));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(void, process_data, (j_compress_ptr cinfo, JSAMPARRAY input_buf, JDIMENSION * in_row_ctr, JDIMENSION in_rows_avail));
}

/* Compression preprocessing (downsampling input buffer control) */
public class jpeg_c_prep_controller
{
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(void, start_pass, (j_compress_ptr cinfo, J_BUF_MODE pass_mode));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(void, pre_process_data, (j_compress_ptr cinfo, JSAMPARRAY input_buf, JDIMENSION * in_row_ctr, JDIMENSION in_rows_avail, JSAMPIMAGE output_buf, JDIMENSION * out_row_group_ctr, JDIMENSION out_row_groups_avail));
}

/* Coefficient buffer control */
public class jpeg_c_coef_controller
{
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(void, start_pass, (j_compress_ptr cinfo, J_BUF_MODE pass_mode));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(boolean, compress_data, (j_compress_ptr cinfo, JSAMPIMAGE input_buf));
}

/* Colorspace conversion */
public class jpeg_color_converter
{
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(void, start_pass, (j_compress_ptr cinfo));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(void, color_convert, (j_compress_ptr cinfo, JSAMPARRAY input_buf, JSAMPIMAGE output_buf, JDIMENSION output_row, int num_rows));
}

/* Downsampling */
public class jpeg_downsampler
{
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(void, start_pass, (j_compress_ptr cinfo));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(void, downsample, (j_compress_ptr cinfo, JSAMPIMAGE input_buf, JDIMENSION in_row_index, JSAMPIMAGE output_buf, JDIMENSION out_row_group_index));

  public boolean need_context_rows = new boolean(); // TRUE if need rows above & below
}

/* Forward DCT (also controls coefficient quantization) */
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
typedef JMETHOD(void, forward_DCT_ptr, (j_compress_ptr cinfo, jpeg_component_info * compptr, JSAMPARRAY sample_data, JBLOCKROW coef_blocks, JDIMENSION start_row, JDIMENSION start_col, JDIMENSION num_blocks));

public class jpeg_forward_dct
{
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(void, start_pass, (j_compress_ptr cinfo));
  /* It is useful to allow each component to have a separate FDCT method. */
  public forward_DCT_ptr[] forward_DCT = Arrays.InitializeWithDefaultInstances<forward_DCT_ptr>(MAX_COMPONENTS);
}

/* Entropy encoding */
public class jpeg_entropy_encoder
{
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(void, start_pass, (j_compress_ptr cinfo, boolean gather_statistics));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(boolean, encode_mcu, (j_compress_ptr cinfo, JBLOCKROW * MCU_data));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(void, finish_pass, (j_compress_ptr cinfo));
}

/* Marker writing */
public class jpeg_marker_writer
{
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(void, write_file_header, (j_compress_ptr cinfo));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(void, write_frame_header, (j_compress_ptr cinfo));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(void, write_scan_header, (j_compress_ptr cinfo));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(void, write_file_trailer, (j_compress_ptr cinfo));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(void, write_tables_only, (j_compress_ptr cinfo));
  /* These routines are exported to allow insertion of extra markers */
  /* Probably only COM and APPn markers should be written this way */
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(void, write_marker_header, (j_compress_ptr cinfo, int marker, uint datalen));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(void, write_marker_byte, (j_compress_ptr cinfo, int val));
}


/* Declarations for decompression modules */

/* Master control module */
public class jpeg_decomp_master
{
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(void, prepare_for_output_pass, (j_decompress_ptr cinfo));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(void, finish_output_pass, (j_decompress_ptr cinfo));

  /* State variables made visible to other modules */
  public boolean is_dummy_pass = new boolean(); // True during 1st pass for 2-pass quant
}

/* Input control module */
public class jpeg_input_controller
{
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(int, consume_input, (j_decompress_ptr cinfo));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(void, reset_input_controller, (j_decompress_ptr cinfo));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(void, start_input_pass, (j_decompress_ptr cinfo));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(void, finish_input_pass, (j_decompress_ptr cinfo));

  /* State variables made visible to other modules */
  public boolean has_multiple_scans = new boolean(); // True if file has multiple scans
  public boolean eoi_reached = new boolean(); // True when EOI has been consumed
}

/* Main buffer control (downsampled-data buffer) */
public class jpeg_d_main_controller
{
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(void, start_pass, (j_decompress_ptr cinfo, J_BUF_MODE pass_mode));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(void, process_data, (j_decompress_ptr cinfo, JSAMPARRAY output_buf, JDIMENSION * out_row_ctr, JDIMENSION out_rows_avail));
}

/* Coefficient buffer control */
public class jpeg_d_coef_controller
{
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(void, start_input_pass, (j_decompress_ptr cinfo));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(int, consume_data, (j_decompress_ptr cinfo));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(void, start_output_pass, (j_decompress_ptr cinfo));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(int, decompress_data, (j_decompress_ptr cinfo, JSAMPIMAGE output_buf));
  /* Pointer to array of coefficient virtual arrays, or NULL if none */
  public jvirt_barray_ptr coef_arrays;
}

/* Decompression postprocessing (color quantization buffer control) */
public class jpeg_d_post_controller
{
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(void, start_pass, (j_decompress_ptr cinfo, J_BUF_MODE pass_mode));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(void, post_process_data, (j_decompress_ptr cinfo, JSAMPIMAGE input_buf, JDIMENSION * in_row_group_ctr, JDIMENSION in_row_groups_avail, JSAMPARRAY output_buf, JDIMENSION * out_row_ctr, JDIMENSION out_rows_avail));
}

/* Marker reading & parsing */
public class jpeg_marker_reader
{
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(void, reset_marker_reader, (j_decompress_ptr cinfo));
  /* Read markers until SOS or EOI.
   * Returns same codes as are defined for jpeg_consume_input:
   * JPEG_SUSPENDED, JPEG_REACHED_SOS, or JPEG_REACHED_EOI.
   */
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(int, read_markers, (j_decompress_ptr cinfo));
  /* Read a restart marker --- exported for use by entropy decoder only */
  public jpeg_marker_parser_method read_restart_marker = new jpeg_marker_parser_method();

  /* State of marker reader --- nominally internal, but applications
   * supplying COM or APPn handlers might like to know the state.
   */
  public boolean saw_SOI = new boolean(); // found SOI?
  public boolean saw_SOF = new boolean(); // found SOF?
  public int next_restart_num; // next restart number expected (0-7)
  public uint discarded_bytes; // # of bytes skipped looking for a marker
}

/* Entropy decoding */
public class jpeg_entropy_decoder
{
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(void, start_pass, (j_decompress_ptr cinfo));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(boolean, decode_mcu, (j_decompress_ptr cinfo, JBLOCKROW * MCU_data));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(void, finish_pass, (j_decompress_ptr cinfo));
}

/* Inverse DCT (also performs dequantization) */
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
typedef JMETHOD(void, inverse_DCT_method_ptr, (j_decompress_ptr cinfo, jpeg_component_info * compptr, JCOEFPTR coef_block, JSAMPARRAY output_buf, JDIMENSION output_col));

public class jpeg_inverse_dct
{
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(void, start_pass, (j_decompress_ptr cinfo));
  /* It is useful to allow each component to have a separate IDCT method. */
  public inverse_DCT_method_ptr[] inverse_DCT = Arrays.InitializeWithDefaultInstances<inverse_DCT_method_ptr>(MAX_COMPONENTS);
}

/* Upsampling (note that upsampler must also call color converter) */
public class jpeg_upsampler
{
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(void, start_pass, (j_decompress_ptr cinfo));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(void, upsample, (j_decompress_ptr cinfo, JSAMPIMAGE input_buf, JDIMENSION * in_row_group_ctr, JDIMENSION in_row_groups_avail, JSAMPARRAY output_buf, JDIMENSION * out_row_ctr, JDIMENSION out_rows_avail));

  public boolean need_context_rows = new boolean(); // TRUE if need rows above & below
}

/* Colorspace conversion */
public class jpeg_color_deconverter
{
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(void, start_pass, (j_decompress_ptr cinfo));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(void, color_convert, (j_decompress_ptr cinfo, JSAMPIMAGE input_buf, JDIMENSION input_row, JSAMPARRAY output_buf, int num_rows));
}

/* Color quantization or color precision reduction */
public class jpeg_color_quantizer
{
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(void, start_pass, (j_decompress_ptr cinfo, boolean is_pre_scan));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(void, color_quantize, (j_decompress_ptr cinfo, JSAMPARRAY input_buf, JSAMPARRAY output_buf, int num_rows));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(void, finish_pass, (j_decompress_ptr cinfo));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
  JMETHOD(void, new_color_map, (j_decompress_ptr cinfo));
}


/* Definition of range extension bits for decompression processes.
 * See the comments with prepare_range_limit_table (in jdmaster.c)
 * for more info.
 * The recommended default value for normal applications is 2.
 * Applications with special requirements may use a different value.
 * For example, Ghostscript wants to use 3 for proper handling of
 * wacky images with oversize coefficient values.
 */

//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define RANGE_CENTER (CENTERJSAMPLE << RANGE_BITS)


/* Miscellaneous useful macros */

//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MAX(a,b) ((a) > (b) ? (a) : (b))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MIN(a,b) ((a) < (b) ? (a) : (b))


/* We assume that right shift corresponds to signed division by 2 with
 * rounding towards minus infinity.  This is correct for typical "arithmetic
 * shift" instructions that shift in copies of the sign bit.  But some
 * C compilers implement >> with an unsigned shift.  For these machines you
 * must define RIGHT_SHIFT_IS_UNSIGNED.
 * RIGHT_SHIFT provides a proper signed right shift of an INT32 quantity.
 * It is only applied with constant shift counts.  SHIFT_TEMPS must be
 * included in the variables of any routine using RIGHT_SHIFT.
 */

#if RIGHT_SHIFT_IS_UNSIGNED
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define SHIFT_TEMPS INT32 shift_temp;
#define SHIFT_TEMPS
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define RIGHT_SHIFT(x,shft) ((shift_temp = (x)) < 0 ? (shift_temp >> (shft)) | ((~((INT32) 0)) << (32-(shft))) : (shift_temp >> (shft)))
#define RIGHT_SHIFT
#else
#define SHIFT_TEMPS
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define RIGHT_SHIFT(x,shft) ((x) >> (shft))
#define RIGHT_SHIFT
#endif


/* Short forms of external names for systems with brain-damaged linkers. */

#if NEED_SHORT_EXTERNAL_NAMES
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
#endif // NEED_SHORT_EXTERNAL_NAMES


/* On normal machines we can apply MEMCOPY() and MEMZERO() to sample arrays
 * and coefficient-block arrays.  This won't work on 80x86 because the arrays
 * are FAR and we're assuming a small-pointer memory model.  However, some
 * DOS compilers provide far-pointer versions of memcpy() and memset() even
 * in the small-model libraries.  These will be used if USE_FMEM is defined.
 * Otherwise, the routines in jutils.c do it the hard way.
 */

#if ! NEED_FAR_POINTERS // normal case, same as regular macro
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define FMEMZERO(target,size) MEMZERO(target,size)
#define FMEMZERO
#else // 80x86 case
#if USE_FMEM
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define FMEMZERO(target,size) _fmemset((void FAR *)(target), 0, (size_t)(size))
#define FMEMZERO
#else
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
EXTERN() jZeroFar JPP((void FAR * target, size_t bytestozero));
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define FMEMZERO(target,size) jzero_far(target, size)
#define FMEMZERO
#endif
#endif


/* Compression module initialization routines */
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
EXTERN() jICompress JPP((j_compress_ptr cinfo));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
EXTERN() jICMaster JPP((j_compress_ptr cinfo, boolean transcode_only));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
EXTERN() jICMainC JPP((j_compress_ptr cinfo, boolean need_full_buffer));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
EXTERN() jICPrepC JPP((j_compress_ptr cinfo, boolean need_full_buffer));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
EXTERN() jICCoefC JPP((j_compress_ptr cinfo, boolean need_full_buffer));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
EXTERN() jICColor JPP((j_compress_ptr cinfo));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
EXTERN() jIDownsampler JPP((j_compress_ptr cinfo));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
EXTERN() jIFDCT JPP((j_compress_ptr cinfo));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
EXTERN() jIHEncoder JPP((j_compress_ptr cinfo));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
EXTERN() jIAEncoder JPP((j_compress_ptr cinfo));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
EXTERN() jIMWriter JPP((j_compress_ptr cinfo));
/* Decompression module initialization routines */
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
EXTERN() jIDMaster JPP((j_decompress_ptr cinfo));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
EXTERN() jIDMainC JPP((j_decompress_ptr cinfo, boolean need_full_buffer));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
EXTERN() jIDCoefC JPP((j_decompress_ptr cinfo, boolean need_full_buffer));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
EXTERN() jIDPostC JPP((j_decompress_ptr cinfo, boolean need_full_buffer));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
EXTERN() jIInCtlr JPP((j_decompress_ptr cinfo));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
EXTERN() jIMReader JPP((j_decompress_ptr cinfo));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
EXTERN() jIHDecoder JPP((j_decompress_ptr cinfo));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
EXTERN() jIADecoder JPP((j_decompress_ptr cinfo));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
EXTERN() jIIDCT JPP((j_decompress_ptr cinfo));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
EXTERN() jIUpsampler JPP((j_decompress_ptr cinfo));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
EXTERN() jIDColor JPP((j_decompress_ptr cinfo));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
EXTERN() jI1Quant JPP((j_decompress_ptr cinfo));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
EXTERN() jI2Quant JPP((j_decompress_ptr cinfo));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
EXTERN() jIMUpsampler JPP((j_decompress_ptr cinfo));
/* Memory manager initialization */
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
EXTERN() jIMemMgr JPP((j_common_ptr cinfo));

/* Utility routines in jutils.c */
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
EXTERN(int) jDivRound JPP((int a, int b));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
EXTERN(int) jRound JPP((int a, int b));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
EXTERN() jCopySamples JPP((JSAMPARRAY input_array, int source_row, JSAMPARRAY output_array, int dest_row, int num_rows, JDIMENSION num_cols));
//# Laniatus Games Studio Inc. | TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
EXTERN() jCopyBlocks JPP((JBLOCKROW input_row, JBLOCKROW output_row, JDIMENSION num_blocks));
/* Constant tables in jutils.c */
#if false // This table is not actually needed in v6a
//extern const int jpeg_zigzag_order[]; // natural coef order to zigzag order 
#endif

/* Suppress undefined-structure complaints if necessary. */

#if INCOMPLETE_TYPES_BROKEN
#if ! AM_MEMORY_MANAGER // only jmemmgr.c defines these
public class jvirt_sarray_control
{
	public int dummy;
}
public class jvirt_barray_control
{
	public int dummy;
}
#endif
#endif // INCOMPLETE_TYPES_BROKEN
