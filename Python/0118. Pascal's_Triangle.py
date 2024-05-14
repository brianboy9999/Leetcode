class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans=[]
        for i in range(0,numRows):
            adds=[0]*(i+1)
            for j in range(0,len(adds)):
                if j==0 or j==i:
                    adds[j]=1
                else:
                    adds[j]=ans[i-1][j-1]+ans[i-1][j]
            ans.append(adds)
        return ans