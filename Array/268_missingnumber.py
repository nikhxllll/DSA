class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expectedSum = n*(n+1) // 2
        return expectedSum - sum(nums) 
    

    # you can used XOR also
    # but this is the simplest soln to this problem