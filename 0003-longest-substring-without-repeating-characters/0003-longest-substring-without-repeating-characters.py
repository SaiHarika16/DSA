class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res_set=set()
        left=0
        max_length=0
        for right in range(len(s)):
            while s[right] in res_set:
                res_set.remove(s[left])
                left+=1
            res_set.add(s[right])
            max_length=max(max_length,right-left+1)
        return max_length



        