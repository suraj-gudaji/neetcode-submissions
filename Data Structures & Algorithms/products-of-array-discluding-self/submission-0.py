class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]*len(nums)
        prefix = 1
        suffix = 1
        n = len(nums)

        for i in range(n):
            result[i] = prefix*result[i]
            prefix = prefix*nums[i]
             
        for i in range(n-1, -1, -1):
            result[i] = result[i]*suffix
            suffix = suffix*nums[i]

        return result

