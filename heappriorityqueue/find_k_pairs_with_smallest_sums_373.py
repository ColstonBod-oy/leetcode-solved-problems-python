import heapq

class Solution(object):
  def kSmallestPairs(self, nums1, nums2, k):
    pq = []
    res = []
    visited = set()

    heapq.heappush(pq, (nums1[0] + nums2[0], 0, 0))
    visited.add((0, 0))

    while pq and len(res) < k:
      _, i, j = heapq.heappop(pq)
      nextI, nextJ = i + 1, j + 1
      res.append([nums1[i], nums2[j]])

      if nextI < len(nums1) and (nextI, j) not in visited:
        heapq.heappush(pq, (nums1[nextI] + nums2[j], nextI, j))
        visited.add((nextI, j))

      if nextJ < len(nums2) and (i, nextJ) not in visited:
        heapq.heappush(pq, (nums1[i] + nums2[nextJ], i, nextJ))
        visited.add((i, nextJ))

    return res