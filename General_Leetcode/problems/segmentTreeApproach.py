class NumArray:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        n = len(nums)
        self.tree = [0] * (2 * n)
        self.n = n
        self.buildTree(nums)

    def buildTree(self, nums):
        # Build the segment tree
        n = self.n
        # Fill the leaves of the tree
        for i in range(n):
            self.tree[n + i] = nums[i]
        # Build the internal nodes
        for i in range(n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        # Update the value at index and propagate the change
        pos = index + self.n
        self.tree[pos] = val
        while pos > 1:
            pos //= 2
            self.tree[pos] = self.tree[2 * pos] + self.tree[2 * pos + 1]

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        # Calculate the sum in the range [left, right]
        left += self.n
        right += self.n
        summation = 0
        while left <= right:
            if left % 2 == 1:
                summation += self.tree[left]
                left += 1
            if right % 2 == 0:
                summation += self.tree[right]
                right -= 1
            left //= 2
            right //= 2
        return summation
