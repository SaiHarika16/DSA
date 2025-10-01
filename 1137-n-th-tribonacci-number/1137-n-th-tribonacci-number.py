class Solution:
    def tribonacci(self, n: int) -> int:
        if n<=1:
            return n
        dp=[0]*(n+1)
        prev1=0
        prev2=1
        prev3=1
        for i in range(3,n+1):
            curr=prev1+prev2+prev3
            prev1=prev2
            prev2=prev3
            prev3=curr
        return prev3

        