class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numset=set(nums)
        ans=-1
        for nums in nums:
            if -nums in numset:
                ans=max(abs(nums),ans)
        return ans        