class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=list(set(nums))
        time=[0 for i in range(0,len(ans))]
        for i in range(0,len(ans)):
            for j in range(0,len(nums)):
                if ans[i]==nums[j]:
                    time[i]+=1
        return ans[time.index(max(time))]