class NumArray(object):
    def __init__(self, nums):
        self.prefixSum = []
        cur = 0
        for n in nums:
            cur += n
            self.prefixSum.append(cur)
            
    def sumRange(self, left, right):
        if left == 0:
            return self.prefixSum[right]
        return self.prefixSum[right] - self.prefixSum[left - 1]