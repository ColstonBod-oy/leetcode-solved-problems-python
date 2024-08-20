import heapq

class Solution(object):
  def findKthLargest(self, nums, k):
    pq = nums[:k]
    heapq.heapify(pq)
    for n in nums[k:]:
      if n > pq[0]:
        heapq.heappop(pq)
        heapq.heappush(pq, n)
    return pq[0]