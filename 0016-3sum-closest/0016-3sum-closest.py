class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        min_diff=float("inf")
        res=float("inf")
        nums.sort()
        for i in range(len(nums)-2):
            left,right=i+1,len(nums)-1
            while left<right:
                curr_sum=nums[i]+nums[left]+nums[right]
                curr_diff=abs(target-curr_sum)
                if curr_diff<min_diff:
                    min_diff=curr_diff
                    res=curr_sum
                if curr_sum<target:
                    left+=1
                elif curr_sum>target:
                    right-=1
                else:
                    return target
        return res