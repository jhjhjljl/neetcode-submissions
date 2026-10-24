"""
i use hashset as my solution.
storing unique integer in the set, then check if the integer is displayed more than once.
time complexity is o(n).
space complexity is also o(n).
"""


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = set()
        for x in nums:
            if x in unique:
                return True
            unique.add(x)
        return False
        
        