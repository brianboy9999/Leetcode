class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        ans=[]
        for X in range(left,right+1):
            test=str(X)
            i=0
            while i!=len(test):
                if int(test[i])==0:
                    break
                elif X%int(test[i])!=0:
                    break
                i+=1
            if i==len(test):
                ans.append(X)
        return ans