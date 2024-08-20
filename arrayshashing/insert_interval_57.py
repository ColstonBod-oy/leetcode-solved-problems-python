class Solution(object):
  def insert(self, intervals, newInterval):
    res = []
    for i, (start, end) in enumerate(intervals):
      if newInterval[1] < start:
        res.append(newInterval)
        return res + intervals[i:]
      elif newInterval[0] > end:
        res.append(intervals[i])
      else:
        newInterval = [min(newInterval[0], start), max(newInterval[1], end)]
    res.append(newInterval)
    return res