class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return [sum(True for X in nums1 if X in nums2),sum(True for X in nums2 if X in nums1)]