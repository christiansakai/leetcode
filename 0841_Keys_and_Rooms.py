class Solution:
    visit_count = 0
    visited = []
    rooms = []

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        self.visited = [False for x in rooms]
        self.rooms = rooms

        self.traverse(0)

        return self.visit_count == len(rooms)

    def traverse(self, num: int) -> None:
        if self.visited[num]:
            return

        self.visited[num] = True
        self.visit_count += 1

        accessable_rooms = self.rooms[num]

        for r in accessable_rooms:
            if not self.visited[r]:
                self.traverse(r)
