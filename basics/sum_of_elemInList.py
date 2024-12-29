def listt(nums,idx = 0):
    if idx == len(nums):
        return 0
    return nums[idx]+listt(nums,idx+1)
     

numbers=[1,2,3,4,5]
print(listt(numbers))
