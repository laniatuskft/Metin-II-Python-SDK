from enum import Enum

#Laniatus Games Studio Inc. | Python Metin II Server Warnings Statement interrupted by a preprocessor statement:
#The original statement from the file sal.h starts with:
#    __inner_fallthrough_dec
#Preprocessor-interrupted statements cannot be handled by this converter.
#The remainder of the header file sal.h is ignored.

class cCsvAlias:


    def __init__(self):
        pass
    def close(self):
        pass

    def AddAlias(self, name, index):
        converted = Lower(name)

        assert m_Name2Index.find(converted) == m_Name2Index.end()
        assert m_Index2Name.find(index) == m_Index2Name.end()

        m_Name2Index.insert(NAME2INDEX_MAP.value_type(converted, index))
        m_Index2Name.insert(INDEX2NAME_MAP.value_type(index, name))

    def Destroy(self):
        m_Name2Index.clear()
        m_Index2Name.clear()

#Laniatus Games Studio Inc. | Python Metin II Server Warnings 'const' methods are not available in Python:
#ORIGINAL LINE: const char* operator [] (size_t index) const
    def get(self, index):
        itr = INDEX2NAME_MAP.const_iterator(m_Index2Name.find(index))
        if itr is m_Index2Name.end():
            (0)
            (None, "cannot find suitable conversion for %d", index)
            assert DefineConstants.false and "cannot find suitable conversion"
            return None

        return itr.second.c_str()

#Laniatus Games Studio Inc. | Python Metin II Server Warnings 'const' methods are not available in Python:
#ORIGINAL LINE: size_t operator [] (const char* name) const
    def get(self, name):
        itr = NAME2INDEX_MAP.const_iterator(m_Name2Index.find(Lower(name)))
        if itr is m_Name2Index.end():
            (0)
            (None, "cannot find suitable conversion for %s", name)
            assert DefineConstants.false and "cannot find suitable conversion"
            return 0

        return itr.second

    def __init__(self, UnnamedParameter):
        pass
#Laniatus Games Studio Inc. | Python Metin II Server Note This 'copy_from' method was converted from the original copy assignment operator:
#ORIGINAL LINE: const cCsvAlias& operator = (const cCsvAlias&)
    def copy_from(self, UnnamedParameter):
        return self

class cCsvRow(list):
    def __init__(self):
        pass
    def close(self):
        pass

#Laniatus Games Studio Inc. | Python Metin II Server Warnings 'const' methods are not available in Python:
#ORIGINAL LINE: int AsInt(size_t index) const
    def AsInt(self, index):
        return atoi(at(index).c_str())
#Laniatus Games Studio Inc. | Python Metin II Server Warnings 'const' methods are not available in Python:
#ORIGINAL LINE: double AsDouble(size_t index) const
    def AsDouble(self, index):
        return atof(at(index).c_str())
#Laniatus Games Studio Inc. | Python Metin II Server Warnings 'const' methods are not available in Python:
#ORIGINAL LINE: const char* AsString(size_t index) const
    def AsString(self, index):
        return at(index).c_str()

#Laniatus Games Studio Inc. | Python Metin II Server Warnings 'const' methods are not available in Python:
#ORIGINAL LINE: int AsInt(const char* name, const cCsvAlias& alias) const
    def AsInt(self, name, alias):
        return atoi(at(alias[name]).c_str())

#Laniatus Games Studio Inc. | Python Metin II Server Warnings 'const' methods are not available in Python:
#ORIGINAL LINE: double AsDouble(const char* name, const cCsvAlias& alias) const
    def AsDouble(self, name, alias):
        return atof(at(alias[name]).c_str())

#Laniatus Games Studio Inc. | Python Metin II Server Warnings 'const' methods are not available in Python:
#ORIGINAL LINE: const char* AsString(const char* name, const cCsvAlias& alias) const
    def AsString(self, name, alias):
        return at(alias[name]).c_str()

    def __init__(self, UnnamedParameter):
        pass
#Laniatus Games Studio Inc. | Python Metin II Server Note This 'copy_from' method was converted from the original copy assignment operator:
#ORIGINAL LINE: const cCsvRow& operator = (const cCsvRow&)
    def copy_from(self, UnnamedParameter):
        return self

class cCsvFile:

    def __init__(self):
        pass
    def close(self):
        Destroy()

    def Load(self, fileName, seperator = ',', quote = '"'):
        assert seperator != quote

        file = std::ifstream(fileName, std::ios.in_)
        if file is None:
            return DefineConstants.false

        Destroy()

        row = None
        state = STATE_NORMAL
        token = ""
        buf = [0] + ['\0' for _ in range(2048+1 - 1)]

        while file.good():
            file.getline(buf, 2048)
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
            buf[sizeof(buf)-1] = 0

            line = Trim(buf)
            if len(line) == 0 or (state is STATE_NORMAL and line[0] == '#'):
                continue

            text = str(line) + "  "
            cur = 0

            while cur < len(text):
                if state is STATE_QUOTE:
                    if text[cur] == quote:
                        if text[cur+1] == quote:
                            token += quote
                            cur += 1
                        else:
                            state = STATE_NORMAL
                    else:
                        token += text[cur]
                elif state is STATE_NORMAL:
                    if row is None:
                        row = cCsvRow()

                    if text[cur] == seperator:
                        row.push_back(token)
                        token = ""
                    elif text[cur] == quote:
                        state = STATE_QUOTE
                    else:
                        token += text[cur]

                cur += 1

            if state is STATE_NORMAL:
                assert row is not None
                row.push_back(token[0:len(token)-2])
                m_Rows.push_back(row)
                token = ""
                row = None
            else:
                token = token[0:len(token)-2] + "\r\n"

        return ((not DefineConstants.false))

#Laniatus Games Studio Inc. | Python Metin II Server Warnings 'const' methods are not available in Python:
#ORIGINAL LINE: bool Save(const char* fileName, bool append =DefineConstants.false, char seperator =',', char quote ='"') const
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

        i = 0
        while i<m_Rows.size():
            row = *(self[i])
            line = ""

            j = 0
            while j<row.size():
                token = row[j]

                if token.find_first_of(special_chars) == -1:
                    line += token
                else:
                    line += quote

                    k = 0
                    while k<len(token):
                        if token[k] == quote:
                            line += quote_escape_string
                        else:
                            line += token[k]
                        k += 1

                    line += quote
                if j is not row.size() - 1:
                    line += seperator
                j += 1
            file << line << std::endl
            i += 1

        return ((not DefineConstants.false))

    def Destroy(self):
        itr = m_Rows.begin()
        while itr is not m_Rows.end():
            *itr = None
            itr += 1

        m_Rows.clear()

    def get(self, index):
        assert index < m_Rows.size()
        return m_Rows[index]

#Laniatus Games Studio Inc. | Python Metin II Server Warnings 'const' methods are not available in Python:
#ORIGINAL LINE: const cCsvRow* operator [] (size_t index) const
    def get(self, index):
        assert index < m_Rows.size()
        return m_Rows[index]

#Laniatus Games Studio Inc. | Python Metin II Server Warnings 'const' methods are not available in Python:
#ORIGINAL LINE: size_t GetRowCount() const
    def GetRowCount(self):
        return m_Rows.size()

    def __init__(self, UnnamedParameter):
        pass
#Laniatus Games Studio Inc. | Python Metin II Server Note This 'copy_from' method was converted from the original copy assignment operator:
#ORIGINAL LINE: const cCsvFile& operator = (const cCsvFile&)
    def copy_from(self, UnnamedParameter):
        return self

class cCsvTable:


    def __init__(self):
        self.m_CurRow = -1

    def close(self):
        pass

    def Load(self, fileName, seperator = ',', quote = '"'):
        Destroy()
        return m_File.Load(fileName, seperator, quote)

    def AddAlias(self, name, index):
        m_Alias.AddAlias(name, index)
    def Next(self):
        m_CurRow += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: return ++m_CurRow < (int)m_File.GetRowCount() ? (!DefineConstants.false) : DefineConstants.false;
        return ((not DefineConstants.false)) if m_CurRow < int(m_File.GetRowCount()) else DefineConstants.false

#Laniatus Games Studio Inc. | Python Metin II Server Warnings 'const' methods are not available in Python:
#ORIGINAL LINE: size_t ColCount() const
    def ColCount(self):
        return CurRow().size()

#Laniatus Games Studio Inc. | Python Metin II Server Warnings 'const' methods are not available in Python:
#ORIGINAL LINE: int AsInt(size_t index) const
    def AsInt(self, index):
        row = CurRow()
        row = assert()
        assert index < row.size()
        return row.AsInt(index)

#Laniatus Games Studio Inc. | Python Metin II Server Warnings 'const' methods are not available in Python:
#ORIGINAL LINE: double AsDouble(size_t index) const
    def AsDouble(self, index):
        row = CurRow()
        row = assert()
        assert index < row.size()
        return row.AsDouble(index)

#Laniatus Games Studio Inc. | Python Metin II Server Warnings 'const' methods are not available in Python:
#ORIGINAL LINE: const char* AsStringByIndex(size_t index) const
    def AsStringByIndex(self, index):
        row = CurRow()
        row = assert()
        assert index < row.size()
        return row.AsString(index)

#Laniatus Games Studio Inc. | Python Metin II Server Warnings 'const' methods are not available in Python:
#ORIGINAL LINE: int AsInt(const char* name) const
    def AsInt(self, name):
        return AsInt(m_Alias[name])
#Laniatus Games Studio Inc. | Python Metin II Server Warnings 'const' methods are not available in Python:
#ORIGINAL LINE: double AsDouble(const char* name) const
    def AsDouble(self, name):
        return AsDouble(m_Alias[name])
#Laniatus Games Studio Inc. | Python Metin II Server Warnings 'const' methods are not available in Python:
#ORIGINAL LINE: const char* AsString(const char* name) const
    def AsString(self, name):
        return AsStringByIndex(m_Alias[name])
    def Destroy(self):
        m_File.Destroy()
        m_Alias.Destroy()
        m_CurRow = -1

#Laniatus Games Studio Inc. | Python Metin II Server Warnings 'const' methods are not available in Python:
#ORIGINAL LINE: const cCsvRow* const CurRow() const
    def CurRow(self):
        if m_CurRow < 0:
            assert DefineConstants.false and "call Next() first!"
            return None
        elif m_CurRow >= int(m_File.GetRowCount()):
            assert DefineConstants.false and "no more rows!"
            return None

        return m_File[m_CurRow]

    def __init__(self, UnnamedParameter):
        pass
#Laniatus Games Studio Inc. | Python Metin II Server Note This 'copy_from' method was converted from the original copy assignment operator:
#ORIGINAL LINE: const cCsvTable& operator = (const cCsvTable&)
    def copy_from(self, UnnamedParameter):
        return self

##define Assert assert
##define LogToFile (void)(0);

#Laniatus Games Studio Inc. | Python Metin II Server Note Anonymous namespaces are not converted:
#namespace
class ParseState(Enum):
    STATE_NORMAL = 0
    STATE_QUOTE = 1