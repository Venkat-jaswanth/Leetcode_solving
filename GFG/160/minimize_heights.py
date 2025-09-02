#User function Template for python3


class Solution:
    def getMinDiff(self, arr,k):
        arr.sort()
        inti_diff = arr[-1] - arr[0]
        min_diff = inti_diff
        for i in range(len(arr)-1):
            min_ele = min(arr[0]+k, arr[i+1]-k)
            max_ele = max(arr[-1]-k, arr[i]+k)
            if min_ele < 0:
                continue
            min_diff = min(min_diff, max_ele - min_ele)
            
        return min_diff



#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        # n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMinDiff(arr, k)
        print(ans)
        tc -= 1

# } Driver Code Ends