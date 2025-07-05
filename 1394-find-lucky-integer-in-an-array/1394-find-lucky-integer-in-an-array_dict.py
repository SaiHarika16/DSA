class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        freqs=Counter(arr)
        max_freq=-1
        for num,freq in freqs.items():
            if num==freq:
                max_freq=max(max_freq,num)
        return max_freq