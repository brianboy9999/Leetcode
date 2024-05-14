class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        ans=[]
        for x,y in zip(nums,index):
            ans.insert(y,x)
        return ans