class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=s.split()
        ans=[]
        for X in s:
            ans.append(X[::-1])
        return " ".join(ans)