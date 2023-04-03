class Solution(object):
    def mySqrt(self, x):
        i = 1
        while i ** 2 < x:
            i += 1
        if i ** 2 == x:
            return i
        else:
            return i - 1

        """
        :type x: int
        :rtype: int
        """