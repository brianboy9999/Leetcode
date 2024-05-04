class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==1:
            return True
        elif n==0:
            return False
        else:
            while n!=4:
                if n%4!=0:
                    return False
                else:
                    n/=4
        return True