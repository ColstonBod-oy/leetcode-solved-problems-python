class Solution(object):
  def findMaxLength(self, nums):
    counter_0, counter_1, res = 0, 0, 0
    my_map = {}
    for i, n in enumerate(nums):
      if n == 0:
        counter_0 += 1
      else:
        counter_1 += 1

      if counter_1 - counter_0 not in my_map:
        my_map[counter_1 - counter_0] = i

      if counter_0 == counter_1:
        res = counter_0 + counter_1
      else:
        res = max(res, i - my_map[counter_1 - counter_0])
    return res