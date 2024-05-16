class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        expected=sorted(heights)
        ans=0
        for i in range(0,len(heights)):
            if heights[i]!=expected[i]:
                ans+=1
        return ans