class Solution(object):
    def sumIndicesWithKSetBits(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans=0
        for i in range(0,len(nums)):
            if format(i,'b').count("1")==k:
                ans+=nums[i]
        return ans