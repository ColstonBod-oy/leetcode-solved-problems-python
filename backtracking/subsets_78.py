class Solution(object):
  def subsets(self, nums):
    res = []
    sub = []

    def dfs(i):
      if i >= len(nums):
        res.append(sub[:])
        return
      sub.append(nums[i])
      dfs(i + 1)
      sub.pop()
      dfs(i + 1)
    dfs(0)
    return res