class SPacketElement:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.iSize = 0
        self.stName = ""
        self.iCalled = 0
        self.dwLoad = 0
        self.bSequencePacket = False


class CPacketInfo:
    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.m_pPacketMap = {}
        self.m_pCurrentPacket = None
        self.m_dwStartTime = 0

        self.m_pCurrentPacket = None
        self.m_dwStartTime = 0

    def close(self):
        it = self.m_pPacketMap.begin()
        while it is not self.m_pPacketMap.end():
            LG_DEL_MEM(it.second)
            it += 1

    def Set(self, header, iSize, c_pszName, bSeq = LGEMiscellaneous.DefineConstants.false):
        if header in self.m_pPacketMap.keys():
            return

        element = LG_NEW_M2 SPacketElement

        element.iSize = iSize
        element.stName.assign(c_pszName)
        element.iCalled = 0
        element.dwLoad = 0

        element.bSequencePacket = bSeq

        if element.bSequencePacket:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
            element.iSize += sizeof(byte)

        self.m_pPacketMap.insert(dict.value_type(header, element))

    def Get(self, header, size, c_ppszName):
        it = self.m_pPacketMap.find(header)

        if it is self.m_pPacketMap.end():
            return LGEMiscellaneous.DEFINECONSTANTS.false

        size.arg_value = it.second.iSize
        c_ppszName[0] = it.second.stName.c_str()

        self.m_pCurrentPacket = it.second
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def Start(self):
        assert self.m_pCurrentPacket is not None
        self.m_dwStartTime = get_dword_time()

    def End(self):
        self.m_pCurrentPacket.iCalled += 1
        self.m_pCurrentPacket.dwLoad += get_dword_time() - self.m_dwStartTime

    def Log(self, c_pszFileName):
        fp = None

        fp = fopen(c_pszFileName, "w")

        if fp is None:
            return

        it = self.m_pPacketMap.begin()

        fprintf(fp, "Name             Called     Load       Ratio\n")

        while it is not self.m_pPacketMap.end():
            p = it.second
            it += 1

            fprintf(fp, "%-16s %-10d %-10u %.2f\n", p.stName, p.iCalled, p.dwLoad,float(p.dwLoad) / p.iCalled if p.iCalled != 0 else 0.0)

        fclose(fp)

    def IsSequence(self, header):
        pkElement = self._GetElement(header)
        return pkElement.bSequencePacket if pkElement is not None else LGEMiscellaneous.DEFINECONSTANTS.false

    def SetSequence(self, header, bSeq):
        pkElem = self._GetElement(header)

        if pkElem:
            if bSeq:
                if not pkElem.bSequencePacket:
                    pkElem.iSize += 1
            else:
                if pkElem.bSequencePacket:
                    pkElem.iSize -= 1

            pkElem.bSequencePacket = bSeq

    def _GetElement(self, header):
        it = self.m_pPacketMap.find(header)

        if it is self.m_pPacketMap.end():
            return None

        return it.second


class CPacketInfoCG(CPacketInfo):
    def __init__(self):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_TEXT, sizeof(command_text), "Text", LGEMiscellaneous.DEFINECONSTANTS.false)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_HANDSHAKE, sizeof(command_handshake), "Handshake", LGEMiscellaneous.DEFINECONSTANTS.false)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_TIME_SYNC, sizeof(command_handshake), "TimeSync", ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_MARK_LOGIN, sizeof(command_mark_login), "MarkLogin", LGEMiscellaneous.DEFINECONSTANTS.false)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_MARK_IDXLIST, sizeof(command_mark_idxlist), "MarkIdxList", LGEMiscellaneous.DEFINECONSTANTS.false)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_MARK_CRCLIST, sizeof(command_mark_crclist), "MarkCrcList", LGEMiscellaneous.DEFINECONSTANTS.false)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_MARK_UPLOAD, sizeof(command_mark_upload), "MarkUpload", LGEMiscellaneous.DEFINECONSTANTS.false)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if _IMPROVED_PACKET_ENCRYPTION_
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_KEY_AGREEMENT, sizeof(TPacketKeyAgreement), "KeyAgreement", LGEMiscellaneous.DEFINECONSTANTS.false)
##endif
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_GUILD_SYMBOL_UPLOAD, sizeof(command_symbol_upload), "SymbolUpload", LGEMiscellaneous.DEFINECONSTANTS.false)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_SYMBOL_CRC, sizeof(command_symbol_crc), "SymbolCRC", LGEMiscellaneous.DEFINECONSTANTS.false)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_LOGIN, sizeof(command_login), "Login", ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_LOGIN2, sizeof(command_login2), "Login2", ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_LOGIN3, sizeof(command_login3), "Login3", ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_ATTACK, sizeof(command_attack), "Attack", ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_CHAT, sizeof(command_chat), "Chat", ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_WHISPER, sizeof(command_whisper), "Whisper", ((not LGEMiscellaneous.DEFINECONSTANTS.false)))

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_CHARACTER_SELECT, sizeof(command_player_select), "Select", ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_CHARACTER_CREATE, sizeof(command_player_create), "Create", ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_CHARACTER_DELETE, sizeof(command_player_delete), "Delete", ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_ENTERGAME, sizeof(command_entergame), "EnterGame", ((not LGEMiscellaneous.DEFINECONSTANTS.false)))

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_ITEM_USE, sizeof(command_item_use), "ItemUse", ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_ITEM_DROP, sizeof(command_item_drop), "ItemDrop", ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_ITEM_DROP2, sizeof(command_item_drop2), "ItemDrop2", ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_ITEM_DESTROY, sizeof(command_item_destroy), "ItemDestroy", ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_ITEM_MOVE, sizeof(command_item_move), "ItemMove", ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_ITEM_PICKUP, sizeof(command_item_pickup), "ItemPickup", ((not LGEMiscellaneous.DEFINECONSTANTS.false)))

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_LG_QUICKSLOT_ADD, sizeof(command_LG_QUICKSLOT_add), "QuickslotAdd", ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_LG_QUICKSLOT_DEL, sizeof(command_LG_QUICKSLOT_del), "QuickslotDel", ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_LG_QUICKSLOT_SWAP, sizeof(command_LG_QUICKSLOT_swap), "QuickslotSwap", ((not LGEMiscellaneous.DEFINECONSTANTS.false)))

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_SHOP, sizeof(command_shop), "Shop", ((not LGEMiscellaneous.DEFINECONSTANTS.false)))

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_ON_CLICK, sizeof(command_on_click), "OnClick", ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_EXCHANGE, sizeof(command_exchange), "Exchange", ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_CHARACTER_POSITION, sizeof(command_position), "Position", ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_SCRIPT_ANSWER, sizeof(command_script_answer), "ScriptAnswer", ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_SCRIPT_BUTTON, sizeof(command_script_button), "ScriptButton", ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_QUEST_INPUT_STRING, sizeof(command_quest_input_string), "QuestInputString", ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_QUEST_CONFIRM, sizeof(command_quest_confirm), "QuestConfirm", ((not LGEMiscellaneous.DEFINECONSTANTS.false)))

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_MOVE, sizeof(command_move), "Move", ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_SYNC_POSITION, sizeof(command_sync_position), "SyncPosition", ((not LGEMiscellaneous.DEFINECONSTANTS.false)))

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_FLY_TARGETING, sizeof(command_fly_targeting), "FlyTarget", ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_ADD_FLY_TARGETING, sizeof(command_fly_targeting), "AddFlyTarget", ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_SHOOT, sizeof(packet_shoot), "Shoot", ((not LGEMiscellaneous.DEFINECONSTANTS.false)))

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_USE_SKILL, sizeof(command_use_skill), "UseSkill", ((not LGEMiscellaneous.DEFINECONSTANTS.false)))

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_ITEM_USE_TO_ITEM, sizeof(command_item_use_to_item), "UseItemToItem", ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_TARGET, sizeof(command_target), "Target", ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_WARP, sizeof(command_warp), "Warp", ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_MESSENGER, sizeof(command_messenger), "Messenger", ((not LGEMiscellaneous.DEFINECONSTANTS.false)))

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_PARTY_REMOVE, sizeof(command_party_remove), "PartyRemove", ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_PARTY_INVITE, sizeof(command_party_invite), "PartyInvite", ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_PARTY_INVITE_ANSWER, sizeof(command_party_invite_answer), "PartyInviteAnswer", ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_PARTY_SET_STATE, sizeof(command_party_set_state), "PartySetState", ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_PARTY_USE_SKILL, sizeof(command_party_use_skill), "PartyUseSkill", ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_PARTY_PARAMETER, sizeof(command_party_parameter), "PartyParam", ((not LGEMiscellaneous.DEFINECONSTANTS.false)))

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_EMPIRE, sizeof(command_empire), "Empire", ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_SAFEBOX_CHECKOUT, sizeof(command_safebox_checkout), "SafeboxCheckout", ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_SAFEBOX_CHECKIN, sizeof(command_safebox_checkin), "SafeboxCheckin", ((not LGEMiscellaneous.DEFINECONSTANTS.false)))

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_SAFEBOX_ITEM_MOVE, sizeof(command_item_move), "SafeboxItemMove", ((not LGEMiscellaneous.DEFINECONSTANTS.false)))

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_GUILD, sizeof(command_guild), "Guild", ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_ANSWER_MAKE_GUILD, sizeof(command_guild_answer_make_guild), "AnswerMakeGuild", ((not LGEMiscellaneous.DEFINECONSTANTS.false)))

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_FISHING, sizeof(command_fishing), "Fishing", ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_ITEM_GIVE, sizeof(command_give_item), "ItemGive", ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_HACK, sizeof(SPacketCGHack), "Hack", ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_MYSHOP, sizeof(SPacketCGMyShop), "MyShop", ((not LGEMiscellaneous.DEFINECONSTANTS.false)))

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_REFINE, sizeof(SPacketCGRefine), "Refine", ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_CHANGE_NAME, sizeof(SPacketCGChangeName), "ChangeName", ((not LGEMiscellaneous.DEFINECONSTANTS.false)))

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_CLIENT_VERSION, sizeof(command_client_version), "Version", ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_CLIENT_VERSION2, sizeof(command_client_version2), "Version", ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_PONG, sizeof(byte), "Pong", ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_MALL_CHECKOUT, sizeof(command_safebox_checkout), "MallCheckout", ((not LGEMiscellaneous.DEFINECONSTANTS.false)))

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_SCRIPT_SELECT_ITEM, sizeof(command_script_select_item), "ScriptSelectItem", ((not LGEMiscellaneous.DEFINECONSTANTS.false)))

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_DRAGON_SOUL_REFINE, sizeof(SPacketCGDragonSoulRefine), "DragonSoulRefine", LGEMiscellaneous.DEFINECONSTANTS.false)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_STATE_CHECKER, sizeof(byte), "ServerStateCheck", LGEMiscellaneous.DEFINECONSTANTS.false)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_ACCE, sizeof(command_acce), "Acce", ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if ENABLE_TARGET_INFO
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_TARGET_INFO_LOAD, sizeof(packet_target_info_load), "TargetInfoLoad", ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
##endif
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if __MULTI_LANGUAGE_SYSTEM__
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_CHANGE_LANGUAGE, sizeof(SPacketChangeLanguage), "ChangeLanguage", ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
##endif
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if __EXTENDED_WHISPER_DETAILS__
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_CG_WHISPER_DETAILS, sizeof(SPacketCGWhisperDetails), "WhisperDetails", ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
##endif

    def close(self):
        self.Log("packet_info.txt")

class CPacketInfoGG(CPacketInfo):
    def __init__(self):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_GG_SETUP, sizeof(SPacketGGSetup), "Setup", LGEMiscellaneous.DEFINECONSTANTS.false)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_GG_LOGIN, sizeof(SPacketGGLogin), "Login", LGEMiscellaneous.DEFINECONSTANTS.false)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_GG_LOGOUT, sizeof(SPacketGGLogout), "Logout", LGEMiscellaneous.DEFINECONSTANTS.false)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_GG_RELAY, sizeof(SPacketGGRelay), "Relay", LGEMiscellaneous.DEFINECONSTANTS.false)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_GG_NOTICE, sizeof(SPacketGGNotice), "Notice", LGEMiscellaneous.DEFINECONSTANTS.false)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_GG_SHUTDOWN, sizeof(SPacketGGShutdown), "Shutdown", LGEMiscellaneous.DEFINECONSTANTS.false)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_GG_GUILD, sizeof(SPacketGGGuild), "Guild", LGEMiscellaneous.DEFINECONSTANTS.false)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_GG_SHOUT, sizeof(SPacketGGShout), "Shout", LGEMiscellaneous.DEFINECONSTANTS.false)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_GG_DISCONNECT, sizeof(SPacketGGDisconnect), "Disconnect", LGEMiscellaneous.DEFINECONSTANTS.false)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_GG_MESSENGER_ADD, sizeof(SPacketGGMessenger), "MessengerAdd", LGEMiscellaneous.DEFINECONSTANTS.false)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_GG_MESSENGER_REMOVE, sizeof(SPacketGGMessenger), "MessengerRemove", LGEMiscellaneous.DEFINECONSTANTS.false)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_GG_FIND_POSITION, sizeof(SPacketGGFindPosition), "FindPosition", LGEMiscellaneous.DEFINECONSTANTS.false)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_GG_WARP_CHARACTER, sizeof(SPacketGGWarpCharacter), "WarpCharacter", LGEMiscellaneous.DEFINECONSTANTS.false)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_GG_GUILD_WAR_ZONE_MAP_INDEX, sizeof(SPacketGGGuildWarMapIndex), "GuildWarMapIndex", LGEMiscellaneous.DEFINECONSTANTS.false)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_GG_TRANSFER, sizeof(SPacketGGTransfer), "Transfer", LGEMiscellaneous.DEFINECONSTANTS.false)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_GG_XMAS_WARP_SANTA, sizeof(SPacketGGXmasWarpSanta), "XmasWarpSanta", LGEMiscellaneous.DEFINECONSTANTS.false)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_GG_XMAS_WARP_SANTA_REPLY, sizeof(SPacketGGXmasWarpSantaReply), "XmasWarpSantaReply", LGEMiscellaneous.DEFINECONSTANTS.false)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_GG_RELOAD_CRC_LIST, sizeof(byte), "ReloadCRCList", LGEMiscellaneous.DEFINECONSTANTS.false)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_GG_CHECK_CLIENT_VERSION, sizeof(byte), "CheckClientVersion", LGEMiscellaneous.DEFINECONSTANTS.false)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_GG_LOGIN_PING, sizeof(SPacketGGLoginPing), "LoginPing", LGEMiscellaneous.DEFINECONSTANTS.false)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_GG_BLOCK_CHAT, sizeof(SPacketGGBlockChat), "BlockChat", LGEMiscellaneous.DEFINECONSTANTS.false)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        self.Set(Globals.LG_HEADER_GG_CHECK_AWAKENESS, sizeof(SPacketGGCheckAwakeness), "CheckAwakeness", LGEMiscellaneous.DEFINECONSTANTS.false)

    def close(self):
        self.Log("p2p_packet_info.txt")

class CPacketInfoUDP(CPacketInfo):
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    CPacketInfoUDP()
# Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Missing function; 03-06-2021 The implementation method for the function has not been implemented yet. It belongs to TSX00389.
#    def close(self):
        pass

