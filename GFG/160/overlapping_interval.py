
class Solution:
	def mergeOverlap(self, segments):
            segments.sort(key=lambda x: (x[0], x[1]))
            n = len(segments)
            merged_intervals = []
            total_length = 0
            count = 0
            current_start, current_end = segments[0]
            for start, end in segments[1:]:
                if start <current_end:
                    # Overlapping or contiguous segment; merge it
                    count += 1
                    current_end = max(current_end, end)

                else:
                    # Non-overlapping segment; add current length to total
                    merged_intervals.append((current_start, current_end))
                    current_start, current_end = start, end

            merged_intervals.append((current_start, current_end))
            print(count)
            return merged_intervals


 # Driver Code Starts
if __name__ == '__main__':

    n = int(input())
    # a = list(map(int, input().strip().split()))
    arr = []
    # j = 0
    for i in range(n):
        a = list(map(int, input().strip().split()))
        x = a[0]
        # j += 1
        y = a[1]
        # j += 1
        arr.append([x, y])
    obj = Solution()
    ans = obj.mergeOverlap(arr)
    for i in ans:
        for j in i:
            print(j, end=" ")
    print()

# } Driver Code Ends