class Solution(object):
  def minWindow(self, s, t):
    mapS, mapT = {}, {}
    minWin = float("inf")
    res = ""
    
    for c in t:
      mapT[c] = mapT.get(c, 0) + 1

    have, need = 0, len(mapT)
    lPtr = 0
    for rPtr, c in enumerate(s):
      mapS[c] = mapS.get(c, 0) + 1
      if c in mapT and mapS[c] == mapT[c]:
        have += 1
      while need == have:
        if minWin > rPtr - lPtr + 1:
          minWin = rPtr - lPtr + 1
          res = s[lPtr:rPtr + 1]
        mapS[s[lPtr]] -= 1
        if s[lPtr] in mapT and mapS[s[lPtr]] < mapT[s[lPtr]]:
          have -= 1
        lPtr += 1
    return res
        