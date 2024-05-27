class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        ans=0
        for X in words:
            test=True
            for Y in X:
                if Y not in allowed:
                    test=False
            if test==True:
                ans+=1
        return ans