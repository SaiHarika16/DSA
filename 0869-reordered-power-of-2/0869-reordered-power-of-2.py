class Solution(object):
    def reorderedPowerOf2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        target="".join(sorted(str(n)))
        for i in range(31):
            curr_pow=str(1 << i)
            if("".join(sorted(curr_pow))==target):
                return True
        return False

        