class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # make prefix sums for rows
        for row in range(len(matrix)):
            for col in range(1, len(matrix[0])):
                matrix[row][col] = matrix[row][col - 1] + matrix[row][col]
                
        # make prefix sums for regions
        for row in range(1, len(matrix)):
            for col in range(len(matrix[0])):
                matrix[row][col] = matrix[row][col] + matrix[row - 1][col]
        self.matrix = matrix
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        current_region_sum = self.matrix[row2][col2]
        origin = self.matrix[row1 - 1][col1 - 1] if row1 != 0 and col1 != 0 else 0
        left_region_sum = self.matrix[row2][col1 - 1] if col1 != 0 else 0
        top_region_sum = self.matrix[row1 - 1][col2] if row1 != 0 else 0
        return current_region_sum - top_region_sum - left_region_sum + origin
    
    
    
# better
class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        zeros = [0] * (len(matrix[0])+1)
        self.matrixpre = [zeros]
        for i, row in enumerate(matrix):
            total = 0
            self.matrixpre.append([])
            self.matrixpre[-1].append(0)
            for j, nu in enumerate(row):
                total += nu 
                self.matrixpre[-1].append(total+self.matrixpre[-2][j+1])

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.matrixpre[row2+1][col2+1] - self.matrixpre[row1][col2+1] - self.matrixpre[row2+1][col1] + self.matrixpre[row1][col1]
    
    
# for future usage

#     def prefixSum(self, nums):
        # prefix = [0] * (len(nums))
        # prefix[0] = nums[0]
        # for i, num in enumerate(nums):
        #     if i == 0:
        #         continue
        #     prefix[i] = prefix[i - 1] + num
        # return prefix