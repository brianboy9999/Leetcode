class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        ans=[]
        for i in range(0,len(words)):
            if x in words[i]:
                ans.append(i)
        return ans