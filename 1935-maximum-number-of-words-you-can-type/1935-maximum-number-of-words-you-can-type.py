class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        n=len(text.split())
        for word in text.split():
            for char in word:
                if char in brokenLetters:
                    n-=1
                    break
        return n 