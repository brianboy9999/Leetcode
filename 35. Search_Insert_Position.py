def searchInsert(nums,target):
    if target in nums:
        return nums.index(target)
    else:
        ans=0
        while nums[ans]<target:
            ans+=1
            if ans==len(nums)-1:
                return ans+1
                break
        return ans
print(searchInsert([1,3,5,6],7))