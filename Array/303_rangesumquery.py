class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        total = 0
        for i in nums:
            total += i
            self.prefix.append(total)


    def sumRange(self, left: int, right: int) -> int:
        rightSum = self.prefix[right]
        
        if left > 0:
            leftSum  = self.prefix[left-1] 
        else:
            leftSum = 0
        
        return rightSum - leftSum


# Prefix sum is used


