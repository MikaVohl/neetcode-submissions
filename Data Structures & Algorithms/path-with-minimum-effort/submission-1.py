class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        visited = set()
        d = []
        heapq.heapify(d)
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        heapq.heappush(d, (0, 0, 0))
        ROW, COL = len(heights), len(heights[0])

        while d:
            cost, r, c = heapq.heappop(d)
            if (r, c) in visited: continue
            if r == ROW - 1 and c == COL - 1:
                return cost
            visited.add((r, c))
            for dr, dc in dirs:
                if min(dr + r, dc + c) < 0 or dr + r >= ROW or dc + c >= COL: continue
                heapq.heappush(d, (max(cost, abs(heights[r][c] - heights[r+dr][c+dc])), r + dr, c + dc))
            
