class Solution(object):
    def intersection(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        ex=set(nums[0])
        for i in range(1,len(nums)):
            ex=ex.intersection(set(nums[i]))
        return sorted(set(ex))