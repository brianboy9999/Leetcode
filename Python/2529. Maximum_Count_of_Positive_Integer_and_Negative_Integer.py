class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return max(len([1 for num in nums if num>0]),len([1 for num in nums if num<0]))