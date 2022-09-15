class building: #this class replaces the original namespace 'building'
    OBJECT_MATERIAL_MAX_NUM = 5

    class SLand:

        def __init__(self):
            #instance fields found by Laniatus Games Studio Inc. T.F |:
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
            #instance fields found by Laniatus Games Studio Inc. T.F |:
            self.dwItemVnum = 0
            self.dwCount = 0


    class SObjectProto:

        def __init__(self):
            #instance fields found by Laniatus Games Studio Inc. T.F |:
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
            #instance fields found by Laniatus Games Studio Inc. T.F |:
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


