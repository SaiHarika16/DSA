class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        prev="0"
        for i in range(2,n+1):
            curr=prev
            curr+="1"
            inverted = ''.join('1' if c == '0' else '0' for c in prev)
            curr+=inverted[::-1]
            prev=curr
        return prev[k-1]