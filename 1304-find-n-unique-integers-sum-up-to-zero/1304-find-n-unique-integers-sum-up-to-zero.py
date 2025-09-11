class Solution:
    def sumZero(self, n: int) -> List[int]:
        res=[0]*n
        start=-1*(n//2)
        if n%2!=0:
            for i in range(len(res)):
                res[i]=start
                start+=1
        else:
            for i in range(len(res)):
                res[i]=start
                start+=1
            res[-1]=0-sum(res[:-1])
        return res

        