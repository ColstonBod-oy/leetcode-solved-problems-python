class Solution(object):
  def floodFill(self, image, sr, sc, color):
    rows, cols = len(image), len(image[0])
    sp = image[sr][sc]

    def dfs(sr, sc):
      if 0 <= sr < rows and 0 <= sc < cols and image[sr][sc] == sp and image[sr][sc] != color:
        image[sr][sc] = color

        dfs(sr + 1, sc)
        dfs(sr - 1, sc)
        dfs(sr, sc + 1)
        dfs(sr, sc - 1)

    dfs(sr, sc)
    return image