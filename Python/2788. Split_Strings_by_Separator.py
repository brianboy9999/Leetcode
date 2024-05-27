class Solution(object):
    def splitWordsBySeparator(self, words, separator):
        """
        :type words: List[str]
        :type separator: str
        :rtype: List[str]
        """
        ans=[]
        for X in words:
            test=X.split(separator)
            for Y in test:
                if Y!="":
                    ans.append(Y)
        return ans