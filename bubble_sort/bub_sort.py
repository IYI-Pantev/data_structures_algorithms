def bubble_sort(data_list):
    for i in range(len(data_list) - 1, 0, -1):
        for j in range(i):
            if data_list[j] > data_list[j + 1]:
                data_list[j], data_list[j+1] = data_list[j+1], data_list[j]
    return data_list
    
print(bubble_sort([3, 8, 4, 1, 9]))