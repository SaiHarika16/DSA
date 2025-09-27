class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_p=0
        min_needed=0
        for i in s:
            if i=="(":
                open_p+=1
            else:
                if open_p>=1:
                    open_p-=1
                else:
                    min_needed+=1
        return min_needed+open_p
        