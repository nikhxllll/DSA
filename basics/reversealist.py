def reversee(nums,idx1 = 0,idx2 = len(nums)):
    if idx1 == idx2:
        return 
    reversee(nums[idx1],nums[idx2] = nums[idx2],nums[idx1])