class stack :
    stack = list()

    def __init__(self,stack) :
        self.stack = stack

    def push(self, value) :
        self.stack.append(value)

    def pop(self) :
        self.stack.pop()

class queue :
    queue = list()

    def __init__(self,queue) :
        self.queue = queue

    def push(self,value) :
        self.queue.append(value)

    def pop(self) :
        self.queue.pop(0)