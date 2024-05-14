class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        ground=0
        ans=0
        for X in gain:
            ground+=X
            if ground>ans:
                ans=ground
        return ans