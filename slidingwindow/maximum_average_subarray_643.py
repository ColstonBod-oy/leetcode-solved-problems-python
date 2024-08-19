class Solution(object):
  def findMaxAverage(self, nums, k):
    maxSum = sum(nums[:k])
    curSum = maxSum
    for i in range(len(nums) - k):
      curSum = (curSum - nums[i] + nums[i + k])
      maxSum = max(maxSum, curSum)
    return float(maxSum) / k
      
    