class Solution(object):
    def maximumNumberOfStringPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        ans=0
        for i in range(0,len(words)-1):
            for j in range(i+1,len(words)):
                if words[i]==words[j][::-1]:
                    ans+=1
        return ans