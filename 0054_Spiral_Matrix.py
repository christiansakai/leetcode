class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []

        result = []
        direction = 'right'
        i = 0
        steps = len(matrix) * len(matrix[0])

        top_row = 0
        bottom_row = len(matrix) - 1
        left_col = 0
        right_col = len(matrix[0]) - 1

        while i < steps:
            if direction == 'right':
                for col in range(left_col, right_col + 1):
                    result.append(matrix[top_row][col])
                    i += 1

                top_row += 1
                direction = 'bottom'

            elif direction == 'bottom':
                for row in range(top_row, bottom_row + 1):
                    result.append(matrix[row][right_col])
                    i += 1

                right_col -= 1
                direction = 'left'

            elif direction == 'left':
                for col in range(right_col, left_col - 1, -1):
                    result.append(matrix[bottom_row][col])
                    i += 1

                bottom_row -= 1
                direction = 'up'

            else:
                for row in range(bottom_row, top_row - 1, - 1):
                    result.append(matrix[row][left_col])
                    i += 1

                left_col += 1
                direction = 'right'

        return result
