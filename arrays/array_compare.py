# O(n^2)
def common_item(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False

# O(n)
def item_in_common(list1, list2):
    my_dict = {i:True for i in list1}
    
    for j in list2:
        if j in my_dict:
            return True
    return False


print(item_in_common([1, 2, 3], [4, 3, 5]))