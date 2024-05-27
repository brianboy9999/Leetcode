class Solution(object):
    def minSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums=sorted(nums)
        ans=[]
        while sum(ans)<=sum(nums):
            ans.append(nums.pop())
        return ans