class Solution:
    def lenLongestFibSubseq(self, sequence):
        if len(sequence) <= 2:
            return 0

        index_by_value = {num: i for i, num in enumerate(sequence)}
        print(index_by_value)
        longest_fib_length = 0

        for i in range(len(sequence)):
            for j in range(i + 1, len(sequence)):
                first, second = sequence[i], sequence[j]
                current_length = 2
                while first + second in index_by_value:
                    next_value = first + second
                    first, second = second, next_value
                    current_length += 1
                    longest_fib_length = max(longest_fib_length, current_length)

        return longest_fib_length if longest_fib_length > 2 else 0
obj = Solution()
print(obj.lenLongestFibSubseq([1,2,3,4,5,6,7,8])) # 5