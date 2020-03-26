from typing import List, Tuple

class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        while self.crush(board):
            self.drop(board)

        return board


    def crush(self, board: List[List[int]]) -> bool:
        crush_mark = [[False for _ in board[0]] for _ in board]
        crushed = False

        # horizontal mark
        for r in range(len(board)):
            for c in range(len(board[0]) - 3):
                if board[r][c] == board[r][c + 1] and \
                        board[r][c + 1] == board[r][c + 2] and\
                            board[r][c + 2] != 0:
                    crush_mark[r][c] = True

        # vertical mark
        for r in range(len(board) - 3):
            for c in range(len(board[0])):
                if board[r][c] == board[r + 1][c] and \
                        board[r + 1] == board[r + 2][c] and \
                            board[r + 2][c] != 0:
                    crush_mark[r][c] = True

        print_board(crush_mark)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if crush_mark[r][c]:
                    board[r][c] = 0
                    crushed = True

        return crushed


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
    [110,5,  112,113,114],
    [210,211,5,  213,214],
    [310,311,3,  313,314],
    [410,411,412,5,  414],
    [5,  1,  512,3,  3],
    [610,4,  1,  613,614],
    [710,1,  2,  713,714],
    [810,1,  2,  1,  1],
    [1,  1,  2,  2,  2],
    [4,  1,  4,  4,  1014]
]

s = Solution()

s.crush(board)
# print_board(board)
