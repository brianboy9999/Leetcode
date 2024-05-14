class Solution(object):
    def findDelayedArrivalTime(self, arrivalTime, delayedTime):
        """
        :type arrivalTime: int
        :type delayedTime: int
        :rtype: int
        """
        time=arrivalTime+delayedTime
        if time>=24:
            return time-24
        else:
            return time