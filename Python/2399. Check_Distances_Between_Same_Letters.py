class Solution(object):
    def checkDistances(self, s, distance):
        """
        :type s: str
        :type distance: List[int]
        :rtype: bool
        """
        test=set(s)
        for X in test:
            if s[s.index(X)+1:].index(X)!=distance[ord(X)-97]:
                return False
        return True