class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        sl = [0]*26
        tl = [0]*26

        for i in s:
            sl[ord(i)-ord('s')] += 1

        for i in t:
            tl[ord(i)-ord('s')] += 1

        if sl == tl:
            return True
        else:
            return False
