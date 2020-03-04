class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[0 for x in range(m)] for y in range(n)]

        for r in range(0, n):
            matrix[r][0] = 1

        for c in range(0, m):
            matrix[0][c] = 1

        for r in range(1, n):
            for c in range(1, m):
                matrix[r][c] = matrix[r - 1][c] + matrix[r][c - 1]

        return matrix[n - 1][m - 1]
