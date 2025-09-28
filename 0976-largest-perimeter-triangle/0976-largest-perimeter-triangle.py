class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        max_per=0
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[k]<nums[i]+nums[j]:
                        curr_per=nums[i]+nums[j]+nums[k]
                        max_per=max(curr_per,max_per)
        return max_per