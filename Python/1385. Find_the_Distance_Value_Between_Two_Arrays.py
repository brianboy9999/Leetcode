class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        ans=0
        for X in arr1:
            check=True
            for Y in arr2:
                if abs(X-Y)<=d:
                    check=False
            if check==True:
                ans+=1
        return ans