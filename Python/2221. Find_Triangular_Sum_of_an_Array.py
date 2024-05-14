class Solution(object):
    def triangularSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        while len(nums)!=1:
            for i in range(0,len(nums)-1):
                nums[i]=(nums[i]+nums[i+1])%10
            nums.pop()
        return nums[0]