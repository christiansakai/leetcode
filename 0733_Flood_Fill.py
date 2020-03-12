class Solution:
    def floodFill(
            self,
            image: List[List[int]],
            sr: int,
            sc: int,
            newColor: int,
    ) -> List[List[int]]:
        if len(image) == 0:
            return image

        visited = [[False for x in image[0]] for y in image]
        self.traverse(image, sr, sc, newColor, visited)
        return image

    def traverse(
            self,
            image: List[List[int]],
            sr: int,
            sc: int,
            newColor: int,
            visited: List[List[bool]],
    ) -> None:
        if visited[sr][sc]:
            return

        visited[sr][sc] = True
        temp_color = image[sr][sc]
        image[sr][sc] = newColor

        neighbors = self.get_neighbors(image, sr, sc, temp_color)

        for n in neighbors:
            if not visited[n[0]][n[1]]:
                self.traverse(image, n[0], n[1], newColor, visited)

    def get_neighbors(
            self,
            image: List[List[int]],
            sr: int,
            sc: int,
            prev_color: int,
    ) -> List[List[int]]:
        neighbors = []

        # top
        if sr - 1 >= 0 and image[sr - 1][sc] == prev_color:
            neighbors.append([sr - 1, sc])

        # right
        if sc + 1 < len(image[0]) and image[sr][sc + 1] == prev_color:
            neighbors.append([sr, sc + 1])

        # bottom
        if sr + 1 < len(image) and image[sr + 1][sc] == prev_color:
            neighbors.append([sr + 1, sc])

        # left
        if sc - 1 >= 0 and image[sr][sc - 1] == prev_color:
            neighbors.append([sr, sc - 1])

        return neighbors
