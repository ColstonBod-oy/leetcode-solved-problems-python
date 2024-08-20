class Solution(object):
  def merge(self, intervals):
    intervals.sort(key=lambda i: i[0])
    res = [intervals[0]]

    for start, end in intervals[1:]:
      prevEnd = res[-1][1]

      if start <= prevEnd: 
        end = max(end, prevEnd)
        res[-1][1] = end
      else:
        res.append([start, end])
    return res