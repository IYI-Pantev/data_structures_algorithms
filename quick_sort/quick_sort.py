def swap(data_list, index1, index2):
    temp = data_list[index1]
    data_list[index1] = data_list[index2]
    data_list[index2] = temp



def pivot(data_list, pivot_index, end_index):
    swap_index = pivot_index

    for i in range(pivot_index+1, end_index+1):
        if data_list[i] < data_list[pivot_index]:
            swap_index += 1
            swap(data_list, swap_index, i)
    swap(data_list, pivot_index, swap_index)

    return swap_index

# data_list = [4, 6, 1, 7, 3, 2, 5]

# print(pivot(data_list, 0, 6))

def quick_sort_helper(data_list, left, right):
    if left < right:
        pivot_index = pivot(data_list, left, right)
        quick_sort_helper(data_list, left, pivot_index - 1)
        quick_sort_helper(data_list, pivot_index+1, right)
    return data_list

def quick_sort(data_list):
    return quick_sort_helper(data_list, 0, len(data_list)-1)

print(quick_sort([4, 6, 1, 7, 3, 2, 5]))