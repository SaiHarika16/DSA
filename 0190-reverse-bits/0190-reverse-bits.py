class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res="{0:032b}".format(n)
        res=res[::-1]
        return int(res,2)

        