class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=sorted(list(set(nums)))
        if len(ans)==2 or len(ans)==1:
            return max(nums)
        return ans[-3]