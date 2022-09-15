class CMemoryTextFileLoader:
    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.m_stLineVector = []


    def close(self):
        pass

    def Bind(self, bufSize, c_pvBuf):
        self.m_stLineVector.clear()

        c_pcBuf = str(c_pvBuf)
        stLine = ""
        pos = 0

        while pos < bufSize:
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: const char c = c_pcBuf[pos++];
            c = c_pcBuf[pos]
            pos += 1

            if '\n' == c or '\r' == c:
                if pos < bufSize:
                    if '\n' == c_pcBuf[pos] or '\r' == c_pcBuf[pos]:
                        pos += 1

                self.m_stLineVector.append(stLine)
                stLine = ""
            elif c < 0:
                stLine.append(c_pcBuf + (pos-1), 2)
                pos += 1
            else:
                stLine += c

        self.m_stLineVector.append(stLine)

    def GetLineCount(self):
        return len(self.m_stLineVector)

    def CheckLineIndex(self, dwLine):
        if dwLine >= len(self.m_stLineVector):
            return DefineConstants.false

        return ((not DefineConstants.false))

    def SplitLine(self, dwLine, pstTokenVector, c_szDelimeter = " \t"):
        pstTokenVector.clear()

        stToken = ""
        c_rstLine = self.GetLineString(dwLine)

        basePos = 0

        condition = True
        while condition:
            beginPos = c_rstLine.find_first_not_of(c_szDelimeter, basePos)
            if beginPos < 0:
                return DefineConstants.false

            endPos = None

            if c_rstLine[beginPos] == '#' and c_rstLine.compare(beginPos, 4, "#--#") != 0:
                return DefineConstants.false
            elif c_rstLine[beginPos] == '"':
                beginPos += 1
                endPos = c_rstLine.find_first_of("\"", beginPos)

                if endPos < 0:
                    return DefineConstants.false

                basePos = uint(endPos + 1)
            else:
                endPos = c_rstLine.find_first_of(c_szDelimeter, beginPos)
                basePos = uint(endPos)

            pstTokenVector.append(c_rstLine[beginPos:endPos])

            if int(c_rstLine.find_first_not_of(c_szDelimeter, basePos)) < 0:
                break
            condition = basePos < len(c_rstLine)

        return ((not DefineConstants.false))

    def GetLineString(self, dwLine):
        CheckLineIndex = assert(dwLine)
        return self.m_stLineVector[dwLine]


