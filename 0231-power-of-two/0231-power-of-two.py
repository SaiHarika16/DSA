class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==1:
            return True
        low=1
        high=n-1
        while low<=high:
            mid=(low+high)//2
            pow_res=2**mid
            if pow_res==n:
                return True
            elif(pow_res<n):
                low=mid+1
            else:
                high=mid-1
        return False
        