class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        num=str(format(num,'b'))
        ans=""
        for X in num:
            if X=="0":
                ans+="1"
            else:
                ans+="0"
        return int(ans,2)