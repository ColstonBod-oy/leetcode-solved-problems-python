class NumArray(object):
    def __init__(self, nums):
        self.prefix_sum = []
        cur = 0
        for n in nums:
            cur += n
            self.prefix_sum.append(cur)
            
    def sumRange(self, left, right):
        if left == 0:
            return self.prefix_sum[right]
        return self.prefix_sum[right] - self.prefix_sum[left - 1]