class Solution(object):
    def splitNum(self, num):
        """
        :type num: int
        :rtype: int
        """
        nums=sorted(list(str(num)))
        num1=""
        num2=""
        for i in range(0,len(nums)):
            if i%2==0:
                num1+=nums[i]
            else:
                num2+=nums[i]
        return int(num1)+int(num2)