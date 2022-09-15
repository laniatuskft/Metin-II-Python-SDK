/* jconfig.vc --- jconfig.h for Microsoft Visual C++ on Windows 9x or NT. */
/* This file also works for Borland C++ 32-bit (bcc32) on Windows 9x or NT. */
/* see jconfig.txt for explanations */

/* #define void char */
/* #define const */

/* Define "boolean" as unsigned char, not enum, per Windows custom */
#if ! __RPCNDR_H__ // don't conflict if rpcndr.h already read
//# Laniatus Games Studio Inc. | TODO TASK: Typedefs defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//typedef byte boolean;
#endif


#if JPEG_INTERNALS

#undef RIGHT_SHIFT_IS_UNSIGNED

#endif // JPEG_INTERNALS

#if JPEG_CJPEG_DJPEG

#define BMP_SUPPORTED // BMP image file format
#define GIF_SUPPORTED // GIF image file format
#define PPM_SUPPORTED // PBMPLUS PPM/PGM image file format
#undef RLE_SUPPORTED // Utah RLE image file format
#define TARGA_SUPPORTED // Targa image file format

#define TWO_FILE_COMMANDLINE // optional
#define USE_SETMODE // Microsoft has setmode()
#undef NEED_SIGNAL_CATCHER
#undef DONT_USE_B_MODE
#undef PROGRESS_REPORT // optional

#endif // JPEG_CJPEG_DJPEG
