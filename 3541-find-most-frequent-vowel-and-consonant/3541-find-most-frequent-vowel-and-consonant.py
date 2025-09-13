class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowel_count=0
        cons_count=0
        for i in s:
            if i in "aeiou":
                vcount=s.count(i)
                vowel_count=max(vcount,vowel_count)
            else:
                ccount=s.count(i)
                cons_count=max(ccount,cons_count)
        return vowel_count+cons_count

        