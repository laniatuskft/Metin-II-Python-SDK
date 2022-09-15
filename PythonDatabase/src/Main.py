import math

def main():
    WriteVersion()

    Config = CConfig()
    poller = CNetPoller()
    DBManager = CDBManager()
    ClientManager = CClientManager()
    GuildManager = CGuildManager()
    PrivManager = CPrivManager()
    ItemAwardManager = ItemAwardManager()
    MarriageManager = marriage.CManager()
    ItemIDRangeManager = CItemIDRangeManager()
    if not Start():
        return 1

    GuildManager.Initialize()
    MarriageManager.Initialize()
    ItemIDRangeManager.Build()
    sys_log(0, "Metin2DBCacheServer Start\n")

    CClientManager.instance().MainLoop()

    signal_timer_disable()

    DBManager.Quit()
    iCount = None

    while True:
        iCount = 0

        iCount += CDBManager.instance().CountReturnQuery(SQL_PLAYER)
        iCount += CDBManager.instance().CountAsyncQuery(SQL_PLAYER)

        if iCount == 0:
            break

        usleep(1000)
        sys_log(0, "WAITING_QUERY_COUNT %d", iCount)

    return 1