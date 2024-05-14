class Solution(object):
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """
        game=0
        while n>1:
            if n%2==0:
                game+=n/2
                n/=2
            else:
                game+=(n-1)/2
                n=(n-1)/2+1
        return game