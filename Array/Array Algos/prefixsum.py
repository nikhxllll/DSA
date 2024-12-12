def prefix(nums):
    p = []

    for i in range(len(nums)):
        if i > 0:
            nums[i] += nums[i-1]
            p.append(nums[i])
        else:
            nums[i] = nums[i]
    return p


l = [1,2,3,4,5]

prefix(l)

print(l)