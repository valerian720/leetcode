# class Solution:
#     def runningSum(self, nums: List[int]) -> List[int]: 
#       ret = []
#       tmp = 0
#       for i in nums:
#         tmp += i
#         ret.append(tmp)
#       return ret

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]: 
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums