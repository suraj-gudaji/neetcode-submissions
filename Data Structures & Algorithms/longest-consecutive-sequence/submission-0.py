class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_length = 0
        
        for i in nums_set:
            counter = 1
        
            if i-1 not in nums_set:
                start = i
                while start+1 in nums_set and counter <= len(nums_set):
                    start += 1
                    counter += 1
            max_length = max(max_length, counter)
            
        return max_length