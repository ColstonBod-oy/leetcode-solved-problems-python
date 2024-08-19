class Solution(object):
  def isHappy(self, n):
    def get_next(val):
      return sum([int(num_str) ** 2 for num_str in str(val)])

    slow = n
    fast = get_next(n)
    while fast != 1 and slow != fast:
      slow = get_next(slow)
      fast = get_next(get_next(fast))
    return fast == 1