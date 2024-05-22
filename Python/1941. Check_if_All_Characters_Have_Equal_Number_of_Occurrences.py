class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        test=list(set(s))
        for i in range(0,len(test)-1):
            if s.count(test[i])!=s.count(test[i+1]):
                return False
        return True