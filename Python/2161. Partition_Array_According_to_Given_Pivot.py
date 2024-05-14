class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        left=[]
        right=[]
        mid=[]
        ans=[]
        for X in nums:
            if X>pivot:
                right.append(X)
            elif X<pivot:
                left.append(X)
            else:
                mid.append(X)
        return left+mid+right