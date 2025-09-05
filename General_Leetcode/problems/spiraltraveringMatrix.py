class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it. Return the number of nice sub-arrays
        # The number of nice sub-arrays is the number of sub-arrays with at most k odd numbers minus the number of sub-arrays with at most k-1 odd numbers
        def atMostK(nums, k):
            # Use a hashmap to store the number of sub-arrays with at most i odd numbers
            seen = {0: 1}
            count = 0
            odd_count = 0
            for num in nums:
                if num % 2 == 1:
                    odd_count += 1
                # Check if the current number of odd numbers is greater than k
                if odd_count - k in seen:
                    count += seen[odd_count - k]
                # Update the count of the current number of odd numbers in the hashmap
                if odd_count in seen:
                    seen[odd_count] += 1
                else:
                    seen[odd_count] = 1
            return count
        



obj = Solution()
mat = [26,19,11,14,18,4,7,1,30,23,19,8,10,6,26,3]
print(obj.minSubarray(mat,26))