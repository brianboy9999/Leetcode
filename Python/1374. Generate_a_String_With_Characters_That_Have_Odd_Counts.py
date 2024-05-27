class Solution(object):
    def generateTheString(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n%2==0:
            return "a"+"b"*(n-1)
        else:
            return "a"*n