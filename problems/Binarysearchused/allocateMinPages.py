class Solution:
    # Function to find the minimum number of pages
    def findPages(self, arr, k):
        """
        arr: List of integers where arr[i] represents pages in the ith book.
        k: Number of students.
        Returns: Minimum number of maximum pages assigned to any student.
        """

        # If the number of books is less than the number of students, allocation is not possible
        if len(arr) < k:
            return -1

        # Initialize the binary search range:
        # - 'low' is the maximum value in the array because at least one student will get the largest book.
        # - 'high' is the sum of all pages since one student could theoretically get all books.
        low = max(arr)  # Minimum possible maximum pages
        high = sum(arr)  # Maximum possible maximum pages

        # Variable to store the result (minimum of the maximum pages).
        result = high

        # Binary search to find the optimal allocation
        while low <= high:
            # Midpoint of the current range
            mid = (low + high) // 2

            # Check if it's possible to allocate books such that the maximum pages per student is 'mid'
            if self.isPossible(arr, k, mid):
                # If it's possible, update the result and try for a smaller maximum
                result = mid
                high = mid - 1
            else:
                # If not possible, increase the maximum allowed pages
                low = mid + 1

        # Return the best (minimum) result found
        return result

    # Helper function to check if allocation is possible with the given maximum pages
    def isPossible(self, arr, k, maxPages):
        """
        arr: List of integers representing the pages in each book.
        k: Number of students.
        maxPages: The maximum pages any student is allowed to receive.
        Returns: True if allocation is possible, False otherwise.
        """

        # Initialize the number of students needed and the current sum of pages for the first student
        students = 1  # Start with one student
        currentPages = 0  # Pages assigned to the current student

        # Iterate through each book
        for pages in arr:
            # If adding this book to the current student's allocation exceeds maxPages
            if currentPages + pages > maxPages:
                # Assign books to a new student
                students += 1
                currentPages = pages  # Start the new student's allocation with this book

                # If the number of students exceeds 'k', allocation is not possible
                if students > k:
                    return False
            else:
                # Otherwise, add this book to the current student's allocation
                currentPages += pages

        # If we complete the loop without exceeding 'k' students, allocation is possible
        return True




#{ 
 # Driver Code Starts
#Initial Template for Python 3
import bisect
#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.findPages(A, D)
        print(ans)
        print("~")

# } Driver Code Ends