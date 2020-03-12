class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []
        self.queue_temp = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        while len(self.queue) > 1:
            temp = self.queue.pop(0)
            self.queue_temp.append(temp)

        val = self.queue.pop(0)

        while len(self.queue_temp) > 0:
            temp = self.queue_temp.pop(0)
            self.queue.append(temp)

        return val

    def top(self) -> int:
        """
        Get the top element.
        """
        while len(self.queue) > 1:
            temp = self.queue.pop(0)
            self.queue_temp.append(temp)

        val = self.queue[0]
        temp = self.queue.pop(0)
        self.queue_temp.append(temp)

        while len(self.queue_temp) > 0:
            temp = self.queue_temp.pop(0)
            self.queue.append(temp)

        return val

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.queue) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
