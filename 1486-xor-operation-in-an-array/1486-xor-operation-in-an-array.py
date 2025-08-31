class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        arr=[0]*n
        res=0
        for i in range(len(arr)):
            arr[i]=start+2*i
            res^=arr[i]
        return res
        
        