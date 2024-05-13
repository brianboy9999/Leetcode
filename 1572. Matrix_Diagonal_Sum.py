class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        ans=0
        for i in range(0,len(mat)):
            if i!=len(mat)-i-1:
                ans+=mat[i][i]+mat[i][len(mat)-i-1]
            else:
                ans+=mat[i][i]
        return ans