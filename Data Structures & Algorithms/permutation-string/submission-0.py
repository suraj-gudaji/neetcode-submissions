class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1_freq = {}
        w_freq = {}

        c = len(s1)
         
        if len(s1) > len(s2):
            return False

        for i in range(c):
            s1_freq[s1[i]] = s1_freq.get(s1[i], 0) + 1
            w_freq[s2[i]] = w_freq.get(s2[i], 0) + 1

        if s1_freq == w_freq:
            return True

        for right in range(c, len(s2)):
            w_freq[s2[right]] = w_freq.get(s2[right], 0) + 1
            w_freq[s2[right-c]] -= 1

            if w_freq[s2[right-c]] == 0:
                del w_freq[s2[right-c]]

            if w_freq == s1_freq:
                return True

        return False 


