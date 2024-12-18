class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]== target:
                    return [i,j]
                
                # This is the optimized version


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in h:
                return [h[diff],i] 
            h[n] = i

            # this is the most optimized version
