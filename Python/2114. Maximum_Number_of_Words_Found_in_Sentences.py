class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        return max([len(sentences[i].split(" ")) for i in range(0,len(sentences))])