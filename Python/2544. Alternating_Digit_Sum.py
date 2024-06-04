class Solution(object):
    def alternateDigitSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans=0
        n=str(n)
        for i in range(0,len(n)):
            if i%2==0:
                ans+=int(n[i])
            if i%2!=0:
                ans-=int(n[i])
        return ans