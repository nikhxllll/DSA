class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        min = nums[0]

        for n in nums:
            if abs(n) < abs(min):
                min = n

        if min < 0 and abs(min) in nums:
            return abs(min)
        else:
            return min
        
        # return abs(min)




        #  array question