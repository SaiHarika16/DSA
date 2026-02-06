class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        res=0
        n=len(nums)
        l=0
        for r in range(n):
            if nums[r]>nums[l]*k:
                l+=1
            res=max(res,r-l+1)
        return n-res