class Solution:
    def longestBalanced(self, s: str) -> int:
        n=len(s)
        res=0
        for i in range(n):
            s_freqs={}
            for j in range(i,n):
                s_freqs[s[j]]=s_freqs.get(s[j],0)+1
                if len(set(s_freqs.values()))==1:
                    res=max(res,j-i+1)
        return res