## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if DEBUG_ALLOC

class DebugPtr:

    def _initialize_instance_fields(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self._p_ = None
        self._age_ = size_t()

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to multiple constructors:
#ORIGINAL METINII C CODE: DebugPtr() : p_(NULL), age_(0)
    def __init__(self):
        self._initialize_instance_fields()

        self._p_ = None
        self._age_ = 0
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to multiple constructors:
#ORIGINAL METINII C CODE: DebugPtr(T* p) : p_(p)
    def __init__(self, p):
        self._initialize_instance_fields()

        self._p_ = p
        self._age_ = DebugAllocator.RetrieveAge(self._p_)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to multiple constructors:
#ORIGINAL METINII C CODE: DebugPtr(U* p) : p_(static_cast<T*>(p))
    def __init__(self, p):
        self._initialize_instance_fields()

        self._p_ = p
        self._age_ = DebugAllocator.RetrieveAge(self._p_)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to multiple constructors:
#ORIGINAL METINII C CODE: DebugPtr(T* p, size_t age) : p_(p), age_(age)
    def __init__(self, p, age):
        self._initialize_instance_fields()

        self._p_ = p
## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: this.age_ = age;
        self._age_.copy_from(age)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to multiple constructors:
#ORIGINAL METINII C CODE: DebugPtr(const DebugPtr& o) : p_(o.p_), age_(o.age_)
    def __init__(self, o):
        self._initialize_instance_fields()

        self._p_ = o._p_
## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: this.age_ = o.age_;
        self._age_.copy_from(o._age_)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to multiple constructors:
#ORIGINAL METINII C CODE: DebugPtr(const DebugPtr<U>& o) : p_(static_cast<T*>(o.Get())), age_(o.GetAge())
    def __init__(self, o):
        self._initialize_instance_fields()

        self._p_ = o.Get()
## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: this.age_ = o.GetAge();
        self._age_.copy_from(o.GetAge())
    def close(self):
        pass

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: T& operator *() const
    def indirection(self):
        return (self._GetVerified())
## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: T* operator ->() const
    def dereference(self):
        return self._GetVerified()

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: T* Get() const
    def Get(self):
        return self._p_
## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: size_t GetAge() const
    def GetAge(self):
        return size_t(self._age_)

## Laniatus Games Studio Inc. | NOTE: This 'copy_from' method was converted from the original copy assignment operator:
#ORIGINAL METINII C CODE: DebugPtr& operator =(const DebugPtr& rhs)
    def copy_from(self, rhs):
        ptr = DebugPtr(rhs)
        return self._Swap(ptr)

## Laniatus Games Studio Inc. | NOTE: This 'copy_from' method was converted from the original copy assignment operator:
#ORIGINAL METINII C CODE: DebugPtr& operator =(const DebugPtr<U>& rhs)
    def copy_from(self, rhs):
        ptr = DebugPtr(rhs)
        return self._Swap(ptr)

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: operator T*() const
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following operator cannot be converted to Python:
    #operator T*() const
    #    {
    #        return GetVerified()
    #    }

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: bool operator !() const
    def not(self):
        return (self.Get() is None)

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: T* GetVerified() const
    def _GetVerified(self):
        p = self._p_
        if p is not None:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no equivalent to 'reinterpret_cast' in Python:
            age = *(reinterpret_cast<size_t>(p) - 1)
            if age is not self._age_:
                if DebugAllocator.Verify(p, self._age_) is not None:
                    DebugAllocator.LogBoundaryCorruption(p, age)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to pointers to value types:
#ORIGINAL METINII C CODE: int* no_way = NULL;
                no_way = None
                no_way = None
        return p

    def _Swap(self, o):
        std::swap(self._p_, o._p_)
        std::swap(self._age_, o._age_)
        return self



class std: #this class replaces the original namespace 'std'
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: C++ template specialization was removed by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: struct less<DebugPtr<T>>
    class less:
## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: bool operator ()(const DebugPtr<T>& lhs, const DebugPtr<T>& rhs) const
        def functor_method(self, lhs, rhs):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no equivalent to 'reinterpret_cast' in Python:
            return (reinterpret_cast<size_t>(lhs.Get()) < reinterpret_cast<size_t>(rhs.Get()))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: C++ template specialization was removed by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: struct equal_to<DebugPtr<T>>
    class equal_to:
## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: bool operator ()(const DebugPtr<T>& lhs, const DebugPtr<T>& rhs) const
        def functor_method(self, lhs, rhs):
            return (lhs.Get() is rhs.Get())
    def less_than(self, lhs, rhs):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no equivalent to 'reinterpret_cast' in Python:
        return (reinterpret_cast<size_t>(lhs.Get()) < reinterpret_cast<size_t>(rhs.Get()))

class boost: #this class replaces the original namespace 'boost'
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: C++ template specialization was removed by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: struct hash<DebugPtr<T>>
    class hash:
## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: size_t operator ()(const DebugPtr<T>& v) const
        def functor_method(self, v):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no equivalent to 'reinterpret_cast' in Python:
            return reinterpret_cast<size_t>(v.Get())


##endif
