from collections import deque

class Solution(object):
  def orangesRotting(self, grid):
    rotten_oranges = deque()
    fresh_oranges = 0
    time = 0
    adj_indexes = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for i in range(len(grid)):
      for j in range(len(grid[0])):
        if grid[i][j] == 1:
          fresh_oranges += 1
        if grid[i][j] == 2:
          rotten_oranges.append((i, j))

    while rotten_oranges and fresh_oranges > 0:
      for _ in range(len(rotten_oranges)):
        row, col = rotten_oranges.popleft()
        for i, j in adj_indexes:
          adj_row, adj_col = row + i, col + j
          if (0 <= adj_row < len(grid) 
              and 0 <= adj_col < len(grid[0]) 
              and grid[adj_row][adj_col] == 1):
            grid[adj_row][adj_col] = 2
            rotten_oranges.append((adj_row, adj_col))
            fresh_oranges -= 1
      time += 1
    return time if fresh_oranges == 0 else -1

    