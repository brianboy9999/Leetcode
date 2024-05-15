class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num=list(set(nums))
        for i in range(0,len(num)):
            if nums.count(num[i])==1:
                return num[i]