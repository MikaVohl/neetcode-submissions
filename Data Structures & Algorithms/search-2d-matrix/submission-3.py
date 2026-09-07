class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # determine which row its in. Binary search on rows
        # if we compare using row[0] then we want to see the greatest i such that matrix[i][0] <= target
        n_rows = len(matrix)
        start = 0
        end = n_rows-1
        while start < end:
            middle = (end - start) // 2 + start
            if matrix[middle][0] <= target <= matrix[middle][-1]:
                start = end = middle
                break
            if matrix[middle][0] > target:
                end = middle - 1
            else:
                start = middle + 1
        
        row = matrix[start]
        start = 0
        end = len(row) - 1
        while start < end:
            middle = (end - start) // 2 + start
            if row[middle] == target:
                return True
            elif row[middle] < target:
                start = middle + 1
            else:
                end = middle
        return row[start] == target