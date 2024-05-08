class Solution(object):
    def sumOfMultiples(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum=0
        for X in range(n+1):
            if X%3==0 or X%5==0 or X%7==0:
                sum+=X
        return sum