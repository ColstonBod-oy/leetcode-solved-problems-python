class Solution(object):
  def isAnagram(self, s, t):
    sMap, tMap = {}, {}

    if (len(s) != len(t)):
      return False
      
    for sChar, tChar in zip(s, t):
      if sChar in sMap:
        sMap[sChar] += 1
      else:
        sMap[sChar] = 1
        
      if tChar in tMap:
        tMap[tChar] += 1
      else:
        tMap[tChar] = 1

    return sMap == tMap