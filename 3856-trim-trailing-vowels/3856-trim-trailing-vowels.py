class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        vowels=["a","e","i","o","u"]
        ind=0
        for i in range(len(s)-1,-1,-1):
            if s[i] not in vowels:
                return s[:i+1]
        return ""