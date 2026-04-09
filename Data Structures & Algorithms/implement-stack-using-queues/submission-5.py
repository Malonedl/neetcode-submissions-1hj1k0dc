class MyStack:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        # add x to the queue
        self.queue.append(x)

        # shift size - 1 elements to the back of the queue to put x in front 
        for i in range(len(self.queue) -1):
            self.queue.append(self.queue[-1])
            self.queue.pop()


    def pop(self) -> int:
        val = self.queue[-1]
        self.queue.pop()
        return val

    def top(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        if len(self.queue) > 0:
            return False
        else:
            return True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()