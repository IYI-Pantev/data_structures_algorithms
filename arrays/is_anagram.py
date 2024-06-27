class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            return True
        return False
sol = Solution()
print(sol.isAnagram("racecar", "carrace"))

print(sorted("hello"))