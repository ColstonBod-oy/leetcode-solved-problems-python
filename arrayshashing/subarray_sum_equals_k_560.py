class Solution(object):
  def subarraySum(self, nums, k):
    my_map = { 0: 1 }
    cur_sum, res = 0, 0
    for n in nums:
      cur_sum += n
      res += my_map.get(cur_sum - k, 0)
      my_map[cur_sum] = 1 + my_map.get(cur_sum, 0)
    return res
      