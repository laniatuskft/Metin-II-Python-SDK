class quest: #this class replaces the original namespace 'quest'
    class FWarpToHome:
        def functor_method(self, ent):
            if ent.IsType(EEntityTypes.ENTITY_CHARACTER):
                ch = ent

                if ch.IsPC() == ((not LGEMiscellaneous.DEFINECONSTANTS.false)) and ch.IsGM() != ((not LGEMiscellaneous.DEFINECONSTANTS.false)):
                    if ((ch.GetX() >= 764503 and ch.GetX() <= 772362) and (ch.GetY() >= 22807 and ch.GetY() <= 26499)) == LGEMiscellaneous.DEFINECONSTANTS.false:
                        ch.GoHome()

    @staticmethod
    def dance_event_go_home(L):
        pSecMap = SECTREE_MANAGER.instance().GetMap(115)

        if pSecMap is not None:
            f = FWarpToHome()
            pSecMap.for_each(f.functor_method)

        return 0

    @staticmethod
    def RegisterDanceEventFunctionTable():
        dance_event_functions = [luaL_reg("gohome", dance_event_go_home), luaL_reg(None, None)]

        quest.CQuestManager.instance().AddLuaFunctionTable("dance_event", dance_event_functions)

