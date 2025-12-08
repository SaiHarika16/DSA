class Solution:
    def countTriples(self, n: int) -> int:
        count=0
        for i in range(1,n+1):
            for j in range(i+1,n+1):
                s=(i*i+j*j)**0.5
                if s<=n and s==int(s):
                    count+=2
        return count