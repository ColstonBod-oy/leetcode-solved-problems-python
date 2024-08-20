class Solution(object):
  def nextGreaterElement(self, nums1, nums2):
    myMap = { n:i for i, n in enumerate(nums1) }
    myStack = []
    res = [-1] * len(nums1)

    for n in nums2:
      while myStack and n > myStack[-1]:
        res[myMap[myStack.pop()]] = n
      if n in myMap:
        myStack.append(n)
    return res