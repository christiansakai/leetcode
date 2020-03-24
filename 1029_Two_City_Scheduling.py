class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        cost_diff = []
        for c in costs:
            cost_diff.append((c[0] - c[1], c[0], c[1]))
            
        # sort by diff     
        cost_diff.sort(key=lambda c: c[0])    
        
        total = 0
        
        # first N people to city A
        for i in range(int(len(costs) / 2)):
            total += cost_diff[i][1] # to city A
            
        # next N people to city B
        for i in range(int(len(costs) / 2), len(costs)):
            total += cost_diff[i][2] # to city B
        
        return total
