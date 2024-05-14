class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        test=list(set(nums))
        if len(test)!=len(nums):
            return True
        else:
            return False