def isPalindrome(s):
    data_list = [w.lower() for w in s if w.isalnum()]
    if data_list == data_list[::-1]:
        return True
    return False

text = "Was it a car or a cat I saw?"
print(isPalindrome(text))