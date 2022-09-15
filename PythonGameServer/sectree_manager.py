from enum import Enum
import math

class SMapRegion:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.index = 0
        self.sx = 0
        self.sy = 0
        self.ex = 0
        self.ey = 0
        self.posSpawn = pixel_position_s()
        self.bEmpireSpawnDifferent = False
        self.posEmpire = [pixel_position_s() for _ in range(3)]
        self.strMapName = ""




class TAreaInfo:
    def __init__(self, sx, sy, ex, ey, dir):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.sx = 0
        self.sy = 0
        self.ex = 0
        self.ey = 0
        self.dir = 0

        self.sx = sx
        self.sy = sy
        self.ex = ex
        self.ey = ey
        self.dir = dir

class npc_info:
    def __init__(self, bType, name, x, y):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.bType = 0
        self.name = '\0'
        self.x = 0
        self.y = 0

        self.bType = bType
        self.name = name
        self.x = x
        self.y = y


class SSetting:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.iIndex = 0
        self.iCellScale = 0
        self.iBaseX = 0
        self.iBaseY = 0
        self.iWidth = 0
        self.iHeight = 0
        self.posSpawn = pixel_position_s()



class SECTREE_MAP:

    def _initialize_instance_fields(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.m_setting = SSetting()
        self._map_ = {}


## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to multiple constructors:
#ORIGINAL METINII C CODE: SECTREE_MAP()
    def __init__(self):
        self._initialize_instance_fields()

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memset(self.m_setting, 0, sizeof(self.m_setting))

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to multiple constructors:
#ORIGINAL METINII C CODE: SECTREE_MAP(SECTREE_MAP & r)
    def __init__(self, r):
        self._initialize_instance_fields()

## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: m_setting = r.m_setting;
        self.m_setting.copy_from(r.m_setting)

        it = r._map_.begin()

        while it is not r._map_.end():
            tree = LG_NEW_M2 SECTREE

            tree.m_id.coord = it.second.m_id.coord
            tree.CloneAttribute(it.second)

            self._map_.insert(MapType.value_type(it.first, tree))
            it += 1

        self.Build()

    def close(self):
        it = self._map_.begin()

        while it is not self._map_.end():
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: SECTREE* sectree = (it++)->second;
            sectree = (it).second
            it += 1
            LG_DEL_MEM(sectree)

        self._map_.clear()

    def Add(self, key, sectree):
        return self._map_.insert(dict.value_type(key, sectree)).second

    def Find(self, dwPackage):
        it = self._map_.find(dwPackage)

        if it is self._map_.end():
            return None

        return it.second

    def Find(self, x, y):
        id = SECTREEID()
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        id.coord.x = x / uint(ESectree.SECTREE_SIZE)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        id.coord.y = y / uint(ESectree.SECTREE_SIZE)
        return self.Find(id.package)

    class neighbor_coord_s:
    def Build(self):
        neighbor_coord = [[ -ESectree.SECTREE_SIZE, 0 ], [ (int)ESectree.SECTREE_SIZE, 0 ], [ 0, -ESectree.SECTREE_SIZE ], [ 0, (int)ESectree.SECTREE_SIZE ], [ -ESectree.SECTREE_SIZE, (int)ESectree.SECTREE_SIZE ], [ (int)ESectree.SECTREE_SIZE, -ESectree.SECTREE_SIZE ], [ -ESectree.SECTREE_SIZE, -ESectree.SECTREE_SIZE ], [ (int)ESectree.SECTREE_SIZE, (int)ESectree.SECTREE_SIZE ]]

        it = self._map_.begin()

        while it is not self._map_.end():
            tree = it.second

            tree.m_neighbor_list.push_back(tree)

            #sys_log(3, "%dx%d", tree.m_id.coord.x, tree.m_id.coord.y)

            x = tree.m_id.coord.x * ESectree.SECTREE_SIZE
            y = tree.m_id.coord.y * ESectree.SECTREE_SIZE

            for i in range(0, 8):
                tree2 = self.Find(uint(x + neighbor_coord[i].x), uint(y + neighbor_coord[i].y))

                if tree2:
                    #sys_log(3, "   %d %dx%d", i, tree2.m_id.coord.x, tree2.m_id.coord.y)
                    tree.m_neighbor_list.push_back(tree2)

            it += 1


    def for_each(self, rfunc):
        collector = FCollectEntity()
        it = self._map_.begin()
        while it is not self._map_.end():
            sectree = it.second
            sectree.for_each_entity(collector.functor_method)
            it += 1
        collector.ForEach(rfunc)

    def DumpAllToSysErr(self):
        i = map_.begin()
        while i is not self._map_.end():
            #lani_err("SECTREE %x(%u, %u)", i.first, i.first & 0xffff, i.first >> 16)
            i += 1


class EAttrRegionMode(Enum):
    ATTR_REGION_MODE_SET = 0
    ATTR_REGION_MODE_REMOVE = 1
    ATTR_REGION_MODE_CHECK = 2

class SECTREE_MANAGER(singleton):
    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self._m_map_pkSectree = {}
        self._m_map_pkArea = {}
        self._m_vec_mapRegion = []
        self._m_mapNPCPosition = {}
        self._next_private_index_map_ = _boost_func_of_void.unordered_map()


    def close(self):
        pass

    def GetMap(self, lMapIndex):
        it = self._m_map_pkSectree.find(lMapIndex)

        if it is self._m_map_pkSectree.end():
            return None

        return it.second

    def Get(self, dwIndex, package):
        pkSectreeMap = self.GetMap(int(dwIndex))

        if pkSectreeMap is None:
            return None

        return pkSectreeMap.Find(package)

    def Get(self, dwIndex, x, y):
        id = SECTREEID()
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        id.coord.x = x / uint(ESectree.SECTREE_SIZE)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        id.coord.y = y / uint(ESectree.SECTREE_SIZE)
        return self.Get(dwIndex, id.package)

    def for_each(self, iMapIndex, rfunc):
        pSecMap = SECTREE_MANAGER.instance().GetMap(iMapIndex)
        if pSecMap:
            pSecMap.for_each(rfunc)

    def LoadSettingFile(self, lMapIndex, c_pszSettingFileName, r_setting):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memset(r_setting, 0, sizeof(SSetting))

        fp = fopen(c_pszSettingFileName, "r")

        if fp is None:
            #lani_err("cannot open file: %s", c_pszSettingFileName)
            return 0

        buf = str(['\0' for _ in range(256)])
        cmd = str(['\0' for _ in range(256)])
        iWidth = 0
        iHeight = 0

        while fgets(buf, 256, fp):
            sscanf(buf, " %s ", cmd)

            if not _stricmp(cmd, "MapSize"):
                sscanf(buf, " %s %d %d ", cmd, iWidth, iHeight)
            elif not _stricmp(cmd, "BasePosition"):
                sscanf(buf, " %s %d %d", cmd, r_setting.iBaseX, r_setting.iBaseY)
            elif not _stricmp(cmd, "CellScale"):
                sscanf(buf, " %s %d ", cmd, r_setting.iCellScale)

        fclose(fp)

        if (iWidth == 0 and iHeight == 0) or r_setting.iCellScale == 0:
            #lani_err("Invalid Settings file: %s", c_pszSettingFileName)
            return 0

        r_setting.iIndex = lMapIndex
        r_setting.iWidth = (r_setting.iCellScale * 128 * iWidth)
        r_setting.iHeight = (r_setting.iCellScale * 128 * iHeight)
        return 1

    def LoadMapRegion(self, c_pszFileName, r_setting, c_pszMapName):
        fp = fopen(c_pszFileName, "r")

        if test_server:
            #sys_log(0, "[LoadMapRegion] file(%s)", c_pszFileName)

        if fp is None:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        iX = 0
        iY = 0
        pos = [pixel_position_s(0, 0, 0), pixel_position_s(0, 0, 0), pixel_position_s(0, 0, 0)]

        fscanf(fp, " %d %d ", iX, iY)

        iEmpirePositionCount = fscanf(fp, " %d %d %d %d %d %d ", pos[0].x, pos[0].y, pos[1].x, pos[1].y, pos[2].x, pos[2].y)

        fclose(fp)

        if iEmpirePositionCount == 6:
            for n in range(0, 3):
                #sys_log(0,"LoadMapRegion %d %d ", pos[n].x, pos[n].y)
        else:
            #sys_log(0, "LoadMapRegion no empire specific start point")

        region = SMapRegion()

        region.index = r_setting.iIndex
        region.sx = r_setting.iBaseX
        region.sy = r_setting.iBaseY
        region.ex = r_setting.iBaseX + r_setting.iWidth
        region.ey = r_setting.iBaseY + r_setting.iHeight

        region.strMapName = c_pszMapName

        region.posSpawn.x = r_setting.iBaseX + (iX * 100)
        region.posSpawn.y = r_setting.iBaseY + (iY * 100)

## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: r_setting.posSpawn = region.posSpawn;
        r_setting.posSpawn.copy_from(region.posSpawn)

        #sys_log(0, "LoadMapRegion %d x %d ~ %d y %d ~ %d, town %d %d", region.index, region.sx, region.ex, region.sy, region.ey, region.posSpawn.x, region.posSpawn.y)

        if iEmpirePositionCount == 6:
            region.bEmpireSpawnDifferent = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

            for i in range(0, 3):
                region.posEmpire[i].x = r_setting.iBaseX + (pos[i].x * 100)
                region.posEmpire[i].y = r_setting.iBaseY + (pos[i].y * 100)
        else:
            region.bEmpireSpawnDifferent = LGEMiscellaneous.DEFINECONSTANTS.false

        self._m_vec_mapRegion.append(region)

        #sys_log(0,"LoadMapRegion %d End", region.index)
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def Build(self, c_pszListFileName, c_pszMapBasePath):
        if test_server:
            #sys_log(0, "[BUILD] Build %s %s ", c_pszListFileName, c_pszMapBasePath)

        fp = fopen(c_pszListFileName, "r")

        if None is fp:
            return 0

        buf = str(['\0' for _ in range(256 + 1)])
        szFilename = str(['\0' for _ in range(256)])
        szMapName = str(['\0' for _ in range(256)])
        iIndex = None

        while fgets(buf, 256, fp):
            *strrchr(buf, '\n') = '\0'

            if (not strncmp(buf, "#", 2)) or buf[0] == '#':
                continue

            sscanf(buf, " %d %s ", iIndex, szMapName)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            snprintf(szFilename, sizeof(szFilename), "%s/%s/Setting.txt", c_pszMapBasePath, szMapName)

            setting = SSetting()
            setting.iIndex = iIndex

            if self.LoadSettingFile(iIndex, szFilename, setting) == 0:
                #lani_err("can't load file %s in LoadSettingFile", szFilename)
                fclose(fp)
                return 0

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            snprintf(szFilename, sizeof(szFilename), "%s/%s/Town.txt", c_pszMapBasePath, szMapName)

            if not self.LoadMapRegion(szFilename, setting, szMapName):
                #lani_err("can't load file %s in LoadMapRegion", szFilename)
                fclose(fp)
                return 0

            if test_server:
                #sys_log(0,"[BUILD] Build %s %s %d ",c_pszMapBasePath, szMapName, iIndex)

            if map_allow_find(iIndex):
                pkMapSectree = self.BuildSectreeFromSetting(setting)
                self._m_map_pkSectree.insert(dict.value_type(iIndex, pkMapSectree))

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                snprintf(szFilename, sizeof(szFilename), "%s/%s/server_attr", c_pszMapBasePath, szMapName)
                self.LoadAttribute(pkMapSectree, szFilename, setting)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                snprintf(szFilename, sizeof(szFilename), "%s/%s/regen.txt", c_pszMapBasePath, szMapName)
                regen_load(szFilename, setting.iIndex, setting.iBaseX, setting.iBaseY)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                snprintf(szFilename, sizeof(szFilename), "%s/%s/npc.txt", c_pszMapBasePath, szMapName)
                regen_load(szFilename, setting.iIndex, setting.iBaseX, setting.iBaseY)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                snprintf(szFilename, sizeof(szFilename), "%s/%s/boss.txt", c_pszMapBasePath, szMapName)
                regen_load(szFilename, setting.iIndex, setting.iBaseX, setting.iBaseY)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                snprintf(szFilename, sizeof(szFilename), "%s/%s/stone.txt", c_pszMapBasePath, szMapName)
                regen_load(szFilename, setting.iIndex, setting.iBaseX, setting.iBaseY)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                snprintf(szFilename, sizeof(szFilename), "%s/%s/dungeon.txt", c_pszMapBasePath, szMapName)
                self.LoadDungeon(iIndex, szFilename)

                pkMapSectree.Build()

        fclose(fp)

        return 1

    def BuildSectreeFromSetting(self, r_setting):
        pkMapSectree = LG_NEW_M2 SECTREE_MAP

## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: pkMapSectree->m_setting = r_setting;
        pkMapSectree.m_setting.copy_from(r_setting)

        x = None
        y = None
        tree = None

        x = r_setting.iBaseX
        while x < r_setting.iBaseX + r_setting.iWidth:
            y = r_setting.iBaseY
            while y < r_setting.iBaseY + r_setting.iHeight:
                tree = LG_NEW_M2 SECTREE
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
                tree.m_id.coord.x = x / int(ESectree.SECTREE_SIZE)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
                tree.m_id.coord.y = y / int(ESectree.SECTREE_SIZE)
                pkMapSectree.Add(tree.m_id.package, tree)
                #sys_log(3, "new sectree %d x %d", tree.m_id.coord.x, tree.m_id.coord.y)
                y += SECTREE_SIZE
            x += SECTREE_SIZE

        if math.fmod((r_setting.iBaseX + r_setting.iWidth), ESectree.SECTREE_SIZE):
            tree = LG_NEW_M2 SECTREE
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
            tree.m_id.coord.x = ((r_setting.iBaseX + r_setting.iWidth) / ESectree.SECTREE_SIZE) + 1
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
            tree.m_id.coord.y = ((r_setting.iBaseY + r_setting.iHeight) / ESectree.SECTREE_SIZE)
            pkMapSectree.Add(tree.m_id.package, tree)

        if math.fmod((r_setting.iBaseY + r_setting.iHeight), ESectree.SECTREE_SIZE):
            tree = LG_NEW_M2 SECTREE
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
            tree.m_id.coord.x = ((r_setting.iBaseX + r_setting.iWidth) / ESectree.SECTREE_SIZE)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
            tree.m_id.coord.y = ((r_setting.iBaseX + r_setting.iHeight) / ESectree.SECTREE_SIZE) + 1
            pkMapSectree.Add(tree.m_id.package, tree)

        return pkMapSectree

    def LoadAttribute(self, pkMapSectree, c_pszFileName, r_setting):
        fp = fopen(c_pszFileName, "rb")

        if fp is None:
            #lani_err("SECTREE_MANAGER::LoadAttribute : cannot open %s", c_pszFileName)
            return LGEMiscellaneous.DEFINECONSTANTS.false

        iWidth = None
        iHeight = None

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        fread(iWidth, sizeof(int), 1, fp)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        fread(iHeight, sizeof(int), 1, fp)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        maxMemSize = LZOManager.instance().GetMaxCompressedSize(sizeof(uint) * (ESectree.SECTREE_SIZE / ESectree.CELL_SIZE) * (ESectree.SECTREE_SIZE / ESectree.CELL_SIZE))

        uiSize = None
        uiDestSize = None

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to pointers to value types:
#ORIGINAL METINII C CODE: byte* abComp = LG_NEW_M2 byte[maxMemSize];
        abComp = LG_NEW_M2 byte[maxMemSize]
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to pointers to value types:
#ORIGINAL METINII C CODE: uint * attr = LG_NEW_M2 uint[maxMemSize];
        attr = LG_NEW_M2 uint[maxMemSize]

        for y in range(0, iHeight):
            for x in range(0, iWidth):
                id = SECTREEID()
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
                id.coord.x = (r_setting.iBaseX / int(ESectree.SECTREE_SIZE)) + x
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
                id.coord.y = (r_setting.iBaseY / int(ESectree.SECTREE_SIZE)) + y

                tree = pkMapSectree.Find(id.package)

                if tree is None:
                    #lani_err("FATAL ERROR! LoadAttribute(%s) - cannot find sectree(package=%x, coord=(%u, %u), map_index=%u, map_base=(%u, %u))", c_pszFileName, id.package, id.coord.x, id.coord.y, r_setting.iIndex, r_setting.iBaseX, r_setting.iBaseY)
                    #lani_err("ERROR_ATTR_POS(%d, %d) attr_size(%d, %d)", x, y, iWidth, iHeight)
                    #lani_err("CHECK! 'Setting.txt' and 'server_attr' MAP_SIZE!!")

                    pkMapSectree.DumpAllToSysErr()
                    abort()

                    LG_DEL_MEM_ARRAY(attr)
                    LG_DEL_MEM_ARRAY(abComp)
                    return LGEMiscellaneous.DEFINECONSTANTS.false

                if tree.m_id.package != id.package:
                    #lani_err("returned tree id mismatch! return %u, request %u", tree.m_id.package, id.package)
                    fclose(fp)

                    LG_DEL_MEM_ARRAY(attr)
                    LG_DEL_MEM_ARRAY(abComp)
                    return LGEMiscellaneous.DEFINECONSTANTS.false

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                fread(uiSize, sizeof(int), 1, fp)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                fread(abComp, sizeof(char), uiSize, fp)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                uiDestSize = sizeof(uint) * maxMemSize
                LZOManager.instance().Decompress(abComp, uiSize, byte(int(attr)), uiDestSize)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                if uiDestSize != sizeof(uint) * (ESectree.SECTREE_SIZE / ESectree.CELL_SIZE) * (ESectree.SECTREE_SIZE / ESectree.CELL_SIZE):
                    #lani_err("SECTREE_MANAGER::LoadAttribte : %s : %d %d size mismatch! %d", c_pszFileName, tree.m_id.coord.x, tree.m_id.coord.y, uiDestSize)
                    fclose(fp)

                    LG_DEL_MEM_ARRAY(attr)
                    LG_DEL_MEM_ARRAY(abComp)
                    return LGEMiscellaneous.DEFINECONSTANTS.false

                temp_ref_attr = RefObject(attr);
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
                tree.BindAttribute(LG_NEW_M2 CAttribute(temp_ref_attr, ESectree.SECTREE_SIZE / ESectree.CELL_SIZE, ESectree.SECTREE_SIZE / ESectree.CELL_SIZE))
                attr = temp_ref_attr.arg_value

        fclose(fp)

        LG_DEL_MEM_ARRAY(attr)
        LG_DEL_MEM_ARRAY(abComp)
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def LoadDungeon(self, iIndex, c_pszFileName):
        fp = fopen(c_pszFileName, "r")

        if fp is None:
            return

        count = 0

        while not feof(fp):
            buf = str(['\0' for _ in range(1024)])

            if None == fgets(buf, 1024, fp):
                break

            if buf[0] == '#' or buf[0] == '/' and buf[1] == '/':
                continue

            ins = std::istringstream(buf, std::ios_base.in_)
            position_name = ""
            x = None
            y = None
            sx = None
            sy = None
            dir = None

            ins >> position_name >> x >> y >> sx >> sy >> dir

            if ins.fail():
                continue

            x -= sx
            y -= sy
            sx *= 2
            sy *= 2
            sx += x
            sy += y

            self._m_map_pkArea[iIndex].insert((position_name, TAreaInfo(x, y, sx, sy, dir)))

            count += 1

        fclose(fp)

        #sys_log(0, "Dungeon Position Load [%3d]%s count %d", iIndex, c_pszFileName, count)

    def GetValidLocation(self, lMapIndex, x, y, r_lValidMapIndex, r_pos, empire = 0):
        pkSectreeMap = self.GetMap(lMapIndex)

        if pkSectreeMap is None:
            if lMapIndex >= 10000:
                return self.GetValidLocation(math.trunc(lMapIndex / float(10000)), x, y, r_lValidMapIndex, r_pos, 0)
            else:
                #lani_err("cannot find sectree_map by map index %d", lMapIndex)
                return LGEMiscellaneous.DEFINECONSTANTS.false

        lRealMapIndex = lMapIndex

        if lRealMapIndex >= 10000:
            lRealMapIndex = math.trunc(lRealMapIndex / float(10000))

        it = self._m_vec_mapRegion.begin()

        while it is not self._m_vec_mapRegion.end():
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: SMapRegion & rRegion = *(it++);
            rRegion = *(it)
            it += 1

            if rRegion.index == lRealMapIndex:
                tree = pkSectreeMap.Find(uint(x), uint(y))

                if tree is None:
                    #lani_err("cannot find tree by %d %d (map index %d)", x, y, lMapIndex)
                    return LGEMiscellaneous.DEFINECONSTANTS.false

                r_lValidMapIndex.arg_value = lMapIndex
                r_pos.x = x
                r_pos.y = y
                return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        #lani_err("invalid location (map index %d %d x %d)", lRealMapIndex, x, y)
        return LGEMiscellaneous.DEFINECONSTANTS.false

    def GetSpawnPosition(self, x, y, r_pos):
        it = self._m_vec_mapRegion.begin()

        while it is not self._m_vec_mapRegion.end():
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: SMapRegion & rRegion = *(it++);
            rRegion = *(it)
            it += 1

            if x >= rRegion.sx and y >= rRegion.sy and x < rRegion.ex and y < rRegion.ey:
                r_pos.arg_value = rRegion.posSpawn
                return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        return LGEMiscellaneous.DEFINECONSTANTS.false

    def GetSpawnPositionByMapIndex(self, lMapIndex, r_pos):
        if lMapIndex> 10000:
            lMapIndex = math.trunc(lMapIndex / float(10000))
        it = self._m_vec_mapRegion.begin()

        while it is not self._m_vec_mapRegion.end():
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: SMapRegion & rRegion = *(it++);
            rRegion = *(it)
            it += 1

            if lMapIndex == rRegion.index:
                r_pos.arg_value = rRegion.posSpawn
                return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        return LGEMiscellaneous.DEFINECONSTANTS.false

    def GetRecallPositionByEmpire(self, iMapIndex, bEmpire, r_pos):
        it = self._m_vec_mapRegion.begin()

        if iMapIndex >= 10000:
            iMapIndex = math.trunc(iMapIndex / float(10000))

        while it is not self._m_vec_mapRegion.end():
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: SMapRegion & rRegion = *(it++);
            rRegion = *(it)
            it += 1

            if rRegion.index == iMapIndex:
                if rRegion.bEmpireSpawnDifferent and bEmpire >= 1 and bEmpire <= 3:
                    r_pos.arg_value = rRegion.posEmpire[bEmpire - 1]
                else:
                    r_pos.arg_value = rRegion.posSpawn

                return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        return LGEMiscellaneous.DEFINECONSTANTS.false

    def GetMapRegion(self, lMapIndex):
        it = self._m_vec_mapRegion.begin()

        while it is not self._m_vec_mapRegion.end():
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: SMapRegion & rRegion = *(it++);
            rRegion = *(it)
            it += 1

            if rRegion.index == lMapIndex:
                return rRegion

        return None

    def GetMapIndex(self, x, y):
        it = self._m_vec_mapRegion.begin()

        while it is not self._m_vec_mapRegion.end():
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: SMapRegion & rRegion = *(it++);
            rRegion = *(it)
            it += 1

            if x >= rRegion.sx and y >= rRegion.sy and x < rRegion.ex and y < rRegion.ey:
                return rRegion.index

        #sys_log(0, "SECTREE_MANAGER::GetMapIndex(%d, %d)", x, y)

        for i in self._m_vec_mapRegion:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to references to variables:
#ORIGINAL METINII C CODE: SMapRegion & rRegion = *i;
            rRegion = *i
            #sys_log(0, "%d: (%d, %d) ~ (%d, %d)", rRegion.index, rRegion.sx, rRegion.sy, rRegion.ex, rRegion.ey)

        return 0

    def FindRegionByPartialName(self, szMapName):
        it = self._m_vec_mapRegion.begin()

        while it is not self._m_vec_mapRegion.end():
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: SMapRegion & rRegion = *(it++);
            rRegion = *(it)
            it += 1

            if rRegion.strMapName.find(szMapName) != 0:
                return rRegion

        return None

    def GetMapBasePosition(self, x, y, r_pos):
        it = self._m_vec_mapRegion.begin()

        while it is not self._m_vec_mapRegion.end():
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: SMapRegion & rRegion = *(it++);
            rRegion = *(it)
            it += 1

            if x >= rRegion.sx and y >= rRegion.sy and x < rRegion.ex and y < rRegion.ey:
                r_pos.x = rRegion.sx
                r_pos.y = rRegion.sy
                r_pos.z = 0
                return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        return LGEMiscellaneous.DEFINECONSTANTS.false

    def GetMapBasePositionByMapIndex(self, lMapIndex, r_pos):
        if lMapIndex> 10000:
            lMapIndex = math.trunc(lMapIndex / float(10000))
        it = self._m_vec_mapRegion.begin()

        while it is not self._m_vec_mapRegion.end():
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: SMapRegion & rRegion = *(it++);
            rRegion = *(it)
            it += 1

            if lMapIndex == rRegion.index:
                r_pos.x = rRegion.sx
                r_pos.y = rRegion.sy
                r_pos.z = 0
                return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        return LGEMiscellaneous.DEFINECONSTANTS.false

    def GetMovablePosition(self, lMapIndex, x, y, pos):
        i = 0

        condition = True
        while condition:
            dx = x + aArroundCoords[i].x
            dy = y + aArroundCoords[i].y

            tree = self.Get(uint(lMapIndex), uint(dx), uint(dy))

            if tree is None:
                continue

            if not tree.IsAttr(dx, dy, uint(Globals.ATTR_BLOCK | Globals.ATTR_OBJECT)):
                pos.x = dx
                pos.y = dy
                return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
            i += 1
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: } while (++i < DefineConstants.ARROUND_COORD_MAX_NUM);
            condition = i < LGEMiscellaneous.DEFINECONSTANTS.ARROUND_COORD_MAX_NUM

        pos.x = x
        pos.y = y
        return LGEMiscellaneous.DEFINECONSTANTS.false

    def IsMovablePosition(self, lMapIndex, x, y):
        tree = self.Get(uint(lMapIndex), uint(x), uint(y))

        if tree is None:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        return ((not tree.IsAttr(x, y, uint(Globals.ATTR_BLOCK | Globals.ATTR_OBJECT))))

    def GetCenterPositionOfMap(self, lMapIndex, r_pos):
        it = self._m_vec_mapRegion.begin()

        while it is not self._m_vec_mapRegion.end():
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: SMapRegion & rRegion = *(it++);
            rRegion = *(it)
            it += 1

            if rRegion.index == lMapIndex:
                r_pos.x = rRegion.sx + math.trunc((rRegion.ex - rRegion.sx) / float(2))
                r_pos.y = rRegion.sy + math.trunc((rRegion.ey - rRegion.sy) / float(2))
                r_pos.z = 0
                return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        return LGEMiscellaneous.DEFINECONSTANTS.false

    def GetRandomLocation(self, lMapIndex, r_pos, dwCurrentX = 0, dwCurrentY = 0, iMaxDistance = 0):
        pkSectreeMap = self.GetMap(lMapIndex)

        if pkSectreeMap is None:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        x = None
        y = None

        it = self._m_vec_mapRegion.begin()

        while it is not self._m_vec_mapRegion.end():
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: SMapRegion & rRegion = *(it++);
            rRegion = *(it)
            it += 1

            if rRegion.index != lMapIndex:
                continue

            i = 0

## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: while (i++ < 100)
            while i < 100:
                i += 1
                x = number(rRegion.sx + 50, rRegion.ex - 50)
                y = number(rRegion.sy + 50, rRegion.ey - 50)

                if iMaxDistance != 0:
                    d = None

                    d = abs(float(dwCurrentX) - x)

                    if d > iMaxDistance:
                        if x < dwCurrentX:
                            x = dwCurrentX - iMaxDistance
                        else:
                            x = dwCurrentX + iMaxDistance

                    d = abs(float(dwCurrentY) - y)

                    if d > iMaxDistance:
                        if y < dwCurrentY:
                            y = dwCurrentY - iMaxDistance
                        else:
                            y = dwCurrentY + iMaxDistance

                tree = pkSectreeMap.Find(x, y)

                if tree is None:
                    continue

                if tree.IsAttr(int(x), int(y), uint(Globals.ATTR_BLOCK | Globals.ATTR_OBJECT)):
                    continue

                r_pos.x = int(x)
                r_pos.y = int(y)
                return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
            i += 1

        return LGEMiscellaneous.DEFINECONSTANTS.false

    def CreatePrivateMap(self, lMapIndex):
        if lMapIndex >= 10000:
            return 0

        pkMapSectree = self.GetMap(lMapIndex)

        if pkMapSectree is None:
            #lani_err("Cannot find map index %d", lMapIndex)
            return 0

        base = lMapIndex * 10000
        index_cap = 10000
        if lMapIndex == 107 or lMapIndex == 108 or lMapIndex == 109:
            index_cap = (1 if test_server else 51)
        it = self._next_private_index_map_.find(lMapIndex)
        if it == self._next_private_index_map_.end():
            it = self._next_private_index_map_.insert(PrivateIndexMapType.value_type(lMapIndex, 0)).first
        i = None
        next_index = it.second
        for i in range(0, index_cap):
            if self.GetMap(base + next_index) is None:
                break
            next_index += 1
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: if (++next_index >= index_cap)
            if next_index >= index_cap:
                next_index = 0
        if i == index_cap:
            return 0
        lNewMapIndex = base + next_index
        next_index += 1
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: if (++next_index >= index_cap)
        if next_index >= index_cap:
            next_index = 0
        it.second = next_index

        pkMapSectree = LG_NEW_M2 SECTREE_MAP(pkMapSectree)
        self._m_map_pkSectree.insert(dict.value_type(lNewMapIndex, pkMapSectree))

        #sys_log(0, "PRIVATE_MAP: %d created (original %d)", lNewMapIndex, lMapIndex)
        return lNewMapIndex

    def DestroyPrivateMap(self, lMapIndex):
        if lMapIndex < 10000:
            return

        pkMapSectree = self.GetMap(lMapIndex)

        if pkMapSectree is None:
            return

        f = FDestroyPrivateMapEntity()
        pkMapSectree.for_each(f.functor_method)

        self._m_map_pkSectree.pop(lMapIndex)
        LG_DEL_MEM(pkMapSectree)

        #sys_log(0, "PRIVATE_MAP: %d destroyed", lMapIndex)

    def GetDungeonArea(self, lMapIndex):
        it = self._m_map_pkArea.find(lMapIndex)

        if it is self._m_map_pkArea.end():
            return self._m_map_pkArea[-1]
        return it.second

    def SendNPCPosition(self, ch):
        d = ch.GetDesc()
        if d is None:
            return

        lMapIndex = ch.GetMapIndex()

        if self._m_mapNPCPosition[lMapIndex].empty():
            return

        buf = TEMP_BUFFER(8192, DefineConstants.false)
        p = SPacketGCNPCPosition()
        p.header = byte(Globals.LG_HEADER_GC_NPC_POSITION)
        p.count = self._m_mapNPCPosition[lMapIndex].size()

        np = TNPCPosition()

        it = m_mapNPCPosition[lMapIndex].begin()
        while it is not self._m_mapNPCPosition[lMapIndex].end():
            np.bType = it.bType
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            strncpy_s(np.name, sizeof(np.name), it.name, _TRUNCATE)
            np.x = it.x
            np.y = it.y
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            buf.write(np, sizeof(np))
            it += 1

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        p.size = sizeof(p) + buf.size()

        if buf.size() != 0:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            d.BufferedPacket(p, sizeof(SPacketGCNPCPosition))
            d.Packet(buf.read_peek(), buf.size())
        else:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            d.Packet(p, sizeof(SPacketGCNPCPosition))

    def InsertNPCPosition(self, lMapIndex, bType, szName, x, y):
        self._m_mapNPCPosition[lMapIndex].push_back(npc_info(bType, szName, x, y))

    def GetEmpireFromMapIndex(self, lMapIndex):
        if lMapIndex >= 1 and lMapIndex <= 20:
            return 1

        if lMapIndex >= 21 and lMapIndex <= 40:
            return 2

        if lMapIndex >= 41 and lMapIndex <= 60:
            return 3

        if lMapIndex == 184 or lMapIndex == 185:
            return 1

        if lMapIndex == 186 or lMapIndex == 187:
            return 2

        if lMapIndex == 188 or lMapIndex == 189:
            return 3

        if lMapIndex == 190:
            return 1
        if (lMapIndex == 190) or (lMapIndex == 191):
            return 2
        if (lMapIndex == 190) or (lMapIndex == 191) or (lMapIndex == 192):
            return 3

        return 0

    def PurgeMonstersInMap(self, lMapIndex):
        sectree = self.GetMap(lMapIndex)

        if sectree is not None:
            f = FPurgeMonsters()

            sectree.for_each(f.functor_method)

    def PurgeStonesInMap(self, lMapIndex):
        sectree = self.GetMap(lMapIndex)

        if sectree is not None:
            f = FPurgeStones()

            sectree.for_each(f.functor_method)

    def PurgeNPCsInMap(self, lMapIndex):
        sectree = SECTREE_MANAGER.instance().GetMap(lMapIndex)

        if sectree is not None:
            f = FPurgeNPCs()

            sectree.for_each(f.functor_method)

    def GetMonsterCountInMap(self, lMapIndex):
        sectree = self.GetMap(lMapIndex)

        if sectree is not None:
            f = FCountMonsters()

            sectree.for_each(f.functor_method)

            return len(f.m_map_Monsters)

        return 0

    def GetMonsterCountInMap(self, lMapIndex, dwVnum):
        sectree = SECTREE_MANAGER.instance().GetMap(lMapIndex)

        if None is not sectree:
            f = FCountSpecifiedMonster(dwVnum)

            sectree.for_each(f.functor_method)

            return size_t(f.cnt)

        return 0

    def ForAttrRegion(self, lMapIndex, lStartX, lStartY, lEndX, lEndY, lRotate, dwAttr, mode):
        pkMapSectree = self.GetMap(lMapIndex)

        if pkMapSectree is None:
            #lani_err("Cannot find SECTREE_MAP by map index %d", lMapIndex)
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false)) if mode == EAttrRegionMode.ATTR_REGION_MODE_CHECK else LGEMiscellaneous.DEFINECONSTANTS.false

        lStartX -= math.fmod(lStartX, ESectree.CELL_SIZE)
        lStartY -= math.fmod(lStartY, ESectree.CELL_SIZE)
        lEndX += math.fmod(lEndX, ESectree.CELL_SIZE)
        lEndY += math.fmod(lEndY, ESectree.CELL_SIZE)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        lCX = lStartX / int(ESectree.CELL_SIZE)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        lCY = lStartY / int(ESectree.CELL_SIZE)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        lCW = (lEndX - lStartX) / ESectree.CELL_SIZE
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        lCH = (lEndY - lStartY) / ESectree.CELL_SIZE

        #sys_log(1, "ForAttrRegion %d %d ~ %d %d", lStartX, lStartY, lEndX, lEndY)

        lRotate = math.fmod(lRotate, 360)

        if 0 == math.fmod(lRotate, 90):
            return self._ForAttrRegionRightAngle(lMapIndex, lCX, lCY, lCW, lCH, lRotate, dwAttr, mode)

        return self._ForAttrRegionFreeAngle(lMapIndex, lCX, lCY, lCW, lCH, lRotate, dwAttr, mode)

    def SaveAttributeToImage(self, lMapIndex, c_pszFileName, pMapSrc = None):
        pMap = self.GetMap(lMapIndex)

        if pMap is None:
            if pMapSrc:
                pMap = pMapSrc
            else:
                #lani_err("cannot find sectree_map %d", lMapIndex)
                return LGEMiscellaneous.DEFINECONSTANTS.false

        iMapHeight = math.trunc(pMap.m_setting.iHeight / float(math.trunc(128 / float(200))))
        iMapWidth = math.trunc(pMap.m_setting.iWidth / float(math.trunc(128 / float(200))))

        if iMapHeight < 0 or iMapWidth < 0:
            #lani_err("map size error w %d h %d", iMapWidth, iMapHeight)
            return LGEMiscellaneous.DEFINECONSTANTS.false

        #sys_log(0, "SaveAttributeToImage w %d h %d file %s", iMapWidth, iMapHeight, c_pszFileName)

        image = CTargaImage()

        image.Create(512 * iMapWidth, 512 * iMapHeight)

        #sys_log(0, "1")

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Pointer arithmetic is detected on this variable:
#ORIGINAL METINII C CODE: uint * pdwDest = (uint *) image.GetBasePointer();
        pdwDest = image.GetBasePointer(0)

        pixels = 0
        x = None
        x2 = None
        y = None
        y2 = None

        #sys_log(0, "2 %p", pdwDest)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        pdwLine = LG_NEW_M2 uint[(int)ESectree.SECTREE_SIZE / ESectree.CELL_SIZE]

        y = 0
        while y < 4 * iMapHeight:
            y2 = 0
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
            while y2 < ESectree.SECTREE_SIZE / ESectree.CELL_SIZE:
                x = 0
                while x < 4 * iMapWidth:
                    id = SECTREEID()

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
                    id.coord.x = x + pMap.m_setting.iBaseX / int(ESectree.SECTREE_SIZE)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
                    id.coord.y = y + pMap.m_setting.iBaseY / int(ESectree.SECTREE_SIZE)

                    pSec = pMap.Find(id.package)

                    if pSec is None:
                        #lani_err("cannot get sectree for %d %d %d %d", id.coord.x, id.coord.y, pMap.m_setting.iBaseX, pMap.m_setting.iBaseY)
                        continue

                    temp_ref_pdwLine = RefObject(pdwLine);
                    pSec.m_pkAttribute.CopyRow(uint(y2), temp_ref_pdwLine)
                    pdwLine = temp_ref_pdwLine.arg_value

                    if not pdwLine:
                        #lani_err("cannot get attribute line pointer")
                        LG_DEL_MEM_ARRAY(pdwLine)
                        continue

                    x2 = 0
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
                    while x2 < ESectree.SECTREE_SIZE / ESectree.CELL_SIZE:
                        dwColor = None

                        ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'IS_SET' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
                        if IS_SET(pdwLine[x2], Globals.ATTR_WATER):
                            dwColor = 0xff0000ff
                        ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'IS_SET' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
                        elif IS_SET(pdwLine[x2], Globals.ATTR_BANPK):
                            dwColor = 0xff00ff00
                        ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'IS_SET' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
                        elif IS_SET(pdwLine[x2], Globals.ATTR_BLOCK):
                            dwColor = 0xffff0000
                        else:
                            dwColor = 0xffffffff

## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: *(pdwDest++) = dwColor;
                        *(pdwDest) = dwColor
                        pdwDest += 1
                        pixels += 1
                        x2 += 1
                    x += 1
                y2 += 1
            y += 1

        LG_DEL_MEM_ARRAY(pdwLine)
        #sys_log(0, "3")

        if image.Save(c_pszFileName):
            #sys_log(0, "SECTREE: map %d attribute saved to %s (%d bytes)", lMapIndex, c_pszFileName, pixels)
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
        else:
            #lani_err("cannot save file, map_index %d filename %s", lMapIndex, c_pszFileName)
            return LGEMiscellaneous.DEFINECONSTANTS.false

    def _ForAttrRegionRightAngle(self, lMapIndex, lCX, lCY, lCW, lCH, lRotate, dwAttr, mode):
        if 1 == math.trunc(lRotate / float(90)) or 3 == math.trunc(lRotate / float(90)):
            for x in range(0, lCH):
                for y in range(0, lCW):
                    if self._ForAttrRegionCell(lMapIndex, lCX + x, lCY + y, dwAttr, mode):
                        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
        if 0 == math.trunc(lRotate / float(90)) or 2 == math.trunc(lRotate / float(90)):
            for x in range(0, lCW):
                for y in range(0, lCH):
                    if self._ForAttrRegionCell(lMapIndex, lCX + x, lCY + y, dwAttr, mode):
                        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        return LGEMiscellaneous.DEFINECONSTANTS.false if mode == EAttrRegionMode.ATTR_REGION_MODE_CHECK else ((not LGEMiscellaneous.DEFINECONSTANTS.false))

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if ! _WIN32
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
##define min( l, r ) ((l) < (r) ? (l) : (r))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
##define max( l, r ) ((l) < (r) ? (r) : (l))
##endif
    def _ForAttrRegionFreeAngle(self, lMapIndex, lCX, lCY, lCW, lCH, lRotate, dwAttr, mode):
        fx1 = (-math.trunc(lCW / float(2))) * sinf(float(lRotate)/180.0 *3.14) + (-math.trunc(lCH / float(2))) * cosf(float(lRotate)/180.0 *3.14)
        fy1 = (-math.trunc(lCW / float(2))) * cosf(float(lRotate)/180.0 *3.14) - (-math.trunc(lCH / float(2))) * sinf(float(lRotate)/180.0 *3.14)

        fx2 = (+math.trunc(lCW / float(2))) * sinf(float(lRotate)/180.0 *3.14) + (-math.trunc(lCH / float(2))) * cosf(float(lRotate)/180.0 *3.14)
        fy2 = (+math.trunc(lCW / float(2))) * cosf(float(lRotate)/180.0 *3.14) - (-math.trunc(lCH / float(2))) * sinf(float(lRotate)/180.0 *3.14)

        fx3 = (-math.trunc(lCW / float(2))) * sinf(float(lRotate)/180.0 *3.14) + (+math.trunc(lCH / float(2))) * cosf(float(lRotate)/180.0 *3.14)
        fy3 = (-math.trunc(lCW / float(2))) * cosf(float(lRotate)/180.0 *3.14) - (+math.trunc(lCH / float(2))) * sinf(float(lRotate)/180.0 *3.14)

        fx4 = (+math.trunc(lCW / float(2))) * sinf(float(lRotate)/180.0 *3.14) + (+math.trunc(lCH / float(2))) * cosf(float(lRotate)/180.0 *3.14)
        fy4 = (+math.trunc(lCW / float(2))) * cosf(float(lRotate)/180.0 *3.14) - (+math.trunc(lCH / float(2))) * sinf(float(lRotate)/180.0 *3.14)

        fdx1 = fx2 - fx1
        fdy1 = fy2 - fy1
        fdx2 = fx1 - fx3
        fdy2 = fy1 - fy3

        if 0 == fdx1 or 0 == fdx2:
            #lani_err("SECTREE_MANAGER::ForAttrRegion - Unhandled exception. MapIndex: %d", lMapIndex)
            return LGEMiscellaneous.DEFINECONSTANTS.false

        fTilt1 = float(fdy1) / float(fdx1)
        fTilt2 = float(fdy2) / float(fdx2)
        fb1 = fy1 - fTilt1 *fx1
        fb2 = fy1 - fTilt2 *fx1
        fb3 = fy4 - fTilt1 *fx4
        fb4 = fy4 - fTilt2 *fx4

        fxMin = ((fx1) if (fx1) < (((fx2) if (fx2) < (((fx3) if (fx3) < (fx4) else (fx4))) else (((fx3) if (fx3) < (fx4) else (fx4))))) else (((fx2) if (fx2) < (((fx3) if (fx3) < (fx4) else (fx4))) else (((fx3) if (fx3) < (fx4) else (fx4))))))
        fxMax = ((((((fx4) if (fx3) < (fx4) else (fx3))) if (fx2) < (((fx4) if (fx3) < (fx4) else (fx3))) else (fx2))) if (fx1) < (((((fx4) if (fx3) < (fx4) else (fx3))) if (fx2) < (((fx4) if (fx3) < (fx4) else (fx3))) else (fx2))) else (fx1))
        i = int(fxMin)
        while i < int(fxMax):
            fyValue1 = fTilt1 *i + ((fb1) if (fb1) < (fb3) else (fb3))
            fyValue2 = fTilt2 *i + ((fb2) if (fb2) < (fb4) else (fb4))

            fyValue3 = fTilt1 *i + ((fb3) if (fb1) < (fb3) else (fb1))
            fyValue4 = fTilt2 *i + ((fb4) if (fb2) < (fb4) else (fb2))

            fMinValue = None
            fMaxValue = None
            if abs(int(fyValue1)) < abs(int(fyValue2)):
                fMaxValue = fyValue1
            else:
                fMaxValue = fyValue2
            if abs(int(fyValue3)) < abs(int(fyValue4)):
                fMinValue = fyValue3
            else:
                fMinValue = fyValue4

            j = int(((fMinValue) < (fMaxValue) ? (fMinValue) : (fMaxValue)))
            while j < int(((fMaxValue) if (fMinValue) < (fMaxValue) else (fMinValue))):
                if self._ForAttrRegionCell(lMapIndex, lCX + (math.trunc(lCW / float(2))) + i, lCY + (math.trunc(lCH / float(2))) + j, dwAttr, mode):
                    return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
                j += 1
            i += 1

        return LGEMiscellaneous.DEFINECONSTANTS.false if mode == EAttrRegionMode.ATTR_REGION_MODE_CHECK else ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def _ForAttrRegionCell(self, lMapIndex, lCX, lCY, dwAttr, mode):
        id = SECTREEID()

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        id.coord.x = lCX / (ESectree.SECTREE_SIZE / ESectree.CELL_SIZE)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        id.coord.y = lCY / (ESectree.SECTREE_SIZE / ESectree.CELL_SIZE)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        lTreeCX = id.coord.x * (ESectree.SECTREE_SIZE / ESectree.CELL_SIZE)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        lTreeCY = id.coord.y * (ESectree.SECTREE_SIZE / ESectree.CELL_SIZE)

        pSec = self.Get(uint(lMapIndex), id.package)
        if pSec is None:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if mode == EAttrRegionMode.ATTR_REGION_MODE_SET:
            pSec.SetAttribute(uint(lCX - lTreeCX), uint(lCY - lTreeCY), dwAttr)

        elif mode == EAttrRegionMode.ATTR_REGION_MODE_REMOVE:
            pSec.RemoveAttribute(uint(lCX - lTreeCX), uint(lCY - lTreeCY), dwAttr)

        elif mode == EAttrRegionMode.ATTR_REGION_MODE_CHECK:
            if pSec.IsAttr(lCX * int(ESectree.CELL_SIZE), lCY * int(ESectree.CELL_SIZE), uint(Globals.ATTR_OBJECT)):
                return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        else:
            #lani_err("Unknown region mode %u", mode)

        return LGEMiscellaneous.DEFINECONSTANTS.false

    _current_sectree_version = MAKEWORD(0, 3)



class FDestroyPrivateMapEntity:
    def functor_method(self, ent):
        if ent.IsType(EEntityTypes.ENTITY_CHARACTER):
            ch = ent
            #sys_log(0, "PRIVAE_MAP: removing character %s", ch.GetName(LOCALE_LANIATUS))

            if ch.GetDesc():
                DESC_MANAGER.instance().DestroyDesc(ch.GetDesc(), ((not DefineConstants.false)))
            else:
                CHARACTER_MANAGER.instance().DestroyCharacter(ch)
        elif ent.IsType(EEntityTypes.ENTITY_ITEM):
            item = ent
            #sys_log(0, "PRIVATE_MAP: removing item %s", item.GetName(LOCALE_LANIATUS))

            ITEM_MANAGER.instance().DestroyItem(item)
        else:
            #lani_err("PRIVAE_MAP: trying to remove unknown entity %d", ent.GetType())

class FRemoveIfAttr:
    def __init__(self, pkTree, dwAttr):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.m_pkTree = None
        self.m_dwCheckAttr = 0

        self.m_pkTree = pkTree
        self.m_dwCheckAttr = dwAttr

    def functor_method(self, entity):
        if not self.m_pkTree.IsAttr(entity.GetX(), entity.GetY(), self.m_dwCheckAttr):
            return

        if entity.IsType(EEntityTypes.ENTITY_ITEM):
            ITEM_MANAGER.instance().DestroyItem(entity)
        elif entity.IsType(EEntityTypes.ENTITY_CHARACTER):
            ch = entity

            if ch.IsPC():
                pos = pixel_position_s()

                temp_ref_pos = RefObject(pos);
                if SECTREE_MANAGER.instance().GetRecallPositionByEmpire(ch.GetMapIndex(), ch.GetEmpire(), temp_ref_pos):
                    pos = temp_ref_pos.arg_value
                    ch.WarpSet(pos.x, pos.y, 0)
                else:
                    pos = temp_ref_pos.arg_value
                    ch.WarpSet(int(Globals.EMPIRE_START_X(ch.GetEmpire())), int(Globals.EMPIRE_START_Y(ch.GetEmpire())), 0)
            else:
                ch.Dead(NULL, DefineConstants.false)



class FPurgeMonsters:
    def functor_method(self, ent):
        if ent.IsType(EEntityTypes.ENTITY_CHARACTER) == ((not LGEMiscellaneous.DEFINECONSTANTS.false)):
            lpChar = ent

            if lpChar.IsMonster() == ((not LGEMiscellaneous.DEFINECONSTANTS.false)) and not lpChar.IsPet():
                CHARACTER_MANAGER.instance().DestroyCharacter(lpChar)

class FPurgeStones:
    def functor_method(self, ent):
        if ent.IsType(EEntityTypes.ENTITY_CHARACTER) == ((not LGEMiscellaneous.DEFINECONSTANTS.false)):
            lpChar = ent

            if lpChar.IsStone() == ((not LGEMiscellaneous.DEFINECONSTANTS.false)):
                CHARACTER_MANAGER.instance().DestroyCharacter(lpChar)

class FPurgeNPCs:
    def functor_method(self, ent):
        if ent.IsType(EEntityTypes.ENTITY_CHARACTER) == ((not LGEMiscellaneous.DEFINECONSTANTS.false)):
            lpChar = ent

            if lpChar.IsNPC() == ((not LGEMiscellaneous.DEFINECONSTANTS.false)) and not lpChar.IsPet():
                CHARACTER_MANAGER.instance().DestroyCharacter(lpChar)

class FCountMonsters:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.m_map_Monsters = {}


    def functor_method(self, ent):
        if ent.IsType(EEntityTypes.ENTITY_CHARACTER) == ((not LGEMiscellaneous.DEFINECONSTANTS.false)):
            lpChar = ent

            if lpChar.IsMonster() == ((not LGEMiscellaneous.DEFINECONSTANTS.false)):
                self.m_map_Monsters[lpChar.GetVID()] = lpChar.GetVID()

class FCountSpecifiedMonster:

    def __init__(self, id):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.SpecifiedVnum = 0
        self.cnt = size_t()

        self.SpecifiedVnum = id
        self.cnt = 0

    def functor_method(self, ent):
        if ((not LGEMiscellaneous.DEFINECONSTANTS.false)) == ent.IsType(EEntityTypes.ENTITY_CHARACTER):
            pChar = ent

            if ((not LGEMiscellaneous.DEFINECONSTANTS.false)) == pChar.IsStone():
                if pChar.GetMobTable().dwVnum == self.SpecifiedVnum:
                    self.cnt += 1


