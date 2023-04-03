class Solution(object):
    def isValid(self, s):
        char = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        test = []
        for i in s:
            if i in char:
                test.append(i)
            elif len(test) == 0 or char[test.pop()] != i:
                return False
        return len(test) == 0

        """
        :type s: str
        :rtype: bool
        """