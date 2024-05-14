class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        n=format(n,'b')
        ans=0
        for i in range(0,len(n)):
            if n[i]=="1":
                ans+=1
        return ans