class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[]
        for i in range(0,len(nums)-1,2):
            for j in range(1,nums[i]+1):
                ans.append(nums[i+1])
        return ans