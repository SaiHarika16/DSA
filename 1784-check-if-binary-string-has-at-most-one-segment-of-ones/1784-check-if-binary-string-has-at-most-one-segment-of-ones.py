class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        end_index=len(s)-1
        for i in range(len(s)-1):
            if s[i]=="1" and s[i]!=s[i+1]:
                end_index=i
                break
        for i in range(end_index+1,len(s)):
            if s[i]=="1":
                return False
        return True