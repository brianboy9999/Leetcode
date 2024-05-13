class Solution(object):
    def finalString(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans=""
        for X in s:
            if X != "i":
                ans+=X
            else:
                ans=ans[::-1]
        return ans