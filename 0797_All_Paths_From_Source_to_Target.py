class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        path = []
        
        path.append(0)
        self.recurse(graph, 0, path, result)
        path.pop()
        
        return result
    
    
    def recurse(self,
        graph: List[List[int]],
        index: 0,
        path: List[int],
        result: List[List[int]],
    ) -> None:
        if index == len(graph) - 1:
            result.append(path.copy())
            
        neighbors = graph[index]
        
        for n in neighbors:
            path.append(n)
            self.recurse(graph, n, path, result)
            path.pop()
