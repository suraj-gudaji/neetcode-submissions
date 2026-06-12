class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        state = defaultdict(int)
        result = 0

        for right in range(0, len(s)):

            state[s[right]] += 1

            while state[s[right]] > 1:
                state[s[left]] -= 1
                left += 1

            result = max(result, right-left+1)

        return result
