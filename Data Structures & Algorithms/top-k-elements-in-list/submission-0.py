class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        buckets = []
        result = []

        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
    
        for _ in range(len(nums)+1):
            buckets.append([])
        
        for key, value in freq.items():
            buckets[value].append(key)
        
        for i in range(len(buckets)-1, -1, -1):
            for j in buckets[i]:
                if len(result) <= k:
                    result.append(j)
                if len(result) == k:
                    return result


    