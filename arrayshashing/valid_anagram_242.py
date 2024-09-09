class Solution(object):
  def isAnagram(self, s, t):
    s_map, t_map = {}, {}

    if (len(s) != len(t)):
      return False
      
    for s_char, t_char in zip(s, t):
      if s_char in s_map:
        s_map[s_char] += 1
      else:
        s_map[s_char] = 1
        
      if t_char in t_map:
        t_map[t_char] += 1
      else:
        t_map[t_char] = 1

    return s_map == t_map