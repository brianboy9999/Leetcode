class Solution(object):
    def convertDateToBinary(self, date):
        """
        :type date: str
        :rtype: str
        """
        dates = date.split("-")
        for i, value in enumerate(dates):
            dates[i] = bin(int(value))[2:]
        return dates[0]+'-'+dates[1]+'-'+dates[2]