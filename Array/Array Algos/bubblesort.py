def bubblesort(nums):
    for i in range(1,len(nums)):
        for j in range(len(nums)-i): # here we used "i" insted of one coz of the upper loop for understanding well go to mysirg youtube channel
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
                
l = [10,50,20,30,40]
bubblesort(l)
print(l)




# Modified bubble sort

def modifiedbubblesort(nums1):
    for i in range(1,len(nums1)):
        flag = False
        for j in range(len(nums1)-i): 
            if nums1[j]>nums1[j+1]:
                nums1[j],nums1[j+1] = nums1[j+1],nums1[j]
                flag = True
        if not flag:
            break

modifiedbubblesort(l)
print(l)
