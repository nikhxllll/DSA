class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix = []
        # total = 0

        for i in range(len(nums)):
            if i > 0:
                nums[i] += nums[i - 1]
                prefix.append(nums[i])
            else :
                nums[i] = nums[i]
                prefix.append(nums[i])
        return prefix

