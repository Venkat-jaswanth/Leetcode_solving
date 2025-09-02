class Solution:
    def maxProdSubArray(self, nums):
        
        neg_digits,zero = self.countNegatives(nums)
        print(zero)
        if neg_digits % 2 == 0 and zero == 0:
            product = 1
            print('here')
            for i in range(len(nums)):
                product *= nums[i]
            return product  
        else:
            product = 1
            max1 = -float('inf')
            for i in range(len(nums)):
                product *= nums[i]
                max1 = max(product,max1)
                product = 1 if product == 0 else product
            product = 1
            for i in range(len(nums)-1,-1,-1):
                product *= nums[i]
                max1 = max(product,max1)
                product = 1 if product == 0 else product
            return max1
    def countNegatives(self, arr):
        count = 0
        zero = 0
        for i in range(len(arr)):
                if arr[i] < 0:
                    count += 1
                elif arr[i] == 0:
                    zero = 1
        return count,zero
    
if __name__ == '__main__':
    s = Solution()
    # take input
    nums = list(map(int, input().strip().split()))
    print(s.maxProdSubArray(nums))