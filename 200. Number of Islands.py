class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range (rows)]
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]] #left, down, right, up

        count = 0

        def inArea(row, col):
            return (0<= row < rows) and (0<= col < cols)

        def dfs(row, col):
            visited[row][col] = True
            for d in direction:
                next_row = row + d[0]
                next_col = col + d[1]
                if inArea(next_row, next_col):
                    if grid[next_row][next_col] == '1' and (not visited[next_row][next_col]):
                        dfs(next_row, next_col)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1' and (not visited[row][col]):
                    dfs(row, col)
                    count += 1
        return count
