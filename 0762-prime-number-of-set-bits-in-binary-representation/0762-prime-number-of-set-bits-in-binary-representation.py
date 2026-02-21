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
            bin_i=format(i,"b")
            curr_count=0
            for bit in bin_i:
                if bit=="1":
                    curr_count+=1
            if self.isPrime(curr_count):
                count+=1
        return count
        