class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_arr = [0]*26
        t_arr = [0]*26
    
        for i in s:
            s_arr[ord(i)-ord('a')] += 1
        
        for j in t:
            t_arr[ord(j)-ord('a')] += 1
    
        return s_arr == t_arr
