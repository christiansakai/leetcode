from typing import List

class Solution:
    # Recursive
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        prev_row = self.getRow(rowIndex - 1)
        
        next_row = [1]
        
        for i in range(1, len(prev_row)):
            next_row.append(prev_row[i - 1] + prev_row[i])
            
        next_row.append(1)
        
        return next_row
