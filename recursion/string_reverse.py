def reverse_string(s):
    # Base case: if the string is empty or a single character, return it as is
    if len(s) <= 1:
        return s
    else:
        # Recursive case: return the last character plus the reverse of the rest of the string
        return s[-1] + reverse_string(s[:-1])

# Example usage
input_string = "hello"
reversed_string = reverse_string(input_string)
print(f"Original string: {input_string}")
print(f"Reversed string: {reversed_string}")
