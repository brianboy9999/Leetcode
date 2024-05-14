class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        X=sorted([point[0] for point in points])
        ans=0
        for i in range(0,len(X)-1):
            if X[i+1]-X[i]>ans:
                ans=X[i+1]-X[i]
        return ans