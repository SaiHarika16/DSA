class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sums=0
        res=float("inf")
        if sum(nums)<target:
            return 0
        elif target in nums:
            return 1
        else:
            left=0
            for i in range(len(nums)):
                sums+=nums[i]
                while sums>=target:
                    sums-=nums[left]
                    res=min(res,i-left+1)
                    left+=1
        return res