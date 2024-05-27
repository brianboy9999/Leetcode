class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        times=[]
        test=list(set(arr))
        for i in range(0,len(test)):
            if arr.count(test[i]) in times:
                return False
            times.append(arr.count(test[i]))
        return True