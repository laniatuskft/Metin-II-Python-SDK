import math

class marriage: #this class replaces the original namespace 'marriage'
    WEDDING_MAP_INDEX = 81

    class WeddingMap:
        def __init__(self, dwMapIndex, dwPID1, dwPID2):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self._m_dwMapIndex = 0
            self._m_pEndEvent = _boost_func_of_void.intrusive_ptr()
            self._m_set_pkChr = charset_t()
            self._m_isDark = False
            self._m_isSnow = False
            self._m_isMusic = False
            self._dwPID1 = 0
            self._dwPID2 = 0
            self._m_stMusicFileName = ""

            self._m_dwMapIndex = dwMapIndex
            self._m_pEndEvent = None
            self._m_isDark = LGEMiscellaneous.DEFINECONSTANTS.false
            self._m_isSnow = LGEMiscellaneous.DEFINECONSTANTS.false
            self._m_isMusic = LGEMiscellaneous.DEFINECONSTANTS.false
            self._dwPID1 = dwPID1
            self._dwPID2 = dwPID2

        def close(self):
            event_cancel(self._m_pEndEvent)

        def GetMapIndex(self):
            return self._m_dwMapIndex
        def WarpAll(self):
            f = FWarpEveryone()
            for_each(self._m_set_pkChr.begin(), self._m_set_pkChr.end(), f.functor_method)

        def DestroyAll(self):
            #sys_log(0, "WeddingMap::DestroyAll: m_set_pkChr size %zu", self._m_set_pkChr.size())

            f = FDestroyEveryone()

            it = m_set_pkChr.begin()
            while it is not self._m_set_pkChr.end():
                f.functor_method(*it)
                it = m_set_pkChr.begin()

        def Notice(self, psz):
            f = FNotice(psz)
            for_each(self._m_set_pkChr.begin(), self._m_set_pkChr.end(), f.functor_method)

        def SetEnded(self):
            if self._m_pEndEvent:
                #lani_err("WeddingMap::SetEnded - ALREADY EndEvent(m_pEndEvent=%x)", Globals.get_pointer(self._m_pEndEvent))
                return

            info = Globals.AllocEventInfo()

            info.pWeddingMap = self

            self._m_pEndEvent = event_create_ex(wedding_end_event, info, ((5) * passes_per_sec))

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if __MULTI_LANGUAGE_SYSTEM__
            self.Notice("The Wedding will soon end.")
            self.Notice("Players will be teleported to town now.")
##else
            self.Notice(LC_TEXT("The Wedding will soon end."))
            self.Notice(LC_TEXT("Players will be teleported to town now."))
##endif

            it = m_set_pkChr.begin()
            while it is not self._m_set_pkChr.end():
                ch = *it
                if ch.GetPlayerID() == self._dwPID1 or ch.GetPlayerID() == self._dwPID2:
                    continue

                if ch.GetLevel() < 10:
                    continue

                ch.AutoGiveItem(27002, 5)
                it += 1

        def IncMember(self, ch):
            if self.IsMember(ch) == ((not LGEMiscellaneous.DEFINECONSTANTS.false)):
                return

            self._m_set_pkChr.insert(ch)

            self.SendLocalEvent(ch)

            if ch.GetLevel() < 10:
                ch.SetObserverMode(((not LGEMiscellaneous.DEFINECONSTANTS.false)))

        def DecMember(self, ch):
            if self.IsMember(ch) == LGEMiscellaneous.DEFINECONSTANTS.false:
                return

            self._m_set_pkChr.erase(ch)

            if ch.GetLevel() < 10:
                ch.SetObserverMode(LGEMiscellaneous.DEFINECONSTANTS.false)

        def IsMember(self, ch):
            if self._m_set_pkChr.size() <= 0:
                return LGEMiscellaneous.DEFINECONSTANTS.false

            return self._m_set_pkChr.find(ch) != self._m_set_pkChr.end()

        def SetDark(self, bSet):
            if self._m_isDark != bSet:
                self._m_isDark = bSet

                if self._m_isDark:
                    self.ShoutInMap(EChatType.CHAT_TYPE_COMMAND, "DayMode dark")
                else:
                    self.ShoutInMap(EChatType.CHAT_TYPE_COMMAND, "DayMode light")

        def SetSnow(self, bSet):
            if self._m_isSnow != bSet:
                self._m_isSnow = bSet

                if self._m_isSnow:
                    self.ShoutInMap(EChatType.CHAT_TYPE_COMMAND, "xmas_snow 1")
                else:
                    self.ShoutInMap(EChatType.CHAT_TYPE_COMMAND, "xmas_snow 0")

        def SetMusic(self, bSet, musicFileName):
            if self._m_isMusic != bSet:
                self._m_isMusic = bSet
                self._m_stMusicFileName = musicFileName

                szCommand = str(['\0' for _ in range(256)])
                if self._m_isMusic:
                    temp_ref_szCommand = RefObject(szCommand);
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                    self.ShoutInMap(EChatType.CHAT_TYPE_COMMAND, self._BuildCommandPlayMusic(temp_ref_szCommand, sizeof(szCommand), 1, self._m_stMusicFileName))
                    szCommand = temp_ref_szCommand.arg_value
                else:
                    temp_ref_szCommand2 = RefObject(szCommand);
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                    self.ShoutInMap(EChatType.CHAT_TYPE_COMMAND, self._BuildCommandPlayMusic(temp_ref_szCommand2, sizeof(szCommand), 0, "default"))
                    szCommand = temp_ref_szCommand2.arg_value

        def IsPlayingMusic(self):
            return self._m_isMusic

        def SendLocalEvent(self, ch):
            szCommand = str(['\0' for _ in range(256)])

            if self._m_isDark:
                ch.ChatPacket(EChatType.CHAT_TYPE_COMMAND, "DayMode dark")
            if self._m_isSnow:
                ch.ChatPacket(EChatType.CHAT_TYPE_COMMAND, "xmas_snow 1")
            if self._m_isMusic:
                temp_ref_szCommand = RefObject(szCommand);
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                ch.ChatPacket(EChatType.CHAT_TYPE_COMMAND, self._BuildCommandPlayMusic(temp_ref_szCommand, sizeof(szCommand), 1, self._m_stMusicFileName))
                szCommand = temp_ref_szCommand.arg_value

        def ShoutInMap(self, type, msg):
            it = m_set_pkChr.begin()
            while it is not self._m_set_pkChr.end():
                ch = *it
                ch.ChatPacket(EChatType.CHAT_TYPE_COMMAND, msg)
                it += 1

# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#        _BuildCommandPlayMusic(szCommand, nCmdLen, bSet, c_szMusicFileName)


    class WeddingManager(singleton):
        def __init__(self):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self._m_mapWedding = {}


        def close(self):
            pass

        def IsWeddingMap(self, dwMapIndex):
            return (dwMapIndex == WEDDING_MAP_INDEX or math.trunc(dwMapIndex / float(10000)) == WEDDING_MAP_INDEX)

        def Request(self, dwPID1, dwPID2):
            if map_allow_find(WEDDING_MAP_INDEX):
                dwMapIndex = self._CreateWeddingMap(dwPID1, dwPID2)

                if dwMapIndex == 0:
                    #lani_err("cannot create wedding map for %u, %u", dwPID1, dwPID2)
                    return

                p = TPacketWeddingReady()
                p.dwPID1 = dwPID1
                p.dwPID2 = dwPID2
                p.dwMapIndex = dwMapIndex

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                db_clientdesc.DBPacket(Globals.LG_HEADER_GD_WEDDING_READY, 0, p, sizeof(p))

        def End(self, dwMapIndex):
            it = self._m_mapWedding.find(dwMapIndex)

            if it is self._m_mapWedding.end():
                return LGEMiscellaneous.DEFINECONSTANTS.false

            it.second.SetEnded()
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

        def DestroyWeddingMap(self, pMap):
            #sys_log(0, "DestroyWeddingMap(index=%u)", pMap.GetMapIndex())
            pMap.DestroyAll()
            self._m_mapWedding.pop(pMap.GetMapIndex())
            SECTREE_MANAGER.instance().DestroyPrivateMap(int(pMap.GetMapIndex()))
            LG_DEL_MEM(pMap)

        def Find(self, dwMapIndex):
            it = self._m_mapWedding.find(dwMapIndex)

            if it is self._m_mapWedding.end():
                return None

            return it.second

        def _CreateWeddingMap(self, dwPID1, dwPID2):
            rkSecTreeMgr = SECTREE_MANAGER.instance()

            dwMapIndex = uint(rkSecTreeMgr.CreatePrivateMap(WEDDING_MAP_INDEX))

            if dwMapIndex == 0:
                #lani_err("CreateWeddingMap(pid1=%d, pid2=%d) / CreatePrivateMap(%d) FAILED", dwPID1, dwPID2, WEDDING_MAP_INDEX)
                return 0

            self._m_mapWedding.update({dwMapIndex: LG_NEW_M2 WeddingMap(dwMapIndex, dwPID1, dwPID2)})

            pkSectreeMap = rkSecTreeMgr.GetMap(int(dwMapIndex))
            if pkSectreeMap is None:
                return 0
            st_weddingMapRegenFileName = ""
            st_weddingMapRegenFileName.reserve(64)
            st_weddingMapRegenFileName = LocaleService_GetMapPath()
            st_weddingMapRegenFileName += "/Event/Hochzeit/npc.txt"

            if not regen_do(st_weddingMapRegenFileName, dwMapIndex, pkSectreeMap.m_setting.iBaseX, pkSectreeMap.m_setting.iBaseY, None, ((not LGEMiscellaneous.DEFINECONSTANTS.false))):
                #lani_err("CreateWeddingMap(pid1=%d, pid2=%d) / regen_do(fileName=%s, mapIndex=%d, basePos=(%d, %d)) FAILED", dwPID1, dwPID2, st_weddingMapRegenFileName, dwMapIndex, pkSectreeMap.m_setting.iBaseX, pkSectreeMap.m_setting.iBaseY)
            else:
                #sys_log(0, "CreateWeddingMap(pid1=%d, pid2=%d) / regen_do(fileName=%s, mapIndex=%d, basePos=(%d, %d)) ok", dwPID1, dwPID2, st_weddingMapRegenFileName, dwMapIndex, pkSectreeMap.m_setting.iBaseX, pkSectreeMap.m_setting.iBaseY)

            return dwMapIndex



class marriage: #this class replaces the original namespace 'marriage'

    class wedding_map_info(event_info_data):

        def __init__(self):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.pWeddingMap = None
            self.iStep = 0

            self.pWeddingMap = None
            self.iStep = 0

    @staticmethod
    def (UnnamedParameter):
        info = if isinstance(event.info, wedding_map_info) else None

        if info is None:
            #lani_err("wedding_end_event> <Factor> Null pointer")
            return 0

        pMap = info.pWeddingMap

        if info.iStep == 0:
            info.iStep += 1
            pMap.WarpAll()
            return ((15) * passes_per_sec)
        marriage.WeddingManager.instance().DestroyWeddingMap(pMap)
        return 0

    class FNotice:
        def __init__(self, psz):
            #instance fields found by # Laniatus Games Studio Inc. |:
            self.m_psz = '\0'

            self.m_psz = psz

        def functor_method(self, ch):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if __MULTI_LANGUAGE_SYSTEM__
            if ch is None:
                return

            bLocale = ch.GetDesc().GetLanguage() if ch.GetDesc() is not None else LaniatusLocalization.LOCALE_LANIATUS
            ch.ChatPacket(EChatType.CHAT_TYPE_NOTICE, LC_LOCALE_TEXT(self.m_psz, bLocale))
##else
            ch.ChatPacket(EChatType.CHAT_TYPE_NOTICE, "%s", self.m_psz)
##endif


    class FWarpEveryone:
        def functor_method(self, ch):
            if ch.IsPC():
                ch.ExitToSavedLocation()

    class FDestroyEveryone:
        def functor_method(self, ch):
            #sys_log(0, "WeddingMap::DestroyAll: %s", ch.GetName(LOCALE_LANIATUS))

            if ch.GetDesc():
                DESC_MANAGER.instance().DestroyDesc(ch.GetDesc(), ((not DefineConstants.false)))
            else:
                CHARACTER_MANAGER.instance().DestroyCharacter(ch)

    @staticmethod
    def __BuildCommandPlayMusic(szCommand, nCmdLen, bSet, c_szMusicFileName):
        if nCmdLen < 1:
            szCommand.arg_value[0] = '\0'
            return "PlayMusic 0 CommandLengthError"

        snprintf(szCommand.arg_value, nCmdLen, "PlayMusic %d %s", bSet, c_szMusicFileName)
        return szCommand.arg_value

