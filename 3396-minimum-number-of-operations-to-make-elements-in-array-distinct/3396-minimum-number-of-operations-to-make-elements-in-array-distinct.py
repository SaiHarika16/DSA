class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        seen = set()
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] in seen:
                # Found duplicate → remove first (i+1) elements in ceil((i+1)/3) ops
                return (i + 3) // 3
            seen.add(nums[i])
        return 0
