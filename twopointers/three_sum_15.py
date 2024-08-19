class Solution(object):
  def threeSum(self, nums):
    res = []
    nums.sort()

    for i, n in enumerate(nums):
      if i > 0 and n == nums[i - 1]:
        continue

      lPtr, rPtr = i + 1, len(nums) - 1
      while lPtr < rPtr:
        curSum = n + nums[lPtr] + nums[rPtr]
        if curSum < 0:
          lPtr += 1
        elif curSum > 0:
          rPtr -= 1
        else:
          res.append([n, nums[lPtr], nums[rPtr]])
          lPtr += 1
          while nums[lPtr] == nums[lPtr - 1] and lPtr < rPtr:
            lPtr += 1

    return res
        