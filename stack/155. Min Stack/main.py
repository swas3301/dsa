class MinStack(object):

    def __init__(self):
        self.s1 = []
        self.min = []

    def push(self, val):
        self.s1.append(val)
        val = min(val, self.min[-1] if self.min else val)
        self.min.append(val)

    def pop(self):
        self.s1.pop()
        self.min.pop()

    def top(self):
        return self.s1[-1]

    def getMin(self):
        return self.min[-1]
