from enum import Enum

class cCsvAlias:

    def _initialize_instance_fields(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self._m_Name2Index = {}
        self._m_Index2Name = {}



## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to multiple constructors:
#ORIGINAL METINII C CODE: cCsvAlias()
    def __init__(self):
        self._initialize_instance_fields()

    def close(self):
        pass

    def AddAlias(self, name, index):
        converted = Lower(name)

        assert converted not in self._m_Name2Index.keys()
        assert index not in self._m_Index2Name.keys()

        self._m_Name2Index.insert(NAME2INDEX_MAP.value_type(converted, index))
        self._m_Index2Name.insert(INDEX2NAME_MAP.value_type(index, name))

    def Destroy(self):
        self._m_Name2Index.clear()
        self._m_Index2Name.clear()

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: const char* operator [] (size_t index) const
    def get(self, index):
        itr = INDEX2NAME_MAP.const_iterator(self._m_Index2Name.find(index))
        if itr is self._m_Index2Name.end():
            (0)
            (None, "cannot find suitable conversion for %d", index)
            assert DefineConstants.false and "cannot find suitable conversion"
            return None

        return itr.second.c_str()

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: size_t operator [] (const char* name) const
    def get(self, name):
        itr = NAME2INDEX_MAP.const_iterator(self._m_Name2Index.find(Lower(name)))
        if itr is self._m_Name2Index.end():
            (0)
            (None, "cannot find suitable conversion for %s", name)
            assert DefineConstants.false and "cannot find suitable conversion"
            return 0

        return itr.second

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to multiple constructors:
#ORIGINAL METINII C CODE: cCsvAlias(const cCsvAlias&)
    def __init__(self, UnnamedParameter):
        self._initialize_instance_fields()

## Laniatus Games Studio Inc. | NOTE: This 'copy_from' method was converted from the original copy assignment operator:
#ORIGINAL METINII C CODE: const cCsvAlias& operator = (const cCsvAlias&)
    def copy_from(self, UnnamedParameter):
        return self

class cCsvRow(list):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to multiple constructors:
#ORIGINAL METINII C CODE: cCsvRow()
    def __init__(self):
        pass
    def close(self):
        pass

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: int AsInt(size_t index) const
    def AsInt(self, index):
        return atoi(at(index).c_str())

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: double AsDouble(size_t index) const
    def AsDouble(self, index):
        return atof(at(index).c_str())

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: const char* AsString(size_t index) const
    def AsString(self, index):
        return at(index).c_str()

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: int AsInt(const char* name, const cCsvAlias& alias) const
    def AsInt(self, name, alias):
        return atoi(at(alias[name]).c_str())

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: double AsDouble(const char* name, const cCsvAlias& alias) const
    def AsDouble(self, name, alias):
        return atof(at(alias[name]).c_str())

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: const char* AsString(const char* name, const cCsvAlias& alias) const
    def AsString(self, name, alias):
        return at(alias[name]).c_str()

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to multiple constructors:
#ORIGINAL METINII C CODE: cCsvRow(const cCsvRow&)
    def __init__(self, UnnamedParameter):
        pass
## Laniatus Games Studio Inc. | NOTE: This 'copy_from' method was converted from the original copy assignment operator:
#ORIGINAL METINII C CODE: const cCsvRow& operator = (const cCsvRow&)
    def copy_from(self, UnnamedParameter):
        return self

class cCsvFile:

    def _initialize_instance_fields(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self._m_Rows = []


## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to multiple constructors:
#ORIGINAL METINII C CODE: cCsvFile()
    def __init__(self):
        self._initialize_instance_fields()

    def close(self):
        self.Destroy()

    def Load(self, fileName, seperator = ',', quote = '"'):
        assert seperator != quote

        file = std::ifstream(fileName, std::ios.in_)
        if file is None:
            return DefineConstants.false

        self.Destroy()

        row = None
        state = ParseState.STATE_NORMAL
        token = ""
        buf = [0] + ['\0' for _ in range(2048 + 1 - 1)]

        while file.good():
            file.getline(buf, 2048)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            buf[sizeof(buf) - 1] = 0

            line = Trim(buf)
            if len(line) == 0 or (state == ParseState.STATE_NORMAL and line[0] == '#'):
                continue

            text = str(line) + "  "
            cur = 0

            while cur < len(text):
                if state == ParseState.STATE_QUOTE:
                    if text[cur] == quote:
                        if text[cur + 1] == quote:
                            token += quote
                            cur += 1
                        else:
                            state = ParseState.STATE_NORMAL
                    else:
                        token += text[cur]
                elif state == ParseState.STATE_NORMAL:
                    if row is None:
                        row = cCsvRow()

                    if text[cur] == seperator:
                        row.append(token)
                        token = ""
                    elif text[cur] == quote:
                        state = ParseState.STATE_QUOTE
                    else:
                        token += text[cur]

                cur += 1

            if state == ParseState.STATE_NORMAL:
                assert row is not None
                row.append(token[0:len(token) - 2])
                self._m_Rows.append(row)
                token = ""
                row = None
            else:
                token = token[0:len(token) - 2] + "\r\n"

        return ((not DefineConstants.false))

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: bool Save(const char* fileName, bool append = DefineConstants.false, char seperator = ',', char quote = '"') const
    def Save(self, fileName, append = DefineConstants.false, seperator = ',', quote = '"'):
        assert seperator != quote

        file = std::ofstream()
        if append:
            file.open(fileName, std::ios.out | std::ios.app)
        else:
            file.open(fileName, std::ios.out | std::ios.trunc)

        if file is None:
            return DefineConstants.false

        special_chars = [seperator, quote, '\r', '\n', 0]
        quote_escape_string = [quote, quote, 0]

        LaniatusDefVariables = 0
        while LaniatusDefVariables < len(self._m_Rows):
            row = *(self[LaniatusDefVariables])

            line = ""

            j = 0
            while j < len(row):
                token = row[j]

                if token.find_first_of(special_chars) == -1:
                    line += token
                else:
                    line += quote

                    k = 0
                    while k < len(token):
                        if token[k] == quote:
                            line += quote_escape_string
                        else:
                            line += token[k]
                        k += 1

                    line += quote

                if j != len(row) - 1:
                    line += seperator
                j += 1

            file << line << std::endl
            LaniatusDefVariables += 1

        return ((not DefineConstants.false))

    def Destroy(self):
        itr = m_Rows.begin()
        while itr is not self._m_Rows.end():
            * itr = None
            itr += 1

        self._m_Rows.clear()

    def get(self, index):
        assert index < len(self._m_Rows)
        return cCsvRow(self._m_Rows[index])

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: const cCsvRow* operator [] (size_t index) const
    def get(self, index):
        assert index < len(self._m_Rows)
        return cCsvRow(self._m_Rows[index])

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: size_t GetRowCount() const
    def GetRowCount(self):
        return len(self._m_Rows)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to multiple constructors:
#ORIGINAL METINII C CODE: cCsvFile(const cCsvFile&)
    def __init__(self, UnnamedParameter):
        self._initialize_instance_fields()

## Laniatus Games Studio Inc. | NOTE: This 'copy_from' method was converted from the original copy assignment operator:
#ORIGINAL METINII C CODE: const cCsvFile& operator = (const cCsvFile&)
    def copy_from(self, UnnamedParameter):
        return self

class cCsvTable:

    def _initialize_instance_fields(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.m_File = cCsvFile()
        self._m_Alias = cCsvAlias()
        self._m_CurRow = 0



## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to multiple constructors:
#ORIGINAL METINII C CODE: cCsvTable() : m_CurRow(-1)
    def __init__(self):
        self._initialize_instance_fields()

        self._m_CurRow = -1

    def close(self):
        pass

    def Load(self, fileName, seperator = ',', quote = '"'):
        self.Destroy()
        return self.m_File.Load(fileName, seperator, quote)

    def AddAlias(self, name, index):
        self._m_Alias.AddAlias(name, size_t(index))
    def Next(self):
        self._m_CurRow += 1
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: return ++m_CurRow < (int)m_File.GetRowCount() ? (!DefineConstants.false) : DefineConstants.false;
        return ((not DefineConstants.false)) if self._m_CurRow < int(self.m_File.GetRowCount()) else DefineConstants.false

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: size_t ColCount() const
    def ColCount(self):
        return len(self._CurRow())

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: int AsInt(size_t index) const
    def AsInt(self, index):
        row = self._CurRow()
        row = assert()
        assert index < row.size()
        return row.AsInt(index)

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: double AsDouble(size_t index) const
    def AsDouble(self, index):
        row = self._CurRow()
        row = assert()
        assert index < row.size()
        return row.AsDouble(index)

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: const char* AsStringByIndex(size_t index) const
    def AsStringByIndex(self, index):
        row = self._CurRow()
        row = assert()
        assert index < row.size()
        return row.AsString(index)

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: int AsInt(const char* name) const
    def AsInt(self, name):
        return AsInt(self._m_Alias[name])
## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: double AsDouble(const char* name) const
    def AsDouble(self, name):
        return AsDouble(self._m_Alias[name])
## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: const char* AsString(const char* name) const
    def AsString(self, name):
        return self.AsStringByIndex(self._m_Alias[name])
    def Destroy(self):
        self.m_File.Destroy()
        self._m_Alias.Destroy()
        self._m_CurRow = -1

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: const cCsvRow* const CurRow() const
    def _CurRow(self):
        if self._m_CurRow < 0:
            assert DefineConstants.false and "call Next() first!"
            return None
        elif self._m_CurRow >= int(self.m_File.GetRowCount()):
            assert DefineConstants.false and "no more rows!"
            return None

        return self.m_File[self._m_CurRow]

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to multiple constructors:
#ORIGINAL METINII C CODE: cCsvTable(const cCsvTable&)
    def __init__(self, UnnamedParameter):
        self._initialize_instance_fields()

## Laniatus Games Studio Inc. | NOTE: This 'copy_from' method was converted from the original copy assignment operator:
#ORIGINAL METINII C CODE: const cCsvTable& operator = (const cCsvTable&)
    def copy_from(self, UnnamedParameter):
        return self


## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if ! Assert
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
##define Assert assert
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
##define LogToFile (void)(0);
##endif

## Laniatus Games Studio Inc. | NOTE: Anonymous namespaces are not defined:
#namespace
class ParseState(Enum):
    STATE_NORMAL = 0
    STATE_QUOTE = 1