class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        Fn=0
        FN=1
        ans=0
        if n==1:
            return FN
        else:
            m=1
            while m<n:
                ans=FN+Fn
                Fn=FN
                FN=ans
                m+=1
        return ans