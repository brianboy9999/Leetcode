class Solution(object):
    def returnToBoundaryCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=0
        loc=0
        for i in range(0,len(nums)):
            loc+=nums[i]
            if loc==0:
                ans+=1
        return ans