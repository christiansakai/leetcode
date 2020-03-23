from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) <= 1:
            return len(intervals)

        intervals.sort(key=lambda interval: interval[0])

        rooms = []

        for interval in intervals:
            has_room = False

            for i in range(len(rooms)):
                last_meeting_in_room = rooms[i][len(rooms[i]) - 1]

                if not self.is_overlap(last_meeting_in_room, interval):
                    rooms[i].append(interval)
                    has_room = True
                    break

            if not has_room:
                rooms.append([interval])

        return len(rooms)


    def is_overlap(self, room: List[int], interval: List[int]) -> bool:
        max_left = max(room[0], interval[0])
        min_right = min(room[1], interval[1])

        return (min_right - max_left) > 0
