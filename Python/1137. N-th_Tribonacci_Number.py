class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        X=0
        Y=1
        Z=1
        ans=0
        if n==0:
            return X
        elif n==1:
            return Y
        elif n==2:
            return Z
        else:
            for i in range(3,n+1):
                ans=X+Y+Z
                X=Y
                Y=Z
                Z=ans
            return ans