## Laniatus Games Studio Inc. | NOTE: Python has no need of forward class declarations:
#class SECTREE

class CEntity:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.m_bIsObserver = False
        self.m_bObserverModeChange = False
        self.m_map_view = _boost_func_of_void.unordered_map()
        self.m_lMapIndex = 0
        self._m_lpDesc = None
        self._m_iType = 0
        self._m_bIsDestroyed = False
        self._m_pos = pixel_position_s()
        self._m_iViewAge = 0
        self._m_pSectree = None

        self.Initialize(-1)

    def close(self):
        if not self._m_bIsDestroyed:
            assert not "You must call CEntity::destroy() method in your derived class destructor"

    def EncodeInsertPacket(self, entity):
        pass
    def EncodeRemovePacket(self, entity):
        pass

    def Initialize(self, type = -1):
        self._m_bIsDestroyed = LGEMiscellaneous.DEFINECONSTANTS.false

        self._m_iType = type
        self._m_iViewAge = 0
        self._m_pos.x = self._m_pos.y = self._m_pos.z = 0
        self.m_map_view.clear()

        self._m_pSectree = None
        self._m_lpDesc = None
        self.m_lMapIndex = 0
        self.m_bIsObserver = LGEMiscellaneous.DEFINECONSTANTS.false
        self.m_bObserverModeChange = LGEMiscellaneous.DEFINECONSTANTS.false

    def Destroy(self):
        if self._m_bIsDestroyed:
            return
        self.ViewCleanup()
        self._m_bIsDestroyed = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def SetType(self, type):
        self._m_iType = type

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: int GetType() const
    def GetType(self):
        return self._m_iType

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: bool IsType(int type) const
    def IsType(self, type):
        return (((not LGEMiscellaneous.DEFINECONSTANTS.false)) if self._m_iType == type else LGEMiscellaneous.DEFINECONSTANTS.false)

# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    ViewCleanup()
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    ViewInsert(entity, recursive = (!LGEMiscellaneous.DefineConstants.false))
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    ViewRemove(entity, recursive = (!LGEMiscellaneous.DefineConstants.false))
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    ViewReencode()
## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: int GetViewAge() const
    def GetViewAge(self):
        return self._m_iViewAge
## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: int GetX() const
    def GetX(self):
        return self._m_pos.x
## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: int GetY() const
    def GetY(self):
        return self._m_pos.y
## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: int GetZ() const
    def GetZ(self):
        return self._m_pos.z
## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: const pixel_position_s & GetXYZ() const
    def GetXYZ(self):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
#ORIGINAL METINII C CODE: return m_pos;
        return pixel_position_s(self._m_pos)
    def SetXYZ(self, x, y, z):
        self._m_pos.x = x, self._m_pos.y = y, self._m_pos.z = z
    def SetXYZ(self, pos):
## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: m_pos = pos;
        self._m_pos.copy_from(pos)
## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: SECTREE* GetSectree() const
    def GetSectree(self):
        return self._m_pSectree
    def SetSectree(self, tree):
        self._m_pSectree = tree
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    UpdateSectree()
    def PacketAround(self, data, bytes, except_ = None):
        self.PacketView(data, bytes, except_)

    def PacketView(self, data, bytes, except_ = None):
        if self.GetSectree() is None:
            return

        f = FuncPacketView(data, bytes, except_)

        if not self.m_bIsObserver:
            for_each(self.m_map_view.begin(), self.m_map_view.end(), f.functor_method)

        f.functor_method((self, 0))

    def BindDesc(self, _d):
        self._m_lpDesc = _d
## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: DESC* GetDesc() const
    def GetDesc(self):
        return self._m_lpDesc
    def SetMapIndex(self, l):
        self.m_lMapIndex = l
## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: int GetMapIndex() const
    def GetMapIndex(self):
        return self.m_lMapIndex
    def SetObserverMode(self, bFlag):
        if self.m_bIsObserver == bFlag:
            return

        self.m_bIsObserver = bFlag
        self.m_bObserverModeChange = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
        self.UpdateSectree()

        if self.IsType(EEntityTypes.ENTITY_CHARACTER):
            ch = self
            ch.ChatPacket(EChatType.CHAT_TYPE_COMMAND, "ObserverMode %d",1 if self.m_bIsObserver else 0)

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: bool IsObserverMode() const
    def IsObserverMode(self):
        return self.m_bIsObserver



class FuncPacketAround:

    def __init__(self, data, bytes, except_ = None):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.m_data = None
        self.m_bytes = 0
        self.m_except = None

        self.m_data = data
        self.m_bytes = bytes
        self.m_except = except_

    def functor_method(self, ent):
        if ent is self.m_except:
            return

        if ent.GetDesc():
            ent.GetDesc().Packet(self.m_data, self.m_bytes)

class FuncPacketView(FuncPacketAround):
    def __init__(self, data, bytes, except_ = None):
        super().functor_method(data, bytes, except_)

    def functor_method(self, v):
        base .functor_method() v.first

