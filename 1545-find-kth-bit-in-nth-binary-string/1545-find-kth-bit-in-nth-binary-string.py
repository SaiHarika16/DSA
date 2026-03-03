class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        prev1="011"
        prev2="0"
        if n==1:
            return prev2
        if n==2:
            return prev1
        curr=""
        for i in range(2,n+1):
            curr=prev1
            curr+="1"
            inverted = ''.join('1' if c == '0' else '0' for c in prev1)
            curr+=inverted[::-1]
            prev1=curr
            prev2=prev1
            print(curr)
        return curr[k-1]