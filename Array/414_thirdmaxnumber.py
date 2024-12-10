class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        uniquenums = set(nums)
        sortednums = sorted(uniquenums,reverse = True)
        if len(sortednums)>=3:
            return sortednums[2]
        else:
            return sortednums[0]

