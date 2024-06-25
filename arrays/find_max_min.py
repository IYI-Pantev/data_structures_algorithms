def find_max_min(data_list):
    max_num_index = 0
    min_num_index = 0

    for i in range(1, len(data_list)):
        if data_list[i] > data_list[max_num_index]:
            max_num_index = i
        if data_list[i] < data_list[min_num_index]:
            min_num_index = i
    return (data_list[max_num_index], data_list[min_num_index])
            


print( find_max_min([5, 3, 8, 1, 6, 9]) )


"""
    EXPECTED OUTPUT:
    ----------------
    (9, 1)
    
"""