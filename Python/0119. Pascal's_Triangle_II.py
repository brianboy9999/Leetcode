class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        i=0
        ex=[1]
        while i<=rowIndex:
            ans=[0]*(i+1)
            for j in range(0,len(ans)):
                if j==0 or j==i:
                    ans[j]=1
                else:
                    ans[j]=ex[j-1]+ex[j]
            ex=ans
            i+=1
        return ans   