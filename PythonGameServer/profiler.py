class CProfiler(singleton):
    STACK_DATA_MAX_NUM = 64

    class SProfileStackData:

        def __init__(self):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.iCallStep = 0
            self.iStartTime = 0
            self.iEndTime = 0
            self.strName = ""



    class SProfileAccumData:

        def __init__(self):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.iStartTime = 0
            self.iCallingCount = 0
            self.iCollapsedTime = 0
            self.iDepth = 0
            self.strName = ""



    class stringhash:
## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: size_t operator ()(const str& str) const
        def functor_method(self, str):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Pointer arithmetic is detected on this variable:
#ORIGINAL METINII C CODE: const byte * s = (const byte *) str.c_str();
            s = byte(int(str))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to pointers to value types:
#ORIGINAL METINII C CODE: const byte * end = s + str.size();
            end = byte(s + len(str))
            h = 0

            while s < end:
                h *= 16777619
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: h ^= (byte) *(byte *)(s++);
                h ^= (byte) *int((s))
                s += 1

            return size_t(h)



    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.m_ProfileStackDataCount = 0
        self.m_ProfileStackDatas = [SProfileStackData() for _ in range(STACK_DATA_MAX_NUM)]
        self.m_ProfileAccumDataMap = boost.unordered_map()
        self.m_vec_Accum = []
        self.m_iAccumDepth = 0
        self.m_iCallStep = 0

        self.Initialize()

    def close(self):
        pass

    def Initialize(self):
        self.m_iAccumDepth = 0
        self.m_ProfileStackDataCount = 0
        self.m_iCallStep = 0

    def Clear(self):
        it = self.m_ProfileAccumDataMap.begin()

        while it is not self.m_ProfileAccumDataMap.end():
            rData = it.second
            rData.iCallingCount = 0
            rData.iCollapsedTime = 0
            it += 1

        self.Initialize()

    def Push(self, c_szName):
        assert self.m_ProfileStackDataCount < STACK_DATA_MAX_NUM
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: SProfileStackData & rProfileStackData = m_ProfileStackDatas[m_ProfileStackDataCount++];
        rProfileStackData = self.m_ProfileStackDatas[self.m_ProfileStackDataCount]
        self.m_ProfileStackDataCount += 1

        rProfileStackData.iCallStep = self.m_iCallStep
        rProfileStackData.iStartTime = get_dword_time()
        rProfileStackData.strName = c_szName

        self.m_iCallStep += 1

    def Pop(self, c_szName):
        pProfileStackData = None

        if not self.GetProfileStackDataPointer(c_szName, pProfileStackData):
            assert not "The name doesn't exist"
            return

        pProfileStackData.iEndTime = get_dword_time()
        self.m_iCallStep -= 1

    def PushAccum(self, c_szName):
        it = self.m_ProfileAccumDataMap.find(c_szName)

        if it == self.m_ProfileAccumDataMap.end():
            ProfileAccumData = SProfileAccumData()

            ProfileAccumData.iCollapsedTime = 0
            ProfileAccumData.iCallingCount = 0
            ProfileAccumData.strName = c_szName
            ProfileAccumData.iDepth = self.m_iAccumDepth

            self.m_ProfileAccumDataMap.insert(boost.unordered_map.value_type(c_szName, ProfileAccumData))
            it = self.m_ProfileAccumDataMap.find(c_szName)
            self.m_vec_Accum.append(it.second)

        rData = it.second
        rData.iStartTime = get_dword_time()
        self.m_iAccumDepth += 1

    def PopAccum(self, c_szName):
        it = self.m_ProfileAccumDataMap.find(c_szName)

        if it == self.m_ProfileAccumDataMap.end():
            return

        rData = it.second
        rData.iCollapsedTime += get_dword_time() - rData.iStartTime
        rData.iCallingCount += 1
        self.m_iAccumDepth -= 1

    def Log(self, c_pszFileName):
        fp = fopen(c_pszFileName, "w")

        if fp is None:
            return

        self.Print(fp)
        fclose(fp)

    def Print(self, fp = stderr):
        i = 0
        while i < self.m_ProfileStackDataCount:
            rProfileStackData = self.m_ProfileStackDatas[i]

            i = 0
            while i < rProfileStackData.iCallStep:
                fprintf(fp, "\t")
                i += 1

            fprintf(fp, "%-24s: %lu\n", rProfileStackData.strName, rProfileStackData.iEndTime - rProfileStackData.iStartTime)
            i += 1

        fprintf(fp, "Name                                 Call/Load       Ratio\n")

        stLine = ""

        k = 0
        while k < len(self.m_vec_Accum):
            p = self.m_vec_Accum[k]

            stLine.assign(p.iDepth * 5, ' ')
            stLine += p.strName

            fprintf(fp, "%-30s %10d/%-10d %.2f\n", stLine, p.iCallingCount, p.iCollapsedTime,float(p.iCollapsedTime) / p.iCallingCount if p.iCallingCount != 0 else 0.0)
            k += 1

    def PrintOneStackData(self, c_szName):
        pProfileStackData = None

        if not self.GetProfileStackDataPointer(c_szName, pProfileStackData):
            return

        #sys_log(0, "%-10s: %3d", pProfileStackData.strName, pProfileStackData.iEndTime - pProfileStackData.iStartTime)

    def PrintOneAccumData(self, c_szName):
        it = self.m_ProfileAccumDataMap.find(c_szName)

        if it == self.m_ProfileAccumDataMap.end():
            return

        rData = it.second

        #sys_log(0, "%-10s : [CollapsedTime : %3d] / [CallingCount : %3d]", rData.strName, rData.iCollapsedTime, rData.iCallingCount)

    def GetProfileStackDataPointer(self, c_szName, ppProfileStackData):
        i = 0
        while i < self.m_ProfileStackDataCount:
            if 0 == self.m_ProfileStackDatas[i].strName.compare(c_szName):
## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: *ppProfileStackData = &m_ProfileStackDatas[i];
                ppProfileStackData[0].copy_from(self.m_ProfileStackDatas[i])

                return True
            i += 1

        return False




class CProfileUnit:
    def __init__(self, c_pszName):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.m_stName = ""
        self.m_bPushed = False

        self.m_stName = c_pszName
        CProfiler.instance().PushAccum(self.m_stName)
        self.m_bPushed = True

    def close(self):
        if self.m_bPushed:
            self.Pop()

    def Pop(self):
        if self.m_bPushed:
            CProfiler.instance().PopAccum(self.m_stName)
            self.m_bPushed = False


## Laniatus Games Studio Inc. | NOTE: The following #define macro was replaced in-line:
#ORIGINAL METINII C CODE: #define PROF_UNIT CProfileUnit<void>
