class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        max_window = 0
        left = 0

        for right in range (n):
            while nums[left] * k < nums[right]:
                left += 1
            
            max_window = max(max_window, right - left + 1)
        return n - max_window 
       
