class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        jewel=0
        for stone in stones:
            if stone in jewels:
                jewel+=1
        return jewel