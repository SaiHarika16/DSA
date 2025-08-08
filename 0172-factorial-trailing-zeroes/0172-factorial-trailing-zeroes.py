class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        prod=1
        for i in range(1,n+1):
            prod*=i
        return len(str(prod)) - len(str(prod).rstrip('0'))
        