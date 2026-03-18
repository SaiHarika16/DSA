class Solution:
    def frequencySort(self, s: str) -> str:
        res=""
        freqs=Counter(s)
        sorted_freqs=sorted(freqs.items(), key=lambda x:x[1], reverse=True)
        for val,f in sorted_freqs:
            res+=val*f
        return res