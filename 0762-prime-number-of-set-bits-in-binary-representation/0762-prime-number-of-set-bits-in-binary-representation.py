class Solution:
    def isPrime(self,n: int) -> int:
        if n<2:
            return False
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        return True
    def countPrimeSetBits(self, left: int, right: int) -> int:
        count=0
        for i in range(left,right+1):
            curr_count=i.bit_count()
            if self.isPrime(curr_count):
                count+=1
        return count       