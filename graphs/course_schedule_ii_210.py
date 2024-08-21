class Solution(object):
  def findOrder(self, numCourses, prerequisites):
    res = []
    adj_list = { i: [] for i in range(numCourses) }
    for course, prereq in prerequisites:
      adj_list[course].append(prereq)

    visited, start_cycle = set(), set()
    def dfs(node):
      if node in start_cycle:
        return False
      if node in visited:
        return True

      start_cycle.add(node)
      for prereq in adj_list[node]:
        if dfs(prereq) == False:
          return False

      start_cycle.remove(node)
      visited.add(node)
      res.append(node)
      return True

    for node in range(numCourses):
      if dfs(node) == False:
        return []
    return res