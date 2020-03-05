class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []

        for i in range(0, numRows):
            if i == 0:
                result.append([1])
            else:
                prev_row = result[i - 1]

                new_row = [1]

                for j in range(1, len(prev_row)):
                    new_row.append(prev_row[j] + prev_row[j - 1])

                new_row.append(1)
                result.append(new_row)

        return result
