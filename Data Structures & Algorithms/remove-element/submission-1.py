class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # res = []
        # for x in nums:
        #     if x == val:
        #         continue
        #     res.append(x)
        # return res

        prefix = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[prefix] = nums[i]
                prefix += 1
        return prefix

            
            
            
        

