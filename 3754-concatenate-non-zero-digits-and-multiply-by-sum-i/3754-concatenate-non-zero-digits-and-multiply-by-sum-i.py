class Solution:
    def sumAndMultiply(self, n: int) -> int:
        res=""
        sums=0
        if n==0:
            return 0
        for num in str(n):
            if num!="0":
                res+=num
                sums+=int(num)
        return int(res)*sums