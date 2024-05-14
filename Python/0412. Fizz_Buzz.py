class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans=[]
        for X in range(1,n+1):
            if X%3==0 and X%5 == 0:
                ans.append("FizzBuzz")
            elif X%3==0:
                ans.append("Fizz")
            elif X%5==0:
                ans.append("Buzz")
            else:
                ans.append(str(X))
        return ans