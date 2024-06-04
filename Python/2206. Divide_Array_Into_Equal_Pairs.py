class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums=sorted(nums)
        i=0
        while i+1<len(nums):
            if nums[i]!=nums[i+1]:
                return False
            i+=2
        return True