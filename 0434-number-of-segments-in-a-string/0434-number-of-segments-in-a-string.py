class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s=="":
            return 0
        s=s.split(" ")
        return len(s)
        