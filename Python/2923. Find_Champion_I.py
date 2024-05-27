class Solution(object):
    def findChampion(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        for i in range(0,len(grid)):
            grid[i]=sum(grid[i])
        return grid.index(max(grid))