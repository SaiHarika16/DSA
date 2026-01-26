class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        n=len(arr)
        min_diff=float("inf")
        min_diff_arr=[]
        for i in range(0,n-1):
            min_diff=min(min_diff,arr[i+1]-arr[i])
        for i in range(0,n-1):
            if arr[i+1]-arr[i]==min_diff:
                min_diff_arr.append((arr[i],arr[i+1]))
        return min_diff_arr