class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n%2!=0:
            return [X for X in range(-(n//2),(n//2)+1)]
        else:
            return [X for X in range(-1,-(n//2)-1,-1)]+[X for X in range(1,(n//2)+1)]