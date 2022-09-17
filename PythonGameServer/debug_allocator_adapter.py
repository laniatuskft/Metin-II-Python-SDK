##define DBGALLOC_NO_STACKTRACE
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if ! DBGALLOC_NO_STACKTRACE
## Laniatus Games Studio Inc. | WARNING: The following #include directive was ignored:
##include <execinfo.h>
##endif

class AllocTag:
    def __init__(self, file, line):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.in_use = False
        self.file = '\0'
        self.line = size_t()
        self.age = size_t()

        self.in_use = True
        self.age = 1
        self.file = file
## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: this->line = line;
        self.line.copy_from(line)
    def Reuse(self, file, line):
        self.in_use = True
        self.file = file
## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: this->line = line;
        self.line.copy_from(line)
## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: age = IncreaseAge(age);
        self.age.copy_from(AllocTag.IncreaseAge(size_t(self.age)))
    def Unuse(self, file, line):
        self.in_use = False
        self.file = file
## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: this->line = line;
        self.line.copy_from(line)
## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: age = IncreaseAge(age);
        self.age.copy_from(AllocTag.IncreaseAge(size_t(self.age)))
    @staticmethod
    def IncreaseAge(value):
        result = size_t(value)
        result += 1
        if result == 0:
            result = 1
        return size_t(result)

class ScopedOutputFile:
    def __init__(self, filename, mode = std::ios_base.app):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.stream = std::ofstream()

        self.stream.open(filename, mode)
    def close(self):
        if self.stream.is_open():
            self.stream.close()
    def Datetime(self):
        buf = str(['\0' for _ in range(24)])
        t = time(None)
        strftime(buf, 24, "%Y-%m-%d %H:%M:%S", localtime(t))
        return self.stream << buf

## Laniatus Games Studio Inc. | NOTE: Python has no need of forward class declarations:
#class DebugPtr

class DebugAllocatorAdapter:
    def close(self):
        pass

    @staticmethod
    def StaticSetUp():
        DebugAllocatorAdapter._GetInstance()._detail_.SetUp()

    @staticmethod
    def StaticTearDown():
        instance = DebugAllocatorAdapter._GetInstance()
        instance._DumpLeakReport()
        instance._detail_.TearDown()

    @staticmethod
    def Alloc(size):
        return DebugAllocatorAdapter._GetInstance()._detail_.Alloc(size)

    @staticmethod
    def Free(p):
        DebugAllocatorAdapter._GetInstance()._detail_.Free(p)

    @staticmethod
    def MarkAcquired(p, file, line, context):
        if p is None:
            return 0
        alloc_map = DebugAllocatorAdapter._GetInstance()._alloc_map_
        age = 0
        it = alloc_map.find(p)
        if it == alloc_map.end():
            tag = AllocTag(file, line)
            alloc_map.insert(AllocMapType.value_type(p, tag))
## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: age = tag.age;
            age.copy_from(tag.age)
        else:
            tag = it.second
            if not tag.in_use:
                tag.Reuse(file, size_t(line))
## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: age = tag.age;
                age.copy_from(tag.age)
            else:
                of = ScopedOutputFile(DefineConstants.DBGALLOC_LOG_FILENAME, std::ios_base.app)
                if of.stream.is_open():
                    of.Datetime() << " [" << context << "] " << p << " " << tag << " already in use. " << "(" << file << " line:" << line << ")" << std::endl
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if ! DBGALLOC_NO_STACKTRACE
                    self._PrintStack(of.stream)
##endif
        return size_t(age)

    @staticmethod
    def MarkReleased(p, file, line, context):
        return (p if DebugAllocatorAdapter._GetInstance()._VerifyReference(p, file, size_t(line), context, True, False, 0) else None)
    @staticmethod
    def MarkReleased(ptr, file, line, context):
        return (ptr.Get() if DebugAllocatorAdapter._GetInstance()._VerifyReference(ptr.Get(), file, size_t(line), context, True, True, ptr.GetAge()) else None)

    @staticmethod
    def RetrieveAge(p):
        if p is None:
            return 0
        alloc_map = DebugAllocatorAdapter._GetInstance()._alloc_map_
        it = alloc_map.find(p)
        if it != alloc_map.end():
            tag = it.second
            if tag.in_use:
                return size_t(tag.age)
        return 0

    @staticmethod
    def Verify(p, age, file = None, line = 0):
        return (p if DebugAllocatorAdapter._GetInstance()._VerifyReference(p, file, size_t(line), "ref", False, True, size_t(age)) else None)

    @staticmethod
    def VerifyDeletion(p, file, line, verify_age = False, age = 0):
        return (p if DebugAllocatorAdapter._GetInstance()._VerifyReference(p, file, size_t(line), "pre_delete", False, verify_age, size_t(age)) else None)

    @staticmethod
    def LogBoundaryCorruption(p, age):
        alloc_map = DebugAllocatorAdapter._GetInstance()._alloc_map_
        it = alloc_map.find(p)
        if it != alloc_map.end():
            tag = it.second
            of = ScopedOutputFile(DefineConstants.DBGALLOC_LOG_FILENAME, std::ios_base.app)
            if of.stream.is_open():
                of.Datetime() << " [boundary] " << p << " " << tag << " age header corrupted:" << " current age value " << age << std::endl
                self._PrintStack(of.stream)

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self._detail_ = None
        self._alloc_map_ = boost.unordered_map()


    ## Laniatus Games Studio Inc. | NOTE: This was formerly a static local variable declaration (not allowed in Python):
    GetInstance_instance = DebugAllocatorAdapter()

    @staticmethod
    def _GetInstance():
        ## Laniatus Games Studio Inc. | NOTE: This static local variable declaration (not allowed in Python) has been moved just prior to the method:
        #        static DebugAllocatorAdapter instance
        return _GetInstance_instance

    def _VerifyReference(self, p, file, line, context, mark_released, verify_age = False, age = 0):
        if p is None:
            return mark_released
        it = self._alloc_map_.find(p)
        if it != self._alloc_map_.end():
            tag = it.second
            if tag.in_use:
                if verify_age and tag.age is not age:
                    of = ScopedOutputFile(DefineConstants.DBGALLOC_LOG_FILENAME, std::ios_base.app)
                    if of.stream.is_open():
                        of.Datetime() << " [" << context << "] " << p << " " << tag << " has different age with " << age << " (" << file << " line:" << line << ")" << std::endl
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if ! DBGALLOC_NO_STACKTRACE
                        self._PrintStack(of.stream)
##endif
                else:
                    if mark_released:
                        tag.Unuse(file, size_t(line))
                    return True
            else:
                of = ScopedOutputFile(DefineConstants.DBGALLOC_LOG_FILENAME, std::ios_base.app)
                if of.stream.is_open():
                    of.Datetime() << " [" << context << "] " << p << " " << tag << " already freed. " << "(" << file << " line:" << line << ")" << std::endl
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if ! DBGALLOC_NO_STACKTRACE
                    self._PrintStack(of.stream)
##endif
        else:
            of = ScopedOutputFile(DefineConstants.DBGALLOC_LOG_FILENAME, std::ios_base.app)
            if of.stream.is_open():
                of.Datetime() << " [" << context << "] " << p << " is not a valid entry. " << "(" << file << " line:" << line << ")" << std::endl
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if ! DBGALLOC_NO_STACKTRACE
                self._PrintStack(of.stream)
##endif
        return False

    def _DumpLeakReport(self):
        it = self._alloc_map_.begin()
        end = self._alloc_map_.end()
        while it is not end:
            if it.second.in_use:
                break
            it += 1
        if it is end:
            return
        of = ScopedOutputFile(DefineConstants.DBGALLOC_REPORT_FILENAME, std::ios_base.app)
        if not of.stream.is_open():
            return
        of.Datetime() << std::endl
        while it is not end:
            tag = it.second
            if tag.in_use:
                of.stream << "[leak] " << it.first << " " << tag << std::endl
            it += 1

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if ! DBGALLOC_NO_STACKTRACE
    def _PrintStack(self, out):
        array = [None for _ in range(200)]
        size = None
        symbols = []

        size = backtrace(array, 200)
        symbols = backtrace_symbols(array, size)

        out << std::endl

        for LaniatusDefVariables in range(0, size):
            out << "Stack> " << symbols[LaniatusDefVariables] << std::endl

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'free' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
        free(symbols)
##endif


