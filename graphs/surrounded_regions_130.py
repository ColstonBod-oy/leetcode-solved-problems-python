class Solution(object):
  def solve(self, board):
    rows, cols = len(board), len(board[0])

    def dfs(sr, sc):
      if 0 <= sr < rows and 0 <= sc < cols and board[sr][sc] == 'O':
        board[sr][sc] = 'T'
        dfs(sr + 1, sc)
        dfs(sr - 1, sc)
        dfs(sr, sc + 1)
        dfs(sr, sc - 1)

    for i in range(cols):
      dfs(0, i)
      dfs(rows - 1, i)

    for i in range(1, rows - 1):
      dfs(i, 0)
      dfs(i, cols - 1)

    for i in range(rows):
      for j in range(cols):
        if board[i][j] == 'O':
          board[i][j] = 'X'
        elif board[i][j] == 'T':
          board[i][j] = 'O'