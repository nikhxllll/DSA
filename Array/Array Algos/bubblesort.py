def bubblesort(nums):
    for i in range(1,len(nums)):
        for j in range(len(nums)-i): # here we used "i" insted of one coz of the upper loop for understanding well go to mysirg youtube channel
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
                # i +=1
                # j +=1

l = [10,50,20,30,40]
bubblesort(l)
print(l)