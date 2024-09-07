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

    for i in range(rows):
      for j in range(cols):
        if (board[i][j] == 'O' and
            (i in (0, rows - 1) or j in (0, cols - 1))):
            dfs(i, j)

    for i in range(rows):
      for j in range(cols):
        if board[i][j] == 'O':
          board[i][j] = 'X'
        elif board[i][j] == 'T':
          board[i][j] = 'O'