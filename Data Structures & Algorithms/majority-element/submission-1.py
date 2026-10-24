class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hm = dict()
        max_count = 0
        max_num = 0

        for x in nums:
            if x not in hm:
                hm[x] = 1
            else:
                hm[x] += 1
            if max_count < hm[x]:
                max_count = hm[x]
                max_num = x
        
        return max_num
        
        return max_num
        
