class Solution(object):
    def rowAndMaximumOnes(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        ans=[]
        for X in mat:
            ans.append(sum(X))
        return [ans.index(max(ans)),max(ans)]