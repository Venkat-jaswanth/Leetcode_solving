from typing import List
from collections import defaultdict

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        frequency = defaultdict(int)
        total_numbers = len(nums)
        
        for start_index in range(total_numbers - k + 1):
            unique_numbers = set(nums[start_index:start_index + k])
            for number in unique_numbers:
                frequency[number] += 1
        
        missing_numbers = [number for number, count in frequency.items() if count == 1]
        
        return max(missing_numbers) if missing_numbers else -1

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    nums = [3, 9, 2, 1, 7]
    k = 3
    print(solution.largestInteger(nums, k))  # Expected output: 7
