class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        ans=0
        for X in words:
            test=True
            for Y in X:
                if X.count(Y)>chars.count(Y):
                    test=False
                    break
            if test==True:
                ans+=len(X)
        return ans