import math

## Laniatus Games Studio Inc. | WARNING: The following #include directive was ignored:
##include <devil/il.h>


class SGuildMark:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.m_apxBuf = [0 for _ in range(SIZE)]

    WIDTH = 16
    HEIGHT = 12
    SIZE = WIDTH * HEIGHT

    def Clear(self):
        for iPixel in range(0, SIZE):
            self.m_apxBuf[iPixel] = 0xff000000

    def IsEmpty(self):
        for iPixel in range(0, SIZE):
            if self.m_apxBuf[iPixel] != 0x00000000:
                return DefineConstants.false

        return ((not DefineConstants.false))

class SGuildMarkBlock:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.m_apxBuf = [0 for _ in range(SIZE)]
        self.m_abCompBuf = [0 for _ in range(MAX_COMP_SIZE)]
        self.m_sizeCompBuf = lzo_uint()
        self.m_crc = 0

    MARK_PER_BLOCK_WIDTH = 4
    MARK_PER_BLOCK_HEIGHT = 4
    WIDTH = SGuildMark.WIDTH * MARK_PER_BLOCK_WIDTH
    HEIGHT = SGuildMark.HEIGHT * MARK_PER_BLOCK_HEIGHT
    SIZE = WIDTH * HEIGHT
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    MAX_COMP_SIZE = (SIZE * sizeof(uint)) + ((SIZE * sizeof(uint)) >> 4) + 64 + 3

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: uint GetCRC() const
    def GetCRC(self):
        return self.m_crc

    def CopyFrom(self, pbCompBuf, dwCompSize, crc):
        if dwCompSize > MAX_COMP_SIZE:
            return

        self.m_sizeCompBuf = dwCompSize
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memcpy' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
        memcpy(self.m_abCompBuf, pbCompBuf, dwCompSize)
        self.m_crc = crc

    def Compress(self, pxBuf):
        self.m_sizeCompBuf = MAX_COMP_SIZE

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        if LZO_E_OK != lzo1x_1_compress(int(pxBuf), sizeof(uint) * SGuildMarkBlock.SIZE, self.m_abCompBuf, self.m_sizeCompBuf, LZOManager.Instance().GetWorkMemory()):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            #lani_err("SGuildMarkBlock::Compress: Error! %u > %u", sizeof(uint) * SGuildMarkBlock.SIZE, self.m_sizeCompBuf)
            return

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.m_crc = GetCRC32(str(pxBuf), sizeof(uint) * SGuildMarkBlock.SIZE)

class CGuildMarkImage:
    WIDTH = 512
    HEIGHT = 512
    BLOCK_ROW_COUNT = HEIGHT / SGuildMarkBlock.HEIGHT
    BLOCK_COL_COUNT = WIDTH / SGuildMarkBlock.WIDTH
    BLOCK_TOTAL_COUNT = BLOCK_ROW_COUNT * BLOCK_COL_COUNT
    MARK_ROW_COUNT = BLOCK_ROW_COUNT * SGuildMarkBlock.MARK_PER_BLOCK_HEIGHT
    MARK_COL_COUNT = BLOCK_COL_COUNT * SGuildMarkBlock.MARK_PER_BLOCK_WIDTH
    MARK_TOTAL_COUNT = MARK_ROW_COUNT * MARK_COL_COUNT
    INVALID_MARK_POSITION = 0xffffffff

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self._m_aakBlock = [[] for _ in range(BLOCK_ROW_COUNT)]
        self._m_uImg = ILuint()

        self._m_uImg = _INVALID_HANDLE
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
        memset(m_apxImage, 0, self._sizeof(m_apxImage))

    def close(self):
        self.Destroy()

    def Create(self):
        if _INVALID_HANDLE != self._m_uImg:
            return

        ilGenImages(1, self._m_uImg)

    def Destroy(self):
        if _INVALID_HANDLE == self._m_uImg:
            return

        ilDeleteImages(1, self._m_uImg)
        self._m_uImg = _INVALID_HANDLE

    def Build(self, c_szFileName):
        #sys_log(0, "GuildMarkImage: creating new file %s", c_szFileName)

        self.Destroy()
        self.Create()

        ilBindImage(self._m_uImg)
        ilEnable(IL_ORIGIN_SET)
        ilOriginFunc(IL_ORIGIN_UPPER_LEFT)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to pointers to value types:
#ORIGINAL METINII C CODE: byte * data = (byte *) malloc(sizeof(uint) * WIDTH * HEIGHT);
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'malloc' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
        data = byte(int(malloc(self._sizeof(uint) * WIDTH * HEIGHT)))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
        memset(data, 0, self._sizeof(uint) * WIDTH * HEIGHT)

        if not ilTexImage(WIDTH, HEIGHT, 1, 4, IL_BGRA, IL_UNSIGNED_BYTE, data):
            #lani_err("GuildMarkImage: cannot initialize image")
            return DefineConstants.false

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'free' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
        free(data)

        ilEnable(IL_FILE_OVERWRITE)

        if not ilSave(IL_TGA, c_szFileName):
            return DefineConstants.false

        return ((not DefineConstants.false))

    def Save(self, c_szFileName):
        ilEnable(IL_FILE_OVERWRITE)
        ilBindImage(self._m_uImg)

        if not ilSave(IL_TGA, c_szFileName):
            return DefineConstants.false

        return ((not DefineConstants.false))

    def Load(self, c_szFileName):
        self.Destroy()
        self.Create()

        ilBindImage(self._m_uImg)
        ilEnable(IL_ORIGIN_SET)
        ilOriginFunc(IL_ORIGIN_UPPER_LEFT)

        if not ilLoad(IL_TYPE_UNKNOWN, c_szFileName):
            #lani_err("GuildMarkImage: %s cannot open file.", c_szFileName)
            return DefineConstants.false

        if ilGetInteger(IL_IMAGE_WIDTH) != WIDTH:
            #lani_err("GuildMarkImage: %s width must be %u", c_szFileName, WIDTH)
            return DefineConstants.false

        if ilGetInteger(IL_IMAGE_HEIGHT) != HEIGHT:
            #lani_err("GuildMarkImage: %s height must be %u", c_szFileName, HEIGHT)
            return DefineConstants.false

        ilConvertImage(IL_BGRA, IL_UNSIGNED_BYTE)

        self._BuildAllBlocks()
        return ((not DefineConstants.false))

    def PutData(self, x, y, width, height, data):
        ilBindImage(self._m_uImg)
        ilSetPixels(x, y, 0, width, height, 1, IL_BGRA, IL_UNSIGNED_BYTE, data)

    def GetData(self, x, y, width, height, data):
        ilBindImage(self._m_uImg)
        ilCopyPixels(x, y, 0, width, height, 1, IL_BGRA, IL_UNSIGNED_BYTE, data)

    def SaveMark(self, posMark, pbImage):
        if posMark >= MARK_TOTAL_COUNT:
            #lani_err("GuildMarkImage::CopyMarkFromData: Invalid mark position %u", posMark)
            return DefineConstants.false

        colMark = math.fmod(posMark, MARK_COL_COUNT)
        rowMark = math.trunc(posMark / float(MARK_COL_COUNT))

        printf("PutMark pos %u %ux%u\n", posMark, colMark * SGuildMark.WIDTH, rowMark * SGuildMark.HEIGHT)
        self.PutData(colMark * SGuildMark.WIDTH, rowMark * SGuildMark.HEIGHT, uint(SGuildMark.WIDTH), uint(SGuildMark.HEIGHT), pbImage.arg_value)

        rowBlock = math.trunc(rowMark / float(SGuildMarkBlock.MARK_PER_BLOCK_HEIGHT))
        colBlock = math.trunc(colMark / float(SGuildMarkBlock.MARK_PER_BLOCK_WIDTH))

        apxBuf = [0 for _ in range(SGuildMarkBlock.SIZE)]
        self.GetData(colBlock * SGuildMarkBlock.WIDTH, rowBlock * SGuildMarkBlock.HEIGHT, uint(SGuildMarkBlock.WIDTH), uint(SGuildMarkBlock.HEIGHT), apxBuf)
        self._m_aakBlock[rowBlock][colBlock].Compress(apxBuf)
        return ((not DefineConstants.false))

    def DeleteMark(self, posMark):
        image = [0 for _ in range(SGuildMark.SIZE)]
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
        memset(image, 0, self._sizeof(image))
        return self.SaveMark(posMark, byte(int(image)))

    def SaveBlockFromCompressedData(self, posBlock, pbComp, dwCompSize):
        if posBlock >= BLOCK_TOTAL_COUNT:
            return DefineConstants.false

        apxBuf = [0 for _ in range(SGuildMarkBlock.SIZE)]
        sizeBuf = self._sizeof(apxBuf)

        if LZO_E_OK != lzo1x_decompress_safe(pbComp, dwCompSize, int(apxBuf), sizeBuf, LZOManager.Instance().GetWorkMemory()):
            #lani_err("GuildMarkImage::CopyBlockFromCompressedData: cannot decompress, compressed size = %u", dwCompSize)
            return DefineConstants.false

        if sizeBuf is not self._sizeof(apxBuf):
            #lani_err("GuildMarkImage::CopyBlockFromCompressedData: image corrupted, decompressed size = %u", sizeBuf)
            return DefineConstants.false

        rowBlock = math.trunc(posBlock / float(BLOCK_COL_COUNT))
        colBlock = math.fmod(posBlock, BLOCK_COL_COUNT)

        self.PutData(colBlock * SGuildMarkBlock.WIDTH, rowBlock * SGuildMarkBlock.HEIGHT, uint(SGuildMarkBlock.WIDTH), uint(SGuildMarkBlock.HEIGHT), apxBuf)

        self._m_aakBlock[rowBlock][colBlock].CopyFrom(pbComp, dwCompSize, GetCRC32(str(apxBuf), self._sizeof(uint) * SGuildMarkBlock.SIZE))
        return ((not DefineConstants.false))

    def GetEmptyPosition(self):
        kMark = SGuildMark()

        for row in range(0, MARK_ROW_COUNT):
            for col in range(0, MARK_COL_COUNT):
                self.GetData(col * SGuildMark.WIDTH, row * SGuildMark.HEIGHT, uint(SGuildMark.WIDTH), uint(SGuildMark.HEIGHT), kMark.m_apxBuf)

                if kMark.IsEmpty():
                    return (row * MARK_COL_COUNT + col)

        return uint(INVALID_MARK_POSITION)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Pointer arithmetic is detected on the parameter 'crcList':
#ORIGINAL METINII C CODE: void GetBlockCRCList(uint * crcList)
    def GetBlockCRCList(self, crcList):
        for row in range(0, BLOCK_ROW_COUNT):
            for col in range(0, BLOCK_COL_COUNT):
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: *(crcList++) = m_aakBlock[row][col].GetCRC();
                *(crcList) = self._m_aakBlock[row][col].GetCRC()
                crcList += 1

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Pointer arithmetic is detected on the parameter 'crcList':
#ORIGINAL METINII C CODE: void GetDiffBlocks(const uint * crcList, dict<byte, const SGuildMarkBlock *> & mapDiffBlocks)
    def GetDiffBlocks(self, crcList, mapDiffBlocks):
        posBlock = 0

        for row in range(0, BLOCK_ROW_COUNT):
            for col in range(0, BLOCK_COL_COUNT):
                if self._m_aakBlock[row][col].m_crc != *crcList:
                    mapDiffBlocks.insert(dict.value_type(posBlock, self._m_aakBlock[row][col]))
                crcList += 1
                posBlock += 1

    _INVALID_HANDLE = 0xffffffff

    def _BuildAllBlocks(self):
        apxBuf = [0 for _ in range(SGuildMarkBlock.SIZE)]
        #sys_log(0, "GuildMarkImage::BuildAllBlocks")

        for row in range(0, BLOCK_ROW_COUNT):
            for col in range(0, BLOCK_COL_COUNT):
                self.GetData(col * SGuildMarkBlock.WIDTH, row * SGuildMarkBlock.HEIGHT, uint(SGuildMarkBlock.WIDTH), uint(SGuildMarkBlock.HEIGHT), apxBuf)
                self._m_aakBlock[row][col].Compress(apxBuf)

# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    _sizeof(UnnamedParameter)