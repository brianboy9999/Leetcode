class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(list(set(nums)))==len(nums):
            return False
        if len(nums)==1:
            return False
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    if(abs(i-j)<=k):
                        return True
        return False