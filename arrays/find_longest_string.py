def find_longest_string(data_list):
    if len(data_list) < 2 and len(data_list) != 0:
        return data_list[0]
    if len(data_list) == 0:
        return ''
    longest_index = 0
    for i in range(1, len(data_list)):
        if len(data_list[i]) > len(data_list[longest_index]):
            longest_index = i
    return data_list[longest_index] 


string_list = ['apple', 'banana', 'kiwi', 'pear']
longest = find_longest_string(string_list)
print(longest)  


"""
    EXPECTED OUTPUT:
    ----------------
    banana
    
"""