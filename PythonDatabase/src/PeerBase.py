#Laniatus Games Studio Inc. | Python Metin II Server Warnings Statement interrupted by a preprocessor statement:
#The original statement from the file sal.h starts with:
#    __inner_fallthrough_dec
#Preprocessor-interrupted statements cannot be handled by this converter.
#The remainder of the header file sal.h is ignored.

class CPeerBase(CNetBase):
    LG_MAX_HOST_LENGTH = 30
    MAX_INPUT_LEN = 1024 * 1024 * 2
    DEFAULT_PACKET_BUFFER_SIZE = 1024 * 1024 * 2

    def OnAccept(self):
        pass
    def OnConnect(self):
        pass
    def OnClose(self):
        pass

    def Accept(self, fd_accept):
        peer = sockaddr_in_IPV6INCOMPATIBLE()

# Laniatus Games Studio Inc. |  TODO TASK: The following assignments within expression was not converted by Laniatus Games Studio Inc. T.F |:
#ORIGINAL LINE: if ((m_fd = socket_accept(fd_accept, &peer)) == (UINT_PTR)(~0))
        if (m_fd = socket_accept(fd_accept, peer)) == (~0):
            Destroy()
            return DefineConstants.false

        socket_sndbuf(m_fd, 233016)
        socket_rcvbuf(m_fd, 233016)

# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        strlcpy(m_host, inet_ntoa_IPV6INCOMPATIBLE, sizeof(m_host))
        m_outBuffer = buffer_new(DEFAULT_PACKET_BUFFER_SIZE)
        m_inBuffer = buffer_new(MAX_INPUT_LEN)

        if (not m_outBuffer) or not m_inBuffer:
            Destroy()
            return DefineConstants.false

        fdwatch_add_fd(m_fdWatcher, m_fd, self, FDW_READ, DefineConstants.false)

        OnAccept()
        sys_log(0, "ACCEPT FROM %s", inet_ntoa_IPV6INCOMPATIBLE)
        return ((not DefineConstants.false))

    def Connect(self, host, port):
# Laniatus Games Studio Inc. |  TODO TASK: There is no Python equivalent to 'sizeof':
        strlcpy(m_host, host, sizeof(m_host))

# Laniatus Games Studio Inc. |  TODO TASK: The following assignments within expression was not converted by Laniatus Games Studio Inc. T.F |:
#ORIGINAL LINE: if ((m_fd = socket_connect(host, port)) == (UINT_PTR)(~0))
        if (m_fd = socket_connect(host, port)) == (~0):
            return DefineConstants.false

        m_outBuffer = buffer_new(DEFAULT_PACKET_BUFFER_SIZE)

        if not m_outBuffer:
            Destroy()
            return DefineConstants.false

        fdwatch_add_fd(m_fdWatcher, m_fd, self, FDW_READ, DefineConstants.false)

        OnConnect()
        return ((not DefineConstants.false))

    def Close(self):
        OnClose()

    def __init__(self):
        self.m_fd = (~0)
        self.m_BytesRemain = 0
        self.m_outBuffer = None
        self.m_inBuffer = None

    def close(self):
        Destroy()

    def Disconnect(self):
        if m_fd != (~0):
            fdwatch_del_fd(m_fdWatcher, m_fd)

            socket_close(m_fd)
            m_fd = (~0)

    def Destroy(self):
        Disconnect()

        if m_outBuffer:
            buffer_delete(m_outBuffer)
            m_outBuffer = None

        if m_inBuffer:
            buffer_delete(m_inBuffer)
            m_inBuffer = None

    def GetFd(self):
        return m_fd
    def EncodeBYTE(self, b):
        if not m_outBuffer:
            sys_err("Not ready to write")
            return

        buffer_write(m_outBuffer, b, 1)
        fdwatch_add_fd(m_fdWatcher, m_fd, self, FDW_WRITE, ((not DefineConstants.false)))

    def EncodeWORD(self, w):
        if not m_outBuffer:
            sys_err("Not ready to write")
            return

        buffer_write(m_outBuffer, w, 2)
        fdwatch_add_fd(m_fdWatcher, m_fd, self, FDW_WRITE, ((not DefineConstants.false)))

    def EncodeDWORD(self, dw):
        if not m_outBuffer:
            sys_err("Not ready to write")
            return

        buffer_write(m_outBuffer, dw, 4)
        fdwatch_add_fd(m_fdWatcher, m_fd, self, FDW_WRITE, ((not DefineConstants.false)))

    def Encode(self, data, size):
        if not m_outBuffer:
            sys_err("Not ready to write")
            return

        buffer_write(m_outBuffer, data, size)
        fdwatch_add_fd(m_fdWatcher, m_fd, self, FDW_WRITE, ((not DefineConstants.false)))

    def Send(self):
        if buffer_size(m_outBuffer) <= 0:
            return 0

        iBufferLeft = fdwatch_get_buffer_size(m_fdWatcher, m_fd)
        iBytesToWrite = MIN(iBufferLeft, buffer_size(m_outBuffer))

        if iBytesToWrite == 0:
            return 0

        result = socket_write(m_fd, str(buffer_read_peek(m_outBuffer)), iBytesToWrite)

        if result == 0:
            buffer_read_proceed(m_outBuffer, iBytesToWrite)

            if buffer_size(m_outBuffer) != 0:
                fdwatch_add_fd(m_fdWatcher, m_fd, self, FDW_WRITE, ((not DefineConstants.false)))

        return (result)

    def Recv(self):
        if not m_inBuffer:
            sys_err("input buffer nil")
            return -1

        buffer_adjust_size(m_inBuffer, MAX_INPUT_LEN >> 2)
        bytes_to_read = buffer_has_space(m_inBuffer)
        bytes_read = socket_read(m_fd, str(buffer_write_peek(m_inBuffer)), bytes_to_read)

        if bytes_read < 0:
# Laniatus Games Studio Inc. |  TODO TASK: There is no preprocessor in Python:
##if ! _WIN32
            sys_err("socket_read failed %s", strerror(errno))
##endif
            return -1
        elif bytes_read == 0:
            return 0

        buffer_write_proceed(m_inBuffer, bytes_read)
        m_BytesRemain = buffer_size(m_inBuffer)
        return 1

    def RecvEnd(self, proceed_bytes):
        buffer_read_proceed(m_inBuffer, proceed_bytes)
        m_BytesRemain = buffer_size(m_inBuffer)

    def GetRecvLength(self):
        return m_BytesRemain

    def GetRecvBuffer(self):
        return buffer_read_peek(m_inBuffer)

    def GetSendLength(self):
        return buffer_size(m_outBuffer)

    def GetHost(self):
        return m_host


