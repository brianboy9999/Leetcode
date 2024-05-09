class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """

        piles.sort(reverse=True)
        del piles[int(len(piles)*2/3):(len(piles))]
        ans=0
        for i in range(0,len(piles)):
            if i%2!=0:
                ans+=piles[i]
        return ans