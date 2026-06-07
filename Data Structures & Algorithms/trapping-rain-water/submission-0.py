class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max = [0]*n
        left_max_value = height[0]
        
        right_max = [0]*n
        right_max_value = height[n-1]
        right_max[n-1] = height[n-1]
        
        total = 0
        
        for i in range(1, n):
            left_max_value = max(height[i-1], left_max_value)
            left_max[i] = left_max_value
            
        for i in range(n-2, -1, -1):
            right_max_value = max(height[i+1], right_max_value)
            right_max[i] = right_max_value
            
        for i in range(n):
            s = min(left_max[i], right_max[i]) - height[i]
            
            if s > 0:
                total += s
                
        return total