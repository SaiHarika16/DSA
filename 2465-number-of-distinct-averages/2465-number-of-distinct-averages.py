class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        avgs=[]
        while nums:
            curr_max=max(nums)
            curr_min=min(nums)
            avgs.append((curr_max+curr_min)/2)
            nums.remove(curr_max)
            nums.remove(curr_min)
        return len(set(avgs))
        