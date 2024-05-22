class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        i=0
        ans=0
        while n>=7:
            ans+=(1+7)*7/2+i*7
            i+=1
            n-=7
        if n>0:
            ans+=(1+n)*n/2+i*n
        return ans