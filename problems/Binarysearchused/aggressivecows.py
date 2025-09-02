#User function Template for python3


class Solution:

    def aggressiveCows(self, stalls, k):
        stalls.sort()
        if k == 2:
            return stalls[-1] - stalls[0]
        n = len(stalls)
        low = 0
        high = stalls[-1] - stalls[0]
        while low < high:
            mid = (low + high) // 2
            if self.isPossible(mid, k, n, stalls):
                low = mid + 1
            else:
                high = mid
        return low - 1


    
    def isPossible(self, mid, k, n, stalls):
        cows = 1
        last = stalls[0]
        for i in range(1, n):
            if stalls[i] - last >= mid:
                cows += 1
                last = stalls[i]
        print(cows)
        return cows >= k

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import bisect
#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.aggressiveCows(A, D)
        print(ans)
        print("~")
# } Driver Code Ends


# another approach
class Solution:
    def aggressiveCows(self, stalls, k):
        # Sort the stall positions
        stalls.sort()
        
        # Helper function to check if we can place cows with at least 'dist' distance apart
        def canplacecows(dist):
            count = 1  # Place the first cow in the first stall
            last_pos = stalls[0]
            
            for i in range(1, len(stalls)):
                if stalls[i] - last_pos >= dist:
                    count += 1
                    last_pos = stalls[i]
                    if count == k:  # All cows placed
                        return True
            return False
        
        # Binary search for the largest minimum distance
        low, high = 0, stalls[-1] - stalls[0]
        result = 0
        
        while low <= high:
            mid = (low + high) // 2
            if canplacecows(mid):
                result = mid  # Update result as this distance is feasible
                low = mid + 1  # Try for a larger distance
            else:
                high = mid - 1  # Try for a smaller distance
        
        return result


# Driver Code
if __name__ == '__main__':
    t = int(input("Number of test cases: "))
    while t:
        t -= 1
        A = [int(x) for x in input("Stalls array: ").strip().split()]
        D = int(input("Number of cows: "))
        ob = Solution()
        ans = ob.aggressiveCows(A, D)
        print("Maximum minimum distance:", ans)
        print("~")
