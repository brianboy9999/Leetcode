class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        if ch not in word:
            return word
        else:
            loc=word.find(ch)
        left=word[0:(loc+1)]
        right=word[(loc+1):]
        left=left[len(left)::-1]
        return left+right

    
