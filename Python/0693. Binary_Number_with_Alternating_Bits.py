class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n=str(format(n,'b'))
        for i in range(0,len(n)-1):
            if n[i]==n[i+1]:
                return False
        return True