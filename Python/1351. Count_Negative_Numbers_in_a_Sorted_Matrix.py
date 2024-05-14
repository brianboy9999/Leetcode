class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        negative=0
        for i in range(0,len(grid)):
            for j in range(0,len(grid[i])):
                if grid[i][j]<0:
                    negative+=1
        return negative