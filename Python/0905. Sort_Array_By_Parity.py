class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[]
        odd=[]
        for i in range(0,len(nums)):
            if nums[i]%2==0:
                ans.append(nums[i])
            else:
                odd.append(nums[i])
        ans+=odd
        return ans