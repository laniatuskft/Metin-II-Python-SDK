import math

class CGuildMarkManager(singleton):
    MAX_IMAGE_COUNT = 5
    INVALID_MARK_ID = 0xffffffff

    class TGuildSymbol:

        def __init__(self):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.crc = 0
            self.raw = []


    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self._m_mapIdx_Image = {}
        self._m_mapGID_MarkID = {}
        self._m_setFreeMarkID = std::set()
        self._m_pathPrefix = ""
        self._m_mapSymbol = {}

        i = 0
        while i < MAX_IMAGE_COUNT * CGuildMarkImage.MARK_TOTAL_COUNT:
            self._m_setFreeMarkID.insert(i)
            i += 1

    def close(self):
        it = m_mapIdx_Image.begin()
        while it is not self._m_mapIdx_Image.end():
            self._DeleteImage(it.second)
            it += 1

        self._m_mapIdx_Image.clear()

    def GetGuildSymbol(self, guildID):
        it = self._m_mapSymbol.find(guildID)

        if it is self._m_mapSymbol.end():
            return None

        return it.second

    def LoadSymbol(self, filename):
        fp = fopen(filename, "rb")

        if fp is None:
            return ((not DefineConstants.false))
        else:
            symbolCount = None
            fread(symbolCount, 4, 1, fp)

            for i in range(0, symbolCount):
                guildID = None
                dwSize = None
                fread(guildID, 4, 1, fp)
                fread(dwSize, 4, 1, fp)

                gs = TGuildSymbol()
                gs.raw.resize(dwSize)
                fread(gs.raw[0], 1, dwSize, fp)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no equivalent to 'reinterpret_cast' in Python:
                gs.crc = GetCRC32(reinterpret_cast<const char>(gs.raw[0]), dwSize)
                self._m_mapSymbol.update({guildID: gs})

        fclose(fp)
        return ((not DefineConstants.false))

    def SaveSymbol(self, filename):
        fp = fopen(filename, "wb")
        if fp is None:
            #lani_err("Cannot open Symbol file (name: %s)", filename)
            return

        symbolCount = len(self._m_mapSymbol)
        fwrite(symbolCount, 4, 1, fp)

        it = m_mapSymbol.begin()
        while it is not self._m_mapSymbol.end():
            guildID = it.first
            dwSize = it.second.raw.size()
            fwrite(guildID, 4, 1, fp)
            fwrite(dwSize, 4, 1, fp)
            fwrite(it.second.raw[0], 1, dwSize, fp)
            it += 1

        fclose(fp)

    def UploadSymbol(self, guildID, iSize, pbyData):
        #sys_log(0, "GuildSymbolUpload guildID %u Size %d", guildID, iSize)

        if guildID not in self._m_mapSymbol.keys():
            self._m_mapSymbol.update({guildID: TGuildSymbol()})

        rSymbol = self._m_mapSymbol[guildID]
        rSymbol.raw.clear()

        if iSize > 0:
            rSymbol.raw.reserve(iSize)
            std::copy(pbyData, (pbyData + iSize), std::back_inserter(rSymbol.raw))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no equivalent to 'reinterpret_cast' in Python:
            rSymbol.crc = GetCRC32(reinterpret_cast<const char>(pbyData), iSize)

    def SetMarkPathPrefix(self, prefix):
        self._m_pathPrefix = prefix

    def LoadMarkIndex(self):
        buf = str(['\0' for _ in range(64)])
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        snprintf(buf, sizeof(buf), "mark/%s_index", self._m_pathPrefix)
        fp = fopen(buf, "r")

        if fp is None:
            return DefineConstants.false

        guildID = None
        markID = None

        line = str(['\0' for _ in range(256)])

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        while fgets(line, sizeof(line)-1, fp):
            sscanf(line, "%u %u", guildID, markID)
            line[0] = '\0'
            self.AddMarkIDByGuildID(guildID, markID)

        self.LoadMarkImages()

        fclose(fp)
        return ((not DefineConstants.false))

    def SaveMarkIndex(self):
        buf = str(['\0' for _ in range(64)])
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        snprintf(buf, sizeof(buf), "mark/%s_index", self._m_pathPrefix)
        fp = fopen(buf, "w")

        if fp is None:
            #lani_err("MarkManager::SaveMarkIndex: cannot open index file.")
            return DefineConstants.false

        it = m_mapGID_MarkID.begin()
        while it is not self._m_mapGID_MarkID.end():
            fprintf(fp, "%u %u\n", it.first, it.second)
            it += 1

        fclose(fp)
        #sys_log(0, "MarkManager::SaveMarkIndex: index count %d", len(self._m_mapGID_MarkID))
        return ((not DefineConstants.false))

    def LoadMarkImages(self):
        isMarkExists = [False for _ in range(MAX_IMAGE_COUNT)]
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memset(isMarkExists, 0, sizeof(isMarkExists))

        it = m_mapGID_MarkID.begin()
        while it is not self._m_mapGID_MarkID.end():
            markID = it.second

            if markID < MAX_IMAGE_COUNT * CGuildMarkImage.MARK_TOTAL_COUNT:
                isMarkExists[math.trunc(markID / float(CGuildMarkImage.MARK_TOTAL_COUNT))] = ((not DefineConstants.false))
            it += 1

        for i in range(0, MAX_IMAGE_COUNT):
            if isMarkExists[i]:
                self._GetImage(i)

    def SaveMarkImage(self, imgIdx):
        path = ""

        temp_ref_path = RefObject(path);
        if self.GetMarkImageFilename(imgIdx, temp_ref_path):
            path = temp_ref_path.arg_value
            if not self._GetImage(imgIdx).Save(path):
                #lani_err("%s Save failed\n", path)
        else:
            path = temp_ref_path.arg_value

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: bool GetMarkImageFilename(uint imgIdx, str & path) const
    def GetMarkImageFilename(self, imgIdx, path):
        if imgIdx >= MAX_IMAGE_COUNT:
            return DefineConstants.false

        buf = str(['\0' for _ in range(64)])
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        snprintf(buf, sizeof(buf), "mark/%s_%u.tga", self._m_pathPrefix, imgIdx)
        path.arg_value = buf
        return ((not DefineConstants.false))

    def AddMarkIDByGuildID(self, guildID, markID):
        if markID >= MAX_IMAGE_COUNT * CGuildMarkImage.MARK_TOTAL_COUNT:
            return DefineConstants.false

        self._m_mapGID_MarkID.insert(dict.value_type(guildID, markID))
        self._m_setFreeMarkID.erase(markID)
        return ((not DefineConstants.false))

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: uint GetMarkImageCount() const
    def GetMarkImageCount(self):
        return len(self._m_mapIdx_Image)

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: uint GetMarkCount() const
    def GetMarkCount(self):
        return len(self._m_mapGID_MarkID)

    def GetMarkID(self, guildID):
        it = self._m_mapGID_MarkID.find(guildID)

        if it is self._m_mapGID_MarkID.end():
            return uint(INVALID_MARK_ID)

        return it.second

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: void CopyMarkIdx(char * pcBuf) const
    def CopyMarkIdx(self, pcBuf):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Pointer arithmetic is detected on this variable:
#ORIGINAL METINII C CODE: ushort * pwBuf = (ushort *) pcBuf;
        pwBuf = pcBuf.arg_value

        it = m_mapGID_MarkID.begin()
        while it is not self._m_mapGID_MarkID.end():
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: *(pwBuf++) = it->first;
            *(pwBuf) = it.first
            pwBuf += 1
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: *(pwBuf++) = it->second;
            *(pwBuf) = it.second
            pwBuf += 1
            it += 1

    def SaveMark(self, guildID, pbMarkImage):
        idMark = None

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((idMark = GetMarkID(guildID)) == INVALID_MARK_ID)
        if (idMark = self.GetMarkID(guildID)) == INVALID_MARK_ID:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((idMark = __AllocMarkID(guildID)) == INVALID_MARK_ID)
            if (idMark = self._AllocMarkID(guildID)) == INVALID_MARK_ID:
                #lani_err("CGuildMarkManager: cannot alloc mark id %u", guildID)
                return DefineConstants.false
            else:
                #sys_log(0, "SaveMark: mark id alloc %u", idMark)
        else:
            #sys_log(0, "SaveMark: mark id found %u", idMark)

        imgIdx = (math.trunc(idMark / float(CGuildMarkImage.MARK_TOTAL_COUNT)))
        pkImage = self._GetImage(imgIdx)

        if pkImage:
            pkImage.SaveMark(math.fmod(idMark, CGuildMarkImage.MARK_TOTAL_COUNT), pbMarkImage)

            self.SaveMarkImage(imgIdx)
            self.SaveMarkIndex()

        return idMark

    def DeleteMark(self, guildID):
        it = self._m_mapGID_MarkID.find(guildID)

        if it is self._m_mapGID_MarkID.end():
            return

        pkImage = None

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if ((pkImage = __GetImage(it->second / CGuildMarkImage::MARK_TOTAL_COUNT)) != NULL)
        if (pkImage = self._GetImage(it.second / CGuildMarkImage.MARK_TOTAL_COUNT)) is not None:
            pkImage.DeleteMark(math.fmod(it.second, CGuildMarkImage.MARK_TOTAL_COUNT))

        self._m_setFreeMarkID.insert(it.second)
        self._m_mapGID_MarkID.pop(it)

        self.SaveMarkIndex()

    def GetDiffBlocks(self, imgIdx, crcList, mapDiffBlocks):
        mapDiffBlocks.clear()

        if self._m_mapIdx_Image.end() == self._m_mapIdx_Image.find(imgIdx):
            #lani_err("invalid idx %u", imgIdx)
            return

        p = self._GetImage(imgIdx)

        if p:
            p.GetDiffBlocks(crcList, mapDiffBlocks)

    def SaveBlockFromCompressedData(self, imgIdx, posBlock, pbBlock, dwSize):
        pkImage = self._GetImage(imgIdx)

        if pkImage:
            pkImage.SaveBlockFromCompressedData(posBlock, pbBlock, dwSize)

        return DefineConstants.false

    def GetBlockCRCList(self, imgIdx, crcList):
        if self._m_mapIdx_Image.end() == self._m_mapIdx_Image.find(imgIdx):
            #lani_err("invalid idx %u", imgIdx)
            return DefineConstants.false

        p = self._GetImage(imgIdx)

        if p:
            p.GetBlockCRCList(crcList)

        return ((not DefineConstants.false))

    def _NewImage(self):
        return LG_NEW_M2 CGuildMarkImage

    def _DeleteImage(self, pkImgDel):
        LG_DEL_MEM(pkImgDel)

    def _AllocMarkID(self, guildID):
        it = self._m_setFreeMarkID.lower_bound(0)

        if it is self._m_setFreeMarkID.end():
            return uint(INVALID_MARK_ID)

        markID = *it

        imgIdx = math.trunc(markID / float(CGuildMarkImage.MARK_TOTAL_COUNT))
        pkImage = self._GetImage(imgIdx)

        if pkImage is not None and self.AddMarkIDByGuildID(guildID, markID):
            return markID

        return uint(INVALID_MARK_ID)

    def _GetImage(self, imgIdx):
        it = self._m_mapIdx_Image.find(imgIdx)

        if it is self._m_mapIdx_Image.end():
            imagePath = ""

            temp_ref_imagePath = RefObject(imagePath);
            if self.GetMarkImageFilename(imgIdx, temp_ref_imagePath):
                imagePath = temp_ref_imagePath.arg_value
                pkImage = self._NewImage()
                self._m_mapIdx_Image.insert(dict.value_type(imgIdx, pkImage))

                if not pkImage.Load(imagePath):
                    pkImage.Build(imagePath)
                    pkImage.Load(imagePath)

                return pkImage
            else:
                imagePath = temp_ref_imagePath.arg_value
                return None
        else:
            return it.second

# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    _GetImagePtr(idMark)


def main(args):
    lzo = LZOManager()
    mgr = CGuildMarkManager()
    f = str(['\0' for _ in range(64)])

    srandomdev()

    ilInit()
    Globals.thecore_init(25, heartbeat)

    mgr.SetMarkPathPrefix("mark")
    mgr.LoadMarkIndex()
    for i in range(0, 1279):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        snprintf(f, sizeof(f), "%u.jpg", (math.fmod(random(), 5)) + 1)
        Globals.SaveMark(i, f)

    idx_client = [0 for _ in range(CGuildMarkImage.BLOCK_TOTAL_COUNT)]
    idx_server = [0 for _ in range(CGuildMarkImage.BLOCK_TOTAL_COUNT)]

    temp_ref_idx_client = RefObject(idx_client);
    mgr.GetBlockCRCList(0, temp_ref_idx_client)
    idx_client = temp_ref_idx_client.arg_value
    temp_ref_idx_server = RefObject(idx_server);
    mgr.GetBlockCRCList(1, temp_ref_idx_server)
    idx_server = temp_ref_idx_server.arg_value

    mapDiff = {}
    mgr.GetDiffBlocks(1, idx_client, mapDiff)

    printf("#1 Diff %u\n", len(mapDiff))

    it = mapDiff.begin()
    while it is not mapDiff.end():
        printf("Put Block pos %u crc %u\n", it.first, it.second.m_crc)
        mgr.SaveBlockFromCompressedData(0, it.first, it.second.m_abCompBuf, it.second.m_sizeCompBuf)
        it += 1

    temp_ref_idx_client2 = RefObject(idx_client);
    mgr.GetBlockCRCList(0, temp_ref_idx_client2)
    idx_client = temp_ref_idx_client2.arg_value
    mgr.GetDiffBlocks(1, idx_client, mapDiff)
    printf("#2 Diff %u\n", len(mapDiff))
    return 1
##endif
