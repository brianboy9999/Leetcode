class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==1:
            return True
        elif n==0:
            return False
        else:
            while n!=3:
                if n%3!=0:
                    return False
                else:
                    n/=3
        return True