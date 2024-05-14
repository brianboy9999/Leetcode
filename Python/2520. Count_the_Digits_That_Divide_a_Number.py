class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        time=0
        for X in str(num):
            if num%int(X)==0:
                time+=1
        return time