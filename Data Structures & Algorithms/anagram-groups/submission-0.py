class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        seen = {}

        for i in strs:
            ana_bin = [0]*26

            for j in i:
                ana_bin[ord(j) - ord('a')] += 1

            k = tuple(ana_bin)

            if k in seen:
                seen[k].append(i)
            else:
                seen[k] = [i]

        return list(seen.values())