class Solution(object):
    def evenOddBit(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        n=format(n,"b")[::-1]
        ans=[0,0]
        for i in range(0,len(n)):
            if n[i]=="1":
                if int(i%2)==0:
                    ans[0]+=1
                else:
                    ans[1]+=1
        return ans