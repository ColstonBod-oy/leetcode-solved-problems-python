class Solution(object):
  def twoSum(self, nums, target):
    my_map = {}
    for i, num in enumerate(nums):
      find_val = target - num
      if (find_val in my_map):
        return [my_map[find_val], i]
      else:
        my_map[num] = i