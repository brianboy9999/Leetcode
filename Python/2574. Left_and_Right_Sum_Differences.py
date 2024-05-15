class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        leftSum=[]
        rightSum=[]
        ans=[]
        for i in range(0,len(nums)):
            leftSum.append(sum(nums[0:i]))
            rightSum.append(sum(nums[len(nums)-i:len(nums)]))
        for i in range(0,len(nums)):
            ans.append(abs(leftSum[i]-rightSum[len(nums)-i-1]))
        return ans