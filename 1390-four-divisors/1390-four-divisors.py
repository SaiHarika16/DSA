class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        count=0
        sum_of_divisors=0
        res=0
        for i in nums:
            for j in range(1,int(i**0.5)+1):
                if(i%j==0):
                    if j*j==i:
                        count+=1
                        sum_of_divisors+=j
                    else:
                        count+=2
                        sum_of_divisors+=j
                        sum_of_divisors+=i//j
                if count>4:
                    break
            if count==4:
                res+=sum_of_divisors
            count=0
            sum_of_divisors=0
        return res