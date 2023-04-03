class Solution(object):
    def climbStairs(self, n):
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            step = [0] * n
            step[0] = 1
            step[1] = 2
            for i in range(2, n):
                step[i] = step[i - 1] + step[i - 2]
        return step[n - 1]

        """
        :type n: int
        :rtype: int
        """