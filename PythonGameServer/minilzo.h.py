## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if __LZOCONF_H_INCLUDED
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##error "you cannot use both LZO and miniLZO"
##endif

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if MINILZO_HAVE_CONFIG_H
##endif

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if ! __LZODEFS_H_INCLUDED
## Laniatus Games Studio Inc. | WARNING: The following #include directive was ignored:
#    #include "lzo/lzodefs.h"
##endif
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##undef LZO_HAVE_CONFIG_H
## Laniatus Games Studio Inc. | WARNING: The following #include directive was ignored:
##include "lzo/lzoconf.h"

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if !LZO_VERSION || (LZO_VERSION != MINILZO_VERSION)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
    ##error "version mismatch in header files"
##endif


## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if __cplusplus
##endif

## Laniatus Games Studio Inc. | NOTE: The following #define macro was replaced in-line:
#ORIGINAL METINII C CODE: #define LZO1X_MEM_COMPRESS LZO1X_1_MEM_COMPRESS
## Laniatus Games Studio Inc. | NOTE: The following #define macro was replaced in-line:
#ORIGINAL METINII C CODE: #define LZO1X_1_MEM_COMPRESS ((lzo_uint32_t) (16384L * lzo_sizeof_dict_t))

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following statement was not recognized, possibly due to an unrecognized macro:
LZO_EXTERN(int) lzo1x_1_compress(const lzo_bytep src, lzo_uint src_len, lzo_bytep dst, lzo_uintp dst_len, lzo_voidp wrkmem)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following statement was not recognized, possibly due to an unrecognized macro:
LZO_EXTERN(int) lzo1x_decompress(const lzo_bytep src, lzo_uint src_len, lzo_bytep dst, lzo_uintp dst_len, lzo_voidp wrkmem)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following statement was not recognized, possibly due to an unrecognized macro:
LZO_EXTERN(int) lzo1x_decompress_safe(const lzo_bytep src, lzo_uint src_len, lzo_bytep dst, lzo_uintp dst_len, lzo_voidp wrkmem)


## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if __cplusplus
##endif

