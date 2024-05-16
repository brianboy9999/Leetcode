class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        i=0
        ans=""
        while i!=max(len(word1),len(word2)):
            if i<len(word1) and i<len(word2):
                ans+=word1[i]
                ans+=word2[i]
            elif i<len(word1) and i>=len(word2):
                ans+=word1[i]
            else:
                ans+=word2[i]
            i+=1
        return ans