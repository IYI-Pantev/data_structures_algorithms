def find_duplicates(nums):
    my_dict = {}
    duplicates = []
    for i in nums:
        if i in my_dict and i not in duplicates:
            duplicates.append(i)
        else:
            my_dict[i] = None
    return duplicates
            
    
    
       

# # print(find_duplicates([2, 6, 8, 2, 3, 9, 7, 3]))
# # ? 
# print(find_duplicates([2, 6, 8, 3, 9]))
print ( find_duplicates([1, 2, 3, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 3]) )
print ( find_duplicates([1, 1, 1, 1, 1]) )
print ( find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([]) )



"""
    EXPECTED OUTPUT:
    ----------------
    []
    [1, 2]
    [1]
    [3, 4]
    [1, 2, 3]
    [1, 2, 3]
    []

"""
