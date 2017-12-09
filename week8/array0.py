nums=[x for x in range(500)]
nums = list()
nums = [1, 2, 3 , 4]
nums.append(5)
nums.insert(0, 7) # adding in specifying index
nums[len(nums):] = [8, 9]

print(nums)