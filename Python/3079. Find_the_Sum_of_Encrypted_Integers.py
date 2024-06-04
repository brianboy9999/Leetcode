class Solution(object):
    def sumOfEncryptedInt(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=0
        for X in nums:
            ans+=int(max(str(X))*len(str(X)))
        return ans