def sel_sort(nums):
    for i in range(0,len(nums)-1):
        min = i
        for j in range(i + 1,len(nums)):
            if nums[j] < nums[min]:
                min = j
        nums[i],nums[min] = nums[min],nums[i]


l1 = [24,12,43,42,34354,542]
sel_sort(l1)
print(l1)