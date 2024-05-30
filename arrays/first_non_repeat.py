def first_non_repeating_char(string):
    char_counts = {}
    for char in string:
        char_counts[char] = char_counts.get(char, 0) + 1
    for char in string:
        if char_counts[char] == 1:
            return char
    return None

# text = 'leetcode'
# my_dict = {}
# for c in text:
#     my_dict[c] = my_dict.get(c, 0) + 1
# print(my_dict)
# print('- - - - -')
# print(my_dict.get('z', 0))
# print(my_dict.get('e', 0))

print( first_non_repeating_char('leetcode') )

print( first_non_repeating_char('hello') )

print( first_non_repeating_char('aabbcc') )



"""
    EXPECTED OUTPUT:
    ----------------
    l
    h
    None

"""