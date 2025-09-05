class Solution:
    def secretSports(self, arr):
        a_count = arr.count('A')
        b_count = arr.count('B')
        print(a_count, b_count)
        if a_count > b_count and arr[-1] == 'A':
            return 'A'
        elif a_count < b_count and arr[-1] == 'B':
            return 'B'
        else:
            return '?'
        pass



a = int(input())
for _ in range(a):
    n = int(input())
    arr = input()
    print(arr[-1])