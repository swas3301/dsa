class Solution(object):
    def asteroidCollision(self, asteroids):
        asta = []
        for i in asteroids:
            while asta and i < 0 and asta[-1] > 0:
                if abs(asta[-1]) < abs(i):
                    asta.pop()
                    continue
                elif abs(asta[-1]) == abs(i):
                    asta.pop()
                break
            else:
                asta.append(i) 


        return asta
