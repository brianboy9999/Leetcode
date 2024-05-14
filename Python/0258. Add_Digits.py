class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        num=str(num)
        while len(num)!=1:
            num=str(sum([int(X) for X in num]))
        return int(num)