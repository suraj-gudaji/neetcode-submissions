class Solution:
    def maxArea(self, heights: List[int]) -> int:
         max_area = 0
         i = 0
         j = len(heights)-1

         while i < j:

            area = (j-i) * min(heights[i], heights[j])

            min_height = min(heights[i], heights[j])

            if min_height == heights[i]:
                i += 1
            else:
                j -= 1

            max_area = max(max_area, area)

         return max_area
