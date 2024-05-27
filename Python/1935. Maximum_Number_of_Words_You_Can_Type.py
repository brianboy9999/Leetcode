class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        text=text.split(" ")
        ans=len(text)
        for X in text:
            for Y in brokenLetters:
                if Y in X:
                    ans-=1
                    break
        return ans