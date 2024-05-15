class Solution(object):
    def findPermutationDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        ans=0
        for i in range(0,len(s)):
            ans+=abs(i-t.index(s[i]))
        return ans