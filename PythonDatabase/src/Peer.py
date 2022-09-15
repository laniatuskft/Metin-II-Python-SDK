from enum import Enum

#Laniatus Games Studio Inc. | Python Metin II Server Warnings Statement interrupted by a preprocessor statement:
#The original statement from the file sal.h starts with:
#    __inner_fallthrough_dec
#Preprocessor-interrupted statements cannot be handled by this converter.
#The remainder of the header file sal.h is ignored.

class CPeer(CPeerBase):
    #Laniatus Games Studio Inc. | Python Metin II Server Note This was formerly a static local variable declaration (not allowed in Python):

    def OnAccept(self):
        m_state = STATE_PLAYING

        #Laniatus Games Studio Inc. | Python Metin II Server Note This static local variable declaration (not allowed in Python) has been moved just prior to the method:
        #        static uint current_handle = 0
        OnAccept_current_handle += 1
#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: m_dwHandle = ++current_handle;
        m_dwHandle = OnAccept_current_handle

        sys_log(0, "Connection accepted. (host: %s handle: %u fd: %d)", m_host, m_dwHandle, m_fd)

    def OnClose(self):
        m_state = STATE_CLOSE

        sys_log(0, "Connection closed. (host: %s)", m_host)
        sys_log(0, "ItemIDRange: returned. %u ~ %u", m_itemRange.dwMin, m_itemRange.dwMax)

        CItemIDRangeManager.instance().UpdateRange(m_itemRange.dwMin, m_itemRange.dwMax)

        m_itemRange.dwMin = 0
        m_itemRange.dwMax = 0
        m_itemRange.dwUsableItemIDMin = 0

    def OnConnect(self):
        sys_log(0, "Connection established. (host: %s handle: %u fd: %d)", m_host, m_dwHandle, m_fd)
        m_state = STATE_PLAYING

# Laniatus Games Studio Inc. |  TODO TASK: There is no preprocessor in Python:
##pragma pack(1)
    class _header:
# Laniatus Games Studio Inc. |  TODO TASK: There is no preprocessor in Python:
##pragma pack()
    class EState(Enum):
        STATE_CLOSE = 0
        STATE_PLAYING = 1

    def __init__(self):
        m_state = 0
        m_bChannel = 0
        m_dwHandle = 0
        m_dwUserCount = 0
        m_wListenPort = 0
        m_wP2PPort = 0

# Laniatus Games Studio Inc. |  TODO TASK: The memory management function 'memset' has no equivalent in Python:
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        memset(m_alMaps, 0, sizeof(m_alMaps))

        m_itemRange.dwMin = m_itemRange.dwMax = m_itemRange.dwUsableItemIDMin = 0
        m_itemSpareRange.dwMin = m_itemSpareRange.dwMax = m_itemSpareRange.dwUsableItemIDMin = 0

    def close(self):
        Close()

    def EncodeHeader(self, header, dwHandle, dwSize):
        h = HEADER()

        sys_log(1, "EncodeHeader %u handle %u size %u", header, dwHandle, dwSize)

        h.bHeader = header
        h.dwHandle = dwHandle
        h.dwSize = dwSize

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        Encode(h, sizeof(HEADER))

    def PeekPacket(self, iBytesProceed, header, dwHandle, dwLength, data):
        if GetRecvLength() < iBytesProceed.arg_value + 9:
            return DefineConstants.false

# Laniatus Games Studio Inc. |  TODO TASK: Pointer arithmetic is detected on this variable:
#ORIGINAL LINE: const char * buf = (const char *) GetRecvBuffer();
        buf = str(GetRecvBuffer())
        buf += iBytesProceed.arg_value

#Laniatus Games Studio Inc. | Python Metin II Server Warnings An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: header = *(buf++);
        header.arg_value = *(buf)
        buf += 1

        dwHandle.arg_value = buf
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        buf += sizeof(uint)

        dwLength.arg_value = buf
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        buf += sizeof(uint)

        if iBytesProceed.arg_value + dwLength.arg_value + 9 > GetRecvLength():
            sys_log(0, "PeekPacket: not enough buffer size: len %u, recv %d", 9+dwLength.arg_value, GetRecvLength()-iBytesProceed.arg_value)
            return DefineConstants.false

        data[0] = buf
        iBytesProceed.arg_value += int(dwLength.arg_value + 9)
        return ((not DefineConstants.false))

    def EncodeReturn(self, header, dwHandle):
        EncodeHeader(header, dwHandle, 0)

    def Send(self):
        if m_state == STATE_CLOSE:
            return -1

        return (CPeerBase.Send())

    def GetHandle(self):
        return m_dwHandle

    def GetUserCount(self):
        return m_dwUserCount

    def SetUserCount(self, dwCount):
        m_dwUserCount = dwCount

    def SetPublicIP(self, ip):
        m_stPublicIP = ip
    def GetPublicIP(self):
        return m_stPublicIP.c_str()
    def SetChannel(self, bChannel):
        m_bChannel = bChannel
    def GetChannel(self):
        return m_bChannel
    def SetListenPort(self, wPort):
        m_wListenPort = wPort
    def GetListenPort(self):
        return m_wListenPort
    def SetP2PPort(self, wPort):
        m_wP2PPort = wPort

    def GetP2PPort(self):
        return m_wP2PPort
    def SetMaps(self, pl):
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        thecore_memcpy(m_alMaps, pl.arg_value, sizeof(m_alMaps))

#Laniatus Games Studio Inc. | Python Metin II Server Warnings Python has no equivalent to methods returning pointers to value types:
#ORIGINAL LINE: int * GetMaps()
    def GetMaps(self):
        return m_alMaps[0]
    def SetItemIDRange(self, itemRange):
        if itemRange.dwMin == 0 or itemRange.dwMax == 0 or itemRange.dwUsableItemIDMin == 0:
            return DefineConstants.false

        m_itemRange = itemRange
        sys_log(0, "ItemIDRange: SET %s %u ~ %u start: %u", GetPublicIP(), m_itemRange.dwMin, m_itemRange.dwMax, m_itemRange.dwUsableItemIDMin)

        return ((not DefineConstants.false))

    def SetSpareItemIDRange(self, itemRange):
        if itemRange.dwMin == 0 or itemRange.dwMax == 0 or itemRange.dwUsableItemIDMin == 0:
            return DefineConstants.false

        m_itemSpareRange = itemRange
        sys_log(0, "ItemIDRange: SPARE SET %s %u ~ %u start: %u", GetPublicIP(), m_itemSpareRange.dwMin, m_itemSpareRange.dwMax, m_itemSpareRange.dwUsableItemIDMin)

        return ((not DefineConstants.false))

    def CheckItemIDRangeCollision(self, itemRange):
        if m_itemRange.dwMin < itemRange.dwMax and m_itemRange.dwMax > itemRange.dwMin:
            sys_err("ItemIDRange: Collision!! this %u ~ %u check %u ~ %u", m_itemRange.dwMin, m_itemRange.dwMax, itemRange.dwMin, itemRange.dwMax)
            return DefineConstants.false

        if m_itemSpareRange.dwMin < itemRange.dwMax and m_itemSpareRange.dwMax > itemRange.dwMin:
            sys_err("ItemIDRange: Collision with spare range this %u ~ %u check %u ~ %u", m_itemSpareRange.dwMin, m_itemSpareRange.dwMax, itemRange.dwMin, itemRange.dwMax)
            return DefineConstants.false

        return ((not DefineConstants.false))

    def SendSpareItemIDRange(self):
        if m_itemSpareRange.dwMin == 0 or m_itemSpareRange.dwMax == 0 or m_itemSpareRange.dwUsableItemIDMin == 0:
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
            EncodeHeader(LG_HEADER_DG_ACK_SPARE_ITEM_ID_RANGE, 0, sizeof(TItemIDRangeTable))
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
            Encode(m_itemSpareRange, sizeof(TItemIDRangeTable))
        else:
            SetItemIDRange(m_itemSpareRange)

            if SetSpareItemIDRange(CItemIDRangeManager.instance().GetRange()) == DefineConstants.false:
                sys_log(0, "ItemIDRange: spare range set error")
                m_itemSpareRange.dwMin = m_itemSpareRange.dwMax = m_itemSpareRange.dwUsableItemIDMin = 0

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
            EncodeHeader(LG_HEADER_DG_ACK_SPARE_ITEM_ID_RANGE, 0, sizeof(TItemIDRangeTable))
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
            Encode(m_itemSpareRange, sizeof(TItemIDRangeTable))





