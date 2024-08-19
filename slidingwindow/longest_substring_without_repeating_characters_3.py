class Solution(object):
  def lengthOfLongestSubstring(self, s):
    mySet = set()
    res = 0
    lPtr = 0
    for rPtr in range(len(s)):
      while s[rPtr] in mySet:
        mySet.remove(s[lPtr])
        lPtr += 1

      mySet.add(s[rPtr])
      res = max(res, rPtr - lPtr + 1)
    return res
        
        