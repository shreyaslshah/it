class Solve:
    arr = []
    target = 0

    def __init__(self, arr, target):
        self.arr = arr
        self.target = target

    def sol(self):
        for i in range(len(self.arr) - 1):
            j = i+1
            while (j<len(self.arr)):
                if(self.arr[i] + self.arr[j] == self.target):
                    return (i,j)
                j+=1
        return 'No solution exists'

n = int(input('enter number of elements\n'))
arr = []
for i in range(n):
    arr.append(int(input()))
target = int(input('enter target'))

s = Solve(arr, target)
print(s.sol())