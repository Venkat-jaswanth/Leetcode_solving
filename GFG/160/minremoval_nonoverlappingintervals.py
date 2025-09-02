#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def minRemoval(self, segments):
        # Code here
        if not segments:
            return 0

        # Sort intervals by end point
        segments.sort(key=lambda x: x[1])
    
        # Initialize the count of intervals to remove
        count_removed = 0
        last_end = segments[0][1]
    
        # Iterate over the remaining intervals
        for start, end in segments[1:]:
            if start < last_end:
                # If the current interval overlaps, increment the removal count
                count_removed += 1
            else:
                # If no overlap, update the last_end to the current interval's end
                last_end = end
    
        return count_removed

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        intervals = [list(map(int, input().split())) for i in range(N)]
        ob = Solution()
        res = ob.minRemoval(intervals)
        print(res)
        print("~")
# } Driver Code Ends