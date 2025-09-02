
class Solution:
	def insertInterval(self, segments, newEvent):
            segments.append(newEvent)
            segments.sort(key=lambda x: (x[0], x[1]))
            n = len(segments)
            merged_intervals = []
            total_length = 0
            count = 0
            current_start, current_end = segments[0]
            for start, end in segments[1:]:
                if start <=current_end:
                    # Overlapping or contiguous segment; merge it
                    count += 1
                    current_end = max(current_end, end)

                else:
                    # Non-overlapping segment; add current length to total
                    merged_intervals.append((current_start, current_end))
                    current_start, current_end = start, end

            merged_intervals.append((current_start, current_end))
            # print(count)
            return merged_intervals



if __name__ == '__main__': 

    N = int(input())
    intervals = [list(map(int, input().split())) for i in range(N)]
    newEvent = list(map(int, input().split()))
    ob = Solution()
    res = ob.insertInterval(intervals, newEvent)
    print('[', end = '')
    for i in range(len(res)):
        print('[', end = '')
        print(str(res[i][0])+','+str(res[i][1]), end = '')
        print(']', end = '')
        if i < len(res)-1:
            print(',', end='')
    print(']')
    print("~")
# } Driver Code Ends
# } Driver Code Ends