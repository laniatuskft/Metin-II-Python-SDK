import math

class xmas: #this class replaces the original namespace 'xmas'
    MOB_SANTA_VNUM = 20031
    MOB_XMAS_TREE_VNUM = 20032
    MOB_XMAS_FIRWORK_SELLER_VNUM = 9004

    @staticmethod
    def ProcessEventFlag(name, prev_value, value):
        if name == "xmas_snow" or name == "xmas_boom" or name == "xmas_song" or name == "xmas_tree":
            c_ref_set = DESC_MANAGER.instance().GetClientSet()

            it = c_ref_set.begin()
            while it is not c_ref_set.end():
                ch = it.GetCharacter()

                if ch is None:
                    continue

                ch.ChatPacket(EChatType.CHAT_TYPE_COMMAND, "%s %d", name, value)
                it += 1

            if name == "xmas_boom":
                if value != 0 and prev_value == 0:
                    xmas.SpawnEventHelper(((not LGEMiscellaneous.DEFINECONSTANTS.false)))
                elif value == 0 and prev_value != 0:
                    xmas.SpawnEventHelper(LGEMiscellaneous.DEFINECONSTANTS.false)
            elif name == "xmas_tree":
                if value > 0 and prev_value == 0:
                    LaniatusDefVariables = CharacterVectorInteractor()

                    if not CHARACTER_MANAGER.instance().GetCharactersByRaceNum(uint(xmas.MOB_XMAS_TREE_VNUM), i):
                        CHARACTER_MANAGER.instance().SpawnMob(uint(xmas.MOB_XMAS_TREE_VNUM), 61, 76500 + 358400, 60900 + 153600, 0, LGEMiscellaneous.DEFINECONSTANTS.false, -1, ((not DefineConstants.false)))
                elif prev_value > 0 and value == 0:
                    LaniatusDefVariables = CharacterVectorInteractor()

                    if CHARACTER_MANAGER.instance().GetCharactersByRaceNum(uint(xmas.MOB_XMAS_TREE_VNUM), i):
                        it = i.begin()

                        while it is not i.end():
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: CHARACTER_MANAGER::instance().DestroyCharacter(*it++);
                            CHARACTER_MANAGER.instance().DestroyCharacter(it)
                            it += 1
        elif name == "xmas_santa":
            if value == 0:
                    LaniatusDefVariables = CharacterVectorInteractor()

                    if CHARACTER_MANAGER.instance().GetCharactersByRaceNum(uint(xmas.MOB_SANTA_VNUM), i):
                        it = i.begin()

                        while it is not i.end():
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: CHARACTER_MANAGER::instance().DestroyCharacter(*it++);
                            CHARACTER_MANAGER.instance().DestroyCharacter(it)
                            it += 1


            elif value == 1:
                if map_allow_find(61):
                    quest.CQuestManager.instance().RequestSetEventFlag("xmas_santa", 2)

                    LaniatusDefVariables = CharacterVectorInteractor()

                    if CHARACTER_MANAGER.instance().GetCharactersByRaceNum(uint(xmas.MOB_SANTA_VNUM), i):
                        CHARACTER_MANAGER.instance().SpawnMobRandomPosition(uint(xmas.MOB_SANTA_VNUM), 61)

            elif value == 2:
                pass

    @staticmethod
    def SpawnSanta(lMapIndex, iTimeGapSec):
        if test_server:
            iTimeGapSec = math.trunc(iTimeGapSec / float(60))

        #sys_log(0, "santa respawn time = %d", iTimeGapSec)
        info = Globals.AllocEventInfo()

        info.lMapIndex = lMapIndex

        event_create_ex(spawn_santa_event, info, ((iTimeGapSec) * passes_per_sec))

    class SNPCSellFireworkPosition:

        def __init__(self):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.lMapIndex = 0
            self.x = 0
            self.y = 0

    @staticmethod
    def SpawnEventHelper(spawn):
        if spawn == ((not LGEMiscellaneous.DEFINECONSTANTS.false)):
            positions = [SNPCSellFireworkPosition(1, 615, 618), SNPCSellFireworkPosition(3, 500, 625), SNPCSellFireworkPosition(21, 598, 665), SNPCSellFireworkPosition(23, 476, 360), SNPCSellFireworkPosition(41, 318, 629), SNPCSellFireworkPosition(43, 478, 375), SNPCSellFireworkPosition(0, 0, 0)]

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Pointer arithmetic is detected on this variable:
#ORIGINAL METINII C CODE: SNPCSellFireworkPosition* p = positions;
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
            p = SNPCSellFireworkPosition(positions)
            while p.lMapIndex != 0:
                if map_allow_find(p.lMapIndex):
                    posBase = pixel_position_s()
                    if not SECTREE_MANAGER.instance().GetMapBasePositionByMapIndex(p.lMapIndex, posBase):
                        #lani_err("cannot get map base position %d", p.lMapIndex)
                        p += 1
                        continue

                    CHARACTER_MANAGER.instance().SpawnMob(uint(xmas.MOB_XMAS_FIRWORK_SELLER_VNUM), p.lMapIndex, posBase.x + p.x * 100, posBase.y + p.y * 100, 0, LGEMiscellaneous.DEFINECONSTANTS.false, -1, ((not DefineConstants.false)))
                p += 1
        else:
            LaniatusDefVariables = CharacterVectorInteractor()

            if CHARACTER_MANAGER.instance().GetCharactersByRaceNum(uint(xmas.MOB_XMAS_FIRWORK_SELLER_VNUM), i):
                it = i.begin()

                while it is not i.end():
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: CHARACTER_MANAGER::instance().DestroyCharacter(*it++);
                    CHARACTER_MANAGER.instance().DestroyCharacter(it)
                    it += 1



class xmas: #this class replaces the original namespace 'xmas'

    class spawn_santa_info(event_info_data):

        def __init__(self):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.lMapIndex = 0

            self.lMapIndex = 0

    @staticmethod
    def (UnnamedParameter):
        info = if isinstance(event.info, spawn_santa_info) else None

        if info is None:
            #lani_err("spawn_santa_event> <Factor> Null pointer")
            return 0

        lMapIndex = info.lMapIndex

        if quest.CQuestManager.instance().GetEventFlag("xmas_santa") == 0:
            return 0

        LaniatusDefVariables = CharacterVectorInteractor()

        if CHARACTER_MANAGER.instance().GetCharactersByRaceNum(uint(xmas.MOB_SANTA_VNUM), i):
            return 0

        if CHARACTER_MANAGER.instance().SpawnMobRandomPosition(uint(xmas.MOB_SANTA_VNUM), lMapIndex):
            #sys_log(0, "santa comes to town!")
            return 0

        return ((5) * passes_per_sec)
