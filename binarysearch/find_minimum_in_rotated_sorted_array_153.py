class Solution(object):
  def findMin(self, nums):
    res = nums[0]
    l_ptr, r_ptr = 0, len(nums) - 1
    while l_ptr <= r_ptr:
      if nums[l_ptr] < nums[r_ptr]:
        res = min(res, nums[l_ptr])
        break

      mid = (l_ptr + r_ptr) // 2 
      res = min(res, nums[mid])

      if nums[l_ptr] <= nums[mid]:
        l_ptr = mid + 1
      else:
        r_ptr = mid - 1
    return res