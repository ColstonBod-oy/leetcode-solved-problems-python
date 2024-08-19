class Solution(object):
  def twoSum(self, numbers, target):
    lPtr, rPtr = 0, len(numbers) - 1
    while lPtr < rPtr:
      if numbers[lPtr] + numbers[rPtr] == target:
        return [lPtr + 1, rPtr + 1]
      elif numbers[lPtr] + numbers[rPtr] < target:
        lPtr += 1
      else:
        rPtr -= 1