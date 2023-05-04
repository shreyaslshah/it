class Solve:
    arr = []

    def __init__(self, arr):
        self.arr = arr

    def subSets(self):
        return self.getSubsets([], sorted(self.arr))

    def getSubsets(self, curr, set):
        if set:
            return self.getSubsets(curr, set[1:]) + self.getSubsets(curr + [set[0]], set[1:])
        return [curr]

n = int(input('enter number of elements\n'))
arr = []
for i in range(n):
    arr.append(int(input()))

s = Solve(arr)
print(s.subSets())