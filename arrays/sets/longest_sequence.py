def longest_consecutive_sequence(nums):
    filt = set()
    numbers = sorted(nums)
    for i in range(len(numbers)):
        prev = numbers[i - 1]
        if numbers[i] == prev + 1:
            filt.add(prev)
            filt.add(numbers[i])
    if len(filt) > 1:
        return len(filt)
    else:
        return 0
        
# second way

# def longest_consecutive_sequence(nums):
#     num_set = set(nums)
#     longest_sequence = 0
    
#     for num in nums:
#         if num - 1 not in num_set:
#             current_num = num
#             current_sequence = 1
            
#             while current_num + 1 in num_set:
#                 current_num += 1
#                 current_sequence += 1
            
#             longest_sequence = max(longest_sequence, current_sequence)
    
#     return longest_sequence

print( longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) )



"""
    EXPECTED OUTPUT:
    ----------------
    4

"""