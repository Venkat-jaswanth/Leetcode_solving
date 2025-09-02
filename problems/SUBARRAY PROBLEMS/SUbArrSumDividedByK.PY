class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix = {0: 1}
        count = 0
        current_sum = 0
        for num in nums:
            current_sum = (current_sum+num)%k
            if current_sum<0:
                current_sum += k
            if current_sum in prefix:
                count += prefix[current_sum]
                prefix[current_sum] += 1
            else:
                prefix[current_sum] = 1
        return count