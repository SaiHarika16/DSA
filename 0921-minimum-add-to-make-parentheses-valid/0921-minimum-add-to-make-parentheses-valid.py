class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_brackets=0
        min_adds_needed=0
        for i in s:
            if i=="(":
                open_brackets+=1
            else:
                if open_brackets>=1:
                    open_brackets-=1
                else:
                    min_adds_needed+=1
        return open_brackets+min_adds_needed
        