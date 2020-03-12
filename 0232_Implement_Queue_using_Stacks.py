class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.stack_temp = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        while len(self.stack) > 0:
            temp = self.stack.pop()
            self.stack_temp.append(temp)

        val = self.stack_temp.pop()

        while len(self.stack_temp) > 0:
            temp = self.stack_temp.pop()
            self.stack.append(temp)

        return val

    def peek(self) -> int:
        """
        Get the front element.
        """
        while len(self.stack) > 0:
            temp = self.stack.pop()
            self.stack_temp.append(temp)

        val = self.stack_temp[len(self.stack_temp) - 1]

        while len(self.stack_temp) > 0:
            temp = self.stack_temp.pop()
            self.stack.append(temp)

        return val

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
