class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        nums=sorted(str(num))
        return int(nums[0]+nums[2])+int(nums[1]+nums[3])