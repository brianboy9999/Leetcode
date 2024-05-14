class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if (x<0):
            return False
        elif (x==0):
            return True
        elif(x%10==0):
            return False
        else:
            num=[]
            while x>=1:
                num.append(str(x%10))
                x=x//10
            renum=[]
            i=len(num)
            while i>0:
                renum+=num[i-1]
                i-=1
            if (num==renum):
                return True
            else:
                return False