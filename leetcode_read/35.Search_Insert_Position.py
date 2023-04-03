class Solution(object):
    def searchInsert(self, nums, target):
        up = len(nums) - 1
        down = 0
        while down <= up:
            mid = (down + up) // 2
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                down = mid + 1
            else:
                up = mid - 1
        return down

        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """