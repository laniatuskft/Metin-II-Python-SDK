from building import *

import math

class building: #this class replaces the original namespace 'building'
    OBJECT_MATERIAL_MAX_NUM = 5

    class SLand:

        def __init__(self):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.dwID = 0
            self.lMapIndex = 0
            self.x = 0
            self.y = 0
            self.width = 0
            self.height = 0
            self.dwGuildID = 0
            self.bGuildLevelLimit = 0
            self.lldPrice = 0


    class SObjectMaterial:

        def __init__(self):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.dwItemVnum = 0
            self.dwCount = 0


    class SObjectProto:

        def __init__(self):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.dwVnum = 0
            self.lldPrice = 0
            self.kMaterials = [TObjectMaterial() for _ in range(OBJECT_MATERIAL_MAX_NUM)]
            self.dwUpgradeVnum = 0
            self.dwUpgradeLimitTime = 0
            self.lLife = 0
            self.lRegion = [0 for _ in range(4)]
            self.dwNPCVnum = 0
            self.lNPCX = 0
            self.lNPCY = 0
            self.dwGroupVnum = 0
            self.dwDependOnGroupVnum = 0






    class SObject:

        def __init__(self):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.dwID = 0
            self.dwLandID = 0
            self.dwVnum = 0
            self.lMapIndex = 0
            self.x = 0
            self.y = 0
            self.xRot = 0
            self.yRot = 0
            self.zRot = 0
            self.lLife = 0




class building: #this class replaces the original namespace 'building'
## Laniatus Games Studio Inc. | NOTE: Python has no need of forward class declarations:
#    class CLand

    class CObject(CEntity):
        def __init__(self, pData, pProto):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.m_pProto = None
            self.m_data = TObject()
            self.m_dwVID = 0
            self.m_pkLand = None
            self.m_chNPC = None

            self.m_pProto = pProto
            self.m_dwVID = 0
            self.m_chNPC = None
            super().Initialize(EEntityTypes.ENTITY_OBJECT)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memcpy' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            memcpy(self.m_data, pData, sizeof(TObject))

        def close(self):
            self.Destroy()

        def Destroy(self):
            if self.m_pProto:
                SECTREE_MANAGER.instance().ForAttrRegion(self.GetMapIndex(), self.GetX() + self.m_pProto.lRegion[0], self.GetY() + self.m_pProto.lRegion[1], self.GetX() + self.m_pProto.lRegion[2], self.GetY() + self.m_pProto.lRegion[3], int(self.m_data.zRot), uint(Globals.ATTR_OBJECT), EAttrRegionMode.ATTR_REGION_MODE_REMOVE)

            super().Destroy()

            if self.GetSectree():
                self.GetSectree().RemoveEntity(self)

            self.RemoveSpecialEffect()

        def EncodeInsertPacket(self, entity):
            d = None

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if (!(d = entity->GetDesc()))
            if not(d = entity.GetDesc()):
                return

            #sys_log(0, "ObjectInsertPacket vid %u vnum %u rot %f %f %f", self.m_dwVID, self.m_data.dwVnum, self.m_data.xRot, self.m_data.yRot, self.m_data.zRot)

            pack = packet_add_char()

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memset' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            memset(pack, 0, sizeof(packet_add_char))

            pack.header = byte(Globals.LG_HEADER_GC_CHARACTER_ADD)
            pack.dwVID = self.m_dwVID
            pack.bType = ECharType.CHAR_TYPE_BUILDING
            pack.angle = self.m_data.zRot
            pack.x = self.GetX()
            pack.y = self.GetY()
            pack.z = self.GetZ()
            pack.wRaceNum = self.m_data.dwVnum
            pack.dwAffectFlag[0] = uint(self.m_data.xRot)
            pack.dwAffectFlag[1] = uint(self.m_data.yRot)

            if self.GetLand():
                pass

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            d.Packet(pack, sizeof(pack))

        def EncodeRemovePacket(self, entity):
            d = None

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if (!(d = entity->GetDesc()))
            if not(d = entity.GetDesc()):
                return

            #sys_log(0, "ObjectRemovePacket vid %u", self.m_dwVID)

            pack = packet_del_char()

            pack.header = byte(Globals.LG_HEADER_GC_CHARACTER_DEL)
            pack.id = self.m_dwVID

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            d.Packet(pack, sizeof(packet_del_char))

        def GetID(self):
            return self.m_data.dwID
        def SetVID(self, dwVID):
            self.m_dwVID = dwVID

        def GetVID(self):
            return self.m_dwVID
        def Show(self, lMapIndex, x, y):
            tree = SECTREE_MANAGER.instance().Get(uint(lMapIndex), uint(x), uint(y))

            if tree is None:
                #lani_err("cannot find sectree by %dx%d mapindex %d", x, y, lMapIndex)
                return LGEMiscellaneous.DEFINECONSTANTS.false

            if self.GetSectree():
                self.GetSectree().RemoveEntity(self)
                ViewCleanup()

            self.m_data.lMapIndex = lMapIndex
            self.m_data.x = x
            self.m_data.y = y

            self.Save()

            self.SetMapIndex(lMapIndex)
            self.SetXYZ(x, y, 0)

            tree.InsertEntity(self)
            UpdateSectree()

            SECTREE_MANAGER.instance().ForAttrRegion(lMapIndex, x + self.m_pProto.lRegion[0], y + self.m_pProto.lRegion[1], x + self.m_pProto.lRegion[2], y + self.m_pProto.lRegion[3], int(self.m_data.zRot), uint(Globals.ATTR_OBJECT), EAttrRegionMode.ATTR_REGION_MODE_SET)

            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        def Save(self):
            pass

        def SetLand(self, pkLand):
            self.m_pkLand = pkLand
        def GetLand(self):
            return self.m_pkLand
        def GetVnum(self):
            return uint(self.m_pProto.dwVnum if self.m_pProto is not None else 0)
        def GetGroup(self):
            return uint(self.m_pProto.dwGroupVnum if self.m_pProto is not None else 0)
        def RegenNPC(self):
            if self.m_pProto is None:
                return

            if not self.m_pProto.dwNPCVnum:
                return

            if self.m_pkLand is None:
                return

            dwGuildID = self.m_pkLand.GetOwner()
            pGuild = CGuildManager.instance().FindGuild(dwGuildID)

            if pGuild is None:
                return

            x = self.m_pProto.lNPCX
            y = self.m_pProto.lNPCY
            newX = None
            newY = None

            rot = self.m_data.zRot * 2.0 * LGEMiscellaneous.DEFINECONSTANTS.M_PI / 360.0

            newX = int(((x * cosf(rot)) + (y * sinf(rot))))
            newY = int(((y * cosf(rot)) - (x * sinf(rot))))

            self.m_chNPC = CHARACTER_MANAGER.instance().SpawnMob(self.m_pProto.dwNPCVnum, self.GetMapIndex(), self.GetX() + newX, self.GetY() + newY, self.GetZ(), LGEMiscellaneous.DEFINECONSTANTS.false, int(self.m_data.zRot), ((not DefineConstants.false)))


            if self.m_chNPC is None:
                #lani_err("Cannot create guild npc")
                return

            self.m_chNPC.SetGuild(pGuild)

            if self.m_pProto.dwVnum == 14061 or self.m_pProto.dwVnum == 14062 or self.m_pProto.dwVnum == 14063:
                pPC = quest.CQuestManager.instance().GetPC(pGuild.GetMasterPID())

                if pPC is not None:
                    pPC.SetFlag("alter_of_power.build_level", pGuild.GetLevel(), DefineConstants.false)

        def ApplySpecialEffect(self):
            if self.m_pProto:
                if self.m_pProto.dwVnum == Globals.BUILDING_INCREASE_GUILD_MEMBER_COUNT_SMALL or self.m_pProto.dwVnum == Globals.BUILDING_INCREASE_GUILD_MEMBER_COUNT_MEDIUM or self.m_pProto.dwVnum == Globals.BUILDING_INCREASE_GUILD_MEMBER_COUNT_LARGE:
                    pLand = self.GetLand()
                    guild_id = 0
                    if pLand:
                        guild_id = pLand.GetOwner()
                    pGuild = CGuildManager.instance().FindGuild(guild_id)
                    if pGuild:
                        if self.m_pProto.dwVnum == Globals.BUILDING_INCREASE_GUILD_MEMBER_COUNT_SMALL:
                            pGuild.SetMemberCountBonus(6)
                        elif self.m_pProto.dwVnum == Globals.BUILDING_INCREASE_GUILD_MEMBER_COUNT_MEDIUM:
                            pGuild.SetMemberCountBonus(12)
                        elif self.m_pProto.dwVnum == Globals.BUILDING_INCREASE_GUILD_MEMBER_COUNT_LARGE:
                            pGuild.SetMemberCountBonus(18)
                        if map_allow_find(pLand.GetMapIndex()):
                            pGuild.BroadcastMemberCountBonus()

        def RemoveSpecialEffect(self):
            if self.m_pProto:
                if self.m_pProto.dwVnum == Globals.BUILDING_INCREASE_GUILD_MEMBER_COUNT_SMALL or self.m_pProto.dwVnum == Globals.BUILDING_INCREASE_GUILD_MEMBER_COUNT_MEDIUM or self.m_pProto.dwVnum == Globals.BUILDING_INCREASE_GUILD_MEMBER_COUNT_LARGE:
                    pLand = self.GetLand()
                    guild_id = 0
                    if pLand:
                        guild_id = pLand.GetOwner()
                    pGuild = CGuildManager.instance().FindGuild(guild_id)
                    if pGuild:
                        pGuild.SetMemberCountBonus(0)
                        if map_allow_find(pLand.GetMapIndex()):
                            pGuild.BroadcastMemberCountBonus()

        def Reconstruct(self, dwVnum):
            r = SECTREE_MANAGER.instance().GetMapRegion(self.m_data.lMapIndex)
            if r is None:
                return

            pLand = self.GetLand()
            pLand.RequestDeleteObject(self.GetID())
            pLand.RequestCreateObject(dwVnum, self.m_data.lMapIndex, self.m_data.x - r.sx, self.m_data.y - r.sy, self.m_data.xRot, self.m_data.yRot, self.m_data.zRot, LGEMiscellaneous.DEFINECONSTANTS.false)

        def GetNPC(self):
            return self.m_chNPC


    class CLand:
        def __init__(self, pData):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.m_data = TLand()
            self.m_map_pkObject = {}
            self.m_map_pkObjectByVID = {}

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memcpy' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            memcpy(self.m_data, pData, sizeof(TLand))

        def close(self):
            self.Destroy()

        def Destroy(self):
            it = self.m_map_pkObject.begin()

            while it is not self.m_map_pkObject.end():
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: LPOBJECT pkObj = (it++)->second;
                pkObj = (it).second
                it += 1
                CManager.instance().UnregisterObject(LPOBJECT(pkObj))
                LG_DEL_MEM(pkObj)

            self.m_map_pkObject.clear()
            self.m_map_pkObjectByVID.clear()

        def GetData(self):
            return TLand(self.m_data)

        def PutData(self, data):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memcpy' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            memcpy(self.m_data, data, sizeof(TLand))

            if self.m_data.dwGuildID:
                r = SECTREE_MANAGER.instance().GetMapRegion(self.m_data.lMapIndex)

                if r:
                    LaniatusDefVariables = CharacterVectorInteractor()

                    if CHARACTER_MANAGER.instance().GetCharactersByRaceNum(20040, i):
                        it = i.begin()

                        while it is not i.end():
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: CHARACTER* ch = *(it++);
                            ch = *(it)
                            it += 1

                            if ch.GetMapIndex() != self.m_data.lMapIndex:
                                continue

                            x = ch.GetX() - r.sx
                            y = ch.GetY() - r.sy

                            if x > self.m_data.x + self.m_data.width or x < self.m_data.x:
                                continue

                            if y > self.m_data.y + self.m_data.height or y < self.m_data.y:
                                continue

                            CHARACTER_MANAGER.instance().DestroyCharacter(ch)

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: uint GetID() const
        def GetID(self):
            return self.m_data.dwID
        def SetOwner(self, dwGuild):
            if self.m_data.dwGuildID != dwGuild:
                self.m_data.dwGuildID = dwGuild
                self.RequestUpdate(dwGuild)

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: uint GetOwner() const
        def GetOwner(self):
            return self.m_data.dwGuildID
        def InsertObject(self, pkObj):
            self.m_map_pkObject.update({pkObj.GetID(): pkObj})
            self.m_map_pkObjectByVID.update({pkObj.GetVID(): pkObj})

            pkObj.SetLand(self)

        def FindObject(self, dwID):
            it = self.m_map_pkObject.find(dwID)

            if it is self.m_map_pkObject.end():
                return None

            return it.second

        def FindObjectByVID(self, dwVID):
            it = self.m_map_pkObjectByVID.find(dwVID)
            if it is self.m_map_pkObjectByVID.end():
                return None

            return it.second

        def FindObjectByVnum(self, dwVnum):
            it = m_map_pkObject.begin()
            while it is not self.m_map_pkObject.end():
                pObj = it.second
                if pObj.GetVnum() == dwVnum:
                    return LPOBJECT(pObj)
                it += 1

            return None

        def FindObjectByGroup(self, dwGroupVnum):
            it = m_map_pkObject.begin()
            while it is not self.m_map_pkObject.end():
                pObj = it.second
                if pObj.GetGroup() == dwGroupVnum:
                    return LPOBJECT(pObj)
                it += 1

            return None

        def FindObjectByNPC(self, npc):
            if npc is None:
                return None

            it = m_map_pkObject.begin()
            while it is not self.m_map_pkObject.end():
                pObj = it.second
                if pObj.GetNPC() is npc:
                    return LPOBJECT(pObj)
                it += 1

            return None

        def DeleteObject(self, dwID):
            pkObj = LPOBJECT()

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if (!(pkObj = FindObject(dwID)))
            if not(pkObj = self.FindObject(dwID)):
                return

            #sys_log(0, "Land::DeleteObject %u", dwID)
            CManager.instance().UnregisterObject(LPOBJECT(pkObj))
            CHARACTER_MANAGER.instance().DestroyCharacter(pkObj.GetNPC())

            self.m_map_pkObject.pop(dwID)
            self.m_map_pkObjectByVID.pop(dwID)

            LG_DEL_MEM(pkObj)

        def RequestCreateObject(self, dwVnum, lMapIndex, x, y, xRot, yRot, zRot, checkAnother):
            rkSecTreeMgr = SECTREE_MANAGER.instance()
            pkProto = CManager.instance().GetObjectProto(dwVnum)

            if pkProto is None:
                #lani_err("Invalid Object vnum %u", dwVnum)
                return LGEMiscellaneous.DEFINECONSTANTS.false
            r = rkSecTreeMgr.GetMapRegion(lMapIndex)
            if r is None:
                return LGEMiscellaneous.DEFINECONSTANTS.false

            #sys_log(0, "RequestCreateObject(vnum=%u, map=%d, pos=(%d,%d), rot=(%.1f,%.1f,%.1f) region(%d,%d ~ %d,%d)", dwVnum, lMapIndex, x, y, xRot, yRot, zRot, r.sx, r.sy, r.ex, r.ey)

            x += r.sx
            y += r.sy

            sx = r.sx + self.m_data.x
            ex = sx + self.m_data.width
            sy = r.sy + self.m_data.y
            ey = sy + self.m_data.height

            osx = x + pkProto.lRegion[0]
            osy = y + pkProto.lRegion[1]
            oex = x + pkProto.lRegion[2]
            oey = y + pkProto.lRegion[3]

            rad = zRot * 2.0 * LGEMiscellaneous.DEFINECONSTANTS.M_PI / 360.0

            tsx = int((pkProto.lRegion[0] * cosf(rad) + pkProto.lRegion[1] * sinf(rad) + x))
            tsy = int((pkProto.lRegion[0] * -sinf(rad) + pkProto.lRegion[1] * cosf(rad) + y))

            tex = int((pkProto.lRegion[2] * cosf(rad) + pkProto.lRegion[3] * sinf(rad) + x))
            tey = int((pkProto.lRegion[2] * -sinf(rad) + pkProto.lRegion[3] * cosf(rad) + y))

            if tsx < sx or tex > ex or tsy < sy or tey > ey:
                #lani_err("invalid position: object is outside of land region\nLAND: %d %d ~ %d %d\nOBJ: %d %d ~ %d %d", sx, sy, ex, ey, osx, osy, oex, oey)
                return LGEMiscellaneous.DEFINECONSTANTS.false

            if checkAnother:
                if rkSecTreeMgr.ForAttrRegion(lMapIndex, osx, osy, oex, oey, int(zRot), uint(Globals.ATTR_OBJECT), EAttrRegionMode.ATTR_REGION_MODE_CHECK):
                    #lani_err("another object already exist")
                    return LGEMiscellaneous.DEFINECONSTANTS.false
                f = FIsIn(osx, osy, oex, oey)
                rkSecTreeMgr.GetMap(lMapIndex).for_each(f.functor_method)

                if f.bIn:
                    #lani_err("another object already exist")
                    return LGEMiscellaneous.DEFINECONSTANTS.false

            p = SPacketGDCreateObject()

            p.dwVnum = dwVnum
            p.dwLandID = self.m_data.dwID
            p.lMapIndex = lMapIndex
            p.x = x
            p.y = y
            p.xRot = xRot
            p.yRot = yRot
            p.zRot = zRot

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            db_clientdesc.DBPacket(Globals.LG_HEADER_GD_CREATE_OBJECT, 0, p, sizeof(SPacketGDCreateObject))
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        def RequestDeleteObject(self, dwID):
            if self.FindObject(dwID) is None:
                #lani_err("no object by id %u", dwID)
                return

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            db_clientdesc.DBPacket(Globals.LG_HEADER_GD_DELETE_OBJECT, 0, dwID, sizeof(uint))
            #sys_log(0, "RequestDeleteObject id %u", dwID)

        def RequestDeleteObjectByVID(self, dwVID):
            pkObj = LPOBJECT()

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if (!(pkObj = FindObjectByVID(dwVID)))
            if not(pkObj = self.FindObjectByVID(dwVID)):
                #lani_err("no object by vid %u", dwVID)
                return

            dwID = pkObj.GetID()
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            db_clientdesc.DBPacket(Globals.LG_HEADER_GD_DELETE_OBJECT, 0, dwID, sizeof(uint))
            #sys_log(0, "RequestDeleteObject vid %u id %u", dwVID, dwID)

        def RequestUpdate(self, dwGuild):
            a = [0 for _ in range(2)]

            a[0] = self.GetID()
            a[1] = dwGuild

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            db_clientdesc.DBPacket(Globals.LG_HEADER_GD_UPDATE_LAND, 0, a[0], sizeof(uint) * 2)
            #sys_log(0, "RequestUpdate id %u guild %u", a[0], a[1])

        def ClearLand(self):
            iter = self.m_map_pkObject.begin()

            while iter is not self.m_map_pkObject.end():
                self.RequestDeleteObject(iter.second.GetID())
                iter += 1

            self.SetOwner(0)

            r = self.GetData()
            region = SECTREE_MANAGER.instance().GetMapRegion(r.lMapIndex)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
            CHARACTER_MANAGER.instance().SpawnMob(20040, r.lMapIndex, region.sx + r.x + (r.width / 2), region.sy + r.y + (r.height / 2), 0, DefineConstants.false, -1, ((not DefineConstants.false)))

        def RequestCreateWall(self, nMapIndex, rot):
            WALL_ANOTHER_CHECKING_ENABLE = LGEMiscellaneous.DEFINECONSTANTS.false

            land = self.GetData()

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
            center_x = land.x + land.width / 2
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
            center_y = land.y + land.height / 2

            wall_x = center_x
            wall_y = center_y
            wall_half_w = 1000
            wall_half_h = 1362

            if rot == 0.0:
                door_x = wall_x
                door_y = wall_y + wall_half_h
                self.RequestCreateObject(uint(Globals.WALL_DOOR_VNUM), nMapIndex, wall_x, wall_y + wall_half_h, door_x, door_y, 0.0, WALL_ANOTHER_CHECKING_ENABLE)
                self.RequestCreateObject(uint(Globals.WALL_BACK_VNUM), nMapIndex, wall_x, wall_y - wall_half_h, door_x, door_y, 0.0, WALL_ANOTHER_CHECKING_ENABLE)
                self.RequestCreateObject(uint(Globals.WALL_LEFT_VNUM), nMapIndex, wall_x - wall_half_w, wall_y, door_x, door_y, 0.0, WALL_ANOTHER_CHECKING_ENABLE)
                self.RequestCreateObject(uint(Globals.WALL_RIGHT_VNUM), nMapIndex, wall_x + wall_half_w, wall_y, door_x, door_y, 0.0, WALL_ANOTHER_CHECKING_ENABLE)
            elif rot == 180.0:
                door_x = wall_x
                door_y = wall_y - wall_half_h
                self.RequestCreateObject(uint(Globals.WALL_DOOR_VNUM), nMapIndex, wall_x, wall_y - wall_half_h, door_x, door_y, 180.0, WALL_ANOTHER_CHECKING_ENABLE)
                self.RequestCreateObject(uint(Globals.WALL_BACK_VNUM), nMapIndex, wall_x, wall_y + wall_half_h, door_x, door_y, 0.0, WALL_ANOTHER_CHECKING_ENABLE)
                self.RequestCreateObject(uint(Globals.WALL_LEFT_VNUM), nMapIndex, wall_x - wall_half_w, wall_y, door_x, door_y, 0.0, WALL_ANOTHER_CHECKING_ENABLE)
                self.RequestCreateObject(uint(Globals.WALL_RIGHT_VNUM), nMapIndex, wall_x + wall_half_w, wall_y, door_x, door_y, 0.0, WALL_ANOTHER_CHECKING_ENABLE)
            elif rot == 90.0:
                door_x = wall_x + wall_half_h
                door_y = wall_y
                self.RequestCreateObject(uint(Globals.WALL_DOOR_VNUM), nMapIndex, wall_x + wall_half_h, wall_y, door_x, door_y, 90.0, WALL_ANOTHER_CHECKING_ENABLE)
                self.RequestCreateObject(uint(Globals.WALL_BACK_VNUM), nMapIndex, wall_x - wall_half_h, wall_y, door_x, door_y, 90.0, WALL_ANOTHER_CHECKING_ENABLE)
                self.RequestCreateObject(uint(Globals.WALL_LEFT_VNUM), nMapIndex, wall_x, wall_y - wall_half_w, door_x, door_y, 90.0, WALL_ANOTHER_CHECKING_ENABLE)
                self.RequestCreateObject(uint(Globals.WALL_RIGHT_VNUM), nMapIndex, wall_x, wall_y + wall_half_w, door_x, door_y, 90.0, WALL_ANOTHER_CHECKING_ENABLE)
            elif rot == 270.0:
                door_x = wall_x - wall_half_h
                door_y = wall_y
                self.RequestCreateObject(uint(Globals.WALL_DOOR_VNUM), nMapIndex, wall_x - wall_half_h, wall_y, door_x, door_y, 90.0, WALL_ANOTHER_CHECKING_ENABLE)
                self.RequestCreateObject(uint(Globals.WALL_BACK_VNUM), nMapIndex, wall_x + wall_half_h, wall_y, door_x, door_y, 90.0, WALL_ANOTHER_CHECKING_ENABLE)
                self.RequestCreateObject(uint(Globals.WALL_LEFT_VNUM), nMapIndex, wall_x, wall_y - wall_half_w, door_x, door_y, 90.0, WALL_ANOTHER_CHECKING_ENABLE)
                self.RequestCreateObject(uint(Globals.WALL_RIGHT_VNUM), nMapIndex, wall_x, wall_y + wall_half_w, door_x, door_y, 90.0, WALL_ANOTHER_CHECKING_ENABLE)

            if test_server:
                self.RequestCreateObject(uint(Globals.FLAG_VNUM), nMapIndex, land.x + 50, land.y + 50, 0, 0, 0.0, WALL_ANOTHER_CHECKING_ENABLE)
                self.RequestCreateObject(uint(Globals.FLAG_VNUM), nMapIndex, land.x + land.width - 50, land.y + 50, 0, 0, 90.0, WALL_ANOTHER_CHECKING_ENABLE)
                self.RequestCreateObject(uint(Globals.FLAG_VNUM), nMapIndex, land.x + land.width - 50, land.y + land.height - 50, 0, 0, 180.0, WALL_ANOTHER_CHECKING_ENABLE)
                self.RequestCreateObject(uint(Globals.FLAG_VNUM), nMapIndex, land.x + 50, land.y + land.height - 50, 0, 0, 270.0, WALL_ANOTHER_CHECKING_ENABLE)
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        def RequestDeleteWall(self):
            iter = self.m_map_pkObject.begin()

            while iter is not self.m_map_pkObject.end():
                id = iter.second.GetID()
                vnum = iter.second.GetVnum()

                if (vnum == Globals.WALL_DOOR_VNUM) or (vnum == Globals.WALL_BACK_VNUM) or (vnum == Globals.WALL_LEFT_VNUM) or (vnum == Globals.WALL_RIGHT_VNUM):
                    self.RequestDeleteObject(id)


                if test_server:
                    if Globals.FLAG_VNUM == vnum:
                        self.RequestDeleteObject(id)


                iter += 1

        def RequestCreateWallBlocks(self, dwVnum, nMapIndex, wallSize, doorEast, doorWest, doorSouth, doorNorth):
            r = self.GetData()

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
            startX = r.x + (r.width / 2) - (1300 + wallSize *500)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
            startY = r.y + (r.height / 2) + (1300 + wallSize *500)

            corner = dwVnum - 4
            wall = dwVnum - 3
            door = dwVnum - 1

            checkAnother = LGEMiscellaneous.DEFINECONSTANTS.false
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to pointers to value types:
#ORIGINAL METINII C CODE: int* ptr = NULL;
            ptr = None
            delta = 1
            rot = 270

            doorOpen = [False for _ in range(4)]
            doorOpen[0] = doorWest
            doorOpen[1] = doorNorth
            doorOpen[2] = doorEast
            doorOpen[3] = doorSouth

            if wallSize > 3:
                wallSize = 3
            elif wallSize < 0:
                wallSize = 0

            LaniatusDefVariables = 0
            while LaniatusDefVariables < 4:
                if LaniatusDefVariables == 0:
                    delta = -1
                    ptr = startY
                elif LaniatusDefVariables == 1:
                    delta = 1
                    ptr = startX
                elif LaniatusDefVariables == 2:
                    ptr = startY
                    delta = 1
                elif LaniatusDefVariables == 3:
                    ptr = startX
                    delta = -1

                self.RequestCreateObject(corner, nMapIndex, startX, startY, 0, 0, rot, checkAnother)

                ptr = ptr + (700 * delta)

                if doorOpen[LaniatusDefVariables]:
                    temp_ref_startX = RefObject(startX);
                    temp_ref_startY = RefObject(startY);
                    self._DrawWall(wall, nMapIndex, temp_ref_startX, temp_ref_startY, wallSize, rot)
                    startY = temp_ref_startY.arg_value
                    startX = temp_ref_startX.arg_value

                    ptr = ptr + (700 * delta)

                    self.RequestCreateObject(door, nMapIndex, startX, startY, 0, 0, rot, checkAnother)

                    ptr = ptr + (1300 * delta)

                    temp_ref_startX2 = RefObject(startX);
                    temp_ref_startY2 = RefObject(startY);
                    self._DrawWall(wall, nMapIndex, temp_ref_startX2, temp_ref_startY2, wallSize, rot)
                    startY = temp_ref_startY2.arg_value
                    startX = temp_ref_startX2.arg_value
                else:
                    temp_ref_startX3 = RefObject(startX);
                    temp_ref_startY3 = RefObject(startY);
                    self._DrawWall(wall, nMapIndex, temp_ref_startX3, temp_ref_startY3, wallSize *2 + 4, rot)
                    startY = temp_ref_startY3.arg_value
                    startX = temp_ref_startX3.arg_value

                ptr = ptr + (100 * delta)
                LaniatusDefVariables += 1
                rot -= 90

            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        def RequestDeleteWallBlocks(self, dwID):
            iter = self.m_map_pkObject.begin()

            corner = dwID - 4
            wall = dwID - 3
            door = dwID - 1
            dwVnum = 0

            while iter is not self.m_map_pkObject.end():
                dwVnum = iter.second.GetVnum()

                if dwVnum == corner or dwVnum == wall or dwVnum == door:
                    self.RequestDeleteObject(iter.second.GetID())
                iter += 1

        def GetMapIndex(self):
            return self.m_data.lMapIndex


        def _DrawWall(self, dwVnum, nMapIndex, x, y, length, zRot):
            rot = int(zRot)
            rot = (math.trunc((math.fmod(rot, 360)) / float(90))) * 90

            dx = 0
            dy = 0

            if rot == 0:
                dx = -500
                dy = 0

            elif rot == 90:
                dx = 0
                dy = 500

            elif rot == 180:
                dx = 500
                dy = 0

            elif rot == 270:
                dx = 0
                dy = -500

            for LaniatusDefVariables in range(0, length):
                self.RequestCreateObject(dwVnum, nMapIndex, x.arg_value, y.arg_value, 0, 0, rot, LGEMiscellaneous.DEFINECONSTANTS.false)
                x.arg_value += dx
                y.arg_value += dy

    class CManager(singleton):
        def __init__(self):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.m_vec_kObjectProto = []
            self.m_map_pkObjectProto = {}
            self.m_map_pkLand = {}
            self.m_map_pkObjByID = {}
            self.m_map_pkObjByVID = {}


        def close(self):
            self.Destroy()

        def Destroy(self):
            it = self.m_map_pkLand.begin()
            while it is not self.m_map_pkLand.end():
                LG_DEL_MEM(it.second)
                it += 1
            self.m_map_pkLand.clear()

        def FinalizeBoot(self):
            it = self.m_map_pkObjByID.begin()

            while it is not self.m_map_pkObjByID.end():
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: LPOBJECT pkObj = (it++)->second;
                pkObj = (it).second
                it += 1

                pkObj.Show(pkObj.GetMapIndex(), pkObj.GetX(), pkObj.GetY())
                pkObj.RegenNPC()
                pkObj.ApplySpecialEffect()

            #sys_log(0, "FinalizeBoot")

            it2 = self.m_map_pkLand.begin()

            while it2 is not self.m_map_pkLand.end():
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: CLand * pkLand = (it2++)->second;
                pkLand = (it2).second
                it2 += 1
                r = pkLand.GetData()

                #sys_log(0, "LandMaster map_index=%d pos=(%d, %d)", r.lMapIndex, r.x, r.y)

                if r.dwGuildID != 0:
                    continue

                if not map_allow_find(r.lMapIndex):
                    continue

                region = SECTREE_MANAGER.instance().GetMapRegion(r.lMapIndex)
                if region is None:
                    continue

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
                CHARACTER_MANAGER.instance().SpawnMob(20040, r.lMapIndex, region.sx + r.x + (r.width / 2), region.sy + r.y + (r.height / 2), 0, DefineConstants.false, -1, ((not DefineConstants.false)))

        def LoadObjectProto(self, pProto, size):
            self.m_vec_kObjectProto.resize(size)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memcpy' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            memcpy(self.m_vec_kObjectProto[0], pProto, sizeof(TObjectProto) * size)

            for LaniatusDefVariables in range(0, size):
                r = self.m_vec_kObjectProto[LaniatusDefVariables]

                #sys_log(0, "ObjectProto %u price %lld upgrade %u upg_limit %u life %d NPC %u", r.dwVnum, r.lldPrice, r.dwUpgradeVnum, r.dwUpgradeLimitTime, r.lLife, r.dwNPCVnum)

                j = 0
                while j < OBJECT_MATERIAL_MAX_NUM:
                    if not r.kMaterials[j].dwItemVnum:
                        break

                    if None is ITEM_MANAGER.instance().GetTable(r.kMaterials[j].dwItemVnum):
                        #lani_err("          mat: ERROR!! no item by vnum %u", r.kMaterials[j].dwItemVnum)
                        return LGEMiscellaneous.DEFINECONSTANTS.false

                    #sys_log(0, "          mat: %u %u", r.kMaterials[j].dwItemVnum, r.kMaterials[j].dwCount)
                    j += 1

                self.m_map_pkObjectProto.update({r.dwVnum: self.m_vec_kObjectProto[LaniatusDefVariables]})

            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        def GetObjectProto(self, dwVnum):
            it = self.m_map_pkObjectProto.find(dwVnum)

            if it is self.m_map_pkObjectProto.end():
                return None

            return it.second

        def LoadLand(self, pTable):
            pkLand = LG_NEW_M2 CLand(pTable)
            self.m_map_pkLand.update({pkLand.GetID(): pkLand})

            #sys_log(0, "LAND: %u map %d %dx%d w %u h %u", pTable.dwID, pTable.lMapIndex, pTable.x, pTable.y, pTable.width, pTable.height)

            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        def FindLand(self, dwID):
            it = self.m_map_pkLand.find(dwID)

            if it is self.m_map_pkLand.end():
                return None

            return it.second

        def FindLand(self, lMapIndex, x, y):
            #sys_log(0, "BUILDING: FindLand %d %d %d", lMapIndex, x, y)

            r = SECTREE_MANAGER.instance().GetMapRegion(lMapIndex)

            if r is None:
                return None

            x -= r.sx
            y -= r.sy

            it = self.m_map_pkLand.begin()

            while it is not self.m_map_pkLand.end():
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: CLand * pkLand = (it++)->second;
                pkLand = (it).second
                it += 1
                r = pkLand.GetData()

                if r.lMapIndex != lMapIndex:
                    continue

                if x < r.x or y < r.y:
                    continue

                if x > r.x + r.width or y > r.y + r.height:
                    continue

                return pkLand

            return None

        def FindLandByGuild(self, GID):
            it = self.m_map_pkLand.begin()

            while it is not self.m_map_pkLand.end():
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: CLand * pkLand = (it++)->second;
                pkLand = (it).second
                it += 1

                if pkLand.GetData().dwGuildID == GID:
                    return pkLand

            return None

        def UpdateLand(self, pTable):
            pkLand = self.FindLand(pTable.dwID)

            if pkLand is None:
                #lani_err("cannot find land by id %u", pTable.dwID)
                return

            pkLand.PutData(pTable)

            cont = DESC_MANAGER.instance().GetClientSet()

            it = cont.begin()

            p = packet_land_list()

            p.header = byte(Globals.LG_HEADER_GC_LAND_LIST)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            p.size = sizeof(packet_land_list) + sizeof(TLandPacketElement)

            e = TLandPacketElement()

            e.dwID = pTable.dwID
            e.x = pTable.x
            e.y = pTable.y
            e.width = pTable.width
            e.height = pTable.height
            e.dwGuildID = pTable.dwGuildID

            #sys_log(0, "BUILDING: UpdateLand %u pos %dx%d guild %u", e.dwID, e.x, e.y, e.dwGuildID)

            guild = CGuildManager.instance().FindGuild(pTable.dwGuildID)
            while it is not cont.end():
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: DESC* d = *(it++);
                d = *(it)
                it += 1

                if d.GetCharacter() is not None and d.GetCharacter().GetMapIndex() == pTable.lMapIndex:
                    d.GetCharacter().SendGuildName(guild)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                    d.BufferedPacket(p, sizeof(packet_land_list))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                    d.Packet(e, sizeof(TLandPacketElement))

        def LoadObject(self, pTable, isBoot = LGEMiscellaneous.DefineConstants.false):
            pkLand = self.FindLand(pTable.dwLandID)

            if not map_allow_find(pTable.lMapIndex):
                return LGEMiscellaneous.DEFINECONSTANTS.false

            if pkLand is None:
                #sys_log(0, "Cannot find land by id %u", pTable.dwLandID)
                return LGEMiscellaneous.DEFINECONSTANTS.false

            pkProto = self.GetObjectProto(pTable.dwVnum)

            if pkProto is None:
                #lani_err("Cannot find object %u in prototype (id %u)", pTable.dwVnum, pTable.dwID)
                return LGEMiscellaneous.DEFINECONSTANTS.false

            #sys_log(0, "OBJ: id %u vnum %u map %d pos %dx%d", pTable.dwID, pTable.dwVnum, pTable.lMapIndex, pTable.x, pTable.y)

            pkObj = LG_NEW_M2 CObject(pTable, pkProto)

            dwVID = CHARACTER_MANAGER.instance().AllocVID()
            pkObj.SetVID(dwVID)

            self.m_map_pkObjByVID.update({dwVID: pkObj})
            self.m_map_pkObjByID.update({pTable.dwID: pkObj})

            pkLand.InsertObject(LPOBJECT(pkObj))

            if not isBoot:
                pkObj.Show(pTable.lMapIndex, pTable.x, pTable.y)
            else:
                pkObj.SetMapIndex(pTable.lMapIndex)
                pkObj.SetXYZ(pTable.x, pTable.y, 0)

            if not isBoot:
                if pkProto.dwNPCVnum:
                    pkObj.RegenNPC()

                pkObj.ApplySpecialEffect()

            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        def DeleteObject(self, dwID):
            #sys_log(0, "OBJ_DEL: %u", dwID)

            it = self.m_map_pkObjByID.find(dwID)

            if it is self.m_map_pkObjByID.end():
                return

            it.second.GetLand().DeleteObject(dwID)

        def UnregisterObject(self, pkObj):
            self.m_map_pkObjByID.pop(pkObj.GetID())
            self.m_map_pkObjByVID.pop(pkObj.GetVID())

        def FindObjectByVID(self, dwVID):
            it = self.m_map_pkObjByVID.find(dwVID)

            if it is self.m_map_pkObjByVID.end():
                return None

            return it.second

        def SendLandList(self, d, lMapIndex):
            e = TLandPacketElement()

            buf = TEMP_BUFFER(8192, DefineConstants.false)

            wCount = 0

            it = self.m_map_pkLand.begin()

            while it is not self.m_map_pkLand.end():
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: CLand * pkLand = (it++)->second;
                pkLand = (it).second
                it += 1
                r = pkLand.GetData()

                if r.lMapIndex != lMapIndex:
                    continue

                ch = d.GetCharacter()
                if ch:
                    guild = CGuildManager.instance().FindGuild(r.dwGuildID)
                    ch.SendGuildName(guild)

                e.dwID = r.dwID
                e.x = r.x
                e.y = r.y
                e.width = r.width
                e.height = r.height
                e.dwGuildID = r.dwGuildID

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                buf.write(e, sizeof(TLandPacketElement))
                wCount += 1

            #sys_log(0, "SendLandList map %d count %u elem_size: %d", lMapIndex, wCount, buf.size())

            if wCount != 0:
                p = packet_land_list()

                p.header = byte(Globals.LG_HEADER_GC_LAND_LIST)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                p.size = sizeof(packet_land_list) + buf.size()

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                d.BufferedPacket(p, sizeof(packet_land_list))
                d.Packet(buf.read_peek(), buf.size())

        def ClearLand(self, dwLandID):
            pLand = self.FindLand(dwLandID)

            if pLand is None:
                #sys_log(0, "LAND_CLEAR: there is no LAND id like %d", dwLandID)
                return

            pLand.ClearLand()

            #sys_log(0, "LAND_CLEAR: request Land Clear. LandID: %d", pLand.GetID())

        def ClearLandByGuildID(self, dwGuildID):
            pLand = self.FindLandByGuild(dwGuildID)

            if pLand is None:
                #sys_log(0, "LAND_CLEAR: there is no GUILD id like %d", dwGuildID)
                return

            pLand.ClearLand()

            #sys_log(0, "LAND_CLEAR: request Land Clear. LandID: %d", pLand.GetID())


class FIsIn:

    def __init__(self, sx_, sy_, ex_, ey_):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.sx = 0
        self.sy = 0
        self.ex = 0
        self.ey = 0
        self.bIn = False

        self.sx = sx_
        self.sy = sy_
        self.ex = ex_
        self.ey = ey_
        self.bIn = LGEMiscellaneous.DEFINECONSTANTS.false

    def functor_method(self, ent):
        if ent.IsType(EEntityTypes.ENTITY_CHARACTER):
            ch = ent
            if ch.IsMonster():
                return
            if self.sx <= ch.GetX() and ch.GetX() <= self.ex and self.sy <= ch.GetY() and ch.GetY() <= self.ey:
                self.bIn = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
