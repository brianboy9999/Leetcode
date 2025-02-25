class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        ans = [num for num, cnt in count.items() if cnt > 1]
        return ans