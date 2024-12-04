class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for n in range(len(nums)):
            for i in range(n+1,len(nums)):
                if nums[n] == nums[i]:
                    return True
        
        return False
    
# //Optimized approach

def containsDuplicate(nums):
    # Create an empty set to track elements we've seen
    seen = set()
    
    # Iterate over each number in the list
    for num in nums:
        # If the number is already in the set, return True (duplicate found)
        if num in seen:
            return True
        # Otherwise, add the number to the set
        seen.add(num)
    
    # If no duplicates are found, return False
    return False
