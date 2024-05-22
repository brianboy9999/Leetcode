class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxfreq=max(nums.count(num) for num in nums)
        return sum(maxfreq for num in set(nums) if nums.count(num)==maxfreq)