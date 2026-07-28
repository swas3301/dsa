class Solution(object):
    def nearestValidPoint(self, x, y, points):
        best = -1
        smallest = float("inf")
        for i, (a, b) in enumerate(points):
            if a == x or b == y:
                d = abs(a - x) + abs(b - y)
                if d < smallest:
                    smallest = d
                    best = i
        return best
