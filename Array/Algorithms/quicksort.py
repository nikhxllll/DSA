def quicksort(nums):
    # i = 0
    pivot = 0
    for i in range(len(nums)-1):
        if nums[pivot] > nums[i+1]:
            nums[pivot],nums[i + 1] = nums[i + 1],nums[pivot]
        else:
            pivot+=1
    return nums


l1 = [10,50,30,20,40]

quicksort(l1)
print(l1)