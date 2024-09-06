class Solution(object):
  def numIslands(self, grid):
    if not grid or not grid[0]:
      return 0

    rows, cols = len(grid), len(grid[0])
    num_islands = 0

    def dfs(sr, sc):
      if 0 <= sr < rows and 0 <= sc < cols and grid[sr][sc] == '1':
        grid[sr][sc] = '0'

        dfs(sr + 1, sc)
        dfs(sr - 1, sc)
        dfs(sr, sc + 1)
        dfs(sr, sc - 1)

    for i in range(rows):
      for j in range(cols):
        if grid[i][j] == '1':
          dfs(i, j)
          num_islands += 1
          
    return num_islands