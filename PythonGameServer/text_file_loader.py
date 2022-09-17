class CTextFileLoader:
    class SGroupNode:

        def __init__(self):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.strGroupName = ""
            self.LocalTokenVectorMap = {}
            self.pParentNode = None
            self.ChildNodeVector = []





    @staticmethod
    def DestroySystem():
        CTextFileLoader.Globals.ms_groupNodePool.Clear()

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.m_strFileName = ""
        self.m_dwcurLineIndex = 0
        self.mc_pData = None
        self.m_fileLoader = CMemoryTextFileLoader()
        self.m_globalNode = SGroupNode()
        self.m_pcurNode = None

        self.m_dwcurLineIndex = 0
        self.mc_pData = None
        self.SetTop()

        self.m_globalNode.strGroupName = "global"
        self.m_globalNode.pParentNode = None

    def close(self):
        pass

    def Load(self, c_szFileName):
        self.m_strFileName = c_szFileName

        self.m_dwcurLineIndex = 0

        fp = fopen(c_szFileName, "rb")

        if None is fp:
            return DefineConstants.false

        fseek(fp, 0, SEEK_END)
        fileSize = ftell(fp)
        fseek(fp, 0, SEEK_SET)

        pData = LG_NEW_M2 char[fileSize]
        fread(pData, fileSize, 1, fp)
        fclose(fp)

        self.m_fileLoader.Bind(size_t(fileSize), pData)
        LG_DEL_MEM_ARRAY(pData)

        self.LoadGroup(self.m_globalNode)
        return ((not DefineConstants.false))

    def GetFileName(self):
        return self.m_strFileName

    def SetTop(self):
        self.m_pcurNode = self.m_globalNode

    def GetChildNodeCount(self):
        if self.m_pcurNode is None:
            assert not "Node to access has not set!"
            return 0

        return len(self.m_pcurNode.ChildNodeVector)

    def SetChildNode(self, c_szKey):
        if self.m_pcurNode is None:
            assert not "Node to access has not set!"
            return DefineConstants.false

        LaniatusDefVariables = 0
        while LaniatusDefVariables < len(self.m_pcurNode.ChildNodeVector):
            pGroupNode = self.m_pcurNode.ChildNodeVector[LaniatusDefVariables]
            if 0 == pGroupNode.strGroupName.compare(c_szKey):
                self.m_pcurNode = pGroupNode
                return ((not DefineConstants.false))
            LaniatusDefVariables += 1

        return DefineConstants.false

    def SetChildNode(self, c_rstrKeyHead, dwIndex):
        szKey = str(['\0' for _ in range(32)])
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        snprintf(szKey, sizeof(szKey), "%s%02u", c_rstrKeyHead, dwIndex)
        return self.SetChildNode(szKey)

    def SetChildNode(self, dwIndex):
        if self.m_pcurNode is None:
            assert not "Node to access has not set!"
            return DefineConstants.false

        if dwIndex >= len(self.m_pcurNode.ChildNodeVector):
            assert not "Node index to set is too large to access!"
            return DefineConstants.false

        self.m_pcurNode = self.m_pcurNode.ChildNodeVector[dwIndex]

        return ((not DefineConstants.false))

    def SetParentNode(self):
        if self.m_pcurNode is None:
            assert not "Node to access has not set!"
            return DefineConstants.false

        if None is self.m_pcurNode.pParentNode:
            assert not "Current group node is already top!"
            return DefineConstants.false

        self.m_pcurNode = self.m_pcurNode.pParentNode

        return ((not DefineConstants.false))

    def GetCurrentNodeName(self, pstrName):
        if self.m_pcurNode is None:
            return DefineConstants.false
        if None is self.m_pcurNode.pParentNode:
            return DefineConstants.false

        pstrName = self.m_pcurNode.strGroupName

        return ((not DefineConstants.false))

    def IsToken(self, c_rstrKey):
        if self.m_pcurNode is None:
            assert not "Node to access has not set!"
            return DefineConstants.false

        return self.m_pcurNode.LocalTokenVectorMap.end() != self.m_pcurNode.LocalTokenVectorMap.find(c_rstrKey)

    def GetTokenVector(self, c_rstrKey, ppTokenVector):
        if self.m_pcurNode is None:
            assert not "Node to access has not set!"
            return DefineConstants.false

        it = self.m_pcurNode.LocalTokenVectorMap.find(c_rstrKey)
        if self.m_pcurNode.LocalTokenVectorMap.end() is it:
            #sys_log(2, " CTextFileLoader::GetTokenVector - Failed to find the key %s [%s :: %s]", self.m_strFileName, self.m_pcurNode.strGroupName, c_rstrKey)
            return DefineConstants.false

        ppTokenVector[0] = it.second

        return ((not DefineConstants.false))

    def GetTokenBoolean(self, c_rstrKey, pData):
        pTokenVector = None
        if not self.GetTokenVector(c_rstrKey, pTokenVector):
            return DefineConstants.false

        if not pTokenVector:
            #sys_log(2, " CTextFileLoader::GetTokenBoolean - Failed to find the value %s [%s : %s]", self.m_strFileName, self.m_pcurNode.strGroupName, c_rstrKey)
            return DefineConstants.false

        out = False
        temp_ref_out = RefObject(out);
        Globals.str_to_number(temp_ref_out, pTokenVector[0])
        out = temp_ref_out.arg_value
        pData.arg_value = out

        return ((not DefineConstants.false))

    def GetTokenByte(self, c_rstrKey, pData):
        pTokenVector = None
        if not self.GetTokenVector(c_rstrKey, pTokenVector):
            return DefineConstants.false

        if not pTokenVector:
            #sys_log(2, " CTextFileLoader::GetTokenByte - Failed to find the value %s [%s : %s]", self.m_strFileName, self.m_pcurNode.strGroupName, c_rstrKey)
            return DefineConstants.false

        out = 0
        temp_ref_out = RefObject(out);
        Globals.str_to_number(temp_ref_out, pTokenVector[0])
        out = temp_ref_out.arg_value
        pData.arg_value = out

        return ((not DefineConstants.false))

    def GetTokenWord(self, c_rstrKey, pData):
        pTokenVector = None
        if not self.GetTokenVector(c_rstrKey, pTokenVector):
            return DefineConstants.false

        if not pTokenVector:
            #sys_log(2, " CTextFileLoader::GetTokenWord - Failed to find the value %s [%s : %s]", self.m_strFileName, self.m_pcurNode.strGroupName, c_rstrKey)
            return DefineConstants.false

        out = 0
        temp_ref_out = RefObject(out);
        Globals.str_to_number(temp_ref_out, pTokenVector[0])
        out = temp_ref_out.arg_value
        pData.arg_value = out

        return ((not DefineConstants.false))

    def GetTokenInteger(self, c_rstrKey, pData):
        pTokenVector = None
        if not self.GetTokenVector(c_rstrKey, pTokenVector):
            return DefineConstants.false

        if not pTokenVector:
            #sys_log(2, " CTextFileLoader::GetTokenInteger - Failed to find the value %s [%s : %s]", self.m_strFileName, self.m_pcurNode.strGroupName, c_rstrKey)
            return DefineConstants.false

        out = 0
        temp_ref_out = RefObject(out);
        Globals.str_to_number(temp_ref_out, pTokenVector[0])
        out = temp_ref_out.arg_value
        pData.arg_value = out

        return ((not DefineConstants.false))

    def GetTokenDoubleWord(self, c_rstrKey, pData):
        return self.GetTokenInteger(c_rstrKey, int(pData.arg_value))

    def GetTokenFloat(self, c_rstrKey, pData):
        pTokenVector = None
        if not self.GetTokenVector(c_rstrKey, pTokenVector):
            return DefineConstants.false

        if not pTokenVector:
            #sys_log(2, " CTextFileLoader::GetTokenFloat - Failed to find the value %s [%s : %s]", self.m_strFileName, self.m_pcurNode.strGroupName, c_rstrKey)
            return DefineConstants.false

        pData.arg_value = atof(pTokenVector[0])

        return ((not DefineConstants.false))

    def GetTokenVector2(self, c_rstrKey, pVector2):
        pTokenVector = None
        if not self.GetTokenVector(c_rstrKey, pTokenVector):
            return DefineConstants.false

        if len(pTokenVector) != 2:
            #sys_log(2, " CTextFileLoader::GetTokenVector2 - This key should have 2 values %s [%s : %s]", self.m_strFileName, self.m_pcurNode.strGroupName, c_rstrKey)
            return DefineConstants.false

        pVector2.x = atof(pTokenVector[0])
        pVector2.y = atof(pTokenVector[1])

        return ((not DefineConstants.false))

    def GetTokenVector3(self, c_rstrKey, pVector3):
        pTokenVector = None
        if not self.GetTokenVector(c_rstrKey, pTokenVector):
            return DefineConstants.false

        if len(pTokenVector) != 3:
            #sys_log(2, " CTextFileLoader::GetTokenVector3 - This key should have 3 values %s [%s : %s]", self.m_strFileName, self.m_pcurNode.strGroupName, c_rstrKey)
            return DefineConstants.false

        pVector3.x = atof(pTokenVector[0])
        pVector3.y = atof(pTokenVector[1])
        pVector3.z = atof(pTokenVector[2])

        return ((not DefineConstants.false))

    def GetTokenVector4(self, c_rstrKey, pVector4):
        pTokenVector = None
        if not self.GetTokenVector(c_rstrKey, pTokenVector):
            return DefineConstants.false

        if len(pTokenVector) != 4:
            #sys_log(2, " CTextFileLoader::GetTokenVector3 - This key should have 3 values %s [%s : %s]", self.m_strFileName, self.m_pcurNode.strGroupName, c_rstrKey)
            return DefineConstants.false

        pVector4.x = atof(pTokenVector[0])
        pVector4.y = atof(pTokenVector[1])
        pVector4.z = atof(pTokenVector[2])
        pVector4.w = atof(pTokenVector[3])

        return ((not DefineConstants.false))

    def GetTokenPosition(self, c_rstrKey, pVector):
        return self.GetTokenVector3(c_rstrKey, pVector)

    def GetTokenQuaternion(self, c_rstrKey, pQ):
        pTokenVector = None
        if not self.GetTokenVector(c_rstrKey, pTokenVector):
            return DefineConstants.false

        if len(pTokenVector) != 4:
            #sys_log(2, " CTextFileLoader::GetTokenVector3 - This key should have 3 values %s [%s : %s]", self.m_strFileName, self.m_pcurNode.strGroupName, c_rstrKey)
            return DefineConstants.false

        pQ.x = atof(pTokenVector[0])
        pQ.y = atof(pTokenVector[1])
        pQ.z = atof(pTokenVector[2])
        pQ.w = atof(pTokenVector[3])
        return ((not DefineConstants.false))

    def GetTokenDirection(self, c_rstrKey, pVector):
        pTokenVector = None
        if not self.GetTokenVector(c_rstrKey, pTokenVector):
            return DefineConstants.false

        if len(pTokenVector) != 3:
            #sys_log(2, " CTextFileLoader::GetTokenDirection - This key should have 3 values %s [%s : %s]", self.m_strFileName, self.m_pcurNode.strGroupName, c_rstrKey)
            return DefineConstants.false

        pVector.x = atof(pTokenVector[0])
        pVector.y = atof(pTokenVector[1])
        pVector.z = atof(pTokenVector[2])
        return ((not DefineConstants.false))

    def GetTokenColor(self, c_rstrKey, pColor):
        pTokenVector = None
        if not self.GetTokenVector(c_rstrKey, pTokenVector):
            return DefineConstants.false

        if len(pTokenVector) != 4:
            #sys_log(2, " CTextFileLoader::GetTokenColor - This key should have 4 values %s [%s : %s]", self.m_strFileName, self.m_pcurNode.strGroupName, c_rstrKey)
            return DefineConstants.false

        pColor.r = atof(pTokenVector[0])
        pColor.g = atof(pTokenVector[1])
        pColor.b = atof(pTokenVector[2])
        pColor.a = atof(pTokenVector[3])

        return ((not DefineConstants.false))

    def GetTokenColor(self, c_rstrKey, pColor):
        pTokenVector = None
        if not self.GetTokenVector(c_rstrKey, pTokenVector):
            return DefineConstants.false

        if len(pTokenVector) != 4:
            #sys_log(2, " CTextFileLoader::GetTokenColor - This key should have 4 values %s [%s : %s]", self.m_strFileName, self.m_pcurNode.strGroupName, c_rstrKey)
            return DefineConstants.false

        pColor.r = atof(pTokenVector[0])
        pColor.g = atof(pTokenVector[1])
        pColor.b = atof(pTokenVector[2])
        pColor.a = atof(pTokenVector[3])

        return ((not DefineConstants.false))

    def GetTokenString(self, c_rstrKey, pString):
        pTokenVector = None
        if not self.GetTokenVector(c_rstrKey, pTokenVector):
            return DefineConstants.false

        if not pTokenVector:
            #sys_log(2, " CTextFileLoader::GetTokenString - Failed to find the value %s [%s : %s]", self.m_strFileName, self.m_pcurNode.strGroupName, c_rstrKey)
            return DefineConstants.false

        pString = pTokenVector[0]

        return ((not DefineConstants.false))

# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    LoadGroup(pGroupNode)


    _ms_groupNodePool = CDynamicPool()

def LoadGroup(pGroupNode):
    stTokenVector = []
    while m_dwcurLineIndex < m_fileLoader.GetLineCount():
        if not m_fileLoader.SplitLine(m_dwcurLineIndex, stTokenVector):
            continue

        stl_lowers(stTokenVector[0])

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

            pNewNode = CTextFileLoader.Globals.ms_groupNodePool.Alloc()
            pNewNode.pParentNode = pGroupNode
            pNewNode.strGroupName = stTokenVector[1]
            stl_lowers(pNewNode.strGroupName)
            pGroupNode.ChildNodeVector.push_back(pNewNode)

            m_dwcurLineIndex += 1

            LoadGroup(pNewNode)
        elif 0 == stTokenVector[0].compare("list"):
            if 2 != len(stTokenVector):
                assert not "There is no list name!"
                continue

            stSubTokenVector = []

            stl_lowers(stTokenVector[1])
            key = stTokenVector[1]
            stTokenVector.clear()

            m_dwcurLineIndex += 1
            while m_dwcurLineIndex < m_fileLoader.GetLineCount():
                if not m_fileLoader.SplitLine(m_dwcurLineIndex, stSubTokenVector):
                    continue

                if '{' == stSubTokenVector[0][0]:
                    continue

                if '}' == stSubTokenVector[0][0]:
                    break

                j = 0
                while j < len(stSubTokenVector):
                    stTokenVector.append(stSubTokenVector[j])
                    j += 1
                m_dwcurLineIndex += 1

            pGroupNode.LocalTokenVectorMap.insert((key, stTokenVector))
        else:
            key = stTokenVector[0]

            if 1 == len(stTokenVector):
                #lani_err("CTextFileLoader::LoadGroup : must have a value (filename: %s line: %d key: %s)", m_strFileName.c_str(), m_dwcurLineIndex, key)
                break

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no direct equivalent to the STL vector 'erase' method in Python:
            stTokenVector.erase(stTokenVector.begin())
            pGroupNode.LocalTokenVectorMap.insert((key, stTokenVector))
        m_dwcurLineIndex += 1

    return ((not DefineConstants.false))

