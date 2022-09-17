from enum import Enum
import math

class ENUM_PROFILER(Enum):
    PF_IDLE = 0
    PF_HEARTBEAT = 1
    NUM_PF = 2

class EProfile(Enum):
    PROF_EVENT = 0
    PROF_CHR_UPDATE = 1
    PROF_IO = 2
    PROF_HEARTBEAT = 3
    PROF_MAX_NUM = 4

## Laniatus Games Studio Inc. | NOTE: Anonymous namespaces are not defined:
#namespace
class SendDisconnectFunc:
    def functor_method(self, d):
        if d.GetCharacter():
            if d.GetCharacter().GetGMLevel() == EGMLevels.GM_PLAYER:
                d.GetCharacter().ChatPacket(EChatType.CHAT_TYPE_COMMAND, "quit Shutdown(SendDisconnectFunc)")

class DisconnectFunc:
    def functor_method(self, d):
        if d.GetType() == EDescType.DESC_TYPE_CONNECTOR:
            return

        if d.IsPhase(EPhase.PHASE_P2P):
            return

        d.SetPhase(EPhase.PHASE_CLOSE)

def main(argc, args):
    ilInit()

    Globals.WriteVersion()

    sectree_manager = SECTREE_MANAGER()
    char_manager = CHARACTER_MANAGER()
    item_manager = ITEM_MANAGER()
    shop_manager = CShopManager()
    mob_manager = CMobManager()
    motion_manager = CMotionManager()
    party_manager = CPartyManager()
    LG_SKILL_manager = CSkillManager()
    pvp_manager = CPVPManager()
    lzo_manager = LZOManager()
    db_manager = DBManager()
    account_db = AccountDB()

    log_manager = LogManager()
    messenger_manager = MessengerManager()
    p2p_manager = P2P_MANAGER()
    guild_manager = CGuildManager()
    mark_manager = CGuildMarkManager()
    dungeon_manager = CDungeonManager()
    refine_manager = CRefineManager()
    priv_manager = CPrivManager()
    war_map_manager = CWarMapManager()
    building_manager = building.CManager()
    target_manager = CTargetManager()
    marriage_manager = marriage.CManager()
    wedding_manager = marriage.WeddingManager()
    item_addon_manager = CItemAddonManager()
    OXEvent_manager = COXEventManager()
    horsename_manager = CHorseNameManager()
    desc_manager = DESC_MANAGER()
    SkillPowerByLevel = CTableBySkill()
    polymorph_utils = CPolymorphUtils()
    profiler = CProfiler()
    spam_mgr = SpamManager()
    dl_manager = CDragonLairManager()
    dsManager = DSManager()

    if Globals.start(argc, args) == 0:
        Globals.CleanUpForEarlyExit()


    quest_manager = quest.CQuestManager()
    if not quest_manager.Initialize():
        Globals.CleanUpForEarlyExit()

    MessengerManager.instance().Initialize()
    CGuildManager.instance().Initialize()
    fishing.Initialize()
    OXEvent_manager.Initialize()

    if not g_bAuthServer:
        Globals.Cube_init()
        Globals.Blend_Item_init()
        Globals.ani_init()

    while (Globals.idle()) != 0:
        pass

    #sys_log(0, "<shutdown> Starting...")
    Globals.g_bShutdown = ((not LGEMiscellaneous.DEFINECONSTANTS.false))
    g_bNoMoreClient = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    if g_bAuthServer:
        iLimit = math.trunc(DBManager.instance().CountQuery() / float(50))
        LaniatusDefVariables = 0

        condition = True
        while condition:
            dwCount = DBManager.instance().CountQuery()
            Globals.#sys_log(0, "Queries %u", dwCount)

            if dwCount == 0:
                break

            Globals.usleep(500000)

            LaniatusDefVariables += 1
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: if (++i >= iLimit)
            if LaniatusDefVariables >= iLimit:
                if dwCount == DBManager.instance().CountQuery():
                    break
            condition = 1

    #sys_log(0, "<shutdown> Destroying COXEventManager...")
    OXEvent_manager.Destroy()

    #sys_log(0, "<shutdown> Disabling signal timer...")
    signal_timer_disable()

    #sys_log(0, "<shutdown> Shutting down CHARACTER_MANAGER...")
    char_manager.GracefulShutdown()
    #sys_log(0, "<shutdown> Shutting down ITEM_MANAGER...")
    item_manager.GracefulShutdown()

    #sys_log(0, "<shutdown> Flushing db_clientdesc...")
    db_clientdesc.FlushOutput()
    #sys_log(0, "<shutdown> Flushing p2p_manager...")
    p2p_manager.FlushOutput()

    #sys_log(0, "<shutdown> Destroying CShopManager...")
    shop_manager.Destroy()
    #sys_log(0, "<shutdown> Destroying CHARACTER_MANAGER...")
    char_manager.Destroy()
    #sys_log(0, "<shutdown> Destroying ITEM_MANAGER...")
    item_manager.Destroy()
    #sys_log(0, "<shutdown> Destroying DESC_MANAGER...")
    desc_manager.Destroy()
    #sys_log(0, "<shutdown> Destroying quest::CQuestManager...")
    quest_manager.Destroy()
    #sys_log(0, "<shutdown> Destroying building::CManager...")
    building_manager.Destroy()

    Globals.destroy()

    return 1