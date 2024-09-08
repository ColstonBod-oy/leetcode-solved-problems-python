class Solution(object):
  def maxCoins(self, nums):
    nums = [1] + nums + [1]
    dp = {}

    def dfs(l_ptr, r_ptr):
      if l_ptr > r_ptr:
        return 0

      if (l_ptr, r_ptr) in dp:
        return dp[(l_ptr, r_ptr)]

      for i in range(l_ptr, r_ptr + 1):
        coins = nums[l_ptr - 1] * nums[i] * nums[r_ptr + 1]
        coins += dfs(l_ptr, i - 1) + dfs(i + 1, r_ptr)
        dp[(l_ptr, r_ptr)] = max(dp.get((l_ptr, r_ptr), 0), coins)
      return dp[(l_ptr, r_ptr)]
    return dfs(1, len(nums) - 2)