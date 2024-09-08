import copy

class Solution(object):
  def permute(self, nums):
    res = [[]]

    for num in nums:
      new_res = []
      for sub in res:
        for i in range(len(sub) + 1):
          sub_copy = copy.deepcopy(sub)
          sub_copy.insert(i, num)
          new_res.append(sub_copy)
      res = new_res
    return res
          
  
