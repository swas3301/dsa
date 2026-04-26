class MyStack(object):

    def __init__(self):
        self.q1 = deque()

    def push(self, x):
        self.q1.append(x)

    def pop(self):
        for i in range(len(self.q1)-1):
            self.q1.append(self.q1.popleft())
        return self.q1.popleft()
        
    def top(self):
        return self.q1[-1]

    def empty(self):
        return len(self.q1)==0
