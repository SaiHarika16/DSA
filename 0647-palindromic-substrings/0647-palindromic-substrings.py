class Solution:
    def countSubstrings(self, s: str) -> int:
        count=0
        for i in range(len(s)):
            for j in range(i,len(s)):
                curr_s=s[i:j+1]
                if curr_s==curr_s[::-1]:
                    count+=1
        return count