from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals

        intervals.sort(key=lambda interval: interval[0])

        merged = [intervals[0]]

        for interval in intervals:
            last_merged = merged[len(merged) - 1]
            if self.overlap(last_merged, interval):
                last_merged = merged.pop()
                combined = self.combine(last_merged, interval)
                merged.append(combined)
            else:
                merged.append(interval)

        return merged


    def overlap(self, interval_a: List[int], interval_b) -> bool:
        max_left = max(interval_a[0], interval_b[0])
        min_right = min(interval_a[1], interval_b[1])

        return (min_right - max_left + 1) >= 1


    def combine(self, interval_a: List[int], interval_b) -> List[List[int]]:
        min_left = min(interval_a[0], interval_b[0])
        max_right = max(interval_a[1], interval_b[1])

        return [min_left, max_right]

