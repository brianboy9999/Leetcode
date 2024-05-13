class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[]
        for i in range(0,len(nums)):
            for X in str(nums[i]):
                ans.append(int(X))
        return ans