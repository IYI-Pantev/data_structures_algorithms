class Solution:
    def hasDuplicate(self, nums) -> bool:

        my_dict = {}
        for num in nums:
           my_dict[num] = my_dict.get(num, 0) + 1
           if my_dict[num] > 1:
               return True
        return False
        
        # for num in nums:
        #     if my_dict[num] > 1:
        #         return True
        # return False
    
sol = Solution()
nums=[1,2,3,3]
print(sol.hasDuplicate(nums))