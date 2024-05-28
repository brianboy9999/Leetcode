class Solution(object):
    def smallestRangeI(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        M=max(nums)
        m=min(nums)
        if M-m<=k*2:
            return 0
        else:
            return M-m-k*2