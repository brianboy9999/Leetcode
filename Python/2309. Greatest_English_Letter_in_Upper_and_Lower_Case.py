class Solution(object):
    def greatestLetter(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans=""
        test=set(s)
        for X in test:
            if X.isupper() and X.lower() in s:
                ans=max(ans,X.upper())
        return ans