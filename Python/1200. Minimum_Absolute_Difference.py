class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr=sorted(arr)
        test=abs(arr[1]-arr[0])
        ans=[[arr[0],arr[1]]]
        for i in range(1,len(arr)-1):
            if abs(arr[i+1]-arr[i])<test:
                ans=[]
                ans.append([arr[i],arr[i+1]])
                test=abs(arr[i+1]-arr[i])
            elif abs(arr[i+1]-arr[i])==test:
                ans.append([arr[i],arr[i+1]])
            else:
                continue
        return ans