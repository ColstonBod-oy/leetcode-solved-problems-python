class Solution(object):
  def canPartition(self, nums):
    if sum(nums) % 2 != 0:
      return False

    target = sum(nums) // 2
    dp = {0}

    for num in nums:
      new_dp = set(dp)
      for sum_nums in dp:
        if sum_nums + num == target:
          return True
        new_dp.add(sum_nums + num)
      dp = new_dp
    return target in dp
    