

class Solution:

    # def func(self, arr):
    #     n = len(arr)
    #     max_value = 0
        
    #     # Precompute max_arr and min_arr
    #     max_arr = [[0] * n for _ in range(n)]
    #     min_arr = [[0] * n for _ in range(n)]
        
    #     for i in range(n):
    #         max_arr[i][i] = arr[i]
    #         min_arr[i][i] = arr[i]
    #         for j in range(i + 1, n):
    #             max_arr[i][j] = max(max_arr[i][j - 1], arr[j])
    #             min_arr[i][j] = min(min_arr[i][j - 1], arr[j])
        
    #     # Calculate the max product of max and min
    #     for i in range(n - 1):
    #         for j in range(i + 1, n):
    #             max_value = max(max_value, max_arr[i][j] * min_arr[i][j])
        
    #     return max_value
    def func(self, arr):
        n = len(arr)
        max_value = 0
        for i in range(n-1):
            max_value = max(max_value, arr[i]*arr[i+1])
        return max_value
if __name__ == "__main__":
    
    a = int(input())
    for _ in range(a):
        b = int(input())
        arr = []
        arr = list(map(int, input().split()))
        obj = Solution()
        print(obj.func(arr))
#