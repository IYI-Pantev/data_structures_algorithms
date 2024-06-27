def twoSum(nums, target):
    complement = 0
    indices_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in indices_dict:
            return [indices_dict[complement], i]
        else:
            indices_dict[num] = i 
            






nums = [3,4,5,6]
# print(list(enumerate(nums)))
target = 7

# print(twoSum(nums, target))
print(twoSum([5,5], 10))