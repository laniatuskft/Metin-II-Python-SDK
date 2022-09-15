class MessengerManager(singleton):

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self._m_set_loginAccount = std::set()
        self._m_Relation = {}
        self._m_InverseRelation = {}
        self._m_set_requestToAdd = std::set()


    def close(self):
        pass

    def P2PLogin(self, account):
        self.Login(account)

    def P2PLogout(self, account):
        self.Logout(account)

    def Login(self, account):
        if self._m_set_loginAccount.find(account) != self._m_set_loginAccount.end():
            return

        DBManager.instance().FuncQuery(std::bind(self.LoadList, self, std::placeholders._1), "SELECT account, companion FROM messenger_list%s WHERE account='%s'", get_table_postfix(), account)

        self._m_set_loginAccount.insert(account)

    def Logout(self, account):
        if self._m_set_loginAccount.find(account) == self._m_set_loginAccount.end():
            return

        self._m_set_loginAccount.erase(account)

        it = m_InverseRelation[account].begin()
        while it is not self._m_InverseRelation[account].end():
            self._SendLogout(it, account)
            it += 1

        it2 = self._m_Relation.begin()

        while it2 is not self._m_Relation.end():
            it2.second.erase(account)
            it2 += 1

        self._m_Relation.pop(account)

    def RequestToAdd(self, ch, target):
        if (not ch.IsPC()) or not target.IsPC():
            return

        if quest.CQuestManager.instance().GetPCForce(ch.GetPlayerID()).IsRunning() == ((not LGEMiscellaneous.DEFINECONSTANTS.false)):
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("The recipient cannot receive friend invitation."))
            return

        if quest.CQuestManager.instance().GetPCForce(target.GetPlayerID()).IsRunning() == ((not LGEMiscellaneous.DEFINECONSTANTS.false)):
            return

        dw1 = GetCRC32(ch.GetName(LOCALE_LANIATUS), len(ch.GetName(LOCALE_LANIATUS)))
        dw2 = GetCRC32(target.GetName(LOCALE_LANIATUS), len(target.GetName(LOCALE_LANIATUS)))

        buf = str(['\0' for _ in range(64)])
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        snprintf(buf, sizeof(buf), "%u:%u", dw1, dw2)
        dwComplex = GetCRC32(buf, len(buf))

        self._m_set_requestToAdd.insert(dwComplex)

        target.ChatPacket(EChatType.CHAT_TYPE_COMMAND, "messenger_auth %s", ch.GetName(LOCALE_LANIATUS))

    def AuthToAdd(self, account, companion, bDeny):
        dw1 = GetCRC32(companion, len(companion))
        dw2 = GetCRC32(account, len(account))

        buf = str(['\0' for _ in range(64)])
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        snprintf(buf, sizeof(buf), "%u:%u", dw1, dw2)
        dwComplex = GetCRC32(buf, len(buf))

        if self._m_set_requestToAdd.find(dwComplex) == self._m_set_requestToAdd.end():
            #sys_log(0, "MessengerManager::AuthToAdd : request not exist %s -> %s", companion, account)
            return LGEMiscellaneous.DEFINECONSTANTS.false

        self._m_set_requestToAdd.erase(dwComplex)

        if not bDeny:
            self.AddToList(companion, account)
            self.AddToList(account, companion)

        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def __AddToList(self, account, companion):
        self._m_Relation[account].insert(companion)
        self._m_InverseRelation[companion].insert(account)

        ch = CHARACTER_MANAGER.instance().FindPC(account)
        d = ch.GetDesc() if ch is not None else None

        if d:
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Messenger> You added %s as a friend."), companion)

        tch = CHARACTER_MANAGER.instance().FindPC(companion)

        if tch:
            self._SendLogin(account, companion)
        else:
            self._SendLogout(account, companion)

    def AddToList(self, account, companion):
        if len(companion) == 0:
            return

        if self._m_Relation[account].find(companion) != self._m_Relation[account].end():
            return

        #sys_log(0, "Messenger Add %s %s", account, companion)
        DBManager.instance().Query("INSERT INTO messenger_list%s VALUES ('%s', '%s')", get_table_postfix(), account, companion)

        self.__AddToList(account, companion)

        p2ppck = SPacketGGMessenger()

        p2ppck.bHeader = byte(Globals.LG_HEADER_GG_MESSENGER_ADD)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        strncpy_s(p2ppck.szAccount, sizeof(p2ppck.szAccount), account, _TRUNCATE)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        strncpy_s(p2ppck.szCompanion, sizeof(p2ppck.szCompanion), companion, _TRUNCATE)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        P2P_MANAGER.instance().Send(p2ppck, sizeof(SPacketGGMessenger), NULL)

    def __RemoveFromList(self, account, companion):
        self._m_Relation[account].erase(companion)
        self._m_InverseRelation[companion].erase(account)
        self._m_Relation[companion].erase(account)
        self._m_InverseRelation[account].erase(companion)

        ch = CHARACTER_MANAGER.instance().FindPC(account)
        d = ch.GetDesc() if ch is not None else None

        if d:
            ch.ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<Messenger> You deleted %s off the list. "), companion)

        tch = CHARACTER_MANAGER.Instance().FindPC(companion)
        if tch is not None and tch.GetDesc() is not None:
            p = packet_messenger()
            p.header = byte(Globals.LG_HEADER_GC_MESSENGER)
            p.subheader = byte(Globals.MESSENGER_SUBLG_HEADER_GC_REMOVE_FRIEND)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            p.size = sizeof(packet_messenger) + sizeof(byte) + len(account)

            bLen = byte(len(account))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            tch.GetDesc().BufferedPacket(p, sizeof(p))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            tch.GetDesc().BufferedPacket(bLen, sizeof(byte))
            tch.GetDesc().Packet(account, len(account))

    def RemoveFromList(self, account, companion):
        if len(companion) == 0:
            return

        DBManager.instance().Query("DELETE FROM messenger_list%s WHERE (account='%s' AND companion = '%s') OR (account = '%s' AND companion = '%s')", get_table_postfix(), account, companion, companion, account)

        self.__RemoveFromList(account, companion)

        #sys_log(1, "Messenger Remove %s %s", account, companion)

        pack = SPacketGGMessenger()
        pack.bHeader = byte(Globals.LG_HEADER_GG_MESSENGER_REMOVE)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        strncpy_s(pack.szAccount, sizeof(pack.szAccount), account, _TRUNCATE)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        strncpy_s(pack.szCompanion, sizeof(pack.szCompanion), companion, _TRUNCATE)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        P2P_MANAGER.instance().Send(pack, sizeof(SPacketGGMessenger), NULL)

# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    RemoveAllList(account)
    def Initialize(self):
        pass

    def _SendList(self, account):
        ch = CHARACTER_MANAGER.instance().FindPC(account)

        if ch is None:
            return

        d = ch.GetDesc()

        if d is None:
            return

        if account not in self._m_Relation.keys():
            return

        if self._m_Relation[account].empty():
            return

        pack = packet_messenger()

        pack.header = byte(Globals.LG_HEADER_GC_MESSENGER)
        pack.subheader = byte(Globals.MESSENGER_SUBLG_HEADER_GC_LIST)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        pack.size = sizeof(packet_messenger)

        pack_offline = packet_messenger_list_offline()
        pack_online = packet_messenger_list_online()

        buf = TEMP_BUFFER(128 * 1024, DefineConstants.false)

        it = self._m_Relation[account].begin()
        eit = self._m_Relation[account].end()

        while it is not eit:
            if self._m_set_loginAccount.find(*it) != self._m_set_loginAccount.end():
                pack_online.connected = 1
                pack_online.length = it.size()

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                buf.write(pack_online, sizeof(packet_messenger_list_online))
                buf.write(it.c_str(), it.size())
            else:
                pack_offline.connected = 0
                pack_offline.length = it.size()

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
                buf.write(pack_offline, sizeof(packet_messenger_list_offline))
                buf.write(it.c_str(), it.size())

            it += 1

        pack.size += ushort(buf.size())

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        d.BufferedPacket(pack, sizeof(packet_messenger))
        d.Packet(buf.read_peek(), buf.size())

    def _SendLogin(self, account, companion):
        ch = CHARACTER_MANAGER.instance().FindPC(account)
        d = ch.GetDesc() if ch is not None else None

        if d is None:
            return

        if d.GetCharacter() is None:
            return

        if ch.GetGMLevel() == EGMLevels.GM_PLAYER and gm_get_level(companion) != EGMLevels.GM_PLAYER:
            return

        bLen = byte(len(companion))

        pack = packet_messenger()

        pack.header = byte(Globals.LG_HEADER_GC_MESSENGER)
        pack.subheader = byte(Globals.MESSENGER_SUBLG_HEADER_GC_LOGIN)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        pack.size = sizeof(packet_messenger) + sizeof(byte) + bLen

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        d.BufferedPacket(pack, sizeof(packet_messenger))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        d.BufferedPacket(bLen, sizeof(byte))
        d.Packet(companion, len(companion))

    def _SendLogout(self, account, companion):
        if len(companion) == 0:
            return

        ch = CHARACTER_MANAGER.instance().FindPC(account)
        d = ch.GetDesc() if ch is not None else None

        if d is None:
            return

        bLen = byte(len(companion))

        pack = packet_messenger()

        pack.header = byte(Globals.LG_HEADER_GC_MESSENGER)
        pack.subheader = byte(Globals.MESSENGER_SUBLG_HEADER_GC_LOGOUT)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        pack.size = sizeof(packet_messenger) + sizeof(byte) + bLen

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        d.BufferedPacket(pack, sizeof(packet_messenger))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        d.BufferedPacket(bLen, sizeof(byte))
        d.Packet(companion, len(companion))

    def _LoadList(self, msg):
        if None is msg:
            return

        if None is msg.Get():
            return

        if msg.Get().uiNumRows == 0:
            return

        account = ""

        #sys_log(1, "Messenger::LoadList")

        i = 0
        while i < msg.Get().uiNumRows:
            row = mysql_fetch_row(msg.Get().pSQLResult)

            if row[0] and row[1]:
                if len(account) == 0:
                    account = row[0]

                self._m_Relation[row[0]].insert(row[1])
                self._m_InverseRelation[row[1]].insert(row[0])
            i += 1

        self._SendList(account)

        it = m_InverseRelation[account].begin()
        while it is not self._m_InverseRelation[account].end():
            self._SendLogin(it, account)
            it += 1

    def _Destroy(self):
        pass


def RemoveAllList(account):
    company = std::set(m_Relation[account])
    DBManager.instance().Query("DELETE FROM messenger_list%s WHERE account='%s' OR companion='%s'", get_table_postfix(), account.c_str(), account.c_str())

    iter = company.begin()
    while iter is not company.end():
        self.RemoveFromList(account, *iter)
        iter += 1

    iter = company.begin()
    while iter is not company.end():
## Laniatus Games Studio Inc. | WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL METINII C CODE: company.erase(iter++);
        company.erase(iter)
        iter += 1

    company.clear()

