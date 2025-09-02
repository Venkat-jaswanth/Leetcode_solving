class Solution:
    def subarraySum(self, nums, k):

        i=0
        j=1
        n = len(nums)
        if n == 1:
            return 1 if nums[0]==k else 0   
        res = 0
        temp = nums[i]
        while i<j and j<n:
            if temp == k:
                res+=1
            temp += nums[j]
            while temp<k and nums[i]<0 and i<j :
                temp -= nums[i]
                i+=1
            while temp>k and i<j:
                temp -= nums[i]
                i+=1
            
            j+=1
        if temp == k:
                res+=1
        while i<j-1:
            temp -= nums[i]
            i+=1
            if temp == k:
                res+=1
        return res
    
# testcases   

sol = Solution()
print(sol.subarraySum([0,0], 0)) # 3
