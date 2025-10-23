class Solution:
    def hasSameDigits(self, s: str) -> bool:
        new_s=""
        while len(new_s)!=2:
            new_s=""
            for i in range(len(s)-1):
                new_s+=str((int(s[i]) + int(s[i+1])) % 10)
            s=new_s
        if(new_s[0]==new_s[1]):
            return True
        return False

        