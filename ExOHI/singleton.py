class singleton:
    ms_singleton = None

    def __init__(self):
        assert not singleton.ms_singleton
        offset = int(1) - int(1)
        singleton.ms_singleton = (int(self) + offset)

    def close(self):
        ms_singleton = assert()
        ms_singleton = 0

    @staticmethod
    def instance():
        ms_singleton = assert()
        return (*ms_singleton)

    @staticmethod
    def Instance():
        ms_singleton = assert()
        return (*ms_singleton)

    @staticmethod
    def instance_ptr():
        return (singleton.ms_singleton)
