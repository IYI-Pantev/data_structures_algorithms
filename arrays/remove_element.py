# 1st way
# def remove_element(nums, val):
#     while val in nums:
#          n = nums.pop(0)
#          if n == val:
#               continue
#          else:
#               nums.append(n)
#     return len(nums)

# second way
def remove_element(nums, val):
    i = 0
    while i < len(nums):
        if nums[i] == val:
            nums.pop(i)
        else:
            i += 1
    return len(nums)

nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
val1 = 1
print('Before:', nums1)
print('len of list:', len(nums1))
remove_element(nums1, val1)
print('After:', nums1)
print('len of list:', len(nums1))