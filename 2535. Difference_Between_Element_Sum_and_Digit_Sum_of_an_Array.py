class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        element=0
        digit=0
        for X in nums:
            element+=int(X)
            for Y in str(X):
                digit+=int(Y)
        return element-digit