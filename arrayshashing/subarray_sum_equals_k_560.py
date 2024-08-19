class Solution(object):
  def subarraySum(self, nums, k):
    myMap = { 0: 1 }
    curSum, res = 0, 0
    for n in nums:
      curSum += n
      res += myMap.get(curSum - k, 0)
      myMap[curSum] = 1 + myMap.get(curSum, 0)
    return res
      