from typing import Tuple


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0

        for r in range(0, len(grid)):
            for c in range(0, len(grid[0])):
                if grid[r][c] == '1':
                    self.visit(grid, r, c)
                    islands += 1

        return islands

    def visit(self, grid: List[List[str]], row: int, col: int):
        grid[row][col] = '0'

        for n in self.get_neighbors(grid, row, col):
            next_row = n[0]
            next_col = n[1]

            if grid[next_row][next_col] == '1':
                self.visit(grid, next_row, next_col)

    def get_neighbors(
            self, grid: List[List[str]], row: int, col: int) -> List[Tuple[int, int]]:
        neighbors = []

        if row - 1 >= 0:
            neighbors.append((row - 1, col))

        if col + 1 < len(grid[0]):
            neighbors.append((row, col + 1))

        if row + 1 < len(grid):
            neighbors.append((row + 1, col))

        if col - 1 >= 0:
            neighbors.append((row, col - 1))

        return neighbors
