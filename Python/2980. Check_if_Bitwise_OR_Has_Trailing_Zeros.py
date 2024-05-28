class Solution(object):
    def hasTrailingZeros(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        test=0
        for X in nums:
            test+=X%2
        return len(nums)-test>1