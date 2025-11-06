class Solution:
    def reverseWords(self, s: str) -> str:
        words=s.strip().split()
        rev_s=""
        for word in range(len(words)-1,-1,-1):
            rev_s+=words[word]+" "
        return rev_s.strip()