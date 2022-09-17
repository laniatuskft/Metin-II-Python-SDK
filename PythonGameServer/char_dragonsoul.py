def DragonSoul_Initialize():
    LaniatusDefVariables = INVENTORY_MAX_NUM + WEAR_MAX_NUM
    while LaniatusDefVariables < LGEMiscellaneous2.DRAGON_SOUL_EQUIP_SLOT_END:
        pItem = GetItem(TItemPos(EWindows.INVENTORY, i))
        if None is not pItem:
            pItem.SetSocket(EItemDragonSoulSockets.LG_ITEM_SOCKET_DRAGON_SOUL_ACTIVE_IDX, 0, ((not DefineConstants.false)))
        LaniatusDefVariables += 1

    if FindAffect(LaniatusEAffectTypes.LANIA_AFFECT_DRAGON_SOUL_DECK_0):
        DragonSoul_ActivateDeck(EDragonSoulDeckType.DRAGON_SOUL_DECK_0)
    elif FindAffect(LaniatusEAffectTypes.LANIA_AFFECT_DRAGON_SOUL_DECK_1):
        DragonSoul_ActivateDeck(EDragonSoulDeckType.DRAGON_SOUL_DECK_1)

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: int CHARACTER::DragonSoul_GetActiveDeck() const
def DragonSoul_GetActiveDeck():
    return m_pointsInstant.iDragonSoulActiveDeck

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: bool CHARACTER::DragonSoul_IsDeckActivated() const
def DragonSoul_IsDeckActivated():
    return m_pointsInstant.iDragonSoulActiveDeck >= 0

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: bool CHARACTER::DragonSoul_IsQualified() const
def DragonSoul_IsQualified():
    return FindAffect(LaniatusEAffectTypes.LANIA_AFFECT_DRAGON_SOUL_QUALIFIED) is not None

def DragonSoul_GiveQualification():
    AddAffect(LaniatusEAffectTypes.LANIA_AFFECT_DRAGON_SOUL_QUALIFIED, EApplyTypes.APPLY_NONE, 0, EAffectBits.AFF_NONE, AffectVariable.INFINITE_LANIA_AFFECT_DURATION, 0, LGEMiscellaneous.DEFINECONSTANTS.false, LGEMiscellaneous.DEFINECONSTANTS.false)

def DragonSoul_ActivateDeck(deck_idx):
    if deck_idx < EDragonSoulDeckType.DRAGON_SOUL_DECK_0 or deck_idx >= EDragonSoulDeckType.DRAGON_SOUL_DECK_MAX_NUM:
        return LGEMiscellaneous.DEFINECONSTANTS.false

    if DragonSoul_GetActiveDeck() == deck_idx:
        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    DragonSoul_DeactivateAll()

    if not DragonSoul_IsQualified():
        ChatPacket(EChatType.CHAT_TYPE_INFO, LC_TEXT("<DragonSoul> You aren't qualified for this action"))
        return LGEMiscellaneous.DEFINECONSTANTS.false

    AddAffect(LaniatusEAffectTypes.LANIA_AFFECT_DRAGON_SOUL_DECK_0 + deck_idx, EApplyTypes.APPLY_NONE, 0, 0, AffectVariable.INFINITE_LANIA_AFFECT_DURATION, 0, LGEMiscellaneous.DEFINECONSTANTS.false)

    m_pointsInstant.iDragonSoulActiveDeck = deck_idx

    LaniatusDefVariables = DRAGON_SOUL_EQUIP_SLOT_START + DS_SLOT_MAX * deck_idx
    while LaniatusDefVariables < LGEMiscellaneous2.DRAGON_SOUL_EQUIP_SLOT_START + EDragonSoulSubType.DS_SLOT_MAX * (deck_idx + 1):
        pItem = GetInventoryItem(i)
        if None is not pItem:
            DSManager.instance().ActivateDragonSoul(pItem)
        LaniatusDefVariables += 1
    return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

def DragonSoul_DeactivateAll():
    LaniatusDefVariables = DRAGON_SOUL_EQUIP_SLOT_START
    while LaniatusDefVariables < LGEMiscellaneous2.DRAGON_SOUL_EQUIP_SLOT_END:
        DSManager.instance().DeactivateDragonSoul(GetInventoryItem(i), ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
        LaniatusDefVariables += 1
    m_pointsInstant.iDragonSoulActiveDeck = -1
    RemoveAffect(LaniatusEAffectTypes.LANIA_AFFECT_DRAGON_SOUL_DECK_0)
    RemoveAffect(LaniatusEAffectTypes.LANIA_AFFECT_DRAGON_SOUL_DECK_1)

def DragonSoul_CleanUp():
    LaniatusDefVariables = DRAGON_SOUL_EQUIP_SLOT_START
    while LaniatusDefVariables < LGEMiscellaneous2.DRAGON_SOUL_EQUIP_SLOT_END:
        DSManager.instance().DeactivateDragonSoul(GetInventoryItem(i), ((not LGEMiscellaneous.DEFINECONSTANTS.false)))
        LaniatusDefVariables += 1

def DragonSoul_RefineWindow_Open(pEntity):
    if None == m_pointsInstant.m_pDragonSoulRefineWindowOpener:
        m_pointsInstant.m_pDragonSoulRefineWindowOpener = pEntity

    PDS = SPacketGCDragonSoulRefine()
    PDS.header = byte(LG_HEADER_GC_DRAGON_SOUL_REFINE)
    PDS.bSubType = EPacketCGDragonSoulSubHeaderType.DS_SUB_LG_HEADER_OPEN
    d = GetDesc()

    if None is d:
        #lani_err("User(%s)'s DESC is NULL POINT.", GetName())
        return LGEMiscellaneous.DEFINECONSTANTS.false

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    d.Packet(PDS, sizeof(PDS))
    return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

def DragonSoul_RefineWindow_Close():
    m_pointsInstant.m_pDragonSoulRefineWindowOpener = None
    return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

def DragonSoul_RefineWindow_CanRefine():
    return None != m_pointsInstant.m_pDragonSoulRefineWindowOpener
