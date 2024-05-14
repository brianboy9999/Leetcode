class Solution(object):
    def isAcronym(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: bool
        """
        ans=""
        for X in words:
            ans+=X[0]
        return ans==s