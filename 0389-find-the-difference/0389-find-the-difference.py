class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s_sum=0
        t_sum=0
        for i in s:
            s_sum+=ord(i)
        for j in t:
            t_sum+=ord(j)
        return chr(t_sum-s_sum)
        
        