class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        ans=[]
        for i in range(0,len(candies)):
            ans.append(candies[i]+extraCandies>=max(candies))
        return ans