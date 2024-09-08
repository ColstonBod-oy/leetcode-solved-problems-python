class Solution(object):
  def climbStairs(self, n):
    val_1, val_2 = 1, 1
    for _ in range(n - 1):
      val_1, val_2 = val_1 + val_2, val_1
    return val_1