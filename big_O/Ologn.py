def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2  # Calculate the middle index
        
        if arr[mid] == target:
            return mid  # Found the target, return its index
        elif arr[mid] < target:
            low = mid + 1  # Discard the left half
        else:
            high = mid - 1  # Discard the right half
    
    return -1  # Target not found

# Example usage:
numbers = [2, 5, 8, 12, 16, 23, 38, 56]
target_number = 5

result = binary_search(numbers, target_number)

if result != -1:
    print(f"Found {target_number} at index {result}.")
else:
    print(f"{target_number} not found in the list.")
