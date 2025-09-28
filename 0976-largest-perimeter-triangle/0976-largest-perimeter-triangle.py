class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        max_peri=0
        nums.sort()
        for i in range(len(nums)-1,1,-1):
            if nums[i]<nums[i-1]+nums[i-2]:
                curr_peri=nums[i]+nums[i-1]+nums[i-2]
                max_peri=max(curr_peri,max_peri)
        return max_peri