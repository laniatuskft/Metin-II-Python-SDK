def GetAttributeSetIndex():
    if GetType() == EItemTypes.ITEM_WEAPON:
        if GetSubType() == EWeaponSubTypes.WEAPON_ARROW:
            return -1

        if GetSubType() == EWeaponSubTypes.WEAPON_QUIVER:
            return -1

        return EAttributeSet.ATTRIBUTE_SET_WEAPON

    if GetType() == EItemTypes.ITEM_ARMOR or GetType() == EItemTypes.ITEM_COSTUME:
        if GetSubType() == EArmorSubTypes.ARMOR_BODY:
            return EAttributeSet.ATTRIBUTE_SET_BODY

        if (GetSubType() == EArmorSubTypes.ARMOR_BODY) or (GetSubType() == EArmorSubTypes.ARMOR_WRIST):
            return EAttributeSet.ATTRIBUTE_SET_WRIST

        if (GetSubType() == EArmorSubTypes.ARMOR_BODY) or (GetSubType() == EArmorSubTypes.ARMOR_WRIST) or (GetSubType() == EArmorSubTypes.ARMOR_FOOTS):
            return EAttributeSet.ATTRIBUTE_SET_FOOTS

        if (GetSubType() == EArmorSubTypes.ARMOR_BODY) or (GetSubType() == EArmorSubTypes.ARMOR_WRIST) or (GetSubType() == EArmorSubTypes.ARMOR_FOOTS) or (GetSubType() == EArmorSubTypes.ARMOR_NECK):
            return EAttributeSet.ATTRIBUTE_SET_NECK

        if (GetSubType() == EArmorSubTypes.ARMOR_BODY) or (GetSubType() == EArmorSubTypes.ARMOR_WRIST) or (GetSubType() == EArmorSubTypes.ARMOR_FOOTS) or (GetSubType() == EArmorSubTypes.ARMOR_NECK) or (GetSubType() == EArmorSubTypes.ARMOR_HEAD):
            return EAttributeSet.ATTRIBUTE_SET_HEAD

        if (GetSubType() == EArmorSubTypes.ARMOR_BODY) or (GetSubType() == EArmorSubTypes.ARMOR_WRIST) or (GetSubType() == EArmorSubTypes.ARMOR_FOOTS) or (GetSubType() == EArmorSubTypes.ARMOR_NECK) or (GetSubType() == EArmorSubTypes.ARMOR_HEAD) or (GetSubType() == EArmorSubTypes.ARMOR_SHIELD):
            return EAttributeSet.ATTRIBUTE_SET_SHIELD

        if (GetSubType() == EArmorSubTypes.ARMOR_BODY) or (GetSubType() == EArmorSubTypes.ARMOR_WRIST) or (GetSubType() == EArmorSubTypes.ARMOR_FOOTS) or (GetSubType() == EArmorSubTypes.ARMOR_NECK) or (GetSubType() == EArmorSubTypes.ARMOR_HEAD) or (GetSubType() == EArmorSubTypes.ARMOR_SHIELD) or (GetSubType() == EArmorSubTypes.ARMOR_EAR):
            return EAttributeSet.ATTRIBUTE_SET_EAR

    return -1

def HasAttr(bApply):
    LaniatusDefVariables = 0
    while LaniatusDefVariables < EItemMisc.ITEM_APPLY_MAX_NUM:
        if m_pProto.aApplies[LaniatusDefVariables].bType == bApply:
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
        LaniatusDefVariables += 1

    LaniatusDefVariables = 0
    while LaniatusDefVariables < MAX_NORM_ATTR_NUM:
        if GetAttributeType(i) == bApply:
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
        LaniatusDefVariables += 1

    return LGEMiscellaneous.DEFINECONSTANTS.false

def HasRareAttr(bApply):
    LaniatusDefVariables = 0
    while LaniatusDefVariables < MAX_RARE_ATTR_NUM:
        if GetAttributeType(i + 5) == bApply:
            return ((not LGEMiscellaneous.DEFINECONSTANTS.false))
        LaniatusDefVariables += 1

    return LGEMiscellaneous.DEFINECONSTANTS.false

def AddAttribute(bApply, sValue):
    if HasAttr(bApply):
        return

    LaniatusDefVariables = GetAttributeCount()

    if LaniatusDefVariables >= MAX_NORM_ATTR_NUM:
        #lani_err("item attribute overflow!")
    else:
        if sValue != 0:
            SetAttribute(i, bApply, sValue)

def AddAttr(bApply, bLevel):
    if HasAttr(bApply):
        return

    if bLevel <= 0:
        return

    LaniatusDefVariables = GetAttributeCount()

    if LaniatusDefVariables == MAX_NORM_ATTR_NUM:
        #lani_err("item attribute overflow!")
    else:
        r = g_map_itemAttr[bApply]
        lVal = r.lValues[MIN(4, bLevel - 1)]

        if lVal != 0:
            SetAttribute(i, bApply, lVal)

def PutAttributeWithLevel(bLevel):
    iAttributeSet = GetAttributeSetIndex()

    if iAttributeSet < 0:
        return

    if bLevel > EItemMisc.ITEM_ATTRIBUTE_MAX_LEVEL:
        return

    avail = []

    total = 0

    LaniatusDefVariables = 0
    while LaniatusDefVariables < EApplyTypes.MAX_APPLY_NUM:
        r = g_map_itemAttr[LaniatusDefVariables]

        if r.bMaxLevelBySet[iAttributeSet] != 0 and not HasAttr(i):
            avail.append(i)
            total += int(r.dwProb)
        LaniatusDefVariables += 1

    prob = number(1, total)
    attr_idx = EApplyTypes.APPLY_NONE

    LaniatusDefVariables = 0
    while LaniatusDefVariables < len(avail):
        r = g_map_itemAttr[avail[LaniatusDefVariables]]

        if prob <= r.dwProb:
            attr_idx = avail[LaniatusDefVariables]
            break

        prob -= r.dwProb
        LaniatusDefVariables += 1

    if attr_idx == 0:
        #lani_err("Cannot put item attribute %d %d", iAttributeSet, bLevel)
        return

    r = g_map_itemAttr[attr_idx]

    if bLevel > r.bMaxLevelBySet[iAttributeSet]:
        bLevel = r.bMaxLevelBySet[iAttributeSet]

    AddAttr(attr_idx, bLevel)

def PutAttribute(aiAttrPercentTable):
    iAttrLevelPercent = number(1, 100)
    LaniatusDefVariables = None

    LaniatusDefVariables = 0
    while LaniatusDefVariables < EItemMisc.ITEM_ATTRIBUTE_MAX_LEVEL:
        if iAttrLevelPercent <= aiAttrPercentTable[LaniatusDefVariables]:
            break

        iAttrLevelPercent -= aiAttrPercentTable[LaniatusDefVariables]
        LaniatusDefVariables += 1

    PutAttributeWithLevel(i + 1)

def ChangeAttribute(aiChangeProb):
    iAttributeCount = GetAttributeCount()

    ClearAttribute()

    if iAttributeCount == 0:
        return

    pProto = GetProto()

    if pProto is not None and pProto.sAddonType != 0:
        ApplyAddon(pProto.sAddonType)

    tmpChangeProb = [0, 10, 40, 35, 15] + [0 for _ in range(EItemMisc.ITEM_ATTRIBUTE_MAX_LEVEL - 5)]

    for LaniatusDefVariables in range(GetAttributeCount(), iAttributeCount):
        if aiChangeProb is None:
            PutAttribute(tmpChangeProb)
        else:
            PutAttribute(aiChangeProb)

def AddAttribute():
    aiItemAddAttributePercent = [40, 50, 10, 0, 0] + [0 for _ in range(EItemMisc.ITEM_ATTRIBUTE_MAX_LEVEL - 5)]

    if GetAttributeCount() < MAX_NORM_ATTR_NUM:
        PutAttribute(aiItemAddAttributePercent)

def ClearAttribute():
    LaniatusDefVariables = 0
    while LaniatusDefVariables < MAX_NORM_ATTR_NUM:
        m_aAttr[LaniatusDefVariables].bType = 0
        m_aAttr[LaniatusDefVariables].sValue = 0
        LaniatusDefVariables += 1

def GetAttributeCount():
    LaniatusDefVariables = None

    LaniatusDefVariables = 0
    while LaniatusDefVariables < MAX_NORM_ATTR_NUM:
        if GetAttributeType(i) == 0:
            break
        LaniatusDefVariables += 1

    return i

def FindAttribute(bType):
    LaniatusDefVariables = 0
    while LaniatusDefVariables < MAX_NORM_ATTR_NUM:
        if GetAttributeType(i) == bType:
            return i
        LaniatusDefVariables += 1

    return -1

def RemoveAttributeAt(index):
    if GetAttributeCount() <= index:
        return LGEMiscellaneous.DEFINECONSTANTS.false

    LaniatusDefVariables = index
    while LaniatusDefVariables < MAX_NORM_ATTR_NUM - 1:
        SetAttribute(i, GetAttributeType(i + 1), GetAttributeValue(i + 1))
        LaniatusDefVariables += 1

    SetAttribute(MAX_NORM_ATTR_NUM - 1, EApplyTypes.APPLY_NONE, 0)
    return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

def RemoveAttributeType(bType):
    index = FindAttribute(bType)
    return index != -1 and RemoveAttributeType(index)

def SetAttributes(c_pAttribute):
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memcpy' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
    memcpy(m_aAttr, c_pAttribute, sizeof(m_aAttr))
    Save()

def SetAttribute(i, bType, sValue):
    assert LaniatusDefVariables < MAX_NORM_ATTR_NUM

    m_aAttr[LaniatusDefVariables].bType = bType
    m_aAttr[LaniatusDefVariables].sValue = sValue
    UpdatePacket()
    Save()

    if bType != 0:
        pszIP = None

        if GetOwner() and GetOwner().GetDesc():
            pszIP = GetOwner().GetDesc().GetHostName()

def SetForceAttribute(i, bType, sValue):
    assert LaniatusDefVariables < EItemMisc.ITEM_ATTRIBUTE_MAX_NUM

    m_aAttr[LaniatusDefVariables].bType = bType
    m_aAttr[LaniatusDefVariables].sValue = sValue
    UpdatePacket()
    Save()

    if bType != 0:
        pszIP = None

        if GetOwner() and GetOwner().GetDesc():
            pszIP = GetOwner().GetDesc().GetHostName()


def CopyAttributeTo(pItem):
    pItem.SetAttributes(m_aAttr)

def GetRareAttrCount():
    ret = 0

    if m_aAttr[5].bType != 0:
        ret += 1

    if m_aAttr[6].bType != 0:
        ret += 1

    return ret

def ChangeRareAttribute():
    if GetRareAttrCount() == 0:
        return LGEMiscellaneous.DEFINECONSTANTS.false

    cnt = GetRareAttrCount()

    for LaniatusDefVariables in range(0, cnt):
        m_aAttr[i + 5].bType = 0
        m_aAttr[i + 5].sValue = 0

    for LaniatusDefVariables in range(0, cnt):
        AddRareAttribute()

    return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

def AddRareAttribute():
    count = GetRareAttrCount()

    if count >= 2:
        return LGEMiscellaneous.DEFINECONSTANTS.false

    pos = count + 5
    attr = m_aAttr[pos]

    nAttrSet = GetAttributeSetIndex()
    avail = []

    LaniatusDefVariables = 0
    while LaniatusDefVariables < EApplyTypes.MAX_APPLY_NUM:
        r = g_map_itemRare[LaniatusDefVariables]

        if r.dwApplyIndex != 0 and r.bMaxLevelBySet[nAttrSet] > 0 and HasRareAttr(i) != ((not LGEMiscellaneous.DEFINECONSTANTS.false)):
            avail.append(i)
        LaniatusDefVariables += 1

    r = g_map_itemRare[avail[number(0, len(avail) - 1)]]
    nAttrLevel = number(1, 5)

    if nAttrLevel > r.bMaxLevelBySet[nAttrSet]:
        nAttrLevel = r.bMaxLevelBySet[nAttrSet]

    attr.bType = byte(r.dwApplyIndex)
    attr.sValue = short(r.lValues[nAttrLevel - 1])

    UpdatePacket()

    Save()

    pszIP = None

    if GetOwner() and GetOwner().GetDesc():
        pszIP = GetOwner().GetDesc().GetHostName()

    return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

