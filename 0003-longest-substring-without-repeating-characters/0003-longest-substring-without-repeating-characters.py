class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res=0
        for i in range(len(s)):
            seen={}
            for j in range(i,len(s)):
                if s[j] in seen:
                    break
                seen[s[j]]=True
                res=max(res,j-i+1)
        return res