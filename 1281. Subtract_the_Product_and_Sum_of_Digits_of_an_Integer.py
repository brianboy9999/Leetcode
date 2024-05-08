class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        n=str(n)
        plus=0
        mult=1
        for i in range(0,len(n)):
            plus+=int(n[i])
            mult*=int(n[i])
        return mult-plus