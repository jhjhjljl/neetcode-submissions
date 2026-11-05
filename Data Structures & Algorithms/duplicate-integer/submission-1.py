"""
seen = {1, 2, 3}

[1, 2, 3, 3]
          i
"""
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for x in nums:
            if x in seen:
                return True
            seen.add(x)
        return False
        