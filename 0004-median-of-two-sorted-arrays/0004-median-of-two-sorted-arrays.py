class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i=0
        j=0
        res_nums=[]
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<=nums2[j]:
                res_nums.append(nums1[i])
                i+=1
            else:
                res_nums.append(nums2[j])
                j+=1
                
        while i < len(nums1):
            res_nums.append(nums1[i])
            i += 1

        while j < len(nums2):
            res_nums.append(nums2[j])
            j += 1

        n=len(res_nums)
        if n%2==0:
            return (res_nums[(n//2)-1]+res_nums[n//2])/2
        else:
            return res_nums[n//2]