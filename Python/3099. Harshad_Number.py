class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        """
        :type x: int
        :rtype: int
        """
        ans=sum([int(X) for X in str(x)])
        if x%ans==0:
            return ans
        else:
            return -1