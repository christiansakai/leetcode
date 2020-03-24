class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeters = 0
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    perimeters += self.count_perimeters(grid, r, c)
                    
        return perimeters
    
    
    def count_perimeters(self, grid: List[List[int]], r: int, c: int) -> int:
        perimeters = 0
        
        # top perimeter
        if r - 1 < 0 or grid[r - 1][c] == 0:
            perimeters += 1
            
        # right perimeter
        if c + 1 == len(grid[0]) or grid[r][c + 1] == 0:
            perimeters += 1
            
        # bottom perimeter
        if r + 1 == len(grid) or grid[r + 1][c] == 0:
            perimeters += 1
        
        # left perimeter
        if c - 1 < 0 or grid[r][c - 1] == 0:
            perimeters += 1
            
        return perimeters
