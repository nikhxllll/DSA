class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count  = 0
        current_count = 0
        for num in nums:
            if num == 1:
                current_count += 1
            else : 
                max_count = max(max_count,current_count)
                current_count = 0
        maxx = max(max_count,current_count)

        return maxx
    

    
    # normal array is used two variables is used 