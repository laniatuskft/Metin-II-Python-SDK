class LateAllocator:
    def __init__(self):
        pass

    def close(self):
        while LateAllocator._m_freeBlockCount > 0:
            p = LateAllocator._m_freeBlocks.front()
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if DEBUG_ALLOC
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no equivalent to 'reinterpret_cast' in Python:
            free(reinterpret_cast<size_t>(p) - 1)
##else
            free(p)
##endif

            LateAllocator._m_freeBlocks.pop_front()

            LateAllocator._m_freeBlockCount -= 1

    @staticmethod
    def Alloc(size):
        p = None

        if LateAllocator._m_freeBlockCount > 0:
            p = LateAllocator._m_freeBlocks.front()

            LateAllocator._m_freeBlocks.pop_front()

            LateAllocator._m_freeBlockCount -= 1
        else:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if DEBUG_ALLOC
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            p = malloc(size + sizeof(size_t))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no equivalent to 'reinterpret_cast' in Python:
            p = reinterpret_cast<size_t>(p) + 1
##else
            p = malloc(size)
##endif

        return p

    @staticmethod
    def Free(p):
        if p is None:
            return

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if DEBUG_ALLOC
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memset(p, 0, sizeof(OBJ))
##endif

        if LateAllocator._m_freeBlockCount >= FREE_TRIGGER:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if DEBUG_ALLOC
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no equivalent to 'reinterpret_cast' in Python:
            free(reinterpret_cast<size_t>(p) - 1)
##else
            free(p)
##endif
        else:
            LateAllocator._m_freeBlockCount += 1

            LateAllocator._m_freeBlocks.push_back(p)

    @staticmethod
    def GetFreeBlockCount():
        return size_t(LateAllocator._m_freeBlockCount)


    _m_freeBlockCount = size_t()
    _m_freeBlocks = std::deque()

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: C++ 'constraints' are not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: template <typename OBJ, size_t FREE_TRIGGER>
class ObjectAllocator:
    def __init__(self):
        pass
    def close(self):
        pass

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following operator cannot be converted to Python:
    #static object* operator new(size_t size)
    #    {
    #        return m_allocator.Alloc(size)
    #    }

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following operator cannot be converted to Python:
    #static void operator delete(object* p, size_t size)
    #    {
    ##if DEBUG_ALLOC
    #        size_t& age = *(reinterpret_cast<size_t*>(p) - 1)
    #        age = AllocTag::IncreaseAge(age)
    ##endif
    #        m_allocator.Free(p)
    #    }

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following operator cannot be converted to Python:
    #static object* operator new(size_t size, const char* f, size_t l)
    #    {
    #        object* p = m_allocator.Alloc(size)
    ##if DEBUG_ALLOC
    #        if (p != NULL)
    #        {
    #            size_t age = DebugAllocatorAdapter<FifoAllocator>::MarkAcquired(p, f, l, "new_obj")
    #            *(reinterpret_cast<size_t*>(p) - 1) = age
    #        }
    ##endif
    #        return p
    #    }

    @staticmethod
    def GetFreeBlockCount():
        return ObjectAllocator._m_allocator.GetFreeBlockCount()

    _m_allocator = LateAllocator()

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if DEBUG_ALLOC
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
##define M2_OBJ_NEW new(__FILE__, __LINE__)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
##define M2_OBJ_DELETE(p) delete (get_pointer(p)); DebugAllocator::MarkReleased(p, __FILE__, __LINE__, "delete_obj");
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
##define M2_OBJ_DELETE_EX(p, f, l) delete (get_pointer(p)); DebugAllocator::MarkReleased(p, f, l, "delete_obj");
##else
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
##define M2_OBJ_NEW new
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
##define M2_OBJ_DELETE(p) delete (p)
##endif