class Solution(object):
    def commonFactors(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        end=min(a,b)
        time=0
        for i in range(1,end+1):
            if a%i==0 and b%i==0:
                time+=1
        return time