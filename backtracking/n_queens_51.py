class Solution(object):
  def solveNQueens(self, n):
    res = []
    cur_board = [["."] * n for _ in range(n)]
    capt_cols = set()
    capt_neg_diag = set()
    capt_pos_diag = set()

    def backtrack(r):
      if r == n:
        res.append(["".join(row) for row in cur_board])
        return

      for c in range(n):
        if (c not in capt_cols and 
            r - c not in capt_neg_diag and 
            r + c not in capt_pos_diag):
            capt_cols.add(c)
            capt_neg_diag.add(r - c)
            capt_pos_diag.add(r + c)
            cur_board[r][c] = "Q"
            backtrack(r + 1)
            capt_cols.remove(c)
            capt_neg_diag.remove(r - c)
            capt_pos_diag.remove(r + c)
            cur_board[r][c] = "."
    backtrack(0)
    return res