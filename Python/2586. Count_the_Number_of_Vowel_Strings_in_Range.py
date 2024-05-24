class Solution(object):
    def vowelStrings(self, words, left, right):
        """
        :type words: List[str]
        :type left: int
        :type right: int
        :rtype: int
        """
        ans=0
        test=["a","e","i","o","u"]
        for i in range(left,right+1):
            if words[i][0] in test and words[i][-1] in test:
                ans+=1
        return ans