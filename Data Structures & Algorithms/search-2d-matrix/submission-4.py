class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        start = 0
        end = ROWS * COLS - 1

        while start < end:
            middle = (start + end) // 2
            row = middle // COLS
            col = middle % COLS
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                end = middle - 1
            else:
                start = middle + 1
        return matrix[start // COLS][start % COLS] == target