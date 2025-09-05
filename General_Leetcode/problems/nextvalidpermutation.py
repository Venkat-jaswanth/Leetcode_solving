class Solution:
    def nextValidPermutation(self, arr, value):
        while True:
            arr = self.nextPermutation(arr)
            if self.calculate_s(arr) == value:
                return arr

    def kthPermutation(self, arr, k):
        if self.noOfPermutations(arr) < k:
            print(-1)
        else:
            old_val = self.calculate_s(arr)
            for _ in range(k):
                self.nextValidPermutation(arr, old_val)
            print(' '.join(map(str, arr)))

    def noOfPermutations(self, arr):
        n = len(arr)
        return 1 << n - 1

    def calculate_s(self, p):
        n = len(p)
        total = 0
        for i in range(n):
            min_value = float('inf')
            for j in range(i, n):
                min_value = min(min_value, p[j])
                total += min_value
        return int(total)

    def nextPermutation(self, arr):
        n = len(arr)
        i = n - 2
        while i >= 0 and arr[i] >= arr[i + 1]:
            i -= 1
        if i >= 0:
            j = n - 1
            while arr[j] <= arr[i]:
                j -= 1
            arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1:] = reversed(arr[i + 1:])
        return arr


a = Solution()
b = 1
for _ in range(b):
    c, d = list(map(int, input().split()))
    e = [i + 1 for i in range(c)]
    a.kthPermutation(e, d - 1)
