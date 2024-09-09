class Solution(object):
  def eraseOverlapIntervals(self, intervals):
    intervals.sort()
    res = 0
    prev_end = intervals[0][1]
    for start, end in intervals[1:]: 
      if start >= prev_end:
        prev_end = end
      else:
        res += 1
        prev_end = min(prev_end, end)
    return res