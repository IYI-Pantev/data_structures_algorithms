def print_items(n):
    for i in range(n):
        print(i)

    # O(2n) - O(n) -> DROP CONSTANTS SIMPLIFYING
    for j in range(n):
        print_items(j)
print_items(10)