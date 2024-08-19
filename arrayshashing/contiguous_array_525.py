class Solution(object):
  def findMaxLength(self, nums):
    counter0, counter1, res = 0, 0, 0
    myMap = {}
    for i, n in enumerate(nums):
      if n == 0:
        counter0 += 1
      else:
        counter1 += 1

      if counter1 - counter0 not in myMap:
        myMap[counter1 - counter0] = i

      if counter0 == counter1:
        res = counter0 + counter1
      else:
        res = max(res, i - myMap[counter1 - counter0])
    return res