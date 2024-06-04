class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        i=0
        for X in arr:
            if arr.count(X)==1:
                i+=1
            if i==k:
                return X
        return ""