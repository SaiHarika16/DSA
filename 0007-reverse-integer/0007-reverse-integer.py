class Solution:
    def reverse(self, x: int) -> int:
        sign=-1 if x<0 else 1
        x_abs=abs(x)

        rev_int=int(str(x_abs)[::-1])*sign

        if rev_int<2**31-1 and rev_int>-2**31:
            return rev_int
        else:
            return 0
        
        