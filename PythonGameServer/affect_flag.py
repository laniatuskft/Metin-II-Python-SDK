## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if ! IS_SET
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
##define IS_SET(flag, bit) ((flag) & (bit))
##endif

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if ! SET_BIT
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
##define SET_BIT(var, bit) ((var) |= (bit))
##endif

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if ! REMOVE_BIT
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
##define REMOVE_BIT(var, bit) ((var) &= ~(bit))
##endif

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if ! TOGGLE_BIT
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
##define TOGGLE_BIT(var, bit) ((var) = (var) ^ (bit))
##endif

class TAffectFlag:

    def _initialize_instance_fields(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.bits = [0 for _ in range(2)]


## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to multiple constructors:
#ORIGINAL METINII C CODE: inline TAffectFlag()
    def __init__(self):
        self._initialize_instance_fields()

        self.bits[0] = 0
        self.bits[1] = 0
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to multiple constructors:
#ORIGINAL METINII C CODE: inline TAffectFlag(uint v1, uint v2 = 0)
    def __init__(self, v1, v2 = 0):
        self._initialize_instance_fields()

        self.bits[0] = v1
        self.bits[1] = v2

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: inline bool IsSet(int flag) const
    def IsSet(self, flag):
        if AFF_BITS_MAX <= flag or 0 >= flag:
            return False

        return ((self.bits[(flag - 1) >> 5]) & (((1) << ((flag - 1) & 31)))) != 0

    def Set(self, flag):
        if AFF_BITS_MAX <= flag or 0 >= flag:
            return

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: ((bits[(flag-1)>>5]) |= ((((uint)1)<<((flag-1)&31))));
        ((self.bits[(flag-1)>>5]) |= (((1)<<((flag-1)&31))))

    def Reset(self, flag):
        if AFF_BITS_MAX <= flag or 0 >= flag:
            return

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: ((bits[(flag-1)>>5]) &= ~((((uint)1)<<((flag-1)&31))));
        ((self.bits[(flag-1)>>5]) &= ~(((1)<<((flag-1)&31))))

## Laniatus Games Studio Inc. | NOTE: This 'copy_from' method was converted from the original copy assignment operator:
#ORIGINAL METINII C CODE: inline TAffectFlag& operator = (const TAffectFlag& rhs)
    def copy_from(self, rhs):
        self.bits[0] = rhs.bits[0]
        self.bits[1] = rhs.bits[1]
        return self