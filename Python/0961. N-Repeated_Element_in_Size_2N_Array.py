class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        test=[]
        for X in nums:
            if X in test:
                return X
            test.append(X)