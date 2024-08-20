class Solution(object):
  def searchMatrix(self, matrix, target):
    row, col = len(matrix) - 1, 0

    while row >= 0 and col < len(matrix[0]):
      if matrix[row][col] == target:
        return True

      if matrix[row][col] > target:
        row -= 1
      else:
        col += 1
    return False