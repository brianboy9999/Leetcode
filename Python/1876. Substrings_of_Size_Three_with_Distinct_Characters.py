class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans=0
        for i in range(0,len(s)-2):
            if len(set(s[i:i+3]))==3:
                ans+=1
        return ans