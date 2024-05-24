class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type queryTime: int
        :rtype: int
        """
        return sum([startTime[i]<=queryTime and endTime[i]>=queryTime for i in range(0,len(startTime))])