class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        running_total = 0
        for x in nums:
            running_total += x
            self.prefix.append(running_total)

    def sumRange(self, left: int, right: int) -> int:
        right_val = self.prefix[right]
        left_val = self.prefix[left - 1] if left > 0 else 0
        return right_val - left_val
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)