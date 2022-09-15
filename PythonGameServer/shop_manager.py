import math

## Laniatus Games Studio Inc. | NOTE: Python has no need of forward class declarations:
#class CShop

class CShopManager(singleton):


    ##include <_boost_func_of_void/algorithm/string/predicate.hpp>

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self._m_map_pkShop = {}
        self._m_map_pkShopByNPCVnum = {}
        self._m_map_pkShopByPC = {}


    def close(self):
        self.Destroy()

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Pointer arithmetic is detected on the parameter 'table':
#ORIGINAL METINII C CODE: bool Initialize(SShopTable * table, int size)
    def Initialize(self, table, size):
        if self._m_map_pkShop:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        i = None

        i = 0
        while i < size:
            ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The typedef 'LPSHOP' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
            shop = LG_NEW_M2 CShop

            if not shop.Create(table.dwVnum, table.dwNPCVnum, table.items):
                LG_DEL_MEM(shop)
                continue

            self._m_map_pkShop.insert(TShopMap.value_type(table.dwVnum, shop))
            self._m_map_pkShopByNPCVnum.insert(TShopMap.value_type(table.dwNPCVnum, shop))
            i += 1
            table += 1
        szShopTableExFileName = str(['\0' for _ in range(256)])

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        snprintf(szShopTableExFileName, sizeof(szShopTableExFileName), "%s/shop_table_ex.txt", LocaleService_GetBasePath().c_str())

        return self.ReadShopTableEx(szShopTableExFileName)

    def Destroy(self):
        it = m_map_pkShopByNPCVnum.begin()
        while it is not self._m_map_pkShopByNPCVnum.end():
            it.second = None
            it += 1
        self._m_map_pkShopByNPCVnum.clear()
        self._m_map_pkShop.clear()

    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The typedef 'LPSHOP' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
    def Get(self, dwVnum):
        it = self._m_map_pkShop.find(dwVnum)

        if it is self._m_map_pkShop.end():
            return None

        return (it.second)

    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The typedef 'LPSHOP' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
    def GetByNPCVnum(self, dwVnum):
        it = self._m_map_pkShopByNPCVnum.find(dwVnum)

        if it is self._m_map_pkShopByNPCVnum.end():
            return None

        return (it.second)

    def StartShopping(self, pkChr, pkChrShopKeeper, iShopVnum = 0):
        if pkChr.GetShopOwner() is pkChrShopKeeper:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if pkChrShopKeeper.IsPC():
            return LGEMiscellaneous.DEFINECONSTANTS.false

        if pkChr.IsOpenSafebox() or pkChr.GetExchange() is not None or pkChr.GetMyShop() is not None or pkChr.IsCubeOpen() or pkChr.IsAcceWindowOpen():
            pkChr.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You cannot trade in the Warehouse if another Trade Window is open."))
            return LGEMiscellaneous.DEFINECONSTANTS.false

        distance = Globals.DISTANCE_APPROX(pkChr.GetX() - pkChrShopKeeper.GetX(), pkChr.GetY() - pkChrShopKeeper.GetY())

        if distance >= Globals.SHOP_MAX_DISTANCE:
            #sys_log(1, "SHOP: TOO_FAR: %s distance %d", pkChr.GetName(LOCALE_LANIATUS), distance)
            return LGEMiscellaneous.DEFINECONSTANTS.false

        ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The typedef 'LPSHOP' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
        pkShop = LPSHOP()

        if iShopVnum != 0:
## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: pkShop = Get(iShopVnum);
            pkShop.copy_from(self.Get(uint(iShopVnum)))
        else:
## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: pkShop = GetByNPCVnum(pkChrShopKeeper->GetRaceNum());
            pkShop.copy_from(self.GetByNPCVnum(pkChrShopKeeper.GetRaceNum()))

        if pkShop is None:
            #sys_log(1, "SHOP: NO SHOP")
            return LGEMiscellaneous.DEFINECONSTANTS.false

        bOtherEmpire = LGEMiscellaneous.DEFINECONSTANTS.false

        if pkChr.GetEmpire() != pkChrShopKeeper.GetEmpire():
            bOtherEmpire = ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        pkShop.AddGuest(pkChr, pkChrShopKeeper.GetVID(), bOtherEmpire)
        pkChr.SetShopOwner(pkChrShopKeeper)
        #sys_log(0, "SHOP: START: %s", pkChr.GetName(LOCALE_LANIATUS))
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def StopShopping(self, ch):
        ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The typedef 'LPSHOP' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
        shop = LPSHOP()

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The following assignments within expression was not converted by # Laniatus Games Studio Inc. |:
#ORIGINAL METINII C CODE: if (!(shop = ch->GetShop()))
        if not(shop = ch.GetShop()):
            return

        ch.SetMyShopTime()
        shop.RemoveGuest(ch)
        #sys_log(0, "SHOP: END: %s", ch.GetName(LOCALE_LANIATUS))

    def Buy(self, ch, pos):
        if ch.GetShop() is None:
            return

        if ch.GetShopOwner() is None:
            return

        if Globals.DISTANCE_APPROX(ch.GetX() - ch.GetShopOwner().GetX(), ch.GetY() - ch.GetShopOwner().GetY()) > 2000:
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You are too far away from the shop to buy."))
            return

        pkShop = ch.GetShop()

        ch.SetMyShopTime()

        ret = pkShop.Buy(ch, pos)

        if EPacketShopSubHeaders.SHOP_SUBLG_HEADER_GC_OK != ret:
            pack = packet_shop()

            pack.header = byte(Globals.LG_HEADER_GC_SHOP)
            pack.subheader = byte(ret)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            pack.size = sizeof(packet_shop)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            ch.GetDesc().Packet(pack, sizeof(pack))

    def Sell(self, ch, bCell, wCount = 0):
        if ch.GetShop() is None:
            return

        if ch.GetShopOwner() is None:
            return

        if not ch.CanHandleItem(DefineConstants.false, DefineConstants.false):
            return

        if ch.GetShop().IsPCShop():
            return

        if Globals.DISTANCE_APPROX(ch.GetX()-ch.GetShopOwner().GetX(), ch.GetY()-ch.GetShopOwner().GetY())>2000:
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You are too far away from the shop to sell."))
            return

        item = ch.GetInventoryItem(bCell)

        if item is None:
            return

        if item.IsEquipped() == ((not LGEMiscellaneous.DEFINECONSTANTS.false)):
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You cannot sell items you are already equipped."))
            return

        if ((not LGEMiscellaneous.DEFINECONSTANTS.false)) == item.isLocked():
            return

        ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'IS_SET' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
        if IS_SET(item.GetAntiFlag(), LaniatusEITMAntiFlagDcs.ITEM_ANTIFLAG_SELL):
            return

        lldPrice = None

        if wCount == 0 or wCount > item.GetCount():
            wCount = ushort(item.GetCount())

        lldPrice = item.GetShopBuyPrice()

        ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The #define macro 'IS_SET' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
        if IS_SET(item.GetFlag(), EItemFlag.ITEM_FLAG_COUNT_PER_1GOLD):
            if lldPrice == 0:
                lldPrice = wCount
            else:
                lldPrice = math.trunc(wCount / float(lldPrice))
        else:
            lldPrice *= wCount

        if test_server:
            #sys_log(0, "Sell Item price id %d %s itemid %d", ch.GetPlayerID(), ch.GetName(LOCALE_LANIATUS), item.GetID())


        nTotalMoney = int(ch.GetGold()) + int(lldPrice)

        if MaxGold.GOLD_MAX <= nTotalMoney:
            #lani_err("[OVERFLOW_GOLD] id %u name %s gold %lld", ch.GetPlayerID(), ch.GetName(LOCALE_LANIATUS), ch.GetGold())
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("You carry more than 2 Billion Yang, you cannot trade."))
            return

        #sys_log(0, "SHOP: SELL: %s item name: %s(x%d):%u price: %lld", ch.GetName(LOCALE_LANIATUS), item.GetName(LOCALE_LANIATUS), wCount, item.GetID(), lldPrice)

        if wCount == item.GetCount():

            ITEM_MANAGER.instance().RemoveItem(item, "SELL")
        else:
            item.SetCount(item.GetCount() - wCount)

        ch.PointChange(EPointTypes.LG_POINT_GOLD, lldPrice, LGEMiscellaneous.DEFINECONSTANTS.false, DefineConstants.false)

    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The typedef 'LPSHOP' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
    def CreatePCShop(self, ch, pTable, wItemCount):
        if self.FindPCShop(ch.GetVID()):
            return None

        ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The typedef 'LPSHOP' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
        pkShop = LG_NEW_M2 CShop
        pkShop.SetPCShop(ch)
        pkShop.SetShopItems(pTable, wItemCount)
        ch.RemoveGoodAffect()

        self._m_map_pkShopByPC.insert(TShopMap.value_type(ch.GetVID(), pkShop))
        return LPSHOP(pkShop)

    ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The typedef 'LPSHOP' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
    def FindPCShop(self, dwVID):
        it = self._m_map_pkShopByPC.find(dwVID)

        if it is self._m_map_pkShopByPC.end():
            return None

        return it.second

    def DestroyPCShop(self, ch):
        ## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The typedef 'LPSHOP' was defined in multiple preprocessor conditionals and cannot be replaced in-line:
        pkShop = self.FindPCShop(ch.GetVID())

        if pkShop is None:
            return

        ch.SetMyShopTime()

        self._m_map_pkShopByPC.pop(ch.GetVID())
        LG_DEL_MEM(pkShop)

    def ReadShopTableEx(self, stFileName):
        fp = fopen(stFileName, "rb")
        if None is fp:
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
        fclose(fp)

        loader = CGroupTextParseTreeLoader()
        if not loader.Load(stFileName):
            #lani_err("%s Load fail.", stFileName)
            return LGEMiscellaneous.DEFINECONSTANTS.false

        pShopNPCGroup = loader.GetGroup("shopnpc")
        if None is pShopNPCGroup:
            #lani_err("Group ShopNPC is not exist.")
            return LGEMiscellaneous.DEFINECONSTANTS.false

        map_npcShop = std::multimap()

            v = std::unordered_set()

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Only expression lambdas are converted by # Laniatus Games Studio Inc. |:
# auto ExDelete = [v](TShopMap& c)
            #            {
            #                for (auto it = c.begin(); !c.empty() && it != c.end();)
            #                {
            #                    const auto shop = it->second
            #                    if (shop && shop->IsShopEx())
            #                    {
            #                        it = c.erase(it)
            #                        v.insert(shop)
            #                    }
            #                    else
            #                        ++it
            #                }
            #            }
            ExDelete(self._m_map_pkShopByNPCVnum)
            ExDelete(self._m_map_pkShop)
            for del_ in v:
                del_ = None

        i = 0
        while i < pShopNPCGroup.GetRowCount():
            npcVnum = None
            shopName = ""
            if (not pShopNPCGroup.GetValue(i, "npc", npcVnum)) or not pShopNPCGroup.GetValue(i, "group", shopName):
                #lani_err("Invalid row(%d). Group ShopNPC rows must have 'npc', 'group' columns", i)
                return LGEMiscellaneous.DEFINECONSTANTS.false
            std::transform(shopName.begin(), shopName.end(), shopName.begin(), (int(*)(int))std::tolower)
            pShopGroup = loader.GetGroup(shopName)
            if pShopGroup is None:
                #lani_err("Group %s is not exist.", shopName)
                return LGEMiscellaneous.DEFINECONSTANTS.false
            table = SShopTableEx()
            if not Globals.ConvertToShopItemTable(pShopGroup, table):
                #lani_err("Cannot read Group %s.", shopName)
                return LGEMiscellaneous.DEFINECONSTANTS.false
            if npcVnum in self._m_map_pkShopByNPCVnum.keys():
                #lani_err("%d cannot have both original shop and extended shop", npcVnum)
                return LGEMiscellaneous.DEFINECONSTANTS.false

            map_npcShop.insert(std::multimap .value_type(npcVnum, table))
            i += 1

        it = map_npcShop.begin()
        while it is not map_npcShop.end():
            npcVnum = it.first
            table = it.second
            if table.dwVnum in self._m_map_pkShop.keys():
                #lani_err("Shop vnum(%d) already exists", table.dwVnum)
                return LGEMiscellaneous.DEFINECONSTANTS.false
            shop_it = self._m_map_pkShopByNPCVnum.find(npcVnum)

            pkShopEx = None
            if self._m_map_pkShopByNPCVnum.end() is shop_it:
                pkShopEx = LG_NEW_M2 CShopEx
                pkShopEx.Create(0, npcVnum)
                self._m_map_pkShopByNPCVnum.insert(TShopMap.value_type(npcVnum, pkShopEx))
            else:
                pkShopEx = if isinstance(shop_it.second, CShopEx) else None
                if None is pkShopEx:
                    #lani_err("WTF!!! It can't be happend. NPC(%d) Shop is not extended version.", shop_it.first)
                    return LGEMiscellaneous.DEFINECONSTANTS.false

            if pkShopEx.GetTabCount() >= LGEMiscellaneous.SHOP_TAB_COUNT_MAX:
                #lani_err("ShopEx cannot have tab more than %d", LGEMiscellaneous.SHOP_TAB_COUNT_MAX)
                return LGEMiscellaneous.DEFINECONSTANTS.false

            if table.dwVnum in self._m_map_pkShop.keys():
                #lani_err("Shop vnum(%d) already exist.", table.dwVnum)
                return LGEMiscellaneous.DEFINECONSTANTS.false

            self._m_map_pkShop.insert(TShopMap.value_type(table.dwVnum, pkShopEx))
            pkShopEx.AddShopTable(table)
            it += 1

        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
