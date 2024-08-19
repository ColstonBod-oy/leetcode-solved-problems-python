class Solution(object):
  def maxArea(self, height):
    res = 0
    lPtr, rPtr = 0, len(height) - 1
    while lPtr < rPtr:
      curArea = (rPtr - lPtr) * min(height[lPtr], height[rPtr])
      res = max(res, curArea)

      if height[lPtr] < height[rPtr]:
        lPtr += 1
      else:
        rPtr -= 1

    return res
      