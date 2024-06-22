def invert_selection_sort(data_list):
    for i in range(len(data_list) - 1, 0, -1):
        min_index = i
        for j in range(i-1, -1, -1):
            if data_list[j] < data_list[min_index]:
                min_index = j
        if i != min_index:
            data_list[i], data_list[min_index] = data_list[min_index], data_list[i]
    return data_list

print(invert_selection_sort([4, 2, 5, 6, 1, 3]))