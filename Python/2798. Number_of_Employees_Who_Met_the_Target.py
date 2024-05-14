class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        """
        :type hours: List[int]
        :type target: int
        :rtype: int
        """
        ans=0
        for X in hours:
            if X>=target:
                ans+=1
        return ans 