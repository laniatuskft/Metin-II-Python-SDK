class stringhash:
#Laniatus Games Studio Inc. | Python Metin II Server Warnings 'const' methods are not available in Python:
#ORIGINAL LINE: size_t operator ()(const str & str) const
    def functor_method(self, str):
# Laniatus Games Studio Inc. |  TODO TASK: Pointer arithmetic is detected on this variable:
#ORIGINAL LINE: const byte * s = (const byte*) str.c_str();
        s = byte(int(str))
# Laniatus Games Studio Inc. |  TODO TASK: Python does not have an equivalent to pointers to value types:
#ORIGINAL LINE: const byte * end = s + str.size();
        end = byte(s + len(str))
        h = 0

        while s < end:
            h *= 16777619
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: h ^= *(s++);
            h ^= *(s)
            s += 1

        return size_t(h)

class std: #this class replaces the original namespace 'std'
    @staticmethod
    def erase_if(a, first, past, pred):
        while first is not past:
            if pred(*first):
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: a.erase(first++);
                a.erase(first)
                first += 1
            else:
                first += 1

    @staticmethod
    def wipe(a):
        first = container.iterator()
        past = container.iterator()

        first = a.begin()
        past = a.end()

        while first is not past:
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: delete *(first++);
            *(first) = None
            first += 1

        a.clear()

    @staticmethod
    def wipe_second(a):
        first = container.iterator()
        past = container.iterator()

        first = a.begin()
        past = a.end()

        while first is not past:
            first.second = None
            first += 1

        a.clear()

# Laniatus Games Studio Inc. |  TODO TASK: There is no preprocessor in Python:
##if WIN32
    @staticmethod
    def MIN(a, b):
        return a if a < b else b

    @staticmethod
    def MAX(a, b):
        return a if a > b else b
##endif

    @staticmethod
    def MINMAX(min, value, max):
        tv = None

        tv = (min if min > value else value)
        return max if (max < tv) else tv
