class TEMP_BUFFER:
    def __init__(self, Size = 8192, bForceDelete = DefineConstants.false):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.buf = []
        self.forceDelete = False

        self.forceDelete = bForceDelete

        if self.forceDelete:
            Size = MAX(Size, 1024 * 128)

        self.buf = buffer_new(Size)

    def close(self):
        buffer_delete(self.buf)

    def read_peek(self):
        return (buffer_read_peek(self.buf))

    def write(self, data, size):
        buffer_write(self.buf, data, size)

    def size(self):
        return buffer_size(self.buf)

    def reset(self):
        buffer_reset(self.buf)

    def getptr(self):
        return self.buf


