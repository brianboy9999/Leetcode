class Solution(object):
    def isPalindrome(self, x):
        forw = x
        back = 0
        for i in range(len(str(x)) - 1, -1, -1):
            a = x % 10
            x //= 10
            back += a * (10 ** i)

        if forw == back:
            return True
        else:
            return False

        """
        :type x: int
        :rtype: bool
        """