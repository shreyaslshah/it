class Solver:
    x = 0
    n = 0
    def __init__(self, x, n):
        self.x = x
        self.n = n
    def solve(self):
        i = 1
        result = 1
        while(i<=self.n):
            result = result * self.x
            i+=1
        return result

x = int(input('Enter base: '))
n = int(input('Enter power: '))

s = Solver(x, n)

print(s.solve())