class Solution(object):
    def removeTrailingZeros(self, num):
        """
        :type num: str
        :rtype: str
        """
        num=int(num[::-1])
        return str(num)[::-1]