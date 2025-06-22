class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        res=[s[i:i+k] for i in range(0,len(s),k)]
        res[-1]+=fill*(k-len(res[-1]))
        return res
        
        