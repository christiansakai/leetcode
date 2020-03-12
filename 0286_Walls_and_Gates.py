class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        queue = []

        # Start BFS from gate at the same time, this is key for optimization
        for row in range(0, len(rooms)):
            for col in range(0, len(rooms[0])):
                if rooms[row][col] == 0:
                    queue.append([row, col])

        visited = [[False for x in rooms[0]] for y in rooms]
        distance = -1

        while len(queue) > 0:
            distance += 1
            qlen = len(queue)

            for i in range(0, qlen):
                coord = queue.pop(0)
                row, col = coord[0], coord[1]

                if visited[row][col]:
                    continue

                visited[row][col] = True
                rooms[row][col] = distance

                neighbors = self.get_neighbors(rooms, row, col)
                for n in neighbors:
                    queue.append(n)

    def get_neighbors(self,
                      rooms: List[List[int]],
                      row: int,
                      col: int) -> List[List[int]]:
        neighbors = []

        # top
        if row - 1 >= 0 and self.valid_neighbor(rooms, row - 1, col):
            neighbors.append([row - 1, col])

        # right
        if col + \
                1 < len(rooms[0]) and self.valid_neighbor(rooms, row, col + 1):
            neighbors.append([row, col + 1])

        # bottom
        if row + 1 < len(rooms) and self.valid_neighbor(rooms, row + 1, col):
            neighbors.append([row + 1, col])

        # left
        if col - 1 >= 0 and self.valid_neighbor(rooms, row, col - 1):
            neighbors.append([row, col - 1])

        return neighbors

    def valid_neighbor(self,
                       rooms: List[List[int]],
                       row: int,
                       col: int) -> bool:
        return not(rooms[row][col] == 0 or rooms[row][col] == -1)
