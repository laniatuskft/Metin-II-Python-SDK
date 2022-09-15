class CDragonLair:
    def __init__(self, guildID, BaseMapID, PrivateMapID):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self._StartTime_ = 0
        self._GuildID_ = 0
        self._BaseMapIndex_ = 0
        self._PrivateMapIndex_ = 0

        self._GuildID_ = guildID
        self._BaseMapIndex_ = BaseMapID
        self._PrivateMapIndex_ = PrivateMapID
        self._StartTime_ = get_global_time()

    def close(self):
        pass

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: uint GetEstimatedTime() const
    def GetEstimatedTime(self):
        return get_global_time() - self._StartTime_

    def OnDragonDead(self, pDragon):
        #sys_log(0, "DragonLair: ������� �׾��ȿ")


class CDragonLairManager(singleton):
    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self._LairMap_ = _boost_func_of_void.unordered_map()


    def close(self):
        pass

    def Start(self, MapIndexFrom, BaseMapIndex, GuildID):
        instanceMapIndex = SECTREE_MANAGER.instance().CreatePrivateMap(BaseMapIndex)
        if instanceMapIndex == 0:
            #lani_err("CDragonLairManager::Start() : no private map index available")
            return LGEMiscellaneous.DEFINECONSTANTS.false

        pMap = SECTREE_MANAGER.instance().GetMap(MapIndexFrom)

        if None is not pMap:
            pTargetMap = SECTREE_MANAGER.instance().GetMap(BaseMapIndex)

            if None is pTargetMap:
                return LGEMiscellaneous.DEFINECONSTANTS.false

            pRegionInfo = SECTREE_MANAGER.instance().GetMapRegion(pTargetMap.m_setting.iIndex)

            if None is not pRegionInfo:
                f = FWarpToDragronLairWithGuildMembers(GuildID, instanceMapIndex, 844000, 1066900)

                pMap.for_each(f.functor_method)

                self._LairMap_.insert((GuildID, LG_NEW_M2 CDragonLair(GuildID, BaseMapIndex, instanceMapIndex)))

                strMapBasePath = LocaleService_GetMapPath()

                strMapBasePath += "/" + pRegionInfo.strMapName + "/instance_regen.txt"

                #sys_log(0, "%s", strMapBasePath)

                regen_do(strMapBasePath, instanceMapIndex, pTargetMap.m_setting.iBaseX, pTargetMap.m_setting.iBaseY, None, ((not LGEMiscellaneous.DEFINECONSTANTS.false)))

                return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        return LGEMiscellaneous.DEFINECONSTANTS.false

    def OnDragonDead(self, pDragon, KillerGuildID):
        if None is pDragon:
            return

        if LGEMiscellaneous.DEFINECONSTANTS.false == pDragon.IsMonster():
            return

        iter = self._LairMap_.find(KillerGuildID)

        if self._LairMap_.end() == iter:
            return

        pMap = SECTREE_MANAGER.instance().GetMap(pDragon.GetMapIndex())

        if None == iter.second or None is pMap:
            self._LairMap_.erase(iter)
            return

        iter.second.OnDragonDead(pDragon)

        info = None
        info = Globals.AllocEventInfo()

        info.step = 0
        info.pLair = iter.second
        info.InstanceMapIndex = pDragon.GetMapIndex()

        event_create_ex(DragonLair_Collapse_Event, info, ((10) * passes_per_sec))

        self._LairMap_.erase(iter)

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: size_t GetLairCount() const
    def GetLairCount(self):
        return self._LairMap_.size()


class FWarpToDragronLairWithGuildMembers:

    def __init__(self, guildID, map, X, Y):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.dwGuildID = 0
        self.mapIndex = 0
        self.x = 0
        self.y = 0

        self.dwGuildID = guildID
        self.mapIndex = map
        self.x = X
        self.y = Y

    def functor_method(self, ent):
        if None is not ent and ((not LGEMiscellaneous.DEFINECONSTANTS.false)) == ent.IsType(EEntityTypes.ENTITY_CHARACTER):
            pChar = ent

            if ((not LGEMiscellaneous.DEFINECONSTANTS.false)) == pChar.IsPC():
                if None is not pChar.GetGuild():
                    if self.dwGuildID == pChar.GetGuild().GetID():
                        pChar.WarpSet(self.x, self.y, self.mapIndex)

class FWarpToVillage:
    def functor_method(self, ent):
        if None is not ent:
            pChar = ent

            if None is not pChar:
                if ((not LGEMiscellaneous.DEFINECONSTANTS.false)) == pChar.IsPC():
                    pChar.GoHome()

class tag_DragonLair_Collapse_EventInfo(event_info_data):

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.step = 0
        self.pLair = None
        self.InstanceMapIndex = 0

        self.step = 0
        self.pLair = None
        self.InstanceMapIndex = 0