class Solution(object):
  def twoSum(self, nums, target):
    myMap = {}
    for i, num in enumerate(nums):
      findVal = target - num
      if (findVal in myMap):
        return [myMap[findVal], i]
      else:
        myMap[num] = i