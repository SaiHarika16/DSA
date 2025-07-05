class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        max_res=-1
        for i in range(len(arr)):
            if(arr.count(arr[i])==arr[i]):
                max_res=max(max_res,arr[i])
        return max_res