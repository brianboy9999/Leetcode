class Solution(object):
    def findNonMinOrMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=sorted(list(set(nums)))
        if len(nums)<3:
            return -1
        else:
            return sorted(list(set(nums)))[1]