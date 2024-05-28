class Solution(object):
    def areNumbersAscending(self, s):
        """
        :type s: str
        :rtype: bool
        """
        test=[int(X) for X in s.split(" ") if X.isdigit()]
        return len(set(test))==len(test) and sorted(test)==test