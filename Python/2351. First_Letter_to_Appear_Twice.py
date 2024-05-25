class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        test=[]
        for X in s:
            if X in test:
                return X
            else:
                test.append(X)