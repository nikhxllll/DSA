def prefix(nums):
    p = []

    for i in range(len(nums)):
        if i > 0:
            nums[i] += nums[i-1]
            p.append(nums[i])
        else:
            nums[i] = nums[i]
    return p


l = [10,20,30,40,50]

prefix(l)

print(l)