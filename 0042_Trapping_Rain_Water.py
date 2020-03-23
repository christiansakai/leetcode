class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 2:
            return 0
        
        left_max = [0 for _ in height]
        left_max[0] = height[0]
        for i in range(1, len(height)):
            left_max[i] = max(left_max[i - 1], height[i])
            
        right_max = [0 for _ in height]
        right_max[len(right_max) - 1] = height[len(height) - 1]
        for i in range(len(height) - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])
            
        total = 0
        for i in range(len(height)):
            total += min(left_max[i], right_max[i]) - height[i]
            
        return total
