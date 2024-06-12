class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        def fac(i):
            num=1
            while i>=1:
                num*=i
                i-=1
            return num
        return fac(m+n-2)/(fac(m-1)*fac(n-1))