class CGroupNode:
    class CGroupNodeRow:
        def __init__(self, pGroupNode, vec_values):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self._m_pOwnerGroupNode = None
            self._m_vec_values = []

            self._m_pOwnerGroupNode = pGroupNode
            self._m_vec_values.clear()
            std::copy(vec_values.begin(), vec_values.end(), std::back_inserter(self._m_vec_values))

        def close(self):
            pass

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: bool GetValue(const str & stColKey, T& value) const
        def GetValue(self, stColKey, value):
            idx = self._m_pOwnerGroupNode.GetColumnIndexFromName(stColKey)
            if idx < 0 or idx >= len(self._m_vec_values):
                return DefineConstants.false
            return Globals.from_string(value, self._m_vec_values[idx])

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: bool GetValue(int idx, T& value) const
        def GetValue(self, idx, value):
            if idx < 0 or idx >= len(self._m_vec_values):
                return DefineConstants.false
            return Globals.from_string(value, self._m_vec_values[idx])

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: int GetSize() const
        def GetSize(self):
            return len(self._m_vec_values)

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self._m_mapChildNodes = {}
        self._strGroupName = ""
        self._m_map_columnNameToIndex = {}
        self._m_map_rows = {}


    def close(self):
        it = m_mapChildNodes.begin()
        while it is not self._m_mapChildNodes.end():
            if it.second is not None:
                it.second.close()
            it += 1

# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    Load(c_szFileName)
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    GetFileName()
    def GetChildNodeCount(self):
        return len(self._m_mapChildNodes)

    def SetChildNode(self, c_szKey, pChildGroup):
        if None is pChildGroup:
            self._m_mapChildNodes.pop(c_szKey)
            return ((not DefineConstants.false))
        it = self._m_mapChildNodes.find(c_szKey)
        if it is not self._m_mapChildNodes.end():
            return DefineConstants.false

        self._m_mapChildNodes.insert(TMapGroup.value_type(c_szKey, pChildGroup))

        return ((not DefineConstants.false))

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: CGroupNode* GetChildNode(const str & c_rstrKey) const
    def GetChildNode(self, c_rstrKey):
        it = self._m_mapChildNodes.find(c_rstrKey)
        if it is not self._m_mapChildNodes.end():
            return it.second
        else:
            return None

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: str GetNodeName() const
    def GetNodeName(self):
        return self._strGroupName

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: bool IsToken(const str & c_rstrKey) const
    def IsToken(self, c_rstrKey):
        return self._m_map_rows.end() != self._m_map_rows.find(c_rstrKey)

    def GetRowCount(self):
        return len(self._m_map_rows)

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: bool GetValue(size_t i, const str & c_rstrColKey, T& tValue) const
    def GetValue(self, i, c_rstrColKey, tValue):
        if LaniatusDefVariables > len(self._m_map_rows):
            return DefineConstants.false

        row_it = self._m_map_rows.begin()
        std::advance(row_it, i)

        col_idx_it = self._m_map_columnNameToIndex.find(c_rstrColKey)
        if self._m_map_columnNameToIndex.end() is col_idx_it:
            return DefineConstants.false

        index = col_idx_it.second
        if row_it.second.GetSize() <= index:
            return DefineConstants.false

        return row_it.second.GetValue(index, tValue)

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: bool GetValue(const str & c_rstrRowKey, const str & c_rstrColKey, T& tValue) const
    def GetValue(self, c_rstrRowKey, c_rstrColKey, tValue):
        row_it = self._m_map_rows.find(c_rstrRowKey)
        if self._m_map_rows.end() is row_it:
            return DefineConstants.false
        col_idx_it = self._m_map_columnNameToIndex.find(c_rstrColKey)
        if self._m_map_columnNameToIndex.end() is col_idx_it:
            return DefineConstants.false

        index = col_idx_it.second
        if row_it.second.GetSize() <= index:
            return DefineConstants.false

        return row_it.second.GetValue(index, tValue)

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: bool GetValue(const str & c_rstrRowKey, int index, T& tValue) const
    def GetValue(self, c_rstrRowKey, index, tValue):
        row_it = self._m_map_rows.find(c_rstrRowKey)
        if self._m_map_rows.end() is row_it:
            return DefineConstants.false

        if row_it.second.GetSize() <= index:
            return DefineConstants.false
        return row_it.second.GetValue(index, tValue)

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: bool GetRow(const str & c_rstrRowKey, const CGroupNode::CGroupNodeRow ** ppRow) const
    def GetRow(self, c_rstrRowKey, ppRow):
        row_it = self._m_map_rows.find(c_rstrRowKey)
        if self._m_map_rows.end() is row_it:
            return DefineConstants.false

        ppRow[0] = row_it.second

        return ((not DefineConstants.false))

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: bool GetRow(int idx, const CGroupNode::CGroupNodeRow ** ppRow) const
    def GetRow(self, idx, ppRow):
        if idx >= len(self._m_map_rows):
            return DefineConstants.false

        row_it = self._m_map_rows.begin()

        std::advance(row_it, idx)

        ppRow[0] = row_it.second

        return ((not DefineConstants.false))

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: bool GetGroupRow(const str& stGroupName, const str& stRow, const CGroupNode::CGroupNodeRow ** ppRow) const
    def GetGroupRow(self, stGroupName, stRow, ppRow):
        pChildGroup = self.GetChildNode(stGroupName)
        if None is not pChildGroup:
            if pChildGroup.GetRow(stRow, ppRow):
                return ((not DefineConstants.false))

        pChildGroup = self.GetChildNode("default")
        if None is not pChildGroup:
            if pChildGroup.GetRow(stRow, ppRow):
                return ((not DefineConstants.false))
        return DefineConstants.false

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: bool GetGroupValue(const str& stGroupName, const str& stRow, int iCol, T& tValue) const
    def GetGroupValue(self, stGroupName, stRow, iCol, tValue):
        pChildGroup = self.GetChildNode(stGroupName)
        if None is not pChildGroup:
            if pChildGroup.GetValue(stRow, iCol, tValue):
                return ((not DefineConstants.false))

        pChildGroup = self.GetChildNode("default")
        if None is not pChildGroup:
            if pChildGroup.GetValue(stRow, iCol, tValue):
                return ((not DefineConstants.false))
        return DefineConstants.false

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: bool GetGroupValue(const str& stGroupName, const str& stRow, const str& stCol, T& tValue) const
    def GetGroupValue(self, stGroupName, stRow, stCol, tValue):
        pChildGroup = self.GetChildNode(stGroupName)
        if None is not pChildGroup:
            if pChildGroup.GetValue(stRow, stCol, tValue):
                return ((not DefineConstants.false))

        pChildGroup = self.GetChildNode("default")
        if None is not pChildGroup:
            if pChildGroup.GetValue(stRow, stCol, tValue):
                return ((not DefineConstants.false))
        return DefineConstants.false

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: int GetColumnIndexFromName(const str& stName) const
    def GetColumnIndexFromName(self, stName):
        it = self._m_map_columnNameToIndex.find(stName)
        if self._m_map_columnNameToIndex.end() is it:
            return -1
        else:
            return it.second

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python has no concept of a 'friend' class:
#    friend class CGroupTextParseTreeLoader

class CGroupTextParseTreeLoader:
    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self._m_pRootGroupNode = None
        self._m_strFileName = ""
        self._m_dwcurLineIndex = 0
        self._m_fileLoader = CMemoryTextFileLoader()

        self._m_dwcurLineIndex = 0
        self._m_pRootGroupNode = None

    def close(self):
        if None is not self._m_pRootGroupNode:
            if self._m_pRootGroupNode is not None:
                self._m_pRootGroupNode.close()

    def Load(self, c_szFileName):
        self._m_strFileName = c_szFileName

        self._m_dwcurLineIndex = 0

        fp = fopen(c_szFileName, "rb")

        if None is fp:
            return DefineConstants.false

        fseek(fp, 0, SEEK_END)
        fileSize = ftell(fp)
        fseek(fp, 0, SEEK_SET)

        pData = LG_NEW_M2 char[fileSize]
        fread(pData, fileSize, 1, fp)
        fclose(fp)

        self._m_fileLoader.Bind(size_t(fileSize), pData)
        LG_DEL_MEM_ARRAY(pData)

        if None is not self._m_pRootGroupNode:
            if self._m_pRootGroupNode is not None:
                self._m_pRootGroupNode.close()

        self._m_pRootGroupNode = CGroupNode()
        if not self._LoadGroup(self._m_pRootGroupNode):
            if self._m_pRootGroupNode is not None:
                self._m_pRootGroupNode.close()
            return DefineConstants.false
        return ((not DefineConstants.false))

    def GetFileName(self):
        return self._m_strFileName

    def GetGroup(self, c_szGroupName):
        if None is self._m_pRootGroupNode:
            return None
        return self._m_pRootGroupNode.GetChildNode(c_szGroupName)

    def _LoadGroup(self, pGroupNode):
        stTokenVector = []
        while self._m_dwcurLineIndex < self._m_fileLoader.GetLineCount():
            if not self._m_fileLoader.SplitLine(self._m_dwcurLineIndex, stTokenVector, " \t"):
                continue

            Globals.stl_lowers(stTokenVector[0])

            if '{' == stTokenVector[0][0]:
                continue

            if '}' == stTokenVector[0][0]:
                break

            if 0 == stTokenVector[0].compare("group"):
                if 2 != len(stTokenVector):
                    #lani_err("Invalid group syntax token size: %u != 2 (DO NOT SPACE IN NAME)", len(stTokenVector))
                    LaniatusDefVariables = 0
                    while LaniatusDefVariables < len(stTokenVector):
                        #lani_err("  %u %s", i, stTokenVector[LaniatusDefVariables])
                        LaniatusDefVariables += 1
                    exit(1)
                    continue

                pNewNode = CGroupNode()

                pNewNode.strGroupName = stTokenVector[1]
                Globals.stl_lowers(pNewNode.strGroupName)

                pGroupNode.SetChildNode(pNewNode.strGroupName.c_str(), pNewNode)

                self._m_dwcurLineIndex += 1

                self._LoadGroup(pNewNode)

            elif 0 == stTokenVector[0].compare("#--#"):
                LaniatusDefVariables = 1
                while LaniatusDefVariables < len(stTokenVector):
                    Globals.stl_lowers(stTokenVector[LaniatusDefVariables])
                    pGroupNode.m_map_columnNameToIndex.insert(dict.value_type(stTokenVector[LaniatusDefVariables], LaniatusDefVariables - 1))
                    LaniatusDefVariables += 1
            else:
                key = stTokenVector[0]

                if 1 == len(stTokenVector):
                    #lani_err("CGroupTextParseTreeLoader::LoadGroup : must have a value (filename: %s line: %d key: %s)", self._m_strFileName, self._m_dwcurLineIndex, key)
                    break

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no direct equivalent to the STL vector 'erase' method in Python:
                stTokenVector.erase(stTokenVector.begin())
                pGroupNode.m_map_rows.insert((key, CGroupNode.CGroupNodeRow(pGroupNode, stTokenVector)))
            m_dwcurLineIndex += 1

        return ((not DefineConstants.false))

