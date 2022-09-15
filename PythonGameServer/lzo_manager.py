class LZOManager(singleton):
    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self._m_workmem = None

        if lzo_init() != LZO_E_OK:
            fprintf(stderr, "lzo_init() failed\n")
            abort()

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'malloc' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
        self._m_workmem = byte(int(malloc(((16384 * lzo_sizeof_dict_t)))))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
        memset(self._m_workmem, 0, ((16384 * lzo_sizeof_dict_t)))

    def close(self):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'free' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
        free(self._m_workmem)
        self._m_workmem = None

    def Compress(self, src, srcsize, dest, puiDestSize):
        ret = lzo1x_1_compress(src, srcsize, dest.arg_value, puiDestSize, self.GetWorkMemory())

        if ret != LZO_E_OK:
            return DefineConstants.false

        return ((not DefineConstants.false))

    def Decompress(self, src, srcsize, dest, puiDestSize):
        ret = lzo1x_decompress_safe(src, srcsize, dest.arg_value, puiDestSize, self.GetWorkMemory())

        if ret != LZO_E_OK:
            return DefineConstants.false

        return ((not DefineConstants.false))

    def GetMaxCompressedSize(self, original):
        return (original + (original >> 4) + 64 + 3)

## Laniatus Games Studio Inc. | WARNING: Python has no equivalent to methods returning pointers to value types:
#ORIGINAL METINII C CODE: byte* GetWorkMemory()
    def GetWorkMemory(self):
        return self._m_workmem
