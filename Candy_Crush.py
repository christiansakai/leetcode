from typing import List, Tuple

class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        while self.crush(board):
            self.drop(board)

        return board


    def crush(self, board: List[List[int]]) -> bool:
        crushed = False

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] != 0:
                    crushed_count = self.bfs(board, r, c)
                    if crushed_count > 1:
                        crushed = True

        return crushed


    def bfs(
        self,
        board: List[List[int]],
        row: int,
        col: int,
    ) -> int:
        crushed = 0
        queue = [(row, col)]

        while len(queue) > 0:
            qlen = len(queue)

            for _ in range(0, qlen):
                coord = queue.pop(0)

                curr_val = board[coord[0]][coord[1]] # save curr val
                board[coord[0]][coord[1]] = 0 # crush

                # only count if there are neighbors that will be crushed
                neighbors = self.get_neighbors(board, coord[0], coord[1], curr_val)
                crushed += len(neighbors)

                for n in neighbors:
                    queue.append(n)

        if crushed == 0:
            return 0

        return crushed + 1 # add the original cell as count


    def get_neighbors(
        self,
        board: List[List[int]],
        row: int,
        col: int,
        target: int,
    ) -> List[Tuple[int, int]]:
        neighbors = []

        # top
        if row - 1 >= 0 and board[row - 1][col] == target:
            neighbors.append((row - 1, col))

        # right
        if col + 1 < len(board[0]) and board[row][col + 1] == target:
            neighbors.append((row, col + 1))

        # bot
        if row + 1 < len(board) and board[row + 1][col] == target:
            neighbors.append((row + 1, col))

        # left
        if col - 1 >= 0 and board[row][col - 1] == target:
            neighbors.append((row, col - 1))

        return neighbors


    def drop(self, board: List[List[int]]) -> None:
        for c in range(len(board[0])):
            last_non_zero_idx = len(board)

            for r in range(len(board) - 1, -1, 1):
                if board[r][c] != 0:
                    last_non_zero_idx -= 1

                    temp = board[r][c]
                    board[r][c] = board[last_non_zero_idx][c]
                    board[last_non_zero_idx][c] = temp


def print_board(board):
    for row in board:
        print(row)


board = [
    [110,5,112,113,114],
    [210,211,5,213,214],
    [310,311,3,313,314],
    [410,411,412,5,414],
    [5,1,512,3,3],
    [610,4,1,613,614],
    [710,1,2,713,714],
    [810,1,2,1,1],
    [1,1,2,2,2],
    [4,1,4,4,1014]
]

s = Solution()

s.crush(board)
print_board(board)
