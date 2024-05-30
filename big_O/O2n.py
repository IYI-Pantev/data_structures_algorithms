def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)
    # insignificatn by the time complexity 
    # simplification technique
    for k in range(n):
        print(k)
print_items(5)