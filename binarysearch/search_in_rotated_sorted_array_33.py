class Solution(object):
  def search(self, nums, target):
    l_ptr = 0
    r_ptr = len(nums) - 1
    while l_ptr <= r_ptr:
      mid = (l_ptr + r_ptr) // 2

      if nums[mid] == target:
        return mid

      if nums[l_ptr] <= nums[mid]:
        if nums[l_ptr] <= target < nums[mid]:
          r_ptr = mid - 1
        else:
          l_ptr = mid + 1
      else:
        if nums[mid] < target <= nums[r_ptr]:
          l_ptr = mid + 1
        else:
          r_ptr = mid - 1
    return -1
      
    