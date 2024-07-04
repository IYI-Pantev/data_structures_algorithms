def reverse_string(text):
    for i in range(len(text)-1):
        c = text.pop()
        text.insert(i, c)

text = ['h', 'e', 'l', 'l', 'o']
reverse_string(text)
print(text)
# print(text[::-1])

# revers = text[::-1]
# print(revers)