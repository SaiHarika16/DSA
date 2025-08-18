class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n=len(grid)
        expected_sum=((n**2)*(n**2+1))//2
        expected_sum_of_squares=((n**2)*(n**2+1)*(2*n**2+1))//6
        actual_sum=0
        actual_sum_of_squares=0
        for i in grid:
            for j in i:
                actual_sum+=j
                actual_sum_of_squares+=j*j
        #b-a
        #b is missing
        #a is repeated
        sum_diff=expected_sum-actual_sum
        #b^2-a^2
        sqr_diff=expected_sum_of_squares-actual_sum_of_squares
        #b+a
        sum_sum=(sqr_diff)//(sum_diff)
        missing=(sum_diff+sum_sum)//2
        repeated=missing-sum_diff
        return [repeated,missing]



