class Solution(object):
    def buyChoco(self, prices, money):
        """
        :type prices: List[int]
        :type money: int
        :rtype: int
        """
        prices=sorted(prices)
        test=money-prices[1]-prices[0]
        if test>=0:
            return test
        else:
            return money