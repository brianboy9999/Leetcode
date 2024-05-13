class Solution(object):
    def countTestedDevices(self, batteryPercentages):
        """
        :type batteryPercentages: List[int]
        :rtype: int
        """
        time=0
        for X in batteryPercentages:
            if X-time>0:
                time+=1
        return time