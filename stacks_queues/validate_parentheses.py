class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hash_map = {')': '(', ']': '[', '}': '{'}

        for c in s:
            if c not in hash_map:
                stack.append(c)
                continue
            if not stack or stack[-1] != hash_map[c]:
                return False
            stack.pop()
            
        return not stack
    
s = "([{}])"
s2 = "[(])"

sol = Solution()
print(sol.isValid("{}"))