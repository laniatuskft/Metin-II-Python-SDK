#Laniatus Games Studio Inc. | Python Metin II Server Warnings Statement interrupted by a preprocessor statement:
#The original statement from the file sal.h starts with:
#    __inner_fallthrough_dec
#Preprocessor-interrupted statements cannot be handled by this converter.
#The remainder of the header file sal.h is ignored.


class CConfig(singleton):
    def __init__(self):
        pass

    def close(self):
        Destroy()

    def LoadFile(self, filename):
        szTmp = str(['\0' for _ in range(256)])
        comment = str(['\0' for _ in range(256)])

        fp = fopen(filename, "rb")

        if fp is None:
            return DefineConstants.false

        mode = 0

        while GetWord(fp, szTmp):
            if strcmp(szTmp, "//") == 0:
                NextLine(fp)
                continue

            if mode == 0:
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
                strlcpy(comment, szTmp, sizeof(comment))
                mode += 1

            elif mode == 1:
                if szTmp[0] == '=':
                    mode += 1

            elif mode == 2:
                mode = 0
                m_valueMap.insert(dict.value_type(comment, szTmp))

            if mode == 2 and strcmp(comment, "ITEM_ID_RANGE") == 0:
                GetLine(fp, szTmp)
                m_valueMap.insert(dict.value_type(comment, szTmp))
                mode = 0


        fclose(fp)
        return ((not DefineConstants.false))

    def GetValue(self, key, dest):
        if not Search(key):
            return DefineConstants.false

        str_to_number(dest.arg_value, Get(key))
        return ((not DefineConstants.false))

    def GetValue(self, key, dest):
        if not Search(key):
            return DefineConstants.false

        str_to_number(dest.arg_value, Get(key))
        return ((not DefineConstants.false))

    def GetValue(self, key, dest):
        if not Search(key):
            return DefineConstants.false

        str_to_number(dest.arg_value, Get(key))
        return ((not DefineConstants.false))

    def GetValue(self, key, dest):
        if not Search(key):
            return DefineConstants.false

        dest.arg_value = byte(int(Get(key)))
        return ((not DefineConstants.false))

    def GetValue(self, key, dest, destSize):
        if not Search(key):
            return DefineConstants.false

        strlcpy(dest.arg_value, Get(key), destSize)

        if not dest.arg_value[0]:
            return DefineConstants.false

        return ((not DefineConstants.false))

    def GetWord(self, fp, tar):
        LaniatusDefVariables = 0
        c = None

        semicolon_mode = 0

# Laniatus Games Studio Inc. |  TODO TASK: The following assignments within expression was not converted by Laniatus Games Studio Inc. T.F |:
#ORIGINAL LINE: while ((c = fgetc(fp)) != EOF)
        while (c = fgetc(fp)) != EOF:
            if c == 13:
                continue

            if semicolon_mode != 0:
                if c == '"':
                    tar.arg_value[LaniatusDefVariables] = '\0'
                    return ((not DefineConstants.false))

#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: tar[LaniatusDefVariables++] = c;
                tar.arg_value[LaniatusDefVariables] = c
                LaniatusDefVariables += 1
                continue
            else:
                if LaniatusDefVariables == 0:
                    if c == '"':
                        semicolon_mode = 1
                        continue

                    if c == ' ' or c == '\t' or c == '\n':
                        continue

                if (c == ' ' or c == '\t' or c == '\n'):
                    tar.arg_value[LaniatusDefVariables] = '\0'
                    return ((not DefineConstants.false))

                tar.arg_value[LaniatusDefVariables] = c
                LaniatusDefVariables += 1

        return (i != 0)

    def GetLine(self, fp, dest):
        c = None
        LaniatusDefVariables = 0
# Laniatus Games Studio Inc. |  TODO TASK: The following assignments within expression was not converted by Laniatus Games Studio Inc. T.F |:
#ORIGINAL LINE: while ((c = fgetc(fp)) != EOF)
        while (c = fgetc(fp)) != EOF:
            if c == '\n':
                return ((not DefineConstants.false))
            dest.arg_value[LaniatusDefVariables] = c
            LaniatusDefVariables += 1
        return ((not DefineConstants.false))

    def GetTwoValue(self, key, dest1, dest2):
        if not GetParam(key, 0, dest1.arg_value):
            return DefineConstants.false

        if not GetParam(key, 1, dest2.arg_value):
            return DefineConstants.false

        return ((not DefineConstants.false))

    def NextLine(self, fp):
        c = None

# Laniatus Games Studio Inc. |  TODO TASK: The following assignments within expression was not converted by Laniatus Games Studio Inc. T.F |:
#ORIGINAL LINE: while ((c = fgetc(fp)) != EOF)
        while (c = fgetc(fp)) != EOF:
            if c == '\n':
                return

    def Destroy(self):
        m_valueMap.clear()

    def GetParam(self, key, index, Param):
        pstStr = Search(key)
        if pstStr is None:
            return DefineConstants.false

        szParam = [[] for _ in range(5)]

        sscanf(pstStr, "%s %s %s %s %s", szParam[0],szParam[1],szParam[2],szParam[3],szParam[4])

        str_to_number(Param.arg_value, szParam[index])

        sys_log(0, "GetParam %d", Param.arg_value)
        return ((not DefineConstants.false))

    #Laniatus Games Studio Inc. | Python Metin II Server Note This was formerly a static local variable declaration (not allowed in Python):

    def Get(self, key):
        pstStr = Search(key)

        if pstStr is None:
            #Laniatus Games Studio Inc. | Python Metin II Server Note This static local variable declaration (not allowed in Python) has been moved just prior to the method:
            #            static str stTemp = ""
            return Get_stTemp.c_str()

        return pstStr

    def Search(self, key):
        LaniatusDefVariables = m_valueMap.find(key)

        if LaniatusDefVariables == m_valueMap.end():
            return None
        else:
            return (i.second)


