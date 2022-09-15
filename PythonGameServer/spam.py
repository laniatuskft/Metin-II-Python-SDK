class SpamManager(singleton):

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self._m_vec_word = []

    def GetSpamScore(self, src, len, score):
        word = None
        score.arg_value = 0

        strOrig = src
        strOrig = strOrig[0:remove_if(strOrig.begin(), strOrig.end(), isspace)] + strOrig[remove_if(strOrig.begin(), strOrig.end(), isspace) + strOrig.end():]

        i = 0
        while i < len(self._m_vec_word):
            r = self._m_vec_word[i]

            if True == WildCaseCmp(r[0].c_str(), strOrig):
                word = r[0].c_str()
                score.arg_value += r[1]
            i += 1

        return word

    def Clear(self):
        self._m_vec_word.clear()

    def Insert(self, str, score = 10):
        self._m_vec_word.append((str, score))
        #sys_log(0, "SPAM: %2d %s", score, str)

