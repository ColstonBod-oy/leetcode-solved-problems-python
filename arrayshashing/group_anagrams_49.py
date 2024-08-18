from collections import defaultdict

class Solution(object):
  def groupAnagrams(self, strs):
    if len(strs) == 0:
      return [""]

    if len(strs) == 1:
      return [strs]
  
    myMap = defaultdict(list)
    for str in strs:
      counter = [0] * 26
      for c in str:
        counter[ord(c) - ord("a")] += 1
      myMap[tuple(counter)].append(str)
    return myMap.values()