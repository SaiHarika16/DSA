class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count=0
        for i in arr:
            if self.is_odd(i):
                count+=1
                if count>=3:
                    return True
            else:
                count=0 
        return False
    def is_odd(self,n):
        if n%2==0:
            return False
        return True