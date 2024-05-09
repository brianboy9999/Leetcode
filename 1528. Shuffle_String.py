class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        ans=""
        for i in range(0,len(s)):
            ans+=s[indices.index(i)]
        return ans