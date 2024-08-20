class Solution(object):
  def dailyTemperatures(self, temperatures):
    myStack = []
    res = [0] * len(temperatures)
    for i, t in enumerate(temperatures):
      while myStack and t > temperatures[myStack[-1]]:
        prevI = myStack.pop()
        res[prevI] = i - prevI
      myStack.append(i)
    return res