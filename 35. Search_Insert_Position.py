class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        else:
            ans=0
            while nums[ans]<target:
                if ans>=len(nums)-1:
                    return ans+1
                    break
                ans+=1
            return ans