num = 11

num2 = num
print('num:',num)
print('num2:',num2)
print('num points to :', id(num))
print('num2 points to :', id(num2))

num2 = 22
print('after num2 value is changed:')
print('num:',num)
print('num2:',num2)
print('num points to :', id(num))
print('num2 points to :', id(num2))
print('- - - - - - - ')
# while integers are immutable
# dictionaries can change
dict1 = {
    'value': 11
}

dict2 = dict1
print('dict1:', dict1)
print('dict2:', dict2)
print(id(dict1))
print(id(dict2))

dict2['value'] = 22
print('after dict2 value is changed:')
print(id(dict1))
print(id(dict2))
print('dict1 value:', dict1)
print('dict2 value', dict2)