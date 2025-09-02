#User function Template for python3

class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr):
        #Your code here
        n = len(arr)
        pos_num = list(range(1, n+2))
        count = 0
        for i in range(n):
            if arr[i] <= 0 or arr[i] > n:
                arr[i] = n + 5
        
        set_arr = set(arr)
        arr = list(set_arr)
        arr.sort()
        # print(arr)
        count = 0
        arr2 = list(set(pos_num) - set(arr))
        return arr2[0]
        # print(arr2)
        # for num in pos_num:
        #     if count == n:
        #         return num
        #     if num != arr[0]:
        #         return num
        #     elif num == arr[0]:
        #         count += 1
        #         arr.pop(0)
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():

        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.missingNumber(arr))


if __name__ == "__main__":
    main()

# } Driver Code Ends