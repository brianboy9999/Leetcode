class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        num1=0
        num2=0
        for X in range(n+1):
            if X%m!=0:
                num1+=X
            else:
                num2+=X
        return num1-num2