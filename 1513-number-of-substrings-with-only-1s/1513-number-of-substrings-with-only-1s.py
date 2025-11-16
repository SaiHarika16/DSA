class Solution:
    def numSub(self, s: str) -> int:
        mod=10**9+7
        res=0
        count=0
        for i in s:
            if i=="1":
                count+=1
            elif(i=="0"):
                res+=(count*(count+1))//2
                count=0
            else:
                pass
        res+=(count*(count+1))//2
        return res%mod