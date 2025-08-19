class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count=0
        n=len(nums)
        res=0
        for num in range(len(nums)):
            if(nums[num]==0):
                count+=1
            else:
                res+=(count*(count+1))//2
                count=0
        res+=(count*(count+1))//2
        return res

        