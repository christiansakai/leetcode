class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.queue = []
        self.total = 0
        self.size = size

    def next(self, val: int) -> float:
        if len(self.queue) < self.size:
            self.queue.append(val)
            self.total += val
            return self.total / len(self.queue)

        discard = self.queue.pop(0)
        self.total -= discard

        self.queue.append(val)
        self.total += val
        return self.total / self.size


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
