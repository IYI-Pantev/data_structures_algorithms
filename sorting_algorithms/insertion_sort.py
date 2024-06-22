
# first way
# def insertion_sort(data_list):
#     for i in range(1, len(data_list)):
#         temp = data_list[i]
#         j = i - 1
#         while temp < data_list[j] and j > -1:
#             data_list[j+1] = data_list[j]
#             data_list[j] = temp
#             j -= 1
#     return data_list
# print(insertion_sort([4, 2, 6, 5, 1, 3]))

#second way
def insertion_sort(data_list):
    for i in range(1, len(data_list)):
    
        while data_list[i-1] > data_list[i] and i > 0:
            data_list[i], data_list[i-1] = data_list[i-1], data_list[i]
            i -= 1

    return data_list

print(insertion_sort([3, 1, 6, 5, 4, 2]))