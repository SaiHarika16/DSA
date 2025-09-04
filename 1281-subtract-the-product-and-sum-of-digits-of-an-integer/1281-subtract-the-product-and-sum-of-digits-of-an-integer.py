class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sums=0
        product=1
        for i in str(n):
            sums+=int(i)
            product*=int(i)
        return product-sums
        