class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        test=sorted(s.split(" "),key=lambda x: x[-1])
        ans=[]
        for i in range(0,len(test)):
            ans.append(test[i][:-1])
        return " ".join(ans)