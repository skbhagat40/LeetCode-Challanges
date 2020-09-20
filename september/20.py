"""
On a 2-dimensional grid, there are 4 types of squares:

1 represents the starting square.  There is exactly one starting square.
2 represents the ending square.  There is exactly one ending square.
0 represents empty squares we can walk over.
-1 represents obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.
"""
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        # count 0s and head
        head = None
        c = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    head = [(i, j)]
                elif grid[i][j] == 0:
                    c += 1
        def get_children(i, j):
            mods = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            res = []
            for r, c in mods:
                if i+r >= 0 and i+r<len(grid) and j+c >= 0 and j+c < len(grid[0]) and grid[i+r][j+c] != -1:
                    res.append((i+r, j+c))
            return res
        all_paths = [head]
        ans = 0
        while len(all_paths):
            top = all_paths.pop(0)
            h = top[-1]
            if grid[h[0]][h[1]] == 2 and len(top) == c+2:
                ans += 1
            for child in get_children(*h):
                if child not in top:
                    all_paths.append(top + [child])
        return ans
