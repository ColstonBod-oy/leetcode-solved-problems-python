class Solution(object):
  def largestRectangleArea(self, heights):
    stack = []
    res = 0
    for i, h in enumerate(heights):
      startIndex = i
      while stack and h < stack[-1][1]:
        prevIndex, prevH = stack.pop()
        res = max(res, (i - prevIndex) * prevH)
        startIndex = prevIndex
      stack.append((startIndex, h))

    for i, h in stack:
      res = max(res, h * (len(heights) - i))
    return res
        