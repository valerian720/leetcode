class Solution(object):
    def pivotIndex(self, nums):
        if nums is None: return -1
        left, mid, right = 0, 0, sum(nums)
        
        for i in range(len(nums)):
            left += mid
            mid = nums[i]
            right -= nums[i]
            if left == right:
                return i
        
        return -1