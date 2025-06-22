class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        ans = [s[i: i + k] for i in range(0, len(s), k)]
        ans[-1] += fill * (k - len(ans[-1]))
        return ans
        
        