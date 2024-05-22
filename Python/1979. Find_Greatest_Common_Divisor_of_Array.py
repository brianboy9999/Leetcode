class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        M=max(nums)
        m=min(nums)
        for X in range(m,0,-1):
            if M%X==0 and m%X==0:
                return X