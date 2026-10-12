class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water = 0 

        while left < right:
            curr_height = min(height[left], height[right])
            curr_width = right - left
            curr_area = curr_height * curr_width

            max_water = max(max_water, curr_area)

            if height[left] < height[right]:
                left += 1
            else: 
                right -= 1
        
        return max_water

        
