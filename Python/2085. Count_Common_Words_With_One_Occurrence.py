class Solution(object):
    def countWords(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """
        words=set(words1+words2)
        return sum([1 for X in words if words1.count(X)==1 and words2.count(X)==1])