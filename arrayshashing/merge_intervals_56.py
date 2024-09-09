class Solution(object):
  def merge(self, intervals):
    intervals.sort(key=lambda i: i[0])
    res = [intervals[0]]

    for start, end in intervals[1:]:
      prev_end = res[-1][1]

      if start <= prev_end: 
        end = max(end, prev_end)
        res[-1][1] = end
      else:
        res.append([start, end])
    return res