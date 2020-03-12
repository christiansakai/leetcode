from typing import Dict


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = {}
        steps = -1
        queue = ['0000']

        while len(queue) > 0:
            steps += 1
            qlen = len(queue)

            for i in range(0, qlen):
                curr = queue.pop(0)
                if curr in visited or curr in deadends:
                    continue

                visited[curr] = True

                if curr == target:
                    return steps

                next_combinations = self.get_next_combinations(curr)
                for c in next_combinations:
                    queue.append(c)

        return -1

    def get_next_combinations(self, curr: str) -> List[str]:
        curr_list = list(curr)
        combinations = []
        for i in range(0, len(curr_list)):
            # prev
            prev_ch = self.get_prev_ch(curr_list[i])
            new_combo = curr_list[:i] + [prev_ch] + curr_list[i + 1:]
            combinations.append("".join(new_combo))

            # next
            next_ch = self.get_next_ch(curr_list[i])
            new_combo = curr_list[:i] + [next_ch] + curr_list[i + 1:]
            combinations.append("".join(new_combo))

        return combinations

    def get_prev_ch(self, ch: str) -> str:
        if ch == '0':
            return '9'

        return str(int(ch) - 1)

    def get_next_ch(self, ch: str) -> str:
        if ch == '9':
            return '0'

        return str(int(ch) + 1)
