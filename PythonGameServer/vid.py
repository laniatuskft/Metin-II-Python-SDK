class VID:

    def _initialize_instance_fields(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self._m_id = 0
        self._m_crc = 0

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to multiple constructors:
#ORIGINAL METINII C CODE: VID() : m_id(0), m_crc(0)
    def __init__(self):
        self._initialize_instance_fields()

        self._m_id = 0
        self._m_crc = 0

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to multiple constructors:
#ORIGINAL METINII C CODE: VID(uint id, uint crc)
    def __init__(self, id, crc):
        self._initialize_instance_fields()

        self._m_id = id
        self._m_crc = crc

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to multiple constructors:
#ORIGINAL METINII C CODE: VID(const VID &rvid)
    def __init__(self, rvid):
        self._initialize_instance_fields()

        self = rvid

## Laniatus Games Studio Inc. | NOTE: This 'copy_from' method was converted from the original copy assignment operator:
#ORIGINAL METINII C CODE: const VID & operator = (const VID & rhs)
    def copy_from(self, rhs):
        self._m_id = rhs._m_id
        self._m_crc = rhs._m_crc
        return self

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: bool operator == (const VID & rhs) const
    def equals_to(self, rhs):
        return (self._m_id == rhs._m_id) and (self._m_crc == rhs._m_crc)

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: bool operator != (const VID & rhs) const
    def not_equals_to(self, rhs):
        return not(self is rhs)

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: operator uint() const
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following operator cannot be converted to Python:
    #operator uint() const
    #        {
    #            return m_id
    #        }

    def Reset(self):
        self._m_id = 0, self._m_crc = 0

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: uint getID() const
    def getID(self):
        return self._m_id
