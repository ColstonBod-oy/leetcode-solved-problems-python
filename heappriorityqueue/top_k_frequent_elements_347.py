import heapq

class Solution(object):
  def topKFrequent(self, nums, k):
    count = {}
    for n in nums:
      count[n] = count.get(n, 0) + 1

    pq = []
    for n, c in count.items():
      if len(pq) < k:
        heapq.heappush(pq, (c, n))
      elif c > pq[0][0]:
          heapq.heappushpop(pq, (c, n))

    return [heapq.heappop(pq)[1] for _ in range(k)]
      